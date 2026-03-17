# trace-permissions — Quest Variate Round 6 (Rubric v12)

**Date:** 2026-03-17
**Rubric:** v12 (C-01..C-36, N=28)
**Base:** V-05/R12 architecture (t3 SKILL.md) scores 25/28 under v12.
Missing: C-34 (preamble axis declaration), C-35 (SE-4 TABLE_4 SE-0 cross-ref + CA-1.9), C-36 (tri-dimensional terminal attestation).

**Round 6 target:** 28/28 (100.0) via single-axis isolation then full integration.

## Round 6 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | C-34 only — Preamble orthogonal dimensions declaration | C-34 requires the preamble to convert empirical co-presence of D-1/D-2/D-3 into a binding non-interference contract. Adding a named table in Step 0.2 with axis IDs, mechanism descriptions, and explicit non-interference statements should pass C-34 without touching SE-4 or the CA verdict. C-35/C-36 remain open. |
| V-02 | C-35 only — SE-4 STRUCTURED CLOSE TABLE_4 SE-0 row cross-reference + CA-1.9 | C-35 requires SE-4's STRUCTURED CLOSE to cite a specific TABLE_4 SE-0 row (not generic prose) and a new CA-1.9 row that is a distinct audit target from CA-1.4 and CA-1.7. Adding the row citation to STRUCTURED CLOSE and a CA-1.9 template should pass C-35 without touching the preamble or the verdict. C-34/C-36 remain open. |
| V-03 | C-36 only — CA terminal verdict tri-dimensional self-evidence attestation | C-36 requires the CA verdict to explicitly name each R12 dimension (D-1/D-2/D-3) and cite its specific output-body evidence source — attesting the dimension's presence from the text alone. Adding a tri-dimensional attestation table at the verdict should pass C-36 without modifying the preamble or SE-4. C-34/C-35 remain open. |
| V-04 | C-34 + C-35 combined | Structurally independent axes: C-34 is a Phase 0 preamble property; C-35 is a Phase 2/Phase 3 property. Combining them tests that the axis declaration in Phase 0 does not interfere with the SE-4/CA-1.9 additions in Phase 2/3. C-36 remains open. |
| V-05 | Full integration — C-34 + C-35 + C-36 | All three axes simultaneously active. The axis declaration (C-34) in Phase 0 gives D-2 and D-3 their IDs; SE-4 STRUCTURED CLOSE cites TABLE_4 SE-0 by row name (C-35); CA-1.9 verifies it (C-35); the verdict tri-dimensional attestation cites D-1/D-2/D-3 evidence by output-body location (C-36). Target: 28/28. |

---

## V-01 — Single Axis: C-34 (Preamble Orthogonal Dimensions Declaration)

**Axis:** C-34 — preamble axis declaration only
**Hypothesis:** C-34 requires the preamble (Step 0.2) to name the three R12 structural dimensions as orthogonal axes with an explicit non-interference statement. V-05 has all three dimensions active empirically but never declares them as orthogonal. Adding a named R12 Orthogonal Dimensions Declaration table in Step 0.2 (after the SHALL obligations, before the handoff) should pass C-34 without modifying any other section. C-35 and C-36 remain unaddressed.

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

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins.

**PHASE 0 — CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1: TABLE_1 through TABLE_5 with Tier
columns on TABLE_1 and TABLE_3; CS-2 and CS-3 with SE-updatable columns and SE-update protocols
— seven schemas total) and the Criterion Enforcement Matrix preamble (Step 0.2: SHALL-A through
SHALL-G, M4 row IDs CA-1.1 through CA-1.8 pre-assigned). CA issues handoff to PHASE 1.

**PHASE 1 — CS (Customer Success):**
Executes second. Opens with CS-0 sub-section (Schema Registry acknowledgment: CS echoes Registry
schema IDs for CS-2 and CS-3 by exact Schema ID label, lists SE-updatable columns for each, and
confirms the expectation format before authoring any expectation rows). Then produces CS-1, CS-2,
CS-3 using Registry schemas. CS does not fill TABLE_1-5. CS issues handoff to PHASE 2.

**PHASE 2 — SE (Security Engineer / Dataverse Security Expert):**
Executes third in privilege-tier descent order. SE-0 (admin-tier inventory and TABLE_4 escalation
vectors) runs before SE-1 (role-operation matrix), establishing the privilege ceiling before
populating operation cells. TABLE_1 and TABLE_3 include Tier column. SE-2, SE-3, SE-4 each open
with two-part exact-label closure blocks per SHALL-G. SE-4 cites SE-0 data in cross-tier
differential. Issues handoff to PHASE 3.

**PHASE 3 — CA-1 (CA Verification Pass):**
CA returns. Each CA-1 row performs double-anchor reaffirmation: Registry anchor and Preamble
anchor as structurally distinct labeled elements. Verification line follows. Inline concatenation
fails C-24. CA-1.8 extended to verify CS-0 acknowledgment precedes CS-1.

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
Blank-cell rule: FLS Profile Configured? = Configured / Not Configured (never blank). Gap? = YES / NO.

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Tier values mirror TABLE_1. Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU /
Org-wide / Team-scoped / Sharing-[rule name]. Verified? = YES / NO.

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
Blank-cell rule: all four vectors, Checked? = YES, Finding = escalation path or specific rule-out.
Note: TABLE_4 executes at SE-0 before SE-1 because admin-tier role structure determines escalation
paths before the lower-tier role-operation matrix is populated.

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

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A: Complete TABLE_1 with Tier column. Every cell Granted/Denied/Conditional/N/A. Rows ordered by tier.
- SHALL-B: TABLE_2 lists all PII, Financial, and Audit-Compliance fields with explicit FLS status. Null case explicit. Gap? YES rows in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier and Effective Scope filled. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 at SE-0 (before SE-1), all four vectors, Checked? = YES. Rule-outs name specific mechanism and reason.
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap case requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field Remediation block (CS-Expected, SE-Actual, Delta). Incomplete rows MUST be reopened. CA-1.6 verifies.
- SHALL-G: At the opening of SE-2, SE-3, and SE-4, closure MUST appear as a two-part labeled block — Line 1: `MANUAL GAP [<exact CONTEXT label>]:` where <exact CONTEXT label> is the label character-for-character as written in the CONTEXT section (e.g., "Blind spot 1 — Post-incident FLS gap" — not a paraphrase); Line 2: description of what manual audits miss; Line 3: `STRUCTURED CLOSE:`; Line 4: which table and mechanism closes it. Single-line annotation, blockquote format, TABLE_5 consolidation, or paraphrased label all fail SHALL-G. CA-1.7 verifies exact label carry-through.

**R12 Orthogonal Dimensions Declaration (C-34):**

The three R12 structural dimensions are declared as orthogonal enforcement axes. Each dimension is
independently verifiable. The failure of one dimension does not propagate to or imply the failure
of the others. This declaration converts empirical co-presence into a binding non-interference
contract: all three dimensions SHALL be simultaneously active.

| Dimension | ID | Mechanism | Non-Interference Statement |
|-----------|----|-----------|-----------------------------|
| Execution order | D-1 | CA authors Schema Registry (Step 0.1) and Criterion Enforcement Matrix preamble (Step 0.2) before any SE or CS section begins. CA-1 rows reference pre-assigned M4 IDs as contract completion, not post-hoc decoration. | D-1 verifiability depends on CA authorship sequencing only. D-2 and D-3 may independently pass or fail without affecting D-1 verification. |
| Closure-note format | D-2 | SE-4 STRUCTURED CLOSE block SHALL cite a specific TABLE_4 SE-0 row cross-reference by row name or position label. CA-1.9 verifies this as a distinct audit target from CA-1.4 (TABLE_4 placement before SE-1) and CA-1.7 (exact MANUAL GAP label carry-through). | D-2 verifiability depends on SE-4 STRUCTURED CLOSE content only. D-1 and D-3 may independently pass or fail without affecting D-2 verification. |
| CS self-reference | D-3 | CS-0 cites the Schema Registry entries for CS-2 and CS-3 by exact Schema ID label before authoring any expectation rows. CA-1.8 verifies CS-0 acknowledgment precedes CS-1. | D-3 verifiability depends on CS-phase acknowledgment of Registry provenance only. D-1 and D-2 may independently pass or fail without affecting D-3 verification. |

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
two-part closure blocks per SHALL-G.*

### SE-0 — Admin-Tier Inventory and Escalation Vectors (executes before TABLE_1)

**Admin-tier role inventory:** List System Administrator, Environment Admin, and any
admin-equivalent roles with record scope and key capabilities. Note any admin capability that
bypasses lower-tier controls (e.g., System Administrator bypasses column security profiles).
This establishes the privilege ceiling for all lower-tier roles in SE-1.

**TABLE_4 — Escalation Vector Inventory** *(Schema Registry TABLE_4; placed at SE-0 because
admin-tier role structure determines escalation paths; TABLE_1 rows are interpreted relative to
this ceiling)*

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Finding format: `[Role] -> [Mechanism] -> [Elevated access achieved]` for confirmed escalation;
"Checked [mechanism]: no path found because [specific reason]" for rule-out. After TABLE_4:
populate CS-2 SE Cross-Reference and SE Confirmation. CONTRADICTED rows trigger
CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

### SE-1 / SHALL-A — Section 1: Role-Operation Matrix

**TABLE_1 — Role-Operation Matrix** *(Schema Registry TABLE_1 with Tier column; blank-cell rule)*

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Rows ordered: Admin tier first, Custom tier second, Restricted tier last. After TABLE_1: populate
CS-3 SE Cross-Reference and SE Confirmation. Note confirmations (cite CS-3 row) and CONTRADICTED
rows (trigger CS-EXPECTATION-VIOLATED per SHALL-F).

**Cross-role differential analysis:** Compare the CS role against at least one Admin-tier role
and one Custom-tier role for the same entity and operation. Cite SE-0 TABLE_4 data for any
differential attributable to admin-tier escalation vectors (e.g., cite TABLE_4 row ID where
admin/env role override was confirmed or ruled out).

### SE-2 / SHALL-B — Section 2: Field-Level Security Coverage

MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:
Column security profiles are not auditable from the security roles UI; administrators discover
missing FLS only after a data exposure event reveals that a sensitive field was readable or
writable by an unintended role.

STRUCTURED CLOSE:
TABLE_2 below enumerates every sensitive field in scope with its explicit FLS status (Configured /
Not Configured), surfacing pre-event what the security roles UI conceals. All Not Configured
sensitive fields are forwarded to TABLE_5 as MISSING-FLS gaps with Tier column identifying the
highest-privilege tier with access.

**TABLE_2 — FLS Coverage** *(Schema Registry TABLE_2; blank-cell rule globally)*

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

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
TABLE_3 below maps the effective scope for every role by Tier, recording the OWD baseline, the
scope modifier from team or role depth, and the resulting effective scope as a single traceable
row, making team-accumulated privilege visible and auditable at the tier it occurs.

**TABLE_3 — Record Scope by Role** *(Schema Registry TABLE_3 with Tier column; blank-cell rule)*

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
TABLE_4 (authored at SE-0, rows: Team inheritance / Sharing rules / Impersonation / Admin-role
override) evaluated all four escalation vectors. This section adds cross-tier differential
summary citing SE-0 data: for the most privileged Admin-tier role and the most restricted
Restricted-tier role, identify the specific enforcement layer where access diverges, citing the
SE-0 TABLE_4 row ID that established the admin-tier ceiling. State whether the divergence is
expected and what sharing-rule interaction (if any) was confirmed or ruled out in SE-0 TABLE_4.

### SE-5 / SHALL-E — Section 5: Security Gap Inventory

**TABLE_5 — Security Gap Inventory** *(Schema Registry TABLE_5 with Tier column; blank-cell rule)*

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
- Verification — TABLE_4 at SE-0 (before SE-1)? All four vectors? Checked? = YES? Findings or specific rule-outs? -> PASS / FAIL

**CA-1.5 — C-05 verification** *(Phase 0 M4 pre-assignment CA-1.5)*:
- Registry anchor — Schema ID TABLE_5 (with Tier): [#, Gap Type, Entity, Field or Rule, Role, Tier, Severity, Remediation] — blank cells prohibited globally.
- Preamble anchor — C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 — verifying...
- Verification — TABLE_5 present? Named gap? Tier column populated? Remediations exact? -> PASS / FAIL

**CA-1.6 — SHALL-F compliance verification** *(CS-EXPECTATION-VIOLATED three-field structure)*:
- Registry anchor — Schema ID TABLE_5 CS-EXPECTATION-VIOLATED row: [CS-Expected field, SE-Actual field, Delta field] — all three required per SHALL-F declaration in Phase 0.
- Preamble anchor — SHALL-F as authored by CA in Phase 0: three-field Remediation block mandatory; rows missing any field MUST be reopened.
- Verification — For each CS-EXPECTATION-VIOLATED row: CS-Expected populated? SE-Actual populated? Delta populated with exact configuration change? -> PASS / FAIL per row.

**CA-1.7 — SHALL-G compliance verification** *(exact-label two-part closure blocks)*:
- Registry anchor — CONTEXT section declared exact labels: "Blind spot 1 — Post-incident FLS gap" (SE-2 target), "Blind spot 2 — Cumulative privilege blind spot" (SE-3 target), "Blind spot 3 — OWD-sharing-rule override gap" (SE-4 target). SHALL-G requires two-part blocks with exact label in brackets.
- Preamble anchor — SHALL-G as authored by CA in Phase 0: Line 1 MUST be `MANUAL GAP [<exact CONTEXT label>]:`; exact = character-for-character; paraphrase fails; single-line annotation fails; TABLE_5 consolidation fails; CA-1.7 verifies.
- Verification — SE-2 opens with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:`? Followed by `STRUCTURED CLOSE:`? SE-3 opens with `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:`? Followed by `STRUCTURED CLOSE:`? SE-4 opens with `MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:`? Followed by `STRUCTURED CLOSE:`? -> PASS / FAIL per section.

**CA-1.8 — CS-2/CS-3 Schema Registry registration + CS-0 acknowledgment verification** *(C-29 + C-33)*:
- Registry anchor — Schema Registry declared CS-2 as a named schema entry with SE-updatable columns SE Cross-Reference and SE Confirmation and SE-update protocol co-located. Schema Registry declared CS-3 same. PHASE 1 mandate requires CS-0 sub-section to acknowledge both schema IDs and list SE-updatable columns before CS-1/CS-2/CS-3.
- Preamble anchor — CS-2 and CS-3 are Schema Registry entries alongside TABLE_1-5. CS-0 acknowledgment is a PHASE 1 structural requirement: CS cites both schema IDs and SE-updatable columns before authoring expectation rows. CA-1.8 verifies.
- Verification — CS-2 in Schema Registry with SE-updatable column declarations? CS-3 same? CS-0 present before CS-1? CS-0 cites CS-2 schema ID by exact label? CS-0 cites CS-3 schema ID by exact label? CS-0 lists SE-updatable columns for both? SE populated SE-updatable columns per protocol? -> PASS / FAIL

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0), Phase 0 by label.
[C-01 through C-05 with CA-1.1 through CA-1.5 results. SHALL-F (CA-1.6). SHALL-G exact-label two-part block compliance (CA-1.7). C-29 + C-33 CS-0 acknowledgment (CA-1.8). Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

---
---

## V-02 — Single Axis: C-35 (SE-4 TABLE_4 SE-0 Row Cross-Reference + CA-1.9)

**Axis:** C-35 — SE-4 STRUCTURED CLOSE + CA-1.9 only
**Hypothesis:** C-35 requires SE-4's STRUCTURED CLOSE to cite a specific TABLE_4 SE-0 row (not generic "TABLE_4 (filled at SE-0)" prose) and a new CA-1.9 verification row that is auditing D-2 independently of CA-1.4 (TABLE_4 placement) and CA-1.7 (MANUAL GAP labels). V-05 SE-4 currently says "citing SE-0 data" without naming the specific row. Adding the row citation to STRUCTURED CLOSE and a CA-1.9 template should pass C-35 without changing the preamble or verdict. C-34 and C-36 remain open.

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

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins.

**PHASE 0 — CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1) and the Criterion Enforcement Matrix
preamble (Step 0.2). CA issues handoff to PHASE 1.

**PHASE 1 — CS (Customer Success):**
Executes second. Opens with CS-0 Registry acknowledgment. Then produces CS-1, CS-2, CS-3.
CS does not fill TABLE_1-5. CS issues handoff to PHASE 2.

**PHASE 2 — SE (Security Engineer / Dataverse Security Expert):**
Executes third in privilege-tier descent order. SE-0 (admin-tier inventory and TABLE_4) runs
before SE-1. TABLE_1 and TABLE_3 include Tier column. SE-2/SE-3/SE-4 use exact-label two-part
closure blocks per SHALL-G. SE-4 STRUCTURED CLOSE cites a specific TABLE_4 SE-0 row by name.
Issues handoff to PHASE 3.

**PHASE 3 — CA-1 (CA Verification Pass):**
CA returns. Each CA-1 row performs double-anchor reaffirmation. CA-1.8 verifies CS-0.
CA-1.9 verifies SE-4 STRUCTURED CLOSE TABLE_4 SE-0 row cross-reference as a distinct audit
target from CA-1.4 (TABLE_4 placement) and CA-1.7 (MANUAL GAP label accuracy).

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1 and 0.2 before any other phase begins.*

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Tier values: Admin / Custom / Restricted. Blank-cell rule global.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Blank-cell rule: FLS Profile Configured? = Configured / Not Configured (never blank). Gap? = YES / NO.

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Tier values mirror TABLE_1. Blank-cell rule global.

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
Rows: Team inheritance / Sharing rules / Impersonation (Act on Behalf Of) / Admin-environment role override.
All four rows authored at SE-0 before SE-1. Each row is a named SE-0 output available as
cross-reference target for later sections (including SE-4 STRUCTURED CLOSE).

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation`
Blank-cell rule global. CS-EXPECTATION-VIOLATED Remediation = three-field block (CS-Expected /
SE-Actual / Delta).

**Schema ID: CS-2 — Sharing Rule Expectations**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference; SE Confirmation. SE update protocol: SE populates after
TABLE_4 at SE-0. CONTRADICTED triggers CS-EXPECTATION-VIOLATED per SHALL-F.

**Schema ID: CS-3 — Cross-Role Access Differential Expectations**
Declared columns: `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference; SE Confirmation. SE update protocol: SE populates after
TABLE_1/TABLE_3 analysis. CONTRADICTED triggers CS-EXPECTATION-VIOLATED per SHALL-F.

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

- SHALL-A: Complete TABLE_1 with Tier column. Every cell Granted/Denied/Conditional/N/A. Rows ordered by tier.
- SHALL-B: TABLE_2 lists all PII, Financial, and Audit-Compliance fields with explicit FLS status. Null case explicit. Gap? YES rows in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier and Effective Scope filled. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 at SE-0 (before SE-1), all four vectors, Checked? = YES. Rule-outs name specific mechanism and reason.
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap case requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field Remediation block (CS-Expected, SE-Actual, Delta). CA-1.6 verifies.
- SHALL-G: At the opening of SE-2, SE-3, and SE-4, closure MUST appear as a two-part labeled block — Line 1: `MANUAL GAP [<exact CONTEXT label>]:`; Line 2: description; Line 3: `STRUCTURED CLOSE:`; Line 4: mechanism. CA-1.7 verifies exact label carry-through.
- SHALL-H: SE-4 STRUCTURED CLOSE MUST cite a specific TABLE_4 SE-0 row by name or position label (not generic "TABLE_4 (filled at SE-0)" prose). The Sharing rules row is a named SE-0 output and is the expected cross-reference target. CA-1.9 verifies as a distinct audit target from CA-1.4 and CA-1.7.

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

### CS-0 — Schema Registry Acknowledgment (CS-authored, Phase 1)

**Registry acknowledgment for CS-2:**
Schema ID: CS-2 — Sharing Rule Expectations.
SE-updatable columns as declared by CA in Phase 0 Schema Registry: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged. Expectation format confirmed. SE-updatable columns left blank.

**Registry acknowledgment for CS-3:**
Schema ID: CS-3 — Cross-Role Access Differential Expectations.
SE-updatable columns as declared by CA in Phase 0 Schema Registry: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged. Expectation format confirmed. SE-updatable columns left blank.

### CS-1 — Expected Customer Service Access Baseline

For each entity in scope: (a) CRUD operations expected; (b) expected record scope; (c) sensitive
fields CS needs and why. Flag configurations that may open access beyond job requirements.

**CS-2** *(Schema Registry CS-2; SE-updatable columns blank)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

**CS-3** *(Schema Registry CS-3; SE-updatable columns blank)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis (Privilege-Tier Descent Order)

### SE-0 — Admin-Tier Inventory and Escalation Vectors

**Admin-tier role inventory:** List System Administrator, Environment Admin, and admin-equivalent
roles. Note any admin capability bypassing lower-tier controls.

**TABLE_4 — Escalation Vector Inventory** *(Schema Registry TABLE_4; SE-0 before SE-1)*

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Finding format: `[Role] -> [Mechanism] -> [Elevated access achieved]` for confirmed escalation;
"Checked [mechanism]: no path found because [specific reason]" for rule-out. After TABLE_4:
populate CS-2 SE Cross-Reference and SE Confirmation.

### SE-1 / SHALL-A — Role-Operation Matrix

**TABLE_1** *(Schema Registry TABLE_1 with Tier column)*

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Rows ordered: Admin tier first, Custom tier second, Restricted tier last. After TABLE_1: populate
CS-3 SE Cross-Reference and SE Confirmation.

**Cross-role differential analysis:** Compare the CS role against at least one Admin-tier and one
Custom-tier role. Cite TABLE_4 row ID for any differential attributable to admin-tier vectors.

### SE-2 / SHALL-B — Field-Level Security Coverage

MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:
Column security profiles are not auditable from the security roles UI; administrators discover
missing FLS only after a data exposure event.

STRUCTURED CLOSE:
TABLE_2 below enumerates every sensitive field with explicit FLS status, surfacing pre-event what
the security roles UI conceals. All Not Configured fields forwarded to TABLE_5 as MISSING-FLS.

**TABLE_2** *(Schema Registry TABLE_2)*

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

**Defense-in-depth layer check:** Identify enforcement layer for at least one sensitive field.

### SE-3 / SHALL-C — Record Access Scope

MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access produced by a security role
plus owner team membership plus OWD.

STRUCTURED CLOSE:
TABLE_3 below maps effective scope for every role by Tier, making team-accumulated privilege
visible at the tier it occurs.

**TABLE_3** *(Schema Registry TABLE_3 with Tier column)*

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role MUST appear, ordered by Tier. After TABLE_3: update CS-3 SE Confirmation.

### SE-4 / SHALL-D — Privilege Escalation Cross-Reference

MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing sharing rules that
silently override them.

STRUCTURED CLOSE:
TABLE_4 (authored at SE-0) evaluated all four escalation vectors. Cross-reference for this
section: TABLE_4 SE-0 row — Sharing rules — [cite by row name "Sharing rules"]. This section
uses the TABLE_4 SE-0 Sharing rules row to construct the cross-tier differential summary: for
the most privileged Admin-tier role and the most restricted Restricted-tier role, identify the
specific enforcement layer where access diverges, citing the TABLE_4 SE-0 Sharing rules row
by name. State whether the divergence is expected and what sharing-rule interaction (if any)
was confirmed or ruled out at SE-0.

### SE-5 / SHALL-E — Security Gap Inventory

**TABLE_5** *(Schema Registry TABLE_5)*

| # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation |
|---|----------|--------|---------------|------|------|----------|-------------|

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

**CA-1.1** *(Phase 0 M4 pre-assignment CA-1.1)*:
- Registry anchor — Schema ID TABLE_1 (with Tier): [Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope] — blank cells prohibited globally.
- Preamble anchor — C-01 as authored by CA in Phase 0: TABLE_1 / SE-1 / SHALL-A / CA-1.1 — verifying...
- Verification — TABLE_1 present? Tier column? Ordered by tier? All cells? -> PASS / FAIL

**CA-1.2** *(Phase 0 M4 pre-assignment CA-1.2)*:
- Registry anchor — Schema ID TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?].
- Preamble anchor — C-02: TABLE_2 / SE-2 / SHALL-B / CA-1.2 — verifying...
- Verification — TABLE_2 present? All sensitive fields? FLS status explicit? Null case? Gap? YES in TABLE_5? -> PASS / FAIL

**CA-1.3** *(Phase 0 M4 pre-assignment CA-1.3)*:
- Registry anchor — Schema ID TABLE_3 (with Tier): [Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Verified?].
- Preamble anchor — C-03: TABLE_3 / SE-0+SE-3 / SHALL-C / CA-1.3 — verifying...
- Verification — Every TABLE_1 role in TABLE_3? Tier? Effective Scope filled? -> PASS / FAIL

**CA-1.4** *(Phase 0 M4 pre-assignment CA-1.4)*:
- Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity] — all four vectors.
- Preamble anchor — C-04: TABLE_4 / SE-0 / SHALL-D / CA-1.4 — verifying...
- Verification — TABLE_4 at SE-0 (before SE-1)? All four vectors? Checked? = YES? -> PASS / FAIL

**CA-1.5** *(Phase 0 M4 pre-assignment CA-1.5)*:
- Registry anchor — Schema ID TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Tier, Severity, Remediation].
- Preamble anchor — C-05: TABLE_5 / SE-5 / SHALL-E / CA-1.5 — verifying...
- Verification — TABLE_5 present? Named gap? Tier? Remediations exact? -> PASS / FAIL

**CA-1.6** *(SHALL-F compliance)*:
- Registry anchor — TABLE_5 CS-EXPECTATION-VIOLATED: [CS-Expected, SE-Actual, Delta] — three-field block required.
- Preamble anchor — SHALL-F: three-field block mandatory; missing field = reopen.
- Verification — Each CS-EXPECTATION-VIOLATED row: all three fields populated? -> PASS / FAIL per row.

**CA-1.7** *(SHALL-G compliance)*:
- Registry anchor — CONTEXT exact labels: "Blind spot 1 — Post-incident FLS gap" / "Blind spot 2 — Cumulative privilege blind spot" / "Blind spot 3 — OWD-sharing-rule override gap".
- Preamble anchor — SHALL-G: `MANUAL GAP [<exact label>]:` character-for-character; paraphrase fails.
- Verification — SE-2/SE-3/SE-4 each open with exact two-part block? -> PASS / FAIL per section.

**CA-1.8** *(CS-0 acknowledgment + CS-2/CS-3 Schema Registry)*:
- Registry anchor — Schema Registry declared CS-2 and CS-3 with SE-updatable columns co-located.
- Preamble anchor — CS-0 required to cite both schema IDs by exact label before CS-1.
- Verification — CS-0 present? Cites CS-2 and CS-3 by exact Schema ID label? Lists SE-updatable columns? -> PASS / FAIL

**CA-1.9 — C-35 verification (SE-4 STRUCTURED CLOSE TABLE_4 SE-0 row cross-reference)** *(D-2 axis; distinct from CA-1.4 and CA-1.7)*:
- Registry anchor — Schema ID TABLE_4: Sharing rules row is a named SE-0 output (Vector = "Sharing rules") available as a cross-reference target by name. The row is authored at SE-0; SE-4 STRUCTURED CLOSE may cite it by row name.
- Preamble anchor — SHALL-H as authored by CA in Phase 0: SE-4 STRUCTURED CLOSE MUST cite a specific TABLE_4 SE-0 row by name or position label; generic "TABLE_4 (filled at SE-0)" prose fails SHALL-H. CA-1.9 is a distinct audit target: it tests STRUCTURED CLOSE content, not TABLE_4 placement before SE-1 (CA-1.4) and not MANUAL GAP exact-label accuracy (CA-1.7).
- Verification — SE-4 STRUCTURED CLOSE present? Cites "TABLE_4 SE-0 Sharing rules row" or equivalent named row citation (not generic prose reference)? Citation traceable to a specific SE-0 row by name? -> PASS / FAIL

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0), Phase 0 by label.
[C-01 through C-05 CA-1.1..CA-1.5. SHALL-F CA-1.6. SHALL-G CA-1.7. CS-0 acknowledgment CA-1.8. C-35 SE-4 cross-reference CA-1.9. Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

---
---

## V-03 — Single Axis: C-36 (CA Terminal Verdict Tri-Dimensional Self-Evidence Attestation)

**Axis:** C-36 — CA verdict tri-dimensional attestation only
**Hypothesis:** C-36 requires the CA terminal verdict to explicitly name each R12 dimension (D-1/D-2/D-3) and cite its specific output-body evidence source — making each dimension self-attestable from the output text without prompt inspection. The R12 dimensions are: D-1 (execution order), D-2 (closure-note format), D-3 (CS self-reference). Adding a tri-dimensional attestation table at the CA verdict, with each row naming the evidence location in the output body, should pass C-36 without modifying the preamble or SE-4. C-34 and C-35 remain open.

---

depth: standard
confidence: standard

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

Manual security reviews of Dataverse environments routinely miss three failure scenarios that this
trace is designed to surface:

**Blind spot 1 — Post-incident FLS gap.** Column security profiles are rarely audited proactively.
Sensitive fields remain readable and writable by any role unless a column security profile
explicitly restricts them. Gaps are discovered after data exposure, not before.

**Blind spot 2 — Cumulative privilege blind spot.** A user holding a BU-scoped security role who
also belongs to an owner team whose team role grants org-wide access has effective org-wide access.
No single Dataverse UI view surfaces the combined effective access. Spot-checking individual roles
misses cross-role accumulation through team membership.

**Blind spot 3 — OWD-sharing-rule override gap.** Administrators check OWD settings
entity-by-entity without evaluating the sharing rules that silently override those baselines. A
Private OWD combined with a Power Automate-triggered sharing rule can grant effective org-wide
read without appearing in any security roles UI view.

This trace closes all three blind spots: SE-2 closes Blind spot 1; SE-3 closes Blind spot 2;
SE-4 closes Blind spot 3. Closure notes are exact-label two-part blocks co-located at each SE
sub-section opening, carrying the exact blind-spot label from this CONTEXT section.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers.

**PHASE 0 — CA:** Authors Schema Registry (Step 0.1) and Criterion Enforcement Matrix preamble
(Step 0.2). Issues handoff to PHASE 1.

**PHASE 1 — CS:** Opens with CS-0 Registry acknowledgment. Produces CS-1/CS-2/CS-3.
Issues handoff to PHASE 2.

**PHASE 2 — SE:** SE-0 (TABLE_4 escalation vectors) before SE-1. TABLE_1 and TABLE_3 include
Tier column. SE-2/SE-3/SE-4 use exact-label two-part closure blocks per SHALL-G. Issues handoff
to PHASE 3.

**PHASE 3 — CA-1:** Double-anchor verification rows CA-1.1..CA-1.8. CA terminal verdict includes
R12 Tri-Dimensional Self-Evidence Attestation naming each dimension's output-body evidence source.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

**Schema ID: TABLE_1 — Role-Operation Matrix**
`Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Tier: Admin / Custom / Restricted. Rows ordered by tier. Blank-cell rule global.

**Schema ID: TABLE_2 — FLS Coverage**
`Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
FLS Profile Configured? = Configured / Not Configured. Gap? = YES / NO.

**Schema ID: TABLE_3 — Record Scope by Role**
`Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Tier mirrors TABLE_1. Blank-cell rule global.

**Schema ID: TABLE_4 — Escalation Vector Inventory**
`Vector | Checked? | Finding | Severity`
Four rows: Team inheritance / Sharing rules / Impersonation / Admin-role override.
Authored at SE-0 before SE-1.

**Schema ID: TABLE_5 — Security Gap Inventory**
`# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation`
CS-EXPECTATION-VIOLATED Remediation = three-field block (CS-Expected / SE-Actual / Delta).

**Schema ID: CS-2 — Sharing Rule Expectations**
`Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference / SE Confirmation. SE populates after TABLE_4 at SE-0.

**Schema ID: CS-3 — Cross-Role Access Differential Expectations**
`Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference / SE Confirmation. SE populates after TABLE_1/TABLE_3.

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: M1, M2, M3 simultaneously active. M4 pre-assigned.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-0 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

- SHALL-A: TABLE_1 with Tier column. Every cell Granted/Denied/Conditional/N/A. Ordered by tier.
- SHALL-B: TABLE_2 all PII/Financial/Audit-Compliance fields. Explicit FLS status. Null case stated. Gap? YES in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier and Effective Scope. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 at SE-0 before SE-1. All four vectors. Checked? = YES. Rule-outs name specific reason.
- SHALL-E: TABLE_5 at least one named gap. Zero-gap case requires explicit evidence.
- SHALL-F: CS-EXPECTATION-VIOLATED three-field Remediation block mandatory. CA-1.6 verifies.
- SHALL-G: SE-2/SE-3/SE-4 open with exact-label two-part closure block. CA-1.7 verifies character-for-character.

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS

### CS-0 — Schema Registry Acknowledgment

**Registry acknowledgment for CS-2:** Schema ID: CS-2. SE-updatable columns: SE Cross-Reference, SE Confirmation. Protocol: SE fills after SE-0. Format confirmed. SE-updatable columns blank.

**Registry acknowledgment for CS-3:** Schema ID: CS-3. SE-updatable columns: SE Cross-Reference, SE Confirmation. Protocol: SE fills after TABLE_1/TABLE_3. Format confirmed. SE-updatable columns blank.

### CS-1 — Expected Customer Service Access Baseline

For each entity: expected CRUD operations, expected record scope, sensitive fields needed.

**CS-2** *(SE-updatable columns blank)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

**CS-3** *(SE-updatable columns blank)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE

### SE-0 — Admin-Tier Inventory and Escalation Vectors

Admin-tier inventory. Then:

**TABLE_4** *(SE-0 before SE-1)*

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

### SE-1 / SHALL-A — Role-Operation Matrix

**TABLE_1** *(with Tier column)*

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Cross-role differential analysis vs Admin-tier and Custom-tier roles.

### SE-2 / SHALL-B — FLS Coverage

MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:
Column security profiles not auditable from roles UI; gaps found only after exposure.

STRUCTURED CLOSE:
TABLE_2 enumerates every sensitive field with explicit FLS status, surfacing pre-event gaps.

**TABLE_2**

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Defense-in-depth layer check for at least one sensitive field.

### SE-3 / SHALL-C — Record Access Scope

MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:
No single UI view shows combined role + team + OWD effective access.

STRUCTURED CLOSE:
TABLE_3 maps effective scope for every role by Tier, making team-accumulated privilege auditable.

**TABLE_3** *(with Tier column)*

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|

### SE-4 / SHALL-D — Privilege Escalation Cross-Reference

MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:
OWD audited entity-by-entity without cross-referencing sharing rules that override baselines.

STRUCTURED CLOSE:
TABLE_4 (filled at SE-0) evaluated all four escalation vectors with sharing rules explicitly
cross-referenced against OWD settings. This section adds cross-tier differential summary citing
SE-0 data: for the most privileged Admin-tier role and the most restricted Restricted-tier role,
identify the specific enforcement layer where access diverges, citing the SE-0 TABLE_4 row ID
that established the admin-tier ceiling. State whether the divergence is expected and what
sharing-rule interaction was confirmed or ruled out.

### SE-5 / SHALL-E — Security Gap Inventory

**TABLE_5**

| # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation |
|---|----------|--------|---------------|------|------|----------|-------------|

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1

**CA-1.1** *(Phase 0 M4 pre-assignment CA-1.1)*:
- Registry anchor — TABLE_1 (with Tier): [Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope].
- Preamble anchor — C-01: TABLE_1 / SE-1 / SHALL-A / CA-1.1.
- Verification — TABLE_1 present? Tier? Ordered? All cells? -> PASS / FAIL

**CA-1.2** *(CA-1.2)*:
- Registry anchor — TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?].
- Preamble anchor — C-02: TABLE_2 / SE-2 / SHALL-B / CA-1.2.
- Verification — Present? Fields? FLS explicit? Null case? Gap? YES in TABLE_5? -> PASS / FAIL

**CA-1.3** *(CA-1.3)*:
- Registry anchor — TABLE_3 (with Tier): [Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Verified?].
- Preamble anchor — C-03: TABLE_3 / SE-0+SE-3 / SHALL-C / CA-1.3.
- Verification — Every TABLE_1 role in TABLE_3? Tier? Scope? -> PASS / FAIL

**CA-1.4** *(CA-1.4)*:
- Registry anchor — TABLE_4: [Vector, Checked?, Finding, Severity] — four vectors.
- Preamble anchor — C-04: TABLE_4 / SE-0 / SHALL-D / CA-1.4.
- Verification — TABLE_4 at SE-0 before SE-1? All four? Checked? = YES? -> PASS / FAIL

**CA-1.5** *(CA-1.5)*:
- Registry anchor — TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Tier, Severity, Remediation].
- Preamble anchor — C-05: TABLE_5 / SE-5 / SHALL-E / CA-1.5.
- Verification — Present? Named gap? Tier? Remediations exact? -> PASS / FAIL

**CA-1.6** *(SHALL-F)*:
- Registry anchor — TABLE_5 CS-EXPECTATION-VIOLATED: three-field block.
- Preamble anchor — SHALL-F: mandatory; missing field = reopen.
- Verification — All three fields per violated row? -> PASS / FAIL per row.

**CA-1.7** *(SHALL-G)*:
- Registry anchor — Exact CONTEXT labels for SE-2/SE-3/SE-4.
- Preamble anchor — SHALL-G: character-for-character carry-through; paraphrase fails.
- Verification — Each of SE-2/SE-3/SE-4 opens with exact two-part block? -> PASS / FAIL per section.

**CA-1.8** *(CS-0 acknowledgment + CS-2/CS-3 Registry)*:
- Registry anchor — CS-2 and CS-3 as named Schema Registry entries with SE-updatable columns.
- Preamble anchor — CS-0 required to cite both by exact Schema ID label before CS-1.
- Verification — CS-0 present? Cites CS-2 by exact label? Cites CS-3 by exact label? SE-updatable columns listed? SE filled them? -> PASS / FAIL

**CA Format Compliance Verdict — Phase 0 citation + R12 Tri-Dimensional Self-Evidence Attestation:**

Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0), Phase 0 by label.
[C-01..C-05: CA-1.1..CA-1.5. SHALL-F: CA-1.6. SHALL-G: CA-1.7. CS-0 acknowledgment: CA-1.8. Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

**R12 Tri-Dimensional Self-Evidence Attestation (C-36):**
Each R12 dimension is attested by naming its specific evidence source in the output body above.
Attestation is self-verifiable from the output text alone — prompt inspection not required.

| Dimension | ID | Output-Body Evidence Source | Self-Attestable? |
|-----------|----|-----------------------------|-----------------|
| Execution order | D-1 | Phase 0 section header in output body; "Handing to PHASE 1 — CS" handoff string at Step 0.2 close; CA-1 rows labeled "(Phase 0 M4 pre-assignment CA-1.x)" as provenance strings | [ATTESTED / NOT ATTESTED] |
| Closure-note format | D-2 | SE-4 STRUCTURED CLOSE body text (locate above); note whether it cites a specific TABLE_4 SE-0 row by name or uses generic prose — current architecture cites SE-0 data without naming the specific row | [ATTESTED / NOT ATTESTED] |
| CS self-reference | D-3 | CS-0 sub-section above names "Schema ID: CS-2" and "Schema ID: CS-3" by exact Registry label before CS-1 rows; CA-1.8 confirmed CS-0 precedes CS-1 | [ATTESTED / NOT ATTESTED] |

Overall tri-dimensional attestation: ATTESTED (all three self-attestable from output body) / PARTIAL (one or more dimensions not fully attested) / NOT ATTESTED.

---
---

## V-04 — Combined Axes: C-34 + C-35

**Axis:** C-34 (preamble axis declaration) + C-35 (SE-4 STRUCTURED CLOSE cross-reference + CA-1.9)
**Hypothesis:** C-34 and C-35 are structurally independent: C-34 is a Phase 0 preamble property; C-35 is a Phase 2/3 property. Combining both should show that the axis declaration in Phase 0 (naming D-2 by ID) does not interfere with the SE-4 STRUCTURED CLOSE addition or CA-1.9. The D-2 axis ID declared in Phase 0 is then traceable to the SE-4 cross-reference verified by CA-1.9. C-36 remains open.

---

depth: standard
confidence: standard

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

Manual security reviews of Dataverse environments routinely miss three failure scenarios that this
trace is designed to surface:

**Blind spot 1 — Post-incident FLS gap.** Column security profiles are rarely audited proactively.
Sensitive fields remain readable and writable unless a column security profile explicitly restricts
them. Gaps are discovered after data exposure, not before.

**Blind spot 2 — Cumulative privilege blind spot.** A user holding a BU-scoped role who also
belongs to an owner team with org-wide access has effective org-wide access. No single Dataverse
UI view surfaces the combined role + team + OWD effective access.

**Blind spot 3 — OWD-sharing-rule override gap.** Administrators check OWD entity-by-entity
without evaluating sharing rules that silently override those baselines.

This trace closes all three blind spots: SE-2 closes Blind spot 1; SE-3 closes Blind spot 2;
SE-4 closes Blind spot 3. Closure notes are exact-label two-part blocks at each SE sub-section
opening, carrying the exact blind-spot label from this CONTEXT section.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers.

**PHASE 0 — CA:** Authors Schema Registry (Step 0.1) and Criterion Enforcement Matrix preamble
including R12 Orthogonal Dimensions Declaration (Step 0.2). Issues handoff.

**PHASE 1 — CS:** CS-0 Registry acknowledgment before CS-1/CS-2/CS-3. Issues handoff.

**PHASE 2 — SE:** SE-0 TABLE_4 before SE-1. Tier columns on TABLE_1 and TABLE_3. Exact-label
two-part closure blocks on SE-2/SE-3/SE-4. SE-4 STRUCTURED CLOSE cites TABLE_4 SE-0 Sharing
rules row by name. Issues handoff.

**PHASE 3 — CA-1:** Double-anchor rows CA-1.1..CA-1.9. CA-1.9 verifies SE-4 cross-reference as
distinct from CA-1.4 and CA-1.7.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

### Step 0.1 — Schema Registry

**Schema ID: TABLE_1** — `Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` — Admin/Custom/Restricted, ordered by tier, blank-cell rule global.

**Schema ID: TABLE_2** — `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?` — FLS = Configured/Not Configured; Gap? = YES/NO.

**Schema ID: TABLE_3** — `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?` — Tier mirrors TABLE_1, blank-cell rule global.

**Schema ID: TABLE_4** — `Vector | Checked? | Finding | Severity` — four rows: Team inheritance / Sharing rules / Impersonation / Admin-role override. Authored at SE-0 before SE-1. All four rows available as named cross-reference targets by subsequent sections.

**Schema ID: TABLE_5** — `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation` — CS-EXPECTATION-VIOLATED Remediation = CS-Expected / SE-Actual / Delta three-field block.

**Schema ID: CS-2** — `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation` — SE-updatable: SE Cross-Reference, SE Confirmation (post-TABLE_4 at SE-0).

**Schema ID: CS-3** — `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation` — SE-updatable: SE Cross-Reference, SE Confirmation (post-TABLE_1/TABLE_3).

### Step 0.2 — Criterion Enforcement Matrix Preamble + R12 Orthogonal Dimensions Declaration

**Declared rule: M1, M2, M3 simultaneously active. M4 pre-assigned.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-0 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

- SHALL-A: TABLE_1 with Tier. All cells Granted/Denied/Conditional/N/A. Ordered by tier.
- SHALL-B: TABLE_2 all sensitive fields. Explicit FLS status. Null case. Gap? YES in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier and Effective Scope.
- SHALL-D: TABLE_4 at SE-0 before SE-1. All four vectors. Checked? = YES.
- SHALL-E: TABLE_5 at least one named gap or explicit zero-gap evidence.
- SHALL-F: CS-EXPECTATION-VIOLATED three-field Remediation mandatory. CA-1.6 verifies.
- SHALL-G: SE-2/SE-3/SE-4 exact-label two-part closure blocks. CA-1.7 verifies.
- SHALL-H: SE-4 STRUCTURED CLOSE cites TABLE_4 SE-0 Sharing rules row by name. CA-1.9 verifies independently of CA-1.4 and CA-1.7.

**R12 Orthogonal Dimensions Declaration (C-34):**

The three R12 structural dimensions are declared as orthogonal enforcement axes. Each is
independently verifiable. Failure of one does not propagate to or imply failure of the others.
All three SHALL be simultaneously active: this converts empirical co-presence into a binding
non-interference contract.

| Dimension | ID | Mechanism | Non-Interference Statement |
|-----------|----|-----------|-----------------------------|
| Execution order | D-1 | CA authors Schema Registry and preamble in Phase 0 before any SE/CS section. CA-1 rows reference pre-assigned M4 IDs as contract completion. | D-1 depends on CA authorship sequencing only. D-2 and D-3 may independently pass or fail without affecting D-1 verification. |
| Closure-note format | D-2 | SE-4 STRUCTURED CLOSE cites TABLE_4 SE-0 Sharing rules row by name per SHALL-H. CA-1.9 verifies this as a distinct audit target from CA-1.4 and CA-1.7. | D-2 depends on SE-4 STRUCTURED CLOSE content only. D-1 and D-3 may independently pass or fail without affecting D-2 verification. |
| CS self-reference | D-3 | CS-0 cites Schema Registry entries for CS-2 and CS-3 by exact Schema ID label before authoring any expectation rows. CA-1.8 verifies CS-0 precedes CS-1. | D-3 depends on CS-phase Registry acknowledgment only. D-1 and D-2 may independently pass or fail without affecting D-3 verification. |

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS

### CS-0 — Schema Registry Acknowledgment

**CS-2 acknowledgment:** Schema ID: CS-2 — Sharing Rule Expectations. SE-updatable: SE Cross-Reference, SE Confirmation. Protocol: SE fills after SE-0/TABLE_4. Format confirmed. Columns blank for SE.

**CS-3 acknowledgment:** Schema ID: CS-3 — Cross-Role Access Differential Expectations. SE-updatable: SE Cross-Reference, SE Confirmation. Protocol: SE fills after TABLE_1/TABLE_3. Format confirmed. Columns blank for SE.

### CS-1 — Expected Access Baseline

Expected CRUD operations, record scope, and sensitive field access per entity.

**CS-2** *(SE-updatable blank)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

**CS-3** *(SE-updatable blank)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE

### SE-0 — Admin-Tier Inventory + TABLE_4

Admin-tier inventory: System Administrator, Environment Admin, admin-equivalent roles.

**TABLE_4** *(SE-0, before SE-1)*

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Finding format: `[Role] -> [Mechanism] -> [Access]` for confirmed path; "Checked [mechanism]: no path because [reason]" for rule-out. Populate CS-2 SE Cross-Reference and SE Confirmation after TABLE_4.

### SE-1 / SHALL-A — Role-Operation Matrix

**TABLE_1** *(with Tier column; ordered Admin / Custom / Restricted)*

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Populate CS-3 SE Cross-Reference and SE Confirmation after TABLE_1.

Cross-role differential: CS role vs Admin-tier and Custom-tier. Cite TABLE_4 row ID for admin escalation differentials.

### SE-2 / SHALL-B — FLS Coverage

MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:
Column security profiles not auditable from roles UI; gaps surface only after data exposure.

STRUCTURED CLOSE:
TABLE_2 enumerates every sensitive field with explicit FLS status, surfacing pre-event gaps.

**TABLE_2**

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Defense-in-depth layer check for at least one sensitive field.

### SE-3 / SHALL-C — Record Access Scope

MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:
No single UI view shows combined role + team + OWD effective access.

STRUCTURED CLOSE:
TABLE_3 maps effective scope for every role by Tier, making team-accumulated privilege auditable.

**TABLE_3** *(with Tier column)*

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|

Update CS-3 SE Confirmation after TABLE_3.

### SE-4 / SHALL-D — Privilege Escalation Cross-Reference

MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:
OWD audited entity-by-entity without cross-referencing sharing rules that override baselines.

STRUCTURED CLOSE:
TABLE_4 (authored at SE-0, rows: Team inheritance / Sharing rules / Impersonation / Admin-role
override) evaluated all four escalation vectors. Cross-reference: TABLE_4 SE-0 — Sharing rules
row [cite "Sharing rules" by row name]. This section uses the TABLE_4 SE-0 Sharing rules row
to construct the cross-tier differential summary: for the most privileged Admin-tier role and
the most restricted Restricted-tier role, identify the specific enforcement layer where access
diverges, citing the TABLE_4 SE-0 Sharing rules row by name. State whether the divergence is
expected and what sharing-rule interaction was confirmed or ruled out at SE-0.

### SE-5 / SHALL-E — Security Gap Inventory

**TABLE_5**

| # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation |
|---|----------|--------|---------------|------|------|----------|-------------|

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1

**CA-1.1** *(Phase 0 M4 pre-assignment CA-1.1)*:
- Registry anchor — TABLE_1 (Tier): [Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope].
- Preamble anchor — C-01: TABLE_1 / SE-1 / SHALL-A / CA-1.1.
- Verification -> PASS / FAIL

**CA-1.2** *(CA-1.2)*:
- Registry anchor — TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?].
- Preamble anchor — C-02: TABLE_2 / SE-2 / SHALL-B / CA-1.2.
- Verification -> PASS / FAIL

**CA-1.3** *(CA-1.3)*:
- Registry anchor — TABLE_3 (Tier): [Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Verified?].
- Preamble anchor — C-03: TABLE_3 / SE-0+SE-3 / SHALL-C / CA-1.3.
- Verification -> PASS / FAIL

**CA-1.4** *(CA-1.4)*:
- Registry anchor — TABLE_4: [Vector, Checked?, Finding, Severity].
- Preamble anchor — C-04: TABLE_4 / SE-0 / SHALL-D / CA-1.4.
- Verification — TABLE_4 at SE-0 before SE-1? All four vectors? Checked? = YES? -> PASS / FAIL

**CA-1.5** *(CA-1.5)*:
- Registry anchor — TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Tier, Severity, Remediation].
- Preamble anchor — C-05: TABLE_5 / SE-5 / SHALL-E / CA-1.5.
- Verification -> PASS / FAIL

**CA-1.6** *(SHALL-F)*:
- Registry anchor — CS-EXPECTATION-VIOLATED three-field block.
- Preamble anchor — SHALL-F mandatory.
- Verification -> PASS / FAIL per row.

**CA-1.7** *(SHALL-G)*:
- Registry anchor — Exact CONTEXT labels.
- Preamble anchor — SHALL-G character-for-character.
- Verification — SE-2/SE-3/SE-4 exact two-part blocks? -> PASS / FAIL per section.

**CA-1.8** *(CS-0 acknowledgment)*:
- Registry anchor — CS-2 and CS-3 as Schema Registry entries with SE-updatable columns.
- Preamble anchor — CS-0 cites both by exact Schema ID label before CS-1.
- Verification -> PASS / FAIL

**CA-1.9 — C-35 verification (SE-4 STRUCTURED CLOSE TABLE_4 SE-0 row cross-reference)** *(D-2 axis; distinct from CA-1.4 and CA-1.7)*:
- Registry anchor — TABLE_4 Sharing rules row is a named SE-0 output (Vector = "Sharing rules") available as cross-reference target by name.
- Preamble anchor — SHALL-H: SE-4 STRUCTURED CLOSE MUST cite TABLE_4 SE-0 Sharing rules row by name; generic prose fails. CA-1.9 audits STRUCTURED CLOSE content, not TABLE_4 placement (CA-1.4) or MANUAL GAP label accuracy (CA-1.7).
- Verification — SE-4 STRUCTURED CLOSE cites "TABLE_4 SE-0 — Sharing rules row" by name (not generic "TABLE_4 (filled at SE-0)")? -> PASS / FAIL

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0), Phase 0 by label.
[C-01..C-05: CA-1.1..CA-1.5. SHALL-F: CA-1.6. SHALL-G: CA-1.7. CS-0: CA-1.8. C-35 SE-4 cross-reference: CA-1.9. Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

---
---

## V-05 — Full Integration: C-34 + C-35 + C-36 (28/28 Target)

**Axis:** C-34 + C-35 + C-36 simultaneously active
**Hypothesis:** All three R12 new criteria can be simultaneously satisfied with zero interference:
C-34 (preamble axis declaration with non-interference table) declares D-1/D-2/D-3 as IDs before
analysis begins; C-35 (SE-4 STRUCTURED CLOSE Sharing rules row citation + CA-1.9) closes the
D-2 axis in the output body; C-36 (tri-dimensional terminal attestation) references all three
D-IDs by their output-body evidence sources in the CA verdict. Together with V-05/R12's existing
25 criteria, this should reach 28/28.

---

depth: standard
confidence: standard

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

Manual security reviews of Dataverse environments routinely miss three failure scenarios that this
trace is designed to surface:

**Blind spot 1 — Post-incident FLS gap.** Column security profiles are rarely audited proactively.
Sensitive fields remain readable and writable unless a column security profile explicitly restricts
them. Gaps are discovered after data exposure, not before.

**Blind spot 2 — Cumulative privilege blind spot.** A user holding a BU-scoped role who also
belongs to an owner team with org-wide access has effective org-wide access. No single Dataverse
UI view surfaces the combined role + team + OWD effective access.

**Blind spot 3 — OWD-sharing-rule override gap.** Administrators check OWD entity-by-entity
without evaluating sharing rules that silently override those baselines. A Private OWD combined
with an active sharing rule can grant effective org-wide read without appearing in any UI view.

This trace closes all three blind spots: SE-2 closes Blind spot 1; SE-3 closes Blind spot 2;
SE-4 closes Blind spot 3. Closure notes are exact-label two-part blocks at each SE sub-section
opening, carrying the exact blind-spot label from this CONTEXT section.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins.

**PHASE 0 — CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1: seven schemas, TABLE_1 through TABLE_5
plus CS-2 and CS-3 with Tier columns on TABLE_1 and TABLE_3, SE-updatable columns and protocols
co-located on CS-2 and CS-3) and the Criterion Enforcement Matrix preamble including the R12
Orthogonal Dimensions Declaration (Step 0.2: SHALL-A through SHALL-H, M4 row IDs CA-1.1 through
CA-1.9 pre-assigned, D-1/D-2/D-3 declared with non-interference contracts). CA issues handoff to
PHASE 1.

**PHASE 1 — CS (Customer Success):**
Executes second. Opens with CS-0 Registry acknowledgment (cites Schema ID: CS-2 and Schema ID:
CS-3 by exact label, lists SE-updatable columns, confirms format). Then produces CS-1, CS-2, CS-3
using Registry schemas. Does not fill TABLE_1-5. Issues handoff to PHASE 2.

**PHASE 2 — SE (Security Engineer / Dataverse Security Expert):**
Executes third in privilege-tier descent order. SE-0 (admin-tier inventory + TABLE_4 escalation
vectors) runs before SE-1. TABLE_1 and TABLE_3 include Tier column. SE-2/SE-3/SE-4 use
exact-label two-part closure blocks per SHALL-G. SE-4 STRUCTURED CLOSE cites TABLE_4 SE-0
Sharing rules row by name per SHALL-H. Issues handoff to PHASE 3.

**PHASE 3 — CA-1 (CA Verification Pass):**
CA returns. Each CA-1 row performs double-anchor reaffirmation (Registry anchor + Preamble anchor
as distinct labeled elements; inline concatenation fails C-24). CA-1.8 verifies CS-0 acknowledgment.
CA-1.9 verifies SE-4 STRUCTURED CLOSE cross-reference as distinct from CA-1.4 and CA-1.7. CA
terminal verdict includes R12 Tri-Dimensional Self-Evidence Attestation.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1 and 0.2 before any other phase begins.*

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

**All schemas declared centrally. Blank-cell prohibition global. SE-update protocols for CS-2
and CS-3 co-located with schema entry.**

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Tier values: Admin / Custom / Restricted. Rows ordered Admin first, Custom second, Restricted last.
Blank-cell rule: every cell = Granted / Denied / Conditional (condition inline) / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
FLS Profile Configured? = Configured / Not Configured (never blank). Gap? = YES / NO.

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Tier mirrors TABLE_1. Effective Scope = Own / BU / Parent-Child BU / Org-wide / Team-scoped /
Sharing-[rule name]. Verified? = YES / NO.

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
Four rows: Team inheritance / Sharing rules / Impersonation (Act on Behalf Of) / Admin-environment
role override. All four authored at SE-0 before SE-1. Each row is a named SE-0 output available
as a cross-reference target by subsequent sections (including SE-4 STRUCTURED CLOSE per SHALL-H).

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation`
Blank-cell rule global. CS-EXPECTATION-VIOLATED Remediation = three-field block:
- CS-Expected: cite CS-2 or CS-3 row, expectation verbatim or by row reference.
- SE-Actual: SE finding that contradicts the expectation.
- Delta: exact configuration change to align SE-Actual to CS-Expected.

**Schema ID: CS-2 — Sharing Rule Expectations (CS-authored)**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference (TABLE_4 row ID or TABLE_5 row ID);
SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE update protocol: SE populates after TABLE_4 analysis at SE-0. CONTRADICTED triggers
CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

**Schema ID: CS-3 — Cross-Role Access Differential Expectations (CS-authored)**
Declared columns: `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference (TABLE_1 or TABLE_3 row ID);
SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE update protocol: SE populates after TABLE_1/TABLE_3 analysis. CONTRADICTED triggers
CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

### Step 0.2 — Criterion Enforcement Matrix Preamble + R12 Orthogonal Dimensions Declaration (CA-authored, Phase 0)

**Declared rule: M1, M2, M3 simultaneously active. M4 pre-assigned.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-0 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A: TABLE_1 with Tier column. Every cell Granted/Denied/Conditional/N/A. Rows ordered by tier.
- SHALL-B: TABLE_2 all PII, Financial, Audit-Compliance fields. Explicit FLS status. Null case stated. Gap? YES in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier and Effective Scope. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 at SE-0 before SE-1. All four vectors. Checked? = YES. Rule-outs name specific mechanism and reason.
- SHALL-E: TABLE_5 at least one named gap. Zero-gap case requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field Remediation block (CS-Expected, SE-Actual, Delta). Incomplete rows MUST be reopened. CA-1.6 verifies.
- SHALL-G: SE-2/SE-3/SE-4 each open with exact-label two-part block: Line 1 `MANUAL GAP [<exact CONTEXT label>]:`, Line 3 `STRUCTURED CLOSE:`. Character-for-character; paraphrase fails. CA-1.7 verifies.
- SHALL-H: SE-4 STRUCTURED CLOSE MUST cite TABLE_4 SE-0 Sharing rules row by name or position label. Generic "TABLE_4 (filled at SE-0)" prose fails SHALL-H. CA-1.9 verifies as a distinct audit target from CA-1.4 (TABLE_4 placement) and CA-1.7 (MANUAL GAP label accuracy).

**R12 Orthogonal Dimensions Declaration (C-34):**

The three R12 structural dimensions are declared as orthogonal enforcement axes. Each dimension
is independently verifiable. The failure of one dimension does not propagate to or imply the
failure of the others. All three dimensions SHALL be simultaneously active: this declaration
converts empirical co-presence of D-1/D-2/D-3 into a binding non-interference contract.

| Dimension | ID | Mechanism | Non-Interference Statement |
|-----------|----|-----------|-----------------------------|
| Execution order | D-1 | CA authors Schema Registry (Step 0.1) and Criterion Enforcement Matrix preamble (Step 0.2) before any SE or CS section begins. CA-1 rows reference pre-assigned M4 IDs as contract completion, not post-hoc decoration. Phase 0 section header and handoff string in output body are D-1 evidence. | D-1 verifiability depends on CA authorship sequencing only. D-2 and D-3 may independently pass or fail without affecting D-1 verification. |
| Closure-note format | D-2 | SE-4 STRUCTURED CLOSE cites TABLE_4 SE-0 Sharing rules row by name per SHALL-H. CA-1.9 verifies this as a distinct audit target from CA-1.4 and CA-1.7. SE-4 STRUCTURED CLOSE body text is D-2 evidence. | D-2 verifiability depends on SE-4 STRUCTURED CLOSE content only. D-1 and D-3 may independently pass or fail without affecting D-2 verification. |
| CS self-reference | D-3 | CS-0 cites Schema Registry entries for CS-2 and CS-3 by exact Schema ID label before authoring any expectation rows. CA-1.8 verifies CS-0 precedes CS-1. CS-0 sub-section naming "Schema ID: CS-2" and "Schema ID: CS-3" by exact label is D-3 evidence. | D-3 verifiability depends on CS-phase Registry acknowledgment only. D-1 and D-2 may independently pass or fail without affecting D-3 verification. |

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

*CS opens with CS-0 Registry acknowledgment before authoring any expectation content.*

### CS-0 — Schema Registry Acknowledgment (CS-authored, Phase 1)

CS echoes Schema Registry entries for CS-2 and CS-3 from Phase 0 before authoring expectation rows.

**Registry acknowledgment for CS-2:**
Schema ID: CS-2 — Sharing Rule Expectations.
SE-updatable columns as declared by CA in Phase 0 Schema Registry: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged: SE populates after SE-0/TABLE_4 analysis.
Expectation format confirmed: Rule Name | Trigger | Expected Access Granted | Intended for CS Role? |
Potential Overreach? | SE Cross-Reference | SE Confirmation. SE-updatable columns left blank.

**Registry acknowledgment for CS-3:**
Schema ID: CS-3 — Cross-Role Access Differential Expectations.
SE-updatable columns as declared by CA in Phase 0 Schema Registry: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged: SE populates after SE-1/SE-3 analysis.
Expectation format confirmed: Entity | Operation | CS Role Expected Access | Comparison Role |
Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation.
SE-updatable columns left blank.

### CS-1 — Expected Customer Service Access Baseline

For each entity: expected CRUD operations, expected record scope, sensitive fields needed and why.
Flag configurations that may inadvertently open access beyond job requirements.

**CS-2** *(Schema Registry CS-2; SE-updatable columns blank)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

For each Potential Overreach? YES: name access path and most likely over-reached role.

**CS-3** *(Schema Registry CS-3; SE-updatable columns blank)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

State at minimum one entity and one operation where CS has less access than Comparison Role.

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis (Privilege-Tier Descent Order)

*SE traces from highest-privilege tier to lowest. SE-0 establishes admin ceiling and TABLE_4 before
SE-1. TABLE_1 and TABLE_3 include Tier column. SE-2/SE-3/SE-4 use exact-label two-part closure
blocks per SHALL-G. SE-4 STRUCTURED CLOSE cites TABLE_4 SE-0 Sharing rules row by name per SHALL-H.*

### SE-0 — Admin-Tier Inventory and Escalation Vectors (executes before TABLE_1)

**Admin-tier inventory:** System Administrator, Environment Admin, admin-equivalent roles.
Record scope and key capabilities. Note any admin capability bypassing lower-tier controls (e.g.,
System Administrator bypasses column security profiles — document in defense-in-depth layer check).
This establishes the privilege ceiling for all lower-tier roles in SE-1.

**TABLE_4 — Escalation Vector Inventory** *(Schema Registry TABLE_4; SE-0 placement before SE-1;
rows are named SE-0 outputs available for cross-reference by subsequent sections)*

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Finding format: `[Role] -> [Mechanism] -> [Elevated access achieved]` for confirmed escalation;
"Checked [mechanism]: no path found because [specific reason]" for rule-out.
After TABLE_4: populate CS-2 SE Cross-Reference and SE Confirmation. CONTRADICTED triggers
CS-EXPECTATION-VIOLATED per SHALL-F.

### SE-1 / SHALL-A — Role-Operation Matrix

**TABLE_1 — Role-Operation Matrix** *(Schema Registry TABLE_1 with Tier column)*

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Ordered: Admin tier first, Custom tier second, Restricted tier last. After TABLE_1: populate
CS-3 SE Cross-Reference and SE Confirmation. CONTRADICTED rows trigger CS-EXPECTATION-VIOLATED
per SHALL-F.

**Cross-role differential analysis:** Compare CS role against at least one Admin-tier and one
Custom-tier role for same entity and operation. Cite SE-0 TABLE_4 row ID for any differential
attributable to admin-tier escalation vectors.

### SE-2 / SHALL-B — Field-Level Security Coverage

MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:
Column security profiles are not auditable from the security roles UI; administrators discover
missing FLS only after a data exposure event reveals that a sensitive field was readable or
writable by an unintended role.

STRUCTURED CLOSE:
TABLE_2 below enumerates every sensitive field in scope with explicit FLS status (Configured /
Not Configured), surfacing pre-event what the security roles UI conceals. All Not Configured
sensitive fields forwarded to TABLE_5 as MISSING-FLS gaps with Tier column.

**TABLE_2 — FLS Coverage** *(Schema Registry TABLE_2)*

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Categories: PII / Financial / Audit-Compliance / Other-Sensitive. Null case: "No column security
profiles active on {{topic}}. Sensitive fields identified: [list]. All in TABLE_5 as MISSING-FLS."
System Administrator bypasses column security profiles (SE-0 confirmed); document in
defense-in-depth layer check.

**Defense-in-depth layer check:** Identify enforcement layer for at least one sensitive field.
For Admin-tier roles, note the SE-0 bypass finding.

### SE-3 / SHALL-C — Record Access Scope

MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access produced by a security role
plus owner team membership plus OWD; spot-checking roles individually misses cross-role privilege
accumulation through team inheritance.

STRUCTURED CLOSE:
TABLE_3 below maps effective scope for every role by Tier, recording OWD baseline, scope modifier
from team or role depth, and resulting effective scope as a single traceable row, making
team-accumulated privilege visible and auditable at the tier it occurs.

**TABLE_3 — Record Scope by Role** *(Schema Registry TABLE_3 with Tier column)*

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role MUST appear, ordered by Tier. Roles where effective scope exceeds role-only
scope: flag CS-EXPECTATION-VIOLATED in TABLE_5 if CS-3 expected the unexpanded scope.
After TABLE_3: update CS-3 SE Confirmation.

### SE-4 / SHALL-D — Privilege Escalation Cross-Reference

MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing the sharing rules
that silently override them; a Private OWD combined with an active sharing rule can grant
effective org-wide access without appearing in any security roles UI view.

STRUCTURED CLOSE:
TABLE_4 (authored at SE-0, rows: Team inheritance / Sharing rules / Impersonation / Admin-role
override) evaluated all four escalation vectors. Cross-reference for this section: TABLE_4 SE-0
— Sharing rules row [cite "Sharing rules" by row name]. This section uses the TABLE_4 SE-0
Sharing rules row to construct the cross-tier differential summary: for the most privileged
Admin-tier role and the most restricted Restricted-tier role, identify the specific enforcement
layer where access diverges, citing the TABLE_4 SE-0 Sharing rules row by name. State whether
the divergence is expected and what sharing-rule interaction (if any) was confirmed or ruled out
at SE-0.

### SE-5 / SHALL-E — Security Gap Inventory

**TABLE_5 — Security Gap Inventory** *(Schema Registry TABLE_5 with Tier column)*

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
- Verification — TABLE_4 at SE-0 (before SE-1)? All four vectors? Checked? = YES? Findings or specific rule-outs? -> PASS / FAIL

**CA-1.5 — C-05 verification** *(Phase 0 M4 pre-assignment CA-1.5)*:
- Registry anchor — Schema ID TABLE_5 (with Tier): [#, Gap Type, Entity, Field or Rule, Role, Tier, Severity, Remediation] — blank cells prohibited globally.
- Preamble anchor — C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 — verifying...
- Verification — TABLE_5 present? Named gap? Tier column populated? Remediations exact? -> PASS / FAIL

**CA-1.6 — SHALL-F compliance** *(CS-EXPECTATION-VIOLATED three-field structure)*:
- Registry anchor — TABLE_5 CS-EXPECTATION-VIOLATED: [CS-Expected, SE-Actual, Delta] — all three fields required per SHALL-F.
- Preamble anchor — SHALL-F as authored by CA in Phase 0: three-field block mandatory; missing field = reopen.
- Verification — Each CS-EXPECTATION-VIOLATED row: CS-Expected populated? SE-Actual populated? Delta with exact configuration change? -> PASS / FAIL per row.

**CA-1.7 — SHALL-G compliance** *(exact-label two-part closure blocks)*:
- Registry anchor — CONTEXT exact labels: "Blind spot 1 — Post-incident FLS gap" (SE-2), "Blind spot 2 — Cumulative privilege blind spot" (SE-3), "Blind spot 3 — OWD-sharing-rule override gap" (SE-4).
- Preamble anchor — SHALL-G: `MANUAL GAP [<exact label>]:` character-for-character; paraphrase fails; CA-1.7 verifies.
- Verification — SE-2/SE-3/SE-4 each open with exact two-part block? -> PASS / FAIL per section.

**CA-1.8 — CS-0 acknowledgment + CS-2/CS-3 Schema Registry** *(C-29 + C-33)*:
- Registry anchor — Schema Registry declared CS-2 and CS-3 as named entries with SE-updatable columns and protocols co-located.
- Preamble anchor — CS-0 must cite both schema IDs by exact label before CS-1; SE-updatable columns must be filled by SE.
- Verification — CS-0 present? Cites CS-2 by exact Schema ID label? Cites CS-3? Lists SE-updatable columns? SE filled them? -> PASS / FAIL

**CA-1.9 — C-35 verification (SE-4 STRUCTURED CLOSE TABLE_4 SE-0 row cross-reference)** *(D-2 axis; distinct from CA-1.4 and CA-1.7)*:
- Registry anchor — Schema ID TABLE_4: Sharing rules row is a named SE-0 output (Vector = "Sharing rules") available as cross-reference target. TABLE_4 rows are authored at SE-0; subsequent sections may cite them by row name.
- Preamble anchor — SHALL-H as authored by CA in Phase 0: SE-4 STRUCTURED CLOSE MUST cite TABLE_4 SE-0 Sharing rules row by name or position label; generic prose reference fails. CA-1.9 audits STRUCTURED CLOSE content only — distinct from CA-1.4 (TABLE_4 placement before SE-1) and CA-1.7 (MANUAL GAP exact-label accuracy).
- Verification — SE-4 STRUCTURED CLOSE present? Cites TABLE_4 SE-0 Sharing rules row by name (not generic prose)? Citation traceable to a specific SE-0 row? -> PASS / FAIL

**CA Format Compliance Verdict — Phase 0 citation + R12 Tri-Dimensional Self-Evidence Attestation:**

Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0), Phase 0 by label.

[C-01..C-05: CA-1.1..CA-1.5 results. SHALL-F: CA-1.6. SHALL-G exact-label two-part block compliance: CA-1.7. CS-0 acknowledgment: CA-1.8. C-35 SE-4 STRUCTURED CLOSE cross-reference: CA-1.9. Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

**R12 Tri-Dimensional Self-Evidence Attestation (C-36):**
Each R12 dimension is attested by naming its specific evidence source in the output body above.
Evidence is self-attestable from the output text alone — prompt inspection not required.

| Dimension | ID | Output-Body Evidence Source | Self-Attestable? |
|-----------|----|-----------------------------|-----------------|
| Execution order | D-1 | Phase 0 section header in output; "Handing to PHASE 1 — CS" handoff string at Step 0.2 close; CA-1 rows labeled "(Phase 0 M4 pre-assignment CA-1.x)" as provenance strings | [ATTESTED / NOT ATTESTED] |
| Closure-note format | D-2 | SE-4 STRUCTURED CLOSE body text above cites "TABLE_4 SE-0 — Sharing rules row" by name (per SHALL-H); CA-1.9 row present in Phase 3 with D-2 axis label as distinct audit target | [ATTESTED / NOT ATTESTED] |
| CS self-reference | D-3 | CS-0 sub-section above names "Schema ID: CS-2" and "Schema ID: CS-3" by exact Registry label before CS-1 rows; CA-1.8 confirmed CS-0 precedes CS-1 | [ATTESTED / NOT ATTESTED] |

Overall tri-dimensional attestation: ATTESTED (all three D-1/D-2/D-3 self-attestable from output body) / PARTIAL / NOT ATTESTED.
