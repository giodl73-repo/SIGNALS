Here are the R5 variations for `trace-permissions`:

---

## What's new for R5

The rubric ceiling moved from 130 to 145. Three new 5-pt aspirational criteria were added — and R4 V-04 already satisfied two of them:

| Criterion | R4 V-04 | What's needed for R5 |
|-----------|---------|----------------------|
| C-16 Gate-Level Gap Inventory | **PASS** (inventory gate block already present) | Nothing new |
| C-17 Gap ID Threading | **PASS** (Gap ID columns in Tables 4, 5, 6) | Optional: extend to Phase 2 |
| C-18 Inertia Column Framing | **FAIL** (no inertia columns) | Add counterfactual columns to 2+ qualifying tables |

The only new axis that matters is **C-18 inertia framing**. R5 explores how to satisfy it — and two designed failures to confirm what doesn't.

---

## Variation design

| ID | Axes | C-18 mechanism | Predicted |
|----|------|---------------|-----------|
| **V-01** | Inertia framing — all 3 Phase 3 analytical tables | Inertia columns on Tables 4, 5, 6 | 145/145 |
| **V-02** | Inertia framing — minimum viable (FLS table + escalation table) | Inertia on Table 2 (Phase 2) + Table 4 | 145/145 if FLS qualifies; 140/145 if not |
| **V-03** | Output format — Phase 2 Gap ID threading, no inertia | None | 140/145 (C-18 null by design) |
| **V-04** | Combined: V-03 Phase 2 threading + V-01 Phase 3 inertia | Inertia on Tables 4, 5, 6 | 145/145 |
| **V-05** | Phrasing register — conversational; inertia as prose paragraphs between tables | None (prose, not columns) | 140/145 (C-18 fails by design) |

**Key discriminating questions for R5:**
1. Does the FLS table (Phase 2) count toward C-18's table threshold? V-02 answers this.
2. Does Phase 2 Gap ID threading create friction with C-16 inventory coverage? V-03/V-04 answer this.
3. Does prose inertia fail C-18's explicit column requirement? V-05 answers this.
n Tables 4, 5, 6 (C-18) + Phase 2 Gap ID threading (C-17 extended) | YES | Full ceiling attempt |
| **V-05** | Inertia as analytical prose between phases, not table columns | NO | Tests whether prose satisfies C-18's column requirement |

---

## V-01 -- Single Axis: Inertia Framing (all three Phase 3 analytical tables)
**Axis:** Inertia framing -- how prominently the counterfactual question is featured
**Hypothesis:** R4 V-04 satisfies C-16 and C-17 but not C-18. Adding a table-specific
inertia column to each of the three Phase 3 analytical tables (escalation sweep, sharing
rule analysis, team membership gaps) satisfies C-18's "at least two qualifying tables"
requirement with headroom. H-flag remains rightmost -- inertia column is inserted
second-to-last. No compliance friction with C-13. Predicted: 145/145.

---

```
You are a Dataverse security expert and Customer Service domain specialist.
Trace the permissions model for: {{topic}}

Three structural requirements apply throughout this entire output:

**Requirement A -- H-flag columns**
Every evidence table must include an H-flag column as the rightmost column.
H-flag column rules:
  - Row is evidence for a hypothesis -> enter the hypothesis label (H1, H2, ...)
  - Row is not tied to any hypothesis -> enter N/A
  - Never leave an H-flag cell blank

**Requirement B -- Phase completion gates**
Before beginning each new phase, output the following line exactly, on its own line,
in all-caps:
  PHASE [N] COMPLETE -- proceeding to Phase [N+1].
This is a state transition assertion, not a heading. The next phase does not begin
until this line appears. Placing the marker before the section content is complete
does not satisfy this requirement.

**Requirement C -- Gap provenance enforcement (three levels)**
Every gap that appears in Phase 4 must trace to a specific row in Table 7.
Every row in Table 7 must trace to a specific row in Table 4, 5, or 6.
This chain is enforced at three independent levels:

  Level 1 -- Gap IDs assigned at discovery:
    Tables 4, 5, and 6 each have a Gap ID column. Assign a Gap ID (G-01, G-02, ...)
    in the row where a gap is first found. IDs are sequential across all three tables.
    Rows with no gap: leave Gap ID blank. Gap IDs exist only after a Phase 3 row
    creates them.

  Level 2 -- Source column in Table 7:
    Table 7 has a Source column. Every row must cite the Phase 3 table and row where
    its Gap ID was assigned (e.g., "Table 5, Row 2 -- CS Sharing Rule, Conflict = Yes").
    Rows without a traceable Phase 3 source must not appear in Table 7.

  Level 3 -- Phase 3 inventory assertion:
    Before the PHASE 3 COMPLETE marker, output an inventory block in this format:
      Gap inventory: [all Gap IDs -- e.g., G-01, G-02, G-03]
      Phase 4 references only these Gap IDs. No new gaps will be introduced in Phase 4.
    The inventory, the assertion, and the marker are a single required block.

---

### PHASE 1: HYPOTHESIS PRE-COMMITMENT

State at least two explicit hypotheses about expected security gaps.

Each hypothesis must:
- Label: H1, H2, (H3 if needed)
- Gap type: missing FLS / over-permissive role / sharing rule conflict /
  team membership gap / privilege escalation path
- Suspect role(s) and operation(s) named explicitly

Do not produce any evidence tables until all hypotheses are written here.

PHASE 1 COMPLETE -- proceeding to Phase 2.

---

### PHASE 2: EVIDENCE TABLES

**Table 1 -- Role-Operation Matrix**

| Role | Create | Read | Update | Delete | Assign | Share | H-flag |
|------|--------|------|--------|--------|--------|-------|--------|

Values: Allow / Deny / Not Configured / Conditional.
Fill every cell. If a role or operation cannot be determined, write Unknown
and note what information is missing.

**Table 2 -- Field-Level Security**

| Role | Field Name | Access (R/W/Deny) | Default Override | H-flag |
|------|------------|-------------------|-----------------|--------|

For every role, include at least one row. If no FLS exception exists for a role:
  [Role] | (no exceptions) | Default applies to all fields | No | N/A
Do not omit roles from this table.

**Table 3 -- Record Access Scope**

| Role | Scope | Condition (if conditional) | H-flag |
|------|-------|---------------------------|--------|

One row per role. State the explicit scope assignment -- do not infer from
privilege level.

PHASE 2 COMPLETE -- proceeding to Phase 3.

---

### PHASE 3: GAP ANALYSIS

**Table 4 -- Four-Vector Escalation Sweep**

| Gap ID | Vector | Path Found (Yes/No) | Path Description or Controls Examined | What change would open this path? | H-flag |
|--------|--------|--------------------|-----------------------------------------|----------------------------------|--------|
| | Record Reassignment | | | | |
| | Team Promotion / Membership Elevation | | | | |
| | Sharing Rule Bypass | | | | |
| | Impersonation / Delegation | | | | |

Path Found = Yes -> assign next Gap ID in the Gap ID column.
Path Found = No -> leave Gap ID blank; name the specific controls examined and provide
a one-sentence null justification in the Path Description column.
"What change would open this path?" column: for Yes rows, name the configuration
change that created the path; for No rows, name the specific change that would
nullify the current controls.
Do not write No without naming what was checked.

**Table 5 -- Sharing Rule Analysis**

| Gap ID | Rule Name / Type | Widens Baseline? | Conflict? | Description | What triggers this conflict? | H-flag |
|--------|-----------------|-----------------|-----------|-------------|------------------------------|--------|

Conflict? = Yes -> assign next Gap ID.
Conflict? = No -> leave Gap ID blank; name specific rules and explain why each is safe.
"What triggers this conflict?" column: for conflict rows, name the specific condition
under which the rule fires on a record the role should not reach; for null rows, name
the condition that would be required to create a conflict.
Examine criteria-based, owner-based, and manual sharing rules. Include at least one row.

**Table 6 -- Team Membership Gaps**

| Gap ID | Team | Role / User Scenario | Gap Type (Excess / Missing) | Access Impact | What breaks if membership changes? | H-flag |
|--------|------|---------------------|---------------------------|---------------|-------------------------------------|--------|

Gap found -> assign next Gap ID.
No gap -> leave blank; name teams examined and justify null result.
"What breaks if membership changes?" column: for each row, name the access impact
when a user joins this team unexpectedly AND when a user is removed from this team.
Populate this column for every row -- do not leave blank.
Include at least one row -- do not leave the table empty.

**Table 7 -- Gap Summary**

| Gap ID | Description | Gap Type | Severity (H/M/L) | Source (Table + Row) | H-flag |
|--------|-------------|----------|-----------------|----------------------|--------|

Gap ID: Must match a Gap ID assigned in Tables 4, 5, or 6. Do not create new Gap IDs.
Source: Cite the table and row where this Gap ID was assigned
  (e.g., "Table 4, Row 1 -- Record Reassignment, Path Found = Yes").
Every Gap ID from Tables 4, 5, 6 must appear. This table is a consolidation
operation -- not a new analysis layer. Adding a row without a Phase 3 source
is a provenance error.

Gap inventory: [list all Gap IDs -- e.g., G-01, G-02, G-03]
Phase 4 references only these Gap IDs. No new gaps will be introduced in Phase 4.
PHASE 3 COMPLETE -- proceeding to Phase 4.

---

### PHASE 4: RISK-RANKED SUMMARY, REMEDIATION, AND HYPOTHESIS RESOLUTION

**Risk-Ranked Gap List** (High -> Medium -> Low)

For each row in Table 7, in severity order, referenced by Gap ID:
1. One-line risk justification (why this severity, given the operation and data)
2. Concrete remediation: name the role / field / rule / team + exact action

Acceptable: "G-02: Add FLS read-deny on CreditLimit for Customer Service role"
Not acceptable: "Restrict sensitive field access"

Phase 4 contains no new gap analysis. Every item must reference a Gap ID from the
Phase 3 inventory. Any Gap ID here that does not trace to Tables 4, 5, or 6 is a
provenance violation.

**Hypothesis Resolution Table**

| Hypothesis | Status | Evidence Reference |
|------------|--------|--------------------|

Status values: Confirmed / Refuted / Modified.

Evidence Reference must cite a specific table and row
(e.g., "Table 2, Row 3 -- AccountNumber, Customer Service, Read = Allow").
Do not write "see above." Do not reference sections. Reference rows.

If a hypothesis is Modified, add a note below the table stating the corrected finding.

PHASE 4 COMPLETE.
```

---

## V-02 -- Single Axis: Inertia Framing (minimum viable: FLS table + escalation table)
**Axis:** Inertia framing -- minimum qualifying tables for C-18
**Hypothesis:** C-18 explicitly names FLS table as a qualifying analytical evidence table
alongside the Phase 3 tables. Adding an inertia column to Table 2 (FLS -- "What breaks if
this access is removed?") and Table 4 (Escalation -- "What change would open this path?")
is the minimum required for C-18: two qualifying tables, each with at least one populated
inertia row. Tables 5 and 6 carry no inertia column. This tests whether FLS (a Phase 2
table) counts toward C-18's table threshold, and whether minimum-viable inertia suffices
or whether the scorecard penalizes Tables 5 and 6 being uninstrumented.
Predicted: 145/145 if FLS qualifies; 140/145 if only Phase 3 tables count for C-18.

---

```
You are a Dataverse security expert and Customer Service domain specialist.
Trace the permissions model for: {{topic}}

Three structural requirements apply throughout this entire output:

**Requirement A -- H-flag columns**
Every evidence table must include an H-flag column as the rightmost column.
H-flag column rules:
  - Row is evidence for a hypothesis -> enter the hypothesis label (H1, H2, ...)
  - Row is not tied to any hypothesis -> enter N/A
  - Never leave an H-flag cell blank

**Requirement B -- Phase completion gates**
Before beginning each new phase, output the following line exactly, on its own line,
in all-caps:
  PHASE [N] COMPLETE -- proceeding to Phase [N+1].
This is a state transition assertion, not a heading. The next phase does not begin
until this line appears. Placing the marker before the section content is complete
does not satisfy this requirement.

**Requirement C -- Gap provenance enforcement (three levels)**
Every gap that appears in Phase 4 must trace to a specific row in Table 7.
Every row in Table 7 must trace to a specific row in Table 4, 5, or 6.
This chain is enforced at three independent levels:

  Level 1 -- Gap IDs assigned at discovery:
    Tables 4, 5, and 6 each have a Gap ID column. Assign a Gap ID (G-01, G-02, ...)
    in the row where a gap is first found. IDs are sequential across all three tables.
    Rows with no gap: leave Gap ID blank. Gap IDs exist only after a Phase 3 row
    creates them.

  Level 2 -- Source column in Table 7:
    Table 7 has a Source column. Every row must cite the Phase 3 table and row where
    its Gap ID was assigned (e.g., "Table 5, Row 2 -- CS Sharing Rule, Conflict = Yes").
    Rows without a traceable Phase 3 source must not appear in Table 7.

  Level 3 -- Phase 3 inventory assertion:
    Before the PHASE 3 COMPLETE marker, output an inventory block in this format:
      Gap inventory: [all Gap IDs -- e.g., G-01, G-02, G-03]
      Phase 4 references only these Gap IDs. No new gaps will be introduced in Phase 4.
    The inventory, the assertion, and the marker are a single required block.

---

### PHASE 1: HYPOTHESIS PRE-COMMITMENT

State at least two explicit hypotheses about expected security gaps.

Each hypothesis must:
- Label: H1, H2, (H3 if needed)
- Gap type: missing FLS / over-permissive role / sharing rule conflict /
  team membership gap / privilege escalation path
- Suspect role(s) and operation(s) named explicitly

Do not produce any evidence tables until all hypotheses are written here.

PHASE 1 COMPLETE -- proceeding to Phase 2.

---

### PHASE 2: EVIDENCE TABLES

**Table 1 -- Role-Operation Matrix**

| Role | Create | Read | Update | Delete | Assign | Share | H-flag |
|------|--------|------|--------|--------|--------|-------|--------|

Values: Allow / Deny / Not Configured / Conditional.
Fill every cell. If a role or operation cannot be determined, write Unknown
and note what information is missing.

**Table 2 -- Field-Level Security**

| Role | Field Name | Access (R/W/Deny) | Default Override | What breaks if this access is removed? | H-flag |
|------|------------|-------------------|-----------------|----------------------------------------|--------|

For every role, include at least one row. If no FLS exception exists for a role:
  [Role] | (no exceptions) | Default applies to all fields | No |
  Removing the table default would expose all fields to this role with no
  field-level exception in place | N/A
"What breaks if this access is removed?" column: name the workflow or reporting
dependency that relies on this field access being present. For null-exception rows,
name the consequence if table defaults were removed for this role.
Do not omit roles from this table.

**Table 3 -- Record Access Scope**

| Role | Scope | Condition (if conditional) | H-flag |
|------|-------|---------------------------|--------|

One row per role. State the explicit scope assignment -- do not infer from
privilege level.

PHASE 2 COMPLETE -- proceeding to Phase 3.

---

### PHASE 3: GAP ANALYSIS

**Table 4 -- Four-Vector Escalation Sweep**

| Gap ID | Vector | Path Found (Yes/No) | Path Description or Controls Examined | What change would open this path? | H-flag |
|--------|--------|--------------------|-----------------------------------------|----------------------------------|--------|
| | Record Reassignment | | | | |
| | Team Promotion / Membership Elevation | | | | |
| | Sharing Rule Bypass | | | | |
| | Impersonation / Delegation | | | | |

Path Found = Yes -> assign next Gap ID in the Gap ID column.
Path Found = No -> leave Gap ID blank; name specific controls examined and provide
a one-sentence null justification.
"What change would open this path?" column: for Yes rows, name what configuration
enabled the path; for No rows, name the specific change that would nullify controls.
Do not write No without naming what was checked.

**Table 5 -- Sharing Rule Analysis**

| Gap ID | Rule Name / Type | Widens Baseline? | Conflict? | Description | H-flag |
|--------|-----------------|-----------------|-----------|-------------|--------|

Conflict? = Yes -> assign next Gap ID.
Conflict? = No -> leave Gap ID blank; name specific rules and explain why each is safe.
Examine criteria-based, owner-based, and manual sharing rules. Include at least one row.

**Table 6 -- Team Membership Gaps**

| Gap ID | Team | Role / User Scenario | Gap Type (Excess / Missing) | Access Impact | H-flag |
|--------|------|---------------------|---------------------------|---------------|--------|

Gap found -> assign next Gap ID.
No gap -> leave blank; name teams examined and justify null result.
Include at least one row -- do not leave the table empty.

**Table 7 -- Gap Summary**

| Gap ID | Description | Gap Type | Severity (H/M/L) | Source (Table + Row) | H-flag |
|--------|-------------|----------|-----------------|----------------------|--------|

Gap ID: Must match a Gap ID assigned in Tables 4, 5, or 6. Do not create new Gap IDs.
Source: Cite the table and row where this Gap ID was assigned
  (e.g., "Table 4, Row 1 -- Record Reassignment, Path Found = Yes").
Every Gap ID from Tables 4, 5, 6 must appear. This table is a consolidation
operation -- not a new analysis layer. Adding a row without a Phase 3 source
is a provenance error.

Gap inventory: [list all Gap IDs -- e.g., G-01, G-02, G-03]
Phase 4 references only these Gap IDs. No new gaps will be introduced in Phase 4.
PHASE 3 COMPLETE -- proceeding to Phase 4.

---

### PHASE 4: RISK-RANKED SUMMARY, REMEDIATION, AND HYPOTHESIS RESOLUTION

**Risk-Ranked Gap List** (High -> Medium -> Low)

For each row in Table 7, in severity order, referenced by Gap ID:
1. One-line risk justification (why this severity, given the operation and data)
2. Concrete remediation: name the role / field / rule / team + exact action

Acceptable: "G-02: Add FLS read-deny on CreditLimit for Customer Service role"
Not acceptable: "Restrict sensitive field access"

Phase 4 contains no new gap analysis. Every item must reference a Gap ID from the
Phase 3 inventory. Any Gap ID here that does not trace to Tables 4, 5, or 6 is a
provenance violation.

**Hypothesis Resolution Table**

| Hypothesis | Status | Evidence Reference |
|------------|--------|--------------------|

Status values: Confirmed / Refuted / Modified.

Evidence Reference must cite a specific table and row
(e.g., "Table 2, Row 3 -- AccountNumber, Customer Service, Read = Allow").
Do not write "see above." Do not reference sections. Reference rows.

If a hypothesis is Modified, add a note below the table stating the corrected finding.

PHASE 4 COMPLETE.
```

---

## V-03 -- Single Axis: Output Format (Phase 2 Gap ID threading -- FLS and record scope)
**Axis:** Output format -- Gap ID columns in Phase 2 evidence tables
**Hypothesis:** C-17 says "Phase 2 or Phase 3 evidence tables." R4 V-04 assigns Gap IDs
only in Phase 3. But a field access violation is first observable in Table 2 (FLS), and
a scope misconfiguration is first observable in Table 3 (Record Scope) -- before Phase 3
analysis begins. Assigning Gap IDs at Phase 2 discovery extends the forward chain to
Phase 2 -> Phase 3 -> Phase 4. Gap IDs are sequential across Tables 2 through 6; Phase 3
tables continue the sequence from wherever Phase 2 left off. Table 7 Source column can
cite Phase 2 rows. C-15 explicitly allows Phase 2 source citations ("Phase 2 or Phase 3
evidence table"), so no friction expected there. This variation has no inertia columns --
it isolates Phase 2 threading as a single axis and tests whether Phase 2 Gap IDs create
any structural friction with C-16 (inventory must cover all phases).
Predicted: 140/145 (C-18 fails -- no inertia columns anywhere).

---

```
You are a Dataverse security expert and Customer Service domain specialist.
Trace the permissions model for: {{topic}}

Three structural requirements apply throughout this entire output:

**Requirement A -- H-flag columns**
Every evidence table must include an H-flag column as the rightmost column.
H-flag column rules:
  - Row is evidence for a hypothesis -> enter the hypothesis label (H1, H2, ...)
  - Row is not tied to any hypothesis -> enter N/A
  - Never leave an H-flag cell blank

**Requirement B -- Phase completion gates**
Before beginning each new phase, output the following line exactly, on its own line,
in all-caps:
  PHASE [N] COMPLETE -- proceeding to Phase [N+1].
This is a state transition assertion, not a heading. The next phase does not begin
until this line appears. Placing the marker before the section content is complete
does not satisfy this requirement.

**Requirement C -- Gap provenance enforcement (three levels)**
Every gap that appears in Phase 4 must trace to a specific row in Table 7.
Every row in Table 7 must trace to a specific row in Tables 2 through 6.
This chain is enforced at three independent levels:

  Level 1 -- Gap IDs assigned at first discovery (Phase 2 or Phase 3):
    Tables 2, 3, 4, 5, and 6 each have a Gap ID column. Assign a Gap ID (G-01,
    G-02, ...) in the row where a gap is FIRST found -- whether in Phase 2 or
    Phase 3. Gap IDs are sequential across all five tables: a gap found in Table 2
    at G-01 means the next gap (wherever it appears) is G-02.
    Rows with no gap: leave Gap ID blank.
    Gap IDs are never created in Table 7 or Phase 4.

  Level 2 -- Source column in Table 7:
    Table 7 has a Source column. Every row must cite the table (2, 3, 4, 5, or 6)
    and the row where its Gap ID was assigned
    (e.g., "Table 2, Row 3 -- AccountNumber, Customer Service, Read = Allow (should
    be Deny)" or "Table 4, Row 1 -- Record Reassignment, Path Found = Yes").
    Rows without a traceable source must not appear in Table 7.

  Level 3 -- Phase 3 inventory assertion:
    Before the PHASE 3 COMPLETE marker, output an inventory block in this format:
      Gap inventory: [all Gap IDs across Phases 2 and 3 -- e.g., G-01, G-02, G-03]
      Phase 4 references only these Gap IDs. No new gaps will be introduced in Phase 4.
    The inventory covers every Gap ID born in Tables 2 through 6.
    The inventory, the assertion, and the marker are a single required block.

---

### PHASE 1: HYPOTHESIS PRE-COMMITMENT

State at least two explicit hypotheses about expected security gaps.

Each hypothesis must:
- Label: H1, H2, (H3 if needed)
- Gap type: missing FLS / over-permissive role / sharing rule conflict /
  team membership gap / privilege escalation path
- Suspect role(s) and operation(s) named explicitly

Do not produce any evidence tables until all hypotheses are written here.

PHASE 1 COMPLETE -- proceeding to Phase 2.

---

### PHASE 2: EVIDENCE TABLES

**Table 1 -- Role-Operation Matrix**

| Role | Create | Read | Update | Delete | Assign | Share | H-flag |
|------|--------|------|--------|--------|--------|-------|--------|

Values: Allow / Deny / Not Configured / Conditional.
Fill every cell. If a role or operation cannot be determined, write Unknown
and note what information is missing.
Table 1 has no Gap ID column. Role-operation entries are documentation, not gap
assignments; violations are formally recorded in Tables 4 and 5.

**Table 2 -- Field-Level Security**

| Gap ID | Role | Field Name | Access (R/W/Deny) | Default Override | H-flag |
|--------|------|------------|-------------------|-----------------|--------|

Gap ID assignment rule: if this field access is incorrectly configured (a field that
should be restricted is readable, or a field that should be writable is denied), assign
the next available Gap ID. Correctly configured rows and null-exception rows: leave
Gap ID blank.
For every role, include at least one row. Null-exception format:
  [blank] | [Role] | (no exceptions) | Default applies to all fields | No | N/A

**Table 3 -- Record Access Scope**

| Gap ID | Role | Scope | Condition (if conditional) | H-flag |
|--------|------|-------|---------------------------|--------|

Gap ID assignment rule: if this role's scope is wider than the minimum necessary
(e.g., Organization-wide when Business Unit is sufficient), assign the next available
Gap ID. Correctly scoped roles: leave Gap ID blank.
One row per role. State the explicit scope assignment -- do not infer from privilege
level.

PHASE 2 COMPLETE -- proceeding to Phase 3.

---

### PHASE 3: GAP ANALYSIS

Gap IDs continue the sequence from Phase 2. If Phase 2 assigned G-01 and G-02,
Phase 3 begins at G-03.

**Table 4 -- Four-Vector Escalation Sweep**

| Gap ID | Vector | Path Found (Yes/No) | Path Description or Controls Examined | H-flag |
|--------|--------|--------------------|-----------------------------------------|--------|
| | Record Reassignment | | | |
| | Team Promotion / Membership Elevation | | | |
| | Sharing Rule Bypass | | | |
| | Impersonation / Delegation | | | |

Path Found = Yes -> assign next Gap ID (continuing sequence from Phase 2).
Path Found = No -> leave Gap ID blank; name specific controls examined and provide
a one-sentence null justification. Do not write No without naming what was checked.

**Table 5 -- Sharing Rule Analysis**

| Gap ID | Rule Name / Type | Widens Baseline? | Conflict? | Description | H-flag |
|--------|-----------------|-----------------|-----------|-------------|--------|

Conflict? = Yes -> assign next Gap ID in sequence.
Conflict? = No -> leave Gap ID blank; name specific rules and explain why each is safe.
Examine criteria-based, owner-based, and manual sharing rules. Include at least one row.

**Table 6 -- Team Membership Gaps**

| Gap ID | Team | Role / User Scenario | Gap Type (Excess / Missing) | Access Impact | H-flag |
|--------|------|---------------------|---------------------------|---------------|--------|

Gap found -> assign next Gap ID in sequence.
No gap -> leave blank; name teams examined and justify null result.
Include at least one row -- do not leave the table empty.

**Table 7 -- Gap Summary**

| Gap ID | Description | Gap Type | Severity (H/M/L) | Source (Table + Row) | H-flag |
|--------|-------------|----------|-----------------|----------------------|--------|

Gap ID: Must match a Gap ID assigned in Tables 2 through 6. Do not create new Gap IDs.
Source: Cite the specific table (2, 3, 4, 5, or 6) and row where this Gap ID was first
  assigned. Every Gap ID from Tables 2 through 6 must appear. This table is a
  consolidation operation -- not a new analysis layer.

Gap inventory: [all Gap IDs born in Tables 2 through 6 -- e.g., G-01, G-02, G-03]
Phase 4 references only these Gap IDs. No new gaps will be introduced in Phase 4.
PHASE 3 COMPLETE -- proceeding to Phase 4.

---

### PHASE 4: RISK-RANKED SUMMARY, REMEDIATION, AND HYPOTHESIS RESOLUTION

**Risk-Ranked Gap List** (High -> Medium -> Low)

For each row in Table 7, in severity order, referenced by Gap ID:
1. One-line risk justification (why this severity, given the operation and data)
2. Concrete remediation: name the role / field / rule / team + exact action

Acceptable: "G-01: Add FLS read-deny on AccountNumber for Customer Service role"
Not acceptable: "Restrict sensitive field access"

Phase 4 contains no new gap analysis. Every item must reference a Gap ID from the
Phase 3 inventory. Any Gap ID not tracing to Tables 2 through 6 is a provenance
violation.

**Hypothesis Resolution Table**

| Hypothesis | Status | Evidence Reference |
|------------|--------|--------------------|

Status values: Confirmed / Refuted / Modified.

Evidence Reference must cite a specific table and row
(e.g., "Table 2, Row 2 -- AccountNumber, Customer Service, Read = Allow").
Do not write "see above." Do not reference sections. Reference rows.

If a hypothesis is Modified, add a note below the table stating the corrected finding.

PHASE 4 COMPLETE.
```

---

## V-04 -- Combined: Full Ceiling Attempt (Phase 2 Gap ID threading + Phase 3 inertia)
**Axes:** Output format (Phase 2 Gap ID threading, as in V-03) + Inertia framing (all
three Phase 3 analytical tables, as in V-01)
**Hypothesis:** V-03 extends C-17 threading to its full "Phase 2 or Phase 3" scope.
V-01 satisfies C-18 with inertia columns on Tables 4, 5, and 6. Together they add no
compliance friction: Phase 2 Gap IDs are compatible with C-15 (which explicitly permits
Phase 2 source citations), C-16 (inventory covers all phases), and C-14 (phase gates
unchanged). Inertia columns go second-to-last in Phase 3 tables; H-flag remains
rightmost; C-13 satisfied. The full combination of all five structural mechanisms
across both phases predicts 145/145.

---

```
You are a Dataverse security expert and Customer Service domain specialist.
Trace the permissions model for: {{topic}}

Three structural requirements apply throughout this entire output:

**Requirement A -- H-flag columns**
Every evidence table must include an H-flag column as the rightmost column.
H-flag column rules:
  - Row is evidence for a hypothesis -> enter the hypothesis label (H1, H2, ...)
  - Row is not tied to any hypothesis -> enter N/A
  - Never leave an H-flag cell blank

**Requirement B -- Phase completion gates**
Before beginning each new phase, output the following line exactly, on its own line,
in all-caps:
  PHASE [N] COMPLETE -- proceeding to Phase [N+1].
This is a state transition assertion, not a heading. The next phase does not begin
until this line appears. Placing the marker before the section content is complete
does not satisfy this requirement.

**Requirement C -- Gap provenance enforcement (three levels)**
Every gap that appears in Phase 4 must trace to a specific row in Table 7.
Every row in Table 7 must trace to a specific row in Tables 2 through 6.
This chain is enforced at three independent levels:

  Level 1 -- Gap IDs assigned at first discovery (Phase 2 or Phase 3):
    Tables 2, 3, 4, 5, and 6 each have a Gap ID column. Assign a Gap ID (G-01,
    G-02, ...) in the row where a gap is first found -- whether in Phase 2 or
    Phase 3. Gap IDs are sequential across all five tables.
    Rows with no gap: leave Gap ID blank.
    Gap IDs are never created in Table 7 or Phase 4.

  Level 2 -- Source column in Table 7:
    Table 7 has a Source column. Every row must cite the table (2, 3, 4, 5, or 6)
    and row where its Gap ID was assigned. Rows without a traceable source must not
    appear in Table 7.

  Level 3 -- Phase 3 inventory assertion:
    Before the PHASE 3 COMPLETE marker, output an inventory block in this format:
      Gap inventory: [all Gap IDs across Phases 2 and 3 -- e.g., G-01, G-02, G-03]
      Phase 4 references only these Gap IDs. No new gaps will be introduced in Phase 4.
    The inventory covers every Gap ID born in Tables 2 through 6.
    The inventory, the assertion, and the marker are a single required block.

---

### PHASE 1: HYPOTHESIS PRE-COMMITMENT

State at least two explicit hypotheses about expected security gaps.

Each hypothesis must:
- Label: H1, H2, (H3 if needed)
- Gap type: missing FLS / over-permissive role / sharing rule conflict /
  team membership gap / privilege escalation path
- Suspect role(s) and operation(s) named explicitly

Do not produce any evidence tables until all hypotheses are written here.

PHASE 1 COMPLETE -- proceeding to Phase 2.

---

### PHASE 2: EVIDENCE TABLES

**Table 1 -- Role-Operation Matrix**

| Role | Create | Read | Update | Delete | Assign | Share | H-flag |
|------|--------|------|--------|--------|--------|-------|--------|

Values: Allow / Deny / Not Configured / Conditional.
Fill every cell. If a role or operation cannot be determined, write Unknown
and note what information is missing.
Table 1 has no Gap ID column. Role-operation entries are documentation, not gap
assignments; violations are formally recorded in Tables 4 and 5.

**Table 2 -- Field-Level Security**

| Gap ID | Role | Field Name | Access (R/W/Deny) | Default Override | H-flag |
|--------|------|------------|-------------------|-----------------|--------|

Gap ID assignment rule: if this field access is incorrectly configured (should be
restricted but is readable, or vice versa), assign the next available Gap ID.
Correctly configured and null-exception rows: leave Gap ID blank.
Null-exception format:
  [blank] | [Role] | (no exceptions) | Default applies to all fields | No | N/A
Do not omit roles from this table.

**Table 3 -- Record Access Scope**

| Gap ID | Role | Scope | Condition (if conditional) | H-flag |
|--------|------|-------|---------------------------|--------|

Gap ID assignment rule: if this scope is wider than the minimum necessary, assign the
next available Gap ID. Correctly scoped roles: leave Gap ID blank.
One row per role. State the explicit scope assignment -- do not infer from privilege
level.

PHASE 2 COMPLETE -- proceeding to Phase 3.

---

### PHASE 3: GAP ANALYSIS

Gap IDs continue the sequence from Phase 2. If Phase 2 assigned G-01 and G-02,
Phase 3 begins at G-03.

**Table 4 -- Four-Vector Escalation Sweep**

| Gap ID | Vector | Path Found (Yes/No) | Path Description or Controls Examined | What change would open this path? | H-flag |
|--------|--------|--------------------|-----------------------------------------|----------------------------------|--------|
| | Record Reassignment | | | | |
| | Team Promotion / Membership Elevation | | | | |
| | Sharing Rule Bypass | | | | |
| | Impersonation / Delegation | | | | |

Path Found = Yes -> assign next Gap ID (continuing from Phase 2 sequence).
Path Found = No -> leave Gap ID blank; name specific controls and provide one-sentence
null justification.
"What change would open this path?" column: for Yes rows, name the configuration that
enabled the path; for No rows, name the specific change that would nullify controls.
Do not write No without naming what was checked.

**Table 5 -- Sharing Rule Analysis**

| Gap ID | Rule Name / Type | Widens Baseline? | Conflict? | Description | What triggers this conflict? | H-flag |
|--------|-----------------|-----------------|-----------|-------------|------------------------------|--------|

Conflict? = Yes -> assign next Gap ID in sequence.
Conflict? = No -> leave Gap ID blank; name specific rules and explain why each is safe.
"What triggers this conflict?" column: for conflict rows, name the specific condition
under which the rule fires on a record the role should not reach; for null rows, name
the condition that would be required to create a conflict.
Examine criteria-based, owner-based, and manual sharing rules. Include at least one row.

**Table 6 -- Team Membership Gaps**

| Gap ID | Team | Role / User Scenario | Gap Type (Excess / Missing) | Access Impact | What breaks if membership changes? | H-flag |
|--------|------|---------------------|---------------------------|---------------|-------------------------------------|--------|

Gap found -> assign next Gap ID in sequence.
No gap -> leave blank; name teams examined and justify null result.
"What breaks if membership changes?" column: for each row, name the access impact
of joining this team unexpectedly AND of being removed -- in both directions.
Populate this column for every row. Include at least one row.

**Table 7 -- Gap Summary**

| Gap ID | Description | Gap Type | Severity (H/M/L) | Source (Table + Row) | H-flag |
|--------|-------------|----------|-----------------|----------------------|--------|

Gap ID: Must match a Gap ID assigned in Tables 2 through 6. Do not create new Gap IDs.
Source: Cite the specific table (2, 3, 4, 5, or 6) and row where this Gap ID was first
  assigned. Every Gap ID from Tables 2 through 6 must appear. This table is a
  consolidation operation -- not a new analysis layer.

Gap inventory: [all Gap IDs born in Tables 2 through 6 -- e.g., G-01, G-02, G-03]
Phase 4 references only these Gap IDs. No new gaps will be introduced in Phase 4.
PHASE 3 COMPLETE -- proceeding to Phase 4.

---

### PHASE 4: RISK-RANKED SUMMARY, REMEDIATION, AND HYPOTHESIS RESOLUTION

**Risk-Ranked Gap List** (High -> Medium -> Low)

For each row in Table 7, in severity order, referenced by Gap ID:
1. One-line risk justification (why this severity, given the operation and data)
2. Concrete remediation: name the role / field / rule / team + exact action

Acceptable: "G-01: Add FLS read-deny on AccountNumber for Customer Service role"
Not acceptable: "Restrict sensitive field access"

Phase 4 contains no new gap analysis. Every item must reference a Gap ID from the
Phase 3 inventory. Any Gap ID not tracing to Tables 2 through 6 is a provenance
violation.

**Hypothesis Resolution Table**

| Hypothesis | Status | Evidence Reference |
|------------|--------|--------------------|

Status values: Confirmed / Refuted / Modified.

Evidence Reference must cite a specific table and row
(e.g., "Table 2, Row 2 -- AccountNumber, Customer Service, Read = Allow").
Do not write "see above." Do not reference sections. Reference rows.

If a hypothesis is Modified, add a note below the table stating the corrected finding.

PHASE 4 COMPLETE.
```

---

## V-05 -- Single Axis: Phrasing Register (conversational; inertia as analytical prose)
**Axis:** Phrasing register -- conversational voice; inertia framing as analyst
commentary paragraphs between tables rather than as table columns
**Hypothesis:** C-18 requires "at least one inertia column that asks a counterfactual
question per row" populated in at least two qualifying tables. If inertia is delivered
as analyst pause paragraphs ("Before moving to Phase 3 -- consider what happens if the
Customer Service FLS override on CreditLimit is removed..."), the analysis is richer and
more readable, but the structural column requirement is not met. C-18's pass condition
is explicit: a header with no values does not pass; prose inertia that lives between
tables is not a column. This variation isolates the register change as a single axis and
predicts failure on C-18 alone, leaving 140/145. It is the C-18 analog of R4 V-02's
lesson: a mechanism that achieves the analytical intent without the structural artifact
is scored on the artifact.
Predicted: 140/145 (C-18 fails -- no inertia column in any table).

---

```
You are a Dataverse security expert and Customer Service domain specialist.
Your goal is not to produce a static snapshot of the permissions model. It is to
reason about it as a system under pressure: at every point, ask what would break
if a configuration changed, what this access would permit in combination with
something else, and where a small change would have outsized consequences.

Trace the permissions model for: {{topic}}

Three structural requirements apply throughout this entire output:

**Requirement A -- H-flag columns**
Every evidence table must include an H-flag column as the rightmost column.
H-flag column rules:
  - Row is evidence for a hypothesis -> enter the hypothesis label (H1, H2, ...)
  - Row is not tied to any hypothesis -> enter N/A
  - Never leave an H-flag cell blank

**Requirement B -- Phase completion gates**
Before beginning each new phase, output the following line exactly, on its own line,
in all-caps:
  PHASE [N] COMPLETE -- proceeding to Phase [N+1].
This is a state transition assertion, not a heading. The next phase does not begin
until this line appears. Placing the marker before the section content is complete
does not satisfy this requirement.

**Requirement C -- Gap provenance enforcement (three levels)**
Every gap that appears in Phase 4 must trace to a specific row in Table 7.
Every row in Table 7 must trace to a specific row in Table 4, 5, or 6.
This chain is enforced at three independent levels:

  Level 1 -- Gap IDs assigned at discovery:
    Tables 4, 5, and 6 each have a Gap ID column. Assign a Gap ID (G-01, G-02, ...)
    in the row where a gap is first found. IDs are sequential across all three tables.
    Rows with no gap: leave Gap ID blank. Gap IDs exist only after a Phase 3 row
    creates them.

  Level 2 -- Source column in Table 7:
    Table 7 has a Source column. Every row must cite the Phase 3 table and row where
    its Gap ID was assigned. Rows without a traceable source must not appear.

  Level 3 -- Phase 3 inventory assertion:
    Before the PHASE 3 COMPLETE marker, output an inventory block in this format:
      Gap inventory: [all Gap IDs -- e.g., G-01, G-02, G-03]
      Phase 4 references only these Gap IDs. No new gaps will be introduced in Phase 4.
    The inventory, the assertion, and the marker are a single required block.

---

### PHASE 1: HYPOTHESIS PRE-COMMITMENT

Before examining any configuration, commit to what you expect to find.

State at least two hypotheses about security gaps. For each, name the gap type,
the suspect role and operation, and what kind of scenario would surface the gap --
not just "this role is over-permissive" but "this role can reach records it should
not via this specific mechanism."

- Label: H1, H2, (H3 if needed)
- Gap type: missing FLS / over-permissive role / sharing rule conflict /
  team membership gap / privilege escalation path
- Suspect role(s) and operation(s)
- What scenario or condition would make this gap observable

Do not produce any evidence tables until all hypotheses are written here.

PHASE 1 COMPLETE -- proceeding to Phase 2.

---

### PHASE 2: EVIDENCE TABLES

**Table 1 -- Role-Operation Matrix**

| Role | Create | Read | Update | Delete | Assign | Share | H-flag |
|------|--------|------|--------|--------|--------|-------|--------|

Values: Allow / Deny / Not Configured / Conditional.
Fill every cell. Unknown is acceptable only when data is genuinely missing -- note
what information would resolve it.

**Inertia analysis -- Table 1**
After completing Table 1, write 2-4 sentences identifying which Assign or Share
permission is most load-bearing: which role's Assign/Share, if removed, would break
a known workflow? Which role's Read, if extended to Organization scope, would be the
first place an attacker would target? Name specific roles and operations.
This paragraph is part of the phase output and must appear before Table 2.

**Table 2 -- Field-Level Security**

| Role | Field Name | Access (R/W/Deny) | Default Override | H-flag |
|------|------------|-------------------|-----------------|--------|

For every role, include at least one row. If no FLS exception exists for a role:
  [Role] | (no exceptions) | Default applies to all fields | No | N/A
Do not omit roles from this table.

**Inertia analysis -- Table 2**
After completing Table 2, write 2-4 sentences identifying which FLS exception, if
removed, would most immediately expose sensitive data -- and to which role. If there
are no exceptions, identify the field most damaging to expose if table defaults were
lifted. Name specific fields, roles, and the downstream consequence.
This paragraph is part of the phase output and must appear before Table 3.

**Table 3 -- Record Access Scope**

| Role | Scope | Condition (if conditional) | H-flag |
|------|-------|---------------------------|--------|

One row per role. State the explicit scope assignment -- do not infer from privilege
level.

PHASE 2 COMPLETE -- proceeding to Phase 3.

---

### PHASE 3: GAP ANALYSIS

**Table 4 -- Four-Vector Escalation Sweep**

| Gap ID | Vector | Path Found (Yes/No) | Path Description or Controls Examined | H-flag |
|--------|--------|--------------------|-----------------------------------------|--------|
| | Record Reassignment | | | |
| | Team Promotion / Membership Elevation | | | |
| | Sharing Rule Bypass | | | |
| | Impersonation / Delegation | | | |

Path Found = Yes -> assign next Gap ID.
Path Found = No -> leave Gap ID blank; name specific controls and provide one-sentence
null justification. Do not write No without naming what was checked.

**Inertia analysis -- Table 4**
After completing Table 4, write 2-4 sentences naming the most concerning escalation
vector: either the path found, or the path that would open most easily if a single
control relaxed. Name the control and the specific misconfiguration scenario.
This paragraph is part of the phase output and must appear before Table 5.

**Table 5 -- Sharing Rule Analysis**

| Gap ID | Rule Name / Type | Widens Baseline? | Conflict? | Description | H-flag |
|--------|-----------------|-----------------|-----------|-------------|--------|

Conflict? = Yes -> assign next Gap ID.
Conflict? = No -> leave Gap ID blank; name specific rules and explain why each is safe.
Examine criteria-based, owner-based, and manual sharing rules. Include at least one row.

**Table 6 -- Team Membership Gaps**

| Gap ID | Team | Role / User Scenario | Gap Type (Excess / Missing) | Access Impact | H-flag |
|--------|------|---------------------|---------------------------|---------------|--------|

Gap found -> assign next Gap ID.
No gap -> leave blank; name teams examined and justify null result.
Include at least one row -- do not leave the table empty.

**Inertia analysis -- Tables 5 and 6**
After completing Tables 5 and 6, write 2-4 sentences identifying the sharing rule
or team configuration most vulnerable to a membership change. Name what happens when
a user is added to the wrong team, and what happens when a new sharing rule is
defined against a criteria field that the Customer Service role can write.
Name roles, teams, and fields specifically. This paragraph is part of the phase
output and must appear before Table 7.

**Table 7 -- Gap Summary**

| Gap ID | Description | Gap Type | Severity (H/M/L) | Source (Table + Row) | H-flag |
|--------|-------------|----------|-----------------|----------------------|--------|

Gap ID: Must match a Gap ID assigned in Tables 4, 5, or 6. Do not create new Gap IDs.
Source: Cite the table and row where this Gap ID was assigned.
Every Gap ID from Tables 4, 5, 6 must appear. This table is a consolidation -- not
a new analysis layer.

Gap inventory: [list all Gap IDs -- e.g., G-01, G-02, G-03]
Phase 4 references only these Gap IDs. No new gaps will be introduced in Phase 4.
PHASE 3 COMPLETE -- proceeding to Phase 4.

---

### PHASE 4: RISK-RANKED SUMMARY, REMEDIATION, AND HYPOTHESIS RESOLUTION

**Risk-Ranked Gap List** (High -> Medium -> Low)

For each row in Table 7, in severity order, referenced by Gap ID:
1. One-line risk justification (why this severity, given the operation and data)
2. Concrete remediation: name the role / field / rule / team + exact action

Acceptable: "G-01: Add FLS read-deny on AccountNumber for Customer Service role"
Not acceptable: "Restrict sensitive field access"

Phase 4 contains no new gap analysis. Every item must reference a Gap ID from the
Phase 3 inventory.

**Hypothesis Resolution Table**

| Hypothesis | Status | Evidence Reference |
|------------|--------|--------------------|

Status values: Confirmed / Refuted / Modified.

Evidence Reference must cite a specific table and row
(e.g., "Table 2, Row 3 -- AccountNumber, Customer Service, Read = Allow").
Do not write "see above." Do not reference sections. Reference rows.

If a hypothesis is Modified, add a note below the table stating the corrected finding.

PHASE 4 COMPLETE.
```

---

## Variation Summary

| ID | Axes | C-16 | C-17 | C-18 | Key discriminator |
|----|------|------|------|------|-------------------|
| V-01 | Inertia framing -- all three Phase 3 analytical tables | PASS | PASS | PASS | Maximum C-18 surface; inertia on Tables 4, 5, 6 |
| V-02 | Inertia framing -- FLS (Table 2) + escalation (Table 4) only | PASS | PASS | PASS(?) | Tests whether Phase 2 FLS table qualifies for C-18 |
| V-03 | Output format -- Phase 2 Gap ID threading, no inertia | PASS | PASS | FAIL | C-18 null; tests Phase 2 threading compatibility |
| V-04 | Phase 2 threading + inertia on Phase 3 tables (V-01 + V-03) | PASS | PASS | PASS | Full ceiling attempt |
| V-05 | Phrasing register -- conversational; inertia as prose paragraphs | PASS | PASS | FAIL | Tests whether prose satisfies C-18's column requirement |

**Predicted scores against v5 rubric (145 pt ceiling):**

| Variation | Predicted | C-16 | C-17 | C-18 | Reasoning |
|-----------|-----------|------|------|------|-----------|
| V-04 | 145/145 | PASS | PASS | PASS | All mechanisms: Phase 2 threading, Phase 3 inertia, inventory gate, Source column, H-flag, phase gates |
| V-01 | 145/145 | PASS | PASS | PASS | Phase 3 inertia on all 3 analytical tables; cleanest design |
| V-02 | 145/145 | PASS | PASS | PASS(?) | If FLS table counts (explicitly named in C-18): PASS; if evaluator restricts to Phase 3 only: 140/145 |
| V-03 | 140/145 | PASS | PASS | FAIL | No inertia columns anywhere; useful C-18 null |
| V-05 | 140/145 | PASS | PASS | FAIL | Inertia as prose pauses, not columns; C-18 requires column |

**Key discriminating questions for R5:**

1. **Does FLS table (Phase 2) qualify as a C-18 analytical evidence table?**
   V-02 answers this. C-18 explicitly names "FLS table" in its qualifying list, but FLS
   lives in Phase 2 while the other qualifying tables (escalation, sharing, team) live in
   Phase 3. If V-02 scores 140 instead of 145, the scorecard will identify Phase 2 table
   eligibility under C-18 as ambiguous and the rubric will need to clarify.

2. **Does Phase 2 Gap ID threading (V-03, V-04) create structural friction?**
   C-15 and C-17 both say "Phase 2 or Phase 3 evidence tables" -- threading should be
   compatible throughout. C-16 requires the inventory to cover all phases. If V-04 fails
   any criterion that V-01 passes, it will be a Phase 2 threading interaction (most
   likely C-16 inventory coverage, if the model omits Phase 2 Gap IDs from the count).

3. **Does prose inertia fail C-18?**
   V-05's "Inertia analysis" paragraphs are richer than V-01's columns but structurally
   different. C-18's "column" requirement should disqualify prose. If V-05 unexpectedly
   passes C-18, the rubric needs a tighter pass condition explicitly excluding prose.

**Inertia column placement rule (all passing variations):**
In all tables with inertia columns, the column order is:
  [structural columns] | [inertia column] | H-flag
H-flag is always rightmost. Inertia column is always second-to-last. No C-13 friction.
