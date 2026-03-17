# trace-permissions — Quest Variate Round 6 (Rubric v5, R5 Excellence Signals)

**Date:** 2026-03-16
**Rubric:** v5 (C-01..C-21, N=14 aspirational)
**Base:** R5 V-05 mechanics retained across all R6 variations (TABLE_6 schema registered,
GCR-N headers in all tables, PPF-1..PPF-6, 14-row aspirational table covering C-08..C-21,
M5 enforcement-density column in Step 0.2, COUNT MANDATE on C-17, CA-1.1..CA-1.12).

**Target patterns:** R5 excellence signals A/B/C captured in C-19/C-20/C-21. R6 targets
three latent weaknesses in the V-05 prompt not yet exposed by v5 rubric scoring:

- **Latent 1 — Count-mandate cosmetic compliance.** The COUNT MANDATE says write
  `Row count: [N]`. A model can copy the template literally without substituting the
  integer. The label is present; the count is not. No v5 criterion catches unfilled
  template text as a distinct failure mode.

- **Latent 2 — No enforcement matrix rows for C-19/C-20/C-21.** Step 0.2 covers
  C-01..C-09 with M1-M5 enforcement. C-19/C-20/C-21 appear only in the self-audit
  table — no SHALL obligations of their own, no dedicated CA verification rows.
  Single-layer enforcement only.

- **Latent 3 — Self-Assessment cells permit unobservable assertion.** The C-21
  self-referential loop forces Self-Assessment cells for C-19/C-20/C-21 to be filled.
  But "PASS" without citing the mechanism is assertion without evidence — structurally
  identical to the problem COUNT MANDATE was designed to solve for C-17.

---

## Round 6 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Count-mandate value fills: require integer, not template `[N]` | Cosmetic compliance: model writes `Row count: [N]` without substituting the count. Requiring `Row count: [integer]` closes the gap between structural presence of the label and substantive observability of the count claim |
| V-02 | C-19/C-20/C-21 in Step 0.2 enforcement matrix with M5 entries | New criteria exist only in self-audit table (single-layer). Adding matrix rows gives each criterion M1-M5 scaffolding; C-21 surfaces as single-layer, triggering SHALL-L flag — applying the M5 mechanism recursively |
| V-03 | SHALL-L: mechanism-verification phrases in C-19/C-20/C-21 Self-Assessment cells | "PASS" without mechanism citation is assertion without evidence. SHALL-L requires observable phrases: C-19 cites Row count integer; C-20 cites M5 column counts (K criteria, F flags); C-21 cites actual row count and coverage |
| V-04 | Combined: V-01 count-value fills + V-02 enforcement matrix rows | Structurally independent axes — V-01 is self-audit table property; V-02 is Phase 0 CA property. Combined addresses both the count-placeholder gap and the enforcement-absence gap |
| V-05 | Full integration: V-01 + V-02 + V-03 + CA-1.13 for C-21 loop verification | All three axes plus CA-1.13 double-anchor verification of the self-referential loop: verifies C-19/C-20/C-21 rows present, mechanism phrases filled, C-17 Row count is integer matching actual row count |

---

## V-01 — Single Axis: Count-Mandate Value Fills

**Axis:** Count-mandate value fills (Latent 1 single axis)
**Hypothesis:** The COUNT MANDATE says write `Row count: [N]`. The template `[N]` is an
instruction — replace it with the actual integer count. A model can satisfy this by copying
`Row count: [N]` verbatim without counting. Adding an explicit requirement that `[N]` must be
replaced with the actual integer (and that the literal template text `[N]` is auto-fail
equivalent to absent label) closes the gap between formal compliance and substantive
observability. Same principle as `Checked? [GCR-3] = YES` vs a prose note saying "I checked
the vectors" — the committed value must be observable in the output, not merely described.

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

Manual security reviews of Dataverse environments routinely miss three failure scenarios that
this trace is designed to surface:

**Blind spot 1 — Post-incident FLS gap.** Column security profiles are rarely audited
proactively. Sensitive fields — credit limits, compensation data, SSNs, contact identifiers —
remain readable and writable by any role unless a column security profile explicitly restricts
them. The security roles UI does not surface which fields lack column security profiles; gaps
are discovered after data exposure, not before.

**Blind spot 2 — Cumulative privilege blind spot.** A user holding a BU-scoped security role
who also belongs to an owner team whose team role grants org-wide access has effective org-wide
access. No single Dataverse UI view surfaces the combined effective access produced by role +
team + OWD combination. Spot-checking individual roles misses cross-role accumulation through
team membership.

**Blind spot 3 — OWD-sharing-rule override gap.** Administrators check OWD settings
entity-by-entity without evaluating the sharing rules that silently override those baselines.
A Private OWD on Case combined with a Power Automate-triggered sharing rule grants effective
org-wide read to users who satisfy the trigger condition — including low-trust service accounts
and CS users not intended to have broad case access.

This trace closes all three blind spots: SE-2 closes Blind spot 1; SE-3 closes Blind spot 2;
SE-4 closes Blind spot 3. Closure notes are exact-label two-part blocks co-located at each SE
sub-section opening, carrying the exact blind-spot label from this CONTEXT section.

---

## GRADED COLUMN REGISTRY (CA-authored, Phase 0 precondition)

All graded columns used in this trace are declared here before any table is populated. Each
entry specifies: (a) scale with every level named, (b) auto-fail condition for blank cells,
(c) post-table verification instruction. A table that uses a column not registered here is
structurally incomplete.

**Header citation rule (C-16):** Every graded column header in every table MUST include its
GCR-N identifier in brackets — e.g., `Tier [GCR-1]`, `Severity [GCR-2]`. A header that omits
the `[GCR-N]` suffix on a graded column auto-fails CA-1.9 verification.

**GCR-1 — Tier** (used in TABLE_1, TABLE_3, TABLE_5, TABLE_6)
Scale: `Admin` / `Custom` / `Restricted`
Auto-fail: any cell not one of these three values is a blank-equivalent and auto-fails TABLE
verification.
Post-table verification: after each table with a Tier column, confirm every row has one of the
three declared values.

**GCR-2 — Severity** (used in TABLE_4, TABLE_5)
Scale: `CRITICAL` (exploitable with no additional steps) / `HIGH` (exploitable with one
intermediate step) / `MEDIUM` (limited blast radius or requires specific conditions)
Auto-fail: any Severity cell blank or outside CRITICAL / HIGH / MEDIUM auto-fails TABLE
verification.
Post-table verification: after TABLE_5, list any row with blank or non-declared Severity as
NON-COMPLIANT.

**GCR-3 — Checked?** (used in TABLE_4)
Scale: `YES` (vector examined, finding or specific rule-out written) / `NO` (not checked —
auto-fail)
Auto-fail: Checked? = NO or blank auto-fails TABLE_4 verification. All four vectors must be YES.
Post-table verification: after TABLE_4, confirm all four rows have Checked? = YES.

**GCR-4 — Verified?** (used in TABLE_3)
Scale: `YES` (scope confirmed against configuration) / `NO` (scope inferred, not confirmed —
flag as gap)
Auto-fail: blank Verified? cell treated as NO and auto-fails the row.
Post-table verification: after TABLE_3, list any NO rows as unconfirmed scope entries.

**GCR-5 — FLS Profile Configured?** (used in TABLE_2)
Scale: `Configured` (column security profile exists and restricts this field) / `Not Configured`
(no column security profile; field accessible to any role with entity access)
Auto-fail: blank or any value other than `Configured` / `Not Configured` auto-fails TABLE_2
verification.
Post-table verification: after TABLE_2, confirm every row has one of the two declared values.

**GCR-6 — Gap?** (used in TABLE_2)
Scale: `YES` (field has missing or insufficient protection — forward to TABLE_5) / `NO` (field
adequately protected)
Auto-fail: blank Gap? cell auto-fails the row. Every Gap? = YES row must have a TABLE_5 entry.
Post-table verification: after TABLE_2, verify every YES row has a TABLE_5 cross-reference.

**GCR-7 — Escalation Risk** (used in TABLE_6)
Scale: `HIGH` (role combination or sharing rule produces access materially exceeding job
function) / `MEDIUM` (access exceeds job function in limited scope) / `LOW` (minor excess
access; unlikely to be exploited) / `NONE` (access appropriate to job function; no escalation
vector confirmed)
Auto-fail: blank Escalation Risk cell auto-fails TABLE_6 verification. "Varies" or "see above"
is blank-equivalent.
Post-table verification: after TABLE_6, list any row with blank or non-declared Escalation Risk
as NON-COMPLIANT.

---

## PROHIBITED PROSE FORMS CATALOG (One entry per named table/schema site)

Exactly one entry per named table or schema in this trace. Each entry identifies the wrong form
verbatim and the criterion it violates by ID. Using a prohibited form at the named site is a
structural failure detectable by CA-1.10. Coverage rule: PPF-1 through PPF-6 must all be
present.

**PPF-1 — TABLE_1 (Role-Operation Matrix) — null case:**
Prohibited form: "No operations are restricted for this entity." or leaving a TABLE_1 cell
blank.
Criterion violated: C-11 — null case must be a data row with all cells explicitly filled.

**PPF-2 — TABLE_2 (FLS Coverage) — null case:**
Prohibited form: Writing "No column security profiles active on {{topic}}." as prose above or
below the table.
Criterion violated: C-11 — null case must appear as an explicit TABLE_2 row with FLS Profile
Configured? [GCR-5] = Not Configured.

**PPF-3 — TABLE_3 (Record Scope by Role) — omission form:**
Prohibited form: Omitting a role from TABLE_3 with a note "inherits scope from TABLE_1" or
"default OWD applies."
Criterion violated: C-03 — every TABLE_1 role must appear in TABLE_3 with Effective Scope
explicitly stated.

**PPF-4 — TABLE_4 (Escalation Vector Inventory) — rule-out shortcut:**
Prohibited form: Writing "No escalation paths identified." as the Finding cell for any vector.
Criterion violated: C-04 — rule-out requires naming the specific mechanism: "Checked [vector]:
no path found because [specific control] prevents [escalation mechanism]."

**PPF-5 — TABLE_5 (Security Gap Inventory) — zero-gap omission:**
Prohibited form: Leaving TABLE_5 absent or empty, or writing "No security gaps found." above
the table.
Criterion violated: C-04 — zero-gap case requires explicit evidence rows with Remediation
citing a specific control.

**PPF-6 — TABLE_6 (Closing Summary) — blank Escalation Risk cell:**
Prohibited form: Writing "Varies by entity" or "See TABLE_5 for details" or leaving the
Escalation Risk [GCR-7] cell blank in any TABLE_6 row.
Criterion violated: C-12 — Escalation Risk must be one value from GCR-7 scale with an inline
justification in the same cell.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase
completes fully before the next begins.

**PHASE 0 — CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1: TABLE_1 through TABLE_6 with GCR-N
citations; CS-2 and CS-3 — eight schemas total) and the Criterion Enforcement Matrix preamble
(Step 0.2: SHALL-A through SHALL-K, M5 column active, M4 row IDs CA-1.1 through CA-1.12
pre-assigned). CA issues handoff to PHASE 1.

**PHASE 1 — CS (Customer Success):**
Executes second. Opens with CS-0 sub-section (Schema Registry acknowledgment: CS echoes
Registry schema IDs for CS-2 and CS-3 by exact Schema ID label, lists SE-updatable columns,
and confirms the expectation format before authoring any expectation rows). Then produces
CS-1, CS-2, CS-3 using Registry schemas. CS does not fill TABLE_1-6. CS issues handoff to
PHASE 2.

**PHASE 2 — SE (Security Engineer / Dataverse Security Expert):**
Executes third in privilege-tier descent order. SE-0 (admin-tier inventory and TABLE_4
escalation vectors) runs before SE-1 (role-operation matrix). TABLE_1 and TABLE_3 include
Tier [GCR-1] column. SE-2, SE-3, SE-4 each open with two-part exact-label closure blocks per
SHALL-G. SE-5 produces TABLE_5 and TABLE_6 using registered Schema IDs. Issues handoff to
PHASE 3.

**PHASE 3 — CA-1 (CA Verification Pass):**
CA returns. Each CA-1 row performs double-anchor reaffirmation: Registry anchor and Preamble
anchor as structurally distinct labeled elements. Verification line follows. Inline
concatenation fails. CA-1.8 verifies CS-0 acknowledgment precedes CS-1. CA-1.9 verifies
GCR-N header citations in every table including TABLE_6. CA-1.10 verifies PPF per-site
coverage. CA-1.11 verifies TABLE_6 schema registration and SHALL-I compliance. CA-1.12
verifies M5 enforcement-density floor and count-mandate value fill.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1 and 0.2 before any other phase begins.*

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

**All table schemas declared centrally by CA. Blank-cell prohibition is global. SE-update
protocols for CS-2 and CS-3 declared co-located with schema entry. Every graded column header
includes its GCR-N citation per header citation rule above.**

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Tier [GCR-1] | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Tier [GCR-1] values: Admin / Custom / Restricted. Rows ordered: Admin first, Custom second,
Restricted last. Blank-cell rule: all cells Granted / Denied / Conditional (condition inline) /
N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? [GCR-5] | Roles: Read | Roles: Write | Gap? [GCR-6]`
Blank-cell rule: FLS Profile Configured? [GCR-5] = Configured / Not Configured (never blank).
Gap? [GCR-6] = YES / NO.

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | Tier [GCR-1] | OWD Baseline | Scope Modifier | Effective Scope | Verified? [GCR-4]`
Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU / Org-wide / Team-scoped /
Sharing-[rule name]. Verified? [GCR-4] = YES / NO.

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? [GCR-3] | Finding | Severity [GCR-2]`
Blank-cell rule: all four vectors, Checked? [GCR-3] = YES. Note: TABLE_4 executes at SE-0
before SE-1.

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Tier [GCR-1] | Severity [GCR-2] | Remediation`
Blank-cell rule: Remediation = exact object + exact location + expected post-fix state.
CS-EXPECTATION-VIOLATED Remediation (three-field block):
- CS-Expected: cite CS-2 or CS-3 row, state expectation verbatim or by row reference.
- SE-Actual: SE finding that contradicts the expectation.
- Delta: exact configuration change to align SE-Actual to CS-Expected.

**Schema ID: TABLE_6 — Closing Summary**
Declared columns: `Role | Tier [GCR-1] | Verdict | Open Gap IDs | Escalation Risk [GCR-7]`
Verdict values: PASS-CLEAN / PASS-WITH-GAPS / FAIL. Open Gap IDs: TABLE_5 row numbers or NONE.
Escalation Risk [GCR-7]: one of HIGH / MEDIUM / LOW / NONE with inline justification in same
cell. Blank-cell rule: no column may be blank. TABLE_6 executes at SE-5, after TABLE_5. One
row per TABLE_1 role required per SHALL-I. Absent TABLE_6 = structural failure.

**Schema ID: CS-2 — Sharing Rule Expectations**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference; SE Confirmation (CONFIRMED / CONTRADICTED /
NOT-APPLICABLE). SE populates after SE-0/TABLE_4 analysis. CONTRADICTED triggers
CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

**Schema ID: CS-3 — Cross-Role Access Differential Expectations**
Declared columns: `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference; SE Confirmation. SE populates after TABLE_1/TABLE_3
analysis. CONTRADICTED triggers CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: M1, M2, M3, M4 simultaneously active. M5 enforcement-density column active.
M5 flag rule: any criterion recorded as single-layer MUST be upgraded to dual or triple before
Phase 0 is compliant. CA-1.12 verifies no single-layer criterion remains unresolved.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row | M5: Enforcement Layers |
|-----------|-------------------|---------------------|---------------------|------------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 | quad: M1+M2+M3+M4 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 | quad: M1+M2+M3+M4 |
| C-03 | TABLE_3 | SE-0+SE-3 | SHALL-C | CA-1.3 | quad: M1+M2+M3+M4 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 | quad: M1+M2+M3+M4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 | quad: M1+M2+M3+M4 |
| C-09 | TABLE_6 | SE-5 | SHALL-I | CA-1.11 | quad: M1+M2+M3+M4 |
| C-13 | GCR block | Phase-0-precondition | SHALL-G | CA-1.7 | triple: upfront+SHALL-G+CA-1.7 |
| C-14 | PPF catalog | PPF-section | SHALL-H | CA-1.10 | triple: upfront+SHALL-H+CA-1.10 |
| C-15 | self-audit table | aspirational-section | SHALL-J | — | dual: SHALL-J+self-audit |
| C-16 | GCR header-rule | GCR-block | — | CA-1.9 | triple: upfront+CA-1.9+self-audit-C-16 |
| C-17 | 14-row structure | aspirational-section | SHALL-K | — | dual: SHALL-K(count-value)+self-audit |
| C-18 | PPF catalog | PPF-section | SHALL-H | CA-1.10 | triple: upfront+SHALL-H+CA-1.10 |

**M5 flag resolutions:**

- C-15 flagged (single-layer) — SHALL-J resolution: "The aspirational self-verification table
  MUST use exactly the three-column structure Pass Condition / Fail Signal / Self-Assessment.
  A flat checklist or different column names auto-fails SHALL-J."
- C-17 flagged (single-layer) — SHALL-K resolution (COUNT VALUE MANDATE): "The C-17 row MUST
  include COUNT VALUE MANDATE. Before filling the C-17 Self-Assessment cell: (1) count every
  row in this table; (2) write `Row count: [actual integer]` immediately above the
  Self-Assessment cell — where [actual integer] is the number you counted, NOT the literal
  template text `[N]`; (3) only then write PASS (if count = 14) or FAIL (if count != 14).
  Writing `Row count: [N]` without substituting the count is cosmetically compliant but
  structurally empty — auto-fail equivalent to absent Row count label.
  Correct form: `Row count: 14`."

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A: Complete TABLE_1 with Tier [GCR-1] column. Every cell Granted/Denied/Conditional/N/A.
  Rows ordered by tier.
- SHALL-B: TABLE_2 lists all PII, Financial, and Audit-Compliance fields with explicit FLS
  status. Null case explicit. Gap? [GCR-6] YES rows in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier [GCR-1] and Effective Scope filled.
- SHALL-D: TABLE_4 at SE-0 (before SE-1), all four vectors, Checked? [GCR-3] = YES. Rule-outs
  name specific mechanism and reason.
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap case requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field Remediation block
  (CS-Expected, SE-Actual, Delta). CA-1.6 verifies.
- SHALL-G: At SE-2, SE-3, and SE-4 openings: two-part labeled block — Line 1:
  `MANUAL GAP [<exact CONTEXT label>]:`; Line 2: what manual audits miss; Line 3:
  `STRUCTURED CLOSE:`; Line 4: which table/mechanism closes it. Paraphrase fails.
  CA-1.7 verifies exact label carry-through.
- SHALL-H: PPF-1 through PPF-6 must all be present before any table is populated.
  CA-1.10 verifies count and site coverage.
- SHALL-I: TABLE_6 MUST be present at SE-5 using Schema ID TABLE_6 column structure. Absent
  TABLE_6 = structural failure. Every TABLE_1 role must have a TABLE_6 row. CA-1.11 verifies.
- SHALL-J (C-15 M5 flag resolution): Self-verification table MUST use Pass Condition / Fail
  Signal / Self-Assessment column structure.
- SHALL-K (C-17 M5 flag resolution — COUNT VALUE MANDATE): C-17 row MUST include count-value
  annotation. `Row count: [actual integer]` written before Self-Assessment. Template `[N]`
  unfilled = auto-fail. Correct form: `Row count: 14`.

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

*CS opens with CS-0 Registry acknowledgment before authoring any expectation content.*

### CS-0 — Schema Registry Acknowledgment (CS-authored, Phase 1)

**Registry acknowledgment for CS-2:**
Schema ID: CS-2 — Sharing Rule Expectations. SE-updatable columns: SE Cross-Reference, SE
Confirmation. SE-update protocol acknowledged: SE populates after SE-0/TABLE_4 analysis.
Expectation format confirmed: Rule Name | Trigger | Expected Access Granted | Intended for CS
Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation. SE-updatable columns left
blank; SE fills after SE-0.

**Registry acknowledgment for CS-3:**
Schema ID: CS-3 — Cross-Role Access Differential Expectations. SE-updatable columns: SE
Cross-Reference, SE Confirmation. SE-update protocol acknowledged: SE populates after
SE-1/SE-3 analysis. Expectation format confirmed: Entity | Operation | CS Role Expected Access
| Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference
| SE Confirmation. SE-updatable columns left blank; SE fills after SE-1/SE-3.

### CS-1 — Expected Customer Service Access Baseline

For each entity in scope: (a) which CRUD operations the CS role is expected to perform; (b)
the expected record scope; (c) which sensitive fields CS needs read or write access to and why.
Identify any configuration that may open access beyond job requirements.

**CS-2 — Sharing rule expectations** *(Schema Registry CS-2; SE-updatable columns blank)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

For each Potential Overreach? YES: name the access path and the most likely over-reached role.

**CS-3 — Cross-role access differential** *(Schema Registry CS-3; SE-updatable columns blank)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

State at minimum one entity and one operation where CS has less access than the Comparison
Role.

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

**TABLE_1 — Role-Operation Matrix** *(Schema Registry TABLE_1 with Tier [GCR-1] column)*

| Role | Tier [GCR-1] | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|--------------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Rows ordered: Admin tier first, Custom second, Restricted last. After TABLE_1: populate CS-3
SE Cross-Reference and SE Confirmation.

**Cross-role differential analysis:** Compare the CS role against at least one Admin-tier and
one Custom-tier role. Cite SE-0 TABLE_4 data for differentials attributable to admin-tier
escalation vectors.

### SE-2 / SHALL-B — Section 2: Field-Level Security Coverage

MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:
Column security profiles are not auditable from the security roles UI; administrators discover
missing FLS only after a data exposure event.

STRUCTURED CLOSE:
TABLE_2 enumerates every sensitive field in scope with explicit FLS status (Configured / Not
Configured), surfacing pre-event what the security roles UI conceals. Not Configured sensitive
fields forwarded to TABLE_5 as MISSING-FLS gaps.

**TABLE_2 — FLS Coverage** *(Schema Registry TABLE_2)*

| Entity | Field | Category | FLS Profile Configured? [GCR-5] | Roles: Read | Roles: Write | Gap? [GCR-6] |
|--------|-------|----------|---------------------------------|-------------|--------------|--------------|

Categories: PII / Financial / Audit-Compliance / Other-Sensitive. Null case: "No column
security profiles active on {{topic}}. Sensitive fields identified: [list]. All in TABLE_5
as MISSING-FLS." Note: System Administrator bypasses column security profiles (SE-0 confirmed).

**Defense-in-depth layer check:** Identify the enforcement layer for at least one sensitive
field. For Admin-tier roles, note the SE-0 bypass finding.

### SE-3 / SHALL-C — Section 3: Record Access Scope

MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access from role + team + OWD;
spot-checking roles individually misses cross-role accumulation through team inheritance.

STRUCTURED CLOSE:
TABLE_3 maps the effective scope for every role by Tier [GCR-1], recording OWD baseline,
scope modifier, and resulting effective scope as a single traceable row.

**TABLE_3 — Record Scope by Role** *(Schema Registry TABLE_3 with Tier [GCR-1] column)*

| Role | Tier [GCR-1] | OWD Baseline | Scope Modifier | Effective Scope | Verified? [GCR-4] |
|------|--------------|--------------|----------------|-----------------|-------------------|

Every TABLE_1 role MUST appear, ordered by Tier [GCR-1]. Note roles where effective scope
exceeds role-only scope due to team membership; flag CS-EXPECTATION-VIOLATED in TABLE_5 if
CS-3 expected the unexpanded scope. After TABLE_3: update CS-3 SE Confirmation.

### SE-4 / SHALL-D — Section 4: Privilege Escalation Cross-Reference

MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing sharing rules
that silently override them; a Private OWD combined with an active sharing rule can grant
effective org-wide access without appearing in any security roles UI view.

STRUCTURED CLOSE:
TABLE_4 (filled at SE-0) evaluated all four escalation vectors with sharing rules
cross-referenced against OWD settings. This section adds cross-tier differential summary
citing SE-0 data: for the most privileged Admin-tier role and most restricted Restricted-tier
role, identify the enforcement layer where access diverges, citing the SE-0 TABLE_4 row ID.
State whether divergence is expected and what sharing-rule interaction was confirmed or ruled
out.

### SE-5 / SHALL-E + SHALL-I — Section 5: Security Gap Inventory and Closing Summary

**TABLE_5 — Security Gap Inventory** *(Schema Registry TABLE_5 with Tier [GCR-1] and
Severity [GCR-2])*

| # | Gap Type | Entity | Field or Rule | Role | Tier [GCR-1] | Severity [GCR-2] | Remediation |
|---|----------|--------|---------------|------|--------------|------------------|-------------|

Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED /
CS-EXPECTATION-VIOLATED. Severity [GCR-2]: CRITICAL / HIGH / MEDIUM.

CS-EXPECTATION-VIOLATED rows (three-field Remediation block per SHALL-F):
- CS-Expected: [cite CS-2 or CS-3 row, state expectation verbatim]
- SE-Actual: [SE finding that contradicts the expectation]
- Delta: [exact configuration change to align SE-Actual to CS-Expected]

**TABLE_6 — Closing Summary** *(Schema Registry TABLE_6; SHALL-I requires; one row per
TABLE_1 role)*

| Role | Tier [GCR-1] | Verdict | Open Gap IDs | Escalation Risk [GCR-7] |
|------|--------------|---------|--------------|-------------------------|

Verdict values: PASS-CLEAN / PASS-WITH-GAPS / FAIL. Open Gap IDs: TABLE_5 row numbers or
NONE. Escalation Risk [GCR-7]: one value from GCR-7 scale with inline justification in the
same cell.

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

*CA returns. Each CA-1 row MUST present Registry anchor and Preamble anchor as structurally
distinct labeled elements before the Verification line. Inline concatenation fails.*

**CA-1.1 — C-01 verification:**
- Registry anchor — Schema ID TABLE_1 (with Tier [GCR-1]): declared columns with blank-cell rule.
- Preamble anchor — C-01: TABLE_1 / SE-1 / SHALL-A / CA-1.1.
- Verification — TABLE_1 present? Tier [GCR-1] populated? Rows ordered by tier? All cells
  filled? -> PASS / FAIL

**CA-1.2 — C-02 verification:**
- Registry anchor — Schema ID TABLE_2: FLS Profile Configured? [GCR-5] and Gap? [GCR-6]
  declared.
- Preamble anchor — C-02: TABLE_2 / SE-2 / SHALL-B / CA-1.2.
- Verification — TABLE_2 present? All sensitive fields? FLS status explicit? Null case stated?
  Gap? = YES in TABLE_5? -> PASS / FAIL

**CA-1.3 — C-03 verification:**
- Registry anchor — Schema ID TABLE_3 (Tier [GCR-1], Verified? [GCR-4]) with blank-cell rule.
- Preamble anchor — C-03: TABLE_3 / SE-0+SE-3 / SHALL-C / CA-1.3.
- Verification — Every TABLE_1 role in TABLE_3? Tier [GCR-1] populated? Effective Scope filled?
  Verified? [GCR-4] filled? -> PASS / FAIL

**CA-1.4 — C-04 verification:**
- Registry anchor — Schema ID TABLE_4: Checked? [GCR-3] and Severity [GCR-2]; all four vectors.
- Preamble anchor — C-04: TABLE_4 / SE-0 / SHALL-D / CA-1.4.
- Verification — TABLE_4 at SE-0 (before SE-1)? All four vectors? Checked? [GCR-3] = YES?
  Findings or specific rule-outs? -> PASS / FAIL

**CA-1.5 — C-05 verification:**
- Registry anchor — Schema ID TABLE_5 (Tier [GCR-1], Severity [GCR-2]) with blank-cell rule.
- Preamble anchor — C-05: TABLE_5 / SE-5 / SHALL-E / CA-1.5.
- Verification — TABLE_5 present? Named gap? Tier [GCR-1] populated? Severity [GCR-2]
  populated? Remediations exact? -> PASS / FAIL

**CA-1.6 — SHALL-F compliance verification:**
- Registry anchor — Schema ID TABLE_5 CS-EXPECTATION-VIOLATED: three-field Remediation
  required.
- Preamble anchor — SHALL-F: three-field block mandatory; rows missing any field MUST be
  reopened.
- Verification — For each CS-EXPECTATION-VIOLATED row: CS-Expected populated? SE-Actual
  populated? Delta populated with exact configuration change? -> PASS / FAIL per row.

**CA-1.7 — SHALL-G compliance verification (exact-label two-part closure blocks):**
- Registry anchor — CONTEXT section declared exact labels: "Blind spot 1 — Post-incident FLS
  gap" (SE-2), "Blind spot 2 — Cumulative privilege blind spot" (SE-3), "Blind spot 3 —
  OWD-sharing-rule override gap" (SE-4).
- Preamble anchor — SHALL-G: Line 1 MUST be `MANUAL GAP [<exact CONTEXT label>]:`; exact =
  character-for-character; paraphrase fails.
- Verification — SE-2/SE-3/SE-4 each open with exact label + STRUCTURED CLOSE? -> PASS / FAIL
  per section.

**CA-1.8 — CS-2/CS-3 Schema Registry registration + CS-0 acknowledgment verification:**
- Registry anchor — CS-2 and CS-3 declared with SE-updatable columns and SE-update protocols.
- Preamble anchor — CS-0 acknowledgment is a PHASE 1 structural requirement.
- Verification — CS-2 in Schema Registry? CS-3 same? CS-0 present before CS-1? CS-0 cites both
  schema IDs by exact label? SE populated SE-updatable columns? -> PASS / FAIL

**CA-1.9 — C-16 verification (GCR-N column header citations, all tables):**
- Registry anchor — Header citation rule: every graded column header MUST include [GCR-N]
  suffix. GCR-1=Tier, GCR-2=Severity, GCR-3=Checked?, GCR-4=Verified?,
  GCR-5=FLS Profile Configured?, GCR-6=Gap?, GCR-7=Escalation Risk.
- Preamble anchor — Schema Registry Step 0.1 declared all eight schemas with GCR-N citations.
- Verification — TABLE_1 `Tier [GCR-1]`? TABLE_2 `FLS Profile Configured? [GCR-5]` and
  `Gap? [GCR-6]`? TABLE_3 `Tier [GCR-1]` and `Verified? [GCR-4]`? TABLE_4 `Checked? [GCR-3]`
  and `Severity [GCR-2]`? TABLE_5 `Tier [GCR-1]` and `Severity [GCR-2]`? TABLE_6
  `Tier [GCR-1]` and `Escalation Risk [GCR-7]`? -> PASS / FAIL per table.

**CA-1.10 — C-18 verification (PPF one entry per table site):**
- Registry anchor — PPF Catalog declared PPF-1..PPF-6, one entry per named site
  (TABLE_1..TABLE_6).
- Preamble anchor — SHALL-H: PPF-1..PPF-6 required before any table.
- Verification — PPF-1 through PPF-6 all present? Each with verbatim wrong form + criterion
  by ID? -> PASS / FAIL per entry.

**CA-1.11 — TABLE_6 schema registration and SHALL-I compliance:**
- Registry anchor — Schema ID TABLE_6 declared: Role | Tier [GCR-1] | Verdict | Open Gap IDs
  | Escalation Risk [GCR-7]. Verdict scale: PASS-CLEAN / PASS-WITH-GAPS / FAIL.
- Preamble anchor — SHALL-I: TABLE_6 MUST be present at SE-5; every TABLE_1 role must have a
  TABLE_6 row; absent TABLE_6 = structural failure.
- Verification — TABLE_6 present at SE-5? Uses Schema ID TABLE_6 columns? Every TABLE_1 role
  has a row? Verdict values match scale? Escalation Risk [GCR-7] filled + inline justification?
  -> PASS / FAIL

**CA-1.12 — M5 enforcement-density floor + count-value mandate (V-01 axis):**
- Registry anchor — Step 0.2 M5 column declared enforcement layers. FLAGS: C-15 (SHALL-J),
  C-17 (SHALL-K count-value). SHALL-K requires `Row count: [actual integer]` — integer, not
  template `[N]` — before C-17 Self-Assessment.
- Preamble anchor — CA Phase 0 authored SHALL-J (C-15) and SHALL-K (C-17 count-value mandate).
  No criterion may remain single-layer after flag resolution.
- Verification — M5 column present in Step 0.2? C-15 dual-layer (SHALL-J)? C-17 dual-layer
  (SHALL-K)? No unresolved single-layer criteria? C-17 Self-Assessment contains `Row count:`
  followed by an integer (not template `[N]`)? Integer equals 14? -> PASS / FAIL per item.

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2,
Phase 0). [C-01..C-05: CA-1.1..CA-1.5. SHALL-F: CA-1.6. SHALL-G: CA-1.7. CS-0: CA-1.8.
C-16 GCR-N: CA-1.9. C-18 PPF: CA-1.10. C-09/TABLE_6/SHALL-I: CA-1.11. M5 floor +
count-value: CA-1.12. Overall: COMPLIANT / NON-COMPLIANT.]

---

## ASPIRATIONAL CRITERIA SELF-VERIFICATION (14-item, C-08..C-21)

Complete the Self-Assessment column before finalizing output. FAIL in any row requires revision.

**COUNT VALUE MANDATE applies to C-17 row (per SHALL-K):** Before filling the C-17
Self-Assessment cell: (1) count every row in this table; (2) write `Row count: [actual integer]`
immediately above the C-17 Self-Assessment cell — replace [actual integer] with the number you
counted. Do NOT write the template text `[N]` literally. `Row count: [N]` unfilled = auto-fail
for C-17 and C-19 simultaneously. Correct form: `Row count: 14`.

| Criterion | Pass Condition | Fail Signal | Self-Assessment |
|-----------|----------------|-------------|-----------------|
| C-08 | At least one cross-entity cascade traced: permission on Entity A produces derived access on Entity B, mechanism named | No cross-entity effect analyzed | |
| C-09 | TABLE_6 present at SE-5 using Schema ID TABLE_6 registered columns; one row per TABLE_1 role | No TABLE_6 OR non-registered column structure | |
| C-10 | Every table header includes `[CLOSES: <exact blind spot label>]` where applicable | Table headers missing CLOSES annotation | |
| C-11 | Every table has a null-case row | Table absent when no items found; null case as prose | |
| C-12 | Escalation Risk [GCR-7] column in TABLE_6; blank or "varies" = auto-fail | Blank, "varies", or outside declared GCR-7 scale | |
| C-13 | GCR block present before any table; all 7 columns registered; each has (a) scale (b) auto-fail (c) post-table co-located | Only scale declared; (b) or (c) in separate section | |
| C-14 | At least one prohibited prose form named with verbatim wrong form + criterion ID | No prohibited form named | |
| C-15 | This table present with Pass Condition / Fail Signal / Self-Assessment columns (per SHALL-J) | Flat checklist only OR different column names | |
| C-16 | Every graded column header in every table (TABLE_1..TABLE_6) includes [GCR-N] citation | Any graded column header missing [GCR-N] | |
| C-17 | Exactly 14 rows covering C-08..C-21; `Row count: [integer]` with actual integer (not template `[N]`) present before PASS (per SHALL-K); integer = 14 | Fewer than 14 rows OR any of C-08..C-21 absent OR Row count label absent OR `[N]` unfilled OR integer != 14 | Row count: |
| C-18 | PPF-1..PPF-6 present, one per named table site (TABLE_1..TABLE_6); each has verbatim wrong form + criterion ID | Fewer than 6 entries OR any entry not keyed to a named table site | |
| C-19 | C-17 Self-Assessment cell contains `Row count:` followed by the integer 14 (not template `[N]`); label and value present before PASS is written | C-17 Self-Assessment has absent Row count label OR template `[N]` unfilled OR integer does not equal 14 | |
| C-20 | Step 0.2 M5: Enforcement Layers column present; single-layer criteria flagged with SHALL resolution; no unresolved flags at Phase 0 close | Step 0.2 has no M5 column OR flagged criteria have no SHALL resolution OR flags unresolved at Phase 0 close | |
| C-21 | This self-verification table covers C-08..C-21 (14 rows); C-19/C-20/C-21 rows present; C-17 row contains `Row count:` with integer 14 | Table covers only C-08..C-18 (11 rows) OR C-19/C-20/C-21 absent OR C-17 Row count is template or absent | |

---

## V-02 — Single Axis: C-19/C-20/C-21 in Enforcement Matrix

**Axis:** C-19/C-20/C-21 in Step 0.2 enforcement matrix with M5 entries (Latent 2 single axis)
**Hypothesis:** Under R5 V-05, C-19/C-20/C-21 are aspirational criteria with only self-audit
enforcement (single-layer). Adding C-19/C-20/C-21 rows to the Step 0.2 enforcement matrix
gives each criterion M1-M5 scaffolding. C-20 (M5 Enforcement-Density Column) is
self-referential: its M1 enforcement is the M5 column itself — triple-enforced by inspection.
C-21 (Self-Referential Aspirational Loop) surfaces as single-layer in the new matrix,
triggering SHALL-L — applying the M5 upgrade mechanism recursively to the loop itself.

---

depth: standard
confidence: standard

You are running a permissions trace signal for: {{topic}}

---

[CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS — identical to V-01: three blind spots with exact labels.]

[GRADED COLUMN REGISTRY — identical to V-01: GCR-1..GCR-7 including GCR-7 for TABLE_6.]

[PROHIBITED PROSE FORMS CATALOG — identical to V-01: PPF-1..PPF-6 including PPF-6 for TABLE_6.]

[ROLE SEQUENCING MANDATE — identical to V-01 with the addition: Step 0.2 includes C-19/C-20/
C-21 enforcement matrix rows and SHALL-L for C-21. CA-1.12 extended to cover C-21 flag
resolution.]

[PHASE 0 STEP 0.1 SCHEMA REGISTRY — identical to V-01: eight schemas with GCR-N citations.]

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0) [V-02 changes]

**Declared rule: M1, M2, M3, M4 simultaneously active. M5 enforcement-density column active.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row | M5: Enforcement Layers |
|-----------|-------------------|---------------------|---------------------|------------------------|------------------------|
| C-01..C-18 | [identical to V-01 rows] | | | | |
| C-19 | C-17 row structure | self-audit table | SHALL-K | — | dual: SHALL-K+self-audit-C-19 *(C-19 enforced by same SHALL-K as C-17)* |
| C-20 | Step 0.2 M5 column | Phase-0 | — | CA-1.12 | triple: M1-self-referential(M5-column-presence)+M4-CA-1.12+self-audit-C-20 |
| C-21 | self-audit schema | aspirational-section | — | — | single: self-audit-only **[FLAG: upgrade via SHALL-L]** |

**M5 flag resolutions (C-15, C-17 identical to V-01; C-21 added):**

- C-21 flagged (single-layer) — SHALL-L resolution: "The self-referential aspirational loop
  (C-21) MUST cover all declared criteria C-08..C-21 (exactly 14 rows). A table covering only
  C-08..C-18 (11 rows) fails SHALL-L. Each of C-19, C-20, and C-21 Self-Assessment cells must
  be non-blank. A blank or omitted Self-Assessment for any of C-19/C-20/C-21 fails SHALL-L
  even if the row is structurally present." C-21 upgrades to dual-layer via SHALL-L.

**SHALL obligations:** SHALL-A through SHALL-K identical to V-01. SHALL-L added:
- SHALL-L (C-21 M5 flag resolution): The self-referential loop MUST cover C-08..C-21 (14
  rows). C-19, C-20, and C-21 Self-Assessment cells must each be non-blank.

*Handing to PHASE 1 — CS.*

[PHASE 1 — CS, PHASE 2 — SE: identical to V-01.]

[PHASE 3 CA-1.1 through CA-1.11: identical to V-01.]

**CA-1.12 — M5 enforcement-density floor + C-21 SHALL-L resolution [V-02 version]:**
- Registry anchor — Step 0.2 M5 column covers C-01..C-21. FLAGS: C-15 (SHALL-J), C-17
  (SHALL-K), C-21 (SHALL-L). C-19 dual via SHALL-K. C-20 triple. C-21 upgraded via SHALL-L.
- Preamble anchor — CA Phase 0 authored SHALL-J, SHALL-K, SHALL-L. No criterion may remain
  single-layer after resolution.
- Verification — M5 column present? C-19 dual-layer (SHALL-K)? C-20 triple-layer? C-21 flag
  resolved via SHALL-L? C-19/C-20/C-21 Self-Assessment cells non-blank? -> PASS / FAIL per item.

[ASPIRATIONAL CRITERIA SELF-VERIFICATION: identical to V-01 except C-21 Fail Signal updated
to: "Table covers C-08..C-18 only OR C-19/C-20/C-21 absent OR any of C-19/C-20/C-21
Self-Assessment cells blank (per SHALL-L)."]

---

## V-03 — Single Axis: SHALL-L Mechanism-Verification Phrases

**Axis:** SHALL-L requires specific mechanism-verification phrases in C-19/C-20/C-21
Self-Assessment cells (Latent 3 single axis)
**Hypothesis:** V-02's SHALL-L requires C-19/C-20/C-21 cells to be non-blank. But "PASS"
without citing the mechanism is assertion without evidence — structurally identical to the
problem COUNT MANDATE solved for C-17. Requiring mechanism-verification phrases creates
observable claims verifiable by inspection without reading the full output: C-19's cell cites
the Row count integer; C-20's cell cites M5 column counts; C-21's cell cites actual count and
row coverage.

---

depth: standard
confidence: standard

You are running a permissions trace signal for: {{topic}}

---

[CONTEXT, GRADED COLUMN REGISTRY, PROHIBITED PROSE FORMS CATALOG: identical to V-01.]

[ROLE SEQUENCING MANDATE: identical to V-01 except SHALL-L now requires mechanism-verification
phrases (not just non-blank). CA-1.12 verifies phrase content.]

[PHASE 0 STEP 0.1 SCHEMA REGISTRY: identical to V-01.]

[PHASE 0 STEP 0.2 ENFORCEMENT MATRIX: identical to V-01 (same rows, same M5 values).]

**SHALL obligations:** SHALL-A through SHALL-K identical to V-01. SHALL-L added:
- SHALL-L (mechanism-verification phrases): Each of C-19, C-20, and C-21 Self-Assessment cells
  MUST contain a mechanism-verification phrase. Generic "PASS" or "Confirmed" without citing
  the mechanism is a SHALL-L violation.

  Required phrases:
  - **C-19 Self-Assessment MUST state:** `Row count: [N] confirmed in C-17 Self-Assessment
    cell.` where [N] is the integer found (e.g., `Row count: 14 confirmed in C-17
    Self-Assessment cell.`). Simply writing "PASS" fails.
  - **C-20 Self-Assessment MUST state:** `M5 column confirmed in Step 0.2: [K] criteria listed,
    [F] flagged single-layer, all [F] flags resolved.` where [K] and [F] are actual counts
    from the Step 0.2 matrix. Simply writing "Present" fails.
  - **C-21 Self-Assessment MUST state:** `Table covers C-08..C-21 with Row count: [N] in C-17;
    C-19/C-20/C-21 rows present with mechanism phrases.` where [N] is the integer. Simply
    stating "14 rows present" without confirming mechanism phrase presence fails.

  CA-1.12 verifies SHALL-L compliance by checking each phrase is present and contains integers,
  not template placeholders.

[PHASE 1 — CS, PHASE 2 — SE: identical to V-01.]

[PHASE 3 CA-1.1 through CA-1.11: identical to V-01.]

**CA-1.12 — M5 enforcement-density floor + SHALL-L mechanism-phrase compliance [V-03 version]:**
- Registry anchor — Step 0.2 M5 column: FLAGS C-15 (SHALL-J), C-17 (SHALL-K). SHALL-L requires
  mechanism-verification phrases in C-19/C-20/C-21 Self-Assessment cells per specified format.
- Preamble anchor — CA Phase 0 authored SHALL-J, SHALL-K (count-value), SHALL-L (phrases).
- Verification — M5 column present? C-15 dual-layer? C-17 dual-layer? C-19 Self-Assessment
  contains `Row count: [integer] confirmed in C-17 Self-Assessment cell.` with actual integer?
  C-20 Self-Assessment contains `M5 column confirmed in Step 0.2: [K] criteria listed, [F]
  flagged, all [F] flags resolved.` with actual integers K and F? C-21 Self-Assessment contains
  `Table covers C-08..C-21 with Row count: [N] in C-17; C-19/C-20/C-21 rows present with
  mechanism phrases.` with actual N? -> PASS / FAIL per phrase.

## ASPIRATIONAL CRITERIA SELF-VERIFICATION (14-item, C-08..C-21) [V-03 version]

Complete the Self-Assessment column before finalizing output. FAIL in any row requires revision.
COUNT MANDATE (per SHALL-K): write `Row count: [actual integer]` above C-17 Self-Assessment.
MECHANISM PHRASES required in C-19/C-20/C-21 per SHALL-L (see phrase specifications above).

| Criterion | Pass Condition | Fail Signal | Self-Assessment |
|-----------|----------------|-------------|-----------------|
| C-08 | At least one cross-entity cascade traced with mechanism named | No cross-entity effect analyzed | |
| C-09 | TABLE_6 at SE-5 with Schema ID TABLE_6 columns; one row per TABLE_1 role | No TABLE_6 OR non-registered columns | |
| C-10 | Every table header includes `[CLOSES: <exact label>]` where applicable | Table headers missing CLOSES annotation | |
| C-11 | Every table has a null-case row | Null case as prose OR table absent | |
| C-12 | Escalation Risk [GCR-7] in TABLE_6; blank = auto-fail | Blank, "varies", or outside GCR-7 scale | |
| C-13 | GCR block: 7 columns, each with (a)(b)(c) co-located | (b) or (c) in separate section | |
| C-14 | Prohibited prose form verbatim + criterion by ID | No prohibited form named | |
| C-15 | This table with Pass Condition / Fail Signal / Self-Assessment columns (SHALL-J) | Flat checklist OR different column names | |
| C-16 | GCR-N in every graded column header TABLE_1..TABLE_6 | Any header missing [GCR-N] | |
| C-17 | Exactly 14 rows C-08..C-21; Row count label with integer present before PASS (SHALL-K) | Fewer than 14 rows OR Row count absent OR integer missing | Row count: |
| C-18 | PPF-1..PPF-6, one per table site, verbatim form + criterion ID | Fewer than 6 OR site not named | |
| C-19 | C-17 Self-Assessment has `Row count: [integer] confirmed in C-17 Self-Assessment cell.` with actual integer (SHALL-L) | "PASS" only, no mechanism phrase OR integer absent | |
| C-20 | C-20 Self-Assessment has `M5 column confirmed in Step 0.2: [K] criteria listed, [F] flagged, all [F] flags resolved.` with actual integers (SHALL-L) | "Present" or "PASS" only OR template placeholders for K or F | |
| C-21 | C-21 Self-Assessment has `Table covers C-08..C-21 with Row count: [N] in C-17; C-19/C-20/C-21 rows present with mechanism phrases.` with actual N (SHALL-L) | Generic PASS OR Row count not cited OR mechanism phrase absent | |

---

## V-04 — Combined: Count-Value Fills + Enforcement Matrix Rows

**Axis:** V-01 (count-value fills, Latent 1) + V-02 (C-19/C-20/C-21 in enforcement matrix,
Latent 2)
**Hypothesis:** Structurally independent axes. V-01 targets the self-audit table (C-17
Self-Assessment must contain integer, not template `[N]`). V-02 targets Phase 0 (new criteria
need enforcement scaffolding). Combined they close both the count-placeholder gap and the
enforcement-absence gap. Prediction: V-04 achieves full C-19 pass (integer required AND C-19
has SHALL-K matrix entry) and C-20 pass (triple-layer via matrix) but C-21 may be weak —
SHALL-L's non-blank requirement permits "PASS" assertion without evidence.

---

depth: standard
confidence: standard

You are running a permissions trace signal for: {{topic}}

---

[CONTEXT, GRADED COLUMN REGISTRY, PROHIBITED PROSE FORMS CATALOG: identical to V-01.]

[ROLE SEQUENCING MANDATE: identical to V-01 with addition of C-19/C-20/C-21 in Step 0.2
matrix (V-02), SHALL-L for C-21 (V-02), and count-value mandate in SHALL-K (V-01).]

[PHASE 0 STEP 0.1 SCHEMA REGISTRY: identical to V-01.]

[PHASE 0 STEP 0.2 ENFORCEMENT MATRIX: identical to V-02 (includes C-19/C-20/C-21 rows with
SHALL-L flag for C-21). SHALL-K updated with V-01 count-value language: integer required,
template `[N]` = auto-fail.]

**SHALL obligations:** SHALL-A through SHALL-K as in V-01 (with count-value mandate in SHALL-K).
SHALL-L as in V-02 (non-blank cells for C-19/C-20/C-21).

[PHASE 1 — CS, PHASE 2 — SE: identical to V-01.]
[PHASE 3 CA-1.1 through CA-1.11: identical to V-01.]

**CA-1.12 — M5 floor + count-value mandate + C-21 SHALL-L [V-04 combined version]:**
- Registry anchor — Step 0.2 M5 column covers C-01..C-21. FLAGS: C-15 (SHALL-J), C-17 (SHALL-K
  count-value, integer required), C-21 (SHALL-L). C-19 dual via SHALL-K. C-20 triple. C-21
  dual via SHALL-L (non-blank cells required).
- Preamble anchor — CA Phase 0 authored SHALL-J, SHALL-K (integer), SHALL-L (non-blank).
- Verification — M5 column present? C-19 dual-layer? C-20 triple-layer? C-21 SHALL-L resolved?
  C-17 Self-Assessment contains integer (not `[N]`) = 14? C-19/C-20/C-21 cells non-blank?
  -> PASS / FAIL per item.

## ASPIRATIONAL CRITERIA SELF-VERIFICATION (14-item, C-08..C-21) [V-04 combined]

Complete the Self-Assessment column before finalizing output. FAIL in any row requires revision.

**COUNT VALUE MANDATE (per SHALL-K, V-01 axis):** Write `Row count: [actual integer]` — the
integer you counted — immediately above C-17 Self-Assessment. Template `[N]` unfilled = auto-fail
for C-17 and C-19 simultaneously. Correct form: `Row count: 14`.

| Criterion | Pass Condition | Fail Signal | Self-Assessment |
|-----------|----------------|-------------|-----------------|
| C-08 | At least one cross-entity cascade traced with mechanism named | No cross-entity effect analyzed | |
| C-09 | TABLE_6 at SE-5 with Schema ID TABLE_6 columns; one row per TABLE_1 role | No TABLE_6 OR non-registered columns | |
| C-10 | Every table header includes `[CLOSES: <exact label>]` where applicable | Table headers missing CLOSES annotation | |
| C-11 | Every table has a null-case row | Null case as prose OR table absent | |
| C-12 | Escalation Risk [GCR-7] in TABLE_6; blank = auto-fail | Blank, "varies", or outside GCR-7 scale | |
| C-13 | GCR block: 7 columns, each with (a)(b)(c) co-located | (b) or (c) in separate section | |
| C-14 | Prohibited prose form verbatim + criterion by ID | No prohibited form named | |
| C-15 | This table with Pass Condition / Fail Signal / Self-Assessment columns (SHALL-J) | Flat checklist OR different column names | |
| C-16 | GCR-N in every graded column header TABLE_1..TABLE_6 | Any header missing [GCR-N] | |
| C-17 | Exactly 14 rows C-08..C-21; `Row count: [integer]` (not template) present before PASS (SHALL-K); integer = 14 | Fewer than 14 rows OR Row count absent OR template `[N]` unfilled OR integer != 14 | Row count: |
| C-18 | PPF-1..PPF-6, one per table site, verbatim form + criterion ID | Fewer than 6 OR site not named | |
| C-19 | C-17 Self-Assessment has integer count (not template `[N]`); C-19 in enforcement matrix via SHALL-K | Template `[N]` in C-17 Self-Assessment OR Row count label absent | |
| C-20 | Step 0.2 M5 column present; C-19/C-20/C-21 in enforcement matrix; C-20 triple-layer | No M5 column OR new criteria absent from matrix OR C-21 flag unresolved | |
| C-21 | Table covers C-08..C-21 (14 rows); C-19/C-20/C-21 Self-Assessment cells non-blank (per SHALL-L) | Table covers C-08..C-18 only OR C-19/C-20/C-21 absent OR any cell blank | |

---

## V-05 — Full Integration: V-01 + V-02 + V-03 + CA-1.13 Loop Verification

**Axis:** Count-value fills + enforcement matrix rows + mechanism-verification phrases +
CA-1.13 dedicated double-anchor verification for C-21
**Hypothesis:** V-04 closes the count-placeholder gap and enforcement-absence gap. V-03 closes
the self-assessment assertion gap. CA-1.13 adds the fourth closure: a dedicated double-anchor
verification row for the C-21 self-referential loop, verifying that C-19/C-20/C-21 rows
contain mechanism phrases and that the C-17 integer matches the actual row count. CA-1.13
makes the self-referential loop fully auditable from the CA-1 pass without reading the
self-audit table — the same structural property that makes CA-1.11 sufficient to verify
TABLE_6 without reading SE-5.

---

depth: standard
confidence: standard

You are running a permissions trace signal for: {{topic}}

---

[CONTEXT, GRADED COLUMN REGISTRY, PROHIBITED PROSE FORMS CATALOG: identical to V-01.]

## ROLE SEQUENCING MANDATE

[Identical to V-01 except: Step 0.2 includes C-19/C-20/C-21 enforcement matrix rows (V-02),
SHALL-L mechanism-verification phrases (V-03), and CA-1.13 pre-assigned for C-21 loop
verification. CA-1.1 through CA-1.13 pre-assigned.]

[PHASE 0 STEP 0.1 SCHEMA REGISTRY: identical to V-01.]

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0) [V-05]

**Declared rule: M1, M2, M3, M4 simultaneously active. M5 enforcement-density column active.
CA-1.12 verifies enforcement-density floor. CA-1.13 pre-assigned for C-21 loop verification.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row | M5: Enforcement Layers |
|-----------|-------------------|---------------------|---------------------|------------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 | quad: M1+M2+M3+M4 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 | quad: M1+M2+M3+M4 |
| C-03 | TABLE_3 | SE-0+SE-3 | SHALL-C | CA-1.3 | quad: M1+M2+M3+M4 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 | quad: M1+M2+M3+M4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 | quad: M1+M2+M3+M4 |
| C-09 | TABLE_6 | SE-5 | SHALL-I | CA-1.11 | quad: M1+M2+M3+M4 |
| C-13 | GCR block | Phase-0-precondition | SHALL-G | CA-1.7 | triple: upfront+SHALL-G+CA-1.7 |
| C-14 | PPF catalog | PPF-section | SHALL-H | CA-1.10 | triple: upfront+SHALL-H+CA-1.10 |
| C-15 | self-audit table | aspirational-section | SHALL-J | — | dual: SHALL-J+self-audit |
| C-16 | GCR header-rule | GCR-block | — | CA-1.9 | triple: upfront+CA-1.9+self-audit-C-16 |
| C-17 | 14-row structure | aspirational-section | SHALL-K | — | dual: SHALL-K(count-value)+self-audit |
| C-18 | PPF catalog | PPF-section | SHALL-H | CA-1.10 | triple: upfront+SHALL-H+CA-1.10 |
| C-19 | C-17 row structure | self-audit table | SHALL-K | — | dual: SHALL-K+self-audit-C-19 |
| C-20 | Step 0.2 M5 column | Phase-0 | — | CA-1.12 | triple: M1-self-referential+CA-1.12+self-audit-C-20 |
| C-21 | self-audit schema | aspirational-section | SHALL-L | CA-1.13 | triple: SHALL-L(phrases)+CA-1.13(loop-audit)+self-audit-C-21 |

**M5 flag resolutions:**
- C-15 flagged — SHALL-J resolution: [identical to V-01]
- C-17 flagged — SHALL-K resolution (COUNT VALUE MANDATE): [identical to V-01]
- C-21 flagged — SHALL-L + CA-1.13 resolution: "The self-referential loop MUST cover
  C-08..C-21 (14 rows). C-19/C-20/C-21 Self-Assessment cells must contain mechanism-
  verification phrases per SHALL-L. CA-1.13 verifies the loop from the CA-1 pass using
  double-anchor format, making the loop auditable without reading the full self-audit table."
  C-21 upgrades to triple-layer via SHALL-L + CA-1.13.

**SHALL obligations:** SHALL-A through SHALL-K identical to V-01. SHALL-L identical to V-03
(specific phrase formats for C-19/C-20/C-21 Self-Assessment cells).

[PHASE 1 — CS, PHASE 2 — SE: identical to V-01.]

[PHASE 3 CA-1.1 through CA-1.11: identical to V-01.]

**CA-1.12 — M5 enforcement-density floor + count-value mandate [V-05 version]:**
- Registry anchor — Step 0.2 M5 column covers C-01..C-21. FLAGS: C-15 (SHALL-J), C-17
  (SHALL-K count-value), C-21 (SHALL-L + CA-1.13). C-19 dual. C-20 triple. C-21 triple.
  SHALL-K: integer required (not template `[N]`).
- Preamble anchor — CA Phase 0 authored SHALL-J, SHALL-K (count-value), SHALL-L (phrases).
  CA-1.13 pre-assigned as M4 for C-21.
- Verification — M5 column present? C-15 dual? C-17 dual? C-19 dual? C-20 triple? C-21
  triple? C-17 Self-Assessment contains integer 14 (not `[N]`)? -> PASS / FAIL per item.

**CA-1.13 — C-21 self-referential loop completeness verification:**
- Registry anchor — Aspirational self-verification table schema: C-08..C-21 (14 rows). SHALL-L
  requires mechanism-verification phrases in C-19/C-20/C-21 Self-Assessment cells: C-19 cites
  Row count integer; C-20 cites M5 matrix counts (K criteria, F flags); C-21 cites count and
  row coverage.
- Preamble anchor — CA Phase 0 authored SHALL-L with exact phrase specifications. CA-1.13
  pre-assigned in Step 0.2 as M4 verification row for C-21 (triple-layer upgrade).
- Verification — Self-verification table present with 14 rows? C-08..C-21 all present? C-19
  Self-Assessment contains `Row count: [integer] confirmed in C-17 Self-Assessment cell.` with
  actual integer? C-20 Self-Assessment contains `M5 column confirmed in Step 0.2: [K] criteria
  listed, [F] flagged, all [F] flags resolved.` with actual integers K and F? C-21
  Self-Assessment contains `Table covers C-08..C-21 with Row count: [N] in C-17; C-19/C-20/C-21
  rows present with mechanism phrases.` with actual N? Row count integer in C-17 = 14 = actual
  row count (cross-row consistency check)? -> PASS / FAIL per item.

**CA Format Compliance Verdict — Phase 0 citation:**
[C-01..C-05: CA-1.1..CA-1.5. SHALL-F: CA-1.6. SHALL-G: CA-1.7. CS-0: CA-1.8. C-16 GCR-N:
CA-1.9. C-18 PPF: CA-1.10. C-09/TABLE_6/SHALL-I: CA-1.11. M5 floor + count-value: CA-1.12.
C-21 loop completeness: CA-1.13. Overall: COMPLIANT / NON-COMPLIANT.]

---

## ASPIRATIONAL CRITERIA SELF-VERIFICATION (14-item, C-08..C-21) [V-05 full integration]

Complete the Self-Assessment column before finalizing output. FAIL in any row requires revision.

**COUNT VALUE MANDATE (per SHALL-K):** Write `Row count: [actual integer]` — the integer you
counted — immediately above C-17 Self-Assessment. Template `[N]` unfilled = auto-fail for C-17
and C-19 simultaneously. Correct form: `Row count: 14`.

**MECHANISM PHRASES required (per SHALL-L) in C-19/C-20/C-21 Self-Assessment cells:**
- C-19: `Row count: [integer] confirmed in C-17 Self-Assessment cell.`
- C-20: `M5 column confirmed in Step 0.2: [K] criteria listed, [F] flagged, all [F] flags resolved.`
- C-21: `Table covers C-08..C-21 with Row count: [N] in C-17; C-19/C-20/C-21 rows present with mechanism phrases.`

| Criterion | Pass Condition | Fail Signal | Self-Assessment |
|-----------|----------------|-------------|-----------------|
| C-08 | At least one cross-entity cascade traced with mechanism named | No cross-entity effect analyzed | |
| C-09 | TABLE_6 at SE-5 with Schema ID TABLE_6 columns; one row per TABLE_1 role | No TABLE_6 OR non-registered columns | |
| C-10 | Every table header includes `[CLOSES: <exact label>]` where applicable | Table headers missing CLOSES annotation | |
| C-11 | Every table has a null-case row | Null case as prose OR table absent | |
| C-12 | Escalation Risk [GCR-7] in TABLE_6; blank = auto-fail | Blank, "varies", or outside GCR-7 scale | |
| C-13 | GCR block: 7 columns, each with (a)(b)(c) co-located | (b) or (c) in separate section | |
| C-14 | Prohibited prose form verbatim + criterion by ID | No prohibited form named | |
| C-15 | This table with Pass Condition / Fail Signal / Self-Assessment columns (SHALL-J) | Flat checklist OR different column names | |
| C-16 | GCR-N in every graded column header TABLE_1..TABLE_6 | Any header missing [GCR-N] | |
| C-17 | Exactly 14 rows C-08..C-21; `Row count: [integer]` (not template `[N]`) before PASS (SHALL-K); integer = 14 | Fewer than 14 rows OR C-08..C-21 not all present OR Row count absent OR `[N]` unfilled OR integer != 14 | Row count: |
| C-18 | PPF-1..PPF-6, one per table site, verbatim form + criterion ID | Fewer than 6 OR any entry not keyed to a named table site | |
| C-19 | C-17 Self-Assessment has `Row count: [integer] confirmed in C-17 Self-Assessment cell.` with actual integer (SHALL-L; also enforced by SHALL-K) | Template `[N]` OR "PASS" only OR Row count label absent | |
| C-20 | C-20 Self-Assessment has `M5 column confirmed in Step 0.2: [K] criteria listed, [F] flagged, all [F] flags resolved.` with actual integers (SHALL-L; triple via self-referential M5 + CA-1.12 + self-audit) | "Present" or "PASS" only OR template placeholders for K/F | |
| C-21 | C-21 Self-Assessment has `Table covers C-08..C-21 with Row count: [N] in C-17; C-19/C-20/C-21 rows present with mechanism phrases.` with actual N; CA-1.13 double-anchor verifies (SHALL-L + CA-1.13 triple) | Generic PASS OR Row count not cited OR mechanism phrase absent OR CA-1.13 cross-row consistency fails | |
