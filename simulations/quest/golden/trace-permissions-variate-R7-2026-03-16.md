# trace-permissions Variate -- Round 7 (Rubric v7)
**Date:** 2026-03-16
**Rubric:** v7 (C-01 through C-28)
**New criteria targeted this round:** C-25 (closing mechanism column content exclusivity), C-26 (universal three-field no-finding format at all required sites), C-27 (explicit anti-back-reference prohibition in roll-up field definition), C-28 (composite verdict names mechanism type per vector, not counts)
**Prior round retained:** Essential C-01--C-04, recommended C-05--C-07, aspirational C-08--C-24 are structurally enforced throughout

---

## Round 7 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format -- Structural Basis column content exclusivity rule (C-25 single-axis) | R6 V-04 placed the closing mechanism in a dedicated column. C-25 tightens this: the column instruction must state a content exclusivity rule naming the disallowed content forms ("no verdict language; no declaration tracing; one structural fact only"). Without the rule, the structural isolation benefit of C-21 is preserved at the format level but lost at the instruction level -- a compliant responder can still populate the cell with mixed content while satisfying the column format. Adding the explicit exclusivity rule to the column instruction makes mixed-content cells a visible instruction violation, not merely a prose omission. |
| V-02 | Lifecycle emphasis -- universal three-field no-finding format enumerated across all site types (C-26 single-axis) | R6 V-03 required No-Finding Declaration format for every absence but did not enumerate the required site types. C-26 adds enumeration: the five site types are listed explicitly (NOT POSSIBLE verdicts, sharing rule clean, team no-dependency, escalation no-path, gap-free entity closure), and a two-of-three-field format at any enumerated site is a named format violation. Without enumeration, a partial-site coverage pattern can satisfy C-23 while leaving certain site types with two-field formats; the enumeration makes the gap auditable at the rubric level. |
| V-03 | Phrasing register -- explicit back-reference prohibition in roll-up Mechanisms cited instruction (C-27 single-axis) | R6 V-04 required Mechanisms cited to restate each structural fact inline. C-27 tightens this: the field instruction must name the disallowed form explicitly ("do not write 'see table above'", "back-references to the vector table are not permitted"). Without the prohibition, a technically compliant responder can satisfy the "restate inline" instruction by writing a list that points back to the table entries without transcribing them. The prohibition must appear in the instruction itself -- implying inline restatement is not sufficient. |
| V-04 | Combined: column exclusivity (C-25) + universal no-finding sites (C-26) + anti-back-reference prohibition (C-27) | The three single-axis criteria address independent structural gaps: C-25 governs the column instruction, C-26 governs the no-finding site coverage, C-27 governs the roll-up instruction. None implies the other: a prompt with strict column exclusivity may have partial no-finding site coverage and no back-reference prohibition. Combining the three requires independent enforcement choices that do not overlap. |
| V-05 | Combined: all four new criteria (C-25 + C-26 + C-27 + C-28) on the full R6 V-05 foundation (C-20 + C-21 + C-22 + C-23 + C-24) | Full nine-criterion package. The composite verdict sentence (C-28) names each NOT POSSIBLE vector's mechanism type inline -- not a count, not a reference to Mechanisms cited. This is distinct from C-24 (which requires mechanism restatement in the Mechanisms cited field) by requiring the verdict sentence itself to carry mechanism type content. When combined with C-25 (column exclusivity), C-26 (universal three-field), C-27 (explicit prohibition), and the full R6 V-05 stack, every structural position in the escalation analysis is independently constrained: the column cell (C-21, C-25), the vector verdict (C-20, C-22, C-23), the roll-up mechanisms field (C-24, C-27), and the roll-up verdict sentence (C-19, C-28). |

---

## V-01 -- Output Format: Structural Basis Column Content Exclusivity

**Axis:** Output format (the escalation vector table's `Structural Basis` column carries an explicit content exclusivity rule in its instruction: "one structural fact only; no verdict language; no declaration tracing; no placeholder text" -- C-25 single-axis)
**Hypothesis:** R6 V-04 placed the closing mechanism in a dedicated `Structural Basis` column, satisfying C-21's structural isolation requirement. C-25 adds the exclusivity constraint: the column instruction must explicitly state what content is prohibited, not merely describe what it should contain. A column whose instruction allows "state which assumption this confirms" or permits "N/A" for NOT POSSIBLE rows is structurally isolated but instructionally permissive -- a cell can contain a structural fact plus declaration tracing and satisfy both the instruction and the column format. The exclusivity rule makes that content mix a named violation rather than a permitted form. The hypothesis is that explicitly prohibiting co-mingled content in the column instruction, not just describing the intended content, closes the permissive-column failure mode.

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
- FLS Profile = NONE for a sensitive field: assign G-## now (MISSING-FLS). CRITICAL for PII/Credential/Health; HIGH for Financial/Internal-Audit.
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

For each role in 2a with W, D, or A: check whether that access can reach a higher privilege level.

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

For each role marked Write-Capable = YES in Phase 1b, complete the five-vector table and ESCALATION ROLL-UP.

**Structural Basis column rules (mandatory -- enforced at Phase 3 Gate):**

The `Structural Basis` column is exclusively for the closing mechanism citation. Its content is governed by a strict exclusivity rule:

1. **Content permitted:** Exactly one structural fact sentence per NOT POSSIBLE row. A structural fact names the specific privilege confirmed absent, the configuration state confirmed absent, or the platform constraint that closes the vector. One sentence only.
2. **Content prohibited:** No verdict language (do not write "NOT POSSIBLE" or "Assumption Confirmed" in this column). No declaration tracing (do not write "confirms declared assumption" or reference the COMMITMENT DECLARATION). No evidence prose (do not write the analysis narrative -- that belongs in the Evidence column). No conditional language ("if NOT POSSIBLE..."). No placeholder text ("N/A for NOT POSSIBLE rows", "see verdict cell").
3. **POSSIBLE rows:** The Structural Basis cell must contain exactly: `N/A -- G-##` (the gap log identifier). No other content.
4. **Empty cell on a NOT POSSIBLE row:** A format error. The verdict is unverifiable without a structural fact in this column.

A NOT POSSIBLE row where the Structural Basis cell contains a structural fact mixed with verdict language, declaration tracing, or evidence prose fails the exclusivity rule even if a structural fact is present -- the cell must contain the structural fact and nothing else.

---

### Escalation Vector Audit: [Role Name]

**Write access held by this role:**

For each entity where this role holds W, D, or A: `[Entity]: [operations] at [record scope]`

**Five-vector table:**

| Vector | Evidence | Verdict | Structural Basis |
|--------|----------|---------|------------------|
| Sharing rule creation | [State the privilege checked and configuration reviewed] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: one structural fact sentence -- e.g., "No Share privilege on any entity in role definition; no admin delegation grants sharing rule creation to this role." No verdict language. No declaration tracing. POSSIBLE: N/A -- G-##] |
| Team self-injection | [State the team types checked and membership privilege reviewed] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: one structural fact sentence -- e.g., "Owner team membership requires explicit System Admin assignment; access teams allow self-addition but grant access-only scope, not owner scope." No verdict language. No declaration tracing. POSSIBLE: N/A -- G-##] |
| Field-value escalation | [State the fields reviewed and FLS profiles checked] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: one structural fact sentence -- e.g., "FLS Profile 'Service Rep - Restricted' denies write on SystemUser.BusinessUnit; no custom field in the entity set maps to security role or BU assignment." No verdict language. No declaration tracing. POSSIBLE: N/A -- G-##] |
| Role hierarchy traversal | [State whether hierarchy is enabled and the ancestor roles reviewed] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: one structural fact sentence -- e.g., "Role hierarchy enabled for Read; all ancestors scoped BU-only; no ancestor holds Org-scope on any entity in the trace." No verdict language. No declaration tracing. POSSIBLE: N/A -- G-##] |
| Record ownership transfer | [State whether Assign is held and the OWD behavior reviewed] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: one structural fact sentence -- e.g., "Assign not held; OWD Private -- transferred records leave this role's User scope; no sharing rule re-grants post-transfer access." No verdict language. No declaration tracing. POSSIBLE: N/A -- G-##] |

**Column integrity check (complete before writing ESCALATION ROLL-UP):**

- Every NOT POSSIBLE row has a Structural Basis cell containing one structural fact: YES / NO
- No Structural Basis cell contains verdict language, declaration tracing, or evidence prose: YES / NO
- Every POSSIBLE row has Structural Basis = `N/A -- G-##` with no other content: YES / NO

If any check is NO: correct the cell before continuing.

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

---

*(Repeat five-vector table + ESCALATION ROLL-UP for each Write-capable role.)*

---

## PHASE 3 GATE

| Check | Answer |
|-------|--------|
| Every Write-capable role has a five-vector table | YES / NO |
| Every NOT POSSIBLE row has a Structural Basis cell with one structural fact -- no verdict language, no declaration tracing, no evidence prose | YES / NO |
| Every POSSIBLE row has Structural Basis = N/A -- G-## with no other content | YES / NO |
| Every Write-capable role has an ESCALATION ROLL-UP with all fields populated | YES / NO |
| Every Mechanisms cited entry restates its structural fact inline | YES / NO |

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

- `Structural Basis` column holds only structural facts -- one structural fact sentence per NOT POSSIBLE row; no verdict language, no declaration tracing, no evidence prose, no conditional language
- A Structural Basis cell containing a structural fact mixed with any prohibited content type fails the exclusivity rule
- ESCALATION ROLL-UP Mechanisms cited restates each structural fact inline; no back-references to the table
- ENTITY CLOSURE blocks appear after every entity section regardless of gap state
- Every G-## in the Security Gap Log has a 4a remediation entry

---

## V-02 -- Lifecycle Emphasis: Universal Three-Field No-Finding Format at All Enumerated Sites

**Axis:** Lifecycle emphasis (the no-finding declaration format is required at every one of five explicitly enumerated site types throughout the trace; the site types are named in the prompt; two-of-three-field formats at any enumerated site are named format violations -- C-26 single-axis)
**Hypothesis:** R6 V-03 required No-Finding Declaration format for every absence but did not enumerate which site types require it. A model that applies the format selectively -- fully at escalation vector verdicts but partially at sharing rule clean findings, or with two-of-three fields at team no-dependency sites -- satisfies the spirit of C-23 at some sites while reverting to partial formats at others. C-26 closes this by naming the five required sites explicitly and stating that a two-of-three-field format at any enumerated site is a violation. The hypothesis is that enumeration makes partial-site coverage visible as a named gap rather than an undetected inconsistency.

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

**No-Finding Declaration format -- required at all five enumerated site types:**

```
NO FINDING -- [label]
Checked:     [what was reviewed -- entity, field, role, privilege, or configuration element; be specific]
Confirmed:   [what configuration state was confirmed absent -- the specific privilege, rule, field, or mechanism that would enable the threat was not found]
Conclusion:  [stated outcome -- the access or escalation path is closed because: specific structural fact]
```

**Required site types (all five require this exact three-field format):**

1. **NOT POSSIBLE verdicts** in the escalation vector table -- every vector where escalation was not found
2. **Sharing rule clean verdict per role per entity** -- every role where no sharing rule expands access
3. **Team no-dependency verdict per entity** -- when no role requires team membership to access the entity
4. **Escalation no-path per role on each entity** -- every role where 2e found no escalation path
5. **Gap-free entity closure** -- every ENTITY CLOSURE where Gaps logged = NONE

**Format violations that do not pass (at any of the five site types):**
- A two-of-three-field format (Checked + Confirmed without Conclusion, or Checked + Conclusion without Confirmed) -- all three fields are required without exception
- Bare negatives: "NOT POSSIBLE", "none found", "NONE", "no gaps", "no escalation", "no dependency"
- Inline prose without the three labeled fields: "No sharing rule targets this role" (fails sites 2 and 3)
- The Conclusion field restating the Confirmed field without adding a structural fact about why the path is closed

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

**2c -- Sharing rule audit:**

| Rule Name | Trigger | Access Granted | Recipient | Verdict: Expected / Conflict-[G-##] |
|-----------|---------|----------------|-----------|-------------------------------------|

Per-role sharing rule declarations (required for every role in 2a, regardless of outcome):

For roles where sharing rules expand access: "[Role] on [Entity]: sharing rules expand access -- [rule name], see G-##."

For roles where no sharing rule expansion exists (site type 2 -- required three-field format):
```
NO FINDING -- Sharing rules for [Role] on [Entity]
Checked:     All criteria-based sharing rules targeting [Entity] with [Role] as recipient; all manual sharing grants for [Entity] records accessible to [Role]; owner team expansion rules
Confirmed:   No criteria-based sharing rule triggers for conditions applicable to [Role]; no manual sharing grant expands [Role] access beyond OWD + security role scope
Conclusion:  [Role] access on [Entity] is bounded by [OWD level] + security role privilege only; the sharing rule vector is closed for this role on this entity
```

**2d -- Team membership dependency:**

For any role whose access depends on team membership: "Users in [Role] not in [Team] cannot access [record type] because [OWD+scope]. Team controlled by [mechanism]. Self-addition [possible / not possible]: [reason]. [If possible and unintended: assign G-##.]"

If no team dependency exists (site type 3 -- required three-field format):
```
NO FINDING -- Team dependency for [Entity]
Checked:     OWD setting for [Entity] (Private / BU / Organization); whether any role in the 2a matrix holds access only via team membership to an owner or access team; whether team-owned record visibility is required for any operation listed in 2a
Confirmed:   No role in this entity section holds access that is contingent on team membership; no owner team is listed as the record scope for any role in the 2a matrix; no access team grants the only path to [Entity] records for any role
Conclusion:  [Entity] access is governed by security role privilege + OWD scope for all roles in scope; no team membership gap exists for this entity
```

**2e -- Entity-level escalation check:**

For each role in 2a with W, D, or A: check whether that access can reach a higher privilege level.

Found path: assign G-## (ESCALATION-PATH). Chain: `[Role] -> [action on [Entity]] -> [elevated access reached]`

No path found (site type 4 -- required three-field format per role):
```
NO FINDING -- Escalation from [Role] on [Entity]
Checked:     Assign privilege on [Entity] (present / absent); record ownership transfer effect on [Role]'s own scope under OWD [setting]; sharing rule creation privilege (Share on [Entity]); field modification paths to role assignment or BU membership change via writable fields
Confirmed:   No Write, Assign, or Delete operation available to [Role] on [Entity] enables reaching a higher privilege scope; no field writable by [Role] on [Entity] modifies role or BU assignment; no Assign privilege that would move records out of [Role]'s scope in a way that then re-grants broader access
Conclusion:  [Role] cannot escalate privilege via [Entity] operations because [specific structural reason per mechanism checked]
```

---

### ENTITY CLOSURE: [Entity Name]

```
Operations reviewed:       [List each operation (C/R/W/D/A) audited per role -- do not write "all operations"]
Sensitive fields confirmed: [List each sensitive field reviewed]
Gaps logged this entity:   [G-## list / NONE]
Sharing rule verdicts:     [N of N roles received three-field No-Finding declarations or positive findings: YES]
Escalation checked:        [Roles with W/D/A that received three-field No-Finding declarations or escalation paths: list]
Status:                    CLOSED
```

Gap-free closure (site type 5 -- required three-field format when Gaps logged = NONE):
```
NO FINDING -- [Entity Name] security review
Checked:     [list of operations reviewed per role, sensitive fields confirmed, sharing rules audited per role, escalation vectors checked per W/D/A role]
Confirmed:   No missing FLS rules, no sharing conflicts, no team membership gaps, no escalation paths -- specific items: [enumerate what was confirmed absent]
Conclusion:  [Entity Name] has no security gaps under the scope of this trace; all access paths bounded correctly by [OWD + security role + FLS layer]
```

---

*(Repeat Phase 2 section + ENTITY CLOSURE for each entity.)*

---

## PHASE 2 GATE

| Check | Answer |
|-------|--------|
| Every entity in the 1a catalog has a Phase 2 section | YES / NO |
| Every entity has an ENTITY CLOSURE block | YES / NO |
| Every gap-containing entity names its gaps by G-## in the CLOSURE block | YES / NO |
| Every gap-free entity has a three-field No-Finding closure declaration (Checked / Confirmed / Conclusion) | YES / NO |
| Every role received a three-field sharing rule declaration (finding or No-Finding) for every entity | YES / NO |
| Every W/D/A role received a three-field escalation declaration (finding or No-Finding) per entity | YES / NO |
| No declaration at any site uses a two-of-three-field format | YES / NO |

**PHASE 2 COMPLETE: [YES / NO]**

---

## PHASE 3 -- ESCALATION VECTOR ANALYSIS (organized by Write-capable role)

For each role marked Write-Capable = YES in Phase 1b, complete the five-vector table and ESCALATION ROLL-UP.

**Vector table instruction:** The `Closing Mechanism` column holds the structural basis for NOT POSSIBLE verdicts. NOT POSSIBLE verdicts must use the three-field No-Finding format in the Verdict cell (site type 1). The Closing Mechanism column holds the single structural fact extracted from that declaration -- a separate column for structural isolation.

---

### Escalation Vector Audit: [Role Name]

**Write access held by this role:**

For each entity where this role holds W, D, or A: `[Entity]: [operations] at [record scope]`

**Five-vector table:**

| Vector | Evidence | Verdict | Closing Mechanism |
|--------|----------|---------|-------------------|
| Sharing rule creation | [State the privilege checked and configuration reviewed] | NOT POSSIBLE -- Checked: [privilege reviewed]; Confirmed: [specific privilege confirmed absent]; Conclusion: [path closed because structural fact] OR POSSIBLE -- G-## | [NOT POSSIBLE: single structural fact only; POSSIBLE: N/A -- G-##] |
| Team self-injection | [State the team types and membership privileges reviewed] | NOT POSSIBLE -- Checked: [team types reviewed]; Confirmed: [what confirmed absent]; Conclusion: [path closed because structural fact] OR POSSIBLE -- G-## | [NOT POSSIBLE: single structural fact only; POSSIBLE: N/A -- G-##] |
| Field-value escalation | [State the fields and FLS profiles reviewed] | NOT POSSIBLE -- Checked: [fields and profiles reviewed]; Confirmed: [what confirmed absent]; Conclusion: [path closed because structural fact] OR POSSIBLE -- G-## | [NOT POSSIBLE: single structural fact only; POSSIBLE: N/A -- G-##] |
| Role hierarchy traversal | [State whether hierarchy is enabled and ancestors reviewed] | NOT POSSIBLE -- Checked: [hierarchy setting and ancestors reviewed]; Confirmed: [what confirmed -- no broader scope]; Conclusion: [path closed because structural fact] OR POSSIBLE -- G-## | [NOT POSSIBLE: single structural fact only; POSSIBLE: N/A -- G-##] |
| Record ownership transfer | [State whether Assign is held and OWD behavior reviewed] | NOT POSSIBLE -- Checked: [Assign and OWD reviewed]; Confirmed: [what confirmed -- no scope expansion]; Conclusion: [path closed because structural fact] OR POSSIBLE -- G-## | [NOT POSSIBLE: single structural fact only; POSSIBLE: N/A -- G-##] |

---

### ESCALATION ROLL-UP: [Role Name]

```
Vectors assessed:    5 (sharing rule creation, team self-injection, field-value escalation, role hierarchy traversal, record ownership transfer)
POSSIBLE count:      [count / NONE]
NOT POSSIBLE count:  [count]
Mechanisms cited:    [list closing mechanism per NOT POSSIBLE verdict by vector name, restated inline]
Composite verdict:   [no escalation path identified for this role / ESCALATION PATHS: G-##, G-##]
```

---

*(Repeat five-vector table + ESCALATION ROLL-UP for each Write-capable role.)*

---

## PHASE 3 GATE

| Check | Answer |
|-------|--------|
| Every Write-capable role has a five-vector table | YES / NO |
| Every NOT POSSIBLE vector verdict uses all three fields (Checked / Confirmed / Conclusion) in the Verdict cell | YES / NO |
| No NOT POSSIBLE verdict uses only two of three fields | YES / NO |
| Every POSSIBLE verdict logs a G-## | YES / NO |
| Every Write-capable role has an ESCALATION ROLL-UP with all fields populated | YES / NO |

**PHASE 3 COMPLETE: [YES / NO]**

---

## PHASE 4 -- REMEDIATION AND DEFENSE-IN-DEPTH

**4a -- Gap remediation:**

For each G-## in the Security Gap Log:
`[G-##]: Change [element] on [entity/field/role] from [current state] to [target state] in [solution location]. After fix: [behavioral change for the affected role].`

Cite by G-## identifier. Every G-## must have a 4a entry.

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

- Three-field No-Finding Declaration format (Checked / Confirmed / Conclusion) is required at every one of the five enumerated site types: NOT POSSIBLE vector verdicts, sharing rule clean per role, team no-dependency per entity, escalation no-path per role, gap-free entity closure
- A two-of-three-field format at any enumerated site is a named format violation -- all three fields are required without exception
- Bare negatives at any enumerated site type do not satisfy the standard
- ENTITY CLOSURE blocks appear after every entity section regardless of gap state
- Every G-## in the Security Gap Log has a 4a remediation entry

---

## V-03 -- Phrasing Register: Explicit Anti-Back-Reference Prohibition in Roll-Up

**Axis:** Phrasing register (the ESCALATION ROLL-UP's `Mechanisms cited` field instruction explicitly prohibits back-references by naming the disallowed forms; the prohibition appears in the field instruction itself, not only implied by the "restate inline" framing -- C-27 single-axis)
**Hypothesis:** R6 V-04 required Mechanisms cited to restate each structural fact inline rather than referencing the table above, and the roll-up rules stated "writing 'see table above' ... is a format violation." C-27 moves that prohibition into the field instruction itself, naming the disallowed forms at the instruction level rather than only in a note after the template. Without the prohibition in the field definition, a technically compliant responder can satisfy the "restate inline" framing by writing a list that points back to the table entries by description -- "sharing rule creation: [as documented in vector table, no Share privilege]" -- which is structurally a back-reference. The prohibition must name the disallowed form so it is an auditable constraint at the instruction level, not only a downstream note.

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
- FLS Profile = NONE for a sensitive field: assign G-## now (MISSING-FLS)
- Denied Roles must be populated explicitly

**2c -- Sharing rule audit:**

| Rule Name | Trigger | Access Granted | Recipient | Verdict: Expected / Conflict-[G-##] |
|-----------|---------|----------------|-----------|-------------------------------------|

Per-role sharing rule statements (required for every role in 2a, regardless of outcome):
"[Role] on [Entity]: sharing rules [expand access -- [rule name], see G-##] OR [confirmed do not expand -- basis: [evidence confirming no criteria-based or manual sharing targets this role]]."

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
| Every gap-free entity explicitly states NONE | YES / NO |
| Every role received an explicit sharing rule statement for every entity | YES / NO |

**PHASE 2 COMPLETE: [YES / NO]**

---

## PHASE 3 -- ESCALATION VECTOR ANALYSIS (organized by Write-capable role)

For each role marked Write-Capable = YES in Phase 1b, complete the five-vector table and ESCALATION ROLL-UP.

**Structural Basis column rules:**
1. The `Structural Basis` column holds exactly one value per row: a single structural fact sentence (for NOT POSSIBLE rows) or `N/A -- G-##` (for POSSIBLE rows).
2. No verdict language in this column. No evidence prose. No conditionals.
3. A NOT POSSIBLE row with a blank or generic Structural Basis is a format error.
4. The Structural Basis column is not a restatement of the Evidence column -- it names the specific configuration state confirmed absent, stated once, in this column only.

---

### Escalation Vector Audit: [Role Name]

**Write access held by this role:**

For each entity where this role holds W, D, or A: `[Entity]: [operations] at [record scope]`

**Five-vector table:**

| Vector | Evidence | Verdict | Structural Basis |
|--------|----------|---------|------------------|
| Sharing rule creation | [State the privilege checked and configuration reviewed] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: one structural fact sentence] [POSSIBLE: N/A -- G-##] |
| Team self-injection | [State the team types and membership privileges reviewed] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: one structural fact sentence] [POSSIBLE: N/A -- G-##] |
| Field-value escalation | [State the fields reviewed and FLS profiles checked] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: one structural fact sentence] [POSSIBLE: N/A -- G-##] |
| Role hierarchy traversal | [State whether hierarchy is enabled and ancestors reviewed] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: one structural fact sentence] [POSSIBLE: N/A -- G-##] |
| Record ownership transfer | [State whether Assign is held and OWD behavior reviewed] | POSSIBLE / NOT POSSIBLE | [NOT POSSIBLE: one structural fact sentence] [POSSIBLE: N/A -- G-##] |

---

### ESCALATION ROLL-UP: [Role Name]

```
Vectors assessed:      5 (sharing rule creation, team self-injection, field-value escalation, role hierarchy traversal, record ownership transfer)
POSSIBLE count:        [count / NONE]
NOT POSSIBLE count:    [count]
Mechanisms cited:
  [FIELD INSTRUCTION: For each NOT POSSIBLE vector, restate the structural fact from the Structural Basis cell
   inline in this field, identified by vector name. Do not write "see table above", "mechanisms cited in
   Phase 3", "see vectors above", "as documented in the five-vector table", or any equivalent back-reference.
   Back-references to the vector table are not permitted in this field. A line that says
   "sharing rule creation: [structural fact from table above]" is a back-reference and does not pass.
   Each line must stand alone as an auditable record independent of the vector table:
   - Sharing rule creation:    [the structural fact, restated in full]
   - Team self-injection:      [the structural fact, restated in full]
   - Field-value escalation:   [the structural fact, restated in full]
   - Role hierarchy traversal: [the structural fact, restated in full]
   - Record ownership transfer:[the structural fact, restated in full]
   POSSIBLE vectors: state "POSSIBLE -- G-##" for that vector line.]
Composite verdict:     [no escalation path identified for this role / ESCALATION PATHS: G-##, G-##]
```

Roll-up integrity check:
- Every Mechanisms cited line restates its structural fact inline -- no back-references: YES / NO
- If NO: identify which line contains a back-reference and restate it before continuing.

---

*(Repeat five-vector table + ESCALATION ROLL-UP for each Write-capable role.)*

---

## PHASE 3 GATE

| Check | Answer |
|-------|--------|
| Every Write-capable role has a five-vector table | YES / NO |
| Every NOT POSSIBLE row has a non-blank Structural Basis cell with one structural fact | YES / NO |
| No Structural Basis cell contains verdict language or evidence prose | YES / NO |
| Every POSSIBLE row has Structural Basis = N/A -- G-## | YES / NO |
| Every Write-capable role has an ESCALATION ROLL-UP | YES / NO |
| Every Mechanisms cited line restates its structural fact inline -- zero back-references ("see table", "as documented", "mechanisms cited above") | YES / NO |

**PHASE 3 COMPLETE: [YES / NO]**

---

## PHASE 4 -- REMEDIATION AND DEFENSE-IN-DEPTH

**4a -- Gap remediation:**

For each G-## in the Security Gap Log:
`[G-##]: Change [element] on [entity/field/role] from [current state] to [target state] in [solution location]. After fix: [behavioral change for the affected role].`

Cite by G-## identifier. Every G-## must have a 4a entry.

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

- ESCALATION ROLL-UP Mechanisms cited field must not contain "see table above", "mechanisms cited in Phase 3", "see vectors above", or any equivalent back-reference -- these forms are explicitly prohibited
- Each Mechanisms cited line must stand alone as an auditable record independent of the vector table
- ENTITY CLOSURE blocks appear after every entity section regardless of gap state
- Every G-## in the Security Gap Log has a 4a remediation entry

---

## V-04 -- Combined: Column Exclusivity (C-25) + Universal No-Finding Sites (C-26) + Anti-Back-Reference Prohibition (C-27)

**Axis:** Combined output format + lifecycle emphasis + phrasing register (structural basis column with strict content exclusivity rule naming prohibited content forms; no-finding declaration required at all five explicitly enumerated site types with two-of-three-field formats prohibited by name; Mechanisms cited field instruction explicitly prohibits back-references naming the disallowed forms -- C-25 + C-26 + C-27)
**Hypothesis:** The three single-axis criteria address independent structural positions: C-25 governs what may appear in the Structural Basis column cell; C-26 governs which site types must carry a full three-field no-finding declaration; C-27 governs what the roll-up Mechanisms cited field instruction says about back-references. None of these implies the other -- a prompt can have strict column exclusivity (C-25) while having partial no-finding site coverage (fails C-26) and an implicit-only back-reference prohibition (fails C-27). Combining the three requires three independent enforcement choices that act on different structural positions in the output. The combined variation tests whether all three can be enforced simultaneously without creating conflicting instructions.

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

**No-Finding Declaration format -- required at all five enumerated site types:**

```
NO FINDING -- [label]
Checked:     [what was reviewed -- specific entities, fields, roles, privileges, or configuration elements]
Confirmed:   [what configuration state was confirmed absent -- the specific privilege, rule, or mechanism that would enable the threat]
Conclusion:  [stated outcome -- the path is closed because: specific structural fact different from Confirmed]
```

**Required site types -- all five require the complete three-field format above:**

1. **NOT POSSIBLE verdicts** in the escalation vector table
2. **Sharing rule clean verdict** per role per entity
3. **Team no-dependency verdict** per entity
4. **Escalation no-path** per role on each entity (2e)
5. **Gap-free entity closure** (ENTITY CLOSURE where Gaps logged = NONE)

**Two-of-three-field formats are explicitly prohibited at all five site types.** A format that supplies Checked + Confirmed without Conclusion, or Confirmed + Conclusion without Checked, does not satisfy the standard at that site.

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

**2c -- Sharing rule audit:**

| Rule Name | Trigger | Access Granted | Recipient | Verdict: Expected / Conflict-[G-##] |
|-----------|---------|----------------|-----------|-------------------------------------|

Per-role sharing rule declarations (required for every role in 2a -- site type 2):

For expansion: "[Role] on [Entity]: sharing rules expand access -- [rule name], see G-##."

For no expansion (three-field format required -- two-of-three-field format not permitted):
```
NO FINDING -- Sharing rules for [Role] on [Entity]
Checked:     All criteria-based sharing rules targeting [Entity] with [Role] as recipient; all manual sharing grants for [Entity] records accessible to [Role]
Confirmed:   No criteria-based or manual sharing rule expands [Role] access beyond OWD + security role scope; [specific rule types checked and found absent]
Conclusion:  [Role] access on [Entity] is bounded by [OWD level] + security role privilege only; sharing rule vector is closed for this role
```

**2d -- Team membership dependency:**

For any role with team-dependent access: "Users in [Role] not in [Team] cannot access [record type] because [OWD+scope]. Team controlled by [mechanism]. Self-addition [possible / not possible]: [reason]. [If possible and unintended: assign G-##.]"

If no team dependency (site type 3 -- three-field format required):
```
NO FINDING -- Team dependency for [Entity]
Checked:     OWD setting for [Entity]; whether any role in the 2a matrix holds access only via team membership; team-owned record scope requirements per role
Confirmed:   No role requires team membership to access [Entity]; no owner team record scope listed for any role in 2a; no access team grants the only path to [Entity] records
Conclusion:  [Entity] access governed by security role + OWD for all roles; no team membership gap exists on this entity
```

**2e -- Entity-level escalation check:**

For each role in 2a with W, D, or A:

Found path: assign G-## (ESCALATION-PATH). Chain: `[Role] -> [action on [Entity]] -> [elevated access reached]`

No path (site type 4 -- three-field format required per role, two-of-three-field format not permitted):
```
NO FINDING -- Escalation from [Role] on [Entity]
Checked:     Assign privilege on [Entity] (present/absent); ownership transfer effect on [Role] scope under OWD [setting]; Share privilege enabling sharing rule creation; write paths to SystemUser.BusinessUnit or security role fields
Confirmed:   No operation available to [Role] on [Entity] enables reaching a higher privilege scope; no writable field on [Entity] modifies role or BU assignment
Conclusion:  [Role] cannot escalate from [Entity] operations because [specific structural reason per mechanism]
```

---

### ENTITY CLOSURE: [Entity Name]

```
Operations reviewed:       [List each operation (C/R/W/D/A) audited per role]
Sensitive fields confirmed: [List each sensitive field reviewed]
Gaps logged this entity:   [G-## list / NONE]
Sharing rule verdicts:     [N of N roles received three-field No-Finding declarations or positive findings: YES]
Escalation checked:        [Roles with W/D/A that received three-field No-Finding declarations or escalation paths: list]
Status:                    CLOSED
```

Gap-free closure (site type 5 -- three-field format required when Gaps logged = NONE):
```
NO FINDING -- [Entity Name] security review
Checked:     Operations per role: [list]; Sensitive fields: [list]; Sharing rules per role: [list]; Escalation per W/D/A role: [list]
Confirmed:   No missing FLS, no sharing conflicts, no team gaps, no escalation paths found; items confirmed absent: [enumerate]
Conclusion:  [Entity Name] has no security gaps in this trace; all access bounded by [OWD + security role + FLS]
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
| Every gap-free entity has a three-field No-Finding closure (site type 5) | YES / NO |
| Every role received a three-field sharing rule declaration (finding or No-Finding) -- site type 2 | YES / NO |
| Every W/D/A role received a three-field escalation declaration (finding or No-Finding) per entity -- site type 4 | YES / NO |
| No declaration at any site uses a two-of-three-field format | YES / NO |
| Every team no-dependency confirmation uses the three-field format -- site type 3 | YES / NO |

**PHASE 2 COMPLETE: [YES / NO]**

---

## PHASE 3 -- ESCALATION VECTOR ANALYSIS (organized by Write-capable role)

For each role marked Write-Capable = YES in Phase 1b, complete the five-vector table and ESCALATION ROLL-UP.

**Structural Basis column content exclusivity rule (applies to every row in every five-vector table):**

The `Structural Basis` column is governed by a strict content exclusivity rule:

- **Permitted content (NOT POSSIBLE rows):** One structural fact sentence only -- the specific privilege confirmed absent or the platform constraint that closes the vector. Nothing else.
- **Prohibited content in this column:** Verdict language ("NOT POSSIBLE", "Assumption Confirmed", "path closed"). Declaration tracing ("confirms the declared assumption", "per commitment above"). Evidence prose (analysis narrative, what was reviewed). Conditional language ("if NOT POSSIBLE..."). Placeholder text ("see verdict cell", "N/A for NOT POSSIBLE").
- **POSSIBLE rows:** Exactly `N/A -- G-##`. No other content.
- **A NOT POSSIBLE row where the Structural Basis cell contains a structural fact mixed with any prohibited content type fails the exclusivity rule** even if the structural fact is present.

---

### Escalation Vector Audit: [Role Name]

**Write access held by this role:**

For each entity where this role holds W, D, or A: `[Entity]: [operations] at [record scope]`

**Five-vector table:**

| Vector | Evidence | Verdict | Structural Basis |
|--------|----------|---------|------------------|
| Sharing rule creation | [State the privilege checked and configuration reviewed] | NOT POSSIBLE -- Checked: [privilege]; Confirmed: [specific privilege confirmed absent]; Conclusion: [path closed because structural fact] OR POSSIBLE -- G-## | [One structural fact only; no verdict language; no declaration tracing; POSSIBLE = N/A -- G-##] |
| Team self-injection | [State the team types and membership privileges reviewed] | NOT POSSIBLE -- Checked: [teams reviewed]; Confirmed: [what confirmed absent]; Conclusion: [path closed because structural fact] OR POSSIBLE -- G-## | [One structural fact only; no verdict language; no declaration tracing; POSSIBLE = N/A -- G-##] |
| Field-value escalation | [State the fields reviewed and FLS profiles checked] | NOT POSSIBLE -- Checked: [fields and profiles]; Confirmed: [what confirmed absent]; Conclusion: [path closed because structural fact] OR POSSIBLE -- G-## | [One structural fact only; no verdict language; no declaration tracing; POSSIBLE = N/A -- G-##] |
| Role hierarchy traversal | [State whether hierarchy is enabled and ancestors reviewed] | NOT POSSIBLE -- Checked: [hierarchy and ancestors]; Confirmed: [no broader scope exists]; Conclusion: [path closed because structural fact] OR POSSIBLE -- G-## | [One structural fact only; no verdict language; no declaration tracing; POSSIBLE = N/A -- G-##] |
| Record ownership transfer | [State whether Assign is held and OWD behavior reviewed] | NOT POSSIBLE -- Checked: [Assign and OWD]; Confirmed: [no scope expansion on transfer]; Conclusion: [path closed because structural fact] OR POSSIBLE -- G-## | [One structural fact only; no verdict language; no declaration tracing; POSSIBLE = N/A -- G-##] |

**Column integrity check (complete before writing ESCALATION ROLL-UP):**
- Every NOT POSSIBLE row has a Structural Basis cell with one structural fact and no prohibited content: YES / NO
- Every POSSIBLE row has Structural Basis = `N/A -- G-##` with no other content: YES / NO
- If any check is NO: correct before continuing.

---

### ESCALATION ROLL-UP: [Role Name]

```
Vectors assessed:      5 (sharing rule creation, team self-injection, field-value escalation, role hierarchy traversal, record ownership transfer)
POSSIBLE count:        [count / NONE]
NOT POSSIBLE count:    [count]
Mechanisms cited:
  [FIELD INSTRUCTION: Restate each NOT POSSIBLE vector's structural fact inline by vector name.
   Do not write "see table above", "mechanisms cited in Phase 3 table", "see vectors above",
   "as documented above", or any equivalent back-reference. Back-references to the vector table
   are not permitted in this field. Each line must be self-contained:
   - Sharing rule creation:    [structural fact restated in full -- no back-reference]
   - Team self-injection:      [structural fact restated in full -- no back-reference]
   - Field-value escalation:   [structural fact restated in full -- no back-reference]
   - Role hierarchy traversal: [structural fact restated in full -- no back-reference]
   - Record ownership transfer:[structural fact restated in full -- no back-reference]
   POSSIBLE vectors: "POSSIBLE -- G-##"]
Composite verdict:     [no escalation path identified for this role / ESCALATION PATHS: G-##, G-##]
```

---

*(Repeat five-vector table + ESCALATION ROLL-UP for each Write-capable role.)*

---

## PHASE 3 GATE

| Check | Answer |
|-------|--------|
| Every Write-capable role has a five-vector table | YES / NO |
| Every NOT POSSIBLE verdict uses all three fields (Checked / Confirmed / Conclusion) in the Verdict cell | YES / NO |
| Every NOT POSSIBLE row has a Structural Basis cell with one structural fact -- no verdict language, no declaration tracing, no evidence prose | YES / NO |
| Every POSSIBLE row has Structural Basis = N/A -- G-## with no other content | YES / NO |
| Every Write-capable role has an ESCALATION ROLL-UP | YES / NO |
| Every Mechanisms cited line restates its structural fact inline -- zero back-references | YES / NO |

**PHASE 3 COMPLETE: [YES / NO]**

---

## PHASE 4 -- REMEDIATION AND DEFENSE-IN-DEPTH

**4a -- Gap remediation:**

For each G-## in the Security Gap Log:
`[G-##]: Change [element] on [entity/field/role] from [current state] to [target state] in [solution location]. After fix: [behavioral change for the affected role].`

Cite by G-## identifier. Every G-## must have a 4a entry.

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

- `Structural Basis` column holds only structural facts -- one structural fact sentence per NOT POSSIBLE row; no verdict language, no declaration tracing, no evidence prose, no conditionals; a cell mixing a structural fact with prohibited content fails the exclusivity rule
- Three-field No-Finding Declaration format required at all five enumerated site types; two-of-three-field formats are named violations at every site
- ESCALATION ROLL-UP Mechanisms cited field must not contain "see table above", "mechanisms cited in Phase 3", or any equivalent back-reference -- these forms are explicitly prohibited by name
- ENTITY CLOSURE blocks appear after every entity section regardless of gap state
- Every G-## in the Security Gap Log has a 4a remediation entry

---

## V-05 -- Combined: C-25 + C-26 + C-27 + C-28 on Full R6 V-05 Foundation

**Axis:** Combined (all four new v7 criteria stacked on the full R6 V-05 foundation: COMMITMENT DECLARATION per role before vectors (C-20), design assumption mini-blocks per vector (C-22), No-Finding Declaration for every absence (C-23), exclusive Structural Basis column (C-21), self-contained roll-up (C-24), plus: column content exclusivity rule naming prohibited forms (C-25), universal three-field format at all five enumerated site types (C-26), explicit back-reference prohibition naming disallowed forms (C-27), composite verdict sentence naming mechanism type per vector not counts (C-28))
**Hypothesis:** The full nine-criterion stack creates a trace where every structural position in the escalation analysis is independently constrained and the constraints are auditable at the instruction level. C-28 is the key new discriminator in this variation: the composite verdict sentence in the ESCALATION ROLL-UP must name each NOT POSSIBLE vector's closing mechanism type inline -- not delegate to the Mechanisms cited field, not use counts alone. A verdict sentence that says "5 vectors assessed, 0 POSSIBLE" is a summary requiring the reader to consult the Mechanisms cited field or the vector table to audit the basis for each verdict. A verdict sentence that says "no escalation path from [Role]: sharing rule creation -- no Share privilege; team self-injection -- no owner team membership privilege; field-value escalation -- FLS denies write on SystemUser fields; role hierarchy traversal -- BU-only ancestors; record ownership transfer -- Assign not held" is self-auditable without consulting any other part of the output. C-28 requires the verdict sentence to carry mechanism type content; the combination with C-24 (which requires Mechanisms cited to restate structural facts) means both structural positions in the roll-up carry independent evidence -- the verdict sentence for auditing, the Mechanisms cited field for citing.

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

**No-Finding Declaration format -- required at all five enumerated site types:**

```
NO FINDING -- [label]
Checked:     [what was reviewed -- specific entities, fields, roles, privileges, or configuration elements]
Confirmed:   [what configuration state was confirmed absent -- the specific privilege, rule, or mechanism that would enable the threat]
Conclusion:  [stated outcome -- the path is closed because: specific structural fact]
```

**Required site types (all five require the complete three-field format):**

1. **NOT POSSIBLE verdicts** in the escalation vector mini-blocks
2. **Sharing rule clean verdict** per role per entity
3. **Team no-dependency verdict** per entity
4. **Escalation no-path** per role per entity (2e)
5. **Gap-free entity closure** (ENTITY CLOSURE where Gaps logged = NONE)

**Two-of-three-field formats are explicitly prohibited at all five site types.** Bare negatives ("NOT POSSIBLE", "none found", "NONE") do not satisfy the standard at any site.

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
- When a sensitive field is correctly protected: use No-Finding Declaration format inline

**2c -- Sharing rule audit:**

| Rule Name | Trigger | Access Granted | Recipient | Verdict: Expected / Conflict-[G-##] |
|-----------|---------|----------------|-----------|-------------------------------------|

Per-role sharing rule declarations (required for every role in 2a -- site type 2):

For expansion: "[Role] on [Entity]: sharing rules expand access -- [rule name], see G-##."

For no expansion (three-field format required -- two-of-three-field not permitted):
```
NO FINDING -- Sharing rules for [Role] on [Entity]
Checked:     All criteria-based sharing rules targeting [Entity] with [Role] as recipient; all manual sharing grants; owner team expansion rules applicable to [Entity]
Confirmed:   No criteria-based or manual sharing rule expands [Role] access beyond OWD + security role scope; [specific rule types checked and found absent]
Conclusion:  [Role] access on [Entity] bounded by [OWD level] + security role privilege; sharing vector closed for this role
```

**2d -- Team membership dependency:**

For any role with team-dependent access: "Users in [Role] not in [Team] cannot access [record type] because [OWD+scope]. Team controlled by [mechanism]. Self-addition [possible / not possible]: [reason]. [If possible and unintended: assign G-##.]"

If no team dependency (site type 3 -- three-field format required):
```
NO FINDING -- Team dependency for [Entity]
Checked:     OWD setting for [Entity]; whether any role in 2a holds access only via team membership; team-owned record scope in 2a matrix; access team grants applicable to [Entity]
Confirmed:   No role requires team membership to access [Entity]; no owner team record scope in the 2a matrix; no access team provides the only path to [Entity] records for any role
Conclusion:  [Entity] access governed by security role + OWD scope for all roles; no team dependency gap on this entity
```

**2e -- Entity-level escalation check:**

For each role in 2a with W, D, or A:

Found path: assign G-## (ESCALATION-PATH). Chain: `[Role] -> [action on [Entity]] -> [elevated access reached]`

No path (site type 4 -- three-field format required per role):
```
NO FINDING -- Escalation from [Role] on [Entity]
Checked:     Assign privilege on [Entity] (present/absent); record ownership transfer effect on [Role] scope under OWD [setting]; Share privilege enabling sharing rule creation via Write; field write paths to SystemUser.BusinessUnit or security role assignment fields
Confirmed:   No operation available to [Role] on [Entity] enables reaching a higher privilege scope; no writable field modifies role or BU assignment
Conclusion:  [Role] cannot escalate from [Entity] because [specific structural reason per mechanism]
```

---

### ENTITY CLOSURE: [Entity Name]

```
Operations reviewed:       [List each operation (C/R/W/D/A) audited per role]
Sensitive fields confirmed: [List each sensitive field reviewed]
Gaps logged this entity:   [G-## list / NONE]
Sharing rule verdicts:     [N of N roles received three-field declarations (finding or No-Finding): YES]
Escalation checked:        [Roles with W/D/A that received three-field declarations: list]
Status:                    CLOSED
```

Gap-free closure (site type 5 -- three-field format required when Gaps logged = NONE):
```
NO FINDING -- [Entity Name] security review
Checked:     Operations per role: [list]; Sensitive fields: [list]; Sharing rules per role: [list]; Escalation per W/D/A role: [list]
Confirmed:   No MISSING-FLS, no SHARING-CONFLICT, no TEAM-GAP, no ESCALATION-PATH found; items confirmed absent: [enumerate]
Conclusion:  [Entity Name] has no security gaps in this trace; all access bounded by [OWD + security role + FLS]
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
| Every gap-free entity has a three-field No-Finding closure (site type 5) | YES / NO |
| Every role received a three-field sharing rule declaration per entity (site type 2) | YES / NO |
| Every W/D/A role received a three-field escalation declaration per entity (site type 4) | YES / NO |
| Every team no-dependency confirmation uses three-field format (site type 3) | YES / NO |
| No declaration at any site uses a two-of-three-field format | YES / NO |

**PHASE 2 COMPLETE: [YES / NO]**

---

## PHASE 3 -- ESCALATION VECTOR ANALYSIS (organized by Write-capable role)

For each role marked Write-Capable = YES in Phase 1b, complete the following sequence in order: (1) COMMITMENT DECLARATION, (2) five vector mini-blocks, (3) ESCALATION ROLL-UP. Do not begin the vector mini-blocks until the COMMITMENT DECLARATION is written.

**Structural Basis column content exclusivity rule (applies to every NOT POSSIBLE row in every vector mini-block):**

The `Structural Basis` cell holds exactly one structural fact sentence per NOT POSSIBLE row.

- **Permitted:** One structural fact sentence -- the specific privilege confirmed absent or the platform constraint that closes the vector. Nothing else.
- **Prohibited in this cell:** Verdict language ("NOT POSSIBLE", "Assumption Confirmed"). Declaration tracing ("confirms assumption", "per commitment"). Evidence prose (analysis narrative). Conditional language. Placeholder text.
- **POSSIBLE rows:** Cell must contain exactly `N/A -- G-##`. No other content.
- **A cell containing a structural fact mixed with any prohibited content type fails the exclusivity rule.**

---

### COMMITMENT DECLARATION: [Role Name]

Before analyzing escalation vectors for [Role Name], I declare the structural assumptions under which NOT POSSIBLE verdicts will be issued. Each vector mini-block below will open with one of these assumptions restated as the inertia frame. Every NOT POSSIBLE verdict must trace to its named assumption here.

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
| [State the specific privilege checked and configuration reviewed] | POSSIBLE / NOT POSSIBLE | [One structural fact only; no verdict language; no declaration tracing; POSSIBLE = N/A -- G-##] |

**Verdict statement (three-field format -- site type 1):**

```
NO FINDING -- Sharing rule creation, [Role Name]
Checked:     [specific privilege checked -- e.g., Share privilege on all entities in the entity set; admin delegation status]
Confirmed:   [what was confirmed absent -- e.g., no Share privilege in role definition; no delegation grant]
Conclusion:  [path closed because: structural fact confirming the declared assumption]
```

OR: `POSSIBLE -- Assumption Refuted: G-##`

---

#### Vector 2: Team self-injection

> **Inertia Frame (from COMMITMENT DECLARATION):** [Restate the Assumption for this vector exactly as declared above.]

| Evidence | Verdict | Structural Basis |
|----------|---------|------------------|
| [State the team types and membership privileges reviewed] | POSSIBLE / NOT POSSIBLE | [One structural fact only; no verdict language; no declaration tracing; POSSIBLE = N/A -- G-##] |

**Verdict statement (three-field format -- site type 1):**

```
NO FINDING -- Team self-injection, [Role Name]
Checked:     [team types checked -- owner teams and access teams; membership privilege reviewed]
Confirmed:   [what confirmed absent -- e.g., owner team membership requires System Admin; access teams do not grant owner scope]
Conclusion:  [path closed because: structural fact confirming the declared assumption]
```

OR: `POSSIBLE -- Assumption Refuted: G-##`

---

#### Vector 3: Field-value escalation

> **Inertia Frame (from COMMITMENT DECLARATION):** [Restate the Assumption for this vector exactly as declared above.]

| Evidence | Verdict | Structural Basis |
|----------|---------|------------------|
| [State the fields and FLS profiles reviewed] | POSSIBLE / NOT POSSIBLE | [One structural fact only; no verdict language; no declaration tracing; POSSIBLE = N/A -- G-##] |

**Verdict statement (three-field format -- site type 1):**

```
NO FINDING -- Field-value escalation, [Role Name]
Checked:     [specific fields reviewed -- e.g., SystemUser.BusinessUnit, SystemUser.SecurityRoles; FLS profiles checked for each; custom fields in entity set audited for role/BU mapping]
Confirmed:   [what confirmed absent -- e.g., FLS Profile 'X' denies write on SystemUser.BusinessUnit; no custom field maps to security role assignment]
Conclusion:  [path closed because: structural fact confirming the declared assumption]
```

OR: `POSSIBLE -- Assumption Refuted: G-##`

---

#### Vector 4: Role hierarchy traversal

> **Inertia Frame (from COMMITMENT DECLARATION):** [Restate the Assumption for this vector exactly as declared above.]

| Evidence | Verdict | Structural Basis |
|----------|---------|------------------|
| [State whether hierarchy is enabled and ancestors reviewed] | POSSIBLE / NOT POSSIBLE | [One structural fact only; no verdict language; no declaration tracing; POSSIBLE = N/A -- G-##] |

**Verdict statement (three-field format -- site type 1):**

```
NO FINDING -- Role hierarchy traversal, [Role Name]
Checked:     [hierarchy enabled/disabled; ancestor roles listed with their scopes; highest ancestor access level confirmed]
Confirmed:   [what confirmed -- e.g., all ancestors scoped BU-only; no ancestor holds Org scope on any entity in the trace]
Conclusion:  [path closed because: structural fact confirming the declared assumption]
```

OR: `POSSIBLE -- Assumption Refuted: G-##`

---

#### Vector 5: Record ownership transfer

> **Inertia Frame (from COMMITMENT DECLARATION):** [Restate the Assumption for this vector exactly as declared above.]

| Evidence | Verdict | Structural Basis |
|----------|---------|------------------|
| [State whether Assign is held and OWD behavior reviewed] | POSSIBLE / NOT POSSIBLE | [One structural fact only; no verdict language; no declaration tracing; POSSIBLE = N/A -- G-##] |

**Verdict statement (three-field format -- site type 1):**

```
NO FINDING -- Record ownership transfer, [Role Name]
Checked:     [Assign privilege on each entity (present/absent); OWD behavior under transferred ownership; sharing rule effect on transferred records]
Confirmed:   [what confirmed -- e.g., Assign not held; OWD Private means transfer removes record from this role's User scope; no sharing rule re-grants access]
Conclusion:  [path closed because: structural fact confirming the declared assumption]
```

OR: `POSSIBLE -- Assumption Refuted: G-##`

---

### ESCALATION ROLL-UP: [Role Name]

```
Vectors assessed:      5 (sharing rule creation, team self-injection, field-value escalation, role hierarchy traversal, record ownership transfer)
POSSIBLE count:        [count / NONE]
NOT POSSIBLE count:    [count]
Declaration honored:   [count / 5 -- number of NOT POSSIBLE verdicts that confirm a prior declared assumption]
Mechanisms cited:
  [FIELD INSTRUCTION: For each NOT POSSIBLE vector, restate the structural fact from the Structural Basis
   cell inline by vector name. Do not write "see table above", "mechanisms cited in Phase 3",
   "see vectors above", "as documented above", or any equivalent back-reference.
   Back-references to the vector mini-blocks are not permitted in this field.
   Each line must be self-contained and auditable without consulting the vector mini-blocks:
   - Sharing rule creation:    [structural fact restated in full]
   - Team self-injection:      [structural fact restated in full]
   - Field-value escalation:   [structural fact restated in full]
   - Role hierarchy traversal: [structural fact restated in full]
   - Record ownership transfer:[structural fact restated in full]
   POSSIBLE vectors: "POSSIBLE -- G-##"]
Composite verdict:
  [FIELD INSTRUCTION: Name each NOT POSSIBLE vector's closing mechanism type inline in this sentence.
   Do not write only a count ("5 vectors assessed, 0 POSSIBLE"). Do not delegate to Mechanisms cited.
   Format: "no escalation path from [Role Name]: sharing rule creation -- [mechanism type, e.g., no Share
   privilege]; team self-injection -- [mechanism type, e.g., no owner team membership privilege];
   field-value escalation -- [mechanism type, e.g., FLS denies write on targeted fields]; role hierarchy
   traversal -- [mechanism type, e.g., BU-only ancestors]; record ownership transfer -- [mechanism type,
   e.g., Assign not held]."
   If any vector is POSSIBLE: list those as "ESCALATION PATHS: G-##" in the sentence.
   A count-only sentence does not pass this field's requirement.]
```

Roll-up rules:
- Mechanisms cited restates each structural fact inline per vector name. "See vectors above", "mechanisms cited in analysis", or any back-reference is explicitly prohibited and does not pass.
- Composite verdict names each NOT POSSIBLE vector's mechanism type inline in the verdict sentence -- counts alone do not pass.
- Declaration honored must equal NOT POSSIBLE count. Mismatch means a NOT POSSIBLE verdict lacks a prior declared assumption -- identify which vector and add the declaration.

---

*(Repeat COMMITMENT DECLARATION + five vector mini-blocks + ESCALATION ROLL-UP for each Write-capable role.)*

---

## PHASE 3 GATE

| Check | Answer |
|-------|--------|
| Every Write-capable role has a COMMITMENT DECLARATION before its vectors | YES / NO |
| Every vector mini-block restates the inertia frame from the COMMITMENT DECLARATION | YES / NO |
| Every NOT POSSIBLE verdict uses all three fields (Checked / Confirmed / Conclusion) -- site type 1 | YES / NO |
| No NOT POSSIBLE verdict uses only two of three fields | YES / NO |
| Every NOT POSSIBLE verdict traces to a named assumption in the COMMITMENT DECLARATION | YES / NO |
| Every Structural Basis cell holds one structural fact only -- no verdict language, no declaration tracing, no evidence prose | YES / NO |
| Every POSSIBLE verdict logs G-## | YES / NO |
| Every Write-capable role has an ESCALATION ROLL-UP | YES / NO |
| Every Mechanisms cited line restates its structural fact inline -- zero back-references ("see table", "as documented", "mechanisms cited above") | YES / NO |
| Composite verdict sentence names mechanism type per NOT POSSIBLE vector inline -- not a count-only sentence | YES / NO |
| Declaration honored count equals NOT POSSIBLE count in every roll-up | YES / NO |

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

- COMMITMENT DECLARATION block precedes the vector mini-blocks for every Write-capable role (C-20)
- Each vector mini-block restates the inertia frame from the COMMITMENT DECLARATION (C-22)
- Three-field No-Finding Declaration format (Checked / Confirmed / Conclusion) is required at all five enumerated site types; two-of-three-field formats explicitly prohibited (C-23, C-26)
- Structural Basis cell holds one structural fact only -- no verdict language, no declaration tracing, no evidence prose; mixed-content cells fail the exclusivity rule (C-21, C-25)
- ESCALATION ROLL-UP Mechanisms cited field restates each structural fact inline; back-references ("see table above", "mechanisms cited above", "as documented") are explicitly prohibited by name (C-24, C-27)
- ESCALATION ROLL-UP Composite verdict sentence names each NOT POSSIBLE vector's mechanism type inline -- counts alone do not pass (C-28)
- ENTITY CLOSURE blocks appear after every entity section regardless of gap state (C-16)
- Every G-## in the Security Gap Log has a 4a remediation entry (C-08)
