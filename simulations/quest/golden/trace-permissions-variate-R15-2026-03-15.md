# trace-permissions Variate -- Round 5 (Rubric v5)
**Date:** 2026-03-15
**Rubric:** v5 (C-01 through C-24)
**Round note:** Rubric v5 adds four new aspirational criteria (C-21--C-24) targeting the tier-structure failure modes identified in Round 4: flat role lists that hide the privilege gradient (C-21), tier boundaries traversed without per-boundary evidence (C-22), over-assignment temptations that are implicit rather than named (C-23), and max-privilege verdicts that hedge rather than commit to a binary outcome (C-24). This round explores each new criterion as a single axis before combining all four in V-05.

---

## Round 5 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Role sequence -- ascending tier ladder declared as the trace's first output | C-21 requires roles organized in named ascending tiers before analysis; making the tier ladder the literal first element means every subsequent role assignment is made in reference to a named tier position rather than a flat list, making over-assignment visible at classification time |
| V-02 | Lifecycle emphasis -- per-tier-boundary Evidence gate as mandatory lifecycle checkpoint | C-22 requires Evidence-template justification at each T-N to T-N+1 boundary; embedding tier advances as explicit lifecycle gates (not just format guidance) closes privilege creep at write-time: advancement without evidence produces a named gate violation before the trace proceeds |
| V-03 | Inertia framing -- pre-committed Temptation Ledger declared before analysis | C-23 requires naming the inertia temptation at each tier boundary; declaring a Temptation Ledger before entities are enumerated forces the trace to pre-commit to the most likely over-assignment lure at each boundary, converting a retrospective label into a prospective gate that must be explicitly rejected |
| V-04 | Combined: role sequence (isolated max-privilege section) + phrasing register (binary verdict format) | C-24 requires a binary justified/not-justified gate for the highest privilege tier; isolating T-4 as a dedicated section and requiring a binary verdict with Evidence-template content closes both failure paths -- silence (no gate = no decision) and narrative hedging (no binary = ambiguous conclusion) |
| V-05 | Combined: all four v5 criteria wired as structural constraints into the full C-11--C-20 scaffold | C-21--C-24 are tier-structure discipline enforcers; they do not conflict with the enforcement-marker and evidence-gate scaffold from rounds 3 and 4 -- they specialize those mechanisms to tier boundaries, the highest-risk assignment points. All four wired together on the proven full scaffold targets 100.00 |

---

## V-01 -- Role Sequence: Ascending Tier Ladder as First Output

**Axis:** Role sequence -- an ascending tier ladder (T-1 through T-4) is the trace's literal first element, before any entity, operation, or gap register
**Hypothesis:** C-21 requires roles organized in named ascending tiers before analysis begins. A tier ladder stated first makes the privilege gradient structurally primary: every role assignment in every subsequent table must reference a named tier. When a T-1 role appears with Org-level write scope, the contradiction is visible at Stage 1 because the tier label was already committed. A flat role list discovered during Stage 3 cannot surface this contradiction at classification time.

---

You are running a permissions trace signal for: {{topic}}

---

## PRIVILEGE TIER LADDER (complete before any other output)

Before naming any entity, operation, or gap category: declare the ascending privilege tier structure for this trace. Tier labels are locked after this section. Every role in this trace must appear in exactly one tier.

**Step 1 -- Define tiers:**

| Tier | Label | Privilege Boundary | Signature Capabilities |
|------|-------|-------------------|----------------------|
| T-1 | Read-Only Floor | Read records within assigned scope only | Read on entities; no Create, Write, Delete, Assign |
| T-2 | Operational | Create and write records within assigned scope | Create + Read + Write on entities; no security configuration |
| T-3 | Elevated | Assign, reassign, or manage team membership | Write + Assign + team/queue management; no BU or role configuration |
| T-4 | Administrative Ceiling | System-level security configuration | Security role assignment, BU configuration, org-wide settings |

**Step 2 -- Assign roles to tiers:**

| Role Name | Tier | Type (human / non-human / stock) | Tier Justification |
|-----------|------|----------------------------------|-------------------|

Place every role identified in {{topic}} in exactly one tier. If a role spans two tiers (holds some T-2 capabilities and some T-3 capabilities): assign it to the higher tier and note the downgrade recommendation.

**Tier gap rule:** If T-4 contains any role beyond System Administrator or a custom role with documented system-administration scope, state the justification for that classification before proceeding. A role in T-4 without justification is an ESCALATION-PATH finding.

---

**GAP CATEGORY REGISTER (pre-committed -- complete before Stage 1)**

| Category | What It Catches |
|----------|----------------|
| FLS-EXPOSURE | Sensitive field accessible without a field security profile |
| ESCALATION-PATH | Role reaches a higher tier through an available action |
| SHARING-CONFLICT | Sharing rule reopens access the OWD + tier model intends to restrict |
| TEAM-GAP | Team-scoped operation with uncontrolled or absent membership governance |
| CROSS-CASCADE | Relationship behavior grants unintended cross-entity access |
| OWD-MISMATCH | OWD broader than entity sensitivity warrants |

**Gap Findings Table -- do not populate now. Return after Stage 3.**

| # | Category | Entity | Field (if FLS) | Role | Tier | Severity | Exact Fix |
|---|----------|--------|----------------|------|------|----------|-----------|

Severity: CRITICAL / HIGH / MEDIUM. Exact Fix: name the specific configuration object and post-fix state.

---

**SCOPE LEXICON (locked -- tokens only in every Record Scope cell)**

| Token | Meaning |
|-------|---------|
| `Org` | All records in the organization |
| `BU` | Records owned by users in the same business unit |
| `Parent-Child BU` | Records in the same BU and all child BUs |
| `Team:[name]` | Records owned by or shared to a named team |
| `User` | Only the user's own records |
| `Sharing:[rule name]` | Records via a named sharing rule |

Inline rule: Non-token scope prose marks **SCOPE-FAIL** -- correct before advancing.

---

## STAGE 1 -- INVENTORY

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) | Tiers with access |
|--------|-----------------|-----------------------------------|-------------------|

For each entity: note which tiers hold any privilege on it. This drives the tier-boundary analysis in Stage 2.

**1b -- Operation-role matrix by tier (one table per entity):**

| Entity: [name] | Role | Tier | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|------|--------|------|-------|--------|--------|--------------|

Use YES / NO / CONDITIONAL (state condition). All Record Scope cells: SCOPE LEXICON tokens only. Mark any SCOPE-FAIL and correct before 1c.

Tier consistency check: for each row, confirm that the operations permitted align with the tier definition. A T-1 role with YES in Write or Delete is a tier misclassification -- correct the tier assignment or flag the excess privilege.

**1c -- Field-level security gate:**

> **Q:** Does every sensitive field on every entity have a field security profile?
> **A:** [verdict per entity]
> **Evidence:** I checked Security > Field Security Profiles for [entity list] -- [result per entity] because [profile name exists / no profile / entity has no sensitive fields and fields reviewed: list].

For each sensitive field with no profile: add FLS-EXPOSURE row to Gap Findings Table now. Severity = CRITICAL. Tier = the tier(s) that can reach this field without restriction.

| Entity | Field | Sensitivity | FLS Profile Name | T-1: Read/Write | T-2: Read/Write | T-3: Read/Write | T-4: Read/Write |
|--------|-------|-------------|-----------------|-----------------|-----------------|-----------------|-----------------|

---

## STAGE 2 -- TIER-BOUNDARY GAP ANALYSIS

For each gate: answer with verdict and Evidence line. A verdict without Evidence is an inline failure.

**Tier escalation gate -- can any tier cross a boundary?**

For each boundary (T-1 to T-2, T-2 to T-3, T-3 to T-4): does any role in the lower tier hold Write on team membership, security role assignment, record ownership, or BU configuration that would let it reach the higher tier's privilege level?

> **Q:** Can any T-1 or T-2 role reach T-3 or T-4 through team membership, security role assignment, ownership reassignment, or BU configuration?
> **A:** [verdict per boundary]
> **Evidence:** I checked [roles at T-1 and T-2] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-role result] because [per-role structural reason].

Finding format: `[Role, Tier N] -> [Action] -> [Privilege gained at Tier N+1]`

**Sharing conflict gate:**

> **Q:** Do any active sharing rules reopen access that the OWD + tier model intends to restrict?
> **A:** [verdict]
> **Evidence:** I checked sharing rules [list rule names or "no rules found"] for [entity list] -- [per-rule result] because [comparison of opened access to OWD + tier scope].

| Rule Name | Trigger | Access Opened | Record Scope | Benefits Tier(s) | Overreach? |
|-----------|---------|---------------|--------------|-----------------|------------|

All Record Scope cells: SCOPE LEXICON only. Overreach = YES: add SHARING-CONFLICT to Gap Findings Table.

**Team membership gate:**

> **Q:** Is team membership for every team-scoped role controlled in a way that prevents a lower-tier role from gaining higher-tier access?
> **A:** [verdict]
> **Evidence:** I checked team [name] membership control -- [mechanism]; a T-[N] role [can / cannot] add itself because [specific constraint].

**OWD sensitivity gate:**

> **Q:** Is the OWD for each high-sensitivity entity more permissive than the data warrants?
> **A:** [verdict per high-sensitivity entity]
> **Evidence:** I checked OWD for [entity] -- [token] -- [justified / unjustified] because [FLS compensates / no compensating control].

---

## STAGE 3 -- ROLE ASSESSMENT AND REMEDIATION

**Customer Service Representative gate:**

> **Q:** Is the Customer Service Representative correctly placed in the tier ladder, with no excess privileges for the CS job function?
> **A:** [verdict and tier assignment]
> **Evidence:** I checked CS access for [entity list, sensitive field list] -- [per-item result] because [FLS / role scope / OWD]. CS belongs in T-[N] because [matching tier definition].

**Dataverse Security Expert gate:**

> **Q:** Does the Dataverse Security Expert hold only the privileges that a security configuration task requires, with no excess above the minimum tier needed?
> **A:** [verdict and tier assignment]
> **Evidence:** I checked expert privileges beyond CS access -- [excess list or NONE] because [comparison to security configuration task scope]. Expert belongs in T-[N] because [matching tier definition].

Both roles must appear by name. Both must have distinct specific observations and an explicit tier assignment.

**Tier-based least-privilege scoring:**

| Role | Tier | Persona | Excess Privileges | LP Score (0-10) | Over-Privileged? | Target Tier if Reclassification Needed |
|------|------|---------|-------------------|-----------------|------------------|----------------------------------------|

LP Score < 7: state the specific privilege to reduce, the target scope, and whether the role should drop a tier.

**Attack scenario (if ESCALATION-PATH found):**
`Starting role (T-N) -> Action sequence -> Privilege gained (T-M)`. Abstract risk statements do not satisfy this section.

**Remediation gate:**

> **Q:** Does every entry in the Gap Findings Table have a specific Exact Fix naming the configuration object and post-fix state?
> **A:** [Yes -- verified / No -- complete now]
> **Evidence:** Every Exact Fix row names [field security profile / sharing rule / security role privilege / OWD setting], current state, and target state.

Return to the Gap Findings Table and fill it in completely.

---

## V-02 -- Lifecycle Emphasis: Tier-Boundary Evidence Gates as Mandatory Checkpoints

**Axis:** Lifecycle emphasis -- each T-N to T-N+1 tier boundary is a named mandatory lifecycle gate; the trace cannot advance past a boundary without an Evidence-template answer justifying why the higher tier's privilege is required
**Hypothesis:** C-22 requires Evidence-template justification at each tier transition. The failure mode is not just omitting the evidence -- it is traversing tier boundaries silently, as if the decision were obvious. Making each boundary a named, mandatory gate (not an inline format note) forces the model to stop, name what is being added, and justify it before the trace continues. A blanket Evidence statement covering multiple tier advances does not satisfy a per-boundary gate.

---

You are running a permissions trace signal for: {{topic}}

---

**GAP CATEGORY REGISTER (pre-committed)**

| Category | What It Catches |
|----------|----------------|
| FLS-EXPOSURE | Sensitive field without a field security profile |
| ESCALATION-PATH | Role reaches a higher tier through an available action |
| SHARING-CONFLICT | Sharing rule reopens access the OWD + role model intends to restrict |
| TEAM-GAP | Team-scoped operation with uncontrolled membership |
| CROSS-CASCADE | Relationship behavior grants unintended cross-entity access |
| OWD-MISMATCH | OWD broader than entity sensitivity warrants |

**Gap Findings Table -- do not populate now. Return after Stage 3.**

| # | Category | Entity | Field (if FLS) | Role | Severity | Exact Fix |
|---|----------|--------|----------------|------|----------|-----------|

---

**SCOPE LEXICON (locked)**

`Org` / `BU` / `Parent-Child BU` / `Team:[name]` / `User` / `Sharing:[rule name]`

Non-token scope prose: mark **SCOPE-FAIL**, correct before advancing.

---

## STAGE 1 -- INVENTORY

**1a -- Tier ladder declaration:**

Declare the ascending tier structure before assigning any role:

| Tier | Privilege Boundary | Roles Assigned |
|------|-------------------|----------------|
| T-1 | Read-only within scope | |
| T-2 | Create + write within scope | |
| T-3 | Assign + team management | |
| T-4 | Security role assignment + BU configuration (System Admin ceiling) | |

Fill in Roles Assigned before proceeding to 1b. Every role must appear in exactly one tier.

**1b -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) |
|--------|-----------------|-----------------------------------|

**1c -- Operation-role matrix (one table per entity):**

| Entity: [name] | Role | Tier | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|------|--------|------|-------|--------|--------|--------------|

All Record Scope cells: SCOPE LEXICON tokens only.

**1d -- Field-level security gate:**

> **Q:** Does every sensitive field on every entity have a field security profile?
> **A:** [verdict per entity]
> **Evidence:** I checked Security > Field Security Profiles for [entity list] -- [per-entity result] because [profile name / no profile / no sensitive fields and fields reviewed: list].

| Entity | Field | Sensitivity | FLS Profile Name | Roles: Read | Roles: Write |
|--------|-------|-------------|-----------------|-------------|--------------|

---

## TIER-BOUNDARY GATES (mandatory -- each gate must be answered before analysis of the next tier)

**BOUNDARY GATE: T-1 to T-2**

Roles entering T-2 gain Create and Write capability. Before listing any T-2 role's operations:

> **Q:** Does each T-2 role require Create and Write capability for its documented function? What is the specific business need that justifies elevation from T-1 (read-only)?
> **A:** [verdict per T-2 role]
> **Evidence:** I checked [T-2 role] function against T-1 capability -- [result] because [the function requires [specific operation] that T-1 cannot perform, and the minimum necessary scope is [token]].

A T-2 assignment without Evidence-template justification is a tier-gate violation. State the justification before listing T-2 operations.

**BOUNDARY GATE: T-2 to T-3**

Roles entering T-3 gain Assign and team/queue management capability. Before listing any T-3 role's operations:

> **Q:** Does each T-3 role require Assign or team management capability for its documented function? What escalation risk does this boundary introduce, and is that risk addressed?
> **A:** [verdict per T-3 role]
> **Evidence:** I checked [T-3 role] function against T-2 capability -- [result] because [the function requires [specific operation] that T-2 cannot perform]. Escalation risk at this boundary: [specific risk, e.g., record reassignment enabling cross-BU access]. Risk addressed by: [specific control].

**BOUNDARY GATE: T-3 to T-4**

Roles entering T-4 gain system-level security configuration capability. This is the highest-risk boundary. Before listing any T-4 role:

> **Q:** Does each T-4 role require security role assignment or BU configuration capability? Is the assignment justified or is the role over-placed into T-4 to avoid configuring a more restrictive custom role?
> **A:** [justified / not justified] (binary -- no middle ground)
> **Evidence:** I checked [T-4 role] function against T-3 capability -- [result] because [the function explicitly requires [specific system-level operation] that T-3 cannot perform]. Alternatives considered: [specific T-3 alternatives that were evaluated and found insufficient].

Binary verdict required. "Probably justified" or "partially warranted" does not satisfy this gate.

---

## STAGE 2 -- GAP ANALYSIS

Apply Evidence-template format to every gate. A verdict without Evidence is an inline failure.

**Escalation gate:**

> **Q:** Can any role reach a higher tier's privilege level through team membership, security role assignment, ownership reassignment, or BU configuration?
> **A:** [verdict]
> **Evidence:** I checked [role list] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-role result] because [per-role structural reason].

**Sharing conflict gate:**

> **Q:** Do any active sharing rules reopen access that the OWD + tier model intends to restrict?
> **A:** [verdict]
> **Evidence:** I checked sharing rules [list or "no rules"] for [entity list] -- [per-rule result] because [comparison to OWD + tier scope].

| Rule Name | Trigger | Access Opened | Record Scope | Benefits Tier | Overreach? |
|-----------|---------|---------------|--------------|--------------|------------|

**Team membership gate:**

> **Q:** Is team membership for every team-scoped role controlled in a way that prevents unauthorized tier elevation?
> **A:** [verdict]
> **Evidence:** I checked team [name] control -- [mechanism]; self-addition is [possible / not possible] because [specific constraint].

**OWD sensitivity gate:**

> **Q:** Is the OWD for each high-sensitivity entity appropriate for its sensitivity?
> **A:** [verdict per entity]
> **Evidence:** I checked OWD for [entity] -- [token] -- [justified / unjustified] because [compensating controls / no compensating controls].

---

## STAGE 3 -- ROLE ASSESSMENT AND REMEDIATION

**Customer Service Representative gate:**

> **Q:** Does the CS role operate at the correct tier with no excess privilege beyond the CS job function?
> **A:** [verdict]
> **Evidence:** I checked CS access for [entity list, sensitive fields] -- [per-item result] because [FLS / tier definition / OWD].

**Dataverse Security Expert gate:**

> **Q:** Does the Dataverse Security Expert hold only the privileges a security configuration task requires?
> **A:** [verdict]
> **Evidence:** I checked expert privileges beyond CS -- [excess or NONE] because [comparison to security task scope].

Both roles must appear by name with distinct specific observations.

**Least-privilege scoring:**

| Role | Tier | Persona | Excess Privileges | LP Score (0-10) | Over-Privileged? | Reduction Required |
|------|------|---------|-------------------|-----------------|------------------|--------------------|

LP Score < 7: state the specific privilege to reduce and target scope.

**Attack scenario (if ESCALATION-PATH found):**
`Starting role (T-N) -> Action sequence -> Gained access (T-M)`. Abstract statements do not satisfy this section.

**Remediation gate:**

> **Q:** Does every entry in the Gap Findings Table have a specific Exact Fix naming the configuration object and post-fix state?
> **A:** [Yes -- verified / No -- complete now]
> **Evidence:** Every Exact Fix names [configuration object], current state, and target state.

Return to the Gap Findings Table and fill it in completely.

---

## V-03 -- Inertia Framing: Pre-Committed Temptation Ledger

**Axis:** Inertia framing -- a named Temptation Ledger is declared before entities are enumerated; each tier boundary has a pre-committed description of the most likely over-assignment temptation; the trace must explicitly reject or accept the temptation with a stated reason before assigning any role to that tier
**Hypothesis:** C-23 requires naming the inertia temptation at each tier boundary and explicitly rejecting it. The key insight is timing: naming the temptation before the assignment decision is made forces the writer to confront the easiest wrong choice at the moment of maximum risk. Post-hoc labeling ("we could have assigned System Admin but didn't") does not intercept the failure mode -- it merely annotates it. The Temptation Ledger pre-commits the wrong choice so that the right choice requires an explicit act of rejection.

---

You are running a permissions trace signal for: {{topic}}

---

## TEMPTATION LEDGER (declare before any role assignment)

Before enumerating any entity, role, or operation: declare the inertia temptation at each tier boundary. These are the over-privileged assignments that feel easiest at each stage of the trace -- the path of least resistance that privilege creep always follows. They are declared now so that each one can be explicitly rejected (or justified) at decision time.

| Tier Boundary | Default Temptation | Why It Feels Easy | What It Costs |
|---------------|-------------------|-------------------|---------------|
| T-1 to T-2 | Assign all roles at T-2 to avoid restricting create/write to a subset | Fewer configuration objects to manage; avoids custom role creation | Every role can create and modify records regardless of whether their job requires it |
| T-2 to T-3 | Assign T-3 (Assign + team management) to any role that occasionally needs to reassign records | Fewer escalation requests; avoids per-operation configuration | Roles with Assign privilege can redirect records to teams they control, bypassing record scope restrictions |
| T-3 to T-4 | Assign System Administrator to avoid configuring field permission sets and sharing rule exceptions | Single role handles all edge cases; no custom role maintenance | System Admin bypasses all record-level security, FLS, and team restrictions; any System Admin account is a complete privilege escalation path |

**Ledger usage rule:** At each tier boundary in Stage 1 and Stage 2, the trace must reference this ledger entry, state whether the temptation was accepted or rejected, and give the specific reason. A tier assignment without a ledger reference is a C-23 gap.

---

**GAP CATEGORY REGISTER (pre-committed)**

| Category | What It Catches |
|----------|----------------|
| FLS-EXPOSURE | Sensitive field without a field security profile |
| ESCALATION-PATH | Role reaches a higher tier through an available action |
| SHARING-CONFLICT | Sharing rule reopens access the OWD + role model intends to restrict |
| TEAM-GAP | Team-scoped operation with uncontrolled membership |
| CROSS-CASCADE | Relationship behavior grants unintended cross-entity access |
| OWD-MISMATCH | OWD broader than entity sensitivity warrants |

**Gap Findings Table -- do not populate now. Return after Stage 3.**

| # | Category | Entity | Field (if FLS) | Role | Severity | Exact Fix |
|---|----------|--------|----------------|------|----------|-----------|

---

**SCOPE LEXICON (locked)**

`Org` / `BU` / `Parent-Child BU` / `Team:[name]` / `User` / `Sharing:[rule name]`

Non-token scope prose: mark **SCOPE-FAIL**, correct before advancing.

---

## STAGE 1 -- INVENTORY AND TIER CLASSIFICATION

**1a -- Ascending tier ladder with ledger references:**

Assign roles to tiers. At each tier boundary, reference the Temptation Ledger and state explicitly whether the temptation was accepted or rejected.

| Tier | Roles Assigned | Ledger Temptation Rejected? | Rejection Reason (or Acceptance Justification) |
|------|----------------|-----------------------------|-------------------------------------------------|
| T-1 (Read-Only) | | N/A (floor tier) | N/A |
| T-2 (Operational) | | [T-1 to T-2 temptation from ledger: accepted / rejected] | |
| T-3 (Elevated) | | [T-2 to T-3 temptation from ledger: accepted / rejected] | |
| T-4 (Admin Ceiling) | | [T-3 to T-4 temptation from ledger: accepted / rejected] | |

Rejection format: "Rejected [ledger temptation] because [specific reason the correct approach is safer or adequate for the function]. Instead: [what was configured and why it is sufficient]."

Acceptance format: "Accepted [ledger temptation] because [documented business justification that outweighs the cost stated in the ledger]. Compensating control: [specific control that limits the risk of the over-privileged assignment]."

**1b -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) |
|--------|-----------------|-----------------------------------|

**1c -- Operation-role matrix (one table per entity):**

| Entity: [name] | Role | Tier | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|------|--------|------|-------|--------|--------|--------------|

All Record Scope cells: SCOPE LEXICON tokens only. Mark any SCOPE-FAIL and correct before 1d.

**1d -- Field-level security gate:**

> **Q:** Does every sensitive field on every entity have a field security profile?
> **A:** [verdict per entity]
> **Evidence:** I checked Security > Field Security Profiles for [entity list] -- [per-entity result] because [profile name / no profile / no sensitive fields and fields reviewed: list].

| Entity | Field | Sensitivity | FLS Profile Name | Roles: Read | Roles: Write |
|--------|-------|-------------|-----------------|-------------|--------------|

---

## STAGE 2 -- GAP ANALYSIS

Apply Evidence-template format to every gate.

**Escalation gate:**

> **Q:** Can any role reach a higher tier's privilege level through team membership, security role assignment, ownership reassignment, or BU configuration?
> **A:** [verdict]
> **Evidence:** I checked [role list] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-role result] because [per-role structural reason].

Note: if any T-3 role can modify team membership in a way that grants T-4-equivalent access, cross-reference the T-2-to-T-3 ledger rejection -- was the temptation rejection invalidated by this escalation path?

**Sharing conflict gate:**

> **Q:** Do any active sharing rules reopen access that the OWD + tier model intends to restrict?
> **A:** [verdict]
> **Evidence:** I checked sharing rules [list or "no rules"] for [entity list] -- [per-rule result] because [comparison to OWD + tier scope].

| Rule Name | Trigger | Access Opened | Record Scope | Benefits Tier | Overreach? |
|-----------|---------|---------------|--------------|--------------|------------|

**Team membership gate:**

> **Q:** Is team membership for every team-scoped role controlled in a way that prevents unauthorized tier elevation?
> **A:** [verdict]
> **Evidence:** I checked team [name] control -- [mechanism]; self-addition is [possible / not possible] because [specific constraint].

**OWD sensitivity gate:**

> **Q:** Is the OWD for each high-sensitivity entity appropriate for its sensitivity?
> **A:** [verdict per entity]
> **Evidence:** I checked OWD for [entity] -- [token] -- [justified / unjustified] because [compensating controls or absence thereof].

---

## STAGE 3 -- ROLE ASSESSMENT AND REMEDIATION

**Customer Service Representative gate:**

> **Q:** Does the CS role operate at the correct tier, and was the T-1-to-T-2 ledger temptation properly rejected for this role?
> **A:** [verdict]
> **Evidence:** I checked CS access for [entity list, sensitive fields] -- [per-item result]. Ledger reference: [T-1-to-T-2 temptation] was [rejected because / accepted with compensating control].

**Dataverse Security Expert gate:**

> **Q:** Does the Dataverse Security Expert belong in T-4, and was the T-3-to-T-4 ledger temptation properly handled?
> **A:** [verdict]
> **Evidence:** I checked expert privileges -- [excess or NONE]. Ledger reference: [T-3-to-T-4 temptation] was [rejected because / accepted with compensating control].

Both roles must appear by name with distinct observations. Both must include a Ledger reference.

**Least-privilege scoring:**

| Role | Tier | Persona | Excess Privileges | LP Score (0-10) | Over-Privileged? | Ledger Temptation Accepted? |
|------|------|---------|-------------------|-----------------|------------------|-----------------------------|

Accepted temptations scoring below 7: the compensating control stated in Stage 1 must be verified or the acceptance must be reversed.

**Attack scenario (if ESCALATION-PATH found):**
`Starting role (T-N) -> Action sequence -> Gained access (T-M)`. Abstract statements do not satisfy this section.

**Remediation gate:**

> **Q:** Does every entry in the Gap Findings Table have a specific Exact Fix naming the configuration object and post-fix state?
> **A:** [Yes -- verified / No -- complete now]
> **Evidence:** Every Exact Fix names [configuration object], current state, and target state.

Return to the Gap Findings Table and fill it in completely.

---

## V-04 -- Combined: Isolated Max-Privilege Section + Binary Verdict Format

**Axis:** Role sequence (T-4 System Admin isolated in a dedicated section that runs before the main analysis) + phrasing register (binary justified/not-justified verdict format with no middle ground)
**Hypothesis:** C-24 requires a binary justified/not-justified gate for the highest privilege tier, answered with Evidence-template content. Two failure paths lead to non-binary outcomes: (1) the max-privilege role is not treated as a special case and receives the same narrative assessment as other roles, allowing hedged language; (2) the gate exists but permits "probably justified" or "partially warranted" verdicts that are not binary. Isolating T-4 as the first dedicated section -- before any entity or operation analysis -- and requiring a binary verdict with Evidence-template content closes both paths. The verdict is committed before the main trace begins, preventing post-hoc rationalization.

---

You are running a permissions trace signal for: {{topic}}

---

## SECTION 0 -- SYSTEM ADMINISTRATOR (T-4) BINARY GATE

This section runs before any entity enumeration, operation matrix, or gap register. The highest privilege role in the Dataverse security model -- System Administrator or an equivalent max-privilege role -- requires a dedicated binary justification before the trace proceeds.

**Step 0a -- Identify the max-privilege role:**

Name the role that holds the highest privilege level in this trace. If System Administrator (stock role) is present: it is automatically the T-4 role. If a custom role with organization-level access to security configuration or BU administration is present: name it and classify it as T-4.

Max-privilege role identified: _______

**Step 0b -- Binary justification gate:**

Answer exactly one of the two verdicts below. No other verdict is permitted. Narrative assessments that conclude ambiguously ("likely justified," "appears to be warranted," "reasonable given the context") do not satisfy this gate.

**Verdict options:**
- **JUSTIFIED** -- the max-privilege role is required because [the specific system operation required by {{topic}} cannot be performed with a lower tier role, and this is demonstrated by...]
- **NOT JUSTIFIED** -- the max-privilege role is not required; the operations in {{topic}} can be performed with [specific T-3 or T-2 role with documented capability]. The System Administrator assignment should be replaced with [specific alternative role].

> **Q:** Is the System Administrator (or equivalent T-4 max-privilege role) justified for this trace?
> **A:** [JUSTIFIED / NOT JUSTIFIED] -- select one, no middle ground
> **Evidence:** I checked [named operations in {{topic}} that are claimed to require T-4] against [T-3 capabilities: security role scoping, team management, record-level assignment] -- [result] because [specific reason T-3 is or is not sufficient for each operation examined]. The minimum tier required is T-[N] because [per-operation justification].

If NOT JUSTIFIED: add ESCALATION-PATH to the Gap Findings Table now (before Stage 1) with Severity = CRITICAL and Exact Fix = "Replace System Administrator assignment with [specific T-3 role] configured with [specific privileges]."

---

**GAP CATEGORY REGISTER (pre-committed -- complete before Stage 1)**

| Category | What It Catches |
|----------|----------------|
| FLS-EXPOSURE | Sensitive field without a field security profile |
| ESCALATION-PATH | Role reaches a higher tier through an available action |
| SHARING-CONFLICT | Sharing rule reopens access the OWD + role model intends to restrict |
| TEAM-GAP | Team-scoped operation with uncontrolled membership |
| CROSS-CASCADE | Relationship behavior grants unintended cross-entity access |
| OWD-MISMATCH | OWD broader than entity sensitivity warrants |

**Gap Findings Table -- do not populate now (except as directed in Section 0b). Return after Stage 3.**

| # | Category | Entity | Field (if FLS) | Role | Severity | Exact Fix |
|---|----------|--------|----------------|------|----------|-----------|

---

**SCOPE LEXICON (locked)**

`Org` / `BU` / `Parent-Child BU` / `Team:[name]` / `User` / `Sharing:[rule name]`

Non-token scope prose: mark **SCOPE-FAIL**, correct before advancing.

---

## STAGE 1 -- INVENTORY

**1a -- Ascending tier ladder:**

| Tier | Roles | Note |
|------|-------|------|
| T-1 (Read-Only) | | |
| T-2 (Operational) | | |
| T-3 (Elevated) | | |
| T-4 (Admin Ceiling) | [from Section 0 -- already justified or flagged] | Binary gate completed in Section 0 |

**1b -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) |
|--------|-----------------|-----------------------------------|

**1c -- Operation-role matrix (one table per entity):**

| Entity: [name] | Role | Tier | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|------|--------|------|-------|--------|--------|--------------|

All Record Scope cells: SCOPE LEXICON only. Mark any SCOPE-FAIL and correct before 1d.

**1d -- Field-level security gate:**

> **Q:** Does every sensitive field on every entity have a field security profile?
> **A:** [verdict per entity]
> **Evidence:** I checked Security > Field Security Profiles for [entity list] -- [per-entity result] because [profile name / no profile / no sensitive fields and fields reviewed: list].

| Entity | Field | Sensitivity | FLS Profile Name | Roles: Read | Roles: Write |
|--------|-------|-------------|-----------------|-------------|--------------|

---

## STAGE 2 -- GAP ANALYSIS

**Escalation gate:**

> **Q:** Can any role below T-4 reach T-4 privilege level through team membership, security role assignment, ownership reassignment, or BU configuration?
> **A:** [verdict]
> **Evidence:** I checked [role list] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-role result] because [per-role structural reason].

**Sharing conflict gate:**

> **Q:** Do any active sharing rules reopen access that the OWD + tier model intends to restrict?
> **A:** [verdict]
> **Evidence:** I checked sharing rules [list or "no rules"] for [entity list] -- [per-rule result] because [comparison to OWD + tier scope].

| Rule Name | Trigger | Access Opened | Record Scope | Overreach? |
|-----------|---------|---------------|--------------|------------|

**Team membership gate:**

> **Q:** Is team membership for every team-scoped role controlled in a way that prevents unauthorized tier elevation?
> **A:** [verdict]
> **Evidence:** I checked team [name] control -- [mechanism]; self-addition is [possible / not possible] because [specific constraint].

**OWD sensitivity gate:**

> **Q:** Is the OWD for each high-sensitivity entity appropriate?
> **A:** [verdict per entity]
> **Evidence:** I checked OWD for [entity] -- [token] -- [justified / unjustified] because [compensating controls or absence].

---

## STAGE 3 -- ROLE ASSESSMENT AND REMEDIATION

**Customer Service Representative gate:**

> **Q:** Does the CS role exceed its least-privilege scope for the CS job function?
> **A:** [JUSTIFIED / NOT JUSTIFIED] (binary for any privilege beyond T-1)
> **Evidence:** I checked CS access for [entity list, sensitive fields] -- [per-item result] because [FLS / role scope / OWD].

**Dataverse Security Expert gate:**

> **Q:** Does the Dataverse Security Expert hold only the privileges that a security configuration task requires?
> **A:** [JUSTIFIED / NOT JUSTIFIED] (binary for any T-4 or near-T-4 privileges)
> **Evidence:** I checked expert privileges beyond CS -- [excess or NONE] because [comparison to security task scope].

Both roles must appear by name with distinct specific observations.

**Least-privilege scoring:**

| Role | Tier | Persona | Excess Privileges | LP Score (0-10) | Binary Assessment |
|------|------|---------|-------------------|-----------------|-------------------|

Binary Assessment: JUSTIFIED (excess is documented) / NOT JUSTIFIED (excess must be removed).

**Attack scenario (if ESCALATION-PATH found):**
`Starting role (T-N) -> Action sequence -> Gained access (T-M)`. Abstract statements do not satisfy this section.

**Remediation gate:**

> **Q:** Does every entry in the Gap Findings Table have a specific Exact Fix naming the configuration object and post-fix state?
> **A:** [Yes -- verified / No -- complete now]
> **Evidence:** Every Exact Fix names [configuration object], current state, and target state.

Return to the Gap Findings Table and fill it in completely.

---

## V-05 -- Combined: Full v5 Structural Scaffold (C-21 + C-22 + C-23 + C-24)

**Axis:** All four v5 criteria wired as structural constraints into the full enforcement-marker scaffold from rubric v4 (C-11 through C-20)
**Hypothesis:** C-21--C-24 are tier-structure discipline enforcers that specialize the existing enforcement mechanism to the highest-risk decision points -- tier boundaries and max-privilege role assignments. They do not conflict with the write-time enforcement marker system (C-15--C-20) or the evidence-template gate system (C-12, C-14, C-16); they extend those systems to the new failure domain of tier-transition over-assignment. Wiring all four as structural rules in a prompt that already satisfies C-11--C-20 should produce a 100.00 trace: each constraint removes one failure mode that a partial scaffold leaves open.

---

You are running a permissions trace signal for: {{topic}}

---

## PREAMBLE -- EIGHT STRUCTURAL CONSTRAINTS (read before starting)

This trace enforces eight structural rules. Rules 1--4 are discipline enforcers from prior rubric versions. Rules 5--8 are the four new tier-structure constraints. Violating any rule produces a named inline marker -- correct it before advancing.

**Rule 1 (C-20 -- Enforcement-First):** This preamble is the trace's literal first output. No entity name, role name, or operation may appear before this section is complete.

**Rule 2 (C-11 -- Pre-Committed Register):** The Gap Category Register below is declared before any entity is enumerated. Categories are locked. Retroactive gap discovery without a pre-declared category is an inline failure.

**Rule 3 (C-13 -- Scope Token Lexicon):** Every Record Scope cell must use exactly one token from the SCOPE LEXICON below. Prose scope descriptions are **SCOPE-FAIL** -- mark and correct before advancing.

**Rule 4 (C-14 + C-16 -- Question-Form Evidence Gates):** Every critical security check appears as a question with a required answer. Every answer must use the template "Evidence: I checked [X] -- [result] because [Y]." A question without an answer, or an answer without Evidence, is **EVIDENCE-REQUIRED** -- mark and correct before advancing.

**Rule 5 (C-21 -- Ascending Tier Sequence):** Roles are organized into a named ascending tier ladder (T-1 through T-4 minimum) before any operation analysis begins. A flat unordered role list is a **TIER-FAIL** -- the tier structure must be declared and locked before Stage 1.

**Rule 6 (C-22 -- Tier-Gate Evidence Requirement):** At each T-N to T-N+1 boundary, an Evidence-template gate answer justifying the tier advance is required before assigning operations at the higher tier. A tier advance without a per-boundary Evidence gate is a **TIER-GATE-FAIL** -- state the evidence before continuing.

**Rule 7 (C-23 -- Named Inertia Temptation Anchors):** At each tier boundary, the specific over-privileged assignment that would be easiest at that boundary (the inertia temptation) is named, and an explicit rejection with stated reason is provided. An assignment without a named temptation and rejection is a **TEMPTATION-FAIL** -- name the temptation before the assignment.

**Rule 8 (C-24 -- Binary Privileged-Role Gate):** The T-4 max-privilege role (System Administrator or equivalent) requires a dedicated binary gate answered "JUSTIFIED" or "NOT JUSTIFIED" with Evidence-template content. Narrative hedging ("likely justified," "probably warranted") is a **VERDICT-FAIL** -- select one of the two binary verdicts.

---

## SECTION 0 -- T-4 BINARY GATE (Rule 8 -- must run before any other content)

Identify the max-privilege role in this trace.

> **Q:** Is the System Administrator (or equivalent T-4 role) JUSTIFIED for this trace?
> **A:** [JUSTIFIED / NOT JUSTIFIED -- binary, no other verdict]
> **Evidence:** I checked [named operations requiring T-4] against T-3 capabilities -- [result] because [per-operation justification: operation X requires system-level privilege Y, which T-3 cannot hold / alternatively, T-3 is sufficient for operation X because ...].

VERDICT-FAIL if the answer is not exactly "JUSTIFIED" or "NOT JUSTIFIED."

If NOT JUSTIFIED: add ESCALATION-PATH to Gap Findings Table with Severity = CRITICAL before proceeding.

---

## ENFORCEMENT MARKERS (active throughout this trace)

| Marker | Domain | Fires When | Correction Required |
|--------|--------|-----------|---------------------|
| **SCOPE-FAIL** | Scope | A Record Scope cell contains non-token prose | Replace with the correct SCOPE LEXICON token before advancing |
| **VERDICT-FAIL** | Verdict | A gate answer hedges, is absent, or contains more than two possible outcomes for a binary gate | Restate as a binary verdict (JUSTIFIED / NOT JUSTIFIED) or an explicit yes/no with Evidence |
| **EVIDENCE-REQUIRED** | Evidence | A gate answer lacks an "Evidence: I checked [X]..." line | Add the Evidence line before advancing; name the specific objects checked |
| **FLS-MISSING** | Field Security | A sensitive field has no FLS profile and no FLS-EXPOSURE row in the Gap Register | Add the FLS-EXPOSURE gap row now; do not advance past this entity |
| **TIER-FAIL** | Tier Structure | Roles appear in a flat unordered list without tier labels | Declare the ascending tier ladder before listing any role |
| **TIER-GATE-FAIL** | Tier Structure | A tier boundary is traversed without a per-boundary Evidence gate | State the Evidence-template justification for the tier advance before continuing |
| **TEMPTATION-FAIL** | Tier Structure | A role is assigned to a tier without naming and rejecting (or accepting with justification) the boundary's inertia temptation | Name the temptation from the Temptation Ledger and state the rejection reason |
| **GAP-FAIL** | Gap Detection | A gap type is discovered that is not in the pre-declared Gap Category Register | Add the category to the register; do not omit gaps because no category existed at analysis time |

Re-declare active markers at the start of each major section (Rule C-19 -- section-open reactivation).

---

## TEMPTATION LEDGER (pre-committed -- locked before Stage 1)

| Tier Boundary | Inertia Temptation | Why It Feels Easy | What It Costs |
|---------------|-------------------|-------------------|---------------|
| T-1 to T-2 | Grant Create + Write to all roles to simplify role maintenance | Fewer custom roles; fewer support tickets about missing access | Every role can create and modify records; over-write access expands blast radius on data errors |
| T-2 to T-3 | Grant Assign to any role that occasionally needs to redirect a record | Avoids configuring per-operation rules; fewer escalation requests | Assign enables record scope bypass; a T-2 role with Assign can redirect records to teams it controls, effectively expanding to Team-level scope |
| T-3 to T-4 | Grant System Administrator to avoid configuring field permission sets and sharing rules | Single role eliminates all access edge cases | System Admin bypasses record-level security, FLS, and team restrictions; every System Admin account is a complete privilege escalation terminal |

---

## SCOPE LEXICON (locked)

| Token | Meaning |
|-------|---------|
| `Org` | All records in the organization |
| `BU` | Records in the same business unit |
| `Parent-Child BU` | Records in the same BU and all child BUs |
| `Team:[name]` | Records owned by or shared to a named team |
| `User` | Only the user's own records |
| `Sharing:[rule name]` | Records via a named sharing rule |

---

## GAP CATEGORY REGISTER (pre-committed -- categories locked)

| Category | What It Catches |
|----------|----------------|
| FLS-EXPOSURE | Sensitive field readable/writable without a field security profile |
| ESCALATION-PATH | Role reaches a higher tier through an available action |
| SHARING-CONFLICT | Sharing rule reopens access the OWD + tier model intends to restrict |
| TEAM-GAP | Team-scoped operation with uncontrolled membership |
| CROSS-CASCADE | Relationship behavior grants unintended cross-entity access |
| OWD-MISMATCH | OWD broader than entity sensitivity warrants |

**Gap Findings Table -- do not populate now (except as directed). Return after Stage 3.**

| # | Category | Entity | Field (if FLS) | Role | Tier | Severity | Exact Fix |
|---|----------|--------|----------------|------|------|----------|-----------|

Severity: CRITICAL / HIGH / MEDIUM. Exact Fix: configuration object name + current state -> target state.

---

## STAGE 1 -- INVENTORY

Active markers: SCOPE-FAIL | VERDICT-FAIL | EVIDENCE-REQUIRED | FLS-MISSING | TIER-FAIL | TIER-GATE-FAIL | TEMPTATION-FAIL

**1a -- Ascending tier ladder (Rule 5 -- TIER-FAIL if omitted):**

Declare the tier structure before listing any role.

| Tier | Label | Privilege Boundary | Roles Assigned | Temptation Handled? |
|------|-------|-------------------|----------------|---------------------|
| T-1 | Read-Only Floor | Read within scope only | | N/A (floor) |
| T-2 | Operational | Create + Write within scope | | See T-1 to T-2 ledger |
| T-3 | Elevated | Assign + team/queue management | | See T-2 to T-3 ledger |
| T-4 | Admin Ceiling | Security role assignment + BU config | [from Section 0 -- binary gate completed] | See T-3 to T-4 ledger |

At each boundary (T-1->T-2, T-2->T-3):

> **BOUNDARY GATE T-N to T-N+1:** [TIER-GATE-FAIL if absent]
> **Temptation:** [from ledger -- name the specific temptation for this boundary] [TEMPTATION-FAIL if absent]
> **Rejection / Acceptance:** [Rejected because: [specific reason the temptation leads to over-privilege in this trace] / Accepted because: [justification + compensating control]] [TEMPTATION-FAIL if absent]
> **Q:** Do the roles assigned to T-N+1 require the capabilities that distinguish T-N+1 from T-N?
> **A:** [verdict per role]
> **Evidence:** I checked [role] function against T-N capability -- [result] because [specific operation required at T-N+1 that T-N cannot perform].

**1b -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) | Tiers with access |
|--------|-----------------|-----------------------------------|-------------------|

**1c -- Operation-role matrix by tier (one table per entity):**

| Entity: [name] | Role | Tier | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|------|--------|------|-------|--------|--------|--------------|

All Record Scope cells: SCOPE LEXICON only. SCOPE-FAIL if prose used. Correct before 1d.

Tier consistency: a role's operations must align with the tier definition. T-1 with Write = TIER-FAIL.

**1d -- Field-level security gate:**

> **Q:** Does every sensitive field on every entity have a field security profile?
> **A:** [verdict per entity]
> **Evidence:** I checked Security > Field Security Profiles for [entity list] -- [per-entity result] because [profile name / no profile / no sensitive fields and fields reviewed: list].

FLS-MISSING if sensitive field has no profile. Add FLS-EXPOSURE row immediately.

| Entity | Field | Sensitivity | FLS Profile Name | T-1: R/W | T-2: R/W | T-3: R/W | T-4: R/W |
|--------|-------|-------------|-----------------|----------|----------|----------|----------|

---

## STAGE 2 -- GAP ANALYSIS

Active markers: SCOPE-FAIL | VERDICT-FAIL | EVIDENCE-REQUIRED | TIER-GATE-FAIL

**Tier escalation gate:**

> **Q:** Can any role below T-4 reach T-4 privilege level through team membership, security role assignment, ownership reassignment, or BU configuration?
> **A:** [verdict]
> **Evidence:** I checked [role list] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-role result] because [per-role structural reason].

**Sharing conflict gate:**

> **Q:** Do any active sharing rules reopen access that the OWD + tier model intends to restrict?
> **A:** [verdict]
> **Evidence:** I checked sharing rules [list or "no rules found"] for [entity list] -- [per-rule result] because [comparison to OWD + tier scope].

| Rule Name | Trigger | Access Opened | Record Scope | Benefits Tier | Overreach? |
|-----------|---------|---------------|--------------|--------------|------------|

All Record Scope cells: SCOPE LEXICON only. SCOPE-FAIL if prose.

**Team membership gate:**

> **Q:** Is team membership for every team-scoped role controlled in a way that prevents unauthorized tier elevation?
> **A:** [verdict]
> **Evidence:** I checked team [name] control -- [mechanism]; self-addition is [possible / not possible] because [specific constraint].

**OWD sensitivity gate:**

> **Q:** Is the OWD for each high-sensitivity entity appropriate?
> **A:** [verdict per entity]
> **Evidence:** I checked OWD for [entity] -- [token] -- [justified / unjustified] because [compensating controls or absence].

**Cross-entity cascade gate:**

> **Q:** What is the lowest-privilege path to the highest-sensitivity entity, and is each hop intentional?
> **A:** [trace]
> **Evidence:** I traced [Role, T-N] -> [Entity A, Record Scope: token] -> [Relationship: type, cascade] -> [Entity B, Record Scope: token] -> [cascade] -> [Entity C, Record Scope: token] -- hop 1 [intentional/emergent because reason]; hop 2 [intentional/emergent because reason].

All Record Scope tokens: SCOPE LEXICON only.

---

## STAGE 3 -- ROLE ASSESSMENT AND REMEDIATION

Active markers: SCOPE-FAIL | VERDICT-FAIL | EVIDENCE-REQUIRED | TEMPTATION-FAIL

**Customer Service Representative gate:**

> **Q:** Does the Customer Service Representative operate at the correct tier with no excess privilege beyond the CS job function?
> **A:** [verdict + tier assignment]
> **Evidence:** I checked CS access for [entity list, sensitive fields] -- [per-item result] because [FLS / role scope / OWD].
> **Temptation reference:** [T-1-to-T-2 temptation from ledger] was [rejected because / accepted with compensating control]. TEMPTATION-FAIL if absent.

**Dataverse Security Expert gate:**

> **Q:** Does the Dataverse Security Expert hold only the privileges that a security configuration task requires, at the minimum tier justified?
> **A:** [verdict + tier assignment]
> **Evidence:** I checked expert privileges beyond CS -- [excess or NONE] because [comparison to security task scope].
> **Temptation reference:** [T-3-to-T-4 temptation from ledger] was [rejected because / accepted with compensating control]. TEMPTATION-FAIL if absent.

Both roles must appear by name with distinct specific observations, a tier assignment, and a Temptation Ledger reference.

**Least-privilege scoring:**

| Role | Tier | Persona | Excess Privileges | LP Score (0-10) | Over-Privileged? | Temptation Accepted? |
|------|------|---------|-------------------|-----------------|------------------|----------------------|

LP Score < 7 with accepted temptation: compensating control must be verified or acceptance reversed.

**Attack scenario (if ESCALATION-PATH found):**
`Starting role (T-N) -> Action sequence -> Gained access (T-M)`. Abstract risk statements do not satisfy this section.

**Remediation gate:**

> **Q:** Does every entry in the Gap Findings Table have a specific Exact Fix naming the configuration object and post-fix state?
> **A:** [Yes -- verified / No -- complete now]
> **Evidence:** Every Exact Fix row names [configuration object], current state, and target state. Format: "Change [object] in [solution location] from [current] to [target]. Post-fix: [audit verification step]."

Return to the Gap Findings Table and fill it in completely. Every row must fit a pre-declared category. Every Exact Fix must name the object.
