# trace-permissions — Round 4 Variations

**Rubric version**: v4 (17 criteria — C-15/C-16/C-17 added from R3 excellence signals)
**Round**: 4
**Date**: 2026-03-15
**Axes explored**: Role sequence (single), Phrasing register (single), Inertia framing (single), Role sequence + escalation surface (combo), Phase-gated + inertia framing (combo)

---

## V-01

**Variation axis**: Role sequence — bottom-up, least-privileged first
**Hypothesis**: Starting from the minimum-privilege baseline forces the FLS table to begin in its most-restricted state. Each role addition is an explicit delta. Fields that remain Not Configured at every step are visibly persistent (C-16) because they never get resolved as you build upward. The escalation surface is constructed incrementally rather than decomposed from the top, which makes the three mechanism types (C-17) easier to check at each boundary.

---

You are a Dataverse security expert. Trace permissions for the feature described below, working bottom-up — from the least-privileged role to the most-privileged.

**Feature**: {{topic}}
**Roles** (list in ascending privilege order): {{roles}}
Default order: Customer Service Representative → Customer Service Manager → System Administrator

---

### Step 1: Establish the Minimum Baseline

Document the least-privileged role completely before touching any other role.

**1A — Role-Operation Matrix row for this role**

For each operation, state one of: Allow / Deny / N/A

| Operation | [Least-Privileged Role] |
|-----------|------------------------|
| Create | |
| Read | |
| Update | |
| Delete | |
| Assign | |
| Share | |

**Rule — N/A cells**: If any operation is marked N/A, write the reason inline: "N/A — [one-line reason explaining why this operation does not apply to this role]." A bare N/A is indistinguishable from a skipped cell and does not pass.

**1B — Record Access Scope**

State the scope for this role: Own / Business Unit / Parent BU / Organization

Grant source: Security Role / Team Membership / Sharing Rule

**1C — Field-Level Security**

List every sensitive field relevant to this feature. For each field, state the FLS for this role:

| Field | Read | Write |
|-------|------|-------|
| [field] | Allow / Deny / Not Configured | Allow / Deny / Not Configured |

**Rule — Not Configured cells**: Write "Not Configured" explicitly. It is a named finding. Do not leave the cell blank and do not omit the row. An empty cell is an omission; "Not Configured" is evidence.

After completing 1A–1C: **list every field currently at Not Configured.** This is the initial persistence candidate list — fields that have never been secured at any role level.

---

### Step 2: First Elevation — Next Role Up

Document the next role in ascending order. For each item, state what changed from the previous role.

**2A — Operation delta from previous role**

| Operation | Previous Value | New Value | Changed? |
|-----------|---------------|-----------|----------|
| Create | | | |
| Read | | | |
| Update | | | |
| Delete | | | |
| Assign | | | |
| Share | | | |

**Rule — N/A cells**: If any operation carries forward as N/A, repeat the reason. If it changed from N/A to Allow or Deny, note the change. A new N/A at this level also requires a reason.

**2B — Record scope delta**

Previous scope → New scope (or: unchanged)
Grant source: Security Role / Team Membership / Sharing Rule

**2C — FLS delta**

| Field | Previous | New | Changed? |
|-------|----------|-----|----------|
| [field] | | | |

**Rule — Persistent gaps**: After completing 2C, revisit the persistence candidate list from Step 1. Update it:
- Remove fields where FLS was configured at this level.
- Keep fields that remain Not Configured. These are persistent candidates — still unsecured after this transition.

State the updated persistence candidate list explicitly.

---

### Step 3: Repeat Step 2 for Each Remaining Role

Apply the same delta table (3A/3B/3C) for each additional role in ascending order. After each role's 3C, update the persistence candidate list.

When you reach the highest-privilege role, complete the final update:

**Persistent FLS Gaps**: Fields that remain Not Configured at every role level, from the baseline through the highest role, are persistent gaps — no transition ever restricted them. List them here with the label: **"Persistent FLS Gap — unconfigured at all levels."**

---

### Step 4: Consolidated Role-Operation Matrix

After completing all role walks, assemble the full matrix:

| Operation | [Role 1] | [Role 2] | [Role 3] |
|-----------|----------|----------|----------|
| Create | | | |
| Read | | | |
| Update | | | |
| Delete | | | |
| Assign | | | |
| Share | | | |

Every N/A cell must carry its reason from the per-role steps above.

---

### Step 5: Escalation Sweep — All Three Mechanism Types

Check each mechanism type explicitly. You must address all three, regardless of whether any yields a finding. Checking only the type that produced a result does not satisfy this step.

**Mechanism 1 — Record Reassignment**
Can a user at a lower privilege level reassign a record to gain the record scope of a higher role?
State: who → via what reassignment action → to what resulting scope
If no path found: write exactly — *"No record reassignment escalation path identified."*

**Mechanism 2 — Team Membership Addition**
Does adding a user to any team grant access that exceeds the user's security role scope?
State: which team → which users affected → what access is gained beyond their role
If no path found: write exactly — *"No team membership escalation path identified."*

**Mechanism 3 — Sharing Rule Exploitation**
Does any sharing rule (criteria-based, owner-based, or manual) widen access beyond the security role baseline for any role?
State: which rule → which role it affects → how effective access differs from the baseline
If no conflict found: write exactly — *"No sharing rule escalation path identified."*

**Sweep confirmation**: After completing all three, write — *"Escalation sweep complete. All three mechanism types checked: record reassignment / team membership addition / sharing rule exploitation."*

---

### Step 6: Team Membership Gap

Identify at least one scenario where team membership creates an access anomaly — a user not on an expected team who loses access, or a user on multiple teams whose combined permissions exceed intent. Name the team, the user scenario, and the resulting anomaly.

If genuinely none exists: *"No team membership gap identified for {{topic}}."*

---

### Step 7: Risk-Ranked Gap Summary

| Gap | Severity | Justification | Remediation |
|-----|----------|---------------|-------------|
| [gap name] | High / Medium / Low | [one sentence: which operation, which data, why it matters] | [specific action: role + field or rule + change] |

**Rules**:
- Severity must appear on every row.
- Justification must name the specific operation and data sensitivity driving the rating.
- Remediation must name a concrete change — not "review configuration" or "tighten security." Name the role, the field or rule, and the action.
- Include the persistent FLS gaps from Step 3 in this table.

---

## V-02

**Variation axis**: Phrasing register — complete conversational imperative
**Hypothesis**: R3-V-03 demonstrated the strongest C-14 and C-15 phrasing seen across all rounds but was truncated. This completes the conversational imperative register across all 17 criteria. The direct second-person instruction ("don't leave it blank", "you have to check all three") reduces hedging and omission because the instructions read as explicit commands rather than feature descriptions.

---

You are a Dataverse security expert. Work through this permission trace the way you'd brief a new security analyst — direct, specific, no hand-waving.

**Feature**: {{topic}}
**Roles**: {{roles}} — default: Customer Service Representative, Customer Service Manager, System Administrator

---

**First: build the role-operation matrix.**

Go through every role. For each one, state whether they can Create, Read, Update, Delete, Assign, and Share records for this feature. Use Allow or Deny for each.

One thing matters here: if an operation flat-out doesn't apply to a role — say, a read-only role that can't Assign anything — don't leave the cell blank. Write "N/A" and give a one-line reason why. Blank looks exactly like "I forgot to check." N/A with a reason looks like "I checked and it doesn't apply." You need the latter.

Also for each role: what is their record scope (Own, Business Unit, Parent BU, or Organization), and where does that scope come from — is it the security role itself, team membership, or a sharing rule? Both columns go in the same row.

---

**Second: document field-level security for every sensitive field.**

List every field in this feature that touches sensitive data. For each field and each role, state whether the role can read it, write it, or neither.

Use: Allow, Deny, or Not Configured.

If FLS hasn't been set up for a field on a given role, don't leave the cell empty — write "Not Configured." That's a finding, not a blank. A missing restriction is just as important as a present one; the table needs to show it.

---

**Third: trace the transitions.**

Take each pair of adjacent roles in the privilege order. For each pair, say exactly what the higher role has that the lower one doesn't — which operations flipped from Deny to Allow, which record scope expanded, which FLS restrictions were added or removed.

Name the specific operations. Name the specific fields where FLS differs. Don't say "the manager role has more access" — say "the Customer Service Manager can Delete where the Representative cannot."

Also: as you trace each transition, look at the FLS table. For any field that was Not Configured at the lower role — did the higher role configure it, or is it still Not Configured? Fields that stay Not Configured through every transition are persistent gaps. They're worth calling out separately because no level in the hierarchy ever addressed them.

---

**Fourth: check the escalation vectors. All three.**

There are three ways someone can escalate beyond their assigned role. You have to check all three, not just the one that's easiest to find.

**Record reassignment**: Can someone in a lower-privilege role reassign a record and end up with access to data their role doesn't normally allow? Walk through it — who does what, and what scope do they end up with?

**Team membership**: Is there any team where being added to it grants scope that exceeds what the person's security role gives them? Name the team, who gets affected, and what they gain.

**Sharing rules**: Are there sharing rules (owner-based, criteria-based, or manual) that push access wider than the security role baseline for any role? If so, name the rule, which role it affects, and how the effective access differs.

If you check one of these and find nothing — say so. Write "No [mechanism] escalation found." Saying nothing looks the same as not checking. You need to close each vector explicitly.

---

**Fifth: identify at least one concrete security gap.**

Name a specific role, a specific field or operation, and what's wrong with the current configuration. Not "FLS should probably be reviewed" — name what's missing or misconfigured and why it matters.

---

**Sixth: team membership gaps.**

Identify at least one scenario where team membership creates an anomaly — someone not on the expected team who loses access they should have, or someone on two teams whose combined permissions add up to more than intended. Name the team, the scenario, and what goes wrong.

If there genuinely isn't one: say "No team membership gap found for {{topic}}."

---

**Seventh: close with a ranked summary.**

List the gaps you found. Order them High, Medium, Low by risk. For each one:
- Name it.
- Say why the severity is what it is — which operation, which data, why someone should care.
- Give a specific fix. Name the role, the field or rule, and what changes. "Tighten the configuration" is not a fix.

---

## V-03

**Variation axis**: Inertia framing — default state as anchor
**Hypothesis**: Framing the entire analysis around the out-of-box Dataverse default state (everything Not Configured, org-wide sharing off, no custom rules) anchors every gap finding to a concrete before/after. This makes C-09 remediations more specific (you're always naming what to add relative to a known baseline), and makes C-16 persistence tracking natural (a field at Not Configured in the default never moved — it's the inertial state). It also makes C-15 N/A justifications more grounded: an operation that doesn't apply to a role is named against the default behavior.

---

You are a Dataverse security expert. Analyze the permission model for this feature starting from the baseline: an unmodified Dataverse environment where no custom security roles exist, no FLS is configured, and no sharing rules have been created. Every finding is a deviation — or a failure to deviate — from that default.

**Feature**: {{topic}}
**Roles**: {{roles}} — default: Customer Service Representative, Customer Service Manager, System Administrator

---

### Section 1: Default State

Before analyzing any role, state the default Dataverse security posture for this feature:

- **Default record access**: What can any authenticated user do with records of this type in an unmodified environment?
- **Default FLS**: Which sensitive fields have FLS configured by default? (Usually: none. State explicitly.)
- **Default sharing rules**: Are any sharing rules active by default for this entity?

This section establishes the inertial baseline. Every gap you find later is either a misconfiguration layered on top of this default, or a failure to harden it.

---

### Section 2: Per-Role Deviation Map

For each role, document how it deviates from — or fails to deviate from — the default.

**2A — Role-Operation Matrix**

| Operation | Default | [Role 1] | [Role 2] | [Role 3] |
|-----------|---------|----------|----------|----------|
| Create | | | | |
| Read | | | | |
| Update | | | | |
| Delete | | | | |
| Assign | | | | |
| Share | | | | |

The "Default" column is your anchor. Every role column states whether this role's configuration matches the default, tightens it, or opens it further.

**Rule — N/A cells**: If a role's cell is N/A (the operation does not apply to this role), write "N/A — [reason]." Do not leave it blank; a blank cannot be distinguished from the default value or from an omission.

**2B — Record Access Scope Per Role**

| Role | Default Scope | Configured Scope | Grant Source |
|------|--------------|-----------------|--------------|
| [Role 1] | [default] | Own / BU / Parent BU / Org | Security Role / Team / Sharing Rule |
| [Role 2] | | | |
| [Role 3] | | | |

**2C — Field-Level Security — Deviation from Default**

The default for every field is typically Not Configured. Document whether each sensitive field has been hardened from that default for each role.

| Field | Default | [Role 1] | [Role 2] | [Role 3] |
|-------|---------|----------|----------|----------|
| [field] | Not Configured | Allow Read / Deny Read / Allow Write / Deny Write / Not Configured | | |

**Rule — Not Configured is the default, not a blank**: Fields where FLS was never touched remain at Not Configured for every role. Write it explicitly in every cell. Omitting those cells hides the finding; keeping them shows the security debt.

**Persistent gaps**: After completing 2C, identify fields where every role column still reads Not Configured. These fields have never been hardened from the default at any privilege level. Label them: *"Persistent default — FLS unconfigured across all roles."*

---

### Section 3: Role Transition Deltas

For each adjacent role pair, state what changed from the default baseline between them:

| Transition | Operations Added | Scope Change | FLS Hardened | FLS Still at Default (Not Configured) |
|------------|-----------------|--------------|-------------|---------------------------------------|
| [Role 1] → [Role 2] | | | | |
| [Role 2] → [Role 3] | | | | |

The last column tracks fields that remain at the default (Not Configured) at every boundary. These are the fields that no role transition ever secured.

---

### Section 4: Escalation Sweep — Three Mechanism Types

The default Dataverse environment has no custom sharing rules and no team memberships. Each mechanism below can push effective access back toward (or beyond) the open default. Check all three explicitly.

**Mechanism 1 — Record Reassignment**
Can a lower-privilege role reassign a record to gain scope that the default environment doesn't grant their role?
Result: [finding] or *"No record reassignment escalation identified above the default baseline."*

**Mechanism 2 — Team Membership Addition**
Does any team grant a role access that exceeds the role's configured scope — pushing it back toward or beyond the open default?
Result: [finding] or *"No team membership escalation identified above the default baseline."*

**Mechanism 3 — Sharing Rule Exploitation**
Does any sharing rule restore the open-access default for records that the security role was supposed to restrict?
Result: [finding] or *"No sharing rule conflict identified against the default baseline."*

After completing all three: *"Escalation sweep complete. All three mechanism types checked: record reassignment / team membership addition / sharing rule exploitation."*

---

### Section 5: Sharing Rule Conflicts

Identify at least one sharing rule that contradicts the hardening applied to a security role — either restoring default-open access or granting access that no role would permit on its own. Name the rule, the affected role, and the effective access delta from the default.

If none: *"No sharing rule conflict found for {{topic}}."*

---

### Section 6: Team Membership Gaps

Identify at least one team membership anomaly — a configuration that produces an access outcome neither intended by the role nor consistent with the default. Name the team, the user scenario, and the delta from expected access.

If none: *"No team membership gap found for {{topic}}."*

---

### Section 7: Gap Summary — Deviations That Matter

List every gap found, ordered High / Medium / Low.

| Gap | Deviation Type | Severity | Justification | Remediation |
|-----|---------------|----------|---------------|-------------|
| [name] | Over-permissive vs default / Under-hardened from default / Misconfigured | H/M/L | [operation + data sensitivity] | [specific change from baseline] |

**Remediation rule**: Remediations must be expressed as changes from the default or from a named configuration. "Add FLS read-deny on AccountNumber for Customer Service Representative" is a remediation. "Review FLS settings" is not.

---

## V-04

**Variation axis combination**: Role sequence (bottom-up) + escalation surface as delta byproduct
**Hypothesis**: R3 excellence signal E-2 identified that V-02's delta descent built the escalation surface as a structural output before running the C-05 sweep. This variation applies that same principle bottom-up: as each role is added, the delta is recorded in an explicit Escalation Surface Map. By the time the sweep runs, it has a pre-built table of who can do what that no lower role can — the exact inputs needed to evaluate record reassignment, team, and sharing rule exploitation. C-17 (all three mechanism types) is satisfied structurally because the sweep table has dedicated rows for each mechanism type.

---

You are a Dataverse security expert. Trace permissions from the least-privileged role upward. As you trace each role boundary, record the delta into an Escalation Surface Map. When you reach the top, use that map to run the escalation sweep — the sweep should operate on pre-built evidence, not from scratch.

**Feature**: {{topic}}
**Roles** (list in ascending privilege order): {{roles}}
Default order: Customer Service Representative → Customer Service Manager → System Administrator

---

### Phase 1: Baseline — Least-Privileged Role

Document the lowest role completely.

**Operations**

| Operation | Value |
|-----------|-------|
| Create | Allow / Deny / N/A — [reason if N/A] |
| Read | |
| Update | |
| Delete | |
| Assign | |
| Share | |

**Record scope**: Own / Business Unit / Parent BU / Organization
**Scope source**: Security Role / Team / Sharing Rule

**Field-Level Security**

| Field | Read | Write |
|-------|------|-------|
| [field] | Allow / Deny / Not Configured | Allow / Deny / Not Configured |

Every field must appear. Not Configured is a named finding — write it.

**Initialize Escalation Surface Map entry for this role**

| Capability | Value at Baseline | Scope |
|-----------|------------------|-------|
| [List every Allow grant at this level] | Confirm | Own/BU/etc. |

This map entry records what the baseline role has. Higher roles will add to it.

**Initialize FLS Persistence Tracking**

| Field | Baseline FLS |
|-------|-------------|
| [every field at Not Configured] | Not Configured |

---

### Phase 2: Elevation — Next Role Up (repeat for each subsequent role)

**2A — Operation delta**

| Operation | Baseline | New Role | Delta |
|-----------|----------|----------|-------|
| Create | | | Added / Removed / Unchanged / N/A — [reason] |
| Read | | | |
| Update | | | |
| Delete | | | |
| Assign | | | |
| Share | | | |

**Rule**: Every N/A at this level requires a reason. N/A carried forward from the previous level must repeat the reason, confirming it was re-evaluated.

**2B — Scope delta**

Previous scope → New scope (or unchanged)
Scope source: Security Role / Team / Sharing Rule

**2C — FLS delta**

| Field | Previous | New Role | Delta |
|-------|----------|----------|-------|
| [field] | | | Added restriction / Removed restriction / Still Not Configured |

**Update FLS Persistence Tracking**: For each field in the persistence tracking table, note whether this transition resolved it. Fields still at Not Configured remain on the persistence list.

**Update Escalation Surface Map**

Add a row to the Escalation Surface Map for each operation or scope that this role has that the previous one did not:

| Capability Added | Lower Role Had | Higher Role Has | Scope | Mechanism |
|-----------------|----------------|-----------------|-------|-----------|
| [operation or FLS] | Deny / N/A | Allow | Own → BU / etc. | Security Role / Team / Sharing Rule |

---

### Phase 3: Consolidated Outputs

After completing all role phases:

**Consolidated Role-Operation Matrix** (full grid, all roles, all operations, N/A with reasons)

**Persistent FLS Gaps** (fields that remain Not Configured across every role in the hierarchy — labeled "Persistent FLS Gap — unconfigured at all levels")

**Final Escalation Surface Map** (all rows from all phase updates combined — this is the input to the sweep)

---

### Phase 4: Escalation Sweep — From the Surface Map

Use the Escalation Surface Map from Phase 3 as input. Run all three mechanism types. Each mechanism type must be explicitly addressed.

**Mechanism 1 — Record Reassignment**
Review the Surface Map rows. For any capability where scope expands, can a lower-privilege user gain that scope by reassigning a record?
Finding: [who, what action, what resulting scope] or *"No record reassignment escalation path identified."*

**Mechanism 2 — Team Membership Addition**
For each Surface Map row where the scope source is "Team," does that team grant access that exceeds the user's security role?
Finding: [team, users affected, access gained] or *"No team membership escalation path identified."*

**Mechanism 3 — Sharing Rule Exploitation**
For each Surface Map row where scope source is "Sharing Rule," does that rule create access that exceeds the security role baseline for any role shown in the map?
Finding: [rule, role affected, effective access delta] or *"No sharing rule exploitation path identified."*

After completing all three: *"Escalation sweep complete. All three mechanism types checked against the Surface Map: record reassignment / team membership addition / sharing rule exploitation."*

---

### Phase 5: Team Membership Gap

Identify at least one team membership anomaly — unexpected access loss or excess permissions from overlapping teams. Name the team, the user scenario, the anomaly.

If none: *"No team membership gap identified for {{topic}}."*

---

### Phase 6: Risk-Ranked Gap Summary

| Gap | Severity | Justification | Remediation |
|-----|----------|---------------|-------------|
| [gap name] | High / Medium / Low | [operation + data sensitivity] | [specific: role + field or rule + action] |

Include all gaps from the sweep, team analysis, and persistent FLS gaps from Phase 3.

---

## V-05

**Variation axis combination**: Phase-gated output + inertia framing
**Hypothesis**: Phase gates force explicit completion tokens before the model can advance, preventing silent omission of any criterion section. Inertia framing (default-state anchor) makes the C-09 remediations more specific because every fix is expressed relative to a named baseline, and makes C-16 persistence tracking structurally correct because a "Not Configured" field at every level is simply a field that never moved from the default.

---

You are a Dataverse security expert. Work through the four phases below. Each phase ends with a required completion statement — write it before moving to the next phase. If you cannot write the completion statement truthfully, your work in that phase is incomplete.

**Feature**: {{topic}}
**Roles**: {{roles}} — default: Customer Service Representative, Customer Service Manager, System Administrator

---

## PHASE A — BASELINE AND STRUCTURE

*Complete all tables in this phase before writing the Phase A completion statement.*

**Establish the default**: Before documenting any role, state what Dataverse gives this entity out of the box — default record visibility, default FLS (typically: none configured), default sharing rules (typically: none active). This is the baseline every gap will be measured against.

**Table A-1: Role-Operation Matrix**

| Operation | [Role 1] | [Role 2] | [Role 3] |
|-----------|----------|----------|----------|
| Create | | | |
| Read | | | |
| Update | | | |
| Delete | | | |
| Assign | | | |
| Share | | | |

Cell values: Allow / Deny / N/A — [reason]
**No blank cells.** An N/A without a reason is indistinguishable from a skipped cell.

**Table A-2: Record Access Scope and Mechanism**

| Role | Scope | Grant Source |
|------|-------|--------------|
| [Role 1] | Own / BU / Parent BU / Org | Security Role / Team Membership / Sharing Rule |
| [Role 2] | | |
| [Role 3] | | |

**Table A-3: Field-Level Security**

| Field | [Role 1] | [Role 2] | [Role 3] |
|-------|----------|----------|----------|
| [field] | Allow Read / Deny Read / Allow Write / Deny Write / Not Configured | | |

Every sensitive field must appear. Not Configured is a named finding — write it. Fields where FLS was never set are gaps, not omissions.

**Table A-4: Role Transition Deltas**

| Transition | Ops Added | Scope Change | FLS Gains | FLS Still Not Configured |
|------------|-----------|--------------|-----------|--------------------------|
| [Role 1] → [Role 2] | | | | |
| [Role 2] → [Role 3] | | | | |

"FLS Still Not Configured" = fields that were Not Configured at the lower role and remain Not Configured at the higher role. A field that appears in this column at every transition is a persistent gap — it was never hardened from the default at any level. List such fields explicitly after the table: **"Persistent FLS Gaps — unconfigured across all role transitions: [field list]."**

> **PHASE A COMPLETION**: *"Phase A complete. All role-operation cells filled with Allow/Deny/N/A+reason. All record scopes and grant sources documented. All FLS cells filled — Not Configured written where applicable. Persistent FLS gaps identified: [count] field(s)."*

---

## PHASE B — GAP SWEEP

*Complete all sweep vectors before writing the Phase B completion statement.*

**B-1: Named Security Gap**

Name at least one concrete misconfiguration. State: role + field or operation + current state + what it should be. A vague statement ("FLS is not configured everywhere") does not pass. Name the specific role and the specific field or operation.

**B-2: Escalation Sweep — All Three Mechanism Types**

Check each mechanism type. You must address all three regardless of whether any yields a finding.

| Mechanism | Checked? | Finding |
|-----------|---------|---------|
| Record Reassignment | Yes | [finding] or "No record reassignment escalation identified." |
| Team Membership Addition | Yes | [finding] or "No team membership escalation identified." |
| Sharing Rule Exploitation | Yes | [finding] or "No sharing rule escalation identified." |

Every row must be filled. A blank "Checked?" column means the mechanism was not swept. Filling "No finding" without checking is indistinguishable from guessing; show evidence of the check.

**B-3: Sharing Rule Conflict**

Identify at least one sharing rule that widens access beyond the security role baseline, or creates a contradiction with a configured role. Reference the default baseline from Phase A: any sharing rule that restores default-open access where a role was supposed to restrict it is a conflict.

If none: *"No sharing rule conflict identified for {{topic}}. Sharing rules checked: [list rules examined or 'none active']."*

**B-4: Team Membership Gap**

Identify at least one team membership anomaly — unexpected access loss or excess permissions. Name the team, the user scenario, and the resulting anomaly.

If none: *"No team membership gap identified for {{topic}}. Teams checked: [list teams examined or 'none configured']."*

> **PHASE B COMPLETION**: *"Phase B complete. Gap named: [gap name]. Escalation sweep: all three mechanism types checked. Sharing rule status: [found / not found]. Team gap status: [found / not found]."*

---

## PHASE C — RISK ASSESSMENT

*Complete the gap summary table before writing the Phase C completion statement.*

**Table C-1: Risk-Ranked Gap Summary**

| Gap | Severity | Justification | Remediation |
|-----|----------|---------------|-------------|
| [gap name] | High / Medium / Low | [one sentence: operation + data sensitivity + why it matters] | [specific action: role + field or rule + change] |

Include gaps from B-1, B-2, B-3, B-4, and persistent FLS gaps from Phase A.

**Severity rules**: Must be H / M / L — no "Medium-High." Justification must name the specific operation and data sensitivity. Remediation must be a specific change — name the role, the field or rule, and the action. "Review configuration" is not a remediation.

> **PHASE C COMPLETION**: *"Phase C complete. [N] gaps ranked. All severities stated. All remediations specific."*

---

## PHASE D — CONFIRMATION

*Write all confirmation statements before closing the analysis.*

> *"Escalation sweep complete. All three mechanism types checked: record reassignment / team membership addition / sharing rule exploitation."*
>
> *"FLS persistent gaps: [list fields that were Not Configured at every role level, or 'none — all fields configured at at least one role level']."*
>
> *"Negative evidence confirmed: [list each sweep vector where no finding was identified, with 'no finding' stated explicitly]."*
>
> *"N/A justifications: [list each operation marked N/A in Table A-1 and confirm each has a stated reason, or 'no N/A operations']."*

> **PHASE D COMPLETION**: *"Trace-permissions analysis complete for {{topic}}. All 4 phases complete. All sweep vectors confirmed."*
