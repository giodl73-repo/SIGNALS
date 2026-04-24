content = """\
# trace-permissions Variate — Round 4 (Rubric v4)
**Date:** 2026-03-16
**Rubric:** v4 (C-01 through C-17)
**New criteria targeted this round:** C-13 (security state persistence / inertia framing), C-14 (failure mode enumeration per phase), C-15 (pre-phase failure mode catalog), C-16 (SHALL-level cross-role differential enforcement), C-17 (skill-level threat model in CONTEXT)
**R3 structural baseline retained:** Entity catalog, role catalog, gap register [G-##] assigned at discovery, sharing rule verdict blocks per role, phase gate coverage check, remediation naming exact Dataverse configuration object

---

## Round 4 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Security state persistence -- inertia framing (C-13 single-axis) | Adding a SECURITY STATE REGISTER with mandatory carry-forward notation ("INERTIA: [verdict] from Phase N, no new finding") prevents verdict drift by making it structurally visible: a phase that omits carry-forward for any role is treating that role's verdict as unknown, which is a detectable format failure -- not a silent omission |
| V-02 | Failure mode enumeration -- per-phase annotation (C-14 single-axis) | Annotating each phase with a named structural purpose block ("Structural purpose: prevents [failure mode]") makes the phase choice legible and testable; a reader can verify that the structure actually prevents the named failure, and a model that skips a phase loses its failure mode defense visibly |
| V-03 | SHALL-level cross-role differential enforcement (C-16 single-axis) | Replacing descriptive comparison guidance with explicit SHALL instructions -- naming the comparison required, the conclusion required for each pair, and the disposition (EXPECTED DIFFERENTIAL vs CANDIDATE OVER-PERMISSION) -- elevates C-10 from emergent-PARTIAL (data present, comparison derivable) to enforced-PASS (analysis structurally required regardless of whether individual role analysis found issues) |
| V-04 | Combined: inertia framing (C-13) + failure mode enumeration per phase (C-14) | Pairing per-phase failure mode annotations with inertia framing creates dual reinforcement: the model knows WHY each phase exists and must explicitly carry verdicts forward to prove the chain is not broken; a model that collapses phases loses both the failure mode defense and the inertia continuity in the same structural move |
| V-05 | Full combination: C-13 + C-14 + C-15 + C-16 + C-17 | Providing a skill-level threat model in CONTEXT (C-17), followed by a FAILURE MODE MAP before Phase 1 (C-15), with per-phase failure mode annotations (C-14), inertia framing throughout (C-13), and SHALL-enforced differential analysis (C-16) makes structural omissions detectable at three levels simultaneously: skill-level (CONTEXT explains why the structure exists), catalog-level (FAILURE MODE MAP lists what each phase defends before any phase begins), and phase-level (inline annotations confirm the defense is active at each step) |

---

## V-01 -- Security State Persistence: Inertia Framing

**Axis:** Security state persistence / inertia framing (C-13 single-axis)
**Hypothesis:** The failure mode C-13 targets -- verdict drift -- is silent by default: a phase that re-evaluates a role from scratch produces a verdict that may or may not match the prior verdict, and if it differs, no structural element flags the inconsistency. Introducing a SECURITY STATE REGISTER that requires explicit carry-forward notation for every role in every phase makes drift structurally visible. A phase that omits carry-forward for a role is detectable as a coverage gap, not a silent omission.

---

You are running a permissions trace signal for: **{{topic}}**

---

**SECURITY GAP REGISTER -- assign [G-##] identifiers sequentially starting at G-01. Add rows as gaps are found. Never defer.**

| ID | Entity | Field / Operation | Role(s) | Gap Type | Risk | Status |
|----|--------|-------------------|---------|----------|------|--------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH
Risk: CRITICAL / HIGH / MEDIUM

---

**SECURITY STATE REGISTER -- the authoritative per-role verdict record. Every phase updates this or writes a carry-forward entry.**

| Role | Phase Last Updated | Current Verdict | Active Gap IDs | Notes |
|------|--------------------|-----------------|----------------|-------|

Verdict values: `CLEARED` / `FLAGGED [G-##, G-##]` / `PENDING-PHASE-[N]`

**Inertia rule:** When a phase completes analysis for a role and finds nothing new, write:
`[Role] -- INERTIA: [prior verdict] from Phase [N], no new finding this phase.`
This notation is required. A phase that omits carry-forward notation for any role is treating that role's verdict as unknown -- a format failure detectable by the absence of the entry.

---

### PHASE 1 -- Inventory

**1.1 -- Entity catalog:**

List every entity that {{topic}} creates, reads, updates, or deletes.

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

Sensitivity: High (PII, financial, credentials, health) / Medium (internal-only, cross-BU risk) / Low (lookup, reference, configuration)

**1.2 -- Role catalog:**

List every security role, team, and environment role present in this scenario.

| Role | Type (Stock / Custom / Team / Env) | Business Unit Scope | Purpose | Has Write? |
|------|-------------------------------------|---------------------|---------|------------|

Stock roles to check: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 -- Security state initialization:**

After completing the catalogs, initialize the SECURITY STATE REGISTER with all roles set to `PENDING-PHASE-2`. Update the register here with this baseline entry before proceeding.

---

### PHASE 2 -- Per-Entity Trace

**Instruction: Complete all sub-steps for one entity, then advance to the next. Log gaps to the SECURITY GAP REGISTER immediately -- do not defer. Update the SECURITY STATE REGISTER after each entity section before moving to the next.**

---

#### Entity: [name] (Sensitivity: [level])

**2a -- Operations per role:**

| Entity | Role | Create | Read | Write | Delete | Record Scope |
|--------|------|--------|------|-------|--------|--------------|

**2b -- Field-level security for sensitive fields:**

| Entity | Field | Sensitivity | FLS Profile (YES/NO/UNKNOWN) | Role | Can Read? | Can Write? |
|--------|-------|-------------|------------------------------|------|-----------|------------|

Rule: A sensitive field with no FLS profile is readable by any role with entity-level Read. If a role can read a High-sensitivity field with no FLS profile: assign a [G-##] immediately. Gap Type = MISSING-FLS. Risk = CRITICAL.

**2c -- Escalation path check (Write roles only):**

| Vector | Roles Checked | Verdict | Evidence |
|--------|---------------|---------|----------|
| Record Assign | ... | POSSIBLE / NOT POSSIBLE | ... |
| Share to higher-privilege role | ... | POSSIBLE / NOT POSSIBLE | ... |
| Field modification affecting role/BU | ... | POSSIBLE / NOT POSSIBLE | ... |
| Team self-addition | ... | POSSIBLE / NOT POSSIBLE | ... |

POSSIBLE vectors: assign [G-##]. Gap Type = ESCALATION-PATH.

**2d -- Security state update for this entity:**

For each role: did this entity section produce a new finding?
- New gap found: update SECURITY STATE REGISTER to `FLAGGED [G-##]`. Source: Phase 2 / [Entity].
- No new finding: write carry-forward notation: `[Role] -- INERTIA: [prior verdict] from Phase 1 init, no new finding on [Entity].`

Every role in the Role Catalog must appear in this update block. Omitting a role is a coverage failure.

---

[Repeat Phase 2 for each entity in sensitivity order]

---

### PHASE 3 -- Sharing Rule Analysis

**Instruction: Complete the SHARING RULE VERDICT block for one role, update the SECURITY STATE REGISTER, then advance to the next role.**

---

#### SHARING RULE VERDICT: [Role name]

For each entity this role touches, state the sharing rule verdict explicitly:

| Entity | Sharing Rules Found? | Rule Name (if any) | Access Expanded Beyond OWD+Role? | Verdict |
|--------|---------------------|-------------------|----------------------------------|---------|

Verdict options:
- `"Confirmed: no sharing rules expand [Role] access on [Entity]. Checked: [method]. Basis: OWD=[value], role scope=[scope]. No criteria-based or manual sharing applies."`
- `"CONFLICT FOUND: [Rule] expands [Role] access on [Entity] to [record set]. Exceeds design intent because [reason]. Assigned [G-##]. Gap Type = SHARING-CONFLICT."`

Every entity in the role catalog's "Has Write?" list must appear. A role with no entity coverage fails this block.

**Security state update after this sharing verdict:**
- Conflict found: update SECURITY STATE REGISTER to `FLAGGED [new G-##]`. Source: Phase 3 / [Entity].
- No conflict: `[Role] -- INERTIA: [prior verdict] from Phase 2, sharing confirmed clean on [entity list].`

---

[Repeat SHARING RULE VERDICT + security state update for each role]

---

### PHASE 4 -- Phase Gate: Coverage Check

Before advancing to cross-entity analysis, verify coverage:

**Gate table:**

| Role | Phase 2 SECURITY STATE Updated? | Phase 3 SHARING VERDICT Written? | Phase 3 SECURITY STATE Updated? | Current Verdict | Active Gaps |
|------|----------------------------------|----------------------------------|----------------------------------|-----------------|-------------|

**Gate assertion:** "All [N] roles have security state entries from Phase 2. All [N] roles have sharing verdicts from Phase 3. SECURITY STATE REGISTER is consistent -- no role has a PENDING-PHASE entry that was not resolved. Total gaps in register: [N]. Proceeding to Phase 5."

If any role has a PENDING-PHASE entry that was not updated: stop. Name the role and the missing update before continuing.

---

### PHASE 5 -- Cross-Entity Cascade

**5a -- Relationship map (two highest-sensitivity entities):**

| Source | Relationship Type | Target | Cascade Behavior |
|--------|-------------------|--------|-----------------|

**5b -- Cascade access trace:**

`[Role] -> [Source, access level, scope] -> [Relationship + cascade] -> [Target, access level resulting]`

State at each hop: INTENTIONAL or EMERGENT. EMERGENT access exceeding direct grant: assign [G-##]. Gap Type = CASCADE-OVERREACH.

**5c -- Security state carry-forward:**

For every role: did Phase 5 produce a cascade finding?
- New gap: update SECURITY STATE REGISTER. Source: Phase 5.
- No new finding: `[Role] -- INERTIA: [prior verdict] from Phase 3/4, no cascade finding.`

---

### PHASE 6 -- Remediation and Defense-in-Depth

**6a -- Gap remediation (cite by [G-##]):**

For each row in the SECURITY GAP REGISTER:

`[G-##]: Apply [specific change] to [role / FLS profile / sharing rule / OWD / team config] in [solution location]. Current state: [what exists]. Target state: [what it should be]. After fix: [what a user can / cannot do].`

Generic advice does not qualify. Remediation must name the exact Dataverse configuration object.

**6b -- Defense-in-depth assessment:**

| Entity | Security Role: Independent? | FLS: Independent? | Record Scope: Independent? | Single Point of Failure? |
|--------|---------------------------|-------------------|---------------------------|-------------------------|

**6c -- Final security state:**

Copy the SECURITY STATE REGISTER here in its final form. Every role must have a `CLEARED` or `FLAGGED [G-##]` verdict. No PENDING entries permitted in the final state. This is the authoritative security output.

---

## V-02 -- Lifecycle Emphasis: Per-Phase Failure Mode Annotation

**Axis:** Lifecycle emphasis -- each phase carries an inline structural purpose block naming the failure mode it prevents (C-14 single-axis)
**Hypothesis:** Phase-by-phase structural motivation (C-14) produces legible, testable prompt design: a reader can verify that each phase's structure actually prevents its named failure. A model that skips or merges phases loses its failure mode defense visibly -- the missing annotation is itself a gap signal. This differs from C-15's pre-phase catalog: here the failure mode motivation is discovered as each phase is reached, not assembled into a catalog that precedes Phase 1.

---

You are running a permissions trace signal for: **{{topic}}**

---

**SECURITY GAP REGISTER -- assign [G-##] identifiers sequentially starting at G-01. Add rows at the moment of discovery. Never batch or defer.**

| ID | Entity | Field / Operation | Role(s) | Gap Type | Risk |
|----|--------|-------------------|---------|----------|------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH

---

### PHASE 1 -- Inventory and Analysis Order

> **Structural purpose:** Prevents incomplete role and entity coverage -- the failure mode where analysis proceeds on an assumed set that excludes system roles, environment roles, team-inherited access, or low-salience entities, causing access verdicts to be wrong from Phase 2 onward. The inventory phase exists because incorrect coverage is undetectable once analysis begins; it must be fixed before the first verdict is issued.

**1.1 -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

**1.2 -- Role catalog:**

List every security role, team, and environment role with any privilege in this scenario.

| Role | Type (Stock / Custom / Team / Env) | Business Unit Scope | Purpose | Has Write? |
|------|-------------------------------------|---------------------|---------|------------|

Stock roles to check: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 -- Analysis order declaration:**

Order entities from highest to lowest sensitivity. State: "I will trace entities in this order: [list]. First gap ID: G-01."

---

### PHASE 2 -- Per-Entity Trace

> **Structural purpose:** Prevents verdict scatter -- the failure mode where access conclusions are embedded inline in prose across multiple sections, making them impossible to audit, compare across roles, or use as structured input for escalation and sharing analysis. Entity-by-entity organization with explicit operation/FLS tables makes verdicts referenceable artifacts, not prose side-effects.

**Input required:** Entity catalog from Phase 1 (ordered by sensitivity). Role catalog from Phase 1.
**Dependency check:** If Phase 1 is incomplete, name the missing roles or entities before proceeding.

For each entity (highest sensitivity first):

**2a -- Operations per role (complete for every role x entity combination):**

| Entity | Role | Create | Read | Write | Delete | Record Scope |
|--------|------|--------|------|-------|--------|--------------|

**2b -- Sensitive field FLS status:**

| Entity | Field | Sensitivity | FLS Profile (YES/NO/UNKNOWN) | Role | Can Read? |
|--------|-------|-------------|------------------------------|------|-----------|

MISSING-FLS gap rule: sensitive field + no FLS profile + role has Read = assign [G-##] immediately.

**2c -- Escalation path check (Write roles only):**

| Vector | Roles | Verdict | Evidence |
|--------|-------|---------|----------|

POSSIBLE verdict: assign [G-##], Gap Type = ESCALATION-PATH.

---

### PHASE 3 -- Sharing Rule Analysis

> **Structural purpose:** Prevents the sharing/FLS intersection gap -- the failure mode where record-level sharing overrides field-level security verdicts, producing effective field access that role analysis alone would not predict. Dataverse sharing rules (manual, team-based, Power Automate) are evaluated separately from role privileges because they operate at the record layer, below security role scope and independent of FLS. Phase 2 cannot catch this; Phase 3 exists because it cannot.

**Input required:** Role catalog from Phase 1. Entity catalog from Phase 1. Gap register current state from Phase 2.

For each role, produce a SHARING RULE VERDICT block:

#### SHARING RULE VERDICT: [Role name]

| Entity | Sharing Rules Found? | Rule Name | Access Expanded Beyond OWD+Role? | Verdict |
|--------|---------------------|-----------|----------------------------------|---------|

- Every entity the role touches must appear -- no silent omissions.
- CONFLICT FOUND: assign [G-##], Gap Type = SHARING-CONFLICT.
- No conflict: name the OWD value, role record scope, and confirmation method.

---

### PHASE 4 -- Phase Gate: Coverage Check

> **Structural purpose:** Prevents phase-transition coverage loss -- the failure mode where the analysis moves from traversal to synthesis without confirming that all roles and entities were actually covered; gaps discovered in Phases 2-3 that were not logged to the register are silently lost. The gate forces an explicit accounting before cross-entity analysis begins.

**Input required:** All Phase 2 entity sections. All Phase 3 sharing rule verdicts.

| Role | All Entities Covered in Phase 2? | Sharing Verdict Written (Phase 3)? | Gaps Found (N) |
|------|----------------------------------|-------------------------------------|----------------|

Gate assertion: "All [N] entities traced in Phase 2. All [N] roles have sharing verdicts. Total gaps in register: [N]. Proceeding to Phase 5."

---

### PHASE 5 -- Cross-Entity Cascade

> **Structural purpose:** Prevents single-entity tunnel vision -- the failure mode where access is analyzed entity by entity, but relationships between entities create cascade access paths that no single-entity analysis predicts. A role with Read on an Account entity and the Account-Contact relationship has effective access to Contact records even if the Contact entity section showed DENY.

**Input required:** Phase 2 operation verdicts. Phase 4 gate confirmation.

**5a -- Relationship map:**

| Source | Relationship | Target | Cascade Behavior |
|--------|-------------|--------|-----------------|

**5b -- Cascade trace:**

`[Role] -> [Source, access, scope] -> [Relationship + cascade] -> [Target, resulting access]` -> INTENTIONAL or EMERGENT

EMERGENT access exceeding direct grant: assign [G-##], Gap Type = CASCADE-OVERREACH.

---

### PHASE 6 -- Remediation and Defense-in-Depth

> **Structural purpose:** Prevents generic remediation -- the failure mode where gap inventory entries are resolved with "add FLS" or "tighten role" advice that cannot be implemented without additional analysis, leaving the fix non-actionable. Remediation specificity is enforced here by requiring the exact Dataverse configuration object for each gap.

**Input required:** All [G-##] entries from the SECURITY GAP REGISTER.

**6a -- Gap remediation (cite by [G-##]):**

`[G-##]: Apply [specific change] to [exact Dataverse object] in [solution location]. Current state: [...]. Target state: [...]. Post-fix behavior: [...].`

Exact Dataverse objects: column security profile name, security role privilege + table, team type and membership rule, sharing rule name, OWD setting per entity.

**6b -- Defense-in-depth assessment:**

| Entity | Security Role Layer: Independent? | FLS Layer: Independent? | Record Scope Layer: Independent? | Single Point of Failure? |
|--------|-----------------------------------|------------------------|----------------------------------|-------------------------|

**6c -- Stock role summary:**

For each stock Dataverse role present: baseline privileges, modified how, necessary or removable.

---

### PHASE 7 -- Cross-Role Differential

> **Structural purpose:** Prevents differential blindness -- the failure mode where per-role analysis is internally correct but cross-role comparisons that would surface anomalous divergence are never performed. A role that is individually correct may still be over-permissioned relative to its peer roles, and this is only visible when roles are compared side-by-side.

**Input required:** Phase 2 operation verdicts per role. Role catalog from Phase 1.

For at least two roles, compare access side-by-side on the same operation set:

| Role Pair | Operation | Role A Access | Role B Access | Differential | Assessment |
|-----------|-----------|--------------|--------------|--------------|------------|

Assessment: `EXPECTED DIFFERENTIAL -- [explain why the difference matches stated purposes]` or `CANDIDATE OVER-PERMISSION -- [explain what access exceeds the lower role's stated purpose]`.

---

## V-03 -- SHALL-Level Cross-Role Differential Enforcement

**Axis:** Phrasing register -- SHALL-level enforcement for cross-role differential analysis (C-16 single-axis)
**Hypothesis:** The C-10 criterion distinguishes PARTIAL (comparison data is present in a matrix, comparison is derivable if the model chooses) from PASS (comparison is structurally required). The mechanism for this boundary is SHALL language: an instruction that names the comparison, requires a conclusion for each pair, and specifies the disposition vocabulary (EXPECTED DIFFERENTIAL vs CANDIDATE OVER-PERMISSION). Without SHALL language, the model may produce comparison data as an emergent property of matrix output without producing explicit per-pair conclusions -- satisfying the letter but not the structure of C-10.

---

You are running a permissions trace signal for: **{{topic}}**

---

**SECURITY GAP REGISTER -- assign [G-##] identifiers at the moment of discovery. Never defer.**

| ID | Entity | Field / Operation | Role(s) | Gap Type | Risk |
|----|--------|-------------------|---------|----------|------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH

---

### PHASE 1 -- Inventory

**1.1 -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

**1.2 -- Role catalog:**

| Role | Type (Stock / Custom / Team / Env) | Business Unit Scope | Purpose | Has Write? |
|------|-------------------------------------|---------------------|---------|------------|

Stock roles to check: Customer Service Representative, Basic User, System Customizer, System Administrator. Do not assume roles not present in or directly inferrable from the provided context.

**1.3 -- Analysis order:** Order entities by sensitivity (highest first). State first gap ID.

---

### PHASE 2 -- Per-Entity Trace

For each entity in sensitivity order:

**Operations per role:**

| Entity | Role | Create | Read | Write | Delete | Record Scope |
|--------|------|--------|------|-------|--------|--------------|

**Sensitive field FLS status:**

| Entity | Field | FLS Profile | Role | Access |
|--------|-------|-------------|------|--------|

MISSING-FLS -> [G-##] immediately.

**Escalation check (Write roles):**

| Vector | Roles | Verdict | Evidence |
|--------|-------|---------|----------|

POSSIBLE -> [G-##].

---

### PHASE 3 -- Sharing Rule Analysis

For each role, produce a SHARING RULE VERDICT block naming every entity the role touches and an explicit verdict per entity. CONFLICT FOUND -> [G-##].

---

### PHASE 4 -- Phase Gate

| Role | Phase 2 Covered? | Phase 3 Verdict Written? | Gaps (N) |
|------|-----------------|--------------------------|----------|

Gate assertion before proceeding to Phase 5.

---

### PHASE 5 -- Cross-Entity Cascade

Trace relationships between the two highest-sensitivity entities. EMERGENT access -> [G-##].

---

### PHASE 6 -- Remediation and Defense-in-Depth

For each [G-##]: exact Dataverse object, current state, target state, post-fix behavior.
Defense-in-depth table. Stock role summary.

---

### PHASE 7 -- Cross-Role Differential Analysis (SHALL-enforced)

**SHALL instructions -- these are not guidelines. Each SHALL instruction is a required output condition.**

The model **SHALL** produce a DIFFERENTIAL ANALYSIS section that compares access across all roles in the Role Catalog for each operation in the operation tables from Phase 2.

The model **SHALL NOT** produce this section as a matrix with comparison data only. A matrix is not a conclusion. Each role pair **SHALL** receive an explicit conclusion statement -- one of:

- `EXPECTED DIFFERENTIAL -- [Role A] has [access] that [Role B] does not because [reason tied to stated purpose]. The difference is consistent with the roles' design intent.`
- `CANDIDATE OVER-PERMISSION -- [Role A] has [access] that exceeds what [Role A's stated purpose] requires relative to [Role B]. Specific access in question: [named operation or field]. This is a candidate for tightening.`

The model **SHALL NOT** produce a conclusion of "the differential appears expected" without naming the specific access elements compared and the purpose statement that justifies the assessment.

The model **SHALL** process every role pair. If N roles are in the catalog, the number of pair assessments is N*(N-1)/2 for unordered pairs. Each pair **SHALL** appear as a named row in the differential table.

The model **SHALL** flag any CANDIDATE OVER-PERMISSION finding for remediation: add to SECURITY GAP REGISTER as [G-##], Gap Type = BU-SCOPE or ESCALATION-PATH as appropriate.

**Differential Analysis Table:**

| Role Pair | Operations Compared | Role A Access | Role B Access | Conclusion |
|-----------|--------------------|--------------|--------------| -----------|

Each Conclusion cell: full conclusion statement -- not a verdict code. The conclusion names the specific access, the stated purpose of each role, and whether the differential is justified.

---

## V-04 -- Combined: Inertia Framing (C-13) + Failure Mode Annotation (C-14)

**Axis:** Combined -- security state persistence (C-13) + per-phase failure mode annotation (C-14)
**Hypothesis:** C-13 and C-14 reinforce each other structurally. The inertia rule prevents verdict drift (C-13's target failure mode). Per-phase failure mode annotations make the inertia rule legible: the annotation for each phase names verdict drift as a failure mode to prevent, motivating the carry-forward notation at that phase. When both are present, collapsing a phase costs both a structural annotation and the carry-forward notations that phase would require -- making phase collapse detectable at two levels rather than one.

---

You are running a permissions trace signal for: **{{topic}}**

---

**SECURITY GAP REGISTER -- assign [G-##] at point of discovery. Never defer.**

| ID | Entity | Field / Operation | Role(s) | Gap Type | Risk |
|----|--------|-------------------|---------|----------|------|

---

**SECURITY STATE REGISTER -- authoritative per-role verdict record. Updated by every phase.**

| Role | Phase Last Updated | Current Verdict | Active Gap IDs |
|------|--------------------|-----------------|----------------|

Verdict values: `CLEARED` / `FLAGGED [G-##]` / `PENDING-PHASE-[N]`

**Inertia rule:** A verdict from Phase N is the persistent default entering Phase N+1. When Phase N+1 finds nothing new for a role, write:
`[Role] -- INERTIA: [verdict] from Phase [N], no new finding this phase.`
Required for every role. Absence of this notation means the role's verdict is unknown -- a detectable format failure.

---

### PHASE 1 -- Inventory

> **Structural purpose:** Prevents incomplete coverage -- the failure mode where analysis proceeds on an assumed role/entity set that excludes implicit roles, team-inherited access, or low-salience entities. Incorrect inventory is undetectable once analysis begins; it must be fixed here. **Inertia initialization:** After completing catalogs, set all roles to `PENDING-PHASE-2` in the SECURITY STATE REGISTER.

**1.1 -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

**1.2 -- Role catalog:**

| Role | Type (Stock / Custom / Team / Env) | Business Unit Scope | Purpose | Has Write? |
|------|-------------------------------------|---------------------|---------|------------|

Stock roles: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 -- Initialize SECURITY STATE REGISTER:** Enter all roles with verdict `PENDING-PHASE-2`.

---

### PHASE 2 -- Per-Entity Trace

> **Structural purpose:** Prevents verdict scatter -- the failure mode where access conclusions are embedded in prose and cannot be audited or compared. Entity tables produce referenceable verdicts. **Inertia requirement:** After each entity section, update the SECURITY STATE REGISTER -- new gap: FLAGGED; no finding: explicit carry-forward notation. Every role must appear in each update block.

For each entity (highest sensitivity first):

**2a -- Operations per role:**

| Entity | Role | Create | Read | Write | Delete | Record Scope |
|--------|------|--------|------|-------|--------|--------------|

**2b -- Sensitive field FLS:**

| Entity | Field | FLS Profile | Role | Access |
|--------|-------|-------------|------|--------|

MISSING-FLS -> [G-##] immediately.

**2c -- Escalation path check (Write roles only):**

| Vector | Roles | Verdict | Evidence |
|--------|-------|---------|----------|

POSSIBLE -> [G-##].

**2d -- SECURITY STATE UPDATE after this entity:**

For each role in the catalog:
- New finding: update SECURITY STATE REGISTER. `[Role] -- FLAGGED [G-##]. Source: Phase 2 / [Entity].`
- No finding: `[Role] -- INERTIA: PENDING-PHASE-2 (Phase 1 init), no finding on [Entity].` <- or carry the Phase 2 verdict if this is not the first entity.

---

### PHASE 3 -- Sharing Rule Analysis

> **Structural purpose:** Prevents sharing/FLS intersection gap -- the failure mode where record-level sharing produces field access invisible to role-level analysis. Sharing rules operate below security role scope and cannot be caught in Phase 2. **Inertia requirement:** After each SHARING RULE VERDICT, update the SECURITY STATE REGISTER.

For each role: SHARING RULE VERDICT block (every entity the role touches, explicit verdict per entity, [G-##] for conflicts).

**After each SHARING RULE VERDICT -- SECURITY STATE UPDATE:**
- Conflict: `[Role] -- FLAGGED [new G-##]. Source: Phase 3 / [Entity].`
- No conflict: `[Role] -- INERTIA: [verdict] from Phase 2, sharing clean on [entity list].`

---

### PHASE 4 -- Phase Gate: Coverage Check

> **Structural purpose:** Prevents phase-transition coverage loss -- the failure mode where the analysis advances to synthesis without confirming that all roles and entities were covered and all verdicts are consistent. **Security state consistency check:** Every role must have a non-PENDING verdict before Phase 5 begins.

| Role | Phase 2 Updated? | Phase 3 Updated? | Current Verdict | Open Gaps |
|------|-----------------|-----------------|-----------------|-----------|

Gate assertion: "All roles have non-PENDING verdicts. SECURITY STATE REGISTER is consistent. Total gaps: [N]. Proceeding."

Stop condition: if any role is still `PENDING-PHASE-[N]`, name it and resolve before continuing.

---

### PHASE 5 -- Cross-Entity Cascade

> **Structural purpose:** Prevents single-entity tunnel vision -- the failure mode where entity-by-entity analysis misses access that emerges only from entity relationships. **Inertia requirement:** Roles not involved in a cascade finding carry forward their Phase 4 verdict.

Cascade trace for two highest-sensitivity entities. EMERGENT access -> [G-##].

**SECURITY STATE UPDATE:** New cascade gap: update FLAGGED. No finding: carry-forward notation.

---

### PHASE 6 -- Remediation and Defense-in-Depth

> **Structural purpose:** Prevents non-actionable remediation -- the failure mode where gap entries are resolved with generic advice that cannot be implemented. Exact Dataverse object names are required.

For each [G-##]: exact Dataverse object, current state, target state, post-fix behavior.
Defense-in-depth table. Stock role summary.

**Final security state:** Copy SECURITY STATE REGISTER in final form. No PENDING entries. This is the authoritative output.

---

### PHASE 7 -- Cross-Role Differential

> **Structural purpose:** Prevents differential blindness -- the failure mode where per-role analysis is correct in isolation but cross-role comparisons that surface anomalous divergence are never made.

Compare at least two roles side-by-side on the same operations:

| Role Pair | Operation | Role A Access | Role B Access | Differential | Assessment |
|-----------|-----------|--------------|--------------|--------------|------------|

Assessment: `EXPECTED DIFFERENTIAL -- [reason]` or `CANDIDATE OVER-PERMISSION -- [specific access + why it exceeds stated purpose]`.

Carry SECURITY STATE forward: CANDIDATE OVER-PERMISSION -> [G-##], update FLAGGED.

---

## V-05 -- Full Combination: C-13 + C-14 + C-15 + C-16 + C-17

**Axis:** Full combination -- skill-level threat model in CONTEXT (C-17) + pre-phase failure mode catalog (C-15) + per-phase failure mode annotation (C-14) + inertia framing (C-13) + SHALL-level differential enforcement (C-16)
**Hypothesis:** Providing the failure mode structure at three levels simultaneously -- skill-wide (CONTEXT names why permissions tracing as a category fails), catalog-level (FAILURE MODE MAP lists what each phase defends before Phase 1 begins), and phase-level (inline annotations confirm the defense is active at each step) -- makes structural omissions detectable at all three levels. A model that collapses Phase 3 loses the FAILURE MODE MAP entry, the Phase 3 structural annotation, and the inertia carry-forward notations that Phase 3 would require. Unlike R3 V-05 which built toward this structure through incremental combination, V-05 here targets the new C-13 through C-17 criteria directly on top of the R3 structural baseline.

---

You are running a permissions trace signal for: **{{topic}}**

---

## CONTEXT -- Why Permissions Tracing Fails: Skill-Level Threat Model

Before any analysis begins, understand the three failure modes that permissions tracing as a category of work is prone to produce:

**FM-SKILL-1 -- FLS post-incident discovery.** Field-level security gaps are structurally invisible at role level. A security role can be correctly scoped -- the right operations on the right entities at the right BU scope -- while a sensitive field has no column security profile configured. This gap surfaces only after an incident: an authenticated user reads a field they were never meant to access, and post-incident review reveals the FLS profile was never created. Standard role-matrix analysis does not catch this because role-level Read on an entity does not expose which fields within that entity are unprotected. FLS must be traced as a separate analytical pass.

**FM-SKILL-2 -- Cumulative scope blindness.** Each individual role may be scoped correctly relative to its stated purpose. The failure occurs when role combinations -- team inheritance granting broader BU scope than the base role, sharing records granting record access below the entity-level deny, environment admin roles elevating restricted roles, cascade relationships between entities -- produce an effective access scope that no single-role analysis predicts. The analyst checks each role, finds nothing anomalous, and misses the cross-role combination that creates over-permission. This failure is invisible to per-role analysis and visible only to cross-role differential and cascade analysis.

**FM-SKILL-3 -- Verdict drift.** Role verdicts assigned early in the analysis are silently overridden when the model transitions between phases. A role that received a CLEARED verdict in Phase 2 is re-evaluated from scratch in Phase 3, sometimes with a different conclusion -- not because new evidence was found, but because the prior verdict was not carried forward. The analysis becomes internally inconsistent: the gap inventory reflects Phase 6 verdicts, not the accumulated verdicts from Phases 2-5. This produces a security assessment whose conclusions are not causally connected to its analysis.

These three failure modes motivate the structure of this analysis: a dedicated FLS phase (FM-SKILL-1), cross-role differential and cascade phases (FM-SKILL-2), and an inertia framing protocol that makes verdict carry-forward explicit and detectable (FM-SKILL-3).

Use Dataverse-native terminology throughout: business units, security roles, owner teams, access teams, column security profiles, table permissions, sharing records, environment roles. At least four Dataverse-specific terms must appear and be used accurately.

---

## FAILURE MODE MAP

Read this map before executing Phase 1. It lists every structural element and the failure mode it defends against. If a phase is absent from the output, its defended failure mode is unmitigated -- and that omission is visible here before any analysis begins.

| Structural Element | Defends Against |
|-------------------|-----------------|
| Phase 1 -- complete entity + role catalog (no assumed defaults) | FM-P1: Incomplete inventory producing wrong verdicts from Phase 2 onward; undetectable once analysis begins |
| Phase 2 -- per-entity operation + FLS tables with [G-##] at discovery | FM-SKILL-1 (FLS gap invisible at role level) + FM-P2: Verdict scatter from inline prose analysis |
| Phase 3 -- per-role SHARING RULE VERDICT blocks | FM-SKILL-2 (sharing rules produce access below role scope) + FM-P3: Sharing/FLS intersection gap not caught by role analysis |
| Phase 4 -- phase gate coverage check | FM-P4: Phase-transition coverage loss -- roles/entities not covered before synthesis begins |
| Phase 5 -- cross-entity cascade | FM-SKILL-2 (relationship-derived access invisible to per-entity analysis) + FM-P5: Single-entity tunnel vision |
| Phase 6 -- SHALL cross-role differential | FM-SKILL-2 (cross-role combination blindness) + FM-P6: Differential omitted when per-role analysis finds no individual anomaly |
| SECURITY STATE REGISTER + inertia rule | FM-SKILL-3 (verdict drift) + FM-P7: Phase-transition verdict reset producing inconsistent analysis |
| Phase 7 -- gap inventory aggregated from [G-##] sentinels | FM-P8: Gap loss during model transition from traversal to summary -- inventory re-created from memory rather than from logged sentinels |
| Phase 8 -- remediation with exact Dataverse object names | FM-P9: Non-actionable remediation requiring additional analysis before implementation |

---

**SECURITY GAP REGISTER -- assign [G-##] at point of discovery. Never defer.**

| ID | Entity | Field / Operation | Role(s) | Gap Type | Risk |
|----|--------|-------------------|---------|----------|------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH
Risk: CRITICAL / HIGH / MEDIUM

---

**SECURITY STATE REGISTER -- authoritative per-role verdict. Updated every phase.**

| Role | Phase Last Updated | Current Verdict | Active Gap IDs |
|------|--------------------|-----------------|----------------|

Verdict values: `CLEARED` / `FLAGGED [G-##]` / `PENDING-PHASE-[N]`

**Inertia rule:** Every verdict from Phase N is the persistent default entering Phase N+1. When a phase finds nothing new for a role:
`[Role] -- INERTIA: [verdict] from Phase [N], no new finding this phase.`
Required for every role. Absence = verdict unknown = detectable format failure.

**Phase dependency protocol:** Each phase declares its required inputs. A phase SHALL NOT proceed without its declared inputs.

---

### PHASE 1 -- Inventory

> **Structural purpose:** Prevents FM-P1 -- incomplete inventory. **Inertia initialization:** All roles set to `PENDING-PHASE-2` after catalogs complete.

**Input required:** System description from provided context.
**Output:** ENTITY CATALOG + ROLE CATALOG

**1.1 -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

Sensitivity: High (PII, financial, credentials, health) / Medium (internal-only, cross-BU risk) / Low

**1.2 -- Role catalog:**

| Role | Type (Stock / Custom / Team / Env) | Business Unit Scope | Purpose | Has Write? |
|------|-------------------------------------|---------------------|---------|------------|

Stock roles to check: Customer Service Representative, Basic User, System Customizer, System Administrator. Do not list roles not present in or directly inferrable from the provided context.

**1.3 -- For each role:** state whether the assigned Business Unit Scope is appropriate relative to the stated purpose, or whether it is over-permissioned. This is a required judgment.

**1.4 -- Initialize SECURITY STATE REGISTER** with all roles: `PENDING-PHASE-2`.

**1.5 -- Analysis order:** Order entities highest to lowest sensitivity. State: "I will trace entities in this order: [list]. First gap ID: G-01."

---

### PHASE 2 -- Per-Entity Trace

> **Structural purpose:** Prevents FM-SKILL-1 (FLS post-incident discovery) + FM-P2 (verdict scatter). **Inertia requirement:** SECURITY STATE REGISTER updated after each entity section -- new gap: FLAGGED; no finding: explicit carry-forward notation. Every role must appear.

**Input required:** ENTITY CATALOG from Phase 1 (ordered). ROLE CATALOG from Phase 1.
**Dependency check:** If Phase 1 catalogs are incomplete, name missing items before proceeding.

For each entity (highest sensitivity first):

**2a -- Operations per role:**

| Entity | Role | Create | Read | Write | Delete | Record Scope |
|--------|------|--------|------|-------|--------|--------------|

**2b -- Sensitive field FLS status:**

| Entity | Field | Sensitivity | FLS Profile (YES/NO/UNKNOWN) | Role | Can Read? | Can Write? |
|--------|-------|-------------|------------------------------|------|-----------|------------|

MISSING-FLS rule: High/Medium sensitivity + NO FLS profile + role has Read -> assign [G-##] immediately. Gap Type = MISSING-FLS. Risk = CRITICAL.

**2c -- Escalation path check (Write roles only):**

| Vector | Roles | Verdict | Evidence |
|--------|-------|---------|----------|
| Record Assign | ... | POSSIBLE / NOT POSSIBLE | ... |
| Share to higher-privilege role | ... | POSSIBLE / NOT POSSIBLE | ... |
| Field modification affecting role/BU | ... | POSSIBLE / NOT POSSIBLE | ... |
| Team self-addition | ... | POSSIBLE / NOT POSSIBLE | ... |

POSSIBLE -> assign [G-##], Gap Type = ESCALATION-PATH.

**2d -- SECURITY STATE UPDATE for this entity (required for every role):**
- New gap: `[Role] -- FLAGGED [G-##]. Source: Phase 2 / [Entity].`
- No finding: `[Role] -- INERTIA: [prior verdict], no finding on [Entity].`

---

### PHASE 3 -- Sharing Rule Analysis

> **Structural purpose:** Prevents FM-SKILL-2 (sharing as access path below role scope) + FM-P3 (sharing/FLS intersection gap). **Inertia requirement:** SECURITY STATE REGISTER updated after each SHARING RULE VERDICT.

**Input required:** ROLE CATALOG from Phase 1. ENTITY CATALOG from Phase 1. Gap register current state from Phase 2.

For each role, produce a SHARING RULE VERDICT block covering every entity the role touches:

#### SHARING RULE VERDICT: [Role name]

| Entity | Sharing Rules Found? | Rule Name | Access Expanded Beyond OWD+Role? | Verdict |
|--------|---------------------|-----------|----------------------------------|---------|

Verdict format:
- `"Confirmed: no sharing rules expand [Role] access on [Entity]. OWD=[value], role scope=[scope]. No criteria-based or manual sharing applies."`
- `"CONFLICT FOUND: [Rule] expands [Role] access on [Entity] to [record set]. Exceeds design intent: [reason]. Assigned [G-##]. Gap Type = SHARING-CONFLICT."`

Every entity the role touches must appear. Silent omissions fail this block.

**SECURITY STATE UPDATE after each SHARING RULE VERDICT:**
- Conflict found: `[Role] -- FLAGGED [G-##]. Source: Phase 3 / [Entity].`
- No conflict: `[Role] -- INERTIA: [prior verdict] from Phase 2, sharing clean on [entity list].`

---

### PHASE 4 -- Phase Gate: Coverage Check

> **Structural purpose:** Prevents FM-P4 (phase-transition coverage loss). **Security state consistency gate:** No PENDING-PHASE entries permitted before Phase 5.

**Input required:** All Phase 2 entity sections. All Phase 3 sharing rule verdicts.

| Role | Phase 2: All Entities? | Phase 3: Verdict Written? | Phase 3: State Updated? | Current Verdict | Open Gaps |
|------|------------------------|--------------------------|------------------------|-----------------|-----------|

Gate assertion: "All [N] entities traced. All [N] roles have sharing verdicts and state register entries. No PENDING-PHASE entries remain. Total gaps: [N]. Proceeding to Phase 5."

Stop condition: PENDING-PHASE entry remaining -> name the role, resolve before continuing.

---

### PHASE 5 -- Cross-Entity Cascade

> **Structural purpose:** Prevents FM-SKILL-2 (relationship-derived access) + FM-P5 (single-entity tunnel vision). **Inertia requirement:** Roles not involved in cascade carry forward Phase 4 verdict.

**Input required:** Phase 2 operation verdicts. Phase 4 gate confirmation.

**5a -- Relationship map (two highest-sensitivity entities):**

| Source | Relationship | Target | Cascade Behavior |
|--------|-------------|--------|-----------------|

**5b -- Cascade access trace:**

`[Role] -> [Source, access, scope] -> [Relationship + cascade] -> [Target, resulting access]` -> INTENTIONAL or EMERGENT

EMERGENT access exceeding direct grant: assign [G-##], Gap Type = CASCADE-OVERREACH.

**5c -- SECURITY STATE UPDATE:**
- Cascade gap: `[Role] -- FLAGGED [G-##]. Source: Phase 5.`
- No cascade finding: `[Role] -- INERTIA: [verdict] from Phase 4, no cascade finding.`

---

### PHASE 6 -- Cross-Role Differential Analysis (SHALL-enforced)

> **Structural purpose:** Prevents FM-SKILL-2 (cumulative scope blindness) + FM-P6 (differential omitted when per-role analysis finds no individual anomaly). **Inertia requirement:** Verdicts from SECURITY STATE REGISTER are the authoritative starting point. This phase does not re-derive verdicts from scratch.

**Input required:** Phase 2 ACCESS MATRIX verdicts. SECURITY STATE REGISTER current state. ROLE CATALOG from Phase 1.

**SHALL instructions:**

The model **SHALL** compare access differentials across all roles in the ROLE CATALOG for each operation in the Phase 2 operation tables.

For each role pair, the model **SHALL** state an explicit conclusion -- one of:
- `EXPECTED DIFFERENTIAL -- [Role A] has [specific access] that [Role B] does not. This is consistent with [Role A's stated purpose] because [reason].`
- `CANDIDATE OVER-PERMISSION -- [Role A] has [specific access] that exceeds what [Role A's stated purpose] requires relative to [Role B]. Access in question: [named operation or field]. This is a candidate for tightening.`

The model **SHALL NOT** produce a conclusion of "differential appears expected" without naming the specific access elements compared and the purpose statement that justifies the assessment.

The model **SHALL** process every role pair. Number of pairs: N*(N-1)/2 for N roles.

The model **SHALL** assign a [G-##] for every CANDIDATE OVER-PERMISSION finding. Gap Type = BU-SCOPE.

**Differential Analysis Table:**

| Role Pair | Operations Compared | Role A Access | Role B Access | Conclusion |
|-----------|--------------------|--------------|--------------| -----------|

Conclusion cell: full statement -- not a verdict code.

**SECURITY STATE UPDATE:** CANDIDATE OVER-PERMISSION -> `FLAGGED [G-##]. Source: Phase 6.` No new finding -> carry-forward notation.

---

### PHASE 7 -- Gap Inventory

> **Structural purpose:** Prevents FM-P8 (gap loss during model transition). Aggregate all [G-##] sentinels logged during Phases 2-6. Do not invent gaps not logged inline. Do not drop sentinels.

**Input required:** All [G-##] from SECURITY GAP REGISTER. SECURITY STATE REGISTER current state.

For each [G-##]: Gap ID | Type | Entity/Field/Role | Description | Remediation

The gap inventory is a reference to logged sentinels -- not a re-creation from memory.

---

### PHASE 8 -- Remediation and Defense-in-Depth

> **Structural purpose:** Prevents FM-P9 (non-actionable remediation). Each gap resolved with an exact Dataverse configuration object.

**Input required:** GAP INVENTORY from Phase 7.

**8a -- Gap remediation (cite by [G-##]):**

`[G-##]: Apply [specific change] to [exact Dataverse object] in [solution location]. Current state: [...]. Target state: [...]. Post-fix behavior: [...].`

Exact objects: column security profile name, security role privilege + table name, team type + membership rule, sharing rule name, OWD value per entity. Generic advice fails.

**8b -- Defense-in-depth assessment:**

| Entity | Security Role Layer: Independent? | FLS Layer: Independent? | Record Scope Layer: Independent? | Single Point of Failure? |
|--------|-----------------------------------|------------------------|----------------------------------|-------------------------|

**8c -- Stock role summary:**

For each stock Dataverse role present: baseline privileges, modified how, necessary or removable from this scenario.

**8d -- Final security state:**

Copy SECURITY STATE REGISTER in final form. Every role: `CLEARED` or `FLAGGED [G-##]`. No PENDING entries. This is the authoritative security output of this trace.

---

*End of Round 4 variations*
"""

with open(r"C:\\src\\sim\\simulations\\quest\\golden\\trace-permissions-variate-R4-2026-03-16.md", "w", encoding="utf-8") as f:
    f.write(content)
print("written", len(content), "chars")
