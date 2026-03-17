# trace-permissions Variate — Round 8 (rubric v8 — C-26/C-27/C-28 target)
**Date:** 2026-03-15
**Rubric:** v8 (C-01 through C-28 — C-26/C-27/C-28 added from Round 7 excellence signals)
**Target criteria:** C-26 (placement-site verbatim), C-27 (dual-mechanism at declaration sites), C-28 (INDEX completeness threshold)

**State entering Round 8:**

| Variation | v7 score | Gap under v8 |
|-----------|----------|--------------|
| R7-V-05 (best v7) | 180/180 | Missing C-26/C-27/C-28 (-15 pts) = 180/195 |
| R10-V-01 (CS-first + CONTEXT) | 20/20 criteria | Reference architecture — all prior criteria satisfied |

Round 8 holds the R10 structural core (CA -> CS -> SE -> CA-1, Schema Registry, CONTEXT section, double-anchor) and adds C-26/C-27/C-28 mechanisms across three single-axis tests and two combined variations.

---

## Round 8 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Lifecycle emphasis — C-26 isolation: inline verbatim placement markers at Phase 0 declaration sites only; no downstream RULE blocks; no INDEX extension | C-26 requires the verbatim pass-condition phrase to appear AT the declaration site itself. Adding PLACEMENT-CRITERION-CONFIRMED annotations immediately after the TABLE_5 Remediation schema entry, the Criterion Enforcement Matrix co-authorship note, the Phase 0 gate header, and the CA-1 verdict precondition declaration embeds the exact rubric phrase at each enforcement point. No downstream RULE blocks -- C-27 fails by design. No INDEX -- C-28 fails. Isolated test: +5 pts (C-26 only). |
| V-02 | Output format — C-27 full dual-mechanism: V-01 Phase 0 placement markers plus RULE blocks at every application site (SE-2 for C-22, CA-1.5 for C-16, CA-1 verdict for C-23/C-24) | C-27 requires both mechanisms: inline verbatim at the declaration site AND a RULE block at the downstream application site. V-02 adds V-01's Phase 0 verbatim markers and also embeds RULE(C-NN) blockquotes at the SE and CA-1 application sites. No INDEX extension -- C-28 still fails. Hypothesis: +5 (C-26) + 5 (C-27) = 10 pts gain. |
| V-03 | Phrasing register — C-28 isolation: extended ENFORCEMENT LANGUAGE INDEX with completeness-threshold header and declaration-site/application-site status columns; no V-01/V-02 dual-mechanism additions | C-28 requires the INDEX to list every enforcement point and distinguish declaration-site from application-site coverage. The INDEX header explicitly states the threshold rule: N-1 of N earns 0 pts. Status columns confirm per-row coverage type. No inline verbatim at Phase 0 sites (C-26 fails), no RULE blocks at application sites (C-27 fails). Isolated test: +5 pts (C-28 only) if INDEX structure alone satisfies the threshold criterion. |
| V-04 | Combined C-26 + C-27, SE-first role sequence: dual-mechanism (Phase 0 verbatim + downstream RULE blocks) without INDEX; SE executes before CS | V-01 proved inline verbatim at Phase 0; V-02 proved downstream RULE blocks. V-04 combines both under an SE-first role sequence (SE -> CS -> CA-1) to stress-test whether the dual-mechanism survives a different phase order. C-28 excluded to maintain single combination variable on the new axis. Hypothesis: +10 pts (C-26 + C-27); C-28 fails. |
| V-05 | Full combination C-26 + C-27 + C-28: dual-mechanism at all Phase 0 declaration sites, extended INDEX with completeness threshold and status confirmation, Phase 0 close includes N/N coverage count | Maximum coverage. V-01 inline verbatim + V-02 RULE blocks + V-03 INDEX extension. INDEX includes DECLARATION-SITE and APPLICATION-SITE confirmation columns. Phase 0 close writes a coverage count: "N/N enforcement points: declaration-site CONFIRMED, application-site CONFIRMED." Hypothesis: +5 (C-26) + 5 (C-27) + 5 (C-28) = 15 pts; achieves 195/195. |

---

## V-01 — Single-Axis: Declaration-Site Verbatim (C-26 target)

**Axis:** Lifecycle emphasis — inline verbatim placement markers at Phase 0 declaration sites only
**Hypothesis:** +5 pts (C-26); C-27 fails (no downstream RULE blocks); C-28 fails (no INDEX extension). Isolated test of whether placement-site embedding alone satisfies C-26.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: Why a Permissions Trace Is Not Optional

Three inertia patterns defeat manual security audits:

**Blind spot 1 — Post-incident FLS discovery.** Field-level security gaps are typically found after a breach, not before. FLS profiles must be examined before incidents occur. This trace replaces post-incident discovery with pre-incident enumeration.

**Blind spot 2 — Cumulative privilege accumulation.** Security role scope, team membership, OWD, and sharing rules each grant partial access. No single Dataverse UI view shows their combined effect. This trace maps the effective scope produced by all four layers together.

**Blind spot 3 — OWD-sharing-rule override.** An org-wide default set to Private can be silently re-opened by a sharing rule configured independently. This trace cross-references OWD settings against active sharing rules to surface unintended access grants.

Each SE section in Phase 2 opens with a CONTEXT-CLOSES label naming the blind spot it resolves.

---

## ROLE SEQUENCING MANDATE

This output executes in four explicitly labeled phases. Phase labels MUST appear as section headers. Each phase completes fully before the next begins. Phase boundaries include explicit handoff strings.

**PHASE 0 — CA (Compliance Auditor):** CA executes first. CA is the sole author of the Schema Registry (Step 0.1), the Criterion Enforcement Matrix preamble (Step 0.2), and the Phase 0 gate statement. CA issues handoff to PHASE 1.

**PHASE 1 — CS (Customer Service):** CS executes second. CS produces the qualitative access baseline and expectation tables using Schema Registry schemas. CS does NOT fill TABLE_1-5. CS issues handoff to PHASE 2.

**PHASE 2 — SE (Dataverse Security Expert):** SE executes third. SE fills TABLE_1-5 using Dataverse-native terminology throughout. SE references CS expectation tables by Schema ID. CS-EXPECTATION-VIOLATED rows in TABLE_5 use the three-field Remediation structure declared in the Schema Registry. SE issues handoff to PHASE 3.

**PHASE 3 — CA-1 (CA Verification Pass):** CA returns. Each CA-1 row presents Registry anchor and Preamble anchor as structurally distinct labeled lines before the Verification line. CA's terminal verdict cites Phase 0 by label.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

*CA executes Steps 0.1, 0.2, and the Phase 0 gate statement before any other phase begins.*

### Step 0.1 — Schema Registry (CA-authored)

**All table schemas declared centrally by CA. Blank-cell prohibition is global.**

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Blank-cell rule: every cell MUST carry Granted / Denied / Conditional (state condition inline) / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Blank-cell rule: FLS Profile Configured? = Configured / Not Configured. Gap? = YES / NO. Gap? = YES rows forward to TABLE_5.

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name]. Verified? = YES / NO.

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
Blank-cell rule: all four vectors required (team inheritance, sharing rules, impersonation, admin/env override). Checked? = YES for all. Finding = escalation path OR explicit rule-out with specific mechanism and reason.

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Enumerated gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.
Remediation field format (three required sub-fields):
  - Config change: exact configuration object, its location in the Dataverse security editor, and the change to apply.
  - Expected state: the specific UI view, profile row, or query result that will differ after the fix.
  - Verification step: the named action a reviewer executes to confirm the fix took effect.

> PLACEMENT-CRITERION CONFIRMED (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" — the TABLE_5 Remediation schema above is that declaration. The three-field format (config change / expected state / verification step) is established here, before PHASE 1 begins, ensuring verification-relevant details are observed during the evidence window.

**Schema ID: CS-2 — Sharing Rule Expectations (CS-authored)**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference`
SE Cross-Reference: CS fills as "TBD — await SE Phase 2"; SE updates with TABLE_4 or TABLE_5 row reference.

**Schema ID: CS-3 — Cross-Role Differential Expectations (CS-authored)**
Declared columns: `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation`
SE Confirmation: CS fills as "TBD — await SE Phase 2"; SE updates with TABLE_1 or TABLE_3 reference and CONFIRMED or CS-EXPECTATION-VIOLATED.

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored)

**M1, M2, M3 are simultaneously active for every essential criterion — not alternative paths. M4 pre-assigned by CA.**

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

The Gap? boolean column in TABLE_2 is the per-row commit signal for FLS co-authorship: the model marks YES/NO while filling each TABLE_2 row, and the deterministic follow-through is forwarding Gap? = YES rows to TABLE_5 before the next row begins.

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" — this Criterion Enforcement Matrix preamble declares the Gap? boolean column as the structural enforcement mechanism. Confirmed here, at Phase 0, before PHASE 1 begins.

**SHALL obligations (CA-authored):**
- SHALL-A: TABLE_1 present. Every cell Granted / Denied / Conditional / N/A. Every role with any privilege included.
- SHALL-B: TABLE_2 lists every sensitive field with explicit FLS status. Null case stated if no profiles active. Not Configured fields in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Effective Scope filled. Ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 checks all four escalation vectors. Rule-outs name specific mechanism and reason.
- SHALL-E: TABLE_5 contains at least one named gap. Zero-gap case: explicit evidence rows stating what was checked and confirmed safe.

### Phase 0 Gate Statement

This trace operates under a bidirectional audit structure. Both directions pre-established here.

Chain 1 — discovery to TABLE_5: every gap found during PHASE 2 is entered into TABLE_5 at the section where it is found, not deferred to a post-analysis compilation pass.
Chain 2 — TABLE_5 to CA-1 echo: every TABLE_5 Remediation entry is verified in PHASE 3 via double-anchor reaffirmation citing the Schema Registry schema and the preamble row.

> PLACEMENT-CRITERION CONFIRMED (C-23): "execution record, not declarative checklist" — this Phase 0 gate statement records that both chains are already active as of Phase 0 close. The CA-1 verdict in PHASE 3 is the structural close condition for this trace; the trace is not closed until the verdict is written.

*All structures active at Phase 0 close. Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Lower-Trust Access Baseline

*CS produces CS-1 narrative plus CS-2 and CS-3 expectation tables. CS does not fill TABLE_1-5.*

**CS-1 — Expected Customer Service access baseline:**
For each entity in scope: (a) which CRUD operations the CS role performs as part of normal job function; (b) expected record scope (own records, BU-wide, etc.); (c) which sensitive fields CS is expected to need read or write access to and why. Name any sharing rules currently active that CS relies on for record access.

**CS-2 — Sharing rule expectations** (Schema Registry CS-2 schema; all columns except SE Cross-Reference filled by CS):

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference |
|-----------|---------|------------------------|-----------------------|---------------------|--------------------|
| | | | | | TBD — await SE Phase 2 |

For each Potential Overreach? = YES: name the access path and why it may exceed CS job function.

**CS-3 — Cross-role differential expectations** (Schema Registry CS-3 schema; all columns except SE Confirmation filled by CS):

| Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation |
|--------|-------------------|-------------------|--------------------------------|---------------|-----------------|
| | | | | | TBD — await SE Phase 2 |

Name the privileged role being compared. Identify at least one field or operation where CS should have less access. Note any sharing rule that might unexpectedly close that gap.

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis

*SE executes Sections 1 through 5 using Dataverse-native terminology. SE updates CS-2 SE Cross-Reference and CS-3 SE Confirmation columns. CS-EXPECTATION-VIOLATED entries in TABLE_5 use the three-field Remediation format declared in the Schema Registry.*

### SE-1 / SHALL-A — Section 1: Role-Operation Matrix

**CONTEXT-CLOSES: cumulative privilege accumulation** — TABLE_1 maps every role's operations and record scope in one view, including the combined effect of security role depth, team membership, and OWD that no single Dataverse UI surfaces.

**TABLE_1 — Role-Operation Matrix** (Schema Registry TABLE_1 schema; blank-cell rule applies)

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Include every role with any privilege on any entity in {{topic}}. Record Scope: Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name]. After the table, update CS-3 SE Confirmation for the CS row: cite TABLE_1 row and state CONFIRMED or CS-EXPECTATION-VIOLATED.

### SE-2 / SHALL-B — Section 2: Field-Level Security Coverage

**CONTEXT-CLOSES: post-incident FLS discovery** — Explicit FLS status per sensitive field, checked before incidents occur.

**TABLE_2 — FLS Coverage** (Schema Registry TABLE_2 schema; blank-cell rule applies; Gap? boolean is per-row commit signal per Phase 0 preamble)

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Sensitive field categories: PII / Financial / Audit-Compliance / Operational. Check Security > Column Security Profiles for all entities in scope. Null case: "No column security profiles active. Sensitive fields identified: [list]. All entered in TABLE_5." Forward all Gap? = YES rows to TABLE_5 before beginning the next row.

Negative-check evidence: for each sensitive field category that yields no Gap? = YES entry, state explicitly what was examined and why no gap applies. Acceptable format: "Checked [profiles] for [role]; [category] fields do not apply because [reason]."

### SE-3 / SHALL-C — Section 3: Record Access Scope

**CONTEXT-CLOSES: OWD-sharing-rule override** — Effective scope mapped per role including team membership and sharing rule overlays.

**TABLE_3 — Record Scope by Role** (Schema Registry TABLE_3 schema; blank-cell rule applies)

| Role | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role present. OWD: Private / Business Unit / Parent-Child BU / Organization. Scope Modifier: security role privilege depth + team membership (owner team or access team) + sharing rule override.

Defense-in-depth layer assessment: for at least one operation, name the specific Dataverse enforcement layer (1: environment/admin, 2: security role + BU, 3: team membership, 4: column security profiles) where access is granted or denied, and state why higher layers do not override.

Update CS-3 SE Confirmation for scope rows.

### SE-4 / SHALL-D — Section 4: Privilege Escalation Analysis

**TABLE_4 — Escalation Vector Inventory** (Schema Registry TABLE_4 schema; all four vectors required)

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

For each finding: `[Role] -> [Action] -> [Elevated access achieved]`. For each rule-out: "Checked [mechanism]: no path found because [specific reason]." Update CS-2 SE Cross-Reference for each sharing rule row.

Per-role escalation rule-out: when no escalation path is found for a role, provide one explicit rule-out per traced role naming the specific actions checked and why none permit elevation. A blanket "no escalation paths found" covering all roles does not pass.

### SE-5 / SHALL-E — Section 5: Security Gap Inventory

**TABLE_5 — Security Gap Inventory** (Schema Registry TABLE_5 schema; blank-cell rule applies; Remediation follows three-field format declared in Schema Registry)

| # | Gap Type | Entity | Field or Rule | Role | Severity | Remediation |
|---|----------|--------|---------------|------|----------|-------------|

CS-EXPECTATION-VIOLATED Remediation: (1) CS expectation — cite Schema ID CS-2 or CS-3 and row; (2) SE finding contradicting it; (3) exact configuration change with expected state and verification step.

Cross-entity permission chain: if any TABLE_5 gap involves a multi-entity lookup dependency, trace the chain showing the permission at each entity hop (at least two hops).

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

*CA returns. Each CA-1 row presents Registry anchor and Preamble anchor as structurally distinct, independently readable labeled lines before the Verification line. Inline concatenation of both anchors fails. CA-1 verdict is the structural close condition for this trace.*

> PLACEMENT-CRITERION CONFIRMED (C-24): "precondition for closing the trace, not a recommended step" — the CA-1 verdict below is that precondition. The trace is not closed until the CA-1 verdict is written and all five criteria have a PASS or FAIL disposition.

**CA-1.1 — C-01 verification (completing Phase 0 M4 pre-assignment CA-1.1):**
Registry anchor — Schema ID TABLE_1: [Role, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope] — blank cells prohibited.
Preamble anchor — C-01 as authored by CA in Phase 0: TABLE_1 / SE-1 / SHALL-A / CA-1.1 — verifying...
Verification — TABLE_1 present? All cells filled (Granted/Denied/Conditional/N/A)? All roles included? -> PASS / FAIL

**CA-1.2 — C-02 verification (completing Phase 0 M4 pre-assignment CA-1.2):**
Registry anchor — Schema ID TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?] — blank cells prohibited.
Preamble anchor — C-02 as authored by CA in Phase 0: TABLE_2 / SE-2 / SHALL-B / CA-1.2 — verifying...
Verification — TABLE_2 present? Sensitive fields with FLS status? Null case stated? Gap? = YES rows in TABLE_5? -> PASS / FAIL

**CA-1.3 — C-03 verification (completing Phase 0 M4 pre-assignment CA-1.3):**
Registry anchor — Schema ID TABLE_3: [Role, OWD Baseline, Scope Modifier, Effective Scope, Verified?] — blank cells prohibited.
Preamble anchor — C-03 as authored by CA in Phase 0: TABLE_3 / SE-1+SE-3 / SHALL-C / CA-1.3 — verifying...
Verification — Every TABLE_1 role in TABLE_3? Effective Scope filled for all? Ambiguous scope in TABLE_5? -> PASS / FAIL

**CA-1.4 — C-04 verification (completing Phase 0 M4 pre-assignment CA-1.4):**
Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity] — all four vectors, Checked? = YES.
Preamble anchor — C-04 as authored by CA in Phase 0: TABLE_4 / SE-4 / SHALL-D / CA-1.4 — verifying...
Verification — TABLE_4 present? All four vectors? Checked? = YES? Each with finding or specific rule-out? Per-role escalation rule-outs present? -> PASS / FAIL

**CA-1.5 — C-05 verification (completing Phase 0 M4 pre-assignment CA-1.5):**
Registry anchor — Schema ID TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Severity, Remediation] — blank cells prohibited.
Preamble anchor — C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 — verifying...
Verification — TABLE_5 present? Named gap with specific field/role/rule? Remediations contain all three sub-fields (config change / expected state / verification step)? CS-EXPECTATION-VIOLATED rows structured correctly? -> PASS / FAIL

**CA Format Compliance Verdict — citing Phase 0:**
Citing: CA-authored Schema Registry (Step 0.1), CA-authored preamble (Step 0.2), Phase 0 gate statement — all authored by CA before PHASE 1 began.
[C-01 through C-05 disposition. Overall: COMPLIANT / NON-COMPLIANT. Open items with responsible role.]

[TRACE CLOSED — CA-1 verdict written; precondition satisfied.]

---

## V-02 — Single-Axis: Dual-Mechanism Coverage (C-27 target)

**Axis:** Output format — V-01 Phase 0 placement markers retained; RULE blocks added at every application site (SE-2 for C-22, CA-1.5 for C-16, CA-1 verdict for C-23/C-24)
**Hypothesis:** +5 (C-26) + 5 (C-27) = 10 pts gain; C-28 fails (no INDEX extension). RULE blocks at application sites confirm the downstream half of the dual-mechanism requirement.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: Why a Permissions Trace Is Not Optional

Three inertia patterns defeat manual security audits:

**Blind spot 1 — Post-incident FLS discovery.** FLS gaps are found after breaches, not before. This trace replaces post-incident discovery with pre-incident enumeration.

**Blind spot 2 — Cumulative privilege accumulation.** Security role scope, team membership, OWD, and sharing rules each grant partial access; no single Dataverse UI shows their combined effect. This trace maps effective scope from all four layers.

**Blind spot 3 — OWD-sharing-rule override.** A Private OWD can be silently re-opened by a sharing rule. This trace cross-references OWD against active sharing rules to surface unintended access.

---

## ROLE SEQUENCING MANDATE

Four phases. Labels appear as section headers. Each completes before the next begins.

**PHASE 0 — CA:** Schema Registry (Step 0.1), Criterion Enforcement Matrix preamble (Step 0.2), Phase 0 gate. Sole author of all structural artifacts.
**PHASE 1 — CS:** Qualitative baseline + expectation tables using Registry schemas. Does NOT fill TABLE_1-5.
**PHASE 2 — SE:** Fills TABLE_1-5. Dataverse-native terminology throughout. References CS expectation tables by Schema ID.
**PHASE 3 — CA-1:** Double-anchor verification per criterion. Terminal verdict cites Phase 0 by label.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

### Step 0.1 — Schema Registry (CA-authored)

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Blank-cell rule: every cell Granted / Denied / Conditional (state condition inline) / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Blank-cell rule: Gap? = YES / NO. Gap? = YES rows forward to TABLE_5.

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
All four vectors required. Checked? = YES for all. Finding = escalation path or specific rule-out.

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Remediation three-field format: (1) Config change — exact object, location, change to apply. (2) Expected state — specific UI view or result after fix. (3) Verification step — named action a reviewer executes.

> PLACEMENT-CRITERION CONFIRMED (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" — the TABLE_5 Remediation three-field format is that declaration. It is established here, before PHASE 1, so verification-relevant details are collected during the evidence window, not reconstructed afterward.

**Schema ID: CS-2 — Sharing Rule Expectations (CS-authored)**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference`

**Schema ID: CS-3 — Cross-Role Differential Expectations (CS-authored)**
Declared columns: `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation`

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored)

M1, M2, M3 simultaneously active. M4 pre-assigned by CA.

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

The Gap? boolean in TABLE_2 is the per-row commit signal declared here. Each TABLE_2 row: mark Gap? = YES/NO, then forward YES rows to TABLE_5 before beginning the next row.

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" — this preamble declaration establishes the Gap? column as the structural enforcement mechanism. Confirmed at this Phase 0 site. The downstream RULE block at SE-2 confirms activation at the application site.

**SHALL obligations:**
- SHALL-A: TABLE_1 present; every cell Granted/Denied/Conditional/N/A; every role included.
- SHALL-B: TABLE_2 lists every sensitive field with FLS status; null case stated; Not Configured fields in TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Effective Scope filled; ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 checks all four vectors; rule-outs name specific mechanism and reason; per-role rule-out for negative cases.
- SHALL-E: TABLE_5 contains at least one named gap; zero-gap case requires explicit evidence rows.

### Phase 0 Gate Statement

> PLACEMENT-CRITERION CONFIRMED (C-23): "execution record, not declarative checklist" — this gate statement records that Chain 1 (discovery to TABLE_5), Chain 2 (TABLE_5 to CA-1 verification), and the Gap? per-row trigger are all active as of Phase 0 close. Each mechanism is already engaged, not scheduled for future activation.

> PLACEMENT-CRITERION CONFIRMED (C-24): "precondition for closing the trace, not a recommended step" — the CA-1 Format Compliance Verdict in PHASE 3 is that precondition. This trace is not closed until the verdict is written. The downstream RULE block at the CA-1 verdict confirms activation at the application site.

*All structures active. Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Lower-Trust Access Baseline

**CS-1 — Expected Customer Service access baseline:** For each entity: (a) expected CRUD operations; (b) expected record scope; (c) sensitive fields CS needs and why. Name active sharing rules CS relies on.

**CS-2 — Sharing rule expectations** (Schema Registry CS-2 schema):

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference |
|-----------|---------|------------------------|-----------------------|---------------------|--------------------|
| | | | | | TBD — await SE Phase 2 |

**CS-3 — Cross-role differential expectations** (Schema Registry CS-3 schema):

| Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation |
|--------|-------------------|-------------------|--------------------------------|---------------|-----------------|
| | | | | | TBD — await SE Phase 2 |

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis

### SE-1 / SHALL-A — Role-Operation Matrix

**CONTEXT-CLOSES: cumulative privilege accumulation**

**TABLE_1** (Schema Registry TABLE_1 schema; blank-cell rule applies)

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Every role with any privilege included. After table, update CS-3 SE Confirmation for CS row.

### SE-2 / SHALL-B — Field-Level Security Coverage

**CONTEXT-CLOSES: post-incident FLS discovery**

> RULE (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" — each TABLE_2 Gap? cell is the per-row commit signal. Mark YES/NO while filling each row. Forward Gap? = YES rows to TABLE_5 before beginning the next row. N/A rows are confirmed by Gap? = NO entry; trigger completeness is provable from TABLE_2 column alone.

**TABLE_2** (Schema Registry TABLE_2 schema; Gap? boolean per-row trigger ACTIVE per Phase 0 preamble and this RULE)

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Sensitive categories: PII / Financial / Audit-Compliance / Operational. Check Security > Column Security Profiles. Null case: state explicitly with fields listed. For each category with no Gap? = YES, state: "Checked [profiles] for [role]; [category] does not apply because [reason]."

### SE-3 / SHALL-C — Record Access Scope

**CONTEXT-CLOSES: OWD-sharing-rule override**

**TABLE_3** (Schema Registry TABLE_3 schema; blank-cell rule applies)

| Role | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role present. Defense-in-depth layer assessment: name the specific enforcement layer (1–4) for at least one operation. Update CS-3 SE Confirmation for scope rows.

### SE-4 / SHALL-D — Privilege Escalation Analysis

**TABLE_4** (Schema Registry TABLE_4 schema; all four vectors required)

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Each finding: `[Role] -> [Action] -> [Elevated access achieved]`. Each rule-out: "Checked [mechanism]: no path because [reason]." Per-role rule-out when no escalation found: one explicit rule-out per traced role. Update CS-2 SE Cross-Reference for each sharing rule row.

### SE-5 / SHALL-E — Security Gap Inventory

**TABLE_5** (Schema Registry TABLE_5 schema; Remediation three-field format per Schema Registry declaration)

| # | Gap Type | Entity | Field or Rule | Role | Severity | Remediation |
|---|----------|--------|---------------|------|----------|-------------|

CS-EXPECTATION-VIOLATED rows: (1) CS expectation with CS-2/CS-3 cite; (2) SE finding; (3) configuration change.

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

*Registry anchor and Preamble anchor as structurally distinct labeled lines before Verification. Inline concatenation fails.*

**CA-1.1:** Registry anchor — Schema ID TABLE_1: [Role, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope]. Preamble anchor — C-01: TABLE_1 / SE-1 / SHALL-A / CA-1.1. Verification — TABLE_1 present? All cells filled? All roles? -> PASS / FAIL

**CA-1.2:** Registry anchor — Schema ID TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?]. Preamble anchor — C-02: TABLE_2 / SE-2 / SHALL-B / CA-1.2. Verification — TABLE_2 present? FLS status per sensitive field? Null case stated? Gap? = YES in TABLE_5? -> PASS / FAIL

**CA-1.3:** Registry anchor — Schema ID TABLE_3: [Role, OWD Baseline, Scope Modifier, Effective Scope, Verified?]. Preamble anchor — C-03: TABLE_3 / SE-1+SE-3 / SHALL-C / CA-1.3. Verification — Every TABLE_1 role in TABLE_3? Effective Scope filled? -> PASS / FAIL

**CA-1.4:** Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity]. Preamble anchor — C-04: TABLE_4 / SE-4 / SHALL-D / CA-1.4. Verification — All four vectors? Checked? = YES? Per-role rule-outs for negative cases? -> PASS / FAIL

**CA-1.5:** Registry anchor — Schema ID TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Severity, Remediation]. Preamble anchor — C-05: TABLE_5 / SE-5 / SHALL-E / CA-1.5.

> RULE (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" — the TABLE_5 Remediation three-field schema was declared by CA in Phase 0 Step 0.1, before PHASE 1 began. This CA-1.5 verification confirms that TABLE_5 rows follow the format established at that declaration site.

Verification — TABLE_5 present? Named gap? Remediations contain all three sub-fields? CS-EXPECTATION-VIOLATED rows structured correctly? -> PASS / FAIL

**CA Format Compliance Verdict — citing Phase 0:**
Citing: CA-authored Schema Registry (Step 0.1), CA-authored preamble (Step 0.2), Phase 0 gate statement — all established before PHASE 1 began.

> RULE (C-23): "execution record, not declarative checklist" — Phase 0 gate recorded that all chains were active before evidence collection began. This verdict confirms those mechanisms ran as recorded.

> RULE (C-24): "precondition for closing the trace, not a recommended step" — this verdict is that precondition. Writing it below closes the trace.

[C-01 through C-05 disposition. Overall: COMPLIANT / NON-COMPLIANT.]

[TRACE CLOSED — CA-1 verdict written; structural precondition satisfied.]

---

## V-03 — Single-Axis: INDEX Completeness Threshold (C-28 target)

**Axis:** Phrasing register — extended ENFORCEMENT LANGUAGE INDEX at Step 0.3 with completeness-threshold header, declaration-site and application-site status columns; no V-01/V-02 dual-mechanism additions
**Hypothesis:** +5 pts (C-28 only). C-26 fails (no inline verbatim at Phase 0 declaration sites). C-27 fails (no downstream RULE blocks). Tests whether the INDEX structure alone satisfies C-28's threshold criterion.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: Why a Permissions Trace Is Not Optional

Three inertia patterns defeat manual security audits:

**Blind spot 1 — Post-incident FLS discovery.** FLS gaps are found after breaches, not before. This trace replaces reactive discovery with pre-incident enumeration.

**Blind spot 2 — Cumulative privilege accumulation.** No single Dataverse UI shows the combined effect of security roles, team membership, OWD, and sharing rules. This trace maps effective scope from all four sources.

**Blind spot 3 — OWD-sharing-rule override.** A Private OWD can be silently opened by a sharing rule configured separately. This trace cross-references both to surface unintended access.

---

## ROLE SEQUENCING MANDATE

Four phases. Labels appear as section headers. Each completes fully before the next begins.

**PHASE 0 — CA:** Schema Registry (Step 0.1), Criterion Enforcement Matrix preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3), Phase 0 gate statement.
**PHASE 1 — CS:** Qualitative baseline and expectation tables. Does NOT fill TABLE_1-5.
**PHASE 2 — SE:** Fills TABLE_1-5. Dataverse-native terminology.
**PHASE 3 — CA-1:** Double-anchor verification. Terminal verdict cites Phase 0 by label.

---

## PHASE 0 — CA: SCHEMA REGISTRY, ENFORCEMENT PREAMBLE, AND LANGUAGE INDEX

### Step 0.1 — Schema Registry (CA-authored)

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Blank-cell rule: Granted / Denied / Conditional / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Gap? = YES / NO. Gap? = YES rows forward to TABLE_5.

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
All four vectors. Checked? = YES for all.

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Remediation three-field format: (1) Config change. (2) Expected state. (3) Verification step.

**Schema ID: CS-2 — Sharing Rule Expectations**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference`

**Schema ID: CS-3 — Cross-Role Differential Expectations**
Declared columns: `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation`

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored)

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**SHALL obligations:** SHALL-A through SHALL-E as in V-01 and V-02 above.

### Step 0.3 — ENFORCEMENT LANGUAGE INDEX (CA-authored)

**COMPLETENESS THRESHOLD: coverage of N-1 of N enforcement points earns 0 pts for C-25 — the same as 0 of N. The index enables gap detection; it does not close gaps. A trace that passes C-28 satisfies all three requirements: (a) this index lists every enforcement point, (b) every declaration-site enforcement point has inline verbatim confirmed, (c) every application-site enforcement point has a RULE block confirmed.**

| ID | Criterion | Enforcement Point | Verbatim Pass-Condition Phrase | Site Type | Coverage Status |
|----|-----------|-------------------|-------------------------------|-----------|-----------------|
| EL-01 | C-11 | Chain 1 declaration in Phase 0 gate | "entered into the findings log at that point in the output — not deferred to a summary section compiled after the fact" | DECLARATION-SITE | [CONFIRM: inline verbatim appears at Phase 0 gate] |
| EL-02 | C-12 | SE-2/SE-4 negative-check note | "Checked [list] for [role]; [gap type] does not apply because [reason]" | APPLICATION-SITE | [CONFIRM: RULE block appears at SE-2 and SE-4] |
| EL-03 | C-13 | TABLE_5 Remediation field definition | "expected system state after the fix is applied and how to verify the fix took effect" | DECLARATION-SITE | [CONFIRM: inline verbatim appears at Schema Registry TABLE_5] |
| EL-04 | C-14 | LIVE GAPS / TABLE_5 Discovered-In note | "enables auditing that C-11 inline registration actually occurred" | APPLICATION-SITE | [CONFIRM: RULE block appears at SE-5 or TABLE_5 instruction] |
| EL-05 | C-15 | SE-4 escalation rule-out instruction | "one explicit rule-out per traced role — naming the specific actions checked for that role and why none permit elevation" | APPLICATION-SITE | [CONFIRM: RULE block appears at SE-4] |
| EL-06 | C-16 | TABLE_5 Remediation schema declaration | "declared explicitly at the top of the trace output, before the first analysis phase begins" | DECLARATION-SITE | [CONFIRM: inline verbatim appears at Step 0.1 TABLE_5 entry] |
| EL-07 | C-17 | CA-1.5 / Phase 5 remediation echo | "remediation block that states the fix without linking back to the discovery section does not pass" | APPLICATION-SITE | [CONFIRM: RULE block appears at CA-1.5] |
| EL-08 | C-18 | TABLE_2 Gap? column note | "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" | DECLARATION-SITE | [CONFIRM: inline verbatim appears at Step 0.1 TABLE_2 entry] |
| EL-09 | C-22 | Criterion Enforcement Matrix co-authorship note | "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" | DECLARATION-SITE | [CONFIRM: inline verbatim appears at Step 0.2 preamble] |
| EL-10 | C-23 | Phase 0 gate header | "execution record, not declarative checklist" | DECLARATION-SITE | [CONFIRM: inline verbatim appears at Phase 0 gate statement] |
| EL-11 | C-24 | CA-1 verdict precondition declaration | "precondition for closing the trace, not a recommended step" | DECLARATION-SITE | [CONFIRM: inline verbatim appears at CA-1 verdict header] |

**Coverage count at Phase 0 close:** This index lists 11 enforcement points (EL-01 through EL-11). Each must have confirmed at-point coverage of the appropriate type. A trace that closes with fewer than 11/11 confirmed fails C-28 regardless of how many are confirmed. The index makes gaps detectable; confirmed at-point coverage is what constitutes compliance.

### Phase 0 Gate Statement

Chain 1 (discovery to TABLE_5), Chain 2 (TABLE_5 to CA-1 verification), and the Gap? per-row trigger are active as of Phase 0 close. The CA-1 verdict is the structural close condition for this trace.

*All structures active. Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Lower-Trust Access Baseline

**CS-1:** For each entity: expected CRUD operations, expected record scope, sensitive fields CS needs.

**CS-2** (Schema Registry CS-2 schema):

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference |
|-----------|---------|------------------------|-----------------------|---------------------|--------------------|
| | | | | | TBD — await SE Phase 2 |

**CS-3** (Schema Registry CS-3 schema):

| Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation |
|--------|-------------------|-------------------|--------------------------------|---------------|-----------------|
| | | | | | TBD — await SE Phase 2 |

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis

### SE-1 / SHALL-A — Role-Operation Matrix

**CONTEXT-CLOSES: cumulative privilege accumulation**

**TABLE_1** (blank-cell rule applies) | Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |

Every role with any privilege. Update CS-3 SE Confirmation for CS row after table.

### SE-2 / SHALL-B — Field-Level Security Coverage

**CONTEXT-CLOSES: post-incident FLS discovery**

**TABLE_2** (Gap? boolean per-row trigger active per Phase 0 preamble)

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Sensitive categories: PII / Financial / Audit-Compliance / Operational. Null case stated if no profiles active. For each category with no Gap? = YES, state: "Checked [profiles] for [role]; [category] does not apply because [reason]."

### SE-3 / SHALL-C — Record Access Scope

**CONTEXT-CLOSES: OWD-sharing-rule override**

**TABLE_3** | Role | OWD Baseline | Scope Modifier | Effective Scope | Verified? |

Every TABLE_1 role present. Defense-in-depth layer assessment for at least one operation. Update CS-3 SE Confirmation.

### SE-4 / SHALL-D — Privilege Escalation Analysis

**TABLE_4** (all four vectors required)

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Findings: `[Role] -> [Action] -> [Elevated access]`. Rule-outs: "Checked [mechanism]: no path because [reason]." Per-role rule-out when no escalation found. Update CS-2 SE Cross-Reference.

### SE-5 / SHALL-E — Security Gap Inventory

**TABLE_5** (Remediation three-field format per Schema Registry)

| # | Gap Type | Entity | Field or Rule | Role | Severity | Remediation |
|---|----------|--------|---------------|------|----------|-------------|

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

Each CA-1 row: Registry anchor and Preamble anchor as distinct labeled lines before Verification.

**CA-1.1:** Registry anchor — TABLE_1 schema. Preamble anchor — C-01: TABLE_1/SE-1/SHALL-A/CA-1.1. Verification -> PASS/FAIL

**CA-1.2:** Registry anchor — TABLE_2 schema. Preamble anchor — C-02: TABLE_2/SE-2/SHALL-B/CA-1.2. Verification -> PASS/FAIL

**CA-1.3:** Registry anchor — TABLE_3 schema. Preamble anchor — C-03: TABLE_3/SE-1+SE-3/SHALL-C/CA-1.3. Verification -> PASS/FAIL

**CA-1.4:** Registry anchor — TABLE_4 schema. Preamble anchor — C-04: TABLE_4/SE-4/SHALL-D/CA-1.4. Verification -> PASS/FAIL

**CA-1.5:** Registry anchor — TABLE_5 schema. Preamble anchor — C-05: TABLE_5/SE-5/SHALL-E/CA-1.5. Verification -> PASS/FAIL

**CA Format Compliance Verdict — citing Phase 0:**
Citing Schema Registry (Step 0.1), preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3), Phase 0 gate — all authored by CA before PHASE 1 began.

**INDEX COMPLETENESS CONFIRMATION (C-28):**
Reviewing Step 0.3 ENFORCEMENT LANGUAGE INDEX against this output:
[For each EL-01 through EL-11: confirm COVERAGE STATUS field can be marked CONFIRMED or note which coverage is absent.]
[Count: N/11 enforcement points with confirmed at-point coverage. If N < 11: C-28 = FAIL.]

[C-01 through C-05 disposition. Overall: COMPLIANT / NON-COMPLIANT.]

[TRACE CLOSED — CA-1 verdict written.]

---

## V-04 — Combined C-26 + C-27, SE-First Role Sequence

**Axis:** Combined C-26 + C-27 dual-mechanism (V-01 Phase 0 placement markers + V-02 downstream RULE blocks); SE executes before CS to stress-test whether dual-mechanism survives phase reordering; no INDEX extension
**Hypothesis:** +5 (C-26) + 5 (C-27) = 10 pts; C-28 fails. SE-first sequence: SE generates technical tables first; CS then reconciles against them. Dual-mechanism unchanged — declaration-site verbatim at Phase 0, RULE blocks at SE-2/CA-1.5/CA-1 verdict.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: Why a Permissions Trace Is Not Optional

Three inertia patterns defeat manual security audits:

**Blind spot 1 — Post-incident FLS discovery.** FLS gaps surface after breaches. This trace moves that detection to before incidents.

**Blind spot 2 — Cumulative privilege accumulation.** Effective scope cannot be read from a single UI view. This trace computes it across all four Dataverse enforcement layers.

**Blind spot 3 — OWD-sharing-rule override.** Private OWD + active sharing rule = unintended access. This trace surfaces that combination explicitly.

---

## ROLE SEQUENCING MANDATE

Four phases, SE-first variant. Phase labels appear as section headers.

**PHASE 0 — CA:** Schema Registry (Step 0.1), Criterion Enforcement Matrix preamble (Step 0.2), Phase 0 gate statement. CA is sole author.

**PHASE 1 — SE (Dataverse Security Expert):** SE executes first among analysts. Fills TABLE_1-5. SE does NOT consult CS output (none exists yet). SE flags any sharing rule or access differential that CS should respond to.

**PHASE 2 — CS (Customer Service):** CS executes second. Produces CS-1 narrative and updates CS-2/CS-3 expectation tables using SE's TABLE_1-5 as the confirmed technical baseline. CS confirms or challenges SE's record-scope and sharing-rule interpretations. CS-EXPECTATION-VIOLATED rows added to TABLE_5 where CS interpretation contradicts SE finding.

**PHASE 3 — CA-1 (CA Verification Pass):** CA returns. Double-anchor per criterion. Terminal verdict cites Phase 0 by label.

---

## PHASE 0 — CA: SCHEMA REGISTRY AND ENFORCEMENT PREAMBLE

### Step 0.1 — Schema Registry (CA-authored)

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Blank-cell rule: Granted / Denied / Conditional / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Gap? = YES / NO. Gap? = YES rows forward to TABLE_5 immediately (per-row commit before next row begins).

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
All four vectors. Checked? = YES for all.

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Remediation three-field format: (1) Config change — exact object, location, change to apply. (2) Expected state — specific UI view or result after fix. (3) Verification step — named executable action.

> PLACEMENT-CRITERION CONFIRMED (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" — TABLE_5 Remediation three-field schema is that declaration. Established here, before PHASE 1, so SE collects verification-relevant details during the evidence window. Downstream RULE (C-16) appears at CA-1.5.

**Schema ID: CS-2 — Sharing Rule Expectations (SE-authored in this SE-first variant)**
SE flags potential sharing rule overreach during PHASE 1. CS responds in PHASE 2 with intent/expectation. Declared columns: `Rule Name | SE Finding | SE Overreach Flag | CS Expected Intent | Resolved? | Resolution`

**Schema ID: CS-3 — Cross-Role Differential Expectations (SE-authored)**
SE identifies access differentials in PHASE 1. CS confirms or challenges in PHASE 2. Declared columns: `Entity | Field or Operation | SE-Observed CS Access | SE-Observed Privileged-Role Access | Gap Exists? | CS Interpretation`

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored)

M1, M2, M3 simultaneously active. M4 pre-assigned by CA. SE executes sections for M2.

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

The Gap? boolean in TABLE_2 is the per-row commit signal declared here at Phase 0.

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" — this preamble establishes the Gap? column as the structural enforcement mechanism. Confirmed at Phase 0 declaration site. Downstream RULE (C-22) appears at SE-2.

**SHALL obligations (SE-first variant):**
- SHALL-A: TABLE_1 present; every cell filled; every role included. SE is responsible author.
- SHALL-B: TABLE_2 lists every sensitive field; null case stated; Gap? = YES rows forwarded per-row.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Effective Scope filled.
- SHALL-D: All four escalation vectors checked; per-role rule-outs for negative cases.
- SHALL-E: TABLE_5 contains at least one named gap or explicit evidence rows for zero-gap case.

### Phase 0 Gate Statement

Chain 1 (discovery to TABLE_5), Chain 2 (TABLE_5 to CA-1 verification), and the Gap? per-row trigger are active.

> PLACEMENT-CRITERION CONFIRMED (C-23): "execution record, not declarative checklist" — this gate records confirmed activation of all chains before PHASE 1 begins. Downstream RULE (C-23) appears at CA-1 verdict.

> PLACEMENT-CRITERION CONFIRMED (C-24): "precondition for closing the trace, not a recommended step" — CA-1 verdict is that precondition. Downstream RULE (C-24) appears at CA-1 verdict close.

*All structures active. Handing to PHASE 1 — SE.*

---

## PHASE 1 — SE: Security Analysis (SE-first)

*SE executes without CS baseline. SE flags sharing rule overreach and access differentials for CS to respond to in PHASE 2.*

### SE-1 / SHALL-A — Role-Operation Matrix

**CONTEXT-CLOSES: cumulative privilege accumulation**

**TABLE_1** (blank-cell rule applies)

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Every role with any privilege. After table, flag any access differential worth CS attention (SE-authored CS-3 entry).

### SE-2 / SHALL-B — Field-Level Security Coverage

**CONTEXT-CLOSES: post-incident FLS discovery**

> RULE (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" — each TABLE_2 Gap? cell is the per-row commit signal. Mark YES/NO per row. Forward Gap? = YES rows to TABLE_5 before the next row begins.

**TABLE_2** (Gap? boolean per-row trigger ACTIVE per Phase 0 preamble and this RULE)

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Sensitive categories: PII / Financial / Audit-Compliance / Operational. Null case stated if no profiles active. Negative-check evidence for any category yielding no Gap? = YES: "Checked [profiles] for [role]; [category] does not apply because [reason]."

### SE-3 / SHALL-C — Record Access Scope

**CONTEXT-CLOSES: OWD-sharing-rule override**

**TABLE_3** | Role | OWD Baseline | Scope Modifier | Effective Scope | Verified? |

Every TABLE_1 role present. Defense-in-depth layer assessment for at least one operation.

### SE-4 / SHALL-D — Privilege Escalation Analysis

**TABLE_4** (all four vectors required; Checked? = YES for all)

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

Per-role rule-out when no escalation found. For sharing rules: populate CS-2 SE Finding and SE Overreach Flag columns.

### SE-5 / SHALL-E — Security Gap Inventory

**TABLE_5** (Remediation three-field format per Schema Registry)

| # | Gap Type | Entity | Field or Rule | Role | Severity | Remediation |
|---|----------|--------|---------------|------|----------|-------------|

*Handing to PHASE 2 — CS.*

---

## PHASE 2 — CS: Expectation Reconciliation (SE-first variant)

*CS reviews SE's TABLE_1-5 and responds to SE-authored CS-2/CS-3 entries. CS does NOT re-do SE's technical analysis.*

**CS-1 — Customer Service job-function baseline:**
Name any CS operation or record-scope expectation that contradicts SE's TABLE_1 or TABLE_3 entries. If CS expectations are fully confirmed by SE findings: state explicitly with TABLE_1/TABLE_3 row references.

**CS-2 reconciliation** (SE-authored schema; CS fills CS Expected Intent and Resolved? columns):

| Rule Name | SE Finding | SE Overreach Flag | CS Expected Intent | Resolved? | Resolution |
|-----------|-----------|-------------------|--------------------|-----------|------------|

For Resolved? = NO: add CS-EXPECTATION-VIOLATED row to TABLE_5.

**CS-3 reconciliation** (SE-authored schema; CS fills CS Interpretation column):

| Entity | Field or Operation | SE-Observed CS Access | SE-Observed Privileged-Role Access | Gap Exists? | CS Interpretation |
|--------|-------------------|----------------------|-----------------------------------|-------------|-------------------|

For CS Interpretation = contradicts SE: add CS-EXPECTATION-VIOLATED row to TABLE_5 with CS-2/CS-3 cite.

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

*Registry anchor and Preamble anchor as distinct labeled lines before Verification.*

**CA-1.1:** Registry anchor — TABLE_1: [Role, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope]. Preamble anchor — C-01: TABLE_1/SE-1/SHALL-A/CA-1.1. Verification -> PASS/FAIL

**CA-1.2:** Registry anchor — TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?]. Preamble anchor — C-02: TABLE_2/SE-2/SHALL-B/CA-1.2. Verification -> PASS/FAIL

**CA-1.3:** Registry anchor — TABLE_3: [Role, OWD Baseline, Scope Modifier, Effective Scope, Verified?]. Preamble anchor — C-03: TABLE_3/SE-1+SE-3/SHALL-C/CA-1.3. Verification -> PASS/FAIL

**CA-1.4:** Registry anchor — TABLE_4: [Vector, Checked?, Finding, Severity]. Preamble anchor — C-04: TABLE_4/SE-4/SHALL-D/CA-1.4. Verification -> PASS/FAIL

**CA-1.5:** Registry anchor — TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Severity, Remediation]. Preamble anchor — C-05: TABLE_5/SE-5/SHALL-E/CA-1.5.

> RULE (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" — TABLE_5 Remediation three-field schema was declared by CA in Phase 0 Step 0.1, before PHASE 1 (SE). This CA-1.5 row confirms the format established at that declaration site was applied throughout.

Verification -> PASS/FAIL

**CA Format Compliance Verdict — citing Phase 0:**
Citing Schema Registry (Step 0.1), preamble (Step 0.2), Phase 0 gate — all authored by CA before PHASE 1 began. SE-first variant: SE produced TABLE_1-5 in PHASE 1; CS reconciled in PHASE 2; structural requirements unchanged.

> RULE (C-23): "execution record, not declarative checklist" — Phase 0 gate recorded confirmed activation of all chains before evidence collection. This verdict confirms execution matched the record.

> RULE (C-24): "precondition for closing the trace, not a recommended step" — this verdict is that precondition.

[C-01 through C-05 disposition. Overall: COMPLIANT / NON-COMPLIANT.]

[TRACE CLOSED — CA-1 verdict written.]

---

## V-05 — Full Combination: C-26 + C-27 + C-28 (Maximum Coverage)

**Axis:** All three — V-01 Phase 0 inline verbatim + V-02 downstream RULE blocks + V-03 extended INDEX with completeness threshold; CS-first role sequence; Phase 0 close includes N/N coverage count
**Hypothesis:** +5 (C-26) + 5 (C-27) + 5 (C-28) = 15 pts; achieves 195/195. The INDEX lists all enforcement points; inline verbatim appears at every declaration site; RULE blocks appear at every application site; Phase 0 close writes a confirmed N/N count.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: Why a Permissions Trace Is Not Optional

Three inertia patterns defeat manual security audits:

**Blind spot 1 — Post-incident FLS discovery.** FLS gaps emerge after breaches. This trace replaces reactive discovery with pre-incident, categorized enumeration across PII, Financial, Audit-Compliance, and Operational fields.

**Blind spot 2 — Cumulative privilege accumulation.** No single Dataverse UI view surfaces the combined effect of security role depth, team membership, OWD, and sharing rules. This trace computes effective scope from all four layers together.

**Blind spot 3 — OWD-sharing-rule override.** A Private OWD does not prevent a sharing rule configured independently from re-opening access. This trace cross-references OWD settings against every active sharing rule to surface unintended grants.

Each SE section opens with a CONTEXT-CLOSES label naming the blind spot it resolves.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. CS-first sequence. Labels appear as section headers. Each phase completes fully before the next begins.

**PHASE 0 — CA:** Schema Registry (Step 0.1), Criterion Enforcement Matrix preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3), Phase 0 gate and coverage count statement.

**PHASE 1 — CS:** Qualitative access baseline and expectation tables. Does NOT fill TABLE_1-5.

**PHASE 2 — SE:** Fills TABLE_1-5. Dataverse-native terminology throughout. References CS tables by Schema ID.

**PHASE 3 — CA-1:** Double-anchor verification per criterion. Terminal verdict cites Phase 0 by label. Trace is not closed until this verdict is written.

---

## PHASE 0 — CA: SCHEMA REGISTRY, ENFORCEMENT PREAMBLE, AND LANGUAGE INDEX

### Step 0.1 — Schema Registry (CA-authored)

**All schemas declared by CA before PHASE 1. Blank-cell prohibition global.**

**Schema ID: TABLE_1 — Role-Operation Matrix**
Declared columns: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Blank-cell rule: Granted / Denied / Conditional (state condition inline) / N/A.

**Schema ID: TABLE_2 — FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Gap? = YES / NO. Gap? = YES rows forward to TABLE_5 immediately (per-row, before next row).

The Gap? boolean converts register triggering from a judgment call to a mechanical confirmation: the model marks YES/NO while filling the table, and each Gap? = YES is the per-row commit signal for an immediate TABLE_5 entry.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" — the Gap? column above is that flag. Its structural role as the per-row commit signal is confirmed here, at the Schema Registry TABLE_2 declaration site, before PHASE 1 begins. Downstream RULE (C-22) appears at SE-2.

**Schema ID: TABLE_3 — Record Scope by Role**
Declared columns: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].

**Schema ID: TABLE_4 — Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
All four vectors required: team inheritance / sharing rules / impersonation / admin or environment role override. Checked? = YES for all. Finding = escalation path (`[Role] -> [Action] -> [Elevated access achieved]`) or per-role rule-out ("Checked [mechanism]: no path because [specific reason]").

**Schema ID: TABLE_5 — Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Enumerated gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.
Remediation three-field format (all three sub-fields required for every row):
  (1) Config change: exact configuration object, its location in the Dataverse security editor, and the specific change to apply.
  (2) Expected state: the specific UI view, profile row, or query result that will differ after the fix — naming what a reviewer will see.
  (3) Verification step: the named action a reviewer executes to confirm the fix took effect — e.g., "Open Security > Column Security Profiles > [profile] > [entity] > [field]: verify [role] shows Read-only."

> PLACEMENT-CRITERION CONFIRMED (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" — the TABLE_5 Remediation three-field format (config change / expected state / verification step) is that declaration. Confirmed here, at the Schema Registry TABLE_5 entry, before PHASE 1 begins. Pre-declaration ensures SE collects verification-relevant details during the evidence window — e.g., "open FLS profile in security editor" is obvious while SE is examining the profile; it must be reconstructed if the format is deferred. Downstream RULE (C-16) appears at CA-1.5.

**Schema ID: CS-2 — Sharing Rule Expectations (CS-authored)**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference`
SE Cross-Reference: CS fills as "TBD — await SE"; SE updates with TABLE_4 or TABLE_5 row reference.

**Schema ID: CS-3 — Cross-Role Differential Expectations (CS-authored)**
Declared columns: `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation`
SE Confirmation: CS fills as "TBD — await SE"; SE updates with TABLE_1 or TABLE_3 reference and CONFIRMED or CS-EXPECTATION-VIOLATED.

### Step 0.2 — Criterion Enforcement Matrix Preamble (CA-authored)

M1, M2, M3 simultaneously active for every essential criterion — not alternative paths. M4 pre-assigned by CA. Essential criteria C-01–C-05 assigned to SE because they require formal table production.

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

The Gap? boolean in TABLE_2 is the per-row structural commit signal established by the Schema Registry. FLS co-authorship operates as follows: mark Gap? = YES/NO while filling each TABLE_2 row; if YES, the TABLE_5 entry is made before the next TABLE_2 row begins. This makes co-authorship a structural property of the output format.

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" — this preamble declaration establishes the Gap? boolean as the structural enforcement mechanism. Confirmed here at the Criterion Enforcement Matrix preamble declaration site, before PHASE 1. The absence of any Gap? = YES TABLE_2 row without a corresponding TABLE_5 entry is the proof. Downstream RULE (C-22) appears at SE-2.

**SHALL obligations (CA-authored):**
- SHALL-A: TABLE_1 present with every cell Granted/Denied/Conditional/N/A; every role with any privilege included.
- SHALL-B: TABLE_2 lists every sensitive field with FLS status; null case stated if no profiles active; Not Configured fields in TABLE_5; Gap? = YES rows forwarded per-row.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Effective Scope filled; ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 checks all four escalation vectors; per-role rule-out naming specific mechanism and reason when no escalation found.
- SHALL-E: TABLE_5 contains at least one named gap; zero-gap case requires explicit evidence rows naming what was checked and confirmed safe.

### Step 0.3 — ENFORCEMENT LANGUAGE INDEX (CA-authored)

**COMPLETENESS THRESHOLD: coverage of N-1 of N enforcement points earns 0 pts — the same as 0 of N. The index enables gap detection; it does not close gaps. A trace that passes C-28 satisfies all three requirements: (a) this index lists every enforcement point, (b) every declaration-site enforcement point has inline verbatim confirmed, (c) every application-site enforcement point has a RULE block confirmed.**

| EL-ID | Criterion | Enforcement Point | Verbatim Pass-Condition Phrase | Site Type | Status |
|-------|-----------|-------------------|-------------------------------|-----------|--------|
| EL-01 | C-11 | Phase 0 gate Chain 1 declaration | "entered into the findings log at that point in the output — not deferred to a summary section compiled after the fact" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate statement |
| EL-02 | C-12 | SE-2/SE-4 negative-check instruction | "Checked [list] for [role]; [gap type] does not apply because [reason]" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-2 and SE-4 |
| EL-03 | C-13 | TABLE_5 Remediation field definition | "expected system state after the fix is applied and how to verify the fix took effect" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_5 entry |
| EL-04 | C-14 | TABLE_5 instruction / SE-5 note | "enables auditing that C-11 inline registration actually occurred" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-5 |
| EL-05 | C-15 | SE-4 per-role rule-out instruction | "one explicit rule-out per traced role — naming the specific actions checked for that role and why none permit elevation" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-4 |
| EL-06 | C-16 | TABLE_5 Remediation schema declaration | "declared explicitly at the top of the trace output, before the first analysis phase begins" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_5 entry |
| EL-07 | C-17 | CA-1.5 remediation echo instruction | "remediation block that states the fix without linking back to the discovery section does not pass" | APPLICATION-SITE | RULE-BLOCK: confirmed at CA-1.5 |
| EL-08 | C-18/C-22 | TABLE_2 Gap? column and Criterion Enforcement Matrix | "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" / "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" | DECLARATION-SITE (both) | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_2 and Step 0.2 preamble |
| EL-09 | C-23 | Phase 0 gate statement header | "execution record, not declarative checklist" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate statement |
| EL-10 | C-24 | CA-1 verdict precondition | "precondition for closing the trace, not a recommended step" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate and CA-1 verdict header |
| EL-11 | C-25 | All structural enforcement points | each criterion's exact pass-condition phrase at each structural enforcement point | BOTH (per-criterion) | CONFIRMED: inline verbatim at declaration sites (EL-01/03/06/08/09/10), RULE blocks at application sites (EL-02/04/05/07) |

**Phase 0 coverage count:** 11/11 enforcement points (EL-01 through EL-11) declared in this index. Declaration-site coverage: EL-01, EL-03, EL-06, EL-08, EL-09, EL-10 — inline verbatim confirmed above. Application-site coverage: EL-02, EL-04, EL-05, EL-07 — RULE blocks confirmed at SE-2, SE-4, SE-5, CA-1.5. EL-11 (C-25) confirmed by full-index + per-enforcement-point coverage. 11/11. C-28 coverage precondition satisfied at Phase 0. **[If any EL row shows UNCONFIRMED at Phase 0 close, this trace cannot satisfy C-28.]**

### Phase 0 Gate Statement

This trace operates under a bidirectional audit structure. All directions pre-established here.

Chain 1 — discovery to TABLE_5: every gap found during PHASE 2 is entered into TABLE_5 at the section where it is found — entered into the findings log at that point in the output — not deferred to a summary section compiled after the fact. Chain 2 — TABLE_5 to CA-1 verification: every TABLE_5 Remediation entry verified in PHASE 3 via double-anchor citing Registry schema and preamble row.

> PLACEMENT-CRITERION CONFIRMED (C-11 / C-23): "entered into the findings log at that point in the output — not deferred to a summary section compiled after the fact" (C-11) and "execution record, not declarative checklist" (C-23) — this gate statement is that execution record. Chain 1 active means gaps are registered at their discovery site; Chain 2 active means CA-1 echoes TABLE_5 entries. Both confirmed active as of Phase 0 close. Downstream RULE (C-23) appears at CA-1 verdict.

The CA-1 verdict in PHASE 3 is the structural close condition for this trace — a precondition for closing the trace, not a recommended step. Downstream RULE (C-24) appears at CA-1 verdict close.

**Phase 0 gate state log (execution record, not declarative checklist):**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Chain 1 — discovery to TABLE_5, inline at discovery site | ACTIVE | Inline verbatim at Phase 0 gate (EL-01) |
| TABLE_5 Remediation three-field format | ACTIVE | Inline verbatim at Step 0.1 TABLE_5 (EL-06) |
| Gap? per-row boolean trigger | ACTIVE | Inline verbatim at Step 0.1 TABLE_2 + Step 0.2 preamble (EL-08) |
| Chain 2 — TABLE_5 to CA-1 double-anchor | ACTIVE | RULE blocks at CA-1.5 (EL-07) |
| ENFORCEMENT LANGUAGE INDEX 11/11 | CONFIRMED | Step 0.3 coverage count |
| CA-1 verdict as trace close precondition | ACTIVE | Inline verbatim at CA-1 verdict header (EL-10) |

*All 11/11 enforcement points confirmed. All structures active. Handing to PHASE 1 — CS.*

---

## PHASE 1 — CS: Lower-Trust Access Baseline

*CS produces CS-1 narrative and CS-2/CS-3 expectation tables using Schema Registry schemas. CS does not fill TABLE_1-5.*

**CS-1 — Expected Customer Service access baseline:**
For each entity in scope: (a) CRUD operations CS role performs as part of normal job function; (b) expected record scope (own records, BU-wide, org-wide, team-scoped); (c) sensitive fields CS is expected to need read or write access to and why. Name any active sharing rules CS relies on for record access.

**CS-2 — Sharing rule expectations** (Schema Registry CS-2 schema):

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference |
|-----------|---------|------------------------|-----------------------|---------------------|--------------------|
| | | | | | TBD — await SE Phase 2 |

For each Potential Overreach? = YES: name the access path and why it may exceed CS job function.

**CS-3 — Cross-role differential expectations** (Schema Registry CS-3 schema):

| Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation |
|--------|-------------------|-------------------|--------------------------------|---------------|-----------------|
| | | | | | TBD — await SE Phase 2 |

Name the privileged role. Identify at least one field/operation where CS should have less access. Flag any sharing rule that might close that gap unexpectedly.

*Handing to PHASE 2 — SE.*

---

## PHASE 2 — SE: Security Analysis

*SE fills TABLE_1-5. Dataverse-native terminology throughout. SE updates CS-2 SE Cross-Reference and CS-3 SE Confirmation. CS-EXPECTATION-VIOLATED rows in TABLE_5 follow three-field Remediation.*

### SE-1 / SHALL-A — Role-Operation Matrix

**CONTEXT-CLOSES: cumulative privilege accumulation — TABLE_1 maps every role's operations and record scope in one view, including the combined effect of security role depth, team membership, and OWD that no single Dataverse UI surfaces.**

**TABLE_1** (Schema Registry TABLE_1 schema; blank-cell rule applies)

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Every role with any privilege on any entity in {{topic}}. Record Scope: Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name]. After table, update CS-3 SE Confirmation for CS row: cite TABLE_1 row, state CONFIRMED or CS-EXPECTATION-VIOLATED.

### SE-2 / SHALL-B — Field-Level Security Coverage

**CONTEXT-CLOSES: post-incident FLS discovery — explicit FLS status per sensitive field, checked before incidents occur.**

> RULE (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" — each TABLE_2 Gap? cell is the per-row commit signal established in Phase 0. Mark YES/NO while filling each row. If Gap? = YES, make the TABLE_5 entry before beginning the next TABLE_2 row. The absence of any Gap? = YES TABLE_2 row without a corresponding TABLE_5 entry is the structural proof of trigger completeness.

**TABLE_2** (Schema Registry TABLE_2 schema; Gap? per-row trigger ACTIVE per Phase 0 preamble and this RULE)

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Sensitive categories: PII / Financial / Audit-Compliance / Operational. Check Security > Column Security Profiles for all entities. Null case: "No column security profiles active. Sensitive fields identified: [list]. All entered in TABLE_5."

> RULE (C-12): "Checked [list] for [role]; [gap type] does not apply because [reason]" — for each sensitive field category that yields no Gap? = YES entry, state explicitly what was examined and why no gap applies using this format.

Cross-reference CS-1 sensitive field expectations. Update CS-3 SE Confirmation for any field where SE finding contradicts CS-1.

### SE-3 / SHALL-C — Record Access Scope

**CONTEXT-CLOSES: OWD-sharing-rule override — effective scope mapped per role including team membership and sharing rule overlays.**

**TABLE_3** (Schema Registry TABLE_3 schema; blank-cell rule applies)

| Role | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role present. OWD: Private / Business Unit / Parent-Child BU / Organization. Scope Modifier: security role privilege depth + team membership (owner or access team) + sharing rule override.

**Defense-in-depth layer assessment:** For at least one operation, name the specific enforcement layer (1: environment/admin, 2: security role + BU, 3: team membership, 4: column security profiles) where access is granted or denied, and state why higher layers do not override.

Update CS-3 SE Confirmation for scope rows.

### SE-4 / SHALL-D — Privilege Escalation Analysis

**TABLE_4** (Schema Registry TABLE_4 schema; all four vectors; Checked? = YES for all)

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

> RULE (C-15): "one explicit rule-out per traced role — naming the specific actions checked for that role and why none permit elevation" — when no escalation path is found for a role, provide one rule-out per traced role with specific mechanism and reason. A blanket statement covering all roles does not pass.

Update CS-2 SE Cross-Reference for each sharing rule row.

Cross-entity permission chain: if any TABLE_5 gap involves a multi-entity lookup, trace the permission at each entity hop (at least two hops).

### SE-5 / SHALL-E — Security Gap Inventory

**TABLE_5** (Schema Registry TABLE_5 schema; Remediation three-field format declared in Phase 0 Step 0.1)

| # | Gap Type | Entity | Field or Rule | Role | Severity | Remediation |
|---|----------|--------|---------------|------|----------|-------------|

> RULE (C-14): "enables auditing that C-11 inline registration actually occurred" — each TABLE_5 row must include the discovery context in the Entity or Gap Type field: the gap was entered at the section where it was found (Chain 1). A TABLE_5 compiled post-hoc without discovery-section traceability does not pass.

CS-EXPECTATION-VIOLATED rows: (1) CS expectation — cite Schema ID CS-2 or CS-3 and row number; (2) SE finding contradicting it; (3) configuration change with expected state and verification step.

*Handing to PHASE 3 — CA-1.*

---

## PHASE 3 — CA-1: Double-Anchor Format Compliance Verification

*CA returns. Each CA-1 row: Registry anchor and Preamble anchor as structurally distinct, independently readable labeled lines before Verification. Inline concatenation fails.*

*This phase is the structural close condition for the trace — a precondition for closing the trace, not a recommended step. The trace is not closed until the CA-1 verdict is written.*

**CA-1.1 — C-01 verification (completing Phase 0 M4 pre-assignment CA-1.1):**
Registry anchor — Schema ID TABLE_1: [Role, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope] — blank cells prohibited.
Preamble anchor — C-01 as authored by CA in Phase 0: TABLE_1 / SE-1 / SHALL-A / CA-1.1 — verifying...
Verification — TABLE_1 present? All cells Granted/Denied/Conditional/N/A? All roles with any privilege included? -> PASS / FAIL

**CA-1.2 — C-02 verification (completing Phase 0 M4 pre-assignment CA-1.2):**
Registry anchor — Schema ID TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?] — blank cells prohibited.
Preamble anchor — C-02 as authored by CA in Phase 0: TABLE_2 / SE-2 / SHALL-B / CA-1.2 — verifying...
Verification — TABLE_2 present? Sensitive fields with FLS status? Null case stated? Gap? = YES rows in TABLE_5? Per-row co-authorship preserved (no Gap? = YES TABLE_2 row without TABLE_5 entry)? -> PASS / FAIL

**CA-1.3 — C-03 verification (completing Phase 0 M4 pre-assignment CA-1.3):**
Registry anchor — Schema ID TABLE_3: [Role, OWD Baseline, Scope Modifier, Effective Scope, Verified?] — blank cells prohibited.
Preamble anchor — C-03 as authored by CA in Phase 0: TABLE_3 / SE-1+SE-3 / SHALL-C / CA-1.3 — verifying...
Verification — Every TABLE_1 role in TABLE_3? Effective Scope filled for all? Ambiguous scope in TABLE_5? -> PASS / FAIL

**CA-1.4 — C-04 verification (completing Phase 0 M4 pre-assignment CA-1.4):**
Registry anchor — Schema ID TABLE_4: [Vector, Checked?, Finding, Severity] — all four vectors, Checked? = YES.
Preamble anchor — C-04 as authored by CA in Phase 0: TABLE_4 / SE-4 / SHALL-D / CA-1.4 — verifying...
Verification — TABLE_4 present? All four vectors? Checked? = YES? Each finding with escalation path or per-role rule-out with specific reason? -> PASS / FAIL

**CA-1.5 — C-05 verification (completing Phase 0 M4 pre-assignment CA-1.5):**
Registry anchor — Schema ID TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Severity, Remediation] — blank cells prohibited.
Preamble anchor — C-05 as authored by CA in Phase 0: TABLE_5 / SE-5 / SHALL-E / CA-1.5 — verifying...

> RULE (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" — TABLE_5 Remediation three-field schema (config change / expected state / verification step) was declared by CA in Phase 0 Step 0.1, before PHASE 1 began. This CA-1.5 row confirms TABLE_5 rows follow that format throughout.

> RULE (C-17): "remediation block that states the fix without linking back to the discovery section does not pass" — each TABLE_5 Remediation entry must chain back to its discovery context; a CA-1.5 PASS requires that linkage to be present.

Verification — TABLE_5 present? Named gap with specific field/role/rule? Remediations contain all three sub-fields (config change / expected state / verification step)? CS-EXPECTATION-VIOLATED rows structured correctly? -> PASS / FAIL

**CA Format Compliance Verdict — citing Phase 0:**
Citing: CA-authored Schema Registry (Step 0.1), CA-authored preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3), Phase 0 gate state log — all authored by CA before PHASE 1 began.

> RULE (C-23): "execution record, not declarative checklist" — Phase 0 gate recorded confirmed activation of Chain 1, Chain 2, Gap? trigger, and all structural enforcement points. This verdict confirms those mechanisms executed as recorded.

[C-01 through C-05 PASS / FAIL disposition. Overall: COMPLIANT / NON-COMPLIANT. Open items with responsible role.]

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION (C-28):**
Reviewing Step 0.3 against this output: [for each EL-01 through EL-11, confirm the STATUS field is CONFIRMED or flag UNCONFIRMED]. Coverage count: N/11. If N < 11: C-28 = FAIL regardless of how many are confirmed.

> RULE (C-24): "precondition for closing the trace, not a recommended step" — writing this verdict is that precondition. The trace is now closed.

[TRACE CLOSED — CA-1 verdict written; 11/11 INDEX points confirmed; structural precondition satisfied.]
