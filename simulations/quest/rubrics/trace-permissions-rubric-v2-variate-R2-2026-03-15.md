# trace-permissions — Round 2 Variations (Rubric v2)

**Rubric:** v2 (13 criteria: C-01–C-13, including new C-11/C-12/C-13)
**R1 summary:** V-01=100, V-04=100, V-05=100 (golden); V-03=80 (golden at threshold); V-02=58 (below bar on C-01)
**R1 open question:** Does C-09 as structural byproduct (four-layer spine) produce richer enforcement-point reasoning than C-09 as a pre-printed table cell? V-05 addresses this directly.

---

## V-01 — Single-axis: Output Format

**Axis:** Output format — every analysis section as pre-printed table schema with blank-cell prohibition. All 13 criteria covered by dedicated table schemas. C-11 (pre-printed tables) is the structural delivery mechanism for C-12 (SHALL obligations embedded in table headers) and C-13 (expert role assignments as a named section).

**Hypothesis:** Extending the R1 V-01 pre-printed table architecture (which scored 100 against 10 criteria) to explicitly cover all 13 v2 criteria — including dedicated tables for the SHALL obligation register (C-12) and expert role sign-offs (C-13) — will score 100/100 by making all 13 criteria structurally visible and auditable at inspection time.

---

You are a Dataverse security specialist conducting a permissions trace for: {{topic}}

**PRE-FLIGHT RULE: Blank cells are prohibited in every table. Every cell SHALL carry an explicit value. Write "Not Configured", "None Found", "Not Applicable", or "N/A" as appropriate — never leave a cell empty. An output with empty cells is not a valid permissions trace.**

This trace produces 10 tables in sequence. Do not substitute prose for any required table. All schemas are pre-printed below — populate every column for every row.

---

### TABLE 1 — Role-Operation Matrix
**[C-01] SHALL produce a complete matrix. Every cell: Granted / Denied / Conditional / Not Applicable.**
*Failure example: Listing roles without operation columns, or any blank cell, fails this table.*

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Notes |
|------|--------|------|-------|--------|--------|----------|--------|-------|-------|

---

### TABLE 2 — Field-Level Security (Column Security Profile) Status
**[C-02] SHALL name every sensitive field. FLS status per field: Configured / Not Configured. A field with no FLS is a finding, not an omission.**
*Failure example: Omitting fields where no column security profile exists fails this table.*

| Field Name | Sensitivity Reason | FLS Status | Column Security Profile | FLS Gap? (Yes/No) | Notes |
|------------|-------------------|------------|------------------------|-------------------|-------|

**FLS Null Case — mandatory closing statement (write this line regardless of FLS state):**
> FLS NULL CASE: [state explicitly whether any sensitive fields lack column security profiles. If none configured: "No column security profiles are configured. All sensitive fields are accessible to any role with Read privilege on this table. This is flagged as a gap."]

---

### TABLE 3 — Record Access Scope per Role
**[C-03] SHALL assign scope to every role. Ambiguous scope = named gap, not blank cell.**
*Valid scopes: Own Records Only / Business Unit / Parent-Child Business Unit / Organization-Wide / Team-Scoped*

| Role | Access Scope | Business Unit Assignment | Team Scope Modifier (if any) | Ambiguity Flag |
|------|-------------|--------------------------|------------------------------|---------------|

---

### TABLE 4 — Privilege Escalation Vector Sweep
**[C-04] SHALL check all four named vectors. CLEAN requires explicit justification per row. No blank rows permitted.**
*Failure example: Checking only vectors that yielded findings, or CLEAN with no justification, fails this table.*

| Escalation Vector | Status (FINDING / CLEAN) | Mechanism | Effective Scope Gained | Justification |
|-------------------|--------------------------|-----------|----------------------|--------------|
| Team Membership Inheritance | | | | |
| Sharing Rule FLS Bypass | | | | |
| Impersonation / Run-As | | | | |
| Environment / System Admin Override | | | | |

---

### TABLE 5 — Sharing Rule Conflict Analysis
**[C-07] SHALL evaluate each sharing rule type for conflict with role-level access and FLS column profiles.**
*Failure example: A row with "Rule Present? No" must still carry an explicit "N/A — no rule present" in conflict columns.*

| Sharing Rule Type | Rule Present? | Conflict with Role Access? | Conflict with FLS Profile? | Conflict Description | Notes |
|-------------------|--------------|---------------------------|---------------------------|---------------------|-------|
| Manual Sharing | | | | | |
| Owner Team-Based Sharing | | | | | |
| Power Automate / Flow Sharing | | | | | |

---

### TABLE 6 — Security Gap Inventory
**[C-05] SHALL name at least one gap with a specific field, role, or rule. MUST contain at least one row.**
*If no gaps exist, provide explicit evidence per row (e.g., "All sensitive fields have FLS configured — see Table 2 rows X, Y, Z").*

| Gap ID | Gap Type | Specific Field / Role / Rule | Severity | Evidence / Notes |
|--------|----------|------------------------------|----------|-----------------|

*Valid Gap Types: Missing FLS / Team Membership Hole / Sharing Rule Conflict / Over-Permissioned Role / Escalation Path*

---

### TABLE 7 — Defense-in-Depth Layer Analysis
**[C-09] SHALL name all four Dataverse layers and identify the effective enforcement point for at least one operation.**
*Failure example: Naming a layer without explaining why upper layers do not override the enforcement point fails this table.*

| Layer | Layer Name | Assessment | Enforcement Point (Operation) | Why Upper Layers Do Not Override | Notes |
|-------|------------|-----------|-------------------------------|----------------------------------|-------|
| 1 | Environment / Admin Role | | | | |
| 2 | Security Role + BU Scope | | | | |
| 3 | Team Membership | | | | |
| 4 | Field-Level Security / Column Profiles | | | | |

---

### TABLE 8 — Cross-Role Differential Analysis
**[C-10] SHALL compare at least two roles side-by-side on at least one operation with Expected / Anomalous verdict.**

| Role A | Role B | Operation | Role A Access | Role B Access | Differential | Expected / Anomalous | Analysis |
|--------|--------|-----------|--------------|--------------|-------------|---------------------|---------|

---

### TABLE 9 — Gap Remediation Register
**[C-08] SHALL provide a specific remediation for each gap in Table 6. Generic language ("add FLS", "tighten security") does not pass — name the exact column security profile, role, and configuration location.**
*Failure example: "Enable FLS on sensitive fields" fails. "Create column security profile on creditlimit field, restrict Read to Sales Manager role, configure in Power Platform Admin Center > Security > Column Security Profiles" passes.*

| Gap ID (from Table 6) | Specific Remediation Action | Dataverse Configuration Location | Role / Team to Modify | Priority |
|-----------------------|----------------------------|----------------------------------|----------------------|---------|

---

### TABLE 10 — SHALL Obligation Register + Expert Role Sign-Offs
**[C-11, C-12, C-13] Pre-declared SHALL obligations keyed to criteria. Expert role assignments with sign-off cells.**

| # | SHALL Obligation | Criterion | Expert Role | Sign-Off (Satisfied / Open) |
|---|-----------------|-----------|-------------|---------------------------|
| A | SHALL produce a complete role-operation matrix with all cells filled (Table 1) | C-01 | SE | |
| B | SHALL name every sensitive field FLS status; state FLS null case explicitly (Table 2) | C-02 | SE | |
| C | SHALL assign record scope to every role; flag ambiguity as gap (Table 3) | C-03 | SE | |
| D | SHALL check all four escalation vectors; CLEAN requires explicit justification (Table 4) | C-04 | SE | |
| E | SHALL name at least one gap with specific field/role/rule (Table 6) | C-05 | CA | |
| F | SHALL use ≥4 Dataverse-native terms accurately; no generic RBAC substitution | C-06 | SE | |
| G | SHALL evaluate all three sharing rule types for conflict with role access and FLS (Table 5) | C-07 | CS | |
| H | SHALL provide specific remediation for ≥50% of gaps (Table 9) | C-08 | CA | |
| I | SHALL name all four Dataverse layers; identify enforcement point for ≥1 operation (Table 7) | C-09 | SE | |
| J | SHALL compare ≥2 roles side-by-side with Expected/Anomalous verdict (Table 8) | C-10 | SE | |
| K | SHALL deliver ≥5 analysis sections as pre-printed tables; blank cells prohibited throughout | C-11 | All | |
| L | SHALL complete this checklist; open items are gaps in this output | C-12 | CA | |
| M | SHALL assign sections to named SE + CS expert roles with explicit handoff | C-13 | All | |

**SE (Security Engineer) owns:** Tables 1, 2, 3, 4, 7, 8 and SHALL obligations A–D, F, I, J, M
**CS (Customer Success) owns:** Table 5 and SHALL obligation G
**CA (Compliance Analyst) owns:** Tables 6, 9 and SHALL obligations E, H, L

**SE SIGN-OFF:** [State Dataverse terminology compliance verdict. Confirm all SE-owned tables complete. Note any generic RBAC substitutions corrected.]

**CS SIGN-OFF:** [State sharing rule conflict validation verdict from agent-workflow perspective. Confirm Table 5 complete.]

**CA SIGN-OFF:** [State gap inventory completeness verdict. Confirm remediation register covers ≥50% of gaps. Confirm terminal checklist complete.]

---

## V-02 — Single-axis: Phrasing Register (SHALL-Modal with Explicit Failure Examples)

**Axis:** Phrasing register — the entire prompt is framed as 13 SHALL-obligation contracts, one per criterion, each with an explicit failure example. No pre-declared table schemas (unlike V-01); instead, SHALL language drives structure and a terminal checklist provides audit closure.

**Hypothesis:** Formulating 13 SHALL obligations with explicit failure examples (one per criterion) and a terminal 13-item checklist will produce 100/100 by eliminating gray-zone interpretations for all v2 criteria — including C-11 (tables enforced via SHALL K), C-12 (terminal checklist enforced via SHALL L), and C-13 (expert personas enforced via SHALL M).

---

You are conducting a Dataverse permissions trace for: {{topic}}

The following 13 SHALL obligations govern this output. Each is a binary contract — fully satisfied or not. Explicit failure examples are provided to eliminate interpretive slack.

---

**SHALL A — Role-Operation Matrix [C-01]**
The output SHALL produce a matrix mapping every role in scope against eight operations: Create, Read, Write, Delete, Append, AppendTo, Assign, Share. Every cell SHALL carry one of: Granted / Denied / Conditional / Not Applicable. Every cell must be populated.
> *Failure example: A list of roles without operation columns fails SHALL A. A table with any blank cell fails SHALL A. Writing "varies by configuration" without a value fails SHALL A.*

**SHALL B — Field-Level Security with Explicit Null Case [C-02]**
The output SHALL check whether column security profiles are configured for all sensitive fields in scope. For each sensitive field: name the field, state FLS status (Configured / Not Configured), and name the column security profile if one exists. When no FLS is configured on any sensitive field, the output SHALL state explicitly: "FLS NULL CASE: No column security profiles are configured. All sensitive fields are accessible to any role with Read privilege on this table. This is flagged as a gap." Silent omission of unconfigured FLS fails SHALL B.
> *Failure example: An output that only lists fields with FLS configured — omitting fields where no profile exists — fails SHALL B. An output with no mention of FLS at all fails SHALL B.*

**SHALL C — Record Access Scope per Role [C-03]**
The output SHALL assign one of the following scope values to every role: Own Records Only / Business Unit / Parent-Child Business Unit / Organization-Wide / Team-Scoped. A role with ambiguous or unresolved scope SHALL be flagged as a gap with the specific ambiguity named.
> *Failure example: Describing record access as "limited" or "broad" without assigning a Dataverse BU hierarchy scope value fails SHALL C.*

**SHALL D — Privilege Escalation Path Detection [C-04]**
The output SHALL check these four escalation vectors and state a result for each: (1) team membership inheritance granting broader role, (2) sharing rule bypassing FLS, (3) impersonation/run-as access, (4) environment or system admin override. A conclusion of "none found" is valid only when all four vectors have been checked with explicit justification per vector.
> *Failure example: A finding that names team inheritance without checking sharing rule bypass, impersonation, or admin override fails SHALL D. Checking only the vectors that yielded findings fails SHALL D.*

**SHALL E — Security Gap Inventory [C-05]**
The output SHALL produce a named gap inventory with at least one gap carrying: a specific field, role, or rule name; a gap type (Missing FLS / Team Membership Hole / Sharing Rule Conflict / Over-Permissioned Role / Escalation Path); and severity.
> *Failure example: A gap inventory entry that reads "FLS may be missing" without naming a specific field fails SHALL E. A conclusion of "no gaps found" is valid only if explicit evidence is provided for each gap type checked.*

**SHALL F — Dataverse-Native Terminology [C-06]**
The output SHALL use Dataverse-specific security constructs: business units, security roles, owner teams, access teams, column security profiles, table permissions, sharing records, environment roles. At least 4 of these terms SHALL appear and be used accurately. Generic RBAC terms (e.g., "permission group", "access level", "privilege set") without Dataverse mapping SHALL be replaced or flagged.
> *Failure example: Writing "the user's permission group determines access" without mapping to "security role" fails SHALL F.*

**SHALL G — Sharing Rule Conflict Analysis [C-07]**
The output SHALL evaluate at least one sharing rule type for conflict: does the sharing rule grant access that the security role denies, or deny access that FLS would permit? The analysis SHALL cover manual sharing, team-based sharing, and Power Automate/flow-based sharing. A conclusion of "no conflicts" SHALL name at least one sharing rule type that was explicitly checked.
> *Failure example: Stating "sharing rules do not conflict" without identifying which rule types were evaluated fails SHALL G.*

**SHALL H — Remediation Specificity [C-08]**
For each gap named in the gap inventory, the output SHALL provide a specific remediation action naming: the exact Dataverse configuration element to change (e.g., "column security profile on creditlimit"), the role or team to modify, and the configuration location in Dataverse.
> *Failure example: "Create a column security profile for the SSN field" satisfies SHALL H. "Enable FLS on sensitive fields" fails SHALL H for that gap.*

**SHALL I — Defense-in-Depth Layer Analysis [C-09]**
The output SHALL evaluate the four Dataverse security layers in sequence: (1) environment/admin role, (2) security role + BU scope, (3) team membership, (4) field-level security/column profiles. For at least one operation, the output SHALL identify the specific layer where access is granted or denied and explain why upper layers do not override that decision.
> *Failure example: Naming the four layers as a list without specifying which layer is the enforcement point for any specific operation fails SHALL I.*

**SHALL J — Cross-Role Differential Analysis [C-10]**
The output SHALL compare at least two roles side-by-side on at least one operation, naming both the access differential and whether that differential is Expected (consistent with principle of least privilege) or Anomalous (inconsistent with the roles' stated purposes).
> *Failure example: Describing two roles' access in separate paragraphs without a side-by-side comparison with an Expected/Anomalous verdict fails SHALL J.*

**SHALL K — Pre-Printed Table Structure with Blank-Cell Prohibition [C-11]**
The output SHALL deliver at least 5 analysis sections as pre-printed tables with all column headers defined before rows are populated. Blank cells are prohibited — write "Not Configured", "None Found", "Not Applicable", or "N/A" as appropriate. Prose enumeration substituted for a required table fails SHALL K.
> *Failure example: Listing roles and their operations as bullet points instead of a role-operation matrix table fails SHALL K. A table with any empty cell fails SHALL K.*

**SHALL L — Expert Role Persona Sequencing [C-13]**
The output SHALL be produced by at least two named expert roles with dedicated sub-sections:
- **Security Engineer (SE)**: Leads role-operation analysis (SHALL A), FLS analysis (SHALL B), escalation sweep (SHALL D), defense-in-depth layering (SHALL I), and cross-role differential (SHALL J). Uses Dataverse construct vocabulary exclusively.
- **Customer Success (CS)**: Independently validates sharing rule conflicts and escalation paths from an agent-workflow perspective (SHALL G).
Each role SHALL have at least one sub-section explicitly assigned to it by name. SE sections SHALL not use generic RBAC terms.
> *Failure example: Attributing all analysis to an unnamed "reviewer" without explicit SE and CS role sections fails SHALL L.*

**SHALL M — Terminal Verification Checklist [C-12]**
The output SHALL conclude with a checklist confirming that SHALL obligations A through M were each satisfied. Each item SHALL be marked Satisfied or Open. An Open item is a gap in this output — resolve before closing.
> *Failure example: Omitting the terminal checklist fails SHALL M. Marking all items Satisfied without completing the analysis fails SHALL M.*

---

**Dataverse Terminology Reference (SHALL F)**
Required terms to use accurately: security roles, business units, BU hierarchy (Own / BU / Parent-Child BU / Org-Wide), owner teams, access teams, column security profiles, table permissions, sharing records, environment roles, impersonation.

---

**TERMINAL CHECKLIST — SHALL M — complete before closing**

| SHALL | Obligation | Expert | Satisfied? (Yes / Open) |
|-------|-----------|--------|------------------------|
| A | Role-operation matrix with all cells filled | SE | |
| B | FLS coverage + explicit null case statement | SE | |
| C | Record scope assigned to every role | SE | |
| D | All four escalation vectors checked with explicit result | SE | |
| E | Named gap inventory with ≥1 specific field/role/rule | CA | |
| F | ≥4 Dataverse-native terms used accurately | SE | |
| G | ≥1 sharing rule type evaluated for conflict with role + FLS check | CS | |
| H | Specific remediation (not generic) for ≥50% of gaps | CA | |
| I | Four-layer analysis with enforcement-point identification for ≥1 op | SE | |
| J | ≥2 roles compared side-by-side with Expected/Anomalous verdict | SE | |
| K | ≥5 sections delivered as pre-printed tables; no blank cells | All | |
| L | Named SE + CS expert roles with dedicated sub-section assignments | All | |
| M | Terminal checklist present with all items resolved | CA | |

---

## V-03 — Single-axis: Role Sequence (Expert Persona Sequencing)

**Axis:** Role sequence — three named expert personas (SE, CS, CA) with explicit sub-section assignments covering all 13 criteria. Each criterion is a deliverable obligation for a named expert, not a general instruction. C-13 is the structural backbone; C-11 and C-12 are owned by the Compliance Analyst as format obligations.

**Hypothesis:** Assigning every criterion to a named expert sub-section (converting criteria into role obligations) will prevent omission of all 13 criteria, scoring 100/100 by making each criterion's deliverable ownership unambiguous.

---

You are conducting a Dataverse permissions trace for: {{topic}}

This trace is produced by three named expert roles in sequence. Each expert produces the sections assigned to them and does not produce sections outside their assignment. All outputs are in table format.

---

## EXPERT A — Security Engineer (SE)
*SE is a senior Dataverse security architect. SE sections use Dataverse construct vocabulary exclusively: business units, security roles, owner teams, access teams, column security profiles, table permissions, sharing records, environment roles. Generic RBAC terms are not used in SE sections.*

**SE-1: Role-Operation Matrix [C-01]**
Complete matrix: every role × every operation (Create, Read, Write, Delete, Append, AppendTo, Assign, Share). Every cell: Granted / Denied / Conditional / Not Applicable. No blank cells.

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share |
|------|--------|------|-------|--------|--------|----------|--------|-------|

**SE-2: Field-Level Security Coverage [C-02]**
Every sensitive field named. FLS status: Configured / Not Configured. FLS gap flagged. Null case stated.

| Field | Sensitivity Reason | FLS Status | Column Security Profile | Roles Restricted | FLS Gap? |
|-------|-------------------|------------|------------------------|-----------------|---------|

**FLS NULL CASE (mandatory):** [State explicitly whether any sensitive fields lack column security profiles.]

**SE-3: Record Access Scope per Role [C-03]**

| Role | Scope | BU Assignment | Team Scope Modifier | Ambiguity Flag |
|------|-------|--------------|--------------------|--------------|

*Valid scopes: Own Records Only / Business Unit / Parent-Child BU / Organization-Wide / Team-Scoped*

**SE-4: Privilege Escalation Sweep [C-04]**
All four vectors. CLEAN = explicit justification required per row.

| Vector | Status (FINDING / CLEAN) | Mechanism | Scope Gained | Justification |
|--------|--------------------------|-----------|-------------|--------------|
| Team Membership Inheritance | | | | |
| Sharing Rule FLS Bypass | | | | |
| Impersonation / Run-As | | | | |
| Environment / System Admin Override | | | | |

**SE-5: Dataverse Terminology Audit [C-06]**
List all Dataverse-specific terms used in SE-1 through SE-4 and SE-6 through SE-7. Confirm ≥4 terms used accurately.

| Term | Section | Correct Dataverse Construct? | Substitution Detected? |
|------|---------|------------------------------|----------------------|

**SE-6: Defense-in-Depth Layer Analysis [C-09]**
All four layers assessed. Enforcement point identified for ≥1 operation.

| Layer | Layer Name | Assessment | Enforcement Point (Operation) | Why Upper Layers Do Not Override |
|-------|------------|-----------|-------------------------------|----------------------------------|
| 1 | Environment / Admin Role | | | |
| 2 | Security Role + BU Scope | | | |
| 3 | Team Membership | | | |
| 4 | Field-Level Security / Column Profiles | | | |

**SE-7: Cross-Role Differential Analysis [C-10]**
≥2 roles compared side-by-side on ≥1 operation. Expected / Anomalous verdict required.

| Role A | Role B | Operation | Role A Access | Role B Access | Differential | Expected / Anomalous | Analysis |
|--------|--------|-----------|--------------|--------------|-------------|---------------------|---------|

**SE SIGN-OFF:** [Dataverse terminology verified — list terms confirmed. Tables SE-1 through SE-7 complete. No generic RBAC substitution detected / [corrections applied].]

---

## EXPERT B — Customer Success (CS)
*CS is a Dynamics 365 Customer Service platform specialist. CS validates from the agent-workflow perspective: what does a CS agent experience in practice, given the configured roles and sharing rules?*

**CS-1: Sharing Rule Conflict Analysis [C-07]**
All three sharing rule types evaluated for conflict with role-level access and FLS column profiles.

| Sharing Rule Type | Rule Present? | Conflict with Role Access? | Conflict with FLS? | Agent Scenario | CS Assessment |
|-------------------|--------------|---------------------------|-------------------|---------------|--------------|
| Manual Sharing | | | | | |
| Owner Team-Based Sharing | | | | | |
| Power Automate / Flow Sharing | | | | | |

**CS-2: Agent-Workflow Escalation Validation [C-04 — independent validation]**
Validate escalation vectors from SE-4 against standard CS agent workflow scenarios.

| SE-4 Vector | Agent Can Trigger? | Workflow Scenario | CS Assessment |
|-------------|-------------------|------------------|--------------|
| Team Membership Inheritance | | | |
| Sharing Rule Bypass | | | |
| Impersonation | | | |
| Admin Override | | | |

**CS SIGN-OFF:** [Sharing rule conflicts validated from agent-workflow perspective. Tables CS-1 and CS-2 complete.]

---

## EXPERT C — Compliance Analyst (CA)
*CA reviews the gap inventory and remediation register for completeness and audit readiness. CA owns the format obligations (C-11, C-12).*

**CA-1: Security Gap Inventory [C-05]**
All gaps from SE-1 through CS-2, consolidated. MUST contain at least one named gap (specific field, role, or rule).

| Gap ID | Source | Gap Type | Specific Field / Role / Rule | Severity | Notes |
|--------|--------|---------|------------------------------|----------|-------|

**CA-2: Remediation Register [C-08]**
Specific remediation for ≥50% of gaps. Name the exact column security profile, role privilege, or team assignment. Generic language not accepted.

| Gap ID | Specific Remediation | Configuration Location | Who Executes | Priority |
|--------|---------------------|----------------------|-------------|---------|

**CA-3: Format Compliance Verification [C-11]**
Confirm ≥5 sections delivered as pre-printed tables with blank-cell prohibition.

| Section | Table Format? | Blank Cells Present? | Pre-Declared Headers? |
|---------|--------------|---------------------|----------------------|
| SE-1 Role-Operation Matrix | | | |
| SE-2 FLS Coverage | | | |
| SE-3 Record Scope | | | |
| SE-4 Escalation Sweep | | | |
| SE-6 Defense-in-Depth | | | |
| CS-1 Sharing Rule Conflict | | | |
| CA-1 Gap Inventory | | | |
| CA-2 Remediation Register | | | |

**CA SIGN-OFF:** [Gap inventory complete — [X] gaps found. Remediation register covers [X/Y] gaps. Format compliance verified per CA-3.]

---

## TERMINAL CHECKLIST [C-12]
**All criteria verified before output closes. Open items are output gaps.**

| Criterion | Expert Owner | Section | Satisfied? (Yes / Open) |
|-----------|-------------|---------|------------------------|
| C-01: Role-operation matrix complete | SE | SE-1 | |
| C-02: FLS coverage + null case | SE | SE-2 | |
| C-03: Record scope per role | SE | SE-3 | |
| C-04: All four escalation vectors checked | SE + CS | SE-4, CS-2 | |
| C-05: Gap inventory with ≥1 named gap | CA | CA-1 | |
| C-06: ≥4 Dataverse terms verified | SE | SE-5 | |
| C-07: Sharing rule conflict evaluated | CS | CS-1 | |
| C-08: Specific remediation ≥50% gaps | CA | CA-2 | |
| C-09: Four layers + enforcement point | SE | SE-6 | |
| C-10: Cross-role differential | SE | SE-7 | |
| C-11: ≥5 sections as pre-printed tables | CA | CA-3 | |
| C-12: Terminal checklist present | CA | This table | |
| C-13: Named SE + CS + CA with sub-sections | All | All | |

---

## V-04 — Combo: Role Sequence + Output Format + SHALL Obligations

**Combination:** SE + CS expert personas (R1 V-04 mechanism) + all pre-printed table format with blank-cell prohibition (R1 V-01 mechanism) + SHALL-obligation contracts with terminal checklist (R1 V-05 mechanism). All three mechanisms extended to cover C-11, C-12, C-13.

**Hypothesis:** Combining the three independent enforcement mechanisms from R1's top scorers — structural table schemas (C-11), modal obligation language (C-12), and expert role delegation (C-13) — in a single prompt creates three independent paths to criterion compliance. Any criterion missed by one mechanism is caught by the others, producing 100/100 against all 13 v2 criteria.

---

You are conducting a Dataverse permissions trace for: {{topic}}

**STRUCTURAL RULES — read before generating any output:**
1. Every analysis section SHALL be delivered as a pre-printed table. Prose enumeration is not permitted where a table schema is defined below.
2. Blank cells are prohibited in every table. Every cell SHALL carry an explicit value: write "Not Configured", "None Found", "Not Applicable", or "N/A" as appropriate.
3. The analysis SHALL be produced by two named expert roles: Security Engineer (SE) and Customer Success (CS). Each expert SHALL own the sections assigned below.
4. All SHALL obligations below are binary contracts. The terminal checklist confirms each before the output closes.

---

## SECURITY ENGINEER (SE) SECTIONS
*SE uses Dataverse construct vocabulary exclusively: business units, security roles, owner teams, access teams, column security profiles, table permissions, sharing records, environment roles.*

**[SHALL A — C-01] SE TABLE 1: Role-Operation Matrix**
*Failure example: Listing roles without operation columns fails SHALL A. Any blank cell fails SHALL A.*

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|--------|------|-------|--------|--------|----------|--------|-------|-------------|

**[SHALL B — C-02] SE TABLE 2: Field-Level Security Coverage**
FLS NULL CASE statement required at the end of this table regardless of whether FLS is configured.
*Failure example: Omitting fields where no column security profile exists fails SHALL B.*

| Field | Sensitivity Reason | FLS Status | Column Security Profile | Roles Restricted | FLS Gap? |
|-------|-------------------|------------|------------------------|-----------------|---------|

**FLS NULL CASE (mandatory):** [Write this line: state explicitly whether any sensitive fields lack column security profiles.]

**[SHALL C — C-03] SE TABLE 3: Record Access Scope per Role**

| Role | Scope | BU Assignment | Team Scope Modifier | Ambiguity Flag |
|------|-------|--------------|--------------------|--------------|

**[SHALL D — C-04] SE TABLE 4: Privilege Escalation Sweep**
All four vectors. CLEAN = explicit justification required.
*Failure example: Checking only vectors that yielded findings, or CLEAN with no justification, fails SHALL D.*

| Vector | Status (FINDING / CLEAN) | Mechanism | Scope Gained | Justification |
|--------|--------------------------|-----------|-------------|--------------|
| Team Membership Inheritance | | | | |
| Sharing Rule FLS Bypass | | | | |
| Impersonation / Run-As | | | | |
| Environment / System Admin Override | | | | |

**[SHALL F — C-06] SE TABLE 5: Dataverse Terminology Audit**

| Term Used | Section | Correct Dataverse Mapping | Generic Substitution Detected? |
|-----------|---------|--------------------------|-------------------------------|

**[SHALL I — C-09] SE TABLE 6: Defense-in-Depth Layer Analysis**
*Failure example: Naming the layer without explaining why upper layers do not override fails SHALL I.*

| Layer | Layer Name | Assessment | Enforcement Point (Operation) | Why Upper Layers Do Not Override |
|-------|------------|-----------|-------------------------------|----------------------------------|
| 1 | Environment / Admin Role | | | |
| 2 | Security Role + BU Scope | | | |
| 3 | Team Membership | | | |
| 4 | Field-Level Security / Column Profiles | | | |

**[SHALL J — C-10] SE TABLE 7: Cross-Role Differential Analysis**

| Role A | Role B | Operation | Role A Access | Role B Access | Differential | Expected / Anomalous | Analysis |
|--------|--------|-----------|--------------|--------------|-------------|---------------------|---------|

**SE SIGN-OFF:** [Dataverse terminology verified. SE Tables 1–7 complete. No generic RBAC substitution detected / [corrections]. SHALL obligations A, B, C, D, F, I, J confirmed.]

---

## CUSTOMER SUCCESS (CS) SECTIONS

**[SHALL G — C-07] CS TABLE 8: Sharing Rule Conflict Analysis**

| Sharing Rule Type | Rule Present? | Conflict with Role Access? | Conflict with FLS Profile? | Agent Scenario | CS Assessment |
|-------------------|--------------|---------------------------|---------------------------|---------------|--------------|
| Manual Sharing | | | | | |
| Owner Team-Based Sharing | | | | | |
| Power Automate / Flow Sharing | | | | | |

**CS SIGN-OFF:** [Sharing rule conflicts validated from agent-workflow perspective. CS Table 8 complete. SHALL G confirmed.]

---

## COMPLIANCE ANALYST (CA) SECTIONS

**[SHALL E — C-05] CA TABLE 9: Security Gap Inventory**
MUST contain at least one row with a specific field, role, or rule.

| Gap ID | Source | Gap Type | Specific Field / Role / Rule | Severity | Evidence |
|--------|--------|---------|------------------------------|----------|---------|

**[SHALL H — C-08] CA TABLE 10: Remediation Register**
Name the exact column security profile, role, and configuration location. Generic language fails.
*Failure example: "Add FLS" fails. "Create column security profile on SSN field, restrict to HR Manager role, Power Platform Admin Center > Security > Column Security Profiles" passes.*

| Gap ID | Specific Remediation Action | Configuration Location | Role / Team | Priority |
|--------|----------------------------|-----------------------|------------|---------|

**CA SIGN-OFF:** [Gap inventory complete. Remediation covers [X/Y] gaps. CA obligations E and H confirmed.]

---

## TERMINAL VERIFICATION CHECKLIST
**[SHALL K + SHALL L + SHALL M — C-11 + C-13 + C-12] All SHALL obligations verified. Open items are output gaps.**

| SHALL | Criterion | Expert | Table | Satisfied? (Yes / Open) |
|-------|-----------|--------|-------|------------------------|
| A | C-01: Role-operation matrix, all cells filled | SE | T1 | |
| B | C-02: FLS coverage + explicit null case statement | SE | T2 | |
| C | C-03: Record scope assigned to every role | SE | T3 | |
| D | C-04: All four escalation vectors with CLEAN justification or FINDING | SE | T4 | |
| E | C-05: Gap inventory with ≥1 named gap (field/role/rule) | CA | T9 | |
| F | C-06: ≥4 Dataverse-native terms verified | SE | T5 | |
| G | C-07: All 3 sharing rule types evaluated for conflict | CS | T8 | |
| H | C-08: Specific remediation (not generic) for ≥50% of gaps | CA | T10 | |
| I | C-09: Four layers + enforcement point for ≥1 operation | SE | T6 | |
| J | C-10: ≥2 roles side-by-side with Expected/Anomalous verdict | SE | T7 | |
| K | C-11: ≥5 sections as pre-printed tables; no blank cells throughout | All | All | |
| L | C-13: Named SE + CS + CA roles with dedicated sub-section assignments | All | All | |
| M | C-12: Terminal checklist present with all items resolved | CA | This | |

---

## V-05 — Combo: Lifecycle Spine + Expert Persona Layer Handoffs + SHALL Obligations

**Combination:** Four-layer Dataverse security spine (lifecycle emphasis axis) with expert personas assigned to specific layers (role sequence axis) and SHALL-modal obligations (phrasing register axis). Directly probes the R1 open research question: does the four-layer spine produce richer enforcement-point analysis than the pre-printed table approach?

**Hypothesis:** Assigning expert personas to specific Dataverse security layers — rather than to the full document — produces richer layer-boundary reasoning by forcing the SE to reason about enforcement-point transitions at each layer handoff. The four-layer spine makes C-09 a structural byproduct, the layer-scoped personas enforce C-13 with cleaner handoff semantics, and SHALL obligations cover C-12. This answers the R1 open question by making the enforcement-point mechanism *the document's generative structure* rather than a cell in a table.

---

You are conducting a Dataverse permissions trace for: {{topic}}

This trace is structured around the four Dataverse security layers. Each layer is a named section. Expert roles are assigned to specific layers. Analysis accumulates downward: gaps, escalation paths, and FLS gaps found at each layer carry forward explicitly to the next. The four-layer progression is the enforcement spine.

**SHALL contracts govern this trace. The terminal checklist confirms compliance before the output closes.**

---

## PRE-TRACE DECLARATION

Before any layer analysis begins, declare:

| Declaration | Value |
|-------------|-------|
| Roles in scope | [list all roles] |
| Operations in scope | Create, Read, Write, Delete, Append, AppendTo, Assign, Share |
| Sensitive fields in scope | [list all sensitive fields] |
| Escalation vectors to check | Team membership inheritance / Sharing rule FLS bypass / Impersonation / Environment admin override |

*Scope lock: If analysis discovers a role or field not on these lists, add it with a scope-expansion note.*

---

## LAYER 1 — Environment / System Admin Role
**Expert: Security Engineer (SE)**

**[SHALL D — L1 vector] L1 Table: Environment-Level Escalation Check**
Can any in-scope role acquire environment admin or system admin access?

| Role | Environment-Level Privilege | System Admin? | Impersonation Enabled? | Escalation Risk | Notes |
|------|---------------------------|--------------|----------------------|----------------|-------|

**Layer 1 Gap Accumulation:**

| Gap ID | Gap Type | Description | Carry-Forward to Layer |
|--------|---------|-------------|----------------------|

---

## LAYER 2 — Security Role + Business Unit Scope
**Expert: Security Engineer (SE)**

**[SHALL A — C-01] L2 Table: Role-Operation Matrix**
Every role × every operation. Granted / Denied / Conditional / Not Applicable. No blank cells.
*Failure example: Any blank cell fails SHALL A.*

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | BU Scope |
|------|--------|------|-------|--------|--------|----------|--------|-------|---------|

**[SHALL C — C-03] L2 Table: Record Access Scope per Role**

| Role | Scope | BU Assignment | Parent-Child BU? | Ambiguity Flag |
|------|-------|--------------|-----------------|--------------|

**[SHALL J — C-10] L2 Table: Cross-Role Differential Analysis**
Compare ≥2 roles side-by-side on ≥1 operation. Expected / Anomalous verdict required.

| Role A | Role B | Operation | Role A Access | Role B Access | Differential | Expected / Anomalous | Analysis |
|--------|--------|-----------|--------------|--------------|-------------|---------------------|---------|

**Layer 2 Gap Accumulation:**

| Gap ID | Gap Type | Description | Carry-Forward to Layer |
|--------|---------|-------------|----------------------|

---

## LAYER 3 — Team Membership
**Expert: Security Engineer (SE) for configuration; Customer Success (CS) for agent-workflow validation**

**[SHALL D — L3 vectors] SE L3 Table: Team Membership Escalation Sweep**

| Vector | Status (FINDING / CLEAN) | Team / Rule | Scope Gained | Justification |
|--------|--------------------------|------------|-------------|--------------|
| Team Membership Inheritance | | | | |
| Impersonation / Run-As | | | | |

**[SHALL G — C-07] CS L3 Table: Sharing Rule Conflict Analysis**
CS independently evaluates sharing rules from an agent-workflow perspective.

| Rule Type | Rule Present? | Conflict with Role Access? | Conflict with FLS? | Agent Scenario | CS Assessment |
|-----------|--------------|---------------------------|-------------------|---------------|--------------|
| Manual Sharing | | | | | |
| Owner Team-Based Sharing | | | | | |
| Power Automate Sharing | | | | | |

**[SHALL D — L3 sharing vector] Sharing Rule FLS Bypass Check:**
Does any sharing rule grant record access that bypasses a column security profile restriction?

| Sharing Rule | Bypasses FLS Profile? | Evidence | Escalation Risk |
|-------------|----------------------|---------|----------------|

**Layer 3 Gap Accumulation:**

| Gap ID | Gap Type | Description | Carry-Forward to Layer |
|--------|---------|-------------|----------------------|

---

## LAYER 4 — Field-Level Security / Column Security Profiles
**Expert: Security Engineer (SE)**

**[SHALL B — C-02] L4 Table: FLS Coverage per Sensitive Field**
Every sensitive field named. Configured / Not Configured. No silent omissions.

| Field | FLS Status | Column Security Profile | Roles Restricted | FLS Gap? | Carry-Forward from Layer 3? |
|-------|------------|------------------------|-----------------|---------|---------------------------|

**FLS NULL CASE (mandatory — write this line):** [State explicitly whether any sensitive fields lack column security profiles. If none: "FLS NULL CASE: No column security profiles are configured. This is flagged as a gap."]

**[SHALL I — C-09] L4 Table: Defense-in-Depth Enforcement Summary**
Synthesize all four layers. For ≥1 operation: name the effective enforcement layer and explain why upper layers do not override.

| Layer | Layer Name | Assessment | Enforcement Point (Operation) | Why Upper Layers Do Not Override |
|-------|------------|-----------|-------------------------------|----------------------------------|
| 1 | Environment / Admin Role | | | |
| 2 | Security Role + BU Scope | | | |
| 3 | Team Membership | | | |
| 4 | Column Security Profiles | | | |

**Layer 4 Gap Accumulation:**

| Gap ID | Gap Type | Description | Carry-Forward: Final |
|--------|---------|-------------|---------------------|

---

## CROSS-LAYER GAP SYNTHESIS
**Expert: Compliance Analyst (CA)**

**[SHALL E — C-05] Gap Inventory — consolidated across all four layers**
Merge all Gap Accumulation tables from Layers 1–4. MUST contain at least one row with specific field/role/rule.

| Gap ID | Layer Found | Gap Type | Specific Field / Role / Rule | Severity | Notes |
|--------|------------|---------|------------------------------|----------|-------|

**[SHALL H — C-08] Remediation Register**
Name the exact column security profile, role privilege, or team assignment. Generic language fails.

| Gap ID | Layer | Specific Remediation Action | Configuration Location | Priority |
|--------|-------|----------------------------|----------------------|---------|

---

## DATAVERSE TERMINOLOGY AUDIT
**[SHALL F — C-06] Confirm ≥4 Dataverse-native terms used accurately across all layers.**

| Term | Layers Used In | Correctly Applied? | Generic Substitution Detected? |
|------|---------------|-------------------|-------------------------------|

*Required terms: business units, security roles, owner teams, access teams, column security profiles, table permissions, sharing records, environment roles*

---

## EXPERT SIGN-OFFS

**SE SIGN-OFF (Layers 1, 2, 4 + L3 configuration):** [Dataverse terminology verified. Layer analysis complete. All four escalation vectors checked across L1 and L3. Enforcement-point identification confirmed at L4 table.]

**CS SIGN-OFF (L3 sharing rule + agent-workflow):** [Sharing rule conflicts validated from agent-workflow perspective. L3 CS table complete.]

**CA SIGN-OFF (Gap synthesis + remediation):** [Gap inventory complete across all layers. Remediation register covers [X/Y] gaps.]

---

## TERMINAL CHECKLIST
**[SHALL K — C-12] All SHALL obligations verified. Open items are output gaps.**

| SHALL | Coverage | Layer / Section | Satisfied? (Yes / Open) |
|-------|---------|-----------------|------------------------|
| A | C-01: Role-operation matrix, all cells filled | L2 | |
| B | C-02: FLS null case stated; all sensitive fields named | L4 | |
| C | C-03: Record scope assigned to every role | L2 | |
| D | C-04: All four escalation vectors checked (L1 + L3) | L1, L3 | |
| E | C-05: Gap inventory with ≥1 named gap (specific field/role/rule) | Gap Synthesis | |
| F | C-06: ≥4 Dataverse-native terms verified | Terminology Audit | |
| G | C-07: All 3 sharing rule types evaluated for conflict | L3-CS | |
| H | C-08: Specific remediation (not generic) for ≥50% of gaps | Gap Synthesis | |
| I | C-09: Four-layer analysis with enforcement-point identification | L4 | |
| J | C-10: ≥2 roles compared side-by-side with Expected/Anomalous verdict | L2 | |
| K | C-11: ≥5 sections as pre-printed tables; no blank cells | All layers | |
| L | C-13: Named SE + CS + CA roles with layer-assigned sub-sections | All layers | |
| M | C-12: Terminal checklist present with all items resolved | This table | |

---

## Variation Summary

| Variation | Axes | Key Mechanisms | C-11 Path | C-12 Path | C-13 Path | Hypothesis |
|-----------|------|---------------|-----------|-----------|-----------|-----------|
| V-01 | Output format | Pre-printed table schemas for all 13 criteria; expert sign-off table; TABLE 10 as SHALL register | 10 pre-printed tables with blank-cell prohibition | TABLE 10 = SHALL register + CA sign-off | TABLE 10 assigns SE/CS/CA per criterion | Extending R1 V-01 table architecture to 13 criteria scores 100/100 |
| V-02 | Phrasing register | 13 SHALL obligations with failure examples; terminal checklist | SHALL K mandates ≥5 pre-printed tables | SHALL M mandates terminal checklist | SHALL L mandates named SE+CS sections | 13 modal obligations eliminate all gray-zone interpretations |
| V-03 | Role sequence | 3 expert personas (SE, CS, CA); each criterion assigned to named expert sub-section | CA-3 format compliance table verifies ≥5 sections | Terminal checklist with criterion-owner column | 3 named experts with sub-section assignments IS C-13 | Criterion-as-role-obligation prevents all omissions |
| V-04 | Role seq + Output format + SHALL | Combines R1 V-01 + V-04 + V-05 mechanisms; all extended to 13 criteria | ≥10 pre-printed tables with blank-cell prohibition | Terminal checklist confirms all SHALL obligations | SE + CS + CA with named section assignments | 3 independent enforcement mechanisms create redundant criterion coverage |
| V-05 | Lifecycle spine + Role handoff + SHALL | Four-layer spine with expert personas per layer; gap accumulation carries forward; probes R1 open question | ≥5 tables per layer with blank-cell enforcement | Terminal checklist + SHALL K | SE leads L1-L2-L4; CS leads L3 sharing; CA leads synthesis | Layer-scoped persona handoffs produce richer enforcement-point reasoning than table cells (R1 open question answer) |
