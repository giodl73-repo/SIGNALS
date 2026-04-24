obligations (authored by CA, Phase 0):**

- SHALL-A: Complete TABLE_1 with Tier column. Every cell Granted/Denied/Conditional/N/A. Rows ordered by tier.
- SHALL-B: TABLE_2 lists all PII, Financial, and Audit-Compliance fields with explicit FLS status. Null case explicit. Gap? YES rows in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier and Effective Scope filled. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 at SE-0 (before SE-1), all four vectors, Checked? = YES. Rule-outs name specific mechanism and reason.
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap case requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field Remediation block (CS-Expected, SE-Actual, Delta). Incomplete rows MUST be reopened. CA-1.6 verifies.
- SHALL-G: At the opening of SE-2, SE-3, and SE-4, closure MUST appear as a two-part labeled block — Line 1: `MANUAL GAP [<exact CONTEXT label>]:` where \<exact CONTEXT label\> is the label character-for-character as written in the CONTEXT section (e.g., "Blind spot 1 — Post-incident FLS gap" — not a paraphrase); Line 2: description of what manual audits miss; Line 3: `STRUCTURED CLOSE:`; Line 4: which table and mechanism closes it. Single-line annotation, blockquote format, TABLE_5 consolidation, or paraphrased label all fail SHALL-G. CA-1.7 verifies exact label carry-through.

**R12 Structural Axis Declaration (C-34 contract):**

The three Round 12 aspirational dimensions are orthogonal axes with independent structural targets
and no mutual interference:

- Axis 1 — Execution order (C-31): SE-0 runs before SE-1; TABLE_4 is filled at SE-0; TABLE_1 and
  TABLE_3 include a Tier column; SE-4 STRUCTURED CLOSE cites SE-0 TABLE_4 data in cross-tier
  differential. Governs SE section execution order and Tier column presence only.
- Axis 2 — Closure-note format (C-32): SE-2, SE-3, and SE-4 each open with a two-part labeled
  block beginning `MANUAL GAP [<exact CONTEXT label>]:` followed by `STRUCTURED CLOSE:`. Governs
  SE sub-section opening block format only.
- Axis 3 — CS self-reference (C-33): PHASE 1 opens with CS-0, which acknowledges CS-2 and CS-3
  by exact Schema Registry ID label and lists SE-updatable columns before CS-1. Governs CS phase
  opening structure only.

Non-interference declaration: Axis 1 does not condition or modify Axis 2 or Axis 3 requirements.
Axis 2 does not condition or modify Axis 1 or Axis 3 requirements. Axis 3 does not condition or
modify Axis 1 or Axis 2 requirements. All three axes are simultaneously active and independently
satisfiable; satisfying any one axis neither enables nor precludes satisfying either of the others.

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

**CS-2 — Sharing rule expectations** *(Schema Registry CS-2; SE-updatable columns blank; SE fills after SE-0/TABLE_4)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

For each Potential Overreach? YES: name the access path and the most likely over-reached role.

**CS-3 — Cross-role access differential** *(Schema Registry CS-3; SE-updatable columns blank; SE fills after SE-1/SE-3)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

State at minimum one entity and one operation where CS has less access than the Comparison Role.

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis (Privilege-Tier Descent Order)

*SE traces from highest-privilege tier to lowest. SE-0 establishes admin-tier ceiling and TABLE_4
before SE-1. TABLE_1 and TABLE_3 include Tier column. SE-2/SE-3/SE-4 use exact-label two-part
closure blocks per SHALL-G. SE-4 STRUCTURED CLOSE names TABLE_4 SE-0 row IDs T4-1 through T4-4.*

### SE-0 — Admin-Tier Inventory and Escalation Vectors (executes before TABLE_1)

**Admin-tier role inventory:** List System Administrator, Environment Admin, and any
admin-equivalent roles with record scope and key capabilities. Note any admin capability that
bypasses lower-tier controls (e.g., System Administrator bypasses column security profiles).
This establishes the privilege ceiling for all lower-tier roles in SE-1.

**TABLE_4 — Escalation Vector Inventory** *(Schema Registry TABLE_4; SE-0 row IDs T4-1 through
T4-4 pre-assigned in Schema Registry; TABLE_1 rows interpreted relative to this ceiling)*

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| T4-1: Team inheritance | YES | | |
| T4-2: Sharing rules | YES | | |
| T4-3: Impersonation (Act on Behalf Of) | YES | | |
| T4-4: Admin / environment role override | YES | | |

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
differential attributable to admin-tier escalation vectors.

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
TABLE_4 SE-0 rows T4-1 (Team inheritance), T4-2 (Sharing rules), T4-3 (Impersonation), and
T4-4 (Admin/environment role override) — all filled at SE-0 — evaluated all four escalation
vectors with sharing rules explicitly cross-referenced against OWD settings in the Finding
column. This section adds cross-tier differential summary: for the most privileged Admin-tier
role and the most restricted Restricted-tier role, identify the specific enforcement layer where
access diverges, citing SE-0 TABLE_4 row IDs (T4-2 for sharing-rule interaction, T4-4 for
admin-tier ceiling establishment) to attribute the divergence to specific escalation vector
outcomes. State whether the divergence is expected and what sharing-rule interaction (if any)
was confirmed or ruled out in SE-0 TABLE_4 row T4-2.

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
- Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity] — all four vectors T4-1 through T4-4, Checked? = YES.
- Preamble anchor — C-04 as authored by CA in Phase 0: TABLE_4 / SE-0 / SHALL-D / CA-1.4 — verifying...
- Verification — TABLE_4 at SE-0 (before SE-1)? All four vectors T4-1 through T4-4? Checked? = YES? Findings or specific rule-outs? -> PASS / FAIL

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
- Preamble anchor — SHALL-G as authored by CA in Phase 0: Line 1 MUST be `MANUAL GAP [<exact CONTEXT label>]:`; exact = character-for-character; paraphrase fails; single-line annotation fails.
- Verification — SE-2 opens with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:`? Followed by `STRUCTURED CLOSE:`? SE-3 opens with `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:`? SE-4 opens with `MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:`? -> PASS / FAIL per section.

**CA-1.8 — CS-2/CS-3 Schema Registry registration + CS-0 acknowledgment verification** *(C-29 + C-33)*:
- Registry anchor — Schema Registry declared CS-2 as a named schema entry with SE-updatable columns SE Cross-Reference and SE Confirmation and SE-update protocol co-located. Schema Registry declared CS-3 same. PHASE 1 mandate requires CS-0 sub-section to acknowledge both schema IDs and list SE-updatable columns before CS-1/CS-2/CS-3.
- Preamble anchor — CS-2 and CS-3 are Schema Registry entries alongside TABLE_1-5. CS-0 acknowledgment is a PHASE 1 structural requirement: CS cites both schema IDs and SE-updatable columns before authoring expectation rows.
- Verification — CS-2 in Schema Registry with SE-updatable column declarations? CS-3 same? CS-0 present before CS-1? CS-0 cites CS-2 schema ID by exact label? CS-0 cites CS-3 schema ID by exact label? CS-0 lists SE-updatable columns for both? SE populated SE-updatable columns per protocol? -> PASS / FAIL

**CA-1.9 — C-35 verification** *(SE-4 STRUCTURED CLOSE TABLE_4 SE-0 row cross-reference — distinct from CA-1.4 and CA-1.7)*:
- Registry anchor — Schema ID TABLE_4 SE-0 row IDs as declared in Phase 0 Schema Registry: T4-1 (Team inheritance), T4-2 (Sharing rules), T4-3 (Impersonation), T4-4 (Admin/environment role override) — all four filled at SE-0 before SE-1.
- Preamble anchor — TABLE_4 assigned to SE-0 in preamble row C-04: TABLE_4 / SE-0 / SHALL-D / CA-1.4. C-35 audit target is structurally distinct: SE-4's STRUCTURED CLOSE block must contain an explicit TABLE_4 row cross-reference naming SE-0 row IDs. This check is not subsumed by CA-1.4 (which verifies SE-0 ordering and vector completeness) or CA-1.7 (which verifies MANUAL GAP exact-label compliance); CA-1.9 verifies a third structural property of SE-4.
- Verification — SE-4 STRUCTURED CLOSE block contains explicit TABLE_4 row cross-reference naming SE-0 row IDs T4-1 through T4-4? Row IDs cited in the cross-tier differential attribution? Cross-reference structurally present as a distinct element not subsumed by CA-1.4 or CA-1.7 scope? -> PASS / FAIL

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0), Phase 0 by label.
[C-01 through C-05 with CA-1.1 through CA-1.5 results. SHALL-F (CA-1.6). SHALL-G exact-label two-part block compliance (CA-1.7). C-29 + C-33 CS-0 acknowledgment (CA-1.8). C-35 SE-4 STRUCTURED CLOSE TABLE_4 SE-0 row cross-reference (CA-1.9). R12 Structural Axis Declaration present in Step 0.2 preamble — C-34 satisfied. Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

**R12 Tri-Dimensional Self-Evidence Attestation (C-36 contract):**
- Dimension 1 — Execution order (C-31): Output-body evidence source = "SE-0 — Admin-Tier
  Inventory and Escalation Vectors" section header in document body precedes "SE-1" section
  header; TABLE_4 rows T4-1 through T4-4 appear under the SE-0 sub-section before any SE-1
  content; TABLE_1 Tier column populated with Admin / Custom / Restricted values; SE-4
  STRUCTURED CLOSE cites SE-0 TABLE_4 row IDs T4-1 through T4-4 in cross-tier differential.
- Dimension 2 — Closure-note format (C-32): Output-body evidence source = SE-2 section opens
  with two-part block `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:` followed by
  `STRUCTURED CLOSE:`; SE-3 opens with `MANUAL GAP [Blind spot 2 — Cumulative privilege blind
  spot]:` followed by `STRUCTURED CLOSE:`; SE-4 opens with `MANUAL GAP [Blind spot 3 —
  OWD-sharing-rule override gap]:` followed by `STRUCTURED CLOSE:`. CA-1.7 verified each
  exact label.
- Dimension 3 — CS self-reference (C-33): Output-body evidence source = CS-0 sub-section
  "Schema Registry Acknowledgment" in document body precedes CS-1 sub-section; CS-0 cites
  Schema Registry IDs "CS-2" and "CS-3" by exact label; CS-0 lists SE-updatable columns for
  both. CA-1.8 verified.

All three R12 dimensions are simultaneously self-evident from the output body without reference
to prompt instructions.

---

**Predicted scores under v12:**

| Variation | Predicted | C-34 | C-35 | C-36 | Notes |
|-----------|-----------|------|------|------|-------|
| V-01 | 26/28 | PASS | FAIL | FAIL | Axis declaration present; no T4 row IDs; no tri-dimensional verdict |
| V-02 | 26/28 | FAIL | PASS | FAIL | T4 row IDs + CA-1.9 present; no axis declaration; no tri-dimensional verdict |
| V-03 | 26/28 | FAIL | FAIL | PASS | Tri-dimensional verdict present; no axis declaration; no CA-1.9 |
| V-04 | 27/28 | PASS | PASS | FAIL | Axis declaration + T4 row IDs + CA-1.9; no tri-dimensional verdict |
| V-05 | 28/28 | PASS | PASS | PASS | All three R13 axes on R12-V-05 base — 100.0 candidate |
