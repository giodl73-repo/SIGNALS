# trace-permissions Variate — Round 9
**Date:** 2026-03-15
**Rubric:** v8 (C-01 through C-24)
**Target criteria:** Maintain 16/16 across varied structural axes; stress-test C-24 alternative structural forms

**State entering Round 9:**

| Variation | R8 v8 score | Notes |
|-----------|------------|-------|
| V-03 | 100.0 (16/16) | Reference architecture 1: CA-first + Registry + phase markers + labeled double-anchor |
| V-05 | 100.0 (16/16) | Reference architecture 2: same core + rubric-mirror language in Phase 3 |
| V-02 | 99.4 (15/16) | Fails C-22 only (no phase labels in output body) |
| V-01 | 98.1 (13/16) | Fails C-23 (no double-anchor) -> C-24 (requires C-23) |
| V-04 | 98.1 (13/16) | Fails C-23 (inline compression) -> C-24 (requires C-23) |

Round 9 holds the proven structural core and varies along three surface axes. None of the axes removes a structural requirement.

---

## Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Single-axis A: Numbered sub-steps in CA-1 rows | C-24 explicitly names "numbered sub-steps" as a valid structural form alongside labeled lines and delimited bullets. Replacing the bold-line labels with "Step 1 / Step 2 / Step 3" markers makes anchor boundaries readable at list-structure level rather than text-content level. 4-mechanism core unchanged. Hypothesis: 16/16. |
| V-02 | Single-axis B: CS executes before SE | CS establishes a qualitative lower-trust access baseline in Phase 1 (narrative + sharing rule expectations, no formal tables). SE fills TABLE_1-5 in Phase 2, confirming or contradicting CS expectations. Essential criteria C-01 through C-05 remain assigned to SE sections in the preamble. Registry, phase labels, double-anchor unchanged. Hypothesis: 16/16. |
| V-03 | Single-axis C: Inertia framing added | A CONTEXT section opens the prompt describing the manual RBAC audit status quo (spot-checking roles UI, missed cumulative privilege, invisible FLS gaps) that this trace replaces. Core 4-mechanism structure unchanged. Tests whether motivational framing improves C-08 (remediation specificity) and C-04 (escalation depth) without disrupting structural criteria. Hypothesis: 16/16. |
| V-04 | Combined A+B: Numbered sub-steps + CS-first sequence | V-01 + V-02. Tests whether the two surface-level axes compose without interaction effects on structural compliance. Hypothesis: 16/16. |
| V-05 | Combined A+C + rubric-verbatim C-24 language | Numbered sub-steps (A) + inertia framing (C) + Phase 3 mandate uses rubric-exact C-24 language: "each anchor is a separately parseable structural element, not an inline concatenation." Maximum specification fidelity over new axis combination. Hypothesis: 16/16. |

---

## V-01 — Single-Axis A: Numbered Sub-Steps Double-Anchor

**Axis:** Output format — CA-1 double-anchor reaffirmation delivered as three numbered sub-steps (Step 1 Registry / Step 2 Preamble / Step 3 Verification) rather than bold-labeled paragraph lines
**Hypothesis:** C-24's pass condition names "numbered sub-steps" as a valid structural form. V-03-R8 used bold labeled lines (`Schema Registry TABLE_1: ...\nPreamble row C-01 as authored by CA...`). Replacing those with explicit step numbers makes anchor boundaries readable at list position rather than at label text — an evaluator identifies the Registry anchor as Step 1 and the Preamble anchor as Step 2 by their sequence number, not by inferring boundaries from values. Every other structural element is identical to V-03-R8. Hypothesis: 16/16.

---

You are running a permissions trace signal for: {{topic}}

---

## ROLE SEQUENCING MANDATE

This output executes in four explicitly labeled phases. Phase labels MUST appear as section headers in the output. Each phase completes fully before the next begins. Phase boundaries MUST include explicit handoff strings naming the next phase and executor.

**PHASE 0 — CA (Compliance Auditor):**
CA executes first and is the sole author of all structural artifacts. CA authors the Schema Registry (Step 0.1: all table schemas, blank-cell prohibition stated globally) and the Criterion Enforcement Matrix preamble (Step 0.2: M1/M2/M3/M4 columns, M4 row IDs pre-assigned by CA for every essential criterion) in one continuous execution before PHASE 1 begins. CA issues handoff to PHASE 1.

**PHASE 1 — SE (Security Engineer / Dataverse Security Expert):**
Executes second. Performs all security analysis using Dataverse-native terminology exclusively: business units, security roles, owner teams vs. access teams, table permissions, column security profiles, sharing records, environment roles, OWD settings. Issues handoff to PHASE 2.

**PHASE 2 — CS (Customer Success):**
Executes third. Validates lower-trust access and sharing rule conflicts from a practical workflow perspective. Issues handoff to PHASE 3.

**PHASE 3 — CA-1 (CA Verification Pass):**
CA returns. Each CA-1 verification row delivers double-anchor reaffirmation as three numbered sub-steps within the row:
- Step 1 — Registry anchor: state the Schema ID and its declared column list from the Schema Registry authored by CA in Phase 0.
- Step 2 — Preamble anchor: quote the preamble row values for that criterion as authored by CA in Phase 0.
- Step 3 — Verification: state whether each required element is present and the overall result (PASS / FAIL).

Step 1 and Step 2 MUST each constitute a complete, independently readable statement before Step 3 begins. CA's terminal verdict cites Phase 0 by label, the CA-authored Registry, and the CA-authored preamble as the three structural verification bases.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes steps 0.1 and 0.2 in this phase before any other phase begins.*

### Step 0.1 — Schema Registry (CA-authored)

**All table schemas declared centrally by CA. Blank-cell prohibition is global — individual tables do not restate it.**

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Blank-cell rule: every cell MUST carry Granted / Denied / Conditional (state condition inline) / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Blank-cell rule: FLS Profile Configured? = Configured / Not Configured (never blank). Gap? = YES / NO (never blank).

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name] (never blank). Verified? = YES / NO.

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
Blank-cell rule: all four vectors (team inheritance, sharing rules, impersonation, admin/env roles) MUST appear as rows. Checked? = YES for all rows. Finding = escalation path or explicit rule-out with reason (never blank).

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Blank-cell rule: Remediation = the exact configuration change required — naming the specific object, location, and expected post-fix state. "Review permissions" or vague advice fails this column.

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: All three mechanisms (M1 format schema, M2 expert role sub-section, M3 SHALL obligation) are simultaneously active for every essential criterion. They are not alternative coverage paths. M4 CA verification row IDs are pre-assigned by CA below and constitute pre-existing obligations that CA-1 rows fulfill as structural completions of this contract.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row (pre-assigned by CA) |
|-----------|-------------------|---------------------|---------------------|----------------------------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**SHALL obligations (authored by CA, Phase 0):**
- SHALL-A: A complete TABLE_1 MUST be present. Every cell MUST carry Granted / Denied / Conditional / N/A. Every role holding any privilege on any entity in {{topic}} MUST appear as a row.
- SHALL-B: TABLE_2 MUST list every field containing PII, Financial, or Audit-Compliance data with explicit FLS status. When no column security profiles are active, that fact MUST be stated explicitly with sensitive fields identified. Every Not Configured field MUST appear in TABLE_5.
- SHALL-C: Every role in TABLE_1 MUST also appear in TABLE_3 with a filled Effective Scope. Roles with ambiguous scope MUST appear in TABLE_5.
- SHALL-D: TABLE_4 MUST contain all four escalation vectors with Checked? = YES. A rule-out requires naming the specific mechanism examined and the specific reason no path exists.
- SHALL-E: TABLE_5 MUST contain at least one gap row with a named specific field, role, or rule. If zero gaps exist, TABLE_5 MUST contain explicit evidence rows stating what was checked and confirmed safe.

*Handing to PHASE 1 — SE.*

---

## PHASE 1 — SE: Security Analysis

*SE executes Sections 1 through 5 using Dataverse-native terminology throughout.*

### SE-1 / SHALL-A — Section 1: Role-Operation Matrix

**TABLE_1 — Role-Operation Matrix** (Schema Registry TABLE_1 schema; blank-cell rule applies)

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Include every role with any privilege on any entity in {{topic}}. Record Scope: Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].

### SE-2 / SHALL-B — Section 2: Field-Level Security Coverage

**TABLE_2 — FLS Coverage** (Schema Registry TABLE_2 schema; blank-cell rule applies)

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Check Security > Column Security Profiles for all entities in scope. If no profiles exist: state explicitly — "No column security profiles active. Sensitive fields identified: [list]. All entered in TABLE_5." Forward all Gap? YES rows to TABLE_5.

### SE-3 / SHALL-C — Section 3: Record Access Scope

**TABLE_3 — Record Scope by Role** (Schema Registry TABLE_3 schema; blank-cell rule applies)

| Role | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|--------------|----------------|-----------------|-----------|

Every role from TABLE_1 MUST appear. OWD: Private / Business Unit / Parent-Child BU / Organization. Scope Modifier: security role privilege depth, team membership, or sharing rule.

**Defense-in-depth layer assessment:** For at least one operation in TABLE_1, identify the specific Dataverse enforcement layer (1: environment/admin role, 2: security role + BU scope, 3: team membership, 4: column security profiles) where access is granted or denied, and state why the layers above it do not override.

### SE-4 / SHALL-D — Section 4: Privilege Escalation Analysis

**TABLE_4 — Escalation Vector Inventory** (Schema Registry TABLE_4 schema; all four vectors required)

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Findings: `[Role] -> [Action] -> [Elevated access achieved]`. Rule-outs: "Checked [mechanism]: no path found because [specific reason]."

### SE-5 / SHALL-E — Section 5: Security Gap Inventory

**TABLE_5 — Security Gap Inventory** (Schema Registry TABLE_5 schema; blank-cell rule applies)

| # | Gap Type | Entity | Field or Rule | Role | Severity | Remediation |
|---|----------|--------|---------------|------|----------|-------------|

Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED. Severity: CRITICAL / HIGH / MEDIUM. Remediation: exact change — e.g., "Create column security profile on [field], restrict Write to [role] in [solution location]."

*Handing to PHASE 2 — CS.*

---

## PHASE 2 — CS: Agent-Workflow and Sharing Rule Validation

*CS executes this phase.*

**CS-1 — Customer Service access trace:**
State every operation the Customer Service role can perform per entity (CRUD + Assign) and record scope. Name every sensitive field the CS role can read or write; state whether appropriate to job function or overreach.

**CS-2 — Sharing rule conflict audit:**

| Rule Name | Trigger | Access Granted | Intended? | Overreach? |
|-----------|---------|----------------|-----------|------------|

For each Overreach? YES: name the rule, the unintended access gained, and the role that benefits unexpectedly. State how the sharing rule interacts with the FLS status from TABLE_2.

**CS-3 — Cross-role differential:**
Compare the Customer Service and Security Engineer roles on the most sensitive entity in scope for the same operation. State whether the access differential is expected (least privilege satisfied) or anomalous.

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Numbered-Step Double-Anchor Format Compliance Verification

*CA returns for the verification pass. Each CA-1 row MUST deliver double-anchor reaffirmation as three numbered sub-steps. Step 1 cites the Schema Registry entry (schema ID and declared columns). Step 2 quotes the preamble row values for that criterion as authored by CA in Phase 0. Step 3 states the verification result. Step 1 and Step 2 MUST each constitute a complete, independently readable statement before Step 3 begins.*

**CA-1.1 — C-01 verification (completing Phase 0 M4 pre-assignment CA-1.1 as declared in preamble row 1):**
- Step 1 — Registry anchor: Schema ID TABLE_1, declared columns [Role, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope], blank-cell rule: Granted / Denied / Conditional / N/A.
- Step 2 — Preamble anchor: C-01 as authored by CA in Phase 0 — TABLE_1 / SE-1 / SHALL-A / CA-1.1.
- Step 3 — Verification: TABLE_1 present? All cells filled with valid values? All roles with any privilege included? -> PASS / FAIL

**CA-1.2 — C-02 verification (completing Phase 0 M4 pre-assignment CA-1.2 as declared in preamble row 2):**
- Step 1 — Registry anchor: Schema ID TABLE_2, declared columns [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?], blank-cell rule: FLS Profile Configured? = Configured / Not Configured; Gap? = YES / NO.
- Step 2 — Preamble anchor: C-02 as authored by CA in Phase 0 — TABLE_2 / SE-2 / SHALL-B / CA-1.2.
- Step 3 — Verification: TABLE_2 present? Every sensitive field with explicit FLS status? Null case stated if no FLS active? All Gap? YES rows in TABLE_5? -> PASS / FAIL

**CA-1.3 — C-03 verification (completing Phase 0 M4 pre-assignment CA-1.3 as declared in preamble row 3):**
- Step 1 — Registry anchor: Schema ID TABLE_3, declared columns [Role, OWD Baseline, Scope Modifier, Effective Scope, Verified?], blank-cell rule: Effective Scope and Verified? filled for every row.
- Step 2 — Preamble anchor: C-03 as authored by CA in Phase 0 — TABLE_3 / SE-1+SE-3 / SHALL-C / CA-1.3.
- Step 3 — Verification: Every TABLE_1 role appears in TABLE_3? All Effective Scope cells filled? Ambiguous scope rows in TABLE_5? -> PASS / FAIL

**CA-1.4 — C-04 verification (completing Phase 0 M4 pre-assignment CA-1.4 as declared in preamble row 4):**
- Step 1 — Registry anchor: Schema ID TABLE_4, declared columns [Vector, Checked?, Finding, Severity], blank-cell rule: all four vectors required, Checked? = YES for all, Finding = path or explicit rule-out with reason.
- Step 2 — Preamble anchor: C-04 as authored by CA in Phase 0 — TABLE_4 / SE-4 / SHALL-D / CA-1.4.
- Step 3 — Verification: TABLE_4 present? All four vectors as rows? Checked? = YES for all? Each with finding or specific rule-out? -> PASS / FAIL

**CA-1.5 — C-05 verification (completing Phase 0 M4 pre-assignment CA-1.5 as declared in preamble row 5):**
- Step 1 — Registry anchor: Schema ID TABLE_5, declared columns [#, Gap Type, Entity, Field or Rule, Role, Severity, Remediation], blank-cell rule: Remediation = exact configuration change.
- Step 2 — Preamble anchor: C-05 as authored by CA in Phase 0 — TABLE_5 / SE-5 / SHALL-E / CA-1.5.
- Step 3 — Verification: TABLE_5 present? At least one named gap with specific field/role/rule? All remediations exact (not vague)? -> PASS / FAIL

**CA Format Compliance Verdict — citing Phase 0:**
This verdict cites the CA-authored Schema Registry (Step 0.1), the CA-authored preamble (Step 0.2), and Phase 0 by label as the three structural verification bases.
[State: C-01 through C-05 pass/fail counts. Overall: COMPLIANT / NON-COMPLIANT. List any open items with responsible role.]

---

## V-02 — Single-Axis B: CS-First Role Sequence

**Axis:** Role sequence — Customer Success (CS) executes as Phase 1 to establish a lower-trust access baseline before Security Engineer (SE) fills formal tables in Phase 2
**Hypothesis:** Standard R8 sequence: CA -> SE -> CS -> CA-1. Inverting Phases 1 and 2 makes CS run first (narrative access expectations + sharing rule hypotheses) before SE fills TABLE_1-5. The preamble M2 column still assigns all essential criteria to SE sections because C-01 through C-05 require formal tables that only SE can produce. CS Phase 1 provides a qualitative baseline SE can confirm or contradict; discrepancies are flagged in TABLE_5 as CS-EXPECTATION-VIOLATED gaps. Phase labels, Registry, double-anchor structure unchanged. Hypothesis: 16/16.

---

You are running a permissions trace signal for: {{topic}}

---

## ROLE SEQUENCING MANDATE

This output executes in four explicitly labeled phases. Phase labels MUST appear as section headers in the output. Each phase completes fully before the next begins. Phase boundaries MUST include explicit handoff strings naming the next phase and executor.

**PHASE 0 — CA (Compliance Auditor):**
CA executes first and is the sole author of all structural artifacts. CA authors the Schema Registry (Step 0.1) and the Criterion Enforcement Matrix preamble (Step 0.2) in one continuous execution before PHASE 1 begins. CA issues handoff to PHASE 1.

**PHASE 1 — CS (Customer Success):**
Executes second. Establishes practical lower-trust access baseline: describes the Customer Service role's expected operations, expected record scope, and expected sharing rule behavior before the technical trace confirms or refutes them. CS produces a narrative baseline and a sharing rule expectations table. CS does NOT fill TABLE_1-5; those are SE's responsibility. CS issues handoff to PHASE 2.

**PHASE 2 — SE (Security Engineer / Dataverse Security Expert):**
Executes third. Performs all technical security analysis using Dataverse-native terminology exclusively: business units, security roles, owner teams vs. access teams, table permissions, column security profiles, sharing records, environment roles, OWD settings. Fills TABLE_1-5. Where SE findings confirm CS Phase 1 expectations, SE notes confirmation. Where findings contradict CS expectations, SE adds a CS-EXPECTATION-VIOLATED row to TABLE_5. Issues handoff to PHASE 3.

**PHASE 3 — CA-1 (CA Verification Pass):**
CA returns. Each CA-1 verification row performs double-anchor reaffirmation: (1) cite Schema Registry entry for the relevant table — schema ID and declared columns — as a labeled element; (2) quote preamble row values for that criterion as authored by CA in Phase 0 — as a labeled element; (3) state verification result. Both anchors appear as structurally distinct labeled elements before the verification statement. CA's terminal verdict cites Phase 0 by label, the CA-authored Registry, and the CA-authored preamble.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes steps 0.1 and 0.2 before Phase 1 begins.*

### Step 0.1 — Schema Registry (CA-authored)

**All table schemas declared centrally by CA. Blank-cell prohibition is global.**

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Blank-cell rule: every cell MUST carry Granted / Denied / Conditional (state condition) / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Blank-cell rule: FLS Profile Configured? = Configured / Not Configured. Gap? = YES / NO.

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Blank-cell rule: Effective Scope filled for every row. Verified? = YES / NO.

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
Blank-cell rule: all four vectors (team inheritance, sharing rules, impersonation, admin/env roles) present. Checked? = YES for all. Finding = escalation path or explicit rule-out with reason.

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Blank-cell rule: Remediation = exact configuration change required.

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: M1, M2, M3 are simultaneously active for every essential criterion — not alternative paths. M4 pre-assigned by CA. Essential criteria C-01 through C-05 are assigned to SE sections because they require formal table production, which is SE's responsibility regardless of role execution order.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|-------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**SHALL obligations (authored by CA, Phase 0):**
- SHALL-A: TABLE_1 MUST be present. All cells filled. All roles with any privilege on any entity included.
- SHALL-B: TABLE_2 MUST list every sensitive field with explicit FLS status. Null case stated if no FLS active. Not Configured fields in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Effective Scope filled. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 MUST check all four escalation vectors. Rule-outs require specific mechanism + reason.
- SHALL-E: TABLE_5 MUST have at least one named gap with specific field/role/rule. If zero gaps: explicit evidence rows required.

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Lower-Trust Access Baseline

*CS establishes the practical access narrative before SE technical analysis begins. CS does not fill TABLE_1-5.*

**CS-1 — Expected Customer Service access baseline:**
For each entity in scope, describe: (a) which CRUD operations the Customer Service role is expected to perform as part of normal job function; (b) the expected record scope (own records, BU-wide, etc.); (c) which sensitive fields (PII, financial, audit data) CS is expected to need read or write access to and why. This qualitative baseline will be verified or contradicted by SE in Phase 2.

**CS-2 — Sharing rule expectations:**
List every active or expected sharing rule for entities in scope. For each rule state:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? |
|-----------|---------|------------------------|-----------------------|---------------------|

For any Potential Overreach? YES: name the access path and why it may exceed CS job function requirements. SE will confirm or rule out each flagged rule in Phase 2.

**CS-3 — Expected cross-role access differential:**
State the expected access differential between the Customer Service role and a more privileged role (e.g., Sales Manager, System Administrator) on the most sensitive entity. Name the specific fields or operations where CS should have less access, and identify any sharing rule that might unexpectedly close that gap. SE will verify in TABLE_1 and TABLE_3.

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis

*SE executes Sections 1 through 5 using Dataverse-native terminology. Where SE confirms a CS Phase 1 expectation, SE notes confirmation inline. Where SE contradicts a CS expectation, SE adds a CS-EXPECTATION-VIOLATED row to TABLE_5.*

### SE-1 / SHALL-A — Section 1: Role-Operation Matrix

**TABLE_1 — Role-Operation Matrix** (Schema Registry TABLE_1 schema; blank-cell rule applies)

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Include every role with any privilege on any entity in {{topic}}. For the Customer Service role row, note whether TABLE_1 confirms or contradicts the CS Phase 1 baseline for operations and scope.

### SE-2 / SHALL-B — Section 2: Field-Level Security Coverage

**TABLE_2 — FLS Coverage** (Schema Registry TABLE_2 schema; blank-cell rule applies)

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Check Security > Column Security Profiles. Null case: "No column security profiles active. Sensitive fields identified: [list]. All in TABLE_5." Forward Gap? YES to TABLE_5. Note any fields flagged as sensitive by CS in Phase 1.

### SE-3 / SHALL-C — Section 3: Record Access Scope

**TABLE_3 — Record Scope by Role** (Schema Registry TABLE_3 schema; blank-cell rule applies)

| Role | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role present. OWD: Private / Business Unit / Parent-Child BU / Organization.

**Defense-in-depth layer assessment:** For at least one operation, identify the specific Dataverse enforcement layer (1: environment/admin, 2: security role + BU, 3: team membership, 4: column security profiles) that is the effective enforcement point and explain why higher layers do not override it.

### SE-4 / SHALL-D — Section 4: Privilege Escalation Analysis

**TABLE_4 — Escalation Vector Inventory** (Schema Registry TABLE_4 schema; all four vectors required)

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Cross-reference CS Phase 1 sharing rule expectations (CS-2). For each CS-flagged Potential Overreach? YES rule: confirm it as an escalation path or rule it out with a specific reason.

### SE-5 / SHALL-E — Section 5: Security Gap Inventory

**TABLE_5 — Security Gap Inventory** (Schema Registry TABLE_5 schema; blank-cell rule applies)

| # | Gap Type | Entity | Field or Rule | Role | Severity | Remediation |
|---|----------|--------|---------------|------|----------|-------------|

Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED. Remediation = exact configuration change. CS-EXPECTATION-VIOLATED rows name the CS expectation, the actual SE finding, and the remediation step to align them.

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

*CA returns. Each CA-1 row MUST present the Registry schema citation and the preamble row quotation as structurally distinct labeled elements — using labeled lines or labeled sub-items — such that each anchor is independently readable without inferring boundaries from values.*

**CA-1.1 — C-01 verification (completing Phase 0 M4 pre-assignment CA-1.1 as declared in preamble row 1):**
Registry anchor — Schema ID TABLE_1: [Role, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope] — blank cells prohibited.
Preamble anchor — C-01 as authored by CA in Phase 0: TABLE_1 / SE-1 / SHALL-A / CA-1.1 — verifying...
[TABLE_1 present? All cells filled (Granted/Denied/Conditional/N/A)? All roles included? -> PASS / FAIL]

**CA-1.2 — C-02 verification (completing Phase 0 M4 pre-assignment CA-1.2 as declared in preamble row 2):**
Registry anchor — Schema ID TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?] — blank cells prohibited.
Preamble anchor — C-02 as authored by CA in Phase 0: TABLE_2 / SE-2 / SHALL-B / CA-1.2 — verifying...
[TABLE_2 present? Sensitive fields listed with FLS status? Null case stated? Gap? YES rows in TABLE_5? -> PASS / FAIL]

**CA-1.3 — C-03 verification (completing Phase 0 M4 pre-assignment CA-1.3 as declared in preamble row 3):**
Registry anchor — Schema ID TABLE_3: [Role, OWD Baseline, Scope Modifier, Effective Scope, Verified?] — blank cells prohibited.
Preamble anchor — C-03 as authored by CA in Phase 0: TABLE_3 / SE-1+SE-3 / SHALL-C / CA-1.3 — verifying...
[Every TABLE_1 role in TABLE_3? All Effective Scope cells filled? Ambiguous rows in TABLE_5? -> PASS / FAIL]

**CA-1.4 — C-04 verification (completing Phase 0 M4 pre-assignment CA-1.4 as declared in preamble row 4):**
Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity] — all four vectors, Checked? = YES.
Preamble anchor — C-04 as authored by CA in Phase 0: TABLE_4 / SE-4 / SHALL-D / CA-1.4 — verifying...
[TABLE_4 present? All four vectors? Checked? = YES? Each with finding or specific rule-out? -> PASS / FAIL]

**CA-1.5 — C-05 verification (completing Phase 0 M4 pre-assignment CA-1.5 as declared in preamble row 5):**
Registry anchor — Schema ID TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Severity, Remediation] — blank cells prohibited.
Preamble anchor — C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 — verifying...
[TABLE_5 present? Named gap with specific field/role/rule? All remediations exact? -> PASS / FAIL]

**CA Format Compliance Verdict — citing Phase 0:**
Citing: CA-authored Schema Registry (Step 0.1), CA-authored preamble (Step 0.2), Phase 0 by label.
[C-01 through C-05 pass/fail. Overall: COMPLIANT / NON-COMPLIANT. Open items with responsible role.]

---

## V-03 — Single-Axis C: Inertia Framing

**Axis:** Inertia framing — a CONTEXT section opens the prompt naming the manual RBAC audit status quo and its coverage gaps, motivating precision in findings and remediation
**Hypothesis:** Manual Dataverse RBAC audits produce incomplete coverage: cumulative privilege accumulation through role + team + sharing combinations is not traced; FLS gaps on sensitive fields are invisible in the security roles UI; environment-level admin overrides bypass BU-scoped restrictions without visible indicators. Naming these blind spots as the status quo motivates the model to treat each gap as consequential and each remediation as replacing a manual process. The CONTEXT section is structurally isolated from the 4-mechanism enforcement system; it neither adds nor removes any criterion-bearing element. Hypothesis: 16/16 structural criteria pass; C-08 and C-04 depth may improve.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: THE COST OF MANUAL RBAC AUDITS

Manual security audits of Dataverse environments rely on three fragile techniques that this trace replaces:

**Spot-checking the security roles UI.** Reviewers open individual roles and scan privilege levels per entity. This misses cumulative effects: a user holding Role A (BU-scoped Read on Account) who also belongs to Team T (whose team role grants org-wide Read via inheritance) appears safe in the roles UI but has effective org-wide access. No UI view surfaces this combination.

**OWD review without sharing rule cross-reference.** Administrators check owner settings entity-by-entity without evaluating the sharing rules that override those baselines. A Private OWD on Contact combined with a Power Automate-triggered sharing rule grants effective org-wide read to any user who satisfies the trigger condition — which may include low-trust service accounts.

**Post-incident FLS review.** Field-level security gaps on sensitive fields (credit limits, SSNs, compensation data) are typically discovered after a data exposure event. The security roles UI does not surface which sensitive fields lack column security profiles.

This trace performs systematic four-layer coverage: environment/admin roles -> security role + BU scope -> team membership -> field-level security / column profiles. Every escalation vector is named and checked. Every sensitive field receives an explicit FLS status. Every sharing rule is evaluated against the role model it was meant to complement.

---

## ROLE SEQUENCING MANDATE

This output executes in four explicitly labeled phases. Phase labels MUST appear as section headers in the output. Each phase completes fully before the next begins. Phase boundaries MUST include explicit handoff strings naming the next phase and executor.

**PHASE 0 — CA (Compliance Auditor):**
CA executes first and is the sole author of all structural artifacts. CA authors the Schema Registry (Step 0.1) and the Criterion Enforcement Matrix preamble (Step 0.2) in one continuous execution before PHASE 1 begins. CA issues handoff to PHASE 1.

**PHASE 1 — SE (Security Engineer / Dataverse Security Expert):**
Executes second. Performs all security analysis using Dataverse-native terminology exclusively: business units, security roles, owner teams vs. access teams, table permissions, column security profiles, sharing records, environment roles, OWD settings. Issues handoff to PHASE 2.

**PHASE 2 — CS (Customer Success):**
Executes third. Validates lower-trust access and sharing rule conflicts from a practical workflow perspective. Issues handoff to PHASE 3.

**PHASE 3 — CA-1 (CA Verification Pass):**
CA returns. Each CA-1 verification row performs double-anchor reaffirmation: (1) cite Schema Registry entry for the relevant table — schema ID and declared columns; (2) quote preamble row values for that criterion as authored by CA in Phase 0; (3) state verification result. Both anchors appear as structurally distinct labeled elements before the verification statement. CA's terminal verdict cites Phase 0 by label, the Registry, and the preamble.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes steps 0.1 and 0.2 before Phase 1 begins.*

### Step 0.1 — Schema Registry (CA-authored)

**All table schemas declared centrally by CA. Blank-cell prohibition is global — individual tables do not restate it.**

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Blank-cell rule: every cell MUST carry Granted / Denied / Conditional (state condition inline) / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Blank-cell rule: FLS Profile Configured? = Configured / Not Configured. Gap? = YES / NO.

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name] (never blank). Verified? = YES / NO.

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
Blank-cell rule: all four vectors (team inheritance, sharing rules, impersonation, admin/env roles) MUST appear. Checked? = YES for all. Finding = escalation path or explicit rule-out with reason.

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Blank-cell rule: Remediation = the exact configuration change — specific object, location, expected post-fix state. "Review permissions" fails.

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: M1, M2, M3 are simultaneously active for every essential criterion — not alternative paths. M4 pre-assigned by CA.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row (pre-assigned by CA) |
|-----------|-------------------|---------------------|---------------------|----------------------------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**SHALL obligations (authored by CA, Phase 0):**
- SHALL-A: A complete TABLE_1 MUST be present. Every cell MUST carry Granted / Denied / Conditional / N/A. Every role holding any privilege MUST appear as a row.
- SHALL-B: TABLE_2 MUST list every field containing PII, Financial, or Audit-Compliance data with explicit FLS status. When no column security profiles are active, that fact MUST be stated explicitly with sensitive fields identified. Every Not Configured field MUST appear in TABLE_5.
- SHALL-C: Every TABLE_1 role MUST also appear in TABLE_3 with a filled Effective Scope. Roles with ambiguous scope MUST appear in TABLE_5.
- SHALL-D: TABLE_4 MUST contain all four escalation vectors with Checked? = YES. A rule-out requires naming the specific mechanism and the specific reason no escalation path exists.
- SHALL-E: TABLE_5 MUST contain at least one gap row with a named specific field, role, or rule. If zero gaps: explicit evidence rows stating what was checked and confirmed safe.

*Handing to PHASE 1 — SE.*

---

## PHASE 1 — SE: Security Analysis

*SE executes Sections 1 through 5 using Dataverse-native terminology. The CONTEXT section above names the three manual audit blind spots this trace closes — SE findings should be specific enough to replace each one.*

### SE-1 / SHALL-A — Section 1: Role-Operation Matrix

**TABLE_1 — Role-Operation Matrix** (Schema Registry TABLE_1 schema; blank-cell rule applies)

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Include every role with any privilege. Record Scope: Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].

### SE-2 / SHALL-B — Section 2: Field-Level Security Coverage

**TABLE_2 — FLS Coverage** (Schema Registry TABLE_2 schema; blank-cell rule applies)

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Check Security > Column Security Profiles. Null case: state explicitly with sensitive fields listed. Forward Gap? YES rows to TABLE_5. This section closes the CONTEXT post-incident FLS gap.

### SE-3 / SHALL-C — Section 3: Record Access Scope

**TABLE_3 — Record Scope by Role** (Schema Registry TABLE_3 schema; blank-cell rule applies)

| Role | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role present. OWD: Private / Business Unit / Parent-Child BU / Organization. Scope Modifier: security role privilege depth, team membership, or sharing rule.

**Defense-in-depth layer assessment:** For at least one operation, identify the specific Dataverse enforcement layer (1: environment/admin, 2: security role + BU scope, 3: team membership, 4: column security profiles) where access is granted or denied. This directly addresses the CONTEXT spot-checking blind spot — the effective layer may not be the one visible in the roles UI.

### SE-4 / SHALL-D — Section 4: Privilege Escalation Analysis

**TABLE_4 — Escalation Vector Inventory** (Schema Registry TABLE_4 schema; all four vectors required)

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

For each finding: name the combination path (role + team + sharing rule + OWD) that produces the escalation. Rule-outs require the specific break point. This section closes the CONTEXT cumulative privilege blind spot.

### SE-5 / SHALL-E — Section 5: Security Gap Inventory

**TABLE_5 — Security Gap Inventory** (Schema Registry TABLE_5 schema; blank-cell rule applies)

| # | Gap Type | Entity | Field or Rule | Role | Severity | Remediation |
|---|----------|--------|---------------|------|----------|-------------|

Remediation MUST name the exact Dataverse configuration object — e.g., "Create column security profile on [entity].[field] in solution [solution name], restrict to [role] only." Gaps that a manual spot-check would not surface (cumulative privilege, FLS absence, sharing rule override) are especially important to document here with specific remediations.

*Handing to PHASE 2 — CS.*

---

## PHASE 2 — CS: Agent-Workflow and Sharing Rule Validation

**CS-1 — Customer Service access trace:**
State every operation the CS role can perform per entity (CRUD + Assign) and record scope. Name every sensitive field CS can read or write; state whether appropriate to job function or overreach.

**CS-2 — Sharing rule conflict audit:**

| Rule Name | Trigger | Access Granted | Intended? | Overreach? |
|-----------|---------|----------------|-----------|------------|

For each Overreach? YES: name the rule, the unintended access, and the role that benefits. State how the sharing rule interacts with the FLS status from TABLE_2 — a sharing rule that grants access to a field without FLS protection is a double-exposure gap.

**CS-3 — Cross-role differential:**
Compare CS and SE roles on the most sensitive entity for one operation. State whether the differential is expected (least privilege satisfied) or anomalous. Flag any sharing rule that effectively equalizes access between the two roles beyond job function intent.

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

*CA returns. Each CA-1 row MUST present the Registry schema citation and the preamble row quotation as structurally distinct labeled elements — using labeled lines or labeled sub-items — such that the Registry anchor and the Preamble anchor are each independently readable without inferring boundaries from values.*

**CA-1.1 — C-01 verification (completing Phase 0 M4 pre-assignment CA-1.1 as declared in preamble row 1):**
Registry anchor — Schema ID TABLE_1: [Role, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope] — blank cells prohibited.
Preamble anchor — C-01 as authored by CA in Phase 0: TABLE_1 / SE-1 / SHALL-A / CA-1.1 — verifying...
[TABLE_1 present? All cells filled? All roles included? -> PASS / FAIL]

**CA-1.2 — C-02 verification (completing Phase 0 M4 pre-assignment CA-1.2 as declared in preamble row 2):**
Registry anchor — Schema ID TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?] — blank cells prohibited.
Preamble anchor — C-02 as authored by CA in Phase 0: TABLE_2 / SE-2 / SHALL-B / CA-1.2 — verifying...
[TABLE_2 present? Sensitive fields with explicit FLS status? Null case stated? Gap? YES in TABLE_5? -> PASS / FAIL]

**CA-1.3 — C-03 verification (completing Phase 0 M4 pre-assignment CA-1.3 as declared in preamble row 3):**
Registry anchor — Schema ID TABLE_3: [Role, OWD Baseline, Scope Modifier, Effective Scope, Verified?] — blank cells prohibited.
Preamble anchor — C-03 as authored by CA in Phase 0: TABLE_3 / SE-1+SE-3 / SHALL-C / CA-1.3 — verifying...
[Every TABLE_1 role in TABLE_3? Effective Scope filled? Ambiguous in TABLE_5? -> PASS / FAIL]

**CA-1.4 — C-04 verification (completing Phase 0 M4 pre-assignment CA-1.4 as declared in preamble row 4):**
Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity] — all four vectors, Checked? = YES.
Preamble anchor — C-04 as authored by CA in Phase 0: TABLE_4 / SE-4 / SHALL-D / CA-1.4 — verifying...
[TABLE_4 present? All four vectors? Checked? = YES? Each with finding or specific rule-out? -> PASS / FAIL]

**CA-1.5 — C-05 verification (completing Phase 0 M4 pre-assignment CA-1.5 as declared in preamble row 5):**
Registry anchor — Schema ID TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Severity, Remediation] — blank cells prohibited.
Preamble anchor — C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 — verifying...
[TABLE_5 present? Named gap with specific field/role/rule? All remediations exact? -> PASS / FAIL]

**CA Format Compliance Verdict — citing Phase 0:**
Citing: CA-authored Schema Registry (Step 0.1), CA-authored preamble (Step 0.2), Phase 0 by label.
[C-01 through C-05 pass/fail. Overall: COMPLIANT / NON-COMPLIANT. Open items with responsible role.]

---

## V-04 — Combined A+B: Numbered Sub-Steps + CS-First Sequence

**Axis:** Combined — V-01's numbered sub-steps in CA-1 rows with V-02's CS-first role sequence (CA -> CS -> SE -> CA-1)
**Hypothesis:** V-01 tests whether numbered sub-steps pass C-24. V-02 tests whether CS-first ordering maintains 16/16. V-04 tests whether the two surface-level axes compose without interaction effects. The Registry, preamble, and phase-label requirements are unchanged. CA-1 rows use Step 1 / Step 2 / Step 3 format. CS runs before SE. M2 preamble assignments still point to SE sections. Hypothesis: 16/16.

---

You are running a permissions trace signal for: {{topic}}

---

## ROLE SEQUENCING MANDATE

This output executes in four explicitly labeled phases. Phase labels MUST appear as section headers in the output. Each phase completes fully before the next begins. Phase boundaries MUST include explicit handoff strings naming the next phase and executor.

**PHASE 0 — CA (Compliance Auditor):**
CA executes first and is the sole author of all structural artifacts. CA authors the Schema Registry (Step 0.1) and the Criterion Enforcement Matrix preamble (Step 0.2) in one continuous execution before PHASE 1 begins. CA issues handoff to PHASE 1.

**PHASE 1 — CS (Customer Support):**
Executes second. Establishes lower-trust access baseline: expected operations, expected record scope, and expected sharing rule behavior before the technical trace confirms or refutes them. CS does NOT fill TABLE_1-5. Issues handoff to PHASE 2.

**PHASE 2 — SE (Security Engineer / Dataverse Security Expert):**
Executes third. Fills TABLE_1-5 using Dataverse-native terminology: business units, security roles, owner teams vs. access teams, table permissions, column security profiles, sharing records, environment roles, OWD. Confirms or contradicts CS Phase 1 expectations; CS-EXPECTATION-VIOLATED gaps appear in TABLE_5. Issues handoff to PHASE 3.

**PHASE 3 — CA-1 (CA Verification Pass):**
CA returns. Each CA-1 verification row delivers double-anchor reaffirmation as three numbered sub-steps:
- Step 1 — Registry anchor: state the Schema ID and its declared column list from the Schema Registry.
- Step 2 — Preamble anchor: quote the preamble row values for that criterion as authored by CA in Phase 0.
- Step 3 — Verification: state whether each required element is present and the overall result (PASS / FAIL).

Step 1 and Step 2 MUST each be a complete, independently readable statement before Step 3 begins. CA's terminal verdict cites Phase 0 by label, the CA-authored Registry, and the CA-authored preamble.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes steps 0.1 and 0.2 before Phase 1 begins.*

### Step 0.1 — Schema Registry (CA-authored)

**All table schemas declared centrally by CA. Blank-cell prohibition is global.**

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Blank-cell rule: every cell MUST carry Granted / Denied / Conditional (state condition) / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Blank-cell rule: FLS Profile Configured? = Configured / Not Configured. Gap? = YES / NO.

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Blank-cell rule: Effective Scope filled for every row. Verified? = YES / NO.

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
Blank-cell rule: all four vectors (team inheritance, sharing rules, impersonation, admin/env roles) present. Checked? = YES for all. Finding = escalation path or explicit rule-out with reason.

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Blank-cell rule: Remediation = exact configuration change required.

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: M1, M2, M3 are simultaneously active for every essential criterion — not alternative paths. M4 pre-assigned by CA. C-01 through C-05 are assigned to SE sections because they require formal table production regardless of role execution order.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row (pre-assigned by CA) |
|-----------|-------------------|---------------------|---------------------|----------------------------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**SHALL obligations (authored by CA, Phase 0):**
- SHALL-A: TABLE_1 MUST be present. All cells filled. All roles with any privilege included.
- SHALL-B: TABLE_2 MUST list every sensitive field with explicit FLS status. Null case stated if no FLS active. Not Configured fields in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Effective Scope filled. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 MUST check all four escalation vectors. Rule-outs require specific mechanism + reason.
- SHALL-E: TABLE_5 MUST have at least one named gap. If zero gaps: explicit evidence rows required.

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Lower-Trust Access Baseline

*CS establishes the qualitative access narrative before SE technical analysis begins.*

**CS-1 — Expected Customer Service access baseline:**
For each entity in scope: (a) which CRUD operations the Customer Service role is expected to perform; (b) the expected record scope; (c) which sensitive fields CS legitimately needs read or write access to and why.

**CS-2 — Sharing rule expectations:**

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? |
|-----------|---------|------------------------|-----------------------|---------------------|

For any Potential Overreach? YES: name the access path and why it may exceed CS job function. SE will confirm or rule out each flagged rule in Phase 2.

**CS-3 — Expected cross-role access differential:**
State the expected access gap between the Customer Service role and a more privileged role on the most sensitive entity. Name fields or operations where CS should have less access, and identify any sharing rule that might unexpectedly close that gap.

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis

*SE fills TABLE_1-5 using Dataverse-native terminology. Confirms or contradicts CS Phase 1 expectations inline.*

### SE-1 / SHALL-A — Section 1: Role-Operation Matrix

**TABLE_1 — Role-Operation Matrix** (Schema Registry TABLE_1 schema; blank-cell rule applies)

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Every role with any privilege included. For Customer Service row: note confirmation or contradiction of CS Phase 1 baseline.

### SE-2 / SHALL-B — Section 2: Field-Level Security Coverage

**TABLE_2 — FLS Coverage** (Schema Registry TABLE_2 schema; blank-cell rule applies)

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Check column security profiles. Null case: state explicitly with fields listed. Forward Gap? YES to TABLE_5.

### SE-3 / SHALL-C — Section 3: Record Access Scope

**TABLE_3 — Record Scope by Role** (Schema Registry TABLE_3 schema; blank-cell rule applies)

| Role | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role present. **Defense-in-depth layer assessment:** For at least one operation, identify the Dataverse enforcement layer (1-4) that is the effective enforcement point and explain why higher layers do not override it.

### SE-4 / SHALL-D — Section 4: Privilege Escalation Analysis

**TABLE_4 — Escalation Vector Inventory** (Schema Registry TABLE_4 schema; all four vectors required)

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Cross-reference CS Phase 1 CS-2 sharing rule expectations. For each CS-flagged Potential Overreach? YES: confirm as escalation path or rule out with specific reason.

### SE-5 / SHALL-E — Section 5: Security Gap Inventory

**TABLE_5 — Security Gap Inventory** (Schema Registry TABLE_5 schema; blank-cell rule applies)

| # | Gap Type | Entity | Field or Rule | Role | Severity | Remediation |
|---|----------|--------|---------------|------|----------|-------------|

Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED. Remediation = exact configuration change. CS-EXPECTATION-VIOLATED rows name the expectation, the SE finding, and the remediation to align them.

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Numbered-Step Double-Anchor Format Compliance Verification

*CA returns. Each CA-1 row delivers double-anchor reaffirmation as three numbered sub-steps. Step 1 and Step 2 MUST each be a complete, independently readable statement before Step 3 begins.*

**CA-1.1 — C-01 verification (completing Phase 0 M4 pre-assignment CA-1.1 as declared in preamble row 1):**
- Step 1 — Registry anchor: Schema ID TABLE_1, declared columns [Role, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope], blank-cell rule: Granted / Denied / Conditional / N/A.
- Step 2 — Preamble anchor: C-01 as authored by CA in Phase 0 — TABLE_1 / SE-1 / SHALL-A / CA-1.1.
- Step 3 — Verification: TABLE_1 present? All cells filled? All roles included? -> PASS / FAIL

**CA-1.2 — C-02 verification (completing Phase 0 M4 pre-assignment CA-1.2 as declared in preamble row 2):**
- Step 1 — Registry anchor: Schema ID TABLE_2, declared columns [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?], blank-cell rule: FLS Profile Configured? = Configured / Not Configured; Gap? = YES / NO.
- Step 2 — Preamble anchor: C-02 as authored by CA in Phase 0 — TABLE_2 / SE-2 / SHALL-B / CA-1.2.
- Step 3 — Verification: TABLE_2 present? Sensitive fields with FLS status? Null case stated? Gap? YES in TABLE_5? -> PASS / FAIL

**CA-1.3 — C-03 verification (completing Phase 0 M4 pre-assignment CA-1.3 as declared in preamble row 3):**
- Step 1 — Registry anchor: Schema ID TABLE_3, declared columns [Role, OWD Baseline, Scope Modifier, Effective Scope, Verified?], blank-cell rule: Effective Scope and Verified? filled for every row.
- Step 2 — Preamble anchor: C-03 as authored by CA in Phase 0 — TABLE_3 / SE-1+SE-3 / SHALL-C / CA-1.3.
- Step 3 — Verification: Every TABLE_1 role in TABLE_3? Effective Scope filled? Ambiguous in TABLE_5? -> PASS / FAIL

**CA-1.4 — C-04 verification (completing Phase 0 M4 pre-assignment CA-1.4 as declared in preamble row 4):**
- Step 1 — Registry anchor: Schema ID TABLE_4, declared columns [Vector, Checked?, Finding, Severity], blank-cell rule: all four vectors required, Checked? = YES, Finding = path or explicit rule-out.
- Step 2 — Preamble anchor: C-04 as authored by CA in Phase 0 — TABLE_4 / SE-4 / SHALL-D / CA-1.4.
- Step 3 — Verification: TABLE_4 present? All four vectors? Checked? = YES? Each with finding or specific rule-out? -> PASS / FAIL

**CA-1.5 — C-05 verification (completing Phase 0 M4 pre-assignment CA-1.5 as declared in preamble row 5):**
- Step 1 — Registry anchor: Schema ID TABLE_5, declared columns [#, Gap Type, Entity, Field or Rule, Role, Severity, Remediation], blank-cell rule: Remediation = exact configuration change.
- Step 2 — Preamble anchor: C-05 as authored by CA in Phase 0 — TABLE_5 / SE-5 / SHALL-E / CA-1.5.
- Step 3 — Verification: TABLE_5 present? Named gap with specific field/role/rule? All remediations exact? -> PASS / FAIL

**CA Format Compliance Verdict — citing Phase 0:**
Citing: CA-authored Schema Registry (Step 0.1), CA-authored preamble (Step 0.2), Phase 0 by label.
[C-01 through C-05 pass/fail. Overall: COMPLIANT / NON-COMPLIANT. Open items with responsible role.]

---

## V-05 — Combined A+C + Rubric-Verbatim C-24 Language

**Axis:** Combined — V-01's numbered sub-steps (Axis A) with V-03's inertia framing (Axis C), plus Phase 3 mandate uses rubric-exact C-24 language: "each anchor is a separately parseable structural element, not an inline concatenation"
**Hypothesis:** V-01 tests numbered sub-steps. V-03 tests inertia framing. V-05 combines both with maximum C-24 specification fidelity: the Phase 3 mandate quotes the rubric's own structural-separability test condition verbatim, ensuring the model knows what failure looks like ("an inline concatenation") and what passing requires ("a separately parseable structural element"). Standard CA -> SE -> CS -> CA-1 sequence preserved. Hypothesis: 16/16.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: THE COST OF MANUAL RBAC AUDITS

Manual Dataverse RBAC audits miss three systematic blind spots:

**Cumulative privilege through role + team + sharing combinations.** A user with BU-scoped Read on Account via Role A, who is also a member of Team T (whose owner team role grants org-wide Read), has effective org-wide access that appears safe in the security roles UI. Manual spot-checking does not surface this combination.

**Invisible FLS gaps on sensitive fields.** The security roles UI does not show which sensitive fields (SSN, creditlimit, compensation) lack column security profiles. FLS gaps are typically discovered post-incident, not during routine audit.

**Sharing rule overrides of OWD baselines.** A Private OWD on Contact combined with a Power Automate-triggered sharing rule can grant effective org-wide read to accounts meeting the trigger condition. Manual OWD review without sharing rule cross-reference leaves this vector undetected.

This trace closes all three blind spots through systematic four-layer Dataverse coverage: environment/admin roles -> security role + BU scope -> team membership -> field-level security / column profiles.

---

## ROLE SEQUENCING MANDATE

This output executes in four explicitly labeled phases. Phase labels MUST appear as section headers in the output. Each phase completes fully before the next begins. Phase boundaries MUST include explicit handoff strings naming the next phase and executor.

**PHASE 0 — CA (Compliance Auditor):**
CA executes first and is the sole author of all structural artifacts. CA authors the Schema Registry (Step 0.1: all table schemas declared centrally, blank-cell prohibition stated globally) and the Criterion Enforcement Matrix preamble (Step 0.2: M1/M2/M3/M4 columns, M4 row IDs pre-assigned by CA for every essential criterion) in one continuous execution before PHASE 1 begins. CA issues handoff to PHASE 1.

**PHASE 1 — SE (Security Engineer / Dataverse Security Expert):**
Executes second. Performs all security analysis sections using Dataverse-native terminology exclusively: business units, security roles, owner teams vs. access teams, table permissions, column security profiles, sharing records, environment roles, OWD settings. Issues handoff to PHASE 2.

**PHASE 2 — CS (Customer Success):**
Executes third. Validates lower-trust access and sharing rule conflicts. Issues handoff to PHASE 3.

**PHASE 3 — CA-1 (CA Verification Pass):**
CA returns. Each CA-1 verification row delivers double-anchor reaffirmation as three numbered sub-steps. Each anchor is a separately parseable structural element, not an inline concatenation — an evaluator must be able to identify the Registry anchor and the Preamble anchor by their step number alone, without inferring boundaries from values:
- Step 1 — Registry anchor: state the Schema ID and its declared column list from the CA-authored Schema Registry. This step is a complete statement on its own.
- Step 2 — Preamble anchor: quote the preamble row values for that criterion exactly as authored by CA in Phase 0. This step is a complete statement on its own.
- Step 3 — Verification: state whether each required element is present and the overall result (PASS / FAIL).

CA's terminal verdict cites Phase 0 by label, the CA-authored Registry (Step 0.1), and the CA-authored preamble (Step 0.2) as the three structural verification bases.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes steps 0.1 and 0.2 in this phase before any other phase begins.*

### Step 0.1 — Schema Registry (CA-authored)

**All table schemas declared centrally by CA. Blank-cell prohibition is global — individual tables do not restate it.**

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Blank-cell rule: every cell MUST carry Granted / Denied / Conditional (state condition inline) / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Blank-cell rule: FLS Profile Configured? = Configured / Not Configured (never blank). Gap? = YES / NO (never blank).

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name] (never blank). Verified? = YES / NO.

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
Blank-cell rule: all four vectors (team inheritance, sharing rules, impersonation, admin/env roles) MUST appear as rows. Checked? = YES for all. Finding = escalation path or explicit rule-out with reason (never blank).

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Blank-cell rule: Remediation = the exact configuration change required — naming the specific object, location, and expected post-fix state. "Review permissions" or vague advice fails this column.

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: All three mechanisms (M1 format schema, M2 expert role sub-section, M3 SHALL obligation) are simultaneously active for every essential criterion. They are not alternative coverage paths. M4 CA verification row IDs are pre-assigned by CA below and constitute pre-existing obligations that CA-1 rows fulfill as structural completions of this contract.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row (pre-assigned by CA) |
|-----------|-------------------|---------------------|---------------------|----------------------------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**SHALL obligations (authored by CA, Phase 0):**
- SHALL-A: A complete TABLE_1 MUST be present. Every cell MUST carry Granted / Denied / Conditional / N/A. Every role holding any privilege on any entity in {{topic}} MUST appear as a row.
- SHALL-B: TABLE_2 MUST list every field containing PII, Financial, or Audit-Compliance data with explicit FLS status (Configured / Not Configured). When no column security profiles are active, that fact MUST be stated explicitly with sensitive fields identified. Every Not Configured field MUST appear in TABLE_5. This SHALL closes the CONTEXT invisible-FLS-gap blind spot.
- SHALL-C: Every role in TABLE_1 MUST also appear in TABLE_3 with a filled Effective Scope. Roles with ambiguous scope MUST appear in TABLE_5.
- SHALL-D: TABLE_4 MUST contain all four escalation vectors with Checked? = YES. A rule-out requires naming the specific mechanism and the specific reason no path exists. This SHALL closes the CONTEXT cumulative-privilege blind spot.
- SHALL-E: TABLE_5 MUST contain at least one gap row with a named specific field, role, or rule. If zero gaps: explicit evidence rows stating what was checked and confirmed safe.

*Handing to PHASE 1 — SE.*

---

## PHASE 1 — SE: Security Analysis

*SE executes Sections 1 through 5 using Dataverse-native terminology. The three CONTEXT blind spots frame the analysis — findings should be specific enough to replace each manual audit technique named.*

### SE-1 / SHALL-A — Section 1: Role-Operation Matrix

**TABLE_1 — Role-Operation Matrix** (Schema Registry TABLE_1 schema; blank-cell rule applies)

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Include every role with any privilege on any entity in {{topic}}. Record Scope: Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].

### SE-2 / SHALL-B — Section 2: Field-Level Security Coverage

**TABLE_2 — FLS Coverage** (Schema Registry TABLE_2 schema; blank-cell rule applies)

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Check Security > Column Security Profiles for all entities in scope. If no profiles exist: state explicitly — "No column security profiles active. Sensitive fields identified: [list]. All entered in TABLE_5." Forward all Gap? YES rows to TABLE_5.

### SE-3 / SHALL-C — Section 3: Record Access Scope

**TABLE_3 — Record Scope by Role** (Schema Registry TABLE_3 schema; blank-cell rule applies)

| Role | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|--------------|----------------|-----------------|-----------|

Every role from TABLE_1 MUST appear. OWD: Private / Business Unit / Parent-Child BU / Organization. Scope Modifier: security role privilege depth, team membership, or sharing rule.

**Defense-in-depth layer assessment:** For at least one operation, identify the specific Dataverse enforcement layer (1: environment/admin role, 2: security role + BU scope, 3: team membership, 4: column security profiles) where access is granted or denied, and explain why the layers above it do not override. This addresses the CONTEXT spot-checking blind spot — the effective layer may not be the one visible in the roles UI.

### SE-4 / SHALL-D — Section 4: Privilege Escalation Analysis

**TABLE_4 — Escalation Vector Inventory** (Schema Registry TABLE_4 schema; all four vectors required)

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

For each finding: name the full combination path (role + team membership + sharing rule + OWD) that produces the escalation. Rule-outs: name the specific mechanism checked and the break point. This section directly closes the CONTEXT cumulative-privilege blind spot.

### SE-5 / SHALL-E — Section 5: Security Gap Inventory

**TABLE_5 — Security Gap Inventory** (Schema Registry TABLE_5 schema; blank-cell rule applies)

| # | Gap Type | Entity | Field or Rule | Role | Severity | Remediation |
|---|----------|--------|---------------|------|----------|-------------|

Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED. Remediation MUST name the exact Dataverse configuration object — e.g., "Create column security profile on [entity].[field] in solution [name], restrict Write to [role] only." Gaps invisible to manual spot-checking are especially important to surface with specific remediations.

*Handing to PHASE 2 — CS.*

---

## PHASE 2 — CS: Agent-Workflow and Sharing Rule Validation

**CS-1 — Customer Service access trace:**
State every operation the Customer Service role can perform per entity (CRUD + Assign) and record scope. Name every sensitive field the CS role can read or write; state whether appropriate to job function or overreach.

**CS-2 — Sharing rule conflict audit:**

| Rule Name | Trigger | Access Granted | Intended? | Overreach? |
|-----------|---------|----------------|-----------|------------|

For each Overreach? YES: name the unintended access, the role that benefits, and how the sharing rule interacts with the FLS status from TABLE_2. A sharing rule granting access to a field that lacks a column security profile is a double-exposure gap (CONTEXT blind spot 2 + 3 combined).

**CS-3 — Cross-role differential:**
Compare CS and SE roles on the most sensitive entity for one operation. State whether the differential is expected (least privilege satisfied) or anomalous. Flag any case where sharing rules equalize access beyond job function intent.

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Numbered-Step Double-Anchor Format Compliance Verification

*CA returns for the verification pass. Each CA-1 verification row delivers double-anchor reaffirmation as three numbered sub-steps. Each anchor is a separately parseable structural element, not an inline concatenation: Step 1 (Registry anchor) and Step 2 (Preamble anchor) are each complete, independently readable statements identifiable by step number alone. Step 3 (Verification) follows after both anchors are fully stated.*

**CA-1.1 — C-01 verification (completing Phase 0 M4 pre-assignment CA-1.1 as declared in preamble row 1):**
- Step 1 — Registry anchor: Schema ID TABLE_1, declared columns [Role, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope], blank-cell rule: Granted / Denied / Conditional (state condition) / N/A.
- Step 2 — Preamble anchor: C-01 as authored by CA in Phase 0 — TABLE_1 / SE-1 / SHALL-A / CA-1.1.
- Step 3 — Verification: TABLE_1 present? All cells filled with valid values? All roles with any privilege on any entity in {{topic}} included? -> PASS / FAIL

**CA-1.2 — C-02 verification (completing Phase 0 M4 pre-assignment CA-1.2 as declared in preamble row 2):**
- Step 1 — Registry anchor: Schema ID TABLE_2, declared columns [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?], blank-cell rule: FLS Profile Configured? = Configured / Not Configured; Gap? = YES / NO.
- Step 2 — Preamble anchor: C-02 as authored by CA in Phase 0 — TABLE_2 / SE-2 / SHALL-B / CA-1.2.
- Step 3 — Verification: TABLE_2 present? Every sensitive field listed with explicit FLS status? Null case stated if no FLS active? All Gap? YES rows forwarded to TABLE_5? -> PASS / FAIL

**CA-1.3 — C-03 verification (completing Phase 0 M4 pre-assignment CA-1.3 as declared in preamble row 3):**
- Step 1 — Registry anchor: Schema ID TABLE_3, declared columns [Role, OWD Baseline, Scope Modifier, Effective Scope, Verified?], blank-cell rule: Effective Scope = typed scope value; Verified? = YES / NO.
- Step 2 — Preamble anchor: C-03 as authored by CA in Phase 0 — TABLE_3 / SE-1+SE-3 / SHALL-C / CA-1.3.
- Step 3 — Verification: Every TABLE_1 role appears in TABLE_3? All Effective Scope cells filled? Ambiguous scope rows present in TABLE_5? -> PASS / FAIL

**CA-1.4 — C-04 verification (completing Phase 0 M4 pre-assignment CA-1.4 as declared in preamble row 4):**
- Step 1 — Registry anchor: Schema ID TABLE_4, declared columns [Vector, Checked?, Finding, Severity], blank-cell rule: all four vectors required as rows, Checked? = YES for all, Finding = escalation path or explicit rule-out with reason.
- Step 2 — Preamble anchor: C-04 as authored by CA in Phase 0 — TABLE_4 / SE-4 / SHALL-D / CA-1.4.
- Step 3 — Verification: TABLE_4 present? All four vectors as rows? Checked? = YES for all? Each with finding or specific rule-out? -> PASS / FAIL

**CA-1.5 — C-05 verification (completing Phase 0 M4 pre-assignment CA-1.5 as declared in preamble row 5):**
- Step 1 — Registry anchor: Schema ID TABLE_5, declared columns [#, Gap Type, Entity, Field or Rule, Role, Severity, Remediation], blank-cell rule: Remediation = exact configuration change naming specific object, location, and post-fix state.
- Step 2 — Preamble anchor: C-05 as authored by CA in Phase 0 — TABLE_5 / SE-5 / SHALL-E / CA-1.5.
- Step 3 — Verification: TABLE_5 present? At least one named gap with specific field/role/rule? All remediations exact (not vague)? -> PASS / FAIL

**CA Format Compliance Verdict — citing Phase 0:**
This verdict cites the CA-authored Schema Registry (Step 0.1), the CA-authored preamble (Step 0.2), and Phase 0 by label as the three structural verification bases. The double-anchor format in CA-1.1 through CA-1.5 used numbered sub-steps to ensure each anchor was a separately parseable structural element, not an inline concatenation.
[State: C-01 through C-05 pass/fail counts. Overall: COMPLIANT / NON-COMPLIANT. List any open items with responsible role.]
