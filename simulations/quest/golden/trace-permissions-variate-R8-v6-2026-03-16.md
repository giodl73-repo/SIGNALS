# trace-permissions Variate — Round 8 (Rubric v6)
**Date:** 2026-03-16
**Rubric:** v6 (C-01 through C-22, max 125.0)
**New criteria targeted this round:** C-20 (structural enforcement of layer-override explanation — required table column, not prose), C-21 (complete phase dependency graph — Phase 7 and Phase 8 terminal orphans closed), C-22 (count-comparison coverage gate before aggregation — entities analyzed == entities declared)

**State entering Round 8:**

| Variation | v5 score | Gap under v6 |
|-----------|----------|--------------|
| R7-v5-V-05 (best v5) | All 19 aspirational C-01–C-19 satisfied | Missing C-20/C-21/C-22 (-7.5 pts) = full aspirational miss on new tier |
| Diagnostic | Phase 8b has Effective Enforcement Layer column (C-09 pass) but no required "Why" column | C-20 fails; C-09 passes without triggering C-20 |
| Diagnostic | Phase 7 and Phase 8 have no EXIT GATE declarations | C-21 fails; "each phase" claim in FAILURE MODE MAP is false for terminal phases |
| Diagnostic | Phase 4 gate assertion checks entity count narratively ("All [N] entities") | C-22 fails; count-comparison formula not enforced as a gate with PASS/FAIL output |

Round 8 holds the established v5 scaffold (8-phase, CONTEXT threat model, FAILURE MODE MAP, SECURITY GAP REGISTER with sentinel tokens, SECURITY STATE REGISTER with inertia rule, Phase 1-6 exit gates, sentinel inventory, SHALL cross-role differential, exact-object remediation) and adds C-20/C-21/C-22 mechanisms across three single-axis tests and two combined variations.

**Distinction chains (from rubric v6):**
- **C-09 + C-20** -- which layer is effective (C-09) + why upper layers are overridden, required as a table column not prose (C-20). Same role C-16 plays for C-10.
- **C-11 + C-18 + C-21** -- input declaration (C-11) + output declaration (C-18) + every phase boundary covered, no orphans (C-21). C-21 is the end-state when C-11 and C-18 are both satisfied at every phase boundary.
- **C-19 + C-22** -- routing rules guarantee what-was-found reaches the register (C-19) + coverage gate confirms what-was-found is everything (C-22). C-22 closes the loop C-19 cannot: it checks the completeness of the analysis itself, not just the completeness of routing.

---

## Round 8 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format -- C-20 single-axis: required "Why Upper Layers Don't Override" column in defense-in-depth table | V-05/R7 Phase 8b has the 5-column defense-in-depth table with Effective Enforcement Layer column (C-09 pass), but "why upper layers do not override" is a trailing prose instruction ("explain why upper layers do not override it"), never a required table column. Without a required column, the model names the correct effective layer while the causal reasoning is never demanded structurally -- exactly the diagnostic the rubric calls out. Adding a 6th required column "Why Upper Layers Don't Override" with a MUST-populate rule converts the prose instruction to a structural output requirement: C-09 identifies the effective layer; C-20 requires the causal explanation to appear as tabular output, not prose commentary. Isolated single-axis test: +2.5 pts (C-20 only). |
| V-02 | Lifecycle emphasis -- C-21 single-axis: Phase 7 and Phase 8 EXIT GATE declarations closing terminal phase orphans | V-05/R7 has Phase 1 through Phase 6 EXIT GATE declarations but Phase 7 (SHALL cross-role differential) and Phase 8 (remediation + defense-in-depth) have no exit gates. The FAILURE MODE MAP claims "Named exit gate artifact declarations at end of each phase" but that claim is false for the terminal two phases. Phase 7 produces DIFFERENTIAL FINDINGS and OVER-PERMISSION ASSIGNMENTS -- these are unnamed until Phase 8 INPUT REQUIRED references them. Phase 8 produces REMEDIATION REGISTER and FINAL SECURITY STATE REGISTER -- declared nowhere. Adding explicit exit gate declarations at Phase 7 and Phase 8 closes both orphans and makes the "each phase" claim in the FAILURE MODE MAP true. Isolated single-axis test: +2.5 pts (C-21 only). |
| V-03 | Phase dependency chaining -- C-22 single-axis: count-comparison COVERAGE GATE COUNT block with PASS/FAIL before aggregation | V-05/R7 Phase 4 has a gate assertion that reads "All [N] entities in ACCESS MATRIX" but N is filled from memory -- there is no explicit comparison against the entity count from Phase 1 ENTITY CATALOG. C-19 routing rules guarantee every discovery in the analyzed entities reaches the register; they cannot detect that 3 of 6 entities were never analyzed. C-22 requires a count-comparison formula: "ENTITY CATALOG declared [M] entities. ACCESS MATRIX contains [N] entities. M == N: YES/NO. GATE STATUS: PASS/FAIL. Aggregation SHALL NOT begin until GATE STATUS = PASS." Adding this block to Phase 4 independently catches partial analysis invisible to routing rules. Isolated single-axis test: +2.5 pts (C-22 only). |
| V-04 | Combined C-20 + C-21: required explanation column + complete phase chain | C-20 and C-21 are structurally independent: C-20 targets Phase 8b (defense-in-depth output format), C-21 targets Phase 7 and Phase 8 boundary declarations (lifecycle). Neither interferes with the other. V-04 tests whether the Phase 8 exit gate can reinforce C-20 by requiring the "Why Upper Layers Don't Override" column to be populated as a precondition for exit gate satisfaction -- making the exit gate double as a C-20 enforcement point. Combined: +5.0 pts. |
| V-05 | Full combination: C-20 + C-21 + C-22 on V-05/R7 foundation | The three criteria close three independent gaps: C-20 closes defense-in-depth causal reasoning truncation (structural enforcement of layer-override explanation), C-21 closes terminal phase orphan gap (full 8-phase chain with no orphan boundaries at 7 and 8), C-22 closes entity-count verification gap (count-comparison gate blocks aggregation on partial analysis). Together they address distinct failure modes: FM-SKILL-6 (layer-reasoning truncation), terminal-phase output-schema drift (C-21 extension of FM-SKILL-4), and FM-SKILL-7 (partial-analysis aggregation blindness). Full 22-criterion target: 125.0/125.0 predicted. |

---

## V-01 -- Required Layer-Override Explanation Column (C-20 single-axis)

**Axis:** Output format -- required "Why Upper Layers Don't Override" column in defense-in-depth table (C-20 single-axis)
**Hypothesis:** V-05/R7 Phase 8b has the Effective Enforcement Layer column (satisfying C-09) but the causal reasoning -- why the layers above the effective layer do not independently enforce the same restriction -- is present only as a prose instruction appended to the table definition. Without a required column, any model that names the correct effective layer passes C-09 while the "why" reasoning is never tested structurally. Adding a 6th column "Why Upper Layers Don't Override" with a MUST-populate rule creates the structural enforcement C-20 requires: the output is not complete until the causal explanation appears in the table, not in prose. The precedent: C-10 identifies the cross-role differential; C-16 adds SHALL language making it a structural requirement. C-09 identifies the effective enforcement layer; C-20 adds a required column making the causal reasoning a structural output.

---

You are running a permissions trace signal for: **{{topic}}**

---

## CONTEXT -- Why Permissions Tracing Fails: Skill-Level Threat Model

Before any analysis begins, understand the six failure modes that permissions tracing as a category of work is structurally prone to produce:

**FM-SKILL-1 -- FLS post-incident discovery.** Field-level security gaps are invisible at the security role level. A role can be correctly scoped -- right operations, right entities, right BU scope -- while a sensitive field has no column security profile. This gap surfaces only after an incident. FLS must be traced as a separate analytical pass distinct from operation-level role analysis.

**FM-SKILL-2 -- Cumulative scope blindness.** Each individual role may be scoped correctly. The failure occurs when role combinations -- team inheritance granting broader BU scope, sharing records granting record access below entity-level deny, environment admin roles elevating restricted roles, cascade relationships between entities -- produce an effective access scope that no single-role analysis predicts.

**FM-SKILL-3 -- Verdict drift.** Role verdicts assigned early in the analysis are silently overridden when the model transitions between phases. A CLEARED verdict from Phase 2 is re-evaluated from scratch in Phase 3, sometimes with a different conclusion -- not because new evidence was found, but because the prior verdict was not carried forward.

**FM-SKILL-4 -- Output-schema drift.** Phase dependency declarations reference artifacts from prior phases by name. But if the producing phase never declares its output schema, the artifact name in the consuming phase is a best guess. When context pressure causes the producing phase to restructure its output, the name match breaks silently.

**FM-SKILL-5 -- Routing gap.** Violation discoveries placed inline during traversal phases do not automatically reach the gap inventory. The model must remember which discoveries to aggregate. At the traversal-to-summary transition, discoveries without explicit routing rules are susceptible to omission.

**FM-SKILL-6 -- Layer-override reasoning truncation.** The defense-in-depth table identifies which layer is the effective enforcement point (satisfying C-09) but leaves the causal "why" as a prose instruction after the table. Without a required column, the model names the correct layer while the reasoning -- why upper layers do not independently enforce the same restriction -- is never demanded structurally. The reader cannot verify whether the effective layer identification is correct or coincidental. A required "Why Upper Layers Don't Override" column makes the causal reasoning a structural output requirement: the output is not complete until the column is populated with a specific mechanism explanation.

These failure modes motivate the structure of this analysis: dedicated FLS sentinel placement (FM-SKILL-1), cross-role differential and cascade phases (FM-SKILL-2), SECURITY STATE REGISTER with inertia framing (FM-SKILL-3), named exit gate artifact declarations (FM-SKILL-4), explicit aggregation routing rules (FM-SKILL-5), and required layer-override explanation column (FM-SKILL-6).

Use Dataverse-native terminology throughout: business units, security roles, owner teams, access teams, column security profiles, table permissions, sharing records, environment roles. At least four Dataverse-specific terms must appear and be used accurately.

---

## FAILURE MODE MAP

Read this map before Phase 1. A structural element absent from the output leaves its failure mode unmitigated.

| Structural Element | Defends Against |
|-------------------|-----------------|
| Phase 1 -- complete entity + role catalog | FM-P1: Incorrect coverage undetectable once analysis begins |
| Sentinel tokens [GAP-FLS-*], [GAP-ESC-*], [GAP-SHARE-*], [SCOPE AMBIGUOUS], [UNCHECKED] placed inline at discovery | FM-SKILL-1 + FM-P2: Discoveries not recorded at point of occurrence |
| Phase 2 -- FLS SENTINEL TABLE + ESCALATION FINDINGS with sentinels | FM-SKILL-1 (FLS gap invisible at role level) + FM-P3: Verdict scatter from prose |
| Phase 3 -- SHARING RULE VERDICT blocks per role | FM-SKILL-2 (sharing below role scope) + FM-P4: Sharing/FLS intersection missed by role analysis |
| Phase 4 -- coverage gate with named artifact verification | FM-P5: Coverage loss at phase transition before synthesis begins |
| Named exit gate artifact declarations at end of Phases 1-6 | FM-SKILL-4 (output-schema drift) + FM-P6: C-11 input references match coincidental names not declared contracts |
| Aggregation routing rules naming sentinel type and Phase 6 inventory destination | FM-SKILL-5 (routing gap) + FM-P7: Traversal discoveries lost at aggregation step |
| Phase 6 -- SENTINEL INVENTORY aggregated from inline sentinels | FM-SKILL-5 + FM-P8: Gap inventory re-created from memory, not routed from logged tokens |
| SECURITY STATE REGISTER + inertia carry-forward rule | FM-SKILL-3 (verdict drift) + FM-P9: Phase-transition verdict reset |
| Phase 7 -- SHALL cross-role differential | FM-SKILL-2 (cumulative scope blindness) + FM-P10: Differential omitted when per-role analysis finds no individual anomaly |
| Phase 8 -- exact Dataverse object remediation | FM-P11: Generic advice non-actionable without additional analysis |
| Phase 8b -- required "Why Upper Layers Don't Override" column | FM-SKILL-6 (layer-override reasoning truncation): effective layer named without causal explanation |

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

> **Structural purpose:** Prevents FM-SKILL-1 (FLS post-incident discovery) + FM-P3 (verdict scatter). **Inertia requirement:** SECURITY STATE REGISTER updated after every entity section.

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

> **Structural purpose:** Prevents FM-SKILL-2 (sharing below role scope) + FM-P4. **Inertia requirement:** SECURITY STATE REGISTER updated after each SHARING RULE VERDICT.

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

> **Structural purpose:** Prevents FM-SKILL-2 (relationship-derived access). **Inertia requirement:** Roles not involved in cascade carry forward Phase 4 verdict.

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

> **Structural purpose:** Prevents FM-SKILL-5 (routing gap). Aggregate all discovery-point tokens. The gap list derives from this inventory -- not from memory.

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

> **Structural purpose:** Prevents FM-SKILL-2 (cumulative scope blindness). **Inertia requirement:** SECURITY STATE REGISTER verdicts are authoritative. This phase does not re-derive verdicts from scratch.

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

> **Structural purpose:** Prevents FM-P11 (non-actionable remediation) + FM-SKILL-6 (layer-override reasoning truncation).

**Input required:** AGGREGATE GAP LIST from Phase 6 (updated with Phase 7 additions).

**8a -- Gap remediation (cite by [G-##] and sentinel token):**

For each row in AGGREGATE GAP LIST from Phase 6:

`[G-##] [sentinel token]: Apply [specific change] to [exact Dataverse configuration object] in [solution location]. Current state: [what exists today]. Target state: [what it should be]. Post-fix behavior: [what a user can / cannot do].`

Exact Dataverse configuration objects required: column security profile name (not "add FLS"), security role privilege name + table name (not "tighten the role"), team type (owner/access) + membership rule (not "fix team membership"), sharing rule name (not "remove the rule"), OWD value per entity (not "adjust OWD"). Generic advice fails.

**8b -- Defense-in-depth assessment (two highest-sensitivity entities):**

| Entity | Layer 1: Env / Admin Role | Layer 2: Security Role + BU Scope | Layer 3: Team Membership | Layer 4: FLS / Column Security Profile | Effective Enforcement Layer | Why Upper Layers Don't Override |
|--------|--------------------------|----------------------------------|--------------------------|---------------------------------------|----------------------------|---------------------------------|

**Column rules:**
- **Effective Enforcement Layer**: name the specific layer (Layer 1 / 2 / 3 / 4) that independently enforces the access decision for the operation in question.
- **Why Upper Layers Don't Override**: MUST be populated for at least one entity and one operation. State the specific reason the layers above the Effective Enforcement Layer cannot independently grant or deny the same access. Acceptable forms: "Layer 1 admin role does not restrict entity-level Read; only the column security profile in Layer 4 restricts access to [field] specifically" or "Layer 2 security role grants org-wide Read; the access restriction is enforced solely by the Layer 4 column security profile which is evaluated after role-level access is granted." Unacceptable forms: "by design", "see above", "not applicable". A blank cell in this column FAILS C-20 regardless of C-09 satisfaction.

**8c -- Stock role summary:**

For each stock Dataverse role present in ROLE CATALOG from Phase 1: baseline privileges, how modified in this scenario, whether necessary or removable.

**Final SECURITY STATE REGISTER:** Copy in final form. Every role must have `CLEARED` or `FLAGGED [sentinel list, G-## list]`. No PENDING-PHASE entries permitted.

---

## V-02 -- Complete Phase Chain: Terminal Phase Exit Gates (C-21 single-axis)

**Axis:** Lifecycle emphasis -- Phase 7 and Phase 8 EXIT GATE declarations closing terminal phase orphans (C-21 single-axis)
**Hypothesis:** V-05/R7 has Phase 1 through Phase 6 EXIT GATE declarations satisfying C-18. Phase 7 (SHALL cross-role differential) produces DIFFERENTIAL FINDINGS and OVER-PERMISSION ASSIGNMENTS but never formally declares them. Phase 8 references the Phase 6 AGGREGATE GAP LIST by name but the Phase 7 outputs have no declared artifact contract -- Phase 8's input declaration for Phase 7 outputs is a coincidental name reference, not a contract-enforced dependency. Adding PHASE 7 EXIT GATE ("this phase produces: DIFFERENTIAL FINDINGS (schema)") and PHASE 8 EXIT GATE ("this phase produces: REMEDIATION REGISTER + DEFENSE-IN-DEPTH ASSESSMENT + FINAL SECURITY STATE REGISTER") closes both terminal orphans. The FAILURE MODE MAP claim "Named exit gate artifact declarations at end of each phase" becomes true at all 8 phase boundaries. C-21 is the end-state when C-11 and C-18 are both satisfied at every phase boundary -- V-02 achieves that.

---

You are running a permissions trace signal for: **{{topic}}**

---

## CONTEXT -- Why Permissions Tracing Fails: Skill-Level Threat Model

**FM-SKILL-1 -- FLS post-incident discovery.** Field-level security gaps are invisible at the security role level. FLS must be traced as a separate analytical pass distinct from operation-level role analysis.

**FM-SKILL-2 -- Cumulative scope blindness.** Role combinations produce effective access scope that no single-role analysis predicts. Visible only to cross-role differential and cascade analysis.

**FM-SKILL-3 -- Verdict drift.** Role verdicts assigned early are silently overridden at phase transitions. The gap inventory reflects late-phase verdicts, not the accumulated evidence chain.

**FM-SKILL-4 -- Output-schema drift.** If the producing phase never declares its output schema, consuming-phase artifact references are best guesses. When producing phase restructures, the name match breaks silently. This applies equally to terminal phases: Phase 7 produces artifacts that Phase 8 consumes; without a Phase 7 EXIT GATE, that dependency is undeclared.

**FM-SKILL-5 -- Routing gap.** Violations placed inline during traversal do not automatically reach the gap inventory. Explicit routing rules are required at every discovery-to-inventory boundary.

These failure modes motivate: dedicated FLS sentinel placement (FM-SKILL-1), cross-role differential and cascade phases (FM-SKILL-2), SECURITY STATE REGISTER with inertia framing (FM-SKILL-3), named exit gate artifact declarations at every phase boundary including terminal phases (FM-SKILL-4), explicit aggregation routing rules (FM-SKILL-5).

Use Dataverse-native terminology throughout. At least four Dataverse-specific terms must appear and be used accurately.

---

## FAILURE MODE MAP

| Structural Element | Defends Against |
|-------------------|-----------------|
| Phase 1 -- complete entity + role catalog | FM-P1: Incorrect coverage undetectable once analysis begins |
| Sentinel tokens placed inline at discovery | FM-SKILL-1 + FM-P2 |
| Phase 2 -- FLS SENTINEL TABLE + ESCALATION FINDINGS | FM-SKILL-1 + FM-P3 |
| Phase 3 -- SHARING RULE VERDICT blocks per role | FM-SKILL-2 + FM-P4 |
| Phase 4 -- coverage gate | FM-P5 |
| Named exit gate artifact declarations at end of ALL phases (1-8) | FM-SKILL-4 (output-schema drift) -- terminal phases included |
| Aggregation routing rules | FM-SKILL-5 + FM-P7 |
| Phase 6 -- SENTINEL INVENTORY | FM-SKILL-5 + FM-P8 |
| SECURITY STATE REGISTER + inertia rule | FM-SKILL-3 + FM-P9 |
| Phase 7 -- SHALL cross-role differential | FM-SKILL-2 + FM-P10 |
| Phase 8 -- exact Dataverse object remediation | FM-P11 |

---

**SECURITY GAP REGISTER -- assign [G-##] at point of discovery. Never defer.**

| ID | Sentinel Token | Entity | Field / Operation | Role(s) | Gap Type | Risk | Source Phase |
|----|---------------|--------|-------------------|---------|----------|------|-------------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH

**Sentinel token vocabulary:**
- `[GAP-FLS-fieldname]` -- placed inline at the FLS gap discovery row
- `[GAP-ESC-vectorname]` -- placed inline at a POSSIBLE escalation vector row
- `[GAP-SHARE-rulename]` -- placed inline at a sharing conflict verdict row
- `[SCOPE AMBIGUOUS]` -- placed inline where BU scope cannot be assessed
- `[UNCHECKED]` -- placed inline where a vector cannot be evaluated

**Sentinel placement rule:** Every sentinel MUST be placed inline at the exact point of discovery.

---

**SECURITY STATE REGISTER -- authoritative per-role verdict record. Updated by every phase.**

| Role | Phase Last Updated | Current Verdict | Active Sentinel Tokens | Active Gap IDs |
|------|--------------------|-----------------|----------------------|----------------|

Verdict values: `CLEARED` / `FLAGGED [sentinels, G-##]` / `PENDING-PHASE-[N]`

**Inertia rule:** Every verdict from Phase N is the persistent default entering Phase N+1. When a phase finds nothing new: `[Role] -- INERTIA: [verdict] from Phase [N], no new finding this phase.` Required for every role in every phase.

**Phase dependency protocol:** Each phase declares its required inputs by artifact name. A phase SHALL NOT proceed without its declared inputs present.

---

### PHASE 1 -- Inventory

**Input required:** System description from provided context.

**1.1 -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

**1.2 -- Role catalog:**

| Role | Type (Stock / Custom / Team / Env) | Business Unit Scope | Purpose | Has Write? | Column Security Profiles Attached |
|------|-------------------------------------|---------------------|---------|------------|----------------------------------|

Stock roles: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 -- Scope pre-assessment:** For each role, state whether the assigned BU scope is appropriate or over-permissioned. Place `[SCOPE AMBIGUOUS]` inline if undeterminable.

**1.4 -- Initialize SECURITY STATE REGISTER:** Set all roles to `PENDING-PHASE-2`.

**1.5 -- Analysis order:** "I will trace entities in this order: [list, highest sensitivity first]. First gap ID: G-01."

**PHASE 1 EXIT GATE -- this phase produces:**

> **ENTITY CATALOG** (entity name | org-wide default | sensitivity | reason for sensitivity)
> **ROLE CATALOG** (role name | type | BU scope | purpose | has write? | column security profiles)

Phase 2 SHALL reference ENTITY CATALOG from Phase 1 and ROLE CATALOG from Phase 1 by these exact names.

---

### PHASE 2 -- Per-Entity Trace

**Input required:** ENTITY CATALOG from Phase 1. ROLE CATALOG from Phase 1.

For each entity (highest sensitivity first):

**2a -- Operations per role:**

| Entity | Role | Create | Read | Write | Delete | Record Scope |
|--------|------|--------|------|-------|--------|--------------|

**2b -- Sensitive field FLS status:**

| Entity | Field | Sensitivity | FLS Profile (YES/NO/UNKNOWN) | Role | Can Read? | Can Write? | Sentinel |
|--------|-------|-------------|------------------------------|------|-----------|------------|---------|

Gap rule: High/Medium sensitivity + NO FLS profile + role has Read -> `[GAP-FLS-fieldname]` inline, [G-##], Gap Type = MISSING-FLS, Risk = CRITICAL.

**Routing rule -- FLS sentinels:** Any `[GAP-FLS-*]` MUST have [G-##] AND appear in Phase 6 SENTINEL INVENTORY.

**2c -- Escalation path check (Write roles only):**

| Vector | Roles | Verdict | Sentinel (if POSSIBLE) | Evidence |
|--------|-------|---------|----------------------|----------|
| Record Assign | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-assign]` | |
| Share to higher-privilege role | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-share]` | |
| Field modification affecting role/BU | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-field-modify]` | |
| Team self-addition | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-team-self]` | |
| Admin role override | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-admin-override]` | |

**Routing rule -- escalation sentinels:** Any `[GAP-ESC-*]` MUST have [G-##] AND appear in Phase 6 SENTINEL INVENTORY.

**2d -- SECURITY STATE UPDATE (every role, every entity):**
- Sentinel: `[Role] -- FLAGGED [token, G-##]. Source: Phase 2 / [Entity].`
- No finding: `[Role] -- INERTIA: [prior verdict], no finding on [Entity].`

**PHASE 2 EXIT GATE -- this phase produces:**

> **ACCESS MATRIX** (entity | role | create | read | write | delete | record scope -- all roles x all entities)
> **FLS SENTINEL TABLE** (entity | field | sensitivity | FLS profile | role | can read | sentinel token | G-##)
> **ESCALATION FINDINGS** (entity | vector | roles | verdict | sentinel token | G-##)

Phase 3 SHALL reference ACCESS MATRIX from Phase 2, FLS SENTINEL TABLE from Phase 2, and ESCALATION FINDINGS from Phase 2 by these exact names.

---

### PHASE 3 -- Sharing Rule Analysis

**Input required:** ROLE CATALOG from Phase 1. ACCESS MATRIX from Phase 2. ESCALATION FINDINGS from Phase 2.

For each role, produce a SHARING RULE VERDICT block:

#### SHARING RULE VERDICT: [Role name]

| Entity | Sharing Rules Found? | Rule Name | Access Expanded Beyond OWD+Role? | Verdict | Sentinel |
|--------|---------------------|-----------|----------------------------------|---------|---------|

- `"Confirmed: no rules expand [Role] access on [Entity]. OWD=[value], scope=[scope]. Method: [audit method]."`
- `"CONFLICT FOUND: [Rule] grants [Role] access to [record set]. Exceeds design intent: [reason]."` Place `[GAP-SHARE-rulename]`. Assign [G-##], Gap Type = SHARING-CONFLICT.

**Routing rule -- sharing sentinels:** Any `[GAP-SHARE-*]` MUST have [G-##] AND appear in Phase 6 SENTINEL INVENTORY.

**SECURITY STATE UPDATE:** Conflict -> `FLAGGED`. No conflict -> `INERTIA` carry-forward.

**PHASE 3 EXIT GATE -- this phase produces:**

> **SHARING VERDICTS** (role | entity | sharing rules found | access expanded | verdict | sentinel | G-##)

Phase 4 SHALL reference SHARING VERDICTS from Phase 3 by this exact name.

---

### PHASE 4 -- Coverage Gate

**Input required:** ACCESS MATRIX from Phase 2. FLS SENTINEL TABLE from Phase 2. ESCALATION FINDINGS from Phase 2. SHARING VERDICTS from Phase 3.

| Role | ACCESS MATRIX: All Entities? | SHARING VERDICTS Written? | State Register Non-PENDING? | Current Verdict | Active Sentinels |
|------|------------------------------|--------------------------|----------------------------|-----------------|-----------------|

Gate assertion: "All [N] entities in ACCESS MATRIX. All [N] roles have SHARING VERDICTS. Zero PENDING-PHASE entries. Total [G-##]: [N]. Total sentinels: [types and counts]. Proceeding to Phase 5."

**PHASE 4 EXIT GATE -- this phase produces:**

> **COVERAGE GATE CONFIRMATION** (all-entities-traced: YES | all-sharing-verdicts: YES | state-consistent: YES | total gaps: N | total sentinels: N)

Phase 5 SHALL reference COVERAGE GATE CONFIRMATION from Phase 4.

---

### PHASE 5 -- Cross-Entity Cascade

**Input required:** ACCESS MATRIX from Phase 2. COVERAGE GATE CONFIRMATION from Phase 4.

**5a -- Relationship map (two highest-sensitivity entities):**

| Source | Relationship Type | Target | Cascade Behavior |
|--------|-------------------|--------|-----------------|

**5b -- Cascade access trace:**

`[Role] -> [Source, access, scope] -> [Relationship + cascade] -> [Target, resulting access]` -> INTENTIONAL or EMERGENT

EMERGENT: `[GAP-ESC-cascade-[entity]]` inline. [G-##], Gap Type = CASCADE-OVERREACH.

**Routing rule:** Any `[GAP-ESC-cascade-*]` MUST appear in Phase 6 SENTINEL INVENTORY as Phase 5 addition.

**5c -- SECURITY STATE UPDATE:** Cascade gap -> FLAGGED. No finding -> INERTIA.

**PHASE 5 EXIT GATE -- this phase produces:**

> **CASCADE FINDINGS** (role | source | relationship | target | INTENTIONAL/EMERGENT | sentinel | G-##)

---

### PHASE 6 -- Sentinel Inventory

**Input required:** FLS SENTINEL TABLE from Phase 2. ESCALATION FINDINGS from Phase 2. SHARING VERDICTS from Phase 3. CASCADE FINDINGS from Phase 5. SECURITY GAP REGISTER.

**6a -- SENTINEL INVENTORY:**

| Sentinel Token | Type | Phase Placed | Entity | Field / Operation | Role(s) | G-## |
|---------------|------|-------------|--------|------------------|---------|------|

**Routing verification:**
- "Total `[GAP-FLS-*]` placed: [N]. All in inventory: [YES/NO]."
- "Total `[GAP-ESC-*]` placed: [N]. All in inventory: [YES/NO]."
- "Total `[GAP-SHARE-*]` placed: [N]. All in inventory: [YES/NO]."
- "Total `[SCOPE AMBIGUOUS]` placed: [N]. All in inventory: [YES/NO]."
- "Total `[UNCHECKED]` placed: [N]. All in inventory: [YES/NO]."
- "Total [G-##] in SECURITY GAP REGISTER: [N]. All referenced: [YES/NO]."

If any NO: name the missing token and source phase. Do not proceed.

**6b -- Aggregate gap list (derived from SENTINEL INVENTORY):**

| Gap ID | Sentinel Token | Type | Entity | Field / Operation | Role(s) | Risk | Source Phase | Remediation |
|--------|---------------|------|--------|------------------|---------|------|-------------|-------------|

**PHASE 6 EXIT GATE -- this phase produces:**

> **SENTINEL INVENTORY** (all sentinel tokens | type | phase | entity | role | G-##)
> **AGGREGATE GAP LIST** (G-## | sentinel token | type | entity | role | risk | source phase)

Phase 7 SHALL reference AGGREGATE GAP LIST from Phase 6 by this exact name.

---

### PHASE 7 -- Cross-Role Differential Analysis (SHALL-enforced)

**Input required:** AGGREGATE GAP LIST from Phase 6. ACCESS MATRIX from Phase 2. ROLE CATALOG from Phase 1.

**SHALL instructions:**

The model **SHALL** compare access differentials across all roles for each operation in ACCESS MATRIX from Phase 2.

For each role pair, the model **SHALL** state one of:
- `EXPECTED DIFFERENTIAL -- [Role A] has [specific named access] that [Role B] does not because [reason tied to purpose].`
- `CANDIDATE OVER-PERMISSION -- [Role A] has [named access] that exceeds [stated purpose] relative to [Role B]. Access in question: [named operation or field].`

The model **SHALL NOT** conclude "differential appears expected" without naming the specific access elements compared and the purpose justification.

The model **SHALL** assign `[GAP-ESC-overpermission-[role]]` and [G-##] for every CANDIDATE OVER-PERMISSION.

| Role Pair | Entity | Operation | Role A Access | Role B Access | Conclusion |
|-----------|--------|-----------|--------------|--------------|------------|

**SECURITY STATE UPDATE:** CANDIDATE OVER-PERMISSION -> `FLAGGED [sentinel, G-##]`. No finding -> carry-forward.

**PHASE 7 EXIT GATE -- this phase produces:**

> **DIFFERENTIAL FINDINGS** (role pair | entity | operation | Role A access | Role B access | conclusion -- all role pairs x all entities)
> **OVER-PERMISSION ASSIGNMENTS** (G-## | sentinel token | entity | roles | gap type -- all CANDIDATE OVER-PERMISSION verdicts from this phase)

Phase 8 SHALL reference DIFFERENTIAL FINDINGS from Phase 7 and OVER-PERMISSION ASSIGNMENTS from Phase 7 by these exact names. A Phase 8 that begins without naming these artifacts is a terminal dependency failure.

---

### PHASE 8 -- Remediation and Defense-in-Depth

> **Structural purpose:** Prevents FM-P11 (non-actionable remediation). This is the terminal phase.

**Input required:** AGGREGATE GAP LIST from Phase 6. OVER-PERMISSION ASSIGNMENTS from Phase 7. DIFFERENTIAL FINDINGS from Phase 7.
**Dependency check:** If any named artifact is incomplete, name the missing content before proceeding.

**8a -- Gap remediation (cite by [G-##] and sentinel token):**

For each row in AGGREGATE GAP LIST from Phase 6 plus all rows in OVER-PERMISSION ASSIGNMENTS from Phase 7:

`[G-##] [sentinel token]: Apply [specific change] to [exact Dataverse configuration object] in [solution location]. Current state: [...]. Target state: [...]. Post-fix behavior: [...].`

Exact Dataverse configuration objects: column security profile name, security role privilege + table name, team type + membership rule, sharing rule name, OWD value per entity. Generic advice fails.

**8b -- Defense-in-depth assessment (two highest-sensitivity entities):**

| Entity | Layer 1: Env / Admin Role | Layer 2: Security Role + BU Scope | Layer 3: Team Membership | Layer 4: FLS / Column Security Profile | Effective Enforcement Layer |
|--------|--------------------------|----------------------------------|--------------------------|---------------------------------------|----------------------------|

For at least one operation on at least one entity: identify the Effective Enforcement Layer and explain why upper layers do not override it.

**8c -- Stock role summary:**

For each stock Dataverse role present in ROLE CATALOG from Phase 1: baseline privileges, how modified, whether necessary or removable.

**Final SECURITY STATE REGISTER:** Copy in final form. Every role: `CLEARED` or `FLAGGED [sentinel list, G-## list]`. No PENDING-PHASE entries.

**PHASE 8 EXIT GATE -- this phase produces:**

> **REMEDIATION REGISTER** (G-## | sentinel token | exact configuration object | specific change | post-fix behavior -- one row per gap)
> **DEFENSE-IN-DEPTH ASSESSMENT** (entity | four-layer verdict | effective enforcement layer named -- two highest-sensitivity entities)
> **FINAL SECURITY STATE REGISTER** (role | final verdict | active sentinels | active gap IDs -- all roles, no PENDING-PHASE entries)

This is the terminal phase. The phase chain is complete when all three artifacts are populated and FINAL SECURITY STATE REGISTER has zero PENDING-PHASE entries. The full 8-phase dependency chain (Phase 1 EXIT GATE -> Phase 2 INPUT -> Phase 2 EXIT GATE -> Phase 3 INPUT -> ... -> Phase 8 EXIT GATE) is now closed at every boundary.

---

## V-03 -- Count-Comparison Coverage Gate (C-22 single-axis)

**Axis:** Phase dependency chaining -- explicit count-comparison COVERAGE GATE COUNT block with PASS/FAIL before aggregation (C-22 single-axis)
**Hypothesis:** V-05/R7 Phase 4 gate assertion reads "All [N] entities in ACCESS MATRIX" where N is filled in from memory at assertion time. C-19 routing rules guarantee every discovered gap reaches the register, but they cannot detect that 3 of 6 entities were never analyzed -- routing rules applied to a partial analysis produce a correctly-routed partial result. C-22 requires a count-comparison formula that independently verifies analysis completeness before aggregation begins: "ENTITY CATALOG declared [M] entities. ACCESS MATRIX contains [N] entities. M == N: YES/NO. GATE STATUS: PASS/FAIL." When M != N, the gate fails and aggregation is blocked until the missing entities are named and traced. This closes the loop C-19 cannot: routing correctness does not imply routing completeness.

---

You are running a permissions trace signal for: **{{topic}}**

---

## CONTEXT -- Why Permissions Tracing Fails: Skill-Level Threat Model

**FM-SKILL-1 -- FLS post-incident discovery.** FLS gaps invisible at role level; must be traced separately.

**FM-SKILL-2 -- Cumulative scope blindness.** Role combinations produce effective access invisible to per-role analysis.

**FM-SKILL-3 -- Verdict drift.** Prior verdicts overridden at phase transitions without carry-forward.

**FM-SKILL-4 -- Output-schema drift.** Undeclared output schemas make consuming-phase artifact references coincidental.

**FM-SKILL-5 -- Routing gap.** Inline discoveries don't reach the gap inventory without explicit routing rules.

**FM-SKILL-7 -- Partial-analysis aggregation blindness.** Routing rules guarantee every discovery reaches the register -- they do not guarantee every entity was analyzed. An analysis covering 3 of 6 entities satisfies all routing rules perfectly while the 3 unanalyzed entities are invisible. The coverage gate catches routing failures (C-19 closed this); the count-comparison gate catches analysis scope failures (C-22 closes this). Neither substitutes for the other: a routing-rule PASS with a count-match FAIL means gaps were correctly routed from an incomplete analysis.

These failure modes motivate: FLS sentinels (FM-SKILL-1), cascade + differential (FM-SKILL-2), SECURITY STATE REGISTER (FM-SKILL-3), exit gates (FM-SKILL-4), routing rules (FM-SKILL-5), and count-comparison coverage gate (FM-SKILL-7).

Use Dataverse-native terminology throughout. At least four Dataverse-specific terms must appear and be used accurately.

---

## FAILURE MODE MAP

| Structural Element | Defends Against |
|-------------------|-----------------|
| Phase 1 -- complete entity + role catalog | FM-P1 |
| Sentinel tokens placed inline | FM-SKILL-1 + FM-P2 |
| Phase 2 -- FLS SENTINEL TABLE + ESCALATION FINDINGS | FM-SKILL-1 + FM-P3 |
| Phase 3 -- SHARING RULE VERDICT blocks | FM-SKILL-2 + FM-P4 |
| Phase 4 -- COVERAGE GATE COUNT (M == N formula) | FM-SKILL-7 (partial-analysis aggregation blindness) |
| Phase 4 -- coverage gate role/verdict check | FM-P5 |
| Named exit gate declarations at end of each phase | FM-SKILL-4 + FM-P6 |
| Aggregation routing rules | FM-SKILL-5 + FM-P7 |
| Phase 6 -- SENTINEL INVENTORY | FM-SKILL-5 + FM-P8 |
| SECURITY STATE REGISTER + inertia | FM-SKILL-3 + FM-P9 |
| Phase 7 -- SHALL cross-role differential | FM-SKILL-2 + FM-P10 |
| Phase 8 -- exact object remediation | FM-P11 |

---

**SECURITY GAP REGISTER -- assign [G-##] at point of discovery. Never defer.**

| ID | Sentinel Token | Entity | Field / Operation | Role(s) | Gap Type | Risk | Source Phase |
|----|---------------|--------|-------------------|---------|----------|------|-------------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH

**Sentinel token vocabulary:**
- `[GAP-FLS-fieldname]` -- FLS gap discovery row
- `[GAP-ESC-vectorname]` -- POSSIBLE escalation vector row
- `[GAP-SHARE-rulename]` -- sharing conflict verdict row
- `[SCOPE AMBIGUOUS]` -- BU scope undeterminable
- `[UNCHECKED]` -- vector unevaluable

**Sentinel placement rule:** Inline at point of discovery. No batching.

---

**SECURITY STATE REGISTER -- authoritative per-role verdict record.**

| Role | Phase Last Updated | Current Verdict | Active Sentinel Tokens | Active Gap IDs |
|------|--------------------|-----------------|----------------------|----------------|

Verdict values: `CLEARED` / `FLAGGED [sentinels, G-##]` / `PENDING-PHASE-[N]`

**Inertia rule:** Every Phase N verdict is the persistent default entering Phase N+1. No-finding notation required for every role in every phase.

**Phase dependency protocol:** Each phase declares required inputs by artifact name. Proceed only when declared inputs are present.

---

### PHASE 1 -- Inventory

**Input required:** System description.

**1.1 -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

**1.2 -- Role catalog:**

| Role | Type (Stock / Custom / Team / Env) | Business Unit Scope | Purpose | Has Write? | Column Security Profiles Attached |
|------|-------------------------------------|---------------------|---------|------------|----------------------------------|

Stock roles: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 -- Scope pre-assessment:** State whether each role's BU scope is appropriate or over-permissioned. `[SCOPE AMBIGUOUS]` if undeterminable.

**1.4 -- Initialize SECURITY STATE REGISTER:** All roles to `PENDING-PHASE-2`.

**1.5 -- Analysis order:** "Entities in order: [list]. First gap ID: G-01."

**PHASE 1 EXIT GATE -- this phase produces:**

> **ENTITY CATALOG** (entity | OWD | sensitivity | reason) -- entity count M = [N declared here]
> **ROLE CATALOG** (role | type | BU scope | purpose | has write? | profiles) -- role count M = [N declared here]

Phase 2 SHALL reference ENTITY CATALOG from Phase 1 and ROLE CATALOG from Phase 1. Entity count M is the authoritative count for the Phase 4 coverage gate.

---

### PHASE 2 -- Per-Entity Trace

**Input required:** ENTITY CATALOG from Phase 1. ROLE CATALOG from Phase 1.

For each entity (highest sensitivity first):

**2a -- Operations per role:**

| Entity | Role | Create | Read | Write | Delete | Record Scope |
|--------|------|--------|------|-------|--------|--------------|

**2b -- Sensitive field FLS status:**

| Entity | Field | Sensitivity | FLS Profile (YES/NO/UNKNOWN) | Role | Can Read? | Can Write? | Sentinel |
|--------|-------|-------------|------------------------------|------|-----------|------------|---------|

`[GAP-FLS-fieldname]` + [G-##] for High/Medium + NO FLS + role has Read. **Routing rule:** Any `[GAP-FLS-*]` MUST appear in Phase 6 SENTINEL INVENTORY.

**2c -- Escalation path check (Write roles only):**

| Vector | Roles | Verdict | Sentinel (if POSSIBLE) | Evidence |
|--------|-------|---------|----------------------|----------|
| Record Assign | | | `[GAP-ESC-assign]` | |
| Share to higher-privilege role | | | `[GAP-ESC-share]` | |
| Field modification affecting role/BU | | | `[GAP-ESC-field-modify]` | |
| Team self-addition | | | `[GAP-ESC-team-self]` | |
| Admin role override | | | `[GAP-ESC-admin-override]` | |

**Routing rule:** Any `[GAP-ESC-*]` MUST appear in Phase 6 SENTINEL INVENTORY.

**2d -- SECURITY STATE UPDATE (every role, every entity).**

**PHASE 2 EXIT GATE -- this phase produces:**

> **ACCESS MATRIX** (entity | role | create | read | write | delete | record scope -- all roles x all entities) -- entity count in matrix: [N]
> **FLS SENTINEL TABLE** (entity | field | sensitivity | FLS profile | role | can read | sentinel | G-##)
> **ESCALATION FINDINGS** (entity | vector | roles | verdict | sentinel | G-##)

Phase 3 SHALL reference ACCESS MATRIX from Phase 2, FLS SENTINEL TABLE from Phase 2, ESCALATION FINDINGS from Phase 2.

---

### PHASE 3 -- Sharing Rule Analysis

**Input required:** ROLE CATALOG from Phase 1. ACCESS MATRIX from Phase 2. ESCALATION FINDINGS from Phase 2.

For each role: SHARING RULE VERDICT block.

#### SHARING RULE VERDICT: [Role name]

| Entity | Sharing Rules Found? | Rule Name | Access Expanded Beyond OWD+Role? | Verdict | Sentinel |
|--------|---------------------|-----------|----------------------------------|---------|---------|

- Confirmed: `"OWD=[value], scope=[scope]. Method: [audit method]."`
- Conflict: Place `[GAP-SHARE-rulename]`. [G-##], Gap Type = SHARING-CONFLICT.

Every entity in ACCESS MATRIX that this role touches must appear.

**Routing rule:** Any `[GAP-SHARE-*]` MUST appear in Phase 6 SENTINEL INVENTORY.

**SECURITY STATE UPDATE** after each verdict block.

**PHASE 3 EXIT GATE -- this phase produces:**

> **SHARING VERDICTS** (role | entity | rules found | access expanded | verdict | sentinel | G-##)

Phase 4 SHALL reference SHARING VERDICTS from Phase 3.

---

### PHASE 4 -- Coverage Gate

**Input required:** ENTITY CATALOG from Phase 1. ACCESS MATRIX from Phase 2. SHARING VERDICTS from Phase 3.

**COVERAGE GATE COUNT (required before Phase 6 aggregation may begin):**

| Dimension | Declared in Phase 1 | Present in Analysis | Match? | Gate Status |
|-----------|--------------------|--------------------|--------|-------------|
| Entities | [M from ENTITY CATALOG from Phase 1] | [N distinct entities in ACCESS MATRIX from Phase 2] | M == N: YES/NO | PASS / FAIL |
| Roles (sharing) | [M from ROLE CATALOG from Phase 1] | [N roles with SHARING VERDICTS from Phase 3] | M == N: YES/NO | PASS / FAIL |

**Count-match rule:** Entities analyzed MUST equal entities declared in ENTITY CATALOG from Phase 1. Roles with sharing verdicts MUST equal roles declared in ROLE CATALOG from Phase 1. A FAIL on either row MUST be resolved by naming the missing entity or role and completing its trace before this gate can advance to PASS.

**GATE ASSERTION:** "ENTITY CATALOG declared [M] entities. ACCESS MATRIX contains [N] entities. M == N: [YES/NO]. ROLE CATALOG declared [M] roles. SHARING VERDICTS written for [N] roles. M == N: [YES/NO]. GATE STATUS: [PASS / FAIL]. Phase 6 aggregation [authorized / blocked pending resolution of: [list missing items]]."

Phase 6 aggregation SHALL NOT begin until GATE STATUS = PASS on both rows.

**Secondary gate (state consistency):**

| Role | State Register Non-PENDING? | Current Verdict | Active Sentinels |
|------|----------------------------|-----------------|-----------------|

Gate assertion: "Zero PENDING-PHASE entries. Total [G-##]: [N]. Total sentinels: [types and counts]. Proceeding to Phase 5."

**PHASE 4 EXIT GATE -- this phase produces:**

> **COVERAGE GATE CONFIRMATION** (entities-declared: M | entities-traced: N | M==N: YES | roles-declared: M | roles-sharing: N | M==N: YES | state-consistent: YES | total gaps: N | gate-status: PASS)

Phase 5 SHALL reference COVERAGE GATE CONFIRMATION from Phase 4. A COVERAGE GATE CONFIRMATION with GATE STATUS = FAIL is a hard stop.

---

### PHASE 5 -- Cross-Entity Cascade

**Input required:** ACCESS MATRIX from Phase 2. COVERAGE GATE CONFIRMATION from Phase 4.

**5a -- Relationship map (two highest-sensitivity entities):**

| Source | Relationship Type | Target | Cascade Behavior |
|--------|-------------------|--------|-----------------|

**5b -- Cascade access trace:**

`[Role] -> [Source, access, scope] -> [Relationship + cascade] -> [Target, resulting access]` -> INTENTIONAL or EMERGENT

EMERGENT: `[GAP-ESC-cascade-[entity]]` inline. [G-##], Gap Type = CASCADE-OVERREACH. **Routing rule:** Must appear in Phase 6 SENTINEL INVENTORY.

**SECURITY STATE UPDATE:** EMERGENT -> FLAGGED. No finding -> INERTIA.

**PHASE 5 EXIT GATE -- this phase produces:**

> **CASCADE FINDINGS** (role | source | relationship | target | INTENTIONAL/EMERGENT | sentinel | G-##)

---

### PHASE 6 -- Sentinel Inventory

**Input required:** FLS SENTINEL TABLE from Phase 2. ESCALATION FINDINGS from Phase 2. SHARING VERDICTS from Phase 3. CASCADE FINDINGS from Phase 5. SECURITY GAP REGISTER. COVERAGE GATE CONFIRMATION from Phase 4 (GATE STATUS must be PASS before this phase proceeds).

**6a -- SENTINEL INVENTORY:**

| Sentinel Token | Type | Phase Placed | Entity | Field / Operation | Role(s) | G-## |
|---------------|------|-------------|--------|------------------|---------|------|

**Routing verification:**
- "`[GAP-FLS-*]`: [N] placed, [YES/NO] all in inventory."
- "`[GAP-ESC-*]`: [N] placed, [YES/NO] all in inventory."
- "`[GAP-SHARE-*]`: [N] placed, [YES/NO] all in inventory."
- "`[SCOPE AMBIGUOUS]`: [N], [YES/NO]."
- "`[UNCHECKED]`: [N], [YES/NO]."
- "[G-##] in register: [N]. All referenced: [YES/NO]."

If any NO: name missing token and source phase. Do not proceed.

**6b -- Aggregate gap list:**

| Gap ID | Sentinel Token | Type | Entity | Field / Operation | Role(s) | Risk | Source Phase | Remediation |
|--------|---------------|------|--------|------------------|---------|------|-------------|-------------|

**PHASE 6 EXIT GATE -- this phase produces:**

> **SENTINEL INVENTORY** (all tokens | type | phase | entity | role | G-##)
> **AGGREGATE GAP LIST** (G-## | sentinel token | type | entity | role | risk | source phase)

Phase 7 SHALL reference AGGREGATE GAP LIST from Phase 6.

---

### PHASE 7 -- Cross-Role Differential Analysis (SHALL-enforced)

**Input required:** ACCESS MATRIX from Phase 2. SECURITY STATE REGISTER. ROLE CATALOG from Phase 1.

The model **SHALL** compare all role pairs for every operation in ACCESS MATRIX. Every pair gets one of:
- `EXPECTED DIFFERENTIAL -- [Role A] has [specific access] that [Role B] does not because [stated-purpose reason].`
- `CANDIDATE OVER-PERMISSION -- [Role A] has [named access] that exceeds [purpose] relative to [Role B]. Access in question: [named].`

**SHALL NOT** conclude "expected" without naming specific access elements and purpose justification.

**SHALL** assign `[GAP-ESC-overpermission-[role]]` + [G-##] for every CANDIDATE OVER-PERMISSION.

| Role Pair | Entity | Operation | Role A Access | Role B Access | Conclusion |
|-----------|--------|-----------|--------------|--------------|------------|

**SECURITY STATE UPDATE:** CANDIDATE OVER-PERMISSION -> FLAGGED. No finding -> carry-forward.

---

### PHASE 8 -- Remediation and Defense-in-Depth

**Input required:** AGGREGATE GAP LIST from Phase 6 (updated with Phase 7 additions).

**8a -- Gap remediation:**

`[G-##] [sentinel token]: Apply [specific change] to [exact Dataverse object]. Current state: [...]. Target state: [...]. Post-fix behavior: [...].`

**8b -- Defense-in-depth assessment:**

| Entity | Layer 1: Env / Admin Role | Layer 2: Security Role + BU | Layer 3: Team | Layer 4: FLS / Column Profile | Effective Enforcement Layer |
|--------|--------------------------|----------------------------|---------------|------------------------------|----------------------------|

For at least one operation: identify effective layer and explain why upper layers do not override it.

**8c -- Stock role summary:** For each stock role: baseline privileges, how modified, whether removable.

**Final SECURITY STATE REGISTER:** All roles `CLEARED` or `FLAGGED`. No PENDING-PHASE entries.

---

## V-04 -- Combined: C-20 + C-21 (Required Column + Complete Phase Chain)

**Axis:** Combined output format + lifecycle emphasis -- required "Why Upper Layers Don't Override" column (C-20) + Phase 7 and Phase 8 EXIT GATE declarations (C-21)
**Hypothesis:** C-20 and C-21 are structurally independent and additive: C-20 targets Phase 8b output format (adds a 6th column), C-21 targets Phase 7 and Phase 8 boundary declarations (adds exit gates). Neither change interferes with the other. The combination tests whether the Phase 8 exit gate reinforces C-20 by requiring the "Why Upper Layers Don't Override" column to be populated as a precondition for exit gate satisfaction -- making the exit gate double as a C-20 enforcement point: PHASE 8 EXIT GATE artifact "DEFENSE-IN-DEPTH ASSESSMENT" must include the Why column data, making a blank Why cell both a C-20 failure and a gate incompletion. Combined: +5.0 pts under v6.

---

You are running a permissions trace signal for: **{{topic}}**

---

## CONTEXT -- Why Permissions Tracing Fails: Skill-Level Threat Model

**FM-SKILL-1 -- FLS post-incident discovery.** FLS gaps invisible at role level; traced separately.

**FM-SKILL-2 -- Cumulative scope blindness.** Role combinations produce effective access invisible to per-role analysis.

**FM-SKILL-3 -- Verdict drift.** Prior verdicts overridden at phase transitions without carry-forward.

**FM-SKILL-4 -- Output-schema drift.** Undeclared output schemas make consuming-phase references coincidental. Applies to terminal phases: Phase 7 produces DIFFERENTIAL FINDINGS consumed by Phase 8; without a Phase 7 EXIT GATE the dependency is undeclared.

**FM-SKILL-5 -- Routing gap.** Inline discoveries don't reach the gap inventory without explicit routing rules.

**FM-SKILL-6 -- Layer-override reasoning truncation.** Defense-in-depth table names the effective enforcement layer (C-09) but leaves the causal "why upper layers don't override" as a prose instruction. Without a required column, the model satisfies C-09 while the causal reasoning is never demanded structurally.

These failure modes motivate: FLS sentinels (FM-SKILL-1), cascade + differential (FM-SKILL-2), SECURITY STATE REGISTER (FM-SKILL-3), exit gates at all 8 phase boundaries including terminal phases (FM-SKILL-4), routing rules (FM-SKILL-5), required Why column (FM-SKILL-6).

Use Dataverse-native terminology. At least four terms must appear and be used accurately.

---

## FAILURE MODE MAP

| Structural Element | Defends Against |
|-------------------|-----------------|
| Phase 1 -- entity + role catalog | FM-P1 |
| Sentinel tokens inline | FM-SKILL-1 + FM-P2 |
| Phase 2 -- FLS SENTINEL TABLE + ESCALATION FINDINGS | FM-SKILL-1 + FM-P3 |
| Phase 3 -- SHARING RULE VERDICT blocks | FM-SKILL-2 + FM-P4 |
| Phase 4 -- coverage gate | FM-P5 |
| Named exit gate declarations at end of ALL 8 phases | FM-SKILL-4 (including terminal phases 7 and 8) |
| Aggregation routing rules | FM-SKILL-5 + FM-P7 |
| Phase 6 -- SENTINEL INVENTORY | FM-SKILL-5 + FM-P8 |
| SECURITY STATE REGISTER + inertia | FM-SKILL-3 + FM-P9 |
| Phase 7 -- SHALL cross-role differential | FM-SKILL-2 + FM-P10 |
| Phase 8b -- required "Why Upper Layers Don't Override" column | FM-SKILL-6 (layer-override reasoning truncation) |
| Phase 8 -- exact Dataverse object remediation | FM-P11 |

---

**SECURITY GAP REGISTER -- assign [G-##] at point of discovery. Never defer.**

| ID | Sentinel Token | Entity | Field / Operation | Role(s) | Gap Type | Risk | Source Phase |
|----|---------------|--------|-------------------|---------|----------|------|-------------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH

**Sentinel token vocabulary:**
- `[GAP-FLS-fieldname]` / `[GAP-ESC-vectorname]` / `[GAP-SHARE-rulename]` / `[SCOPE AMBIGUOUS]` / `[UNCHECKED]`

**Sentinel placement rule:** Inline at discovery. No batching.

---

**SECURITY STATE REGISTER**

| Role | Phase Last Updated | Current Verdict | Active Sentinel Tokens | Active Gap IDs |
|------|--------------------|-----------------|----------------------|----------------|

**Inertia rule:** Phase N verdict is persistent default entering Phase N+1. No-finding notation required for every role.

**Phase dependency protocol:** Each phase declares required inputs. Proceed only when declared inputs present.

---

### PHASE 1 -- Inventory

**Input required:** System description.

**1.1 -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

**1.2 -- Role catalog:**

| Role | Type | Business Unit Scope | Purpose | Has Write? | Column Security Profiles |
|------|------|---------------------|---------|------------|--------------------------|

Stock roles: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 -- Scope pre-assessment.** **1.4 -- Initialize SECURITY STATE REGISTER** (all PENDING-PHASE-2). **1.5 -- Analysis order** (highest sensitivity first, first gap G-01).

**PHASE 1 EXIT GATE -- this phase produces:**

> **ENTITY CATALOG** (entity | OWD | sensitivity | reason)
> **ROLE CATALOG** (role | type | BU scope | purpose | has write? | profiles)

Phase 2 SHALL reference ENTITY CATALOG from Phase 1 and ROLE CATALOG from Phase 1.

---

### PHASE 2 -- Per-Entity Trace

**Input required:** ENTITY CATALOG from Phase 1. ROLE CATALOG from Phase 1.

For each entity (highest sensitivity first):

**2a -- Operations per role:**

| Entity | Role | Create | Read | Write | Delete | Record Scope |
|--------|------|--------|------|-------|--------|--------------|

**2b -- Sensitive field FLS status:**

| Entity | Field | Sensitivity | FLS Profile | Role | Can Read? | Can Write? | Sentinel |
|--------|-------|-------------|-------------|------|-----------|------------|---------|

`[GAP-FLS-fieldname]` + [G-##] for High/Medium + NO FLS + Read. Routing: must reach Phase 6 SENTINEL INVENTORY.

**2c -- Escalation check (Write roles):**

| Vector | Roles | Verdict | Sentinel | Evidence |
|--------|-------|---------|----------|----------|
| Record Assign | | | `[GAP-ESC-assign]` | |
| Share to higher-privilege role | | | `[GAP-ESC-share]` | |
| Field modification affecting role/BU | | | `[GAP-ESC-field-modify]` | |
| Team self-addition | | | `[GAP-ESC-team-self]` | |
| Admin role override | | | `[GAP-ESC-admin-override]` | |

Routing: `[GAP-ESC-*]` must reach Phase 6 SENTINEL INVENTORY.

**2d -- SECURITY STATE UPDATE** (every role, every entity).

**PHASE 2 EXIT GATE -- this phase produces:**

> **ACCESS MATRIX** (entity | role | create | read | write | delete | scope -- all roles x all entities)
> **FLS SENTINEL TABLE** (entity | field | sensitivity | profile | role | can read | sentinel | G-##)
> **ESCALATION FINDINGS** (entity | vector | roles | verdict | sentinel | G-##)

Phase 3 SHALL reference ACCESS MATRIX, FLS SENTINEL TABLE, ESCALATION FINDINGS from Phase 2.

---

### PHASE 3 -- Sharing Rule Analysis

**Input required:** ROLE CATALOG from Phase 1. ACCESS MATRIX from Phase 2. ESCALATION FINDINGS from Phase 2.

For each role: SHARING RULE VERDICT block.

#### SHARING RULE VERDICT: [Role name]

| Entity | Sharing Rules Found? | Rule Name | Access Expanded? | Verdict | Sentinel |
|--------|---------------------|-----------|-----------------|---------|---------|

Conflict: `[GAP-SHARE-rulename]` + [G-##]. Every entity the role touches must appear.

Routing: `[GAP-SHARE-*]` must reach Phase 6 SENTINEL INVENTORY. SECURITY STATE UPDATE after each block.

**PHASE 3 EXIT GATE -- this phase produces:**

> **SHARING VERDICTS** (role | entity | rules found | access expanded | verdict | sentinel | G-##)

Phase 4 SHALL reference SHARING VERDICTS from Phase 3.

---

### PHASE 4 -- Coverage Gate

**Input required:** ACCESS MATRIX from Phase 2. SHARING VERDICTS from Phase 3.

| Role | ACCESS MATRIX Complete? | SHARING VERDICTS Written? | State Non-PENDING? | Verdict | Active Sentinels |
|------|------------------------|--------------------------|-------------------|---------|-----------------|

Gate assertion: "All [N] entities. All [N] roles have sharing verdicts. Zero PENDING-PHASE entries. Total [G-##]: [N]. Proceeding."

**PHASE 4 EXIT GATE -- this phase produces:**

> **COVERAGE GATE CONFIRMATION** (all-entities: YES | all-sharing: YES | state-consistent: YES | total gaps: N)

Phase 5 SHALL reference COVERAGE GATE CONFIRMATION from Phase 4.

---

### PHASE 5 -- Cross-Entity Cascade

**Input required:** ACCESS MATRIX from Phase 2. COVERAGE GATE CONFIRMATION from Phase 4.

**5a -- Relationship map:**

| Source | Relationship Type | Target | Cascade Behavior |
|--------|-------------------|--------|-----------------|

**5b -- Cascade trace:** `[Role] -> [Source] -> [Relationship] -> [Target]` -> INTENTIONAL or EMERGENT

EMERGENT: `[GAP-ESC-cascade-[entity]]` + [G-##]. Routing: must reach Phase 6.

**SECURITY STATE UPDATE.** EMERGENT -> FLAGGED. No finding -> INERTIA.

**PHASE 5 EXIT GATE -- this phase produces:**

> **CASCADE FINDINGS** (role | source | relationship | target | verdict | sentinel | G-##)

---

### PHASE 6 -- Sentinel Inventory

**Input required:** FLS SENTINEL TABLE from Phase 2. ESCALATION FINDINGS from Phase 2. SHARING VERDICTS from Phase 3. CASCADE FINDINGS from Phase 5. SECURITY GAP REGISTER.

**SENTINEL INVENTORY:**

| Sentinel Token | Type | Phase | Entity | Field / Op | Role(s) | G-## |
|---------------|------|-------|--------|-----------|---------|------|

**Routing verification:** Counts for all token types. Any NO -> name missing token and phase, do not proceed.

**Aggregate gap list:**

| Gap ID | Sentinel | Type | Entity | Field / Op | Role(s) | Risk | Source Phase | Remediation |
|--------|----------|------|--------|-----------|---------|------|-------------|-------------|

**PHASE 6 EXIT GATE -- this phase produces:**

> **SENTINEL INVENTORY** (all tokens | type | phase | entity | role | G-##)
> **AGGREGATE GAP LIST** (G-## | sentinel | type | entity | role | risk | source phase)

Phase 7 SHALL reference AGGREGATE GAP LIST from Phase 6.

---

### PHASE 7 -- Cross-Role Differential Analysis (SHALL-enforced)

**Input required:** ACCESS MATRIX from Phase 2. SECURITY STATE REGISTER. ROLE CATALOG from Phase 1.

**SHALL:** Compare all role pairs on all operations. Every pair: `EXPECTED DIFFERENTIAL` or `CANDIDATE OVER-PERMISSION` (with named access elements and purpose justification). N*(N-1)/2 assessments required. CANDIDATE OVER-PERMISSION: `[GAP-ESC-overpermission-[role]]` + [G-##]. SECURITY STATE UPDATE.

| Role Pair | Entity | Operation | Role A Access | Role B Access | Conclusion |
|-----------|--------|-----------|--------------|--------------|------------|

**PHASE 7 EXIT GATE -- this phase produces:**

> **DIFFERENTIAL FINDINGS** (role pair | entity | operation | Role A access | Role B access | conclusion -- all role pairs x all entities)
> **OVER-PERMISSION ASSIGNMENTS** (G-## | sentinel token | entity | roles | gap type)

Phase 8 SHALL reference DIFFERENTIAL FINDINGS from Phase 7 and OVER-PERMISSION ASSIGNMENTS from Phase 7 by these exact names. A Phase 8 that begins without naming these artifacts is a terminal dependency failure.

---

### PHASE 8 -- Remediation and Defense-in-Depth

**Input required:** AGGREGATE GAP LIST from Phase 6. OVER-PERMISSION ASSIGNMENTS from Phase 7. DIFFERENTIAL FINDINGS from Phase 7.
**Dependency check:** If any named artifact is incomplete, name the missing content before proceeding.

**8a -- Gap remediation:**

`[G-##] [sentinel token]: Apply [specific change] to [exact Dataverse object]. Current state: [...]. Target state: [...]. Post-fix behavior: [...].`

Exact objects: column security profile name, security role privilege + table name, team type + membership rule, sharing rule name, OWD value per entity. Generic advice fails.

**8b -- Defense-in-depth assessment (two highest-sensitivity entities):**

| Entity | Layer 1: Env / Admin Role | Layer 2: Security Role + BU Scope | Layer 3: Team Membership | Layer 4: FLS / Column Security Profile | Effective Enforcement Layer | Why Upper Layers Don't Override |
|--------|--------------------------|----------------------------------|--------------------------|---------------------------------------|----------------------------|---------------------------------|

**Column rules:**
- **Effective Enforcement Layer**: the lowest layer that independently enforces the access decision.
- **Why Upper Layers Don't Override**: MUST be populated for at least one entity and one operation. State the specific mechanism reason why the layers above the Effective Enforcement Layer cannot independently grant or deny the same access. Acceptable: "Layer 2 security role grants org-wide Read; the column security profile in Layer 4 is the only mechanism that restricts access to [field] specifically -- Layer 2 does not evaluate field visibility." Unacceptable: "by design", "see above", blank. A blank cell FAILS C-20 regardless of C-09 satisfaction.

**8c -- Stock role summary.**

**Final SECURITY STATE REGISTER:** All roles CLEARED or FLAGGED. No PENDING-PHASE entries.

**PHASE 8 EXIT GATE -- this phase produces:**

> **REMEDIATION REGISTER** (G-## | sentinel | exact object | change | post-fix behavior -- one row per gap)
> **DEFENSE-IN-DEPTH ASSESSMENT** (entity | four-layer verdict | effective enforcement layer | why upper layers don't override -- Why column populated for at least one entity/operation)
> **FINAL SECURITY STATE REGISTER** (role | verdict | sentinels | gap IDs -- no PENDING-PHASE entries)

Phase chain is complete when all three artifacts are populated and Why column has at least one non-blank entry. Full 8-phase chain closed at all boundaries.

---

## V-05 -- Full Combination: C-20 + C-21 + C-22 (All Three New Criteria)

**Axis:** Full structural integration -- required Why column (C-20) + complete 8-phase chain with terminal exit gates (C-21) + count-comparison coverage gate (C-22) on V-05/R7 foundation
**Hypothesis:** The three new criteria address three independent failure modes not covered by the C-01 through C-19 scaffold: FM-SKILL-6 (layer-override reasoning truncation -- C-20 closes it), terminal-phase output-schema drift at Phase 7/Phase 8 boundaries (C-21 closes it as the logical end-state of C-11+C-18 applied uniformly), and FM-SKILL-7 (partial-analysis aggregation blindness -- C-22 closes it independently of C-19). Each mechanism is structurally independent: C-20 modifies Phase 8b output format; C-21 adds Phase 7 and Phase 8 exit gates; C-22 adds a count-comparison block to Phase 4. No interference between mechanisms. The combined addition targets 125.0/125.0 under rubric v6 -- all 22 criteria satisfied simultaneously.

---

You are running a permissions trace signal for: **{{topic}}**

---

## CONTEXT -- Why Permissions Tracing Fails: Skill-Level Threat Model

Before any analysis begins, understand the seven failure modes that permissions tracing is structurally prone to produce:

**FM-SKILL-1 -- FLS post-incident discovery.** Field-level security gaps are invisible at the security role level. A role can be correctly scoped -- right operations, right entities, right BU scope -- while a sensitive field has no column security profile. FLS must be traced as a separate analytical pass distinct from operation-level role analysis.

**FM-SKILL-2 -- Cumulative scope blindness.** Each individual role may be scoped correctly. The failure occurs when role combinations -- team inheritance, sharing records, environment admin override, cascade relationships -- produce an effective access scope that no single-role analysis predicts.

**FM-SKILL-3 -- Verdict drift.** Role verdicts assigned early are silently overridden at phase transitions. A CLEARED verdict from Phase 2 is re-evaluated from scratch in Phase 3, sometimes with a different conclusion -- not because new evidence was found, but because the prior verdict was not carried forward.

**FM-SKILL-4 -- Output-schema drift.** If the producing phase never declares its output schema, consuming-phase artifact references are best guesses. Applies equally to terminal phases: Phase 7 produces DIFFERENTIAL FINDINGS consumed by Phase 8; without a Phase 7 EXIT GATE, that dependency is undeclared and the name reference is coincidental.

**FM-SKILL-5 -- Routing gap.** Violation discoveries placed inline during traversal phases do not automatically reach the gap inventory. Explicit routing rules are required at every discovery-to-inventory boundary.

**FM-SKILL-6 -- Layer-override reasoning truncation.** The defense-in-depth table names the effective enforcement layer (C-09 pass) but leaves the causal "why upper layers don't override" as a prose instruction. Without a required column, the model satisfies C-09 while the causal reasoning is never demanded structurally.

**FM-SKILL-7 -- Partial-analysis aggregation blindness.** Routing rules guarantee every discovery reaches the register -- they do not guarantee every entity was analyzed. An analysis covering 3 of 6 entities satisfies all routing rules perfectly while 3 entities remain unanalyzed. A count-comparison gate independently catches analysis scope failures invisible to routing-rule passes.

These failure modes motivate the structure of this analysis: FLS sentinels (FM-SKILL-1), cascade + differential (FM-SKILL-2), SECURITY STATE REGISTER (FM-SKILL-3), exit gates at all 8 phase boundaries (FM-SKILL-4), routing rules (FM-SKILL-5), required Why column (FM-SKILL-6), count-comparison gate (FM-SKILL-7).

Use Dataverse-native terminology throughout: business units, security roles, owner teams, access teams, column security profiles, table permissions, sharing records, environment roles. At least four Dataverse-specific terms must appear and be used accurately.

---

## FAILURE MODE MAP

Read this map before Phase 1. A structural element absent from the output leaves its failure mode unmitigated.

| Structural Element | Defends Against |
|-------------------|-----------------|
| Phase 1 -- complete entity + role catalog | FM-P1: Incorrect coverage undetectable once analysis begins |
| Sentinel tokens inline at discovery | FM-SKILL-1 + FM-P2 |
| Phase 2 -- FLS SENTINEL TABLE + ESCALATION FINDINGS | FM-SKILL-1 + FM-P3 |
| Phase 3 -- SHARING RULE VERDICT blocks per role | FM-SKILL-2 + FM-P4 |
| Phase 4 -- COVERAGE GATE COUNT (M == N formula) | FM-SKILL-7 (partial-analysis aggregation blindness) |
| Phase 4 -- role/verdict coverage gate | FM-P5 |
| Named exit gate declarations at end of ALL 8 phases | FM-SKILL-4 (output-schema drift -- terminal phases included) |
| Aggregation routing rules | FM-SKILL-5 + FM-P7 |
| Phase 6 -- SENTINEL INVENTORY | FM-SKILL-5 + FM-P8 |
| SECURITY STATE REGISTER + inertia | FM-SKILL-3 + FM-P9 |
| Phase 7 -- SHALL cross-role differential | FM-SKILL-2 + FM-P10 |
| Phase 8b -- required "Why Upper Layers Don't Override" column | FM-SKILL-6 (layer-override reasoning truncation) |
| Phase 8 -- exact Dataverse object remediation | FM-P11 |

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

**Sentinel placement rule:** Every sentinel MUST be placed inline at the exact point of discovery. Do not batch or invent at summary time.

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

> **ENTITY CATALOG** (entity name | org-wide default | sensitivity | reason for sensitivity) -- entity count M declared here
> **ROLE CATALOG** (role name | type | BU scope | purpose | has write? | column security profiles) -- role count M declared here

Phase 2 SHALL reference ENTITY CATALOG from Phase 1 and ROLE CATALOG from Phase 1 by these exact names. Entity count M and role count M from this gate are the authoritative counts for the Phase 4 COVERAGE GATE COUNT.

---

### PHASE 2 -- Per-Entity Trace

> **Structural purpose:** Prevents FM-SKILL-1 (FLS discovery) + FM-P3 (verdict scatter). **Inertia requirement:** SECURITY STATE REGISTER updated after every entity section.

**Input required:** ENTITY CATALOG from Phase 1. ROLE CATALOG from Phase 1.
**Dependency check:** If either named artifact is incomplete, name the missing content before proceeding.

For each entity (highest sensitivity first):

**2a -- Operations per role:**

| Entity | Role | Create | Read | Write | Delete | Record Scope |
|--------|------|--------|------|-------|--------|--------------|

**2b -- Sensitive field FLS status:**

| Entity | Field | Sensitivity | FLS Profile (YES/NO/UNKNOWN) | Role | Can Read? | Can Write? | Sentinel |
|--------|-------|-------------|------------------------------|------|-----------|------------|---------|

Gap rule: High/Medium sensitivity + NO FLS profile + role has Read -> place `[GAP-FLS-fieldname]` inline, assign [G-##]. Gap Type = MISSING-FLS. Risk = CRITICAL.

**Routing rule -- FLS sentinels:** Any `[GAP-FLS-*]` sentinel placed in this table MUST have a [G-##] in the SECURITY GAP REGISTER AND MUST appear in Phase 6 SENTINEL INVENTORY by sentinel token name.

**2c -- Escalation path check (Write roles only):**

| Vector | Roles | Verdict | Sentinel (if POSSIBLE) | Evidence |
|--------|-------|---------|----------------------|----------|
| Record Assign | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-assign]` | |
| Share to higher-privilege role | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-share]` | |
| Field modification affecting role/BU | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-field-modify]` | |
| Team self-addition | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-team-self]` | |
| Admin role override | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-admin-override]` | |

NOT POSSIBLE requires naming the ruling-out check. POSSIBLE: sentinel inline, [G-##].

**Routing rule -- escalation sentinels:** Any `[GAP-ESC-*]` MUST have [G-##] AND appear in Phase 6 SENTINEL INVENTORY.

**2d -- SECURITY STATE UPDATE (required for every role after every entity):**
- Sentinel placed: `[Role] -- FLAGGED [sentinel token, G-##]. Source: Phase 2 / [Entity].`
- No finding: `[Role] -- INERTIA: [prior verdict], no finding on [Entity].`

**PHASE 2 EXIT GATE -- this phase produces:**

> **ACCESS MATRIX** (entity | role | create | read | write | delete | record scope -- all roles x all entities) -- entity count in matrix: [N, must equal M from Phase 1]
> **FLS SENTINEL TABLE** (entity | field | sensitivity | FLS profile | role | can read | sentinel token | G-##)
> **ESCALATION FINDINGS** (entity | vector | roles | verdict | sentinel token | G-##)

Phase 3 SHALL reference ACCESS MATRIX from Phase 2, FLS SENTINEL TABLE from Phase 2, and ESCALATION FINDINGS from Phase 2 by these exact names.

---

### PHASE 3 -- Sharing Rule Analysis

> **Structural purpose:** Prevents FM-SKILL-2 (sharing below role scope) + FM-P4. **Inertia requirement:** SECURITY STATE REGISTER updated after each SHARING RULE VERDICT.

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

**Routing rule:** Any `[GAP-SHARE-*]` MUST appear in Phase 6 SENTINEL INVENTORY.

**SECURITY STATE UPDATE after each block:** Conflict -> FLAGGED. No conflict -> INERTIA carry-forward.

**PHASE 3 EXIT GATE -- this phase produces:**

> **SHARING VERDICTS** (role | entity | sharing rules found | access expanded | verdict | sentinel | G-##)

Phase 4 SHALL reference SHARING VERDICTS from Phase 3.

---

### PHASE 4 -- Coverage Gate

> **Structural purpose:** Prevents FM-SKILL-7 (partial-analysis aggregation blindness) + FM-P5. **Security state consistency gate:** Zero PENDING-PHASE entries before Phase 5.

**Input required:** ENTITY CATALOG from Phase 1. ROLE CATALOG from Phase 1. ACCESS MATRIX from Phase 2. SHARING VERDICTS from Phase 3.
**Dependency check:** If any named artifact is missing, stop before proceeding.

**COVERAGE GATE COUNT (required before Phase 6 aggregation may begin):**

| Dimension | Declared in Phase 1 | Present in Analysis | Match? | Gate Status |
|-----------|--------------------|--------------------|--------|-------------|
| Entities | [M from ENTITY CATALOG from Phase 1] | [N distinct entities in ACCESS MATRIX from Phase 2] | M == N: YES/NO | PASS / FAIL |
| Roles (sharing) | [M from ROLE CATALOG from Phase 1] | [N roles with SHARING VERDICTS from Phase 3] | M == N: YES/NO | PASS / FAIL |

**Count-match rule:** Entities analyzed MUST equal entities declared in ENTITY CATALOG from Phase 1. Roles with sharing verdicts MUST equal roles declared in ROLE CATALOG from Phase 1. A FAIL on either row MUST be resolved by naming the missing entity or role and completing its trace before this gate advances to PASS.

**GATE ASSERTION:** "ENTITY CATALOG declared [M] entities. ACCESS MATRIX contains [N] entities. M == N: [YES/NO]. ROLE CATALOG declared [M] roles. SHARING VERDICTS written for [N] roles. M == N: [YES/NO]. GATE STATUS: [PASS / FAIL]. Phase 6 aggregation [authorized / blocked pending: [list missing items]]."

Phase 6 aggregation SHALL NOT begin until GATE STATUS = PASS on both rows.

**Secondary gate (state consistency):**

| Role | ACCESS MATRIX: All Entities? | SHARING VERDICTS Written? | State Non-PENDING? | Current Verdict | Active Sentinels |
|------|------------------------------|--------------------------|-------------------|-----------------|-----------------|

Secondary assertion: "Zero PENDING-PHASE entries in SECURITY STATE REGISTER. Total [G-##]: [N]. Total sentinels placed: [types and counts]. Proceeding to Phase 5."

Stop condition: PENDING-PHASE entry or missing SHARING VERDICT -- resolve before continuing.

**PHASE 4 EXIT GATE -- this phase produces:**

> **COVERAGE GATE CONFIRMATION** (entities-declared: M | entities-traced: N | M==N: YES | roles-declared: M | roles-sharing: N | M==N: YES | state-consistent: YES | total gaps: N | gate-status: PASS)

Phase 5 SHALL reference COVERAGE GATE CONFIRMATION from Phase 4. A COVERAGE GATE CONFIRMATION with gate-status FAIL is a hard stop.

---

### PHASE 5 -- Cross-Entity Cascade

> **Structural purpose:** Prevents FM-SKILL-2 (relationship-derived access). **Inertia requirement:** Non-cascade roles carry forward Phase 4 verdict.

**Input required:** ACCESS MATRIX from Phase 2. COVERAGE GATE CONFIRMATION from Phase 4.

**5a -- Relationship map (two highest-sensitivity entities):**

| Source | Relationship Type | Target | Cascade Behavior |
|--------|-------------------|--------|-----------------|

**5b -- Cascade access trace:**

`[Role] -> [Source, access, scope] -> [Relationship + cascade] -> [Target, resulting access]` -> INTENTIONAL or EMERGENT

EMERGENT: `[GAP-ESC-cascade-[entity]]` inline. [G-##], Gap Type = CASCADE-OVERREACH.

**Routing rule:** Any `[GAP-ESC-cascade-*]` MUST appear in Phase 6 SENTINEL INVENTORY as Phase 5 addition.

**5c -- SECURITY STATE UPDATE:**
- Cascade gap: `[Role] -- FLAGGED [GAP-ESC-cascade-*, G-##]. Source: Phase 5.`
- No finding: `[Role] -- INERTIA: [verdict] from Phase 4, no cascade finding.`

**PHASE 5 EXIT GATE -- this phase produces:**

> **CASCADE FINDINGS** (role | source | relationship | target | INTENTIONAL/EMERGENT | sentinel | G-##)

---

### PHASE 6 -- Sentinel Inventory

> **Structural purpose:** Prevents FM-SKILL-5 (routing gap). Aggregates all discovery-point tokens. Gap list derives from this inventory, not from memory.

**Input required:** FLS SENTINEL TABLE from Phase 2. ESCALATION FINDINGS from Phase 2. SHARING VERDICTS from Phase 3. CASCADE FINDINGS from Phase 5. SECURITY GAP REGISTER. COVERAGE GATE CONFIRMATION from Phase 4 (GATE STATUS must be PASS before this phase begins).

**6a -- SENTINEL INVENTORY (complete aggregation):**

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

> **Structural purpose:** Prevents FM-SKILL-2 (cumulative scope blindness). **Inertia requirement:** SECURITY STATE REGISTER verdicts are authoritative. This phase does not re-derive verdicts from scratch.

**Input required:** AGGREGATE GAP LIST from Phase 6. ACCESS MATRIX from Phase 2. ROLE CATALOG from Phase 1.

**SHALL instructions -- structural requirements, not guidelines:**

The model **SHALL** compare access differentials across all roles in ROLE CATALOG from Phase 1 for each operation in ACCESS MATRIX from Phase 2.

For each role pair, the model **SHALL** state an explicit conclusion -- one of:
- `EXPECTED DIFFERENTIAL -- [Role A] has [specific named access] that [Role B] does not because [reason tied to Role A's stated purpose]. The differential is consistent with the roles' design intent.`
- `CANDIDATE OVER-PERMISSION -- [Role A] has [specific named access] that exceeds what [Role A's stated purpose] requires relative to [Role B]. Access in question: [named operation or field].`

The model **SHALL NOT** conclude "differential appears expected" without naming specific access elements compared and the purpose justification.

The model **SHALL** process every role pair. For N roles: N*(N-1)/2 assessments required.

The model **SHALL** assign `[GAP-ESC-overpermission-[role]]` and [G-##] for every CANDIDATE OVER-PERMISSION. Gap Type = BU-SCOPE. Add to AGGREGATE GAP LIST as Phase 7 addition.

**Differential Analysis Table:**

| Role Pair | Entity | Operation | Role A Access | Role B Access | Conclusion |
|-----------|--------|-----------|--------------|--------------|------------|

Conclusion cell: full statement -- not a verdict code.

**SECURITY STATE UPDATE:** CANDIDATE OVER-PERMISSION -> `FLAGGED [sentinel, G-##]. Source: Phase 7.` No finding -> carry-forward notation.

**PHASE 7 EXIT GATE -- this phase produces:**

> **DIFFERENTIAL FINDINGS** (role pair | entity | operation | Role A access | Role B access | conclusion -- all role pairs x all entities)
> **OVER-PERMISSION ASSIGNMENTS** (G-## | sentinel token | entity | roles | gap type -- all CANDIDATE OVER-PERMISSION verdicts)

Phase 8 SHALL reference DIFFERENTIAL FINDINGS from Phase 7 and OVER-PERMISSION ASSIGNMENTS from Phase 7 by these exact names. A Phase 8 that begins without naming these artifacts is a terminal dependency failure.

---

### PHASE 8 -- Remediation and Defense-in-Depth

> **Structural purpose:** Prevents FM-P11 (non-actionable remediation) + FM-SKILL-6 (layer-override reasoning truncation). Terminal phase.

**Input required:** AGGREGATE GAP LIST from Phase 6. OVER-PERMISSION ASSIGNMENTS from Phase 7. DIFFERENTIAL FINDINGS from Phase 7.
**Dependency check:** If any named artifact is incomplete, name the missing content before proceeding.

**8a -- Gap remediation (cite by [G-##] and sentinel token):**

For each row in AGGREGATE GAP LIST from Phase 6 plus all rows in OVER-PERMISSION ASSIGNMENTS from Phase 7:

`[G-##] [sentinel token]: Apply [specific change] to [exact Dataverse configuration object] in [solution location]. Current state: [what exists today]. Target state: [what it should be]. Post-fix behavior: [what a user can / cannot do].`

Exact Dataverse configuration objects required: column security profile name (not "add FLS"), security role privilege name + table name (not "tighten the role"), team type (owner/access) + membership rule (not "fix team membership"), sharing rule name (not "remove the rule"), OWD value per entity (not "adjust OWD"). Generic advice fails.

**8b -- Defense-in-depth assessment (two highest-sensitivity entities):**

| Entity | Layer 1: Env / Admin Role | Layer 2: Security Role + BU Scope | Layer 3: Team Membership | Layer 4: FLS / Column Security Profile | Effective Enforcement Layer | Why Upper Layers Don't Override |
|--------|--------------------------|----------------------------------|--------------------------|---------------------------------------|----------------------------|---------------------------------|

**Column rules:**
- **Effective Enforcement Layer**: name the specific layer (Layer 1 / 2 / 3 / 4) that independently enforces the access decision for the operation in question.
- **Why Upper Layers Don't Override**: MUST be populated for at least one entity and one operation. State the specific mechanism reason why the layers above the Effective Enforcement Layer cannot independently grant or deny the same access. Acceptable forms: "Layer 2 security role grants org-wide Read; only the Layer 4 column security profile restricts access to [field] specifically -- Layer 2 does not evaluate field visibility" or "Layer 1 admin role does not block entity-level create; the restriction is enforced solely by Layer 2 security role privilege which evaluates before team-level access is checked." Unacceptable: "by design", "see above", blank. A blank cell in this column FAILS C-20 regardless of C-09 satisfaction.

**8c -- Stock role summary:**

For each stock Dataverse role present in ROLE CATALOG from Phase 1: baseline privileges, how modified in this scenario, whether necessary or removable.

**Final SECURITY STATE REGISTER:** Copy in final form. Every role must have `CLEARED` or `FLAGGED [sentinel list, G-## list]`. No PENDING-PHASE entries.

**PHASE 8 EXIT GATE -- this phase produces:**

> **REMEDIATION REGISTER** (G-## | sentinel token | exact configuration object | specific change | post-fix behavior -- one row per gap)
> **DEFENSE-IN-DEPTH ASSESSMENT** (entity | four-layer verdict | effective enforcement layer | why upper layers don't override -- Why column MUST be populated for at least one entity/operation; a blank Why column fails the exit gate)
> **FINAL SECURITY STATE REGISTER** (role | final verdict | active sentinels | active gap IDs -- all roles, zero PENDING-PHASE entries)

This is the terminal phase. The phase chain is complete when:
1. All three artifacts are populated
2. Why column has at least one non-blank entry (C-20 enforcement)
3. FINAL SECURITY STATE REGISTER has zero PENDING-PHASE entries
4. COVERAGE GATE CONFIRMATION from Phase 4 confirmed GATE STATUS = PASS (C-22 enforcement)

Full 8-phase dependency chain closed at all boundaries: Phase 1 EXIT GATE -> Phase 2 INPUT -> Phase 2 EXIT GATE -> Phase 3 INPUT -> Phase 3 EXIT GATE -> Phase 4 INPUT -> Phase 4 EXIT GATE -> Phase 5 INPUT -> Phase 5 EXIT GATE -> Phase 6 INPUT -> Phase 6 EXIT GATE -> Phase 7 INPUT -> Phase 7 EXIT GATE -> Phase 8 INPUT -> Phase 8 EXIT GATE. No orphan phase boundaries.

---

## Variation Axis Summary

| Variation | C-20 | C-21 | C-22 | C-01-C-19 |
|-----------|------|------|------|-----------|
| V-01 | TARGETED (Why column in Phase 8b) | -- (Phase 7/8 orphans remain) | -- (gate assertion only) | INHERITS R7-v5-V-05 |
| V-02 | -- (prose instruction remains) | TARGETED (Phase 7 EXIT GATE + Phase 8 EXIT GATE) | -- | INHERITS R7-v5-V-05 |
| V-03 | -- | -- | TARGETED (COVERAGE GATE COUNT with M==N formula) | INHERITS R7-v5-V-05 |
| V-04 | TARGETED | TARGETED | -- | INHERITS R7-v5-V-05 |
| V-05 | TARGETED | TARGETED | TARGETED | INHERITS R7-v5-V-05 |

**Predicted scoring (rubric v6, max 125.0):**

| Variation | Essential | Rec | Aspirational passes | Predicted |
|-----------|-----------|-----|---------------------|-----------|
| V-01 | 60 | 30 | C-09 PASS, C-10-C-19 PASS, C-20 PASS | 120.0 |
| V-02 | 60 | 30 | C-09-C-19 PASS, C-21 PASS | 120.0 |
| V-03 | 60 | 30 | C-09-C-19 PASS, C-22 PASS | 120.0 |
| V-04 | 60 | 30 | C-09-C-19 PASS, C-20 PASS, C-21 PASS | 122.5 |
| V-05 | 60 | 30 | all 14 aspirational PASS | 125.0 |

**Key additions vs R7-v5-V-05 baseline:**

- **C-20 (Why column):** Added to V-01, V-04, V-05. Phase 8b defense-in-depth table gains a 6th required column. MUST-populate rule with acceptable/unacceptable form examples. Blank cell fails C-20 regardless of C-09 satisfaction. Phase 8 EXIT GATE in V-04/V-05 requires Why column populated as exit gate precondition.

- **C-21 (terminal phase exit gates):** Added to V-02, V-04, V-05. Phase 7 EXIT GATE declares DIFFERENTIAL FINDINGS and OVER-PERMISSION ASSIGNMENTS as named artifacts. Phase 8 INPUT REQUIRED now references Phase 7 artifacts by their declared names. Phase 8 EXIT GATE declares REMEDIATION REGISTER, DEFENSE-IN-DEPTH ASSESSMENT, FINAL SECURITY STATE REGISTER. FAILURE MODE MAP claim "Named exit gate declarations at end of each phase" is now true at all 8 phase boundaries.

- **C-22 (count-comparison gate):** Added to V-03, V-05. Phase 4 gains COVERAGE GATE COUNT block with M==N formula table, count-match rule, and GATE ASSERTION with PASS/FAIL output. Phase 6 aggregation blocked until GATE STATUS = PASS. COVERAGE GATE CONFIRMATION exit artifact includes gate-status field. FM-SKILL-7 added to CONTEXT and FAILURE MODE MAP.
