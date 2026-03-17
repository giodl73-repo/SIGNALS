# trace-permissions Variate -- Round 1
**Date:** 2026-03-15
**Rubric:** v1 (C-01 through C-09)
**Target criteria:** C-01 (operation-role matrix), C-02 (record access scope), C-03 (field-level security), C-04 (security gap identification), C-05 (escalation path tracing), C-06 (sharing rule conflict), C-07 (team membership gap), C-08 (remediation guidance), C-09 (defense-in-depth)

---

## Round 1 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Role sequence -- entity-centric, risk-surface-first | Anchoring on entities (not roles) before assigning roles forces C-01 completeness; the riskiest entity drives the ordering, which naturally surfaces C-04 before analysis diffuses into low-sensitivity objects |
| V-02 | Output format -- prose investigation log, no tables | Narrative format with explicit "finding" and "verdict" tokens tests whether C-03/C-04 survive without table scaffolding; reveals whether structured output is doing the work or the underlying reasoning is |
| V-03 | Phrasing register -- conversational walking-investigator | First-person investigation voice ("I checked ... I found ... this surprised me because ...") lowers the formality barrier and forces the model to surface judgment, not just enumeration; hypothesis is that C-04/C-07 coverage improves when the model is invited to express surprise |
| V-04 | Combined: lifecycle emphasis (extended inventory gate) + output format (phase-end checkpoint summary) | Making inventory a complete, gated phase with an explicit sign-off table before gap analysis prevents the most common failure mode: jumping to escalation analysis before FLS is mapped; checkpoint summaries test whether the model can self-audit |
| V-05 | Combined: inertia framing (assumptions named before analysis) + role sequence (CS-last as validator) | Listing the team's stated assumptions about the security model before tracing makes assumption-violation the primary output type; CS role run last validates or falsifies those assumptions from the user perspective rather than the architect's |

---

## V-01 -- Role Sequence: Entity-Centric, Risk-Surface-First

**Axis:** Role sequence (ordered by entity sensitivity, not by role hierarchy -- the riskiest data surface is traced first regardless of which role owns it)
**Hypothesis:** Anchoring the analysis on entities before roles prevents the common failure of mapping low-risk role-operations in detail while glossing over high-sensitivity entities that many roles touch partially. Starting with the riskiest entity pulls C-03 and C-04 to the front of the output before attention degrades.

---

You are running a permissions trace signal for: {{topic}}

---

**SECURITY GAP LOG -- do not fill this now. Populate it as you find each gap throughout the analysis.**

| # | Entity | Field / Operation | Role(s) Affected | Gap Type | Risk | Fix |
|---|--------|-------------------|-----------------|----------|------|-----|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE
Risk: CRITICAL / HIGH / MEDIUM

Add a row the moment you identify a gap. Do not defer to the end.

---

## PHASE 1 -- ENTITY INVENTORY AND SENSITIVITY RANKING

You are a Dataverse security architect. Before any role analysis, map the complete data surface.

**Step 1.1 -- Entity catalog:**

List every entity that {{topic}} creates, reads, updates, or deletes. For each:

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) | Reason for Sensitivity Rating |
|--------|-----------------|-----------------------------------|-------------------------------|

Sensitivity rating criteria:
- High: contains PII, financial data, credentials, health data, or records that would cause material harm if exposed
- Medium: contains internal-only data, case history, pricing, or records that should not cross BU boundaries
- Low: lookup data, configuration records, non-personal reference data

**Step 1.2 -- Risk-surface ordering:**

Reorder your entity list from highest to lowest sensitivity. This is your analysis order for all subsequent phases. State: "I will trace entities in this order: [list]. The highest-risk entity is [name] because [reason]."

You will complete Phases 2 and 3 for your highest-sensitivity entity first, then work down the list. Do not interleave entities.

---

## PHASE 2 -- PER-ENTITY TRACE (repeat for each entity, highest sensitivity first)

### Entity: [name] (Sensitivity: [rating])

**2a -- Who can touch this entity (operation-role matrix):**

| Role | Create | Read | Write | Delete | Assign | Record Scope |
|------|--------|------|-------|--------|--------|--------------|

Record Scope options: Org / BU / Parent-Child BU / Team / User / Sharing-[rule name]
Include every role with any privilege, including read-only. Do not combine roles.

**2b -- What fields does each role see (field-level security):**

For every field on this entity:

| Field | Sensitivity Category | FLS Profile Applied? | Roles: Read | Roles: Write | Roles: Denied |
|-------|----------------------|----------------------|-------------|--------------|---------------|

Sensitivity categories: PII / Financial / Health / Credential / Internal-Audit / None

Rules:
- A sensitive field with no FLS profile applied: add a row to the Security Gap Log now. Gap Type = MISSING-FLS. Risk = CRITICAL for PII/Credential/Health, HIGH for Financial/Internal-Audit.
- Do not write "FLS not configured" without listing each sensitive field by name and confirming the absence.
- The Roles: Denied column must be filled -- "none denied" is a valid answer only if explicitly confirmed.

**2c -- Sharing rules active on this entity:**

| Rule Name | Trigger Condition | Access Granted | To Whom | Intended vs. Unexpected |
|-----------|-------------------|----------------|---------|------------------------|

For each rule marked Unexpected: add to the Security Gap Log. Gap Type = SHARING-CONFLICT.

**2d -- Team membership dependency:**

Does any role's access to this entity depend on team membership? If yes:
- Name the team
- State who controls team membership
- Describe the scenario where a user in the right role but the wrong team is blocked
- State whether a user can add themselves (or request addition) to the team

Format: "Users in [Role] who are not in [Team] cannot access [record type] because [OWD + scope]. Team membership is controlled by [Role/mechanism]. Self-addition is [possible / not possible] because [reason]."

If no team dependency exists: confirm explicitly -- "Confirmed: [Entity] access does not depend on team membership. Checked: [what was checked]."

**2e -- Business unit scope:**

For each role with BU-scoped access to this entity: does the BU scope actually confine records, or does the OWD override it? Show one concrete path:
`[Role] at [BU level] -> [OWD behavior] -> [records visible: confined / exposed beyond BU]`

**2f -- Escalation path check:**

For each role with Write on this entity: can that write access be used to elevate to a higher privilege? Check:
- Record Assign (transfer ownership to a higher-privileged user's scope)
- Sharing (share to a higher-privileged role)
- Field modification (modify a field that affects role assignment or BU membership)

Chain format: `[Role] -> [Write action on [Entity]] -> [elevated access reached]`
Rule-out format: "Checked [Role]: write access to [specific fields/operations]. No escalation because [specific reason]."

---

## PHASE 3 -- CROSS-ENTITY CASCADE

After completing Phase 2 for all entities, trace the permission chain across entities.

**Step 3.1 -- Relationship map:**

For your two highest-sensitivity entities, identify their relationships to other entities in scope:

| Source Entity | Relationship Type (1:N / N:N / lookup) | Target Entity | Cascade Behavior (Parental / Referential / None) |
|---------------|----------------------------------------|---------------|--------------------------------------------------|

**Step 3.2 -- Cascade access trace:**

For each relationship: trace whether a role with access to the source entity gains unintended access to related records in the target entity.

Chain format: `[Role] -> [Source Entity, access level] -> [Relationship + cascade behavior] -> [Target Entity, access level]`

State at each hop: INTENTIONAL (access was explicitly configured) or EMERGENT (access flows from relationship cascade behavior).

For any EMERGENT access: add to the Security Gap Log if the access exceeds what the role should hold.

---

## PHASE 4 -- REMEDIATION AND DEFENSE-IN-DEPTH

**Step 4.1 -- Gap remediation:**

For each row in the Security Gap Log:
`[Gap #]: Apply [specific change] to [role / FLS profile / sharing rule / OWD / team config] in [solution location: e.g., Settings > Security > Field Security Profiles]. Current state: [what exists now]. Target state: [what it should be]. After fix: [what a user can / cannot do that they currently can / cannot].`

Generic advice ("review permissions", "add FLS") does not qualify. Each fix must be implementable by a Dataverse administrator reading only this output.

**Step 4.2 -- Defense-in-depth assessment:**

For each entity, assess whether the three enforcement layers operate independently:

| Entity | Security Role Enforces? | FLS Enforces Independently? | Record Scope Enforces Independently? | Single Point of Failure? |
|--------|------------------------|----------------------------|--------------------------------------|-------------------------|

"Enforces Independently?" = YES if bypassing the other two layers still leaves this layer enforcing the control. NO if this layer's protection collapses when another layer is misconfigured.

For any entity with Single Point of Failure? = YES: name which layer is the sole enforcer and what happens if it is misconfigured.

**Step 4.3 -- Stock role coverage:**

Name every Dataverse stock role present in this scenario (Customer Service Representative, Basic User, System Customizer, System Administrator, others). For each:
- State its baseline privilege set relevant to {{topic}}
- State whether custom configuration has strengthened or weakened its baseline
- State whether its presence in the security model is necessary or could be removed

---

## OUTPUT REQUIREMENTS

- Entities must appear in sensitivity order (highest first) throughout the output
- Every sensitive field must appear in a 2b table -- no entity may have its FLS coverage collapsed into a prose statement
- Every gap in the Security Gap Log must have a complete remediation entry in Step 4.1
- The Security Gap Log must be filled progressively (rows added as found), not retroactively filled at the end
- Do not use "See above" or "as noted" -- every finding must be stated where it is relevant

---

## V-02 -- Output Format: Prose Investigation Log

**Axis:** Output format (no tables -- findings written as a structured investigation log with explicit "FINDING", "VERDICT", and "GAP" tokens)
**Hypothesis:** Prose-format output with mandatory finding tokens tests whether the analytical depth required by C-03/C-04/C-05 depends on table scaffolding or is present in the model's underlying reasoning. If prose coverage is weaker, tables are doing structural work; if prose coverage is equal, the model has the reasoning and tables are presentation only.

---

You are running a permissions trace signal for: {{topic}}

Write a permissions trace investigation log. Do not use tables. Use structured tokens to mark findings.

**Token definitions:**

`ENTITY:` -- introduces an entity being analyzed
`ROLE:` -- introduces a role being analyzed within an entity section
`FIELD:` -- introduces a field-level security finding
`FINDING:` -- a specific, named observation about access, scope, or configuration
`GAP:` -- a concrete security gap; must include role/field/record, gap type, and risk level
`VERDICT:` -- a resolution of an open question or assertion
`FIX:` -- a specific remediation action (no generic advice)

Every GAP token must be followed by a FIX token before moving to the next section.

---

## INVESTIGATION LOG

### Scope and Data Surface

Begin your investigation log here. Start with a statement of scope: what entities does {{topic}} touch, what is the overall sensitivity classification of the data surface, and what stock Dataverse roles (Customer Service Representative, Basic User, System Customizer, System Administrator) are present?

Write: "This investigation covers [N] entities. The highest-sensitivity data surface is [Entity] because [reason]. Stock roles present: [list]. Custom roles configured: [list]."

---

### Entity-by-Entity Trace

For each entity, write a section beginning with the ENTITY: token.

For each entity, you must cover:

**Operations and scope:** State, for each role, what operations it can perform and the record scope. Use the ROLE: token for each. Example:

`ROLE: Customer Service Representative -- Read on Case at BU scope; Write on Case at User scope (own records only); no Create, Delete, or Assign. Record scope is Business Unit for Read because OWD = Business Unit.`

Do not combine roles. Do not use "all roles" -- each role is a separate ROLE: entry.

**Field-level security:** For every sensitive field (PII, financial, health, credential, internal-audit), write a FIELD: token entry. Example:

`FIELD: SSN on Contact -- Sensitivity: PII. FLS profile applied: YES, profile name "Contact-PII-Restricted". Roles with Read access under profile: System Administrator, Compliance Officer. Roles denied Read: Customer Service Representative, Basic User. Write access: System Administrator only.`

If no FLS profile exists for a sensitive field, write:

`FIELD: [name] on [Entity] -- Sensitivity: [category]. FLS profile applied: NONE. FINDING: This field is readable by any role with Entity Read privilege on [Entity]. GAP: MISSING-FLS on [Entity].[field]. Role(s) affected: [all roles with entity-level Read]. Risk: CRITICAL. FIX: Create field security profile "[suggested name]" in Settings > Security > Field Security Profiles. Add columns: [field name]. Grant Read to: [roles that require it]. Deny all others.`

**Sharing rule audit:** For each sharing rule active on this entity, write a FINDING: entry naming the rule, its trigger, the access it opens, and whether that access is intentional. If a sharing rule opens access beyond the OWD + security role intent:

`GAP: SHARING-CONFLICT on [Entity]. Rule "[name]" grants [access] to [role/group] when [trigger]. This opens [what records] to [who] beyond what the role-defined scope permits. Risk: [HIGH/MEDIUM]. FIX: [specific rule change].`

**Team membership dependency:** If access to this entity depends on team membership, write a FINDING: naming the team, the blocked scenario, and who controls membership. If a user can reach higher-privilege team membership through any available action:

`GAP: TEAM-INJECTION on [Entity]. [Role] can [action] to gain membership in [Team], reaching [elevated access]. Risk: HIGH. FIX: [specific control change].`

**Escalation path:** For each role with Write access, check whether that write access can escalate privilege. Write VERDICT: for each role:

`VERDICT: [Role] escalation check. Checked: Write on [field list / operations]. Escalation via [Assign / Share / field modification]: [CONFIRMED or RULED OUT]. [If confirmed] Path: [Role] -> [action] -> [elevated access]. GAP: [details]. [If ruled out] Because: [specific mechanism preventing escalation].`

---

### Cross-Entity Cascade

After all entities are traced, write the cascade section. For the highest-sensitivity entity, trace through at least two relationship hops:

`ENTITY: [Entity A] -- [access level] for [Role] -> [relationship type + cascade behavior] -> ENTITY: [Entity B] -- [access level resulting] -> [relationship type + cascade behavior] -> ENTITY: [Entity C] -- [access level resulting]`

For each hop: VERDICT: INTENTIONAL or EMERGENT. If EMERGENT and the access exceeds what the role should hold: write a GAP: entry.

---

### Defense-in-Depth Assessment

For each entity, write a VERDICT: addressing whether the three enforcement layers (security role, FLS, record scope) operate independently:

`VERDICT: [Entity] defense-in-depth. Security role layer independently enforces: [YES/NO, reason]. FLS layer independently enforces: [YES/NO, reason]. Record scope layer independently enforces: [YES/NO, reason]. Single point of failure: [YES -- layer name / NO].`

If any entity has a single point of failure, write a GAP: and FIX:.

---

### Investigation Summary

Close the investigation log with:
- Count of entities traced
- Count of roles covered
- Count of sensitive fields reviewed
- Count of GAP tokens written
- List of all GAP tokens with their FIX tokens (cross-reference only -- do not repeat the full text)
- VERDICT: on whether the security model meets least-privilege for the Customer Service Representative stock role

---

## V-03 -- Phrasing Register: Conversational Walking-Investigator

**Axis:** Phrasing register (first-person investigator voice, conversational framing, explicit surprise and judgment language)
**Hypothesis:** Inviting judgment ("this surprised me", "this feels wrong") rather than pure enumeration prompts the model to surface C-04 (gap identification) and C-07 (team gaps) more reliably. Formal specification voice suppresses judgment tokens; investigator voice makes them mandatory.

---

You are running a permissions trace signal for: {{topic}}

You are a Dataverse security investigator who has just been handed access to this system for the first time. Your job is to walk through the security configuration and write up what you find -- including what surprises you, what concerns you, and what you would fix.

Write in first person. Use plain language. When something concerns you, say so. When something is fine, say so and explain why.

---

**Before you begin -- write your assumptions:**

Before reading any configuration, state what you would expect a well-configured system for {{topic}} to look like:
- What roles should exist?
- What is the highest-sensitivity data, and who should be able to read it?
- What is the Customer Service Representative's job, and what is the minimum access they need to do it?
- What would "too much access" look like for a CS rep?

Write these as expectations. You will revisit each one at the end to see if the system matched them.

---

## WALK-THROUGH

### First look: entities and data surface

Start by listing everything {{topic}} works with -- every entity you find. For each entity, tell me:
- What data lives on it (roughly)
- Whether that data feels sensitive and why
- What the org-wide default is and whether that setting makes sense given the data

Rank the entities by how worried you would be if a CS rep had too much access to them. Explain your ranking.

### Operations: who can do what

For each entity, starting with the one you ranked most sensitive:

Walk me through which roles can perform each operation (Create, Read, Write, Delete, Assign) and what records they can reach. Use plain language:

"The Customer Service Representative can read all Cases in their business unit. They can also write to Cases they own, but not to Cases owned by other reps in the BU. That feels right to me -- [explain why]. What concerns me slightly is [specific thing]."

Or: "I notice the Customer Service Representative can delete Cases. That surprised me -- deletion is permanent and usually reserved for admin roles. Let me note this."

For every operation that surprises you (too much access or too little), flag it explicitly. These are your security signals.

You must cover:
- Every role with any privilege on this entity
- Every privilege (C/R/W/D/A) with its record scope -- do not collapse these into "standard access"
- Why each access grant feels appropriate or concerning given the persona

### Field-level security: what can each role see

For each entity, walk through the fields that feel sensitive -- PII, financial, health data, case notes, internal audit fields, credentials.

For each sensitive field, tell me:
- Whether a field security profile is applied
- If yes: who can read it and who cannot, and whether that matches the persona's job
- If no: who can currently read it (every role with entity-level Read), and whether that concerns you

Use this format for a field with a problem:

"I found that the [field name] field on [Entity] has no field security profile. That means anyone with Read access to [Entity] -- including Customer Service Representatives -- can see [what the field contains]. That concerns me because [reason]. I would fix this by [specific fix]."

Use this format for a field that is fine:

"The [field name] field on [Entity] is covered by the [profile name] profile. Only [roles] can read it. That matches the job -- [explain]. No concern here."

You must cover at least three sensitive fields across the entities in scope. Do not collapse this into "FLS is configured" -- walk each field individually.

### Sharing rules: what gets opened by rules

For each entity, check whether any sharing rules are active. For each rule you find:

Tell me the rule's name, what triggers it, what access it opens, and who benefits. Then tell me whether you expected this rule to exist or whether it surprised you.

If a rule opens access that feels broader than the role model intends, say so:

"I found a sharing rule called [name] that triggers when [condition] and gives [role/group] [access level] to [records]. That surprised me because the role model says [role] should only see [what the role says], but this rule opens [what the rule opens]. This feels like it could let a CS rep see [records they should not see]. I would revisit this rule."

If no sharing rules are active, confirm you checked: "I looked for sharing rules on [Entity] and found none. I checked [where]."

### Team access: who gets blocked and why

For each entity where team membership affects access:

Tell me which team is involved, what happens to a user who is in the right role but not in the team, and whether there is any way a user could get themselves added to the team without an admin's help.

"A CS rep who is not in the [Team name] team cannot access [record type]. That could be a problem if [scenario where this blocks legitimate work]. The team is managed by [who]. There is [no way / a way] for a CS rep to add themselves -- [explain either way]. [If a way exists: that concerns me because ...]"

If no team dependency exists, confirm: "I confirmed that access to [Entity] does not depend on team membership."

### Privilege escalation: could someone do more than they should

For each role with any Write access: think through whether that write access could be used to reach a higher privilege level. Walk me through what you checked and what you concluded.

"I looked at what the Customer Service Representative can write. They can write to [fields / records]. Could they use that to escalate? I checked [specific things]. My conclusion: [escalation is / is not possible]. [If possible: here is how: ...] [If not: the reason is ...]"

If you find an escalation path, this is a significant finding -- describe it clearly and tell me what you would do about it.

### Cross-entity cascade: what access follows relationships

Find the most sensitive entity in scope. Trace through its relationships: when a role has access to this entity, does that automatically give access to related records in other entities?

Walk through at least two relationship hops. For each hop:

"[Entity A] has a [relationship type] to [Entity B]. The cascade behavior is [Parental / Referential / None]. That means a role with [access] on [Entity A] [does / does not] automatically get [access] on [Entity B]. [Is that intentional?] [Any concerns?]"

---

## CHECKING BACK: WERE YOUR ASSUMPTIONS RIGHT?

Return to the assumptions you wrote at the start. For each one:

- State the assumption
- State what you found
- State whether the system matched your expectation, exceeded it (more secure than expected), or fell short

"I assumed [assumption]. What I found: [finding]. The system [matched / exceeded / fell short of] that expectation because [reason]."

---

## WHAT I WOULD FIX

Write a plain-language remediation list. For each problem you found:

"Problem: [what the problem is, in one sentence]. Why it matters: [the risk]. Fix: [the specific change to make, named precisely enough that a Dataverse admin can implement it -- role, profile, rule, or OWD -- no generic advice]."

Close with a one-paragraph assessment of whether the Customer Service Representative's access in {{topic}} feels right -- appropriate for the job, not over-privileged, with no surprises that concern you. Be honest.

---

## V-04 -- Combined: Extended Inventory Gate + Phase-End Checkpoint Summaries

**Axis:** Lifecycle emphasis (inventory is a fully gated phase with explicit completion criteria) + output format (each phase ends with a structured checkpoint summary the model must complete before proceeding)
**Hypothesis:** Hard phase gates with mandatory checkpoint summaries before proceeding prevent the most common skip pattern: completing the operation matrix then producing prose analysis without building FLS tables. Checkpoint summaries force the model to self-audit coverage before analysis begins, catching gaps while they can still be fixed in the output.

---

You are running a permissions trace signal for: {{topic}}

---

**MASTER GAP TABLE -- do not fill this now. Add rows as you identify gaps. Complete it fully after Phase 3.**

| # | Phase Found | Entity | Role / Field / Rule | Gap Type | Severity | Fix |
|---|-------------|--------|---------------------|----------|----------|-----|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH

---

## PHASE 1 -- INVENTORY (must be fully complete before Phase 2 begins)

You are a Dataverse security architect building the permission foundation for {{topic}}.

**1.1 -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason |
|--------|-----------------|-------------|--------|

List every entity {{topic}} creates, reads, updates, or deletes. OWD options: Private / Business Unit / Parent-Child Business Unit / Organization. Sensitivity: High / Medium / Low.

Do not proceed to 1.2 until every entity is listed.

**1.2 -- Role catalog:**

| Role Name | Type (Stock / Custom) | Primary Persona / Job Function |
|-----------|----------------------|-------------------------------|

List every security role with any privilege in this scenario. Stock roles include: Customer Service Representative, Basic User, System Customizer, System Administrator. Do not omit read-only roles.

**1.3 -- Operation-role matrix:**

Build one table per entity:

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|--------|------|-------|--------|--------|--------------|

Allowed values: YES / NO / CONDITIONAL (state condition in line). Record Scope: Org / BU / Parent-Child BU / Team / User / Sharing-[rule name]. Every role from 1.2 must appear in the matrix for every entity where it holds any privilege.

**1.4 -- Field-level security inventory:**

For each entity in 1.1, build this table:

| Entity | Field | Sensitivity Category | FLS Profile Name | Read: Allowed Roles | Write: Allowed Roles | Denied Roles |
|--------|-------|----------------------|-----------------|---------------------|---------------------|-------------|

Sensitivity categories: PII / Financial / Health / Credential / Internal-Audit / Not-Sensitive.

Rules:
- Every field with Sensitivity Category != Not-Sensitive must have a row
- FLS Profile Name = NONE means no profile is applied -- mark the row with [GAP: MISSING-FLS] and add to Master Gap Table immediately
- If an entity has no sensitive fields: write a single row with Field = "No sensitive fields -- confirmed by reviewing: [field names reviewed]"
- Do not use "FLS not configured" as a blanket statement without per-field confirmation

**1.5 -- Sharing rule inventory:**

For each entity in 1.1:

| Entity | Rule Name | Trigger | Access Granted | Recipient | Intentional? | Exceeds OWD+Role Scope? |
|--------|-----------|---------|----------------|-----------|-------------|------------------------|

If no sharing rules exist: "Confirmed no sharing rules on [Entity] -- checked Settings > Advanced Settings > Business Management > Sharing [or equivalent]. Zero rules found."

---

## *** PHASE 1 CHECKPOINT -- complete this before proceeding to Phase 2 ***

Answer each question explicitly. Do not proceed until all answers are YES or N/A.

| Check | Answer | Notes |
|-------|--------|-------|
| Every entity that {{topic}} touches is in the 1.1 table | YES / NO | |
| Every role present in the scenario is in the 1.2 catalog | YES / NO | |
| The 1.3 matrix contains a row for every role-entity pair with any privilege | YES / NO | |
| Every sensitive field appears in the 1.4 FLS table | YES / NO | |
| Every NONE entry in the 1.4 FLS Profile Name column has been added to the Master Gap Table | YES / NO / N/A | |
| The 1.5 sharing rule inventory is complete (including explicit "no rules" confirmation) | YES / NO | |
| Stock roles (Customer Service Representative, Basic User, System Customizer, etc.) are represented where applicable | YES / NO | |

**PHASE 1 COMPLETE: [YES / NO -- if NO, complete the missing items above before continuing]**

---

## PHASE 2 -- GAP ANALYSIS

You may now proceed. All inventory tables are complete.

**2.1 -- Privilege escalation analysis:**

For each role in the 1.2 catalog: check whether it holds Write on any of the following escalation vectors: team membership management, security role assignment, record ownership reassignment (Assign), BU configuration, or field modification that affects role or BU.

For each role:
- If escalation vector exists: chain format: `[Role] -> [Write action on X] -> [Elevated access on Y]`. Add to Master Gap Table.
- If no escalation vector: rule-out format: "Checked [Role]: holds Write on [privilege list audited]. No escalation because [specific mechanism preventing it]." A verdict without named privileges does not pass.

**2.2 -- Business unit scope analysis:**

For each role in the 1.3 matrix with BU or Parent-Child BU scope: state whether a user in that role at a parent BU can read or write child BU records. Show one concrete path per role:
`[Role] -> [BU scope from matrix] -> [OWD behavior] -> [child BU records: accessible YES/NO] -> [reason]`

**2.3 -- Team membership gap analysis:**

For each team-dependent access configuration identified in Phase 1: state the blocked scenario and whether self-addition is possible.
Format: "Users in [Role] not in [Team] cannot access [record type] because [OWD + scope]. Team membership controlled by [Role/mechanism]. Self-addition is [possible / not possible] because [reason]."

**2.4 -- Cross-table cascade:**

Identify the highest-sensitivity entity from 1.1. Trace through at least two relationship hops:
`[Role] -> [Entity A, operation, scope] -> [Relationship type + cascade behavior] -> [Entity B, operation, scope] -> [Relationship type + cascade behavior] -> [Entity C, operation, scope]`

At each hop: INTENTIONAL (explicitly configured) or EMERGENT (consequence of cascade behavior). Emergent access that exceeds the role's direct grant: add to Master Gap Table as CASCADE-OVERREACH.

---

## *** PHASE 2 CHECKPOINT -- complete this before proceeding to Phase 3 ***

| Check | Answer | Notes |
|-------|--------|-------|
| Every role in the 1.2 catalog has an escalation verdict (confirmed or ruled out with evidence) | YES / NO | |
| Every BU-scoped role has a concrete parent->child access path shown | YES / NO | |
| Every team-dependent access configuration has a blocked-scenario statement | YES / NO | |
| The cross-table cascade covers at least two relationship hops | YES / NO | |
| All new gaps found in Phase 2 have been added to the Master Gap Table | YES / NO | |

**PHASE 2 COMPLETE: [YES / NO]**

---

## PHASE 3 -- ASSESSMENT AND REMEDIATION

**3.1 -- Least-privilege assessment:**

| Role | Persona | Privileges Beyond Persona Need | LP Score (0-10) | Status |
|------|---------|-------------------------------|-----------------|--------|

LP Score: 10 = exact least-privilege. 7-9 = minor excess. 4-6 = moderate excess. 0-3 = significant excess.
For each role with LP Score < 7: state the specific privilege to reduce and the target scope.

**3.2 -- Defense-in-depth layer assessment:**

For each entity in 1.1:

| Entity | Security Role Layer: Independent? | FLS Layer: Independent? | Record Scope Layer: Independent? | Single Point of Failure |
|--------|----------------------------------|------------------------|----------------------------------|------------------------|

"Independent?" = YES if this layer enforces access even if the other two layers are misconfigured. NO if this layer's protection collapses when another layer fails.

For any entity with a Single Point of Failure: add to Master Gap Table with Gap Type = SINGLE-LAYER-FAILURE.

**3.3 -- Remediation for every gap in the Master Gap Table:**

For each row:
`[Gap #]: Change [privilege / FLS profile / sharing rule / OWD / team config] on [entity/field/role] from [current state] to [target state] in [solution location]. After fix: [what a user can or cannot do that they currently can or cannot].`

Generic advice does not qualify. Each fix must be implementable by a Dataverse administrator reading only this output.

---

## *** PHASE 3 CHECKPOINT ***

| Check | Answer | Notes |
|-------|--------|-------|
| Every role has an LP score | YES / NO | |
| Every entity has a defense-in-depth assessment | YES / NO | |
| Every row in the Master Gap Table has a complete remediation entry | YES / NO | |
| Customer Service Representative stock role coverage is addressed | YES / NO | |

**ANALYSIS COMPLETE: [YES / NO]**

---

## V-05 -- Combined: Inertia Framing (Stated Assumptions) + CS-Last Validation

**Axis:** Inertia framing (the team's stated assumptions about the security model are written down before analysis begins, making assumption-violation the primary output type) + role sequence (CS role traced last as a validator of expert-level design claims)
**Hypothesis:** Stating the team's design assumptions explicitly before tracing makes the primary output type "this assumption holds / this assumption is violated," which is easier for reviewers to evaluate and more directly surfaces C-04 (gap identification). Running the CS role last -- after the expert-level design is traced -- turns the CS analysis into a test of the design claims rather than an independent description.

---

You are running a permissions trace signal for: {{topic}}

---

**Before you trace anything: write down the assumptions.**

Based on what you know about {{topic}} from its name and context, state what the security design should be guaranteeing. These are the claims the design is trying to make. You will test each one.

Write 5 to 8 security assumptions in this format:

| A# | Assumption | Testable By |
|----|-----------|-------------|
| A-01 | [What the security design should guarantee, stated as a positive claim] | [Which phase of analysis will confirm or refute this] |

Example assumptions (replace with ones specific to {{topic}}):
- "Customer Service Representatives cannot read financial fields on Account records"
- "No role can escalate from CS-level access to admin-level access without IT intervention"
- "All PII fields are protected by field security profiles"
- "Sharing rules do not re-expose records that the OWD restricts"

These are your hypotheses. Every finding in the trace should point back to one of them.

---

**GAP LOG -- add rows as you find violations. Note which assumption each gap violates.**

| # | Assumption Violated | Entity | Detail | Gap Type | Risk | Fix |
|---|-------------------|--------|--------|----------|------|-----|

---

## PHASE 1 -- DESIGN TRACE: THE EXPERT-LEVEL SECURITY MODEL

You are a Dataverse security expert. You have designed the security model for {{topic}}. Trace what the design is supposed to do -- and confirm that it actually does it.

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity | Design Rationale for OWD Choice |
|--------|-----------------|-------------|----------------------------------|

The "Design Rationale" column is mandatory. State why each OWD was chosen -- what the design is trying to enforce with this setting.

**1b -- Operation-role matrix (from the designer's perspective):**

For each entity, build:

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope | Why This Role Has This Access |
|----------------|------|--------|------|-------|--------|--------|--------------|-------------------------------|

The "Why" column is mandatory. State the persona's need that justifies each access grant. If you cannot state a justification, flag the grant as unexplained.

**1c -- Field-level security (from the designer's perspective):**

For each entity, for each sensitive field (PII, Financial, Health, Credential, Internal-Audit):

| Entity | Field | Sensitivity | FLS Profile | Assumption Protected | Read: Who | Write: Who | Denied: Who |
|--------|-------|-------------|-------------|---------------------|-----------|-----------|-------------|

The "Assumption Protected" column maps each FLS decision to the assumption it enforces (reference the A# from your assumption table). If a sensitive field has no FLS profile, the "Assumption Protected" column = **ASSUMPTION UNPROTECTED** -- add to Gap Log now.

**1d -- Privilege escalation (expert review):**

For each role with Write access: trace whether a deliberate design decision prevents escalation, or whether the prevention is emergent (i.e., escalation happens to be impossible due to configuration, not due to explicit intent).

Format: "For [Role]: escalation prevention is [DESIGNED / EMERGENT / NOT PREVENTED]. Evidence: [specific privilege or OWD or sharing rule that prevents / fails to prevent escalation]."

For any role where prevention is NOT PREVENTED or EMERGENT without deliberate design: add to Gap Log.

**1e -- Sharing rule design intent:**

For each sharing rule in scope:

| Rule Name | Design Purpose | Assumption It Serves | Records Exposed | Is the Exposure Scoped? |
|-----------|---------------|---------------------|----------------|------------------------|

"Is the Exposure Scoped?" = YES if the rule opens only the records the design intends; NO if the rule could open records beyond intent. For each NO: add to Gap Log.

**1f -- Team structure design intent:**

For each team-based access configuration: state the design purpose. Who should be in the team? Who controls membership? What is the failure mode if team membership is wrong?

Format: "Team [name] exists to grant [access] to [record type] to [personas]. Without membership, users in [role] cannot [operation]. Membership is controlled by [mechanism]. The design assumption is [A#]: [that assumption]."

---

## PHASE 2 -- ASSUMPTION TESTING: DO THE ASSUMPTIONS HOLD?

For each assumption in your opening table, write a test:

**Test A-[#]: [Assumption text]**

Evidence for: [What you found in Phase 1 that supports this assumption]
Evidence against: [What you found in Phase 1 that contradicts or undermines this assumption]
Verdict: HOLDS / PARTIALLY HOLDS / VIOLATED
If VIOLATED or PARTIALLY HOLDS: describe the gap and add to the Gap Log.

You must write a test for every assumption. A test with no "Evidence against" that concludes HOLDS is valid only if you state what you specifically checked and found clean.

---

## PHASE 3 -- CUSTOMER SERVICE VALIDATION: DOES THE DESIGN HOLD FROM THE USER'S PERSPECTIVE?

You are now a Customer Service Representative using {{topic}} in daily work. The expert in Phase 1 made design claims about what you can and cannot do. Your job is to validate those claims from inside the user experience.

**3a -- What you can actually do:**

Walk through your daily workflow in {{topic}}. For each operation you perform: state what you can access and what scope you can see. Note any access that surprises you -- either because you can do something you did not expect to be able to do, or because you cannot do something the job requires.

For each surprise: add to the Gap Log and reference the assumption it tests.

**3b -- Sensitive fields you can read:**

As a CS rep, which sensitive fields can you see? Walk through each entity you touch and name the fields that appear to contain sensitive data. For each:

- Can you read it?
- Should you be able to, given your job?
- Does this match what the Phase 1 design claimed?

If you can read a sensitive field that the Phase 1 design claimed was restricted: this is a gap. State the discrepancy explicitly: "The design claimed [Assumption A-#], but I can read [field] on [entity]."

**3c -- Where you are blocked and why:**

Name every place you cannot do something the job requires. For each blockage: is this a correct restriction (the design intended it) or a missing access grant (the design has a gap)? Trace the cause: role privilege, OWD, FLS profile, or team membership.

**3d -- CS escalation check:**

Is there any action available to you as a CS rep -- reassigning a record, sharing to another user, joining a team -- that could give you access beyond your role-defined scope? Walk through what is available to you and whether it leads anywhere it should not.

**3e -- Final assumption validation:**

Return to the assumption table. For each assumption, state from the CS perspective whether the assumption matches user experience:

"From the CS perspective: Assumption [A-#] ([assumption text]) [VALIDATED / CONTRADICTED / CANNOT VERIFY FROM CS PERSPECTIVE]. [Evidence from the CS workflow that confirms or contradicts]."

---

## PHASE 4 -- REMEDIATION AND DEFENSE-IN-DEPTH

**4a -- Gap remediation:**

For each row in the Gap Log: write a specific fix.

Format: `[Gap #]: Assumption [A-#] requires [what the assumption claims]. The gap is [what the current configuration does instead]. Fix: [specific configuration change: role/FLS profile/sharing rule/OWD in solution location]. After fix: [assumption holds because ...]`

Generic advice does not qualify. Each fix must name the specific Dataverse configuration element to change.

**4b -- Defense-in-depth layer assessment:**

For each entity: does removing any single enforcement layer (security role / FLS / record scope) collapse the security model?

| Entity | If security role removed: still enforced by FLS + scope? | If FLS removed: still enforced by role + scope? | If record scope removed: still enforced by role + FLS? | Defense-in-depth: STRONG / PARTIAL / WEAK |
|--------|----------------------------------------------------------|-------------------------------------------------|-------------------------------------------------------|------------------------------------------|

For each entity rated PARTIAL or WEAK: name the single point of failure and the assumption it undermines.

**4c -- Assumption coverage summary:**

Close with a table:

| A# | Assumption | Final Verdict | Phase Found | Gap Log # |
|----|-----------|---------------|-------------|-----------|

Every assumption must have a final verdict. A verdict of HOLDS must cite at least one piece of positive evidence from Phase 1 or Phase 3.
