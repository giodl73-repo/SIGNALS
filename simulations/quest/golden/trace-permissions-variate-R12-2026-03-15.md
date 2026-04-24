# trace-permissions Variate — Round 12
**Date:** 2026-03-15
**Rubric:** v11 (C-01 through C-33)
**Target:** 25/25 — add C-32 (exact-label two-part SHALL-G blocks) to the C-31/C-33 base

**State entering Round 12:**

| Variation | v11 score | Notes |
|-----------|-----------|-------|
| R11-V-01 | 98.8 (22/25) | fails C-31, C-32, C-33 — full base, single-line CONTEXT-CLOSES |
| R11-V-02 | 99.2 (23/25) | passes C-31 (SE-0 + Tier cols); fails C-32 (no exact-label blocks), C-33 (no CS-0) |
| R11-V-03 | 98.0 (20/25) | fails C-28/C-30 (two-part blocks without exact labels); fails C-31/C-32/C-33 by consequence |
| R11-V-04 | 99.2 (23/25) | passes C-33 (CS-0 acknowledgment); fails C-31 (no SE-0), C-32 (no exact-label blocks) |

Path to 25/25: R11-V-01 base + SE-0 ordering (C-31) + exact-label two-part blocks in SHALL-G (C-32) + CS-0 acknowledgment (C-33). C-32 is the only aspirational axis not yet tested in isolation.

V-03 in R11 introduced two-part blocks but failed C-32 because it used `MANUAL GAP:` without the bracketed exact CONTEXT label. C-32 requires `MANUAL GAP [<exact CONTEXT label>]:` with character-exact carry-through from the CONTEXT section. C-28 is the underlying exact-label requirement; C-30 is the SHALL-G enforcement floor; C-32 is the ceiling.

---

## Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Single-axis C-32: exact-label two-part SHALL-G blocks — `MANUAL GAP [<exact label>]:` / `STRUCTURED CLOSE:` at SE-2/SE-3/SE-4; SHALL-G updated to mandate exact CONTEXT label carry-through | C-32 requires C-27+C-28+C-30 as floor. V-01 adds the exact-label mandate to the two-part block format (fixing R11-V-03's failure mode). All other mechanisms from R11-V-01 preserved. Hypothesis: 23/25 (adds C-32; still fails C-31, C-33). |
| V-02 | Combined C-31+C-33: SE-0 admin-tier escalation before TABLE_1 (R11-V-02 axis) + CS-0 Registry acknowledgment (R11-V-04 axis) — both proven aspirational axes fused onto R11-V-01 base | SE-0 executes TABLE_4 before SE-1; TABLE_1/TABLE_3 gain Tier column; SE-4 cites SE-0 data. CS opens with CS-0 back-referencing Registry schema IDs and listing SE-updatable columns. CA-1.8 extended to verify CS-0 precedes CS-1. Single-line CONTEXT-CLOSES preserved (no C-32). Hypothesis: 24/25 (adds C-31+C-33; fails C-32). |
| V-03 | Single-axis phrasing register: imperative numbered-step voice throughout — all instruction prose rewritten as numbered execution steps with explicit MUST imperatives | Same mechanism coverage as R11-V-01 (7-schema Registry, SHALL-A through SHALL-G, CA-1.1 through CA-1.8). No new aspirational axes. Tests whether imperative register alters structural compliance detection. Hypothesis: 22/25. |
| V-04 | Single-axis TABLE_3 scope expansion: team membership decomposition — TABLE_3 gains Team Membership and Team Role Scope columns; SE-3 adds explicit team-by-team scope computation before Effective Scope | Same mechanism base. Tests whether granular team decomposition in TABLE_3 strengthens C-03/C-10 signal without aspirational changes. Hypothesis: 22/25. |
| V-05 | Full combination C-31+C-32+C-33: SE-0 + exact-label two-part blocks + CS-0 acknowledgment — the 25/25 candidate | All three aspirational axes on R11-V-01 base. SE-0 TABLE_4 before SE-1 with Tier columns (C-31). Exact-label two-part blocks at SE-2/SE-3/SE-4 with SHALL-G exact-label mandate (C-32). CS-0 Registry acknowledgment before CS-1/CS-2/CS-3 (C-33). CA-1.7 verifies exact labels; CA-1.8 extended to verify CS-0 precedes CS-1. Hypothesis: 25/25. |

---

## V-01 — Single-Axis C-32: Exact-Label Two-Part SHALL-G Closure Blocks

**Axis:** C-32 — exact-label two-part blocks at SE-2/SE-3/SE-4. Replaces single-line `> CONTEXT-CLOSES:` blockquotes with two-part labeled blocks: `MANUAL GAP [<exact CONTEXT label>]:` then `STRUCTURED CLOSE:`. SHALL-G updated to mandate exact character-for-character label carry-through from the CONTEXT section. R11-V-03 used two-part blocks without exact labels; V-01 fixes that failure mode.
**Hypothesis:** 23/25 (adds C-32; fails C-31, C-33).

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

Manual security reviews of Dataverse environments routinely miss three failure scenarios that this
trace is designed to surface:

**Blind spot 1 — Post-incident FLS gap.** Column security profiles are rarely audited proactively.
Sensitive fields — credit limits, compensation data, SSNs, contact identifiers — remain readable
and writable by any role unless a column security profile explicitly restricts them. The security
roles UI does not surface which fields lack column security profiles; gaps are discovered after data
exposure, not before.

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
SE-4 closes Blind spot 3. Closure notes are two-part labeled blocks co-located at each SE
sub-section opening, carrying the exact blind-spot label from this CONTEXT section.

---

## ROLE SEQUENCING MANDATE

This output executes in four explicitly labeled phases. Phase labels MUST appear as section
headers. Each phase completes fully before the next begins.

**PHASE 0 — CA (Compliance Auditor):**
CA executes first. Authors the Schema Registry (Step 0.1: TABLE_1 through TABLE_5, CS-2, CS-3 —
seven schemas total, SE-updatable columns declared on CS-2 and CS-3) and the Criterion
Enforcement Matrix preamble (Step 0.2: SHALL-A through SHALL-G, M4 row IDs CA-1.1 through CA-1.8
pre-assigned). CA issues handoff to PHASE 1.

**PHASE 1 — CS (Customer Success):**
Executes second. Produces CS-1 qualitative baseline plus expectation tables CS-2 and CS-3 using
the Schema Registry schemas. CS does not fill TABLE_1-5. CS issues handoff to PHASE 2.

**PHASE 2 — SE (Security Engineer / Dataverse Security Expert):**
Executes third. Fills TABLE_1-5 using Dataverse-native terminology. Populates SE-updatable columns
in CS-2 and CS-3. Sub-sections SE-2, SE-3, SE-4 each open with a two-part exact-label closure
block per SHALL-G. Issues handoff to PHASE 3.

**PHASE 3 — CA-1 (CA Verification Pass):**
CA returns. Each CA-1 row performs double-anchor reaffirmation: Registry anchor (labeled line
citing schema ID and declared columns) and Preamble anchor (labeled line quoting preamble row
values). Verification line follows both anchors. Inline concatenation of anchors into a single
string fails C-24.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1 and 0.2 before any other phase begins.*

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

**All table schemas declared centrally by CA. Blank-cell prohibition is global — individual
tables do not restate it. SE-update protocols for CS-2 and CS-3 declared co-located with schema
entry.**

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Blank-cell rule: every cell MUST carry Granted / Denied / Conditional (state condition inline) / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Blank-cell rule: FLS Profile Configured? = Configured / Not Configured (never blank). Gap? = YES / NO (never blank).

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name]. Verified? = YES / NO.

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
Blank-cell rule: all four vectors (team inheritance, sharing rules, impersonation, admin/env roles)
MUST appear. Checked? = YES for all. Finding = escalation path or specific rule-out (never blank).

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Blank-cell rule: Remediation = exact configuration change naming specific object, location, and
expected post-fix state. Generic text ("review permissions", "add FLS") fails.
CS-EXPECTATION-VIOLATED Remediation structure (three-field block):
- Field 1 — CS-Expected: cite CS-2 or CS-3 row and state the expectation verbatim or by row reference.
- Field 2 — SE-Actual: state the SE finding that contradicts the expectation.
- Field 3 — Delta: exact configuration change to align SE-Actual to CS-Expected.

**Schema ID: CS-2 — Sharing Rule Expectations (CS-authored expectation table)**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference (SE populates with TABLE_4 row or TABLE_5 row ID),
SE Confirmation (SE populates with CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE update protocol: After TABLE_4 analysis, SE populates SE Cross-Reference using TABLE_4 or
TABLE_5 row number. SE Confirmation: CONFIRMED if CS expectation matches SE finding; CONTRADICTED
if SE finding diverges (triggers CS-EXPECTATION-VIOLATED in TABLE_5); NOT-APPLICABLE if out of scope.

**Schema ID: CS-3 — Cross-Role Access Differential Expectations (CS-authored expectation table)**
Declared columns: `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference (SE populates with TABLE_1 row or TABLE_3 row ID),
SE Confirmation (SE populates with CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE update protocol: After TABLE_1 and TABLE_3 analysis, SE populates SE Cross-Reference and SE
Confirmation. CONTRADICTED triggers CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: M1, M2, M3 are simultaneously active. M4 CA verification row IDs pre-assigned
by CA constitute pre-existing contract obligations fulfilled as structural completions in Phase 3.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**SHALL obligations (authored by CA, Phase 0):**

- SHALL-A: A complete TABLE_1 MUST be present. Every cell carries Granted / Denied / Conditional / N/A. Every role with any privilege on any entity in {{topic}} MUST appear.
- SHALL-B: TABLE_2 MUST list every field containing PII, Financial, or Audit-Compliance data with explicit FLS status. Null case MUST be explicitly stated. All Gap? YES rows MUST appear in TABLE_5.
- SHALL-C: Every TABLE_1 role MUST appear in TABLE_3 with a filled Effective Scope. Ambiguous scope MUST appear in TABLE_5.
- SHALL-D: TABLE_4 MUST contain all four escalation vectors with Checked? = YES. A rule-out requires naming the mechanism and a specific reason no path exists.
- SHALL-E: TABLE_5 MUST contain at least one gap row with a named field, role, or rule. If zero gaps, TABLE_5 MUST contain explicit evidence rows confirming what was checked.
- SHALL-F: When any CS-2 or CS-3 expectation conflicts with an SE finding, the conflict MUST be recorded in TABLE_5 as gap type CS-EXPECTATION-VIOLATED. Each such row MUST carry all three fields of the three-field Remediation block (CS-Expected, SE-Actual, Delta). A gap recorded without all three fields is structurally incomplete and MUST be reopened. CA-1.6 verifies this structure.
- SHALL-G: At the opening of each SE sub-section SE-2, SE-3, and SE-4, closure MUST appear as a two-part labeled block with the following exact structure — Line 1: `MANUAL GAP [<exact CONTEXT label>]:` where <exact CONTEXT label> is the label as written character-for-character in the CONTEXT section above (e.g., "Blind spot 1 — Post-incident FLS gap" — not a paraphrase or abbreviation); Line 2: one or two sentences describing what manual audits fail to detect that this sub-section addresses; Line 3: `STRUCTURED CLOSE:`; Line 4: which table and mechanism in this sub-section closes the gap. A single-line blockquote annotation fails SHALL-G. A closure note in TABLE_5 or the terminal checklist fails SHALL-G. A label that paraphrases or abbreviates the CONTEXT label fails SHALL-G. CA-1.7 verifies exact label carry-through.

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Lower-Trust Access Baseline and Expectation Tables

*CS runs before SE. CS-2 and CS-3 are authored using the Schema Registry schemas declared in
Phase 0. CS does not fill TABLE_1-5.*

**CS-1 — Expected Customer Service access baseline:**
For each entity in scope: (a) which CRUD operations the CS role is expected to perform as part of
normal job function; (b) the expected record scope (own records, BU-wide, org-wide, etc.);
(c) which sensitive fields CS is expected to need read or write access to and why. Identify any
configuration CS relies on that may inadvertently open access beyond job requirements.

**CS-2 — Sharing rule expectations** *(using Schema Registry CS-2 schema — SE will populate
SE Cross-Reference and SE Confirmation after TABLE_4 analysis)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

For each Potential Overreach? YES: name the access path and the role most likely to be
over-reached by it.

**CS-3 — Expected cross-role access differential** *(using Schema Registry CS-3 schema — SE will
populate SE Cross-Reference and SE Confirmation after TABLE_1/TABLE_3 analysis)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

State at minimum one entity and one operation where CS should have less access than the Comparison
Role. Name any sharing rule that might close the gap unexpectedly.

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis

*SE executes Sections 1 through 5. SE uses Dataverse-native terminology throughout. SE populates
SE-updatable columns in CS-2 and CS-3. Confirmed expectations noted by row reference. Contradicted
expectations entered in TABLE_5 as CS-EXPECTATION-VIOLATED per SHALL-F.*

### SE-1 / SHALL-A — Section 1: Role-Operation Matrix

**TABLE_1 — Role-Operation Matrix** *(Schema Registry TABLE_1; blank-cell rule applies globally)*

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Include every role with any privilege on any entity in {{topic}}. After the table: cross-reference
CS-3's expected access differential — note which rows confirm CS expectations (with CS-3 row
reference) and which contradict (triggers CS-EXPECTATION-VIOLATED in TABLE_5).

**Cross-role differential analysis:** Compare the CS role against at least one more privileged role
for the same entity and operation. State whether the access differential observed in TABLE_1 is
expected (least privilege satisfied) or anomalous, and why.

### SE-2 / SHALL-B — Section 2: Field-Level Security Coverage

MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:
Column security profiles are not auditable from the security roles UI; administrators discover
missing FLS only after a data exposure event reveals that a sensitive field was readable by an
unintended role.

STRUCTURED CLOSE:
TABLE_2 below enumerates every sensitive field in scope with its explicit FLS status (Configured /
Not Configured), surfacing pre-event what the security roles UI conceals. All Not Configured
sensitive fields are forwarded to TABLE_5 as MISSING-FLS gaps.

**TABLE_2 — FLS Coverage** *(Schema Registry TABLE_2; blank-cell rule applies globally)*

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Categories: PII / Financial / Audit-Compliance / Other-Sensitive. Null case: "No column security
profiles active on {{topic}}. Sensitive fields identified: [list]. All entered in TABLE_5 as
MISSING-FLS." Forward all Gap? YES rows to TABLE_5.

**Defense-in-depth layer check for FLS:** Identify the enforcement layer (1: environment/admin,
2: security role + BU scope, 3: team membership, 4: column security profile) where field read or
write access is effectively granted or denied for at least one sensitive field. Explain why the
layer above it does not override.

### SE-3 / SHALL-C — Section 3: Record Access Scope

MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:
No single Dataverse UI view surfaces the combined effective access produced by a security role
plus owner team membership plus OWD settings; spot-checking roles individually misses cross-role
privilege accumulation through team inheritance.

STRUCTURED CLOSE:
TABLE_3 below maps the effective scope for every role by recording the OWD baseline, the scope
modifier from team or role depth, and the resulting effective scope as a single traceable row,
making team-accumulated privilege visible and auditable in one place.

**TABLE_3 — Record Scope by Role** *(Schema Registry TABLE_3; blank-cell rule applies globally)*

| Role | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role MUST appear. OWD: Private / Business Unit / Parent-Child BU / Organization.
Scope Modifier: security role privilege depth, owner team membership, access team, or sharing rule
that changes the baseline. Note any role where effective scope exceeds role-only scope due to team
membership — this is a CS-EXPECTATION-VIOLATED candidate.

After TABLE_3: populate SE Cross-Reference and SE Confirmation in CS-3 rows. Enter CONTRADICTED
rows as CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

### SE-4 / SHALL-D — Section 4: Privilege Escalation Analysis

MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:
Administrators audit OWD settings entity-by-entity without cross-referencing the sharing rules
that silently override them; a Private OWD combined with an active sharing rule can grant effective
org-wide access without appearing in any security roles UI view.

STRUCTURED CLOSE:
TABLE_4 below evaluates all four escalation vectors simultaneously, with sharing rules explicitly
cross-referenced against OWD settings in the Finding column. CS-2 sharing rule expectations are
confirmed or contradicted by SE Cross-Reference and SE Confirmation columns after TABLE_4 is filled.

**TABLE_4 — Escalation Vector Inventory** *(Schema Registry TABLE_4; all four vectors required)*

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Finding format: `[Role] -> [Mechanism] -> [Elevated access achieved]` for confirmed escalation;
for rule-out: "Checked [mechanism]: no path found because [specific reason naming the specific
configuration examined]." After TABLE_4: populate SE Cross-Reference and SE Confirmation in CS-2.
Enter CONTRADICTED rows as CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

### SE-5 / SHALL-E — Section 5: Security Gap Inventory

**TABLE_5 — Security Gap Inventory** *(Schema Registry TABLE_5; blank-cell rule applies globally)*

| # | Gap Type | Entity | Field or Rule | Role | Severity | Remediation |
|---|----------|--------|---------------|------|----------|-------------|

Gap Types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED /
CS-EXPECTATION-VIOLATED. Severity: CRITICAL / HIGH / MEDIUM.

Remediation specificity standard: name the exact object, the exact location (Power Platform Admin
Center path), and the expected post-fix state.

CS-EXPECTATION-VIOLATED rows (three-field Remediation block per SHALL-F):
- CS-Expected: [cite CS-2 or CS-3 row, state expectation verbatim or by row reference]
- SE-Actual: [SE finding that contradicts the expectation]
- Delta: [exact configuration change to align SE-Actual to CS-Expected]

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

*CA returns. Each CA-1 row MUST present the Registry schema citation and the preamble row
quotation as structurally distinct labeled elements. Each anchor constitutes a complete,
independently readable statement before the Verification line. Inline concatenation fails C-24.*

**CA-1.1 — C-01 verification** *(completing Phase 0 M4 pre-assignment CA-1.1)*:
- Registry anchor — Schema ID TABLE_1: [Role, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope] — blank cells prohibited globally.
- Preamble anchor — C-01 as authored by CA in Phase 0: TABLE_1 / SE-1 / SHALL-A / CA-1.1 — verifying...
- Verification — TABLE_1 present? Every cell has Granted/Denied/Conditional/N/A? All roles included? -> PASS / FAIL

**CA-1.2 — C-02 verification** *(completing Phase 0 M4 pre-assignment CA-1.2)*:
- Registry anchor — Schema ID TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?] — blank cells prohibited globally.
- Preamble anchor — C-02 as authored by CA in Phase 0: TABLE_2 / SE-2 / SHALL-B / CA-1.2 — verifying...
- Verification — TABLE_2 present? Sensitive fields with explicit FLS status? Null case stated? Gap? YES rows in TABLE_5? -> PASS / FAIL

**CA-1.3 — C-03 verification** *(completing Phase 0 M4 pre-assignment CA-1.3)*:
- Registry anchor — Schema ID TABLE_3: [Role, OWD Baseline, Scope Modifier, Effective Scope, Verified?] — blank cells prohibited globally.
- Preamble anchor — C-03 as authored by CA in Phase 0: TABLE_3 / SE-1+SE-3 / SHALL-C / CA-1.3 — verifying...
- Verification — Every TABLE_1 role in TABLE_3? Effective Scope filled? Ambiguous scope in TABLE_5? -> PASS / FAIL

**CA-1.4 — C-04 verification** *(completing Phase 0 M4 pre-assignment CA-1.4)*:
- Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity] — all four vectors, Checked? = YES.
- Preamble anchor — C-04 as authored by CA in Phase 0: TABLE_4 / SE-4 / SHALL-D / CA-1.4 — verifying...
- Verification — TABLE_4 present? All four vectors? Checked? = YES? Each with finding or specific rule-out? -> PASS / FAIL

**CA-1.5 — C-05 verification** *(completing Phase 0 M4 pre-assignment CA-1.5)*:
- Registry anchor — Schema ID TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Severity, Remediation] — blank cells prohibited globally.
- Preamble anchor — C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 — verifying...
- Verification — TABLE_5 present? Named gap with specific field/role/rule? Remediations exact? -> PASS / FAIL

**CA-1.6 — SHALL-F compliance verification** *(CS-EXPECTATION-VIOLATED three-field structure)*:
- Registry anchor — Schema ID TABLE_5 CS-EXPECTATION-VIOLATED row structure: [CS-Expected field, SE-Actual field, Delta field] — all three required per SHALL-F declaration in Phase 0.
- Preamble anchor — SHALL-F as authored by CA in Phase 0: CS-EXPECTATION-VIOLATED rows MUST carry CS-Expected, SE-Actual, Delta. Incomplete rows MUST be reopened.
- Verification — For each CS-EXPECTATION-VIOLATED row in TABLE_5: CS-Expected populated? SE-Actual populated? Delta populated with exact configuration change? -> PASS / FAIL per row.

**CA-1.7 — SHALL-G compliance verification** *(exact-label two-part closure blocks)*:
- Registry anchor — CONTEXT section declared exact labels: "Blind spot 1 — Post-incident FLS gap" (SE-2 closure target), "Blind spot 2 — Cumulative privilege blind spot" (SE-3 closure target), "Blind spot 3 — OWD-sharing-rule override gap" (SE-4 closure target). SHALL-G requires two-part blocks beginning with `MANUAL GAP [<exact label>]:` followed by `STRUCTURED CLOSE:`.
- Preamble anchor — SHALL-G as authored by CA in Phase 0: closure block Line 1 MUST begin `MANUAL GAP [<exact CONTEXT label>]:`; exact label = character-for-character match; paraphrase or abbreviation fails; single-line annotation fails; TABLE_5 consolidation fails.
- Verification — SE-2 opens with `MANUAL GAP [Blind spot 1 — Post-incident FLS gap]:`? SE-3 opens with `MANUAL GAP [Blind spot 2 — Cumulative privilege blind spot]:`? SE-4 opens with `MANUAL GAP [Blind spot 3 — OWD-sharing-rule override gap]:`? Each followed by `STRUCTURED CLOSE:` block? -> PASS / FAIL per section.

**CA-1.8 — CS-2/CS-3 Schema Registry registration verification** *(C-29)*:
- Registry anchor — Schema Registry declared CS-2 with SE-updatable columns SE Cross-Reference and SE Confirmation, SE-update protocol named. Schema Registry declared CS-3 with SE-updatable columns SE Cross-Reference and SE Confirmation, SE-update protocol named.
- Preamble anchor — CS-2 and CS-3 appear as named entries in the Schema Registry alongside TABLE_1-5. SE-update protocols co-located with schema entries.
- Verification — CS-2 in Schema Registry with SE-updatable column declarations? CS-3 in Schema Registry with SE-updatable column declarations? SE populated SE-updatable columns per protocol? -> PASS / FAIL

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0), Phase 0 by label.
[C-01 through C-05 with CA-1.1 through CA-1.5 results. SHALL-F (CA-1.6). SHALL-G exact-label two-part block compliance (CA-1.7). C-29 Schema Registry registration (CA-1.8). Overall: COMPLIANT / NON-COMPLIANT. Open items attributed to responsible role.]

---

## V-02 — Combined C-31+C-33: SE-0 Admin-Tier Ordering + CS-0 Registry Acknowledgment

**Axis:** R11-V-02 axis (SE-0 TABLE_4 before TABLE_1; Tier column in TABLE_1/TABLE_3; SE-4 cites
SE-0 data) combined with R11-V-04 axis (CS-0 sub-section back-references Registry schema IDs and
lists SE-updatable columns before CS-1/CS-2/CS-3). Single-line CONTEXT-CLOSES preserved (no C-32).
CA-1.8 extended to verify CS-0 acknowledgment precedes CS-1.
**Hypothesis:** 24/25 (adds C-31+C-33; fails C-32).

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

Manual security reviews of Dataverse environments routinely miss three failure scenarios that this
trace is designed to surface:

**Blind spot 1 — Post-incident FLS gap.** Column security profiles are rarely audited proactively.
Sensitive fields remain readable and writable by any role unless a column security profile
explicitly restricts them. Gaps are discovered after data exposure, not before.

**Blind spot 2 — Cumulative privilege blind spot.** A user holding a BU-scoped security role who
also belongs to an owner team with a broader team role has effective access beyond what the
security role alone grants. No single UI view surfaces the combined role + team + OWD scope.
Spot-checking individual roles misses team-accumulated privilege.

**Blind spot 3 — OWD-sharing-rule override gap.** Administrators review OWD settings without
cross-referencing the sharing rules that silently override them. A Private OWD combined with an
active Power Automate-triggered sharing rule grants effective org-wide read to trigger-condition
users, including low-trust accounts not intended to have broad access.

This trace closes all three blind spots: SE-2 closes Blind spot 1; SE-3 closes Blind spot 2;
SE-4 closes Blind spot 3. Section-level CONTEXT-CLOSES attestations co-located at each opening.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers.

**PHASE 0 — CA:** Authors Schema Registry (7 schemas: TABLE_1-5 with Tier columns on TABLE_1 and
TABLE_3 + CS-2 + CS-3 with SE-updatable columns and update protocols) and preamble (SHALL-A
through SHALL-G; M4 CA-1.1 through CA-1.8 pre-assigned). Handoff to PHASE 1.

**PHASE 1 — CS:** Opens with CS-0 sub-section (Schema Registry acknowledgment — cites Registry
schema IDs for CS-2 and CS-3 by exact Schema ID label, lists SE-updatable columns for each, and
confirms the expectation format declared in the Registry before proceeding). Then produces CS-1,
CS-2, CS-3 using Registry schemas. CS does not fill TABLE_1-5. Handoff to PHASE 2.

**PHASE 2 — SE:** Executes in privilege-tier order. SE-0 (admin-tier inventory + TABLE_4
escalation vectors) runs before SE-1 (role-operation matrix), establishing the privilege ceiling
before populating operation cells. TABLE_1 and TABLE_3 include Tier column. CONTEXT-CLOSES
attestations at SE-2, SE-3, SE-4 per SHALL-G. Handoff to PHASE 3.

**PHASE 3 — CA-1:** Double-anchor verification. CA-1.1 through CA-1.8 (CA-1.8 extended to verify
CS-0 acknowledgment precedes CS-1). Terminal verdict.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1 and 0.2 before any other phase begins.*

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

**All table schemas declared centrally by CA. Blank-cell prohibition is global. SE-update
protocols for CS-2 and CS-3 declared co-located with schema entry.**

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Tier values: Admin / Custom / Restricted. Rows ordered: Admin tier first, Custom tier second,
Restricted tier last. Blank-cell rule: all cells Granted / Denied / Conditional (condition inline) / N/A.

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
Note: TABLE_4 executes at SE-0 (before TABLE_1) because admin-tier and sharing-rule vectors
establish the privilege ceiling that shapes TABLE_1 interpretation.

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation`
Blank-cell rule: Remediation = exact object + exact location + expected post-fix state.
CS-EXPECTATION-VIOLATED Remediation: three-field block (CS-Expected / SE-Actual / Delta).

**Schema ID: CS-2 — Sharing Rule Expectations (CS-authored expectation table)**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference (TABLE_4 row ID or TABLE_5 row ID),
SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE update protocol: SE populates SE Cross-Reference and SE Confirmation after TABLE_4 analysis
at SE-0. CONTRADICTED triggers CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

**Schema ID: CS-3 — Cross-Role Access Differential Expectations (CS-authored expectation table)**
Declared columns: `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
SE-updatable columns: SE Cross-Reference (TABLE_1 row ID or TABLE_3 row ID),
SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE update protocol: SE populates SE Cross-Reference and SE Confirmation after TABLE_1/TABLE_3
analysis. CONTRADICTED triggers CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

**Declared rule: M1, M2, M3 simultaneously active. M4 pre-assigned.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-0 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-0 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**SHALL obligations:**
- SHALL-A: Complete TABLE_1 with Tier column. Every cell Granted/Denied/Conditional/N/A. Rows ordered by tier.
- SHALL-B: TABLE_2 lists all sensitive fields with explicit FLS status. Null case explicit. Gap? YES rows in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Effective Scope filled. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 all four vectors at SE-0, Checked? = YES. Rule-outs name specific mechanism and reason.
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap case requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field Remediation block. Incomplete rows MUST be reopened. CA-1.6 verifies.
- SHALL-G: SE-2, SE-3, and SE-4 each open with CONTEXT-CLOSES attestation co-located at sub-section opening naming the specific CONTEXT blind spot (using the exact label from the CONTEXT section) that this sub-section closes. Closure notes consolidated in TABLE_5 or the terminal checklist fail SHALL-G.

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Schema Registry Acknowledgment + Lower-Trust Access Baseline

*CS opens with CS-0 Schema Registry acknowledgment before any expectation content.*

### CS-0 — Schema Registry Acknowledgment (CS-authored, Phase 1)

CS acknowledges the Schema Registry entries for CS-2 and CS-3 before authoring expectation rows.
This sub-section confirms the handoff from CA's Phase 0 Registry to CS's Phase 1 authoring task.

**Registry acknowledgment for CS-2:**
Schema ID: CS-2 — Sharing Rule Expectations.
SE-updatable columns as declared by CA in Phase 0 Registry: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged: SE will populate SE Cross-Reference (TABLE_4 row or TABLE_5 row
ID) and SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE) after TABLE_4 analysis.
Expectation format confirmed: CS-2 rows authored using columns Rule Name | Trigger | Expected
Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation.
SE-updatable columns left blank by CS; SE fills after SE-0.

**Registry acknowledgment for CS-3:**
Schema ID: CS-3 — Cross-Role Access Differential Expectations.
SE-updatable columns as declared by CA in Phase 0 Registry: SE Cross-Reference, SE Confirmation.
SE-update protocol acknowledged: SE will populate SE Cross-Reference (TABLE_1 or TABLE_3 row ID)
and SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE) after SE-1/SE-3 analysis.
Expectation format confirmed: CS-3 rows authored using columns Entity | Operation | CS Role
Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential |
SE Cross-Reference | SE Confirmation. SE-updatable columns left blank by CS; SE fills after SE-1/SE-3.

### CS-1 — Expected Customer Service Access Baseline

For each entity in scope: (a) which CRUD operations the CS role is expected to perform as part of
normal job function; (b) the expected record scope; (c) which sensitive fields CS is expected to
need read or write access to and why. Identify any configuration CS relies on that may
inadvertently open access beyond job requirements.

**CS-2 — Sharing rule expectations** *(Schema Registry CS-2 — SE-updatable columns blank; SE
fills after SE-0)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

**CS-3 — Cross-role access differential** *(Schema Registry CS-3 — SE-updatable columns blank;
SE fills after SE-1/SE-3)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis (Privilege-Tier Descent Order)

*SE traces from highest-privilege tier to lowest. SE-0 establishes admin-tier ceiling and
TABLE_4 escalation vectors before SE-1 role-operation matrix.*

### SE-0 — Admin-Tier Inventory and Escalation Vectors (before TABLE_1)

**Admin-tier role inventory:** List System Administrator, Environment Admin, and any
admin-equivalent roles. For each: record scope (System Administrator = org-wide always), key
operations, and whether any admin capability bypasses lower-tier controls (e.g., System
Administrator overrides column security profiles). This establishes the privilege ceiling against
which all lower-tier roles are evaluated in SE-1.

**TABLE_4 — Escalation Vector Inventory** *(Schema Registry TABLE_4; placed at SE-0 because
admin-tier role structure determines escalation paths before lower-tier role matrix is populated)*

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Finding format: `[Role] -> [Mechanism] -> [Elevated access achieved]` for confirmed escalation;
for rule-out: "Checked [mechanism]: no path found because [specific reason]." After TABLE_4:
populate CS-2 SE Cross-Reference and SE Confirmation. CONTRADICTED rows trigger
CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

### SE-1 / SHALL-A — Section 1: Role-Operation Matrix

**TABLE_1 — Role-Operation Matrix** *(Schema Registry TABLE_1 with Tier column; blank-cell rule)*

| Role | Tier | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Rows ordered: Admin tier first, Custom tier second, Restricted tier last. Admin-tier roles cite
SE-0 privilege ceiling in Record Scope or notes where applicable. After TABLE_1: populate CS-3
SE Cross-Reference and SE Confirmation. Note confirmations and CONTRADICTED rows.

**Cross-role differential analysis:** Compare the CS role against at least one Admin-tier role
and one Custom-tier role for the same entity and operation. Cite SE-0 TABLE_4 data for any
differential that stems from admin-tier escalation vectors (e.g., "System Administrator
org-wide scope confirmed by SE-0 TABLE_4 row: Admin / environment role override").

### SE-2 / SHALL-B — Section 2: Field-Level Security Coverage

> CONTEXT-CLOSES: Blind spot 1 — Post-incident FLS gap — This section provides explicit FLS
> status per sensitive field, closing the manual audit failure mode where column security profile
> gaps are discovered only after a data exposure incident.

**TABLE_2 — FLS Coverage** *(Schema Registry TABLE_2; blank-cell rule)*

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Note: System Administrator bypasses column security profiles regardless of FLS configuration.
Document this admin-tier override in the defense-in-depth layer check. Forward Gap? YES rows
to TABLE_5 with Tier column populated.

**Defense-in-depth layer check:** Identify the enforcement layer where field access is granted or
denied for at least one sensitive field. For Admin-tier roles, note the SE-0 finding confirming
bypass status.

### SE-3 / SHALL-C — Section 3: Record Access Scope

> CONTEXT-CLOSES: Blind spot 2 — Cumulative privilege blind spot — This section maps the effective
> access scope for every role including the combined effect of security role privilege + team
> membership + OWD, which no single Dataverse UI view surfaces.

**TABLE_3 — Record Scope by Role** *(Schema Registry TABLE_3 with Tier column; blank-cell rule)*

| Role | Tier | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role MUST appear, ordered by Tier (Admin first). Note any role where effective
scope exceeds role-only scope due to team membership. Enter such cases as CS-EXPECTATION-VIOLATED
in TABLE_5 if CS-3 expected the tighter scope. After TABLE_3: update CS-3 SE Confirmation.

### SE-4 / SHALL-D — Section 4: Privilege Escalation Cross-Reference

> CONTEXT-CLOSES: Blind spot 3 — OWD-sharing-rule override gap — This section cross-references
> sharing rule triggers against OWD settings, surfacing cases where a Private or BU OWD is
> silently overridden by an active sharing rule that manual OWD-only review would not detect.

TABLE_4 was filled in SE-0. This section adds the cross-role differential summary citing SE-0
data: for the most privileged Admin-tier role and the most restricted Restricted-tier role,
identify the specific Dataverse enforcement layer (1: environment/admin from SE-0 TABLE_4, 2:
security role + BU, 3: team membership, 4: column security profile) where access diverges.
State whether the divergence is expected (least privilege satisfied) and cite the specific SE-0
TABLE_4 row ID that established the Admin-tier ceiling.

### SE-5 / SHALL-E — Section 5: Security Gap Inventory

**TABLE_5 — Security Gap Inventory** *(Schema Registry TABLE_5 with Tier column; blank-cell rule)*

| # | Gap Type | Entity | Field or Rule | Role | Tier | Severity | Remediation |
|---|----------|--------|---------------|------|------|----------|-------------|

CS-EXPECTATION-VIOLATED rows: CS-Expected / SE-Actual / Delta (three-field per SHALL-F).

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

*CA returns. Labeled-element double-anchor structure.*

**CA-1.1 — C-01 verification** *(Phase 0 M4 pre-assignment CA-1.1)*:
- Registry anchor — Schema ID TABLE_1 (with Tier): [Role, Tier, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope] — blank cells prohibited globally.
- Preamble anchor — C-01 as authored by CA in Phase 0: TABLE_1 / SE-1 / SHALL-A / CA-1.1 — verifying...
- Verification — TABLE_1 present? Tier column populated? Rows ordered by tier? All cells filled? -> PASS / FAIL

**CA-1.2 — C-02 verification** *(Phase 0 M4 pre-assignment CA-1.2)*:
- Registry anchor — Schema ID TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?] — blank cells prohibited globally.
- Preamble anchor — C-02 as authored by CA in Phase 0: TABLE_2 / SE-2 / SHALL-B / CA-1.2 — verifying...
- Verification — TABLE_2 present? All sensitive fields? FLS status explicit? Admin-tier override noted? -> PASS / FAIL

**CA-1.3 — C-03 verification** *(Phase 0 M4 pre-assignment CA-1.3)*:
- Registry anchor — Schema ID TABLE_3 (with Tier): [Role, Tier, OWD Baseline, Scope Modifier, Effective Scope, Verified?] — blank cells prohibited globally.
- Preamble anchor — C-03 as authored by CA in Phase 0: TABLE_3 / SE-0+SE-3 / SHALL-C / CA-1.3 — verifying...
- Verification — Every TABLE_1 role in TABLE_3? Tier column populated? Effective Scope filled? -> PASS / FAIL

**CA-1.4 — C-04 verification** *(Phase 0 M4 pre-assignment CA-1.4)*:
- Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity] — all four vectors, Checked? = YES.
- Preamble anchor — C-04 as authored by CA in Phase 0: TABLE_4 / SE-0 / SHALL-D / CA-1.4 — verifying...
- Verification — TABLE_4 at SE-0 (before TABLE_1)? All four vectors? Findings or specific rule-outs? -> PASS / FAIL

**CA-1.5 — C-05 verification** *(Phase 0 M4 pre-assignment CA-1.5)*:
- Registry anchor — Schema ID TABLE_5 (with Tier): [#, Gap Type, Entity, Field or Rule, Role, Tier, Severity, Remediation] — blank cells prohibited globally.
- Preamble anchor — C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 — verifying...
- Verification — TABLE_5 present? Named gap? Tier column populated? Remediations exact? -> PASS / FAIL

**CA-1.6 — SHALL-F compliance** *(CS-EXPECTATION-VIOLATED three-field structure)*:
- Registry anchor — TABLE_5 CS-EXPECTATION-VIOLATED row: three-field Remediation block — CS-Expected, SE-Actual, Delta — all three required per SHALL-F.
- Preamble anchor — SHALL-F as authored by CA in Phase 0: three-field structure mandatory; incomplete rows reopened.
- Verification — Each CS-EXPECTATION-VIOLATED row: CS-Expected? SE-Actual? Delta exact? -> PASS / FAIL per row.

**CA-1.7 — SHALL-G compliance** *(CONTEXT-CLOSES attestations)*:
- Registry anchor — CONTEXT section names Blind spots 1/2/3 with exact labels. SHALL-G requires CONTEXT-CLOSES co-located at SE-2/SE-3/SE-4 openings naming the specific blind spot.
- Preamble anchor — SHALL-G as authored by CA in Phase 0: CONTEXT-CLOSES at sub-section openings; TABLE_5 or checklist consolidation fails.
- Verification — SE-2 opens with CONTEXT-CLOSES naming Blind spot 1? SE-3 Blind spot 2? SE-4 Blind spot 3? -> PASS / FAIL.

**CA-1.8 — CS-2/CS-3 Schema Registry registration + CS-0 acknowledgment verification** *(C-29 + C-33)*:
- Registry anchor — Schema Registry declared CS-2 and CS-3 as named schema entries with SE-updatable columns and SE-update protocols. PHASE 1 mandate requires CS-0 sub-section to acknowledge these Registry entries before CS-1/CS-2/CS-3.
- Preamble anchor — CS-2 and CS-3 in Schema Registry alongside TABLE_1-5. CS-0 acknowledgment precedes CS-1 as Phase 1 structural requirement. SE-update protocols cited in CS-0.
- Verification — CS-2 in Registry? CS-3 in Registry? CS-0 present before CS-1? CS-0 cites both schema IDs and lists SE-updatable columns? SE populated SE-updatable columns per protocol? -> PASS / FAIL

**CA Format Compliance Verdict — Phase 0 citation:**
Citing: CA-authored Schema Registry (Step 0.1, Phase 0), CA-authored preamble (Step 0.2, Phase 0).
[CA-1.1 through CA-1.8 results. Overall: COMPLIANT / NON-COMPLIANT. Open items attributed.]

---

## V-03 — Single-Axis Phrasing Register: Imperative Numbered-Step Voice

**Axis:** Phrasing register — all instruction prose rewritten as numbered execution steps with
explicit MUST imperatives and execution verbs. Same mechanism coverage as R11-V-01: 7-schema
Registry, SHALL-A through SHALL-G, CA-1.1 through CA-1.8, single-line CONTEXT-CLOSES, no SE-0,
no CS-0 acknowledgment. Tests whether imperative register alters structural compliance detection.
**Hypothesis:** 22/25 (same base criteria; no aspirational axis added).

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

Manual security reviews of Dataverse environments routinely miss three failure scenarios:

**Blind spot 1 — Post-incident FLS gap.** Column security profiles are not audited proactively.
Sensitive fields remain accessible until a data exposure event surfaces the gap.

**Blind spot 2 — Cumulative privilege blind spot.** Role + team + OWD combined access is never
surfaced by a single Dataverse UI view. Spot-checks miss team-accumulated scope elevation.

**Blind spot 3 — OWD-sharing-rule override gap.** OWD and sharing rules are audited separately.
Active sharing rules silently override Private OWD baselines in ways neither audit detects alone.

This trace closes all three blind spots. SE-2 closes Blind spot 1. SE-3 closes Blind spot 2.
SE-4 closes Blind spot 3.

---

## EXECUTION MANDATE: FOUR PHASES IN ORDER

Execute the following four phases in strict sequence. Each phase MUST complete before the next
begins. Phase header labels MUST appear exactly as written. Output a phase-transition handoff
string naming the next phase before advancing.

**1. Execute PHASE 0 — CA first.** CA is the sole author of all structural schemas. CA MUST
produce the Schema Registry (Step 0.1) and the Criterion Enforcement Matrix preamble (Step 0.2)
before any other content is generated.

**2. Execute PHASE 1 — CS second.** CS MUST produce CS-1, CS-2, and CS-3 using the schemas
declared in the PHASE 0 Registry. CS MUST NOT fill TABLE_1 through TABLE_5.

**3. Execute PHASE 2 — SE third.** SE MUST fill TABLE_1 through TABLE_5 using Dataverse-native
terminology exclusively. SE MUST populate the SE-updatable columns in CS-2 and CS-3.
SE MUST open each of SE-2, SE-3, and SE-4 with a CONTEXT-CLOSES attestation per SHALL-G.

**4. Execute PHASE 3 — CA-1 last.** CA MUST return and execute one verification row per
criterion. Each row MUST contain a Registry anchor, a Preamble anchor, and a Verification line
as structurally distinct labeled elements. Inline concatenation of both anchors fails C-24.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

### Step 0.1 — Schema Registry

1. Declare Schema ID TABLE_1 — Role-Operation Matrix.
   - Columns: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
   - MUST apply blank-cell rule globally: every cell carries Granted / Denied / Conditional / N/A.

2. Declare Schema ID TABLE_2 — FLS Coverage.
   - Columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
   - MUST apply: FLS Profile Configured? = Configured / Not Configured. Gap? = YES / NO. Never blank.

3. Declare Schema ID TABLE_3 — Record Scope by Role.
   - Columns: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
   - MUST apply: Effective Scope = Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[name]. Never blank.

4. Declare Schema ID TABLE_4 — Escalation Vector Inventory.
   - Columns: `Vector | Checked? | Finding | Severity`
   - MUST include all four vectors. Checked? = YES for all. Finding = path or specific rule-out. Never blank.

5. Declare Schema ID TABLE_5 — Security Gap Inventory.
   - Columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
   - Remediation MUST name exact object, exact location, and expected post-fix state.
   - CS-EXPECTATION-VIOLATED Remediation MUST contain three-field block:
     - CS-Expected: cite CS-2 or CS-3 row verbatim or by row reference.
     - SE-Actual: state the SE finding that contradicts the expectation.
     - Delta: exact configuration change to align SE-Actual to CS-Expected.

6. Declare Schema ID CS-2 — Sharing Rule Expectations.
   - Columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
   - SE-updatable columns: SE Cross-Reference (populate with TABLE_4 row ID or TABLE_5 row ID after TABLE_4 analysis); SE Confirmation (populate with CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
   - SE update protocol: SE fills SE Cross-Reference and SE Confirmation after completing TABLE_4. CONTRADICTED triggers CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F.

7. Declare Schema ID CS-3 — Cross-Role Access Differential Expectations.
   - Columns: `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
   - SE-updatable columns: SE Cross-Reference (TABLE_1 row or TABLE_3 row ID); SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
   - SE update protocol: SE fills after TABLE_1 and TABLE_3 analysis. CONTRADICTED triggers CS-EXPECTATION-VIOLATED per SHALL-F.

### Step 0.2 — Criterion Enforcement Matrix Preamble

Declare the following enforcement matrix. All four mechanism columns (M1-M4) are simultaneously
active for every row. M4 CA verification row IDs are pre-assigned contract obligations.

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

Declare the following SHALL obligations:

- SHALL-A: Produce a complete TABLE_1. Every cell MUST carry Granted / Denied / Conditional / N/A. Every role with any privilege on any entity in {{topic}} MUST appear.
- SHALL-B: Produce TABLE_2 listing every PII, Financial, or Audit-Compliance field with explicit FLS status. Null case MUST be stated explicitly. Forward all Gap? YES rows to TABLE_5.
- SHALL-C: Every TABLE_1 role MUST appear in TABLE_3 with a filled Effective Scope. Ambiguous scope MUST be forwarded to TABLE_5.
- SHALL-D: TABLE_4 MUST contain all four escalation vectors with Checked? = YES. Each rule-out MUST name the specific mechanism and the specific reason no path exists.
- SHALL-E: TABLE_5 MUST contain at least one gap row with a named field, role, or rule. Zero-gap case MUST include explicit evidence rows confirming what was checked and found clear.
- SHALL-F: Every CS-2 or CS-3 expectation that conflicts with an SE finding MUST be recorded in TABLE_5 as CS-EXPECTATION-VIOLATED. Each such row MUST carry all three fields of the three-field Remediation block. Rows missing any field MUST be reopened. CA-1.6 enforces.
- SHALL-G: Sub-sections SE-2, SE-3, and SE-4 MUST each open with a CONTEXT-CLOSES attestation co-located at the sub-section opening, naming the specific CONTEXT blind spot (using the exact label from the CONTEXT section above) that this sub-section closes. Placing closure notes in TABLE_5 or the terminal checklist instead of at the sub-section opening fails SHALL-G.

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Lower-Trust Access Baseline and Expectation Tables

1. Produce CS-1 — Expected Customer Service access baseline.
   - For each entity in scope, state: (a) expected CRUD operations for normal CS job function;
     (b) expected record scope; (c) which sensitive fields CS needs read or write access to and why.
   - Identify configurations that may inadvertently expand CS access beyond job requirements.

2. Produce CS-2 — Sharing rule expectations using Schema Registry CS-2 schema.
   - SE-updatable columns (SE Cross-Reference, SE Confirmation) MUST be left blank by CS.
   - For each Potential Overreach? YES row: name the access path and the most likely over-reached role.

   | Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
   |-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

3. Produce CS-3 — Cross-role access differential using Schema Registry CS-3 schema.
   - SE-updatable columns MUST be left blank by CS.
   - MUST include at minimum one entity and one operation where CS has less access than the Comparison Role.
   - Name any sharing rule that might unexpectedly close the differential.

   | Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
   |--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis

Execute sections SE-1 through SE-5 in order. Use Dataverse-native terminology exclusively.
Populate SE-updatable columns in CS-2 and CS-3 at the designated points.

### SE-1 / SHALL-A — Role-Operation Matrix

1. Produce TABLE_1 using Schema Registry TABLE_1 schema. Include every role with any privilege
   on any entity in {{topic}}.
2. Fill every cell: Granted / Denied / Conditional (state condition inline) / N/A.
3. After TABLE_1: populate CS-3 SE Cross-Reference and SE Confirmation. Document confirmations
   (cite CS-3 row) and contradictions (record CS-EXPECTATION-VIOLATED in TABLE_5 per SHALL-F).
4. Produce cross-role differential analysis: compare CS role vs. at least one more-privileged
   role for the same entity and operation. State whether differential is expected or anomalous.

**TABLE_1 — Role-Operation Matrix** *(Schema Registry TABLE_1; blank-cell rule global)*

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

### SE-2 / SHALL-B — Field-Level Security Coverage

> CONTEXT-CLOSES: Blind spot 1 — Post-incident FLS gap — Explicit FLS status per sensitive field
> closes the manual audit failure mode of discovering column security profile gaps post-incident.

1. Check Security > Column Security Profiles for all entities in scope.
2. Produce TABLE_2 using Schema Registry TABLE_2 schema. Assign Category: PII / Financial /
   Audit-Compliance / Other-Sensitive. State null case explicitly if no profiles are active.
3. Forward all Gap? YES rows to TABLE_5.
4. Produce defense-in-depth layer check: identify the enforcement layer for at least one sensitive
   field; explain why the layer above it does not override.

**TABLE_2 — FLS Coverage** *(Schema Registry TABLE_2; blank-cell rule global)*

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

### SE-3 / SHALL-C — Record Access Scope

> CONTEXT-CLOSES: Blind spot 2 — Cumulative privilege blind spot — Mapping role + team + OWD
> combined effective scope closes the single-UI-view gap that causes team-accumulated privilege
> to go undetected in manual spot-checks.

1. Produce TABLE_3 using Schema Registry TABLE_3 schema. Every TABLE_1 role MUST appear.
2. Record OWD Baseline (Private / Business Unit / Parent-Child BU / Organization), Scope Modifier
   (role depth, owner team, access team, or sharing rule), and Effective Scope.
3. Flag any role where effective scope exceeds role-only scope due to team membership.
4. Populate CS-3 SE Cross-Reference and SE Confirmation for record-scope differential rows.
   Enter CONTRADICTED rows in TABLE_5 as CS-EXPECTATION-VIOLATED per SHALL-F.

**TABLE_3 — Record Scope by Role** *(Schema Registry TABLE_3; blank-cell rule global)*

| Role | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|--------------|----------------|-----------------|-----------|

### SE-4 / SHALL-D — Privilege Escalation Analysis

> CONTEXT-CLOSES: Blind spot 3 — OWD-sharing-rule override gap — Cross-referencing sharing rule
> triggers against OWD settings surfaces silent Private-OWD overrides that neither OWD-only nor
> sharing-rule-only audits detect.

1. Produce TABLE_4 using Schema Registry TABLE_4 schema. Check all four vectors.
2. For each confirmed escalation, record format: `[Role] -> [Mechanism] -> [Elevated access achieved]`.
3. For each rule-out, record: "Checked [mechanism]: no path found because [specific reason naming
   the specific configuration examined]."
4. Populate CS-2 SE Cross-Reference and SE Confirmation. Enter CONTRADICTED rows in TABLE_5 per SHALL-F.

**TABLE_4 — Escalation Vector Inventory** *(Schema Registry TABLE_4; all four vectors required)*

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

### SE-5 / SHALL-E — Security Gap Inventory

1. Produce TABLE_5 using Schema Registry TABLE_5 schema. Include at minimum one named gap.
2. Use gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.
3. Remediation MUST name exact object, exact Power Platform Admin Center location, and expected post-fix state.
4. CS-EXPECTATION-VIOLATED rows MUST carry the three-field block: CS-Expected / SE-Actual / Delta.

**TABLE_5 — Security Gap Inventory** *(Schema Registry TABLE_5; blank-cell rule global)*

| # | Gap Type | Entity | Field or Rule | Role | Severity | Remediation |
|---|----------|--------|---------------|------|----------|-------------|

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

Execute one verification row per criterion. Each row MUST contain: Registry anchor (cite schema
ID and declared columns), Preamble anchor (quote preamble row values as authored in Phase 0),
and Verification line. Both anchors MUST appear as structurally distinct labeled elements.
Inline concatenation fails C-24.

**CA-1.1 — C-01:**
- Registry anchor — Schema ID TABLE_1: [Role, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope] — blank cells prohibited globally.
- Preamble anchor — C-01 as authored by CA in Phase 0: TABLE_1 / SE-1 / SHALL-A / CA-1.1.
- Verification — TABLE_1 produced? Every cell Granted/Denied/Conditional/N/A? All roles present? -> PASS / FAIL

**CA-1.2 — C-02:**
- Registry anchor — Schema ID TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?] — blank cells prohibited globally.
- Preamble anchor — C-02 as authored by CA in Phase 0: TABLE_2 / SE-2 / SHALL-B / CA-1.2.
- Verification — TABLE_2 produced? All sensitive fields? FLS status explicit? Null case stated? Gap? YES in TABLE_5? -> PASS / FAIL

**CA-1.3 — C-03:**
- Registry anchor — Schema ID TABLE_3: [Role, OWD Baseline, Scope Modifier, Effective Scope, Verified?] — blank cells prohibited globally.
- Preamble anchor — C-03 as authored by CA in Phase 0: TABLE_3 / SE-1+SE-3 / SHALL-C / CA-1.3.
- Verification — Every TABLE_1 role in TABLE_3? Effective Scope filled? Ambiguous scope in TABLE_5? -> PASS / FAIL

**CA-1.4 — C-04:**
- Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity] — all four vectors, Checked? = YES.
- Preamble anchor — C-04 as authored by CA in Phase 0: TABLE_4 / SE-4 / SHALL-D / CA-1.4.
- Verification — TABLE_4 produced? All four vectors? Checked? = YES? Findings or specific rule-outs? -> PASS / FAIL

**CA-1.5 — C-05:**
- Registry anchor — Schema ID TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Severity, Remediation] — blank cells prohibited globally.
- Preamble anchor — C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5.
- Verification — TABLE_5 produced? Named gap with specific field/role/rule? Remediations exact? -> PASS / FAIL

**CA-1.6 — SHALL-F:**
- Registry anchor — Schema ID TABLE_5 CS-EXPECTATION-VIOLATED row: [CS-Expected, SE-Actual, Delta] — all three required per SHALL-F.
- Preamble anchor — SHALL-F as declared in Phase 0: CS-EXPECTATION-VIOLATED rows must carry three-field block; incomplete rows must be reopened.
- Verification — For each CS-EXPECTATION-VIOLATED row: CS-Expected present? SE-Actual present? Delta is exact configuration change? -> PASS / FAIL per row.

**CA-1.7 — SHALL-G:**
- Registry anchor — CONTEXT section exact labels: "Blind spot 1 — Post-incident FLS gap" (SE-2), "Blind spot 2 — Cumulative privilege blind spot" (SE-3), "Blind spot 3 — OWD-sharing-rule override gap" (SE-4). SHALL-G requires CONTEXT-CLOSES naming exact label at sub-section opening.
- Preamble anchor — SHALL-G as declared in Phase 0: co-located attestation at SE-2/SE-3/SE-4 openings; TABLE_5 consolidation fails.
- Verification — SE-2 CONTEXT-CLOSES at opening? Exact label cited? SE-3 same? SE-4 same? -> PASS / FAIL per section.

**CA-1.8 — C-29 Schema Registry registration:**
- Registry anchor — Schema Registry entries CS-2 and CS-3 with SE-updatable columns (SE Cross-Reference, SE Confirmation) and SE-update protocols declared co-located.
- Preamble anchor — CS-2 and CS-3 appear as named Schema Registry entries alongside TABLE_1-5 with SE-update protocols.
- Verification — CS-2 in Registry with SE-updatable column declarations? CS-3 same? SE populated both? -> PASS / FAIL

**CA Format Compliance Verdict — Phase 0 citation:**
[CA-1.1 through CA-1.8 results. Overall COMPLIANT / NON-COMPLIANT. Open items attributed.]

---

## V-04 — Single-Axis TABLE_3 Scope Expansion: Team Membership Decomposition

**Axis:** TABLE_3 schema expansion — adds Team Membership column (listing all owner teams a role
participates in) and Team Role Scope column (the privilege depth granted by the team role). SE-3
adds explicit team-by-team scope computation before Effective Scope is determined. Tests whether
granular team decomposition strengthens C-03/C-10 signal. Same mechanism base as R11-V-01.
**Hypothesis:** 22/25 (no new aspirational axes).

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: MANUAL RBAC AUDIT BLIND SPOTS

Manual security reviews of Dataverse environments routinely miss three failure scenarios:

**Blind spot 1 — Post-incident FLS gap.** Column security profiles are not audited proactively.
Sensitive fields remain readable and writable unless a column security profile explicitly restricts
them. Gaps emerge after data exposure.

**Blind spot 2 — Cumulative privilege blind spot.** A user's effective access is the combination
of security role privilege depth, team membership, and OWD. No single UI view surfaces this.
Spot-checking individual roles misses team-accumulated scope.

**Blind spot 3 — OWD-sharing-rule override gap.** OWD and sharing rules are reviewed separately.
A Private OWD combined with an active sharing rule creates effective broader access that neither
review catches in isolation.

This trace closes all three blind spots: SE-2 closes Blind spot 1; SE-3 closes Blind spot 2;
SE-4 closes Blind spot 3.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. Phase labels MUST appear as section headers.

**PHASE 0 — CA:** Authors Schema Registry (7 schemas: TABLE_1-5 + CS-2 + CS-3; TABLE_3 extended
with Team Membership and Team Role Scope columns) and preamble (SHALL-A through SHALL-G; M4
CA-1.1 through CA-1.8 pre-assigned). Handoff to PHASE 1.

**PHASE 1 — CS:** Produces CS-1, CS-2, CS-3 using Registry schemas. Handoff to PHASE 2.

**PHASE 2 — SE:** Fills TABLE_1-5. TABLE_3 uses expanded schema — SE decomposes team membership
per role before computing Effective Scope. CONTEXT-CLOSES at SE-2, SE-3, SE-4 per SHALL-G.
Handoff to PHASE 3.

**PHASE 3 — CA-1:** Double-anchor verification. CA-1.1 through CA-1.8. Terminal verdict.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

### Step 0.1 — Schema Registry (CA-authored, Phase 0)

**Global blank-cell prohibition. SE-update protocols co-located with CS-2/CS-3 entries.**

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Blank-cell rule: Granted / Denied / Conditional (condition inline) / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Blank-cell rule: Configured / Not Configured; YES / NO.

**Schema ID: TABLE_3 — Record Scope by Role (expanded)**
Declared columns: `Role | OWD Baseline | Team Membership | Team Role Scope | Scope Modifier | Effective Scope | Verified?`
Team Membership: list all owner teams the role participates in; "None" if no owner teams.
Team Role Scope: the privilege depth granted by the team's associated security role (Own / BU /
Parent-Child BU / Org-wide); "N/A" if Team Membership = None.
Scope Modifier: the net effect on scope from team membership relative to the base security role
(e.g., "Owner team grants Org-wide, elevating BU-scoped role to Org-wide").
Effective Scope: Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].
Verified? = YES / NO. Blank-cell rule applies to all columns.

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
Blank-cell rule: four vectors, Checked? = YES, Finding = path or specific rule-out.

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
CS-EXPECTATION-VIOLATED Remediation: CS-Expected / SE-Actual / Delta (three-field block).

**Schema ID: CS-2 — Sharing Rule Expectations**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference (TABLE_4 row ID), SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE update protocol: SE fills after TABLE_4. CONTRADICTED triggers CS-EXPECTATION-VIOLATED per SHALL-F.

**Schema ID: CS-3 — Cross-Role Access Differential Expectations**
Declared columns: `Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation`
SE-updatable: SE Cross-Reference (TABLE_1 or TABLE_3 row ID), SE Confirmation (CONFIRMED / CONTRADICTED / NOT-APPLICABLE).
SE update protocol: SE fills after TABLE_1/TABLE_3. CONTRADICTED triggers CS-EXPECTATION-VIOLATED per SHALL-F.

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored, Phase 0)

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**SHALL obligations:**
- SHALL-A: Complete TABLE_1. Every cell Granted/Denied/Conditional/N/A. All roles present.
- SHALL-B: TABLE_2 lists all sensitive fields with explicit FLS status. Null case explicit. Gap? YES rows in TABLE_5.
- SHALL-C: Every TABLE_1 role MUST appear in TABLE_3 with Team Membership, Team Role Scope, and Effective Scope filled. Any role where Effective Scope exceeds base role scope due to Team Role Scope elevation MUST be flagged; CS-EXPECTATION-VIOLATED if CS-3 expected the unexpanded scope.
- SHALL-D: TABLE_4 all four vectors, Checked? = YES. Rule-outs name specific mechanism and reason.
- SHALL-E: TABLE_5 has at least one named gap. Zero-gap case requires explicit evidence rows.
- SHALL-F: CS-EXPECTATION-VIOLATED rows MUST carry three-field Remediation block. Incomplete rows reopened. CA-1.6 verifies.
- SHALL-G: SE-2, SE-3, SE-4 each open with CONTEXT-CLOSES co-located at sub-section opening, naming the exact CONTEXT blind spot label. TABLE_5 consolidation fails SHALL-G.

*Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Lower-Trust Access Baseline and Expectation Tables

**CS-1 — Expected CS access baseline:** Expected operations, record scope, and sensitive field
access for the Customer Service role. Flag configurations that may expand access beyond job function.

**CS-2** *(Schema Registry CS-2; SE fills SE Cross-Reference and SE Confirmation after TABLE_4)*:

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference | SE Confirmation |
|-----------|---------|------------------------|-----------------------|---------------------|---------------------|-----------------|

**CS-3** *(Schema Registry CS-3; SE fills SE Cross-Reference and SE Confirmation after TABLE_1/TABLE_3)*:

| Entity | Operation | CS Role Expected Access | Comparison Role | Comparison Role Expected Access | Expected Differential | SE Cross-Reference | SE Confirmation |
|--------|-----------|------------------------|-----------------|---------------------------------|-----------------------|---------------------|-----------------|

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis

### SE-1 / SHALL-A — Role-Operation Matrix

**TABLE_1** *(Schema Registry TABLE_1; blank-cell rule)*:

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

After TABLE_1: populate CS-3 SE Cross-Reference and SE Confirmation. Cross-role differential:
compare CS role vs. at least one more-privileged role; state whether differential is expected.

### SE-2 / SHALL-B — Field-Level Security Coverage

> CONTEXT-CLOSES: Blind spot 1 — Post-incident FLS gap — Explicit FLS status per sensitive field
> closes the post-incident gap-discovery failure mode.

**TABLE_2** *(Schema Registry TABLE_2; blank-cell rule)*:

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Forward Gap? YES rows to TABLE_5. Defense-in-depth layer: identify the enforcement layer for at
least one sensitive field.

### SE-3 / SHALL-C — Record Access Scope (Team Membership Decomposition)

> CONTEXT-CLOSES: Blind spot 2 — Cumulative privilege blind spot — Decomposing team membership
> per role and computing the net Effective Scope closes the spot-check gap where team-accumulated
> privilege is invisible in individual role views.

For each role, explicitly enumerate all owner teams the role participates in before computing
Effective Scope. If a role belongs to multiple owner teams, evaluate each team's security role
privilege depth independently, then derive the net Effective Scope as the maximum privilege
granted by role + team combination.

**TABLE_3** *(Schema Registry TABLE_3 expanded; blank-cell rule)*:

| Role | OWD Baseline | Team Membership | Team Role Scope | Scope Modifier | Effective Scope | Verified? |
|------|--------------|-----------------|-----------------|----------------|-----------------|-----------|

Every TABLE_1 role MUST appear. After TABLE_3: populate CS-3 SE Confirmation for scope
differential expectations. CONTRADICTED rows trigger CS-EXPECTATION-VIOLATED per SHALL-F.

### SE-4 / SHALL-D — Privilege Escalation Analysis

> CONTEXT-CLOSES: Blind spot 3 — OWD-sharing-rule override gap — Cross-referencing sharing rule
> triggers against OWD settings surfaces silent overrides that OWD-only review misses.

**TABLE_4** *(Schema Registry TABLE_4; all four vectors required)*:

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

After TABLE_4: populate CS-2 SE Cross-Reference and SE Confirmation. CONTRADICTED rows trigger
CS-EXPECTATION-VIOLATED per SHALL-F.

### SE-5 / SHALL-E — Security Gap Inventory

**TABLE_5** *(Schema Registry TABLE_5; blank-cell rule)*:

| # | Gap Type | Entity | Field or Rule | Role | Severity | Remediation |
|---|----------|--------|---------------|------|----------|-------------|

CS-EXPECTATION-VIOLATED rows: CS-Expected / SE-Actual / Delta (three-field per SHALL-F).

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

**CA-1.1 — C-01:**
- Registry anchor — Schema ID TABLE_1: [Role, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope] — blank cells prohibited.
- Preamble anchor — C-01 as authored by CA in Phase 0: TABLE_1 / SE-1 / SHALL-A / CA-1.1.
- Verification — TABLE_1 present? All cells filled? All roles? -> PASS / FAIL

**CA-1.2 — C-02:**
- Registry anchor — Schema ID TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?] — blank cells prohibited.
- Preamble anchor — C-02 as authored by CA in Phase 0: TABLE_2 / SE-2 / SHALL-B / CA-1.2.
- Verification — TABLE_2 present? All sensitive fields? FLS status? Null case? Gap? YES in TABLE_5? -> PASS / FAIL

**CA-1.3 — C-03:**
- Registry anchor — Schema ID TABLE_3 expanded: [Role, OWD Baseline, Team Membership, Team Role Scope, Scope Modifier, Effective Scope, Verified?] — blank cells prohibited.
- Preamble anchor — C-03 as authored by CA in Phase 0: TABLE_3 / SE-1+SE-3 / SHALL-C / CA-1.3.
- Verification — Every TABLE_1 role in TABLE_3? Team Membership column filled? Effective Scope filled? Elevation cases in TABLE_5? -> PASS / FAIL

**CA-1.4 — C-04:**
- Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity] — all four, Checked? = YES.
- Preamble anchor — C-04 as authored by CA in Phase 0: TABLE_4 / SE-4 / SHALL-D / CA-1.4.
- Verification — TABLE_4 present? All four vectors? Findings or specific rule-outs? -> PASS / FAIL

**CA-1.5 — C-05:**
- Registry anchor — Schema ID TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Severity, Remediation] — blank cells prohibited.
- Preamble anchor — C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5.
- Verification — TABLE_5 present? Named gap? Remediations exact? -> PASS / FAIL

**CA-1.6 — SHALL-F:**
- Registry anchor — CS-EXPECTATION-VIOLATED Remediation: three-field block [CS-Expected, SE-Actual, Delta] per SHALL-F.
- Preamble anchor — SHALL-F: three-field mandatory; incomplete rows reopened.
- Verification — Each CS-EXPECTATION-VIOLATED row: CS-Expected? SE-Actual? Delta exact? -> PASS / FAIL per row.

**CA-1.7 — SHALL-G:**
- Registry anchor — CONTEXT labels: "Blind spot 1 — Post-incident FLS gap" (SE-2), "Blind spot 2 — Cumulative privilege blind spot" (SE-3), "Blind spot 3 — OWD-sharing-rule override gap" (SE-4). Co-located attestation required.
- Preamble anchor — SHALL-G: CONTEXT-CLOSES at sub-section openings; consolidation elsewhere fails.
- Verification — SE-2/SE-3/SE-4 each open with CONTEXT-CLOSES? Exact labels? -> PASS / FAIL.

**CA-1.8 — C-29:**
- Registry anchor — CS-2 in Schema Registry with SE-updatable columns declared. CS-3 same.
- Preamble anchor — CS-2 and CS-3 as named Registry entries with SE-update protocols co-located.
- Verification — Both in Registry? SE-updatable columns declared? SE populated them? -> PASS / FAIL

**CA Format Compliance Verdict — Phase 0 citation:**
[CA-1.1 through CA-1.8 results. Overall: COMPLIANT / NON-COMPLIANT.]

---

## V-05 — Full Combination C-31+C-32+C-33: The 25/25 Candidate

**Axis:** All three aspirational axes combined on the R11-V-01 base — SE-0 TABLE_4 before TABLE_1
with Tier columns in TABLE_1/TABLE_3 and SE-4 citing SE-0 data (C-31); exact-label two-part
`MANUAL GAP [<exact label>]:` / `STRUCTURED CLOSE:` blocks at SE-2/SE-3/SE-4 with SHALL-G
exact-label mandate (C-32); CS-0 Registry acknowledgment sub-section before CS-1/CS-2/CS-3 with
CA-1.8 extended to verify CS-0 precedes CS-1 (C-33).
**Hypothesis:** 25/25.

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
TABLE_4 (filled at SE-0) evaluated all four escalation vectors with sharing rules explicitly
cross-referenced against OWD settings. This section adds cross-tier differential summary citing
SE-0 data: for the most privileged Admin-tier role and the most restricted Restricted-tier role,
identify the specific enforcement layer where access diverges, citing the SE-0 TABLE_4 row ID
that established the admin-tier ceiling. State whether the divergence is expected and what
sharing-rule interaction (if any) was confirmed or ruled out in SE-0 TABLE_4.

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
