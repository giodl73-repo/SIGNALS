# trace-permissions Variate — Round 4
**Date:** 2026-03-15
**Rubric:** v4 (C-01 through C-18)
**Round note:** R3-V-05 scored 130/130 on v3 (C-01–C-15). This round targets three criteria extracted from that ceiling as v4 additions: C-16 (pre-ceiling INERTIA/DESIGN categorization inventory as a blocking step before any ceiling block), C-17 (whole-output compliance self-check as a submission gate), C-18 (compound block format extended into dual-track remediation with typed DELTA tokens).

**Baseline prompt:** R3-V-05 (inertia framing + multi-marker enforcement + evidence template). All variations preserve R3-V-05's C-01–C-15 scaffold and add one or more of C-16/C-17/C-18.

---

## Round 4 Variation Map

| Variation | Axis | New Criteria | Hypothesis |
|-----------|------|--------------|------------|
| V-01 | Lifecycle emphasis — dedicated Step 0 categorization gate (C-16 isolation) | C-16 | A Step 0 that assigns INERTIA/DESIGN to every permission before Stage 1 opens prevents inline category derivation. When Stage 1 cannot start until Step 0 is complete, the category is structurally an input rather than a conclusion. R3-V-05 labeled inline during analysis — the upgrade is making the inventory a blocking gate. |
| V-02 | Output format — terminal compliance gate table (C-17 isolation) | C-17 | A mandatory five-row verification table after all stages, with the rule "any unchecked item requires revision before submission," converts the output ending from an editorial judgment into a formal verified state. R3-V-05 had a per-inertia-gate audit; C-17 is a different structural layer: whole-output, not section-level. |
| V-03 | Phrasing register — explicit compound block contract in remediation (C-18 isolation) | C-18 | Declaring the compound block contract for remediation explicitly — with typed token names, FORMAT-VIOLATION markers for prose in DELTA rows, and a pre-declared template — prevents the Track A/B distinction from being satisfied in form while breaking block discipline. C-13 applies in analysis; C-18 makes it apply equally in remediation. |
| V-04 | Lifecycle + output format (C-16 + C-17 combined) | C-16, C-17 | Step 0 gates the start; Stage 6 compliance table gates the end. Together they are structural bookends: one prevents inline category derivation, the other prevents premature completion without verifying constraint coverage end-to-end. |
| V-05 | All three axes + inertia framing reinforcement (C-16 + C-17 + C-18) — CEILING | C-16, C-17, C-18 | When Step 0 labels every permission INERTIA/DESIGN before analysis, inertia gates can reference the pre-assigned category rather than discovering it. Remediation compound blocks inherit the same category label and use typed DELTA tokens per track. The compliance gate closes the loop by verifying the chain held end-to-end. The three criteria reinforce rather than operate in separate sections. |

---

## V-01 — Lifecycle Emphasis: Pre-Ceiling Categorization Gate (C-16)

**Axis:** Lifecycle emphasis — dedicated Step 0 assigns INERTIA/DESIGN labels to all permissions before any ceiling or gap analysis begins
**Hypothesis:** R3-V-05 assigned INERTIA/DESIGN inline during analysis sections. This variation adds a blocking Step 0 that produces a complete category table before Stage 1 opens. When the ceiling block instruction says "inherit Category from Step 0 — do not derive inline," the category becomes structurally an input. A Stage 1 block that runs before Step 0 is complete fails the gate.

---

You are running a permissions trace signal for: {{topic}}

---

## STEP 0 — INERTIA/DESIGN CATEGORIZATION INVENTORY

**Complete this step before writing any Stage 1 content. Stage 1 may not open until this step is complete.**

Enumerate every permission element in scope for {{topic}}: OWD settings per entity, role privileges per operation, field security profile presence or absence per sensitive field, sharing rules, team membership controls.

| # | Permission Element | Entity / Scope | Current State | Category | Rationale |
|---|-------------------|---------------|---------------|----------|-----------|
| | OWD for [entity] | [entity] | [access level] | INERTIA / DESIGN | |
| | [Role] privilege on [entity] | [entity] | [privilege set] | INERTIA / DESIGN | |
| | FLS on [entity].[field] | [entity] | [profile name / NONE] | INERTIA / DESIGN | |
| | [Sharing rule name] | [entity] | [access opened] | INERTIA / DESIGN | |
| | [Team] membership control | [team] | [mechanism] | INERTIA / DESIGN | |

**Category definitions:**
- **INERTIA**: Platform default, stock role permission, or never explicitly configured. The organization may not know this state exists. Every Dataverse stock role permission is INERTIA until a deliberate modification is documented.
- **DESIGN**: Explicitly created, modified, or configured. Intent-drift risk — the original decision may no longer match current requirements.

**Gate C-16:** Every permission element in scope must have a Category value before Stage 1 opens. An empty Category cell is a `CATEGORY-INCOMPLETE` marker — write it inline and complete the row before advancing.

**Propagation contract:** In every analysis block and Gap Register row in Stages 1–5, inherit Category from this table. Write `(Category: INERTIA)` or `(Category: DESIGN)` after the permission reference. Do not re-derive the category inline — return to Step 0 if the correct label is uncertain.

---

## ENFORCEMENT RULES

**Write-time markers (active throughout):**
- `SCOPE-FAIL` — Record Scope cell with prose instead of a lexicon token; correct before next row
- `VERDICT-FAIL` — Gate verdict without a named inspection record; add before advancing
- `EVIDENCE-REQUIRED` — Gate answer missing any of: `I checked [X]` / `[result]` / `because [Y]`; complete before advancing
- `FLS-FAIL` — Sensitive field assessed without FLS profile status confirmation; complete before next field
- `GAP-FAIL` — Gap identified but not immediately added to Gap Register; add the row before continuing
- `INERTIA-UNCHECKED` — Inertia gate section ended without an evidence-template refutation; complete before closing the stage
- `CATEGORY-INCOMPLETE` — Stage 1 block references a permission with no Step 0 Category; add the row to Step 0 before continuing

---

## SCOPE LEXICON (locked)

| Token | Meaning |
|-------|---------|
| `Org` | All records in the organization |
| `BU` | Records in the same business unit |
| `Parent-Child BU` | Records in the same BU and all child BUs |
| `Team:[name]` | Records owned by or shared to the named team |
| `User` | Only the user's own records |
| `Sharing:[rule name]` | Records reached via the named sharing rule |

---

**GAP REGISTER — add rows at point of identification.**

| # | Gap Type | Entity | Field (if FLS) | Role | Category (Step 0) | Severity | TR Rule | Exact Fix |
|---|----------|--------|----------------|------|-------------------|----------|---------|-----------|

Gap types: FLS-EXPOSURE / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-CASCADE / OWD-MISMATCH / ELEVATION-UNJUSTIFIED
Category: copy from Step 0 — do not derive here.
Severity: CRITICAL / HIGH / MEDIUM. TR Rule: named trigger rule (not subjective judgment). Exact Fix: configuration object + post-fix state.

---

## STAGE 1 — CEILING ESTABLISHMENT

**Prerequisite: Step 0 is complete. No CATEGORY-INCOMPLETE cells.**

You are a Dataverse security architect. Establish the maximum access level in this permission model.

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity | Category (Step 0) |
|--------|-----------------|-------------|-------------------|

**[Inertia threat I-1: Org OWD because Private + sharing rules is effort]**

For each entity with Sensitivity = High or Medium:

> Gate I-1: Is the OWD more permissive than data sensitivity warrants?
> Evidence: I checked OWD settings for [entity] — [result: Private / BU / Organization] because [data sensitivity / compensating FLS controls / no compensating control exists]. (Category: [Step 0 label])

OWD = Organization with no compensating FLS: INERTIA-UNCHECKED if gate unanswered. Add OWD-MISMATCH to Gap Register with TR Rule: `sensitive entity + OWD = Organization → HIGH`.

**1b — Admin ceiling: operation-role matrix (one table per entity):**

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope | Category (Step 0) |
|----------------|------|--------|------|-------|--------|--------|--------------|-------------------|

SCOPE-FAIL active in Record Scope. Category column: copy from Step 0 — do not derive. Include every role with any privilege.

**[Inertia threat I-2: System Admin because scoping a custom role takes effort]**

> Gate I-2: Does any role use System Administrator when a restricted custom role would suffice?
> Evidence: I checked each role assignment against its persona function — [per-role result] because [function comparison: what the persona needs vs. what System Admin grants beyond that]. (Category per role from Step 0)

System Admin unjustified: INERTIA-UNCHECKED if gate unanswered. ELEVATION-UNJUSTIFIED to Gap Register.

**1c — Role identification:** List every security role. Name every Dataverse stock role (Customer Service Representative, Basic User, System Customizer, System Administrator). Stock roles are INERTIA by definition in Step 0 unless a deliberate modification is documented.

---

## STAGE 2 — CS-FLOOR DELTA

Express CS-floor gaps as structural deltas from the Admin ceiling established in Stage 1.

**CS-floor delta table (one per entity):**

| Entity | Operation | Admin Ceiling | CS Floor | Delta? | Category (Step 0) | Finding |
|--------|-----------|---------------|----------|--------|-------------------|---------|

Delta = YES: use Step 0 category to classify the gap. INERTIA = CS never received the access (nobody granted it). DESIGN = CS was intentionally excluded. Do not re-derive the category.

---

## STAGE 3 — FIELD-LEVEL SECURITY

**[Inertia threat I-3: No FLS because profile creation is overhead]**

For each entity: enumerate every field with sensitivity >= Medium (PII / Financial / Health / Credential / Internal-Audit).

> Gate I-3: Does every sensitive field have a field security profile, or were profiles skipped?
> Evidence: I checked Security > Field Security Profiles for [entity list] — [per-field result: profile [name] / no profile for [field]] because [profiles required by design / FLS not configured]. (Category per field from Step 0)

FLS-FAIL active. INERTIA-UNCHECKED if Gate I-3 unanswered. For each field with no profile: add FLS-EXPOSURE to Gap Register (Severity: CRITICAL, TR Rule: `sensitive field + NO-PROFILE → CRITICAL`).

| Entity | Field | Sensitivity | FLS Profile? | Profile Name | Roles: Read | Roles: Write | Category (Step 0) |
|--------|-------|-------------|-------------|--------------|-------------|--------------|-------------------|

Entity with no sensitive fields: "Confirmed: [Entity] — no fields with sensitivity >= Medium. Reviewed: [list]."

---

## STAGE 4 — PRIVILEGE ESCALATION AND SHARING RULES

**4a — Escalation (four vectors per role):**

For each role: check team-membership-write / role-assign-write / ownership-reassign / BU-config-write.

Finding: `[Role] (Category: [Step 0 label]) -> [Action] -> [Elevated access]` — add ESCALATION-PATH to Gap Register (GAP-FAIL if deferred).

Rule-out: `Evidence: I checked [role] for [vectors] — [per-category result] because [structural reason].` VERDICT-FAIL for any role not individually named.

**[Inertia threat I-5: Service account with Org scope because least-privilege scoping is complex]**

For each non-human role:
> Gate I-5: Does this service account hold Org scope when a narrower scope would suffice?
> Evidence: I checked [service account role] scope — [token] — because [automation function: what records the account needs, and whether Org scope is necessary or merely convenient]. (Category from Step 0)

Org scope unjustified: INERTIA-UNCHECKED if gate unanswered. ELEVATION-UNJUSTIFIED to Gap Register.

**4b — Sharing rules:**

| Rule Name | Entity | Trigger | Access Opened | Record Scope | Category (Step 0) | Review Date | Overreach? |
|-----------|--------|---------|---------------|--------------|-------------------|-------------|------------|

SCOPE-FAIL active. **[Inertia threat I-4: Sharing rule without review date because proper scoping is slow]**

> Gate I-4: Does any rule reopen access the OWD + role model restricts, or exist without a documented review date?
> Evidence: I checked sharing rules [list or "no rules found"] for [entity list] — [per-rule: access opened vs. OWD scope, review date status] because [rule intent vs. current configuration].

INERTIA-UNCHECKED for rules without review date. Overreach: SHARING-CONFLICT to Gap Register.

**4c — Team membership:** For each team-scoped role:
> Evidence: I checked team [name] membership control — [mechanism]; self-addition [possible / impossible] because [constraint]. (Category: [Step 0 label for membership control])

**4d — Cross-entity cascade:** Highest-sensitivity entity. Trace at least two relationship hops.
`[Role] -> [Entity A: op, Scope] -> [Relationship + cascade: Parental / Referential / None] -> [Entity B: op, Scope] -> [cascade] -> [Entity C: op, Scope]`
SCOPE-FAIL at each hop scope cell. At each hop: intentional or emergent? Emergent access to High-sensitivity: CROSS-CASCADE to Gap Register.

---

## STAGE 5 — ROLE ASSESSMENT

**Customer Service Representative gate:**
> Evidence: I checked CS role access for [entity list, sensitive field list] — [per-item result] because [FLS profile / OWD / role scope].

**Dataverse Security Expert gate:**
> Evidence: I checked expert role privileges beyond CS access — [excess list or NONE] because [comparison to security configuration task scope].

Both roles must appear by Dataverse system name with distinct Evidence-backed observations.

**Least-privilege scoring:**

| Role | Persona | Excess Privileges | LP Score (0-10) | Category (Step 0) | Reduction Required |
|------|---------|-------------------|-----------------|-------------------|--------------------|

LP Score < 7: state specific reduction and target scope.

**Attack scenario (if any ESCALATION-PATH in register):**
`Starting role -> Action sequence -> Gained access.`

**INERTIA-UNCHECKED audit:** Review gates I-1 through I-5. Any gate without a complete Evidence line: complete it now before returning to the Gap Register.

---

Return to GAP REGISTER. Every Category column must match Step 0. Every TR Rule must name the trigger rule. Every Exact Fix must name the configuration object and post-fix state.

---

## V-02 — Output Format: Compliance Submission Gate (C-17)

**Axis:** Output format — a mandatory five-row compliance verification table is the final output element; its status gates whether the output may be declared complete
**Hypothesis:** R3-V-05 ended with a per-inertia-gate INERTIA-UNCHECKED audit — section-level coverage. C-17 is a different structural layer: a whole-output gate with one row per master constraint. The phrase "any unchecked item requires revision before submission" converts the end of the trace from a natural stopping point into a verified state. A trace that ends before this table exists, or before every row is marked PASS, is structurally incomplete.

---

You are running a permissions trace signal for: {{topic}}

---

## PREAMBLE: THE INERTIA THREAT

Permission models accumulate risk through the path of least resistance. Five inertia threats are named at their gates.

| # | Inertia Threat | Gate | Danger |
|---|---------------|------|--------|
| I-1 | Org-level OWD | OWD assessment | All users read all records; FLS becomes sole protection |
| I-2 | System Admin for convenience | Least-privilege assessment | Bypasses OWD, FLS, all role checks |
| I-3 | No FLS profiles | Field-level security | Any role with entity Read sees PII, financial, credential data |
| I-4 | Sharing rule without review date | Sharing rule audit | Access accumulates indefinitely |
| I-5 | Service account with Org scope | Service account assessment | Highest-value escalation target |

An inertia gate not answered with a complete Evidence line is `INERTIA-UNCHECKED` — write inline.

---

## ENFORCEMENT RULES

**Write-time markers:**
- `SCOPE-FAIL` — prose in Record Scope cell; correct before next row
- `VERDICT-FAIL` — gate verdict without named inspection record; add before advancing
- `EVIDENCE-REQUIRED` — Evidence template missing any part; complete before advancing
- `FLS-FAIL` — sensitive field without FLS profile status confirmation; complete before next field
- `GAP-FAIL` — gap not immediately registered; add the row before continuing
- `INERTIA-UNCHECKED` — inertia gate section ended without evidence-template refutation

---

## SCOPE LEXICON (locked)

| Token | Meaning |
|-------|---------|
| `Org` | All records in the organization |
| `BU` | Records in the same business unit |
| `Parent-Child BU` | Records in the same BU and all child BUs |
| `Team:[name]` | Records owned by or shared to the named team |
| `User` | Only the user's own records |
| `Sharing:[rule name]` | Records reached via the named sharing rule |

---

**GAP REGISTER — add rows at point of identification.**

| # | Gap Type | Entity | Field (if FLS) | Role | Category | Severity | TR Rule | Exact Fix |
|---|----------|--------|----------------|------|----------|----------|---------|-----------|

Gap types: FLS-EXPOSURE / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-CASCADE / OWD-MISMATCH
Category: INERTIA / DESIGN. Severity: CRITICAL / HIGH / MEDIUM. TR Rule: named trigger rule.

---

## STAGE 1 — INVENTORY

You are a Dataverse security architect.

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity |
|--------|-----------------|-------------|

**[Gate I-1 active]**
> Gate I-1: Evidence: I checked OWD settings for [entity] — [result] because [data sensitivity / compensating controls / no compensating control].

INERTIA-UNCHECKED if not answered. OWD broader than sensitivity warrants: OWD-MISMATCH to Gap Register.

**1b — Operation-role matrix (one table per entity):**

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|--------|------|-------|--------|--------|--------------|

SCOPE-FAIL active. Include every role with any privilege. Identify each Dataverse stock role by system name.

**1c — Field-level security:**

| Entity | Field | Sensitivity | FLS Profile? | Profile Name | Roles: Read | Roles: Write |
|--------|-------|-------------|-------------|--------------|-------------|--------------|

FLS-FAIL active. Sensitive field without profile: FLS-EXPOSURE to Gap Register (CRITICAL).

**[Gate I-2 active]**
> Gate I-2: Evidence: I checked each role assignment against its persona function — [per-role result] because [function comparison].

---

## STAGE 2 — PRIVILEGE ESCALATION

For each role: check team-membership-write / role-assign-write / ownership-reassign / BU-config-write.

Finding: `[Role] -> [Action] -> [Elevated access]` — GAP-FAIL if not added to register.
Rule-out: `Evidence: I checked [role] for [vectors] — [per-category result] because [structural reason].`

VERDICT-FAIL for blanket statements. EVIDENCE-REQUIRED for missing Evidence line.

**[Gate I-5 active]** For each service/integration account:
> Gate I-5: Evidence: I checked [service account role] scope — [token] — because [automation function and scope necessity].

INERTIA-UNCHECKED if not answered.

---

## STAGE 3 — FIELD-LEVEL SECURITY (INERTIA/DESIGN noted per finding)

**[Gate I-3 active]** For each entity: sensitive fields >= Medium.

| Entity | Field | Sensitivity | FLS Profile? | Profile Name | Roles: Read | Roles: Write | Category |
|--------|-------|-------------|-------------|--------------|-------------|--------------|----------|

> Gate I-3: Evidence: I checked Field Security Profiles for [entity list] — [per-field result] because [profiles configured / skipped].

FLS-FAIL + INERTIA-UNCHECKED if gate unanswered. Note category per field (INERTIA = no profile because nobody created one; DESIGN = profile intentionally omitted).

---

## STAGE 4 — SHARING RULES AND TEAM MEMBERSHIP

**[Gate I-4 active]**

**4a — Sharing rules:**

| Rule Name | Entity | Trigger | Access Opened | Record Scope | Category | Review Date | Overreach? |
|-----------|--------|---------|---------------|--------------|----------|-------------|------------|

> Gate I-4: Evidence: I checked sharing rules [list] for [entity list] — [per-rule result] because [rule intent vs. configuration].

INERTIA-UNCHECKED if not answered. Overreach: SHARING-CONFLICT to Gap Register.

**4b — Team membership:**
> Gate team: Evidence: I checked team [name] membership control — [mechanism]; self-addition [possible / impossible] because [constraint].

**4c — Cross-entity cascade:** Two hops minimum. SCOPE-FAIL at each scope cell. Emergent High-sensitivity access: CROSS-CASCADE to Gap Register.

---

## STAGE 5 — ROLE ASSESSMENT

CS Representative and Security Expert gates (Evidence lines per entity and sensitive field). Least-privilege scoring. Attack scenario if escalation paths found.

| Role | Persona | Inertia Threat Applied? | Excess Privileges | LP Score | Reduction |
|------|---------|------------------------|-------------------|----------|-----------|

INERTIA-UNCHECKED audit: for every gate I-1 through I-5, confirm the Evidence line is complete before Stage 6.

---

Return to GAP REGISTER. All Exact Fix values must name the configuration object and post-fix state.

---

## STAGE 6 — COMPLIANCE SELF-CHECK GATE

**This table must be completed before the output is declared done. It is a submission gate — not a self-review section.**

Verify that every master constraint holds across the full output. This is a whole-output check. Read the actual content above for each row before marking status.

| # | Constraint | What to Verify in This Output | Status |
|---|------------|------------------------------|--------|
| 1 | **C-01/C-03**: All roles use Dataverse system names with Record Scope per entity | Every role row in Stage 1 matrix has a scope token (not prose) for every entity; scope is stated per role per entity, not once per section | [ ] PASS / [ ] FAIL |
| 2 | **C-02**: FLS analyzed for every sensitive entity | Every entity with Sensitivity >= Medium has an FLS block; every sensitive field is named with profile status and per-role access result | [ ] PASS / [ ] FAIL |
| 3 | **C-10/C-11**: Ceiling established first; trigger rule fires at least once | Stage 1 Admin ceiling precedes gap analysis; at least one Gap Register row carries a named TR Rule (not bare severity without a rule name) | [ ] PASS / [ ] FAIL |
| 4 | **C-14/C-15**: Dual remediation tracks; every gap row cites a TR rule | Gap Register contains at least one INERTIA and one DESIGN gap; no severity cell is blank or contains subjective language without a named rule | [ ] PASS / [ ] FAIL |
| 5 | **C-12/C-13**: Stock defaults named as INERTIA baseline; compound block format used in analysis | At least one permission is explicitly identified as a platform default (INERTIA); at least one analysis section uses Admin / CS / DELTA row structure rather than prose narration | [ ] PASS / [ ] FAIL |

**Submission rule:** Any row marked FAIL requires revision of the relevant stage(s) above before this trace is complete. Any unchecked item (`[ ]`) is treated as FAIL until marked. Do not mark PASS without reading the corresponding stage content. A speculative PASS is a `VERDICT-FAIL`.

---

## V-03 — Phrasing Register: Compound Remediation Blocks (C-18)

**Axis:** Phrasing register — explicit compound block contract declared before remediation; FORMAT-VIOLATION marker enforces typed DELTA tokens; prose in DELTA rows is a write-time failure
**Hypothesis:** C-13 requires compound block format in analysis sections. R3-V-05's Gap Register used an "Exact Fix" prose column that satisfies C-08 in form while breaking block discipline. C-18 requires that the same discipline propagates into the dual-track remediation section. This variation makes the compound block contract explicit for remediation, names the typed token forms (`Action: Enable` / `Action: Change`), and activates FORMAT-VIOLATION as a write-time marker — not a post-hoc review flag.

---

You are running a permissions trace signal for: {{topic}}

---

## PREAMBLE: THE INERTIA THREAT

Permission models accumulate risk through the path of least resistance. Five inertia threats are named at their gates.

| # | Inertia Threat | Gate |
|---|---------------|------|
| I-1 | Org-level OWD | OWD assessment |
| I-2 | System Admin for convenience | Least-privilege assessment |
| I-3 | No FLS profiles | Field-level security |
| I-4 | Sharing rule without review date | Sharing rule audit |
| I-5 | Service account with Org scope | Service account assessment |

---

## ENFORCEMENT RULES

**Write-time markers:**
- `SCOPE-FAIL` — prose in Record Scope cell; correct before next row
- `VERDICT-FAIL` — gate verdict without named inspection
- `EVIDENCE-REQUIRED` — Evidence template incomplete
- `FLS-FAIL` — sensitive field without FLS profile confirmation
- `GAP-FAIL` — gap not immediately registered
- `INERTIA-UNCHECKED` — inertia gate not answered before end of section
- `FORMAT-VIOLATION` — DELTA row in a remediation compound block contains prose rather than a typed `Action: Enable` or `Action: Change` token (Stage 5 only; see contract below)

---

## COMPOUND BLOCK CONTRACT

**Analysis sections (Stages 1–4):** Use compound block format for gap findings.

```
| Row   | Content                                                    |
|-------|------------------------------------------------------------|
| Admin | [Admin ceiling state: privilege / scope token / FLS]       |
| CS    | [CS floor state: privilege / scope token / FLS]            |
| DELTA | [gap expressed as a typed row value, not a sentence]       |
```

DELTA row rule in analysis: express the gap as a gap-type token (FLS-EXPOSURE, OWD-MISMATCH, ESCALATION-PATH, SHARING-CONFLICT, CROSS-CASCADE) or a scope token differential. A sentence in an analysis DELTA row is a format violation; write `FORMAT-VIOLATION` and restate as a typed row value.

**Remediation section (Stage 5) — compound block contract mandatory:**

Track A applies to INERTIA gaps (permission was never deliberately configured):

```
| Row   | Content                                                                           |
|-------|-----------------------------------------------------------------------------------|
| Admin | [current Admin ceiling state for this permission]                                 |
| CS    | [current CS floor state]                                                          |
| DELTA | Action: Enable [object] on [role/entity/field] in [solution layer].               |
|       | After fix: [behavioral delta — one sentence]. (First-time configuration)          |
```

Track B applies to DESIGN gaps (permission was explicitly configured but is now incorrect):

```
| Row   | Content                                                                           |
|-------|-----------------------------------------------------------------------------------|
| Admin | [current Admin ceiling state]                                                     |
| CS    | [current CS floor state]                                                          |
| DELTA | Action: Change [setting] on [role/entity/field] in [solution layer]               |
|       | from [current value] to [target value]. This reverses [prior decision].           |
|       | After fix: [behavioral delta — one sentence].                                     |
```

**FORMAT-VIOLATION enforcement (Stage 5):** Any DELTA row that does not begin with `Action: Enable` (Track A) or `Action: Change` (Track B) is a FORMAT-VIOLATION. Write the marker inline before the next block and rewrite the failing DELTA row. Prose text in a Stage 5 DELTA row — such as "Restrict CS access to this field" — is a FORMAT-VIOLATION regardless of whether it is factually correct.

---

## SCOPE LEXICON (locked)

| Token | Meaning |
|-------|---------|
| `Org` | All records in the organization |
| `BU` | Records in the same business unit |
| `Parent-Child BU` | Records in the same BU and all child BUs |
| `Team:[name]` | Records owned by or shared to the named team |
| `User` | Only the user's own records |
| `Sharing:[rule name]` | Records reached via the named sharing rule |

---

**GAP REGISTER — add rows at point of identification.**

| # | Gap Type | Entity | Field (if FLS) | Role | Category | Severity | TR Rule | Track |
|---|----------|--------|----------------|------|----------|----------|---------|-------|

Category: INERTIA / DESIGN (assign at point of finding).
Track: A (INERTIA) / B (DESIGN) — determines compound block type in Stage 5.
TR Rule: named trigger rule.

---

## STAGE 1 — INVENTORY

You are a Dataverse security architect.

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity |
|--------|-----------------|-------------|

**[Gate I-1 active]**
> Gate I-1: Evidence: I checked OWD settings for [entity] — [result] because [reason].

For each OWD-MISMATCH finding, write an analysis compound block:

| Row | Content |
|-----|---------|
| Admin | [entity] OWD: [token] |
| CS | CS floor read scope under this OWD: [token consequence] |
| DELTA | OWD-MISMATCH |

Add to Gap Register. Assign Category (INERTIA if default was never changed; DESIGN if deliberately set broad).

**1b — Operation-role matrix (one per entity):**

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope |
|----------------|------|--------|------|-------|--------|--------|--------------|

SCOPE-FAIL active. Include all roles by Dataverse system name.

**1c — Field-level security:**

**[Gate I-3 active]**

| Entity | Field | Sensitivity | FLS Profile? | Profile Name | Roles: Read | Roles: Write | Category |
|--------|-------|-------------|-------------|--------------|-------------|--------------|----------|

> Gate I-3: Evidence: I checked Field Security Profiles for [entity list] — [per-field result] because [profiles configured / not configured].

For each field with no FLS profile, write an analysis compound block:

| Row | Content |
|-----|---------|
| Admin | [entity].[field] FLS profile: NONE |
| CS | CS Read access to [entity].[field]: UNRESTRICTED (no FLS gate) |
| DELTA | FLS-EXPOSURE |

Add FLS-EXPOSURE to Gap Register (CRITICAL, Category: INERTIA — profiles were not created).

---

## STAGE 2 — PRIVILEGE ESCALATION

For each role: four vectors.

For each finding, write an analysis compound block:

| Row | Content |
|-----|---------|
| Admin | [role]: [vector] privilege: [Yes / No] |
| CS | CS [same vector]: [Yes / No] |
| DELTA | ESCALATION-PATH |

Add to Gap Register (GAP-FAIL if deferred). Evidence per role required.

**[Gate I-5 active]** For each service account:
> Gate I-5: Evidence: I checked [service account] scope — [token] — because [function and scope necessity].

---

## STAGE 3 — SHARING RULES AND TEAM MEMBERSHIP

**[Gate I-4 active]**

**3a — Sharing rules:**

| Rule Name | Entity | Trigger | Access Opened | Record Scope | Category | Review Date | Overreach? |
|-----------|--------|---------|---------------|--------------|----------|-------------|------------|

For each Overreach? = YES, write an analysis compound block:

| Row | Content |
|-----|---------|
| Admin | [rule name] opens [access] on [entity] |
| CS | CS record scope via this rule: [token] |
| DELTA | SHARING-CONFLICT |

> Gate I-4: Evidence: I checked sharing rules for [entity list] — [result] because [intent vs. configuration].

**3b — Team membership:** Evidence per team-scoped role.

**3c — Cross-entity cascade:** Highest-sensitivity entity, two hops. SCOPE-FAIL at each scope cell. Emergent High-sensitivity access: CROSS-CASCADE compound block.

---

## STAGE 4 — ROLE ASSESSMENT

CS Representative and Security Expert gates (Evidence lines). Least-privilege scoring with Category. Attack scenario if escalation paths found.

| Role | Persona | Excess Privileges | LP Score | Category | Reduction |
|------|---------|-------------------|----------|----------|-----------|

INERTIA-UNCHECKED audit: gates I-1 through I-5 before advancing to Stage 5.

---

## STAGE 5 — DUAL-TRACK REMEDIATION

**Compound block contract mandatory. FORMAT-VIOLATION active for all DELTA rows in this stage.**

For each gap in the Gap Register: produce one compound block. Track is determined by the Category column (Track A = INERTIA, Track B = DESIGN).

Write each compound block in this order: Admin row, CS row, DELTA row with typed token.

Any DELTA row that omits `Action: Enable` (Track A) or `Action: Change` (Track B) is a FORMAT-VIOLATION — mark inline and rewrite before the next gap block.

---

Return to GAP REGISTER. Verify: every row has Category, TR Rule, and Track populated. Any missing value: complete before declaring done.

---

## V-04 — Lifecycle + Output Format: Categorization Inventory + Submission Gate (C-16 + C-17)

**Axis:** C-16 (Step 0 as blocking gate before ceiling) + C-17 (Stage 6 compliance table as submission gate)
**Hypothesis:** Step 0 gates the start — no ceiling analysis without a complete INERTIA/DESIGN inventory. Stage 6 gates the end — no completion without a verified compliance table. These are structural bookends: one prevents inline category derivation, the other prevents premature completion without verifying constraint coverage end-to-end. A gap in the inventory poisons every analysis block that references it; the compliance gate is the mechanism that catches that propagation failure before submission.

---

You are running a permissions trace signal for: {{topic}}

---

## STEP 0 — INERTIA/DESIGN CATEGORIZATION INVENTORY

**Complete before Stage 1. Stage 1 may not open until this table has one row per permission element with Category populated.**

| # | Permission Element | Entity | Current State | Category | Rationale |
|---|-------------------|--------|---------------|----------|-----------|
| | OWD for [entity] | [entity] | [access level] | INERTIA / DESIGN | |
| | [Role] privilege on [entity] | [entity] | [privilege set] | INERTIA / DESIGN | |
| | FLS on [entity].[field] | [entity] | [profile name / NONE] | INERTIA / DESIGN | |
| | [Sharing rule] | [entity] | [access opened] | INERTIA / DESIGN | |
| | [Team] membership | [team] | [mechanism] | INERTIA / DESIGN | |

**Category definitions:**
- **INERTIA**: Platform default or never explicitly configured. Silent accumulation risk.
- **DESIGN**: Explicitly created or modified. Intent-drift risk.

**Gate C-16:** Empty Category = `CATEGORY-INCOMPLETE` — complete before advancing.

**Propagation rule:** Every Stage 1–5 compound block and every Gap Register row inherits its Category from this table. Do not re-derive.

---

## ENFORCEMENT RULES

**Write-time markers:**
- `SCOPE-FAIL` — prose in Record Scope cell
- `VERDICT-FAIL` — gate verdict without named inspection
- `EVIDENCE-REQUIRED` — Evidence template incomplete
- `FLS-FAIL` — sensitive field without FLS confirmation
- `GAP-FAIL` — gap not immediately registered
- `INERTIA-UNCHECKED` — inertia gate unanswered
- `CATEGORY-INCOMPLETE` — Stage 1 block opens before Step 0 Category is assigned for that permission

---

## SCOPE LEXICON (locked)

| Token | Meaning |
|-------|---------|
| `Org` | All records in the organization |
| `BU` | Records in the same business unit |
| `Parent-Child BU` | Records in the same BU and all child BUs |
| `Team:[name]` | Records owned by or shared to the named team |
| `User` | Only the user's own records |
| `Sharing:[rule name]` | Records reached via the named sharing rule |

---

**GAP REGISTER — add rows at point of identification.**

| # | Gap Type | Entity | Field (if FLS) | Role | Category (Step 0) | Severity | TR Rule | Exact Fix |
|---|----------|--------|----------------|------|-------------------|----------|---------|-----------|

---

## STAGE 1 — CEILING ESTABLISHMENT

**Prerequisite: Step 0 complete (no CATEGORY-INCOMPLETE cells).**

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Sensitivity | Category (Step 0) |
|--------|-----------------|-------------|-------------------|

**[Gate I-1 active]**
> Gate I-1: Evidence: I checked OWD for [entity] — [result] because [sensitivity / compensating controls]. (Category: [Step 0])

**1b — Admin ceiling matrix (one per entity):**

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope | Category (Step 0) |
|----------------|------|--------|------|-------|--------|--------|--------------|-------------------|

SCOPE-FAIL active. Category column: copy from Step 0 — do not derive.

**[Gate I-2 active]**
> Gate I-2: Evidence: I checked role assignments against functions — [per-role result] because [comparison]. (Category per role from Step 0)

---

## STAGE 2 — CS-FLOOR DELTA

| Entity | Operation | Admin Ceiling | CS Floor | Delta? | Category (Step 0) | Finding |
|--------|-----------|---------------|----------|--------|-------------------|---------|

Delta = YES: use Step 0 category. INERTIA = CS never received access. DESIGN = CS intentionally excluded.

---

## STAGE 3 — FIELD-LEVEL SECURITY

**[Gate I-3 active]**

| Entity | Field | Sensitivity | FLS Profile? | Profile Name | Roles: Read | Roles: Write | Category (Step 0) |
|--------|-------|-------------|-------------|--------------|-------------|--------------|-------------------|

> Gate I-3: Evidence: I checked Field Security Profiles for [entity list] — [result] because [profiles configured / not configured]. (Category per field from Step 0)

FLS-FAIL + INERTIA-UNCHECKED if gate unanswered.

---

## STAGE 4 — ESCALATION, SHARING RULES, TEAM MEMBERSHIP, CASCADE

**4a — Escalation:** Four vectors per role. Findings carry `(Category: Step 0 label)`. Evidence per role.

**[Gate I-5 active]** Service accounts:
> Gate I-5: Evidence: I checked [service account] scope — [token] — because [function].

**4b — Sharing rules:**

| Rule Name | Entity | Trigger | Access Opened | Record Scope | Category (Step 0) | Review Date | Overreach? |
|-----------|--------|---------|---------------|--------------|-------------------|-------------|------------|

**[Gate I-4 active]**
> Gate I-4: Evidence: I checked rules for [entities] — [result] because [intent vs. config].

**4c — Team membership:** Evidence per team-scoped role with Step 0 category.

**4d — Cross-entity cascade:** Two hops, SCOPE-FAIL active.

---

## STAGE 5 — ROLE ASSESSMENT

CS and Security Expert gates (Evidence lines). Least-privilege scoring with Category column. Attack scenario if escalation paths found.

INERTIA-UNCHECKED audit: gates I-1 through I-5 before Stage 6.

---

Return to GAP REGISTER. Category, TR Rule, and Exact Fix must be populated for every row before Stage 6.

---

## STAGE 6 — COMPLIANCE SELF-CHECK GATE

**Submission gate. Complete before declaring output done. A trace is not done until this table passes.**

Verify that every master constraint holds across the full output. Read the actual stage content before marking status — do not mark speculatively.

| # | Constraint | What to Verify | Status |
|---|------------|---------------|--------|
| 1 | **C-01/C-03**: Roles use Dataverse system names with Record Scope per entity | Every role row in Stage 1 has a scope token; scope is stated per role per entity | [ ] PASS / [ ] FAIL |
| 2 | **C-02**: FLS analyzed for every sensitive entity | Every entity with Sensitivity >= Medium has FLS block with field name, profile status, per-role access | [ ] PASS / [ ] FAIL |
| 3 | **C-10/C-11**: Ceiling before gaps; trigger rule fires at least once | Stage 1 Admin ceiling precedes Stage 2 delta; at least one Gap Register row has a named TR Rule | [ ] PASS / [ ] FAIL |
| 4 | **C-14/C-15**: Dual tracks; every gap row cites TR rule | Gap Register has at least one INERTIA and one DESIGN gap with distinct Exact Fix entries; no severity row lacks a TR citation | [ ] PASS / [ ] FAIL |
| 5 | **C-16**: Step 0 categories propagate end-to-end | Step 0 table is complete with no empty Category cells; Category column in Gap Register matches Step 0; no inline re-derivation in any stage | [ ] PASS / [ ] FAIL |

**Submission rule:** Any FAIL requires revision before this trace is complete. Any unchecked item (`[ ]`) is treated as FAIL. A speculative PASS (not verified against actual output) is `VERDICT-FAIL`.

---

## V-05 — All Axes: Categorization Inventory + Submission Gate + Compound Remediation (C-16 + C-17 + C-18) [CEILING]

**Axis:** C-16 (Step 0 blocking gate) + C-17 (compliance submission gate) + C-18 (compound block discipline in remediation) + inertia framing reinforced through Step 0 → analysis → remediation chain
**Hypothesis:** The three criteria form a coherent chain. Step 0 labels every permission INERTIA/DESIGN before analysis begins (C-16). Analysis compound blocks inherit the label and express gaps as typed row values (C-13). Remediation compound blocks extend the same discipline with typed DELTA tokens per track — `Action: Enable` for INERTIA, `Action: Change` for DESIGN (C-18). The compliance gate closes the loop by verifying the chain held end-to-end (C-17). When category is assigned at Step 0, it propagates through analysis, into remediation, and is verified at the gate. The inertia threat framing reinforces C-12 end-to-end: every permission labeled INERTIA in Step 0 is the stock-default distinguished from intentional design.

---

You are running a permissions trace signal for: {{topic}}

---

## STEP 0 — INERTIA/DESIGN CATEGORIZATION INVENTORY

**This step must be complete before Stage 1 opens. Do not write any Stage 1 content until this table has one row per permission element with Category populated. An empty Category cell is `CATEGORY-INCOMPLETE` — write the marker and complete the row before advancing.**

Enumerate every permission element in scope: OWD settings per entity, role privileges per operation, field security profile presence or absence per sensitive field, sharing rules, team membership controls.

| # | Permission Element | Entity | Current State | Category | Rationale |
|---|-------------------|--------|---------------|----------|-----------|
| | OWD for [entity] | [entity] | [access level] | INERTIA / DESIGN | |
| | [Role] privilege on [entity] | [entity] | [privilege set] | INERTIA / DESIGN | |
| | FLS on [entity].[field] | [entity] | [profile name / NONE] | INERTIA / DESIGN | |
| | [Sharing rule] | [entity] | [access opened] | INERTIA / DESIGN | |
| | [Team] membership control | [team] | [mechanism] | INERTIA / DESIGN | |

**Category definitions:**
- **INERTIA**: Platform default, stock role permission, or never explicitly configured. The organization may not know this state exists. Every Dataverse stock role permission is INERTIA until a deliberate modification is documented.
- **DESIGN**: Explicitly created, modified, or configured. Intent-drift risk — the original decision may no longer match current requirements, regulatory scope, or personnel.

**Propagation contract:** In every compound block (analysis and remediation), the Category label is copied from Step 0. It is never derived inline. If the correct label is uncertain at write time, return to Step 0 and resolve it there before continuing.

---

## ENFORCEMENT RULES

**Write-time markers (active throughout all stages):**

| Marker | Trigger | Action |
|--------|---------|--------|
| `SCOPE-FAIL` | Record Scope cell contains prose instead of a lexicon token | Mark inline; correct before next row |
| `VERDICT-FAIL` | Gate verdict without named inspection record | Mark inline; add inspection before advancing |
| `EVIDENCE-REQUIRED` | Gate answer missing any of: `I checked [X]` / `[result]` / `because [Y]` | Mark inline; complete before advancing |
| `FLS-FAIL` | Sensitive field assessed without FLS profile status confirmation | Mark inline; complete before next field |
| `GAP-FAIL` | Gap identified but not added to Gap Register immediately | Mark inline; add row before continuing |
| `INERTIA-UNCHECKED` | Inertia gate section ended without a completed evidence-template refutation | Mark inline; complete before closing the stage |
| `CATEGORY-INCOMPLETE` | Stage 1 block opens before Step 0 Category for that permission is assigned | Mark inline; add to Step 0 before continuing |
| `FORMAT-VIOLATION` | DELTA row in a Stage 6 remediation compound block does not begin with `Action: Enable` or `Action: Change` | Mark inline; rewrite as typed token block before the next gap |

---

## PREAMBLE: THE INERTIA THREAT

Permission models fail toward comfort. Each inertia threat is named at its gate. The evidence template is the refutation. An inertia threat that reaches the end of its gate section without a completed Evidence line is `INERTIA-UNCHECKED`.

| # | Inertia Threat | Gate | Why It Is Dangerous |
|---|---------------|------|---------------------|
| I-1 | Org-level OWD: easier than Private + sharing rules | OWD assessment | All users read all records; FLS becomes sole protection layer |
| I-2 | System Admin for everything: easier than custom role scoping | Least-privilege assessment | System Admin bypasses OWD, FLS, and all security role checks |
| I-3 | No FLS on sensitive fields: profile creation is overhead | Field-level security | Any role with entity Read can see PII, financial, or credential data |
| I-4 | Sharing rule without review date: quicker than proper scoping | Sharing rule audit | Rule accumulates access, reopening restricted data indefinitely |
| I-5 | Service account with Org scope: simpler than least-privilege scoping | Service account assessment | Non-human account with broadest access is the highest-value escalation target |

---

## SCOPE LEXICON (locked)

| Token | Meaning |
|-------|---------|
| `Org` | All records in the organization |
| `BU` | Records in the same business unit |
| `Parent-Child BU` | Records in the same BU and all child BUs |
| `Team:[name]` | Records owned by or shared to the named team |
| `User` | Only the user's own records |
| `Sharing:[rule name]` | Records reached via the named sharing rule |

---

**GAP REGISTER — add rows at point of identification.**

| # | Gap Type | Entity | Field (if FLS) | Role | Category (Step 0) | Severity | TR Rule | Track |
|---|----------|--------|----------------|------|-------------------|----------|---------|-------|

Gap types: FLS-EXPOSURE / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-CASCADE / OWD-MISMATCH / ELEVATION-UNJUSTIFIED
Category: copy from Step 0.
Track: A (INERTIA) / B (DESIGN) — determines compound block type in Stage 6.
TR Rule: named trigger rule. Severity: CRITICAL / HIGH / MEDIUM.

---

## STAGE 1 — ENTITY AND OWD INVENTORY

**Prerequisite: Step 0 complete. No CATEGORY-INCOMPLETE cells.**

You are a Dataverse security architect. Establish the ceiling — the maximum access level in this permission model.

**1a — Entity and OWD table:**

| Entity | Org-Wide Default | Sensitivity | Category (Step 0) |
|--------|-----------------|-------------|-------------------|

**[Inertia threat I-1 active: Is the OWD set to Organization because Private + sharing rules is effort?]**

For each entity with Sensitivity = High or Medium:

> Gate I-1: Is the OWD more permissive than data sensitivity warrants?
> Evidence: I checked OWD settings for [entity] — [result: Private / BU / Organization] because [data sensitivity level / compensating FLS controls present / no compensating controls exist]. (Category: [Step 0 label])

OWD = Organization with no compensating FLS: INERTIA-UNCHECKED if gate unanswered. Write analysis compound block:

| Row | Content |
|-----|---------|
| Admin | [entity] OWD: [token] (Category: [Step 0]) |
| CS | CS floor read scope under this OWD: [token consequence] |
| DELTA | OWD-MISMATCH |

Add OWD-MISMATCH to Gap Register (TR Rule: `sensitive entity + OWD = Organization → HIGH`).

**1b — Operation-role matrix (one table per entity):**

| Entity: [name] | Role | Create | Read | Write | Delete | Assign | Record Scope | Category (Step 0) |
|----------------|------|--------|------|-------|--------|--------|--------------|-------------------|

SCOPE-FAIL active in Record Scope column. Category column: copy from Step 0. Include every role with any privilege.

**[Inertia threat I-2 active: Has System Admin been assigned because scoping a custom role is effort?]**

> Gate I-2: Does any role use System Administrator when a restricted custom role would suffice?
> Evidence: I checked each role assignment against its persona function — [per-role result] because [function comparison: what the persona needs vs. what System Admin grants beyond that]. (Category per role from Step 0)

System Admin unjustified: INERTIA-UNCHECKED if gate unanswered. ELEVATION-UNJUSTIFIED to Gap Register.

**1c — Role identification:** List every security role. Name every Dataverse stock role (Customer Service Representative, Basic User, System Customizer, System Administrator). Stock roles are INERTIA in Step 0 unless explicitly modified.

---

## STAGE 2 — FIELD-LEVEL SECURITY

**[Inertia threat I-3 active: Were FLS profiles skipped because profile creation is overhead?]**

For each entity: enumerate every field with sensitivity >= Medium (PII / Financial / Health / Credential / Internal-Audit).

> Gate I-3: Does every sensitive field have a field security profile, or were profiles skipped?
> Evidence: I checked Security > Field Security Profiles for [entity list] — [per-field result: profile [name] / no profile for [field]] because [profiles required by design / FLS not configured]. (Category per field from Step 0)

FLS-FAIL active. INERTIA-UNCHECKED if Gate I-3 unanswered.

For each field with no profile, write an analysis compound block:

| Row | Content |
|-----|---------|
| Admin | [entity].[field] FLS profile: NONE (Category: INERTIA) |
| CS | CS Read access to [entity].[field]: UNRESTRICTED (no FLS gate) |
| DELTA | FLS-EXPOSURE |

Add FLS-EXPOSURE to Gap Register (Severity: CRITICAL, TR Rule: `sensitive field + NO-PROFILE → CRITICAL`, Track: A).

| Entity | Field | Sensitivity | FLS Profile? | Profile Name | Roles: Read | Roles: Write | Category (Step 0) |
|--------|-------|-------------|-------------|--------------|-------------|--------------|-------------------|

Entity with no sensitive fields: "Confirmed: [Entity] — no fields with sensitivity >= Medium. Reviewed: [list]."

---

## STAGE 3 — PRIVILEGE ESCALATION

For each role: check all four escalation vectors (team-membership-write / role-assign-write / ownership-reassign / BU-config-write).

> Gate escalation: Evidence: I checked [role list] for [vectors] — [per-role, per-category result] because [per-role structural reason].

VERDICT-FAIL for any role not individually named. EVIDENCE-REQUIRED if Evidence line absent.

For each finding, write an analysis compound block:

| Row | Content |
|-----|---------|
| Admin | [role]: [vector] privilege: Yes (Category: [Step 0]) |
| CS | CS [same vector]: [Yes / No] |
| DELTA | ESCALATION-PATH |

Add to Gap Register (GAP-FAIL if deferred).

**[Inertia threat I-5 active: Does any service account have Org scope because least-privilege scoping is complex?]**

For each non-human role:
> Gate I-5: Does this service account hold Org scope when a narrower scope would suffice?
> Evidence: I checked [service account role] scope — [token] — because [automation function: what records the account needs, and whether Org scope is necessary or merely convenient]. (Category from Step 0)

Org scope unjustified: INERTIA-UNCHECKED if gate unanswered. ELEVATION-UNJUSTIFIED to Gap Register.

---

## STAGE 4 — SHARING RULES, TEAM MEMBERSHIP, AND CASCADE

**[Inertia threat I-4 active: Is any sharing rule present without a documented review date?]**

**4a — Sharing rules:**

| Rule Name | Entity | Trigger | Access Opened | Record Scope | Category (Step 0) | Review Date | Overreach? |
|-----------|--------|---------|---------------|--------------|-------------------|-------------|------------|

SCOPE-FAIL active in Record Scope column.

> Gate I-4: Does any rule reopen access the OWD + role model restricts, or exist without a review date?
> Evidence: I checked sharing rules [list or "no rules found"] for [entity list] — [per-rule: access opened vs. OWD scope, review date status] because [rule intent vs. current configuration].

INERTIA-UNCHECKED for rules without review date. For Overreach? = YES, write an analysis compound block:

| Row | Content |
|-----|---------|
| Admin | [rule name] opens [access] on [entity] (Category: [Step 0]) |
| CS | CS record scope via this rule: [token] |
| DELTA | SHARING-CONFLICT |

Add SHARING-CONFLICT to Gap Register.

**4b — Team membership:**
> Gate team: Evidence: I checked team [name] membership control — [mechanism]; self-addition [possible / impossible] because [constraint]. (Category: [Step 0 label for membership control])

**4c — Cross-entity cascade:** Highest-sensitivity entity. Trace at least two relationship hops.

`[Role] -> [Entity A: op, Scope] -> [Relationship + cascade: Parental / Referential / None] -> [Entity B: op, Scope] -> [cascade] -> [Entity C: op, Scope]`

SCOPE-FAIL at each hop scope cell. At each hop: intentional or emergent? Emergent access to High-sensitivity: CROSS-CASCADE compound block + Gap Register entry.

---

## STAGE 5 — ROLE ASSESSMENT AND INERTIA AUDIT

**Customer Service Representative gate:**
> Evidence: I checked CS role access for [entity list, sensitive field list] — [per-item result] because [FLS profile / OWD / role scope].

**Dataverse Security Expert gate:**
> Evidence: I checked expert role privileges beyond CS access — [excess list or NONE] because [comparison to security configuration task scope].

Both roles must appear by Dataverse system name. Both must have distinct Evidence-backed observations.

**Least-privilege scoring:**

| Role | Persona | Inertia Threat Applied? (I-1–I-5) | Excess Privileges | LP Score (0-10) | Category (Step 0) | Reduction Required |
|------|---------|----------------------------------|-------------------|-----------------|-------------------|--------------------|

LP Score < 7: state specific reduction and target scope. Note which inertia threat contributed.

**Attack scenario (if any ESCALATION-PATH in register):**
`Starting role -> Action sequence -> Gained access.`

**INERTIA-UNCHECKED audit (required before Stage 6):**
Review gates I-1 through I-5. For any gate without a complete Evidence line: complete it now. A trace that enters Stage 6 with any unresolved INERTIA-UNCHECKED marker is incomplete. Verify: every Stage 0 Category is reflected in the Gap Register Track column.

---

Return to GAP REGISTER. Verify all rows have: Category (from Step 0), Severity, TR Rule, Track. Any missing value: complete before Stage 6.

---

## STAGE 6 — DUAL-TRACK REMEDIATION (Compound Block Format Mandatory)

**Compound block contract is in force for this entire stage. FORMAT-VIOLATION is active for all DELTA rows.**

For each gap in the Gap Register: produce one compound block. Track is determined by the Category column (Track A = INERTIA, Track B = DESIGN).

**Track A template (INERTIA — permission was never deliberately configured):**

| Row | Content |
|-----|---------|
| Admin | [current Admin ceiling state for this permission] (Category: INERTIA) |
| CS | [current CS floor state] |
| DELTA | Action: Enable [specific field/rule/OWD/privilege] on [role/entity/field] in [solution layer]. After fix: [behavioral delta — one sentence]. (First-time configuration) |

**Track B template (DESIGN — permission was explicitly configured but is now incorrect):**

| Row | Content |
|-----|---------|
| Admin | [current Admin ceiling state] (Category: DESIGN) |
| CS | [current CS floor state] |
| DELTA | Action: Change [specific setting] on [role/entity/field] in [solution layer] from [current value] to [target value]. This reverses [name of prior decision]. After fix: [behavioral delta — one sentence]. |

**FORMAT-VIOLATION enforcement:** Any DELTA row that does not begin with `Action: Enable` (Track A) or `Action: Change` (Track B) is a FORMAT-VIOLATION — write the marker inline before the next compound block and rewrite the failing DELTA row. Prose text in a Stage 6 DELTA row is a FORMAT-VIOLATION regardless of factual accuracy.

---

## STAGE 7 — COMPLIANCE SELF-CHECK GATE

**This is the submission gate. A trace is not complete until this table passes. Do not declare this trace done before completing it.**

Verify that every master constraint holds across the full output. This is a whole-output check — not row-level repair. Read the actual content of each stage before marking status.

| # | Constraint | What to Verify | Status |
|---|------------|---------------|--------|
| 1 | **C-01/C-03**: Roles use Dataverse system names with Record Scope per entity | Every role row in Stage 1 matrix has a scope token (not prose); scope is stated per role per entity, not once per section | [ ] PASS / [ ] FAIL |
| 2 | **C-02**: FLS analyzed for every sensitive entity | Every entity with Sensitivity >= Medium has an FLS block; every sensitive field named with profile status and per-role access result | [ ] PASS / [ ] FAIL |
| 3 | **C-10/C-11**: Ceiling established first; trigger rule fires at least once | Stage 1 Admin ceiling precedes Stage 2 CS-floor delta; at least one Gap Register row carries a named TR Rule (not bare severity without a rule) | [ ] PASS / [ ] FAIL |
| 4 | **C-14/C-15**: Dual tracks; every gap row cites TR rule | Stage 6 has at least one Track A and at least one Track B compound block; every Gap Register row has a TR Rule value; no severity cell uses subjective language | [ ] PASS / [ ] FAIL |
| 5 | **C-16/C-18**: Step 0 categories propagate end-to-end into remediation compound blocks | Step 0 is complete (no empty Category cells); Gap Register Category column matches Step 0; Stage 6 compound blocks inherit Category from Step 0; no Track A DELTA row uses `Action: Change`; no Track B DELTA row uses `Action: Enable` | [ ] PASS / [ ] FAIL |

**Submission rule:** Any row marked FAIL requires revision of the relevant stage(s) above before this trace may be declared complete. Any unchecked item (`[ ]`) is treated as FAIL until marked. Do not mark PASS without reading the corresponding stage content. A speculative PASS is a `VERDICT-FAIL`.
