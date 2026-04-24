# trace-permissions -- Round 11 Variations

**Rubric version**: v10 (32 criteria -- C-30/C-31/C-32 added from R10 excellence signals V-05)
**Round**: 11
**Date**: 2026-03-15
**Axes explored**:
- V-01: C-32 Top-Down Privilege Descent as structural spine (single)
- V-02: C-31 Pre-Declared Structural Identifiers as slot-filling framework (single)
- V-03: C-30 SHALL-Condition Compliance Tests throughout preamble register (single)
- V-04: C-30 + C-31 combined (SHALL conditions + pre-declared identifiers)
- V-05: C-31 + C-32 + C-30 combined (full triple integration)

**Scoring formula change from R10**: Aspirational denominator is now 25 (not 22). Max aspirational = (pass_count / 25) x 10. Each passed aspirational criterion is worth 0.40 pts.

**New criteria targeted**:
- C-30: Each preamble register entry expressed as SHALL condition + named compliance test
- C-31: All structural element identifiers declared before analysis begins
- C-32: Role analysis ordered SysAdmin -> Manager -> CSR; each non-max role opens with explicit delta from role above

---

## V-01

**Variation axis**: C-32 Top-Down Privilege Descent as structural spine
**Hypothesis**: Making descent ordering the explicit organizing axis of the prompt -- not merely a requirement stated in an instruction block -- causes C-10 delta tracking to emerge as a natural byproduct of section headers rather than a separate tracking step. When the prompt is structured so that each role section MUST open with a delta statement relative to the role above, the model cannot produce a role section without generating the delta. The prior infrastructure (preamble register, inertia columns, split-row checklist) remains unchanged so the signal is isolated to the ordering axis.

---

You are a Dataverse security expert. Produce a complete permission trace for the feature described below.

**Feature**: {{topic}}
**Roles** (in descent order, maximum to minimum privilege): {{roles}} -- default: System Administrator, Customer Service Manager, Customer Service Representative

**ANALYSIS ORDERING RULE**: The role analysis in every section runs in top-down privilege descent order: System Administrator first, then Customer Service Manager, then Customer Service Representative. Each non-maximum role section MUST open with an explicit DELTA statement naming what the role immediately above it holds that this role does not. This is not optional -- a section that begins with role capabilities without first stating the delta from the role above is structurally incomplete.

---

## PREAMBLE: Anti-Pattern Register

Before analysis begins, this register states what satisfies and what does NOT satisfy the structural criteria most commonly causing incomplete outputs. Every section references criteria by ID.

| Criterion | What SATISFIES | What Does NOT Satisfy |
|-----------|---------------|----------------------|
| **C-24** Sweep Execution Confirmation | Two orthogonal markers per sweep: Execution (Checked: Yes/No) AND Status (CLEAN / FINDING PRESENT) as separate labeled fields | A single combined marker such as "Sweep A: CLEAN" -- conflates execution with outcome; cannot distinguish "ran and found nothing" from "skipped" |
| **C-25** Inertia Framing Cross-Section | Every section-level finding or clean-outcome statement includes an explicit note about what standard operational behavior produces or sustains that state | Inertia framing confined only to the gap registry -- absent from role-matrix sections, FLS table, and sweep conclusions |
| **C-27** Inertia Note Per-Row Column | Each structured table includes a named "Inertia Note" column; every row carries its own annotation in that column | Section-level inertia narrative above or below a table but not instantiated as a column within the table |
| **C-28** Terminal Checklist Split Rows | Terminal checklist has separate rows per sweep: "Sweep A -- Execution: Yes/No" and "Sweep A -- Status: CLEAN / FINDING PRESENT" as distinct checklist items | Single combined row per sweep such as "Sweep A: Checked, CLEAN" |
| **C-29** Three-Way Inertia Taxonomy | Each gap's failure mode classified as: (a) process absent / (b) process present but insufficient frequency / (c) process present but insufficient scope | Naming the organizational behavior that would miss a gap without classifying which failure type it represents |
| **C-32** Top-Down Privilege Descent | Each non-maximum role section opens with an explicit DELTA statement: what the role above holds that this role does not | Analyzing roles in alphabetical order, isolated sections, or bottom-up; or presenting role capabilities without an opening delta statement |
| **C-18** Baseline Declaration | Zero-permission baseline declared before any role enumeration; all gaps are named departures from that baseline | Beginning directly with role capabilities without establishing the zero-point |
| **C-20** Sweep Vector Binary Status | Explicit CLEAN / FINDING PRESENT label as a discrete labeled element separate from narrative | Status embedded only in prose sentences requiring parsing to infer completeness |

---

### Section 0: Baseline Zero-Point Declaration

Declare the permission state that exists before any security role is assigned:

- Default record operations for any authenticated user on this entity type (typically: none beyond org-level read for some entities)
- FLS configured by default on sensitive fields (typically: none configured)
- Sharing rules active by default
- Teams configured by default

Write the baseline anchor sentence:
> *"The baseline permission state for {{topic}} is: ___. Every finding below is a deviation from -- or failure to deviate from -- this state."*

**Inertia note** (C-25): State what standard organizational behavior (default provisioning, IT onboarding scripts, standing configuration templates) produces or sustains this baseline state.

---

### Section 1: Role-Operation Matrix -- Descent Order

Build the complete role-operation matrix. Columns run in descent order: System Administrator | Customer Service Manager | Customer Service Representative. Operations as rows: Create, Read, Update, Delete, Assign, Share. Values: Allow / Deny / N/A+reason. No blank cells.

| Operation | System Administrator | CS Manager | CS Representative | Inertia Note |
|-----------|---------------------|------------|-------------------|--------------|
| Create    |                     |            |                   |              |
| Read      |                     |            |                   |              |
| Update    |                     |            |                   |              |
| Delete    |                     |            |                   |              |
| Assign    |                     |            |                   |              |
| Share     |                     |            |                   |              |

**N/A rule** (C-15): Any N/A cell must carry a parenthetical reason on the same line.
**Inertia Note column** (C-27): For each operation row, state what periodic process or standing organizational behavior produces the current Allow/Deny configuration across all roles. If no process enforces this, classify: (a) absent / (b) insufficient frequency / (c) insufficient scope.

For each role, also state:
- **Record access scope**: Own / Business Unit / Parent BU / Organization
- **Scope grant source**: Security Role / Team Membership / Sharing Rule (C-12)

**DELTA opener requirement** (C-32): Before presenting CS Manager capabilities, open with:
> *"DELTA from System Administrator: CS Manager does NOT hold: [list operations/scope/FLS items held by SysAdmin that Manager does not]"*

Before presenting CS Representative capabilities, open with:
> *"DELTA from CS Manager: CS Representative does NOT hold: [list operations/scope/FLS items held by Manager that CSR does not]"*

**Section closure** (C-21): State either a named finding with role/mechanism/scope or: *"No role-operation misconfiguration identified in Section 1."*
**Inertia note** (C-25): State what standard operational behavior produces or sustains the current role-operation configuration.

---

### Section 2: Field-Level Security -- Descent Order

For each sensitive field relevant to {{topic}}, state FLS per role in descent order: System Administrator | CS Manager | CS Representative. Values: Allow / Deny / Not Configured. No blank cells.

| Field | System Administrator | CS Manager | CS Representative | Inertia Note |
|-------|---------------------|------------|-------------------|--------------|
|       |                     |            |                   |              |

**Not Configured is a finding** (C-14): Write "Not Configured" explicitly -- do not omit the row or leave the cell blank.
**Inertia Note column** (C-27): For each field row, state what standard organizational behavior (default profile inheritance, provisioning tooling that does not configure FLS columns) sustains the Not Configured state.

**DELTA opener requirement** (C-32): Before each non-maximum role column, note:
> *"DELTA from [role above]: [field X] moves from Allow -> Not Configured"* or equivalent per-field FLS delta.

State this as a lead-in to the FLS table or as annotated column headers for Manager and CSR.

**Section closure** (C-21): State either a named FLS finding or: *"No FLS misconfiguration identified in Section 2."*
**Inertia note** (C-25): State what standard operational behavior produces or sustains the current FLS configuration.

---

### Section 3: Role Transition Delta Table

For each adjacent role pair in descent order, state exactly what the higher role has that the lower role does not.

| Transition | Operations Added (by higher) | Scope Change | FLS Resolved | FLS Still Not Configured | Inertia Note |
|------------|------------------------------|--------------|-------------|--------------------------|--------------|
| SysAdmin -> Manager |                 |              |             |                          |              |
| Manager -> CSR      |                 |              |             |                          |              |

**Persistent FLS gap tracking** (C-16): Any field appearing in "FLS Still Not Configured" at every transition row is labeled: *"Persistent FLS Gap -- not configured at any role level."*
**Inertia Note column** (C-27): For each transition row, state what provisioning or role-management process would or would not surface this specific delta.

**Section closure** (C-21): State either a named transition anomaly or: *"No transition delta anomaly identified in Section 3."*

---

### Section 4: Named Security Gaps

Name at least one concrete misconfiguration before the escalation sweep (C-04). For each gap: role, field or operation, risk tier with justification (C-08), remediation action (C-09), inertia default, and failure type classification (C-29).

| Gap | Role | Field/Operation | Risk | Remediation | Inertia Default | Failure Type |
|-----|------|-----------------|------|-------------|-----------------|--------------|
| G-01 | | | High/Med/Low: [reason] | [specific config action] | [org behavior that would miss this] | (a)/(b)/(c) |

**Failure Type** (C-29): Classify the inertia default into: (a) process absent / (b) process present but insufficient frequency / (c) process present but insufficient scope.

---

### Section 5: Escalation Sweep -- All Three Mechanism Types

Address all three escalation vectors regardless of whether each yields a finding (C-11, C-17).

**Mechanism A -- Record Reassignment**
Can a lower-privilege user reassign a record to gain scope their role does not allow? State: who -> via what action -> resulting scope.

- **Execution** (C-24): Checked: Yes / No
- **Status** (C-20): CLEAN / FINDING PRESENT
- **Inertia note** (C-25): [what standard operational behavior sustains or would miss this path]
- If clean: *"No record reassignment escalation path identified. Scope examined: {{topic}} records within CSR-accessible BU."*

**Mechanism B -- Team Membership Addition**
Does adding a user to any team grant scope exceeding their security role baseline?

- **Execution** (C-24): Checked: Yes / No
- **Status** (C-20): CLEAN / FINDING PRESENT
- **Inertia note** (C-25): [what team roster management behavior sustains or would miss this path]
- If clean: *"No team membership escalation path identified. Teams examined: {{topic}}-relevant access teams and owner teams."*

**Mechanism C -- Sharing Rule Exploitation**
Does any sharing rule widen access beyond the security role baseline?

- **Execution** (C-24): Checked: Yes / No
- **Status** (C-20): CLEAN / FINDING PRESENT
- **Inertia note** (C-25): [what sharing-rule governance process sustains or would miss this path]
- If clean: *"No sharing rule escalation path identified. Rules examined: all sharing rules targeting {{topic}} entity."*

**Section closure** (C-21): State either a named escalation finding or: *"No escalation path identified across all three mechanism types."*

---

### Section 6: Team Membership Gap

Identify at least one team membership anomaly (C-07). Name the team, the user or role scenario, and the resulting scope delta.

- **Status** (C-20): CLEAN / FINDING PRESENT
- **Inertia note** (C-25): [what team-management process sustains or would miss this gap]
- If none: *"No team membership gap identified for {{topic}}. Scope examined: all teams with access to {{topic}} entity."*

If finding present: add to gap registry in Section 4 with Failure Type classification (C-29).

**Section closure** (C-21): State the finding or explicit absence.

---

### Section 7: Sharing Rule Conflict

Identify at least one sharing rule that widens access beyond role baseline or creates a contradiction (C-06).

- **Status** (C-20): CLEAN / FINDING PRESENT
- **Inertia note** (C-25): [what sharing-rule governance behavior sustains or would miss this conflict]
- If none: *"No sharing rule conflict identified for {{topic}}. Rules examined: all rules targeting {{topic}} entity type."*

**Section closure** (C-21): State the finding or explicit absence.

---

### Section 8: Terminal Structural Completion Checklist

Confirm structural completeness (C-22). Each sweep vector has two separate checklist rows (C-28).

**Table and registry markers:**
- [ ] Section 1 Role-Operation Matrix: complete (no blank cells, all N/A justified, delta openers present for Manager and CSR)
- [ ] Section 2 FLS Table: complete (all Not Configured explicit, delta openers present)
- [ ] Section 3 Transition Delta Table: complete (persistent FLS gaps labeled)
- [ ] Section 4 Gap Registry: at least one entry, all columns populated, Failure Type classified

**Sweep execution and status markers (C-28 split rows):**
- [ ] SA-Exec: Sweep A (Record Reassignment) -- Execution: Yes / No
- [ ] SA-Status: Sweep A (Record Reassignment) -- Status: CLEAN / FINDING PRESENT
- [ ] SB-Exec: Sweep B (Team Membership) -- Execution: Yes / No
- [ ] SB-Status: Sweep B (Team Membership) -- Status: CLEAN / FINDING PRESENT
- [ ] SC-Exec: Sweep C (Sharing Rule) -- Execution: Yes / No
- [ ] SC-Status: Sweep C (Sharing Rule) -- Status: CLEAN / FINDING PRESENT

**Section closure markers:**
- [ ] Section 1 closure: stated
- [ ] Section 2 closure: stated
- [ ] Section 3 closure: stated
- [ ] Section 5 closure: stated
- [ ] Section 6 closure: stated
- [ ] Section 7 closure: stated

**Inertia column markers (C-27):**
- [ ] Role matrix Inertia Note column: present and populated in every row
- [ ] FLS table Inertia Note column: present and populated in every row
- [ ] Delta table Inertia Note column: present and populated in every row

**Descent ordering markers (C-32):**
- [ ] Section 1: DELTA opener present before CS Manager analysis
- [ ] Section 1: DELTA opener present before CS Representative analysis
- [ ] Section 2: FLS delta noted for each non-maximum role column

*"Structural completion verification complete. All STATUS markers confirmed present. Descent ordering confirmed via delta openers."*

---

## V-02

**Variation axis**: C-31 Pre-Declared Structural Identifiers as slot-filling framework
**Hypothesis**: When the prompt opens with an explicit Structural Element Registry that names every identifier -- checklist row IDs, table column names, taxonomy condition labels -- before any analysis section begins, the output converts from a narrative exercise to a slot-filling exercise. The model must populate named slots; it cannot improvise or defer structure. This should eliminate the pattern where structural elements appear for the first time mid-analysis (the C-31 failure mode). The prior infrastructure (preamble register, inertia columns, descent ordering) is present but no new behavioral emphasis is added -- the signal is isolated to the pre-declaration axis.

---

You are a Dataverse security expert. Produce a complete permission trace for the feature described below.

**Feature**: {{topic}}
**Roles**: {{roles}} -- default: Customer Service Representative, Customer Service Manager, System Administrator

---

## PREAMBLE PART 1: Structural Element Registry

All structural element identifiers used in this analysis are declared here before any analysis section begins. Sections populate these named slots. An auditor can verify compliance by checking for identifier presence without re-reading surrounding prose.

**Checklist Row IDs** (terminal checklist, Section 8):

| Row ID | Description |
|--------|-------------|
| M-Complete | Role-Operation Matrix complete (no blank cells, all N/A justified) |
| F-Complete | FLS Table complete (all Not Configured explicit, no blank cells) |
| D-Complete | Delta Table complete (persistent gaps labeled) |
| G-Complete | Gap Registry complete (at least one entry, all columns populated) |
| SA-Exec | Sweep A (Record Reassignment) -- Execution marker |
| SA-Status | Sweep A (Record Reassignment) -- Status marker |
| SB-Exec | Sweep B (Team Membership Addition) -- Execution marker |
| SB-Status | Sweep B (Team Membership Addition) -- Status marker |
| SC-Exec | Sweep C (Sharing Rule Exploitation) -- Execution marker |
| SC-Status | Sweep C (Sharing Rule Exploitation) -- Status marker |
| S1-Close | Section 1 outcome closure |
| S2-Close | Section 2 outcome closure |
| S3-Close | Section 3 outcome closure |
| S5-Close | Section 5 outcome closure |
| S6-Close | Section 6 outcome closure |
| S7-Close | Section 7 outcome closure |

**Table Column Names**:

| Table | Required Columns |
|-------|-----------------|
| Role-Operation Matrix | Operation, [Role columns in order], Inertia Note |
| FLS Table | Field, [Role columns in order], Inertia Note |
| Role-Transition Delta Table | Transition, Operations Added, Scope Change, FLS Resolved, FLS Still Not Configured, Inertia Note |
| Gap Registry | Gap, Role, Field/Operation, Risk, Remediation, Inertia Default, Failure Type |

**Taxonomy Condition Labels** (used in Failure Type column and Inertia Default classification):

- **(a) process absent**: No organizational process exists to detect this gap
- **(b) process present but insufficient frequency**: A periodic review cycle exists but its cadence would not catch intra-period changes
- **(c) process present but insufficient scope/coverage**: A review process exists but excludes this specific vector or combination

These three labels are the only valid values for the Failure Type column in the Gap Registry. No other classification labels are permitted.

---

## PREAMBLE PART 2: Anti-Pattern Register

| Criterion | What SATISFIES | What Does NOT Satisfy |
|-----------|---------------|----------------------|
| **C-24** Sweep Execution Confirmation | Two orthogonal markers per sweep vector: SA-Exec (Checked: Yes/No) AND SA-Status (CLEAN / FINDING PRESENT) as separate labeled checklist items using declared row IDs | A single combined marker per sweep -- collapses execution with outcome; SA-Exec and SA-Status must appear as independent rows |
| **C-25** Inertia Framing Cross-Section | Every section-level finding or clean-outcome statement includes an explicit Inertia Note using the declared taxonomy labels; Inertia Note column present in all three declared tables | Inertia framing confined to gap registry; absent from role-matrix rows, FLS rows, and sweep conclusions |
| **C-27** Inertia Note Per-Row Column | Tables use the declared column name "Inertia Note" in exact form; every row carries a populated annotation | Narrative about inertia appearing above or below the table but not as a column named "Inertia Note" within it |
| **C-28** Terminal Checklist Split Rows | Terminal checklist uses declared row IDs SA-Exec, SA-Status, SB-Exec, SB-Status, SC-Exec, SC-Status as separate items | Single combined checklist row per sweep that does not use the declared split-row IDs |
| **C-29** Three-Way Inertia Taxonomy | Gap Failure Type column uses exactly one of: (a) process absent / (b) process present but insufficient frequency / (c) process present but insufficient scope | Any other classification label; narrative about inertia without using one of the three declared labels |
| **C-31** Pre-Declared Identifiers | All structural elements from the Structural Element Registry (Part 1 above) appear by their declared names in every section that uses them | Introducing a column name or checklist row ID for the first time mid-analysis without it appearing in the Structural Element Registry |
| **C-18** Baseline Declaration | Zero-permission baseline declared before Section 1; all gaps are departures from the named baseline | Proceeding directly to role capabilities without establishing the zero-point |
| **C-20** Sweep Vector Binary Status | Explicit binary label CLEAN / FINDING PRESENT as a discrete labeled element separate from narrative | Status only in prose; reader must parse sentences to determine outcome |

---

### Section 0: Baseline Zero-Point Declaration

Declare the permission state that exists before any security role is assigned for {{topic}}:

- Default record operations for any authenticated user (typically: none)
- FLS configured by default on sensitive fields (typically: none)
- Sharing rules active by default for this entity type
- Teams configured by default

> *"The baseline permission state for {{topic}} is: ___. Every finding below is a deviation from -- or failure to deviate from -- this state."*

**Inertia Note** (using declared taxonomy): State what standard organizational behavior produces or sustains this baseline state. Classify: (a) / (b) / (c).

---

### Section 1: Role-Operation Matrix

Build the complete Role-Operation Matrix using the declared column structure: Operation | [Role columns] | Inertia Note.

Every cell in the Role columns must contain Allow / Deny / N/A+reason. No blank cells.

| Operation | Customer Service Rep | CS Manager | System Administrator | Inertia Note |
|-----------|---------------------|------------|---------------------|--------------|
| Create    |                     |            |                     |              |
| Read      |                     |            |                     |              |
| Update    |                     |            |                     |              |
| Delete    |                     |            |                     |              |
| Assign    |                     |            |                     |              |
| Share     |                     |            |                     |              |

**Inertia Note column** (declared column "Inertia Note"): For each row, state the specific organizational process or standing behavior that produces the Allow/Deny configuration. Classify using declared labels: (a) / (b) / (c) if no enforcing process.

For each role, state:
- **Record access scope**: Own / Business Unit / Parent BU / Organization
- **Scope grant source**: Security Role / Team Membership / Sharing Rule

**N/A rule** (C-15): N/A cells require a parenthetical reason on the same line.

**Section closure** [S1-Close] (C-21): State either a named finding with role/mechanism/scope or: *"No role-operation misconfiguration identified in Section 1. [Inertia note: what process produces this state]."*

---

### Section 2: Field-Level Security

Build the FLS Table using the declared column structure: Field | [Role columns] | Inertia Note.

Every cell must contain Allow / Deny / Not Configured. No blank cells.

| Field | Customer Service Rep | CS Manager | System Administrator | Inertia Note |
|-------|---------------------|------------|---------------------|--------------|
|       |                     |            |                     |              |

**Not Configured is a finding** (C-14): Write "Not Configured" explicitly -- do not omit the row.
**Inertia Note column** (declared column "Inertia Note"): For each field row, state what provisioning behavior sustains the Not Configured state. Classify: (a) / (b) / (c).

**Section closure** [S2-Close] (C-21): State either a named FLS finding or: *"No FLS misconfiguration identified in Section 2. [Inertia note]."*

---

### Section 3: Role-Transition Delta Table

Build the Role-Transition Delta Table using the declared column structure: Transition | Operations Added | Scope Change | FLS Resolved | FLS Still Not Configured | Inertia Note.

| Transition | Operations Added | Scope Change | FLS Resolved | FLS Still Not Configured | Inertia Note |
|------------|-----------------|--------------|-------------|--------------------------|--------------|
| CSR -> Manager |            |              |             |                          |              |
| Manager -> SysAdmin |       |              |             |                          |              |

**Persistent FLS gap tracking** (C-16): Any field in "FLS Still Not Configured" across both transition rows is labeled: *"Persistent FLS Gap."*

**Section closure** [S3-Close] (C-21): State either a named delta anomaly or: *"No transition delta anomaly identified."*

---

### Section 4: Gap Registry

Name at least one concrete gap before the sweep. Populate the Gap Registry using the declared column structure: Gap | Role | Field/Operation | Risk | Remediation | Inertia Default | Failure Type.

| Gap | Role | Field/Operation | Risk | Remediation | Inertia Default | Failure Type |
|-----|------|-----------------|------|-------------|-----------------|--------------|
| G-01 | | | High/Med/Low: [reason] | [specific configuration action] | [organizational behavior that would miss this] | (a)/(b)/(c) |

**Failure Type** (C-29): Use exactly one declared taxonomy label per row: (a) process absent / (b) process present but insufficient frequency / (c) process present but insufficient scope.

---

### Section 5: Escalation Sweep -- All Three Mechanism Types

Address each sweep vector using declared row IDs for execution and status markers.

**Mechanism A -- Record Reassignment**
Can a lower-privilege user reassign a record to gain scope their role does not allow?

- [SA-Exec] Execution: Checked: Yes / No
- [SA-Status] Status: CLEAN / FINDING PRESENT
- **Inertia note**: [process or behavior that sustains or would miss this path; classify (a)/(b)/(c)]
- If clean: *"No record reassignment escalation path identified. Scope examined: [define]."*

**Mechanism B -- Team Membership Addition**
Does adding a user to any team grant scope exceeding their security role?

- [SB-Exec] Execution: Checked: Yes / No
- [SB-Status] Status: CLEAN / FINDING PRESENT
- **Inertia note**: [process or behavior that sustains or would miss this path; classify (a)/(b)/(c)]
- If clean: *"No team membership escalation path identified. Teams examined: [define]."*

**Mechanism C -- Sharing Rule Exploitation**
Does any sharing rule widen access beyond the security role baseline?

- [SC-Exec] Execution: Checked: Yes / No
- [SC-Status] Status: CLEAN / FINDING PRESENT
- **Inertia note**: [process or behavior that sustains or would miss this path; classify (a)/(b)/(c)]
- If clean: *"No sharing rule escalation path identified. Rules examined: [define]."*

**Section closure** [S5-Close] (C-21): State either a named escalation finding or: *"No escalation path identified across all three mechanism types."*

---

### Section 6: Team Membership Gap

Name at least one team membership anomaly: the team, the user or role scenario, and the resulting delta.

- Status (C-20): CLEAN / FINDING PRESENT
- **Inertia note**: [team-management behavior that sustains or would miss this gap; classify (a)/(b)/(c)]
- If clean: *"No team membership gap identified. Teams examined: [define]."*

**Section closure** [S6-Close] (C-21): State the finding or explicit absence.

---

### Section 7: Sharing Rule Conflict

Name at least one sharing rule that widens access beyond role baseline or creates a contradiction.

- Status (C-20): CLEAN / FINDING PRESENT
- **Inertia note**: [sharing-rule governance behavior that sustains or would miss this conflict; classify (a)/(b)/(c)]
- If clean: *"No sharing rule conflict identified. Rules examined: [define]."*

**Section closure** [S7-Close] (C-21): State the finding or explicit absence.

---

### Section 8: Terminal Structural Completion Checklist

Populate using declared row IDs. Each row uses the ID declared in the Structural Element Registry.

| Row ID | Item | Value |
|--------|------|-------|
| M-Complete | Role-Operation Matrix complete | Yes / No |
| F-Complete | FLS Table complete | Yes / No |
| D-Complete | Delta Table complete | Yes / No |
| G-Complete | Gap Registry complete | Yes / No |
| SA-Exec | Sweep A (Record Reassignment) -- Execution | Yes / No |
| SA-Status | Sweep A (Record Reassignment) -- Status | CLEAN / FINDING PRESENT |
| SB-Exec | Sweep B (Team Membership Addition) -- Execution | Yes / No |
| SB-Status | Sweep B (Team Membership Addition) -- Status | CLEAN / FINDING PRESENT |
| SC-Exec | Sweep C (Sharing Rule Exploitation) -- Execution | Yes / No |
| SC-Status | Sweep C (Sharing Rule Exploitation) -- Status | CLEAN / FINDING PRESENT |
| S1-Close | Section 1 outcome closure | Present / Absent |
| S2-Close | Section 2 outcome closure | Present / Absent |
| S3-Close | Section 3 outcome closure | Present / Absent |
| S5-Close | Section 5 outcome closure | Present / Absent |
| S6-Close | Section 6 outcome closure | Present / Absent |
| S7-Close | Section 7 outcome closure | Present / Absent |

**Inertia column audit** (C-27):
- [ ] Role matrix "Inertia Note" column: present and populated in every row
- [ ] FLS table "Inertia Note" column: present and populated in every row
- [ ] Delta table "Inertia Note" column: present and populated in every row

**Structural Element Registry audit** (C-31):
- [ ] All declared table column names appear in their respective tables by exact declared name
- [ ] All declared checklist row IDs appear in the terminal checklist
- [ ] All declared taxonomy labels (a)/(b)/(c) used in Failure Type and Inertia Note columns

*"Structural completion verification complete. All declared identifiers populated. All STATUS markers confirmed present."*

---

## V-03

**Variation axis**: C-30 SHALL-Condition Compliance Tests throughout preamble register
**Hypothesis**: Converting every preamble register entry from descriptive format ("What SATISFIES / What Does NOT Satisfy") to SHALL-condition format ("SHALL [action]; COMPLIANCE TEST: [named failure condition]") eliminates the partial-pass gray zone by making each entry a testable contract. The prior V-01 and V-02 approaches rely on the model interpreting descriptions; the SHALL approach forces binary compliance: either the named condition is present or a named test fails. If this is the mechanism that produced V-05's clean 22/22 in R10, applying it to R11's expanded denominator should reproduce the pattern. The base structure (standard section progression, inertia columns, split checklist) is unchanged.

---

You are a Dataverse security expert. Produce a complete permission trace for the feature described below.

**Feature**: {{topic}}
**Roles**: {{roles}} -- default: Customer Service Representative, Customer Service Manager, System Administrator

---

## PREAMBLE: SHALL-Condition Compliance Register

Every entry below is expressed as a SHALL condition paired with a named compliance test. If the output does not satisfy the SHALL condition, the named test FAILS. An auditor can verify compliance by running each test without re-reading the analysis.

| Criterion | SHALL Condition | COMPLIANCE TEST |
|-----------|----------------|-----------------|
| **C-18** Baseline Declaration | SHALL declare a zero-permission baseline state before Section 1 begins; all gaps SHALL be expressed as named departures from that baseline | COMPLIANCE TEST: if Section 0 is absent or the baseline sentence is missing, C-18 FAILS |
| **C-20** Sweep Binary Status | Each sweep vector SHALL carry an explicit CLEAN / FINDING PRESENT label as a discrete labeled field separate from narrative text | COMPLIANCE TEST: if any sweep vector's status can only be determined by parsing prose, C-20 FAILS |
| **C-21** Section Outcome Closure | Every named analysis section SHALL conclude with an explicit outcome: a named finding with role/mechanism/scope OR an explicit "no [X] found" with scope defined | COMPLIANCE TEST: if any section ends without an outcome statement, C-21 FAILS |
| **C-22** Terminal Checklist | Output SHALL include a terminal completion checklist that confirms all required STATUS markers are present; this checklist SHALL function as a standalone structural audit | COMPLIANCE TEST: if the checklist is absent or if structural incompleteness is only detectable by re-reading the full output, C-22 FAILS |
| **C-23** Inertia Default per Gap | For each identified gap, output SHALL name the specific organizational behavior that would leave that gap undiscovered without an explicit sweep | COMPLIANCE TEST: if any gap row lacks an Inertia Default cell, C-23 FAILS |
| **C-24** Sweep Execution Confirmation | Each sweep vector SHALL carry an execution-confirmation marker (Checked: Yes/No) that is orthogonal to the outcome status marker; these are two distinct fields | COMPLIANCE TEST: if any sweep vector has a single combined marker that collapses execution with outcome, C-24 FAILS |
| **C-25** Inertia Framing Cross-Section | Every section-level finding or clean-outcome statement SHALL include an explicit inertia note about what standard operational behavior produces or sustains that state | COMPLIANCE TEST: if any section-level closure statement lacks an inertia note, C-25 FAILS |
| **C-26** Anti-Pattern Preamble Register | Output SHALL open with a criterion-keyed preamble register table with "What SATISFIES" and "What Does NOT Satisfy" columns, covering C-24 and C-25 at minimum, appearing before any analysis section | COMPLIANCE TEST: if the register is absent, appears after Section 0, or lacks C-24/C-25 entries, C-26 FAILS |
| **C-27** Inertia Note Per-Row Column | Each structured table (role matrix, FLS table, transition delta table) SHALL contain a named "Inertia Note" column; every row SHALL carry its own annotation in that column | COMPLIANCE TEST: if any table lacks the named Inertia Note column or any row has a blank inertia cell, C-27 FAILS |
| **C-28** Terminal Checklist Split Rows | The terminal checklist SHALL contain separate rows for each sweep vector's execution marker and status marker as distinct items | COMPLIANCE TEST: if any sweep vector has a single combined checklist row, C-28 FAILS |
| **C-29** Three-Way Taxonomy | For each identified gap, the inertia failure mode SHALL be classified as exactly one of: (a) process absent / (b) process present but insufficient frequency / (c) process present but insufficient scope | COMPLIANCE TEST: if any gap's Failure Type does not use one of the three labeled taxonomy values, C-29 FAILS |
| **C-30** SHALL Conditions per Entry | The preamble register SHALL express each entry as a SHALL condition with a named compliance test | COMPLIANCE TEST: if any preamble entry is purely descriptive without a SHALL condition and a named test, C-30 FAILS |
| **C-31** Pre-Declared Identifiers | All structural element identifiers SHALL be declared before any analysis section begins: checklist row IDs, table column names, taxonomy condition labels | COMPLIANCE TEST: if any table column name or checklist row ID first appears mid-analysis without prior declaration, C-31 FAILS |
| **C-32** Top-Down Descent Ordering | Role analysis SHALL proceed SysAdmin -> Manager -> CSR; each non-maximum role section SHALL open with an explicit delta statement naming what the role above holds that this role does not | COMPLIANCE TEST: if any non-maximum role section lacks an opening delta statement, C-32 FAILS |

---

### Section 0: Baseline Zero-Point Declaration

Declare the zero-permission baseline state for {{topic}} before any role analysis begins.

> *"The baseline permission state for {{topic}} is: ___. Every finding below is a deviation from -- or failure to deviate from -- this state."*

**Inertia note** (C-25 SHALL): State what standard organizational behavior produces or sustains this baseline.

---

### Section 1: Role-Operation Matrix

Build the complete Role-Operation Matrix. Roles as columns. Operations as rows: Create, Read, Update, Delete, Assign, Share. Values: Allow / Deny / N/A+reason.

| Operation | Customer Service Rep | CS Manager | System Administrator | Inertia Note |
|-----------|---------------------|------------|---------------------|--------------|
| Create    |                     |            |                     |              |
| Read      |                     |            |                     |              |
| Update    |                     |            |                     |              |
| Delete    |                     |            |                     |              |
| Assign    |                     |            |                     |              |
| Share     |                     |            |                     |              |

**N/A rule** (C-15 SHALL): SHALL provide a parenthetical reason on the same line as any N/A cell. COMPLIANCE TEST: unexplained N/A is indistinguishable from omission and C-15 FAILS.
**Inertia Note column** (C-27 SHALL): For each row, state the organizational process that produces the current configuration. If no process enforces it, classify: (a) absent / (b) insufficient frequency / (c) insufficient scope.

For each role, state record access scope (Own/BU/Parent BU/Org) and scope grant source (Security Role/Team/Sharing Rule).

**Section closure** [S1-Close] (C-21 SHALL): SHALL state a named finding with role/mechanism/scope OR *"No role-operation misconfiguration identified in Section 1. [Inertia note: what process produces this state]."*
**Inertia note** (C-25 SHALL): SHALL include what standard operational behavior produces or sustains the role-operation configuration. COMPLIANCE TEST: absent inertia note at closure = C-25 FAILS for this section.

---

### Section 2: Field-Level Security

Build the FLS Table. Sensitive fields relevant to {{topic}} as rows. Roles as columns. Values: Allow / Deny / Not Configured.

| Field | Customer Service Rep | CS Manager | System Administrator | Inertia Note |
|-------|---------------------|------------|---------------------|--------------|
|       |                     |            |                     |              |

**Not Configured SHALL** (C-14): SHALL write "Not Configured" explicitly per cell -- do not omit rows. COMPLIANCE TEST: blank cell = C-14 FAILS.
**Inertia Note column** (C-27 SHALL): For each row, state what provisioning behavior sustains the Not Configured state.

**Section closure** [S2-Close] (C-21 SHALL): State a named FLS finding or *"No FLS misconfiguration identified. [Inertia note]."*

---

### Section 3: Role Transition Deltas

For each adjacent role pair, state what the higher role holds that the lower role does not.

| Transition | Operations Added | Scope Change | FLS Resolved | FLS Still Not Configured | Inertia Note |
|------------|-----------------|--------------|-------------|--------------------------|--------------|
| CSR -> Manager |            |              |             |                          |              |
| Manager -> SysAdmin |       |              |             |                          |              |

**Persistent FLS gap** (C-16 SHALL): SHALL explicitly label any field in "FLS Still Not Configured" across both rows as "Persistent FLS Gap." COMPLIANCE TEST: unlabeled persistent gap = C-16 FAILS.

**Section closure** [S3-Close]: State a named delta anomaly or *"No transition delta anomaly identified."*

---

### Section 4: Gap Registry

Name at least one concrete gap. All columns SHALL be populated per the SHALL conditions in the preamble register.

| Gap | Role | Field/Operation | Risk | Remediation | Inertia Default | Failure Type |
|-----|------|-----------------|------|-------------|-----------------|--------------|
| G-01 | | | High/Med/Low: [reason] | [specific config action] | [org behavior that would miss this] | (a)/(b)/(c) |

**Risk tier** (C-08 SHALL): SHALL provide a risk tier AND a one-line justification per entry. COMPLIANCE TEST: list of gaps without justification = C-08 FAILS.
**Remediation** (C-09 SHALL): SHALL name the specific configuration change required. COMPLIANCE TEST: generic advice without naming the target = C-09 FAILS.
**Inertia Default** (C-23 SHALL): SHALL name the organizational behavior that would miss this gap. COMPLIANCE TEST: absent = C-23 FAILS.
**Failure Type** (C-29 SHALL): SHALL classify using one of: (a) process absent / (b) process present but insufficient frequency / (c) process present but insufficient scope. COMPLIANCE TEST: any other label = C-29 FAILS.

---

### Section 5: Escalation Sweep

Address all three mechanism types (C-11 SHALL, C-17 SHALL).

**Mechanism A -- Record Reassignment**

- **Execution** (C-24 SHALL): Checked: Yes / No
- **Status** (C-20 SHALL): CLEAN / FINDING PRESENT
- **Inertia note** (C-25 SHALL): [process or behavior; classify (a)/(b)/(c)]
- If clean: *"No record reassignment escalation path identified. Scope: [define]."*

**Mechanism B -- Team Membership Addition**

- **Execution** (C-24 SHALL): Checked: Yes / No
- **Status** (C-20 SHALL): CLEAN / FINDING PRESENT
- **Inertia note** (C-25 SHALL): [process or behavior; classify (a)/(b)/(c)]
- If clean: *"No team membership escalation path identified. Teams examined: [define]."*

**Mechanism C -- Sharing Rule Exploitation**

- **Execution** (C-24 SHALL): Checked: Yes / No
- **Status** (C-20 SHALL): CLEAN / FINDING PRESENT
- **Inertia note** (C-25 SHALL): [process or behavior; classify (a)/(b)/(c)]
- If clean: *"No sharing rule escalation path identified. Rules examined: [define]."*

**Section closure** [S5-Close] (C-21 SHALL): State a named escalation finding or *"No escalation path identified across all three mechanism types."*

---

### Section 6: Team Membership Gap

- Status (C-20): CLEAN / FINDING PRESENT
- **Inertia note** (C-25 SHALL): [team-management behavior; classify (a)/(b)/(c)]
- If clean: *"No team membership gap identified. Teams examined: [define]."*

**Section closure** [S6-Close]: State the finding or explicit absence.

---

### Section 7: Sharing Rule Conflict

- Status (C-20): CLEAN / FINDING PRESENT
- **Inertia note** (C-25 SHALL): [sharing-rule governance behavior; classify (a)/(b)/(c)]
- If clean: *"No sharing rule conflict identified. Rules examined: [define]."*

**Section closure** [S7-Close]: State the finding or explicit absence.

---

### Section 8: Terminal Structural Completion Checklist

Confirm structural completeness. Each sweep vector has two separate rows (C-28 SHALL). COMPLIANCE TEST: single combined row = C-28 FAILS.

**Table and registry markers:**
- [ ] Role-Operation Matrix: complete
- [ ] FLS Table: complete
- [ ] Delta Table: complete
- [ ] Gap Registry: complete

**Sweep execution and status markers (split rows per C-28 SHALL):**
- [ ] Sweep A (Record Reassignment) -- Execution: Yes / No
- [ ] Sweep A (Record Reassignment) -- Status: CLEAN / FINDING PRESENT
- [ ] Sweep B (Team Membership Addition) -- Execution: Yes / No
- [ ] Sweep B (Team Membership Addition) -- Status: CLEAN / FINDING PRESENT
- [ ] Sweep C (Sharing Rule Exploitation) -- Execution: Yes / No
- [ ] Sweep C (Sharing Rule Exploitation) -- Status: CLEAN / FINDING PRESENT

**Section closure markers:**
- [ ] S1-Close: stated
- [ ] S2-Close: stated
- [ ] S3-Close: stated
- [ ] S5-Close: stated
- [ ] S6-Close: stated
- [ ] S7-Close: stated

**Inertia column markers (C-27 SHALL):**
- [ ] Role matrix "Inertia Note" column: present and every row populated
- [ ] FLS table "Inertia Note" column: present and every row populated
- [ ] Delta table "Inertia Note" column: present and every row populated

**Preamble register (C-26 SHALL, C-30 SHALL):**
- [ ] Anti-pattern / SHALL-condition register present before Section 0
- [ ] All entries expressed as SHALL condition + named COMPLIANCE TEST
- [ ] C-24, C-25 entries included

*"Structural completion verification complete. All SHALL conditions confirmed present. All STATUS markers verified."*

---

## V-04

**Variation axis**: Combined C-30 + C-31 (SHALL conditions + pre-declared identifiers)
**Hypothesis**: C-31 pre-declaration provides named slots; C-30 SHALL conditions provide testable contracts for those slots. The two mechanisms are mutually reinforcing: pre-declared identifiers without SHALL conditions can still produce partial passes (model names the right column but populates it partially); SHALL conditions without pre-declaration can still produce structural improvisation (model satisfies the contract but invents identifiers mid-analysis). Together, they should produce both a generative constraint (C-31: must populate declared slots) and a binary compliance test (C-30: either the slot is present or a named test fails). The descent ordering is present but not emphasized -- it is included as a structural requirement without being the primary axis.

---

You are a Dataverse security expert. Produce a complete permission trace for the feature described below.

**Feature**: {{topic}}
**Roles**: {{roles}} -- default: Customer Service Representative, Customer Service Manager, System Administrator

---

## PREAMBLE PART 1: Structural Element Registry

All structural element identifiers are declared here. Sections populate these named slots. An auditor verifies compliance by checking for identifier presence. Introducing a column name or checklist row ID for the first time mid-analysis is a C-31 failure.

**Declared Checklist Row IDs:**

| ID | Description |
|----|-------------|
| M-Complete | Role-Operation Matrix -- all cells populated, all N/A justified |
| F-Complete | FLS Table -- all cells explicit, all Not Configured rows present |
| D-Complete | Delta Table -- all adjacent pairs covered, persistent gaps labeled |
| G-Complete | Gap Registry -- at least one entry, all columns populated |
| SA-Exec | Sweep A (Record Reassignment) -- Execution: Yes/No |
| SA-Status | Sweep A (Record Reassignment) -- Status: CLEAN / FINDING PRESENT |
| SB-Exec | Sweep B (Team Membership Addition) -- Execution: Yes/No |
| SB-Status | Sweep B (Team Membership Addition) -- Status: CLEAN / FINDING PRESENT |
| SC-Exec | Sweep C (Sharing Rule Exploitation) -- Execution: Yes/No |
| SC-Status | Sweep C (Sharing Rule Exploitation) -- Status: CLEAN / FINDING PRESENT |
| S1-Close | Section 1 outcome closure |
| S2-Close | Section 2 outcome closure |
| S3-Close | Section 3 outcome closure |
| S5-Close | Section 5 outcome closure |
| S6-Close | Section 6 outcome closure |
| S7-Close | Section 7 outcome closure |

**Declared Table Column Names:**

| Table | Required Columns (in order) |
|-------|-----------------------------|
| Role-Operation Matrix | Operation \| [roles] \| Inertia Note |
| FLS Table | Field \| [roles] \| Inertia Note |
| Role-Transition Delta Table | Transition \| Operations Added \| Scope Change \| FLS Resolved \| FLS Still Not Configured \| Inertia Note |
| Gap Registry | Gap \| Role \| Field/Operation \| Risk \| Remediation \| Inertia Default \| Failure Type |

**Declared Taxonomy Condition Labels:**

| Label | Definition |
|-------|-----------|
| **(a) process absent** | No organizational process exists to detect this gap |
| **(b) process present but insufficient frequency** | A periodic review cycle exists but cadence would not catch intra-period changes |
| **(c) process present but insufficient scope/coverage** | A review process exists but excludes this specific vector or combination |

Failure Type column SHALL use exactly these three labels. Any other label is a C-29 failure.

---

## PREAMBLE PART 2: SHALL-Condition Compliance Register

Each entry is expressed as a SHALL condition + named compliance test. An output either satisfies the SHALL or fails the named test -- no partial verdicts.

| Criterion | SHALL Condition | COMPLIANCE TEST |
|-----------|----------------|-----------------|
| **C-15** N/A Justification | Output SHALL provide a parenthetical reason for every N/A cell on the same line as the N/A | COMPLIANCE TEST: any unexplained N/A cell = C-15 FAILS |
| **C-18** Baseline | Output SHALL declare a zero-permission baseline before Section 1; all gaps SHALL depart from this named zero-point | COMPLIANCE TEST: absent baseline sentence = C-18 FAILS |
| **C-20** Sweep Binary Status | Each sweep vector SHALL carry a discrete CLEAN / FINDING PRESENT label separate from any narrative | COMPLIANCE TEST: status determinable only by parsing prose = C-20 FAILS |
| **C-21** Section Closure | Every named analysis section SHALL end with an explicit outcome: named finding OR explicit "no [X] found" with scope | COMPLIANCE TEST: section ends with methodology description but no outcome statement = C-21 FAILS |
| **C-23** Inertia Default | Each gap row in the Gap Registry SHALL carry an Inertia Default cell naming the organizational behavior that would miss it | COMPLIANCE TEST: any gap row with a blank Inertia Default = C-23 FAILS |
| **C-24** Sweep Execution | Each sweep SHALL carry an execution-confirmation marker (Checked: Yes/No) orthogonal to the status marker | COMPLIANCE TEST: single combined marker conflating execution with outcome = C-24 FAILS |
| **C-25** Cross-Section Inertia | Every section-level closure statement SHALL include an inertia note about what standard operational behavior produces or sustains that state | COMPLIANCE TEST: any section-level closure without an inertia note = C-25 FAILS |
| **C-27** Inertia Note Column | Each table listed in the declared table column names SHALL contain a column named exactly "Inertia Note"; every row SHALL have a populated annotation in that column | COMPLIANCE TEST: table without declared "Inertia Note" column, or any blank inertia cell = C-27 FAILS |
| **C-28** Split Checklist Rows | Terminal checklist SHALL use declared split row IDs: SA-Exec and SA-Status as separate items, SB-Exec and SB-Status as separate items, SC-Exec and SC-Status as separate items | COMPLIANCE TEST: any sweep vector with a single combined checklist row not using declared split IDs = C-28 FAILS |
| **C-29** Three-Way Taxonomy | Every gap's Failure Type column SHALL contain exactly one declared label: (a)/(b)/(c) | COMPLIANCE TEST: any gap with an undeclared Failure Type label = C-29 FAILS |
| **C-30** SHALL Register | This preamble register SHALL express every entry as a SHALL condition with a named COMPLIANCE TEST | COMPLIANCE TEST: any descriptive-only entry without a SHALL condition and named test = C-30 FAILS |
| **C-31** Pre-Declared Identifiers | All checklist row IDs, table column names, and taxonomy labels SHALL be declared in Preamble Part 1 before any analysis section begins | COMPLIANCE TEST: any structural identifier appearing for the first time in an analysis section = C-31 FAILS |
| **C-32** Descent Ordering | Role analysis SHALL proceed SysAdmin -> Manager -> CSR in every section; each non-maximum role section SHALL open with a DELTA statement from the role above | COMPLIANCE TEST: any non-maximum role section without an opening DELTA statement = C-32 FAILS |

---

### Section 0: Baseline Zero-Point Declaration

> *"The baseline permission state for {{topic}} is: ___. Every finding below is a deviation from -- or failure to deviate from -- this state."*

**Inertia note**: [standard behavior producing this baseline; classify using declared taxonomy (a)/(b)/(c)]

---

### Section 1: Role-Operation Matrix

Using declared columns: Operation | Customer Service Rep | CS Manager | System Administrator | Inertia Note.

**Descent ordering** (C-32 SHALL):
- System Administrator section: present as first role column
- CS Manager section: open with DELTA from System Administrator
  > *"DELTA from System Administrator: CS Manager does NOT hold: [list]"*
- CS Representative section: open with DELTA from CS Manager
  > *"DELTA from CS Manager: CS Representative does NOT hold: [list]"*

| Operation | System Administrator | CS Manager | CS Representative | Inertia Note |
|-----------|---------------------|------------|-------------------|--------------|
| Create    |                     |            |                   |              |
| Read      |                     |            |                   |              |
| Update    |                     |            |                   |              |
| Delete    |                     |            |                   |              |
| Assign    |                     |            |                   |              |
| Share     |                     |            |                   |              |

For each role: Record access scope (Own/BU/Parent BU/Org) and scope grant source (Security Role/Team/Sharing Rule).

**Section closure** [S1-Close]: Named finding with role/mechanism/scope OR *"No role-operation misconfiguration in Section 1. Inertia: [state behavior; classify (a)/(b)/(c)]."*

---

### Section 2: Field-Level Security

Using declared columns: Field | System Administrator | CS Manager | CS Representative | Inertia Note.

| Field | System Administrator | CS Manager | CS Representative | Inertia Note |
|-------|---------------------|------------|-------------------|--------------|
|       |                     |            |                   |              |

**Section closure** [S2-Close]: Named FLS finding OR *"No FLS misconfiguration in Section 2. Inertia: [state behavior; classify (a)/(b)/(c)]."*

---

### Section 3: Role-Transition Delta Table

Using declared columns: Transition | Operations Added | Scope Change | FLS Resolved | FLS Still Not Configured | Inertia Note.

| Transition | Operations Added | Scope Change | FLS Resolved | FLS Still Not Configured | Inertia Note |
|------------|-----------------|--------------|-------------|--------------------------|--------------|
| SysAdmin -> Manager |        |              |             |                          |              |
| Manager -> CSR |             |              |             |                          |              |

Label any persistent FLS gap: *"Persistent FLS Gap -- not configured at any role level."*

**Section closure** [S3-Close]: Named delta anomaly OR *"No transition delta anomaly."*

---

### Section 4: Gap Registry

Using declared columns: Gap | Role | Field/Operation | Risk | Remediation | Inertia Default | Failure Type.

| Gap | Role | Field/Operation | Risk | Remediation | Inertia Default | Failure Type |
|-----|------|-----------------|------|-------------|-----------------|--------------|
| G-01 | | | High/Med/Low: [reason] | [specific config action] | [org behavior that would miss this] | (a)/(b)/(c) |

---

### Section 5: Escalation Sweep -- All Three Mechanism Types

**Mechanism A -- Record Reassignment**
- [SA-Exec] Execution: Checked: Yes / No
- [SA-Status] Status: CLEAN / FINDING PRESENT
- **Inertia note**: [behavior; classify (a)/(b)/(c)]
- If clean: *"No record reassignment escalation path. Scope: [define]."*

**Mechanism B -- Team Membership Addition**
- [SB-Exec] Execution: Checked: Yes / No
- [SB-Status] Status: CLEAN / FINDING PRESENT
- **Inertia note**: [behavior; classify (a)/(b)/(c)]
- If clean: *"No team membership escalation path. Teams: [define]."*

**Mechanism C -- Sharing Rule Exploitation**
- [SC-Exec] Execution: Checked: Yes / No
- [SC-Status] Status: CLEAN / FINDING PRESENT
- **Inertia note**: [behavior; classify (a)/(b)/(c)]
- If clean: *"No sharing rule escalation path. Rules: [define]."*

**Section closure** [S5-Close]: Named escalation finding OR *"No escalation path across all three mechanism types."*

---

### Section 6: Team Membership Gap

- Status: CLEAN / FINDING PRESENT
- **Inertia note**: [behavior; classify (a)/(b)/(c)]
- If clean: *"No team membership gap. Teams: [define]."*

**Section closure** [S6-Close]: Finding or explicit absence.

---

### Section 7: Sharing Rule Conflict

- Status: CLEAN / FINDING PRESENT
- **Inertia note**: [behavior; classify (a)/(b)/(c)]
- If clean: *"No sharing rule conflict. Rules: [define]."*

**Section closure** [S7-Close]: Finding or explicit absence.

---

### Section 8: Terminal Structural Completion Checklist

Using declared row IDs from the Structural Element Registry:

| Row ID | Item | Value |
|--------|------|-------|
| M-Complete | Role-Operation Matrix | Yes/No |
| F-Complete | FLS Table | Yes/No |
| D-Complete | Delta Table | Yes/No |
| G-Complete | Gap Registry | Yes/No |
| SA-Exec | Sweep A -- Execution | Yes/No |
| SA-Status | Sweep A -- Status | CLEAN / FINDING PRESENT |
| SB-Exec | Sweep B -- Execution | Yes/No |
| SB-Status | Sweep B -- Status | CLEAN / FINDING PRESENT |
| SC-Exec | Sweep C -- Execution | Yes/No |
| SC-Status | Sweep C -- Status | CLEAN / FINDING PRESENT |
| S1-Close | Section 1 closure | Present/Absent |
| S2-Close | Section 2 closure | Present/Absent |
| S3-Close | Section 3 closure | Present/Absent |
| S5-Close | Section 5 closure | Present/Absent |
| S6-Close | Section 6 closure | Present/Absent |
| S7-Close | Section 7 closure | Present/Absent |

**Inertia column audit** (C-27 SHALL):
- [ ] "Inertia Note" column present and populated in every row of Role-Operation Matrix
- [ ] "Inertia Note" column present and populated in every row of FLS Table
- [ ] "Inertia Note" column present and populated in every row of Delta Table

**Structural identifier audit** (C-31 SHALL):
- [ ] All declared row IDs appear in checklist above
- [ ] All declared column names appear in their respective tables
- [ ] All declared taxonomy labels (a)/(b)/(c) used in Failure Type and Inertia Note columns

**Descent ordering audit** (C-32 SHALL):
- [ ] Section 1: DELTA opener present before CS Manager analysis
- [ ] Section 1: DELTA opener present before CS Representative analysis

*"Structural completion verification complete. All SHALL conditions confirmed. All declared identifiers populated. All STATUS markers present."*

---

## V-05

**Variation axis**: Combined C-31 + C-32 + C-30 (triple integration -- full formal specification architecture)
**Hypothesis**: The combination that produced R10's winning V-05 (clean 22/22 aspirational without PARTIAL verdicts) can be replicated for the R11 denominator by making all three new axes mutually reinforcing structural constraints. C-32 (descent ordering) creates the section structure and causes C-10 delta tracking to be a byproduct of section headers. C-31 (pre-declared identifiers) names every slot within that section structure -- including the delta section headers themselves. C-30 (SHALL conditions) makes each declared slot a testable contract, not a guideline. The interaction is: C-32 defines the frame, C-31 populates the slot names within that frame, C-30 converts every slot into a binary pass/fail test. Any PARTIAL verdict becomes impossible when the condition is a named SHALL and the compliance test names the exact failure.

---

You are a Dataverse security expert. Produce a complete permission trace for the feature described below.

**Feature**: {{topic}}
**Roles in descent order**: {{roles}} -- default: System Administrator (maximum), Customer Service Manager, Customer Service Representative (minimum)

**FORMAL SPECIFICATION RULE**: This analysis operates under a formal specification. All structural element identifiers are declared before analysis begins. All requirements are expressed as SHALL conditions with named compliance tests. Role analysis proceeds top-down: System Administrator first, then each subsequent role opens with an explicit delta statement from the role above. Any section that violates a declared SHALL condition fails the named test; the failure is detectable from the structural audit alone without re-reading prose.

---

## SPECIFICATION PART 1: Structural Element Registry

All concrete structural identifiers used in this output are declared here before any analysis section begins. C-31: introducing an identifier for the first time mid-analysis is a structural failure.

### 1.1 Checklist Row IDs (terminal checklist, Section 8)

| Row ID | Full Description | Section |
|--------|-----------------|---------|
| M-Complete | Role-Operation Matrix -- all cells present, all N/A justified | Section 1 |
| F-Complete | FLS Table -- all cells explicit, all Not Configured written | Section 2 |
| D-Complete | Role-Transition Delta Table -- all adjacent pairs, persistent gaps labeled | Section 3 |
| G-Complete | Gap Registry -- at least one entry, all columns populated | Section 4 |
| SA-Exec | Sweep A (Record Reassignment) -- Execution: Yes/No | Section 5 |
| SA-Status | Sweep A (Record Reassignment) -- Status: CLEAN / FINDING PRESENT | Section 5 |
| SB-Exec | Sweep B (Team Membership Addition) -- Execution: Yes/No | Section 5 |
| SB-Status | Sweep B (Team Membership Addition) -- Status: CLEAN / FINDING PRESENT | Section 5 |
| SC-Exec | Sweep C (Sharing Rule Exploitation) -- Execution: Yes/No | Section 5 |
| SC-Status | Sweep C (Sharing Rule Exploitation) -- Status: CLEAN / FINDING PRESENT | Section 5 |
| S1-Close | Section 1 outcome closure statement | Section 1 |
| S2-Close | Section 2 outcome closure statement | Section 2 |
| S3-Close | Section 3 outcome closure statement | Section 3 |
| S5-Close | Section 5 outcome closure statement | Section 5 |
| S6-Close | Section 6 outcome closure statement | Section 6 |
| S7-Close | Section 7 outcome closure statement | Section 7 |

### 1.2 Table Column Names

| Table Name | Declared Columns (in order) |
|------------|-----------------------------|
| Role-Operation Matrix | Operation \| System Administrator \| CS Manager \| CS Representative \| Inertia Note |
| FLS Table | Field \| System Administrator \| CS Manager \| CS Representative \| Inertia Note |
| Role-Transition Delta Table | Transition \| Operations Added \| Scope Change \| FLS Resolved \| FLS Still Not Configured \| Inertia Note |
| Gap Registry | Gap \| Role \| Field/Operation \| Risk \| Remediation \| Inertia Default \| Failure Type |

Column names in analysis sections SHALL match these declared names exactly. Any deviation is a C-31 failure.

### 1.3 Taxonomy Condition Labels

The only valid labels for Failure Type (Gap Registry) and inertia classification anywhere in the output:

| Label | Meaning |
|-------|---------|
| **(a) process absent** | No organizational process exists to detect this gap |
| **(b) process present but insufficient frequency** | Review cycle exists but cadence does not catch intra-period changes |
| **(c) process present but insufficient scope/coverage** | Review process exists but excludes this specific vector or combination |

### 1.4 Descent Section Identifiers

Top-down role analysis uses these section opener patterns:

| Section | Opener Format |
|---------|---------------|
| System Administrator | [Present capabilities and scope directly -- this is the maximum-privilege reference point] |
| CS Manager | DELTA from System Administrator: CS Manager does NOT hold: [list]. Capabilities: [then proceed] |
| CS Representative | DELTA from CS Manager: CS Representative does NOT hold: [list]. Capabilities: [then proceed] |

These opener formats are declared identifiers. Non-maximum role sections SHALL begin with the declared DELTA opener before presenting capabilities.

---

## SPECIFICATION PART 2: SHALL-Condition Compliance Register

Each entry is expressed as a SHALL condition + named compliance test. Binary verdict: either the condition is present or the named test FAILS. No partial verdicts.

| Criterion | SHALL Condition | COMPLIANCE TEST |
|-----------|----------------|-----------------|
| **C-14** Not Configured | Output SHALL write "Not Configured" for every field/role combination with no FLS; SHALL NOT omit rows or leave blank cells | COMPLIANCE TEST: any blank FLS cell or omitted field/role row = C-14 FAILS |
| **C-15** N/A Justification | Every N/A cell SHALL carry a parenthetical reason on the same line | COMPLIANCE TEST: any unexplained N/A = C-15 FAILS |
| **C-16** Persistent FLS Gap | Any field appearing in "FLS Still Not Configured" across all transition rows SHALL be labeled "Persistent FLS Gap" | COMPLIANCE TEST: unlabeled persistent gap in Delta Table = C-16 FAILS |
| **C-18** Baseline | Output SHALL open with a baseline zero-permission declaration before Section 1; all gaps SHALL depart from this named zero-point | COMPLIANCE TEST: absent baseline sentence = C-18 FAILS |
| **C-20** Sweep Binary Status | Each sweep vector SHALL carry a discrete CLEAN / FINDING PRESENT label as a standalone field, not embedded in prose | COMPLIANCE TEST: status determinable only by parsing prose = C-20 FAILS |
| **C-21** Section Closure | Every named analysis section SHALL conclude with an explicit outcome: named finding with role/mechanism/scope OR explicit "no [X] found" with scope | COMPLIANCE TEST: section ends with methodology description or finding summary without explicit outcome statement = C-21 FAILS |
| **C-22** Terminal Checklist | Output SHALL include a terminal checklist that confirms all STATUS markers using declared row IDs; structural incompleteness SHALL be detectable from checklist alone | COMPLIANCE TEST: absent checklist, or checklist not using declared row IDs = C-22 FAILS |
| **C-23** Inertia Default | Each gap in the Gap Registry SHALL carry an Inertia Default cell naming the specific organizational behavior that would miss the gap | COMPLIANCE TEST: any gap row with empty or generic Inertia Default = C-23 FAILS |
| **C-24** Sweep Execution | Each sweep vector SHALL carry an execution-confirmation marker (SA-Exec, SB-Exec, SC-Exec from the registry) orthogonal to the status marker (SA-Status, SB-Status, SC-Status) | COMPLIANCE TEST: any sweep with a single combined execution+status marker = C-24 FAILS |
| **C-25** Cross-Section Inertia | Every section-level closure statement SHALL include an inertia note using a declared taxonomy label (a)/(b)/(c) | COMPLIANCE TEST: any section-level closure without an inertia note = C-25 FAILS |
| **C-26** Anti-Pattern Register | Output SHALL include a criterion-keyed register with SHALL conditions and compliance tests before Section 0; SHALL cover C-24 and C-25 at minimum | COMPLIANCE TEST: absent register, or register appearing after Section 0 = C-26 FAILS |
| **C-27** Inertia Note Column | Each declared table (Role-Operation Matrix, FLS Table, Delta Table) SHALL contain a column named exactly "Inertia Note"; every row SHALL have a populated annotation | COMPLIANCE TEST: any declared table without "Inertia Note" column, or any row with blank Inertia Note = C-27 FAILS |
| **C-28** Split Checklist Rows | Terminal checklist SHALL use declared split row IDs; SA-Exec and SA-Status SHALL be separate rows; same for SB and SC pairs | COMPLIANCE TEST: any sweep with combined single row = C-28 FAILS |
| **C-29** Three-Way Taxonomy | Every gap's Failure Type column SHALL use exactly one declared label from 1.3: (a)/(b)/(c) | COMPLIANCE TEST: any Failure Type cell using an undeclared label = C-29 FAILS |
| **C-30** SHALL Register | Every entry in this register SHALL be expressed as a SHALL condition with a named COMPLIANCE TEST | COMPLIANCE TEST: any descriptive-only entry without SHALL condition and named test = C-30 FAILS |
| **C-31** Pre-Declared Identifiers | All table column names, checklist row IDs, and taxonomy labels SHALL be declared in Specification Part 1 before any analysis section begins | COMPLIANCE TEST: any structural identifier appearing for the first time in an analysis section = C-31 FAILS |
| **C-32** Descent Ordering | Role analysis SHALL proceed System Administrator -> CS Manager -> CS Representative; each non-maximum role section SHALL begin with the declared DELTA opener from Section 1.4 | COMPLIANCE TEST: any non-maximum role section without a declared DELTA opener = C-32 FAILS |

---

### Section 0: Baseline Zero-Point Declaration

> *"The baseline permission state for {{topic}} is: ___. Every finding below is a deviation from -- or failure to deviate from -- this state."*

**Inertia note**: [standard organizational behavior producing this baseline; classify using declared label: (a)/(b)/(c)]

---

### Section 1: Role-Operation Matrix

Using declared table columns: Operation | System Administrator | CS Manager | CS Representative | Inertia Note.

**System Administrator** (maximum privilege -- no delta opener needed):

| Operation | System Administrator | CS Manager | CS Representative | Inertia Note |
|-----------|---------------------|------------|-------------------|--------------|
| Create    |                     |            |                   |              |
| Read      |                     |            |                   |              |
| Update    |                     |            |                   |              |
| Delete    |                     |            |                   |              |
| Assign    |                     |            |                   |              |
| Share     |                     |            |                   |              |

**CS Manager column** SHALL open with declared DELTA opener:
> *"DELTA from System Administrator: CS Manager does NOT hold: [specific operations/scope items from the table above that SysAdmin holds]"*

**CS Representative column** SHALL open with declared DELTA opener:
> *"DELTA from CS Manager: CS Representative does NOT hold: [specific operations/scope items from the table above that Manager holds]"*

For each role, state: Record access scope (Own/BU/Parent BU/Org) and scope grant source (Security Role/Team/Sharing Rule).

**Inertia Note column**: For each operation row, state the organizational process producing the current configuration. Classify using declared label (a)/(b)/(c) if no enforcing process.

**Section closure** [S1-Close] (SHALL): Named finding with role/mechanism/scope OR *"No role-operation misconfiguration in Section 1. Inertia: [behavior; label (a)/(b)/(c)]."*

---

### Section 2: Field-Level Security

Using declared table columns: Field | System Administrator | CS Manager | CS Representative | Inertia Note.

**CS Manager column** SHALL open with declared DELTA opener at the FLS level:
> *"DELTA from System Administrator (FLS): CS Manager does NOT have configured FLS for: [field list] compared to SysAdmin"*

**CS Representative column** SHALL open with declared DELTA opener:
> *"DELTA from CS Manager (FLS): CS Representative does NOT have configured FLS for: [field list] compared to Manager"*

| Field | System Administrator | CS Manager | CS Representative | Inertia Note |
|-------|---------------------|------------|-------------------|--------------|
|       |                     |            |                   |              |

**Section closure** [S2-Close] (SHALL): Named FLS finding OR *"No FLS misconfiguration in Section 2. Inertia: [behavior; label (a)/(b)/(c)]."*

---

### Section 3: Role-Transition Delta Table

Using declared table columns: Transition | Operations Added | Scope Change | FLS Resolved | FLS Still Not Configured | Inertia Note.

| Transition | Operations Added | Scope Change | FLS Resolved | FLS Still Not Configured | Inertia Note |
|------------|-----------------|--------------|-------------|--------------------------|--------------|
| SysAdmin -> Manager |        |              |             |                          |              |
| Manager -> CSR      |        |              |             |                          |              |

Any field in "FLS Still Not Configured" across both rows SHALL be labeled: *"Persistent FLS Gap -- not configured at any role level."*

**Section closure** [S3-Close] (SHALL): Named delta anomaly OR *"No transition delta anomaly."*

---

### Section 4: Gap Registry

Using declared table columns: Gap | Role | Field/Operation | Risk | Remediation | Inertia Default | Failure Type.

| Gap | Role | Field/Operation | Risk | Remediation | Inertia Default | Failure Type |
|-----|------|-----------------|------|-------------|-----------------|--------------|
| G-01 | | | High/Med/Low: [one-line reason] | [specific configuration change] | [org behavior that would miss this without explicit sweep] | (a)/(b)/(c) |

---

### Section 5: Escalation Sweep -- All Three Mechanism Types

**Mechanism A -- Record Reassignment**
Can a lower-privilege user reassign a record to gain scope beyond their role?

- [SA-Exec] Execution (C-24): Checked: Yes / No
- [SA-Status] Status (C-20): CLEAN / FINDING PRESENT
- **Inertia note** (C-25): [behavior; classify (a)/(b)/(c)]
- Negative confirmation (C-13): If clean: *"No record reassignment escalation path. Scope examined: [define]."*

**Mechanism B -- Team Membership Addition**
Does adding a user to any team grant scope exceeding their security role?

- [SB-Exec] Execution (C-24): Checked: Yes / No
- [SB-Status] Status (C-20): CLEAN / FINDING PRESENT
- **Inertia note** (C-25): [behavior; classify (a)/(b)/(c)]
- Negative confirmation (C-13): If clean: *"No team membership escalation path. Teams examined: [define]."*

**Mechanism C -- Sharing Rule Exploitation**
Does any sharing rule widen access beyond the security role baseline?

- [SC-Exec] Execution (C-24): Checked: Yes / No
- [SC-Status] Status (C-20): CLEAN / FINDING PRESENT
- **Inertia note** (C-25): [behavior; classify (a)/(b)/(c)]
- Negative confirmation (C-13): If clean: *"No sharing rule escalation path. Rules examined: [define]."*

**Section closure** [S5-Close] (SHALL): Named escalation finding OR *"No escalation path identified across all three mechanism types."*

---

### Section 6: Team Membership Gap

- Status (C-20): CLEAN / FINDING PRESENT
- **Inertia note** (C-25): [team roster management behavior; classify (a)/(b)/(c)]
- Negative confirmation (C-13): If clean: *"No team membership gap. Teams examined: [define]."*

**Section closure** [S6-Close] (SHALL): Finding or explicit absence.

---

### Section 7: Sharing Rule Conflict

- Status (C-20): CLEAN / FINDING PRESENT
- **Inertia note** (C-25): [sharing-rule governance behavior; classify (a)/(b)/(c)]
- Negative confirmation (C-13): If clean: *"No sharing rule conflict. Rules examined: [define]."*

**Section closure** [S7-Close] (SHALL): Finding or explicit absence.

---

### Section 8: Terminal Structural Completion Checklist

Using declared row IDs from Specification Part 1.1. Every row ID declared in 1.1 SHALL appear in this checklist. C-28: SA-Exec and SA-Status are separate rows; same for SB and SC pairs.

| Row ID | Item | Value |
|--------|------|-------|
| M-Complete | Role-Operation Matrix -- all cells, all N/A justified | Yes / No |
| F-Complete | FLS Table -- all Not Configured explicit, no blank cells | Yes / No |
| D-Complete | Delta Table -- all pairs, persistent gaps labeled | Yes / No |
| G-Complete | Gap Registry -- at least one entry, all columns | Yes / No |
| SA-Exec | Sweep A (Record Reassignment) -- Execution | Yes / No |
| SA-Status | Sweep A (Record Reassignment) -- Status | CLEAN / FINDING PRESENT |
| SB-Exec | Sweep B (Team Membership Addition) -- Execution | Yes / No |
| SB-Status | Sweep B (Team Membership Addition) -- Status | CLEAN / FINDING PRESENT |
| SC-Exec | Sweep C (Sharing Rule Exploitation) -- Execution | Yes / No |
| SC-Status | Sweep C (Sharing Rule Exploitation) -- Status | CLEAN / FINDING PRESENT |
| S1-Close | Section 1 outcome closure | Present / Absent |
| S2-Close | Section 2 outcome closure | Present / Absent |
| S3-Close | Section 3 outcome closure | Present / Absent |
| S5-Close | Section 5 outcome closure | Present / Absent |
| S6-Close | Section 6 outcome closure | Present / Absent |
| S7-Close | Section 7 outcome closure | Present / Absent |

**Inertia column audit** -- C-27 SHALL (verify declared column "Inertia Note" present in all three declared tables):
- [ ] Role-Operation Matrix "Inertia Note" column: present and every row populated
- [ ] FLS Table "Inertia Note" column: present and every row populated
- [ ] Role-Transition Delta Table "Inertia Note" column: present and every row populated

**Structural identifier audit** -- C-31 SHALL (verify no identifier introduced mid-analysis):
- [ ] All checklist row IDs from 1.1 appear in checklist above using declared IDs
- [ ] All table column names from 1.2 appear in their respective tables using declared names
- [ ] All taxonomy labels from 1.3 used in Failure Type column and inertia notes

**Descent ordering audit** -- C-32 SHALL (verify declared DELTA openers present):
- [ ] Section 1: DELTA opener present before CS Manager analysis (declared format from 1.4)
- [ ] Section 1: DELTA opener present before CS Representative analysis (declared format from 1.4)
- [ ] Section 2: FLS DELTA opener present before CS Manager column
- [ ] Section 2: FLS DELTA opener present before CS Representative column

**SHALL register audit** -- C-30 SHALL (verify compliance register present and formatted):
- [ ] Specification Part 2 register present before Section 0
- [ ] All entries expressed as SHALL condition + named COMPLIANCE TEST
- [ ] C-24 and C-25 entries included

*"Structural completion verification complete. All declared row IDs populated. All SHALL conditions confirmed. All STATUS markers verified. Descent ordering confirmed via declared DELTA openers. Structural identifier audit complete -- no mid-analysis identifier introductions detected."*
