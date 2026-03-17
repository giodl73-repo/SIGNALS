# trace-permissions Variate — Round 3
**Date:** 2026-03-15
**Rubric:** v3 (C-01 through C-15)
**Target criteria:** All v2 criteria plus C-13 (remediation includes expected post-fix state and verification step), C-14 (gaps register includes discovery-section reference), C-15 (escalation rule-out is per-role, not blanket)

---

## Round 3 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Lifecycle emphasis — remediation-verification template as a pre-declared structural contract | Printing a three-field remediation template (change / expected-state / verification) before the trace begins primes the model to collect verification evidence during analysis, making C-13 a generative fill-in rather than a retroactive afterthought |
| V-02 | Output format — discovery-section column as first-class register field | Adding a mandatory "Discovered In" column to the register — with an explicit fill instruction at every section — makes C-14 structurally unavoidable and simultaneously forces C-11 compliance, because you cannot reference a discovery section without having registered the gap at that section |
| V-03 | Role sequence — per-role escalation subsections replacing a single escalation sweep | Decomposing the escalation phase into one named subsection per traced role forces the model to produce one positive-or-negative entry per role, making the blanket "no escalation paths found" syntactically impossible and satisfying C-15 |
| V-04 | Combined: discovery-section register (V-02 axis) + per-role escalation subsections (V-03 axis) | The register's discovery column provides the C-14 audit trail; the per-role escalation structure prevents the C-15 blanket rule-out; together they close both new behavioral criteria without requiring a third axis |
| V-05 | Combined: remediation-verification template (V-01 axis) + discovery register (V-02 axis) + per-role escalation (V-03 axis) | All three new v3 criteria are addressed structurally: C-13 via the pre-declared template, C-14 via the discovery column, C-15 via per-role subsections; layering all three axes should achieve the highest composite score across all fifteen criteria |

---

## V-01 — Lifecycle Emphasis: Remediation-Verification Template as Pre-Declared Contract

**Axis:** Lifecycle emphasis — the remediation phase uses a three-field template that is declared before the trace begins
**Hypothesis:** When the model is shown the remediation template (config-change / expected-state / verification-step) before it starts tracing, it collects verification-relevant detail during analysis rather than trying to reconstruct it afterward. This makes C-13 a slot-filling exercise rather than a retrospective add-on, and it prevents C-08 failures (vague remediation) at the same time.

---

You are running a permissions trace signal for: {{topic}}

---

**REMEDIATION TEMPLATE — every gap fix must use this format:**

```
Gap ID: [ID]
Config change: [exact configuration element to modify and where]
Expected state after fix: [what the system will show when the change is applied — name the UI location or query result]
Verification step: [how to confirm the fix took effect — e.g., "Open the FLS profile for [entity] in the solution editor; field X shows Read-only for Customer Service role"]
```

Vague entries ("review permissions," "improve security," "consult your admin") do not satisfy this template. Every field must be filled.

---

**GAPS REGISTER — do not fill this now. Return here after Phase 3.**

| ID | Gap Type | Entity | Field (if FLS) | Role | Severity | Config Change | Expected State After Fix | Verification Step |
|----|----------|--------|----------------|------|----------|---------------|--------------------------|-------------------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY.
Severity: CRITICAL / HIGH / MEDIUM.

---

## PHASE 1 — PERMISSION MAP

You are a Dataverse security architect. Build the map before any gap analysis.

**1a — Entity and OWD inventory:**

List every entity that {{topic}} creates, reads, updates, or deletes. For each entity, state the org-wide default (Private / Business Unit / Parent-Child Business Unit / Organization) and what that default grants to a user with no explicit role.

**1b — Operation-role matrix:**

For each entity, build:

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Use: YES / NO / CONDITIONAL (state condition). Record Scope: Org / BU / Team / User / Sharing-[rule name]. Every role with any privilege must appear.

**1c — Sensitive field categorization (mandatory before Phase 2):**

For each entity, group fields into these categories before checking any FLS profiles:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII (name, email, phone, address, ID numbers) | |
| | Financial (revenue, billing, payment, credit) | |
| | Audit/Compliance (created-by, modified-by, consent flags, audit trail) | |
| | Operational (status, queue, assignment, SLA, notes) | |

Write "none" for any category with no fields on that entity — do not leave rows blank.

After completing the category table, check FLS for every PII, Financial, and Audit/Compliance field:

| Entity | Field | Category | FLS Profile? | Roles: Read | Roles: Write |
|--------|-------|----------|-------------|-------------|--------------|

For every field where FLS Profile? = NO: this is a gap. Note it here. You will register it in the GAPS REGISTER in Phase 3 with a full remediation entry using the template above.

---

## PHASE 2 — SECURITY GAP ANALYSIS

Still as the Dataverse security architect. Use the Phase 1 map for each check. For every check: find the gap or explicitly rule it out.

**2a — Privilege escalation (per-role):**

For each role in the Phase 1b matrix, examine whether it holds Write on: team membership, security role assignment, record ownership (Assign), or business unit configuration.

For each role — whether or not a path exists — write one of:

- Finding: `[Role] → [action available] → [elevated access achieved]`
- Rule-out: "Checked [specific privilege list] for [Role]: no escalation path because [reason]."

One entry per role. Do not consolidate roles into a single statement.

**2b — Sharing rule audit:**

List every active sharing rule for the entities in scope. For each rule: name it, state the trigger, state the access it opens beyond the OWD, and state whether it conflicts with the security role model.

If no sharing rules exist: "Checked sharing rules for [entity list]: no active sharing rules found."

**2c — Team membership gap:**

For each team-scoped role: who controls team membership? Can any role add a user (or themselves) to a team that grants access above their base role? State the mechanism or rule-out explicitly.

**2d — Cross-entity permission chain:**

Pick the entity with the highest data sensitivity (use Phase 1c categories to justify). Trace access through at least two entity hops:

`[Role] → [Entity A, op: X, scope: Y] → [Relationship type] → [Entity B, op: X, scope: Y]`

State whether each hop is intentional or an emergent side-effect of the relationship.

---

## PHASE 3 — ROLE DIFFERENTIATION AND REMEDIATION

**Customer Service Representative:**
State CRUD + Assign + Record Scope per entity. State which Phase 1c sensitive fields the CS role can read or write and whether that access is appropriate.

**Dataverse Security Expert:**
State CRUD + Assign + Record Scope per entity. Note every privilege the expert holds that CS does not. Does the expert role follow least-privilege?

**Contrast statement (required):**
One paragraph explicitly naming both roles — what CS can do that the expert cannot, and what the expert can do that CS cannot. Both role names must appear.

**Remediation — fill the GAPS REGISTER now:**

For every gap identified in Phases 1–2, return to the GAPS REGISTER above and add a complete row using the remediation template. Every row must have all three remediation fields filled (Config Change, Expected State After Fix, Verification Step).

---

## OUTPUT REQUIREMENTS

- Phase 1c (category table + FLS check) must appear before Phase 2.
- Phase 2a (escalation) must produce one entry per traced role — not one consolidated statement.
- Every GAPS REGISTER row must have all remediation template fields filled.
- Both CS Representative and Dataverse Security Expert must appear by name in Phase 3 with role-specific access stated.

---

## V-02 — Output Format: Discovery-Section Column as First-Class Register Field

**Axis:** Output format — the GAPS register has a required "Discovered In" column that must be filled at each section point
**Hypothesis:** A register with a mandatory discovery-section column, combined with a per-section log-update instruction, forces C-14 compliance structurally. The discovery-section reference also provides the audit trail that proves C-11 (inline registration) actually occurred — a gap with a "Discovered In" field that matches the section in which it appears is provably inline; one discovered at the end cannot reference an earlier section without fabricating the reference.

---

You are running a permissions trace signal for: {{topic}}

---

## LIVE GAPS REGISTER

This register is updated throughout the trace. Every time a gap is identified, add a row immediately — before the next section begins. Do not defer.

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity | Remediation |
|----|--------------|----------|--------|----------------|------|----------|-------------|

- **Discovered In**: the section header where this gap was found (e.g., "Section 2 FLS check" or "Section 4 escalation — Customer Service role"). This column is mandatory. A gap row with no "Discovered In" entry is incomplete.
- Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY
- Severity: CRITICAL / HIGH / MEDIUM
- Remediation: name the exact configuration change. "Review permissions" does not qualify.

**Log update rule:** At the end of every section below, before moving to the next section header, check whether the work in that section produced any new gaps. If yes: add the row to this register with the current section name in "Discovered In" before continuing. If no: write a one-line confirmation: "Section [N] log check: no new gaps found — [brief reason]."

---

## SECTION 1 — ENTITY AND OWD INVENTORY

You are a Dataverse security architect.

List every entity {{topic}} creates, reads, updates, or deletes. For each: state the org-wide default (Private / BU / Parent-Child BU / Organization).

**Section 1 log check:** Does the OWD for any entity create unexpected default access? If yes, add to LIVE GAPS REGISTER now.

---

## SECTION 2 — OPERATION-ROLE MATRIX

For each entity, build:

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Team / User / Sharing-[rule name]. Every role with any privilege must appear.

**Section 2 log check:** Does any role hold a Record Scope broader than its function requires? Add any finding to LIVE GAPS REGISTER now (Discovered In: "Section 2 operation-role matrix").

---

## SECTION 3 — SENSITIVE FIELD CATEGORIZATION AND FLS

Before checking FLS profiles, enumerate sensitive fields by category:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII | |
| | Financial | |
| | Audit/Compliance | |
| | Operational | |

After completing the category inventory, check FLS for every PII, Financial, and Audit/Compliance field:

| Entity | Field | Category | FLS Profile? | Roles: Read | Roles: Write |
|--------|-------|----------|-------------|-------------|--------------|

**Section 3 log check:** For every sensitive field where FLS Profile? = NO: add a MISSING-FLS row to the LIVE GAPS REGISTER now (Discovered In: "Section 3 FLS check — [field name]"). If no FLS gaps: "Section 3 log check: no MISSING-FLS entries — confirmed by reviewing [field list] and finding profiles on all PII/Financial/Audit-Compliance fields."

---

## SECTION 4 — PRIVILEGE ESCALATION

For each role in the Section 2 matrix, examine whether it holds Write on: team membership, security role assignment, record ownership (Assign), or BU configuration.

For each role:
- Finding: `[Role] → [action] → [elevated access]`
- Rule-out: "Checked [privilege list] for [Role]: no escalation path because [reason]."

One entry per role. Do not merge roles into a single statement.

**Section 4 log check:** Add any escalation path to LIVE GAPS REGISTER now (Discovered In: "Section 4 escalation — [role name]"). If all roles ruled out: confirm each role separately, then write "Section 4 log check: no ESCALATION-PATH entries — [per-role evidence summary]."

---

## SECTION 5 — SHARING RULE AUDIT

List every active sharing rule for the entities in scope. For each rule: name it, state the trigger, state the access opened, and state whether it conflicts with the OWD or security role model.

**Section 5 log check:** Add any SHARING-CONFLICT to LIVE GAPS REGISTER now (Discovered In: "Section 5 sharing rule — [rule name]"). If no rules or no conflicts: "Section 5 log check: no SHARING-CONFLICT entries — [rules checked]."

---

## SECTION 6 — TEAM MEMBERSHIP GAP

For each team-scoped role: identify who controls team membership. Can any role reach elevated access through team membership? State mechanism or explicit rule-out.

**Section 6 log check:** Add any TEAM-GAP to LIVE GAPS REGISTER now (Discovered In: "Section 6 team gap — [team name]"). If no gap: "Section 6 log check: no TEAM-GAP entries — [reason]."

---

## SECTION 7 — CROSS-ENTITY PERMISSION CHAIN

Pick the entity with the highest data sensitivity (use Section 3 categories to justify). Trace at least two entity hops:

`[Role] → [Entity A, op: X, scope: Y] → [Relationship] → [Entity B, op: X, scope: Y]`

State whether each hop is intentional or emergent.

**Section 7 log check:** Add any CROSS-ENTITY finding to LIVE GAPS REGISTER now (Discovered In: "Section 7 cross-entity chain — [role name]").

---

## SECTION 8 — ROLE DIFFERENTIATION

**Customer Service Representative:**
State CRUD + Assign + Record Scope per entity. State which Section 3 sensitive fields the CS role can access and whether that is appropriate.

**Dataverse Security Expert:**
State CRUD + Assign + Record Scope per entity. Note every privilege the expert holds that CS does not.

**Contrast statement (required):** One paragraph explicitly naming both roles.

---

## SECTION 9 — REMEDIATION

For every entry in the LIVE GAPS REGISTER:

`[Gap ID]: [exact configuration change] in [location in solution]. Expected state after fix: [what changes]. Verification step: [how to confirm the fix took effect].`

Vague advice ("improve security," "review permissions") fails. Name the specific change, the expected outcome, and how to verify.

---

## V-03 — Role Sequence: Per-Role Escalation Subsections

**Axis:** Role sequence — the escalation phase is decomposed into one named subsection per traced role, run in sequence
**Hypothesis:** When the escalation check is structured as "Role A — escalation check" / "Role B — escalation check" / ... rather than a single "escalation scan" section, the model must produce an explicit entry for each role. The blanket "no escalation paths found" becomes syntactically impossible because each subsection is labeled with a role name and demands a role-specific response. This satisfies C-15 without a reminder, while the per-role structure also makes C-05 (positive escalation trace) more likely to appear because each role is examined individually.

---

You are running a permissions trace signal for: {{topic}}

---

**GAPS TABLE — do not fill this now. Return here after Phase 3.**

| ID | Gap Type | Entity | Field (if FLS) | Role | Severity | Remediation |
|----|----------|--------|----------------|------|----------|-------------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY.
Severity: CRITICAL / HIGH / MEDIUM.
Remediation: name the exact configuration change plus the expected state after fix and how to verify it.

---

## PHASE 1 — PERMISSION MAP

You are a Dataverse security architect.

**1a — Entity and OWD inventory:**

List every entity {{topic}} touches. For each: state the org-wide default (Private / BU / Parent-Child BU / Organization) and what it grants by default.

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Team / User / Sharing-[rule name]. All roles with any privilege on any entity must appear.

**1c — Sensitive field categorization:**

For each entity, enumerate fields by category before checking FLS:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII | |
| | Financial | |
| | Audit/Compliance | |
| | Operational | |

Write "none" for empty categories.

Then check FLS for every PII, Financial, and Audit/Compliance field:

| Entity | Field | Category | FLS Profile? | Roles: Read | Roles: Write |
|--------|-------|----------|-------------|-------------|--------------|

For every FLS Profile? = NO on a sensitive field: note it. You will add it to the GAPS TABLE in Phase 3.

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflict? |
|-----------|---------|---------------|-------------|-----------|

---

## PHASE 2 — PER-ROLE ESCALATION ANALYSIS

You are reviewing the Phase 1 matrix for privilege escalation. The analysis runs one subsection per role.

For each role: examine whether it holds Write on any of — team membership, security role assignment, record ownership (Assign), or business unit configuration.

**Template for a finding:**
```
Role: [name]
Escalation-capable privilege: [what it can modify]
Path: [Role] → [action] → [elevated access achieved]
```

**Template for a rule-out:**
```
Role: [name]
Privileges checked: [team membership / security role assignment / record ownership / BU configuration — state each]
Result: no escalation path
Reason: [specific reason — e.g., Assign privilege is user-scoped and cannot reassign to a higher-scope owner; no Write on team membership]
```

Run this for every role in the Phase 1b matrix. One subsection per role. Do not merge roles. Do not write a single collective statement.

After completing all per-role subsections: add any escalation paths found to the GAPS TABLE. If all roles ruled out, confirm the per-role evidence is in the subsections above — the GAPS TABLE will have no ESCALATION-PATH rows, and that is valid.

---

## PHASE 3 — ADDITIONAL GAP CHECKS

**3a — FLS gap registration:**
Add a MISSING-FLS row to the GAPS TABLE for every sensitive field found without an FLS profile in Phase 1c.

**3b — Sharing rule conflicts:**
From Phase 1d: for each rule marked Conflict = YES, add a SHARING-CONFLICT row to the GAPS TABLE. If no conflicts: "No sharing rule conflicts — [rules checked]."

**3c — Team membership gap:**
For each team-scoped role in Phase 1b: can any role add themselves (or a user they control) to a team that grants elevated access? State mechanism or rule-out explicitly. Add any TEAM-GAP to the GAPS TABLE.

**3d — Cross-entity permission chain:**
Pick the entity with the highest data sensitivity (use Phase 1c to justify). Trace at least two entity hops:

`[Role] → [Entity A, op: X, scope: Y] → [Relationship type] → [Entity B, op: X, scope: Y]`

Add any emergent (unintended) cross-entity access as CROSS-ENTITY in the GAPS TABLE.

---

## PHASE 4 — ROLE DIFFERENTIATION AND REMEDIATION

**Customer Service Representative:**
CRUD + Assign + Record Scope per entity. Which Phase 1c sensitive fields can the CS role access, and is that appropriate?

**Dataverse Security Expert:**
CRUD + Assign + Record Scope per entity. Every privilege the expert holds that CS does not. Does the expert role follow least-privilege?

**Contrast statement (required):** One paragraph explicitly naming both roles with what each can and cannot do.

**Remediation — fill the GAPS TABLE now:**

For every row in the GAPS TABLE:

`[Gap ID]: [exact config change] in [location in solution]. Expected state after fix: [what the system shows when the change is applied]. Verification step: [how to confirm — name the UI location or test action].`

"Review permissions" does not qualify. Every row needs all three remediation components.

---

## V-04 — Combined: Discovery-Section Register + Per-Role Escalation Subsections

**Axis:** Output format (discovery-section column in register) + Role sequence (per-role escalation subsections)
**Hypothesis:** The discovery-section column provides the C-14 audit trail; the per-role escalation structure prevents the C-15 blanket rule-out. Together they close both new behavioral criteria. The combination is additive rather than redundant: the register column makes C-11 auditable regardless of which phase produced the gap, while the per-role escalation structure specifically prevents the C-15 failure mode in the escalation phase.

---

You are running a permissions trace signal for: {{topic}}

---

## LIVE GAPS LOG

Updated throughout the trace. Add a row at point of discovery. Do not defer to the end.

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity | Fix |
|----|--------------|----------|--------|----------------|------|----------|-----|

- **Discovered In**: section name and check point (e.g., "Phase 1c FLS check — Case.CreditLimit" or "Phase 3 escalation — Queue Manager role"). Required. A row without "Discovered In" is incomplete.
- Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY
- Severity: CRITICAL / HIGH / MEDIUM
- Fix: exact configuration change. "Review permissions" does not qualify.

---

## PHASE 1 — PERMISSION MAP

You are a Dataverse security architect.

**1a — Entities and OWDs:**

List every entity {{topic}} touches. For each: org-wide default (Private / BU / Parent-Child BU / Organization).

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Team / User / Sharing-[rule name].

**Log check after 1b:** Does any role hold Record Scope broader than its function requires? If yes, add to LIVE GAPS LOG (Discovered In: "Phase 1b operation-role matrix — [role name]").

**1c — Sensitive field categorization (complete before Phase 2):**

| Entity | Category | Fields |
|--------|----------|--------|
| | PII | |
| | Financial | |
| | Audit/Compliance | |
| | Operational | |

"none" for empty categories.

FLS check for all PII, Financial, and Audit/Compliance fields:

| Entity | Field | Category | FLS Profile? | Roles: Read | Roles: Write |
|--------|-------|----------|-------------|-------------|--------------|

**Log check after 1c:** For every FLS Profile? = NO on a sensitive field: add a MISSING-FLS row to LIVE GAPS LOG now (Discovered In: "Phase 1c FLS check — [entity].[field]"). If no FLS gaps: "Phase 1c log check: no MISSING-FLS entries — profiles confirmed for [field list]."

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflict? |
|-----------|---------|---------------|-------------|-----------|

**Log check after 1d:** For each Conflict = YES: add a SHARING-CONFLICT row to LIVE GAPS LOG (Discovered In: "Phase 1d sharing rule — [rule name]").

---

## PHASE 2 — TEAM MEMBERSHIP AND CROSS-ENTITY CHECKS

**2a — Team membership gap:**

For each team-scoped role: identify who controls team membership and whether that control can be used to reach elevated access. State mechanism or rule-out.

**Log check after 2a:** Add any TEAM-GAP to LIVE GAPS LOG (Discovered In: "Phase 2a team membership — [team name]").

**2b — Cross-entity permission chain:**

Pick the entity with the highest data sensitivity (use Phase 1c to justify). Trace at least two hops:

`[Role] → [Entity A, op: X, scope: Y] → [Relationship] → [Entity B, op: X, scope: Y]`

State whether each hop is intentional or emergent.

**Log check after 2b:** Add any emergent cross-entity access as CROSS-ENTITY to LIVE GAPS LOG (Discovered In: "Phase 2b cross-entity chain — [role name]").

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

The escalation check runs one subsection per role. Do not consolidate roles.

For each role in the Phase 1b matrix:

**Role: [name]**

Privileges checked for escalation capability:
- [ ] Write on team membership
- [ ] Write on security role assignment
- [ ] Write on record ownership (Assign privilege — scope and target)
- [ ] Write on business unit configuration

Result: ESCALATION-PATH FOUND / RULED OUT

If ESCALATION-PATH FOUND:
`[Role] → [action taken] → [elevated access achieved]`

If RULED OUT:
State which specific privileges were examined and why none permit elevation.

**Log check after each role subsection:** If ESCALATION-PATH FOUND: add a row to LIVE GAPS LOG now (Discovered In: "Phase 3 escalation — [role name]").

---

## PHASE 4 — ROLE DIFFERENTIATION AND REMEDIATION

**Customer Service Representative:**
CRUD + Assign + Record Scope per entity. Which Phase 1c sensitive fields can CS access? Appropriate?

**Dataverse Security Expert:**
CRUD + Assign + Record Scope per entity. Every privilege the expert holds that CS does not. Least-privilege?

**Contrast statement (required):** One paragraph naming both roles explicitly.

**Remediation:**

For every entry in the LIVE GAPS LOG:

`[Gap ID] (Discovered In: [section]): [exact config change] in [location]. Expected state after fix: [what changes]. Verification step: [how to confirm].`

Name the specific change, the expected outcome, and the verification method.

---

## V-05 — Combined: Remediation-Verification Template + Discovery Register + Per-Role Escalation

**Axis:** Lifecycle emphasis (remediation template pre-declared) + Output format (discovery-section column) + Role sequence (per-role escalation subsections)
**Hypothesis:** All three new v3 criteria are addressed structurally rather than through reminders. C-13 (verification step in remediation) is forced by a template declared before analysis begins — the model fills slots rather than deciding whether to include verification. C-14 (discovery-section reference) is forced by a register column that must be filled at each section. C-15 (per-role escalation rule-out) is forced by the per-role subsection structure. Together with the v1/v2 criteria already addressed in earlier rounds, this combination should achieve the highest composite score across all 15 criteria.

---

You are running a permissions trace signal for: {{topic}}

---

## REMEDIATION CONTRACT

Every gap identified in this trace must be remediated using the following three-field format. Declare this now, before analysis begins, so that evidence for all three fields can be gathered during the trace rather than reconstructed at the end.

```
Gap [ID]:
  Config change:        [the exact configuration element to modify, and where in the system]
  Expected state:       [what the system will show after the change — name the specific UI view, profile, or query result]
  Verification step:    [how to confirm the fix took effect — a named action a reviewer can execute]
```

A remediation row that omits Expected State or Verification Step is incomplete regardless of how specific the Config Change is.

---

## LIVE GAPS REGISTER

Updated at point of discovery — not deferred. Every row requires a Discovered In entry.

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

Remediation is handled separately in Phase 5 using the contract above. Discovered In format: "[Phase N] [section name] — [specific context]" (e.g., "Phase 1 FLS check — Contact.AnnualRevenue" or "Phase 3 escalation — Customer Service role").

**Register rule:** Before advancing past any section header, check whether that section produced a gap. If yes: add the row immediately. If no: write a one-line negative confirmation with the evidence. Gap rows without Discovered In are invalid.

---

## PHASE 1 — ENTITY AND ROLE MAP

You are a Dataverse security architect.

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Default access for a user with no explicit role |
|--------|-----------------|------------------------------------------------|

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Team / User / Sharing-[rule name]. All roles with any privilege must appear.

**Register check after 1b:** Any role with Record Scope broader than its function? Add to register (Discovered In: "Phase 1b operation-role matrix — [role]"). If none: "Phase 1b check: no scope anomalies — [brief basis]."

**1c — Sensitive field categorization (gate — complete before Phase 2):**

Step 1: category inventory per entity:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII (name, contact, ID, government data) | |
| | Financial (billing, pricing, payment, credit) | |
| | Audit/Compliance (modified-by, consent, audit trail) | |
| | Operational (status, queue, SLA, internal notes) | |

"none" for empty categories. Do not leave rows blank.

Step 2: FLS check for every PII, Financial, and Audit/Compliance field:

| Entity | Field | Category | FLS Profile? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|-------------|-------------|--------------|------|

**Register check after 1c:** For each Gap? = YES: add to LIVE GAPS REGISTER now (Discovered In: "Phase 1 FLS check — [entity].[field]"). If no gaps: "Phase 1c check: no MISSING-FLS entries — FLS profiles confirmed for all PII/Financial/Audit-Compliance fields; profiles examined: [list]."

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

**Register check after 1d:** For each Conflicts = YES: add to LIVE GAPS REGISTER (Discovered In: "Phase 1d sharing rule — [rule name]"). If none: "Phase 1d check: no SHARING-CONFLICT entries — [rules checked, reason no conflict]."

---

## PHASE 2 — TEAM MEMBERSHIP AND CROSS-ENTITY

**2a — Team membership gap:**

For each team-scoped role: identify who controls membership and whether a role can use that control to reach elevated access.

Finding: `[Role] → [adds user to Team X] → [elevated access via team] — mechanism: [how]`
Rule-out: "Checked team membership control for [team list]: no injection path — [reason]."

**Register check after 2a:** Add any TEAM-GAP (Discovered In: "Phase 2a team membership — [team]"). If none: confirm per team.

**2b — Cross-entity permission chain:**

Pick the entity with the highest data sensitivity (use Phase 1c category inventory to justify).

Trace at least two entity hops:

`[Role] → [Entity A, op: X, scope: Y] → [Relationship type: lookup/child/N:N] → [Entity B, op: X, scope: Y]`

At each hop: state whether access is INTENTIONAL (expected by design) or EMERGENT (side effect of relationship). Mark EMERGENT hops as gaps.

**Register check after 2b:** Add any CROSS-ENTITY findings (Discovered In: "Phase 2b cross-entity — [role] via [entity A] → [entity B]").

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

One subsection per role from the Phase 1b matrix. Do not merge. Do not write a collective statement.

For each role:

**Role: [name]**

Escalation-capable privileges examined:
- Team membership Write: [YES / NO — evidence]
- Security role assignment Write: [YES / NO — evidence]
- Record ownership (Assign scope): [state scope and whether reassignment can elevate]
- Business unit configuration Write: [YES / NO — evidence]

Conclusion: ESCALATION-PATH FOUND / RULED OUT

If FOUND: `[Role] → [action] → [elevated access achieved]`
If RULED OUT: "No path — [specific reason each checked privilege does not permit elevation]."

**Register check after each role:** If ESCALATION-PATH FOUND: add to LIVE GAPS REGISTER (Discovered In: "Phase 3 escalation — [role name]"). If ruled out: the absence in the register confirms the negative.

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative:**
CRUD + Assign + Record Scope per entity. Which Phase 1c sensitive fields can CS read or write? For each: is access appropriate to the CS job function, or is it overreach?

**Dataverse Security Expert:**
CRUD + Assign + Record Scope per entity. Every privilege the expert holds that CS does not. Does the expert role follow least-privilege, or hold admin-level access beyond the configuration task?

**Contrast statement (required):**
One paragraph explicitly contrasting the two roles: what CS can do that the expert cannot, and what the expert can do that CS cannot. Both role names must appear.

---

## PHASE 5 — REMEDIATION

For every entry in the LIVE GAPS REGISTER, apply the Remediation Contract declared at the top of this trace:

```
Gap [ID] (Discovered In: [section]):
  Config change:        [exact element — role name / field name / profile name / rule name, and where to find it in the solution]
  Expected state:       [what you will see after applying the change — specify the UI view or test query]
  Verification step:    [the action to confirm the fix — e.g., "Open Security > Field Security Profiles > [profile name] > [entity] > [field]: verify Role [name] shows Read-only"]
```

Every gap gets all three fields. A gap with Expected State missing fails C-13. A gap with no Verification Step fails C-13. "Consult your admin" or "review this configuration" fails C-08 and C-13 together.
