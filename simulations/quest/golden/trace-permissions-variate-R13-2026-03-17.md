# trace-permissions Variate — Round 13
**Date:** 2026-03-17
**Rubric:** v12 (C-01 through C-36, denominator 28)
**Target:** 28/28 — add C-34 (preamble axis declaration), C-35 (SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference + CA-1.9), C-36 (CA terminal tri-dimensional self-evidence attestation)

**State entering Round 13:**

| Variation | v12 score | Notes |
|-----------|-----------|-------|
| R12-V-05 | 98.9 (25/28) | Full C-31+C-32+C-33; no axis declaration, no CA-1.9, no tri-dimensional attestation |
| R12-V-02 | 98.6 (24/28) | C-31+C-33 combined; missing C-32 blocks all three new criteria |
| R12-V-01 | 98.2 (23/28) | C-32 only; missing C-31+C-33 blocks all three new criteria |
| R12-V-03 | 97.9 (22/28) | Phrasing register; no R12 axes; fails C-34/C-35/C-36 by dependency |
| R12-V-04 | 97.9 (22/28) | TABLE_3 expansion; no R12 axes; fails C-34/C-35/C-36 by dependency |

Path to 28/28: R12-V-05 base + C-34 (axis non-interference declaration in preamble) + C-35 (SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference with CA-1.9) + C-36 (CA terminal tri-dimensional self-evidence attestation). All three are additive on R12-V-05; none conflict.

---

## Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Single-axis C-35: SE-4 STRUCTURED CLOSE TABLE_4 SE-0 cross-reference + CA-1.9 pre-assignment | R12-V-05 base. SE-4's STRUCTURED CLOSE gains an SE-0-slot TABLE_4 row cross-reference naming a specific vector row. CA-1.9 pre-assigned in Phase 0 and verified in Phase 3 as distinct from CA-1.4 (SE-0 ordering) and CA-1.7 (MANUAL GAP labels). Hypothesis: 26/28 (adds C-35; misses C-34, C-36). |
| V-02 | Single-axis C-34: preamble R12 axis declaration | R12-V-05 base. Step 0.2 gains a named R12 STRUCTURAL AXIS DECLARATION block after the preamble table, naming execution order / closure-note format / CS self-reference as orthogonal dimensions with explicit non-interference statement. No TABLE_4 SE-0 cross-ref, no tri-dimensional attestation. Hypothesis: 26/28 (adds C-34; misses C-35, C-36). |
| V-03 | Single-axis C-36: tri-dimensional CA terminal self-evidence attestation | R12-V-05 base. Terminal verdict gains a TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION block naming each R12 dimension (execution order / closure-note format / CS self-reference) with its specific output-body evidence source. No axis declaration, no TABLE_4 SE-0 cross-ref. Hypothesis: 26/28 (adds C-36; misses C-34, C-35). |
| V-04 | Combined C-34+C-35: preamble axis declaration + SE-4 TABLE_4 SE-0 cross-reference + CA-1.9 | V-02 + V-01 on R12-V-05 base. Both preamble axis declaration and SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference active simultaneously. No tri-dimensional attestation. Hypothesis: 27/28 (adds C-34+C-35; misses C-36). |
| V-05 | Full combination C-34+C-35+C-36: the 28/28 candidate | V-04 + tri-dimensional CA terminal attestation. All three new criteria active on R12-V-05 base. Hypothesis: 28/28. |

---

## V-01 — Single-Axis C-35: SE-4 STRUCTURED CLOSE TABLE_4 Row Cross-Reference

**Axis:** C-35 — SE-4's STRUCTURED CLOSE block carries a TABLE_4 row cross-reference at the
SE-0 slot. CA-1.9 is pre-assigned in Phase 0 and verified in Phase 3 as an audit target distinct
from CA-1.4 (which verifies SE-0 execution ordering) and CA-1.7 (which verifies MANUAL GAP exact
labels). R12-V-05 full architecture preserved. No preamble axis declaration (C-34 not targeted).
No tri-dimensional terminal attestation (C-36 not targeted).
**Hypothesis:** 26/28 (adds C-35; misses C-34, C-36).

---

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

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins.

**PHASE 0 — CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1: TABLE_1 through TABLE_5 with Tier
columns on TABLE_1 and TABLE_3; CS-2 and CS-3 with SE-updatable columns and SE-update protocols
— seven schemas total) and the Criterion Enforcement Matrix preamble (Step 0.2: SHALL-A through
SHALL-G, M4 row IDs CA-1.1 through CA-1.9 pre-assigned). CA issues handoff to PHASE 1.

Note: CA-1.9 is pre-assigned in Step 0.2 to verify the SE-4 STRUCTURED CLOSE TABLE_4 row
cross-reference at the SE-0 slot. CA-1.9 is a distinct audit target from CA-1.4 (which verifies
TABLE_4 execution at SE-0 before SE-1) and CA-1.7 (which verifies exact-label MANUAL GAP blocks).

**PHASE 1 — CS (Customer Success):**
Executes second. Opens with CS-0 sub-section (Schema Registry acknowledgment: CS echoes Registry
schema IDs for CS-2 and CS-3 by exact Schema ID label, lists SE-updatable columns for each, and
confirms the expectation format before authoring any expectation rows). Then produces CS-1, CS-2,
CS-3 using Registry schemas. CS does not fill TABLE_1-5. CS issues handoff to PHASE 2.

**PHASE 2 — SE (Security Engineer / Dataverse Security Expert):**
Executes third in privilege-tier descent order. SE-0 (admin-tier inventory and TABLE_4 escalation
vectors) runs before SE-1 (role-operation matrix), establishing the privilege ceiling before
populating operation cells. TABLE_1 and TABLE_3 include Tier column. SE-2, SE-3, SE-4 each open
with two-part exact-label closure blocks per SHALL-G. SE-4 STRUCTURED CLOSE carries a TABLE_4
row cross-reference at the SE-0 slot naming a specific TABLE_4 vector row. SE-4 cites SE-0 data
in cross-tier differential. Issues handoff to PHASE 3.

**PHASE 3 — CA-1 (CA Verification Pass):**
CA returns. Each CA-1 row performs double-anchor reaffirmation: Registry anchor and Preamble
anchor as structurally distinct labeled elements. Verification line follows. Inline concatenation
fails C-24. CA-1.8 verifies CS-0 acknowledgment precedes CS-1. CA-1.9 verifies SE-4 STRUCTURED
CLOSE TABLE_4 row cross-reference at SE-0 slot, distinct from CA-1.4 and CA-1.7.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1 and 0.2 before any other phase begins.*

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

**All table schemas declared centrally by CA. Blank-cell prohibition is global — individual
tables do not restate it. SE-update protocols for CS-2 and CS-3 declared co-located with schema
entry.**

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Tier values: Admin / Custom / Restricted. Rows ordered: Admin tier first, Custom second,
Restricted last. Blank-cell rule: all cells Granted / Denied / Conditional (condition inline) / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Blank-cell rule: FLS Profile Configured? = Configured / Not Configured (never blank). Gap? = YES / NO.

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Tier values mirror TABLE_1. Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU /
Org-wide / Team-scoped / Sharing-[rule name]. Verified? = YES / NO.

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
Blank-cell rule: all four vectors (team inheritance, sharing rules, impersonation, admin/env roles),
Checked? = YES, Finding = escalation path or specific rule-out (never blank).
Note: TABLE_4 executes at SE-0 before SE-1 because admin-tier role structure determines escalation
paths before the lower-tier role-operation matrix is populated. SE-4's STRUCTURED CLOSE block SHALL
carry a TABLE_4 row cross-reference at its SE-0 slot, naming a specific TABLE_4 vector row by
vector name to anchor the closure note to a concrete TABLE_4 finding.

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation`
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

**Pre-assigned supplementary CA verification rows (Phase 0):**

| Row ID | What it verifies | Scope | Distinct from |
|--------|-----------------|-------|---------------|
| CA-1.6 | SHALL-F: CS-EXPECTATION-VIOLATED three-field structure | TABLE_5 CS-EV rows | — |
| CA-1.7 | SHALL-G: exact-label MANUAL GAP two-part block at SE-2/SE-3/SE-4 | SE-2, SE-3, SE-4 openings | CA-1.9 |
| CA-1.8 | CS-2/CS-3 Schema Registry registration + CS-0 acknowledgment precedes CS-1 | Phase 1 CS-0 | — |
| CA-1.9 | SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 slot | SE-4 STRUCTURED CLOSE | CA-1.4 (SE-0 ordering), CA-1.7 (MANUAL GAP labels) |

CA-1.9 scope clarification: CA-1.4 verifies that TABLE_4 executes at SE-0 (before SE-1). CA-1.7
verifies that the MANUAL GAP exact-label block appears at SE-4's opening. CA-1.9 verifies that
SE-4's STRUCTURED CLOSE block contains a TABLE_4 row cross-reference at the SE-0 slot — that
is, the first named element of the STRUCTURED CLOSE names a specific TABLE_4 vector row by its
exact vector label. These are three non-overlapping audit targets on the same SE-4 section.

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A: Complete TABLE_1 with Tier column. Every cell Granted/Denied/Conditional/N/A. Rows ordered by tier.
- SHALL-B: TABLE_2 lists all PII, Financial, and Audit-Compliance fields with explicit FLS status. Null case explicit. Gap? YES rows in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier and Effective Scope filled. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 at SE-0 (before SE-1), all four vectors, Checked? = YES. Rule-outs name specific mechanism and reason.
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap case requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field Remediation block (CS-Expected, SE-Actual, Delta). Incomplete rows MUST be reopened. CA-1.6 verifies.
- SHALL-G: At the opening of SE-2, SE-3, and SE-4, closure MUST appear as a two-part labeled block — Line 1: `MANUAL GAP [<exact CONTEXT label>]:` where <exact CONTEXT label> is the label character-for-character as written in the CONTEXT section (e.g., "Blind spot 1 — Post-incident FLS gap"); Line 2: description of what manual audits miss; Line 3: `STRUCTURED CLOSE:`; Line 4: which table and mechanism closes it. Additionally, SE-4's STRUCTURED CLOSE block SHALL carry a TABLE_4 row cross-reference at the SE-0 slot: the SE-0 slot names a specific TABLE_4 vector row (by exact vector label) as the concrete anchor for this section's closure. CA-1.7 verifies the exact-label MANUAL GAP block; CA-1.9 verifies the TABLE_4 SE-0 slot cross-reference as a separate audit target.

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

*CS opens with CS-0 Registry acknowledgment before authoring any expectation content.*

### CS-0 — Schema Registry Acknowledgment (CS-authored, Phase 1)

CS echoes the Schema Registry entries for CS-2 and CS-3 from Phase 0 before authoring expectation
rows. This sub-section confirms the handoff from CA's Registry to CS's authoring task.

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
TABLE_4 before SE-1. TABLE_1 and TABLE_3 include Tier column. SE-2/SE-3/SE-4 use exact-label
two-part closure blocks per SHALL-G. SE-4's STRUCTURED CLOSE carries a TABLE_4 row cross-
reference at the SE-0 slot naming a specific TABLE_4 vector row.*

### SE-0 — Admin-Tier Inventory and Escalation Vectors (executes before TABLE_1)

**Admin-tier role inventory:** List System Administrator, Environment Admin, and any
admin-equivalent roles with record scope and key capabilities. Note any admin capability that
bypasses lower-tier controls (e.g., System Administrator bypasses column security profiles).
This establishes the privilege ceiling for all lower-tier roles in SE-1.

**TABLE_4 — Escalation Vector Inventory** *(Schema Registry TABLE_4; placed at SE-0 because
admin-tier role structure determines escalation paths; TABLE_1 rows are interpreted relative to
the ceiling established here)*

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Finding format: `[Role] -> [Mechanism] -> [Elevated access achieved]` for confirmed escalation;
for rule-out: "Checked [mechanism]: no path found because [specific reason naming the configuration
examined]." After TABLE_4: populate SE Cross-Reference and SE Confirmation in CS-2. Enter
CONTRADICTED rows as CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

### SE-1 / SHALL-A — Section 1: Role-Operation Matrix

**TABLE_1 — Role-Operation Matrix** *(Schema Registry TABLE_1 with Tier; blank-cell rule)*

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Include every role with any privilege on any entity in {{topic}}. Admin-tier rows first.
After the table: cross-reference CS-3's expected access differential — note which rows confirm CS
expectations (with CS-3 row reference) and which contradict (triggers CS-EXPECTATION-VIOLATED).

**Cross-role differential analysis:** Compare the CS role against at least one more privileged role
for the same entity and operation. State whether the access differential is expected (least
privilege satisfied) or anomalous, and why.

### SE-2 / SHALL-B — Section 2: Field-Level Security Coverage

MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:
Column security profiles are not auditable from the security roles UI; administrators discover
missing FLS only after a data exposure event reveals that a sensitive field was readable by an
unintended role.

STRUCTURED CLOSE:
TABLE_2 below enumerates every sensitive field in scope with its explicit FLS status (Configured /
Not Configured), surfacing pre-event what the security roles UI conceals. All Not Configured
sensitive fields are forwarded to TABLE_5 as MISSING-FLS gaps.

**TABLE_2 — FLS Coverage** *(Schema Registry TABLE_2; blank-cell rule)*

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Categories: PII / Financial / Audit-Compliance / Other-Sensitive. Null case: "No column security
profiles active on {{topic}}. Sensitive fields identified: [list]. All entered in TABLE_5 as
MISSING-FLS." Forward all Gap? YES rows to TABLE_5.

**Defense-in-depth layer check for FLS:** Identify the enforcement layer (1: environment/admin,
2: security role + BU scope, 3: team membership, 4: column security profile) where field access
is effectively granted or denied for at least one sensitive field. For Admin-tier roles, note the
SE-0 bypass finding.

After TABLE_2: update CS-3 SE Confirmation for any CS-3 row where a sensitive field finding
contradicts CS-3 expectations.

### SE-3 / SHALL-C — Section 3: Record Access Scope

MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access produced by a security role
plus owner team membership plus OWD; spot-checking roles individually misses cross-role privilege
accumulation through team inheritance.

STRUCTURED CLOSE:
TABLE_3 below maps the effective scope for every role by Tier, recording the OWD baseline, the
scope modifier from team or role depth, and the resulting effective scope as a single traceable
row, making team-accumulated privilege visible and auditable at the tier it occurs.

**TABLE_3 — Record Scope by Role** *(Schema Registry TABLE_3 with Tier; blank-cell rule)*

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role MUST appear, ordered by Tier. Note roles where effective scope exceeds
role-only scope due to team membership; flag CS-EXPECTATION-VIOLATED in TABLE_5 if CS-3 expected
the unexpanded scope. After TABLE_3: update CS-3 SE Confirmation.

### SE-4 / SHALL-D — Section 4: Privilege Escalation Cross-Reference

MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing the sharing rules
that silently override them; a Private OWD combined with an active sharing rule can grant
effective org-wide access without appearing in any security roles UI view.

STRUCTURED CLOSE:
SE-0 cross-reference: TABLE_4 row [name the specific TABLE_4 vector row most relevant to
{{topic}}'s escalation surface — e.g., "Team inheritance" or "Sharing rules" — citing the exact
vector label, the Checked? value, and the Finding from the TABLE_4 row populated at SE-0]. This
TABLE_4 row cross-reference anchors this STRUCTURED CLOSE to a specific SE-0 finding; it occupies
the SE-0 slot of this closure block and is the subject of CA-1.9 verification.
TABLE_4 (filled at SE-0) evaluated all four escalation vectors with sharing rules explicitly
cross-referenced against OWD settings. This section adds the cross-tier differential summary
citing SE-0 data: for the most privileged Admin-tier role and the most restricted Restricted-tier
role, identify the specific Dataverse enforcement layer where access diverges, citing the SE-0
TABLE_4 row named above. State whether the divergence is expected and what sharing-rule
interaction (if any) was confirmed or ruled out in SE-0 TABLE_4.

### SE-5 / SHALL-E — Section 5: Security Gap Inventory

**TABLE_5 — Security Gap Inventory** *(Schema Registry TABLE_5 with Tier; blank-cell rule)*

| # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation |
|---|----------|--------|---------------|------|------|----------|-------------|

Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED /
CS-EXPECTATION-VIOLATED. Severity: CRITICAL / HIGH / MEDIUM.

CS-EXPECTATION-VIOLATED rows (three-field Remediation block per SHALL-F):
- CS-Expected: [cite CS-2 or CS-3 row, state expectation verbatim or by row reference]
- SE-Actual: [SE finding that contradicts the expectation]
- Delta: [exact configuration change to align SE-Actual to CS-Expected]

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

*CA returns. Each CA-1 row MUST present Registry anchor and Preamble anchor as structurally
distinct labeled elements before the Verification line. Inline concatenation fails C-24.*

**CA-1.1 — C-01 verification** *(Phase 0 M4 pre-assignment CA-1.1)*:
- Registry anchor — Schema ID TABLE_1 (with Tier): [Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope] — blank cells prohibited globally.
- Preamble anchor — C-01 as authored by CA in Phase 0: TABLE_1 / SE-1 / SHALL-A / CA-1.1 — verifying...
- Verification — TABLE_1 present? Tier column populated? Rows ordered by tier? All cells filled? -> PASS / FAIL

**CA-1.2 — C-02 verification** *(Phase 0 M4 pre-assignment CA-1.2)*:
- Registry anchor — Schema ID TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?] — blank cells prohibited globally.
- Preamble anchor — C-02 as authored by CA in Phase 0: TABLE_2 / SE-2 / SHALL-B / CA-1.2 — verifying...
- Verification — TABLE_2 present? All sensitive fields? FLS status explicit? Null case stated? Gap? YES in TABLE_5? -> PASS / FAIL

**CA-1.3 — C-03 verification** *(Phase 0 M4 pre-assignment CA-1.3)*:
- Registry anchor — Schema ID TABLE_3 (with Tier): [Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Verified?] — blank cells prohibited globally.
- Preamble anchor — C-03 as authored by CA in Phase 0: TABLE_3 / SE-0+SE-3 / SHALL-C / CA-1.3 — verifying...
- Verification — Every TABLE_1 role in TABLE_3? Tier column populated? Effective Scope filled? -> PASS / FAIL

**CA-1.4 — C-04 verification** *(Phase 0 M4 pre-assignment CA-1.4)*:
- Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity] — all four vectors, Checked? = YES.
- Preamble anchor — C-04 as authored by CA in Phase 0: TABLE_4 / SE-0 / SHALL-D / CA-1.4 — verifying...
- Verification — TABLE_4 at SE-0 (before SE-1)? All four vectors? Findings or specific rule-outs? -> PASS / FAIL
- Note: CA-1.4 verifies SE-0 execution ordering only. SE-4 STRUCTURED CLOSE content is CA-1.9's scope.

**CA-1.5 — C-05 verification** *(Phase 0 M4 pre-assignment CA-1.5)*:
- Registry anchor — Schema ID TABLE_5 (with Tier): [#, Gap Type, Entity, Field or Rule, Role, Tier, Severity, Remediation] — blank cells prohibited globally.
- Preamble anchor — C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 — verifying...
- Verification — TABLE_5 present? Named gap? Tier column populated? Remediations exact? -> PASS / FAIL

**CA-1.6 — SHALL-F compliance verification** *(CS-EXPECTATION-VIOLATED three-field structure)*:
- Registry anchor — Schema ID TABLE_5 CS-EXPECTATION-VIOLATED row: [CS-Expected field, SE-Actual field, Delta field] — all three required per SHALL-F declaration in Phase 0.
- Preamble anchor — SHALL-F as authored by CA in Phase 0: three-field Remediation block mandatory; rows missing any field MUST be reopened.
- Verification — For each CS-EXPECTATION-VIOLATED row: CS-Expected populated? SE-Actual populated? Delta populated with exact configuration change? -> PASS / FAIL per row.

**CA-1.7 — SHALL-G compliance verification** *(exact-label MANUAL GAP two-part closure blocks)*:
- Registry anchor — CONTEXT section declared exact labels: "Blind spot 1 — Post-incident FLS gap" (SE-2 target), "Blind spot 2 — Cumulative privilege blind spot" (SE-3 target), "Blind spot 3 — OWD-sharing-rule override gap" (SE-4 target). SHALL-G requires two-part blocks with exact label in brackets.
- Preamble anchor — SHALL-G as authored by CA in Phase 0: Line 1 MUST be `MANUAL GAP [<exact CONTEXT label>]:`; exact = character-for-character; paraphrase fails; CA-1.7 verifies.
- Verification — SE-2 opens with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:`? Followed by `STRUCTURED CLOSE:`? SE-3/SE-4 same pattern? -> PASS / FAIL per section.
- Note: CA-1.7 verifies the MANUAL GAP label format only. SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference is CA-1.9's scope.

**CA-1.8 — CS-2/CS-3 Schema Registry registration + CS-0 acknowledgment verification** *(C-29 + C-33)*:
- Registry anchor — Schema Registry declared CS-2 as named schema entry with SE-updatable columns SE Cross-Reference and SE Confirmation and SE-update protocol co-located. Schema Registry declared CS-3 same. PHASE 1 mandate requires CS-0 sub-section to acknowledge both schema IDs and list SE-updatable columns before CS-1/CS-2/CS-3.
- Preamble anchor — CS-2 and CS-3 are Schema Registry entries alongside TABLE_1-5. CS-0 acknowledgment is a PHASE 1 structural requirement. CA-1.8 verifies.
- Verification — CS-2 in Registry? CS-3 in Registry? CS-0 present before CS-1? CS-0 cites both schema IDs and SE-updatable columns? SE populated SE-updatable columns per protocol? -> PASS / FAIL

**CA-1.9 — SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 slot** *(C-35; pre-assigned
in Phase 0; distinct audit target from CA-1.4 and CA-1.7)*:
- Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity]. Note declared in Phase 0 Schema Registry: "SE-4's STRUCTURED CLOSE block SHALL carry a TABLE_4 row cross-reference at its SE-0 slot, naming a specific TABLE_4 vector row by vector label."
- Preamble anchor — CA-1.9 pre-assigned in Phase 0 supplementary rows: "SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 slot | SE-4 STRUCTURED CLOSE | Distinct from CA-1.4 (SE-0 ordering), CA-1.7 (MANUAL GAP labels)."
- Verification — SE-4's STRUCTURED CLOSE block begins with an SE-0 slot entry? The SE-0 slot names a specific TABLE_4 vector row by its exact vector label? The named row was populated at SE-0 with Checked?=YES and a Finding? This cross-reference is present in the STRUCTURED CLOSE block itself (not in the MANUAL GAP block, not in TABLE_5)? -> PASS / FAIL
- Distinction: CA-1.4 verified TABLE_4 execution at SE-0 (before SE-1). CA-1.7 verified the MANUAL GAP exact-label block at SE-4's opening. CA-1.9 verifies the TABLE_4 row cross-reference inside SE-4's STRUCTURED CLOSE block — a separate structural element on the same SE-4 section.

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0), Phase 0 by label.
[CA-1.1 through CA-1.5 results. SHALL-F (CA-1.6). SHALL-G exact-label two-part block compliance (CA-1.7). C-29 + C-33 CS-0 acknowledgment (CA-1.8). C-35 SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference (CA-1.9). Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

---

## V-02 — Single-Axis C-34: Preamble R12 Structural Axis Declaration

**Axis:** C-34 — Step 0.2 Criterion Enforcement Matrix preamble gains a named R12 STRUCTURAL
AXIS DECLARATION block after the enforcement table, explicitly declaring execution order /
closure-note format / CS self-reference as three orthogonal R12 dimensions with a binding
non-interference statement. This converts R12-V-05's empirically demonstrated composability into
a contractual declaration. No TABLE_4 SE-0 cross-ref added (C-35 not targeted). No tri-dimensional
terminal attestation (C-36 not targeted). All other R12-V-05 mechanisms preserved.
**Hypothesis:** 26/28 (adds C-34; misses C-35, C-36).

---

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

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins.

**PHASE 0 — CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1: seven schemas total — TABLE_1 through
TABLE_5 with Tier columns on TABLE_1 and TABLE_3; CS-2 and CS-3 with SE-updatable columns and
update protocols) and the Criterion Enforcement Matrix preamble (Step 0.2: SHALL-A through SHALL-G,
M4 row IDs CA-1.1 through CA-1.8 pre-assigned, plus R12 Structural Axis Declaration). CA issues
handoff to PHASE 1.

**PHASE 1 — CS (Customer Success):**
Executes second. Opens with CS-0 sub-section (Schema Registry acknowledgment). Then produces
CS-1, CS-2, CS-3 using Registry schemas. CS does not fill TABLE_1-5. CS issues handoff to PHASE 2.

**PHASE 2 — SE (Security Engineer / Dataverse Security Expert):**
Executes third in privilege-tier descent order. SE-0 (admin-tier inventory and TABLE_4) runs
before SE-1. TABLE_1 and TABLE_3 include Tier column. SE-2/SE-3/SE-4 use exact-label two-part
closure blocks per SHALL-G. SE-4 cites SE-0 data. Issues handoff to PHASE 3.

**PHASE 3 — CA-1 (CA Verification Pass):**
CA returns. Double-anchor reaffirmation per row. CA-1.8 verifies CS-0 acknowledgment precedes CS-1.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1 and 0.2 before any other phase begins.*

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

**All table schemas declared centrally by CA. Blank-cell prohibition is global. SE-update
protocols for CS-2 and CS-3 declared co-located with schema entry.**

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Tier values: Admin / Custom / Restricted. Rows ordered Admin first. Blank-cell rule: all cells
Granted / Denied / Conditional (condition inline) / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Blank-cell rule: FLS Profile Configured? = Configured / Not Configured. Gap? = YES / NO.

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Tier values mirror TABLE_1. Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU /
Org-wide / Team-scoped / Sharing-[rule name]. Verified? = YES / NO.

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
Blank-cell rule: all four vectors, Checked? = YES, Finding = escalation path or specific rule-out.
Note: TABLE_4 executes at SE-0 before SE-1.

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation`
Blank-cell rule: Remediation = exact object + exact location + expected post-fix state.
CS-EXPECTATION-VIOLATED Remediation (three-field block): CS-Expected / SE-Actual / Delta.

**Schema ID: CS-2 — Sharing Rule Expectations**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference, SE Confirmation. SE update protocol: after SE-0 TABLE_4.

**Schema ID: CS-3 — Cross-Role Access Differential Expectations**
Declared columns: `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference, SE Confirmation. SE update protocol: after SE-1/SE-3.

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: M1, M2, M3 simultaneously active. M4 pre-assigned.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-0 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**R12 STRUCTURAL AXIS DECLARATION (authored by CA, Phase 0):**

This output activates three structural dimensions introduced in the R12 criterion set. These
dimensions are orthogonal: they govern distinct structural properties of the output and do not
interact with each other's enforcement mechanisms. Activating one dimension neither enables nor
disables another.

| R12 Dimension | Label | Structural Property Governed | Output-Body Evidence |
|---------------|-------|------------------------------|----------------------|
| Dimension 1 | Execution order | TABLE_4 at SE-0 (before SE-1); Tier columns in TABLE_1/TABLE_3; SE-4 cites SE-0 TABLE_4 row | SE-0 section precedes SE-1 in Phase 2 output |
| Dimension 2 | Closure-note format | Exact-label two-part MANUAL GAP / STRUCTURED CLOSE blocks at SE-2, SE-3, SE-4 openings | MANUAL GAP [<exact label>]: / STRUCTURED CLOSE: present at each |
| Dimension 3 | CS self-reference | CS-0 Registry acknowledgment sub-section cites CS-2 and CS-3 schema IDs and SE-updatable columns before CS-1 | CS-0 present before CS-1 in Phase 1 output |

**Non-interference statement:** Dimension 1 (execution order) governs SE section sequencing and
TABLE_1/TABLE_3 column structure. Dimension 2 (closure-note format) governs the exact textual
structure of closure blocks within SE-2, SE-3, and SE-4. Dimension 3 (CS self-reference) governs
CS's Phase 1 opening sub-section. No dimension's enforcement mechanism overlaps with another's.
Satisfying one dimension does not satisfy or exempt any other. A model that elides any dimension
on the basis that another dimension provides equivalent coverage fails C-34's non-interference
contract. CA-1.7 verifies Dimension 2; CA-1.8 verifies Dimension 3; CA-1.4 verifies Dimension 1.

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A: Complete TABLE_1 with Tier column. Every cell Granted/Denied/Conditional/N/A. Rows ordered by tier.
- SHALL-B: TABLE_2 lists all PII, Financial, and Audit-Compliance fields with explicit FLS status. Null case explicit. Gap? YES rows in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier and Effective Scope filled. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 at SE-0 (before SE-1), all four vectors, Checked? = YES. Rule-outs name specific mechanism and reason.
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap case requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field Remediation block (CS-Expected, SE-Actual, Delta). Incomplete rows MUST be reopened. CA-1.6 verifies.
- SHALL-G: At the opening of SE-2, SE-3, and SE-4, closure MUST appear as a two-part labeled block — Line 1: `MANUAL GAP [<exact CONTEXT label>]:`; Line 2: description; Line 3: `STRUCTURED CLOSE:`; Line 4: closing mechanism. Exact label required; paraphrase fails. CA-1.7 verifies.

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

*CS opens with CS-0 Registry acknowledgment before authoring any expectation content.*

### CS-0 — Schema Registry Acknowledgment (CS-authored, Phase 1)

**Registry acknowledgment for CS-2:**
Schema ID: CS-2 — Sharing Rule Expectations.
SE-updatable columns as declared by CA in Phase 0 Schema Registry: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged: SE populates after SE-0/TABLE_4 analysis.
Expectation format confirmed. SE-updatable columns left blank; SE fills after SE-0.

**Registry acknowledgment for CS-3:**
Schema ID: CS-3 — Cross-Role Access Differential Expectations.
SE-updatable columns as declared by CA in Phase 0 Schema Registry: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged: SE populates after SE-1/SE-3 analysis.
Expectation format confirmed. SE-updatable columns left blank; SE fills after SE-1/SE-3.

### CS-1 — Expected Customer Service Access Baseline

For each entity in scope: (a) CRUD operations expected for normal CS job function; (b) expected
record scope; (c) sensitive fields CS needs and why. Identify configurations that may open access
beyond job requirements.

**CS-2 — Sharing rule expectations** *(Schema Registry CS-2; SE-updatable columns blank)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

**CS-3 — Cross-role access differential** *(Schema Registry CS-3; SE-updatable columns blank)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis (Privilege-Tier Descent Order)

*SE-0 establishes admin-tier ceiling and TABLE_4 before SE-1. R12 Dimension 1 (execution order)
active. TABLE_1 and TABLE_3 include Tier column. SE-2/SE-3/SE-4 use exact-label two-part closure
blocks (R12 Dimension 2). CS-0 Registry acknowledgment completed in Phase 1 (R12 Dimension 3).*

### SE-0 — Admin-Tier Inventory and Escalation Vectors (executes before TABLE_1)

**Admin-tier role inventory:** List System Administrator, Environment Admin, and admin-equivalent
roles with record scope and key capabilities. Note admin bypasses of lower-tier controls.

**TABLE_4 — Escalation Vector Inventory** *(Schema Registry TABLE_4; SE-0 placement per SHALL-D)*

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

After TABLE_4: populate SE Cross-Reference and SE Confirmation in CS-2. Enter CONTRADICTED rows
as CS-EXPECTATION-VIOLATED in TABLE_5.

### SE-1 / SHALL-A — Section 1: Role-Operation Matrix

**TABLE_1 — Role-Operation Matrix** *(Schema Registry TABLE_1 with Tier; blank-cell rule)*

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Cross-reference CS-3 expectations after table. Cross-role differential: compare CS role against
one more privileged role; state whether differential is expected or anomalous.

### SE-2 / SHALL-B — Section 2: Field-Level Security Coverage

MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:
Column security profiles are not auditable from the security roles UI; administrators discover
missing FLS only after a data exposure event reveals that a sensitive field was readable by an
unintended role.

STRUCTURED CLOSE:
TABLE_2 below enumerates every sensitive field in scope with its explicit FLS status, surfacing
pre-event what the security roles UI conceals. All Not Configured sensitive fields are forwarded
to TABLE_5 as MISSING-FLS gaps.

**TABLE_2 — FLS Coverage** *(Schema Registry TABLE_2; blank-cell rule)*

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Defense-in-depth layer check: identify enforcement layer for at least one sensitive field.

### SE-3 / SHALL-C — Section 3: Record Access Scope

MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access produced by a security role
plus owner team membership plus OWD; spot-checking roles misses team-accumulated privilege.

STRUCTURED CLOSE:
TABLE_3 below maps effective scope for every role by Tier, recording OWD baseline, scope modifier,
and resulting effective scope as a single traceable row.

**TABLE_3 — Record Scope by Role** *(Schema Registry TABLE_3 with Tier; blank-cell rule)*

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|

After TABLE_3: update CS-3 SE Confirmation.

### SE-4 / SHALL-D — Section 4: Privilege Escalation Cross-Reference

MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:
Administrators audit OWD settings without cross-referencing sharing rules that silently override
them; a Private OWD combined with an active sharing rule can grant effective org-wide access
without appearing in any security roles UI view.

STRUCTURED CLOSE:
TABLE_4 (filled at SE-0) evaluated all four escalation vectors with sharing rules explicitly
cross-referenced against OWD settings. This section adds the cross-tier differential summary
citing SE-0 data: for the most privileged Admin-tier role and the most restricted Restricted-tier
role, identify the specific enforcement layer where access diverges, citing the SE-0 TABLE_4 row
ID that established the admin-tier ceiling. State whether the divergence is expected and what
sharing-rule interaction (if any) was confirmed or ruled out in SE-0 TABLE_4.

### SE-5 / SHALL-E — Section 5: Security Gap Inventory

**TABLE_5 — Security Gap Inventory** *(Schema Registry TABLE_5 with Tier; blank-cell rule)*

| # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation |
|---|----------|--------|---------------|------|------|----------|-------------|

CS-EXPECTATION-VIOLATED rows: CS-Expected / SE-Actual / Delta.

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

**CA-1.1 through CA-1.8** *(same double-anchor structure as R12-V-05; see CA-1.1–CA-1.8 in V-01
above — identical text applies here; CA-1.9 is NOT present in this variation)*

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0),
Phase 0 by label, including the R12 Structural Axis Declaration authored in Step 0.2.
[CA-1.1 through CA-1.5. SHALL-F (CA-1.6). SHALL-G (CA-1.7). CS-0 acknowledgment (CA-1.8).
R12 Axis Declaration non-interference contract: all three dimensions active and non-overlapping.
Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

---

## V-03 — Single-Axis C-36: Tri-Dimensional CA Terminal Self-Evidence Attestation

**Axis:** C-36 — CA's terminal verdict gains a TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION block
naming each R12 dimension (execution order / closure-note format / CS self-reference) with its
specific output-body evidence source. This extends C-22's phase-execution self-evidence (which
names Phase 0 by label as a structural basis) to all three R12 dimensions simultaneously. No
preamble axis declaration added (C-34 not targeted). No TABLE_4 SE-0 cross-ref (C-35 not
targeted). Full R12-V-05 architecture preserved.
**Hypothesis:** 26/28 (adds C-36; misses C-34, C-35).

---

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

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins.

**PHASE 0 — CA (Compliance Auditor):**
CA executes first. Authors Schema Registry (Step 0.1: seven schemas) and Criterion Enforcement
Matrix preamble (Step 0.2: SHALL-A through SHALL-G, M4 CA-1.1 through CA-1.8 pre-assigned).
CA issues handoff to PHASE 1.

**PHASE 1 — CS (Customer Success):**
Executes second. Opens with CS-0 Registry acknowledgment. Produces CS-1, CS-2, CS-3. CS does
not fill TABLE_1-5. Issues handoff to PHASE 2.

**PHASE 2 — SE (Security Engineer / Dataverse Security Expert):**
Executes third in privilege-tier descent order. SE-0 establishes admin-tier ceiling and TABLE_4
before SE-1. TABLE_1 and TABLE_3 include Tier column. SE-2/SE-3/SE-4 use exact-label two-part
closure blocks per SHALL-G. SE-4 cites SE-0 data. Issues handoff to PHASE 3.

**PHASE 3 — CA-1 (CA Verification Pass):**
CA returns. Double-anchor reaffirmation per row. CA-1.8 verifies CS-0 precedes CS-1. Terminal
verdict includes TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION naming each R12 dimension with its
specific output-body evidence source.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*(Identical to R12-V-05 / V-02 PHASE 0 — Schema Registry and SHALL obligations unchanged.
Seven schemas: TABLE_1 with Tier, TABLE_2, TABLE_3 with Tier, TABLE_4, TABLE_5 with Tier, CS-2,
CS-3. Preamble: C-01 through C-05 mapping, SHALL-A through SHALL-G, CA-1.1 through CA-1.8.
No axis declaration block. No CA-1.9.)*

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Tier values: Admin / Custom / Restricted. Admin rows first. Blank-cell rule: Granted/Denied/Conditional/N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Blank-cell rule: Configured / Not Configured; YES / NO.

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule].

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
All four vectors, Checked? = YES. TABLE_4 executes at SE-0 before SE-1.

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation`
CS-EXPECTATION-VIOLATED Remediation: CS-Expected / SE-Actual / Delta.

**Schema ID: CS-2 — Sharing Rule Expectations**
SE-updatable: SE Cross-Reference, SE Confirmation. Protocol: after SE-0.

**Schema ID: CS-3 — Cross-Role Access Differential Expectations**
SE-updatable: SE Cross-Reference, SE Confirmation. Protocol: after SE-1/SE-3.

**Criterion Enforcement Matrix Preamble:** C-01/TABLE_1/SE-1/SHALL-A/CA-1.1 | C-02/TABLE_2/SE-2/SHALL-B/CA-1.2 | C-03/TABLE_3/SE-0+SE-3/SHALL-C/CA-1.3 | C-04/TABLE_4/SE-0/SHALL-D/CA-1.4 | C-05/TABLE_5/SE-5/SHALL-E/CA-1.5. M1+M2+M3 simultaneously active. M4 pre-assigned.

**SHALL-A through SHALL-G:** (identical to R12-V-05 — full text as declared in V-01 above).

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

*(Identical structure to R12-V-05: CS-0 Registry acknowledgment, CS-1, CS-2, CS-3.)*

### CS-0 — Schema Registry Acknowledgment (CS-authored, Phase 1)

**Registry acknowledgment for CS-2:** Schema ID: CS-2. SE-updatable columns: SE Cross-Reference,
SE Confirmation. Protocol: SE fills after SE-0/TABLE_4. Columns left blank by CS.

**Registry acknowledgment for CS-3:** Schema ID: CS-3. SE-updatable columns: SE Cross-Reference,
SE Confirmation. Protocol: SE fills after SE-1/SE-3. Columns left blank by CS.

### CS-1 / CS-2 / CS-3 — *(standard content as in R12-V-05)*

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis (Privilege-Tier Descent Order)

*(Identical structure to R12-V-05: SE-0 through SE-5. Full exact-label two-part closure blocks
at SE-2/SE-3/SE-4 per SHALL-G. SE-4 STRUCTURED CLOSE cites SE-0 TABLE_4 row ID. No TABLE_4 SE-0
slot cross-reference in STRUCTURED CLOSE block beyond the existing citation.)*

### SE-0 — Admin-Tier Inventory and Escalation Vectors

TABLE_4 at SE-0. All four vectors, Checked? = YES. Update CS-2 after TABLE_4.

### SE-1 / SE-2 / SE-3 / SE-4 / SE-5 — *(standard content as in R12-V-05)*

SE-2: MANUAL GAP [Blind spot 1 — Post-incident FLS gap]: / STRUCTURED CLOSE:
SE-3: MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]: / STRUCTURED CLOSE:
SE-4: MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]: / STRUCTURED CLOSE:
SE-4 STRUCTURED CLOSE cites SE-0 TABLE_4 row ID in cross-tier differential.

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

*(CA-1.1 through CA-1.8 identical to R12-V-05 double-anchor structure.)*

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0),
Phase 0 by label.
[CA-1.1 through CA-1.8 results. Overall: COMPLIANT / NON-COMPLIANT. Open items attributed.]

**TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION (R12 dimensions, authored by CA in terminal verdict):**

This verdict extends C-22's phase-execution self-evidence to all three R12 structural dimensions.
For each R12 dimension, the specific output-body evidence source is named below. This attestation
is self-referential: the evidence sources cited are sections of this output, verifiable by
inspection without reading the prompt.

| R12 Dimension | Label | Specific Output-Body Evidence Source |
|---------------|-------|--------------------------------------|
| Dimension 1 | Execution order | SE-0 section header in PHASE 2 precedes SE-1 section header; TABLE_4 table appears in SE-0 before any TABLE_1 content; Tier column present in both TABLE_1 and TABLE_3; SE-4 STRUCTURED CLOSE cites a TABLE_4 row ID from SE-0. |
| Dimension 2 | Closure-note format | SE-2 opens with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:` followed by `STRUCTURED CLOSE:`; SE-3 opens with `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:` followed by `STRUCTURED CLOSE:`; SE-4 opens with `MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:` followed by `STRUCTURED CLOSE:`. These three exact-label blocks are present in the Phase 2 output body. |
| Dimension 3 | CS self-reference | CS-0 sub-section appears in PHASE 1 before CS-1; CS-0 cites Schema ID CS-2 and Schema ID CS-3 by exact label; CS-0 lists SE Cross-Reference and SE Confirmation as SE-updatable columns for both schemas. This sub-section is present in the Phase 1 output body. |

All three dimensions are simultaneously active in this output. Their evidence sources are
independent: Dimension 1 evidence is in SE-0 and TABLE_4/TABLE_1/TABLE_3 structure; Dimension 2
evidence is in SE-2/SE-3/SE-4 opening blocks; Dimension 3 evidence is in CS-0. No dimension's
evidence source overlaps with another's.

---

## V-04 — Combined C-34+C-35: Preamble Axis Declaration + SE-4 TABLE_4 SE-0 Cross-Reference

**Axis:** V-02 (C-34: preamble axis declaration) + V-01 (C-35: SE-4 STRUCTURED CLOSE TABLE_4
row cross-reference at SE-0 slot + CA-1.9). Both criteria active simultaneously on R12-V-05 base.
No tri-dimensional terminal attestation (C-36 not targeted).
**Hypothesis:** 27/28 (adds C-34+C-35; misses C-36).

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

*(Identical to V-01/V-02/V-03 — full CONTEXT text with Blind spot 1/2/3 exact labels.)*

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases.

**PHASE 0 — CA:** Authors Schema Registry (seven schemas including TABLE_4 with SE-0 placement
note and SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot requirement) and preamble (SHALL-A through
SHALL-G; M4 CA-1.1 through CA-1.9 pre-assigned; R12 Structural Axis Declaration included).

**PHASE 1 — CS:** CS-0 Registry acknowledgment + CS-1/CS-2/CS-3.

**PHASE 2 — SE:** SE-0 (TABLE_4 before TABLE_1) + SE-1 through SE-5. SE-4 STRUCTURED CLOSE
carries TABLE_4 row cross-reference at SE-0 slot.

**PHASE 3 — CA-1:** CA-1.1 through CA-1.9 double-anchor. CA-1.9 verifies SE-4 STRUCTURED CLOSE
TABLE_4 SE-0 slot cross-reference, distinct from CA-1.4 and CA-1.7.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

*(Schemas TABLE_1 through TABLE_5 with Tier, CS-2, CS-3 — identical to V-01 Step 0.1. TABLE_4
schema note includes: "SE-4's STRUCTURED CLOSE block SHALL carry a TABLE_4 row cross-reference
at its SE-0 slot, naming a specific TABLE_4 vector row by exact vector label.")*

**Schema ID: TABLE_1** — `Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` — Admin/Custom/Restricted, Admin first, no blank cells.

**Schema ID: TABLE_2** — `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?` — Configured/Not Configured, YES/NO.

**Schema ID: TABLE_3** — `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?` — Tier mirrors TABLE_1.

**Schema ID: TABLE_4** — `Vector | Checked? | Finding | Severity` — four vectors, Checked?=YES, TABLE_4 at SE-0. SE-4 STRUCTURED CLOSE SHALL carry TABLE_4 row cross-reference at SE-0 slot naming a specific vector by exact label.

**Schema ID: TABLE_5** — `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation` — CS-EV rows: CS-Expected / SE-Actual / Delta.

**Schema ID: CS-2** — SE-updatable: SE Cross-Reference, SE Confirmation. Protocol: after SE-0.

**Schema ID: CS-3** — SE-updatable: SE Cross-Reference, SE Confirmation. Protocol: after SE-1/SE-3.

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: M1, M2, M3 simultaneously active. M4 pre-assigned.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-0 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**Supplementary CA verification rows (Phase 0 pre-assignment):**

| Row ID | Scope | Distinct from |
|--------|-------|---------------|
| CA-1.6 | SHALL-F three-field CS-EV structure | — |
| CA-1.7 | SHALL-G exact-label MANUAL GAP blocks | CA-1.9 |
| CA-1.8 | CS-2/CS-3 Registry registration + CS-0 precedes CS-1 | — |
| CA-1.9 | SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 slot | CA-1.4 (SE-0 ordering), CA-1.7 (MANUAL GAP labels) |

**R12 STRUCTURAL AXIS DECLARATION (authored by CA, Phase 0):**

Three R12 dimensions are active in this output. They are orthogonal — their enforcement
mechanisms are structurally independent and non-overlapping.

| R12 Dimension | Label | Structural Property | CA Verification |
|---------------|-------|---------------------|-----------------|
| Dimension 1 | Execution order | TABLE_4 at SE-0 before TABLE_1; Tier in TABLE_1/TABLE_3; SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference | CA-1.4 (SE-0 ordering), CA-1.9 (SE-0 slot cross-ref) |
| Dimension 2 | Closure-note format | Exact-label MANUAL GAP / STRUCTURED CLOSE two-part blocks at SE-2/SE-3/SE-4 | CA-1.7 |
| Dimension 3 | CS self-reference | CS-0 cites CS-2 and CS-3 schema IDs and SE-updatable columns before CS-1 | CA-1.8 |

**Non-interference statement:** Each dimension governs a structurally distinct element of the
output. Dimension 1 governs SE section order, TABLE_1/TABLE_3 column structure, and SE-4
STRUCTURED CLOSE TABLE_4 SE-0 slot. Dimension 2 governs the exact textual format of SE-2/SE-3/
SE-4 opening blocks. Dimension 3 governs CS's Phase 1 opening sub-section. No dimension's
enforcement overlaps with another's. A model that satisfies one dimension and defers another
on coverage grounds fails the non-interference contract. CA-1.4+CA-1.9 verify Dimension 1;
CA-1.7 verifies Dimension 2; CA-1.8 verifies Dimension 3.

**SHALL-A through SHALL-G:** *(identical to V-01, including SHALL-G's SE-4 STRUCTURED CLOSE
TABLE_4 SE-0 slot requirement and CA-1.9 distinction note)*

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

*(CS-0 Registry acknowledgment + CS-1/CS-2/CS-3 — identical to R12-V-05.)*

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis (Privilege-Tier Descent Order)

*SE-0 before SE-1. Exact-label two-part closure blocks at SE-2/SE-3/SE-4. SE-4 STRUCTURED CLOSE
carries TABLE_4 row cross-reference at SE-0 slot.*

### SE-0 — Admin-Tier Inventory and Escalation Vectors

TABLE_4 at SE-0 before TABLE_1. Four vectors, Checked?=YES. Update CS-2 after.

### SE-1 / SE-2 / SE-3 — *(standard R12-V-05 content)*

SE-2: `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:` / `STRUCTURED CLOSE:`
SE-3: `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:` / `STRUCTURED CLOSE:`

### SE-4 / SHALL-D — Section 4: Privilege Escalation Cross-Reference

MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing sharing rules that
silently override them; a Private OWD combined with an active sharing rule can grant effective
org-wide access without appearing in any security roles UI view.

STRUCTURED CLOSE:
SE-0 cross-reference: TABLE_4 row [name the specific TABLE_4 vector row most relevant to
{{topic}}'s primary escalation surface — cite exact vector label, Checked? value, and the
Finding from SE-0 TABLE_4]. This TABLE_4 row cross-reference is the SE-0 slot of this STRUCTURED
CLOSE block; it is the subject of CA-1.9 verification and is distinct from the MANUAL GAP block
above (which CA-1.7 verifies) and from TABLE_4's SE-0 execution order (which CA-1.4 verifies).
TABLE_4 (filled at SE-0) evaluated all four escalation vectors simultaneously. This section adds
the cross-tier differential: for the most privileged Admin-tier role and the most restricted
Restricted-tier role, identify the enforcement layer where access diverges, citing the SE-0 TABLE_4
row named in the SE-0 slot above.

### SE-5 — *(standard TABLE_5 content)*

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

**CA-1.1 through CA-1.8** — *(identical to R12-V-05 double-anchor structure for C-01 through C-05,
SHALL-F, SHALL-G, and CS-0 acknowledgment)*

**CA-1.9 — SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 slot** *(C-35; pre-assigned
Phase 0; distinct from CA-1.4 and CA-1.7)*:
- Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity]. Phase 0 declared: "SE-4's STRUCTURED CLOSE block SHALL carry a TABLE_4 row cross-reference at its SE-0 slot, naming a specific TABLE_4 vector row by exact vector label."
- Preamble anchor — CA-1.9 pre-assigned in Phase 0: "SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 slot | SE-4 STRUCTURED CLOSE | Distinct from CA-1.4 (SE-0 ordering), CA-1.7 (MANUAL GAP labels)."
- Verification — SE-4's STRUCTURED CLOSE begins with an SE-0 slot entry naming a specific TABLE_4 vector row by its exact label? The named row was populated at SE-0 with Checked?=YES and a Finding? The cross-reference is inside the STRUCTURED CLOSE block (not in the MANUAL GAP block, not in TABLE_5)? -> PASS / FAIL
- Distinction: CA-1.4 verified TABLE_4 appeared at SE-0 before TABLE_1. CA-1.7 verified the MANUAL GAP exact-label blocks. CA-1.9 verifies the TABLE_4 row cross-reference inside SE-4's STRUCTURED CLOSE.

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0),
R12 Structural Axis Declaration (Step 0.2, Phase 0), Phase 0 by label.
[CA-1.1 through CA-1.9. R12 Dimension 1 (CA-1.4+CA-1.9), Dimension 2 (CA-1.7), Dimension 3
(CA-1.8). Non-interference contract active. Overall: COMPLIANT / NON-COMPLIANT. Open items.]

---

## V-05 — Full Combination C-34+C-35+C-36: The 28/28 Candidate

**Axis:** All three new v12 criteria on R12-V-05 base — preamble R12 Structural Axis Declaration
with non-interference statement (C-34); SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0
slot + CA-1.9 (C-35); tri-dimensional self-evidence attestation in CA terminal verdict naming each
R12 dimension with specific output-body evidence source (C-36).
**Hypothesis:** 28/28.

---

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

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins.

**PHASE 0 — CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1: seven schemas — TABLE_1 through TABLE_5
with Tier columns on TABLE_1 and TABLE_3; CS-2 and CS-3 with SE-updatable columns and update
protocols; TABLE_4 schema note declares SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot requirement) and
the Criterion Enforcement Matrix preamble (Step 0.2: SHALL-A through SHALL-G; M4 CA-1.1 through
CA-1.9 pre-assigned; R12 Structural Axis Declaration with non-interference statement). CA issues
handoff to PHASE 1.

**PHASE 1 — CS (Customer Success):**
Executes second. Opens with CS-0 sub-section (Schema Registry acknowledgment: cites CS-2 and CS-3
schema IDs by exact label; lists SE-updatable columns; confirms expectation format). Then produces
CS-1, CS-2, CS-3. CS does not fill TABLE_1-5. Issues handoff to PHASE 2.

**PHASE 2 — SE (Security Engineer / Dataverse Security Expert):**
Executes third in privilege-tier descent order. SE-0 (admin-tier inventory + TABLE_4) before SE-1.
TABLE_1 and TABLE_3 include Tier column. SE-2/SE-3/SE-4 use exact-label two-part closure blocks
per SHALL-G. SE-4 STRUCTURED CLOSE carries TABLE_4 row cross-reference at SE-0 slot naming a
specific TABLE_4 vector row. Issues handoff to PHASE 3.

**PHASE 3 — CA-1 (CA Verification Pass):**
CA returns. Double-anchor reaffirmation per row. CA-1.8 verifies CS-0 precedes CS-1. CA-1.9
verifies SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference (distinct from CA-1.4 and
CA-1.7). Terminal verdict includes TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION naming each R12
dimension with its specific output-body evidence source.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1 and 0.2 before any other phase begins.*

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

**All table schemas declared centrally by CA. Blank-cell prohibition is global. SE-update
protocols for CS-2 and CS-3 declared co-located with schema entry.**

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Tier values: Admin / Custom / Restricted. Rows ordered: Admin tier first, Custom second,
Restricted last. Blank-cell rule: all cells Granted / Denied / Conditional (condition inline) / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Blank-cell rule: FLS Profile Configured? = Configured / Not Configured. Gap? = YES / NO.

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Tier values mirror TABLE_1. Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU /
Org-wide / Team-scoped / Sharing-[rule name]. Verified? = YES / NO.

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
Blank-cell rule: all four vectors (team inheritance, sharing rules, impersonation, admin/env roles),
Checked? = YES, Finding = escalation path or specific rule-out.
Note: TABLE_4 executes at SE-0 before SE-1. Additionally, SE-4's STRUCTURED CLOSE block SHALL
carry a TABLE_4 row cross-reference at its SE-0 slot: the SE-0 slot names a specific TABLE_4
vector row by its exact vector label, anchoring the closure note to a concrete TABLE_4 finding.
This SE-0 slot cross-reference is the subject of CA-1.9 verification, distinct from CA-1.4
(SE-0 execution ordering) and CA-1.7 (MANUAL GAP exact-label blocks).

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation`
Blank-cell rule: Remediation = exact object + exact location + expected post-fix state.
CS-EXPECTATION-VIOLATED Remediation (three-field block):
- CS-Expected: cite CS-2 or CS-3 row, state expectation verbatim or by row reference.
- SE-Actual: SE finding that contradicts the expectation.
- Delta: exact configuration change to align SE-Actual to CS-Expected.

**Schema ID: CS-2 — Sharing Rule Expectations (CS-authored expectation table)**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference (TABLE_4 row ID or TABLE_5 row ID);
SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE update protocol: SE populates after TABLE_4 analysis at SE-0. CONTRADICTED triggers
CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

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

**Supplementary CA verification rows (Phase 0 pre-assignment):**

| Row ID | What it verifies | Scope | Distinct from |
|--------|-----------------|-------|---------------|
| CA-1.6 | SHALL-F CS-EXPECTATION-VIOLATED three-field structure | TABLE_5 CS-EV rows | — |
| CA-1.7 | SHALL-G exact-label MANUAL GAP two-part blocks at SE-2/SE-3/SE-4 | SE-2, SE-3, SE-4 openings | CA-1.9 |
| CA-1.8 | CS-2/CS-3 Schema Registry registration + CS-0 acknowledgment precedes CS-1 | Phase 1 CS-0 | — |
| CA-1.9 | SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 slot | SE-4 STRUCTURED CLOSE | CA-1.4 (SE-0 ordering), CA-1.7 (MANUAL GAP labels) |

**R12 STRUCTURAL AXIS DECLARATION (authored by CA, Phase 0):**

This output activates three R12 structural dimensions. These dimensions are orthogonal: each
governs a structurally distinct property of the output, and activating one neither enables nor
exempts another. The non-interference contract below is binding; a model that treats any two
dimensions as jointly satisfying a single dimension's requirement fails this declaration.

| R12 Dimension | Label | Structural Property Governed | CA Verification |
|---------------|-------|------------------------------|-----------------|
| Dimension 1 | Execution order | SE-0 before SE-1; Tier in TABLE_1/TABLE_3; SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference naming a specific TABLE_4 vector row | CA-1.4 (SE-0 ordering) + CA-1.9 (SE-0 slot cross-ref) |
| Dimension 2 | Closure-note format | Exact-label two-part `MANUAL GAP [<exact label>]:` / `STRUCTURED CLOSE:` blocks at openings of SE-2, SE-3, and SE-4 | CA-1.7 |
| Dimension 3 | CS self-reference | CS-0 sub-section cites CS-2 and CS-3 schema IDs by exact label and lists SE-updatable columns before CS-1/CS-2/CS-3 | CA-1.8 |

**Non-interference statement:** Dimension 1 governs SE section sequencing, TABLE column structure,
and SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot. Dimension 2 governs the exact textual format of
SE section opening blocks (MANUAL GAP / STRUCTURED CLOSE). Dimension 3 governs CS's Phase 1
opening sub-section structure. No dimension's enforcement mechanism intersects with another's.
Verifying CA-1.7 (Dimension 2) does not verify Dimension 1 or Dimension 3. Verifying CA-1.8
(Dimension 3) does not verify Dimensions 1 or 2. Verifying CA-1.4+CA-1.9 (Dimension 1) does
not verify Dimensions 2 or 3. Each dimension requires independent satisfaction.

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A: Complete TABLE_1 with Tier column. Every cell Granted/Denied/Conditional/N/A. Rows ordered by tier.
- SHALL-B: TABLE_2 lists all PII, Financial, and Audit-Compliance fields with explicit FLS status. Null case explicit. Gap? YES rows in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier and Effective Scope filled. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 at SE-0 (before SE-1), all four vectors, Checked? = YES. Rule-outs name specific mechanism and reason.
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap case requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field Remediation block (CS-Expected, SE-Actual, Delta). Incomplete rows MUST be reopened. CA-1.6 verifies.
- SHALL-G: At the opening of SE-2, SE-3, and SE-4, closure MUST appear as a two-part labeled block — Line 1: `MANUAL GAP [<exact CONTEXT label>]:` where the label is character-for-character as written in the CONTEXT section above; Line 2: description of what manual audits miss; Line 3: `STRUCTURED CLOSE:`; Line 4: closing mechanism. Additionally, SE-4's STRUCTURED CLOSE block SHALL carry a TABLE_4 row cross-reference at the SE-0 slot naming a specific TABLE_4 vector row by exact label — this is CA-1.9's audit target, distinct from CA-1.7's MANUAL GAP label audit.

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

*CS opens with CS-0 Registry acknowledgment before authoring any expectation content.*

### CS-0 — Schema Registry Acknowledgment (CS-authored, Phase 1)

CS echoes the Schema Registry entries for CS-2 and CS-3 from Phase 0 before authoring expectation
rows. This sub-section confirms the handoff from CA's Registry to CS's authoring task.

**Registry acknowledgment for CS-2:**
Schema ID: CS-2 — Sharing Rule Expectations.
SE-updatable columns as declared by CA in Phase 0 Schema Registry: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged: SE populates SE Cross-Reference (TABLE_4 or TABLE_5 row ID)
and SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE) after SE-0/TABLE_4 analysis.
Expectation format confirmed. SE-updatable columns left blank by CS; SE fills after SE-0.

**Registry acknowledgment for CS-3:**
Schema ID: CS-3 — Cross-Role Access Differential Expectations.
SE-updatable columns as declared by CA in Phase 0 Schema Registry: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged: SE populates SE Cross-Reference (TABLE_1 or TABLE_3 row ID)
and SE Confirmation after SE-1/SE-3 analysis. SE-updatable columns left blank by CS.

### CS-1 — Expected Customer Service Access Baseline

For each entity in scope: (a) CRUD operations the CS role is expected to perform for normal job
function; (b) expected record scope; (c) sensitive fields CS needs and why. Identify configurations
that may inadvertently open access beyond job requirements.

**CS-2 — Sharing rule expectations** *(Schema Registry CS-2; SE-updatable columns blank)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

For each Potential Overreach? YES: name the access path and the most likely over-reached role.

**CS-3 — Cross-role access differential** *(Schema Registry CS-3; SE-updatable columns blank)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

At minimum one entity and one operation where CS has less access than the Comparison Role.

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis (Privilege-Tier Descent Order)

*SE-0 establishes admin-tier ceiling and TABLE_4 before SE-1. R12 Dimension 1 (execution order)
active: TABLE_4 at SE-0, Tier columns in TABLE_1/TABLE_3, SE-4 STRUCTURED CLOSE TABLE_4 SE-0
slot cross-reference. R12 Dimension 2 (closure-note format) active: exact-label two-part MANUAL
GAP / STRUCTURED CLOSE blocks at SE-2/SE-3/SE-4 per SHALL-G. R12 Dimension 3 (CS self-reference)
confirmed: CS-0 Registry acknowledgment completed in Phase 1.*

### SE-0 — Admin-Tier Inventory and Escalation Vectors (executes before TABLE_1)

**Admin-tier role inventory:** List System Administrator, Environment Admin, and admin-equivalent
roles with record scope and key capabilities. Note admin bypasses of lower-tier controls
(e.g., System Administrator bypasses column security profiles). Establishes privilege ceiling.

**TABLE_4 — Escalation Vector Inventory** *(Schema Registry TABLE_4; SE-0 placement per SHALL-D
and R12 Dimension 1; TABLE_1 rows interpreted relative to this ceiling)*

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

### SE-1 / SHALL-A — Section 1: Role-Operation Matrix

**TABLE_1 — Role-Operation Matrix** *(Schema Registry TABLE_1 with Tier; blank-cell rule)*

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Admin-tier rows first. Include every role with any privilege on any entity in {{topic}}.
After table: cross-reference CS-3 expectations. Cross-role differential: compare CS role against
one more privileged role; state whether differential is expected (least privilege satisfied).

### SE-2 / SHALL-B — Section 2: Field-Level Security Coverage

MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:
Column security profiles are not auditable from the security roles UI; administrators discover
missing FLS only after a data exposure event reveals a sensitive field was readable by an
unintended role.

STRUCTURED CLOSE:
TABLE_2 below enumerates every sensitive field with its explicit FLS status, surfacing pre-event
what the security roles UI conceals. All Not Configured sensitive fields are forwarded to TABLE_5
as MISSING-FLS gaps.

**TABLE_2 — FLS Coverage** *(Schema Registry TABLE_2; blank-cell rule)*

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Categories: PII / Financial / Audit-Compliance / Other-Sensitive. Null case: explicitly state
"No column security profiles active on {{topic}}." Defense-in-depth layer check: identify
enforcement layer for at least one sensitive field; note Admin-tier bypass from SE-0 if applicable.

### SE-3 / SHALL-C — Section 3: Record Access Scope

MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access produced by a security role
plus owner team membership plus OWD; spot-checking individual roles misses team-accumulated
privilege accumulation.

STRUCTURED CLOSE:
TABLE_3 below maps effective scope for every role by Tier, recording OWD baseline, scope modifier,
and resulting effective scope, making team-accumulated privilege visible and auditable.

**TABLE_3 — Record Scope by Role** *(Schema Registry TABLE_3 with Tier; blank-cell rule)*

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role MUST appear, ordered by Tier. Roles where effective scope exceeds role-only
scope due to team membership are CS-EXPECTATION-VIOLATED candidates. After TABLE_3: update CS-3.

### SE-4 / SHALL-D — Section 4: Privilege Escalation Cross-Reference

MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing sharing rules that
silently override them; a Private OWD combined with an active sharing rule can grant effective
org-wide access without appearing in any security roles UI view.

STRUCTURED CLOSE:
SE-0 cross-reference: TABLE_4 row [name the specific TABLE_4 vector row most relevant to
{{topic}}'s primary escalation surface — cite exact vector label (e.g., "Team inheritance" or
"Sharing rules"), Checked? value, and the full Finding from SE-0 TABLE_4]. This TABLE_4 row
cross-reference occupies the SE-0 slot of this STRUCTURED CLOSE block and anchors the closure
note to a concrete SE-0 finding. It is the subject of CA-1.9 verification; it is distinct from
the MANUAL GAP block above (CA-1.7's scope) and from TABLE_4's execution order at SE-0 (CA-1.4's
scope).
TABLE_4 (filled at SE-0) evaluated all four escalation vectors simultaneously. This section adds
the cross-tier differential: for the most privileged Admin-tier role and the most restricted
Restricted-tier role, identify the specific Dataverse enforcement layer where access diverges,
citing the TABLE_4 row named in the SE-0 slot above. State whether the divergence is expected.

### SE-5 / SHALL-E — Section 5: Security Gap Inventory

**TABLE_5 — Security Gap Inventory** *(Schema Registry TABLE_5 with Tier; blank-cell rule)*

| # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation |
|---|----------|--------|---------------|------|------|----------|-------------|

Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED /
CS-EXPECTATION-VIOLATED. Severity: CRITICAL / HIGH / MEDIUM.

CS-EXPECTATION-VIOLATED rows (three-field Remediation block per SHALL-F):
- CS-Expected: [cite CS-2 or CS-3 row, state expectation verbatim or by row reference]
- SE-Actual: [SE finding that contradicts the expectation]
- Delta: [exact configuration change to align SE-Actual to CS-Expected]

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

*CA returns. Each CA-1 row presents Registry anchor and Preamble anchor as structurally distinct
labeled elements before the Verification line. Inline concatenation fails C-24.*

**CA-1.1 — C-01 verification** *(Phase 0 M4 pre-assignment CA-1.1)*:
- Registry anchor — Schema ID TABLE_1 (with Tier): [Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope] — blank cells prohibited globally.
- Preamble anchor — C-01 as authored by CA in Phase 0: TABLE_1 / SE-1 / SHALL-A / CA-1.1 — verifying...
- Verification — TABLE_1 present? Tier column populated? Rows ordered by tier? All cells filled? -> PASS / FAIL

**CA-1.2 — C-02 verification** *(Phase 0 M4 pre-assignment CA-1.2)*:
- Registry anchor — Schema ID TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?] — blank cells prohibited globally.
- Preamble anchor — C-02 as authored by CA in Phase 0: TABLE_2 / SE-2 / SHALL-B / CA-1.2 — verifying...
- Verification — TABLE_2 present? All sensitive fields? FLS status explicit? Null case stated? Gap? YES in TABLE_5? -> PASS / FAIL

**CA-1.3 — C-03 verification** *(Phase 0 M4 pre-assignment CA-1.3)*:
- Registry anchor — Schema ID TABLE_3 (with Tier): [Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Verified?] — blank cells prohibited globally.
- Preamble anchor — C-03 as authored by CA in Phase 0: TABLE_3 / SE-0+SE-3 / SHALL-C / CA-1.3 — verifying...
- Verification — Every TABLE_1 role in TABLE_3? Tier column populated? Effective Scope filled? -> PASS / FAIL

**CA-1.4 — C-04 verification** *(Phase 0 M4 pre-assignment CA-1.4)*:
- Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity] — all four vectors, Checked? = YES.
- Preamble anchor — C-04 as authored by CA in Phase 0: TABLE_4 / SE-0 / SHALL-D / CA-1.4 — verifying...
- Verification — TABLE_4 at SE-0 (before SE-1)? All four vectors? Findings or specific rule-outs? -> PASS / FAIL
- Note: CA-1.4 verifies SE-0 execution ordering only. SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot content is CA-1.9's scope.

**CA-1.5 — C-05 verification** *(Phase 0 M4 pre-assignment CA-1.5)*:
- Registry anchor — Schema ID TABLE_5 (with Tier): [#, Gap Type, Entity, Field or Rule, Role, Tier, Severity, Remediation] — blank cells prohibited globally.
- Preamble anchor — C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 — verifying...
- Verification — TABLE_5 present? Named gap? Tier column populated? Remediations exact? -> PASS / FAIL

**CA-1.6 — SHALL-F compliance verification** *(CS-EXPECTATION-VIOLATED three-field structure)*:
- Registry anchor — Schema ID TABLE_5 CS-EXPECTATION-VIOLATED row structure: [CS-Expected, SE-Actual, Delta] — all three required per SHALL-F.
- Preamble anchor — SHALL-F as authored by CA in Phase 0: three-field Remediation block mandatory; rows missing any field MUST be reopened.
- Verification — For each CS-EXPECTATION-VIOLATED row: CS-Expected populated? SE-Actual populated? Delta populated with exact configuration change? -> PASS / FAIL per row.

**CA-1.7 — SHALL-G compliance verification** *(exact-label MANUAL GAP two-part closure blocks)*:
- Registry anchor — CONTEXT section declared exact labels: "Blind spot 1 — Post-incident FLS gap" (SE-2), "Blind spot 2 — Cumulative privilege blind spot" (SE-3), "Blind spot 3 — OWD-sharing-rule override gap" (SE-4). SHALL-G requires two-part blocks with exact label in brackets.
- Preamble anchor — SHALL-G as authored by CA: Line 1 `MANUAL GAP [<exact label>]:`; exact = character-for-character; paraphrase fails. CA-1.7 verifies. Distinct from CA-1.9.
- Verification — SE-2 opens with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:`? Followed by `STRUCTURED CLOSE:`? SE-3/SE-4 same pattern with exact labels? -> PASS / FAIL per section.
- Note: CA-1.7 verifies the MANUAL GAP block format. The TABLE_4 row cross-reference inside SE-4's STRUCTURED CLOSE is CA-1.9's scope.

**CA-1.8 — CS-2/CS-3 Schema Registry registration + CS-0 acknowledgment verification** *(C-29 + C-33 / R12 Dimension 3)*:
- Registry anchor — Schema Registry declared CS-2 as named schema entry with SE-updatable columns SE Cross-Reference and SE Confirmation and SE-update protocol co-located. CS-3 same. PHASE 1 mandate requires CS-0 to acknowledge both schema IDs and list SE-updatable columns before CS-1/CS-2/CS-3.
- Preamble anchor — CS-2 and CS-3 are Schema Registry entries. CS-0 acknowledgment is a PHASE 1 structural requirement per R12 Dimension 3.
- Verification — CS-2 in Registry? CS-3 in Registry? CS-0 present before CS-1? CS-0 cites both schema IDs by exact label? CS-0 lists SE-updatable columns for both? SE populated SE-updatable columns? -> PASS / FAIL

**CA-1.9 — SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 slot** *(C-35; pre-assigned
Phase 0; distinct from CA-1.4 and CA-1.7)*:
- Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity]. Phase 0 Schema Registry declared: "SE-4's STRUCTURED CLOSE block SHALL carry a TABLE_4 row cross-reference at its SE-0 slot, naming a specific TABLE_4 vector row by its exact vector label."
- Preamble anchor — CA-1.9 pre-assigned in Phase 0 supplementary rows: "SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 slot | SE-4 STRUCTURED CLOSE | Distinct from CA-1.4 (SE-0 ordering), CA-1.7 (MANUAL GAP labels)."
- Verification — SE-4's STRUCTURED CLOSE block begins with an SE-0 slot entry naming a specific TABLE_4 vector row by its exact vector label? That row was populated at SE-0 with Checked?=YES and a non-blank Finding? The cross-reference is inside the STRUCTURED CLOSE block (not in the MANUAL GAP block, not in TABLE_5)? -> PASS / FAIL
- Distinction confirmed: CA-1.4 verified TABLE_4 appeared at SE-0 before TABLE_1. CA-1.7 verified the MANUAL GAP exact-label blocks at SE-2/SE-3/SE-4 openings. CA-1.9 verifies the TABLE_4 row cross-reference inside SE-4's STRUCTURED CLOSE block — a third non-overlapping audit target on SE-4.

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0),
R12 Structural Axis Declaration (Step 0.2, Phase 0), Phase 0 by label.
[CA-1.1 through CA-1.9 results. R12 Dimension 1 (CA-1.4+CA-1.9), Dimension 2 (CA-1.7),
Dimension 3 (CA-1.8). Non-interference contract: all three dimensions independently verified.
Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

**TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION (R12 dimensions, authored by CA in terminal verdict):**

This attestation extends C-22's phase-execution self-evidence to all three R12 structural
dimensions. For each dimension, the specific output-body evidence source is named below. The
attestation is self-verifiable: each evidence source is a section or table in this output,
locatable by inspection without reading the prompt instructions.

| R12 Dimension | Label | Specific Output-Body Evidence Source |
|---------------|-------|--------------------------------------|
| Dimension 1 | Execution order | Phase 2 output body: SE-0 section header precedes SE-1 section header; TABLE_4 table appears in SE-0 before any TABLE_1 row; TABLE_1 and TABLE_3 each contain a Tier column; SE-4 STRUCTURED CLOSE block contains an SE-0 slot entry naming a specific TABLE_4 vector row by exact label (the specific row is identified by CA-1.9 verification above). |
| Dimension 2 | Closure-note format | Phase 2 output body: SE-2 opens with the string `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:` followed by a description line and then `STRUCTURED CLOSE:`; SE-3 opens with `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:` followed by `STRUCTURED CLOSE:`; SE-4 opens with `MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:` followed by `STRUCTURED CLOSE:`. These three exact-label two-part blocks are present at the opening of each respective SE section and verified by CA-1.7. |
| Dimension 3 | CS self-reference | Phase 1 output body: CS-0 sub-section appears before CS-1; CS-0 contains the string "Schema ID: CS-2 — Sharing Rule Expectations" and lists SE Cross-Reference and SE Confirmation as SE-updatable columns; CS-0 contains the string "Schema ID: CS-3 — Cross-Role Access Differential Expectations" and lists the same. This sub-section is present in Phase 1 and verified by CA-1.8. |

All three dimensions are simultaneously active. Their evidence sources are structurally
independent: Dimension 1 evidence is in SE-0 and in TABLE_1/TABLE_3 column structure and in
SE-4's STRUCTURED CLOSE SE-0 slot; Dimension 2 evidence is in SE-2/SE-3/SE-4 opening blocks;
Dimension 3 evidence is in CS-0. No dimension's output-body evidence source is the same section
or structural element as another dimension's evidence source. This independence is the output-body
manifestation of the non-interference declaration in the Phase 0 R12 Structural Axis Declaration.
