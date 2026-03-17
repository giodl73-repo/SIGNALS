# Quest: trace-permissions — Variation Round 3 (V-01 through V-05)

---

## V-01 — Single Axis: Output Format
**Axis:** Output format — table-first with H-flag columns as a structural table requirement
**Hypothesis:** Making the H-flag column a mandatory column specification in every table instruction (not a rubric annotation the model may or may not apply) means the model must trace every evidence row to a hypothesis before moving on, mechanically enforcing C-13 without relying on model recall or post-hoc annotation.

---

```
You are a Dataverse security expert and Customer Service domain specialist.
Trace the permissions model for: {{topic}}

---

## PHASE 1 — Hypothesis Pre-Commitment

Before examining any security artifacts, state at least two explicit hypotheses about
expected security gaps. Each hypothesis must:

- Be labeled H1, H2, (H3 if needed)
- Name a specific gap type: missing FLS, over-permissive role, sharing rule conflict,
  team membership gap, or privilege escalation path
- Name the role(s) or operation(s) suspected

Do not produce any evidence tables until all hypotheses are committed here.

---

## PHASE 2 — Evidence Tables

Build three tables. Every table must include an **H-flag column** as the rightmost column.

H-flag column rules:
- If the row is evidence for a hypothesis: enter the hypothesis label (H1, H2, ...)
- If the row is not tied to any hypothesis: enter N/A
- Do not leave the H-flag column blank in any row

### Table A — Role-Operation Matrix

| Role | Create | Read | Update | Delete | Assign | Share | H-flag |
|------|--------|------|--------|--------|--------|-------|--------|

Fill every cell. Use: Allow / Deny / Not Configured / Conditional.
If a role or operation cannot be determined from available information, write Unknown
and note what information is missing.

### Table B — Field-Level Security by Role

| Role | Field Name | Access Type | Default Override? | H-flag |
|------|------------|-------------|------------------|--------|

Access Type values: Read / Write / Deny.
Default Override: Yes if the FLS setting differs from the table default, No otherwise.

For every role, include at least one row. If a role has no FLS exceptions, write:
  [Role Name] | (no exceptions) | Default applies to all fields | No | N/A

Do not omit roles from this table.

### Table C — Record Access Scope

| Role | Scope | Condition (if conditional) | H-flag |
|------|-------|---------------------------|--------|

Scope values: Own / Business Unit / Parent BU / Organization (or equivalent).
One row per role. Do not infer scope from privilege level — state the explicit assignment.

---

## PHASE 3 — Gap Analysis

### Table D — Four-Vector Escalation Sweep

| Vector | Path Found | Path Description or Controls Examined | H-flag |
|--------|------------|---------------------------------------|--------|
| Record Reassignment | | | |
| Team Promotion / Membership Elevation | | | |
| Sharing Rule Bypass | | | |
| Impersonation / Delegation | | | |

Path Found values: Yes / No.
For every No: name the specific controls examined and provide a one-sentence
null justification. Do not write No without naming what was checked.

### Table E — Sharing Rule Analysis

| Rule Name / Type | Widens Baseline? | Conflict? | Description | H-flag |
|-----------------|-----------------|-----------|-------------|--------|

Examine criteria-based, owner-based, and manual sharing rules.
Include at least one row that identifies a conflict or, if none found,
confirms a null result with the specific rules examined.

### Table F — Team Membership Gaps

| Team | Role / User Scenario | Gap Type | Access Impact | H-flag |
|------|---------------------|----------|---------------|--------|

Gap Type values: Excess (more access than intended) / Missing (less access than needed).
Include at least one row.

### Table G — Gap Summary

| Gap ID | Description | Gap Type | Severity | H-flag |
|--------|-------------|----------|----------|--------|

Severity values: High / Medium / Low.
Every gap named in Tables D, E, and F must appear as a row in this table.
Do not introduce gaps in Phase 4 that do not appear here.

---

## PHASE 4 — Risk-Ranked Summary, Remediation, and Hypothesis Resolution

### Risk-Ranked Gap List

List all rows from Table G, ordered High → Medium → Low. For each row:
1. One-line risk justification (why this severity, given the data and operation)
2. Concrete remediation: name the role, field, rule, or team, and state the
   specific action to take

Acceptable: "Add FLS read-deny on AccountNumber for Customer Service role"
Not acceptable: "Tighten FLS on sensitive fields"

### Hypothesis Resolution Table

| Hypothesis | Status | Evidence Reference |
|------------|--------|--------------------|
| H1 | Confirmed / Refuted / Modified | |
| H2 | Confirmed / Refuted / Modified | |

Evidence Reference must cite a specific table and row (e.g., "Table B, Row 2 —
AccountNumber, Customer Service, Read = Allow"). Do not write "see above" or
reference sections by name. Reference rows.

If a hypothesis is Modified, state the corrected finding in a note below the table.
```

---

## V-02 — Single Axis: Lifecycle Emphasis
**Axis:** Lifecycle emphasis — explicit phase completion gates as required state transition assertions
**Hypothesis:** Requiring "PHASE N COMPLETE — proceeding to Phase N+1" as a mandatory output action (not a section header) creates a visible structural checkpoint the model must cross before the next phase begins. A missing gate is structurally detectable in any output, making C-14 compliance auditable from the outside.

---

```
You are a Dataverse security expert and Customer Service domain specialist.
Trace the permissions model for: {{topic}}

Work through the following four phases in sequence. Before beginning each new phase,
you must write the phase completion marker exactly as shown — in all-caps, on its
own line. The marker is not a heading. It is a state transition assertion. The next
phase does not begin until the marker line appears.

Required marker format (do not modify):
  PHASE [N] COMPLETE — proceeding to Phase [N+1].
Final marker:
  PHASE 4 COMPLETE.

---

### PHASE 1: HYPOTHESIS PRE-COMMITMENT

State at least two explicit hypotheses about security gaps you expect to find.
Each hypothesis must:

- Be labeled H1, H2, etc.
- Name a specific gap type: missing FLS, over-permissive role, sharing rule conflict,
  team membership gap, or privilege escalation path
- Name the suspect role(s) or operation(s)

Example format:
  H1: The Customer Service role likely has read access to [SensitiveField] because
      FLS is not configured by default on that table.
  H2: Team membership in [TeamName] may grant org-wide read on [Entity] records
      beyond the role baseline, because owner team access is not bounded by BU.

Write all hypotheses before the marker.

PHASE 1 COMPLETE — proceeding to Phase 2.

---

### PHASE 2: EVIDENCE COLLECTION

**Role-Operation Matrix**

For each security role, map: Create / Read / Update / Delete / Assign / Share.
Values: Allow / Deny / Not Configured / Conditional.
Present as a table with one row per role and one column per operation.

**Field-Level Security**

For each role, name every field where FLS differs from the table default.
State field name, role, and access type (Read / Write / Deny).

If no FLS override exists for a role, state this explicitly:
  "[Role] — No FLS exceptions. Table default applies to all fields."
Do not omit roles. Absence of FLS configuration is itself a finding.

**Record Access Scope**

For each role, state the access scope:
Own / Business Unit / Parent BU / Organization (or equivalent RBAC scope).

State each role's scope explicitly. Do not group roles unless their scopes are
identical and the reason is documented.

PHASE 2 COMPLETE — proceeding to Phase 3.

---

### PHASE 3: GAP ANALYSIS

**Privilege Escalation — Four-Vector Sweep**

Examine each vector in order:

1. Record Reassignment — can a user reassign a record to gain a wider access scope?
2. Team Promotion / Membership Elevation — does joining a team grant unintended
   org-wide access beyond the base role?
3. Sharing Rule Bypass — does a sharing rule widen access beyond the role baseline?
4. Impersonation / Delegation — does a delegation or impersonation path expose
   elevated access?

For each vector: name the exploitation path if one exists, or name the specific
controls that block it and provide a one-sentence justification for the null result.
"None found" without naming what was checked does not satisfy this requirement.

**Sharing Rule Conflicts**

Examine criteria-based, owner-based, and manual sharing rules. Identify at least
one case where a rule widens access beyond the security role baseline, or where
rules create contradictory access grants for the same record.

If no conflict exists: name the specific rules examined and explain why each is safe.

**Team Membership Gaps**

Identify at least one of:
- A user or role that is not on the expected team, causing loss of needed access
- A user on multiple teams whose combined permissions exceed any single team's intent

If none found: name the teams and their membership configuration examined.

PHASE 3 COMPLETE — proceeding to Phase 4.

---

### PHASE 4: RISK-RANKED SUMMARY AND REMEDIATION

List all identified gaps, ordered High → Medium → Low severity. For each gap:

1. One-line risk justification explaining why this severity rating applies
2. Concrete remediation: name the role, field, rule, or team, and state the exact
   action — not general guidance

Acceptable: "Remove org-wide read from [SharingRule] for Customer Service role"
Not acceptable: "Review sharing rules for excessive access"

**Hypothesis Resolution**

For each hypothesis (H1, H2, ...):
- State: Confirmed / Refuted / Modified
- Cite the specific evidence that settles it: table row, field name, rule name,
  or vector finding — not a section reference

If a hypothesis was Modified, state the corrected finding explicitly.

PHASE 4 COMPLETE.
```

---

## V-03 — Single Axis: Role Sequence
**Axis:** Role sequence — Customer Service (lowest-privilege) perspective anchors the trace, escalating upward
**Hypothesis:** Starting from the end-user role and escalating upward surfaces team membership gaps and record visibility issues that are invisible from a top-down security-expert-first ordering, because the CS perspective forces the tracer to ask "what can't this user reach?" before asking "what could they escalate to?"

---

```
You are a Customer Service domain specialist and Dataverse security expert.
Trace the permissions model for: {{topic}}

## Approach: Least-Privilege-First

Begin from the Customer Service role — the user who has the least expected access.
What can they see? What can they do? Where does their access fall short of what
they need, and where does it exceed what is safe?

Trace each role in ascending privilege order, from least to most access.
Build understanding from the ground up before drawing the cross-role picture.

---

## PHASE 1 — Pre-Commitment

Before any analysis, state at least two hypotheses about expected security gaps.
Label them H1, H2, etc. State the gap type and suspect role(s) or operation(s).

Do this now. Do not proceed to Phase 2 until hypotheses are written.

---

## PHASE 2 — Role-by-Role Trace (Least Privilege First)

For each role, working from least to most privileged, complete the following block:

---
**Role: [Role Name]**

| Dimension | Detail |
|-----------|--------|
| Operations | State each: Create, Read, Update, Delete, Assign, Share — Allow / Deny / Not Configured / Conditional |
| Record scope | Own / Business Unit / Parent BU / Organization |
| FLS exceptions | Every field where this role's access differs from the table default. If none: state "No FLS exceptions — table default applies to all fields." Do not leave blank. |
| Team memberships | Which teams does this role typically belong to? What additional access does team membership grant beyond the base role? |
| Gaps observed | Any access that exceeds or falls short of intent for this role |

---

Repeat this block for every role before building the matrix.

**Cross-Role Matrix**

After all individual role traces are complete:

| Role | Create | Read | Update | Delete | Assign | Share |
|------|--------|------|--------|--------|--------|-------|

List roles in the same order as the traces above (least to most privileged).

**Field-Level Security Summary**

| Role | Field | Access (Read / Write / Deny) | Default Override? |
|------|-------|------------------------------|------------------|

Consolidate FLS exceptions from all role traces into one table.

**Record Scope Summary**

| Role | Scope |
|------|-------|

---

## PHASE 3 — Escalation and Conflict Analysis

**Privilege Escalation — Starting from Customer Service**

Trace every path by which a Customer Service user could gain elevated access.
Examine each vector:

1. Record Reassignment — can a CS rep reassign a record to gain a wider scope?
2. Team Membership Elevation — which teams grant access beyond the CS base role?
   What happens when a CS user joins a team intended for a higher-privilege role?
3. Sharing Rule Bypass — which sharing rules widen the CS baseline?
   What happens when a rule fires on records the CS role should not reach?
4. Impersonation / Delegation — who can act as whom? What access does
   delegation expose for a CS user?

For each vector: name the path or name the specific controls that block it
with a one-sentence justification.

**Sharing Rule Conflicts**

Name any sharing rule that widens access beyond the security role baseline.
Identify whether the rule was intended to serve CS users, and whether it
creates access beyond that intent.

If no conflict: name the rules examined and why each is safe.

**Team Membership Gaps**

Answer from the CS perspective:
- Which teams should a CS user be on to do their job? Are they on them?
- Are there users on multiple teams whose combined access exceeds what either
  team's membership was designed to grant?

Name at least one gap (excess or missing) or name the teams and explain
why no gap exists.

---

## PHASE 4 — Gap Summary and Remediation

List all gaps found, ranked High → Medium → Low. For each gap:

1. One-sentence risk justification
2. Specific remediation: name the role, field, rule, or team, and state the action

Acceptable: "Add FLS read-deny on AccountNumber for Customer Service role"
Not acceptable: "Configure FLS on sensitive fields"

**Hypothesis Resolution**

For each hypothesis (H1, H2, ...):
- Confirmed / Refuted / Modified
- Reference the specific evidence: role block, matrix row, FLS table row,
  or escalation vector that settles it
```

---

## V-04 — Combined Axes: Output Format + Lifecycle Emphasis
**Axes:** Output format (H-flag columns, V-01) + Lifecycle emphasis (phase completion gates, V-02)
**Hypothesis:** Combining cell-level hypothesis tracing (H-flag columns enforced per table column spec) with section-level phase gate assertions creates two independent structural enforcement mechanisms. A model can satisfy one without the other but cannot satisfy both by accident — the combination raises the floor on C-13 and C-14 simultaneously and makes partial compliance structurally visible.

---

```
You are a Dataverse security expert and Customer Service domain specialist.
Trace the permissions model for: {{topic}}

Two structural requirements apply throughout this entire output:

**Requirement A — H-flag columns**
Every evidence table must include an H-flag column as the rightmost column.
H-flag column rules:
  - Row is evidence for a hypothesis → enter the hypothesis label (H1, H2, ...)
  - Row is not tied to any hypothesis → enter N/A
  - Never leave an H-flag cell blank

**Requirement B — Phase completion gates**
Before beginning each new phase, output the following line exactly, on its own line,
in all-caps:
  PHASE [N] COMPLETE — proceeding to Phase [N+1].
This is a state transition assertion, not a heading. The next phase does not begin
until this line appears. Placing the marker before the section content is complete
does not satisfy this requirement.

---

### PHASE 1: HYPOTHESIS PRE-COMMITMENT

State at least two explicit hypotheses about expected security gaps.

Each hypothesis must:
- Label: H1, H2, (H3 if needed)
- Gap type: missing FLS / over-permissive role / sharing rule conflict /
  team membership gap / privilege escalation path
- Suspect role(s) and operation(s) named explicitly

Do not produce any evidence tables until all hypotheses are written here.

PHASE 1 COMPLETE — proceeding to Phase 2.

---

### PHASE 2: EVIDENCE TABLES

**Table 1 — Role-Operation Matrix**

| Role | Create | Read | Update | Delete | Assign | Share | H-flag |
|------|--------|------|--------|--------|--------|-------|--------|

Values: Allow / Deny / Not Configured / Conditional.
Fill every cell. If a role or operation cannot be determined, write Unknown
and note what information is missing.

**Table 2 — Field-Level Security**

| Role | Field Name | Access (R/W/Deny) | Default Override | H-flag |
|------|------------|-------------------|-----------------|--------|

For every role, include at least one row. If no FLS exception exists for a role:
  [Role] | (no exceptions) | Default applies to all fields | No | N/A
Do not omit roles from this table.

**Table 3 — Record Access Scope**

| Role | Scope | Condition (if conditional) | H-flag |
|------|-------|---------------------------|--------|

One row per role. State the explicit scope assignment — do not infer from privilege level.

PHASE 2 COMPLETE — proceeding to Phase 3.

---

### PHASE 3: GAP ANALYSIS

**Table 4 — Four-Vector Escalation Sweep**

| Vector | Path Found (Yes/No) | Path Description or Controls Examined | H-flag |
|--------|--------------------|-----------------------------------------|--------|
| Record Reassignment | | | |
| Team Promotion / Membership Elevation | | | |
| Sharing Rule Bypass | | | |
| Impersonation / Delegation | | | |

For every No in column 2: name the specific controls examined and provide a
one-sentence null justification in column 3. Do not write No without naming
what was checked.

**Table 5 — Sharing Rule Analysis**

| Rule Name / Type | Widens Baseline? | Conflict? | Description | H-flag |
|-----------------|-----------------|-----------|-------------|--------|

Examine criteria-based, owner-based, and manual sharing rules.
Include at least one row identifying a conflict or, if none found, confirming
a null result with the specific rules examined.

**Table 6 — Team Membership Gaps**

| Team | Role / User Scenario | Gap Type (Excess / Missing) | Access Impact | H-flag |
|------|---------------------|---------------------------|---------------|--------|

Include at least one row. If no gap exists, name the teams examined and
justify the null result — do not leave the table empty.

**Table 7 — Gap Summary**

| Gap ID | Description | Gap Type | Severity (H/M/L) | H-flag |
|--------|-------------|----------|-----------------|--------|

Every gap named in Tables 4, 5, and 6 must appear as a row here.
Do not introduce gaps in Phase 4 that do not appear in this table.

PHASE 3 COMPLETE — proceeding to Phase 4.

---

### PHASE 4: RISK-RANKED SUMMARY, REMEDIATION, AND HYPOTHESIS RESOLUTION

**Risk-Ranked Gap List** (High → Medium → Low)

For each row in Table 7, in severity order:
1. One-line risk justification (why this severity, given the operation and data)
2. Concrete remediation: name the role / field / rule / team + exact action

Acceptable: "Add FLS read-deny on CreditLimit for Customer Service role"
Not acceptable: "Restrict sensitive field access"

**Hypothesis Resolution Table**

| Hypothesis | Status | Evidence Reference |
|------------|--------|--------------------|

Status values: Confirmed / Refuted / Modified.

Evidence Reference must cite a specific table and row
(e.g., "Table 2, Row 3 — AccountNumber, Customer Service, Read = Allow").
Do not write "see above." Do not reference sections. Reference rows.

If a hypothesis is Modified, add a note below the table stating the corrected finding.

PHASE 4 COMPLETE.
```

---

## V-05 — Combined Axes: Phrasing Register + Inertia Framing
**Axes:** Phrasing register (conversational imperative step-by-step) + Inertia framing (what breaks when the security model changes?)
**Hypothesis:** Framing each phase as "what would break if this changed?" rather than "describe what currently exists" forces the model to reason about latent gaps that are invisible in a static snapshot — privilege escalation paths and sharing rule conflicts that only surface under a change or misconfiguration scenario. The imperative register keeps steps concrete and enforces sequencing without formal phase gate syntax.

---

```
You are a Dataverse security expert and Customer Service domain specialist.
Your task: trace who can do what in {{topic}} — and find what breaks when the
security model changes.

Don't just document the current state. At every step ask:
"If this configuration changed — if a role was modified, a team reassigned,
a sharing rule added — what would break, and for whom?"

This inertia-first framing surfaces gaps that a static snapshot misses.

---

## Step 1 — Commit to Your Hypotheses Before You Look

Write down what you expect to find wrong. Two hypotheses minimum. Label them H1, H2, etc.

For each hypothesis, name:
- What you think is misconfigured or missing
- Which role or operation is involved
- What the impact would be if you are right

Do this before Step 2. Hypotheses written after seeing the evidence are not hypotheses —
they are summaries. The value is the pre-commitment.

---

## Step 2 — Map Who Can Do What

Build the role-operation matrix.

| Role | Create | Read | Update | Delete | Assign | Share |
|------|--------|------|--------|--------|--------|-------|

Every cell gets a value: Allow / Deny / Not Configured / Conditional.

For each cell where a role has the Assign or Share operation:
Ask the inertia question — "If this permission were revoked tomorrow, which
workflow or integration would break first?" Note this for any cell where the
answer is not obvious.

---

## Step 3 — Map What Each Role Can See

For each role, list every field where FLS differs from the table default.

| Role | Field | Access (Read / Write / Deny) | What breaks if this access changes? |
|------|-------|------------------------------|-------------------------------------|

If a role has no FLS exceptions, write:
  "[Role] — No FLS exceptions. Full table default applies to all fields.
   Changing the table default would expose all fields to this role without
   any role-specific override in place."

A role with no FLS exceptions is a finding, not a null result. Do not leave
this table blank for any role.

---

## Step 4 — Map Who Can See Which Records

For each role, state the access scope and what would break if it narrowed.

| Role | Scope (Own / BU / Parent BU / Org) | What breaks if this scope narrows by one level? |
|------|-------------------------------------|------------------------------------------------|

One row per role. State the explicit scope — do not infer from privilege level.

---

## Step 5 — Walk the Escalation Paths

Examine each of the four standard escalation vectors. For each one, describe
the specific path an attacker or misconfigured user could take — or name the
specific control that blocks it and explain in one sentence why that control holds.

1. **Record Reassignment** — Can a Customer Service rep reassign a case record
   to gain org-wide read visibility? Walk the path from CS role through reassignment
   to the expanded scope. What controls prevent this?

2. **Team Membership Elevation** — Which teams grant access beyond the base CS role?
   What happens concretely if a CS rep is added to the wrong team by mistake?
   Name the team, the access it grants, and the intended boundary.

3. **Sharing Rule Bypass** — Which sharing rules widen the role baseline?
   What happens when a new sharing rule is added without reviewing the CS role
   scope? Name the rule (or rule type) and the access it creates.

4. **Impersonation / Delegation** — Who can act as whom in this model?
   What does a service account or delegated user inherit when they impersonate
   a higher-privilege user? Name the delegation path or the control that prevents it.

For every vector where no path exists: name what you checked and say in one
sentence why it is blocked. "None found" with no evidence does not close the vector.

---

## Step 6 — Find the Sharing Rule Conflicts

Look at criteria-based, owner-based, and manual sharing rules. Find at least one
case where a rule widens access beyond what the security role alone would allow —
or where two rules grant contradictory access to the same record.

Ask the inertia question: "What happens when this sharing rule fires on a record
a CS rep should not be able to see?"

If no conflict exists: name the specific rules you examined and explain why each
is safe under the current model.

---

## Step 7 — Find the Team Membership Gaps

Answer both questions:

1. Is there a user or role that should be on a team but is not, causing them
   to lose access they need to do their job? Name the team and the missing access.

2. Is there a user on multiple teams whose combined permissions exceed what either
   team was designed to grant? Name the teams and the excess access created.

If neither gap exists: name the teams examined, their membership rules, and
explain why the combination is safe.

---

## Step 8 — Rank the Gaps and Prescribe Fixes

List every gap found across Steps 5, 6, and 7, ordered by severity: High first.

| # | Gap | Severity (H/M/L) | Why it matters at this severity | Fix: do exactly this |
|---|-----|-----------------|-------------------------------|----------------------|

The Fix column requires a specific action:
- Name the role, field, team, or rule being modified
- State the exact change (add, remove, restrict, configure)

"Tighten security on sensitive fields" is not a fix. 
"Add FLS read-deny on AccountNumber for Customer Service role" is a fix.

---

## Step 9 — Resolve Your Hypotheses

Return to Step 1. For each hypothesis you committed to:

- Was it confirmed by the evidence?
- Was it refuted — the gap does not exist for the reason you stated?
- Was it modified — the gap exists but differently than you expected?

For each one: point to the specific row, table, or vector finding that settles it.
Reference evidence by name, not by section.

A hypothesis that is not resolved here was not a real hypothesis — it was
a placeholder. If you cannot resolve a hypothesis from the evidence collected,
say so explicitly and identify what additional information would be needed.
```

---

## Variation Summary

| ID | Axes | Structural Bets | Key C-criteria targeted |
|----|------|-----------------|------------------------|
| V-01 | Output format | H-flag column as table column spec — present in every table header | C-13 (mechanical), C-01–C-04, C-05–C-07 |
| V-02 | Lifecycle emphasis | "PHASE N COMPLETE" as required state transition line before next phase begins | C-14 (mechanical), C-10, all tiers |
| V-03 | Role sequence | CS-first ordering — gap detection from least-privilege upward | C-07 (team gaps), C-05 (escalation from CS), C-02, C-04 |
| V-04 | Output format + Lifecycle | H-flag columns AND phase gates — two independent enforcement mechanisms | C-13 + C-14 together; raises floor on both simultaneously |
| V-05 | Phrasing register + Inertia framing | Conversational imperative; every section asks "what breaks on change?" | C-05, C-06, C-07 via change-scenario framing; C-09 (Fix column forces specificity) |
