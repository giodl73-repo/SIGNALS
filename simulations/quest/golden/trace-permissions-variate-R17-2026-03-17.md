# trace-permissions Variate -- Round 17
**Date:** 2026-03-17
**Rubric:** v16 (proposed) -- 38 criteria (C-01 through C-46), denominator 38
**Target:** 38/38 -- add C-45 (Phase 3 mandate bilateral verification echo) and C-46
(NON-OVERLAP per-statement bracket citations) to R16-V-04 base (36/36 under v15)

**State entering Round 17:**

| Variation | v15 score | Notes |
|-----------|-----------|-------|
| R16-V-05 | 100.0 (36/36) | Full canonical: C-43+C-44 + foreshadowed C-45 (bilateral echo in Phase 3 mandate) + foreshadowed C-46 (bracket annotations in NON-OVERLAP entries); under proposed v16 already satisfies C-45 and C-46 at 38/38 |
| R16-V-04 | 100.0 (36/36) | Combined C-43+C-44 without Phase 3 bilateral echo or NON-OVERLAP bracket annotations; under v16 fails C-45 and C-46 |
| R16-V-01/V-03 | 99.4 (35/36) | C-43 single-axis; fails C-44, C-45, C-46 |
| R16-V-02 | 97.2 (35/36) | C-44 single-axis; fails C-43, C-45, C-46 |

**Path to 38/38:** R16-V-04 base + C-45 (Phase 3 mandate co-names CA-1.9 SE-side and CA-1.6
CS-side as co-equal bilateral verification obligations with explicit side qualifiers) + C-46
(NON-OVERLAP DECLARATION per-statement inline bracket annotations). Both axes are independent;
V-03 is the canonical combination.

---

## v15 -> v16 Rubric Extension

**2 new aspirational criteria. Denominator: 36 -> 38. Each aspirational = 10/38 ~= 0.263 pts.**

| ID | Hangs off | Pattern | What it tests |
|----|-----------|---------|---------------|
| C-45 | C-44+C-39 | R16-V-05 | Phase 3 ROLE SEQUENCING MANDATE bilateral verification echo -- Phase 3 mandate co-names CA-1.9 (SE-side: SHALL-D-EXT-C35 completion) and CA-1.6 (CS-side: SHALL-F-EXT-CS2CS3 completion) as co-equal named verification obligations with explicit side qualifiers, in a single statement or list. Distinction from C-44: C-44 tests the Phase 0 co-declaration of the *obligation* sub-clauses; C-45 tests the Phase 3 echo of the *verification* obligations. An output that names CA-1.9 and CA-1.6 individually in Phase 3 without co-equal framing or side qualifiers fails this criterion. Both prose and bulleted list forms satisfy the pass condition. |
| C-46 | C-43+C-42 | R16-V-05 | NON-OVERLAP DECLARATION per-statement CA row-ID bracket citations -- each statement within the labeled NON-OVERLAP DECLARATION block carries an inline `[CA-1.N: scope-summary]` annotation. Row-prefix format (`CA-1.N [scope] audits...`) and sentence-embedded format (`bounded by [CA-1.N: scope-summary] is exclusively...`) are both valid; the criterion is format-flexible. An output with a labeled NON-OVERLAP DECLARATION block (C-43 pass) that does not annotate every statement with a bracket citation fails C-46. |

**R16-V-04 re-scored under v16:**

| Criterion | v15 | v16 verdict | Why it moves |
|-----------|-----|-------------|--------------|
| C-45 | -- (new) | FAIL | Phase 3 mandate names CA-1.9 and CA-1.6 individually (distinct sub-obligations), not as a bilateral co-equal pair with side qualifiers |
| C-46 | -- (new) | FAIL | NON-OVERLAP DECLARATION block carries three statements without any bracket annotations |
| R16-V-04 composite | 100.0 (36/36) | **94.7 (36/38)** | 2 x 0.263 = 0.53 pts lost |

**R16-V-05 re-scored under v16:**

| Criterion | v15 | v16 verdict | Why it holds |
|-----------|-----|-------------|--------------|
| C-45 | -- (new) | PASS | Phase 3 mandate: "CA-1.9 (SE-side, completing SHALL-D-EXT-C35) and CA-1.6 (CS-side, completing SHALL-F-EXT-CS2CS3) are co-named as bilateral verification siblings" -- co-equal framing with explicit SE-side/CS-side qualifiers present |
| C-46 | -- (new) | PASS | NON-OVERLAP entries carry inline bracket annotations: CA-1.4 `[SE-0 execution ordering...]`, CA-1.7 `[MANUAL GAP exact-label blocks...]`, CA-1.9 `[SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot...]` |
| R16-V-05 composite | 100.0 (36/36) | **100.0 (38/38)** | v16 ceiling confirmed |

**Structural insight:** C-45 is the Phase 3 mirror of C-44. C-44 (Phase 0) establishes the bilateral
obligation mandate; C-45 (Phase 3) echoes that mandate at the verification layer. The bilateral
SE+CS pattern now spans both ends of the execution protocol.

---

## Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Single-axis C-45: Phase 3 mandate bilateral echo (prose form) on R16-V-04 base | R16-V-04 base. Phase 3 ROLE SEQUENCING MANDATE text adds co-equal bilateral statement naming CA-1.9 (SE-side: SHALL-D-EXT-C35) and CA-1.6 (CS-side: SHALL-F-EXT-CS2CS3) with explicit side qualifiers. Phase 3 body gains a bilateral declaration line before the NON-OVERLAP block. NON-OVERLAP preserves V-04 three-statement form without bracket annotations (C-46 remains open). Hypothesis: 37/38. |
| V-02 | Single-axis C-46: NON-OVERLAP bracket citations (sentence-embedded format) on R16-V-04 base | R16-V-04 base. NON-OVERLAP DECLARATION block statements gain inline `[CA-1.N: scope-summary]` in sentence-embedded form. Phase 3 mandate bilateral echo absent (C-45 remains open). Hypothesis: 37/38. |
| V-03 | Combined C-45 + C-46: canonical 38/38 | R16-V-04 base + V-01 Phase 3 bilateral echo (prose) + V-02 bracket annotations (sentence-embedded). Both axes independently satisfied; no structural interference between Phase 3 mandate layer (C-45) and NON-OVERLAP statement layer (C-46). Hypothesis: 38/38 (100.0). |
| V-04 | C-45 list form + C-46 sentence-embedded | V-03 architecture with Phase 3 bilateral echo as bulleted two-item list (CA-1.9 SE-side bullet / CA-1.6 CS-side bullet) rather than prose sentence. Tests C-45 pass condition "single statement or list." All else identical to V-03. Hypothesis: 38/38 (100.0). |
| V-05 | Definitive compound: C-45 prose + C-46 sentence-embedded + C-47 surface signal | V-03 base plus: NON-OVERLAP DECLARATION block gains a fourth statement covering CA-1.6 (CS-side: SHALL-F-EXT-CS2CS3 three-field structure) with bracket annotation, naming CA-1.9 as its SE-side bilateral complement. Closes bilateral symmetry at the NON-OVERLAP scope-declaration layer -- mirrors C-44 (Phase 0 obligation) and C-45 (Phase 3 mandate). Foreshadows C-47. Hypothesis: 38/38 (100.0). Architecture above ceiling. |

---

## V-01 -- Single-Axis C-45: Phase 3 Mandate Bilateral Echo (Prose)

**Axis:** C-45 -- Phase 3 ROLE SEQUENCING MANDATE text gains a co-equal bilateral statement
naming CA-1.9 (SE-side: SHALL-D-EXT-C35 TABLE_4 row cross-reference) and CA-1.6 (CS-side:
SHALL-F-EXT-CS2CS3 three-field structure) as bilateral verification counterparts with explicit
side qualifiers. Phase 3 body gains a bilateral declaration line before the NON-OVERLAP block.
NON-OVERLAP DECLARATION preserves R16-V-04 three-statement form without bracket annotations
(C-46 remains open).
**Hypothesis:** 37/38 (adds C-45; C-46 open -- no bracket citations in NON-OVERLAP statements).

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
NON-OVERLAP DECLARATION block (named structural header; not inline prose). CA-1.9 (SE-side:
SHALL-D-EXT-C35 TABLE_4 row cross-reference) and CA-1.6 (CS-side: SHALL-F-EXT-CS2CS3 three-field
structure) serve as co-equal named verification obligations completing the bilateral parity declared
in Phase 0. Each CA-1 row performs double-anchor reaffirmation (Registry anchor labeled, Preamble
anchor labeled, Verification statement following both). CA-1.10 verifies bidirectional
label-identity cross-scan. Terminal verdict includes TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION
with ATTEST-A-N Row IDs and Preamble Row Ref back-column, and cites Phase 0 Artifact Manifest
by item counts.

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
| CA-1.6 | SHALL-F-EXT-CS2CS3 CS-EXPECTATION-VIOLATED three-field Remediation structure | TABLE_5 CS-EV rows | CA-1.9 |
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
  mechanism and reason. **Extension sub-clause [C-35] SHALL-D-EXT-C35:** SE-4's STRUCTURED CLOSE
  block SHALL carry a TABLE_4 row cross-reference at the SE-0 slot naming a specific TABLE_4 vector
  row by exact vector label. CA-1.9 verifies this sub-clause; distinct from CA-1.4 (SE-0 ordering).
- SHALL-E: TABLE_5 has at least one named gap with specific field, role, or rule. Zero-gap case
  requires explicit evidence rows confirming what was checked.
- SHALL-F: When any CS-2 or CS-3 expectation conflicts with an SE finding, the conflict MUST be
  recorded in TABLE_5 as CS-EXPECTATION-VIOLATED. **Extension sub-clause SHALL-F-EXT-CS2CS3:**
  Each such row MUST carry all three Remediation fields (CS-Expected citing CS-2 or CS-3 row ID,
  SE-Actual, Delta as exact configuration change). A row missing any field MUST be reopened.
  CA-1.6 verifies this sub-clause; CA-1.6 is the CS-side verification counterpart to CA-1.9
  (SE-side / SHALL-D-EXT-C35).
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
SHALL-A, SHALL-B, SHALL-C, SHALL-D (with SHALL-D-EXT-C35), SHALL-E, SHALL-F (with SHALL-F-EXT-CS2CS3), SHALL-G

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
After TABLE_1: populate SE Cross-Reference and SE Confirmation in CS-3.

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
CA-1.9 verification (SHALL-D-EXT-C35 extension sub-clause); distinct from the MANUAL GAP block
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

CS-EXPECTATION-VIOLATED rows (three-field Remediation block per SHALL-F-EXT-CS2CS3):
- CS-Expected: [cite CS-2 or CS-3 row ID; state expectation verbatim or by row reference]
- SE-Actual: [SE finding that contradicts the expectation]
- Delta: [exact configuration change to align SE-Actual to CS-Expected]

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

**CA-1.N audit-target scope roster:**
CA-1.1 (C-01/TABLE_1), CA-1.2 (C-02/TABLE_2), CA-1.3 (C-03/TABLE_3), CA-1.4 (C-04/TABLE_4
SE-0 ordering), CA-1.5 (C-05/TABLE_5), CA-1.6 (SHALL-F-EXT-CS2CS3 CS-side bilateral sub-clause),
CA-1.7 (SHALL-G MANUAL GAP exact labels), CA-1.8 (CS-0 CS-2/CS-3 acknowledgment), CA-1.9
(SHALL-D-EXT-C35 SE-side bilateral sub-clause -- SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot),
CA-1.10 (bidirectional label-identity cross-scan).

**Bilateral verification pair:** CA-1.9 (SE-side: SHALL-D-EXT-C35 TABLE_4 row cross-reference) and
CA-1.6 (CS-side: SHALL-F-EXT-CS2CS3 three-field structure) serve as co-equal named verification
obligations completing the bilateral parity declared in Phase 0. Each side is independently
mandated and independently verified; completion of one does not substitute for the other.

**NON-OVERLAP DECLARATION:**
The following three CA-1 rows have non-overlapping audit scopes. Each verifies a structurally
distinct sub-obligation; no two rows verify the same output artifact:

- CA-1.4: Scope is SE-0 execution ordering -- verifies TABLE_4 appears at SE-0 before TABLE_1;
  does not verify MANUAL GAP labels or SE-4 STRUCTURED CLOSE content.
- CA-1.7: Scope is MANUAL GAP exact-label blocks -- verifies character-for-character label match
  at SE-2, SE-3, SE-4 openings only; does not verify SE-0 execution order or SE-4 STRUCTURED
  CLOSE TABLE_4 row cross-reference.
- CA-1.9: Scope is SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot -- verifies the TABLE_4 row
  cross-reference inside SE-4's STRUCTURED CLOSE block (SHALL-D-EXT-C35 SE-side); does not
  verify TABLE_4 execution order (CA-1.4) or MANUAL GAP label format (CA-1.7).

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
- Note (NON-OVERLAP): CA-1.4 verifies SE-0 execution ordering only. SE-4 STRUCTURED CLOSE SE-0 slot content is CA-1.9's scope (SHALL-D-EXT-C35 extension).

**CA-1.5 -- C-05 verification** *(Phase 0 M4 pre-assignment CA-1.5)*:
- Registry anchor -- Schema ID TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Tier, Severity, Remediation] -- blank cells prohibited globally.
- Preamble anchor -- C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 -- verifying...
- Verification -- TABLE_5 present? Named gap with specific field/role/rule? Tier column populated? Remediations exact? -> PASS / FAIL

**CA-1.6 -- SHALL-F-EXT-CS2CS3 compliance verification** *(CS-side bilateral sub-clause)*:
- Registry anchor -- Schema ID TABLE_5 CS-EXPECTATION-VIOLATED row structure: [CS-Expected (cites CS-2/CS-3 row ID), SE-Actual, Delta] -- all three fields required per SHALL-F-EXT-CS2CS3.
- Preamble anchor -- Completing SHALL-F-EXT-CS2CS3 as authored by CA in Phase 0: three-field Remediation block mandatory; CS-Expected MUST cite CS-2 or CS-3 row by ID; rows missing any field MUST be reopened. CA-1.6 pre-assigned as CS-side counterpart to CA-1.9 (SE-side / SHALL-D-EXT-C35).
- Verification -- For each CS-EXPECTATION-VIOLATED row: CS-Expected populated with row ID citation? SE-Actual populated? Delta populated with exact configuration change? -> PASS / FAIL per row.

**CA-1.7 -- SHALL-G compliance verification** *(exact-label MANUAL GAP two-part closure blocks)*:
- Registry anchor -- CONTEXT section declared exact labels: "Blind spot 1 -- Post-incident FLS gap" (SE-2), "Blind spot 2 -- Cumulative privilege blind spot" (SE-3), "Blind spot 3 -- OWD-sharing-rule override gap" (SE-4). SHALL-G requires two-part blocks with character-for-character label.
- Preamble anchor -- SHALL-G as authored by CA: Line 1 `MANUAL GAP [<exact label>]:`; paraphrase fails. CA-1.7 verifies. Distinct from CA-1.9.
- Verification -- SE-2 opens with `MANUAL GAP [Blind spot 1 -- Post-incident FLS gap]:`? Followed by `STRUCTURED CLOSE:`? SE-3/SE-4 same pattern with exact labels? -> PASS / FAIL per section.
- Note (NON-OVERLAP): CA-1.7 verifies MANUAL GAP block format only. TABLE_4 row cross-reference inside SE-4's STRUCTURED CLOSE is CA-1.9's scope.

**CA-1.8 -- CS-2/CS-3 Schema Registry registration + CS-0 acknowledgment** *(A-3 / C-33)*:
- Registry anchor -- Schema Registry declared CS-2 and CS-3 as named schema entries with SE-updatable columns and SE-update protocols co-located. PHASE 1 mandate requires CS-0 to acknowledge both schema IDs before CS-1.
- Preamble anchor -- CS-2 and CS-3 are Schema Registry entries. CS-0 acknowledgment is a PHASE 1 structural requirement per Axis A-3 (C-33) of the R12 Structural Axis Declaration.
- Verification -- CS-2 in Registry? CS-3 in Registry? CS-0 present before CS-1? CS-0 cites both schema IDs by exact label? CS-0 lists SE-updatable columns for both? SE populated SE-updatable columns? -> PASS / FAIL

**CA-1.9 -- SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference** *(completing SHALL-D-EXT-C35
SE-side bilateral sub-clause; distinct from CA-1.4 and CA-1.7)*:
- Registry anchor -- Schema ID TABLE_4 with Phase 0 SE-0 slot declaration: "SE-4's STRUCTURED CLOSE block SHALL carry a TABLE_4 row cross-reference at its SE-0 slot, naming a specific TABLE_4 vector row by its exact vector label."
- Preamble anchor -- Completing SHALL-D-EXT-C35 as authored by CA: CA-1.9 pre-assigned to verify SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot | SE-4 STRUCTURED CLOSE block only | Distinct from CA-1.4 (SE-0 ordering) and CA-1.7 (MANUAL GAP labels). CA-1.9 is SE-side bilateral counterpart to CA-1.6 (CS-side / SHALL-F-EXT-CS2CS3).
- Verification -- SE-4's STRUCTURED CLOSE block begins with an SE-0 slot entry naming a specific TABLE_4 vector row by its exact vector label? That row was populated at SE-0? The cross-reference is inside STRUCTURED CLOSE (not in MANUAL GAP block, not in TABLE_5)? -> PASS / FAIL
- Distinction confirmed (NON-OVERLAP): CA-1.4 verified TABLE_4 appeared at SE-0 before TABLE_1. CA-1.7 verified MANUAL GAP exact-label blocks. CA-1.9 verifies the TABLE_4 row cross-reference inside SE-4's STRUCTURED CLOSE -- three non-overlapping audit targets.

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
(Step 0.2, Phase 0, 5 criterion rows, 7 SHALL obligations including SHALL-D-EXT-C35 and
SHALL-F-EXT-CS2CS3, 5 supplementary CA-1.N rows), R12 Structural Axis Declaration (Step 0.2,
Phase 0, 3 A-N rows), Phase 0 Artifact Manifest (Step 0.3, Phase 0: 8 schemas / 5 criterion
rows / 7 SHALLs / 5 supplementary rows / 3 A-N rows -- all declared artifacts exercised).
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

## V-02 -- Single-Axis C-46: NON-OVERLAP Bracket Citations (Sentence-Embedded)

**Axis:** C-46 -- NON-OVERLAP DECLARATION block statements gain inline `[CA-1.N: scope-summary]`
in sentence-embedded format. Each statement restructured as: "The audit scope bounded by
[CA-1.N: scope-description] is exclusively [what it covers]; does not cover [what it excludes]."
Phase 3 ROLE SEQUENCING MANDATE bilateral echo absent (C-45 remains open -- Phase 3 mandate
does not co-name CA-1.9/CA-1.6 as bilateral co-equal pair with side qualifiers).
All other R16-V-04 architecture preserved unchanged.
**Hypothesis:** 37/38 (adds C-46; C-45 open -- no bilateral echo in Phase 3 mandate or body).

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
*(Identical to V-01 PHASE 0 mandate.)*

**PHASE 1 -- CS (Customer Success):**
*(Identical to V-01 PHASE 1 mandate.)*

**PHASE 2 -- SE (Security Engineer / Dataverse Security Expert):**
*(Identical to V-01 PHASE 2 mandate.)*

**PHASE 3 -- CA-1 (CA Verification Pass):**
CA returns. Phase 3 mandate carries complete CA-1.N audit-target scope roster followed by labeled
NON-OVERLAP DECLARATION block (named structural header; entries carry inline bracket annotations
per statement). Each CA-1 row performs double-anchor reaffirmation (Registry anchor labeled,
Preamble anchor labeled, Verification statement following both). CA-1.9 verifies SE-4 STRUCTURED
CLOSE TABLE_4 SE-0 slot (completing SHALL-D-EXT-C35). CA-1.6 verifies CS-EXPECTATION-VIOLATED
three-field Remediation (completing SHALL-F-EXT-CS2CS3). CA-1.10 verifies bidirectional
label-identity cross-scan. Terminal verdict includes TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION
and cites Phase 0 Artifact Manifest by item counts.

---

## PHASE 0 -- CA

*(Identical to V-01 -- Schema Registry, CEM preamble, SHALL obligations, Artifact Manifest
unchanged.)*

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

**NON-OVERLAP DECLARATION:**
The following three CA-1 rows have non-overlapping audit scopes. Each statement carries an inline
bracket annotation bounding the scope:

- The audit scope bounded by [CA-1.4: SE-0 execution ordering and four-vector TABLE_4 presence]
  is exclusively TABLE_4 appearing at SE-0 before SE-1; does not cover MANUAL GAP label format
  at SE-2/SE-3/SE-4 or SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference content.
- The audit scope bounded by [CA-1.7: MANUAL GAP exact-label blocks at SE-2/SE-3/SE-4 openings]
  is exclusively character-for-character label verification at SE-2, SE-3, SE-4 openings; does not
  cover SE-0 execution order or TABLE_4 row cross-reference inside SE-4's STRUCTURED CLOSE block.
- The audit scope bounded by [CA-1.9: SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference]
  is exclusively the TABLE_4 row named inside SE-4's STRUCTURED CLOSE block (SHALL-D-EXT-C35
  SE-side); does not cover TABLE_4 execution order (CA-1.4) or MANUAL GAP label format (CA-1.7).

*Each CA-1 row presents Registry anchor and Preamble anchor as structurally distinct labeled
elements before the Verification line.*

*(CA-1.1 through CA-1.10, CA Format Compliance Verdict, and TRI-DIMENSIONAL SELF-EVIDENCE
ATTESTATION identical to V-01.)*

---

## V-03 -- Combined C-45 + C-46: Canonical 38/38

**Axis:** Combined -- V-01 Phase 3 bilateral echo (prose co-equal statement, C-45) + V-02
sentence-embedded NON-OVERLAP bracket annotations (C-46). Canonical path to 38/38.
Both axes are independent: C-45 operates at the Phase 3 mandate layer; C-46 operates at the
NON-OVERLAP statement layer. No structural interference.
**Hypothesis:** 38/38 (100.0). Definitive golden candidate.

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
*(Identical to V-01 PHASE 0 mandate.)*

**PHASE 1 -- CS (Customer Success):**
*(Identical to V-01 PHASE 1 mandate.)*

**PHASE 2 -- SE (Security Engineer / Dataverse Security Expert):**
*(Identical to V-01 PHASE 2 mandate.)*

**PHASE 3 -- CA-1 (CA Verification Pass):**
CA returns. Phase 3 mandate carries complete CA-1.N audit-target scope roster followed by labeled
NON-OVERLAP DECLARATION block (named structural header; entries carry inline bracket annotations
per statement). CA-1.9 (SE-side: SHALL-D-EXT-C35 TABLE_4 row cross-reference) and CA-1.6
(CS-side: SHALL-F-EXT-CS2CS3 three-field structure) serve as co-equal named verification
obligations completing the bilateral parity declared in Phase 0. Each CA-1 row performs
double-anchor reaffirmation. CA-1.10 verifies bidirectional label-identity cross-scan. Terminal
verdict includes TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION and cites Phase 0 Artifact Manifest
by item counts.

---

## PHASE 0 -- CA

*(Identical to V-01 Phase 0 -- Schema Registry, CEM preamble with SHALL-D-EXT-C35 and
SHALL-F-EXT-CS2CS3, R12 Structural Axis Declaration, SHALL obligations, Artifact Manifest
unchanged.)*

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

**Bilateral verification pair:** CA-1.9 (SE-side: SHALL-D-EXT-C35 TABLE_4 row cross-reference) and
CA-1.6 (CS-side: SHALL-F-EXT-CS2CS3 three-field structure) serve as co-equal named verification
obligations completing the bilateral parity declared in Phase 0. Each side is independently
mandated and independently verified; completion of one does not substitute for the other.

**NON-OVERLAP DECLARATION:**
The following three CA-1 rows have non-overlapping audit scopes. Each statement carries an inline
bracket annotation bounding the scope:

- The audit scope bounded by [CA-1.4: SE-0 execution ordering and four-vector TABLE_4 presence]
  is exclusively TABLE_4 appearing at SE-0 before SE-1; does not cover MANUAL GAP label format
  at SE-2/SE-3/SE-4 or SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference content.
- The audit scope bounded by [CA-1.7: MANUAL GAP exact-label blocks at SE-2/SE-3/SE-4 openings]
  is exclusively character-for-character label verification at SE-2, SE-3, SE-4 openings; does not
  cover SE-0 execution order or TABLE_4 row cross-reference inside SE-4's STRUCTURED CLOSE block.
- The audit scope bounded by [CA-1.9: SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference]
  is exclusively the TABLE_4 row named inside SE-4's STRUCTURED CLOSE block (SHALL-D-EXT-C35
  SE-side); does not cover TABLE_4 execution order (CA-1.4) or MANUAL GAP label format (CA-1.7).

*Each CA-1 row presents Registry anchor and Preamble anchor as structurally distinct labeled
elements before the Verification line.*

*(CA-1.1 through CA-1.10, CA Format Compliance Verdict, and TRI-DIMENSIONAL SELF-EVIDENCE
ATTESTATION identical to V-01.)*

---

## V-04 -- C-45 List Form + C-46: Format-Flexibility Confirmation

**Axis:** V-03 architecture with Phase 3 bilateral echo as bulleted two-item list rather than
prose sentence. Tests whether C-45 pass condition "single statement or list" is unambiguously
satisfied by the bulleted form. CA-1.9 SE-side and CA-1.6 CS-side appear as separate bullet items,
each with sub-clause ID and side qualifier. NON-OVERLAP bracket annotations identical to V-03
(C-46 axis preserved). All else identical to V-03.
**Hypothesis:** 38/38 (100.0). Confirms C-45 list-form equivalence to prose co-equal statement.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

*(Identical to V-01.)*

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins. Execution order is self-attestable from phase labels alone.

**PHASE 0 -- CA:** *(Identical to V-01.)*

**PHASE 1 -- CS:** *(Identical to V-01.)*

**PHASE 2 -- SE:** *(Identical to V-01.)*

**PHASE 3 -- CA-1 (CA Verification Pass):**
CA returns. Phase 3 mandate carries complete CA-1.N audit-target scope roster followed by labeled
NON-OVERLAP DECLARATION block (named structural header; entries carry inline bracket annotations
per statement). The following bilateral verification obligations complete the bilateral parity
declared in Phase 0:
- CA-1.9 (SE-side: SHALL-D-EXT-C35 -- SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference)
- CA-1.6 (CS-side: SHALL-F-EXT-CS2CS3 -- CS-EXPECTATION-VIOLATED three-field Remediation)

Both are co-equal named verification obligations; each side is independently mandated and
independently verified. Each CA-1 row performs double-anchor reaffirmation. CA-1.10 verifies
bidirectional label-identity cross-scan. Terminal verdict includes TRI-DIMENSIONAL SELF-EVIDENCE
ATTESTATION and cites Phase 0 Artifact Manifest by item counts.

---

## PHASE 0 -- CA

*(Identical to V-01.)*

---

## PHASE 1 -- CS

*(Identical to V-01.)*

---

## PHASE 2 -- SE

*(Identical to V-01.)*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

**CA-1.N audit-target scope roster:**
*(Identical to V-03.)*

**Bilateral verification obligations (co-equal; both independently mandated):**
- CA-1.9 (SE-side): verifies SHALL-D-EXT-C35 -- SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot
  cross-reference naming a specific TABLE_4 vector row by exact vector label.
- CA-1.6 (CS-side): verifies SHALL-F-EXT-CS2CS3 -- CS-EXPECTATION-VIOLATED three-field
  Remediation completeness (CS-Expected row-ID citation, SE-Actual, Delta).

**NON-OVERLAP DECLARATION:**
*(Identical to V-03 -- three sentence-embedded bracket annotations for CA-1.4, CA-1.7, CA-1.9.)*

*Each CA-1 row presents Registry anchor and Preamble anchor as structurally distinct labeled
elements before the Verification line.*

*(CA-1.1 through CA-1.10, CA Format Compliance Verdict, and TRI-DIMENSIONAL SELF-EVIDENCE
ATTESTATION identical to V-01.)*

---

## V-05 -- Definitive Compound: C-45 Prose + C-46 Sentence-Embedded + C-47 Surface Signal

**Axis:** V-03 base (C-45 prose bilateral echo + C-46 sentence-embedded bracket annotations)
plus one additional structural reinforcement:
NON-OVERLAP DECLARATION gains a fourth statement covering CA-1.6 (CS-side: SHALL-F-EXT-CS2CS3
three-field structure) with bracket annotation `[CA-1.6: CS-side SHALL-F-EXT-CS2CS3 three-field
structure]`, explicitly naming CA-1.9 as its SE-side bilateral complement. This closes bilateral
symmetry at the NON-OVERLAP scope-declaration layer -- the same bilateral SE/CS pair declared in
Phase 0 (C-44) and echoed in Phase 3 mandate (C-45) now also appears at the scope-boundary layer.
Foreshadows C-47: NON-OVERLAP DECLARATION bilateral scope boundary completion.
**Hypothesis:** 38/38 (100.0). Architecture above v16 ceiling; likely C-47 surface.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

*(Identical to V-01.)*

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes
fully before the next begins. Execution order is self-attestable from phase labels alone.

**PHASE 0 -- CA:** *(Identical to V-01.)*

**PHASE 1 -- CS:** *(Identical to V-01.)*

**PHASE 2 -- SE:** *(Identical to V-01.)*

**PHASE 3 -- CA-1 (CA Verification Pass):**
CA returns. Phase 3 mandate carries complete CA-1.N audit-target scope roster followed by labeled
NON-OVERLAP DECLARATION block (named structural header; entries carry inline bracket annotations
per statement). CA-1.9 (SE-side: SHALL-D-EXT-C35 TABLE_4 row cross-reference) and CA-1.6
(CS-side: SHALL-F-EXT-CS2CS3 three-field structure) serve as co-equal named verification
obligations completing the bilateral parity declared in Phase 0. Each CA-1 row performs
double-anchor reaffirmation. CA-1.10 verifies bidirectional label-identity cross-scan. Terminal
verdict includes TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION and cites Phase 0 Artifact Manifest
by item counts.

---

## PHASE 0 -- CA

*(Identical to V-01.)*

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

**Bilateral verification pair:** CA-1.9 (SE-side: SHALL-D-EXT-C35 TABLE_4 row cross-reference) and
CA-1.6 (CS-side: SHALL-F-EXT-CS2CS3 three-field structure) serve as co-equal named verification
obligations completing the bilateral parity declared in Phase 0. Each side is independently
mandated and independently verified; completion of one does not substitute for the other.

**NON-OVERLAP DECLARATION:**
The following CA-1 rows have non-overlapping audit scopes. Each statement carries an inline
bracket annotation bounding the scope:

- The audit scope bounded by [CA-1.4: SE-0 execution ordering and four-vector TABLE_4 presence]
  is exclusively TABLE_4 appearing at SE-0 before SE-1; does not cover MANUAL GAP label format
  at SE-2/SE-3/SE-4 or SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference content.
- The audit scope bounded by [CA-1.7: MANUAL GAP exact-label blocks at SE-2/SE-3/SE-4 openings]
  is exclusively character-for-character label verification at SE-2, SE-3, SE-4 openings; does not
  cover SE-0 execution order or TABLE_4 row cross-reference inside SE-4's STRUCTURED CLOSE block.
- The audit scope bounded by [CA-1.9: SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference
  (SE-side bilateral sub-clause)]
  is exclusively the TABLE_4 row named inside SE-4's STRUCTURED CLOSE block; does not cover
  TABLE_4 execution order (CA-1.4) or MANUAL GAP label format (CA-1.7).
- The audit scope bounded by [CA-1.6: CS-side SHALL-F-EXT-CS2CS3 three-field structure]
  is exclusively CS-EXPECTATION-VIOLATED row completeness -- verifies CS-Expected row-ID citation,
  SE-Actual presence, and Delta specificity; this scope is the CS-side bilateral complement to the
  SE-side scope bounded by [CA-1.9: SE-4 STRUCTURED CLOSE TABLE_4 SE-0 slot cross-reference].

Non-overlap is structural: CA-1.9 and CA-1.6 are bilateral complements occupying distinct output
locations (SE-4 STRUCTURED CLOSE vs. TABLE_5 CS-EV rows) and distinct mechanism obligations
(SHALL-D-EXT-C35 vs. SHALL-F-EXT-CS2CS3). No output artifact is covered by more than one row.

*Each CA-1 row presents Registry anchor and Preamble anchor as structurally distinct labeled
elements before the Verification line.*

*(CA-1.1 through CA-1.10, CA Format Compliance Verdict, and TRI-DIMENSIONAL SELF-EVIDENCE
ATTESTATION identical to V-01.)*

---

## C-47 Candidate

**Pattern:** NON-OVERLAP DECLARATION bilateral scope boundary completion -- the sub-clause
verification row pair (CA-1.9 SE-side / CA-1.6 CS-side) each has a dedicated NON-OVERLAP scope
statement with inline bracket annotation, and each statement explicitly names the other as the
bilateral complement. This closes bilateral parity at the scope-declaration layer, paralleling:
- C-44 (Phase 0): bilateral *obligation* mandate (SHALL-D-EXT-C35 SE-side / SHALL-F-EXT-CS2CS3 CS-side co-declared)
- C-45 (Phase 3): bilateral *verification mandate* echo (CA-1.9 SE-side / CA-1.6 CS-side co-named)
- C-47 (NON-OVERLAP): bilateral *scope-boundary declaration* (CA-1.9 and CA-1.6 each bounding their scope AND naming the other as bilateral complement)

**Hangs off:** C-46 (per-statement bracket citations) + C-45 (Phase 3 bilateral verification echo).
The same bilateral pair that C-45 declares in the Phase 3 mandate is now also bounded symmetrically
in the NON-OVERLAP block -- closing the bilateral triangle's third leg.

**Pass condition (proposed):** NON-OVERLAP DECLARATION contains a dedicated statement for CA-1.6
(CS-side: SHALL-F-EXT-CS2CS3) carrying `[CA-1.6: scope-summary]` bracket annotation AND explicitly
naming CA-1.9 as its SE-side bilateral complement within the same statement. Reciprocally, the
CA-1.9 NON-OVERLAP statement (already present in C-46 passing form) either names CA-1.6 as the
CS-side complement OR the overall block declares bilateral symmetry. A NON-OVERLAP block with only
three SE-side statements (CA-1.4/CA-1.7/CA-1.9) without a CS-side CA-1.6 statement fails C-47
even if C-46 passes.
