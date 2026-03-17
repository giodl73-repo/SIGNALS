# trace-permissions Variate — Round 15
**Date:** 2026-03-17
**Rubric:** v14 (proposed) — 34 criteria (C-01 through C-42), denominator 34
**Target:** 34/34 — add C-40 (bidirectional loop verification), C-41 (attestation schema in
Registry), C-42 (Phase 0 artifact manifest) to R14-V-05 base

**State entering Round 15:**

| Variation | v13 score | Under v14 | Notes |
|-----------|-----------|-----------|-------|
| R14-V-05 | 100.0 (31/31) | 99.1 (31/34) | Bidirectional columns present as excellence signal; no CA-1.10 label-identity scan; no ATTEST-TBL schema in Registry; no Phase 0 manifest |
| R14-V-04 | 100.0 (31/31) | 99.1 (31/34) | Same three gaps; CA-1.N Scope Declaration table is enhancement but does not cover C-40/41/42 |
| R14-V-01/02/03 | 100.0 (31/31) | 99.1 (31/34) | Same three gaps |

Path to 34/34: R14-V-05 base + C-40 (CA-1.10 label-identity cross-scan formalizing the
bidirectional loop) + C-41 (ATTEST-TBL schema declared in Schema Registry Step 0.1) + C-42
(Phase 0 Artifact Manifest with terminal verdict item-count citation).

---

## v13 -> v14 Rubric Extension

Three new aspirational criteria. Denominator: 31 -> 34. Each aspirational = 10/34 ~= 0.294 pts.

| ID | Hangs off | What it tests |
|----|-----------|---------------|
| C-40 | C-34+C-36+C-37 | Preamble axis table includes "Attestation Row Ref" column pre-assigning attestation row labels (ATTEST-A-N); attestation table includes "Preamble Row Ref" back-column. CA-1.10 explicitly verifies label-identity cross-scan: for each A-N row, preamble Attestation Row Ref = ATTEST-A-N matches attestation Preamble Row Ref = A-N. Elevates V-05's bidirectional excellence signal into a verifiable structural criterion. Pass condition: preamble axis table has Attestation Row Ref column with values for all three rows; attestation table has Preamble Row Ref back-column; CA-1.10 row performs explicit per-row cross-scan. An output where bidirectional columns exist but no CA-1.10 cross-scan is performed fails. |
| C-41 | C-20+C-36+C-40 | Schema Registry Step 0.1 includes pre-declared schema entry for the TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION table (Schema ID: ATTEST-TBL), declaring its column structure including the Preamble Row Ref back-column and global blank-cell rule. At least one CA-1.N verification row that touches attestation content opens with a double-anchor citing ATTEST-TBL. Pass condition: ATTEST-TBL schema entry appears in Step 0.1 with at least 5 declared columns including Row ID, Preamble Row Ref, and Status; at least one CA-1.N row cites ATTEST-TBL in its Registry anchor. An output where the attestation table exists but no Schema Registry schema governs it fails even if C-23 passes. |
| C-42 | C-21+C-22+C-40 | At the close of Phase 0, before the handoff string, CA produces a numbered Phase 0 Artifact Manifest listing: (a) every Schema ID registered in Step 0.1 by exact ID; (b) every preamble criterion row by C-NN ID; (c) every SHALL obligation by letter; (d) every supplementary CA-1.N row ID; (e) every A-N axis declaration row ID. CA's terminal verdict in Phase 3 cites the Phase 0 manifest by section counts confirming all declared artifacts were exercised. Pass condition: named Phase 0 Artifact Manifest section appears before the Phase 0 handoff string with all five enumeration categories; terminal verdict contains explicit manifest citation with item counts per category. |

**R14-V-05 re-scored under v14:**

| Criterion | v13 | v14 verdict | Why it moves |
|-----------|-----|-------------|--------------|
| C-40 | -- (new) | FAIL | Bidirectional columns present but CA-1.10 label-identity scan absent |
| C-41 | -- (new) | FAIL | No ATTEST-TBL schema in Schema Registry Step 0.1 |
| C-42 | -- (new) | FAIL | No Phase 0 Artifact Manifest; terminal verdict has no manifest citation |
| R14-V-05 composite | 100.0 (31/31) | **99.1 (31/34)** | 3 x 0.294 = 0.88 pts lost |

---

## Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Single-axis C-40: CA-1.10 label-identity cross-scan | R14-V-05 base. CA-1.10 supplementary row added in Step 0.2 preamble. Phase 3 CA-1.10 performs explicit per-row label-identity cross-scan over preamble Attestation Row Ref and attestation Preamble Row Ref. Phase 3 mandate updated to name CA-1.10. Hypothesis: 32/34 (C-41 and C-42 remain open). |
| V-02 | Single-axis C-41: ATTEST-TBL schema in Registry | R14-V-05 base. Schema Registry gains ATTEST-TBL entry in Step 0.1. Phase 3 terminal verdict CA verification opens with ATTEST-TBL double-anchor reaffirmation. Hypothesis: 32/34 (C-40 and C-42 remain open). |
| V-03 | Single-axis C-42: Phase 0 Artifact Manifest | R14-V-05 base. Phase 0 gains Step 0.3 -- Phase 0 Artifact Manifest before handoff. Terminal verdict cites manifest by item count per category. Phase 0 mandate updated to name Step 0.3. Hypothesis: 32/34 (C-40 and C-41 remain open). |
| V-04 | C-40 + C-41 combined | R14-V-05 base + both changes. ATTEST-TBL in Registry; CA-1.10 cites ATTEST-TBL schema in its Registry anchor, closing the Registry-preamble-verification chain over the attestation table itself. Hypothesis: 33/34 (C-42 remains open). |
| V-05 | Full canonical: C-40 + C-41 + C-42 | R14-V-05 base + all three new criteria. CA-1.10 (label-identity scan, double-anchored by ATTEST-TBL) + ATTEST-TBL schema in Registry + Phase 0 Artifact Manifest with terminal manifest citation. Hypothesis: 34/34. |

---

## V-01 -- Single-Axis C-40: CA-1.10 Label-Identity Cross-Scan

**Axis:** C-40 -- CA-1.10 supplementary row added to Phase 0 Step 0.2 preamble and Phase 3
mandate. CA-1.10 performs an explicit label-identity cross-scan: for each A-N row in the preamble
axis declaration, confirms the preamble Attestation Row Ref value (ATTEST-A-N) matches the
attestation table Preamble Row Ref value (A-N), and vice versa. Converts V-05's bidirectional
column loop from excellence signal into verifiable structural criterion. All other R14-V-05
architecture preserved.
**Hypothesis:** 32/34 (adds C-40; C-41 and C-42 remain open).

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

Manual security reviews of Dataverse environments routinely miss three failure scenarios that this
trace is designed to surface:

**Blind spot 1 -- Post-incident FLS gap.** Column security profiles are rarely audited
proactively. Sensitive fields -- credit limits, compensation data, SSNs, contact identifiers --
remain readable and writable by any role unless a column security profile explicitly restricts
them. The security roles UI does not surface which fields lack column security profiles; gaps are
discovered after data exposure, not before.

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
SE-4 closes Blind spot 3. Closure notes are exact-label two-part blocks co-located at each SE
sub-section opening, carrying the exact blind-spot label from this CONTEXT section.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins.

**PHASE 0 -- CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1: seven schemas -- TABLE_1 through TABLE_5
with Tier columns on TABLE_1 and TABLE_3; CS-2 and CS-3 with SE-updatable columns and update
protocols; TABLE_4 schema note declares SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot requirement)
and the Criterion Enforcement Matrix preamble (Step 0.2: SHALL-A through SHALL-G with SHALL-D
extension sub-clause for C-35; M4 CA-1.1 through CA-1.10 pre-assigned; R12 Structural Axis
Declaration with A-1/A-2/A-3 Row IDs, Attestation Row Ref column (ATTEST-A-1/A-2/A-3), and
non-interference statement). CA issues handoff to PHASE 1.

**PHASE 1 -- CS (Customer Success):**
Executes second. Opens with CS-0 sub-section (Schema Registry acknowledgment: cites CS-2 and CS-3
schema IDs by exact label; lists SE-updatable columns; confirms expectation format). Then produces
CS-1, CS-2, CS-3. CS does not fill TABLE_1-5. Issues handoff to PHASE 2.

**PHASE 2 -- SE (Security Engineer / Dataverse Security Expert):**
Executes third in privilege-tier descent order. SE-0 (admin-tier inventory + TABLE_4) before SE-1.
TABLE_1 and TABLE_3 include Tier column. SE-2/SE-3/SE-4 use exact-label two-part closure blocks
per SHALL-G. SE-4 STRUCTURED CLOSE carries TABLE_4 row cross-reference at SE-0 slot naming a
specific TABLE_4 vector row. Issues handoff to PHASE 3.

**PHASE 3 -- CA-1 (CA Verification Pass):**
CA returns. Double-anchor reaffirmation per row. CA-1.8 verifies CS-0 precedes CS-1. CA-1.9
verifies SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference (distinct from CA-1.4 and
CA-1.7). CA-1.10 verifies label-identity between preamble Attestation Row Ref column (A-N rows)
and attestation Preamble Row Ref column (ATTEST-A-N rows) by explicit cross-scan: ATTEST-A-1
Preamble Row Ref = A-1; A-1 Attestation Row Ref = ATTEST-A-1; same for A-2/A-3. Terminal verdict
includes TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION with ATTEST-A-N Row IDs and Preamble Row Ref
back-column.

---

## PHASE 0 -- CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1 and 0.2 before any other phase begins.*

### Step 0.1 -- Schema Registry (CA-authored, Phase 0)

**All table schemas declared centrally by CA. Blank-cell prohibition is global. SE-update
protocols for CS-2 and CS-3 declared co-located with schema entry.**

**Schema ID: TABLE_1 -- Role-Operation Matrix**
Declared columns: `Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Tier values: Admin / Custom / Restricted. Rows ordered: Admin tier first, Custom second,
Restricted last. Blank-cell rule: all cells Granted / Denied / Conditional (condition inline) / N/A.

**Schema ID: TABLE_2 -- FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Blank-cell rule: FLS Profile Configured? = Configured / Not Configured. Gap? = YES / NO.

**Schema ID: TABLE_3 -- Record Scope by Role**
Declared columns: `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Tier values mirror TABLE_1. Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU /
Org-wide / Team-scoped / Sharing-[rule name]. Verified? = YES / NO.

**Schema ID: TABLE_4 -- Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
Blank-cell rule: all four vectors (team inheritance, sharing rules, impersonation, admin/env
roles), Checked? = YES, Finding = escalation path or specific rule-out (never blank).
Note: TABLE_4 executes at SE-0 before SE-1. Additionally, SE-4's STRUCTURED CLOSE block SHALL
carry a TABLE_4 row cross-reference at its SE-0 slot: the SE-0 slot names a specific TABLE_4
vector row by its exact vector label. This SE-0 slot cross-reference is the subject of CA-1.9
verification, distinct from CA-1.4 (SE-0 execution ordering) and CA-1.7 (MANUAL GAP blocks).

**Schema ID: TABLE_5 -- Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation`
Blank-cell rule: Remediation = exact object + exact location + expected post-fix state.
CS-EXPECTATION-VIOLATED Remediation (three-field block):
- CS-Expected: cite CS-2 or CS-3 row, state expectation verbatim or by row reference.
- SE-Actual: SE finding that contradicts the expectation.
- Delta: exact configuration change to align SE-Actual to CS-Expected.

**Schema ID: CS-2 -- Sharing Rule Expectations (CS-authored expectation table)**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference (TABLE_4 row ID or TABLE_5 row ID);
SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE update protocol: SE populates after TABLE_4 analysis at SE-0. CONTRADICTED triggers
CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

**Schema ID: CS-3 -- Cross-Role Access Differential Expectations (CS-authored expectation table)**
Declared columns: `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference (TABLE_1 row ID or TABLE_3 row ID);
SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE update protocol: SE populates after TABLE_1/TABLE_3 analysis. CONTRADICTED triggers
CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: M1, M2, M3 simultaneously active. M4 pre-assigned.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-0 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**Supplementary CA verification rows (Phase 0 pre-assignment):**

| Row ID | What it verifies | Scope | Distinct from |
|--------|-----------------|-------|---------------|
| CA-1.6 | SHALL-F CS-EXPECTATION-VIOLATED three-field structure | TABLE_5 CS-EV rows | -- |
| CA-1.7 | SHALL-G exact-label MANUAL GAP two-part blocks at SE-2/SE-3/SE-4 | SE-2, SE-3, SE-4 openings | CA-1.9 |
| CA-1.8 | CS-2/CS-3 Schema Registry registration + CS-0 acknowledgment precedes CS-1 | Phase 1 CS-0 | -- |
| CA-1.9 | SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 slot | SE-4 STRUCTURED CLOSE | CA-1.4 (SE-0 ordering), CA-1.7 (MANUAL GAP labels) |
| CA-1.10 | Label-identity cross-scan: preamble Attestation Row Ref (A-N) matches attestation Preamble Row Ref (ATTEST-A-N) | Preamble axis table col 6 + attestation Preamble Row Ref col | CA-1.4, CA-1.7, CA-1.9 |

**R12 STRUCTURAL AXIS DECLARATION (authored by CA, Phase 0):**

This output activates three R12 structural dimensions. These dimensions are orthogonal: each
governs a structurally distinct property of the output, and activating one neither enables nor
exempts another. The non-interference contract is binding throughout execution.

| Row ID | R12 Criterion | Label | Structural Property Governed | CA Verification | Attestation Row Ref |
|--------|---------------|-------|------------------------------|-----------------|---------------------|
| A-1 | C-31 | Execution order | SE-0 before SE-1; Tier in TABLE_1/TABLE_3; SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference naming a specific TABLE_4 vector row | CA-1.4 (SE-0 ordering) + CA-1.9 (SE-0 slot cross-ref) | ATTEST-A-1 |
| A-2 | C-32 | Closure-note format | Exact-label two-part `MANUAL GAP [<exact label>]:` / `STRUCTURED CLOSE:` blocks at openings of SE-2, SE-3, and SE-4 | CA-1.7 | ATTEST-A-2 |
| A-3 | C-33 | CS self-reference | CS-0 sub-section cites CS-2 and CS-3 schema IDs by exact label and lists SE-updatable columns before CS-1/CS-2/CS-3 | CA-1.8 | ATTEST-A-3 |

**Non-interference statement:** A-1 governs SE section sequencing, TABLE column structure, and
SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot. A-2 governs the exact textual format of SE section
opening blocks (MANUAL GAP / STRUCTURED CLOSE). A-3 governs CS's Phase 1 opening sub-section
structure. No axis enforcement mechanism intersects with another's. Verifying CA-1.7 (A-2) does
not verify A-1 or A-3. Verifying CA-1.8 (A-3) does not verify A-1 or A-2. Verifying CA-1.4+CA-1.9
(A-1) does not verify A-2 or A-3. Each axis requires independent satisfaction.

**Bidirectional loop binding (C-40):** Attestation Row Ref column above pre-declares the
attestation table row label for each A-N row. CA-1.10 verifies label identity by cross-scan: for
each A-N row, preamble Attestation Row Ref = ATTEST-A-N and attestation row ATTEST-A-N Preamble
Row Ref = A-N. The cross-scan is auditable at the column level without semantic interpretation.

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A: Complete TABLE_1 with Tier column. Every cell Granted/Denied/Conditional/N/A. Rows ordered by tier.
- SHALL-B: TABLE_2 lists all PII, Financial, and Audit-Compliance fields with explicit FLS status. Null case explicit. Gap? YES rows in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier and Effective Scope filled. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 at SE-0 (before SE-1), all four vectors, Checked? = YES. Rule-outs name specific mechanism and reason. **SHALL-D extension [C-35]:** Additionally, SE-4's STRUCTURED CLOSE block SHALL carry a TABLE_4 row cross-reference at the SE-0 slot naming a specific TABLE_4 vector row by exact vector label. CA-1.9 verifies this sub-clause, distinct from CA-1.4 (SE-0 execution ordering).
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap case requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field Remediation block (CS-Expected, SE-Actual, Delta). Incomplete rows MUST be reopened. CA-1.6 verifies.
- SHALL-G: At the opening of SE-2, SE-3, and SE-4, closure MUST appear as a two-part labeled block -- Line 1: `MANUAL GAP [<exact CONTEXT label>]:` where the label is character-for-character as written in the CONTEXT section above; Line 2: description of what manual audits miss; Line 3: `STRUCTURED CLOSE:`; Line 4: closing mechanism. Exact label required; paraphrase fails. CA-1.7 verifies the MANUAL GAP block. CA-1.9 separately verifies the TABLE_4 SE-0 slot cross-reference inside SE-4's STRUCTURED CLOSE.

*Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

*CS opens with CS-0 Registry acknowledgment before authoring any expectation content.*

### CS-0 -- Schema Registry Acknowledgment (CS-authored, Phase 1)

CS echoes the Schema Registry entries for CS-2 and CS-3 from Phase 0 before authoring expectation
rows. This sub-section confirms the handoff from CA's Registry to CS's authoring task.

**Registry acknowledgment for CS-2:**
Schema ID: CS-2 -- Sharing Rule Expectations.
SE-updatable columns as declared by CA in Phase 0 Schema Registry: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged: SE populates SE Cross-Reference (TABLE_4 or TABLE_5 row ID)
and SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE) after SE-0/TABLE_4 analysis.
Expectation format confirmed. SE-updatable columns left blank by CS; SE fills after SE-0.

**Registry acknowledgment for CS-3:**
Schema ID: CS-3 -- Cross-Role Access Differential Expectations.
SE-updatable columns as declared by CA in Phase 0 Schema Registry: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged: SE populates SE Cross-Reference (TABLE_1 or TABLE_3 row ID)
and SE Confirmation after SE-1/SE-3 analysis. SE-updatable columns left blank by CS.

### CS-1 -- Expected Customer Service Access Baseline

For each entity in scope: (a) CRUD operations the CS role is expected to perform for normal job
function; (b) expected record scope; (c) sensitive fields CS needs and why. Identify configurations
that may inadvertently open access beyond job requirements.

**CS-2 -- Sharing rule expectations** *(Schema Registry CS-2; SE-updatable columns blank)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

For each Potential Overreach? YES: name the access path and the most likely over-reached role.

**CS-3 -- Cross-role access differential** *(Schema Registry CS-3; SE-updatable columns blank)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

At minimum one entity and one operation where CS has less access than the Comparison Role.

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis (Privilege-Tier Descent Order)

*SE-0 establishes admin-tier ceiling and TABLE_4 before SE-1. A-1 (execution order) active:
TABLE_4 at SE-0, Tier columns in TABLE_1/TABLE_3, SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot
cross-reference. A-2 (closure-note format) active: exact-label two-part MANUAL GAP / STRUCTURED
CLOSE blocks at SE-2/SE-3/SE-4 per SHALL-G. A-3 (CS self-reference) confirmed: CS-0 Registry
acknowledgment completed in Phase 1.*

### SE-0 -- Admin-Tier Inventory and Escalation Vectors (executes before TABLE_1)

**Admin-tier role inventory:** List System Administrator, Environment Admin, and admin-equivalent
roles with record scope and key capabilities. Note admin bypasses of lower-tier controls (e.g.,
System Administrator bypasses column security profiles). Establishes privilege ceiling.

**TABLE_4 -- Escalation Vector Inventory** *(Schema Registry TABLE_4; SE-0 placement per
SHALL-D and A-1; TABLE_1 rows interpreted relative to this ceiling)*

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Finding format: `[Role] -> [Mechanism] -> [Elevated access achieved]` for escalation; for
rule-out: "Checked [mechanism]: no path found because [specific reason]." After TABLE_4: populate
SE Cross-Reference and SE Confirmation in CS-2. Enter CONTRADICTED rows as CS-EXPECTATION-VIOLATED
in TABLE_5 per SHALL-F.

### SE-1 / SHALL-A -- Section 1: Role-Operation Matrix

**TABLE_1 -- Role-Operation Matrix** *(Schema Registry TABLE_1 with Tier; blank-cell rule)*

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Admin-tier rows first. Include every role with any privilege on any entity in {{topic}}.
After table: cross-reference CS-3 expectations. Cross-role differential: compare CS role against
one more privileged role; state whether differential is expected (least privilege satisfied).

### SE-2 / SHALL-B -- Section 2: Field-Level Security Coverage

MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:
Column security profiles are not auditable from the security roles UI; administrators discover
missing FLS only after a data exposure event reveals a sensitive field was readable by an unintended
role.

STRUCTURED CLOSE:
TABLE_2 below enumerates every sensitive field with its explicit FLS status, surfacing pre-event
what the security roles UI conceals. All Not Configured sensitive fields are forwarded to TABLE_5
as MISSING-FLS gaps.

**TABLE_2 -- FLS Coverage** *(Schema Registry TABLE_2; blank-cell rule)*

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Categories: PII / Financial / Audit-Compliance / Other-Sensitive. Null case: explicitly state
"No column security profiles active on {{topic}}." Defense-in-depth layer check: identify
enforcement layer for at least one sensitive field; note Admin-tier bypass from SE-0 if applicable.
After TABLE_2: update CS-3 SE Confirmation for any row where a sensitive field finding contradicts.

### SE-3 / SHALL-C -- Section 3: Record Access Scope

MANUAL GAP [Blind spot 2 -- Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access produced by a security role
plus owner team membership plus OWD; spot-checking individual roles misses team-accumulated
privilege accumulation.

STRUCTURED CLOSE:
TABLE_3 below maps effective scope for every role by Tier, recording OWD baseline, scope modifier,
and resulting effective scope, making team-accumulated privilege visible and auditable.

**TABLE_3 -- Record Scope by Role** *(Schema Registry TABLE_3 with Tier; blank-cell rule)*

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role MUST appear, ordered by Tier. Roles where effective scope exceeds role-only
scope due to team membership are CS-EXPECTATION-VIOLATED candidates. After TABLE_3: update CS-3.

### SE-4 / SHALL-D -- Section 4: Privilege Escalation Cross-Reference

MANUAL GAP [Blind spot 3 -- OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing sharing rules that
silently override them; a Private OWD combined with an active sharing rule can grant effective
org-wide access without appearing in any security roles UI view.

STRUCTURED CLOSE:
SE-0 cross-reference: TABLE_4 row [name the specific TABLE_4 vector row most relevant to
{{topic}}'s primary escalation surface -- cite exact vector label (e.g., "Team inheritance" or
"Sharing rules"), Checked? value, and the full Finding from SE-0 TABLE_4]. This TABLE_4 row
cross-reference occupies the SE-0 slot of this STRUCTURED CLOSE block and anchors the closure
note to a concrete SE-0 finding. It is the subject of CA-1.9 verification (SHALL-D [C-35]
extension sub-clause); it is distinct from the MANUAL GAP block above (CA-1.7's scope) and
from TABLE_4's execution order at SE-0 (CA-1.4's scope).
TABLE_4 (filled at SE-0) evaluated all four escalation vectors simultaneously. This section adds
the cross-tier differential: for the most privileged Admin-tier role and the most restricted
Restricted-tier role, identify the specific Dataverse enforcement layer where access diverges,
citing the TABLE_4 row named in the SE-0 slot above. State whether the divergence is expected.

### SE-5 / SHALL-E -- Section 5: Security Gap Inventory

**TABLE_5 -- Security Gap Inventory** *(Schema Registry TABLE_5; blank-cell rule)*

| # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation |
|---|----------|--------|---------------|------|------|----------|-------------|

Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED /
CS-EXPECTATION-VIOLATED. Severity: CRITICAL / HIGH / MEDIUM.

CS-EXPECTATION-VIOLATED rows (three-field Remediation block per SHALL-F):
- CS-Expected: [cite CS-2 or CS-3 row, state expectation verbatim or by row reference]
- SE-Actual: [SE finding that contradicts the expectation]
- Delta: [exact configuration change to align SE-Actual to CS-Expected]

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*CA returns. Each CA-1 row presents Registry anchor and Preamble anchor as structurally distinct
labeled elements before the Verification line. Inline concatenation fails C-24. CA-1.9 verifies
SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference (completing SHALL-D [C-35] extension
sub-clause) -- distinct from CA-1.4 (SE-0 ordering) and CA-1.7 (MANUAL GAP labels). CA-1.10
verifies label-identity cross-scan between preamble Attestation Row Ref column and attestation
Preamble Row Ref column -- distinct from CA-1.4, CA-1.7, CA-1.9.*

**CA-1.1 -- C-01 verification** *(Phase 0 M4 pre-assignment CA-1.1)*:
- Registry anchor -- Schema ID TABLE_1 (with Tier): [Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope] -- blank cells prohibited globally.
- Preamble anchor -- C-01 as authored by CA in Phase 0: TABLE_1 / SE-1 / SHALL-A / CA-1.1 -- verifying...
- Verification -- TABLE_1 present? Tier column populated? Rows ordered by tier? All cells filled? -> PASS / FAIL

**CA-1.2 -- C-02 verification** *(Phase 0 M4 pre-assignment CA-1.2)*:
- Registry anchor -- Schema ID TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?] -- blank cells prohibited globally.
- Preamble anchor -- C-02 as authored by CA in Phase 0: TABLE_2 / SE-2 / SHALL-B / CA-1.2 -- verifying...
- Verification -- TABLE_2 present? All sensitive fields? FLS status explicit? Null case stated? Gap? YES in TABLE_5? -> PASS / FAIL

**CA-1.3 -- C-03 verification** *(Phase 0 M4 pre-assignment CA-1.3)*:
- Registry anchor -- Schema ID TABLE_3 (with Tier): [Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Verified?] -- blank cells prohibited globally.
- Preamble anchor -- C-03 as authored by CA in Phase 0: TABLE_3 / SE-0+SE-3 / SHALL-C / CA-1.3 -- verifying...
- Verification -- Every TABLE_1 role in TABLE_3? Tier column populated? Effective Scope filled? -> PASS / FAIL

**CA-1.4 -- C-04 verification** *(Phase 0 M4 pre-assignment CA-1.4)*:
- Registry anchor -- Schema ID TABLE_4: [Vector, Checked?, Finding, Severity] -- all four vectors, Checked? = YES.
- Preamble anchor -- C-04 as authored by CA in Phase 0: TABLE_4 / SE-0 / SHALL-D / CA-1.4 -- verifying...
- Verification -- TABLE_4 at SE-0 (before SE-1)? All four vectors? Findings or specific rule-outs? -> PASS / FAIL
- Note: CA-1.4 verifies SE-0 execution ordering only. SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot content is CA-1.9's scope (SHALL-D [C-35] extension).

**CA-1.5 -- C-05 verification** *(Phase 0 M4 pre-assignment CA-1.5)*:
- Registry anchor -- Schema ID TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Tier, Severity, Remediation] -- blank cells prohibited globally.
- Preamble anchor -- C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 -- verifying...
- Verification -- TABLE_5 present? Named gap? Tier column populated? Remediations exact? -> PASS / FAIL

**CA-1.6 -- SHALL-F compliance verification** *(CS-EXPECTATION-VIOLATED three-field structure)*:
- Registry anchor -- Schema ID TABLE_5 CS-EXPECTATION-VIOLATED row structure: [CS-Expected, SE-Actual, Delta] -- all three required per SHALL-F.
- Preamble anchor -- SHALL-F as authored by CA in Phase 0: three-field Remediation block mandatory; rows missing any field MUST be reopened.
- Verification -- For each CS-EXPECTATION-VIOLATED row: CS-Expected populated? SE-Actual populated? Delta populated with exact configuration change? -> PASS / FAIL per row.

**CA-1.7 -- SHALL-G compliance verification** *(exact-label MANUAL GAP two-part closure blocks)*:
- Registry anchor -- CONTEXT section declared exact labels: "Blind spot 1 -- Post-incident FLS gap" (SE-2), "Blind spot 2 -- Cumulative privilege blind spot" (SE-3), "Blind spot 3 -- OWD-sharing-rule override gap" (SE-4). SHALL-G requires two-part blocks with exact label in brackets.
- Preamble anchor -- SHALL-G as authored by CA: Line 1 `MANUAL GAP [<exact label>]:`; exact = character-for-character; paraphrase fails. CA-1.7 verifies. Distinct from CA-1.9.
- Verification -- SE-2 opens with `MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:`? Followed by `STRUCTURED CLOSE:`? SE-3/SE-4 same pattern with exact labels? -> PASS / FAIL per section.
- Note: CA-1.7 verifies the MANUAL GAP block format only. TABLE_4 row cross-reference inside SE-4's STRUCTURED CLOSE is CA-1.9's scope.

**CA-1.8 -- CS-2/CS-3 Schema Registry registration + CS-0 acknowledgment** *(A-3 / C-33)*:
- Registry anchor -- Schema Registry declared CS-2 and CS-3 as named schema entries with SE-updatable columns and SE-update protocols co-located. PHASE 1 mandate requires CS-0 to acknowledge both schema IDs before CS-1/CS-2/CS-3.
- Preamble anchor -- CS-2 and CS-3 are Schema Registry entries. CS-0 acknowledgment is a PHASE 1 structural requirement per Axis A-3 (C-33) of the R12 Structural Axis Declaration.
- Verification -- CS-2 in Registry? CS-3 in Registry? CS-0 present before CS-1? CS-0 cites both schema IDs by exact label? CS-0 lists SE-updatable columns for both? SE populated SE-updatable columns? -> PASS / FAIL

**CA-1.9 -- SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 slot** *(C-35; completing
SHALL-D [C-35] extension sub-clause; distinct from CA-1.4 and CA-1.7)*:
- Registry anchor -- Schema ID TABLE_4: [Vector, Checked?, Finding, Severity]. Phase 0 Schema Registry declared: "SE-4's STRUCTURED CLOSE block SHALL carry a TABLE_4 row cross-reference at its SE-0 slot, naming a specific TABLE_4 vector row by its exact vector label."
- Preamble anchor -- Completing SHALL-D [C-35] extension sub-clause as authored by CA in Phase 0: "CA-1.9 verifies SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 slot | SE-4 STRUCTURED CLOSE | Distinct from CA-1.4 (SE-0 ordering), CA-1.7 (MANUAL GAP labels)."
- Verification -- SE-4's STRUCTURED CLOSE block begins with an SE-0 slot entry naming a specific TABLE_4 vector row by its exact vector label? That row was populated at SE-0 with Checked?=YES and a non-blank Finding? The cross-reference is inside the STRUCTURED CLOSE block (not in the MANUAL GAP block, not in TABLE_5)? -> PASS / FAIL
- Distinction confirmed: CA-1.4 verified TABLE_4 appeared at SE-0 before TABLE_1. CA-1.7 verified the MANUAL GAP exact-label blocks. CA-1.9 verifies the TABLE_4 row cross-reference inside SE-4's STRUCTURED CLOSE.

**CA-1.10 -- Bidirectional loop label-identity cross-scan** *(Phase 0 pre-assignment CA-1.10;
completing bidirectional loop binding declared in Phase 0 R12 Structural Axis Declaration)*:
- Registry anchor -- R12 Structural Axis Declaration col 6 "Attestation Row Ref": A-1 -> ATTEST-A-1; A-2 -> ATTEST-A-2; A-3 -> ATTEST-A-3. No blank cells per global blank-cell rule.
- Preamble anchor -- CA-1.10 pre-assigned (supplementary rows, Phase 0): "Label-identity cross-scan: preamble Attestation Row Ref (A-N) matches attestation Preamble Row Ref (ATTEST-A-N) | Preamble axis table col 6 + attestation table Preamble Row Ref col | Distinct from CA-1.4, CA-1.7, CA-1.9."
- Verification -- Cross-scan result for each row:
  - A-1: preamble Attestation Row Ref = ATTEST-A-1; attestation row ATTEST-A-1 Preamble Row Ref = A-1. Label pair consistent? -> PASS / FAIL
  - A-2: preamble Attestation Row Ref = ATTEST-A-2; attestation row ATTEST-A-2 Preamble Row Ref = A-2. Label pair consistent? -> PASS / FAIL
  - A-3: preamble Attestation Row Ref = ATTEST-A-3; attestation row ATTEST-A-3 Preamble Row Ref = A-3. Label pair consistent? -> PASS / FAIL
  - Overall loop integrity: all three label pairs consistent? -> PASS / FAIL
- Distinction confirmed: CA-1.4 verified SE-0 execution ordering. CA-1.7 verified MANUAL GAP format. CA-1.9 verified SE-4 STRUCTURED CLOSE SE-0 slot content. CA-1.10 verifies the label consistency between preamble axis col 6 and attestation Preamble Row Ref col -- a fourth non-overlapping audit target.

**CA Format Compliance Verdict -- Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0),
R12 Structural Axis Declaration with A-1/A-2/A-3 Row IDs and Attestation Row Ref column
(Step 0.2, Phase 0), Phase 0 by label.
[CA-1.1 through CA-1.10 results. A-1 verified by CA-1.4+CA-1.9. A-2 verified by CA-1.7.
A-3 verified by CA-1.8. Bidirectional loop label-identity verified by CA-1.10.
Non-interference contract: all three axes independently verified. Loop integrity confirmed.
Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

**TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION (R12 axes, authored by CA in terminal verdict):**

| Row ID | R12 Dimension | Axis Label | Specific Output-Body Evidence Source | Preamble Row Ref | Status |
|--------|---------------|------------|--------------------------------------|-----------------|--------|
| ATTEST-A-1 | C-31 (Preamble Row A-1) | Execution order | Phase 2 output body: SE-0 section header precedes SE-1; TABLE_4 appears in SE-0 before TABLE_1; TABLE_1 and TABLE_3 contain Tier column; SE-4 STRUCTURED CLOSE contains SE-0 slot entry naming a specific TABLE_4 vector row by exact label (CA-1.9). | A-1 | CONFIRMED |
| ATTEST-A-2 | C-32 (Preamble Row A-2) | Closure-note format | Phase 2 output body: SE-2 opens with `MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:` followed by `STRUCTURED CLOSE:`; SE-3 and SE-4 same pattern with exact labels from CONTEXT. Verified by CA-1.7. | A-2 | CONFIRMED |
| ATTEST-A-3 | C-33 (Preamble Row A-3) | CS self-reference | Phase 1 output body: CS-0 sub-section before CS-1; CS-0 cites Schema ID CS-2 and Schema ID CS-3 by exact label; CS-0 lists SE Cross-Reference and SE Confirmation as SE-updatable columns. Verified by CA-1.8. | A-3 | CONFIRMED |

All three axes simultaneously active. Preamble Row Ref column back-references each ATTEST-A-N row
to its A-N declaration in the Phase 0 preamble. CA-1.10 confirmed label identity by cross-scan.
Non-interference manifestation: A-1 evidence in SE-0/TABLE_1/TABLE_3/SE-4 STRUCTURED CLOSE; A-2
evidence in SE-2/SE-3/SE-4 opening blocks; A-3 evidence in CS-0. No evidence source overlaps.

---

## V-02 -- Single-Axis C-41: ATTEST-TBL Schema in Schema Registry

**Axis:** C-41 -- Schema Registry Step 0.1 gains ATTEST-TBL: the pre-declared schema entry for
the TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION table, naming its column structure (including the
Preamble Row Ref back-column) and blank-cell rule. The terminal verdict CA verification in Phase 3
opens with a double-anchor citing ATTEST-TBL. This extends the Schema Registry's governance to
the attestation table itself. All other R14-V-05 architecture preserved; no CA-1.10 added (that
is C-40's scope).
**Hypothesis:** 32/34 (adds C-41; C-40 and C-42 remain open).

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

*(Identical to V-01 -- full three Blind spot paragraphs with exact labels preserved.)*

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins.

**PHASE 0 -- CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1: eight schemas -- TABLE_1 through TABLE_5
with Tier columns on TABLE_1 and TABLE_3; CS-2 and CS-3 with SE-updatable columns and update
protocols; TABLE_4 schema note declares SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot requirement;
ATTEST-TBL declaring the TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION table schema) and the
Criterion Enforcement Matrix preamble (Step 0.2: SHALL-A through SHALL-G with SHALL-D extension
sub-clause for C-35; M4 CA-1.1 through CA-1.9 pre-assigned; R12 Structural Axis Declaration with
A-1/A-2/A-3 Row IDs, Attestation Row Ref column (ATTEST-A-1/A-2/A-3), and non-interference
statement). CA issues handoff to PHASE 1.

**PHASE 1 -- CS (Customer Success):**
*(Identical to V-01 PHASE 1 mandate.)*

**PHASE 2 -- SE (Security Engineer / Dataverse Security Expert):**
*(Identical to V-01 PHASE 2 mandate.)*

**PHASE 3 -- CA-1 (CA Verification Pass):**
CA returns. Double-anchor reaffirmation per row. CA-1.8 verifies CS-0 precedes CS-1. CA-1.9
verifies SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference (distinct from CA-1.4 and
CA-1.7). Terminal verdict TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION table verification opens with
Schema Registry anchor citing ATTEST-TBL schema before preamble anchor. Terminal verdict includes
TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION with ATTEST-A-N Row IDs and Preamble Row Ref
back-column.

---

## PHASE 0 -- CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1 and 0.2 before any other phase begins.*

### Step 0.1 -- Schema Registry (CA-authored, Phase 0)

**All table schemas declared centrally by CA. Blank-cell prohibition is global.**

*(Schema IDs TABLE_1 through TABLE_5, CS-2, CS-3 -- identical to V-01 Step 0.1 in full, including
all declared columns, Tier specifications, blank-cell rules, TABLE_4 SE-0 slot note, CS-2/CS-3
SE-update protocols.)*

**Schema ID: ATTEST-TBL -- TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION**
Declared columns: `Row ID | R12 Dimension | Axis Label | Specific Output-Body Evidence Source | Preamble Row Ref | Status`
Row ID values: ATTEST-A-1, ATTEST-A-2, ATTEST-A-3 (pre-assigned by CA-authored preamble axis
Attestation Row Ref column). Preamble Row Ref values: A-1, A-2, A-3. Status: CONFIRMED / FAILED.
Blank-cell rule: all cells filled; Evidence Source must name a specific section or table in the
output body; Preamble Row Ref must match the A-N value declared in the preamble axis table
Attestation Row Ref column for this row.

### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

*(Identical to V-01 Step 0.2 in full -- five-row criterion matrix, supplementary CA-1.6 through
CA-1.9 rows (no CA-1.10 in V-02), R12 Structural Axis Declaration with A-1/A-2/A-3 Row IDs and
Attestation Row Ref column, non-interference statement, bidirectional loop binding note, and
SHALL-A through SHALL-G obligations.)*

*Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

*(Identical to V-01 PHASE 1 in full -- CS-0 acknowledgment citing CS-2 and CS-3 by exact Schema
ID; CS-1 baseline; CS-2 sharing rule expectations table; CS-3 cross-role differential table.)*

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis (Privilege-Tier Descent Order)

*(Identical to V-01 PHASE 2 in full -- SE-0 admin inventory + TABLE_4; SE-1 TABLE_1; SE-2 TABLE_2
with MANUAL GAP [Blind spot 1 -- Post-incident FLS gap] + STRUCTURED CLOSE; SE-3 TABLE_3 with
MANUAL GAP [Blind spot 2 -- Cumulative privilege blind spot] + STRUCTURED CLOSE; SE-4 with MANUAL
GAP [Blind spot 3 -- OWD-sharing-rule override gap] + STRUCTURED CLOSE with SE-0 TABLE_4 slot
cross-reference; SE-5 TABLE_5.)*

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*CA returns. Each CA-1 row: Registry anchor then Preamble anchor then Verification line. CA-1.9
verifies SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot. No CA-1.10 in V-02 (C-40 is separate axis).*

*(CA-1.1 through CA-1.9 -- identical to V-01 in full.)*

**CA Format Compliance Verdict -- Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0, eight schemas including ATTEST-TBL),
CA-authored preamble (Step 0.2, Phase 0), R12 Structural Axis Declaration with A-1/A-2/A-3 Row
IDs and Attestation Row Ref column (Step 0.2, Phase 0), Phase 0 by label.
[CA-1.1 through CA-1.9 results. A-1/A-2/A-3 verified per standard. ATTEST-TBL schema governs
the attestation table below. Overall: COMPLIANT / NON-COMPLIANT.]

**TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION verification** *(ATTEST-TBL governed)*:
- Registry anchor -- Schema ID ATTEST-TBL: [Row ID, R12 Dimension, Axis Label, Specific Output-Body Evidence Source, Preamble Row Ref, Status] -- blank cells prohibited globally; Preamble Row Ref must match A-N value from preamble axis Attestation Row Ref column.
- Preamble anchor -- R12 Structural Axis Declaration as authored by CA in Phase 0: A-1 Attestation Row Ref = ATTEST-A-1; A-2 Attestation Row Ref = ATTEST-A-2; A-3 Attestation Row Ref = ATTEST-A-3.
- Verification -- Attestation table present? Row IDs = ATTEST-A-1/A-2/A-3? Each Preamble Row Ref matches corresponding A-N axis row? All Evidence Source cells name specific output-body sections? Status = CONFIRMED for all three? -> PASS / FAIL

**TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION (R12 axes, governed by Schema ID ATTEST-TBL):**

| Row ID | R12 Dimension | Axis Label | Specific Output-Body Evidence Source | Preamble Row Ref | Status |
|--------|---------------|------------|--------------------------------------|-----------------|--------|
| ATTEST-A-1 | C-31 (Preamble Row A-1) | Execution order | Phase 2 output body: SE-0 precedes SE-1; TABLE_4 in SE-0 before TABLE_1; Tier columns in TABLE_1/TABLE_3; SE-4 STRUCTURED CLOSE SE-0 slot names specific TABLE_4 vector row (CA-1.9). | A-1 | CONFIRMED |
| ATTEST-A-2 | C-32 (Preamble Row A-2) | Closure-note format | Phase 2 output body: SE-2/SE-3/SE-4 open with exact-label MANUAL GAP / STRUCTURED CLOSE two-part blocks (CA-1.7). | A-2 | CONFIRMED |
| ATTEST-A-3 | C-33 (Preamble Row A-3) | CS self-reference | Phase 1 output body: CS-0 before CS-1; CS-0 cites Schema ID CS-2 and Schema ID CS-3 by exact label and lists SE-updatable columns (CA-1.8). | A-3 | CONFIRMED |

---

## V-03 -- Single-Axis C-42: Phase 0 Artifact Manifest

**Axis:** C-42 -- Phase 0 gains Step 0.3: Phase 0 Artifact Manifest. CA produces a numbered
manifest listing all Phase 0 authored artifacts by category before the handoff string: Schema IDs
(by exact ID), preamble criterion rows (by C-NN), SHALL obligations (by letter), supplementary
CA-1.N rows (by ID), and A-N axis declaration rows (by ID). CA's terminal verdict cites the
manifest by section item counts. Phase 0 mandate updated to name Step 0.3. No CA-1.10 (C-40's
scope) and no ATTEST-TBL schema (C-41's scope).
**Hypothesis:** 32/34 (adds C-42; C-40 and C-41 remain open).

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

*(Identical to V-01 -- full three Blind spot paragraphs with exact labels preserved.)*

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins.

**PHASE 0 -- CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1: seven schemas) and the Criterion
Enforcement Matrix preamble (Step 0.2: SHALL-A through SHALL-G with SHALL-D extension sub-clause;
M4 CA-1.1 through CA-1.9 pre-assigned; R12 Structural Axis Declaration with A-1/A-2/A-3 Row IDs,
Attestation Row Ref column, and non-interference statement). Step 0.3: Phase 0 Artifact Manifest
-- CA produces a numbered manifest listing all Step 0.1 Schema IDs and all Step 0.2 structural
contract elements before the PHASE 1 handoff string. CA issues handoff to PHASE 1.

**PHASE 1 -- CS (Customer Success):**
*(Identical to V-01 PHASE 1 mandate.)*

**PHASE 2 -- SE (Security Engineer / Dataverse Security Expert):**
*(Identical to V-01 PHASE 2 mandate.)*

**PHASE 3 -- CA-1 (CA Verification Pass):**
CA returns. Double-anchor reaffirmation per row. CA-1.8 verifies CS-0 precedes CS-1. CA-1.9
verifies SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference (distinct from CA-1.4 and
CA-1.7). Terminal verdict includes TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION with ATTEST-A-N Row
IDs and Preamble Row Ref back-column. Terminal verdict closes with Phase 0 Manifest Citation:
item counts per manifest category confirming all declared artifacts were exercised.

---

## PHASE 0 -- CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1, 0.2, and 0.3 before any other phase begins.*

### Step 0.1 -- Schema Registry (CA-authored, Phase 0)

*(Identical to V-01 Step 0.1 in full -- TABLE_1 through TABLE_5, CS-2, CS-3.)*

### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

*(Identical to V-01 Step 0.2 in full -- five-row criterion matrix, supplementary CA-1.6 through
CA-1.9 rows, R12 Structural Axis Declaration with A-1/A-2/A-3 Row IDs and Attestation Row Ref
column (ATTEST-A-1/A-2/A-3), non-interference statement, bidirectional loop binding note, and
SHALL-A through SHALL-G obligations.)*

### Step 0.3 -- Phase 0 Artifact Manifest (CA-authored, Phase 0)

CA produces a numbered manifest of all structural artifacts authored in Steps 0.1 and 0.2. This
manifest is the authoritative record of Phase 0 authorship. CA's terminal verdict in Phase 3 cites
this manifest by item counts.

**Section A -- Schema Registry entries (Step 0.1):**
1. TABLE_1 -- Role-Operation Matrix
2. TABLE_2 -- FLS Coverage
3. TABLE_3 -- Record Scope by Role
4. TABLE_4 -- Escalation Vector Inventory
5. TABLE_5 -- Security Gap Inventory
6. CS-2 -- Sharing Rule Expectations
7. CS-3 -- Cross-Role Access Differential Expectations
Total Schema IDs authored: 7

**Section B -- Criterion Enforcement Matrix rows (Step 0.2):**
C-01, C-02, C-03, C-04, C-05
Total criterion rows authored: 5

**Section C -- SHALL obligation letters (Step 0.2):**
SHALL-A, SHALL-B, SHALL-C, SHALL-D (with [C-35] extension sub-clause), SHALL-E, SHALL-F, SHALL-G
Total SHALL obligations authored: 7

**Section D -- Supplementary CA verification rows (Step 0.2):**
CA-1.6, CA-1.7, CA-1.8, CA-1.9
Total supplementary CA-1.N rows authored: 4

**Section E -- R12 Structural Axis Declaration rows (Step 0.2):**
A-1 (C-31, Execution order, ATTEST-A-1), A-2 (C-32, Closure-note format, ATTEST-A-2), A-3 (C-33, CS self-reference, ATTEST-A-3)
Total axis rows authored: 3

Manifest totals: 7 schemas / 5 criterion rows / 7 SHALL obligations / 4 CA-1.N rows / 3 axis rows.
This manifest is cited in the Phase 3 terminal verdict to confirm all declared artifacts were
exercised during execution.

*Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

*(Identical to V-01 PHASE 1 in full.)*

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis (Privilege-Tier Descent Order)

*(Identical to V-01 PHASE 2 in full.)*

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*CA returns. Each CA-1 row: Registry anchor then Preamble anchor then Verification line. CA-1.9
verifies SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot. No CA-1.10 in V-03.*

*(CA-1.1 through CA-1.9 -- identical to V-01 in full.)*

**CA Format Compliance Verdict -- Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0),
Phase 0 Artifact Manifest (Step 0.3, Phase 0), Phase 0 by label.
[CA-1.1 through CA-1.9 results. A-1/A-2/A-3 verified per standard. Overall: COMPLIANT /
NON-COMPLIANT. Open items attributed to responsible role.]

**Phase 0 Manifest Citation:**
Phase 0 Artifact Manifest (Step 0.3) declared: 7 schemas / 5 criterion rows / 7 SHALL obligations
/ 4 CA-1.N rows / 3 axis rows. Confirmation that all declared artifacts were exercised:
- 7 schemas: TABLE_1 exercised at SE-1; TABLE_2 at SE-2; TABLE_3 at SE-3; TABLE_4 at SE-0;
  TABLE_5 at SE-5; CS-2 at CS-1+SE-0; CS-3 at CS-1+SE-1. All 7 exercised.
- 5 criterion rows: C-01 through C-05 verified by CA-1.1 through CA-1.5. All 5 exercised.
- 7 SHALL obligations: SHALL-A through SHALL-G (including SHALL-D [C-35] extension) verified by
  CA-1.1 through CA-1.9. All 7 exercised.
- 4 CA-1.N supplementary rows: CA-1.6 through CA-1.9 executed in Phase 3. All 4 exercised.
- 3 axis rows: A-1 verified by CA-1.4+CA-1.9; A-2 by CA-1.7; A-3 by CA-1.8. All 3 exercised.
Manifest citation complete. All declared Phase 0 artifacts confirmed exercised.

**TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION (R12 axes, authored by CA in terminal verdict):**

*(Identical to V-01 attestation table in full -- ATTEST-A-1/A-2/A-3 Row IDs, full evidence
sources, Preamble Row Ref back-column with A-1/A-2/A-3 values, CONFIRMED status.)*

---

## V-04 -- C-40 + C-41 Combined: CA-1.10 Cross-Scan + ATTEST-TBL Schema

**Axis:** C-40 + C-41 combined. ATTEST-TBL schema in Schema Registry Step 0.1 (C-41). CA-1.10
supplementary row added (C-40). CA-1.10's Registry anchor cites ATTEST-TBL, unifying the Schema
Registry governance and the label-identity cross-scan into a single CA-1.10 double-anchor row
that is simultaneously a C-41 schema citation and a C-40 verification step. No Phase 0 Artifact
Manifest (C-42 remains open).
**Hypothesis:** 33/34 (adds C-40 and C-41; C-42 remains open).

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

*(Identical to V-01 -- full three Blind spot paragraphs with exact labels preserved.)*

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins.

**PHASE 0 -- CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1: eight schemas -- TABLE_1 through TABLE_5
with Tier columns; CS-2 and CS-3 with SE-updatable columns; TABLE_4 schema note for SE-4
STRUCTURED CLOSE SE-0 slot requirement; ATTEST-TBL for the TRI-DIMENSIONAL SELF-EVIDENCE
ATTESTATION table) and the Criterion Enforcement Matrix preamble (Step 0.2: SHALL-A through
SHALL-G with SHALL-D extension for C-35; M4 CA-1.1 through CA-1.10 pre-assigned; R12 Structural
Axis Declaration with A-1/A-2/A-3 Row IDs, Attestation Row Ref column (ATTEST-A-1/A-2/A-3), and
non-interference statement). CA issues handoff to PHASE 1.

**PHASE 1 -- CS (Customer Success):**
*(Identical to V-01 PHASE 1 mandate.)*

**PHASE 2 -- SE (Security Engineer / Dataverse Security Expert):**
*(Identical to V-01 PHASE 2 mandate.)*

**PHASE 3 -- CA-1 (CA Verification Pass):**
CA returns. Double-anchor reaffirmation per row. CA-1.8 verifies CS-0 precedes CS-1. CA-1.9
verifies SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference (distinct from CA-1.4 and
CA-1.7). CA-1.10 performs double-anchor label-identity cross-scan: Registry anchor cites ATTEST-TBL
schema from Step 0.1; Preamble anchor cites Phase 0 CA-1.10 pre-assignment; Verification confirms
each A-N Attestation Row Ref = ATTEST-A-N matches corresponding attestation Preamble Row Ref = A-N.
Terminal verdict includes TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION governed by ATTEST-TBL.

---

## PHASE 0 -- CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1 and 0.2 before any other phase begins.*

### Step 0.1 -- Schema Registry (CA-authored, Phase 0)

*(Schema IDs TABLE_1 through TABLE_5, CS-2, CS-3 -- identical to V-01 Step 0.1 in full.)*

**Schema ID: ATTEST-TBL -- TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION**
Declared columns: `Row ID | R12 Dimension | Axis Label | Specific Output-Body Evidence Source | Preamble Row Ref | Status`
Row ID values: ATTEST-A-1, ATTEST-A-2, ATTEST-A-3 (pre-assigned by preamble axis Attestation Row
Ref column). Preamble Row Ref values: A-1, A-2, A-3. Status: CONFIRMED / FAILED.
Blank-cell rule: all cells filled; Evidence Source names a specific output-body section or table;
Preamble Row Ref matches the A-N value in the preamble axis Attestation Row Ref column for this row.
CA-1.10 verifies this schema is satisfied and that Preamble Row Ref values are label-consistent
with the preamble axis table Attestation Row Ref column (bidirectional loop verification).

### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: M1, M2, M3 simultaneously active. M4 pre-assigned.**

*(Five-row criterion matrix C-01 through C-05 -- identical to V-01 Step 0.2.)*

**Supplementary CA verification rows (Phase 0 pre-assignment):**

| Row ID | What it verifies | Scope | Distinct from |
|--------|-----------------|-------|---------------|
| CA-1.6 | SHALL-F CS-EXPECTATION-VIOLATED three-field structure | TABLE_5 CS-EV rows | -- |
| CA-1.7 | SHALL-G exact-label MANUAL GAP two-part blocks at SE-2/SE-3/SE-4 | SE-2, SE-3, SE-4 openings | CA-1.9 |
| CA-1.8 | CS-2/CS-3 Schema Registry registration + CS-0 acknowledgment precedes CS-1 | Phase 1 CS-0 | -- |
| CA-1.9 | SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 slot | SE-4 STRUCTURED CLOSE | CA-1.4 (SE-0 ordering), CA-1.7 (MANUAL GAP labels) |
| CA-1.10 | Double-anchor: ATTEST-TBL schema (Registry) + label-identity cross-scan (Preamble): preamble A-N Attestation Row Ref = ATTEST-A-N matches attestation ATTEST-A-N Preamble Row Ref = A-N | ATTEST-TBL schema compliance + preamble axis col 6 + attestation Preamble Row Ref col | CA-1.4, CA-1.7, CA-1.9 |

*(R12 Structural Axis Declaration with A-1/A-2/A-3 Row IDs and Attestation Row Ref column
(ATTEST-A-1/A-2/A-3), non-interference statement, bidirectional loop binding note, and
SHALL-A through SHALL-G obligations -- identical to V-01 Step 0.2 in full.)*

*Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

*(Identical to V-01 PHASE 1 in full.)*

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis (Privilege-Tier Descent Order)

*(Identical to V-01 PHASE 2 in full.)*

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*CA returns. Each CA-1 row: Registry anchor then Preamble anchor then Verification line. CA-1.9
verifies SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot. CA-1.10 performs double-anchor label-identity
cross-scan citing ATTEST-TBL.*

*(CA-1.1 through CA-1.9 -- identical to V-01 in full.)*

**CA-1.10 -- ATTEST-TBL schema compliance + bidirectional loop label-identity cross-scan**
*(Phase 0 pre-assignment CA-1.10; double-anchor integrates Schema Registry ATTEST-TBL and
preamble CA-1.10 supplementary row pre-assignment)*:
- Registry anchor -- Schema ID ATTEST-TBL: declared columns [Row ID, R12 Dimension, Axis Label, Specific Output-Body Evidence Source, Preamble Row Ref, Status]. Blank-cell rule: all cells filled. Preamble Row Ref must match A-N value from preamble axis Attestation Row Ref column for this row. CA-1.10 verifies schema compliance and bidirectional label consistency.
- Preamble anchor -- CA-1.10 pre-assigned (supplementary rows, Phase 0): "Double-anchor: ATTEST-TBL schema (Registry) + label-identity cross-scan (Preamble): preamble A-N Attestation Row Ref = ATTEST-A-N matches attestation ATTEST-A-N Preamble Row Ref = A-N | ATTEST-TBL schema compliance + preamble axis col 6 + attestation Preamble Row Ref col | Distinct from CA-1.4, CA-1.7, CA-1.9."
- Verification -- ATTEST-TBL schema satisfied (6 columns present, no blank cells, Status = CONFIRMED for all rows)? Cross-scan:
  - A-1: preamble Attestation Row Ref = ATTEST-A-1; attestation ATTEST-A-1 Preamble Row Ref = A-1. Consistent? -> PASS / FAIL
  - A-2: preamble Attestation Row Ref = ATTEST-A-2; attestation ATTEST-A-2 Preamble Row Ref = A-2. Consistent? -> PASS / FAIL
  - A-3: preamble Attestation Row Ref = ATTEST-A-3; attestation ATTEST-A-3 Preamble Row Ref = A-3. Consistent? -> PASS / FAIL
  - Overall: ATTEST-TBL schema compliant + all three label pairs consistent? -> PASS / FAIL
- Distinction confirmed: CA-1.4 verified SE-0 ordering. CA-1.7 verified MANUAL GAP format. CA-1.9 verified SE-4 STRUCTURED CLOSE SE-0 slot. CA-1.10 verifies ATTEST-TBL schema compliance and preamble-attestation label identity -- a fourth non-overlapping audit target.

**CA Format Compliance Verdict -- Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0, eight schemas including ATTEST-TBL),
CA-authored preamble (Step 0.2, Phase 0), R12 Structural Axis Declaration with A-1/A-2/A-3 and
Attestation Row Ref column (Step 0.2, Phase 0), Phase 0 by label.
[CA-1.1 through CA-1.10 results. A-1 verified by CA-1.4+CA-1.9. A-2 by CA-1.7. A-3 by CA-1.8.
ATTEST-TBL schema compliance and bidirectional loop label-identity verified by CA-1.10.
Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

**TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION** *(governed by Schema ID ATTEST-TBL; verified by CA-1.10)*:

| Row ID | R12 Dimension | Axis Label | Specific Output-Body Evidence Source | Preamble Row Ref | Status |
|--------|---------------|------------|--------------------------------------|-----------------|--------|
| ATTEST-A-1 | C-31 (Preamble Row A-1) | Execution order | Phase 2 output body: SE-0 precedes SE-1; TABLE_4 in SE-0 before TABLE_1; Tier columns in TABLE_1/TABLE_3; SE-4 STRUCTURED CLOSE SE-0 slot names specific TABLE_4 vector row (CA-1.9). | A-1 | CONFIRMED |
| ATTEST-A-2 | C-32 (Preamble Row A-2) | Closure-note format | Phase 2 output body: SE-2/SE-3/SE-4 open with exact-label MANUAL GAP / STRUCTURED CLOSE two-part blocks (CA-1.7). | A-2 | CONFIRMED |
| ATTEST-A-3 | C-33 (Preamble Row A-3) | CS self-reference | Phase 1 output body: CS-0 before CS-1; CS-0 cites Schema ID CS-2 and Schema ID CS-3 by exact label and lists SE-updatable columns (CA-1.8). | A-3 | CONFIRMED |

---

## V-05 -- Full Canonical: C-40 + C-41 + C-42

**Axis:** C-40 + C-41 + C-42 simultaneously. ATTEST-TBL schema in Registry (C-41) + CA-1.10
double-anchor label-identity cross-scan citing ATTEST-TBL (C-40) + Phase 0 Artifact Manifest
in Step 0.3 with terminal manifest citation (C-42). This is the canonical path to 34/34 under v14.
**Hypothesis:** 34/34.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

*(Identical to V-01 -- full three Blind spot paragraphs with exact labels preserved.)*

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins.

**PHASE 0 -- CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1: eight schemas -- TABLE_1 through TABLE_5
with Tier columns on TABLE_1 and TABLE_3; CS-2 and CS-3 with SE-updatable columns and update
protocols; TABLE_4 schema note for SE-4 STRUCTURED CLOSE SE-0 slot requirement; ATTEST-TBL for
the TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION table) and the Criterion Enforcement Matrix preamble
(Step 0.2: SHALL-A through SHALL-G with SHALL-D extension sub-clause for C-35; M4 CA-1.1 through
CA-1.10 pre-assigned; R12 Structural Axis Declaration with A-1/A-2/A-3 Row IDs, Attestation Row
Ref column (ATTEST-A-1/A-2/A-3), and non-interference statement) and the Phase 0 Artifact Manifest
(Step 0.3: numbered manifest of all Step 0.1 Schema IDs and Step 0.2 structural contract elements).
CA issues handoff to PHASE 1.

**PHASE 1 -- CS (Customer Success):**
*(Identical to V-01 PHASE 1 mandate.)*

**PHASE 2 -- SE (Security Engineer / Dataverse Security Expert):**
*(Identical to V-01 PHASE 2 mandate.)*

**PHASE 3 -- CA-1 (CA Verification Pass):**
CA returns. Double-anchor reaffirmation per row. CA-1.8 verifies CS-0 precedes CS-1. CA-1.9
verifies SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference (distinct from CA-1.4 and
CA-1.7). CA-1.10 performs double-anchor label-identity cross-scan: Registry anchor cites ATTEST-TBL;
Preamble anchor cites Phase 0 CA-1.10 pre-assignment; Verification confirms per-row label
consistency. Terminal verdict includes TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION governed by
ATTEST-TBL, followed by Phase 0 Manifest Citation confirming all declared artifacts were exercised.

---

## PHASE 0 -- CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1, 0.2, and 0.3 before any other phase begins.*

### Step 0.1 -- Schema Registry (CA-authored, Phase 0)

**All table schemas declared centrally by CA. Blank-cell prohibition is global. SE-update
protocols for CS-2 and CS-3 declared co-located with schema entry.**

*(Schema IDs TABLE_1 through TABLE_5, CS-2, CS-3 -- identical to V-01 Step 0.1 in full, including
all declared columns, Tier specifications, blank-cell rules, TABLE_4 SE-0 slot note, CS-2/CS-3
SE-update protocols.)*

**Schema ID: ATTEST-TBL -- TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION**
Declared columns: `Row ID | R12 Dimension | Axis Label | Specific Output-Body Evidence Source | Preamble Row Ref | Status`
Row ID values: ATTEST-A-1, ATTEST-A-2, ATTEST-A-3 (pre-assigned by preamble axis Attestation Row
Ref column). Preamble Row Ref values: A-1, A-2, A-3. Status: CONFIRMED / FAILED.
Blank-cell rule: all cells filled; Evidence Source names a specific output-body section or table;
Preamble Row Ref matches the A-N value in the preamble axis Attestation Row Ref column for this row.
CA-1.10 verifies this schema is satisfied and that Preamble Row Ref values are label-consistent
with the preamble axis Attestation Row Ref column (bidirectional loop verification).

### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: M1, M2, M3 simultaneously active. M4 pre-assigned.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-0 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**Supplementary CA verification rows (Phase 0 pre-assignment):**

| Row ID | What it verifies | Scope | Distinct from |
|--------|-----------------|-------|---------------|
| CA-1.6 | SHALL-F CS-EXPECTATION-VIOLATED three-field structure | TABLE_5 CS-EV rows | -- |
| CA-1.7 | SHALL-G exact-label MANUAL GAP two-part blocks at SE-2/SE-3/SE-4 | SE-2, SE-3, SE-4 openings | CA-1.9 |
| CA-1.8 | CS-2/CS-3 Schema Registry registration + CS-0 acknowledgment precedes CS-1 | Phase 1 CS-0 | -- |
| CA-1.9 | SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 slot | SE-4 STRUCTURED CLOSE | CA-1.4 (SE-0 ordering), CA-1.7 (MANUAL GAP labels) |
| CA-1.10 | Double-anchor: ATTEST-TBL schema (Registry) + label-identity cross-scan (Preamble): preamble A-N Attestation Row Ref = ATTEST-A-N matches attestation ATTEST-A-N Preamble Row Ref = A-N | ATTEST-TBL schema compliance + preamble axis col 6 + attestation Preamble Row Ref col | CA-1.4, CA-1.7, CA-1.9 |

**R12 STRUCTURAL AXIS DECLARATION (authored by CA, Phase 0):**

This output activates three R12 structural dimensions. These dimensions are orthogonal: each
governs a structurally distinct property of the output, and activating one neither enables nor
exempts another. The non-interference contract is binding throughout execution.

| Row ID | R12 Criterion | Label | Structural Property Governed | CA Verification | Attestation Row Ref |
|--------|---------------|-------|------------------------------|-----------------|---------------------|
| A-1 | C-31 | Execution order | SE-0 before SE-1; Tier in TABLE_1/TABLE_3; SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference naming a specific TABLE_4 vector row | CA-1.4 (SE-0 ordering) + CA-1.9 (SE-0 slot cross-ref) | ATTEST-A-1 |
| A-2 | C-32 | Closure-note format | Exact-label two-part `MANUAL GAP [<exact label>]:` / `STRUCTURED CLOSE:` blocks at openings of SE-2, SE-3, and SE-4 | CA-1.7 | ATTEST-A-2 |
| A-3 | C-33 | CS self-reference | CS-0 sub-section cites CS-2 and CS-3 schema IDs by exact label and lists SE-updatable columns before CS-1/CS-2/CS-3 | CA-1.8 | ATTEST-A-3 |

**Non-interference statement:** A-1 governs SE section sequencing, TABLE column structure, and
SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot. A-2 governs exact textual format of SE section opening
blocks. A-3 governs CS's Phase 1 opening sub-section structure. No axis enforcement mechanism
intersects with another's. Each axis requires independent satisfaction.

**Bidirectional loop binding (C-40):** Attestation Row Ref column above pre-declares the
attestation table row label for each A-N row. CA-1.10 verifies label identity by double-anchor
cross-scan (Registry: ATTEST-TBL Preamble Row Ref column; Preamble: A-N Attestation Row Ref
column): for each A-N, preamble Attestation Row Ref = ATTEST-A-N and attestation Preamble Row Ref
= A-N. Cross-scan is auditable at column level without semantic interpretation.

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A: Complete TABLE_1 with Tier column. Every cell Granted/Denied/Conditional/N/A. Rows ordered by tier.
- SHALL-B: TABLE_2 lists all PII, Financial, and Audit-Compliance fields with explicit FLS status. Null case explicit. Gap? YES rows in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier and Effective Scope filled. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 at SE-0 (before SE-1), all four vectors, Checked? = YES. Rule-outs name specific mechanism and reason. **SHALL-D extension [C-35]:** Additionally, SE-4's STRUCTURED CLOSE block SHALL carry a TABLE_4 row cross-reference at the SE-0 slot naming a specific TABLE_4 vector row by exact vector label. CA-1.9 verifies this sub-clause, distinct from CA-1.4 (SE-0 execution ordering).
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap case requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field Remediation block (CS-Expected, SE-Actual, Delta). Incomplete rows MUST be reopened. CA-1.6 verifies.
- SHALL-G: At the opening of SE-2, SE-3, and SE-4, closure MUST appear as a two-part labeled block -- Line 1: `MANUAL GAP [<exact CONTEXT label>]:` where the label is character-for-character as written in the CONTEXT section above; Line 2: description of what manual audits miss; Line 3: `STRUCTURED CLOSE:`; Line 4: closing mechanism. Exact label required; paraphrase fails. CA-1.7 verifies the MANUAL GAP block. CA-1.9 separately verifies the TABLE_4 SE-0 slot cross-reference inside SE-4's STRUCTURED CLOSE.

### Step 0.3 -- Phase 0 Artifact Manifest (CA-authored, Phase 0)

CA produces a numbered manifest of all structural artifacts authored in Steps 0.1 and 0.2. This
manifest is the authoritative record of Phase 0 authorship. CA's terminal verdict in Phase 3 cites
this manifest by item counts.

**Section A -- Schema Registry entries (Step 0.1):**
1. TABLE_1 -- Role-Operation Matrix
2. TABLE_2 -- FLS Coverage
3. TABLE_3 -- Record Scope by Role
4. TABLE_4 -- Escalation Vector Inventory
5. TABLE_5 -- Security Gap Inventory
6. CS-2 -- Sharing Rule Expectations
7. CS-3 -- Cross-Role Access Differential Expectations
8. ATTEST-TBL -- TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION
Total Schema IDs authored: 8

**Section B -- Criterion Enforcement Matrix rows (Step 0.2):**
C-01, C-02, C-03, C-04, C-05
Total criterion rows authored: 5

**Section C -- SHALL obligation letters (Step 0.2):**
SHALL-A, SHALL-B, SHALL-C, SHALL-D (with [C-35] extension sub-clause), SHALL-E, SHALL-F, SHALL-G
Total SHALL obligations authored: 7

**Section D -- Supplementary CA verification rows (Step 0.2):**
CA-1.6, CA-1.7, CA-1.8, CA-1.9, CA-1.10
Total supplementary CA-1.N rows authored: 5

**Section E -- R12 Structural Axis Declaration rows (Step 0.2):**
A-1 (C-31, Execution order, ATTEST-A-1), A-2 (C-32, Closure-note format, ATTEST-A-2), A-3 (C-33, CS self-reference, ATTEST-A-3)
Total axis rows authored: 3

Manifest totals: 8 schemas / 5 criterion rows / 7 SHALL obligations / 5 CA-1.N rows / 3 axis rows.
This manifest is cited in the Phase 3 terminal verdict to confirm all declared artifacts were
exercised during execution.

*Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

*(Identical to V-01 PHASE 1 in full -- CS-0 acknowledgment citing CS-2 and CS-3 by exact Schema
ID; CS-1 baseline; CS-2 sharing rule expectations table; CS-3 cross-role differential table.)*

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis (Privilege-Tier Descent Order)

*(Identical to V-01 PHASE 2 in full -- SE-0 admin inventory + TABLE_4; SE-1 TABLE_1; SE-2 TABLE_2
with MANUAL GAP [Blind spot 1 -- Post-incident FLS gap] + STRUCTURED CLOSE; SE-3 TABLE_3 with
MANUAL GAP [Blind spot 2 -- Cumulative privilege blind spot] + STRUCTURED CLOSE; SE-4 with MANUAL
GAP [Blind spot 3 -- OWD-sharing-rule override gap] + STRUCTURED CLOSE with SE-0 TABLE_4 slot
cross-reference; SE-5 TABLE_5.)*

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*CA returns. Each CA-1 row: Registry anchor then Preamble anchor then Verification line. CA-1.9
verifies SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot. CA-1.10 double-anchor: ATTEST-TBL schema +
label-identity cross-scan. Terminal verdict closes with Phase 0 Manifest Citation.*

*(CA-1.1 through CA-1.9 -- identical to V-01 in full.)*

**CA-1.10 -- ATTEST-TBL schema compliance + bidirectional loop label-identity cross-scan**
*(Phase 0 pre-assignment CA-1.10; double-anchor closes ATTEST-TBL schema governance over the
attestation table and confirms preamble-attestation label identity)*:
- Registry anchor -- Schema ID ATTEST-TBL (Step 0.1, Phase 0): declared columns [Row ID, R12 Dimension, Axis Label, Specific Output-Body Evidence Source, Preamble Row Ref, Status]. Blank-cell rule: all cells filled. Preamble Row Ref must match A-N value from preamble axis Attestation Row Ref column for this row.
- Preamble anchor -- CA-1.10 pre-assigned (supplementary rows, Step 0.2, Phase 0): "Double-anchor: ATTEST-TBL schema (Registry) + label-identity cross-scan (Preamble): preamble A-N Attestation Row Ref = ATTEST-A-N matches attestation ATTEST-A-N Preamble Row Ref = A-N | ATTEST-TBL schema compliance + preamble axis col 6 + attestation Preamble Row Ref col | Distinct from CA-1.4, CA-1.7, CA-1.9."
- Verification -- ATTEST-TBL schema satisfied (6 columns present, no blank cells)? Cross-scan:
  - A-1: preamble Attestation Row Ref = ATTEST-A-1; attestation ATTEST-A-1 Preamble Row Ref = A-1. Consistent? -> PASS / FAIL
  - A-2: preamble Attestation Row Ref = ATTEST-A-2; attestation ATTEST-A-2 Preamble Row Ref = A-2. Consistent? -> PASS / FAIL
  - A-3: preamble Attestation Row Ref = ATTEST-A-3; attestation ATTEST-A-3 Preamble Row Ref = A-3. Consistent? -> PASS / FAIL
  - Overall: ATTEST-TBL schema compliant + all three label pairs consistent? -> PASS / FAIL
- Distinction confirmed: CA-1.4 verified SE-0 ordering. CA-1.7 verified MANUAL GAP format. CA-1.9 verified SE-4 STRUCTURED CLOSE SE-0 slot. CA-1.10 verifies ATTEST-TBL schema compliance and preamble-attestation label identity.

**CA Format Compliance Verdict -- Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0, eight schemas including ATTEST-TBL),
CA-authored preamble (Step 0.2, Phase 0), Phase 0 Artifact Manifest (Step 0.3, Phase 0), R12
Structural Axis Declaration with A-1/A-2/A-3 Row IDs and Attestation Row Ref column, Phase 0 by label.
[CA-1.1 through CA-1.10 results. A-1 verified by CA-1.4+CA-1.9. A-2 by CA-1.7. A-3 by CA-1.8.
ATTEST-TBL schema compliance and bidirectional loop label-identity verified by CA-1.10.
Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

**Phase 0 Manifest Citation:**
Phase 0 Artifact Manifest (Step 0.3) declared: 8 schemas / 5 criterion rows / 7 SHALL obligations
/ 5 CA-1.N rows / 3 axis rows. Confirmation that all declared artifacts were exercised:
- 8 schemas: TABLE_1 at SE-1; TABLE_2 at SE-2; TABLE_3 at SE-3; TABLE_4 at SE-0; TABLE_5 at SE-5;
  CS-2 at CS-1+SE-0; CS-3 at CS-1+SE-1; ATTEST-TBL governs attestation table below (CA-1.10). All 8 exercised.
- 5 criterion rows: C-01 through C-05 verified by CA-1.1 through CA-1.5. All 5 exercised.
- 7 SHALL obligations: SHALL-A through SHALL-G (including SHALL-D [C-35] extension) verified by
  CA-1.1 through CA-1.9. All 7 exercised.
- 5 CA-1.N supplementary rows: CA-1.6 through CA-1.10 executed in Phase 3. All 5 exercised.
- 3 axis rows: A-1 verified by CA-1.4+CA-1.9; A-2 by CA-1.7; A-3 by CA-1.8; bidirectional loop
  by CA-1.10. All 3 exercised.
Manifest citation complete. All declared Phase 0 artifacts confirmed exercised.

**TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION** *(governed by Schema ID ATTEST-TBL; verified by CA-1.10)*:

| Row ID | R12 Dimension | Axis Label | Specific Output-Body Evidence Source | Preamble Row Ref | Status |
|--------|---------------|------------|--------------------------------------|-----------------|--------|
| ATTEST-A-1 | C-31 (Preamble Row A-1) | Execution order | Phase 2 output body: SE-0 section header precedes SE-1; TABLE_4 in SE-0 before TABLE_1; TABLE_1 and TABLE_3 contain Tier column; SE-4 STRUCTURED CLOSE contains SE-0 slot entry naming a specific TABLE_4 vector row by exact label (CA-1.9). | A-1 | CONFIRMED |
| ATTEST-A-2 | C-32 (Preamble Row A-2) | Closure-note format | Phase 2 output body: SE-2 opens with `MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:` followed by `STRUCTURED CLOSE:`; SE-3 and SE-4 same pattern with exact labels from CONTEXT. Verified by CA-1.7. | A-2 | CONFIRMED |
| ATTEST-A-3 | C-33 (Preamble Row A-3) | CS self-reference | Phase 1 output body: CS-0 sub-section before CS-1; CS-0 cites Schema ID CS-2 and Schema ID CS-3 by exact label; CS-0 lists SE Cross-Reference and SE Confirmation as SE-updatable columns. Verified by CA-1.8. | A-3 | CONFIRMED |

All three axes simultaneously active. Preamble Row Ref column back-references each ATTEST-A-N row
to its A-N preamble declaration. CA-1.10 confirmed ATTEST-TBL schema compliance and label
identity by double-anchor cross-scan. Phase 0 Manifest Citation confirms all 8 schemas, 5
criterion rows, 7 SHALL obligations, 5 CA-1.N rows, and 3 axis rows were exercised.
Non-interference manifestation: A-1 evidence in SE-0/TABLE_1/TABLE_3/SE-4 STRUCTURED CLOSE;
A-2 evidence in SE-2/SE-3/SE-4 opening blocks; A-3 evidence in CS-0. No evidence source overlaps.
