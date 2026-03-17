# trace-permissions Variate — Round 18
**Date:** 2026-03-16
**Rubric:** v17 (C-01 through C-47)
**Session note:** R17-V-05 scored 100.0 (39/39) under v17 — four-statement NON-OVERLAP
DECLARATION adding CA-1.6 CS-side bilateral complement (C-47) produced the ceiling. R17-V-01
through V-04 scored 97.4 (38/39) each, failing only C-47.

**State entering Round 18:**

| Variation | v17 score | Notes |
|-----------|-----------|-------|
| R17-V-05 | 100.0 (39/39) | Passes all criteria including C-47 (four-statement NON-OVERLAP with CA-1.6 CS-side bilateral complement) |
| R17-V-01 through V-04 | 97.4 (38/39) | Fail C-47 only — three-statement NON-OVERLAP without CA-1.6 fourth statement |

**Path from R17:** All 39 criteria satisfied by R17-V-05. R18 explores new structural axes that
may surface C-48. All R18 variations start from R17-V-05 architecture (four-statement
NON-OVERLAP, Phase 0 bilateral mandate C-44, Phase 3 bilateral echo C-45).

---

## Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Single-axis: R17-V-05 architecture reproduced as R18 baseline — four-statement NON-OVERLAP DECLARATION (C-43+C-46+C-47), Phase 0 bilateral mandate (C-44), Phase 3 bilateral echo (C-45) | Confirms 39/39 ceiling holds in fresh R18 execution. Expected: 39/39 (100.0). |
| V-02 | Single-axis: CA Format Compliance Verdict bilateral echo — verdict citation names CA-1.9 (SE-side: SHALL-D-EXT-C35) and CA-1.6 (CS-side: SHALL-F-EXT-CS2CS3) as explicit bilateral sub-clause verification pair with side qualifiers | V-01 holds C-47. V-02 extends bilateral naming to the Verdict citation layer. Tests whether explicit bilateral pairing in the Verdict produces a new C-48 pattern. Expected: 39/39 or reveals new criterion. |
| V-03 | Single-axis: SHALL bilateral side-labeling — SHALL-D-EXT-C35 and SHALL-F-EXT-CS2CS3 carry explicit "(SE-side bilateral sub-clause, verified at CA-1.9)" and "(CS-side bilateral sub-clause, verified at CA-1.6)" labels within the Phase 0 SHALL obligation text | Tests whether bilateral labeling at the SHALL source-obligation layer (below the Phase 0 mandate paragraph of C-44) surfaces a new C-48 criterion. Expected: 39/39 or reveals new criterion. |
| V-04 | Combined: V-02 (Verdict bilateral echo) + V-03 (SHALL side-labeling) on V-01 base | Both Verdict and SHALL layers carry bilateral side labels simultaneously. If either axis independently surfaces a pattern, V-04 captures both. Expected: 39/39 or combined surfacing of new criteria. |
| V-05 | Maximum reinforcement: V-04 base + CEM bilateral sub-clause annotation — bilateral M4 extension note added after CEM table in Phase 0 Step 0.2, naming CA-1.9 (SE-side) and CA-1.6 (CS-side) as the bilateral M4 sub-clause pair co-declared alongside the CEM | Bilateral parity declared at every structural layer: SHALL declarations (V-03), CEM annotation (V-05 new), Phase 0 mandate (C-44), Phase 3 mandate (C-45), NON-OVERLAP statements (C-47), Verdict citation (V-02). Most likely to expose C-48 if one exists. Expected: 39/39; maximum structural reinforcement. |

---

## V-01 — Single-Axis: R17-V-05 Architecture as R18 Baseline

**Axis:** Complete reproduction of R17-V-05. Four-statement NON-OVERLAP DECLARATION: CA-1.4
[SE-0 ordering], CA-1.7 [MANUAL GAP labels], CA-1.9 [SE-side verbatim citation], CA-1.6
[CS-side three-field structure — bilateral complement to CA-1.9]. Phase 0 bilateral mandate
(C-44) and Phase 3 bilateral echo (C-45) present. All other elements identical to established
architecture from R13 forward.
**Hypothesis:** R17-V-05 satisfies all 39 criteria. Reproducing that architecture in R18
confirms the ceiling holds. Expected: 39/39 (100.0).

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

Manual security reviews of Dataverse environments routinely miss three failure scenarios this
trace is designed to surface:

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
entity-by-entity without evaluating the sharing rules that silently override those baselines. A
Private OWD on Case combined with a Power Automate-triggered sharing rule grants effective
org-wide read to users who satisfy the trigger condition — including low-trust service accounts
not intended to have broad case access.

CONTEXT BLIND SPOTS (input-level uncertainty):

| Label | Description | Impact |
|-------|-------------|--------|
| BS-U1 | Field inventory not described — sensitive fields per entity must be inferred from typical Dataverse deployments for {{topic}} | High |
| BS-U2 | Sharing rule list not provided — zero vs. multiple active rules cannot be determined without environment inspection | High |
| BS-U3 | Team structure not specified — owner vs. access teams and their membership control mechanism assumed from feature context | Medium |

---

## ROLE SEQUENCING MANDATE

This output executes in four explicitly labeled phases. Phase labels MUST appear as structural
section headers in the output body. Each phase completes fully before the next begins.
Execution order is self-attestable from phase labels alone.

**PHASE 0 — CA (Compliance Auditor):** CA executes first. Authors Schema Registry (Step 0.1:
seven table schemas declared centrally) and Criterion Enforcement Matrix preamble (Step 0.2:
SHALL obligations including two named sub-clauses declared with bilateral parity —
SHALL-D-EXT-C35 (SE-side: SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference, verified at
CA-1.9) and SHALL-F-EXT-CS2CS3 (CS-side: CS-EXPECTATION-VIOLATED three-field Remediation,
verified at CA-1.6) — CEM four-column mapping, STRUCTURAL AXIS NON-INTERFERENCE DECLARATION
with A-1/A-2/A-3 labeled rows and attestation cross-link mandate, M4 pre-assignments CA-1.1
through CA-1.9). CA issues handoff to PHASE 1 — SE.

**PHASE 1 — SE (Security Engineer / Dataverse Security Expert):** Executes second. Opens with
SE-0 (TABLE_4 escalation vectors before TABLE_1). Populates TABLE_1 through TABLE_5 using
Dataverse-native terminology. SE-2, SE-3, SE-4 each open with exact-label two-part closure
block per SHALL-G. SE-4 STRUCTURED CLOSE carries TABLE_4 row cross-reference per
SHALL-D-EXT-C35. SE populates SE-updatable columns in CS-2 and CS-3. Handoff to PHASE 2 — CS.

**PHASE 2 — CS (Customer Success):** Executes third. Opens with CS-0 (Schema Registry ID
citations for CS-2 and CS-3 before CS-1). Produces CS-1 qualitative baseline and expectation
tables CS-2 and CS-3 per SHALL-F-EXT-CS2CS3. Handoff to PHASE 3 — CA-1.

**PHASE 3 — CA-1 (CA Verification Pass):** CA returns. Phase 3 mandate carries complete CA-1.N
audit-target scope roster followed by labeled NON-OVERLAP DECLARATION block. Bilateral
sub-clause verification targets: CA-1.9 (SE-side: SHALL-D-EXT-C35 TABLE_4 row
cross-reference) and CA-1.6 (CS-side: SHALL-F-EXT-CS2CS3 three-field structure) serve as
co-equal named verification obligations completing the bilateral parity declared in Phase 0.
Each CA-1 row performs double-anchor reaffirmation (Registry anchor labeled, Preamble anchor
labeled, Verification statement following both). CA-1.9 is distinct from CA-1.4 and CA-1.7.
Terminal verdict includes TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION with A-N axis labels per
attestation cross-link mandate.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1 and 0.2 before any other phase begins.*

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

All table schemas declared centrally by CA. Blank-cell prohibition is global — individual tables
do not restate it. SE-update protocols for CS-2 and CS-3 declared co-located with schema entry.

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Tier values: Admin / Custom / Restricted. Rows ordered Admin first, Custom second, Restricted last.
Blank-cell rule: every cell MUST carry Granted / Denied / Conditional (condition inline) / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Blank-cell rule: FLS Profile Configured? = Configured / Not Configured. Gap? = YES / NO.

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Effective Scope values: Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
All four vectors (team inheritance / sharing rules / impersonation / admin-env-role) MUST appear.
Checked? = YES for all. Finding = escalation path or specific rule-out (never blank).
Note: TABLE_4 fills at SE-0, BEFORE TABLE_1 — the privilege ceiling is established first.

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation`
Remediation = exact configuration object + exact path + expected post-fix state. Generic text fails.
CS-EXPECTATION-VIOLATED Remediation: three-field block (CS-Expected / SE-Actual / Delta).

**Schema ID: CS-2 — Sharing Rule Expectations**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference (TABLE_4 row ID), SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE update protocol: populate after TABLE_4 at SE-0. CONTRADICTED triggers CS-EXPECTATION-VIOLATED per SHALL-F-EXT-CS2CS3.

**Schema ID: CS-3 — Cross-Role Access Differential Expectations**
Declared columns: `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference (TABLE_1 or TABLE_3 row ID), SE Confirmation.
SE update protocol: populate after TABLE_1 and TABLE_3 analysis. CONTRADICTED triggers CS-EXPECTATION-VIOLATED per SHALL-F-EXT-CS2CS3.

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: M1, M2, M3, M4 are simultaneously active — not alternative coverage paths. M4
CA verification row IDs pre-assigned by CA constitute pre-existing contract obligations fulfilled
as structural completions in Phase 3.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 + SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A: A complete TABLE_1 MUST be present. Every cell carries Granted / Denied / Conditional / N/A. Every role with any privilege on any entity in {{topic}} MUST appear, ordered by Tier.
- SHALL-B: TABLE_2 MUST list every field containing PII, Financial, or Audit-Compliance data with explicit FLS status. Null case MUST be explicitly stated with field list. All Gap? YES rows MUST appear in TABLE_5.
- SHALL-C: Every TABLE_1 role MUST appear in TABLE_3 with a filled Effective Scope. Ambiguous scope MUST appear in TABLE_5.
- SHALL-D: TABLE_4 MUST contain all four escalation vectors with Checked? = YES. A rule-out requires naming the specific mechanism and a specific reason no path exists. TABLE_4 fills at SE-0 before TABLE_1. SHALL-D extension sub-clause SHALL-D-EXT-C35: SE-4's STRUCTURED CLOSE block MUST contain a verbatim TABLE_4 row cross-reference in the format "Cite: TABLE_4 (filled at SE-0) row [ID] — [role] privilege ceiling: [pattern]". CA-1.9 verifies this sub-clause as a distinct audit target from CA-1.4.
- SHALL-E: TABLE_5 MUST contain at least one gap row with a named field, role, or rule. Zero gaps requires explicit evidence rows confirming what was checked.
- SHALL-F: When any CS-2 or CS-3 expectation conflicts with an SE finding, the conflict MUST be recorded in TABLE_5 as gap type CS-EXPECTATION-VIOLATED. SHALL-F extension sub-clause SHALL-F-EXT-CS2CS3: Each CS-EXPECTATION-VIOLATED row MUST carry all three Remediation fields — CS-Expected (citing the CS-2 or CS-3 row by ID), SE-Actual (the diverging SE finding), and Delta (exact configuration change to align SE-Actual to CS-Expected). A row missing any field MUST be reopened. CA-1.6 verifies this sub-clause; CA-1.6's preamble-anchor paragraph cites SHALL-F-EXT-CS2CS3 as the obligation it completes.
- SHALL-G: Each SE sub-section SE-2, SE-3, SE-4 opens with a two-part exact-label closure block. Line 1: `MANUAL GAP [<exact CONTEXT label>]:` where the label is character-for-character from the CONTEXT section (e.g., "Blind spot 1 — Post-incident FLS gap"). Line 2: description of what manual audits miss. Line 3: `STRUCTURED CLOSE:`. Line 4: which table closes the gap. Paraphrase or abbreviation of the CONTEXT label fails. CA-1.7 verifies exact labels.

**STRUCTURAL AXIS NON-INTERFERENCE DECLARATION**

The three R12 structural dimensions are orthogonal obligations. Each is independently mandated.

| Axis | Dimension | Criterion | Self-Evidence Mechanism |
|------|-----------|-----------|------------------------|
| A-1 | Execution order | C-31 | TABLE_4 fills at SE-0 section header, which precedes SE-1 in output body |
| A-2 | Closure-note format | C-32 | MANUAL GAP / STRUCTURED CLOSE exact labels at SE-2, SE-3, SE-4 openings |
| A-3 | CS self-reference | C-33 | CS-0 cites Schema Registry IDs for CS-2 and CS-3 before CS-1 content |

Non-interference rule: satisfying A-1 does not justify relaxing A-2 or A-3. These are
independently mandated obligations with distinct enforcement mechanisms and distinct CA-1.N
verification rows.

**Attestation cross-link mandate:** The TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION block in the
CA Format Compliance Verdict (Phase 3) MUST identify each R12 dimension by its axis label as
declared in this table (A-1, A-2, A-3). Attestation rows that identify dimensions only by
criterion number (C-31, C-32, C-33) or descriptive phrase without citing the corresponding A-N
axis label from this declaration VIOLATE the cross-link mandate and fail C-37.

*Handing to PHASE 1 — SE.*

---

## PHASE 1 — SE: Security Analysis

*SE uses Dataverse-native terminology throughout. Execution begins at SE-0.*

### SE-0 / SHALL-D — Escalation Vector Inventory (executes BEFORE SE-1)

TABLE_4 fills here, establishing the privilege ceiling before any TABLE_1 cell is populated.
SE-0 is an explicitly labeled sub-step. Handoff to SE-1 follows SE-0 completion.

**TABLE_4 — Escalation Vector Inventory** *(Schema Registry TABLE_4; all four vectors required)*

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Finding format for confirmed escalation: `[Role] -> [Mechanism: specific privilege name] -> [Elevated access achieved]`
Finding format for rule-out: "Checked [mechanism]: no path because [specific reason naming the exact configuration examined]."

After TABLE_4: populate SE Cross-Reference and SE Confirmation in CS-2 rows. CONTRADICTED entries
trigger CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F-EXT-CS2CS3.

*SE-0 complete — handing to SE-1.*

### SE-1 / SHALL-A — Role-Operation Matrix

**TABLE_1 — Role-Operation Matrix** *(Schema Registry TABLE_1; Tier column required; blank-cell rule global)*

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Include every role with any privilege on any entity in {{topic}}. Cross-reference CS-3's expected
access differential after the table — note rows that confirm CS expectations (with CS-3 row
reference) and rows that contradict (triggers CS-EXPECTATION-VIOLATED in TABLE_5 per
SHALL-F-EXT-CS2CS3).

**Cross-role differential analysis:** Compare the CS role against at least one more privileged
role for the same entity and operation. State whether the differential is expected (least
privilege satisfied) or anomalous, and why.

### SE-2 / SHALL-B — Field-Level Security Coverage

MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:
Column security profiles are not discoverable from the security roles UI; administrators learn of
missing FLS only after a data exposure reveals that a sensitive field was readable by an unintended
role.

STRUCTURED CLOSE:
TABLE_2 below enumerates every sensitive field in scope with explicit FLS status, surfacing
pre-event what the security roles UI conceals. All Not Configured sensitive fields forward to
TABLE_5 as MISSING-FLS.

**TABLE_2 — FLS Coverage** *(Schema Registry TABLE_2; blank-cell rule global)*

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Categories: PII / Financial / Audit-Compliance / Other-Sensitive.
Null case: "No column security profiles active on {{topic}}. Sensitive fields identified: [list]. All entered in TABLE_5 as MISSING-FLS."
Forward all Gap? YES rows to TABLE_5.

**Defense-in-depth layer check:** For at least one sensitive field, identify the enforcement
layer (1: environment/admin role, 2: security role + BU scope, 3: team membership, 4: column
security profile) where read or write access is effectively granted or denied. Explain why the
layer above does not override.

### SE-3 / SHALL-C — Record Access Scope

MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access produced by a security role
plus owner team membership plus OWD settings; spot-checking roles individually misses
team-accumulated privilege escalation.

STRUCTURED CLOSE:
TABLE_3 below maps effective scope for every role by recording the OWD baseline, the scope
modifier from team or role depth, and the resulting effective scope as a single traceable row,
making team-accumulated privilege visible in one place.

**TABLE_3 — Record Scope by Role** *(Schema Registry TABLE_3; blank-cell rule global)*

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role MUST appear. Scope Modifier: privilege depth, owner team membership, access
team, or sharing rule that changes the OWD baseline. Note any role where effective scope exceeds
role-only scope due to team membership — this is a CS-EXPECTATION-VIOLATED candidate.

After TABLE_3: populate SE Cross-Reference and SE Confirmation in CS-3 rows. CONTRADICTED entries
trigger CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F-EXT-CS2CS3.

### SE-4 / SHALL-D — Privilege Escalation Analysis

MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing sharing rules that
silently override them; a Private OWD combined with an active sharing rule grants effective
org-wide access without appearing in any security roles UI view.

STRUCTURED CLOSE:
TABLE_4 (filled at SE-0) surfaced escalation vectors before TABLE_1 was populated, establishing
the privilege ceiling first. CS-2 sharing rule expectations are confirmed or contradicted by SE
Cross-Reference and SE Confirmation columns after TABLE_4 analysis at SE-0.

[Cross-reference TABLE_4 (filled at SE-0). State: for each vector with a confirmed escalation
path, trace the path to its terminal access level. For each rule-out, confirm the specific
control that prevents the path at SE-0.]

After full escalation analysis:

MANUAL GAP close for SE-4 — TABLE_4 row cross-reference (SHALL-D-EXT-C35):

Cite: TABLE_4 (filled at SE-0) row [ID] — [role] privilege ceiling: [pattern]

This citation anchors the SE-4 STRUCTURED CLOSE to the specific TABLE_4 row established at SE-0.

### SE-5 / SHALL-E — Security Gap Inventory

**TABLE_5 — Security Gap Inventory** *(Schema Registry TABLE_5; blank-cell rule global)*

| # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation |
|---|----------|--------|---------------|------|------|----------|-------------|

Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.
Severity: CRITICAL / HIGH / MEDIUM.

Remediation specificity: name the exact object, exact path (Power Platform Admin Center
location), and expected post-fix state.

CS-EXPECTATION-VIOLATED rows (three-field Remediation block per SHALL-F-EXT-CS2CS3):
- CS-Expected: [cite CS-2 or CS-3 row by ID, state expectation verbatim or by row reference]
- SE-Actual: [SE finding that contradicts the expectation]
- Delta: [exact configuration change to align SE-Actual to CS-Expected]

*Handing to PHASE 2 — CS.*

---

## PHASE 2 — CS: Customer Success Analysis

*CS opens with CS-0. CS uses Schema Registry schemas for CS-2 and CS-3.*

### CS-0 — Schema Registry Acknowledgment (executes before CS-1)

Before producing any analysis content, CS cites the Schema Registry entries for CS-2 and CS-3
by exact Schema ID label and lists the SE-updatable columns for each:

- Schema ID: CS-2 — Sharing Rule Expectations. SE-updatable columns: SE Cross-Reference (TABLE_4 row ID), SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE). SE populates after TABLE_4 at SE-0.
- Schema ID: CS-3 — Cross-Role Access Differential Expectations. SE-updatable columns: SE Cross-Reference (TABLE_1 or TABLE_3 row ID), SE Confirmation. SE populates after TABLE_1/TABLE_3 analysis.

CS-0 confirms these Registry IDs govern the CS-2 and CS-3 tables below.

*CS-0 complete — proceeding to CS-1.*

### CS-1 — Qualitative Baseline

For each entity in {{topic}} scope:

(a) Which CRUD operations is the CS role expected to perform as part of normal job function?
(b) What is the expected record scope (own records / BU-wide / org-wide / team-scoped)?
(c) Which sensitive fields does CS need read or write access to, and why?
(d) Which configuration does CS rely on that may inadvertently open access beyond job requirements?

Name the business process at stake, at least two affected personas, and the expected access
pattern per persona. CS-1 findings are the expectation anchor for CS-EXPECTATION-VIOLATED gap type.

### CS-2 — Sharing Rule Expectations *(SE will populate SE Cross-Reference and SE Confirmation)*

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

For each Potential Overreach? YES: name the access path and the role most likely to be over-reached.

### CS-3 — Cross-Role Access Differential Expectations *(SE will populate SE Cross-Reference and SE Confirmation)*

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|-----------------------------|----------------------|---------------------|-----------------|

State at minimum one entity and one operation where CS should have less access than the
Comparison Role.

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

*CA returns. Phase 3 CA-1.N audit-target scope roster:*

| CA Row | Audit Target | Criterion | Non-Overlapping Scope |
|--------|-------------|-----------|----------------------|
| CA-1.1 | TABLE_1 completeness | C-01 | Role-operation matrix cell coverage and role enumeration |
| CA-1.2 | TABLE_2 FLS coverage | C-02 | Sensitive field FLS status and null-case declaration |
| CA-1.3 | TABLE_3 record scope | C-03 | Effective scope completeness for every TABLE_1 role |
| CA-1.4 | TABLE_4 SE-0 ordering | C-04 | SE-0 execution before SE-1 in output body; all four vectors present |
| CA-1.5 | TABLE_5 gap inventory | C-05 | Named gap with specific field/role/rule; remediation object/path/state |
| CA-1.6 | SHALL-F-EXT-CS2CS3 three-field structure | SHALL-F | CS-EXPECTATION-VIOLATED row completeness — CS-Expected/SE-Actual/Delta — only |
| CA-1.7 | MANUAL GAP exact labels | SHALL-G | Character-for-character CONTEXT label carry-through at SE-2, SE-3, SE-4 only |
| CA-1.8 | CS-0 Registry citation | C-33 | CS-0 presence before CS-1; Schema ID labels cited by exact string |
| CA-1.9 | SE-4 STRUCTURED CLOSE TABLE_4 cross-reference | SHALL-D-EXT-C35 | Verbatim TABLE_4 row reference in SE-4 close only — distinct from CA-1.4 and CA-1.7 |

NON-OVERLAP DECLARATION:
The audit scope bounded by [CA-1.4: SE-0 ordering and four-vector presence] is exclusively
whether TABLE_4 precedes TABLE_1 in the output body and whether all four vectors carry
Checked? = YES — this scope does not extend to label matching or verbatim citation format.
The audit scope bounded by [CA-1.7: MANUAL GAP exact-label match] is exclusively whether the
character-for-character CONTEXT label appears at SE-2, SE-3, SE-4 — this scope does not extend
to structural ordering or verbatim citation format.
The audit scope bounded by [CA-1.9: SE-4 STRUCTURED CLOSE verbatim row cross-reference] is
exclusively the "Cite: TABLE_4 (filled at SE-0) row [ID]" verbatim format in SE-4's STRUCTURED
CLOSE — this scope does not extend to ordering (bounded by [CA-1.4: SE-0 ordering]) or label
match (bounded by [CA-1.7: MANUAL GAP exact-label match]).
The audit scope bounded by [CA-1.6: CS-side SHALL-F-EXT-CS2CS3 three-field structure] is
exclusively CS-EXPECTATION-VIOLATED row completeness (CS-Expected / SE-Actual / Delta) — this
scope is the CS-side bilateral complement to the SE-side scope bounded by [CA-1.9:
SE-4 STRUCTURED CLOSE verbatim row cross-reference], and does not extend to structural ordering
(CA-1.4), label match (CA-1.7), or the SE-side verbatim citation check (CA-1.9).

Each CA-1 row MUST present Registry anchor and Preamble anchor as structurally distinct labeled
paragraphs before the Verification paragraph. Inline concatenation of anchors into a single
string fails C-24.

**CA-1.1 — C-01 verification** *(completing Phase 0 M4 pre-assignment CA-1.1)*:

Registry anchor — Schema ID TABLE_1: [Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope] — blank cells prohibited globally; Tier ordered Admin/Custom/Restricted.

Preamble anchor — C-01 as authored by CA in Phase 0: TABLE_1 / SE-1 / SHALL-A / CA-1.1 — verifying...

Verification — TABLE_1 present? Every cell Granted/Denied/Conditional/N/A? All roles with any privilege included? Tier column populated and ordered? -> PASS / FAIL

**CA-1.2 — C-02 verification** *(completing Phase 0 M4 pre-assignment CA-1.2)*:

Registry anchor — Schema ID TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?] — blank cells prohibited globally.

Preamble anchor — C-02 as authored by CA in Phase 0: TABLE_2 / SE-2 / SHALL-B / CA-1.2 — verifying...

Verification — TABLE_2 present? Every sensitive field with explicit FLS status? Null case stated with field list? Gap? YES rows in TABLE_5? -> PASS / FAIL

**CA-1.3 — C-03 verification** *(completing Phase 0 M4 pre-assignment CA-1.3)*:

Registry anchor — Schema ID TABLE_3: [Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Verified?] — blank cells prohibited globally.

Preamble anchor — C-03 as authored by CA in Phase 0: TABLE_3 / SE-1+SE-3 / SHALL-C / CA-1.3 — verifying...

Verification — Every TABLE_1 role in TABLE_3? Effective Scope filled for all? Ambiguous scope in TABLE_5? -> PASS / FAIL

**CA-1.4 — C-04 verification** *(completing Phase 0 M4 pre-assignment CA-1.4)*:

Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity] — all four vectors required; Checked? = YES; TABLE_4 fills at SE-0 before TABLE_1 per Registry note.

Preamble anchor — C-04 as authored by CA in Phase 0: TABLE_4 / SE-0+SE-4 / SHALL-D / CA-1.4 — verifying SE-0 ordering only; SE-4 cross-reference verified at CA-1.9...

Verification — TABLE_4 present? All four vectors with Checked? = YES? Each with finding or specific rule-out? TABLE_4 precedes TABLE_1 in output body (SE-0 before SE-1)? -> PASS / FAIL

**CA-1.5 — C-05 verification** *(completing Phase 0 M4 pre-assignment CA-1.5)*:

Registry anchor — Schema ID TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Tier, Severity, Remediation] — blank cells prohibited globally.

Preamble anchor — C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 — verifying...

Verification — TABLE_5 present? Named gap with specific field/role/rule? Remediations exact (object + path + post-fix state)? -> PASS / FAIL

**CA-1.6 — SHALL-F-EXT-CS2CS3 compliance verification** *(completing Phase 0 M4 pre-assignment CA-1.6)*:

Registry anchor — Schema ID TABLE_5 CS-EXPECTATION-VIOLATED row structure: [CS-Expected field citing CS-2/CS-3 row ID, SE-Actual field naming diverging SE finding, Delta field stating exact configuration change] — all three Remediation fields required per SHALL-F-EXT-CS2CS3; a row missing any field is structurally incomplete and MUST be reopened.

Preamble anchor — SHALL-F extended with sub-clause SHALL-F-EXT-CS2CS3 as authored by CA in Phase 0: CS-EXPECTATION-VIOLATED rows MUST carry CS-Expected (CS-2/CS-3 row citation) / SE-Actual (diverging SE finding) / Delta (exact config change). CA-1.6 completes the pre-assigned M4 obligation for SHALL-F-EXT-CS2CS3 — verifying...

Verification — For each CS-EXPECTATION-VIOLATED row in TABLE_5: CS-Expected populated with CS-2 or CS-3 row ID citation? SE-Actual populated with specific SE finding? Delta populated with exact configuration change? -> PASS / FAIL per row.

**CA-1.7 — SHALL-G compliance verification** *(MANUAL GAP exact-label two-part blocks)*:

Registry anchor — CONTEXT section declared exact labels: "Blind spot 1 — Post-incident FLS gap" (SE-2 target), "Blind spot 2 — Cumulative privilege blind spot" (SE-3 target), "Blind spot 3 — OWD-sharing-rule override gap" (SE-4 target). SHALL-G requires two-part blocks: `MANUAL GAP [<exact label>]:` then `STRUCTURED CLOSE:`.

Preamble anchor — SHALL-G as authored by CA in Phase 0: Line 1 MUST begin `MANUAL GAP [<exact CONTEXT label>]:` — character-for-character match; paraphrase or abbreviation fails — verifying...

Verification — SE-2 opens with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:`? SE-3 opens with `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:`? SE-4 opens with `MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:`? Each followed by `STRUCTURED CLOSE:`? -> PASS / FAIL per section.

**CA-1.8 — CS-0 Registry acknowledgment precedes CS-1** *(C-33 verification)*:

Registry anchor — Schema Registry declares CS-2 and CS-3 with Schema IDs "CS-2 — Sharing Rule Expectations" and "CS-3 — Cross-Role Access Differential Expectations", each with SE-updatable column declarations.

Preamble anchor — C-33 requires CS role to open with CS-0 citing Schema Registry IDs for CS-2 and CS-3 by exact label before any CS-1 content. CA-1.8 verifies CS-0 precedes CS-1 — verifying...

Verification — CS-0 section present as explicitly labeled sub-step? CS-0 quotes Schema ID: CS-2 and Schema ID: CS-3 by exact label? CS-0 appears before CS-1 content begins? -> PASS / FAIL

**CA-1.9 — SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference** *(completing Phase 0 M4 pre-assignment CA-1.9 — SHALL-D-EXT-C35; distinct audit target from CA-1.4 and CA-1.7)*:

Registry anchor — Schema ID TABLE_4 (filled at SE-0): [Vector, Checked?, Finding, Severity]. SE-4 STRUCTURED CLOSE MUST contain verbatim cross-reference format: "Cite: TABLE_4 (filled at SE-0) row [ID] — [role] privilege ceiling: [pattern]". This is distinct from SE-0 ordering (CA-1.4) and MANUAL GAP labels (CA-1.7).

Preamble anchor — SHALL-D extended with sub-clause SHALL-D-EXT-C35 as authored by CA in Phase 0: SE-4's STRUCTURED CLOSE MUST contain verbatim TABLE_4 row cross-reference. CA-1.9 completes the pre-assigned M4 obligation for SHALL-D-EXT-C35 — verifying...

Verification — SE-4 STRUCTURED CLOSE contains verbatim "Cite: TABLE_4 (filled at SE-0) row [ID]" format? Cross-reference names a specific TABLE_4 row ID and role privilege ceiling pattern? This cross-reference is structurally distinct from the SE-0 ordering check in CA-1.4 and the exact-label check in CA-1.7? -> PASS / FAIL

**CA Format Compliance Verdict (Phase 0 citation):**

Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0),
Phase 0 label as structural basis.

[C-01 through C-05: CA-1.1–CA-1.5 results. SHALL-F-EXT-CS2CS3 three-field structure: CA-1.6 result. SHALL-G exact-label blocks: CA-1.7 result. CS-0 Registry acknowledgment: CA-1.8 result. SE-4 STRUCTURED CLOSE cross-reference: CA-1.9 result. Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

**TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION**

Each R12 structural dimension is independently verifiable from the output body without consulting
prompt instructions. Axis labels match the STRUCTURAL AXIS NON-INTERFERENCE DECLARATION in
Phase 0 Step 0.2 per attestation cross-link mandate.

| Axis | Dimension (Criterion) | Output-Body Evidence Source | Status |
|------|-----------------------|-----------------------------|--------|
| A-1 | Execution order (C-31) | PHASE 1 section header "SE-0 / SHALL-D — Escalation Vector Inventory (executes BEFORE SE-1)" appears before "SE-1 / SHALL-A"; TABLE_4 rows precede TABLE_1 rows in output body | CONFIRMED |
| A-2 | Closure-note format (C-32) | SE-2, SE-3, SE-4 each open with verbatim "MANUAL GAP [...]:" / "STRUCTURED CLOSE:" two-part block; labels character-for-character match CONTEXT section entries | CONFIRMED |
| A-3 | CS self-reference (C-33) | PHASE 2 section header "CS-0 — Schema Registry Acknowledgment (executes before CS-1)" cites Schema ID: CS-2 and Schema ID: CS-3 by exact label before CS-1 content begins | CONFIRMED |

---

## V-02 — Single-Axis: CA Format Compliance Verdict Bilateral Echo

**Axis:** V-01 base with one change: the CA Format Compliance Verdict citation explicitly names
CA-1.9 (SE-side: SHALL-D-EXT-C35) and CA-1.6 (CS-side: SHALL-F-EXT-CS2CS3) as the bilateral
sub-clause verification pair with "(SE-side)" and "(CS-side)" qualifiers, and confirms bilateral
parity closure in a single verdict statement. All other elements identical to V-01.
**Hypothesis:** V-01 passes C-47 via four-statement NON-OVERLAP. V-02 tests whether the Verdict
citation layer requires bilateral echo parallel to Phase 0 mandate (C-44), Phase 3 mandate
(C-45), and NON-OVERLAP statement (C-47). Tests whether explicit bilateral pairing in the
Verdict produces a new C-48 pattern. Expected: 39/39 or reveals new criterion.

---

You are running a permissions trace signal for: {{topic}}

---

[CONTEXT section: identical to V-01]

[ROLE SEQUENCING MANDATE: identical to V-01 — Phase 0 bilateral mandate (C-44) present;
Phase 3 bilateral echo (C-45) present]

---

[PHASE 0 Steps 0.1 and 0.2: identical to V-01]

[PHASE 1 — SE: identical to V-01]

[PHASE 2 — CS: identical to V-01]

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification (V-02)

*CA returns. Phase 3 CA-1.N audit-target scope roster (V-02 — Verdict bilateral echo):*

[CA-1.N audit-target scope roster table: identical to V-01]

[NON-OVERLAP DECLARATION: identical to V-01 — all four statements including CA-1.6 CS-side
fourth statement (C-47) present]

[CA-1.1 through CA-1.9: identical to V-01]

**CA Format Compliance Verdict (Phase 0 citation) — V-02 bilateral echo:**

Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0),
Phase 0 label as structural basis.

[C-01 through C-05: CA-1.1–CA-1.5 results. Bilateral sub-clause verification pair — CA-1.9
(SE-side: SHALL-D-EXT-C35 SE-4 STRUCTURED CLOSE verbatim cross-reference) result and CA-1.6
(CS-side: SHALL-F-EXT-CS2CS3 CS-EXPECTATION-VIOLATED three-field structure) result; bilateral
parity declared in Phase 0 mandate and echoed in Phase 3 mandate and NON-OVERLAP DECLARATION
confirmed. SHALL-G exact-label blocks: CA-1.7 result. CS-0 Registry acknowledgment: CA-1.8
result. Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

[TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION: identical to V-01]

---

## V-03 — Single-Axis: SHALL Bilateral Side-Labeling at Phase 0 Obligation Text

**Axis:** V-01 base with one change: the SHALL-D-EXT-C35 and SHALL-F-EXT-CS2CS3 sub-clause
declarations in Phase 0 Step 0.2 carry explicit bilateral side labels — "(SE-side bilateral
sub-clause, verified at CA-1.9)" appended to SHALL-D-EXT-C35 and "(CS-side bilateral
sub-clause, verified at CA-1.6)" appended to SHALL-F-EXT-CS2CS3. The Verdict citation remains
as V-01 (no bilateral echo). All other elements identical to V-01.
**Hypothesis:** C-44 places bilateral side labels at the Phase 0 mandate paragraph level. V-03
tests whether bilateral labels are also required at the SHALL obligation declaration level —
specifically, whether the sub-clause declarations themselves must carry "(SE-side)" and
"(CS-side)" qualifiers as a distinct structural layer below the mandate paragraph. Tests whether
SHALL-level bilateral labeling produces a new C-48 criterion. Expected: 39/39 or reveals new
criterion.

---

You are running a permissions trace signal for: {{topic}}

---

[CONTEXT section: identical to V-01]

[ROLE SEQUENCING MANDATE: identical to V-01]

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE (V-03)

*CA executes Steps 0.1 and 0.2 before any other phase begins.*

[Step 0.1 — Schema Registry: identical to V-01]

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0) — V-03

[CEM declared rule and CEM table: identical to V-01]

**SHALL obligations (authored by CA, Phase 0) — V-03 SHALL bilateral side-labeling:**

- SHALL-A: [identical to V-01]
- SHALL-B: [identical to V-01]
- SHALL-C: [identical to V-01]
- SHALL-D: TABLE_4 MUST contain all four escalation vectors with Checked? = YES. A rule-out requires naming the specific mechanism and a specific reason no path exists. TABLE_4 fills at SE-0 before TABLE_1. SHALL-D extension sub-clause SHALL-D-EXT-C35 (SE-side bilateral sub-clause, verified at CA-1.9): SE-4's STRUCTURED CLOSE block MUST contain a verbatim TABLE_4 row cross-reference in the format "Cite: TABLE_4 (filled at SE-0) row [ID] — [role] privilege ceiling: [pattern]". CA-1.9 verifies this sub-clause as a distinct audit target from CA-1.4.
- SHALL-E: [identical to V-01]
- SHALL-F: When any CS-2 or CS-3 expectation conflicts with an SE finding, the conflict MUST be recorded in TABLE_5 as gap type CS-EXPECTATION-VIOLATED. SHALL-F extension sub-clause SHALL-F-EXT-CS2CS3 (CS-side bilateral sub-clause, verified at CA-1.6): Each CS-EXPECTATION-VIOLATED row MUST carry all three Remediation fields — CS-Expected (citing the CS-2 or CS-3 row by ID), SE-Actual (the diverging SE finding), and Delta (exact configuration change to align SE-Actual to CS-Expected). A row missing any field MUST be reopened. CA-1.6 verifies this sub-clause; CA-1.6's preamble-anchor paragraph cites SHALL-F-EXT-CS2CS3 as the obligation it completes.
- SHALL-G: [identical to V-01]

[STRUCTURAL AXIS NON-INTERFERENCE DECLARATION: identical to V-01]

[PHASE 1 — SE: identical to V-01]

[PHASE 2 — CS: identical to V-01]

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification (V-03)

*CA returns. Phase 3 CA-1.N audit-target scope roster (V-03 — SHALL bilateral side-labeling):*

[CA-1.N audit-target scope roster table: identical to V-01]

[NON-OVERLAP DECLARATION: identical to V-01 — all four statements including CA-1.6 CS-side
fourth statement (C-47) present]

[CA-1.1 through CA-1.9: identical to V-01]

[CA Format Compliance Verdict: identical to V-01 — no bilateral echo in Verdict]

[TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION: identical to V-01]

---

## V-04 — Combined: V-02 (Verdict Bilateral Echo) + V-03 (SHALL Side-Labeling)

**Axis:** Two independent single-axis innovations applied simultaneously: (V-02) CA Format
Compliance Verdict citation explicitly names CA-1.9 (SE-side) and CA-1.6 (CS-side) as the
bilateral sub-clause verification pair with bilateral parity confirmation statement; (V-03)
SHALL-D-EXT-C35 and SHALL-F-EXT-CS2CS3 declarations carry "(SE-side bilateral sub-clause,
verified at CA-1.9)" and "(CS-side bilateral sub-clause, verified at CA-1.6)" labels in Phase 0
Step 0.2 SHALL obligation text. V-01 base otherwise (four-statement NON-OVERLAP, C-44, C-45,
C-47 all present).
**Hypothesis:** V-02 and V-03 are structurally independent axes — Verdict citation layer and
SHALL declaration layer do not interfere. If either independently surfaces a new criterion, V-04
captures both simultaneously. Expected: 39/39 or combined surfacing of new criteria if one or
both axes activate a C-48 pattern.

---

You are running a permissions trace signal for: {{topic}}

---

[CONTEXT section: identical to V-01]

[ROLE SEQUENCING MANDATE: identical to V-01]

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE (V-04)

[Step 0.1 — Schema Registry: identical to V-01]

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0) — V-04

[CEM declared rule and CEM table: identical to V-01]

**SHALL obligations (authored by CA, Phase 0) — V-04 SHALL bilateral side-labeling:**

- SHALL-A through SHALL-C: [identical to V-01]
- SHALL-D: TABLE_4 MUST contain all four escalation vectors with Checked? = YES. A rule-out requires naming the specific mechanism and a specific reason no path exists. TABLE_4 fills at SE-0 before TABLE_1. SHALL-D extension sub-clause SHALL-D-EXT-C35 (SE-side bilateral sub-clause, verified at CA-1.9): SE-4's STRUCTURED CLOSE block MUST contain a verbatim TABLE_4 row cross-reference in the format "Cite: TABLE_4 (filled at SE-0) row [ID] — [role] privilege ceiling: [pattern]". CA-1.9 verifies this sub-clause as a distinct audit target from CA-1.4.
- SHALL-E: [identical to V-01]
- SHALL-F: When any CS-2 or CS-3 expectation conflicts with an SE finding, the conflict MUST be recorded in TABLE_5 as gap type CS-EXPECTATION-VIOLATED. SHALL-F extension sub-clause SHALL-F-EXT-CS2CS3 (CS-side bilateral sub-clause, verified at CA-1.6): Each CS-EXPECTATION-VIOLATED row MUST carry all three Remediation fields — CS-Expected (citing the CS-2 or CS-3 row by ID), SE-Actual (the diverging SE finding), and Delta (exact configuration change to align SE-Actual to CS-Expected). A row missing any field MUST be reopened. CA-1.6 verifies this sub-clause; CA-1.6's preamble-anchor paragraph cites SHALL-F-EXT-CS2CS3 as the obligation it completes.
- SHALL-G: [identical to V-01]

[STRUCTURAL AXIS NON-INTERFERENCE DECLARATION: identical to V-01]

[PHASE 1 — SE: identical to V-01]

[PHASE 2 — CS: identical to V-01]

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification (V-04)

*CA returns. Phase 3 CA-1.N audit-target scope roster (V-04 — combined SHALL side-labeling
+ Verdict bilateral echo):*

[CA-1.N audit-target scope roster table: identical to V-01]

[NON-OVERLAP DECLARATION: identical to V-01 — all four statements including CA-1.6 CS-side
fourth statement (C-47) present]

[CA-1.1 through CA-1.9: identical to V-01]

**CA Format Compliance Verdict (Phase 0 citation) — V-04 bilateral echo:**

Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0),
Phase 0 label as structural basis.

[C-01 through C-05: CA-1.1–CA-1.5 results. Bilateral sub-clause verification pair — CA-1.9
(SE-side: SHALL-D-EXT-C35 SE-4 STRUCTURED CLOSE verbatim cross-reference) result and CA-1.6
(CS-side: SHALL-F-EXT-CS2CS3 CS-EXPECTATION-VIOLATED three-field structure) result; bilateral
parity declared in Phase 0 mandate and echoed in Phase 3 mandate and NON-OVERLAP DECLARATION
confirmed. SHALL-G exact-label blocks: CA-1.7 result. CS-0 Registry acknowledgment: CA-1.8
result. Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

[TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION: identical to V-01]

---

## V-05 — Maximum Reinforcement: V-04 + CEM Bilateral Sub-Clause Annotation

**Axis:** V-04 base (SHALL bilateral side-labeling + Verdict bilateral echo) extended with a
CEM bilateral sub-clause annotation block added immediately after the CEM table in Phase 0
Step 0.2. The annotation explicitly registers CA-1.9 and CA-1.6 as the bilateral M4 sub-clause
pair alongside the CEM, using "(SE-side bilateral sub-clause)" and "(CS-side bilateral
sub-clause)" labels. This makes bilateral parity visible at the CEM layer — parallel to how it
is declared at the SHALL declaration layer (V-03), the Phase 0 mandate paragraph (C-44), the
Phase 3 mandate (C-45), the NON-OVERLAP statements (C-47), and the Verdict citation (V-02).
**Hypothesis:** V-04 satisfies all 39 criteria plus both new single-axis extensions. V-05
tests whether bilateral symmetry at the CEM table layer (directly alongside the M1-M4 mapping)
surfaces yet another criterion — specifically whether a C-48 requires the CEM to register the
bilateral sub-clause pair as M4 extensions co-declared with the five CEM rows. Expected: 39/39;
most likely to expose C-48 if one exists.

---

You are running a permissions trace signal for: {{topic}}

---

[CONTEXT section: identical to V-01]

[ROLE SEQUENCING MANDATE: identical to V-01]

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE (V-05)

[Step 0.1 — Schema Registry: identical to V-01]

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0) — V-05

**Declared rule: M1, M2, M3, M4 are simultaneously active — not alternative coverage paths. M4
CA verification row IDs pre-assigned by CA constitute pre-existing contract obligations fulfilled
as structural completions in Phase 3.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 + SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**Bilateral sub-clause M4 extensions (co-declared alongside CEM, Phase 0):**
- SHALL-D-EXT-C35 (SE-side bilateral sub-clause) -> M4: CA-1.9 — distinct from CA-1.4; co-declared with SHALL-F-EXT-CS2CS3 as bilateral pair.
- SHALL-F-EXT-CS2CS3 (CS-side bilateral sub-clause) -> M4: CA-1.6 — distinct from CA-1.5; co-declared with SHALL-D-EXT-C35 as bilateral pair.
These two M4 sub-clause assignments constitute the bilateral parity pair (SE-side: CA-1.9 /
CS-side: CA-1.6) first established by the Phase 0 mandate bilateral sub-clause declaration and
independently verified in Phase 3 as co-equal named obligations.

**SHALL obligations (authored by CA, Phase 0) — V-05 SHALL bilateral side-labeling:**

- SHALL-A through SHALL-C: [identical to V-01]
- SHALL-D: TABLE_4 MUST contain all four escalation vectors with Checked? = YES. A rule-out requires naming the specific mechanism and a specific reason no path exists. TABLE_4 fills at SE-0 before TABLE_1. SHALL-D extension sub-clause SHALL-D-EXT-C35 (SE-side bilateral sub-clause, verified at CA-1.9): SE-4's STRUCTURED CLOSE block MUST contain a verbatim TABLE_4 row cross-reference in the format "Cite: TABLE_4 (filled at SE-0) row [ID] — [role] privilege ceiling: [pattern]". CA-1.9 verifies this sub-clause as a distinct audit target from CA-1.4.
- SHALL-E: [identical to V-01]
- SHALL-F: When any CS-2 or CS-3 expectation conflicts with an SE finding, the conflict MUST be recorded in TABLE_5 as gap type CS-EXPECTATION-VIOLATED. SHALL-F extension sub-clause SHALL-F-EXT-CS2CS3 (CS-side bilateral sub-clause, verified at CA-1.6): Each CS-EXPECTATION-VIOLATED row MUST carry all three Remediation fields — CS-Expected (citing the CS-2 or CS-3 row by ID), SE-Actual (the diverging SE finding), and Delta (exact configuration change to align SE-Actual to CS-Expected). A row missing any field MUST be reopened. CA-1.6 verifies this sub-clause; CA-1.6's preamble-anchor paragraph cites SHALL-F-EXT-CS2CS3 as the obligation it completes.
- SHALL-G: [identical to V-01]

[STRUCTURAL AXIS NON-INTERFERENCE DECLARATION: identical to V-01]

[PHASE 1 — SE: identical to V-01]

[PHASE 2 — CS: identical to V-01]

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification (V-05)

*CA returns. Phase 3 CA-1.N audit-target scope roster (V-05 — maximum reinforcement: SHALL
bilateral side-labeling + CEM bilateral M4 annotation + Verdict bilateral echo):*

[CA-1.N audit-target scope roster table: identical to V-01]

[NON-OVERLAP DECLARATION: identical to V-01 — all four statements including CA-1.6 CS-side
fourth statement (C-47) present]

[CA-1.1 through CA-1.9: identical to V-01]

**CA Format Compliance Verdict (Phase 0 citation) — V-05 bilateral echo:**

Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0),
Phase 0 label as structural basis.

[C-01 through C-05: CA-1.1–CA-1.5 results. Bilateral sub-clause verification pair — CA-1.9
(SE-side: SHALL-D-EXT-C35 SE-4 STRUCTURED CLOSE verbatim cross-reference) result and CA-1.6
(CS-side: SHALL-F-EXT-CS2CS3 CS-EXPECTATION-VIOLATED three-field structure) result; bilateral
parity declared in Phase 0 (SHALL declarations, CEM bilateral annotation, mandate sub-clause)
and echoed in Phase 3 mandate and NON-OVERLAP DECLARATION confirmed. SHALL-G exact-label blocks:
CA-1.7 result. CS-0 Registry acknowledgment: CA-1.8 result. Overall: COMPLIANT / NON-COMPLIANT.
Open items attributed to responsible role.]

[TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION: identical to V-01]
