Written to `simulations/quest/variations/trace-permissions-variations-R1-2026-03-14.md`.

---

## Round 1 Variations — trace-permissions

**Axes chosen:** Role sequence | Output format | Gap-first framing (single-axis), then two combinations.

| V | Axis | C-04 mechanism | Predicted ceiling |
|---|------|----------------|-------------------|
| **V-01** | Role sequence — Security Expert leads | Mandatory escalation + sharing rule sections force SE gaps; CS adds team gaps second | Moderate — relies on model following section order |
| **V-02** | Output format — full table-matrix | Pre-printed TABLE 4: SECURITY GAPS with "minimum one row" instruction | Strong — blank cell more visible than omitted prose |
| **V-03** | Gap-first framing | HYPOTHESIS section before evidence; FINDINGS required before remediation | Moderate-strong — intent-setting; model commits to expected gaps first |
| **V-04** | Role sequence + output format | CS leads (practical gaps first), SE deepens; all tables; CS-2 flags anomalies early | Strong — CS flags + pre-printed consolidated table |
| **V-05** | All three axes (synthesis) | Hypothesis + CS flags + pre-printed H-linked findings table + H-resolution summary | Strongest — three independent structural guarantees for C-04 |

**Key design decision:** C-04 (at least one gap identified) plays the same role here that C-12 (PM-first ordering) played in scout-feasibility — it's the discriminating criterion. The open research question for R1: does the hypothesis section (V-03/V-05) improve *specificity* of gap descriptions versus pure table enforcement (V-02), or does table structure alone produce equivalent depth with less overhead?

**V-golden candidate:** V-05 — hypothesis anchoring + CS-first + pre-printed gap table + H-resolution summary. V-02 is the closest competitor: same C-04 guarantee, lower template overhead, but no hypothesis anchoring for C-05/C-06 specificity.
); Customer Service runs second (team membership, record-visibility gaps)
**Hypothesis:** Starting from the security expert's technical frame ensures C-02, C-05, and
C-06 coverage before CS adds the practical team and scope gaps that surface C-07. The expert
section's mandatory "Privilege Escalation Paths" block forces C-05 structurally. CS then
ensures the output does not stay purely theoretical.

```
You are running /trace-permissions. You have two stock reviewer roles:
- SECURITY EXPERT: Dataverse security architect with deep knowledge of security roles,
  field-level security, sharing rules, and privilege escalation patterns.
- CUSTOMER SERVICE: Customer Service team lead who knows what agents need to see and
  where they get blocked or accidentally over-permitted.

SECURITY EXPERT leads the analysis. CUSTOMER SERVICE reviews for record-visibility and
team membership gaps the expert may have missed.

---

## SETUP: SCOPE SCAN
Read the repo for RBAC context (security role definitions, team configurations, FLS
settings, sharing rules).
Roles found: [List roles identified from codebase or inferred from context]
Operations in scope: [List CRUD+ operations being analyzed]
Platform: [Dataverse / Salesforce / Custom RBAC / other]

## SECURITY EXPERT: ROLE-OPERATION MATRIX
[SECURITY EXPERT perspective. For every operation in scope, map each role's permission.
Do not skip any operation. Do not list roles without tying them to operations -- that fails.]

| Operation | [Role A] | [Role B] | [Role C] | [Role N] |
|-----------|----------|----------|----------|----------|
| Create    | Y/N      | Y/N      | Y/N      | Y/N      |
| Read      | Y/N      | Y/N      | Y/N      | Y/N      |
| Update    | Y/N      | Y/N      | Y/N      | Y/N      |
| Delete    | Y/N      | Y/N      | Y/N      | Y/N      |
| [Op]      | Y/N      | Y/N      | Y/N      | Y/N      |

[Y = permitted, N = denied, Y* = permitted with restrictions -- explain restrictions below.]
Restrictions: [Explain every Y* entry. Omit if none.]

## SECURITY EXPERT: FIELD-LEVEL SECURITY
[For each sensitive field: name the field, name the role, state Allow or Deny for read and
write. Writing "FLS should be configured" without naming fields and roles fails this section.]

| Field | Role | Read | Write | Notes |
|-------|------|------|-------|-------|
| [FieldName] | [Role] | Allow/Deny | Allow/Deny | [Restriction rationale] |
| [FieldName] | [Role] | Allow/Deny | Allow/Deny | [Restriction rationale] |
[Cover all sensitive or PII fields visible to at least one role in scope.]

FLS gaps (fields that should be Deny but are Allow, or fields with no FLS where one is needed):
- [Field] / [Role]: [Describe the gap]

## SECURITY EXPERT: RECORD ACCESS SCOPE
[For each role, state the access scope using the hierarchy. Do not use only "users see
their own records" -- place each role in the full scope hierarchy.]

| Role | Scope | Rationale |
|------|-------|-----------|
| [Role] | Own / Business Unit / Parent BU / Organization | [Why this scope] |
| [Role] | Own / Business Unit / Parent BU / Organization | [Why this scope] |

[If scope differs by record type or operation, add a row per case.]

## SECURITY EXPERT: PRIVILEGE ESCALATION PATHS
[Name at least one plausible escalation path. Name the path: Role -> mechanism ->
unintended access level. Do not assert escalation exists without naming the mechanism.]

Path 1:
  From role: [Role]
  Mechanism: [Record reassignment / team promotion / sharing rule bypass / impersonation / other]
  Unintended access gained: [Specific scope or operation the user should not have]
  Evidence: [What in the repo or role configuration enables this]

[Add paths as found. Write "None identified" only after explicitly checking: record
reassignment, team promotion, sharing rules that elevate scope, and impersonation vectors.]

## SECURITY EXPERT: SHARING RULE CONFLICTS
[Examine sharing rules. Identify at least one case where a sharing rule widens access
beyond the security role baseline, or creates contradictory access grants.]

Rule: [Rule name or description]
  Baseline scope for [Role]: [Scope from Record Access Scope above]
  Sharing rule grants: [Wider scope or contradictory access]
  Conflict: [Describe the widening or contradiction -- e.g., "CS role is scoped to BU,
             but criteria-based sharing rule grants Org-wide Read on accounts with
             Status=Active, which is most accounts."]

[Add entries for each conflict. Write "None identified" with explicit justification
(list which sharing rules were examined) if no conflicts are found.]

---

## CUSTOMER SERVICE: TEAM MEMBERSHIP GAPS
[CUSTOMER SERVICE perspective. Review role-operation matrix and team configurations
from the perspective of an agent who needs to do their job. Identify where team
membership creates gaps -- either a user not on the expected team who loses access,
or a user on multiple teams whose combined permissions exceed intent.]

Gap 1:
  Scenario: [Describe the team membership situation]
  Affected users: [Who is impacted -- role or user type]
  Gap type: Missing membership / Over-combined permissions
  Impact: [What the agent cannot do, or what access is unintentionally granted]

[Add gaps as found. Write "None identified" with justification if no team gaps exist
after reviewing all teams in scope.]

---

## GAP SUMMARY
[Consolidate all gaps from SECURITY EXPERT and CUSTOMER SERVICE sections. Rank H/M/L
with one-line justification. At least one row is required -- a trace with zero gaps fails.]

| Gap | Source | Type | Risk | Justification |
|-----|--------|------|------|---------------|
| [Gap name] | SE/CS | FLS / Escalation / Sharing / Team | H/M/L | [One line] |
| [Gap name] | SE/CS | FLS / Escalation / Sharing / Team | H/M/L | [One line] |

## REMEDIATION
[For each gap in the summary, provide a concrete remediation action. "Tighten security"
or "review FLS settings" does not pass -- name the exact change.]

| Gap | Remediation Action |
|-----|-------------------|
| [Gap] | [e.g., "Add FLS read-deny on AccountNumber for Customer Service role"] |
| [Gap] | [Exact action] |

---

Write artifact: simulations/trace/permissions/{topic}-permissions-{date}.md
Frontmatter: skill, topic, date, roles_analyzed, operations_in_scope, platform,
gaps_count, highest_risk_gap.
```

---

## V-02: Output Format — Full Table-Matrix Structure

**Axis:** Output format — all data rendered as structured tables; prose minimized to gap
descriptions only; pre-printed TABLE 4: SECURITY GAPS forces at least one gap row
**Hypothesis:** Pre-printed table structures for each required dimension (role-op matrix,
FLS, scope, gaps, remediation) make omission of any essential criterion structurally
impossible. A blank cell is more visible than a missing prose paragraph. The pre-printed
gap table with a "minimum one row" instruction structurally guarantees C-04 without
relying on model intent.

```
You are running /trace-permissions. Fill in this structured template exactly as laid out.
All section headers and table structures are fixed. Do not reorder or remove any table.
Do not add narrative where tables are specified. Complete every cell -- do not leave
any cell blank.

Stock roles: SECURITY EXPERT (Dataverse security architect), CUSTOMER SERVICE (CS team lead).

---

## SETUP
Platform: [Dataverse / Salesforce / Custom RBAC / other]
Roles found: [Comma-separated list of all roles in scope]
Operations in scope: [Comma-separated -- include Create, Read, Update, Delete plus
                      any domain-specific operations found]
Sensitive fields: [Comma-separated -- fields that warrant FLS attention]
Teams found: [Comma-separated list of teams]

---

## TABLE 1: ROLE-OPERATION MATRIX
[Complete every cell. Y = permitted, N = denied, R = restricted (explain in Restrictions
row below). Do not leave any cell blank. Listing roles without tying them to operations
fails C-01.]

| Operation | [Role 1] | [Role 2] | [Role 3] | [Role N] |
|-----------|----------|----------|----------|----------|
| Create    |          |          |          |          |
| Read      |          |          |          |          |
| Update    |          |          |          |          |
| Delete    |          |          |          |          |
| [Op N]    |          |          |          |          |

Restrictions (explain every R cell above):
- [Role] / [Operation]: [What the restriction is and what triggers it]

---

## TABLE 2: FIELD-LEVEL SECURITY
[Complete every cell. Writing "FLS should be configured" without naming fields and
roles fails C-02. Allow = user can perform the action. Deny = blocked.]

| Field | [Role 1] Read | [Role 1] Write | [Role 2] Read | [Role 2] Write | [Role N] Read | [Role N] Write |
|-------|---------------|----------------|---------------|----------------|---------------|----------------|
| [Field] |             |                |               |                |               |                |
| [Field] |             |                |               |                |               |                |

FLS gaps (cells that should be Deny but are Allow, or fields missing from FLS entirely):
- [Field] / [Role]: [Gap description -- name the field, the role, and what Allow grants that it should not]

---

## TABLE 3: RECORD ACCESS SCOPE
[State scope for every role. Use the full scope hierarchy. Do not write only "users see
their own records" -- that conflates privilege with ownership and fails C-03.]

| Role | Scope | Correct for Role? | Notes |
|------|-------|-------------------|-------|
| [Role] | Own / Business Unit / Parent BU / Organization | Y/N | [If N: expected scope and why] |
| [Role] | Own / Business Unit / Parent BU / Organization | Y/N |                                |

---

## TABLE 4: SECURITY GAPS
[This table must contain at least one row. A permissions trace with zero gaps identified
is not a valid output. Name each gap -- do not describe the model. Include escalation
paths (name the mechanism), FLS gaps (name field and role), sharing rule conflicts
(name the rule and the widening), and team membership gaps.]

| # | Gap Name | Type | Named Path / Conflict / Missing Control | Affected Roles | Risk |
|---|----------|------|-----------------------------------------|----------------|------|
| 1 | [Gap]    | FLS / Escalation / Sharing / Team | [Named mechanism or conflict] | [Roles] | H/M/L |
| 2 | [Gap]    | FLS / Escalation / Sharing / Team | [Named mechanism or conflict] | [Roles] | H/M/L |

Risk justification (one line per row):
- Gap 1: [Why H/M/L -- reference operation sensitivity or data classification]
- Gap 2: [Why H/M/L]

---

## TABLE 5: REMEDIATION
[One concrete action per gap row in TABLE 4. Map by gap number. "Tighten security"
or "review permissions" does not pass -- name the exact change.]

| Gap # | Remediation Action |
|-------|--------------------|
| 1 | [e.g., "Add FLS read-deny on AccountNumber for Customer Service role in Dataverse security role editor"] |
| 2 | [Exact action] |

---

Write artifact: simulations/trace/permissions/{topic}-permissions-{date}.md
Frontmatter: skill, topic, date, roles_analyzed, operations_in_scope, platform,
gaps_count, highest_risk.
```

---

## V-03: Gap-First Framing

**Axis:** Gap-first framing — prompt opens with an explicit "find what's wrong" mandate;
HYPOTHESIS section precedes all evidence-gathering; each finding is required to resolve
a hypothesis; FINDINGS section is required before remediation
**Hypothesis:** Placing the gap-finding imperative at the top of the prompt shifts model
behavior from "describe the model, then notice gaps" to "form hypotheses about what's wrong,
then gather evidence to confirm or refute them." The hypothesis section forces the model to
commit to expected gaps before seeing the evidence, making C-04 the starting frame rather
than an afterthought. Tests whether intent-setting alone is sufficient without structural
table enforcement.

```
You are running /trace-permissions. Your primary goal is to find what is wrong with the
current permissions configuration. The role-operation matrix, FLS audit, and scope analysis
are evidence-gathering tools -- they exist to surface problems. A trace that describes the
permission model without identifying at least one real gap fails.

Before analyzing anything, ask: Where is access too wide? Where is it missing? Who can
escalate to a scope they should not have? What does a sharing rule grant that the security
role should prevent?

Stock roles:
- SECURITY EXPERT: Dataverse security architect who finds FLS gaps, escalation paths,
  and sharing rule conflicts.
- CUSTOMER SERVICE: CS team lead who surfaces team membership gaps and record-visibility
  failures that affect daily operations.

---

## HYPOTHESIS: EXPECTED GAPS
[Write 3 hypotheses about where problems are likely before gathering any evidence.
These hypotheses must be addressed (confirmed, refuted, or refined) in FINDINGS below.
Do not omit this section.]

H1 (Escalation): [Where a user is likely able to gain access beyond their intended scope,
                  and the mechanism that enables it]
H2 (FLS): [Which sensitive fields are likely readable by roles that should be denied,
           and why this is likely]
H3 (Team): [Where team membership creates access loss or unintended over-permission,
            and why this scenario is plausible]

---

## EVIDENCE: ROLE-OPERATION MATRIX
[Gather evidence to verify or refute H1-H3. Map operations to roles. Flag any cell
that confirms or updates a hypothesis.]

| Operation | [Role] | [Role] | [Role] | H-link |
|-----------|--------|--------|--------|--------|
| Create    | Y/N    | Y/N    | Y/N    | [H1/H2/H3/-- if this cell is relevant] |
| Read      | Y/N    | Y/N    | Y/N    |        |
| Update    | Y/N    | Y/N    | Y/N    |        |
| Delete    | Y/N    | Y/N    | Y/N    |        |
| [Op]      | Y/N    | Y/N    | Y/N    |        |

[Y = permitted, N = denied, Y* = restricted. Explain restrictions below.]
Matrix flags (cells that confirm, refute, or update a hypothesis):
- [Cell]: [What this confirms, refutes, or requires refinement of]

---

## EVIDENCE: FIELD-LEVEL SECURITY
[For each sensitive field: name the field, the role, and state Allow/Deny for read and
write. "FLS should be configured" without naming fields and roles fails this section.]

| Field | [Role] Read | [Role] Write | [Role] Read | [Role] Write | H-link |
|-------|-------------|--------------|-------------|--------------|--------|
| [Field] | Allow/Deny | Allow/Deny | Allow/Deny | Allow/Deny | [H2/-- if relevant] |
| [Field] | Allow/Deny | Allow/Deny | Allow/Deny | Allow/Deny |        |

FLS flags (entries that confirm or refute H2):
- [Field] / [Role]: [How this evidence relates to H2]

---

## EVIDENCE: RECORD ACCESS SCOPE
[For each role, name the scope in the hierarchy. Do not use "users see their own records"
without placing it in the scope hierarchy -- Own / Business Unit / Parent BU / Organization.]

| Role | Scope | H-link |
|------|-------|--------|
| [Role] | Own / BU / Parent BU / Org | [H1/H3/-- if scope is relevant to a hypothesis] |
| [Role] | Own / BU / Parent BU / Org |        |

Scope flags (scopes that are wider or narrower than H1/H3 predicted):
- [Role]: [What this scope confirms, refutes, or requires refinement of]

---

## FINDINGS: WHAT IS WRONG
[This section is required. Minimum one finding. Each finding must name a gap -- not
describe the model. Each finding must reference at least one evidence table and address
at least one hypothesis.]

Finding 1:
  Gap name: [Short name for this gap]
  Type: FLS / Escalation / Sharing Rule Conflict / Team Membership
  Evidence: [Which table row or cell reveals this -- e.g., "FLS table: AccountNumber /
             Customer Service role: Allow Read"]
  Hypothesis addressed: [H1 / H2 / H3 / new]
  H resolution: Confirmed / Refuted / Refined
  Details: [Concrete description -- e.g., "Customer Service role has Read-Allow on
            AccountNumber. This field contains billing account identifiers. The role
            should have Deny. Current configuration allows any CS agent to export
            billing data without supervisor approval."]

Finding 2:
  Gap name: [Short name]
  Type: FLS / Escalation / Sharing Rule Conflict / Team Membership
  Evidence: [Table reference]
  Hypothesis addressed: [H1 / H2 / H3 / new]
  H resolution: Confirmed / Refuted / Refined
  Details: [Concrete description]

[Add findings as warranted. If a hypothesis is refuted (no gap found in that area),
note the refutation and what was checked.]

---

## RISK RANKING
[Rank all findings H/M/L. One-line justification per finding. Ranking must be defensible
-- reference the operation type or data sensitivity, not just the gap category.]

| Finding | Risk | Justification |
|---------|------|---------------|
| [Finding 1 name] | H/M/L | [e.g., "Billing field readable by all CS agents -- direct PCI exposure"] |
| [Finding 2 name] | H/M/L | [One line] |

## REMEDIATION
[Concrete action per finding. "Tighten security" or "improve FLS" does not pass --
name the exact change: which field, which role, which configuration setting.]

| Finding | Action |
|---------|--------|
| [Finding 1] | [e.g., "Add FLS read-deny on AccountNumber for Customer Service role in Dataverse security role editor. Requires supervisor role to retain Allow."] |
| [Finding 2] | [Exact action] |

---

Write artifact: simulations/trace/permissions/{topic}-permissions-{date}.md
Frontmatter: skill, topic, date, roles_analyzed, operations_in_scope, platform,
hypotheses_confirmed, hypotheses_refuted, gaps_count, highest_risk.
```

---

## V-04: Role Sequence + Output Format (Customer Service Leads, Full Tables)

**Axes:** Role sequence (CS leads) + output format (all tables)
**Hypothesis:** CS leading grounds the analysis in practical record-visibility and team
scenarios that surface C-07 early, before the security expert adds technical depth for
C-05 and C-06. Table-only format prevents both perspectives from lapsing into model
description. The CS-first ordering also reflects the most common real-world scenario:
a support team escalates an access complaint to a security architect, not the reverse.

```
You are running /trace-permissions. CUSTOMER SERVICE leads: trace what agents can and
cannot do from an operational perspective. SECURITY EXPERT deepens with escalation path
analysis and sharing rule conflicts. All output is structured as tables -- minimize prose.

Stock roles:
- CUSTOMER SERVICE: CS team lead who operates the system daily, knows where agents get
  blocked, and spots when agents see data they should not see.
- SECURITY EXPERT: Dataverse security architect who audits privilege escalation vectors,
  FLS misconfigurations, and sharing rule conflicts.

CUSTOMER SERVICE analysis runs first. SECURITY EXPERT analysis follows. Findings from
both perspectives are merged into a single ranked gap summary.

---

## SETUP
Platform: [Dataverse / Salesforce / Custom RBAC / other]
Roles found: [Comma-separated list]
Operations in scope: [Comma-separated list -- include CRUD plus domain-specific ops]
Sensitive fields: [Comma-separated list]
Teams: [Comma-separated list]

---

## CUSTOMER SERVICE: WHAT CAN AGENTS DO?

### CS-1: Role-Operation Matrix (CS Perspective)
[CUSTOMER SERVICE fills this from operational knowledge. Focus on operations agents
perform. Mark: Y = can do, N = blocked, ? = inconsistent behavior observed.
Complete every cell. Do not leave blanks.]

| Operation | [Agent Role] | [Supervisor Role] | [Manager Role] | CS Flag |
|-----------|-------------|-------------------|----------------|---------|
| Create    |             |                   |                | [Flag if anomalous] |
| Read      |             |                   |                |         |
| Update    |             |                   |                |         |
| Delete    |             |                   |                |         |
| Escalate  |             |                   |                |         |
| Close     |             |                   |                |         |
| [Op]      |             |                   |                |         |

CS Observations (operations where access does not match operational intent):
- [e.g., "Agents marked Y for Delete on Case -- this should be supervisor-only"]
- [e.g., "Agents marked N for Read on Account history -- blocks resolution workflow"]

### CS-2: Team Membership Gaps
[CUSTOMER SERVICE identifies where team configuration creates access loss or
over-permission. Minimum one row. "None identified" requires explicit justification.]

| Scenario | Team(s) | Affected Users | Gap Type | Operational Impact |
|----------|---------|----------------|----------|--------------------|
| [Scenario] | [Team] | [Who -- role or user type] | Missing membership / Over-combined | [What breaks or what over-access enables] |

---

## SECURITY EXPERT: DEEP TECHNICAL AUDIT

### SE-3: Field-Level Security Audit
[SECURITY EXPERT names specific fields, specific roles, specific Allow/Deny.
"FLS should be configured" without naming fields and roles fails this section.
Complete every cell.]

| Field | [Role] Read | [Role] Write | [Role] Read | [Role] Write | FLS Gap? |
|-------|-------------|--------------|-------------|--------------|----------|
| [Field] |           |              |             |              | Y: [describe] / N |
| [Field] |           |              |             |              | Y: [describe] / N |

### SE-4: Record Access Scope
[SECURITY EXPERT confirms scope per role. Use the full hierarchy.
Do not conflate role privileges with record ownership.]

| Role | Scope | Correct? | Notes |
|------|-------|----------|-------|
| [Role] | Own / Business Unit / Parent BU / Organization | Y/N | [If N: expected scope and why] |
| [Role] | Own / Business Unit / Parent BU / Organization | Y/N |                               |

### SE-5: Privilege Escalation Paths
[Name the path. Do not assert escalation without naming the mechanism and the
unintended access gained. Check: record reassignment, team promotion, sharing rule
bypass, impersonation.]

| Path # | From Role | Mechanism | Unintended Access Gained |
|--------|-----------|-----------|--------------------------|
| 1 | [Role] | [Mechanism] | [Specific scope or operation gained unintentionally] |

[Add rows as found. If none: "None identified -- checked [list of vectors]. Justification."]

### SE-6: Sharing Rule Conflicts
[Sharing rules that widen access beyond the security role baseline in SE-4, or
that create contradictory access grants.]

| Rule | Role | Baseline Scope | Sharing Grants | Conflict Type |
|------|------|---------------|----------------|---------------|
| [Rule name] | [Role] | [Scope from SE-4] | [Access beyond baseline] | Widening / Contradiction |

[If none: "None identified -- sharing rules examined: [list]. No widening or contradiction found."]

---

## CONSOLIDATED GAP SUMMARY
[Merge CS and SE findings. At least one row required -- a trace with zero gaps fails.]

| # | Gap | Source | Type | Risk | Justification |
|---|-----|--------|------|------|---------------|
| 1 | [Gap name] | CS / SE | FLS / Escalation / Sharing / Team | H/M/L | [One line -- reference operation or data sensitivity] |
| 2 | [Gap name] | CS / SE | FLS / Escalation / Sharing / Team | H/M/L | [One line] |

## REMEDIATION
[Concrete action per gap. Map by gap number. "Tighten security" does not pass.]

| Gap # | Remediation Action |
|-------|--------------------|
| 1 | [Exact action -- name field, role, configuration location] |
| 2 | [Exact action] |

---

Write artifact: simulations/trace/permissions/{topic}-permissions-{date}.md
Frontmatter: skill, topic, date, roles_analyzed, operations_in_scope, platform,
cs_gaps_count, se_gaps_count, total_gaps, highest_risk.
```

---

## V-05: Full Synthesis (Gap-First + Customer Service Leads + Full Tables)

**Axes:** Gap-first framing (V-03) + CS-leads role sequence (V-04) + full table-matrix
output format (V-02)
**Hypothesis:** Maximum structural coverage of all criteria. The hypothesis mandate (V-03)
sets intent before analysis begins. CS-first ordering (V-04) grounds the trace in practical
operational gaps that reveal C-07 early and make C-04 concrete. Pre-printed table structures
(V-02) prevent any criterion from being omitted. The CONSOLIDATED FINDINGS table pre-prints
a "minimum one row" requirement. Hypothesis resolution links every finding back to the stated
H1/H2/H3, preventing generic gap descriptions. The synthesis of all three axes creates the
strongest structural guarantee across all 9 criteria.

```
You are running /trace-permissions. Your goal is to find what is wrong. The role-operation
matrix, FLS audit, and scope analysis are evidence-gathering tools -- not the deliverable.
A trace with no gaps identified fails.

Stock roles:
- CUSTOMER SERVICE: CS team lead who sees daily agent friction, record-visibility failures,
  and team membership oddities.
- SECURITY EXPERT: Dataverse security architect who audits privilege escalation paths, FLS
  misconfigurations, and sharing rule conflicts.

CUSTOMER SERVICE leads. SECURITY EXPERT deepens. All analysis is structured as tables.
Findings from both perspectives are consolidated and ranked.

---

## SETUP
Platform: [Dataverse / Salesforce / Custom RBAC / other]
Roles found: [Comma-separated list of all roles in scope]
Operations in scope: [Comma-separated -- CRUD plus domain-specific ops]
Sensitive fields: [Comma-separated -- fields that warrant FLS attention]
Teams: [Comma-separated list]

## GAP HYPOTHESIS
[Before any analysis. State what you expect to find wrong. Do not omit this section.
Each hypothesis is confirmed, refuted, or refined in CONSOLIDATED FINDINGS below.]

H1 (Escalation): [Where a user is likely able to gain access beyond their intended scope,
                  and the mechanism -- e.g., record reassignment, team promotion, sharing rule]
H2 (FLS): [Which sensitive fields are likely readable by roles that should be denied, and why]
H3 (Team): [Where team membership creates access loss or unintended over-permission, and why]

---

## CUSTOMER SERVICE: ROLE-OPERATION MATRIX
[CUSTOMER SERVICE fills this from operational knowledge. What can agents, supervisors,
and managers do? Flag anomalies -- operations where access does not match operational
intent. Complete every cell. Do not leave any cell blank.]

| Operation | [Agent Role] | [Supervisor Role] | [Manager Role] | CS Flag |
|-----------|-------------|-------------------|----------------|---------|
| Create    |             |                   |                |         |
| Read      |             |                   |                |         |
| Update    |             |                   |                |         |
| Delete    |             |                   |                |         |
| Escalate  |             |                   |                |         |
| [Op]      |             |                   |                |         |

[Y = permitted, N = denied, Y* = restricted (explain below). Complete every cell.]

Restrictions: [Explain any Y* entries -- what triggers the restriction]
CS Flags: [Operations where access is inconsistent with operational intent, with H-link
           if relevant to H1/H2/H3]

## CUSTOMER SERVICE: TEAM MEMBERSHIP GAPS
[CUSTOMER SERVICE identifies where team configuration creates access problems -- either
users missing access they need, or users with over-combined permissions from multiple teams.
Minimum one row. "None identified" requires explicit justification of what was checked.]

| Scenario | Team(s) | Affected Users | Gap Type | Operational Impact | H-link |
|----------|---------|----------------|----------|--------------------|--------|
| [Scenario] | [Team] | [Who] | Missing membership / Over-combined | [What breaks or leaks] | H3/new |

---

## SECURITY EXPERT: FIELD-LEVEL SECURITY AUDIT
[SECURITY EXPERT names specific fields, specific roles, specific Allow/Deny.
"FLS should be configured" without naming fields and roles fails this section.
Complete every cell. Mark H-link for fields relevant to H2.]

| Field | [Role] Read | [Role] Write | [Role] Read | [Role] Write | FLS Gap? | H-link |
|-------|-------------|--------------|-------------|--------------|----------|--------|
| [Field] |           |              |             |              | Y: [describe] / N | H2/-- |
| [Field] |           |              |             |              | Y: [describe] / N |       |

## SECURITY EXPERT: RECORD ACCESS SCOPE
[Scope per role. Own / Business Unit / Parent BU / Organization. Do not conflate role
privileges with record ownership. Mark H-link for scopes relevant to H1 or H3.]

| Role | Scope | Correct? | Notes | H-link |
|------|-------|----------|-------|--------|
| [Role] | Own / BU / Parent BU / Org | Y/N | [If N: expected scope and reason] | H1/H3/-- |
| [Role] | Own / BU / Parent BU / Org | Y/N |                                   |          |

## SECURITY EXPERT: PRIVILEGE ESCALATION PATHS
[Name the path. Do not assert escalation without naming the mechanism and the
unintended access gained. Check all vectors: record reassignment, team promotion,
sharing rule bypass, impersonation.]

| Path # | From Role | Mechanism | Unintended Access Gained | H-link |
|--------|-----------|-----------|--------------------------|--------|
| 1 | [Role] | [Mechanism] | [Specific scope or operation] | H1/new |

[Add rows as found. If no paths found: "None identified -- checked: [list of vectors].
H1: [Confirmed refuted / requires scope adjustment]."]

## SECURITY EXPERT: SHARING RULE CONFLICTS
[Sharing rules that widen access beyond the security role baseline, or that create
contradictory access grants across roles.]

| Rule | Role | Baseline Scope | Sharing Grants | Conflict Type |
|------|------|---------------|----------------|---------------|
| [Rule] | [Role] | [Scope from Scope table] | [Wider or contradictory access] | Widening / Contradiction |

[If none: "None identified -- sharing rules examined: [list]. No widening or contradiction."]

---

## CONSOLIDATED FINDINGS
[Merge CS and SE findings. This section must have at least one row -- a trace with no
findings fails. Each finding names a gap (not describes the model) and resolves a hypothesis.]

| # | Finding | Source | Type | H-link | H resolution | Risk | Justification |
|---|---------|--------|------|--------|--------------|------|---------------|
| 1 | [Finding name] | CS / SE | FLS / Escalation / Sharing / Team | H1/H2/H3/new | Confirmed / Refuted / Refined | H/M/L | [One line -- reference operation or data sensitivity] |
| 2 | [Finding name] | CS / SE | FLS / Escalation / Sharing / Team | H1/H2/H3/new | Confirmed / Refuted / Refined | H/M/L | [One line] |

Hypothesis resolution summary:
- H1 (Escalation): [Confirmed / Refuted / Refined -- cite finding # or explain what was checked]
- H2 (FLS): [Confirmed / Refuted / Refined]
- H3 (Team): [Confirmed / Refuted / Refined]

## REMEDIATION
[Concrete action per finding. Map by finding number. "Tighten security" does not pass --
name the exact change: which field, which role, which configuration setting, which team.]

| Finding # | Remediation Action |
|-----------|--------------------|
| 1 | [e.g., "Add FLS read-deny on AccountNumber for Customer Service role in Dataverse security role editor. Supervisor role retains Allow."] |
| 2 | [Exact action] |

---

Write artifact: simulations/trace/permissions/{topic}-permissions-{date}.md
Frontmatter: skill, topic, date, roles_analyzed, operations_in_scope, platform,
hypotheses_confirmed, hypotheses_refuted, cs_gaps, se_gaps, total_gaps, highest_risk.
```

---

## Round 1 Design Notes

### Variation axis selection

Three single-axis variations:
- V-01 tests **role sequence** (expert-first): does leading with the security architect's
  technical frame guarantee C-02, C-05, C-06 before CS adds C-07?
- V-02 tests **output format** (full tables): does pre-printing a TABLE 4: SECURITY GAPS
  with "minimum one row" force C-04 without requiring intent-setting?
- V-03 tests **gap-first framing**: does an explicit mandate + hypothesis section at the top
  of the prompt shift the model from "describe then notice" to "hypothesize then prove"?

Two combination variations:
- V-04 (axes 1+2): CS-first ordering + full tables. Tests whether CS leading + table structure
  is sufficient without hypothesis framing.
- V-05 (all three axes): Full synthesis. Maximum structural coverage across all 9 criteria.

### C-04 guarantee comparison

| V | C-04 mechanism | Structural strength |
|---|----------------|---------------------|
| V-01 | Expert section ends with explicit gap sections | Moderate (relies on model following section order) |
| V-02 | Pre-printed TABLE 4 with "minimum one row" instruction | Strong (blank cell is visible; table cannot be omitted) |
| V-03 | Hypothesis + FINDINGS section required before remediation | Moderate-strong (intent-set; FINDINGS required) |
| V-04 | CS observations + pre-printed gap summary table | Strong (CS flags anomalies early; table enforces at least one row) |
| V-05 | Hypothesis + CS flags + pre-printed gap table + H-resolution | Strongest (three independent forcing mechanisms) |

### C-09 (remediation specificity) approach

All five variations use "Tighten security does not pass -- name the exact change" language.
The example ("Add FLS read-deny on AccountNumber for Customer Service role") appears in all
five to calibrate the specificity threshold consistently across variations.

### C-08 (risk ranking) approach

V-01 and V-03 use inline risk columns in their gap summary tables. V-02 uses a separate
"Risk justification" block. V-04 and V-05 embed risk and justification in the consolidated
gap table. All five require a one-line justification per gap, which is the aspirational
pass condition for C-08.

### Open research question for R1

Does the hypothesis section (V-03/V-05) improve the *specificity* of gap descriptions
relative to pure table enforcement (V-02)? The hypothesis forces the model to commit to
a gap category before seeing evidence, which may produce more concrete C-04/C-05/C-06
findings. Or does the table structure alone (V-02) produce equivalent specificity with
less template overhead?

### V-golden candidate

**V-05** is the direct synthesis target for R1:
- H-link columns tie every finding to a stated hypothesis (C-04 structural intent)
- CS-first ordering surfaces team gaps before technical analysis (C-07 early)
- Pre-printed TABLE 4 equivalent (CONSOLIDATED FINDINGS with "minimum one row") (C-04)
- Explicit hypothesis resolution summary (prevents vague gap descriptions)
- Remediation table with specificity example (C-09)
- Risk + justification columns (C-08)

**V-02** is the closest structural competitor: pure table enforcement without hypothesis
overhead. Simpler template; same C-04 guarantee; may score equivalently on C-04 while
losing points on finding specificity (C-05/C-06) relative to V-05's hypothesis anchoring.
