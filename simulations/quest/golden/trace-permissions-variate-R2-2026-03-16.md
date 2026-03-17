# trace-permissions — Round 2 Variations

**Skill**: trace-permissions — Trace who can do what through RBAC, security roles, teams, and field-level security.
**Rubric**: v2 — C-01..C-12 (4 essential / 3 recommended / 5 aspirational)
**Date**: 2026-03-16
**Round**: R2 — second variate pass, rubric v2
**Supersedes**: prior R2 file (targeted incorrect C-11/C-12 definitions from pre-v2 rubric)

---

## Context: What Changed from R1

R1 against rubric v1 produced V-05 as champion (95 pts). Three new aspirational criteria were
extracted from V-05 excellence signals and added to rubric v2:

| New Criterion | What it Requires |
|---------------|-----------------|
| C-10 Blind-Spot-Labeled Tables | Each table/section header names the specific failure mode it closes — e.g., `[CLOSES: FLS-GAP]` — not a generic label like "FLS Analysis" |
| C-11 Data-Row Null-Case Mandate | The null case appears as an explicit DATA ROW in the relevant table — not as a prose disclaimer before the table |
| C-12 Escalation Risk Column | The closing summary table includes Escalation Risk (HIGH/MEDIUM/LOW/NONE) with every row populated and a declared scale |

**R1 V-05 produced these signals implicitly.** R2 variations make each mechanism explicit and
structurally unreachable by omission. Three single-axis variations (V-01, V-02, V-03) isolate
each new criterion. Two combination variations (V-04, V-05) layer the mechanisms.

---

## Variation Design Notes

The v2 rubric has 12 criteria. Key tensions for R2:

- **C-10 (Blind-Spot Labels)** is aspirational because an output without labeled tables can still
  pass all essential and recommended bars. The question is: what structural instruction produces
  the label reliably? R1 V-05 produced closes annotations on table headers naturally from the
  inertia framing. V-01 tests whether making the label a required schema element (separate from
  inertia framing) produces the same signal.

- **C-11 (Null-Case Row)** fails silently — the model produces prose disclaimers ("No FLS
  configured") instead of data rows because it doesn't know what a null row looks like. V-02
  tests whether providing an exact null-case row template for each table eliminates this failure
  mode entirely.

- **C-12 (Escalation Risk Column)** is present in R1 V-05 but the most common failure mode is:
  column exists but rows are blank, or scale is undefined so values are inconsistent. V-03 tests
  whether pre-declaring the scale with an explicit auto-fail condition ("any blank cell = table
  fails") prevents this.

- **C-10 + C-11 combination (V-04)** tests whether both format-level rules can be layered onto
  a different structural backbone (SE-first phase structure from R1 V-04) without the full
  inertia framing, and whether the combination produces aspirational signals independently.

- **Full integration (V-05)** locks in all three mechanisms on the R1 V-05 base structure,
  converting implicit signals into structural requirements that cannot be silently omitted.

**Single-axis variations: V-01, V-02, V-03**
**Combination variations: V-04 (C-10 + C-11), V-05 (full integration)**

---

## Criterion Hypothesis Matrix

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|------|------|------|------|------|
| C-01 Operation-Role Matrix | YES | YES | YES | YES | YES |
| C-02 FLS Coverage (null case explicit) | YES | YES | YES | YES | YES |
| C-03 Record Accessibility Scope | YES | YES | YES | YES | YES |
| C-04 Gap or Risk Identification | YES | YES | YES | YES | YES |
| C-05 Privilege Escalation Path | YES | YES | YES | YES | YES |
| C-06 Role Hierarchy Respected | YES | YES | PARTIAL | YES | YES |
| C-07 Remediation Suggestions | YES | YES | YES | YES | YES |
| C-08 Cross-Entity Cascade | PARTIAL | PARTIAL | - | PARTIAL | YES |
| C-09 Structured Summary Table | YES | YES | YES | YES | YES |
| C-10 Blind-Spot-Labeled Tables | YES | PARTIAL | - | YES | YES |
| C-11 Data-Row Null-Case Mandate | PARTIAL | YES | PARTIAL | YES | YES |
| C-12 Escalation Risk Column | YES | YES | YES | PARTIAL | YES |

---

## V-01 — Single Axis: C-10 — Blind-Spot Label as Required Schema Element

**Axis**: C-10 structural enforcement — every table header carries a `[CLOSES: <label>]`
annotation declared as a required part of the table's schema entry, not a stylistic
suggestion. The Blind Spot Registry defines valid labels. Paraphrasing a registered label
is declared as a structural failure.

**Hypothesis**: When closes labels are declared as table schema metadata rather than
supplementary annotation, the model produces them reliably because they read as mandatory
rather than optional. R1 V-05 produced closes annotations naturally from inertia framing;
V-01 tests whether the label mandate can stand alone without the inertia framing narrative —
making C-10 achievable in contexts where a verbose blind-spot preamble is not appropriate.

---

You are running a permissions trace signal for: {{topic}}

---

## BLIND SPOT REGISTRY

Labels for all `[CLOSES: <label>]` annotations in this trace. Use verbatim — character-for-character.
A section or table header missing a closes annotation is structurally incomplete.

- `FLS-GAP` — Column security profiles are not auditable from the security roles UI; administrators
  discover missing FLS only after a data exposure event reveals a sensitive field was readable or
  writable by an unintended role.
- `CUMULATIVE-PRIVILEGE` — A user holding a BU-scoped role who also belongs to an owner team with
  org-wide access has effective org-wide access. No single Dataverse UI view surfaces the combined
  access from role + team + OWD. Spot-checking individual roles misses cross-role accumulation.
- `SHARING-OVERRIDE` — Administrators audit OWD settings entity-by-entity without cross-referencing
  the sharing rules that silently override those baselines. A Private OWD combined with an active
  sharing rule can grant effective org-wide read to users satisfying the trigger condition.

**Label format rule**: Every table and major section header MUST include `[CLOSES: <label>]` as a
suffix using one or more registry labels. Example:

> `**TABLE 2 — Field-Level Security Coverage [CLOSES: FLS-GAP]**`

A section header without a closes annotation is structurally incomplete. At the end of the trace,
list any section missing a closes label as NON-COMPLIANT.

---

### ROLE: SECURITY ENGINEER (Dataverse Security Expert)

Execute the full technical permissions analysis in privilege-tier descent order.

**SE-0 — Admin-Tier Inventory and Escalation Vectors [CLOSES: CUMULATIVE-PRIVILEGE, SHARING-OVERRIDE]**

List all admin-equivalent roles (System Administrator, Environment Admin, any admin-equivalent
custom roles). For each: record scope and whether the role bypasses lower-tier controls such as
column security profiles. This ceiling is referenced by all subsequent sections.

Escalation Vector Table [CLOSES: CUMULATIVE-PRIVILEGE, SHARING-OVERRIDE]

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

All four Checked? = YES. No blank Finding cells.
Finding for confirmed path: `[Role] -> [Mechanism] -> [Elevated access achieved]`
Finding for cleared vector: `Checked [vector]: no path because [specific reason and mechanism]`

**TABLE 1 — Role-Operation Matrix [CLOSES: baseline required before FLS-GAP, CUMULATIVE-PRIVILEGE, SHARING-OVERRIDE]**

Columns: Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope
Tier: Admin / Custom / Restricted. Cells: Granted / Denied / Conditional (condition inline) / N/A.
No blank cells. Order: Admin tier first, Custom second, Restricted last.

**TABLE 2 — Field-Level Security Coverage [CLOSES: FLS-GAP]**

For every PII, Financial, and Audit-Compliance field in scope.

Columns: Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?
FLS Profile Configured?: Configured / Not Configured — never blank.
Gap?: YES / NO — never blank.

Null-case obligation: if no column security profiles are active on {{topic}}, state explicitly:
"No column security profiles configured on {{topic}}. Sensitive fields with unrestricted access: [list each field by name]."
Missing FLS is itself the finding — do not omit a field because no profile exists.

**TABLE 3 — Record Scope by Role [CLOSES: CUMULATIVE-PRIVILEGE]**

Columns: Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?
Every TABLE 1 role must appear, ordered by Tier.
Effective Scope: Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].
For any role where team membership expands scope beyond base role: flag the expansion explicitly.
Verified? = YES / NO. Record NO for any role where effective scope could not be confirmed.

**TABLE 5 — Security Gap Inventory [CLOSES: FLS-GAP, CUMULATIVE-PRIVILEGE, SHARING-OVERRIDE]**

Columns: # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation
Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED
Severity: CRITICAL / HIGH / MEDIUM
Remediation: exact object name + exact location (entity, field, column security profile, team,
rule) + expected post-fix state. Generic observations do not pass — name the exact field and
exact role to restrict.

At least one gap required. If genuinely none, produce rows with Gap Type = CLEARED and the
specific check performed for each gap type.

---

### ROLE: CUSTOMER SERVICE (Lower-Trust Perspective)

**CS-1 — Expected CS Access Baseline**

For each entity in scope: which CRUD operations are expected for normal CS job function?
Expected record scope? Which sensitive fields does CS legitimately need to read or write?

**CS-2 — Sharing Rule Overreach Check [CLOSES: SHARING-OVERRIDE]**

For each sharing rule identified by SE: is the access granted intended for CS users?
Flag any rule granting CS access beyond job scope as Potential Overreach. For each:
name the access path and the most likely over-reached population.

**CS-3 — Cross-Role Differential**

State at least one entity and operation where CS has less access than a higher-privilege role.
Confirm this differential is intentional.

---

**Closing Summary [CLOSES: FLS-GAP, CUMULATIVE-PRIVILEGE, SHARING-OVERRIDE]**

| Operation | Role | FLS Verdict | Record Scope | Escalation Risk | Gap? |
|-----------|------|-------------|--------------|-----------------|------|

FLS Verdict: PASS / FAIL / PARTIAL / N/A
Escalation Risk: HIGH / MEDIUM / LOW / NONE
Gap?: YES / NO
One row per operation-role combination traced. All cells populated.

**Closes label compliance check**: List any section or table above missing a `[CLOSES: <label>]`
annotation from the registry. Any unlabeled section is NON-COMPLIANT.

---

## V-02 — Single Axis: C-11 — Null-Case Row Templates

**Axis**: C-11 null-case row placement — null-case row templates are declared alongside each
table schema as the first structural element. When no positive findings exist, the null-case
row IS the output. The prompt provides the exact row content for each table's null scenario.

**Hypothesis**: Prose null-case disclaimers occur when the model does not know what a null row
looks like. Providing the exact template — with column values pre-filled for the no-data
scenario — eliminates this ambiguity. Silent omission is structurally impossible when the model
has a row to copy. The null-case template converts the C-11 requirement from a behavioral
instruction to a copy-paste operation.

---

You are running a permissions trace signal for: {{topic}}

---

## NULL-CASE ROW MANDATE

Every table in this trace has a null-case row template declared below. The null-case row is
written as a DATA ROW — never as a prose disclaimer before the table. When no positive findings
exist for a table, the null-case row IS the table's output. When positive findings exist,
the null-case row is replaced by the actual findings. Never substitute prose commentary for
a data row.

---

### ROLE: SECURITY ENGINEER

Execute analysis in privilege-tier descent order: admin-tier first, then custom, then restricted.

**TABLE 1 — Role-Operation Matrix**

Null-case row template (use only if no security roles are configured for {{topic}}):
`[No roles in scope] | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A`

Columns: Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope
Tier: Admin / Custom / Restricted. Cells: Granted / Denied / Conditional (inline) / N/A.
No blank cells. Order: Admin first, Custom second, Restricted last.

**TABLE 2 — Field-Level Security Coverage** *(closes: Post-incident FLS gap)*

Null-case row template — write as the FIRST DATA ROW when no column security profiles are configured:
`[entity name] | [sensitive field] | [PII/Financial/Audit-Compliance] | Not Configured | All with entity Read | All with entity Write | YES`

This null-case row is written as a DATA ROW — not as a prose paragraph before the table.
Writing "No FLS configured on {{topic}}. See analysis above." instead of this row fails C-11.

Columns: Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?
FLS Profile Configured?: Configured / Not Configured — never blank.
Gap?: YES / NO — never blank. All Gap? = YES rows forwarded to TABLE 5.

One null-case row per sensitive field that lacks FLS. Rows for configured FLS follow after.

**Escalation Vector Table** *(closes: Cumulative privilege + OWD-sharing-rule override)*

Null-case row template (for each vector where no path was found):
`[vector name] | YES | Checked [vector]: no path confirmed; [specific mechanism and reason] | N/A`

Columns: Vector | Checked? | Finding | Severity
Vectors: Team inheritance / Sharing rules / Impersonation (Act on Behalf Of) / Admin-role override.
All four Checked? = YES.
Confirmed path: `[Role] -> [Mechanism] -> [Elevated access achieved]`
Cleared: `Checked [vector]: no path because [specific reason and mechanism]`

**TABLE 3 — Record Scope by Role** *(closes: Cumulative privilege accumulation)*

Null-case row template (for roles where scope could not be confirmed):
`[Role name] | [Tier] | [OWD setting] | None | Own | NO`

Verified? = NO means scope was not confirmed — flag for follow-up, do not omit the row.

Columns: Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?
Every TABLE 1 role must appear. Effective Scope: Own / BU / Parent-Child BU / Org-wide / Team-scoped.
For any role where team membership expands scope: flag the expansion explicitly.

**TABLE 5 — Security Gap Inventory**

Null-case row template (use ONLY if all gap types were checked and cleared):
`1 | CLEARED | {{topic}} | All vectors | All roles | All tiers | N/A | Gap types checked and cleared: MISSING-FLS — [evidence]; ESCALATION-PATH — [evidence]; SHARING-CONFLICT — [evidence]; TEAM-GAP — [evidence]; OVER-PERMISSIONED — [evidence].`

Columns: # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation
Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CLEARED
Severity: CRITICAL / HIGH / MEDIUM / N/A (CLEARED rows)
Remediation: exact object name + exact location + expected post-fix state.

---

### ROLE: CUSTOMER SERVICE

**CS-1 — Expected CS Access Baseline**

For each entity: expected CRUD operations for normal CS job function. Expected record scope.
Sensitive fields CS legitimately needs to read or write.

**CS-2 — Sharing Rule Expectations** *(closes: OWD-sharing-rule override)*

For each sharing rule from the escalation vector table: intended for CS users?
Flag overreach. For each Potential Overreach: name the access path and the over-reached population.

**CS-3 — Cross-Role Differential**

At least one entity and operation where CS has less access than a higher-privilege role.
Confirm the differential is intentional.

---

**Closing Summary**

Null-case row template (use only if no operations were traced):
`[No operations traced] | N/A | N/A | N/A | NONE | NO`

| Operation | Role | FLS Verdict | Record Scope | Escalation Risk | Gap? |
|-----------|------|-------------|--------------|-----------------|------|

FLS Verdict: PASS / FAIL / PARTIAL / N/A
Escalation Risk: HIGH / MEDIUM / LOW / NONE
Gap?: YES / NO
One row per operation-role combination traced. All cells populated — no blank cells.

---

## V-03 — Single Axis: C-12 — Escalation Risk Scale Declaration + Auto-Fail Condition

**Axis**: C-12 escalation risk column enforcement — the closing summary table schema is declared
with the Escalation Risk column included, a 4-level scale fully defined, and an explicit auto-fail
condition: if any row has a blank Escalation Risk cell, the table fails verification.

**Hypothesis**: The most common C-12 failure mode is: the Escalation Risk column appears in
the table header but rows are blank, or the scale is undefined so values are inconsistent.
Pre-declaring the scale with specific meanings for each level and an explicit auto-fail condition
for blank cells converts C-12 from a "nice to have" annotation to a hard verification gate. This
variation tests C-12 in isolation using the imperative backbone from R1 V-03 for all other sections.

---

You are running a permissions trace signal for: {{topic}}

Trace who can do what through RBAC, security roles, teams, and field-level security.
For each operation: which roles can perform it, which fields are visible, which records are accessible.
Identify privilege escalation paths, missing FLS, team membership gaps, and sharing rule conflicts.

---

## ESCALATION RISK SCALE

The Closing Summary requires an Escalation Risk column. Use exactly one of these values per row:

- **HIGH**: A confirmed escalation path exists — a lower-privilege role can reach higher-privilege
  resources through team membership, sharing rules, or impersonation as demonstrated in Step 4.
- **MEDIUM**: A conditional or unverified escalation risk — the path depends on a specific
  configuration that may or may not be present, or could not be confirmed definitively.
- **LOW**: An escalation path is theoretically possible given the role and entity architecture
  but no specific instance was found after checking all four vectors in Step 4.
- **NONE**: All four escalation vectors checked and cleared for this operation-role combination;
  no path exists by any mechanism examined.

**Auto-fail condition**: If any row in the Closing Summary has a blank Escalation Risk cell,
the Closing Summary fails verification. Confirm all rows are populated before submitting.

---

**Step 1 — Build the role-operation matrix.**

Produce a table: Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope
Tier: Admin / Custom / Restricted. Cells: Granted / Denied / Conditional (inline) / N/A.
No blank cells. Order: Admin tier first, then Custom, then Restricted.

**Step 2 — Audit field-level security.**

List every field in scope carrying PII, Financial, or Audit-Compliance sensitivity.
For each: is a column security profile configured? Which roles can read it? Write it?

You must explicitly state the null case if no FLS exists:
"No column security profiles configured on {{topic}}. These sensitive fields are exposed to
any role with entity access: [list each field by name]."

Produce a table: Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?
FLS Profile Configured?: Configured / Not Configured — never blank.
Gap?: YES / NO — never blank.

**Step 3 — Map record scope per role.**

For each role: OWD baseline, scope modifier from team membership, effective scope.
Produce: Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?
Effective Scope: Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].
Every Step 1 role must appear. Flag any role where team membership expands scope beyond the base.

**Step 4 — Check all four escalation vectors.**

For each vector, produce a verdict — confirmed or cleared:

1. Team inheritance — does any team membership grant elevated access to a lower-privilege role?
2. Sharing rules — does any sharing rule override the OWD baseline granting broader access?
3. Impersonation (Act on Behalf Of) — can any service account or application user act on
   behalf of a higher-privilege identity?
4. Admin/environment role override — does any admin-equivalent role bypass lower-tier controls?

Confirmed path: `[Role] -> [Mechanism] -> [Elevated access reached]`
Cleared: `Checked [vector]: no path because [specific mechanism and reason]`
All four vectors must produce a verdict. Step 4 results populate Escalation Risk values in Step 5.

**Step 5 — List all security gaps.**

For each gap: Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation
Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED
Severity: CRITICAL / HIGH / MEDIUM
Remediation: exact object name + exact location + expected post-fix state.
At least one gap required. If no gaps, produce CLEARED rows with per-gap-type evidence.

---

**Closing Summary** *(Escalation Risk column required; auto-fail if any row blank)*

| Operation | Role | FLS Verdict | Record Scope | Escalation Risk | Gap? |
|-----------|------|-------------|--------------|-----------------|------|

- FLS Verdict: PASS / FAIL / PARTIAL / N/A
- Record Scope: Own / BU / Parent-Child BU / Org-wide / Team-scoped
- Escalation Risk: HIGH / MEDIUM / LOW / NONE — see scale above. Blank = auto-fail.
- Gap?: YES / NO

One row per operation-role combination traced. All cells populated — no blank cells.

Verification gate: confirm every Escalation Risk cell is populated with one of HIGH / MEDIUM /
LOW / NONE before submitting. Any blank cell means the table is incomplete.

---

## V-04 — Combination: C-10 + C-11 (Blind-Spot Labels + Null-Case Row Templates)

**Axes combined**: C-10 blind-spot label structural mandate + C-11 null-case row templates,
layered onto the SE-first phase structure from R1 V-04.

**Hypothesis**: C-10 (labeling) and C-11 (null-case rows) address different table quality
dimensions and should not conflict when combined. Using the SE-first phase backbone without
the verbose inertia framing tests whether the two format rules are self-sustaining: can closes
labels produce C-10 without a motivating narrative? Can null-case templates produce C-11 on
a backbone that doesn't use blind-spot framing idiom? The R1 V-04 phase gates prevent phase
skip; C-10 + C-11 format rules prevent format degradation within each phase.

---

You are running a permissions trace signal for: {{topic}}

---

## STRUCTURAL RULES (apply globally to all tables and section headers)

**Rule 1 — Blind-Spot Label [C-10]**: Every table and major section header must carry a
`[CLOSES: <label>]` suffix using one or more labels from the registry below. Labels are
verbatim — character-for-character. A header without a closes annotation is structurally
incomplete.

**Rule 2 — Null-Case Row [C-11]**: Every table has a null-case row template declared with it.
The null-case row is a DATA ROW — written in the table, not as prose before the table. When
no positive findings exist, the null-case row IS the output. When findings exist, they replace
the null-case row.

**Blind Spot Registry** (for closes labels):
- `FLS-GAP` — Column security profiles invisible from security roles UI; gaps surface post-exposure.
- `CUMULATIVE-PRIVILEGE` — Role + team + OWD combination invisible in any single UI view;
  spot-checking individual roles misses accumulated access.
- `SHARING-OVERRIDE` — OWD-per-entity audit misses sharing rules that silently override it;
  Private OWD + active rule grants effective org-wide access without appearing in security UI.

---

### PHASE 1 — Security Engineer: Technical Analysis (privilege-tier descent)

*Complete all SE sections before writing PHASE 1 GATE. Do not begin PHASE 2 until GATE is written.*

**SE-0 — Admin-Tier Inventory and Escalation Vectors [CLOSES: CUMULATIVE-PRIVILEGE, SHARING-OVERRIDE]**

Admin-tier inventory: System Administrator, Environment Admin, admin-equivalent roles.
For each: record scope and whether the role bypasses column security profiles.

**Escalation Vector Table [CLOSES: CUMULATIVE-PRIVILEGE, SHARING-OVERRIDE]**
Null-case row: `[vector name] | YES | Checked [vector]: no path; [specific mechanism and reason] | N/A`

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

All four Checked? = YES. No blank Finding cells.
Confirmed path: `[Role] -> [Mechanism] -> [Elevated access]`
Cleared: `Checked [vector]: no path because [specific reason]`

**TABLE 1 — Role-Operation Matrix [CLOSES: baseline required before FLS-GAP, CUMULATIVE-PRIVILEGE, SHARING-OVERRIDE]**
Null-case row: `[No roles in scope] | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A`

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Tier: Admin / Custom / Restricted. Cells: Granted / Denied / Conditional (inline) / N/A.
No blank cells. Order: Admin first, Custom second, Restricted last.

**TABLE 2 — Field-Level Security Coverage [CLOSES: FLS-GAP]**
Null-case row (write as FIRST DATA ROW when no column security profiles configured):
`[entity name] | [sensitive field] | [PII/Financial/Audit-Compliance] | Not Configured | All with entity Read | All with entity Write | YES`

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

FLS Profile Configured?: Configured / Not Configured — never blank.
Gap?: YES / NO — never blank. All Gap? = YES rows forwarded to TABLE 5.

**TABLE 3 — Record Scope by Role [CLOSES: CUMULATIVE-PRIVILEGE]**
Null-case row (for roles where scope cannot be confirmed): `[Role] | [Tier] | [OWD] | None | Own | NO`

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|

Every TABLE 1 role must appear, ordered by Tier. Verified? = NO for unconfirmed scope.
Effective Scope: Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].

**TABLE 5 — Security Gap Inventory [CLOSES: FLS-GAP, CUMULATIVE-PRIVILEGE, SHARING-OVERRIDE]**
Null-case row (only when all gap types cleared):
`1 | CLEARED | {{topic}} | All checked | All roles | All tiers | N/A | Gap types checked and cleared: MISSING-FLS — [evidence]; ESCALATION-PATH — [evidence]; SHARING-CONFLICT — [evidence]; TEAM-GAP — [evidence]; OVER-PERMISSIONED — [evidence].`

| # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation |
|---|----------|--------|---------------|------|------|----------|-------------|

Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CLEARED
Severity: CRITICAL / HIGH / MEDIUM / N/A
Remediation: exact object + exact location + expected post-fix state.

---

**PHASE 1 GATE — SE confirms**:
- TABLE 1: all cells filled, Tier column populated, rows ordered by tier? YES / NO
- TABLE 2: null case handled as a data row (not prose)? YES / NO
- TABLE 3: every TABLE 1 role present, Effective Scope filled? YES / NO
- Escalation vectors: all four Checked? = YES, all Finding cells populated? YES / NO
- TABLE 5: at least one row present? YES / NO

If any NO: complete the missing section before crossing PHASE 1 GATE.

*[SE: PHASE 1 complete. Handing to PHASE 2 — CS.]*

---

### PHASE 2 — Customer Service: Lower-Trust Review

**CS-1 — Expected CS Access Baseline**

For each entity: expected CRUD operations for normal CS job function, expected record scope,
sensitive fields CS legitimately needs to read or write.

**CS-2 — Sharing Rule Overreach Check [CLOSES: SHARING-OVERRIDE]**
Null-case row: `[No sharing rules found] | N/A | N/A | No sharing rules configured | NO`

For each sharing rule from SE-0: intended for CS users? Flag any overreach with the access
path and the most likely over-reached population.

**CS-3 — Cross-Role Differential**

At least one entity and operation where CS has less access than a higher-privilege role.
Confirm the differential is intentional. Flag any contradiction with TABLE 1 as
CS-EXPECTATION-VIOLATED and add to TABLE 5.

---

**Closing Summary [CLOSES: FLS-GAP, CUMULATIVE-PRIVILEGE, SHARING-OVERRIDE]**
Null-case row: `[No operations traced] | N/A | N/A | N/A | NONE | NO`

| Operation | Role | FLS Verdict | Record Scope | Escalation Risk | Gap? |
|-----------|------|-------------|--------------|-----------------|------|

FLS Verdict: PASS / FAIL / PARTIAL / N/A
Escalation Risk: HIGH / MEDIUM / LOW / NONE
Gap?: YES / NO. All cells populated. One row per operation-role combination traced.

**Structural compliance check**:
- C-10: List any section/table header missing a `[CLOSES: <label>]` annotation — NON-COMPLIANT.
- C-11: List any table where the null case was handled as prose instead of a data row — NON-COMPLIANT.

---

## V-05 — Full Integration: R1-V-05 Base + C-10/C-11/C-12 All Hardened

**Axes combined**: Table-first structure + inertia framing (from R1 V-05) + explicit hardening
for all three new aspirational criteria (C-10, C-11, C-12).

**Hypothesis**: R1 V-05 produced C-10, C-11, and C-12 signals implicitly — earning 95 pts and
generating the rubric criteria that defined those signals. V-05(R2) converts each implicit
signal to a structural requirement: closes labels as required schema metadata on every table
header, null-case row templates per table, and the escalation risk scale with auto-fail. The
inertia framing and table-first format are preserved because they drove the essential/recommended
score; the three mechanisms are layered on top. This is the "lock in the excellence" variation —
making all five aspirational criteria as structurally unreachable by omission as the essential ones.

---

You are running a permissions trace signal for: {{topic}}

---

## WHY THIS TRACE EXISTS: THREE MANUAL AUDIT BLIND SPOTS

Manual security reviews of Dataverse environments routinely miss three failure scenarios.
This trace surfaces all three. Every table below names the exact blind spot it closes —
converting gap-hunting from a generic obligation into motivated closure against a named failure mode.

**[FLS-GAP] — Blind spot 1: Post-incident FLS gap**: Column security profiles are not auditable
from the security roles UI. Sensitive fields (credit limits, compensation data, SSNs, contact
identifiers) remain readable and writable by any role unless a column security profile explicitly
restricts them. Gaps are discovered after data exposure, not before.

**[CUMULATIVE-PRIVILEGE] — Blind spot 2: Cumulative privilege accumulation**: A user holding a
BU-scoped role who also belongs to an owner team with org-wide access has effective org-wide
access. No single Dataverse UI view surfaces the combined access from role + team + OWD.
Spot-checking individual roles misses cross-role accumulation through team membership.

**[SHARING-OVERRIDE] — Blind spot 3: OWD-sharing-rule override**: Administrators audit OWD
settings entity-by-entity without cross-referencing the sharing rules that silently override those
baselines. A Private OWD combined with a Power Automate-triggered sharing rule can grant effective
org-wide read to users satisfying the trigger condition — including low-trust service accounts.

**Three structural rules apply globally:**

1. **C-10 — Closes label**: Every table header includes `[CLOSES: <label>]` using one or more
   blind-spot labels above verbatim. A header missing a closes label is structurally incomplete.
2. **C-11 — Null-case row**: Every table has a null-case row template. The null case is a DATA
   ROW in the table — never a prose disclaimer before the table. When no positive findings exist,
   the null-case row IS the output.
3. **C-12 — Escalation Risk scale**: The Closing Summary includes an Escalation Risk column
   with the 4-level scale declared below. Every row must be populated. Any blank Escalation Risk
   cell = Closing Summary fails verification.

---

### ROLE: SECURITY ENGINEER

Execute in privilege-tier descent order: admin first, then custom, then restricted.

---

**TABLE 1 — Role-Operation Matrix [CLOSES: baseline required before FLS-GAP, CUMULATIVE-PRIVILEGE, SHARING-OVERRIDE]**
Null-case row: `[No roles in scope] | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A`

Columns: Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope
Tier: Admin / Custom / Restricted. Cells: Granted / Denied / Conditional (inline) / N/A.
No blank cells. Order: Admin first, Custom second, Restricted last.

After the table: one sentence per tier noting any capability that bypasses lower-tier controls.

---

**TABLE 2 — Field-Level Security Coverage [CLOSES: FLS-GAP]**
Null-case row template — write as the FIRST DATA ROW when no column security profiles configured:
`[entity name] | [sensitive field] | [PII/Financial/Audit-Compliance] | Not Configured | All with entity Read | All with entity Write | YES`

Writing "No FLS configured. See note above." instead of this row fails C-11.

Columns: Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?
Categories: PII / Financial / Audit-Compliance / Other-Sensitive.
FLS Profile Configured?: Configured / Not Configured — never blank.
Gap?: YES / NO — never blank. All Gap? = YES rows forwarded to TABLE 5.

---

**TABLE 3 — Record Scope by Role [CLOSES: CUMULATIVE-PRIVILEGE]**
Null-case row: `[Role name] | [Tier] | [OWD setting] | None | Own | NO`
(Verified? = NO for roles where effective scope could not be confirmed — flag, do not omit.)

Columns: Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?
Effective Scope: Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].
Every TABLE 1 role must appear, ordered by Tier.
For every role where Effective Scope > role-only scope, write one sentence:
"[Role] acquires [scope] through [team/rule name]. Base role scope was [base scope]."

---

**TABLE 4 — Escalation Vector Inventory [CLOSES: CUMULATIVE-PRIVILEGE, SHARING-OVERRIDE]**
Null-case row: `[vector name] | YES | Checked [vector]: no path; [specific mechanism and reason] | N/A`

Columns: Vector | Checked? | Finding | Severity
Vectors: Team inheritance / Sharing rules / Impersonation (Act on Behalf Of) / Admin-role override.
All four Checked? = YES.
Confirmed path: `[Role] -> [Mechanism] -> [Elevated access achieved]`
Cleared: `Checked [vector]: no path because [specific reason and mechanism]`
Severity for cleared: N/A.

After the table: for each confirmed escalation path, cite the specific blind-spot label
([FLS-GAP], [CUMULATIVE-PRIVILEGE], or [SHARING-OVERRIDE]) that it instantiates.

---

**TABLE 5 — Security Gap Inventory [CLOSES: FLS-GAP, CUMULATIVE-PRIVILEGE, SHARING-OVERRIDE]**
Null-case row (ONLY if all five gap types were checked and cleared):
`1 | CLEARED | {{topic}} | All checked | All roles | All tiers | N/A | Gap types checked and cleared: MISSING-FLS — [evidence]; ESCALATION-PATH — [evidence]; SHARING-CONFLICT — [evidence]; TEAM-GAP — [evidence]; OVER-PERMISSIONED — [evidence].`

Columns: # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation
Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CLEARED
Severity: CRITICAL / HIGH / MEDIUM / N/A
Remediation: exact object name + exact location + expected post-fix state.
Insufficient: "Restrict access to revenue data."
Sufficient: "Create column security profile 'RevenueSensitive'; restrict Write on estimatedrevenue
to Sales Manager role only; confirm No Access for CS User role in the profile."

---

### ROLE: CUSTOMER SERVICE

**CS-1 — Expected CS Access Baseline**

For each entity in scope: expected CRUD operations for normal CS job function, expected record
scope, sensitive fields CS legitimately needs, and any configuration that may open access beyond
job requirements.

**CS-2 — Sharing Rule Overreach [CLOSES: SHARING-OVERRIDE]**

For each sharing rule from TABLE 4: intended for CS users? Flag any rule granting CS users
access beyond job scope. For each: name the access path and the over-reached population.

**CS-3 — Cross-Role Differential**

At least one entity and operation where CS has less access than a higher-privilege role.
Confirm this differential is intentional. Flag any contradiction with TABLE 1 as
CS-EXPECTATION-VIOLATED and add to TABLE 5.

---

## ESCALATION RISK SCALE (required before populating Closing Summary)

- **HIGH**: Confirmed escalation path — lower-privilege role reaches higher-privilege resource as
  confirmed in TABLE 4.
- **MEDIUM**: Conditional risk — path exists if a specific configuration is present, not yet confirmed.
- **LOW**: Theoretically possible given architecture; no specific instance found after checking all
  four TABLE 4 vectors.
- **NONE**: All four TABLE 4 escalation vectors checked and cleared for this operation-role combination.

---

**Closing Summary [CLOSES: FLS-GAP, CUMULATIVE-PRIVILEGE, SHARING-OVERRIDE]**
Null-case row: `[No operations traced] | N/A | N/A | N/A | NONE | NO`
Auto-fail condition: Any blank Escalation Risk cell = Closing Summary fails verification.

| Operation | Role | FLS Verdict | Record Scope | Escalation Risk | Gap? |
|-----------|------|-------------|--------------|-----------------|------|

- FLS Verdict: PASS / FAIL / PARTIAL / N/A
- Record Scope: Own / BU / Parent-Child BU / Org-wide / Team-scoped
- Escalation Risk: HIGH / MEDIUM / LOW / NONE — blank = auto-fail
- Gap?: YES / NO

One row per operation-role combination traced. No blank cells.

**Final verification (C-10 / C-11 / C-12):**
1. C-10: Every table header carries a `[CLOSES: <label>]` from the registry verbatim. List any unlabeled header as NON-COMPLIANT.
2. C-11: Every table's null case was handled as a data row, not a prose disclaimer. List any prose substitution as NON-COMPLIANT.
3. C-12: Every Escalation Risk cell populated with HIGH / MEDIUM / LOW / NONE. List any blank cell as NON-COMPLIANT.

---

*Trace complete. Blind spots addressed: TABLE 2 closes FLS-GAP; TABLE 3 + TABLE 4 close
CUMULATIVE-PRIVILEGE; TABLE 4 closes SHARING-OVERRIDE. Closing Summary carries Escalation Risk
column per declared scale. All null cases handled as data rows. All headers carry closes labels.*
