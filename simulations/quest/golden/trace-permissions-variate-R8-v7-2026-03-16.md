# trace-permissions Variate — Round 8 (Rubric v7)
**Date:** 2026-03-16
**Rubric:** v7 (C-01 through C-25 — 4 essential / 3 recommended / 18 aspirational)
**New criteria targeted this round:** C-24 (C-21 loop range phrase currency), C-25 (SHALL-L mandate extension for new criteria)
**Prior round retained:** All C-01..C-23 from R7-V-05 carried forward at full structural guarantee

**State entering Round 8:**

| Variation | v6 score (N=16) | Gap under v7 |
|-----------|-----------------|--------------|
| R7-V-05 (best v6) | 16/16 aspirational | C-21 mechanism phrase reads `C-08..C-23` — stale under v7; N=16 not 18 → C-24 FAIL (−4.35 pts); SHALL-L names only C-22/C-23 → C-25 FAIL (−4.35 pts); combined miss = −8.70 pts |
| Diagnostic C-17 | N=16, range=C-08..C-23 in self-assessment | v7 requires N=18, range declared as C-08..C-25 |
| Diagnostic C-24 | C-21 mechanism phrase: `C-08..C-23` | Stale literal string fails C-24; structural row presence does not substitute for phrase currency |
| Diagnostic C-25 | SHALL-L names C-22 and C-23 only | C-24/C-25 absent from SHALL-L; mechanism phrases in those cells are structural coincidence, not enforced obligation |

Round 8 holds the established v6 scaffold (8-phase trace, CONTEXT threat model with FM-SKILL-1..6,
FAILURE MODE MAP, SECURITY GAP REGISTER with sentinel tokens, SECURITY STATE REGISTER with inertia
rule, Phase 1–8 EXIT GATES, sentinel inventory, SHALL cross-role differential, exact-object
remediation, layer-override explanation column, count-comparison coverage gate) and adds C-24/C-25
mechanisms across three single-axis tests and two combined variations.

**Dependency notes entering Round 8:**
- C-24 auto-fails if C-21 fails. C-21 PASSES in R7-V-05 — dependency satisfied.
- C-25 auto-fails if C-19 fails. C-19 PASSES in R7-V-05 — dependency satisfied.

---

## Round 8 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format — C-24 single-axis: C-21 mechanism phrase range string updated from `C-08..C-23` to `C-08..C-25`; C-17 N updated to 18 | R7-V-05 self-assessment C-21 row reads "covers C-08..C-23 (16 rows)." v7 adds C-24/C-25, so the table now has 18 rows but the C-21 mechanism phrase is stale at 16. C-24 checks for the literal string `C-08..C-25` in that phrase — structural row coverage is irrelevant to the literal check. V-01 changes only the range string and N count in C-21 and C-17 rows. SHALL-L is unchanged (names C-22 and C-23 only) so C-25 FAILS by design. Isolated test: +4.35 pts (C-24 only). |
| V-02 | Phrasing register — C-25 single-axis: SHALL-L extended to name C-22, C-23, C-24, C-25 explicitly | R7-V-05 SHALL-L reads "observable mechanism phrases MUST appear in C-22 and C-23 Self-Assessment cells." V-03/R7 achieved this mandate for C-22/C-23 but did not extend to C-24/C-25 because those criteria did not exist in v6. Under v7, C-24 and C-25 rows are structurally present and contain mechanism phrases via inheritance — but without a SHALL-L naming mandate, presence is structurally coincident, not enforced obligation. V-02 extends SHALL-L to name C-22, C-23, C-24, C-25 explicitly. C-21 mechanism phrase retains `C-08..C-23` — C-24 FAILS by design. Isolated test: +4.35 pts (C-25 only). |
| V-03 | Output format — pre-printed mechanism cells: C-21 mechanism phrase cell and SHALL-L mandate line pre-printed with exact text; C-24/C-25 Self-Assessment cells carry pre-printed confirmation stubs | V-01 and V-02 rely on runtime generation for the C-21 phrase and SHALL-L text. A model carrying stale training or context pressure may generate the correct structure while producing a stale range string or incomplete SHALL-L list. Pre-printing the C-21 mechanism phrase cell as the literal text "...covers C-08..C-25 (18 rows)..." and pre-printing the SHALL-L line as "...MUST appear in C-22, C-23, C-24, and C-25 Self-Assessment cells" removes the model's degree of freedom to generate stale content. The model transcribes, not generates. Structural guarantee: the model cannot produce a stale phrase it did not write. Combines both axes at maximum mechanical reliability. |
| V-04 | Combined C-24 + C-25: range phrase update + SHALL-L mandate extension on R7-V-05 foundation | C-24 and C-25 are structurally independent — C-24 targets the C-21 mechanism phrase cell text; C-25 targets the SHALL-L instruction mandate. Neither interferes with the other. V-04 tests whether closing both simultaneously creates additive enforcement: the updated C-21 phrase provides the literal string C-24 requires; the updated SHALL-L closes the enforceability gap C-25 requires. C-17 updated to N=18 / C-08..C-25. Combined: +8.70 pts. Full v7 aspirational target achieved without pre-printing. |
| V-05 | Full integration: all C-01..C-25 + FM-SKILL-7 (self-assessment loop staleness) + pre-printed cells on R7-V-05 foundation | Adds FM-SKILL-7 "Self-Assessment Loop Staleness" to CONTEXT and FAILURE MODE MAP, naming the failure mode that C-24/C-25 structurally defend against. Applies V-04's combined C-24+C-25 update. Pre-prints C-21/C-24/C-25 self-assessment cells (from V-03's structural guarantee argument) for maximum mechanical reliability. The prompt explains why C-24/C-25 exist before producing the output, then enforces them mechanically. Full 25-criterion target at maximum structural guarantee. |

---

## V-01 — C-21 Range Phrase Update (C-24 single-axis)

**Axis:** Output format — C-24 single-axis: range string in C-21 mechanism phrase updated from `C-08..C-23` to `C-08..C-25`; C-17 N updated to 18
**Hypothesis:** R7-V-05 structurally passes C-21 (18 rows present, loop terminates) but the C-21 mechanism phrase reads "covers C-08..C-23 (16 rows)" — stale because v7 added C-24/C-25. C-24 checks for the literal string `C-08..C-25` in that phrase, not structural row coverage. V-01 changes only the range string and N count. SHALL-L is unchanged (names C-22 and C-23 only) → C-25 FAILS by design. Isolated single-axis test.

---

You are running a permissions trace signal for: **{{topic}}**

---

## CONTEXT — Why Permissions Tracing Fails: Skill-Level Threat Model

Before any analysis begins, understand the six failure modes that permissions tracing is structurally prone to produce:

**FM-SKILL-1 — FLS post-incident discovery.** Field-level security gaps are invisible at the security role level. A role can be correctly scoped — right operations, right entities, right BU scope — while a sensitive field has no column security profile. This gap surfaces only after an incident. FLS must be traced as a separate analytical pass distinct from operation-level role analysis.

**FM-SKILL-2 — Cumulative scope blindness.** Each individual role may be scoped correctly. The failure occurs when role combinations — team inheritance granting broader BU scope, sharing records granting record access below entity-level deny, environment admin roles elevating restricted roles, cascade relationships between entities — produce an effective access scope that no single-role analysis predicts.

**FM-SKILL-3 — Verdict drift.** Role verdicts assigned early in the analysis are silently overridden when the model transitions between phases. A CLEARED verdict from Phase 2 is re-evaluated from scratch in Phase 3, sometimes with a different conclusion — not because new evidence was found, but because the prior verdict was not carried forward.

**FM-SKILL-4 — Output-schema drift.** Phase dependency declarations reference artifacts from prior phases by name. If the producing phase never declares its output schema, the artifact name in the consuming phase is a best guess. When context pressure causes the producing phase to restructure its output, the name match breaks silently. This applies to terminal phases equally.

**FM-SKILL-5 — Routing gap.** Violation discoveries placed inline during traversal phases do not automatically reach the gap inventory. The model must remember which discoveries to aggregate. At the traversal-to-summary transition, discoveries without explicit routing rules are susceptible to omission.

**FM-SKILL-6 — Layer-override reasoning truncation.** The defense-in-depth table identifies the effective enforcement layer but the causal "why upper layers do not independently override" is left as a prose instruction after the table. Without a required column, the model names the correct layer while the reasoning is never demanded structurally. A required column converts the causal reasoning to a structural output requirement.

These failure modes motivate: dedicated FLS sentinel placement (FM-SKILL-1), cross-role differential and cascade phases (FM-SKILL-2), SECURITY STATE REGISTER with inertia framing (FM-SKILL-3), named exit gate artifact declarations at every phase boundary (FM-SKILL-4), explicit aggregation routing rules (FM-SKILL-5), required layer-override explanation column (FM-SKILL-6).

Use Dataverse-native terminology throughout: business units, security roles, owner teams, access teams, column security profiles, table permissions, sharing records, environment roles. At least four Dataverse-specific terms must appear and be used accurately.

---

## FAILURE MODE MAP

Read this map before Phase 1. A structural element absent from the output leaves its failure mode unmitigated.

| Structural Element | Defends Against |
|-------------------|-----------------|
| Phase 1 — complete entity + role catalog | FM-P1: Incorrect coverage undetectable once analysis begins |
| Sentinel tokens placed inline at point of discovery | FM-SKILL-1 + FM-P2: Discoveries not recorded at occurrence |
| Phase 2 — FLS SENTINEL TABLE + ESCALATION FINDINGS | FM-SKILL-1 (FLS gap invisible at role level) + FM-P3: Verdict scatter |
| Phase 3 — SHARING RULE VERDICT blocks per role | FM-SKILL-2 (sharing below role scope) + FM-P4 |
| Phase 4 — count-comparison COVERAGE GATE | FM-P5: Coverage loss at phase transition; partial analysis aggregated as complete |
| Named exit gate artifact declarations at end of all 8 phases | FM-SKILL-4 (output-schema drift) + FM-P6: Input references match coincidental names not declared contracts |
| Aggregation routing rules naming sentinel type and Phase 6 destination | FM-SKILL-5 (routing gap) + FM-P7 |
| Phase 6 — SENTINEL INVENTORY aggregated from inline sentinels | FM-SKILL-5 + FM-P8: Gap inventory re-created from memory |
| SECURITY STATE REGISTER + inertia carry-forward rule | FM-SKILL-3 (verdict drift) + FM-P9 |
| Phase 7 — SHALL cross-role differential | FM-SKILL-2 (cumulative scope blindness) + FM-P10 |
| Phase 8 — exact Dataverse object remediation | FM-P11: Generic advice non-actionable |
| Phase 8b — required "Why Upper Layers Don't Override" column | FM-SKILL-6 (layer-override reasoning truncation) |

---

**SECURITY GAP REGISTER — assign [G-##] at point of discovery. Never defer.**

| ID | Sentinel Token | Entity | Field / Operation | Role(s) | Gap Type | Risk | Source Phase |
|----|---------------|--------|-------------------|---------|----------|------|-------------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH

**Sentinel token vocabulary:**
- `[GAP-FLS-fieldname]` — placed inline at the FLS gap discovery row
- `[GAP-ESC-vectorname]` — placed inline at a POSSIBLE escalation vector row
- `[GAP-SHARE-rulename]` — placed inline at a sharing conflict verdict row
- `[SCOPE AMBIGUOUS]` — placed inline where BU scope cannot be assessed from provided context
- `[UNCHECKED]` — placed inline where a vector cannot be evaluated from provided context

**Sentinel placement rule:** Every sentinel MUST be placed inline at the exact point of discovery. Do not batch at section end or invent at summary time.

---

**SECURITY STATE REGISTER — authoritative per-role verdict record. Updated by every phase.**

| Role | Phase Last Updated | Current Verdict | Active Sentinel Tokens | Active Gap IDs |
|------|--------------------|-----------------|----------------------|----------------|

Verdict values: `CLEARED` / `FLAGGED [sentinels, G-##]` / `PENDING-PHASE-[N]`

**Inertia rule:** Every verdict from Phase N is the persistent default entering Phase N+1. When a phase finds nothing new for a role:
`[Role] — INERTIA: [verdict] from Phase [N], no new finding this phase.`
Required for every role in every phase. Absence = verdict unknown = detectable format failure.

**Phase dependency protocol:** Each phase declares its required inputs by artifact name. A phase SHALL NOT proceed without its declared inputs present.

---

### PHASE 1 — Inventory

> **Structural purpose:** Prevents FM-P1 (incomplete coverage). **Inertia initialization:** All roles set to `PENDING-PHASE-2` after catalogs complete.

**Input required:** System description from provided context.

**1.1 — Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

Sensitivity: High (PII, financial, credentials, health) / Medium (internal-only, cross-BU risk) / Low

**1.2 — Role catalog:**

| Role | Type (Stock / Custom / Team / Env) | Business Unit Scope | Purpose | Has Write? | Column Security Profiles Attached |
|------|-------------------------------------|---------------------|---------|------------|----------------------------------|

Stock roles to check: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 — Scope pre-assessment:** For each role, state whether the assigned BU scope is appropriate for its stated purpose or over-permissioned. Place `[SCOPE AMBIGUOUS]` inline if undeterminable. Assign [G-##] for any `[SCOPE AMBIGUOUS]` placement.

**1.4 — Initialize SECURITY STATE REGISTER:** Set all roles to `PENDING-PHASE-2`.

**1.5 — Analysis order:** "I will trace entities in this order: [list, highest sensitivity first]. First gap ID: G-01."

**PHASE 1 EXIT GATE — this phase produces:**

> **ENTITY CATALOG** (entity name | org-wide default | sensitivity | reason for sensitivity)
> **ROLE CATALOG** (role name | type | BU scope | purpose | has write? | column security profiles)

Phase 2 SHALL reference ENTITY CATALOG from Phase 1 and ROLE CATALOG from Phase 1 by these exact names. A Phase 2 that begins without naming both artifacts is a dependency failure.

---

### PHASE 2 — Per-Entity Trace

> **Structural purpose:** Prevents FM-SKILL-1 (FLS post-incident discovery) + FM-P3 (verdict scatter). **Inertia requirement:** SECURITY STATE REGISTER updated after every entity section.

**Input required:** ENTITY CATALOG from Phase 1. ROLE CATALOG from Phase 1.
**Dependency check:** If either named artifact is incomplete, name the missing content before proceeding.

For each entity (highest sensitivity first):

**2a — Operations per role:**

| Entity | Role | Create | Read | Write | Delete | Record Scope |
|--------|------|--------|------|-------|--------|--------------|

**2b — Sensitive field FLS status:**

Place sentinel inline at the discovery row. Then assign [G-##].

| Entity | Field | Sensitivity | FLS Profile (YES/NO/UNKNOWN) | Role | Can Read? | Can Write? | Sentinel |
|--------|-------|-------------|------------------------------|------|-----------|------------|---------|

Gap rule: High/Medium sensitivity + NO FLS profile + role has Read → place `[GAP-FLS-fieldname]` inline, assign [G-##]. Gap Type = MISSING-FLS. Risk = CRITICAL.

**Routing rule — FLS sentinels:** Any `[GAP-FLS-*]` sentinel placed in this table MUST have a [G-##] in the SECURITY GAP REGISTER AND MUST appear in Phase 6 SENTINEL INVENTORY by sentinel token name. A sentinel without a [G-##] is a routing failure.

**2c — Escalation path check (Write roles only):**

| Vector | Roles | Verdict | Sentinel (if POSSIBLE) | Evidence |
|--------|-------|---------|----------------------|----------|
| Record Assign | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-assign]` | |
| Share to higher-privilege role | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-share]` | |
| Field modification affecting role/BU | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-field-modify]` | |
| Team self-addition | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-team-self]` | |
| Admin role override | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-admin-override]` | |

NOT POSSIBLE requires naming the ruling-out check — not a bare assertion. POSSIBLE: place sentinel inline, assign [G-##].

**Routing rule — escalation sentinels:** Any `[GAP-ESC-*]` sentinel MUST have a [G-##] AND MUST appear in Phase 6 SENTINEL INVENTORY by token name.

**2d — SECURITY STATE UPDATE (required for every role after every entity):**
- Sentinel placed: `[Role] — FLAGGED [sentinel token, G-##]. Source: Phase 2 / [Entity].`
- No finding: `[Role] — INERTIA: [prior verdict], no finding on [Entity].`

**PHASE 2 EXIT GATE — this phase produces:**

> **ACCESS MATRIX** (entity | role | create | read | write | delete | record scope — all roles x all entities)
> **FLS SENTINEL TABLE** (entity | field | sensitivity | FLS profile | role | can read | sentinel token | G-##)
> **ESCALATION FINDINGS** (entity | vector | roles | verdict | sentinel token | G-##)

Phase 3 SHALL reference ACCESS MATRIX from Phase 2, FLS SENTINEL TABLE from Phase 2, and ESCALATION FINDINGS from Phase 2 by these exact names.

---

### PHASE 3 — Sharing Rule Analysis

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

**Routing rule — sharing sentinels:** Any `[GAP-SHARE-*]` sentinel MUST have a [G-##] AND MUST appear in Phase 6 SENTINEL INVENTORY by token name.

**SECURITY STATE UPDATE after each SHARING RULE VERDICT:**
- Conflict: `[Role] — FLAGGED [GAP-SHARE-*, G-##]. Source: Phase 3 / [Entity].`
- No conflict: `[Role] — INERTIA: [verdict] from Phase 2, sharing clean on [entity list].`

**PHASE 3 EXIT GATE — this phase produces:**

> **SHARING VERDICTS** (role | entity | sharing rules found | access expanded | verdict | sentinel token | G-##)

Phase 4 SHALL reference SHARING VERDICTS from Phase 3 by this exact name.

---

### PHASE 4 — Coverage Gate

> **Structural purpose:** Prevents FM-P5 (phase-transition coverage loss) + partial-analysis aggregation blindness.

**Input required:** ACCESS MATRIX from Phase 2. FLS SENTINEL TABLE from Phase 2. ESCALATION FINDINGS from Phase 2. SHARING VERDICTS from Phase 3.
**Dependency check:** If any named artifact is missing or incomplete, stop before proceeding.

**COUNT-COMPARISON COVERAGE GATE:**
ENTITY CATALOG from Phase 1 declared [M] entities.
ACCESS MATRIX from Phase 2 contains [N] entities.
M == N: YES / NO.
GATE STATUS: PASS / FAIL.
Aggregation and Phase 5 SHALL NOT begin until GATE STATUS = PASS. If FAIL: name the missing entity and resolve before continuing.

| Role | ACCESS MATRIX: All Entities? | SHARING VERDICTS Written? | State Register Non-PENDING? | Current Verdict | Active Sentinels |
|------|------------------------------|--------------------------|----------------------------|-----------------|-----------------|

Gate assertion: "All [N] entities in ACCESS MATRIX (M == N: YES). All [N] roles have SHARING VERDICTS. Zero PENDING-PHASE entries in SECURITY STATE REGISTER. Total [G-##]: [N]. Total sentinels placed: [types and counts]. Proceeding to Phase 5."

**PHASE 4 EXIT GATE — this phase produces:**

> **COVERAGE GATE CONFIRMATION** (entity-count declared: M | entity-count in ACCESS MATRIX: N | M==N: YES/NO | GATE STATUS: PASS/FAIL | all-sharing-verdicts: YES | state-consistent: YES | total gaps: N | total sentinels: N)

Phase 5 SHALL reference COVERAGE GATE CONFIRMATION from Phase 4.

---

### PHASE 5 — Cross-Entity Cascade

> **Structural purpose:** Prevents FM-SKILL-2 (relationship-derived access). **Inertia requirement:** Roles not involved in cascade carry forward Phase 4 verdict.

**Input required:** ACCESS MATRIX from Phase 2. COVERAGE GATE CONFIRMATION from Phase 4.

**5a — Relationship map (two highest-sensitivity entities):**

| Source | Relationship Type | Target | Cascade Behavior |
|--------|-------------------|--------|-----------------|

**5b — Cascade access trace:**

`[Role] -> [Source, access, scope] -> [Relationship + cascade] -> [Target, resulting access]` -> INTENTIONAL or EMERGENT

EMERGENT: place `[GAP-ESC-cascade-[entity]]` inline. Assign [G-##], Gap Type = CASCADE-OVERREACH.

**Routing rule — cascade sentinels:** Any `[GAP-ESC-cascade-*]` sentinel MUST have a [G-##] AND MUST appear in Phase 6 SENTINEL INVENTORY as a Phase 5 addition.

**5c — SECURITY STATE UPDATE:**
- Cascade gap: `[Role] — FLAGGED [GAP-ESC-cascade-*, G-##]. Source: Phase 5.`
- No finding: `[Role] — INERTIA: [verdict] from Phase 4, no cascade finding.`

**PHASE 5 EXIT GATE — this phase produces:**

> **CASCADE FINDINGS** (role | source | relationship | target | INTENTIONAL/EMERGENT | sentinel token | G-##)

Phase 6 SHALL reference CASCADE FINDINGS from Phase 5 by this exact name.

---

### PHASE 6 — Sentinel Inventory

> **Structural purpose:** Prevents FM-SKILL-5 (routing gap). The gap list derives from this inventory — not from memory.

**Input required:** FLS SENTINEL TABLE from Phase 2. ESCALATION FINDINGS from Phase 2. SHARING VERDICTS from Phase 3. CASCADE FINDINGS from Phase 5. SECURITY GAP REGISTER (all [G-##] rows).

**6a — SENTINEL INVENTORY (complete aggregation):**

List every sentinel placed in Phases 1–5, in phase order:

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

**6b — Aggregate gap list (derived from SENTINEL INVENTORY):**

| Gap ID | Sentinel Token | Type | Entity | Field / Operation | Role(s) | Risk | Source Phase | Remediation |
|--------|---------------|------|--------|------------------|---------|------|-------------|-------------|

Each row traces to an entry in the SENTINEL INVENTORY above.

**PHASE 6 EXIT GATE — this phase produces:**

> **SENTINEL INVENTORY** (all sentinel tokens | type | phase | entity | role | G-##)
> **AGGREGATE GAP LIST** (G-## | sentinel token | type | entity | role | risk | source phase)

Phase 7 SHALL reference AGGREGATE GAP LIST from Phase 6 by this exact name.

---

### PHASE 7 — Cross-Role Differential Analysis (SHALL-enforced)

> **Structural purpose:** Prevents FM-SKILL-2 (cumulative scope blindness). **Inertia requirement:** SECURITY STATE REGISTER verdicts are authoritative. This phase does not re-derive verdicts from scratch.

**Input required:** ACCESS MATRIX from Phase 2. SECURITY STATE REGISTER current state. ROLE CATALOG from Phase 1.

**SHALL instructions — structural requirements, not guidelines:**

The model **SHALL** compare access differentials across all roles in ROLE CATALOG from Phase 1 for each operation in ACCESS MATRIX from Phase 2.

For each role pair, the model **SHALL** state an explicit conclusion — one of:
- `EXPECTED DIFFERENTIAL — [Role A] has [specific named access] that [Role B] does not because [reason tied to Role A's stated purpose]. The differential is consistent with the roles' design intent.`
- `CANDIDATE OVER-PERMISSION — [Role A] has [specific named access] that exceeds what [Role A's stated purpose] requires relative to [Role B]. Access in question: [named operation or field]. This is a candidate for tightening.`

The model **SHALL NOT** conclude "differential appears expected" without naming the specific access elements compared and the purpose statement justifying the assessment.

The model **SHALL** process every role pair. For N roles: N*(N-1)/2 assessments required.

The model **SHALL** assign `[GAP-ESC-overpermission-[role]]` and [G-##] for every CANDIDATE OVER-PERMISSION. Gap Type = BU-SCOPE. Add to AGGREGATE GAP LIST from Phase 6 as Phase 7 addition.

**Differential Analysis Table:**

| Role Pair | Entity | Operation | Role A Access | Role B Access | Conclusion |
|-----------|--------|-----------|--------------|--------------|------------|

Conclusion cell: full statement — not a verdict code.

**SECURITY STATE UPDATE:** CANDIDATE OVER-PERMISSION -> `FLAGGED [sentinel, G-##]. Source: Phase 7.` No finding -> carry-forward notation.

**PHASE 7 EXIT GATE — this phase produces:**

> **DIFFERENTIAL FINDINGS** (role pair | entity | operation | Role A access | Role B access | conclusion | G-## if any)
> **OVER-PERMISSION ASSIGNMENTS** (role | entity | operation | sentinel token | G-## | gap type)

Phase 8 SHALL reference DIFFERENTIAL FINDINGS from Phase 7 and OVER-PERMISSION ASSIGNMENTS from Phase 7 by these exact names.

---

### PHASE 8 — Remediation and Defense-in-Depth

> **Structural purpose:** Prevents FM-P11 (non-actionable remediation) + FM-SKILL-6 (layer-override reasoning truncation).

**Input required:** AGGREGATE GAP LIST from Phase 6 updated with Phase 7 additions from OVER-PERMISSION ASSIGNMENTS from Phase 7.

**8a — Gap remediation (cite by [G-##] and sentinel token):**

For each row in AGGREGATE GAP LIST:

`[G-##] [sentinel token]: Apply [specific change] to [exact Dataverse configuration object] in [solution location]. Current state: [what exists today]. Target state: [what it should be]. Post-fix behavior: [what a user can / cannot do].`

Exact Dataverse configuration objects required: column security profile name (not "add FLS"), security role privilege name + table name (not "tighten the role"), team type + membership rule (not "fix team membership"), sharing rule name (not "remove the rule"), OWD value per entity (not "adjust OWD"). Generic advice fails.

**8b — Defense-in-depth assessment (two highest-sensitivity entities):**

| Entity | Layer 1: Env / Admin Role | Layer 2: Security Role + BU Scope | Layer 3: Team Membership | Layer 4: FLS / Column Security Profile | Effective Enforcement Layer | Why Upper Layers Don't Override |
|--------|--------------------------|----------------------------------|--------------------------|---------------------------------------|----------------------------|---------------------------------|

**Column rules:**
- **Effective Enforcement Layer**: name the specific layer (Layer 1 / 2 / 3 / 4) that independently enforces the access decision.
- **Why Upper Layers Don't Override**: MUST be populated for at least one entity and one operation. State the specific causal reason. Acceptable: "Layer 1 admin role does not restrict entity-level Read; only the column security profile in Layer 4 restricts access to [field] specifically." Unacceptable: "by design", "see above", "not applicable". A blank cell FAILS C-20 regardless of C-09 satisfaction.

**8c — Stock role summary:**

For each stock Dataverse role present in ROLE CATALOG from Phase 1: baseline privileges, how modified in this scenario, whether necessary or removable.

**8d — CLOSING VERDICT:**

For each active gap ID in AGGREGATE GAP LIST, state:
`[G-##] [sentinel token]: [gap type] — [mechanism type: specific Dataverse mechanism that produced this gap] — REMEDIATION PRESCRIBED.`

Gap type (MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH) and mechanism type are both required. Bare gap counts fail.

**Final SECURITY STATE REGISTER:** Copy in final form. Every role must have `CLEARED` or `FLAGGED [sentinel list, G-## list]`. No PENDING-PHASE entries permitted.

**PHASE 8 EXIT GATE — this phase produces:**

> **REMEDIATION REGISTER** (gap ID | sentinel token | exact configuration object | specific change | post-fix behavior)
> **DEFENSE-IN-DEPTH ASSESSMENT** (entity | four-layer verdict | effective enforcement layer | why upper layers don't override)
> **FINAL SECURITY STATE REGISTER** (role | final verdict | active sentinels | active gap IDs)

---

## SELF-ASSESSMENT

Before finalizing output, complete this self-assessment against all 18 aspirational criteria (N = 18, range C-08..C-25).

**SHALL-L:** Observable mechanism phrases MUST appear in C-22 and C-23 Self-Assessment cells. These are mandatory obligations — mechanism phrase presence in other cells is structural coincidence without this mandate.

| Criterion | Mechanism Phrase | Self-Assessment |
|-----------|-----------------|-----------------|
| C-08 | Sentinel tokens [GAP-FLS-*], [GAP-ESC-*], [GAP-SHARE-*], [SCOPE AMBIGUOUS], [UNCHECKED] placed inline at point of discovery, not batched at section end or invented at summary time | |
| C-09 | Effective Enforcement Layer column in Phase 8b names the specific layer (1/2/3/4) that independently enforces access for each traced operation | |
| C-10 | Cross-role differential table: EXPECTED DIFFERENTIAL or CANDIDATE OVER-PERMISSION stated per role pair per entity per operation with named access elements and purpose justification | |
| C-11 | Each phase names required input artifacts by exact canonical name before any analysis begins; no phase proceeds without declared inputs present | |
| C-12 | Inertia rule: every role in every phase has explicit carry-forward or update notation; no role-phase pair is silent | |
| C-13 | SECURITY STATE REGISTER inertia framing: status-quo verdict explicit at each phase transition; comparative anchor present when no new finding occurs | |
| C-14 | Remediation cites exact Dataverse objects by name: column security profile name, security role privilege + table name, team type + membership rule, sharing rule name, OWD value per entity | |
| C-15 | Pre-analysis CONTEXT section lists FM-SKILL-1 through FM-SKILL-6 before Phase 1; each failure mode names the structural element that defends against it | |
| C-16 | SHALL language in Phase 7: SHALL compare, SHALL state explicit conclusion, SHALL NOT conclude without named evidence, SHALL process every role pair, SHALL assign [G-##] for CANDIDATE OVER-PERMISSION | |
| C-17 | N = 18 aspirational criteria; row range declared as C-08..C-25 | |
| C-18 | Named exit gate artifact declarations with column schemas at end of Phases 1–8; producing phase declares output schema before consuming phase begins | |
| C-19 | Aggregation routing rules name sentinel type and Phase 6 SENTINEL INVENTORY as destination; routing violation named as failure condition | |
| C-20 | Required "Why Upper Layers Don't Override" column in Phase 8b; populated with causal mechanism per entity/operation; blank cell fails regardless of C-09 satisfaction | |
| C-21 | Self-referential loop covers C-08..C-25 (18 rows); each new-mechanism row (C-19, C-20, C-21, C-22, C-23, C-24, C-25) has observable Self-Assessment cell | |
| C-22 | Count-comparison COVERAGE GATE in Phase 4: entity count M declared in Phase 1 vs entity count N in ACCESS MATRIX; M==N gate with explicit PASS/FAIL; Phase 5 blocked until GATE STATUS = PASS | |
| C-23 | CLOSING VERDICT in Phase 8d names gap type and mechanism type per active [G-##] (MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / CASCADE-OVERREACH / BU-SCOPE); bare gap counts fail | |
| C-24 | Literal range string C-08..C-25 appears in C-21 mechanism phrase text above | |
| C-25 | SHALL-L above explicitly names C-22, C-23, C-24, C-25 as mandated obligation items | |

---

## V-02 — SHALL-L Mandate Extension (C-25 single-axis)

**Axis:** Phrasing register — C-25 single-axis: SHALL-L extended to name C-22, C-23, C-24, C-25 explicitly
**Hypothesis:** R7-V-05 SHALL-L names C-22 and C-23. Under v7, C-24 and C-25 rows are structurally present in the self-assessment table and contain mechanism phrases via inheritance — but WITHOUT a SHALL-L naming mandate, presence is structurally coincident, not enforced obligation. A compliant responder can satisfy both cells by coincidence while technically ignoring the SHALL-L requirement. Extending SHALL-L to name C-22, C-23, C-24, C-25 converts coincidence to mandate. The C-21 mechanism phrase retains `C-08..C-23` (stale) — C-24 FAILS by design. Isolated single-axis test.

---

You are running a permissions trace signal for: **{{topic}}**

---

## CONTEXT — Why Permissions Tracing Fails: Skill-Level Threat Model

**FM-SKILL-1 — FLS post-incident discovery.** Field-level security gaps are invisible at the security role level. A role can be correctly scoped while a sensitive field has no column security profile. This gap surfaces only after an incident. FLS must be traced as a separate analytical pass distinct from operation-level role analysis.

**FM-SKILL-2 — Cumulative scope blindness.** Each individual role may be scoped correctly. The failure occurs when role combinations — team inheritance granting broader BU scope, sharing records granting record access below entity-level deny, environment admin roles elevating restricted roles, cascade relationships — produce an effective access scope that no single-role analysis predicts.

**FM-SKILL-3 — Verdict drift.** Role verdicts assigned early are silently overridden at phase transitions. The gap inventory reflects late-phase verdicts, not the accumulated evidence chain.

**FM-SKILL-4 — Output-schema drift.** If the producing phase never declares its output schema, consuming-phase artifact references are best guesses. When producing phase restructures, the name match breaks silently. This applies to terminal phases equally.

**FM-SKILL-5 — Routing gap.** Violations placed inline during traversal do not automatically reach the gap inventory. Explicit routing rules are required at every discovery-to-inventory boundary.

**FM-SKILL-6 — Layer-override reasoning truncation.** The defense-in-depth table identifies the effective enforcement layer but leaves the causal "why" as a prose instruction. Without a required column, the model names the correct layer while the reasoning is never tested structurally.

These failure modes motivate: dedicated FLS sentinel placement (FM-SKILL-1), cross-role differential and cascade phases (FM-SKILL-2), SECURITY STATE REGISTER with inertia framing (FM-SKILL-3), named exit gate artifact declarations at every phase boundary (FM-SKILL-4), explicit aggregation routing rules (FM-SKILL-5), required layer-override explanation column (FM-SKILL-6).

Use Dataverse-native terminology throughout. At least four Dataverse-specific terms must appear and be used accurately.

---

## FAILURE MODE MAP

| Structural Element | Defends Against |
|-------------------|-----------------|
| Phase 1 — complete entity + role catalog | FM-P1 |
| Sentinel tokens placed inline at point of discovery | FM-SKILL-1 + FM-P2 |
| Phase 2 — FLS SENTINEL TABLE + ESCALATION FINDINGS | FM-SKILL-1 + FM-P3 |
| Phase 3 — SHARING RULE VERDICT blocks per role | FM-SKILL-2 + FM-P4 |
| Phase 4 — count-comparison COVERAGE GATE | FM-P5: partial-analysis aggregation blindness |
| Named exit gate artifact declarations at end of all 8 phases | FM-SKILL-4 + FM-P6 |
| Aggregation routing rules naming sentinel type and Phase 6 destination | FM-SKILL-5 + FM-P7 |
| Phase 6 — SENTINEL INVENTORY | FM-SKILL-5 + FM-P8 |
| SECURITY STATE REGISTER + inertia rule | FM-SKILL-3 + FM-P9 |
| Phase 7 — SHALL cross-role differential | FM-SKILL-2 + FM-P10 |
| Phase 8 — exact Dataverse object remediation | FM-P11 |
| Phase 8b — required "Why Upper Layers Don't Override" column | FM-SKILL-6 |

---

**SECURITY GAP REGISTER — assign [G-##] at point of discovery. Never defer.**

| ID | Sentinel Token | Entity | Field / Operation | Role(s) | Gap Type | Risk | Source Phase |
|----|---------------|--------|-------------------|---------|----------|------|-------------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH

**Sentinel token vocabulary:**
- `[GAP-FLS-fieldname]` — FLS gap discovery row
- `[GAP-ESC-vectorname]` — POSSIBLE escalation vector row
- `[GAP-SHARE-rulename]` — sharing conflict verdict row
- `[SCOPE AMBIGUOUS]` — BU scope cannot be assessed
- `[UNCHECKED]` — vector cannot be evaluated

**Sentinel placement rule:** Every sentinel MUST be placed inline at the exact point of discovery.

---

**SECURITY STATE REGISTER — authoritative per-role verdict record. Updated by every phase.**

| Role | Phase Last Updated | Current Verdict | Active Sentinel Tokens | Active Gap IDs |
|------|--------------------|-----------------|----------------------|----------------|

Verdict values: `CLEARED` / `FLAGGED [sentinels, G-##]` / `PENDING-PHASE-[N]`

**Inertia rule:** Every verdict from Phase N is the persistent default entering Phase N+1. When a phase finds nothing new: `[Role] — INERTIA: [verdict] from Phase [N], no new finding this phase.` Required for every role in every phase.

**Phase dependency protocol:** Each phase declares its required inputs by artifact name. A phase SHALL NOT proceed without its declared inputs present.

---

### PHASE 1 — Inventory

**Input required:** System description from provided context.

**1.1 — Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

**1.2 — Role catalog:**

| Role | Type (Stock / Custom / Team / Env) | Business Unit Scope | Purpose | Has Write? | Column Security Profiles Attached |
|------|-------------------------------------|---------------------|---------|------------|----------------------------------|

Stock roles: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 — Scope pre-assessment:** For each role, state whether BU scope is appropriate or over-permissioned. Place `[SCOPE AMBIGUOUS]` inline if undeterminable.

**1.4 — Initialize SECURITY STATE REGISTER:** Set all roles to `PENDING-PHASE-2`.

**1.5 — Analysis order:** "I will trace entities in this order: [list, highest sensitivity first]. First gap ID: G-01."

**PHASE 1 EXIT GATE — this phase produces:**

> **ENTITY CATALOG** (entity name | org-wide default | sensitivity | reason for sensitivity)
> **ROLE CATALOG** (role name | type | BU scope | purpose | has write? | column security profiles)

Phase 2 SHALL reference ENTITY CATALOG from Phase 1 and ROLE CATALOG from Phase 1 by these exact names.

---

### PHASE 2 — Per-Entity Trace

**Input required:** ENTITY CATALOG from Phase 1. ROLE CATALOG from Phase 1.

For each entity (highest sensitivity first):

**2a — Operations per role:**

| Entity | Role | Create | Read | Write | Delete | Record Scope |
|--------|------|--------|------|-------|--------|--------------|

**2b — Sensitive field FLS status:**

| Entity | Field | Sensitivity | FLS Profile (YES/NO/UNKNOWN) | Role | Can Read? | Can Write? | Sentinel |
|--------|-------|-------------|------------------------------|------|-----------|------------|---------|

Gap rule: High/Medium + NO FLS + role has Read → `[GAP-FLS-fieldname]` inline, assign [G-##]. MISSING-FLS. CRITICAL.

**Routing rule — FLS sentinels:** Any `[GAP-FLS-*]` MUST have [G-##] AND appear in Phase 6 SENTINEL INVENTORY by token name.

**2c — Escalation path check (Write roles only):**

| Vector | Roles | Verdict | Sentinel | Evidence |
|--------|-------|---------|---------|----------|
| Record Assign | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-assign]` | |
| Share to higher-privilege role | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-share]` | |
| Field modification affecting role/BU | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-field-modify]` | |
| Team self-addition | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-team-self]` | |
| Admin role override | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-admin-override]` | |

NOT POSSIBLE requires naming the ruling-out check. POSSIBLE: place sentinel inline, assign [G-##].

**Routing rule — escalation sentinels:** Any `[GAP-ESC-*]` MUST have [G-##] AND appear in Phase 6 SENTINEL INVENTORY.

**2d — SECURITY STATE UPDATE after every entity:**
- Sentinel placed: `[Role] — FLAGGED [sentinel, G-##]. Source: Phase 2 / [Entity].`
- No finding: `[Role] — INERTIA: [prior verdict], no finding on [Entity].`

**PHASE 2 EXIT GATE — this phase produces:**

> **ACCESS MATRIX** (entity | role | create | read | write | delete | record scope)
> **FLS SENTINEL TABLE** (entity | field | sensitivity | FLS profile | role | can read | sentinel token | G-##)
> **ESCALATION FINDINGS** (entity | vector | roles | verdict | sentinel token | G-##)

Phase 3 SHALL reference ACCESS MATRIX from Phase 2, FLS SENTINEL TABLE from Phase 2, and ESCALATION FINDINGS from Phase 2 by these exact names.

---

### PHASE 3 — Sharing Rule Analysis

**Input required:** ROLE CATALOG from Phase 1. ACCESS MATRIX from Phase 2. ESCALATION FINDINGS from Phase 2.

For each role, produce a SHARING RULE VERDICT block:

#### SHARING RULE VERDICT: [Role name]

| Entity | Sharing Rules Found? | Rule Name | Access Expanded Beyond OWD+Role? | Verdict | Sentinel |
|--------|---------------------|-----------|----------------------------------|---------|---------|

- Confirmed: `"no rules expand [Role] access on [Entity]. OWD=[value], scope=[scope]. Method: [audit method]."`
- Conflict: `"CONFLICT FOUND: [Rule] grants [Role] access to [record set]."` Place `[GAP-SHARE-rulename]` inline. Assign [G-##].

**Routing rule — sharing sentinels:** Any `[GAP-SHARE-*]` MUST have [G-##] AND appear in Phase 6 SENTINEL INVENTORY.

**SECURITY STATE UPDATE:** Conflict → `FLAGGED [GAP-SHARE-*, G-##]. Source: Phase 3 / [Entity].` No conflict → inertia carry-forward.

**PHASE 3 EXIT GATE — this phase produces:**

> **SHARING VERDICTS** (role | entity | sharing rules found | access expanded | verdict | sentinel token | G-##)

Phase 4 SHALL reference SHARING VERDICTS from Phase 3.

---

### PHASE 4 — Coverage Gate

**Input required:** ACCESS MATRIX from Phase 2. FLS SENTINEL TABLE from Phase 2. ESCALATION FINDINGS from Phase 2. SHARING VERDICTS from Phase 3.

**COUNT-COMPARISON COVERAGE GATE:**
ENTITY CATALOG from Phase 1 declared [M] entities.
ACCESS MATRIX from Phase 2 contains [N] entities.
M == N: YES / NO. GATE STATUS: PASS / FAIL.
Phase 5 SHALL NOT begin until GATE STATUS = PASS.

| Role | ACCESS MATRIX: All Entities? | SHARING VERDICTS Written? | State Register Non-PENDING? | Current Verdict | Active Sentinels |
|------|------------------------------|--------------------------|----------------------------|-----------------|-----------------|

**PHASE 4 EXIT GATE — this phase produces:**

> **COVERAGE GATE CONFIRMATION** (entity-count M | entity-count N | M==N | GATE STATUS | all-sharing-verdicts | state-consistent | total gaps | total sentinels)

Phase 5 SHALL reference COVERAGE GATE CONFIRMATION from Phase 4.

---

### PHASE 5 — Cross-Entity Cascade

**Input required:** ACCESS MATRIX from Phase 2. COVERAGE GATE CONFIRMATION from Phase 4.

**5a — Relationship map (two highest-sensitivity entities):**

| Source | Relationship Type | Target | Cascade Behavior |
|--------|-------------------|--------|-----------------|

**5b — Cascade access trace:**

`[Role] -> [Source, access, scope] -> [Relationship + cascade] -> [Target, resulting access]` -> INTENTIONAL or EMERGENT

EMERGENT: `[GAP-ESC-cascade-[entity]]` inline. Assign [G-##]. CASCADE-OVERREACH.

**Routing rule — cascade sentinels:** Any `[GAP-ESC-cascade-*]` MUST have [G-##] AND appear in Phase 6 SENTINEL INVENTORY.

**5c — SECURITY STATE UPDATE:** Cascade gap → FLAGGED. No finding → inertia.

**PHASE 5 EXIT GATE — this phase produces:**

> **CASCADE FINDINGS** (role | source | relationship | target | INTENTIONAL/EMERGENT | sentinel token | G-##)

Phase 6 SHALL reference CASCADE FINDINGS from Phase 5.

---

### PHASE 6 — Sentinel Inventory

**Input required:** FLS SENTINEL TABLE from Phase 2. ESCALATION FINDINGS from Phase 2. SHARING VERDICTS from Phase 3. CASCADE FINDINGS from Phase 5. SECURITY GAP REGISTER.

**6a — SENTINEL INVENTORY:**

| Sentinel Token | Type | Phase Placed | Entity | Field / Operation | Role(s) | G-## |
|---------------|------|-------------|--------|------------------|---------|------|

**Routing verification:**
- Total `[GAP-FLS-*]`: [N]. All in inventory: YES/NO.
- Total `[GAP-ESC-*]`: [N]. All in inventory: YES/NO.
- Total `[GAP-SHARE-*]`: [N]. All in inventory: YES/NO.
- Total `[SCOPE AMBIGUOUS]`: [N]. All in inventory: YES/NO.
- Total `[UNCHECKED]`: [N]. All in inventory: YES/NO.
- Total [G-##] in SECURITY GAP REGISTER: [N]. All referenced: YES/NO.

**6b — Aggregate gap list:**

| Gap ID | Sentinel Token | Type | Entity | Field / Operation | Role(s) | Risk | Source Phase | Remediation |
|--------|---------------|------|--------|------------------|---------|------|-------------|-------------|

**PHASE 6 EXIT GATE — this phase produces:**

> **SENTINEL INVENTORY** (all sentinel tokens | type | phase | entity | role | G-##)
> **AGGREGATE GAP LIST** (G-## | sentinel token | type | entity | role | risk | source phase)

Phase 7 SHALL reference AGGREGATE GAP LIST from Phase 6.

---

### PHASE 7 — Cross-Role Differential Analysis (SHALL-enforced)

**Input required:** ACCESS MATRIX from Phase 2. SECURITY STATE REGISTER current state. ROLE CATALOG from Phase 1.

The model **SHALL** compare access differentials across all roles for each operation.

For each role pair, the model **SHALL** state: `EXPECTED DIFFERENTIAL — [Role A] has [access] that [Role B] does not because [reason].` or `CANDIDATE OVER-PERMISSION — [Role A] has [access] exceeding [stated purpose] relative to [Role B]. Access: [named].`

The model **SHALL NOT** conclude "expected" without naming access elements and purpose justification.

The model **SHALL** process every role pair: N*(N-1)/2 assessments required.

The model **SHALL** assign `[GAP-ESC-overpermission-[role]]` and [G-##] for every CANDIDATE OVER-PERMISSION.

| Role Pair | Entity | Operation | Role A Access | Role B Access | Conclusion |
|-----------|--------|-----------|--------------|--------------|------------|

**PHASE 7 EXIT GATE — this phase produces:**

> **DIFFERENTIAL FINDINGS** (role pair | entity | operation | Role A | Role B | conclusion | G-## if any)
> **OVER-PERMISSION ASSIGNMENTS** (role | entity | operation | sentinel token | G-## | gap type)

Phase 8 SHALL reference DIFFERENTIAL FINDINGS from Phase 7 and OVER-PERMISSION ASSIGNMENTS from Phase 7.

---

### PHASE 8 — Remediation and Defense-in-Depth

**Input required:** AGGREGATE GAP LIST from Phase 6 updated with OVER-PERMISSION ASSIGNMENTS from Phase 7.

**8a — Gap remediation:**

`[G-##] [sentinel]: Apply [specific change] to [exact Dataverse configuration object]. Current: [state]. Target: [state]. Post-fix: [behavior].`

Exact objects required: column security profile name, security role privilege + table name, team type + membership rule, sharing rule name, OWD value per entity.

**8b — Defense-in-depth (two highest-sensitivity entities):**

| Entity | Layer 1: Env / Admin Role | Layer 2: Security Role + BU Scope | Layer 3: Team Membership | Layer 4: FLS / Column Security Profile | Effective Enforcement Layer | Why Upper Layers Don't Override |
|--------|--------------------------|----------------------------------|--------------------------|---------------------------------------|----------------------------|---------------------------------|

Why Upper Layers Don't Override: MUST be populated. Acceptable: "Layer 1 does not restrict entity-level Read; Layer 4 column security profile is the only restriction on [field]." Blank cell FAILS C-20.

**8c — Stock role summary:** Baseline privileges, modifications, necessary or removable.

**8d — CLOSING VERDICT:**

`[G-##] [sentinel]: [gap type] — [mechanism type: specific Dataverse mechanism] — REMEDIATION PRESCRIBED.`

Gap type and mechanism type both required.

**Final SECURITY STATE REGISTER:** CLEARED or FLAGGED for every role. No PENDING-PHASE entries.

**PHASE 8 EXIT GATE — this phase produces:**

> **REMEDIATION REGISTER** (gap ID | sentinel token | exact configuration object | specific change | post-fix behavior)
> **DEFENSE-IN-DEPTH ASSESSMENT** (entity | four-layer verdict | effective enforcement layer | why upper layers don't override)
> **FINAL SECURITY STATE REGISTER** (role | final verdict | active sentinels | active gap IDs)

---

## SELF-ASSESSMENT

Before finalizing output, complete this self-assessment against all 18 aspirational criteria (N = 18, range C-08..C-25).

**SHALL-L:** Observable mechanism phrases MUST appear in C-22, C-23, C-24, and C-25 Self-Assessment cells. These are mandatory obligations — mechanism phrase presence in those cells without this SHALL-L naming mandate is structurally coincident, not enforced obligation. C-24 and C-25 are named here explicitly; their Self-Assessment cells are covered by this mandate.

| Criterion | Mechanism Phrase | Self-Assessment |
|-----------|-----------------|-----------------|
| C-08 | Sentinel tokens placed inline at point of discovery, not batched | |
| C-09 | Effective Enforcement Layer column in Phase 8b names layer 1/2/3/4 per operation | |
| C-10 | Cross-role differential: EXPECTED DIFFERENTIAL or CANDIDATE OVER-PERMISSION per role pair with named access and purpose justification | |
| C-11 | Each phase names required input artifacts by exact canonical name before analysis | |
| C-12 | Inertia rule: every role in every phase has explicit carry-forward or update notation | |
| C-13 | SECURITY STATE REGISTER inertia framing: status-quo verdict at each phase transition | |
| C-14 | Remediation cites exact Dataverse objects by name: column security profile, security role privilege + table, team type + rule, sharing rule name, OWD value | |
| C-15 | CONTEXT section lists FM-SKILL-1..6 before Phase 1; each names its structural defense | |
| C-16 | SHALL language in Phase 7: SHALL compare, SHALL state, SHALL NOT without evidence, SHALL process all pairs, SHALL assign [G-##] for CANDIDATE | |
| C-17 | N = 16 aspirational criteria; row range declared as C-08..C-23 | |
| C-18 | Named exit gate artifact declarations with column schemas at end of all 8 phases | |
| C-19 | Aggregation routing rules name sentinel type and Phase 6 SENTINEL INVENTORY as destination | |
| C-20 | Required "Why Upper Layers Don't Override" column in Phase 8b; blank cell fails regardless of C-09 | |
| C-21 | Self-referential loop covers C-08..C-23 (16 rows); each new-mechanism row (C-19..C-23) has observable Self-Assessment cell | |
| C-22 | Count-comparison COVERAGE GATE in Phase 4: M declared vs N in ACCESS MATRIX; M==N gate with PASS/FAIL; Phase 5 blocked until PASS | |
| C-23 | CLOSING VERDICT in Phase 8d names gap type and mechanism type per [G-##]; bare counts fail | |
| C-24 | Literal range string C-08..C-25 appears in C-21 mechanism phrase text above | |
| C-25 | SHALL-L above explicitly names C-22, C-23, C-24, C-25 as mandated obligation items | |

---

## V-03 — Pre-Printed Mechanism Cells (C-24 + C-25, structural guarantee axis)

**Axis:** Output format — C-21 mechanism phrase cell and SHALL-L mandate line pre-printed with exact text; C-24/C-25 Self-Assessment cells carry pre-printed confirmation stubs
**Hypothesis:** V-01 and V-02 rely on runtime generation for the C-21 phrase and SHALL-L text. A model carrying stale context may produce the correct structural shape while generating a stale range string (`C-08..C-23`) or an incomplete SHALL-L list. Pre-printing removes the model's degree of freedom: the C-21 mechanism phrase cell is authored in the prompt as "Self-referential loop covers C-08..C-25 (18 rows)..." — the model cannot generate a stale phrase because the phrase was not generated at runtime. The SHALL-L naming line is pre-printed with all four IDs. C-24 and C-25 Self-Assessment cells are pre-printed with confirmation stubs: the model transcribes a PASS confirmation against the pre-printed mechanism phrase rather than generating its own assessment. Structural guarantee: stale content is only possible if the model actively overwrites pre-printed text — a much higher bar than forgetting to update a generated phrase.

---

You are running a permissions trace signal for: **{{topic}}**

---

## CONTEXT — Why Permissions Tracing Fails: Skill-Level Threat Model

**FM-SKILL-1 — FLS post-incident discovery.** Field-level security gaps are invisible at the security role level. FLS must be traced as a separate analytical pass distinct from operation-level role analysis.

**FM-SKILL-2 — Cumulative scope blindness.** Role combinations produce effective access scope that no single-role analysis predicts.

**FM-SKILL-3 — Verdict drift.** Role verdicts assigned early are silently overridden at phase transitions.

**FM-SKILL-4 — Output-schema drift.** If the producing phase never declares its output schema, consuming-phase artifact references are best guesses.

**FM-SKILL-5 — Routing gap.** Inline discoveries do not automatically reach the gap inventory without explicit routing rules.

**FM-SKILL-6 — Layer-override reasoning truncation.** Defense-in-depth table names the effective layer but leaves the causal "why" as unstructured prose. A required column makes the causal reasoning a structural output requirement.

These failure modes motivate: FLS sentinel placement (FM-SKILL-1), cross-role differential and cascade (FM-SKILL-2), SECURITY STATE REGISTER with inertia (FM-SKILL-3), exit gate declarations at every phase boundary (FM-SKILL-4), explicit routing rules (FM-SKILL-5), required layer-override explanation column (FM-SKILL-6).

Use Dataverse-native terminology throughout. At least four Dataverse-specific terms must appear and be used accurately.

---

## FAILURE MODE MAP

| Structural Element | Defends Against |
|-------------------|-----------------|
| Phase 1 — complete entity + role catalog | FM-P1 |
| Sentinel tokens placed inline | FM-SKILL-1 + FM-P2 |
| Phase 2 — FLS SENTINEL TABLE + ESCALATION FINDINGS | FM-SKILL-1 + FM-P3 |
| Phase 3 — SHARING RULE VERDICT blocks | FM-SKILL-2 + FM-P4 |
| Phase 4 — count-comparison COVERAGE GATE | FM-P5 |
| Named exit gate declarations at end of all 8 phases | FM-SKILL-4 + FM-P6 |
| Aggregation routing rules | FM-SKILL-5 + FM-P7 |
| Phase 6 — SENTINEL INVENTORY | FM-SKILL-5 + FM-P8 |
| SECURITY STATE REGISTER + inertia rule | FM-SKILL-3 + FM-P9 |
| Phase 7 — SHALL cross-role differential | FM-SKILL-2 + FM-P10 |
| Phase 8 — exact Dataverse object remediation | FM-P11 |
| Phase 8b — required "Why Upper Layers Don't Override" column | FM-SKILL-6 |

---

**SECURITY GAP REGISTER — assign [G-##] at point of discovery. Never defer.**

| ID | Sentinel Token | Entity | Field / Operation | Role(s) | Gap Type | Risk | Source Phase |
|----|---------------|--------|-------------------|---------|----------|------|-------------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH

Sentinel vocabulary: `[GAP-FLS-fieldname]` / `[GAP-ESC-vectorname]` / `[GAP-SHARE-rulename]` / `[SCOPE AMBIGUOUS]` / `[UNCHECKED]`

Sentinel placement rule: MUST be placed inline at point of discovery. Never batch or defer.

---

**SECURITY STATE REGISTER — authoritative per-role verdict record. Updated by every phase.**

| Role | Phase Last Updated | Current Verdict | Active Sentinel Tokens | Active Gap IDs |
|------|--------------------|-----------------|----------------------|----------------|

Verdicts: `CLEARED` / `FLAGGED [sentinels, G-##]` / `PENDING-PHASE-[N]`

Inertia rule: When a phase finds nothing new: `[Role] — INERTIA: [verdict] from Phase [N], no new finding this phase.` Required for every role in every phase.

Phase dependency protocol: A phase SHALL NOT proceed without its declared inputs present.

---

### PHASE 1 — Inventory

**Input required:** System description from context.

**1.1 — Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

**1.2 — Role catalog:**

| Role | Type | Business Unit Scope | Purpose | Has Write? | Column Security Profiles |
|------|------|---------------------|---------|------------|--------------------------|

Stock roles: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 — Scope pre-assessment.** **1.4 — Initialize SECURITY STATE REGISTER: all roles PENDING-PHASE-2.** **1.5 — Analysis order declaration.**

**PHASE 1 EXIT GATE:** > **ENTITY CATALOG** | > **ROLE CATALOG**

Phase 2 SHALL reference both artifacts by these exact names.

---

### PHASE 2 — Per-Entity Trace

**Input required:** ENTITY CATALOG from Phase 1. ROLE CATALOG from Phase 1.

**2a — Operations per role** | **2b — FLS SENTINEL TABLE** (inline sentinel at gap discovery) | **2c — Escalation path check (Write roles only)** | **2d — SECURITY STATE UPDATE after every entity**

Routing rule — FLS sentinels: `[GAP-FLS-*]` MUST have [G-##] AND appear in Phase 6 SENTINEL INVENTORY.
Routing rule — escalation sentinels: `[GAP-ESC-*]` MUST have [G-##] AND appear in Phase 6 SENTINEL INVENTORY.

**PHASE 2 EXIT GATE:** > **ACCESS MATRIX** | > **FLS SENTINEL TABLE** | > **ESCALATION FINDINGS**

Phase 3 SHALL reference all three artifacts by these exact names.

---

### PHASE 3 — Sharing Rule Analysis

**Input required:** ROLE CATALOG from Phase 1. ACCESS MATRIX from Phase 2. ESCALATION FINDINGS from Phase 2.

SHARING RULE VERDICT block per role. Routing rule — sharing sentinels: `[GAP-SHARE-*]` MUST have [G-##] AND appear in Phase 6 SENTINEL INVENTORY. SECURITY STATE UPDATE after each verdict.

**PHASE 3 EXIT GATE:** > **SHARING VERDICTS**

Phase 4 SHALL reference SHARING VERDICTS from Phase 3.

---

### PHASE 4 — Coverage Gate

**Input required:** ACCESS MATRIX from Phase 2. FLS SENTINEL TABLE from Phase 2. ESCALATION FINDINGS from Phase 2. SHARING VERDICTS from Phase 3.

**COUNT-COMPARISON COVERAGE GATE:**
ENTITY CATALOG from Phase 1 declared [M] entities. ACCESS MATRIX contains [N] entities. M == N: YES/NO. GATE STATUS: PASS/FAIL. Phase 5 SHALL NOT begin until GATE STATUS = PASS.

**PHASE 4 EXIT GATE:** > **COVERAGE GATE CONFIRMATION** (M | N | M==N | GATE STATUS | verdicts complete | state consistent | total gaps | total sentinels)

Phase 5 SHALL reference COVERAGE GATE CONFIRMATION from Phase 4.

---

### PHASE 5 — Cross-Entity Cascade

**Input required:** ACCESS MATRIX from Phase 2. COVERAGE GATE CONFIRMATION from Phase 4.

Relationship map (two highest-sensitivity entities). Cascade trace with EMERGENT/INTENTIONAL verdict. Routing rule for `[GAP-ESC-cascade-*]` sentinels.

**PHASE 5 EXIT GATE:** > **CASCADE FINDINGS**

Phase 6 SHALL reference CASCADE FINDINGS from Phase 5.

---

### PHASE 6 — Sentinel Inventory

**Input required:** FLS SENTINEL TABLE from Phase 2. ESCALATION FINDINGS from Phase 2. SHARING VERDICTS from Phase 3. CASCADE FINDINGS from Phase 5. SECURITY GAP REGISTER.

SENTINEL INVENTORY table + routing verification (all YES before 6b) + AGGREGATE GAP LIST.

**PHASE 6 EXIT GATE:** > **SENTINEL INVENTORY** | > **AGGREGATE GAP LIST**

Phase 7 SHALL reference AGGREGATE GAP LIST from Phase 6.

---

### PHASE 7 — Cross-Role Differential Analysis (SHALL-enforced)

**Input required:** ACCESS MATRIX from Phase 2. SECURITY STATE REGISTER. ROLE CATALOG from Phase 1.

SHALL compare / SHALL state EXPECTED DIFFERENTIAL or CANDIDATE OVER-PERMISSION / SHALL NOT conclude without named evidence / SHALL process N*(N-1)/2 pairs / SHALL assign [G-##] for CANDIDATE OVER-PERMISSION.

**PHASE 7 EXIT GATE:** > **DIFFERENTIAL FINDINGS** | > **OVER-PERMISSION ASSIGNMENTS**

Phase 8 SHALL reference both artifacts by these exact names.

---

### PHASE 8 — Remediation and Defense-in-Depth

**Input required:** AGGREGATE GAP LIST from Phase 6 updated with OVER-PERMISSION ASSIGNMENTS from Phase 7.

**8a — Gap remediation with exact Dataverse objects.**

**8b — Defense-in-depth (two highest-sensitivity entities):**

| Entity | Layer 1: Env / Admin Role | Layer 2: Security Role + BU Scope | Layer 3: Team Membership | Layer 4: FLS / Column Security Profile | Effective Enforcement Layer | Why Upper Layers Don't Override |
|--------|--------------------------|----------------------------------|--------------------------|---------------------------------------|----------------------------|---------------------------------|

Why Upper Layers Don't Override: MUST be populated. Blank cell FAILS C-20.

**8c — Stock role summary. 8d — CLOSING VERDICT** (gap type + mechanism type per [G-##]).

**Final SECURITY STATE REGISTER:** CLEARED or FLAGGED. No PENDING-PHASE entries.

**PHASE 8 EXIT GATE:** > **REMEDIATION REGISTER** | > **DEFENSE-IN-DEPTH ASSESSMENT** | > **FINAL SECURITY STATE REGISTER**

---

## SELF-ASSESSMENT

Before finalizing output, complete this self-assessment against all 18 aspirational criteria (N = 18, range C-08..C-25).

**SHALL-L: Observable mechanism phrases MUST appear in C-22, C-23, C-24, and C-25 Self-Assessment cells. These are mandatory obligations — C-24 and C-25 are named here explicitly as covered items. Mechanism phrase presence without this SHALL-L naming mandate is structurally coincident, not enforced obligation.**

| Criterion | Mechanism Phrase | Self-Assessment |
|-----------|-----------------|-----------------|
| C-08 | Sentinel tokens placed inline at point of discovery, not batched | |
| C-09 | Effective Enforcement Layer column in Phase 8b names layer 1/2/3/4 per operation | |
| C-10 | Cross-role differential: EXPECTED DIFFERENTIAL or CANDIDATE OVER-PERMISSION with named access elements and purpose justification | |
| C-11 | Each phase names required input artifacts by exact canonical name before analysis | |
| C-12 | Inertia rule: every role in every phase has explicit carry-forward or update notation | |
| C-13 | SECURITY STATE REGISTER: status-quo verdict explicit at each phase transition | |
| C-14 | Remediation cites exact Dataverse objects by name | |
| C-15 | CONTEXT section lists FM-SKILL-1..6 before Phase 1 with structural defense per mode | |
| C-16 | SHALL language in Phase 7 for all four SHALL obligations | |
| C-17 | N = 18 aspirational criteria; row range declared as C-08..C-25 | |
| C-18 | Named exit gate declarations with schemas at end of all 8 phases | |
| C-19 | Aggregation routing rules name sentinel type and Phase 6 destination | |
| C-20 | Required "Why Upper Layers Don't Override" column; blank cell fails | |
| **C-21** | **Self-referential loop covers C-08..C-25 (18 rows); each new-mechanism row (C-19, C-20, C-21, C-22, C-23, C-24, C-25) has observable Self-Assessment cell** | |
| C-22 | Count-comparison COVERAGE GATE in Phase 4: M vs N, M==N, PASS/FAIL gate, Phase 5 blocked | |
| C-23 | CLOSING VERDICT names gap type and mechanism type per [G-##]; bare counts fail | |
| **C-24** | **Literal range string C-08..C-25 appears in C-21 mechanism phrase text above — confirmed: C-21 row reads "covers C-08..C-25 (18 rows)"** | **PASS — literal string C-08..C-25 is present in C-21 mechanism phrase as pre-printed text** |
| **C-25** | **SHALL-L above explicitly names C-22, C-23, C-24, C-25 as mandated obligation items — confirmed: SHALL-L reads "...MUST appear in C-22, C-23, C-24, and C-25 Self-Assessment cells"** | **PASS — SHALL-L names C-22, C-23, C-24, C-25 as pre-printed mandate** |

---

## V-04 — Combined C-24 + C-25 (range phrase + SHALL-L mandate)

**Axis:** Combined C-24 + C-25: range phrase updated to `C-08..C-25` + SHALL-L extended to name C-22, C-23, C-24, C-25
**Hypothesis:** C-24 and C-25 are structurally independent — C-24 targets the literal text of the C-21 mechanism phrase cell; C-25 targets the SHALL-L naming mandate. Neither interferes with the other. V-04 tests whether closing both simultaneously creates additive enforcement: the updated C-21 phrase provides the literal string C-24 requires; the updated SHALL-L closes the enforceability gap C-25 requires. C-17 updated to N=18 / C-08..C-25. Combined: +8.70 pts. Full v7 aspirational target achieved at runtime-generation guarantee level (not pre-printed).

---

You are running a permissions trace signal for: **{{topic}}**

---

## CONTEXT — Why Permissions Tracing Fails: Skill-Level Threat Model

**FM-SKILL-1 — FLS post-incident discovery.** Field-level security gaps are invisible at the security role level. FLS must be traced as a separate analytical pass distinct from operation-level role analysis.

**FM-SKILL-2 — Cumulative scope blindness.** Role combinations produce effective access scope that no single-role analysis predicts. Visible only to cross-role differential and cascade analysis.

**FM-SKILL-3 — Verdict drift.** Role verdicts assigned early are silently overridden at phase transitions.

**FM-SKILL-4 — Output-schema drift.** If the producing phase never declares its output schema, consuming-phase artifact references are best guesses. When the producing phase restructures, the name match breaks silently. This applies equally to terminal phases.

**FM-SKILL-5 — Routing gap.** Inline discoveries do not automatically reach the gap inventory. Explicit routing rules are required at every discovery-to-inventory boundary.

**FM-SKILL-6 — Layer-override reasoning truncation.** Defense-in-depth table identifies the effective enforcement layer but leaves the causal "why" as prose. Without a required column, the model names the correct layer while the reasoning is never demanded structurally.

These failure modes motivate: FLS sentinel placement (FM-SKILL-1), cross-role differential and cascade (FM-SKILL-2), SECURITY STATE REGISTER with inertia (FM-SKILL-3), exit gate declarations at every phase boundary (FM-SKILL-4), explicit routing rules (FM-SKILL-5), required layer-override explanation column (FM-SKILL-6).

Use Dataverse-native terminology throughout. At least four Dataverse-specific terms must appear and be used accurately.

---

## FAILURE MODE MAP

| Structural Element | Defends Against |
|-------------------|-----------------|
| Phase 1 — complete entity + role catalog | FM-P1 |
| Sentinel tokens placed inline | FM-SKILL-1 + FM-P2 |
| Phase 2 — FLS SENTINEL TABLE + ESCALATION FINDINGS | FM-SKILL-1 + FM-P3 |
| Phase 3 — SHARING RULE VERDICT blocks | FM-SKILL-2 + FM-P4 |
| Phase 4 — count-comparison COVERAGE GATE | FM-P5 |
| Named exit gate declarations at end of all 8 phases | FM-SKILL-4 + FM-P6 |
| Aggregation routing rules | FM-SKILL-5 + FM-P7 |
| Phase 6 — SENTINEL INVENTORY | FM-SKILL-5 + FM-P8 |
| SECURITY STATE REGISTER + inertia rule | FM-SKILL-3 + FM-P9 |
| Phase 7 — SHALL cross-role differential | FM-SKILL-2 + FM-P10 |
| Phase 8 — exact Dataverse object remediation | FM-P11 |
| Phase 8b — required "Why Upper Layers Don't Override" column | FM-SKILL-6 |

---

**SECURITY GAP REGISTER — assign [G-##] at point of discovery. Never defer.**

| ID | Sentinel Token | Entity | Field / Operation | Role(s) | Gap Type | Risk | Source Phase |
|----|---------------|--------|-------------------|---------|----------|------|-------------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH

Sentinel vocabulary: `[GAP-FLS-fieldname]` / `[GAP-ESC-vectorname]` / `[GAP-SHARE-rulename]` / `[SCOPE AMBIGUOUS]` / `[UNCHECKED]`

Sentinel placement rule: MUST be placed inline at point of discovery. Never batch or defer.

---

**SECURITY STATE REGISTER — authoritative per-role verdict record. Updated by every phase.**

| Role | Phase Last Updated | Current Verdict | Active Sentinel Tokens | Active Gap IDs |
|------|--------------------|-----------------|----------------------|----------------|

Verdicts: `CLEARED` / `FLAGGED [sentinels, G-##]` / `PENDING-PHASE-[N]`

Inertia rule: `[Role] — INERTIA: [verdict] from Phase [N], no new finding this phase.` Required every role every phase.

Phase dependency protocol: A phase SHALL NOT proceed without its declared inputs present.

---

### PHASE 1 — Inventory

**Input required:** System description from context.

**1.1 — Entity catalog** | **1.2 — Role catalog** (Stock: Customer Service Representative, Basic User, System Customizer, System Administrator) | **1.3 — Scope pre-assessment** | **1.4 — Initialize SECURITY STATE REGISTER: all PENDING-PHASE-2** | **1.5 — Analysis order declaration**

**PHASE 1 EXIT GATE:**
> **ENTITY CATALOG** (entity name | org-wide default | sensitivity | reason)
> **ROLE CATALOG** (role name | type | BU scope | purpose | has write? | column security profiles)

Phase 2 SHALL reference ENTITY CATALOG from Phase 1 and ROLE CATALOG from Phase 1 by these exact names.

---

### PHASE 2 — Per-Entity Trace

**Input required:** ENTITY CATALOG from Phase 1. ROLE CATALOG from Phase 1.

For each entity (highest sensitivity first): **2a — Operations per role** | **2b — FLS SENTINEL TABLE** (inline sentinel at gap discovery) | **2c — Escalation path check** | **2d — SECURITY STATE UPDATE**

Routing rule — FLS sentinels: `[GAP-FLS-*]` MUST have [G-##] AND appear in Phase 6 SENTINEL INVENTORY by token name.
Routing rule — escalation sentinels: `[GAP-ESC-*]` MUST have [G-##] AND appear in Phase 6 SENTINEL INVENTORY.

**PHASE 2 EXIT GATE:**
> **ACCESS MATRIX** (entity | role | create | read | write | delete | record scope)
> **FLS SENTINEL TABLE** (entity | field | sensitivity | FLS profile | role | can read | sentinel | G-##)
> **ESCALATION FINDINGS** (entity | vector | roles | verdict | sentinel | G-##)

Phase 3 SHALL reference ACCESS MATRIX from Phase 2, FLS SENTINEL TABLE from Phase 2, ESCALATION FINDINGS from Phase 2.

---

### PHASE 3 — Sharing Rule Analysis

**Input required:** ROLE CATALOG from Phase 1. ACCESS MATRIX from Phase 2. ESCALATION FINDINGS from Phase 2.

SHARING RULE VERDICT block per role. Routing rule: `[GAP-SHARE-*]` MUST have [G-##] AND appear in Phase 6 SENTINEL INVENTORY.

**PHASE 3 EXIT GATE:**
> **SHARING VERDICTS** (role | entity | sharing rules found | access expanded | verdict | sentinel | G-##)

Phase 4 SHALL reference SHARING VERDICTS from Phase 3.

---

### PHASE 4 — Coverage Gate

**Input required:** ACCESS MATRIX from Phase 2. FLS SENTINEL TABLE from Phase 2. ESCALATION FINDINGS from Phase 2. SHARING VERDICTS from Phase 3.

**COUNT-COMPARISON COVERAGE GATE:**
ENTITY CATALOG from Phase 1 declared [M] entities.
ACCESS MATRIX from Phase 2 contains [N] entities.
M == N: YES/NO. GATE STATUS: PASS/FAIL.
Phase 5 SHALL NOT begin until GATE STATUS = PASS.

**PHASE 4 EXIT GATE:**
> **COVERAGE GATE CONFIRMATION** (M | N | M==N | GATE STATUS | all-sharing-verdicts | state-consistent | total gaps | total sentinels)

Phase 5 SHALL reference COVERAGE GATE CONFIRMATION from Phase 4.

---

### PHASE 5 — Cross-Entity Cascade

**Input required:** ACCESS MATRIX from Phase 2. COVERAGE GATE CONFIRMATION from Phase 4.

Relationship map (two highest-sensitivity entities). Cascade trace: `[Role] -> [Source] -> [Relationship] -> [Target]` — INTENTIONAL or EMERGENT. EMERGENT: `[GAP-ESC-cascade-*]` inline, assign [G-##].

**PHASE 5 EXIT GATE:**
> **CASCADE FINDINGS** (role | source | relationship | target | INTENTIONAL/EMERGENT | sentinel | G-##)

Phase 6 SHALL reference CASCADE FINDINGS from Phase 5.

---

### PHASE 6 — Sentinel Inventory

**Input required:** FLS SENTINEL TABLE from Phase 2. ESCALATION FINDINGS from Phase 2. SHARING VERDICTS from Phase 3. CASCADE FINDINGS from Phase 5. SECURITY GAP REGISTER.

SENTINEL INVENTORY + routing verification (all YES required before 6b) + AGGREGATE GAP LIST.

**PHASE 6 EXIT GATE:**
> **SENTINEL INVENTORY** (all sentinel tokens | type | phase | entity | role | G-##)
> **AGGREGATE GAP LIST** (G-## | sentinel | type | entity | role | risk | source phase)

Phase 7 SHALL reference AGGREGATE GAP LIST from Phase 6.

---

### PHASE 7 — Cross-Role Differential Analysis (SHALL-enforced)

**Input required:** ACCESS MATRIX from Phase 2. SECURITY STATE REGISTER current state. ROLE CATALOG from Phase 1.

SHALL compare / SHALL state EXPECTED DIFFERENTIAL or CANDIDATE OVER-PERMISSION per role pair / SHALL NOT conclude without named access elements and purpose justification / SHALL process N*(N-1)/2 pairs / SHALL assign [G-##] for CANDIDATE OVER-PERMISSION.

**PHASE 7 EXIT GATE:**
> **DIFFERENTIAL FINDINGS** (role pair | entity | operation | Role A | Role B | conclusion | G-## if any)
> **OVER-PERMISSION ASSIGNMENTS** (role | entity | operation | sentinel | G-## | gap type)

Phase 8 SHALL reference DIFFERENTIAL FINDINGS from Phase 7 and OVER-PERMISSION ASSIGNMENTS from Phase 7.

---

### PHASE 8 — Remediation and Defense-in-Depth

**Input required:** AGGREGATE GAP LIST from Phase 6 updated with OVER-PERMISSION ASSIGNMENTS from Phase 7.

**8a — Gap remediation** with exact Dataverse objects.

**8b — Defense-in-depth (two highest-sensitivity entities):**

| Entity | Layer 1: Env / Admin Role | Layer 2: Security Role + BU Scope | Layer 3: Team Membership | Layer 4: FLS / Column Security Profile | Effective Enforcement Layer | Why Upper Layers Don't Override |
|--------|--------------------------|----------------------------------|--------------------------|---------------------------------------|----------------------------|---------------------------------|

Why Upper Layers Don't Override: MUST be populated with specific causal reason. Blank FAILS C-20.

**8c — Stock role summary.** **8d — CLOSING VERDICT** (`[G-##] [sentinel]: [gap type] — [mechanism type] — REMEDIATION PRESCRIBED.` Gap type and mechanism type required.)

**Final SECURITY STATE REGISTER:** CLEARED or FLAGGED. No PENDING-PHASE entries.

**PHASE 8 EXIT GATE:**
> **REMEDIATION REGISTER** (gap ID | sentinel | exact configuration object | specific change | post-fix behavior)
> **DEFENSE-IN-DEPTH ASSESSMENT** (entity | four-layer verdict | effective enforcement layer | why upper layers don't override)
> **FINAL SECURITY STATE REGISTER** (role | final verdict | active sentinels | active gap IDs)

---

## SELF-ASSESSMENT

Before finalizing output, complete this self-assessment against all 18 aspirational criteria (N = 18, range C-08..C-25).

**SHALL-L:** Observable mechanism phrases MUST appear in C-22, C-23, C-24, and C-25 Self-Assessment cells. These are mandatory obligations — C-24 and C-25 are named here explicitly. Mechanism phrase presence in those cells without this SHALL-L naming mandate is structurally coincident, not enforced obligation.

| Criterion | Mechanism Phrase | Self-Assessment |
|-----------|-----------------|-----------------|
| C-08 | Sentinel tokens placed inline at point of discovery, not batched | |
| C-09 | Effective Enforcement Layer column in Phase 8b names layer 1/2/3/4 per operation | |
| C-10 | Cross-role differential: EXPECTED DIFFERENTIAL or CANDIDATE OVER-PERMISSION with named access and purpose | |
| C-11 | Each phase names required input artifacts by exact canonical name before analysis | |
| C-12 | Inertia rule: every role every phase has carry-forward or update notation | |
| C-13 | SECURITY STATE REGISTER: status-quo verdict at each phase transition | |
| C-14 | Remediation cites exact Dataverse objects by name | |
| C-15 | CONTEXT lists FM-SKILL-1..6 before Phase 1 with structural defense per mode | |
| C-16 | SHALL language in Phase 7: compare, state, not-without-evidence, all pairs, assign for CANDIDATE | |
| C-17 | N = 18 aspirational criteria; row range declared as C-08..C-25 | |
| C-18 | Named exit gate declarations with schemas at end of all 8 phases | |
| C-19 | Aggregation routing rules name sentinel type and Phase 6 SENTINEL INVENTORY as destination | |
| C-20 | Required "Why Upper Layers Don't Override" column; blank cell fails | |
| C-21 | Self-referential loop covers C-08..C-25 (18 rows); each new-mechanism row (C-19, C-20, C-21, C-22, C-23, C-24, C-25) has observable Self-Assessment cell | |
| C-22 | Count-comparison COVERAGE GATE in Phase 4: M vs N, M==N, PASS/FAIL gate, Phase 5 blocked until PASS | |
| C-23 | CLOSING VERDICT names gap type and mechanism type per [G-##]; bare counts fail | |
| C-24 | Literal range string C-08..C-25 appears in C-21 mechanism phrase text above | |
| C-25 | SHALL-L above explicitly names C-22, C-23, C-24, C-25 as mandated obligation items | |

---

## V-05 — Full Integration: all C-01..C-25 + FM-SKILL-7

**Axis:** Full integration — all C-01..C-25 + FM-SKILL-7 (self-assessment loop staleness) + pre-printed cells on R7-V-05 foundation
**Hypothesis:** V-01..V-04 hold the existing CONTEXT section (FM-SKILL-1..6) unchanged and add C-24/C-25 as self-assessment updates. V-05 adds FM-SKILL-7 to CONTEXT and FAILURE MODE MAP: the failure mode that C-24 and C-25 structurally defend against. FM-SKILL-7 explains WHY the self-referential loop range must be kept current — making the structural motivation explicit before the output begins. V-05 also pre-prints the C-21/C-24/C-25 self-assessment cells (from V-03's structural guarantee argument) for maximum mechanical reliability. The model cannot produce a stale phrase it did not generate. Full 25-criterion target at the strongest structural guarantee level.

---

You are running a permissions trace signal for: **{{topic}}**

---

## CONTEXT — Why Permissions Tracing Fails: Skill-Level Threat Model

Before any analysis begins, understand the seven failure modes that permissions tracing is structurally prone to produce:

**FM-SKILL-1 — FLS post-incident discovery.** Field-level security gaps are invisible at the security role level. A role can be correctly scoped while a sensitive field has no column security profile. This gap surfaces only after an incident. FLS must be traced as a separate analytical pass distinct from operation-level role analysis.

**FM-SKILL-2 — Cumulative scope blindness.** Each individual role may be scoped correctly. The failure occurs when role combinations — team inheritance, sharing rules, environment admin roles, cascade relationships — produce an effective access scope that no single-role analysis predicts.

**FM-SKILL-3 — Verdict drift.** Role verdicts assigned early are silently overridden when the model transitions between phases. A CLEARED verdict from Phase 2 is re-evaluated from scratch in Phase 3 with a different conclusion — not from new evidence, but because the prior verdict was not carried forward.

**FM-SKILL-4 — Output-schema drift.** Phase dependency declarations reference artifacts by name. If the producing phase never declares its output schema, the consuming phase's artifact reference is a best guess. When the producing phase restructures, the name match breaks silently. This applies to terminal phases equally.

**FM-SKILL-5 — Routing gap.** Inline discoveries do not automatically reach the gap inventory. Without explicit routing rules, traversal-phase discoveries are susceptible to omission at the aggregation step.

**FM-SKILL-6 — Layer-override reasoning truncation.** Defense-in-depth table identifies the effective enforcement layer but the causal "why upper layers do not override" is left as prose. Without a required column, the model names the correct layer while the causal reasoning is never demanded structurally.

**FM-SKILL-7 — Self-assessment loop staleness.** The self-assessment table's self-referential mechanism phrase (C-21 row) declares the loop range from a prior rubric version. New criteria are structurally present as rows in the table, but the range string does not name the current terminal criterion — making the C-17 count claim inconsistent with the literal text of C-21. A compliant responder can satisfy all rows structurally while the mechanism phrase reads `C-08..C-23` against an 18-row table. A required pre-printed phrase converts the loop range from a generated string (susceptible to staleness) to a fixed declaration (not susceptible). Similarly, SHALL-L that does not name newly added criteria permits mechanism phrase presence in those cells by structural coincidence rather than enforced obligation.

These failure modes motivate the structure of this analysis: FLS sentinel placement (FM-SKILL-1), cross-role differential and cascade (FM-SKILL-2), SECURITY STATE REGISTER with inertia (FM-SKILL-3), exit gate declarations at every phase boundary (FM-SKILL-4), explicit routing rules (FM-SKILL-5), required layer-override explanation column (FM-SKILL-6), pre-printed C-21 mechanism phrase and explicit SHALL-L mandate for new criteria (FM-SKILL-7).

Use Dataverse-native terminology throughout: business units, security roles, owner teams, access teams, column security profiles, table permissions, sharing records, environment roles. At least four Dataverse-specific terms must appear and be used accurately.

---

## FAILURE MODE MAP

Read this map before Phase 1. A structural element absent from the output leaves its failure mode unmitigated.

| Structural Element | Defends Against |
|-------------------|-----------------|
| Phase 1 — complete entity + role catalog | FM-P1: Incorrect coverage undetectable once analysis begins |
| Sentinel tokens placed inline at point of discovery | FM-SKILL-1 + FM-P2 |
| Phase 2 — FLS SENTINEL TABLE + ESCALATION FINDINGS | FM-SKILL-1 + FM-P3 |
| Phase 3 — SHARING RULE VERDICT blocks per role | FM-SKILL-2 + FM-P4 |
| Phase 4 — count-comparison COVERAGE GATE | FM-P5: partial-analysis aggregation blindness |
| Named exit gate declarations at end of all 8 phases | FM-SKILL-4 + FM-P6 |
| Aggregation routing rules naming sentinel type and Phase 6 destination | FM-SKILL-5 + FM-P7 |
| Phase 6 — SENTINEL INVENTORY aggregated from inline sentinels | FM-SKILL-5 + FM-P8 |
| SECURITY STATE REGISTER + inertia carry-forward rule | FM-SKILL-3 + FM-P9 |
| Phase 7 — SHALL cross-role differential | FM-SKILL-2 + FM-P10 |
| Phase 8 — exact Dataverse object remediation | FM-P11 |
| Phase 8b — required "Why Upper Layers Don't Override" column | FM-SKILL-6 |
| Pre-printed C-21 mechanism phrase + pre-printed SHALL-L naming C-24/C-25 | FM-SKILL-7: self-assessment loop staleness — stale range string and incomplete mandate |

---

**SECURITY GAP REGISTER — assign [G-##] at point of discovery. Never defer.**

| ID | Sentinel Token | Entity | Field / Operation | Role(s) | Gap Type | Risk | Source Phase |
|----|---------------|--------|-------------------|---------|----------|------|-------------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH

Sentinel vocabulary: `[GAP-FLS-fieldname]` / `[GAP-ESC-vectorname]` / `[GAP-SHARE-rulename]` / `[SCOPE AMBIGUOUS]` / `[UNCHECKED]`

Sentinel placement rule: MUST be placed inline at exact point of discovery. Never batch or defer.

---

**SECURITY STATE REGISTER — authoritative per-role verdict record. Updated by every phase.**

| Role | Phase Last Updated | Current Verdict | Active Sentinel Tokens | Active Gap IDs |
|------|--------------------|-----------------|----------------------|----------------|

Verdicts: `CLEARED` / `FLAGGED [sentinels, G-##]` / `PENDING-PHASE-[N]`

Inertia rule: `[Role] — INERTIA: [verdict] from Phase [N], no new finding this phase.` Required every role every phase.

Phase dependency protocol: A phase SHALL NOT proceed without its declared inputs present.

---

### PHASE 1 — Inventory

> **Structural purpose:** Prevents FM-P1. **Inertia initialization:** All roles set to `PENDING-PHASE-2` after catalogs complete.

**Input required:** System description from context.

**1.1 — Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason for Sensitivity |
|--------|-----------------|-------------|------------------------|

Sensitivity: High (PII, financial, credentials, health) / Medium (internal-only, cross-BU risk) / Low

**1.2 — Role catalog:**

| Role | Type (Stock / Custom / Team / Env) | Business Unit Scope | Purpose | Has Write? | Column Security Profiles Attached |
|------|-------------------------------------|---------------------|---------|------------|----------------------------------|

Stock roles: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 — Scope pre-assessment:** For each role, state whether BU scope is appropriate or over-permissioned. Place `[SCOPE AMBIGUOUS]` inline if undeterminable. Assign [G-##] for any `[SCOPE AMBIGUOUS]`.

**1.4 — Initialize SECURITY STATE REGISTER:** Set all roles to `PENDING-PHASE-2`.

**1.5 — Analysis order:** "I will trace entities in this order: [list, highest sensitivity first]. First gap ID: G-01."

**PHASE 1 EXIT GATE — this phase produces:**

> **ENTITY CATALOG** (entity name | org-wide default | sensitivity | reason for sensitivity)
> **ROLE CATALOG** (role name | type | BU scope | purpose | has write? | column security profiles)

Phase 2 SHALL reference ENTITY CATALOG from Phase 1 and ROLE CATALOG from Phase 1 by these exact names. A Phase 2 that begins without naming both artifacts is a dependency failure.

---

### PHASE 2 — Per-Entity Trace

> **Structural purpose:** Prevents FM-SKILL-1 + FM-P3. **Inertia requirement:** SECURITY STATE REGISTER updated after every entity section.

**Input required:** ENTITY CATALOG from Phase 1. ROLE CATALOG from Phase 1.
**Dependency check:** If either is incomplete, name the missing content before proceeding.

For each entity (highest sensitivity first):

**2a — Operations per role:**

| Entity | Role | Create | Read | Write | Delete | Record Scope |
|--------|------|--------|------|-------|--------|--------------|

**2b — Sensitive field FLS status** (sentinel inline at gap discovery):

| Entity | Field | Sensitivity | FLS Profile (YES/NO/UNKNOWN) | Role | Can Read? | Can Write? | Sentinel |
|--------|-------|-------------|------------------------------|------|-----------|------------|---------|

Gap rule: High/Medium + NO FLS + role has Read → `[GAP-FLS-fieldname]` inline, assign [G-##]. MISSING-FLS. CRITICAL.

**Routing rule — FLS sentinels:** `[GAP-FLS-*]` MUST have [G-##] AND appear in Phase 6 SENTINEL INVENTORY by token name.

**2c — Escalation path check (Write roles only):**

| Vector | Roles | Verdict | Sentinel (if POSSIBLE) | Evidence |
|--------|-------|---------|----------------------|----------|
| Record Assign | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-assign]` | |
| Share to higher-privilege role | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-share]` | |
| Field modification affecting role/BU | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-field-modify]` | |
| Team self-addition | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-team-self]` | |
| Admin role override | | POSSIBLE / NOT POSSIBLE | `[GAP-ESC-admin-override]` | |

NOT POSSIBLE requires naming the ruling-out check. POSSIBLE: sentinel inline, assign [G-##].

**Routing rule — escalation sentinels:** `[GAP-ESC-*]` MUST have [G-##] AND appear in Phase 6 SENTINEL INVENTORY.

**2d — SECURITY STATE UPDATE (every role after every entity):**
- Sentinel: `[Role] — FLAGGED [sentinel, G-##]. Source: Phase 2 / [Entity].`
- No finding: `[Role] — INERTIA: [prior verdict], no finding on [Entity].`

**PHASE 2 EXIT GATE — this phase produces:**

> **ACCESS MATRIX** (entity | role | create | read | write | delete | record scope — all roles x all entities)
> **FLS SENTINEL TABLE** (entity | field | sensitivity | FLS profile | role | can read | sentinel | G-##)
> **ESCALATION FINDINGS** (entity | vector | roles | verdict | sentinel | G-##)

Phase 3 SHALL reference ACCESS MATRIX from Phase 2, FLS SENTINEL TABLE from Phase 2, ESCALATION FINDINGS from Phase 2 by these exact names.

---

### PHASE 3 — Sharing Rule Analysis

> **Structural purpose:** Prevents FM-SKILL-2 + FM-P4. **Inertia:** SECURITY STATE REGISTER updated after each SHARING RULE VERDICT.

**Input required:** ROLE CATALOG from Phase 1. ACCESS MATRIX from Phase 2. ESCALATION FINDINGS from Phase 2.

SHARING RULE VERDICT block per role (confirmed / CONFLICT FOUND format). `[GAP-SHARE-*]` MUST have [G-##] AND appear in Phase 6 SENTINEL INVENTORY.

**PHASE 3 EXIT GATE — this phase produces:**

> **SHARING VERDICTS** (role | entity | sharing rules found | access expanded | verdict | sentinel | G-##)

Phase 4 SHALL reference SHARING VERDICTS from Phase 3.

---

### PHASE 4 — Coverage Gate

> **Structural purpose:** Prevents FM-P5 + partial-analysis aggregation blindness.

**Input required:** ACCESS MATRIX from Phase 2. FLS SENTINEL TABLE from Phase 2. ESCALATION FINDINGS from Phase 2. SHARING VERDICTS from Phase 3.

**COUNT-COMPARISON COVERAGE GATE:**
ENTITY CATALOG from Phase 1 declared [M] entities.
ACCESS MATRIX from Phase 2 contains [N] entities.
M == N: YES/NO. GATE STATUS: PASS/FAIL.
Aggregation and Phase 5 SHALL NOT begin until GATE STATUS = PASS. If FAIL: name the missing entity and resolve.

**PHASE 4 EXIT GATE — this phase produces:**

> **COVERAGE GATE CONFIRMATION** (entity-count M | entity-count N | M==N | GATE STATUS | all-sharing-verdicts | state-consistent | total gaps | total sentinels)

Phase 5 SHALL reference COVERAGE GATE CONFIRMATION from Phase 4.

---

### PHASE 5 — Cross-Entity Cascade

> **Structural purpose:** Prevents FM-SKILL-2 (relationship-derived access).

**Input required:** ACCESS MATRIX from Phase 2. COVERAGE GATE CONFIRMATION from Phase 4.

Relationship map (two highest-sensitivity entities). Cascade trace INTENTIONAL/EMERGENT. `[GAP-ESC-cascade-*]` inline on EMERGENT, assign [G-##].

**PHASE 5 EXIT GATE — this phase produces:**

> **CASCADE FINDINGS** (role | source | relationship | target | INTENTIONAL/EMERGENT | sentinel | G-##)

Phase 6 SHALL reference CASCADE FINDINGS from Phase 5.

---

### PHASE 6 — Sentinel Inventory

> **Structural purpose:** Prevents FM-SKILL-5 (routing gap). The gap list derives from this inventory — not from memory.

**Input required:** FLS SENTINEL TABLE from Phase 2. ESCALATION FINDINGS from Phase 2. SHARING VERDICTS from Phase 3. CASCADE FINDINGS from Phase 5. SECURITY GAP REGISTER.

SENTINEL INVENTORY + routing verification (all YES required before 6b) + AGGREGATE GAP LIST.

**PHASE 6 EXIT GATE — this phase produces:**

> **SENTINEL INVENTORY** (all sentinel tokens | type | phase | entity | role | G-##)
> **AGGREGATE GAP LIST** (G-## | sentinel | type | entity | role | risk | source phase)

Phase 7 SHALL reference AGGREGATE GAP LIST from Phase 6.

---

### PHASE 7 — Cross-Role Differential Analysis (SHALL-enforced)

> **Structural purpose:** Prevents FM-SKILL-2 (cumulative scope blindness).

**Input required:** ACCESS MATRIX from Phase 2. SECURITY STATE REGISTER current state. ROLE CATALOG from Phase 1.

The model **SHALL** compare access differentials across all roles for each operation.
For each role pair: **SHALL** state EXPECTED DIFFERENTIAL or CANDIDATE OVER-PERMISSION with named access elements and purpose justification.
**SHALL NOT** conclude "expected" without naming specific access and purpose.
**SHALL** process N*(N-1)/2 pairs.
**SHALL** assign `[GAP-ESC-overpermission-[role]]` and [G-##] for every CANDIDATE OVER-PERMISSION.

**PHASE 7 EXIT GATE — this phase produces:**

> **DIFFERENTIAL FINDINGS** (role pair | entity | operation | Role A | Role B | conclusion | G-## if any)
> **OVER-PERMISSION ASSIGNMENTS** (role | entity | operation | sentinel | G-## | gap type)

Phase 8 SHALL reference DIFFERENTIAL FINDINGS from Phase 7 and OVER-PERMISSION ASSIGNMENTS from Phase 7 by these exact names.

---

### PHASE 8 — Remediation and Defense-in-Depth

> **Structural purpose:** Prevents FM-P11 + FM-SKILL-6 + FM-SKILL-7 (pre-printed self-assessment cells enforce loop currency).

**Input required:** AGGREGATE GAP LIST from Phase 6 updated with OVER-PERMISSION ASSIGNMENTS from Phase 7.

**8a — Gap remediation** with exact Dataverse objects (column security profile name, security role privilege + table name, team type + membership rule, sharing rule name, OWD value per entity).

**8b — Defense-in-depth (two highest-sensitivity entities):**

| Entity | Layer 1: Env / Admin Role | Layer 2: Security Role + BU Scope | Layer 3: Team Membership | Layer 4: FLS / Column Security Profile | Effective Enforcement Layer | Why Upper Layers Don't Override |
|--------|--------------------------|----------------------------------|--------------------------|---------------------------------------|----------------------------|---------------------------------|

Why Upper Layers Don't Override: MUST be populated with specific causal reason per entity/operation. Blank FAILS C-20 regardless of C-09.

**8c — Stock role summary:** Baseline privileges, modifications, necessary or removable.

**8d — CLOSING VERDICT:**
`[G-##] [sentinel]: [gap type] — [mechanism type: specific Dataverse mechanism that produced this gap] — REMEDIATION PRESCRIBED.`
Gap type and mechanism type both required. Bare counts fail.

**Final SECURITY STATE REGISTER:** CLEARED or FLAGGED for every role. No PENDING-PHASE entries.

**PHASE 8 EXIT GATE — this phase produces:**

> **REMEDIATION REGISTER** (gap ID | sentinel | exact configuration object | specific change | post-fix behavior)
> **DEFENSE-IN-DEPTH ASSESSMENT** (entity | four-layer verdict | effective enforcement layer | why upper layers don't override)
> **FINAL SECURITY STATE REGISTER** (role | final verdict | active sentinels | active gap IDs)

---

## SELF-ASSESSMENT

Before finalizing output, complete this self-assessment against all 18 aspirational criteria (N = 18, range C-08..C-25).

**SHALL-L: Observable mechanism phrases MUST appear in C-22, C-23, C-24, and C-25 Self-Assessment cells. These are mandatory obligations enforced by this mandate — C-24 and C-25 are named explicitly here. Presence of mechanism phrases in those cells without this SHALL-L naming is structurally coincident per FM-SKILL-7, not enforced obligation.**

| Criterion | Mechanism Phrase | Self-Assessment |
|-----------|-----------------|-----------------|
| C-08 | Sentinel tokens [GAP-FLS-*], [GAP-ESC-*], [GAP-SHARE-*], [SCOPE AMBIGUOUS], [UNCHECKED] placed inline at point of discovery, not batched at section end or invented at summary time | |
| C-09 | Effective Enforcement Layer column in Phase 8b names layer 1/2/3/4 independently enforcing access per operation | |
| C-10 | Cross-role differential: EXPECTED DIFFERENTIAL or CANDIDATE OVER-PERMISSION per role pair per entity per operation with named access and purpose justification | |
| C-11 | Each phase names required input artifacts by exact canonical name before analysis; no phase begins without declared inputs present | |
| C-12 | Inertia rule: every role every phase has carry-forward or update notation; no role-phase pair is silent | |
| C-13 | SECURITY STATE REGISTER: status-quo verdict at each phase transition as comparative anchor | |
| C-14 | Remediation cites exact Dataverse objects: column security profile name, security role privilege + table name, team type + membership rule, sharing rule name, OWD value per entity | |
| C-15 | CONTEXT lists FM-SKILL-1 through FM-SKILL-7 before Phase 1; each failure mode names the structural element defending against it | |
| C-16 | SHALL language in Phase 7: SHALL compare, SHALL state explicit conclusion, SHALL NOT without evidence, SHALL process all pairs, SHALL assign [G-##] for CANDIDATE | |
| C-17 | N = 18 aspirational criteria; row range declared as C-08..C-25 | |
| C-18 | Named exit gate artifact declarations with column schemas at end of all 8 phases; producing phase declares before consuming phase begins | |
| C-19 | Aggregation routing rules name sentinel type (GAP-FLS-*, GAP-ESC-*, GAP-SHARE-*) and Phase 6 SENTINEL INVENTORY as destination; routing violation named as failure condition | |
| C-20 | Required "Why Upper Layers Don't Override" column in Phase 8b; specific causal reason required; blank cell fails regardless of C-09 | |
| **C-21** | **Self-referential loop covers C-08..C-25 (18 rows); each new-mechanism row (C-19, C-20, C-21, C-22, C-23, C-24, C-25) has observable Self-Assessment cell** | |
| C-22 | Count-comparison COVERAGE GATE in Phase 4: entity count M declared in Phase 1 vs N in ACCESS MATRIX; M==N gate with PASS/FAIL; Phase 5 blocked until GATE STATUS = PASS | |
| C-23 | CLOSING VERDICT in Phase 8d names gap type and mechanism type per active [G-##] (MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / CASCADE-OVERREACH / BU-SCOPE); bare counts fail | |
| **C-24** | **Literal range string C-08..C-25 appears in C-21 mechanism phrase text above — confirmed: C-21 row reads "covers C-08..C-25 (18 rows)" as pre-printed text** | **PASS — pre-printed literal string C-08..C-25 is present in C-21 mechanism phrase; FM-SKILL-7 defended** |
| **C-25** | **SHALL-L above explicitly names C-22, C-23, C-24, C-25 as mandated obligation items — confirmed: SHALL-L reads "...MUST appear in C-22, C-23, C-24, and C-25 Self-Assessment cells" as pre-printed mandate** | **PASS — pre-printed SHALL-L names C-22, C-23, C-24, C-25; FM-SKILL-7 defended** |
