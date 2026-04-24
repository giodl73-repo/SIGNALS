# trace-permissions — Round 5 Variations

**Rubric version**: v4 (18 criteria — C-17/C-18 added from R4 excellence signals)
**Round**: 5
**Date**: 2026-03-15
**Axes explored**: Phrasing register / C-18 isolation (single), Output format / C-17+C-18 column labeling (single), Role sequence / CA-first preamble authorship (single), Output format x Lifecycle emphasis / schema registry + preamble reaffirmation (combo), All four / full quad-lock integration (combo)

**Scoring formula from rubric v4**: Aspirational denominator is 10. Max aspirational = (pass_count / 10) × 10. Each passed aspirational criterion is worth 1.0 pt.

**New criteria targeted this round**:
- C-17: Criterion enforcement preamble matrix — pre-analysis table mapping C-01–C-05 to format schema + role sub-section + SHALL, with stated "all three SHALL be active simultaneously" rule
- C-18: Four-mechanism criterion enforcement (quad-lock) — preamble has M1/M2/M3/M4 columns; CA audit rows cross-reference each criterion by ID; CA verdict cites the preamble matrix

**Baseline from R4**: V-05 already has the preamble (C-17 baseline), CA role (C-16), triple-lock enforcement (C-15), checklist attribution (C-14). The gap: CA-1 in V-05 audited by inspection ("Table Present and Populated?") rather than by matrix cross-reference. C-18 requires CA to use criterion-ID-prefixed verification rows ("C-01: TABLE 1 present, all cells filled — PASS") and CA-3 to cite the preamble matrix by name.

---

## V-01

**Variation axis**: Phrasing register — criterion-ID-prefixed CA audit rows (C-18 isolation)
**Hypothesis**: R4 V-05 had all four preamble columns and a CA role, but CA-1 used generic column headers ("Table Present and Populated?", "SE Sub-Section Assigned?") and audited by structural inspection. C-18 fails when CA audits by inspection rather than by matrix cross-reference. The minimum change is rewriting CA-1 as a criterion-ID-indexed cross-reference: each row starts with "C-01:", "C-02:", etc., and the verification statement explicitly names which preamble row it is checking. CA-3 is rewritten to open with "Per preamble enforcement matrix:" before issuing its verdict. No changes to preamble structure, SE sections, CS sections, or checklist ownership — single axis isolation.

---

You are a Dataverse security specialist (SE) leading a three-role permissions trace. Every essential criterion is simultaneously enforced by three co-active mechanisms declared below. A Compliance Auditor (CA) will cross-reference each criterion against the preamble enforcement matrix — not by inspection, but by matrix row.

**Feature**: {{topic}}
**Roles in scope**: {{roles}} — default: Customer Service Representative, Customer Service Manager, System Administrator

---

## PREAMBLE: Criterion Enforcement Matrix [C-15 | C-17]

*This table is the enforcement contract. Each essential criterion is mapped to three co-active mechanisms. All three mechanisms SHALL be active simultaneously — not alternatives, not sequential fallbacks. The CA Audit Point column names the specific CA-1 row that will verify this row. CA audits by matrix cross-reference, not by independent inspection.*

| Criterion | M1: Pre-Printed Table Schema | M2: Expert Role Sub-Section | M3: SHALL Obligation | CA Audit Point |
|-----------|-----------------------------|-----------------------------|---------------------|----------------|
| C-01: Role-operation matrix | TABLE 1 — role × 8-op schema; blank cells prohibited | SE-1 owns; Dataverse privilege terms required | SHALL A — complete matrix, all cells filled | CA-1 row C-01 |
| C-02: FLS coverage + null case | TABLE 2 — field × FLS schema + mandatory null case line | SE-2 owns; column security profile terms required | SHALL B — every sensitive field named; null case stated | CA-1 row C-02 |
| C-03: Record scope per role | TABLE 3 — role × scope schema; ambiguity flag column required | SE-3 owns; BU / team-scoped Dataverse labels required | SHALL C — scope assigned to every role | CA-1 row C-03 |
| C-04: Escalation vector sweep | TABLE 4 — pre-printed 4-row vector schema; no row omissions | SE-4 owns; all four named vectors checked | SHALL D — all vectors checked; CLEAN justified per row | CA-1 row C-04 |
| C-05: Gap inventory | TABLE 5 — gap registry schema; no-gap requires evidence row | SE-5 owns; specific field/role/rule per gap required | SHALL E — inventory produced; no-gap has explicit evidence | CA-1 row C-05 |

**Enforcement rule**: All three mechanisms SHALL be active simultaneously. Completing a table without a SHALL check is a partial lock failure. A SHALL without a populated table is a partial lock failure. Content outside the SE-assigned sub-section is a partial lock failure.

---

**Expert Role Mandates**:

**SE — Security Engineer**
*Security content analysis. Dataverse-native terminology only: security roles, business units, column security profiles, owner teams / access teams, table permissions, sharing records, environment roles.*
Owns: Tables 1–9, SHALLs A–E, Terminal checklist items 1–9

**CS — Customer Success Advisor**
*Independent agent-workflow and end-user access differential analysis.*
Owns: Table 10, Terminal checklist item 10

**CA — Compliance Auditor**
*Output structural integrity ONLY. CA does NOT make security conclusions, identify security gaps, or recommend remediation. CA validates: table completeness, blank-cell compliance, schema adherence, and preamble enforcement matrix completion — by cross-referencing the preamble, not by independent inspection.*
Owns: Sections CA-1, CA-2, CA-3, Terminal checklist items 11–14

**MANDATE BOUNDARY**: CA sections contain no security content. SE/CS sections contain no structural compliance verdicts.

---

**Pre-flight rules**:
- **Blank-cell prohibition**: Every table cell SHALL carry an explicit value. Write "Not Configured", "None Found", or "N/A — [reason]" where no affirmative value applies.
- **SHALL A** — Role-operation matrix complete, all cells filled
- **SHALL B** — Every sensitive field named with FLS status; null case stated explicitly
- **SHALL C** — Record access scope assigned to every role
- **SHALL D** — All four escalation vectors checked; CLEAN justified per row
- **SHALL E** — Gap inventory produced; no-gap case has explicit evidence

---

### TABLE 1 — Role-Operation Matrix [SE-1 | SHALL A | C-01 | Triple-Lock Active]
*Pre-printed schema. All cells: Granted / Denied / Conditional / N/A — reason. M1: this table; M2: SE-1; M3: SHALL A in checklist.*

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Notes |
|------|--------|------|-------|--------|--------|----------|--------|-------|-------|

---

### TABLE 2 — Field-Level Security Coverage [SE-2 | SHALL B | C-02 | Triple-Lock Active]
*Pre-printed schema. All sensitive fields listed. "Not Configured" = finding, not omission. M1: this table; M2: SE-2; M3: SHALL B in checklist.*

| Field | Sensitivity Reason | FLS Status | Column Security Profile | Gap? | Notes |
|-------|--------------------|------------|------------------------|------|-------|

**FLS Null Case** (SHALL B component — mandatory closing line):
> FLS NULL CASE: [Explicitly state whether any sensitive field lacks a column security profile. If none configured: "No column security profiles configured. All sensitive fields accessible to any role with Read privilege. Gap confirmed."]

---

### TABLE 3 — Record Access Scope per Role [SE-3 | SHALL C | C-03 | Triple-Lock Active]
*Pre-printed schema. Valid scopes: Own / Business Unit / Parent-Child BU / Organization-Wide / Team-Scoped. Ambiguous scope = named gap. M1: this table; M2: SE-3; M3: SHALL C in checklist.*

| Role | Access Scope | BU Assignment | Team Modifier | Ambiguity Flag |
|------|-------------|---------------|--------------|----------------|

---

### TABLE 4 — Privilege Escalation Vector Sweep [SE-4 | SHALL D | C-04 | Triple-Lock Active]
*Pre-printed 4-row schema. All rows required. CLEAN requires explicit justification. M1: this table; M2: SE-4; M3: SHALL D in checklist.*

| Vector | Status | Mechanism | Scope Gained | Justification |
|--------|--------|-----------|-------------|---------------|
| Team membership inheritance | | | | |
| Sharing rule bypass of FLS | | | | |
| Impersonation / service account | | | | |
| Environment-level admin override | | | | |

---

### TABLE 5 — Security Gap Inventory [SE-5 | SHALL E | C-05 | Triple-Lock Active]
*Pre-printed schema. Named gaps with specific field/role/rule, or explicit no-gap evidence row. M1: this table; M2: SE-5; M3: SHALL E in checklist.*

| Gap ID | Description | Type | Affected Element | Severity |
|--------|------------|------|-----------------|----------|

---

### TABLE 6 — Sharing Rule Conflict Analysis [SE + CS | C-07]
*At least one sharing scenario evaluated for conflict: grants above role level, or blocks below FLS permit.*

| Sharing Rule | Type | Role-Level Access | FLS State | Conflict? | Description |
|-------------|------|------------------|-----------|-----------|-------------|

---

### TABLE 7 — Remediation Register [SE | C-08]
*Specific Dataverse-mechanism remediations per gap. "Add FLS" fails specificity; "create column security profile on [field], restrict Read to [role]" passes.*

| Gap ID | Remediation | Dataverse Mechanism | Owner | Success Criteria |
|--------|------------|--------------------|----|-----------------|

---

### TABLE 8 — Defense-in-Depth Layer Analysis [SE | C-09]
*All four layers named and assessed. Enforcement point named for at least one operation.*

| Layer | Name | Assessed | Status | Enforcement Point? | Notes |
|-------|------|----------|---------|--------------------|-------|
| 1 | Environment / Admin Role | | | | |
| 2 | Security Role + BU Scope | | | | |
| 3 | Team Membership | | | | |
| 4 | FLS / Column Profiles | | | | |

**Enforcement point narrative** (required):
> [Operation] — access [granted/denied] at Layer [N] because [reason]. Layer [N-1] does not override because [reason].

---

### TABLE 9 — Role Delta Pre-Work [SE → CS handoff | C-10]
*SE documents raw divergence data for CS interpretation in TABLE 10.*

| Role A | Role B | Divergent Operations | FLS Divergence | Scope Divergence |
|--------|--------|---------------------|---------------|-----------------|

---

### TABLE 10 — Cross-Role Differential Analysis [CS | C-10]
*CS compares at least two roles side-by-side on one operation. States whether divergence is expected or anomalous.*

| Role Pair | Operation | Role A Access | Role B Access | Differential Expected? | CS Verdict |
|-----------|-----------|-------------|-------------|----------------------|-----------|

**CS Workflow Implication**:
> [For each anomalous differential: which agent or Power Automate workflow is affected? What user behavior change results?]

---

### CA FORMAT COMPLIANCE SECTIONS [CA — structural integrity only, no security content]

**CA mandate**: The following sections audit output structure only. CA uses the preamble enforcement matrix as its audit reference — not independent inspection. CA produces no security conclusions.

#### CA-1: Preamble Enforcement Matrix Cross-Reference Audit [C-15 | C-18]
*CA verifies each essential criterion by explicitly cross-referencing its preamble row. Each audit row starts with the criterion ID. A row with any FAIL entry means the triple-lock for that criterion is incomplete.*

| Criterion | Preamble Row | M1 Verified (table present + populated) | M2 Verified (SE sub-section assigned + used) | M3 Verified (SHALL in checklist + marked) | Triple-Lock Status |
|-----------|-------------|----------------------------------------|---------------------------------------------|------------------------------------------|-------------------|
| C-01 | TABLE 1 / SE-1 / SHALL A | | | | |
| C-02 | TABLE 2 / SE-2 / SHALL B | | | | |
| C-03 | TABLE 3 / SE-3 / SHALL C | | | | |
| C-04 | TABLE 4 / SE-4 / SHALL D | | | | |
| C-05 | TABLE 5 / SE-5 / SHALL E | | | | |

#### CA-2: Table Completeness and Blank-Cell Audit

| Section | All Columns Pre-Defined? | Blank Cells Found? | Count | Resolution Required |
|---------|--------------------------|-------------------|-------|---------------------|
| TABLE 1 | | | | |
| TABLE 2 | | | | |
| TABLE 3 | | | | |
| TABLE 4 | | | | |
| TABLE 5 | | | | |
| TABLEs 6–10 | | | | |

#### CA-3: Format Compliance Verdict
*CA verdict cites the preamble enforcement matrix explicitly before issuing the structural finding.*

> **FORMAT COMPLIANCE VERDICT**: [PASS / CONDITIONAL PASS / FAIL]
>
> Per preamble enforcement matrix (5 rows, 3 mechanism columns + CA audit point):
> Triple-lock status: [N of 5 essential criteria have all 3 mechanisms verified in CA-1]
> Sections complete: [N of 10 required tables present and populated]
> Blank-cell violations: [N found / none found]
>
> CA finding: [One-sentence structural verdict citing the preamble matrix. Independent of security findings. Example: "Per preamble enforcement matrix, all 5 essential criteria have all three mechanisms active; output is structurally complete with no blank-cell violations."]

---

### TERMINAL VERIFICATION CHECKLIST [C-12 | C-14]
*Each item names the accountable expert role. OPEN items attribute the failure to the responsible role.*

| # | Obligation | Status | Owner | Notes |
|---|-----------|--------|-------|-------|
| 1 | SHALL A — Role-operation matrix complete (C-01) | [ ] | SE | |
| 2 | SHALL B — FLS coverage + null case stated (C-02) | [ ] | SE | |
| 3 | SHALL C — Record scope assigned to all roles (C-03) | [ ] | SE | |
| 4 | SHALL D — All four escalation vectors checked (C-04) | [ ] | SE | |
| 5 | SHALL E — Gap inventory with evidence (C-05) | [ ] | SE | |
| 6 | Dataverse-native terminology throughout SE sections (C-06) | [ ] | SE | |
| 7 | Sharing rule conflict — at least one scenario evaluated (C-07) | [ ] | SE + CS | |
| 8 | Remediation specificity — at least 50% of gaps have specific steps (C-08) | [ ] | SE | |
| 9 | Defense-in-depth layers assessed; enforcement point named for at least one operation (C-09) | [ ] | SE | |
| 10 | Cross-role differential; anomalous items flagged (C-10) | [ ] | CS | |
| 11 | Triple-lock verified: all 5 essential criteria have 3 active mechanisms per CA-1 (C-15) | [ ] | CA | |
| 12 | All 10 sections present; all columns pre-defined; no blank cells (C-11) | [ ] | CA | |
| 13 | Format Compliance Verdict produced as independent CA section citing preamble matrix (C-16 | C-18) | [ ] | CA | |
| 14 | Every checklist item above names an accountable expert role (C-14) | [ ] | CA | |

---

## V-02

**Variation axis**: Output format — M1/M2/M3/M4 explicit column labeling in preamble (C-17 + C-18 column structure)
**Hypothesis**: R4 V-05 had four preamble columns but labeled them descriptively: "Pre-Printed Table Schema", "Expert Role Sub-Section", "SHALL Obligation", "CA Audit Point." C-18 requires the preamble matrix to expose four mechanisms with M1/M2/M3/M4 or equivalent labels. When column headers are labeled M1–M4, the audit model is explicit: CA-1 is an M4 verification, not a parallel audit. Renaming the preamble columns to M1/M2/M3/M4 with one-sentence mechanism definitions also makes the stated rule ("all four SHALL be active simultaneously") land on the actual column labels rather than descriptive prose. The single-axis test: does explicit Mx labeling in the preamble column headers increase the probability that CA-1 audits "per M4" rather than independently?

---

You are a Dataverse security specialist (SE) leading a three-role permissions trace with quad-lock criterion enforcement. Before any analysis section, a Compliance Auditor (CA) has co-authored the enforcement preamble mapping each essential criterion to four labeled mechanisms: M1 (format schema), M2 (role sub-section), M3 (SHALL obligation), M4 (CA verification row). All four SHALL be active simultaneously.

**Feature**: {{topic}}
**Roles in scope**: {{roles}} — default: Customer Service Representative, Customer Service Manager, System Administrator

---

## PREAMBLE: Quad-Lock Enforcement Matrix [C-15 | C-17 | C-18]

*Mechanism definitions:*
- *M1 — Pre-printed format schema: a table with pre-defined columns that SE fills in*
- *M2 — Expert role sub-section: the SE sub-section exclusively assigned to this criterion*
- *M3 — SHALL obligation: the named SHALL that the terminal checklist marks SATISFIED or OPEN*
- *M4 — CA verification row: the specific row in CA-1 where CA cross-references this criterion by ID*

*All four mechanisms SHALL be active simultaneously for each essential criterion. Treating any Mx as optional or as a fallback for another is a quad-lock failure.*

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01: Role-operation matrix | TABLE 1 — role × 8-op schema; blank cells prohibited | SE-1; Dataverse privilege terms required | SHALL A — complete matrix, all cells filled | CA-1, row C-01 |
| C-02: FLS coverage + null case | TABLE 2 — field × FLS schema + mandatory null case closing line | SE-2; column security profile terminology required | SHALL B — every sensitive field named; null case stated | CA-1, row C-02 |
| C-03: Record scope per role | TABLE 3 — role × scope schema; ambiguity flag column required | SE-3; BU / team-scoped Dataverse labels required | SHALL C — scope assigned to every role | CA-1, row C-03 |
| C-04: Escalation vector sweep | TABLE 4 — pre-printed 4-row schema; no row omissions | SE-4; all four named vectors checked | SHALL D — all vectors checked; CLEAN justified per row | CA-1, row C-04 |
| C-05: Gap inventory | TABLE 5 — gap registry schema; evidence row required for no-gap case | SE-5; specific field/role/rule per gap required | SHALL E — inventory produced; no-gap has explicit evidence | CA-1, row C-05 |

**Quad-lock enforcement rule**: For each essential criterion, all four mechanisms must be active simultaneously:
- M1: SE populates the pre-printed table schema
- M2: SE produces content within the assigned SE-N sub-section using Dataverse terminology
- M3: SE marks the corresponding SHALL SATISFIED in the terminal checklist
- M4: CA cross-references this criterion by ID in CA-1 using the row ID above

Using any mechanism in isolation or as a fallback for another is a quad-lock failure. CA operates by cross-referencing M1–M3 against this preamble matrix — CA does not audit by independent inspection.

---

**Expert Role Mandates**:

**SE — Security Engineer**
*Security content analysis. Dataverse-native terminology only: security roles, business units, column security profiles, owner teams / access teams, table permissions, sharing records, environment roles. No generic RBAC language.*
Owns: Tables 1–9, SHALLs A–E, Terminal checklist items 1–9

**CS — Customer Success Advisor**
*Independent agent-workflow and end-user access differential analysis.*
Owns: Table 10, Terminal checklist item 10

**CA — Compliance Auditor**
*Output structural integrity ONLY. CA does NOT make security conclusions, identify security gaps, or recommend remediation. CA audits by cross-referencing M1–M3 against the preamble quad-lock matrix. CA's M4 verification rows are pre-assigned in the preamble — CA fills them in; CA does not author new audit criteria.*
Owns: Sections CA-1, CA-2, CA-3, Terminal checklist items 11–14

**MANDATE BOUNDARY**: CA sections contain no security content. SE/CS sections contain no structural compliance verdicts. Cross-mandate language is a violation.

---

**Pre-flight rules**:
- **Blank-cell prohibition**: Every table cell SHALL carry an explicit value.
- **SHALL A** — Role-operation matrix complete, all cells filled
- **SHALL B** — Every sensitive field named with FLS status; null case stated
- **SHALL C** — Record access scope assigned to every role
- **SHALL D** — All four escalation vectors checked; CLEAN justified per row
- **SHALL E** — Gap inventory produced; no-gap case has explicit evidence

---

### TABLE 1 — Role-Operation Matrix [SE-1 | M1 for C-01 | SHALL A | Triple-Lock Active]
*M1 for C-01. All cells: Granted / Denied / Conditional / N/A — reason.*

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Notes |
|------|--------|------|-------|--------|--------|----------|--------|-------|-------|

---

### TABLE 2 — Field-Level Security Coverage [SE-2 | M1 for C-02 | SHALL B | Triple-Lock Active]
*M1 for C-02. All sensitive fields listed. "Not Configured" = finding.*

| Field | Sensitivity Reason | FLS Status | Column Security Profile | Gap? | Notes |
|-------|--------------------|------------|------------------------|------|-------|

**FLS Null Case** (SHALL B component — mandatory):
> FLS NULL CASE: [State whether any sensitive field lacks a column security profile.]

---

### TABLE 3 — Record Access Scope [SE-3 | M1 for C-03 | SHALL C | Triple-Lock Active]
*M1 for C-03. Scopes: Own / Business Unit / Parent-Child BU / Organization-Wide / Team-Scoped.*

| Role | Access Scope | BU Assignment | Team Modifier | Ambiguity Flag |
|------|-------------|---------------|--------------|----------------|

---

### TABLE 4 — Escalation Vector Sweep [SE-4 | M1 for C-04 | SHALL D | Triple-Lock Active]
*M1 for C-04. Pre-printed 4-row schema. CLEAN requires explicit justification.*

| Vector | Status | Mechanism | Scope Gained | Justification |
|--------|--------|-----------|-------------|---------------|
| Team membership inheritance | | | | |
| Sharing rule bypass of FLS | | | | |
| Impersonation / service account | | | | |
| Environment-level admin override | | | | |

---

### TABLE 5 — Security Gap Inventory [SE-5 | M1 for C-05 | SHALL E | Triple-Lock Active]
*M1 for C-05. Named gaps with specific element, or explicit no-gap evidence row.*

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

**CA instruction**: Audit by cross-referencing M1–M3 against the preamble quad-lock matrix above. The CA-1 rows below correspond to M4 verification rows pre-assigned in the preamble. Fill each row by checking the preamble's M1, M2, and M3 values against the actual output.

#### CA-1: Quad-Lock Verification (M4 rows — pre-assigned in preamble) [C-15 | C-18]
*Each row is a pre-assigned M4 verification row from the preamble. Fill by checking preamble M1–M3 against output.*

| Criterion | Preamble M1 Reference | M1 PASS? | Preamble M2 Reference | M2 PASS? | Preamble M3 Reference | M3 PASS? | Quad-Lock |
|-----------|----------------------|----------|----------------------|----------|-----------------------|----------|-----------|
| C-01 | TABLE 1 / role × 8-op / no blank cells | | SE-1 / Dataverse terms | | SHALL A / checklist row 1 | | |
| C-02 | TABLE 2 / field × FLS + null case | | SE-2 / column security profile terms | | SHALL B / checklist row 2 | | |
| C-03 | TABLE 3 / role × scope / ambiguity flag | | SE-3 / BU + team-scoped labels | | SHALL C / checklist row 3 | | |
| C-04 | TABLE 4 / 4-row schema / no omissions | | SE-4 / all 4 vectors named | | SHALL D / checklist row 4 | | |
| C-05 | TABLE 5 / gap registry / evidence row | | SE-5 / specific element per gap | | SHALL E / checklist row 5 | | |

#### CA-2: Table Completeness and Blank-Cell Audit

| Section | All Columns Pre-Defined? | Blank Cells Found? | Count | Resolution Required |
|---------|--------------------------|-------------------|-------|---------------------|
| TABLE 1 | | | | |
| TABLE 2 | | | | |
| TABLE 3 | | | | |
| TABLE 4 | | | | |
| TABLE 5 | | | | |
| TABLEs 6–10 | | | | |

#### CA-3: Format Compliance Verdict [C-16 | C-18]

> **FORMAT COMPLIANCE VERDICT**: [PASS / CONDITIONAL PASS / FAIL]
>
> Citing preamble quad-lock enforcement matrix (5 rows × M1/M2/M3/M4 columns):
> M4 verification complete: [N of 5 criteria have all 3 preamble references confirmed in CA-1]
> Sections complete: [N of 10 required tables present and populated]
> Blank-cell violations: [N found / none found]
>
> CA finding: [One-sentence structural verdict. Cites preamble matrix row results. Independent of security findings.]

---

### TERMINAL VERIFICATION CHECKLIST [C-12 | C-14]

| # | Obligation | Status | Owner | Notes |
|---|-----------|--------|-------|-------|
| 1 | SHALL A — Role-operation matrix complete (C-01) | [ ] | SE | |
| 2 | SHALL B — FLS coverage + null case stated (C-02) | [ ] | SE | |
| 3 | SHALL C — Record scope assigned to all roles (C-03) | [ ] | SE | |
| 4 | SHALL D — All four escalation vectors checked (C-04) | [ ] | SE | |
| 5 | SHALL E — Gap inventory with evidence (C-05) | [ ] | SE | |
| 6 | Dataverse-native terminology throughout SE sections (C-06) | [ ] | SE | |
| 7 | Sharing rule conflict — at least one scenario evaluated (C-07) | [ ] | SE + CS | |
| 8 | Remediation specificity — at least 50% of gaps have specific steps (C-08) | [ ] | SE | |
| 9 | Defense-in-depth layers assessed; enforcement point named (C-09) | [ ] | SE | |
| 10 | Cross-role differential; anomalous items flagged (C-10) | [ ] | CS | |
| 11 | Quad-lock verified: all 5 essential criteria have M1–M4 active per CA-1 (C-15 | C-18) | [ ] | CA | |
| 12 | All 10 sections present; all columns pre-defined; no blank cells (C-11) | [ ] | CA | |
| 13 | Format Compliance Verdict produced citing preamble quad-lock matrix (C-16) | [ ] | CA | |
| 14 | Every checklist item above names an accountable expert role (C-14) | [ ] | CA | |

---

## V-03

**Variation axis**: Role sequence — CA-first preamble authorship (C-17 + C-18 binding)
**Hypothesis**: In all R4 variations, SE ran first (producing analysis) and CA ran last (auditing the result). CA operating last creates a structural asymmetry: CA's audit references a preamble that SE wrote, and the model must reach backward to honor it. If CA runs first as the preamble author — declaring the enforcement matrix before any security analysis begins — the preamble is CA's artifact, not SE's backdrop. CA-authored preamble rows include pre-assigned M4 verification IDs that CA will fill in later; this makes the CA-1 cross-reference a completion of CA's own prior declaration rather than a retrospective audit. The test: does CA authoring the preamble increase the probability that CA-1 uses criterion-ID cross-reference language rather than independent inspection?

---

You are running a three-role permissions trace for {{topic}}. The execution order is: **CA declares the enforcement preamble → SE runs security analysis → CS runs differential analysis → CA completes its audit.** CA authors the enforcement contract first; SE and CS execute within it.

**Feature**: {{topic}}
**Roles in scope**: {{roles}} — default: Customer Service Representative, Customer Service Manager, System Administrator

---

**Expert Role Mandates**:

**CA — Compliance Auditor** *(runs first: preamble authorship and audit)*
*Mandate: Output structural integrity ONLY. CA does NOT make security conclusions, identify security gaps, or recommend remediation. CA authors the enforcement preamble matrix below, pre-assigns M4 verification rows, and completes those rows after SE and CS finish.*
Owns: PREAMBLE section, Sections CA-1 through CA-3, Terminal checklist items 11–14

**SE — Security Engineer** *(runs second: security analysis)*
*Mandate: Security content analysis. Dataverse-native terminology only: security roles, business units, column security profiles, owner teams / access teams, table permissions, sharing records, environment roles.*
Owns: Tables 1–9, SHALLs A–E, Terminal checklist items 1–9

**CS — Customer Success Advisor** *(runs third: differential analysis)*
*Mandate: Independent agent-workflow and end-user access differential analysis.*
Owns: Table 10, Terminal checklist item 10

**MANDATE BOUNDARY**: CA sections contain no security content. SE/CS sections contain no structural compliance verdicts.

---

## PREAMBLE [CA SECTION — authored by CA before SE begins] [C-15 | C-17 | C-18]

*CA declares the enforcement contract. Each essential criterion is mapped to three co-active mechanisms. CA pre-assigns the M4 verification row IDs that CA will complete after SE and CS finish. All three mechanisms SHALL be active simultaneously — not alternatives.*

| Criterion | M1: Pre-Printed Table Schema | M2: SE Sub-Section | M3: SHALL Obligation | M4 (pre-assigned): CA Verification Row ID |
|-----------|-----------------------------|--------------------|---------------------|------------------------------------------|
| C-01: Role-operation matrix | TABLE 1 | SE-1 | SHALL A | CA-1 / C-01 |
| C-02: FLS coverage + null case | TABLE 2 | SE-2 | SHALL B | CA-1 / C-02 |
| C-03: Record scope per role | TABLE 3 | SE-3 | SHALL C | CA-1 / C-03 |
| C-04: Escalation vector sweep | TABLE 4 | SE-4 | SHALL D | CA-1 / C-04 |
| C-05: Gap inventory | TABLE 5 | SE-5 | SHALL E | CA-1 / C-05 |

**CA enforcement declaration**: The above three mechanisms SHALL be simultaneously active for each essential criterion. SE SHALL populate each M1 table, produce content in each M2 sub-section using Dataverse-native terminology, and mark each M3 SHALL SATISFIED in the terminal checklist. CA will complete M4 verification rows CA-1/C-01 through CA-1/C-05 after SE and CS execute. An essential criterion is complete only when all four mechanism slots are filled.

---

**Pre-flight rules** (declared by CA, enforced by SE):
- **Blank-cell prohibition**: Every table cell SHALL carry an explicit value.
- **SHALL A** — Role-operation matrix complete, all cells filled (TABLE 1)
- **SHALL B** — Every sensitive field named with FLS status; null case stated (TABLE 2)
- **SHALL C** — Record access scope assigned to every role (TABLE 3)
- **SHALL D** — All four escalation vectors checked; CLEAN justified per row (TABLE 4)
- **SHALL E** — Gap inventory produced; no-gap case has explicit evidence (TABLE 5)

---

### TABLE 1 — Role-Operation Matrix [SE-1 | SHALL A | C-01]
*SE fills. All cells: Granted / Denied / Conditional / N/A — reason. CA will verify in CA-1/C-01.*

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Notes |
|------|--------|------|-------|--------|--------|----------|--------|-------|-------|

---

### TABLE 2 — Field-Level Security Coverage [SE-2 | SHALL B | C-02]
*SE fills. All sensitive fields listed. "Not Configured" = finding. CA will verify in CA-1/C-02.*

| Field | Sensitivity Reason | FLS Status | Column Security Profile | Gap? | Notes |
|-------|--------------------|------------|------------------------|------|-------|

**FLS Null Case** (SHALL B component — mandatory):
> FLS NULL CASE: [State whether any sensitive field lacks a column security profile.]

---

### TABLE 3 — Record Access Scope [SE-3 | SHALL C | C-03]
*SE fills. Scopes: Own / Business Unit / Parent-Child BU / Organization-Wide / Team-Scoped. CA will verify in CA-1/C-03.*

| Role | Access Scope | BU Assignment | Team Modifier | Ambiguity Flag |
|------|-------------|---------------|--------------|----------------|

---

### TABLE 4 — Escalation Vector Sweep [SE-4 | SHALL D | C-04]
*SE fills. All four vectors. CLEAN requires explicit justification. CA will verify in CA-1/C-04.*

| Vector | Status | Mechanism | Scope Gained | Justification |
|--------|--------|-----------|-------------|---------------|
| Team membership inheritance | | | | |
| Sharing rule bypass of FLS | | | | |
| Impersonation / service account | | | | |
| Environment-level admin override | | | | |

---

### TABLE 5 — Security Gap Inventory [SE-5 | SHALL E | C-05]
*SE fills. Named gaps with specific element, or explicit no-gap evidence row. CA will verify in CA-1/C-05.*

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

### CA FORMAT COMPLIANCE SECTIONS [CA — completes M4 rows pre-declared in preamble]

**CA instruction**: CA now completes the M4 verification rows pre-assigned in the PREAMBLE. For each essential criterion, locate the preamble row, check whether M1 (table), M2 (SE sub-section), and M3 (SHALL) were satisfied, and write the verdict in the criterion-ID-prefixed row below. CA does not introduce new audit criteria here — CA completes the contract declared above.

#### CA-1: M4 Verification Rows [C-15 | C-18]
*Pre-assigned M4 rows from the preamble. CA fills by checking M1, M2, M3 against the preamble declaration.*

- **C-01 (CA-1/C-01)**: TABLE 1 present with all cells filled (M1) | SE-1 produced with Dataverse privilege terms (M2) | SHALL A marked SATISFIED in checklist (M3) → Verdict: [PASS / FAIL / PARTIAL — reason]
- **C-02 (CA-1/C-02)**: TABLE 2 present with all sensitive fields listed + null case stated (M1) | SE-2 produced with column security profile terms (M2) | SHALL B marked SATISFIED in checklist (M3) → Verdict: [PASS / FAIL / PARTIAL — reason]
- **C-03 (CA-1/C-03)**: TABLE 3 present with scope assigned to every role (M1) | SE-3 produced with BU/team-scoped Dataverse labels (M2) | SHALL C marked SATISFIED in checklist (M3) → Verdict: [PASS / FAIL / PARTIAL — reason]
- **C-04 (CA-1/C-04)**: TABLE 4 present with all 4 rows filled + CLEAN justified (M1) | SE-4 produced with all four named vectors (M2) | SHALL D marked SATISFIED in checklist (M3) → Verdict: [PASS / FAIL / PARTIAL — reason]
- **C-05 (CA-1/C-05)**: TABLE 5 present with named gaps or explicit no-gap evidence row (M1) | SE-5 produced with specific field/role/rule per gap (M2) | SHALL E marked SATISFIED in checklist (M3) → Verdict: [PASS / FAIL / PARTIAL — reason]

#### CA-2: Table Completeness and Blank-Cell Audit

| Section | All Columns Pre-Defined? | Blank Cells Found? | Count | Resolution Required |
|---------|--------------------------|-------------------|-------|---------------------|
| TABLE 1 | | | | |
| TABLE 2 | | | | |
| TABLE 3 | | | | |
| TABLE 4 | | | | |
| TABLE 5 | | | | |
| TABLEs 6–10 | | | | |

#### CA-3: Format Compliance Verdict [C-16 | C-18]
*CA verdict cites the preamble enforcement contract authored above.*

> **FORMAT COMPLIANCE VERDICT**: [PASS / CONDITIONAL PASS / FAIL]
>
> Per preamble enforcement matrix (CA-authored, 5 rows × M1/M2/M3/M4 columns):
> M4 completion: [N of 5 CA-1 verification rows completed with PASS verdict]
> Sections complete: [N of 10 required tables present]
> Blank-cell violations: [N found / none found]
>
> CA finding: [One-sentence structural verdict. References preamble enforcement matrix by name. Independent of security findings.]

---

### TERMINAL VERIFICATION CHECKLIST [C-12 | C-14]

| # | Obligation | Status | Owner | Notes |
|---|-----------|--------|-------|-------|
| 1 | SHALL A — Role-operation matrix complete (C-01) | [ ] | SE | |
| 2 | SHALL B — FLS coverage + null case stated (C-02) | [ ] | SE | |
| 3 | SHALL C — Record scope assigned to all roles (C-03) | [ ] | SE | |
| 4 | SHALL D — All four escalation vectors checked (C-04) | [ ] | SE | |
| 5 | SHALL E — Gap inventory with evidence (C-05) | [ ] | SE | |
| 6 | Dataverse-native terminology throughout SE sections (C-06) | [ ] | SE | |
| 7 | Sharing rule conflict — at least one scenario evaluated (C-07) | [ ] | SE + CS | |
| 8 | Remediation specificity — at least 50% specific (C-08) | [ ] | SE | |
| 9 | Defense-in-depth layers assessed; enforcement point named (C-09) | [ ] | SE | |
| 10 | Cross-role differential; anomalous items flagged (C-10) | [ ] | CS | |
| 11 | All M4 verification rows completed; quad-lock verified for all 5 essential criteria (C-15 | C-18) | [ ] | CA | |
| 12 | All 10 sections present; all columns pre-defined; no blank cells (C-11) | [ ] | CA | |
| 13 | Format Compliance Verdict produced citing preamble enforcement matrix (C-16) | [ ] | CA | |
| 14 | Every checklist item above names an accountable expert role (C-14) | [ ] | CA | |

---

## V-04

**Variation axis**: Output format × Lifecycle emphasis — schema registry + preamble reaffirmation
**Hypothesis**: Two R4 failure patterns remain. First: CA audits by inspection when the preamble's M1 column says "TABLE 1 — role × 8-op schema" but CA-1 asks "Table Present and Populated?" — the audit question is generic and doesn't require reading the preamble. Second: preamble drift — the model declares the preamble correctly but by the time CA runs its audit sections, the preamble has scrolled out of the model's active attention. This variation attacks both with two lifecycle changes: (1) a Schema Registry section immediately after the preamble pre-prints all 10 table schemas by name so that M1 references resolve to numbered registry entries; (2) a Preamble Reaffirmation step at the start of CA-1 where CA quotes the relevant preamble row before auditing each criterion. Together these reduce the gap between preamble declaration and CA audit completion.

---

You are a Dataverse security specialist (SE) leading a three-role permissions trace. The execution structure has four phases: (1) Preamble enforcement declaration, (2) Schema registry (all table schemas pre-printed), (3) Security analysis by SE and CS, (4) CA audit with preamble reaffirmation. Every essential criterion is co-enforced by four mechanisms declared in the preamble and verified by CA using criterion-ID cross-references.

**Feature**: {{topic}}
**Roles in scope**: {{roles}} — default: Customer Service Representative, Customer Service Manager, System Administrator

---

## PHASE 1 — PREAMBLE: Quad-Lock Enforcement Matrix [C-15 | C-17 | C-18]

*Before any analysis section, this table binds each essential criterion to four co-active enforcement mechanisms. M4 pre-assigns the CA-1 verification row ID that CA will complete after SE and CS finish. All four mechanisms SHALL be active simultaneously.*

| Criterion | M1: Schema Registry Entry | M2: SE Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|--------------------------|-------------------|---------------------|------------------------|
| C-01: Role-operation matrix | SR-1 (role × 8-op, blank cells prohibited) | SE-1; Dataverse privilege terms | SHALL A | CA-1 row "C-01:" |
| C-02: FLS coverage + null case | SR-2 (field × FLS + mandatory null case line) | SE-2; column security profile terms | SHALL B | CA-1 row "C-02:" |
| C-03: Record scope per role | SR-3 (role × scope + ambiguity flag) | SE-3; BU/team-scoped Dataverse labels | SHALL C | CA-1 row "C-03:" |
| C-04: Escalation vector sweep | SR-4 (pre-printed 4-row, no omissions) | SE-4; all four named vectors | SHALL D | CA-1 row "C-04:" |
| C-05: Gap inventory | SR-5 (gap registry; evidence row for no-gap) | SE-5; specific field/role/rule per gap | SHALL E | CA-1 row "C-05:" |

**Enforcement rule**: All four mechanisms SHALL be simultaneously active. M4 is not a post-hoc check — it is the fourth co-active mechanism, pre-assigned here before analysis begins.

---

## PHASE 2 — SCHEMA REGISTRY [pre-printed table structures — SE populates these in Phase 3]

*All table schemas are pre-defined here. SE SHALL populate each schema in the numbered section below. Blank cells are prohibited in all schemas.*

**SR-1 — Role-Operation Matrix schema**:
| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Notes |
|------|--------|------|-------|--------|--------|----------|--------|-------|-------|
*(SE populates in TABLE 1)*

**SR-2 — Field-Level Security Coverage schema**:
| Field | Sensitivity Reason | FLS Status | Column Security Profile | Gap? | Notes |
|-------|--------------------|------------|------------------------|------|-------|
*(SE populates in TABLE 2; mandatory null case closing line: "FLS NULL CASE: ...")*

**SR-3 — Record Access Scope schema**:
| Role | Access Scope | BU Assignment | Team Modifier | Ambiguity Flag |
|------|-------------|---------------|--------------|----------------|
*(SE populates in TABLE 3)*

**SR-4 — Escalation Vector Sweep schema** (4 rows pre-printed; no omissions):
| Vector | Status | Mechanism | Scope Gained | Justification |
|--------|--------|-----------|-------------|---------------|
| Team membership inheritance | | | | |
| Sharing rule bypass of FLS | | | | |
| Impersonation / service account | | | | |
| Environment-level admin override | | | | |
*(SE populates in TABLE 4)*

**SR-5 — Security Gap Inventory schema**:
| Gap ID | Description | Type | Affected Element | Severity |
|--------|------------|------|-----------------|----------|
*(SE populates in TABLE 5; if no gaps, write evidence row: "G-00 | No gaps found | N/A | N/A — [evidence] | N/A")*

---

**Expert Role Mandates**:

**SE — Security Engineer**
*Security content analysis. Dataverse-native terminology only. Uses schema registry entries SR-1 through SR-5 as pre-defined formats for Tables 1–5.*
Owns: Tables 1–9, SHALLs A–E, Terminal checklist items 1–9

**CS — Customer Success Advisor**
*Independent agent-workflow and end-user access differential analysis.*
Owns: Table 10, Terminal checklist item 10

**CA — Compliance Auditor**
*Output structural integrity ONLY. No security conclusions. In CA-1, CA reaffirms each preamble row before issuing its verification verdict for that criterion — CA audits by preamble cross-reference, not by independent inspection.*
Owns: Sections CA-1, CA-2, CA-3, Terminal checklist items 11–14

---

## PHASE 3 — SECURITY ANALYSIS

**Pre-flight rules**:
- **Blank-cell prohibition**: Every table cell SHALL carry an explicit value.
- **SHALL A** — TABLE 1 complete (SR-1 format), all cells filled
- **SHALL B** — TABLE 2 complete (SR-2 format), every sensitive field named, null case stated
- **SHALL C** — TABLE 3 complete (SR-3 format), scope assigned to every role
- **SHALL D** — TABLE 4 complete (SR-4 format), all four vectors checked, CLEAN justified
- **SHALL E** — TABLE 5 complete (SR-5 format), named gaps or explicit evidence row

---

### TABLE 1 — Role-Operation Matrix [SE-1 | SHALL A | C-01]
*Use SR-1 schema. All cells filled.*

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Notes |
|------|--------|------|-------|--------|--------|----------|--------|-------|-------|

---

### TABLE 2 — Field-Level Security Coverage [SE-2 | SHALL B | C-02]
*Use SR-2 schema. All sensitive fields listed.*

| Field | Sensitivity Reason | FLS Status | Column Security Profile | Gap? | Notes |
|-------|--------------------|------------|------------------------|------|-------|

**FLS Null Case** (SHALL B component — mandatory):
> FLS NULL CASE: [State whether any sensitive field lacks a column security profile.]

---

### TABLE 3 — Record Access Scope [SE-3 | SHALL C | C-03]
*Use SR-3 schema.*

| Role | Access Scope | BU Assignment | Team Modifier | Ambiguity Flag |
|------|-------------|---------------|--------------|----------------|

---

### TABLE 4 — Escalation Vector Sweep [SE-4 | SHALL D | C-04]
*Use SR-4 schema. All 4 rows. CLEAN requires justification.*

| Vector | Status | Mechanism | Scope Gained | Justification |
|--------|--------|-----------|-------------|---------------|
| Team membership inheritance | | | | |
| Sharing rule bypass of FLS | | | | |
| Impersonation / service account | | | | |
| Environment-level admin override | | | | |

---

### TABLE 5 — Security Gap Inventory [SE-5 | SHALL E | C-05]
*Use SR-5 schema. Named gaps or explicit evidence row.*

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

## PHASE 4 — CA AUDIT [CA — preamble reaffirmation + structural verification]

**CA instruction**: For each criterion in CA-1, reaffirm the preamble row first (quote M1/M2/M3/M4 values from the preamble), then verify whether each mechanism was satisfied. Audit by preamble cross-reference — not by independent inspection.

### CA-1: Preamble Reaffirmation + Verification [C-15 | C-17 | C-18]

**C-01 reaffirmation** (from preamble): M1 = SR-1 (TABLE 1); M2 = SE-1; M3 = SHALL A; M4 = this row.
> C-01 verification: TABLE 1 present with all cells filled [PASS/FAIL] | SE-1 produced with Dataverse privilege terms [PASS/FAIL] | SHALL A in checklist [PASS/FAIL] → C-01 quad-lock: [COMPLETE / PARTIAL — which mechanism failed]

**C-02 reaffirmation** (from preamble): M1 = SR-2 (TABLE 2); M2 = SE-2; M3 = SHALL B; M4 = this row.
> C-02 verification: TABLE 2 present + null case stated [PASS/FAIL] | SE-2 produced with column security profile terms [PASS/FAIL] | SHALL B in checklist [PASS/FAIL] → C-02 quad-lock: [COMPLETE / PARTIAL — which mechanism failed]

**C-03 reaffirmation** (from preamble): M1 = SR-3 (TABLE 3); M2 = SE-3; M3 = SHALL C; M4 = this row.
> C-03 verification: TABLE 3 present + scope for every role [PASS/FAIL] | SE-3 produced with BU/team-scoped labels [PASS/FAIL] | SHALL C in checklist [PASS/FAIL] → C-03 quad-lock: [COMPLETE / PARTIAL — which mechanism failed]

**C-04 reaffirmation** (from preamble): M1 = SR-4 (TABLE 4); M2 = SE-4; M3 = SHALL D; M4 = this row.
> C-04 verification: TABLE 4 present + all 4 rows + CLEAN justified [PASS/FAIL] | SE-4 produced with all four named vectors [PASS/FAIL] | SHALL D in checklist [PASS/FAIL] → C-04 quad-lock: [COMPLETE / PARTIAL — which mechanism failed]

**C-05 reaffirmation** (from preamble): M1 = SR-5 (TABLE 5); M2 = SE-5; M3 = SHALL E; M4 = this row.
> C-05 verification: TABLE 5 present + named gaps or evidence row [PASS/FAIL] | SE-5 produced with specific element per gap [PASS/FAIL] | SHALL E in checklist [PASS/FAIL] → C-05 quad-lock: [COMPLETE / PARTIAL — which mechanism failed]

### CA-2: Table Completeness and Blank-Cell Audit

| Section | All Columns Pre-Defined? | Blank Cells Found? | Count | Resolution Required |
|---------|--------------------------|-------------------|-------|---------------------|
| TABLE 1 | | | | |
| TABLE 2 | | | | |
| TABLE 3 | | | | |
| TABLE 4 | | | | |
| TABLE 5 | | | | |
| TABLEs 6–10 | | | | |

### CA-3: Format Compliance Verdict [C-16 | C-18]

> **FORMAT COMPLIANCE VERDICT**: [PASS / CONDITIONAL PASS / FAIL]
>
> Per preamble quad-lock enforcement matrix (Phase 1, 5 rows × M1/M2/M3/M4 columns):
> CA-1 reaffirmation complete: [N of 5 criteria verified with explicit preamble row reaffirmation]
> Quad-lock complete: [N of 5 essential criteria have all 4 mechanisms confirmed]
> Blank-cell violations: [N found / none found]
>
> CA finding: [One-sentence structural verdict. References preamble enforcement matrix by phase and row count. Independent of security findings.]

---

### TERMINAL VERIFICATION CHECKLIST [C-12 | C-14]

| # | Obligation | Status | Owner | Notes |
|---|-----------|--------|-------|-------|
| 1 | SHALL A — Role-operation matrix complete (C-01) | [ ] | SE | |
| 2 | SHALL B — FLS coverage + null case stated (C-02) | [ ] | SE | |
| 3 | SHALL C — Record scope assigned to all roles (C-03) | [ ] | SE | |
| 4 | SHALL D — All four escalation vectors checked (C-04) | [ ] | SE | |
| 5 | SHALL E — Gap inventory with evidence (C-05) | [ ] | SE | |
| 6 | Dataverse-native terminology throughout SE sections (C-06) | [ ] | SE | |
| 7 | Sharing rule conflict — at least one scenario evaluated (C-07) | [ ] | SE + CS | |
| 8 | Remediation specificity — at least 50% specific (C-08) | [ ] | SE | |
| 9 | Defense-in-depth layers assessed; enforcement point named (C-09) | [ ] | SE | |
| 10 | Cross-role differential; anomalous items flagged (C-10) | [ ] | CS | |
| 11 | Quad-lock verified for all 5 essential criteria via CA-1 preamble reaffirmation (C-15 | C-18) | [ ] | CA | |
| 12 | All 10 sections present; schema registry entries used; no blank cells (C-11) | [ ] | CA | |
| 13 | Format Compliance Verdict citing preamble enforcement matrix (C-16) | [ ] | CA | |
| 14 | Every checklist item above names an accountable expert role (C-14) | [ ] | CA | |

---

## V-05

**Variation axis**: Role sequence × Output format × Phrasing register × Lifecycle emphasis — full quad-lock integration targeting C-17 + C-18 simultaneously
**Hypothesis**: The full integration attempts C-17 + C-18 as a unified system. C-17 requires the preamble to have 3+ mechanism columns and a stated "all three SHALL be active simultaneously" rule. C-18 requires a fourth column (CA verification), criterion-ID-prefixed CA-1 rows, and CA-3 citing the preamble. The failure mode for V-03 in R4 (which PASSed C-15 but may have PARTIAL C-17): the preamble had columns labeled descriptively and the "simultaneously" rule was present but the M4 column was labeled "CA Audit Point" — not "M4: CA Verification Row." This variation combines: (1) CA-first role sequence so preamble is CA's authored contract; (2) M1/M2/M3/M4 explicit column headers with mechanism definitions; (3) imperative phrasing throughout all sections with no conditional language; (4) CA-1 uses criterion-ID-prefixed rows with explicit preamble row citations; (5) CA-3 opens "Citing preamble enforcement matrix (Phase 1, 5 rows × M1/M2/M3/M4)." The hypothesis: all four Mx mechanisms named, all four axes active, C-17 and C-18 both addressable in a single execution.

---

You are running a Dataverse permissions trace with quad-lock criterion enforcement. Execution proceeds in four phases: CA authors the enforcement contract, SE produces security analysis, CS produces differential analysis, CA completes verification. Every essential criterion is bound to four co-active mechanisms (M1/M2/M3/M4). No mechanism is optional. No mechanism substitutes for another.

**Feature**: {{topic}}
**Roles in scope**: {{roles}} — default: Customer Service Representative, Customer Service Manager, System Administrator

---

**Expert Role Mandates** (declared before preamble):

**CA — Compliance Auditor** *(Phase 1 and Phase 4)*
Mandate: Output structural integrity ONLY. CA does NOT produce security analysis, identify security gaps, or recommend remediation. In Phase 1, CA authors the enforcement preamble. In Phase 4, CA completes M4 verification rows using criterion-ID cross-references, then issues a format compliance verdict citing the preamble by name.
Owns: PREAMBLE, Sections CA-1 through CA-3, Terminal checklist items 11–14

**SE — Security Engineer** *(Phase 3)*
Mandate: Security content analysis. SHALL use Dataverse-native terminology exclusively: security roles, business units, column security profiles, owner teams / access teams, table permissions, sharing records, environment roles. Generic terms ("group", "permission level") without Dataverse mapping are precision failures.
Owns: Tables 1–9, SHALLs A–E, Terminal checklist items 1–9

**CS — Customer Success Advisor** *(Phase 3)*
Mandate: Independent agent-workflow and end-user access differential analysis.
Owns: Table 10, Terminal checklist item 10

**MANDATE BOUNDARY**: CA sections SHALL NOT contain security conclusions, gap findings, or remediation. SE/CS sections SHALL NOT contain structural compliance verdicts.

---

## PHASE 1 — PREAMBLE [CA authors] [C-15 | C-17 | C-18]

*Mechanism definitions (these labels SHALL appear throughout this output):*
- **M1** — Pre-printed format schema: a pre-defined table structure that SE fills in; blank cells are prohibited
- **M2** — Expert role sub-section: the SE-N sub-section exclusively assigned to this criterion; Dataverse terminology required
- **M3** — SHALL obligation: the named SHALL that terminal checklist row N marks SATISFIED or OPEN
- **M4** — CA verification row: the criterion-ID-prefixed row in CA-1 where CA cross-references this criterion against M1, M2, and M3

*All four mechanisms SHALL be active simultaneously for every essential criterion. M4 is the fourth co-active mechanism, not a post-hoc check. Using any Mx as optional or as a fallback for another is a quad-lock failure.*

| Criterion | M1: Pre-Printed Schema | M2: SE Sub-Section | M3: SHALL | M4: CA Verification Row |
|-----------|----------------------|-------------------|-----------|------------------------|
| C-01: Role-operation matrix | TABLE 1 — role × Create/Read/Write/Delete/Append/AppendTo/Assign/Share; blank cells prohibited | SE-1 — Dataverse privilege terminology required | SHALL A — checklist row 1 | CA-1 row "C-01:" |
| C-02: FLS coverage + null case | TABLE 2 — field × FLS status + mandatory null case closing line | SE-2 — column security profile terminology required | SHALL B — checklist row 2 | CA-1 row "C-02:" |
| C-03: Record scope per role | TABLE 3 — role × Own/BU/Parent-Child BU/Org-Wide/Team-Scoped + ambiguity flag column | SE-3 — Dataverse scope labels required (BU, team-scoped, not "department" or "group") | SHALL C — checklist row 3 | CA-1 row "C-03:" |
| C-04: Escalation vector sweep | TABLE 4 — pre-printed 4-row schema: team inheritance / sharing bypass / impersonation / env-admin; no row omissions | SE-4 — all four vectors named; CLEAN requires explicit justification per row | SHALL D — checklist row 4 | CA-1 row "C-04:" |
| C-05: Security gap inventory | TABLE 5 — gap registry with Gap ID / Description / Type / Affected Element / Severity; no-gap requires evidence row | SE-5 — specific field/role/rule per gap; not generic ("missing FLS" fails; "missing FLS on creditlimit" passes) | SHALL E — checklist row 5 | CA-1 row "C-05:" |

**Quad-lock enforcement rule declared by CA**: Every essential criterion SHALL have all four mechanisms active. SE SHALL populate each M1 schema, produce content in each M2 sub-section using Dataverse terminology, and mark each M3 SHALL in the terminal checklist. CA SHALL complete each M4 verification row in CA-1 using criterion-ID cross-references, and SHALL issue CA-3 citing this preamble matrix by name. A criterion with any mechanism inactive is a quad-lock failure.

---

## PHASE 2 — PRE-FLIGHT RULES [effective for all SE sections]

- **Blank-cell prohibition**: Every table cell SHALL carry an explicit value. Permitted nulls: "Not Configured", "None Found", "N/A — [reason]". A blank cell is omission evidence.
- **SHALL A** — TABLE 1 complete, all cells filled (Granted/Denied/Conditional/N/A)
- **SHALL B** — TABLE 2 complete, every sensitive field named with FLS status, null case stated
- **SHALL C** — TABLE 3 complete, access scope assigned to every role in scope
- **SHALL D** — TABLE 4 complete, all four vectors checked, CLEAN justified per row
- **SHALL E** — TABLE 5 complete, named gaps with specific element, or explicit evidence row

---

## PHASE 3 — SECURITY ANALYSIS [SE, then CS]

### TABLE 1 — Role-Operation Matrix [SE-1 | M1 for C-01 | SHALL A]
*SE fills. M1: pre-printed schema. M2: SE-1. M3: SHALL A. CA will complete M4 in CA-1 row "C-01:".*
*All cells: Granted / Denied / Conditional / N/A — reason. No blank cells.*

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Notes |
|------|--------|------|-------|--------|--------|----------|--------|-------|-------|

---

### TABLE 2 — Field-Level Security Coverage [SE-2 | M1 for C-02 | SHALL B]
*SE fills. M1: pre-printed schema. M2: SE-2. M3: SHALL B. CA will complete M4 in CA-1 row "C-02:".*
*All sensitive fields listed. "Not Configured" = finding, not omission.*

| Field | Sensitivity Reason | FLS Status | Column Security Profile | Gap? | Notes |
|-------|--------------------|------------|------------------------|------|-------|

**FLS Null Case** (SHALL B component — mandatory, no exceptions):
> FLS NULL CASE: [State whether any sensitive field lacks a column security profile. If none configured: "No column security profiles configured. Gap confirmed."]

---

### TABLE 3 — Record Access Scope [SE-3 | M1 for C-03 | SHALL C]
*SE fills. M1: pre-printed schema. M2: SE-3. M3: SHALL C. CA will complete M4 in CA-1 row "C-03:".*
*Scopes: Own / Business Unit / Parent-Child BU / Organization-Wide / Team-Scoped. Ambiguous = gap, not blank.*

| Role | Access Scope | BU Assignment | Team Modifier | Ambiguity Flag |
|------|-------------|---------------|--------------|----------------|

---

### TABLE 4 — Escalation Vector Sweep [SE-4 | M1 for C-04 | SHALL D]
*SE fills. M1: pre-printed 4-row schema. M2: SE-4. M3: SHALL D. CA will complete M4 in CA-1 row "C-04:".*
*All four rows required. CLEAN requires explicit justification — unchecked = OPEN.*

| Vector | Status | Mechanism | Scope Gained | Justification |
|--------|--------|-----------|-------------|---------------|
| Team membership inheritance | | | | |
| Sharing rule bypass of FLS | | | | |
| Impersonation / service account | | | | |
| Environment-level admin override | | | | |

---

### TABLE 5 — Security Gap Inventory [SE-5 | M1 for C-05 | SHALL E]
*SE fills. M1: pre-printed schema. M2: SE-5. M3: SHALL E. CA will complete M4 in CA-1 row "C-05:".*
*Named gaps with specific field/role/rule. No gaps: write evidence row with Gap ID "G-00".*

| Gap ID | Description | Type | Affected Element | Severity |
|--------|------------|------|-----------------|----------|

---

### TABLE 6 — Sharing Rule Conflict Analysis [SE + CS | C-07]
*At least one sharing scenario evaluated for role-level or FLS conflict.*

| Sharing Rule | Type | Role-Level Access | FLS State | Conflict? | Description |
|-------------|------|------------------|-----------|-----------|-------------|

---

### TABLE 7 — Remediation Register [SE | C-08]
*Specific Dataverse-mechanism remediation per gap. Specificity required: name the column security profile, the role, and the privilege.*

| Gap ID | Remediation | Dataverse Mechanism | Owner | Success Criteria |
|--------|------------|--------------------|----|-----------------|

---

### TABLE 8 — Defense-in-Depth Layer Analysis [SE | C-09]
*All four Dataverse security layers assessed. Name the effective enforcement point for at least one operation.*

| Layer | Name | Assessed | Status | Enforcement Point? | Notes |
|-------|------|----------|---------|--------------------|-------|
| 1 | Environment / Admin Role | | | | |
| 2 | Security Role + BU Scope | | | | |
| 3 | Team Membership | | | | |
| 4 | FLS / Column Profiles | | | | |

**Enforcement point narrative** (required — at least one operation):
> [Operation] — access [granted/denied] at Layer [N] because [reason]. Layer [N-1] does not override because [reason].

---

### TABLE 9 — Role Delta Pre-Work [SE → CS handoff | C-10]
*SE documents raw divergence data for CS interpretation.*

| Role A | Role B | Divergent Operations | FLS Divergence | Scope Divergence |
|--------|--------|---------------------|---------------|-----------------|

---

### TABLE 10 — Cross-Role Differential Analysis [CS | C-10]
*CS compares at least two roles. States whether divergence is expected (least-privilege satisfied) or anomalous.*

| Role Pair | Operation | Role A Access | Role B Access | Differential Expected? | CS Verdict |
|-----------|-----------|-------------|-------------|----------------------|-----------|

**CS Workflow Implication**:
> [For each anomalous differential: which agent or Power Automate workflow is affected? What user behavior change results?]

---

## PHASE 4 — CA AUDIT [CA completes M4 verification rows and issues compliance verdict]

**CA instruction**: Complete M4 rows CA-1/"C-01:" through CA-1/"C-05:" by cross-referencing the preamble enforcement matrix (Phase 1). Each row is labeled with its criterion ID. For each row: quote the M1, M2, and M3 preamble values, check whether each was satisfied, and issue a verdict. Issue CA-3 citing the preamble matrix by phase and row count. No security conclusions in any CA section.

### CA-1: M4 Criterion-ID Cross-Reference Rows [C-15 | C-18]

- **C-01:** TABLE 1 (M1: role × 8-op schema, blank cells prohibited) [PASS/FAIL] | SE-1 with Dataverse privilege terms (M2) [PASS/FAIL] | SHALL A in checklist row 1 (M3) [PASS/FAIL] → **C-01 quad-lock: [COMPLETE / PARTIAL — state which Mx failed]**

- **C-02:** TABLE 2 (M1: field × FLS + null case closing line) [PASS/FAIL] | SE-2 with column security profile terminology (M2) [PASS/FAIL] | SHALL B in checklist row 2 (M3) [PASS/FAIL] → **C-02 quad-lock: [COMPLETE / PARTIAL — state which Mx failed]**

- **C-03:** TABLE 3 (M1: role × Dataverse scope labels + ambiguity flag) [PASS/FAIL] | SE-3 with BU/team-scoped labels (M2) [PASS/FAIL] | SHALL C in checklist row 3 (M3) [PASS/FAIL] → **C-03 quad-lock: [COMPLETE / PARTIAL — state which Mx failed]**

- **C-04:** TABLE 4 (M1: 4-row schema, no omissions, CLEAN justified) [PASS/FAIL] | SE-4 with all four named vectors (M2) [PASS/FAIL] | SHALL D in checklist row 4 (M3) [PASS/FAIL] → **C-04 quad-lock: [COMPLETE / PARTIAL — state which Mx failed]**

- **C-05:** TABLE 5 (M1: gap registry or evidence row for no-gap) [PASS/FAIL] | SE-5 with specific field/role/rule per gap (M2) [PASS/FAIL] | SHALL E in checklist row 5 (M3) [PASS/FAIL] → **C-05 quad-lock: [COMPLETE / PARTIAL — state which Mx failed]**

### CA-2: Table Completeness and Blank-Cell Audit

| Section | All Columns Pre-Defined? | Blank Cells Found? | Count | Resolution Required |
|---------|--------------------------|-------------------|-------|---------------------|
| TABLE 1 | | | | |
| TABLE 2 | | | | |
| TABLE 3 | | | | |
| TABLE 4 | | | | |
| TABLE 5 | | | | |
| TABLEs 6–10 | | | | |

### CA-3: Format Compliance Verdict [C-16 | C-17 | C-18]

> **FORMAT COMPLIANCE VERDICT**: [PASS / CONDITIONAL PASS / FAIL]
>
> Citing preamble enforcement matrix (Phase 1, 5 rows × M1/M2/M3/M4 columns):
> M4 verification complete: [N of 5 criterion-ID rows completed in CA-1 / expected: 5 of 5]
> Quad-lock complete: [N of 5 essential criteria have all four mechanisms confirmed]
> Sections present: [N of 10 required tables / expected: 10 of 10]
> Blank-cell violations: [N found / expected: 0]
>
> CA finding: [One-sentence structural verdict. MUST cite the preamble enforcement matrix by phase reference. MUST state whether all M4 rows were completed. MUST be independent of security findings.]

---

### TERMINAL VERIFICATION CHECKLIST [C-12 | C-14]
*Each item names the accountable expert role. OPEN items identify both the gap and the responsible role. No item SHALL have an empty Owner column.*

| # | Obligation | Status | Owner | Notes |
|---|-----------|--------|-------|-------|
| 1 | SHALL A — TABLE 1 complete, all cells filled (C-01) | [ ] | SE | |
| 2 | SHALL B — TABLE 2 complete, all sensitive fields named, null case stated (C-02) | [ ] | SE | |
| 3 | SHALL C — TABLE 3 complete, scope assigned to every role (C-03) | [ ] | SE | |
| 4 | SHALL D — TABLE 4 complete, all four vectors checked, CLEAN justified (C-04) | [ ] | SE | |
| 5 | SHALL E — TABLE 5 complete, named gaps or explicit evidence row (C-05) | [ ] | SE | |
| 6 | Dataverse-native terminology throughout all SE sections — no generic RBAC substitution (C-06) | [ ] | SE | |
| 7 | Sharing rule conflict — at least one scenario evaluated at role-level and FLS intersection (C-07) | [ ] | SE + CS | |
| 8 | Remediation specificity — at least 50% of gaps have named column security profile, role, and privilege (C-08) | [ ] | SE | |
| 9 | All four defense-in-depth layers assessed; enforcement point named for at least one operation (C-09) | [ ] | SE | |
| 10 | Cross-role differential complete; at least two roles compared; anomalous items flagged (C-10) | [ ] | CS | |
| 11 | Quad-lock verified: all 5 essential criteria have M1/M2/M3/M4 active per CA-1 criterion-ID rows (C-15 | C-18) | [ ] | CA | |
| 12 | All 10 tables present; all column headers pre-defined; no blank cells (C-11) | [ ] | CA | |
| 13 | Format Compliance Verdict issued citing preamble enforcement matrix Phase 1 by name (C-16 | C-18) | [ ] | CA | |
| 14 | Every checklist row above carries an explicit Owner column entry naming a specific expert role (C-14) | [ ] | CA | |
