# trace-permissions Variate -- Round 3 (Rubric v3)
**Date:** 2026-03-16
**Rubric:** v3 (C-01 through C-15)
**New criteria targeted this round:** C-13 (entity-level closure marker), C-14 (per-role sharing rule explicit verdict), C-15 (numbered gap identifiers enabling cross-reference)
**Prior round retained:** Essential C-01--C-04, recommended C-05--C-07, aspirational C-08--C-12 are structurally enforced throughout

---

## Round 3 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format -- numbered gap identifiers assigned at discovery (C-15 single-axis) | Requiring every gap to receive a sequential [G-##] identifier at the moment it is logged -- and requiring every downstream section (remediation, phase gate, defense-in-depth) to cite gaps by identifier rather than re-description -- makes the cross-reference chain structurally unavoidable; the prompt collapses if a gap is unnamed |
| V-02 | Lifecycle emphasis -- entity closure protocol (C-13 single-axis) | A mandatory ENTITY CLOSURE block at the end of every entity section -- naming (a) operations reviewed, (b) sensitive fields confirmed, (c) gaps tallied by ID -- forces explicit coverage confirmation at entity granularity; entities cannot advance until the block is written; implicit transitions fail the format requirement |
| V-03 | Role sequence -- per-role sharing verdict spine (C-14 single-axis) | Role-first organization where each role section closes on a mandatory SHARING RULE VERDICT block (naming the role, each entity checked, and the explicit verdict -- expansion found or confirmed none) makes C-14 structurally unavoidable; the verdict applies to every role regardless of whether conflicts were found |
| V-04 | Combined: output format (numbered IDs, C-15) + lifecycle emphasis (entity closure, C-13) | The entity closure block is the assignment point for gap IDs: each gap discovered during entity traversal is named and numbered in the closure block, then remediation cites IDs; linking ID assignment to the closure event forces both C-13 (closure before advancing) and C-15 (IDs at discovery, referenced downstream) in a single structural move |
| V-05 | Combined: phrasing register (explicit verdict vocabulary) + inertia framing (OWD + stock role baseline as null hypothesis) | Anchoring every sharing rule analysis to the Dataverse stock baseline -- stated before checking actual configuration -- forces a per-role verdict structure (C-14): "Baseline for [Role]: OWD=[value] + stock privilege, no rules. Actual: [checked]. Delta: [none / conflict G-##]." Gaps are deviations from baseline and receive IDs (C-15); baseline-first framing surfaces deviations naturally rather than requiring the model to generate conflict from nothing |

---

## V-01 -- Output Format: Numbered Gap Identifiers at Discovery

**Axis:** Output format (every gap assigned [G-##] at the moment of logging; all downstream sections reference by ID)
**Hypothesis:** Gap logs that use prose descriptions rather than identifiers force downstream sections to re-describe gaps rather than cite them. If the remediation section must say "the gap where CSR can read the SSN field because no FLS profile exists" rather than "G-03", the remediation is not cross-referencing the gap log -- it is re-creating it. Assigning sequential identifiers at discovery time, then requiring downstream sections to cite those identifiers, makes the gap log a referenceable artifact. Any remediation entry that re-describes instead of citing an ID signals that the gap log was created retrospectively.

---

You are running a permissions trace signal for: {{topic}}

---

**SECURITY GAP REGISTER -- assign [G-##] identifiers sequentially starting at G-01. Add rows as gaps are found. Never defer.**

| ID | Entity | Field / Operation | Role(s) | Gap Type | Risk | Status |
|----|--------|-------------------|---------|----------|------|--------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH
Risk: CRITICAL / HIGH / MEDIUM
Status: OPEN (fill now) -- remediation in Phase 4 will reference by ID

**Gap identifier rules:**
- Assign the next sequential ID ([G-01], [G-02], etc.) the moment a gap is identified during entity or field traversal
- Do not batch-assign IDs at the end of a phase
- If an entity is clean, write a CLEAR entry: "ENTITY CLEAR: [Entity]. Checked: [operations], [FLS fields by name], [sharing rules]. No gaps. Next ID will be: G-[N]."
- Every downstream reference to a gap must use its ID. Re-describing a gap in lieu of citing its ID is a format failure.

---

## PHASE 1 -- INVENTORY AND ANALYSIS ORDER

**1.1 -- Entity catalog:**

List every entity that {{topic}} creates, reads, updates, or deletes.

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

Sensitivity: High (PII, financial, credentials, health) / Medium (internal-only, cross-BU risk) / Low (lookup, reference, configuration)

**1.2 -- Role catalog:**

List every security role with any privilege in this scenario.

| Role | Type (Stock / Custom) | Persona | Has Write? |
|------|-----------------------|---------|------------|

Stock roles to check: Customer Service Representative, Basic User, System Customizer, System Administrator.
Mark every role with Write -- these require escalation verdicts in Phase 2.

**1.3 -- Analysis order declaration:**

Reorder entities from highest to lowest sensitivity. State: "I will trace entities in this order: [list]. The first gap ID I will assign is G-01."

---

## PHASE 2 -- PER-ENTITY TRACE

**Instruction: Complete all sub-steps for one entity, then advance to the next. The Running Gap Register must receive any new gaps before the entity section closes.**

---

### Entity: [name] (Sensitivity: [rating])

**2a -- Operation-role matrix:**

| Role | Create | Read | Write | Delete | Assign | Record Scope |
|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Parent-Child BU / Team / User / Sharing-[rule name]
Every role from 1.2 must appear. Do not combine roles.

**2b -- Field-level security:**

| Field | Sensitivity | FLS Profile | Read: Allowed Roles | Write: Allowed Roles | Denied Roles |
|-------|-------------|-------------|--------------------|--------------------|--------------|

Rules:
- Every sensitive field must have a row
- FLS Profile = NONE: state this explicitly per field -- do not use blanket "FLS not configured"
- If a sensitive field has no FLS profile: assign the next gap ID now. Log to Security Gap Register. Gap Type = MISSING-FLS. Risk = CRITICAL (PII/Credential/Health) or HIGH (Financial/Internal-Audit).
- Denied column: "none denied" requires explicit confirmation

**2c -- Sharing rule audit:**

| Rule Name | Trigger | Access Granted | Recipient Role | Verdict |
|-----------|---------|----------------|----------------|---------|

Verdict: EXPECTED / CONFLICT-[gap ID assigned]
- If conflict: assign next gap ID at this moment. Log to Security Gap Register. Gap Type = SHARING-CONFLICT.
- If no rules exist: "Confirmed no sharing rules on [Entity]. Checked [location]."
- For every role in 1.2: state the sharing rule verdict for this entity explicitly -- whether rules were found or not. "Confirmed: no sharing rules expand [Role] access on [Entity]." Silence is not acceptable.

**2d -- Team membership dependency:**

Does any role's access to this entity depend on team membership? If yes: name the team, the blocked scenario, who controls membership, whether self-addition is possible. Assign gap ID if self-addition is possible and unintended. If no: "Confirmed: [Entity] access does not depend on team membership. Checked: [what was checked]."

**2e -- Escalation path check:**

For each role with Write access to this entity:
- Check: Record Assign (transfer ownership to higher-privilege scope), Share (share to higher-privilege role), field modification (modify field affecting role or BU assignment)
- Escalation confirmed format: `[Role] -> [Write action on [Entity]] -> [elevated access reached]` -- assign gap ID, Gap Type = ESCALATION-PATH
- Escalation ruled out format: "Checked [Role]: write on [specific fields/operations listed]. No escalation because [specific mechanism named]."
- Every role with Write must receive one of these two formats. Assign gap IDs to confirmed escalation paths.

---

[Repeat Phase 2 for each entity in sensitivity order]

---

## PHASE 3 -- PHASE GATE: INVENTORY COMPLETENESS CHECK

Before proceeding to cross-entity cascade and gap analysis, complete this gate. Do not proceed until it is filled.

**Phase Gate Table:**

| Entity | Operations Covered | Sensitive Fields Confirmed by Name | Sharing Rules Checked | Gaps Found (IDs) | Scope Decision |
|--------|-------------------|-----------------------------------|-----------------------|------------------|----------------|

Rules:
- "Operations Covered" must list specific CRUD operations checked -- not "all operations"
- "Sensitive Fields Confirmed by Name" must name the fields -- not "all fields reviewed"
- "Gaps Found (IDs)" must list gap IDs -- or "NONE" confirmed explicitly
- "Scope Decision" states any entity excluded from scope and why

**Gate assertion:** "I confirm the following entities were fully inventoried before advancing to Phase 4: [entity list]. No inline gap signals were deferred. Open gaps: [list IDs or NONE]. I am proceeding to Phase 4."

---

## PHASE 4 -- CROSS-ENTITY CASCADE

**4a -- Relationship map:**

For the two highest-sensitivity entities:

| Source | Relationship Type | Target | Cascade Behavior |
|--------|-------------------|--------|-----------------|

**4b -- Cascade access trace:**

For each relationship: `[Role] -> [Source, access level, scope] -> [Relationship + cascade] -> [Target, access level resulting]`

State at each hop: INTENTIONAL or EMERGENT. If EMERGENT and exceeds direct grant: assign next gap ID, Gap Type = CASCADE-OVERREACH.

---

## PHASE 5 -- REMEDIATION AND DEFENSE-IN-DEPTH

**5a -- Gap remediation:**

For each row in the Security Gap Register, cite by ID:

`[G-##]: Apply [specific change] to [role / FLS profile / sharing rule / OWD / team config] in [solution location]. Current state: [what exists]. Target state: [what it should be]. After fix: [what a user can / cannot do].`

Requirements:
- Every row in the Security Gap Register must have a remediation entry here
- Reference by ID -- do not re-describe the gap instead of citing it
- Generic advice ("review permissions") does not qualify
- Each fix must be implementable by a Dataverse administrator reading only this output

**5b -- Defense-in-depth assessment:**

| Entity | Security Role: Independent? | FLS: Independent? | Record Scope: Independent? | Single Point of Failure? | Gaps Referenced |
|--------|---------------------------|-------------------|---------------------------|-------------------------|-----------------|

"Independent?" = YES if bypassing the other two layers still leaves this layer enforcing access control.
"Gaps Referenced" = list gap IDs that affect this entity's enforcement stack, or NONE.

**5c -- Stock role summary:**

For each Dataverse stock role present: state its baseline privilege set, whether custom configuration has strengthened or weakened its baseline, and whether its presence is necessary. Reference any gap IDs that implicate this role.

---

## OUTPUT REQUIREMENTS

- Every gap receives a sequential [G-##] identifier at the moment of discovery -- never retroactively
- Every downstream reference to a gap cites its ID -- re-description in lieu of ID citation is a format failure
- Every role in 2c must receive an explicit sharing rule verdict for each entity -- whether conflict was found or not
- Phase Gate in Phase 3 must be completed before Phase 4 begins -- implicit transitions do not satisfy the gate
- Every role with Write must have an escalation verdict (confirmed or ruled out with named evidence)

---

## V-02 -- Lifecycle Emphasis: Entity Closure Protocol

**Axis:** Lifecycle emphasis (mandatory ENTITY CLOSURE block at the end of every entity section, before the trace advances)
**Hypothesis:** Entity-first traces fail C-13 by flowing smoothly between entity sections without asserting what was covered. The model completes a trace of Entity A and begins Entity B without pausing to name what was reviewed in A, which fields were confirmed, and how many gaps were found. A mandatory ENTITY CLOSURE block -- structurally separate from the gap register and from inline analysis -- forces the model to stop at the entity boundary and confirm coverage before the section closes. The closure block is not a gap summary; it is a coverage assertion.

---

You are running a permissions trace signal for: {{topic}}

---

**SECURITY GAP REGISTER -- populate inline as gaps are found.**

| # | Entity | Field / Operation | Role(s) | Gap Type | Risk |
|---|--------|-------------------|---------|----------|------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH
Risk: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 -- INVENTORY

**1.1 -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

**1.2 -- Role catalog:**

| Role | Type (Stock / Custom) | Persona | Has Write? |
|------|-----------------------|---------|------------|

Stock roles to check: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 -- Entity analysis order:**

Reorder entities from highest to lowest sensitivity. State: "I will trace entities in this order: [list]. I will write an ENTITY CLOSURE block for each entity before advancing."

---

## PHASE 2 -- PER-ENTITY TRACE WITH MANDATORY CLOSURE

**Instruction: Complete all sub-steps for one entity, write the ENTITY CLOSURE block, then begin the next entity. The ENTITY CLOSURE block is a required format element -- the trace is not complete for an entity until the block is written.**

---

### Entity: [name] (Sensitivity: [rating])

**2a -- Operation-role matrix:**

| Role | Create | Read | Write | Delete | Assign | Record Scope |
|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Parent-Child BU / Team / User / Sharing-[rule name]
Every role from 1.2 must appear.

**2b -- Field-level security:**

| Field | Sensitivity | FLS Profile | Read: Allowed | Write: Allowed | Denied |
|-------|-------------|-------------|---------------|----------------|--------|

Rules:
- Every sensitive field must have a row
- FLS Profile = NONE: state this explicitly per field
- Sensitive field with no FLS profile: add to Security Gap Register now. Gap Type = MISSING-FLS.
- Denied column must be confirmed explicitly

**2c -- Sharing rule audit:**

| Rule Name | Trigger | Access Granted | Recipient | Exceeds OWD+Role Intent? |
|-----------|---------|----------------|-----------|--------------------------|

For each role with Read on this entity: state the sharing rule verdict explicitly -- whether rules were found or not. Format: "Checked sharing rules for [Role] on [Entity]: [rule found -- named / no rules found -- confirmed via [location]]."

**2d -- Team membership dependency:**

Does any role's access depend on team membership? If yes: name the team, blocked scenario, who controls membership, whether self-addition is possible. If no: "Confirmed: [Entity] access does not depend on team membership. Checked: [what was checked]."

**2e -- Escalation path check:**

For each role with Write access:
- Escalation confirmed: `[Role] -> [Write action] -> [elevated access reached]` -- add to Security Gap Register
- Escalation ruled out: "Checked [Role]: write on [specific fields/operations]. No escalation because [specific mechanism]."
- Every role with Write must receive one of these two formats.

---

### ENTITY CLOSURE: [Entity name]

**Write this block before advancing to the next entity. This block is a required format element.**

State all three elements:

**(a) Operations reviewed:**
"For [Entity], I reviewed the following operations: [Create / Read / Write / Delete / Assign -- list each CRUD operation explicitly with the roles checked for each]. I did not review: [any operations excluded from scope and why, or NONE excluded]."

**(b) Sensitive fields confirmed:**
"Sensitive fields on [Entity] confirmed: [list each sensitive field by name with its FLS status]. Fields with no FLS protection: [list names or NONE]. FLS coverage: [complete / gaps noted in register]."

**(c) Gaps tallied:**
"Gaps added to register during this entity section: [N]. Entries: [Gap # list -- or NONE]. Inline signals captured without deferral: YES."

Do not write "covered above" or "see gap register" in this block. The closure block must be self-contained.

---

[Repeat Phase 2 + ENTITY CLOSURE for each entity in sensitivity order]

---

## PHASE 3 -- PHASE GATE: INVENTORY COMPLETENESS

After all entity closure blocks are written, complete this gate before advancing.

**Gate table:**

| Entity | Closure Block Written? | Operations Reviewed (count) | Sensitive Fields Confirmed (count by name) | Gaps Found (N) | Status |
|--------|------------------------|---------------------------|-------------------------------------------|----------------|--------|

Gate assertion: "All [N] entity closure blocks are written. Total gaps in register: [N]. I am proceeding to Phase 4."

---

## PHASE 4 -- CROSS-ENTITY CASCADE

**4a -- Relationship map:**

For the two highest-sensitivity entities:

| Source | Relationship Type | Target | Cascade Behavior |
|--------|-------------------|--------|-----------------|

**4b -- Cascade access trace:**

For each relationship: `[Role] -> [Source, access level, scope] -> [Relationship + cascade] -> [Target, access level resulting]`

State at each hop: INTENTIONAL or EMERGENT. If EMERGENT and exceeds direct grant: add to Security Gap Register.

**4c -- Cascade closure:**

"Cascade trace complete. Additional gaps found: [N]. Entries: [Gap # list -- or NONE]."

---

## PHASE 5 -- REMEDIATION AND DEFENSE-IN-DEPTH

**5a -- Gap remediation:**

For each row in the Security Gap Register:

`[Gap #]: Apply [specific change] to [role / FLS profile / sharing rule / OWD / team config] in [solution location]. Current state: [what exists]. Target state: [what it should be]. After fix: [what a user can / cannot do].`

Generic advice does not qualify. Each fix must be implementable by a Dataverse administrator reading only this output.

**5b -- Defense-in-depth assessment:**

| Entity | Security Role: Independent? | FLS: Independent? | Record Scope: Independent? | Single Point of Failure? |
|--------|---------------------------|-------------------|---------------------------|-------------------------|

**5c -- Stock role summary:**

For each stock role present: baseline privileges, strengthened or weakened, necessary or removable.

---

## OUTPUT REQUIREMENTS

- Every entity section must have an ENTITY CLOSURE block written before the next entity begins
- The closure block must name (a) operations reviewed, (b) sensitive fields confirmed by name, (c) gaps tallied by count
- "Covered above" or "see gap register" in the closure block is a format failure -- the block must be self-contained
- Phase Gate in Phase 3 must reference every entity's closure block by name
- Every role with Write must have an escalation verdict
- Every role on every entity must receive an explicit sharing rule verdict

---

## V-03 -- Role Sequence: Per-Role Sharing Verdict Spine

**Axis:** Role sequence (role-first organization where each role section closes on a mandatory SHARING RULE VERDICT block)
**Hypothesis:** Entity-first organization places sharing rule analysis at the entity level, which makes it easy to document conflicts while leaving clean roles with no verdict. Role-first organization -- where each role's complete picture is traced across all entities before moving to the next role -- forces a sharing rule verdict at the natural close of each role section. The verdict must name every entity the role touches and state explicitly whether sharing rules expand that role's access or not. This makes C-14 structurally unavoidable: a role section cannot close without the verdict block, and the verdict block cannot omit any entity.

---

You are running a permissions trace signal for: {{topic}}

---

**SECURITY GAP REGISTER -- add rows as gaps are found.**

| # | Role | Entity / Field | Gap Type | Risk |
|---|------|----------------|----------|------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH
Risk: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 -- INVENTORY

**1.1 -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

**1.2 -- Role catalog:**

List every role with any privilege in this scenario.

| Role | Type (Stock / Custom) | Persona | Has Write? | Entities Touched |
|------|-----------------------|---------|------------|-----------------|

"Entities Touched" = list every entity where this role holds at least one privilege.
Stock roles to check: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 -- Role analysis order:**

Process roles in this order:
1. Roles with Write access to highest-sensitivity entities (highest risk first)
2. Roles with Read-only access to high-sensitivity entities
3. Roles touching only medium/low sensitivity entities

State: "I will trace roles in this order: [list with reason]. Each role section closes with a SHARING RULE VERDICT block before advancing."

---

## PHASE 2 -- PER-ROLE TRACE

**Instruction: Complete all sub-steps for one role across all entities it touches, then write the SHARING RULE VERDICT before advancing to the next role. The SHARING RULE VERDICT block is mandatory for every role.**

---

### Role: [name] (Persona: [job function] | Has Write: [YES/NO] | Entities: [list])

**2a -- What this role can do (across all entities):**

| Entity | Create | Read | Write | Delete | Assign | Record Scope |
|--------|--------|------|-------|--------|--------|--------------|

Every entity from 1.1 where this role holds any privilege. Entities with no access: "No access on [Entity list] -- confirmed."

**2b -- What sensitive fields this role can see:**

For each entity where this role has Read:

| Entity | Field | Sensitivity | FLS Profile | Can Read? | Can Write? |
|--------|-------|-------------|-------------|-----------|------------|

Rule: A sensitive field with no FLS profile is readable by any role with entity-level Read. If this role can read a PII/Credential/Health field with no FLS profile: add to Security Gap Register now. Gap Type = MISSING-FLS. Risk = CRITICAL.

**2c -- Team membership dependencies for this role:**

Does this role have access that depends on team membership? If yes: name the team, the access it grants, who controls membership, whether a user in this role can manipulate their own membership. If no: "Confirmed: [Role] access does not depend on team membership."

**2d -- Escalation path check for this role:**

**(Complete only if this role has Write access.)**

Step through each vector:

| Vector | Operations Checked | Verdict | Evidence |
|--------|-------------------|---------|----------|
| Record Assign | [Assign privileges this role holds] | POSSIBLE / NOT POSSIBLE | [specific reason] |
| Share to higher-privilege role | [sharing capability] | POSSIBLE / NOT POSSIBLE | [specific reason] |
| Field modification affecting role/BU | [field write capability] | POSSIBLE / NOT POSSIBLE | [specific reason] |
| Team self-addition | [team modification capability] | POSSIBLE / NOT POSSIBLE | [specific reason] |

If any vector shows POSSIBLE: add to Security Gap Register. Gap Type = ESCALATION-PATH.

If this role has no Write access: "Escalation check: [Role] has no Write access. No escalation vectors apply."

---

### SHARING RULE VERDICT: [Role name]

**Write this block for every role before advancing to the next role. This block is mandatory.**

For each entity this role touches (listed in 1.2 "Entities Touched"), state the sharing rule verdict explicitly:

| Entity | Sharing Rules Found? | Rule Name (if any) | Access Expanded Beyond OWD+Role? | Verdict |
|--------|---------------------|-------------------|----------------------------------|---------|

Verdict options:
- "Confirmed: no sharing rules expand [Role] access on [Entity]. Checked: [location / method]. Basis: OWD=[value], security role record scope=[scope]. No criteria-based or manual sharing applies."
- "CONFLICT FOUND: [Rule name] expands [Role] access on [Entity] to [record set]. Exceeds design intent because [reason]. Added to Security Gap Register as Gap #[N]. Gap Type = SHARING-CONFLICT."

**Rules:**
- Every entity in "Entities Touched" must appear in this table -- no entity may be omitted
- "No sharing rules configured" at the org level does not satisfy this block -- check must be per-entity per-role
- A verdict that names only conflicts while leaving clean entities with no entry fails this block

---

[Repeat Phase 2 + SHARING RULE VERDICT for each role in analysis order]

---

## PHASE 3 -- PHASE GATE: COVERAGE CHECK

Before advancing to cross-entity analysis:

**Gate table:**

| Role | Sharing Rule Verdict Written? | Entities Covered in Verdict | Escalation Verdict Written? | Gaps Found (N) |
|------|------------------------------|---------------------------|---------------------------|----------------|

Gate assertion: "All [N] role sections have SHARING RULE VERDICT blocks. All [M] roles with Write access have escalation verdicts. Total gaps in register: [N]. I am proceeding to Phase 4."

---

## PHASE 4 -- CROSS-ENTITY CASCADE

**4a -- Relationship map (entity-level, for two highest-sensitivity entities):**

| Source | Relationship Type | Target | Cascade Behavior |
|--------|-------------------|--------|-----------------|

**4b -- Cascade access trace:**

`[Role] -> [Source, access level, scope] -> [Relationship + cascade] -> [Target, access level resulting]`

State at each hop: INTENTIONAL or EMERGENT. If EMERGENT and access exceeds direct grant: add to Security Gap Register.

---

## PHASE 5 -- REMEDIATION AND DEFENSE-IN-DEPTH

**5a -- Gap remediation:**

For each row in the Security Gap Register:

`[Gap #]: Apply [specific change] to [role / FLS profile / sharing rule / OWD / team config] in [solution location]. Current state: [what exists]. Target state: [what it should be]. After fix: [what a user can / cannot do].`

Generic advice does not qualify.

**5b -- Defense-in-depth assessment:**

| Entity | Security Role: Independent? | FLS: Independent? | Record Scope: Independent? | Single Point of Failure? |
|--------|---------------------------|-------------------|---------------------------|-------------------------|

**5c -- Stock role summary:**

For each Dataverse stock role present: baseline privileges, strengthened or weakened, necessary or removable.

---

## OUTPUT REQUIREMENTS

- Every role section must close with a SHARING RULE VERDICT block before the next role begins
- The SHARING RULE VERDICT must cover every entity the role touches -- named individually, with an explicit verdict
- A verdict that names only conflicts while leaving clean entities without a statement fails this requirement
- Every role with Write must have a completed escalation table
- Phase Gate in Phase 3 must confirm all sharing rule verdicts before advancing
- Security Gap Register must be populated inline -- not retroactively

---

## V-04 -- Combined: Numbered Gap IDs (C-15) + Entity Closure Protocol (C-13)

**Axis:** Output format (numbered gap IDs assigned at discovery) + lifecycle emphasis (entity closure block is the ID-assignment point)
**Hypothesis:** Gap identifiers and entity closure reinforce each other when the entity closure block is the canonical point at which discovered gaps receive their IDs. During entity traversal, signals are noted inline as provisional ("provisional gap: CSR can read SSN field, no FLS"). At entity closure, each provisional signal is converted to a registered gap with a sequential ID. Downstream sections then reference by ID. This links the two criteria: you cannot close an entity without assigning IDs to any provisional signals, and you cannot assign IDs without explicitly tallying what the entity section found. The failure mode each prevents -- entity drift and unanchored gap references -- are two sides of the same coverage gap.

---

You are running a permissions trace signal for: {{topic}}

---

**SECURITY GAP REGISTER -- gaps are assigned sequential IDs at entity closure. Rows added during traversal carry PROVISIONAL status until the closure block promotes them.**

| ID | Entity | Field / Operation | Role(s) | Gap Type | Risk | Promoted? |
|----|--------|-------------------|---------|----------|------|-----------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH
Risk: CRITICAL / HIGH / MEDIUM
Promoted: YES (ID assigned at entity closure) / PROVISIONAL (inline signal, awaiting closure)

**How gap IDs are assigned:**
- During entity traversal: note provisional gaps inline with `[PROVISIONAL: [description]]`
- At the ENTITY CLOSURE block: convert each provisional signal to a registered gap, assign the next sequential ID ([G-01], [G-02], etc.), add to Security Gap Register with Promoted = YES
- After Phase 2: every gap in the register has an ID. No gap may remain PROVISIONAL after its entity closure block is written.
- Downstream references (Phase 4 remediation, Phase 5 defense-in-depth) cite by ID only.

---

## PHASE 1 -- INVENTORY AND ANALYSIS ORDER

**1.1 -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

**1.2 -- Role catalog:**

| Role | Type (Stock / Custom) | Persona | Has Write? |
|------|-----------------------|---------|------------|

Stock roles to check: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 -- Analysis order declaration:**

Reorder entities from highest to lowest sensitivity. State: "I will trace entities in this order: [list]. Provisional gaps will be noted inline and promoted to registered gaps at each entity closure block. The first gap ID assigned will be G-01."

---

## PHASE 2 -- PER-ENTITY TRACE WITH ID-ASSIGNMENT CLOSURE

**Instruction: During traversal, note provisional gaps inline. At the ENTITY CLOSURE block, assign IDs to all provisional signals for that entity, then advance.**

---

### Entity: [name] (Sensitivity: [rating])

**2a -- Operation-role matrix:**

| Role | Create | Read | Write | Delete | Assign | Record Scope |
|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Parent-Child BU / Team / User / Sharing-[rule name]
Every role from 1.2 must appear.

Inline signal instruction: If any operation assignment appears inconsistent with the entity's sensitivity rating, note: `[PROVISIONAL: [Role] has [operation] on [Entity] with [scope] -- unexpected given sensitivity. Flag at closure.]`

**2b -- Field-level security:**

| Field | Sensitivity | FLS Profile | Read: Allowed | Write: Allowed | Denied |
|-------|-------------|-------------|---------------|----------------|--------|

Rules:
- Every sensitive field must have a row
- FLS Profile = NONE: state this explicitly per field
- If a sensitive field has no FLS profile: note inline `[PROVISIONAL: [Field] on [Entity] -- no FLS, readable by any role with entity Read. Flag at closure. Expected type: MISSING-FLS, Risk: CRITICAL/HIGH]`
- Denied column must be confirmed explicitly

**2c -- Sharing rule audit:**

| Rule Name | Trigger | Access Granted | Recipient | Verdict |
|-----------|---------|----------------|-----------|---------|

For each role: state explicitly whether sharing rules expand access -- "Confirmed: no sharing rules expand [Role] access on [Entity]" or note the rule.
If a rule exceeds design intent: `[PROVISIONAL: [Rule] expands [Role] access on [Entity] beyond OWD+role intent. Flag at closure. Expected type: SHARING-CONFLICT.]`

**2d -- Team membership dependency:**

Team-dependent access? If yes: name team, blocked scenario, membership control, self-addition possibility. If PROVISIONAL signal: note inline. If no: "Confirmed: [Entity] access does not depend on team membership. Checked: [what was checked]."

**2e -- Escalation path check:**

For each role with Write access:
- Escalation confirmed: `[Role] -> [Write action] -> [elevated access reached]` -- note `[PROVISIONAL: escalation path via [mechanism]. Flag at closure. Expected type: ESCALATION-PATH, Risk: CRITICAL.]`
- Escalation ruled out: "Checked [Role]: write on [specific fields/operations]. No escalation because [specific mechanism]."
- Every role with Write must receive one of these two formats.

---

### ENTITY CLOSURE: [Entity name] -- ID Assignment Block

**Write this block before advancing. This is the point where provisional signals become registered gaps.**

**(a) Operations reviewed:**
"For [Entity], I reviewed: Create ([roles checked]), Read ([roles checked]), Write ([roles checked]), Delete ([roles checked]), Assign ([roles checked]). Excluded from scope: [list or NONE]."

**(b) Sensitive fields confirmed:**
"Sensitive fields on [Entity]: [list each field name and its FLS status -- profile name or NONE]. Fields without FLS protection: [list names or NONE]."

**(c) Provisional signals reviewed and promoted:**

| Provisional Signal | Gap Type | Risk | Assigned ID | Added to Register? |
|-------------------|----------|------|-------------|-------------------|

For each provisional signal noted during traversal of this entity:
- Assign the next sequential gap ID
- Confirm Gap Type and Risk
- Mark row as Promoted = YES in the Security Gap Register

If no provisional signals were noted: "No provisional signals during this entity. Register state unchanged. Next available ID: G-[N]."

**(d) Sharing rule verdicts confirmed:**
"Sharing rule verdicts for [Entity]: [list each role from 1.2 with its verdict -- expansion found or confirmed none]. All roles covered: YES."

---

[Repeat Phase 2 + ENTITY CLOSURE for each entity in sensitivity order]

---

## PHASE 3 -- PHASE GATE: PROMOTION AUDIT

**Before advancing to Phase 4, confirm all provisional signals have been promoted.**

Gate table:

| Entity | Closure Block Written? | Provisional Signals Found | IDs Assigned (list) | All Promoted? |
|--------|------------------------|--------------------------|---------------------|---------------|

Gate assertion: "All [N] entity closure blocks are written. All provisional signals have been promoted to registered gaps with sequential IDs. No PROVISIONAL entries remain in the Security Gap Register. Total registered gaps: [N] (G-01 through G-[N]). I am proceeding to Phase 4."

---

## PHASE 4 -- CROSS-ENTITY CASCADE

**4a -- Relationship map:**

| Source | Relationship Type | Target | Cascade Behavior |
|--------|-------------------|--------|-----------------|

**4b -- Cascade access trace:**

`[Role] -> [Source, access level, scope] -> [Relationship + cascade] -> [Target, access level resulting]`

State: INTENTIONAL or EMERGENT. If EMERGENT and exceeds direct grant: assign next gap ID at this point (cascade gaps may be assigned outside entity closure -- note in register with Promoted = YES at cascade trace time).

---

## PHASE 5 -- REMEDIATION AND DEFENSE-IN-DEPTH

**5a -- Gap remediation:**

For each row in the Security Gap Register, cite by ID:

`[G-##]: Apply [specific change] to [role / FLS profile / sharing rule / OWD / team config] in [solution location]. Current state: [what exists]. Target state: [what it should be]. After fix: [what a user can / cannot do].`

Re-describing a gap instead of citing its ID is a format failure. Every [G-##] in the register must appear exactly once in this section.

**5b -- Defense-in-depth assessment:**

| Entity | Security Role: Independent? | FLS: Independent? | Record Scope: Independent? | Single Point of Failure? | Open Gaps (IDs) |
|--------|---------------------------|-------------------|---------------------------|-------------------------|-----------------|

"Open Gaps (IDs)" = list any gap IDs that represent an unresolved risk to this entity's enforcement stack.

**5c -- Stock role summary:**

For each stock role present: baseline privileges, strengthened or weakened, necessary or removable. Reference gap IDs where this role is implicated.

---

## OUTPUT REQUIREMENTS

- Provisional signals noted inline must be promoted (ID assigned) at the entity closure block -- not earlier, not later
- No gap may remain PROVISIONAL after its entity closure block is written
- Every downstream reference to a gap cites its [G-##] ID -- re-description in lieu of ID citation is a format failure
- Entity closure block must include all three elements: (a) operations reviewed, (b) fields confirmed, (c) provisional signals promoted with IDs
- Phase Gate must confirm all provisional signals promoted before advancing to Phase 4

---

## V-05 -- Combined: Phrasing Register (Verdict Vocabulary) + Inertia Framing (OWD + Stock Baseline as Null Hypothesis)

**Axis:** Phrasing register (explicit verdict vocabulary for sharing rule analysis) + inertia framing (Dataverse stock baseline as the stated null hypothesis -- deviations trigger gap IDs)
**Hypothesis:** Sharing rule analysis fails C-14 not because the model ignores clean roles, but because there is no structural prompt to emit a verdict for them -- they are simply not mentioned. Framing the analysis against an explicit null hypothesis ("the Dataverse stock configuration for this role, at this OWD, with no sharing rules") forces a verdict by design: the model must either confirm the system matches baseline or identify the deviation. Combined with explicit verdict vocabulary ("BASELINE MATCH" / "DEVIATION G-##"), this makes every role's sharing rule status visible regardless of whether a conflict was found. Deviations become gap IDs, creating the cross-reference chain required by C-15.

---

You are running a permissions trace signal for: {{topic}}

---

**SECURITY DEVIATION REGISTER -- gaps are deviations from the stated Dataverse stock baseline. Assign [G-##] IDs at the point of deviation discovery.**

| ID | Entity | Field / Operation | Role(s) | Deviation Type | Baseline | Actual | Risk |
|----|--------|-------------------|---------|---------------|----------|--------|------|

Deviation types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH
Risk: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 -- INVENTORY AND BASELINE DECLARATION

**1.1 -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

**1.2 -- Role catalog:**

| Role | Type (Stock / Custom) | Persona | Dataverse Stock Baseline | Has Write? |
|------|-----------------------|---------|--------------------------|------------|

"Dataverse Stock Baseline" = the out-of-the-box privilege set for this role at the stated OWD:
- Customer Service Representative: Read/Write/Append on Case, Contact at BU scope; no sharing rules in stock config
- Basic User: Read personal, Append/AppendTo lookup fields; no entity-level Write on restricted entities
- System Customizer: metadata access; no data access without explicit grant
- System Administrator: org-level access to all entities; all FLS bypassed
- Custom roles: state privilege set as declared in the topic's security design

**1.3 -- Analysis order:**

Reorder entities from highest to lowest sensitivity. State: "I will trace entities in this order: [list]. For each role, I will state whether the actual configuration matches the declared baseline before identifying deviations."

---

## PHASE 2 -- PER-ENTITY TRACE: BASELINE-FIRST ANALYSIS

**Instruction: For each entity, state the baseline expectation for every role before examining actual configuration. Deviations from baseline receive a [G-##] identifier. Matches are confirmed. Both outcomes are visible in the output.**

---

### Entity: [name] (Sensitivity: [rating])

**2a -- Baseline vs. actual operation-role matrix:**

For each role, state baseline first, then actual:

| Role | Baseline Scope (from 1.2) | Actual: Create | Actual: Read | Actual: Write | Actual: Delete | Actual: Assign | Actual Record Scope | Verdict |
|------|--------------------------|---------------|-------------|--------------|---------------|---------------|---------------------|---------|

Verdict: BASELINE MATCH / DEVIATION [G-##]
- BASELINE MATCH: actual privileges and scope match the declared baseline
- DEVIATION [G-##]: assign next sequential ID; add to Security Deviation Register; state what differs

**2b -- Baseline vs. actual field-level security:**

For each sensitive field on this entity, state the expected FLS state before checking actual:

| Field | Sensitivity | Baseline FLS Expectation | Actual FLS Profile | Read: Allowed | Write: Allowed | Verdict |
|-------|-------------|-------------------------|--------------------|---------------|----------------|---------|

Baseline FLS expectation: "Given sensitivity=[High/Medium], baseline expectation for FLS = [REQUIRED / OPTIONAL]. Expected profile: [name or NONE]."
Verdict: BASELINE MATCH / DEVIATION [G-##]
- If sensitive field has no FLS profile where one is expected: assign [G-##], Deviation Type = MISSING-FLS

**2c -- Per-role sharing rule verdict:**

For each role with access to this entity, apply the sharing rule baseline and check actual:

| Role | Baseline Sharing Rule State | Actual Sharing Rules | Verdict |
|------|-----------------------------|---------------------|---------|

Baseline: "For [Role] at [OWD] with [record scope], stock Dataverse configuration: no sharing rules. Expected actual state: none."
Verdict:
- "BASELINE MATCH: Confirmed no sharing rules expand [Role] access on [Entity]. Checked: [location]. OWD=[value] + security role scope=[scope] apply. No criteria-based or manual sharing configured."
- "DEVIATION [G-##]: [Rule name] expands [Role] access on [Entity] to [record set]. Baseline expected: no sharing rules. Deviation type = SHARING-CONFLICT. Risk = [level]. Added to Security Deviation Register."

Every role must receive one of these two verdicts. Every entity must cover every role. Silence on a clean role fails this section.

**2d -- Team membership dependency:**

Baseline team dependency for this entity: "Stock configuration expects [team-dependent / team-independent] access for this entity."
Actual: does any role's access depend on team membership? If yes: name team, blocked scenario, membership control, self-addition possibility. Verdict: BASELINE MATCH / DEVIATION [G-##]. If no: "Confirmed: [Entity] access does not depend on team membership. Baseline match."

**2e -- Escalation path check:**

For each role with Write access:
- State baseline escalation risk: "Baseline for [Role] with Write at [scope]: [escalation risk expected based on stock privileges -- HIGH/LOW/NONE and reason]."
- Check actual: escalation confirmed or ruled out with specific mechanism.
- Escalation confirmed: add DEVIATION [G-##], Deviation Type = ESCALATION-PATH
- Escalation ruled out: "Checked [Role]: write on [specific operations]. No escalation path. Mechanism: [specific reason]. Baseline risk assessment: [CONFIRMED / REVISED]."

---

### ENTITY CLOSURE: [Entity name]

**(a) Operations reviewed:** "For [Entity], operations reviewed: [list each CRUD operation and the roles checked]. Excluded: [list or NONE]."

**(b) Sensitive fields confirmed:** "Sensitive fields: [list each by name with FLS verdict -- BASELINE MATCH or DEVIATION ID]. Fields deviating from baseline: [list or NONE]."

**(c) Deviations logged:** "Deviations found during this entity: [N]. IDs assigned: [list or NONE]. Baseline matches confirmed: [N] roles across [N] entities."

---

[Repeat Phase 2 + ENTITY CLOSURE for each entity in sensitivity order]

---

## PHASE 3 -- PHASE GATE: BASELINE COVERAGE AUDIT

Gate table:

| Entity | Baseline Declared? | Sharing Verdicts: All Roles Covered? | Deviations Found (IDs) | Baseline Matches Confirmed (N) |
|--------|-------------------|--------------------------------------|------------------------|-------------------------------|

Gate assertion: "Baseline coverage complete. Every role received a sharing rule verdict for every entity it touches. Total deviations: [N] (IDs: [list]). Total baseline confirmations: [N]. I am proceeding to Phase 4."

---

## PHASE 4 -- CROSS-ENTITY CASCADE

**4a -- Relationship map:**

| Source | Relationship Type | Target | Cascade Behavior | Baseline Cascade Expectation |
|--------|-------------------|--------|-----------------|------------------------------|

**4b -- Cascade access trace:**

For each relationship: `[Role] -> [Source, access level, scope] -> [Relationship + cascade] -> [Target, access level resulting]`

Baseline cascade expectation: state whether this cascade behavior is expected given stock Dataverse relationship configuration.
State: INTENTIONAL (matches baseline) or EMERGENT (deviation from baseline expectation). If EMERGENT and access exceeds direct grant: assign [G-##], Deviation Type = CASCADE-OVERREACH.

---

## PHASE 5 -- REMEDIATION AND DEFENSE-IN-DEPTH

**5a -- Deviation remediation:**

For each row in the Security Deviation Register, cite by ID:

`[G-##]: Deviation from baseline: [what the baseline expected]. Actual state: [what was found]. Fix: Apply [specific change] to [role / FLS profile / sharing rule / OWD / team config] in [solution location]. After fix: configuration returns to baseline behavior -- [what a user can / cannot do].`

Referencing by ID is required. Re-description instead of ID citation is a format failure.

**5b -- Defense-in-depth assessment:**

| Entity | Security Role: Independent? | FLS: Independent? | Record Scope: Independent? | Single Point of Failure? | Deviations That Threaten This Layer (IDs) |
|--------|---------------------------|-------------------|---------------------------|-------------------------|-------------------------------------------|

**5c -- Stock role baseline deviation summary:**

For each Dataverse stock role present: summarize whether its actual configuration matches the declared baseline, any deviations found (by ID), and whether the deviation strengthens or weakens the security posture.

---

## OUTPUT REQUIREMENTS

- Every role must receive an explicit sharing rule verdict for every entity it touches -- BASELINE MATCH or DEVIATION [G-##]
- Verdict silence on clean roles (roles with no sharing rule conflicts) is a format failure
- Every deviation receives a sequential [G-##] ID at the point of discovery
- Every downstream reference cites the ID -- re-description instead of ID citation is a format failure
- Entity closure must name (a) operations reviewed, (b) fields confirmed, (c) deviations logged with IDs
- Phase Gate must confirm all roles received sharing rule verdicts for all entities before advancing
