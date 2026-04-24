# trace-permissions Variate — Round 16
**Date:** 2026-03-17
**Rubric:** v15 (proposed) — 36 criteria (C-01 through C-44), denominator 36
**Target:** 36/36 — add C-43 (labeled NON-OVERLAP DECLARATION block) and C-44 (Phase 0
bilateral mandate co-declaration) to R15-V-05 base (34/34 under v14)

**State entering Round 16:**

| Variation | v14 score | Notes |
|-----------|-----------|-------|
| R15-V-05 | 100.0 (34/34) | Full canonical: C-40 (bidirectional loop CA-1.10), C-41 (ATTEST-TBL in Registry), C-42 (Phase 0 Artifact Manifest + terminal manifest citation); no labeled NON-OVERLAP DECLARATION block in Phase 3 mandate; Phase 0 mandate does not co-name SHALL-D-EXT-C35 and SHALL-F-EXT-CS2CS3 as bilateral siblings |
| R15-V-04 | 99.4 (33/34) | Has C-40+C-41; no Artifact Manifest |
| R15-V-01/V-02/V-03 | 99.1 (31/34) | Single-axis innovations only |

**Path to 36/36:** R15-V-05 base + C-43 (labeled NON-OVERLAP DECLARATION block in Phase 3
mandate naming CA-1.4/CA-1.7/CA-1.9 by Row ID with scope summaries) + C-44 (Phase 0 ROLE
SEQUENCING MANDATE co-names SHALL-D-EXT-C35 SE-side and SHALL-F-EXT-CS2CS3 CS-side as sibling
sub-clauses with bilateral parity markers and CA-1.9/CA-1.6 verification row citations). Both axes
are independent; V-04 is the canonical combination.

---

## v14 -> v15 Rubric Extension

**2 new aspirational criteria. Denominator: 34 -> 36. Each aspirational = 10/36 ~= 0.278 pts.**

| ID | Hangs off | Pattern | What it tests |
|----|-----------|---------|---------------|
| C-43 | C-16+C-19+C-22 | R16-V-01 | Phase 3 ROLE SEQUENCING MANDATE carries a labeled NON-OVERLAP DECLARATION block (named structural header, not inline prose) immediately following the CA-1.N scope roster. The block enumerates CA-1.4 (SE-0 execution ordering), CA-1.7 (MANUAL GAP exact-label blocks at SE-2/SE-3/SE-4), and CA-1.9 (SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference) by Row ID and scope summary, making their non-overlap structurally verifiable from the block alone. A prose non-overlap note embedded inside a CA-1.N row annotation satisfies C-16 and C-22 but fails C-43; the labeled block is the distinct structural requirement. |
| C-44 | C-22+C-35+C-19 | R16-V-02 | Phase 0 ROLE SEQUENCING MANDATE co-names SHALL-D-EXT-C35 (SE-side) and SHALL-F-EXT-CS2CS3 (CS-side) as explicit bilateral sibling sub-clauses within the Phase 0 mandate description. Each sibling carries: (a) sub-clause ID, (b) side qualifier (SE-side / CS-side), (c) structural obligation description, (d) CA verification row citation (CA-1.9 / CA-1.6). An output where both sub-clauses exist in the SHALL obligations text and both verification rows are pre-assigned, but the Phase 0 mandate description does not co-name them with bilateral parity markers and side qualifiers, fails this criterion. |

**R15-V-05 re-scored under v15:**

| Criterion | v14 | v15 verdict | Why it moves |
|-----------|-----|-------------|--------------|
| C-43 | -- (new) | FAIL | Non-overlap of CA-1.4/CA-1.7/CA-1.9 asserted only in CA-1.4/CA-1.7/CA-1.9 note annotations inside Phase 3 rows; no labeled NON-OVERLAP DECLARATION block appears in Phase 3 mandate or Phase 3 body |
| C-44 | -- (new) | FAIL | SHALL-F names three-field Remediation obligation; CA-1.6 is pre-assigned; but Phase 0 ROLE SEQUENCING MANDATE paragraph does not co-name SHALL-D-EXT-C35 and SHALL-F-EXT-CS2CS3 as bilateral siblings with SE-side/CS-side markers and CA-1.9/CA-1.6 citations |
| R15-V-05 composite | 100.0 (34/34) | **98.9 (34/36)** | 2 x 0.278 = 0.56 pts lost |

---

## Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Single-axis C-43: labeled NON-OVERLAP DECLARATION block added to Phase 3 mandate + body | R15-V-05 base. Phase 3 ROLE SEQUENCING MANDATE text adds "followed by labeled NON-OVERLAP DECLARATION block". Phase 3 body gains NON-OVERLAP DECLARATION block after CA-1.10 naming CA-1.4/CA-1.7/CA-1.9 by Row ID and scope. Hypothesis: 35/36 (C-44 remains open). |
| V-02 | Single-axis C-44: Phase 0 bilateral mandate co-declaration + SHALL-F-EXT-CS2CS3 explicit naming | R15-V-05 base. Phase 0 ROLE SEQUENCING MANDATE Phase 0 paragraph co-names SHALL-D-EXT-C35 (SE-side, CA-1.9) and SHALL-F-EXT-CS2CS3 (CS-side, CA-1.6) as bilateral siblings. SHALL-F obligation text gains explicit sub-clause label SHALL-F-EXT-CS2CS3. CA-1.6 preamble-anchor cites SHALL-F-EXT-CS2CS3 by name. Hypothesis: 35/36 (C-43 remains open). |
| V-03 | Single-axis C-43 (table variant): NON-OVERLAP DECLARATION block as table with Row ID / Scope / Distinct-From columns | V-01 axis but the NON-OVERLAP DECLARATION block uses a three-column table instead of a bulleted list. Tests whether tabular structure is structurally equivalent or superior to list form for C-43. All other V-01 changes identical. Hypothesis: 35/36. |
| V-04 | Combined C-43 + C-44 | R15-V-05 base + V-01 NON-OVERLAP DECLARATION block + V-02 bilateral mandate co-declaration. Canonical path to 36/36. Hypothesis: 36/36 (100.0). |
| V-05 | Definitive compound: C-43 + C-44 + Phase 3 bilateral echo + NON-OVERLAP bracket annotations | V-04 base plus: Phase 3 mandate names CA-1.9 (SE-side, SHALL-D-EXT-C35) and CA-1.6 (CS-side, SHALL-F-EXT-CS2CS3) as bilateral verification siblings (foreshadowing C-45); NON-OVERLAP DECLARATION block entries carry inline bracket annotations summarizing scope (foreshadowing C-46). Expected: 36/36. Architecture maximally reinforced to surface C-45/C-46 if new criteria emerge. |

---

## V-01 -- Single-Axis C-43: Labeled NON-OVERLAP DECLARATION Block

**Axis:** C-43 -- Phase 3 ROLE SEQUENCING MANDATE gains "followed by labeled NON-OVERLAP
DECLARATION block" in the CA-1 mandate description. Phase 3 body gains a NON-OVERLAP DECLARATION
block (labeled structural header, not inline prose) after CA-1.10, before the terminal verdict.
The block enumerates CA-1.4, CA-1.7, and CA-1.9 by Row ID with scope summaries. All other R15-V-05
architecture preserved unchanged.
**Hypothesis:** 35/36 (adds C-43; C-44 remains open -- Phase 0 mandate does not co-name
SHALL-D-EXT-C35 / SHALL-F-EXT-CS2CS3 as bilateral siblings).

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

Manual security reviews of Dataverse environments routinely miss three failure scenarios this trace
is designed to surface:

**Blind spot 1 -- Post-incident FLS gap.** Column security profiles are rarely audited proactively.
Sensitive fields -- credit limits, compensation data, SSNs, contact identifiers -- remain readable
and writable by any role unless a column security profile explicitly restricts them. The security
roles UI does not surface which fields lack column security profiles; gaps are discovered after data
exposure, not before.

**Blind spot 2 -- Cumulative privilege blind spot.** A user holding a BU-scoped security role who
also belongs to an owner team whose team role grants org-wide access has effective org-wide access.
No single Dataverse UI view surfaces the combined effective access produced by role + team + OWD
combination. Spot-checking individual roles misses cross-role accumulation through team membership.

**Blind spot 3 -- OWD-sharing-rule override gap.** Administrators check OWD settings
entity-by-entity without evaluating the sharing rules that silently override those baselines. A
Private OWD on Case combined with a Power Automate-triggered sharing rule grants effective
org-wide read to users who satisfy the trigger condition -- including low-trust service accounts
not intended to have broad case access.

This trace closes all three blind spots: SE-2 closes Blind spot 1; SE-3 closes Blind spot 2;
SE-4 closes Blind spot 3. Closure notes are exact-label two-part blocks co-located at each SE
sub-section opening, carrying the exact blind-spot label from this CONTEXT section.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins. Execution order is self-attestable from phase labels alone.

**PHASE 0 -- CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1: eight schemas -- TABLE_1 through TABLE_5
with Tier columns on TABLE_1 and TABLE_3; CS-2 and CS-3 with SE-updatable columns and update
protocols; TABLE_4 schema note declares SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot requirement;
ATTEST-TBL declaring TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION table schema with Preamble Row Ref
back-column) and the Criterion Enforcement Matrix preamble (Step 0.2: SHALL-A through SHALL-G with
SHALL-D extension sub-clause for C-35 and SHALL-F three-field Remediation obligation; M4 CA-1.1
through CA-1.10 pre-assigned; R12 Structural Axis Declaration with A-1/A-2/A-3 Row IDs, Attestation
Row Ref column (ATTEST-A-1/A-2/A-3), non-interference statement, and bidirectional loop binding).
Closes Phase 0 with Step 0.3 Phase 0 Artifact Manifest before handoff. CA issues handoff to PHASE 1.

**PHASE 1 -- CS (Customer Success):**
Executes second. Opens with CS-0 sub-section (Schema Registry acknowledgment: cites CS-2 and CS-3
schema IDs by exact label; lists SE-updatable columns; confirms SE-update protocol). Then produces
CS-1 (access baseline), CS-2 (sharing rule expectations), CS-3 (cross-role differential
expectations). CS does not populate TABLE_1 through TABLE_5. Issues handoff to PHASE 2.

**PHASE 2 -- SE (Security Engineer / Dataverse Security Expert):**
Executes third in privilege-tier descent order. SE-0 (admin-tier inventory + TABLE_4) before SE-1.
TABLE_1 and TABLE_3 include Tier column. SE-2, SE-3, SE-4 open with exact-label two-part closure
blocks per SHALL-G. SE-4 STRUCTURED CLOSE carries TABLE_4 row cross-reference at SE-0 slot naming
a specific TABLE_4 vector row by exact vector label. SE populates SE-updatable columns in CS-2 and
CS-3. Issues handoff to PHASE 3.

**PHASE 3 -- CA-1 (CA Verification Pass):**
CA returns. Phase 3 mandate carries complete CA-1.N audit-target scope roster followed by labeled
NON-OVERLAP DECLARATION block (named structural header; not inline prose). Each CA-1 row performs
double-anchor reaffirmation (Registry anchor labeled, Preamble anchor labeled, Verification
statement following both). CA-1.9 verifies SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference
(distinct from CA-1.4 and CA-1.7). CA-1.10 verifies bidirectional label-identity cross-scan.
Terminal verdict includes TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION with ATTEST-A-N Row IDs and
Preamble Row Ref back-column.

---

## PHASE 0 -- CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1, 0.2, and 0.3 before any other phase begins.*

### Step 0.1 -- Schema Registry (CA-authored, Phase 0)

**All table schemas declared centrally by CA. Blank-cell prohibition is global -- individual
tables do not restate it. SE-update protocols for CS-2 and CS-3 declared co-located with schema.**

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
Blank-cell rule: all four vectors (team inheritance, sharing rules, impersonation, admin/env roles),
Checked? = YES, Finding = escalation path or specific rule-out (never blank).
Note: TABLE_4 executes at SE-0 before SE-1. Additionally, SE-4's STRUCTURED CLOSE block SHALL
carry a TABLE_4 row cross-reference at its SE-0 slot: the SE-0 slot names a specific TABLE_4
vector row by its exact vector label. This SE-0 slot cross-reference is the subject of CA-1.9
verification, distinct from CA-1.4 (SE-0 execution ordering) and CA-1.7 (MANUAL GAP blocks).

**Schema ID: TABLE_5 -- Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation`
Blank-cell rule: Remediation = exact configuration object + exact path + expected post-fix state.
CS-EXPECTATION-VIOLATED Remediation (three-field block per SHALL-F):
- CS-Expected: cite CS-2 or CS-3 row ID; state expectation verbatim or by row reference.
- SE-Actual: SE finding that contradicts the expectation.
- Delta: exact configuration change to align SE-Actual to CS-Expected.

**Schema ID: CS-2 -- Sharing Rule Expectations**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference (TABLE_4 row ID); SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE update protocol: SE populates after TABLE_4 at SE-0. CONTRADICTED triggers CS-EXPECTATION-VIOLATED
in TABLE_5 per SHALL-F.

**Schema ID: CS-3 -- Cross-Role Access Differential Expectations**
Declared columns: `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference (TABLE_1 or TABLE_3 row ID); SE Confirmation.
SE update protocol: SE populates after TABLE_1/TABLE_3 analysis. CONTRADICTED triggers
CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

**Schema ID: ATTEST-TBL -- TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION**
Declared columns: `Row ID | R12 Dimension | Axis Label | Specific Output-Body Evidence Source | Preamble Row Ref | Status`
Blank-cell rule: all cells must carry explicit values. Preamble Row Ref back-references each
ATTEST-A-N row to its corresponding A-N row in the R12 Structural Axis Declaration.

### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: M1, M2, M3, M4 are simultaneously active -- not alternative coverage paths. M4
CA verification row IDs pre-assigned by CA constitute pre-existing contract obligations fulfilled
as structural completions in Phase 3.**

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
| CA-1.6 | SHALL-F CS-EXPECTATION-VIOLATED three-field Remediation structure | TABLE_5 CS-EV rows | CA-1.9 |
| CA-1.7 | SHALL-G exact-label MANUAL GAP two-part blocks at SE-2/SE-3/SE-4 | SE-2, SE-3, SE-4 openings | CA-1.9 |
| CA-1.8 | CS-2/CS-3 Schema Registry registration + CS-0 acknowledgment precedes CS-1 | Phase 1 CS-0 sub-section | -- |
| CA-1.9 | SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference at SE-0 slot | SE-4 STRUCTURED CLOSE block, SE-0 slot only | CA-1.4 (SE-0 ordering), CA-1.7 (MANUAL GAP labels) |
| CA-1.10 | Label-identity cross-scan: preamble Attestation Row Ref (A-N) matches attestation Preamble Row Ref (ATTEST-A-N) | R12 Axis Declaration col 6 + ATTEST-TBL Preamble Row Ref col | CA-1.4, CA-1.7, CA-1.9 |

**R12 STRUCTURAL AXIS DECLARATION (authored by CA, Phase 0):**

This output activates three R12 structural dimensions. These dimensions are orthogonal: each
governs a structurally distinct property, and activating one neither enables nor exempts another.
The non-interference contract is binding throughout execution.

| Row ID | R12 Criterion | Label | Structural Property Governed | CA Verification | Attestation Row Ref |
|--------|---------------|-------|------------------------------|-----------------|---------------------|
| A-1 | C-31 | Execution order | SE-0 before SE-1; Tier in TABLE_1/TABLE_3; SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference naming a specific TABLE_4 vector row | CA-1.4 (SE-0 ordering) + CA-1.9 (SE-0 slot cross-ref) | ATTEST-A-1 |
| A-2 | C-32 | Closure-note format | Exact-label two-part `MANUAL GAP [<exact label>]:` / `STRUCTURED CLOSE:` blocks at SE-2, SE-3, SE-4 openings | CA-1.7 | ATTEST-A-2 |
| A-3 | C-33 | CS self-reference | CS-0 cites CS-2 and CS-3 schema IDs by exact label and lists SE-updatable columns before CS-1/CS-2/CS-3 | CA-1.8 | ATTEST-A-3 |

**Non-interference statement:** A-1 governs SE section sequencing and TABLE Tier column structure
and SE-4 STRUCTURED CLOSE SE-0 slot. A-2 governs exact textual format of SE opening blocks. A-3
governs CS Phase 1 opening sub-section structure. No axis enforcement mechanism intersects another.
Verifying CA-1.7 (A-2) does not verify A-1 or A-3. Verifying CA-1.8 (A-3) does not verify A-1 or
A-2. Verifying CA-1.4+CA-1.9 (A-1) does not verify A-2 or A-3. Each axis requires independent
satisfaction.

**Bidirectional loop binding (C-40):** Attestation Row Ref column above pre-declares the attestation
table row label for each A-N row. CA-1.10 verifies label identity by cross-scan: for each A-N row,
preamble Attestation Row Ref = ATTEST-A-N and attestation row ATTEST-A-N Preamble Row Ref = A-N.

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A: Complete TABLE_1 with Tier column. Every cell Granted/Denied/Conditional/N/A. Rows
  ordered Admin first, Custom second, Restricted last.
- SHALL-B: TABLE_2 lists all PII, Financial, and Audit-Compliance fields with explicit FLS status.
  Null case explicit. All Gap? YES rows forwarded to TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Tier and Effective Scope filled. Ambiguous scope
  in TABLE_5.
- SHALL-D: TABLE_4 at SE-0 before SE-1, all four vectors, Checked? = YES. Rule-outs name specific
  mechanism and reason. **Extension sub-clause [C-35]:** SE-4's STRUCTURED CLOSE block SHALL carry
  a TABLE_4 row cross-reference at the SE-0 slot naming a specific TABLE_4 vector row by exact
  vector label. CA-1.9 verifies this sub-clause; distinct from CA-1.4 (SE-0 ordering).
- SHALL-E: TABLE_5 has at least one named gap with specific field, role, or rule. Zero-gap case
  requires explicit evidence rows confirming what was checked.
- SHALL-F: When any CS-2 or CS-3 expectation conflicts with an SE finding, the conflict MUST be
  recorded in TABLE_5 as CS-EXPECTATION-VIOLATED. Each such row MUST carry all three Remediation
  fields (CS-Expected, SE-Actual, Delta). A row missing any field MUST be reopened. CA-1.6 verifies.
- SHALL-G: At the opening of SE-2, SE-3, and SE-4, a two-part labeled block MUST appear. Line 1:
  `MANUAL GAP [<exact CONTEXT label>]:` (character-for-character from CONTEXT; paraphrase fails).
  Line 2: description of what manual audits miss. Line 3: `STRUCTURED CLOSE:`. Line 4: closing
  mechanism. CA-1.7 verifies MANUAL GAP block format. CA-1.9 separately verifies TABLE_4 SE-0 slot
  cross-reference inside SE-4's STRUCTURED CLOSE.

### Step 0.3 -- Phase 0 Artifact Manifest (CA-authored, Phase 0)

**Phase 0 Artifact Manifest -- all structural artifacts declared by CA in this phase:**

(a) Schema IDs registered in Step 0.1 (8 total):
TABLE_1, TABLE_2, TABLE_3, TABLE_4, TABLE_5, CS-2, CS-3, ATTEST-TBL

(b) Preamble criterion rows by C-NN ID (5 total):
C-01, C-02, C-03, C-04, C-05

(c) SHALL obligations by letter (7 total):
SHALL-A, SHALL-B, SHALL-C, SHALL-D (with [C-35] extension), SHALL-E, SHALL-F, SHALL-G

(d) Supplementary CA-1.N verification row IDs (5 total):
CA-1.6, CA-1.7, CA-1.8, CA-1.9, CA-1.10

(e) R12 Axis Declaration row IDs (3 total):
A-1, A-2, A-3

Terminal verdict in Phase 3 SHALL cite this manifest by item counts per category confirming all
declared artifacts were exercised.

*Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Schema Registry Acknowledgment + Access Baseline

*CS opens with CS-0 Registry acknowledgment before authoring any expectation content.*

### CS-0 -- Schema Registry Acknowledgment (CS-authored, Phase 1)

CS echoes the Schema Registry entries for CS-2 and CS-3 declared by CA in Phase 0.

**Registry acknowledgment for CS-2:**
Schema ID: CS-2 -- Sharing Rule Expectations.
SE-updatable columns as declared by CA: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged: SE populates after TABLE_4 at SE-0.
Expectation format confirmed. SE-updatable columns left blank by CS.

**Registry acknowledgment for CS-3:**
Schema ID: CS-3 -- Cross-Role Access Differential Expectations.
SE-updatable columns as declared by CA: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged: SE populates after TABLE_1/TABLE_3 analysis.
SE-updatable columns left blank by CS.

### CS-1 -- Expected Customer Service Access Baseline

For each entity in scope: (a) CRUD operations the CS role is expected to perform for normal job
function; (b) expected record scope (own-records or BU); (c) sensitive fields CS needs and why.
Flag any configurations that may inadvertently open access beyond job requirements.

**CS-2 -- Sharing rule expectations** *(Schema Registry CS-2; SE-updatable columns blank)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

For each Potential Overreach? YES: name the access path and the most likely over-reached role.

**CS-3 -- Cross-role access differential** *(Schema Registry CS-3; SE-updatable columns blank)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|------------------------|---------------------|-----------------|

At minimum one entity and one operation where CS has less access than the Comparison Role.

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis (Privilege-Tier Descent Order)

*SE-0 establishes admin-tier ceiling and TABLE_4 before SE-1. A-1 active. A-2 active. A-3
confirmed by CS-0 in Phase 1.*

### SE-0 / SHALL-D -- Escalation Vector Inventory (executes before TABLE_1)

**Admin-tier role inventory:** List System Administrator, Environment Admin, and admin-equivalent
roles. Note admin bypasses of lower-tier controls. Establishes privilege ceiling.

**TABLE_4 -- Escalation Vector Inventory** *(Schema Registry TABLE_4; SE-0 placement per SHALL-D)*

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

After TABLE_4: populate SE Cross-Reference and SE Confirmation in CS-2. CONTRADICTED entries
trigger CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

### SE-1 / SHALL-A -- Role-Operation Matrix

**TABLE_1 -- Role-Operation Matrix** *(Schema Registry TABLE_1 with Tier)*

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Admin-tier rows first. Include every role with any privilege on any entity in {{topic}}.
After TABLE_1: populate SE Cross-Reference and SE Confirmation in CS-3. Cross-role differential:
compare CS role against one more privileged role; state whether differential is expected.

### SE-2 / SHALL-B -- Field-Level Security Coverage

MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:
Column security profiles are not auditable from the security roles UI; administrators discover
missing FLS only after a data exposure event reveals a sensitive field was readable by an unintended
role.

STRUCTURED CLOSE:
TABLE_2 below enumerates every sensitive field with explicit FLS status, surfacing pre-event what
the security roles UI conceals. All Not Configured sensitive fields forwarded to TABLE_5 as
MISSING-FLS gaps.

**TABLE_2 -- FLS Coverage** *(Schema Registry TABLE_2)*

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Categories: PII / Financial / Audit-Compliance / Other-Sensitive. Null case: explicitly state
"No column security profiles active on {{topic}}." After TABLE_2: update CS-3 SE Confirmation for
any sensitive field finding that contradicts a CS-3 expectation.

### SE-3 / SHALL-C -- Record Access Scope

MANUAL GAP [Blind spot 2 -- Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access produced by security role plus
owner team membership plus OWD; spot-checking individual roles misses team-accumulated privilege.

STRUCTURED CLOSE:
TABLE_3 below maps effective scope for every role by Tier, recording OWD baseline, scope modifier,
and resulting effective scope, making team-accumulated privilege visible and auditable.

**TABLE_3 -- Record Scope by Role** *(Schema Registry TABLE_3 with Tier)*

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role MUST appear, ordered by Tier. Roles where effective scope exceeds role-only
scope due to team membership are CS-EXPECTATION-VIOLATED candidates. After TABLE_3: update CS-3.

### SE-4 / SHALL-D -- Privilege Escalation Cross-Reference

MANUAL GAP [Blind spot 3 -- OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing sharing rules that
silently override them; a Private OWD combined with an active sharing rule can grant effective
org-wide access without appearing in any security roles UI view.

STRUCTURED CLOSE:
SE-0 cross-reference: TABLE_4 row [name the specific TABLE_4 vector row most relevant to
{{topic}}'s primary escalation surface -- cite exact vector label (e.g., "Team inheritance" or
"Sharing rules"), Checked? value, and the full Finding from SE-0 TABLE_4]. This TABLE_4 row
cross-reference occupies the SE-0 slot of this STRUCTURED CLOSE block and is the subject of
CA-1.9 verification (SHALL-D [C-35] extension sub-clause); distinct from the MANUAL GAP block
above (CA-1.7 scope) and from TABLE_4's execution order at SE-0 (CA-1.4 scope).
TABLE_4 evaluated all four escalation vectors simultaneously. This section adds the cross-tier
differential: for the most privileged Admin-tier role and the most restricted Restricted-tier role,
identify the specific Dataverse enforcement layer where access diverges, citing the TABLE_4 row
named in the SE-0 slot above. State whether the divergence is expected.

### SE-5 / SHALL-E -- Security Gap Inventory

**TABLE_5 -- Security Gap Inventory** *(Schema Registry TABLE_5)*

| # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation |
|---|----------|--------|---------------|------|------|----------|-------------|

Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED /
CS-EXPECTATION-VIOLATED. Severity: CRITICAL / HIGH / MEDIUM.

CS-EXPECTATION-VIOLATED rows (three-field Remediation block per SHALL-F):
- CS-Expected: [cite CS-2 or CS-3 row ID; state expectation verbatim or by row reference]
- SE-Actual: [SE finding that contradicts the expectation]
- Delta: [exact configuration change to align SE-Actual to CS-Expected]

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

**CA-1.N audit-target scope roster:**
CA-1.1 (C-01/TABLE_1), CA-1.2 (C-02/TABLE_2), CA-1.3 (C-03/TABLE_3), CA-1.4 (C-04/TABLE_4
SE-0 ordering), CA-1.5 (C-05/TABLE_5), CA-1.6 (SHALL-F CS-EV three-field structure), CA-1.7
(SHALL-G MANUAL GAP exact labels), CA-1.8 (CS-0 CS-2/CS-3 acknowledgment), CA-1.9 (SE-4
STRUCTURED CLOSE TABLE_4 SE-0 slot -- distinct from CA-1.4 and CA-1.7), CA-1.10 (bidirectional
label-identity cross-scan).

**NON-OVERLAP DECLARATION:**
The following three CA-1 rows have non-overlapping audit scopes. Each verifies a structurally
distinct sub-obligation; no two rows verify the same output artifact:

- CA-1.4 [Scope: SE-0 execution ordering -- verifies TABLE_4 appears at SE-0 before TABLE_1]
- CA-1.7 [Scope: MANUAL GAP exact-label blocks -- verifies character-for-character labels at
  SE-2, SE-3, SE-4 openings; does not verify SE-0 position or SE-4 STRUCTURED CLOSE content]
- CA-1.9 [Scope: SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot -- verifies the cross-reference
  inside SE-4's STRUCTURED CLOSE block; does not verify TABLE_4 execution order (CA-1.4) or
  MANUAL GAP label format (CA-1.7)]

*Each CA-1 row presents Registry anchor and Preamble anchor as structurally distinct labeled
elements before the Verification line.*

**CA-1.1 -- C-01 verification** *(Phase 0 M4 pre-assignment CA-1.1)*:
- Registry anchor -- Schema ID TABLE_1 (with Tier): [Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope] -- blank cells prohibited globally.
- Preamble anchor -- C-01 as authored by CA in Phase 0: TABLE_1 / SE-1 / SHALL-A / CA-1.1 -- verifying...
- Verification -- TABLE_1 present? Tier column populated? Rows ordered by tier? All cells filled? -> PASS / FAIL

**CA-1.2 -- C-02 verification** *(Phase 0 M4 pre-assignment CA-1.2)*:
- Registry anchor -- Schema ID TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?] -- blank cells prohibited globally.
- Preamble anchor -- C-02 as authored by CA in Phase 0: TABLE_2 / SE-2 / SHALL-B / CA-1.2 -- verifying...
- Verification -- TABLE_2 present? All sensitive fields listed? FLS status explicit? Null case stated? Gap? YES rows in TABLE_5? -> PASS / FAIL

**CA-1.3 -- C-03 verification** *(Phase 0 M4 pre-assignment CA-1.3)*:
- Registry anchor -- Schema ID TABLE_3 (with Tier): [Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Verified?] -- blank cells prohibited globally.
- Preamble anchor -- C-03 as authored by CA in Phase 0: TABLE_3 / SE-0+SE-3 / SHALL-C / CA-1.3 -- verifying...
- Verification -- Every TABLE_1 role in TABLE_3? Tier column populated? Effective Scope filled? Ambiguous scope in TABLE_5? -> PASS / FAIL

**CA-1.4 -- C-04 verification** *(Phase 0 M4 pre-assignment CA-1.4)*:
- Registry anchor -- Schema ID TABLE_4: [Vector, Checked?, Finding, Severity] -- all four vectors, Checked? = YES.
- Preamble anchor -- C-04 as authored by CA in Phase 0: TABLE_4 / SE-0 / SHALL-D / CA-1.4 -- verifying...
- Verification -- TABLE_4 at SE-0 before SE-1? All four vectors present? Findings or specific rule-outs? -> PASS / FAIL
- Note (NON-OVERLAP): CA-1.4 verifies SE-0 execution ordering only. SE-4 STRUCTURED CLOSE SE-0 slot content is CA-1.9's scope (SHALL-D [C-35] extension).

**CA-1.5 -- C-05 verification** *(Phase 0 M4 pre-assignment CA-1.5)*:
- Registry anchor -- Schema ID TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Tier, Severity, Remediation] -- blank cells prohibited globally.
- Preamble anchor -- C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 -- verifying...
- Verification -- TABLE_5 present? Named gap with specific field/role/rule? Tier column populated? Remediations exact? -> PASS / FAIL

**CA-1.6 -- SHALL-F compliance verification** *(CS-EXPECTATION-VIOLATED three-field structure)*:
- Registry anchor -- Schema ID TABLE_5 CS-EXPECTATION-VIOLATED row structure: [CS-Expected, SE-Actual, Delta] -- all three fields required per SHALL-F.
- Preamble anchor -- SHALL-F as authored by CA in Phase 0: three-field Remediation block mandatory; rows missing any field MUST be reopened. CA-1.6 verifies.
- Verification -- For each CS-EXPECTATION-VIOLATED row: CS-Expected populated (cites CS-2 or CS-3 row)? SE-Actual populated? Delta populated with exact configuration change? -> PASS / FAIL per row.

**CA-1.7 -- SHALL-G compliance verification** *(exact-label MANUAL GAP two-part closure blocks)*:
- Registry anchor -- CONTEXT section declared exact labels: "Blind spot 1 -- Post-incident FLS gap" (SE-2), "Blind spot 2 -- Cumulative privilege blind spot" (SE-3), "Blind spot 3 -- OWD-sharing-rule override gap" (SE-4). SHALL-G requires two-part blocks with character-for-character label.
- Preamble anchor -- SHALL-G as authored by CA: Line 1 `MANUAL GAP [<exact label>]:`; paraphrase fails. CA-1.7 verifies. Distinct from CA-1.9.
- Verification -- SE-2 opens with `MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:`? Followed by `STRUCTURED CLOSE:`? SE-3/SE-4 same pattern with exact labels? -> PASS / FAIL per section.
- Note (NON-OVERLAP): CA-1.7 verifies MANUAL GAP block format only. TABLE_4 row cross-reference inside SE-4's STRUCTURED CLOSE is CA-1.9's scope.

**CA-1.8 -- CS-2/CS-3 Schema Registry registration + CS-0 acknowledgment** *(A-3 / C-33)*:
- Registry anchor -- Schema Registry declared CS-2 and CS-3 as named schema entries with SE-updatable columns and SE-update protocols co-located. PHASE 1 mandate requires CS-0 to acknowledge both schema IDs before CS-1.
- Preamble anchor -- CS-2 and CS-3 are Schema Registry entries. CS-0 acknowledgment is a PHASE 1 structural requirement per Axis A-3 (C-33) of the R12 Structural Axis Declaration.
- Verification -- CS-2 in Registry? CS-3 in Registry? CS-0 present before CS-1? CS-0 cites both schema IDs by exact label? CS-0 lists SE-updatable columns for both? SE populated SE-updatable columns? -> PASS / FAIL

**CA-1.9 -- SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference** *(C-35; completing
SHALL-D [C-35] extension sub-clause; distinct from CA-1.4 and CA-1.7)*:
- Registry anchor -- Schema ID TABLE_4 with Phase 0 SE-0 slot declaration: "SE-4's STRUCTURED CLOSE block SHALL carry a TABLE_4 row cross-reference at its SE-0 slot, naming a specific TABLE_4 vector row by its exact vector label."
- Preamble anchor -- Completing SHALL-D [C-35] extension sub-clause as authored by CA: CA-1.9 pre-assigned to verify SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot | SE-4 STRUCTURED CLOSE block only | Distinct from CA-1.4 (SE-0 ordering) and CA-1.7 (MANUAL GAP labels).
- Verification -- SE-4's STRUCTURED CLOSE block begins with an SE-0 slot entry naming a specific TABLE_4 vector row by its exact vector label? That row was populated at SE-0? The cross-reference is inside STRUCTURED CLOSE (not in MANUAL GAP block, not in TABLE_5)? -> PASS / FAIL
- Distinction confirmed (NON-OVERLAP): CA-1.4 verified TABLE_4 appeared at SE-0 before TABLE_1. CA-1.7 verified MANUAL GAP exact-label blocks. CA-1.9 verifies the TABLE_4 row cross-reference inside SE-4's STRUCTURED CLOSE -- a third non-overlapping audit target.

**CA-1.10 -- Bidirectional loop label-identity cross-scan** *(Phase 0 pre-assignment CA-1.10)*:
- Registry anchor -- Schema ID ATTEST-TBL: [Row ID, R12 Dimension, Axis Label, Specific Output-Body Evidence Source, Preamble Row Ref, Status]. R12 Axis Declaration col 6 "Attestation Row Ref": A-1 -> ATTEST-A-1; A-2 -> ATTEST-A-2; A-3 -> ATTEST-A-3.
- Preamble anchor -- CA-1.10 pre-assigned (supplementary rows, Phase 0): label-identity cross-scan between preamble Attestation Row Ref column and ATTEST-TBL Preamble Row Ref column | Distinct from CA-1.4, CA-1.7, CA-1.9.
- Verification -- Cross-scan per row:
  - A-1: preamble Attestation Row Ref = ATTEST-A-1; ATTEST-A-1 Preamble Row Ref = A-1. Consistent? -> PASS / FAIL
  - A-2: preamble Attestation Row Ref = ATTEST-A-2; ATTEST-A-2 Preamble Row Ref = A-2. Consistent? -> PASS / FAIL
  - A-3: preamble Attestation Row Ref = ATTEST-A-3; ATTEST-A-3 Preamble Row Ref = A-3. Consistent? -> PASS / FAIL
  - Overall loop integrity: all three label pairs consistent? -> PASS / FAIL

**CA Format Compliance Verdict:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0, 8 schema IDs), CA-authored preamble
(Step 0.2, Phase 0, 5 criterion rows, 7 SHALL obligations, 5 supplementary CA-1.N rows),
R12 Structural Axis Declaration (Step 0.2, Phase 0, 3 A-N rows), Phase 0 Artifact Manifest
(Step 0.3, Phase 0: 8 schemas / 5 criterion rows / 7 SHALLs / 5 supplementary rows / 3 A-N rows
-- all declared artifacts exercised).
[CA-1.1 through CA-1.10 results. A-1 verified by CA-1.4+CA-1.9. A-2 verified by CA-1.7. A-3
verified by CA-1.8. Bidirectional loop verified by CA-1.10. Non-interference contract: all three
axes independently verified. Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to role.]

**TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION** *(Schema Registry ATTEST-TBL; CA-authored)*:

| Row ID | R12 Dimension | Axis Label | Specific Output-Body Evidence Source | Preamble Row Ref | Status |
|--------|---------------|------------|--------------------------------------|-----------------|--------|
| ATTEST-A-1 | C-31 (Preamble Row A-1) | Execution order | Phase 2 output body: SE-0 section header precedes SE-1; TABLE_4 appears in SE-0 before TABLE_1; TABLE_1 and TABLE_3 contain Tier column; SE-4 STRUCTURED CLOSE contains SE-0 slot entry naming a specific TABLE_4 vector row by exact label (CA-1.9). | A-1 | CONFIRMED |
| ATTEST-A-2 | C-32 (Preamble Row A-2) | Closure-note format | Phase 2 output body: SE-2 opens with `MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:` followed by `STRUCTURED CLOSE:`; SE-3 and SE-4 same pattern with exact labels from CONTEXT. Verified by CA-1.7. | A-2 | CONFIRMED |
| ATTEST-A-3 | C-33 (Preamble Row A-3) | CS self-reference | Phase 1 output body: CS-0 sub-section before CS-1; CS-0 cites Schema ID CS-2 and Schema ID CS-3 by exact label; CS-0 lists SE Cross-Reference and SE Confirmation as SE-updatable columns. Verified by CA-1.8. | A-3 | CONFIRMED |

All three axes simultaneously active. Preamble Row Ref column back-references each ATTEST-A-N row
to its A-N declaration in Phase 0. CA-1.10 confirmed label identity by cross-scan. Non-interference:
A-1 evidence in SE-0/TABLE_1/TABLE_3/SE-4 STRUCTURED CLOSE; A-2 evidence in SE-2/SE-3/SE-4
opening blocks; A-3 evidence in CS-0. No evidence source overlaps.

---

## V-02 -- Single-Axis C-44: Phase 0 Bilateral Mandate Co-Declaration

**Axis:** C-44 -- Phase 0 ROLE SEQUENCING MANDATE Phase 0 paragraph co-names SHALL-D-EXT-C35
(SE-side, verified at CA-1.9) and SHALL-F-EXT-CS2CS3 (CS-side, verified at CA-1.6) as explicit
bilateral sibling sub-clauses with SE-side/CS-side qualifiers. SHALL-F obligation text gains the
explicit sub-clause label SHALL-F-EXT-CS2CS3. CA-1.6 preamble-anchor paragraph cites
SHALL-F-EXT-CS2CS3 by name. All other R15-V-05 architecture preserved; no NON-OVERLAP DECLARATION
block added (C-43 remains open).
**Hypothesis:** 35/36 (adds C-44; C-43 remains open -- labeled block absent from Phase 3 mandate).

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

*(Identical to V-01 -- three Blind spot paragraphs with exact labels preserved.)*

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins. Execution order is self-attestable from phase labels alone.

**PHASE 0 -- CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1: eight schemas) and the Criterion
Enforcement Matrix preamble (Step 0.2: SHALL-A through SHALL-G including two named extension
sub-clauses declared with bilateral parity -- SHALL-D-EXT-C35 (SE-side: SE-4 STRUCTURED CLOSE
TABLE_4 SE-0 slot cross-reference, verified at CA-1.9) and SHALL-F-EXT-CS2CS3 (CS-side:
CS-EXPECTATION-VIOLATED three-field Remediation obligation, verified at CA-1.6) -- CEM four-column
mapping, R12 Structural Axis Declaration with A-1/A-2/A-3 and Attestation Row Ref column, M4
pre-assignments CA-1.1 through CA-1.10). Closes Phase 0 with Step 0.3 Phase 0 Artifact Manifest.
CA issues handoff to PHASE 1.

**PHASE 1 -- CS (Customer Success):**
*(Identical to V-01 PHASE 1 mandate.)*

**PHASE 2 -- SE (Security Engineer / Dataverse Security Expert):**
*(Identical to V-01 PHASE 2 mandate.)*

**PHASE 3 -- CA-1 (CA Verification Pass):**
CA returns. Each CA-1 row performs double-anchor reaffirmation. CA-1.9 verifies SE-4 STRUCTURED
CLOSE TABLE_4 SE-0 slot (completing SHALL-D-EXT-C35). CA-1.6 verifies CS-EXPECTATION-VIOLATED
three-field Remediation (completing SHALL-F-EXT-CS2CS3). CA-1.10 verifies bidirectional
label-identity cross-scan. Terminal verdict includes TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION.

---

## PHASE 0 -- CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1, 0.2, and 0.3 before any other phase begins.*

### Step 0.1 -- Schema Registry (CA-authored, Phase 0)

*(Identical to V-01 Step 0.1 -- all eight schema declarations unchanged.)*

### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

*(CEM table and R12 Structural Axis Declaration identical to V-01. SHALL obligations below are
the only change from V-01: SHALL-F gains explicit sub-clause label SHALL-F-EXT-CS2CS3.)*

**Declared rule: M1, M2, M3, M4 simultaneously active.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-0 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

*(Supplementary CA-1.N rows identical to V-01.)*

*(R12 Structural Axis Declaration with A-1/A-2/A-3, Attestation Row Ref column, non-interference
statement, and bidirectional loop binding identical to V-01.)*

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A through SHALL-E: *(identical to V-01)*
- SHALL-D: *(identical to V-01 including [C-35] extension sub-clause; CA-1.9 verifies.)*
- **SHALL-F extension sub-clause SHALL-F-EXT-CS2CS3:** When any CS-2 or CS-3 expectation
  conflicts with an SE finding, the conflict MUST be recorded in TABLE_5 as CS-EXPECTATION-VIOLATED.
  Each such row MUST carry all three Remediation fields: CS-Expected (citing the CS-2 or CS-3 row
  by row ID and stating the expectation verbatim or by reference), SE-Actual (the diverging SE
  finding), and Delta (exact configuration change to align SE-Actual to CS-Expected). A row missing
  any field MUST be reopened. CA-1.6 verifies this sub-clause; CA-1.6's preamble-anchor paragraph
  cites SHALL-F-EXT-CS2CS3 as the obligation it completes.
- SHALL-G: *(identical to V-01)*

*(Step 0.3 Phase 0 Artifact Manifest identical to V-01.)*

*Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS

*(Identical to V-01 -- CS-0, CS-1, CS-2, CS-3 tables unchanged.)*

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE

*(Identical to V-01 -- SE-0 through SE-5 with exact-label closure blocks unchanged.)*

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*CA returns. Each CA-1 row presents Registry anchor and Preamble anchor as labeled elements
before the Verification line. CA-1.9 verifies SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot
(completing SHALL-D-EXT-C35, distinct from CA-1.4 and CA-1.7). CA-1.6 verifies
CS-EXPECTATION-VIOLATED three-field Remediation (completing SHALL-F-EXT-CS2CS3). CA-1.10
verifies bidirectional label-identity cross-scan.*

*(CA-1.1 through CA-1.5 identical to V-01.)*

**CA-1.6 -- SHALL-F-EXT-CS2CS3 compliance verification** *(completing SHALL-F-EXT-CS2CS3 as
declared in Phase 0 bilateral mandate co-declaration)*:
- Registry anchor -- Schema ID TABLE_5 CS-EXPECTATION-VIOLATED row structure: [CS-Expected, SE-Actual, Delta] -- all three fields required per SHALL-F-EXT-CS2CS3 (CS-side bilateral sub-clause).
- Preamble anchor -- Completing SHALL-F-EXT-CS2CS3 as authored by CA in Phase 0: three-field Remediation block mandatory; CS-Expected MUST cite CS-2 or CS-3 row by ID; rows missing any field MUST be reopened. CA-1.6 pre-assigned as CS-side verification counterpart to CA-1.9 (SE-side).
- Verification -- For each CS-EXPECTATION-VIOLATED row: CS-Expected populated with row ID citation? SE-Actual populated? Delta populated with exact configuration change? -> PASS / FAIL per row.

*(CA-1.7 through CA-1.10 identical to V-01, with CA-1.9 note updated:)*

**CA-1.9** -- *(identical to V-01 CA-1.9 except preamble anchor names SHALL-D-EXT-C35 as
SE-side bilateral sub-clause counterpart to CA-1.6 / SHALL-F-EXT-CS2CS3 CS-side)*:
- Preamble anchor -- Completing SHALL-D-EXT-C35 as authored by CA in Phase 0 bilateral mandate:
  CA-1.9 pre-assigned as SE-side verification counterpart to CA-1.6 (CS-side / SHALL-F-EXT-CS2CS3).

*(CA Format Compliance Verdict and TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION identical to V-01.)*

---

## V-03 -- Single-Axis C-43 (Table Variant): NON-OVERLAP DECLARATION as Table

**Axis:** C-43 -- Same axis as V-01. Phase 3 gains the labeled NON-OVERLAP DECLARATION block,
but the block is formatted as a three-column table (`Row ID | Scope | Distinct From`) rather than
a bulleted list. Tests whether tabular structure is structurally more explicit than prose list
format for the C-43 labeled block requirement. All other R15-V-05 architecture unchanged (no C-44
bilateral mandate co-declaration).
**Hypothesis:** 35/36 (adds C-43 via table format; C-44 remains open). If table and list are
equivalent, same score as V-01. If table is strictly required, V-03 may differ from V-01.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

*(Identical to V-01.)*

---

## ROLE SEQUENCING MANDATE

*(Identical to V-01 ROLE SEQUENCING MANDATE -- Phase 0 through Phase 3 mandate text unchanged.
Phase 3 mandate text includes "labeled NON-OVERLAP DECLARATION block" as in V-01.)*

---

## PHASE 0 -- CA

*(Identical to V-01 Phase 0 -- Schema Registry, CEM preamble, SHALL obligations, Artifact
Manifest unchanged.)*

---

## PHASE 1 -- CS

*(Identical to V-01.)*

---

## PHASE 2 -- SE

*(Identical to V-01.)*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*(CA-1.1 through CA-1.10 identical to V-01. NON-OVERLAP DECLARATION block below uses table
format instead of bulleted list. All else identical.)*

**CA-1.N audit-target scope roster:**
*(Identical to V-01 scope roster.)*

**NON-OVERLAP DECLARATION:**

| Row ID | Scope | Distinct From |
|--------|-------|---------------|
| CA-1.4 | SE-0 execution ordering -- verifies TABLE_4 appears at SE-0 before TABLE_1; does not verify SE-4 STRUCTURED CLOSE content | CA-1.7 (MANUAL GAP format), CA-1.9 (SE-4 STRUCTURED CLOSE SE-0 slot) |
| CA-1.7 | MANUAL GAP exact-label blocks -- verifies character-for-character labels at SE-2, SE-3, SE-4 openings; does not verify SE-0 execution order or SE-4 STRUCTURED CLOSE content | CA-1.4 (SE-0 ordering), CA-1.9 (SE-4 STRUCTURED CLOSE SE-0 slot) |
| CA-1.9 | SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot -- verifies the TABLE_4 row cross-reference inside SE-4's STRUCTURED CLOSE block; does not verify TABLE_4 execution order or MANUAL GAP label format | CA-1.4 (SE-0 ordering), CA-1.7 (MANUAL GAP format) |

*(CA-1.1 through CA-1.10, Verdict, and TRI-DIMENSIONAL ATTESTATION identical to V-01.)*

---

## V-04 -- Combined C-43 + C-44: Full 36/36 Canonical

**Axis:** Combined -- V-01 NON-OVERLAP DECLARATION block (C-43) + V-02 bilateral mandate
co-declaration and SHALL-F-EXT-CS2CS3 explicit naming (C-44). Canonical path to 36/36.
**Hypothesis:** 36/36 (100.0). Both C-43 and C-44 simultaneously active; all R15-V-05 criteria
preserved.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

*(Identical to V-01.)*

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins. Execution order is self-attestable from phase labels alone.

**PHASE 0 -- CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1: eight schemas) and the Criterion
Enforcement Matrix preamble (Step 0.2: SHALL-A through SHALL-G including two named extension
sub-clauses declared with bilateral parity -- SHALL-D-EXT-C35 (SE-side: SE-4 STRUCTURED CLOSE
TABLE_4 SE-0 slot cross-reference, verified at CA-1.9) and SHALL-F-EXT-CS2CS3 (CS-side:
CS-EXPECTATION-VIOLATED three-field Remediation obligation, verified at CA-1.6) -- CEM four-column
mapping, R12 Structural Axis Declaration with A-1/A-2/A-3 and Attestation Row Ref column,
bidirectional loop binding, M4 pre-assignments CA-1.1 through CA-1.10). Closes with Step 0.3
Phase 0 Artifact Manifest. CA issues handoff to PHASE 1.

**PHASE 1 -- CS:** *(Identical to V-01.)*

**PHASE 2 -- SE:** *(Identical to V-01.)*

**PHASE 3 -- CA-1 (CA Verification Pass):**
CA returns. Phase 3 mandate carries complete CA-1.N audit-target scope roster followed by labeled
NON-OVERLAP DECLARATION block (named structural header; not inline prose; enumerates CA-1.4,
CA-1.7, CA-1.9 by Row ID and scope). Each CA-1 row performs double-anchor reaffirmation. CA-1.9
verifies SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot (completing SHALL-D-EXT-C35, distinct from
CA-1.4 and CA-1.7). CA-1.6 verifies CS-EXPECTATION-VIOLATED three-field Remediation (completing
SHALL-F-EXT-CS2CS3). CA-1.10 verifies bidirectional label-identity cross-scan. Terminal verdict
cites Phase 0 Artifact Manifest by item counts.

---

## PHASE 0 -- CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1, 0.2, and 0.3 before any other phase begins.*

### Step 0.1 -- Schema Registry

*(Identical to V-01 -- all eight schema declarations unchanged.)*

### Step 0.2 -- Criterion Enforcement Matrix Preamble

*(CEM table, supplementary CA-1.N rows, R12 Structural Axis Declaration, non-interference
statement, and bidirectional loop binding identical to V-01.)*

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A through SHALL-E: *(identical to V-01)*
- SHALL-D: *(identical to V-01 including [C-35] extension sub-clause; CA-1.9 verifies.)*
- **SHALL-F extension sub-clause SHALL-F-EXT-CS2CS3:** When any CS-2 or CS-3 expectation conflicts
  with an SE finding, the conflict MUST be recorded in TABLE_5 as CS-EXPECTATION-VIOLATED. Each
  such row MUST carry all three Remediation fields: CS-Expected (citing the CS-2 or CS-3 row by
  row ID), SE-Actual (the diverging SE finding), and Delta (exact configuration change to align
  SE-Actual to CS-Expected). A row missing any field MUST be reopened. CA-1.6 verifies this
  sub-clause; CA-1.6's preamble-anchor paragraph cites SHALL-F-EXT-CS2CS3 as the obligation
  it completes.
- SHALL-G: *(identical to V-01)*

### Step 0.3 -- Phase 0 Artifact Manifest

*(Identical to V-01.)*

*Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS

*(Identical to V-01.)*

---

## PHASE 2 -- SE

*(Identical to V-01.)*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

**CA-1.N audit-target scope roster:**
CA-1.1 (C-01/TABLE_1), CA-1.2 (C-02/TABLE_2), CA-1.3 (C-03/TABLE_3), CA-1.4 (C-04/TABLE_4
SE-0 ordering), CA-1.5 (C-05/TABLE_5), CA-1.6 (SHALL-F-EXT-CS2CS3 CS-EV three-field structure),
CA-1.7 (SHALL-G MANUAL GAP exact labels), CA-1.8 (CS-0 CS-2/CS-3 acknowledgment), CA-1.9 (SE-4
STRUCTURED CLOSE TABLE_4 SE-0 slot -- distinct from CA-1.4 and CA-1.7), CA-1.10 (bidirectional
label-identity cross-scan).

**NON-OVERLAP DECLARATION:**
The following three CA-1 rows have non-overlapping audit scopes:

- CA-1.4 [Scope: SE-0 execution ordering -- verifies TABLE_4 appears at SE-0 before TABLE_1;
  does not verify SE-4 STRUCTURED CLOSE content or MANUAL GAP label format]
- CA-1.7 [Scope: MANUAL GAP exact-label blocks -- verifies character-for-character labels at
  SE-2, SE-3, SE-4 openings; does not verify SE-0 execution order or SE-4 STRUCTURED CLOSE
  TABLE_4 row cross-reference]
- CA-1.9 [Scope: SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot -- verifies the TABLE_4 row
  cross-reference inside SE-4's STRUCTURED CLOSE block (SHALL-D-EXT-C35 completion); does not
  verify TABLE_4 execution order (CA-1.4) or MANUAL GAP label format (CA-1.7)]

*Each CA-1 row presents Registry anchor and Preamble anchor as structurally distinct labeled
elements before the Verification line.*

*(CA-1.1 through CA-1.5 identical to V-01.)*

**CA-1.6 -- SHALL-F-EXT-CS2CS3 compliance verification** *(CS-side bilateral sub-clause;
completing SHALL-F-EXT-CS2CS3 as declared in Phase 0 bilateral mandate co-declaration)*:
- Registry anchor -- Schema ID TABLE_5 CS-EXPECTATION-VIOLATED row structure: [CS-Expected (cites CS-2/CS-3 row ID), SE-Actual, Delta] -- all three fields required per SHALL-F-EXT-CS2CS3 (CS-side bilateral sub-clause).
- Preamble anchor -- Completing SHALL-F-EXT-CS2CS3 as authored by CA in Phase 0: three-field Remediation mandatory; CS-Expected MUST cite row ID; rows missing any field MUST be reopened. CA-1.6 pre-assigned as CS-side counterpart to CA-1.9 (SE-side / SHALL-D-EXT-C35).
- Verification -- For each CS-EXPECTATION-VIOLATED row: CS-Expected populated with row ID citation? SE-Actual populated? Delta populated with exact configuration change? -> PASS / FAIL per row.

*(CA-1.7 and CA-1.8 identical to V-01.)*

**CA-1.9 -- SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference** *(completing
SHALL-D-EXT-C35 SE-side bilateral sub-clause; distinct from CA-1.4 and CA-1.7)*:
- Registry anchor -- Schema ID TABLE_4 with Phase 0 SE-0 slot declaration (eight-schema Registry).
- Preamble anchor -- Completing SHALL-D-EXT-C35 as authored by CA in Phase 0 bilateral mandate:
  CA-1.9 pre-assigned as SE-side counterpart to CA-1.6 (CS-side / SHALL-F-EXT-CS2CS3).
- Verification -- SE-4's STRUCTURED CLOSE block begins with SE-0 slot naming a specific TABLE_4
  vector row by exact label? Populated at SE-0 with Checked?=YES? Inside STRUCTURED CLOSE block?
  -> PASS / FAIL
- Distinction confirmed: CA-1.4 (SE-0 ordering), CA-1.7 (MANUAL GAP format), CA-1.9 (SE-4
  STRUCTURED CLOSE SE-0 slot) -- three non-overlapping scopes.

*(CA-1.10, Verdict, and TRI-DIMENSIONAL ATTESTATION identical to V-01.)*

---

## V-05 -- Definitive Compound: C-43 + C-44 + Phase 3 Bilateral Echo + Bracket Annotations

**Axis:** V-04 base (C-43 NON-OVERLAP DECLARATION block + C-44 bilateral mandate co-declaration)
plus two additional structural reinforcements:
(1) Phase 3 mandate adds bilateral echo: CA-1.9 (SE-side, completing SHALL-D-EXT-C35) and CA-1.6
    (CS-side, completing SHALL-F-EXT-CS2CS3) are co-named as bilateral verification siblings in
    the Phase 3 mandate description, mirroring the Phase 0 co-declaration (foreshadows C-45).
(2) NON-OVERLAP DECLARATION block entries carry inline bracket annotations summarizing scope
    per statement (foreshadows C-46).
Architecture maximally reinforced; designed to surface C-45/C-46 if new rubric criteria emerge.
**Hypothesis:** 36/36 (100.0 under v15). Over-specification relative to v15; potential C-45/C-46
materialization if R16 variations are reviewed.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

*(Identical to V-01.)*

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins. Execution order is self-attestable from phase labels alone.

**PHASE 0 -- CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1: eight schemas) and the Criterion
Enforcement Matrix preamble (Step 0.2: SHALL-A through SHALL-G including two named extension
sub-clauses declared with bilateral parity -- SHALL-D-EXT-C35 (SE-side: SE-4 STRUCTURED CLOSE
TABLE_4 SE-0 slot cross-reference, verified at CA-1.9) and SHALL-F-EXT-CS2CS3 (CS-side:
CS-EXPECTATION-VIOLATED three-field Remediation obligation, verified at CA-1.6) -- CEM four-column
mapping, R12 Structural Axis Declaration with A-1/A-2/A-3 and Attestation Row Ref column,
bidirectional loop binding, M4 pre-assignments CA-1.1 through CA-1.10). Closes with Step 0.3
Phase 0 Artifact Manifest. CA issues handoff to PHASE 1.

**PHASE 1 -- CS:** *(Identical to V-01.)*

**PHASE 2 -- SE:** *(Identical to V-01.)*

**PHASE 3 -- CA-1 (CA Verification Pass):**
CA returns. Phase 3 mandate carries complete CA-1.N audit-target scope roster followed by labeled
NON-OVERLAP DECLARATION block (named structural header; entries carry inline bracket annotations
per statement). CA-1.9 (SE-side, completing SHALL-D-EXT-C35) and CA-1.6 (CS-side, completing
SHALL-F-EXT-CS2CS3) are co-named as bilateral verification siblings -- both verification rows
cited with their sub-clause identifiers and side qualifiers in the Phase 3 mandate. Each CA-1 row
performs double-anchor reaffirmation. CA-1.10 verifies bidirectional label-identity cross-scan.
Terminal verdict cites Phase 0 Artifact Manifest by item counts.

---

## PHASE 0 -- CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*(Identical to V-04 Phase 0 -- Schema Registry, CEM preamble with SHALL-F-EXT-CS2CS3 explicit
naming, R12 Structural Axis Declaration, bidirectional loop, SHALL obligations A-G, and Phase 0
Artifact Manifest unchanged.)*

---

## PHASE 1 -- CS

*(Identical to V-01.)*

---

## PHASE 2 -- SE

*(Identical to V-01.)*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

**CA-1.N audit-target scope roster:**
CA-1.1 (C-01/TABLE_1), CA-1.2 (C-02/TABLE_2), CA-1.3 (C-03/TABLE_3), CA-1.4 (C-04/TABLE_4
SE-0 ordering), CA-1.5 (C-05/TABLE_5), CA-1.6 (SHALL-F-EXT-CS2CS3 CS-side bilateral sub-clause),
CA-1.7 (SHALL-G MANUAL GAP exact labels), CA-1.8 (CS-0 CS-2/CS-3 acknowledgment), CA-1.9
(SHALL-D-EXT-C35 SE-side bilateral sub-clause), CA-1.10 (bidirectional label-identity cross-scan).

**Bilateral verification siblings declared:** CA-1.9 (SE-side, completing SHALL-D-EXT-C35: SE-4
STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference) and CA-1.6 (CS-side, completing
SHALL-F-EXT-CS2CS3: CS-EXPECTATION-VIOLATED three-field Remediation) are co-equal bilateral
verification counterparts. SE-side and CS-side sub-clauses are independently mandated and
independently verified; completion of one does not substitute for the other.

**NON-OVERLAP DECLARATION:**
The following three CA-1 rows have non-overlapping audit scopes. Bracket annotations state scope
per entry:

- CA-1.4 [SE-0 execution ordering: TABLE_4 appears at SE-0 before TABLE_1; Tier columns present
  in TABLE_1/TABLE_3; does not cover MANUAL GAP labels or SE-4 STRUCTURED CLOSE content]
- CA-1.7 [MANUAL GAP exact-label blocks: character-for-character label match at SE-2/SE-3/SE-4
  openings only; does not cover SE-0 execution position or SE-4 STRUCTURED CLOSE TABLE_4 row
  cross-reference]
- CA-1.9 [SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot: TABLE_4 row cross-reference inside
  STRUCTURED CLOSE block only (SHALL-D-EXT-C35 SE-side); does not cover TABLE_4 execution
  ordering (CA-1.4) or MANUAL GAP label format (CA-1.7)]

Non-overlap is structural: each entry references a distinct output location and a distinct
mechanism obligation. No output artifact is covered by more than one of these three rows.

*Each CA-1 row presents Registry anchor and Preamble anchor as structurally distinct labeled
elements before the Verification line.*

*(CA-1.1 through CA-1.5 identical to V-01.)*

**CA-1.6 -- SHALL-F-EXT-CS2CS3 compliance verification** *(CS-side bilateral sub-clause;
bilateral counterpart to CA-1.9 SE-side)*:
- Registry anchor -- Schema ID TABLE_5 CS-EXPECTATION-VIOLATED row structure: [CS-Expected (cites CS-2/CS-3 row ID), SE-Actual, Delta] -- all three fields required per SHALL-F-EXT-CS2CS3 (CS-side bilateral sub-clause; CA-1.6 is CS-side counterpart to CA-1.9 SE-side).
- Preamble anchor -- Completing SHALL-F-EXT-CS2CS3 as authored by CA in Phase 0 bilateral mandate co-declaration: three-field Remediation mandatory; CS-Expected MUST cite row ID. CA-1.6 pre-assigned as CS-side bilateral counterpart to CA-1.9 (SE-side / SHALL-D-EXT-C35).
- Verification -- For each CS-EXPECTATION-VIOLATED row: CS-Expected populated with row ID citation? SE-Actual populated? Delta with exact configuration change? -> PASS / FAIL per row.

*(CA-1.7 and CA-1.8 identical to V-01.)*

**CA-1.9 -- SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference** *(completing
SHALL-D-EXT-C35 SE-side bilateral sub-clause; bilateral counterpart to CA-1.6 CS-side)*:
- Registry anchor -- Schema ID TABLE_4 with Phase 0 SE-0 slot declaration.
- Preamble anchor -- Completing SHALL-D-EXT-C35 as authored by CA in Phase 0 bilateral mandate:
  CA-1.9 pre-assigned as SE-side counterpart to CA-1.6 (CS-side / SHALL-F-EXT-CS2CS3). The
  bilateral pair (CA-1.9 SE-side, CA-1.6 CS-side) is declared in Phase 0 mandate and echoed in
  Phase 3 mandate; both sides independently verified.
- Verification -- SE-4's STRUCTURED CLOSE block begins with SE-0 slot naming a specific TABLE_4
  vector row by exact label? Populated at SE-0? Inside STRUCTURED CLOSE? -> PASS / FAIL
- Distinction confirmed: CA-1.4 (SE-0 ordering), CA-1.7 (MANUAL GAP format), CA-1.9 (SE-4
  STRUCTURED CLOSE SE-0 slot) -- three non-overlapping scopes confirmed by NON-OVERLAP DECLARATION.

**CA-1.10 -- Bidirectional loop label-identity cross-scan:**
*(Identical to V-01 CA-1.10.)*

**CA Format Compliance Verdict:**
*(Identical to V-04 verdict structure, citing 8 schemas / 5 criterion rows / 7 SHALLs including
bilateral sub-clauses SHALL-D-EXT-C35 and SHALL-F-EXT-CS2CS3 / 5 supplementary rows / 3 A-N rows.)*

**TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION:**
*(Identical to V-01 attestation table with ATTEST-A-1/A-2/A-3 rows, Preamble Row Ref back-column.)*
