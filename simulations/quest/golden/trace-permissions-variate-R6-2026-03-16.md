# trace-permissions Variate -- Round 6 (Rubric v6)
**Date:** 2026-03-16
**Rubric:** v6 (C-01 through C-24)
**New criteria targeted this round:** C-20 (pre-declaration commitment as two-point verifiable contract), C-21 (structural isolation of closing mechanism in dedicated column), C-22 (inertia framing -- design assumption stated above each vector block), C-23 (no-finding as positive declaration with equal evidential standard), C-24 (roll-up mechanisms-cited field restates per-verdict, not references)
**Prior round retained:** Essential C-01--C-04, recommended C-05--C-07, aspirational C-08--C-19 are structurally enforced throughout

---

## Round 6 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Lifecycle emphasis -- pre-declaration commitment block before each role (C-20 single-axis) | Before tracing any vectors for a Write-capable role, requiring a COMMITMENT DECLARATION block that names the structural assumption for each of the five vectors creates a two-point verifiable contract: the assumption is on record before analysis starts, and the NOT POSSIBLE verdict at the vector level must trace to a named declaration. A verdict without a matching prior assumption is a visible contract violation -- the Phase 3 gate check enforces this |
| V-02 | Inertia framing -- design assumption mini-block per vector (C-22 single-axis) | Breaking the monolithic five-vector table into per-vector mini-blocks where each opens with an explicit "Design Assumption" statement converts the NOT POSSIBLE verdict from a bare conclusion into a confirmation or refutation of a prior commitment. A NOT POSSIBLE verdict that says "Assumption Confirmed: [cited evidence]" is structurally different from one that says "NOT POSSIBLE"; the former is checkpointed against the assumption above it, the latter is unconstrained |
| V-03 | Phrasing register -- no-finding as formal No-Finding declaration (C-23 single-axis) | Requiring every absence -- NOT POSSIBLE vector verdict, clean sharing rule, gap-free entity, no team dependency found -- to be expressed as a formal declaration naming (a) what was checked, (b) what configuration state was confirmed absent, and (c) the conclusion enforces evidential symmetry throughout. A model that applies audit declaration discipline to positive findings automatically generates it for negative ones when the format demands it |
| V-04 | Combined: output format (structurally isolated Structural Basis column, C-21) + role sequence (self-contained roll-up with mechanisms restated inline, C-24) | Round 5 V-04's Closing Mechanism column shared the column header space with instruction prose, and the roll-up's Mechanisms cited field pointed back to the table. V-04 here restructures the column as a single-purpose Structural Basis field that holds exactly one structural fact per NOT POSSIBLE row -- no verdict language, no evidence prose -- and rewrites the roll-up block so Mechanisms cited restates each mechanism inline by vector name, making the roll-up auditable independently of the table |
| V-05 | Combined: pre-declaration (C-20) + inertia framing (C-22) + symmetric evidence (C-23) + structural column isolation (C-21) + self-contained roll-up (C-24) | Full five-criterion package. The COMMITMENT DECLARATION anchors each role's analysis with explicit assumptions per vector (C-20); each vector block opens with that assumption restated as the inertia frame (C-22); every absence at any level carries a formal No-Finding declaration (C-23); the Structural Basis column is exclusively for closing mechanism citations with no co-mingled prose (C-21); the roll-up restates each mechanism inline (C-24). All five new criteria are independently enforceable and do not overlap |

---

## V-01 -- Lifecycle Emphasis: Pre-Declaration Commitment Block

**Axis:** Lifecycle emphasis (before tracing escalation vectors for any Write-capable role, a COMMITMENT DECLARATION block is required naming the structural assumption that governs each vector's NOT POSSIBLE verdict -- C-20 single-axis)
**Hypothesis:** Round 5 V-03 introduced pre-declaration as part of a phase-gate discipline, but the declaration was framed as a Phase 3 preamble rather than a per-role contract. C-20 requires the declaration to be traceable at two points: the assumption is on record before analysis starts for that role, and the NOT POSSIBLE verdict at the vector level explicitly references the declared assumption. Making the COMMITMENT DECLARATION a mandatory named block before each role's vector table -- with the Phase 3 gate checking that every NOT POSSIBLE verdict traces to a prior declaration -- creates the two-point contract C-20 requires.

---

You are running a permissions trace signal for: {{topic}}

---

**SECURITY GAP LOG -- add rows progressively. Assign G-## identifiers at discovery.**

| G-## | Entity | Field / Operation | Role(s) | Gap Type | Risk |
|------|--------|-------------------|---------|----------|------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH
Risk: CRITICAL / HIGH / MEDIUM

Assign the next sequential identifier (G-01, G-02, ...) the moment a gap is identified. Do not defer to phase end.

---

## PHASE 1 -- INVENTORY

**1a -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason |
|--------|-----------------|-------------|--------|

Sensitivity: High (PII, Financial, Credential, Health) / Medium (Internal-only, cross-BU risk) / Low (lookup, reference, config)

**1b -- Role catalog:**

| Role | Type (Stock / Custom) | Write-Capable? | Persona |
|------|-----------------------|----------------|---------|

Write-Capable = YES for any role holding Write, Delete, or Assign on any entity.
Stock roles to confirm: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1c -- Analysis order:**

State: "I will trace entities in this order: [list, highest to lowest sensitivity]. First gap ID to assign: G-01."

---

## PHASE 1 GATE

| Check | Answer |
|-------|--------|
| All entities that {{topic}} touches are in the 1a table | YES / NO |
| All roles with any privilege are in the 1b catalog | YES / NO |
| Write-Capable flag is set for every role holding W/D/A | YES / NO |
| Analysis order declared | YES / NO |

**PHASE 1 COMPLETE: [YES / NO -- resolve before continuing]**

---

## PHASE 2 -- PER-ENTITY TRACE

Complete all steps for one entity, then write the ENTITY CLOSURE block before advancing to the next entity.

---

### Entity: [name] (Sensitivity: [rating])

**2a -- Operation-role matrix:**

| Role | Create | Read | Write | Delete | Assign | Record Scope |
|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Parent-Child BU / Team / User / Sharing-[rule name]
Every role from 1b with any privilege on this entity must appear.

**2b -- Field-level security:**

| Field | Sensitivity | FLS Profile | Read: Allowed Roles | Write: Allowed Roles | Denied Roles |
|-------|-------------|-------------|---------------------|----------------------|--------------|

Rules:
- Every field with Sensitivity != Not-Sensitive must have a row
- FLS Profile = NONE for a sensitive field: add to Security Gap Log now (MISSING-FLS). CRITICAL for PII/Credential/Health; HIGH for Financial/Internal-Audit. Assign G-## now.
- Denied Roles must be populated explicitly -- "none denied" is valid only when confirmed

**2c -- Sharing rule audit:**

| Rule Name | Trigger | Access Granted | Recipient | Verdict: Expected / Conflict-[G-##] |
|-----------|---------|----------------|-----------|-------------------------------------|

For each conflict: assign G-## now. Log to Security Gap Log.

Per-role sharing rule statements (required for every role in 2a, regardless of outcome):
"[Role] on [Entity]: sharing rules [expand access -- [rule name], see G-##] OR [confirmed do not expand -- basis: [evidence confirming no criteria-based or manual sharing targets this role]]."

**2d -- Team membership dependency:**

For any role whose access depends on team membership: "Users in [Role] not in [Team] cannot access [record type] because [OWD+scope]. Team controlled by [mechanism]. Self-addition [possible / not possible]: [reason]. [If possible and unintended: assign G-##.]"

If no team dependency: "Confirmed: [Entity] access requires no team membership for any role. Checked: [what was reviewed]."

**2e -- Entity-level escalation check:**

For each role in 2a with W, D, or A: check whether that access can reach a higher privilege level via record ownership transfer, sharing to a higher-privilege scope, or field modification affecting role or BU assignment.

- Found path: assign G-## (ESCALATION-PATH). Chain: `[Role] -> [action on [Entity]] -> [elevated access reached]`
- No path: "Checked [Role] on [Entity]: audited [specific operations]. No escalation via [mechanisms checked] because [reason per mechanism]."

---

### ENTITY CLOSURE: [Entity Name]

```
Operations reviewed:       [List each operation (C/R/W/D/A) audited per role -- do not write "all operations"]
Sensitive fields confirmed: [List each sensitive field reviewed, or "none -- confirmed by reviewing [field names]"]
Gaps logged this entity:   [G-01, G-02 ... / NONE -- one of these two forms; blank is not valid]
Sharing rule verdicts:     [N of N roles in scope received explicit sharing rule statements: YES]
Escalation checked:        [Roles with W/D/A that received an explicit escalation check: list]
Status:                    CLOSED
```

Rules:
- The `Gaps logged` field takes a G-## list or NONE -- never blank, never "see above"
- An entity where gaps were found must name those gaps by G-## in this block
- An entity where no gaps were found states NONE explicitly
- A closure block with any field blank is incomplete; the entity has not been closed

---

*(Repeat Phase 2 section + ENTITY CLOSURE for each entity, highest to lowest sensitivity.)*

---

## PHASE 2 GATE

| Check | Answer |
|-------|--------|
| Every entity in the 1a catalog has a Phase 2 section | YES / NO |
| Every entity has an ENTITY CLOSURE block using the standard template | YES / NO |
| Every gap-containing entity names its gaps by G-## in the CLOSURE block | YES / NO |
| Every gap-free entity explicitly states NONE in the CLOSURE block | YES / NO |
| Every role received an explicit sharing rule statement for every entity it appears in | YES / NO |

**PHASE 2 COMPLETE: [YES / NO]**

---

## PHASE 3 -- ESCALATION VECTOR ANALYSIS (organized by Write-capable role)

For each role marked Write-Capable = YES in Phase 1b, complete the full sequence: COMMITMENT DECLARATION, then five-vector table, then ESCALATION ROLL-UP -- in that order. Do not begin the vector table until the COMMITMENT DECLARATION is written.

---

### COMMITMENT DECLARATION: [Role Name]

Before tracing escalation vectors for [Role Name], I declare the structural assumptions under which NOT POSSIBLE verdicts will be issued for this role. Every NOT POSSIBLE verdict in the five-vector table below must trace to one of these declared assumptions. A NOT POSSIBLE verdict issued without a matching prior assumption in this block is a contract violation.

| Vector | Structural Assumption Governing NOT POSSIBLE Verdict |
|--------|------------------------------------------------------|
| Sharing rule creation | Assumption: [Role Name] is expected to lack the privilege to create or modify sharing rules (e.g., Share privilege on [Entity], or admin delegation) because [stated design reason]. |
| Team self-injection | Assumption: [Role Name] is expected to be unable to add itself to owner teams with higher-privilege record scope because [stated mechanism -- e.g., team membership restricted to System Admin]. |
| Field-value escalation | Assumption: No field writable by [Role Name] changes role assignment, BU membership, or security profile because [stated basis -- FLS confirmed or no such field exists in the entity set]. |
| Role hierarchy traversal | Assumption: Role hierarchy does not elevate [Role Name]'s record scope because [stated basis -- hierarchy disabled, or all ancestor roles have equivalent or narrower scope]. |
| Record ownership transfer | Assumption: Assigning records to another owner does not expand [Role Name]'s own visibility because [stated OWD behavior and confirmation method]. |

Commitment: the five-vector analysis below will verify each assumption. A confirmed assumption produces NOT POSSIBLE. A refuted assumption produces POSSIBLE and a G-## entry in the Security Gap Log.

---

### Escalation Vector Audit: [Role Name]

**Write access held by this role:**

For each entity where this role holds W, D, or A: `[Entity]: [operations] at [record scope]`

**Five-vector table:**

| Vector | Mechanism Description | Verdict | Closing Mechanism (NOT POSSIBLE only) |
|--------|----------------------|---------|---------------------------------------|
| Sharing rule creation | Can this role create or modify sharing rules to expand its own record access? | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: name the specific privilege confirmed absent and state which declared assumption this confirms. POSSIBLE: N/A -- log G-##] |
| Team self-injection | Can this role add itself to a team with higher-privilege record scope? | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: name the specific team management privilege absent or team configuration that prevents self-addition, tracing to the declared assumption. POSSIBLE: N/A -- log G-##] |
| Field-value escalation | Can this role write a field whose value changes role assignment, BU membership, or security profile? | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: name the specific fields audited and the FLS profile denying write, or confirm no such field exists in the entity set -- tracing to the declared assumption. POSSIBLE: N/A -- log G-##] |
| Role hierarchy traversal | Does the role hierarchy chain this role to a parent with broader access? | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: state whether role hierarchy is enabled; name ancestor roles checked and their scopes; confirm no parent broadens access -- tracing to the declared assumption. POSSIBLE: N/A -- log G-##] |
| Record ownership transfer | Can this role assign records to an owner in a different scope, triggering broader visibility? | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: state whether Assign is held; name OWD behavior under transferred ownership; confirm no cross-BU or org scope expansion -- tracing to the declared assumption. POSSIBLE: N/A -- log G-##] |

Column rules:
- `Closing Mechanism` is required for every NOT POSSIBLE verdict and must include a reference to the declared assumption it confirms
- `Closing Mechanism` for a POSSIBLE verdict must read exactly: `N/A -- G-##` citing the gap log entry
- A NOT POSSIBLE verdict that does not trace to a named assumption in the COMMITMENT DECLARATION above is a contract violation

---

### ESCALATION ROLL-UP: [Role Name]

```
Vectors assessed:      [count and list: sharing rule creation, team self-injection, field-value escalation, role hierarchy traversal, record ownership transfer]
POSSIBLE count:        [count / NONE]
NOT POSSIBLE count:    [count]
Mechanisms cited:      [list the closing mechanism per NOT POSSIBLE verdict by vector name]
Composite verdict:     [no escalation path identified for this role / ESCALATION PATHS: G-##, G-##]
Declaration honored:   [YES -- every NOT POSSIBLE verdict traces to a declared assumption / NO -- identify which verdict lacks a prior declaration]
```

---

*(Repeat COMMITMENT DECLARATION + five-vector table + ESCALATION ROLL-UP for each Write-capable role.)*

---

## PHASE 3 GATE

| Check | Answer |
|-------|--------|
| Every Write-capable role has a COMMITMENT DECLARATION before its vector table | YES / NO |
| Every Write-capable role has a five-vector table | YES / NO |
| Every NOT POSSIBLE row has a non-blank Closing Mechanism naming a structural basis | YES / NO |
| Every NOT POSSIBLE row traces its Closing Mechanism to a named declared assumption | YES / NO |
| Every POSSIBLE row has a G-## in the Security Gap Log | YES / NO |
| Every Write-capable role has an ESCALATION ROLL-UP block | YES / NO |
| Declaration honored field in every roll-up reads YES | YES / NO |

**PHASE 3 COMPLETE: [YES / NO]**

---

## PHASE 4 -- REMEDIATION AND DEFENSE-IN-DEPTH

**4a -- Gap remediation:**

For each G-## in the Security Gap Log:
`[G-##]: Change [element] on [entity/field/role] from [current state] to [target state] in [solution location]. After fix: [behavioral change for the affected role].`

Cite by G-## identifier. Generic advice ("review permissions", "add FLS") does not qualify. Every G-## in the log must have a 4a entry.

**4b -- Defense-in-depth assessment:**

| Entity | Security Role: Independent? | FLS: Independent? | Record Scope: Independent? | Single Point of Failure? |
|--------|----------------------------|-------------------|---------------------------|--------------------------|

Independent = YES if this layer enforces access even when the other two layers are misconfigured. Single POF = YES: add G-## if not already logged.

**4c -- Stock role least-privilege:**

For Customer Service Representative and any other stock role present:
- Baseline privileges relevant to {{topic}}
- Whether custom configuration strengthened or weakened the baseline
- Least-privilege verdict: SATISFIED or EXCESS -- [specific privilege to reduce]

---

## OUTPUT REQUIREMENTS

- COMMITMENT DECLARATION block precedes the vector table for every Write-capable role
- Every NOT POSSIBLE vector verdict cites its closing mechanism AND traces to a named declared assumption
- ENTITY CLOSURE blocks appear after every entity section regardless of gap state
- Every G-## in the Security Gap Log has a 4a remediation entry citing the same identifier
- ESCALATION ROLL-UP appears after every Write-capable role's vector table with all fields populated

---

## V-02 -- Inertia Framing: Design Assumption Mini-Block Per Vector

**Axis:** Inertia framing (each of the five escalation vectors is a mini-block that opens with an explicit "Design Assumption" statement; the verdict is expressed as "Assumption Confirmed" or "Assumption Refuted"; a NOT POSSIBLE verdict without a prior stated assumption in the same block does not pass -- C-22 single-axis)
**Hypothesis:** Round 5 V-05 introduced hypothesis-per-vector framing as a combined axis with audit evidence standard. C-22 isolates this pattern: the assumption is not a pre-analysis declaration for the whole role (that is C-20), it is an inertia anchor stated at the top of each vector's own block. By converting the monolithic five-vector table into five mini-blocks each with Assumption -> Evidence -> Verdict flow, the verdict becomes a verification of a prior commitment rather than a free-form conclusion. The model cannot issue "NOT POSSIBLE" without first stating the assumption that makes NOT POSSIBLE the expected outcome; a verdict that confirms an assumption is checkpointed; one issued without an assumption is unconstrained.

---

You are running a permissions trace signal for: {{topic}}

---

**SECURITY GAP LOG -- add rows progressively. Assign G-## identifiers at discovery.**

| G-## | Entity | Field / Operation | Role(s) | Gap Type | Risk |
|------|--------|-------------------|---------|----------|------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH
Risk: CRITICAL / HIGH / MEDIUM

Assign the next sequential identifier (G-01, G-02, ...) the moment a gap is identified. Do not defer.

---

## PHASE 1 -- INVENTORY

**1a -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason |
|--------|-----------------|-------------|--------|

Sensitivity: High (PII, Financial, Credential, Health) / Medium (Internal-only, cross-BU risk) / Low (lookup, reference, config)

**1b -- Role catalog:**

| Role | Type (Stock / Custom) | Write-Capable? | Persona |
|------|-----------------------|----------------|---------|

Write-Capable = YES for any role holding Write, Delete, or Assign on any entity.
Stock roles to confirm: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1c -- Analysis order:**

State: "I will trace entities in this order: [list, highest to lowest sensitivity]. First gap ID to assign: G-01."

---

## PHASE 1 GATE

| Check | Answer |
|-------|--------|
| All entities that {{topic}} touches are in the 1a table | YES / NO |
| All roles with any privilege are in the 1b catalog | YES / NO |
| Write-Capable flag is set for every role holding W/D/A | YES / NO |
| Analysis order declared | YES / NO |

**PHASE 1 COMPLETE: [YES / NO -- resolve before continuing]**

---

## PHASE 2 -- PER-ENTITY TRACE

Complete all steps for one entity, then write the ENTITY CLOSURE block before advancing to the next entity.

---

### Entity: [name] (Sensitivity: [rating])

**2a -- Operation-role matrix:**

| Role | Create | Read | Write | Delete | Assign | Record Scope |
|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Parent-Child BU / Team / User / Sharing-[rule name]
Every role from 1b with any privilege on this entity must appear.

**2b -- Field-level security:**

| Field | Sensitivity | FLS Profile | Read: Allowed Roles | Write: Allowed Roles | Denied Roles |
|-------|-------------|-------------|---------------------|----------------------|--------------|

Rules:
- Every field with Sensitivity != Not-Sensitive must have a row
- FLS Profile = NONE for a sensitive field: add to Security Gap Log now. Assign G-## now.
- Denied Roles must be populated explicitly -- "none denied" is valid only when confirmed

**2c -- Sharing rule audit:**

| Rule Name | Trigger | Access Granted | Recipient | Verdict: Expected / Conflict-[G-##] |
|-----------|---------|----------------|-----------|-------------------------------------|

Per-role sharing rule statements (required for every role in 2a, regardless of outcome):
"[Role] on [Entity]: sharing rules [expand access -- [rule name], see G-##] OR [confirmed do not expand -- basis: [evidence]]."

**2d -- Team membership dependency:**

For any role whose access depends on team membership: "Users in [Role] not in [Team] cannot access [record type] because [OWD+scope]. Team controlled by [mechanism]. Self-addition [possible / not possible]: [reason]. [If possible and unintended: assign G-##.]"

If no team dependency: "Confirmed: [Entity] access requires no team membership for any role. Checked: [what was reviewed]."

**2e -- Entity-level escalation check:**

For each role in 2a with W, D, or A: check whether that access can reach a higher privilege level via record ownership transfer, sharing to a higher-privilege scope, or field modification affecting role or BU assignment.

- Found path: assign G-## (ESCALATION-PATH). Chain: `[Role] -> [action on [Entity]] -> [elevated access reached]`
- No path: "Checked [Role]: [specific operations audited]. No escalation via Assign / Share / field modification because [specific reason per mechanism]."

---

### ENTITY CLOSURE: [Entity Name]

```
Operations reviewed:       [List each operation (C/R/W/D/A) audited per role]
Sensitive fields confirmed: [List each sensitive field reviewed, or "none -- confirmed by reviewing [field names]"]
Gaps logged this entity:   [G-## list / NONE]
Sharing rule verdicts:     [N of N roles received explicit sharing rule statements: YES]
Escalation checked:        [Roles with W/D/A that received an explicit escalation check: list]
Status:                    CLOSED
```

---

*(Repeat Phase 2 section + ENTITY CLOSURE for each entity.)*

---

## PHASE 2 GATE

| Check | Answer |
|-------|--------|
| Every entity in the 1a catalog has a Phase 2 section | YES / NO |
| Every entity has an ENTITY CLOSURE block using the standard template | YES / NO |
| Every gap-containing entity names its gaps by G-## in the CLOSURE block | YES / NO |
| Every gap-free entity explicitly states NONE in the CLOSURE block | YES / NO |
| Every role received an explicit sharing rule statement for every entity it appears in | YES / NO |

**PHASE 2 COMPLETE: [YES / NO]**

---

## PHASE 3 -- ESCALATION VECTOR ANALYSIS (organized by Write-capable role)

For each role marked Write-Capable = YES in Phase 1b, complete the five vector mini-blocks in sequence, then write the ESCALATION ROLL-UP. Each vector is a mini-block with three elements: Design Assumption, Evidence, Verdict. The Design Assumption must be written before the verdict. A verdict issued without a prior Design Assumption in the same vector block fails the inertia anchor requirement.

---

### Escalation Vector Audit: [Role Name]

**Write access held by this role:**

For each entity where this role holds W, D, or A: `[Entity]: [operations] at [record scope]`

---

#### Vector 1: Sharing rule creation

> **Design Assumption:** [Role Name] is expected to lack the privilege to create or modify sharing rules because [state design intent -- e.g., "only System Administrator holds the Share privilege at org scope; Service Rep is installed without delegation"]. If this assumption holds, the verdict is NOT POSSIBLE. If refuted, a G-## entry is required.

**Evidence:** [State the specific privilege checked, the configuration reviewed, and what was found.]

**Verdict:** `NOT POSSIBLE -- Assumption Confirmed: [name the structural fact that confirms the stated assumption]` OR `POSSIBLE -- Assumption Refuted: G-##`

---

#### Vector 2: Team self-injection

> **Design Assumption:** [Role Name] is expected to be unable to add itself to owner teams with broader record scope because [state design intent -- e.g., "owner team membership is managed by System Admin only; access teams allow self-addition but grant access-level scope only, not owner scope"]. If this assumption holds, the verdict is NOT POSSIBLE.

**Evidence:** [State the specific team types checked, the membership permission audited, and what was found.]

**Verdict:** `NOT POSSIBLE -- Assumption Confirmed: [name the structural fact]` OR `POSSIBLE -- Assumption Refuted: G-##`

---

#### Vector 3: Field-value escalation

> **Design Assumption:** No field writable by [Role Name] changes role assignment, BU membership, or security profile because [state design intent -- e.g., "SystemUser.BusinessUnit is not writeable by Service Rep; no custom field maps to security role assignment"]. If this assumption holds, the verdict is NOT POSSIBLE.

**Evidence:** [List the specific fields audited, the FLS profiles checked, and what was found.]

**Verdict:** `NOT POSSIBLE -- Assumption Confirmed: [name the structural fact]` OR `POSSIBLE -- Assumption Refuted: G-##`

---

#### Vector 4: Role hierarchy traversal

> **Design Assumption:** The role hierarchy does not elevate [Role Name]'s record scope beyond its direct assignment because [state design intent -- e.g., "role hierarchy is enabled for Read but all ancestor roles are scoped BU-only; no ancestor holds Org scope on the entities in question"]. If this assumption holds, the verdict is NOT POSSIBLE.

**Evidence:** [State whether hierarchy is enabled, list the ancestor roles inspected and their scopes, and confirm the highest ancestor's access level.]

**Verdict:** `NOT POSSIBLE -- Assumption Confirmed: [name the structural fact]` OR `POSSIBLE -- Assumption Refuted: G-##`

---

#### Vector 5: Record ownership transfer

> **Design Assumption:** Assigning a record to another owner does not expand [Role Name]'s own visibility because [state design intent -- e.g., "OWD is Private; transferred ownership moves the record out of Service Rep's User-scope access; no sharing rule re-grants it; the role loses access after transfer rather than gaining broader scope"]. If this assumption holds, the verdict is NOT POSSIBLE.

**Evidence:** [State whether Assign is held, the OWD behavior confirmed, and any sharing rule effect on transferred records.]

**Verdict:** `NOT POSSIBLE -- Assumption Confirmed: [name the structural fact]` OR `POSSIBLE -- Assumption Refuted: G-##`

---

### ESCALATION ROLL-UP: [Role Name]

```
Vectors assessed:    5 (sharing rule creation, team self-injection, field-value escalation, role hierarchy traversal, record ownership transfer)
POSSIBLE count:      [count / NONE]
NOT POSSIBLE count:  [count]
Assumptions honored: [count of verdicts that confirmed their stated assumption / count of vectors assessed]
Mechanisms cited:    [list the structural fact cited per NOT POSSIBLE verdict by vector name]
Composite verdict:   [no escalation path identified for this role / ESCALATION PATHS: G-##, G-##]
```

---

*(Repeat Vector Audit + ESCALATION ROLL-UP for each Write-capable role.)*

---

## PHASE 3 GATE

| Check | Answer |
|-------|--------|
| Every Write-capable role has five vector mini-blocks | YES / NO |
| Every vector mini-block has a Design Assumption before its verdict | YES / NO |
| Every NOT POSSIBLE verdict explicitly confirms the stated assumption in that vector block | YES / NO |
| Every POSSIBLE verdict explicitly states which assumption was refuted and logs G-## | YES / NO |
| Every Write-capable role has an ESCALATION ROLL-UP with all fields populated | YES / NO |

**PHASE 3 COMPLETE: [YES / NO]**

---

## PHASE 4 -- REMEDIATION AND DEFENSE-IN-DEPTH

**4a -- Gap remediation:**

For each G-## in the Security Gap Log:
`[G-##]: Change [element] on [entity/field/role] from [current state] to [target state] in [solution location]. After fix: [behavioral change for the affected role].`

Cite by G-## identifier. Every G-## in the log must have a 4a entry.

**4b -- Defense-in-depth assessment:**

| Entity | Security Role: Independent? | FLS: Independent? | Record Scope: Independent? | Single Point of Failure? |
|--------|----------------------------|-------------------|---------------------------|--------------------------|

**4c -- Stock role least-privilege:**

For Customer Service Representative and any other stock role present:
- Baseline privileges relevant to {{topic}}
- Whether custom configuration strengthened or weakened the baseline
- Least-privilege verdict: SATISFIED or EXCESS -- [specific privilege to reduce]

---

## OUTPUT REQUIREMENTS

- Each vector is a mini-block with Design Assumption -> Evidence -> Verdict flow; table rows are not used for Phase 3
- Every NOT POSSIBLE verdict says "Assumption Confirmed: [structural fact]" tracing to the assumption above it
- Every POSSIBLE verdict says "Assumption Refuted: G-##" naming the gap log entry
- ENTITY CLOSURE blocks appear after every entity section regardless of gap state

---

## V-03 -- Phrasing Register: No-Finding as Formal Declaration

**Axis:** Phrasing register (every absence -- NOT POSSIBLE vector verdict, clean sharing rule, gap-free entity, no team dependency -- is expressed as a formal No-Finding declaration naming (a) what was checked, (b) what configuration state was confirmed absent, and (c) the conclusion; bare negatives "none found", "NOT POSSIBLE", "NONE" without supporting evidence do not satisfy the format -- C-23 single-axis)
**Hypothesis:** Round 4 V-03 introduced audit certification register for correctness and completeness. C-23 isolates the evidential symmetry requirement: positive findings are always declared with full evidence (role, field, gap type, risk, chain); no-findings must carry the same evidential weight. If the format marks every "no-finding" as a formal declaration with its own evidence fields -- what was checked, what configuration state was confirmed absent, what the conclusion is -- the model cannot produce an evidentially complete positive finding next to a bare negative. The declaration format applies uniformly; absence of evidence becomes visible as a format violation rather than an implied clean bill.

---

You are running a permissions trace signal for: {{topic}}

---

**SECURITY GAP LOG -- add rows progressively. Assign G-## identifiers at discovery.**

| G-## | Entity | Field / Operation | Role(s) | Gap Type | Risk |
|------|--------|-------------------|---------|----------|------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH
Risk: CRITICAL / HIGH / MEDIUM

Assign the next sequential identifier (G-01, G-02, ...) the moment a gap is identified. Do not defer.

---

**No-Finding Declaration format (required wherever absence is stated):**

```
NO FINDING -- [label]
Checked:     [what was reviewed -- entity, field, role, privilege, or configuration element]
Confirmed:   [what configuration state was confirmed absent -- the specific privilege, rule, field, or mechanism that would enable the threat was not found]
Conclusion:  [stated outcome -- the access or escalation path is closed because [specific structural fact]]
```

This format applies to:
- NOT POSSIBLE verdicts in the escalation vector table
- Clean sharing rule findings per role per entity
- Gap-free ENTITY CLOSURE blocks
- Confirmed-no-dependency team membership checks
- Any other explicit statement that no threat or gap was found

A bare negative ("NOT POSSIBLE", "none found", "NONE", "no gaps") without the three-field declaration does not satisfy the evidential standard.

---

## PHASE 1 -- INVENTORY

**1a -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason |
|--------|-----------------|-------------|--------|

Sensitivity: High (PII, Financial, Credential, Health) / Medium (Internal-only, cross-BU risk) / Low (lookup, reference, config)

**1b -- Role catalog:**

| Role | Type (Stock / Custom) | Write-Capable? | Persona |
|------|-----------------------|----------------|---------|

Write-Capable = YES for any role holding Write, Delete, or Assign on any entity.
Stock roles to confirm: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1c -- Analysis order:**

State: "I will trace entities in this order: [list, highest to lowest sensitivity]. First gap ID to assign: G-01."

---

## PHASE 1 GATE

| Check | Answer |
|-------|--------|
| All entities that {{topic}} touches are in the 1a table | YES / NO |
| All roles with any privilege are in the 1b catalog | YES / NO |
| Write-Capable flag is set for every role holding W/D/A | YES / NO |
| Analysis order declared | YES / NO |

**PHASE 1 COMPLETE: [YES / NO -- resolve before continuing]**

---

## PHASE 2 -- PER-ENTITY TRACE

Complete all steps for one entity, then write the ENTITY CLOSURE block before advancing to the next entity.

---

### Entity: [name] (Sensitivity: [rating])

**2a -- Operation-role matrix:**

| Role | Create | Read | Write | Delete | Assign | Record Scope |
|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Parent-Child BU / Team / User / Sharing-[rule name]
Every role from 1b with any privilege on this entity must appear.

**2b -- Field-level security:**

| Field | Sensitivity | FLS Profile | Read: Allowed Roles | Write: Allowed Roles | Denied Roles |
|-------|-------------|-------------|---------------------|----------------------|--------------|

Rules:
- Every field with Sensitivity != Not-Sensitive must have a row
- FLS Profile = NONE for a sensitive field: assign G-## now (MISSING-FLS)
- Denied Roles must be populated explicitly

When a sensitive field has no FLS gap (FLS profile correctly restricts access), state:

```
NO FINDING -- FLS on [field]
Checked:     FLS profile assignment for [field] on [Entity]; roles reviewed: [list]
Confirmed:   No role holds write access to [field] without an explicit FLS profile restriction
Conclusion:  [field] is correctly protected; no MISSING-FLS gap on this field
```

**2c -- Sharing rule audit:**

| Rule Name | Trigger | Access Granted | Recipient | Verdict: Expected / Conflict-[G-##] |
|-----------|---------|----------------|-----------|-------------------------------------|

Per-role sharing rule statements (required for every role in 2a, regardless of outcome):

For roles where sharing rules expand access: "[Role] on [Entity]: sharing rules expand access -- [rule name], see G-##."

For roles where no sharing rule expansion exists, use No-Finding Declaration format:
```
NO FINDING -- Sharing rules for [Role] on [Entity]
Checked:     All criteria-based sharing rules targeting [Entity] with [Role] as recipient; all manual sharing grants for [Entity] records where [Role] holds access
Confirmed:   No criteria-based or manual sharing rule expands [Role]'s access beyond OWD + security role scope
Conclusion:  [Role] access on [Entity] is bounded by [OWD level] + security role privilege only
```

**2d -- Team membership dependency:**

For any role whose access depends on team membership: "Users in [Role] not in [Team] cannot access [record type] because [OWD+scope]. Team controlled by [mechanism]. Self-addition [possible / not possible]: [reason]. [If possible and unintended: assign G-##.]"

If no team dependency, use No-Finding Declaration format:
```
NO FINDING -- Team dependency for [Entity]
Checked:     OWD setting for [Entity]; whether any role in 2a holds access only via team membership; whether team-owned record visibility requires team assignment
Confirmed:   No role in this entity section requires team membership to access [Entity] records
Conclusion:  [Entity] access is governed by security role + OWD scope for all roles; no team dependency gap exists
```

**2e -- Entity-level escalation check:**

For each role in 2a with W, D, or A, check for escalation. For each found path: assign G-## (ESCALATION-PATH). Chain: `[Role] -> [action on [Entity]] -> [elevated access reached]`

For each role where no escalation path exists, use No-Finding Declaration format:
```
NO FINDING -- Escalation from [Role] on [Entity]
Checked:     Assign privilege (present / absent); record ownership transfer effect on [Role]'s own scope; sharing-rule creation via Write on [Entity]; field modification paths to role/BU change
Confirmed:   No Write/Assign/Delete operation available to [Role] on [Entity] elevates access scope
Conclusion:  [Role] cannot escalate from [Entity] operations; [specific structural reason per mechanism checked]
```

---

### ENTITY CLOSURE: [Entity Name]

```
Operations reviewed:       [List each operation (C/R/W/D/A) audited per role]
Sensitive fields confirmed: [List each sensitive field reviewed]
Gaps logged this entity:   [G-## list / NONE -- if NONE: state "confirmed by reviewing [what was checked]"]
Sharing rule verdicts:     [N of N roles received explicit sharing rule declarations (finding or no-finding): YES]
Escalation checked:        [Roles with W/D/A that received explicit escalation declarations (finding or no-finding): list]
Status:                    CLOSED
```

Rule: A "Gaps logged: NONE" entry must be followed by "confirmed by reviewing [what was checked and found absent]" -- it is not a bare negative.

---

*(Repeat Phase 2 section + ENTITY CLOSURE for each entity.)*

---

## PHASE 2 GATE

| Check | Answer |
|-------|--------|
| Every entity in the 1a catalog has a Phase 2 section | YES / NO |
| Every entity has an ENTITY CLOSURE block | YES / NO |
| Every gap-containing entity names its gaps by G-## | YES / NO |
| Every gap-free entity states NONE with a confirmation of what was reviewed | YES / NO |
| Every role received a sharing rule declaration (finding or No-Finding) for every entity | YES / NO |
| Every W/D/A role received an escalation declaration (finding or No-Finding) for every entity | YES / NO |

**PHASE 2 COMPLETE: [YES / NO]**

---

## PHASE 3 -- ESCALATION VECTOR ANALYSIS (organized by Write-capable role)

For each role marked Write-Capable = YES in Phase 1b, complete the five-vector table and ESCALATION ROLL-UP.

**Instruction for the vector table:** The table has four columns: Vector, Mechanism Description, Verdict, Closing Mechanism. For NOT POSSIBLE verdicts, the Verdict cell must use No-Finding Declaration format inline: "NOT POSSIBLE -- [Checked: ...] [Confirmed: ...] [Conclusion: ...]". For POSSIBLE verdicts, the Verdict cell reads "POSSIBLE -- G-##".

---

### Escalation Vector Audit: [Role Name]

**Write access held by this role:**

For each entity where this role holds W, D, or A: `[Entity]: [operations] at [record scope]`

**Five-vector table:**

| Vector | Mechanism Description | Verdict | Closing Mechanism |
|--------|----------------------|---------|--------------------|
| Sharing rule creation | Can this role create or modify sharing rules to expand its own record access? | NOT POSSIBLE -- Checked: [privilege reviewed]; Confirmed: [configuration state confirmed absent]; Conclusion: [path closed because structural fact] OR POSSIBLE -- G-## | [structural mechanism if NOT POSSIBLE; N/A if POSSIBLE] |
| Team self-injection | Can this role add itself to a team with higher-privilege record scope? | NOT POSSIBLE -- Checked: [team types and membership privileges reviewed]; Confirmed: [what was confirmed absent]; Conclusion: [path closed because structural fact] OR POSSIBLE -- G-## | [structural mechanism if NOT POSSIBLE; N/A if POSSIBLE] |
| Field-value escalation | Can this role write a field whose value changes role assignment, BU membership, or security profile? | NOT POSSIBLE -- Checked: [fields and FLS profiles reviewed]; Confirmed: [what was confirmed absent or denied]; Conclusion: [path closed because structural fact] OR POSSIBLE -- G-## | [structural mechanism if NOT POSSIBLE; N/A if POSSIBLE] |
| Role hierarchy traversal | Does the role hierarchy chain this role to a parent with broader access? | NOT POSSIBLE -- Checked: [hierarchy setting and ancestor roles reviewed]; Confirmed: [what was confirmed -- no broader scope exists]; Conclusion: [path closed because structural fact] OR POSSIBLE -- G-## | [structural mechanism if NOT POSSIBLE; N/A if POSSIBLE] |
| Record ownership transfer | Can this role assign records to an owner in a different scope, triggering broader visibility? | NOT POSSIBLE -- Checked: [Assign privilege and OWD behavior reviewed]; Confirmed: [what was confirmed -- no scope expansion on transfer]; Conclusion: [path closed because structural fact] OR POSSIBLE -- G-## | [structural mechanism if NOT POSSIBLE; N/A if POSSIBLE] |

---

### ESCALATION ROLL-UP: [Role Name]

```
Vectors assessed:    5 (sharing rule creation, team self-injection, field-value escalation, role hierarchy traversal, record ownership transfer)
POSSIBLE count:      [count / NONE]
NOT POSSIBLE count:  [count]
Mechanisms cited:    [list closing mechanism per NOT POSSIBLE verdict by vector name]
Composite verdict:   [no escalation path identified for this role / ESCALATION PATHS: G-##, G-##]
```

---

*(Repeat five-vector table + ESCALATION ROLL-UP for each Write-capable role.)*

---

## PHASE 3 GATE

| Check | Answer |
|-------|--------|
| Every Write-capable role has a five-vector table | YES / NO |
| Every NOT POSSIBLE verdict uses the No-Finding Declaration format naming Checked, Confirmed, and Conclusion | YES / NO |
| Every POSSIBLE verdict logs a G-## | YES / NO |
| Every Write-capable role has an ESCALATION ROLL-UP with all fields populated | YES / NO |

**PHASE 3 COMPLETE: [YES / NO]**

---

## PHASE 4 -- REMEDIATION AND DEFENSE-IN-DEPTH

**4a -- Gap remediation:**

For each G-## in the Security Gap Log:
`[G-##]: Change [element] on [entity/field/role] from [current state] to [target state] in [solution location]. After fix: [behavioral change for the affected role].`

Every G-## in the log must have a 4a entry.

**4b -- Defense-in-depth assessment:**

| Entity | Security Role: Independent? | FLS: Independent? | Record Scope: Independent? | Single Point of Failure? |
|--------|----------------------------|-------------------|---------------------------|--------------------------|

**4c -- Stock role least-privilege:**

For Customer Service Representative and any other stock role present:
- Baseline privileges relevant to {{topic}}
- Whether custom configuration strengthened or weakened the baseline
- Least-privilege verdict: SATISFIED or EXCESS -- [specific privilege to reduce]

---

## OUTPUT REQUIREMENTS

- No-Finding Declaration format (Checked / Confirmed / Conclusion) is required for every absence throughout -- vector verdicts, sharing rule clean findings, gap-free entities, no-team-dependency confirmations
- Bare negatives ("none found", "NOT POSSIBLE", "NONE", "no escalation") without the three-field declaration do not satisfy the evidential standard
- ENTITY CLOSURE blocks appear after every entity section regardless of gap state
- Every G-## in the Security Gap Log has a 4a remediation entry

---

## V-04 -- Combined: Structural Column Isolation (C-21) + Self-Contained Roll-Up (C-24)

**Axis:** Combined output format (the escalation vector table carries a `Structural Basis` column that holds exclusively a single structural fact per NOT POSSIBLE row -- no verdict language, no evidence prose, no conditionals may share this column; the ESCALATION ROLL-UP's `Mechanisms cited` field restates each closing mechanism inline by vector name, not by reference to the table above -- C-21 + C-24)
**Hypothesis:** Round 5 V-04 placed the closing mechanism in a fourth column. C-21 tightens this: the column must be exclusively for the structural fact -- no verdict text, no "if NOT POSSIBLE" instruction prose, no conditional language. When the fourth column holds only one structural fact per NOT POSSIBLE row, a blank cell is a visible format error detectable without reading the verdict cell. C-24 tightens the roll-up: the Mechanisms cited field in Round 5 V-04 used "list mechanism names per NOT POSSIBLE verdict -- see table above", which delegates evidential content to the table. C-24 requires the roll-up to restate each mechanism inline by vector name so the roll-up is auditable without returning to the table. The two structures address independent failure modes and do not overlap.

---

You are running a permissions trace signal for: {{topic}}

---

**SECURITY GAP LOG -- add rows progressively. Assign G-## identifiers at discovery.**

| G-## | Entity | Field / Operation | Role(s) | Gap Type | Risk |
|------|--------|-------------------|---------|----------|------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH
Risk: CRITICAL / HIGH / MEDIUM

Assign the next sequential identifier (G-01, G-02, ...) the moment a gap is identified. Do not defer.

---

## PHASE 1 -- INVENTORY

**1a -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason |
|--------|-----------------|-------------|--------|

Sensitivity: High (PII, Financial, Credential, Health) / Medium (Internal-only, cross-BU risk) / Low (lookup, reference, config)

**1b -- Role catalog:**

| Role | Type (Stock / Custom) | Write-Capable? | Persona |
|------|-----------------------|----------------|---------|

Write-Capable = YES for any role holding Write, Delete, or Assign on any entity.
Stock roles to confirm: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1c -- Analysis order:**

State: "I will trace entities in this order: [list, highest to lowest sensitivity]. First gap ID to assign: G-01."

---

## PHASE 1 GATE

| Check | Answer |
|-------|--------|
| All entities that {{topic}} touches are in the 1a table | YES / NO |
| All roles with any privilege are in the 1b catalog | YES / NO |
| Write-Capable flag is set for every role holding W/D/A | YES / NO |
| Analysis order declared | YES / NO |

**PHASE 1 COMPLETE: [YES / NO -- resolve before continuing]**

---

## PHASE 2 -- PER-ENTITY TRACE

Complete all steps for one entity, then write the ENTITY CLOSURE block before advancing to the next entity.

---

### Entity: [name] (Sensitivity: [rating])

**2a -- Operation-role matrix:**

| Role | Create | Read | Write | Delete | Assign | Record Scope |
|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Parent-Child BU / Team / User / Sharing-[rule name]
Every role from 1b with any privilege on this entity must appear.

**2b -- Field-level security:**

| Field | Sensitivity | FLS Profile | Read: Allowed Roles | Write: Allowed Roles | Denied Roles |
|-------|-------------|-------------|---------------------|----------------------|--------------|

Rules:
- Every field with Sensitivity != Not-Sensitive must have a row
- FLS Profile = NONE for a sensitive field: assign G-## now
- Denied Roles must be populated explicitly

**2c -- Sharing rule audit:**

| Rule Name | Trigger | Access Granted | Recipient | Verdict: Expected / Conflict-[G-##] |
|-----------|---------|----------------|-----------|-------------------------------------|

Per-role sharing rule statements (required for every role in 2a, regardless of outcome):
"[Role] on [Entity]: sharing rules [expand access -- [rule name], see G-##] OR [confirmed do not expand -- basis: [evidence]]."

**2d -- Team membership dependency:**

For any role whose access depends on team membership: "Users in [Role] not in [Team] cannot access [record type] because [OWD+scope]. Team controlled by [mechanism]. Self-addition [possible / not possible]: [reason]. [If possible and unintended: assign G-##.]"

If no team dependency: "Confirmed: [Entity] access requires no team membership for any role. Checked: [what was reviewed]."

**2e -- Entity-level escalation check:**

For each role in 2a with W, D, or A: check for escalation paths.

- Found path: assign G-## (ESCALATION-PATH). Chain: `[Role] -> [action on [Entity]] -> [elevated access reached]`
- No path: "Checked [Role]: [specific operations audited]. No escalation via [mechanisms checked] because [specific reason per mechanism]."

---

### ENTITY CLOSURE: [Entity Name]

```
Operations reviewed:       [List each operation (C/R/W/D/A) audited per role]
Sensitive fields confirmed: [List each sensitive field reviewed]
Gaps logged this entity:   [G-## list / NONE]
Sharing rule verdicts:     [N of N roles received explicit sharing rule statements: YES]
Escalation checked:        [Roles with W/D/A that received an explicit escalation check: list]
Status:                    CLOSED
```

---

*(Repeat Phase 2 section + ENTITY CLOSURE for each entity.)*

---

## PHASE 2 GATE

| Check | Answer |
|-------|--------|
| Every entity in the 1a catalog has a Phase 2 section | YES / NO |
| Every entity has an ENTITY CLOSURE block | YES / NO |
| Every gap-containing entity names its gaps by G-## | YES / NO |
| Every gap-free entity states NONE explicitly | YES / NO |
| Every role received an explicit sharing rule statement for every entity | YES / NO |

**PHASE 2 COMPLETE: [YES / NO]**

---

## PHASE 3 -- ESCALATION VECTOR ANALYSIS (organized by Write-capable role)

For each role marked Write-Capable = YES in Phase 1b, complete the five-vector table and ESCALATION ROLL-UP.

**Structural Basis column rules (enforced before Phase 3 Gate):**
1. The `Structural Basis` column holds exactly one value per row: either a single structural fact sentence (for NOT POSSIBLE rows) or the literal text `N/A -- G-##` (for POSSIBLE rows).
2. No verdict language may appear in the Structural Basis column. No "if NOT POSSIBLE" conditionals. No evidence prose that belongs in the Evidence column.
3. A NOT POSSIBLE row with a blank or generic Structural Basis cell (e.g., "not applicable", "no path found") is a format error -- the verdict is unverifiable.
4. The Structural Basis column is NOT a restatement of the Evidence column. It names the specific configuration state confirmed absent or the platform constraint that closes the vector -- one structural fact, stated once, in this column only.

---

### Escalation Vector Audit: [Role Name]

**Write access held by this role:**

For each entity where this role holds W, D, or A: `[Entity]: [operations] at [record scope]`

**Five-vector table:**

| Vector | Evidence | Verdict | Structural Basis |
|--------|----------|---------|------------------|
| Sharing rule creation | [State the privilege checked and configuration reviewed] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: one structural fact sentence -- e.g., "No Share privilege on any entity in role definition; no admin delegation grants sharing rule creation to this role"] [POSSIBLE: N/A -- G-##] |
| Team self-injection | [State the team types checked and membership privilege reviewed] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: one structural fact sentence -- e.g., "Owner team membership requires explicit System Admin assignment; access teams allow self-addition but grant access-only scope, not owner scope"] [POSSIBLE: N/A -- G-##] |
| Field-value escalation | [State the fields reviewed and FLS profiles checked] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: one structural fact sentence -- e.g., "FLS Profile 'Service Rep - Restricted' denies write on SystemUser.BusinessUnit; no custom field in the entity set maps to security role or BU assignment"] [POSSIBLE: N/A -- G-##] |
| Role hierarchy traversal | [State whether hierarchy is enabled and the ancestor roles reviewed] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: one structural fact sentence -- e.g., "Role hierarchy enabled for Read; all ancestors scoped BU-only; no ancestor holds Org-scope on any entity in the trace"] [POSSIBLE: N/A -- G-##] |
| Record ownership transfer | [State whether Assign is held and the OWD behavior reviewed] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: one structural fact sentence -- e.g., "Assign not held; OWD Private -- transferred records leave this role's User scope; no sharing rule re-grants post-transfer access"] [POSSIBLE: N/A -- G-##] |

**Column integrity check (complete before writing ESCALATION ROLL-UP):**

- Every NOT POSSIBLE row has a Structural Basis cell containing one structural fact: YES / NO
- No Structural Basis cell contains verdict language or evidence prose: YES / NO
- Every POSSIBLE row has Structural Basis = `N/A -- G-##`: YES / NO

---

### ESCALATION ROLL-UP: [Role Name]

```
Vectors assessed:      5 (sharing rule creation, team self-injection, field-value escalation, role hierarchy traversal, record ownership transfer)
POSSIBLE count:        [count / NONE]
NOT POSSIBLE count:    [count]
Mechanisms cited (restated inline -- not by reference to the table above):
  - Sharing rule creation:    [restate the structural fact from the Structural Basis cell, or "POSSIBLE -- G-##"]
  - Team self-injection:      [restate the structural fact from the Structural Basis cell, or "POSSIBLE -- G-##"]
  - Field-value escalation:   [restate the structural fact from the Structural Basis cell, or "POSSIBLE -- G-##"]
  - Role hierarchy traversal: [restate the structural fact from the Structural Basis cell, or "POSSIBLE -- G-##"]
  - Record ownership transfer:[restate the structural fact from the Structural Basis cell, or "POSSIBLE -- G-##"]
Composite verdict:     [no escalation path identified for this role / ESCALATION PATHS: G-##, G-##]
```

Roll-up rules:
- The `Mechanisms cited` field names every vector and restates its structural fact inline. Writing "see table above", "mechanisms cited in Phase 3", or any back-reference is a format violation -- the roll-up must be auditable independently of the table.
- A roll-up with any vector line blank or referencing the table does not pass the Phase 3 Gate check.

---

*(Repeat five-vector table + ESCALATION ROLL-UP for each Write-capable role.)*

---

## PHASE 3 GATE

| Check | Answer |
|-------|--------|
| Every Write-capable role has a five-vector table | YES / NO |
| Every NOT POSSIBLE row has a non-blank Structural Basis cell containing one structural fact | YES / NO |
| No Structural Basis cell contains verdict language or evidence prose | YES / NO |
| Every POSSIBLE row has Structural Basis = N/A -- G-## | YES / NO |
| Every Write-capable role has an ESCALATION ROLL-UP | YES / NO |
| Every roll-up Mechanisms cited entry restates its structural fact inline -- no back-references | YES / NO |

**PHASE 3 COMPLETE: [YES / NO]**

---

## PHASE 4 -- REMEDIATION AND DEFENSE-IN-DEPTH

**4a -- Gap remediation:**

For each G-## in the Security Gap Log:
`[G-##]: Change [element] on [entity/field/role] from [current state] to [target state] in [solution location]. After fix: [behavioral change for the affected role].`

Every G-## in the log must have a 4a entry. Cite by G-## identifier.

**4b -- Defense-in-depth assessment:**

| Entity | Security Role: Independent? | FLS: Independent? | Record Scope: Independent? | Single Point of Failure? |
|--------|----------------------------|-------------------|---------------------------|--------------------------|

**4c -- Stock role least-privilege:**

For Customer Service Representative and any other stock role present:
- Baseline privileges relevant to {{topic}}
- Whether custom configuration strengthened or weakened the baseline
- Least-privilege verdict: SATISFIED or EXCESS -- [specific privilege to reduce]

---

## OUTPUT REQUIREMENTS

- `Structural Basis` column holds only structural facts -- no verdict language, no evidence prose, no conditionals
- A blank Structural Basis cell on a NOT POSSIBLE row is a format error
- ESCALATION ROLL-UP Mechanisms cited restates each structural fact inline; no back-references to the table
- ENTITY CLOSURE blocks appear after every entity section regardless of gap state
- Every G-## in the Security Gap Log has a 4a remediation entry

---

## V-05 -- Combined: Pre-Declaration (C-20) + Inertia Framing (C-22) + Symmetric Evidence (C-23) + Structural Column Isolation (C-21) + Self-Contained Roll-Up (C-24)

**Axis:** Combined (all five new criteria stacked into one prompt: COMMITMENT DECLARATION per role before vectors, design assumption mini-blocks per vector, No-Finding Declaration format for every absence, exclusive Structural Basis column with no co-mingled prose, and self-contained roll-up with mechanisms restated inline -- C-20 + C-22 + C-23 + C-21 + C-24)
**Hypothesis:** Each of the five new criteria addresses an independent structural gap in escalation analysis: pre-commitment (C-20) prevents post-hoc verdict anchoring; inertia framing (C-22) turns verdicts into assumption confirmations; symmetric evidence (C-23) prevents evidential asymmetry between findings and non-findings; column isolation (C-21) makes absence structurally detectable; self-contained roll-up (C-24) makes the summary independently auditable. These five requirements address different layers of verifiability -- commitment timing, verdict framing, evidential standard, format structure, and summary completeness -- and do not overlap. A prompt that enforces all five creates a trace where every NOT POSSIBLE verdict is: committed to in advance (C-20), framed as assumption confirmation (C-22), declared with full evidence (C-23), cited in an isolated structural cell (C-21), and restated in a self-contained summary (C-24).

---

You are running a permissions trace signal for: {{topic}}

---

**SECURITY GAP LOG -- add rows progressively. Assign G-## identifiers at discovery.**

| G-## | Entity | Field / Operation | Role(s) | Gap Type | Risk |
|------|--------|-------------------|---------|----------|------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH
Risk: CRITICAL / HIGH / MEDIUM

Assign the next sequential identifier (G-01, G-02, ...) the moment a gap is identified. Do not defer.

---

**No-Finding Declaration format (required for every absence at any level):**

```
NO FINDING -- [label]
Checked:     [what was reviewed]
Confirmed:   [what configuration state was confirmed absent]
Conclusion:  [path or gap closed because: specific structural fact]
```

Bare negatives ("NOT POSSIBLE", "none found", "NONE", "no gaps") without this three-field format do not satisfy the evidential standard anywhere in the output.

---

## PHASE 1 -- INVENTORY

**1a -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason |
|--------|-----------------|-------------|--------|

Sensitivity: High (PII, Financial, Credential, Health) / Medium (Internal-only, cross-BU risk) / Low (lookup, reference, config)

**1b -- Role catalog:**

| Role | Type (Stock / Custom) | Write-Capable? | Persona |
|------|-----------------------|----------------|---------|

Write-Capable = YES for any role holding Write, Delete, or Assign on any entity.
Stock roles to confirm: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1c -- Analysis order:**

State: "I will trace entities in this order: [list, highest to lowest sensitivity]. First gap ID to assign: G-01."

---

## PHASE 1 GATE

| Check | Answer |
|-------|--------|
| All entities that {{topic}} touches are in the 1a table | YES / NO |
| All roles with any privilege are in the 1b catalog | YES / NO |
| Write-Capable flag is set for every role holding W/D/A | YES / NO |
| Analysis order declared | YES / NO |

**PHASE 1 COMPLETE: [YES / NO -- resolve before continuing]**

---

## PHASE 2 -- PER-ENTITY TRACE

Complete all steps for one entity, then write the ENTITY CLOSURE block before advancing to the next entity.

---

### Entity: [name] (Sensitivity: [rating])

**2a -- Operation-role matrix:**

| Role | Create | Read | Write | Delete | Assign | Record Scope |
|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Parent-Child BU / Team / User / Sharing-[rule name]
Every role from 1b with any privilege on this entity must appear.

**2b -- Field-level security:**

| Field | Sensitivity | FLS Profile | Read: Allowed Roles | Write: Allowed Roles | Denied Roles |
|-------|-------------|-------------|---------------------|----------------------|--------------|

Rules:
- Every field with Sensitivity != Not-Sensitive must have a row
- FLS Profile = NONE for a sensitive field: assign G-## now
- Denied Roles must be populated explicitly
- When a sensitive field is correctly protected: use No-Finding Declaration format inline

**2c -- Sharing rule audit:**

| Rule Name | Trigger | Access Granted | Recipient | Verdict: Expected / Conflict-[G-##] |
|-----------|---------|----------------|-----------|-------------------------------------|

Per-role sharing rule declarations (required for every role in 2a, regardless of outcome):

For expansion: "[Role] on [Entity]: sharing rules expand access -- [rule name], see G-##."

For no expansion, use No-Finding Declaration format:
```
NO FINDING -- Sharing rules for [Role] on [Entity]
Checked:     All criteria-based sharing rules for [Entity] with [Role] as recipient; all manual sharing grants
Confirmed:   No criteria-based or manual sharing rule expands [Role] access beyond OWD + security role scope
Conclusion:  [Role] access on [Entity] bounded by [OWD level] + security role privilege only
```

**2d -- Team membership dependency:**

For any role with team-dependent access: "Users in [Role] not in [Team] cannot access [record type] because [OWD+scope]. Team controlled by [mechanism]. Self-addition [possible / not possible]: [reason]. [If possible and unintended: assign G-##.]"

If no team dependency, use No-Finding Declaration format:
```
NO FINDING -- Team dependency for [Entity]
Checked:     OWD setting; whether any role holds access only via team membership; team-owned record visibility requirements
Confirmed:   No role in this entity section requires team membership to access [Entity] records
Conclusion:  [Entity] access governed by security role + OWD scope for all roles; no team dependency gap
```

**2e -- Entity-level escalation check:**

For each role in 2a with W, D, or A: check for escalation paths.

- Found path: assign G-## (ESCALATION-PATH). Chain: `[Role] -> [action on [Entity]] -> [elevated access reached]`
- No path: use No-Finding Declaration format per role:
```
NO FINDING -- Escalation from [Role] on [Entity]
Checked:     Assign privilege; record ownership transfer effect; sharing rule creation via Write; field paths to role/BU change
Confirmed:   No operation available to [Role] on [Entity] elevates access scope
Conclusion:  [Role] cannot escalate from [Entity] because [structural reason per mechanism]
```

---

### ENTITY CLOSURE: [Entity Name]

```
Operations reviewed:       [List each operation (C/R/W/D/A) audited per role]
Sensitive fields confirmed: [List each sensitive field reviewed]
Gaps logged this entity:   [G-## list / NONE -- if NONE: "confirmed by reviewing [what was checked and found absent]"]
Sharing rule verdicts:     [N of N roles received explicit sharing rule declarations: YES]
Escalation checked:        [Roles with W/D/A that received explicit escalation declarations: list]
Status:                    CLOSED
```

---

*(Repeat Phase 2 section + ENTITY CLOSURE for each entity.)*

---

## PHASE 2 GATE

| Check | Answer |
|-------|--------|
| Every entity in the 1a catalog has a Phase 2 section | YES / NO |
| Every entity has an ENTITY CLOSURE block | YES / NO |
| Every gap-containing entity names its gaps by G-## | YES / NO |
| Every gap-free entity states NONE with a confirmation of what was reviewed | YES / NO |
| Every role received a sharing rule declaration (finding or No-Finding) for every entity | YES / NO |
| Every W/D/A role received an escalation declaration (finding or No-Finding) for every entity | YES / NO |

**PHASE 2 COMPLETE: [YES / NO]**

---

## PHASE 3 -- ESCALATION VECTOR ANALYSIS (organized by Write-capable role)

For each role marked Write-Capable = YES in Phase 1b, complete the following sequence in order: (1) COMMITMENT DECLARATION, (2) five vector mini-blocks, (3) ESCALATION ROLL-UP. Do not begin the vector mini-blocks until the COMMITMENT DECLARATION is written.

---

### COMMITMENT DECLARATION: [Role Name]

Before analyzing escalation vectors for [Role Name], I declare the structural assumptions under which NOT POSSIBLE verdicts will be issued. Each vector mini-block below will open with one of these assumptions restated as the inertia anchor. Every NOT POSSIBLE verdict must trace to its named assumption here.

| Vector | Pre-Analysis Structural Assumption |
|--------|-------------------------------------|
| Sharing rule creation | [Role Name] is expected to lack the privilege to create or modify sharing rules because [design intent]. This assumption governs the NOT POSSIBLE verdict in Vector 1 below. |
| Team self-injection | [Role Name] is expected to be unable to add itself to higher-scope owner teams because [design intent]. This assumption governs the NOT POSSIBLE verdict in Vector 2 below. |
| Field-value escalation | No field writable by [Role Name] changes role assignment, BU membership, or security profile because [design intent]. This assumption governs the NOT POSSIBLE verdict in Vector 3 below. |
| Role hierarchy traversal | Role hierarchy does not elevate [Role Name] beyond its direct assignment because [design intent]. This assumption governs the NOT POSSIBLE verdict in Vector 4 below. |
| Record ownership transfer | Assigning records does not expand [Role Name]'s own visibility because [design intent]. This assumption governs the NOT POSSIBLE verdict in Vector 5 below. |

Commitment: each vector mini-block confirms or refutes the stated assumption. A NOT POSSIBLE verdict without a corresponding prior assumption in this table is a contract violation.

---

### Escalation Vector Audit: [Role Name]

**Write access held by this role:**

For each entity where this role holds W, D, or A: `[Entity]: [operations] at [record scope]`

---

#### Vector 1: Sharing rule creation

> **Inertia Frame (from COMMITMENT DECLARATION):** [Restate the Assumption for this vector exactly as declared above.]

| Evidence | Verdict | Structural Basis |
|----------|---------|------------------|
| [State the specific privilege checked and the configuration reviewed] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: one structural fact sentence only -- no verdict language, no evidence prose] [POSSIBLE: N/A -- G-##] |

**Verdict statement:** `NOT POSSIBLE -- Assumption Confirmed: [structural fact]` OR `POSSIBLE -- Assumption Refuted: G-##`

---

#### Vector 2: Team self-injection

> **Inertia Frame (from COMMITMENT DECLARATION):** [Restate the Assumption for this vector exactly as declared above.]

| Evidence | Verdict | Structural Basis |
|----------|---------|------------------|
| [State the team types and membership privileges checked] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: one structural fact sentence only] [POSSIBLE: N/A -- G-##] |

**Verdict statement:** `NOT POSSIBLE -- Assumption Confirmed: [structural fact]` OR `POSSIBLE -- Assumption Refuted: G-##`

---

#### Vector 3: Field-value escalation

> **Inertia Frame (from COMMITMENT DECLARATION):** [Restate the Assumption for this vector exactly as declared above.]

| Evidence | Verdict | Structural Basis |
|----------|---------|------------------|
| [State the fields and FLS profiles reviewed] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: one structural fact sentence only] [POSSIBLE: N/A -- G-##] |

**Verdict statement:** `NOT POSSIBLE -- Assumption Confirmed: [structural fact]` OR `POSSIBLE -- Assumption Refuted: G-##`

---

#### Vector 4: Role hierarchy traversal

> **Inertia Frame (from COMMITMENT DECLARATION):** [Restate the Assumption for this vector exactly as declared above.]

| Evidence | Verdict | Structural Basis |
|----------|---------|------------------|
| [State whether hierarchy is enabled and the ancestor roles reviewed] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: one structural fact sentence only] [POSSIBLE: N/A -- G-##] |

**Verdict statement:** `NOT POSSIBLE -- Assumption Confirmed: [structural fact]` OR `POSSIBLE -- Assumption Refuted: G-##`

---

#### Vector 5: Record ownership transfer

> **Inertia Frame (from COMMITMENT DECLARATION):** [Restate the Assumption for this vector exactly as declared above.]

| Evidence | Verdict | Structural Basis |
|----------|---------|------------------|
| [State whether Assign is held and OWD behavior reviewed] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: one structural fact sentence only] [POSSIBLE: N/A -- G-##] |

**Verdict statement:** `NOT POSSIBLE -- Assumption Confirmed: [structural fact]` OR `POSSIBLE -- Assumption Refuted: G-##`

---

### ESCALATION ROLL-UP: [Role Name]

```
Vectors assessed:      5 (sharing rule creation, team self-injection, field-value escalation, role hierarchy traversal, record ownership transfer)
POSSIBLE count:        [count / NONE]
NOT POSSIBLE count:    [count]
Declaration honored:   [count / 5 -- number of NOT POSSIBLE verdicts that confirm a prior declared assumption]
Mechanisms cited (restated inline -- not by reference to vectors above):
  - Sharing rule creation:    [restate the Structural Basis cell from Vector 1, or "POSSIBLE -- G-##"]
  - Team self-injection:      [restate the Structural Basis cell from Vector 2, or "POSSIBLE -- G-##"]
  - Field-value escalation:   [restate the Structural Basis cell from Vector 3, or "POSSIBLE -- G-##"]
  - Role hierarchy traversal: [restate the Structural Basis cell from Vector 4, or "POSSIBLE -- G-##"]
  - Record ownership transfer:[restate the Structural Basis cell from Vector 5, or "POSSIBLE -- G-##"]
Composite verdict:     [no escalation path identified for this role / ESCALATION PATHS: G-##, G-##]
```

Roll-up rules:
- Mechanisms cited restates each structural fact inline per vector name. "See vectors above", "mechanisms cited in analysis", or any back-reference is a format violation.
- Declaration honored must equal NOT POSSIBLE count. Any mismatch means a NOT POSSIBLE verdict was issued without a prior declared assumption -- identify which vector and add a declaration before continuing.

---

*(Repeat COMMITMENT DECLARATION + five vector mini-blocks + ESCALATION ROLL-UP for each Write-capable role.)*

---

## PHASE 3 GATE

| Check | Answer |
|-------|--------|
| Every Write-capable role has a COMMITMENT DECLARATION before its vectors | YES / NO |
| Every vector mini-block restates the inertia frame from the COMMITMENT DECLARATION | YES / NO |
| Every NOT POSSIBLE verdict says "Assumption Confirmed: [structural fact]" | YES / NO |
| Every NOT POSSIBLE verdict traces to a named assumption in the COMMITMENT DECLARATION above it | YES / NO |
| Every Structural Basis cell holds only one structural fact -- no verdict language or evidence prose | YES / NO |
| Every POSSIBLE verdict logs G-## | YES / NO |
| Every Write-capable role has an ESCALATION ROLL-UP | YES / NO |
| Every Mechanisms cited entry restates its structural fact inline -- no back-references | YES / NO |
| Declaration honored count equals NOT POSSIBLE count in every roll-up | YES / NO |

**PHASE 3 COMPLETE: [YES / NO]**

---

## PHASE 4 -- REMEDIATION AND DEFENSE-IN-DEPTH

**4a -- Gap remediation:**

For each G-## in the Security Gap Log:
`[G-##]: Change [element] on [entity/field/role] from [current state] to [target state] in [solution location]. After fix: [behavioral change for the affected role].`

Every G-## in the log must have a 4a entry. Cite by G-## identifier. Generic advice does not qualify.

**4b -- Defense-in-depth assessment:**

| Entity | Security Role: Independent? | FLS: Independent? | Record Scope: Independent? | Single Point of Failure? |
|--------|----------------------------|-------------------|---------------------------|--------------------------|

Independent = YES if this layer enforces access even when the other two layers are misconfigured. Single POF = YES: add G-## if not already logged.

**4c -- Stock role least-privilege:**

For Customer Service Representative and any other stock role present:
- Baseline privileges relevant to {{topic}}
- Whether custom configuration strengthened or weakened the baseline
- Least-privilege verdict: SATISFIED or EXCESS -- [specific privilege to reduce]

---

## OUTPUT REQUIREMENTS

- COMMITMENT DECLARATION required before every Write-capable role's vector analysis (C-20)
- Every vector mini-block opens with inertia frame restated from COMMITMENT DECLARATION; verdict says "Assumption Confirmed/Refuted" (C-22)
- No-Finding Declaration format (Checked / Confirmed / Conclusion) required for every absence at every level (C-23)
- Structural Basis column holds only one structural fact per NOT POSSIBLE row -- no co-mingled prose (C-21)
- Mechanisms cited in ESCALATION ROLL-UP restates each structural fact inline per vector; no back-references (C-24)
- ENTITY CLOSURE blocks appear after every entity section regardless of gap state
- Every G-## in the Security Gap Log has a 4a remediation entry

---

## Variation Summary

| Variation | Primary Axis | New Criteria Targeted | Key Structural Addition |
|-----------|-------------|----------------------|------------------------|
| V-01 | Lifecycle emphasis | C-20 | COMMITMENT DECLARATION block before each role's vector table; Phase 3 Gate checks NOT POSSIBLE trace to prior declaration |
| V-02 | Inertia framing | C-22 | Five vector mini-blocks (replaces monolithic table); each opens with Design Assumption; verdict says "Assumption Confirmed/Refuted" |
| V-03 | Phrasing register | C-23 | No-Finding Declaration format (Checked/Confirmed/Conclusion) required for every absence throughout all phases |
| V-04 | Output format + Role sequence | C-21 + C-24 | `Structural Basis` column holds one structural fact only; ESCALATION ROLL-UP Mechanisms cited restates inline per vector |
| V-05 | Combined | C-20 + C-21 + C-22 + C-23 + C-24 | All five new criteria stacked: COMMITMENT DECLARATION + inertia mini-blocks + No-Finding declarations + isolated Structural Basis column + self-contained roll-up |
