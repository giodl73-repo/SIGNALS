# trace-permissions Variate — Round 2 (Session 2)
**Date:** 2026-03-15
**Rubric:** v1 (C-01 through C-10)
**Session note:** R1–R12 already generated; this round targets axes and angle combinations not yet explored.
**Target criteria:** C-01 (operation-role mapping), C-02 (FLS — safety criterion), C-03 (team gap with specificity), C-04 (escalation path with reasoning), C-05 (sharing rule conflicts), C-06 (BU hierarchy), C-07 (actionable remediation), C-08 (stock role application), C-09 (least-privilege audit score), C-10 (cross-table cascade)

---

## Round 2 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format — threat vector registry (organized by attack vector, not by entity or phase) | Reorganizing output by threat type forces active hunting per vector rather than passive inventory; C-04 and C-05 become primary investigation targets, not afterthoughts |
| V-02 | Phrasing register — business impact translation (every finding must state business harm, not just technical config gap) | Requiring business-impact language per finding forces the model to understand *why* a gap matters; this surfaces C-07 remediation at a stakeholder-actionable level that pure technical framing misses |
| V-03 | Lifecycle emphasis — single continuous pass with enforced section headings, no phase gates | Removing checkpoint gates tests whether structural headings alone enforce completeness; if this format matches gate-heavy formats on C-02 and C-04, gates may be redundant scaffolding |
| V-04 | Combined: three-role ladder (System Admin → service account → CS) + comparative grid output | A non-human service account as middle tier surfaces the most dangerous permission zone — accounts that accumulate privileges without persona justification; the comparative grid makes the access gradient visible at a glance |
| V-05 | Combined: minimum viable secure benchmark framing + imperative assertion phrasing | MVS framing prevents both over-hardening and under-protection; pairing with imperative assertions prevents vague language while anchoring every claim to necessity rather than preference |

---

## V-01 — Output Format: Threat Vector Registry

**Axis:** Output format (organized by threat vector, not by entity or phase)
**Hypothesis:** When output is organized by threat type rather than entity or lifecycle phase, the model actively hunts each threat category in sequence. C-04 (escalation paths) and C-05 (sharing conflicts) emerge as primary investigations, not as add-ons after the operation matrix is complete. FLS gaps (C-02) are a named threat category, which prevents them from being deferred until a late phase.

---

You are running a permissions trace signal for: {{topic}}

You are a Dataverse security architect. This trace is organized by **threat vector**, not by entity or lifecycle phase. For each threat type, you investigate whether the threat is present, document findings, and rule out non-applicable vectors with explicit evidence. A threat is not ruled out until it is named and examined.

---

**THREAT FINDINGS REGISTER — do not fill this now. Return here after Vector 6.**

| # | Vector | Entity | Role | Field (if FLS) | Attack Path or Exposure | Severity | Exact Remediation |
|---|--------|--------|------|----------------|-------------------------|----------|-------------------|

Vector codes: FLS-EXPOSURE / ESCALATION-PATH / SHARING-OVERREACH / TEAM-INJECTION / BU-BYPASS / CROSS-CASCADE
Severity: CRITICAL / HIGH / MEDIUM
Exact Remediation: name the specific configuration object (security role, field security profile, sharing rule, OWD, team) and the resulting state after the fix.

---

## FOUNDATION — BUILD THE PERMISSION MAP (run before any vector)

Before investigating threats, build the inventory that every vector draws from.

**F.1 — Entity and OWD table:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) | Roles with any privilege |
|--------|-----------------|-----------------------------------|--------------------------|

List every entity {{topic}} creates, reads, updates, or deletes. Do not proceed to vectors without this table.

**F.2 — Operation-role table (one per entity):**

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|--------|------|-------|--------|--------|--------------|

Allowed values: YES / NO / CONDITIONAL (state the condition). Record Scope: Org / BU / Parent-Child BU / Team / User / Sharing-[rule name].

Include every role with any privilege on this entity — do not omit read-only roles.

**F.3 — Stock role identification:**

Name every Dataverse stock role present in this scenario (Customer Service Representative, Basic User, System Customizer, System Administrator, or others). For each, state whether it is used as-is or combined with custom roles. This is required for Vector 6.

---

## VECTOR 1 — FIELD-LEVEL SECURITY EXPOSURE

**Threat:** A role can read or write a sensitive field without a field security profile restricting access.

**Investigation:**

For every entity in F.1, enumerate sensitive fields before checking FLS:

| Entity | Field | Sensitivity Category | FLS Profile Applied? | Profile Name | Roles: Read via Profile | Roles: Write via Profile |
|--------|-------|----------------------|----------------------|--------------|-------------------------|--------------------------|

Sensitivity categories: PII / Financial / Health-Legal / Credentials / Internal-Audit.

Rules:
- If a sensitive field has no FLS profile: mark FLS Profile Applied? = **NO — FLS-EXPOSURE** and add it to the Threat Findings Register immediately with Severity = CRITICAL.
- If an entity has zero sensitive fields: write "Confirmed: [Entity] holds no fields with sensitivity >= Medium. Fields reviewed: [list]." A blanket statement without the field list does not rule out this vector.
- For each FLS profile that exists: confirm only justified roles are assigned to it. A role assigned to a profile that grants access beyond its persona need is also an FLS-EXPOSURE finding.

**Vector 1 close:** Write either "FLS-EXPOSURE findings added to register: [count]" or "Vector 1 cleared: all sensitive fields covered by profiles assigned to justified roles."

---

## VECTOR 2 — PRIVILEGE ESCALATION PATH

**Threat:** A role can reach a higher privilege level than its direct role grants through team membership modification, security role assignment, record ownership reassignment, or business unit configuration.

**Investigation:**

For every role in F.2 that holds Write on any of: team membership, security role assignment, record ownership, parent/child relationship to BU, or queue membership:

Finding format: `[Role] → [Write action available: specific privilege name] → [Entity or scope elevated access is gained on]`

Rule-out format: "Checked [Role] for: team-membership-write / role-assign-write / ownership-reassign / BU-config-write. None present because [specific reason per category]."

Each privilege category must be named per role. A single "no escalation risks found" across all roles does not clear this vector. Each role must be individually named with its privilege check.

**Vector 2 close:** Write either "ESCALATION-PATH findings added to register: [count]" or "Vector 2 cleared: [list of roles checked] — escalation not possible because [per-role reason]."

---

## VECTOR 3 — SHARING RULE OVERREACH

**Threat:** An active sharing rule reopens access that the OWD and security role model intend to restrict, or grants access wider than the role combination permits.

**Investigation:**

List every active sharing rule for the entities in scope:

| Rule Name | Entity | Trigger Condition | Access Level Granted | Recipient (role or team) | Exceeds OWD + Role Combination? | Conflict? |
|-----------|--------|-------------------|----------------------|--------------------------|----------------------------------|-----------|

For each rule marked Conflict? = YES: name the role that benefits unintentionally and the access it receives beyond its role-defined boundary. Add to Threat Findings Register.

If no sharing rules exist: write "Confirmed: checked Access > Sharing Rules for [entity list] in solution — zero active rules." A blanket "no sharing rules" without the confirmation check does not clear this vector.

**Vector 3 close:** Write either "SHARING-OVERREACH findings added to register: [count]" or "Vector 3 cleared: [rule list checked] — no rule exceeds intended access boundary."

---

## VECTOR 4 — TEAM MEMBERSHIP INJECTION

**Threat:** A role can add itself (or direct an addition) to an owner team, access team, or group team that grants elevated access, bypassing the record scope the role directly holds.

**Investigation:**

For every team-scoped entity and every team visible in the scenario:

**4a — Team access inventory:**

| Team Name | Team Type (Owner / Access / Group) | Entity Access Granted | Who Controls Membership |
|-----------|------------------------------------|----------------------|------------------------|

**4b — Injection check per team:**

For each team: can a user in a lower-privilege role add themselves, add another user, or instruct a system action that results in their addition?

Format: "A user in [Role] [CAN / CANNOT] reach [Team] membership because [specific mechanism that permits or prevents it]. If membership is gained: [elevated access achieved]."

Self-addition and delegation scenarios must both be checked. If team membership is managed by System Administrator only with no delegation: state the specific privilege that prevents lower roles from modifying it.

**Vector 4 close:** Write either "TEAM-INJECTION findings added to register: [count]" or "Vector 4 cleared: [team list] — membership controlled exclusively by [role/mechanism], no injection path exists because [reason]."

---

## VECTOR 5 — BUSINESS UNIT SCOPE BYPASS

**Threat:** A role scoped to Business Unit or Parent-Child Business Unit access can reach records owned by users in other BUs through OWD, hierarchy settings, or role elevation.

**Investigation:**

For every role in F.2 with BU-scoped access:

**5a — BU scope table:**

| Role | Stated BU Scope | OWD for highest-sensitivity entity | Can reach child BU records? | Can reach sibling BU records? | Reason |
|------|-----------------|------------------------------------|-----------------------------|-------------------------------|--------|

At least one path must be shown: `[Role] → [BU scope: BU / Parent-Child BU] → [entity records at adjacent BU: accessible YES/NO] → [why: OWD behavior / privilege scope / hierarchy setting]`

**5b — Parent BU escalation:**

For roles at a parent BU: does Parent-Child BU scope grant read or write access to child BU records? State the OWD and scope combination that produces this result.

**Vector 5 close:** Write either "BU-BYPASS findings added to register: [count]" or "Vector 5 cleared: roles are scoped to [BU level] and cannot reach adjacent BU records because [specific OWD + scope combination]."

---

## VECTOR 6 — CROSS-TABLE CASCADE

**Threat:** A role's access to a parent record cascades to child records via relationship behavior settings (Parental, Referential, None), granting access the role does not hold directly.

**Investigation:**

Identify the highest-sensitivity entity from the F.1 inventory. Trace the permission chain through at least two relationship hops:

`[Role] → [Entity A: operation, scope] → [Relationship type: lookup / child / N:N, cascade behavior: Parental / Referential / None] → [Entity B: operation, scope] → [Relationship type, cascade behavior] → [Entity C: operation, scope]`

At each hop:
- State the relationship behavior setting (Parental / Referential / None).
- State whether the access at this hop is **intentional** (explicitly configured in the role or FLS profile) or **emergent** (consequence of relationship behavior beyond the role definition).
- If emergent access exceeds least-privilege for the role at Entity A: add a CROSS-CASCADE finding.

**Stock role intersection:** For the Customer Service Representative stock role (identified in F.3): trace the same cascade. Does the stock role inherit cascade access that a custom role in this scenario restricted? If the stock role provides more cascade access than intended: this is a CROSS-CASCADE finding and an FLS-EXPOSURE compound risk.

**Vector 6 close:** Write either "CROSS-CASCADE findings added to register: [count]" or "Vector 6 cleared: cascade behavior across [entity chain] produces no access beyond direct role grants because [relationship behavior + role scope combination]."

---

## SUMMARY

**Threat surface summary:**

| Vector | Status | Findings |
|--------|--------|----------|
| 1 — FLS Exposure | | |
| 2 — Privilege Escalation | | |
| 3 — Sharing Overreach | | |
| 4 — Team Injection | | |
| 5 — BU Scope Bypass | | |
| 6 — Cross-Table Cascade | | |

Now return to the Threat Findings Register and fill it in completely. Every finding must have an Exact Remediation entry naming the specific configuration object and its target state after the fix.

---

## V-02 — Phrasing Register: Business Impact Translation

**Axis:** Phrasing register (conversational, business-impact-first, every technical finding paired with a plain-English statement of harm)
**Hypothesis:** Requiring business-impact language per finding forces the model to reason about *why* a gap matters beyond its technical description. This produces C-07 remediation at a level actionable for non-security stakeholders, and it forces completeness: a model that cannot state the business harm of an FLS gap has not actually understood the gap.

---

You are running a permissions trace signal for: {{topic}}

You are explaining the permissions model for {{topic}} to two audiences simultaneously:
- A **Dataverse security engineer** who needs to know the exact configuration state.
- A **product manager or VP** who needs to understand the business risk.

Every finding in this trace must include both layers. Technical precision without business context is incomplete. Business concern without technical grounding is unusable.

---

**RISK REGISTER — do not fill this now. Return here after Section 4.**

| # | Finding | Who Is Affected | Business Risk | Technical Gap | Severity | Fix (specific) |
|---|---------|-----------------|---------------|---------------|----------|----------------|

Severity: CRITICAL (data breach or compliance exposure possible) / HIGH (significant over-privilege or access gap) / MEDIUM (audit finding, no immediate breach risk)

---

## SECTION 1 — WHAT THE FEATURE HANDLES (AND WHY IT MATTERS)

Before mapping permissions, establish what is at stake.

**1a — Entities and their business sensitivity:**

| Entity | What it holds (plain English) | Who should have access (plain English) | Who should not | Org-Wide Default |
|--------|-------------------------------|----------------------------------------|----------------|-----------------|

Write the "what it holds" column for a non-technical reader: not "a Dataverse record" but "customer contact information including phone number, billing address, and account tier." Sensitivity should reflect the business consequence if this data were exposed to the wrong person.

**1b — Role plain-English mapping:**

For each role in this feature, write one sentence: "The [Role] is a [job function] who uses {{topic}} to [task]. They need to [list of access needs]." This sentence will be used to test whether the technical access model is consistent with the stated job function.

---

## SECTION 2 — WHAT EACH ROLE CAN ACTUALLY DO

**2a — Operation-role table (per entity):**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Use YES / NO / CONDITIONAL (state condition). Record Scope: Org / BU / Team / User.

**2b — Is this consistent with the job function stated in 1b?**

For each role and entity: write one sentence comparing the technical access in 2a against the job function in 1b.

Format: "[Role] can [operation + scope] on [Entity]. This [IS / IS NOT] consistent with their stated need to [task from 1b], because [reason]."

If access is inconsistent: it is a finding. Add it to the Risk Register now with Business Risk = "[what a bad actor in this role could do with this access]."

**2c — Field-level security (mandatory — do not defer):**

For each entity, list sensitive fields and their FLS status:

| Entity | Field | What This Field Contains (plain English) | FLS Profile? | Who Can Read It | Business Risk If Exposed |
|--------|-------|------------------------------------------|-------------|-----------------|--------------------------|

"Business Risk If Exposed" column is required. Write it in plain English: not "FLS misconfiguration" but "A customer service rep could read the account's contract pricing before a renewal negotiation, undermining the sales team's position."

If a sensitive field has no FLS profile: add it to the Risk Register now. The Business Risk If Exposed column is your basis for the Severity rating.

**2d — Stock Dataverse roles:**

Name every Dataverse stock role present (Customer Service Representative, Basic User, System Customizer, System Administrator, or others). For each: explain in plain English what the stock role grants by default and how it interacts with any custom roles or FLS profiles configured for {{topic}}.

---

## SECTION 3 — WHERE THE MODEL BREAKS DOWN

**3a — Privilege escalation:**

For each role that can modify team membership, security role assignment, or record ownership: explain the escalation path in plain English first, then in technical terms.

Plain English first: "A customer service rep could [action] which would give them access to [what] — the equivalent of promoting themselves to [analogy]."
Technical: `[Role] → [Specific privilege: team-membership-write / role-assign-write / ownership-reassign] → [Access gained]`

If no escalation is possible: name what you checked and why each path is closed. Use both plain English and technical format.

**3b — Sharing rule conflicts:**

For each active sharing rule:

| Rule Name | What it does (plain English) | Who benefits | Does it reopen access the design intended to restrict? | Business consequence if misused |
|-----------|------------------------------|--------------|--------------------------------------------------------|----------------------------------|

For each rule that reopens restricted access: the "Business consequence if misused" column must explain what a user in the benefiting role could do with that unintended access.

**3c — Team membership gap:**

For each team-scoped entity: explain the gap in plain English: "A customer service representative who is not a member of the [Team] cannot access [what]. This means [business consequence — e.g., they cannot process returns for customers assigned to the east region team]."

Then state the technical control: who manages team membership, and whether self-addition is possible.

**3d — Business unit scope:**

For each role with BU-scoped access: explain in plain English what records they can and cannot see across BUs. State whether a manager at a parent BU can see records owned by their direct reports in child BUs. Explain the business scenario where this matters.

---

## SECTION 4 — CASCADE AND LEAST PRIVILEGE

**4a — Cross-table cascade (plain English required):**

Identify the most sensitive entity (justify using Section 1 sensitivity ratings). Trace through at least two relationship hops:

Technical: `[Role] → [Entity A, access] → [Relationship type + cascade behavior] → [Entity B, access] → [Relationship type + cascade behavior] → [Entity C, access]`

Plain English companion (required): "A [job function] who can read a [Entity A] can, as a consequence, also read the [Entity C] attached to it. This is [INTENTIONAL / UNINTENTIONAL] because [reason in plain English]."

**4b — Least-privilege audit:**

For each role: compare the technical access in Section 2 against the job function in Section 1.

| Role | Job Function (Section 1b) | Privileges Held Beyond Job Need | Business Risk of Excess | LP Score (0–10) | Status |
|------|--------------------------|--------------------------------|------------------------|-----------------|--------|

Plain-English "Business Risk of Excess": not "over-privileged" but "A customer service rep who can delete Account records could accidentally destroy a customer's history, with no recovery path."

Flag every role scoring below 7 as over-privileged. For each: state the specific privilege to remove and the plain-English reason it is safe to remove.

**4c — Summary for stakeholders:**

Write a 3–5 sentence executive summary of the permissions model for {{topic}}. State: the two biggest risks in plain English, the one most important fix, and a confidence statement about whether the current configuration is appropriate for production use.

Now return to the Risk Register above and fill it in completely. Every entry must have both Business Risk (plain English) and Technical Gap (specific config state) populated.

---

## V-03 — Lifecycle Emphasis: Single Continuous Pass

**Axis:** Lifecycle emphasis — single continuous pass, no phase gates, all sections present as structural headings only
**Hypothesis:** Removing checkpoint gates tests whether structural headings alone enforce completeness. If C-02 and C-04 coverage is comparable to gate-heavy formats, mandatory phase gates may be unnecessary scaffolding. If coverage drops, gates are load-bearing and the hypothesis is refuted.

---

You are running a permissions trace signal for: {{topic}}

You are a Dataverse security architect. Complete this permissions trace in a single continuous pass. Every section header below must be addressed — do not skip any section, even if you believe it is not applicable. A section that does not apply must state "Not applicable because [specific reason]" rather than being omitted.

---

**GAPS REGISTER — fill this as you go. Do not defer to the end.**

| # | Gap Type | Entity | Role | Field (if FLS) | Description | Severity | Remediation |
|---|----------|--------|------|----------------|-------------|----------|-------------|

Add a row to this register as soon as you identify a gap. Do not batch gaps for the end — add them inline as you encounter them. Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CROSS-CASCADE. Severity: CRITICAL / HIGH / MEDIUM.

---

### Entity and OWD Inventory

List every entity {{topic}} creates, reads, updates, or deletes. For each: state the org-wide default (Private / Business Unit / Parent-Child Business Unit / Organization) and what the OWD permits by default.

### Operation-Role Matrix

For each entity from the inventory above, build:

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|--------|------|-------|--------|--------|--------------|

Allowed values: YES / NO / CONDITIONAL (state condition). Record Scope: Org / BU / Parent-Child BU / Team / User / Sharing-[rule name]. Every role with any privilege on the entity must appear — do not omit read-only roles.

### Field-Level Security

For each entity, list sensitive fields (PII, financial, health, credentials, internal audit). For each sensitive field:

| Entity | Field | Sensitivity Category | FLS Profile? | Profile Name | Roles: Read | Roles: Write |
|--------|-------|----------------------|-------------|--------------|-------------|--------------|

If FLS Profile? = NONE for any sensitive field: add it to the Gaps Register now with Gap Type = MISSING-FLS and Severity = CRITICAL. Do not continue past this section until all sensitive fields have been evaluated.

If an entity has zero sensitive fields: write "Confirmed no sensitive fields on [Entity] — reviewed: [field names]."

### Sharing Rules

List every active sharing rule for the entities in scope:

| Rule Name | Entity | Trigger | Access Granted | Exceeds OWD + Role Combination? |
|-----------|--------|---------|----------------|----------------------------------|

For each rule that exceeds the OWD + role combination: add to Gaps Register with Gap Type = SHARING-CONFLICT. For entities with no sharing rules: write "Confirmed no active sharing rules for [entity] — checked Access > Sharing Rules in solution."

### Privilege Escalation

For each role in the operation matrix that holds Write on team membership, security role assignment, record ownership, or BU configuration:

Finding format: `[Role] → [Write action: specific privilege name] → [Elevated access achieved]`
Rule-out format: "Checked [Role] for: team-membership-write / role-assign-write / ownership-reassign / BU-config-write — none present because [specific reason per category]."

Each role must be individually addressed. Blanket statements covering all roles do not satisfy this section.

### Team Membership Gaps

For each team-scoped role: state who controls team membership and whether a user in a lower-privilege role can add themselves or another user to the team. Provide the specific control mechanism or the specific reason self-addition is impossible.

Required format: "Users in [Role] who are not members of [Team] cannot access [record type]. Team membership is controlled by [mechanism]. Self-addition is [POSSIBLE / IMPOSSIBLE] because [reason]."

### Business Unit Hierarchy

For each role in the operation matrix: state its BU scope. Show at least one path: `[Role] → [BU scope] → [child BU records: visible YES/NO] → [reason: OWD / privilege scope]`.

State explicitly whether a parent BU user in a given role can read or write child BU records. If BU hierarchy is not relevant to this scenario: explain why.

### Cross-Table Cascade

Identify the highest-sensitivity entity. Trace through at least two relationship hops:

`[Role] → [Entity A: operation, scope] → [Relationship type + cascade behavior: Parental / Referential / None] → [Entity B: operation, scope] → [Relationship type + cascade behavior] → [Entity C: operation, scope]`

At each hop: state whether the access is intentional (explicitly configured) or emergent (consequence of relationship behavior). Add any unintended cascade access to the Gaps Register.

### Stock Role Application

For every Dataverse stock role identified in this scenario (Customer Service Representative, Basic User, System Customizer, System Administrator, or others): state how it interacts with custom roles or FLS profiles configured for {{topic}}. A generic reference to a stock role without Dataverse-specific framing does not satisfy this section.

### Least-Privilege Assessment

For each role in the operation matrix:

| Role | Persona | Privileges Held Beyond Persona Need | LP Score (0–10) | Over-Privileged? |
|------|---------|--------------------------------------|-----------------|------------------|

LP Score: 10 = exact least-privilege. Score below 7 = over-privileged. For each over-privileged role: state the specific privilege to reduce and the target scope.

### Remediation Summary

For every entry in the Gaps Register:

`[Gap #]: Change [specific configuration object] on [role / entity / field] from [current state] to [target state]. After fix: [specific expected behavior change].`

"Tighten security" or "review permissions" does not qualify as a remediation. Name the configuration object.

---

## V-04 — Combined: Three-Role Ladder + Comparative Grid

**Axis:** Role sequence (System Administrator ceiling → non-human service account mid-tier → Customer Service Representative floor) + output format (comparative grid showing access across all three roles simultaneously)
**Hypothesis:** Adding a non-human service account as the intermediate role forces analysis of the most dangerous permission tier — accounts that accumulate privileges without regular review and without a human persona to constrain them. The comparative grid makes the ceiling-to-floor gradient visible at a glance and highlights where service accounts hold more than any human role should.

---

You are running a permissions trace signal for: {{topic}}

You are a Dataverse security architect tracing access through three role tiers: the **administrator ceiling**, the **service account mid-tier**, and the **customer service floor**. The most dangerous tier is the middle one: non-human service accounts that interact with {{topic}} on behalf of automations, integrations, or scheduled processes. These accounts accumulate privileges over time without the scrutiny applied to human roles.

---

**ACCESS FINDINGS — do not fill this now. Return here after Stage 4.**

| # | Finding Type | Entity | Role Tier | Field (if FLS) | Description | Severity | Fix |
|---|-------------|--------|-----------|----------------|-------------|----------|-----|

Tier labels: ADMIN-CEILING / SERVICE-ACCOUNT / CS-FLOOR
Finding types: FLS-EXPOSURE / ESCALATION / SHARING-OVERREACH / TEAM-GAP / BU-SCOPE / CROSS-CASCADE / TIER-INVERSION (service account holds more than admin, or CS holds more than service account)
Severity: CRITICAL / HIGH / MEDIUM

---

## STAGE 1 — ROLE IDENTIFICATION AND TIER ASSIGNMENT

**1a — Three-tier role roster:**

| Tier | Role Name | Type (human / non-human) | Dataverse stock role? | Custom role? | Primary function |
|------|-----------|--------------------------|----------------------|--------------|------------------|

For each tier:
- **Admin ceiling**: The role with the broadest access to {{topic}} (e.g., System Administrator, Custom Admin role, or a power user with organization-level write).
- **Service account / mid-tier**: Any non-human role — Power Automate, integration user, scheduled job account, API service principal, or background process account. If no non-human account exists in the scenario: use the highest-privilege non-admin human role (e.g., Sales Manager, Team Lead, or equivalent). State this substitution explicitly.
- **CS floor**: The Customer Service Representative (stock role or a custom equivalent). This is the baseline minimum human access.

**1b — Stock role identification:**

Name every Dataverse stock role present (Customer Service Representative, Basic User, System Customizer, System Administrator, or others). State how each interacts with custom roles or FLS profiles configured for {{topic}}.

---

## STAGE 2 — COMPARATIVE ACCESS GRID

For each entity {{topic}} touches, build a three-column comparison grid:

**Entity: [name] — OWD: [Private / BU / Parent-Child BU / Organization]**

| Operation | Admin Ceiling | Service Account / Mid-Tier | CS Floor | Tier Inversion? |
|-----------|--------------|---------------------------|----------|-----------------|

Operations: Create / Read / Write / Delete / Assign. For each cell: YES / NO / CONDITIONAL (state condition) + Record Scope (Org / BU / Team / User).

"Tier Inversion?" = YES if Service Account or CS holds a privilege or scope that the tier above does not. This is unexpected. Flag it and add to ACCESS FINDINGS with Finding Type = TIER-INVERSION.

Build one grid per entity. After all grids are complete, produce a cross-entity rollup:

| Entity | Admin Ceiling: broadest scope | Service Account: broadest scope | CS Floor: broadest scope | Service Account > CS on anything? |
|--------|------------------------------|--------------------------------|--------------------------|-----------------------------------|

"Service Account > CS on anything?" = YES if the service account holds any privilege or scope CS does not. State which and why.

---

## STAGE 3 — FIELD-LEVEL SECURITY ACROSS TIERS

For every entity, build a three-tier FLS grid:

| Entity | Field | Sensitivity | FLS Profile? | Admin: Read/Write | Service Account: Read/Write | CS Floor: Read/Write | Gap? |
|--------|-------|-------------|-------------|-------------------|----------------------------|----------------------|------|

Gap conditions:
- A sensitive field with no FLS profile is a gap at all tiers — add as FLS-EXPOSURE, Severity = CRITICAL.
- A service account that reads or writes a sensitive field without a business justification for the automation function is a gap — add as FLS-EXPOSURE for the SERVICE-ACCOUNT tier.
- The CS floor that reads a sensitive field the job function does not require is a gap — add as FLS-EXPOSURE for CS-FLOOR.

---

## STAGE 4 — GAP ANALYSIS ACROSS TIERS

**4a — Escalation paths (per tier):**

For each tier: can a role in this tier reach a higher tier's privilege level through team membership, security role assignment, record ownership, or BU configuration?

| Tier | Escalation Vector Checked | Can Reach Higher Tier? | Path or Rule-Out |
|------|--------------------------|----------------------|------------------|

Rule-out format: "Checked [tier role] for: team-membership-write / role-assign-write / ownership-reassign / BU-config-write — escalation impossible because [specific control]."

Service accounts require special attention: can an integration user add itself (or its service principal) to a team that grants organization-level access? Trace this explicitly.

**4b — Sharing rule audit:**

| Rule Name | Entity | Access Opened | Which Tier Benefits? | Exceeds OWD + Role? | Conflict? |
|-----------|--------|---------------|---------------------|---------------------|-----------|

For rules that benefit the SERVICE-ACCOUNT tier: state whether the rule was configured knowing the service account would benefit, or whether it was intended for human roles only.

**4c — BU scope per tier:**

For each tier: state the BU scope. Show at least one path per tier:
`[Role] → [BU scope] → [child BU records: visible YES/NO] → [reason]`

Note whether the service account has Organization-level scope when BU-level would suffice for its automation function.

**4d — Cross-table cascade:**

Identify the highest-sensitivity entity. Trace through at least two relationship hops from each of the three tiers:

`[Tier Role] → [Entity A, access] → [Relationship + cascade behavior] → [Entity B, access] → [Relationship + cascade behavior] → [Entity C, access]`

At each hop: state whether access is intentional or emergent. Note whether the service account tier inherits more cascade access than its function requires.

**4e — Least-privilege assessment:**

| Tier | Role | Persona / Function | Privileges Beyond Function Need | LP Score (0–10) | Status |
|------|------|-------------------|--------------------------------|-----------------|--------|

For service accounts: "Persona / Function" = the specific automation or integration task the account performs. "Privileges Beyond Function Need" = any privilege the account holds that the automation does not require.

Flag every role scoring below 7 as over-privileged. For service accounts scoring below 5: mark as CRITICAL — service accounts with significant excess privilege are a high-value target for privilege escalation.

Now return to the ACCESS FINDINGS register and fill it in completely. Every Fix entry must name the specific configuration object and its target state.

---

## V-05 — Combined: Minimum Viable Secure Benchmark + Imperative Assertion Phrasing

**Axis:** Inertia framing (minimum viable secure benchmark — every finding is rated against the least configuration needed to be safe) + phrasing register (imperative assertion format — MUST / MUST NOT / SHALL / SHALL NOT with explicit rationale)
**Hypothesis:** MVS framing prevents both gold-plating (adding security beyond what the data requires) and under-protection (missing the baseline that the data demands). Pairing it with imperative assertions prevents vague language: every claim must pass or fail against a stated necessity, not a preference. This is the format most likely to surface C-09 (least-privilege) and C-02 (FLS as safety criterion) because both are grounded in necessity rather than best practice.

---

You are running a permissions trace signal for: {{topic}}

---

**Framework: Minimum Viable Secure (MVS)**

For each access decision in {{topic}}, the standard is: **what is the least configuration needed to protect this data appropriately?**

- **Below MVS**: The configuration exposes sensitive data or enables unintended access that must be remediated. CRITICAL gap.
- **At MVS**: The configuration meets the minimum protection standard for the data sensitivity. Acceptable.
- **Above MVS**: The configuration exceeds the minimum standard — optional hardening. Document but do not require.

Every assertion below is written in imperative form: MUST (required to reach MVS), SHOULD (recommended above MVS), MAY (optional hardening). A MUST that is not satisfied is a CRITICAL gap. A SHOULD that is not satisfied is a HIGH gap.

---

**MVS COMPLIANCE REGISTER — do not fill this now. Return here after Section 4.**

| # | Assertion ID | Status | Gap Level | Exact Remediation |
|---|-------------|--------|-----------|-------------------|

Status: SATISFIED / VIOLATED / NOT-APPLICABLE (with reason)
Gap Level: CRITICAL (MUST violated) / HIGH (SHOULD violated) / ACCEPTED (SHOULD not satisfied, acceptable risk documented)
Exact Remediation: name the specific configuration object and target state — "improve security" does not qualify.

---

## SECTION 1 — SCOPE AND SENSITIVITY CLASSIFICATION

**1.1** List every entity {{topic}} creates, reads, updates, or deletes.

For each entity: state the data sensitivity (High / Medium / Low) and the rationale. High = PII, financial, health, credentials, or regulated data. Medium = internal business data not publicly available. Low = reference data with no sensitivity.

MVS assertion: **MUST-1.1**: For every entity with High or Medium sensitivity, the org-wide default MUST NOT be set to Organization (all users read all records) unless the feature design explicitly requires it and the business justification is documented. State whether each entity satisfies or violates MUST-1.1.

**1.2** Identify every security role with any privilege on the entities listed in 1.1.

For each role: state its type (stock Dataverse role / custom role / both), its primary persona or job function, and the entities it touches. Name every Dataverse stock role by its standard name (Customer Service Representative, Basic User, System Customizer, System Administrator, or others).

MVS assertion: **MUST-1.2**: Every role MUST have a documented business justification for each entity it holds privileges on. State whether each role satisfies or violates MUST-1.2 for each entity. Roles without a justifiable business function on an entity are candidates for privilege removal.

---

## SECTION 2 — OPERATION-ROLE ASSERTIONS

**2.1** For each entity and each role: build the operation-role table.

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope | MVS Assessment |
|----------------|------|--------|------|-------|--------|--------|--------------|----------------|

Allowed values: YES / NO / CONDITIONAL (state condition). Record Scope: Org / BU / Parent-Child BU / Team / User / Sharing-[rule name]. MVS Assessment: AT-MVS / BELOW-MVS (state why) / ABOVE-MVS (state why).

MVS assertion: **MUST-2.1**: Every role holding Write or Delete on a High-sensitivity entity MUST be scoped to the minimum record scope needed for the role's function (User or Team scope preferred over BU or Org scope). State whether each Write/Delete privilege satisfies this assertion.

MVS assertion: **MUST-2.2**: Assign privilege on High or Medium sensitivity entities MUST only be granted to roles whose function requires record reassignment. State whether each Assign grant satisfies this assertion or flags as BELOW-MVS.

**2.2** Cross-reference with stock role behavior: for each Dataverse stock role, does its out-of-box privilege table satisfy or violate MUST-2.1 and MUST-2.2 in this scenario? State explicitly.

---

## SECTION 3 — FIELD-LEVEL SECURITY ASSERTIONS

**3.1** For each entity, enumerate sensitive fields (PII, financial, health, credentials, internal audit).

For each sensitive field:

Assert **MUST-3.1**: Field [name] on [Entity] MUST be restricted by a field security profile if it holds [sensitivity category] data. Current state: [FLS profile exists: YES / NO]. MVS compliance: SATISFIED / VIOLATED.

If VIOLATED: add to MVS Compliance Register immediately with Gap Level = CRITICAL.

Assert **MUST-3.2**: The field security profile for [field] MUST assign Read access only to roles whose function requires reading [field type] data. For each role assigned to the profile: "The [Role] function [REQUIRES / DOES NOT REQUIRE] reading [field] because [reason]. SATISFIED / VIOLATED."

Assert **MUST-3.3**: If an entity has no sensitive fields, this MUST be confirmed by explicit enumeration: "Confirmed: [Entity] holds no High or Medium sensitivity fields. Fields reviewed: [complete list]." A blanket assertion without the field list VIOLATES MUST-3.3.

**3.2** For each FLS profile that exists: state the roles assigned to it for Read and Write. Assert whether each role assignment is at, below, or above MVS.

SHOULD-3.4 (above MVS, recommended): Sensitive fields SHOULD be restricted with separate Read and Write profiles where write access is needed by fewer roles than read access. State whether this hardening is in place.

---

## SECTION 4 — GAP ANALYSIS ASSERTIONS

**4.1 — Privilege escalation:**

Assert **MUST-4.1**: No role SHALL hold Write on security role assignment or business unit configuration unless its function explicitly requires cross-role or BU administration. For each role with such Write privilege: assert whether the function justification exists. If not: VIOLATED.

Assert **MUST-4.2**: No role SHALL be able to add itself to an owner team or access team that grants a higher record scope than the role's direct privilege. For each team-scoped entity: trace whether this path is open or closed. State the specific control that closes it. A team with membership managed by a role that can also modify its own membership VIOLATES MUST-4.2.

Assert **MUST-4.3**: Every active sharing rule MUST be reviewed for continued intent. A sharing rule that reopens access the OWD + role combination intends to restrict VIOLATES MUST-4.3. For each rule: state whether it is at-MVS (still valid), below-MVS (reopens restricted access), or above-MVS (hardening beyond what the role model provides). Rules with no documented review date SHOULD be flagged for review (SHOULD-4.4).

**4.2 — Business unit hierarchy:**

Assert **MUST-4.5**: For roles with BU-scoped access on High or Medium sensitivity entities: access to records owned by users in other BUs MUST be restricted unless the role's function requires cross-BU visibility. Show at least one path: `[Role] → [BU scope] → [sibling or child BU records: accessible YES/NO] → [MVS assessment]`.

**4.3 — Cross-table cascade:**

Identify the highest-sensitivity entity. Trace through at least two relationship hops:

`[Role] → [Entity A: operation, scope] → [Relationship + cascade: Parental / Referential / None] → [Entity B: operation, scope] → [Relationship + cascade] → [Entity C: operation, scope]`

Assert **MUST-4.6**: Cascade access to High-sensitivity records MUST be intentional. At each hop: state whether the access is explicitly configured or an emergent consequence of the relationship behavior. An emergent hop that grants access to High-sensitivity data VIOLATES MUST-4.6 unless the relationship behavior is necessary and the cascade scope is documented.

**4.4 — Least-privilege audit:**

| Role | Persona | Privileges Held Beyond MVS Need | LP Score (0–10) | MVS Status |
|------|---------|--------------------------------|-----------------|------------|

MVS Status: COMPLIANT (at or above MVS) / BELOW-MVS (violates one or more MUST assertions). For each BELOW-MVS role: state which MUST assertion is violated and the specific privilege to reduce.

SHOULD-4.7 (above MVS): Roles MAY be further restricted below MVS to above-MVS hardening levels where the data sensitivity justifies it. State whether any such hardening is in place or recommended.

Now return to the MVS Compliance Register and fill it in. Every MUST violation must have an Exact Remediation entry naming the configuration object and its target state. Format: `[Assertion ID]: Change [object] from [current state] to [target state] in [solution location]. After fix: [verification step confirming MVS compliance].`
