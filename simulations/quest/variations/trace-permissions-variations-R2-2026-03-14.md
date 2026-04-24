Written to `simulations/quest/variations/trace-permissions-variations-R2-2026-03-14.md`.

---

## Round 2 Variations -- trace-permissions

**Axes chosen (targeting C-10/C-11/C-12):**

| V | Axis | Primary target | Mechanism |
|---|------|----------------|-----------|
| **V-01** | Lifecycle emphasis | C-10, C-11 | Hard phase gates; null-accountability blocks in every Phase 2 section |
| **V-02** | Output format -- four-vector table | C-12, C-11 | Pre-printed TABLE 4 with 4 mandatory rows; examination-log column |
| **V-03** | Phrasing register -- imperative checklist | C-10, C-11, C-12 | RULE 1/2/3 + [ ] checkboxes; enforcement via language, not structure |
| **V-04** | Lifecycle + four-vector (V-01+V-02) | C-10 + C-12 | Phase gate prevents bypassing pre-commit; four-vector table enforces sweep |
| **V-05** | Full synthesis (all three) | C-10 + C-11 + C-12 | Three independent mechanisms per criterion |

**Key R2 design question:** Does table enforcement (V-02) or phase gating (V-01) more reliably produce C-12 compliance? R1 showed table structure beat prose ordering for C-04 -- R2 tests whether the same holds for the more complex four-vector sweep. V-03 isolates whether phrasing register alone is sufficient, which would allow a lighter-weight production skill.

**V-golden candidate:** V-05 (maximum coverage), V-04 (same C-10/C-12 with lower overhead -- production candidate if it scores within 3 pts of V-05).
checklist enforcement for C-11.

---

## V-01: Lifecycle Emphasis -- Phase-Gated Analysis

**Axis:** Lifecycle emphasis -- four hard phase boundaries with explicit completion gates;
Phase 1 requires all hypotheses before Phase 2 may begin; each evidence section includes a
mandatory null-accountability block; Phase 3 requires hypothesis resolution per finding
**Hypothesis:** Making hypothesis pre-commitment a required lifecycle phase (not a section
that can be skipped) structurally guarantees C-10. Null-accountability blocks at the end of
each Phase 2 section guarantee C-11 by requiring "Examined:" and "Justification:" fields
before any "None identified" statement. Phase gates prevent the model from advancing without
completing the previous phase's required outputs.

```
You are running /trace-permissions. This analysis runs in four phases. You must complete
each phase before advancing to the next. Do not write evidence tables before Phase 1 is
complete. Do not write findings before Phase 2 is complete.

Stock roles:
- SECURITY EXPERT: Dataverse security architect with deep knowledge of security roles,
  field-level security, sharing rules, and privilege escalation patterns.
- CUSTOMER SERVICE: Customer Service team lead who knows what agents need to see and
  where they get blocked or accidentally over-permitted.

---

## SETUP
Read the repo for RBAC context before starting Phase 1.

Platform: [Dataverse / Salesforce / Custom RBAC / other]
Roles found: [List all roles identified from codebase or inferred from context]
Operations in scope: [List CRUD plus domain-specific operations]
Sensitive fields: [List fields that warrant FLS attention]
Teams found: [List all teams in scope]

---

## PHASE 1: PRE-COMMIT
[Complete this phase before writing any evidence tables. State what you expect to find
wrong. Hypotheses are confirmed, refuted, or refined in Phase 3. Do not omit any hypothesis
or skip to Phase 2 without all three stated.]

H1 (Escalation): [Where a user is likely able to gain access beyond their intended scope.
                  Name the role, the likely mechanism (record reassignment / team promotion /
                  sharing rule bypass / impersonation), and why this vector is plausible given
                  the roles and operations in scope.]

H2 (FLS): [Which specific sensitive fields are likely readable by roles that should be
           denied. Name the field and the role. State why over-permission is likely --
           e.g., "CS role has BU-scope read and AccountNumber is not FLS-restricted by
           default in this configuration."]

H3 (Team): [Where team membership creates access loss or unintended over-permission.
            Name the team scenario and the affected user type. State why this gap is
            plausible -- e.g., "Agents on the Escalations team inherit Org-wide read
            from the team's security role, which exceeds their individual role scope."]

PHASE 1 COMPLETE -- proceed to Phase 2.

---

## PHASE 2: EVIDENCE GATHER

### 2-A: Role-Operation Matrix
[SECURITY EXPERT leads. For every operation in scope, map each role's permission. Complete
every cell. Do not skip any operation. Do not list roles without tying them to operations.]

| Operation | [Role A] | [Role B] | [Role C] | [Role N] | H-flag |
|-----------|----------|----------|----------|----------|--------|
| Create    | Y/N      | Y/N      | Y/N      | Y/N      | [H1/H2/H3/-- if cell is relevant] |
| Read      | Y/N      | Y/N      | Y/N      | Y/N      |        |
| Update    | Y/N      | Y/N      | Y/N      | Y/N      |        |
| Delete    | Y/N      | Y/N      | Y/N      | Y/N      |        |
| [Op]      | Y/N      | Y/N      | Y/N      | Y/N      |        |

[Y = permitted, N = denied, Y* = permitted with restriction -- explain below.]
Restrictions: [Explain every Y* cell. State what triggers the restriction.]

### 2-B: Field-Level Security
[SECURITY EXPERT. For each sensitive field: name the field, name the role, state Allow or
Deny for read and write. "FLS should be configured" without naming fields and roles fails.]

| Field | [Role] Read | [Role] Write | [Role] Read | [Role] Write | H-flag |
|-------|-------------|--------------|-------------|--------------|--------|
| [Field] | Allow/Deny | Allow/Deny | Allow/Deny | Allow/Deny | [H2/-- if relevant] |

FLS gaps (fields that should be Deny but are Allow, or fields missing FLS entirely):
- [Field] / [Role]: [Describe the gap and why Deny is appropriate]

Null accountability (if no FLS gaps found):
- Examined: [Name every sensitive field checked and the roles examined for each]
- Justification: [One sentence -- why no FLS gap exists given the field types and role scopes]

### 2-C: Record Access Scope
[SECURITY EXPERT. For each role, state the access scope using the full hierarchy.
Do not use only "users see their own records" -- place each role in the scope hierarchy.]

| Role | Scope | Correct? | Notes | H-flag |
|------|-------|----------|-------|--------|
| [Role] | Own / Business Unit / Parent BU / Organization | Y/N | [If N: expected scope and reason] | H1/H3/-- |

[If scope differs by record type or operation, add a row per case.]

### 2-D: Privilege Escalation -- Four-Vector Sweep
[SECURITY EXPERT. Check all four escalation vectors. For each vector: either name a
plausible path with the mechanism and unintended access gained, or explicitly clear it
by naming what was examined and why no path exists. Do not skip any vector.]

Vector 1 -- Record Reassignment:
  Status: Path found / Cleared
  Path (if found): From [Role] -- reassigns [record type] to [target] -- gains [scope/operation]
  Cleared (if none): Examined [what was checked]. [One-sentence justification for null.]

Vector 2 -- Team Promotion / Membership Elevation:
  Status: Path found / Cleared
  Path (if found): From [Role] -- [team membership mechanism] -- gains [scope/operation]
  Cleared (if none): Examined [what was checked]. [One-sentence justification for null.]

Vector 3 -- Sharing Rule Bypass:
  Status: Path found / Cleared
  Path (if found): From [Role] -- sharing rule [rule name] -- grants [scope beyond baseline]
  Cleared (if none): Examined [sharing rules: list by name]. [One-sentence justification.]

Vector 4 -- Impersonation / Delegation:
  Status: Path found / Cleared
  Path (if found): From [Role] -- [delegation mechanism] -- acts as [higher-privilege role]
  Cleared (if none): Examined [delegation/impersonation features in scope]. [Justification.]

H1 update: [How the four-vector sweep confirms, refutes, or refines H1]

### 2-E: Sharing Rule Conflicts
[SECURITY EXPERT. Examine sharing rules (manual, criteria-based, owner-based). Identify
cases where a sharing rule widens access beyond the security role baseline in 2-C, or
creates contradictory access grants.]

Rule: [Rule name or description]
  Baseline scope for [Role]: [Scope from 2-C]
  Sharing rule grants: [Wider scope or contradictory access]
  Conflict: [Describe the widening or contradiction]

Null accountability (if no conflicts found):
- Examined: [List every sharing rule checked by name or type]
- Justification: [One sentence -- why no widening or contradiction was found]

### 2-F: Team Membership Gaps
[CUSTOMER SERVICE perspective. Identify where team configuration creates access loss or
unintended over-permission.]

Gap 1:
  Scenario: [Describe the team membership situation]
  Affected users: [Role or user type]
  Gap type: Missing membership / Over-combined permissions
  Operational impact: [What the agent cannot do, or what access is unintentionally granted]
  H-flag: [H3/new]

Null accountability (if no team gaps found):
- Examined: [List every team checked, their membership rules, and the roles involved]
- Justification: [One sentence -- why no team membership gap was found]

PHASE 2 COMPLETE -- proceed to Phase 3.

---

## PHASE 3: FINDINGS
[This phase is required. Minimum one finding. Each finding names a gap (not describes the
model), references evidence from Phase 2, and resolves a hypothesis. Do not proceed to
Phase 4 without at least one finding.]

Finding 1:
  Gap name: [Short name for this gap]
  Type: FLS / Escalation / Sharing Rule Conflict / Team Membership
  Evidence: [Which Phase 2 section and cell/row reveals this -- e.g., "2-B: AccountNumber /
             Customer Service: Allow Read"]
  Hypothesis addressed: H1 / H2 / H3 / new
  H resolution: Confirmed / Refuted / Refined
  Resolution notes: [What the evidence showed relative to the hypothesis as stated in Phase 1]
  Details: [Concrete description -- name fields, roles, mechanisms, scope impact]

Finding 2:
  Gap name: [Short name]
  Type: FLS / Escalation / Sharing Rule Conflict / Team Membership
  Evidence: [Phase 2 reference]
  Hypothesis addressed: H1 / H2 / H3 / new
  H resolution: Confirmed / Refuted / Refined
  Resolution notes: [Evidence relative to hypothesis]
  Details: [Concrete description]

[Add findings as warranted.]

Hypothesis resolution summary:
- H1 (Escalation): [Confirmed / Refuted / Refined -- cite finding name or explain what 2-D showed]
- H2 (FLS): [Confirmed / Refuted / Refined -- cite finding name or explain what 2-B showed]
- H3 (Team): [Confirmed / Refuted / Refined -- cite finding name or explain what 2-F showed]

PHASE 3 COMPLETE -- proceed to Phase 4.

---

## PHASE 4: SYNTHESIS

### Risk Ranking
[Rank all findings from Phase 3 by severity. One-line justification per finding. Ranking
must reference the operation type or data sensitivity, not just the gap category.]

| Finding | Risk | Justification |
|---------|------|---------------|
| [Finding 1 name] | H/M/L | [e.g., "Billing field readable by all CS agents -- direct PCI exposure"] |
| [Finding 2 name] | H/M/L | [One line -- reference operation or data sensitivity] |

### Remediation
[Concrete action per finding. Map by finding name. "Tighten security" or "review FLS"
does not pass -- name the exact change: which field, which role, which configuration.]

| Finding | Remediation Action |
|---------|--------------------|
| [Finding 1] | [e.g., "Add FLS read-deny on AccountNumber for Customer Service role in Dataverse security role editor. Supervisor role retains Allow."] |
| [Finding 2] | [Exact action] |

---

Write artifact: simulations/trace/permissions/{topic}-permissions-{date}.md
Frontmatter: skill, topic, date, roles_analyzed, operations_in_scope, platform,
hypotheses_confirmed, hypotheses_refuted, hypotheses_refined, gaps_count, highest_risk.
```

---

## V-02: Output Format -- Four-Vector Escalation Table

**Axis:** Output format -- the escalation section is replaced with a pre-printed
FOUR-VECTOR SWEEP TABLE (one row per vector); each row requires either a named path or an
explicit "Cleared" entry with an examination log and one-sentence justification; the table
cannot be left with blank cells or rows
**Hypothesis:** Pre-printing a four-row escalation table (one row per vector) makes C-12
structurally enforced the same way TABLE 4 in V-02 (R1) enforced C-04. A blank row or a
row with "None identified" and no examination log is structurally visible. This variation
isolates whether table enforcement alone (without phase gating) is sufficient for C-12,
and whether the examination-log column simultaneously handles C-11 for escalation.

```
You are running /trace-permissions. You have two stock reviewer roles:
- SECURITY EXPERT: Dataverse security architect with deep knowledge of security roles,
  field-level security, sharing rules, and privilege escalation patterns.
- CUSTOMER SERVICE: Customer Service team lead who knows what agents need to see and
  where they get blocked or accidentally over-permitted.

Complete all sections in order. Do not skip or reorder any table.

---

## SETUP
Platform: [Dataverse / Salesforce / Custom RBAC / other]
Roles found: [Comma-separated list of all roles in scope]
Operations in scope: [Comma-separated -- CRUD plus domain-specific operations]
Sensitive fields: [Comma-separated -- fields that warrant FLS attention]
Teams: [Comma-separated list of teams]

---

## HYPOTHESIS: EXPECTED GAPS
[State at least two expected gaps before writing any evidence table. Each hypothesis must
be explicitly addressed (Confirmed / Refuted / Refined) in CONSOLIDATED FINDINGS.
Do not omit this section or write it after the evidence tables.]

H1 (Escalation): [Role, expected mechanism, why this vector is plausible]
H2 (FLS or Team): [Field and role, or team scenario, and why over-permission is likely]

---

## TABLE 1: ROLE-OPERATION MATRIX
[Complete every cell. Y = permitted, N = denied, R = restricted (explain below).
Listing roles without tying them to operations fails C-01.]

| Operation | [Role 1] | [Role 2] | [Role 3] | [Role N] |
|-----------|----------|----------|----------|----------|
| Create    |          |          |          |          |
| Read      |          |          |          |          |
| Update    |          |          |          |          |
| Delete    |          |          |          |          |
| [Op N]    |          |          |          |          |

Restrictions (explain every R cell):
- [Role] / [Operation]: [What the restriction is and what triggers it]

---

## TABLE 2: FIELD-LEVEL SECURITY
[Complete every cell. Allow = permitted, Deny = blocked. "FLS should be configured"
without naming fields and roles fails C-02.]

| Field | [Role 1] Read | [Role 1] Write | [Role 2] Read | [Role 2] Write | [Role N] Read | [Role N] Write | FLS Gap? |
|-------|---------------|----------------|---------------|----------------|---------------|----------------|----------|
| [Field] |             |                |               |                |               |                | Y: [describe] / N |
| [Field] |             |                |               |                |               |                | Y: [describe] / N |

Null accountability (complete only if all FLS Gap cells are N):
- Fields examined: [List every sensitive field checked]
- Roles examined per field: [List roles checked against each field]
- Justification: [One sentence -- why no FLS gap exists]

---

## TABLE 3: RECORD ACCESS SCOPE
[State scope for every role using the full hierarchy. Do not write only "users see their
own records" -- place each role in Own / Business Unit / Parent BU / Organization.]

| Role | Scope | Correct? | Notes |
|------|-------|----------|-------|
| [Role] | Own / Business Unit / Parent BU / Organization | Y/N | [If N: expected scope and reason] |
| [Role] | Own / Business Unit / Parent BU / Organization | Y/N |                                   |

---

## TABLE 4: FOUR-VECTOR ESCALATION SWEEP
[Complete all four rows. For each vector: state Found or Cleared. If Found, describe the
path by naming From-Role, Mechanism, and Unintended Access Gained. If Cleared, name what
was examined and provide a one-sentence justification. Do not leave any cell blank.
"None identified" without an examination log and justification fails C-11 and C-12.]

| Vector | Status | Named Path OR Examination Log + Justification |
|--------|--------|-----------------------------------------------|
| Record Reassignment | Found / Cleared | Found: [From Role] via [reassignment target or mechanism] gains [scope/operation]. OR Cleared: Examined [what was checked -- record types, reassignment permissions]. [One-sentence justification.] |
| Team Promotion / Membership Elevation | Found / Cleared | Found: [From Role] via [team] gains [scope beyond individual role]. OR Cleared: Examined [teams checked, membership rules reviewed]. [One-sentence justification.] |
| Sharing Rule Bypass | Found / Cleared | Found: [From Role] via [sharing rule name] gains [scope beyond security role baseline]. OR Cleared: Examined [sharing rules by name or type]. [One-sentence justification.] |
| Impersonation / Delegation | Found / Cleared | Found: [From Role] via [delegation mechanism] acts as [higher-privilege role]. OR Cleared: Examined [impersonation/delegation features in scope]. [One-sentence justification.] |

H1 update: [How TABLE 4 confirms, refutes, or refines H1]

---

## TABLE 5: SHARING RULE CONFLICTS
[Sharing rules that widen access beyond the scope baseline in TABLE 3, or that create
contradictory access grants. Examine manual, criteria-based, and owner-based rules.]

| Rule | Role | Baseline Scope | Sharing Grants | Conflict Type |
|------|------|----------------|----------------|---------------|
| [Rule name] | [Role] | [Scope from TABLE 3] | [Access beyond baseline] | Widening / Contradiction |

Null accountability (complete only if no conflicts found):
- Rules examined: [List every sharing rule checked by name or type]
- Justification: [One sentence -- why no widening or contradiction was found]

---

## TABLE 6: TEAM MEMBERSHIP GAPS
[CUSTOMER SERVICE perspective. Team configurations that create access loss or
over-permission. At least one row required unless null accountability is completed.]

| Scenario | Team(s) | Affected Users | Gap Type | Operational Impact |
|----------|---------|----------------|----------|--------------------|
| [Scenario] | [Team] | [Role or user type] | Missing membership / Over-combined | [What breaks or leaks] |

Null accountability (complete only if no gaps found):
- Teams examined: [List every team checked]
- Membership rules reviewed: [What was inspected -- default teams, owner teams, access teams]
- Justification: [One sentence -- why no team membership gap was found]

---

## TABLE 7: CONSOLIDATED FINDINGS
[Merge all gaps from TABLE 2 through TABLE 6. This table must have at least one row.
A trace with zero gaps is not a valid output. Each finding names a gap and resolves a
hypothesis. Do not describe the model -- name what is wrong.]

| # | Finding | Source Table | Type | H-link | H resolution | Risk | Justification |
|---|---------|--------------|------|--------|--------------|------|---------------|
| 1 | [Gap name] | TABLE [N] | FLS / Escalation / Sharing / Team | H1/H2/new | Confirmed / Refuted / Refined | H/M/L | [One line -- reference operation or data sensitivity] |
| 2 | [Gap name] | TABLE [N] | FLS / Escalation / Sharing / Team | H1/H2/new | Confirmed / Refuted / Refined | H/M/L | [One line] |

Hypothesis resolution summary:
- H1 (Escalation): [Confirmed / Refuted / Refined -- cite finding # or TABLE 4 result]
- H2 (FLS or Team): [Confirmed / Refuted / Refined -- cite finding # or source table]

---

## TABLE 8: REMEDIATION
[One concrete action per finding in TABLE 7. Map by finding number. "Tighten security"
or "review permissions" does not pass -- name the exact change.]

| Finding # | Remediation Action |
|-----------|--------------------|
| 1 | [e.g., "Add FLS read-deny on AccountNumber for Customer Service role in Dataverse security role editor. Supervisor role retains Allow."] |
| 2 | [Exact action -- field, role, configuration location] |

---

Write artifact: simulations/trace/permissions/{topic}-permissions-{date}.md
Frontmatter: skill, topic, date, roles_analyzed, operations_in_scope, platform,
escalation_vectors_found, escalation_vectors_cleared, hypotheses_confirmed,
hypotheses_refuted, gaps_count, highest_risk.
```

---

## V-03: Phrasing Register -- Imperative Checklist

**Axis:** Phrasing register -- all requirements expressed as imperative commands with
inline [ ] checklist markers; explicit MUST gates before advancing; null-finding protocol
stated as a rule the model must follow, not a template slot
**Hypothesis:** Converting requirements into imperative checklist items targets a
different compliance mechanism than table structure: the model is told explicitly what it
must not do ("Do not advance until all boxes are checked"), making omission a visible
violation rather than a missed section. The MUST language also calibrates specificity
expectations more aggressively than section headers alone. Tests whether phrasing register
alone (without phase gates or pre-printed tables) produces equivalent C-10/C-11/C-12
coverage, or whether the conversational register sacrifices structural enforcement.

```
You are running /trace-permissions. Your job is to find what is wrong with the current
permissions configuration. Read the following rules before you start.

RULE 1 -- HYPOTHESES FIRST: You must state at least two gap hypotheses before writing
any role-operation matrix, FLS table, or scope analysis. Do not advance to evidence
sections without completing the HYPOTHESES section. Hypotheses stated after evidence
tables do not count.

RULE 2 -- NULL FINDINGS REQUIRE EVIDENCE: If you write "None identified" or "No gaps
found" in any section, you must first name every control or configuration you examined
and provide one sentence explaining why no gap exists. "None identified" alone fails.

RULE 3 -- ESCALATION SWEEP IS EXHAUSTIVE: Privilege escalation analysis must cover all
four standard vectors: record reassignment, team promotion or membership elevation,
sharing rule bypass, and impersonation or delegation. Identifying one path and stopping
fails. Each vector must be either named (path found) or cleared (examination described).

RULE 4 -- GAPS ARE NAMED, NOT DESCRIBED: A trace that describes the permission model
without naming at least one specific misconfiguration, missing control, or over-permission
fails. "Field-level security should be configured" is not a named gap. "AccountNumber is
Allow-Read for Customer Service role and should be Deny" is a named gap.

RULE 5 -- REMEDIATIONS ARE EXACT: Every identified gap requires a concrete remediation
action naming the specific field, role, configuration, or team change required.
"Tighten security" or "improve FLS" fails.

Stock roles:
- SECURITY EXPERT: Dataverse security architect.
- CUSTOMER SERVICE: Customer Service team lead.

---

## STEP 1: SETUP

Read the repo for RBAC context. Then complete:

Platform: [Dataverse / Salesforce / Custom RBAC / other]
Roles found: [List all roles]
Operations in scope: [List all CRUD plus domain-specific operations]
Sensitive fields: [List fields that warrant FLS attention]
Teams: [List all teams]

[ ] Setup complete -- all fields above are filled in.

---

## STEP 2: HYPOTHESES (RULE 1 -- complete before Step 3)

State at least two expected security gaps. Each hypothesis must name: the gap type,
the specific role or field or team involved, and why this gap is plausible.

[ ] H1 (Escalation): [Role, likely mechanism, why plausible given the roles and operations
                      in scope. Example: "CS role can reassign Cases to supervisor queue --
                      if reassignment grants the supervisor scope, CS agents gain BU-wide
                      access to all accounts in the queue."]

[ ] H2 (FLS): [Specific field, specific role, why over-permission is likely.
               Example: "AccountNumber likely has no FLS restriction for CS role -- default
               Dataverse FLS does not restrict account number fields by role."]

[ ] H3 (optional, Team): [Team scenario and why it creates over-permission or access loss.
                          Example: "Agents on the Escalations team likely inherit org-wide
                          read from the team security role, exceeding their individual scope."]

Do not advance to Step 3 until all checked boxes above are completed.

---

## STEP 3: ROLE-OPERATION MATRIX

[ ] Map every operation in scope to every role. Do not list roles without tying them to
    operations (RULE 4 failure mode).

| Operation | [Role A] | [Role B] | [Role C] | [Role N] | H-flag |
|-----------|----------|----------|----------|----------|--------|
| Create    | Y/N/R    | Y/N/R    | Y/N/R    | Y/N/R    | [H1/H2/H3/--] |
| Read      | Y/N/R    | Y/N/R    | Y/N/R    | Y/N/R    |               |
| Update    | Y/N/R    | Y/N/R    | Y/N/R    | Y/N/R    |               |
| Delete    | Y/N/R    | Y/N/R    | Y/N/R    | Y/N/R    |               |
| [Op]      | Y/N/R    | Y/N/R    | Y/N/R    | Y/N/R    |               |

[R = restricted -- explain restrictions below]
Restrictions: [Explain every R cell]

[ ] All cells completed, no blanks.

---

## STEP 4: FIELD-LEVEL SECURITY

[ ] For every sensitive field, state Allow or Deny per role for read and write.
    Do not write "FLS should be configured" -- name the field and the role (RULE 4).

| Field | [Role] Read | [Role] Write | [Role] Read | [Role] Write | H-flag |
|-------|-------------|--------------|-------------|--------------|--------|
| [Field] | Allow/Deny | Allow/Deny | Allow/Deny | Allow/Deny | [H2/--] |

FLS gaps (fields where Allow is found but Deny is required):
- [Field] / [Role]: [Concrete description -- name the field, the role, and what the
                    Allow permission exposes that it should not]

[ ] If no FLS gaps found, complete null protocol (RULE 2):
    Fields examined: [List every sensitive field checked]
    Roles examined per field: [What was checked for each]
    Justification: [One sentence -- why no FLS gap exists]

---

## STEP 5: RECORD ACCESS SCOPE

[ ] State the scope for every role using the full hierarchy. Do not use only
    "users see their own records" -- that fails C-03.

| Role | Scope | Notes |
|------|-------|-------|
| [Role] | Own / Business Unit / Parent BU / Organization | [Scope anomalies or conflicts] |
| [Role] | Own / Business Unit / Parent BU / Organization |                               |

---

## STEP 6: PRIVILEGE ESCALATION -- FOUR-VECTOR SWEEP (RULE 3)

You MUST address all four vectors. For each vector: either name a found path (From Role,
Mechanism, Unintended Access Gained) or explicitly clear it (Examined + Justification).

[ ] Vector 1 -- Record Reassignment:
    Status: Found / Cleared
    Found: From [Role] -- reassigns [record type] to [target] -- gains [scope/operation unintended]
    Cleared: Examined [specific record types checked, reassignment permissions reviewed].
             [One sentence: why no path exists -- e.g., "reassignment restricted to System Admin."]

[ ] Vector 2 -- Team Promotion / Membership Elevation:
    Status: Found / Cleared
    Found: From [Role] -- via [team name/mechanism] -- gains [scope beyond individual role]
    Cleared: Examined [teams and their security roles]. [One sentence justification.]

[ ] Vector 3 -- Sharing Rule Bypass:
    Status: Found / Cleared
    Found: From [Role] -- sharing rule [name] -- grants [access beyond security role baseline]
    Cleared: Examined [sharing rules by name -- manual, criteria-based, owner-based].
             [One sentence: why no bypass is possible.]

[ ] Vector 4 -- Impersonation / Delegation:
    Status: Found / Cleared
    Found: From [Role] -- via [delegation feature] -- acts as [higher-privilege role]
    Cleared: Examined [impersonation and delegation features in scope].
             [One sentence: why this vector is not exploitable.]

H1 update: [How the four-vector sweep confirms, refutes, or refines H1]

Do not stop after finding one path -- all four vectors MUST be addressed.

---

## STEP 7: SHARING RULE CONFLICTS

[ ] Examine sharing rules for cases where access is widened beyond the security role
    scope established in Step 5, or where rules create contradictory grants.

Rule: [Name or description]
  Baseline scope for [Role]: [From Step 5]
  Sharing rule grants: [Wider or contradictory access]
  Conflict: [Describe the widening or contradiction concretely]

[ ] If no conflicts found, complete null protocol (RULE 2):
    Rules examined: [List every sharing rule by name or type]
    Justification: [One sentence -- why no widening or contradiction was found]

---

## STEP 8: TEAM MEMBERSHIP GAPS

[ ] CUSTOMER SERVICE: Identify team membership configurations that create access loss
    or unintended over-permission.

Gap 1:
  Scenario: [Team membership situation]
  Affected users: [Role or user type]
  Gap type: Missing membership / Over-combined permissions
  Impact: [What the agent cannot do, or what access is unintentionally granted]

[ ] If no gaps found, complete null protocol (RULE 2):
    Teams examined: [List every team, their membership rules, and the security roles inherited]
    Justification: [One sentence -- why no team membership gap was found]

---

## STEP 9: FINDINGS

[ ] Name at least one gap. A trace with no findings fails (RULE 4).
    Each finding must reference the step where evidence was found and resolve a hypothesis.

Finding 1:
  Gap name: [Short name]
  Type: FLS / Escalation / Sharing / Team
  Evidence: [Step number and specific cell or entry -- e.g., "Step 4: AccountNumber /
             Customer Service: Allow Read"]
  Hypothesis addressed: H1 / H2 / H3 / new
  H resolution: Confirmed / Refuted / Refined
  Details: [Concrete -- name fields, roles, mechanisms, what access is wrongly granted
            or denied. Do not restate the model.]

Finding 2:
  [Same structure]

Hypothesis resolution:
- H1: [Confirmed / Refuted / Refined -- cite finding name or Step 6 result]
- H2: [Confirmed / Refuted / Refined -- cite finding name or Step 4/8 result]
- H3 (if stated): [Confirmed / Refuted / Refined]

---

## STEP 10: RISK RANKING AND REMEDIATION

[ ] Rank all findings H/M/L. One-line justification per finding. Reference the operation
    type or data sensitivity -- not just the gap category.

| Finding | Risk | Justification |
|---------|------|---------------|
| [Name] | H/M/L | [e.g., "Billing identifier readable by all CS agents -- direct PCI exposure"] |

[ ] Provide a concrete remediation per finding (RULE 5). Name the exact change.

| Finding | Remediation Action |
|---------|--------------------|
| [Name] | [e.g., "Add FLS read-deny on AccountNumber for Customer Service role in Dataverse security role editor. Supervisor role retains Allow."] |

---

Write artifact: simulations/trace/permissions/{topic}-permissions-{date}.md
Frontmatter: skill, topic, date, roles_analyzed, operations_in_scope, platform,
hypotheses_confirmed, hypotheses_refuted, escalation_vectors_found,
escalation_vectors_cleared, gaps_count, highest_risk.
```

---

## V-04: Lifecycle + Four-Vector Table (V-01 + V-02 Combination)

**Axes:** Lifecycle emphasis (V-01) -- four hard phase gates targeting C-10 and C-11 +
output format four-vector escalation table (V-02) -- targeting C-12
**Hypothesis:** Phase gating (V-01) structurally guarantees C-10 by making hypothesis
pre-commitment a mandatory lifecycle phase that cannot be bypassed. The four-vector table
(V-02) structurally guarantees C-12 by pre-printing all four rows and requiring examination
logs for cleared vectors (C-11). Combining them covers the three new aspirational criteria
with two independent structural mechanisms, without the additional overhead of imperative
checklist formatting. Tests whether phase gates + table enforcement is sufficient without
the phrasing register of V-03.

```
You are running /trace-permissions. Analysis runs in four phases. Complete each phase
before advancing. Do not write evidence tables before Phase 1 is complete.

Stock roles:
- SECURITY EXPERT: Dataverse security architect.
- CUSTOMER SERVICE: Customer Service team lead.

---

## SETUP
Platform: [Dataverse / Salesforce / Custom RBAC / other]
Roles found: [All roles in scope]
Operations in scope: [CRUD plus domain-specific operations]
Sensitive fields: [Fields warranting FLS attention]
Teams: [All teams in scope]

---

## PHASE 1: PRE-COMMIT
[Complete before any evidence table. State what you expect to find wrong.
Findings in Phase 3 must address H1 and H2 by name.]

H1 (Escalation): [Role, expected escalation mechanism, why this vector is plausible.
                  Name the mechanism: record reassignment / team promotion / sharing rule
                  bypass / impersonation.]

H2 (FLS or Team): [Field and role (for FLS), or team scenario (for team gap), and why
                   over-permission or access loss is likely.]

PHASE 1 COMPLETE.

---

## PHASE 2: EVIDENCE GATHER

### 2-A: Role-Operation Matrix
[SECURITY EXPERT. Every operation mapped to every role. No role listed without an
operation. Complete every cell. Y = permitted, N = denied, R = restricted.]

| Operation | [Role A] | [Role B] | [Role C] | [Role N] |
|-----------|----------|----------|----------|----------|
| Create    |          |          |          |          |
| Read      |          |          |          |          |
| Update    |          |          |          |          |
| Delete    |          |          |          |          |
| [Op]      |          |          |          |          |

Restrictions: [Explain every R cell]

### 2-B: Field-Level Security
[SECURITY EXPERT. Name field, role, and Allow/Deny for read and write.
"FLS should be configured" without naming fields and roles fails.]

| Field | [Role] Read | [Role] Write | [Role] Read | [Role] Write | FLS Gap? |
|-------|-------------|--------------|-------------|--------------|----------|
| [Field] |           |              |             |              | Y: [describe] / N |

Null accountability (if all FLS Gap cells are N):
- Examined: [Every sensitive field and the roles checked against it]
- Justification: [One sentence -- why no FLS gap exists]

### 2-C: Record Access Scope
[SECURITY EXPERT. Scope per role using Own / Business Unit / Parent BU / Organization.
Do not conflate role privileges with record ownership.]

| Role | Scope | Correct? | Notes |
|------|-------|----------|-------|
| [Role] | Own / BU / Parent BU / Org | Y/N | [If N: expected scope and reason] |

### 2-D: FOUR-VECTOR ESCALATION SWEEP
[SECURITY EXPERT. Complete all four rows. Found = describe the path by naming From-Role,
Mechanism, Unintended Access Gained. Cleared = name what was examined and provide one
sentence justification. Do not leave any cell blank. "None identified" without examination
log and justification fails C-11 and C-12.]

| Vector | Status | Named Path OR Examination Log + Justification |
|--------|--------|-----------------------------------------------|
| Record Reassignment | Found / Cleared | Found: [From Role] via [mechanism/target] gains [scope or operation]. OR Cleared: Examined [record types, reassignment permission settings]. [One sentence -- e.g., "Reassignment restricted to System Administrator; no path available to CS or supervisor roles."] |
| Team Promotion / Membership Elevation | Found / Cleared | Found: [From Role] via [team name] gains [scope beyond individual role]. OR Cleared: Examined [teams and their associated security roles]. [One sentence justification.] |
| Sharing Rule Bypass | Found / Cleared | Found: [From Role] via [sharing rule name] gains [scope beyond 2-C baseline]. OR Cleared: Examined [sharing rules by name -- list them]. [One sentence -- e.g., "All three criteria-based rules are scope-narrowing relative to role baseline."] |
| Impersonation / Delegation | Found / Cleared | Found: [From Role] via [delegation mechanism] acts as [higher-privilege role]. OR Cleared: Examined [delegation features: list what was checked]. [One sentence justification.] |

H1 update: [How TABLE 2-D confirms, refutes, or refines H1]

### 2-E: Sharing Rule Conflicts
[SECURITY EXPERT. Rules that widen access beyond 2-C scope or create contradictory grants.]

Rule: [Name]
  Baseline scope for [Role]: [From 2-C]
  Sharing rule grants: [Wider or contradictory]
  Conflict: [Concrete description]

Null accountability (if no conflicts found):
- Examined: [Every sharing rule by name or type]
- Justification: [One sentence]

### 2-F: Team Membership Gaps
[CUSTOMER SERVICE. Access loss or over-permission from team configuration.]

Gap 1:
  Scenario: [Team membership situation]
  Affected users: [Role or user type]
  Gap type: Missing membership / Over-combined
  Impact: [Operational consequence]

Null accountability (if no gaps found):
- Examined: [Every team, membership rules, and roles involved]
- Justification: [One sentence]

PHASE 2 COMPLETE.

---

## PHASE 3: FINDINGS
[Minimum one finding. Each finding names a gap, references Phase 2 evidence, and
resolves a hypothesis. Do not advance to Phase 4 without at least one finding.]

Finding 1:
  Gap name: [Short name]
  Type: FLS / Escalation / Sharing / Team
  Evidence: [Phase 2 section and specific entry]
  Hypothesis addressed: H1 / H2 / new
  H resolution: Confirmed / Refuted / Refined
  Details: [Concrete -- name fields, roles, mechanisms, scope impact]

Finding 2:
  [Same structure]

Hypothesis resolution summary:
- H1 (Escalation): [Confirmed / Refuted / Refined -- cite finding or 2-D result]
- H2 (FLS or Team): [Confirmed / Refuted / Refined -- cite finding or 2-B/2-F result]

PHASE 3 COMPLETE.

---

## PHASE 4: SYNTHESIS

### Risk Ranking
[All findings ranked H/M/L. One-line justification per finding -- reference operation
type or data sensitivity.]

| Finding | Risk | Justification |
|---------|------|---------------|
| [Name] | H/M/L | [One line -- reference operation or data sensitivity] |

### Remediation
[Concrete action per finding. Name the exact change. "Tighten security" fails.]

| Finding | Remediation Action |
|---------|--------------------|
| [Name] | [e.g., "Add FLS read-deny on AccountNumber for Customer Service role in Dataverse security role editor. Supervisor role retains Allow."] |

---

Write artifact: simulations/trace/permissions/{topic}-permissions-{date}.md
Frontmatter: skill, topic, date, roles_analyzed, operations_in_scope, platform,
hypotheses_confirmed, hypotheses_refuted, escalation_vectors_found,
escalation_vectors_cleared, gaps_count, highest_risk.
```

---

## V-05: Full R2 Synthesis (Lifecycle + Four-Vector Table + Imperative Checklist)

**Axes:** Lifecycle emphasis (V-01) + four-vector escalation table (V-02) + imperative
checklist phrasing register (V-03); null-accountability template slots built into every
Phase 2 section; hypothesis pre-commitment is phase-gated AND checkboxed; four-vector
sweep is table-enforced AND checkboxed; every null finding requires an examination log
**Hypothesis:** Maximum structural coverage of C-10/C-11/C-12 simultaneously. Three
independent enforcement mechanisms: (1) phase gate prevents evidence before hypothesis --
C-10 cannot be bypassed by reordering sections; (2) pre-printed four-vector table with
mandatory examination-log column -- C-12 cannot produce a single-vector answer; (3) null-
accountability template in every section plus imperative register -- C-11 cannot produce
a bare "None identified." V-04 is the closest competitor: same C-10 and C-12 guarantees
without imperative register overhead. V-05 adds C-11 coverage across all sections through
the combination of template slots and RULE 2 framing.

```
You are running /trace-permissions. Your goal is to find what is wrong with the current
permissions configuration. Read the three rules before starting.

RULE 1 -- HYPOTHESES BEFORE EVIDENCE: You must complete the PHASE 1: PRE-COMMIT section
before writing any evidence table. Hypotheses written after evidence tables do not count
toward C-10 compliance. The phase gate is enforced by section order -- do not proceed to
Phase 2 without checking the Phase 1 completion box.

RULE 2 -- NULL FINDINGS REQUIRE EXAMINATION LOGS: In every Phase 2 section, if no gap
is found, you must name every control or configuration you examined and provide one
sentence explaining why no gap exists. "None identified" alone fails every time.

RULE 3 -- FOUR-VECTOR SWEEP IS EXHAUSTIVE: The four-vector escalation table has four
rows. All four must be completed. One path found does not satisfy the remaining three
vectors. Each cleared vector requires an examination log + one-sentence justification.

Stock roles:
- SECURITY EXPERT: Dataverse security architect with deep knowledge of security roles,
  field-level security, sharing rules, and privilege escalation patterns.
- CUSTOMER SERVICE: Customer Service team lead who knows what agents need to see and
  where they get blocked or accidentally over-permitted.

SECURITY EXPERT leads Phases 2-A through 2-D. CUSTOMER SERVICE leads Phase 2-E.
Both perspectives merge into Phase 3 findings.

---

## SETUP
Platform: [Dataverse / Salesforce / Custom RBAC / other]
Roles found: [All roles in scope -- from codebase or inferred from context]
Operations in scope: [All CRUD plus domain-specific operations]
Sensitive fields: [Fields warranting FLS attention]
Teams: [All teams in scope]

[ ] Setup complete.

---

## PHASE 1: PRE-COMMIT (RULE 1 -- complete before Phase 2)

[ ] H1 (Escalation): [Name the role. Name the expected escalation mechanism: record
                      reassignment / team promotion / sharing rule bypass / impersonation.
                      State why this vector is plausible given the roles and operations in
                      scope. Example: "CS agents can reassign Cases to the Escalations queue.
                      If the Escalations team has Org-wide read on Account, any CS agent who
                      reassigns a case gains read access to all Accounts in the org."]

[ ] H2 (FLS): [Name the specific sensitive field. Name the role that likely has Allow when
               Deny is appropriate. State why over-permission is likely. Example: "AccountNumber
               is likely not FLS-restricted for the Customer Service role -- default Dataverse
               configurations do not restrict standard account fields by role unless explicitly
               configured."]

[ ] H3 (Team, optional but recommended): [Name the team scenario. State the affected user
                                          type and why over-permission or access loss is
                                          likely. Example: "Agents on the Tier-2 team likely
                                          inherit BU-wide write from the team's security role,
                                          exceeding their individual Own-scope write permission."]

Do not write any evidence table until all checked boxes above are completed.

PHASE 1 COMPLETE [ ] -- check this box before starting Phase 2.

---

## PHASE 2: EVIDENCE GATHER

### 2-A: Role-Operation Matrix
[SECURITY EXPERT. Every operation mapped to every role. Complete every cell.
Y = permitted, N = denied, R = restricted (explain below).]

| Operation | [Role A] | [Role B] | [Role C] | [Role N] | H-flag |
|-----------|----------|----------|----------|----------|--------|
| Create    |          |          |          |          | [H1/H2/H3/--] |
| Read      |          |          |          |          |               |
| Update    |          |          |          |          |               |
| Delete    |          |          |          |          |               |
| [Op]      |          |          |          |          |               |

Restrictions: [Explain every R cell -- what the restriction is and what triggers it]

[ ] All cells completed, H-flags marked where relevant.

### 2-B: Field-Level Security
[SECURITY EXPERT. Name field, role, and Allow/Deny. "FLS should be configured" without
naming fields and roles fails. Complete every cell. Flag cells relevant to H2.]

| Field | [Role] Read | [Role] Write | [Role] Read | [Role] Write | FLS Gap? | H-flag |
|-------|-------------|--------------|-------------|--------------|----------|--------|
| [Field] |           |              |             |              | Y: [describe] / N | H2/-- |
| [Field] |           |              |             |              | Y: [describe] / N |       |

FLS gaps (fields where Allow is found but Deny is appropriate):
- [Field] / [Role]: [Concrete description -- name the exposure]

[ ] If all FLS Gap cells are N (RULE 2 -- complete before advancing):
    Fields examined: [List every sensitive field checked]
    Roles examined per field: [What roles were checked against each field]
    Justification: [One sentence -- why no FLS gap exists]

### 2-C: Record Access Scope
[SECURITY EXPERT. Scope per role using full hierarchy. Do not conflate privilege with
record ownership. Mark H-flag for scopes relevant to H1 or H3.]

| Role | Scope | Correct? | Notes | H-flag |
|------|-------|----------|-------|--------|
| [Role] | Own / Business Unit / Parent BU / Organization | Y/N | [If N: expected scope and reason] | H1/H3/-- |
| [Role] | Own / Business Unit / Parent BU / Organization | Y/N |                                   |          |

[ ] All roles mapped to scope hierarchy.

### 2-D: FOUR-VECTOR ESCALATION SWEEP (RULE 3)
[SECURITY EXPERT. All four rows required. Found = named path (From-Role, Mechanism,
Unintended Access Gained). Cleared = examination log + one-sentence justification.
Do not leave any cell blank. H1 update required at the end of this section.]

| Vector | Status | Named Path OR Examination Log + Justification |
|--------|--------|-----------------------------------------------|
| Record Reassignment | Found / Cleared | Found: From [Role] -- reassigns [record type] to [target] -- gains [specific scope or operation not normally permitted]. OR Cleared: Examined [record types in scope, which roles have reassignment permission, reassignment configuration]. [One sentence -- e.g., "Reassignment is restricted to System Administrator; no other role can change record ownership."] |
| Team Promotion / Membership Elevation | Found / Cleared | Found: From [Role] -- via team [name] -- gains [scope or operation beyond individual role scope]. OR Cleared: Examined [list each team, their associated security roles, and team membership rules]. [One sentence -- e.g., "No team security role exceeds the highest individual role scope; no promotion path exists."] |
| Sharing Rule Bypass | Found / Cleared | Found: From [Role] -- sharing rule [name] -- grants [specific access beyond security role scope in 2-C]. OR Cleared: Examined sharing rules: [list by name or type -- manual rules, criteria-based rules, owner-based rules]. [One sentence -- e.g., "All three criteria-based rules are scope-narrowing; no rule grants access beyond the security role baseline."] |
| Impersonation / Delegation | Found / Cleared | Found: From [Role] -- via [delegation feature or mechanism] -- acts as [higher-privilege role] and gains [specific access]. OR Cleared: Examined [impersonation features: service accounts, run-as capabilities, delegation settings]. [One sentence -- e.g., "No delegation mechanism is configured for non-administrator roles."] |

[ ] All four vectors addressed.
H1 update: [How this sweep confirms, refutes, or refines H1 as stated in Phase 1]

### 2-E: Sharing Rule Conflicts
[SECURITY EXPERT. Rules that widen access beyond 2-C scope or create contradictory grants.
Examine manual, criteria-based, and owner-based rules.]

Rule: [Name or description]
  Baseline scope for [Role]: [From 2-C]
  Sharing rule grants: [Access beyond baseline or contradictory]
  Conflict: [Concrete -- describe the widening or contradiction]

[ ] If no conflicts found (RULE 2 -- complete before advancing):
    Rules examined: [List every sharing rule by name or type]
    Justification: [One sentence -- why no widening or contradiction was found]

### 2-F: Team Membership Gaps
[CUSTOMER SERVICE. Team configurations that create access loss or over-permission.]

Gap 1:
  Scenario: [Team membership situation]
  Affected users: [Role or user type]
  Gap type: Missing membership / Over-combined permissions
  Operational impact: [What breaks or what access leaks]
  H-flag: [H3/new]

[ ] If no gaps found (RULE 2 -- complete before advancing):
    Teams examined: [Every team, their membership rules, and security roles inherited]
    Justification: [One sentence -- why no team membership gap was found]

PHASE 2 COMPLETE [ ] -- check this box before starting Phase 3.

---

## PHASE 3: FINDINGS
[Minimum one finding required. Each finding names a gap (not describes the model),
references Phase 2 evidence, and resolves a hypothesis. Do not advance to Phase 4
without at least one finding with a hypothesis resolution.]

Finding 1:
  Gap name: [Short name]
  Type: FLS / Escalation / Sharing / Team
  Evidence: [Phase 2 section and specific entry -- e.g., "2-B: AccountNumber /
             Customer Service: Allow Read"]
  Hypothesis addressed: H1 / H2 / H3 / new
  H resolution: Confirmed / Refuted / Refined
  Resolution notes: [What the evidence showed relative to the hypothesis as stated in
                    Phase 1 -- was the mechanism correct? the field? the scope?]
  Details: [Concrete -- name fields, roles, mechanisms, what access is wrongly granted
            or denied. Do not restate the model description.]

Finding 2:
  Gap name: [Short name]
  Type: FLS / Escalation / Sharing / Team
  Evidence: [Phase 2 reference]
  Hypothesis addressed: H1 / H2 / H3 / new
  H resolution: Confirmed / Refuted / Refined
  Resolution notes: [Evidence relative to hypothesis]
  Details: [Concrete]

[Add findings as warranted. If a hypothesis is refuted, note what was examined and why
no gap was found in that category.]

Hypothesis resolution summary:
- H1 (Escalation): [Confirmed / Refuted / Refined -- cite finding name or Phase 2-D result]
- H2 (FLS): [Confirmed / Refuted / Refined -- cite finding name or Phase 2-B result]
- H3 (Team, if stated): [Confirmed / Refuted / Refined -- cite finding or Phase 2-F result]

[ ] At least one finding completed with hypothesis resolution.

PHASE 3 COMPLETE [ ] -- check this box before starting Phase 4.

---

## PHASE 4: SYNTHESIS

### Risk Ranking
[All findings H/M/L. One-line justification per finding. Reference operation type or
data sensitivity -- not just the gap category.]

| Finding | Risk | Justification |
|---------|------|---------------|
| [Name] | H/M/L | [e.g., "Billing identifier readable by all CS agents -- direct PCI exposure"] |
| [Name] | H/M/L | [One line -- data sensitivity or operation type] |

### Remediation
[One concrete action per finding. Name the exact change: field, role, configuration,
or team. "Tighten security" or "review FLS" fails.]

| Finding | Remediation Action |
|---------|--------------------|
| [Name] | [e.g., "Add FLS read-deny on AccountNumber for Customer Service role in Dataverse security role editor. Supervisor role retains Allow."] |
| [Name] | [Exact action] |

---

Write artifact: simulations/trace/permissions/{topic}-permissions-{date}.md
Frontmatter: skill, topic, date, roles_analyzed, operations_in_scope, platform,
hypotheses_confirmed, hypotheses_refuted, hypotheses_refined,
escalation_vectors_found, escalation_vectors_cleared,
cs_gaps, se_gaps, total_gaps, highest_risk.
```

---

## Round 2 Design Notes

### Variation axis selection for R2

Three single-axis variations targeting the new rubric criteria:
- V-01 tests **lifecycle emphasis**: does hard phase gating prevent hypothesis omission
  (C-10) and force null accountability (C-11) without table enforcement?
- V-02 tests **output format -- four-vector table**: does pre-printing all four escalation
  rows with examination-log columns structurally guarantee C-12 and C-11 for escalation
  without requiring phase gates?
- V-03 tests **phrasing register**: does imperative/checklist language targeting C-10/C-11/
  C-12 via MUST commands and [ ] markers produce equivalent structural coverage to phase
  gates or table enforcement, with lower template overhead?

Two combination variations:
- V-04 (axes 1+2): phase gates (C-10) + four-vector table (C-12). Tests whether C-11 is
  adequately covered by the null-accountability blocks inside V-01's phase structure without
  needing the imperative register of V-03.
- V-05 (all three axes): Full synthesis. Maximum structural coverage. Phase gate cannot be
  bypassed; four-vector table cannot be partially completed; null findings require examination
  logs enforced by both template and imperative register.

### C-10/C-11/C-12 mechanism comparison

| V | C-10 mechanism | C-11 mechanism | C-12 mechanism |
|---|----------------|----------------|----------------|
| V-01 | Phase 1 gate | Null-accountability blocks in each Phase 2 section | Four-vector prose section with explicit vector names |
| V-02 | Hypothesis section before tables (same as R1 V-03) | Examination-log column in TABLE 4 four-vector table | Pre-printed four-row TABLE 4 with mandatory completion |
| V-03 | RULE 1 + Phase 1 checkboxes | RULE 2 + null protocol after each section | RULE 3 + four-vector step with per-vector checkboxes |
| V-04 | Phase 1 gate | Null-accountability blocks in Phase 2 | Pre-printed four-row table in 2-D |
| V-05 | Phase 1 gate + RULE 1 + checkboxes | RULE 2 + null-accountability template in every section | RULE 3 + pre-printed four-row table + per-row checkboxes |

### C-11 coverage breadth comparison

C-11 requires null accountability not just for escalation but for every recommended
section (escalation, sharing rules, team membership). V-01 and V-05 include null-
accountability blocks in all three sections (2-D, 2-E, 2-F). V-02's examination-log
column only covers the escalation table; sharing rules and team membership use a
separate "Null accountability" block appended to those sections. V-03 applies RULE 2
globally. V-04 covers all three via null-accountability blocks inherited from V-01.

### R1 connection

R1 open question: does hypothesis anchoring improve specificity relative to table
enforcement? R2 V-03 isolates whether phrasing register alone produces C-10/C-11/C-12
without table enforcement. If V-03 scores comparably to V-04 on C-12, phrasing register
is sufficient for the four-vector sweep. If V-04 outscores V-03 on C-12, table structure
is required -- same conclusion as R1's V-02 vs V-03 finding for C-04.

### V-golden candidate for R2

**V-05** is the direct synthesis target:
- Three independent C-10 mechanisms (phase gate, RULE 1, checkboxes)
- C-11 coverage in every Phase 2 section via template + RULE 2
- C-12 via pre-printed four-row table + RULE 3 + per-row checkboxes
- H-flags tie evidence to hypotheses (C-04 specificity)
- Hypothesis resolution summary in Phase 3 (hypothesis integrity)

**V-04** is the closest competitor: same C-10 and C-12 guarantees, C-11 coverage in
all Phase 2 sections, lower template overhead than V-05. If V-04 scores within 3 points
of V-05 on the rubric, V-04 is the better production candidate.
