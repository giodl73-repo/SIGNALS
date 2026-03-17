---
skill: flow-lifecycle
round: 10
date: 2026-03-15
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v9-2026-03-15.md
---

# flow-lifecycle -- Round 10 Variations

Round 10 holds the R9 V-05 full floor and probes the two guarantees that C-26 requires of
the AC-13 meta-registry: (a) complete enumeration of all current canonical per-row quality
artifacts, and (b) forward protection when the template is extended with a novel artifact.

R9 V-05 introduced AC-13, naming three canonical per-row quality artifacts in the Pass
Condition cell. This satisfies the basic C-26 test (registry present, named, scan per-artifact).
But three structural gaps remain:

| Gap | What R9 V-05 does | What C-26 needs |
|-----|-------------------|-----------------|
| Registry form | AC-13 prose list inside OAC cell | Structured registry that makes additions visible |
| Update policy | "Three canonical" -- static, closed | Live trigger: new artifact = mandatory registry update |
| Completeness proof | Author asserts 3 | Boundary scan discovers all qualifying artifacts |

The R10 failure modes to probe:

| Mode | Tested by | What is present | What is missing |
|------|-----------|-----------------|-----------------|
| Static registry (no update trigger) | V-01 | AC-13 names 3 | No update policy; "canonical" closes the list |
| Unstructured registry (prose in AC cell) | V-02 | 3 artifacts named | No PQAR table; additions invisible without re-reading prose |
| Asserted completeness (no discovery) | V-03 | AC-13 claims coverage | No boundary scan; Bottleneck Register Root Cause format may qualify undetected |
| No meta-structure without meta-table | V-04 | V-01 + V-03 | Structured PQAR table absent |
| Full C-26 floor | V-05 | All three combined | -- |

Single-axis: V-01 (live update policy), V-02 (PQAR registry table), V-03 (boundary scan).
Combined: V-04 (V-01 + V-03), V-05 (all three + R9 V-05 floor).

**Round 10 hypothesis matrix:**

| Variation | Update Policy | PQAR Table | Boundary Scan | Primary Test |
|-----------|:------------:|:----------:|:-------------:|-------------|
| V-01 | TARGET | NONE | NONE | Open-ended live registry with explicit update trigger |
| V-02 | NONE | TARGET | NONE | Structured PQAR table as dedicated registry section |
| V-03 | NONE | NONE | TARGET | Discover all per-row quality artifacts before declaring registry |
| V-04 | TARGET | NONE | TARGET | Update policy + boundary scan; no structured table |
| V-05 | TARGET | TARGET | TARGET | Full C-26 floor; maximum registry integrity |

---

## V-01 -- Axis: Lifecycle Emphasis (Live Registry with Update Policy)

**Variation axis:** Lifecycle emphasis -- AC-13 is upgraded from a static "three canonical"
enumeration to a LIVE registry with an explicit update trigger. The phrase "three canonical
per-row quality artifacts" is replaced with: "All per-row quality artifacts currently registered
in this model (initial set: Phase Delta Block, Constraint Chain Table, Constraint-Incumbent Gap
Analysis)." A mandatory update policy is declared inside AC-13: "If any phase authoring or
optional section introduces a new structural artifact with per-row quality requirements (a
severity column, rationale column, compliance flag, or equivalent), the author must add that
artifact to this AC-13 entry before continuing. Silent omission is a fail." The Coverage Scan
AC-13 row must confirm: (a) registry was not extended during authoring without a new entry;
(b) each registered artifact passes C-25 parity individually; (c) no per-row quality artifact
exists in the final model that is absent from the registry.

**Hypothesis:** R9 V-05 hardcodes "three canonical" -- this closes the list and prevents
forward protection. A model that introduces a fourth per-row quality artifact (e.g., adds a
Severity column to the Edge Case Catalog, or authors a Risk Register) can pass all per-artifact
ACs and AC-13 silently because "three canonical" was the declared scope. The live update
policy removes that closure: any new artifact triggers a registry update obligation, and the
Coverage Scan AC-13 row must confirm no artifact evaded the registry. Expected: C-26 PASS for
the initial three artifacts; forward protection activated by the update trigger clause.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

Before any artifact is authored: (1) declare the status-quo process as a named competitor,
(2) declare the output acceptance criteria by ID including all C-24 sub-conditions, per-column
sub-conditions for Phase Delta Block and Constraint Chain Table quality, and AC-13 as a LIVE
meta-registry with an explicit update trigger policy, (3) register the constraint chain with
explicit incumbent coverage flags. Every artifact carries incumbent comparison fields. Phase
contracts import and export named constraints by CC-ID. Exception flows caused by constraint
import failures are traced bidirectionally in a dedicated Constraint-Break Exceptions subsection.
The cross-axis bridge is synthesized in a severity-rated, rationale-equipped Constraint-Incumbent
Gap Analysis section verified by a pre-declared five-condition acceptance check. Phase Delta
Blocks and the Constraint Chain Table carry inline column-level quality constraints. If any new
per-row quality artifact is introduced during authoring, AC-13 must be updated before continuing.

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
| AC-10 | Constraint chain completeness and quality | (a) every CC-ID exported in a phase appears as imported in the designated consuming phase; (b) every Handoff Strength cell in CCT is STRONG, WEAK, or ABSENT-with-justification -- blank or unrecognized value is a fail; (c) every `Incumbent Models?` cell in CCT is Y, N, or ABSENT-with-justification -- blank is a fail | Any CC-ID with no consuming import; blank or invalid Handoff Strength cell; blank or invalid Incumbent Models? cell in CCT |
| AC-11 | Constraint-break exception tagging | Exception Catalog has dedicated Constraint-Break Exceptions subsection with 5-column schema; every CC-ID break has E-ID; every E-ID traces to valid CC-ID and main catalog | Subsection absent or prose-only; entry missing required column; CC-ID break unrepresented; E-ID with invalid CC-ID |
| AC-12 | C-24 gap analysis completeness | (a) Constraint-Incumbent Gap Analysis is a named structural section in Inertia Summary; (b) every CC-ID with `Incumbent Models? = N` appears as one row; (c) each row carries `Gap Severity (HIGH/MED/LOW)`; (d) each row carries `Why As-Is Fails` naming a specific process characteristic; (e) no blank cells in `Incumbent Models?` in CCR or CCT | Section absent; N-tagged CC-ID without row; row missing severity; row with generic or absent rationale; blank `Incumbent Models?` cell anywhere |
| AC-13 | Per-row quality artifact meta-registry (LIVE) | All per-row quality artifacts currently registered in this model (initial set: Phase Delta Block, Constraint Chain Table, Constraint-Incumbent Gap Analysis). UPDATE POLICY: if any phase or optional section introduces a new structural artifact with per-row quality requirements (severity column, rationale column, compliance flag, or equivalent), add that artifact to this entry before continuing -- silent omission is a fail. Coverage Scan must confirm: (a) no per-row quality artifact in the final model is absent from this registry; (b) each registered artifact passes C-25 schema-AC parity with per-sub-condition evidence; (c) the registry was not closed prematurely -- if the authored model contains a per-row quality artifact not listed above, name it here | Any per-row quality artifact absent from registry; bulk C-25 attestation without per-artifact enumeration; new artifact introduced after authoring start without registry update |

These thirteen checks are the acceptance definition. AC-13 is the LIVE C-26 meta-registry.
The Coverage Scan AC-13 row must confirm sub-conditions (a)-(b)-(c) individually and name any
artifact discovered outside the initial set. AC-04 sub-conditions (a)-(b)-(c) and AC-10
sub-conditions (a)-(b)-(c) must be confirmed individually. AC-12 sub-conditions (a)-(e)
must be confirmed individually.

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

**PHASE DELTA BLOCK REQUIREMENT** *(feeds AC-04)*

Each lifecycle phase contains a mandatory Phase Delta Block, authored BEFORE the State Table.
Quality constraints are embedded inline in each column header -- not in notes below the table.

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed -- any other value is a fail) | Impact Severity (HIGH / MED / LOW -- HIGH or MED requires FM trace or "New gap" note; blank is a fail) |
|-------|----------------------|-------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|

- If no divergences exist: explicit no-divergence row required (write "No divergence" in Current Process Step)

---

**DELTA CROSS-REFERENCE REQUIREMENT** *(feeds AC-03)*

Five artifacts carry `Delta Ref (DL-ID or NONE)` (exact name):
State Trace / Exception Catalog / Edge Case Catalog / Bottleneck Register / Gap Register.

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
N entries must appear in the Constraint-Incumbent Gap Analysis. Update this registry if new
constraints are identified during phase authoring.

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

**PHASE DELTA BLOCK [Ph-ID: Phase Name]** -- AUTHOR BEFORE STATE TABLE *(feeds AC-04)*

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
| Exported constraints | [CC-IDs this phase exports. Format: CC-NN: [constraint name and verified state].] |
| Constraint export gap | [Constraint that should export but cannot be verified; or NONE] |
| Incumbent exit | [How the incumbent transitions out -- or ABSENT] |

---

*Repeat for each phase. Update Constraint Chain Registry with any new CC-IDs discovered.*

---

**CONSTRAINT CHAIN TABLE** *(finalized after all phases -- feeds AC-10, AC-12)*

| CC-ID | Constraint Name | From Ph-ID | Exported As | To Ph-ID | Imported As | Verification Method | Handoff Strength (STRONG / WEAK / ABSENT -- ABSENT requires justification note; blank is a fail) | Incumbent Models? (Y / N / ABSENT-with-justification -- blank is a hard fail) |
|-------|-----------------|-----------|-------------|---------|-------------|---------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| CC-01 | | | | | | | | |

At least one STRONG Handoff Strength required. ABSENT requires an explicit justification note
in the same cell (e.g., "ABSENT -- handoff dropped; downstream phase receives stale data").

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

Bidirectional traceability rules: every CC-ID break must appear as at least one E-ID here;
every E-ID here must trace to valid CC-ID and main Exception Catalog. Phase-of-Origin is the
importing phase where violation occurred. Check V audits these rules. Resolve before output.

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

Root Cause format: `Phase Delta [Ph-ID] [DL-ID] -- Current Process Step: [value]`
or: `Phase Exit Gate [Ph-ID] -- Blocked by: [value]`

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

**COVERAGE SCAN** *(executes AC-01 through AC-13 plus Check V)*

For each AC-ID, record PASS or FAIL with enumerated evidence. Do NOT restate pass conditions.
AC-04 must confirm sub-conditions (a)-(b)-(c) individually. AC-10 must confirm sub-conditions
(a)-(b)-(c) individually. AC-12 must confirm sub-conditions (a)-(e) individually. AC-13 must
confirm sub-conditions (a)-(b)-(c) individually -- name any per-row quality artifact discovered
outside the initial registered set.

| AC-ID | Result | Evidence or Failure Detail |
|-------|--------|---------------------------|
| AC-01 | | [S-IDs checked; failures named] |
| AC-02 | | [paths and E-IDs checked; open-ended named] |
| AC-03 | | [artifacts and row counts; blank cells named] |
| AC-04 | | [(a) block order per phase confirmed; (b) Divergence Type values enumerated -- non-enumerated named; (c) Impact Severity values enumerated -- HIGH/MED FM-trace confirmed] |
| AC-05 | | [decisions and state owners; generic labels named] |
| AC-06 | | [E-IDs checked; most-dense phase with DL-ID] |
| AC-07 | | [phases; missing contract or gate named] |
| AC-08 | | [registers; Root Cause format confirmed] |
| AC-09 | | [per-artifact incumbent field completeness; blanks named] |
| AC-10 | | [(a) chain completeness per CC-ID; (b) Handoff Strength values enumerated -- blanks or invalid named; (c) Incumbent Models? values in CCT enumerated -- blanks named] |
| AC-11 | | [subsection present? each entry has CC-ID + Ph-ID? every CC-ID break has E-ID? every E-ID traces to valid CC-ID?] |
| AC-12 | | [(a) section named? (b) all N-tagged CC-IDs have rows? (c) each row has Gap Severity? (d) each row has specific rationale? (e) no blank Incumbent Models? cells in CCR or CCT?] |
| AC-13 | | [(a) all per-row quality artifacts in final model named -- any outside initial set? (b) each registered artifact: Phase Delta Block C-25 parity confirmed (schema inline + AC-04 sub-conditions + scan per-sub-condition); Constraint Chain Table C-25 parity confirmed (schema inline + AC-10 sub-conditions + scan per-sub-condition); Gap Analysis C-25 parity confirmed (schema inline + AC-12 sub-conditions + scan per-sub-condition); (c) no registry closed prematurely -- any artifact introduced after authoring start listed here] |

**Check V -- Constraint-Break bidirectional traceability:**

(a) For every CC-ID with a known break: confirm it appears as at least one E-ID in the subsection.
(b) For every E-ID in the subsection: confirm CC-ID Violated exists in Constraint Chain Table.
(c) For every E-ID in the subsection: confirm it also exists in the main Exception Catalog.

Any FAIL must be corrected before output. Self-attestation is not acceptable.

---

**INERTIA SUMMARY**

| Item | Count / Detail |
|------|---------------|
| Exceptions incumbent cannot detect (As-Is Detection? = N) | [list E-IDs] |
| Edge cases incumbent cannot handle (As-Is Handled? = N) | [list EC-IDs] |
| Terminals incumbent leaves open-ended (Incumbent Terminal? = N) | [list T-IDs] |
| Roles absent from incumbent | [list R-IDs] |
| Gaps invisible to incumbent (Incumbent Awareness = N) | [list G-IDs] |
| Known failure modes addressed | [FM-1/FM-2/FM-3 closed by which artifacts] |

**Constraint-Incumbent Gap Analysis** *(required when any CC-ID has `Incumbent Models? = N` -- feeds AC-12)*

One row per CC-ID where `Incumbent Models? = N`. Explicit NONE with justification if none.

Gap Severity criteria:
- HIGH: governs critical-path or financial-close; absence causes material risk or compliance exposure
- MED: governs recommended guard condition; absence causes rework, escalation, or increased errors
- LOW: governs nice-to-have check; absence causes minor inefficiency

`Why As-Is Fails` must name a specific process characteristic. Generic language ("not implemented",
"lacking") is a fail for this column.

| CC-ID | Constraint Name | Gap Severity (HIGH/MED/LOW) | Why As-Is Fails |
|-------|-----------------|----------------------------|-----------------|
| [CC-ID where N] | | | [specific named process characteristic] |

---

**FINAL AUTHORING CHECK**

Before writing output:
- [ ] STATUS-QUO PROCESS DECLARATION is the first section
- [ ] OUTPUT ACCEPTANCE CRITERIA is second with AC-01 through AC-13 all declared
- [ ] AC-13 is LIVE: open-ended registry with update trigger policy declared
- [ ] AC-04 enumerates sub-conditions (a)-(b)-(c) for Phase Delta Block quality
- [ ] AC-10 enumerates sub-conditions (a)-(b)-(c) for CCT quality fields
- [ ] CONSTRAINT CHAIN REGISTRY authored before any phase; no blank `Incumbent Models?` cells
- [ ] Status-Quo Role Comparison is dedicated (not embedded in Domain Role Registry)
- [ ] Every phase: Entry Contract with `Imported constraints` + `Incumbent entry`
- [ ] Every phase: Phase Delta Block with inline column-level quality constraints
- [ ] Every phase: Exit Gate with `Exported constraints` + `Incumbent exit`
- [ ] All five artifacts carry `Delta Ref (DL-ID or NONE)` column (exact name)
- [ ] Constraint-Break Exceptions: formal 5-column table; Check V confirmed
- [ ] Constraint Chain Table: inline quality bars for Handoff Strength + Incumbent Models?
- [ ] Gap Analysis: both `Gap Severity` and `Why As-Is Fails` columns; one row per N-tagged CC-ID
- [ ] If any new per-row quality artifact was introduced during authoring: AC-13 updated
- [ ] Coverage Scan: AC-01 through AC-13 + Check V; AC-04, AC-10, AC-12, AC-13 sub-conditions confirmed individually

**OUTPUT:** Write to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Status-Quo Process Declaration > Output Acceptance Criteria > Domain Role Registry >
Status-Quo Role Comparison > Phase Index > Constraint Chain Registry > Phases (Entry Contract +
Phase Delta Block + State Table + Decision Table + Parallel Path + Exit Gate per phase) >
Constraint Chain Table > Terminal Declaration > Exception Catalog (with Constraint-Break
Exceptions subsection) > Edge Case Catalog > Bottleneck Register > Gap Register > Cross-Process
Handoff (optional) > SLA Annotation (optional) > Coverage Scan (AC-01--AC-13 + Check V) >
Inertia Summary (with Constraint-Incumbent Gap Analysis).

---

## V-02 -- Axis: Output Format (Structured PQAR Registry Table)

**Variation axis:** Output format -- AC-13 is restructured as a pointer to a dedicated
PER-ROW QUALITY ARTIFACT REGISTRY (PQAR) section. This section appears between the OUTPUT
ACCEPTANCE CRITERIA and the INCUMBENT COVERAGE MANDATE and contains a formal table with
columns: Reg-ID, Artifact Name, Per-Row Quality Columns, Corresponding AC-ID, Sub-conditions
Declared. The AC-13 row in the OAC table says: "See PER-ROW QUALITY ARTIFACT REGISTRY below.
Coverage Scan must verify each Reg-ID individually." The PQAR table format makes additions
structurally visible -- adding a new per-row quality artifact requires inserting a row, which
is auditable at a glance. No update-trigger policy is added in prose; the structured form
provides the forward-protection mechanism. The Coverage Scan AC-13 row must name each Reg-ID
and confirm C-25 parity for each.

**Hypothesis:** R9 V-05 embeds the registry as prose inside the AC-13 cell. A prose list
is opaque -- you must re-read the full cell to detect an omission, and adding a new artifact
means editing a dense paragraph. A PQAR table makes completeness auditable in O(1): count
the rows. The table form also makes the "corresponding AC-ID" explicit and scannable without
reading prose. Expected: C-26 PASS with stronger structural forward-protection than V-01
prose list; but no explicit update-trigger policy may leave the policy gap open if a model
author ignores the table structure.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

Before any artifact is authored: (1) declare the status-quo process as a named competitor,
(2) declare the output acceptance criteria by ID including all C-24 sub-conditions, per-column
sub-conditions for Phase Delta Block and Constraint Chain Table quality, and AC-13 as a pointer
to a dedicated PER-ROW QUALITY ARTIFACT REGISTRY table, (3) register the constraint chain with
explicit incumbent coverage flags. Every artifact carries incumbent comparison fields. Phase
contracts import and export named constraints by CC-ID. Exception flows caused by constraint
import failures are traced bidirectionally in a dedicated Constraint-Break Exceptions subsection.
The cross-axis bridge is synthesized in a severity-rated, rationale-equipped Constraint-Incumbent
Gap Analysis section verified by a pre-declared five-condition acceptance check. Phase Delta
Blocks and the Constraint Chain Table carry inline column-level quality constraints. The
PER-ROW QUALITY ARTIFACT REGISTRY is the authoritative list of all per-row quality artifacts;
any new artifact introduced during authoring must appear as a new row in that table.

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
| AC-10 | Constraint chain completeness and quality | (a) every CC-ID exported in a phase appears as imported in the designated consuming phase; (b) every Handoff Strength cell in CCT is STRONG, WEAK, or ABSENT-with-justification -- blank or unrecognized value is a fail; (c) every `Incumbent Models?` cell in CCT is Y, N, or ABSENT-with-justification -- blank is a fail | Any CC-ID with no consuming import; blank or invalid Handoff Strength cell; blank or invalid Incumbent Models? cell in CCT |
| AC-11 | Constraint-break exception tagging | Exception Catalog has dedicated Constraint-Break Exceptions subsection with 5-column schema; every CC-ID break has E-ID; every E-ID traces to valid CC-ID and main catalog | Subsection absent or prose-only; entry missing required column; CC-ID break unrepresented; E-ID with invalid CC-ID |
| AC-12 | C-24 gap analysis completeness | (a) Constraint-Incumbent Gap Analysis is a named structural section in Inertia Summary; (b) every CC-ID with `Incumbent Models? = N` appears as one row; (c) each row carries `Gap Severity (HIGH/MED/LOW)`; (d) each row carries `Why As-Is Fails` naming a specific process characteristic; (e) no blank cells in `Incumbent Models?` in CCR or CCT | Section absent; N-tagged CC-ID without row; row missing severity; row with generic or absent rationale; blank `Incumbent Models?` cell anywhere |
| AC-13 | Per-row quality artifact meta-registry | See PER-ROW QUALITY ARTIFACT REGISTRY section (below). Coverage Scan must verify each Reg-ID row individually: confirm schema inline quality bars present, confirm corresponding AC sub-conditions declared, confirm Coverage Scan row confirms each sub-condition with evidence. Bulk attestation across all Reg-IDs in a single undifferentiated statement is a fail. | Any Reg-ID missing from registry; per-Reg-ID verification omitted; new per-row quality artifact introduced without a new registry row |

These thirteen checks are the acceptance definition. AC-13 points to the PER-ROW QUALITY
ARTIFACT REGISTRY. The Coverage Scan AC-13 row must cite each Reg-ID individually.
AC-04 sub-conditions (a)-(b)-(c), AC-10 sub-conditions (a)-(b)-(c), and AC-12 sub-conditions
(a)-(e) must each be confirmed individually.

---

**PER-ROW QUALITY ARTIFACT REGISTRY** *(canonical registry -- feeds AC-13)*

This table is the authoritative list of all structural artifacts in this model that carry
declared per-row quality requirements. Adding a new structural artifact with a severity column,
rationale column, or compliance flag requires inserting a new row before continuing authoring.

| Reg-ID | Artifact Name | Per-Row Quality Columns | Corresponding AC-ID | Sub-conditions Declared |
|--------|---------------|------------------------|---------------------|------------------------|
| PQAR-01 | Phase Delta Block | Divergence Type (enum), Impact Severity (enum+trace) | AC-04 | (a) block order; (b) Divergence Type values; (c) Impact Severity values + FM trace |
| PQAR-02 | Constraint Chain Table | Handoff Strength (enum+justification), Incumbent Models? (enum+blank-fail) | AC-10 | (a) chain completeness; (b) Handoff Strength values; (c) Incumbent Models? values |
| PQAR-03 | Constraint-Incumbent Gap Analysis | Gap Severity (HIGH/MED/LOW), Why As-Is Fails (specific rationale) | AC-12 | (a) section named; (b) N-tagged CC-IDs have rows; (c) Gap Severity per row; (d) Why As-Is Fails per row; (e) no blank Incumbent Models? |

Coverage Scan AC-13 row must confirm PQAR-01, PQAR-02, and PQAR-03 individually by Reg-ID.

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

Each lifecycle phase contains a mandatory Phase Delta Block, authored BEFORE the State Table.
Quality constraints are embedded inline in each column header -- not in notes below the table.

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed -- any other value is a fail) | Impact Severity (HIGH / MED / LOW -- HIGH or MED requires FM trace or "New gap" note; blank is a fail) |
|-------|----------------------|-------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|

- If no divergences exist: explicit no-divergence row required

---

**DELTA CROSS-REFERENCE REQUIREMENT** *(feeds AC-03)*

Five artifacts carry `Delta Ref (DL-ID or NONE)` (exact name):
State Trace / Exception Catalog / Edge Case Catalog / Bottleneck Register / Gap Register.

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
| Exported constraints | [CC-IDs this phase exports. Format: CC-NN: [constraint name and verified state].] |
| Constraint export gap | [Constraint that should export but cannot be verified; or NONE] |
| Incumbent exit | [How the incumbent transitions out -- or ABSENT] |

---

*Repeat for each phase. Update Constraint Chain Registry and PQAR table if new per-row quality artifacts introduced.*

---

**CONSTRAINT CHAIN TABLE** *(finalized after all phases -- feeds AC-10 / PQAR-02)*

| CC-ID | Constraint Name | From Ph-ID | Exported As | To Ph-ID | Imported As | Verification Method | Handoff Strength (STRONG / WEAK / ABSENT -- ABSENT requires justification note; blank is a fail) | Incumbent Models? (Y / N / ABSENT-with-justification -- blank is a hard fail) |
|-------|-----------------|-----------|-------------|---------|-------------|---------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| CC-01 | | | | | | | | |

At least one STRONG required. ABSENT requires inline justification.

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

**Exception Density Note:** Most-dense Ph-ID + structural rationale + DL-ID citation.

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

Root Cause format: `Phase Delta [Ph-ID] [DL-ID] -- Current Process Step: [value]`
or: `Phase Exit Gate [Ph-ID] -- Blocked by: [value]`

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

**COVERAGE SCAN** *(executes AC-01 through AC-13 plus Check V)*

For each AC-ID, record PASS or FAIL with enumerated evidence. AC-04 sub-conditions (a)-(b)-(c),
AC-10 sub-conditions (a)-(b)-(c), and AC-12 sub-conditions (a)-(e) must be confirmed individually.
AC-13 must verify each PQAR Reg-ID individually -- bulk attestation is a fail.

| AC-ID | Result | Evidence or Failure Detail |
|-------|--------|---------------------------|
| AC-01 | | [S-IDs checked; failures named] |
| AC-02 | | [paths and E-IDs checked; open-ended named] |
| AC-03 | | [artifacts and row counts; blank cells named] |
| AC-04 | | [(a) block order per phase confirmed; (b) Divergence Type values enumerated; (c) Impact Severity values + FM-trace confirmed] |
| AC-05 | | [decisions and state owners; generic labels named] |
| AC-06 | | [E-IDs checked; most-dense phase with DL-ID] |
| AC-07 | | [phases; missing contract or gate named] |
| AC-08 | | [registers; Root Cause format confirmed] |
| AC-09 | | [per-artifact incumbent field completeness; blanks named] |
| AC-10 | | [(a) chain completeness per CC-ID; (b) Handoff Strength values -- blanks named; (c) Incumbent Models? in CCT -- blanks named] |
| AC-11 | | [subsection present? CC-ID+Ph-ID per entry? CC-ID break coverage? E-ID validity?] |
| AC-12 | | [(a)-(e) confirmed individually] |
| AC-13 | | [PQAR-01 (Phase Delta Block): schema inline bars present? AC-04 sub-conditions declared? scan per-sub-condition confirmed? PQAR-02 (Constraint Chain Table): schema inline bars present? AC-10 sub-conditions declared? scan per-sub-condition confirmed? PQAR-03 (Gap Analysis): schema inline? AC-12 sub-conditions? scan per-sub-condition? Any new Reg-ID rows added during authoring?] |

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

Gap Severity: HIGH (critical-path/compliance) / MED (rework/escalation) / LOW (minor inefficiency).
`Why As-Is Fails` must name a specific process characteristic. Generic language is a fail.

| CC-ID | Constraint Name | Gap Severity (HIGH/MED/LOW) | Why As-Is Fails |
|-------|-----------------|----------------------------|-----------------|
| [CC-ID where N] | | | [specific named process characteristic] |

---

**FINAL AUTHORING CHECK**

- [ ] STATUS-QUO PROCESS DECLARATION is the first section
- [ ] OUTPUT ACCEPTANCE CRITERIA is second with AC-01 through AC-13 all declared
- [ ] PER-ROW QUALITY ARTIFACT REGISTRY section present between OAC and INCUMBENT COVERAGE MANDATE
- [ ] PQAR table has PQAR-01, PQAR-02, PQAR-03 with all columns populated
- [ ] AC-13 row in OAC points to PQAR section by name
- [ ] If any new per-row quality artifact introduced: new PQAR row added
- [ ] AC-04 enumerates sub-conditions (a)-(b)-(c); AC-10 enumerates sub-conditions (a)-(b)-(c)
- [ ] Phase Delta Block and CCT schema templates have inline quality bars in column headers
- [ ] CONSTRAINT CHAIN REGISTRY authored before any phase; no blank `Incumbent Models?` cells
- [ ] All five artifacts carry `Delta Ref (DL-ID or NONE)` column
- [ ] Constraint-Break Exceptions: formal 5-column table; Check V confirmed
- [ ] Gap Analysis: both columns; one row per N-tagged CC-ID
- [ ] Coverage Scan: AC-01 through AC-13 + Check V; AC-13 verifies each PQAR Reg-ID individually

**OUTPUT:** Write to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

---

## V-03 -- Axis: Inertia Framing (C-25 Boundary Scan Before Registry Declaration)

**Variation axis:** Inertia framing -- before AC-13 is declared, a mandatory C-25 BOUNDARY
SCAN step is required. This step enumerates every structural artifact in the model and
classifies each as: (a) HAS per-row quality requirements (severity column, rationale column,
compliance flag, or equivalent -- must be registered in AC-13) or (b) NO per-row quality
requirements. The Bottleneck Register Root Cause format, the Exception Catalog As-Is Detection?
flag, and any other artifact with declared per-row constraints are evaluated against the C-25
definition. AC-13 is then declared as the OUTPUT of the boundary scan -- not a pre-assumed
list. The Coverage Scan AC-13 row must confirm: (a) boundary scan was run and table populated;
(b) each artifact classified QUALIFIES is registered and passes C-25 parity with per-sub-condition
evidence; (c) any QUALIFIES artifact discovered after authoring begins was added to the registry.

**Hypothesis:** R9 V-05 pre-declares "three canonical" without scanning. If additional
artifacts qualify under C-25 (e.g., the Bottleneck Register Root Cause is a rationale column
with a specific format requirement), the registry silently undercounts. A boundary scan forces
the model to discover all qualifying artifacts before declaring the registry, making the
completeness claim earned rather than asserted. Expected: boundary scan may identify 3 or
4 qualifying artifacts; any artifact beyond the canonical 3 is new rubric evidence.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

Before any artifact is authored: (1) declare the status-quo process as a named competitor,
(2) run a C-25 BOUNDARY SCAN that classifies every structural artifact in this model as having
or lacking per-row quality requirements, then declare the output acceptance criteria with AC-13
as the registry output of that scan, (3) register the constraint chain with explicit incumbent
coverage flags. Every artifact carries incumbent comparison fields. Phase contracts import and
export named constraints by CC-ID. Exception flows caused by constraint import failures are
traced bidirectionally in a dedicated Constraint-Break Exceptions subsection. The cross-axis
bridge is synthesized in a severity-rated, rationale-equipped Constraint-Incumbent Gap Analysis
section. Phase Delta Blocks and the Constraint Chain Table carry inline column-level quality
constraints. AC-13 is not a pre-assumed list -- it is derived from the boundary scan.

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

**C-25 BOUNDARY SCAN** *(run before declaring OUTPUT ACCEPTANCE CRITERIA)*

Enumerate every structural artifact in this model. For each, determine whether it has declared
per-row quality requirements: a severity column (e.g., HIGH/MED/LOW), a rationale column
(specific text required, generic fails), or a compliance flag (Y/N with blank-fail enforcement
or enum with justification). Classify each as QUALIFIES or NO.

| Artifact | Per-Row Quality Column(s) | Classification | Reason |
|----------|--------------------------|----------------|--------|
| Phase Delta Block | Divergence Type (enum), Impact Severity (enum+trace) | QUALIFIES | Enum values enforced; HIGH/MED requires FM trace |
| Constraint Chain Table | Handoff Strength (enum+justification), Incumbent Models? (enum+blank-fail) | QUALIFIES | Enum values enforced; blank is a fail |
| Constraint-Incumbent Gap Analysis | Gap Severity (HIGH/MED/LOW), Why As-Is Fails (specific rationale) | QUALIFIES | Severity enum + specific rationale required |
| State Table | Delta Ref (DL-ID or NONE) | [Model classifies] | [Justify: cross-reference field or per-row quality req?] |
| Exception Catalog | As-Is Detection? (Y/N) | [Model classifies] | [Justify: Y/N flag with no justification -- qualifies under C-25?] |
| Bottleneck Register | Root Cause (specific format required) | [Model classifies] | [Justify: format-required rationale field -- qualifies under C-25?] |
| Edge Case Catalog | As-Is Handled? (Y/N) | [Model classifies] | [Justify] |
| Terminal Declaration | Incumbent Terminal? (Y/N) | [Model classifies] | [Justify] |
| Gap Register | Incumbent Awareness (Y/N) | [Model classifies] | [Justify] |

**Boundary Scan Outcome:** List all QUALIFIES artifacts. AC-13 registers exactly these.
Any QUALIFIES artifact lacking schema-inline quality bars and an AC with sub-conditions is
a C-25 gap that must be addressed before the Coverage Scan.

---

**OUTPUT ACCEPTANCE CRITERIA**

Declared after Boundary Scan, before any content is authored.

| AC-ID | Criterion | Pass Condition | Fail Condition |
|-------|-----------|----------------|----------------|
| AC-01 | State coverage | Every S-ID has Entry Condition and labeled exit | S-ID with blank entry condition or no labeled exit |
| AC-02 | Terminal closure | Every path and E-ID reaches a named T-ID | Any open-ended path or E-ID |
| AC-03 | Delta Ref completeness | All five artifacts have `Delta Ref (DL-ID or NONE)` per row | Blank Delta Ref cell in any row |
| AC-04 | Phase Delta Block schema and quality | (a) each phase has rubric-exact block before State Table; (b) every Divergence Type cell is exactly `missing`, `incorrect`, or `reversed`; (c) every Impact Severity cell is `HIGH`, `MED`, or `LOW`; HIGH/MED rows cite FM or "New gap" | Wrong column names; model-level block; wrong order; non-enumerated Divergence Type; blank or non-enumerated Impact Severity; HIGH/MED without FM trace |
| AC-05 | Role explicitness | All decisions + state owners cite R-ID; no generic labels | Generic label; uncited decision |
| AC-06 | Exception phase attribution | Every E-ID has Ph-ID; density analysis with DL-ID | Missing Ph-ID; no density analysis |
| AC-07 | Phase entry/exit gating | Each phase has Entry Contract + Exit Gate with required fields | Missing contract or gate; blank Blocked by |
| AC-08 | Root-cause traceability | Bottleneck + Gap Registers have Root Cause citing source artifact and field | Missing column; format without source citation |
| AC-09 | Incumbent field completeness | Every artifact in Incumbent Coverage Mandate has required field populated | Any artifact missing its field; any blank incumbent field |
| AC-10 | Constraint chain completeness and quality | (a) every CC-ID exported appears as imported in consuming phase; (b) every Handoff Strength cell is STRONG, WEAK, or ABSENT-with-justification -- blank is a fail; (c) every Incumbent Models? cell in CCT is Y, N, or ABSENT-with-justification -- blank is a fail | Any CC-ID with no consuming import; blank or invalid Handoff Strength; blank or invalid Incumbent Models? in CCT |
| AC-11 | Constraint-break exception tagging | Exception Catalog has dedicated Constraint-Break Exceptions subsection with 5-column schema; every CC-ID break has E-ID; every E-ID traces to valid CC-ID and main catalog | Subsection absent or prose-only; entry missing required column; CC-ID break unrepresented; E-ID with invalid CC-ID |
| AC-12 | C-24 gap analysis completeness | (a) section named; (b) every N-tagged CC-ID has row; (c) each row has Gap Severity; (d) each row has specific Why As-Is Fails; (e) no blank Incumbent Models? in CCR or CCT | Section absent; N-tagged CC-ID without row; row missing severity; generic rationale; blank Incumbent Models? |
| AC-13 | Per-row quality artifact meta-registry (boundary-scan derived) | All artifacts classified QUALIFIES in the C-25 Boundary Scan are registered here. For each registered artifact: (a) boundary scan classification confirmed; (b) C-25 parity confirmed -- schema inline quality bars present, corresponding AC sub-conditions declared, Coverage Scan confirms each sub-condition with evidence; (c) any artifact discovered QUALIFIES after authoring begins must be added to this registry before Coverage Scan | Any QUALIFIES artifact absent from registry; bulk C-25 attestation; new QUALIFIES artifact introduced without registry update |

AC-13 registry is derived from the C-25 Boundary Scan. Coverage Scan AC-13 must confirm
(a)-(b)-(c) for each registered artifact individually. AC-04, AC-10, and AC-12 sub-conditions
must each be confirmed individually.

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

**PHASE DELTA BLOCK REQUIREMENT** *(feeds AC-04)*

Each lifecycle phase contains a mandatory Phase Delta Block, authored BEFORE the State Table.
Quality constraints are embedded inline in each column header.

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed -- any other value is a fail) | Impact Severity (HIGH / MED / LOW -- HIGH or MED requires FM trace or "New gap" note; blank is a fail) |
|-------|----------------------|-------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|

- If no divergences exist: explicit no-divergence row required

---

**DELTA CROSS-REFERENCE REQUIREMENT** *(feeds AC-03)*

Five artifacts carry `Delta Ref (DL-ID or NONE)` (exact name):
State Trace / Exception Catalog / Edge Case Catalog / Bottleneck Register / Gap Register.

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

**PHASE DELTA BLOCK [Ph-ID: Phase Name]** -- AUTHOR BEFORE STATE TABLE *(feeds AC-04)*

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

Fork (S-ID): [branching state]
Branch A: [named path]
Branch B: [named path]
Join condition: [what must hold before merge]
Merge owner: [R-ID]
As-Is join: [incumbent join behavior -- or ABSENT]
Incumbent gap: [what breaks in the incumbent if join condition fails -- or N/A]

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
| Exported constraints | [CC-IDs this phase exports.] |
| Constraint export gap | [Constraint that should export but cannot be verified; or NONE] |
| Incumbent exit | [How the incumbent transitions out -- or ABSENT] |

---

*Repeat for each phase. If a new per-row quality artifact is introduced, classify it in the
Boundary Scan table and update AC-13 before continuing.*

---

**CONSTRAINT CHAIN TABLE** *(finalized after all phases -- feeds AC-10)*

| CC-ID | Constraint Name | From Ph-ID | Exported As | To Ph-ID | Imported As | Verification Method | Handoff Strength (STRONG / WEAK / ABSENT -- ABSENT requires justification note; blank is a fail) | Incumbent Models? (Y / N / ABSENT-with-justification -- blank is a hard fail) |
|-------|-----------------|-----------|-------------|---------|-------------|---------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| CC-01 | | | | | | | | |

At least one STRONG required. ABSENT requires inline justification.

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

**Exception Density Note:** Most-dense Ph-ID + structural rationale + DL-ID citation.

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

Root Cause format: `Phase Delta [Ph-ID] [DL-ID] -- Current Process Step: [value]`
or: `Phase Exit Gate [Ph-ID] -- Blocked by: [value]`

---

**GAP REGISTER** *(feeds AC-03, AC-08)*

| G-ID | Phase (Ph-ID) | Gap | Delta Ref (DL-ID or NONE) | As-Is (from DL-ID row) | Harm from Absence | Incumbent Awareness (Y/N) |
|------|---------------|-----|---------------------------|------------------------|-------------------|--------------------------|
| G-01 | | | | | | |

---

**CROSS-PROCESS HANDOFF (raise score)** *(feeds AC-09 if authored)*

Handoff trigger: [Event initiating handoff]
Recipient process: [Named adjacent process]
Fields passed: [Named data elements]
Acceptance condition: [What recipient verifies]
As-Is gap: [Y/N + note]
Delta source: [DL-ID or NONE]
Exported constraint: [CC-ID governing this handoff -- or NONE]

**SLA ANNOTATION (raise score)** *(feeds AC-09 if authored)*

| Gate or S-ID | Node Name | Expected Duration | At-Risk Threshold | As-Is Typical Duration | Scenario Breach (Y/N) |
|--------------|-----------|-------------------|-------------------|-----------------------|-----------------------|
| | | | | | |

---

**COVERAGE SCAN** *(executes AC-01 through AC-13 plus Check V)*

For each AC-ID, record PASS or FAIL with enumerated evidence. AC-04, AC-10, AC-12, and AC-13
sub-conditions must be confirmed individually.

| AC-ID | Result | Evidence or Failure Detail |
|-------|--------|---------------------------|
| AC-01 | | [S-IDs checked; failures named] |
| AC-02 | | [paths and E-IDs checked; open-ended named] |
| AC-03 | | [artifacts and row counts; blank cells named] |
| AC-04 | | [(a) block order per phase; (b) Divergence Type values; (c) Impact Severity + FM-trace] |
| AC-05 | | [decisions and state owners; generic labels named] |
| AC-06 | | [E-IDs checked; most-dense phase with DL-ID] |
| AC-07 | | [phases; missing contract or gate named] |
| AC-08 | | [registers; Root Cause format confirmed] |
| AC-09 | | [per-artifact incumbent field completeness] |
| AC-10 | | [(a) chain completeness; (b) Handoff Strength values; (c) Incumbent Models? values] |
| AC-11 | | [subsection present? CC-ID+Ph-ID per entry? CC-ID break coverage? E-ID validity?] |
| AC-12 | | [(a)-(e) confirmed individually] |
| AC-13 | | [(a) Boundary scan confirmed run; QUALIFIES artifacts listed; (b) per registered artifact -- schema inline? AC sub-conditions? scan per-sub-condition?; (c) any QUALIFIES artifact discovered after authoring -- named and registry updated?] |

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

**Constraint-Incumbent Gap Analysis** *(required when any CC-ID has `Incumbent Models? = N`)*

One row per CC-ID where `Incumbent Models? = N`. Explicit NONE with justification if none.

Gap Severity: HIGH / MED / LOW. `Why As-Is Fails` must name a specific process characteristic.

| CC-ID | Constraint Name | Gap Severity (HIGH/MED/LOW) | Why As-Is Fails |
|-------|-----------------|----------------------------|-----------------|
| [CC-ID where N] | | | [specific named process characteristic] |

---

**FINAL AUTHORING CHECK**

- [ ] C-25 BOUNDARY SCAN completed and table populated before OAC declared
- [ ] All QUALIFIES artifacts from boundary scan are registered in AC-13
- [ ] OUTPUT ACCEPTANCE CRITERIA declared after boundary scan; AC-01 through AC-13 all declared
- [ ] AC-04 enumerates sub-conditions (a)-(b)-(c) for Phase Delta Block quality
- [ ] AC-10 enumerates sub-conditions (a)-(b)-(c) for CCT quality fields
- [ ] Phase Delta Block and CCT schema templates have inline quality bars in column headers
- [ ] CONSTRAINT CHAIN REGISTRY authored before any phase; no blank `Incumbent Models?` cells
- [ ] Status-Quo Role Comparison is dedicated
- [ ] All five artifacts carry `Delta Ref (DL-ID or NONE)` column
- [ ] Constraint-Break Exceptions: formal 5-column table; Check V confirmed
- [ ] Gap Analysis: both columns; one row per N-tagged CC-ID
- [ ] Coverage Scan: AC-01 through AC-13 + Check V; AC-13 boundary-scan-derived registry confirmed

**OUTPUT:** Write to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

---

## V-04 -- Axis: Combined V-01 + V-03 (Live Registry + Boundary Scan, No PQAR Table)

**Variation axis:** Lifecycle emphasis + inertia framing -- V-01 (live registry with update
policy) and V-03 (C-25 boundary scan before registry declaration) are combined. The boundary
scan discovers all qualifying artifacts. AC-13 is then declared as a LIVE registry of the
discovered set, with an explicit update trigger: any new per-row quality artifact introduced
during authoring must be added before continuing. No PQAR table is added -- the registry
remains prose-form inside the AC-13 cell, but the boundary scan ensures its completeness
is earned rather than assumed. The Coverage Scan AC-13 row must confirm: (a) boundary scan
ran and produced the registered set; (b) each registered artifact passes C-25 parity with
per-sub-condition evidence; (c) no per-row quality artifact in the final model is absent
from the registry; (d) the live update trigger was observed -- any artifact added after
authoring start is named.

**Hypothesis:** V-01 tests whether the live update policy alone (without a scan) prevents
forward-protection gaps. V-03 tests whether the boundary scan alone (without a policy)
ensures completeness. V-04 combines both: the scan earns completeness at authoring start,
the live policy maintains it during authoring. Without the PQAR table structure (V-02), the
registry remains in prose and additions are less structurally visible. Expected: C-26 PASS --
both completeness guarantees are active; the only remaining gap vs V-05 is the structural
visibility of the PQAR table form.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

Before any artifact is authored: (1) declare the status-quo process as a named competitor,
(2) run a C-25 BOUNDARY SCAN to discover all per-row quality artifacts, then declare the
output acceptance criteria with AC-13 as a LIVE meta-registry of the discovered set with an
explicit update trigger policy, (3) register the constraint chain with explicit incumbent
coverage flags. Every artifact carries incumbent comparison fields. Phase contracts import and
export named constraints by CC-ID. Exception flows caused by constraint import failures are
traced bidirectionally in a dedicated Constraint-Break Exceptions subsection. The cross-axis
bridge is synthesized in a severity-rated, rationale-equipped Constraint-Incumbent Gap Analysis
section verified by a pre-declared five-condition acceptance check. Phase Delta Blocks and the
Constraint Chain Table carry inline column-level quality constraints. If any new per-row quality
artifact is introduced during authoring, AC-13 must be updated before continuing.

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

**C-25 BOUNDARY SCAN** *(run before declaring OUTPUT ACCEPTANCE CRITERIA)*

Classify every structural artifact in this model as QUALIFIES (has per-row quality requirements:
severity column, rationale column, compliance flag with justification, or enum with blank-fail
enforcement) or NO. Justify each classification.

| Artifact | Per-Row Quality Column(s) | Classification | Reason |
|----------|--------------------------|----------------|--------|
| Phase Delta Block | Divergence Type (enum), Impact Severity (enum+trace) | QUALIFIES | Enum values enforced; HIGH/MED requires FM trace |
| Constraint Chain Table | Handoff Strength (enum+justification), Incumbent Models? (enum+blank-fail) | QUALIFIES | Enum values enforced; blank is a fail |
| Constraint-Incumbent Gap Analysis | Gap Severity (HIGH/MED/LOW), Why As-Is Fails (specific rationale) | QUALIFIES | Severity enum + specific rationale required |
| State Table | Delta Ref (DL-ID or NONE) | [Model classifies] | [Justify] |
| Exception Catalog | As-Is Detection? (Y/N) | [Model classifies] | [Justify] |
| Bottleneck Register | Root Cause (specific format required) | [Model classifies] | [Justify] |
| Edge Case Catalog | As-Is Handled? (Y/N) | [Model classifies] | [Justify] |
| Terminal Declaration | Incumbent Terminal? (Y/N) | [Model classifies] | [Justify] |
| Gap Register | Incumbent Awareness (Y/N) | [Model classifies] | [Justify] |

**Boundary Scan Outcome:** [List all QUALIFIES artifacts here. AC-13 will register exactly these.]

---

**OUTPUT ACCEPTANCE CRITERIA**

Declared after Boundary Scan, before any content is authored.

| AC-ID | Criterion | Pass Condition | Fail Condition |
|-------|-----------|----------------|----------------|
| AC-01 | State coverage | Every S-ID has Entry Condition and labeled exit | S-ID with blank entry condition or no labeled exit |
| AC-02 | Terminal closure | Every path and E-ID reaches a named T-ID | Any open-ended path or E-ID |
| AC-03 | Delta Ref completeness | All five artifacts have `Delta Ref (DL-ID or NONE)` per row | Blank Delta Ref cell in any row |
| AC-04 | Phase Delta Block schema and quality | (a) each phase has rubric-exact block before State Table; (b) every Divergence Type cell is exactly `missing`, `incorrect`, or `reversed`; (c) every Impact Severity cell is `HIGH`, `MED`, or `LOW`; HIGH/MED rows cite FM or "New gap" | Wrong column names; model-level block; wrong order; non-enumerated Divergence Type; blank or non-enumerated Impact Severity; HIGH/MED without FM trace |
| AC-05 | Role explicitness | All decisions + state owners cite R-ID; no generic labels | Generic label; uncited decision |
| AC-06 | Exception phase attribution | Every E-ID has Ph-ID; density analysis with DL-ID | Missing Ph-ID; no density analysis |
| AC-07 | Phase entry/exit gating | Each phase has Entry Contract + Exit Gate with required fields | Missing contract or gate; blank Blocked by |
| AC-08 | Root-cause traceability | Bottleneck + Gap Registers have Root Cause citing source artifact and field | Missing column; format without source citation |
| AC-09 | Incumbent field completeness | Every artifact in Incumbent Coverage Mandate has required field populated | Any artifact missing its field; any blank incumbent field |
| AC-10 | Constraint chain completeness and quality | (a) every CC-ID exported appears as imported in consuming phase; (b) every Handoff Strength cell is STRONG, WEAK, or ABSENT-with-justification -- blank is a fail; (c) every Incumbent Models? cell in CCT is Y, N, or ABSENT-with-justification -- blank is a fail | Any CC-ID with no consuming import; blank or invalid Handoff Strength; blank or invalid Incumbent Models? in CCT |
| AC-11 | Constraint-break exception tagging | Exception Catalog has dedicated Constraint-Break Exceptions subsection with 5-column schema; every CC-ID break has E-ID; every E-ID traces to valid CC-ID and main catalog | Subsection absent; entry missing required column; CC-ID break unrepresented; E-ID with invalid CC-ID |
| AC-12 | C-24 gap analysis completeness | (a) section named; (b) every N-tagged CC-ID has row; (c) each row has Gap Severity; (d) each row has specific Why As-Is Fails; (e) no blank Incumbent Models? in CCR or CCT | Section absent; N-tagged CC-ID without row; row missing severity; generic rationale; blank Incumbent Models? |
| AC-13 | Per-row quality artifact meta-registry (LIVE, boundary-scan derived) | All artifacts classified QUALIFIES in the C-25 Boundary Scan registered here (initial set from scan: [list QUALIFIES artifacts]). UPDATE POLICY: if any phase or optional section introduces a new structural artifact with per-row quality requirements, add that artifact to this entry before continuing -- silent omission is a fail. Coverage Scan must confirm: (a) boundary scan was run and QUALIFIES set produced; (b) each registered artifact passes C-25 parity with per-sub-condition evidence; (c) no per-row quality artifact in the final model is absent from this registry; (d) live update trigger was observed -- any artifact added after authoring start named here | Any QUALIFIES artifact absent from registry; bulk C-25 attestation; new artifact introduced without registry update; boundary scan absent or skipped |

These thirteen checks are the acceptance definition. AC-13 is LIVE and boundary-scan derived.
AC-04 sub-conditions (a)-(b)-(c), AC-10 sub-conditions (a)-(b)-(c), AC-12 sub-conditions
(a)-(e), and AC-13 sub-conditions (a)-(b)-(c)-(d) must each be confirmed individually.

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

**PHASE DELTA BLOCK REQUIREMENT** *(feeds AC-04)*

Each lifecycle phase contains a mandatory Phase Delta Block, authored BEFORE the State Table.
Quality constraints are embedded inline in each column header.

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed -- any other value is a fail) | Impact Severity (HIGH / MED / LOW -- HIGH or MED requires FM trace or "New gap" note; blank is a fail) |
|-------|----------------------|-------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|

- If no divergences exist: explicit no-divergence row required

---

**DELTA CROSS-REFERENCE REQUIREMENT** *(feeds AC-03)*

Five artifacts carry `Delta Ref (DL-ID or NONE)` (exact name):
State Trace / Exception Catalog / Edge Case Catalog / Bottleneck Register / Gap Register.

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

**PHASE DELTA BLOCK [Ph-ID: Phase Name]** -- AUTHOR BEFORE STATE TABLE *(feeds AC-04)*

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

Fork (S-ID): [branching state]
Branch A: [named path]
Branch B: [named path]
Join condition: [what must hold before merge]
Merge owner: [R-ID]
As-Is join: [incumbent join behavior -- or ABSENT]
Incumbent gap: [what breaks in the incumbent if join condition fails -- or N/A]

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
| Exported constraints | [CC-IDs this phase exports.] |
| Constraint export gap | [Constraint that should export but cannot be verified; or NONE] |
| Incumbent exit | [How the incumbent transitions out -- or ABSENT] |

---

*Repeat for each phase. If a new per-row quality artifact is introduced, classify it in the
Boundary Scan table and update AC-13 before continuing.*

---

**CONSTRAINT CHAIN TABLE** *(finalized after all phases -- feeds AC-10)*

| CC-ID | Constraint Name | From Ph-ID | Exported As | To Ph-ID | Imported As | Verification Method | Handoff Strength (STRONG / WEAK / ABSENT -- ABSENT requires justification note; blank is a fail) | Incumbent Models? (Y / N / ABSENT-with-justification -- blank is a hard fail) |
|-------|-----------------|-----------|-------------|---------|-------------|---------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| CC-01 | | | | | | | | |

At least one STRONG required. ABSENT requires inline justification.

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

**Exception Density Note:** Most-dense Ph-ID + structural rationale + DL-ID citation.

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

Root Cause format: `Phase Delta [Ph-ID] [DL-ID] -- Current Process Step: [value]`
or: `Phase Exit Gate [Ph-ID] -- Blocked by: [value]`

---

**GAP REGISTER** *(feeds AC-03, AC-08)*

| G-ID | Phase (Ph-ID) | Gap | Delta Ref (DL-ID or NONE) | As-Is (from DL-ID row) | Harm from Absence | Incumbent Awareness (Y/N) |
|------|---------------|-----|---------------------------|------------------------|-------------------|--------------------------|
| G-01 | | | | | | |

---

**CROSS-PROCESS HANDOFF (raise score)** *(feeds AC-09 if authored)*

Handoff trigger: [Event initiating handoff]
Recipient process: [Named adjacent process]
Fields passed: [Named data elements]
Acceptance condition: [What recipient verifies]
As-Is gap: [Y/N + note]
Delta source: [DL-ID or NONE]
Exported constraint: [CC-ID governing this handoff -- or NONE]

**SLA ANNOTATION (raise score)** *(feeds AC-09 if authored)*

| Gate or S-ID | Node Name | Expected Duration | At-Risk Threshold | As-Is Typical Duration | Scenario Breach (Y/N) |
|--------------|-----------|-------------------|-------------------|-----------------------|-----------------------|
| | | | | | |

---

**COVERAGE SCAN** *(executes AC-01 through AC-13 plus Check V)*

For each AC-ID, record PASS or FAIL with enumerated evidence. AC-04, AC-10, AC-12, and AC-13
sub-conditions must each be confirmed individually.

| AC-ID | Result | Evidence or Failure Detail |
|-------|--------|---------------------------|
| AC-01 | | [S-IDs checked; failures named] |
| AC-02 | | [paths and E-IDs checked; open-ended named] |
| AC-03 | | [artifacts and row counts; blank cells named] |
| AC-04 | | [(a) block order per phase; (b) Divergence Type values; (c) Impact Severity + FM-trace] |
| AC-05 | | [decisions and state owners; generic labels named] |
| AC-06 | | [E-IDs checked; most-dense phase with DL-ID] |
| AC-07 | | [phases; missing contract or gate named] |
| AC-08 | | [registers; Root Cause format confirmed] |
| AC-09 | | [per-artifact incumbent field completeness] |
| AC-10 | | [(a) chain completeness; (b) Handoff Strength values; (c) Incumbent Models? values] |
| AC-11 | | [subsection present? CC-ID+Ph-ID? CC-ID break coverage? E-ID validity?] |
| AC-12 | | [(a)-(e) confirmed individually] |
| AC-13 | | [(a) boundary scan confirmed run; QUALIFIES set named; (b) per registered artifact -- schema inline? AC sub-conditions? scan per-sub-condition?; (c) no per-row quality artifact absent from registry; (d) live update trigger observed -- artifacts introduced after authoring start named or confirmed absent] |

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

**Constraint-Incumbent Gap Analysis** *(required when any CC-ID has `Incumbent Models? = N`)*

One row per CC-ID where `Incumbent Models? = N`. Explicit NONE with justification if none.

Gap Severity: HIGH / MED / LOW. `Why As-Is Fails` must name a specific process characteristic.

| CC-ID | Constraint Name | Gap Severity (HIGH/MED/LOW) | Why As-Is Fails |
|-------|-----------------|----------------------------|-----------------|
| [CC-ID where N] | | | [specific named process characteristic] |

---

**FINAL AUTHORING CHECK**

- [ ] C-25 BOUNDARY SCAN completed before OAC declared; QUALIFIES set identified
- [ ] OUTPUT ACCEPTANCE CRITERIA declared after boundary scan; AC-01 through AC-13 all declared
- [ ] AC-13 is LIVE: derived from boundary scan + update trigger policy declared
- [ ] AC-04 enumerates sub-conditions (a)-(b)-(c); AC-10 enumerates sub-conditions (a)-(b)-(c)
- [ ] Phase Delta Block and CCT schema templates have inline quality bars in column headers
- [ ] CONSTRAINT CHAIN REGISTRY authored before any phase; no blank `Incumbent Models?` cells
- [ ] Status-Quo Role Comparison is dedicated
- [ ] All five artifacts carry `Delta Ref (DL-ID or NONE)` column
- [ ] Constraint-Break Exceptions: formal 5-column table; Check V confirmed
- [ ] Gap Analysis: both columns; one row per N-tagged CC-ID
- [ ] If any new per-row quality artifact introduced during authoring: boundary scan updated + AC-13 updated
- [ ] Coverage Scan: AC-01 through AC-13 + Check V; AC-13 (a)-(d) confirmed individually

**OUTPUT:** Write to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

---

## V-05 -- Axis: Combined (PQAR Table + Live Registry + Boundary Scan -- Full C-26 Floor)

**Variation axis:** Output format + lifecycle emphasis + inertia framing -- maximum C-26
structural density. Holds the complete R9 V-05 floor (inline quality bars in Phase Delta Block
and CCT schemas; AC-04 and AC-10 with per-column sub-conditions; AC-12 with five sub-conditions;
formal Constraint-Break Exceptions subsection; AC-11 pre-declared) and adds all three R10
C-26 components: (1) a mandatory C-25 BOUNDARY SCAN that classifies every structural artifact
before AC-13 is declared, (2) a dedicated PER-ROW QUALITY ARTIFACT REGISTRY (PQAR) section
as a formal table, (3) AC-13 as a LIVE registry pointer with an explicit update trigger policy.
The Coverage Scan AC-13 row must verify: (a) boundary scan was run; (b) PQAR table is populated
with all QUALIFIES artifacts; (c) per Reg-ID in the PQAR table, C-25 parity is confirmed
individually; (d) live update trigger was observed.

**Hypothesis:** V-01 tests the live policy alone; V-02 tests the PQAR table alone; V-03 tests
the boundary scan alone; V-04 tests policy + scan without the table. V-05 combines all three.
The boundary scan earns completeness at authoring start. The PQAR table makes additions
structurally visible. The live policy maintains completeness during authoring. Together these
provide the full C-26 forward-protection guarantee: silent omission of any per-row quality
artifact is detectable at scan time. V-05 is the R10 definitive floor. Comparison with V-04
(no PQAR table) will identify whether the table form is the binding remaining structural gap.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or
process named in the signal.

Before any artifact is authored: (1) declare the status-quo process as a named competitor,
(2) run a C-25 BOUNDARY SCAN to discover all per-row quality artifacts, then declare the
output acceptance criteria with a dedicated PER-ROW QUALITY ARTIFACT REGISTRY (PQAR) table
and AC-13 as a LIVE meta-registry pointer with update trigger policy, (3) register the
constraint chain with explicit incumbent coverage flags. Every artifact carries incumbent
comparison fields. Phase contracts import and export named constraints by CC-ID. Exception
flows caused by constraint import failures are traced bidirectionally in a dedicated
Constraint-Break Exceptions subsection. The cross-axis bridge is synthesized in a
severity-rated, rationale-equipped Constraint-Incumbent Gap Analysis section verified by a
pre-declared five-condition acceptance check. Phase Delta Blocks and the Constraint Chain
Table carry inline column-level quality constraints. The PQAR table is the authoritative
structural registry; any new per-row quality artifact requires a new PQAR row and an AC-13
update before authoring continues.

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

**C-25 BOUNDARY SCAN** *(run before declaring OUTPUT ACCEPTANCE CRITERIA)*

Classify every structural artifact in this model as QUALIFIES (has per-row quality requirements:
severity column, rationale column, compliance flag with justification, or enum with blank-fail
enforcement) or NO. Justify each classification. QUALIFIES artifacts become rows in the PQAR
table below.

| Artifact | Per-Row Quality Column(s) | Classification | Reason |
|----------|--------------------------|----------------|--------|
| Phase Delta Block | Divergence Type (enum), Impact Severity (enum+trace) | QUALIFIES | Enum values enforced; HIGH/MED requires FM trace |
| Constraint Chain Table | Handoff Strength (enum+justification), Incumbent Models? (enum+blank-fail) | QUALIFIES | Enum values enforced; blank is a fail |
| Constraint-Incumbent Gap Analysis | Gap Severity (HIGH/MED/LOW), Why As-Is Fails (specific rationale) | QUALIFIES | Severity enum + specific rationale required |
| State Table | Delta Ref (DL-ID or NONE) | [Model classifies] | [Justify] |
| Exception Catalog | As-Is Detection? (Y/N) | [Model classifies] | [Justify] |
| Bottleneck Register | Root Cause (specific format required) | [Model classifies] | [Justify] |
| Edge Case Catalog | As-Is Handled? (Y/N) | [Model classifies] | [Justify] |
| Terminal Declaration | Incumbent Terminal? (Y/N) | [Model classifies] | [Justify] |
| Gap Register | Incumbent Awareness (Y/N) | [Model classifies] | [Justify] |

**Boundary Scan Outcome:** [List all QUALIFIES artifacts. These become PQAR rows.]

---

**OUTPUT ACCEPTANCE CRITERIA**

Declared after Boundary Scan, before any content is authored.

| AC-ID | Criterion | Pass Condition | Fail Condition |
|-------|-----------|----------------|----------------|
| AC-01 | State coverage | Every S-ID has Entry Condition and labeled exit | S-ID with blank entry condition or no labeled exit |
| AC-02 | Terminal closure | Every path and E-ID reaches a named T-ID | Any open-ended path or E-ID |
| AC-03 | Delta Ref completeness | All five artifacts have `Delta Ref (DL-ID or NONE)` per row | Blank Delta Ref cell in any row |
| AC-04 | Phase Delta Block schema and quality | (a) each phase has rubric-exact block before State Table; (b) every Divergence Type cell is exactly `missing`, `incorrect`, or `reversed`; (c) every Impact Severity cell is `HIGH`, `MED`, or `LOW`; HIGH/MED rows cite FM or "New gap" | Wrong column names; model-level block; wrong order; non-enumerated Divergence Type; blank or non-enumerated Impact Severity; HIGH/MED without FM trace |
| AC-05 | Role explicitness | All decisions + state owners cite R-ID; no generic labels | Generic label; uncited decision |
| AC-06 | Exception phase attribution | Every E-ID has Ph-ID; density analysis with DL-ID | Missing Ph-ID; no density analysis |
| AC-07 | Phase entry/exit gating | Each phase has Entry Contract + Exit Gate with required fields | Missing contract or gate; blank Blocked by |
| AC-08 | Root-cause traceability | Bottleneck + Gap Registers have Root Cause citing source artifact and field | Missing column; format without source citation |
| AC-09 | Incumbent field completeness | Every artifact in Incumbent Coverage Mandate has required field populated | Any artifact missing its field; any blank incumbent field |
| AC-10 | Constraint chain completeness and quality | (a) every CC-ID exported appears as imported in consuming phase; (b) every Handoff Strength cell is STRONG, WEAK, or ABSENT-with-justification -- blank is a fail; (c) every Incumbent Models? cell in CCT is Y, N, or ABSENT-with-justification -- blank is a fail | Any CC-ID with no consuming import; blank or invalid Handoff Strength; blank or invalid Incumbent Models? in CCT |
| AC-11 | Constraint-break exception tagging | Exception Catalog has dedicated Constraint-Break Exceptions subsection with 5-column schema; every CC-ID break has E-ID; every E-ID traces to valid CC-ID and main catalog | Subsection absent; entry missing required column; CC-ID break unrepresented; E-ID with invalid CC-ID |
| AC-12 | C-24 gap analysis completeness | (a) section named; (b) every N-tagged CC-ID has row; (c) each row has Gap Severity; (d) each row has specific Why As-Is Fails; (e) no blank Incumbent Models? in CCR or CCT | Section absent; N-tagged CC-ID without row; row missing severity; generic rationale; blank Incumbent Models? |
| AC-13 | Per-row quality artifact meta-registry (LIVE, boundary-scan derived) | See PER-ROW QUALITY ARTIFACT REGISTRY (PQAR) table below. UPDATE POLICY: if any phase or optional section introduces a new structural artifact with per-row quality requirements, insert a new row in the PQAR table and update this entry before continuing -- silent omission is a fail. Coverage Scan must verify: (a) boundary scan ran; (b) PQAR table populated with all QUALIFIES artifacts; (c) per Reg-ID: C-25 parity confirmed -- schema inline bars present, AC sub-conditions declared, scan confirms each sub-condition with evidence; (d) live update trigger observed -- new PQAR rows added during authoring are named, or confirmed absent | Any Reg-ID absent from PQAR table; bulk C-25 attestation; new per-row quality artifact introduced without PQAR row; boundary scan absent |

These thirteen checks are the acceptance definition. AC-13 is LIVE and PQAR-table-backed.
AC-04 (a)-(b)-(c), AC-10 (a)-(b)-(c), AC-12 (a)-(e), and AC-13 (a)-(b)-(c)-(d) must each
be confirmed individually in the Coverage Scan.

---

**PER-ROW QUALITY ARTIFACT REGISTRY (PQAR)** *(canonical registry -- feeds AC-13)*

Populated from the C-25 Boundary Scan QUALIFIES set. Adding a new structural artifact with
per-row quality requirements requires inserting a new row here before continuing authoring.
Each new row requires: corresponding AC-ID created or updated with sub-conditions declared,
and schema template updated with inline quality bars.

| Reg-ID | Artifact Name | Per-Row Quality Columns | Corresponding AC-ID | Sub-conditions Declared | Schema Inline Bars? |
|--------|---------------|------------------------|---------------------|------------------------|---------------------|
| PQAR-01 | Phase Delta Block | Divergence Type (must be exactly missing/incorrect/reversed), Impact Severity (HIGH/MED/LOW; HIGH/MED requires FM trace) | AC-04 | (a) block order; (b) Divergence Type values; (c) Impact Severity values + FM trace | Y -- embedded in column headers |
| PQAR-02 | Constraint Chain Table | Handoff Strength (STRONG/WEAK/ABSENT-with-justification; blank=fail), Incumbent Models? (Y/N/ABSENT-with-justification; blank=fail) | AC-10 | (a) chain completeness; (b) Handoff Strength values; (c) Incumbent Models? values | Y -- embedded in column headers |
| PQAR-03 | Constraint-Incumbent Gap Analysis | Gap Severity (HIGH/MED/LOW), Why As-Is Fails (specific named process characteristic; generic=fail) | AC-12 | (a) section named; (b) N-tagged CC-IDs have rows; (c) Gap Severity per row; (d) Why As-Is Fails per row; (e) no blank Incumbent Models? | Y -- schema columns declared in Inertia Summary template |
| [PQAR-NN] | [Any additional artifact classified QUALIFIES in boundary scan] | [Columns] | [AC-ID] | [Sub-conditions] | [Y/N] |

Coverage Scan AC-13 row must cite each Reg-ID individually. Bulk attestation is a fail.

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

Each lifecycle phase contains a mandatory Phase Delta Block, authored BEFORE the State Table.
Quality constraints are embedded inline in each column header.

| DL-ID | Current Process Step | Target Model Step | Divergence Type (must be exactly: missing / incorrect / reversed -- any other value is a fail) | Impact Severity (HIGH / MED / LOW -- HIGH or MED requires FM trace or "New gap" note; blank is a fail) |
|-------|----------------------|-------------------|-------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|

- If no divergences exist: explicit no-divergence row required

---

**DELTA CROSS-REFERENCE REQUIREMENT** *(feeds AC-03)*

Five artifacts carry `Delta Ref (DL-ID or NONE)` (exact name):
State Trace / Exception Catalog / Edge Case Catalog / Bottleneck Register / Gap Register.

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
N entries must appear in the Constraint-Incumbent Gap Analysis. Update this registry if new
constraints are identified during phase authoring.

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

Fork (S-ID): [branching state]
Branch A: [named path]
Branch B: [named path]
Join condition: [what must hold before merge]
Merge owner: [R-ID]
As-Is join: [incumbent join behavior -- or ABSENT]
Incumbent gap: [what breaks in the incumbent if join condition fails -- or N/A]

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
| Exported constraints | [CC-IDs this phase exports. Format: CC-NN: [constraint name and verified state].] |
| Constraint export gap | [Constraint that should export but cannot be verified; or NONE] |
| Incumbent exit | [How the incumbent transitions out -- or ABSENT] |

---

*Repeat for each phase. Update Constraint Chain Registry with any new CC-IDs discovered.
If a new per-row quality artifact is introduced: (1) classify in Boundary Scan table,
(2) add row to PQAR table, (3) update AC-13, (4) then continue.*

---

**CONSTRAINT CHAIN TABLE** *(finalized after all phases -- feeds AC-10 / PQAR-02)*

| CC-ID | Constraint Name | From Ph-ID | Exported As | To Ph-ID | Imported As | Verification Method | Handoff Strength (STRONG / WEAK / ABSENT -- ABSENT requires justification note; blank is a fail) | Incumbent Models? (Y / N / ABSENT-with-justification -- blank is a hard fail) |
|-------|-----------------|-----------|-------------|---------|-------------|---------------------|--------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------|
| CC-01 | | | | | | | | |

At least one STRONG required. ABSENT requires inline justification.

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

Bidirectional traceability rules: every CC-ID break must appear as at least one E-ID here;
every E-ID here must trace to valid CC-ID and main Exception Catalog. Check V audits.
Resolve before output.

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

Root Cause format: `Phase Delta [Ph-ID] [DL-ID] -- Current Process Step: [value]`
or: `Phase Exit Gate [Ph-ID] -- Blocked by: [value]`

---

**GAP REGISTER** *(feeds AC-03, AC-08)*

| G-ID | Phase (Ph-ID) | Gap | Delta Ref (DL-ID or NONE) | As-Is (from DL-ID row) | Harm from Absence | Incumbent Awareness (Y/N) |
|------|---------------|-----|---------------------------|------------------------|-------------------|--------------------------|
| G-01 | | | | | | |

---

**CROSS-PROCESS HANDOFF (raise score)** *(feeds AC-09 if authored)*

Handoff trigger: [Event initiating handoff]
Recipient process: [Named adjacent process]
Fields passed: [Named data elements]
Acceptance condition: [What recipient verifies]
As-Is gap: [Y/N + note]
Delta source: [DL-ID or NONE]
Exported constraint: [CC-ID governing this handoff -- or NONE]

**SLA ANNOTATION (raise score)** *(feeds AC-09 if authored)*

| Gate or S-ID | Node Name | Expected Duration | At-Risk Threshold | As-Is Typical Duration | Scenario Breach (Y/N) |
|--------------|-----------|-------------------|-------------------|-----------------------|-----------------------|
| | | | | | |

---

**COVERAGE SCAN** *(executes AC-01 through AC-13 plus Check V)*

For each AC-ID, record PASS or FAIL with enumerated evidence. AC-04 (a)-(b)-(c), AC-10
(a)-(b)-(c), AC-12 (a)-(e), and AC-13 (a)-(b)-(c)-(d) must each be confirmed individually.
AC-13 must cite each PQAR Reg-ID individually -- bulk attestation is a fail.

| AC-ID | Result | Evidence or Failure Detail |
|-------|--------|---------------------------|
| AC-01 | | [S-IDs checked; failures named] |
| AC-02 | | [paths and E-IDs checked; open-ended named] |
| AC-03 | | [artifacts and row counts; blank cells named] |
| AC-04 | | [(a) block order per phase confirmed; (b) Divergence Type values enumerated -- non-enumerated named; (c) Impact Severity values -- HIGH/MED FM-trace confirmed] |
| AC-05 | | [decisions and state owners; generic labels named] |
| AC-06 | | [E-IDs checked; most-dense phase with DL-ID] |
| AC-07 | | [phases; missing contract or gate named] |
| AC-08 | | [registers; Root Cause format confirmed] |
| AC-09 | | [per-artifact incumbent field completeness; blanks named] |
| AC-10 | | [(a) chain completeness per CC-ID; (b) Handoff Strength values -- blanks or invalid named; (c) Incumbent Models? values in CCT -- blanks named] |
| AC-11 | | [subsection present? CC-ID+Ph-ID per entry? every CC-ID break has E-ID? every E-ID traces to valid CC-ID?] |
| AC-12 | | [(a)-(e) confirmed individually] |
| AC-13 | | [(a) boundary scan confirmed run; QUALIFIES set named; (b) PQAR-01 (Phase Delta Block): schema inline bars present? AC-04 sub-conditions declared? scan per-sub-condition confirmed?; PQAR-02 (Constraint Chain Table): schema inline bars? AC-10 sub-conditions? scan per-sub-condition?; PQAR-03 (Gap Analysis): schema inline? AC-12 sub-conditions? scan per-sub-condition?; any additional PQAR rows -- same verification; (c) no per-row quality artifact absent from PQAR table; (d) live update trigger observed -- new PQAR rows during authoring named or confirmed absent] |

**Check V -- Constraint-Break bidirectional traceability:**

(a) For every CC-ID with a known break: confirm it appears as at least one E-ID in the subsection.
(b) For every E-ID in the subsection: confirm CC-ID Violated exists in Constraint Chain Table.
(c) For every E-ID in the subsection: confirm it also exists in the main Exception Catalog.

Any FAIL must be corrected before output. Self-attestation is not acceptable.

---

**INERTIA SUMMARY**

| Item | Count / Detail |
|------|---------------|
| Exceptions incumbent cannot detect (As-Is Detection? = N) | [list E-IDs] |
| Edge cases incumbent cannot handle (As-Is Handled? = N) | [list EC-IDs] |
| Terminals incumbent leaves open-ended (Incumbent Terminal? = N) | [list T-IDs] |
| Roles absent from incumbent | [list R-IDs] |
| Gaps invisible to incumbent (Incumbent Awareness = N) | [list G-IDs] |
| Known failure modes addressed | [FM-1/FM-2/FM-3 closed by which artifacts] |

**Constraint-Incumbent Gap Analysis** *(required when any CC-ID has `Incumbent Models? = N` -- feeds AC-12 / PQAR-03)*

One row per CC-ID where `Incumbent Models? = N`. Explicit NONE with justification if none.

Gap Severity criteria:
- HIGH: governs critical-path or financial-close; absence causes material risk or compliance exposure
- MED: governs recommended guard condition; absence causes rework, escalation, or increased errors
- LOW: governs nice-to-have check; absence causes minor inefficiency

`Why As-Is Fails` must name a specific process characteristic. Generic language ("not implemented",
"lacking") is a fail for this column.

| CC-ID | Constraint Name | Gap Severity (HIGH/MED/LOW) | Why As-Is Fails |
|-------|-----------------|----------------------------|-----------------|
| [CC-ID where N] | | | [specific named process characteristic] |

---

**FINAL AUTHORING CHECK**

Before writing output:
- [ ] C-25 BOUNDARY SCAN completed before OAC declared; QUALIFIES set identified
- [ ] PER-ROW QUALITY ARTIFACT REGISTRY (PQAR) section present; all QUALIFIES artifacts have Reg-IDs
- [ ] STATUS-QUO PROCESS DECLARATION is the first section
- [ ] OUTPUT ACCEPTANCE CRITERIA is second with AC-01 through AC-13 all declared
- [ ] AC-13 is LIVE: PQAR-table-backed, update trigger policy declared
- [ ] AC-04 enumerates sub-conditions (a)-(b)-(c) for Phase Delta Block quality
- [ ] AC-10 enumerates sub-conditions (a)-(b)-(c) for CCT quality fields
- [ ] Phase Delta Block schema: inline quality bars embedded in column headers
- [ ] Constraint Chain Table schema: inline quality bars for Handoff Strength + Incumbent Models?
- [ ] CONSTRAINT CHAIN REGISTRY authored before any phase; no blank `Incumbent Models?` cells
- [ ] Status-Quo Role Comparison is dedicated (not embedded in Domain Role Registry)
- [ ] Every phase: Entry Contract with `Imported constraints` + `Incumbent entry`
- [ ] Every phase: Phase Delta Block with inline column-level quality constraints authored before State Table
- [ ] Every phase: Exit Gate with `Exported constraints` + `Incumbent exit`
- [ ] All five artifacts carry `Delta Ref (DL-ID or NONE)` column (exact name)
- [ ] Constraint-Break Exceptions: formal 5-column table; Check V confirmed
- [ ] Constraint Chain Table: Handoff Strength + Incumbent Models? columns; no blank cells
- [ ] Gap Analysis: both `Gap Severity` and `Why As-Is Fails` columns; one row per N-tagged CC-ID
- [ ] If any new per-row quality artifact introduced: Boundary Scan updated, PQAR row added, AC-13 updated
- [ ] Coverage Scan: AC-01 through AC-13 + Check V; AC-04, AC-10, AC-12 sub-conditions confirmed individually; AC-13 cites each PQAR Reg-ID individually

**OUTPUT:** Write to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Status-Quo Process Declaration > C-25 Boundary Scan > Output Acceptance Criteria >
PER-ROW QUALITY ARTIFACT REGISTRY > Domain Role Registry > Status-Quo Role Comparison >
Phase Index > Constraint Chain Registry > Phases (Entry Contract + Phase Delta Block + State
Table + Decision Table + Parallel Path + Exit Gate per phase) > Constraint Chain Table >
Terminal Declaration > Exception Catalog (with Constraint-Break Exceptions subsection) >
Edge Case Catalog > Bottleneck Register > Gap Register > Cross-Process Handoff (optional) >
SLA Annotation (optional) > Coverage Scan (AC-01--AC-13 + Check V) > Inertia Summary
(with Constraint-Incumbent Gap Analysis).
