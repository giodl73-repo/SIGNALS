# trace-permissions Variate — Round 7 (Rubric v5)
**Date:** 2026-03-16
**Rubric:** v5 (C-01 through C-19, max 117.5)
**New criteria targeted this round:** C-18 (named phase exit gate artifacts), C-19 (aggregation routing rules)
**Prior structural baseline:** R4 V-05 provides C-13 (inertia framing), C-14 (per-phase failure mode annotation), C-15 (pre-phase failure mode catalog), C-16 (SHALL cross-role differential), C-17 (CONTEXT skill-level threat model); R6 V-01 provides C-11 PASS via two-pass artifact naming; R6 V-03 provides strongest phase dependency chaining

---

## Round 7 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Lifecycle emphasis -- named phase exit gate artifacts (C-18 single-axis) | V-01/R6 passes C-11 because Pass 2 references "Customer Service Access Summary from Pass 1" by exact name, but the PRODUCING phase never formally declares that artifact with a labeled schema. Without a production-side declaration, the name match is a coincidence -- if Pass 1 restructures its output, the match breaks silently. Adding "This pass produces: ARTIFACT (col \| col \| col)" at the end of Pass 1 converts coincidence into a two-point verifiable contract: the schema is on record before Pass 2 references it, and a mismatch is a visible contract violation |
| V-02 | Phase dependency chaining -- aggregation routing rules (C-19 single-axis) | V-03/R6 passes C-11 with three consecutive named artifact declarations but fails C-19: discoveries during traversal phases have no explicit path to the gap inventory. The model must remember which [G-##] assignments belong in Phase 4 -- an implicit convention, not a structural guarantee. Adding named routing rules ("any row where FLS Gap = YES MUST be assigned a [G-##] before the entity section closes; all [G-##] from Phases 2-3 MUST appear in Phase 4 inventory by ID; a gap absent from the inventory is a routing failure") closes the traversal-to-inventory boundary and makes failures detectable from the rule itself |
| V-03 | Combined: C-18 + C-19 (two closed contracts) | The four structural elements form two independent contracts: C-18 (output declaration) + C-11 (input declaration) closes the phase-to-phase dependency path; C-12-style inline discovery placement + C-19 (routing rules) closes the discovery-to-inventory path. Neither contract is complete without both halves. V-03 closes both simultaneously on the lifecycle phase baseline and tests whether dual-contract structure produces better coherence than each axis in isolation |
| V-04 | Combined: C-12 + C-13 + C-18 + C-19 (sentinel + inertia + both contracts) | Named sentinel tokens ([GAP-FLS-fieldname], [GAP-ESC-vectorname], [GAP-SHARE-rulename], [SCOPE AMBIGUOUS], [UNCHECKED]) are more precise routing targets than bare [G-##] IDs: a routing rule that says "any [GAP-FLS-*] sentinel placed in Phase 2 MUST appear in the Phase 6 inventory with token cited" identifies the routing gap by discovery type, not just by ID. Inertia framing (C-13) closes verdict drift alongside routing gap. C-18 exit gate declarations provide the named schemas that make C-11 input references contract-enforced rather than coincidental |
| V-05 | Full combination: all C-01 through C-19 | R4 V-05 provides C-13 through C-17 but leaves C-12, C-18, and C-19 unaddressed. Adding inline sentinel tokens (C-12), exit gate declarations (C-18), and aggregation routing rules (C-19) to the R4 V-05 baseline closes all remaining structural gaps. Two new skill-level failure modes are added to CONTEXT (FM-SKILL-4 output-schema drift, FM-SKILL-5 routing gap). Structural omissions are detectable at five levels simultaneously: skill-wide threat model, pre-phase catalog, phase-level annotation, exit gate declaration, and routing rule |

---

## V-01 -- Named Phase Exit Gate Artifacts

**Axis:** Lifecycle emphasis -- named phase exit gate artifacts with labeled schemas (C-18 single-axis)
**Hypothesis:** Adding an explicit "This pass produces: ARTIFACT NAME (col | col | col)" declaration at the end of Pass 1 converts the C-11 name match from coincidence to contract. The consuming phase (Pass 2) already references the artifact name; the producing phase (Pass 1) now formally declares it with a schema. The artifact name becomes the canonical token. A discrepancy between the declared schema and the consuming phase's reference is a visible contract violation. A producing phase that skips its output declaration leaves the C-11 chain with no enforced output side.

---

You are running a permissions trace signal for: **{{topic}}**

---

**SECURITY GAP REGISTER -- assign [G-##] identifiers sequentially starting at G-01. Add rows at the moment of discovery. Never batch or defer.**

| ID | Entity | Field / Operation | Role(s) | Gap Type | Risk | Remediation |
|----|--------|-------------------|---------|----------|------|-------------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH
Risk: CRITICAL / HIGH / MEDIUM

---

### PASS 1 -- Customer Service Baseline

**Scope:** Trace every entity, operation, and field accessible to the Customer Service Representative role (and any stock roles it inherits) for {{topic}}.

**Step 1a -- Entity catalog:**

List every entity that {{topic}} creates, reads, updates, or deletes.

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

Sensitivity: High (PII, financial, credentials, health) / Medium (internal-only, cross-BU risk) / Low (lookup, configuration)

**Step 1b -- Operation trace (Customer Service Representative):**

For each entity in sensitivity order (highest first):

| Entity | Create | Read | Write | Delete | Record Scope | Scope Appropriate? |
|--------|--------|------|-------|--------|--------------|-------------------|

Record Scope: User-owned / BU / Child BUs / Org-wide. Scope Appropriate: state whether the BU scope level is appropriate for the Customer Service role's stated purpose, or over-permissioned relative to that purpose. Required judgment per entity -- a blank cell fails this step.

**Step 1c -- Field visibility for sensitive fields:**

For each High or Medium sensitivity entity, evaluate FLS coverage per role per operation:

| Entity | Field | Sensitivity | FLS Profile (YES/NO/UNKNOWN) | Customer Service: Can Read? | Customer Service: Can Write? |
|--------|-------|-------------|------------------------------|-----------------------------|------------------------------|

Rule: Sensitive field + NO FLS profile + Customer Service has Read = assign [G-##] immediately. Gap Type = MISSING-FLS. Risk = CRITICAL.

**Step 1d -- Escalation path check (Write entities):**

For each entity where Customer Service has Write access, check all five vectors:

| Vector | Entity | Verdict | Evidence / Check Used |
|--------|--------|---------|----------------------|
| Record Assign | | POSSIBLE / NOT POSSIBLE | |
| Share to higher-privilege role | | POSSIBLE / NOT POSSIBLE | |
| Field modification affecting role or BU assignment | | POSSIBLE / NOT POSSIBLE | |
| Team self-addition | | POSSIBLE / NOT POSSIBLE | |
| Environment admin role override | | POSSIBLE / NOT POSSIBLE | |

NOT POSSIBLE requires naming the check that ruled it out -- not a bare assertion. POSSIBLE: assign [G-##], Gap Type = ESCALATION-PATH.

**Step 1e -- Scope appropriateness assessment:**

For each entity in the catalog, state explicitly: is the Customer Service record scope appropriate for the role's stated purpose, or over-permissioned relative to it? Name the purpose and the scope level in each assessment.

**Step 1f -- Sharing rule verdict (Customer Service):**

For each entity Customer Service touches:

| Entity | Sharing Rules Found? | Rule Name (if any) | Access Expanded Beyond OWD+Role? | Verdict |
|--------|---------------------|-------------------|----------------------------------|---------|

Confirmed: name the OWD value, role record scope, and confirmation method.
CONFLICT FOUND: assign [G-##], Gap Type = SHARING-CONFLICT.

**PASS 1 EXIT GATE -- this pass produces:**

> **CUSTOMER SERVICE ACCESS SUMMARY** (entity | operation | record scope | scope-appropriate verdict | FLS profile status per sensitive field | escalation vector verdicts | sharing verdict | gap IDs assigned)

This artifact is the canonical input for Pass 2. Pass 2 SHALL reference this artifact by its exact name: CUSTOMER SERVICE ACCESS SUMMARY from Pass 1. If Pass 1 is incomplete when Pass 2 begins, name the missing sections before advancing. A Pass 2 that proceeds without this artifact present is a dependency failure.

---

### PASS 2 -- Security Expert Extension

**Input required:** CUSTOMER SERVICE ACCESS SUMMARY from Pass 1. If Pass 1 is incomplete, name the missing sections before proceeding.

**Scope:** Extend the trace to the Security Expert (Dataverse security expert / custom role) for {{topic}}. For each entity and operation in the CUSTOMER SERVICE ACCESS SUMMARY from Pass 1, determine what the Security Expert can do that Customer Service cannot.

**Step 2a -- Security Expert role catalog entry:**

| Role | Type (Stock / Custom / Team / Env) | Business Unit Scope | Purpose | Has Write? | Column Security Profiles Attached |
|------|-------------------------------------|---------------------|---------|------------|----------------------------------|

**Step 2b -- Security Expert operation trace:**

For each entity in the CUSTOMER SERVICE ACCESS SUMMARY from Pass 1:

| Entity | Create | Read | Write | Delete | Record Scope | Delta vs Customer Service |
|--------|--------|------|-------|--------|--------------|--------------------------|

Delta: what the Security Expert can do that Customer Service cannot, per entity and operation. Note any operations where Security Expert can do less.

**Step 2c -- Security Expert field visibility:**

Reference sensitive fields from CUSTOMER SERVICE ACCESS SUMMARY from Pass 1:

| Entity | Field | Sensitivity | Security Expert: Can Read? | Security Expert: Can Write? | Delta vs Customer Service | FLS Gap? |
|--------|-------|-------------|-----------------------------|-----------------------------|--------------------------|----------|

FLS Gap: High-sensitivity field + no FLS profile + Security Expert has Read = assign [G-##]. Gap Type = MISSING-FLS. Risk = CRITICAL.

**Step 2d -- Security Expert escalation extension:**

Reference escalation verdicts from CUSTOMER SERVICE ACCESS SUMMARY from Pass 1:

| Vector | Customer Service Verdict | Security Expert Verdict | Escalation Delta | Gap |
|--------|--------------------------|-------------------------|-----------------|-----|

Security Expert opens an escalation path that Customer Service does not: assign [G-##], Gap Type = ESCALATION-PATH.

**Step 2e -- Scope appropriateness assessment (Security Expert):**

For each entity, state whether the Security Expert's record scope is appropriate for its stated purpose or over-permissioned. Name the purpose and the scope level.

**Step 2f -- Cross-role differential:**

For each entity and operation in the CUSTOMER SERVICE ACCESS SUMMARY from Pass 1, compare both roles side-by-side:

| Entity | Operation | Customer Service Access | Security Expert Access | Differential | Assessment |
|--------|-----------|------------------------|----------------------|--------------|------------|

Assessment: `EXPECTED DIFFERENTIAL -- [specific access elements named] consistent with [role's stated purpose] because [reason]` or `CANDIDATE OVER-PERMISSION -- [named access] exceeds [stated purpose] relative to [comparison role]. Access in question: [named operation or field].`

CANDIDATE OVER-PERMISSION: assign [G-##], Gap Type = BU-SCOPE.

**PASS 2 EXIT GATE -- this pass produces:**

> **FULL ACCESS INVENTORY** (role | entity | operation | record scope | scope verdict | sensitive field visibility | escalation verdict | sharing verdict | differential assessment | gap IDs assigned)

Pass 3 SHALL reference this artifact by its exact name: FULL ACCESS INVENTORY from Pass 2.

---

### PASS 3 -- Defense-in-Depth and Remediation

**Input required:** FULL ACCESS INVENTORY from Pass 2. SECURITY GAP REGISTER (all [G-##] rows).

**Step 3a -- Defense-in-depth assessment:**

For the two highest-sensitivity entities, evaluate security at all four Dataverse layers:

| Entity | Layer 1: Environment / Admin Role | Layer 2: Security Role + BU Scope | Layer 3: Team Membership | Layer 4: FLS / Column Security Profile | Effective Enforcement Layer |
|--------|----------------------------------|----------------------------------|--------------------------|---------------------------------------|----------------------------|

Effective Enforcement Layer: the lowest layer that independently enforces access without relying on upper layers. For at least one operation on at least one entity, explain why upper layers do not override it.

**Step 3b -- Gap remediation (cite by [G-##]):**

For each row in the SECURITY GAP REGISTER:

`[G-##]: Apply [specific change] to [exact Dataverse configuration object] in [solution location]. Current state: [what exists]. Target state: [what it should be]. After fix: [what a user can / cannot do].`

Exact Dataverse configuration objects: column security profile name (not "add FLS"), security role privilege + table name (not "tighten the role"), team type + membership rule (not "fix team membership"), sharing rule name (not "remove the rule"), OWD value per entity (not "adjust OWD"). Generic advice fails.

**Step 3c -- Dataverse terminology verification:**

Confirm that at least four of these Dataverse-native terms appear and are used accurately throughout this output: business unit, security role, owner team, access team, column security profile, table permission, sharing record, environment role.

**PASS 3 EXIT GATE -- this pass produces:**

> **REMEDIATION REGISTER** (gap ID | exact configuration object | specific change | post-fix behavior)
> **DEFENSE-IN-DEPTH ASSESSMENT** (entity | four-layer verdict | effective enforcement layer named)

---

## V-02 -- Aggregation Routing Rules

**Axis:** Phase dependency chaining -- explicit aggregation routing rules between discovery and gap inventory (C-19 single-axis)
**Hypothesis:** V-03/R6 has the strongest C-11 phase dependency architecture but fails C-19 because discoveries during traversal phases have no explicit path to the gap inventory. Adding named routing rules in each discovery section closes this boundary: (a) "any row where FLS Gap = YES MUST be assigned a [G-##] before the entity section closes" names the discovery mechanism and requires immediate routing; (b) "all [G-##] from Phases 2-3 MUST appear in the Phase 4 gap inventory by ID; a [G-##] absent from the inventory is a routing failure" names the aggregation destination and makes the failure detectable from the rule without re-reading the full trace.

---

You are running a permissions trace signal for: **{{topic}}**

---

**SECURITY GAP REGISTER -- assign [G-##] identifiers at the moment of discovery. Never defer.**

| ID | Entity | Field / Operation | Role(s) | Gap Type | Risk | Inventory Status |
|----|--------|-------------------|---------|----------|------|-----------------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH
Risk: CRITICAL / HIGH / MEDIUM
Inventory Status: PENDING (assigned, not yet verified in Phase 4 inventory) / ROUTED (confirmed in Phase 4 inventory)

---

### PHASE 1 -- Inventory

**Input required:** System description from provided context.

**1.1 -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

**1.2 -- Role catalog:**

| Role | Type (Stock / Custom / Team / Env) | Business Unit Scope | Purpose | Has Write? |
|------|-------------------------------------|---------------------|---------|------------|

Stock roles to check: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 -- Analysis order:** Order entities by sensitivity (highest first). State: "I will trace entities in this order: [list]. First gap ID: G-01."

---

### PHASE 2 -- Per-Entity Trace

**Input required:** ENTITY CATALOG and ROLE CATALOG from Phase 1. If Phase 1 is incomplete, name the missing items before proceeding.

For each entity (highest sensitivity first):

**2a -- Operations per role:**

| Entity | Role | Create | Read | Write | Delete | Record Scope | Scope Appropriate? |
|--------|------|--------|------|-------|--------|--------------|-------------------|

Scope Appropriate: required judgment per role per entity -- is the BU scope appropriate for the role's stated purpose, or over-permissioned? A blank cell fails this step.

**2b -- Sensitive field FLS status:**

| Entity | Field | Sensitivity | FLS Profile (YES/NO/UNKNOWN) | Role | Can Read? | FLS Gap? |
|--------|-------|-------------|------------------------------|------|-----------|----------|

**Routing rule -- FLS gaps:** Any row in this table where FLS Gap = YES MUST be assigned a [G-##] in the SECURITY GAP REGISTER (Gap Type = MISSING-FLS, Risk = CRITICAL) before this entity section closes. Completing step 2b for an entity without routing all YES rows is a routing failure. State at end of each entity: "FLS routing complete for [entity]: [G-##] assigned for [field/role pairs] / no FLS gaps."

**2c -- Escalation path check (Write roles only):**

| Vector | Roles | Verdict | Evidence |
|--------|-------|---------|----------|
| Record Assign | | POSSIBLE / NOT POSSIBLE | |
| Share to higher-privilege role | | POSSIBLE / NOT POSSIBLE | |
| Field modification affecting role/BU | | POSSIBLE / NOT POSSIBLE | |
| Team self-addition | | POSSIBLE / NOT POSSIBLE | |
| Admin role override | | POSSIBLE / NOT POSSIBLE | |

NOT POSSIBLE requires naming the check that ruled it out -- not a bare assertion.

**Routing rule -- escalation gaps:** Any POSSIBLE verdict MUST be assigned a [G-##] in the SECURITY GAP REGISTER (Gap Type = ESCALATION-PATH) before advancing to the next vector. A POSSIBLE verdict with no corresponding [G-##] is a routing failure. State at end of 2c: "Escalation routing complete for [entity]: [N] POSSIBLE verdicts, routed as [G-##, G-##] / no POSSIBLE verdicts."

---

### PHASE 3 -- Sharing Rule Analysis

**Input required:** ROLE CATALOG from Phase 1. ENTITY CATALOG from Phase 1. SECURITY GAP REGISTER current state from Phase 2.

For each role, produce a SHARING RULE VERDICT block:

#### SHARING RULE VERDICT: [Role name]

| Entity | Sharing Rules Found? | Rule Name | Access Expanded Beyond OWD+Role? | Verdict |
|--------|---------------------|-----------|----------------------------------|---------|

Verdict formats:
- `"Confirmed: no rules expand [Role] access on [Entity]. OWD=[value], role scope=[scope]. Method: [audit method]."`
- `"CONFLICT FOUND: [Rule] grants [Role] access to [record set] on [Entity]. Exceeds design intent: [reason]. Assigned [G-##]. Gap Type = SHARING-CONFLICT."`

Every entity the role touches must appear. Silent omissions fail this block.

**Routing rule -- sharing conflicts:** Any CONFLICT FOUND verdict MUST be assigned a [G-##] before the SHARING RULE VERDICT block for this role closes. State: "Sharing routing complete for [Role]: [N] conflicts routed as [G-##] / no conflicts found."

---

### PHASE 4 -- Gap Inventory and Coverage Gate

**Input required:** SECURITY GAP REGISTER (all [G-##] rows from Phases 2 and 3). ROLE CATALOG from Phase 1.

**4a -- Coverage gate:**

| Role | All Entities Traced (Phase 2)? | Sharing Verdict Written (Phase 3)? | Scope Assessed? | Open Gaps (N) |
|------|-------------------------------|-----------------------------------|-----------------|--------------|

Gate assertion: "All [N] entities traced in Phase 2. All [N] roles have sharing verdicts from Phase 3. All scope assessments present. Total gaps in SECURITY GAP REGISTER: [N]. Proceeding to gap inventory step."

**4b -- Gap inventory (aggregation step):**

List every [G-##] from the SECURITY GAP REGISTER:

| Gap ID | Type | Entity | Field / Operation | Role(s) | Risk | Source Phase | Remediation |
|--------|------|--------|-------------------|---------|------|-------------|-------------|

**Routing verification:** "Total [G-##] in SECURITY GAP REGISTER: [N]. Total rows in this inventory: [N]. All gaps routed: [YES/NO]."

If routing is not complete: name each missing [G-##] and the phase that produced it. Do not continue until every [G-##] in the SECURITY GAP REGISTER has a corresponding row in this inventory.

**4c -- Mark SECURITY GAP REGISTER:** Update all [G-##] rows to Inventory Status = ROUTED.

---

### PHASE 5 -- Cross-Entity Cascade

**Input required:** Phase 2 operation verdicts. Phase 4 gate confirmation.

**5a -- Relationship map (two highest-sensitivity entities):**

| Source | Relationship Type | Target | Cascade Behavior |
|--------|-------------------|--------|-----------------|

**5b -- Cascade access trace:**

`[Role] -> [Source, access, scope] -> [Relationship + cascade] -> [Target, resulting access]` -> INTENTIONAL or EMERGENT

EMERGENT access exceeding direct grant: assign [G-##], Gap Type = CASCADE-OVERREACH.

**Routing rule -- cascade gaps:** Any EMERGENT finding MUST be assigned a [G-##] immediately. Any [G-##] from Phase 5 MUST be added to the Phase 4 gap inventory as a Phase 5 addition. State: "Phase 5 cascade routing: [G-##] added to inventory / no cascade gaps found."

---

### PHASE 6 -- Cross-Role Differential and Remediation

**Input required:** Phase 4 gap inventory (updated with Phase 5 additions). Phase 2 operation verdicts.

**6a -- Cross-role differential:**

For at least two roles, compare access side-by-side on the same operation set:

| Role Pair | Entity | Operation | Role A Access | Role B Access | Differential | Assessment |
|-----------|--------|-----------|--------------|--------------|--------------|------------|

Assessment: `EXPECTED DIFFERENTIAL -- [specific access] consistent with [stated purpose] because [reason]` or `CANDIDATE OVER-PERMISSION -- [named access] exceeds [stated purpose] relative to [comparison role].`

CANDIDATE OVER-PERMISSION: assign [G-##], Gap Type = BU-SCOPE. Add to inventory as Phase 6 addition.

**6b -- Gap remediation (cite by [G-##]):**

For each gap in the Phase 4 inventory (including Phase 5-6 additions):

`[G-##]: Apply [specific change] to [exact Dataverse object] in [solution location]. Current state: [...]. Target state: [...]. Post-fix behavior: [...].`

Exact Dataverse objects: column security profile name, security role privilege + table name, team type + membership rule, sharing rule name, OWD value per entity. Generic advice fails.

**6c -- Defense-in-depth assessment:**

| Entity | Layer 1: Env / Admin | Layer 2: Security Role + BU | Layer 3: Team | Layer 4: FLS / Column Profile | Effective Enforcement Layer |
|--------|---------------------|----------------------------|---------------|------------------------------|----------------------------|

---

## V-03 -- Combined: C-18 + C-19 (Two Closed Contracts)

**Axis:** Lifecycle emphasis + phase dependency chaining -- named exit gate artifacts (C-18) + aggregation routing rules (C-19) combined
**Hypothesis:** The four structural elements form two independent closed contracts. Contract A governs the phase-to-phase dependency path: C-18 declares the output schema (producing phase), C-11 references the exact artifact name (consuming phase). Without C-18, C-11 references are coincidental name matches. Without C-11, C-18 declarations go unreferenced. Contract B governs the discovery-to-inventory path: discoveries are placed inline at point of occurrence (via [G-##] assignments), routing rules explicitly guarantee they reach the aggregation destination (C-19). Without routing rules, the aggregation relies on memory. V-03 tests whether closing both contracts simultaneously produces coherence benefits that neither single-axis variation alone achieves.

---

You are running a permissions trace signal for: **{{topic}}**

---

**SECURITY GAP REGISTER -- assign [G-##] at point of discovery. Never defer.**

| ID | Entity | Field / Operation | Role(s) | Gap Type | Risk | Source Phase | Inventory Status |
|----|--------|-------------------|---------|----------|------|-------------|-----------------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH
Inventory Status: PENDING / ROUTED

**Global routing rule:** Every [G-##] assigned in any phase MUST appear in the Phase 5 GAP INVENTORY by Gap ID before the analysis concludes. A [G-##] in the SECURITY GAP REGISTER with Inventory Status = PENDING at the end of Phase 5 is a routing failure.

---

### PHASE 1 -- Inventory and Analysis Order

**Input required:** System description from provided context.

**1.1 -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

**1.2 -- Role catalog:**

| Role | Type (Stock / Custom / Team / Env) | Business Unit Scope | Purpose | Has Write? | Column Security Profiles Attached |
|------|-------------------------------------|---------------------|---------|------------|----------------------------------|

Stock roles: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 -- Scope appropriateness pre-assessment:** For each role, state whether the assigned BU scope is appropriate for its stated purpose or over-permissioned. Required judgment -- do not leave blank.

**1.4 -- Analysis order:** "I will trace entities in this order: [list, highest sensitivity first]. First gap ID: G-01."

**PHASE 1 EXIT GATE -- this phase produces:**

> **ENTITY CATALOG** (entity name | org-wide default | sensitivity | reason for sensitivity)
> **ROLE CATALOG** (role name | type | BU scope | purpose | has write? | column security profiles)

These are the canonical artifact names for Phase 2 input declarations. Phase 2 SHALL reference ENTITY CATALOG from Phase 1 and ROLE CATALOG from Phase 1 by these exact names. A Phase 2 that begins without both artifacts named is a dependency failure.

---

### PHASE 2 -- Per-Entity Trace

**Input required:** ENTITY CATALOG from Phase 1. ROLE CATALOG from Phase 1. If either named artifact is incomplete, name the missing content before proceeding.

For each entity in sensitivity order (highest first):

**2a -- Operations per role:**

| Entity | Role | Create | Read | Write | Delete | Record Scope |
|--------|------|--------|------|-------|--------|--------------|

**2b -- Sensitive field FLS status:**

| Entity | Field | Sensitivity | FLS Profile (YES/NO/UNKNOWN) | Role | Can Read? | FLS Gap? |
|--------|-------|-------------|------------------------------|------|-----------|----------|

**Routing rule -- FLS gaps:** Any row where FLS Gap = YES MUST be assigned a [G-##] in the SECURITY GAP REGISTER (Gap Type = MISSING-FLS, Risk = CRITICAL) before this entity section closes. State: "FLS routing for [entity]: [G-##] assigned / no FLS gaps."

**2c -- Escalation path check (Write roles only):**

| Vector | Roles | Verdict | Evidence |
|--------|-------|---------|----------|
| Record Assign | | POSSIBLE / NOT POSSIBLE | |
| Share to higher-privilege role | | POSSIBLE / NOT POSSIBLE | |
| Field modification affecting role/BU | | POSSIBLE / NOT POSSIBLE | |
| Team self-addition | | POSSIBLE / NOT POSSIBLE | |
| Admin role override | | POSSIBLE / NOT POSSIBLE | |

NOT POSSIBLE requires naming the check that ruled it out.

**Routing rule -- escalation gaps:** Any POSSIBLE verdict MUST be assigned a [G-##] before advancing to the next vector. State: "Escalation routing for [entity]: [N] POSSIBLE, routed as [G-##] / no POSSIBLE."

**PHASE 2 EXIT GATE -- this phase produces:**

> **ACCESS MATRIX** (entity | role | create | read | write | delete | record scope -- all roles x all entities populated)
> **FLS GAP TABLE** (entity | field | sensitivity | FLS profile | role | can read | FLS gap flag -- all sensitive fields populated)
> **ESCALATION FINDINGS** (entity | vector | roles checked | verdict | evidence -- all write roles x all vectors populated)

Phase 3 SHALL reference ACCESS MATRIX from Phase 2 and ESCALATION FINDINGS from Phase 2 by these exact names. A Phase 3 that begins without naming these artifacts is a dependency failure.

---

### PHASE 3 -- Sharing Rule Analysis

**Input required:** ROLE CATALOG from Phase 1. ACCESS MATRIX from Phase 2. ESCALATION FINDINGS from Phase 2. If any named artifact is incomplete, stop before proceeding.

For each role, produce a SHARING RULE VERDICT block:

#### SHARING RULE VERDICT: [Role name]

| Entity | Sharing Rules Found? | Rule Name | Access Expanded Beyond OWD+Role? | Verdict |
|--------|---------------------|-----------|----------------------------------|---------|

Verdict formats:
- `"Confirmed: no rules expand [Role] access on [Entity]. OWD=[value], scope=[scope]. Method: [audit method]."`
- `"CONFLICT FOUND: [Rule] grants [Role] access to [record set]. Exceeds design intent: [reason]. Assigned [G-##]. Gap Type = SHARING-CONFLICT."`

Every entity in the ACCESS MATRIX from Phase 2 that the role touches must appear. Silent omissions fail.

**Routing rule -- sharing conflicts:** Any CONFLICT FOUND verdict MUST be assigned a [G-##] before the SHARING RULE VERDICT block for this role closes. State: "Sharing routing for [Role]: [N] conflicts routed as [G-##] / no conflicts."

**PHASE 3 EXIT GATE -- this phase produces:**

> **SHARING VERDICTS** (role | entity | sharing rules found | access expanded | verdict | gap ID if any -- all roles x all entities populated)

Phase 4 SHALL reference SHARING VERDICTS from Phase 3 by this exact name.

---

### PHASE 4 -- Coverage Gate

**Input required:** ACCESS MATRIX from Phase 2. FLS GAP TABLE from Phase 2. ESCALATION FINDINGS from Phase 2. SHARING VERDICTS from Phase 3. If any named artifact is missing, stop and name the gap.

| Role | ACCESS MATRIX Complete? | ESCALATION FINDINGS Written? | SHARING VERDICTS Written? | Current Gap Count |
|------|------------------------|-----------------------------|-----------------------------|-----------------|

Gate assertion: "All [N] entities in ACCESS MATRIX. All write-capable roles have ESCALATION FINDINGS. All [N] roles have SHARING VERDICTS. Total [G-##] in SECURITY GAP REGISTER: [N]. Proceeding to Phase 5."

Stop condition: missing artifact or role -- name and resolve before continuing.

**PHASE 4 EXIT GATE -- this phase produces:**

> **COVERAGE GATE CONFIRMATION** (all-entities-traced: YES/NO | all-sharing-verdicts: YES/NO | total gaps: N)

Phase 5 SHALL reference COVERAGE GATE CONFIRMATION from Phase 4 as authorization to proceed.

---

### PHASE 5 -- Gap Inventory and Cross-Entity Cascade

**Input required:** SECURITY GAP REGISTER (all [G-##] rows). ACCESS MATRIX from Phase 2. COVERAGE GATE CONFIRMATION from Phase 4.

**5a -- Gap inventory (aggregation step):**

List every [G-##] from the SECURITY GAP REGISTER:

| Gap ID | Type | Entity | Field / Operation | Role(s) | Risk | Source Phase | Remediation |
|--------|------|--------|-------------------|---------|------|-------------|-------------|

**Routing verification:** "[N] gaps in SECURITY GAP REGISTER. [N] rows in this inventory. All routing complete: [YES/NO]."

If routing is not complete: name the missing [G-##] and the phase that produced it. Do not continue until every [G-##] is present.

Update SECURITY GAP REGISTER: mark all rows Inventory Status = ROUTED.

**5b -- Cross-entity cascade (two highest-sensitivity entities):**

| Source | Relationship Type | Target | Cascade Behavior |
|--------|-------------------|--------|-----------------|

`[Role] -> [Source, access, scope] -> [Relationship + cascade] -> [Target, resulting access]` -> INTENTIONAL or EMERGENT

EMERGENT: assign [G-##], Gap Type = CASCADE-OVERREACH. Add to gap inventory immediately as Phase 5 addition.

**PHASE 5 EXIT GATE -- this phase produces:**

> **AGGREGATE GAP LIST** (gap ID | type | entity | field/operation | role(s) | risk | source phase -- all gaps including Phase 5 additions)

Phase 6 SHALL reference AGGREGATE GAP LIST from Phase 5 by this exact name.

---

### PHASE 6 -- Cross-Role Differential and Remediation

**Input required:** AGGREGATE GAP LIST from Phase 5. ACCESS MATRIX from Phase 2.

**6a -- Cross-role differential:**

For at least two roles, compare access side-by-side:

| Role Pair | Entity | Operation | Role A Access | Role B Access | Differential | Assessment |
|-----------|--------|-----------|--------------|--------------|--------------|------------|

Assessment: `EXPECTED DIFFERENTIAL -- [specific access] consistent with [stated purpose] because [reason]` or `CANDIDATE OVER-PERMISSION -- [named access] exceeds [stated purpose] relative to [comparison role].`

CANDIDATE OVER-PERMISSION: assign [G-##], add to AGGREGATE GAP LIST from Phase 5 as Phase 6 addition.

**6b -- Gap remediation (cite by [G-##]):**

For each row in the AGGREGATE GAP LIST from Phase 5:

`[G-##]: Apply [specific change] to [exact Dataverse object]. Current state: [...]. Target state: [...]. Post-fix behavior: [...].`

**6c -- Defense-in-depth assessment:**

| Entity | Layer 1: Env/Admin | Layer 2: Security Role + BU | Layer 3: Team | Layer 4: FLS/Column Profile | Effective Enforcement Layer |
|--------|------------------|----------------------------|---------------|----------------------------|----------------------------|

---

## V-04 -- Sentinel + Inertia + C-18 + C-19

**Axis:** Combined -- inline violation sentinels (C-12) + security state persistence (C-13) + named exit gate artifacts (C-18) + aggregation routing rules (C-19)
**Hypothesis:** Named sentinel tokens are more precise routing targets than bare [G-##] IDs. A routing rule that says "any [GAP-FLS-*] sentinel placed in Phase 2 MUST appear in the Phase 6 SENTINEL INVENTORY with token cited" identifies the specific discovery type at the routing gap, not just a missing ID. The sentinel type ([GAP-FLS-*] vs [GAP-ESC-*] vs [GAP-SHARE-*]) carries semantic content -- a routing failure involving [GAP-FLS-creditlimit] is more diagnosable than a generic missing [G-##]. Inertia framing (C-13) adds verdict continuity: SECURITY STATE REGISTER verdicts carry forward explicitly across phases, making verdict drift detectable as a missing carry-forward notation alongside the routing gaps. C-18 exit gate declarations close the phase-to-phase dependency path so C-11 input references are contract-enforced.

---

You are running a permissions trace signal for: **{{topic}}**

---

**SECURITY GAP REGISTER -- assign [G-##] at point of discovery. Never defer.**

| ID | Sentinel Token | Entity | Field / Operation | Role(s) | Gap Type | Risk |
|----|---------------|--------|-------------------|---------|----------|------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH

**Sentinel token vocabulary:**
- `[GAP-FLS-fieldname]` -- sensitive field with no FLS profile; place inline at the discovery row in the FLS table
- `[GAP-ESC-vectorname]` -- POSSIBLE escalation vector; place inline at the escalation check row
- `[GAP-SHARE-rulename]` -- sharing conflict found; place inline at the SHARING RULE VERDICT row
- `[SCOPE AMBIGUOUS]` -- BU scope cannot be assessed without additional information; place inline at the scope assessment step
- `[UNCHECKED]` -- a vector, field, or entity that cannot be evaluated from provided context; place inline at the analysis point

**Sentinel placement rule:** Every sentinel token MUST be placed inline in the analysis text at the exact point of discovery. Do not batch sentinels at end of sections or invent them at summary time.

---

**SECURITY STATE REGISTER -- authoritative per-role verdict record. Updated by every phase.**

| Role | Phase Last Updated | Current Verdict | Active Sentinel Tokens | Active Gap IDs |
|------|--------------------|-----------------|----------------------|----------------|

Verdict values: `CLEARED` / `FLAGGED [sentinel tokens, G-##]` / `PENDING-PHASE-[N]`

**Inertia rule:** Every verdict from Phase N is the persistent default entering Phase N+1. When a phase finds nothing new for a role:
`[Role] -- INERTIA: [verdict] from Phase [N], no new finding this phase.`
Required for every role in every phase. Absence = verdict unknown = detectable format failure.

---

### PHASE 1 -- Inventory

> **Structural purpose:** Prevents incomplete coverage -- the failure mode where analysis proceeds on an assumed set that excludes system roles, environment roles, or low-salience entities.

**Input required:** System description from provided context.

**1.1 -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

**1.2 -- Role catalog:**

| Role | Type (Stock / Custom / Team / Env) | Business Unit Scope | Purpose | Has Write? | Column Security Profiles |
|------|-------------------------------------|---------------------|---------|------------|--------------------------|

Stock roles: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 -- Scope pre-assessment:** For each role, state whether the assigned BU scope is appropriate for its stated purpose or over-permissioned. Place `[SCOPE AMBIGUOUS]` inline if undeterminable. Assign [G-##] for any `[SCOPE AMBIGUOUS]` placement.

**1.4 -- Initialize SECURITY STATE REGISTER:** Set all roles to `PENDING-PHASE-2`.

**1.5 -- Analysis order:** "I will trace entities in this order: [list, highest sensitivity first]. First gap ID: G-01."

**PHASE 1 EXIT GATE -- this phase produces:**

> **ENTITY CATALOG** (entity name | org-wide default | sensitivity | reason)
> **ROLE CATALOG** (role name | type | BU scope | purpose | has write? | column security profiles)

Phase 2 SHALL reference ENTITY CATALOG from Phase 1 and ROLE CATALOG from Phase 1 by these exact names.

---

### PHASE 2 -- Per-Entity Trace

> **Structural purpose:** Prevents FLS post-incident discovery (sensitive fields unprotected at the role level) and verdict scatter (access conclusions embedded in prose and unauditable).

**Input required:** ENTITY CATALOG from Phase 1. ROLE CATALOG from Phase 1.
**Dependency check:** If either named artifact is incomplete, name the missing content before proceeding.

For each entity (highest sensitivity first):

**2a -- Operations per role:**

| Entity | Role | Create | Read | Write | Delete | Record Scope |
|--------|------|--------|------|-------|--------|--------------|

**2b -- Sensitive field FLS status:**

Place sentinel token inline at the discovery row when a field has no FLS profile and a role can read it. Then assign [G-##].

| Entity | Field | Sensitivity | FLS Profile (YES/NO/UNKNOWN) | Role | Can Read? | Can Write? | Sentinel |
|--------|-------|-------------|------------------------------|------|-----------|------------|---------|

Gap rule: High/Medium sensitivity + NO FLS profile + role has Read -> place `[GAP-FLS-fieldname]` inline, assign [G-##]. Gap Type = MISSING-FLS. Risk = CRITICAL.

**Routing rule -- FLS sentinels:** Any `[GAP-FLS-*]` sentinel placed in this table MUST have a corresponding [G-##] in the SECURITY GAP REGISTER AND MUST appear in the Phase 6 SENTINEL INVENTORY by sentinel token name. A sentinel without a [G-##] is a routing failure.

**2c -- Escalation path check (Write roles only):**

| Vector | Roles | Verdict | Sentinel (if POSSIBLE) | Evidence |
|--------|-------|---------|----------------------|----------|
| Record Assign | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-assign]` | |
| Share to higher-privilege role | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-share]` | |
| Field modification affecting role/BU | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-field-modify]` | |
| Team self-addition | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-team-self]` | |
| Admin role override | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-admin-override]` | |

NOT POSSIBLE requires naming the ruling-out check. POSSIBLE: place sentinel inline at this row, assign [G-##].

**Routing rule -- escalation sentinels:** Any `[GAP-ESC-*]` sentinel MUST have a [G-##] AND MUST appear in Phase 6 SENTINEL INVENTORY.

**2d -- SECURITY STATE UPDATE (required for every role after every entity):**
- Sentinel placed: `[Role] -- FLAGGED [sentinel token, G-##]. Source: Phase 2 / [Entity].`
- No finding: `[Role] -- INERTIA: [prior verdict], no finding on [Entity].`

**PHASE 2 EXIT GATE -- this phase produces:**

> **ACCESS MATRIX** (entity | role | create | read | write | delete | record scope -- all roles x all entities)
> **FLS SENTINEL TABLE** (entity | field | sensitivity | FLS profile | role | can read | sentinel token | G-##)
> **ESCALATION FINDINGS** (entity | vector | roles | verdict | sentinel token | G-##)

Phase 3 SHALL reference ACCESS MATRIX from Phase 2, FLS SENTINEL TABLE from Phase 2, and ESCALATION FINDINGS from Phase 2 by these exact names.

---

### PHASE 3 -- Sharing Rule Analysis

> **Structural purpose:** Prevents the sharing/FLS intersection gap -- sharing rules operate below security role scope and produce access invisible to role-level analysis. Cannot be caught in Phase 2.

**Input required:** ROLE CATALOG from Phase 1. ACCESS MATRIX from Phase 2. ESCALATION FINDINGS from Phase 2.

For each role, produce a SHARING RULE VERDICT block:

#### SHARING RULE VERDICT: [Role name]

| Entity | Sharing Rules Found? | Rule Name | Access Expanded Beyond OWD+Role? | Verdict | Sentinel |
|--------|---------------------|-----------|----------------------------------|---------|---------|

Verdict: `Confirmed: no rules expand access. OWD=[value], scope=[scope]. Method: [audit method].`
Conflict: `CONFLICT FOUND: [Rule] grants access to [record set]. Exceeds design intent: [reason].` + place `[GAP-SHARE-rulename]` inline. Assign [G-##], Gap Type = SHARING-CONFLICT.

Every entity in ACCESS MATRIX from Phase 2 that the role touches must appear.

**Routing rule -- sharing sentinels:** Any `[GAP-SHARE-*]` sentinel MUST have a [G-##] AND MUST appear in Phase 6 SENTINEL INVENTORY by token name.

**SECURITY STATE UPDATE after each SHARING RULE VERDICT:**
- Conflict: `[Role] -- FLAGGED [GAP-SHARE-*, G-##]. Source: Phase 3 / [Entity].`
- No conflict: `[Role] -- INERTIA: [verdict] from Phase 2, sharing clean on [entity list].`

**PHASE 3 EXIT GATE -- this phase produces:**

> **SHARING VERDICTS** (role | entity | sharing rules found | access expanded | verdict | sentinel token | G-##)

Phase 4 SHALL reference SHARING VERDICTS from Phase 3 by this exact name.

---

### PHASE 4 -- Coverage Gate

> **Structural purpose:** Prevents phase-transition coverage loss -- all roles and entities must be confirmed covered before synthesis begins.

**Input required:** ACCESS MATRIX from Phase 2. FLS SENTINEL TABLE from Phase 2. ESCALATION FINDINGS from Phase 2. SHARING VERDICTS from Phase 3.

| Role | ACCESS MATRIX: All Entities? | SHARING VERDICTS Written? | State Register Non-PENDING? | Current Verdict | Active Sentinels |
|------|------------------------------|--------------------------|----------------------------|-----------------|-----------------|

Gate assertion: "All [N] entities in ACCESS MATRIX. All [N] roles have SHARING VERDICTS. SECURITY STATE REGISTER has zero PENDING-PHASE entries. Total [G-##]: [N]. Total sentinels placed so far: [types and counts]. Proceeding."

Stop condition: any PENDING-PHASE entry remaining -- name the role and resolve before continuing.

**PHASE 4 EXIT GATE -- this phase produces:**

> **COVERAGE GATE CONFIRMATION** (all-entities-traced: YES | all-sharing-verdicts: YES | state-consistent: YES | total gaps: N | total sentinels: N)

Phase 5 SHALL reference COVERAGE GATE CONFIRMATION from Phase 4.

---

### PHASE 5 -- Cross-Entity Cascade

> **Structural purpose:** Prevents single-entity tunnel vision -- entity relationships produce access paths invisible to per-entity analysis.

**Input required:** ACCESS MATRIX from Phase 2. COVERAGE GATE CONFIRMATION from Phase 4.

**5a -- Relationship map (two highest-sensitivity entities):**

| Source | Relationship Type | Target | Cascade Behavior |
|--------|-------------------|--------|-----------------|

**5b -- Cascade access trace:**

`[Role] -> [Source, access, scope] -> [Relationship + cascade] -> [Target, resulting access]` -> INTENTIONAL or EMERGENT

EMERGENT: place `[GAP-ESC-cascade-[entity]]` inline. Assign [G-##], Gap Type = CASCADE-OVERREACH.

**Routing rule -- cascade sentinels:** Any `[GAP-ESC-cascade-*]` sentinel MUST have a [G-##] AND MUST appear in Phase 6 SENTINEL INVENTORY as a Phase 5 addition.

**SECURITY STATE UPDATE:**
- Cascade gap: `[Role] -- FLAGGED [GAP-ESC-cascade-*, G-##]. Source: Phase 5.`
- No finding: `[Role] -- INERTIA: [verdict] from Phase 4, no cascade finding.`

**PHASE 5 EXIT GATE -- this phase produces:**

> **CASCADE FINDINGS** (role | source | relationship | target | INTENTIONAL/EMERGENT | sentinel token | G-##)

---

### PHASE 6 -- Sentinel Inventory (Aggregation)

> **Structural purpose:** Prevents gap loss at the traversal-to-summary transition -- the sentinel inventory aggregates all discovery-point tokens; the gap list derives from this inventory, not from memory.

**Input required:** FLS SENTINEL TABLE from Phase 2. ESCALATION FINDINGS from Phase 2. SHARING VERDICTS from Phase 3. CASCADE FINDINGS from Phase 5. SECURITY GAP REGISTER (all [G-##] rows).

**6a -- SENTINEL INVENTORY:**

List every sentinel placed in Phases 1-5, in phase order:

| Sentinel Token | Type | Phase Placed | Entity | Field / Operation | Role(s) | G-## |
|---------------|------|-------------|--------|------------------|---------|------|

**Routing verification (mandatory before proceeding):**
- "Total `[GAP-FLS-*]` sentinels placed: [N]. All in inventory: [YES/NO]."
- "Total `[GAP-ESC-*]` sentinels placed: [N]. All in inventory: [YES/NO]."
- "Total `[GAP-SHARE-*]` sentinels placed: [N]. All in inventory: [YES/NO]."
- "Total `[SCOPE AMBIGUOUS]` placed: [N]. All in inventory: [YES/NO]."
- "Total `[UNCHECKED]` placed: [N]. All in inventory: [YES/NO]."
- "Total [G-##] in SECURITY GAP REGISTER: [N]. All referenced in inventory: [YES/NO]."

If any answer is NO: name the missing token and the phase that produced it. Do not proceed until reconciled.

**6b -- Aggregate gap list (derived from SENTINEL INVENTORY):**

| Gap ID | Sentinel Token | Type | Entity | Field / Operation | Role(s) | Risk | Source Phase | Remediation |
|--------|---------------|------|--------|------------------|---------|------|-------------|-------------|

Each row traces to an entry in the SENTINEL INVENTORY above. A gap row without a sentinel inventory entry is an unsourced claim.

**PHASE 6 EXIT GATE -- this phase produces:**

> **SENTINEL INVENTORY** (all sentinel tokens | type | phase | entity | role | G-##)
> **AGGREGATE GAP LIST** (G-## | sentinel token | type | entity | role | risk | source phase)

Phase 7 SHALL reference AGGREGATE GAP LIST from Phase 6 by this exact name.

---

### PHASE 7 -- Cross-Role Differential, Remediation, Defense-in-Depth

> **Structural purpose:** Prevents differential blindness and non-actionable remediation.

**Input required:** AGGREGATE GAP LIST from Phase 6. ACCESS MATRIX from Phase 2. ROLE CATALOG from Phase 1.

**7a -- Cross-role differential:**

For at least two roles, compare access side-by-side on the same operations:

| Role Pair | Entity | Operation | Role A Access | Role B Access | Differential | Assessment |
|-----------|--------|-----------|--------------|--------------|--------------|------------|

Assessment: `EXPECTED DIFFERENTIAL -- [specific access] consistent with [stated purpose]` or `CANDIDATE OVER-PERMISSION -- [named access] exceeds [stated purpose] relative to [comparison role].`

CANDIDATE OVER-PERMISSION: place `[GAP-ESC-overpermission-[role]]` inline. Assign [G-##]. Add to AGGREGATE GAP LIST from Phase 6 as Phase 7 addition.

**SECURITY STATE UPDATE:** CANDIDATE OVER-PERMISSION -> `FLAGGED [sentinel, G-##]. Source: Phase 7.` No finding -> carry-forward notation.

**7b -- Gap remediation (cite by [G-##] and sentinel token):**

For each row in AGGREGATE GAP LIST from Phase 6:

`[G-##] [sentinel token]: Apply [specific change] to [exact Dataverse object] in [solution location]. Current state: [...]. Target state: [...]. Post-fix behavior: [...].`

**7c -- Defense-in-depth assessment (two highest-sensitivity entities):**

| Entity | Layer 1: Env/Admin | Layer 2: Security Role + BU | Layer 3: Team | Layer 4: FLS/Column Profile | Effective Enforcement Layer |
|--------|------------------|----------------------------|---------------|----------------------------|----------------------------|

**Final SECURITY STATE REGISTER:** Copy in final form. Every role must have `CLEARED` or `FLAGGED [sentinel list, G-## list]`. No PENDING entries.

---

## V-05 -- Full Combination: All C-01 Through C-19

**Axis:** Full structural integration -- all 19 criteria simultaneously targeted
**Hypothesis:** R4 V-05 provides C-13 through C-17 but leaves C-12 (inline sentinels), C-18 (exit gate declarations), and C-19 (aggregation routing rules) unaddressed. Adding these three mechanisms closes the last structural gaps. Two new skill-level failure modes are added to CONTEXT (FM-SKILL-4 for output-schema drift, FM-SKILL-5 for routing gap). Structural omissions are now detectable at five levels simultaneously: skill-wide threat model (C-17), pre-phase catalog (C-15), phase-level annotation (C-14), exit gate declaration (C-18 enforcing C-11), and routing rule (C-19 closing C-12 discovery to inventory).

---

You are running a permissions trace signal for: **{{topic}}**

---

## CONTEXT -- Why Permissions Tracing Fails: Skill-Level Threat Model

Before any analysis begins, understand the five failure modes that permissions tracing as a category of work is structurally prone to produce:

**FM-SKILL-1 -- FLS post-incident discovery.** Field-level security gaps are invisible at the security role level. A role can be correctly scoped -- right operations, right entities, right BU scope -- while a sensitive field has no column security profile. This gap surfaces only after an incident: an authenticated user reads a field they were never meant to access. Standard role-matrix analysis does not catch this because entity-level Read does not expose which fields within that entity are unprotected. FLS must be traced as a separate analytical pass distinct from operation-level role analysis.

**FM-SKILL-2 -- Cumulative scope blindness.** Each individual role may be scoped correctly. The failure occurs when role combinations -- team inheritance granting broader BU scope, sharing records granting record access below entity-level deny, environment admin roles elevating restricted roles, cascade relationships between entities -- produce an effective access scope that no single-role analysis predicts. This failure is invisible to per-role analysis and visible only to cross-role differential and cascade analysis.

**FM-SKILL-3 -- Verdict drift.** Role verdicts assigned early in the analysis are silently overridden when the model transitions between phases. A CLEARED verdict from Phase 2 is re-evaluated from scratch in Phase 3, sometimes with a different conclusion -- not because new evidence was found, but because the prior verdict was not carried forward. The gap inventory then reflects late-phase verdicts, not the accumulated evidence chain.

**FM-SKILL-4 -- Output-schema drift.** Phase dependency declarations reference artifacts from prior phases by name. But if the producing phase never declares its output schema, the artifact name in the consuming phase is a best guess. When context pressure causes the producing phase to restructure its output, the name match breaks silently. The consuming phase proceeds with a reference that no longer has a corresponding artifact, and the dependency chain is broken without detection.

**FM-SKILL-5 -- Routing gap.** Violation discoveries placed inline during traversal phases do not automatically reach the gap inventory. The model must remember which discoveries to aggregate. At the traversal-to-summary transition, discoveries without explicit routing rules are susceptible to omission -- not because the discovery was missed, but because the aggregation step recollects from memory rather than routing from named sources.

These failure modes motivate the structure of this analysis: dedicated FLS sentinel placement (FM-SKILL-1), cross-role differential and cascade phases (FM-SKILL-2), SECURITY STATE REGISTER with inertia framing (FM-SKILL-3), named exit gate artifact declarations (FM-SKILL-4), and explicit aggregation routing rules (FM-SKILL-5).

Use Dataverse-native terminology throughout: business units, security roles, owner teams, access teams, column security profiles, table permissions, sharing records, environment roles. At least four Dataverse-specific terms must appear and be used accurately.

---

## FAILURE MODE MAP

Read this map before Phase 1. It lists every structural element and the failure mode it defends against. A structural element absent from the output leaves its failure mode unmitigated -- detectable here before analysis begins.

| Structural Element | Defends Against |
|-------------------|-----------------|
| Phase 1 -- complete entity + role catalog | FM-P1: Incorrect coverage undetectable once analysis begins |
| Sentinel tokens [GAP-FLS-*], [GAP-ESC-*], [GAP-SHARE-*], [SCOPE AMBIGUOUS], [UNCHECKED] placed inline at discovery | FM-SKILL-1 + FM-P2: Discoveries not recorded at point of occurrence |
| Phase 2 -- FLS SENTINEL TABLE + ESCALATION FINDINGS with sentinels | FM-SKILL-1 (FLS gap invisible at role level) + FM-P3: Verdict scatter from prose |
| Phase 3 -- SHARING RULE VERDICT blocks per role | FM-SKILL-2 (sharing below role scope) + FM-P4: Sharing/FLS intersection missed by role analysis |
| Phase 4 -- coverage gate with named artifact verification | FM-P5: Coverage loss at phase transition before synthesis begins |
| Named exit gate artifact declarations at end of each phase | FM-SKILL-4 (output-schema drift) + FM-P6: C-11 input references match coincidental names not declared contracts |
| Aggregation routing rules naming sentinel type and Phase 6 inventory destination | FM-SKILL-5 (routing gap) + FM-P7: Traversal discoveries lost at aggregation step |
| Phase 6 -- SENTINEL INVENTORY aggregated from inline sentinels | FM-SKILL-5 + FM-P8: Gap inventory re-created from memory, not routed from logged tokens |
| SECURITY STATE REGISTER + inertia carry-forward rule | FM-SKILL-3 (verdict drift) + FM-P9: Phase-transition verdict reset |
| Phase 7 -- SHALL cross-role differential | FM-SKILL-2 (cumulative scope blindness) + FM-P10: Differential omitted when per-role analysis finds no individual anomaly |
| Phase 8 -- exact Dataverse object remediation | FM-P11: Generic advice non-actionable without additional analysis |

---

**SECURITY GAP REGISTER -- assign [G-##] at point of discovery. Never defer.**

| ID | Sentinel Token | Entity | Field / Operation | Role(s) | Gap Type | Risk | Source Phase |
|----|---------------|--------|-------------------|---------|----------|------|-------------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH

**Sentinel token vocabulary:**
- `[GAP-FLS-fieldname]` -- placed inline at the FLS gap discovery row
- `[GAP-ESC-vectorname]` -- placed inline at a POSSIBLE escalation vector row
- `[GAP-SHARE-rulename]` -- placed inline at a sharing conflict verdict row
- `[SCOPE AMBIGUOUS]` -- placed inline where BU scope cannot be assessed from provided context
- `[UNCHECKED]` -- placed inline where a vector cannot be evaluated from provided context

**Sentinel placement rule:** Every sentinel MUST be placed inline at the exact point of discovery. Do not batch at section end or invent at summary time.

---

**SECURITY STATE REGISTER -- authoritative per-role verdict record. Updated by every phase.**

| Role | Phase Last Updated | Current Verdict | Active Sentinel Tokens | Active Gap IDs |
|------|--------------------|-----------------|----------------------|----------------|

Verdict values: `CLEARED` / `FLAGGED [sentinels, G-##]` / `PENDING-PHASE-[N]`

**Inertia rule:** Every verdict from Phase N is the persistent default entering Phase N+1. When a phase finds nothing new for a role:
`[Role] -- INERTIA: [verdict] from Phase [N], no new finding this phase.`
Required for every role in every phase. Absence = verdict unknown = detectable format failure.

**Phase dependency protocol:** Each phase declares its required inputs by artifact name. A phase SHALL NOT proceed without its declared inputs present.

---

### PHASE 1 -- Inventory

> **Structural purpose:** Prevents FM-P1 (incomplete coverage). **Inertia initialization:** All roles set to `PENDING-PHASE-2` after catalogs complete.

**Input required:** System description from provided context.

**1.1 -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

Sensitivity: High (PII, financial, credentials, health) / Medium (internal-only, cross-BU risk) / Low

**1.2 -- Role catalog:**

| Role | Type (Stock / Custom / Team / Env) | Business Unit Scope | Purpose | Has Write? | Column Security Profiles Attached |
|------|-------------------------------------|---------------------|---------|------------|----------------------------------|

Stock roles to check: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 -- Scope pre-assessment:** For each role, state whether the assigned BU scope is appropriate for its stated purpose or over-permissioned. Place `[SCOPE AMBIGUOUS]` inline if undeterminable. Assign [G-##] for any `[SCOPE AMBIGUOUS]` placement.

**1.4 -- Initialize SECURITY STATE REGISTER:** Set all roles to `PENDING-PHASE-2`.

**1.5 -- Analysis order:** "I will trace entities in this order: [list, highest sensitivity first]. First gap ID: G-01."

**PHASE 1 EXIT GATE -- this phase produces:**

> **ENTITY CATALOG** (entity name | org-wide default | sensitivity | reason for sensitivity)
> **ROLE CATALOG** (role name | type | BU scope | purpose | has write? | column security profiles)

Phase 2 SHALL reference ENTITY CATALOG from Phase 1 and ROLE CATALOG from Phase 1 by these exact names. A Phase 2 that begins without naming both artifacts is a dependency failure.

---

### PHASE 2 -- Per-Entity Trace

> **Structural purpose:** Prevents FM-SKILL-1 (FLS post-incident discovery) + FM-P3 (verdict scatter). **Inertia requirement:** SECURITY STATE REGISTER updated after every entity section -- new sentinel: FLAGGED; no finding: explicit carry-forward. Every role must appear.

**Input required:** ENTITY CATALOG from Phase 1. ROLE CATALOG from Phase 1.
**Dependency check:** If either named artifact is incomplete, name the missing content before proceeding.

For each entity (highest sensitivity first):

**2a -- Operations per role:**

| Entity | Role | Create | Read | Write | Delete | Record Scope |
|--------|------|--------|------|-------|--------|--------------|

**2b -- Sensitive field FLS status:**

Place sentinel inline at the discovery row. Then assign [G-##].

| Entity | Field | Sensitivity | FLS Profile (YES/NO/UNKNOWN) | Role | Can Read? | Can Write? | Sentinel |
|--------|-------|-------------|------------------------------|------|-----------|------------|---------|

Gap rule: High/Medium sensitivity + NO FLS profile + role has Read -> place `[GAP-FLS-fieldname]` inline, assign [G-##]. Gap Type = MISSING-FLS. Risk = CRITICAL.

**Routing rule -- FLS sentinels:** Any `[GAP-FLS-*]` sentinel placed in this table MUST have a [G-##] in the SECURITY GAP REGISTER AND MUST appear in Phase 6 SENTINEL INVENTORY by sentinel token name. A sentinel without a [G-##] is a routing failure.

**2c -- Escalation path check (Write roles only):**

| Vector | Roles | Verdict | Sentinel (if POSSIBLE) | Evidence |
|--------|-------|---------|----------------------|----------|
| Record Assign | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-assign]` | |
| Share to higher-privilege role | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-share]` | |
| Field modification affecting role/BU | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-field-modify]` | |
| Team self-addition | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-team-self]` | |
| Admin role override | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-admin-override]` | |

NOT POSSIBLE requires naming the ruling-out check -- not a bare assertion. POSSIBLE: place sentinel inline, assign [G-##].

**Routing rule -- escalation sentinels:** Any `[GAP-ESC-*]` sentinel MUST have a [G-##] AND MUST appear in Phase 6 SENTINEL INVENTORY by token name.

**2d -- SECURITY STATE UPDATE (required for every role after every entity):**
- Sentinel placed: `[Role] -- FLAGGED [sentinel token, G-##]. Source: Phase 2 / [Entity].`
- No finding: `[Role] -- INERTIA: [prior verdict], no finding on [Entity].`

**PHASE 2 EXIT GATE -- this phase produces:**

> **ACCESS MATRIX** (entity | role | create | read | write | delete | record scope -- all roles x all entities)
> **FLS SENTINEL TABLE** (entity | field | sensitivity | FLS profile | role | can read | sentinel token | G-##)
> **ESCALATION FINDINGS** (entity | vector | roles | verdict | sentinel token | G-##)

Phase 3 SHALL reference ACCESS MATRIX from Phase 2, FLS SENTINEL TABLE from Phase 2, and ESCALATION FINDINGS from Phase 2 by these exact names.

---

### PHASE 3 -- Sharing Rule Analysis

> **Structural purpose:** Prevents FM-SKILL-2 (sharing below role scope) + FM-P4 (sharing/FLS intersection gap). **Inertia requirement:** SECURITY STATE REGISTER updated after each SHARING RULE VERDICT.

**Input required:** ROLE CATALOG from Phase 1. ACCESS MATRIX from Phase 2. ESCALATION FINDINGS from Phase 2.
**Dependency check:** If any named artifact is incomplete, name the missing content before proceeding.

For each role, produce a SHARING RULE VERDICT block:

#### SHARING RULE VERDICT: [Role name]

| Entity | Sharing Rules Found? | Rule Name | Access Expanded Beyond OWD+Role? | Verdict | Sentinel |
|--------|---------------------|-----------|----------------------------------|---------|---------|

Verdict:
- `"Confirmed: no rules expand [Role] access on [Entity]. OWD=[value], scope=[scope]. Method: [audit method]."`
- `"CONFLICT FOUND: [Rule] grants [Role] access to [record set]. Exceeds design intent: [reason]."` Place `[GAP-SHARE-rulename]` inline. Assign [G-##], Gap Type = SHARING-CONFLICT.

Every entity in ACCESS MATRIX from Phase 2 that this role touches must appear. Silent omissions fail.

**Routing rule -- sharing sentinels:** Any `[GAP-SHARE-*]` sentinel MUST have a [G-##] AND MUST appear in Phase 6 SENTINEL INVENTORY by token name.

**SECURITY STATE UPDATE after each SHARING RULE VERDICT:**
- Conflict: `[Role] -- FLAGGED [GAP-SHARE-*, G-##]. Source: Phase 3 / [Entity].`
- No conflict: `[Role] -- INERTIA: [verdict] from Phase 2, sharing clean on [entity list].`

**PHASE 3 EXIT GATE -- this phase produces:**

> **SHARING VERDICTS** (role | entity | sharing rules found | access expanded | verdict | sentinel token | G-##)

Phase 4 SHALL reference SHARING VERDICTS from Phase 3 by this exact name.

---

### PHASE 4 -- Coverage Gate

> **Structural purpose:** Prevents FM-P5 (phase-transition coverage loss). **Security state consistency gate:** Zero PENDING-PHASE entries before Phase 5.

**Input required:** ACCESS MATRIX from Phase 2. FLS SENTINEL TABLE from Phase 2. ESCALATION FINDINGS from Phase 2. SHARING VERDICTS from Phase 3.
**Dependency check:** If any named artifact is missing or incomplete, stop before proceeding.

| Role | ACCESS MATRIX: All Entities? | SHARING VERDICTS Written? | State Register Non-PENDING? | Current Verdict | Active Sentinels |
|------|------------------------------|--------------------------|----------------------------|-----------------|-----------------|

Gate assertion: "All [N] entities in ACCESS MATRIX. All [N] roles have SHARING VERDICTS. Zero PENDING-PHASE entries in SECURITY STATE REGISTER. Total [G-##]: [N]. Total sentinels placed: [types and counts]. Proceeding to Phase 5."

Stop condition: PENDING-PHASE entry or missing SHARING VERDICT -- resolve before continuing.

**PHASE 4 EXIT GATE -- this phase produces:**

> **COVERAGE GATE CONFIRMATION** (all-entities-traced: YES | all-sharing-verdicts: YES | state-consistent: YES | total gaps: N | total sentinels: N)

Phase 5 SHALL reference COVERAGE GATE CONFIRMATION from Phase 4.

---

### PHASE 5 -- Cross-Entity Cascade

> **Structural purpose:** Prevents FM-SKILL-2 (relationship-derived access) + FM-P5 (single-entity tunnel vision). **Inertia requirement:** Roles not involved in cascade carry forward Phase 4 verdict.

**Input required:** ACCESS MATRIX from Phase 2. COVERAGE GATE CONFIRMATION from Phase 4.

**5a -- Relationship map (two highest-sensitivity entities):**

| Source | Relationship Type | Target | Cascade Behavior |
|--------|-------------------|--------|-----------------|

**5b -- Cascade access trace:**

`[Role] -> [Source, access, scope] -> [Relationship + cascade] -> [Target, resulting access]` -> INTENTIONAL or EMERGENT

EMERGENT: place `[GAP-ESC-cascade-[entity]]` inline. Assign [G-##], Gap Type = CASCADE-OVERREACH.

**Routing rule -- cascade sentinels:** Any `[GAP-ESC-cascade-*]` sentinel MUST have a [G-##] AND MUST appear in Phase 6 SENTINEL INVENTORY as a Phase 5 addition.

**5c -- SECURITY STATE UPDATE:**
- Cascade gap: `[Role] -- FLAGGED [GAP-ESC-cascade-*, G-##]. Source: Phase 5.`
- No finding: `[Role] -- INERTIA: [verdict] from Phase 4, no cascade finding.`

**PHASE 5 EXIT GATE -- this phase produces:**

> **CASCADE FINDINGS** (role | source | relationship | target | INTENTIONAL/EMERGENT | sentinel token | G-##)

---

### PHASE 6 -- Sentinel Inventory

> **Structural purpose:** Prevents FM-SKILL-5 (routing gap) + FM-P8 (gap inventory re-created from memory). Aggregate all discovery-point tokens. The gap list derives from this inventory -- not from memory.

**Input required:** FLS SENTINEL TABLE from Phase 2. ESCALATION FINDINGS from Phase 2. SHARING VERDICTS from Phase 3. CASCADE FINDINGS from Phase 5. SECURITY GAP REGISTER (all [G-##] rows).

**6a -- SENTINEL INVENTORY (complete aggregation):**

List every sentinel placed in Phases 1-5, in phase order:

| Sentinel Token | Type | Phase Placed | Entity | Field / Operation | Role(s) | G-## |
|---------------|------|-------------|--------|------------------|---------|------|

**Routing verification (mandatory before 6b):**
- "Total `[GAP-FLS-*]` placed: [N]. All in inventory: [YES/NO]."
- "Total `[GAP-ESC-*]` placed: [N]. All in inventory: [YES/NO]."
- "Total `[GAP-SHARE-*]` placed: [N]. All in inventory: [YES/NO]."
- "Total `[SCOPE AMBIGUOUS]` placed: [N]. All in inventory: [YES/NO]."
- "Total `[UNCHECKED]` placed: [N]. All in inventory: [YES/NO]."
- "Total [G-##] in SECURITY GAP REGISTER: [N]. All referenced in inventory: [YES/NO]."

If any answer is NO: name the missing token and its source phase. Do not proceed until reconciled.

**6b -- Aggregate gap list (derived from SENTINEL INVENTORY):**

| Gap ID | Sentinel Token | Type | Entity | Field / Operation | Role(s) | Risk | Source Phase | Remediation |
|--------|---------------|------|--------|------------------|---------|------|-------------|-------------|

Each row traces to an entry in the SENTINEL INVENTORY above.

**PHASE 6 EXIT GATE -- this phase produces:**

> **SENTINEL INVENTORY** (all sentinel tokens | type | phase | entity | role | G-##)
> **AGGREGATE GAP LIST** (G-## | sentinel token | type | entity | role | risk | source phase)

Phase 7 SHALL reference AGGREGATE GAP LIST from Phase 6 by this exact name.

---

### PHASE 7 -- Cross-Role Differential Analysis (SHALL-enforced)

> **Structural purpose:** Prevents FM-SKILL-2 (cumulative scope blindness) + FM-P10 (differential omitted when per-role analysis finds no individual anomaly). **Inertia requirement:** SECURITY STATE REGISTER verdicts are authoritative. This phase does not re-derive verdicts from scratch.

**Input required:** ACCESS MATRIX from Phase 2. SECURITY STATE REGISTER current state. ROLE CATALOG from Phase 1.

**SHALL instructions -- structural requirements, not guidelines:**

The model **SHALL** compare access differentials across all roles in ROLE CATALOG from Phase 1 for each operation in ACCESS MATRIX from Phase 2.

For each role pair, the model **SHALL** state an explicit conclusion -- one of:
- `EXPECTED DIFFERENTIAL -- [Role A] has [specific named access] that [Role B] does not because [reason tied to Role A's stated purpose]. The differential is consistent with the roles' design intent.`
- `CANDIDATE OVER-PERMISSION -- [Role A] has [specific named access] that exceeds what [Role A's stated purpose] requires relative to [Role B]. Access in question: [named operation or field]. This is a candidate for tightening.`

The model **SHALL NOT** conclude "differential appears expected" without naming the specific access elements compared and the purpose statement justifying the assessment.

The model **SHALL** process every role pair. For N roles: N*(N-1)/2 assessments required.

The model **SHALL** assign `[GAP-ESC-overpermission-[role]]` and [G-##] for every CANDIDATE OVER-PERMISSION. Gap Type = BU-SCOPE. Add to AGGREGATE GAP LIST from Phase 6 as Phase 7 addition.

**Differential Analysis Table:**

| Role Pair | Entity | Operation | Role A Access | Role B Access | Conclusion |
|-----------|--------|-----------|--------------|--------------|------------|

Conclusion cell: full statement -- not a verdict code.

**SECURITY STATE UPDATE:** CANDIDATE OVER-PERMISSION -> `FLAGGED [sentinel, G-##]. Source: Phase 7.` No finding -> carry-forward notation.

---

### PHASE 8 -- Remediation and Defense-in-Depth

> **Structural purpose:** Prevents FM-P11 (non-actionable remediation). Every gap resolved with an exact Dataverse configuration object.

**Input required:** AGGREGATE GAP LIST from Phase 6 (updated with Phase 7 additions).

**8a -- Gap remediation (cite by [G-##] and sentinel token):**

For each row in AGGREGATE GAP LIST from Phase 6:

`[G-##] [sentinel token]: Apply [specific change] to [exact Dataverse configuration object] in [solution location]. Current state: [what exists today]. Target state: [what it should be]. Post-fix behavior: [what a user can / cannot do].`

Exact Dataverse configuration objects required: column security profile name (not "add FLS"), security role privilege name + table name (not "tighten the role"), team type (owner/access) + membership rule (not "fix team membership"), sharing rule name (not "remove the rule"), OWD value per entity (not "adjust OWD"). Generic advice fails.

**8b -- Defense-in-depth assessment (two highest-sensitivity entities):**

| Entity | Layer 1: Env / Admin Role | Layer 2: Security Role + BU Scope | Layer 3: Team Membership | Layer 4: FLS / Column Security Profile | Effective Enforcement Layer |
|--------|--------------------------|----------------------------------|--------------------------|---------------------------------------|----------------------------|

Effective Enforcement Layer: the lowest layer that independently enforces access without relying on upper layers. For at least one operation on at least one entity: explain why upper layers do not override it.

**8c -- Stock role summary:**

For each stock Dataverse role present in ROLE CATALOG from Phase 1: baseline privileges, how modified in this scenario, whether necessary or removable.

**Final SECURITY STATE REGISTER:** Copy in final form. Every role must have `CLEARED` or `FLAGGED [sentinel list, G-## list]`. No PENDING-PHASE entries permitted.

---

## Variation Axis Summary

| Variation | C-18 | C-19 | C-12 | C-13 | C-11 | C-14 | C-15 | C-16 | C-17 | Base |
|-----------|------|------|------|------|------|------|------|------|------|------|
| V-01 | TARGETED | -- | -- | -- | INHERITS R6-V1 | -- | -- | -- | -- | R6 V-01 two-pass |
| V-02 | -- | TARGETED | -- | -- | INHERITS R6-V3 | -- | -- | -- | -- | R6 V-03 lifecycle |
| V-03 | TARGETED | TARGETED | partial | -- | TARGETED | -- | -- | -- | -- | R6 V-03 lifecycle |
| V-04 | TARGETED | TARGETED | TARGETED | TARGETED | TARGETED | TARGETED | -- | -- | -- | R4 V-04 |
| V-05 | TARGETED | TARGETED | TARGETED | TARGETED | TARGETED | TARGETED | TARGETED | TARGETED | TARGETED | R4 V-05 |

**Key additions vs best prior baselines:**

- **C-12 (inline sentinels):** Added to V-04 and V-05. Named token types [GAP-FLS-*], [GAP-ESC-*], [GAP-SHARE-*], [SCOPE AMBIGUOUS], [UNCHECKED] placed inline at discovery. Each has a corresponding routing rule and a Phase 6 SENTINEL INVENTORY target.

- **C-18 (exit gate declarations):** Added to V-01, V-03, V-04, V-05. Each phase ends with "This phase produces: ARTIFACT (schema)". The declared name becomes the canonical token for downstream C-11 input declarations. In V-01 this converts the previously coincidental C-11 pass into a contract-enforced pass.

- **C-19 (aggregation routing rules):** Added to V-02, V-03, V-04, V-05. Each discovery section has a routing rule naming both (a) the discovery mechanism by token type or flag value and (b) the aggregation destination by name. V-05 uses sentinel tokens as routing targets; V-02 and V-03 use [G-##] IDs and row flags.

**Predicted scoring (rubric v5, max 117.5):**

| Variation | Essential | Rec | Key aspirational passes | Predicted |
|-----------|-----------|-----|-------------------------|-----------|
| V-01 | 60 | 30 | C-09 PARTIAL, C-10 PASS, C-11 PASS, C-18 PASS | ~98.75 |
| V-02 | 60 | 30 | C-09 PARTIAL, C-10 PARTIAL, C-11 PASS, C-19 PASS | ~97.5 |
| V-03 | 60 | 30 | C-09 PARTIAL, C-10 PASS, C-11 PASS, C-18 PASS, C-19 PASS | ~101.25 |
| V-04 | 60 | 30 | C-09 PARTIAL, C-10 PASS, C-11-C-14 PASS, C-18 PASS, C-19 PASS | ~108.75 |
| V-05 | 60 | 30 | all 11 aspirational PASS | 117.5 |
