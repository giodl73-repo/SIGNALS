# trace-permissions Variate -- Round 3 (Rubric v3, Corrected)

**Date:** 2026-03-16
**Rubric:** v3 (C-01 through C-15)
**New criteria targeted this round:** C-13 (Pre-Declared Scale with Auto-Fail Condition), C-14 (Prose-Substitution Failure Mode Named by Example), C-15 (Self-Verification Checklist for Aspirational Criteria)
**Prior round retained:** All C-01..C-12 mechanics from R2 V-05 (current T3) preserved across all variations. These variations add new structural mechanisms on top without removing existing ones.

---

## Round 3 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | C-13 single axis -- Graded Column Registry generalized to all graded columns | Pre-declaring ALL graded column scales in one GRADED COLUMN REGISTRY before any table creates a global C-13 contract at schema level rather than a per-table annotation, making blank-cell violations detectable against one authoritative source |
| V-02 | C-14 single axis -- Prohibited Prose Forms catalog for every table | Naming the wrong prose form verbatim at every table site, citing the criterion each violation fails, makes every prose-substitution path recognizable before selection, not just the FLS case |
| V-03 | C-15 single axis -- Full aspirational checklist expanded to all 8 criteria | Replacing the 3-item (C-10/C-11/C-12) checklist with a structured 8-item table covering C-08..C-15 with explicit PASS/FAIL conditions makes C-15 a formal self-audit protocol rather than a spot-check |
| V-04 | Combined: C-13 + C-14 (Graded Column Registry + Prohibited Prose Forms) | Dual enforcement: scale contract declared once at registry (C-13) + prose wrong-form examples at every table site (C-14); the two mechanisms defend opposite failure modes without structural conflict |
| V-05 | Full integration: C-13 + C-14 + C-15 all hardened | All three v3 mechanisms: Graded Column Registry + Prohibited Prose Forms + full 8-item aspirational audit table; the model can self-verify every aspirational criterion before submission |

---

## V-01 -- Single Axis: C-13 (Graded Column Registry)

**Axis:** C-13 single axis
**Hypothesis:** The R2 V-05 base (current T3) declares a scale only for the Escalation Risk column. Under v3 C-13, "at least one graded column" passes, but pre-declaring ALL graded columns in a single GRADED COLUMN REGISTRY block before any table should make the pattern more robust: blank-cell violations in ANY graded column are detectable against the registry, not requiring inspectors to locate per-column definitions. The registry also serves as the auto-fail preamble for every column simultaneously.

---

depth: standard
# quick   -> fast scan, 5+ findings, prioritize obvious issues
# standard -> thorough, 15+ findings, full coverage (default)
# deep    -> exhaustive adversarial audit, 25+ findings, treat missing as failure

confidence: standard
# low    -> include findings without citation
# standard -> cite source section for each finding (default)
# strict  -> only include findings with quotable specific evidence

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

Manual security reviews of Dataverse environments routinely miss three failure scenarios that this
trace is designed to surface:

**Blind spot 1 -- Post-incident FLS gap.** Column security profiles are rarely audited proactively.
Sensitive fields -- credit limits, compensation data, SSNs, contact identifiers -- remain readable
and writable by any role unless a column security profile explicitly restricts them. The security
roles UI does not surface which fields lack column security profiles; gaps are discovered after
data exposure, not before.

**Blind spot 2 -- Cumulative privilege blind spot.** A user holding a BU-scoped security role who
also belongs to an owner team whose team role grants org-wide access has effective org-wide access.
No single Dataverse UI view surfaces the combined effective access produced by role + team + OWD
combination. Spot-checking individual roles misses cross-role accumulation through team membership.

**Blind spot 3 -- OWD-sharing-rule override gap.** Administrators check OWD settings
entity-by-entity without evaluating the sharing rules that silently override those baselines. A
Private OWD on Case combined with a Power Automate-triggered sharing rule grants effective
org-wide read to users who satisfy the trigger condition -- including low-trust service accounts
and CS users not intended to have broad case access.

This trace closes all three blind spots: SE-2 closes Blind spot 1; SE-3 closes Blind spot 2;
SE-4 closes Blind spot 3.

---

## GRADED COLUMN REGISTRY (CA-authored, Phase 0 precondition)

All graded columns used in this trace are declared here before any table is populated.
Each entry specifies: (a) scale with every level named, (b) auto-fail condition for blank cells,
(c) post-table verification instruction. A table that uses a column not registered here is
structurally incomplete. A cell that does not match the declared values auto-fails.

**GCR-1 -- Tier** (used in TABLE_1, TABLE_3, TABLE_5)
Scale: `Admin` / `Custom` / `Restricted`
Auto-fail: any cell not one of these three values is a blank-equivalent and auto-fails TABLE verification.
Post-table verification: after each table with a Tier column, confirm every row has one of the three declared values.

**GCR-2 -- Severity** (used in TABLE_4, TABLE_5)
Scale: `CRITICAL` (exploitable with no additional steps) / `HIGH` (exploitable with one intermediate step) / `MEDIUM` (limited blast radius or requires specific conditions)
Auto-fail: any Severity cell that is blank or uses a value outside CRITICAL / HIGH / MEDIUM auto-fails TABLE_5 verification.
Post-table verification: after TABLE_5, list any row with a blank or non-declared Severity as NON-COMPLIANT.

**GCR-3 -- Checked?** (used in TABLE_4)
Scale: `YES` (vector examined, finding or specific rule-out written) / `NO` (not checked -- auto-fail)
Auto-fail: any Checked? = NO or blank auto-fails TABLE_4 verification. All four vectors must be YES.
Post-table verification: after TABLE_4, confirm all four rows have Checked? = YES.

**GCR-4 -- Verified?** (used in TABLE_3)
Scale: `YES` (scope confirmed against configuration) / `NO` (scope inferred, not confirmed -- flag as gap)
Auto-fail: a blank Verified? cell is treated as NO and auto-fails the row.
Post-table verification: after TABLE_3, list any NO rows as unconfirmed scope entries requiring follow-up.

**GCR-5 -- FLS Profile Configured?** (used in TABLE_2)
Scale: `Configured` (a column security profile exists and restricts this field) / `Not Configured` (no column security profile; field accessible to any role with entity access)
Auto-fail: blank or any value other than `Configured` / `Not Configured` auto-fails TABLE_2 verification.
Post-table verification: after TABLE_2, confirm every row has one of the two declared values.

**GCR-6 -- Gap?** (used in TABLE_2)
Scale: `YES` (field has missing or insufficient protection -- forward to TABLE_5) / `NO` (field adequately protected)
Auto-fail: blank Gap? cell auto-fails the row. Every Gap? = YES row must have a corresponding TABLE_5 entry.
Post-table verification: after TABLE_2, verify every YES row has a TABLE_5 cross-reference.

**GCR-7 -- Escalation Risk** (used in Closing Summary)
Scale: `HIGH` (role combination or sharing rule produces access materially exceeding job function) / `MEDIUM` (access exceeds job function in limited scope; low blast radius) / `LOW` (minor excess access; unlikely to be exploited) / `NONE` (access appropriate to job function; no escalation vector confirmed)
Auto-fail: blank Escalation Risk cell auto-fails Closing Summary verification. Inline text "varies" or "see above" is blank-equivalent.
Post-table verification: after Closing Summary, list any row with a blank or non-declared Escalation Risk as NON-COMPLIANT.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins.

**PHASE 0 -- CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1: TABLE_1 through TABLE_5 with Tier
columns on TABLE_1 and TABLE_3; CS-2 and CS-3 with SE-updatable columns and SE-update protocols
-- seven schemas total) and the Criterion Enforcement Matrix preamble (Step 0.2: SHALL-A through
SHALL-G, M4 row IDs CA-1.1 through CA-1.8 pre-assigned). CA issues handoff to PHASE 1.

**PHASE 1 -- CS (Customer Success):**
Executes second. Opens with CS-0 sub-section (Schema Registry acknowledgment: CS echoes Registry
schema IDs for CS-2 and CS-3 by exact Schema ID label, lists SE-updatable columns for each, and
confirms the expectation format before authoring any expectation rows). Then produces CS-1, CS-2,
CS-3 using Registry schemas. CS does not fill TABLE_1-5. CS issues handoff to PHASE 2.

**PHASE 2 -- SE (Security Engineer / Dataverse Security Expert):**
Executes third in privilege-tier descent order. SE-0 (admin-tier inventory and TABLE_4 escalation
vectors) runs before SE-1 (role-operation matrix), establishing the privilege ceiling before
populating operation cells. TABLE_1 and TABLE_3 include Tier column. SE-2, SE-3, SE-4 each open
with two-part exact-label closure blocks per SHALL-G. SE-4 cites SE-0 data in cross-tier
differential. Issues handoff to PHASE 3.

**PHASE 3 -- CA-1 (CA Verification Pass):**
CA returns. Each CA-1 row performs double-anchor reaffirmation: Registry anchor and Preamble
anchor as structurally distinct labeled elements. Verification line follows. CA-1.8 extended to
verify CS-0 acknowledgment precedes CS-1. Final Graded Column Registry verification after CA-1.8.

---

## PHASE 0 -- CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

### Step 0.1 -- Schema Registry (CA-authored, Phase 0)

**All table schemas declared centrally by CA. Blank-cell prohibition is global. GCR values govern
all graded columns -- every cell must match its registered scale.**

**Schema ID: TABLE_1 -- Role-Operation Matrix**
Declared columns: `Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Tier values: GCR-1 (Admin / Custom / Restricted). Rows ordered: Admin tier first, Custom second,
Restricted last. Blank-cell rule: all cells Granted / Denied / Conditional (condition inline) / N/A.

**Schema ID: TABLE_2 -- FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
FLS Profile Configured? values: GCR-5. Gap? values: GCR-6. Blank-cell rule: never blank.

**Schema ID: TABLE_3 -- Record Scope by Role**
Declared columns: `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Tier values: GCR-1. Verified? values: GCR-4. Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU /
Org-wide / Team-scoped / Sharing-[rule name].

**Schema ID: TABLE_4 -- Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
Checked? values: GCR-3. Severity values: GCR-2. Blank-cell rule: all four vectors, Checked? = YES.

**Schema ID: TABLE_5 -- Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation`
Tier values: GCR-1. Severity values: GCR-2. Blank-cell rule: Remediation = exact object + exact location + expected post-fix state.
CS-EXPECTATION-VIOLATED Remediation (three-field block): CS-Expected / SE-Actual / Delta.

**Schema ID: CS-2 -- Sharing Rule Expectations**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference; SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).

**Schema ID: CS-3 -- Cross-Role Access Differential Expectations**
Declared columns: `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference; SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).

### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: M1, M2, M3 simultaneously active. M4 pre-assigned. GCR values override any
inline column value that conflicts with the registry.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-0 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**SHALL obligations:**
- SHALL-A: Complete TABLE_1 with Tier column (GCR-1). Every cell Granted/Denied/Conditional/N/A. Rows ordered by tier.
- SHALL-B: TABLE_2 lists all PII, Financial, and Audit-Compliance fields with explicit FLS status (GCR-5, GCR-6). Null case explicit. Gap? YES rows in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier (GCR-1) and Effective Scope filled. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 at SE-0 (before SE-1), all four vectors, Checked? = YES (GCR-3). Severity per GCR-2. Rule-outs name specific mechanism.
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap case requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field Remediation block (CS-Expected, SE-Actual, Delta).
- SHALL-G: At the opening of SE-2, SE-3, and SE-4, closure MUST appear as a two-part labeled block -- Line 1: `MANUAL GAP [<exact CONTEXT label>]:`; Line 3: `STRUCTURED CLOSE:`; exact = character-for-character.

*Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

### CS-0 -- Schema Registry Acknowledgment (CS-authored, Phase 1)

**Registry acknowledgment for CS-2:**
Schema ID: CS-2 -- Sharing Rule Expectations.
SE-updatable columns as declared by CA in Phase 0 Schema Registry: SE Cross-Reference, SE Confirmation.
Expectation format confirmed. SE-updatable columns left blank; SE fills after SE-0.

**Registry acknowledgment for CS-3:**
Schema ID: CS-3 -- Cross-Role Access Differential Expectations.
SE-updatable columns as declared by CA in Phase 0 Schema Registry: SE Cross-Reference, SE Confirmation.
Expectation format confirmed. SE-updatable columns left blank; SE fills after SE-1/SE-3.

### CS-1 -- Expected Customer Service Access Baseline

For each entity in scope: (a) which CRUD operations the CS role is expected to perform as part of
normal job function; (b) the expected record scope; (c) which sensitive fields CS needs read or
write access to and why. Identify any configuration that may inadvertently open access beyond job
requirements.

**CS-2 -- Sharing rule expectations** *(Schema Registry CS-2; SE-updatable columns blank)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

For each Potential Overreach? YES: name the access path and the most likely over-reached role.

**CS-3 -- Cross-role access differential** *(Schema Registry CS-3; SE-updatable columns blank)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

State at minimum one entity and one operation where CS has less access than the Comparison Role.

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis (Privilege-Tier Descent Order)

### SE-0 -- Admin-Tier Inventory and Escalation Vectors

**Admin-tier role inventory:** List System Administrator, Environment Admin, and any
admin-equivalent roles with record scope and key capabilities.

**TABLE_4 -- Escalation Vector Inventory** *(Schema Registry TABLE_4; GCR-3 for Checked?, GCR-2 for Severity)*

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Finding format: `[Role] -> [Mechanism] -> [Elevated access achieved]` for confirmed escalation;
"Checked [mechanism]: no path found because [specific reason]" for rule-out.

### SE-1 / SHALL-A -- Role-Operation Matrix

**TABLE_1 -- Role-Operation Matrix** *(Schema Registry TABLE_1; GCR-1 for Tier)*

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Rows ordered: Admin tier first, Custom second, Restricted last per GCR-1.

### SE-2 / SHALL-B -- Field-Level Security Coverage

MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:
Column security profiles are not auditable from the security roles UI; administrators discover
missing FLS only after a data exposure event.

STRUCTURED CLOSE:
TABLE_2 enumerates every sensitive field in scope with its explicit FLS status per GCR-5,
surfacing pre-event what the security roles UI conceals.

**TABLE_2 -- FLS Coverage** *(Schema Registry TABLE_2; GCR-5 for FLS Profile Configured?, GCR-6 for Gap?)*

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|
| [No sensitive fields identified] | N/A | N/A | Not Configured | N/A | N/A | YES -- null case: all fields exposed to entity-access roles; TABLE_5 MISSING-FLS row required |

Categories: PII / Financial / Audit-Compliance / Other-Sensitive. Null case: use the null-case row above.
Writing "No column security profiles active on {{topic}}. See analysis above." instead of the null-case row fails C-11.

### SE-3 / SHALL-C -- Record Access Scope

MANUAL GAP [Blind spot 2 -- Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access produced by role + team + OWD.

STRUCTURED CLOSE:
TABLE_3 maps the effective scope for every role by Tier (GCR-1), making team-accumulated privilege visible.

**TABLE_3 -- Record Scope by Role** *(Schema Registry TABLE_3; GCR-1 for Tier, GCR-4 for Verified?)*

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role MUST appear, ordered by Tier per GCR-1.
For any role where Effective Scope exceeds role-only scope due to team membership, write:
"[Role] acquires [scope] through [team/rule name]. Base role scope was [base scope]."

### SE-4 / SHALL-D -- Privilege Escalation Cross-Reference

MANUAL GAP [Blind spot 3 -- OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing sharing rules
that silently override them.

STRUCTURED CLOSE:
TABLE_4 (filled at SE-0) evaluated all four escalation vectors with sharing rules explicitly
cross-referenced against OWD settings. This section adds cross-tier differential citing SE-0 data.

### SE-5 / SHALL-E -- Security Gap Inventory

**ESCALATION RISK SCALE** *(GCR-7; placed before Closing Summary)*
Scale declared in GRADED COLUMN REGISTRY GCR-7: HIGH / MEDIUM / LOW / NONE.
Auto-fail: blank Escalation Risk cell auto-fails verification.
Post-table verification: list any blank or non-declared cell as NON-COMPLIANT.

**TABLE_5 -- Security Gap Inventory** *(Schema Registry TABLE_5; GCR-1 for Tier, GCR-2 for Severity)*

| # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation |
|---|----------|--------|---------------|------|------|----------|-------------|
| CLEARED | -- | No gaps found | -- | -- | -- | -- | Evidence: [per-gap-type confirmation that each gap type was checked and cleared] |

Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

**CA-1.1 -- C-01:** Registry anchor TABLE_1 (GCR-1 Tier). Preamble anchor C-01/SE-1/SHALL-A. Verification: TABLE_1 present? Tier per GCR-1? Rows ordered? -> PASS / FAIL

**CA-1.2 -- C-02:** Registry anchor TABLE_2 (GCR-5, GCR-6). Preamble anchor C-02/SE-2/SHALL-B. Verification: TABLE_2 present? FLS per GCR-5? Gap? per GCR-6? Null case as data row? -> PASS / FAIL

**CA-1.3 -- C-03:** Registry anchor TABLE_3 (GCR-1, GCR-4). Preamble anchor C-03/SE-0+SE-3/SHALL-C. Verification: Every TABLE_1 role in TABLE_3? Tier per GCR-1? Verified? per GCR-4? -> PASS / FAIL

**CA-1.4 -- C-04:** Registry anchor TABLE_4 (GCR-3, GCR-2). Preamble anchor C-04/SE-0/SHALL-D. Verification: TABLE_4 at SE-0? All four vectors? Checked? = YES per GCR-3? Severity per GCR-2? -> PASS / FAIL

**CA-1.5 -- C-05:** Registry anchor TABLE_5 (GCR-1, GCR-2). Preamble anchor C-05/SE-5/SHALL-E. Verification: TABLE_5 present? Named gap or CLEARED row? Tier per GCR-1? Severity per GCR-2? -> PASS / FAIL

**CA-1.6 -- SHALL-F compliance:** CS-EXPECTATION-VIOLATED rows: CS-Expected + SE-Actual + Delta all present? -> PASS / FAIL per row.

**CA-1.7 -- SHALL-G compliance:** SE-2 opens with `MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:`? SE-3 with `[Blind spot 2 -- Cumulative privilege blind spot]:`? SE-4 with `[Blind spot 3 -- OWD-sharing-rule override gap]:`? -> PASS / FAIL per section.

**CA-1.8 -- CS-0 acknowledgment:** CS-2 and CS-3 in Schema Registry? CS-0 present before CS-1? CS-0 cites both schema IDs? SE populated SE-updatable columns? -> PASS / FAIL

**CA-1.9 -- Graded Column Registry compliance:**
- GCR-1 (Tier): all TABLE_1 and TABLE_3 Tier cells are Admin / Custom / Restricted? -> PASS / FAIL
- GCR-2 (Severity): all TABLE_4 and TABLE_5 Severity cells are CRITICAL / HIGH / MEDIUM? -> PASS / FAIL
- GCR-3 (Checked?): all TABLE_4 Checked? cells are YES? -> PASS / FAIL
- GCR-4 (Verified?): all TABLE_3 Verified? cells are YES / NO? -> PASS / FAIL
- GCR-5 (FLS Profile Configured?): all TABLE_2 cells are Configured / Not Configured? -> PASS / FAIL
- GCR-6 (Gap?): all TABLE_2 Gap? cells are YES / NO? Every YES has TABLE_5 entry? -> PASS / FAIL
- GCR-7 (Escalation Risk): all Closing Summary Escalation Risk cells are HIGH / MEDIUM / LOW / NONE? -> PASS / FAIL

**Final Verification Checklist:**
1. C-10: Every table header carries `[CLOSES: <label>]` from the blind-spot registry verbatim. List any unlabeled header as NON-COMPLIANT.
2. C-11: Every table's null case was handled as a data row. List any prose substitution as NON-COMPLIANT.
3. C-12: Every Escalation Risk cell populated per GCR-7. List any blank cell as NON-COMPLIANT.

**CA Format Compliance Verdict:** [C-01 through C-05, SHALL-F, SHALL-G, CS-0, GCR compliance. Overall: COMPLIANT / NON-COMPLIANT.]

---

## V-02 -- Single Axis: C-14 (Prohibited Prose Forms Catalog)

**Axis:** C-14 single axis
**Hypothesis:** The R2 V-05 base names one prose-substitution failure by example ("Writing 'No FLS configured. See note above.' instead of this row fails C-11"). C-14 under v3 requires at least one such example naming the criterion violated -- the base already passes. This variation generalizes the technique to every table in the prompt, creating a PROHIBITED PROSE FORMS section that makes every wrong-form path recognizable before selection. The hypothesis: exhaustive coverage of wrong forms eliminates the residual probability that the model substitutes prose at any one of the other four tables.

---

depth: standard
confidence: standard

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

Manual security reviews of Dataverse environments routinely miss three failure scenarios that this
trace is designed to surface:

**Blind spot 1 -- Post-incident FLS gap.** Column security profiles are rarely audited proactively.
Sensitive fields remain readable and writable by any role unless a column security profile
explicitly restricts them. Gaps are discovered after data exposure, not before.

**Blind spot 2 -- Cumulative privilege blind spot.** A user holding a BU-scoped security role who
also belongs to an owner team whose team role grants org-wide access has effective org-wide access.
No single Dataverse UI view surfaces the combined effective access.

**Blind spot 3 -- OWD-sharing-rule override gap.** A Private OWD on Case combined with a
Power Automate-triggered sharing rule grants effective org-wide read to users who satisfy the
trigger condition -- including low-trust service accounts and CS users not intended to have broad
case access.

---

## PROHIBITED PROSE FORMS

These prose forms are structurally prohibited. Each names the wrong form verbatim and the
criterion it violates. Encountering a matching pattern in your own output is a structural failure
-- rewrite using the required data-row format before submission.

**TABLE_1 null case -- fails C-11:**
PROHIBITED: "No roles are currently configured for {{topic}}. Access will be defined in a future
sprint." -- This is prose. Use the null-case data row: `[No roles in scope] | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A`

**TABLE_2 null case -- fails C-11:**
PROHIBITED: "No column security profiles active on {{topic}}. Sensitive fields are exposed to any
role with entity access." -- This is prose. Use the null-case data row:
`[No sensitive fields identified] | N/A | N/A | Not Configured | N/A | N/A | YES`
Writing "No FLS configured. See note above." instead of this row fails C-11.

**TABLE_3 null case -- fails C-11:**
PROHIBITED: "Record scope varies by team membership -- see TABLE_1 for configuration context." --
This is prose. Use the null-case data row: `[Role] | [Tier] | [OWD] | No modifier | [OWD Baseline] | NO`
For any role where Effective Scope > role-only scope, the expansion sentence is REQUIRED in the row's Scope Modifier cell, not as a prose paragraph after the table.

**TABLE_4 rule-out -- fails C-04:**
PROHIBITED: "No escalation paths were found in this environment." -- This is a conclusion without
mechanism. Use the finding format: "Checked [mechanism]: no path found because [specific reason
naming the configuration that prevents escalation]." Every Checked? cell must be YES.

**TABLE_5 remediation -- fails C-07:**
PROHIBITED: "Restrict access to revenue data." -- This is insufficient. Use the exact-object
format: "[Object name] + [exact location in Dataverse admin] + [expected state after fix]."
Example of sufficient remediation: "Create column security profile 'RevenueSensitive'; restrict
Write on estimatedrevenue to Sales Manager role only; confirm No Access for CS User role in the
profile." -- failing C-07 means the gap is named without an actionable path to close it.

**Escalation Risk null -- fails C-12:**
PROHIBITED: "See TABLE_5 for risk details." or leaving the cell blank. -- Use one of the four
declared values: HIGH / MEDIUM / LOW / NONE. "See above" is blank-equivalent and auto-fails.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins.

**PHASE 0 -- CA:** Schema Registry (TABLE_1 through TABLE_5, CS-2, CS-3) and Criterion
Enforcement Matrix preamble (SHALL-A through SHALL-G, CA-1.1 through CA-1.8). Handoff to PHASE 1.

**PHASE 1 -- CS:** CS-0 Registry acknowledgment, then CS-1 / CS-2 / CS-3. Handoff to PHASE 2.

**PHASE 2 -- SE:** Privilege-tier descent. SE-0 (TABLE_4) before SE-1 (TABLE_1). SE-2/3/4 use
exact-label two-part closure blocks per SHALL-G. Handoff to PHASE 3.

**PHASE 3 -- CA-1:** Double-anchor verification rows CA-1.1 through CA-1.8. Final verification
checklist. CA Format Compliance Verdict.

---

## PHASE 0 -- CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

### Step 0.1 -- Schema Registry

**Schema ID: TABLE_1 -- Role-Operation Matrix**
Columns: `Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Tier: Admin / Custom / Restricted. Rows ordered by tier. All cells: Granted / Denied / Conditional / N/A.
Null-case row: `[No roles in scope] | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A`
-- Writing "No roles configured" as prose instead of this row fails C-11.

**Schema ID: TABLE_2 -- FLS Coverage**
Columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
FLS Profile Configured? = Configured / Not Configured (never blank). Gap? = YES / NO.
Null-case row (FIRST DATA ROW when no sensitive fields found):
`[No sensitive fields identified] | N/A | N/A | Not Configured | N/A | N/A | YES`
-- Writing "No column security profiles active. Sensitive fields exposed to any role." instead of
   this row fails C-11.

**Schema ID: TABLE_3 -- Record Scope by Role**
Columns: `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Tier mirrors TABLE_1. Verified? = YES / NO. Effective Scope = Own / BU / Parent-Child BU /
Org-wide / Team-scoped / Sharing-[rule name].
Null-case row: `[Role] | [Tier] | [OWD] | No scope modifier found | [OWD Baseline] | NO`
-- Writing "Scope varies by team configuration -- consult admin" instead of a data row fails C-11.

**Schema ID: TABLE_4 -- Escalation Vector Inventory**
Columns: `Vector | Checked? | Finding | Severity`
All four vectors. Checked? = YES. Finding: escalation path or specific rule-out. Severity: CRITICAL / HIGH / MEDIUM.
-- Writing "No escalation paths found" without per-vector findings fails C-04.

**Schema ID: TABLE_5 -- Security Gap Inventory**
Columns: `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation`
Remediation = exact object + exact location + expected post-fix state.
-- Writing "Restrict access" without the three-part format fails C-07.
CLEARED row: `CLEARED | -- | No gaps found | -- | -- | -- | -- | Evidence: [per-gap-type checks]`

**Schema ID: CS-2 -- Sharing Rule Expectations**
SE-updatable: SE Cross-Reference; SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).

**Schema ID: CS-3 -- Cross-Role Access Differential Expectations**
SE-updatable: SE Cross-Reference; SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).

### Step 0.2 -- Criterion Enforcement Matrix Preamble

| Criterion | Schema | Role Section | SHALL | CA Row |
|-----------|--------|-------------|-------|--------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-0+SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

SHALL-A through SHALL-G: [same as V-01 base -- SHALL-A: TABLE_1 complete; SHALL-B: all PII/Financial/Audit-Compliance fields; SHALL-C: every TABLE_1 role in TABLE_3; SHALL-D: TABLE_4 at SE-0, all vectors, Checked?=YES; SHALL-E: at least one named gap; SHALL-F: CS-EXPECTATION-VIOLATED three-field Remediation; SHALL-G: exact-label two-part closure at SE-2/3/4]

*Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

### CS-0 -- Schema Registry Acknowledgment

**Registry acknowledgment for CS-2:** Schema ID CS-2 confirmed. SE-updatable columns: SE Cross-Reference, SE Confirmation. Left blank; SE fills after SE-0/TABLE_4.

**Registry acknowledgment for CS-3:** Schema ID CS-3 confirmed. SE-updatable columns: SE Cross-Reference, SE Confirmation. Left blank; SE fills after SE-1/SE-3.

### CS-1 -- Expected Customer Service Access Baseline

For each entity: (a) expected CRUD operations; (b) expected record scope; (c) sensitive fields CS needs.

**CS-2 -- Sharing rule expectations** *(SE-updatable columns blank)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

**CS-3 -- Cross-role access differential** *(SE-updatable columns blank)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis

### SE-0 -- Admin-Tier Inventory and Escalation Vectors

**Admin-tier inventory:** System Administrator, Environment Admin, admin-equivalent roles.

**TABLE_4 [CLOSES: CUMULATIVE-PRIVILEGE, SHARING-OVERRIDE] -- Escalation Vector Inventory**

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Rule-out format: "Checked [mechanism]: no path found because [specific reason]." -- Writing "No
escalation paths found" without per-vector findings fails C-04 and violates PROHIBITED PROSE FORMS.

### SE-1 / SHALL-A -- Role-Operation Matrix

**TABLE_1 [CLOSES: CUMULATIVE-PRIVILEGE] -- Role-Operation Matrix**

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|
| [No roles in scope] | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |

Rows ordered Admin / Custom / Restricted. If roles exist, replace null-case row with actual data.

### SE-2 / SHALL-B -- Field-Level Security Coverage

MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:
Column security profiles are not auditable from the security roles UI; administrators discover
missing FLS only after a data exposure event reveals that a sensitive field was readable or
writable by an unintended role.

STRUCTURED CLOSE:
TABLE_2 enumerates every sensitive field in scope with its explicit FLS status, surfacing pre-event
what the security roles UI conceals.

**TABLE_2 [CLOSES: POST-INCIDENT-FLS-GAP] -- FLS Coverage**

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|
| [No sensitive fields identified] | N/A | N/A | Not Configured | N/A | N/A | YES |

Writing "No column security profiles active on {{topic}}. Sensitive fields exposed." instead of
the null-case row above fails C-11. The null case IS the finding -- it must appear as a data row.

### SE-3 / SHALL-C -- Record Access Scope

MANUAL GAP [Blind spot 2 -- Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access produced by role + team + OWD.

STRUCTURED CLOSE:
TABLE_3 maps effective scope for every role by Tier.

**TABLE_3 [CLOSES: CUMULATIVE-PRIVILEGE] -- Record Scope by Role**

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|
| [Role] | [Tier] | [OWD] | No scope modifier found | [OWD Baseline] | NO |

Writing "Scope varies by team configuration" instead of a data row fails C-11.
For any role where team membership expands scope: write the expansion in Scope Modifier cell,
not as prose after the table.

### SE-4 / SHALL-D -- Privilege Escalation Cross-Reference

MANUAL GAP [Blind spot 3 -- OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing sharing rules
that silently override them.

STRUCTURED CLOSE:
TABLE_4 (SE-0) evaluated all four vectors with sharing rules cross-referenced against OWD.

Cross-tier differential: cite SE-0 TABLE_4 data for the gap between most-privileged Admin-tier
and most-restricted Restricted-tier role.

### SE-5 / SHALL-E -- Security Gap Inventory

**ESCALATION RISK SCALE** (before Closing Summary)
HIGH: role combination produces access materially exceeding job function.
MEDIUM: limited-scope excess access; low blast radius.
LOW: minor excess; unlikely to be exploited.
NONE: access appropriate; no escalation vector confirmed.
Auto-fail: blank Escalation Risk cell auto-fails. "See above" is blank-equivalent.

**TABLE_5 [CLOSES: ALL-GAPS] -- Security Gap Inventory**

| # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation |
|---|----------|--------|---------------|------|------|----------|-------------|
| CLEARED | -- | No gaps found | -- | -- | -- | -- | Evidence: [per-gap-type checks] |

Writing "Restrict access to [field]" without exact object + location + post-fix state fails C-07
and violates PROHIBITED PROSE FORMS.

**Closing Summary**

| Role | FLS Status | Record Scope | Escalation Risk |
|------|-----------|-------------|----------------|
| [Role] | [Configured / Not Configured] | [Scope] | [HIGH / MEDIUM / LOW / NONE] |

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

**CA-1.1:** Registry anchor TABLE_1. Preamble anchor C-01/SE-1/SHALL-A. -> PASS / FAIL
**CA-1.2:** Registry anchor TABLE_2 null-case row. Preamble anchor C-02/SE-2/SHALL-B. -> PASS / FAIL
**CA-1.3:** Registry anchor TABLE_3. Preamble anchor C-03/SE-3/SHALL-C. -> PASS / FAIL
**CA-1.4:** Registry anchor TABLE_4 all-YES. Preamble anchor C-04/SE-0/SHALL-D. -> PASS / FAIL
**CA-1.5:** Registry anchor TABLE_5. Preamble anchor C-05/SE-5/SHALL-E. -> PASS / FAIL
**CA-1.6:** CS-EXPECTATION-VIOLATED three-field blocks. -> PASS / FAIL per row.
**CA-1.7:** SE-2/3/4 exact-label two-part closure blocks. -> PASS / FAIL per section.
**CA-1.8:** CS-0 acknowledgment precedes CS-1. Both schema IDs cited. -> PASS / FAIL

**Final Verification Checklist:**
1. C-10: Every table header carries `[CLOSES: <label>]` verbatim. List any unlabeled header as NON-COMPLIANT.
2. C-11: Every table's null case is a data row. List any prose substitution -- including any form listed in PROHIBITED PROSE FORMS above -- as NON-COMPLIANT.
3. C-12: Every Escalation Risk cell is HIGH / MEDIUM / LOW / NONE. List any blank as NON-COMPLIANT.

**CA Format Compliance Verdict:** [C-01 through C-05, SHALL-F, SHALL-G, CS-0 acknowledgment. Overall: COMPLIANT / NON-COMPLIANT.]

---

## V-03 -- Single Axis: C-15 (Full Aspirational Self-Verification Checklist)

**Axis:** C-15 single axis
**Hypothesis:** The R2 V-05 base has a 3-item checklist covering C-10/C-11/C-12. Under v3 C-15 this already passes (>=3 aspirational criteria, named by ID, explicit compliance checks). This variation replaces it with an 8-item structured table covering ALL aspirational criteria C-08..C-15. The hypothesis: an 8-item table with PASS condition and FAIL signal per criterion makes aspirational omission self-diagnosing at every criterion, not just the three most structurally enforced ones. It also future-proofs against rubric expansion -- new aspirational criteria added to the checklist automatically get a verification row.

---

depth: standard
confidence: standard

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

Manual security reviews routinely miss three failure scenarios this trace closes:

**Blind spot 1 -- Post-incident FLS gap.** Column security profiles are rarely audited proactively;
sensitive fields remain accessible until a data exposure event.

**Blind spot 2 -- Cumulative privilege blind spot.** Role + team + OWD combinations produce
effective access not visible in any single Dataverse UI view.

**Blind spot 3 -- OWD-sharing-rule override gap.** A Private OWD combined with an active sharing
rule (including Power Automate-triggered rules) can grant effective org-wide read to low-trust
service accounts and CS users not intended to have broad access.

---

## ROLE SEQUENCING MANDATE

Four phases. PHASE 0 (CA schema registry) -> PHASE 1 (CS baseline) -> PHASE 2 (SE analysis,
privilege-tier descent) -> PHASE 3 (CA-1 verification + full aspirational audit table).

---

## PHASE 0 -- CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

### Step 0.1 -- Schema Registry

**Schema ID: TABLE_1** -- `Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Tier: Admin / Custom / Restricted. Rows ordered by tier. Cells: Granted / Denied / Conditional / N/A.
Null-case row template: `[No roles in scope] | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A`

**Schema ID: TABLE_2** -- `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
FLS Profile Configured? = Configured / Not Configured. Gap? = YES / NO. Never blank.
Null-case row template (FIRST DATA ROW): `[No sensitive fields] | N/A | N/A | Not Configured | N/A | N/A | YES`
Writing "No column security profiles active. See analysis." instead of this row fails C-11.

**Schema ID: TABLE_3** -- `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Every TABLE_1 role must appear. Null-case row: `[Role] | [Tier] | [OWD] | No modifier | [OWD Baseline] | NO`

**Schema ID: TABLE_4** -- `Vector | Checked? | Finding | Severity`
All four vectors. Checked? = YES. Severity: CRITICAL / HIGH / MEDIUM.

**Schema ID: TABLE_5** -- `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation`
Remediation = exact object + exact location + post-fix state. CLEARED row when no gaps found.
CS-EXPECTATION-VIOLATED: three-field Remediation block (CS-Expected / SE-Actual / Delta).

**Schema ID: CS-2** -- SE-updatable: SE Cross-Reference; SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).

**Schema ID: CS-3** -- SE-updatable: SE Cross-Reference; SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).

### Step 0.2 -- Criterion Enforcement Matrix Preamble

| Criterion | Schema | Role Section | SHALL | CA Row |
|-----------|--------|-------------|-------|--------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-0+SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

SHALL-A: TABLE_1 complete, Tier, ordered. SHALL-B: all sensitive fields, FLS explicit, null case as data row. SHALL-C: every TABLE_1 role in TABLE_3, Effective Scope filled. SHALL-D: TABLE_4 before SE-1, all vectors Checked?=YES. SHALL-E: at least one named gap or CLEARED evidence. SHALL-F: CS-EXPECTATION-VIOLATED three-field Remediation. SHALL-G: exact-label two-part closure blocks at SE-2/SE-3/SE-4.

*Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS

### CS-0 -- Schema Registry Acknowledgment

CS-2 acknowledged: SE-updatable columns SE Cross-Reference and SE Confirmation; left blank for SE.
CS-3 acknowledged: SE-updatable columns SE Cross-Reference and SE Confirmation; left blank for SE.

### CS-1 / CS-2 / CS-3

CS-1 baseline: expected operations, record scope, sensitive field access per entity.

CS-2 sharing rule expectations *(SE-updatable blank)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

CS-3 cross-role differential *(SE-updatable blank)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis

### SE-0

Admin-tier inventory. TABLE_4 [CLOSES: CUMULATIVE-PRIVILEGE, SHARING-OVERRIDE]:

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation | YES | | |
| Admin / environment role override | YES | | |

Finding format: confirmed `[Role] -> [Mechanism] -> [Elevated access]` or rule-out "Checked [mechanism]: no path because [specific reason]". Update CS-2 SE columns after TABLE_4.

### SE-1 / SHALL-A

TABLE_1 [CLOSES: CUMULATIVE-PRIVILEGE]:

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|
| [No roles in scope] | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |

Update CS-3 SE columns after TABLE_1.

### SE-2 / SHALL-B

MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:
Column security profiles are not auditable from the security roles UI; administrators discover missing FLS only after a data exposure event reveals that a sensitive field was readable or writable by an unintended role.

STRUCTURED CLOSE:
TABLE_2 enumerates every sensitive field with explicit FLS status, surfacing pre-event what the security roles UI conceals.

TABLE_2 [CLOSES: POST-INCIDENT-FLS-GAP]:

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|
| [No sensitive fields identified] | N/A | N/A | Not Configured | N/A | N/A | YES |

Writing "No column security profiles active on {{topic}}. Sensitive fields exposed to any role with entity access." instead of the null-case row fails C-11.

### SE-3 / SHALL-C

MANUAL GAP [Blind spot 2 -- Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access produced by role + team + OWD; spot-checking individual roles misses cross-role accumulation through team inheritance.

STRUCTURED CLOSE:
TABLE_3 maps effective scope for every role by Tier, making team-accumulated privilege visible and auditable.

TABLE_3 [CLOSES: CUMULATIVE-PRIVILEGE]:

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|
| [Role] | [Tier] | [OWD] | No scope modifier found | [OWD Baseline] | NO |

Every TABLE_1 role MUST appear. For any role where team membership expands scope:
"[Role] acquires [scope] through [team/rule name]. Base role scope was [base scope]."

### SE-4 / SHALL-D

MANUAL GAP [Blind spot 3 -- OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing sharing rules that silently override them; a Private OWD combined with an active sharing rule can grant effective org-wide access without appearing in any security roles UI view.

STRUCTURED CLOSE:
TABLE_4 (SE-0) evaluated all four escalation vectors with sharing rules explicitly cross-referenced against OWD settings.

### SE-5 / SHALL-E

ESCALATION RISK SCALE (before Closing Summary):
HIGH: role combination produces access materially exceeding job function.
MEDIUM: limited-scope excess; low blast radius.
LOW: minor excess; unlikely to be exploited.
NONE: access appropriate; no escalation vector confirmed.
Auto-fail: blank Escalation Risk cell auto-fails. "See above" is blank-equivalent.

TABLE_5 [CLOSES: ALL-GAPS]:

| # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation |
|---|----------|--------|---------------|------|------|----------|-------------|
| CLEARED | -- | No gaps found | -- | -- | -- | -- | Evidence: [per-gap-type] |

Closing Summary:

| Role | FLS Status | Record Scope | Escalation Risk |
|------|-----------|-------------|----------------|

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Verification + Full Aspirational Audit Table

**CA-1.1:** Registry anchor TABLE_1. Preamble C-01/SE-1/SHALL-A. -> PASS / FAIL
**CA-1.2:** Registry anchor TABLE_2 null-case row. Preamble C-02/SE-2/SHALL-B. -> PASS / FAIL
**CA-1.3:** Registry anchor TABLE_3. Preamble C-03/SE-3/SHALL-C. -> PASS / FAIL
**CA-1.4:** Registry anchor TABLE_4. Preamble C-04/SE-0/SHALL-D. -> PASS / FAIL
**CA-1.5:** Registry anchor TABLE_5. Preamble C-05/SE-5/SHALL-E. -> PASS / FAIL
**CA-1.6:** CS-EXPECTATION-VIOLATED Remediation blocks. -> PASS / FAIL per row.
**CA-1.7:** SE-2/3/4 exact-label two-part closure blocks. -> PASS / FAIL per section.
**CA-1.8:** CS-0 acknowledgment. -> PASS / FAIL

---

### ASPIRATIONAL CRITERIA SELF-VERIFICATION TABLE

Inspect your output against each criterion below. Mark PASS or FAIL with evidence. Submit only
when all items show PASS or explicitly acknowledge FAIL with reason.

| ID | Criterion | PASS Condition | FAIL Signal | Self-Assessment |
|----|-----------|---------------|------------|-----------------|
| C-08 | Cross-Entity Cascade | At least one cross-entity cascade: parent entity, child entity, mechanism cited | No cross-entity cascade mechanism anywhere in output | PASS / FAIL: [evidence] |
| C-09 | Structured Summary Table | Closing Summary present with >= 3 columns (role, FLS status, record scope), every row populated | Closing Summary absent or has blank cells | PASS / FAIL: [evidence] |
| C-10 | Blind-Spot-Labeled Tables | Every table/section header has `[CLOSES: <label>]` from CONTEXT verbatim. List any unlabeled header | Any table header missing closes annotation | PASS / FAIL: [list unlabeled or COMPLIANT] |
| C-11 | Data-Row Null-Case Mandate | Every table's null case is a data row. No prose disclaimers replacing the null-case row | Any table has prose where the null-case row template should appear | PASS / FAIL: [list prose violations or COMPLIANT] |
| C-12 | Escalation Risk Column | Every Closing Summary Escalation Risk cell is HIGH / MEDIUM / LOW / NONE. List any blank | Any blank or non-declared Escalation Risk cell | PASS / FAIL: [list blanks or COMPLIANT] |
| C-13 | Pre-Declared Scale with Auto-Fail | The ESCALATION RISK SCALE section names all four levels with definitions, states auto-fail for blank, and the verification row checks compliance | Scale absent, auto-fail condition absent, or verification absent | PASS / FAIL: [evidence] |
| C-14 | Prose-Substitution Failure Mode Named by Example | At least one structural requirement shows the wrong prose form verbatim AND names the criterion it violates | Only generic warnings ("avoid prose") without specific example and criterion citation | PASS / FAIL: [cite example] |
| C-15 | Self-Verification Checklist | This table is present after the main output body with >= 3 aspirational criteria, each named by ID, with explicit self-assessment | Generic completion signal without per-criterion assessment by ID | PASS: this table satisfies C-15 if populated |

**CA Format Compliance Verdict:** [C-01 through C-05, SHALL-F, SHALL-G, CS-0 acknowledgment, aspirational audit table. Overall: COMPLIANT / NON-COMPLIANT.]

---

## V-04 -- Combined: C-13 + C-14 (Graded Column Registry + Prohibited Prose Forms)

**Axis:** C-13 + C-14 combined
**Hypothesis:** V-01 adds registry-level scale declarations (C-13) and V-02 adds wrong-form examples at every table (C-14). Combined, they create a dual enforcement layer: the registry declares what a valid cell looks like (scale enforcement before output), and the prohibited forms declare what an invalid form looks like (prose enforcement at selection time). Neither alone prevents the other's failure mode: a model could know the scale but still write a prose null case; a model could avoid prose but use wrong scale values. Together they close both sides of the structural failure space.

---

depth: standard
confidence: standard

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

**Blind spot 1 -- Post-incident FLS gap.** Column security profiles are not proactively audited;
sensitive fields remain accessible until data exposure.

**Blind spot 2 -- Cumulative privilege blind spot.** Role + team + OWD combinations produce
effective access invisible in any single Dataverse UI view.

**Blind spot 3 -- OWD-sharing-rule override gap.** Private OWD + Power Automate sharing rule =
effective org-wide read to low-trust accounts and CS users not intended for broad access.

---

## GRADED COLUMN REGISTRY (CA-authored, before any table)

All graded column scales declared here. Every cell in every table must match its registered values.
A cell not matching its scale is blank-equivalent and auto-fails verification.

**GCR-1 -- Tier:** `Admin` / `Custom` / `Restricted`
Auto-fail: any non-declared value. Post-table: verify all Tier cells match GCR-1.

**GCR-2 -- Severity:** `CRITICAL` / `HIGH` / `MEDIUM`
CRITICAL = exploitable immediately. HIGH = one intermediate step. MEDIUM = limited blast radius.
Auto-fail: blank or non-declared value. Post-table: list any non-compliant cell.

**GCR-3 -- Checked?:** `YES` (examined, finding written) / `NO` (auto-fail)
Auto-fail: any NO or blank. All four TABLE_4 vectors must be YES.

**GCR-4 -- Verified?:** `YES` (confirmed against config) / `NO` (inferred)
Auto-fail: blank = NO. NO rows flagged as unconfirmed in post-table check.

**GCR-5 -- FLS Profile Configured?:** `Configured` / `Not Configured`
Auto-fail: blank or any other value.

**GCR-6 -- Gap?:** `YES` / `NO`. Every YES must have TABLE_5 entry.
Auto-fail: blank. Post-table: verify every YES has cross-reference.

**GCR-7 -- Escalation Risk:** `HIGH` / `MEDIUM` / `LOW` / `NONE`
HIGH = materially exceeds job function. MEDIUM = limited scope. LOW = minor. NONE = appropriate.
Auto-fail: blank or "see above". Post-table: list any non-compliant cell.

---

## PROHIBITED PROSE FORMS

Wrong-form examples for every table. Each names the criterion violated.

**TABLE_1 null case -- fails C-11:**
PROHIBITED: "No roles currently configured. Access TBD."
REQUIRED: null-case data row `[No roles in scope] | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A`

**TABLE_2 null case -- fails C-11:**
PROHIBITED: "No column security profiles active on {{topic}}. Sensitive fields exposed."
REQUIRED: `[No sensitive fields identified] | N/A | N/A | Not Configured | N/A | N/A | YES`
Writing "No FLS configured. See note above." instead of this row fails C-11.

**TABLE_3 null case -- fails C-11:**
PROHIBITED: "Scope varies by team membership -- see TABLE_1."
REQUIRED: `[Role] | [Tier] | [OWD] | No modifier found | [OWD Baseline] | NO`

**TABLE_4 rule-out -- fails C-04:**
PROHIBITED: "No escalation paths identified."
REQUIRED: "Checked [mechanism]: no path found because [specific configuration reason]."

**TABLE_5 remediation -- fails C-07:**
PROHIBITED: "Restrict access to sensitive data."
REQUIRED: "[Exact object name] + [exact location in Dataverse] + [expected post-fix state]."

**Escalation Risk blank -- fails C-12:**
PROHIBITED: blank cell or "See TABLE_5."
REQUIRED: one of GCR-7 values: HIGH / MEDIUM / LOW / NONE.

---

## ROLE SEQUENCING MANDATE

PHASE 0 (CA) -> PHASE 1 (CS) -> PHASE 2 (SE, privilege-tier descent) -> PHASE 3 (CA-1).
Each phase completes before the next begins. Phase labels as section headers.

---

## PHASE 0 -- CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

### Step 0.1 -- Schema Registry

**TABLE_1:** `Role | Tier(GCR-1) | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Rows ordered Admin / Custom / Restricted. All operation cells: Granted / Denied / Conditional / N/A.
Null-case row: `[No roles in scope] | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A`
-- Writing "No roles configured" as prose instead of this row fails C-11 (PROHIBITED PROSE FORMS).

**TABLE_2:** `Entity | Field | Category | FLS Profile Configured?(GCR-5) | Roles: Read | Roles: Write | Gap?(GCR-6)`
Null-case row (FIRST DATA ROW): `[No sensitive fields] | N/A | N/A | Not Configured | N/A | N/A | YES`
-- Writing "No FLS profiles active. Sensitive fields exposed." instead fails C-11.

**TABLE_3:** `Role | Tier(GCR-1) | OWD Baseline | Scope Modifier | Effective Scope | Verified?(GCR-4)`
Null-case row: `[Role] | [Tier] | [OWD] | No modifier | [OWD Baseline] | NO`
-- Writing "Scope varies by configuration" instead of a data row fails C-11.

**TABLE_4:** `Vector | Checked?(GCR-3) | Finding | Severity(GCR-2)`
Four vectors. All Checked? = YES per GCR-3.
-- Writing "No escalation paths found" without per-vector findings fails C-04.

**TABLE_5:** `# | Gap Type | Entity | Field or Rule | Role | Tier(GCR-1) | Severity(GCR-2) | Remediation`
Remediation: exact object + location + post-fix state.
CLEARED row: `CLEARED | -- | No gaps | -- | -- | -- | -- | Evidence: [checks]`
-- Writing "Restrict access" without the three-part format fails C-07.

**CS-2 / CS-3:** SE-updatable columns (SE Cross-Reference; SE Confirmation) left blank by CS; SE fills.

### Step 0.2 -- Enforcement Preamble

| C | Schema | Section | SHALL | CA-1 |
|---|--------|---------|-------|------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

SHALL-A through SHALL-G apply. SHALL-G: exact-label two-part closure at SE-2/SE-3/SE-4.

*Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS

CS-0: acknowledge CS-2 (SE-updatable: SE Cross-Reference, SE Confirmation) and CS-3 (same) before authoring expectations.
CS-1: expected operations, scope, sensitive field access.
CS-2 / CS-3: fill expectation rows; leave SE columns blank.

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE

### SE-0
Admin-tier inventory. TABLE_4 [CLOSES: CUMULATIVE-PRIVILEGE, SHARING-OVERRIDE]:

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation | YES | | |
| Admin / environment role override | YES | | |

### SE-1 / SHALL-A
TABLE_1 [CLOSES: CUMULATIVE-PRIVILEGE]:

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|
| [No roles in scope] | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |

### SE-2 / SHALL-B

MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:
Column security profiles are not auditable from the security roles UI; administrators discover missing FLS only after a data exposure event reveals that a sensitive field was readable or writable by an unintended role.

STRUCTURED CLOSE:
TABLE_2 enumerates every sensitive field with explicit FLS status per GCR-5.

TABLE_2 [CLOSES: POST-INCIDENT-FLS-GAP]:

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|
| [No sensitive fields identified] | N/A | N/A | Not Configured | N/A | N/A | YES |

Writing "No column security profiles active on {{topic}}. Sensitive fields exposed to any role with entity access." instead of the null-case row fails C-11 (see PROHIBITED PROSE FORMS).

### SE-3 / SHALL-C

MANUAL GAP [Blind spot 2 -- Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access produced by role + team + OWD; spot-checking misses cross-role accumulation.

STRUCTURED CLOSE:
TABLE_3 maps effective scope per role per Tier (GCR-1), making team-accumulated privilege auditable.

TABLE_3 [CLOSES: CUMULATIVE-PRIVILEGE]:

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|
| [Role] | [Tier] | [OWD] | No modifier found | [OWD Baseline] | NO |

Writing "Scope varies by team membership" instead of a data row fails C-11.

### SE-4 / SHALL-D

MANUAL GAP [Blind spot 3 -- OWD-sharing-rule override gap]:
Administrators audit OWD entity-by-entity without cross-referencing sharing rules that silently override those baselines.

STRUCTURED CLOSE:
TABLE_4 (SE-0) evaluated all four vectors with sharing rules cross-referenced against OWD.

### SE-5 / SHALL-E

ESCALATION RISK SCALE [GCR-7; placed before Closing Summary]:
HIGH / MEDIUM / LOW / NONE as declared in GCR-7.
Auto-fail: blank or "see above" in any Escalation Risk cell.
Post-table: list any blank as NON-COMPLIANT.

TABLE_5 [CLOSES: ALL-GAPS]:

| # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation |
|---|----------|--------|---------------|------|------|----------|-------------|
| CLEARED | -- | No gaps found | -- | -- | -- | -- | Evidence: [per-gap-type] |

Writing "Restrict access" without exact object + location + post-fix state fails C-07 (PROHIBITED PROSE FORMS).

Closing Summary:

| Role | FLS Status | Record Scope | Escalation Risk |
|------|-----------|-------------|----------------|

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Verification

CA-1.1 through CA-1.8 (double-anchor: Registry anchor + Preamble anchor + Verification per criterion).

**CA-1.9 -- Graded Column Registry compliance:**
GCR-1 Tier values correct in TABLE_1/TABLE_3? GCR-2 Severity in TABLE_4/TABLE_5? GCR-3 all Checked?=YES in TABLE_4? GCR-4 Verified? in TABLE_3? GCR-5 FLS Profile Configured? in TABLE_2? GCR-6 Gap? with TABLE_5 cross-reference? GCR-7 Escalation Risk in Closing Summary? -> PASS / FAIL per GCR entry.

**Final Verification Checklist:**
1. C-10: Every table header carries `[CLOSES: <label>]` verbatim. List unlabeled headers as NON-COMPLIANT.
2. C-11: Every table null case is a data row. List any prose form from PROHIBITED PROSE FORMS as NON-COMPLIANT.
3. C-12: Every Escalation Risk cell is HIGH / MEDIUM / LOW / NONE per GCR-7. List blanks as NON-COMPLIANT.

**CA Format Compliance Verdict:** [COMPLIANT / NON-COMPLIANT.]

---

## V-05 -- Full Integration: C-13 + C-14 + C-15 All Hardened

**Axis:** Full integration
**Hypothesis:** V-01 (Graded Column Registry) + V-02 (Prohibited Prose Forms) + V-03 (Full 8-item aspirational checklist) combined. Every structural requirement has: (1) a pre-declared scale with auto-fail (C-13), (2) a named wrong form example citing which criterion it violates (C-14), and (3) a self-verification row in the final audit table (C-15). A model following this prompt can verify its own compliance against all 15 criteria without external scoring.

---

depth: standard
confidence: standard

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

Manual security reviews routinely miss three failure scenarios this trace closes:

**Blind spot 1 -- Post-incident FLS gap.** Column security profiles are not proactively audited.
Sensitive fields remain readable/writable by any role until after data exposure.

**Blind spot 2 -- Cumulative privilege blind spot.** Role + team + OWD accumulation is invisible
in any single Dataverse UI view. Spot-checking misses cross-role privilege through team membership.

**Blind spot 3 -- OWD-sharing-rule override gap.** A Private OWD combined with a Power
Automate-triggered sharing rule grants effective org-wide read to low-trust service accounts and
CS users not intended for broad case access, without appearing in any security roles UI view.

This trace closes all three: SE-2 closes Blind spot 1; SE-3 closes Blind spot 2; SE-4 closes Blind spot 3.

---

## GRADED COLUMN REGISTRY (GCR)

All graded column scales declared before any table. Every cell must match its registered values.
A cell not matching is blank-equivalent and auto-fails its table's verification check.

| GCR | Column | Scale (every level named) | Auto-Fail Condition | Post-Table Verification |
|-----|--------|--------------------------|--------------------|-----------------------|
| GCR-1 | Tier | Admin / Custom / Restricted | Any non-declared value | List any Tier cell not in {Admin, Custom, Restricted} as NON-COMPLIANT |
| GCR-2 | Severity | CRITICAL (immediate exploit) / HIGH (one intermediate step) / MEDIUM (limited blast radius) | Blank or non-declared | List any non-compliant Severity cell |
| GCR-3 | Checked? | YES (examined, finding written) / NO (auto-fail: blocks TABLE_4 verification) | Any NO or blank = TABLE_4 FAIL | All four vectors must show YES before TABLE_4 closes |
| GCR-4 | Verified? | YES (confirmed against config) / NO (inferred -- flag as gap) | Blank treated as NO | List all NO rows as unconfirmed scope requiring follow-up |
| GCR-5 | FLS Profile Configured? | Configured / Not Configured | Any other value | Confirm every cell is one of the two declared values |
| GCR-6 | Gap? | YES / NO (every YES requires TABLE_5 entry) | Blank | Verify every YES row has TABLE_5 cross-reference |
| GCR-7 | Escalation Risk | HIGH (materially exceeds job function) / MEDIUM (limited scope excess) / LOW (minor, unlikely exploited) / NONE (appropriate, no escalation confirmed) | Blank or "see above" = auto-fail | List any blank or non-declared Escalation Risk cell as NON-COMPLIANT |

---

## PROHIBITED PROSE FORMS

Each entry names the wrong form verbatim and the criterion it violates.
Finding a prohibited form in your output is a structural failure -- replace with the required data row.

| Table | Prohibited Form | Criterion Violated | Required Form |
|-------|----------------|-------------------|--------------|
| TABLE_1 null case | "No roles currently configured for {{topic}}. Access TBD." | C-11 | `[No roles in scope] \| N/A \| N/A \| N/A \| N/A \| N/A \| N/A \| N/A \| N/A \| N/A \| N/A` |
| TABLE_2 null case | "No column security profiles active on {{topic}}. Sensitive fields exposed to any role with entity access." | C-11 | `[No sensitive fields] \| N/A \| N/A \| Not Configured \| N/A \| N/A \| YES` |
| TABLE_2 null case variant | "No FLS configured. See note above." | C-11 | Same null-case data row as above |
| TABLE_3 null case | "Scope varies by team membership -- consult admin." | C-11 | `[Role] \| [Tier] \| [OWD] \| No modifier found \| [OWD Baseline] \| NO` |
| TABLE_4 rule-out | "No escalation paths identified in this environment." | C-04 | "Checked [mechanism]: no path found because [specific configuration reason]" |
| TABLE_5 remediation | "Restrict access to [field/entity]." | C-07 | "[Exact object] + [exact Dataverse location] + [expected post-fix state]" |
| Escalation Risk | blank cell or "See TABLE_5 for risk assessment." | C-12 | One of GCR-7 values: HIGH / MEDIUM / LOW / NONE |

---

## ROLE SEQUENCING MANDATE

Four phases. Each completes fully before the next begins. Phase labels as section headers.

**PHASE 0 -- CA:** Schema Registry (TABLE_1 through TABLE_5, CS-2, CS-3; seven schemas). Criterion
Enforcement Matrix preamble (SHALL-A through SHALL-G; CA-1.1 through CA-1.8 pre-assigned). Handoff to PHASE 1.

**PHASE 1 -- CS:** CS-0 Schema Registry acknowledgment (both CS-2 and CS-3 by exact label, SE-updatable
columns named, before any expectation rows). CS-1 / CS-2 / CS-3. Handoff to PHASE 2.

**PHASE 2 -- SE:** Privilege-tier descent. SE-0 (TABLE_4) before SE-1 (TABLE_1). SE-2 / SE-3 / SE-4
use exact-label two-part closure blocks per SHALL-G. SE-4 cites SE-0. Handoff to PHASE 3.

**PHASE 3 -- CA-1:** Double-anchor verification rows (CA-1.1 through CA-1.8). GCR compliance check.
Full aspirational criteria self-verification table. CA Format Compliance Verdict.

---

## PHASE 0 -- CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

### Step 0.1 -- Schema Registry

**Schema ID: TABLE_1 -- Role-Operation Matrix**
Columns: `Role | Tier(GCR-1) | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Row order: Admin tier first, Custom second, Restricted last per GCR-1. All operation cells: Granted / Denied / Conditional (condition inline) / N/A. No blank cells.
Null-case row: `[No roles in scope] | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A`
-- Writing "No roles configured for {{topic}}." instead of this row fails C-11.

**Schema ID: TABLE_2 -- FLS Coverage**
Columns: `Entity | Field | Category | FLS Profile Configured?(GCR-5) | Roles: Read | Roles: Write | Gap?(GCR-6)`
Categories: PII / Financial / Audit-Compliance / Other-Sensitive. Gap? YES rows -> TABLE_5 MISSING-FLS.
Null-case row (FIRST DATA ROW when no sensitive fields found):
`[No sensitive fields identified] | N/A | N/A | Not Configured | N/A | N/A | YES`
-- Writing "No column security profiles active. Sensitive fields exposed to any role with entity access." instead of this row fails C-11.
-- Writing "No FLS configured. See note above." instead of this row also fails C-11.
SE-updatable note: System Administrator bypasses column security profiles (SE-0 confirmed).

**Schema ID: TABLE_3 -- Record Scope by Role**
Columns: `Role | Tier(GCR-1) | OWD Baseline | Scope Modifier | Effective Scope | Verified?(GCR-4)`
Every TABLE_1 role must appear. Effective Scope: Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].
Null-case row: `[Role] | [Tier] | [OWD] | No scope modifier found | [OWD Baseline] | NO`
-- Writing "Scope varies by team membership -- consult admin." instead of a data row fails C-11.
For any role where team membership expands scope: write expansion in Scope Modifier cell.

**Schema ID: TABLE_4 -- Escalation Vector Inventory**
Columns: `Vector | Checked?(GCR-3) | Finding | Severity(GCR-2)`
Four vectors (Team inheritance / Sharing rules / Impersonation / Admin override). All Checked? = YES.
Finding: `[Role] -> [Mechanism] -> [Elevated access]` or "Checked [mechanism]: no path because [specific reason]."
-- Writing "No escalation paths identified." without per-vector findings fails C-04.

**Schema ID: TABLE_5 -- Security Gap Inventory**
Columns: `# | Gap Type | Entity | Field or Rule | Role | Tier(GCR-1) | Severity(GCR-2) | Remediation`
Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.
Remediation = exact object + exact Dataverse location + expected post-fix state.
-- Writing "Restrict access to [data]." without the three-part format fails C-07.
CLEARED row (when no gaps): `CLEARED | -- | No gaps found | -- | -- | -- | -- | Evidence: [per-type confirmation]`
CS-EXPECTATION-VIOLATED Remediation: CS-Expected: [cite row] / SE-Actual: [finding] / Delta: [config change].

**Schema ID: CS-2 -- Sharing Rule Expectations**
Columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference (TABLE_4 or TABLE_5 row ID); SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE protocol: populate after TABLE_4 analysis at SE-0. CONTRADICTED -> TABLE_5 CS-EXPECTATION-VIOLATED per SHALL-F.

**Schema ID: CS-3 -- Cross-Role Access Differential Expectations**
Columns: `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference (TABLE_1 or TABLE_3 row ID); SE Confirmation.
SE protocol: populate after TABLE_1/TABLE_3 analysis. CONTRADICTED -> TABLE_5 CS-EXPECTATION-VIOLATED.

### Step 0.2 -- Criterion Enforcement Matrix Preamble

**M1, M2, M3 simultaneously active. M4 pre-assigned. GCR values override all inline declarations.**

| Criterion | Schema | Role Section | SHALL | CA-1 Row |
|-----------|--------|-------------|-------|---------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-0+SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**SHALL obligations:**
- SHALL-A: TABLE_1 complete with Tier (GCR-1). All cells Granted/Denied/Conditional/N/A. Rows ordered by tier.
- SHALL-B: TABLE_2 lists all PII, Financial, Audit-Compliance fields. FLS status per GCR-5. Gap? per GCR-6. Null case as data row.
- SHALL-C: Every TABLE_1 role in TABLE_3. Tier per GCR-1. Effective Scope filled. Ambiguous scope -> TABLE_5.
- SHALL-D: TABLE_4 at SE-0 before SE-1. All four vectors. Checked? = YES per GCR-3. Severity per GCR-2.
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap requires CLEARED row with per-type evidence.
- SHALL-F: CS-EXPECTATION-VIOLATED rows carry three-field Remediation (CS-Expected / SE-Actual / Delta). Incomplete rows reopened. CA-1.6 verifies.
- SHALL-G: SE-2/SE-3/SE-4 each open with two-part exact-label closure block. Line 1: `MANUAL GAP [<exact CONTEXT label>]:` (character-for-character). Line 3: `STRUCTURED CLOSE:`. Paraphrase, single-line, or TABLE_5 consolidation fails SHALL-G. CA-1.7 verifies.

*Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

### CS-0 -- Schema Registry Acknowledgment

Before authoring any expectation rows, CS echoes the Schema Registry entries for CS-2 and CS-3.

**Registry acknowledgment for CS-2:**
Schema ID: CS-2 -- Sharing Rule Expectations.
SE-updatable columns as declared in Phase 0: SE Cross-Reference (TABLE_4 or TABLE_5 row ID), SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE-update protocol acknowledged: SE fills after SE-0/TABLE_4. CONTRADICTED -> TABLE_5 CS-EXPECTATION-VIOLATED.
Expectation format confirmed: Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation.
SE-updatable columns left blank by CS.

**Registry acknowledgment for CS-3:**
Schema ID: CS-3 -- Cross-Role Access Differential Expectations.
SE-updatable columns as declared in Phase 0: SE Cross-Reference (TABLE_1 or TABLE_3 row ID), SE Confirmation.
SE-update protocol acknowledged: SE fills after TABLE_1/TABLE_3 analysis. CONTRADICTED -> TABLE_5.
Expectation format confirmed. SE-updatable columns left blank by CS.

### CS-1 -- Expected Customer Service Access Baseline

For each entity in scope: (a) expected CRUD operations per normal job function; (b) expected record scope; (c) sensitive fields CS needs and why. Identify configurations that may open access beyond job requirements.

**CS-2 -- Sharing rule expectations** *(SE-updatable columns blank)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

For each Potential Overreach? YES: name the access path and most likely over-reached role.

**CS-3 -- Cross-role access differential** *(SE-updatable columns blank)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

State at minimum one entity and one operation where CS has less access than the Comparison Role.

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis (Privilege-Tier Descent)

### SE-0 -- Admin-Tier Inventory and Escalation Vectors

**Admin-tier inventory:** List System Administrator, Environment Admin, admin-equivalent roles.
Note capabilities that bypass lower-tier controls (e.g., System Administrator bypasses column
security profiles -- this establishes the privilege ceiling for all SE-1 roles).

**TABLE_4 [CLOSES: CUMULATIVE-PRIVILEGE, SHARING-OVERRIDE] -- Escalation Vector Inventory**
*(GCR-3 for Checked?, GCR-2 for Severity; TABLE_4 executes before SE-1)*

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Finding: `[Role] -> [Mechanism] -> [Elevated access achieved]` for confirmed paths; "Checked [mechanism]: no path found because [specific reason]" for rule-outs.
-- "No escalation paths identified." without per-vector findings fails C-04 (PROHIBITED PROSE FORMS).
After TABLE_4: populate CS-2 SE Cross-Reference and SE Confirmation. CONTRADICTED -> CS-EXPECTATION-VIOLATED per SHALL-F.

### SE-1 / SHALL-A -- Role-Operation Matrix

**TABLE_1 [CLOSES: CUMULATIVE-PRIVILEGE] -- Role-Operation Matrix**
*(GCR-1 for Tier; TABLE_1 follows SE-0 because admin-tier ceiling established)*

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|
| [No roles in scope] | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A |

Rows ordered: Admin first, Custom second, Restricted last per GCR-1.
After TABLE_1: populate CS-3 SE Cross-Reference and SE Confirmation. CONTRADICTED -> CS-EXPECTATION-VIOLATED.
Cross-role differential: compare CS role against one Admin-tier and one Custom-tier role for same entity/operation.

### SE-2 / SHALL-B -- Field-Level Security Coverage

MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:
Column security profiles are not auditable from the security roles UI; administrators discover
missing FLS only after a data exposure event reveals that a sensitive field was readable or
writable by an unintended role.

STRUCTURED CLOSE:
TABLE_2 enumerates every sensitive field in scope with its explicit FLS status (GCR-5),
surfacing pre-event what the security roles UI conceals. All Not Configured sensitive fields
forwarded to TABLE_5 as MISSING-FLS gaps.

**TABLE_2 [CLOSES: POST-INCIDENT-FLS-GAP] -- FLS Coverage**
*(GCR-5 for FLS Profile Configured?, GCR-6 for Gap?)*

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|
| [No sensitive fields identified] | N/A | N/A | Not Configured | N/A | N/A | YES |

Writing "No column security profiles active on {{topic}}. Sensitive fields exposed to any role with entity access." instead of the null-case row fails C-11.
Writing "No FLS configured. See note above." instead of this row also fails C-11.
(Both forms are in PROHIBITED PROSE FORMS above.)

Defense-in-depth check: for at least one sensitive field, name the enforcement layer. For Admin-tier roles, note SE-0 bypass finding.

### SE-3 / SHALL-C -- Record Access Scope

MANUAL GAP [Blind spot 2 -- Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access produced by role + team + OWD;
spot-checking individual roles misses cross-role privilege accumulation through team inheritance.

STRUCTURED CLOSE:
TABLE_3 maps the effective scope for every role by Tier (GCR-1), making team-accumulated privilege
visible and auditable at the tier it occurs.

**TABLE_3 [CLOSES: CUMULATIVE-PRIVILEGE] -- Record Scope by Role**
*(GCR-1 for Tier, GCR-4 for Verified?)*

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|
| [Role] | [Tier] | [OWD] | No scope modifier found | [OWD Baseline] | NO |

Every TABLE_1 role MUST appear, ordered by Tier per GCR-1.
Writing "Scope varies by team membership -- consult admin." instead of a data row fails C-11.
For every role where Effective Scope > role-only scope due to team membership:
"[Role] acquires [scope] through [team/rule name]. Base role scope was [base scope]."
After TABLE_3: update CS-3 SE Confirmation.

### SE-4 / SHALL-D -- Privilege Escalation Cross-Reference

MANUAL GAP [Blind spot 3 -- OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing the sharing rules
that silently override them; a Private OWD combined with an active sharing rule can grant
effective org-wide access without appearing in any security roles UI view.

STRUCTURED CLOSE:
TABLE_4 (filled at SE-0) evaluated all four escalation vectors with sharing rules explicitly
cross-referenced against OWD settings. This section adds cross-tier differential summary citing
SE-0 data: for the most-privileged Admin-tier and most-restricted Restricted-tier role, identify
the specific enforcement layer where access diverges, citing the SE-0 TABLE_4 row ID.

### SE-5 / SHALL-E -- Security Gap Inventory

**ESCALATION RISK SCALE** *(GCR-7; this block appears before the Closing Summary table)*

As declared in GCR-7:
- HIGH: role combination or sharing rule produces access materially exceeding job function
- MEDIUM: access exceeds job function in limited scope; low blast radius
- LOW: minor excess access; unlikely to be exploited
- NONE: access appropriate to job function; no escalation vector confirmed

Auto-fail condition: any blank Escalation Risk cell in the Closing Summary auto-fails GCR-7 verification.
"See above" or "See TABLE_5" is blank-equivalent and auto-fails.
Post-table verification: list any blank or non-declared Escalation Risk cell as NON-COMPLIANT.

**TABLE_5 [CLOSES: ALL-GAPS] -- Security Gap Inventory**
*(GCR-1 for Tier, GCR-2 for Severity)*

| # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation |
|---|----------|--------|---------------|------|------|----------|-------------|
| CLEARED | -- | No gaps found | -- | -- | -- | -- | Evidence: [per-gap-type confirmation] |

Writing "Restrict access to [field]." without exact object + exact Dataverse location + post-fix state fails C-07.
CS-EXPECTATION-VIOLATED rows: CS-Expected / SE-Actual / Delta all required per SHALL-F.

**Closing Summary** *(Escalation Risk per GCR-7; all cells required)*:

| Role | FLS Status | Record Scope | Escalation Risk |
|------|-----------|-------------|----------------|

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Verification + GCR Check + Full Aspirational Audit

### CA-1.1 through CA-1.8 (Double-Anchor Verification)

Each row: Registry anchor (Schema ID + declared columns) -- Preamble anchor (criterion/section/SHALL/row-ID) -- Verification (specific checks) -> PASS / FAIL.

**CA-1.1:** Registry anchor TABLE_1 (GCR-1 Tier, Granted/Denied/Conditional/N/A). Preamble C-01/SE-1/SHALL-A. Verification: TABLE_1 present? Tier per GCR-1? Rows ordered? All cells filled? -> PASS / FAIL

**CA-1.2:** Registry anchor TABLE_2 (GCR-5, GCR-6, null-case row as FIRST DATA ROW). Preamble C-02/SE-2/SHALL-B. Verification: All sensitive fields? FLS per GCR-5? Gap? per GCR-6? Null case a data row (not prose)? -> PASS / FAIL

**CA-1.3:** Registry anchor TABLE_3 (GCR-1, GCR-4). Preamble C-03/SE-3/SHALL-C. Verification: Every TABLE_1 role present? Tier per GCR-1? Effective Scope filled? Verified? per GCR-4? -> PASS / FAIL

**CA-1.4:** Registry anchor TABLE_4 (GCR-3 all YES, GCR-2 Severity). Preamble C-04/SE-0/SHALL-D. Verification: TABLE_4 before SE-1? All four vectors? Checked?=YES per GCR-3? Findings or specific rule-outs? -> PASS / FAIL

**CA-1.5:** Registry anchor TABLE_5 (GCR-1, GCR-2, CLEARED row). Preamble C-05/SE-5/SHALL-E. Verification: Named gap or CLEARED evidence? Tier per GCR-1? Severity per GCR-2? Remediations exact? -> PASS / FAIL

**CA-1.6:** CS-EXPECTATION-VIOLATED rows: CS-Expected / SE-Actual / Delta all populated? -> PASS / FAIL per row.

**CA-1.7:** SE-2 opens with `MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:`? SE-3 with `MANUAL GAP [Blind spot 2 -- Cumulative privilege blind spot]:`? SE-4 with `MANUAL GAP [Blind spot 3 -- OWD-sharing-rule override gap]:`? Each followed by `STRUCTURED CLOSE:`? -> PASS / FAIL per section.

**CA-1.8:** CS-2 in Schema Registry with SE-updatable column declarations? CS-3 same? CS-0 present before CS-1? CS-0 cites both schema IDs by exact label? SE populated SE-updatable columns? -> PASS / FAIL

### CA-1.9 -- Graded Column Registry Compliance

Cite GCR block declared in Phase 0. For each registry entry:
- GCR-1 (Tier): all TABLE_1/TABLE_3 Tier cells in {Admin, Custom, Restricted}? -> PASS / FAIL
- GCR-2 (Severity): all TABLE_4/TABLE_5 Severity cells in {CRITICAL, HIGH, MEDIUM}? -> PASS / FAIL
- GCR-3 (Checked?): all TABLE_4 Checked? = YES? -> PASS / FAIL
- GCR-4 (Verified?): all TABLE_3 Verified? in {YES, NO}? NO rows flagged? -> PASS / FAIL
- GCR-5 (FLS Profile Configured?): all TABLE_2 cells in {Configured, Not Configured}? -> PASS / FAIL
- GCR-6 (Gap?): all TABLE_2 Gap? in {YES, NO}? Every YES has TABLE_5 entry? -> PASS / FAIL
- GCR-7 (Escalation Risk): all Closing Summary cells in {HIGH, MEDIUM, LOW, NONE}? -> PASS / FAIL

### ASPIRATIONAL CRITERIA SELF-VERIFICATION TABLE

Inspect your output against each row below. State PASS or FAIL with specific output evidence.
Submit only when all rows are completed. This table satisfies C-15 when populated.

| ID | Criterion | PASS Condition (with output evidence) | FAIL Signal | Self-Assessment |
|----|-----------|--------------------------------------|------------|-----------------|
| C-08 | Cross-Entity Cascade | A cross-entity cascade was traced: parent entity named, child entity named, mechanism (sharing rule / relationship / OWD interaction) cited | No cross-entity mechanism appears anywhere in output | PASS / FAIL: [cite the cascade path traced or state absent] |
| C-09 | Structured Summary Table | Closing Summary present with columns role, FLS status, record scope, Escalation Risk; all rows populated | Closing Summary absent or has blank cells | PASS / FAIL: [confirm table present and all cells populated] |
| C-10 | Blind-Spot-Labeled Tables | Every table header and major section header carries `[CLOSES: <label>]` using verbatim CONTEXT label. List any unlabeled headers | Any table/section header missing closes annotation | PASS / FAIL: [list unlabeled headers or COMPLIANT] |
| C-11 | Data-Row Null-Case Mandate | Every table uses its registered null-case data row when no findings exist. No prose from PROHIBITED PROSE FORMS appears | Any prohibited prose form appears in place of a null-case data row | PASS / FAIL: [list any prose violations or COMPLIANT] |
| C-12 | Escalation Risk Column | Every Closing Summary Escalation Risk cell is HIGH / MEDIUM / LOW / NONE per GCR-7. No blank cells | Any blank or non-GCR-7 value in Escalation Risk | PASS / FAIL: [list any blank cells or COMPLIANT] |
| C-13 | Pre-Declared Scale with Auto-Fail | GCR block present before any table with all seven columns: each has (a) named scale levels, (b) explicit auto-fail condition, (c) post-table verification instruction. CA-1.9 verifies | GCR absent, any entry missing auto-fail, any entry missing post-table verification | PASS / FAIL: [confirm GCR present and CA-1.9 completed] |
| C-14 | Prose-Substitution Failure Mode Named by Example | PROHIBITED PROSE FORMS block present with at least one entry naming wrong form verbatim and citing criterion violated. Multiple entries present | Only generic warning ("avoid prose") without specific verbatim example and criterion citation | PASS / FAIL: [cite one example from PROHIBITED PROSE FORMS block] |
| C-15 | Self-Verification Checklist | This table is present after main output body with >= 3 aspirational criteria (C-08..C-15) named by ID with explicit pass/fail self-assessment | Generic completeness signal without per-criterion ID assessment | PASS: this table satisfies C-15 when populated with self-assessments |

**CA Format Compliance Verdict -- Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0), GCR (pre-table block), PROHIBITED PROSE FORMS (pre-table block).
[C-01 through C-05 with CA-1.1 through CA-1.5. SHALL-F (CA-1.6). SHALL-G exact-label blocks (CA-1.7). CS-0 acknowledgment (CA-1.8). GCR compliance (CA-1.9). Aspirational self-verification table. Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]
