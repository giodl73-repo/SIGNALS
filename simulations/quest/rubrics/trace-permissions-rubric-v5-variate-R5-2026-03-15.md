# trace-permissions — Round 5 Variations

**Rubric version**: v5 (19 criteria — C-18/C-19 added from R4 excellence signals V-01, V-02)
**Round**: 5
**Date**: 2026-03-15
**Axes explored**: C-19 anti-pattern inline annotation (single), Audit form output format (single), Formal/technical specification register (single), C-18 anchor + C-19 anti-pattern naming (combo), Bottom-up + C-19 anti-pattern naming (combo)

**Scoring formula change from R4**: Aspirational denominator is now 12 (not 10). Max aspirational = (pass_count / 12) × 10.

---

## V-01

**Variation axis**: C-19 anti-pattern naming — inline at every instruction
**Hypothesis**: R4-V-02 named a few anti-patterns ("tighten security fails the register," "rank them, don't just list them") and those were the excellence signals that produced C-19 as a new criterion. This variation makes anti-pattern naming the sole axis: every instruction block ends with a "What does NOT satisfy this step" note. C-19 becomes structural — the prompt itself demonstrates anti-pattern naming at more than two criteria, so the output must reproduce those named failure modes to accurately describe what it did. C-18 is captured by making Step 0 a required declaration with its own anti-pattern note. The base structure is neutral (standard section progression) so no other axis contaminates the signal.

---

You are a Dataverse security expert. Produce a complete permission trace for the feature described below. At each step, this prompt names what does NOT satisfy that step alongside what does.

**Feature**: {{topic}}
**Roles**: {{roles}} — default: Customer Service Representative, Customer Service Manager, System Administrator

---

### Step 0: Declare the Baseline Zero-Point

Before naming any role's permissions, declare the starting state:

- What operations does any authenticated user have on this entity type before any role is assigned?
- What FLS is configured by default for sensitive fields in this feature? (Typically: none.)
- What sharing rules are active by default?

This is the permission state that exists before your analysis begins. Every gap you find is either a deviation from this baseline that should not exist, or a failure to deviate from it that should have been addressed.

**Does NOT satisfy this step**: Beginning the analysis with "Customer Service Representative can Create records..." without first establishing the zero-permission baseline. An analysis that starts mid-hierarchy cannot prove that unconfigured fields are gaps rather than omissions — the reader has no zero-point to measure against.

---

### Step 1: Role-Operation Matrix

Build a complete role-operation matrix. Every role appears as a column. Every operation appears as a row: Create, Read, Update, Delete, Assign, Share. Use Allow or Deny. If an operation is N/A for a role, write "N/A — [one-line reason]".

| Operation | [Role 1] | [Role 2] | [Role 3] |
|-----------|----------|----------|----------|
| Create    |          |          |          |
| Read      |          |          |          |
| Update    |          |          |          |
| Delete    |          |          |          |
| Assign    |          |          |          |
| Share     |          |          |          |

For each role also state:
- **Record access scope**: Own / Business Unit / Parent BU / Organization
- **Scope grant source**: Security Role / Team Membership / Sharing Rule

**Does NOT satisfy the matrix**: A prose list of role capabilities ("the manager can update and delete"). The matrix must be structured so that every role/operation intersection is explicit — prose cannot be scanned for omissions. An omitted column or row does not pass. A blank N/A cell without a reason does not pass — it is indistinguishable from a skipped analysis.

**Does NOT satisfy scope documentation**: Naming only the scope level without the source ("BU scope" with no source named). Without the source, the analysis cannot identify whether the scope was tightened by role configuration or widened by a team or sharing rule — which is precisely what gap analysis requires.

---

### Step 2: Field-Level Security

For each sensitive field relevant to this feature, state the FLS per role using: Allow, Deny, or Not Configured.

| Field    | [Role 1] | [Role 2] | [Role 3] |
|----------|----------|----------|----------|
| [field]  |          |          |          |

**Does NOT satisfy this step**: Cells left blank. Blank and "Not Configured" are not the same — blank is an omission, "Not Configured" is a finding. Writing "FLS applies to this feature" or "FLS should be restricted for sensitive fields" without naming which role has what permission on which specific field does not pass. Describing only fields that have restrictions hides the security debt — unconfigured fields are the gaps.

---

### Step 3: Role Transition Deltas

For each adjacent role pair, state exactly what the higher role has that the lower role does not: which operations changed, whether scope expanded, which FLS restrictions were added or remained Not Configured.

| Transition           | Operations Added | Scope Change | FLS Resolved | FLS Still Not Configured |
|----------------------|-----------------|--------------|-------------|--------------------------|
| [Role 1] → [Role 2]  |                 |              |             |                          |
| [Role 2] → [Role 3]  |                 |              |             |                          |

After completing this table: list any field that appears in "FLS Still Not Configured" at every transition. Label them: *"Persistent FLS Gap — unconfigured at all levels."*

**Does NOT satisfy delta tracking**: Describing each role in isolation without a comparison ("Role A: Allow/Deny/Deny... Role B: Allow/Allow/Deny..."). Saying "Role B has more access than Role A" without naming the specific operations or fields that differ does not pass. The delta column must exist and must name the specific change at each boundary.

**Does NOT satisfy persistent gap identification**: Noting per-cell that a field is Not Configured. Persistence requires cross-role visibility — a field at Not Configured at every transition is categorically different from a gap that exists at one level and is resolved at the next.

---

### Step 4: Named Security Gap

Before the sweep: name at least one concrete security misconfiguration. State the role, the field or operation, and the specific problem.

**Does NOT satisfy this step**: "FLS is not comprehensively configured across all roles." A general observation is not a finding. Name a specific role and a specific field or operation. The gap must be concrete enough to generate a remediation action without asking a follow-up question.

---

### Step 5: Escalation Sweep — All Three Mechanism Types

Check all three escalation vectors. Address each one regardless of whether it yields a finding.

**Mechanism 1 — Record Reassignment**
Can a user at a lower privilege level reassign a record to gain scope their role does not normally allow? State: who → via what action → resulting scope.
If no path: write exactly — *"No record reassignment escalation path identified."*

**Does NOT satisfy Mechanism 1**: Silence. Not mentioning this mechanism is indistinguishable from not checking it. Finding an escalation path under Mechanism 2 and not addressing Mechanism 1 does not pass.

**Mechanism 2 — Team Membership Addition**
Does adding a user to any team grant scope that exceeds the user's security role? State: team → users affected → access gained beyond their role.
If no path: write exactly — *"No team membership escalation path identified."*

**Does NOT satisfy Mechanism 2**: "Team memberships may create escalation depending on configuration." Either name the team and the path, or explicitly confirm no path was found. Asserted possibility is not a sweep result.

**Mechanism 3 — Sharing Rule Exploitation**
Does any sharing rule (criteria-based, owner-based, manual) widen access beyond the security role baseline? State: rule → role affected → effective access delta.
If no conflict: write exactly — *"No sharing rule escalation path identified."*

**Does NOT satisfy Mechanism 3**: Naming that a sharing rule exists without diagnosing whether it conflicts with the security role baseline. "An owner-based sharing rule is configured" is an observation, not a sweep finding.

After completing all three:
*"Escalation sweep complete. All three mechanism types checked: record reassignment / team membership addition / sharing rule exploitation."*

---

### Step 6: Team Membership Gap

Identify at least one team membership anomaly — a user not on an expected team who loses access, or a user on multiple teams whose combined permissions exceed intent. State the team, the user scenario, and the resulting anomaly.

If none: *"No team membership gap identified for {{topic}}."*

**Does NOT satisfy this step**: "Teams could potentially create access anomalies." Name a specific team and a specific scenario — or explicitly confirm none exists.

---

### Step 7: Sharing Rule Conflict

Identify at least one sharing rule that widens access beyond the security role baseline or creates a contradiction with a configured role. Reference the baseline from Step 0.

If none: *"No sharing rule conflict identified for {{topic}}."*

---

### Step 8: Risk-Ranked Gap Summary

| Gap      | Severity           | Justification                            | Remediation                           |
|----------|--------------------|------------------------------------------|---------------------------------------|
| [name]   | High / Medium / Low | [operation + data sensitivity + why]     | [role + field or rule + specific action] |

Include all gaps: from Step 4, Step 5, Step 6, Step 7, and persistent FLS gaps from Step 3.

**Does NOT satisfy severity**: An unranked list. Every row must carry H/M/L — the reader must be able to triage from this table alone.

**Does NOT satisfy justification**: "This is a high risk." Name the specific operation and the sensitivity of the data involved.

**Does NOT satisfy remediation**: "Tighten security" or "review FLS settings." Name the role, the field or rule, and the specific action. "Add FLS read-deny on AccountNumber for Customer Service Representative" is a remediation. "Improve FLS coverage" is not.

---

## V-02

**Variation axis**: Output format — pre-printed audit form
**Hypothesis**: Formatting the prompt as a fillable audit form makes C-18 structural — Section 0 is pre-printed and cannot be skipped. C-13 (negative evidence), C-11 (sweep procedure), and C-17 (all three mechanism types) become impossible to omit because the sweep section has three mandatory rows. C-15 (N/A justification) is enforced by a column rule rather than a remembered instruction. The audit form also creates a navigable output where each criterion maps to a numbered section — the scorer cannot silently elide a section the way they can skip a prose paragraph. The single axis is output format; no other axis (phrasing register, role sequence, inertia framing) varies.

---

You are a Dataverse security expert completing a formal permission audit. Fill in every section of this audit form. Do not skip rows or leave cells blank.

**Feature**: {{topic}}
**Roles**: {{roles}} — default: Customer Service Representative, Customer Service Manager, System Administrator

---

## SECTION 0 — BASELINE PERMISSION STATE

*Fill in before any role-specific analysis. This declaration anchors every gap finding.*

| Dimension                                               | Default State (before any role assignment)             |
|---------------------------------------------------------|--------------------------------------------------------|
| Default record operations (authenticated, no role)      |                                                        |
| FLS configured by default on sensitive fields?          |                                                        |
| Sharing rules active by default?                        |                                                        |
| Teams configured by default?                            |                                                        |

**Baseline declaration** (write this sentence before proceeding):
> *"The baseline permission state for {{topic}} is: ___________. Every finding below is a deviation from or failure to deviate from this state."*

This section is not optional. Analysis that begins with role-specific permissions without a named baseline cannot prove that unconfigured fields are gaps rather than omissions.

---

## SECTION 1 — ROLE-OPERATION MATRIX

*Fill in every cell. Values: Allow / Deny / N/A+reason. No blank cells permitted.*

| Operation | [Role 1] | [Role 2] | [Role 3] |
|-----------|----------|----------|----------|
| Create    |          |          |          |
| Read      |          |          |          |
| Update    |          |          |          |
| Delete    |          |          |          |
| Assign    |          |          |          |
| Share     |          |          |          |

**N/A rule**: Any N/A cell must carry a parenthetical reason on the same line. "N/A" alone is indistinguishable from a skipped analysis. "N/A — Assign does not apply: this entity routes via queue, not user ownership" is a documented decision.

---

## SECTION 2 — RECORD ACCESS SCOPE

*Fill in scope level and grant source for every role. Both columns are required.*

| Role     | Scope Level                      | Grant Source                               |
|----------|----------------------------------|--------------------------------------------|
| [Role 1] | Own / BU / Parent BU / Org       | Security Role / Team / Sharing Rule        |
| [Role 2] |                                  |                                            |
| [Role 3] |                                  |                                            |

**Source rule**: Scope level alone does not identify whether the scope comes from role configuration, a team, or a sharing rule — which is critical for gap analysis.

---

## SECTION 3 — FIELD-LEVEL SECURITY

*Fill in every cell. Values: Allow / Deny / Not Configured. No blank cells permitted.*

| Field    | [Role 1] | [Role 2] | [Role 3] |
|----------|----------|----------|----------|
| [field]  |          |          |          |
| [field]  |          |          |          |
| [field]  |          |          |          |

**Not Configured rule**: Write "Not Configured" where FLS has not been set. Do not omit the row or leave the cell blank. Not Configured is a finding — it means no restriction was applied, which is the same effective state as Allow for read access.

---

## SECTION 4 — ROLE TRANSITION DELTAS

*Fill in every transition row. Name specific operations and fields — "more access" summaries do not pass.*

| Transition          | Operations Added | Scope Changed? | FLS Restricted (newly) | FLS Still Not Configured |
|---------------------|-----------------|---------------|----------------------|--------------------------|
| [Role 1] → [Role 2] |                 |               |                      |                          |
| [Role 2] → [Role 3] |                 |               |                      |                          |

**Persistent FLS gaps** — list fields appearing in "FLS Still Not Configured" at every transition:
> *Persistent FLS gaps (never configured at any role level): ___________*

---

## SECTION 5 — ESCALATION SWEEP

*All three rows must be filled. The "Checked?" checkbox must be marked. A blank Finding cell is not acceptable.*

| Mechanism                | Checked? | Finding (or explicit no-finding statement)                    |
|--------------------------|---------|---------------------------------------------------------------|
| Record Reassignment      | ☐ Yes   |                                                               |
| Team Membership Addition | ☐ Yes   |                                                               |
| Sharing Rule Exploitation| ☐ Yes   |                                                               |

Permitted no-finding statements (copy exactly if applicable):
- *"No record reassignment escalation path identified."*
- *"No team membership escalation path identified."*
- *"No sharing rule escalation path identified."*

**Sweep confirmation** (write after filling all rows):
> *"Escalation sweep complete. All three mechanism types checked: record reassignment / team membership addition / sharing rule exploitation."*

---

## SECTION 6 — SECURITY GAPS

*Name at least one gap per applicable type. If a category has no finding, write the explicit no-finding statement — do not leave the cell blank.*

| Gap Type                   | Finding                                                               |
|----------------------------|-----------------------------------------------------------------------|
| FLS misconfiguration       |                                                                       |
| Over-permissive operation  |                                                                       |
| Sharing rule conflict      | [finding] or *"No sharing rule conflict identified for {{topic}}."*  |
| Team membership anomaly    | [finding] or *"No team membership gap identified for {{topic}}."*    |
| Privilege escalation path  | [finding] or *"No escalation path identified."*                      |

---

## SECTION 7 — RISK-RANKED SUMMARY

*Fill in every column for every gap from Section 6 and persistent FLS gaps from Section 4. Severity is H/M/L — no compound ratings.*

| Gap | Severity | Justification | Remediation |
|-----|----------|---------------|-------------|
|     | H / M / L | [operation + data sensitivity + why it matters] | [role + field or rule + specific action] |

**Remediation requirement**: "Add FLS read-deny on AccountNumber for Customer Service Representative" passes. "Review security configuration" or "tighten FLS" does not pass.

---

## AUDIT COMPLETION STATEMENT

> *"Permission audit complete for {{topic}}. Section 0 baseline declared. Sections 1 through 7 complete. [N] gaps identified. All three escalation sweep vectors confirmed. Persistent FLS gaps tracked: [field list or 'none']."*

---

## V-03

**Variation axis**: Phrasing register — formal/technical specification
**Hypothesis**: R4-V-02 used conversational imperative ("you have to check all three"). This variation tests the opposite register: formal third-person specification language ("The output shall enumerate...", "The analysis must establish..."). Formal register is the standard for security audit specifications (ISO 27001, NIST 800-53, SOC 2 criteria). The hypothesis is that formal register produces the same structural coverage as conversational imperative but with different failure modes — formal register may generate technically correct but incomplete outputs, while conversational register may generate less precise but more complete outputs. Testing this axis isolates the register effect on C-18 (baseline declaration, which formal register handles via §1) and C-19 (anti-pattern naming, which formal register does not naturally produce — testing whether "does not conform" language achieves the same effect as named examples of failure).

---

You are a Dataverse security expert. Produce a complete permission trace conforming to the following output specification.

**Feature**: {{topic}}
**Roles**: {{roles}} — default: Customer Service Representative, Customer Service Manager, System Administrator

---

### §1 — Baseline State Establishment

The output shall establish the default permission state for the entity type associated with {{topic}} prior to any role-specific analysis. The baseline declaration shall identify:

(a) Default operation permissions available to an authenticated user with no assigned role.
(b) Default field-level security configuration for sensitive fields (expected: None configured — state explicitly if otherwise).
(c) Default sharing rule configuration (expected: None active — state explicitly if otherwise).

The baseline declaration shall appear as a named starting state before the first role-specific section. Analysis that begins with role-specific permissions without prior baseline establishment does not conform to this specification — the baseline is the zero-point that makes gap identification verifiable.

---

### §2 — Role-Operation Matrix

The output shall present a complete role-operation matrix conforming to the following requirements:

(a) Every role named in {{roles}} shall appear as a column.
(b) Every relevant operation shall appear as a row: Create, Read, Update, Delete, Assign, Share.
(c) Every cell shall contain one of: Allow, Deny, N/A.
(d) Every N/A cell shall include an inline justification: "N/A — [reason]." An N/A cell without inline justification does not conform — it is indistinguishable from an unevaluated cell.
(e) Record access scope shall be stated for each role: Own / Business Unit / Parent BU / Organization.
(f) The grant source for each scope level shall be identified: Security Role / Team Membership / Sharing Rule. A scope level stated without its grant source does not conform.

---

### §3 — Field-Level Security

The output shall enumerate field-level security for all sensitive fields relevant to {{topic}} conforming to the following requirements:

(a) Every sensitive field shall appear as a row.
(b) FLS status shall be stated per field per role using one of: Allow, Deny, Not Configured.
(c) Field-role combinations where FLS has not been configured shall be written as "Not Configured" — not omitted, not left blank. An omitted cell and a blank cell are indistinguishable from each other and from an incomplete analysis. Not Configured is a named finding indicating that no restriction has been applied.

---

### §4 — Role Transition Deltas

For each adjacent role pair in the privilege hierarchy, the output shall state:

(a) Operations added to or removed from the higher role relative to the lower.
(b) Change in record access scope, if any; scope changes shall name the source mechanism.
(c) FLS configurations added or removed at this transition.
(d) FLS fields that remain Not Configured at both levels of this transition.

Upon completing all transition rows, the output shall identify any field that remains Not Configured across every role transition. Such fields shall be labeled: *"Persistent FLS Gap — unconfigured at all levels."* Per-cell flagging without cross-role persistence analysis does not conform to this requirement.

---

### §5 — Security Gap Identification

The output shall identify at least one concrete security misconfiguration. The gap statement shall name:

(a) The specific role affected.
(b) The specific field or operation involved.
(c) The current misconfiguration state.

A gap statement of the form "FLS is not fully configured" does not conform. The statement must be specific enough to generate a remediation action without requesting additional information.

---

### §6 — Privilege Escalation Sweep

The output shall conduct a privilege escalation sweep explicitly covering all three mechanism types. Each mechanism type shall be explicitly addressed regardless of whether it yields a finding. Addressing only the mechanism type that produced a result does not conform.

**§6.1 — Record Reassignment**
The output shall determine whether a user at a lower privilege level can gain expanded record scope by reassigning a record. The result shall state: actor, reassignment action, and resulting scope. Where no path is identified: *"No record reassignment escalation path identified."*

**§6.2 — Team Membership Addition**
The output shall determine whether adding a user to any team grants scope exceeding the user's security role. The result shall name: team, affected users, access gained. Where no path is identified: *"No team membership escalation path identified."*

**§6.3 — Sharing Rule Exploitation**
The output shall determine whether any sharing rule widens access beyond the security role baseline. The result shall name: rule, affected role, effective access delta. Where no path is identified: *"No sharing rule escalation path identified."*

Upon completion of §6.1 through §6.3, the output shall include:
*"Escalation sweep complete. All three mechanism types checked: record reassignment / team membership addition / sharing rule exploitation."*

---

### §7 — Team Membership Gap

The output shall identify at least one team membership anomaly producing an access outcome that deviates from intended configuration — either access loss from absent membership or access excess from overlapping memberships. The identification shall name: team, user scenario, and resulting anomaly.

Where no gap is identified: *"No team membership gap identified for {{topic}}."*

---

### §8 — Sharing Rule Conflict

The output shall identify at least one sharing rule that widens access beyond the security role baseline or creates a contradiction with a configured role.

Where no conflict is identified: *"No sharing rule conflict identified for {{topic}}."*

---

### §9 — Risk-Ranked Gap Summary

The output shall present all identified gaps in a table ordered by severity (High / Medium / Low) conforming to:

(a) Severity: H, M, or L on every row — compound ratings such as "Medium-High" do not conform.
(b) Justification: shall name the specific operation and data sensitivity driving the rating. "This is a high risk" does not conform.
(c) Remediation: shall specify a concrete configuration change naming the role, the field or rule, and the action. "Review FLS settings" or "tighten security configuration" do not conform.

The summary shall include all gaps identified in §5 through §8 and all persistent FLS gaps from §4.

---

## V-04

**Variation axis combination**: C-18 explicit baseline anchor + C-19 anti-pattern naming
**Hypothesis**: Both new v5 criteria are the primary targets. C-18 is addressed by making the baseline declaration a fill-in-the-blank template — a ritual commitment that must be completed before the model can advance, not just a requested section. C-19 is addressed by embedding "What does NOT satisfy this" blocks at every substantive instruction. The combination tests whether targeting both new criteria simultaneously in a single prompt produces higher coverage of C-18/C-19 than the R5 single-axis variations, or whether the density of anti-pattern naming imposes cognitive load that displaces accuracy in other sections.

---

You are a Dataverse security expert. This trace begins with a required baseline declaration and names the failure mode alongside the requirement at each step.

**Feature**: {{topic}}
**Roles**: {{roles}} — default: Customer Service Representative, Customer Service Manager, System Administrator

---

## REQUIRED FIRST: BASELINE PERMISSION DECLARATION

Before any role is documented, write this declaration, filling in the blanks:

> **Baseline Permission State for {{topic}}:**
> - Default record operations for an authenticated user with no role: ___________
> - Default FLS on sensitive fields: Not Configured (list any exceptions)
> - Default sharing rules: ___________ (none active / [name active rules])
> - Default team memberships: ___________ (none configured / [name configured teams])
>
> **Zero-point anchor**: Every role-specific permission documented below is a deviation from, or a failure to deviate from, the above baseline state.

**This declaration is not optional.** An analysis that begins "Customer Service Representative can Create records..." without a named zero-point is unverifiable — the reader cannot distinguish a missing FLS restriction from an omitted table row. The declaration transforms the analysis from a description into an audit.

---

## Section 1: Role-Operation Matrix

Map every role to every operation. Use Allow, Deny, or N/A+reason.

| Operation | [Role 1] | [Role 2] | [Role 3] |
|-----------|----------|----------|----------|
| Create    |          |          |          |
| Read      |          |          |          |
| Update    |          |          |          |
| Delete    |          |          |          |
| Assign    |          |          |          |
| Share     |          |          |          |

For each role also state: **Record Scope** (Own/BU/Parent BU/Org) and **Scope Source** (Security Role/Team/Sharing Rule).

**What does NOT satisfy this section**:
- Prose description of role capabilities ("the representative can read and update") without the table — prose cannot be scanned for omissions.
- A blank N/A cell without a reason — "N/A" alone is indistinguishable from a skipped cell; "N/A — Assign does not apply: this entity uses queue routing" is a documented decision.
- Scope level without source — knowing a role has BU scope does not reveal whether it comes from the security role, team membership, or a sharing rule.

---

## Section 2: Field-Level Security

List every sensitive field relevant to this feature. For each field and each role, state: Allow, Deny, or Not Configured.

| Field   | [Role 1] | [Role 2] | [Role 3] |
|---------|----------|----------|----------|
| [field] |          |          |          |

**What does NOT satisfy this section**:
- A blank cell — blank is an omission; "Not Configured" is a finding; they are not the same thing.
- "FLS should be reviewed for this feature" — name the specific field and the specific role configuration, not the general principle.
- Listing only fields that have restrictions — fields without any FLS configured are the gaps; omitting them hides the security debt.

---

## Section 3: Role Transition Deltas

For each adjacent pair, state what the higher role has that the lower does not.

| Transition          | Operations Added | Scope Change | FLS Resolved | FLS Still Not Configured |
|---------------------|-----------------|--------------|-------------|--------------------------|
| [Role 1] → [Role 2] |                 |              |             |                          |
| [Role 2] → [Role 3] |                 |              |             |                          |

After completing: list fields that remain Not Configured at every transition. Label: *"Persistent FLS Gap — unconfigured at all levels."*

**What does NOT satisfy this section**:
- "Role B has broader access than Role A" — this says nothing about which specific operations or fields differ.
- Omitting the "FLS Still Not Configured" column — this is where persistent gaps become visible; a table without this column cannot prove persistence tracking.
- Noting per-cell that a field is Not Configured without a cross-role persistence analysis — a field at Not Configured at every transition is a categorically different problem from a gap resolved at a higher level.

---

## Section 4: Named Security Gap

Before the sweep, name at least one concrete misconfiguration: role + field or operation + current state + why it matters.

**What does NOT satisfy this section**:
- "FLS is not consistently configured across all roles" — a general observation is not a finding.
- "The permission model has potential issues" — potential is not a finding; name the specific role, the specific field or operation, and the specific misconfiguration.

---

## Section 5: Escalation Sweep — All Three Mechanism Types

Check all three vectors. State a finding or an explicit no-finding for each.

**Mechanism 1 — Record Reassignment**
Finding: [who → what action → resulting scope] or *"No record reassignment escalation path identified."*

**What does NOT satisfy Mechanism 1**: Silence. Not mentioning this mechanism is indistinguishable from not checking it. Finding a path under Mechanism 2 does not satisfy Mechanism 1.

**Mechanism 2 — Team Membership Addition**
Finding: [team → users → access gained] or *"No team membership escalation path identified."*

**What does NOT satisfy Mechanism 2**: "Team memberships could potentially create escalation." Either name the team and the specific path, or explicitly confirm no path was found. Asserted possibility is not a sweep result.

**Mechanism 3 — Sharing Rule Exploitation**
Finding: [rule → role affected → effective access delta] or *"No sharing rule escalation path identified."*

**What does NOT satisfy Mechanism 3**: Naming that a sharing rule exists without diagnosing whether it conflicts with the security role baseline. "An owner-based sharing rule is configured" is an observation, not a finding.

*"Escalation sweep complete. All three mechanism types checked: record reassignment / team membership addition / sharing rule exploitation."*

---

## Section 6: Sharing Rule Conflict

Identify at least one sharing rule that widens access beyond the role baseline or contradicts a configured role. Reference the baseline declaration above.

If none: *"No sharing rule conflict identified for {{topic}}."*

---

## Section 7: Team Membership Gap

Identify at least one team membership anomaly. Name the team, the user scenario, and the resulting access deviation.

If none: *"No team membership gap identified for {{topic}}."*

---

## Section 8: Risk-Ranked Gap Summary

| Gap  | Severity           | Justification                         | Remediation                              |
|------|--------------------|---------------------------------------|------------------------------------------|
| [name] | High / Medium / Low | [operation + data sensitivity + why] | [role + field or rule + specific action] |

Include all gaps from Sections 4–7 and persistent FLS gaps from Section 3.

**What does NOT satisfy severity**: A list of gaps without rankings. Every row must carry H/M/L.

**What does NOT satisfy justification**: "This gap poses a high risk." Name the specific operation and the data at risk.

**What does NOT satisfy remediation**: "Tighten security" or "review FLS configuration." Name the role, the field or rule, and the specific action. "Add FLS read-deny on CreditLimit for Customer Service Representative" is a remediation. "Improve FLS coverage" is not.

---

## V-05

**Variation axis combination**: Bottom-up role sequence (R4-V-01 base) + C-19 anti-pattern naming at every rule block
**Hypothesis**: R4-V-01 was the second-strongest single-axis variation at Round 4 (83 pts). Its excellence signal was that it achieved C-18 "by construction" — bottom-up ordering forces the least-privileged baseline to be established before any role is enumerated, which is exactly the zero-point declaration C-18 requires. The only gap in R4-V-01 was C-19 (not targeted). This variation adds C-19 to R4-V-01 by inserting "What this is NOT" notes at every rule block — the same technique that made V-01 in this round a single-axis test. The combination should achieve C-18 structurally (bottom-up construction) and C-19 structurally (named anti-patterns at every boundary). If the hypothesis is correct, this variation achieves both new v5 criteria without changing any other structural property of R4-V-01.

---

You are a Dataverse security expert. Trace permissions for the feature described below, working bottom-up — from the least-privileged role to the most-privileged. As you define each rule, this prompt names what would appear to satisfy it but does not.

**Feature**: {{topic}}
**Roles** (list in ascending privilege order): {{roles}}
Default order: Customer Service Representative → Customer Service Manager → System Administrator

---

### Step 1: Establish the Minimum Baseline

Document the least-privileged role completely before touching any other role.

**1A — Role-Operation Matrix row**

| Operation | [Least-Privileged Role]                     |
|-----------|---------------------------------------------|
| Create    | Allow / Deny / N/A — [reason if N/A]        |
| Read      |                                             |
| Update    |                                             |
| Delete    |                                             |
| Assign    |                                             |
| Share     |                                             |

**Rule — N/A cells**: If any operation is N/A, write the reason inline. A bare N/A is indistinguishable from a skipped cell.

**What a bare N/A looks like vs what passes**: "N/A" — the reader cannot tell if this was evaluated. "N/A — Assign does not apply: this entity routes via queue, not user ownership" — the reader sees a documented decision. One is evidence; the other is a gap in the audit trail.

**1B — Record Access Scope**

State the scope for this role: Own / Business Unit / Parent BU / Organization
Grant source: Security Role / Team Membership / Sharing Rule

**Rule**: Both scope level and source are required.

**What does NOT satisfy scope documentation**: "BU scope" alone. Without the source, the analysis cannot identify whether the scope is constrained by the role definition or widened by a team or sharing rule — which is precisely the question privilege escalation analysis must answer.

**1C — Field-Level Security**

| Field   | Read                              | Write                             |
|---------|-----------------------------------|-----------------------------------|
| [field] | Allow / Deny / Not Configured     | Allow / Deny / Not Configured     |

**Rule — Not Configured cells**: Write "Not Configured" explicitly. It is a named finding — not a blank, not an omission.

**What blank looks like vs what passes**: A blank cell — the reader cannot distinguish a missing restriction from an incomplete table. "Not Configured" — the reader sees a gap that no one in the security design has ever addressed. The distinction matters for identifying security debt that spans the entire role hierarchy.

After completing 1A–1C: **list every field currently at Not Configured.** This is the persistence candidate list — fields that have never been secured at any role level.

---

### Step 2: First Elevation — Next Role Up

For each item, state what changed from the previous role.

**2A — Operation delta**

| Operation | Previous | New Value | Changed? |
|-----------|----------|-----------|----------|
| Create    |          |           |          |
| Read      |          |           |          |
| Update    |          |           |          |
| Delete    |          |           |          |
| Assign    |          |           |          |
| Share     |          |           |          |

**Rule — N/A carries forward**: If an operation was N/A at the previous role and remains N/A here, repeat the reason — confirming it was re-evaluated, not just copied.

**What does NOT satisfy delta tracking**: Restating both roles' capabilities from scratch ("Role A: Allow/Deny/Deny... Role B: Allow/Allow/Deny...") without a comparison column. The delta column must exist and must name the specific change. "Role B has more access" is not a delta; "Delete added at Role B" is.

**2B — Record scope delta**

Previous scope → New scope (or: unchanged)
Scope source: Security Role / Team Membership / Sharing Rule

**2C — FLS delta**

| Field   | Previous | New | Changed?                                              |
|---------|----------|-----|-------------------------------------------------------|
| [field] |          |     | Added restriction / Removed restriction / Still Not Configured |

**Rule — Persistent gaps**: After completing 2C, revisit the persistence candidate list from Step 1. Remove fields where FLS was configured at this level. Keep fields still at Not Configured.

State the updated persistence candidate list explicitly.

**What does NOT satisfy persistence tracking**: Noting that a field is Not Configured for this role in isolation. Persistence tracking requires cross-role visibility — the same field appearing at Not Configured at multiple transitions is a different signal from a gap at one level that is resolved at the next. A reader looking at per-cell entries cannot determine persistence without this cross-role list.

---

### Step 3: Repeat for Each Remaining Role

Apply the same delta table (3A/3B/3C) for each additional role in ascending order. After each role's FLS delta, update the persistence candidate list.

When you reach the highest-privilege role:

**Persistent FLS Gaps**: Fields that remain Not Configured at every role level, from the least-privileged baseline through the highest role. Label: *"Persistent FLS Gap — unconfigured at all levels."*

**What does NOT satisfy persistent gap identification**: Listing all Not Configured cells at each role independently. A field that is Not Configured for every role is a different category of problem — it means no transition in the security design ever addressed it. This requires the running cross-role list maintained through Steps 1–3, not per-cell flagging after the fact.

---

### Step 4: Consolidated Role-Operation Matrix

After all role walks, assemble the full matrix:

| Operation | [Role 1] | [Role 2] | [Role 3] |
|-----------|----------|----------|----------|
| Create    |          |          |          |
| Read      |          |          |          |
| Update    |          |          |          |
| Delete    |          |          |          |
| Assign    |          |          |          |
| Share     |          |          |          |

Every N/A cell must carry its reason from the per-role steps above.

---

### Step 5: Escalation Sweep — All Three Mechanism Types

Check each mechanism type explicitly. Address all three regardless of whether any yields a finding.

**Mechanism 1 — Record Reassignment**
Can a user at a lower privilege level reassign a record to gain the scope of a higher role?
State: who → via what reassignment action → resulting scope
If no path: *"No record reassignment escalation path identified."*

**What does NOT satisfy Mechanism 1**: Detecting an escalation path under Mechanism 2 or 3 and skipping Mechanism 1 because "no similar reassignment issue was found." Each mechanism type must be explicitly checked and explicitly closed. Checking the easy one and not the others does not pass.

**Mechanism 2 — Team Membership Addition**
Does adding a user to any team grant access beyond their security role scope?
State: team → users affected → access gained beyond their role
If no path: *"No team membership escalation path identified."*

**What does NOT satisfy Mechanism 2**: "Team membership may create escalation depending on configuration." Either name the team and the path, or confirm no path was found. Unconfirmed possibility is not a sweep result.

**Mechanism 3 — Sharing Rule Exploitation**
Does any sharing rule widen access beyond the security role baseline?
State: rule → role affected → effective access delta
If no conflict: *"No sharing rule escalation path identified."*

**What does NOT satisfy Mechanism 3**: Naming that a sharing rule exists without determining whether it conflicts with the security role baseline. "An owner-based sharing rule is configured" is an observation. "The owner-based sharing rule grants Org-read to the Customer Service role whose baseline is BU-read" is a finding.

*"Escalation sweep complete. All three mechanism types checked: record reassignment / team membership addition / sharing rule exploitation."*

---

### Step 6: Team Membership Gap

Identify at least one team membership anomaly — a user not on an expected team who loses access, or a user on multiple teams whose combined permissions exceed intent. Name the team, the user scenario, and the resulting anomaly.

If none: *"No team membership gap identified for {{topic}}."*

**What does NOT satisfy this step**: "Teams could potentially create access anomalies." Name a specific team and a specific scenario, or explicitly confirm none exists. Asserted possibility is not a named finding.

---

### Step 7: Risk-Ranked Gap Summary

| Gap        | Severity           | Justification                              | Remediation                                   |
|------------|--------------------|--------------------------------------------|-----------------------------------------------|
| [gap name] | High / Medium / Low | [operation + data sensitivity + why it matters] | [role + field or rule + specific action]  |

Include all gaps: from the sweep, team analysis, and persistent FLS gaps from Step 3.

**What does NOT satisfy severity**: A list of gaps without H/M/L labels. Ranking is required on every row — the reader must be able to triage from this table alone.

**What does NOT satisfy justification**: "This gap poses a high risk." The justification must name the specific operation at risk and the sensitivity of the data involved. "Customer Service Representative can read AccountNumber with no FLS restriction; this field contains PAN-adjacent data and should be restricted to Manager and above" is a justification.

**What does NOT satisfy remediation**: "Tighten security" or "review FLS configuration." Name the role, the field or rule, and the specific action. "Add FLS read-deny on AccountNumber for Customer Service Representative" is a remediation. "Improve FLS coverage for sensitive fields" is not — it contains no actionable target.
