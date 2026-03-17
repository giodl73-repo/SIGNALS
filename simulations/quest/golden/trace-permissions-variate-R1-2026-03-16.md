# trace-permissions — Round 1 Variations

**Skill**: trace-permissions — Trace who can do what through RBAC, security roles, teams, and field-level security.
**Rubric**: v1 — C-01..C-09 (4 essential / 3 recommended / 2 aspirational)
**Date**: 2026-03-16
**Round**: R1 — first variate pass, rubric v1

---

## Variation Design Notes

The v1 rubric has 9 criteria. Key tensions to stress-test:

- **C-01 (Operation-Role Matrix)** rewards explicit matrix or equivalent table/list. Prose role
  descriptions tend to produce narrative permission summaries rather than enumerable cell values.
  A prompt that structurally forces a table gets C-01 "for free"; prose-first prompts must
  explicitly mandate the matrix or risk a C-01 miss.

- **C-02 (FLS Coverage)** is the most silently violated criterion. When no FLS is configured,
  a prompt that says "identify FLS restrictions" produces silence — the null case is omitted.
  The pass condition allows "all fields available" only if *explicitly justified*. Prompts must
  force the null-case declaration.

- **C-04 (Gap/Risk Identification)** is essential and the highest-value discriminator. Outputs
  that only confirm what is allowed have zero value. Every prompt variation must explicitly
  motivate gap-hunting — either through role instruction, structural requirement, or inertia
  framing.

- **C-05 (Privilege Escalation Path)** is recommended, not essential, because a clean security
  configuration can legitimately have no escalation path. Variations that treat escalation as
  optional risk producing outputs where the check is silently omitted rather than explicitly
  cleared.

**Single-axis variations: V-01, V-02, V-03**
**Combination variations: V-04 (role sequence + lifecycle emphasis), V-05 (output format + inertia framing)**

---

## Criterion Hypothesis Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Operation-Role Matrix | YES | PARTIAL | YES | YES | YES |
| C-02 FLS Coverage (null case explicit) | YES | YES | YES | YES | YES |
| C-03 Record Accessibility Scope | YES | YES | PARTIAL | YES | YES |
| C-04 Gap or Risk Identification | YES | YES | YES | YES | YES |
| C-05 Privilege Escalation Path | YES | PARTIAL | PARTIAL | YES | YES |
| C-06 Role Hierarchy Respected | YES | PARTIAL | PARTIAL | YES | YES |
| C-07 Remediation Suggestions | YES | YES | YES | YES | YES |
| C-08 Cross-Entity Cascade | PARTIAL | YES | - | PARTIAL | YES |
| C-09 Structured Summary Table | PARTIAL | YES | - | YES | YES |

---

## V-01 — Single Axis: Role Sequence (SE-First, No CA Meta-Phase)

**Axis**: Role sequence — Security Engineer leads the entire analysis; Customer Service provides
a lower-trust perspective second; no separate Compliance Auditor meta-phase.

**Hypothesis**: SE-first ordering produces richer gap detection than CA-first because the
security engineer maps the actual ground state (what the platform actually allows) before any
expectation baseline is established. When CA runs first, CS expectations anchor the analysis
and the SE can confirm or contradict them; when SE runs first, the analysis is unconstrained
by expectations and is more likely to surface blind spots the CS baseline would have missed.
Trade-off: without a CA verification phase, structural compliance gaps in the output are not
caught.

---

You are running a permissions trace signal for: {{topic}}

---

### ROLE: SECURITY ENGINEER (Dataverse Security Expert)

You are the Security Engineer. Execute the full technical permissions analysis in privilege-tier
descent order — admin-tier roles first, custom roles second, restricted roles last.

**Section SE-1 — Role-Operation Matrix**

Produce a table: Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope

Tier values: Admin / Custom / Restricted. Cell values: Granted / Denied / Conditional (inline condition) / N/A.
No blank cells. Rows ordered: Admin tier first, Custom tier second, Restricted tier last.

**Section SE-2 — Field-Level Security Coverage**

For each entity in scope, enumerate every PII, Financial, and Audit-Compliance field.
For each field: (a) is a column security profile configured? (b) which roles can read it? (c) which roles can write it? (d) is this a gap?

Null case obligation: if no column security profiles are active on {{topic}}, state this explicitly:
"No column security profiles configured. Sensitive fields identified: [list]. All are exposed to any role with entity access."

**Section SE-3 — Record Scope by Role**

For each role in the matrix: (a) the OWD baseline; (b) any scope modifier from team membership or role depth; (c) the effective scope (Own / BU / Parent-Child BU / Org-wide / Team-scoped).

For roles where team membership expands scope beyond the base role setting, flag the expansion explicitly.

**Section SE-4 — Privilege Escalation Vectors**

Check all four escalation vectors. For each: confirm or rule out with specific evidence.

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Rule-out format: "Checked [vector]: no path found because [specific mechanism and reason]."
Escalation path format: "[Role] -> [Mechanism] -> [Elevated access achieved]"

**Section SE-5 — Security Gap Inventory**

Produce a gap table: # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation

Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED
Severity: CRITICAL / HIGH / MEDIUM
Remediation: exact object + exact location + expected post-fix state. Generic observations (e.g., "add FLS to revenue fields") do not pass — name the exact field and the exact role to restrict.

At least one named gap must appear. If no gaps exist, produce explicit evidence rows demonstrating why
each gap type was checked and cleared.

---

### ROLE: CUSTOMER SERVICE (Lower-Trust Baseline Review)

You are the Customer Service reviewer. After reading the SE analysis, for each entity in scope:

1. For each operation the CS role is expected to perform: confirm or flag the SE findings.
2. Identify any access the SE mapped to the CS role that exceeds what the job function requires.
3. For each sharing rule that grants access to CS users: flag whether the access is appropriate or overreaching.

State at least one entity and operation where the CS role has less access than a higher-privilege role,
and confirm this differential is expected.

---

## V-02 — Single Axis: Output Format (Prose-Narrative, Closing Summary Table)

**Axis**: Output format — narrative prose sections per topic, single structured summary table
at the close instead of inline tables throughout.

**Hypothesis**: Prose-first format reduces blank-cell structural failures and produces more
readable diagnostic text (especially for gap descriptions). The trade-off is that C-01
(Operation-Role Matrix) is harder to satisfy in prose without an explicit mandate to include
a matrix; and C-09 (Structured Summary Table) is pushed to the close where it may be omitted.
This variation explicitly mandates both a matrix in Section 1 and a closing table to keep C-01
and C-09 in scope despite the prose register.

---

You are running a permissions trace signal for: {{topic}}

You are a Dataverse security expert and Customer Service domain specialist running a joint
permissions analysis. Your output is a diagnostic document written in professional technical
prose. One structured table appears in Section 1 (the role-operation matrix) and one at the
close (the summary table). All other sections are prose paragraphs.

---

### Section 1 — Who Can Do What: Role-Operation Matrix

Produce a role-operation matrix table: Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope.

After the table, write one paragraph per role tier (Admin / Custom / Restricted) summarizing
what each tier can do and why.

### Section 2 — Field-Level Security Analysis

Write 2-4 paragraphs describing the FLS landscape for {{topic}}. Cover:
- Which fields carry PII, Financial, or Audit-Compliance sensitivity
- Whether column security profiles are configured for each sensitive field
- Which roles can read and write each sensitive field
- Where gaps exist (fields reachable by roles that should not have access)

Null case: if no FLS is configured on {{topic}}, state this explicitly in the opening sentence:
"No column security profiles are active on {{topic}}. The following sensitive fields are therefore
accessible to any role with entity read/write access: [list]."

### Section 3 — Record Scope and Team Membership Effects

Write 2-4 paragraphs describing how record scope works for each role. Cover:
- The OWD baseline per entity
- How team membership modifies effective scope for specific roles
- Where a role's effective scope exceeds what the base role setting implies

If team membership expands any role's effective scope, describe the expansion path in the
format: "[Role] + [Team] → [Effective scope] (base role scope was [base scope])."

### Section 4 — Privilege Escalation Analysis

Write 2-4 paragraphs addressing each escalation vector: team inheritance, sharing rules,
impersonation (Act on Behalf Of), and admin/environment role overrides.

For each vector: state whether an escalation path exists or was cleared, and the evidence.
If an escalation path exists, describe it as: "[Starting role/user] → [Intermediate mechanism] → [Elevated access reached]."
If cleared: "[Vector] was checked. No path exists because [specific mechanism and reason]."

### Section 5 — Security Gaps and Remediations

Write one paragraph per identified gap. Each paragraph names:
- The gap type (MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED)
- The specific entity, field, role, and tier affected
- The severity (CRITICAL / HIGH / MEDIUM) with justification
- A specific remediation: the exact object to create/modify and the exact expected post-fix state

At least one gap must be named. Generic observations do not satisfy this section.

### Cross-Entity Cascade (if applicable)

If the entities in scope include parent-child relationships, describe at least one cross-entity
cascade effect: the parent entity, the child entity, the mechanism (cascade sharing, lookup
field, related record access), and whether the resulting access is appropriate.

### Closing Summary Table

| Operation | Role | FLS Status | Record Scope | Gap? |
|-----------|------|------------|--------------|------|

One row per combination of operation and role that was analyzed. FLS Status: PASS / FAIL / PARTIAL / N/A.
Gap? = YES / NO. This table must cover all operations and roles discussed in Sections 1-5.

---

## V-03 — Single Axis: Phrasing Register (Imperative/Conversational, No Role Personas)

**Axis**: Phrasing register — direct second-person imperatives, no role-persona framing.
The prompt describes what to produce and what constraints to satisfy; it does not assign
named roles (CA, CS, SE) or ask the model to adopt a persona.

**Hypothesis**: Imperative register without persona framing produces cleaner, more direct
outputs because the model is not managing persona transitions and handoff acknowledgments.
The trade-off: C-02 null-case coverage and C-05 escalation vector completeness depend more
heavily on explicit constraint language because there is no SE persona whose job is to
find gaps. This variation compensates with explicit constraint lines ("you must state
explicitly whether each vector was confirmed or cleared").

---

You are running a permissions trace signal for: {{topic}}

Trace who can do what through RBAC, security roles, teams, and field-level security.
For each operation: which roles can perform it, which fields are visible, which records are accessible.
Identify privilege escalation paths, missing FLS, team membership gaps, and sharing rule conflicts.

---

**Step 1 — Build the role-operation matrix.**

List every security role in scope for {{topic}}. For each role, for each CRUD and platform operation
(Create / Read / Write / Delete / Append / AppendTo / Assign / Share): state Granted, Denied, or
Conditional (with the condition inline). Include the record scope for each role.
Produce this as a table. No blank cells. Tier the rows: Admin tier first, then Custom, then Restricted.

**Step 2 — Audit field-level security.**

List every field in scope that carries PII, Financial, or Audit-Compliance sensitivity.
For each field: is a column security profile configured? Which roles can read it? Which roles can write it?

You must explicitly state the null case if it applies:
"No column security profiles are configured on {{topic}}. These sensitive fields are exposed to any
role with entity access: [list each field]."

Do not omit a field because no FLS exists on it. Missing FLS is itself the finding.

**Step 3 — Map record scope per role.**

For each role in the matrix: state the OWD baseline, any scope modifier from team membership, and
the resulting effective scope (Own / BU / Parent-Child BU / Org-wide / Team-scoped).

For any role where team membership expands scope beyond the base role configuration, state the
expansion explicitly: "[Role] + [Team name] → [Effective scope]. Base role scope was [base scope]."

**Step 4 — Check privilege escalation vectors.**

For each of the four escalation vectors, state whether a path was confirmed or cleared:

1. Team inheritance — does any team membership grant elevated access to a lower-privilege role?
2. Sharing rules — does any sharing rule override the OWD baseline in a way that grants
   broader access than the role's security level implies?
3. Impersonation (Act on Behalf Of) — is any service account or application user able to act
   on behalf of a higher-privilege identity?
4. Admin/environment role override — does any admin-equivalent role bypass lower-tier controls?

For each: either trace the path ("[Role] → [Mechanism] → [Elevated access]") or clear it with
evidence ("No path: [specific mechanism and reason]"). You must produce a verdict for all four.

**Step 5 — List all security gaps.**

For each gap found in Steps 1-4, name it:
- Gap type (MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED)
- The specific entity, field or rule, role, and tier
- Severity (CRITICAL / HIGH / MEDIUM)
- Remediation: the exact object to configure, exactly where, and what the post-fix state will be

At least one gap must appear. If you genuinely find no gaps, explain why each gap type was
checked and cleared with specific evidence. "No issues found" without evidence does not pass.

---

## V-04 — Combination: Role Sequence (SE→CS) + Explicit Lifecycle Gates

**Axes combined**: Role sequence (SE leads, CS reviews) + Lifecycle emphasis (explicit phase
gates with commit statements between phases, preventing phase-skip and ensuring each phase
fully closes before the next begins).

**Hypothesis**: Combining SE-first ordering with explicit phase gates addresses two failure
modes simultaneously: (a) SE-first prevents CS expectations from anchoring the gap analysis;
(b) explicit phase gates with commit statements prevent the model from telescoping phases —
producing a brief note where a full section was required. The commit statement forces the model
to explicitly complete each section before moving on.

The phase structure is: PHASE 1 (SE: full technical analysis) → GATE-1 → PHASE 2 (CS: lower-trust
review) → GATE-2 → PHASE 3 (CA: format compliance verification).

---

You are running a permissions trace signal for: {{topic}}

---

### PHASE 1 — SE: Technical Permissions Analysis (privilege-tier descent order)

*Complete all five SE sections before writing GATE-1. Do not begin PHASE 2 until GATE-1 is written.*

**SE-0 — Admin-Tier Inventory**

List all admin-equivalent roles (System Administrator, Environment Admin, any admin-equivalent
custom roles). For each: record scope and whether they bypass lower-tier controls such as
column security profiles. This ceiling is referenced by all subsequent sections.

**SE-1 — Role-Operation Matrix**

TABLE_1: Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope.
Tier values: Admin / Custom / Restricted. Cell values: Granted / Denied / Conditional (inline) / N/A.
No blank cells. Rows ordered Admin-first, Custom-second, Restricted-last.

**SE-2 — Field-Level Security**

Three-step FLS audit: (1) identify every PII, Financial, and Audit-Compliance field in scope;
(2) for each, state whether a column security profile is configured; (3) for fields without FLS
on sensitive categories, forward them to SE-5 as MISSING-FLS gaps.

Null-case mandate: if no column security profiles exist, open this section with the null statement:
"No column security profiles configured on {{topic}}. Sensitive fields with unrestricted access: [list]."

Note: System Administrator bypasses column security profiles (see SE-0 ceiling). Document as a
defense-in-depth consideration, not a gap, unless a non-admin role also has unrestricted access.

**SE-3 — Record Scope by Role**

TABLE_3: Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?
Effective Scope values: Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].
Every role in TABLE_1 must appear in TABLE_3. Flag any role where effective scope exceeds
the base role configuration due to team membership.

**SE-4 — Escalation Vectors**

TABLE_4: Vector | Checked? | Finding | Severity.
Vectors: Team inheritance / Sharing rules / Impersonation (Act on Behalf Of) / Admin-role override.
All four Checked? = YES. Finding format: "[Role] → [Mechanism] → [Elevated access]" for confirmed;
"Checked [vector]: no path because [specific reason]" for ruled-out. Every Finding cell populated.

**SE-5 — Gap Inventory**

TABLE_5: # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation.
Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED.
Remediation: exact object + exact location + expected post-fix state. At least one gap required.

---

**GATE-1 — SE Phase Complete**

SE confirms: TABLE_1 populated (all cells)? TABLE_3 all roles present? TABLE_4 all four vectors checked?
TABLE_5 at least one named gap? If any answer is NO, complete the missing section before crossing GATE-1.

*[SE: PHASE 1 complete. Handing to PHASE 2 — CS.]*

---

### PHASE 2 — CS: Lower-Trust Baseline Review

*Complete all CS sections before writing GATE-2.*

**CS-1 — Expected CS Access Baseline**

For each entity in scope: which CRUD operations are expected as part of normal CS job function?
What is the expected record scope? Which sensitive fields does CS legitimately need to read or write?

**CS-2 — Sharing Rule Expectations**

For each sharing rule identified by SE: is the access granted intended for CS users?
Flag any sharing rule that grants CS users access beyond their job scope as Potential Overreach.
For each Potential Overreach: name the access path and the most likely over-reached population.

**CS-3 — Cross-Role Differential Check**

State at least one entity and operation where the CS role has less access than a higher-privilege role.
Confirm this differential is intentional. If SE's TABLE_1 contradicts any CS expectation, flag the
contradiction here and add a CS-EXPECTATION-VIOLATED gap to TABLE_5 via SE amendment.

---

**GATE-2 — CS Phase Complete**

CS confirms: CS-1 covers all entities? CS-2 addresses all sharing rules in SE-4?
CS-3 includes at least one confirmed differential? If not, complete before crossing GATE-2.

*[CS: PHASE 2 complete. Handing to PHASE 3 — CA.]*

---

### PHASE 3 — CA: Format Compliance Verification

*CA verifies structural completeness only. No new analysis.*

For each criterion:
- C-01: TABLE_1 present? All cells filled? Tier column populated? Rows ordered by tier? PASS / FAIL
- C-02: TABLE_2 or FLS section present? Null case explicit if applicable? Missing-FLS gaps in TABLE_5? PASS / FAIL
- C-03: TABLE_3 present? Every TABLE_1 role in TABLE_3? Effective Scope filled? PASS / FAIL
- C-04: TABLE_4 present? All four vectors? Checked? = YES for all? Findings populated? PASS / FAIL
- C-05: TABLE_5 present? At least one named gap? Remediations specific (not generic)? PASS / FAIL

**CA Verdict**: COMPLIANT / NON-COMPLIANT. If NON-COMPLIANT: list open items with responsible role.

---

## V-05 — Combination: Output Format (Table-First) + Inertia Framing (Manual Audit Blind Spots)

**Axes combined**: Output format (tables lead the output; prose is explanation, not structure) +
inertia framing (the primary competitor is "doing it manually", and the manual audit blind spots
are stated upfront as the motivation for each table produced).

**Hypothesis**: When the prompt names what manual reviews *miss* before asking for the analysis,
the model has a concrete target for gap identification. C-04 (gap identification) and C-05
(escalation path) scores highest when the model understands why those gaps are hard to find
manually. Inertia framing converts gap-hunting from a generic instruction into a motivated search
against a named failure mode.

The format design: tables produced in the exact order they are needed to surface blind spots,
with one sentence before each table naming the blind spot the table closes.

---

You are running a permissions trace signal for: {{topic}}

---

## WHY THIS TRACE EXISTS: THREE MANUAL AUDIT BLIND SPOTS

Manual security reviews of Dataverse environments routinely miss three failure scenarios.
This trace is designed to surface all three.

**Blind spot 1 — Post-incident FLS gap**: Column security profiles are not auditable from
the security roles UI. Sensitive fields (credit limits, compensation data, SSNs, contact
identifiers) remain readable and writable by any role unless a column security profile
explicitly restricts them. Gaps are discovered after data exposure, not before.

**Blind spot 2 — Cumulative privilege accumulation**: A user holding a BU-scoped security
role who also belongs to an owner team whose team role grants org-wide access has effective
org-wide access. No single Dataverse UI view surfaces the combined effective access produced
by role + team + OWD combination. Spot-checking individual roles misses cross-role
accumulation through team membership.

**Blind spot 3 — OWD-sharing-rule override**: Administrators check OWD settings
entity-by-entity without evaluating the sharing rules that silently override those baselines.
A Private OWD on Case combined with a Power Automate-triggered sharing rule can grant
effective org-wide read to users who satisfy the trigger condition — including low-trust
service accounts not intended to have broad access.

Each table below closes one or more of these blind spots.

---

**TABLE 1 — Role-Operation Matrix** *(closes: baseline required for all three blind spots)*

Columns: Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope
Tier values: Admin / Custom / Restricted. Cell values: Granted / Denied / Conditional (inline) / N/A.
No blank cells. Order: Admin tier first, then Custom, then Restricted.

After the table: one sentence per tier noting any admin capability that bypasses lower-tier controls.

---

**TABLE 2 — Field-Level Security Coverage** *(closes: Blind spot 1 — Post-incident FLS gap)*

Columns: Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?
Categories: PII / Financial / Audit-Compliance / Other-Sensitive.
FLS Profile Configured?: Configured / Not Configured — never blank.
Gap?: YES / NO — never blank. All Gap? = YES rows are forwarded to TABLE 5.

Null-case mandate: if no column security profiles exist for {{topic}}, the first data row of TABLE 2
must read: Entity=[entity] | Field=[field] | Category=[category] | FLS Profile Configured?=Not Configured.
Opening the table with a prose paragraph instead of a data row fails this mandate.

---

**TABLE 3 — Record Scope by Role** *(closes: Blind spot 2 — Cumulative privilege accumulation)*

Columns: Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?
Effective Scope values: Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].
Every TABLE 1 role must appear. Scope Modifier = team name + how it expands scope, or "None".
Verified? = YES / NO — record any role where effective scope could not be confirmed as NO and flag it.

After the table: for every role where Effective Scope > role-only scope, write one sentence:
"[Role] acquires [scope] through [team/rule name]. Base role scope was [base scope]."

---

**TABLE 4 — Escalation Vector Inventory** *(closes: Blind spot 2 + Blind spot 3)*

Columns: Vector | Checked? | Finding | Severity
Vectors: Team inheritance / Sharing rules / Impersonation (Act on Behalf Of) / Admin-role override.
All four Checked? = YES — this is not optional.
Finding format for confirmed path: "[Role] → [Mechanism] → [Elevated access achieved]"
Finding format for cleared vector: "Checked [vector]: no path because [specific reason and mechanism]"
Severity for cleared vectors: N/A.

After the table: for each confirmed escalation path, cite the specific Blind spot it instantiates.

---

**TABLE 5 — Security Gap Inventory** *(consolidates all gaps from TABLE 2, TABLE 3, TABLE 4)*

Columns: # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation
Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED
Severity: CRITICAL / HIGH / MEDIUM
Remediation: exact object name + exact location (entity, column, rule, team) + expected post-fix state.
"Restrict access to revenue data" fails — "Create column security profile 'RevenueSensitive',
restrict Write on estimatedrevenue to Sales Manager role only" passes.

At least one row required. If no gaps exist, produce evidence rows with Gap Type = CLEARED and
Finding = the specific check performed.

---

**Closing Summary**

| Operation | Role | FLS Verdict | Record Scope | Escalation Risk | Gap? |
|-----------|------|-------------|--------------|-----------------|------|

One row per operation-role combination traced. FLS Verdict: PASS / FAIL / PARTIAL / N/A.
Escalation Risk: HIGH / MEDIUM / LOW / NONE. This table must be consistent with TABLE 1-5.

---

*Trace complete. All three blind spots addressed: TABLE 2 (Blind spot 1), TABLE 3+4 (Blind spot 2), TABLE 4 (Blind spot 3).*
