# trace-permissions — Round 10 Variations

**Rubric version**: v9 (29 criteria — C-26/C-27/C-28/C-29 added from R9 excellence signals V-01)
**Round**: 10
**Date**: 2026-03-15
**Axes explored**: C-26 preamble register as primary structure (single), C-27 per-row inertia column (single), C-28 split-row terminal checklist (single), C-29 three-way taxonomy + inertia framing cross-section (combo), All four new criteria + formal specification register (combo)

**Scoring formula change from R9**: Aspirational denominator is now 22 (not 18). Max aspirational = (pass_count / 22) × 10. Each passed aspirational criterion is worth ~0.455 pts.

---

## V-01

**Variation axis**: C-26 preamble register as primary structure
**Hypothesis**: R9-V-01 produced C-26 by opening with a mandatory preamble table before analysis. This variation makes the preamble register the organizing axis: the prompt opens with an explicit criterion-keyed anti-pattern register (covering C-24, C-25, C-27, C-28, C-29 at minimum) and every downstream section references back to the register by criterion ID. The preamble both primes the output against its own failure modes and demonstrates C-19 at scale — rather than naming anti-patterns ad hoc in instruction blocks, they are pre-compiled into a navigable register. The base structure (standard section progression) is unchanged so no other axis contaminates the signal.

---

You are a Dataverse security expert. Produce a complete permission trace for the feature described below.

**Feature**: {{topic}}
**Roles**: {{roles}} — default: Customer Service Representative, Customer Service Manager, System Administrator

---

## PREAMBLE: Anti-Pattern Register

Before analysis begins, this register states what satisfies and what does NOT satisfy the structural criteria that most commonly produce incomplete outputs. Every section in this prompt references criteria by ID. Use this register to verify compliance before submitting.

| Criterion | What SATISFIES | What Does NOT Satisfy |
|-----------|---------------|----------------------|
| **C-24** Sweep Vector Execution Confirmation | Each sweep vector carries two orthogonal markers: Execution (Checked: Yes/No) AND Status (CLEAN / FINDING PRESENT) as separate labeled fields | A single combined marker such as "Sweep A: CLEAN" — this collapses execution confirmation with outcome, making it impossible to distinguish "sweep ran and found nothing" from "sweep was skipped" |
| **C-25** Inertia Framing as Cross-Section Lens | Every section-level finding or clean-outcome statement includes an explicit note about what standard operational behavior produces or sustains that state | Inertia framing that appears only in the gap registry — absent from the role-matrix section, FLS table, and sweep conclusions |
| **C-27** Inertia Note as Per-Row Mandatory Column | Each structured table (role matrix, FLS table, role-transition delta table) includes a named "Inertia Note" column; every row carries its own annotation in that column | Section-level inertia narrative appearing above or below a table but not instantiated as a named column within the table |
| **C-28** Terminal Checklist Split Rows | Terminal checklist contains separate rows: "Sweep A — Execution: Yes/No" and "Sweep A — Status: CLEAN / FINDING PRESENT" as distinct checklist items | A checklist with a single combined row per sweep vector such as "Sweep A: Checked, CLEAN" |
| **C-29** Three-Way Inertia Taxonomy | Each gap's default trust failure mode is labeled as one of: (a) process absent / (b) process present but insufficient frequency / (c) process present but insufficient scope | Naming the organizational behavior that would miss a gap ("quarterly reviews skip this") without classifying which failure type it represents |
| **C-18** Baseline Declaration | Zero-permission baseline declared before any role enumeration; all gaps expressed as named departures from that baseline | Beginning directly with "Customer Service Representative can Create..." without establishing the zero-point from which gaps are measured |
| **C-20** Sweep Vector Binary Status | Each sweep vector carries an explicit CLEAN / FINDING PRESENT label as a discrete labeled element separate from narrative | Embedding status only within prose sentences where a reader must parse text to infer completeness |

---

### Section 0: Baseline Zero-Point Declaration

Declare the permission state that exists before any role is assigned:

- Default record operations for any authenticated user on this entity type
- FLS configured by default on sensitive fields (typically: none)
- Sharing rules active by default
- Teams configured by default

Write a baseline sentence:
> *"The baseline permission state for {{topic}} is: ___. Every finding below is a deviation from — or failure to deviate from — this state."*

This is the anchor for C-18. All gaps in subsequent sections are departures from this named baseline, not observations in isolation.

---

### Section 1: Role-Operation Matrix

Build the complete role-operation matrix. Every role as a column. Every operation as a row: Create, Read, Update, Delete, Assign, Share. Values: Allow / Deny / N/A+reason. No blank cells.

| Operation | [Role 1] | [Role 2] | [Role 3] | Inertia Note |
|-----------|----------|----------|----------|--------------|
| Create    |          |          |          |              |
| Read      |          |          |          |              |
| Update    |          |          |          |              |
| Delete    |          |          |          |              |
| Assign    |          |          |          |              |
| Share     |          |          |          |              |

**Inertia Note column** (C-27): For each row, state what standard operational behavior — periodic audits, standing role assignments, annual provisioning reviews — produces or sustains the current permission configuration across all roles in that row.

For each role also include:
- **Record access scope**: Own / Business Unit / Parent BU / Organization
- **Scope grant source**: Security Role / Team Membership / Sharing Rule (C-12)

**N/A rule** (C-15): Any N/A cell must carry a parenthetical reason on the same line.

Section closure (C-21): After the matrix, state either a named finding with role/mechanism/scope or: *"No role-operation misconfiguration identified in Section 1."*

Inertia note for section closure (C-25): State what standard operational behavior produces or sustains the current role-operation configuration.

---

### Section 2: Field-Level Security

For each sensitive field relevant to {{topic}}, state FLS per role: Allow / Deny / Not Configured. No blank cells.

| Field   | [Role 1] | [Role 2] | [Role 3] | Inertia Note |
|---------|----------|----------|----------|--------------|
| [field] |          |          |          |              |

**Not Configured is a finding** (C-14): Write "Not Configured" where FLS is absent — do not omit the row or leave the cell blank. Not Configured is not the same as blank.

**Inertia Note column** (C-27): For each field row, state what standard organizational behavior (e.g., default profile inheritance, provisioning tooling that does not configure FLS columns) sustains the Not Configured state without a specific sweep.

Section closure (C-21): State either a named FLS finding with role and field or: *"No FLS misconfiguration identified in Section 2."*

Inertia note for section closure (C-25): State what standard operational behavior produces or sustains the current FLS configuration.

---

### Section 3: Role Transition Deltas

For each adjacent role pair, state exactly what the higher role has that the lower role does not.

| Transition          | Operations Added | Scope Change | FLS Resolved | FLS Still Not Configured | Inertia Note |
|---------------------|-----------------|--------------|-------------|--------------------------|--------------|
| [Role 1] → [Role 2] |                 |              |             |                          |              |
| [Role 2] → [Role 3] |                 |              |             |                          |              |

**Inertia Note column** (C-27): For each transition row, state what provisioning or role-management process would or would not surface the specific delta at that boundary.

**Persistent FLS gap tracking** (C-16): List any field appearing in "FLS Still Not Configured" at every transition. Label: *"Persistent FLS Gap — not configured at any role level."*

Section closure (C-21): State either a named delta finding or: *"No transition delta anomaly identified in Section 3."*

---

### Section 4: Named Security Gap

Before the sweep, name at least one concrete security misconfiguration (C-04). State: role, field or operation, specific problem, risk tier (C-08), remediation action (C-09), and default trust failure mode with three-way classification (C-29).

Gap registry entry format:

| Gap | Role | Field/Operation | Risk | Remediation | Inertia Default | Failure Type |
|-----|------|-----------------|------|-------------|-----------------|--------------|
| [G-01] | | | High/Med/Low | [specific action] | [org behavior that would miss this] | (a) absent / (b) insufficient frequency / (c) insufficient scope |

**Failure Type** (C-29): Classify the inertia default into one of: (a) process absent — no organizational process exists to detect this gap; (b) process present but insufficient frequency — a review cycle exists but cadence would not catch intra-period changes; (c) process present but insufficient scope — a review process exists but excludes this specific vector or combination.

---

### Section 5: Escalation Sweep — All Three Mechanism Types

Check all three escalation vectors. Address each regardless of whether it yields a finding (C-11, C-17).

**Mechanism A — Record Reassignment**
Can a lower-privilege user reassign a record to gain scope their role does not allow? State: who → via what action → resulting scope.

- **Execution** (C-24): Checked: Yes / No
- **Status** (C-20): CLEAN / FINDING PRESENT
- **Inertia note** (C-25): [what standard operational behavior sustains or would miss this path]
- If no path: *"No record reassignment escalation path identified."*

**Mechanism B — Team Membership Addition**
Does adding a user to any team grant scope exceeding their security role?

- **Execution** (C-24): Checked: Yes / No
- **Status** (C-20): CLEAN / FINDING PRESENT
- **Inertia note** (C-25): [what standard operational behavior sustains or would miss this path]
- If no path: *"No team membership escalation path identified."*

**Mechanism C — Sharing Rule Exploitation**
Does any sharing rule widen access beyond the security role baseline?

- **Execution** (C-24): Checked: Yes / No
- **Status** (C-20): CLEAN / FINDING PRESENT
- **Inertia note** (C-25): [what standard operational behavior sustains or would miss this path]
- If no path: *"No sharing rule escalation path identified."*

Section closure (C-21): State either a named escalation finding or: *"No escalation path identified across all three mechanism types."*

---

### Section 6: Team Membership Gap

Identify at least one team membership anomaly (C-07). Name the team, the user or role scenario, and the resulting delta.

- **Status** (C-20): CLEAN / FINDING PRESENT
- **Inertia note** (C-25): [what team-management behavior sustains or would miss this gap]
- If none: *"No team membership gap identified for {{topic}}."*

If gap found, add to gap registry in Section 4 with Failure Type classification (C-29).

Section closure (C-21): State the finding or explicit absence.

---

### Section 7: Sharing Rule Conflict

Identify at least one sharing rule that widens access beyond baseline or creates a contradiction (C-06).

- **Status** (C-20): CLEAN / FINDING PRESENT
- **Inertia note** (C-25): [what sharing-rule governance process sustains or would miss this conflict]
- If none: *"No sharing rule conflict identified for {{topic}}."*

Section closure (C-21): State the finding or explicit absence.

---

### Section 8: Terminal Structural Completion Checklist

Confirm structural completeness. Each sweep vector has two separate checklist rows (C-28).

**Matrix and table markers:**
- [ ] Section 1 Role-Operation Matrix: complete (no blank cells, all N/A rows justified)
- [ ] Section 2 FLS Table: complete (all Not Configured cells explicit, no blanks)
- [ ] Section 3 Transition Delta Table: complete (persistent FLS gaps identified)
- [ ] Section 4 Gap Registry: at least one entry, all columns populated, Failure Type classified

**Sweep execution and status markers (C-28 split rows):**
- [ ] Sweep A (Record Reassignment) — Execution: Yes / No
- [ ] Sweep A (Record Reassignment) — Status: CLEAN / FINDING PRESENT
- [ ] Sweep B (Team Membership) — Execution: Yes / No
- [ ] Sweep B (Team Membership) — Status: CLEAN / FINDING PRESENT
- [ ] Sweep C (Sharing Rule) — Execution: Yes / No
- [ ] Sweep C (Sharing Rule) — Status: CLEAN / FINDING PRESENT

**Section closure markers:**
- [ ] Section 1 closure: finding or explicit "no misconfiguration" stated
- [ ] Section 2 closure: finding or explicit "no FLS misconfiguration" stated
- [ ] Section 3 closure: finding or explicit "no delta anomaly" stated
- [ ] Section 5 closure: finding or explicit "no escalation path" stated
- [ ] Section 6 closure: finding or explicit "no team gap" stated
- [ ] Section 7 closure: finding or explicit "no sharing rule conflict" stated

**Inertia column markers (C-27):**
- [ ] Role matrix Inertia Note column: present and populated in every row
- [ ] FLS table Inertia Note column: present and populated in every row
- [ ] Transition delta Inertia Note column: present and populated in every row

**Preamble register:**
- [ ] Anti-pattern register present before Section 0
- [ ] C-24, C-25, C-27, C-28, C-29 entries included in register

*"Structural completion verification complete. All STATUS markers confirmed present."*

---

## V-02

**Variation axis**: C-27 per-row inertia column as primary structure
**Hypothesis**: R9-V-01 demonstrated that inertia framing as a column in tables makes C-25 verifiable per row without parsing prose. This variation makes the per-row inertia column the organizing principle: the prompt explicitly frames every table as having a mandatory Inertia Note column, defines the column semantics at the start of each table instruction, and treats a missing or empty inertia column as a structural failure equivalent to a blank N/A cell. The role sequence is standard (CSR → Manager → SysAdmin) so no other axis contaminates the signal. The goal is to determine whether explicit per-row column enforcement produces richer inertia framing than section-level prompting.

---

You are a Dataverse security expert. Produce a complete permission trace for the feature described below. Every structured table in your output must include an Inertia Note column. This column is mandatory in the same sense that a role column is mandatory — a table without it is structurally incomplete.

**Feature**: {{topic}}
**Roles**: {{roles}} — default: Customer Service Representative, Customer Service Manager, System Administrator

**Inertia Note column semantics**: For each row, state the specific organizational behavior — a process, a schedule, an assumption — that currently produces or sustains the row's permission configuration. If no active process enforces the configuration, state which type of inertia applies: (a) no process exists / (b) a periodic process exists but cadence is insufficient / (c) a process exists but excludes this scope.

---

### Step 0: Baseline

Declare the baseline zero-permission state before any role analysis:
- Default operations for an authenticated user with no role on this entity type
- FLS state by default on sensitive fields
- Default sharing rules
- Default team configuration

> *"Baseline for {{topic}}: ___. All findings are deviations from or failures to deviate from this state."*

---

### Step 1: Role-Operation Matrix

| Operation | Customer Service Rep | CS Manager | System Admin | Inertia Note |
|-----------|---------------------|------------|--------------|--------------|
| Create    |                     |            |              |              |
| Read      |                     |            |              |              |
| Update    |                     |            |              |              |
| Delete    |                     |            |              |              |
| Assign    |                     |            |              |              |
| Share     |                     |            |              |              |

**Inertia Note column**: For each operation row, state what provisioning process or organizational schedule currently produces the Allow/Deny state across all roles in that row. If no process enforces this, classify: (a) absent / (b) insufficient frequency / (c) insufficient scope.

**Column rules**: Values are Allow / Deny / N/A+reason. The Inertia Note column is not optional — a row with a blank inertia cell is structurally the same as a row with a blank operation cell.

For each role:
- Record access scope: Own / BU / Parent BU / Org
- Scope grant source: Security Role / Team Membership / Sharing Rule

Section outcome: Named finding with role/mechanism/scope OR *"No role-operation misconfiguration. Standard provisioning process produces current state: ___."*

---

### Step 2: Field-Level Security

| Field   | Customer Service Rep | CS Manager | System Admin | Inertia Note |
|---------|---------------------|------------|--------------|--------------|
| [field] |                     |            |              |              |

**Inertia Note column**: For each field row, state what organizational behavior sustains the current FLS state across all roles. Not Configured rows require a specific note: which type of inertia leaves this field unconfigured — (a) no FLS review process / (b) annual FLS review but field was added post-cycle / (c) FLS review exists but does not cover this entity type.

**Not Configured rule**: Write "Not Configured" in every cell where FLS is absent. Blank and Not Configured are not the same. Not Configured is a finding.

Section outcome: Named finding OR *"No FLS misconfiguration. Inertia note: ___."*

---

### Step 3: Role Transition Deltas

| Transition          | Ops Added | Scope Change | FLS Resolved | FLS Still Not Configured | Inertia Note |
|---------------------|-----------|--------------|-------------|--------------------------|--------------|
| CSR → CS Manager    |           |              |             |                          |              |
| CS Manager → SysAdmin|          |              |             |                          |              |

**Inertia Note column**: For each transition row, state what provisioning or access-review process would or would not surface the specific delta at that boundary. If the delta would be missed by a standard periodic review, classify: (a) absent / (b) insufficient frequency / (c) insufficient scope.

**Persistent FLS gaps**: List fields appearing in "FLS Still Not Configured" at every transition. Label: *"Persistent FLS Gap."*

Section outcome: Named delta anomaly OR *"No transition delta anomaly. Inertia note: ___."*

---

### Step 4: Gap Registry

Name at least one concrete gap before the sweep.

| Gap   | Role | Field/Operation | Risk | Remediation | Inertia Default | Failure Type |
|-------|------|-----------------|------|-------------|-----------------|--------------|
| G-01  |      |                 | H/M/L |            |                 | (a)/(b)/(c)  |

**Inertia Default**: The specific organizational behavior that would leave this gap undiscovered without an explicit sweep.
**Failure Type**: (a) process absent / (b) insufficient frequency / (c) insufficient scope.

---

### Step 5: Escalation Sweep

Address all three mechanism types regardless of findings. For each:
- **Execution**: Checked: Yes / No
- **Status**: CLEAN / FINDING PRESENT
- **Inertia note**: What standard process would or would not surface this vector

**Mechanism A — Record Reassignment**
Who → via what action → resulting scope.
Execution: __ / Status: __ / Inertia note: __
If none: *"No record reassignment escalation path identified."*

**Mechanism B — Team Membership Addition**
Team → users → access beyond role baseline.
Execution: __ / Status: __ / Inertia note: __
If none: *"No team membership escalation path identified."*

**Mechanism C — Sharing Rule Exploitation**
Rule → role affected → effective scope delta.
Execution: __ / Status: __ / Inertia note: __
If none: *"No sharing rule escalation path identified."*

Section outcome: Named finding OR *"No escalation path identified. All three mechanism types confirmed checked."*

---

### Step 6: Team Membership Gap

Name at least one team anomaly: team → user scenario → scope delta. If none: *"No team membership gap identified."*

Status: CLEAN / FINDING PRESENT
Inertia note: What team roster or membership review process would or would not surface this.
Section outcome: Finding or explicit absence.

---

### Step 7: Sharing Rule Conflict

Name at least one sharing rule that widens access or creates contradiction. If none: *"No sharing rule conflict identified."*

Status: CLEAN / FINDING PRESENT
Inertia note: What sharing rule governance process would or would not surface this.
Section outcome: Finding or explicit absence.

---

### Step 8: Terminal Completion Checklist

**Table completeness:**
- [ ] Role matrix: Inertia Note column present and all rows populated
- [ ] FLS table: Inertia Note column present and all rows populated
- [ ] Transition delta table: Inertia Note column present and all rows populated

**Sweep markers (split rows per C-28):**
- [ ] Sweep A (Record Reassignment) — Execution: Yes / No
- [ ] Sweep A (Record Reassignment) — Status: CLEAN / FINDING PRESENT
- [ ] Sweep B (Team Membership) — Execution: Yes / No
- [ ] Sweep B (Team Membership) — Status: CLEAN / FINDING PRESENT
- [ ] Sweep C (Sharing Rule) — Execution: Yes / No
- [ ] Sweep C (Sharing Rule) — Status: CLEAN / FINDING PRESENT

**Section closures:**
- [ ] Sections 1-7 each conclude with an explicit outcome statement
- [ ] Gap registry: at least one entry with Failure Type classified

*"Structural completion verified. Inertia Note column present in all structured tables."*

---

## V-03

**Variation axis**: C-28 split-row terminal checklist as primary structure
**Hypothesis**: C-28 requires separate rows for Execution and Status per sweep vector in the terminal checklist. This variation makes the checklist structure the organizing axis: the terminal section is designed first and back-referenced throughout the prompt, so every sweep instruction explicitly tells the model which checklist rows it will produce. The base structure remains standard (section progression, standard role sequence) and phrasing is neutral. The goal is to determine whether prompting toward a specific terminal checklist shape — defined at the top of the prompt as the output contract — produces consistent C-24 compliance (orthogonal execution/outcome markers) without requiring per-section instruction.

---

You are a Dataverse security expert. Produce a complete permission trace for the feature described below.

**Feature**: {{topic}}
**Roles**: {{roles}} — default: Customer Service Representative, Customer Service Manager, System Administrator

**Output contract**: Your output closes with Section 8, a structural completion checklist. That checklist contains specific rows listed below. Every section in this prompt produces data that populates one or more rows of Section 8. Build your analysis so Section 8 can be filled truthfully.

**Section 8 preview — rows you will fill:**

| Row ID | Checklist Item | Value |
|--------|---------------|-------|
| S1-complete | Section 1 Role Matrix: all cells filled, N/A rows justified | Yes / No |
| S2-complete | Section 2 FLS Table: no blank cells, Not Configured explicit | Yes / No |
| S3-complete | Section 3 Transition Deltas: persistent gaps identified | Yes / No |
| S4-complete | Section 4 Gap Registry: ≥1 gap, all columns populated, Failure Type classified | Yes / No |
| SA-exec | Sweep A (Record Reassignment) — Execution | Yes / No |
| SA-status | Sweep A (Record Reassignment) — Status | CLEAN / FINDING PRESENT |
| SB-exec | Sweep B (Team Membership) — Execution | Yes / No |
| SB-status | Sweep B (Team Membership) — Status | CLEAN / FINDING PRESENT |
| SC-exec | Sweep C (Sharing Rule) — Execution | Yes / No |
| SC-status | Sweep C (Sharing Rule) — Status | CLEAN / FINDING PRESENT |
| S5-closure | Section 5 outcome stated | Yes / No |
| S6-closure | Section 6 outcome stated | Yes / No |
| S7-closure | Section 7 outcome stated | Yes / No |
| inertia-s1 | Section 1 inertia note present at section closure | Yes / No |
| inertia-s2 | Section 2 inertia note present at section closure | Yes / No |
| inertia-s5 | Section 5 inertia notes present per mechanism | Yes / No |

Note on SA-exec vs SA-status: these are two different questions. SA-exec = "did I run this sweep?" SA-status = "what did I find?" A sweep can be Executed:Yes and Status:CLEAN. It cannot be Executed:No and Status:CLEAN — that would mean the sweep was skipped, not that it was clean. Keep these rows separate.

---

### Section 0: Baseline

Declare the baseline zero-permission state before role analysis. → Populates baseline-declared marker.

> *"Baseline for {{topic}}: ___. All findings are deviations from or failures to deviate from this state."*

---

### Section 1: Role-Operation Matrix

Build the complete matrix. → Populates S1-complete and inertia-s1.

| Operation | [Role 1] | [Role 2] | [Role 3] | Inertia Note |
|-----------|----------|----------|----------|--------------|
| Create    |          |          |          |              |
| Read      |          |          |          |              |
| Update    |          |          |          |              |
| Delete    |          |          |          |              |
| Assign    |          |          |          |              |
| Share     |          |          |          |              |

Values: Allow / Deny / N/A+reason. Inertia Note: what standard process produces/sustains each row's configuration.
Record access scope and scope grant source per role.

Section closure for S1-complete: State named finding or *"No role-operation misconfiguration."* State inertia note for inertia-s1.

---

### Section 2: Field-Level Security

Build the FLS table. → Populates S2-complete and inertia-s2.

| Field   | [Role 1] | [Role 2] | [Role 3] | Inertia Note |
|---------|----------|----------|----------|--------------|
| [field] |          |          |          |              |

Not Configured is a finding — not a blank cell. Inertia Note: what organizational behavior sustains Not Configured status.

Section closure for S2-complete: Finding or *"No FLS misconfiguration."* Inertia note for inertia-s2.

---

### Section 3: Role Transition Deltas

Build the delta table. → Populates S3-complete.

| Transition           | Ops Added | Scope Change | FLS Resolved | FLS Not Configured | Inertia Note |
|----------------------|-----------|--------------|-------------|--------------------|--------------|
| [Role 1] → [Role 2]  |           |              |             |                    |              |
| [Role 2] → [Role 3]  |           |              |             |                    |              |

Persistent FLS gaps: list fields Not Configured at every transition. Label: *"Persistent FLS Gap."*

Section closure for S3-complete: Named delta anomaly or *"No delta anomaly."*

---

### Section 4: Gap Registry

Name at least one gap. → Populates S4-complete.

| Gap  | Role | Field/Operation | Risk | Remediation | Inertia Default | Failure Type |
|------|------|-----------------|------|-------------|-----------------|--------------|
| G-01 |      |                 | H/M/L |            |                 | (a)/(b)/(c)  |

Failure Type: (a) no process / (b) insufficient frequency / (c) insufficient scope. This classification is required per gap — a named default without a failure-type label does not pass S4-complete.

---

### Section 5: Escalation Sweep

Run all three mechanisms. → Populates SA-exec, SA-status, SB-exec, SB-status, SC-exec, SC-status, S5-closure, inertia-s5.

**Mechanism A — Record Reassignment**
Analysis: [who → action → scope]
Inertia note: [process that would/would not surface this]
→ **SA-exec**: Checked: Yes / No
→ **SA-status**: CLEAN / FINDING PRESENT
If none found: *"No record reassignment escalation path identified."*

**Mechanism B — Team Membership Addition**
Analysis: [team → users → scope delta]
Inertia note: [process that would/would not surface this]
→ **SB-exec**: Checked: Yes / No
→ **SB-status**: CLEAN / FINDING PRESENT
If none found: *"No team membership escalation path identified."*

**Mechanism C — Sharing Rule Exploitation**
Analysis: [rule → role → scope delta]
Inertia note: [process that would/would not surface this]
→ **SC-exec**: Checked: Yes / No
→ **SC-status**: CLEAN / FINDING PRESENT
If none found: *"No sharing rule escalation path identified."*

Section closure for S5-closure: Named finding or *"No escalation paths identified. All three mechanism types confirmed checked."*

---

### Section 6: Team Membership Gap

Analysis: name team anomaly or confirm absence. → Populates S6-closure.
Status: CLEAN / FINDING PRESENT
Inertia note: What roster review would/would not surface this.
Section closure for S6-closure: Finding or *"No team membership gap identified."*

---

### Section 7: Sharing Rule Conflict

Analysis: name conflict or confirm absence. → Populates S7-closure.
Status: CLEAN / FINDING PRESENT
Inertia note: What governance process would/would not surface this.
Section closure for S7-closure: Finding or *"No sharing rule conflict identified."*

---

### Section 8: Terminal Structural Completion Checklist

Fill each row from the output contract defined at the top of this prompt. Execution and Status rows are always separate — do not combine them.

| Row ID | Checklist Item | Value |
|--------|---------------|-------|
| S1-complete | Role Matrix: all cells filled, N/A justified | |
| S2-complete | FLS Table: no blanks, Not Configured explicit | |
| S3-complete | Transition Deltas: persistent gaps identified | |
| S4-complete | Gap Registry: ≥1 gap, Failure Type classified | |
| SA-exec | Sweep A — Execution | |
| SA-status | Sweep A — Status | |
| SB-exec | Sweep B — Execution | |
| SB-status | Sweep B — Status | |
| SC-exec | Sweep C — Execution | |
| SC-status | Sweep C — Status | |
| S5-closure | Section 5 outcome stated | |
| S6-closure | Section 6 outcome stated | |
| S7-closure | Section 7 outcome stated | |
| inertia-s1 | Section 1 inertia note at closure | |
| inertia-s2 | Section 2 inertia note at closure | |
| inertia-s5 | Section 5 inertia notes per mechanism | |

*"Structural completion verified."*

---

## V-04

**Variation axis**: C-29 three-way taxonomy as primary + inertia framing cross-section lens (combo)
**Hypothesis**: C-29 classifies inertia defaults into (a) process absent / (b) insufficient frequency / (c) insufficient scope. This combo variation makes the taxonomy the primary analytical lens: every section's closure explicitly classifies its inertia type, and the gap registry uses the taxonomy as a first-class column. The combo with C-25 cross-section inertia framing means every major section (not just the gap registry) applies the taxonomy — readers can verify classification coverage without reading the gap registry alone. The phrasing register is formal-technical to match C-29's classification vocabulary. Role sequence is bottom-up (CSR first) to test whether taxonomy framing holds when the lowest-privilege role anchors the analysis.

---

You are a Dataverse security expert. Produce a complete permission trace for the feature described below. Each major analysis section concludes with an inertia classification: identify the organizational process failure type that sustains the current state or would leave a gap undiscovered. Use the three-way taxonomy: (a) process absent — no organizational process exists / (b) process present, insufficient frequency — review cadence would not catch intra-period changes / (c) process present, insufficient scope — review excludes this specific vector or combination.

**Feature**: {{topic}}
**Roles**: {{roles}} — default: Customer Service Representative (lowest privilege), Customer Service Manager, System Administrator (highest privilege); analyze in this sequence

---

### Section 0: Baseline and Taxonomy Introduction

Declare the baseline zero-permission state. Identify what type of process failure would leave the baseline unconfigured or unexamined.

> *"Baseline for {{topic}}: ___. Inertia type for baseline examination: (a/b/c) — ___."*

---

### Section 1: Role-Operation Matrix (CSR first)

Construct the role-operation matrix starting with the lowest-privilege role. For each role, work upward.

| Operation | CSR   | CS Manager | System Admin | Inertia Note | Failure Type |
|-----------|-------|------------|--------------|--------------|--------------|
| Create    |       |            |              |              | (a)/(b)/(c)  |
| Read      |       |            |              |              | (a)/(b)/(c)  |
| Update    |       |            |              |              | (a)/(b)/(c)  |
| Delete    |       |            |              |              | (a)/(b)/(c)  |
| Assign    |       |            |              |              | (a)/(b)/(c)  |
| Share     |       |            |              |              | (a)/(b)/(c)  |

Values: Allow / Deny / N/A+reason.
Inertia Note: specific organizational behavior that produces current configuration.
Failure Type: taxonomy classification for the inertia note in that row.

Record access scope and scope grant source per role.

Section closure: Named finding or *"No role-operation misconfiguration."*
Section inertia closure: *"Section 1 inertia classification: (a/b/c) — [the specific process failure or absence that would leave a role-operation gap undiscovered in normal operations]."*

---

### Section 2: Field-Level Security

| Field   | CSR   | CS Manager | System Admin | Inertia Note | Failure Type |
|---------|-------|------------|--------------|--------------|--------------|
| [field] |       |            |              |              | (a)/(b)/(c)  |

Not Configured is a finding — write it explicitly in the cell.
Failure Type per field row: classify what process failure leaves this field unconfigured.

Section closure: Finding or *"No FLS misconfiguration."*
Section inertia closure: *"Section 2 inertia classification: (a/b/c) — ___."*

---

### Section 3: Role Transition Deltas (CSR → Manager → SysAdmin)

| Transition        | Ops Added | Scope Change | FLS Resolved | FLS Not Configured | Inertia Note | Failure Type |
|-------------------|-----------|--------------|-------------|--------------------|--------------|--------------|
| CSR → CS Manager  |           |              |             |                    |              | (a)/(b)/(c)  |
| CS Manager → SysAdmin |       |              |             |                    |              | (a)/(b)/(c)  |

Persistent FLS gaps: fields Not Configured at every transition. Classify the failure type for each persistent gap.

Section closure: Named delta anomaly or *"No delta anomaly."*
Section inertia closure: *"Section 3 inertia classification: (a/b/c) — ___."*

---

### Section 4: Gap Registry

| Gap  | Role | Field/Operation | Risk | Remediation | Inertia Default | Failure Type |
|------|------|-----------------|------|-------------|-----------------|--------------|
| G-01 |      |                 | H/M/L |            |                 | (a)/(b)/(c)  |

**Failure Type** is required per gap. A gap with an Inertia Default but no Failure Type classification is incomplete. The three types:
- **(a) process absent**: No organizational process would ever surface this gap without an explicit targeted sweep
- **(b) insufficient frequency**: A review process exists (e.g., quarterly access review) but its cadence would miss intra-period changes
- **(c) insufficient scope**: A review process exists but excludes this specific entity, field, or mechanism combination

---

### Section 5: Escalation Sweep

All three mechanism types. Each carries execution confirmation, status, inertia note, and taxonomy classification.

**Mechanism A — Record Reassignment**
Analysis: [who → action → resulting scope]
Inertia note: [organizational process that would/would not surface this]
Failure type: (a)/(b)/(c)
Execution: Checked: Yes / No
Status: CLEAN / FINDING PRESENT
If none: *"No record reassignment escalation path identified."*

**Mechanism B — Team Membership Addition**
Analysis: [team → users → scope delta]
Inertia note: [organizational process that would/would not surface this]
Failure type: (a)/(b)/(c)
Execution: Checked: Yes / No
Status: CLEAN / FINDING PRESENT
If none: *"No team membership escalation path identified."*

**Mechanism C — Sharing Rule Exploitation**
Analysis: [rule → role → effective access delta]
Inertia note: [organizational process that would/would not surface this]
Failure type: (a)/(b)/(c)
Execution: Checked: Yes / No
Status: CLEAN / FINDING PRESENT
If none: *"No sharing rule escalation path identified."*

Section closure: Named finding or *"No escalation paths identified. All three mechanism types confirmed checked."*
Section inertia closure: *"Section 5 inertia classification: dominant failure type (a/b/c) — ___."*

---

### Section 6: Team Membership Gap

Name anomaly or confirm absence.
Status: CLEAN / FINDING PRESENT
Inertia note: Process that would/would not surface this
Failure type: (a)/(b)/(c)
Section closure: Finding or *"No team membership gap identified."*

---

### Section 7: Sharing Rule Conflict

Name conflict or confirm absence.
Status: CLEAN / FINDING PRESENT
Inertia note: Governance process that would/would not surface this
Failure type: (a)/(b)/(c)
Section closure: Finding or *"No sharing rule conflict identified."*

---

### Section 8: Terminal Structural Completion Checklist

**Section completeness:**
- [ ] Section 1 matrix: all cells filled, N/A justified
- [ ] Section 2 FLS table: Not Configured explicit, no blanks
- [ ] Section 3 deltas: persistent gaps identified
- [ ] Section 4 gap registry: ≥1 entry, Failure Type classified per gap

**Sweep execution and status (split rows):**
- [ ] Sweep A — Execution: Yes / No
- [ ] Sweep A — Status: CLEAN / FINDING PRESENT
- [ ] Sweep B — Execution: Yes / No
- [ ] Sweep B — Status: CLEAN / FINDING PRESENT
- [ ] Sweep C — Execution: Yes / No
- [ ] Sweep C — Status: CLEAN / FINDING PRESENT

**Taxonomy coverage:**
- [ ] Sections 1-7 each conclude with an inertia closure statement
- [ ] Failure Type column present in role matrix, FLS table, delta table
- [ ] All gap registry entries carry Failure Type classification

*"Structural completion verified. Taxonomy classification present at all required locations."*

---

## V-05

**Variation axis**: All four new criteria (C-26/C-27/C-28/C-29) combined with formal specification register phrasing
**Hypothesis**: R9-V-01 produced all four new criteria from a single structural innovation. This variation tests whether a formal specification register phrasing style — using "SHALL" requirements, numbered compliance tests, and explicit pass/fail conditions in each section heading — can implement all four criteria simultaneously without requiring per-instruction anti-pattern reminders. The spec register style naturally produces: (1) a requirement catalogue that becomes the preamble register (C-26); (2) table columns defined as formal requirements (C-27); (3) checklist rows specified as distinct line items in the spec (C-28); (4) taxonomy labels required by the spec alongside each inertia claim (C-29). The role sequence is top-down (SysAdmin baseline then restricted downward) to test whether a descending decomposition changes inertia framing density.

---

You are a Dataverse security expert. This prompt is written as a formal specification. Every section begins with a SHALL statement that defines the minimum structural requirement. Produce a complete permission trace for the feature described below that satisfies all SHALL requirements.

**Feature**: {{topic}}
**Roles**: {{roles}} — default: System Administrator (baseline), Customer Service Manager, Customer Service Representative (most restricted); analyze in descending order

---

## SPECIFICATION PREAMBLE: Criterion Compliance Register

The following register defines compliance requirements for structural criteria. This register SHALL appear before analysis begins. Sections referencing these criteria by ID inherit these definitions.

| Criterion | SHALL satisfy | SHALL NOT satisfy |
|-----------|--------------|-------------------|
| **C-24** | Each sweep vector SHALL carry two separate markers: Execution (Checked: Yes/No) and Status (CLEAN/FINDING PRESENT) as independent fields; they answer different questions | A single marker ("Sweep A: CLEAN") that collapses execution confirmation with outcome; if the sweep was not run the marker cannot exist, but it also cannot confirm execution occurred |
| **C-25** | Every section-level finding or clean-outcome statement SHALL include an explicit inertia note naming the organizational behavior that produces or sustains that state | Inertia framing confined to the gap registry section alone; each major section SHALL have its own inertia closure statement |
| **C-27** | Each structured table SHALL include a named Inertia Note column; every row SHALL carry an annotation in that column | Section-level inertia narrative above/below a table that is not instantiated as a column within it; a column that exists in the header but has empty cells in data rows |
| **C-28** | The terminal checklist SHALL contain separate line items for each sweep vector's Execution marker and Status marker | A single combined checklist row per sweep vector; the row "Sweep A: Checked, CLEAN" does not satisfy this requirement |
| **C-29** | Each gap's inertia default SHALL be classified as: (a) process absent / (b) process present, insufficient frequency / (c) process present, insufficient scope | Naming an organizational default behavior without assigning a failure-type label; "quarterly reviews would miss this" without classifying it as type (b) does not satisfy this requirement |
| **C-18** | Output SHALL declare a zero-permission baseline before role enumeration begins | Beginning role analysis without a declared baseline; analysis anchored to "typical Dataverse defaults" without explicit declaration does not satisfy this requirement |
| **C-20** | Each sweep vector SHALL carry a binary CLEAN/FINDING PRESENT label as a discrete labeled element | Sweep outcome embedded only in narrative prose; a reader SHALL be able to verify all sweep statuses without parsing prose |

---

## SECTION 0: Baseline Declaration

**SHALL**: Declare the baseline zero-permission state before any role analysis. All findings SHALL be expressed as named departures from this baseline.

| Dimension | Default State |
|-----------|--------------|
| Default record operations (authenticated, no role) | |
| FLS configured by default on sensitive fields | |
| Sharing rules active by default | |
| Teams configured by default | |

Baseline declaration sentence (SHALL be written before proceeding to Section 1):
> *"Baseline for {{topic}}: ___. Every finding below is a deviation from or failure to deviate from this state."*

---

## SECTION 1: Role-Operation Matrix

**SHALL**: Map every named role to every operation. Table SHALL include an Inertia Note column and a Failure Type column. No blank cells permitted.

| Operation | SysAdmin | CS Manager | CSR | Inertia Note | Failure Type |
|-----------|----------|------------|-----|--------------|--------------|
| Create    |          |            |     |              | (a)/(b)/(c)  |
| Read      |          |            |     |              | (a)/(b)/(c)  |
| Update    |          |            |     |              | (a)/(b)/(c)  |
| Delete    |          |            |     |              | (a)/(b)/(c)  |
| Assign    |          |            |     |              | (a)/(b)/(c)  |
| Share     |          |            |     |              | (a)/(b)/(c)  |

Compliance tests:
- CT-1.1: Every cell is Allow / Deny / N/A+reason — no blanks
- CT-1.2: Inertia Note column present and populated in every row (C-27)
- CT-1.3: Failure Type column present with (a)/(b)/(c) classification per row (C-29)
- CT-1.4: N/A cells carry one-line reason on same line (C-15)

Record access scope per role: Own / BU / Parent BU / Org
Scope grant source per role: Security Role / Team / Sharing Rule (C-12)

**Section closure (C-21)**: Named finding with role/mechanism/scope OR *"No role-operation misconfiguration identified."*
**Section inertia closure (C-25)**: *"Section 1 inertia: ___. Failure type: (a/b/c)."*

---

## SECTION 2: Field-Level Security

**SHALL**: For each sensitive field, state FLS per role. Table SHALL include Inertia Note and Failure Type columns. Not Configured SHALL appear explicitly — blank cells are not permitted.

| Field   | SysAdmin | CS Manager | CSR | Inertia Note | Failure Type |
|---------|----------|------------|-----|--------------|--------------|
| [field] |          |            |     |              | (a)/(b)/(c)  |

Compliance tests:
- CT-2.1: Values are Allow / Deny / Not Configured — no blank cells
- CT-2.2: "Not Configured" is a finding, not an omission (C-14)
- CT-2.3: Inertia Note column present and populated (C-27)
- CT-2.4: Failure Type column present with classification (C-29)

**Section closure (C-21)**: Named FLS finding OR *"No FLS misconfiguration identified."*
**Section inertia closure (C-25)**: *"Section 2 inertia: ___. Failure type: (a/b/c)."*

---

## SECTION 3: Role Transition Deltas

**SHALL**: For each adjacent role pair in descending order, state the operations/scope/FLS that the higher role holds that the lower does not. Table SHALL include Inertia Note and Failure Type columns.

| Transition              | Ops Removed | Scope Narrowed | FLS Restrictions Added | FLS Still Not Configured | Inertia Note | Failure Type |
|-------------------------|-------------|----------------|----------------------|--------------------------|--------------|--------------|
| SysAdmin → CS Manager   |             |                |                      |                          |              | (a)/(b)/(c)  |
| CS Manager → CSR        |             |                |                      |                          |              | (a)/(b)/(c)  |

Persistent FLS gaps: fields in "FLS Still Not Configured" at every transition → label *"Persistent FLS Gap."* Classify Failure Type per persistent gap.

**Section closure (C-21)**: Named delta anomaly OR *"No transition delta anomaly identified."*
**Section inertia closure (C-25)**: *"Section 3 inertia: ___. Failure type: (a/b/c)."*

---

## SECTION 4: Gap Registry

**SHALL**: Name at least one concrete security gap. Each entry SHALL carry risk tier, remediation, inertia default, and Failure Type classification.

| Gap  | Role | Field/Op | Risk | Remediation | Inertia Default | Failure Type |
|------|------|----------|------|-------------|-----------------|--------------|
| G-01 |      |          | H/M/L |            |                 | (a)/(b)/(c)  |

Compliance tests:
- CT-4.1: ≥1 gap present (C-04)
- CT-4.2: Risk tier assigned per gap with justification (C-08)
- CT-4.3: Remediation names specific role/field/action — not generic advice (C-09)
- CT-4.4: Inertia Default names specific organizational behavior (C-23)
- CT-4.5: Failure Type classified as (a)/(b)/(c) — not optional (C-29)

---

## SECTION 5: Escalation Sweep

**SHALL**: Check all three mechanism types. Each SHALL produce four discrete outputs: analysis, inertia note with failure type, execution confirmation (C-24), and status marker (C-20).

**Mechanism A — Record Reassignment**
Analysis: [who → action → resulting scope]
Inertia note: [organizational behavior that would miss this] / Failure type: (a)/(b)/(c)
- **Execution (C-24)**: Checked: Yes / No
- **Status (C-20)**: CLEAN / FINDING PRESENT
If none: *"No record reassignment escalation path identified."*

**Mechanism B — Team Membership Addition**
Analysis: [team → users → scope delta]
Inertia note: [organizational behavior that would miss this] / Failure type: (a)/(b)/(c)
- **Execution (C-24)**: Checked: Yes / No
- **Status (C-20)**: CLEAN / FINDING PRESENT
If none: *"No team membership escalation path identified."*

**Mechanism C — Sharing Rule Exploitation**
Analysis: [rule → role → effective access delta]
Inertia note: [organizational behavior that would miss this] / Failure type: (a)/(b)/(c)
- **Execution (C-24)**: Checked: Yes / No
- **Status (C-20)**: CLEAN / FINDING PRESENT
If none: *"No sharing rule escalation path identified."*

**Section closure (C-21)**: Named finding OR *"No escalation paths identified across all three mechanism types."*
**Section inertia closure (C-25)**: *"Section 5 dominant inertia type: (a/b/c) — ___."*

---

## SECTION 6: Team Membership Gap

**SHALL**: Name at least one team anomaly or provide explicit no-finding statement with scope examined.
- Status (C-20): CLEAN / FINDING PRESENT
- Inertia note + Failure type: ___  / (a)/(b)/(c)
**Section closure (C-21)**: Finding or *"No team membership gap identified. Scope examined: ___."*

---

## SECTION 7: Sharing Rule Conflict

**SHALL**: Name at least one conflict or provide explicit no-finding statement with scope examined.
- Status (C-20): CLEAN / FINDING PRESENT
- Inertia note + Failure type: ___ / (a)/(b)/(c)
**Section closure (C-21)**: Finding or *"No sharing rule conflict identified. Scope examined: ___."*

---

## SECTION 8: Terminal Structural Compliance Checklist

**SHALL**: Confirm every compliance test defined in the specification. Execution and Status checklist rows SHALL be separate line items (C-28).

**Specification preamble:**
- [ ] Anti-pattern register present before Section 0 (C-26)
- [ ] C-24, C-25, C-27, C-28, C-29 entries in register (C-26)

**Table structural requirements (C-27):**
- [ ] Section 1 Inertia Note column: present and all rows populated
- [ ] Section 1 Failure Type column: present and all rows classified
- [ ] Section 2 Inertia Note column: present and all rows populated
- [ ] Section 2 Failure Type column: present and all rows classified
- [ ] Section 3 Inertia Note column: present and all rows populated
- [ ] Section 3 Failure Type column: present and all rows classified

**Sweep markers — separate rows per C-28:**
- [ ] Sweep A (Record Reassignment) — Execution: Yes / No
- [ ] Sweep A (Record Reassignment) — Status: CLEAN / FINDING PRESENT
- [ ] Sweep B (Team Membership Addition) — Execution: Yes / No
- [ ] Sweep B (Team Membership Addition) — Status: CLEAN / FINDING PRESENT
- [ ] Sweep C (Sharing Rule Exploitation) — Execution: Yes / No
- [ ] Sweep C (Sharing Rule Exploitation) — Status: CLEAN / FINDING PRESENT

**Section closures (C-21):**
- [ ] Section 1: outcome stated
- [ ] Section 2: outcome stated
- [ ] Section 3: outcome stated
- [ ] Section 5: outcome stated
- [ ] Section 6: outcome stated (with scope)
- [ ] Section 7: outcome stated (with scope)

**Inertia closure statements (C-25):**
- [ ] Section 1 inertia closure with failure type
- [ ] Section 2 inertia closure with failure type
- [ ] Section 3 inertia closure with failure type
- [ ] Section 5 inertia closure with failure type

**Gap registry (C-29):**
- [ ] ≥1 gap present with Failure Type classified

*"Specification compliance verified. All SHALL requirements confirmed."*
