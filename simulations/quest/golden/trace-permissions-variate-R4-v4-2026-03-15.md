# trace-permissions Variate -- Round 4 (Rubric v4)
**Date:** 2026-03-15
**Rubric:** v4 (C-01 through C-20)
**Round note:** R3-v3 best performers: V-01 (multi-marker system, 97.5) and V-02 (enforcement-first + section reactivation, 97.9). C-18 was PARTIAL on both -- V-01's Correction column said "correct before advancing" without specifying the exact repair; V-02 used the same phrasing in section banners. C-20 was PARTIAL on V-01 -- enforcement rules appeared inside a named section after the session header, not as the literal first output. This round closes both residual gaps: V-01 is upgraded with explicit domain-typed corrections (C-17 + C-18); V-02 is upgraded so that enforcement rules precede the document's first section header rather than appearing inside a named section (C-20 strict); V-03 tests whether gate-level imperative corrections achieve C-18 without a preamble table; V-04 and V-05 combine.

**Target criteria focus:** C-17 (per-domain typed marker coverage -- five domains, one distinct named marker each: scope / verdict / evidence / field security / gap-conflict), C-18 (correction-coupled marker definitions -- trigger condition + exact repair action, not just "correct before advancing"), C-19 (section-open rule reactivation -- active markers re-declared at the start of at least two distinct sections beyond the document opening), C-20 (enforcement-first declaration -- enforcement rules precede all entities and operations in document order; any entity or operation name before the rules fail this criterion).

---

## Round 4 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format -- 5-domain correction table (Domain / Trigger / Correction columns) | R3-V-01 had three columns: Marker / Trigger Rule / Action Required. Action Required said "correct before advancing" for all markers -- generic enough to score PARTIAL on C-18. This variation adds a Domain column (satisfying C-17 by labeling the failure domain) and rewrites the Correction column to specify the exact action: which token to substitute, which format to adopt, which register row to add. A writer who sees SCOPE-FAIL has no judgment to exercise -- the Correction column names the exact text to produce. |
| V-02 | Lifecycle emphasis -- enforcement rules as position-zero output (before any section header) + section-open marker banners at every stage boundary | R3-V-02 declared enforcement rules inside an "ENFORCEMENT DECLARATION" section that followed the session header. That section still named entities (via the gap register's category list) before the rules were complete, leaving a narrow C-20 gap. This variation pushes the rules above all section markup -- they appear as the prompt's first prose lines, with no section header between the session header and the first enforcement rule. Section-open banners ([Active markers this stage: ...]) then appear at every stage boundary, satisfying C-19 by restating active markers at multiple distinct sections beyond the opening. |
| V-03 | Phrasing register -- gate-level imperative correction commands ("You cannot advance past this gate until...") embedded at each check, not in a preamble table | C-18 requires corrections to be specified in the marker definition. An alternative structural path: embed the correction as a hard-stop imperative at the gate itself, so the correction appears at the moment the failure condition could arise rather than only in a preamble the model may not re-consult. This tests whether correction-coupling at the gate level produces equivalent C-18 compliance to correction-coupling in a preamble table. |
| V-04 | Combined: Output format + Lifecycle emphasis (C-17 + C-18 + C-19 + C-20) | V-01 satisfies C-17 + C-18 via a correction-specific domain table; V-02 satisfies C-19 + C-20 via enforcement-first position + section banners. Combining them should produce full satisfaction of all four new criteria: the 5-domain correction table appears before any section header (C-20), each section carries a reactivation banner (C-19), the table has distinct domain markers (C-17), and each correction is exact (C-18). |
| V-05 | Combined: V-04 base + Role sequence (ascending privilege: Basic User -> CS Representative -> Security Expert -> System Administrator) + Inertia framing (the easy over-grant temptation named at each tier boundary) | Ascending role order turns each tier transition into an explicit least-privilege gate: "what does this tier add, and is each addition justified?" At each tier boundary the prompt names the inertia temptation (the easy over-grant path) and requires the correction action to explicitly refute it using the Evidence template. Tests whether ascending sequence + inertia naming strengthens C-07 (least-privilege) and C-09 (attack scenario) while preserving all four new criteria from V-04. |

---

## V-01 -- Output Format: 5-Domain Correction-Specific Marker Table

**Axis:** Output format -- a 5-domain enforcement table with Domain / Trigger / Correction columns, where each Correction cell specifies the exact repair action
**Hypothesis:** Upgrading the R3-V-01 Action Required column to a domain-labeled Correction column with specific repair instructions closes C-17 (one named marker per domain) and C-18 (correction coupled to the trigger, not just "correct before advancing"). The test is whether specifying the exact correction action -- which token to use, which three-part line to write, which register row to add -- produces a qualitatively different trace from one that merely says "correct this before advancing."

---

You are running a permissions trace signal for: {{topic}}

---

## ENFORCEMENT SYSTEM -- read before producing any output

Five domain markers are active in this trace. Each fires inline at the exact point of violation -- not in a summary, not at the end. The Correction column specifies exactly what to produce before advancing; it is not a suggestion.

| Marker | Domain | Trigger (when it fires) | Correction (produce this before advancing) |
|--------|--------|------------------------|---------------------------------------------|
| `SCOPE-FAIL` | Record Access Scope | Any Record Scope cell contains a phrase other than a lexicon token (e.g., "appropriate records," "all relevant cases," "permitted access") | Replace the phrase with exactly one token: `Org` / `BU` / `Parent-Child BU` / `Team:[name]` (substitute actual team name) / `User` / `Sharing:[rule name]` (substitute actual rule name). The corrected token must be present in the cell. Do not write the next table row. |
| `VERDICT-FAIL` | Role Decisions & Gate Results | A security gate verdict appears without naming the specific roles, rules, or objects inspected (e.g., "no escalation found" with no per-role record) | List each inspected item: "[Role / Rule / Object] -- [result]." Replace the bare verdict with this list. Do not advance to the next gate. |
| `EVIDENCE-REQUIRED` | Source Citations | A gate answer lacks the three-part Evidence line: "I checked [X] -- [result] because [Y]" | Write: "I checked [named objects] -- [result] because [specific structural reason]." All three parts are mandatory: named objects (X), result, structural reason (Y). A line missing any part does not clear this marker. Do not advance to the next section. |
| `FLS-FAIL` | Field-Level Security | A sensitive field (PII / Financial / Health / Credential / Internal-Audit) is listed without explicit confirmation of whether a field security profile governs it | State "FLS Profile: [profile name]" or "FLS Profile: NONE" on that row. If NONE: add an FLS-EXPOSURE row to the Gap Register immediately with Severity = CRITICAL and Exact Fix naming the profile to create, its location, and the roles to include. Do not list the next field. |
| `GAP-FAIL` | Gap & Conflict Detection | A gap, conflict, or access risk is identified in analysis but no typed register row is present before the next analysis line | Add a typed row: Category / Entity / Field (if FLS) / Role / Severity / Exact Fix. Severity: CRITICAL / HIGH / MEDIUM -- not blank. Exact Fix: name the specific configuration object (security role, field security profile, sharing rule, OWD setting) and its post-fix state. "Tighten permissions" does not qualify. Do not write the next analysis line. |

A trace that ends with zero markers triggered has never tested whether its rules were applied.

---

## SCOPE LEXICON (locked)

| Token | Meaning |
|-------|---------|
| `Org` | All records in the organization |
| `BU` | Records owned by users in the same business unit |
| `Parent-Child BU` | Records owned by users in the same BU and all child BUs |
| `Team:[name]` | Records owned by or shared to the named team |
| `User` | Only the user's own records |
| `Sharing:[rule name]` | Records accessible via the named sharing rule |

---

## GAP REGISTER -- pre-committed (do not populate now; return after Stage 4)

Categories are locked. Do not introduce a new category after this declaration.

| # | Category | Entity | Field (if FLS) | Role | Severity | Exact Fix |
|---|----------|--------|----------------|------|----------|-----------|

Categories: FLS-EXPOSURE / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-CASCADE / OWD-MISMATCH
Severity: CRITICAL / HIGH / MEDIUM. Exact Fix: name the configuration object and post-fix state.

---

## STAGE 1 -- INVENTORY

You are a Dataverse security architect.

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) |
|--------|-----------------|-----------------------------------|

For each High-sensitivity entity: if the OWD is broader than the sensitivity warrants, write `OWD-MISMATCH -- [Entity] -- OWD: [token]` inline and add to Gap Register (GAP-FAIL if deferred).

**1b -- Operation-role matrix (one table per entity):**

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|--------|------|-------|--------|--------|--------------|

Values: YES / NO / CONDITIONAL (state condition). Record Scope: SCOPE LEXICON tokens only. SCOPE-FAIL inline for any non-token entry -- apply the Correction column before the next row. Include every role with any privilege including read-only.

**1c -- Field-level security:**

For each entity: list every field with sensitivity >= Medium.

| Entity | Field | Sensitivity | FLS Profile? | Profile Name | Roles: Read | Roles: Write |
|--------|-------|-------------|-------------|--------------|-------------|--------------|

FLS-FAIL inline if profile status is not explicitly confirmed on a row. If FLS Profile? = NO: apply the FLS-FAIL correction (add FLS-EXPOSURE to register) before listing the next field.
For entities with no sensitive fields: "Confirmed: [Entity] has no fields with sensitivity >= Medium. Fields reviewed: [list]." A blanket statement without the field list triggers FLS-FAIL.

---

## STAGE 2 -- PRIVILEGE ESCALATION

For each role in Stage 1: check all four vectors (team-membership-write / role-assign-write / ownership-reassign / BU-config-write).

**Finding format:** `[Role] -> [Specific privilege name] -> [Elevated access gained]` -- add ESCALATION-PATH to Gap Register (GAP-FAIL if deferred).

**Rule-out format (required per role, not per group):**

> Evidence: I checked [Role] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-category result] because [per-category structural reason].

A verdict without this Evidence line fires EVIDENCE-REQUIRED. A blanket statement covering multiple roles without per-role examination fires VERDICT-FAIL for each unchecked role.

---

## STAGE 3 -- SHARING RULES AND TEAM MEMBERSHIP

**3a -- Sharing rules:**

| Rule Name | Entity | Trigger | Access Opened | Record Scope | Overreach? |
|-----------|--------|---------|---------------|--------------|------------|

Record Scope: SCOPE LEXICON tokens only. SCOPE-FAIL inline for any prose entry.
Overreach? = YES: add SHARING-CONFLICT to Gap Register (GAP-FAIL if deferred).
If no rules exist: "Evidence: I checked sharing rules for [entity list] -- no active rules found because [confirmation of check]." A blanket "no sharing rules" without named entities fires VERDICT-FAIL.

**3b -- Team membership:**

For each team-scoped role:
> Evidence: I checked team [name] membership control -- [mechanism]; self-addition is [possible / impossible] because [specific constraint].

A statement without this format fires EVIDENCE-REQUIRED. Uncontrolled membership or possible self-addition: add TEAM-GAP to Gap Register (GAP-FAIL if deferred).

---

## STAGE 4 -- CROSS-ENTITY CASCADE AND ROLE ANALYSIS

**4a -- Cross-entity cascade:**

Identify the highest-sensitivity entity from Stage 1. Trace at least two relationship hops:

`[Role] -> [Entity A: operation, Record Scope: <token>] -> [Relationship type + cascade: Parental / Referential / None] -> [Entity B: operation, Record Scope: <token>] -> [cascade behavior] -> [Entity C: operation, Record Scope: <token>]`

SCOPE-FAIL at each hop for any non-token scope cell. At each hop: intentional or emergent? Emergent access to a High-sensitivity entity: GAP-FAIL until CROSS-CASCADE row is in register.

**4b -- Stock role assessment (Customer Service Representative and Dataverse Security Expert -- both required, distinct):**

For each:
> Evidence: I checked [Stock Role] default privileges against {{topic}} -- [result] because [specific privilege comparison].

EVIDENCE-REQUIRED if this format is omitted. A merged summary of both roles fails.

**4c -- Least-privilege scoring:**

| Role | Persona | Excess Privileges | LP Score (0-10) | Over-Privileged? | Reduction Required |
|------|---------|-------------------|-----------------|------------------|--------------------|

LP Score < 7: name the specific privilege to reduce and the target scope. "Restrict access" is not a specific reduction.

**4d -- Attack scenario (required if any ESCALATION-PATH in Gap Register):**

Step-by-step: `Starting role -> Action sequence -> Gained access`. Abstract risk statements ("this could allow elevation") do not satisfy this section.

---

Now return to the GAP REGISTER and fill it in completely. Every Exact Fix must name the specific configuration object and post-fix state.

---

## V-02 -- Lifecycle Emphasis: Enforcement-First Position + Section-Open Reactivation Banners

**Axis:** Lifecycle emphasis -- enforcement rules appear as position-zero prose (before any section header or entity name); each stage boundary opens with a marker reactivation banner
**Hypothesis:** R3-V-02 placed enforcement rules in a named section ("ENFORCEMENT DECLARATION") that followed the session header. That section declared gap register categories -- which are themselves entity-class names -- before the rules were fully stated, leaving a narrow C-20 failure path. This variation places the four enforcement rules as the document's first prose lines, below the session header and above the first section marker. No section label, entity name, or gap category appears before Rule E-4 is stated. Section-open banners at every stage boundary satisfy C-19 by re-declaring active markers at stages 1 through 4 -- each independently beyond the document's opening declaration.

---

You are running a permissions trace signal for: {{topic}}

Rule E-1 (Record Access Scope domain): Every Record Scope cell uses exactly one token from the SCOPE LEXICON. A non-token entry fires `SCOPE-FAIL` -- replace with a valid token before the next row.

Rule E-2 (Role Decisions & Gate Results domain): Every security gate verdict carries an Evidence line: "I checked [named objects] -- [result] because [reason]." A verdict without this line fires `EVIDENCE-REQUIRED` -- write the three-part line before the next gate.

Rule E-3 (Field-Level Security domain): Every sensitive field has its FLS profile status explicitly confirmed before the next field is listed. Missing confirmation fires `FLS-FAIL` -- state "FLS Profile: [name or NONE]" before continuing. If NONE: add FLS-EXPOSURE to the Gap Register immediately.

Rule E-4 (Gap & Conflict Detection domain): Every gap is added to the register at the moment of identification. A gap identified but not yet in the register fires `GAP-FAIL` -- add the typed row before the next analysis line.

These rules govern every section below. A trace that reaches its end with zero markers triggered has never tested whether the rules were applied.

---

**SCOPE LEXICON (locked):** `Org` / `BU` / `Parent-Child BU` / `Team:[name]` / `User` / `Sharing:[rule name]`

**GAP REGISTER -- add rows as gaps are found, not at the end.**

| # | Gap Type | Entity | Field (if FLS) | Role | Severity | Exact Fix |
|---|----------|--------|----------------|------|----------|-----------|

Gap types: FLS-EXPOSURE / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-CASCADE / OWD-MISMATCH
Severity: CRITICAL / HIGH / MEDIUM. Exact Fix: name the configuration object and post-fix state.

---

## STAGE 1 -- INVENTORY
**[Active markers this stage: SCOPE-FAIL (E-1) | FLS-FAIL (E-3) | GAP-FAIL (E-4)]**

You are a Dataverse security architect.

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) |
|--------|-----------------|-----------------------------------|

**1b -- Operation-role matrix (one table per entity):**

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|--------|------|-------|--------|--------|--------------|

E-1: SCOPE-FAIL inline for any non-token scope cell. Correct before the next row. Include all roles with any privilege.

**1c -- Field-level security:**

| Entity | Field | Sensitivity | FLS Profile? | Profile Name | Roles: Read | Roles: Write |
|--------|-------|-------------|-------------|--------------|-------------|--------------|

E-3: FLS-FAIL inline for any field without explicit profile status. E-4: GAP-FAIL if FLS-EXPOSURE identified but register row not added immediately.
No sensitive fields: "Confirmed: [Entity] -- no fields with sensitivity >= Medium. Reviewed: [list]."

---

## STAGE 2 -- PRIVILEGE ESCALATION
**[Active markers this stage: EVIDENCE-REQUIRED (E-2) | VERDICT-FAIL for blanket statements | GAP-FAIL (E-4)]**

For each role in Stage 1: check team-membership-write / role-assign-write / ownership-reassign / BU-config-write.

Finding: `[Role] -> [Action] -> [Elevated access]` -- add to Gap Register. E-4: add the row before writing the next role check.

Rule-out (required per role): "I checked [Role] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-category result] because [per-category structural reason]."

E-2: any verdict without "I checked [X] -- [result] because [Y]" fires EVIDENCE-REQUIRED. A blanket statement across multiple roles without per-role examination fires VERDICT-FAIL for each unchecked role.

---

## STAGE 3 -- SHARING RULES AND TEAM GAPS
**[Active markers this stage: SCOPE-FAIL (E-1) | EVIDENCE-REQUIRED (E-2) | GAP-FAIL (E-4)]**

**3a -- Sharing rules:**

| Rule Name | Entity | Trigger | Access Opened | Record Scope | Overreach? |
|-----------|--------|---------|---------------|--------------|------------|

E-1 in Record Scope column. No rules: "I checked sharing rules for [entity list] -- no active rules found because [confirmation]." A bare "no rules" without named entities fires VERDICT-FAIL.
Overreach? = YES: add SHARING-CONFLICT to register. E-4.

**3b -- Team membership:**

For each team-scoped role: "I checked team [name] membership control -- [mechanism]; self-addition is [possible / impossible] because [specific constraint]."

E-2: a membership statement without this format fires EVIDENCE-REQUIRED.

---

## STAGE 4 -- CROSS-ENTITY CASCADE AND ROLE ANALYSIS
**[Active markers this stage: SCOPE-FAIL (E-1) | EVIDENCE-REQUIRED (E-2) | GAP-FAIL (E-4)]**

**4a -- Cross-entity cascade:**

Highest-sensitivity entity from Stage 1. Trace at least two hops:

`[Role] -> [Entity A: operation, Record Scope: <token>] -> [Relationship + cascade: Parental / Referential / None] -> [Entity B: operation, Record Scope: <token>] -> [cascade] -> [Entity C: operation, Record Scope: <token>]`

E-1 at each scope cell. At each hop: intentional or emergent? Emergent access to High-sensitivity: GAP-FAIL until CROSS-CASCADE row is in register.

**4b -- Stock role assessment (both named, distinct):**

For each (Customer Service Representative / Dataverse Security Expert):
"I checked [Stock Role] default privileges against {{topic}} -- [result] because [specific comparison]."
E-2: omitting this format fires EVIDENCE-REQUIRED. Merged summary fails.

**4c -- Least-privilege scoring:**

| Role | Persona | Excess Privileges | LP Score (0-10) | Over-Privileged? | Reduction Required |
|------|---------|-------------------|-----------------|------------------|--------------------|

LP Score < 7: name the specific privilege to reduce and the target scope.

**4d -- Attack scenario (if any ESCALATION-PATH in Gap Register):**

Step-by-step: `Starting role -> Action sequence -> Gained access`. Abstract risk statements do not satisfy this section.

---

Now return to the GAP REGISTER and fill it in completely. Every Exact Fix must name the specific configuration object and post-fix state.

---

## V-03 -- Phrasing Register: Gate-Level Imperative Correction Commands

**Axis:** Phrasing register -- each gate carries its own imperative repair instruction written in hard-stop form ("You cannot advance past this gate until..."), embedded at the point of the check rather than in a preamble table
**Hypothesis:** C-18 requires correction actions to be specified in the marker definition. A structurally equivalent path: embed the correction as a hard-stop at each gate. When the failure condition is named alongside the repair instruction at the exact moment the failure could arise, the writer encounters the correction without needing to re-consult the preamble. This variation tests whether gate-level imperative corrections achieve C-18 compliance in the absence of a preamble enforcement table, and whether the imperative phrasing ("You cannot advance") produces stronger structural compliance than the conditional phrasing ("correct before advancing") in prior rounds.

---

You are running a permissions trace signal for: {{topic}}

---

You are a Dataverse security architect. Four enforcement rules govern this trace. Each gate below carries the repair instruction that applies if the rule fires. Read each gate's repair instruction before attempting the gate.

**Active rule summary:**
- Scope rule: Record Scope cells use SCOPE LEXICON tokens only -- `Org` / `BU` / `Parent-Child BU` / `Team:[name]` / `User` / `Sharing:[rule name]`
- Evidence rule: security gate verdicts carry "I checked [X] -- [result] because [Y]"
- FLS rule: sensitive fields have explicit FLS profile status confirmed before the next field
- Gap rule: gaps are added to the register at the moment of identification, not batched

---

**GAP REGISTER -- pre-committed (do not populate now; return after Stage 4)**

| # | Category | Entity | Field (if FLS) | Role | Severity | Exact Fix |
|---|----------|--------|----------------|------|----------|-----------|

Categories: FLS-EXPOSURE / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-CASCADE / OWD-MISMATCH
Severity: CRITICAL / HIGH / MEDIUM. Exact Fix: name the configuration object and post-fix state.

---

## STAGE 1 -- INVENTORY

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) |
|--------|-----------------|-----------------------------------|

**OWD gate:** For each High-sensitivity entity -- is the OWD broader than the sensitivity warrants?
If YES: write `OWD-MISMATCH -- [Entity] -- OWD: [token]` inline. You cannot advance to 1b until an OWD-MISMATCH row is present in the Gap Register for each flagged entity.
If NO: state the justification ("OWD = [token]; compensating control: [FLS / restrictive role scope]").

**1b -- Operation-role matrix (one table per entity):**

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|--------|------|-------|--------|--------|--------------|

**Scope gate (active on every row):** If you write a non-token phrase in Record Scope: you must mark it `SCOPE-FAIL`, replace it with the correct lexicon token, and you cannot advance to the next row.

Include every role with any privilege, including read-only.

**1c -- Field-level security:**

For each entity: list every field with sensitivity >= Medium (PII / Financial / Health / Credential / Internal-Audit).

| Entity | Field | Sensitivity | FLS Profile? | Profile Name | Roles: Read | Roles: Write |
|--------|-------|-------------|-------------|--------------|-------------|--------------|

**FLS gate (active on every field row):** If you list a sensitive field without explicitly stating FLS Profile? (YES with profile name, or NO): you must mark it `FLS-FAIL`, state the FLS status, and you cannot list the next field. If FLS Profile? = NO: you must add an FLS-EXPOSURE row to the Gap Register with Severity = CRITICAL before listing the next field. You cannot advance with an empty Exact Fix on an FLS-EXPOSURE row.

For entities with no sensitive fields: "Confirmed: [Entity] has no fields with sensitivity >= Medium. Fields reviewed: [list]." You cannot write this confirmation without naming the fields reviewed.

---

## STAGE 2 -- PRIVILEGE ESCALATION

For each role in Stage 1: check all four escalation vectors.

**Escalation gate (active per role):**

Check: Does [Role] hold team-membership-write / role-assign-write / ownership-reassign / BU-config-write?

If finding: write `[Role] -> [specific privilege] -> [elevated access gained]`. You must add an ESCALATION-PATH row to the Gap Register before checking the next role. You cannot advance to the next role with the row absent.

If rule-out: write "I checked [Role] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-category result] because [per-category structural reason]." You cannot write a rule-out without this format. If you write a bare "no escalation" for any role: you must mark it `EVIDENCE-REQUIRED`, produce the per-category check, and you cannot advance.

You cannot write a single "no escalation paths found" statement covering all roles. Each role must be checked individually.

---

## STAGE 3 -- SHARING RULES AND TEAM MEMBERSHIP

**3a -- Sharing rules:**

| Rule Name | Entity | Trigger | Access Opened | Record Scope | Overreach? |
|-----------|--------|---------|---------------|--------------|------------|

**Scope gate:** active in Record Scope column. SCOPE-FAIL inline for any non-token entry. You cannot advance to the next row.

**Sharing overreach gate:** For each row where Overreach? = YES: you must add a SHARING-CONFLICT row to the Gap Register before writing the next sharing rule row.

**No-rules gate:** If no active sharing rules exist: you must write "I checked sharing rules for [entity list] -- no active rules found because [confirmation of check]." You cannot write "no sharing rules" without naming the entities checked.

**3b -- Team membership:**

**Team gate (active per team-scoped role):**

For each team-scoped role: you must write "I checked team [name] membership control -- [mechanism]; self-addition is [possible / impossible] because [specific constraint]." You cannot assess team membership without this format. If you write a bare membership statement: you must mark it `EVIDENCE-REQUIRED` and complete the statement before continuing. If self-addition is possible or control is undefined: you must add a TEAM-GAP row to the Gap Register immediately.

---

## STAGE 4 -- CROSS-ENTITY CASCADE AND ROLE ANALYSIS

**4a -- Cross-entity cascade:**

Identify the highest-sensitivity entity from Stage 1. Trace at least two relationship hops:

`[Role] -> [Entity A: operation, Record Scope: <token>] -> [Relationship type + cascade: Parental / Referential / None] -> [Entity B: operation, Record Scope: <token>] -> [cascade] -> [Entity C: operation, Record Scope: <token>]`

**Cascade gate:** At each hop: state intentional or emergent. If emergent access reaches a High-sensitivity entity: you must add a CROSS-CASCADE row to the Gap Register before writing the next hop. You cannot advance.

**4b -- Stock role assessment:**

**Role assessment gate (required for both named roles):**

For each (Customer Service Representative and Dataverse Security Expert): you must write "I checked [role] default privileges against {{topic}} -- [result] because [specific privilege comparison]." You cannot assess a role without this format. A merged summary of both roles fails -- each must appear separately.

**4c -- Least-privilege scoring:**

| Role | Persona | Excess Privileges | LP Score (0-10) | Over-Privileged? | Reduction Required |
|------|---------|-------------------|-----------------|------------------|--------------------|

**LP gate:** For any LP Score < 7: you must name the specific privilege to reduce and the target scope. You cannot leave Reduction Required blank for a score < 7. "Restrict access" is not a specific reduction.

**4d -- Attack scenario (if any ESCALATION-PATH in Gap Register):**

You must write: `Starting role -> Action sequence -> Gained access`. You cannot satisfy this section with abstract language ("this could allow privilege escalation"). The scenario must name the starting role, each action step, and the specific access obtained.

---

**Remediation gate:** For every row in the Gap Register: you must name the specific configuration object in Exact Fix and its post-fix state. You cannot leave Exact Fix as "tighten permissions" or any generic instruction. You cannot mark the trace complete until every row has a specific Exact Fix.

Now return to the GAP REGISTER and fill it in completely.

---

## V-04 -- Combined: C-17 + C-18 + C-19 + C-20 (All Four New Criteria)

**Axis:** Combined output format + lifecycle emphasis -- 5-domain correction table as position-zero output + section-open reactivation banners at every stage boundary
**Hypothesis:** V-01 satisfies C-17 + C-18 via a correction-specific domain table but places the table inside a section after the session header. V-02 satisfies C-19 + C-20 via enforcement-first position + section banners but uses generic "correct before advancing" in the banners. Combining them should satisfy all four criteria simultaneously: the 5-domain correction table appears before any section header (C-20), each stage opens with a marker banner naming the active markers with their domain labels (C-19), the table provides five distinct domain markers (C-17), and each correction specifies the exact repair action (C-18).

---

You are running a permissions trace signal for: {{topic}}

| Marker | Domain | Trigger | Correction (exact action before advancing) |
|--------|--------|---------|---------------------------------------------|
| `SCOPE-FAIL` | Record Access Scope | Record Scope cell contains prose rather than a lexicon token | Replace with exactly one token: `Org` / `BU` / `Parent-Child BU` / `Team:[name]` / `User` / `Sharing:[rule name]`. Do not write the next row. |
| `VERDICT-FAIL` | Role Decisions & Gate Results | Gate verdict names no inspected objects | List each inspected item: "[Role / Rule / Object] -- [result]." Replace the bare verdict. Do not advance to the next gate. |
| `EVIDENCE-REQUIRED` | Source Citations | Gate answer lacks "I checked [X] -- [result] because [Y]" | Write the three-part line: named objects (X), result, structural reason (Y). All three required. Do not advance to the next section. |
| `FLS-FAIL` | Field-Level Security | Sensitive field listed without explicit FLS profile confirmation | State "FLS Profile: [name]" or "FLS Profile: NONE." If NONE: add FLS-EXPOSURE to Gap Register (Severity = CRITICAL, Exact Fix = [profile name to create + roles to include]). Do not list the next field. |
| `GAP-FAIL` | Gap & Conflict Detection | Gap identified but no typed register row present before next analysis line | Add: Category / Entity / Field / Role / Severity / Exact Fix. Severity must be CRITICAL / HIGH / MEDIUM. Exact Fix must name the configuration object and post-fix state. Do not write the next analysis line. |

**SCOPE LEXICON:** `Org` / `BU` / `Parent-Child BU` / `Team:[name]` / `User` / `Sharing:[rule name]`

**GAP REGISTER -- add rows at the moment of identification.**

| # | Category | Entity | Field (if FLS) | Role | Severity | Exact Fix |
|---|----------|--------|----------------|------|----------|-----------|

Categories: FLS-EXPOSURE / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-CASCADE / OWD-MISMATCH

---

## STAGE 1 -- INVENTORY
**[Active: SCOPE-FAIL (Record Access Scope) | FLS-FAIL (Field-Level Security) | GAP-FAIL (Gap & Conflict Detection)]**

You are a Dataverse security architect.

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) |
|--------|-----------------|-----------------------------------|

High-sensitivity entity with OWD broader than sensitivity warrants: `OWD-MISMATCH -- [Entity] -- OWD: [token]` inline, add to register (GAP-FAIL if deferred).

**1b -- Operation-role matrix (one table per entity):**

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|--------|------|-------|--------|--------|--------------|

SCOPE-FAIL correction: replace any non-token scope cell before the next row. Include all roles.

**1c -- Field-level security:**

| Entity | Field | Sensitivity | FLS Profile? | Profile Name | Roles: Read | Roles: Write |
|--------|-------|-------------|-------------|--------------|-------------|--------------|

FLS-FAIL correction: state "FLS Profile: [name or NONE]" before the next field. If NONE: apply the FLS-FAIL correction (add FLS-EXPOSURE row with Severity = CRITICAL, Exact Fix specifying profile name to create and roles).
No sensitive fields: "Confirmed: [Entity] -- no fields with sensitivity >= Medium. Reviewed: [list]."

---

## STAGE 2 -- PRIVILEGE ESCALATION
**[Active: EVIDENCE-REQUIRED (Source Citations) | VERDICT-FAIL for blanket statements | GAP-FAIL (Gap & Conflict Detection)]**

For each role in Stage 1: check team-membership-write / role-assign-write / ownership-reassign / BU-config-write.

Finding: `[Role] -> [Specific privilege] -> [Elevated access]` -- add ESCALATION-PATH to register. GAP-FAIL correction: add row before the next role check.

Rule-out: "I checked [Role] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-category result] because [per-category structural reason]."

EVIDENCE-REQUIRED correction: write the three-part line before the next gate. VERDICT-FAIL correction for blanket statements: produce per-role check before continuing.

---

## STAGE 3 -- SHARING RULES AND TEAM GAPS
**[Active: SCOPE-FAIL (Record Access Scope) | EVIDENCE-REQUIRED (Source Citations) | GAP-FAIL (Gap & Conflict Detection)]**

**3a -- Sharing rules:**

| Rule Name | Entity | Trigger | Access Opened | Record Scope | Overreach? |
|-----------|--------|---------|---------------|--------------|------------|

SCOPE-FAIL correction in Record Scope column: replace before the next row.
Overreach? = YES: add SHARING-CONFLICT to register. GAP-FAIL correction: add before the next row.
No rules: "I checked sharing rules for [entity list] -- no active rules found because [confirmation]." VERDICT-FAIL correction: name entities checked before writing "no rules."

**3b -- Team membership:**

For each team-scoped role: "I checked team [name] membership control -- [mechanism]; self-addition is [possible / impossible] because [specific constraint]."

EVIDENCE-REQUIRED correction: write the three-part statement before continuing.

---

## STAGE 4 -- CROSS-ENTITY CASCADE AND ROLE ANALYSIS
**[Active: SCOPE-FAIL (Record Access Scope) | EVIDENCE-REQUIRED (Source Citations) | GAP-FAIL (Gap & Conflict Detection)]**

**4a -- Cross-entity cascade:**

Highest-sensitivity entity from Stage 1. Trace at least two hops:

`[Role] -> [Entity A: operation, Record Scope: <token>] -> [Relationship + cascade: Parental / Referential / None] -> [Entity B: operation, Record Scope: <token>] -> [cascade] -> [Entity C: operation, Record Scope: <token>]`

SCOPE-FAIL correction at each hop. Emergent access to High-sensitivity: GAP-FAIL correction (add CROSS-CASCADE row before the next hop).

**4b -- Stock role assessment (Customer Service Representative and Dataverse Security Expert -- distinct):**

For each: "I checked [Stock Role] default privileges against {{topic}} -- [result] because [specific comparison]."
EVIDENCE-REQUIRED correction: write the three-part statement before the next role. Merged summary fails.

**4c -- Least-privilege scoring:**

| Role | Persona | Excess Privileges | LP Score (0-10) | Over-Privileged? | Reduction Required |
|------|---------|-------------------|-----------------|------------------|--------------------|

LP Score < 7: name the specific privilege to reduce and target scope.

**4d -- Attack scenario (if any ESCALATION-PATH in register):**

Step-by-step: `Starting role -> Action sequence -> Gained access`. Abstract risk language does not satisfy this section.

---

Now return to the GAP REGISTER and fill it in completely. Every Exact Fix: name the configuration object and post-fix state.

---

## V-05 -- Combined: All Four New Criteria + Ascending Role Sequence + Inertia Framing

**Axis:** V-04 base (C-17 + C-18 + C-19 + C-20) + role sequence (ascending privilege: Basic User -> CS Representative -> Security Expert -> System Administrator) + inertia framing (the easy over-grant path named at each tier boundary)
**Hypothesis:** Ascending role order turns each tier transition into a structural least-privilege gate. At each boundary, the prompt names the inertia temptation -- the easiest over-grant that would make the analysis faster -- and requires the correction action to explicitly refute it using the Evidence template. The combination should strengthen C-07 (least-privilege assessment: transitions force justification of each privilege addition) and C-09 (attack scenario: the ascending trace naturally surfaces the smallest step from a lower tier to a higher privilege). The four new criteria from V-04 remain intact as structural scaffolding.

---

You are running a permissions trace signal for: {{topic}}

| Marker | Domain | Trigger | Correction (exact action before advancing) |
|--------|--------|---------|---------------------------------------------|
| `SCOPE-FAIL` | Record Access Scope | Record Scope cell contains prose rather than a lexicon token | Replace with one token: `Org` / `BU` / `Parent-Child BU` / `Team:[name]` / `User` / `Sharing:[rule name]`. Do not write the next row. |
| `VERDICT-FAIL` | Role Decisions & Gate Results | Gate verdict names no inspected objects | List each item: "[Role / Rule / Object] -- [result]." Replace the bare verdict. Do not advance. |
| `EVIDENCE-REQUIRED` | Source Citations | Gate answer lacks "I checked [X] -- [result] because [Y]" | Write the three-part line: named objects (X), result, structural reason (Y). Do not advance to the next section. |
| `FLS-FAIL` | Field-Level Security | Sensitive field listed without explicit FLS profile confirmation | State "FLS Profile: [name or NONE]." If NONE: add FLS-EXPOSURE row (Severity = CRITICAL, Exact Fix = profile to create + roles). Do not list the next field. |
| `GAP-FAIL` | Gap & Conflict Detection | Gap identified but register row absent before next analysis line | Add: Category / Entity / Field / Role / Severity / Exact Fix. Exact Fix must name the object and post-fix state. Do not write the next analysis line. |

**SCOPE LEXICON:** `Org` / `BU` / `Parent-Child BU` / `Team:[name]` / `User` / `Sharing:[rule name]`

**ROLE SEQUENCE (ascending privilege -- run in this order):**

| Tier | Role | Expected Privilege Ceiling | Inertia Temptation |
|------|------|---------------------------|-------------------|
| T-1 | Basic User | Read-only, User scope | Grant BU scope "because they need visibility" |
| T-2 | Customer Service Representative | Create/Read/Write Cases and related; BU scope | Grant Org scope "because CS needs to see all cases" |
| T-3 | Dataverse Security Expert | Role and permission management; Org scope on config entities | Grant System Admin "because security configuration is complex" |
| T-4 | System Administrator | Full privileges; Org scope | No tier above -- assess whether System Admin is justified at all |

At each tier transition: state whether the privilege addition is justified by the persona's job function, and explicitly refute the Inertia Temptation using the Evidence template.

**GAP REGISTER -- add rows at the moment of identification.**

| # | Category | Entity | Field (if FLS) | Role | Severity | Exact Fix |
|---|----------|--------|----------------|------|----------|-----------|

Categories: FLS-EXPOSURE / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-CASCADE / OWD-MISMATCH

---

## STAGE 1 -- INVENTORY
**[Active: SCOPE-FAIL (Record Access Scope) | FLS-FAIL (Field-Level Security) | GAP-FAIL (Gap & Conflict Detection)]**

You are a Dataverse security architect.

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity (High / Medium / Low) |
|--------|-----------------|-----------------------------------|

High-sensitivity + OWD broader than sensitivity warrants: `OWD-MISMATCH` inline, GAP-FAIL if not registered.

**1b -- Operation-role matrix (one table per entity, roles in ascending tier order T-1 through T-4):**

| Entity: [name] | Role (Tier) | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|-------------|--------|------|-------|--------|--------|--------------|

Roles in order: Basic User (T-1) -> CS Representative (T-2) -> Security Expert (T-3) -> System Admin (T-4).
SCOPE-FAIL correction: replace non-token scope cells before the next row.

**Tier transition gates (write after each tier in the table):**

**T-1 -> T-2 gate:**
> Evidence: I checked CS Representative privileges above Basic User -- additions are [list] because [job function justification].
> Inertia refutation: Granting Org scope to CS Representative because "CS needs to see all cases" is unjustified because [specific constraint: OWD + security role combination restricts to BU / team-scoped sharing rule / case ownership model].

**T-2 -> T-3 gate:**
> Evidence: I checked Security Expert privileges above CS Representative -- additions are [list] because [job function justification].
> Inertia refutation: Granting System Admin to Security Expert because "security configuration is complex" is unjustified because [specific constraint: security configuration requires role management and field permission set access, not full System Admin; the minimal role set is X].

**T-3 -> T-4 gate:**
> Evidence: I checked System Administrator privileges above Security Expert -- additions are [list]. System Admin is [justified / not justified] because [comparison: is there a task in scope that requires privileges only System Admin provides, or does Security Expert scope suffice].

VERDICT-FAIL correction at each gate: produce the per-tier inspection before advancing. EVIDENCE-REQUIRED correction: write the three-part line before advancing.

**1c -- Field-level security:**

| Entity | Field | Sensitivity | FLS Profile? | Profile Name | Roles: Read | Roles: Write |
|--------|-------|-------------|-------------|--------------|-------------|--------------|

FLS-FAIL correction: confirm profile status per field. GAP-FAIL correction: register FLS-EXPOSURE immediately if Profile? = NO.
No sensitive fields: "Confirmed: [Entity] -- no sensitive fields. Reviewed: [list]."

---

## STAGE 2 -- PRIVILEGE ESCALATION
**[Active: EVIDENCE-REQUIRED (Source Citations) | VERDICT-FAIL for blanket statements | GAP-FAIL (Gap & Conflict Detection)]**

For each role in ascending tier order: check team-membership-write / role-assign-write / ownership-reassign / BU-config-write.

Finding: `[Role (Tier)] -> [Specific privilege] -> [Elevated access -- which tier does this reach?]` -- add ESCALATION-PATH to register. GAP-FAIL correction: add row before the next role.

Rule-out: "I checked [Role] for team-membership-write / role-assign-write / ownership-reassign / BU-config-write -- [per-category result] because [per-category structural reason]."

EVIDENCE-REQUIRED correction: write three-part line before next gate. Ascending order benefit: if T-1 can reach T-3 level access, this surfaces as an unexpected tier skip rather than an abstract "escalation path."

---

## STAGE 3 -- SHARING RULES AND TEAM GAPS
**[Active: SCOPE-FAIL (Record Access Scope) | EVIDENCE-REQUIRED (Source Citations) | GAP-FAIL (Gap & Conflict Detection)]**

**3a -- Sharing rules:**

| Rule Name | Entity | Trigger | Access Opened | Record Scope | Intended Tier Ceiling | Overreach? |
|-----------|--------|---------|---------------|--------------|----------------------|------------|

SCOPE-FAIL correction in Record Scope column. Overreach? = YES: GAP-FAIL correction (add SHARING-CONFLICT row).
No rules: "I checked sharing rules for [entity list] -- no active rules found because [confirmation]." VERDICT-FAIL correction: name entities.

**3b -- Team membership:**

For each team-scoped role: "I checked team [name] membership control -- [mechanism]; self-addition is [possible / impossible] because [specific constraint]." EVIDENCE-REQUIRED correction.

---

## STAGE 4 -- CASCADE, ASSESSMENT, AND ATTACK
**[Active: SCOPE-FAIL (Record Access Scope) | EVIDENCE-REQUIRED (Source Citations) | GAP-FAIL (Gap & Conflict Detection)]**

**4a -- Cross-entity cascade (trace from lowest tier that can reach the highest-sensitivity entity):**

Start from T-1 (Basic User). Trace at least two hops:

`[T-1: Basic User] -> [Entity A: operation, Record Scope: <token>] -> [Relationship + cascade] -> [Entity B: operation, Record Scope: <token>] -> [cascade] -> [Entity C: operation, Record Scope: <token>]`

At each hop: intentional or emergent? If T-1 reaches High-sensitivity content that T-2 cannot: this is a tier-inversion finding -- add CROSS-CASCADE to register. GAP-FAIL correction.

**4b -- Stock role contrast (ascending order: CS Representative -> Dataverse Security Expert):**

For each: "I checked [Stock Role] default privileges against {{topic}} -- [result] because [specific comparison]."
EVIDENCE-REQUIRED correction. Distinct observations per role; merged summary fails.

Contrast statement (required): One paragraph naming both roles, noting the privilege delta, and stating whether each delta is justified by the ascending tier model.

**4c -- Least-privilege scoring:**

| Role (Tier) | Persona | Excess Privileges vs Tier Ceiling | LP Score (0-10) | Over-Privileged? | Reduction Required |
|-------------|---------|----------------------------------|-----------------|------------------|--------------------|

LP Score < 7: name the specific privilege to reduce and the target scope. Reduction must reference the tier ceiling -- "reduce to T-2 scope by removing [privilege X]" is a specific reduction.

**4d -- Attack scenario (required if any ESCALATION-PATH in register):**

Use the ascending tier model: show the minimum tier an attacker starts from and the tier they reach.
`Starting tier and role -> Action 1 [specific] -> Action 2 [specific] -> Reached tier / access`.
Abstract risk statements do not satisfy this section.

---

Now return to the GAP REGISTER and fill it in completely. Every Exact Fix: name the configuration object and post-fix state.
