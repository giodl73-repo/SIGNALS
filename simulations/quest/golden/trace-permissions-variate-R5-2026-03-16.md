# trace-permissions Variate -- Round 5 (Rubric v5)
**Date:** 2026-03-16
**Rubric:** v5 (C-01 through C-19)
**New criteria targeted this round:** C-18 (NOT POSSIBLE verdict closure mechanism citation), C-19 (per-role escalation roll-up assertion)
**Prior round retained:** Essential C-01--C-04, recommended C-05--C-07, aspirational C-08--C-17 are structurally enforced throughout

---

## Round 5 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format -- dedicated `Closing Mechanism` column in the vector table (C-18 single-axis) | Round 4 V-02 embedded the mechanism citation hint inside the Evidence column, making it optional text rather than a required field. Splitting the table into four columns -- Vector, Mechanism, Verdict, Closing Mechanism -- makes the closing mechanism a distinct cell that cannot share space with the verdict; a NOT POSSIBLE verdict with a blank Closing Mechanism cell is a visible format violation, not a missing phrase buried inside prose |
| V-02 | Role sequence -- mandatory ESCALATION ROLL-UP block after each role (C-19 single-axis) | Round 4 V-02's "Summary for [Role]" was a one-sentence format hint rather than a structured block. Replacing it with a named block containing declared fields -- `Vectors assessed:`, `POSSIBLE count:`, `NOT POSSIBLE count:`, `Mechanisms cited:`, `Composite verdict:` -- makes each field independently checkable; a roll-up with a blank `Composite verdict:` field is an incomplete block, not an incomplete sentence |
| V-03 | Lifecycle emphasis -- Phase 3 pre-declaration commitment (C-18 + C-19 via phase discipline) | Before tracing any vectors for a role, the output declares the exact N vectors it will check and commits to: (a) naming a closing mechanism for every NOT POSSIBLE verdict it will produce, and (b) writing a roll-up block at the end. Phase 3 gate verifies that every declared vector was assessed and every commitment was honored. Pre-declaration makes incompleteness detectable at two points: the declaration and the gate |
| V-04 | Combined: output format (dedicated closing mechanism column, C-18) + role sequence (mandatory roll-up block, C-19) | Direct stack of V-01 and V-02 mechanics: the vector table has four columns forcing mechanism citation into its own cell; the role section ends with a structured roll-up block with required fields. Both structures are independent and address distinct failure modes: V-01 prevents bare NOT POSSIBLE cells; V-02 prevents missing role-level synthesis |
| V-05 | Combined: phrasing register (audit evidence standard for NOT POSSIBLE) + inertia framing (hypothesis-per-vector + design assumption tested) | Audit evidence standard: a NOT POSSIBLE verdict is written as a formal "No Finding" declaration that must cite the confirming evidence and the configuration state verified absent. Inertia framing: each vector opens with the design assumption being tested (e.g., "Sharing rule creation: the security model assumes this role cannot create sharing rules; confirm by checking [privilege]"), making the NOT POSSIBLE closure a confirmation or refutation of a stated assumption rather than a bare verdict |

---

## V-01 -- Output Format: Dedicated Closing Mechanism Column

**Axis:** Output format (the escalation vector table carries a dedicated `Closing Mechanism` column; NOT POSSIBLE verdicts must populate this cell; POSSIBLE verdicts leave it blank and populate the Gap Log instead -- C-18 single-axis)
**Hypothesis:** Round 4 V-02 placed the mechanism citation as a parenthetical hint inside the Evidence column: "if NOT POSSIBLE, name the mechanism that closes this vector." A hint inside a single shared column can be satisfied by adding a phrase to existing Evidence text, which makes omission hard to detect. Splitting into four columns -- Vector, Mechanism Description, Verdict, Closing Mechanism -- creates a cell that exists only for NOT POSSIBLE verdicts and has no valid non-blank state for those verdicts. A blank Closing Mechanism cell in a NOT POSSIBLE row is a visible format error. The model cannot satisfy the form of C-18 without also satisfying its substance.

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
- FLS Profile = NONE for a sensitive field: add to Security Gap Log now (MISSING-FLS). CRITICAL for PII/Credential/Health; HIGH for Financial/Internal-Audit. Assign G-## now.
- Denied Roles must be populated explicitly -- "none denied" is valid only when confirmed

**2c -- Sharing rule audit:**

| Rule Name | Trigger | Access Granted | Recipient | Verdict: Expected / Conflict-[G-##] |
|-----------|---------|----------------|-----------|-------------------------------------|

For each conflict: assign G-## now. Log to Security Gap Log.

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

For each role marked Write-Capable = YES in Phase 1b, complete the full vector audit before moving to the next role.

**Instruction for the vector table:** The table has four columns. The `Closing Mechanism` column applies only to NOT POSSIBLE verdicts -- it names the specific configuration state confirmed absent, the platform boundary enforced, or the mechanism confirmed non-applicable. For POSSIBLE verdicts, `Closing Mechanism` is N/A; those rows must have a G-## in the Security Gap Log. A NOT POSSIBLE verdict with a blank `Closing Mechanism` cell is a format error -- the verdict is unverifiable without it.

---

### Escalation Vector Audit: [Role Name]

**Write access held by this role:**

For each entity where this role holds W, D, or A: `[Entity]: [operations] at [record scope]`

**Five-vector table:**

| Vector | Mechanism Description | Verdict | Closing Mechanism (NOT POSSIBLE only) |
|--------|----------------------|---------|---------------------------------------|
| Sharing rule creation | Can this role create or modify sharing rules to expand its own record access? | POSSIBLE / NOT POSSIBLE | [If NOT POSSIBLE: name the specific privilege absent, configuration that blocks this, or platform constraint that closes the vector. If POSSIBLE: N/A -- log G-##] |
| Team self-injection | Can this role add itself to a team with higher-privilege record scope? | POSSIBLE / NOT POSSIBLE | [If NOT POSSIBLE: name the specific team management privilege absent, the team type (e.g., owner vs. access team), or the configuration that prevents self-addition. If POSSIBLE: N/A -- log G-##] |
| Field-value escalation | Can this role write a field whose value changes role assignment, BU membership, or security profile? | POSSIBLE / NOT POSSIBLE | [If NOT POSSIBLE: name the specific fields audited, the FLS profile denying write, or the absence of such a field in the entity set. If POSSIBLE: N/A -- log G-##] |
| Role hierarchy traversal | Does the role hierarchy chain this role to a parent with broader access? | POSSIBLE / NOT POSSIBLE | [If NOT POSSIBLE: state whether role hierarchy is enabled for this environment; name the ancestor roles checked and their access grants; confirm no parent broadens access. If POSSIBLE: N/A -- log G-##] |
| Record ownership transfer | Can this role assign records to an owner in a different scope, triggering broader visibility? | POSSIBLE / NOT POSSIBLE | [If NOT POSSIBLE: state whether Assign is held; name the OWD behavior under transferred ownership; confirm cross-BU or org-level scope expansion does not apply. If POSSIBLE: N/A -- log G-##] |

**Column rules:**
- `Closing Mechanism` is required for every NOT POSSIBLE verdict. A NOT POSSIBLE row with a blank or generic `Closing Mechanism` (e.g., "not applicable", "no escalation") is a format error.
- `Closing Mechanism` for a POSSIBLE verdict must read exactly: `N/A -- G-##` citing the gap log entry.
- `Verdict` must be one of the two listed values. No other values.

---

*(Repeat escalation vector audit for each Write-capable role.)*

---

## PHASE 3 GATE

| Check | Answer |
|-------|--------|
| Every Write-capable role has a five-vector table | YES / NO |
| Every row in every table has a Verdict | YES / NO |
| Every NOT POSSIBLE row has a non-blank Closing Mechanism naming a structural basis | YES / NO |
| Every POSSIBLE row has a G-## in the Security Gap Log | YES / NO |

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

- Gap log rows added at discovery time; G-## assigned at the moment the gap is found
- Every NOT POSSIBLE vector verdict has a non-blank `Closing Mechanism` cell naming a structural basis
- ENTITY CLOSURE blocks appear after every entity section -- including entities where gaps were found
- Closure blocks on gap-containing entities name the gaps by G-## in the `Gaps logged` field
- Closure blocks on gap-free entities state NONE explicitly in the `Gaps logged` field
- Every G-## in the Security Gap Log has a 4a remediation entry citing the same identifier

---

## V-02 -- Role Sequence: Mandatory Escalation Roll-Up Block

**Axis:** Role sequence (after each Write-capable role's vector analysis, a structured ESCALATION ROLL-UP block is required with declared fields -- `Vectors assessed:`, `POSSIBLE count:`, `NOT POSSIBLE count:`, `Mechanisms cited:`, `Composite verdict:` -- C-19 single-axis)
**Hypothesis:** Round 4 V-02's "Summary for [Role]" was one sentence, making it easy to satisfy with a short statement that does not name vector count or composite conclusion. A named block with individually required fields -- each field needing a distinct value -- cannot be completed by a single sentence. The `Vectors assessed:` field forces the count to be explicit; the `Composite verdict:` field forces a role-level conclusion to be stated; the `Mechanisms cited:` field cross-links back to the vector table. Each field is independently verifiable against the vector table above it. An incomplete block (any field blank or generic) is a visible format violation.

---

You are running a permissions trace signal for: {{topic}}

---

**SECURITY GAP LOG -- add rows progressively. Assign G-## identifiers at discovery.**

| G-## | Entity | Field / Operation | Role(s) | Gap Type | Risk |
|------|--------|-------------------|---------|----------|------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH
Risk: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 -- INVENTORY

**1a -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason |
|--------|-----------------|-------------|--------|

**1b -- Role catalog:**

| Role | Type (Stock / Custom) | Write-Capable? | Persona |
|------|-----------------------|----------------|---------|

Write-Capable = YES for roles holding Write, Delete, or Assign on any entity. These roles undergo full escalation roll-up in Phase 3.
Stock roles to confirm: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1c -- Operation-role matrix (per entity):**

For each entity in 1a:

| Entity: [name] | Role | C | R | W | D | A | Record Scope |
|----------------|------|---|---|---|---|---|--------------|

Values: YES / NO / CONDITIONAL. Record Scope: Org / BU / Parent-Child BU / Team / User / Sharing-[rule name].

**1d -- Field-level security (per entity):**

For each entity, every sensitive field:

| Entity | Field | Sensitivity | FLS Profile | Read: Allowed | Write: Allowed | Denied |
|--------|-------|-------------|-------------|--------------|----------------|--------|

FLS Profile = NONE on a sensitive field: add to Gap Log now (MISSING-FLS). CRITICAL for PII/Credential/Health; HIGH for Financial/Internal-Audit.

**1e -- Sharing rule inventory and per-role verdicts:**

For each entity: list all sharing rules. For every role on each entity, state explicitly:
"[Role] on [Entity]: [sharing rule [name] expands access -- CONFLICT, see G-##] OR [confirmed: no sharing rules expand access -- basis: [evidence]]."

No rules on an entity: "Confirmed: no sharing rules on [Entity]. Checked: [location]."

---

## PHASE 1 GATE

| Check | Answer |
|-------|--------|
| All entities in 1a | YES / NO |
| All roles in 1b with Write-Capable flag | YES / NO |
| 1c matrices complete for every entity | YES / NO |
| All sensitive fields in 1d with FLS status | YES / NO |
| Per-role sharing rule verdicts issued for all entity-role combinations | YES / NO |

**PHASE 1 COMPLETE: [YES / NO]**

---

## PHASE 2 -- ENTITY-LEVEL GAP ANALYSIS

For each entity (highest sensitivity first):

**Entity: [name]**

**2a -- Team membership gap:**

For any role with team-dependent access: "Users in [Role] not in [Team] cannot access [record type] because [OWD+scope]. Team controlled by [mechanism]. Self-addition [possible: concern -- G-## / not possible: [reason]]."
If no team dependency: "Confirmed: [Entity] access requires no team membership for any role. Checked: [what]."

**2b -- Business unit scope:**

For each BU-scoped role: `[Role] -> [BU scope] -> [OWD behavior] -> [child BU records: visible YES/NO] -> [reason]`

**2c -- Entity closure:**

```
Entity: [name] -- CLOSED
Operations reviewed:       [list each operation per role]
Sensitive fields confirmed: [list, or "none -- confirmed by reviewing [field names]"]
Gaps logged this entity:   [G-## list / NONE]
Status: CLOSED
```

*(Repeat 2a-2c for each entity.)*

---

## PHASE 2 GATE

| Check | Answer |
|-------|--------|
| Every entity has a closure block with all fields populated | YES / NO |
| Gap-containing entities name gaps by G-## in their closure block | YES / NO |
| Gap-free entities state NONE in their closure block | YES / NO |

**PHASE 2 COMPLETE: [YES / NO]**

---

## PHASE 3 -- ESCALATION VECTOR ANALYSIS (Write-capable role first)

For each role marked Write-Capable = YES in Phase 1b: complete the full vector audit and the ESCALATION ROLL-UP block before moving to the next role. The ESCALATION ROLL-UP block is mandatory for every Write-capable role. A section that ends without it is incomplete.

---

### Escalation Vector Audit: [Role Name]

**Write access held by this role:**

For each entity where this role holds W, D, or A: `[Entity]: [operations] at [record scope]`

**Five-vector table:**

| Vector | Mechanism | Verdict | Evidence / Closing Mechanism |
|--------|-----------|---------|------------------------------|
| Sharing rule creation | Can this role create or modify sharing rules to expand its own record access? | POSSIBLE / NOT POSSIBLE | [POSSIBLE: chain + G-##. NOT POSSIBLE: name the specific privilege absent or platform constraint that closes this vector] |
| Team self-injection | Can this role add itself to a team with higher-privilege record scope? | POSSIBLE / NOT POSSIBLE | [POSSIBLE: chain + G-##. NOT POSSIBLE: name the team management privilege absent, team type, or configuration blocking self-addition] |
| Field-value escalation | Can this role write a field whose value changes role assignment, BU membership, or security profile? | POSSIBLE / NOT POSSIBLE | [POSSIBLE: chain + G-##. NOT POSSIBLE: name the specific fields audited and the FLS profile or field absence that closes the vector] |
| Role hierarchy traversal | Does the role hierarchy chain this role to a parent with broader access? | POSSIBLE / NOT POSSIBLE | [POSSIBLE: chain + G-##. NOT POSSIBLE: state hierarchy enablement status; name ancestor roles checked; confirm no ancestor broadens access] |
| Record ownership transfer | Can this role assign records to an owner in a different scope for broader visibility? | POSSIBLE / NOT POSSIBLE | [POSSIBLE: chain + G-##. NOT POSSIBLE: state Assign privilege status; name OWD transfer behavior; confirm cross-BU/org scope expansion does not apply] |

---

### ESCALATION ROLL-UP: [Role Name]

```
Vectors assessed:     [integer -- must equal the number of rows in the table above]
POSSIBLE count:       [integer -- must equal POSSIBLE verdicts in table]
NOT POSSIBLE count:   [integer -- must equal NOT POSSIBLE verdicts in table]
Mechanisms cited:     [For each NOT POSSIBLE verdict: "Vector name -- closing mechanism: [one-line citation]". One entry per NOT POSSIBLE row.]
Composite verdict:    [ESCALATION CONFIRMED: G-## / CLEAN: all vectors ruled out, no escalation path from this role]
```

**Block rules:**
- `Vectors assessed` must be a non-zero integer matching the table row count.
- `POSSIBLE count` + `NOT POSSIBLE count` must equal `Vectors assessed`.
- `Mechanisms cited` must have one entry per NOT POSSIBLE verdict -- not a count, not "see table", not "evidence above". A per-verdict citation of the closing mechanism.
- `Composite verdict` must be one of the two stated forms. It cannot be blank, conditional, or a cross-reference to the table. The verdict is the conclusion; the table is the evidence.
- A block with any field blank, generic, or pointing back to the table instead of restating the fact is incomplete.

---

*(Repeat escalation vector audit + ESCALATION ROLL-UP for each Write-capable role.)*

---

## PHASE 3 GATE

| Check | Answer |
|-------|--------|
| Every Write-capable role has a five-vector table | YES / NO |
| Every row in every vector table has a verdict | YES / NO |
| Every NOT POSSIBLE verdict cites the closing mechanism in the Evidence column | YES / NO |
| Every Write-capable role has an ESCALATION ROLL-UP block | YES / NO |
| Every ESCALATION ROLL-UP block has all five fields populated with non-generic values | YES / NO |
| `Mechanisms cited` has one entry per NOT POSSIBLE verdict (not per role) | YES / NO |
| Every POSSIBLE verdict has a G-## in the Security Gap Log | YES / NO |

**PHASE 3 COMPLETE: [YES / NO]**

---

## PHASE 4 -- REMEDIATION AND DEFENSE-IN-DEPTH

**4a -- Gap remediation:**

`[G-##]: Change [element] on [entity/field/role] from [current state] to [target state] in [solution location]. After fix: [behavioral change].`

Cite by G-##. Generic advice does not qualify. Every G-## must have a 4a entry.

**4b -- Defense-in-depth assessment:**

| Entity | Security Role: Independent? | FLS: Independent? | Record Scope: Independent? | Single POF? |
|--------|----------------------------|-------------------|---------------------------|-------------|

Single POF = YES: add G-## if not already present.

**4c -- Stock role coverage:**

Customer Service Representative (and any other stock role): baseline privileges, least-privilege verdict (SATISFIED or EXCESS -- specific reduction).

---

## OUTPUT REQUIREMENTS

- Gap log rows added at discovery time
- Every Write-capable role has a five-vector table and a mandatory ESCALATION ROLL-UP block
- Every NOT POSSIBLE verdict cites the closing mechanism in the Evidence column
- ESCALATION ROLL-UP blocks have all five fields populated; `Mechanisms cited` is per-NOT-POSSIBLE-verdict, not per-role
- Entity closure blocks appear for every entity; gap-containing entities name gaps by G-##; gap-free entities state NONE
- Every G-## has a 4a remediation entry

---

## V-03 -- Lifecycle Emphasis: Phase 3 Pre-Declaration Commitment

**Axis:** Lifecycle emphasis (Phase 3 begins with a per-role Declaration of Intent that commits the output to (a) name a closing mechanism for every NOT POSSIBLE verdict and (b) produce an ESCALATION ROLL-UP block at the end; Phase 3 gate verifies that every declaration was honored -- C-18 + C-19 via phase discipline)
**Hypothesis:** Rounds 3 and 4 placed structural requirements at the point of production (the table column, the closure block template). An alternative lifecycle approach commits the output before the analysis begins, creating a checkable contract at two points: (1) the pre-declaration states the vectors and commitments; (2) the gate verifies that every declared commitment was met. Pre-declaration changes the framing -- the model is not discovering what it must do as it goes; it is executing against stated commitments. An unmet commitment (a NOT POSSIBLE verdict without a mechanism citation, a roll-up block that was promised but absent) is a contract violation detectable without reading the full vector table.

---

You are running a permissions trace signal for: {{topic}}

---

**SECURITY GAP LOG -- add rows progressively. Assign G-## identifiers at discovery.**

| G-## | Entity | Field / Operation | Role(s) | Gap Type | Risk |
|------|--------|-------------------|---------|----------|------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH
Risk: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 -- INVENTORY

**1a -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason |
|--------|-----------------|-------------|--------|

**1b -- Role catalog:**

| Role | Type (Stock / Custom) | Write-Capable? | Persona |
|------|-----------------------|----------------|---------|

Write-Capable = YES for roles holding Write, Delete, or Assign on any entity.
Stock roles to confirm: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1c -- Analysis order:**

State: "I will trace entities in this order: [list, highest to lowest sensitivity]. Write-capable roles for Phase 3 escalation analysis: [list]. First gap ID to assign: G-01."

---

## PHASE 1 GATE

| Check | Answer |
|-------|--------|
| All entities in 1a | YES / NO |
| All roles in 1b with Write-Capable flag | YES / NO |
| Analysis order declared; Write-capable roles named | YES / NO |

**PHASE 1 COMPLETE: [YES / NO]**

---

## PHASE 2 -- PER-ENTITY TRACE

### Entity: [name] (Sensitivity: [rating])

**2a -- Operation-role matrix:**

| Role | Create | Read | Write | Delete | Assign | Record Scope |
|------|--------|------|-------|--------|--------|--------------|

**2b -- Field-level security:**

| Field | Sensitivity | FLS Profile | Read: Allowed Roles | Write: Allowed Roles | Denied Roles |
|-------|-------------|-------------|---------------------|----------------------|--------------|

FLS Profile = NONE on a sensitive field: add to Gap Log now. Assign G-## now.

**2c -- Sharing rule audit:**

Per-role sharing rule statements for every role in 2a:
"[Role] on [Entity]: [expansion found -- G-##] OR [confirmed no expansion -- basis: [evidence]]."

**2d -- Team membership dependency:**

For team-dependent roles: "[Role] not in [Team]: cannot access [record] because [reason]. Self-addition [possible/not possible]: [reason]. [G-## if gap.]"
If none: "Confirmed: no team dependency on [Entity]. Checked: [what]."

**2e -- Entity-level escalation:**

For each W/D/A role: found path -> G-## (ESCALATION-PATH). No path -> "Checked [Role]: [operations]. No escalation via [mechanisms] because [reason per mechanism]."

---

### ENTITY CLOSURE: [Entity Name]

```
Operations reviewed:       [List each operation per role]
Sensitive fields confirmed: [list, or "none -- confirmed by reviewing [field names]"]
Gaps logged this entity:   [G-## list / NONE]
Sharing rule verdicts:     [N of N roles received explicit statements: YES]
Escalation checked:        [W/D/A roles that received explicit escalation check]
Status:                    CLOSED
```

*(Repeat for each entity, highest to lowest sensitivity.)*

---

## PHASE 2 GATE

| Check | Answer |
|-------|--------|
| Every entity has a complete ENTITY CLOSURE block | YES / NO |
| Gap-containing entities name gaps by G-## in CLOSURE | YES / NO |
| Gap-free entities state NONE explicitly in CLOSURE | YES / NO |
| All roles received explicit sharing rule verdicts per entity | YES / NO |

**PHASE 2 COMPLETE: [YES / NO]**

---

## PHASE 3 -- ESCALATION VECTOR ANALYSIS

Phase 3 is organized by Write-capable role. Before analyzing any vector for a role, write a pre-declaration block. After completing all vectors for a role, write the roll-up block. Both blocks are mandatory for every Write-capable role.

---

### Escalation Analysis: [Role Name]

#### PRE-DECLARATION: [Role Name]

```
Vectors I will check: [list all N vectors by name]
Number of vectors:    [integer]
Commitments:
  (a) For every NOT POSSIBLE verdict, I will cite the specific structural mechanism that closes the vector
      -- naming the configuration state confirmed absent, the platform boundary enforced,
      or the privilege confirmed absent. "Not possible" without a cited mechanism will not appear.
  (b) After all vectors, I will write an ESCALATION ROLL-UP block naming: vectors assessed count,
      POSSIBLE count, NOT POSSIBLE count, per-NOT-POSSIBLE mechanism citations, and composite verdict.
```

**Write access held by this role:**

For each entity where this role holds W, D, or A: `[Entity]: [operations] at [record scope]`

**Five-vector analysis:**

For each vector named in the pre-declaration:

**Vector: [name]**

Question: [one sentence stating what is being checked]
Evidence: [what was reviewed -- the privilege checked, the configuration inspected, the field list audited]
Verdict: POSSIBLE / NOT POSSIBLE
- If POSSIBLE: `[Role] -> [action] -> [elevated access reached]`. Assign G-## now.
- If NOT POSSIBLE: Closing mechanism: [name the specific structural fact that closes this vector -- the privilege absent, the platform constraint, the configuration state confirmed. This must be a specific, verifiable statement. "No path" or "not possible" restated is not a closing mechanism.]

*(Repeat for each declared vector.)*

---

#### ESCALATION ROLL-UP: [Role Name]

```
Vectors assessed:     [integer -- must equal count in pre-declaration]
POSSIBLE count:       [integer]
NOT POSSIBLE count:   [integer]
Mechanisms cited:
  [Vector name]: [one-line closing mechanism citation]
  [Vector name]: [one-line closing mechanism citation]
  ... (one entry per NOT POSSIBLE verdict)
Composite verdict:    [ESCALATION CONFIRMED: G-## / CLEAN: all [N] vectors ruled out for this role]
Pre-declaration honored: YES / NO -- [if NO, state which commitment was not met]
```

**Block rules:**
- `Vectors assessed` must match the pre-declaration count.
- `Mechanisms cited` must have one entry per NOT POSSIBLE verdict. Cross-referencing the vector section ("see above") does not satisfy this field -- restate the mechanism.
- `Composite verdict` must be one of the two forms. It names the count in the CLEAN variant.
- `Pre-declaration honored` must be YES for a complete block. If NO, the analysis is incomplete.

---

*(Repeat pre-declaration + vector analysis + roll-up for each Write-capable role.)*

---

## PHASE 3 GATE

| Check | Answer |
|-------|--------|
| Every Write-capable role has a PRE-DECLARATION block | YES / NO |
| Every declared vector was analyzed | YES / NO |
| Every NOT POSSIBLE verdict cites a specific closing mechanism | YES / NO |
| Every Write-capable role has an ESCALATION ROLL-UP block | YES / NO |
| `Mechanisms cited` in every roll-up has one entry per NOT POSSIBLE verdict (not "see above") | YES / NO |
| Every `Pre-declaration honored` field reads YES | YES / NO |
| Every POSSIBLE verdict has a G-## in the Security Gap Log | YES / NO |

**PHASE 3 COMPLETE: [YES / NO]**

---

## PHASE 4 -- REMEDIATION AND DEFENSE-IN-DEPTH

**4a -- Gap remediation:**

`[G-##]: Change [element] on [entity/field/role] from [current state] to [target state] in [location]. After fix: [behavioral change].`

Every G-## in the log must have a 4a entry. Generic advice does not qualify.

**4b -- Defense-in-depth:**

| Entity | Security Role: Independent? | FLS: Independent? | Record Scope: Independent? | Single POF? |
|--------|----------------------------|-------------------|---------------------------|-------------|

Single POF = YES: add G-## if not already present.

**4c -- Stock role coverage:**

Customer Service Representative (and any other stock role): baseline privileges, least-privilege verdict (SATISFIED or EXCESS -- specific reduction).

---

## OUTPUT REQUIREMENTS

- Gap log rows added at discovery time; G-## assigned at moment of discovery
- Every Write-capable role has a PRE-DECLARATION and an ESCALATION ROLL-UP block; both blocks fully populated
- Every NOT POSSIBLE verdict cites its closing mechanism inline and in the roll-up `Mechanisms cited` field
- ENTITY CLOSURE blocks appear for every entity; gap-containing entities name gaps; gap-free entities state NONE
- Every G-## has a 4a remediation entry

---

## V-04 -- Combined: Dedicated Closing Mechanism Column (C-18) + Mandatory Roll-Up Block (C-19)

**Axis:** Combined -- output format (dedicated `Closing Mechanism` column in the vector table, C-18) + role sequence (structured ESCALATION ROLL-UP block with required fields, C-19)
**Hypothesis:** V-01 prevents bare NOT POSSIBLE cells by making the closing mechanism a distinct column that cannot share space with the verdict. V-02 prevents missing role-level synthesis by making the roll-up a structured block with fields that must each contain a non-generic value. The two failure modes are independent: a trace could have complete closing mechanism citations but no roll-up (passes C-18, fails C-19), or a complete roll-up but bare NOT POSSIBLE cells (fails C-18, passes C-19). Combining both structures addresses both failure modes independently without the mechanics of one depending on the other.

---

You are running a permissions trace signal for: {{topic}}

---

**SECURITY GAP LOG -- add rows progressively. Assign G-## identifiers at discovery.**

| G-## | Entity | Field / Operation | Role(s) | Gap Type | Risk |
|------|--------|-------------------|---------|----------|------|

Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / CASCADE-OVERREACH
Risk: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 -- INVENTORY

**1a -- Entity catalog:**

| Entity | Org-Wide Default | Sensitivity | Reason |
|--------|-----------------|-------------|--------|

**1b -- Role catalog:**

| Role | Type (Stock / Custom) | Write-Capable? | Persona |
|------|-----------------------|----------------|---------|

Write-Capable = YES for roles holding Write, Delete, or Assign on any entity.
Stock roles to confirm: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1c -- Operation-role matrix (per entity):**

| Entity: [name] | Role | C | R | W | D | A | Record Scope |
|----------------|------|---|---|---|---|---|--------------|

**1d -- Field-level security (per entity):**

| Entity | Field | Sensitivity | FLS Profile | Read: Allowed | Write: Allowed | Denied |
|--------|-------|-------------|-------------|--------------|----------------|--------|

FLS Profile = NONE on a sensitive field: add to Gap Log now (MISSING-FLS, CRITICAL or HIGH).

**1e -- Sharing rule inventory and per-role verdicts:**

For every role on each entity: "[Role] on [Entity]: [expansion found -- G-##] OR [confirmed no expansion -- basis: [evidence]]."
No rules: "Confirmed: no sharing rules on [Entity]. Checked: [location]."

---

## PHASE 1 GATE

| Check | Answer |
|-------|--------|
| All entities in 1a | YES / NO |
| All roles in 1b with Write-Capable flag | YES / NO |
| All 1c matrices complete | YES / NO |
| All sensitive fields in 1d with FLS status | YES / NO |
| Per-role sharing rule verdicts issued for all entity-role combinations | YES / NO |

**PHASE 1 COMPLETE: [YES / NO]**

---

## PHASE 2 -- ENTITY-LEVEL GAP ANALYSIS

**Entity: [name]**

**2a -- Team membership gap:**

Team-dependent roles: "Users in [Role] not in [Team]: cannot access [record] because [reason]. Self-addition [possible: G-## / not possible: [reason]]."
None: "Confirmed: no team dependency on [Entity]. Checked: [what]."

**2b -- Business unit scope:**

For each BU-scoped role: `[Role] -> [BU scope] -> [OWD behavior] -> [child BU records: YES/NO] -> [reason]`

**2c -- Entity closure:**

```
Entity: [name] -- CLOSED
Operations reviewed:       [list per role]
Sensitive fields confirmed: [list or "none -- confirmed by reviewing [fields]"]
Gaps logged this entity:   [G-## list / NONE]
Status: CLOSED
```

*(Repeat 2a-2c for each entity.)*

---

## PHASE 2 GATE

| Check | Answer |
|-------|--------|
| Every entity has a closure block with all fields | YES / NO |
| Gap-containing entities cite gaps by G-## | YES / NO |
| Gap-free entities state NONE | YES / NO |

**PHASE 2 COMPLETE: [YES / NO]**

---

## PHASE 3 -- ESCALATION VECTOR ANALYSIS (Write-capable role first)

For each Write-capable role: complete the five-vector table and the ESCALATION ROLL-UP block before advancing to the next role.

**Vector table format -- four columns:**

The `Closing Mechanism` column is a distinct cell, separate from `Evidence`. It is required for NOT POSSIBLE verdicts only. For POSSIBLE verdicts it must read exactly `N/A -- G-##`.

**Column rules:**
1. `Verdict`: POSSIBLE or NOT POSSIBLE. No other values.
2. `Evidence`: for POSSIBLE, state the chain of access reached; for NOT POSSIBLE, state what was reviewed (the privilege list checked, the configuration inspected, the field inventory audited).
3. `Closing Mechanism` (NOT POSSIBLE only): name the specific structural fact that closes the vector -- the privilege confirmed absent, the platform constraint, the configuration state verified. "Not applicable", "no escalation", or a restatement of the verdict are not valid. A blank cell for a NOT POSSIBLE row is a format error.

---

### Escalation Vector Audit: [Role Name]

**Write access held by this role:**

For each entity where this role holds W, D, or A: `[Entity]: [operations] at [record scope]`

**Five-vector table:**

| Vector | Evidence | Verdict | Closing Mechanism (NOT POSSIBLE only; N/A for POSSIBLE) |
|--------|----------|---------|----------------------------------------------------------|
| Sharing rule creation | [what was checked to determine whether this role can create or modify sharing rules] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: name the specific privilege absent (e.g., "sharing rule creation requires Write on System Settings -- this role holds no System Settings privilege") or platform constraint. POSSIBLE: N/A -- G-##] |
| Team self-injection | [what was checked -- team management privilege, team types present, self-add controls] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: name the team management privilege absent or configuration preventing self-addition. POSSIBLE: N/A -- G-##] |
| Field-value escalation | [specific fields audited for role/BU/security-profile write access] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: name the specific field list reviewed and the FLS profile denying write, or confirm no such field exists in the entity set. POSSIBLE: N/A -- G-##] |
| Role hierarchy traversal | [hierarchy enabled status, ancestor roles identified, their access grants reviewed] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: state hierarchy enablement status and confirm no ancestor role holds broader access than this role (name the ancestors checked). POSSIBLE: N/A -- G-##] |
| Record ownership transfer | [Assign privilege status, OWD transfer behavior, cross-BU/org scope result] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: state whether Assign is held; if held, state OWD behavior under transferred ownership and confirm cross-scope expansion does not result. POSSIBLE: N/A -- G-##] |

---

### ESCALATION ROLL-UP: [Role Name]

```
Vectors assessed:     [integer]
POSSIBLE count:       [integer]
NOT POSSIBLE count:   [integer]
Mechanisms cited:
  Sharing rule creation:    [one-line closing mechanism -- from the Closing Mechanism cell above]
  Team self-injection:      [one-line closing mechanism]
  Field-value escalation:   [one-line closing mechanism]
  Role hierarchy traversal: [one-line closing mechanism]
  Record ownership transfer:[one-line closing mechanism]
  (List only NOT POSSIBLE verdicts -- omit POSSIBLE rows from this section)
Composite verdict:    [ESCALATION CONFIRMED: G-## / CLEAN: all [N] vectors ruled out -- no escalation path from [Role]]
```

**Block rules:**
- `Mechanisms cited` lists each NOT POSSIBLE vector by name with its closing mechanism. "See table" is not valid. Restate the mechanism.
- For rows where the verdict is POSSIBLE, omit from `Mechanisms cited` (the G-## in the Security Gap Log is the record).
- `Composite verdict` in the CLEAN form must name the count of vectors assessed.
- A roll-up block with any required field blank, generic ("all vectors ruled out"), or pointing to the table above without restating is incomplete.

---

*(Repeat five-vector table + ESCALATION ROLL-UP for each Write-capable role.)*

---

## PHASE 3 GATE

| Check | Answer |
|-------|--------|
| Every Write-capable role has a five-vector table with four columns | YES / NO |
| Every NOT POSSIBLE row has a non-blank `Closing Mechanism` cell naming a structural basis | YES / NO |
| Every POSSIBLE row has `N/A -- G-##` in `Closing Mechanism` | YES / NO |
| Every Write-capable role has an ESCALATION ROLL-UP block | YES / NO |
| `Mechanisms cited` lists only NOT POSSIBLE vectors, one per line, with restated mechanism | YES / NO |
| `Composite verdict` names the vector count in the CLEAN form | YES / NO |
| Every POSSIBLE verdict has a G-## in the Security Gap Log | YES / NO |

**PHASE 3 COMPLETE: [YES / NO]**

---

## PHASE 4 -- REMEDIATION AND DEFENSE-IN-DEPTH

**4a -- Gap remediation:**

`[G-##]: Change [element] on [entity/field/role] from [current state] to [target state] in [location]. After fix: [behavioral change].`

Every G-## must have a 4a entry. Generic advice does not qualify.

**4b -- Defense-in-depth:**

| Entity | Security Role: Independent? | FLS: Independent? | Record Scope: Independent? | Single POF? |
|--------|----------------------------|-------------------|---------------------------|-------------|

Single POF = YES: add G-## if not already present.

**4c -- Stock role coverage:**

Customer Service Representative (and any other stock role): baseline privileges, least-privilege verdict (SATISFIED or EXCESS -- specific reduction).

---

## OUTPUT REQUIREMENTS

- Gap log rows added at discovery time
- Every NOT POSSIBLE vector verdict has a non-blank `Closing Mechanism` cell with a named structural basis
- Every Write-capable role has both a five-vector table and an ESCALATION ROLL-UP block
- `Mechanisms cited` in the roll-up restates (does not reference) each NOT POSSIBLE closing mechanism
- ENTITY CLOSURE blocks appear for every entity; gap-containing entities cite G-##; gap-free entities state NONE
- Every G-## has a 4a remediation entry

---

## V-05 -- Combined: Phrasing Register (Audit Evidence Standard) + Inertia Framing (Hypothesis-Per-Vector)

**Axis:** Combined -- phrasing register (audit evidence standard: NOT POSSIBLE verdicts are formal "No Finding" declarations that must cite confirming evidence and the configuration state verified absent) + inertia framing (each vector opens with a stated design assumption being tested; NOT POSSIBLE closure is a confirmation that the assumption holds; POSSIBLE is a refutation)
**Hypothesis:** C-18 and C-19 both address a gap in synthesis rigor: NOT POSSIBLE verdicts without structural basis, and role-level conclusions left implicit. Inertia framing makes the design assumption explicit before the vector is tested -- "This role is assumed to have no sharing rule creation privilege" -- turning NOT POSSIBLE into a confirmation ("Assumption confirmed") and POSSIBLE into a refutation ("Assumption violated"). A confirmation without stating what was checked to validate the assumption is detectable as incomplete because the design assumption is right there above it. Audit evidence standard provides the per-role roll-up naturally: every audit section has a SECTION VERDICT that synthesizes the evidence, including the count of assumptions confirmed vs. violated.

---

You are running a permissions trace signal for: {{topic}}

---

You are a certified Dataverse security auditor preparing an access control audit report.

**Audit conventions in this report:**
- **Numbered findings:** every security issue receives a sequential identifier (F-01, F-02, ...) assigned at discovery
- **Explicit No Finding declarations:** wherever no issue is found, the report states this explicitly: "No Finding -- confirmed by reviewing [what was reviewed] -- basis: [evidence for the determination]"
- **Design assumption testing:** each escalation vector check opens with the design assumption being tested ("Assumption: this role cannot..."); the verdict confirms or refutes that assumption; a confirmation cites the evidence that validates it
- **Audit section verdicts:** every entity section and every role escalation section closes with a formal AUDIT VERDICT summarizing what was assessed, what assumptions were confirmed vs. refuted, and the composite determination

---

**FINDINGS REGISTER**

| F-## | Section | Entity / Role / Field | Finding Type | Severity | Status |
|------|---------|----------------------|--------------|---------|--------|

Finding types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / BU-SCOPE / SINGLE-LAYER-FAILURE
Severity: CRITICAL / HIGH / MEDIUM
Assign F-## at moment of discovery.

---

## SECTION 1 -- AUDIT SCOPE

**1.1 -- Entities in scope:**

| Entity | Org-Wide Default | Data Classification | Audit Sensitivity |
|--------|-----------------|---------------------|------------------|

Data Classification: Controlled / Internal / Public. Audit Sensitivity: High / Medium / Low.

**1.2 -- Roles in scope:**

| Role | Type (Stock / Custom) | Write-Capable? | Persona |
|------|-----------------------|----------------|---------|

Write-Capable = YES for roles holding W/D/A on any entity.
Stock roles to verify: Customer Service Representative, Basic User, System Customizer, System Administrator.

**1.3 -- Audit scope statement:**

State: "This audit covers [N] entities and [M] roles. Highest audit-sensitivity entity: [name]. Write-capable roles subject to escalation audit: [list]. Stock roles in scope: [list]."

---

## SECTION 2 -- ACCESS RIGHTS AUDIT (per entity, high-sensitivity first)

### Entity: [name] (Audit Sensitivity: [rating])

**2.1 -- Operation rights matrix:**

| Role | C | R | W | D | A | Record Scope | Scope Justification |
|------|---|---|---|---|---|--------------|---------------------|

Scope Justification: state why this scope matches the persona's need. If it exceeds that need: assign F-## (BU-SCOPE or ESCALATION-PATH).

**2.2 -- Field-level security audit:**

| Field | Classification | FLS Profile | Read: Who | Write: Who | Denied: Who | Audit Verdict |
|-------|---------------|-------------|-----------|-----------|-------------|---------------|

Audit Verdict:
- COMPLIANT: profile applied, access matches persona need
- FINDING F-##: [type] -- logged in Findings Register
- NO FINDING: no FLS required -- confirmed: [basis for confirmation that this field requires no FLS]

FLS Profile = NONE on a Controlled or Internal field: FINDING F-## (MISSING-FLS). CRITICAL for Controlled; HIGH for Internal.

**2.3 -- Sharing rule audit:**

Per-role sharing rule verdict (required for every role in 2.1, whether or not rules exist):
- Finding: "FINDING F-## -- [Rule name] grants [access] to [Role] beyond OWD+security role scope -- [over-exposed record set]"
- No finding: "No Finding -- [Role] on [Entity]: confirmed no sharing rules expand access beyond OWD+security role scope -- basis: [evidence of how this was verified]"

**2.4 -- Team membership audit:**

Team-dependent roles: "FINDING F-## -- Users in [Role] not in [Team] are excluded from [record] because [OWD+scope]. Self-addition [confirmed possible -- concern / confirmed not possible -- basis: [configuration reviewed]]."
No team dependency: "No Finding -- [Entity] access requires no team membership for any role -- basis: [what was confirmed]."

---

### ENTITY AUDIT VERDICT: [Entity Name]

```
Operations audited:        [list each operation per role]
Fields audited:            [list each sensitive field, or "none -- confirmed by reviewing [list]"]
Findings logged:           [F-## list / NONE]
Sharing rule verdicts:     [N of N roles received explicit verdicts: YES]
Entity determination:      [FINDINGS PRESENT: F-## list / CLEAN: all access rights confirmed compliant]
```

*(Repeat Section 2 for each entity.)*

---

## SECTION 2 AUDIT GATE

| Check | Answer |
|-------|--------|
| Every entity has an ENTITY AUDIT VERDICT block | YES / NO |
| Entities with findings name findings by F-## | YES / NO |
| Clean entities state CLEAN with explicit determination | YES / NO |
| Every role received an explicit sharing rule verdict per entity | YES / NO |

**SECTION 2 COMPLETE: [YES / NO]**

---

## SECTION 3 -- ESCALATION AUDIT (Write-capable roles)

For each Write-capable role: test five escalation vectors using the design assumption protocol. Close with a ROLE ESCALATION AUDIT VERDICT.

---

### Escalation Audit: [Role Name]

**Write access summary for this role:**

For each entity where this role holds W, D, or A: `[Entity]: [operations] at [record scope]`

**Vector Audit:**

For each of the five vectors:

---

**Vector: Sharing Rule Creation**

> **Design assumption:** This role cannot create or modify sharing rules to expand its own record access.
>
> **What to verify:** Whether this role holds any privilege enabling sharing rule creation or modification (e.g., Write on System Settings, or equivalent in the security role configuration).
>
> **Evidence:** [state what was reviewed -- the specific privilege list consulted, the system setting checked]
>
> **Verdict:** ASSUMPTION CONFIRMED / ASSUMPTION VIOLATED
>
> - If CONFIRMED: "No Finding -- assumption confirmed by [evidence]: [specific structural basis -- the privilege name that is absent, the configuration state verified]. The design assumption holds."
> - If VIOLATED: "FINDING F-## -- ESCALATION-PATH: [Role] can create/modify sharing rules via [specific mechanism]. Chain: [Role] -> [action] -> [elevated access reached]." Log to Findings Register.

---

**Vector: Team Self-Injection**

> **Design assumption:** This role cannot add itself to a team with higher-privilege record scope.
>
> **What to verify:** Team management privileges held by this role; team types present (owner-type vs. access-type); whether self-addition is possible given those team types and privilege grants.
>
> **Evidence:** [state what was reviewed]
>
> **Verdict:** ASSUMPTION CONFIRMED / ASSUMPTION VIOLATED
>
> - If CONFIRMED: "No Finding -- assumption confirmed by [evidence]: [specific structural basis -- the team management privilege absent, the team type restriction, or the configuration preventing self-addition]."
> - If VIOLATED: "FINDING F-## -- ESCALATION-PATH." Log to Findings Register.

---

**Vector: Field-Value Escalation**

> **Design assumption:** This role cannot write a field whose value modifies role assignment, BU membership, or security profile for any user or record in the system.
>
> **What to verify:** Sensitive fields (role lookup, BU lookup, security profile reference) in the entity set; FLS profiles on those fields; whether this role has write access to any of them.
>
> **Evidence:** [list the fields examined and the FLS profile on each]
>
> **Verdict:** ASSUMPTION CONFIRMED / ASSUMPTION VIOLATED
>
> - If CONFIRMED: "No Finding -- assumption confirmed by [evidence]: [specific fields audited; the FLS profile denying write; or the confirmed absence of such a field in the entity set for this topic]."
> - If VIOLATED: "FINDING F-##." Log to Findings Register.

---

**Vector: Role Hierarchy Traversal**

> **Design assumption:** The role hierarchy configuration does not chain this role to a parent role holding broader record access than this role's direct grants.
>
> **What to verify:** Whether role hierarchy is enabled in this environment; the parent roles in this role's hierarchy chain; the access grants of those parent roles vs. this role's grants.
>
> **Evidence:** [hierarchy enabled status; parent roles identified; their access scopes confirmed]
>
> **Verdict:** ASSUMPTION CONFIRMED / ASSUMPTION VIOLATED
>
> - If CONFIRMED: "No Finding -- assumption confirmed by [evidence]: [hierarchy enablement status; named parent roles checked and their access scope; confirmation that no parent broadens access]."
> - If VIOLATED: "FINDING F-##." Log to Findings Register.

---

**Vector: Record Ownership Transfer**

> **Design assumption:** This role cannot assign records to an owner in a different scope in a way that makes those records visible to higher-privilege users under the new owner's scope.
>
> **What to verify:** Whether this role holds Assign; if so, the OWD behavior when ownership transfers to a different BU or org-level owner; whether that results in cross-scope visibility expansion beyond the role's direct grants.
>
> **Evidence:** [Assign privilege status; OWD transfer behavior; cross-scope result confirmed]
>
> **Verdict:** ASSUMPTION CONFIRMED / ASSUMPTION VIOLATED
>
> - If CONFIRMED: "No Finding -- assumption confirmed by [evidence]: [Assign privilege status; if held, the OWD behavior that prevents cross-scope expansion; or the absence of Assign on this role]."
> - If VIOLATED: "FINDING F-##." Log to Findings Register.

---

### ROLE ESCALATION AUDIT VERDICT: [Role Name]

```
Vectors audited:              [integer -- must equal 5]
Assumptions confirmed:        [integer]
Assumptions violated:         [integer -- findings logged as F-## list or NONE]
Confirmed assumption bases:
  Sharing rule creation:    [one-line structural basis from the "No Finding" declaration above]
  Team self-injection:      [one-line structural basis]
  Field-value escalation:   [one-line structural basis]
  Role hierarchy traversal: [one-line structural basis]
  Record ownership transfer:[one-line structural basis]
  (List only CONFIRMED vectors; omit VIOLATED vectors -- those are in the Findings Register)
Escalation audit conclusion:  [ESCALATION PATHS FOUND: F-## list / NO ESCALATION: all 5 assumptions confirmed for [Role] -- no privilege escalation path identified]
```

**Block rules:**
- `Confirmed assumption bases` lists each CONFIRMED vector by name with its structural basis restated from the "No Finding" declaration. Cross-referencing ("see above") does not qualify.
- `Escalation audit conclusion` in the NO ESCALATION form must name the role and the count.
- A block with any required field blank, generic, or pointing back to the vector section without restating is an incomplete audit section.

---

*(Repeat Section 3 for each Write-capable role.)*

---

## SECTION 3 AUDIT GATE

| Check | Answer |
|-------|--------|
| Every Write-capable role has five vector audits using the assumption protocol | YES / NO |
| Every CONFIRMED verdict has a "No Finding" declaration citing a structural basis | YES / NO |
| Every CONFIRMED vector in the ROLE ESCALATION AUDIT VERDICT restates (not references) its structural basis | YES / NO |
| Every Write-capable role has a ROLE ESCALATION AUDIT VERDICT block | YES / NO |
| `Escalation audit conclusion` names role and vector count in the NO ESCALATION form | YES / NO |
| Every VIOLATED verdict has an F-## in the Findings Register | YES / NO |

**SECTION 3 COMPLETE: [YES / NO]**

---

## SECTION 4 -- REMEDIATION AND ASSURANCE

**4.1 -- Remediation plan:**

For each F-## in the Findings Register:
`[F-##]: Change [element] on [entity/field/role] from [current state] to [target state] in [location]. After remediation: [behavioral change]. Priority: [Severity level].'

Cite by F-## identifier. Generic advice does not qualify. Every F-## must have a 4.1 entry.

**4.2 -- Defense-in-depth assessment:**

| Entity | Security Role: Independent? | FLS: Independent? | Record Scope: Independent? | Single Layer Failure? |
|--------|----------------------------|-------------------|---------------------------|----------------------|

Single Layer Failure = YES: assign F-## (SINGLE-LAYER-FAILURE) if not already logged.

**4.3 -- Stock role least-privilege assessment:**

Customer Service Representative (and any other stock role):
- Baseline privileges for {{topic}}
- Strengthened or weakened from baseline by custom config
- Least-privilege verdict: SATISFIED or EXCESS -- [specific privilege to reduce]

---

## AUDIT REPORT STANDARDS

- Every security finding carries an F-## identifier assigned at discovery
- Every "no finding" determination is an explicit declaration citing the evidence reviewed and the structural basis for the determination
- Every Write-capable role closes with a ROLE ESCALATION AUDIT VERDICT naming: vectors audited, confirmed/violated counts, per-confirmed-vector structural basis restated, and composite escalation conclusion
- Entity sections close with an ENTITY AUDIT VERDICT naming findings or explicit CLEAN determination
- Every F-## in the Findings Register has a 4.1 remediation plan entry
