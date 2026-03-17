# trace-permissions Variate -- Round 6 (Rubric v6)
**Date:** 2026-03-15
**Rubric:** v6 (C-01 through C-28)
**Round note:** Rubric v6 adds four new aspirational criteria (C-25--C-28) extracted directly from R5 scorecard signals. C-25 requires a tier-stratified FLS table (lowest tier at which each sensitive field is reachable is structurally visible). C-26 requires a named gate-absence marker (skipped gates are a distinct failure mode from content-error). C-27 requires binary gate definitions to name excluded language (hedging phrases cannot satisfy a gate that explicitly names them as disqualifying). C-28 requires that pre-committed artifacts (Temptation Ledger, Gap Register) are cited by name in at least one later gate (converting declaration into active constraint). This round explores C-25, C-26, C-27 as single axes (output format, lifecycle emphasis, phrasing register), then combines lifecycle + phrasing (V-04), then wires all four into the complete R6 scaffold (V-05).

---

## Round 6 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format -- tier-stratified FLS table replaces flat role-to-field map | C-25 requires the FLS analysis to organize fields by tier column, not by role list. A flat Roles:Read/Roles:Write table satisfies C-02 by listing who can access a field but does not reveal which tier that access starts at. A T-column matrix makes the lowest tier at which each sensitive field becomes reachable structurally visible before analysis -- a cross-tier FLS gap appears as YES in a low-tier Write column rather than as an inference from role names |
| V-02 | Lifecycle emphasis -- gate-absence named markers as mandatory structural checkpoints | C-26 requires a named marker that fires when a mandatory gate section is absent, not just when gate content is wrong. C-15/C-17 markers fire on content violations; a skipped gate produces no content and no content-error. Adding GATE-ABSENT markers creates a structural signal for omission -- making gate-skipping a named, detectable failure mode at the same structural level as gate-content-error |
| V-03 | Phrasing register -- binary gate anti-hedging exclusion named at definition time | C-27 requires binary gate definitions to include at least one explicitly named excluded phrase. Without named exclusions, "probably justified" can satisfy the surface form of a binary gate. Naming excluded language at definition time closes this gap before any output is written: the writer cannot satisfy the gate with language the definition explicitly disqualifies |
| V-04 | Combined: lifecycle emphasis (C-26) + phrasing register (C-27) | Gate-absence and anti-hedging target the same gate from two failure directions: C-26 ensures the T-4 binary gate cannot be silently omitted; C-27 ensures that when present, it cannot be satisfied by hedging. Together they close both failure paths for the highest-risk assignment point |
| V-05 | Combined: all four R6 criteria on the full C-11--C-24 scaffold | The R5-V-05 scaffold achieves 98.0 by satisfying C-11--C-24; the four new criteria fit cleanly. C-25 replaces the flat FLS table with a tier-stratified matrix; C-26 extends the enforcement marker system to cover gate-absence; C-27 adds named exclusions to all binary gate definitions; C-28 mandates that each Stage 2 tier-boundary gate and the Stage 3 T-4 gate explicitly cite a named Temptation Ledger entry -- converting the Ledger from a structural formality into an active constraint with named checkpoints |

---

## V-01 -- Output Format: Tier-Stratified FLS Table

**Axis:** Output format -- the FLS matrix in Stage 1 is organized by tier column (T-1/T-2/T-3/T-4 columns) rather than by role list, making the lowest tier at which each sensitive field becomes reachable structurally visible before analysis
**Hypothesis:** C-25 requires the FLS analysis to reveal the lowest tier at which each sensitive field becomes readable or writable. A flat "Roles: Read | Roles: Write" table satisfies C-02 by listing who can access a field but does not surface whether that access starts at T-1 or T-3. Replacing role columns with tier columns forces the matrix to answer a structurally more dangerous question: not which roles can reach this field, but at what tier does it first become reachable? A field writable at T-2 when only T-3 operations require write access is invisible in a role list but obvious as YES in the T-2 Write column.

---

You are running a permissions trace signal for: {{topic}}

---

## ENFORCEMENT SYSTEM (complete before any entity name, operation, or content)

| Marker | Domain | Trigger Condition | Correction Required |
|--------|--------|-------------------|---------------------|
| `SCOPE-FAIL` | Record Access | Any Record Scope cell contains prose rather than a SCOPE LEXICON token | Replace with exact SCOPE LEXICON token before advancing to the next row |
| `VERDICT-FAIL` | Verdict | Any gate answer omits a binary verdict, or conclusion is expressed in hedging language | Restate with a declared binary verdict before advancing |
| `EVIDENCE-REQUIRED` | Evidence | Any gate answer lacks an Evidence line ("I checked [X] -- [result] because [Y]") | Add the three-part Evidence line before advancing to the next gate |
| `FLS-FAIL` | Field Security | A sensitive field (PII / Financial / Health / Credential / Internal-Audit) appears in the FLS matrix without a field security profile | Add FLS-EXPOSURE to Gap Findings Table immediately; do not defer |
| `GAP-FAIL` | Gap / Conflict | A gap category is investigated with no explicit finding or explicit rule-out | State the finding or rule-out with evidence before advancing |

**Section-open rule:** At the start of Stage 1, Stage 2, and Stage 3, re-declare active markers by name before any section content appears.

---

## SCOPE LEXICON (locked)

| Token | Meaning |
|-------|---------|
| `Org` | All records in the organization |
| `BU` | Records owned by users in the same business unit |
| `Parent-Child BU` | Records in the same BU and all child BUs |
| `Team:[name]` | Records owned by or shared to a named team (substitute actual name) |
| `User` | Only the user's own records |
| `Sharing:[rule name]` | Records accessible via a named sharing rule (substitute actual rule name) |

---

## PRIVILEGE TIER LADDER (complete before Gap Register -- locked after this section)

| Tier | Label | Privilege Boundary | Signature Capabilities |
|------|-------|-------------------|------------------------|
| T-1 | Read-Only Floor | Read records within assigned scope only | Read on entities; no Create, Write, Delete, Assign |
| T-2 | Operational | Create and write records within assigned scope | Create + Read + Write; no security configuration |
| T-3 | Elevated | Assign, reassign, or manage team membership | Write + Assign + team/queue management; no BU or role configuration |
| T-4 | Administrative Ceiling | System-level security configuration | Security role assignment, BU configuration, org-wide settings |

**Role-to-tier assignment (complete before Gap Register):**

| Role Name | Tier | Type (human / non-human / stock) | Tier Justification |
|-----------|------|----------------------------------|--------------------|

Assign every role in scope to exactly one tier. A role spanning two tiers: assign to the higher and note the downgrade recommendation. Any T-4 role beyond System Administrator or a fully documented custom admin role is an ESCALATION-PATH finding.

---

## TEMPTATION LEDGER (pre-committed -- complete before Gap Register)

| Boundary | Inertia Temptation | Rejection Criterion |
|----------|--------------------|---------------------|
| T-1 → T-2 | Assigning Create/Write to a read-only persona to avoid restricting the base role | Write is justified only when the persona has documented Create or Write job tasks |
| T-2 → T-3 | Assigning Assign/team-management to an operational role to avoid configuring queue ownership | Assign is justified only when the role must formally reassign records |
| T-3 → T-4 | Assigning System Administrator to avoid creating a custom security role | System Administrator is justified only when no lower-tier combination satisfies the documented requirement |

---

## GAP CATEGORY REGISTER (pre-committed -- complete before Stage 1)

| Category | What It Catches |
|----------|----------------|
| FLS-EXPOSURE | Sensitive field accessible without a field security profile |
| ESCALATION-PATH | Role reaches a higher tier through an available action |
| SHARING-CONFLICT | Sharing rule reopens access the OWD + tier model intends to restrict |
| TEAM-GAP | Team-scoped operation with uncontrolled or absent membership governance |
| CROSS-CASCADE | Relationship behavior grants unintended cross-entity access |
| OWD-MISMATCH | OWD broader than entity sensitivity warrants |

**Gap Findings Table -- do not populate now. Return here after Stage 3.**

| # | Category | Entity | Field (if FLS) | Role | Tier | Severity | Exact Fix |
|---|----------|--------|----------------|------|------|----------|-----------|

Severity: CRITICAL / HIGH / MEDIUM. Exact Fix: name the configuration object and expected post-fix state.

---

## STAGE 1 -- INVENTORY

**Active markers: `SCOPE-FAIL` | `VERDICT-FAIL` | `EVIDENCE-REQUIRED` | `FLS-FAIL` | `GAP-FAIL`**

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) | Tiers with any access |
|--------|-----------------|-----------------------------------|-----------------------|

For each entity: list which tiers hold any privilege. This determines which tier-boundary gates must fire in Stage 2.

**1b -- Operation-role matrix by tier (one table per entity):**

| Entity: [name] | Role | Tier | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|------|--------|------|-------|--------|--------|--------------|

Allowed values: YES / NO / CONDITIONAL (state condition). Record Scope: SCOPE LEXICON tokens only. Mark any `SCOPE-FAIL` and correct before 1c.

Tier consistency check: A T-1 role with Write = YES is a tier misclassification -- correct the tier assignment or flag the excess privilege before advancing.

**1c -- Field-level security gate (C-25: tier-stratified matrix required):**

> **Q:** Does every sensitive field on every entity in scope have a field security profile, and what is the lowest tier at which each sensitive field first becomes readable or writable?
> **A:** [verdict per entity]
> **Evidence:** I checked Security > Field Security Profiles for [entity list] -- [per-entity result] because [profile name exists / no profile / no sensitive fields; fields reviewed: list].

For each sensitive field with no FLS profile: `FLS-FAIL` fires -- add FLS-EXPOSURE row to Gap Findings Table now. Severity = CRITICAL. Tier = lowest tier with entity Read access.

Build the tier-stratified FLS matrix for each entity with sensitive fields:

| Entity | Field | Sensitivity | FLS Profile Name | T-1: R/W | T-2: R/W | T-3: R/W | T-4: R/W |
|--------|-------|-------------|-----------------|----------|----------|----------|----------|

Column values: `R` = roles at this tier may read this field. `W` = write. `R+W` = both. `-` = denied at this tier. No FLS profile applied: `OPEN` for every tier with entity Read access.

**Lowest-tier access statement (required for each sensitive field):** "Lowest tier with Read access on [field]: T-[N]. Lowest tier with Write access on [field]: T-[N]." If either value is lower than the tier at which documented operations require that access level, add an FLS-EXPOSURE finding now.

If an entity has zero sensitive fields: "Confirmed: [Entity] has no fields with sensitivity >= Medium. Fields reviewed: [list at least three field names]."

---

## STAGE 2 -- GAP ANALYSIS

**Active markers: `SCOPE-FAIL` | `VERDICT-FAIL` | `EVIDENCE-REQUIRED` | `FLS-FAIL` | `GAP-FAIL`**

**Tier-boundary gates (required for every boundary where roles span the transition):**

For each T-N → T-N+1 boundary present in the tier assignment:

> **Q:** Why does the privilege step from T-[N] to T-[N+1] represent a justified security boundary for the operations in scope?
> **A:** [JUSTIFIED / NOT-JUSTIFIED]
> **Evidence:** I checked [operations requiring T-[N+1] capabilities] -- [specific capability unavailable at T-[N]] because [why T-[N] ceiling is insufficient]. Temptation Ledger entry for this boundary: [restate named temptation]. Rejection: [how this evidence rejects the temptation].

A tier boundary traversed without this gate fires `VERDICT-FAIL`.

**Escalation gate:**

> **Q:** Can any role in the model reach a higher tier through team membership, security role assignment, ownership reassignment, or BU configuration?
> **A:** [Yes / No]
> **Evidence:** I checked [role list] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-role result] because [per-role structural reason].

Finding format: `[Role, T-N] -> [Action] -> [Tier or access gained]` -- add ESCALATION-PATH to Gap Findings Table.

**Sharing conflict gate:**

> **Q:** Do any active sharing rules reopen access the OWD + tier model intends to restrict?
> **A:** [Yes / No]
> **Evidence:** I checked sharing rules [list or "no rules found"] for [entity list] -- [per-rule result] because [comparison to OWD + tier scope].

| Rule Name | Trigger | Access Opened | Record Scope | Benefits Tier(s) | Overreach? |
|-----------|---------|---------------|--------------|-----------------|------------|

Record Scope: SCOPE LEXICON tokens only. Overreach = YES: add SHARING-CONFLICT to Gap Findings Table.

**Team membership gate:**

> **Q:** Is team membership for every team-scoped role controlled to prevent lower-tier elevation?
> **A:** [Yes / No]
> **Evidence:** I checked team [name] membership control -- [mechanism]; self-addition is [possible / not possible] because [specific constraint].

**OWD sensitivity gate:**

> **Q:** Is the OWD for each high-sensitivity entity more permissive than the data warrants?
> **A:** [verdict per high-sensitivity entity]
> **Evidence:** I checked OWD for [entity] -- [OWD token] -- [justified / unjustified] because [FLS compensates / no compensating control].

**Cross-entity cascade gate:**

> **Q:** What is the lowest-tier path to the highest-sensitivity entity, and is each hop intentional?
> **A:** [trace through at least two hops]
> **Evidence:** I traced [Role, T-N] -> [Entity A, Record Scope: token] -> [Relationship type, cascade setting] -> [Entity B, Record Scope: token] -- hop 1 [intentional / emergent because reason]; hop 2 [intentional / emergent because reason].

All Record Scope tokens: SCOPE LEXICON only.

---

## STAGE 3 -- ROLE ASSESSMENT AND REMEDIATION

**Active markers: `SCOPE-FAIL` | `VERDICT-FAIL` | `EVIDENCE-REQUIRED` | `FLS-FAIL` | `GAP-FAIL`**

**Customer Service Representative gate:**

> **Q:** Does the Customer Service Representative access any sensitive field or operation beyond what the CS job function requires, and which tier does it occupy?
> **A:** [verdict and tier]
> **Evidence:** I checked CS access for [entity list, sensitive field list from the tier-stratified FLS matrix in 1c] -- [per-item result] because [FLS profile / OWD / role scope]. CS belongs in T-[N] because [matching tier definition].

**Dataverse Security Expert gate:**

> **Q:** Does the Dataverse Security Expert hold privileges beyond least-privilege for a security configuration task, and which tier does it occupy?
> **A:** [verdict and tier]
> **Evidence:** I checked expert privileges beyond CS access -- [excess list or NONE] because [comparison against security configuration task scope]. Expert belongs in T-[N] because [matching tier definition].

Both roles must appear by name with distinct specific observations and explicit tier assignments. A merged summary fires `VERDICT-FAIL`.

**Least-privilege scoring:**

| Role | Tier | Persona | Excess Privileges | LP Score (0-10) | Over-Privileged? | Reduction Required |
|------|------|---------|-------------------|-----------------|------------------|--------------------|

LP Score < 7: state the specific privilege to reduce, the target scope, and whether the role should drop a tier.

**T-4 binary gate (required if any T-4 role exists):**

> **Q:** Is the assignment of a T-4 (Administrative Ceiling) role JUSTIFIED or NOT-JUSTIFIED for the operations in scope?
> **A:** [JUSTIFIED / NOT-JUSTIFIED]
> **Evidence:** I checked T-4 role's required operations -- [operation list] -- [each requires T-4 because / no operation requires T-4]. Temptation Ledger T-3→T-4 entry: [restate named temptation]. Rejection: [how this evidence rejects or confirms the temptation].

Binary verdict required. `VERDICT-FAIL` fires for any non-binary conclusion.

**Attack scenario (if ESCALATION-PATH found):**
`Starting role (T-N) -> Action sequence -> Tier or access gained`. Abstract risk statements do not satisfy this section.

**Remediation gate:**

> **Q:** Does every entry in the Gap Findings Table have a specific Exact Fix naming the configuration object and post-fix state?
> **A:** [Yes -- verified / No -- complete now]
> **Evidence:** Every Exact Fix row names [field security profile / sharing rule / security role privilege / OWD setting], current state, and target state.

Return to the Gap Findings Table and fill it in completely. Every row must fit a pre-declared category. Every Exact Fix must name the specific configuration object.

---

## V-02 -- Lifecycle Emphasis: Gate-Absence Named Markers

**Axis:** Lifecycle emphasis -- each mandatory gate in the trace has a dedicated named absence marker that fires when the gate section is structurally absent, not merely when its content is incorrect
**Hypothesis:** C-26 requires a named marker for gate-absence. The existing enforcement system (C-15/C-17) has content-violation markers that fire when a gate produces incorrect content. The gap is structural: a gate skipped entirely produces no content, and therefore no content-violation marker fires -- the omission is silent. Adding per-gate absence markers (`FLS-GATE-ABSENT`, `TIER-GATE-ABSENT`, `ESCALATION-GATE-ABSENT`, `BINARY-GATE-ABSENT`) creates a distinct named signal for structural omission. The writer cannot claim no gate violation occurred when the gate section is simply absent from the output.

---

You are running a permissions trace signal for: {{topic}}

---

## ENFORCEMENT SYSTEM (complete before any entity name, operation, or content)

Two classes of markers are active for this trace. Both classes must be re-declared at the start of each stage.

### Content-Violation Markers

| Marker | Domain | Trigger Condition | Correction Required |
|--------|--------|-------------------|---------------------|
| `SCOPE-FAIL` | Record Access | Record Scope cell contains prose rather than a SCOPE LEXICON token | Replace with exact token before advancing |
| `VERDICT-FAIL` | Verdict | Gate answer omits a binary verdict or conclusion is ambiguous | Restate with declared binary verdict before advancing |
| `EVIDENCE-REQUIRED` | Evidence | Gate answer lacks an Evidence line ("I checked [X] -- [result] because [Y]") | Add three-part Evidence line before advancing |
| `FLS-FAIL` | Field Security | Sensitive field in FLS matrix without a field security profile | Add FLS-EXPOSURE to Gap Findings Table immediately |
| `GAP-FAIL` | Gap / Conflict | Gap category investigated without explicit finding or rule-out | State finding or rule-out with evidence before advancing |

### Gate-Absence Markers

A gate-absence marker fires when a mandatory gate section does not appear in the output at the point where it is required. A section heading with no content does not escape the marker -- the gate must be answered, not merely headed.

| Marker | Gate It Guards | When It Fires | Recovery Required |
|--------|----------------|---------------|-------------------|
| `FLS-GATE-ABSENT` | Stage 1 § 1c FLS gate | 1c section (Evidence gate + tier-stratified table) is missing before Stage 2 begins | Insert the complete 1c FLS gate section before advancing to Stage 2 |
| `TIER-GATE-ABSENT` | Stage 2 per-boundary tier gate | Any T-N→T-N+1 boundary in the tier assignment has no corresponding gate section in Stage 2 | Insert the missing boundary gate with Evidence-template answer before advancing |
| `ESCALATION-GATE-ABSENT` | Stage 2 escalation gate | Escalation gate section missing from Stage 2 | Insert the complete escalation gate before Stage 3 |
| `BINARY-GATE-ABSENT` | Stage 3 T-4 binary gate | A T-4 role exists in the tier assignment but no binary justified/not-justified gate section appears in Stage 3 | Insert the T-4 binary gate with Evidence-template answer before the remediation gate |

**Section-open rule:** At the start of Stage 1, Stage 2, and Stage 3, re-declare both content-violation and gate-absence markers by name.

---

## SCOPE LEXICON (locked)

`Org` / `BU` / `Parent-Child BU` / `Team:[name]` / `User` / `Sharing:[rule name]`

---

## PRIVILEGE TIER LADDER (complete before Gap Register)

| Tier | Label | Privilege Boundary | Signature Capabilities |
|------|-------|-------------------|------------------------|
| T-1 | Read-Only Floor | Read within scope | Read only |
| T-2 | Operational | Create + write within scope | Create + Read + Write |
| T-3 | Elevated | Assign + team management | Write + Assign + team/queue management |
| T-4 | Administrative Ceiling | System-level security configuration | Security role assignment, BU configuration |

**Role-to-tier assignment:**

| Role Name | Tier | Type | Tier Justification |
|-----------|------|------|--------------------|

---

## TEMPTATION LEDGER (pre-committed)

| Boundary | Inertia Temptation | Rejection Criterion |
|----------|--------------------|---------------------|
| T-1 → T-2 | Assigning Create/Write to a read-only persona to avoid restricting the base role | Write justified only when persona has documented Create/Write job tasks |
| T-2 → T-3 | Assigning Assign/team-management to avoid configuring queue ownership separately | Assign justified only when role must formally reassign records |
| T-3 → T-4 | Assigning System Administrator to avoid creating a custom security role | System Administrator justified only when no lower-tier combination satisfies the documented requirement |

---

## GAP CATEGORY REGISTER (pre-committed)

| Category | What It Catches |
|----------|----------------|
| FLS-EXPOSURE | Sensitive field without a field security profile |
| ESCALATION-PATH | Role reaches higher tier through an available action |
| SHARING-CONFLICT | Sharing rule reopens access the tier model intends to restrict |
| TEAM-GAP | Team-scoped operation with uncontrolled membership |
| CROSS-CASCADE | Relationship behavior grants unintended cross-entity access |
| OWD-MISMATCH | OWD broader than entity sensitivity warrants |

**Gap Findings Table -- do not populate now. Return after Stage 3.**

| # | Category | Entity | Field (if FLS) | Role | Tier | Severity | Exact Fix |
|---|----------|--------|----------------|------|------|----------|-----------|

---

## STAGE 1 -- INVENTORY

**Active content-violation markers: `SCOPE-FAIL` | `VERDICT-FAIL` | `EVIDENCE-REQUIRED` | `FLS-FAIL` | `GAP-FAIL`**
**Active gate-absence markers: `FLS-GATE-ABSENT`**

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) | Tiers with any access |
|--------|-----------------|-----------------------------------|-----------------------|

**1b -- Operation-role matrix by tier:**

| Entity: [name] | Role | Tier | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|------|--------|------|-------|--------|--------|--------------|

Record Scope: SCOPE LEXICON tokens only. Mark `SCOPE-FAIL`, correct before 1c.
Tier consistency: T-1 role with Write = YES is a misclassification -- correct before advancing.

**1c -- Field-level security gate** *(absent before Stage 2: `FLS-GATE-ABSENT` fires)*

> **Q:** Does every sensitive field on every entity have a field security profile, and what is the lowest tier at which each sensitive field becomes readable or writable?
> **A:** [verdict per entity]
> **Evidence:** I checked Security > Field Security Profiles for [entity list] -- [per-entity result] because [profile name / no profile / no sensitive fields; fields reviewed: list].

`FLS-FAIL` fires for each sensitive field with no profile -- add FLS-EXPOSURE to Gap Findings Table. Severity = CRITICAL.

| Entity | Field | Sensitivity | FLS Profile Name | T-1: R/W | T-2: R/W | T-3: R/W | T-4: R/W |
|--------|-------|-------------|-----------------|----------|----------|----------|----------|

Column values: `R` = read. `W` = write. `R+W` = both. `-` = denied. No profile: `OPEN`.
Lowest-tier access: "Lowest tier with Read on [field]: T-[N]. Lowest tier with Write on [field]: T-[N]."

---

## STAGE 2 -- GAP ANALYSIS

**Active content-violation markers: `SCOPE-FAIL` | `VERDICT-FAIL` | `EVIDENCE-REQUIRED` | `FLS-FAIL` | `GAP-FAIL`**
**Active gate-absence markers: `TIER-GATE-ABSENT` | `ESCALATION-GATE-ABSENT`**

**Tier-boundary gates** *(absent boundary gate: `TIER-GATE-ABSENT` fires for that boundary)*

For each T-N→T-N+1 boundary:

> **Q:** Why does the privilege step from T-[N] to T-[N+1] represent a justified security boundary?
> **A:** [JUSTIFIED / NOT-JUSTIFIED]
> **Evidence:** I checked [operations requiring T-[N+1] capabilities] -- [specific T-[N] limitation] because [reason]. Temptation Ledger entry: [restate named temptation]. Rejection: [how evidence rejects it].

**Escalation gate** *(absent: `ESCALATION-GATE-ABSENT` fires)*

> **Q:** Can any role reach a higher tier through team membership, security role assignment, ownership reassignment, or BU configuration?
> **A:** [Yes / No]
> **Evidence:** I checked [role list] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-role result] because [per-role structural reason].

**Sharing conflict gate:**

> **Q:** Do any active sharing rules reopen access the OWD + tier model intends to restrict?
> **A:** [Yes / No]
> **Evidence:** I checked sharing rules [list or "no rules"] for [entity list] -- [per-rule result].

| Rule Name | Trigger | Access Opened | Record Scope | Overreach? |
|-----------|---------|---------------|--------------|------------|

**Team membership gate:**

> **Q:** Is team membership controlled to prevent lower-tier elevation?
> **A:** [Yes / No]
> **Evidence:** I checked team [name] -- [mechanism]; self-addition [possible / not possible] because [constraint].

**OWD sensitivity gate:**

> **Q:** Is the OWD for each high-sensitivity entity more permissive than the data warrants?
> **A:** [verdict per entity]
> **Evidence:** I checked OWD for [entity] -- [token] -- [justified / unjustified] because [FLS compensates / no control].

**Cross-entity cascade gate:**

> **Q:** What is the lowest-tier path to the highest-sensitivity entity?
> **A:** [trace through at least two hops]
> **Evidence:** I traced [Role, T-N] -> [Entity A, Record Scope: token] -> [Relationship, cascade] -> [Entity B, Record Scope: token] -- hop 1 [intentional / emergent]; hop 2 [intentional / emergent].

---

## STAGE 3 -- ROLE ASSESSMENT AND REMEDIATION

**Active content-violation markers: `SCOPE-FAIL` | `VERDICT-FAIL` | `EVIDENCE-REQUIRED` | `FLS-FAIL` | `GAP-FAIL`**
**Active gate-absence markers: `BINARY-GATE-ABSENT`**

**Customer Service Representative gate:**

> **Q:** Does the Customer Service Representative access any sensitive field or operation beyond what the CS job function requires?
> **A:** [verdict and tier]
> **Evidence:** I checked CS access for [entity list, sensitive fields] -- [per-item result] because [FLS / OWD / role scope].

**Dataverse Security Expert gate:**

> **Q:** Does the Dataverse Security Expert hold privileges beyond least-privilege for a security configuration task?
> **A:** [verdict and tier]
> **Evidence:** I checked expert privileges beyond CS access -- [excess or NONE] because [comparison against task scope].

Both roles: distinct specific observations required. Merged summary fires `VERDICT-FAIL`.

**Least-privilege scoring:**

| Role | Tier | Persona | Excess Privileges | LP Score (0-10) | Over-Privileged? | Reduction Required |
|------|------|---------|-------------------|-----------------|------------------|--------------------|

**T-4 binary gate** *(absent: `BINARY-GATE-ABSENT` fires)*

> **Q:** Is the assignment of a T-4 (Administrative Ceiling) role JUSTIFIED or NOT-JUSTIFIED?
> **A:** [JUSTIFIED / NOT-JUSTIFIED]
> **Evidence:** I checked T-4 role's required operations -- [operation list] -- [each requires T-4 because / no operation requires T-4]. Temptation Ledger T-3→T-4: [restate named temptation]. Rejection: [how evidence rejects or confirms it].

Binary verdict required. `VERDICT-FAIL` fires for any non-binary conclusion. Absent gate: `BINARY-GATE-ABSENT` fires.

**Attack scenario (if ESCALATION-PATH found):**
`Starting role (T-N) -> Action sequence -> Tier or access gained`.

**Remediation gate:**

> **Q:** Does every Gap Findings Table entry have a specific Exact Fix naming the configuration object and post-fix state?
> **A:** [Yes -- verified / No -- complete now]
> **Evidence:** Every Exact Fix names the object, current state, and target state.

Return to the Gap Findings Table and fill it in completely.

---

## V-03 -- Phrasing Register: Binary Gate Anti-Hedging Exclusion

**Axis:** Phrasing register -- every binary verdict gate definition names at least one excluded phrase; the definition explicitly states which language does not satisfy the gate before any output is produced
**Hypothesis:** C-24 already requires a binary JUSTIFIED/NOT-JUSTIFIED gate for T-4, but the gate definition does not name excluded language. Without named exclusions, "probably justified," "likely warranted," or "appears appropriate" can satisfy the surface form of a binary gate -- each gestures toward one option without committing. Adding explicit named exclusions at definition time closes this gap before any output is written: the writer cannot claim compliance with the gate when the definition explicitly identifies their chosen phrase as disqualifying. The exclusion operates at definition time, not review time -- a scorer can cite the gate definition itself as the authority for rejection.

---

You are running a permissions trace signal for: {{topic}}

---

## ENFORCEMENT SYSTEM (complete before any entity name, operation, or content)

| Marker | Domain | Trigger Condition | Correction Required |
|--------|--------|-------------------|---------------------|
| `SCOPE-FAIL` | Record Access | Record Scope cell contains prose rather than a SCOPE LEXICON token | Replace with exact token before advancing |
| `VERDICT-FAIL` | Verdict | Gate answer omits a binary verdict, or uses language named in a gate's anti-hedging exclusion list | Restate with a declared permitted verdict before advancing |
| `EVIDENCE-REQUIRED` | Evidence | Gate answer lacks an Evidence line ("I checked [X] -- [result] because [Y]") | Add three-part Evidence line before advancing |
| `FLS-FAIL` | Field Security | Sensitive field in FLS matrix without a field security profile | Add FLS-EXPOSURE to Gap Findings Table immediately |
| `GAP-FAIL` | Gap / Conflict | Gap category investigated without finding or rule-out | State finding or rule-out with evidence before advancing |

**Section-open rule:** Re-declare active markers at the start of Stage 1, Stage 2, and Stage 3.

---

## BINARY VERDICT GATE DEFINITIONS (read before Stage 2 and Stage 3 -- locked)

Permitted and excluded language are declared here before any gate is answered. A gate answer using excluded language fires `VERDICT-FAIL` even if the surface form resembles a binary answer.

**Tier-boundary binary gate (applies at T-2→T-3 and T-3→T-4):**
- Permitted verdicts: `JUSTIFIED` or `NOT-JUSTIFIED`
- **Excluded language (does not satisfy this gate):** "probably justified," "likely warranted," "appears appropriate," "seems reasonable," "generally acceptable," "may be justified," "could be necessary"
- A verdict using any excluded phrase fires `VERDICT-FAIL` and must be restated with a permitted verdict.

**T-4 binary gate (applies to every T-4 role in Stage 3):**
- Permitted verdicts: `JUSTIFIED` or `NOT-JUSTIFIED`
- **Excluded language (does not satisfy this gate):** "probably justified," "likely warranted," "appears appropriate," "might be necessary," "arguably required," "probably not required," "seems to be needed," "appears to be the right level," "probably makes sense"
- Only `JUSTIFIED` or `NOT-JUSTIFIED` satisfies this gate. Any excluded phrase fires `VERDICT-FAIL`.

---

## SCOPE LEXICON (locked)

`Org` / `BU` / `Parent-Child BU` / `Team:[name]` / `User` / `Sharing:[rule name]`

---

## PRIVILEGE TIER LADDER (complete before Gap Register)

| Tier | Label | Privilege Boundary | Signature Capabilities |
|------|-------|-------------------|------------------------|
| T-1 | Read-Only Floor | Read within scope | Read only |
| T-2 | Operational | Create + write within scope | Create + Read + Write |
| T-3 | Elevated | Assign + team management | Write + Assign + team/queue management |
| T-4 | Administrative Ceiling | System-level security configuration | Security role assignment, BU configuration |

**Role-to-tier assignment:**

| Role Name | Tier | Type | Tier Justification |
|-----------|------|------|--------------------|

---

## TEMPTATION LEDGER (pre-committed)

| Boundary | Inertia Temptation | Rejection Criterion |
|----------|--------------------|---------------------|
| T-1 → T-2 | Assigning Create/Write to a read-only persona to avoid restricting the base role | Write justified only when persona has documented Create/Write job tasks |
| T-2 → T-3 | Assigning Assign/team-management to avoid configuring queue ownership separately | Assign justified only when role must formally reassign records |
| T-3 → T-4 | Assigning System Administrator to avoid creating a custom security role | System Administrator justified only when no lower-tier combination satisfies the documented requirement |

---

## GAP CATEGORY REGISTER (pre-committed)

| Category | What It Catches |
|----------|----------------|
| FLS-EXPOSURE | Sensitive field without a field security profile |
| ESCALATION-PATH | Role reaches higher tier through an available action |
| SHARING-CONFLICT | Sharing rule reopens access the tier model intends to restrict |
| TEAM-GAP | Team-scoped operation with uncontrolled membership |
| CROSS-CASCADE | Relationship behavior grants unintended cross-entity access |
| OWD-MISMATCH | OWD broader than entity sensitivity warrants |

**Gap Findings Table -- do not populate now. Return after Stage 3.**

| # | Category | Entity | Field (if FLS) | Role | Tier | Severity | Exact Fix |
|---|----------|--------|----------------|------|------|----------|-----------|

---

## STAGE 1 -- INVENTORY

**Active markers: `SCOPE-FAIL` | `VERDICT-FAIL` | `EVIDENCE-REQUIRED` | `FLS-FAIL` | `GAP-FAIL`**

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) | Tiers with any access |
|--------|-----------------|-----------------------------------|-----------------------|

**1b -- Operation-role matrix by tier:**

| Entity: [name] | Role | Tier | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|------|--------|------|-------|--------|--------|--------------|

Record Scope: SCOPE LEXICON tokens only. Mark `SCOPE-FAIL`, correct before 1c.
Tier consistency: T-1 role with Write = YES is a misclassification -- correct before advancing.

**1c -- Field-level security gate:**

> **Q:** Does every sensitive field on every entity have a field security profile, and what is the lowest tier at which each sensitive field becomes readable or writable?
> **A:** [verdict per entity]
> **Evidence:** I checked Security > Field Security Profiles for [entity list] -- [per-entity result] because [profile name / no profile / no sensitive fields; fields reviewed: list].

`FLS-FAIL` fires for each sensitive field with no profile -- add FLS-EXPOSURE to Gap Findings Table. Severity = CRITICAL.

| Entity | Field | Sensitivity | FLS Profile Name | T-1: R/W | T-2: R/W | T-3: R/W | T-4: R/W |
|--------|-------|-------------|-----------------|----------|----------|----------|----------|

Column values: `R` = read. `W` = write. `R+W` = both. `-` = denied. No profile: `OPEN`.
Lowest-tier access: "Lowest tier with Read on [field]: T-[N]. Lowest tier with Write on [field]: T-[N]."

---

## STAGE 2 -- GAP ANALYSIS

**Active markers: `SCOPE-FAIL` | `VERDICT-FAIL` | `EVIDENCE-REQUIRED` | `FLS-FAIL` | `GAP-FAIL`**

**Tier-boundary gates (refer to Binary Verdict Gate Definitions above -- excluded language fires `VERDICT-FAIL`):**

For each T-N→T-N+1 boundary:

> **Q:** Is the privilege step from T-[N] to T-[N+1] JUSTIFIED or NOT-JUSTIFIED?
> **A:** [JUSTIFIED / NOT-JUSTIFIED -- permitted verdicts only; excluded language fires `VERDICT-FAIL`]
> **Evidence:** I checked [operations requiring T-[N+1] capabilities] -- [specific T-[N] limitation] because [reason]. Temptation Ledger entry: [restate named temptation]. Rejection: [how evidence rejects it].

**Escalation gate:**

> **Q:** Can any role reach a higher tier through team membership, security role assignment, ownership reassignment, or BU configuration?
> **A:** [Yes / No]
> **Evidence:** I checked [role list] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-role result] because [per-role structural reason].

**Sharing conflict gate:**

> **Q:** Do any active sharing rules reopen access the OWD + tier model intends to restrict?
> **A:** [Yes / No]
> **Evidence:** I checked sharing rules [list or "no rules"] for [entity list] -- [per-rule result].

| Rule Name | Trigger | Access Opened | Record Scope | Overreach? |
|-----------|---------|---------------|--------------|------------|

**Team membership gate:**

> **Q:** Is team membership controlled to prevent lower-tier elevation?
> **A:** [Yes / No]
> **Evidence:** I checked team [name] -- [mechanism]; self-addition [possible / not possible] because [constraint].

**OWD sensitivity gate:**

> **Q:** Is the OWD for each high-sensitivity entity more permissive than the data warrants?
> **A:** [verdict per entity]
> **Evidence:** I checked OWD for [entity] -- [token] -- [justified / unjustified] because [FLS compensates / no control].

**Cross-entity cascade gate:**

> **Q:** What is the lowest-tier path to the highest-sensitivity entity?
> **A:** [trace through at least two hops]
> **Evidence:** I traced [Role, T-N] -> [Entity A, Record Scope: token] -> [Relationship, cascade] -> [Entity B, Record Scope: token] -- hop 1 [intentional / emergent]; hop 2 [intentional / emergent].

---

## STAGE 3 -- ROLE ASSESSMENT AND REMEDIATION

**Active markers: `SCOPE-FAIL` | `VERDICT-FAIL` | `EVIDENCE-REQUIRED` | `FLS-FAIL` | `GAP-FAIL`**

**Customer Service Representative gate:**

> **Q:** Does the Customer Service Representative access any sensitive field or operation beyond what the CS job function requires?
> **A:** [verdict and tier]
> **Evidence:** I checked CS access for [entity list, sensitive fields] -- [per-item result] because [FLS / OWD / role scope].

**Dataverse Security Expert gate:**

> **Q:** Does the Dataverse Security Expert hold privileges beyond least-privilege for a security configuration task?
> **A:** [verdict and tier]
> **Evidence:** I checked expert privileges beyond CS access -- [excess or NONE] because [comparison against task scope].

Both roles: distinct specific observations required. Merged summary fires `VERDICT-FAIL`.

**Least-privilege scoring:**

| Role | Tier | Persona | Excess Privileges | LP Score (0-10) | Over-Privileged? | Reduction Required |
|------|------|---------|-------------------|-----------------|------------------|--------------------|

**T-4 binary gate (refer to Binary Verdict Gate Definitions above):**

> **Q:** Is the assignment of a T-4 (Administrative Ceiling) role JUSTIFIED or NOT-JUSTIFIED?
> **A:** [JUSTIFIED / NOT-JUSTIFIED -- permitted verdicts only; see Binary Verdict Gate Definitions]
> **Evidence:** I checked T-4 role's required operations -- [operation list] -- [each requires T-4 because / no operation requires T-4]. Temptation Ledger T-3→T-4: [restate named temptation]. Rejection: [how evidence rejects or confirms it].

A verdict using excluded language (e.g., "probably justified," "likely warranted," "appears appropriate") fires `VERDICT-FAIL`. Only `JUSTIFIED` or `NOT-JUSTIFIED` satisfies this gate.

**Attack scenario (if ESCALATION-PATH found):**
`Starting role (T-N) -> Action sequence -> Tier or access gained`.

**Remediation gate:**

> **Q:** Does every Gap Findings Table entry have a specific Exact Fix naming the configuration object and post-fix state?
> **A:** [Yes -- verified / No -- complete now]
> **Evidence:** Every Exact Fix names the object, current state, and target state.

Return to the Gap Findings Table and fill it in completely.

---

## V-04 -- Combined: Gate-Absence Markers (C-26) + Anti-Hedging Exclusion (C-27)

**Axis:** Lifecycle emphasis + phrasing register -- gate-absence named markers and binary gate anti-hedging exclusions applied together
**Hypothesis:** C-26 and C-27 target the T-4 binary gate from two failure directions: C-26 ensures the gate cannot be silently omitted (gate-absence fires a named marker); C-27 ensures that when present, the gate cannot be satisfied by hedging language (anti-hedging exclusion disqualifies at definition time). A trace that satisfies C-26 alone can still produce "probably justified" as its T-4 verdict; one that satisfies C-27 alone can still skip the gate entirely. Wiring both means the gate must be present and its verdict must be from the permitted set -- neither omission nor evasion is available.

---

You are running a permissions trace signal for: {{topic}}

---

## ENFORCEMENT SYSTEM (complete before any entity name, operation, or content)

### Content-Violation Markers

| Marker | Domain | Trigger Condition | Correction Required |
|--------|--------|-------------------|---------------------|
| `SCOPE-FAIL` | Record Access | Record Scope cell contains prose rather than a SCOPE LEXICON token | Replace with exact token before advancing |
| `VERDICT-FAIL` | Verdict | Gate answer omits a binary verdict, or uses language named in a gate's excluded list | Restate with a permitted binary verdict before advancing |
| `EVIDENCE-REQUIRED` | Evidence | Gate answer lacks an Evidence line ("I checked [X] -- [result] because [Y]") | Add three-part Evidence line before advancing |
| `FLS-FAIL` | Field Security | Sensitive field in FLS matrix without a field security profile | Add FLS-EXPOSURE to Gap Findings Table immediately |
| `GAP-FAIL` | Gap / Conflict | Gap category investigated without finding or rule-out | State finding or rule-out with evidence before advancing |

### Gate-Absence Markers

| Marker | Gate It Guards | When It Fires | Recovery Required |
|--------|----------------|---------------|-------------------|
| `FLS-GATE-ABSENT` | Stage 1 § 1c | 1c section missing before Stage 2 begins | Insert complete FLS gate + tier-stratified matrix |
| `TIER-GATE-ABSENT` | Stage 2 tier-boundary gate | Any T-N→T-N+1 boundary has no gate section | Insert missing boundary gate with Evidence-template answer |
| `ESCALATION-GATE-ABSENT` | Stage 2 escalation gate | Escalation gate section missing from Stage 2 | Insert complete escalation gate before Stage 3 |
| `BINARY-GATE-ABSENT` | Stage 3 T-4 binary gate | T-4 role exists but no binary gate section in Stage 3 | Insert T-4 binary gate with Evidence-template answer |

**Section-open rule:** Re-declare both marker classes at the start of Stage 1, Stage 2, and Stage 3.

---

## BINARY VERDICT GATE DEFINITIONS (locked -- applies at every binary gate in Stages 2 and 3)

**Tier-boundary binary gate (T-2→T-3 and T-3→T-4):**
- Permitted verdicts: `JUSTIFIED` or `NOT-JUSTIFIED`
- **Excluded language:** "probably justified," "likely warranted," "appears appropriate," "seems reasonable," "generally acceptable," "may be justified," "could be necessary"
- A verdict using any excluded phrase fires `VERDICT-FAIL`.

**T-4 binary gate:**
- Permitted verdicts: `JUSTIFIED` or `NOT-JUSTIFIED`
- **Excluded language:** "probably justified," "likely warranted," "appears appropriate," "might be necessary," "arguably required," "probably not required," "seems to be needed," "appears to be the right level," "probably makes sense"
- Only `JUSTIFIED` or `NOT-JUSTIFIED` satisfies this gate.

---

## SCOPE LEXICON (locked)

`Org` / `BU` / `Parent-Child BU` / `Team:[name]` / `User` / `Sharing:[rule name]`

---

## PRIVILEGE TIER LADDER

| Tier | Label | Privilege Boundary | Signature Capabilities |
|------|-------|-------------------|------------------------|
| T-1 | Read-Only Floor | Read within scope | Read only |
| T-2 | Operational | Create + write within scope | Create + Read + Write |
| T-3 | Elevated | Assign + team management | Write + Assign + team/queue management |
| T-4 | Administrative Ceiling | System-level security configuration | Security role assignment, BU configuration |

**Role-to-tier assignment:**

| Role Name | Tier | Type | Tier Justification |
|-----------|------|------|--------------------|

---

## TEMPTATION LEDGER (pre-committed)

| Boundary | Inertia Temptation | Rejection Criterion |
|----------|--------------------|---------------------|
| T-1 → T-2 | Assigning Create/Write to a read-only persona to avoid restricting the base role | Write justified only when persona has documented Create/Write job tasks |
| T-2 → T-3 | Assigning Assign/team-management to avoid configuring queue ownership separately | Assign justified only when role must formally reassign records |
| T-3 → T-4 | Assigning System Administrator to avoid creating a custom security role | System Administrator justified only when no lower-tier combination satisfies the documented requirement |

---

## GAP CATEGORY REGISTER (pre-committed)

| Category | What It Catches |
|----------|----------------|
| FLS-EXPOSURE | Sensitive field without a field security profile |
| ESCALATION-PATH | Role reaches higher tier through an available action |
| SHARING-CONFLICT | Sharing rule reopens access the tier model intends to restrict |
| TEAM-GAP | Team-scoped operation with uncontrolled membership |
| CROSS-CASCADE | Relationship behavior grants unintended cross-entity access |
| OWD-MISMATCH | OWD broader than entity sensitivity warrants |

**Gap Findings Table -- do not populate now. Return after Stage 3.**

| # | Category | Entity | Field (if FLS) | Role | Tier | Severity | Exact Fix |
|---|----------|--------|----------------|------|------|----------|-----------|

---

## STAGE 1 -- INVENTORY

**Active content-violation markers: `SCOPE-FAIL` | `VERDICT-FAIL` | `EVIDENCE-REQUIRED` | `FLS-FAIL` | `GAP-FAIL`**
**Active gate-absence markers: `FLS-GATE-ABSENT`**

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) | Tiers with any access |
|--------|-----------------|-----------------------------------|-----------------------|

**1b -- Operation-role matrix by tier:**

| Entity: [name] | Role | Tier | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|------|--------|------|-------|--------|--------|--------------|

Record Scope: SCOPE LEXICON tokens only. Mark `SCOPE-FAIL`, correct before 1c.
Tier consistency: T-1 role with Write = YES is a misclassification -- correct before advancing.

**1c -- Field-level security gate** *(absent before Stage 2: `FLS-GATE-ABSENT` fires)*

> **Q:** Does every sensitive field on every entity have a field security profile, and what is the lowest tier at which each sensitive field becomes readable or writable?
> **A:** [verdict per entity]
> **Evidence:** I checked Security > Field Security Profiles for [entity list] -- [per-entity result] because [profile name / no profile / no sensitive fields; fields reviewed: list].

`FLS-FAIL` fires for each sensitive field with no profile -- add FLS-EXPOSURE to Gap Findings Table. Severity = CRITICAL.

| Entity | Field | Sensitivity | FLS Profile Name | T-1: R/W | T-2: R/W | T-3: R/W | T-4: R/W |
|--------|-------|-------------|-----------------|----------|----------|----------|----------|

Column values: `R` = read. `W` = write. `R+W` = both. `-` = denied. No profile: `OPEN`.
Lowest-tier access: "Lowest tier with Read on [field]: T-[N]. Lowest tier with Write on [field]: T-[N]."

---

## STAGE 2 -- GAP ANALYSIS

**Active content-violation markers: `SCOPE-FAIL` | `VERDICT-FAIL` | `EVIDENCE-REQUIRED` | `FLS-FAIL` | `GAP-FAIL`**
**Active gate-absence markers: `TIER-GATE-ABSENT` | `ESCALATION-GATE-ABSENT`**

**Tier-boundary gates** *(absent gate: `TIER-GATE-ABSENT` fires; present gate with excluded verdict: `VERDICT-FAIL` fires)*

For each T-N→T-N+1 boundary:

> **Q:** Is the privilege step from T-[N] to T-[N+1] JUSTIFIED or NOT-JUSTIFIED?
> **A:** [JUSTIFIED / NOT-JUSTIFIED -- see Binary Verdict Gate Definitions; excluded language fires `VERDICT-FAIL`]
> **Evidence:** I checked [operations requiring T-[N+1] capabilities] -- [specific T-[N] limitation] because [reason]. Temptation Ledger entry: [restate named temptation]. Rejection: [how evidence rejects it].

**Escalation gate** *(absent: `ESCALATION-GATE-ABSENT` fires)*

> **Q:** Can any role reach a higher tier through team membership, security role assignment, ownership reassignment, or BU configuration?
> **A:** [Yes / No]
> **Evidence:** I checked [role list] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-role result] because [per-role structural reason].

**Sharing conflict gate:**

> **Q:** Do any active sharing rules reopen access the OWD + tier model intends to restrict?
> **A:** [Yes / No]
> **Evidence:** I checked sharing rules [list or "no rules"] for [entity list] -- [per-rule result].

| Rule Name | Trigger | Access Opened | Record Scope | Overreach? |
|-----------|---------|---------------|--------------|------------|

**Team membership gate:**

> **Q:** Is team membership controlled to prevent lower-tier elevation?
> **A:** [Yes / No]
> **Evidence:** I checked team [name] -- [mechanism]; self-addition [possible / not possible] because [constraint].

**OWD sensitivity gate:**

> **Q:** Is the OWD for each high-sensitivity entity more permissive than the data warrants?
> **A:** [verdict per entity]
> **Evidence:** I checked OWD for [entity] -- [token] -- [justified / unjustified] because [FLS compensates / no control].

**Cross-entity cascade gate:**

> **Q:** What is the lowest-tier path to the highest-sensitivity entity?
> **A:** [trace through at least two hops]
> **Evidence:** I traced [Role, T-N] -> [Entity A, Record Scope: token] -> [Relationship, cascade] -> [Entity B, Record Scope: token] -- hop 1 [intentional / emergent]; hop 2 [intentional / emergent].

---

## STAGE 3 -- ROLE ASSESSMENT AND REMEDIATION

**Active content-violation markers: `SCOPE-FAIL` | `VERDICT-FAIL` | `EVIDENCE-REQUIRED` | `FLS-FAIL` | `GAP-FAIL`**
**Active gate-absence markers: `BINARY-GATE-ABSENT`**

**Customer Service Representative gate:**

> **Q:** Does the Customer Service Representative access any sensitive field or operation beyond what the CS job function requires?
> **A:** [verdict and tier]
> **Evidence:** I checked CS access for [entity list, sensitive fields] -- [per-item result] because [FLS / OWD / role scope].

**Dataverse Security Expert gate:**

> **Q:** Does the Dataverse Security Expert hold privileges beyond least-privilege for a security configuration task?
> **A:** [verdict and tier]
> **Evidence:** I checked expert privileges beyond CS access -- [excess or NONE] because [comparison against task scope].

Both roles: distinct specific observations required. Merged summary fires `VERDICT-FAIL`.

**Least-privilege scoring:**

| Role | Tier | Persona | Excess Privileges | LP Score (0-10) | Over-Privileged? | Reduction Required |
|------|------|---------|-------------------|-----------------|------------------|--------------------|

**T-4 binary gate** *(absent: `BINARY-GATE-ABSENT` fires; excluded verdict: `VERDICT-FAIL` fires)*

> **Q:** Is the assignment of a T-4 (Administrative Ceiling) role JUSTIFIED or NOT-JUSTIFIED?
> **A:** [JUSTIFIED / NOT-JUSTIFIED -- see Binary Verdict Gate Definitions; excluded language fires `VERDICT-FAIL`]
> **Evidence:** I checked T-4 role's required operations -- [operation list] -- [each requires T-4 because / no operation requires T-4]. Temptation Ledger T-3→T-4: [restate named temptation]. Rejection: [how evidence rejects or confirms it].

Excluded language at this gate includes "probably justified," "likely warranted," "appears appropriate," "might be necessary," "arguably required." None satisfies this gate. Only `JUSTIFIED` or `NOT-JUSTIFIED` does.

**Attack scenario (if ESCALATION-PATH found):**
`Starting role (T-N) -> Action sequence -> Tier or access gained`.

**Remediation gate:**

> **Q:** Does every Gap Findings Table entry have a specific Exact Fix naming the configuration object and post-fix state?
> **A:** [Yes -- verified / No -- complete now]
> **Evidence:** Every Exact Fix names the object, current state, and target state.

Return to the Gap Findings Table and fill it in completely.

---

## V-05 -- Combined: Full R6 Scaffold (C-25 + C-26 + C-27 + C-28)

**Axis:** All four R6 criteria wired as structural constraints into the complete C-11--C-24 scaffold
**Hypothesis:** C-25--C-28 are four structurally adjacent improvements that fit cleanly into the R5-V-05 scaffold. C-25 replaces the flat FLS table with a tier-stratified matrix (lowest tier at which each sensitive field is reachable is now visible before analysis). C-26 extends the enforcement marker system with a second class: gate-absence markers that fire when mandatory gate sections are missing. C-27 adds named language exclusions to every binary verdict gate definition -- excluded phrases are declared at definition time so a scorer can cite the definition itself as the authority for rejection. C-28 adds forward-reference mandates: Stage 2 tier-boundary gates and the Stage 3 T-4 binary gate must each cite a named Temptation Ledger entry by its Boundary label -- converting the Ledger from a structural declaration that can be ignored into an active constraint with named checkpoints. A perfect R6 trace satisfying all 20 aspirational criteria scores 100.00.

---

You are running a permissions trace signal for: {{topic}}

---

## ENFORCEMENT SYSTEM (complete before any entity name, operation, or content)

This is the trace's literal first output. No entity name, operation, gap category, or analysis content appears before this section is complete.

### Content-Violation Markers

| Marker | Domain | Trigger Condition | Correction Required |
|--------|--------|-------------------|---------------------|
| `SCOPE-FAIL` | Record Access | Record Scope cell contains prose rather than a SCOPE LEXICON token | Replace with exact SCOPE LEXICON token; correct before advancing to the next row |
| `VERDICT-FAIL` | Verdict | Gate answer omits a binary verdict, or uses language named in a gate's excluded list | Restate with a declared permitted binary verdict before advancing |
| `EVIDENCE-REQUIRED` | Evidence | Gate answer lacks an Evidence line ("I checked [X] -- [result] because [Y]") | Add the three-part Evidence line before advancing to the next gate |
| `FLS-FAIL` | Field Security | Sensitive field (PII / Financial / Health / Credential / Internal-Audit) in FLS matrix without a field security profile | Add FLS-EXPOSURE to Gap Findings Table immediately; do not defer |
| `GAP-FAIL` | Gap / Conflict | Gap category investigated with no explicit finding or rule-out | State the finding or rule-out with evidence before advancing |

### Gate-Absence Markers

A gate-absence marker fires when a mandatory gate section is missing from the output at the point where it is required. A section heading with no content does not escape the marker -- the gate must be answered, not merely headed.

| Marker | Gate It Guards | When It Fires | Recovery Required |
|--------|----------------|---------------|-------------------|
| `FLS-GATE-ABSENT` | Stage 1 § 1c FLS gate | 1c section (Evidence gate + tier-stratified matrix) missing before Stage 2 begins | Insert the complete 1c FLS gate section before advancing |
| `TIER-GATE-ABSENT` | Stage 2 per-boundary tier gate | Any T-N→T-N+1 boundary in the tier assignment has no gate section in Stage 2 | Insert the missing boundary gate with Evidence-template answer and Temptation Ledger citation |
| `ESCALATION-GATE-ABSENT` | Stage 2 escalation gate | Escalation gate section missing from Stage 2 | Insert the complete escalation gate before Stage 3 |
| `BINARY-GATE-ABSENT` | Stage 3 T-4 binary gate | T-4 role exists in the tier assignment but no binary gate section appears in Stage 3 | Insert T-4 binary gate with Evidence-template answer and Temptation Ledger citation |

**Section-open rule:** At the start of Stage 1, Stage 2, and Stage 3, re-declare both content-violation and gate-absence markers by name before any section content appears.

---

## BINARY VERDICT GATE DEFINITIONS (locked -- applies at every binary gate in Stages 2 and 3)

Permitted and excluded language are declared here before any gate is answered. A writer may not claim a gate is satisfied with language this section explicitly names as excluded.

**Tier-boundary binary gate (T-2→T-3 and T-3→T-4):**
- Permitted verdicts: `JUSTIFIED` or `NOT-JUSTIFIED`
- **Excluded language (does not satisfy this gate):** "probably justified," "likely warranted," "appears appropriate," "seems reasonable," "generally acceptable," "may be justified," "could be necessary"
- A verdict using any excluded phrase fires `VERDICT-FAIL` and must be restated with a permitted verdict.

**T-4 binary gate (every T-4 role in Stage 3):**
- Permitted verdicts: `JUSTIFIED` or `NOT-JUSTIFIED`
- **Excluded language (does not satisfy this gate):** "probably justified," "likely warranted," "appears appropriate," "might be necessary," "arguably required," "probably not required," "seems to be needed," "appears to be the right level," "probably makes sense"
- No other verdict form satisfies this gate.

---

## SCOPE LEXICON (locked)

| Token | Meaning |
|-------|---------|
| `Org` | All records in the organization |
| `BU` | Records owned by users in the same business unit |
| `Parent-Child BU` | Records in the same BU and all child BUs |
| `Team:[name]` | Records owned by or shared to a named team (substitute actual name) |
| `User` | Only the user's own records |
| `Sharing:[rule name]` | Records accessible via a named sharing rule (substitute actual rule name) |

---

## PRIVILEGE TIER LADDER (complete before Temptation Ledger -- locked after this section)

| Tier | Label | Privilege Boundary | Signature Capabilities |
|------|-------|-------------------|------------------------|
| T-1 | Read-Only Floor | Read records within assigned scope only | Read on entities; no Create, Write, Delete, Assign |
| T-2 | Operational | Create and write records within assigned scope | Create + Read + Write; no security configuration |
| T-3 | Elevated | Assign, reassign, or manage team membership | Write + Assign + team/queue management; no BU or role configuration |
| T-4 | Administrative Ceiling | System-level security configuration | Security role assignment, BU configuration, org-wide settings |

**Role-to-tier assignment (complete before Temptation Ledger):**

| Role Name | Tier | Type (human / non-human / stock) | Tier Justification (one sentence) |
|-----------|------|----------------------------------|----------------------------------|

Assign every role to exactly one tier. A role spanning two tiers: assign to the higher and note the downgrade recommendation. Any T-4 role beyond System Administrator or a fully documented custom admin role is an ESCALATION-PATH finding.

---

## TEMPTATION LEDGER (pre-committed -- complete before Gap Register)

These entries are locked before any role assignment analysis begins. Every Stage 2 tier-boundary gate and the Stage 3 T-4 binary gate must cite the relevant entry by its exact Boundary label. A gate that does not cite its Ledger entry fails C-28's forward-reference mandate and fires `EVIDENCE-REQUIRED`.

| Boundary | Inertia Temptation | Rejection Criterion |
|----------|--------------------|---------------------|
| T-1 → T-2 | Assigning Create/Write to a read-only persona to avoid restricting the base role | Write is justified only when the persona has documented Create or Write job tasks; read-only personas do not require Create or Write on any entity |
| T-2 → T-3 | Assigning Assign/team-management to an operational role to avoid configuring queue ownership separately | Assign is justified only when the role must formally reassign records; team or queue management requires explicit documentation of the ownership requirement |
| T-3 → T-4 | Assigning System Administrator to avoid creating a custom security role with constrained privileges | System Administrator is justified only when no combination of lower-tier privileges satisfies the documented requirement; "it is easier to configure" is not a justification |

Add rows for boundary-specific temptations discovered during Stage 2. Do not remove rows.

---

## GAP CATEGORY REGISTER (pre-committed -- complete before Stage 1)

| Category | What It Catches |
|----------|----------------|
| FLS-EXPOSURE | Sensitive field accessible without a field security profile |
| ESCALATION-PATH | Role reaches a higher tier through an available action |
| SHARING-CONFLICT | Sharing rule reopens access the OWD + tier model intends to restrict |
| TEAM-GAP | Team-scoped operation with uncontrolled or absent membership governance |
| CROSS-CASCADE | Relationship behavior grants unintended cross-entity access |
| OWD-MISMATCH | OWD broader than entity sensitivity warrants |

**Gap Findings Table -- do not populate now. Return here after Stage 3.**

| # | Category | Entity | Field (if FLS) | Role | Tier | Severity | Exact Fix |
|---|----------|--------|----------------|------|------|----------|-----------|

Severity: CRITICAL / HIGH / MEDIUM. Exact Fix: name the specific configuration object and the expected state after the fix.

---

## STAGE 1 -- INVENTORY

**Active content-violation markers: `SCOPE-FAIL` | `VERDICT-FAIL` | `EVIDENCE-REQUIRED` | `FLS-FAIL` | `GAP-FAIL`**
**Active gate-absence markers: `FLS-GATE-ABSENT`**

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) | Tiers with any access |
|--------|-----------------|-----------------------------------|-----------------------|

For each entity: list which tiers hold any privilege. This determines which tier-boundary gates must fire in Stage 2.

**1b -- Operation-role matrix by tier (one table per entity):**

| Entity: [name] | Role | Tier | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|------|--------|------|-------|--------|--------|--------------|

Allowed values: YES / NO / CONDITIONAL (state condition). Record Scope: SCOPE LEXICON tokens only. Mark any `SCOPE-FAIL` and correct before 1c.

Tier consistency check: A T-1 role with Write = YES is a tier misclassification -- correct the tier assignment or flag the excess privilege before advancing.

**1c -- Field-level security gate (C-25: tier-stratified matrix required)** *(absent before Stage 2: `FLS-GATE-ABSENT` fires)*

> **Q:** Does every sensitive field on every entity in scope have a field security profile, and what is the lowest tier at which each sensitive field first becomes readable or writable?
> **A:** [verdict per entity]
> **Evidence:** I checked Security > Field Security Profiles for [entity list] -- [per-entity result] because [profile name exists / no profile found / no sensitive fields; fields reviewed: list].

For each sensitive field with no FLS profile: `FLS-FAIL` fires -- add FLS-EXPOSURE row to Gap Findings Table now. Severity = CRITICAL. Tier = lowest tier with entity Read access.

Build the tier-stratified FLS matrix for each entity with sensitive fields:

| Entity | Field | Sensitivity | FLS Profile Name | T-1: R/W | T-2: R/W | T-3: R/W | T-4: R/W |
|--------|-------|-------------|-----------------|----------|----------|----------|----------|

Column values: `R` = roles at this tier may read this field. `W` = write. `R+W` = both. `-` = denied. No FLS profile: `OPEN` for every tier with entity Read access.

**Lowest-tier access statement (required for each sensitive field):** "Lowest tier with Read access on [field]: T-[N]. Lowest tier with Write access on [field]: T-[N]." If either value is lower than the tier at which documented operations require that access level, add an FLS-EXPOSURE finding now.

If an entity has zero sensitive fields: "Confirmed: [Entity] has no fields with sensitivity >= Medium. Fields reviewed: [list at least three field names]."

---

## STAGE 2 -- GAP ANALYSIS

**Active content-violation markers: `SCOPE-FAIL` | `VERDICT-FAIL` | `EVIDENCE-REQUIRED` | `FLS-FAIL` | `GAP-FAIL`**
**Active gate-absence markers: `TIER-GATE-ABSENT` | `ESCALATION-GATE-ABSENT`**

**Tier-boundary gates** *(C-28 forward-reference: each gate must cite its Temptation Ledger entry by Boundary label; absent gate: `TIER-GATE-ABSENT` fires; present gate with excluded verdict: `VERDICT-FAIL` fires)*

For each T-N→T-N+1 boundary present in the tier assignment:

> **Q:** Is the privilege step from T-[N] to T-[N+1] JUSTIFIED or NOT-JUSTIFIED for the operations in scope?
> **A:** [JUSTIFIED / NOT-JUSTIFIED -- permitted verdicts only per Binary Verdict Gate Definitions; excluded language fires `VERDICT-FAIL`]
> **Evidence:** I checked [operations requiring T-[N+1] capabilities] -- [specific capability unavailable at T-[N]] because [why T-[N] ceiling is insufficient]. **Temptation Ledger citation (T-[N]→T-[N+1]):** [quote the named Temptation from the Ledger entry for this exact boundary]. Rejection: [how this evidence specifically rejects the named temptation -- state what the temptation would have assigned and why the evidence rules it out or confirms it].

Forward-reference check: the Temptation Ledger entry must be cited by its exact Boundary label. A tier-boundary gate answer without a Temptation Ledger citation fires `EVIDENCE-REQUIRED`.

**Escalation gate** *(absent: `ESCALATION-GATE-ABSENT` fires)*

> **Q:** Can any role in the model reach a higher tier through team membership, security role assignment, ownership reassignment, or BU configuration?
> **A:** [Yes / No]
> **Evidence:** I checked [role list] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-role result] because [per-role structural reason].

Finding format: `[Role, T-N] -> [Action] -> [Tier or access gained]` -- add ESCALATION-PATH to Gap Findings Table.

**Sharing conflict gate:**

> **Q:** Do any active sharing rules reopen access the OWD + tier model intends to restrict?
> **A:** [Yes / No]
> **Evidence:** I checked sharing rules [list or "no rules found"] for [entity list] -- [per-rule result] because [comparison to OWD + tier scope].

| Rule Name | Trigger | Access Opened | Record Scope | Benefits Tier(s) | Overreach? |
|-----------|---------|---------------|--------------|-----------------|------------|

Record Scope: SCOPE LEXICON tokens only. Overreach = YES: add SHARING-CONFLICT to Gap Findings Table.

**Team membership gate:**

> **Q:** Is team membership for every team-scoped role controlled to prevent lower-tier elevation?
> **A:** [Yes / No]
> **Evidence:** I checked team [name] membership -- [mechanism]; self-addition is [possible / not possible] because [specific constraint].

**OWD sensitivity gate:**

> **Q:** Is the OWD for each high-sensitivity entity more permissive than the data warrants?
> **A:** [verdict per high-sensitivity entity]
> **Evidence:** I checked OWD for [entity] -- [OWD token] -- [justified / unjustified] because [FLS compensates / no compensating control].

**Cross-entity cascade gate:**

> **Q:** What is the lowest-tier path to the highest-sensitivity entity, and is each hop intentional?
> **A:** [trace through at least two hops]
> **Evidence:** I traced [Role, T-N] -> [Entity A, Record Scope: token] -> [Relationship type, cascade setting] -> [Entity B, Record Scope: token] -- hop 1 [intentional / emergent because reason]; hop 2 [intentional / emergent because reason].

All Record Scope tokens at every hop: SCOPE LEXICON only.

---

## STAGE 3 -- ROLE ASSESSMENT AND REMEDIATION

**Active content-violation markers: `SCOPE-FAIL` | `VERDICT-FAIL` | `EVIDENCE-REQUIRED` | `FLS-FAIL` | `GAP-FAIL`**
**Active gate-absence markers: `BINARY-GATE-ABSENT`**

**Customer Service Representative gate:**

> **Q:** Does the Customer Service Representative stock role access any sensitive field or operation beyond what the CS job function requires, and which tier does it occupy?
> **A:** [verdict and tier]
> **Evidence:** I checked CS access for [entity list, sensitive field list from the tier-stratified FLS matrix in 1c] -- [per-item result] because [FLS profile / OWD / role scope]. CS belongs in T-[N] because [matching tier definition].

**Dataverse Security Expert gate:**

> **Q:** Does the Dataverse Security Expert role hold privileges beyond least-privilege for a security configuration task, and which tier does it occupy?
> **A:** [verdict and tier]
> **Evidence:** I checked expert privileges beyond CS access -- [excess list or NONE] because [comparison against security configuration task scope]. Expert belongs in T-[N] because [matching tier definition].

Both roles must appear by name with distinct specific access observations and explicit tier assignments. A merged summary fires `VERDICT-FAIL`.

**Least-privilege scoring:**

| Role | Tier | Persona | Excess Privileges | LP Score (0-10) | Over-Privileged? | Reduction Required |
|------|------|---------|-------------------|-----------------|------------------|--------------------|

LP Score < 7: state the specific privilege to reduce, the target scope, and whether the role should drop a tier.

**T-4 binary gate (required if any T-4 role exists)** *(C-28 forward-reference: cite Temptation Ledger T-3→T-4 entry by label; absent: `BINARY-GATE-ABSENT` fires; excluded verdict: `VERDICT-FAIL` fires)*

> **Q:** Is the assignment of a T-4 (Administrative Ceiling) role JUSTIFIED or NOT-JUSTIFIED for the operations in scope?
> **A:** [JUSTIFIED / NOT-JUSTIFIED -- permitted verdicts only per Binary Verdict Gate Definitions; excluded language fires `VERDICT-FAIL`]
> **Evidence:** I checked T-4 role's required operations -- [operation list] -- [each requires T-4 because specific structural reason / no operation requires T-4 because lower-tier alternative exists]. **Temptation Ledger citation (T-3→T-4):** [quote the named Temptation from the Ledger's T-3→T-4 entry]. Rejection: [how this evidence specifically rejects the named temptation -- state what the temptation would have assigned and why the evidence rules it out or confirms it].

Forward-reference check: the T-3→T-4 Temptation Ledger entry must be cited by its exact Boundary label. A T-4 binary gate answer without a Ledger citation fires `EVIDENCE-REQUIRED`. Excluded language at this gate: "probably justified," "likely warranted," "appears appropriate," "might be necessary," "arguably required." None satisfies this gate.

**Gap Register citation check (required before remediation):**

> **Q:** Does every row in the Gap Findings Table reference a category from the pre-committed Gap Category Register?
> **A:** [Yes -- verified / No -- correct now]
> **Evidence:** I checked each Gap Findings row against the Gap Category Register -- [per-row result]. Any row without a matching pre-declared category fires `GAP-FAIL`.

**Attack scenario (if any ESCALATION-PATH found in Stage 2):**
`Starting role (T-N) -> Action sequence -> Tier or access gained`. Abstract risk statements do not satisfy this section.

**Remediation gate:**

> **Q:** Does every entry in the Gap Findings Table have a specific Exact Fix that names the configuration object and post-fix state?
> **A:** [Yes -- verified / No -- complete now]
> **Evidence:** Every Exact Fix row names [field security profile / sharing rule / security role privilege / OWD setting], current state, and target state.

Format per finding: "Change [configuration object name] in [solution location] from [current state] to [target state]. Post-fix verification: [what a security auditor would observe to confirm the fix]."

Now return to the Gap Findings Table and fill it in completely. Every row must fit a pre-declared category. Every Exact Fix must name the specific configuration object.
