content = r"""
## V-03 -- Single-Axis C-36: Tri-Dimensional Terminal Attestation

**Axis:** C-36 -- CA Format Compliance Verdict gains an explicit named "TRI-DIMENSIONAL
SELF-EVIDENCE ATTESTATION" block with per-dimension entries naming the specific output-body
evidence source for each R12 structural dimension: execution order (C-31), closure-note format
(C-32), CS self-reference (C-33). The attestation extends C-22 to all three R12 dimensions
simultaneously. PHASE 3 description updated to mention tri-dimensional attestation. All other
mechanisms from R12-V-05 are preserved unchanged.
**Hypothesis:** 26/28 (adds C-36; fails C-34 -- no axis declaration; fails C-35 -- no CA-1.9).

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
CA executes first. Authors the Schema Registry (Step 0.1: TABLE_1 through TABLE_5 with Tier
columns on TABLE_1 and TABLE_3; CS-2 and CS-3 with SE-updatable columns and SE-update protocols
-- seven schemas total) and the Criterion Enforcement Matrix preamble (Step 0.2: SHALL-A through
SHALL-G, M4 row IDs CA-1.1 through CA-1.8 pre-assigned). CA issues handoff to PHASE 1.

**PHASE 1 -- CS (Customer Success):**
Executes second. Opens with CS-0 sub-section (Schema Registry acknowledgment: cites Registry
schema IDs for CS-2 and CS-3 by exact Schema ID label, lists SE-updatable columns, confirms
expectation format). Then produces CS-1, CS-2, CS-3. CS does not fill TABLE_1-5. Handoff to PHASE 2.

**PHASE 2 -- SE (Security Engineer / Dataverse Security Expert):**
Executes third in privilege-tier descent order. SE-0 (admin-tier inventory + TABLE_4) runs before
SE-1 (role-operation matrix). TABLE_1 and TABLE_3 include Tier column. SE-2, SE-3, SE-4 each
open with exact-label two-part closure blocks per SHALL-G. SE-4 cites SE-0 data in cross-tier
differential. Handoff to PHASE 3.

**PHASE 3 -- CA-1 (CA Verification Pass):**
CA returns. Each CA-1 row performs double-anchor reaffirmation as structurally distinct labeled
elements. Inline concatenation fails C-24. CA-1.8 verifies CS-0 acknowledgment precedes CS-1.
CA Format Compliance Verdict includes a tri-dimensional self-evidence attestation naming the
specific output-body evidence source for each R12 structural dimension.

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
Blank-cell rule: all four vectors, Checked? = YES, Finding = escalation path or specific rule-out.
Note: TABLE_4 executes at SE-0 before SE-1 because admin-tier role structure determines escalation
paths before the lower-tier role-operation matrix is populated.

**Schema ID: TABLE_5 -- Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation`
Blank-cell rule: Remediation = exact object + exact location + expected post-fix state.
CS-EXPECTATION-VIOLATED Remediation (three-field block): CS-Expected / SE-Actual / Delta.

**Schema ID: CS-2 -- Sharing Rule Expectations**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference (TABLE_4 row ID or TABLE_5 row ID);
SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE update protocol: SE populates after TABLE_4 analysis at SE-0. CONTRADICTED triggers
CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

**Schema ID: CS-3 -- Cross-Role Access Differential Expectations**
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
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field Remediation block. Incomplete rows reopened. CA-1.6 verifies.
- SHALL-G: SE-2, SE-3, SE-4 each open with two-part labeled block -- Line 1: `MANUAL GAP [<exact CONTEXT label>]:`; Line 2: what manual audits miss; Line 3: `STRUCTURED CLOSE:`; Line 4: closing mechanism. Single-line annotation, blockquote, TABLE_5 consolidation, or paraphrased label all fail. CA-1.7 verifies.

*Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

*CS opens with CS-0 Registry acknowledgment before authoring any expectation content.*

### CS-0 -- Schema Registry Acknowledgment (CS-authored, Phase 1)

**Registry acknowledgment for CS-2:**
Schema ID: CS-2 -- Sharing Rule Expectations.
SE-updatable columns as declared by CA in Phase 0 Schema Registry: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged: SE populates after SE-0/TABLE_4 analysis.
Expectation format confirmed: CS-2 uses declared column schema. SE-updatable columns left blank.

**Registry acknowledgment for CS-3:**
Schema ID: CS-3 -- Cross-Role Access Differential Expectations.
SE-updatable columns as declared by CA in Phase 0 Schema Registry: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged: SE populates after SE-1/SE-3 analysis.
Expectation format confirmed: CS-3 uses declared column schema. SE-updatable columns left blank.

### CS-1 -- Expected Customer Service Access Baseline

For each entity in scope: (a) expected CRUD operations for normal CS job function; (b) expected
record scope; (c) which sensitive fields CS needs access to and why. Identify configurations
that may inadvertently expand CS access beyond job requirements.

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

*SE-0 establishes admin-tier ceiling and TABLE_4 before SE-1. TABLE_1 and TABLE_3 include Tier
column. SE-2/SE-3/SE-4 use exact-label two-part closure blocks per SHALL-G.*

### SE-0 -- Admin-Tier Inventory and Escalation Vectors (executes before TABLE_1)

**Admin-tier role inventory:** List System Administrator, Environment Admin, and any
admin-equivalent roles with record scope and key capabilities. Note admin capabilities that
bypass lower-tier controls. This establishes the privilege ceiling for all lower-tier roles.

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

**TABLE_1 -- Role-Operation Matrix** *(Schema Registry TABLE_1 with Tier column)*

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Rows ordered by tier. After TABLE_1: populate CS-3 SE Cross-Reference and SE Confirmation.

**Cross-role differential analysis:** Compare CS role against at least one Admin-tier and one
Custom-tier role. Cite SE-0 TABLE_4 data for differentials attributable to admin-tier escalation.

### SE-2 / SHALL-B -- Section 2: Field-Level Security Coverage

MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:
Column security profiles are not auditable from the security roles UI; administrators discover
missing FLS only after a data exposure event reveals that a sensitive field was readable or
writable by an unintended role.

STRUCTURED CLOSE:
TABLE_2 below enumerates every sensitive field with explicit FLS status (Configured / Not
Configured), surfacing pre-event what the security roles UI conceals. All Not Configured
sensitive fields are forwarded to TABLE_5 as MISSING-FLS gaps.

**TABLE_2 -- FLS Coverage** *(Schema Registry TABLE_2)*

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

**Defense-in-depth layer check:** Identify enforcement layer for at least one sensitive field.

### SE-3 / SHALL-C -- Section 3: Record Access Scope

MANUAL GAP [Blind spot 2 -- Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access produced by a security role
plus owner team membership plus OWD; spot-checking roles individually misses cross-role privilege
accumulation through team inheritance.

STRUCTURED CLOSE:
TABLE_3 maps effective scope for every role by Tier, recording OWD baseline, scope modifier, and
resulting effective scope as a single traceable row.

**TABLE_3 -- Record Scope by Role** *(Schema Registry TABLE_3 with Tier column)*

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
that established the admin-tier ceiling. State whether the divergence is expected and what
sharing-rule interaction (if any) was confirmed or ruled out in SE-0 TABLE_4.

### SE-5 / SHALL-E -- Section 5: Security Gap Inventory

**TABLE_5 -- Security Gap Inventory** *(Schema Registry TABLE_5 with Tier column)*

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
labeled elements. Verification line follows. Inline concatenation fails C-24.*

**CA-1.1 -- C-01 verification** *(Phase 0 M4 pre-assignment CA-1.1)*:
- Registry anchor -- Schema ID TABLE_1 (with Tier): [Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope] -- blank cells prohibited globally.
- Preamble anchor -- C-01 as authored by CA in Phase 0: TABLE_1 / SE-1 / SHALL-A / CA-1.1 -- verifying...
- Verification -- TABLE_1 present? Tier column populated? Rows ordered by tier? All cells filled? -> PASS / FAIL

**CA-1.2 -- C-02 verification** *(Phase 0 M4 pre-assignment CA-1.2)*:
- Registry anchor -- Schema ID TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?] -- blank cells prohibited globally.
- Preamble anchor -- C-02 as authored by CA in Phase 0: TABLE_2 / SE-2 / SHALL-B / CA-1.2 -- verifying...
- Verification -- TABLE_2 present? Sensitive fields covered? FLS status explicit? Null case stated? Gap? YES in TABLE_5? -> PASS / FAIL

**CA-1.3 -- C-03 verification** *(Phase 0 M4 pre-assignment CA-1.3)*:
- Registry anchor -- Schema ID TABLE_3 (with Tier): [Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Verified?] -- blank cells prohibited globally.
- Preamble anchor -- C-03 as authored by CA in Phase 0: TABLE_3 / SE-0+SE-3 / SHALL-C / CA-1.3 -- verifying...
- Verification -- Every TABLE_1 role in TABLE_3? Tier column populated? Effective Scope filled? -> PASS / FAIL

**CA-1.4 -- C-04 verification** *(Phase 0 M4 pre-assignment CA-1.4)*:
- Registry anchor -- Schema ID TABLE_4: [Vector, Checked?, Finding, Severity] -- all four vectors, Checked? = YES.
- Preamble anchor -- C-04 as authored by CA in Phase 0: TABLE_4 / SE-0 / SHALL-D / CA-1.4 -- verifying...
- Verification -- TABLE_4 at SE-0 (before SE-1)? All four vectors? Findings or specific rule-outs? -> PASS / FAIL

**CA-1.5 -- C-05 verification** *(Phase 0 M4 pre-assignment CA-1.5)*:
- Registry anchor -- Schema ID TABLE_5 (with Tier): [#, Gap Type, Entity, Field or Rule, Role, Tier, Severity, Remediation] -- blank cells prohibited globally.
- Preamble anchor -- C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 -- verifying...
- Verification -- TABLE_5 present? Named gap? Tier populated? Remediations exact? -> PASS / FAIL

**CA-1.6 -- SHALL-F compliance verification** *(CS-EXPECTATION-VIOLATED three-field structure)*:
- Registry anchor -- Schema ID TABLE_5 CS-EXPECTATION-VIOLATED row: [CS-Expected, SE-Actual, Delta] -- all three required per SHALL-F.
- Preamble anchor -- SHALL-F as authored by CA in Phase 0: three-field block mandatory; incomplete rows reopened.
- Verification -- Each CS-EXPECTATION-VIOLATED row: CS-Expected? SE-Actual? Delta exact? -> PASS / FAIL per row.

**CA-1.7 -- SHALL-G compliance verification** *(exact-label two-part closure blocks)*:
- Registry anchor -- CONTEXT section exact labels: "Blind spot 1 -- Post-incident FLS gap" (SE-2), "Blind spot 2 -- Cumulative privilege blind spot" (SE-3), "Blind spot 3 -- OWD-sharing-rule override gap" (SE-4). SHALL-G requires two-part blocks with exact bracketed label.
- Preamble anchor -- SHALL-G as authored by CA in Phase 0: Line 1 MUST be `MANUAL GAP [<exact CONTEXT label>]:`; paraphrase fails; single-line annotation fails; CA-1.7 verifies.
- Verification -- SE-2 opens with `MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:`? SE-3 with `MANUAL GAP [Blind spot 2 -- Cumulative privilege blind spot]:`? SE-4 with `MANUAL GAP [Blind spot 3 -- OWD-sharing-rule override gap]:`? Each followed by `STRUCTURED CLOSE:`? -> PASS / FAIL per section.

**CA-1.8 -- CS-2/CS-3 Schema Registry registration + CS-0 acknowledgment** *(C-29 + C-33)*:
- Registry anchor -- Schema Registry declared CS-2 and CS-3 as named entries with SE-updatable columns and SE-update protocols. PHASE 1 mandate requires CS-0 to acknowledge both IDs before CS-1.
- Preamble anchor -- CS-2 and CS-3 are Schema Registry entries. CS-0 is a PHASE 1 structural requirement citing both schema IDs and SE-updatable columns before authoring expectation rows.
- Verification -- CS-2 in Registry? CS-3 in Registry? CS-0 before CS-1? CS-0 cites both schema IDs by exact label? SE-updatable columns listed? SE populated per protocol? -> PASS / FAIL

**CA Format Compliance Verdict -- Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0), Phase 0 by label.
[C-01 through C-05 with CA-1.1 through CA-1.5 results. SHALL-F (CA-1.6). SHALL-G exact-label two-part compliance (CA-1.7). C-29+C-33 CS-0 acknowledgment (CA-1.8).]

**TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION (C-36):**
The three Round 12 structural compliance dimensions are each verifiable from this output body
alone, without consulting the prompt. Each dimension's output-body evidence source is named below.

| Dimension | Criterion | Output-Body Evidence Source | Body-Verifiable? |
|-----------|-----------|----------------------------|-----------------|
| Execution order | C-31 | PHASE 2 section header "SE-0 -- Admin-Tier Inventory and Escalation Vectors (executes before TABLE_1)" precedes SE-1; TABLE_4 populated at SE-0 before TABLE_1 at SE-1; ordering is readable from section header sequence and table placement in the output body alone | CONFIRMED |
| Closure-note format | C-32 | MANUAL GAP [exact label] / STRUCTURED CLOSE two-part structure at SE-2, SE-3, SE-4 -- the bracket pattern and two-line format are body-readable by structure alone; a reader can identify each anchor by reading the block structure without evaluating prompt instructions | CONFIRMED |
| CS self-reference | C-33 | CS-0 sub-section cites "Schema ID: CS-2" and "Schema ID: CS-3" by exact Registry ID labels before CS-1; a reader can verify the CS-to-Registry link by reading CS-0 alone, without cross-referencing the Schema Registry entries and CS table schemas independently | CONFIRMED |

Overall compliance: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.

---

"""

with open("C:/src/sim/simulations/quest/golden/trace-permissions-variate-R13-2026-03-16.md", "a", encoding="utf-8") as f:
    f.write(content)
print("V-03 appended.")
