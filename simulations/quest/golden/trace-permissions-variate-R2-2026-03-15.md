# trace-permissions Variate -- Round 2 (Rubric v2)
**Date:** 2026-03-15
**Rubric:** v2 (C-01 through C-12)
**New criteria targeted this round:** C-10 (real-time gap accumulation), C-11 (explicit non-escalation documentation), C-12 (phase-gate completeness checkpoint)
**Prior round retained:** Essential C-01--C-04 and recommended C-05--C-07 are structurally enforced throughout

---

## Round 2 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format -- per-entity inline gap tally (C-10 single-axis) | Requiring a mandatory gap-tally block at the close of every entity section (before advancing to the next entity) forces inline accumulation; the tally must name specific fields and operations checked, not declare completion in prose |
| V-02 | Role sequence -- full-verdict per-role escalation spine (C-11 single-axis) | Organizing output role-first rather than entity-first, with each role section closing on a mandatory ESCALATION VERDICT block naming what was checked and the specific reason escalation is or is not possible, makes C-11 structurally unavoidable |
| V-03 | Lifecycle emphasis -- named inventory gate with per-entity FLS confirmation (C-12 single-axis) | A mandatory PHASE GATE table between inventory and gap analysis -- listing every entity by name with FLS coverage status and scope decision -- forces the completeness assertion C-12 requires; implicit "all reviewed" prose does not satisfy the gate |
| V-04 | Combined: output format (inline gap accumulation) + lifecycle emphasis (gate-then-proceed checkpoint) | Inline gap stream (C-10) feeds the phase gate (C-12): gaps accumulate during traversal and the gate must enumerate them and confirm no inline signals were collapsed; the two mechanisms reinforce each other |
| V-05 | Combined: phrasing register (verdict-per-role discipline) + inertia framing (Dataverse stock defaults as baseline) | Mandating "I checked [Role]: [operations checked] -- VERDICT: [escalation confirmed / ruled out because specific reason]" for every role makes C-11 unavoidable; anchoring every access grant to the Dataverse stock default (what ships out of the box) gives the verdict a concrete reference to rule against and surfaces C-10 gaps as deviations from baseline |

---

## V-01 -- Output Format: Per-Entity Inline Gap Tally

**Axis:** Output format (mandatory gap-tally block at the end of every entity section, before the next entity begins)
**Hypothesis:** Collapsing gap discovery to a post-analysis summary is the primary failure mode for C-10. Requiring the model to stop at the end of every entity and write a gap-tally block -- naming what was found or confirming what was checked and found clean -- forces accumulation at discovery time. The tally block is distinct from the consolidated gap section: it is a record of what the model noticed while inside that entity, not a retrospective sweep.

---

You are running a permissions trace signal for: {{topic}}

---

**RUNNING GAP REGISTER -- do not fill this now. Each entity section will add rows to this table before advancing.**

| # | Entity | Field / Operation | Role(s) | Gap Type | Risk | Fix |
|---|--------|-------------------|---------|----------|------|-----|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH
Risk: CRITICAL / HIGH / MEDIUM

Instructions for this register:
- Add rows inline as you work through each entity
- Do not defer to the end
- If an entity produces no gaps, write a CLEAR entry: "ENTITY CLEAR: [Entity] -- Checked: [operations reviewed], [FLS fields reviewed], [sharing rules checked]. No gaps found."
- CLEAR entries are required -- silence is not acceptable

---

## PHASE 1 -- ENTITY INVENTORY AND ROLE CATALOG

**1.1 -- Entity catalog:**

List every entity that {{topic}} creates, reads, updates, or deletes.

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

Sensitivity: High (PII, financial, credentials, health data) / Medium (internal-only, cross-BU risk) / Low (lookup, reference, configuration).

**1.2 -- Role catalog:**

List every security role with any privilege in this scenario, including read-only.

| Role | Type (Stock / Custom) | Primary Persona |
|------|-----------------------|-----------------|

Stock roles to check for presence: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 -- Entity analysis order:**

Reorder entities from 1.1 by sensitivity (highest first). State: "I will trace entities in this order: [list]. I will add to the Running Gap Register at the end of each entity section before proceeding to the next."

---

## PHASE 2 -- PER-ENTITY TRACE WITH INLINE GAP TALLY

**Instruction: Complete all sub-steps for one entity, then write the ENTITY GAP TALLY for that entity, then advance to the next entity. Do not write all entity traces and then tally all at once.**

---

### Entity: [name] (Sensitivity: [rating])

**2a -- Operation-role matrix:**

| Role | Create | Read | Write | Delete | Assign | Record Scope |
|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Parent-Child BU / Team / User / Sharing-[rule name]
Every role from 1.2 must appear. Do not combine roles.

**2b -- Field-level security:**

| Field | Sensitivity | FLS Profile | Read: Allowed | Write: Allowed | Denied |
|-------|-------------|-------------|---------------|----------------|--------|

Rules:
- Every sensitive field (PII, Financial, Health, Credential, Internal-Audit) must have a row
- FLS Profile = NONE: state this explicitly per field; do not use blanket "FLS not configured"
- Denied column must be filled -- "none denied" requires explicit confirmation

**2c -- Sharing rule audit:**

| Rule Name | Trigger | Access Granted | Recipient | Exceeds OWD+Role Intent? |
|-----------|---------|----------------|-----------|--------------------------|

If no rules exist: "Confirmed no sharing rules on [Entity]. Checked [location]."

**2d -- Team membership dependency:**

Does any role's access to this entity depend on team membership? If yes: name the team, the blocked scenario, who controls membership, whether self-addition is possible. If no: "Confirmed: [Entity] access does not depend on team membership. Checked: [what was checked]."

**2e -- Escalation path check (per role with Write):**

For each role with Write access to this entity:
- Check: Record Assign (transfer ownership to higher-privilege scope), Share (share to higher-privilege role), field modification (modify field affecting role or BU assignment)
- Escalation confirmed format: `[Role] -> [Write action on [Entity]] -> [elevated access reached]`
- Escalation ruled out format: "Checked [Role]: write on [specific fields/operations listed]. No escalation because [specific mechanism -- e.g., no sharing rule grants cross-BU, no team membership path to higher-privilege scope]."
- Every role with Write must have one of these two formats. No role may be skipped.

---

### ENTITY GAP TALLY: [Entity name] -- complete this before advancing to the next entity

Write one of the following for this entity:

**If gaps were found:** Add each gap as a row to the Running Gap Register at the top of the document. Then write here:
"Tally for [Entity]: [N] gap(s) added to register. Entries: [Gap # list]. Inline signals captured: YES."

**If no gaps were found:** Write:
"ENTITY CLEAR: [Entity] -- Checked: operations [list of operations reviewed], FLS on fields [list of sensitive fields reviewed by name], sharing rules [confirmed none / list reviewed], team dependency [confirmed none / noted]. No gaps found."

Do not write "reviewed all fields" or "no gaps found" without naming what was reviewed.

---

[Repeat Phase 2 template for each entity in order]

---

## PHASE 3 -- CROSS-ENTITY CASCADE

After all entity sections and their gap tallies are complete:

**3a -- Relationship map:**

For the two highest-sensitivity entities, map their relationships to other entities in scope:

| Source | Relationship Type | Target | Cascade Behavior |
|--------|-------------------|--------|-----------------|

Cascade behaviors: Parental (child records cascade delete and share) / Referential (FK link only) / None.

**3b -- Cascade access trace:**

For each relationship: trace whether access to the source entity creates unintended access to the target.

Format: `[Role] -> [Source, access level, scope] -> [Relationship + cascade] -> [Target, access level resulting]`

State at each hop: INTENTIONAL (explicitly configured) or EMERGENT (consequence of cascade).
If EMERGENT and access exceeds the role's direct grant: add to Running Gap Register.

**3b Gap Tally:** After cascade trace, add a tally entry for any cascade gaps found.

---

## PHASE 4 -- REMEDIATION AND DEFENSE-IN-DEPTH

**4a -- Gap remediation:**

For each row in the Running Gap Register:

`[Gap #]: Apply [specific change] to [role / FLS profile / sharing rule / OWD / team config] in [solution location]. Current state: [what exists]. Target state: [what it should be]. After fix: [what a user can / cannot do].`

Generic advice ("review permissions") does not qualify. Each fix must be implementable by a Dataverse administrator reading only this output.

**4b -- Defense-in-depth assessment:**

For each entity:

| Entity | Security Role: Independent? | FLS: Independent? | Record Scope: Independent? | Single Point of Failure? |
|--------|---------------------------|-------------------|---------------------------|-------------------------|

"Independent?" = YES if bypassing the other two layers still leaves this layer enforcing access control. NO if this layer's protection collapses when another layer is misconfigured.

**4c -- Stock role summary:**

For each Dataverse stock role present (Customer Service Representative, Basic User, System Customizer, System Administrator): state whether its baseline privileges were strengthened, weakened, or unchanged for {{topic}}, and whether its presence is necessary.

---

## OUTPUT REQUIREMENTS

- Entities must appear in sensitivity order throughout
- The Running Gap Register must be populated inline -- not retroactively filled at the end
- Every entity must have an ENTITY GAP TALLY block before the next entity begins
- ENTITY CLEAR entries must name specific fields and operations checked
- Every role with Write access must have an escalation verdict (confirmed or ruled out with named evidence)

---

## V-02 -- Role Sequence: Full-Verdict Per-Role Escalation Spine

**Axis:** Role sequence (output organized role-first, with each role section closing on a mandatory ESCALATION VERDICT block)
**Hypothesis:** Entity-first organization allows the model to defer escalation analysis to a separate phase where it is treated as optional. Role-first organization -- where each role's complete picture across all entities is traced before moving to the next role -- forces an escalation verdict at the natural close of each role section. The verdict must name what was checked across all entities and state the specific mechanism preventing (or enabling) escalation. This makes C-11 structurally unavoidable.

---

You are running a permissions trace signal for: {{topic}}

---

**SECURITY GAP REGISTER -- add rows as gaps are found throughout the trace.**

| # | Role | Entity / Field | Gap Type | Risk | Fix |
|---|------|----------------|----------|------|-----|

---

## PHASE 1 -- INVENTORY

**1.1 -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason |
|--------|-----------------|-------------|--------|

**1.2 -- Role catalog:**

List every role with any privilege in this scenario.

| Role | Type | Persona | Has Write Access? |
|------|------|---------|------------------|

Mark every role with write access -- these roles require a full escalation verdict in Phase 2.
Stock roles to check: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 -- Role analysis order:**

Process roles in this order:
1. Roles with Write access to highest-sensitivity entities (highest risk first)
2. Roles with Read-only access to high-sensitivity entities
3. Roles touching only medium/low sensitivity entities

State your order: "I will trace roles in this order: [list with reason for order]."

---

## PHASE 2 -- PER-ROLE TRACE

**Instruction: Complete all sub-steps for one role across all entities it touches, then write the ROLE ESCALATION VERDICT before advancing to the next role.**

---

### Role: [name] (Persona: [job function] | Has Write: [YES/NO])

**2a -- What this role can do (across all entities):**

| Entity | Create | Read | Write | Delete | Assign | Record Scope |
|--------|--------|------|-------|--------|--------|--------------|

Every entity from 1.1 where this role holds any privilege. "No access" entities may be omitted but must be confirmed: "No access on [Entity list] -- confirmed."

**2b -- What sensitive fields this role can see:**

For each entity where this role has Read:

| Entity | Field | Sensitivity | FLS Profile | Can This Role Read? | Can This Role Write? |
|--------|-------|-------------|-------------|---------------------|---------------------|

Rule: A sensitive field with no FLS profile is readable by any role with entity-level Read. If this role can read a PII/Credential/Health field with no FLS profile: add to Security Gap Register now. Gap Type = MISSING-FLS. Risk = CRITICAL.

**2c -- Sharing rules that expand this role's access:**

For each entity: does any sharing rule expand this role's record access beyond what the OWD + security role privilege would otherwise permit? If yes:
- Name the rule, the trigger, and what records become accessible
- Add to Security Gap Register if expansion is beyond design intent. Gap Type = SHARING-CONFLICT.

If no expansion: "Confirmed: no sharing rules expand [Role] access on [Entity list]."

**2d -- Team membership dependencies for this role:**

Does this role have any access that depends on team membership? If yes: name the team, the access it grants, who controls membership, and whether a user in this role can manipulate their own team membership. If no: "Confirmed: [Role] access does not depend on team membership."

---

### ROLE ESCALATION VERDICT: [Role name]

Write this block for every role before advancing to the next role. This block is mandatory.

**If this role has Write access (marked in 1.2):**

Step through each escalation vector below and give an explicit verdict for each:

| Vector | Operations Checked | Verdict | Evidence |
|--------|-------------------|---------|----------|
| Record Assign | [what Assign privileges this role holds, if any] | ESCALATION POSSIBLE / NOT POSSIBLE | [specific reason: e.g., BU scope limits Assign to own records; no cross-BU OWD exception] |
| Share to higher-privilege role | [can this role share records to a higher-privilege group] | ESCALATION POSSIBLE / NOT POSSIBLE | [specific reason] |
| Field modification affecting role/BU | [can this role write fields that control security role assignment or BU membership] | ESCALATION POSSIBLE / NOT POSSIBLE | [specific reason] |
| Team self-addition | [can this role add itself to a team that grants higher privilege] | ESCALATION POSSIBLE / NOT POSSIBLE | [specific reason] |

If any vector shows ESCALATION POSSIBLE: add to Security Gap Register. Gap Type = ESCALATION-PATH. Risk = CRITICAL or HIGH.

**Rule-out summary (required even if no escalation found):**

Write: "Checked [Role]: Write on [list every operation and entity the Write covers]. Vectors checked: [Assign / Share / Field modification / Team self-addition]. No escalation because [state the specific mechanism that closes each vector -- e.g., "Assign is BU-scope only and OWD = Business Unit, so records assigned to this role's scope stay within BU; sharing rule does not exist that bridges to higher-privilege scope; no field on [Entity] governs role assignment or BU; team membership is controlled by System Administrator only."]. VERDICT: [ESCALATION POSSIBLE (see Gap Register) / NO ESCALATION PATH]."

**If this role has NO Write access:**

Write: "Checked [Role]: Read-only on [entity list, operations listed]. No Write access confirmed. Escalation requires Write or Assign privilege -- neither held. VERDICT: NO ESCALATION PATH because read-only access on all entities in scope."

---

[Repeat Phase 2 template for each role in order]

---

## PHASE 3 -- CROSS-ENTITY AND AGGREGATE ANALYSIS

**3a -- Cross-entity cascade:**

For the two highest-sensitivity entities: trace relationship hops.

`[Role] -> [Entity A, access level] -> [Relationship + cascade behavior] -> [Entity B, access level resulting]`

For each hop: INTENTIONAL (explicitly configured) or EMERGENT. EMERGENT access exceeding the role's direct grant: add to Security Gap Register. Gap Type = CASCADE-OVERREACH.

**3b -- Least-privilege scoring:**

| Role | Persona Need | Privileges Beyond Need | LP Score (10 = exact, 7-9 = minor excess, 4-6 = moderate, 0-3 = significant) |
|------|-------------|----------------------|-------------------------------------------------------------------------------|

For any role with LP Score < 7: name the specific privilege to reduce and the target scope.

---

## PHASE 4 -- REMEDIATION

**4a -- Gap remediation:**

For each row in the Security Gap Register:

`[Gap #]: Change [privilege / FLS profile / sharing rule / OWD / team config] on [entity/field/role] from [current state] to [target state] in [solution location]. After fix: [what the role can / cannot do that it currently can / cannot].`

**4b -- Defense-in-depth:**

| Entity | Security Role: Independent? | FLS: Independent? | Record Scope: Independent? | Single Point of Failure? |
|--------|---------------------------|-------------------|---------------------------|-------------------------|

**4c -- Stock role coverage:**

Customer Service Representative: baseline privilege set for {{topic}}, whether custom config strengthened or weakened the baseline, whether presence is necessary.
[Repeat for each stock role present]

---

## OUTPUT REQUIREMENTS

- Roles must be processed in the order stated in 1.3 -- no interleaving
- Every role section must close with a ROLE ESCALATION VERDICT block before the next role begins
- Write-access roles must list every escalation vector and give an explicit verdict per vector
- Read-only roles must receive an explicit "no escalation because read-only" verdict
- Generic verdicts ("access appears appropriate") do not pass -- every verdict requires named operations and named mechanisms

---

## V-03 -- Lifecycle Emphasis: Named Inventory Gate with Per-Entity FLS Confirmation

**Axis:** Lifecycle emphasis (a mandatory named PHASE GATE between inventory and gap analysis; the gate is a structured table the model must complete, not a prose declaration)
**Hypothesis:** The most common failure mode for C-12 is the implicit phase transition: the model finishes an operation matrix and immediately begins producing analysis without confirming inventory is complete. A structured gate table that must list every entity by name, confirm FLS coverage per entity, and state scope decisions makes the completeness assertion required by C-12 structurally unavoidable. Implicit "all reviewed" prose cannot satisfy the gate.

---

You are running a permissions trace signal for: {{topic}}

---

**MASTER GAP TABLE -- do not fill this now. Add rows throughout the trace.**

| # | Phase | Entity | Detail | Gap Type | Severity | Fix |
|---|-------|--------|--------|----------|----------|-----|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH

---

## PHASE 1 -- COMPLETE INVENTORY

You are a Dataverse security architect. Build the full security inventory before any analysis begins.

**1.1 -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason |
|--------|-----------------|-------------|--------|

List every entity {{topic}} creates, reads, updates, or deletes.

**1.2 -- Role catalog:**

| Role | Type (Stock / Custom) | Persona | Has Write? |
|------|-----------------------|---------|------------|

Stock roles to check: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 -- Operation-role matrix:**

One table per entity:

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|--------|------|-------|--------|--------|--------------|

Every role from 1.2 must appear for every entity where it holds any privilege.

**1.4 -- Field-level security inventory:**

One table per entity:

| Entity | Field | Sensitivity | FLS Profile Name | Read: Roles | Write: Roles | Denied: Roles |
|--------|-------|-------------|-----------------|-------------|--------------|---------------|

Rules:
- Every sensitive field (PII, Financial, Health, Credential, Internal-Audit) must have a row
- FLS Profile Name = NONE: mark the row [MISSING-FLS] and add to Master Gap Table immediately
- "No sensitive fields" requires: "Entity [name] -- no sensitive fields. Fields reviewed: [list every field reviewed by name]"

**1.5 -- Sharing rule inventory:**

| Entity | Rule Name | Trigger | Access Granted | Recipient | Exceeds Intent? |
|--------|-----------|---------|----------------|-----------|----------------|

No rules: "Confirmed no sharing rules on [Entity] -- checked [location]. Zero rules found."

---

## *** PHASE GATE: INVENTORY COMPLETE? ***

**Complete this gate before proceeding to Phase 2. Do not advance until every answer is YES or N/A.**

| Check | Entity / Field / Role Named | Answer |
|-------|----------------------------|--------|
| All entities in 1.1 | [list every entity name from 1.1] | YES / NO |
| All roles in 1.2 | [list every role name from 1.2] | YES / NO |
| Every role-entity pair in 1.3 matrix | [confirm table is populated for all pairs] | YES / NO |
| Every sensitive field in 1.4 FLS table | [list every sensitive field by entity and field name] | YES / NO |
| Every MISSING-FLS row added to Master Gap Table | [list gap numbers assigned, or N/A] | YES / N/A |
| Sharing rules confirmed for every entity | [list entities confirmed, including "no rules" confirmations] | YES / NO |
| Stock roles (CS Rep, Basic User, etc.) addressed | [list stock roles present or confirmed absent] | YES / NO |

**Scope decisions:**

State any entities, roles, or fields that are out of scope and why: "[Entity / Field / Role] is out of scope because [reason]."
If everything is in scope: "No scope exclusions. All entities in 1.1 are in scope for full analysis."

**PHASE GATE VERDICT:** INVENTORY COMPLETE: [YES -- proceed to Phase 2 / NO -- return to Phase 1 and complete: [specific items]]

*If NO: do not proceed until the gate reaches YES.*

---

## PHASE 2 -- GAP ANALYSIS

**2.1 -- Privilege escalation analysis:**

For each role in 1.2:
- If escalation vector exists: `[Role] -> [Write action on [Entity]] -> [elevated access reached]`. Add to Master Gap Table.
- Rule-out format (required for every role): "Checked [Role]: holds Write on [list operations and entities]. No escalation because [specific mechanism: OWD behavior, absence of sharing rule, team membership control, no field governs role/BU assignment]. VERDICT: NO ESCALATION PATH."

Every role must have one of: escalation path chain OR rule-out statement. A verdict without named operations does not satisfy this requirement.

**2.2 -- Business unit scope analysis:**

For each role with BU or Parent-Child BU scope:

`[Role] -> [BU scope from 1.3] -> [OWD behavior] -> [child BU records: accessible YES/NO] -> [reason]`

**2.3 -- Team membership gap analysis:**

For each team-dependent configuration: "Users in [Role] not in [Team] cannot access [record type] because [OWD + scope]. Team membership controlled by [mechanism]. Self-addition is [possible / not possible] because [reason]."

**2.4 -- Cross-entity cascade:**

For the highest-sensitivity entity, trace at least two relationship hops:

`[Role] -> [Entity A, operation, scope] -> [Relationship + cascade] -> [Entity B, operation resulting] -> [Relationship + cascade] -> [Entity C, operation resulting]`

Each hop: INTENTIONAL (explicitly configured) or EMERGENT. EMERGENT access exceeding direct grant: add to Master Gap Table. Gap Type = CASCADE-OVERREACH.

---

## *** PHASE GATE: GAP ANALYSIS COMPLETE? ***

**Complete this gate before proceeding to Phase 3.**

| Check | Evidence | Answer |
|-------|----------|--------|
| Every role has an escalation verdict (confirmed or ruled out with named operations) | [list roles and their verdict: ESCALATION POSSIBLE / NO ESCALATION PATH] | YES / NO |
| Every BU-scoped role has a concrete parent-child access path shown | [list roles with BU scope] | YES / NO |
| Team membership gaps identified or confirmed absent | [list teams checked] | YES / NO |
| Cascade trace covers at least two hops from highest-sensitivity entity | [name entities in cascade chain] | YES / NO |
| All new gaps found in Phase 2 added to Master Gap Table | [list gap numbers added in this phase, or "none found"] | YES / NO |

**PHASE GATE VERDICT:** GAP ANALYSIS COMPLETE: [YES -- proceed to Phase 3 / NO -- return to Phase 2 and complete: [specific items]]

---

## PHASE 3 -- ASSESSMENT AND REMEDIATION

**3.1 -- Least-privilege scoring:**

| Role | Persona | Privileges Beyond Need | LP Score | Status |
|------|---------|----------------------|----------|--------|

LP Score: 10 = exact least-privilege. 7-9 = minor excess. 4-6 = moderate. 0-3 = significant.

**3.2 -- Defense-in-depth:**

| Entity | Security Role: Independent? | FLS: Independent? | Record Scope: Independent? | Single Point of Failure? |
|--------|---------------------------|-------------------|---------------------------|-------------------------|

"Independent?" = YES if this layer enforces access even if the other two layers are misconfigured. For any Single Point of Failure = YES: add to Master Gap Table. Gap Type = SINGLE-LAYER-FAILURE.

**3.3 -- Gap remediation:**

For each row in the Master Gap Table:

`[Gap #]: Change [privilege / FLS profile / sharing rule / OWD / team config] on [entity/field/role] from [current state] to [target state] in [solution location]. After fix: [what a user can or cannot do].`

**3.4 -- Stock role coverage:**

Customer Service Representative and any other stock roles: baseline privileges for {{topic}}, whether custom config modified the baseline, whether presence is necessary.

---

## *** PHASE GATE: ANALYSIS COMPLETE? ***

| Check | Answer |
|-------|--------|
| Every role has an LP score | YES / NO |
| Every entity has a defense-in-depth row | YES / NO |
| Every row in the Master Gap Table has a remediation entry | YES / NO |
| Customer Service Representative addressed | YES / NO |

**ANALYSIS COMPLETE: [YES / NO]**

---

## OUTPUT REQUIREMENTS

- The two PHASE GATE tables are mandatory -- they cannot be replaced by prose summaries
- Every gate check must name the entities, fields, or roles it covers -- "all reviewed" without names fails the gate
- Phase 2 may not begin until the first PHASE GATE is complete (VERDICT = YES)
- Phase 3 may not begin until the second PHASE GATE is complete (VERDICT = YES)
- Gap entries added during Phase 1 (MISSING-FLS) must appear in the Master Gap Table before the first gate is written

---

## V-04 -- Combined: Inline Gap Stream + Gate Checkpoint

**Axis:** Output format (inline gap accumulation) + lifecycle emphasis (gate-then-proceed checkpoint that audits the gap stream)
**Hypothesis:** The inline gap stream (C-10) and the phase-gate checkpoint (C-12) are mutually reinforcing. Gaps discovered during entity traversal flow into the gap stream; the gate requires the model to enumerate all stream entries and confirm no inline signals were missed or collapsed. The gate cannot pass unless the stream was actively maintained. This combination closes both failure modes simultaneously: gap collapse (C-10 failure) and implicit phase transition (C-12 failure).

---

You are running a permissions trace signal for: {{topic}}

---

**INLINE GAP STREAM -- open throughout the entire trace. Add entries the moment gaps are found.**

Each entry format:
`[G-##] [Entity].[Field / Operation] -- [Role(s)] -- [Gap Type] -- Risk: [CRITICAL/HIGH/MEDIUM] -- Fix: [specific action]`

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH / SINGLE-LAYER-FAILURE

This stream is your working log. Add entries here immediately when discovered. Do not defer to the end.

---

## PHASE 1 -- INVENTORY

**1.1 -- Entity catalog with OWD and sensitivity:**

| Entity | OWD | Sensitivity | Reason |
|--------|-----|-------------|--------|

**1.2 -- Role catalog:**

| Role | Type | Persona | Write Access Entities |
|------|------|---------|----------------------|

Stock roles to check: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 -- Operation-role matrix (per entity):**

| Entity: [name] | Role | C | R | W | D | A | Record Scope |
|----------------|------|---|---|---|---|---|--------------|

One table per entity. Every role with any privilege on this entity must appear.

**1.4 -- Field-level security (per entity):**

For each entity, for each sensitive field:

| Field | Sensitivity | FLS Profile | Read: Who | Write: Who | Denied: Who |
|-------|-------------|-------------|-----------|------------|-------------|

Rule: FLS Profile = NONE on a sensitive field means every role with entity-level Read can see it.
Action: Add to Inline Gap Stream immediately: `[G-##] [Entity].[Field] -- All roles with Read -- MISSING-FLS -- Risk: CRITICAL (PII/Credential/Health) or HIGH (Financial/Internal-Audit) -- Fix: Create field security profile "[Entity]-[Field]-Restricted" in Settings > Security > Field Security Profiles. Grant Read to [roles requiring it]. Deny all others.`

**1.5 -- Sharing rules (per entity):**

| Entity | Rule | Trigger | Access | Recipient | Beyond Intent? |
|--------|------|---------|--------|-----------|----------------|

Rules beyond intent: add to Inline Gap Stream immediately. `[G-##] [Entity] -- [Role(s) over-exposed] -- SHARING-CONFLICT -- Risk: HIGH -- Fix: [specific rule restriction]`

---

## *** PHASE 1 GATE ***

**Complete before proceeding to Phase 2.**

**Part A -- Inventory coverage confirmation:**

| Covered | Names |
|---------|-------|
| Entities in scope | [list every entity name] |
| Roles in scope | [list every role name] |
| Sensitive fields confirmed per entity | [list: Entity: [fields reviewed]] |
| Sharing rules audited per entity | [list: Entity: [rule names or "confirmed none"]] |
| Scope decisions | [entities/fields/roles excluded and why, or "no exclusions"] |

**Part B -- Inline Gap Stream audit at Phase 1:**

| Gap ID | Type | Added During | Status |
|--------|------|--------------|--------|
| [list every G-## entry added so far] | | [1.4 / 1.5 / etc.] | Open |

"Gap stream entries at Phase 1 close: [N] entries. Confirm: all MISSING-FLS and SHARING-CONFLICT signals from Phase 1 are recorded in the stream."

**PHASE 1 GATE VERDICT:** INVENTORY COMPLETE -- Gap stream has [N] entries -- PROCEED TO PHASE 2: [YES / NO]

---

## PHASE 2 -- GAP ANALYSIS

**2.1 -- Escalation analysis (per role):**

For each role with Write access:
- Escalation confirmed: `[Role] -> [Write on Entity] -> [elevated access]`. Add to Inline Gap Stream: `[G-##] [Entity] -- [Role] -- ESCALATION-PATH -- Risk: CRITICAL -- Fix: [specific privilege reduction]`
- Escalation ruled out: "Checked [Role]: Write on [operations listed]. Vectors: Assign [verdict + reason], Share [verdict + reason], Field modification affecting role/BU [verdict + reason], Team self-addition [verdict + reason]. VERDICT: NO ESCALATION PATH because [specific mechanism]."

For each role WITHOUT Write access: "Checked [Role]: Read-only on [entities]. No Write, no Assign, no escalation vector. VERDICT: NO ESCALATION PATH."

**2.2 -- BU scope analysis:**

For each BU-scoped role: `[Role] -> [BU scope] -> [OWD] -> [child records: accessible YES/NO] -> [reason]`

**2.3 -- Team gap analysis:**

For each team-dependent configuration: "Users in [Role] not in [Team] cannot access [record type] because [OWD + scope]. Team controlled by [mechanism]. Self-addition: [possible / not possible -- reason]."

**2.4 -- Cross-entity cascade:**

From highest-sensitivity entity, two hops minimum:
`[Role] -> [Entity A, level, scope] -> [Relationship + cascade] -> [Entity B, level resulting] -> [Relationship + cascade] -> [Entity C, level resulting]`

Per hop: INTENTIONAL or EMERGENT. EMERGENT over-access: add to Inline Gap Stream.

---

## *** PHASE 2 GATE ***

**Complete before proceeding to Phase 3.**

**Part A -- Analysis coverage confirmation:**

| Covered | Evidence |
|---------|----------|
| Every role has an escalation verdict | [list roles + VERDICT for each] |
| Every BU-scoped role has a concrete path | [list roles + path summary] |
| Team gaps identified or confirmed absent | [list teams checked] |
| Cascade covers 2+ hops from highest-sensitivity entity | [entity chain: A -> B -> C] |

**Part B -- Inline Gap Stream audit at Phase 2:**

| Gap ID | Type | Phase Added | Status |
|--------|------|-------------|--------|
| [list all G-## entries, including those added in Phase 2] | | | Open |

"Gap stream entries at Phase 2 close: [N] total. Phase 2 additions: [N new entries]. All escalation paths and cascade overreach signals captured: [YES / NO -- if NO, add missing entries now]."

**PHASE 2 GATE VERDICT:** GAP ANALYSIS COMPLETE -- Gap stream has [N] total entries -- PROCEED TO PHASE 3: [YES / NO]

---

## PHASE 3 -- REMEDIATION AND ASSESSMENT

**3.1 -- Remediation for every gap in the Inline Gap Stream:**

For each G-## entry:

`[G-##]: Change [privilege / FLS profile / sharing rule / OWD / team config] from [current state] to [target state] in [solution location]. After fix: [what changes for the affected role].`

The Fix field in the stream is your starting point -- expand it here with current/target/after.

**3.2 -- Defense-in-depth:**

| Entity | Security Role: Independent? | FLS: Independent? | Record Scope: Independent? | Single Point of Failure? |
|--------|---------------------------|-------------------|---------------------------|-------------------------|

Single Point of Failure = YES: add to Inline Gap Stream. Gap Type = SINGLE-LAYER-FAILURE.

**3.3 -- LP scoring:**

| Role | Privileges Beyond Need | LP Score (10 = exact) |
|------|----------------------|----------------------|

LP Score < 7: state specific privilege to reduce and target scope.

**3.4 -- Stock role coverage:**

Customer Service Representative: baseline for {{topic}}, whether modified, whether necessary.

---

## *** FINAL GATE ***

| Check | Answer |
|-------|--------|
| Every G-## entry has a remediation entry in 3.1 | YES / NO |
| Every entity has a defense-in-depth row | YES / NO |
| Every role has an LP score | YES / NO |
| Inline Gap Stream entry count matches remediation count | [stream count] = [remediation count]: YES / NO |

**ANALYSIS COMPLETE: [YES / NO]**

---

## OUTPUT REQUIREMENTS

- Inline Gap Stream must be populated during the trace -- pre-populating at the end fails C-10
- Phase 1 Gate and Phase 2 Gate are mandatory sections -- cannot be collapsed or omitted
- Each gate Part B must enumerate every stream entry by ID -- "all gaps captured" without IDs fails C-12
- Every role (Write-access and Read-only) must have an explicit escalation verdict in 2.1

---

## V-05 -- Combined: Verdict-Per-Role Discipline + Dataverse Stock Defaults as Baseline

**Axis:** Phrasing register (imperative verdict discipline -- every role interaction with every escalation vector closes with an explicit verdict statement) + inertia framing (Dataverse stock default is named first in every access comparison, making "deviation from default" the primary output type)
**Hypothesis:** Naming the Dataverse stock default before every configured state makes the model's job comparative rather than descriptive: "Dataverse ships [X] by default; this system has configured [Y]; the delta is [Z]." This framing naturally surfaces C-10 gaps as deviations from safe defaults. The verdict-per-role discipline for escalation forces C-11: every role examined gets an explicit closed-case statement, not just the roles where escalation was found. The combination produces a trace that is structured around violations of expected defaults and closed verdicts on every role examined.

---

You are running a permissions trace signal for: {{topic}}

---

**DEVIATION LOG -- add entries when configured access deviates from Dataverse stock defaults in a security-relevant way.**

| # | Entity | Field / Role | Default Behavior | Configured Behavior | Risk Direction | Gap? |
|---|--------|-------------|-----------------|---------------------|----------------|------|

Risk direction: HARDENED (configured is more restrictive than default) / LOOSENED (configured is less restrictive) / NEUTRAL (changed but equivalent security)
Gap? = YES if LOOSENED and the loosening creates a security concern. Add to Gap Register if YES.

**GAP REGISTER -- add entries as gaps are found.**

| # | Entity | Detail | Gap Type | Risk | Fix |
|---|--------|--------|----------|------|-----|

---

## PHASE 1 -- INVENTORY WITH DEFAULT BASELINES

**1.1 -- Entity catalog with default OWD:**

| Entity | Dataverse Default OWD | Configured OWD | Delta | Reason for Delta |
|--------|----------------------|----------------|-------|-----------------|

Dataverse default OWDs: most entities default to Organization (Public); some to Business Unit. State which default applies. If Configured OWD is more restrictive than default: note as HARDENED. If less restrictive: note as LOOSENED and add to Deviation Log.

**1.2 -- Role catalog with stock baseline:**

For each role, state the Dataverse stock baseline first, then what was configured:

| Role | Stock Baseline Privileges | Configured Privileges | Delta Type | Security Implication |
|------|--------------------------|----------------------|------------|---------------------|

For stock roles (Customer Service Representative, Basic User, System Customizer, System Administrator): the stock baseline is well-defined by Dataverse. State it explicitly. Delta Type: HARDENED / LOOSENED / UNCHANGED. If LOOSENED: add to Deviation Log.

For custom roles: State "Custom role -- no stock baseline. Designed access: [what was designed]. Minimum-necessary assessment: [privileges appear necessary / excess privileges: specify]."

**1.3 -- Operation-role matrix with default comparison:**

For each entity, for each role:

| Role | Default C/R/W/D/A | Configured C/R/W/D/A | Record Scope (Default) | Record Scope (Configured) | Delta |
|------|-------------------|---------------------|------------------------|--------------------------|-------|

"Default" = what Dataverse's stock role would have on a new environment. "Configured" = what this scenario has. Delta = HARDENED / LOOSENED / SAME. LOOSENED entries: note whether the loosening is security-relevant.

**1.4 -- Field-level security with default comparison:**

Dataverse default for all fields: no FLS profile applied (all fields visible to any role with entity-level Read).

For each sensitive field:

| Entity | Field | Sensitivity | Default Access | Configured (FLS Profile?) | Delta | Security State |
|--------|-------|-------------|---------------|--------------------------|-------|----------------|

Security State: PROTECTED (FLS profile restricts access -- improved over default) / UNPROTECTED (no FLS profile -- at Dataverse default -- may be a gap for sensitive fields).

For every UNPROTECTED sensitive field: add to Deviation Log (Risk Direction = NEUTRAL -- at default, but default is insufficient for this sensitivity) AND add to Gap Register. `[G-##] [Entity].[Field] -- MISSING-FLS -- Risk: CRITICAL/HIGH -- Fix: Create FLS profile "[name]" restricting Read/Write to [named roles only].`

**1.5 -- Sharing rules:**

Dataverse default: no sharing rules (records follow OWD + role scope only).

| Entity | Rule | Trigger | Access Granted | vs. Default (adds access beyond OWD+role) | Intentional? |
|--------|------|---------|----------------|------------------------------------------|-------------|

Every sharing rule adds access beyond default. State whether the addition is intentional and scoped. If unintentional or over-broad: add to Deviation Log (LOOSENED) and Gap Register.

---

## PHASE 2 -- ESCALATION ANALYSIS WITH CLOSED-CASE VERDICTS

**Instruction: Every role in the 1.2 catalog must receive a closed-case verdict before Phase 2 is complete. Write-access roles receive full vector analysis. Read-only roles receive a brief confirmation. No role may be left without a verdict.**

---

### Role: [name]

**Write-access roles -- full vector analysis:**

For each escalation vector:

`I checked [Role]'s ability to escalate via [vector]. The stock [Role / "Custom role"] baseline [has / does not have] this vector. The configured state [has / does not have] this vector. Specifically: [Role] holds [operation on entity at scope]. For escalation to occur via this vector: [what would need to be true]. That condition is [MET / NOT MET] because [specific reason: OWD value, sharing rule absence, team membership control, field content]. VERDICT: [ESCALATION POSSIBLE -- path: ... / NO ESCALATION -- closed because ...]`

Vectors to check:
- Record Assign (transfer ownership to higher-privilege scope)
- Share (share record to higher-privilege role or group)
- Field modification affecting security role or BU assignment
- Team self-addition (add self to team granting higher privilege)

If any vector yields ESCALATION POSSIBLE: add to Gap Register. `[G-##] [Entity] -- [Role] -- ESCALATION-PATH -- Risk: CRITICAL -- Fix: [specific privilege change].`

**Closed-case summary (required for all roles):**

Write the following at the end of every role's escalation analysis, write-access or read-only:

"Checked [Role]: [operations held, entities covered]. Default baseline for this role [has / does not have] escalation vectors in this configuration. Vectors checked: [Assign, Share, Field modification, Team self-addition -- state YES/NO checked for each]. CLOSED CASE: [ESCALATION CONFIRMED -- see G-## / NO ESCALATION PATH -- all vectors closed because [specific named mechanisms]]."

---

**Read-only roles -- brief confirmation:**

"Checked [Role]: Read-only on [entities listed]. Operations held: [Read + any non-Write operations]. No Write, Assign, Share, or field-modification operations held. Escalation requires Write or Assign -- neither present. Stock baseline for [Role] [matches / does not match] configured state: [Delta]. CLOSED CASE: NO ESCALATION PATH -- read-only access on all entities."

---

## PHASE 3 -- DEVIATION SUMMARY AND GAP REMEDIATION

**3.1 -- Deviation log review:**

For each row in the Deviation Log:
- HARDENED entries: confirm the hardening is appropriate and does not block legitimate access
- LOOSENED entries: confirm whether a Gap Register entry was created; if no gap was created, explain why the loosening is acceptable
- NEUTRAL (at-default, insufficient) entries: confirm Gap Register entries exist for all unprotected sensitive fields

**3.2 -- Gap remediation:**

For each row in the Gap Register:

`[G-##]: [Entity].[Field/Role/Rule] -- Current state: [what the configured state is, vs. stock default]. Target state: [what it should be]. Change: [specific Dataverse admin action -- role privilege table, FLS profile creation, sharing rule edit, OWD setting, team configuration -- in named solution location]. After fix: [what a user can or cannot do that they currently can or cannot]. Why this matters vs. default: [how this brings the system to a more secure state than Dataverse default].`

**3.3 -- Defense-in-depth vs. default:**

| Entity | Default Defense-in-Depth | Configured Defense-in-Depth | Improvement or Regression? |
|--------|-------------------------|----------------------------|---------------------------|

Dataverse default defense-in-depth for most entities: security role only (OWD = Org, no FLS, no sharing rules). A well-configured system should add FLS and tighten OWD. State whether this scenario improves on the default, matches it, or regresses below it.

**3.4 -- Stock role final assessment:**

For each stock role present:

"[Role] in this scenario vs. Dataverse baseline: Baseline [X]. Configured [Y]. Delta: [HARDENED / LOOSENED / UNCHANGED]. Least-privilege assessment: [appropriate for the job / excess privileges: specify]. Recommendation: [keep as configured / reduce to: specific target]."

Customer Service Representative specifically: "The CS Representative's configured access [is / is not] consistent with the CS job function as defined by {{topic}}. The deviation from Dataverse default is [appropriate / over-loosened / over-hardened] because [reason]. Overall: [ACCEPTABLE / NEEDS REVIEW -- specific items]."

**3.5 -- LP scoring:**

| Role | Configured Access | Minimum Necessary | LP Score | Status |
|------|------------------|------------------|----------|--------|

---

## OUTPUT REQUIREMENTS

- Deviation Log must be populated inline -- add entries at the moment each entity, field, or role is analyzed
- Every role must have a CLOSED CASE statement in Phase 2 -- no role may be left without a verdict
- Write-access roles must show vector-by-vector analysis with each vector named and explicitly closed
- Read-only roles must receive the brief confirmation format -- silence is not acceptable
- Gap Register entries must precede the Phase 3 summary (gaps are found in Phases 1-2, remediated in Phase 3)
- The "Why this matters vs. default" field in 3.2 is mandatory -- generic remediation without baseline comparison does not pass
