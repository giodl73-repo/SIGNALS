# trace-permissions Variate — Round 19
**Date:** 2026-03-17
**Rubric:** v12 (C-01 through C-36)
**Session note:** R12-V-05 scored 98.9 (25/28) under v12 — V-05's full C-31+C-32+C-33
architecture activates all prerequisites but lacks the three binding declarations that convert
empirical composability into contractual obligations: no preamble axis non-interference
declaration (C-34), no CA-1.9 targeting SE-4's STRUCTURED CLOSE TABLE_4 cross-reference (C-35),
no tri-dimensional self-evidence attestation in the CA terminal verdict (C-36).

**State entering Round 19:**

| Variation | v12 score | Notes |
|-----------|-----------|-------|
| R12-V-05 | 98.9 (25/28) | Passes C-31/C-32/C-33; fails C-34/C-35/C-36 (no axis declaration, no CA-1.9, no tri-dimensional attestation) |
| R12-V-02 | 98.6 (24/28) | Missing C-32 blocks all three new criteria |
| R12-V-01 | 98.2 (23/28) | Missing C-31+C-33 blocks C-34/C-35/C-36 |
| R12-V-03 | 97.9 (22/28) | C-31/C-32/C-33 deps unmet |
| R12-V-04 | 97.9 (22/28) | C-31/C-32/C-33 deps unmet |

**Path from R12:** All three new criteria have clear prerequisites satisfied by R12-V-05.
R19 explores the three independent addition axes (C-34 alone, C-35 alone, C-36 alone) then
combines them. All R19 variations start from R12-V-05 architecture (SE-0 descent C-31,
exact-label two-part blocks C-32, CS-0 acknowledgment C-33).

---

## Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Single-axis: Preamble Structural Axis Non-Interference Declaration (C-34) — add explicit orthogonal-dimension block to preamble, naming C-31/C-32/C-33 with per-axis non-interference statements | R12-V-05 has all prerequisites (C-31+C-32+C-33+C-17). V-01 adds the declaration. Expected: 26/28 (98.9 + 0.36 = 99.2 if scoring holds). |
| V-02 | Single-axis: SE-4 STRUCTURED CLOSE verbatim TABLE_4 row cross-reference + CA-1.9 (C-35) — add SHALL-D-EXT-C35 sub-clause, SE-4 verbatim Cite: format, CA-1.9 row distinct from CA-1.4 and CA-1.7 | R12-V-05 has prerequisites (C-31+C-32). V-02 adds the STRUCTURED CLOSE verbatim citation and a dedicated CA-1 row. Expected: 26/28. |
| V-03 | Single-axis: Tri-Dimensional Self-Evidence Attestation in CA terminal verdict (C-36) — add attestation cross-link mandate in Phase 0 and TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION table in verdict | R12-V-05 has prerequisites (C-22+C-32+C-33). V-03 adds the attestation block with per-axis output-body evidence sources named. Expected: 26/28. |
| V-04 | Combined: V-01 (C-34) + V-02 (C-35) — preamble axis declaration AND SE-4 STRUCTURED CLOSE + CA-1.9, neither alone | Tests whether C-34 and C-35 compose without interference. Expected: 27/28. |
| V-05 | Full: V-01 (C-34) + V-02 (C-35) + V-03 (C-36) — complete 28/28 attempt | All three new mechanisms simultaneously active. V-06 from path-to-100 analysis. Expected: 28/28 (100.0). |

---

## V-01 — Single-Axis: Preamble Structural Axis Non-Interference Declaration (C-34)

**Axis:** R12-V-05 base with one structural addition: a STRUCTURAL AXIS NON-INTERFERENCE
DECLARATION block inserted in Phase 0 Step 0.2 (preamble), after the CEM table and SHALL
obligations, naming C-31/C-32/C-33 as three orthogonal structural dimensions with an explicit
per-axis non-interference statement. No changes to SE-4 STRUCTURED CLOSE format, no CA-1.9
row, no tri-dimensional attestation in terminal verdict.
**Hypothesis:** V-01 adds the declaration that converts V-05's empirical composability into a
preamble-level binding contract. Expected: passes C-34; fails C-35 (no CA-1.9) and C-36 (no
tri-dimensional attestation). Score: 26/28.

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
| BS-U1 | Field inventory not described — sensitive fields per entity inferred from typical Dataverse deployments for {{topic}} | High |
| BS-U2 | Sharing rule list not provided — zero vs. multiple active rules cannot be determined without environment inspection | High |
| BS-U3 | Team structure not specified — owner vs. access teams and membership control assumed from feature context | Medium |

---

## ROLE SEQUENCING MANDATE

This output executes in four explicitly labeled phases. Phase labels MUST appear as structural
section headers in the output body. Each phase completes fully before the next begins.
Execution order is self-attestable from phase labels alone.

**PHASE 0 — CA (Compliance Auditor):** CA executes first. Authors Schema Registry (Step 0.1:
seven table schemas declared centrally) and Criterion Enforcement Matrix preamble (Step 0.2:
SHALL obligations, CEM four-column mapping, STRUCTURAL AXIS NON-INTERFERENCE DECLARATION with
A-1/A-2/A-3 labeled rows, M4 pre-assignments CA-1.1 through CA-1.8). CA issues handoff to
PHASE 1 — SE.

**PHASE 1 — SE (Security Engineer / Dataverse Security Expert):** Executes second. Opens with
SE-0 (TABLE_4 escalation vectors before TABLE_1). Populates TABLE_1 through TABLE_5 using
Dataverse-native terminology. SE-2, SE-3, SE-4 each open with exact-label two-part closure
block per SHALL-G. SE populates SE-updatable columns in CS-2 and CS-3. Handoff to PHASE 2 — CS.

**PHASE 2 — CS (Customer Success):** Executes third. Opens with CS-0 (Schema Registry ID
citations for CS-2 and CS-3 before CS-1). Produces CS-1 qualitative baseline and expectation
tables CS-2 and CS-3. Handoff to PHASE 3 — CA-1.

**PHASE 3 — CA-1 (CA Verification Pass):** CA returns. CA-1.N audit-target scope roster
followed by NON-OVERLAP DECLARATION. Each CA-1 row performs double-anchor reaffirmation
(Registry anchor labeled, Preamble anchor labeled, Verification statement following both).
Terminal verdict cites CA-authored Registry and preamble.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1 and 0.2 before any other phase begins.*

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

All table schemas declared centrally by CA. Blank-cell prohibition is global.

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
Remediation = exact configuration object + exact path + expected post-fix state.
CS-EXPECTATION-VIOLATED Remediation: three-field block (CS-Expected / SE-Actual / Delta).

**Schema ID: CS-2 — Sharing Rule Expectations**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference (TABLE_4 row ID), SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE update protocol: populate after TABLE_4 at SE-0.

**Schema ID: CS-3 — Cross-Role Access Differential Expectations**
Declared columns: `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference (TABLE_1 or TABLE_3 row ID), SE Confirmation.
SE update protocol: populate after TABLE_1 and TABLE_3 analysis.

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
- SHALL-D: TABLE_4 MUST contain all four escalation vectors with Checked? = YES. A rule-out requires naming the specific mechanism and a specific reason no path exists. TABLE_4 fills at SE-0 before TABLE_1.
- SHALL-E: TABLE_5 MUST contain at least one gap row with a named field, role, or rule. Zero gaps requires explicit evidence rows confirming what was checked.
- SHALL-F: When any CS-2 or CS-3 expectation conflicts with an SE finding, the conflict MUST be recorded in TABLE_5 as gap type CS-EXPECTATION-VIOLATED with three-field Remediation block: CS-Expected (citing the CS-2 or CS-3 row by ID) / SE-Actual (the diverging SE finding) / Delta (exact configuration change). A row missing any field MUST be reopened.
- SHALL-G: Each SE sub-section SE-2, SE-3, SE-4 opens with a two-part exact-label closure block. Line 1: `MANUAL GAP [<exact CONTEXT label>]:` where the label is character-for-character from the CONTEXT section. Line 2: failure-mode description. Line 3: `STRUCTURED CLOSE:`. Line 4: which table closes the gap. Paraphrase or abbreviation of the CONTEXT label fails. CA-1.7 verifies exact labels.

**STRUCTURAL AXIS NON-INTERFERENCE DECLARATION** *(V-01 addition — C-34)*

The three R12 structural dimensions are orthogonal obligations. Each is independently mandated
and activating one does not constrain or relax the others.

| Axis | Dimension | Criterion | Self-Evidence Mechanism | Non-Interference Statement |
|------|-----------|-----------|------------------------|---------------------------|
| A-1 | Execution order | C-31 | TABLE_4 fills at SE-0 section header, which precedes SE-1 in output body | Satisfying A-1 (SE-0 ordering) does not justify relaxing A-2 or A-3 |
| A-2 | Closure-note format | C-32 | MANUAL GAP [...] / STRUCTURED CLOSE exact-label two-part blocks at SE-2, SE-3, SE-4 | Satisfying A-2 (two-part blocks) does not justify relaxing A-1 or A-3 |
| A-3 | CS self-reference | C-33 | CS-0 cites Schema Registry IDs for CS-2 and CS-3 by exact label before CS-1 | Satisfying A-3 (CS-0 acknowledgment) does not justify relaxing A-1 or A-2 |

These axes share no mechanism overlap. CA-1.4 verifies A-1; CA-1.7 verifies A-2; CA-1.8
verifies A-3. Each axis has a distinct, non-overlapping CA-1 audit target.

*Handing to PHASE 1 — SE.*

---

## PHASE 1 — SE: Security Analysis

*SE uses Dataverse-native terminology throughout. Execution begins at SE-0.*

### SE-0 / SHALL-D — Escalation Vector Inventory (executes BEFORE SE-1)

TABLE_4 fills here, establishing the privilege ceiling before any TABLE_1 cell is populated.

**TABLE_4 — Escalation Vector Inventory** *(Schema Registry TABLE_4; all four vectors required)*

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Finding format for confirmed escalation: `[Role] -> [Mechanism: specific privilege name] -> [Elevated access achieved]`
Finding format for rule-out: "Checked [mechanism]: no path because [specific reason naming the exact configuration examined]."

After TABLE_4: populate SE Cross-Reference and SE Confirmation in CS-2 rows.

*SE-0 complete — handing to SE-1.*

### SE-1 / SHALL-A — Role-Operation Matrix

**TABLE_1 — Role-Operation Matrix** *(Schema Registry TABLE_1; Tier column required)*

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Include every role with any privilege on any entity in {{topic}}. After the table, cross-reference
CS-3's expected access differential — note rows that confirm expectations (with CS-3 row ref)
and rows that contradict (triggers CS-EXPECTATION-VIOLATED in TABLE_5).

**Cross-role differential analysis:** Compare the CS role against at least one more privileged
role for the same entity and operation. State whether the differential is expected or anomalous.

### SE-2 / SHALL-B — Field-Level Security Coverage

MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:
Column security profiles are not discoverable from the security roles UI; administrators learn
of missing FLS only after a data exposure reveals that a sensitive field was readable by an
unintended role.

STRUCTURED CLOSE:
TABLE_2 below enumerates every sensitive field in scope with explicit FLS status, surfacing
pre-event what the security roles UI conceals. All Not Configured sensitive fields forward to
TABLE_5 as MISSING-FLS.

**TABLE_2 — FLS Coverage** *(Schema Registry TABLE_2)*

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Null case: "No column security profiles active on {{topic}}. Sensitive fields identified: [list]. All entered in TABLE_5 as MISSING-FLS."
Forward all Gap? YES rows to TABLE_5.

**Defense-in-depth layer check:** For at least one sensitive field, identify the enforcement
layer (1: environment/admin role, 2: security role + BU scope, 3: team membership, 4: column
security profile) where read or write access is effectively granted or denied.

### SE-3 / SHALL-C — Record Access Scope

MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access produced by security role
plus owner team membership plus OWD; spot-checking individual roles misses team-accumulated
privilege escalation.

STRUCTURED CLOSE:
TABLE_3 below maps effective scope for every role by recording the OWD baseline, scope modifier
from team or role depth, and resulting effective scope in one traceable row.

**TABLE_3 — Record Scope by Role** *(Schema Registry TABLE_3)*

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role MUST appear. Note any role where effective scope exceeds role-only scope due
to team membership — this is a CS-EXPECTATION-VIOLATED candidate.

After TABLE_3: populate SE Cross-Reference and SE Confirmation in CS-3 rows.

### SE-4 / SHALL-D — Privilege Escalation Analysis

MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing sharing rules that
silently override them; a Private OWD combined with an active sharing rule grants effective
org-wide access without appearing in any security roles UI view.

STRUCTURED CLOSE:
TABLE_4 (filled at SE-0) surfaced escalation vectors before TABLE_1 was populated, establishing
the privilege ceiling first. CS-2 sharing rule expectations are confirmed or contradicted by
SE Cross-Reference and SE Confirmation columns after TABLE_4 analysis at SE-0.

[Cross-reference TABLE_4 (filled at SE-0). For each vector with a confirmed escalation path,
trace the path to its terminal access level. For each rule-out, confirm the specific control
that prevents the path.]

### SE-5 / SHALL-E — Security Gap Inventory

**TABLE_5 — Security Gap Inventory** *(Schema Registry TABLE_5)*

| # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation |
|---|----------|--------|---------------|------|------|----------|-------------|

Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.
CS-EXPECTATION-VIOLATED rows require three-field Remediation (CS-Expected / SE-Actual / Delta).
Remediation specificity: name exact object, exact path, expected post-fix state.

*Handing to PHASE 2 — CS.*

---

## PHASE 2 — CS: Customer Success Analysis

*CS opens with CS-0. CS uses Schema Registry schemas for CS-2 and CS-3.*

### CS-0 — Schema Registry Acknowledgment (executes before CS-1)

Before producing any analysis content, CS cites the Schema Registry entries for CS-2 and CS-3
by exact Schema ID label and lists the SE-updatable columns for each:

- Schema ID: CS-2 — Sharing Rule Expectations. SE-updatable columns: SE Cross-Reference (TABLE_4 row ID), SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
- Schema ID: CS-3 — Cross-Role Access Differential Expectations. SE-updatable columns: SE Cross-Reference (TABLE_1 or TABLE_3 row ID), SE Confirmation.

CS-0 confirms these Registry IDs govern the CS-2 and CS-3 tables below.

*CS-0 complete — proceeding to CS-1.*

### CS-1 — Qualitative Baseline

For each entity in {{topic}} scope: (a) Which CRUD operations is the CS role expected to
perform? (b) What is the expected record scope? (c) Which sensitive fields does CS need access
to, and why? (d) Which configuration may inadvertently open access beyond job requirements?

Name the business process at stake, at least two affected personas, and the expected access
pattern per persona.

### CS-2 — Sharing Rule Expectations *(SE will populate SE Cross-Reference and SE Confirmation)*

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

### CS-3 — Cross-Role Access Differential Expectations *(SE will populate SE Cross-Reference and SE Confirmation)*

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|-----------------------------|----------------------|---------------------|-----------------|

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

*CA returns. Phase 3 CA-1.N audit-target scope roster:*

| CA Row | Audit Target | Criterion | Non-Overlapping Scope |
|--------|-------------|-----------|----------------------|
| CA-1.1 | TABLE_1 completeness | C-01 | Role-operation matrix cell coverage and role enumeration |
| CA-1.2 | TABLE_2 FLS coverage | C-02 | Sensitive field FLS status and null-case declaration |
| CA-1.3 | TABLE_3 record scope | C-03 | Effective scope completeness for every TABLE_1 role |
| CA-1.4 | TABLE_4 SE-0 ordering | C-04 | SE-0 execution before SE-1; all four vectors present with Checked? = YES |
| CA-1.5 | TABLE_5 gap inventory | C-05 | Named gap with specific field/role/rule; exact remediation |
| CA-1.6 | SHALL-F CS-EXPECTATION-VIOLATED structure | SHALL-F | Three-field Remediation completeness (CS-Expected/SE-Actual/Delta) only |
| CA-1.7 | MANUAL GAP exact labels | SHALL-G | Character-for-character CONTEXT label carry-through at SE-2, SE-3, SE-4 only |
| CA-1.8 | CS-0 Registry citation | C-33 | CS-0 presence before CS-1; Schema ID labels cited by exact string |

NON-OVERLAP DECLARATION:
The audit scope bounded by [CA-1.4: SE-0 ordering and four-vector presence] is exclusively
whether TABLE_4 precedes TABLE_1 in the output body and whether all four vectors carry
Checked? = YES — this scope does not extend to label matching or verbatim citation format.
The audit scope bounded by [CA-1.7: MANUAL GAP exact-label match] is exclusively whether the
character-for-character CONTEXT label appears at SE-2, SE-3, SE-4 — this scope does not extend
to structural ordering or verbatim citation format.
The audit scope bounded by [CA-1.6: CS-EXPECTATION-VIOLATED three-field structure] is
exclusively the Remediation field completeness for CS-EXPECTATION-VIOLATED rows — this scope
does not extend to structural ordering (CA-1.4) or label matching (CA-1.7).

Each CA-1 row MUST present Registry anchor and Preamble anchor as structurally distinct labeled
paragraphs before the Verification paragraph. Inline concatenation of anchors fails C-24.

**CA-1.1 — C-01 verification** *(completing Phase 0 M4 pre-assignment CA-1.1)*:

Registry anchor — Schema ID TABLE_1: [Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope] — blank cells prohibited globally; Tier ordered Admin/Custom/Restricted.

Preamble anchor — C-01 as authored by CA in Phase 0: TABLE_1 / SE-1 / SHALL-A / CA-1.1 — verifying...

Verification — TABLE_1 present? Every cell Granted/Denied/Conditional/N/A? All roles included? Tier column populated and ordered? -> PASS / FAIL

**CA-1.2 — C-02 verification** *(completing Phase 0 M4 pre-assignment CA-1.2)*:

Registry anchor — Schema ID TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?] — blank cells prohibited globally.

Preamble anchor — C-02 as authored by CA in Phase 0: TABLE_2 / SE-2 / SHALL-B / CA-1.2 — verifying...

Verification — TABLE_2 present? Every sensitive field with explicit FLS status? Null case stated? Gap? YES rows in TABLE_5? -> PASS / FAIL

**CA-1.3 — C-03 verification** *(completing Phase 0 M4 pre-assignment CA-1.3)*:

Registry anchor — Schema ID TABLE_3: [Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Verified?] — blank cells prohibited globally.

Preamble anchor — C-03 as authored by CA in Phase 0: TABLE_3 / SE-1+SE-3 / SHALL-C / CA-1.3 — verifying...

Verification — Every TABLE_1 role in TABLE_3? Effective Scope filled for all? Ambiguous scope in TABLE_5? -> PASS / FAIL

**CA-1.4 — C-04 verification** *(completing Phase 0 M4 pre-assignment CA-1.4)*:

Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity] — all four vectors required; Checked? = YES; TABLE_4 fills at SE-0 before TABLE_1 per Registry note.

Preamble anchor — C-04 as authored by CA in Phase 0: TABLE_4 / SE-0+SE-4 / SHALL-D / CA-1.4 — verifying SE-0 ordering only...

Verification — TABLE_4 present? All four vectors with Checked? = YES? Each with finding or specific rule-out? TABLE_4 precedes TABLE_1 in output body (SE-0 before SE-1)? -> PASS / FAIL

**CA-1.5 — C-05 verification** *(completing Phase 0 M4 pre-assignment CA-1.5)*:

Registry anchor — Schema ID TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Tier, Severity, Remediation] — blank cells prohibited globally.

Preamble anchor — C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 — verifying...

Verification — TABLE_5 present? Named gap with specific field/role/rule? Remediations exact (object + path + post-fix state)? -> PASS / FAIL

**CA-1.6 — SHALL-F CS-EXPECTATION-VIOLATED structure verification**:

Registry anchor — Schema ID TABLE_5 CS-EXPECTATION-VIOLATED row structure: [CS-Expected field citing CS-2/CS-3 row ID, SE-Actual field naming diverging SE finding, Delta field stating exact configuration change] — all three Remediation fields required; a row missing any field is structurally incomplete.

Preamble anchor — SHALL-F as authored by CA in Phase 0: CS-EXPECTATION-VIOLATED rows MUST carry CS-Expected / SE-Actual / Delta — verifying...

Verification — For each CS-EXPECTATION-VIOLATED row in TABLE_5: CS-Expected populated with CS-2 or CS-3 row ID? SE-Actual populated with specific SE finding? Delta populated with exact configuration change? -> PASS / FAIL per row.

**CA-1.7 — SHALL-G compliance verification** *(MANUAL GAP exact-label two-part blocks)*:

Registry anchor — CONTEXT section declared exact labels: "Blind spot 1 — Post-incident FLS gap" (SE-2 target), "Blind spot 2 — Cumulative privilege blind spot" (SE-3 target), "Blind spot 3 — OWD-sharing-rule override gap" (SE-4 target). SHALL-G requires two-part blocks: `MANUAL GAP [<exact label>]:` then `STRUCTURED CLOSE:`.

Preamble anchor — SHALL-G as authored by CA in Phase 0: Line 1 MUST begin `MANUAL GAP [<exact CONTEXT label>]:` — character-for-character match — verifying...

Verification — SE-2 opens with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:`? SE-3 opens with `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:`? SE-4 opens with `MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:`? Each followed by `STRUCTURED CLOSE:`? -> PASS / FAIL per section.

**CA-1.8 — CS-0 Registry acknowledgment precedes CS-1** *(C-33 verification)*:

Registry anchor — Schema Registry declares CS-2 and CS-3 with Schema IDs "CS-2 — Sharing Rule Expectations" and "CS-3 — Cross-Role Access Differential Expectations", each with SE-updatable column declarations.

Preamble anchor — C-33 requires CS role to open with CS-0 citing Schema Registry IDs for CS-2 and CS-3 by exact label before any CS-1 content — verifying...

Verification — CS-0 section present as explicitly labeled sub-step? CS-0 quotes Schema ID: CS-2 and Schema ID: CS-3 by exact label? CS-0 appears before CS-1 content begins? -> PASS / FAIL

**CA Format Compliance Verdict (Phase 0 citation):**

Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0), Phase 0 label as structural basis.

[C-01 through C-05: CA-1.1–CA-1.5 results. SHALL-F three-field structure: CA-1.6 result. SHALL-G exact-label blocks: CA-1.7 result. CS-0 Registry acknowledgment: CA-1.8 result. Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

---

## V-02 — Single-Axis: SE-4 STRUCTURED CLOSE TABLE_4 Row Cross-Reference + CA-1.9 (C-35)

**Axis:** R12-V-05 base with one structural addition: (a) SHALL-D extended with sub-clause
SHALL-D-EXT-C35 mandating that SE-4's STRUCTURED CLOSE block contain a verbatim TABLE_4 row
cross-reference in the format "Cite: TABLE_4 (filled at SE-0) row [ID] — [role] privilege
ceiling: [pattern]"; (b) CA-1.9 row added to Phase 3 as a distinct audit target for this
verbatim citation, explicitly separate from CA-1.4 (SE-0 ordering) and CA-1.7 (MANUAL GAP
labels); (c) NON-OVERLAP DECLARATION extended to three statements naming CA-1.4 / CA-1.7 /
CA-1.9 as non-overlapping scopes. No preamble axis declaration block; no tri-dimensional
attestation.
**Hypothesis:** V-02 adds the STRUCTURED CLOSE verbatim citation and dedicated CA-1.9 row.
Expected: passes C-35; fails C-34 (no axis declaration) and C-36 (no tri-dimensional
attestation). Score: 26/28.

---

You are running a permissions trace signal for: {{topic}}

[CONTEXT section: identical to V-01]

[ROLE SEQUENCING MANDATE: identical to V-01 except Phase 0 description includes SHALL-D-EXT-C35
and CA-1.9 pre-assignment; Phase 3 description notes CA-1.9 as distinct audit target; no
STRUCTURAL AXIS NON-INTERFERENCE DECLARATION or attestation cross-link mandate.]

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1 and 0.2 before any other phase begins.*

[Step 0.1 — Schema Registry: identical to V-01]

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: M1, M2, M3, M4 are simultaneously active — not alternative coverage paths. M4
CA verification row IDs pre-assigned by CA constitute pre-existing contract obligations.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 + SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A through SHALL-E: identical to V-01.
- SHALL-D extended with sub-clause **SHALL-D-EXT-C35** *(V-02 addition)*: SE-4's STRUCTURED CLOSE block MUST contain a verbatim TABLE_4 row cross-reference in the exact format: "Cite: TABLE_4 (filled at SE-0) row [ID] — [role] privilege ceiling: [pattern]". The citation MUST appear within the STRUCTURED CLOSE content (the second part of the two-part block), not in the MANUAL GAP line or in SE-4's analytical prose outside the two-part block. CA-1.9 verifies this sub-clause as a distinct audit target from CA-1.4 and CA-1.7.
- SHALL-F: identical to V-01.
- SHALL-G: identical to V-01.

*Handing to PHASE 1 — SE.*

---

## PHASE 1 — SE: Security Analysis

[SE-0 through SE-3: identical to V-01]

### SE-4 / SHALL-D — Privilege Escalation Analysis *(V-02 — STRUCTURED CLOSE TABLE_4 cross-reference)*

MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing sharing rules that
silently override them; a Private OWD combined with an active sharing rule grants effective
org-wide access without appearing in any security roles UI view.

STRUCTURED CLOSE:
TABLE_4 (filled at SE-0) surfaced escalation vectors before TABLE_1 was populated, establishing
the privilege ceiling first. CS-2 sharing rule expectations are confirmed or contradicted by SE
Cross-Reference and SE Confirmation columns after TABLE_4 analysis at SE-0.

Cite: TABLE_4 (filled at SE-0) row [ID] — [role] privilege ceiling: [pattern]

*(Per SHALL-D-EXT-C35: this verbatim TABLE_4 row cross-reference names the specific SE-0 row
that established the privilege ceiling, anchoring the SE-4 gap closure to the precise escalation
vector finding recorded at SE-0.)*

[Full escalation analysis: cross-reference TABLE_4. For each confirmed vector, trace to terminal
access level. For each rule-out, confirm the specific control at SE-0.]

[SE-5: identical to V-01]

*Handing to PHASE 2 — CS.*

---

[PHASE 2 — CS: identical to V-01]

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification (V-02)

*CA returns. Phase 3 CA-1.N audit-target scope roster:*

| CA Row | Audit Target | Criterion | Non-Overlapping Scope |
|--------|-------------|-----------|----------------------|
| CA-1.1 | TABLE_1 completeness | C-01 | Role-operation matrix cell coverage and role enumeration |
| CA-1.2 | TABLE_2 FLS coverage | C-02 | Sensitive field FLS status and null-case declaration |
| CA-1.3 | TABLE_3 record scope | C-03 | Effective scope completeness for every TABLE_1 role |
| CA-1.4 | TABLE_4 SE-0 ordering | C-04 | SE-0 execution before SE-1; all four vectors with Checked? = YES — ordering and presence only |
| CA-1.5 | TABLE_5 gap inventory | C-05 | Named gap with specific field/role/rule; exact remediation |
| CA-1.6 | SHALL-F CS-EXPECTATION-VIOLATED structure | SHALL-F | Three-field Remediation completeness only |
| CA-1.7 | MANUAL GAP exact labels | SHALL-G | Character-for-character CONTEXT label carry-through only |
| CA-1.8 | CS-0 Registry citation | C-33 | CS-0 presence before CS-1; Schema ID labels by exact string |
| CA-1.9 | SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference | SHALL-D-EXT-C35 | Verbatim "Cite: TABLE_4 (filled at SE-0) row [ID]" format in SE-4's STRUCTURED CLOSE only — distinct from SE-0 ordering (CA-1.4) and MANUAL GAP labels (CA-1.7) |

NON-OVERLAP DECLARATION *(V-02 — three-statement)*:
The audit scope bounded by [CA-1.4: SE-0 ordering and four-vector presence] is exclusively
whether TABLE_4 precedes TABLE_1 in the output body and whether all four vectors carry
Checked? = YES — this scope does not extend to label matching or verbatim citation format.
The audit scope bounded by [CA-1.7: MANUAL GAP exact-label match] is exclusively whether the
character-for-character CONTEXT label appears at SE-2, SE-3, SE-4 — this scope does not extend
to structural ordering or verbatim citation format.
The audit scope bounded by [CA-1.9: SE-4 STRUCTURED CLOSE verbatim TABLE_4 row cross-reference]
is exclusively the "Cite: TABLE_4 (filled at SE-0) row [ID]" verbatim format in SE-4's
STRUCTURED CLOSE — this scope does not extend to ordering (bounded by CA-1.4) or label match
(bounded by CA-1.7).

[CA-1.1 through CA-1.8: identical to V-01]

**CA-1.9 — SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference** *(completing Phase 0 M4 pre-assignment CA-1.9 — SHALL-D-EXT-C35; distinct audit target from CA-1.4 and CA-1.7)*:

Registry anchor — Schema ID TABLE_4 (filled at SE-0): [Vector, Checked?, Finding, Severity]. SE-4 STRUCTURED CLOSE MUST contain verbatim cross-reference format: "Cite: TABLE_4 (filled at SE-0) row [ID] — [role] privilege ceiling: [pattern]". This is distinct from SE-0 ordering (CA-1.4) and MANUAL GAP labels (CA-1.7).

Preamble anchor — SHALL-D extended with sub-clause SHALL-D-EXT-C35 as authored by CA in Phase 0: SE-4's STRUCTURED CLOSE MUST contain verbatim TABLE_4 row cross-reference. CA-1.9 completes the pre-assigned M4 obligation for SHALL-D-EXT-C35 — verifying...

Verification — SE-4 STRUCTURED CLOSE contains verbatim "Cite: TABLE_4 (filled at SE-0) row [ID]" format? Cross-reference names a specific TABLE_4 row ID and role privilege ceiling pattern? This cross-reference is structurally distinct from the SE-0 ordering check (CA-1.4) and exact-label check (CA-1.7)? -> PASS / FAIL

**CA Format Compliance Verdict (Phase 0 citation):**

Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0), Phase 0 label as structural basis.

[C-01 through C-05: CA-1.1–CA-1.5 results. SHALL-F three-field structure: CA-1.6 result. SHALL-G exact-label blocks: CA-1.7 result. CS-0 Registry acknowledgment: CA-1.8 result. SE-4 STRUCTURED CLOSE TABLE_4 cross-reference: CA-1.9 result. Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

---

## V-03 — Single-Axis: Tri-Dimensional Self-Evidence Attestation in CA Terminal Verdict (C-36)

**Axis:** R12-V-05 base with one structural addition: (a) attestation cross-link mandate added
to Phase 0 Step 0.2 preamble, requiring the CA terminal verdict to include a TRI-DIMENSIONAL
SELF-EVIDENCE ATTESTATION block with A-N axis labels matching the output body; (b) the CA
terminal verdict gains a TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION table naming each R12
dimension by axis label with specific output-body evidence sources. No preamble axis declaration
block; no SHALL-D-EXT-C35 or CA-1.9.
**Hypothesis:** V-03 adds the terminal attestation that extends C-22's phase-execution
self-evidence to all three R12 dimensions simultaneously. Expected: passes C-36; fails C-34
(no axis declaration) and C-35 (no CA-1.9). Score: 26/28.

---

You are running a permissions trace signal for: {{topic}}

[CONTEXT section: identical to V-01]

[ROLE SEQUENCING MANDATE: identical to V-01 except Phase 3 description notes terminal verdict
includes TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION; no STRUCTURAL AXIS NON-INTERFERENCE
DECLARATION block or SHALL-D-EXT-C35/CA-1.9.]

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

[Step 0.1 — Schema Registry: identical to V-01]

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

[CEM table and SHALL-A through SHALL-G: identical to V-01 — no axis declaration block]

**Attestation cross-link mandate** *(V-03 addition)*: The TRI-DIMENSIONAL SELF-EVIDENCE
ATTESTATION block in the CA Format Compliance Verdict MUST identify each R12 dimension by
axis label A-1, A-2, A-3. Each row MUST name the specific output-body element that makes the
dimension self-evidencing — not a prompt-level mandate. Rows that identify dimensions only by
criterion number (C-31, C-32, C-33) without an A-N label fail the cross-link mandate.

*Handing to PHASE 1 — SE.*

---

[PHASE 1 — SE through PHASE 2 — CS: identical to V-01]

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification (V-03)

[CA-1.N audit-target scope roster: identical to V-01 — eight rows, CA-1.1 through CA-1.8]

[NON-OVERLAP DECLARATION: identical to V-01 — three statements (CA-1.4 / CA-1.7 / CA-1.6)]

[CA-1.1 through CA-1.8: identical to V-01]

**CA Format Compliance Verdict (Phase 0 citation):**

Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0), Phase 0 label as structural basis.

[C-01 through C-05: CA-1.1–CA-1.5 results. SHALL-F three-field structure: CA-1.6 result. SHALL-G exact-label blocks: CA-1.7 result. CS-0 Registry acknowledgment: CA-1.8 result. Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

**TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION** *(V-03 addition — C-36)*

Each R12 structural dimension is independently verifiable from the output body without consulting
prompt instructions. Axis labels A-1, A-2, A-3 match the STRUCTURAL AXIS DECLARATION per
attestation cross-link mandate in Phase 0 Step 0.2.

| Axis | Dimension (Criterion) | Output-Body Evidence Source | Status |
|------|-----------------------|-----------------------------|--------|
| A-1 | Execution order (C-31) | PHASE 1 section header "SE-0 / SHALL-D — Escalation Vector Inventory (executes BEFORE SE-1)" appears before "SE-1 / SHALL-A" in output body; TABLE_4 rows precede TABLE_1 rows | CONFIRMED |
| A-2 | Closure-note format (C-32) | SE-2, SE-3, SE-4 each open with verbatim "MANUAL GAP [...]:" / "STRUCTURED CLOSE:" two-part block; labels are character-for-character matches to CONTEXT section entries | CONFIRMED |
| A-3 | CS self-reference (C-33) | PHASE 2 section header "CS-0 — Schema Registry Acknowledgment (executes before CS-1)" cites "Schema ID: CS-2" and "Schema ID: CS-3" by exact label before CS-1 content begins | CONFIRMED |

---

## V-04 — Combined: C-34 (Preamble Axis Declaration) + C-35 (SE-4 STRUCTURED CLOSE + CA-1.9)

**Axis:** V-01 (C-34 preamble axis declaration) + V-02 (SHALL-D-EXT-C35 + CA-1.9) combined.
No tri-dimensional attestation block (V-03 withheld).
**Hypothesis:** C-34 and C-35 are architecturally independent — the preamble declaration does
not require the STRUCTURED CLOSE verbatim citation and vice versa. V-04 tests that both
mechanisms compose without producing an unexpected constraint. Expected: 27/28 (fails only C-36).

---

You are running a permissions trace signal for: {{topic}}

[CONTEXT section: identical to V-01]

[ROLE SEQUENCING MANDATE: Phase 0 description includes both STRUCTURAL AXIS NON-INTERFERENCE
DECLARATION with A-1/A-2/A-3 rows AND SHALL-D-EXT-C35 + CA-1.9 pre-assignment. Phase 3
includes NON-OVERLAP DECLARATION with four statements (CA-1.4/CA-1.7/CA-1.9 plus axis
non-overlap note). No attestation cross-link mandate; no tri-dimensional attestation.]

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

[Step 0.1 — Schema Registry: identical to V-01]

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

[CEM table: identical to V-01 — five rows, four columns]

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A through SHALL-E: identical to V-01.
- SHALL-D extended with sub-clause **SHALL-D-EXT-C35** (from V-02): SE-4's STRUCTURED CLOSE block MUST contain a verbatim TABLE_4 row cross-reference: "Cite: TABLE_4 (filled at SE-0) row [ID] — [role] privilege ceiling: [pattern]". CA-1.9 verifies this sub-clause as a distinct audit target from CA-1.4 and CA-1.7.
- SHALL-F: identical to V-01.
- SHALL-G: identical to V-01.

**STRUCTURAL AXIS NON-INTERFERENCE DECLARATION** *(from V-01 — C-34)*

| Axis | Dimension | Criterion | Self-Evidence Mechanism | Non-Interference Statement |
|------|-----------|-----------|------------------------|---------------------------|
| A-1 | Execution order | C-31 | TABLE_4 fills at SE-0 section header, which precedes SE-1 in output body | Satisfying A-1 does not justify relaxing A-2 or A-3 |
| A-2 | Closure-note format | C-32 | MANUAL GAP [...] / STRUCTURED CLOSE exact-label two-part blocks at SE-2, SE-3, SE-4 | Satisfying A-2 does not justify relaxing A-1 or A-3 |
| A-3 | CS self-reference | C-33 | CS-0 cites Schema Registry IDs for CS-2 and CS-3 by exact label before CS-1 | Satisfying A-3 does not justify relaxing A-1 or A-2 |

These axes share no mechanism overlap. CA-1.4 verifies A-1; CA-1.7 verifies A-2; CA-1.8
verifies A-3. Each axis has a distinct, non-overlapping CA-1 audit target. CA-1.9 verifies
SHALL-D-EXT-C35 — the verbatim cross-reference of a specific TABLE_4 row within SE-4's
STRUCTURED CLOSE content — and is structurally distinct from all three axis verification rows.

*Handing to PHASE 1 — SE.*

---

## PHASE 1 — SE: Security Analysis

[SE-0 through SE-3: identical to V-01]

### SE-4 / SHALL-D — Privilege Escalation Analysis *(V-04 — STRUCTURED CLOSE TABLE_4 cross-reference per SHALL-D-EXT-C35)*

MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing sharing rules that
silently override them; a Private OWD combined with an active sharing rule grants effective
org-wide access without appearing in any security roles UI view.

STRUCTURED CLOSE:
TABLE_4 (filled at SE-0) surfaced escalation vectors before TABLE_1 was populated, establishing
the privilege ceiling first.

Cite: TABLE_4 (filled at SE-0) row [ID] — [role] privilege ceiling: [pattern]

*(Per SHALL-D-EXT-C35: verbatim TABLE_4 row cross-reference anchors SE-4's STRUCTURED CLOSE to
the specific privilege-ceiling row established at SE-0.)*

[Full escalation analysis: identical to V-01/V-02]

[SE-5: identical to V-01]

*Handing to PHASE 2 — CS.*

---

[PHASE 2 — CS: identical to V-01]

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification (V-04)

*CA returns. Phase 3 CA-1.N audit-target scope roster:*

| CA Row | Audit Target | Criterion | Non-Overlapping Scope |
|--------|-------------|-----------|----------------------|
| CA-1.1 | TABLE_1 completeness | C-01 | Role-operation matrix cell coverage and role enumeration |
| CA-1.2 | TABLE_2 FLS coverage | C-02 | Sensitive field FLS status and null-case declaration |
| CA-1.3 | TABLE_3 record scope | C-03 | Effective scope completeness for every TABLE_1 role |
| CA-1.4 | TABLE_4 SE-0 ordering | C-04 | SE-0 execution before SE-1; all four vectors present — ordering and presence only |
| CA-1.5 | TABLE_5 gap inventory | C-05 | Named gap with specific field/role/rule; exact remediation |
| CA-1.6 | SHALL-F CS-EXPECTATION-VIOLATED structure | SHALL-F | Three-field Remediation completeness only |
| CA-1.7 | MANUAL GAP exact labels | SHALL-G | Character-for-character CONTEXT label carry-through only |
| CA-1.8 | CS-0 Registry citation | C-33 | CS-0 presence before CS-1; Schema ID labels by exact string |
| CA-1.9 | SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference | SHALL-D-EXT-C35 | Verbatim "Cite: TABLE_4 (filled at SE-0) row [ID]" format in SE-4 STRUCTURED CLOSE only |

NON-OVERLAP DECLARATION *(V-04 — four statements)*:
[CA-1.4: SE-0 ordering and four-vector presence] — exclusively ordering and Checked? = YES.
[CA-1.7: MANUAL GAP exact-label match] — exclusively character-for-character CONTEXT label.
[CA-1.9: SE-4 STRUCTURED CLOSE verbatim TABLE_4 row cross-reference] — exclusively the
verbatim "Cite: TABLE_4 (filled at SE-0) row [ID]" format in SE-4's STRUCTURED CLOSE; does
not extend to ordering (CA-1.4) or label match (CA-1.7).
[Axis non-overlap: C-34 preamble declaration verifies that A-1/A-2/A-3 are orthogonal; the
three axis verification rows CA-1.4/CA-1.7/CA-1.8 verify each axis independently; CA-1.9
targets the SHALL-D-EXT-C35 sub-clause and is not an axis verification row.]

[CA-1.1 through CA-1.8: identical to V-01]

[CA-1.9: identical to V-02]

**CA Format Compliance Verdict (Phase 0 citation):**

Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0), Phase 0 label as structural basis.

[C-01 through C-05: CA-1.1–CA-1.5 results. SHALL-F three-field structure: CA-1.6 result. SHALL-G exact-label blocks: CA-1.7 result. CS-0 Registry acknowledgment: CA-1.8 result. SE-4 STRUCTURED CLOSE TABLE_4 cross-reference: CA-1.9 result. Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

---

## V-05 — Full: C-34 + C-35 + C-36 (28/28 Attempt)

**Axis:** All three new mechanisms simultaneously active on the R12-V-05 base:
(1) STRUCTURAL AXIS NON-INTERFERENCE DECLARATION in preamble (C-34) — from V-01;
(2) SHALL-D-EXT-C35 + SE-4 STRUCTURED CLOSE verbatim TABLE_4 citation + CA-1.9 (C-35) — from V-02;
(3) Attestation cross-link mandate + TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION in terminal
verdict (C-36) — from V-03.
**Hypothesis:** All three mechanisms share no prerequisite overlap: C-34 hangs on C-31+C-32+C-33+C-17
(all pass in base); C-35 hangs on C-31+C-32 (both pass); C-36 hangs on C-22+C-32+C-33 (all pass).
Activating all three simultaneously should not introduce mutual interference given their
distinct verification targets. Expected: 28/28 (100.0).

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
| BS-U1 | Field inventory not described — sensitive fields per entity inferred from typical Dataverse deployments for {{topic}} | High |
| BS-U2 | Sharing rule list not provided — zero vs. multiple active rules cannot be determined without environment inspection | High |
| BS-U3 | Team structure not specified — owner vs. access teams and membership control assumed from feature context | Medium |

---

## ROLE SEQUENCING MANDATE

This output executes in four explicitly labeled phases. Phase labels MUST appear as structural
section headers in the output body. Each phase completes fully before the next begins.
Execution order is self-attestable from phase labels alone.

**PHASE 0 — CA (Compliance Auditor):** CA executes first. Authors Schema Registry (Step 0.1:
seven table schemas declared centrally) and Criterion Enforcement Matrix preamble (Step 0.2:
SHALL obligations including SHALL-D-EXT-C35 sub-clause, CEM four-column mapping, STRUCTURAL
AXIS NON-INTERFERENCE DECLARATION with A-1/A-2/A-3 labeled rows, attestation cross-link
mandate, M4 pre-assignments CA-1.1 through CA-1.9). CA issues handoff to PHASE 1 — SE.

**PHASE 1 — SE (Security Engineer / Dataverse Security Expert):** Executes second. Opens with
SE-0 (TABLE_4 escalation vectors before TABLE_1). Populates TABLE_1 through TABLE_5 using
Dataverse-native terminology. SE-2, SE-3, SE-4 each open with exact-label two-part closure
block per SHALL-G. SE-4 STRUCTURED CLOSE carries verbatim TABLE_4 row cross-reference per
SHALL-D-EXT-C35. SE populates SE-updatable columns in CS-2 and CS-3. Handoff to PHASE 2 — CS.

**PHASE 2 — CS (Customer Success):** Executes third. Opens with CS-0 (Schema Registry ID
citations for CS-2 and CS-3 before CS-1). Produces CS-1 qualitative baseline and expectation
tables CS-2 and CS-3. Handoff to PHASE 3 — CA-1.

**PHASE 3 — CA-1 (CA Verification Pass):** CA returns. CA-1.N audit-target scope roster
followed by NON-OVERLAP DECLARATION (four statements: CA-1.4/CA-1.7/CA-1.9/axis non-overlap).
Each CA-1 row performs double-anchor reaffirmation (Registry anchor labeled, Preamble anchor
labeled, Verification paragraph following both). CA-1.9 is distinct from CA-1.4 and CA-1.7.
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
Note: TABLE_4 fills at SE-0, BEFORE TABLE_1 — privilege ceiling established first.

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation`
Remediation = exact configuration object + exact path + expected post-fix state. Generic text fails.
CS-EXPECTATION-VIOLATED Remediation: three-field block (CS-Expected / SE-Actual / Delta).

**Schema ID: CS-2 — Sharing Rule Expectations**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference (TABLE_4 row ID), SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE update protocol: populate after TABLE_4 at SE-0. CONTRADICTED triggers CS-EXPECTATION-VIOLATED.

**Schema ID: CS-3 — Cross-Role Access Differential Expectations**
Declared columns: `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference (TABLE_1 or TABLE_3 row ID), SE Confirmation.
SE update protocol: populate after TABLE_1 and TABLE_3 analysis. CONTRADICTED triggers CS-EXPECTATION-VIOLATED.

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
- SHALL-D: TABLE_4 MUST contain all four escalation vectors with Checked? = YES. A rule-out requires naming the specific mechanism and a specific reason no path exists. TABLE_4 fills at SE-0 before TABLE_1. **SHALL-D extension sub-clause SHALL-D-EXT-C35** *(C-35)*: SE-4's STRUCTURED CLOSE block MUST contain a verbatim TABLE_4 row cross-reference in the exact format: "Cite: TABLE_4 (filled at SE-0) row [ID] — [role] privilege ceiling: [pattern]". The citation MUST appear within the STRUCTURED CLOSE content, not in the MANUAL GAP line or in SE-4's analytical prose outside the two-part block. CA-1.9 verifies this sub-clause as a distinct audit target from CA-1.4 (SE-0 ordering) and CA-1.7 (MANUAL GAP exact labels).
- SHALL-E: TABLE_5 MUST contain at least one gap row with a named field, role, or rule. Zero gaps requires explicit evidence rows confirming what was checked.
- SHALL-F: When any CS-2 or CS-3 expectation conflicts with an SE finding, the conflict MUST be recorded in TABLE_5 as gap type CS-EXPECTATION-VIOLATED with three-field Remediation block: CS-Expected / SE-Actual / Delta. A row missing any field MUST be reopened.
- SHALL-G: Each SE sub-section SE-2, SE-3, SE-4 opens with a two-part exact-label closure block. Line 1: `MANUAL GAP [<exact CONTEXT label>]:` — character-for-character match required; paraphrase fails. Line 2: failure-mode description. Line 3: `STRUCTURED CLOSE:`. Line 4: which table closes the gap. CA-1.7 verifies exact labels.

**STRUCTURAL AXIS NON-INTERFERENCE DECLARATION** *(C-34)*

The three R12 structural dimensions are orthogonal obligations. Each is independently mandated
and activating one does not constrain or relax the others. This declaration converts the
architectural independence demonstrated by R12-V-05 into a binding preamble contract.

| Axis | Dimension | Criterion | Self-Evidence Mechanism | Non-Interference Statement |
|------|-----------|-----------|------------------------|---------------------------|
| A-1 | Execution order | C-31 | TABLE_4 fills at SE-0 section header, which precedes SE-1 in output body | Satisfying A-1 (SE-0 ordering) does not justify relaxing A-2 or A-3 |
| A-2 | Closure-note format | C-32 | MANUAL GAP [...] / STRUCTURED CLOSE exact-label two-part blocks at SE-2, SE-3, SE-4 | Satisfying A-2 (two-part blocks) does not justify relaxing A-1 or A-3 |
| A-3 | CS self-reference | C-33 | CS-0 cites Schema Registry IDs for CS-2 and CS-3 by exact label before CS-1 | Satisfying A-3 (CS-0 acknowledgment) does not justify relaxing A-1 or A-2 |

These axes share no mechanism overlap. CA-1.4 verifies A-1; CA-1.7 verifies A-2; CA-1.8
verifies A-3. Each axis has a distinct, non-overlapping CA-1 audit target. CA-1.9 targets
the SHALL-D-EXT-C35 sub-clause and is not an axis verification row.

**Attestation cross-link mandate** *(C-36 prerequisite)*: The TRI-DIMENSIONAL SELF-EVIDENCE
ATTESTATION block in the CA Format Compliance Verdict (Phase 3) MUST identify each R12
dimension by its axis label as declared in this table (A-1, A-2, A-3). Each row MUST name the
specific output-body element that makes the dimension self-evidencing — not a prompt-level
mandate. Attestation rows that identify dimensions only by criterion number without the A-N
axis label fail the cross-link mandate.

*Handing to PHASE 1 — SE.*

---

## PHASE 1 — SE: Security Analysis

*SE uses Dataverse-native terminology throughout. Execution begins at SE-0.*

### SE-0 / SHALL-D — Escalation Vector Inventory (executes BEFORE SE-1)

TABLE_4 fills here, establishing the privilege ceiling before any TABLE_1 cell is populated.

**TABLE_4 — Escalation Vector Inventory** *(Schema Registry TABLE_4; all four vectors required)*

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Finding format for confirmed escalation: `[Role] -> [Mechanism: specific privilege name] -> [Elevated access achieved]`
Finding format for rule-out: "Checked [mechanism]: no path because [specific reason naming the exact configuration examined]."

After TABLE_4: populate SE Cross-Reference and SE Confirmation in CS-2 rows. CONTRADICTED
entries trigger CS-EXPECTATION-VIOLATED in TABLE_5.

*SE-0 complete — handing to SE-1.*

### SE-1 / SHALL-A — Role-Operation Matrix

**TABLE_1 — Role-Operation Matrix** *(Schema Registry TABLE_1; Tier column required; blank-cell rule global)*

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Include every role with any privilege on any entity in {{topic}}. Cross-reference CS-3's expected
access differential after the table — note rows that confirm expectations (with CS-3 row ref)
and rows that contradict (triggers CS-EXPECTATION-VIOLATED in TABLE_5).

**Cross-role differential analysis:** Compare the CS role against at least one more privileged
role for the same entity and operation. State whether the differential is expected (least
privilege satisfied) or anomalous, and why.

### SE-2 / SHALL-B — Field-Level Security Coverage

MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:
Column security profiles are not discoverable from the security roles UI; administrators learn
of missing FLS only after a data exposure reveals that a sensitive field was readable by an
unintended role.

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
No single Dataverse UI view surfaces the combined effective access produced by security role
plus owner team membership plus OWD; spot-checking individual roles misses team-accumulated
privilege escalation.

STRUCTURED CLOSE:
TABLE_3 below maps effective scope for every role by recording the OWD baseline, scope modifier
from team or role depth, and resulting effective scope in one traceable row, making
team-accumulated privilege visible without cross-referencing multiple views.

**TABLE_3 — Record Scope by Role** *(Schema Registry TABLE_3; blank-cell rule global)*

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role MUST appear. Scope Modifier: privilege depth, owner team membership, access
team, or sharing rule that changes the OWD baseline. Note any role where effective scope exceeds
role-only scope — this is a CS-EXPECTATION-VIOLATED candidate.

After TABLE_3: populate SE Cross-Reference and SE Confirmation in CS-3 rows. CONTRADICTED
entries trigger CS-EXPECTATION-VIOLATED in TABLE_5.

### SE-4 / SHALL-D — Privilege Escalation Analysis *(V-05 — STRUCTURED CLOSE verbatim TABLE_4 row cross-reference per SHALL-D-EXT-C35)*

MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing sharing rules that
silently override them; a Private OWD combined with an active sharing rule grants effective
org-wide access without appearing in any security roles UI view.

STRUCTURED CLOSE:
TABLE_4 (filled at SE-0) surfaced escalation vectors before TABLE_1 was populated, establishing
the privilege ceiling first. CS-2 sharing rule expectations are confirmed or contradicted by SE
Cross-Reference and SE Confirmation columns after TABLE_4 analysis at SE-0.

Cite: TABLE_4 (filled at SE-0) row [ID] — [role] privilege ceiling: [pattern]

*(Per SHALL-D-EXT-C35: this verbatim TABLE_4 row cross-reference names the specific SE-0 row
that established the privilege ceiling, anchoring SE-4's STRUCTURED CLOSE to the privilege-
ceiling-to-gap-closure chain. CA-1.9 verifies this citation as a distinct audit target.)*

[Cross-reference TABLE_4 (filled at SE-0). For each confirmed vector, trace the path to its
terminal access level. For each rule-out, confirm the specific control that prevents the path
at SE-0.]

### SE-5 / SHALL-E — Security Gap Inventory

**TABLE_5 — Security Gap Inventory** *(Schema Registry TABLE_5; blank-cell rule global)*

| # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation |
|---|----------|--------|---------------|------|------|----------|-------------|

Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.
Severity: CRITICAL / HIGH / MEDIUM.
Remediation specificity: name the exact object, exact path (Power Platform Admin Center
location), and expected post-fix state.
CS-EXPECTATION-VIOLATED rows (three-field Remediation block):
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
| CA-1.4 | TABLE_4 SE-0 ordering | C-04 | SE-0 execution before SE-1; all four vectors present with Checked? = YES — ordering and presence only |
| CA-1.5 | TABLE_5 gap inventory | C-05 | Named gap with specific field/role/rule; exact remediation |
| CA-1.6 | SHALL-F CS-EXPECTATION-VIOLATED structure | SHALL-F | Three-field Remediation completeness (CS-Expected/SE-Actual/Delta) only |
| CA-1.7 | MANUAL GAP exact labels | SHALL-G | Character-for-character CONTEXT label carry-through at SE-2, SE-3, SE-4 only |
| CA-1.8 | CS-0 Registry citation | C-33 | CS-0 presence before CS-1; Schema ID labels cited by exact string |
| CA-1.9 | SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference | SHALL-D-EXT-C35 | Verbatim "Cite: TABLE_4 (filled at SE-0) row [ID]" format in SE-4's STRUCTURED CLOSE only — distinct from CA-1.4 and CA-1.7 |

NON-OVERLAP DECLARATION *(V-05 — four statements)*:
The audit scope bounded by [CA-1.4: SE-0 ordering and four-vector presence] is exclusively
whether TABLE_4 precedes TABLE_1 in the output body and whether all four vectors carry
Checked? = YES — this scope does not extend to label matching or verbatim citation format.
The audit scope bounded by [CA-1.7: MANUAL GAP exact-label match] is exclusively whether the
character-for-character CONTEXT label appears at SE-2, SE-3, SE-4 — this scope does not extend
to structural ordering or verbatim citation format.
The audit scope bounded by [CA-1.9: SE-4 STRUCTURED CLOSE verbatim TABLE_4 row cross-reference]
is exclusively the "Cite: TABLE_4 (filled at SE-0) row [ID]" verbatim format in SE-4's
STRUCTURED CLOSE — this scope does not extend to ordering (bounded by CA-1.4) or label match
(bounded by CA-1.7).
The audit scope bounded by [STRUCTURAL AXIS NON-INTERFERENCE DECLARATION (C-34): orthogonality
of A-1/A-2/A-3 dimensions] is exclusively the preamble-level binding contract that the three
axes share no mechanism overlap — it is not an additional CA-1 verification row but a preamble
declaration whose effect is verified by the individual A-1/A-2/A-3 rows (CA-1.4/CA-1.7/CA-1.8)
not interfering with each other's scopes.

Each CA-1 row MUST present Registry anchor and Preamble anchor as structurally distinct labeled
paragraphs before the Verification paragraph. Inline concatenation of anchors fails C-24.

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

Preamble anchor — C-04 as authored by CA in Phase 0: TABLE_4 / SE-0+SE-4 / SHALL-D / CA-1.4 — verifying SE-0 ordering only; SE-4 STRUCTURED CLOSE verbatim cross-reference verified at CA-1.9...

Verification — TABLE_4 present? All four vectors with Checked? = YES? Each with finding or specific rule-out? TABLE_4 precedes TABLE_1 in output body (SE-0 before SE-1)? -> PASS / FAIL

**CA-1.5 — C-05 verification** *(completing Phase 0 M4 pre-assignment CA-1.5)*:

Registry anchor — Schema ID TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Tier, Severity, Remediation] — blank cells prohibited globally.

Preamble anchor — C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 — verifying...

Verification — TABLE_5 present? Named gap with specific field/role/rule? Remediations exact (object + path + post-fix state)? -> PASS / FAIL

**CA-1.6 — SHALL-F CS-EXPECTATION-VIOLATED structure verification**:

Registry anchor — Schema ID TABLE_5 CS-EXPECTATION-VIOLATED row structure: [CS-Expected field citing CS-2/CS-3 row ID, SE-Actual field naming diverging SE finding, Delta field stating exact configuration change] — all three Remediation fields required; a row missing any field is structurally incomplete and MUST be reopened.

Preamble anchor — SHALL-F as authored by CA in Phase 0: CS-EXPECTATION-VIOLATED rows MUST carry CS-Expected / SE-Actual / Delta — verifying...

Verification — For each CS-EXPECTATION-VIOLATED row in TABLE_5: CS-Expected populated with CS-2 or CS-3 row ID citation? SE-Actual populated with specific SE finding? Delta populated with exact configuration change? -> PASS / FAIL per row.

**CA-1.7 — SHALL-G compliance verification** *(MANUAL GAP exact-label two-part blocks)*:

Registry anchor — CONTEXT section declared exact labels: "Blind spot 1 — Post-incident FLS gap" (SE-2 target), "Blind spot 2 — Cumulative privilege blind spot" (SE-3 target), "Blind spot 3 — OWD-sharing-rule override gap" (SE-4 target). SHALL-G requires: `MANUAL GAP [<exact label>]:` then `STRUCTURED CLOSE:`.

Preamble anchor — SHALL-G as authored by CA in Phase 0: Line 1 MUST begin `MANUAL GAP [<exact CONTEXT label>]:` — character-for-character match; paraphrase or abbreviation fails — verifying...

Verification — SE-2 opens with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:`? SE-3 opens with `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:`? SE-4 opens with `MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:`? Each followed by `STRUCTURED CLOSE:`? -> PASS / FAIL per section.

**CA-1.8 — CS-0 Registry acknowledgment precedes CS-1** *(C-33 verification)*:

Registry anchor — Schema Registry declares CS-2 and CS-3 with Schema IDs "CS-2 — Sharing Rule Expectations" and "CS-3 — Cross-Role Access Differential Expectations", each with SE-updatable column declarations.

Preamble anchor — C-33 requires CS role to open with CS-0 citing Schema Registry IDs for CS-2 and CS-3 by exact label before any CS-1 content — verifying...

Verification — CS-0 section present as explicitly labeled sub-step? CS-0 quotes Schema ID: CS-2 and Schema ID: CS-3 by exact label? CS-0 appears before CS-1 content begins? -> PASS / FAIL

**CA-1.9 — SE-4 STRUCTURED CLOSE TABLE_4 row cross-reference** *(completing Phase 0 M4 pre-assignment CA-1.9 — SHALL-D-EXT-C35; distinct audit target from CA-1.4 and CA-1.7)*:

Registry anchor — Schema ID TABLE_4 (filled at SE-0): [Vector, Checked?, Finding, Severity]. SE-4 STRUCTURED CLOSE MUST contain verbatim cross-reference format: "Cite: TABLE_4 (filled at SE-0) row [ID] — [role] privilege ceiling: [pattern]". This is structurally distinct from SE-0 ordering (CA-1.4) and MANUAL GAP labels (CA-1.7).

Preamble anchor — SHALL-D extended with sub-clause SHALL-D-EXT-C35 as authored by CA in Phase 0: SE-4's STRUCTURED CLOSE MUST contain verbatim TABLE_4 row cross-reference. CA-1.9 completes the pre-assigned M4 obligation for SHALL-D-EXT-C35 — verifying...

Verification — SE-4 STRUCTURED CLOSE contains verbatim "Cite: TABLE_4 (filled at SE-0) row [ID]" format? Cross-reference names a specific TABLE_4 row ID and role privilege ceiling pattern? This cross-reference is structurally distinct from the SE-0 ordering check (CA-1.4) and exact-label check (CA-1.7)? -> PASS / FAIL

**CA Format Compliance Verdict (Phase 0 citation):**

Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0), Phase 0 label as structural basis.

[C-01 through C-05: CA-1.1–CA-1.5 results. SHALL-F three-field structure: CA-1.6 result. SHALL-G exact-label blocks: CA-1.7 result. CS-0 Registry acknowledgment: CA-1.8 result. SE-4 STRUCTURED CLOSE TABLE_4 cross-reference: CA-1.9 result. Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

**TRI-DIMENSIONAL SELF-EVIDENCE ATTESTATION** *(C-36)*

Each R12 structural dimension is independently verifiable from the output body without consulting
prompt instructions. Axis labels match the STRUCTURAL AXIS NON-INTERFERENCE DECLARATION in
Phase 0 Step 0.2 per attestation cross-link mandate.

| Axis | Dimension (Criterion) | Output-Body Evidence Source | Status |
|------|-----------------------|-----------------------------|--------|
| A-1 | Execution order (C-31) | PHASE 1 section header "SE-0 / SHALL-D — Escalation Vector Inventory (executes BEFORE SE-1)" appears before "SE-1 / SHALL-A" in output body; TABLE_4 rows precede TABLE_1 rows in output body | CONFIRMED |
| A-2 | Closure-note format (C-32) | SE-2, SE-3, SE-4 each open with verbatim "MANUAL GAP [...]:" / "STRUCTURED CLOSE:" two-part block; labels are character-for-character matches to CONTEXT section entries — body-readable by structure alone | CONFIRMED |
| A-3 | CS self-reference (C-33) | PHASE 2 section header "CS-0 — Schema Registry Acknowledgment (executes before CS-1)" cites "Schema ID: CS-2" and "Schema ID: CS-3" by exact label before CS-1 content begins — body-verifiable without cross-referencing Registry and CS schemas independently | CONFIRMED |
