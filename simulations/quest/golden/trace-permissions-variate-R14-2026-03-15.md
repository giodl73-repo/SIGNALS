# trace-permissions Variate -- Round 2 (Rubric v2)
**Date:** 2026-03-15
**Rubric:** v2 (C-01 through C-14)
**Round note:** First round targeting the four new aspirational criteria (C-11 through C-14). Round 1 best performer (R1-V-01) scored 93 -- C-11/C-12 partial, C-13 satisfied via scope token syntax, C-14 absent. This round pushes the remaining aspirational ceiling.
**Target criteria focus:** C-11 (pre-committed gap register), C-12 (escalation rule-out evidence), C-13 (scope token vocabulary), C-14 (question-form negative anchoring) -- while preserving all essential (C-01 through C-05) and recommended (C-06 through C-08) coverage.

---

## Round 2 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Lifecycle emphasis -- gap register category schema declared as the first output, before entity enumeration | True pre-commitment requires the model to commit to gap categories before it knows which entities exist; declaring the schema first (not just the empty table) prevents selective retroactive population |
| V-02 | Output format -- locked scope token lexicon section before any table; inline failure markers for non-token scope prose | Declaring the scope token set as a named lexicon and treating any prose scope cell as an inline error eliminates superficial C-03 compliance while simultaneously satisfying C-13 at every table cell |
| V-03 | Phrasing register -- all critical security gates in question form with required explicit yes/no answer + evidence | Question-form gates cannot be silently passed; a question demands a response, which forces the model to write an explicit verdict where a declarative assertion would allow omission |
| V-04 | Combined: C-12 (evidence-cited rule-out format) + C-14 (question-form gates) | Pairing question form with mandatory evidence citation closes the dual failure mode: questions prevent omission (C-14); evidence format prevents verdicts without inspection records (C-12) |
| V-05 | Combined: all four aspirational criteria as structural constraints -- pre-committed register (C-11), scope lexicon (C-13), question gates (C-14), evidence rule-outs (C-12) | All four aspirational criteria are discipline enforcers, not content additions; wiring them together as structural rules preserves the essential/recommended structure from R1-V-01 while targeting the full 10-point aspirational tier |

---

## V-01 -- Lifecycle Emphasis: Category-First Gap Register Pre-Commitment

**Axis:** Lifecycle emphasis -- gap register category schema is the first output element, declared before entity enumeration
**Hypothesis:** C-11 requires the register to appear "at the top of the trace with categories named." The R1 round satisfied this partially by placing an empty register header before Stage 1. This variation goes further: the model declares the gap category vocabulary as a typed schema before it has enumerated any entity -- making selective omission structurally impossible because the categories are locked before evidence collection begins.

---

You are running a permissions trace signal for: {{topic}}

---

## STEP 0 -- GAP CATEGORY COMMITMENT (complete this before reading any further)

Before enumerating entities, operations, or fields: commit to the gap categories you will look for. These categories are now locked. You may not introduce a new gap type after this step.

**Declare your gap register now:**

| # | Gap Category | Definition | Example |
|---|-------------|------------|---------|
| FLS-EXPOSURE | Sensitive field accessible without a field security profile | PII field readable by any role with entity Read | Social Security Number on Contact with no FLS profile |
| ESCALATION-PATH | A role can reach a higher privilege level through a reachable action | CS role can reassign record ownership, gaining Write on target entity | Team membership Write grants elevation to admin team |
| SHARING-CONFLICT | A sharing rule opens access the OWD + security role model intends to restrict | Sharing rule re-opens Org-level access after OWD = Private | Rule grants Write to all users, overriding BU restriction |
| TEAM-GAP | An operation requires team membership but team assignment is uncontrolled or absent | Queue access requires team but any user can self-add | No process governs who joins the Tier-2 team |
| OWD-MISMATCH | Org-wide default is broader than the data sensitivity warrants | Org-level OWD on a high-sensitivity entity with no compensating FLS | Financial entity at Organization OWD with no FLS profiles |
| CROSS-CASCADE | A relationship behavior grants unintended access across entities | Parental cascade gives a role entity-level access through a child record | Delete on child entity propagates to parent via Parental behavior |

Add rows for any additional gap categories you discover. Do not remove rows.

**Gap Findings Table -- do not populate this now. Return here after Stage 3.**

| # | Gap Category | Entity | Field (if FLS) | Role | Severity | Exact Fix |
|---|-------------|--------|----------------|------|----------|-----------|

Severity: CRITICAL / HIGH / MEDIUM. Exact Fix: name the specific configuration object and the resulting state after change.

---

## STAGE 1 -- INVENTORY

You are a Dataverse security architect. The gap categories above are fixed. Now build the permission foundation.

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) | Gap Category Risk |
|--------|-----------------|-----------------------------------|-------------------|

For each entity: state the OWD and which gap categories are plausible given the entity's sensitivity. This is your per-entity hunting checklist.

**1b -- Operation-role matrix (one table per entity):**

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|--------|------|-------|--------|--------|--------------|

Allowed values: YES / NO / CONDITIONAL (state condition). Record Scope: Org / BU / Parent-Child BU / Team:[name] / User / Sharing:[rule name]. Every role with any privilege must appear, including read-only.

**1c -- Field-level security matrix (mandatory before Stage 2):**

| Entity | Field | Sensitivity Category | FLS Profile Name | Roles: Read | Roles: Write |
|--------|-------|----------------------|-----------------|-------------|--------------|

Sensitivity categories: PII / Financial / Health / Credential / Internal-Audit.

- If FLS Profile Name = NONE for a sensitive field: add an FLS-EXPOSURE row to the Gap Findings Table now. Do not defer.
- If an entity has zero sensitive fields: write "Confirmed: [Entity] has no fields with sensitivity >= Medium. Fields checked: [list]."
- A blanket "no FLS configured" without naming the fields checked does not pass.

---

## STAGE 2 -- GAP ANALYSIS

For each gap category declared in Step 0: investigate and document findings or explicit rule-outs.

**2a -- ESCALATION-PATH:**
For each role with Write on team membership, security role assignment, record ownership, or BU configuration:
- Finding: `[Role] -> [Action available] -> [Elevated access gained]`
- Rule-out: "Checked [Role] for: team-membership-write / role-assign-write / ownership-reassign / BU-config-write. None present -- [specific structural reason per category checked]."

A role not explicitly checked is not ruled out.

**2b -- SHARING-CONFLICT:**
List every active sharing rule:

| Rule Name | Trigger | Access Opened | Wider than OWD + Security Role? | Conflict? |
|-----------|---------|---------------|--------------------------------|-----------|

For rules with Conflict? = YES: add SHARING-CONFLICT row to Gap Findings Table now.
If no sharing rules exist: "Checked sharing rules for [entity list] in solution: no active rules found."

**2c -- TEAM-GAP:**
For each team-scoped role: who controls membership? Can a lower-privilege role add itself or another user? Name the control mechanism or rule it out with the specific constraint that prevents self-addition.

**2d -- OWD-MISMATCH:**
For each entity with sensitivity = High: is the OWD more permissive than the sensitivity warrants? State whether FLS compensates for an open OWD.

**2e -- CROSS-CASCADE:**
Identify the highest-sensitivity entity. Trace at least two relationship hops:
`[Role] -> [Entity A, access, scope] -> [Relationship type + cascade: Parental / Referential / None] -> [Entity B, access, scope] -> [cascade] -> [Entity C, access, scope]`
At each hop: state whether access is intentional or emergent.

---

## STAGE 3 -- ROLE ASSESSMENT AND LEAST-PRIVILEGE

**3a -- Customer Service Representative and Dataverse Security Expert:**

For each role: state CRUD + Assign per entity with Record Scope. Both roles must appear by name with distinct access observations -- a merged summary fails.

**3b -- Least-privilege scoring:**

| Role | Persona | Privileges Beyond Persona Need | LP Score (0-10) | Over-Privileged? |
|------|---------|-------------------------------|-----------------|------------------|

LP Score: 10 = exact least-privilege. Score < 7: state the specific privilege to reduce and the target scope.

**3c -- Attack scenario (if any escalation path found in 2a):**
Step-by-step: `Starting role -> Action sequence -> Gained access`. Abstract risk statements do not satisfy this section.

Now return to the Gap Findings Table in Step 0 and populate it completely. Every Exact Fix must name the specific configuration object -- no general advice.

---

## V-02 -- Output Format: Locked Scope Token Lexicon

**Axis:** Output format -- a named, locked scope token lexicon appears before any table; non-token scope prose is an inline failure
**Hypothesis:** C-13 requires every scope cell to use a token from a predefined enumerated set. Stating the lexicon once in passing (as R1-V-01 did inside the Record Scope column definition) allows models to satisfy it accidentally or ignore it after the first table. Declaring the lexicon as a named, locked section -- and treating any prose scope entry as an explicit inline failure -- enforces C-13 structurally across every table rather than at first encounter.

---

You are running a permissions trace signal for: {{topic}}

---

## RECORD ACCESS LEXICON (locked -- read before building any table)

Every Record Scope cell in every table in this trace must use exactly one token from this set:

| Token | Meaning |
|-------|---------|
| `Org` | User can access all records in the organization regardless of owner or BU |
| `BU` | User can access records owned by users in the same business unit |
| `Parent-Child BU` | User can access records owned by users in the same BU and all child BUs |
| `Team:[name]` | User can access records owned by or shared to a named team; replace [name] with the actual team name |
| `User` | User can access only their own records |
| `Sharing:[rule name]` | User reaches records via a named sharing rule; replace [rule name] with the actual rule name |

**Inline failure rule:** If any Record Scope cell contains prose ("appropriate records," "relevant records," "permitted scope," or any non-token phrase), mark that cell **SCOPE-FAIL** and correct it before advancing to the next section. A table with uncorrected SCOPE-FAILs does not satisfy this trace.

---

**GAP REGISTER -- do not fill this now. Return here after Stage 3.**

| # | Gap Type | Entity | Field (if FLS) | Role | Severity | Exact Fix |
|---|----------|--------|----------------|------|----------|-----------|

Gap types: FLS-EXPOSURE / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-CASCADE
Severity: CRITICAL / HIGH / MEDIUM

---

## STAGE 1 -- INVENTORY

You are a Dataverse security architect. All Record Scope cells must use tokens from the RECORD ACCESS LEXICON above.

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) |
|--------|-----------------|-----------------------------------|

**1b -- Operation-role matrix (one table per entity):**

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|--------|------|-------|--------|--------|--------------|

All Record Scope cells: lexicon tokens only. If you write a non-token phrase, mark it SCOPE-FAIL and correct it immediately.

**1c -- Field-level security matrix (mandatory):**

| Entity | Field | Sensitivity Category | FLS Profile Name | Roles: Read | Roles: Write |
|--------|-------|----------------------|-----------------|-------------|--------------|

Sensitivity categories: PII / Financial / Health / Credential / Internal-Audit.
- Sensitive field with no FLS profile: add FLS-EXPOSURE to the Gap Register now.
- Entity with zero sensitive fields: "Confirmed: [Entity] contains no fields with sensitivity >= Medium. Fields reviewed: [list]."

**Lexicon check after Stage 1:** Scan every Record Scope cell in 1b. Replace any SCOPE-FAILs now. Do not advance to Stage 2 with uncorrected cells.

---

## STAGE 2 -- GAP ANALYSIS

**2a -- Privilege escalation:**
For each role with Write on team membership, security role assignment, record ownership, or BU configuration: trace the path.
- Finding: `[Role] -> [Action] -> [Elevated access]`
- Rule-out: "Checked [Role]: team-membership-write / role-assign-write / ownership-reassign / BU-config-write. No escalation because [specific structural reason per category]."

**2b -- Sharing rule audit:**

| Rule Name | Trigger | Access Opened | Record Scope of Opened Access | Intended? | Overreach? |
|-----------|---------|---------------|------------------------------|-----------|------------|

Record Scope of Opened Access: lexicon tokens only. If no sharing rules exist: "Checked sharing rules for [entity list]: no active rules found."
Overreach = YES: add SHARING-CONFLICT to Gap Register now.

**2c -- Team membership gap:**
For each team-scoped role: state who controls membership and whether self-addition is possible. Name the specific control or rule it out with the mechanism that prevents it.

**2d -- Cross-entity cascade:**
Pick the highest-sensitivity entity. Trace at least two relationship hops:
`[Role] -> [Entity A, operation, Record Scope: <lexicon token>] -> [Relationship type + cascade] -> [Entity B, operation, Record Scope: <lexicon token>]`
At each hop: lexicon token required in scope; state intentional vs emergent access.

---

## STAGE 3 -- ROLE ASSESSMENT

**3a -- Customer Service Representative (named):**
Per entity: CRUD + Assign + Record Scope (lexicon token). Per sensitive field from 1c: can this role read or write it?

**3b -- Dataverse Security Expert (named):**
Per entity: CRUD + Assign + Record Scope (lexicon token). State every privilege the expert holds that CS does not.

**3c -- Contrast statement (required):**
One paragraph explicitly contrasting the two roles. Both names must appear. Both must have specific distinct observations -- a merged summary fails.

**3d -- Least-privilege scoring:**

| Role | Persona | Excess Privileges | LP Score (0-10) | Over-Privileged? |
|------|---------|-------------------|-----------------|------------------|

Score < 7: state the specific privilege to reduce and the target scope.

**Final lexicon check:** Scan every Record Scope cell across all stages. Correct any remaining SCOPE-FAILs.

Now return to the GAP REGISTER and fill it in completely. Every Exact Fix must name the specific configuration object and expected post-fix state.

---

## V-03 -- Phrasing Register: Question-Form Negative Anchoring at All Critical Gates

**Axis:** Phrasing register -- all critical security gates use question form with required explicit answers
**Hypothesis:** C-14 requires at least two critical gates in question form with explicit answers. This variation applies question form to every critical gate across the trace -- not just two. A question cannot be silently passed: "Does this role have team-membership-write access?" forces a yes/no response. The declarative equivalent ("No escalation paths found.") can appear without any examination. Question form closes the silent-pass path at every gate where a verdict can otherwise be omitted.

---

You are running a permissions trace signal for: {{topic}}

---

**GAP REGISTER -- do not fill this now. Return here after Stage 3.**

| # | Gap Type | Entity | Field (if FLS) | Role | Severity | Exact Fix |
|---|----------|--------|----------------|------|----------|-----------|

Gap types: FLS-EXPOSURE / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-CASCADE
Severity: CRITICAL / HIGH / MEDIUM

---

## STAGE 1 -- INVENTORY

You are a Dataverse security architect. Build the permission foundation for {{topic}}.

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) |
|--------|-----------------|-----------------------------------|

**1b -- Operation-role matrix (one table per entity):**

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|--------|------|-------|--------|--------|--------------|

Allowed values: YES / NO / CONDITIONAL (state condition). Record Scope: Org / BU / Parent-Child BU / Team:[name] / User / Sharing:[rule name]. Include every role with any privilege.

**1c -- FIELD-LEVEL SECURITY GATE (answer required before advancing):**

For each entity in 1a, answer these questions:

**Q: Does [Entity] contain fields with sensitivity >= Medium (PII, Financial, Health, Credential, Internal-Audit)?**
A: [Yes / No -- if No, list three fields confirmed as non-sensitive]

**If Yes -- Q: Is a field security profile applied to each sensitive field on [Entity]?**

| Entity | Field | Sensitivity | Q: FLS Profile Applied? | Profile Name | Roles: Read | Roles: Write |
|--------|-------|-------------|------------------------|--------------|-------------|--------------|

For every field where FLS Profile Applied? = No: add FLS-EXPOSURE to the Gap Register now.

**Q: Have I confirmed FLS coverage (or confirmed absence of sensitive fields) for every entity in 1a?**
A: [Yes / No -- if No, return and complete the table]

Do not advance to Stage 2 until this answer is Yes.

---

## STAGE 2 -- GAP ANALYSIS

For each gap vector: answer the gate question before proceeding to the next.

**ESCALATION GATE**

**Q: Does any role in the 1b matrix hold Write on team membership, security role assignment, record ownership, or BU configuration?**
A: [Yes / No]

If Yes -- **Q: What elevated access does that Write capability enable?**
For each such role: `[Role] -> [Write action available] -> [Elevated access gained]`
Add ESCALATION-PATH to Gap Register.

If No -- **Q: What did I check to confirm no role holds these privileges?**
A: For each role: "Checked [Role] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- none present because [specific structural reason]."
A blanket "no escalation" across all roles without per-role examination does not answer this question.

---

**SHARING RULE GATE**

**Q: Are there active sharing rules for the entities in scope?**
A: [Yes / No -- if No, state "Checked sharing rules for [entity list]: no active rules found"]

If Yes -- **Q: Does any sharing rule grant access wider than the OWD + security role combination intends?**

| Rule Name | Trigger | Access Opened | Record Scope | Intended? | Overreach? |
|-----------|---------|---------------|--------------|-----------|------------|

For rules with Overreach? = Yes: add SHARING-CONFLICT to Gap Register.

**Q: Have I examined every active sharing rule and stated whether it overreaches?**
A: [Yes / No -- if No, return and complete the table]

---

**TEAM MEMBERSHIP GATE**

**Q: Does any role in the model have access scoped to a team?**
A: [Yes / No]

If Yes -- **Q: Who controls team membership, and can a lower-privilege role add itself or another user to this team?**
A: "Team [name] membership is controlled by [role/mechanism]. Self-addition is [possible / not possible] because [specific constraint]."
Add TEAM-GAP to Gap Register if self-addition is possible or membership control is undefined.

---

**CROSS-ENTITY GATE**

**Q: Which entity in scope has the highest sensitivity, and what is the lowest-privilege role that can reach it?**
A: "Highest-sensitivity entity: [name]. Lowest-privilege path: [trace through at least two relationship hops]."
`[Role] -> [Entity A, operation, scope] -> [Relationship type + cascade] -> [Entity B, operation, scope]`
At each hop: state whether access is intentional or emergent from cascade behavior.

---

## STAGE 3 -- ROLE ASSESSMENT

**Q: Can the Customer Service Representative stock role access sensitive fields on any entity without a field security profile?**
A: State each sensitive field the CS role can access. For each: is an FLS profile preventing inappropriate read/write, or is the field open?

**Q: Does the Dataverse Security Expert role hold privileges beyond what the security configuration task requires?**
A: State each privilege the expert holds beyond CS. For each: is it least-privilege for a security expert persona, or over-permissioned?

**Least-privilege scoring:**

| Role | Persona | Excess Privileges | LP Score (0-10) | Q: Over-Privileged? | Recommended Reduction |
|------|---------|-------------------|-----------------|---------------------|-----------------------|

**Q: Do both named roles appear with distinct specific access observations?**
A: [Yes / No -- if No, expand the above before continuing]

**Q: Does every gap in the Gap Register have a specific Exact Fix that names the configuration object?**
A: [Yes / No -- if No, add Exact Fix entries now. "Tighten permissions" does not satisfy this question.]

Now return to the GAP REGISTER and fill it in completely.

---

## V-04 -- Combined: Evidence-Cited Questions (C-12 + C-14)

**Axis:** Evidence-cited question form -- every critical security gate is a question whose answer must follow the template "Q: [gate]? A: [verdict] -- Evidence: I checked [X]; result is [Y] because [Z]."
**Hypothesis:** C-12 and C-14 target the same failure mode from two directions: C-14 prevents omission through silence (a question forces a response); C-12 prevents verdicts without inspection records (an evidence citation forces the model to name what was examined). Combining them into a single answer format means every verdict is both present and evidenced. A model cannot write "no escalation" -- it must write "no escalation -- Evidence: I checked team-membership-write, role-assign-write, ownership-reassign for each role; none present because [structural reason per role]."

---

You are running a permissions trace signal for: {{topic}}

---

**GAP REGISTER -- do not fill this now. Return here after Stage 3.**

| # | Gap Type | Entity | Field (if FLS) | Role | Severity | Exact Fix |
|---|----------|--------|----------------|------|----------|-----------|

Gap types: FLS-EXPOSURE / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-CASCADE

---

## EVIDENCE-CITATION FORMAT

Every answer to a gate question must follow this format:

> **Q:** [gate question]
> **A:** [verdict: Yes / No / Conditional]
> **Evidence:** I checked [named objects / privilege categories / entities examined] -- [result] because [specific structural reason].

A verdict without an Evidence line does not satisfy the gate. "No escalation" with no evidence line fails. "No escalation -- Evidence: I checked all roles" with no named privilege categories fails. Both the named objects and the structural reason are required.

---

## STAGE 1 -- INVENTORY

You are a Dataverse security architect. Build the permission foundation.

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) |
|--------|-----------------|-----------------------------------|

**1b -- Operation-role matrix (one table per entity):**

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Parent-Child BU / Team:[name] / User / Sharing:[rule name]. Include every role with any privilege.

**1c -- Field-level security (answer the gate question):**

> **Q:** Does every sensitive field on every entity in scope have a field security profile?
> **A:** [answer per entity]
> **Evidence:** I checked Security > Field Security Profiles for [entity list] -- [result per entity] because [profile name exists / profile absent / entity has no sensitive fields and fields reviewed are: list].

For every sensitive field with no FLS profile: add FLS-EXPOSURE to the Gap Register now with Severity = CRITICAL.

Build the FLS table for each entity:

| Entity | Field | Sensitivity | FLS Profile Name | Roles: Read | Roles: Write |
|--------|-------|-------------|-----------------|-------------|--------------|

---

## STAGE 2 -- GAP ANALYSIS

Apply the Evidence-Citation Format to every gate.

**Escalation gate:**

> **Q:** Can any role in the model reach a higher privilege level through team membership, security role assignment, record ownership reassignment, or BU configuration?
> **A:** [verdict]
> **Evidence:** I checked [role names] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-role result] because [per-role structural reason].

For each role where a path exists: add ESCALATION-PATH to the Gap Register with the chain: `[Role] -> [Action] -> [Elevated access]`.

**Sharing conflict gate:**

> **Q:** Do any active sharing rules reopen access that the OWD + security role model intends to restrict?
> **A:** [verdict]
> **Evidence:** I checked sharing rules [list rule names or "no rules found"] for entities [list] -- [per-rule result] because [per-rule comparison to OWD + role scope].

Rules where overreach is confirmed: add SHARING-CONFLICT to Gap Register.

**Team membership gate:**

> **Q:** Is team membership for any team-scoped role controlled in a way that prevents unauthorized elevation?
> **A:** [verdict]
> **Evidence:** I checked team [name] membership control -- [mechanism] controls addition; self-addition is [possible/not possible] because [specific constraint].

**Least-privilege gate:**

> **Q:** Does each role in the model hold only the privileges its persona requires?
> **A:** [verdict per role]
> **Evidence:** I checked [role] against persona [job function] -- excess privileges: [list or NONE] because [comparison of held vs. required privileges].

For over-privileged roles: state the specific reduction and target scope.

**Cross-entity cascade gate:**

> **Q:** What is the lowest-privilege path to the highest-sensitivity entity, and is each hop intentional?
> **A:** [trace through at least two hops]
> **Evidence:** I traced [Role] -> [Entity A, access] -> [Relationship type, cascade setting] -> [Entity B, access] -- [hop 1 intentional/emergent because reason]; -> [Relationship type, cascade setting] -> [Entity C, access] -- [hop 2 intentional/emergent because reason].

---

## STAGE 3 -- ROLE DIFFERENTIATION AND REMEDIATION

**Customer Service Representative gate:**

> **Q:** Does the Customer Service Representative role access any sensitive field or operation beyond what the CS job function requires?
> **A:** [verdict]
> **Evidence:** I checked CS access to [entity list and sensitive field list] -- [per-entity/per-field result] because [FLS profile / OWD / role scope].

**Dataverse Security Expert gate:**

> **Q:** Does the Dataverse Security Expert role hold privileges that exceed least-privilege for a security configuration task?
> **A:** [verdict]
> **Evidence:** I checked the expert role's privileges beyond CS access -- [excess list or NONE] because [comparison to what security configuration task requires].

Both roles must appear by name with distinct specific observations.

**Remediation gate:**

> **Q:** Does every gap in the Gap Register have a specific Exact Fix that names the configuration object and the post-fix state?
> **A:** [Yes -- verified / No -- complete fixes now]
> **Evidence:** Every Exact Fix row names [field security profile / sharing rule / security role privilege / OWD setting] and states current state -> target state.

Now return to the GAP REGISTER and fill it in completely.

---

## V-05 -- Combined: Full Aspirational Scaffold (C-11 + C-12 + C-13 + C-14)

**Axis:** All four aspirational criteria wired as structural constraints -- pre-committed gap register (C-11), scope token lexicon (C-13), question-form gates (C-14), evidence-cited rule-outs (C-12)
**Hypothesis:** C-11 through C-14 are discipline enforcers, not content additions. Embedded as structural rules in a prompt that already satisfies C-01 through C-10, they do not increase the required output length -- they change the format of what was already required. A single prompt can target all four simultaneously: declare the gap register before entities (C-11), lock the scope vocabulary before any table (C-13), wire every critical gate as a question (C-14), require every answer to carry an evidence citation (C-12).

---

You are running a permissions trace signal for: {{topic}}

---

## PREAMBLE -- FOUR STRUCTURAL CONSTRAINTS (read before starting)

This trace enforces four structural rules. Violating any rule is an inline failure -- correct it before advancing.

**Rule 1 (C-11 -- Pre-Committed Register):** The Gap Category Register below is declared now, before you enumerate any entity. You may add rows but may not remove categories. Retroactive gap reporting (discovering a gap type after analysis and claiming it was always tracked) is an inline failure.

**Rule 2 (C-13 -- Scope Token Lexicon):** Every Record Scope cell must use exactly one token from the SCOPE LEXICON below. Prose scope descriptions ("appropriate records," "permitted access," "relevant data") are SCOPE-FAILs -- mark them and correct before advancing.

**Rule 3 (C-14 -- Question-Form Gates):** Every critical security check appears as a question with a required answer. A question that has no answer is an inline failure.

**Rule 4 (C-12 -- Evidence-Citation):** Every gate answer must include an Evidence line in the form "I checked [named objects] -- [result] because [reason]." A verdict without an Evidence line is an inline failure.

---

## SCOPE LEXICON (locked)

| Token | Meaning |
|-------|---------|
| `Org` | All records in the organization |
| `BU` | Records owned by users in the same business unit |
| `Parent-Child BU` | Records owned by users in the same BU and all child BUs |
| `Team:[name]` | Records owned by or shared to named team (substitute actual team name) |
| `User` | Only the user's own records |
| `Sharing:[rule name]` | Records accessible via named sharing rule (substitute actual rule name) |

---

## GAP CATEGORY REGISTER (pre-committed -- declare now, before Stage 1)

The following categories are locked. All gap findings must fit one of these types.

| Category | What It Catches |
|----------|----------------|
| FLS-EXPOSURE | Sensitive field accessible without a field security profile |
| ESCALATION-PATH | Role reaches higher privilege level through an available action |
| SHARING-CONFLICT | Sharing rule reopens access the role model intends to restrict |
| TEAM-GAP | Team-scoped operation with uncontrolled or absent team membership |
| CROSS-CASCADE | Relationship behavior grants unintended cross-entity access |
| OWD-MISMATCH | OWD broader than entity sensitivity warrants |

**Gap Findings Table -- do not populate now. Return here after Stage 3.**

| # | Category | Entity | Field (if FLS) | Role | Severity | Exact Fix |
|---|----------|--------|----------------|------|----------|-----------|

Severity: CRITICAL / HIGH / MEDIUM. Exact Fix: name the specific configuration object and post-fix state.

---

## STAGE 1 -- INVENTORY

You are a Dataverse security architect.

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) |
|--------|-----------------|-----------------------------------|

**1b -- Operation-role matrix (one table per entity):**

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|--------|------|-------|--------|--------|--------------|

All Record Scope cells: SCOPE LEXICON tokens only. Mark any SCOPE-FAIL and correct before 1c.

**1c -- Field-level security gate:**

> **Q:** Does every sensitive field on every entity have a field security profile?
> **A:** [verdict per entity]
> **Evidence:** I checked Security > Field Security Profiles for [entity list] -- [result per entity] because [profile name / no profile found / no sensitive fields; fields reviewed: list].

For each sensitive field with no profile: add FLS-EXPOSURE row to Gap Findings Table now. Severity = CRITICAL.

| Entity | Field | Sensitivity | FLS Profile Name | Roles: Read | Roles: Write |
|--------|-------|-------------|-----------------|-------------|--------------|

---

## STAGE 2 -- GAP ANALYSIS

Apply Rules 3 and 4 to every gate. Every question requires an answer. Every answer requires an Evidence line.

**Escalation gate:**

> **Q:** Can any role reach a higher privilege level through team membership, security role assignment, ownership reassignment, or BU configuration?
> **A:** [verdict]
> **Evidence:** I checked [role list] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-role result] because [per-role structural reason].

Finding format: `[Role] -> [Action] -> [Elevated access]` -- add ESCALATION-PATH to Gap Findings Table.

**Sharing conflict gate:**

> **Q:** Do any active sharing rules reopen access the OWD + security role model intends to restrict?
> **A:** [verdict]
> **Evidence:** I checked sharing rules [list rule names or "no rules found"] for [entity list] -- [per-rule result] because [comparison of opened access to OWD + role scope].

Overreach confirmed: add SHARING-CONFLICT to Gap Findings Table. Build the full sharing rule table:

| Rule Name | Trigger | Access Opened | Record Scope | Intended? | Overreach? |
|-----------|---------|---------------|--------------|-----------|------------|

All Record Scope cells: SCOPE LEXICON tokens only.

**Team membership gate:**

> **Q:** Is team membership for every team-scoped role controlled in a way that prevents unauthorized elevation?
> **A:** [verdict]
> **Evidence:** I checked team [name] membership control -- [mechanism]; self-addition is [possible/not possible] because [specific constraint].

Uncontrolled membership or possible self-addition: add TEAM-GAP to Gap Findings Table.

**OWD sensitivity gate:**

> **Q:** Is the org-wide default for each high-sensitivity entity more permissive than the data warrants?
> **A:** [verdict per high-sensitivity entity]
> **Evidence:** I checked OWD for [entity] -- [OWD token] -- [justified / unjustified] because [FLS compensates / no compensating control exists].

Unjustified OWD: add OWD-MISMATCH to Gap Findings Table.

**Cross-entity cascade gate:**

> **Q:** What is the lowest-privilege path to the highest-sensitivity entity, and is each hop intentional?
> **A:** [trace]
> **Evidence:** I traced [Role] -> [Entity A, Record Scope: <token>] -> [Relationship: type, cascade setting] -> [Entity B, Record Scope: <token>] -> [cascade setting] -> [Entity C, Record Scope: <token>] -- hop 1 [intentional/emergent because reason]; hop 2 [intentional/emergent because reason].

All Record Scope cells in the trace: SCOPE LEXICON tokens only.

---

## STAGE 3 -- ROLE ASSESSMENT AND REMEDIATION

**Customer Service Representative gate:**

> **Q:** Does the Customer Service Representative role access any sensitive field or operation beyond what the CS job function requires?
> **A:** [verdict]
> **Evidence:** I checked CS access for [entity list, sensitive field list] -- [per-item result] because [FLS profile / role scope / OWD].

**Dataverse Security Expert gate:**

> **Q:** Does the Dataverse Security Expert role hold any privilege that exceeds least-privilege for a security configuration task?
> **A:** [verdict]
> **Evidence:** I checked expert privileges beyond CS access -- [excess list or NONE] because [comparison against security configuration task scope].

Both roles must appear by name. Both must have specific distinct observations -- a merged summary fails.

**Least-privilege scoring:**

| Role | Persona | Excess Privileges | LP Score (0-10) | Over-Privileged? | Reduction Required |
|------|---------|-------------------|-----------------|------------------|--------------------|

For LP Score < 7: state the specific privilege to reduce and the target scope.

**Attack scenario (if any ESCALATION-PATH found):**
Step-by-step: `Starting role -> Action sequence -> Gained access`. Abstract statements do not satisfy this section.

**Remediation gate:**

> **Q:** Does every entry in the Gap Findings Table have a specific Exact Fix that names the configuration object and post-fix state?
> **A:** [Yes -- verified / No -- complete now]
> **Evidence:** Every Exact Fix row names [field security profile / sharing rule / security role privilege / OWD setting], current state, and target state.

Format per finding: "Change [configuration object name] in [solution location] from [current state] to [target state]. Post-fix: [what a security auditor would observe to confirm the fix]."

Now return to the Gap Findings Table in the Pre-Committed Register and fill it in completely. Every row must fit a pre-declared category. Every Exact Fix must name the object.
