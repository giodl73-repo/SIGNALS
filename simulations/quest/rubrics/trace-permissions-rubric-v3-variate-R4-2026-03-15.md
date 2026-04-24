# trace-permissions — Round 4 Variations

**Rubric version**: v3 (16 criteria — C-14/C-15/C-16 added from R3 excellence signals)
**Round**: 4
**Date**: 2026-03-15
**Axes explored**: Output format / C-14 isolation (single), Role sequence / C-16 isolation (single), Lifecycle emphasis / C-15 isolation (single), Role sequence + Output format / C-16+C-14 combo, Full triple / C-14+C-15+C-16 combo

**Scoring formula from rubric v3**: Aspirational denominator is 8. Max aspirational = (pass_count / 8) × 10. Each passed aspirational criterion is worth 1.25 pts.

**New criteria targeted this round**:
- C-14: Criterion-owner attribution in terminal checklist — each item names the accountable expert role
- C-15: Multi-mechanism criterion enforcement (triple-lock) — each essential criterion co-enforced by format schema + role sub-section + SHALL obligation simultaneously
- C-16: Dedicated format-compliance auditor role (CA) — third role whose mandate is output structural integrity, not security analysis

---

## V-01

**Variation axis**: Output format — criterion-owner attribution in terminal checklist (C-14)
**Hypothesis**: Rubric v3 adds C-14 (criterion-owner attribution). The proven R3 base (SE+CS personas, pre-printed tables, SHALL contracts, terminal checklist) already satisfies C-11/C-12/C-13. The minimal intervention for C-14 is one new column in the terminal checklist mapping each SHALL item to the accountable expert role. This is a single-column change to one table — isolating C-14 cleanly — and tests whether attribution alone converts the checklist from a pass/fail register to an accountability register without contaminating other criteria.

---

You are a Dataverse security specialist (SE) working alongside a Customer Success advisor (CS). Produce a complete permissions trace for the feature described below.

**Feature**: {{topic}}
**Roles**: {{roles}} — default: Customer Service Representative, Customer Service Manager, System Administrator

---

**PRE-FLIGHT RULE — Blank-cell prohibition**: Every table cell SHALL carry an explicit value. Write "Not Configured", "None Found", or "N/A — [reason]" where no affirmative value applies. A blank cell is omission evidence, not absence evidence.

**SHALL obligations**:
- **SHALL A** — Role-operation matrix complete, all cells filled (C-01)
- **SHALL B** — Every sensitive field named with FLS status; null case stated explicitly (C-02)
- **SHALL C** — Record access scope assigned to every role (C-03)
- **SHALL D** — All four escalation vectors checked; each CLEAN justified (C-04)
- **SHALL E** — Gap inventory produced; no-gap case provides explicit evidence (C-05)

**Expert roles**:
- **SE (Security Engineer)** — owns Sections 1–9. Uses Dataverse-native terminology exclusively: security roles, business units, column security profiles, owner teams / access teams, table permissions, sharing records, environment roles. Generic terms like "group" or "permission level" without a Dataverse mapping are precision failures.
- **CS (Customer Success Advisor)** — owns Section 10. Independent perspective on agent-workflow implications and access differentials from an end-user standpoint.

---

### TABLE 1 — Role-Operation Matrix [SE | SHALL A | C-01]
*All cells: Granted / Denied / Conditional / N/A — reason. No blank cells.*

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Notes |
|------|--------|------|-------|--------|--------|----------|--------|-------|-------|

---

### TABLE 2 — Field-Level Security Coverage [SE | SHALL B | C-02]
*Every sensitive field listed regardless of FLS state. "Not Configured" is a finding, not an omission.*

| Field | Sensitivity Reason | FLS Status | Column Security Profile | Gap? | Notes |
|-------|--------------------|------------|------------------------|------|-------|

**FLS Null Case (write this line regardless of FLS state)**:
> FLS NULL CASE: [Explicitly state whether any sensitive field lacks a column security profile. If none configured: "No column security profiles configured. All sensitive fields accessible to any role with Read privilege. Gap confirmed."]

---

### TABLE 3 — Record Access Scope per Role [SE | SHALL C | C-03]
*Valid scopes: Own / Business Unit / Parent-Child BU / Organization-Wide / Team-Scoped. Ambiguous scope = named gap, not blank.*

| Role | Access Scope | BU Assignment | Team Scope Modifier | Ambiguity Flag |
|------|-------------|---------------|---------------------|----------------|

---

### TABLE 4 — Privilege Escalation Vector Sweep [SE | SHALL D | C-04]
*All four vectors checked. CLEAN requires explicit justification. No missing rows.*

| Vector | Status | Mechanism | Scope Gained | Justification |
|--------|--------|-----------|-------------|---------------|
| Team membership inheritance | | | | |
| Sharing rule bypass of FLS | | | | |
| Impersonation / service account | | | | |
| Environment-level admin override | | | | |

---

### TABLE 5 — Security Gap Inventory [SE | SHALL E | C-05]
*At least one named gap with specific field/role/rule, or explicit evidence of no gaps.*

| Gap ID | Description | Type | Affected Element | Severity |
|--------|------------|------|-----------------|----------|

---

### TABLE 6 — Sharing Rule Conflict Analysis [SE + CS | C-07]
*At least one sharing scenario evaluated for conflict: grants above role level, or blocks below FLS permit.*

| Sharing Rule | Type | Role-Level Access | FLS State | Conflict? | Description |
|-------------|------|------------------|-----------|-----------|-------------|

---

### TABLE 7 — Remediation Register [SE | C-08]
*Each gap from TABLE 5 gets a specific Dataverse-mechanism remediation. "Add FLS" is not specific; "create column security profile on [field], restrict Read to [role]" is.*

| Gap ID | Remediation | Dataverse Mechanism | Owner | Success Criteria |
|--------|------------|--------------------|----|-----------------|

---

### TABLE 8 — Defense-in-Depth Layer Analysis [SE | C-09]
*All four layers named and assessed. Identify the effective enforcement point for at least one operation.*

| Layer | Name | Assessed | Status | Enforcement Point? | Notes |
|-------|------|----------|---------|--------------------|-------|
| 1 | Environment / Admin Role | | | | |
| 2 | Security Role + BU Scope | | | | |
| 3 | Team Membership | | | | |
| 4 | Field-Level Security / Column Profiles | | | | |

**Enforcement point narrative (required for at least one operation)**:
> [Operation] — access [granted/denied] at Layer [N] because [reason]. Layer [N-1] does not override because [reason].

---

### TABLE 9 — Role Delta Pre-Work [SE → CS handoff | C-10]
*SE documents raw divergence data; CS interprets in TABLE 10.*

| Role A | Role B | Divergent Operations | FLS Divergence | Scope Divergence |
|--------|--------|---------------------|---------------|-----------------|

---

### TABLE 10 — Cross-Role Differential Analysis [CS | C-10]
*CS compares at least two roles side-by-side on one operation. States whether divergence is expected or anomalous.*

| Role Pair | Operation | Role A Access | Role B Access | Differential Expected? | CS Verdict |
|-----------|-----------|-------------|-------------|----------------------|-----------|

**CS Agent-Workflow Implication**:
> [For each anomalous differential: which agent or Power Automate workflow is affected? What user behavior change results?]

---

### TERMINAL VERIFICATION CHECKLIST [C-12 | C-14]
*Mark each SHALL: [x] SATISFIED or [ ] OPEN. OPEN items are self-identified output gaps. Each item names the accountable expert role — failures are attributed to the owner, not left anonymous.*

| # | Obligation | Status | Owner | Notes |
|---|-----------|--------|-------|-------|
| 1 | SHALL A — Role-operation matrix complete, all cells filled (C-01) | [ ] | SE | |
| 2 | SHALL B — Sensitive fields named with FLS status; null case explicitly stated (C-02) | [ ] | SE | |
| 3 | SHALL C — Record access scope assigned to every role (C-03) | [ ] | SE | |
| 4 | SHALL D — All four escalation vectors checked; CLEAN items justified (C-04) | [ ] | SE | |
| 5 | SHALL E — Gap inventory produced; no-gap case has explicit evidence (C-05) | [ ] | SE | |
| 6 | Dataverse-native terminology throughout SE sections — no generic RBAC substitution (C-06) | [ ] | SE | |
| 7 | Sharing rule conflict check — at least one scenario evaluated (C-07) | [ ] | SE + CS | |
| 8 | Remediation specificity — at least 50% of gaps have specific steps (C-08) | [ ] | SE | |
| 9 | All four defense-in-depth layers assessed; enforcement point named for at least one operation (C-09) | [ ] | SE | |
| 10 | Cross-role differential — at least two roles compared; anomalous items flagged (C-10) | [ ] | CS | |

---

## V-02

**Variation axis**: Role sequence — dedicated CA format-compliance auditor role (C-16)
**Hypothesis**: C-16 requires a third expert role whose mandate is explicitly format compliance, not security analysis. The cleanest structural enforcement is to define CA's mandate as the inverse of SE's: "CA validates the output's structure, not the permissions state." CA receives three dedicated sub-sections (table completeness audit, blank-cell compliance, format compliance verdict) and is explicitly prohibited from drawing security conclusions. SE and CS remain unchanged from the proven base. The single-axis test: does a role with a non-security mandate produce a structurally separate format verdict that satisfies C-16 without displacing existing criteria?

---

You are a Dataverse security specialist (SE) leading a three-role permissions trace. Roles and their mandates are stated below. A Compliance Auditor (CA) will validate output structural integrity after SE and CS complete their sections.

**Feature**: {{topic}}
**Roles in scope**: {{roles}} — default: Customer Service Representative, Customer Service Manager, System Administrator

---

**Role Mandates (non-negotiable)**:

**SE — Security Engineer**
*Mandate: Security content analysis using Dataverse-native constructs only. Terminology: security roles, business units, column security profiles, owner teams / access teams, table permissions, sharing records, environment roles.*
Owns: Sections 1–9 (all security analysis)

**CS — Customer Success Advisor**
*Mandate: Independent validation of agent-workflow implications and end-user access differentials.*
Owns: Section 10 (cross-role differential and workflow impact)

**CA — Compliance Auditor**
*Mandate: Output structural integrity ONLY. CA does NOT perform security analysis, draw security conclusions, name security gaps, or recommend remediation. CA validates that the output produced by SE and CS meets the structural requirements of a permissions trace: table completeness, blank-cell prohibition enforcement, and format schema adherence.*
Owns: Section CA-1 (table completeness audit), Section CA-2 (blank-cell compliance), Section CA-3 (format compliance verdict)

**MANDATE BOUNDARY RULE**: CA sections SHALL NOT contain security conclusions, gap findings, or remediation suggestions. Any security-content language in CA sections is a mandate violation. CA's sole question at every point is: "Does this output have the correct structure?"

---

**Pre-flight rules**:
- **Blank-cell prohibition**: Every table cell SHALL carry an explicit value.
- **SHALL A** — Role-operation matrix complete, all cells filled
- **SHALL B** — Every sensitive field named with FLS status; null case stated
- **SHALL C** — Record access scope assigned to every role
- **SHALL D** — All four escalation vectors checked; each CLEAN justified
- **SHALL E** — Gap inventory produced; no-gap case provides explicit evidence

---

### SECTION 1 — Role-Operation Matrix [SE | SHALL A | C-01]
*SE. All cells: Granted / Denied / Conditional / N/A — reason.*

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Notes |
|------|--------|------|-------|--------|--------|----------|--------|-------|-------|

---

### SECTION 2 — Field-Level Security Coverage [SE | SHALL B | C-02]
*SE. All sensitive fields listed. "Not Configured" is a finding, not an omission.*

| Field | Sensitivity Reason | FLS Status | Column Security Profile | Gap? | Notes |
|-------|--------------------|------------|------------------------|------|-------|

**FLS Null Case**:
> FLS NULL CASE: [State whether any sensitive field lacks a column security profile. If none: "No column security profiles configured. Gap confirmed."]

---

### SECTION 3 — Record Access Scope per Role [SE | SHALL C | C-03]
*SE. Valid scopes: Own / Business Unit / Parent-Child BU / Organization-Wide / Team-Scoped.*

| Role | Access Scope | BU Assignment | Team Modifier | Ambiguity Flag |
|------|-------------|---------------|--------------|----------------|

---

### SECTION 4 — Privilege Escalation Vector Sweep [SE | SHALL D | C-04]
*SE. All four vectors. CLEAN requires justification.*

| Vector | Status | Mechanism | Scope Gained | Justification |
|--------|--------|-----------|-------------|---------------|
| Team membership inheritance | | | | |
| Sharing rule bypass of FLS | | | | |
| Impersonation / service account | | | | |
| Environment-level admin override | | | | |

---

### SECTION 5 — Security Gap Inventory [SE | SHALL E | C-05]
*SE. Named gaps with specific field/role/rule, or explicit evidence of no gaps.*

| Gap ID | Description | Type | Affected Element | Severity |
|--------|------------|------|-----------------|----------|

---

### SECTION 6 — Sharing Rule Conflict Analysis [SE + CS | C-07]
*At least one sharing scenario evaluated for conflict.*

| Sharing Rule | Type | Role-Level Access | FLS State | Conflict? | Description |
|-------------|------|------------------|-----------|-----------|-------------|

---

### SECTION 7 — Remediation Register [SE | C-08]
*Specific Dataverse-mechanism remediations per gap.*

| Gap ID | Remediation | Dataverse Mechanism | Owner Team | Success Criteria |
|--------|------------|--------------------|-----------|--------------------|

---

### SECTION 8 — Defense-in-Depth Layer Analysis [SE | C-09]
*All four layers named and assessed. Enforcement point named for at least one operation.*

| Layer | Name | Assessed | Status | Enforcement Point? | Notes |
|-------|------|----------|---------|--------------------|-------|
| 1 | Environment / Admin Role | | | | |
| 2 | Security Role + BU Scope | | | | |
| 3 | Team Membership | | | | |
| 4 | FLS / Column Profiles | | | | |

**Enforcement point narrative**:
> [Operation] — access [granted/denied] at Layer [N] because [reason].

---

### SECTION 9 — Role Delta Pre-Work [SE → CS handoff | C-10]
*SE. Raw divergence data for CS interpretation.*

| Role A | Role B | Divergent Operations | FLS Divergence | Scope Divergence |
|--------|--------|---------------------|---------------|-----------------|

---

### SECTION 10 — Cross-Role Differential Analysis [CS | C-10]
*CS. Compare at least two roles side-by-side. State whether divergence is expected or anomalous.*

| Role Pair | Operation | Role A Access | Role B Access | Differential Expected? | CS Verdict |
|-----------|-----------|-------------|-------------|----------------------|-----------|

**CS Workflow Implication**:
> [Anomalous differentials: which workflow or agent is affected? What user behavior change results?]

---

### TERMINAL CHECKLIST [C-12]

| # | Obligation | Status | Notes |
|---|-----------|--------|-------|
| 1 | SHALL A — Role-operation matrix complete (C-01) | [ ] | |
| 2 | SHALL B — FLS coverage complete; null case stated (C-02) | [ ] | |
| 3 | SHALL C — Record scope assigned to every role (C-03) | [ ] | |
| 4 | SHALL D — All four escalation vectors checked (C-04) | [ ] | |
| 5 | SHALL E — Gap inventory with evidence (C-05) | [ ] | |
| 6 | Dataverse terminology throughout SE sections (C-06) | [ ] | |
| 7 | Sharing rule conflict evaluated (C-07) | [ ] | |
| 8 | Remediation specificity — 50% of gaps specific (C-08) | [ ] | |
| 9 | Defense-in-depth layers assessed; enforcement point named (C-09) | [ ] | |
| 10 | Cross-role differential complete; anomalous items flagged (C-10) | [ ] | |

---

### CA FORMAT COMPLIANCE SECTIONS [CA — structural validation only, no security content]

**CA mandate reminder**: The following sections contain no security conclusions. CA validates structural correctness of the output produced by SE and CS.

#### CA-1: Table Completeness Audit
*CA verifies that every required section is present and that all column headers are pre-defined.*

| Required Section | Present? | All Columns Pre-Defined? | Missing Elements |
|-----------------|----------|--------------------------|----------------|
| Section 1: Role-Operation Matrix | | | |
| Section 2: FLS Coverage | | | |
| Section 3: Record Access Scope | | | |
| Section 4: Escalation Vector Sweep | | | |
| Section 5: Gap Inventory | | | |
| Section 6: Sharing Rule Conflicts | | | |
| Section 7: Remediation Register | | | |
| Section 8: Defense-in-Depth | | | |
| Section 9: Role Delta Pre-Work | | | |
| Section 10: Cross-Role Differential | | | |

#### CA-2: Blank-Cell Compliance Audit
*CA checks that no table has empty cells — every cell carries an explicit value.*

| Section | Blank Cells Found? | Count | Required Resolution |
|---------|-------------------|-------|---------------------|
| Section 1 | | | |
| Section 2 | | | |
| Section 3 | | | |
| Section 4 | | | |
| Section 5 | | | |
| Sections 6–10 | | | |

#### CA-3: Format Compliance Verdict
*CA produces a single structural verdict independent of security findings.*

> **FORMAT COMPLIANCE VERDICT**: [PASS / CONDITIONAL PASS / FAIL]
>
> Structural integrity: [All 10 required sections present / N of 10 present]
> Blank-cell compliance: [No violations / N violations in sections X, Y, Z]
> Schema adherence: [All column headers pre-defined / deviations: ...]
>
> CA finding: [One-sentence structural summary. Example: "Output is structurally complete; Section 3 has one blank Ambiguity Flag cell that SHALL be resolved before this trace is accepted as a signal artifact."]

---

## V-03

**Variation axis**: Lifecycle emphasis — triple-lock preamble enforcement matrix (C-15)
**Hypothesis**: C-15 requires each essential criterion to be co-enforced by format schema + role sub-section + SHALL obligation simultaneously, not as alternatives. The challenge is that without an explicit declaration, models may use tables, roles, and SHALLs as independent coverage strategies rather than co-active enforcers of the same criterion. This variation makes the triple-lock visible before analysis begins: a preamble matrix maps each essential criterion (C-01 through C-05) to all three mechanisms and instructs that all three must be simultaneously active. Lifecycle emphasis is the axis — heavier pre-analysis declaration — while the analysis structure itself remains the proven base.

---

You are a Dataverse security expert. Before producing the permissions trace for {{topic}}, this prompt declares an enforcement matrix: every essential criterion is wired to three co-active mechanisms. All three mechanisms SHALL be active simultaneously — not alternatives.

**Feature**: {{topic}}
**Roles**: {{roles}} — default: Customer Service Representative, Customer Service Manager, System Administrator

---

## PREAMBLE: Criterion Enforcement Matrix [C-15]

*This table declares how each essential criterion is enforced by three orthogonal mechanisms. All three mechanisms SHALL be co-active for each criterion — not alternatives, not sequential fallbacks. An output that uses tables, roles, and SHALLs as independent coverage strategies rather than simultaneous enforcers fails the triple-lock requirement.*

| Criterion | Mechanism 1: Format Schema (pre-printed table) | Mechanism 2: Role Sub-Section Assignment | Mechanism 3: SHALL Obligation | All Three Active? |
|-----------|----------------------------------------------|----------------------------------------|------------------------------|-------------------|
| C-01: Role-operation matrix | TABLE 1 — pre-printed role × operation schema; blank cells prohibited | SE-1: SE owns exclusively; Dataverse privilege terminology required | SHALL A: complete matrix, all cells filled | Required: Yes |
| C-02: FLS coverage + null case | TABLE 2 — pre-printed field × FLS schema + mandatory null case closing line | SE-2: SE owns exclusively; column security profile terminology required | SHALL B: every sensitive field named; null case stated | Required: Yes |
| C-03: Record scope per role | TABLE 3 — pre-printed role × scope schema; ambiguity flag column | SE-3: SE owns exclusively; BU/team Dataverse scope labels required | SHALL C: scope assigned to every role | Required: Yes |
| C-04: Escalation vector sweep | TABLE 4 — pre-printed 4-row vector schema; no row omissions | SE-4: SE owns exclusively; all four named vectors | SHALL D: all vectors checked; CLEAN justified per row | Required: Yes |
| C-05: Gap inventory | TABLE 5 — pre-printed gap registry schema; no-gap requires evidence row | SE-5: SE owns exclusively; specific field/role/rule per gap | SHALL E: inventory produced; no-gap evidence stated | Required: Yes |

**Triple-lock enforcement rule**: For each essential criterion, you must:
1. Populate the pre-printed table schema (Mechanism 1 — format layer)
2. Produce the content within the SE-assigned sub-section using Dataverse terminology (Mechanism 2 — role layer)
3. Mark the corresponding SHALL as SATISFIED in the terminal checklist (Mechanism 3 — obligation layer)

All three are simultaneous requirements, not alternatives. Completing a table without a SHALL check is a partial lock failure. Writing a SHALL without a populated table is a partial lock failure. Producing content outside the SE-assigned sub-section is a partial lock failure.

---

**Expert roles**:
- **SE (Security Engineer)** — security content analysis. Dataverse-native terminology only. Owns Tables 1–9 and their corresponding SHALLs.
- **CS (Customer Success Advisor)** — independent agent-workflow implications analysis. Owns Table 10.

**Blank-cell prohibition**: Every table cell SHALL carry an explicit value.

---

### TABLE 1 — Role-Operation Matrix [SE-1 | SHALL A | C-01 | Triple-Lock: Format + Role + SHALL]
*Pre-printed schema. All cells: Granted / Denied / Conditional / N/A — reason. Triple-lock: this is Mechanism 1; SE-1 is Mechanism 2; SHALL A in terminal checklist is Mechanism 3.*

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Notes |
|------|--------|------|-------|--------|--------|----------|--------|-------|-------|

---

### TABLE 2 — Field-Level Security Coverage [SE-2 | SHALL B | C-02 | Triple-Lock: Format + Role + SHALL]
*Pre-printed schema. All sensitive fields listed. "Not Configured" is a finding. Null case line is part of SHALL B.*

| Field | Sensitivity Reason | FLS Status | Column Security Profile | Gap? | Notes |
|-------|--------------------|------------|------------------------|------|-------|

**FLS Null Case** (mandatory closing line — part of SHALL B):
> FLS NULL CASE: [Explicitly state whether any sensitive field lacks a column security profile.]

---

### TABLE 3 — Record Access Scope [SE-3 | SHALL C | C-03 | Triple-Lock: Format + Role + SHALL]
*Pre-printed schema. Scopes: Own / Business Unit / Parent-Child BU / Organization-Wide / Team-Scoped.*

| Role | Access Scope | BU Assignment | Team Modifier | Ambiguity Flag |
|------|-------------|---------------|--------------|----------------|

---

### TABLE 4 — Escalation Vector Sweep [SE-4 | SHALL D | C-04 | Triple-Lock: Format + Role + SHALL]
*Pre-printed 4-row schema. CLEAN requires justification. No row omissions.*

| Vector | Status | Mechanism | Scope Gained | Justification |
|--------|--------|-----------|-------------|---------------|
| Team membership inheritance | | | | |
| Sharing rule bypass of FLS | | | | |
| Impersonation / service account | | | | |
| Environment-level admin override | | | | |

---

### TABLE 5 — Security Gap Inventory [SE-5 | SHALL E | C-05 | Triple-Lock: Format + Role + SHALL]
*Pre-printed schema. Named gaps with specific element, or explicit no-gap evidence row.*

| Gap ID | Description | Type | Affected Element | Severity |
|--------|------------|------|-----------------|----------|

---

### TABLE 6 — Sharing Rule Conflict Analysis [SE + CS | C-07]
*At least one sharing scenario evaluated for conflict.*

| Sharing Rule | Type | Role-Level Access | FLS State | Conflict? | Description |
|-------------|------|------------------|-----------|-----------|-------------|

---

### TABLE 7 — Remediation Register [SE | C-08]
*Specific Dataverse-mechanism remediations per gap.*

| Gap ID | Remediation | Dataverse Mechanism | Owner | Success Criteria |
|--------|------------|--------------------|----|-----------------|

---

### TABLE 8 — Defense-in-Depth Layer Analysis [SE | C-09]
*All four layers. Enforcement point named for at least one operation.*

| Layer | Name | Assessed | Status | Enforcement Point? | Notes |
|-------|------|----------|---------|--------------------|-------|
| 1 | Environment / Admin Role | | | | |
| 2 | Security Role + BU Scope | | | | |
| 3 | Team Membership | | | | |
| 4 | FLS / Column Profiles | | | | |

**Enforcement point narrative**:
> [Operation] — access [granted/denied] at Layer [N] because [reason].

---

### TABLE 9 — Role Delta Pre-Work [SE → CS handoff | C-10]

| Role A | Role B | Divergent Operations | FLS Divergence | Scope Divergence |
|--------|--------|---------------------|---------------|-----------------|

---

### TABLE 10 — Cross-Role Differential Analysis [CS | C-10]
*Compare at least two roles. State whether divergence is expected or anomalous.*

| Role Pair | Operation | Role A Access | Role B Access | Differential Expected? | CS Verdict |
|-----------|-----------|-------------|-------------|----------------------|-----------|

---

### TERMINAL CHECKLIST — SHALL Verification [C-12 | Triple-Lock Completion Register]
*Marking SATISFIED here completes Mechanism 3 (the obligation lock) for that essential criterion. An item left OPEN means the triple-lock for that criterion is incomplete.*

| # | SHALL | Status | Notes |
|---|-------|--------|-------|
| 1 | SHALL A — Role-operation matrix complete (C-01) — Triple-lock: Table 1 + SE-1 + this item | [ ] | |
| 2 | SHALL B — FLS coverage + null case stated (C-02) — Triple-lock: Table 2 + SE-2 + this item | [ ] | |
| 3 | SHALL C — Record scope assigned to all roles (C-03) — Triple-lock: Table 3 + SE-3 + this item | [ ] | |
| 4 | SHALL D — All four escalation vectors checked (C-04) — Triple-lock: Table 4 + SE-4 + this item | [ ] | |
| 5 | SHALL E — Gap inventory with evidence (C-05) — Triple-lock: Table 5 + SE-5 + this item | [ ] | |
| 6 | Dataverse-native terminology throughout SE sections (C-06) | [ ] | |
| 7 | Sharing rule conflict — at least one scenario evaluated (C-07) | [ ] | |
| 8 | Remediation specificity — at least 50% of gaps have specific steps (C-08) | [ ] | |
| 9 | Defense-in-depth layers assessed; enforcement point named (C-09) | [ ] | |
| 10 | Cross-role differential; anomalous differentials flagged (C-10) | [ ] | |

---

## V-04

**Variation axis**: Role sequence × Output format — CA role (C-16) + checklist ownership (C-14)
**Hypothesis**: C-14 and C-16 are structurally complementary. C-16 creates the CA role whose mandate is format compliance; C-14 assigns terminal checklist items to named owners. When CA is introduced, the most natural ownership split is: SE owns security-content criteria (C-01–C-09), CS owns differential criteria (C-10), and CA owns format-structural criteria (table completeness, blank-cell compliance, compliance verdict). This makes C-14 (ownership attribution) and C-16 (CA mandate) mutually reinforcing — CA's format audit sub-sections map directly to CA-owned checklist items, converting the terminal checklist into a cross-role accountability register.

---

You are a Dataverse security specialist (SE) leading a three-role permissions trace. The terminal checklist assigns each obligation to a specific expert role — failures are attributable, not anonymous.

**Feature**: {{topic}}
**Roles in scope**: {{roles}} — default: Customer Service Representative, Customer Service Manager, System Administrator

---

**Expert Role Mandates**:

**SE — Security Engineer**
*Security content analysis. Dataverse-native terminology only: security roles, business units, column security profiles, owner/access teams, table permissions, sharing records, environment roles.*
Owns: Sections 1–9 + Terminal checklist items 1–9

**CS — Customer Success Advisor**
*Independent agent-workflow and end-user access differential analysis.*
Owns: Section 10 + Terminal checklist item 10

**CA — Compliance Auditor**
*Output structural integrity ONLY. CA does NOT make security conclusions, name gaps, or recommend remediation. CA validates table completeness, blank-cell compliance, and schema adherence.*
Owns: Sections CA-1, CA-2, CA-3 + Terminal checklist items 11–13

**MANDATE BOUNDARY RULE**: CA sections contain no security content. SE/CS sections contain no structural compliance verdicts.

---

**Pre-flight rules**:
- **Blank-cell prohibition**: Every table cell SHALL carry an explicit value.
- **SHALL A** — Role-operation matrix complete, all cells filled
- **SHALL B** — Every sensitive field named with FLS status; null case stated
- **SHALL C** — Record scope assigned to every role
- **SHALL D** — All four escalation vectors checked; CLEAN justified
- **SHALL E** — Gap inventory produced; no-gap has explicit evidence

---

### SECTION 1 — Role-Operation Matrix [SE | SHALL A | C-01]

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Notes |
|------|--------|------|-------|--------|--------|----------|--------|-------|-------|

---

### SECTION 2 — Field-Level Security Coverage [SE | SHALL B | C-02]

| Field | Sensitivity Reason | FLS Status | Column Security Profile | Gap? | Notes |
|-------|--------------------|------------|------------------------|------|-------|

**FLS Null Case**:
> FLS NULL CASE: [...]

---

### SECTION 3 — Record Access Scope [SE | SHALL C | C-03]

| Role | Access Scope | BU Assignment | Team Modifier | Ambiguity Flag |
|------|-------------|---------------|--------------|----------------|

---

### SECTION 4 — Escalation Vector Sweep [SE | SHALL D | C-04]

| Vector | Status | Mechanism | Scope Gained | Justification |
|--------|--------|-----------|-------------|---------------|
| Team membership inheritance | | | | |
| Sharing rule bypass of FLS | | | | |
| Impersonation / service account | | | | |
| Environment-level admin override | | | | |

---

### SECTION 5 — Security Gap Inventory [SE | SHALL E | C-05]

| Gap ID | Description | Type | Affected Element | Severity |
|--------|------------|------|-----------------|----------|

---

### SECTION 6 — Sharing Rule Conflict Analysis [SE + CS | C-07]

| Sharing Rule | Type | Role-Level Access | FLS State | Conflict? | Description |
|-------------|------|------------------|-----------|-----------|-------------|

---

### SECTION 7 — Remediation Register [SE | C-08]

| Gap ID | Remediation | Dataverse Mechanism | Owner Team | Success Criteria |
|--------|------------|--------------------|-----------|--------------------|

---

### SECTION 8 — Defense-in-Depth Layer Analysis [SE | C-09]

| Layer | Name | Assessed | Status | Enforcement Point? | Notes |
|-------|------|----------|---------|--------------------|-------|
| 1 | Environment / Admin Role | | | | |
| 2 | Security Role + BU Scope | | | | |
| 3 | Team Membership | | | | |
| 4 | FLS / Column Profiles | | | | |

**Enforcement point narrative**:
> [Operation] — access [granted/denied] at Layer [N] because [reason].

---

### SECTION 9 — Role Delta Pre-Work [SE → CS | C-10]

| Role A | Role B | Divergent Operations | FLS Divergence | Scope Divergence |
|--------|--------|---------------------|---------------|-----------------|

---

### SECTION 10 — Cross-Role Differential Analysis [CS | C-10]

| Role Pair | Operation | Role A Access | Role B Access | Differential Expected? | CS Verdict |
|-----------|-----------|-------------|-------------|----------------------|-----------|

**CS Workflow Implication**:
> [Anomalous differentials: which workflow or agent is affected?]

---

### CA FORMAT COMPLIANCE SECTIONS [CA — structural validation only, no security content]

#### CA-1: Table Completeness Audit

| Section | Present? | All Columns Pre-Defined? | Missing Elements |
|---------|----------|--------------------------|----------------|
| Section 1: Role-Operation Matrix | | | |
| Section 2: FLS Coverage | | | |
| Section 3: Record Access Scope | | | |
| Section 4: Escalation Vector Sweep | | | |
| Section 5: Gap Inventory | | | |
| Section 6: Sharing Rule Conflicts | | | |
| Section 7: Remediation Register | | | |
| Section 8: Defense-in-Depth | | | |
| Section 9: Role Delta Pre-Work | | | |
| Section 10: Cross-Role Differential | | | |

#### CA-2: Blank-Cell Compliance Audit

| Section | Blank Cells Found? | Count | Required Resolution |
|---------|-------------------|-------|---------------------|
| Sections 1–5 | | | |
| Sections 6–10 | | | |

#### CA-3: Format Compliance Verdict

> **FORMAT COMPLIANCE VERDICT**: [PASS / CONDITIONAL PASS / FAIL]
>
> Tables present: [N of 10] | Blank-cell violations: [N] | Schema deviations: [describe or "None"]
>
> CA finding: [One-sentence structural verdict. Independent of security findings.]

---

### TERMINAL VERIFICATION CHECKLIST [C-12 | C-14]
*Each item names the accountable expert role. OPEN items identify both the gap and the responsible role.*

| # | Obligation | Status | Owner | Notes |
|---|-----------|--------|-------|-------|
| 1 | SHALL A — Role-operation matrix complete (C-01) | [ ] | SE | |
| 2 | SHALL B — FLS coverage + null case stated (C-02) | [ ] | SE | |
| 3 | SHALL C — Record scope assigned to all roles (C-03) | [ ] | SE | |
| 4 | SHALL D — All four escalation vectors checked (C-04) | [ ] | SE | |
| 5 | SHALL E — Gap inventory with evidence (C-05) | [ ] | SE | |
| 6 | Dataverse terminology throughout SE sections (C-06) | [ ] | SE | |
| 7 | Sharing rule conflict evaluated (C-07) | [ ] | SE + CS | |
| 8 | Remediation specificity — at least 50% specific (C-08) | [ ] | SE | |
| 9 | Defense-in-depth layers assessed; enforcement point named (C-09) | [ ] | SE | |
| 10 | Cross-role differential; anomalous items flagged (C-10) | [ ] | CS | |
| 11 | All 10 required sections present; all columns pre-defined (CA-1) | [ ] | CA | |
| 12 | No blank cells in any section (CA-2) | [ ] | CA | |
| 13 | Format Compliance Verdict produced as independent CA section (CA-3) | [ ] | CA | |

---

## V-05

**Variation axis**: Role sequence × Output format × Lifecycle emphasis — C-14 + C-15 + C-16 (full new aspirational integration)
**Hypothesis**: The three new aspirational criteria form a mutually reinforcing system. Triple-lock (C-15) makes co-enforcement structurally visible via preamble matrix. CA (C-16) provides a dedicated non-security role whose format audit sub-sections serve as a fourth enforcement axis beyond the three locks. Checklist ownership (C-14) maps every criterion to a named owner so that lock failures are attributed, not anonymous. Full integration makes C-15 the architectural skeleton, C-16 the independent structural auditor, and C-14 the accountability register — no essential criterion can fail silently across any of the three enforcement paths. The CA's triple-lock compliance audit in CA-1 also directly closes the loop: CA verifies that C-15 itself was satisfied.

---

You are a Dataverse security specialist (SE) leading a three-role permissions trace with triple-lock criterion enforcement. Every essential criterion is simultaneously enforced by three orthogonal mechanisms. A Compliance Auditor (CA) validates the output's structural integrity independently. Every terminal checklist item names an accountable expert role — no failure is anonymous.

**Feature**: {{topic}}
**Roles in scope**: {{roles}} — default: Customer Service Representative, Customer Service Manager, System Administrator

---

## PREAMBLE: Triple-Lock Enforcement Matrix [C-15]

*Each essential criterion is mapped to three co-active mechanisms below. All three SHALL be simultaneously active. The CA role audits completion of this matrix in Section CA-1.*

| Criterion | Mechanism 1: Pre-Printed Table Schema | Mechanism 2: Expert Role Sub-Section | Mechanism 3: SHALL Obligation | CA Audit Point |
|-----------|--------------------------------------|-------------------------------------|------------------------------|----------------|
| C-01: Role-operation matrix | TABLE 1 — role × operation schema; all 8 ops; blank cells prohibited | SE-1 owns; Dataverse privilege terms required | SHALL A — complete matrix, all cells filled | CA-1 row 1 |
| C-02: FLS + null case | TABLE 2 — field × FLS schema + mandatory null case closing line | SE-2 owns; column security profile terminology required | SHALL B — every sensitive field named; null case stated | CA-1 row 2 |
| C-03: Record scope | TABLE 3 — role × scope schema; ambiguity flag column required | SE-3 owns; BU / team-scoped Dataverse labels required | SHALL C — scope assigned to every role | CA-1 row 3 |
| C-04: Escalation vectors | TABLE 4 — pre-printed 4-row vector schema; no row omissions permitted | SE-4 owns; all four named vectors checked | SHALL D — all vectors checked; CLEAN justified per row | CA-1 row 4 |
| C-05: Gap inventory | TABLE 5 — gap registry schema; no-gap case requires evidence row | SE-5 owns; specific field/role/rule per gap required | SHALL E — inventory produced; no-gap has explicit evidence | CA-1 row 5 |

**Triple-lock enforcement rule**: For each essential criterion, all three mechanisms must be simultaneously active:
1. Populate the pre-printed table schema (format layer — Mechanism 1)
2. Produce content in the SE-assigned sub-section using Dataverse terminology (role layer — Mechanism 2)
3. Mark the corresponding SHALL SATISFIED in the terminal checklist (obligation layer — Mechanism 3)

Using any mechanism in isolation or as a fallback for another is a partial lock failure.

---

**Expert Role Mandates**:

**SE — Security Engineer**
*Security content analysis. Dataverse-native terminology only. No generic RBAC language.*
Owns: Tables 1–9, SHALLs A–E, Terminal checklist items 1–9

**CS — Customer Success Advisor**
*Independent agent-workflow and end-user access differential analysis.*
Owns: Table 10, Terminal checklist item 10

**CA — Compliance Auditor**
*Output structural integrity ONLY. CA does NOT make security conclusions, identify security gaps, or recommend remediation. CA validates: table completeness, blank-cell compliance, schema adherence, and triple-lock enforcement matrix completion.*
Owns: Sections CA-1, CA-2, CA-3, Terminal checklist items 11–14

**MANDATE BOUNDARY**: CA sections are structurally distinct from SE/CS sections. CA produces no security findings. SE/CS produce no structural compliance verdicts. Cross-mandate content is a violation.

---

**Pre-flight rules**:
- **Blank-cell prohibition**: Every table cell SHALL carry an explicit value.
- **SHALL A** — Role-operation matrix complete
- **SHALL B** — Every sensitive field named; null case stated
- **SHALL C** — Record scope assigned to every role
- **SHALL D** — All four escalation vectors checked; CLEAN justified
- **SHALL E** — Gap inventory produced; no-gap has explicit evidence

---

### TABLE 1 — Role-Operation Matrix [SE-1 | SHALL A | C-01 | Triple-Lock Active]
*Pre-printed schema. All cells: Granted / Denied / Conditional / N/A — reason. Triple-lock: Table 1 is M1; SE-1 is M2; SHALL A in checklist is M3.*

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Notes |
|------|--------|------|-------|--------|--------|----------|--------|-------|-------|

---

### TABLE 2 — Field-Level Security Coverage [SE-2 | SHALL B | C-02 | Triple-Lock Active]
*Pre-printed schema. All sensitive fields. "Not Configured" = finding. Null case line is part of SHALL B.*

| Field | Sensitivity Reason | FLS Status | Column Security Profile | Gap? | Notes |
|-------|--------------------|------------|------------------------|------|-------|

**FLS Null Case** (SHALL B component — mandatory):
> FLS NULL CASE: [State whether any sensitive field lacks a column security profile.]

---

### TABLE 3 — Record Access Scope [SE-3 | SHALL C | C-03 | Triple-Lock Active]
*Scopes: Own / Business Unit / Parent-Child BU / Organization-Wide / Team-Scoped.*

| Role | Access Scope | BU Assignment | Team Modifier | Ambiguity Flag |
|------|-------------|---------------|--------------|----------------|

---

### TABLE 4 — Escalation Vector Sweep [SE-4 | SHALL D | C-04 | Triple-Lock Active]
*Pre-printed 4-row schema. All rows required. CLEAN requires justification.*

| Vector | Status | Mechanism | Scope Gained | Justification |
|--------|--------|-----------|-------------|---------------|
| Team membership inheritance | | | | |
| Sharing rule bypass of FLS | | | | |
| Impersonation / service account | | | | |
| Environment-level admin override | | | | |

---

### TABLE 5 — Security Gap Inventory [SE-5 | SHALL E | C-05 | Triple-Lock Active]
*Named gaps with specific element, or explicit no-gap evidence row.*

| Gap ID | Description | Type | Affected Element | Severity |
|--------|------------|------|-----------------|----------|

---

### TABLE 6 — Sharing Rule Conflict Analysis [SE + CS | C-07]

| Sharing Rule | Type | Role-Level Access | FLS State | Conflict? | Description |
|-------------|------|------------------|-----------|-----------|-------------|

---

### TABLE 7 — Remediation Register [SE | C-08]

| Gap ID | Remediation | Dataverse Mechanism | Owner | Success Criteria |
|--------|------------|--------------------|----|-----------------|

---

### TABLE 8 — Defense-in-Depth Layer Analysis [SE | C-09]

| Layer | Name | Assessed | Status | Enforcement Point? | Notes |
|-------|------|----------|---------|--------------------|-------|
| 1 | Environment / Admin Role | | | | |
| 2 | Security Role + BU Scope | | | | |
| 3 | Team Membership | | | | |
| 4 | FLS / Column Profiles | | | | |

**Enforcement point narrative**:
> [Operation] — access [granted/denied] at Layer [N] because [reason].

---

### TABLE 9 — Role Delta Pre-Work [SE → CS | C-10]

| Role A | Role B | Divergent Operations | FLS Divergence | Scope Divergence |
|--------|--------|---------------------|---------------|-----------------|

---

### TABLE 10 — Cross-Role Differential Analysis [CS | C-10]

| Role Pair | Operation | Role A Access | Role B Access | Differential Expected? | CS Verdict |
|-----------|-----------|-------------|-------------|----------------------|-----------|

**CS Workflow Implication**:
> [Anomalous differentials: which workflow or agent is affected?]

---

### CA FORMAT COMPLIANCE SECTIONS [CA — structural integrity only, no security content]

#### CA-1: Triple-Lock Compliance Audit [C-15]
*CA verifies that each essential criterion has all three mechanisms active. A row with any "No" is a partial lock failure.*

| Criterion | Table Present and Populated? | SE Sub-Section Assigned? | SHALL in Checklist? | Triple-Lock Complete? |
|-----------|------------------------------|--------------------------|--------------------|-----------------------|
| C-01 (Table 1 / SE-1 / SHALL A) | | | | |
| C-02 (Table 2 / SE-2 / SHALL B) | | | | |
| C-03 (Table 3 / SE-3 / SHALL C) | | | | |
| C-04 (Table 4 / SE-4 / SHALL D) | | | | |
| C-05 (Table 5 / SE-5 / SHALL E) | | | | |

#### CA-2: Table Completeness and Blank-Cell Audit

| Section | All Columns Present? | Blank Cells Found? | Count | Resolution Required |
|---------|---------------------|--------------------|-------|---------------------|
| Table 1 | | | | |
| Table 2 | | | | |
| Table 3 | | | | |
| Table 4 | | | | |
| Table 5 | | | | |
| Tables 6–10 | | | | |

#### CA-3: Format Compliance Verdict

> **FORMAT COMPLIANCE VERDICT**: [PASS / CONDITIONAL PASS / FAIL]
>
> Triple-lock status: [N of 5 essential criteria have all 3 mechanisms active]
> Sections complete: [N of 10 required tables present and populated]
> Blank-cell violations: [N found / none found]
>
> CA finding: [One-sentence structural verdict. Independent of security findings.]

---

### TERMINAL VERIFICATION CHECKLIST [C-12 | C-14]
*Each item names the accountable expert role. OPEN items attribute the failure to the responsible role — failures are not anonymous.*

| # | Obligation | Status | Owner | Notes |
|---|-----------|--------|-------|-------|
| 1 | SHALL A — Role-operation matrix complete (C-01) | [ ] | SE | |
| 2 | SHALL B — FLS coverage + null case stated (C-02) | [ ] | SE | |
| 3 | SHALL C — Record scope assigned to all roles (C-03) | [ ] | SE | |
| 4 | SHALL D — All four escalation vectors checked (C-04) | [ ] | SE | |
| 5 | SHALL E — Gap inventory with evidence (C-05) | [ ] | SE | |
| 6 | Dataverse-native terminology throughout SE sections (C-06) | [ ] | SE | |
| 7 | Sharing rule conflict evaluated (C-07) | [ ] | SE + CS | |
| 8 | Remediation specificity — at least 50% specific (C-08) | [ ] | SE | |
| 9 | Defense-in-depth layers assessed; enforcement point named (C-09) | [ ] | SE | |
| 10 | Cross-role differential; anomalous items flagged (C-10) | [ ] | CS | |
| 11 | Triple-lock verified: all 5 essential criteria have 3 active mechanisms (C-15) | [ ] | CA | |
| 12 | All 10 sections present; all columns pre-defined; no blank cells (C-11) | [ ] | CA | |
| 13 | Format Compliance Verdict produced as independent CA section (C-16) | [ ] | CA | |
| 14 | Every checklist item above names an accountable expert role (C-14) | [ ] | CA | |
