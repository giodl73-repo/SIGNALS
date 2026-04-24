---
skill: flow-lifecycle
round: 3
date: 2026-03-15
status: VARIATE
variations: 5
rubric: simulations/quest/rubrics/flow-lifecycle-rubric-v3-2026-03-15.md
---

# flow-lifecycle -- Round 3 Variations

Round 3 targets the two new v3 aspirational criteria, both traced to V-04 (Inertia Framing Axis) from R2:
- C-14 As-Is Divergence Anchoring -- every major structural table carries a per-row "As-Is Divergence" column
- C-15 Root-Cause Traceability in Registers -- Bottleneck and Gap registers carry root-cause columns with source references traceable to the artifact field that generated them

Single-axis variations: V-01 (As-Is Column Enforcement), V-02 (Root-Cause Register Schema), V-03 (Phase Delta Block).
Combined variations: V-04 (V-01 + V-02), V-05 (all three R3 axes + C-11/C-12/C-13 from R2).

---

## V-01 -- As-Is Column Enforcement Axis

**Variation axis:** Every major structural table in the lifecycle artifact carries a mandatory "As-Is Divergence" column, populated per row. The column documents what the current process actually does at that row vs. what the model specifies. Empty cells are a fail. A prose summary attached to the table does not substitute for the per-row column.

**Hypothesis:** Adding the As-Is Divergence column to every structural table at the schema level forces per-row gap analysis at the moment of authoring. Rather than assembling a separate gap section after the fact, every state, exception, and edge case carries its own as-is comparison inline. C-14 passes by construction because the schema enforces it. The column also enriches C-04 (bottleneck identification) because as-is divergences naturally reveal where the process is broken, and C-07 (edge case enumeration) because edge cases frequently arise where as-is behavior is hardcoded and the should-be behavior was never implemented.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Every major structural table in this artifact carries a mandatory **As-Is Divergence** column. The column documents what the current process actually does at each row vs. what the model specifies. The column must be populated for every row -- an empty cell is a fail, and a prose summary substituted for a per-row entry is a fail.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

Declare all domain roles before the lifecycle trace opens. Generic labels (user, approver, system) without a domain qualifier are not acceptable. If you cannot name a specific role for a function, name the function gap explicitly.

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned |
|------|------------------------------|--------|-----------------|
| R-01 | | | |
| R-02 | | | |
| ... | | | |

**GATE: Every decision point in the trace must cite an R-ID from this table.**

---

**STEP 2 -- PHASE MAP**

Before tracing states, identify all lifecycle phases. Every state that will be traced belongs to exactly one phase.

| Ph-ID | Phase Name | Purpose | Receives From |
|-------|-----------|---------|--------------|
| PH-01 | | | INITIAL |
| PH-02 | | | PH-01 |
| ... | | | |

---

**STEP 3 -- STATE TRACE**

Trace all named states. The last two columns are required on every row -- empty cells are a fail.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions (labeled) | Owner (R-ID) | As-Is Divergence (Y/N) | Current Practice |
|------|--------------|------------|-----------------|---------------------------|--------------|------------------------|-----------------|
| S-01 | | | | | | | |
| S-02 | | | | | | | |
| ... | | | | | | | |

**Current Practice column rules:**
- Divergence = Y: describe what the current process does differently at this state (wrong role, missing step, different condition, etc.).
- Divergence = N: write "Matches model" -- do not leave empty.
- A row where Current Practice is blank is a fail regardless of the Y/N value.

Decision points: for every branch, label the condition, name the R-ID owner, name each branch path, and provide a fallback path.

| D-ID | Decision | Condition | Owner (R-ID) | Branch A | Branch B | Fallback | As-Is Owner (actual role today or ABSENT) |
|------|----------|-----------|-------------|----------|----------|----------|------------------------------------------|
| | | | | | | | |

Parallel paths: for at least one fork-join:
```
Fork (S-ID):    [branching state]
Branch A:       [path]
Branch B:       [path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
As-Is join:     [how the join works today -- or ABSENT if not implemented]
```

---

**STEP 4 -- EXCEPTION CATALOG**

At least 3 exceptions, each specific to this process. The "As-Is Handling" column is required on every row.

| E-ID | Phase Origin (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | As-Is Handling | Terminal or Recovery (T-ID or S-ID) |
|------|---------------------|---------------|---------|--------------------------|----------------|-------------------------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |
| ... | | | | | | |

**As-Is Handling column rules:**
- If the current process has a defined procedure: describe it.
- If the current process has no defined procedure: write "No defined handling -- [what typically happens in practice]".
- An empty cell is a fail.

After completing the table, identify which phase generates the most exceptions. Name it and provide a one-sentence structural rationale.

---

**STEP 5 -- TERMINAL DECLARATION**

Every traced path and every exception must reach a terminal.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (S-IDs and E-IDs) |
|------|--------------|-----------------------------------|---------------------------------|
| T-01 | | | |
| ... | | | |

---

**STEP 6 -- EDGE CASE CATALOG**

At least 3 edge cases distinct from Step 4 exceptions. The "As-Is Behavior" column is required on every row.

| EC-ID | Edge Case | Phase (Ph-ID) | Trigger | Process Impact | As-Is Behavior | Correct Handling |
|-------|-----------|--------------|---------|----------------|----------------|-----------------|
| EC-01 | | | | | | |
| EC-02 | | | | | | |
| EC-03 | | | | | | |

**As-Is Behavior column rules:**
- If the current process handles this edge case (even poorly): describe the current handling.
- If the current process has no handling: write "Unhandled -- [what falls through in practice]".
- An empty cell is a fail.

---

**STEP 7 -- BOTTLENECK AND GAP REGISTER**

At least 2 bottlenecks and 1 gap.

| ID | Type | Phase (Ph-ID) | Name | Cause | Downstream Impact |
|----|------|--------------|------|-------|-------------------|
| B-01 | bottleneck | | | | |
| B-02 | bottleneck | | | | |
| G-01 | gap | | | | Why it matters: |

---

**CROSS-PROCESS HANDOFF (raise score)**

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition | As-Is Gap (Y/N) |
|-----------------|------------------|---------------|---------------------|----------------|
| | | | | |

**SLA ANNOTATION (raise score)**

At least 3 nodes. "As-Is Typical Duration" is encouraged -- compare to expected duration to determine breach.

| S-ID or Ph-ID | Node Name | Expected Duration | At-Risk Threshold | As-Is Typical Duration | Scenario Breach (Y/N) |
|--------------|-----------|------------------|-------------------|-----------------------|----------------------|
| | | | | | |
| | | | | | |
| | | | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Map > State Trace > Exception Catalog > Terminal Declaration > Edge Case Catalog > Bottleneck and Gap Register > Supplemental sections.

Every major structural table must carry its As-Is column, populated per row. No empty cells in As-Is columns. No prose summary substituted for a per-row entry.

---

## V-02 -- Root-Cause Register Schema Axis

**Variation axis:** The Bottleneck Register and Gap Register each carry a mandatory root-cause column that traces every entry to its source artifact and field using the format `[Artifact] -- [Field]: [value]`. Registers assembled without source references are a fail.

**Hypothesis:** Making root-cause a structured column with a mandatory source-field reference transforms the registers from editorial opinion into derived artifacts. Every bottleneck and gap becomes traceable to a specific field in the lifecycle model (e.g., "Phase Exit Gate PH-03 -- Blocked by: Credit Analyst queue", "State Trace S-07 -- Exception Exit: No defined path"). This forces the author to build the lifecycle model before authoring the registers, and ensures C-15 passes by construction. Populating the source references also acts as a partial coverage scan, because the author must review all exit gates, exception handlers, and divergence annotations to source the root-cause entries.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

The Bottleneck Register and Gap Register must trace every entry to its source artifact and field using this format:

`[Artifact Name] -- [Field Name]: [value from that field]`

Example: `Phase Exit Gate PH-02 -- Blocked by: Pending credit approval sign-off`

Registers assembled without source references or root-cause columns are a fail.

---

**SECTION 1 -- DOMAIN ROLE REGISTRY**

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned |
|------|------------------------------|--------|-----------------|
| R-01 | | | |
| R-02 | | | |
| ... | | | |

Generic labels are a fail. Every decision point in the trace must cite an R-ID.

---

**SECTION 2 -- PHASE MAP AND EXIT GATES**

List all phases. For each phase, the Exit Gate is the primary source artifact for bottleneck root-cause entries -- the "Blocked by" field must be specific.

**Phase Index**

| Ph-ID | Phase Name | Purpose | Receives From |
|-------|-----------|---------|--------------|
| PH-01 | | | INITIAL |
| PH-02 | | | PH-01 |
| ... | | | |

**Phase Exit Gates** (author after tracing each phase's states)

For each phase:
```
Phase: [Ph-ID: Phase Name]
Exit condition:   [What must be true for this phase to complete]
Success:          [Ph-ID of next phase or T-ID]
Failure:          [T-ID or exception name]
Blocked by:       [Specific role, resource, or condition most likely to delay exit -- this is a root-cause source]
Typical duration: [Expected elapsed time]
```

NONE is not acceptable in "Blocked by" unless you explicitly justify why this phase has no common delay source.

---

**SECTION 3 -- STATE TRACE**

Trace all states. For each phase, walk states from phase entry to phase exit.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions (labeled) | Owner (R-ID) | Exception Exit |
|------|--------------|------------|-----------------|---------------------------|--------------|---------------|
| S-01 | | | | | | |
| ... | | | | | | |

Decision points: label condition, name R-ID owner, name all branches, provide fallback.

Parallel paths: model at least one fork-join with named branches, join condition, and merge owner (R-ID).

---

**SECTION 4 -- EXCEPTION CATALOG**

At least 3 exceptions, specific to this process. Phase Origin and As-Is Handling are both required columns.

| E-ID | Phase Origin (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | As-Is Handling | Terminal or Recovery (T-ID or S-ID) |
|------|---------------------|---------------|---------|--------------------------|----------------|-------------------------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |
| ... | | | | | | |

After completing the table, identify the most exception-dense phase and provide a one-sentence structural rationale.

---

**SECTION 5 -- TERMINAL DECLARATION**

Every traced path and every exception must reach a terminal.

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (S-IDs and E-IDs) |
|------|--------------|-----------------------------------|---------------------------------|
| T-01 | | | |
| ... | | | |

---

**SECTION 6 -- EDGE CASE CATALOG**

At least 3 edge cases distinct from Section 4 exceptions.

| EC-ID | Edge Case | Phase (Ph-ID) | Trigger | Process Impact | Correct Handling |
|-------|-----------|--------------|---------|----------------|-----------------|
| EC-01 | | | | | |
| EC-02 | | | | | |
| EC-03 | | | | | |

---

**SECTION 7 -- BOTTLENECK REGISTER**

At least 2 bottlenecks. Every entry must carry a populated Source Artifact, Source Field, and Root Cause. A bottleneck without source references is a fail.

| B-ID | Phase (Ph-ID) | Bottleneck Name | Source Artifact | Source Field | Root Cause | Downstream Impact |
|------|--------------|-----------------|-----------------|--------------|------------|-------------------|
| B-01 | | | | | | |
| B-02 | | | | | | |

**Root Cause format:** `[Source Artifact] -- [Source Field]: [value]`

**Valid source artifacts for bottlenecks:**
- `Phase Exit Gate [Ph-ID]` -- Source Field: `Blocked by`
- `State Trace [S-ID]` -- Source Field: `Exception Exit` (when exception-dense state)
- `Exception Catalog [E-ID]` -- Source Field: `As-Is Handling: No defined handling`
- `Exception Density Note` -- Source Field: `Most exception-dense phase`

**Root Cause examples:**
- `Phase Exit Gate PH-02 -- Blocked by: Credit Analyst approval queue`
- `Exception Catalog E-03 -- As-Is Handling: No defined handling; falls to manual email`
- `State Trace S-07 -- Exception Exit: Approval rejected with no reassignment path`

---

**SECTION 8 -- GAP REGISTER**

At least 1 gap. Every entry must carry a populated Source Artifact, Source Field, and Root Cause.

| G-ID | Phase (Ph-ID) | Gap Name | Source Artifact | Source Field | Root Cause | Harm from Absence |
|------|--------------|---------|-----------------|--------------|------------|------------------|
| G-01 | | | | | | |

**Valid source artifacts for gaps:**
- `State Trace [S-ID]` -- Source Field: `Exception Exit: NONE` (exception handling absent)
- `Exception Catalog [E-ID]` -- Source Field: `As-Is Handling: No defined handling`
- `Phase Exit Gate [Ph-ID]` -- Source Field: `Exit condition` (condition references a step that doesn't exist)
- `Parallel Path` -- Source Field: `Join condition` (condition never evaluated because branch not implemented)

---

**CROSS-PROCESS HANDOFF (raise score)**

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition |
|-----------------|------------------|---------------|---------------------|
| | | | |

**SLA ANNOTATION (raise score)**

| S-ID or Ph-ID | Node Name | Expected Duration | At-Risk Threshold | Scenario Breach (Y/N) |
|--------------|-----------|------------------|-------------------|-----------------------|
| | | | | |
| | | | | |
| | | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Map > Phase Exit Gates (interspersed with state traces per phase) > State Trace > Exception Catalog > Terminal Declaration > Edge Case Catalog > Bottleneck Register > Gap Register > Supplemental sections.

Every row in the Bottleneck Register and Gap Register must carry a populated Root Cause column in the format `[Artifact] -- [Field]: [Value]`. Registers assembled without this structure are a fail. Phase Exit Gate "Blocked by" fields are the primary source -- trace from there.

---

## V-03 -- Phase Delta Block Axis

**Variation axis:** Lifecycle emphasis -- each phase contains a mandatory PHASE DELTA section (a structured delta table with DL-IDs) positioned between the state trace and the exit gate. Delta rows catalog the gap between current (as-is) and modeled (should-be) practice at the item level. Delta entries are the source data for: (1) As-Is Divergence columns in structural tables -- cite the DL-ID; (2) root-cause entries in registers -- cite the DL-ID and field.

**Hypothesis:** Assembling the as-is/should-be gap analysis at the moment of phase authoring -- before advancing to the next phase -- prevents the common failure mode where gap analysis is deferred and becomes editorial opinion rather than evidence. The delta table forces per-item comparison while the phase is fresh. The DL-ID reference system then automatically populates C-14's divergence columns and C-15's root-cause citations, because the delta entries are the traceable source artifacts. The delta also converts bottleneck and gap identification from a separate analysis step to a mechanical read-off of delta rows with HIGH severity.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

The lifecycle is organized by phases. After tracing each phase's states and before declaring the phase exit gate, you must author a **PHASE DELTA** section. The delta section catalogs the gap between the current (as-is) process and the modeled (should-be) lifecycle at the item level. Delta entries are not prose -- they are rows in a delta table with assigned DL-IDs.

Delta entries are the authoritative source for:
1. As-Is Divergence columns in structural tables -- the State Table and Exception Catalog each have a "Delta Ref" column that cites the DL-ID for this row's divergence.
2. Root-cause columns in the Bottleneck and Gap registers -- cite the DL-ID and the "As-Is" field value from the delta row.

---

**SETUP**

**Role Registry**

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned |
|------|------------------------------|--------|-----------------|
| R-01 | | | |
| R-02 | | | |
| ... | | | |

Generic labels are a fail. Every decision point in the lifecycle must cite an R-ID.

**Phase Index**

List all phases before authoring any phase content. Every state belongs to exactly one phase.

| Ph-ID | Phase Name | Purpose | Receives From |
|-------|-----------|---------|--------------|
| PH-01 | | | INITIAL |
| PH-02 | | | PH-01 |
| ... | | | |

---

**FOR EACH PHASE, IN THIS EXACT ORDER:**

---

**PHASE ENTRY CONTRACT [Ph-ID: Phase Name]**

| Field | Value |
|-------|-------|
| Entry condition | [Specific precondition -- must be true for this phase to begin] |
| Prior phase | [Ph-ID or INITIAL] |
| Active roles | [R-IDs active in this phase] |
| Objects entering | [Named artifacts or records entering this phase] |
| Exception pre-check | [Conditions that would block entry and route to exception] |

---

**STATE TABLE [Ph-ID: Phase Name]**

The "Delta Ref" column links each state to the PHASE DELTA row (DL-ID) that documents its as-is divergence. NONE = no divergence at this state.

| S-ID | State Name | Entry Condition | Happy-Path Exit (labeled) | Exception Exit | Owner (R-ID) | Delta Ref (DL-ID or NONE) |
|------|------------|-----------------|--------------------------|----------------|--------------|--------------------------|
| | | | | | | |

**Decision Table [Ph-ID: Phase Name]**

| D-ID | Decision | Condition | Owner (R-ID) | Branch A | Branch B | Fallback | Delta Ref (DL-ID or NONE) |
|------|----------|-----------|-------------|----------|----------|----------|--------------------------|
| | | | | | | | |

**Parallel Path [Ph-ID: Phase Name]** (if parallel execution occurs)
```
Fork (S-ID):    [branching state]
Branch A:       [path]
Branch B:       [path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
As-Is join:     [how this join actually works today -- or ABSENT]
```
If no parallel execution occurs, state that explicitly and identify one parallel path that would improve this phase.

---

**PHASE DELTA [Ph-ID: Phase Name]**

This section is mandatory. Omitting it or replacing it with prose is a fail. Author one row per item that diverges between as-is and should-be practice. If no divergences exist in this phase, write one explicit "no-divergence" row.

| DL-ID | Item Type | Item ID (S-ID / D-ID / other) | Should-Be (model) | As-Is (current practice) | Divergence Type | Gap Severity |
|-------|-----------|-------------------------------|-------------------|--------------------------|-----------------|--------------|
| DL-01 | | | | | | |
| DL-02 | | | | | | |
| ... | | | | | | |

**Item Type vocabulary:** `state`, `decision`, `handoff`, `validation`, `role assignment`, `sequence`

**Divergence Type vocabulary:**
- `role gap` -- wrong role owns this step in current practice
- `missing step` -- this state or decision does not exist in current practice
- `wrong condition` -- current practice uses a different (incorrect) condition
- `absent` -- the entire phase element is absent from current practice
- `none` -- no divergence (use only for the explicit no-divergence row)

**Gap Severity:** HIGH = active harm to process outcomes; MED = workaround exists but creates technical debt; LOW = cosmetic or edge-only impact

If no divergences exist in this phase:
```
DL-XX | ALL | N/A | MATCHES AS-IS | MATCHES AS-IS | none | N/A
```

---

**PHASE EXIT GATE [Ph-ID: Phase Name]**

| Field | Value |
|-------|-------|
| Exit condition | [What must be true for this phase to complete] |
| Success transition | [Ph-ID of next phase or T-ID] |
| Failure transition | [T-ID or exception name] |
| Blocked by | [Specific role, resource, or condition -- NONE requires explicit justification] |
| Typical duration | [Expected elapsed time] |
| Delta source | [DL-IDs of delta rows that explain why this phase is blocked -- or NONE if exit is structurally clean] |

---

*Repeat PHASE ENTRY CONTRACT > STATE TABLE > DECISION TABLE > PARALLEL PATH > PHASE DELTA > PHASE EXIT GATE for each Ph-ID in the Phase Index.*

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (Ph-IDs and E-IDs) |
|------|--------------|-----------------------------------|---------------------------------|
| T-01 | | | |
| ... | | | |

---

**EXCEPTION CATALOG**

At least 3 exceptions, specific to this process. Phase Origin and Delta Ref are required columns.

| E-ID | Phase Origin (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | As-Is Handling | Delta Ref (DL-ID or NONE) | Terminal or Recovery (T-ID or S-ID) |
|------|---------------------|---------------|---------|--------------------------|----------------|--------------------------|-------------------------------------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |
| ... | | | | | | | |

**Exception Density Note:** After completing the table, identify which Ph-ID has the most exceptions. Name it and give a one-sentence structural rationale. Cite at least one DL-ID from that phase's delta table.

---

**EDGE CASE CATALOG**

At least 3 edge cases distinct from the exceptions above.

| EC-ID | Edge Case | Phase (Ph-ID) | Trigger | Process Impact | As-Is Behavior | Delta Ref (DL-ID or NONE) | Correct Handling |
|-------|-----------|--------------|---------|----------------|----------------|--------------------------|-----------------|
| EC-01 | | | | | | | |
| EC-02 | | | | | | | |
| EC-03 | | | | | | | |

---

**BOTTLENECK REGISTER**

Compiled from PHASE EXIT GATE "Blocked by" fields and PHASE DELTA rows with Gap Severity = HIGH or MED. At least 2 bottlenecks. Source reference is required for every row.

| B-ID | Phase (Ph-ID) | Bottleneck | Source (cite DL-ID or Phase Exit Gate [Ph-ID] -- Blocked by) | Root Cause | Downstream Impact |
|------|--------------|-----------|--------------------------------------------------------------|------------|-------------------|
| B-01 | | | | | |
| B-02 | | | | | |

**Root Cause format:** `[Source artifact] -- [Field]: [value]`
Examples:
- `Phase Delta PH-02 DL-04 -- As-Is: No approval routing implemented; emails sent manually`
- `Phase Exit Gate PH-03 -- Blocked by: Regional controller sign-off with no SLA`

A bottleneck without a source citation is a fail.

---

**GAP REGISTER**

Compiled from PHASE DELTA rows with Divergence Type = `missing step` or `absent`. At least 1 gap. Source DL-ID is required.

| G-ID | Phase (Ph-ID) | Gap | Source (DL-ID) | As-Is (from DL-ID row) | Harm from Absence |
|------|--------------|-----|---------------|------------------------|------------------|
| G-01 | | | | | |

A gap without a DL-ID source citation is a fail.

---

**CROSS-PROCESS HANDOFF (raise score)**

```
Handoff trigger:      [Event]
Recipient process:    [Named adjacent process]
Fields passed:        [Named data elements]
Acceptance condition: [What recipient must verify]
As-Is gap:            [Whether the as-is process implements this handoff -- Y/N + note]
Delta source:         [DL-ID if the handoff gap appears in a Phase Delta table]
```

**SLA ANNOTATION (raise score)**

| Gate or S-ID | Node Name | Expected Duration | At-Risk Threshold | As-Is Typical Duration | Scenario Breach (Y/N) |
|-------------|-----------|------------------|-------------------|-----------------------|----------------------|
| | | | | | |
| | | | | | |
| | | | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Index > Phases (entry contract + state table + decision table + parallel path + phase delta + exit gate, in order for each phase) > Terminal Declaration > Exception Catalog > Edge Case Catalog > Bottleneck Register > Gap Register > Supplemental sections.

Every PHASE DELTA section is mandatory. The source column in the Bottleneck and Gap registers must cite a DL-ID or Phase Exit Gate reference. Registers without source citations are a fail. Gap Severity HIGH delta rows without a corresponding bottleneck or gap register entry require justification.

---

## V-04 -- Combined (As-Is Column Enforcement + Root-Cause Register Schema)

**Variation axes combined:**
1. As-Is Divergence columns on every major structural table (C-14 axis from V-01)
2. Root-cause columns in Bottleneck and Gap registers traceable to source artifact fields (C-15 axis from V-02)

**Hypothesis:** The two v3 aspirational axes are structurally linked: the As-Is Divergence columns in the tables are the source data for the root-cause entries in the registers. Running both axes together closes the loop -- divergence is documented where it occurs (per-row in tables), and the registers then aggregate and trace back to those rows by ID and field name. C-14 and C-15 both pass by construction. The register-building step acts as an implicit audit of the As-Is columns, because populating a source reference requires reading the divergence column. This also surfaces any As-Is column that was left empty after the fact.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Two structural rules apply throughout this artifact:

**Rule 1 -- As-Is Divergence columns:** Every major structural table (State Trace, Exception Catalog, Edge Case Catalog) carries a mandatory As-Is column, populated per row. Empty cells are a fail. A prose summary substituted for a per-row entry is a fail.

**Rule 2 -- Root-cause source references:** Every entry in the Bottleneck Register and Gap Register carries a source reference in the format `[Artifact] -- [Field]: [value]`. Registers assembled without this structure are a fail.

---

**STEP 1 -- DOMAIN ROLE REGISTRY**

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned |
|------|------------------------------|--------|-----------------|
| R-01 | | | |
| R-02 | | | |
| ... | | | |

Generic labels are a fail. Every decision point in the trace must cite an R-ID.

---

**STEP 2 -- PHASE MAP**

| Ph-ID | Phase Name | Purpose | Receives From |
|-------|-----------|---------|--------------|
| PH-01 | | | INITIAL |
| PH-02 | | | PH-01 |
| ... | | | |

---

**STEP 3 -- STATE TRACE**

Trace all named states. "As-Is Divergence" and "Current Practice" are required columns on every row.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition | Exit Transitions (labeled) | Owner (R-ID) | As-Is Divergence (Y/N) | Current Practice |
|------|--------------|------------|-----------------|---------------------------|--------------|------------------------|-----------------|
| S-01 | | | | | | | |
| ... | | | | | | | |

**Current Practice rules:**
- Y: describe what the current process does differently at this state.
- N: write "Matches model".
- Empty cell: fail.

Decision points: label condition, name R-ID owner, name all branches, provide fallback path.

| D-ID | Decision | Condition | Owner (R-ID) | Branch A | Branch B | Fallback | As-Is Owner (actual role today or ABSENT) |
|------|----------|-----------|-------------|----------|----------|----------|------------------------------------------|
| | | | | | | | |

Parallel paths: for at least one fork-join:
```
Fork (S-ID):    [branching state]
Branch A:       [path]
Branch B:       [path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
As-Is join:     [how this join actually works today -- or ABSENT]
```

---

**STEP 4 -- PHASE EXIT GATES**

After tracing each phase's states, declare the exit gate. "Blocked by" is the primary source field for bottleneck root-cause entries.

For each phase:
```
Phase: [Ph-ID: Phase Name]
Exit condition:   [What must be true for this phase to complete]
Success:          [Ph-ID or T-ID]
Failure:          [T-ID or exception name]
Blocked by:       [Specific role, resource, or condition -- required; this is a root-cause source field]
Typical duration: [Expected elapsed time]
```

---

**STEP 5 -- EXCEPTION CATALOG**

At least 3 exceptions, specific to this process. Phase Origin and As-Is Handling are required columns.

| E-ID | Phase Origin (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | As-Is Handling | Terminal or Recovery (T-ID or S-ID) |
|------|---------------------|---------------|---------|--------------------------|----------------|-------------------------------------|
| E-01 | | | | | | |
| E-02 | | | | | | |
| E-03 | | | | | | |
| ... | | | | | | |

**As-Is Handling rules:**
- Defined procedure exists: describe it.
- No procedure: write "No defined handling -- [what typically happens]".
- Empty cell: fail.

After completing the table, identify the most exception-dense phase and provide a one-sentence structural rationale.

---

**STEP 6 -- TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (S-IDs and E-IDs) |
|------|--------------|-----------------------------------|---------------------------------|
| T-01 | | | |
| ... | | | |

---

**STEP 7 -- EDGE CASE CATALOG**

At least 3 edge cases distinct from Step 5 exceptions. "As-Is Behavior" is required on every row.

| EC-ID | Edge Case | Phase (Ph-ID) | Trigger | Process Impact | As-Is Behavior | Correct Handling |
|-------|-----------|--------------|---------|----------------|----------------|-----------------|
| EC-01 | | | | | | |
| EC-02 | | | | | | |
| EC-03 | | | | | | |

**As-Is Behavior rules:**
- Current handling exists (even if poor): describe it.
- No handling: write "Unhandled -- [what falls through]".
- Empty cell: fail.

---

**STEP 8 -- BOTTLENECK REGISTER**

At least 2 bottlenecks. Root Cause is required. Source for each entry must reference a specific artifact and field from this artifact.

| B-ID | Phase (Ph-ID) | Bottleneck Name | Source Artifact | Source Field | Root Cause | Downstream Impact |
|------|--------------|-----------------|-----------------|--------------|------------|-------------------|
| B-01 | | | | | | |
| B-02 | | | | | | |

**Root Cause format:** `[Source Artifact] -- [Source Field]: [value]`

**Valid source artifacts for bottlenecks (in priority order):**
1. `Phase Exit Gate [Ph-ID]` -- Source Field: `Blocked by`
2. `State Trace [S-ID]` -- Source Field: `Current Practice` (when divergence = Y and involves delay)
3. `Exception Catalog [E-ID]` -- Source Field: `As-Is Handling` (when value is "No defined handling")
4. `Exception Density Note` -- Source Field: `Most exception-dense phase`

**Root Cause examples:**
- `Phase Exit Gate PH-02 -- Blocked by: Credit analyst queue; no SLA enforced`
- `State Trace S-07 -- Current Practice: Manual email to controller; no tracking`
- `Exception Catalog E-03 -- As-Is Handling: No defined handling; supervisor escalation by phone`

A bottleneck row with empty Source Artifact or empty Root Cause is a fail.

---

**STEP 9 -- GAP REGISTER**

At least 1 gap. Root Cause is required. Source for each entry must reference a specific artifact and field.

| G-ID | Phase (Ph-ID) | Gap Name | Source Artifact | Source Field | Root Cause | Harm from Absence |
|------|--------------|---------|-----------------|--------------|------------|------------------|
| G-01 | | | | | | |

**Valid source artifacts for gaps:**
1. `State Trace [S-ID]` -- Source Field: `Exception Exit: NONE` (exception handling absent)
2. `Exception Catalog [E-ID]` -- Source Field: `As-Is Handling: No defined handling`
3. `Edge Case Catalog [EC-ID]` -- Source Field: `As-Is Behavior: Unhandled`
4. `Phase Exit Gate [Ph-ID]` -- Source Field: `Exit condition` (references a step that doesn't exist in the model)

A gap row with empty Source Artifact or empty Root Cause is a fail.

---

**CROSS-PROCESS HANDOFF (raise score)**

| Handoff Trigger | Recipient Process | Fields Passed | Acceptance Condition | As-Is Gap (Y/N) |
|-----------------|------------------|---------------|---------------------|----------------|
| | | | | |

**SLA ANNOTATION (raise score)**

| S-ID or Ph-ID | Node Name | Expected Duration | At-Risk Threshold | As-Is Typical Duration | Scenario Breach (Y/N) |
|--------------|-----------|------------------|-------------------|-----------------------|----------------------|
| | | | | | |
| | | | | | |
| | | | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Map > State Trace > Phase Exit Gates > Exception Catalog > Terminal Declaration > Edge Case Catalog > Bottleneck Register > Gap Register > Supplemental sections.

**Completion checklist before writing:**
- Every State Trace row: As-Is Divergence column populated (not blank).
- Every Exception Catalog row: As-Is Handling column populated (not blank).
- Every Edge Case Catalog row: As-Is Behavior column populated (not blank).
- Every Bottleneck Register row: Source Artifact + Root Cause columns populated; Root Cause uses `[Artifact] -- [Field]: [value]` format.
- Every Gap Register row: Source Artifact + Root Cause columns populated; same format.

Any unchecked item in this list is a fail.

---

## V-05 -- Combined (All Three R3 Axes + Phase Gates + Coverage Scan + Exception Density)

**Variation axes combined:**
1. As-Is Divergence columns on all major tables (C-14 -- V-01 axis)
2. Root-cause register schema with source traceability (C-15 -- V-02 axis)
3. Phase Delta blocks as the derivation source for both (lifecycle emphasis -- V-03 axis)
4. Phase Entry Contract + Phase Exit Gate formalization (C-11 -- from R2 V-03)
5. Post-fill Coverage Scan (C-12 -- from R2 V-01)
6. Exception Phase Attribution + Density Analysis (C-13 -- from R2 V-02)

**Hypothesis:** All six axes are mechanically linked. Phase Delta blocks generate source references (DL-IDs). As-Is Divergence columns consume them in structural tables. Root-cause registers aggregate them into the Bottleneck and Gap registers. Phase entry contracts constrain phase boundaries at entry. Phase exit gates constrain them at exit. The coverage scan verifies completeness after all phases are authored. Exception density analysis surfaces which phases are structurally brittle. Running all six creates an artifact where C-14 and C-15 pass by construction from the delta tables, C-11/C-12/C-13 pass by schema enforcement, and the five essential criteria (C-01/C-02/C-03/C-04/C-05) are nearly impossible to fail because each has multiple independent enforcement points. Cost: substantial prompt length and author overhead. Benefit: the artifact cannot close with status OPEN.

---

You are a business-process simulation expert. Simulate the full lifecycle of the document or process named in the signal.

Work in three layers:
- **Layer 1 -- Phase-Gated Lifecycle:** Build the model phase by phase with mandatory entry contracts, phase delta blocks, and exit gates.
- **Layer 2 -- Exception Attribution and Density:** Catalog exceptions by phase, analyze density, and compile registers with source-traceable root causes.
- **Layer 3 -- Coverage Scan:** Verify completeness state-by-state, exception-by-exception, and phase-by-phase before writing the artifact.

All three layers are required. An artifact missing any layer is incomplete.

---

**LAYER 0: SETUP**

**Role Registry**

| R-ID | Role Name (domain-qualified) | Domain | Decisions Owned |
|------|------------------------------|--------|-----------------|
| R-01 | | | |
| R-02 | | | |
| ... | | | |

Generic labels are a fail. Every decision point must cite an R-ID.

**Phase Index**

List all phases before authoring any phase content. Every state belongs to exactly one phase.

| Ph-ID | Phase Name | Purpose | Receives From |
|-------|-----------|---------|--------------|
| PH-01 | | | INITIAL |
| PH-02 | | | PH-01 |
| ... | | | |

---

**LAYER 1: PHASE-GATED LIFECYCLE**

For each phase in the Phase Index, author in this exact order:

---

**PHASE ENTRY CONTRACT [Ph-ID: Phase Name]**

Information about phase entry that appears only in prose outside this schema does not count for C-11.

| Field | Required? | Value |
|-------|-----------|-------|
| Entry condition | YES | [Specific precondition -- must be true for this phase to begin] |
| Prior phase | YES | [Ph-ID or INITIAL] |
| Active roles | YES | [R-IDs active in this phase] |
| Objects entering | YES | [Named artifacts or records entering this phase] |
| Exception pre-check | YES | [Conditions that block entry and route to exception] |

---

**STATE TABLE [Ph-ID: Phase Name]**

"As-Is Divergence" and "Delta Ref" are required columns.

| S-ID | State Name | Entry Condition | Happy-Path Exit (labeled) | Exception Exit | Owner (R-ID) | As-Is Divergence (Y/N) | Delta Ref (DL-ID or NONE) |
|------|------------|-----------------|--------------------------|----------------|--------------|------------------------|--------------------------|
| | | | | | | | |

**Decision Table [Ph-ID: Phase Name]**

| D-ID | Decision | Condition | Owner (R-ID) | Branch A | Branch B | Fallback | Delta Ref (DL-ID or NONE) |
|------|----------|-----------|-------------|----------|----------|----------|--------------------------|
| | | | | | | | |

**Parallel Path [Ph-ID: Phase Name]**

If parallel execution occurs:
```
Fork (S-ID):    [branching state]
Branch A:       [path]
Branch B:       [path]
Join condition: [what must hold before merge]
Merge owner:    [R-ID]
As-Is join:     [how this join actually works today -- or ABSENT]
```
If no parallel execution: state that explicitly and identify one parallel path that would improve this phase.

---

**PHASE DELTA [Ph-ID: Phase Name]**

Mandatory. Replacing with prose is a fail. Author one row per item that diverges between as-is and should-be. If no divergences exist, author one explicit no-divergence row.

| DL-ID | Item Type | Item ID | Should-Be (model) | As-Is (current practice) | Divergence Type | Gap Severity |
|-------|-----------|---------|-------------------|--------------------------|-----------------|--------------|
| DL-01 | | | | | | |
| DL-02 | | | | | | |
| ... | | | | | | |

**Divergence Type:** `role gap` / `missing step` / `wrong condition` / `absent` / `none`
**Gap Severity:** HIGH / MED / LOW

No-divergence row format: `DL-XX | ALL | N/A | MATCHES AS-IS | MATCHES AS-IS | none | N/A`

---

**PHASE EXIT GATE [Ph-ID: Phase Name]**

Information about phase exit that appears only in prose outside this schema does not count for C-11. "Blocked by" is mandatory -- NONE requires explicit justification.

| Field | Required? | Value |
|-------|-----------|-------|
| Exit condition | YES | [What must be true for phase to complete] |
| Success transition | YES | [Ph-ID of next phase or T-ID] |
| Failure transition | YES | [T-ID or exception name] |
| Blocked by | YES | [Specific role, resource, or condition most likely to delay exit] |
| Typical cycle time | YES | [Expected elapsed time] |
| Delta source | YES | [DL-IDs that explain this phase's blockage -- or NONE if exit is structurally clean] |

---

*Repeat PHASE ENTRY CONTRACT > STATE TABLE > DECISION TABLE > PARALLEL PATH > PHASE DELTA > PHASE EXIT GATE for each Ph-ID.*

---

**TERMINAL DECLARATION**

| T-ID | Terminal Name | Type (success / failure / cancel) | Reached From (Ph-IDs and E-IDs) |
|------|--------------|-----------------------------------|---------------------------------|
| T-01 | | | |
| ... | | | |

---

**LAYER 2: EXCEPTION ATTRIBUTION, DENSITY, REGISTERS**

**Exception Catalog**

At least 3 exceptions, specific to this process. Phase Origin, As-Is Handling, and Delta Ref are required columns.

| E-ID | Phase Origin (Ph-ID) | Exception Name | Trigger | Deviation from Happy Path | As-Is Handling | Delta Ref (DL-ID or NONE) | Terminal or Recovery (T-ID or S-ID) |
|------|---------------------|---------------|---------|--------------------------|----------------|--------------------------|-------------------------------------|
| E-01 | | | | | | | |
| E-02 | | | | | | | |
| E-03 | | | | | | | |
| ... | | | | | | | |

**Exception Density Analysis**

| Ph-ID | Phase Name | Exception Count | Exception IDs |
|-------|-----------|-----------------|--------------|
| PH-01 | | | |
| PH-02 | | | |
| ... | | | |
| Total | | | |

Density finding (required):
```
Most exception-dense phase: [Ph-ID: Phase Name] -- [N] exceptions
Structural rationale:       [Why -- role handoff, data quality, timing pressure, absent validation, etc.]
Delta confirmation:         [DL-ID from this phase's delta table that corroborates the density finding]
Improvement implication:    [What structural change to this phase would reduce exception count]
```

A density finding without a structural rationale and DL-ID citation is a fail.

**Edge Case Catalog**

At least 3 edge cases distinct from the exceptions above. As-Is Behavior and Delta Ref are required columns.

| EC-ID | Edge Case | Phase (Ph-ID) | Trigger | Process Impact | As-Is Behavior | Delta Ref (DL-ID or NONE) | Correct Handling |
|-------|-----------|--------------|---------|----------------|----------------|--------------------------|-----------------|
| EC-01 | | | | | | | |
| EC-02 | | | | | | | |
| EC-03 | | | | | | | |

**Bottleneck Register**

Compiled from Phase Exit Gate "Blocked by" fields and Phase Delta rows with Gap Severity = HIGH or MED. At least 2 bottlenecks. Source reference required.

| B-ID | Phase (Ph-ID) | Bottleneck | Source Artifact | Source Field | Root Cause | Downstream Impact |
|------|--------------|-----------|-----------------|--------------|------------|-------------------|
| B-01 | | | | | | |
| B-02 | | | | | | |

**Root Cause format:** `[Source Artifact] -- [Source Field]: [value]`

Valid source artifacts:
- `Phase Exit Gate [Ph-ID]` -- `Blocked by`
- `Phase Delta [Ph-ID] DL-[ID]` -- `As-Is`
- `State Trace [S-ID]` -- `As-Is Divergence + Current Practice`
- `Exception Catalog [E-ID]` -- `As-Is Handling`

**Gap Register**

Compiled from Phase Delta rows with Divergence Type = `missing step` or `absent`. At least 1 gap. DL-ID source citation required.

| G-ID | Phase (Ph-ID) | Gap | Source Artifact | Source Field | Root Cause | Harm from Absence |
|------|--------------|-----|-----------------|--------------|------------|------------------|
| G-01 | | | | | | |

Root Cause format: `Phase Delta [Ph-ID] DL-[ID] -- As-Is: [value from delta row]`

---

**LAYER 3: COVERAGE SCAN**

After completing Layers 1 and 2, run this scan. The artifact may not be written with status OPEN.

**Scan Table A -- State Coverage**

One row per S-ID from all State Tables across all phases.

| S-ID | Phase (Ph-ID) | State Name | Entry Condition Present? (Y/N) | Labeled Exit Present? (Y/N) | Reaches Terminal? (T-ID or OPEN) | As-Is Divergence Column Populated? (Y/N) | Resolution (if OPEN) |
|------|--------------|------------|-------------------------------|----------------------------|----------------------------------|------------------------------------------|----------------------|
| | | | | | | | |
| ... | | | | | | | |

Rules:
- "Entry Condition Present" -- Y only if entry condition appears in the State Table row, not only in prose.
- "Labeled Exit Present" -- Y only if exit transition is named, not implied.
- "Reaches Terminal" -- write T-ID. OPEN requires resolution before closing.
- "As-Is Divergence Column Populated" -- Y only if the As-Is Divergence cell in the State Table is non-empty. N requires filling the cell before closing.

**Scan Table B -- Exception Coverage**

One row per E-ID.

| E-ID | Phase Origin Present? (Y/N) | As-Is Handling Present? (Y/N) | Has Terminal or Recovery? (Y/N) | Terminal/Recovery ID | In Density Analysis? (Y/N) |
|------|----------------------------|------------------------------|--------------------------------|---------------------|--------------------------|
| | | | | | |
| ... | | | | | |

**Scan Table C -- Phase Gate Coverage**

One row per Ph-ID.

| Ph-ID | Phase Name | Entry Contract Present? (Y/N) | Phase Delta Present? (Y/N) | Exit Gate Present? (Y/N) | "Blocked by" Populated? (Y/N) | "Delta source" Populated? (Y/N) | Success Transition Named? (Y/N) | Failure Transition Named? (Y/N) |
|-------|-----------|------------------------------|--------------------------|--------------------------|-------------------------------|--------------------------------|--------------------------------|--------------------------------|
| | | | | | | | | |
| ... | | | | | | | | |

**Scan Table D -- Register Source Coverage**

One row per Bottleneck Register entry and one row per Gap Register entry.

| Register ID (B-ID or G-ID) | Register Type | Source Artifact Populated? (Y/N) | Root Cause in Required Format? (Y/N) | Resolution (if N) |
|---------------------------|--------------|----------------------------------|--------------------------------------|------------------|
| | | | | |
| ... | | | | |

**Scan Summary**

```
Total states scanned:                    [N]
States with open paths:                  [N] -- list S-IDs
States with missing entry condition:     [N] -- list S-IDs
States with As-Is Divergence empty:      [N] -- list S-IDs
Total exceptions scanned:               [N]
Exceptions without phase origin:         [N] -- list E-IDs
Exceptions without As-Is Handling:       [N] -- list E-IDs
Exceptions without resolution:           [N] -- list E-IDs
Total phases scanned:                   [N]
Phases missing entry contract:           [N] -- list Ph-IDs
Phases missing phase delta:              [N] -- list Ph-IDs
Phases missing exit gate:                [N] -- list Ph-IDs
Phases with "Blocked by" empty:          [N] -- list Ph-IDs
Phases with "Delta source" empty:        [N] -- list Ph-IDs
Register entries missing source refs:    [N] -- list B-IDs and G-IDs
Artifact status:                         CLOSED / OPEN
```

If status is OPEN, list all remaining open items and resolve them before writing the artifact.

---

**CROSS-PROCESS HANDOFF (raise score)**

```
Handoff trigger:      [Event]
Recipient process:    [Named adjacent process]
Fields passed:        [Named data elements]
Acceptance condition: [What recipient must verify]
As-Is gap:            [Whether as-is process implements this handoff -- Y/N + note]
Delta source:         [DL-ID if handoff gap appears in a Phase Delta table]
```

**SLA ANNOTATION (raise score)**

At least 3 nodes from Phase Exit Gates or State Tables:

| Gate or S-ID | Node Name | Expected Duration | At-Risk Threshold | As-Is Typical Duration | Scenario Breach (Y/N) |
|-------------|-----------|------------------|-------------------|-----------------------|----------------------|
| | | | | | |
| | | | | | |
| | | | | | |

---

**OUTPUT**

Write the lifecycle artifact to `simulations/flow/lifecycle/{topic}-lifecycle-{date}.md`.

Structure: Role Registry > Phase Index > Phases (entry contract + state table + decision table + parallel path + phase delta + exit gate, in order for each phase) > Terminal Declaration > Exception Catalog > Exception Density Analysis > Edge Case Catalog > Bottleneck Register > Gap Register > Coverage Scan (all four tables + summary) > Supplemental sections.

**The artifact may not be written until Scan Summary shows status CLOSED.** Every S-ID, E-ID, and Ph-ID must appear in the scan tables. Every required column cell must be populated. Every register entry must have a root-cause source reference in the required format. Any unchecked item is a fail.
