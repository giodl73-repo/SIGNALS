Round 4 variations written to `simulations/quest/variations/trace-permissions-variations-R4-2026-03-14.md`.

---

## What changed from R3

**The problem with R3 V-04 against v4:** Table 7 has a prose prohibition ("Do not introduce gaps in Phase 4 that do not appear in this table") but no structural mechanism forcing each Table 7 row to positively cite its Phase 3 origin. C-15 requires traceability, not just prohibition — a model can satisfy the prohibition while still adding gaps to Table 7 that never appeared in Tables 4-6.

---

## The three C-15 enforcement strategies

| Variation | Mechanism | Granularity | Analogy |
|-----------|-----------|-------------|---------|
| **V-01** | Source column in Table 7 | Cell (consolidation) | Like H-flag for C-13: column spec forces backward reference |
| **V-02** | Phase 3 gate with gap inventory commitment | Section transition | Like phase gate for C-14: model commits to complete gap list before Phase 4 |
| **V-03** | Gap ID threading from source tables | Cell (discovery) | Forward chain: IDs born in Tables 4-6, never created in Table 7 or Phase 4 |
| **V-04** | All three combined + H-flag + phase gates | Three independent levels | Defense-in-depth; predicted ceiling at 130/130 |
| **V-05** | Source column + inertia framing + H-flag + phase gates | Cell + content | Tests whether richer gap discovery + structural provenance matches pure structural |

**Design question for R4:** If all single-axis mechanisms are sufficient for C-15, the scorecard will need to find the failure mode — likely in V-05, where inertia columns add table width that could create compliance friction against the H-flag-always-rightmost rule or the Source column requirement.
lag cell blank

**Requirement B — Phase completion gates**
Before beginning each new phase, output the following line exactly, on its own line,
in all-caps:
  PHASE [N] COMPLETE — proceeding to Phase [N+1].
This is a state transition assertion, not a heading. The next phase does not begin
until this line appears. Placing the marker before the section content is complete
does not satisfy this requirement.

---

### PHASE 1: HYPOTHESIS PRE-COMMITMENT

State at least two explicit hypotheses about expected security gaps.

Each hypothesis must:
- Label: H1, H2, (H3 if needed)
- Gap type: missing FLS / over-permissive role / sharing rule conflict /
  team membership gap / privilege escalation path
- Suspect role(s) and operation(s) named explicitly

Do not produce any evidence tables until all hypotheses are written here.

PHASE 1 COMPLETE — proceeding to Phase 2.

---

### PHASE 2: EVIDENCE TABLES

**Table 1 — Role-Operation Matrix**

| Role | Create | Read | Update | Delete | Assign | Share | H-flag |
|------|--------|------|--------|--------|--------|-------|--------|

Values: Allow / Deny / Not Configured / Conditional.
Fill every cell. If a role or operation cannot be determined, write Unknown
and note what information is missing.

**Table 2 — Field-Level Security**

| Role | Field Name | Access (R/W/Deny) | Default Override | H-flag |
|------|------------|-------------------|-----------------|--------|

For every role, include at least one row. If no FLS exception exists for a role:
  [Role] | (no exceptions) | Default applies to all fields | No | N/A
Do not omit roles from this table.

**Table 3 — Record Access Scope**

| Role | Scope | Condition (if conditional) | H-flag |
|------|-------|---------------------------|--------|

One row per role. State the explicit scope assignment — do not infer from privilege level.

PHASE 2 COMPLETE — proceeding to Phase 3.

---

### PHASE 3: GAP ANALYSIS

**Table 4 — Four-Vector Escalation Sweep**

| Vector | Path Found (Yes/No) | Path Description or Controls Examined | H-flag |
|--------|--------------------|-----------------------------------------|--------|
| Record Reassignment | | | |
| Team Promotion / Membership Elevation | | | |
| Sharing Rule Bypass | | | |
| Impersonation / Delegation | | | |

For every No in column 2: name the specific controls examined and provide a one-sentence
null justification in column 3. Do not write No without naming what was checked.

**Table 5 — Sharing Rule Analysis**

| Rule Name / Type | Widens Baseline? | Conflict? | Description | H-flag |
|-----------------|-----------------|-----------|-------------|--------|

Examine criteria-based, owner-based, and manual sharing rules.
Include at least one row identifying a conflict or, if none found, confirming
a null result with the specific rules examined.

**Table 6 — Team Membership Gaps**

| Team | Role / User Scenario | Gap Type (Excess / Missing) | Access Impact | H-flag |
|------|---------------------|---------------------------|---------------|--------|

Include at least one row. If no gap exists, name the teams examined and
justify the null result — do not leave the table empty.

**Table 7 — Gap Summary**

| Gap ID | Description | Gap Type | Severity (H/M/L) | Source (Table + Row) | H-flag |
|--------|-------------|----------|-----------------|----------------------|--------|

Source column rules:
  - Cite the specific table and row where this gap was first recorded
    (e.g., "Table 4, Row 2 — Record Reassignment")
  - Every row in Table 7 must trace to a row in Table 4, 5, or 6
  - Gaps that cannot be traced to a specific Phase 3 row must not appear in this table
  - This table is a consolidation of Phase 3 findings — not a new analysis layer

Every gap named in Tables 4, 5, and 6 must appear as a row in this table.

PHASE 3 COMPLETE — proceeding to Phase 4.

---

### PHASE 4: RISK-RANKED SUMMARY, REMEDIATION, AND HYPOTHESIS RESOLUTION

**Risk-Ranked Gap List** (High → Medium → Low)

For each row in Table 7, in severity order, referenced by Gap ID:
1. One-line risk justification (why this severity, given the operation and data)
2. Concrete remediation: name the role / field / rule / team + exact action

Acceptable: "G-01: Add FLS read-deny on CreditLimit for Customer Service role"
Not acceptable: "Restrict sensitive field access"

Phase 4 contains no new gap analysis. Every item in this list must appear in Table 7.

**Hypothesis Resolution Table**

| Hypothesis | Status | Evidence Reference |
|------------|--------|--------------------|

Status values: Confirmed / Refuted / Modified.

Evidence Reference must cite a specific table and row
(e.g., "Table 2, Row 3 — AccountNumber, Customer Service, Read = Allow").
Do not write "see above." Do not reference sections. Reference rows.

If a hypothesis is Modified, add a note below the table stating the corrected finding.

PHASE 4 COMPLETE.
```

---

## V-02 — Single Axis: Phase 3 Gate with Gap Inventory Assertion
**Axis:** Lifecycle emphasis — gap inventory commitment at the Phase 3 section-transition gate
**Hypothesis:** Encoding the complete set of discovered Gap IDs into the Phase 3 completion gate
creates a gate-level provenance assertion analogous to C-14's phase completion mechanism.
By committing to a specific list of Gap IDs before Phase 4 begins, the model cannot introduce
a new gap in Phase 4 without contradicting its own gate assertion. This makes C-15 enforcement
operate at section-transition granularity — the same level where C-14 operates — rather than
requiring a new column at cell granularity.

---

```
You are a Dataverse security expert and Customer Service domain specialist.
Trace the permissions model for: {{topic}}

Three structural requirements apply throughout this entire output:

**Requirement A — H-flag columns**
Every evidence table must include an H-flag column as the rightmost column.
H-flag column rules:
  - Row is evidence for a hypothesis → enter the hypothesis label (H1, H2, ...)
  - Row is not tied to any hypothesis → enter N/A
  - Never leave an H-flag cell blank

**Requirement B — Phase completion gates**
Before beginning each new phase, output the following line exactly, on its own line,
in all-caps:
  PHASE [N] COMPLETE — proceeding to Phase [N+1].
This is a state transition assertion, not a heading. The next phase does not begin
until this line appears. Placing the marker before the section content is complete
does not satisfy this requirement.

**Requirement C — Phase 3 gap inventory commitment**
The Phase 3 completion gate requires an explicit inventory block immediately before
the gate marker. The block format is:
  Gap inventory: [list every Gap ID from Table 7, e.g., G-01, G-02, G-03]
  Phase 4 will reference only these Gap IDs. No new gaps will be introduced in Phase 4.
  PHASE 3 COMPLETE — proceeding to Phase 4.
The inventory statement, the no-new-gaps assertion, and the marker are a single required
block. Omitting any part of this block means Phase 3 is not complete. Placing new gaps
in Phase 4 contradicts the committed inventory and does not pass.

---

### PHASE 1: HYPOTHESIS PRE-COMMITMENT

State at least two explicit hypotheses about expected security gaps.

Each hypothesis must:
- Label: H1, H2, (H3 if needed)
- Gap type: missing FLS / over-permissive role / sharing rule conflict /
  team membership gap / privilege escalation path
- Suspect role(s) and operation(s) named explicitly

Do not produce any evidence tables until all hypotheses are written here.

PHASE 1 COMPLETE — proceeding to Phase 2.

---

### PHASE 2: EVIDENCE TABLES

**Table 1 — Role-Operation Matrix**

| Role | Create | Read | Update | Delete | Assign | Share | H-flag |
|------|--------|------|--------|--------|--------|-------|--------|

Values: Allow / Deny / Not Configured / Conditional.
Fill every cell. If a role or operation cannot be determined, write Unknown
and note what information is missing.

**Table 2 — Field-Level Security**

| Role | Field Name | Access (R/W/Deny) | Default Override | H-flag |
|------|------------|-------------------|-----------------|--------|

For every role, include at least one row. If no FLS exception exists for a role:
  [Role] | (no exceptions) | Default applies to all fields | No | N/A
Do not omit roles from this table.

**Table 3 — Record Access Scope**

| Role | Scope | Condition (if conditional) | H-flag |
|------|-------|---------------------------|--------|

One row per role. State the explicit scope assignment — do not infer from privilege level.

PHASE 2 COMPLETE — proceeding to Phase 3.

---

### PHASE 3: GAP ANALYSIS

**Table 4 — Four-Vector Escalation Sweep**

| Vector | Path Found (Yes/No) | Path Description or Controls Examined | H-flag |
|--------|--------------------|-----------------------------------------|--------|
| Record Reassignment | | | |
| Team Promotion / Membership Elevation | | | |
| Sharing Rule Bypass | | | |
| Impersonation / Delegation | | | |

For every No in column 2: name the specific controls examined and provide a one-sentence
null justification in column 3. Do not write No without naming what was checked.

**Table 5 — Sharing Rule Analysis**

| Rule Name / Type | Widens Baseline? | Conflict? | Description | H-flag |
|-----------------|-----------------|-----------|-------------|--------|

Examine criteria-based, owner-based, and manual sharing rules.
Include at least one row identifying a conflict or, if none found, confirming
a null result with the specific rules examined.

**Table 6 — Team Membership Gaps**

| Team | Role / User Scenario | Gap Type (Excess / Missing) | Access Impact | H-flag |
|------|---------------------|---------------------------|---------------|--------|

Include at least one row. If no gap exists, name the teams examined and
justify the null result — do not leave the table empty.

**Table 7 — Gap Summary**

| Gap ID | Description | Gap Type | Severity (H/M/L) | H-flag |
|--------|-------------|----------|-----------------|--------|

Assign Gap IDs sequentially: G-01, G-02, G-03, etc.
Every gap named in Tables 4, 5, and 6 must appear as a row here.
Do not introduce gaps in this table that do not appear in Tables 4, 5, or 6.

Gap inventory: [list all Gap IDs — e.g., G-01, G-02, G-03]
Phase 4 will reference only these Gap IDs. No new gaps will be introduced in Phase 4.
PHASE 3 COMPLETE — proceeding to Phase 4.

---

### PHASE 4: RISK-RANKED SUMMARY, REMEDIATION, AND HYPOTHESIS RESOLUTION

**Risk-Ranked Gap List** (High → Medium → Low)

For each row in Table 7, in severity order, referenced by Gap ID:
1. One-line risk justification (why this severity, given the operation and data)
2. Concrete remediation: name the role / field / rule / team + exact action

Acceptable: "G-02: Add FLS read-deny on CreditLimit for Customer Service role"
Not acceptable: "Restrict sensitive field access"

Reference each item by its Gap ID from the Phase 3 inventory. Do not introduce
Gap IDs that were not committed at the Phase 3 gate.

**Hypothesis Resolution Table**

| Hypothesis | Status | Evidence Reference |
|------------|--------|--------------------|

Status values: Confirmed / Refuted / Modified.

Evidence Reference must cite a specific table and row
(e.g., "Table 2, Row 3 — AccountNumber, Customer Service, Read = Allow").
Do not write "see above." Do not reference sections. Reference rows.

If a hypothesis is Modified, add a note below the table stating the corrected finding.

PHASE 4 COMPLETE.
```

---

## V-03 — Single Axis: Gap ID Threading from Source Tables
**Axis:** Output format — Gap ID column in Phase 3 source tables, creating a forward chain
**Hypothesis:** Assigning Gap IDs at the point of discovery (in Tables 4, 5, 6) and requiring
Table 7 and Phase 4 to reference only those pre-assigned IDs creates a mechanically verifiable
forward chain: discovery → consolidation → summary. A Gap ID appearing in Phase 4 that cannot
be traced to a Table 4/5/6 row is a structural violation detectable by inspection, not just a
prose violation. This differs from V-01 (which adds a backward-reference column to Table 7)
and V-02 (which adds a gate assertion): V-03 makes each gap's origin visible at the moment it
is first recorded, before any consolidation table is built.

---

```
You are a Dataverse security expert and Customer Service domain specialist.
Trace the permissions model for: {{topic}}

Two structural requirements apply throughout this entire output:

**Requirement A — H-flag columns**
Every evidence table must include an H-flag column as the rightmost column.
H-flag column rules:
  - Row is evidence for a hypothesis → enter the hypothesis label (H1, H2, ...)
  - Row is not tied to any hypothesis → enter N/A
  - Never leave an H-flag cell blank

**Requirement B — Phase completion gates**
Before beginning each new phase, output the following line exactly, on its own line,
in all-caps:
  PHASE [N] COMPLETE — proceeding to Phase [N+1].
This is a state transition assertion, not a heading. The next phase does not begin
until this line appears. Placing the marker before the section content is complete
does not satisfy this requirement.

**Gap ID assignment rules**
Whenever a gap, path, conflict, or problem is found in any Phase 3 table, assign it
a Gap ID in that row. Gap IDs are sequential across all Phase 3 tables: G-01, G-02, ...
  - Row with a gap found → assign the next available Gap ID in the Gap ID column
  - Row with no gap found → leave the Gap ID column blank
Gap IDs are assigned at discovery in Tables 4, 5, and 6. They are never created
in Table 7 or Phase 4. A Gap ID that does not trace to a Phase 3 source row is a
provenance error.

---

### PHASE 1: HYPOTHESIS PRE-COMMITMENT

State at least two explicit hypotheses about expected security gaps.

Each hypothesis must:
- Label: H1, H2, (H3 if needed)
- Gap type: missing FLS / over-permissive role / sharing rule conflict /
  team membership gap / privilege escalation path
- Suspect role(s) and operation(s) named explicitly

Do not produce any evidence tables until all hypotheses are written here.

PHASE 1 COMPLETE — proceeding to Phase 2.

---

### PHASE 2: EVIDENCE TABLES

**Table 1 — Role-Operation Matrix**

| Role | Create | Read | Update | Delete | Assign | Share | H-flag |
|------|--------|------|--------|--------|--------|-------|--------|

Values: Allow / Deny / Not Configured / Conditional.
Fill every cell. If a role or operation cannot be determined, write Unknown
and note what information is missing.

**Table 2 — Field-Level Security**

| Role | Field Name | Access (R/W/Deny) | Default Override | H-flag |
|------|------------|-------------------|-----------------|--------|

For every role, include at least one row. If no FLS exception exists for a role:
  [Role] | (no exceptions) | Default applies to all fields | No | N/A
Do not omit roles from this table.

**Table 3 — Record Access Scope**

| Role | Scope | Condition (if conditional) | H-flag |
|------|-------|---------------------------|--------|

One row per role. State the explicit scope assignment — do not infer from privilege level.

PHASE 2 COMPLETE — proceeding to Phase 3.

---

### PHASE 3: GAP ANALYSIS

**Table 4 — Four-Vector Escalation Sweep**

| Gap ID | Vector | Path Found (Yes/No) | Path Description or Controls Examined | H-flag |
|--------|--------|--------------------|-----------------------------------------|--------|
| | Record Reassignment | | | |
| | Team Promotion / Membership Elevation | | | |
| | Sharing Rule Bypass | | | |
| | Impersonation / Delegation | | | |

Gap ID column: Path Found = Yes → assign next Gap ID. Path Found = No → leave blank.
For every No: name the specific controls examined and provide a one-sentence null
justification. Do not write No without naming what was checked.

**Table 5 — Sharing Rule Analysis**

| Gap ID | Rule Name / Type | Widens Baseline? | Conflict? | Description | H-flag |
|--------|-----------------|-----------------|-----------|-------------|--------|

Gap ID column: Conflict? = Yes → assign next Gap ID. Conflict? = No → leave blank.
Null rows must still appear with specific rules named and one-sentence safe justification.
Examine criteria-based, owner-based, and manual sharing rules.
Include at least one row.

**Table 6 — Team Membership Gaps**

| Gap ID | Team | Role / User Scenario | Gap Type (Excess / Missing) | Access Impact | H-flag |
|--------|------|---------------------|---------------------------|---------------|--------|

Gap ID column: Gap found → assign next Gap ID. No gap → leave blank.
Null rows must name teams examined and justify null result.
Include at least one row — do not leave the table empty.

**Table 7 — Gap Summary**

| Gap ID | Description | Gap Type | Severity (H/M/L) | Source (Table + Row) | H-flag |
|--------|-------------|----------|-----------------|----------------------|--------|

Gap ID column: Each row must use a Gap ID assigned in Tables 4, 5, or 6.
Do not create new Gap IDs here.
Source column: Cite the table and row where this Gap ID was assigned
  (e.g., "Table 4, Row 1 — Record Reassignment, Path Found = Yes").
Every Gap ID from Tables 4, 5, 6 must appear. This table is a consolidation —
not a new analysis. Adding a row without a Phase 3 source is a provenance error.

PHASE 3 COMPLETE — proceeding to Phase 4.

---

### PHASE 4: RISK-RANKED SUMMARY, REMEDIATION, AND HYPOTHESIS RESOLUTION

**Risk-Ranked Gap List** (High → Medium → Low)

For each row in Table 7, in severity order, referenced by Gap ID:
1. One-line risk justification (why this severity, given the operation and data)
2. Concrete remediation: name the role / field / rule / team + exact action

Acceptable: "G-01: Add FLS read-deny on AccountNumber for Customer Service role"
Not acceptable: "Restrict sensitive field access"

Every item must reference a Gap ID from Table 7. A Gap ID not present in Tables 4, 5,
or 6 must not appear here. Phase 4 is a rendering of Table 7 in risk order — not a
new analysis.

**Hypothesis Resolution Table**

| Hypothesis | Status | Evidence Reference |
|------------|--------|--------------------|

Status values: Confirmed / Refuted / Modified.

Evidence Reference must cite a specific table and row
(e.g., "Table 2, Row 3 — AccountNumber, Customer Service, Read = Allow").
Do not write "see above." Do not reference sections. Reference rows.

If a hypothesis is Modified, add a note below the table stating the corrected finding.

PHASE 4 COMPLETE.
```

---

## V-04 — Combined: Source Column + Gap ID Threading + Inventory Gate + H-flag + Phase Gates
**Axes:** All three C-15 mechanisms (V-01 + V-02 + V-03) layered onto R3 V-04's C-13 + C-14 base
**Hypothesis:** Three independent C-15 enforcement mechanisms operating at different granularities
create a defense-in-depth provenance guarantee. Level 1 (Gap ID at source table row) makes
provenance visible at discovery. Level 2 (Source column in Table 7) makes provenance visible at
consolidation. Level 3 (inventory gate assertion) makes provenance visible at section transition.
A model would have to fail all three mechanisms simultaneously to introduce a spurious Phase 4 gap.
This is the combinatorial analog of R3 V-04's dual-mechanism design — and the predicted ceiling
for v4's 130-point rubric.

---

```
You are a Dataverse security expert and Customer Service domain specialist.
Trace the permissions model for: {{topic}}

Three structural requirements apply throughout this entire output:

**Requirement A — H-flag columns**
Every evidence table must include an H-flag column as the rightmost column.
H-flag column rules:
  - Row is evidence for a hypothesis → enter the hypothesis label (H1, H2, ...)
  - Row is not tied to any hypothesis → enter N/A
  - Never leave an H-flag cell blank

**Requirement B — Phase completion gates**
Before beginning each new phase, output the following line exactly, on its own line,
in all-caps:
  PHASE [N] COMPLETE — proceeding to Phase [N+1].
This is a state transition assertion, not a heading. The next phase does not begin
until this line appears. Placing the marker before the section content is complete
does not satisfy this requirement.

**Requirement C — Gap provenance enforcement (three levels)**
Every gap that appears in Phase 4 must trace to a specific row in Table 7.
Every row in Table 7 must trace to a specific row in Table 4, 5, or 6.
This chain is enforced at three independent levels:

  Level 1 — Gap IDs assigned at discovery:
    Tables 4, 5, and 6 each have a Gap ID column. Assign a Gap ID (G-01, G-02, ...)
    in the row where a gap is first found. IDs are sequential across all three tables.
    Rows with no gap: leave Gap ID blank. Gap IDs exist only after a Phase 3 row creates them.

  Level 2 — Source column in Table 7:
    Table 7 has a Source column. Every row must cite the Phase 3 table and row where
    its Gap ID was assigned (e.g., "Table 5, Row 2 — CS Sharing Rule, Conflict = Yes").
    Rows without a traceable Phase 3 source must not appear in Table 7.

  Level 3 — Phase 3 inventory assertion:
    Before the PHASE 3 COMPLETE marker, output an inventory block in this format:
      Gap inventory: [all Gap IDs — e.g., G-01, G-02, G-03]
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

PHASE 1 COMPLETE — proceeding to Phase 2.

---

### PHASE 2: EVIDENCE TABLES

**Table 1 — Role-Operation Matrix**

| Role | Create | Read | Update | Delete | Assign | Share | H-flag |
|------|--------|------|--------|--------|--------|-------|--------|

Values: Allow / Deny / Not Configured / Conditional.
Fill every cell. If a role or operation cannot be determined, write Unknown
and note what information is missing.

**Table 2 — Field-Level Security**

| Role | Field Name | Access (R/W/Deny) | Default Override | H-flag |
|------|------------|-------------------|-----------------|--------|

For every role, include at least one row. If no FLS exception exists for a role:
  [Role] | (no exceptions) | Default applies to all fields | No | N/A
Do not omit roles from this table.

**Table 3 — Record Access Scope**

| Role | Scope | Condition (if conditional) | H-flag |
|------|-------|---------------------------|--------|

One row per role. State the explicit scope assignment — do not infer from privilege level.

PHASE 2 COMPLETE — proceeding to Phase 3.

---

### PHASE 3: GAP ANALYSIS

**Table 4 — Four-Vector Escalation Sweep**

| Gap ID | Vector | Path Found (Yes/No) | Path Description or Controls Examined | H-flag |
|--------|--------|--------------------|-----------------------------------------|--------|
| | Record Reassignment | | | |
| | Team Promotion / Membership Elevation | | | |
| | Sharing Rule Bypass | | | |
| | Impersonation / Delegation | | | |

Path Found = Yes → assign next Gap ID in the Gap ID column.
Path Found = No → leave Gap ID blank; name specific controls and provide
one-sentence null justification. Do not write No without naming what was checked.

**Table 5 — Sharing Rule Analysis**

| Gap ID | Rule Name / Type | Widens Baseline? | Conflict? | Description | H-flag |
|--------|-----------------|-----------------|-----------|-------------|--------|

Conflict? = Yes → assign next Gap ID.
Conflict? = No → leave Gap ID blank; name specific rules and explain why each is safe.
Examine criteria-based, owner-based, and manual sharing rules.
Include at least one row.

**Table 6 — Team Membership Gaps**

| Gap ID | Team | Role / User Scenario | Gap Type (Excess / Missing) | Access Impact | H-flag |
|--------|------|---------------------|---------------------------|---------------|--------|

Gap found → assign next Gap ID.
No gap → leave blank; name teams examined and justify null result.
Include at least one row — do not leave the table empty.

**Table 7 — Gap Summary**

| Gap ID | Description | Gap Type | Severity (H/M/L) | Source (Table + Row) | H-flag |
|--------|-------------|----------|-----------------|----------------------|--------|

Gap ID: Must match a Gap ID assigned in Tables 4, 5, or 6. Do not create new Gap IDs here.
Source: Cite the table and row where this Gap ID was assigned
  (e.g., "Table 4, Row 1 — Record Reassignment, Path Found = Yes").
Every Gap ID from Tables 4, 5, 6 must appear. This table is a consolidation operation,
not a new analysis layer. Adding a row without a Phase 3 source is a provenance error.

Gap inventory: [list all Gap IDs — e.g., G-01, G-02, G-03]
Phase 4 references only these Gap IDs. No new gaps will be introduced in Phase 4.
PHASE 3 COMPLETE — proceeding to Phase 4.

---

### PHASE 4: RISK-RANKED SUMMARY, REMEDIATION, AND HYPOTHESIS RESOLUTION

**Risk-Ranked Gap List** (High → Medium → Low)

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
(e.g., "Table 2, Row 3 — AccountNumber, Customer Service, Read = Allow").
Do not write "see above." Do not reference sections. Reference rows.

If a hypothesis is Modified, add a note below the table stating the corrected finding.

PHASE 4 COMPLETE.
```

---

## V-05 — Combined: Source Column + Inertia Framing + H-flag + Phase Gates
**Axes:** Source column in Table 7 (C-15) + inertia framing ("what breaks if this changes?") + H-flag (C-13) + phase gates (C-14)
**Hypothesis:** Inertia framing surfaces latent gaps that static-snapshot tracing misses —
escalation paths that open under specific conditions, FLS overrides that create silent exposure
under role modification, team combinations that exceed intended scope when a new team is added.
Pairing this content-richness mechanism with a source column in Table 7 achieves two goals
simultaneously: more gaps discovered (inertia framing), and all discovered gaps structurally
anchored before Phase 4 begins (source column). This tests whether content-plus-provenance
outperforms pure structural enforcement (V-04's triple mechanism design) or whether V-04's
additional C-15 mechanisms add discriminating power beyond what V-05 provides.

---

```
You are a Dataverse security expert and Customer Service domain specialist.
Trace the permissions model for: {{topic}}

Don't just document the current state. At every step, apply the inertia question:
"If this configuration changed — a role modified, a sharing rule added, a team
reassigned — what would break, and for whom?"

Inertia framing surfaces gaps that static snapshots miss: escalation paths that only
open under misconfiguration, FLS overrides that create silent exposure when table
defaults shift, team combinations that exceed intent when membership is adjusted.

Two structural requirements apply throughout this entire output:

**Requirement A — H-flag columns**
Every evidence table must include an H-flag column as the rightmost column.
H-flag column rules:
  - Row is evidence for a hypothesis → enter the hypothesis label (H1, H2, ...)
  - Row is not tied to any hypothesis → enter N/A
  - Never leave an H-flag cell blank

**Requirement B — Phase completion gates**
Before beginning each new phase, output the following line exactly, on its own line,
in all-caps:
  PHASE [N] COMPLETE — proceeding to Phase [N+1].
This is a state transition assertion, not a heading. The next phase does not begin
until this line appears. Placing the marker before the section content is complete
does not satisfy this requirement.

---

### PHASE 1: HYPOTHESIS PRE-COMMITMENT

Before examining any artifacts, state at least two hypotheses about expected security
gaps. For each hypothesis, also name what configuration change would activate it —
this forces pre-commitment to the scenario, not just the gap type.

Each hypothesis must:
- Label: H1, H2, (H3 if needed)
- Gap type: missing FLS / over-permissive role / sharing rule conflict /
  team membership gap / privilege escalation path
- Suspect role(s) and operation(s)
- What change or scenario would cause this gap to emerge

Do not produce any evidence tables until all hypotheses are written here.

PHASE 1 COMPLETE — proceeding to Phase 2.

---

### PHASE 2: EVIDENCE TABLES

**Table 1 — Role-Operation Matrix**

| Role | Create | Read | Update | Delete | Assign | Share | H-flag |
|------|--------|------|--------|--------|--------|-------|--------|

Values: Allow / Deny / Not Configured / Conditional.
Fill every cell. For any Assign or Share = Allow: note what workflow or access
pattern depends on that permission remaining in place.
If a role or operation cannot be determined, write Unknown and note what is missing.

**Table 2 — Field-Level Security**

| Role | Field Name | Access (R/W/Deny) | Default Override | What breaks if this access is removed? | H-flag |
|------|------------|-------------------|-----------------|----------------------------------------|--------|

For every role, include at least one row. If no FLS exception exists for a role:
  [Role] | (no exceptions) | Default applies to all fields | No |
  Removing table default exposes all fields to this role with no override in place | N/A
Do not omit roles from this table.

**Table 3 — Record Access Scope**

| Role | Scope | Condition (if conditional) | What breaks if scope narrows by one level? | H-flag |
|------|-------|---------------------------|--------------------------------------------|--------|

One row per role. State the explicit scope assignment — do not infer from privilege level.

PHASE 2 COMPLETE — proceeding to Phase 3.

---

### PHASE 3: GAP ANALYSIS

**Table 4 — Four-Vector Escalation Sweep**

| Vector | Path Found (Yes/No) | Path Description or Controls Examined | What change would open this path? | H-flag |
|--------|--------------------|-----------------------------------------|----------------------------------|--------|
| Record Reassignment | | | | |
| Team Promotion / Membership Elevation | | | | |
| Sharing Rule Bypass | | | | |
| Impersonation / Delegation | | | | |

For every No: name the specific controls examined, provide a one-sentence null
justification, and name the specific configuration change that would nullify those controls.
Do not write No without naming what was checked.

**Table 5 — Sharing Rule Analysis**

| Rule Name / Type | Widens Baseline? | Conflict? | Description | What triggers this conflict? | H-flag |
|-----------------|-----------------|-----------|-------------|------------------------------|--------|

"What triggers this conflict?" column: name the specific condition under which the rule
fires on a record the role should not reach — the inertia scenario for this rule.
Examine criteria-based, owner-based, and manual sharing rules.
Include at least one row identifying a conflict or confirming null with specific rules named.

**Table 6 — Team Membership Gaps**

| Team | Role / User Scenario | Gap Type (Excess / Missing) | Access Impact | H-flag |
|------|---------------------|---------------------------|---------------|--------|

Consider: what happens when a user joins an additional team by mistake, or is
removed from the expected team? Name the team and the access impact in each direction.
Include at least one row.

**Table 7 — Gap Summary**

| Gap ID | Description | Gap Type | Severity (H/M/L) | Source (Table + Row) | H-flag |
|--------|-------------|----------|-----------------|----------------------|--------|

Source column rules:
  - Cite the specific table and row where this gap was first recorded
    (e.g., "Table 4, Row 2 — Record Reassignment, Path Found = Yes")
  - Every row in Table 7 must trace to a row in Table 4, 5, or 6
  - Gaps not traceable to a Phase 3 row must not appear in this table
  - This table is a consolidation of Phase 3 findings, not a new analysis layer

Every gap named in Tables 4, 5, and 6 must appear as a row here.

PHASE 3 COMPLETE — proceeding to Phase 4.

---

### PHASE 4: RISK-RANKED SUMMARY, REMEDIATION, AND HYPOTHESIS RESOLUTION

**Risk-Ranked Gap List** (High → Medium → Low)

For each row in Table 7, in severity order, referenced by Gap ID:
1. One-line risk justification (why this severity, given the operation and data)
2. Concrete remediation: name the role / field / rule / team + exact action

Acceptable: "G-01: Add FLS read-deny on AccountNumber for Customer Service role"
Not acceptable: "Restrict sensitive field access"

Phase 4 contains no new gap analysis. Every item must appear in Table 7.
Reference each gap by its Gap ID from Table 7.

**Hypothesis Resolution Table**

| Hypothesis | Status | Evidence Reference |
|------------|--------|--------------------|

Status values: Confirmed / Refuted / Modified.

Evidence Reference must cite a specific table and row
(e.g., "Table 2, Row 3 — AccountNumber, Customer Service, Read = Allow").
Do not write "see above." Do not reference sections. Reference rows.

If a hypothesis is Modified, add a note below the table stating the corrected finding.

PHASE 4 COMPLETE.
```

---

## Variation Summary

| ID | Axes | C-15 Mechanism | Key C-criteria targeted |
|----|------|---------------|------------------------|
| V-01 | Output format | Source column in Table 7 — backward reference from consolidation to Phase 3 row | C-15 (cell-level); retains C-13 + C-14 from R3 V-04 |
| V-02 | Lifecycle emphasis | Phase 3 gate with Gap ID inventory commitment — provenance at section-transition | C-15 (gate-level); retains C-13 + C-14 from R3 V-04 |
| V-03 | Output format | Gap ID threading from source tables — forward chain at discovery row | C-15 (discovery-level); retains C-13 + C-14 from R3 V-04 |
| V-04 | All three C-15 axes combined | Source column + Gap ID threading + inventory gate — three independent provenance mechanisms | C-15 at three granularities; C-13 + C-14; predicted ceiling for v4 |
| V-05 | Source column + Inertia framing | Source column (C-15) + "what breaks if this changes?" (content richness) | C-15 + richer C-05/C-06/C-07 discovery; tests content-plus-provenance vs pure structural |

**Predicted scores against v4 rubric (130 pt ceiling):**

| Variation | Predicted Score | C-13 | C-14 | C-15 | Reasoning |
|-----------|----------------|------|------|------|-----------|
| V-04 | 130/130 | PASS | PASS | PASS | All five mechanisms cover all three aspirational structural criteria |
| V-01 | 130/130 | PASS | PASS | PASS | Source column structurally sufficient for C-15; H-flag + gates retained |
| V-02 | 130/130 | PASS | PASS | PASS | Inventory gate structurally sufficient for C-15; H-flag + gates retained |
| V-03 | 130/130 | PASS | PASS | PASS | Gap ID threading structurally sufficient for C-15; H-flag + gates retained |
| V-05 | 130/130 | PASS | PASS | PASS | Source column covers C-15; inertia framing adds content depth not at C-15 risk |

**Key discriminating question for R4:** If all five variations pass C-15, what separates them?
The scorecard will need to test whether each C-15 mechanism is genuinely sufficient or whether
any mechanism has a structural gap that allows a well-formed output to pass the prompt but fail
the criterion. The inertia framing in V-05 introduces additional table columns ("What breaks...")
that create width — does that width create compliance risk for any criterion?

**Inertia framing risk (V-05):** R3 V-05 scored 115/125 (failed C-13 + C-14). In V-05 here,
those mechanisms are explicitly retained. But V-05's inertia columns ("What breaks if this
access is removed?", "What triggers this conflict?") add table width and may distract from the
H-flag and Source column requirements. If V-05 fails, it will be because inertia framing
creates friction against Requirement A (H-flag always rightmost) or Table 7 Source column
compliance — not because inertia framing is wrong in principle.
