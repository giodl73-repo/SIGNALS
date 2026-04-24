# trace-permissions Variate — Round 14
**Date:** 2026-03-17
**Rubric:** v13 (C-01 through C-39, denominator 31)
**Target:** 31/31 — add C-37 (preamble A-N axis labels cited in attestation rows) to R13-V-05 base

**State entering Round 14:**

| Variation | v13 score | Notes |
|-----------|-----------|-------|
| R13-V-05 | 99.7 (30/31) | Passes all v12 criteria (28/28) + C-38 + C-39; fails C-37: attestation rows use "Dimension 1/2/3" labels (V-03 inheritance), not A-N preamble axis labels |
| R13-V-04 | 98.7 (27/31) | Fails C-37 (no C-36), C-38 (preamble anchor citation not confirmed), C-39 (Phase 3 mandate absent) |
| R13-V-02 | 98.7 (27/31) | Gains C-38; fails C-37 (no C-34 means no A-N labels), C-39 (Phase 3 mandate absent) |
| R13-V-01 | 98.4 (26/31) | No C-35 blocks C-38+C-39; no C-34+C-36 blocks C-37 |
| R13-V-03 | 98.4 (26/31) | Passes C-36 but no C-34, so no A-N labels; C-37 fails |

Path to 31/31: R13-V-05 base + update TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION to identify
each dimension by preamble axis row label (A-1/A-2/A-3 or equivalent). C-38 and C-39 already
satisfied. Only C-37 remains.

---

## Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Single-axis C-37 (numeric A-N): preamble axis declaration gains a Row ID column (A-1/A-2/A-3); attestation rows use A-N as primary identifier | R13-V-05 base. Minimal surgical change: preamble axis table adds "Row ID" as first column; attestation table changes "Dimension 1" rows to "A-1: Execution order (C-31)" etc. Non-interference statement updated to reference A-1/A-2/A-3. Hypothesis: 31/31 (adds C-37; all other criteria preserved). |
| V-02 | Single-axis C-37 (semantic axis IDs): preamble uses AXIS:EXE / AXIS:CNF / AXIS:CSR instead of A-N numbers; attestation rows carry those same semantic IDs | Tests whether C-37's "or equivalent" clause accepts semantic labels. Axis ID column values are AXIS:EXE, AXIS:CNF, AXIS:CSR in preamble; attestation row headers use same IDs. Non-interference statement references semantic IDs. Hypothesis: 31/31. |
| V-03 | C-37 + phrasing register (imperative numbered-step voice throughout) | Full R13-V-05 + C-37 A-N fix, with all instruction prose rewritten as numbered MUST imperatives. Tests whether register change disrupts any of the 31 criteria. Hypothesis: 31/31. |
| V-04 | C-37 + lifecycle emphasis (Phase 3 CA-1.N scope declaration table pre-listing all 9 rows) | R13-V-05 + C-37 A-N fix, with Phase 3 mandate gaining a pre-printed CA-1.N Scope Declaration table naming all 9 rows, their verification scopes, and CA-1.9's distinctness at the phase-mandate level. Strengthens C-39 signal without changing anything else. Hypothesis: 31/31. |
| V-05 | Full canonical C-37 integration (five-column preamble axis table + bi-directional attestation cross-link) | Preamble axis declaration gains a fifth column "Attestation Row Ref" pre-assigning each row's attestation label (A-1/A-2/A-3); attestation table adds a "Preamble Axis Ref" column that back-references the declaration row. Closes C-34->C-37 loop at the column level, making the loop auditable without semantic interpretation. Hypothesis: 31/31. |

---

## V-01 — Single-Axis C-37: A-N Row Labels in Preamble Axis Declaration and Attestation

**Axis:** C-37 — The preamble R12 STRUCTURAL AXIS DECLARATION gains a "Row ID" column with
values A-1, A-2, A-3 as the first column. The TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION table
in the CA terminal verdict changes its row identifiers from "Dimension 1/2/3" to
"A-1: Execution order (C-31)", "A-2: Closure-note format (C-32)", "A-3: CS self-reference (C-33)".
The non-interference statement is updated to reference A-1/A-2/A-3 by label. All other R13-V-05
architecture preserved unchanged.
**Hypothesis:** 31/31 (adds C-37; C-38 and C-39 preserved from R13-V-05 inheritance).

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
protocols; TABLE_4 schema note declares SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot requirement)
and the Criterion Enforcement Matrix preamble (Step 0.2: SHALL-A through SHALL-G with SHALL-D
extension sub-clause for C-35; M4 CA-1.1 through CA-1.9 pre-assigned; R12 Structural Axis
Declaration with A-1/A-2/A-3 Row IDs and non-interference statement). CA issues handoff to PHASE 1.

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
dimension by its preamble A-N Row ID with its specific output-body evidence source.

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
Checked? = YES, Finding = escalation path or specific rule-out (never blank).
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
exempts another. The non-interference contract is binding throughout execution.

| Row ID | R12 Criterion | Label | Structural Property Governed | CA Verification |
|--------|---------------|-------|------------------------------|-----------------|
| A-1 | C-31 | Execution order | SE-0 before SE-1; Tier in TABLE_1/TABLE_3; SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference naming a specific TABLE_4 vector row | CA-1.4 (SE-0 ordering) + CA-1.9 (SE-0 slot cross-ref) |
| A-2 | C-32 | Closure-note format | Exact-label two-part `MANUAL GAP [<exact label>]:` / `STRUCTURED CLOSE:` blocks at openings of SE-2, SE-3, and SE-4 | CA-1.7 |
| A-3 | C-33 | CS self-reference | CS-0 sub-section cites CS-2 and CS-3 schema IDs by exact label and lists SE-updatable columns before CS-1/CS-2/CS-3 | CA-1.8 |

**Non-interference statement:** A-1 governs SE section sequencing, TABLE column structure, and
SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot. A-2 governs the exact textual format of SE section
opening blocks (MANUAL GAP / STRUCTURED CLOSE). A-3 governs CS's Phase 1 opening sub-section
structure. No axis enforcement mechanism intersects with another's. Verifying CA-1.7 (A-2)
does not verify A-1 or A-3. Verifying CA-1.8 (A-3) does not verify A-1 or A-2. Verifying
CA-1.4+CA-1.9 (A-1) does not verify A-2 or A-3. Each axis requires independent satisfaction.
A model that treats two axes as jointly satisfying a single axis's obligation fails this contract.

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A: Complete TABLE_1 with Tier column. Every cell Granted/Denied/Conditional/N/A. Rows ordered by tier.
- SHALL-B: TABLE_2 lists all PII, Financial, and Audit-Compliance fields with explicit FLS status. Null case explicit. Gap? YES rows in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier and Effective Scope filled. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 at SE-0 (before SE-1), all four vectors, Checked? = YES. Rule-outs name specific mechanism and reason. **SHALL-D extension [C-35]:** Additionally, SE-4's STRUCTURED CLOSE block SHALL carry a TABLE_4 row cross-reference at the SE-0 slot naming a specific TABLE_4 vector row by exact vector label. CA-1.9 verifies this sub-clause obligation, distinct from CA-1.4 (which verifies SE-0 execution ordering).
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap case requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field Remediation block (CS-Expected, SE-Actual, Delta). Incomplete rows MUST be reopened. CA-1.6 verifies.
- SHALL-G: At the opening of SE-2, SE-3, and SE-4, closure MUST appear as a two-part labeled block — Line 1: `MANUAL GAP [<exact CONTEXT label>]:` where the label is character-for-character as written in the CONTEXT section above; Line 2: description of what manual audits miss; Line 3: `STRUCTURED CLOSE:`; Line 4: closing mechanism. Exact label required; paraphrase fails. CA-1.7 verifies the MANUAL GAP block. CA-1.9 separately verifies the TABLE_4 SE-0 slot cross-reference inside SE-4's STRUCTURED CLOSE — a distinct audit target.

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

*SE-0 establishes admin-tier ceiling and TABLE_4 before SE-1. A-1 (execution order) active:
TABLE_4 at SE-0, Tier columns in TABLE_1/TABLE_3, SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot
cross-reference. A-2 (closure-note format) active: exact-label two-part MANUAL GAP / STRUCTURED
CLOSE blocks at SE-2/SE-3/SE-4 per SHALL-G. A-3 (CS self-reference) confirmed: CS-0 Registry
acknowledgment completed in Phase 1.*

### SE-0 — Admin-Tier Inventory and Escalation Vectors (executes before TABLE_1)

**Admin-tier role inventory:** List System Administrator, Environment Admin, and admin-equivalent
roles with record scope and key capabilities. Note admin bypasses of lower-tier controls
(e.g., System Administrator bypasses column security profiles). Establishes privilege ceiling.

**TABLE_4 — Escalation Vector Inventory** *(Schema Registry TABLE_4; SE-0 placement per
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
After TABLE_2: update CS-3 SE Confirmation for any row where a sensitive field finding contradicts.

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
note to a concrete SE-0 finding. It is the subject of CA-1.9 verification (SHALL-D [C-35]
extension sub-clause); it is distinct from the MANUAL GAP block above (CA-1.7's scope) and
from TABLE_4's execution order at SE-0 (CA-1.4's scope).
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
labeled elements before the Verification line. Inline concatenation fails C-24. CA-1.9 verifies
SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference (completing SHALL-D [C-35] extension
sub-clause) — distinct from CA-1.4 (SE-0 ordering) and CA-1.7 (MANUAL GAP labels).*

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
- Note: CA-1.4 verifies SE-0 execution ordering only. SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot content is CA-1.9's scope (SHALL-D [C-35] extension).

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
- Note: CA-1.7 verifies the MANUAL GAP block format only. The TABLE_4 row cross-reference inside SE-4's STRUCTURED CLOSE is CA-1.9's scope.

**CA-1.8 — CS-2/CS-3 Schema Registry registration + CS-0 acknowledgment verification** *(A-3 / C-33)*:
- Registry anchor — Schema Registry declared CS-2 as named schema entry with SE-updatable columns SE Cross-Reference and SE Confirmation and SE-update protocol co-located. CS-3 same. PHASE 1 mandate requires CS-0 to acknowledge both schema IDs and list SE-updatable columns before CS-1/CS-2/CS-3.
- Preamble anchor — CS-2 and CS-3 are Schema Registry entries. CS-0 acknowledgment is a PHASE 1 structural requirement per Axis A-3 (C-33) of the R12 Structural Axis Declaration.
- Verification — CS-2 in Registry? CS-3 in Registry? CS-0 present before CS-1? CS-0 cites both schema IDs by exact label? CS-0 lists SE-updatable columns for both? SE populated SE-updatable columns? -> PASS / FAIL

**CA-1.9 — SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 slot** *(C-35; completing
SHALL-D [C-35] extension sub-clause pre-assigned Phase 0; distinct from CA-1.4 and CA-1.7)*:
- Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity]. Phase 0 Schema Registry declared: "SE-4's STRUCTURED CLOSE block SHALL carry a TABLE_4 row cross-reference at its SE-0 slot, naming a specific TABLE_4 vector row by its exact vector label."
- Preamble anchor — Completing SHALL-D [C-35] extension sub-clause as authored by CA in Phase 0: "CA-1.9 verifies SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 slot | SE-4 STRUCTURED CLOSE | Distinct from CA-1.4 (SE-0 ordering), CA-1.7 (MANUAL GAP labels)."
- Verification — SE-4's STRUCTURED CLOSE block begins with an SE-0 slot entry naming a specific TABLE_4 vector row by its exact vector label? That row was populated at SE-0 with Checked?=YES and a non-blank Finding? The cross-reference is inside the STRUCTURED CLOSE block (not in the MANUAL GAP block, not in TABLE_5)? -> PASS / FAIL
- Distinction confirmed: CA-1.4 verified TABLE_4 appeared at SE-0 before TABLE_1. CA-1.7 verified the MANUAL GAP exact-label blocks. CA-1.9 verifies the TABLE_4 row cross-reference inside SE-4's STRUCTURED CLOSE — a third non-overlapping audit target on SE-4.

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0),
R12 Structural Axis Declaration with A-1/A-2/A-3 Row IDs (Step 0.2, Phase 0), Phase 0 by label.
[CA-1.1 through CA-1.9 results. A-1 verified by CA-1.4+CA-1.9. A-2 verified by CA-1.7.
A-3 verified by CA-1.8. Non-interference contract: all three axes independently verified.
Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

**TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION (R12 axes, authored by CA in terminal verdict):**

This attestation extends C-22's phase-execution self-evidence to all three R12 structural axes
declared in the Phase 0 preamble. Each row is identified by its preamble axis Row ID (A-1/A-2/A-3),
closing the C-34->C-37 labeling loop: the A-N labels declared in the Phase 0 axis table are the
same A-N labels used here as row identifiers. Each evidence source is a section or table in this
output, verifiable by inspection without reading the prompt instructions.

| Row ID | Dimension (Preamble Ref) | Label | Specific Output-Body Evidence Source | Status |
|--------|--------------------------|-------|--------------------------------------|--------|
| A-1 | C-31 (Preamble Row A-1) | Execution order | Phase 2 output body: SE-0 section header precedes SE-1 section header; TABLE_4 appears in SE-0 before any TABLE_1 row; TABLE_1 and TABLE_3 contain Tier column; SE-4 STRUCTURED CLOSE contains SE-0 slot entry naming a specific TABLE_4 vector row by exact label (verified by CA-1.9). | CONFIRMED |
| A-2 | C-32 (Preamble Row A-2) | Closure-note format | Phase 2 output body: SE-2 opens with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:` followed by `STRUCTURED CLOSE:`; SE-3 opens with `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:` followed by `STRUCTURED CLOSE:`; SE-4 opens with `MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:` followed by `STRUCTURED CLOSE:`. Verified by CA-1.7. | CONFIRMED |
| A-3 | C-33 (Preamble Row A-3) | CS self-reference | Phase 1 output body: CS-0 sub-section appears before CS-1; CS-0 cites Schema ID CS-2 and Schema ID CS-3 by exact label; CS-0 lists SE Cross-Reference and SE Confirmation as SE-updatable columns for both. Verified by CA-1.8. | CONFIRMED |

All three axes are simultaneously active. Evidence sources are structurally independent:
A-1 evidence is in SE-0 and TABLE_1/TABLE_3 column structure and SE-4 STRUCTURED CLOSE SE-0 slot;
A-2 evidence is in SE-2/SE-3/SE-4 opening blocks; A-3 evidence is in CS-0. No axis evidence source
overlaps with another. This independence is the output-body manifestation of the non-interference
declaration in the Phase 0 R12 Structural Axis Declaration (Row IDs A-1/A-2/A-3).

---

## V-02 — Single-Axis C-37: Semantic Axis IDs in Preamble Declaration and Attestation

**Axis:** C-37 with semantic labels — the preamble axis declaration uses AXIS:EXE / AXIS:CNF /
AXIS:CSR as row identifiers instead of A-N numbers. The attestation rows carry those same semantic
IDs as primary row identifiers. Tests C-37's "or equivalent" clause: if the labeling scheme is
consistent between preamble declaration and terminal attestation, C-37 should pass regardless of
whether the labels are numeric (A-N) or semantic (AXIS:*). All other R13-V-05 architecture
preserved.
**Hypothesis:** 31/31 (C-37 satisfied via semantic label consistency).

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

*(Identical to V-01 — full Blind spot 1/2/3 text with exact labels preserved.)*

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
CA executes first. Authors the Schema Registry (Step 0.1: seven schemas) and the Criterion
Enforcement Matrix preamble (Step 0.2: SHALL-A through SHALL-G with SHALL-D [C-35] extension;
M4 CA-1.1 through CA-1.9 pre-assigned; R12 Structural Axis Declaration with semantic axis IDs
AXIS:EXE / AXIS:CNF / AXIS:CSR and non-interference statement). CA issues handoff to PHASE 1.

**PHASE 1 — CS (Customer Success):**
*(Identical to V-01 PHASE 1 mandate.)*

**PHASE 2 — SE (Security Engineer / Dataverse Security Expert):**
*(Identical to V-01 PHASE 2 mandate.)*

**PHASE 3 — CA-1 (CA Verification Pass):**
CA returns. Double-anchor reaffirmation per row. CA-1.8 verifies CS-0 precedes CS-1. CA-1.9
verifies SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference (distinct from CA-1.4 and
CA-1.7). Terminal verdict includes TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION naming each R12
axis by its preamble semantic Axis ID (AXIS:EXE, AXIS:CNF, AXIS:CSR) with specific output-body
evidence source.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

*(Identical to V-01 Step 0.1 — all seven schemas with identical column declarations, blank-cell
rules, TABLE_4 SE-0 slot note, and CS-2/CS-3 SE-update protocols.)*

**Schema ID: TABLE_1** — `Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` — Admin/Custom/Restricted, Admin first, blank-cell rule applies.

**Schema ID: TABLE_2** — `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?` — Configured/Not Configured; YES/NO.

**Schema ID: TABLE_3** — `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?` — Tier mirrors TABLE_1.

**Schema ID: TABLE_4** — `Vector | Checked? | Finding | Severity` — four vectors, Checked?=YES, TABLE_4 at SE-0. SE-4 STRUCTURED CLOSE SHALL carry TABLE_4 row cross-reference at SE-0 slot naming a specific vector by exact label. Subject of CA-1.9.

**Schema ID: TABLE_5** — `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation` — CS-EV rows: CS-Expected / SE-Actual / Delta.

**Schema ID: CS-2** — SE-updatable: SE Cross-Reference, SE Confirmation. Protocol: after SE-0/TABLE_4.

**Schema ID: CS-3** — SE-updatable: SE Cross-Reference, SE Confirmation. Protocol: after SE-1/SE-3.

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

*(C-01 through C-05 mechanism mapping table and supplementary CA-1.6 through CA-1.9 rows
identical to V-01 Step 0.2. SHALL obligations identical to V-01 including SHALL-D [C-35]
extension sub-clause. Only the R12 Structural Axis Declaration differs: uses semantic Axis IDs
instead of A-N numeric labels.)*

**Declared rule: M1, M2, M3 simultaneously active. M4 pre-assigned.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-0 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**Supplementary CA verification rows:** *(identical to V-01 — CA-1.6 through CA-1.9 with same scope and distinct-from assignments)*

**R12 STRUCTURAL AXIS DECLARATION (authored by CA, Phase 0) — semantic axis IDs:**

This output activates three R12 structural axes. These axes are orthogonal and non-interfering.
Each is identified by a semantic Axis ID that will be used as the row identifier in the terminal
attestation, closing the preamble-to-attestation labeling loop.

| Axis ID | R12 Criterion | Label | Structural Property Governed | CA Verification |
|---------|---------------|-------|------------------------------|-----------------|
| AXIS:EXE | C-31 | Execution order | SE-0 before SE-1; Tier in TABLE_1/TABLE_3; SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference naming a specific TABLE_4 vector row | CA-1.4 (SE-0 ordering) + CA-1.9 (SE-0 slot cross-ref) |
| AXIS:CNF | C-32 | Closure-note format | Exact-label two-part `MANUAL GAP [<exact label>]:` / `STRUCTURED CLOSE:` blocks at openings of SE-2, SE-3, and SE-4 | CA-1.7 |
| AXIS:CSR | C-33 | CS self-reference | CS-0 sub-section cites CS-2 and CS-3 schema IDs by exact label and lists SE-updatable columns before CS-1/CS-2/CS-3 | CA-1.8 |

**Non-interference statement:** AXIS:EXE governs SE section sequencing, TABLE column structure,
and SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot. AXIS:CNF governs the exact textual format of SE
section opening closure blocks. AXIS:CSR governs CS's Phase 1 opening sub-section structure.
No axis enforcement mechanism intersects with another's. Satisfying AXIS:EXE does not satisfy
or exempt AXIS:CNF or AXIS:CSR; the same applies to all pairings. Each axis requires independent
satisfaction. The Axis IDs (AXIS:EXE, AXIS:CNF, AXIS:CSR) declared here are used as row
identifiers in the terminal TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION.

**SHALL obligations:** *(identical to V-01 — SHALL-A through SHALL-G including SHALL-D [C-35] extension)*

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

*(Identical to V-01 PHASE 1 — CS-0 Registry acknowledgment for CS-2 and CS-3, CS-1 qualitative
baseline, CS-2 sharing rule expectations table, CS-3 cross-role differential table, handoff
to PHASE 2.)*

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis (Privilege-Tier Descent Order)

*(Identical to V-01 PHASE 2 — SE-0 through SE-5 with TABLE_4 at SE-0, Tier columns in
TABLE_1/TABLE_3, exact-label MANUAL GAP / STRUCTURED CLOSE blocks at SE-2/SE-3/SE-4, SE-4
STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference, TABLE_5 gap inventory.)*

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

*(CA-1.1 through CA-1.9 identical to V-01 — same Registry anchor, Preamble anchor, and
Verification paragraph structure for each row. CA-1.9 preamble anchor cites SHALL-D [C-35]
extension sub-clause. Distinction notes preserved. Only the CA Format Compliance Verdict and
TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION differ.)*

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0),
R12 Structural Axis Declaration with semantic Axis IDs AXIS:EXE/AXIS:CNF/AXIS:CSR (Step 0.2,
Phase 0), Phase 0 by label.
[CA-1.1 through CA-1.9 results. AXIS:EXE verified by CA-1.4+CA-1.9. AXIS:CNF verified by CA-1.7.
AXIS:CSR verified by CA-1.8. Non-interference contract: all three axes independently verified.
Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

**TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION (R12 axes, authored by CA in terminal verdict):**

Each row is identified by its preamble Axis ID (AXIS:EXE, AXIS:CNF, AXIS:CSR), closing the
preamble-to-attestation labeling loop under the semantic label scheme declared in Phase 0.

| Axis ID (Preamble Ref) | Criterion | Label | Specific Output-Body Evidence Source | Status |
|------------------------|-----------|-------|--------------------------------------|--------|
| AXIS:EXE | C-31 | Execution order | Phase 2 output body: SE-0 section header precedes SE-1 section header; TABLE_4 appears in SE-0 before any TABLE_1 row; TABLE_1 and TABLE_3 contain Tier column; SE-4 STRUCTURED CLOSE contains SE-0 slot entry naming a specific TABLE_4 vector row by exact label (verified by CA-1.9). | CONFIRMED |
| AXIS:CNF | C-32 | Closure-note format | Phase 2 output body: SE-2 opens with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:` followed by `STRUCTURED CLOSE:`; SE-3 with `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:`; SE-4 with `MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:`. Verified by CA-1.7. | CONFIRMED |
| AXIS:CSR | C-33 | CS self-reference | Phase 1 output body: CS-0 sub-section appears before CS-1; CS-0 cites Schema ID CS-2 and Schema ID CS-3 by exact label; CS-0 lists SE Cross-Reference and SE Confirmation as SE-updatable columns for both. Verified by CA-1.8. | CONFIRMED |

All three axes are simultaneously active and their evidence sources are structurally independent.
The semantic Axis IDs (AXIS:EXE, AXIS:CNF, AXIS:CSR) declared in the Phase 0 preamble are the
same identifiers used here, making the loop verifiable by ID match without semantic interpretation.

---

## V-03 — C-37 + Phrasing Register: Imperative Numbered-Step Voice

**Axis:** C-37 A-N label fix (from V-01) combined with imperative numbered-step register. All
instruction prose in Role Sequencing Mandate, Phase mandates, and sub-section instructions
rewritten as numbered MUST imperatives. Tests whether register changes affect structural criterion
compliance. All 31 criteria should be register-neutral.
**Hypothesis:** 31/31 (C-37 active via A-N labels; all other criteria preserved under imperative register).

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

*(Identical to V-01 — full Blind spot 1/2/3 exact-label text preserved.)*

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

**You MUST execute in four numbered phases. You MUST NOT begin a phase until the prior phase
is complete. Phase labels MUST appear as section headers in the output.**

1. **PHASE 0 — CA:** You MUST author the Schema Registry (seven schemas) and Criterion
Enforcement Matrix preamble (SHALL-A through SHALL-G with SHALL-D [C-35] extension; M4 CA-1.1
through CA-1.9 pre-assigned; R12 Structural Axis Declaration with A-1/A-2/A-3 Row IDs and
non-interference statement) before any other phase begins. You MUST issue a handoff string to
PHASE 1 at the end of PHASE 0.

2. **PHASE 1 — CS:** You MUST open with CS-0 (Schema Registry acknowledgment citing CS-2 and
CS-3 schema IDs and SE-updatable columns). You MUST produce CS-1, CS-2, CS-3 using Registry
schemas. You MUST NOT fill TABLE_1-5. You MUST issue a handoff string to PHASE 2.

3. **PHASE 2 — SE:** You MUST fill TABLE_4 at SE-0 (before SE-1) in privilege-tier descent
order. You MUST include Tier column in TABLE_1 and TABLE_3. You MUST open SE-2, SE-3, SE-4
with exact-label two-part closure blocks per SHALL-G. You MUST include a TABLE_4 row
cross-reference at the SE-0 slot of SE-4's STRUCTURED CLOSE. You MUST issue a handoff string
to PHASE 3.

4. **PHASE 3 — CA-1:** You MUST perform double-anchor reaffirmation for CA-1.1 through CA-1.9.
Each row MUST present the Registry anchor as a distinct labeled paragraph, the Preamble anchor
as a distinct labeled paragraph, and the Verification statement as a distinct labeled paragraph.
Inline concatenation MUST NOT occur. CA-1.9 MUST complete the SHALL-D [C-35] extension
sub-clause obligation and MUST be distinct from CA-1.4 and CA-1.7. The terminal verdict MUST
include a TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION table using A-1/A-2/A-3 as row identifiers.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

**Step 0.1 — Schema Registry instructions:**
1. You MUST declare all table schemas centrally before any analysis begins.
2. You MUST declare the blank-cell prohibition globally — individual tables MUST NOT restate it.
3. You MUST co-locate SE-update protocols with CS-2 and CS-3 schema entries.
4. TABLE_4 schema MUST include the SE-0 placement note and the SE-4 STRUCTURED CLOSE SE-0 slot
   requirement.

**Schema ID: TABLE_1 — Role-Operation Matrix**
Columns: `Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Tier values: Admin / Custom / Restricted. Admin rows first. Blank-cell rule: Granted/Denied/Conditional/N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Blank-cell rule: Configured/Not Configured; YES/NO.

**Schema ID: TABLE_3 — Record Scope by Role**
Columns: `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Tier mirrors TABLE_1. Blank-cell rule: Own/BU/Parent-Child BU/Org-wide/Team-scoped/Sharing-[rule].

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Columns: `Vector | Checked? | Finding | Severity`
Four vectors. Checked?=YES. TABLE_4 MUST execute at SE-0 before SE-1. SE-4's STRUCTURED CLOSE
block MUST carry a TABLE_4 row cross-reference at its SE-0 slot naming a specific vector by
exact label. CA-1.9 verifies this SE-0 slot — distinct from CA-1.4 and CA-1.7.

**Schema ID: TABLE_5 — Security Gap Inventory**
Columns: `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation`
CS-EV rows MUST carry three-field Remediation: CS-Expected / SE-Actual / Delta.

**Schema ID: CS-2** — SE-updatable: SE Cross-Reference, SE Confirmation. Protocol: after SE-0.
**Schema ID: CS-3** — SE-updatable: SE Cross-Reference, SE Confirmation. Protocol: after SE-1/SE-3.

**Step 0.2 — Enforcement Preamble instructions:**
1. You MUST declare M1+M2+M3 as simultaneously active. You MUST pre-assign M4 row IDs.
2. You MUST include the R12 Structural Axis Declaration table with Row IDs A-1/A-2/A-3.
3. You MUST include a non-interference statement referencing A-1, A-2, A-3 by label.
4. You MUST declare SHALL-A through SHALL-G including SHALL-D [C-35] extension sub-clause.

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
| CA-1.6 | SHALL-F CS-EV three-field structure | TABLE_5 CS-EV rows | — |
| CA-1.7 | SHALL-G exact-label MANUAL GAP blocks at SE-2/SE-3/SE-4 | SE-2, SE-3, SE-4 openings | CA-1.9 |
| CA-1.8 | CS-2/CS-3 Registry registration + CS-0 precedes CS-1 | Phase 1 CS-0 | — |
| CA-1.9 | SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference | SE-4 STRUCTURED CLOSE | CA-1.4 (SE-0 ordering), CA-1.7 (MANUAL GAP labels) |

**R12 STRUCTURAL AXIS DECLARATION (authored by CA, Phase 0):**

Three R12 structural axes are active. They are orthogonal. Each is assigned a Row ID (A-1/A-2/A-3)
that MUST be used as the row identifier in the terminal TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION.

| Row ID | R12 Criterion | Label | Structural Property Governed | CA Verification |
|--------|---------------|-------|------------------------------|-----------------|
| A-1 | C-31 | Execution order | SE-0 before SE-1; Tier in TABLE_1/TABLE_3; SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference | CA-1.4 + CA-1.9 |
| A-2 | C-32 | Closure-note format | Exact-label MANUAL GAP / STRUCTURED CLOSE two-part blocks at SE-2/SE-3/SE-4 | CA-1.7 |
| A-3 | C-33 | CS self-reference | CS-0 cites CS-2 and CS-3 schema IDs and SE-updatable columns before CS-1 | CA-1.8 |

**Non-interference statement:** A-1, A-2, and A-3 govern structurally distinct output elements.
Satisfying one axis MUST NOT be treated as satisfying any other. Each axis requires independent
satisfaction and independent CA verification.

**SHALL obligations:**
- SHALL-A: Complete TABLE_1 with Tier column. Every cell Granted/Denied/Conditional/N/A. Rows ordered by tier.
- SHALL-B: TABLE_2 lists all PII, Financial, and Audit-Compliance fields with explicit FLS status. Null case explicit. Gap? YES rows in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier and Effective Scope filled. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 at SE-0 (before SE-1), all four vectors, Checked?=YES. **SHALL-D extension [C-35]:** SE-4's STRUCTURED CLOSE block MUST carry a TABLE_4 row cross-reference at the SE-0 slot naming a specific TABLE_4 vector row by exact label. CA-1.9 verifies this extension, distinct from CA-1.4.
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap case requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field Remediation (CS-Expected/SE-Actual/Delta). CA-1.6 verifies.
- SHALL-G: SE-2/SE-3/SE-4 openings MUST use two-part exact-label blocks: `MANUAL GAP [<exact CONTEXT label>]:` then `STRUCTURED CLOSE:`. Exact = character-for-character. CA-1.7 verifies MANUAL GAP block; CA-1.9 verifies SE-4 STRUCTURED CLOSE SE-0 slot.

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

**CS-0 instructions:** You MUST open with CS-0. You MUST cite CS-2 and CS-3 schema IDs by
exact label. You MUST list SE-updatable columns for both. You MUST NOT author CS-1 before CS-0
is complete.

### CS-0 — Schema Registry Acknowledgment (CS-authored, Phase 1)

**Registry acknowledgment for CS-2:** Schema ID: CS-2 — Sharing Rule Expectations.
SE-updatable columns as declared by CA in Phase 0 Schema Registry: SE Cross-Reference,
SE Confirmation. Protocol: SE fills after SE-0/TABLE_4. Columns left blank by CS.

**Registry acknowledgment for CS-3:** Schema ID: CS-3 — Cross-Role Access Differential Expectations.
SE-updatable columns: SE Cross-Reference, SE Confirmation. Protocol: SE fills after SE-1/SE-3.
Columns left blank by CS.

### CS-1 — Expected Customer Service Access Baseline

For each entity in scope: (a) CRUD operations expected for normal CS job function; (b) expected
record scope; (c) sensitive fields CS needs and why. Identify configurations that may open access
beyond job requirements.

**CS-2** *(Schema Registry CS-2; SE-updatable blank)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

**CS-3** *(Schema Registry CS-3; SE-updatable blank)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis (Privilege-Tier Descent Order)

**SE execution instructions:**
1. You MUST fill TABLE_4 at SE-0 before populating TABLE_1.
2. You MUST include Tier column in TABLE_1 and TABLE_3.
3. You MUST open SE-2 with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:` then `STRUCTURED CLOSE:`.
4. You MUST open SE-3 with `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:` then `STRUCTURED CLOSE:`.
5. You MUST open SE-4 with `MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:` then `STRUCTURED CLOSE:`.
6. SE-4's STRUCTURED CLOSE MUST begin with the SE-0 slot naming a specific TABLE_4 vector row.

### SE-0 — Admin-Tier Inventory and Escalation Vectors (MUST execute before TABLE_1)

**Admin-tier inventory:** List System Administrator, Environment Admin, and admin-equivalent roles.
Note admin bypasses of lower-tier controls. This establishes the privilege ceiling for TABLE_1.

**TABLE_4** *(Schema Registry TABLE_4; SE-0 placement per SHALL-D and A-1)*:

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

After TABLE_4: populate CS-2 SE Cross-Reference and SE Confirmation. Enter CONTRADICTED rows
as CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

### SE-1 / SHALL-A — Role-Operation Matrix

**TABLE_1** *(Schema Registry TABLE_1 with Tier; blank-cell rule)*:

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Admin-tier rows first. After table: cross-reference CS-3. Compare CS role against one more
privileged role; state whether differential is expected.

### SE-2 / SHALL-B — Field-Level Security Coverage

MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:
Column security profiles are not auditable from the security roles UI; administrators discover
missing FLS only after a data exposure event reveals a sensitive field was readable by an
unintended role.

STRUCTURED CLOSE:
TABLE_2 enumerates every sensitive field with explicit FLS status. All Not Configured fields
are forwarded to TABLE_5 as MISSING-FLS.

**TABLE_2** *(Schema Registry TABLE_2; blank-cell rule)*:

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Null case: "No column security profiles active on {{topic}}." Defense-in-depth layer check:
identify enforcement layer for at least one sensitive field.

### SE-3 / SHALL-C — Record Access Scope

MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access produced by a security role
plus owner team membership plus OWD; spot-checking individual roles misses team-accumulated
privilege.

STRUCTURED CLOSE:
TABLE_3 maps effective scope for every role by Tier, making team-accumulated privilege visible.

**TABLE_3** *(Schema Registry TABLE_3 with Tier; blank-cell rule)*:

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role MUST appear, ordered by Tier. After TABLE_3: update CS-3 SE Confirmation.

### SE-4 / SHALL-D — Privilege Escalation Cross-Reference

MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing sharing rules that
silently override them; a Private OWD combined with an active sharing rule can grant effective
org-wide access without appearing in any security roles UI view.

STRUCTURED CLOSE:
SE-0 cross-reference: TABLE_4 row [cite exact vector label, Checked? value, and Finding from
SE-0 TABLE_4 for the vector most relevant to {{topic}}'s escalation surface]. This SE-0 slot
entry is the subject of CA-1.9 verification (SHALL-D [C-35] extension); it is distinct from
the MANUAL GAP block above (CA-1.7) and from TABLE_4's execution ordering (CA-1.4).
Cross-tier differential: for the most privileged Admin-tier role and most restricted
Restricted-tier role, identify the enforcement layer where access diverges, citing the TABLE_4
row named above. State whether the divergence is expected.

### SE-5 / SHALL-E — Security Gap Inventory

**TABLE_5** *(Schema Registry TABLE_5 with Tier; blank-cell rule)*:

| # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation |
|---|----------|--------|---------------|------|------|----------|-------------|

CS-EXPECTATION-VIOLATED rows: CS-Expected / SE-Actual / Delta.

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

**CA-1 execution instructions:**
1. You MUST present Registry anchor, Preamble anchor, and Verification as distinct labeled
   paragraphs within each CA-1 row. You MUST NOT concatenate them inline.
2. You MUST complete CA-1.1 through CA-1.9 in sequence.
3. CA-1.9 MUST complete the SHALL-D [C-35] extension sub-clause. Its preamble anchor MUST
   cite "SHALL-D [C-35] extension sub-clause" by name.
4. The terminal verdict TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION table MUST use A-1/A-2/A-3
   as row identifiers, matching the Row IDs declared in the Phase 0 R12 Structural Axis
   Declaration.

*(CA-1.1 through CA-1.9 — identical double-anchor structure to V-01, including SHALL-D [C-35]
extension citation in CA-1.9 preamble anchor and distinction notes. Only the terminal verdict
attestation table formatting differs in the imperative-register framing above.)*

**CA-1.1 — C-01 verification** *(Phase 0 M4 pre-assignment CA-1.1)*:
- Registry anchor — Schema ID TABLE_1 (with Tier): [Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope] — blank cells prohibited globally.
- Preamble anchor — C-01 as authored by CA in Phase 0: TABLE_1 / SE-1 / SHALL-A / CA-1.1 — verifying...
- Verification — TABLE_1 present? Tier column populated? Rows ordered by tier? All cells filled? -> PASS / FAIL

**CA-1.2 — C-02 verification** *(Phase 0 M4 pre-assignment CA-1.2)*:
- Registry anchor — Schema ID TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?] — blank cells prohibited globally.
- Preamble anchor — C-02 as authored by CA in Phase 0: TABLE_2 / SE-2 / SHALL-B / CA-1.2 — verifying...
- Verification — TABLE_2 present? FLS status explicit? Null case stated? Gap? YES in TABLE_5? -> PASS / FAIL

**CA-1.3 through CA-1.8** *(identical to V-01 — same Registry anchor, Preamble anchor,
Verification paragraph for C-03 through SHALL-G and CS-0 acknowledgment)*

**CA-1.9 — SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 slot** *(completing
SHALL-D [C-35] extension sub-clause; pre-assigned Phase 0; distinct from CA-1.4 and CA-1.7)*:
- Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity]. Phase 0 declared: "SE-4's STRUCTURED CLOSE block SHALL carry a TABLE_4 row cross-reference at its SE-0 slot naming a specific TABLE_4 vector row by exact vector label."
- Preamble anchor — Completing SHALL-D [C-35] extension sub-clause as authored by CA in Phase 0: CA-1.9 pre-assigned to verify SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot | distinct from CA-1.4 (SE-0 ordering) | distinct from CA-1.7 (MANUAL GAP labels).
- Verification — SE-4's STRUCTURED CLOSE begins with SE-0 slot entry naming a specific TABLE_4 vector row by exact label? That row has Checked?=YES and non-blank Finding? Cross-reference is inside STRUCTURED CLOSE (not MANUAL GAP, not TABLE_5)? -> PASS / FAIL

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0),
R12 Structural Axis Declaration with Row IDs A-1/A-2/A-3 (Step 0.2, Phase 0), Phase 0 by label.
[CA-1.1 through CA-1.9. A-1/CA-1.4+CA-1.9. A-2/CA-1.7. A-3/CA-1.8. Non-interference active.
Overall: COMPLIANT / NON-COMPLIANT.]

**TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION:**

*(Identical to V-01 attestation table — Row IDs A-1/A-2/A-3 as primary identifiers, preamble
back-reference, evidence sources, CONFIRMED status for all three rows.)*

| Row ID | Dimension (Preamble Ref) | Label | Specific Output-Body Evidence Source | Status |
|--------|--------------------------|-------|--------------------------------------|--------|
| A-1 | C-31 (Preamble Row A-1) | Execution order | SE-0 precedes SE-1 in Phase 2; TABLE_4 in SE-0 before TABLE_1; Tier in TABLE_1/TABLE_3; SE-4 STRUCTURED CLOSE SE-0 slot names specific TABLE_4 vector row (verified CA-1.9). | CONFIRMED |
| A-2 | C-32 (Preamble Row A-2) | Closure-note format | SE-2 `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:` + `STRUCTURED CLOSE:`; SE-3 `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:` + `STRUCTURED CLOSE:`; SE-4 `MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:` + `STRUCTURED CLOSE:`. Verified CA-1.7. | CONFIRMED |
| A-3 | C-33 (Preamble Row A-3) | CS self-reference | CS-0 in Phase 1 before CS-1; cites Schema ID CS-2 and Schema ID CS-3; lists SE-updatable columns. Verified CA-1.8. | CONFIRMED |

---

## V-04 — C-37 + Lifecycle Emphasis: Phase 3 CA-1.N Scope Declaration Table

**Axis:** C-37 A-N label fix (from V-01) combined with lifecycle emphasis on Phase 3. The Phase 3
mandate gains a pre-printed CA-1.N SCOPE DECLARATION table naming all 9 verification rows, their
scopes, and CA-1.9's distinctness from CA-1.4 and CA-1.7 at the phase-mandate level. This
strengthens C-39's requirement (phase-mandate block explicitly names CA-1.9 and declares
inter-row distinctness) without altering any other section. All other V-01 architecture preserved.
**Hypothesis:** 31/31 (C-37 active; C-39 signal strengthened; all other criteria preserved).

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

*(Identical to V-01 — full Blind spot 1/2/3 exact-label text.)*

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
SE-4 closes Blind spot 3.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins.

**PHASE 0 — CA (Compliance Auditor):**
CA executes first. Authors Schema Registry (Step 0.1: seven schemas) and Criterion Enforcement
Matrix preamble (Step 0.2: SHALL-A through SHALL-G with SHALL-D [C-35] extension; M4 CA-1.1
through CA-1.9 pre-assigned; R12 Structural Axis Declaration with A-1/A-2/A-3 Row IDs and
non-interference statement). Issues handoff to PHASE 1.

**PHASE 1 — CS (Customer Success):**
Executes second. Opens with CS-0 (Schema Registry acknowledgment). Produces CS-1, CS-2, CS-3.
Does not fill TABLE_1-5. Issues handoff to PHASE 2.

**PHASE 2 — SE (Security Engineer / Dataverse Security Expert):**
Executes third. SE-0 (TABLE_4) before SE-1. TABLE_1 and TABLE_3 include Tier. SE-2/SE-3/SE-4
use exact-label two-part closure blocks. SE-4 STRUCTURED CLOSE carries TABLE_4 SE-0 slot
cross-reference. Issues handoff to PHASE 3.

**PHASE 3 — CA-1 (CA Verification Pass):**
CA returns. Executes CA-1.1 through CA-1.9 in sequence. Each row uses double-anchor reaffirmation
(Registry anchor + Preamble anchor + Verification, each as a distinct labeled paragraph).

**CA-1.N SCOPE DECLARATION (Phase 3 pre-execution, authored by CA):**

Before executing any CA-1.N row, CA declares the scope of each verification row to make the
phase structure auditable from the phase boundary alone. Row scopes and inter-row distinctness
are stated here; entering individual rows is not required to verify this phase structure.

| Row ID | Verification Scope | Scope Target | Distinct from |
|--------|-------------------|--------------|---------------|
| CA-1.1 | C-01 TABLE_1 completeness | SE-1 | — |
| CA-1.2 | C-02 TABLE_2 completeness | SE-2 | — |
| CA-1.3 | C-03 TABLE_3 completeness | SE-0 + SE-3 | — |
| CA-1.4 | C-04 TABLE_4 SE-0 execution ordering | SE-0 placement | CA-1.9 |
| CA-1.5 | C-05 TABLE_5 completeness | SE-5 | — |
| CA-1.6 | SHALL-F CS-EXPECTATION-VIOLATED three-field structure | TABLE_5 CS-EV rows | — |
| CA-1.7 | SHALL-G exact-label MANUAL GAP two-part blocks | SE-2/SE-3/SE-4 openings | CA-1.9 |
| CA-1.8 | CS-2/CS-3 Registry registration + CS-0 precedes CS-1 | Phase 1 CS-0 | — |
| CA-1.9 | SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 slot (SHALL-D [C-35] extension) | SE-4 STRUCTURED CLOSE | CA-1.4 (SE-0 ordering), CA-1.7 (MANUAL GAP labels) |

**CA-1.9 inter-row distinctness (phase-mandate level):** CA-1.9 verifies the TABLE_4 row
cross-reference inside SE-4's STRUCTURED CLOSE block — a structural element distinct from the
two audit targets CA-1.4 and CA-1.7 also operate on SE-4. CA-1.4 verifies that TABLE_4 executes
at SE-0 before TABLE_1 (section ordering). CA-1.7 verifies that the MANUAL GAP exact-label block
appears at SE-4's opening (closure-note format). CA-1.9 verifies that SE-4's STRUCTURED CLOSE
block contains a TABLE_4 row cross-reference at the SE-0 slot (closing-block data anchor). These
are three non-overlapping audit targets on the same SE-4 section, each with an independent scope.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*(Identical to V-01 PHASE 0 — Schema Registry Step 0.1 with all seven schemas, and Step 0.2
with C-01 through C-05 mechanism table, supplementary CA-1.6 through CA-1.9 rows, R12
Structural Axis Declaration with Row IDs A-1/A-2/A-3, non-interference statement, and SHALL-A
through SHALL-G including SHALL-D [C-35] extension sub-clause.)*

**Schema ID: TABLE_1** — `Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` — Admin/Custom/Restricted, Admin first.

**Schema ID: TABLE_2** — `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`

**Schema ID: TABLE_3** — `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?`

**Schema ID: TABLE_4** — `Vector | Checked? | Finding | Severity` — four vectors, Checked?=YES, SE-0 placement. SE-4 STRUCTURED CLOSE MUST carry TABLE_4 SE-0 slot cross-reference. CA-1.9 pre-assigned.

**Schema ID: TABLE_5** — `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation` — CS-EV: CS-Expected / SE-Actual / Delta.

**Schema ID: CS-2** — SE-updatable: SE Cross-Reference, SE Confirmation. After SE-0.
**Schema ID: CS-3** — SE-updatable: SE Cross-Reference, SE Confirmation. After SE-1/SE-3.

**Criterion Enforcement Matrix Preamble:**

| Criterion | M1 | M2 | M3 | M4 |
|-----------|----|----|----|----|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-0+SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

Supplementary rows: CA-1.6 (SHALL-F) | CA-1.7 (SHALL-G MANUAL GAP, distinct from CA-1.9) | CA-1.8 (CS-0) | CA-1.9 (SE-4 STRUCTURED CLOSE SE-0 slot, distinct from CA-1.4 and CA-1.7)

**R12 STRUCTURAL AXIS DECLARATION:**

| Row ID | R12 Criterion | Label | Structural Property Governed | CA Verification |
|--------|---------------|-------|------------------------------|-----------------|
| A-1 | C-31 | Execution order | SE-0 before SE-1; Tier columns; SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot | CA-1.4 + CA-1.9 |
| A-2 | C-32 | Closure-note format | Exact-label MANUAL GAP / STRUCTURED CLOSE at SE-2/SE-3/SE-4 openings | CA-1.7 |
| A-3 | C-33 | CS self-reference | CS-0 cites CS-2/CS-3 schema IDs and SE-updatable columns before CS-1 | CA-1.8 |

Non-interference: A-1, A-2, A-3 govern structurally distinct output elements. Independent
satisfaction required. A-N Row IDs declared here are used as row identifiers in the Phase 3
terminal TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION.

**SHALL-A through SHALL-G** *(including SHALL-D [C-35] extension sub-clause — identical to V-01)*

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

*(Identical to V-01 PHASE 1.)*

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis (Privilege-Tier Descent Order)

*(Identical to V-01 PHASE 2 — SE-0 through SE-5 with all exact-label MANUAL GAP blocks,
TABLE_4 SE-0 slot cross-reference in SE-4 STRUCTURED CLOSE, and Tier columns.)*

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

*CA returns. CA-1.N SCOPE DECLARATION declared in Role Sequencing Mandate above establishes
all row scopes at the phase boundary. Refer to CA-1.N Scope Declaration for CA-1.9 inter-row
distinctness from CA-1.4 and CA-1.7. Each CA-1 row presents Registry anchor and Preamble anchor
as distinct labeled paragraphs before the Verification line.*

*(CA-1.1 through CA-1.9 — identical to V-01, including double-anchor structure, SHALL-D [C-35]
extension citation in CA-1.9 preamble anchor, and distinction notes.)*

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0),
R12 Structural Axis Declaration with Row IDs A-1/A-2/A-3 (Step 0.2, Phase 0), Phase 0 by label.
CA-1.N Scope Declaration declared in Phase 3 mandate confirms CA-1.9 distinctness at phase
boundary level.
[CA-1.1 through CA-1.9. A-1 verified CA-1.4+CA-1.9. A-2 verified CA-1.7. A-3 verified CA-1.8.
Non-interference contract: all three axes independently verified. Overall: COMPLIANT / NON-COMPLIANT.]

**TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION:**

*(Identical to V-01 attestation table — Row IDs A-1/A-2/A-3, preamble back-references,
evidence sources, CONFIRMED for all three rows.)*

| Row ID | Dimension (Preamble Ref) | Label | Specific Output-Body Evidence Source | Status |
|--------|--------------------------|-------|--------------------------------------|--------|
| A-1 | C-31 (Preamble Row A-1) | Execution order | Phase 2: SE-0 precedes SE-1; TABLE_4 in SE-0 before TABLE_1; Tier in TABLE_1/TABLE_3; SE-4 STRUCTURED CLOSE SE-0 slot names specific TABLE_4 vector row (CA-1.9). | CONFIRMED |
| A-2 | C-32 (Preamble Row A-2) | Closure-note format | Phase 2: SE-2 `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:` + `STRUCTURED CLOSE:`; SE-3 `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:` + `STRUCTURED CLOSE:`; SE-4 `MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:` + `STRUCTURED CLOSE:`. CA-1.7. | CONFIRMED |
| A-3 | C-33 (Preamble Row A-3) | CS self-reference | Phase 1: CS-0 before CS-1; cites Schema ID CS-2 and Schema ID CS-3; lists SE-updatable columns. CA-1.8. | CONFIRMED |

---

## V-05 — Full Canonical C-37: Five-Column Axis Table + Bi-Directional Attestation Cross-Link

**Axis:** Full canonical integration. The preamble axis declaration gains a fifth column
"Attestation Row Ref" that pre-assigns the attestation row label for each axis (A-1/A-2/A-3),
declaring the closed loop contract in the preamble itself. The TRI-DIMENSIONAL SELF-EVIDENCE
ATTESTATION table gains a "Preamble Row Ref" column that back-references the preamble axis
declaration row, completing the bidirectional cross-link. The non-interference statement
explicitly references the Attestation Row Ref assignments. This makes the C-34→C-37 labeling
loop auditable at the column level without semantic interpretation of row content.
**Hypothesis:** 31/31 (most explicit C-37 expression; all other criteria from V-01 preserved).

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

*(Identical to V-01 — full Blind spot 1/2/3 exact-label text.)*

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
Matrix preamble (Step 0.2: SHALL-A through SHALL-G with SHALL-D [C-35] extension; M4 CA-1.1
through CA-1.9 pre-assigned; R12 Structural Axis Declaration with five-column format including
A-1/A-2/A-3 Row IDs and Attestation Row Ref assignments; non-interference statement referencing
the closed A-N loop). Issues handoff to PHASE 1.

**PHASE 1 — CS (Customer Success):**
Executes second. Opens with CS-0 (Schema Registry acknowledgment). Produces CS-1, CS-2, CS-3.
Does not fill TABLE_1-5. Issues handoff to PHASE 2.

**PHASE 2 — SE (Security Engineer / Dataverse Security Expert):**
Executes third. SE-0 (TABLE_4) before SE-1. TABLE_1/TABLE_3 include Tier. SE-2/SE-3/SE-4 use
exact-label two-part closure blocks. SE-4 STRUCTURED CLOSE carries TABLE_4 SE-0 slot
cross-reference. Issues handoff to PHASE 3.

**PHASE 3 — CA-1 (CA Verification Pass):**
CA returns. Double-anchor reaffirmation per row. CA-1.9 verifies SE-4 STRUCTURED CLOSE TABLE_4
SE-0 slot cross-reference (completing SHALL-D [C-35] extension; distinct from CA-1.4 and CA-1.7).
Terminal verdict TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION uses A-1/A-2/A-3 as primary row IDs
and includes a Preamble Row Ref column back-referencing the Phase 0 axis declaration, completing
the bidirectional C-34→C-37 loop.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1 and 0.2 before any other phase begins.*

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

*(Identical to V-01 Step 0.1 — all seven schemas with same column declarations, blank-cell
rules, TABLE_4 SE-0 slot note, and CS-2/CS-3 SE-update protocols.)*

**Schema ID: TABLE_1** — `Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` — Admin/Custom/Restricted, Admin first.
**Schema ID: TABLE_2** — `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
**Schema ID: TABLE_3** — `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
**Schema ID: TABLE_4** — `Vector | Checked? | Finding | Severity` — SE-0 placement. SE-4 STRUCTURED CLOSE MUST carry TABLE_4 SE-0 slot cross-reference. CA-1.9 pre-assigned as distinct from CA-1.4 and CA-1.7.
**Schema ID: TABLE_5** — `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation` — CS-EV: CS-Expected / SE-Actual / Delta.
**Schema ID: CS-2** — SE-updatable: SE Cross-Reference, SE Confirmation. After SE-0.
**Schema ID: CS-3** — SE-updatable: SE Cross-Reference, SE Confirmation. After SE-1/SE-3.

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
| CA-1.6 | SHALL-F CS-EV three-field structure | TABLE_5 CS-EV rows | — |
| CA-1.7 | SHALL-G exact-label MANUAL GAP blocks | SE-2/SE-3/SE-4 openings | CA-1.9 |
| CA-1.8 | CS-2/CS-3 Registry registration + CS-0 precedes CS-1 | Phase 1 CS-0 | — |
| CA-1.9 | SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 slot (SHALL-D [C-35] extension) | SE-4 STRUCTURED CLOSE | CA-1.4, CA-1.7 |

**R12 STRUCTURAL AXIS DECLARATION (authored by CA, Phase 0) — five-column format with Attestation Row Ref:**

This output activates three R12 structural axes. Each axis is assigned a Row ID (A-1/A-2/A-3)
and a pre-assigned Attestation Row Ref that names the row identifier the terminal
TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION MUST use for that axis. The Attestation Row Ref
closes the C-34→C-37 labeling loop in the preamble: the attestation row IDs are pre-declared
here alongside the axis declarations, making the loop contract explicit before execution.

| Row ID | R12 Criterion | Label | Structural Property Governed | CA Verification | Attestation Row Ref |
|--------|---------------|-------|------------------------------|-----------------|---------------------|
| A-1 | C-31 | Execution order | SE-0 before SE-1; Tier in TABLE_1/TABLE_3; SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference naming a specific TABLE_4 vector row | CA-1.4 (SE-0 ordering) + CA-1.9 (SE-0 slot cross-ref) | ATTEST-A-1 |
| A-2 | C-32 | Closure-note format | Exact-label two-part `MANUAL GAP [<exact label>]:` / `STRUCTURED CLOSE:` blocks at openings of SE-2, SE-3, and SE-4 | CA-1.7 | ATTEST-A-2 |
| A-3 | C-33 | CS self-reference | CS-0 sub-section cites CS-2 and CS-3 schema IDs by exact label and lists SE-updatable columns before CS-1/CS-2/CS-3 | CA-1.8 | ATTEST-A-3 |

**Non-interference statement:** A-1, A-2, and A-3 govern structurally distinct output elements.
No axis enforcement mechanism intersects with another's. Each axis requires independent
satisfaction and independent CA verification. The Attestation Row Refs (ATTEST-A-1, ATTEST-A-2,
ATTEST-A-3) declared in this table are the mandatory row IDs for the terminal attestation;
the terminal attestation MUST use these refs as row primary identifiers, completing the loop
between this preamble declaration and the Phase 3 terminal verdict.

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A: Complete TABLE_1 with Tier column. Every cell Granted/Denied/Conditional/N/A. Rows ordered by tier.
- SHALL-B: TABLE_2 lists all PII, Financial, and Audit-Compliance fields with explicit FLS status. Null case explicit. Gap? YES rows in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier and Effective Scope filled. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 at SE-0 (before SE-1), all four vectors, Checked? = YES. Rule-outs name specific mechanism and reason. **SHALL-D extension [C-35]:** SE-4's STRUCTURED CLOSE block SHALL carry a TABLE_4 row cross-reference at the SE-0 slot naming a specific TABLE_4 vector row by exact vector label. CA-1.9 verifies this sub-clause obligation as pre-assigned above, distinct from CA-1.4 (SE-0 ordering).
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap case requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field Remediation block (CS-Expected, SE-Actual, Delta). CA-1.6 verifies.
- SHALL-G: SE-2/SE-3/SE-4 openings MUST use two-part exact-label blocks: `MANUAL GAP [<exact CONTEXT label>]:` then `STRUCTURED CLOSE:`. Exact = character-for-character. CA-1.7 verifies MANUAL GAP block; CA-1.9 verifies SE-4 STRUCTURED CLOSE SE-0 slot (these are distinct audit targets).

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

*(Identical to V-01 PHASE 1 — CS-0 Registry acknowledgment for CS-2 and CS-3, CS-1 baseline,
CS-2 and CS-3 tables, handoff to PHASE 2.)*

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis (Privilege-Tier Descent Order)

*(Identical to V-01 PHASE 2 — SE-0 through SE-5 with TABLE_4 at SE-0, Tier columns, exact-label
MANUAL GAP / STRUCTURED CLOSE blocks at SE-2/SE-3/SE-4, SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot
cross-reference, TABLE_5 gap inventory with CS-EV three-field structure.)*

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

*CA returns. Each CA-1 row presents Registry anchor, Preamble anchor, and Verification as
distinct labeled paragraphs. Inline concatenation fails C-24. CA-1.9 completes SHALL-D [C-35]
extension sub-clause, distinct from CA-1.4 and CA-1.7.*

*(CA-1.1 through CA-1.9 — identical to V-01, including double-anchor structure, SHALL-D [C-35]
extension citation in CA-1.9 preamble anchor, and all distinction notes.)*

**CA-1.1 — C-01 verification** *(Phase 0 M4 pre-assignment CA-1.1)*:
- Registry anchor — Schema ID TABLE_1 (with Tier): [Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope] — blank cells prohibited globally.
- Preamble anchor — C-01 as authored by CA in Phase 0: TABLE_1 / SE-1 / SHALL-A / CA-1.1 — verifying...
- Verification — TABLE_1 present? Tier column populated? Rows ordered by tier? All cells filled? -> PASS / FAIL

*(CA-1.2 through CA-1.8 — identical to V-01)*

**CA-1.9 — SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 slot** *(completing
SHALL-D [C-35] extension sub-clause; pre-assigned Phase 0; distinct from CA-1.4 and CA-1.7)*:
- Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity]. Phase 0 Schema Registry declared: "SE-4's STRUCTURED CLOSE block SHALL carry a TABLE_4 row cross-reference at its SE-0 slot naming a specific TABLE_4 vector row by its exact vector label." CA-1.9 was pre-assigned in Phase 0 supplementary rows as distinct from CA-1.4 and CA-1.7.
- Preamble anchor — Completing SHALL-D [C-35] extension sub-clause as authored by CA in Phase 0: CA-1.9 verifies SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot | SE-4 STRUCTURED CLOSE | Distinct from CA-1.4 (SE-0 ordering), CA-1.7 (MANUAL GAP labels). Pre-assigned Attestation Row Refs: preamble axis A-1 assigned ATTEST-A-1; terminal attestation MUST use ATTEST-A-1 for axis A-1.
- Verification — SE-4's STRUCTURED CLOSE begins with SE-0 slot entry naming a specific TABLE_4 vector row by exact label? That row has Checked?=YES and non-blank Finding? Cross-reference inside STRUCTURED CLOSE (not MANUAL GAP, not TABLE_5)? -> PASS / FAIL

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0),
R12 Structural Axis Declaration with Row IDs A-1/A-2/A-3 and Attestation Row Refs ATTEST-A-1/
ATTEST-A-2/ATTEST-A-3 (Step 0.2, Phase 0), Phase 0 by label.
[CA-1.1 through CA-1.9 results. A-1 verified CA-1.4+CA-1.9. A-2 verified CA-1.7. A-3 verified
CA-1.8. Non-interference contract: all three axes independently verified. Attestation Row Ref
loop: terminal attestation used ATTEST-A-1/ATTEST-A-2/ATTEST-A-3 as declared in preamble.
Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

**TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION (R12 axes, authored by CA in terminal verdict):**

Each row is identified by its pre-assigned Attestation Row Ref (ATTEST-A-1, ATTEST-A-2,
ATTEST-A-3) and carries a Preamble Row Ref column back-referencing the preamble axis
declaration row. Together these form the bidirectional C-34→C-37 loop: preamble row A-N
declares Attestation Row Ref ATTEST-A-N; attestation row ATTEST-A-N cites Preamble Row A-N.
The loop is closed at the column level and auditable by reference match without reading row content.

| Attestation Row Ref | Preamble Row Ref | Criterion | Label | Specific Output-Body Evidence Source | Status |
|---------------------|-----------------|-----------|-------|--------------------------------------|--------|
| ATTEST-A-1 | Preamble Row A-1 | C-31 | Execution order | Phase 2 output body: SE-0 section header precedes SE-1 section header; TABLE_4 appears in SE-0 before any TABLE_1 row; TABLE_1 and TABLE_3 contain Tier column; SE-4 STRUCTURED CLOSE contains SE-0 slot entry naming a specific TABLE_4 vector row by exact label (verified by CA-1.9). | CONFIRMED |
| ATTEST-A-2 | Preamble Row A-2 | C-32 | Closure-note format | Phase 2 output body: SE-2 opens with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:` followed by `STRUCTURED CLOSE:`; SE-3 opens with `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:` followed by `STRUCTURED CLOSE:`; SE-4 opens with `MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:` followed by `STRUCTURED CLOSE:`. Verified by CA-1.7. | CONFIRMED |
| ATTEST-A-3 | Preamble Row A-3 | C-33 | CS self-reference | Phase 1 output body: CS-0 sub-section appears before CS-1; CS-0 cites Schema ID CS-2 and Schema ID CS-3 by exact label; CS-0 lists SE Cross-Reference and SE Confirmation as SE-updatable columns for both schemas. Verified by CA-1.8. | CONFIRMED |

All three axes are simultaneously active. Evidence sources are structurally independent.
The bidirectional loop (preamble A-N declares ATTEST-A-N; attestation ATTEST-A-N cites
preamble A-N) makes the C-34→C-37 labeling contract auditable from the output body alone:
the preamble axis table and the terminal attestation table share the same A-N/ATTEST-A-N
label scheme, and any inconsistency between them would be immediately visible by column scan.
This is the output-body manifestation of the non-interference declaration's Attestation Row Ref
pre-assignments in the Phase 0 R12 Structural Axis Declaration.
