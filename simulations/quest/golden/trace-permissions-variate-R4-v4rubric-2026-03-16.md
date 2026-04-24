# trace-permissions Variate — Round 4 (Rubric v4, C-16/C-17/C-18)

**Date:** 2026-03-16
**Rubric:** v4 (C-01 through C-18)
**New criteria targeted this round:** C-16 (GCR Exhaustive Column Registration), C-17 (Full-Coverage Aspirational Audit Table, 11 rows), C-18 (Prohibited Prose Catalog — One Entry per Table Site)
**Base:** R3 V-05 mechanics retained across all variations (GCR-1..GCR-7 declared, 6-entry PPF catalog, 8-item aspirational table). R4 variations add structural mechanisms targeting the three new v4 aspirational criteria without removing any existing mechanism.

---

## Round 4 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | C-16 single axis — GCR-N citations required in every graded column header | The R3 V-05 GCR block declares GCR-1..GCR-7 but table column headers still use bare names (e.g., `Tier`, `Severity`). Adding `[GCR-N]` to every graded column header makes the GCR-to-table link structurally verifiable: CA-1.9 can confirm every graded column cites its GCR entry without reading the GCR block, because the citation is co-located at point of use |
| V-02 | C-18 single axis — Prohibited prose catalog explicitly indexed one entry per table site | R3 V-05 has a PPF section but entries are not keyed to table sites by identity. Introducing PPF-1..PPF-6 with explicit table-site labels (one per named schema: TABLE_1..TABLE_5 + Escalation Risk) makes per-site coverage a countable structural property, not an emergent one: CA-1.10 can verify 6 entries exist and each names a table site |
| V-03 | C-17 single axis — Aspirational audit table expanded to 11 rows covering C-08..C-18 | R3 V-05 aspirational table has 8 rows covering C-08..C-15. With N=11 in v4, a row missing for C-16, C-17, or C-18 means the model cannot self-verify the new criteria before submission; adding 3 rows closes that blind spot and makes the self-audit complete |
| V-04 | Combined: C-16 + C-18 — GCR-N header citations + indexed PPF catalog per table site | Pairing GCR-N header citations with per-site PPF entries creates dual structural reinforcement: every graded column declares its contract in the header (C-16), and every table site names its prohibited prose failure mode (C-18); together they close both the blank-cell detection gap and the prose-substitution detection gap at the point of use |
| V-05 | Full integration: C-16 + C-17 + C-18 — all three v4 mechanisms | GCR-N headers + 11-row aspirational audit table + indexed PPF catalog: the model can pre-verify every blank-cell contract at the column header, confirm every aspirational criterion is addressed including C-16/C-17/C-18 themselves, and identify the wrong prose form at every table site before producing any output |

---

## V-01 — Single Axis: C-16 (GCR-N Column Header Citations)

**Axis:** C-16 single axis
**Hypothesis:** GCR-1..GCR-7 declared as numbered entries is a necessary condition for C-16 but not sufficient. The sufficient condition is that every graded column header in every table includes its `[GCR-N]` citation so the contract is readable at point of use without cross-referencing the GCR block. CA-1.9 can then perform a mechanical header-citation check against the GCR, catching any table where a graded column was populated without the declared scale being visible in context.

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

**Blind spot 1 — Post-incident FLS gap.** Column security profiles are rarely audited proactively.
Sensitive fields — credit limits, compensation data, SSNs, contact identifiers — remain readable
and writable by any role unless a column security profile explicitly restricts them. The security
roles UI does not surface which fields lack column security profiles; gaps are discovered after
data exposure, not before.

**Blind spot 2 — Cumulative privilege blind spot.** A user holding a BU-scoped security role who
also belongs to an owner team whose team role grants org-wide access has effective org-wide access.
No single Dataverse UI view surfaces the combined effective access produced by role + team + OWD
combination. Spot-checking individual roles misses cross-role accumulation through team membership.

**Blind spot 3 — OWD-sharing-rule override gap.** Administrators check OWD settings
entity-by-entity without evaluating the sharing rules that silently override those baselines. A
Private OWD on Case combined with a Power Automate-triggered sharing rule grants effective
org-wide read to users who satisfy the trigger condition — including low-trust service accounts
and CS users not intended to have broad case access.

This trace closes all three blind spots: SE-2 closes Blind spot 1; SE-3 closes Blind spot 2;
SE-4 closes Blind spot 3. Closure notes are exact-label two-part blocks co-located at each SE
sub-section opening, carrying the exact blind-spot label from this CONTEXT section.

---

## GRADED COLUMN REGISTRY (CA-authored, Phase 0 precondition)

All graded columns used in this trace are declared here before any table is populated. Each entry
specifies: (a) scale with every level named, (b) auto-fail condition for blank cells, (c) post-table
verification instruction. A table that uses a column not registered here is structurally incomplete.
A cell that does not match the declared values auto-fails.

**Header citation rule (C-16):** Every graded column header in every table MUST include its GCR-N
identifier in brackets — e.g., `Tier [GCR-1]`, `Severity [GCR-2]`. A table header that omits
the `[GCR-N]` suffix on a graded column auto-fails CA-1.9 verification. The citation is required
at the column header level, not only in this Registry block.

**GCR-1 — Tier** (used in TABLE_1, TABLE_3, TABLE_5)
Scale: `Admin` / `Custom` / `Restricted`
Auto-fail: any cell not one of these three values is a blank-equivalent and auto-fails TABLE verification.
Post-table verification: after each table with a Tier column, confirm every row has one of the three declared values.

**GCR-2 — Severity** (used in TABLE_4, TABLE_5)
Scale: `CRITICAL` (exploitable with no additional steps) / `HIGH` (exploitable with one intermediate step) / `MEDIUM` (limited blast radius or requires specific conditions)
Auto-fail: any Severity cell that is blank or uses a value outside CRITICAL / HIGH / MEDIUM auto-fails TABLE verification.
Post-table verification: after TABLE_5, list any row with a blank or non-declared Severity as NON-COMPLIANT.

**GCR-3 — Checked?** (used in TABLE_4)
Scale: `YES` (vector examined, finding or specific rule-out written) / `NO` (not checked — auto-fail)
Auto-fail: any Checked? = NO or blank auto-fails TABLE_4 verification. All four vectors must be YES.
Post-table verification: after TABLE_4, confirm all four rows have Checked? = YES.

**GCR-4 — Verified?** (used in TABLE_3)
Scale: `YES` (scope confirmed against configuration) / `NO` (scope inferred, not confirmed — flag as gap)
Auto-fail: a blank Verified? cell is treated as NO and auto-fails the row.
Post-table verification: after TABLE_3, list any NO rows as unconfirmed scope entries requiring follow-up.

**GCR-5 — FLS Profile Configured?** (used in TABLE_2)
Scale: `Configured` (a column security profile exists and restricts this field) / `Not Configured` (no column security profile; field accessible to any role with entity access)
Auto-fail: blank or any value other than `Configured` / `Not Configured` auto-fails TABLE_2 verification.
Post-table verification: after TABLE_2, confirm every row has one of the two declared values.

**GCR-6 — Gap?** (used in TABLE_2)
Scale: `YES` (field has missing or insufficient protection — forward to TABLE_5) / `NO` (field adequately protected)
Auto-fail: blank Gap? cell auto-fails the row. Every Gap? = YES row must have a corresponding TABLE_5 entry.
Post-table verification: after TABLE_2, verify every YES row has a TABLE_5 cross-reference.

**GCR-7 — Escalation Risk** (used in Closing Summary)
Scale: `HIGH` (role combination or sharing rule produces access materially exceeding job function) / `MEDIUM` (access exceeds job function in limited scope; low blast radius) / `LOW` (minor excess access; unlikely to be exploited) / `NONE` (access appropriate to job function; no escalation vector confirmed)
Auto-fail: blank Escalation Risk cell auto-fails Closing Summary verification. Inline text "varies" or "see above" is blank-equivalent.
Post-table verification: after Closing Summary, list any row with a blank or non-declared Escalation Risk as NON-COMPLIANT.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins.

**PHASE 0 — CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1: TABLE_1 through TABLE_5 with Tier
columns on TABLE_1 and TABLE_3; CS-2 and CS-3 with SE-updatable columns and SE-update protocols
— seven schemas total) and the Criterion Enforcement Matrix preamble (Step 0.2: SHALL-A through
SHALL-G, M4 row IDs CA-1.1 through CA-1.9 pre-assigned). CA issues handoff to PHASE 1.

**PHASE 1 — CS (Customer Success):**
Executes second. Opens with CS-0 sub-section (Schema Registry acknowledgment: CS echoes Registry
schema IDs for CS-2 and CS-3 by exact Schema ID label, lists SE-updatable columns for each, and
confirms the expectation format before authoring any expectation rows). Then produces CS-1, CS-2,
CS-3 using Registry schemas. CS does not fill TABLE_1-5. CS issues handoff to PHASE 2.

**PHASE 2 — SE (Security Engineer / Dataverse Security Expert):**
Executes third in privilege-tier descent order. SE-0 (admin-tier inventory and TABLE_4 escalation
vectors) runs before SE-1 (role-operation matrix), establishing the privilege ceiling before
populating operation cells. TABLE_1 and TABLE_3 include Tier [GCR-1] column. SE-2, SE-3, SE-4
each open with two-part exact-label closure blocks per SHALL-G. SE-4 cites SE-0 data in cross-tier
differential. Issues handoff to PHASE 3.

**PHASE 3 — CA-1 (CA Verification Pass):**
CA returns. Each CA-1 row performs double-anchor reaffirmation: Registry anchor and Preamble
anchor as structurally distinct labeled elements. Verification line follows. Inline concatenation
fails. CA-1.8 extended to verify CS-0 acknowledgment precedes CS-1. CA-1.9 verifies GCR-N
header citations in every table.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1 and 0.2 before any other phase begins.*

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

**All table schemas declared centrally by CA. Blank-cell prohibition is global. SE-update
protocols for CS-2 and CS-3 declared co-located with schema entry. Every graded column header
includes its GCR-N citation per header citation rule above.**

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Tier [GCR-1] | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Tier [GCR-1] values: Admin / Custom / Restricted. Rows ordered: Admin tier first, Custom second,
Restricted last. Blank-cell rule: all cells Granted / Denied / Conditional (condition inline) / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? [GCR-5] | Roles: Read | Roles: Write | Gap? [GCR-6]`
Blank-cell rule: FLS Profile Configured? [GCR-5] = Configured / Not Configured (never blank). Gap? [GCR-6] = YES / NO.

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | Tier [GCR-1] | OWD Baseline | Scope Modifier | Effective Scope | Verified? [GCR-4]`
Tier [GCR-1] values mirror TABLE_1. Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU /
Org-wide / Team-scoped / Sharing-[rule name]. Verified? [GCR-4] = YES / NO.

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? [GCR-3] | Finding | Severity [GCR-2]`
Blank-cell rule: all four vectors, Checked? [GCR-3] = YES, Finding = escalation path or specific rule-out.
Note: TABLE_4 executes at SE-0 before SE-1.

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Tier [GCR-1] | Severity [GCR-2] | Remediation`
Blank-cell rule: Remediation = exact object + exact location + expected post-fix state.
CS-EXPECTATION-VIOLATED Remediation (three-field block):
- CS-Expected: cite CS-2 or CS-3 row, state expectation verbatim or by row reference.
- SE-Actual: SE finding that contradicts the expectation.
- Delta: exact configuration change to align SE-Actual to CS-Expected.

**Schema ID: CS-2 — Sharing Rule Expectations (CS-authored expectation table)**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference (TABLE_4 row ID or TABLE_5 row ID);
SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE update protocol: SE populates SE Cross-Reference and SE Confirmation after TABLE_4 analysis at
SE-0. CONTRADICTED triggers CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

**Schema ID: CS-3 — Cross-Role Access Differential Expectations (CS-authored expectation table)**
Declared columns: `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference (TABLE_1 row ID or TABLE_3 row ID);
SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE update protocol: SE populates after TABLE_1/TABLE_3 analysis. CONTRADICTED triggers
CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: M1, M2, M3 simultaneously active. M4 pre-assigned.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-0 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A: Complete TABLE_1 with Tier [GCR-1] column. Every cell Granted/Denied/Conditional/N/A. Rows ordered by tier.
- SHALL-B: TABLE_2 lists all PII, Financial, and Audit-Compliance fields with explicit FLS status. Null case explicit. Gap? [GCR-6] YES rows in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier [GCR-1] and Effective Scope filled. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 at SE-0 (before SE-1), all four vectors, Checked? [GCR-3] = YES. Rule-outs name specific mechanism and reason.
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap case requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field Remediation block (CS-Expected, SE-Actual, Delta). Incomplete rows MUST be reopened. CA-1.6 verifies.
- SHALL-G: At the opening of SE-2, SE-3, and SE-4, closure MUST appear as a two-part labeled block — Line 1: `MANUAL GAP [<exact CONTEXT label>]:` where <exact CONTEXT label> is the label character-for-character as written in the CONTEXT section; Line 2: description of what manual audits miss; Line 3: `STRUCTURED CLOSE:`; Line 4: which table and mechanism closes it. Single-line annotation, blockquote format, TABLE_5 consolidation, or paraphrased label all fail SHALL-G. CA-1.7 verifies exact label carry-through.

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

*CS opens with CS-0 Registry acknowledgment before authoring any expectation content.*

### CS-0 — Schema Registry Acknowledgment (CS-authored, Phase 1)

**Registry acknowledgment for CS-2:**
Schema ID: CS-2 — Sharing Rule Expectations.
SE-updatable columns as declared by CA in Phase 0 Schema Registry: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged: SE populates SE Cross-Reference (TABLE_4 row or TABLE_5 row ID)
and SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE) after SE-0/TABLE_4 analysis.
Expectation format confirmed: CS-2 rows use columns Rule Name | Trigger | Expected Access Granted |
Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation.
SE-updatable columns left blank; SE fills after SE-0.

**Registry acknowledgment for CS-3:**
Schema ID: CS-3 — Cross-Role Access Differential Expectations.
SE-updatable columns as declared by CA in Phase 0 Schema Registry: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged: SE populates SE Cross-Reference (TABLE_1 or TABLE_3 row ID)
and SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE) after SE-1/SE-3 analysis.
Expectation format confirmed: CS-3 rows use columns Entity | Operation | CS Role Expected Access |
Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference |
SE Confirmation. SE-updatable columns left blank; SE fills after SE-1/SE-3.

### CS-1 — Expected Customer Service Access Baseline

For each entity in scope: (a) which CRUD operations the CS role is expected to perform as part of
normal job function; (b) the expected record scope; (c) which sensitive fields CS needs read or
write access to and why. Identify any configuration that may inadvertently open access beyond job
requirements.

**CS-2 — Sharing rule expectations** *(Schema Registry CS-2; SE-updatable columns blank; SE
fills after SE-0/TABLE_4)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

For each Potential Overreach? YES: name the access path and the most likely over-reached role.

**CS-3 — Cross-role access differential** *(Schema Registry CS-3; SE-updatable columns blank;
SE fills after SE-1/SE-3)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

State at minimum one entity and one operation where CS has less access than the Comparison Role.

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis (Privilege-Tier Descent Order)

*SE traces from highest-privilege tier to lowest. SE-0 establishes admin-tier ceiling and
TABLE_4 before SE-1. TABLE_1 and TABLE_3 include Tier [GCR-1] column. SE-2/SE-3/SE-4 use
exact-label two-part closure blocks per SHALL-G.*

### SE-0 — Admin-Tier Inventory and Escalation Vectors (executes before TABLE_1)

**Admin-tier role inventory:** List System Administrator, Environment Admin, and any
admin-equivalent roles with record scope and key capabilities. Note any admin capability that
bypasses lower-tier controls (e.g., System Administrator bypasses column security profiles).
This establishes the privilege ceiling for all lower-tier roles in SE-1.

**TABLE_4 — Escalation Vector Inventory** *(Schema Registry TABLE_4; placed at SE-0 because
admin-tier role structure determines escalation paths; TABLE_1 rows are interpreted relative to
this ceiling)*

| Vector | Checked? [GCR-3] | Finding | Severity [GCR-2] |
|--------|------------------|---------|------------------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Finding format: `[Role] -> [Mechanism] -> [Elevated access achieved]` for confirmed escalation;
"Checked [mechanism]: no path found because [specific reason]" for rule-out. After TABLE_4:
populate CS-2 SE Cross-Reference and SE Confirmation. CONTRADICTED rows trigger
CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

### SE-1 / SHALL-A — Section 1: Role-Operation Matrix

**TABLE_1 — Role-Operation Matrix** *(Schema Registry TABLE_1 with Tier [GCR-1] column; blank-cell rule)*

| Role | Tier [GCR-1] | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|--------------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Rows ordered: Admin tier first, Custom tier second, Restricted tier last. After TABLE_1: populate
CS-3 SE Cross-Reference and SE Confirmation.

**Cross-role differential analysis:** Compare the CS role against at least one Admin-tier role
and one Custom-tier role for the same entity and operation. Cite SE-0 TABLE_4 data for any
differential attributable to admin-tier escalation vectors.

### SE-2 / SHALL-B — Section 2: Field-Level Security Coverage

MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:
Column security profiles are not auditable from the security roles UI; administrators discover
missing FLS only after a data exposure event reveals that a sensitive field was readable or
writable by an unintended role.

STRUCTURED CLOSE:
TABLE_2 below enumerates every sensitive field in scope with its explicit FLS status (Configured /
Not Configured), surfacing pre-event what the security roles UI conceals. All Not Configured
sensitive fields are forwarded to TABLE_5 as MISSING-FLS gaps with Tier [GCR-1] column identifying
the highest-privilege tier with access.

**TABLE_2 — FLS Coverage** *(Schema Registry TABLE_2; blank-cell rule globally)*

| Entity | Field | Category | FLS Profile Configured? [GCR-5] | Roles: Read | Roles: Write | Gap? [GCR-6] |
|--------|-------|----------|---------------------------------|-------------|--------------|--------------|

Categories: PII / Financial / Audit-Compliance / Other-Sensitive. Null case: "No column security
profiles active on {{topic}}. Sensitive fields identified: [list]. All in TABLE_5 as MISSING-FLS."
Note: System Administrator bypasses column security profiles (SE-0 confirmed); document in
defense-in-depth layer check.

**Defense-in-depth layer check:** Identify the enforcement layer for at least one sensitive field.
For Admin-tier roles, note the SE-0 bypass finding.

### SE-3 / SHALL-C — Section 3: Record Access Scope

MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access produced by a security role
plus owner team membership plus OWD; spot-checking roles individually misses cross-role privilege
accumulation through team inheritance.

STRUCTURED CLOSE:
TABLE_3 below maps the effective scope for every role by Tier [GCR-1], recording the OWD
baseline, the scope modifier from team or role depth, and the resulting effective scope as a
single traceable row, making team-accumulated privilege visible and auditable at the tier it occurs.

**TABLE_3 — Record Scope by Role** *(Schema Registry TABLE_3 with Tier [GCR-1] column; blank-cell rule)*

| Role | Tier [GCR-1] | OWD Baseline | Scope Modifier | Effective Scope | Verified? [GCR-4] |
|------|--------------|--------------|----------------|-----------------|-------------------|

Every TABLE_1 role MUST appear, ordered by Tier [GCR-1]. Note roles where effective scope exceeds
role-only scope due to team membership; flag CS-EXPECTATION-VIOLATED in TABLE_5 if CS-3 expected
the unexpanded scope. After TABLE_3: update CS-3 SE Confirmation.

### SE-4 / SHALL-D — Section 4: Privilege Escalation Cross-Reference

MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing the sharing rules
that silently override them; a Private OWD combined with an active sharing rule can grant
effective org-wide access without appearing in any security roles UI view.

STRUCTURED CLOSE:
TABLE_4 (filled at SE-0) evaluated all four escalation vectors with sharing rules explicitly
cross-referenced against OWD settings. This section adds cross-tier differential summary citing
SE-0 data: for the most privileged Admin-tier role and the most restricted Restricted-tier role,
identify the specific enforcement layer where access diverges, citing the SE-0 TABLE_4 row ID
that established the admin-tier ceiling.

### SE-5 / SHALL-E — Section 5: Security Gap Inventory

**TABLE_5 — Security Gap Inventory** *(Schema Registry TABLE_5 with Tier [GCR-1] and Severity [GCR-2] columns; blank-cell rule)*

| # | Gap Type | Entity | Field or Rule | Role | Tier [GCR-1] | Severity [GCR-2] | Remediation |
|---|----------|--------|---------------|------|--------------|------------------|-------------|

Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED /
CS-EXPECTATION-VIOLATED. Severity [GCR-2]: CRITICAL / HIGH / MEDIUM.

CS-EXPECTATION-VIOLATED rows (three-field Remediation block per SHALL-F):
- CS-Expected: [cite CS-2 or CS-3 row, state expectation verbatim or by row reference]
- SE-Actual: [SE finding that contradicts the expectation]
- Delta: [exact configuration change to align SE-Actual to CS-Expected]

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

*CA returns. Each CA-1 row MUST present Registry anchor and Preamble anchor as structurally
distinct labeled elements before the Verification line. Inline concatenation fails.*

**CA-1.1 — C-01 verification:**
- Registry anchor — Schema ID TABLE_1 (with Tier [GCR-1]): declared columns with blank-cell rule.
- Preamble anchor — C-01: TABLE_1 / SE-1 / SHALL-A / CA-1.1.
- Verification — TABLE_1 present? Tier [GCR-1] column populated? Rows ordered by tier? All cells filled? -> PASS / FAIL

**CA-1.2 — C-02 verification:**
- Registry anchor — Schema ID TABLE_2: FLS Profile Configured? [GCR-5] and Gap? [GCR-6] columns declared.
- Preamble anchor — C-02: TABLE_2 / SE-2 / SHALL-B / CA-1.2.
- Verification — TABLE_2 present? All sensitive fields? FLS status explicit? Null case stated? Gap? [GCR-6] YES in TABLE_5? -> PASS / FAIL

**CA-1.3 — C-03 verification:**
- Registry anchor — Schema ID TABLE_3 (with Tier [GCR-1], Verified? [GCR-4]): declared columns with blank-cell rule.
- Preamble anchor — C-03: TABLE_3 / SE-0+SE-3 / SHALL-C / CA-1.3.
- Verification — Every TABLE_1 role in TABLE_3? Tier [GCR-1] populated? Effective Scope filled? Verified? [GCR-4] filled? -> PASS / FAIL

**CA-1.4 — C-04 verification:**
- Registry anchor — Schema ID TABLE_4: Checked? [GCR-3] and Severity [GCR-2] columns; all four vectors, Checked? = YES.
- Preamble anchor — C-04: TABLE_4 / SE-0 / SHALL-D / CA-1.4.
- Verification — TABLE_4 at SE-0 (before SE-1)? All four vectors? Checked? [GCR-3] = YES? Findings or specific rule-outs? -> PASS / FAIL

**CA-1.5 — C-05 verification:**
- Registry anchor — Schema ID TABLE_5 (with Tier [GCR-1], Severity [GCR-2]): declared columns with blank-cell rule.
- Preamble anchor — C-05: TABLE_5 / SE-5 / SHALL-E / CA-1.5.
- Verification — TABLE_5 present? Named gap? Tier [GCR-1] populated? Severity [GCR-2] populated? Remediations exact? -> PASS / FAIL

**CA-1.6 — SHALL-F compliance verification:**
- Registry anchor — Schema ID TABLE_5 CS-EXPECTATION-VIOLATED row: three-field Remediation block required per SHALL-F.
- Preamble anchor — SHALL-F: three-field block mandatory; rows missing any field MUST be reopened.
- Verification — For each CS-EXPECTATION-VIOLATED row: CS-Expected populated? SE-Actual populated? Delta populated with exact configuration change? -> PASS / FAIL per row.

**CA-1.7 — SHALL-G compliance verification (exact-label two-part closure blocks):**
- Registry anchor — CONTEXT declared exact labels: "Blind spot 1 — Post-incident FLS gap" (SE-2 target), "Blind spot 2 — Cumulative privilege blind spot" (SE-3 target), "Blind spot 3 — OWD-sharing-rule override gap" (SE-4 target).
- Preamble anchor — SHALL-G: Line 1 MUST be `MANUAL GAP [<exact CONTEXT label>]:`; exact = character-for-character; paraphrase fails.
- Verification — SE-2 opens with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:`? SE-3 opens with `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:`? SE-4 opens with `MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:`? Each followed by `STRUCTURED CLOSE:`? -> PASS / FAIL per section.

**CA-1.8 — CS-2/CS-3 Schema Registry registration + CS-0 acknowledgment verification:**
- Registry anchor — Schema Registry declared CS-2 and CS-3 as named schema entries with SE-updatable columns and SE-update protocol co-located.
- Preamble anchor — CS-0 acknowledgment is a PHASE 1 structural requirement.
- Verification — CS-2 in Schema Registry? CS-3 same? CS-0 present before CS-1? CS-0 cites both schema IDs by exact label? CS-0 lists SE-updatable columns? SE populated SE-updatable columns per protocol? -> PASS / FAIL

**CA-1.9 — C-16 verification (GCR-N column header citations):**
- Registry anchor — GCR section declared header citation rule: every graded column header MUST include [GCR-N] suffix. GCR-1 = Tier, GCR-2 = Severity, GCR-3 = Checked?, GCR-4 = Verified?, GCR-5 = FLS Profile Configured?, GCR-6 = Gap?, GCR-7 = Escalation Risk.
- Preamble anchor — Schema Registry Step 0.1 declared all seven schemas with GCR-N citations in column headers. Missing [GCR-N] in any graded column header = auto-fail.
- Verification — TABLE_1 header has `Tier [GCR-1]`? TABLE_2 has `FLS Profile Configured? [GCR-5]` and `Gap? [GCR-6]`? TABLE_3 has `Tier [GCR-1]` and `Verified? [GCR-4]`? TABLE_4 has `Checked? [GCR-3]` and `Severity [GCR-2]`? TABLE_5 has `Tier [GCR-1]` and `Severity [GCR-2]`? Closing Summary has `Escalation Risk [GCR-7]`? -> PASS / FAIL per table.

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0), Phase 0 by label.
[C-01 through C-05 with CA-1.1 through CA-1.5 results. SHALL-F (CA-1.6). SHALL-G (CA-1.7). CS-0 acknowledgment (CA-1.8). C-16 GCR-N header citations (CA-1.9). Overall: COMPLIANT / NON-COMPLIANT.]

---

## ASPIRATIONAL CRITERIA SELF-VERIFICATION (8-item, C-08..C-15)

Complete the Self-Assessment column before finalizing output. FAIL in any row requires revision.

| Criterion | Pass Condition | Fail Signal | Self-Assessment |
|-----------|----------------|-------------|-----------------|
| C-08 | At least one cross-entity cascade traced: permission on Entity A produces derived access on Entity B, mechanism named | No cross-entity effect analyzed | |
| C-09 | Closing Summary table at SE-5 with role + verdict + open gaps + Escalation Risk [GCR-7] per row | No summary table | |
| C-10 | Every table header includes `[CLOSES: <exact blind spot label>]` | Table headers missing CLOSES annotation | |
| C-11 | Every table has a null-case row | Table absent when no items found; null case as prose | |
| C-12 | Escalation Risk [GCR-7] column in Closing Summary; blank = auto-fail | Escalation Risk blank, "varies", or outside declared GCR-7 scale | |
| C-13 | GCR block present before any table; all 7 columns registered; each entry has (a) scale, (b) auto-fail, (c) post-table verification — all three co-located in one block | Only scale declared; (b) or (c) in a separate section | |
| C-14 | At least one prohibited prose form named with verbatim wrong form + criterion violated by ID | No prohibited form named | |
| C-15 | This table present with Pass Condition / Fail Signal / Self-Assessment columns for each criterion | Flat checklist only | |

---

## V-02 — Single Axis: C-18 (Prohibited Prose Catalog Per Table Site)

**Axis:** C-18 single axis
**Hypothesis:** The R3 V-05 PPF section has 6 entries covering all named table sites, but they are not indexed by site identity. Without an explicit PPF-N label tied to the table name, it is possible to produce a 6-entry catalog that skips one site and adds a second entry for another. Making each entry explicitly keyed to a named table/schema (PPF-1 = TABLE_1, PPF-2 = TABLE_2, ..., PPF-6 = Escalation Risk) turns coverage exhaustion into a countable structural property: CA-1.10 can verify exactly 6 entries, each naming a distinct table site.

---

depth: standard
confidence: standard

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

Manual security reviews of Dataverse environments routinely miss three failure scenarios that this
trace is designed to surface:

**Blind spot 1 — Post-incident FLS gap.** Column security profiles are rarely audited proactively.
Sensitive fields — credit limits, compensation data, SSNs, contact identifiers — remain readable
and writable by any role unless a column security profile explicitly restricts them. The security
roles UI does not surface which fields lack column security profiles; gaps are discovered after
data exposure, not before.

**Blind spot 2 — Cumulative privilege blind spot.** A user holding a BU-scoped security role who
also belongs to an owner team whose team role grants org-wide access has effective org-wide access.
No single Dataverse UI view surfaces the combined effective access produced by role + team + OWD
combination. Spot-checking individual roles misses cross-role accumulation through team membership.

**Blind spot 3 — OWD-sharing-rule override gap.** Administrators check OWD settings
entity-by-entity without evaluating the sharing rules that silently override those baselines. A
Private OWD on Case combined with a Power Automate-triggered sharing rule grants effective
org-wide read to users who satisfy the trigger condition — including low-trust service accounts
and CS users not intended to have broad case access.

This trace closes all three blind spots: SE-2 closes Blind spot 1; SE-3 closes Blind spot 2;
SE-4 closes Blind spot 3. Closure notes are exact-label two-part blocks co-located at each SE
sub-section opening.

---

## GRADED COLUMN REGISTRY (CA-authored, Phase 0 precondition)

All graded columns declared before any table. Each entry has: (a) scale with all levels named,
(b) auto-fail condition, (c) post-table verification instruction — all three in one block.

**GCR-1 — Tier** (TABLE_1, TABLE_3, TABLE_5): Scale: Admin / Custom / Restricted. Auto-fail: cell outside these three values. Post-table: confirm every Tier row has one declared value.
**GCR-2 — Severity** (TABLE_4, TABLE_5): Scale: CRITICAL / HIGH / MEDIUM. Auto-fail: blank or outside scale. Post-table: list non-compliant rows.
**GCR-3 — Checked?** (TABLE_4): Scale: YES / NO (NO = auto-fail). Auto-fail: any Checked? != YES. Post-table: confirm all four rows YES.
**GCR-4 — Verified?** (TABLE_3): Scale: YES / NO. Auto-fail: blank treated as NO. Post-table: list NO rows for follow-up.
**GCR-5 — FLS Profile Configured?** (TABLE_2): Scale: Configured / Not Configured. Auto-fail: blank or outside scale. Post-table: confirm every row has one declared value.
**GCR-6 — Gap?** (TABLE_2): Scale: YES / NO. Auto-fail: blank. Post-table: verify every YES has TABLE_5 cross-reference.
**GCR-7 — Escalation Risk** (Closing Summary): Scale: HIGH / MEDIUM / LOW / NONE. Auto-fail: blank or "varies" or "see above". Post-table: list non-compliant rows.

---

## PROHIBITED PROSE FORMS CATALOG (One entry per named table/schema site)

Exactly one entry per named table or schema in this trace. Each entry identifies the wrong form
verbatim and the criterion it violates by ID. Using a prohibited form at the named site is a
structural failure detectable by CA-1.10. Coverage rule: PPF-1 through PPF-6 must all be present.

**PPF-1 — TABLE_1 (Role-Operation Matrix) — null case:**
Prohibited form: "No operations are restricted for this entity." or leaving the TABLE_1 cell blank.
Criterion violated: C-11 — null case must be a data row: `[Role] | [Tier] | N/A | N/A | ... | No operations available in this configuration`, not inline prose.

**PPF-2 — TABLE_2 (FLS Coverage) — null case:**
Prohibited form: Writing "No column security profiles active on {{topic}}." as prose above or below the table instead of as a table row.
Criterion violated: C-11 — null case must appear as an explicit TABLE_2 row with FLS Profile Configured? = Not Configured and a reason column entry identifying why no profile is active.

**PPF-3 — TABLE_3 (Record Scope by Role) — omission form:**
Prohibited form: Omitting a role from TABLE_3 with a note "inherits scope from TABLE_1" or "default OWD applies."
Criterion violated: C-03 — every TABLE_1 role must appear in TABLE_3 with Effective Scope explicitly stated; inheritance is not a valid TABLE_3 entry.

**PPF-4 — TABLE_4 (Escalation Vector Inventory) — rule-out shortcut:**
Prohibited form: Writing "No escalation paths identified." as the Finding cell for any vector.
Criterion violated: C-04 — rule-out format requires naming the specific Dataverse mechanism: "Checked [vector]: no path found because [specific control name] prevents [escalation mechanism]."

**PPF-5 — TABLE_5 (Security Gap Inventory) — zero-gap omission:**
Prohibited form: Leaving TABLE_5 absent or empty, or writing "No security gaps found." above the table.
Criterion violated: C-04 — zero-gap case requires explicit evidence rows: `| 1 | REVIEWED-NO-GAP | [Entity] | [Field or Rule] | [Role] | [Tier] | N/A | Evidence: [specific control] prevents exploitation |`.

**PPF-6 — Escalation Risk column (Closing Summary) — blank/vague:**
Prohibited form: Writing "Varies by entity" or "See TABLE_5 for details" or leaving the Escalation Risk cell blank.
Criterion violated: C-12 — Escalation Risk must be one value from GCR-7 scale (HIGH / MEDIUM / LOW / NONE) with an inline justification in the same cell.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins.

**PHASE 0 — CA:** Authors Schema Registry (Step 0.1) and Criterion Enforcement Matrix (Step 0.2). M4 rows CA-1.1 through CA-1.10 pre-assigned. Issues handoff to PHASE 1.
**PHASE 1 — CS:** CS-0 Registry acknowledgment first, then CS-1, CS-2, CS-3. Issues handoff to PHASE 2.
**PHASE 2 — SE:** SE-0 (admin inventory + TABLE_4) before SE-1. TABLE_1/TABLE_3 include Tier column. SE-2/SE-3/SE-4 use exact-label two-part closure blocks per SHALL-G. Issues handoff to PHASE 3.
**PHASE 3 — CA-1:** Double-anchor reaffirmation for each row. CA-1.10 verifies PPF per-site coverage.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Tier values: Admin / Custom / Restricted. Blank-cell rule: all cells Granted / Denied / Conditional / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Blank-cell rule: FLS Profile Configured? = Configured / Not Configured. Gap? = YES / NO.

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name]. Verified? = YES / NO.

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
Blank-cell rule: all four vectors, Checked? = YES, Finding = escalation path or specific rule-out.

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation`
Blank-cell rule: Remediation = exact object + exact location + expected post-fix state.
CS-EXPECTATION-VIOLATED three-field block: CS-Expected / SE-Actual / Delta.

**Schema ID: CS-2 — Sharing Rule Expectations**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference, SE Confirmation. Protocol: SE fills after TABLE_4 analysis.

**Schema ID: CS-3 — Cross-Role Access Differential Expectations**
Declared columns: `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference, SE Confirmation. Protocol: SE fills after TABLE_1/TABLE_3.

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-0 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

SHALL-A through SHALL-G: [same obligations as V-01]. SHALL-H (new): PPF-1 through PPF-6 must all be present in the PROHIBITED PROSE FORMS CATALOG before any table is populated. CA-1.10 verifies.

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

[Same structure as V-01 PHASE 1: CS-0 acknowledgment for CS-2 and CS-3, then CS-1/CS-2/CS-3.]

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis (Privilege-Tier Descent Order)

[Same structure as V-01 PHASE 2: SE-0 through SE-5 with TABLE_1 through TABLE_5. Column headers use bare names (no GCR-N citations — V-02 does not target C-16). Exact-label SHALL-G closure blocks at SE-2/SE-3/SE-4.]

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

[CA-1.1 through CA-1.8 same as V-01 (without CA-1.9 GCR-N header check).]

**CA-1.10 — C-18 verification (Prohibited Prose Catalog per table site):**
- Registry anchor — PROHIBITED PROSE FORMS CATALOG declared PPF-1..PPF-6, one entry per named table/schema site. Coverage rule: all 6 must be present, each naming a distinct table site.
- Preamble anchor — SHALL-H: PPF-1 through PPF-6 required before any table. CA-1.10 verifies count and site coverage.
- Verification — PPF-1 (TABLE_1) present? PPF-2 (TABLE_2) present? PPF-3 (TABLE_3) present? PPF-4 (TABLE_4) present? PPF-5 (TABLE_5) present? PPF-6 (Escalation Risk) present? Each entry has verbatim wrong form + criterion by ID? -> PASS / FAIL per entry.

**CA Format Compliance Verdict:**
[C-01 through C-05, SHALL-F, SHALL-G, CS-0, PPF per-site coverage (CA-1.10). Overall: COMPLIANT / NON-COMPLIANT.]

---

## ASPIRATIONAL CRITERIA SELF-VERIFICATION (8-item, C-08..C-15)

| Criterion | Pass Condition | Fail Signal | Self-Assessment |
|-----------|----------------|-------------|-----------------|
| C-08 | Cross-entity cascade traced with mechanism named | No cross-entity effect analyzed | |
| C-09 | Closing Summary table at SE-5 | No summary table | |
| C-10 | `[CLOSES: label]` on every table header | Header annotation missing or paraphrased | |
| C-11 | Null-case row in every table | Null case as prose or table absent | |
| C-12 | Escalation Risk column in Closing Summary; blank = auto-fail | Blank, "varies", or outside GCR-7 scale | |
| C-13 | GCR block with all 7 columns, each having (a) scale (b) auto-fail (c) post-table in one co-located block | (b) or (c) in separate section | |
| C-14 | At least one prohibited prose form verbatim + criterion by ID | No wrong form named | |
| C-15 | This table with Pass Condition / Fail Signal / Self-Assessment structure | Flat checklist only | |

---

## V-03 — Single Axis: C-17 (11-Row Full-Coverage Aspirational Audit Table)

**Axis:** C-17 single axis
**Hypothesis:** The R3 V-05 aspirational table has 8 rows covering C-08..C-15. In v4 with N=11, the model cannot self-verify C-16, C-17, or C-18 before submission. Adding 3 rows makes the self-audit complete: C-16 row forces the model to check GCR-N header citations exist, C-17 row forces it to confirm this table has 11 rows, and C-18 row forces it to count PPF entries against table sites. The self-referential nature of C-17 (the row for C-17 must pass C-17's own Pass Condition) is what makes the 11-row coverage structurally load-bearing rather than decorative.

---

depth: standard
confidence: standard

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

Manual security reviews of Dataverse environments routinely miss three failure scenarios that this
trace is designed to surface:

**Blind spot 1 — Post-incident FLS gap.** Column security profiles are rarely audited proactively.
Sensitive fields — credit limits, compensation data, SSNs, contact identifiers — remain readable
and writable by any role unless a column security profile explicitly restricts them. The security
roles UI does not surface which fields lack column security profiles; gaps are discovered after
data exposure, not before.

**Blind spot 2 — Cumulative privilege blind spot.** A user holding a BU-scoped security role who
also belongs to an owner team whose team role grants org-wide access has effective org-wide access.
No single Dataverse UI view surfaces the combined effective access produced by role + team + OWD
combination. Spot-checking individual roles misses cross-role accumulation through team membership.

**Blind spot 3 — OWD-sharing-rule override gap.** Administrators check OWD settings
entity-by-entity without evaluating the sharing rules that silently override those baselines. A
Private OWD on Case combined with a Power Automate-triggered sharing rule grants effective
org-wide read to users who satisfy the trigger condition — including low-trust service accounts
and CS users not intended to have broad case access.

This trace closes all three blind spots: SE-2 closes Blind spot 1; SE-3 closes Blind spot 2;
SE-4 closes Blind spot 3. Closure notes are exact-label two-part blocks co-located at each SE
sub-section opening.

---

## GRADED COLUMN REGISTRY (CA-authored, Phase 0 precondition)

All graded columns declared before any table. Each entry has: (a) scale, (b) auto-fail, (c) post-table verification — all three in one co-located block.

**GCR-1 — Tier** (TABLE_1, TABLE_3, TABLE_5): Scale: Admin / Custom / Restricted. Auto-fail: cell outside these three values. Post-table: confirm every Tier row has one declared value.
**GCR-2 — Severity** (TABLE_4, TABLE_5): Scale: CRITICAL / HIGH / MEDIUM. Auto-fail: blank or outside scale. Post-table: list non-compliant rows.
**GCR-3 — Checked?** (TABLE_4): Scale: YES / NO (NO = auto-fail). Post-table: confirm all four rows YES.
**GCR-4 — Verified?** (TABLE_3): Scale: YES / NO. Auto-fail: blank = NO. Post-table: list NO rows.
**GCR-5 — FLS Profile Configured?** (TABLE_2): Scale: Configured / Not Configured. Auto-fail: blank or outside scale. Post-table: confirm every row.
**GCR-6 — Gap?** (TABLE_2): Scale: YES / NO. Auto-fail: blank. Post-table: verify YES rows have TABLE_5 cross-reference.
**GCR-7 — Escalation Risk** (Closing Summary): Scale: HIGH / MEDIUM / LOW / NONE. Auto-fail: blank or "varies". Post-table: list non-compliant.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Each completes fully before the next begins. Same phase structure as V-01/V-02. PHASE 3 includes CA-1.1..CA-1.8. No CA-1.9 (C-16 not targeted). No CA-1.10 (C-18 at minimum). CA-1.11 is not added; C-17 is verified by the aspirational audit table's own structural presence.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?`

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation`
CS-EXPECTATION-VIOLATED three-field Remediation block: CS-Expected / SE-Actual / Delta.

**Schema ID: CS-2 — Sharing Rule Expectations**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference, SE Confirmation.

**Schema ID: CS-3 — Cross-Role Access Differential Expectations**
Declared columns: `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference, SE Confirmation.

### Step 0.2 — Criterion Enforcement Matrix Preamble

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL | M4: CA Row |
|-----------|-------------------|---------------------|-----------|------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-0+SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

SHALL-A through SHALL-G: same as V-01.

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

[CS-0 acknowledgment for CS-2 and CS-3 before CS-1/CS-2/CS-3. Same structure as V-01.]

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis (Privilege-Tier Descent Order)

[SE-0 through SE-5. TABLE_1 through TABLE_5. Exact-label SHALL-G closure blocks at SE-2/SE-3/SE-4. Same structure as V-01 except column headers use bare names — V-03 does not target C-16.]

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

[CA-1.1 through CA-1.8 same as V-01. No CA-1.9.]

**CA Format Compliance Verdict:** [C-01..C-05, SHALL-F, SHALL-G, CS-0. Overall: COMPLIANT / NON-COMPLIANT.]

---

## ASPIRATIONAL CRITERIA SELF-VERIFICATION (11-item, C-08..C-18)

Complete ALL rows before finalizing output. FAIL in any row requires revision before submission.
This table covers all 11 v4 aspirational criteria. C-17 is self-referential: verify this table
has 11 rows with all three columns populated as the C-17 self-assessment.

| Criterion | Pass Condition | Fail Signal | Self-Assessment |
|-----------|----------------|-------------|-----------------|
| C-08 | At least one cross-entity cascade traced: permission on Entity A produces derived access on Entity B, cascade mechanism named explicitly | No cross-entity effect analyzed; analysis confined to single entity | |
| C-09 | Closing Summary table present at SE-5 with role + verdict + open gap IDs + Escalation Risk per row | Summary absent; findings only in individual SE sub-sections | |
| C-10 | Every table header includes `[CLOSES: <exact blind spot label>]` — label character-for-character from CONTEXT section | Table headers missing CLOSES annotation; label paraphrased or relocated to prose | |
| C-11 | Every table has a null-case row showing what the table looks like when no instances of the phenomenon exist | Table absent when "no items found"; null case stated as prose above or below table | |
| C-12 | Escalation Risk column in Closing Summary using GCR-7 declared scale; blank or "varies" = auto-fail | Escalation Risk cell blank, uses "varies", "see above", or value outside HIGH / MEDIUM / LOW / NONE | |
| C-13 | GCR block present before any table; all 7 graded columns registered (GCR-1..GCR-7); each entry has (a) full scale with all levels named, (b) auto-fail condition, (c) post-table verification instruction — all three elements in one co-located block per entry | Fewer than 7 columns registered; (b) or (c) deferred to a separate section; elements split across blocks | |
| C-14 | At least one prohibited prose form named with verbatim wrong form text + criterion violated by ID | No prohibited prose form identified; only correct form described | |
| C-15 | This table present with three structured columns (Pass Condition / Fail Signal / Self-Assessment) covering aspirational criteria | Flat checklist with criterion IDs only; Pass Condition or Fail Signal absent | |
| C-16 | Every graded column header in every table includes its [GCR-N] citation (e.g., `Tier [GCR-1]`, `Severity [GCR-2]`) — verifiable at header level without cross-referencing GCR block | Any graded column header in any table missing its [GCR-N] suffix | |
| C-17 | This table has exactly 11 rows covering C-08..C-18; each row has Pass Condition, Fail Signal, and Self-Assessment columns populated | Fewer than 11 rows; any criterion from C-08..C-18 missing; any column empty in any row | |
| C-18 | Prohibited prose catalog has one entry per named table/schema site: TABLE_1, TABLE_2, TABLE_3, TABLE_4, TABLE_5, Escalation Risk = minimum 6 entries; each entry maps verbatim wrong form → criterion violated by ID | Fewer than 6 entries; any named table site without a dedicated PPF entry | |

---

## V-04 — Combined: C-16 + C-18 (GCR-N Header Citations + Indexed PPF Catalog)

**Axis:** C-16 + C-18 combined
**Hypothesis:** GCR-N header citations (C-16) and indexed PPF catalog per table site (C-18) defend orthogonal failure modes without structural conflict. C-16 makes blank-cell violations detectable at the column header level; C-18 makes prose-substitution failures detectable at the table site level. Together they close both detection gaps: a model producing this output cannot accidentally omit a GCR-N citation (CA-1.9 catches it) or substitute prose for a table (PPF entry names the wrong form it must not produce). C-17 is included at 8-row minimum — the single-axis variation for 11-row coverage is V-03.

---

depth: standard
confidence: standard

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

Manual security reviews of Dataverse environments routinely miss three failure scenarios that this
trace is designed to surface:

**Blind spot 1 — Post-incident FLS gap.** Column security profiles are rarely audited proactively.
Sensitive fields — credit limits, compensation data, SSNs, contact identifiers — remain readable
and writable by any role unless a column security profile explicitly restricts them. The security
roles UI does not surface which fields lack column security profiles; gaps are discovered after
data exposure, not before.

**Blind spot 2 — Cumulative privilege blind spot.** A user holding a BU-scoped security role who
also belongs to an owner team whose team role grants org-wide access has effective org-wide access.
No single Dataverse UI view surfaces the combined effective access produced by role + team + OWD
combination. Spot-checking individual roles misses cross-role accumulation through team membership.

**Blind spot 3 — OWD-sharing-rule override gap.** Administrators check OWD settings
entity-by-entity without evaluating the sharing rules that silently override those baselines. A
Private OWD on Case combined with a Power Automate-triggered sharing rule grants effective
org-wide read to users who satisfy the trigger condition — including low-trust service accounts
and CS users not intended to have broad case access.

This trace closes all three blind spots: SE-2 closes Blind spot 1; SE-3 closes Blind spot 2;
SE-4 closes Blind spot 3. Closure notes are exact-label two-part blocks co-located at each SE
sub-section opening.

---

## GRADED COLUMN REGISTRY (CA-authored, Phase 0 precondition)

All graded columns declared before any table. Each entry has (a) scale with all levels named,
(b) auto-fail condition, (c) post-table verification instruction — all three in one co-located block.

**Header citation rule (C-16):** Every graded column header in every table MUST include its [GCR-N]
identifier in brackets. Missing [GCR-N] in any graded column header auto-fails CA-1.9.

**GCR-1 — Tier** (TABLE_1, TABLE_3, TABLE_5): Scale: Admin / Custom / Restricted. Auto-fail: outside these three. Post-table: confirm every Tier row.
**GCR-2 — Severity** (TABLE_4, TABLE_5): Scale: CRITICAL / HIGH / MEDIUM. Auto-fail: blank or outside scale. Post-table: list non-compliant.
**GCR-3 — Checked?** (TABLE_4): Scale: YES / NO (NO = auto-fail). Post-table: confirm all four YES.
**GCR-4 — Verified?** (TABLE_3): Scale: YES / NO. Auto-fail: blank = NO. Post-table: list NO rows.
**GCR-5 — FLS Profile Configured?** (TABLE_2): Scale: Configured / Not Configured. Auto-fail: blank or outside. Post-table: confirm every row.
**GCR-6 — Gap?** (TABLE_2): Scale: YES / NO. Auto-fail: blank. Post-table: verify YES rows cross-reference TABLE_5.
**GCR-7 — Escalation Risk** (Closing Summary): Scale: HIGH / MEDIUM / LOW / NONE. Auto-fail: blank or "varies". Post-table: list non-compliant.

---

## PROHIBITED PROSE FORMS CATALOG (One entry per named table/schema site — C-18)

Coverage rule: PPF-1 through PPF-6 must all be present. Each entry: site label + wrong form verbatim + criterion violated by ID.

**PPF-1 — TABLE_1 null case:**
Prohibited form: "No operations are restricted." or blank cell in any operation column.
Criterion violated: C-11 — null case must be an explicit TABLE_1 data row with N/A values, not prose.

**PPF-2 — TABLE_2 null case:**
Prohibited form: "No column security profiles active on {{topic}}." written as prose instead of a table row.
Criterion violated: C-11 — null case must be a TABLE_2 data row with FLS Profile Configured? = Not Configured.

**PPF-3 — TABLE_3 omission:**
Prohibited form: Omitting a role with "inherits scope from TABLE_1" or "uses default OWD."
Criterion violated: C-03 — every TABLE_1 role must appear in TABLE_3 with Effective Scope explicitly stated.

**PPF-4 — TABLE_4 rule-out shortcut:**
Prohibited form: "No escalation paths identified." as the Finding cell for any vector.
Criterion violated: C-04 — rule-out requires: "Checked [vector]: no path found because [specific Dataverse control prevents it]."

**PPF-5 — TABLE_5 zero-gap omission:**
Prohibited form: Leaving TABLE_5 absent or writing "No security gaps found." instead of data rows.
Criterion violated: C-04 — zero-gap case requires REVIEWED-NO-GAP rows with explicit evidence.

**PPF-6 — Escalation Risk column (Closing Summary):**
Prohibited form: "Varies" / "See TABLE_5" / blank in Escalation Risk cell.
Criterion violated: C-12 — must be one GCR-7 value (HIGH / MEDIUM / LOW / NONE) with inline justification.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Same structure as V-01. M4 rows CA-1.1 through CA-1.10 pre-assigned. CA-1.9 verifies GCR-N header citations; CA-1.10 verifies PPF per-site coverage.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

**All graded column headers include GCR-N citations per header citation rule above.**

**Schema ID: TABLE_1:** `Role | Tier [GCR-1] | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
**Schema ID: TABLE_2:** `Entity | Field | Category | FLS Profile Configured? [GCR-5] | Roles: Read | Roles: Write | Gap? [GCR-6]`
**Schema ID: TABLE_3:** `Role | Tier [GCR-1] | OWD Baseline | Scope Modifier | Effective Scope | Verified? [GCR-4]`
**Schema ID: TABLE_4:** `Vector | Checked? [GCR-3] | Finding | Severity [GCR-2]`
**Schema ID: TABLE_5:** `# | Gap Type | Entity | Field or Rule | Role | Tier [GCR-1] | Severity [GCR-2] | Remediation`
**Schema ID: CS-2:** `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation` (SE-updatable: SE Cross-Reference, SE Confirmation)
**Schema ID: CS-3:** `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation` (SE-updatable: SE Cross-Reference, SE Confirmation)

### Step 0.2 — Criterion Enforcement Matrix Preamble

| Criterion | M1 | M2 | M3 | M4 |
|-----------|----|----|----|----|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-0+SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

SHALL-A through SHALL-G same as V-01. SHALL-H: PPF-1..PPF-6 all present before any table; CA-1.10 verifies.

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

[CS-0 acknowledges CS-2 and CS-3 schema IDs, SE-updatable columns, SE-update protocol. Then CS-1, CS-2, CS-3. Same structure as V-01.]

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis (Privilege-Tier Descent Order)

*All tables use GCR-N citations in column headers as declared in Step 0.1.*

### SE-0 — Admin-Tier Inventory and Escalation Vectors

**TABLE_4 — Escalation Vector Inventory** *(with Checked? [GCR-3] and Severity [GCR-2] headers)*

| Vector | Checked? [GCR-3] | Finding | Severity [GCR-2] |
|--------|------------------|---------|------------------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

### SE-1 / SHALL-A — Role-Operation Matrix

**TABLE_1** *(with Tier [GCR-1] header)*

| Role | Tier [GCR-1] | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|--------------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

### SE-2 / SHALL-B — Field-Level Security Coverage

MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:
[description]. STRUCTURED CLOSE: [TABLE_2 mechanism].

**TABLE_2 — FLS Coverage** *(with FLS Profile Configured? [GCR-5] and Gap? [GCR-6] headers)*

| Entity | Field | Category | FLS Profile Configured? [GCR-5] | Roles: Read | Roles: Write | Gap? [GCR-6] |
|--------|-------|----------|---------------------------------|-------------|--------------|--------------|

### SE-3 / SHALL-C — Record Access Scope

MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:
[description]. STRUCTURED CLOSE: [TABLE_3 mechanism].

**TABLE_3 — Record Scope by Role** *(with Tier [GCR-1] and Verified? [GCR-4] headers)*

| Role | Tier [GCR-1] | OWD Baseline | Scope Modifier | Effective Scope | Verified? [GCR-4] |
|------|--------------|--------------|----------------|-----------------|-------------------|

### SE-4 / SHALL-D — Privilege Escalation Cross-Reference

MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:
[description]. STRUCTURED CLOSE: [cross-tier differential from SE-0 TABLE_4 data].

### SE-5 / SHALL-E — Security Gap Inventory

**TABLE_5 — Security Gap Inventory** *(with Tier [GCR-1] and Severity [GCR-2] headers)*

| # | Gap Type | Entity | Field or Rule | Role | Tier [GCR-1] | Severity [GCR-2] | Remediation |
|---|----------|--------|---------------|------|--------------|------------------|-------------|

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

[CA-1.1 through CA-1.8 same as V-01.]

**CA-1.9 — C-16 verification (GCR-N column header citations):**
- Registry anchor — GCR header citation rule: every graded column header must include [GCR-N] suffix. GCR-1=Tier, GCR-2=Severity, GCR-3=Checked?, GCR-4=Verified?, GCR-5=FLS Profile Configured?, GCR-6=Gap?, GCR-7=Escalation Risk.
- Preamble anchor — Step 0.1 schema declarations include GCR-N in all graded column headers.
- Verification — TABLE_1: `Tier [GCR-1]`? TABLE_2: `FLS Profile Configured? [GCR-5]` and `Gap? [GCR-6]`? TABLE_3: `Tier [GCR-1]` and `Verified? [GCR-4]`? TABLE_4: `Checked? [GCR-3]` and `Severity [GCR-2]`? TABLE_5: `Tier [GCR-1]` and `Severity [GCR-2]`? -> PASS / FAIL per table.

**CA-1.10 — C-18 verification (PPF per table site):**
- Registry anchor — PPF catalog declared PPF-1..PPF-6, one per named table/schema site.
- Preamble anchor — SHALL-H: all 6 entries required before any table. CA-1.10 verifies count and site coverage.
- Verification — PPF-1 (TABLE_1)? PPF-2 (TABLE_2)? PPF-3 (TABLE_3)? PPF-4 (TABLE_4)? PPF-5 (TABLE_5)? PPF-6 (Escalation Risk)? Each with verbatim wrong form + criterion by ID? -> PASS / FAIL per entry.

**CA Format Compliance Verdict:** [C-01..C-05, SHALL-F, SHALL-G, CS-0, C-16 (CA-1.9), C-18 (CA-1.10). Overall: COMPLIANT / NON-COMPLIANT.]

---

## ASPIRATIONAL CRITERIA SELF-VERIFICATION (8-item, C-08..C-15)

| Criterion | Pass Condition | Fail Signal | Self-Assessment |
|-----------|----------------|-------------|-----------------|
| C-08 | Cross-entity cascade with mechanism named | No cross-entity analysis | |
| C-09 | Closing Summary table at SE-5 | No summary table | |
| C-10 | `[CLOSES: label]` on every table header | Annotation missing or paraphrased | |
| C-11 | Null-case row in every table | Null case as prose or table absent | |
| C-12 | Escalation Risk column; blank = auto-fail | Blank, "varies", or outside GCR-7 scale | |
| C-13 | GCR block: all 7 columns, (a)+(b)+(c) co-located per entry | (b) or (c) in separate section | |
| C-14 | At least one prohibited form verbatim + criterion by ID | No wrong form named | |
| C-15 | This table with Pass Condition / Fail Signal / Self-Assessment | Flat checklist only | |

---

## V-05 — Full Integration: C-16 + C-17 + C-18

**Axis:** C-16 + C-17 + C-18 full integration
**Hypothesis:** All three v4 mechanisms active simultaneously. GCR-N header citations (C-16) make every graded column self-annotated with its contract at point of use. The 11-row aspirational audit table (C-17) forces the model to verify all new criteria including C-16/C-17/C-18 themselves before output. The indexed PPF catalog (C-18) pre-names the wrong prose form at every table site. Together, these three mechanisms create three structural checkpoints — column header, self-audit row, and site-specific failure mode warning — that must all be satisfied for a clean submission. Any omission is caught at one of the three levels rather than reaching the user as silent output drift.

---

depth: standard
confidence: standard

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

Manual security reviews of Dataverse environments routinely miss three failure scenarios that this
trace is designed to surface:

**Blind spot 1 — Post-incident FLS gap.** Column security profiles are rarely audited proactively.
Sensitive fields — credit limits, compensation data, SSNs, contact identifiers — remain readable
and writable by any role unless a column security profile explicitly restricts them. The security
roles UI does not surface which fields lack column security profiles; gaps are discovered after
data exposure, not before.

**Blind spot 2 — Cumulative privilege blind spot.** A user holding a BU-scoped security role who
also belongs to an owner team whose team role grants org-wide access has effective org-wide access.
No single Dataverse UI view surfaces the combined effective access produced by role + team + OWD
combination. Spot-checking individual roles misses cross-role accumulation through team membership.

**Blind spot 3 — OWD-sharing-rule override gap.** Administrators check OWD settings
entity-by-entity without evaluating the sharing rules that silently override those baselines. A
Private OWD on Case combined with a Power Automate-triggered sharing rule grants effective
org-wide read to users who satisfy the trigger condition — including low-trust service accounts
and CS users not intended to have broad case access.

This trace closes all three blind spots: SE-2 closes Blind spot 1; SE-3 closes Blind spot 2;
SE-4 closes Blind spot 3. Closure notes are exact-label two-part blocks co-located at each SE
sub-section opening, carrying the exact blind-spot label from this CONTEXT section.

---

## GRADED COLUMN REGISTRY (CA-authored, Phase 0 precondition)

All graded columns declared before any table. Each entry has: (a) scale with all levels named,
(b) auto-fail condition for blank cells, (c) post-table verification instruction — all three
elements in one co-located block per entry.

**Header citation rule (C-16):** Every graded column header in every table MUST include its
[GCR-N] identifier in brackets at the point of use. Example: `Tier [GCR-1]` not `Tier`.
A column header missing its [GCR-N] suffix auto-fails CA-1.9 verification regardless of whether
the GCR-N entry is correctly declared in this block. Citation is required at the header, not just here.

**GCR-1 — Tier** (used in TABLE_1, TABLE_3, TABLE_5)
Scale: `Admin` / `Custom` / `Restricted`
Auto-fail: any cell not one of these three values is a blank-equivalent and auto-fails TABLE verification.
Post-table verification: after each table with a Tier [GCR-1] column, confirm every row has one of the three declared values.

**GCR-2 — Severity** (used in TABLE_4, TABLE_5)
Scale: `CRITICAL` (exploitable with no additional steps) / `HIGH` (exploitable with one intermediate step) / `MEDIUM` (limited blast radius or requires specific conditions)
Auto-fail: any Severity cell blank or outside CRITICAL / HIGH / MEDIUM auto-fails TABLE verification.
Post-table verification: after TABLE_5, list any non-compliant Severity row as NON-COMPLIANT.

**GCR-3 — Checked?** (used in TABLE_4)
Scale: `YES` (vector examined, finding or specific rule-out written) / `NO` (not checked — auto-fail)
Auto-fail: Checked? = NO or blank auto-fails TABLE_4 verification. All four vectors must be YES.
Post-table verification: after TABLE_4, confirm all four rows Checked? [GCR-3] = YES.

**GCR-4 — Verified?** (used in TABLE_3)
Scale: `YES` (scope confirmed against configuration) / `NO` (scope inferred — flag as gap)
Auto-fail: blank Verified? treated as NO and auto-fails the row.
Post-table verification: after TABLE_3, list NO rows as unconfirmed scope entries requiring follow-up.

**GCR-5 — FLS Profile Configured?** (used in TABLE_2)
Scale: `Configured` (column security profile exists and restricts field) / `Not Configured` (no profile; field accessible to any role with entity access)
Auto-fail: blank or any value outside Configured / Not Configured auto-fails TABLE_2 verification.
Post-table verification: after TABLE_2, confirm every row has one of the two declared values.

**GCR-6 — Gap?** (used in TABLE_2)
Scale: `YES` (missing or insufficient protection — forward to TABLE_5) / `NO` (adequately protected)
Auto-fail: blank Gap? cell auto-fails the row. Every YES row must have a TABLE_5 cross-reference.
Post-table verification: after TABLE_2, verify every YES row has a TABLE_5 cross-reference.

**GCR-7 — Escalation Risk** (used in Closing Summary)
Scale: `HIGH` / `MEDIUM` / `LOW` / `NONE`
Auto-fail: blank, "varies", or "see above" is blank-equivalent and auto-fails Closing Summary verification.
Post-table verification: after Closing Summary, list any non-declared Escalation Risk [GCR-7] as NON-COMPLIANT.

---

## PROHIBITED PROSE FORMS CATALOG (One entry per named table/schema site — C-18)

Coverage rule: PPF-1 through PPF-6, one per named table/schema. Each entry: site label +
verbatim prohibited form + criterion violated by ID. CA-1.10 verifies all 6 entries present
and no table site is missing. Using any prohibited form at the named site is a structural
failure, not a content gap.

**PPF-1 — TABLE_1 (Role-Operation Matrix) — null case:**
Prohibited form: "No operations are restricted for this entity." or leaving any operation-column cell blank.
Criterion violated: C-11 — null case must be an explicit TABLE_1 data row: `[Entity] | [Tier] | N/A | N/A | N/A | N/A | N/A | N/A | N/A | N/A | No operations available in this configuration`.

**PPF-2 — TABLE_2 (FLS Coverage) — null case:**
Prohibited form: "No column security profiles active on {{topic}}." written as prose above, below, or in place of the table.
Criterion violated: C-11 — null case must be a TABLE_2 data row: `[Entity] | [Field] | [Category] | Not Configured | All roles | All roles | YES` with a corresponding TABLE_5 MISSING-FLS entry.

**PPF-3 — TABLE_3 (Record Scope by Role) — role omission:**
Prohibited form: "Inherits scope from TABLE_1" or "Default OWD applies" used instead of an explicit TABLE_3 row for a role.
Criterion violated: C-03 — every TABLE_1 role must appear in TABLE_3 with Effective Scope, OWD Baseline, and Scope Modifier all explicitly stated.

**PPF-4 — TABLE_4 (Escalation Vector Inventory) — rule-out shortcut:**
Prohibited form: "No escalation paths identified." or "None found." as the Finding cell for any vector.
Criterion violated: C-04 — rule-out format: "Checked [vector]: no path found because [specific Dataverse control name] prevents [escalation mechanism]." Generic statements do not satisfy the specificity requirement.

**PPF-5 — TABLE_5 (Security Gap Inventory) — zero-gap omission:**
Prohibited form: Omitting TABLE_5 entirely, or "No security gaps found." as prose with an empty table, or an absent table.
Criterion violated: C-04 — zero-gap case requires explicit REVIEWED-NO-GAP evidence rows: `| 1 | REVIEWED-NO-GAP | [Entity] | [Field or Rule] | [Role] | [Tier] | N/A | Evidence: [specific control] prevents exploitation |`.

**PPF-6 — Escalation Risk column (Closing Summary) — vague/blank:**
Prohibited form: "Varies by entity", "See TABLE_5 for details", blank cell, or any value outside HIGH / MEDIUM / LOW / NONE.
Criterion violated: C-12 — Escalation Risk [GCR-7] must be one declared scale value with inline justification in the same cell. Cross-referencing another section is not an inline justification.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins.

**PHASE 0 — CA (Compliance Auditor):**
CA executes first. Authors Schema Registry (Step 0.1: all seven schemas with GCR-N citations in
graded column headers) and Criterion Enforcement Matrix preamble (Step 0.2: SHALL-A through SHALL-H,
M4 rows CA-1.1 through CA-1.10 pre-assigned). Issues handoff to PHASE 1.

**PHASE 1 — CS (Customer Success):**
CS-0 Registry acknowledgment (echo CS-2 and CS-3 schema IDs with SE-updatable columns) before
CS-1/CS-2/CS-3. CS does not fill TABLE_1-5. Issues handoff to PHASE 2.

**PHASE 2 — SE (Security Engineer / Dataverse Security Expert):**
SE-0 (admin inventory + TABLE_4 with Checked? [GCR-3] and Severity [GCR-2] headers) before SE-1.
All tables populated with GCR-N citations in column headers. SE-2/SE-3/SE-4 use exact-label
two-part closure blocks per SHALL-G. Issues handoff to PHASE 3.

**PHASE 3 — CA-1 (CA Verification Pass):**
CA returns. Double-anchor reaffirmation for CA-1.1 through CA-1.10. CA-1.9 verifies GCR-N
header citations in all tables. CA-1.10 verifies PPF-1..PPF-6 per-site coverage. CA-1.11 not
added; C-17 is verified by the aspirational audit table's own structural completeness.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1 and 0.2 before any other phase begins.*

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

**All table schemas declared with GCR-N citations in graded column headers per header citation
rule. Blank-cell prohibition is global. SE-update protocols for CS-2 and CS-3 co-located.**

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Tier [GCR-1] | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Tier [GCR-1] values: Admin / Custom / Restricted. Rows ordered: Admin first, Custom second, Restricted last.
Blank-cell rule: all cells Granted / Denied / Conditional (condition inline) / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? [GCR-5] | Roles: Read | Roles: Write | Gap? [GCR-6]`
Blank-cell rule: FLS Profile Configured? [GCR-5] = Configured / Not Configured. Gap? [GCR-6] = YES / NO.

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | Tier [GCR-1] | OWD Baseline | Scope Modifier | Effective Scope | Verified? [GCR-4]`
Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name]. Verified? [GCR-4] = YES / NO.

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? [GCR-3] | Finding | Severity [GCR-2]`
Blank-cell rule: all four vectors, Checked? [GCR-3] = YES.

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Tier [GCR-1] | Severity [GCR-2] | Remediation`
Blank-cell rule: Remediation = exact object + exact location + expected post-fix state.
CS-EXPECTATION-VIOLATED three-field block: CS-Expected / SE-Actual / Delta.

**Schema ID: CS-2 — Sharing Rule Expectations**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference (TABLE_4 row ID or TABLE_5 row ID); SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE update protocol: SE populates after TABLE_4 analysis. CONTRADICTED triggers CS-EXPECTATION-VIOLATED per SHALL-F.

**Schema ID: CS-3 — Cross-Role Access Differential Expectations**
Declared columns: `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference (TABLE_1 or TABLE_3 row ID); SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE update protocol: SE populates after TABLE_1/TABLE_3 analysis. CONTRADICTED triggers CS-EXPECTATION-VIOLATED per SHALL-F.

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: M1, M2, M3 simultaneously active. M4 pre-assigned.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-0 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**SHALL obligations:**

- SHALL-A: Complete TABLE_1 with Tier [GCR-1] column. Every cell Granted/Denied/Conditional/N/A. Rows ordered by tier.
- SHALL-B: TABLE_2 lists all PII, Financial, Audit-Compliance fields. FLS Profile Configured? [GCR-5] and Gap? [GCR-6] explicit. Null case explicit.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier [GCR-1] and Effective Scope filled. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 at SE-0 (before SE-1). All four vectors, Checked? [GCR-3] = YES. Rule-outs name specific mechanism and reason.
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap case requires explicit REVIEWED-NO-GAP evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows carry three-field Remediation block. Incomplete rows reopened. CA-1.6 verifies.
- SHALL-G: SE-2, SE-3, SE-4 each open with two-part exact-label closure block: `MANUAL GAP [<exact CONTEXT label>]:` then `STRUCTURED CLOSE:`. Paraphrase, single-line annotation, or cross-section split fails. CA-1.7 verifies.
- SHALL-H: PPF-1 through PPF-6 all present in PROHIBITED PROSE FORMS CATALOG before any table. CA-1.10 verifies count and site coverage.

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

*CS opens with CS-0 Registry acknowledgment before authoring any expectation content.*

### CS-0 — Schema Registry Acknowledgment (CS-authored, Phase 1)

**Registry acknowledgment for CS-2:**
Schema ID: CS-2 — Sharing Rule Expectations.
SE-updatable columns as declared by CA in Phase 0 Schema Registry: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged: SE populates SE Cross-Reference (TABLE_4 or TABLE_5 row ID) and
SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE) after SE-0/TABLE_4 analysis.
Expectation format confirmed: CS-2 columns as declared. SE-updatable columns left blank; SE fills after SE-0.

**Registry acknowledgment for CS-3:**
Schema ID: CS-3 — Cross-Role Access Differential Expectations.
SE-updatable columns as declared by CA in Phase 0 Schema Registry: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged: SE populates SE Cross-Reference (TABLE_1 or TABLE_3 row ID) and
SE Confirmation after SE-1/SE-3 analysis.
Expectation format confirmed: CS-3 columns as declared. SE-updatable columns left blank; SE fills after SE-1/SE-3.

### CS-1 — Expected Customer Service Access Baseline

For each entity in scope: (a) which CRUD operations the CS role is expected to perform; (b) expected
record scope; (c) which sensitive fields CS needs access to and why. Identify configurations that
may inadvertently open access beyond job requirements.

**CS-2 — Sharing rule expectations** *(CS-2 schema; SE-updatable columns blank)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

**CS-3 — Cross-role access differential** *(CS-3 schema; SE-updatable columns blank)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis (Privilege-Tier Descent Order)

*SE traces from highest-privilege tier to lowest. All tables use GCR-N header citations as
declared in Step 0.1. SE-0 before SE-1. SE-2/SE-3/SE-4 use exact-label two-part closure blocks.*

### SE-0 — Admin-Tier Inventory and Escalation Vectors

Admin-tier role inventory: System Administrator, Environment Admin, admin-equivalent roles.
Note capabilities that bypass lower-tier controls.

**TABLE_4 — Escalation Vector Inventory** *(GCR-3 and GCR-2 headers required)*

| Vector | Checked? [GCR-3] | Finding | Severity [GCR-2] |
|--------|------------------|---------|------------------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Finding format: `[Role] -> [Mechanism] -> [Elevated access achieved]` for confirmed escalation;
"Checked [mechanism]: no path found because [specific reason]" for rule-out.
After TABLE_4: populate CS-2 SE Cross-Reference and SE Confirmation.

### SE-1 / SHALL-A — Role-Operation Matrix

**TABLE_1 — Role-Operation Matrix** *(GCR-1 header required)*

| Role | Tier [GCR-1] | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|--------------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Rows ordered: Admin tier first, Custom second, Restricted last.
Cross-role differential: compare CS role against one Admin-tier and one Custom-tier role.
After TABLE_1: populate CS-3 SE Cross-Reference and SE Confirmation.

### SE-2 / SHALL-B — Field-Level Security Coverage

MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:
Column security profiles are not auditable from the security roles UI; administrators discover
missing FLS only after a data exposure event reveals that a sensitive field was readable or
writable by an unintended role.

STRUCTURED CLOSE:
TABLE_2 below enumerates every sensitive field in scope with its explicit FLS Profile Configured? [GCR-5]
status, surfacing pre-event what the security roles UI conceals. All Not Configured fields are
forwarded to TABLE_5 as MISSING-FLS gaps with Tier [GCR-1] identifying the highest-privilege
tier with access.

**TABLE_2 — FLS Coverage** *(GCR-5 and GCR-6 headers required)*

| Entity | Field | Category | FLS Profile Configured? [GCR-5] | Roles: Read | Roles: Write | Gap? [GCR-6] |
|--------|-------|----------|---------------------------------|-------------|--------------|--------------|

Categories: PII / Financial / Audit-Compliance / Other-Sensitive.
Defense-in-depth layer check: identify enforcement layer for at least one sensitive field.

### SE-3 / SHALL-C — Record Access Scope

MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access produced by a security role
plus owner team membership plus OWD; spot-checking roles individually misses cross-role privilege
accumulation through team inheritance.

STRUCTURED CLOSE:
TABLE_3 below maps effective scope for every role by Tier [GCR-1], recording OWD baseline, scope
modifier, and effective scope in one traceable row, making team-accumulated privilege visible
at the tier it occurs.

**TABLE_3 — Record Scope by Role** *(GCR-1 and GCR-4 headers required)*

| Role | Tier [GCR-1] | OWD Baseline | Scope Modifier | Effective Scope | Verified? [GCR-4] |
|------|--------------|--------------|----------------|-----------------|-------------------|

Every TABLE_1 role MUST appear, ordered by Tier [GCR-1].
After TABLE_3: update CS-3 SE Confirmation.

### SE-4 / SHALL-D — Privilege Escalation Cross-Reference

MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing the sharing rules
that silently override them; a Private OWD combined with an active sharing rule can grant
effective org-wide access without appearing in any security roles UI view.

STRUCTURED CLOSE:
TABLE_4 (filled at SE-0) evaluated all four escalation vectors. This section adds cross-tier
differential summary: for the most privileged Admin-tier role and most restricted Restricted-tier
role, identify the specific enforcement layer where access diverges, citing the SE-0 TABLE_4
row ID (Severity [GCR-2] value) that established the admin-tier ceiling.

### SE-5 / SHALL-E — Security Gap Inventory + Closing Summary

**TABLE_5 — Security Gap Inventory** *(GCR-1 and GCR-2 headers required)*

| # | Gap Type | Entity | Field or Rule | Role | Tier [GCR-1] | Severity [GCR-2] | Remediation |
|---|----------|--------|---------------|------|--------------|------------------|-------------|

Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.
CS-EXPECTATION-VIOLATED three-field Remediation: CS-Expected / SE-Actual / Delta.

**Closing Summary:**

| Role | Tier [GCR-1] | Verdict | Open Gap IDs | Escalation Risk [GCR-7] |
|------|--------------|---------|--------------|-------------------------|

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

*CA returns. Each row presents Registry anchor and Preamble anchor as structurally distinct
labeled elements before Verification line.*

**CA-1.1 — C-01 verification:**
- Registry anchor — Schema ID TABLE_1 (with Tier [GCR-1]).
- Preamble anchor — C-01: TABLE_1 / SE-1 / SHALL-A / CA-1.1.
- Verification — TABLE_1 present? Tier [GCR-1] column populated? Rows ordered by tier? All cells filled? -> PASS / FAIL

**CA-1.2 — C-02 verification:**
- Registry anchor — Schema ID TABLE_2 (with FLS Profile Configured? [GCR-5] and Gap? [GCR-6]).
- Preamble anchor — C-02: TABLE_2 / SE-2 / SHALL-B / CA-1.2.
- Verification — TABLE_2 present? All sensitive fields? FLS status explicit? Null case stated? Gap? [GCR-6] YES rows in TABLE_5? -> PASS / FAIL

**CA-1.3 — C-03 verification:**
- Registry anchor — Schema ID TABLE_3 (with Tier [GCR-1], Verified? [GCR-4]).
- Preamble anchor — C-03: TABLE_3 / SE-0+SE-3 / SHALL-C / CA-1.3.
- Verification — Every TABLE_1 role in TABLE_3? Tier [GCR-1] populated? Effective Scope filled? Verified? [GCR-4] filled? -> PASS / FAIL

**CA-1.4 — C-04 verification:**
- Registry anchor — Schema ID TABLE_4 (with Checked? [GCR-3] and Severity [GCR-2]; all four vectors).
- Preamble anchor — C-04: TABLE_4 / SE-0 / SHALL-D / CA-1.4.
- Verification — TABLE_4 at SE-0? All four vectors? Checked? [GCR-3] = YES? Specific findings or rule-outs? -> PASS / FAIL

**CA-1.5 — C-05 verification:**
- Registry anchor — Schema ID TABLE_5 (with Tier [GCR-1], Severity [GCR-2]).
- Preamble anchor — C-05: TABLE_5 / SE-5 / SHALL-E / CA-1.5.
- Verification — TABLE_5 present? Named gap? Tier [GCR-1] populated? Severity [GCR-2] populated? Remediations exact? -> PASS / FAIL

**CA-1.6 — SHALL-F compliance verification:**
- Registry anchor — TABLE_5 CS-EXPECTATION-VIOLATED row schema: CS-Expected, SE-Actual, Delta all required.
- Preamble anchor — SHALL-F: three-field block mandatory. Incomplete rows reopened.
- Verification — For each CS-EXPECTATION-VIOLATED row: CS-Expected populated? SE-Actual populated? Delta populated? -> PASS / FAIL per row.

**CA-1.7 — SHALL-G compliance verification (exact-label two-part closure blocks):**
- Registry anchor — CONTEXT exact labels: "Blind spot 1 — Post-incident FLS gap" (SE-2); "Blind spot 2 — Cumulative privilege blind spot" (SE-3); "Blind spot 3 — OWD-sharing-rule override gap" (SE-4).
- Preamble anchor — SHALL-G: Line 1 = `MANUAL GAP [<exact label>]:`. Character-for-character. Followed by `STRUCTURED CLOSE:`. Paraphrase fails.
- Verification — SE-2 opens with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:`? SE-3 with `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:`? SE-4 with `MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:`? Each followed by `STRUCTURED CLOSE:`? -> PASS / FAIL per section.

**CA-1.8 — CS-2/CS-3 Schema Registry + CS-0 acknowledgment verification:**
- Registry anchor — CS-2 and CS-3 as named schema entries with SE-updatable columns and SE-update protocols co-located.
- Preamble anchor — CS-0 acknowledgment is a PHASE 1 structural requirement.
- Verification — CS-2 in Schema Registry? CS-3 same? CS-0 present before CS-1? CS-0 cites both schema IDs by exact label? CS-0 lists SE-updatable columns? SE populated SE-updatable columns? -> PASS / FAIL

**CA-1.9 — C-16 verification (GCR-N column header citations):**
- Registry anchor — GCR header citation rule: every graded column header must include [GCR-N] suffix. GCR-1=Tier, GCR-2=Severity, GCR-3=Checked?, GCR-4=Verified?, GCR-5=FLS Profile Configured?, GCR-6=Gap?, GCR-7=Escalation Risk. Missing [GCR-N] in any header = auto-fail.
- Preamble anchor — Step 0.1 declared all schemas with GCR-N citations. Closing Summary declared with Escalation Risk [GCR-7].
- Verification — TABLE_1 has `Tier [GCR-1]`? TABLE_2 has `FLS Profile Configured? [GCR-5]` and `Gap? [GCR-6]`? TABLE_3 has `Tier [GCR-1]` and `Verified? [GCR-4]`? TABLE_4 has `Checked? [GCR-3]` and `Severity [GCR-2]`? TABLE_5 has `Tier [GCR-1]` and `Severity [GCR-2]`? Closing Summary has `Escalation Risk [GCR-7]`? -> PASS / FAIL per table.

**CA-1.10 — C-18 verification (PPF per table site):**
- Registry anchor — PROHIBITED PROSE FORMS CATALOG declared PPF-1..PPF-6, one per named table/schema site: TABLE_1, TABLE_2, TABLE_3, TABLE_4, TABLE_5, Escalation Risk.
- Preamble anchor — SHALL-H: all 6 entries required before any table; CA-1.10 verifies count and site identity.
- Verification — PPF-1 (TABLE_1) present? PPF-2 (TABLE_2) present? PPF-3 (TABLE_3) present? PPF-4 (TABLE_4) present? PPF-5 (TABLE_5) present? PPF-6 (Escalation Risk) present? Each entry has verbatim prohibited form + criterion violated by ID? -> PASS / FAIL per entry.

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0).
[C-01..C-05: CA-1.1..CA-1.5. SHALL-F: CA-1.6. SHALL-G: CA-1.7. CS-0: CA-1.8. C-16 GCR-N headers: CA-1.9. C-18 PPF per site: CA-1.10. Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

---

## ASPIRATIONAL CRITERIA SELF-VERIFICATION (11-item, C-08..C-18)

Complete ALL rows before finalizing output. FAIL in any row requires revision before submission.
C-17 is self-referential: verify this table has exactly 11 rows with all three columns populated
as part of the C-17 self-assessment.

| Criterion | Pass Condition | Fail Signal | Self-Assessment |
|-----------|----------------|-------------|-----------------|
| C-08 | At least one cross-entity cascade traced: permission on Entity A produces derived access on Entity B, cascade mechanism named explicitly | No cross-entity effect analyzed; analysis confined to single entity | |
| C-09 | Closing Summary table present at SE-5 with role + verdict + open gap IDs + Escalation Risk [GCR-7] per row | Closing Summary absent; findings only in individual SE sub-sections | |
| C-10 | Every table header includes `[CLOSES: <exact blind spot label>]` character-for-character from CONTEXT section | Table headers missing CLOSES annotation; label paraphrased or absent | |
| C-11 | Every table has a null-case row showing the table when no instances of the tracked phenomenon exist | Table absent when "no items found"; null case stated as prose above or below table | |
| C-12 | Escalation Risk [GCR-7] column in Closing Summary using declared scale; blank or "varies" = auto-fail | Escalation Risk cell blank, uses "varies", "see above", or value outside HIGH / MEDIUM / LOW / NONE | |
| C-13 | GCR block present before any table; all 7 graded columns registered (GCR-1..GCR-7); each entry has (a) full scale with all levels named, (b) auto-fail condition, (c) post-table verification instruction — all three elements co-located in one block per entry | Fewer than 7 registered; any entry missing (b) or (c); elements split across sections | |
| C-14 | At least one prohibited prose form named with verbatim wrong form text + criterion violated by ID | No prohibited form named; only correct form described | |
| C-15 | This table present with three columns (Pass Condition / Fail Signal / Self-Assessment) covering aspirational criteria | Flat checklist with criterion IDs only; column structure absent | |
| C-16 | Every graded column header in every table includes its [GCR-N] citation (e.g., `Tier [GCR-1]`, `Severity [GCR-2]`) — verifiable at the header level without reading the GCR block | Any graded column header in any table missing its [GCR-N] suffix | |
| C-17 | This table has exactly 11 rows covering C-08..C-18; every row has Pass Condition, Fail Signal, and Self-Assessment columns populated | Fewer than 11 rows; any criterion from C-08..C-18 missing a row; any column empty in any row | |
| C-18 | Prohibited prose catalog has one entry per named table/schema site (TABLE_1..TABLE_5 + Escalation Risk = minimum 6 entries); each entry maps verbatim wrong form → criterion violated by ID | Fewer than 6 entries; any named table site without a dedicated PPF entry; criterion ID absent from any entry | |
