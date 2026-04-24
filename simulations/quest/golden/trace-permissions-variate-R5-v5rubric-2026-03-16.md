# trace-permissions — Quest Variate Round 5 (Rubric v4, R4 Excellence Signals)

**Date:** 2026-03-16
**Rubric:** v4 (C-01..C-18, N=11 aspirational)
**Target patterns:** R4 V-05 excellence signals not yet captured in C-01..C-18:
- Signal 2 — Closing Summary treated as named schema in Step 0.1 (TABLE_6), not just a prose section at SE-5
- Signal 1 — Self-referential completeness lock in C-17 row produces no *observable* count trace; model can assert PASS without writing a count
- Signal 3 — Triple-point enforcement was observed in V-05 retrospectively but not declared as a first-class enforcement-density property in Step 0.2

**Base:** R4 V-05 mechanics retained across all R5 variations (GCR-N headers in all column declarations, PPF-1..PPF-6 indexed by table site, 11-row aspirational table covering C-08..C-18). R5 variations add structural mechanisms targeting the three R4 signals without removing any existing mechanism.

---

## Round 5 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Signal 2 single axis — Closing Summary registered as TABLE_6 in Step 0.1 | R4 V-05 declared the Closing Summary with GCR-N column headers inside SE-5 and verified them in CA-1.9, but did NOT register it as `Schema ID: TABLE_6` in the central Step 0.1 Schema Registry. Without a Schema ID, the Closing Summary cannot occupy an M1 cell in the enforcement matrix and GCR-N coverage audit must be inferred from prose. Registering TABLE_6 in Step 0.1 makes the Closing Summary structurally identical to TABLE_1..TABLE_5: it has a Schema ID, an M1 cell in the enforcement matrix, a dedicated SHALL-I obligation, and a CA-1.11 verification row that checks it mechanically |
| V-02 | Signal 1 single axis — Count-mandate annotation in C-17 row | R4 V-05 C-17 pass condition says "verify this table has exactly 11 rows." A model can write PASS without observably counting. Adding COUNT MANDATE to the C-17 row — requiring `Row count: [N]` on a labeled line directly before the Self-Assessment cell — creates a structural audit trace: Row count < 11 before PASS is a contradiction CA can flag without reading the table; absent Row count label = auto-fail. The completeness claim becomes verifiable, not merely asserted |
| V-03 | Signal 3 single axis — M5 Enforcement Layers column in Step 0.2 matrix | R4 V-05's triple-point enforcement for C-16/C-17/C-18 was an emergent property observed in the scorecard, not a declared structural property. Adding M5: Enforcement Layers to the Step 0.2 matrix turns enforcement density into a registered first-class attribute. Any criterion recorded as single-layer is explicitly flagged for upgrade. CA-1.12 verifies that no single-layer criterion remains unresolved before marking the preamble compliant |
| V-04 | Combined: TABLE_6 schema + count-mandate lock | TABLE_6 Schema Registry registration (V-01) combined with count-mandate C-17 row (V-02): every graded output site has a registered schema, and the completeness assertion for the self-audit table is provably observable |
| V-05 | Full integration: all three R5 mechanisms + 14-row aspirational table | TABLE_6 schema + count-mandate + M5 enforcement-density column. Aspirational self-audit table extends to 14 rows (C-08..C-21) where C-19 = Closing Summary Schema Registration, C-20 = Count-Mandate Completeness Lock, C-21 = Enforcement-Density Declaration — making the self-audit loop explicitly target all three new candidate criteria |

---

## V-01 — Single Axis: Signal 2 (TABLE_6 Closing Summary Schema Registration)

**Axis:** Signal 2 single axis
**Hypothesis:** The difference between "Closing Summary table with GCR-N headers described in SE-5" (R4 V-05) and "Schema ID: TABLE_6 registered in Step 0.1" is structural, not cosmetic. With a Schema ID: TABLE_6 entry in the central registry, the enforcement matrix can carry TABLE_6 in its M1 column, SHALL-I can require TABLE_6 presence before CA-1 passes, and CA-1.11 can verify TABLE_6 mechanically using the same double-anchor structure as CA-1.1..CA-1.5. The Closing Summary stops being an aspirational output that "should" be present and becomes a schema-registered output whose absence is a structural failure — detectable before the aspirational self-audit loop runs.

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

**GCR-1 — Tier** (used in TABLE_1, TABLE_3, TABLE_5, TABLE_6)
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

**GCR-7 — Escalation Risk** (used in TABLE_6)
Scale: `HIGH` (role combination or sharing rule produces access materially exceeding job function) / `MEDIUM` (access exceeds job function in limited scope) / `LOW` (minor excess access; unlikely to be exploited) / `NONE` (access appropriate to job function; no escalation vector confirmed)
Auto-fail: blank Escalation Risk cell auto-fails TABLE_6 verification. Inline text "varies" or "see above" is blank-equivalent.
Post-table verification: after TABLE_6, list any row with a blank or non-declared Escalation Risk as NON-COMPLIANT.

---

## PROHIBITED PROSE FORMS CATALOG (One entry per named table/schema site)

Exactly one entry per named table or schema in this trace. Each entry identifies the wrong form
verbatim and the criterion it violates by ID. Using a prohibited form at the named site is a
structural failure detectable by CA-1.10. Coverage rule: PPF-1 through PPF-6 must all be present.

**PPF-1 — TABLE_1 (Role-Operation Matrix) — null case:**
Prohibited form: "No operations are restricted for this entity." or leaving a TABLE_1 cell blank.
Criterion violated: C-11 — null case must be a data row with all cells explicitly filled, not inline prose.

**PPF-2 — TABLE_2 (FLS Coverage) — null case:**
Prohibited form: Writing "No column security profiles active on {{topic}}." as prose above or below the table instead of as an explicit TABLE_2 row.
Criterion violated: C-11 — null case must appear as an explicit TABLE_2 row with FLS Profile Configured? [GCR-5] = Not Configured.

**PPF-3 — TABLE_3 (Record Scope by Role) — omission form:**
Prohibited form: Omitting a role from TABLE_3 with a note "inherits scope from TABLE_1" or "default OWD applies."
Criterion violated: C-03 — every TABLE_1 role must appear in TABLE_3 with Effective Scope explicitly stated.

**PPF-4 — TABLE_4 (Escalation Vector Inventory) — rule-out shortcut:**
Prohibited form: Writing "No escalation paths identified." as the Finding cell for any vector.
Criterion violated: C-04 — rule-out format requires naming the specific mechanism: "Checked [vector]: no path found because [specific control] prevents [escalation mechanism]."

**PPF-5 — TABLE_5 (Security Gap Inventory) — zero-gap omission:**
Prohibited form: Leaving TABLE_5 absent or empty, or writing "No security gaps found." above the table.
Criterion violated: C-04 — zero-gap case requires explicit evidence rows with Remediation citing a specific control.

**PPF-6 — TABLE_6 (Closing Summary) — blank Escalation Risk cell:**
Prohibited form: Writing "Varies by entity" or "See TABLE_5 for details" or leaving the Escalation Risk [GCR-7] cell blank in any TABLE_6 row.
Criterion violated: C-12 — Escalation Risk must be one value from GCR-7 scale with an inline justification in the same cell.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins.

**PHASE 0 — CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1: TABLE_1 through TABLE_6 with Tier [GCR-1]
columns on TABLE_1, TABLE_3, TABLE_5, TABLE_6; CS-2 and CS-3 with SE-updatable columns and SE-update
protocols — eight schemas total) and the Criterion Enforcement Matrix preamble (Step 0.2: SHALL-A
through SHALL-I, M4 row IDs CA-1.1 through CA-1.11 pre-assigned). CA issues handoff to PHASE 1.

**PHASE 1 — CS (Customer Success):**
Executes second. Opens with CS-0 sub-section (Schema Registry acknowledgment: CS echoes Registry
schema IDs for CS-2 and CS-3 by exact Schema ID label, lists SE-updatable columns for each, and
confirms the expectation format before authoring any expectation rows). Then produces CS-1, CS-2,
CS-3 using Registry schemas. CS does not fill TABLE_1-6. CS issues handoff to PHASE 2.

**PHASE 2 — SE (Security Engineer / Dataverse Security Expert):**
Executes third in privilege-tier descent order. SE-0 (admin-tier inventory and TABLE_4 escalation
vectors) runs before SE-1 (role-operation matrix), establishing the privilege ceiling before
populating operation cells. TABLE_1 and TABLE_3 include Tier [GCR-1] column. SE-2, SE-3, SE-4
each open with two-part exact-label closure blocks per SHALL-G. SE-5 produces TABLE_5 and TABLE_6
using the registered Schema IDs. Issues handoff to PHASE 3.

**PHASE 3 — CA-1 (CA Verification Pass):**
CA returns. Each CA-1 row performs double-anchor reaffirmation: Registry anchor and Preamble
anchor as structurally distinct labeled elements. Verification line follows. Inline concatenation
fails. CA-1.8 extended to verify CS-0 acknowledgment precedes CS-1. CA-1.9 verifies GCR-N
header citations in every table including TABLE_6. CA-1.10 verifies PPF per-site coverage.
CA-1.11 verifies TABLE_6 schema registration and SHALL-I compliance.

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
Note: TABLE_4 executes at SE-0 before SE-1 because admin-tier role structure determines escalation
paths before the lower-tier role-operation matrix is populated.

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Tier [GCR-1] | Severity [GCR-2] | Remediation`
Blank-cell rule: Remediation = exact object + exact location + expected post-fix state.
CS-EXPECTATION-VIOLATED Remediation (three-field block):
- CS-Expected: cite CS-2 or CS-3 row, state expectation verbatim or by row reference.
- SE-Actual: SE finding that contradicts the expectation.
- Delta: exact configuration change to align SE-Actual to CS-Expected.

**Schema ID: TABLE_6 — Closing Summary**
Declared columns: `Role | Tier [GCR-1] | Verdict | Open Gap IDs | Escalation Risk [GCR-7]`
Tier [GCR-1] values: Admin / Custom / Restricted. Verdict values: PASS-CLEAN (no TABLE_5 gaps for
this role) / PASS-WITH-GAPS (gaps present, none CRITICAL) / FAIL (CRITICAL gap or unresolved
CS-EXPECTATION-VIOLATED). Open Gap IDs: comma-separated TABLE_5 row numbers, or NONE.
Escalation Risk [GCR-7]: one of HIGH / MEDIUM / LOW / NONE with inline justification in same cell.
Blank-cell rule: no column may be blank; Verdict and Escalation Risk [GCR-7] must use declared values.
Note: TABLE_6 executes at SE-5, after TABLE_5. One row per TABLE_1 role required per SHALL-I.
Absent TABLE_6 is a structural failure (not an aspirational miss).

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
| C-09 | TABLE_6 | SE-5 | SHALL-I | CA-1.11 |

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A: Complete TABLE_1 with Tier [GCR-1] column. Every cell Granted/Denied/Conditional/N/A. Rows ordered by tier.
- SHALL-B: TABLE_2 lists all PII, Financial, and Audit-Compliance fields with explicit FLS status. Null case explicit. Gap? [GCR-6] YES rows in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier [GCR-1] and Effective Scope filled. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 at SE-0 (before SE-1), all four vectors, Checked? [GCR-3] = YES. Rule-outs name specific mechanism and reason.
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap case requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field Remediation block (CS-Expected, SE-Actual, Delta). Incomplete rows MUST be reopened. CA-1.6 verifies.
- SHALL-G: At the opening of SE-2, SE-3, and SE-4, closure MUST appear as a two-part labeled block — Line 1: `MANUAL GAP [<exact CONTEXT label>]:`; Line 2: description of what manual audits miss; Line 3: `STRUCTURED CLOSE:`; Line 4: which table and mechanism closes it. Single-line annotation, blockquote format, TABLE_5 consolidation, or paraphrased label all fail SHALL-G. CA-1.7 verifies exact label carry-through.
- SHALL-H: PPF-1 through PPF-6 must all be present in the PROHIBITED PROSE FORMS CATALOG before any table is populated. CA-1.10 verifies count and site coverage.
- SHALL-I: TABLE_6 MUST be present at SE-5 using Schema ID TABLE_6 declared column structure. Absent TABLE_6 = structural failure, not an aspirational miss. Every TABLE_1 role must have a TABLE_6 row. CA-1.11 verifies schema registration and row completeness.

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
exact-label two-part closure blocks per SHALL-G. SE-5 produces TABLE_5 and TABLE_6 using
registered Schema IDs.*

### SE-0 — Admin-Tier Inventory and Escalation Vectors (executes before TABLE_1)

**Admin-tier role inventory:** List System Administrator, Environment Admin, and any
admin-equivalent roles with record scope and key capabilities. Note any admin capability that
bypasses lower-tier controls (e.g., System Administrator bypasses column security profiles).
This establishes the privilege ceiling for all lower-tier roles in SE-1.

**TABLE_4 — Escalation Vector Inventory** *(Schema Registry TABLE_4; placed at SE-0)*

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
that established the admin-tier ceiling. State whether the divergence is expected and what
sharing-rule interaction (if any) was confirmed or ruled out in SE-0 TABLE_4.

### SE-5 / SHALL-E + SHALL-I — Section 5: Security Gap Inventory and Closing Summary

**TABLE_5 — Security Gap Inventory** *(Schema Registry TABLE_5 with Tier [GCR-1] and Severity [GCR-2] columns; blank-cell rule)*

| # | Gap Type | Entity | Field or Rule | Role | Tier [GCR-1] | Severity [GCR-2] | Remediation |
|---|----------|--------|---------------|------|--------------|------------------|-------------|

Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED /
CS-EXPECTATION-VIOLATED. Severity [GCR-2]: CRITICAL / HIGH / MEDIUM.

CS-EXPECTATION-VIOLATED rows (three-field Remediation block per SHALL-F):
- CS-Expected: [cite CS-2 or CS-3 row, state expectation verbatim or by row reference]
- SE-Actual: [SE finding that contradicts the expectation]
- Delta: [exact configuration change to align SE-Actual to CS-Expected]

**TABLE_6 — Closing Summary** *(Schema Registry TABLE_6; SHALL-I requires this table; one row per TABLE_1 role)*

| Role | Tier [GCR-1] | Verdict | Open Gap IDs | Escalation Risk [GCR-7] |
|------|--------------|---------|--------------|-------------------------|

Verdict values per Schema Registry: PASS-CLEAN / PASS-WITH-GAPS / FAIL. Open Gap IDs: comma-separated
TABLE_5 row numbers or NONE. Escalation Risk [GCR-7]: one value from GCR-7 scale with inline
justification in the same cell (e.g., "HIGH — team inheritance in TABLE_4 grants org-wide read").

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
- Registry anchor — CONTEXT section declared exact labels: "Blind spot 1 — Post-incident FLS gap" (SE-2 target), "Blind spot 2 — Cumulative privilege blind spot" (SE-3 target), "Blind spot 3 — OWD-sharing-rule override gap" (SE-4 target).
- Preamble anchor — SHALL-G: Line 1 MUST be `MANUAL GAP [<exact CONTEXT label>]:`; exact = character-for-character; paraphrase fails.
- Verification — SE-2 opens with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:`? SE-3 opens with `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:`? SE-4 opens with `MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:`? Each followed by `STRUCTURED CLOSE:`? -> PASS / FAIL per section.

**CA-1.8 — CS-2/CS-3 Schema Registry registration + CS-0 acknowledgment verification:**
- Registry anchor — Schema Registry declared CS-2 and CS-3 as named schema entries with SE-updatable columns and SE-update protocol co-located.
- Preamble anchor — CS-0 acknowledgment is a PHASE 1 structural requirement.
- Verification — CS-2 in Schema Registry? CS-3 same? CS-0 present before CS-1? CS-0 cites both schema IDs by exact label? CS-0 lists SE-updatable columns? SE populated SE-updatable columns per protocol? -> PASS / FAIL

**CA-1.9 — C-16 verification (GCR-N column header citations, all tables including TABLE_6):**
- Registry anchor — GCR section declared header citation rule: every graded column header MUST include [GCR-N] suffix. GCR-1 = Tier, GCR-2 = Severity, GCR-3 = Checked?, GCR-4 = Verified?, GCR-5 = FLS Profile Configured?, GCR-6 = Gap?, GCR-7 = Escalation Risk.
- Preamble anchor — Schema Registry Step 0.1 declared all eight schemas with GCR-N citations in column headers. Missing [GCR-N] in any graded column header = auto-fail.
- Verification — TABLE_1 has `Tier [GCR-1]`? TABLE_2 has `FLS Profile Configured? [GCR-5]` and `Gap? [GCR-6]`? TABLE_3 has `Tier [GCR-1]` and `Verified? [GCR-4]`? TABLE_4 has `Checked? [GCR-3]` and `Severity [GCR-2]`? TABLE_5 has `Tier [GCR-1]` and `Severity [GCR-2]`? TABLE_6 has `Tier [GCR-1]` and `Escalation Risk [GCR-7]`? -> PASS / FAIL per table.

**CA-1.10 — C-18 verification (PPF one entry per table site):**
- Registry anchor — PROHIBITED PROSE FORMS CATALOG declared PPF-1..PPF-6, one entry per named table/schema site (TABLE_1..TABLE_6).
- Preamble anchor — SHALL-H: PPF-1 through PPF-6 required before any table. CA-1.10 verifies count and site coverage.
- Verification — PPF-1 (TABLE_1) present? PPF-2 (TABLE_2) present? PPF-3 (TABLE_3) present? PPF-4 (TABLE_4) present? PPF-5 (TABLE_5) present? PPF-6 (TABLE_6) present? Each entry has verbatim wrong form + criterion by ID? -> PASS / FAIL per entry.

**CA-1.11 — TABLE_6 schema registration and SHALL-I compliance (candidate C-19):**
- Registry anchor — Schema ID TABLE_6 declared in Step 0.1 Schema Registry with columns Role | Tier [GCR-1] | Verdict | Open Gap IDs | Escalation Risk [GCR-7]. Verdict scale: PASS-CLEAN / PASS-WITH-GAPS / FAIL. Escalation Risk [GCR-7] = GCR-7 scale + inline justification required.
- Preamble anchor — SHALL-I: TABLE_6 MUST be present at SE-5; every TABLE_1 role must have a TABLE_6 row; absent TABLE_6 = structural failure per enforcement matrix C-09 row.
- Verification — TABLE_6 present at SE-5? Uses Schema ID TABLE_6 column structure? Every TABLE_1 role has a row? Verdict values match declared scale? Open Gap IDs reference TABLE_5 rows or NONE? Escalation Risk [GCR-7] filled with declared value + inline justification? -> PASS / FAIL

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0).
[C-01 through C-05: CA-1.1..CA-1.5. SHALL-F: CA-1.6. SHALL-G: CA-1.7. CS-0 acknowledgment: CA-1.8. C-16 GCR-N headers: CA-1.9. C-18 PPF per-site: CA-1.10. TABLE_6 schema registration / C-09 / SHALL-I: CA-1.11. Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

---

## ASPIRATIONAL CRITERIA SELF-VERIFICATION (11-item, C-08..C-18)

Complete the Self-Assessment column before finalizing output. FAIL in any row requires revision.

| Criterion | Pass Condition | Fail Signal | Self-Assessment |
|-----------|----------------|-------------|-----------------|
| C-08 | At least one cross-entity cascade traced: permission on Entity A produces derived access on Entity B, mechanism named | No cross-entity effect analyzed | |
| C-09 | TABLE_6 present at SE-5 using Schema ID TABLE_6 registered columns; one row per TABLE_1 role | No TABLE_6 OR table uses non-registered column structure | |
| C-10 | Every table header includes `[CLOSES: <exact blind spot label>]` where applicable | Table headers missing CLOSES annotation | |
| C-11 | Every table has a null-case row | Table absent when no items found; null case as prose | |
| C-12 | Escalation Risk [GCR-7] column in TABLE_6; blank or "varies" = auto-fail | Blank, "varies", or outside declared GCR-7 scale | |
| C-13 | GCR block present before any table; all 7 columns registered; each entry has (a) scale, (b) auto-fail, (c) post-table verification — all three co-located in one block | Only scale declared; (b) or (c) in a separate section | |
| C-14 | At least one prohibited prose form named with verbatim wrong form + criterion violated by ID | No prohibited form named | |
| C-15 | This table present with Pass Condition / Fail Signal / Self-Assessment columns for each criterion | Flat checklist only | |
| C-16 | Every graded column header in every table (TABLE_1..TABLE_6) includes [GCR-N] citation | Any graded column header missing [GCR-N] | |
| C-17 | Exactly 11 rows covering C-08..C-18 | Fewer than 11 rows; any of C-08..C-18 absent | |
| C-18 | PPF-1..PPF-6 present, one per named table site (TABLE_1..TABLE_6); each has verbatim wrong form + criterion ID | Fewer than 6 entries OR any entry not keyed to a named table site | |

---

## V-02 — Single Axis: Signal 1 (Count-Mandate Self-Referential Lock)

**Axis:** Signal 1 single axis
**Hypothesis:** The C-17 row in the 11-row aspirational table says pass condition = "exactly 11 rows." A model can write PASS without ever counting — the count claim is asserted but not observable in the output. Adding COUNT MANDATE to the C-17 row requires the model to write `Row count: [N]` on a labeled line immediately before the Self-Assessment cell. This creates a structural audit trace: (a) if `Row count: 8` appears before `PASS`, CA can flag the contradiction without reading the full table; (b) if the Row count label is absent, that is auto-fail. The C-17 self-assessment transforms from an unverifiable assertion into a claim with a committed, observable precondition — the same principle that makes `Checked? [GCR-3] = YES` structurally stronger than a prose note saying "all vectors were checked."

---

depth: standard
confidence: standard

You are running a permissions trace signal for: {{topic}}

---

[CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS — identical to V-01: three blind spots, exact labels,
SE-2/SE-3/SE-4 closure assignments.]

---

[GRADED COLUMN REGISTRY — identical to R4 V-05: GCR-1..GCR-7. GCR-7 label reads "(used in
Closing Summary)" as in R4 V-05 (not TABLE_6 — V-02 does not target Signal 2). Header citation
rule for C-16 present. All (a)/(b)/(c) blocks co-located.]

---

[PROHIBITED PROSE FORMS CATALOG — identical to R4 V-05: PPF-1..PPF-6 where PPF-6 is keyed to
"Escalation Risk column (Closing Summary)" not TABLE_6. Six entries. SHALL-H. CA-1.10 verifies.]

---

[ROLE SEQUENCING MANDATE — identical to R4 V-05: four phases, CA-1.1 through CA-1.9 pre-assigned.
No CA-1.11. No SHALL-I.]

---

[PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE — identical to R4 V-05:
Step 0.1 declares TABLE_1..TABLE_5, CS-2, CS-3 (seven schemas; no TABLE_6).
Step 0.2 enforcement matrix has C-01..C-05 rows only; no C-09 row; no SHALL-I.
All GCR-N citations present in column headers per R4 V-05.]

---

[PHASE 1 — CS — identical to V-01: CS-0 acknowledgment for CS-2 and CS-3, then CS-1/CS-2/CS-3.]

---

[PHASE 2 — SE — identical to R4 V-05: SE-0 through SE-5 with GCR-N column headers.
SE-5 has TABLE_5 and a Closing Summary section described with GCR-N headers in prose, but NOT as
registered Schema ID TABLE_6. Exact-label SHALL-G closure blocks at SE-2/SE-3/SE-4.]

---

[PHASE 3 — CA-1 — identical to R4 V-05: CA-1.1 through CA-1.9. No CA-1.10 (PPF) because V-02
does not include PPF catalog — NOTE: this means V-02 does NOT inherit the full R4 V-05 base;
V-02 is strictly R4 V-03 mechanics (11-row table as primary enforcement) plus count-mandate.
CA-1.9 verifies GCR-N headers in TABLE_1..TABLE_5 and Closing Summary section.]

---

## ASPIRATIONAL CRITERIA SELF-VERIFICATION (11-item, C-08..C-18)

Complete the Self-Assessment column before finalizing output. FAIL in any row requires revision.

**COUNT MANDATE applies to C-17 row only.** Before filling the C-17 Self-Assessment cell:
(1) count every row in this table; (2) write `Row count: [N]` as a labeled line immediately
above the C-17 Self-Assessment cell; (3) only then write PASS (if N = 11) or FAIL (if N != 11).
Absent Row count label = auto-fail for C-17, regardless of table content.

| Criterion | Pass Condition | Fail Signal | Self-Assessment |
|-----------|----------------|-------------|-----------------|
| C-08 | At least one cross-entity cascade traced with mechanism named | No cross-entity effect analyzed | |
| C-09 | Closing Summary table at SE-5 with role + verdict + open gaps + Escalation Risk [GCR-7] per row | No summary table | |
| C-10 | Every table header includes `[CLOSES: <exact blind spot label>]` where applicable | Table headers missing CLOSES annotation | |
| C-11 | Every table has a null-case row | Null case as prose or table absent | |
| C-12 | Escalation Risk [GCR-7] column in Closing Summary; blank = auto-fail | Blank, "varies", or outside GCR-7 scale | |
| C-13 | GCR block with all 7 columns registered; each entry has (a) scale (b) auto-fail (c) post-table in one co-located block | (b) or (c) in a separate section | |
| C-14 | At least one prohibited prose form verbatim + criterion by ID | No wrong form named | |
| C-15 | This table with Pass Condition / Fail Signal / Self-Assessment columns | Flat checklist only | |
| C-16 | Every graded column header in every table includes [GCR-N] | Any graded column header missing [GCR-N] | |
| C-17 | Exactly 11 rows covering C-08..C-18. **COUNT MANDATE: write `Row count: [N]` immediately above this Self-Assessment cell before writing PASS or FAIL.** | Fewer than 11 rows OR Row count label absent OR count != 11 | Row count: |
| C-18 | PPF-1..PPF-6 present, one per named table site; each has verbatim wrong form + criterion ID | Fewer than 6 entries OR site identity absent | |

---

## V-03 — Single Axis: Signal 3 (M5 Enforcement-Density Column in Step 0.2)

**Axis:** Signal 3 single axis
**Hypothesis:** R4 V-05's triple-point enforcement for C-16/C-17/C-18 was observed retrospectively
in the R4 scorecard as an excellence signal, not declared prospectively in the skill prompt. If
enforcement density is declared in Step 0.2 as M5: Enforcement Layers — listing the structural
mechanisms per criterion — then (a) any single-layer criterion is explicitly flagged before any
table is produced, (b) CA-1.12 can verify that all flagged criteria have been resolved to at least
dual enforcement, and (c) a future rubric criterion (candidate C-21) could test whether the M5
column is present and flags are resolved. Making enforcement density a declared property turns the
quality of the enforcement structure into an auditable first-class attribute of Phase 0 itself.

---

depth: standard
confidence: standard

You are running a permissions trace signal for: {{topic}}

---

[CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS — identical to V-01.]

---

[GRADED COLUMN REGISTRY — identical to R4 V-05: GCR-1..GCR-7, GCR-7 "(used in Closing Summary)".
Header citation rule for C-16. No TABLE_6 in GCR-7 scope (V-03 does not target Signal 2).]

---

[PROHIBITED PROSE FORMS CATALOG — identical to R4 V-05: PPF-1..PPF-6 with PPF-6 keyed to
"Escalation Risk column (Closing Summary)". Six entries. SHALL-H. CA-1.10.]

---

## ROLE SEQUENCING MANDATE

[Identical to R4 V-05 with one addition: Step 0.2 now includes M5 column, and CA-1.12 is
pre-assigned for enforcement-density floor verification. CA-1.1 through CA-1.10 unchanged.
CA-1.12 added.]

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

[Identical to R4 V-05: TABLE_1..TABLE_5, CS-2, CS-3. Seven schemas. GCR-N citations in all
column headers. No TABLE_6 entry — V-03 does not target Signal 2.]

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: M1, M2, M3, M4 simultaneously active. M5 enforcement-density column active.
M5 flag rule: any criterion recorded as single-layer MUST be upgraded to dual or triple before
Phase 0 is compliant. CA-1.12 verifies no single-layer criterion remains unresolved.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row | M5: Enforcement Layers |
|-----------|-------------------|---------------------|---------------------|------------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 | quad: M1-schema + M2-section + M3-SHALL + M4-CA-row |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 | quad: M1-schema + M2-section + M3-SHALL + M4-CA-row |
| C-03 | TABLE_3 | SE-0+SE-3 | SHALL-C | CA-1.3 | quad: M1-schema + M2-section + M3-SHALL + M4-CA-row |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 | quad: M1-schema + M2-section + M3-SHALL + M4-CA-row |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 | quad: M1-schema + M2-section + M3-SHALL + M4-CA-row |
| C-13 | GCR block | Phase-0-precondition | SHALL-G | CA-1.7 | triple: upfront-declaration + SHALL-G + CA-1.7-row |
| C-14 | PPF catalog | PPF-section | SHALL-H | CA-1.10 | triple: upfront-declaration + SHALL-H + CA-1.10-row |
| C-15 | Self-audit table | Aspirational-section | — | — | single: self-audit-only **[FLAG: upgrade to dual via SHALL-J]** |
| C-16 | GCR header-rule | GCR-block | — | CA-1.9 | triple: upfront-declaration + CA-1.9-row + self-audit-C-16-row |
| C-17 | 11-row structure | Aspirational-section | — | — | single: self-audit-only **[FLAG: upgrade to dual via SHALL-K count-mandate]** |
| C-18 | PPF catalog | PPF-section | SHALL-H | CA-1.10 | triple: upfront-declaration + SHALL-H + CA-1.10-row |

**M5 flag resolutions (CA authors these alongside the flag, resolving them in Phase 0):**

- C-15 flagged (single-layer) — SHALL-J resolution: "The aspirational self-verification table MUST use exactly the three-column structure Pass Condition / Fail Signal / Self-Assessment. A flat checklist or a table with different column names auto-fails SHALL-J." This adds a SHALL obligation as second enforcement layer, making C-15 dual-layer.
- C-17 flagged (single-layer) — SHALL-K resolution: "The C-17 row in the aspirational self-verification table MUST include COUNT MANDATE: before filling Self-Assessment for C-17, write `Row count: [N]` on a labeled line immediately above that cell. Absent Row count label = auto-fail for C-17." This adds an observable precondition as second enforcement layer, making C-17 dual-layer.

CA-1.12 verifies: no criterion in M5 column remains at single-layer after flag resolution.

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A through SHALL-H: [identical to R4 V-05]
- SHALL-J (C-15 M5 flag resolution): Aspirational self-verification table MUST use Pass Condition / Fail Signal / Self-Assessment column structure. Any other column structure auto-fails.
- SHALL-K (C-17 M5 flag resolution): C-17 row MUST include COUNT MANDATE annotation. Row count: N written before Self-Assessment. Absent annotation = SHALL-K violation.

*Handing to PHASE 1 — CS.*

---

[PHASE 1 — CS — identical to V-01.]

---

[PHASE 2 — SE — identical to R4 V-05: SE-0 through SE-5 with GCR-N column headers.
SE-5 has TABLE_5 and Closing Summary described in prose with GCR-N headers but NOT registered as
Schema ID TABLE_6. Exact-label SHALL-G closure blocks at SE-2/SE-3/SE-4.]

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

[CA-1.1 through CA-1.10 identical to R4 V-05.]

**CA-1.12 — M5 enforcement-density floor verification (candidate C-21):**
- Registry anchor — Step 0.2 M5 column declared enforcement layers for C-01..C-18. FLAG rule: C-15 flagged single-layer (SHALL-J resolves), C-17 flagged single-layer (SHALL-K resolves). No other criteria flagged.
- Preamble anchor — CA Phase 0 authored M5 flag resolutions for C-15 (SHALL-J) and C-17 (SHALL-K). No criterion may remain single-layer after resolution.
- Verification — M5 column present in Step 0.2? C-15 row shows single-layer flag with SHALL-J resolution text? C-17 row shows single-layer flag with SHALL-K count-mandate resolution text? No remaining unresolved single-layer criteria? -> PASS / FAIL per flagged criterion.

**CA Format Compliance Verdict — Phase 0 citation:**
[C-01..C-05: CA-1.1..CA-1.5. SHALL-F: CA-1.6. SHALL-G: CA-1.7. CS-0: CA-1.8. C-16 GCR-N: CA-1.9. C-18 PPF: CA-1.10. M5 enforcement-density floor: CA-1.12. Overall: COMPLIANT / NON-COMPLIANT.]

---

## ASPIRATIONAL CRITERIA SELF-VERIFICATION (11-item, C-08..C-18)

Complete the Self-Assessment column before finalizing output. FAIL in any row requires revision.
C-17 COUNT MANDATE (per SHALL-K): write `Row count: [N]` immediately above C-17 Self-Assessment.

| Criterion | Pass Condition | Fail Signal | Self-Assessment |
|-----------|----------------|-------------|-----------------|
| C-08 | At least one cross-entity cascade traced with mechanism named | No cross-entity effect analyzed | |
| C-09 | Closing Summary table at SE-5 with role + verdict + open gaps + Escalation Risk [GCR-7] per row | No summary table | |
| C-10 | Every table header includes `[CLOSES: <exact blind spot label>]` where applicable | Table headers missing CLOSES annotation | |
| C-11 | Every table has a null-case row | Null case as prose or table absent | |
| C-12 | Escalation Risk [GCR-7] in Closing Summary; blank = auto-fail | Blank, "varies", or outside GCR-7 scale | |
| C-13 | GCR block with all 7 columns; each entry (a)+(b)+(c) co-located | (b) or (c) in separate section | |
| C-14 | At least one prohibited prose form verbatim + criterion by ID | No wrong form named | |
| C-15 | This table with Pass Condition / Fail Signal / Self-Assessment columns (SHALL-J) | Flat checklist or alternate column structure | |
| C-16 | Every graded column header includes [GCR-N] | Any graded column header missing [GCR-N] | |
| C-17 | Exactly 11 rows covering C-08..C-18 (SHALL-K: count-mandate applies) | Fewer than 11 rows OR Row count absent | Row count: |
| C-18 | PPF-1..PPF-6 present, one per named table site; each has verbatim wrong form + criterion ID | Fewer than 6 entries OR site identity absent | |

---

## V-04 — Combined: Signal 2 + Signal 1 (TABLE_6 Schema + Count-Mandate Lock)

**Axis:** Combined Signal 2 and Signal 1
**Hypothesis:** V-01 closes the structural gap where the Closing Summary existed but could be
schema-free. V-02 closes the gap where the 11-row completeness claim could be asserted without
an observable count. Together: every graded output site (TABLE_1..TABLE_6) has a registered
schema in Step 0.1, and the C-17 row produces a verifiable Row count: N label before any PASS
is written. These two gaps are independent (one is about output-site registration, the other is
about self-audit observability) and close without interference.

---

depth: standard
confidence: standard

You are running a permissions trace signal for: {{topic}}

---

[CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS — identical to V-01.]

[GRADED COLUMN REGISTRY — identical to V-01: GCR-1..GCR-7 with GCR-7 referencing TABLE_6.
Header citation rule for C-16. All (a)/(b)/(c) co-located.]

[PROHIBITED PROSE FORMS CATALOG — identical to V-01: PPF-1..PPF-6 with PPF-6 keyed to TABLE_6.
Six entries. SHALL-H. CA-1.10.]

[ROLE SEQUENCING MANDATE — identical to V-01: CA-1.1 through CA-1.11 pre-assigned. CA-1.9
verifies GCR-N headers including TABLE_6. CA-1.11 verifies TABLE_6 schema registration.]

[PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE — identical to V-01: Step 0.1 with
TABLE_1..TABLE_6 and all GCR-N column headers; Step 0.2 with TABLE_6 row in enforcement matrix
and SHALL-A through SHALL-I. No M5 column (V-03 mechanism not included in V-04).]

[PHASE 1 — CS — identical to V-01.]

[PHASE 2 — SE — identical to V-01: SE-0 through SE-5. SE-5 produces TABLE_5 and TABLE_6 using
Schema ID TABLE_6 registered column structure.]

[PHASE 3 — CA-1 — identical to V-01: CA-1.1 through CA-1.11. No CA-1.12.]

---

## ASPIRATIONAL CRITERIA SELF-VERIFICATION (11-item, C-08..C-18)

Complete the Self-Assessment column before finalizing output. FAIL in any row requires revision.

**COUNT MANDATE applies to C-17 row only.** Before writing C-17 Self-Assessment:
(1) count all rows in this table; (2) write `Row count: [N]` on a labeled line immediately above
the C-17 Self-Assessment cell; (3) write PASS only if N = 11. Absent Row count label = auto-fail.

| Criterion | Pass Condition | Fail Signal | Self-Assessment |
|-----------|----------------|-------------|-----------------|
| C-08 | At least one cross-entity cascade traced with mechanism named | No cross-entity effect analyzed | |
| C-09 | TABLE_6 present at SE-5 using Schema ID TABLE_6 registered columns; one row per TABLE_1 role | No TABLE_6 OR schema-free Closing Summary | |
| C-10 | Every table header includes `[CLOSES: <exact blind spot label>]` where applicable | Table headers missing CLOSES annotation | |
| C-11 | Every table has a null-case row | Null case as prose or table absent | |
| C-12 | Escalation Risk [GCR-7] in TABLE_6; blank or "varies" = auto-fail | Blank, "varies", or outside GCR-7 scale | |
| C-13 | GCR block with all 7 columns; each entry (a)+(b)+(c) co-located in one block | (b) or (c) in separate section | |
| C-14 | At least one prohibited prose form verbatim + criterion by ID | No wrong form named | |
| C-15 | This table with Pass Condition / Fail Signal / Self-Assessment columns | Flat checklist only | |
| C-16 | Every graded column header in every table (TABLE_1..TABLE_6) includes [GCR-N] | Any graded column header missing [GCR-N] | |
| C-17 | Exactly 11 rows covering C-08..C-18. **COUNT MANDATE: write `Row count: [N]` immediately above this Self-Assessment cell.** | Fewer than 11 rows OR Row count absent OR count != 11 | Row count: |
| C-18 | PPF-1..PPF-6 present, one per named table site (TABLE_1..TABLE_6); each has verbatim wrong form + criterion ID | Fewer than 6 entries OR any entry missing site identity | |

---

## V-05 — Full Integration: All Three R5 Mechanisms + 14-Row Aspirational Table

**Axis:** Full integration Signal 2 + Signal 1 + Signal 3
**Hypothesis:** V-04 closes the structural gaps for the Closing Summary (TABLE_6 registration)
and aspirational completeness (count-mandate). V-03 makes enforcement density a first-class
property in Step 0.2. V-05 combines all three. The aspirational self-audit table extends to
14 rows (C-08..C-21) where C-19, C-20, C-21 are the three candidate v5 criteria, making the
self-audit loop explicitly target all three new mechanisms: filling in C-19 Self-Assessment forces
the model to verify TABLE_6 was registered in Step 0.1; filling in C-20 forces it to verify the
count-mandate Row count: N label was written; filling in C-21 forces it to verify the M5 column
appears in Step 0.2. The count-mandate applies to C-17, which now says "14 rows" (C-08..C-21).
This means V-05 has triple-point enforcement for C-19/C-20/C-21: upfront declaration + CA
verification row + self-audit row — extending the R4 V-05 triple-point pattern to all new criteria.

---

depth: standard
confidence: standard

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

[Identical to V-01: three blind spots with exact labels. SE-2 closes Blind spot 1; SE-3 closes
Blind spot 2; SE-4 closes Blind spot 3. Exact-label two-part blocks required per SHALL-G.]

---

## GRADED COLUMN REGISTRY (CA-authored, Phase 0 precondition)

All graded columns used in this trace are declared here before any table is populated. Each entry
specifies: (a) scale with every level named, (b) auto-fail condition for blank cells, (c) post-table
verification instruction. A table that uses a column not registered here is structurally incomplete.

**Header citation rule (C-16):** Every graded column header in every table MUST include its GCR-N
identifier in brackets. Missing [GCR-N] in any graded column header auto-fails CA-1.9.

**GCR-1 — Tier** (used in TABLE_1, TABLE_3, TABLE_5, TABLE_6)
Scale: `Admin` / `Custom` / `Restricted`
Auto-fail: any cell outside these three values auto-fails TABLE verification.
Post-table verification: confirm every Tier row has one of the three declared values.

**GCR-2 — Severity** (used in TABLE_4, TABLE_5)
Scale: `CRITICAL` / `HIGH` / `MEDIUM`
Auto-fail: blank or outside scale auto-fails TABLE verification.
Post-table verification: list any non-compliant row after TABLE_5.

**GCR-3 — Checked?** (used in TABLE_4)
Scale: `YES` / `NO` (NO = auto-fail)
Auto-fail: any Checked? != YES or blank. Post-table: confirm all four rows YES.

**GCR-4 — Verified?** (used in TABLE_3)
Scale: `YES` / `NO`. Auto-fail: blank treated as NO.
Post-table verification: list any NO rows for follow-up.

**GCR-5 — FLS Profile Configured?** (used in TABLE_2)
Scale: `Configured` / `Not Configured`. Auto-fail: blank or outside scale.
Post-table verification: confirm every row has one of the two declared values.

**GCR-6 — Gap?** (used in TABLE_2)
Scale: `YES` / `NO`. Auto-fail: blank. Post-table: verify every YES has TABLE_5 cross-reference.

**GCR-7 — Escalation Risk** (used in TABLE_6)
Scale: `HIGH` / `MEDIUM` / `LOW` / `NONE`
Auto-fail: blank or "varies" or "see above" auto-fails TABLE_6 verification.
Post-table verification: list any row with blank or non-declared Escalation Risk as NON-COMPLIANT.

---

## PROHIBITED PROSE FORMS CATALOG (One entry per named table/schema site)

Exactly one entry per named table or schema in this trace. Coverage rule: PPF-1 through PPF-6
must all be present before any table is populated (SHALL-H). CA-1.10 verifies count and site identity.

**PPF-1 — TABLE_1 (Role-Operation Matrix) — null case:**
Prohibited form: "No operations are restricted for this entity." or leaving a TABLE_1 cell blank.
Criterion violated: C-11.

**PPF-2 — TABLE_2 (FLS Coverage) — null case:**
Prohibited form: "No column security profiles active on {{topic}}." written as prose above or below the table.
Criterion violated: C-11.

**PPF-3 — TABLE_3 (Record Scope by Role) — omission form:**
Prohibited form: Omitting a role from TABLE_3 with a note "inherits scope from TABLE_1."
Criterion violated: C-03.

**PPF-4 — TABLE_4 (Escalation Vector Inventory) — rule-out shortcut:**
Prohibited form: "No escalation paths identified." as the Finding cell for any vector.
Criterion violated: C-04.

**PPF-5 — TABLE_5 (Security Gap Inventory) — zero-gap omission:**
Prohibited form: TABLE_5 absent or empty, or "No security gaps found." above the table.
Criterion violated: C-04.

**PPF-6 — TABLE_6 (Closing Summary) — blank Escalation Risk:**
Prohibited form: "Varies by entity" or "See TABLE_5" or leaving Escalation Risk [GCR-7] blank.
Criterion violated: C-12.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers.

**PHASE 0 — CA:** Authors Schema Registry (Step 0.1: TABLE_1..TABLE_6 + CS-2 + CS-3, eight schemas,
GCR-N headers) and Criterion Enforcement Matrix preamble (Step 0.2: M5 column active, SHALL-A
through SHALL-K, CA-1.1 through CA-1.12 pre-assigned). Handoff to PHASE 1.

**PHASE 1 — CS:** CS-0 Registry acknowledgment first, then CS-1/CS-2/CS-3. Handoff to PHASE 2.

**PHASE 2 — SE:** SE-0 (admin inventory + TABLE_4) before SE-1. TABLE_1/TABLE_3 include Tier [GCR-1].
SE-2/SE-3/SE-4 use exact-label two-part closure blocks per SHALL-G. SE-5 produces TABLE_5 and
TABLE_6 using registered schemas. Handoff to PHASE 3.

**PHASE 3 — CA-1:** Double-anchor reaffirmation per row. CA-1.9 verifies GCR-N headers for all
tables (TABLE_1..TABLE_6). CA-1.10 verifies PPF per-site coverage (TABLE_1..TABLE_6). CA-1.11
verifies TABLE_6 schema registration and SHALL-I. CA-1.12 verifies M5 enforcement-density floor.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1 and 0.2 before any other phase begins.*

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

**All table schemas declared centrally. Blank-cell prohibition global. GCR-N citations in all
graded column headers per header citation rule. SE-update protocols for CS-2 and CS-3 co-located.**

**Schema ID: TABLE_1 — Role-Operation Matrix**
Columns: `Role | Tier [GCR-1] | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Tier [GCR-1]: Admin / Custom / Restricted. Row order: Admin first, Custom second, Restricted last.
Blank-cell rule: Granted / Denied / Conditional (inline) / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Columns: `Entity | Field | Category | FLS Profile Configured? [GCR-5] | Roles: Read | Roles: Write | Gap? [GCR-6]`
Blank-cell rule: FLS Profile Configured? [GCR-5] = Configured / Not Configured. Gap? [GCR-6] = YES / NO.

**Schema ID: TABLE_3 — Record Scope by Role**
Columns: `Role | Tier [GCR-1] | OWD Baseline | Scope Modifier | Effective Scope | Verified? [GCR-4]`
Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Columns: `Vector | Checked? [GCR-3] | Finding | Severity [GCR-2]`
Blank-cell rule: all four vectors Checked? [GCR-3] = YES. Executes at SE-0 before TABLE_1.

**Schema ID: TABLE_5 — Security Gap Inventory**
Columns: `# | Gap Type | Entity | Field or Rule | Role | Tier [GCR-1] | Severity [GCR-2] | Remediation`
Blank-cell rule: Remediation = exact object + exact location + expected post-fix state.
CS-EXPECTATION-VIOLATED three-field block: CS-Expected / SE-Actual / Delta.

**Schema ID: TABLE_6 — Closing Summary**
Columns: `Role | Tier [GCR-1] | Verdict | Open Gap IDs | Escalation Risk [GCR-7]`
Verdict: PASS-CLEAN / PASS-WITH-GAPS / FAIL. Open Gap IDs: TABLE_5 row numbers or NONE.
Escalation Risk [GCR-7]: HIGH / MEDIUM / LOW / NONE with inline justification.
Blank-cell rule: all columns filled; Verdict and Escalation Risk must use declared values.
Note: TABLE_6 executes at SE-5, after TABLE_5. One row per TABLE_1 role. Absent = SHALL-I violation.

**Schema ID: CS-2 — Sharing Rule Expectations (CS-authored)**
Columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference (TABLE_4/TABLE_5 row ID), SE Confirmation (CONFIRMED/CONTRADICTED/NOT-APPLICABLE).
Protocol: SE fills after SE-0/TABLE_4. CONTRADICTED triggers CS-EXPECTATION-VIOLATED per SHALL-F.

**Schema ID: CS-3 — Cross-Role Access Differential Expectations (CS-authored)**
Columns: `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference (TABLE_1/TABLE_3 row ID), SE Confirmation.
Protocol: SE fills after TABLE_1/TABLE_3. CONTRADICTED triggers CS-EXPECTATION-VIOLATED per SHALL-F.

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**M1, M2, M3, M4 simultaneously active. M5 enforcement-density declared.
M5 flag rule: any single-layer criterion MUST be resolved to dual before Phase 0 is compliant.
CA-1.12 verifies no unresolved single-layer flags remain.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row | M5: Enforcement Layers |
|-----------|-------------------|---------------------|---------------------|------------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 | quad: M1+M2+M3+M4 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 | quad: M1+M2+M3+M4 |
| C-03 | TABLE_3 | SE-0+SE-3 | SHALL-C | CA-1.3 | quad: M1+M2+M3+M4 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 | quad: M1+M2+M3+M4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 | quad: M1+M2+M3+M4 |
| C-09 | TABLE_6 | SE-5 | SHALL-I | CA-1.11 | triple: M1-schema+M3-SHALL+M4-CA-row |
| C-13 | GCR block | Phase-0 | SHALL-G | CA-1.7 | triple: upfront+SHALL+CA-row |
| C-14 | PPF catalog | PPF-section | SHALL-H | CA-1.10 | triple: upfront+SHALL+CA-row |
| C-15 | Self-audit table | Aspirational | SHALL-J | — | dual: SHALL-J+self-audit [resolved from single] |
| C-16 | GCR header-rule | GCR-block | — | CA-1.9 | triple: upfront+CA-row+self-audit |
| C-17 | 14-row table | Aspirational | SHALL-K | — | dual: count-mandate+self-audit [resolved from single] |
| C-18 | PPF catalog | PPF-section | SHALL-H | CA-1.10 | triple: upfront+SHALL+CA-row |
| C-19* | TABLE_6 schema | SE-5 | SHALL-I | CA-1.11 | triple: M1-schema+M3-SHALL+M4-CA-row+self-audit [quad] |
| C-20* | Count-mandate | Aspirational | SHALL-K | — | dual: SHALL-K+self-audit |
| C-21* | M5 column | Step-0.2 | — | CA-1.12 | dual: upfront-M5+CA-1.12-row |

*C-19, C-20, C-21: candidate v5 criteria. Self-audit rows added in aspirational section (C-08..C-21 = 14 rows).*

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A: Complete TABLE_1 with Tier [GCR-1]. Rows ordered by tier. Every cell Granted/Denied/Conditional/N/A.
- SHALL-B: TABLE_2 lists all PII, Financial, Audit-Compliance fields with explicit FLS status. Gap? [GCR-6] YES rows in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier [GCR-1] and Effective Scope. Ambiguous scope to TABLE_5.
- SHALL-D: TABLE_4 at SE-0 before SE-1. All four vectors, Checked? [GCR-3] = YES. Rule-outs name specific mechanism.
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap case requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field block (CS-Expected, SE-Actual, Delta). Incomplete rows MUST be reopened.
- SHALL-G: SE-2, SE-3, SE-4 each open with exact-label two-part block: Line 1 `MANUAL GAP [<exact label>]:`, Line 3 `STRUCTURED CLOSE:`. Paraphrase fails. CA-1.7 verifies.
- SHALL-H: PPF-1 through PPF-6 must be present before any table. CA-1.10 verifies.
- SHALL-I: TABLE_6 MUST be present at SE-5 using Schema ID TABLE_6 columns. Every TABLE_1 role must have a row. Absent TABLE_6 = structural failure. CA-1.11 verifies.
- SHALL-J (C-15 M5 resolution): Aspirational self-verification table MUST use Pass Condition / Fail Signal / Self-Assessment column structure. Any other structure auto-fails.
- SHALL-K (C-17 M5 resolution): The C-17 row MUST include COUNT MANDATE: write `Row count: [N]` immediately above C-17 Self-Assessment. N must equal 14 (C-08..C-21). Absent annotation = SHALL-K violation.

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

[Identical to V-01: CS-0 acknowledgment for CS-2 and CS-3 (exact Schema ID labels, SE-updatable
columns listed), then CS-1/CS-2/CS-3 using registered schemas. Handoff to PHASE 2.]

---

## PHASE 2 — SE: Security Analysis (Privilege-Tier Descent Order)

[SE-0 through SE-4 identical to V-01: admin inventory, TABLE_4, TABLE_1, TABLE_2, TABLE_3,
cross-tier escalation cross-reference. Exact-label SHALL-G closure blocks at SE-2/SE-3/SE-4.]

### SE-5 / SHALL-E + SHALL-I — Section 5: Security Gap Inventory and Closing Summary

**TABLE_5 — Security Gap Inventory** *(Schema Registry TABLE_5; Tier [GCR-1] + Severity [GCR-2])*

| # | Gap Type | Entity | Field or Rule | Role | Tier [GCR-1] | Severity [GCR-2] | Remediation |
|---|----------|--------|---------------|------|--------------|------------------|-------------|

Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED /
CS-EXPECTATION-VIOLATED. CS-EXPECTATION-VIOLATED three-field block: CS-Expected / SE-Actual / Delta.

**TABLE_6 — Closing Summary** *(Schema Registry TABLE_6; SHALL-I; one row per TABLE_1 role)*

| Role | Tier [GCR-1] | Verdict | Open Gap IDs | Escalation Risk [GCR-7] |
|------|--------------|---------|--------------|-------------------------|

Verdict: PASS-CLEAN / PASS-WITH-GAPS / FAIL. Open Gap IDs: TABLE_5 row numbers or NONE.
Escalation Risk [GCR-7]: one declared value with inline justification.

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

*CA returns. Each CA-1 row: Registry anchor (distinct labeled element) + Preamble anchor
(distinct labeled element) + Verification line. Inline concatenation fails.*

**CA-1.1 — C-01:** Registry: TABLE_1 Tier [GCR-1] declared. Preamble: TABLE_1/SE-1/SHALL-A/CA-1.1.
Verification: TABLE_1 present? Tier [GCR-1]? Rows by tier? All cells filled? -> PASS / FAIL

**CA-1.2 — C-02:** Registry: TABLE_2 FLS Profile Configured? [GCR-5] and Gap? [GCR-6] declared.
Preamble: TABLE_2/SE-2/SHALL-B/CA-1.2.
Verification: TABLE_2 present? All sensitive fields? FLS status explicit? Gap? [GCR-6] YES in TABLE_5? -> PASS / FAIL

**CA-1.3 — C-03:** Registry: TABLE_3 Tier [GCR-1] + Verified? [GCR-4] declared.
Preamble: TABLE_3/SE-0+SE-3/SHALL-C/CA-1.3.
Verification: Every TABLE_1 role in TABLE_3? Tier [GCR-1]? Effective Scope? Verified? [GCR-4]? -> PASS / FAIL

**CA-1.4 — C-04:** Registry: TABLE_4 Checked? [GCR-3] + Severity [GCR-2]; all four vectors.
Preamble: TABLE_4/SE-0/SHALL-D/CA-1.4.
Verification: TABLE_4 at SE-0? All four vectors? Checked? = YES? Findings or specific rule-outs? -> PASS / FAIL

**CA-1.5 — C-05:** Registry: TABLE_5 Tier [GCR-1] + Severity [GCR-2] declared.
Preamble: TABLE_5/SE-5/SHALL-E/CA-1.5.
Verification: TABLE_5 present? Named gap? Tier [GCR-1]? Severity [GCR-2]? Remediations exact? -> PASS / FAIL

**CA-1.6 — SHALL-F:** Registry: TABLE_5 CS-EXPECTATION-VIOLATED three-field block required.
Preamble: SHALL-F — three-field mandatory; incomplete rows reopened.
Verification: CS-Expected populated? SE-Actual populated? Delta with exact configuration change? -> PASS / FAIL per row.

**CA-1.7 — SHALL-G:** Registry: CONTEXT exact labels declared.
Preamble: SHALL-G — Line 1 `MANUAL GAP [<exact label>]:`; character-for-character; paraphrase fails.
Verification: SE-2 opens with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:`? SE-3 with `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:`? SE-4 with `MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:`? Each followed by `STRUCTURED CLOSE:`? -> PASS / FAIL per section.

**CA-1.8 — CS-0 acknowledgment:** Registry: CS-2 and CS-3 as named schema entries with SE-update protocols.
Preamble: CS-0 is a PHASE 1 structural requirement.
Verification: CS-2 in Registry? CS-3 same? CS-0 before CS-1? CS-0 cites both schema IDs exactly? SE-updatable columns listed? SE populated them? -> PASS / FAIL

**CA-1.9 — C-16 (GCR-N header citations, TABLE_1..TABLE_6):**
Registry: GCR header citation rule; GCR-1..GCR-7 declared. Step 0.1 all 8 schemas have GCR-N in graded column headers.
Preamble: Missing [GCR-N] = auto-fail.
Verification: TABLE_1 `Tier [GCR-1]`? TABLE_2 `FLS Profile Configured? [GCR-5]` + `Gap? [GCR-6]`? TABLE_3 `Tier [GCR-1]` + `Verified? [GCR-4]`? TABLE_4 `Checked? [GCR-3]` + `Severity [GCR-2]`? TABLE_5 `Tier [GCR-1]` + `Severity [GCR-2]`? TABLE_6 `Tier [GCR-1]` + `Escalation Risk [GCR-7]`? -> PASS / FAIL per table.

**CA-1.10 — C-18 (PPF one entry per table site):**
Registry: PPF-1..PPF-6 declared; coverage rule requires all 6 with distinct site identity.
Preamble: SHALL-H — PPF-1..PPF-6 before any table.
Verification: PPF-1 (TABLE_1)? PPF-2 (TABLE_2)? PPF-3 (TABLE_3)? PPF-4 (TABLE_4)? PPF-5 (TABLE_5)? PPF-6 (TABLE_6)? Each has verbatim wrong form + criterion ID? -> PASS / FAIL per entry.

**CA-1.11 — C-19 (TABLE_6 schema registration, candidate):**
Registry: Schema ID TABLE_6 declared in Step 0.1 with Role | Tier [GCR-1] | Verdict | Open Gap IDs | Escalation Risk [GCR-7]. Verdict scale and Escalation Risk [GCR-7] declared.
Preamble: SHALL-I — TABLE_6 structural; C-09 row in enforcement matrix (M1=TABLE_6, M3=SHALL-I, M4=CA-1.11).
Verification: TABLE_6 present at SE-5? Uses Schema ID TABLE_6 columns exactly? Every TABLE_1 role has a row? Verdict = declared value? Open Gap IDs = TABLE_5 row numbers or NONE? Escalation Risk [GCR-7] = declared value + inline justification? -> PASS / FAIL

**CA-1.12 — C-21 (M5 enforcement-density floor, candidate):**
Registry: Step 0.2 M5 column declared for all criteria including C-19*/C-20*/C-21* candidate rows. C-15 and C-17 flagged single-layer; SHALL-J and SHALL-K declared as resolutions.
Preamble: M5 flag rule — no single-layer criterion unresolved; CA-1.12 verifies.
Verification: M5 column present in Step 0.2? C-15 row shows SHALL-J resolution (dual)? C-17 row shows SHALL-K count-mandate resolution (dual)? All other criteria show declared enforcement layers? No unresolved single-layer flags? -> PASS / FAIL per flagged criterion.

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1), CA-authored preamble (Step 0.2), Phase 0.
[C-01..C-05: CA-1.1..CA-1.5. SHALL-F: CA-1.6. SHALL-G: CA-1.7. CS-0: CA-1.8. C-16 GCR-N: CA-1.9. C-18 PPF: CA-1.10. C-19/TABLE_6 schema: CA-1.11. C-21/M5 enforcement-density: CA-1.12. Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

---

## ASPIRATIONAL CRITERIA SELF-VERIFICATION (14-item, C-08..C-21)

Complete the Self-Assessment column before finalizing output. FAIL in any row requires revision.

**COUNT MANDATE applies to C-17 row only (SHALL-K).** Before writing C-17 Self-Assessment:
(1) count every row in this table; (2) write `Row count: [N]` on a labeled line immediately above
the C-17 Self-Assessment cell; (3) write PASS only if N = 14. Absent Row count label = auto-fail.

| Criterion | Pass Condition | Fail Signal | Self-Assessment |
|-----------|----------------|-------------|-----------------|
| C-08 | At least one cross-entity cascade traced: permission on Entity A produces derived access on Entity B, mechanism named | No cross-entity effect analyzed | |
| C-09 | TABLE_6 present at SE-5 using Schema ID TABLE_6 registered columns; one row per TABLE_1 role | No TABLE_6 OR schema-free Closing Summary OR columns differ from Step 0.1 | |
| C-10 | Every table header includes `[CLOSES: <exact blind spot label>]` where applicable | Table headers missing CLOSES annotation | |
| C-11 | Every table has a null-case row | Table absent when no items found; null case as prose | |
| C-12 | Escalation Risk [GCR-7] in TABLE_6; blank or "varies" = auto-fail | Blank, "varies", or outside GCR-7 scale | |
| C-13 | GCR block with all 7 registered; each entry (a) scale (b) auto-fail (c) post-table all co-located | (b) or (c) in separate section | |
| C-14 | At least one prohibited prose form verbatim + criterion by ID | No wrong form named | |
| C-15 | This table with Pass Condition / Fail Signal / Self-Assessment columns (SHALL-J) | Flat checklist or alternate column structure | |
| C-16 | Every graded column header in TABLE_1..TABLE_6 includes [GCR-N] | Any graded column header missing [GCR-N] | |
| C-17 | Exactly 14 rows covering C-08..C-21. COUNT MANDATE (SHALL-K): write `Row count: [N]` immediately above this Self-Assessment. N must equal 14. | Fewer than 14 rows OR Row count absent OR count != 14 | Row count: |
| C-18 | PPF-1..PPF-6 present, one per named table site (TABLE_1..TABLE_6); each has verbatim wrong form + criterion ID | Fewer than 6 entries OR any entry missing site identity | |
| C-19 | Schema ID TABLE_6 declared in Step 0.1 Registry with Role / Tier [GCR-1] / Verdict / Open Gap IDs / Escalation Risk [GCR-7]; CA-1.11 verification row present | Closing Summary present but NOT registered as Schema ID TABLE_6 in Step 0.1 | |
| C-20 | C-17 row in this table includes COUNT MANDATE annotation with `Row count: [N]` label; N reflects actual row count before PASS is written | C-17 row has no COUNT MANDATE annotation OR Row count label absent | |
| C-21 | M5: Enforcement Layers column present in Step 0.2 Criterion Enforcement Matrix; C-15 and C-17 flagged single-layer with resolutions (SHALL-J / SHALL-K) declared; CA-1.12 verification row present | M5 column absent OR single-layer flag present but unresolved | |
