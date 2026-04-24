# trace-permissions Variate -- Round 3 (Rubric v3)
**Date:** 2026-03-15
**Rubric:** v3 (C-01 through C-16)
**Round note:** R14 (Round 2, session 2) targeted C-11 through C-14. Best performers: R14-V-04 (evidence-cited question fusion) and R14-V-05 (full four-criteria scaffold). This round targets the two v3 ceiling criteria: C-15 (write-time named violation markers) and C-16 (mandatory three-part evidence template). Prior rounds proved questions prevent omission and evidence citations prevent vacuous verdicts -- this round wires the two into a single structural unit and extends marker coverage beyond the scope-token domain.
**Target criteria focus:** C-15 (inline enforcement markers: SCOPE-FAIL / VERDICT-FAIL / EVIDENCE-REQUIRED / FLS-FAIL written at point of violation, not deferred) and C-16 (at least two gate answers using the exact template "Evidence: I checked [X] -- [result] because [Y]", fusing C-12 + C-14 into a single atomic unit) -- while preserving the complete essential/recommended/aspirational scaffold from prior rounds.

---

## Round 3 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format -- multi-marker enforcement system (SCOPE-FAIL / VERDICT-FAIL / EVIDENCE-REQUIRED / FLS-FAIL / GAP-FAIL declared as a typed system before any content) | R14-V-02 proved SCOPE-FAIL markers enforce C-13 at the scope-cell level. Extending the marker type system to cover all gate types should produce structural C-15 compliance -- when every gate has a named failure marker and its trigger rule appears before the gate runs, write-time enforcement becomes a system rather than a single lexicon rule |
| V-02 | Lifecycle emphasis -- enforcement rules are the literal first output element (before entity enumeration); each section reopens with a reminder of its active markers | Declaring all enforcement rules before any entity is known commits the model to the system before selective application is possible; restating active markers at each section boundary prevents rule decay after the first section |
| V-03 | Phrasing register -- two-pass checkpoint verifier: analyst produces each section (tables, findings), then verifier issues a checkpoint whose answer must use the exact C-16 three-part template | The checkpoint pass structurally requires all three template parts simultaneously -- a checkpoint cannot be satisfied with question-form alone or evidence-citation alone; the checkpoint is a required output section, not a formatting preference |
| V-04 | Role sequence (risk-ascending: CS floor -> integration mid-tier -> admin ceiling, bottom-up) + inline ELEVATION-UNJUSTIFIED markers at each tier transition | Running roles from minimum access upward turns each tier transition into a gate: "what does this tier add and why is it justified?" An ELEVATION-UNJUSTIFIED marker written at the point of unjustified elevation catches least-privilege violations at write-time rather than in a retrospective audit pass |
| V-05 | Combined: C-15 multi-marker system + C-16 evidence template + inertia framing (the "easier over-grant" temptation is named at each gate as the specific failure mode the evidence template must refute) | Naming the inertia threat at each gate (Org OWD because it's easier, System Admin because scoping takes effort, no FLS because profiles are overhead) pairs with the enforcement markers and evidence template as the structural defense -- a model that cannot refute "just grant Org access" with the three-part template has not analyzed the permission model |

---

## V-01 -- Output Format: Multi-Marker Enforcement System

**Axis:** Output format -- a named enforcement system with five violation marker types declared before any content
**Hypothesis:** R14-V-02 proved SCOPE-FAIL markers enforce C-13 at scope cells. This variation extends the principle to all gate types. Each gate type gets its own named marker and a trigger rule that appears before the gate runs. When VERDICT-FAIL, EVIDENCE-REQUIRED, and FLS-FAIL are active write-time markers -- not post-hoc flags -- the enforcement system is structural rather than aspirational. A trace that never shows a marker is a trace that never tested its rules.

---

You are running a permissions trace signal for: {{topic}}

---

## ENFORCEMENT SYSTEM (read before producing any output)

Five named markers are active in this trace. Each marker is written inline at the point of violation -- not noted at the end, not collected in a summary. The violation is visible at the moment of production.

| Marker | Trigger Rule | Action Required |
|--------|-------------|-----------------|
| `SCOPE-FAIL` | Any Record Scope cell contains prose instead of a lexicon token | Mark the cell SCOPE-FAIL and replace with a valid token before advancing to the next row |
| `VERDICT-FAIL` | Any escalation, sharing, or team gate produces a verdict without naming what was inspected | Mark the verdict VERDICT-FAIL and add the inspection record before advancing |
| `EVIDENCE-REQUIRED` | Any gate answer lacks the Evidence line "I checked [X] -- [result] because [Y]" | Mark the answer EVIDENCE-REQUIRED and complete the three-part Evidence line before advancing |
| `FLS-FAIL` | Any sensitive field is assessed without explicitly confirming whether a field security profile exists | Mark the field FLS-FAIL and complete the profile check before listing the next field |
| `GAP-FAIL` | Any gap identified in analysis is not immediately added to the Gap Register | Mark the analysis line GAP-FAIL and add the register row before continuing |

These markers are write-time controls. A trace that reaches its end with no markers triggered is a trace whose rules were never tested.

---

## SCOPE LEXICON (locked -- use tokens only in all Record Scope cells)

| Token | Meaning |
|-------|---------|
| `Org` | All records in the organization |
| `BU` | Records owned by users in the same business unit |
| `Parent-Child BU` | Records in the same BU and all child BUs |
| `Team:[name]` | Records owned by or shared to the named team |
| `User` | Only the user's own records |
| `Sharing:[rule name]` | Records reached via the named sharing rule |

---

**GAP REGISTER -- do not populate now. Return here after Stage 4.**

| # | Gap Type | Entity | Field (if FLS) | Role | Severity | Exact Fix |
|---|----------|--------|----------------|------|----------|-----------|

Gap types: FLS-EXPOSURE / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-CASCADE / OWD-MISMATCH
Severity: CRITICAL / HIGH / MEDIUM. Exact Fix: name the specific configuration object and post-fix state. "Tighten permissions" does not qualify.

---

## STAGE 1 -- INVENTORY

You are a Dataverse security architect.

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) |
|--------|-----------------|-----------------------------------|

For each High-sensitivity entity: check whether the OWD is broader than the sensitivity warrants. If it is: write OWD-MISMATCH -- [Entity] -- [OWD token] inline and add to Gap Register (GAP-FAIL if you do not).

**1b -- Operation-role matrix (one table per entity):**

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|--------|------|-------|--------|--------|--------------|

Record Scope: SCOPE LEXICON tokens only. For any prose entry: write SCOPE-FAIL inline and correct before advancing to the next row. Include every role with any privilege -- do not omit read-only roles.

**1c -- Field-level security:**

For each entity: enumerate every field with sensitivity >= Medium (PII / Financial / Health / Credential / Internal-Audit).

| Entity | Field | Sensitivity | FLS Profile? | Profile Name | Roles: Read | Roles: Write |
|--------|-------|-------------|-------------|--------------|-------------|--------------|

For each field: if FLS status is not explicitly confirmed, write FLS-FAIL inline before listing the next field.
If FLS Profile? = NO for a sensitive field: write FLS-FAIL + add FLS-EXPOSURE to Gap Register (Severity = CRITICAL) before continuing (GAP-FAIL if register row is not added immediately).
For entities with no sensitive fields: "Confirmed: [Entity] has no fields with sensitivity >= Medium. Fields reviewed: [list]." A blanket statement without the field list triggers FLS-FAIL.

---

## STAGE 2 -- PRIVILEGE ESCALATION

For each role with Write on team membership, security role assignment, record ownership, or BU configuration:

**Finding format:** `[Role] -> [Write action: specific privilege name] -> [Elevated access gained]` -- add ESCALATION-PATH to Gap Register (GAP-FAIL if not done immediately)

**Rule-out format (required per role):**
> **Evidence:** I checked [Role] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-category result] because [per-category structural reason].

A verdict of "no escalation" without this Evidence line is VERDICT-FAIL. A verdict with an Evidence line that does not name the privilege categories is VERDICT-FAIL. Write the marker inline and complete the Evidence line before continuing.

A blanket "no roles have escalation paths" without per-role examination is VERDICT-FAIL for every unchecked role.

---

## STAGE 3 -- SHARING RULES AND TEAM MEMBERSHIP

**3a -- Sharing rules:**

| Rule Name | Entity | Trigger | Access Opened | Record Scope | Overreach? |
|-----------|--------|---------|---------------|--------------|------------|

Record Scope: SCOPE LEXICON tokens only. SCOPE-FAIL inline for any prose entry.

For rules with Overreach? = YES: add SHARING-CONFLICT to Gap Register (GAP-FAIL if deferred).

If no rules exist:
> **Evidence:** I checked sharing rules for [entity list] in the solution -- no active rules found because [confirmation: checked Access > Sharing Rules for each entity].

A blanket "no sharing rules" without naming the entities checked is VERDICT-FAIL.

**3b -- Team membership:**

For each team-scoped role:

> **Evidence:** I checked team [name] membership control -- [mechanism] governs additions; self-addition is [possible / impossible] because [specific constraint].

A membership assessment without this Evidence line is EVIDENCE-REQUIRED. Write the marker inline and complete before continuing.

---

## STAGE 4 -- CROSS-TABLE CASCADE AND ROLE ASSESSMENT

**4a -- Cross-table cascade:**

Identify the highest-sensitivity entity from Stage 1. Trace through at least two relationship hops:

`[Role] -> [Entity A: operation, Record Scope: <token>] -> [Relationship type + cascade: Parental / Referential / None] -> [Entity B: operation, Record Scope: <token>] -> [cascade behavior] -> [Entity C: operation, Record Scope: <token>]`

Record Scope at each hop: SCOPE LEXICON tokens only. SCOPE-FAIL inline for any prose.

At each hop: state whether access is intentional (explicitly configured in the role) or emergent (consequence of relationship behavior). Emergent access to a High-sensitivity entity: add CROSS-CASCADE to Gap Register (GAP-FAIL if deferred).

**4b -- Stock role assessment:**

Name every Dataverse stock role in scope (Customer Service Representative, Basic User, System Customizer, System Administrator, or others). For each:

> **Evidence:** I checked the [Stock Role] default privilege table against the {{topic}} configuration -- [result: stock role access is / exceeds / falls short of custom configuration] because [specific privilege comparison].

Omitting this Evidence line is EVIDENCE-REQUIRED.

**4c -- Least-privilege scoring:**

| Role | Persona | Excess Privileges | LP Score (0-10) | Over-Privileged? | Reduction Required |
|------|---------|-------------------|-----------------|------------------|--------------------|

LP Score: 10 = exact least-privilege. Score < 7 = over-privileged. For each over-privileged role: name the specific privilege to reduce and the target scope. A general "restrict access" recommendation is not a specific reduction.

**4d -- Attack scenario (required if any ESCALATION-PATH in Gap Register):**

Step-by-step: `Starting role -> Action sequence -> Gained access`. Abstract risk statements do not satisfy this section.

---

Now return to the GAP REGISTER and fill it in completely. Every Exact Fix must name the specific configuration object and the post-fix state.

---

## V-02 -- Lifecycle Emphasis: Enforcement-First Declaration

**Axis:** Lifecycle emphasis -- enforcement rules are the literal first output element, before entity enumeration; each section reopens with a reminder of its active markers
**Hypothesis:** R14-V-05 placed structural constraints in a preamble section after the session header. This variation makes enforcement rules the first content before any entities or roles are known. A rule system declared with no entities in scope cannot be selectively applied to convenient cases. Restating the active markers at each section boundary prevents rule decay: a rule declared once can fade from working context; a rule restated at each section header cannot.

---

You are running a permissions trace signal for: {{topic}}

---

## ENFORCEMENT DECLARATION (first output -- produce this before enumerating any entity)

Commit to these enforcement rules now. They apply to every section that follows.

**Rule E-1 (Scope tokens):** Every Record Scope cell uses exactly one token: `Org` / `BU` / `Parent-Child BU` / `Team:[name]` / `User` / `Sharing:[rule name]`. A prose entry is SCOPE-FAIL -- write the marker inline and correct before the next row.

**Rule E-2 (Verdict evidence):** Every verdict at a security gate carries an Evidence line: "I checked [named objects] -- [result] because [reason]." A verdict without this line is EVIDENCE-REQUIRED -- write the marker inline and complete the line before advancing.

**Rule E-3 (FLS confirmation):** Every sensitive field has its FLS profile status explicitly confirmed before the next field is listed. A field assessed without FLS status confirmation is FLS-FAIL -- write the marker inline and complete the check before advancing.

**Rule E-4 (Immediate gap registration):** Every gap is added to the register at the point of identification -- not batched for the end. A gap identified but not yet in the register is GAP-FAIL -- write the marker inline and add the row before continuing.

These markers are write-time controls. A trace that reaches its end with zero markers triggered has never tested whether its rules were applied.

**GAP REGISTER -- add rows as gaps are found, not at the end.**

| # | Gap Type | Entity | Field (if FLS) | Role | Severity | Exact Fix |
|---|----------|--------|----------------|------|----------|-----------|

Gap types: FLS-EXPOSURE / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-CASCADE / OWD-MISMATCH
Severity: CRITICAL / HIGH / MEDIUM. Exact Fix: name the configuration object and post-fix state.

---

## STAGE 1 -- INVENTORY

**[Active markers this stage: SCOPE-FAIL (E-1) / FLS-FAIL (E-3) / GAP-FAIL (E-4)]**

You are a Dataverse security architect.

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) |
|--------|-----------------|-----------------------------------|

**1b -- Operation-role matrix (one table per entity):**

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|--------|------|-------|--------|--------|--------------|

E-1 active: SCOPE-FAIL inline for any non-token scope cell. Correct before the next row. Include every role with any privilege.

**1c -- Field-level security:**

For each entity: list every field with sensitivity >= Medium (PII / Financial / Health / Credential / Internal-Audit).

| Entity | Field | Sensitivity | FLS Profile? | Profile Name | Roles: Read | Roles: Write |
|--------|-------|-------------|-------------|--------------|-------------|--------------|

E-3 active: FLS-FAIL for any field where profile status is not explicitly confirmed. E-4 active: GAP-FAIL if FLS-EXPOSURE is identified but register row is not added immediately.

For entities with no sensitive fields: "Confirmed: [Entity] -- no fields with sensitivity >= Medium. Reviewed: [list]."

---

## STAGE 2 -- PRIVILEGE ESCALATION

**[Active markers this stage: EVIDENCE-REQUIRED (E-2) / VERDICT-FAIL for blanket statements / GAP-FAIL (E-4)]**

For each role in the Stage 1 matrix: check all four escalation vectors.

**Per-role required format:**
- Finding: `[Role] -> [Action] -> [Elevated access]` -- add to Gap Register (E-4: now)
- Rule-out: "I checked [Role] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-category result] because [per-category structural reason]."

E-2 active: any verdict without "I checked [X] -- [result] because [Y]" is EVIDENCE-REQUIRED. Write the marker and complete the line before continuing. A blanket statement covering multiple roles without per-role examination is VERDICT-FAIL for each unchecked role.

---

## STAGE 3 -- SHARING RULES AND TEAM GAPS

**[Active markers this stage: SCOPE-FAIL (E-1) / EVIDENCE-REQUIRED (E-2) / GAP-FAIL (E-4)]**

**3a -- Sharing rules:**

| Rule Name | Entity | Trigger | Access Opened | Record Scope | Overreach? |
|-----------|--------|---------|---------------|--------------|------------|

E-1 active in Record Scope column. For no rules: "I checked sharing rules for [entity list] -- no active rules found because [confirmation of check]."

Overreach? = YES: add SHARING-CONFLICT to register (E-4).

**3b -- Team membership:**

For each team-scoped role:

"I checked team [name] membership control -- [mechanism]; self-addition is [possible / impossible] because [specific constraint]."

E-2 active: a membership assessment without this format is EVIDENCE-REQUIRED.

---

## STAGE 4 -- CROSS-ENTITY CASCADE AND ROLE ANALYSIS

**[Active markers this stage: SCOPE-FAIL (E-1) / EVIDENCE-REQUIRED (E-2) / GAP-FAIL (E-4)]**

**4a -- Cross-table cascade:**

Highest-sensitivity entity from Stage 1. Trace at least two relationship hops:

`[Role] -> [Entity A: operation, Record Scope: <token>] -> [Relationship + cascade: Parental / Referential / None] -> [Entity B: operation, Record Scope: <token>] -> [cascade] -> [Entity C: operation, Record Scope: <token>]`

E-1 active at each scope cell. At each hop: intentional or emergent? Emergent access to High-sensitivity: GAP-FAIL until CROSS-CASCADE row is in register.

**4b -- Stock role assessment:**

For each Dataverse stock role in scope:

"I checked [Stock Role] default privileges against {{topic}} configuration -- [result] because [specific comparison]."

E-2 active: omitting this format is EVIDENCE-REQUIRED.

**4c -- Least-privilege scoring:**

| Role | Persona | Excess Privileges | LP Score (0-10) | Over-Privileged? | Reduction |
|------|---------|-------------------|-----------------|------------------|-----------|

Score < 7: state specific reduction and target scope.

**4d -- Attack scenario (if any ESCALATION-PATH in register):**

Step-by-step: `Starting role -> Action sequence -> Gained access`. Abstract statements fail.

---

Return to GAP REGISTER. Every Exact Fix must name the configuration object. Any row without an Exact Fix is GAP-FAIL.

---

## V-03 -- Phrasing Register: Two-Pass Checkpoint Verifier

**Axis:** Phrasing register -- two-pass structure: analyst writes each section in production pass, verifier answers checkpoint questions using the exact C-16 evidence template
**Hypothesis:** The evidence template "Evidence: I checked [X] -- [result] because [Y]" can be satisfied superficially if the three parts are allowed to appear in free-form positions across the output. A two-pass format -- where the checkpoint is a required structural section that must produce the exact template -- prevents partial compliance: the checkpoint cannot be satisfied with a question alone (satisfies C-14) or an evidence citation alone (satisfies C-12). Both must appear in the checkpoint format simultaneously, which is the structural definition of C-16.

---

You are running a permissions trace signal for: {{topic}}

You run this trace in two passes per stage:
- **Production pass:** Build the permission model as a Dataverse security architect (tables, matrices, gap findings).
- **Checkpoint pass:** Answer the checkpoint questions as a security verifier. Every checkpoint answer must use the exact template:

> `Evidence: I checked [specifically named objects or privilege categories] -- [specific result] because [specific structural reason].`

All three parts are required. A result without "because [reason]" does not satisfy the checkpoint. A "because [reason]" without "I checked [X]" does not satisfy the checkpoint. A checkpoint answer that omits the Evidence line fails.

The trace is not complete until all checkpoint answers are present and follow the template.

---

**GAP REGISTER -- do not populate now. Return here after Stage 3.**

| # | Gap Type | Entity | Field (if FLS) | Role | Severity | Exact Fix |
|---|----------|--------|----------------|------|----------|-----------|

Gap types: FLS-EXPOSURE / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-CASCADE
Severity: CRITICAL / HIGH / MEDIUM. Exact Fix: name the configuration object and post-fix state.

---

## STAGE 1 -- INVENTORY (Production Pass)

You are a Dataverse security architect.

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) |
|--------|-----------------|-----------------------------------|

**1b -- Operation-role matrix (one table per entity):**

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Parent-Child BU / Team:[name] / User / Sharing:[rule name]. Include every role with any privilege.

**1c -- Field-level security:**

| Entity | Field | Sensitivity | FLS Profile? | Profile Name | Roles: Read | Roles: Write |
|--------|-------|-------------|-------------|--------------|-------------|--------------|

Sensitivity categories: PII / Financial / Health / Credential / Internal-Audit.
Sensitive field with no FLS profile: add FLS-EXPOSURE to Gap Register immediately.
Entity with no sensitive fields: "Confirmed: [Entity] -- no sensitive fields. Reviewed: [list]."

---

### STAGE 1 CHECKPOINT (Verifier)

Answer each question. Every answer must follow the exact template: `Evidence: I checked [X] -- [result] because [Y].`

**CP-1.1: Have all sensitive fields been assessed for FLS coverage?**
Evidence: I checked [fields examined per entity] -- [result: all covered / N fields missing profiles] because [profile name exists / profile absent for: field name / entity has no sensitive fields, reviewed: list].

**CP-1.2: Is the OWD for each High-sensitivity entity appropriately restrictive?**
Evidence: I checked [OWD setting per entity] -- [result: Private / BU / Organization] because [data sensitivity / compensating FLS controls present / no compensating controls].

**CP-1.3: Does every Record Scope cell in the operation matrix use a valid scope token?**
Evidence: I checked all Record Scope cells in Stage 1b -- [result: all cells use valid tokens / N cells contain prose] because [lexicon followed / lexicon not followed for these cells: list].
If any cell fails: correct it now and restate the checkpoint answer.

---

## STAGE 2 -- GAP ANALYSIS (Production Pass)

**2a -- Privilege escalation:**

For each role with Write on team membership, security role assignment, record ownership, or BU configuration:
- Finding: `[Role] -> [Action] -> [Elevated access]` -- add ESCALATION-PATH to Gap Register
- Rule-out: "Checked [Role]: team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- none present because [per-category reason]."

**2b -- Sharing rules:**

| Rule Name | Entity | Trigger | Access Opened | Record Scope | Overreach? |
|-----------|--------|---------|---------------|--------------|------------|

Overreach? = YES: add SHARING-CONFLICT to Gap Register. No rules: "Confirmed: checked sharing rules for [entity list] -- no active rules found."

**2c -- Team membership:**

For each team-scoped role: state who controls membership and whether self-addition is possible. Name the specific constraint.

**2d -- BU hierarchy:**

For each role with BU-scoped access: show at least one path:
`[Role] -> [BU scope token] -> [child BU records: visible YES/NO] -> [reason: OWD + scope combination]`

---

### STAGE 2 CHECKPOINT (Verifier)

**CP-2.1: Has every role been checked for privilege escalation paths?**
Evidence: I checked [role list] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-role result] because [per-role structural reason per category].

**CP-2.2: Have all active sharing rules been assessed for overreach?**
Evidence: I checked sharing rules [list or "no rules found"] for entities [list] -- [per-rule result] because [comparison of opened access to OWD + role scope].

**CP-2.3: Is team membership for every team-scoped role controlled in a way that prevents unauthorized elevation?**
Evidence: I checked team [name] membership control -- [mechanism]; self-addition is [possible / impossible] because [specific constraint].

---

## STAGE 3 -- ROLE ASSESSMENT AND REMEDIATION (Production Pass)

**3a -- Customer Service Representative:**

Per entity: CRUD + Assign + Record Scope. Per sensitive field: state whether this role can read or write it.

**3b -- Dataverse Security Expert:**

Per entity: CRUD + Assign + Record Scope. State every privilege the expert holds that CS does not.

**3c -- Cross-table cascade:**

Highest-sensitivity entity. Trace at least two relationship hops:

`[Role] -> [Entity A: operation, scope] -> [Relationship + cascade: Parental / Referential / None] -> [Entity B: operation, scope] -> [cascade] -> [Entity C: operation, scope]`

At each hop: intentional or emergent? Emergent access to High-sensitivity: add CROSS-CASCADE to Gap Register.

**3d -- Least-privilege scoring:**

| Role | Persona | Excess Privileges | LP Score (0-10) | Over-Privileged? | Reduction |
|------|---------|-------------------|-----------------|------------------|-----------|

Score < 7: state specific reduction and target scope.

**3e -- Attack scenario (if any ESCALATION-PATH in register):**
Step-by-step: `Starting role -> Action sequence -> Gained access`.

---

### STAGE 3 CHECKPOINT (Verifier)

**CP-3.1: Does the Customer Service Representative access any sensitive field or operation beyond what the CS job function requires?**
Evidence: I checked CS access for [entity list, sensitive field list] -- [per-item result] because [FLS profile / OWD / role scope].

**CP-3.2: Does the Dataverse Security Expert hold any privilege exceeding least-privilege for a security configuration task?**
Evidence: I checked expert privileges beyond CS access -- [excess list or NONE] because [comparison to what security configuration task requires].

**CP-3.3: Does every gap in the Gap Register have a specific Exact Fix naming the configuration object and post-fix state?**
Evidence: I checked every Exact Fix row in the Gap Register -- [result: all rows name specific objects / N rows lack specificity] because [configuration object named / "tighten permissions" or similar phrase appears in row N].

---

Return to the GAP REGISTER and fill it in completely.

---

## V-04 -- Combined: Risk-Ascending Role Sequence + Elevation Markers

**Axis:** Role sequence (risk-ascending: CS floor -> integration mid-tier -> admin ceiling) + inline ELEVATION-UNJUSTIFIED markers at each tier transition
**Hypothesis:** R13-V-04 ran ceiling-to-floor. Running bottom-up changes the analytic frame: instead of asking "what does this role restrict from the ceiling?" the question becomes "what does this role add over the minimum, and is that addition justified?" An ELEVATION-UNJUSTIFIED marker written at the transition point catches the least-privilege violation at write-time. The mid-tier (integration/service account) remains the most dangerous analysis surface because it accumulates privilege without the scrutiny applied to human roles.

---

You are running a permissions trace signal for: {{topic}}

You are a Dataverse security architect tracing access from the floor up. Begin with the minimum access (CS Floor), then examine what each higher tier adds and whether that addition is justified by a distinct business or technical function.

**Tier sequence (bottom-up):**
1. **CS Floor** -- The Customer Service Representative (stock role or custom equivalent): minimum human access baseline.
2. **Mid-Tier** -- Any integration account, service principal, Power Automate user, or elevated human role (e.g., Sales Manager, Team Lead). If no non-human account exists: use the next role above CS and state the substitution explicitly.
3. **Admin Ceiling** -- The highest-privilege role: System Administrator, System Customizer with broad access, or a custom admin role.

**Inline elevation marker rules:**

At each tier transition, write one of:
- `ELEVATION-JUSTIFIED: [tier] adds [specific privilege or scope] over [previous tier] because [specific business or technical function that requires this addition].`
- `ELEVATION-UNJUSTIFIED: [tier] adds [specific privilege or scope] over [previous tier] with no justified function difference. FLAG for reduction.`

`ELEVATION-UNJUSTIFIED` is a write-time marker. Write it at the point of the unjustified transition, then immediately add an ESCALATION-PATH or ELEVATION-UNJUSTIFIED row to the Gap Register.

---

**GAP REGISTER -- do not populate now. Return here after Stage 5.**

| # | Gap Type | Entity | Field (if FLS) | Role | Severity | Exact Fix |
|---|----------|--------|----------------|------|----------|-----------|

Gap types: FLS-EXPOSURE / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-CASCADE / ELEVATION-UNJUSTIFIED
Severity: CRITICAL / HIGH / MEDIUM. Exact Fix: name the configuration object and post-fix state.

---

## STAGE 1 -- FOUNDATION INVENTORY

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) |
|--------|-----------------|-----------------------------------|

**1b -- Three-tier role roster:**

| Tier | Role Name | Type (human / non-human) | Stock Role? | Custom Role? | Primary Function |
|------|-----------|--------------------------|-------------|--------------|------------------|

Identify all three tiers. If mid-tier non-human account does not exist: name the highest-privilege non-admin human role and write "SUBSTITUTION: [role] used as mid-tier because no integration/service account is present."

**1c -- Field-level security (three-tier view):**

| Entity | Field | Sensitivity | FLS Profile? | CS Floor: Read/Write | Mid-Tier: Read/Write | Admin: Read/Write |
|--------|-------|-------------|-------------|----------------------|----------------------|-------------------|

For sensitive fields with no FLS profile: add FLS-EXPOSURE to Gap Register now. For entities with no sensitive fields: "Confirmed: [Entity] -- no sensitive fields. Reviewed: [list]."

---

## STAGE 2 -- CS FLOOR BASELINE

Build the complete access model for CS Floor first. No other tier's access is analyzed until the baseline is established.

**CS Floor operation matrix:**

| Entity | Create | Read | Write | Delete | Assign | Record Scope |
|--------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Parent-Child BU / Team:[name] / User / Sharing:[rule name]. No prose entries.

**CS Floor FLS access:** For each sensitive field: state whether CS Floor can read it, write it, or is blocked by FLS profile.

**CS Floor escalation check:**

> **Evidence:** I checked [CS Floor role name] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-category result] because [per-category structural reason].

This Evidence line is required. A verdict without it is incomplete.

---

## STAGE 3 -- MID-TIER DELTA (what mid-tier adds over CS floor)

For each entity and operation: compare mid-tier access against CS Floor baseline.

**Mid-tier delta grid (one per entity):**

| Entity | Operation | CS Floor | Mid-Tier | Delta? | Elevation Marker |
|--------|-----------|----------|---------|--------|------------------|

Delta? = YES if mid-tier holds a privilege or scope CS does not.
For each YES delta: write the elevation marker inline:
- `ELEVATION-JUSTIFIED: [role] adds [privilege/scope] over CS because [specific business or technical function].`
- `ELEVATION-UNJUSTIFIED: [role] adds [privilege/scope] over CS with no justified function difference.` -- add to Gap Register immediately.

**Mid-tier FLS delta:** For each sensitive field where mid-tier FLS access differs from CS Floor: ELEVATION-JUSTIFIED or ELEVATION-UNJUSTIFIED?

**Mid-tier escalation check:**

> **Evidence:** I checked [mid-tier role name] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-category result] because [per-category structural reason].

Special check for non-human mid-tier: can this service account add itself to a team that grants Org-level scope?

> **Evidence:** I checked whether [service account] can reach team membership modification -- [result] because [specific privilege check: team membership API access / delegation path / admin-only control].

---

## STAGE 4 -- ADMIN CEILING DELTA (what admin adds over mid-tier)

**Admin ceiling delta grid (one per entity):**

| Entity | Operation | Mid-Tier | Admin Ceiling | Delta? | Elevation Marker |
|--------|-----------|---------|---------------|--------|------------------|

For each YES delta: ELEVATION-JUSTIFIED or ELEVATION-UNJUSTIFIED?

Expected justified admin elevations: security role management, OWD configuration, system customization, cross-BU oversight. Any elevation beyond these domains requires explicit justification or triggers ELEVATION-UNJUSTIFIED.

**Admin reachability check:** State whether CS Floor or mid-tier can reach admin ceiling access through any of the four escalation vectors. This is the critical question:

> **Evidence:** I checked whether [CS Floor / mid-tier] can reach [Admin Ceiling role's access level] through team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [result] because [specific control that closes each vector per tier].

---

## STAGE 5 -- GAP ANALYSIS AND REMEDIATION

**5a -- Sharing rules (tier-aware):**

| Rule Name | Entity | Trigger | Access Opened | Record Scope | Tier Benefiting | Intended? | Overreach? |
|-----------|--------|---------|---------------|--------------|-----------------|-----------|------------|

For rules that benefit mid-tier: state whether the rule was configured with mid-tier in mind or was intended for human roles only. Record Scope: lexicon tokens only.

**5b -- Cross-table cascade:**

Trace from CS Floor through at least two relationship hops to the highest-sensitivity entity:

`[CS Floor] -> [Entity A: operation, scope] -> [Relationship + cascade: Parental / Referential / None] -> [Entity B: operation, scope] -> [cascade] -> [Entity C: operation, scope]`

At each hop: intentional or emergent? Does mid-tier or admin ceiling inherit more cascade access than their tier's function requires? ELEVATION-UNJUSTIFIED if yes.

**5c -- Least-privilege scoring:**

| Tier | Role | Excess Privileges | LP Score (0-10) | ELEVATION-UNJUSTIFIED Findings | Reduction Required |
|------|------|-------------------|-----------------|-------------------------------|---------------------|

For LP Score < 7: state specific reduction.

**5d -- Attack scenario (if any ESCALATION-PATH in register):**
`Starting role -> Action sequence -> Gained access.`

---

Return to GAP REGISTER. Every Exact Fix must name the configuration object.

---

## V-05 -- Combined: C-15 Marker System + C-16 Template + Inertia Framing

**Axis:** C-15 enforcement markers + C-16 evidence-template gate answers + inertia framing (the specific "easier over-grant" temptation is named at each gate as the failure mode the evidence template must refute)
**Hypothesis:** Permission models fail toward comfort: Org OWD is easier than Private + sharing rules; System Admin is easier than a scoped custom role; no FLS is easier than building profiles. Naming each inertia threat at the gate where it applies -- and then requiring the three-part evidence template to refute it specifically -- produces the strongest structural pressure on C-13, C-14, C-15, and C-16 simultaneously. A model that cannot complete "Evidence: I checked [X] -- [result] because [Y]" in response to a named inertia threat has not analyzed the permission model; it has repeated the inertia assumption.

---

You are running a permissions trace signal for: {{topic}}

---

## PREAMBLE: THE INERTIA THREAT

Permission models accumulate risk through the path of least resistance. This trace names each inertia threat at the gate where it appears and requires an evidence-backed refutation. Silence at an inertia gate means the easier wrong choice was not ruled out.

| # | Inertia Threat | Gate | Why It's Dangerous |
|---|---------------|------|-------------------|
| I-1 | Org-level OWD: easier than Private + sharing rules | OWD assessment | All users read all records; FLS becomes the sole protection layer |
| I-2 | System Admin for everything: easier than custom role scoping | Least-privilege assessment | System Admin bypasses OWD, FLS, and all security role checks |
| I-3 | No FLS on sensitive fields: profile creation is overhead | Field-level security | Any role with entity Read can see PII, financial, or credential data |
| I-4 | Sharing rule added without review date or expiry: quicker than proper scoping | Sharing rule audit | Rule accumulates access, reopening restricted data indefinitely |
| I-5 | Service account with Org scope: simpler than least-privilege scoping | Service account assessment | Non-human account with broadest access is the highest-value escalation target |

Each gate section opens with the applicable inertia threat. The evidence template is your refutation. An inertia threat that reaches the end of its gate section without a completed evidence-template answer is `INERTIA-UNCHECKED` -- write the marker inline.

---

## ENFORCEMENT RULES

**Rule C-15 (Write-time markers):** Four markers are active throughout this trace. Write each inline at point of violation:
- `SCOPE-FAIL` -- Record Scope cell with prose instead of a lexicon token; correct before next row
- `VERDICT-FAIL` -- Gate verdict without a named inspection record; complete before advancing
- `EVIDENCE-REQUIRED` -- Gate answer without the three-part template; complete before advancing
- `INERTIA-UNCHECKED` -- Inertia gate reached end of section without evidence-template refutation

**Rule C-16 (Evidence template):** Every gate answer must include:
`Evidence: I checked [specifically named objects or privilege categories] -- [specific result] because [specific structural reason].`
All three parts are required. Missing "because [reason]": EVIDENCE-REQUIRED. Missing "I checked [X]": EVIDENCE-REQUIRED.

---

## SCOPE LEXICON (locked)

| Token | Meaning |
|-------|---------|
| `Org` | All records in the organization |
| `BU` | Records in the same business unit |
| `Parent-Child BU` | Records in the same BU and all child BUs |
| `Team:[name]` | Records owned by or shared to the named team |
| `User` | Only the user's own records |
| `Sharing:[rule name]` | Records reached via the named sharing rule |

---

**GAP REGISTER -- add rows as gaps are found.**

| # | Gap Type | Entity | Field (if FLS) | Role | Severity | Exact Fix |
|---|----------|--------|----------------|------|----------|-----------|

Gap types: FLS-EXPOSURE / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-CASCADE / OWD-MISMATCH / ELEVATION-UNJUSTIFIED
Severity: CRITICAL / HIGH / MEDIUM. Exact Fix: configuration object + post-fix state.

---

## STAGE 1 -- ENTITY AND OWD INVENTORY

**1a -- Entity and OWD table:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) |
|--------|-----------------|-----------------------------------|

**[Inertia threat I-1 active: Is the OWD set to Organization because it was easier than Private + sharing rules?]**

For each entity with Sensitivity = High or Medium:

> **Gate I-1:** Is the OWD more permissive than the data sensitivity warrants?
> Evidence: I checked OWD settings for [entity] -- [result: Private / BU / Organization] because [configuration rationale: data sensitivity / compensating FLS controls present / no compensating control exists].

OWD = Organization with no compensating FLS: INERTIA-UNCHECKED if gate not answered. Add OWD-MISMATCH to Gap Register.

**1b -- Operation-role matrix (one table per entity):**

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|--------|------|-------|--------|--------|--------------|

SCOPE-FAIL active: prose Record Scope entry -> marker inline + correct before next row.

**1c -- Role identification:**

List every security role in scope. Name every Dataverse stock role (Customer Service Representative, Basic User, System Customizer, System Administrator, or others).

**[Inertia threat I-2 active: Has System Admin been assigned because scoping a custom role is effort?]**

> **Gate I-2:** Does any role in scope use System Administrator when a restricted custom role would suffice for its function?
> Evidence: I checked each role assignment against its persona function -- [per-role result] because [specific function comparison: what the persona needs vs. what System Admin grants beyond that].

System Admin used without justification: INERTIA-UNCHECKED if gate not answered. Add ELEVATION-UNJUSTIFIED to Gap Register.

---

## STAGE 2 -- FIELD-LEVEL SECURITY

**[Inertia threat I-3 active: Were FLS profiles skipped because profile creation is overhead?]**

For each entity: enumerate every field with sensitivity >= Medium (PII / Financial / Health / Credential / Internal-Audit).

> **Gate I-3:** Does every sensitive field on every entity have a field security profile, or were profiles skipped?
> Evidence: I checked Security > Field Security Profiles for [entity list] -- [per-field result: profile [name] exists / no profile found for [field name]] because [profile creation was required by design / FLS was not configured for this field].

For each field with no profile: SCOPE-FAIL inapplicable here; instead write FLS-FAIL inline, add FLS-EXPOSURE to Gap Register (CRITICAL), then complete the gate before listing the next field. INERTIA-UNCHECKED if Gate I-3 reaches end of section without the evidence-template answer.

| Entity | Field | Sensitivity | FLS Profile? | Profile Name | Roles: Read | Roles: Write |
|--------|-------|-------------|-------------|--------------|-------------|--------------|

For entities with no sensitive fields: "Confirmed: [Entity] -- no fields with sensitivity >= Medium. Reviewed: [list]."

---

## STAGE 3 -- PRIVILEGE ESCALATION

For each role: check all four escalation vectors (team-membership-write / role-assign-write / ownership-reassign / BU-config-write).

> **Gate escalation:** Can any role reach a higher privilege level through the available vectors?
> Evidence: I checked [role list] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-role, per-category result] because [per-role structural reason].

VERDICT-FAIL if any role is not individually named. EVIDENCE-REQUIRED if the Evidence line is absent or incomplete.

**[Inertia threat I-5 active: Does any service or integration account have Org scope because least-privilege scoping was not applied?]**

For each non-human role:

> **Gate I-5:** Does this service account hold Org-level scope or System Admin privileges when a narrower scope would suffice?
> Evidence: I checked [service account role] scope -- [token: Org / BU / User] -- because [automation function: what records the account needs to access, and whether Org scope is necessary or merely convenient].

Org scope without automation justification: INERTIA-UNCHECKED if gate not answered. Add ELEVATION-UNJUSTIFIED to Gap Register.

---

## STAGE 4 -- SHARING RULES, TEAM MEMBERSHIP, AND CASCADE

**[Inertia threat I-4 active: Is any sharing rule present without a documented review date or expiry?]**

**4a -- Sharing rules:**

| Rule Name | Entity | Trigger | Access Opened | Record Scope | Review Date | Overreach? |
|-----------|--------|---------|---------------|--------------|-------------|------------|

SCOPE-FAIL active in Record Scope column.

> **Gate I-4:** Does any active sharing rule reopen access the OWD + role model restricts, or exist without a documented review date?
> Evidence: I checked sharing rules [list or "no rules found"] for [entity list] -- [per-rule result: access opened vs. OWD + role scope, review date status] because [rule intent vs. current configuration comparison].

Rules without review date: INERTIA-UNCHECKED (flag as SHOULD-review). Rules with overreach: add SHARING-CONFLICT to Gap Register.

**4b -- Team membership:**

> **Gate team:** Is team membership for every team-scoped role controlled in a way that prevents unauthorized elevation?
> Evidence: I checked team [name] membership control -- [mechanism]; self-addition is [possible / impossible] because [specific constraint].

**4c -- Cross-table cascade:**

Highest-sensitivity entity. Trace at least two relationship hops:

`[Role] -> [Entity A: operation, Record Scope: <token>] -> [Relationship + cascade: Parental / Referential / None] -> [Entity B: operation, Record Scope: <token>] -> [cascade] -> [Entity C: operation, Record Scope: <token>]`

SCOPE-FAIL active at each hop scope cell. At each hop: intentional or emergent? Emergent access to High-sensitivity entity: add CROSS-CASCADE to Gap Register.

---

## STAGE 5 -- ROLE ASSESSMENT AND INERTIA AUDIT

**Customer Service Representative gate:**

> **Evidence:** I checked CS role access for [entity list, sensitive field list] -- [per-item result] because [FLS profile / OWD / role scope].

**Dataverse Security Expert gate:**

> **Evidence:** I checked expert role privileges beyond CS access -- [excess list or NONE] because [comparison to what security configuration task scope requires].

Both roles must appear by name with distinct specific observations.

**Least-privilege scoring:**

| Role | Persona | Inertia Threat Applied? (I-1 through I-5) | Excess Privileges | LP Score (0-10) | Reduction Required |
|------|---------|------------------------------------------|-------------------|-----------------|---------------------|

LP Score < 7: state specific reduction and target scope. Note which inertia threat (I-1 through I-5) contributed to the over-privilege.

**Attack scenario (if any ESCALATION-PATH in register):**
`Starting role -> Action sequence -> Gained access.`

**INERTIA-UNCHECKED audit (required before finishing):**

Review each inertia gate (I-1 through I-5). For any gate that was not answered with a complete Evidence line: complete it now. A trace that ends with any INERTIA-UNCHECKED marker is incomplete.

---

Return to GAP REGISTER. Every Exact Fix must name the configuration object and post-fix state.
