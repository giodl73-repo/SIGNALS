v02 = r"""
## V-02 -- Single-Axis C-35: SE-4 STRUCTURED CLOSE TABLE_4 SE-0 Cross-Reference + CA-1.9

**Axis:** SE-4's STRUCTURED CLOSE block gains an explicit TABLE_4 row cross-reference at the
SE-0 position -- a named structural statement citing TABLE_4 rows by their SE-0 execution-order
anchor. CA-1.9 pre-assigned in Phase 0 mandate; CA-1.9 verification row added in Phase 3 as a
distinct audit target from CA-1.4 (which verifies SE-0 ordering: TABLE_4 before TABLE_1) and
CA-1.7 (which verifies MANUAL GAP exact-label format). All other R12-V-05 mechanisms preserved.
No STRUCTURAL AXIS NON-INTERFERENCE DECLARATION (C-34 not targeted). No tri-dimensional verdict (C-36 not targeted).
**Hypothesis:** 26/28 -- adds C-35; fails C-34 (no axis declaration), C-36 (no tri-dimensional verdict).

---

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
SE-4 closes Blind spot 3. Closure notes are exact-label two-part blocks co-located at each SE
sub-section opening, carrying the exact blind-spot label from this CONTEXT section.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins.

**PHASE 0 -- CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1: seven schemas total) and the Criterion
Enforcement Matrix preamble (Step 0.2: SHALL-A through SHALL-G, M4 row IDs CA-1.1 through CA-1.8
pre-assigned; CA-1.9 pre-assigned as SE-4 STRUCTURED CLOSE TABLE_4 SE-0 cross-reference verifier).
CA issues handoff to PHASE 1.

**PHASE 1 -- CS (Customer Success):**
Executes second. Opens with CS-0 sub-section (Schema Registry acknowledgment). Then produces
CS-1, CS-2, CS-3. CS does not fill TABLE_1-5. CS issues handoff to PHASE 2.

**PHASE 2 -- SE (Security Engineer / Dataverse Security Expert):**
Executes third in privilege-tier descent order. SE-0 (admin-tier inventory and TABLE_4) runs
before SE-1. TABLE_1 and TABLE_3 include Tier column. SE-2, SE-3, SE-4 open with two-part
exact-label closure blocks per SHALL-G. SE-4 STRUCTURED CLOSE block includes explicit TABLE_4
row cross-reference at SE-0 position per CA-1.9 pre-assignment. Issues handoff to PHASE 3.

**PHASE 3 -- CA-1 (CA Verification Pass):**
CA returns. Double-anchor verification rows CA-1.1 through CA-1.9. CA-1.8 verifies CS-0
acknowledgment. CA-1.9 verifies SE-4 STRUCTURED CLOSE TABLE_4 SE-0 cross-reference as a
distinct audit target from CA-1.4 (SE-0 ordering) and CA-1.7 (MANUAL GAP label compliance).

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
Blank-cell rule: FLS Profile Configured? = Configured / Not Configured (never blank). Gap? = YES / NO.

**Schema ID: TABLE_3 -- Record Scope by Role**
Declared columns: `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Tier values mirror TABLE_1. Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU /
Org-wide / Team-scoped / Sharing-[rule name]. Verified? = YES / NO.

**Schema ID: TABLE_4 -- Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
Blank-cell rule: all four vectors, Checked? = YES, Finding = escalation path or specific rule-out.
Note: TABLE_4 executes at SE-0 before SE-1 because admin-tier role structure determines escalation
paths before the lower-tier role-operation matrix is populated. CA-1.9 verifies that SE-4's
STRUCTURED CLOSE block cross-references TABLE_4 rows by their SE-0 position.

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

Additional pre-assignments: CA-1.6 (SHALL-F three-field structure); CA-1.7 (SHALL-G exact-label
two-part blocks); CA-1.8 (C-29 + C-33: CS-2/CS-3 Registry registration and CS-0 acknowledgment);
CA-1.9 (C-35: SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 position -- distinct
from CA-1.4's SE-0 ordering check and CA-1.7's MANUAL GAP label check).

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A: Complete TABLE_1 with Tier column. Every cell Granted/Denied/Conditional/N/A. Rows ordered by tier.
- SHALL-B: TABLE_2 lists all PII, Financial, and Audit-Compliance fields with explicit FLS status. Null case explicit. Gap? YES rows in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier and Effective Scope filled. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 at SE-0 (before SE-1), all four vectors, Checked? = YES. Rule-outs name specific mechanism and reason.
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap case requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field Remediation block (CS-Expected, SE-Actual, Delta). Incomplete rows MUST be reopened. CA-1.6 verifies.
- SHALL-G: At the opening of SE-2, SE-3, and SE-4, closure MUST appear as a two-part labeled block -- Line 1: `MANUAL GAP [<exact CONTEXT label>]:` where <exact CONTEXT label> is the label character-for-character as written in the CONTEXT section; Line 2: description of what manual audits miss; Line 3: `STRUCTURED CLOSE:`; Line 4: which table and mechanism closes it. Single-line annotation, blockquote format, TABLE_5 consolidation, or paraphrased label all fail SHALL-G. CA-1.7 verifies exact label carry-through.
- SHALL-D-EXT (C-35): SE-4 STRUCTURED CLOSE block MUST contain an explicit TABLE_4 row cross-reference at the SE-0 position. The STRUCTURED CLOSE block at SE-4 MUST include a labeled line citing each TABLE_4 row by its SE-0 position using the format "TABLE_4 SE-0 [Vector]: [Finding summary as populated at SE-0]". CA-1.9 verifies this cross-reference. This is a distinct requirement from CA-1.4 (which verifies that TABLE_4 appears before TABLE_1) and from CA-1.7 (which verifies MANUAL GAP label format).

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
SE-update protocol acknowledged: SE populates SE Cross-Reference (TABLE_4 row or TABLE_5 row ID)
and SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE) after SE-0/TABLE_4 analysis.
Expectation format confirmed: CS-2 rows use columns Rule Name | Trigger | Expected Access Granted |
Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation.
SE-updatable columns left blank; SE fills after SE-0.

**Registry acknowledgment for CS-3:**
Schema ID: CS-3 -- Cross-Role Access Differential Expectations.
SE-updatable columns as declared by CA in Phase 0 Schema Registry: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged: SE populates SE Cross-Reference (TABLE_1 or TABLE_3 row ID)
and SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE) after SE-1/SE-3 analysis.
Expectation format confirmed: CS-3 rows use columns Entity | Operation | CS Role Expected Access |
Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference |
SE Confirmation. SE-updatable columns left blank; SE fills after SE-1/SE-3.

### CS-1 -- Expected Customer Service Access Baseline

For each entity in scope: (a) which CRUD operations the CS role is expected to perform as part of
normal job function; (b) the expected record scope; (c) which sensitive fields CS needs read or
write access to and why. Identify any configuration that may inadvertently open access beyond job
requirements.

**CS-2 -- Sharing rule expectations** *(Schema Registry CS-2; SE-updatable columns blank; SE
fills after SE-0/TABLE_4)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

For each Potential Overreach? YES: name the access path and the most likely over-reached role.

**CS-3 -- Cross-role access differential** *(Schema Registry CS-3; SE-updatable columns blank;
SE fills after SE-1/SE-3)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

State at minimum one entity and one operation where CS has less access than the Comparison Role.

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis (Privilege-Tier Descent Order)

*SE traces from highest-privilege tier to lowest. SE-0 establishes admin-tier ceiling and
TABLE_4 before SE-1. TABLE_1 and TABLE_3 include Tier column. SE-2/SE-3/SE-4 use exact-label
two-part closure blocks per SHALL-G. SE-4 STRUCTURED CLOSE includes explicit TABLE_4 row
cross-reference at SE-0 position per CA-1.9 pre-assignment.*

### SE-0 -- Admin-Tier Inventory and Escalation Vectors (executes before TABLE_1)

**Admin-tier role inventory:** List System Administrator, Environment Admin, and any
admin-equivalent roles with record scope and key capabilities. Note any admin capability that
bypasses lower-tier controls. This establishes the privilege ceiling for all lower-tier roles.

**TABLE_4 -- Escalation Vector Inventory** *(Schema Registry TABLE_4; placed at SE-0)*

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Finding format: `[Role] -> [Mechanism] -> [Elevated access achieved]` for confirmed escalation;
"Checked [mechanism]: no path found because [specific reason]" for rule-out. After TABLE_4:
populate CS-2 SE Cross-Reference and SE Confirmation.

### SE-1 / SHALL-A -- Section 1: Role-Operation Matrix

**TABLE_1 -- Role-Operation Matrix** *(Schema Registry TABLE_1 with Tier column; blank-cell rule)*

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Rows ordered: Admin tier first, Custom tier second, Restricted tier last. After TABLE_1: populate
CS-3 SE Cross-Reference and SE Confirmation.

**Cross-role differential analysis:** Compare the CS role against at least one Admin-tier role
and one Custom-tier role. Cite SE-0 TABLE_4 data for any differential attributable to admin-tier
escalation vectors.

### SE-2 / SHALL-B -- Section 2: Field-Level Security Coverage

MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:
Column security profiles are not auditable from the security roles UI; administrators discover
missing FLS only after a data exposure event reveals that a sensitive field was readable or
writable by an unintended role.

STRUCTURED CLOSE:
TABLE_2 below enumerates every sensitive field in scope with its explicit FLS status (Configured /
Not Configured), surfacing pre-event what the security roles UI conceals. All Not Configured
sensitive fields are forwarded to TABLE_5 as MISSING-FLS gaps with Tier column.

**TABLE_2 -- FLS Coverage** *(Schema Registry TABLE_2; blank-cell rule globally)*

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Categories: PII / Financial / Audit-Compliance / Other-Sensitive. Null case explicit.

**Defense-in-depth layer check:** Identify the enforcement layer for at least one sensitive field.

### SE-3 / SHALL-C -- Section 3: Record Access Scope

MANUAL GAP [Blind spot 2 -- Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access produced by a security role
plus owner team membership plus OWD; spot-checking roles individually misses cross-role privilege
accumulation through team inheritance.

STRUCTURED CLOSE:
TABLE_3 below maps the effective scope for every role by Tier, recording the OWD baseline, the
scope modifier from team or role depth, and the resulting effective scope as a single traceable row.

**TABLE_3 -- Record Scope by Role** *(Schema Registry TABLE_3 with Tier column; blank-cell rule)*

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role MUST appear, ordered by Tier. After TABLE_3: update CS-3 SE Confirmation.

### SE-4 / SHALL-D -- Section 4: Privilege Escalation Cross-Reference

MANUAL GAP [Blind spot 3 -- OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing the sharing rules
that silently override them; a Private OWD combined with an active sharing rule can grant
effective org-wide access without appearing in any security roles UI view.

STRUCTURED CLOSE:
TABLE_4 (filled at SE-0) evaluated all four escalation vectors with sharing rules explicitly
cross-referenced against OWD settings. This section adds cross-tier differential summary citing
SE-0 data: for the most privileged Admin-tier role and the most restricted Restricted-tier role,
identify the specific enforcement layer where access diverges, citing the SE-0 TABLE_4 row ID
that established the admin-tier ceiling.

TABLE_4 row cross-reference at SE-0 position (per SHALL-D-EXT, verified at CA-1.9): For each of
the four escalation vectors evaluated at SE-0, cite the TABLE_4 row by its SE-0 position using
the format "TABLE_4 SE-0 [Vector]: [Finding as populated at SE-0]". This cross-reference links
the escalation interpretation in this section back to the SE-0 population event. It is a
structurally distinct statement from: (a) the MANUAL GAP block above (which names the blind spot
and its closure -- verified by CA-1.7), and (b) the SE-0 ordering of TABLE_4 before TABLE_1
(verified by CA-1.4). CA-1.9 verifies this cross-reference independently.

### SE-5 / SHALL-E -- Section 5: Security Gap Inventory

**TABLE_5 -- Security Gap Inventory** *(Schema Registry TABLE_5 with Tier column; blank-cell rule)*

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

*CA returns. Each CA-1 row MUST present Registry anchor and Preamble anchor as structurally
distinct labeled elements before the Verification line. Inline concatenation fails C-24.*

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
- Verification -- TABLE_4 at SE-0 (before SE-1)? All four vectors? Checked? = YES? Findings or specific rule-outs? -> PASS / FAIL

**CA-1.5 -- C-05 verification** *(Phase 0 M4 pre-assignment CA-1.5)*:
- Registry anchor -- Schema ID TABLE_5 (with Tier): [#, Gap Type, Entity, Field or Rule, Role, Tier, Severity, Remediation] -- blank cells prohibited globally.
- Preamble anchor -- C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 -- verifying...
- Verification -- TABLE_5 present? Named gap? Tier column populated? Remediations exact? -> PASS / FAIL

**CA-1.6 -- SHALL-F compliance verification** *(CS-EXPECTATION-VIOLATED three-field structure)*:
- Registry anchor -- Schema ID TABLE_5 CS-EXPECTATION-VIOLATED row: [CS-Expected field, SE-Actual field, Delta field] -- all three required per SHALL-F.
- Preamble anchor -- SHALL-F as authored by CA in Phase 0: three-field Remediation block mandatory; rows missing any field MUST be reopened.
- Verification -- For each CS-EXPECTATION-VIOLATED row: CS-Expected populated? SE-Actual populated? Delta populated with exact configuration change? -> PASS / FAIL per row.

**CA-1.7 -- SHALL-G compliance verification** *(exact-label two-part closure blocks)*:
- Registry anchor -- CONTEXT section declared exact labels: "Blind spot 1 -- Post-incident FLS gap" (SE-2), "Blind spot 2 -- Cumulative privilege blind spot" (SE-3), "Blind spot 3 -- OWD-sharing-rule override gap" (SE-4).
- Preamble anchor -- SHALL-G as authored by CA in Phase 0: Line 1 MUST be `MANUAL GAP [<exact CONTEXT label>]:`; exact = character-for-character; paraphrase fails; CA-1.7 verifies.
- Verification -- SE-2 opens with `MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:`? Followed by `STRUCTURED CLOSE:`? SE-3 opens with `MANUAL GAP [Blind spot 2 -- Cumulative privilege blind spot]:`? SE-4 opens with `MANUAL GAP [Blind spot 3 -- OWD-sharing-rule override gap]:`? -> PASS / FAIL per section.

**CA-1.8 -- CS-2/CS-3 Schema Registry registration + CS-0 acknowledgment verification** *(C-29 + C-33)*:
- Registry anchor -- Schema Registry declared CS-2 and CS-3 as named schema entries with SE-updatable columns and SE-update protocols co-located. PHASE 1 mandate requires CS-0 to acknowledge both.
- Preamble anchor -- CS-0 acknowledgment is a PHASE 1 structural requirement per Phase 0 preamble. CA-1.8 verifies.
- Verification -- CS-2 in Schema Registry with SE-updatable column declarations? CS-3 same? CS-0 present before CS-1? CS-0 cites both schema IDs by exact label? CS-0 lists SE-updatable columns for both? SE populated SE-updatable columns? -> PASS / FAIL

**CA-1.9 -- C-35 verification** *(SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 position)*:
- Registry anchor -- Schema ID TABLE_4 note (Phase 0 Schema Registry): TABLE_4 executes at SE-0 before SE-1; CA-1.9 was pre-assigned to verify SE-4 STRUCTURED CLOSE cites TABLE_4 rows by SE-0 position. This is structurally distinct from CA-1.4 (SE-0 ordering: TABLE_4 before TABLE_1) and CA-1.7 (MANUAL GAP exact-label format at SE-4 opening).
- Preamble anchor -- SHALL-D-EXT as authored by CA in Phase 0: SE-4 STRUCTURED CLOSE MUST contain labeled "TABLE_4 row cross-reference at SE-0 position" citing each of the four TABLE_4 vectors by SE-0 position. CA-1.9 verifies this labeled statement is present, covers all four vectors, and is structurally distinct from the MANUAL GAP label block.
- Verification -- SE-4 STRUCTURED CLOSE contains explicit "TABLE_4 row cross-reference at SE-0 position" labeled statement? Cites all four TABLE_4 vector rows by SE-0 position? Statement is present as a distinct structural element from the MANUAL GAP label (CA-1.7 target) and from SE-0 ordering (CA-1.4 target)? -> PASS / FAIL

**CA Format Compliance Verdict -- Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0), Phase 0 by label.
[C-01 through C-05 with CA-1.1 through CA-1.5 results. SHALL-F (CA-1.6). SHALL-G exact-label two-part block compliance (CA-1.7). C-29 + C-33 CS-0 acknowledgment (CA-1.8). C-35 SE-4 STRUCTURED CLOSE TABLE_4 SE-0 cross-reference (CA-1.9). Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

---
"""

v03 = r"""
## V-03 -- Single-Axis C-36: CA Terminal Verdict Tri-Dimensional Self-Evidence Attestation

**Axis:** CA Format Compliance Verdict gains explicit tri-dimensional self-evidence attestation.
The attestation names each R12 structural dimension and its specific output-body evidence source:
Dimension 1 (execution order / C-31): SE-0 section header + Phase 2 mandate + TABLE_4 before
TABLE_1 in output body. Dimension 2 (closure-note format / C-32): MANUAL GAP / STRUCTURED CLOSE
blocks at SE-2/SE-3/SE-4 with exact label carry-through. Dimension 3 (CS self-reference / C-33):
CS-0 sub-section citing Registry schema IDs CS-2 and CS-3. All other R12-V-05 mechanisms preserved.
No STRUCTURAL AXIS NON-INTERFERENCE DECLARATION (C-34 not targeted). No CA-1.9 (C-35 not targeted).
**Hypothesis:** 26/28 -- adds C-36; fails C-34 (no axis declaration), C-35 (no CA-1.9).

---

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
SE-4 closes Blind spot 3. Closure notes are exact-label two-part blocks co-located at each SE
sub-section opening, carrying the exact blind-spot label from this CONTEXT section.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins.

**PHASE 0 -- CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1: seven schemas total) and the Criterion
Enforcement Matrix preamble (Step 0.2: SHALL-A through SHALL-G, M4 row IDs CA-1.1 through CA-1.8
pre-assigned). CA issues handoff to PHASE 1.

**PHASE 1 -- CS (Customer Success):**
Executes second. Opens with CS-0 sub-section (Schema Registry acknowledgment). Then produces
CS-1, CS-2, CS-3. CS does not fill TABLE_1-5. CS issues handoff to PHASE 2.

**PHASE 2 -- SE (Security Engineer / Dataverse Security Expert):**
Executes third in privilege-tier descent order. SE-0 (admin-tier inventory and TABLE_4) runs
before SE-1. TABLE_1 and TABLE_3 include Tier column. SE-2, SE-3, SE-4 open with two-part
exact-label closure blocks per SHALL-G. Issues handoff to PHASE 3.

**PHASE 3 -- CA-1 (CA Verification Pass):**
CA returns. Double-anchor verification rows CA-1.1 through CA-1.8. CA-1.8 verifies CS-0
acknowledgment. CA terminal verdict includes R12 tri-dimensional self-evidence attestation
naming each dimension and its specific output-body evidence source.

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
Blank-cell rule: FLS Profile Configured? = Configured / Not Configured (never blank). Gap? = YES / NO.

**Schema ID: TABLE_3 -- Record Scope by Role**
Declared columns: `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Tier values mirror TABLE_1. Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU /
Org-wide / Team-scoped / Sharing-[rule name]. Verified? = YES / NO.

**Schema ID: TABLE_4 -- Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
Blank-cell rule: all four vectors, Checked? = YES, Finding = escalation path or specific rule-out.
Note: TABLE_4 executes at SE-0 before SE-1 because admin-tier role structure determines escalation
paths before the lower-tier role-operation matrix is populated.

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

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A: Complete TABLE_1 with Tier column. Every cell Granted/Denied/Conditional/N/A. Rows ordered by tier.
- SHALL-B: TABLE_2 lists all PII, Financial, and Audit-Compliance fields with explicit FLS status. Null case explicit. Gap? YES rows in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier and Effective Scope filled. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 at SE-0 (before SE-1), all four vectors, Checked? = YES. Rule-outs name specific mechanism and reason.
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap case requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field Remediation block (CS-Expected, SE-Actual, Delta). Incomplete rows MUST be reopened. CA-1.6 verifies.
- SHALL-G: At the opening of SE-2, SE-3, and SE-4, closure MUST appear as a two-part labeled block -- Line 1: `MANUAL GAP [<exact CONTEXT label>]:` where <exact CONTEXT label> is the label character-for-character as written in the CONTEXT section; Line 2: description of what manual audits miss; Line 3: `STRUCTURED CLOSE:`; Line 4: which table and mechanism closes it. CA-1.7 verifies exact label carry-through.

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
SE-update protocol acknowledged: SE populates SE Cross-Reference (TABLE_4 row or TABLE_5 row ID)
and SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE) after SE-0/TABLE_4 analysis.
Expectation format confirmed: CS-2 rows use columns Rule Name | Trigger | Expected Access Granted |
Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation.
SE-updatable columns left blank; SE fills after SE-0.

**Registry acknowledgment for CS-3:**
Schema ID: CS-3 -- Cross-Role Access Differential Expectations.
SE-updatable columns as declared by CA in Phase 0 Schema Registry: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged: SE populates SE Cross-Reference (TABLE_1 or TABLE_3 row ID)
and SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE) after SE-1/SE-3 analysis.
Expectation format confirmed: CS-3 rows use columns Entity | Operation | CS Role Expected Access |
Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference |
SE Confirmation. SE-updatable columns left blank; SE fills after SE-1/SE-3.

### CS-1 -- Expected Customer Service Access Baseline

For each entity in scope: (a) which CRUD operations the CS role is expected to perform as part of
normal job function; (b) the expected record scope; (c) which sensitive fields CS needs read or
write access to and why. Identify any configuration that may inadvertently open access beyond job
requirements.

**CS-2 -- Sharing rule expectations** *(Schema Registry CS-2; SE-updatable columns blank; SE
fills after SE-0/TABLE_4)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

For each Potential Overreach? YES: name the access path and the most likely over-reached role.

**CS-3 -- Cross-role access differential** *(Schema Registry CS-3; SE-updatable columns blank;
SE fills after SE-1/SE-3)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

State at minimum one entity and one operation where CS has less access than the Comparison Role.

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis (Privilege-Tier Descent Order)

*SE traces from highest-privilege tier to lowest. SE-0 establishes admin-tier ceiling and
TABLE_4 before SE-1. TABLE_1 and TABLE_3 include Tier column. SE-2/SE-3/SE-4 use exact-label
two-part closure blocks per SHALL-G.*

### SE-0 -- Admin-Tier Inventory and Escalation Vectors (executes before TABLE_1)

**Admin-tier role inventory:** List System Administrator, Environment Admin, and any
admin-equivalent roles with record scope and key capabilities. Note any admin capability that
bypasses lower-tier controls. This establishes the privilege ceiling for all lower-tier roles.

**TABLE_4 -- Escalation Vector Inventory** *(Schema Registry TABLE_4; placed at SE-0)*

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Finding format: `[Role] -> [Mechanism] -> [Elevated access achieved]` for confirmed escalation;
"Checked [mechanism]: no path found because [specific reason]" for rule-out. After TABLE_4:
populate CS-2 SE Cross-Reference and SE Confirmation.

### SE-1 / SHALL-A -- Section 1: Role-Operation Matrix

**TABLE_1 -- Role-Operation Matrix** *(Schema Registry TABLE_1 with Tier column; blank-cell rule)*

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Rows ordered: Admin tier first, Custom tier second, Restricted tier last. After TABLE_1: populate
CS-3 SE Cross-Reference and SE Confirmation.

**Cross-role differential analysis:** Compare the CS role against at least one Admin-tier role
and one Custom-tier role. Cite SE-0 TABLE_4 data for any differential attributable to admin-tier
escalation vectors.

### SE-2 / SHALL-B -- Section 2: Field-Level Security Coverage

MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:
Column security profiles are not auditable from the security roles UI; administrators discover
missing FLS only after a data exposure event reveals that a sensitive field was readable or
writable by an unintended role.

STRUCTURED CLOSE:
TABLE_2 below enumerates every sensitive field in scope with its explicit FLS status (Configured /
Not Configured), surfacing pre-event what the security roles UI conceals. All Not Configured
sensitive fields are forwarded to TABLE_5 as MISSING-FLS gaps with Tier column.

**TABLE_2 -- FLS Coverage** *(Schema Registry TABLE_2; blank-cell rule globally)*

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Categories: PII / Financial / Audit-Compliance / Other-Sensitive. Null case explicit.

**Defense-in-depth layer check:** Identify the enforcement layer for at least one sensitive field.

### SE-3 / SHALL-C -- Section 3: Record Access Scope

MANUAL GAP [Blind spot 2 -- Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access produced by a security role
plus owner team membership plus OWD; spot-checking roles individually misses cross-role privilege
accumulation through team inheritance.

STRUCTURED CLOSE:
TABLE_3 below maps the effective scope for every role by Tier, recording the OWD baseline, the
scope modifier from team or role depth, and the resulting effective scope as a single traceable row.

**TABLE_3 -- Record Scope by Role** *(Schema Registry TABLE_3 with Tier column; blank-cell rule)*

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role MUST appear, ordered by Tier. After TABLE_3: update CS-3 SE Confirmation.

### SE-4 / SHALL-D -- Section 4: Privilege Escalation Cross-Reference

MANUAL GAP [Blind spot 3 -- OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing the sharing rules
that silently override them; a Private OWD combined with an active sharing rule can grant
effective org-wide access without appearing in any security roles UI view.

STRUCTURED CLOSE:
TABLE_4 (filled at SE-0) evaluated all four escalation vectors with sharing rules explicitly
cross-referenced against OWD settings. This section adds cross-tier differential summary citing
SE-0 data: for the most privileged Admin-tier role and the most restricted Restricted-tier role,
identify the specific enforcement layer where access diverges, citing the SE-0 TABLE_4 row ID
that established the admin-tier ceiling.

### SE-5 / SHALL-E -- Section 5: Security Gap Inventory

**TABLE_5 -- Security Gap Inventory** *(Schema Registry TABLE_5 with Tier column; blank-cell rule)*

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

*CA returns. Each CA-1 row MUST present Registry anchor and Preamble anchor as structurally
distinct labeled elements before the Verification line. Inline concatenation fails C-24.*

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
- Verification -- TABLE_4 at SE-0 (before SE-1)? All four vectors? Checked? = YES? Findings or specific rule-outs? -> PASS / FAIL

**CA-1.5 -- C-05 verification** *(Phase 0 M4 pre-assignment CA-1.5)*:
- Registry anchor -- Schema ID TABLE_5 (with Tier): [#, Gap Type, Entity, Field or Rule, Role, Tier, Severity, Remediation] -- blank cells prohibited globally.
- Preamble anchor -- C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 -- verifying...
- Verification -- TABLE_5 present? Named gap? Tier column populated? Remediations exact? -> PASS / FAIL

**CA-1.6 -- SHALL-F compliance verification** *(CS-EXPECTATION-VIOLATED three-field structure)*:
- Registry anchor -- Schema ID TABLE_5 CS-EXPECTATION-VIOLATED row: [CS-Expected field, SE-Actual field, Delta field] -- all three required per SHALL-F.
- Preamble anchor -- SHALL-F as authored by CA in Phase 0: three-field Remediation block mandatory; rows missing any field MUST be reopened.
- Verification -- For each CS-EXPECTATION-VIOLATED row: CS-Expected populated? SE-Actual populated? Delta populated with exact configuration change? -> PASS / FAIL per row.

**CA-1.7 -- SHALL-G compliance verification** *(exact-label two-part closure blocks)*:
- Registry anchor -- CONTEXT section declared exact labels: "Blind spot 1 -- Post-incident FLS gap" (SE-2), "Blind spot 2 -- Cumulative privilege blind spot" (SE-3), "Blind spot 3 -- OWD-sharing-rule override gap" (SE-4).
- Preamble anchor -- SHALL-G as authored by CA in Phase 0: Line 1 MUST be `MANUAL GAP [<exact CONTEXT label>]:`; exact = character-for-character; paraphrase fails; CA-1.7 verifies.
- Verification -- SE-2 opens with `MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:`? Followed by `STRUCTURED CLOSE:`? SE-3 opens with `MANUAL GAP [Blind spot 2 -- Cumulative privilege blind spot]:`? SE-4 opens with `MANUAL GAP [Blind spot 3 -- OWD-sharing-rule override gap]:`? -> PASS / FAIL per section.

**CA-1.8 -- CS-2/CS-3 Schema Registry registration + CS-0 acknowledgment verification** *(C-29 + C-33)*:
- Registry anchor -- Schema Registry declared CS-2 and CS-3 as named schema entries with SE-updatable columns and SE-update protocols co-located. PHASE 1 mandate requires CS-0 to acknowledge both.
- Preamble anchor -- CS-0 acknowledgment is a PHASE 1 structural requirement per Phase 0 preamble. CA-1.8 verifies.
- Verification -- CS-2 in Schema Registry with SE-updatable column declarations? CS-3 same? CS-0 present before CS-1? CS-0 cites both schema IDs by exact label? CS-0 lists SE-updatable columns for both? SE populated SE-updatable columns? -> PASS / FAIL

**CA Format Compliance Verdict -- Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0), Phase 0 by label.
[C-01 through C-05 with CA-1.1 through CA-1.5 results. SHALL-F (CA-1.6). SHALL-G exact-label two-part block compliance (CA-1.7). C-29 + C-33 CS-0 acknowledgment (CA-1.8). Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

**R12 Structural Dimension Self-Evidence Attestation (tri-dimensional, C-36):**
The three R12 structural dimensions are self-evidently satisfied from the output body alone.
Each dimension is named with its specific output-body evidence source:

- R12 Dimension 1 -- Execution order (C-31): Evidence in output body -- (a) Section header
  "SE-0 -- Admin-Tier Inventory and Escalation Vectors (executes before TABLE_1)" appears as a
  named sub-section before "SE-1 / SHALL-A -- Section 1: Role-Operation Matrix"; (b) Phase 2
  mandate states "SE-0 (admin-tier inventory and TABLE_4 escalation vectors) runs before SE-1";
  (c) TABLE_4 is physically positioned under SE-0 heading and TABLE_1 is physically positioned
  under SE-1 heading in the output body. Execution order is recoverable from output body section
  headers and table positions alone, without consulting prompt instructions.
  -> PASS / FAIL

- R12 Dimension 2 -- Closure-note format (C-32): Evidence in output body -- (a) SE-2 opens with
  the exact string "MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:" on its own line,
  followed by "STRUCTURED CLOSE:" on its own line; (b) SE-3 opens with exact string
  "MANUAL GAP [Blind spot 2 -- Cumulative privilege blind spot]:" followed by "STRUCTURED CLOSE:";
  (c) SE-4 opens with exact string "MANUAL GAP [Blind spot 3 -- OWD-sharing-rule override gap]:"
  followed by "STRUCTURED CLOSE:". All three carry exact CONTEXT labels character-for-character
  as declared in the CONTEXT section. Closure-note format is recoverable from SE sub-section
  openings alone.
  -> PASS / FAIL

- R12 Dimension 3 -- CS self-reference (C-33): Evidence in output body -- CS-0 sub-section
  "Schema Registry Acknowledgment (CS-authored, Phase 1)" contains labeled acknowledgment
  statements: "Schema ID: CS-2 -- Sharing Rule Expectations" and
  "Schema ID: CS-3 -- Cross-Role Access Differential Expectations" cited by their exact Phase 0
  Registry schema ID labels; SE-updatable columns listed for both before CS-1 begins. CS
  self-reference to Registry is recoverable from CS-0 sub-section content alone.
  -> PASS / FAIL

All three R12 structural dimensions are simultaneously: PASS / FAIL. Self-evidence attestation:
each dimension's verification evidence is named with a specific output-body location (section
header, table position, or sub-section content), verifiable without consulting the prompt.

---
"""

with open(r"C:/src/sim/simulations/quest/golden/trace-permissions-variate-R3-v12-2026-03-16.md", "a", encoding="utf-8") as f:
    f.write(v02)
    f.write(v03)

print("V-02 and V-03 appended.")
