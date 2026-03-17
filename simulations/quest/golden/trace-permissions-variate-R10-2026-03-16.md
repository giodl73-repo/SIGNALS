# trace-permissions Variate -- Round 10 (rubric v8 -- C-26/C-27/C-28 target)
**Date:** 2026-03-16
**Rubric:** v8 (C-01 through C-28 -- C-26/C-27/C-28 added from Round 9 excellence signals)
**Target criteria:** C-26 (effect-anchored prohibition scope), C-27 (global obligation register), C-28 (sequence-direction-agnostic phase opening)

**State entering Round 10:**

| Variation | Prior score (R9 V-04 best, rubric v7/25 aspirational) | Gap under v8 (28 aspirational) |
|-----------|------------------------------------------------------|-------------------------------|
| Best prior (R9 V-04) | 118.75 / 132.5 | C-26 absent (-2.5), C-27 absent (-2.5), C-28 absent (-2.5); C-13 FAIL (-2.5), C-20 FAIL (-2.5), C-23 FAIL (-2.5), C-25 FAIL (-2.5) |

Round 10 holds the R9 V-04 structural core (C-31 verbatim cross-audit present, C-32 intent-anchored equivalence present, formal/technical register, CS-first canonical sequence, CA -> CS -> SE -> CA-1, Schema Registry, ENFORCEMENT LANGUAGE INDEX with Site Type column, bidirectional chains) and adds C-26/C-27/C-28 mechanisms across three single-axis tests and two combined variations.

Baseline INDEX entry count from R9 V-04: EL-01 through EL-13 (13 enforcement points). Round 10 adds EL-14 (C-26 effect-anchored prohibition), EL-15 (C-27 global obligation register), EL-16 (C-28 phase opening acknowledgment) to reach 14, 15, or 16 enforcement points depending on variation.

---

## Round 10 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format -- C-26 isolation: all restriction and prohibition clauses rewritten with mechanism-of-effect anchoring; C-27 advisory register unchanged from R9 base; C-28 absent (no CS-0 explicit section) | C-26 requires at least one prohibition clause anchored to "achieves the effect of X" rather than naming surface forms. V-01 rewrites every prohibition clause in the prompt -- Mechanisms Cited, equivalence clauses, routing rules -- to anchor to mechanism of effect rather than form. Hypothesis: +weight(C-26); C-27 PARTIAL (register not globally upgraded); C-28 FAIL (CS-0 section absent). |
| V-02 | Phrasing register -- C-27 isolation: all analytically required instructions upgraded to SHALL/MUST/REQUIRED/PROHIBITED throughout; C-26 absent (prohibition clauses retain form-based language); C-28 absent | C-27 requires 80%+ of structurally required operation instructions to use obligation language. V-02 upgrades every SE-X instruction governing required operations. Hypothesis: +weight(C-27); C-26 FAIL (prohibition clauses form-anchored); C-28 FAIL (no CS-0 section). |
| V-03 | Role sequence -- C-28 isolation: SE-first sequence with explicit SE-0 acknowledgment section declaring Phase 0 inputs by labeled artifact name before first analytical schema is filled; C-26 absent; C-27 advisory base | C-28 requires the first analytical phase to contain a named opening acknowledgment section referencing Phase 0 artifacts by their exact exit gate labels. V-03 uses SE-first and adds SE-0 mirroring CS-0's structure. Hypothesis: +weight(C-28); C-21 PASS (SE-0 closes Phase 1 input boundary); C-26 FAIL; C-27 PARTIAL. |
| V-04 | Combined C-26 + C-27 + C-28, CS-first, formal/technical register throughout | V-01 proves C-26; V-02 proves C-27; V-03 proves C-28. V-04 combines all three under formal register with CS-first canonical sequence. Hypothesis: +weight(C-26) + weight(C-27) + weight(C-28); achieves 28/28 aspirational for the three new criteria. |
| V-05 | Full combination C-26 + C-27 + C-28 + C-13 + C-20 + C-23 + C-25; CS-first; verdict carry-forward; layer-override column; terminal chain audit; count echo propagation | Maximum coverage. Adds four persistent fails: C-13 (CLEARED/NOT CLEARED carry-forward across consecutive phases), C-20 (Why Not Overridden column in defense-in-depth table), C-23 (linear chain trace at terminal phase), C-25 (count echo propagation at intermediate phases). Hypothesis: +weight for all seven criteria; approaches ceiling score. |

---

## V-01 -- Single-Axis: Effect-Anchored Prohibition Scope (C-26 target)

**Axis:** Output format -- all restriction/prohibition clauses anchor to mechanism of effect; C-27 register unchanged from R9 base; C-28 absent
**Hypothesis:** +weight(C-26). Prohibition clauses that restrict back-reference, delegation, and scope-reuse patterns use "achieves the effect of X regardless of structural form" language rather than enumerating disallowed forms. C-27 PARTIAL (register not globally upgraded -- only the MUST-level CS-3 update instruction from R9 V-04 is present). C-28 FAIL (no explicit CS-0 acknowledgment section at Phase 1 opening).

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: Why a Permissions Trace Is Not Optional

Three inertia patterns defeat manual security audits:

**Blind spot 1 -- Post-incident FLS discovery.** FLS gaps emerge after breaches. This trace replaces reactive discovery with pre-incident, categorized enumeration across PII, Financial, Audit-Compliance, and Operational fields.

**Blind spot 2 -- Cumulative privilege accumulation.** No single Dataverse UI view surfaces the combined effect of security role depth, team membership, OWD, and sharing rules. This trace computes effective scope from all four layers together.

**Blind spot 3 -- OWD-sharing-rule override.** A Private OWD does not prevent a sharing rule configured independently from re-opening access. This trace cross-references OWD settings against every active sharing rule to surface unintended grants.

Each SE section opens with a CONTEXT-CLOSES label naming the blind spot it resolves.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. CS-first sequence. Labels appear as section headers. Each phase completes fully before the next begins.

**PHASE 0 -- CA:** Schema Registry (Step 0.1), Criterion Enforcement Matrix preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3), Phase 0 gate statement. CA is sole author.

**PHASE 1 -- CS:** Qualitative access baseline and expectation tables. Does NOT fill TABLE_1-5.

**PHASE 2 -- SE:** Fills TABLE_1-5. Dataverse-native terminology. References CS tables by Schema ID.

**PHASE 3 -- CA-1:** Double-anchor verification per criterion. Terminal verdict cites Phase 0 by label. Trace not closed until this verdict is written.

---

## PHASE 0 -- CA: SCHEMA REGISTRY, ENFORCEMENT PREAMBLE, AND LANGUAGE INDEX

### Step 0.1 -- Schema Registry (CA-authored)

**All schemas declared by CA before PHASE 1. Blank-cell prohibition global.**

**Schema ID: TABLE_1 -- Role-Operation Matrix**
Declared columns: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Blank-cell rule: Granted / Denied / Conditional (state condition inline) / N/A.

**Schema ID: TABLE_2 -- FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Gap? = YES / NO. Gap? = YES rows forward to TABLE_5 immediately (per-row, before next row begins). The Gap? boolean converts register triggering from a judgment call to a mechanical confirmation: marks YES/NO while filling the table; each Gap? = YES is the per-row commit signal for an immediate TABLE_5 entry.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" -- the Gap? column above is that flag. Structural role as per-row commit signal confirmed here, at the Schema Registry TABLE_2 declaration site, before PHASE 1 begins. Downstream RULE (C-22) appears at SE-2.

**Schema ID: TABLE_3 -- Record Scope by Role**
Declared columns: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].

**Schema ID: TABLE_4 -- Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
All four vectors: team inheritance / sharing rules / impersonation / admin or environment role override. Checked? = YES for all. Finding = escalation path or per-role rule-out with specific mechanism and reason.

Per-role escalation roll-up sub-table (authored in SE-4):
`Role | Pre-Declaration Commitment | Composite Verdict | Mechanisms Cited | Cross-Audit`

Mechanisms Cited field: PROHIBITED is any content that achieves the effect of routing the reader to another section to obtain mechanism content -- regardless of whether the form that produces that effect is a named back-reference, an implied reference, a parenthetical, a label pointing elsewhere, or any novel structural form not yet encountered. The test is not whether the disallowed forms are present but whether the content achieves the effect of delegation. Only inline enumeration of each mechanism by type satisfies this field.

> PLACEMENT-CRITERION CONFIRMED (C-26 / C-27): "PROHIBITED is any content that achieves the effect of routing the reader to another section" -- this prohibition anchors to mechanism of effect rather than to named surface forms. Any form that achieves the delegation effect is prohibited, regardless of its structural appearance. This is an effect-anchored restriction clause satisfying C-26. The prohibition instruction uses PROHIBITED (obligation-level) for the restriction. Confirmed here at Schema Registry TABLE_4 declaration site, before PHASE 1. Downstream RULE (C-26 / C-27) appears at SE-4.

Cross-Audit field: verbatim-quote format required.
`Pre-decl: "[exact text copied verbatim from Pre-Declaration Commitment cell]" | Filed: "[exact text copied verbatim from Mechanisms Cited cell]" | Match: CONFIRMED`
This format quotes both sites exactly, making match verification a zero-judgment mechanical operation. A characterization-based cross-audit does not satisfy this requirement.

> PLACEMENT-CRITERION CONFIRMED (C-24): verbatim-quote format declared here at Schema Registry TABLE_4 Cross-Audit field declaration site, before PHASE 1. Downstream RULE-BLOCK at SE-4.

**Schema ID: TABLE_5 -- Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Enumerated gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.
Remediation three-field format (all three required): (1) Config change: exact object, location in Dataverse security editor, change to apply. (2) Expected state: specific UI view or result after fix. (3) Verification step: named action to confirm fix took effect.

> PLACEMENT-CRITERION CONFIRMED (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 Remediation three-field format is that declaration. Confirmed here at Step 0.1, before PHASE 1. Downstream RULE (C-16) appears at CA-1.5.

**Schema ID: CS-2**: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference` -- SE Cross-Reference: "TBD -- await SE."
**Schema ID: CS-3**: `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation` -- SE Confirmation: "TBD -- await SE."

### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored)

M1, M2, M3 simultaneously active for every essential criterion -- not alternative paths. M4 pre-assigned by CA.

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

The Gap? boolean in TABLE_2 is the per-row structural commit signal. FLS co-authorship: mark Gap? = YES/NO per row; if YES, make the TABLE_5 entry before the next TABLE_2 row begins.

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- confirmed here at the preamble declaration site, before PHASE 1. Downstream RULE (C-22) appears at SE-2.

**SHALL obligations (CA-authored):**
- SHALL-A: TABLE_1 present; every cell Granted/Denied/Conditional/N/A; every role with any privilege included.
- SHALL-B: TABLE_2 lists every sensitive field; null case stated; Gap? = YES rows forwarded per-row.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Effective Scope filled; ambiguous scope flagged in TABLE_5.
- SHALL-D: TABLE_4 all four vectors; per-role rule-out naming specific mechanism and reason; per-role roll-up with Pre-Declaration Commitment, Composite Verdict, Mechanisms Cited (inline only -- any form that achieves delegation effect is PROHIBITED), Cross-Audit (verbatim format per Step 0.1).
- SHALL-E: TABLE_5 at least one named gap; zero-gap case requires explicit evidence rows.

### Step 0.3 -- ENFORCEMENT LANGUAGE INDEX (CA-authored)

**COMPLETENESS THRESHOLD: N-1 of N enforcement points earns 0 pts -- the same as 0 of N.**

> PLACEMENT-CRITERION CONFIRMED (C-25): Site Type column present per-row. DECLARATION-SITE rows require inline verbatim confirmation; APPLICATION-SITE rows require RULE-BLOCK confirmation.

| EL-ID | Criterion | Enforcement Point | Verbatim Pass-Condition Phrase | Site Type | Status |
|-------|-----------|-------------------|-------------------------------|-----------|--------|
| EL-01 | C-11 | Phase 0 gate Chain 1 declaration | "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate statement |
| EL-02 | C-12 | SE-2/SE-4 negative-check instruction | "Checked [list] for [role]; [gap type] does not apply because [reason]" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-2 and SE-4 |
| EL-03 | C-13 | TABLE_5 Remediation field definition | "expected system state after the fix is applied and how to verify the fix took effect" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_5 |
| EL-04 | C-14 | SE-5 discovery-section note | "enables auditing that C-11 inline registration actually occurred" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-5 |
| EL-05 | C-15 | SE-4 per-role rule-out instruction | "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-4 |
| EL-06 | C-16 | TABLE_5 Remediation schema declaration | "declared explicitly at the top of the trace output, before the first analysis phase begins" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_5 |
| EL-07 | C-17 | CA-1.5 remediation echo instruction | "remediation block that states the fix without linking back to the discovery section does not pass" | APPLICATION-SITE | RULE-BLOCK: confirmed at CA-1.5 |
| EL-08 | C-18/C-22 | TABLE_2 Gap? column and Criterion Enforcement Matrix | "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" / "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" | DECLARATION-SITE (both) | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_2 and Step 0.2 preamble |
| EL-09 | C-23 | Phase 0 gate statement | "execution record, not declarative checklist" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate statement |
| EL-10 | C-24 | CA-1 verdict precondition | "precondition for closing the trace, not a recommended step" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate and CA-1 verdict header |
| EL-11 | C-25 | All structural enforcement points | each criterion's exact pass-condition phrase at each structural enforcement point | BOTH (per-criterion) | CONFIRMED: inline verbatim at declaration sites (EL-01/03/06/08/09/10), RULE blocks at application sites (EL-02/04/05/07) |
| EL-12 | C-24 | TABLE_4 Cross-Audit field definition + SE-4 roll-up instruction | "Pre-decl: '[exact text]' | Filed: '[exact text]' | Match: CONFIRMED" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-4; PLACEMENT annotation at Step 0.1 TABLE_4 Cross-Audit field |
| EL-13 | C-32 / intent-anchored equivalence | TABLE_4 Mechanisms Cited prohibition + SE-4 instruction | equivalent form that achieves delegation effect | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_4 Mechanisms Cited prohibition |
| EL-14 | C-26 | TABLE_4 Mechanisms Cited prohibition -- effect-anchored restriction clause | "PROHIBITED is any content that achieves the effect of routing the reader to another section to obtain mechanism content -- regardless of structural form" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_4; effect-anchored (not form-enumerated) restriction clause present |

**Phase 0 coverage note:** 14/14 enforcement points declared. Site Type breakdown: 7 DECLARATION-SITE (EL-01/03/06/08/09/10/13/14), 5 APPLICATION-SITE (EL-02/04/05/07/12), 1 BOTH (EL-11). C-26 effect-anchored prohibition annotation present at Step 0.1 TABLE_4. C-27 NOT globally enforced -- register not upgraded to SHALL/MUST throughout. C-28 absent -- no explicit CS-0 opening acknowledgment section.

### Phase 0 Gate Statement

Chain 1 -- discovery to TABLE_5: every gap found during PHASE 2 is entered into TABLE_5 at the section where it is found -- entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact.
Chain 2 -- TABLE_5 to CA-1: every TABLE_5 Remediation entry verified in PHASE 3 via double-anchor citing Registry schema and preamble row.

> PLACEMENT-CRITERION CONFIRMED (C-11 / C-23): "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" (C-11) and "execution record, not declarative checklist" (C-23) -- this gate statement is that execution record. Chain 1 active. Chain 2 active. Downstream RULE (C-23) appears at CA-1 verdict.

The CA-1 verdict in PHASE 3 is the structural close condition -- a precondition for closing the trace, not a recommended step. Downstream RULE (C-24) at CA-1 verdict close.

**Phase 0 gate state log (execution record, not declarative checklist):**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Chain 1 -- discovery to TABLE_5, inline at discovery site | ACTIVE | Inline verbatim at Phase 0 gate (EL-01) |
| TABLE_5 Remediation three-field format | ACTIVE | Inline verbatim at Step 0.1 TABLE_5 (EL-06) |
| Gap? per-row boolean trigger | ACTIVE | Inline verbatim at Step 0.1 TABLE_2 + Step 0.2 preamble (EL-08) |
| Chain 2 -- TABLE_5 to CA-1 double-anchor | ACTIVE | RULE blocks at CA-1.5 (EL-07) |
| ENFORCEMENT LANGUAGE INDEX 14/14 | CONFIRMED | EL-14 effect-anchored prohibition (C-26) confirmed at Step 0.1 TABLE_4; EL-12 verbatim cross-audit confirmed at Step 0.1 TABLE_4 Cross-Audit field; EL-13 intent-anchored equivalence confirmed at Step 0.1 TABLE_4 |
| CA-1 verdict as trace close precondition | ACTIVE | Inline verbatim at CA-1 verdict header (EL-10) |

*All 14/14 enforcement points confirmed. All structures active. Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Lower-Trust Access Baseline

*CS produces CS-1 narrative and CS-2/CS-3 expectation tables. CS does not fill TABLE_1-5.*

**CS-1:** For each entity in {{topic}}: expected CRUD operations for CS role, record scope constraints, sensitive fields CS requires read access to. Name sharing rules CS relies on and any potential overreach concerns.

**CS-2** (Schema Registry CS-2 schema): `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference` -- SE Cross-Reference: "TBD -- await SE."

**CS-3** (Schema Registry CS-3 schema): `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation` -- SE Confirmation: "TBD -- await SE."

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: cumulative privilege accumulation**

**TABLE_1** (blank-cell rule applies): `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`

Every role with any privilege. SE MUST update CS-3 SE Confirmation column after filling TABLE_1.

### SE-2 / SHALL-B -- Field-Level Security Coverage

**CONTEXT-CLOSES: post-incident FLS discovery**

> RULE (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- each TABLE_2 Gap? cell is the per-row commit signal. Mark YES/NO per row; if Gap? = YES, make the TABLE_5 entry before beginning the next TABLE_2 row.

**TABLE_2** (Gap? per-row trigger ACTIVE): `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`

Sensitive categories: PII / Financial / Audit-Compliance / Operational.

> RULE (C-12): "Checked [list] for [role]; [gap type] does not apply because [reason]" -- for each category yielding no Gap? = YES, state what was examined and why.

### SE-3 / SHALL-C -- Record Access Scope

**CONTEXT-CLOSES: OWD-sharing-rule override**

**TABLE_3** (blank-cell rule applies): `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`

Every TABLE_1 role present. Defense-in-depth layer assessment for at least one operation.

### SE-4 / SHALL-D -- Privilege Escalation Analysis

**TABLE_4** (all four vectors; Checked? = YES): `Vector | Checked? | Finding | Severity`

Team inheritance / Sharing rules / Impersonation (Act on Behalf Of) / Admin or environment role override -- all Checked? = YES.

> RULE (C-15): "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" -- per-role rule-out required when no escalation found.

Update CS-2 SE Cross-Reference column after TABLE_4.

**Per-role escalation roll-up** (Schema Registry TABLE_4 sub-table):
`Role | Pre-Declaration Commitment | Composite Verdict | Mechanisms Cited | Cross-Audit`

> RULE (C-26): "PROHIBITED is any content that achieves the effect of routing the reader to another section to obtain mechanism content -- regardless of structural form" -- the Mechanisms Cited field test is not whether named disallowed forms are present but whether the content achieves the delegation effect. Any instruction or phrase that achieves the effect of directing the reader elsewhere for mechanism content is PROHIBITED, regardless of whether its structural form resembles the named examples or not.

> RULE (C-24): "Pre-decl: '[exact text]' | Filed: '[exact text]' | Match: CONFIRMED" -- each Cross-Audit cell quotes the Pre-Declaration Commitment cell and the Mechanisms Cited cell verbatim, side-by-side, with an explicit match verdict.

### SE-5 / SHALL-E -- Security Gap Inventory

**TABLE_5** (three-field Remediation per Step 0.1): `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`

> RULE (C-14): "enables auditing that C-11 inline registration actually occurred" -- each row must include discovery context. A TABLE_5 compiled post-hoc does not pass.

> RULE (C-17): "remediation block that states the fix without linking back to the discovery section does not pass" -- each Remediation entry must chain back to the SE section where the gap was discovered.

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*Structural close condition -- precondition for closing the trace, not a recommended step.*

**CA-1.1:** Registry anchor -- TABLE_1 schema (Step 0.1). Preamble anchor -- C-01: TABLE_1/SE-1/SHALL-A/CA-1.1. Verification -> PASS/FAIL

**CA-1.2:** Registry anchor -- TABLE_2 schema (Step 0.1). Preamble anchor -- C-02: TABLE_2/SE-2/SHALL-B/CA-1.2. Verification -> PASS/FAIL

**CA-1.3:** Registry anchor -- TABLE_3 schema (Step 0.1). Preamble anchor -- C-03: TABLE_3/SE-1+SE-3/SHALL-C/CA-1.3. Verification -> PASS/FAIL

**CA-1.4:** Registry anchor -- TABLE_4 schema including per-role roll-up columns (Step 0.1). Preamble anchor -- C-04: TABLE_4/SE-4/SHALL-D/CA-1.4. Verification -> PASS/FAIL

**CA-1.5:** Registry anchor -- TABLE_5 schema (Step 0.1). Preamble anchor -- C-05: TABLE_5/SE-5/SHALL-E/CA-1.5.

> RULE (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 three-field Remediation schema declared by CA at Phase 0 Step 0.1, before PHASE 1.

> RULE (C-17): "remediation block that states the fix without linking back to the discovery section does not pass" -- each Remediation entry must chain to discovery context.

Verification -> PASS/FAIL

**CA Format Compliance Verdict -- citing Phase 0:**
Citing: Schema Registry (Step 0.1 including TABLE_4 effect-anchored Mechanisms Cited prohibition and Cross-Audit verbatim format), preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX with Site Type column (Step 0.3), Phase 0 gate state log -- all CA-authored before PHASE 1 began.

> RULE (C-23): "execution record, not declarative checklist" -- Phase 0 gate recorded confirmed activation. This verdict confirms execution matched the record.

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION:**
Reviewing Step 0.3 against this output: [for each EL-01 through EL-14, confirm STATUS field CONFIRMED or flag UNCONFIRMED]. Coverage count: N/14. If N < 14: FAIL regardless of how many are confirmed. EL-14 (C-26 effect-anchored prohibition): INLINE-VERBATIM confirmed at Step 0.1 TABLE_4 Mechanisms Cited prohibition? [YES/NO]. EL-12 (C-24 verbatim cross-audit): RULE-BLOCK confirmed at SE-4 roll-up? [YES/NO].

> RULE (C-24): "precondition for closing the trace, not a recommended step" -- writing this verdict is that precondition. Trace now closed.

[C-01 through C-05 PASS/FAIL. Overall: COMPLIANT / NON-COMPLIANT.]

[TRACE CLOSED -- CA-1 verdict written.]

---

## V-02 -- Single-Axis: Global Obligation Register (C-27 target)

**Axis:** Phrasing register -- all analytically required instructions upgraded to SHALL/MUST/REQUIRED/PROHIBITED throughout; C-26 absent (prohibition clauses retain form-based language from R9 V-04 base); C-28 absent (no CS-0 explicit section)
**Hypothesis:** +weight(C-27). Every SE-X instruction governing a structurally required operation uses obligation language: no advisory phrasing for steps the model must perform. C-26 FAIL (Mechanisms Cited prohibition lists surface forms rather than anchoring to mechanism of effect). C-28 FAIL (no explicit CS-0 opening acknowledgment section).

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: Why a Permissions Trace Is Not Optional

Three inertia patterns defeat manual security audits:

**Blind spot 1 -- Post-incident FLS discovery.** FLS gaps emerge after breaches. This trace replaces reactive discovery with pre-incident, categorized enumeration across PII, Financial, Audit-Compliance, and Operational fields.

**Blind spot 2 -- Cumulative privilege accumulation.** No single Dataverse UI view surfaces the combined effect of security role depth, team membership, OWD, and sharing rules. This trace computes effective scope from all four layers together.

**Blind spot 3 -- OWD-sharing-rule override.** A Private OWD does not prevent a sharing rule configured independently from re-opening access. This trace cross-references OWD settings against every active sharing rule to surface unintended grants.

Each SE section opens with a CONTEXT-CLOSES label naming the blind spot it resolves.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. CS-first sequence. Labels appear as section headers. Each phase completes fully before the next begins.

**PHASE 0 -- CA:** Schema Registry (Step 0.1), Criterion Enforcement Matrix preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3), Phase 0 gate statement. CA is sole author.

**PHASE 1 -- CS:** Qualitative access baseline and expectation tables. Does NOT fill TABLE_1-5.

**PHASE 2 -- SE:** Fills TABLE_1-5. Dataverse-native terminology. References CS tables by Schema ID.

**PHASE 3 -- CA-1:** Double-anchor verification per criterion. Terminal verdict cites Phase 0 by label. Trace not closed until this verdict is written.

---

## PHASE 0 -- CA: SCHEMA REGISTRY, ENFORCEMENT PREAMBLE, AND LANGUAGE INDEX

### Step 0.1 -- Schema Registry (CA-authored)

**All schemas declared by CA before PHASE 1. Blank-cell prohibition global.**

**Schema ID: TABLE_1 -- Role-Operation Matrix**
Declared columns: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Blank-cell rule: Granted / Denied / Conditional (state condition inline) / N/A.

**Schema ID: TABLE_2 -- FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Gap? = YES / NO. Gap? = YES rows forward to TABLE_5 immediately (per-row, before next row begins). The Gap? boolean converts register triggering from a judgment call to a mechanical confirmation: marks YES/NO while filling the table; each Gap? = YES is the per-row commit signal for an immediate TABLE_5 entry.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" -- confirmed here at Schema Registry TABLE_2 declaration site, before PHASE 1. Downstream RULE (C-22) at SE-2.

**Schema ID: TABLE_3 -- Record Scope by Role**
Declared columns: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].

**Schema ID: TABLE_4 -- Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
All four vectors: team inheritance / sharing rules / impersonation / admin or environment role override. Checked? = YES for all.

Per-role escalation roll-up sub-table (authored in SE-4):
`Role | Pre-Declaration Commitment | Composite Verdict | Mechanisms Cited | Cross-Audit`

Mechanisms Cited field: list each mechanism inline by type. PROHIBITED: "see table above", "mechanisms cited in SE-4", "per the analysis above", "as documented above", or any equivalent form -- restate each mechanism inline.

> PLACEMENT-CRITERION CONFIRMED (C-27): "explicit prohibition naming the disallowed form" -- the Mechanisms Cited field definition above names disallowed back-reference forms using PROHIBITED (obligation-level). Confirmed here at Schema Registry TABLE_4 declaration site, before PHASE 1. Downstream RULE (C-27) at SE-4.

Cross-Audit field: verbatim-quote format required.
`Pre-decl: "[exact text copied verbatim from Pre-Declaration Commitment cell]" | Filed: "[exact text copied verbatim from Mechanisms Cited cell]" | Match: CONFIRMED`

> PLACEMENT-CRITERION CONFIRMED (C-24): verbatim-quote format declared here before PHASE 1. Downstream RULE-BLOCK at SE-4.

Equivalence clause (intent-anchored): any form that routes the reader to another section to obtain mechanism content -- whether that form is a sentence, a label, a parenthetical, or any structure that achieves the effect of delegating mechanism content -- SHALL be treated as a prohibited back-reference form regardless of its surface appearance.

**Schema ID: TABLE_5 -- Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Remediation three-field format (all three required): (1) Config change. (2) Expected state. (3) Verification step.

> PLACEMENT-CRITERION CONFIRMED (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- confirmed at Step 0.1, before PHASE 1.

**Schema ID: CS-2**: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference` -- SE Cross-Reference: "TBD -- await SE."
**Schema ID: CS-3**: `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation` -- SE Confirmation: "TBD -- await SE."

### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored)

M1, M2, M3 simultaneously active for every essential criterion. M4 pre-assigned by CA.

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- confirmed here at preamble, before PHASE 1.

**SHALL obligations (CA-authored):**
- SHALL-A: TABLE_1 SHALL be present; every cell SHALL be Granted/Denied/Conditional/N/A; every role with any privilege SHALL be included.
- SHALL-B: TABLE_2 SHALL list every sensitive field; null case SHALL be stated; Gap? = YES rows SHALL be forwarded per-row immediately.
- SHALL-C: Every TABLE_1 role SHALL appear in TABLE_3 with Effective Scope filled; ambiguous scope SHALL be flagged in TABLE_5.
- SHALL-D: TABLE_4 SHALL contain all four vectors; Checked? SHALL be YES for all four; per-role rule-out SHALL name specific mechanism and reason; per-role roll-up SHALL use verbatim Cross-Audit format.
- SHALL-E: TABLE_5 SHALL contain at least one named gap; zero-gap case SHALL provide explicit evidence rows.

### Step 0.3 -- ENFORCEMENT LANGUAGE INDEX (CA-authored)

**COMPLETENESS THRESHOLD: N-1 of N enforcement points earns 0 pts -- the same as 0 of N.**

> PLACEMENT-CRITERION CONFIRMED (C-25): Site Type column present per-row.

| EL-ID | Criterion | Enforcement Point | Verbatim Pass-Condition Phrase | Site Type | Status |
|-------|-----------|-------------------|-------------------------------|-----------|--------|
| EL-01 | C-11 | Phase 0 gate Chain 1 declaration | "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate statement |
| EL-02 | C-12 | SE-2/SE-4 negative-check instruction | "Checked [list] for [role]; [gap type] does not apply because [reason]" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-2 and SE-4 |
| EL-03 | C-13 | TABLE_5 Remediation field definition | "expected system state after the fix is applied and how to verify the fix took effect" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_5 |
| EL-04 | C-14 | SE-5 discovery-section note | "enables auditing that C-11 inline registration actually occurred" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-5 |
| EL-05 | C-15 | SE-4 per-role rule-out instruction | "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-4 |
| EL-06 | C-16 | TABLE_5 Remediation schema declaration | "declared explicitly at the top of the trace output, before the first analysis phase begins" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_5 |
| EL-07 | C-17 | CA-1.5 remediation echo instruction | "remediation block that states the fix without linking back to the discovery section does not pass" | APPLICATION-SITE | RULE-BLOCK: confirmed at CA-1.5 |
| EL-08 | C-18/C-22 | TABLE_2 Gap? column and Criterion Enforcement Matrix | "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" / "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" | DECLARATION-SITE (both) | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_2 and Step 0.2 preamble |
| EL-09 | C-23 | Phase 0 gate statement | "execution record, not declarative checklist" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate statement |
| EL-10 | C-24 | CA-1 verdict precondition | "precondition for closing the trace, not a recommended step" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate and CA-1 verdict header |
| EL-11 | C-25 | All structural enforcement points | each criterion's exact pass-condition phrase at each structural enforcement point | BOTH (per-criterion) | CONFIRMED: inline verbatim at declaration sites, RULE blocks at application sites |
| EL-12 | C-24 | TABLE_4 Cross-Audit field -- verbatim-quote format | "Pre-decl: '[exact text]' | Filed: '[exact text]' | Match: CONFIRMED" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-4 |
| EL-13 | intent-anchored equivalence | TABLE_4 Mechanisms Cited prohibition equivalence clause | "any form that routes the reader to another section to obtain mechanism content...SHALL be treated as a prohibited back-reference form regardless of its surface appearance" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_4 equivalence clause |
| EL-15 | C-27 | SHALL obligations Step 0.2 + all SE-X instructions | "At least 80% of instructions governing structurally required operations use SHALL, MUST, REQUIRED, PROHIBITED, or FORBIDDEN" | DECLARATION-SITE | INLINE-VERBATIM: SHALL-A through SHALL-E upgraded to SHALL throughout; all SE-X required operation instructions use SHALL/MUST |

**Phase 0 coverage note:** 14/14 enforcement points declared (EL-01 through EL-13 + EL-15). C-27 global obligation register annotation present: all SHALL obligations upgraded to SHALL/MUST throughout. C-26 NOT present -- prohibition clauses enumerate surface forms rather than anchoring to mechanism of effect. C-28 absent -- no explicit CS-0 opening acknowledgment section.

### Phase 0 Gate Statement

Chain 1 -- discovery to TABLE_5: every gap found during PHASE 2 SHALL be entered into TABLE_5 at the section where it is found -- entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact.
Chain 2 -- TABLE_5 to CA-1: every TABLE_5 Remediation entry SHALL be verified in PHASE 3 via double-anchor.

> PLACEMENT-CRITERION CONFIRMED (C-11 / C-23): execution record, not declarative checklist. Chain 1 active. Chain 2 active.

The CA-1 verdict is the structural close condition -- a precondition for closing the trace, not a recommended step.

**Phase 0 gate state log:**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Chain 1 -- discovery to TABLE_5, inline at discovery site | ACTIVE | EL-01 |
| TABLE_5 Remediation three-field format | ACTIVE | EL-06 |
| Gap? per-row boolean trigger | ACTIVE | EL-08 |
| Chain 2 -- TABLE_5 to CA-1 double-anchor | ACTIVE | EL-07 |
| ENFORCEMENT LANGUAGE INDEX 14/14 | CONFIRMED | EL-15 global obligation register confirmed at Step 0.2 SHALL-A through SHALL-E; EL-12 verbatim cross-audit confirmed at Step 0.1; EL-13 intent-anchored equivalence confirmed at Step 0.1 |
| CA-1 verdict as trace close precondition | ACTIVE | EL-10 |

*All 14/14 enforcement points confirmed. Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Lower-Trust Access Baseline

*CS SHALL produce CS-1 narrative and CS-2/CS-3 expectation tables. CS SHALL NOT fill TABLE_1-5.*

**CS-1:** For each entity in {{topic}}: expected CRUD operations for CS role, record scope constraints, sensitive fields CS requires read access to. Name sharing rules CS relies on and any potential overreach concerns.

**CS-2** (Schema Registry CS-2 schema): `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference` -- SE Cross-Reference: "TBD -- await SE."

**CS-3** (Schema Registry CS-3 schema): `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation` -- SE Confirmation: "TBD -- await SE."

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: cumulative privilege accumulation**

**TABLE_1** (blank-cell rule applies): `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`

TABLE_1 SHALL include every role with any privilege in scope. SE SHALL update CS-3 SE Confirmation column after filling TABLE_1. Every cell SHALL be Granted / Denied / Conditional (condition stated inline) / N/A.

### SE-2 / SHALL-B -- Field-Level Security Coverage

**CONTEXT-CLOSES: post-incident FLS discovery**

> RULE (C-22): Gap? per-row commit signal ACTIVE. SE SHALL mark YES/NO per row; if Gap? = YES, SE SHALL make the TABLE_5 entry before beginning the next TABLE_2 row.

**TABLE_2** (Gap? per-row trigger ACTIVE): `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`

TABLE_2 SHALL list every sensitive field across PII / Financial / Audit-Compliance / Operational categories.

> RULE (C-12): "Checked [list] for [role]; [gap type] does not apply because [reason]" -- for each category yielding no Gap? = YES, SE SHALL state what was examined and why.

### SE-3 / SHALL-C -- Record Access Scope

**CONTEXT-CLOSES: OWD-sharing-rule override**

**TABLE_3** (blank-cell rule applies): `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`

TABLE_3 SHALL contain every TABLE_1 role with Effective Scope filled. SE SHALL perform defense-in-depth layer assessment for at least one operation, identifying the effective enforcement layer and evaluating whether upper layers override it.

### SE-4 / SHALL-D -- Privilege Escalation Analysis

**TABLE_4** (all four vectors; Checked? = YES): `Vector | Checked? | Finding | Severity`

TABLE_4 SHALL contain all four vectors: team inheritance / sharing rules / impersonation / admin or environment role override. Checked? SHALL be YES for all four. Finding SHALL name the escalation path or per-role rule-out with specific mechanism and reason.

> RULE (C-15): "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" -- SE SHALL provide per-role rule-out when no escalation found.

SE SHALL update CS-2 SE Cross-Reference column after TABLE_4.

**Per-role escalation roll-up** (Schema Registry TABLE_4 sub-table):
`Role | Pre-Declaration Commitment | Composite Verdict | Mechanisms Cited | Cross-Audit`

> RULE (C-27): Mechanisms Cited field: SE SHALL list each mechanism inline by type. PROHIBITED: "see table above", "mechanisms cited in SE-4", "per the analysis above", "as documented above", or any equivalent form. SE SHALL NOT substitute back-reference language for inline mechanism enumeration.

> RULE (C-24): "Pre-decl: '[exact text]' | Filed: '[exact text]' | Match: CONFIRMED" -- SE SHALL quote the Pre-Declaration Commitment and Mechanisms Cited cells verbatim in each Cross-Audit cell.

### SE-5 / SHALL-E -- Security Gap Inventory

**TABLE_5** (three-field Remediation per Step 0.1): `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`

TABLE_5 SHALL contain at least one named gap. SE SHALL include discovery context in each row.

> RULE (C-14): "enables auditing that C-11 inline registration actually occurred" -- each row SHALL include discovery context. A TABLE_5 compiled post-hoc FAILS.

> RULE (C-17): "remediation block that states the fix without linking back to the discovery section does not pass" -- each Remediation entry SHALL chain back to the SE section where the gap was discovered.

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*Structural close condition -- precondition for closing the trace, not a recommended step.*

**CA-1.1:** Registry anchor -- TABLE_1 schema (Step 0.1). Preamble anchor -- C-01: TABLE_1/SE-1/SHALL-A/CA-1.1. Verification -> PASS/FAIL

**CA-1.2:** Registry anchor -- TABLE_2 schema (Step 0.1). Preamble anchor -- C-02: TABLE_2/SE-2/SHALL-B/CA-1.2. Verification -> PASS/FAIL

**CA-1.3:** Registry anchor -- TABLE_3 schema (Step 0.1). Preamble anchor -- C-03: TABLE_3/SE-1+SE-3/SHALL-C/CA-1.3. Verification -> PASS/FAIL

**CA-1.4:** Registry anchor -- TABLE_4 schema including per-role roll-up (Step 0.1). Preamble anchor -- C-04: TABLE_4/SE-4/SHALL-D/CA-1.4. Verification -> PASS/FAIL

**CA-1.5:** Registry anchor -- TABLE_5 schema (Step 0.1). Preamble anchor -- C-05: TABLE_5/SE-5/SHALL-E/CA-1.5.

> RULE (C-16): TABLE_5 three-field Remediation schema SHALL be declared at Phase 0 Step 0.1.

> RULE (C-17): each Remediation entry SHALL chain to discovery context.

Verification -> PASS/FAIL

**CA Format Compliance Verdict -- citing Phase 0:**
Citing: Schema Registry (Step 0.1), preamble (Step 0.2 including upgraded SHALL-A through SHALL-E), ENFORCEMENT LANGUAGE INDEX with Site Type column (Step 0.3), Phase 0 gate state log -- all CA-authored before PHASE 1 began.

> RULE (C-23): "execution record, not declarative checklist" -- Phase 0 gate recorded confirmed activation. This verdict confirms execution matched the record.

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION:**
Reviewing Step 0.3: [EL-01 through EL-15, confirm STATUS CONFIRMED or flag UNCONFIRMED]. Coverage count: N/14. If N < 14: FAIL. EL-15 (C-27 global obligation register): all SE-X required instructions use SHALL/MUST? [YES/NO].

> RULE (C-24): "precondition for closing the trace, not a recommended step." Trace now closed.

[C-01 through C-05 PASS/FAIL. Overall: COMPLIANT / NON-COMPLIANT.]

[TRACE CLOSED -- CA-1 verdict written.]

---

## V-03 -- Single-Axis: Sequence-Direction-Agnostic Phase Opening (C-28 target)

**Axis:** Role sequence -- SE-first execution order; explicit SE-0 acknowledgment section at Phase 1 opening declaring Phase 0 inputs by labeled artifact name before first analytical schema is filled; C-26 absent; C-27 advisory base
**Hypothesis:** +weight(C-28). SE-first sequence with SE-0 satisfies C-21 at the Phase 1 input boundary -- the structural gap that caused V-03 PARTIAL in Round 9. C-26 FAIL (prohibition clauses enumerate surface forms). C-27 PARTIAL (only MUST-level CS-3 update instruction from R9 base).

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: Why a Permissions Trace Is Not Optional

Three inertia patterns defeat manual security audits:

**Blind spot 1 -- Post-incident FLS discovery.** FLS gaps emerge after breaches. This trace replaces reactive discovery with pre-incident, categorized enumeration across PII, Financial, Audit-Compliance, and Operational fields.

**Blind spot 2 -- Cumulative privilege accumulation.** No single Dataverse UI view surfaces the combined effect of security role depth, team membership, OWD, and sharing rules. This trace computes effective scope from all four layers together.

**Blind spot 3 -- OWD-sharing-rule override.** A Private OWD does not prevent a sharing rule configured independently from re-opening access. This trace cross-references OWD settings against every active sharing rule to surface unintended grants.

Each SE section opens with a CONTEXT-CLOSES label naming the blind spot it resolves.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. **SE-first sequence** -- SE produces TABLE_1-5 in PHASE 1 without CS baseline; CS reconciles against SE output in PHASE 2. Each phase completes fully before the next begins.

**PHASE 0 -- CA:** Schema Registry (Step 0.1), Criterion Enforcement Matrix preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3), Phase 0 gate statement. CA is sole author.

**PHASE 1 -- SE:** Opens with SE-0 input declaration (Phase 0 artifacts consumed by name). Fills TABLE_1-5. No CS baseline yet.

**PHASE 2 -- CS:** Opens with CS-0 input declaration (Phase 0 + Phase 1 artifacts). Reconciles SE-authored CS-2/CS-3. Adds CS-EXPECTATION-VIOLATED rows to TABLE_5 where CS interpretation contradicts SE finding.

**PHASE 3 -- CA-1:** Double-anchor verification. Terminal verdict cites Phase 0 by label. Trace not closed until verdict is written.

---

## PHASE 0 -- CA: SCHEMA REGISTRY, ENFORCEMENT PREAMBLE, AND LANGUAGE INDEX

### Step 0.1 -- Schema Registry (CA-authored)

**All schemas declared by CA before PHASE 1. SE-first variant active.**

**Schema ID: TABLE_1 -- Role-Operation Matrix**
`Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` -- Blank-cell rule: Granted / Denied / Conditional / N/A.

**Schema ID: TABLE_2 -- FLS Coverage**
`Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?` -- Gap? = YES/NO. Gap? = YES rows forward to TABLE_5 per-row.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" -- confirmed at Schema Registry TABLE_2, before PHASE 1.

**Schema ID: TABLE_3 -- Record Scope by Role**
`Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`

**Schema ID: TABLE_4 -- Escalation Vector Inventory**
`Vector | Checked? | Finding | Severity` -- All four vectors; Checked? = YES for all.

Per-role escalation roll-up (SE-authored in PHASE 1):
`Role | Pre-Declaration Commitment | Composite Verdict | Mechanisms Cited | Cross-Audit`

Mechanisms Cited: list each mechanism inline by type. Do not write "see table above", "mechanisms cited in SE-4", "per the analysis above", "as documented above", or any equivalent form -- restate each mechanism inline.

> PLACEMENT-CRITERION CONFIRMED (C-27): prohibition on back-references named here at TABLE_4 declaration site. Downstream RULE at SE-4.

Cross-Audit: verbatim-quote format required.
`Pre-decl: "[exact text verbatim from Pre-Declaration Commitment]" | Filed: "[exact text verbatim from Mechanisms Cited]" | Match: CONFIRMED`

> PLACEMENT-CRITERION CONFIRMED (C-24): verbatim-quote format declared here before PHASE 1.

**Schema ID: TABLE_5 -- Security Gap Inventory**
`# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation` -- Remediation three-field format required.

**Schema ID: CS-2**: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference`
**Schema ID: CS-3**: `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation`

SE-first variant: SE authors CS-2 and CS-3 from SE perspective in PHASE 1. CS responds in PHASE 2.

### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored)

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**SHALL obligations:** SHALL-A through SHALL-E as defined in V-01 base.

### Step 0.3 -- ENFORCEMENT LANGUAGE INDEX (CA-authored)

**COMPLETENESS THRESHOLD: N-1 of N earns 0 pts.**

| EL-ID | Criterion | Enforcement Point | Verbatim Pass-Condition Phrase | Site Type | Status |
|-------|-----------|-------------------|-------------------------------|-----------|--------|
| EL-01 | C-11 | Phase 0 gate Chain 1 | "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate |
| EL-02 | C-12 | SE-2/SE-4 negative-check | "Checked [list] for [role]; [gap type] does not apply because [reason]" | APPLICATION-SITE | RULE-BLOCK: SE-2 and SE-4 |
| EL-03 | C-13 | TABLE_5 Remediation | "expected system state after the fix is applied and how to verify the fix took effect" | DECLARATION-SITE | INLINE-VERBATIM: Step 0.1 TABLE_5 |
| EL-04 | C-14 | SE-5 discovery note | "enables auditing that C-11 inline registration actually occurred" | APPLICATION-SITE | RULE-BLOCK: SE-5 |
| EL-05 | C-15 | SE-4 per-role rule-out | "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" | APPLICATION-SITE | RULE-BLOCK: SE-4 |
| EL-06 | C-16 | TABLE_5 Remediation schema | "declared explicitly at the top of the trace output, before the first analysis phase begins" | DECLARATION-SITE | INLINE-VERBATIM: Step 0.1 TABLE_5 |
| EL-07 | C-17 | CA-1.5 remediation echo | "remediation block that states the fix without linking back to the discovery section does not pass" | APPLICATION-SITE | RULE-BLOCK: CA-1.5 |
| EL-08 | C-18/C-22 | TABLE_2 Gap? + preamble | "boolean flag...mechanical confirmation" / "co-authorship...provable from output alone" | DECLARATION-SITE (both) | INLINE-VERBATIM: Step 0.1 TABLE_2 and Step 0.2 |
| EL-09 | C-23 | Phase 0 gate | "execution record, not declarative checklist" | DECLARATION-SITE | INLINE-VERBATIM: Phase 0 gate |
| EL-10 | C-24 | CA-1 verdict precondition | "precondition for closing the trace, not a recommended step" | DECLARATION-SITE | INLINE-VERBATIM: Phase 0 gate and CA-1 header |
| EL-11 | C-25 | All enforcement points | each criterion's exact pass-condition phrase | BOTH | CONFIRMED per-row |
| EL-12 | C-24 | TABLE_4 Cross-Audit verbatim | "Pre-decl: '[exact text]' | Filed: '[exact text]' | Match: CONFIRMED" | APPLICATION-SITE | RULE-BLOCK: SE-4 |
| EL-13 | intent-anchored equivalence | TABLE_4 Mechanisms Cited prohibition | "any equivalent form -- restate each mechanism inline" | DECLARATION-SITE | INLINE-VERBATIM: Step 0.1 TABLE_4 |
| EL-16 | C-28 | SE-0 opening acknowledgment section at Phase 1 | "Phase 1 contains a named acknowledgment section referencing at least one Phase 0 artifact by its exact Phase 0 label before the first analytical schema is filled" | DECLARATION-SITE | INLINE-VERBATIM: SE-0 declared; confirmed at Phase 1 SE-0 |

**Phase 0 coverage note:** 14/14 enforcement points. SE-first sequence active. C-28 (EL-16): SE-0 required at Phase 1 opening. C-26 absent. C-27 PARTIAL.

### Phase 0 Gate Statement

SE-first sequence active. Chain 1 -- every gap SHALL be entered into TABLE_5 at the section where found -- entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact. Chain 2 -- every TABLE_5 entry verified in PHASE 3.

**Phase 0 gate state log:**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Sequence direction | SE-FIRST | Phase 0 gate state log |
| Chain 1 -- discovery to TABLE_5 inline | ACTIVE | EL-01 |
| TABLE_5 Remediation three-field format | ACTIVE | EL-06 |
| Gap? per-row boolean trigger | ACTIVE | EL-08 |
| Chain 2 -- TABLE_5 to CA-1 | ACTIVE | EL-07 |
| ENFORCEMENT LANGUAGE INDEX 14/14 | CONFIRMED | EL-16 SE-0 requirement confirmed |
| CA-1 verdict as trace close precondition | ACTIVE | EL-10 |

*All 14/14 confirmed. SE-first sequence active. Handing to PHASE 1 -- SE.*

---

## PHASE 1 -- SE: Security Analysis (SE-first)

### SE-0: Phase 0 Input Declaration

*This section declares all Phase 0 artifacts consumed by PHASE 1 before any analytical schema is filled. Required structural mechanism for C-28 (sequence-direction-agnostic phase opening).*

Inputs consumed from Phase 0:
- **Schema Registry (Step 0.1):** TABLE_1, TABLE_2, TABLE_3, TABLE_4 (per-role roll-up sub-table included), TABLE_5, CS-2, CS-3 -- all declared by CA. SE-first variant: SE authors CS-2 and CS-3.
- **Criterion Enforcement Matrix preamble (Step 0.2):** SE appears in M2 for C-01 (SE-1), C-02 (SE-2), C-03 (SE-1+SE-3), C-04 (SE-4), C-05 (SE-5). SHALL-A through SHALL-E govern this phase.
- **ENFORCEMENT LANGUAGE INDEX (Step 0.3):** EL-01 through EL-16 confirmed by CA. EL-16 (C-28) is the criterion this SE-0 section satisfies.
- **Phase 0 gate state log:** SE-first sequence ACTIVE; Chain 1 ACTIVE; all mechanisms confirmed.

> PLACEMENT-CRITERION CONFIRMED (C-28): "Phase 1 contains a named acknowledgment section referencing at least one Phase 0 artifact by its exact Phase 0 label before the first analytical schema is filled" -- this SE-0 section references Schema Registry (Step 0.1), preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3), and Phase 0 gate state log by their exact Phase 0 exit gate labels, before TABLE_1 is filled. The SE-0 section is the structural mechanism that closes the Phase 1 input boundary for SE-first sequences. CS-first sequences require CS-0; SE-first sequences require SE-0. This invariant is sequence-direction-agnostic.

*Phase 0 inputs declared. Proceeding to SE analytical schemas.*

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: cumulative privilege accumulation**

**TABLE_1**: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`

Every role with any privilege. SE MUST update CS-3 SE Confirmation column after filling TABLE_1 (SE perspective; CS responds in PHASE 2).

### SE-2 / SHALL-B -- Field-Level Security Coverage

**CONTEXT-CLOSES: post-incident FLS discovery**

> RULE (C-22): Gap? per-row commit signal ACTIVE. Mark YES/NO per row; if Gap? = YES, TABLE_5 entry before next row.

**TABLE_2**: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`

> RULE (C-12): "Checked [list] for [role]; [gap type] does not apply because [reason]."

### SE-3 / SHALL-C -- Record Access Scope

**CONTEXT-CLOSES: OWD-sharing-rule override**

**TABLE_3**: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?` -- Every TABLE_1 role.

### SE-4 / SHALL-D -- Privilege Escalation Analysis

**TABLE_4** (all four vectors; Checked? = YES): `Vector | Checked? | Finding | Severity`

> RULE (C-15): one explicit rule-out per traced role -- naming specific actions checked and why none permit elevation.

SE MUST update CS-2 SE Cross-Reference after TABLE_4.

**Per-role escalation roll-up**: `Role | Pre-Declaration Commitment | Composite Verdict | Mechanisms Cited | Cross-Audit`

> RULE (C-27): Mechanisms Cited: do not write "see table above", "mechanisms cited in SE-4", "per the analysis above", "as documented above", or any equivalent form -- restate inline.

> RULE (C-24): `Pre-decl: "[verbatim]" | Filed: "[verbatim]" | Match: CONFIRMED`

### SE-5 / SHALL-E -- Security Gap Inventory

**TABLE_5**: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`

> RULE (C-14): each row includes discovery context.
> RULE (C-17): each Remediation chains to discovery section.

*Handing to PHASE 2 -- CS.*

---

## PHASE 2 -- CS: Lower-Trust Reconciliation (SE-first variant)

### CS-0: Phase 0 + Phase 1 Input Declaration

Inputs consumed:
- **Schema Registry (Step 0.1):** CS-2, CS-3 schemas as declared by CA.
- **Phase 1 SE exit artifacts:** TABLE_1 through TABLE_5 as filled by SE; CS-2 and CS-3 as SE-authored.
- **Criterion Enforcement Matrix preamble (Step 0.2):** CS appears in M2 for C-01+C-03 (shared with SE).

**CS-1:** Review SE-authored CS-2/CS-3. Confirm or challenge CS Expected Access. Add CS-EXPECTATION-VIOLATED rows to TABLE_5 where CS interpretation contradicts SE finding.

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*Precondition for closing the trace, not a recommended step.*

**CA-1.1 through CA-1.5:** [double-anchor: Registry anchor (Step 0.1) + Preamble anchor (C-0X/TABLE_X/SE-X/SHALL-X/CA-1.X) + Verification PASS/FAIL]

**CA Format Compliance Verdict -- citing Phase 0:**
Citing: Schema Registry (Step 0.1), preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3 -- EL-16 SE-0 requirement), Phase 0 gate state log (SE-first ACTIVE).

> RULE (C-23): execution record, not declarative checklist.

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION:**
[EL-01 through EL-16, confirm CONFIRMED or flag UNCONFIRMED]. Coverage count: N/14. If N < 14: FAIL. EL-16 (C-28): SE-0 opening acknowledgment section present at Phase 1 start with Phase 0 artifact labels before TABLE_1 filled? [YES/NO].

> RULE (C-24): writing this verdict is the precondition. Trace now closed.

[C-01 through C-05 PASS/FAIL. Overall: COMPLIANT / NON-COMPLIANT.]

[TRACE CLOSED -- CA-1 verdict written.]

---

## V-04 -- Combined: C-26 + C-27 + C-28 (CS-first, formal/technical register)

**Axis:** All three new v8 criteria combined under formal/technical register; CS-first canonical sequence
**Hypothesis:** +weight(C-26) + weight(C-27) + weight(C-28). Effect-anchored prohibition on all restriction clauses (C-26). All required instructions use SHALL/MUST (C-27). Explicit CS-0 at Phase 1 opening (C-28). Maintains R9 V-04 core: C-24 verbatim cross-audit, intent-anchored equivalence, C-16 PASS from formal register.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: Why a Permissions Trace Is Not Optional

Three inertia patterns defeat manual security audits:

**Blind spot 1 -- Post-incident FLS discovery.** FLS gaps emerge after breaches. This trace replaces reactive discovery with pre-incident, categorized enumeration across PII, Financial, Audit-Compliance, and Operational fields.

**Blind spot 2 -- Cumulative privilege accumulation.** No single Dataverse UI view surfaces the combined effect of security role depth, team membership, OWD, and sharing rules. This trace computes effective scope from all four layers together.

**Blind spot 3 -- OWD-sharing-rule override.** A Private OWD does not prevent a sharing rule configured independently from re-opening access. This trace cross-references OWD settings against every active sharing rule to surface unintended grants.

Each SE section opens with a CONTEXT-CLOSES label naming the blind spot it resolves.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. CS-first sequence. Each phase completes fully before the next begins.

**PHASE 0 -- CA:** Schema Registry (Step 0.1), Criterion Enforcement Matrix preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3), Phase 0 gate statement. CA is sole author.

**PHASE 1 -- CS:** Opens with CS-0 input declaration (Phase 0 artifacts by label). SHALL NOT fill TABLE_1-5.

**PHASE 2 -- SE:** Fills TABLE_1-5. All required instructions use SHALL/MUST.

**PHASE 3 -- CA-1:** Double-anchor verification. Terminal verdict cites Phase 0. Trace SHALL NOT close until verdict written.

---

## PHASE 0 -- CA: SCHEMA REGISTRY, ENFORCEMENT PREAMBLE, AND LANGUAGE INDEX

### Step 0.1 -- Schema Registry (CA-authored)

**All schemas SHALL be declared by CA before PHASE 1. Blank-cell prohibition is global.**

**Schema ID: TABLE_1 -- Role-Operation Matrix**
`Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` -- Blank-cell rule: Granted / Denied / Conditional (inline) / N/A.

**Schema ID: TABLE_2 -- FLS Coverage**
`Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Gap? = YES/NO. Gap? = YES rows SHALL be forwarded to TABLE_5 immediately per-row. The Gap? boolean converts register triggering from a judgment call to a mechanical confirmation.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" -- confirmed at Schema Registry TABLE_2, before PHASE 1.

**Schema ID: TABLE_3 -- Record Scope by Role**
`Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`

**Schema ID: TABLE_4 -- Escalation Vector Inventory**
`Vector | Checked? | Finding | Severity` -- All four vectors SHALL be present; Checked? SHALL be YES for all.

Per-role escalation roll-up (authored in SE-4):
`Role | Pre-Declaration Commitment | Composite Verdict | Mechanisms Cited | Cross-Audit`

Mechanisms Cited field: PROHIBITED is any instruction, phrase, or structure that achieves the effect of routing the reader to another section to obtain mechanism content -- regardless of the structural form that produces that effect. The restriction anchors to the mechanism of effect, not to named surface forms: any content that achieves delegation is PROHIBITED whether or not its form resembles any previously named example. Only inline enumeration of each mechanism by type satisfies this field.

> PLACEMENT-CRITERION CONFIRMED (C-26 / C-27): "PROHIBITED is any instruction, phrase, or structure that achieves the effect of routing the reader to another section" -- effect-anchored restriction clause (C-26) using PROHIBITED (obligation-level, C-27). Confirmed at Step 0.1 TABLE_4. Downstream RULE at SE-4.

Cross-Audit field: verbatim-quote format REQUIRED.
`Pre-decl: "[exact text verbatim from Pre-Declaration Commitment]" | Filed: "[exact text verbatim from Mechanisms Cited]" | Match: CONFIRMED`
A characterization-based cross-audit SHALL NOT satisfy this requirement.

Equivalence clause (effect-anchored): any form that achieves the effect of delegating mechanism content -- any instruction whose mechanism of effect routes the reader to another location -- is PROHIBITED under the Mechanisms Cited restriction, regardless of structural form.

> PLACEMENT-CRITERION CONFIRMED (C-26): second effect-anchored restriction clause at equivalence clause site. Both the primary prohibition and the equivalence clause anchor to mechanism of effect. Any novel form achieving the delegation effect is captured. Confirmed at Step 0.1 TABLE_4.

**Schema ID: TABLE_5 -- Security Gap Inventory**
`# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation` -- Remediation three-field format (all three REQUIRED).

> PLACEMENT-CRITERION CONFIRMED (C-16): TABLE_5 three-field format declared at Step 0.1, before PHASE 1.

**Schema ID: CS-2**: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference`
**Schema ID: CS-3**: `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation`

### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored)

M1, M2, M3 SHALL be simultaneously active. M4 pre-assigned by CA.

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- confirmed at preamble.

**SHALL obligations (CA-authored):**
- SHALL-A: TABLE_1 SHALL be present; every cell SHALL be Granted/Denied/Conditional/N/A; every role with any privilege SHALL be included.
- SHALL-B: TABLE_2 SHALL list every sensitive field; Gap? SHALL be YES/NO per row; Gap? = YES rows SHALL forward immediately.
- SHALL-C: Every TABLE_1 role SHALL appear in TABLE_3 with Effective Scope filled.
- SHALL-D: TABLE_4 SHALL contain all four vectors; Checked? SHALL be YES for all; per-role roll-up SHALL use verbatim Cross-Audit; Mechanisms Cited SHALL contain only inline enumeration (effect-anchored prohibition applies).
- SHALL-E: TABLE_5 SHALL contain at least one named gap or explicit evidence rows for zero-gap.

### Step 0.3 -- ENFORCEMENT LANGUAGE INDEX (CA-authored)

**COMPLETENESS THRESHOLD: N-1 of N earns 0 pts.**

| EL-ID | Criterion | Enforcement Point | Verbatim Pass-Condition Phrase | Site Type | Status |
|-------|-----------|-------------------|-------------------------------|-----------|--------|
| EL-01 | C-11 | Phase 0 gate Chain 1 | "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" | DECLARATION-SITE | INLINE-VERBATIM |
| EL-02 | C-12 | SE-2/SE-4 negative-check | "Checked [list] for [role]; [gap type] does not apply because [reason]" | APPLICATION-SITE | RULE-BLOCK |
| EL-03 | C-13 | TABLE_5 Remediation | "expected system state after the fix is applied and how to verify the fix took effect" | DECLARATION-SITE | INLINE-VERBATIM |
| EL-04 | C-14 | SE-5 discovery note | "enables auditing that C-11 inline registration actually occurred" | APPLICATION-SITE | RULE-BLOCK |
| EL-05 | C-15 | SE-4 per-role rule-out | "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" | APPLICATION-SITE | RULE-BLOCK |
| EL-06 | C-16 | TABLE_5 Remediation schema | "declared explicitly at the top of the trace output, before the first analysis phase begins" | DECLARATION-SITE | INLINE-VERBATIM |
| EL-07 | C-17 | CA-1.5 remediation echo | "remediation block that states the fix without linking back to the discovery section does not pass" | APPLICATION-SITE | RULE-BLOCK |
| EL-08 | C-18/C-22 | TABLE_2 Gap? + preamble | "boolean flag...mechanical confirmation" / "co-authorship...provable from output alone" | DECLARATION-SITE (both) | INLINE-VERBATIM |
| EL-09 | C-23 | Phase 0 gate | "execution record, not declarative checklist" | DECLARATION-SITE | INLINE-VERBATIM |
| EL-10 | C-24 | CA-1 verdict precondition | "precondition for closing the trace, not a recommended step" | DECLARATION-SITE | INLINE-VERBATIM |
| EL-11 | C-25 | All enforcement points | each criterion's exact pass-condition phrase | BOTH | CONFIRMED per-row |
| EL-12 | C-24 | TABLE_4 Cross-Audit verbatim | "Pre-decl: '[exact text]' | Filed: '[exact text]' | Match: CONFIRMED" | APPLICATION-SITE | RULE-BLOCK |
| EL-13 | equivalence clause | TABLE_4 equivalence | "any form that achieves the effect of delegating mechanism content...regardless of structural form" | DECLARATION-SITE | INLINE-VERBATIM |
| EL-14 | C-26 | TABLE_4 Mechanisms Cited -- effect-anchored | "PROHIBITED is any instruction, phrase, or structure that achieves the effect of routing the reader to another section" | DECLARATION-SITE | INLINE-VERBATIM: effect-anchored restriction clause satisfying C-26 |
| EL-15 | C-27 | SHALL obligations + SE-X globally | "80%+ of structurally required operation instructions use SHALL/MUST/REQUIRED/PROHIBITED/FORBIDDEN" | DECLARATION-SITE | INLINE-VERBATIM: all SE-X required operations use SHALL/MUST |
| EL-16 | C-28 | CS-0 opening acknowledgment at Phase 1 | "Phase 1 contains a named acknowledgment section referencing at least one Phase 0 artifact by its exact Phase 0 label before the first analytical schema is filled" | DECLARATION-SITE | INLINE-VERBATIM: CS-0 confirmed active at Phase 1 start |

**Phase 0 coverage note:** 16/16 enforcement points. C-26 (EL-14): effect-anchored prohibition + equivalence clause. C-27 (EL-15): global obligation register. C-28 (EL-16): CS-0 phase opening required.

### Phase 0 Gate Statement

Chain 1 -- discovery to TABLE_5: every gap SHALL be entered into TABLE_5 at the point of discovery -- not deferred to a summary section compiled after the fact.
Chain 2 -- TABLE_5 to CA-1: every Remediation entry SHALL be verified via double-anchor.

**Phase 0 gate state log:**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Chain 1 | ACTIVE | EL-01 |
| TABLE_5 three-field format | ACTIVE | EL-06 |
| Gap? per-row trigger | ACTIVE | EL-08 |
| Chain 2 | ACTIVE | EL-07 |
| ENFORCEMENT LANGUAGE INDEX 16/16 | CONFIRMED | EL-14 C-26; EL-15 C-27; EL-16 C-28 |
| CA-1 precondition | ACTIVE | EL-10 |

*All 16/16 confirmed. Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Lower-Trust Access Baseline

### CS-0: Phase 0 Input Declaration

*REQUIRED for C-28 -- named acknowledgment section declaring Phase 0 artifacts before any analytical schema is filled.*

Inputs consumed:
- **Schema Registry (Step 0.1):** TABLE_1, TABLE_2, TABLE_3, TABLE_4 (with effect-anchored Mechanisms Cited prohibition), TABLE_5, CS-2, CS-3.
- **Criterion Enforcement Matrix preamble (Step 0.2):** SHA-A through SHALL-E; CS in M2 for all five criteria.
- **ENFORCEMENT LANGUAGE INDEX (Step 0.3):** EL-01 through EL-16. EL-16 (C-28) is the criterion this CS-0 satisfies.
- **Phase 0 gate state log:** CS-first; all mechanisms ACTIVE; 16/16 confirmed.

> PLACEMENT-CRITERION CONFIRMED (C-28): CS-0 references Schema Registry (Step 0.1), preamble (Step 0.2), INDEX (Step 0.3), and Phase 0 gate state log by their exact Phase 0 labels before CS-2 or CS-3 are filled.

*Proceeding to CS analytical schemas.*

**CS-1:** For each entity: expected CRUD, scope, sensitive fields, sharing rules, overreach concerns.

**CS-2** (CS-2 schema): fill with CS perspective; SE Cross-Reference = "TBD -- await SE."

**CS-3** (CS-3 schema): fill with CS perspective; SE Confirmation = "TBD -- await SE."

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: cumulative privilege accumulation**

**TABLE_1**: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`

TABLE_1 SHALL include every role with any privilege. Every cell SHALL be Granted / Denied / Conditional (inline) / N/A. SE SHALL update CS-3 SE Confirmation after filling TABLE_1.

### SE-2 / SHALL-B -- Field-Level Security Coverage

**CONTEXT-CLOSES: post-incident FLS discovery**

> RULE (C-22): SE SHALL mark Gap? YES/NO per row; if Gap? = YES, SE SHALL make TABLE_5 entry before next row.

**TABLE_2**: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`

TABLE_2 SHALL list every sensitive field across PII / Financial / Audit-Compliance / Operational.

> RULE (C-12): SE SHALL state what was examined and why for each category yielding no Gap? = YES. Format: "Checked [list] for [role]; [gap type] does not apply because [reason]."

### SE-3 / SHALL-C -- Record Access Scope

**CONTEXT-CLOSES: OWD-sharing-rule override**

**TABLE_3**: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`

TABLE_3 SHALL contain every TABLE_1 role with Effective Scope filled. SE SHALL perform defense-in-depth layer assessment for at least one operation.

### SE-4 / SHALL-D -- Privilege Escalation Analysis

**TABLE_4** (all four vectors): `Vector | Checked? | Finding | Severity`

TABLE_4 SHALL contain all four vectors. Checked? SHALL be YES for all. Finding SHALL name escalation path or per-role rule-out.

> RULE (C-15): SE SHALL provide one explicit rule-out per traced role naming specific actions checked and why none permit elevation.

SE SHALL update CS-2 SE Cross-Reference after TABLE_4.

**Per-role escalation roll-up**: `Role | Pre-Declaration Commitment | Composite Verdict | Mechanisms Cited | Cross-Audit`

> RULE (C-26 / C-27): "PROHIBITED is any instruction, phrase, or structure that achieves the effect of routing the reader to another section to obtain mechanism content" -- restriction anchors to mechanism of effect. Any content achieving the delegation effect is PROHIBITED regardless of structural form. SE SHALL enumerate each mechanism inline by type only.

> RULE (C-24): SE SHALL quote Pre-Declaration Commitment and Mechanisms Cited verbatim: `Pre-decl: "[verbatim]" | Filed: "[verbatim]" | Match: CONFIRMED`.

### SE-5 / SHALL-E -- Security Gap Inventory

**TABLE_5**: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`

TABLE_5 SHALL contain at least one named gap. Each row SHALL include discovery context and three-field Remediation.

> RULE (C-14): each row SHALL include discovery context.
> RULE (C-17): each Remediation SHALL chain to discovery section.

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*Structural close condition -- precondition for closing the trace, not a recommended step.*

**CA-1.1:** TABLE_1 / C-01 / SE-1 / SHALL-A. Verification -> PASS/FAIL
**CA-1.2:** TABLE_2 / C-02 / SE-2 / SHALL-B. Verification -> PASS/FAIL
**CA-1.3:** TABLE_3 / C-03 / SE-1+SE-3 / SHALL-C. Verification -> PASS/FAIL
**CA-1.4:** TABLE_4 / C-04 / SE-4 / SHALL-D. Verify Mechanisms Cited uses inline only (C-26 enforcement). Verification -> PASS/FAIL
**CA-1.5:** TABLE_5 / C-05 / SE-5 / SHALL-E. Verify Remediation three-field format (C-16). Verify discovery chain-back (C-17). Verification -> PASS/FAIL

**CA Format Compliance Verdict -- citing Phase 0:**
Citing: Schema Registry (Step 0.1 -- TABLE_4 effect-anchored prohibition + equivalence clause, C-26; TABLE_5 three-field format, C-16), preamble (Step 0.2 -- SHALL-A through SHALL-E in obligation language, C-27), ENFORCEMENT LANGUAGE INDEX (Step 0.3 -- EL-14/C-26, EL-15/C-27, EL-16/C-28), Phase 0 gate state log.

> RULE (C-23): execution record, not declarative checklist.

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION:**
[EL-01 through EL-16]. Coverage count: N/16. If N < 16: FAIL. EL-14 (C-26)? [YES/NO]. EL-15 (C-27)? [YES/NO]. EL-16 (C-28): CS-0 present with Phase 0 artifact labels? [YES/NO].

> RULE (C-24): precondition for closing. Trace now closed.

[C-01 through C-05 PASS/FAIL. Overall: COMPLIANT / NON-COMPLIANT.]

[TRACE CLOSED -- CA-1 verdict written.]

---

## V-05 -- Full Combination: C-26 + C-27 + C-28 + C-13 + C-20 + C-23 + C-25

**Axis:** Maximum coverage. All three new v8 criteria plus four persistent fails: C-13 (CLEARED/NOT CLEARED verdict carry-forward), C-20 (Why Not Overridden structural column), C-23 (terminal linear chain audit), C-25 (count echo propagation). CS-first, formal/technical register throughout.
**Hypothesis:** +weight for all seven criteria. Ceiling score attempt.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: Why a Permissions Trace Is Not Optional

Three inertia patterns defeat manual security audits. Each maps to a structural blind spot closed by design.

**Failure mode 1 -- Post-incident FLS discovery.** FLS gaps surface after breaches. This trace REQUIRES pre-incident enumeration across PII, Financial, Audit-Compliance, and Operational fields. Detection: TABLE_2 Gap? = YES triggers TABLE_5 entry at discovery, not at summary.

**Failure mode 2 -- Cumulative privilege accumulation.** No Dataverse UI surfaces combined effect of role depth, team membership, OWD, and sharing rules. This trace REQUIRES effective scope computation across all four enforcement layers. Detection: TABLE_3 Effective Scope combines all four.

**Failure mode 3 -- OWD-sharing-rule override.** Private OWD does not prevent a separately configured sharing rule from re-opening access. This trace REQUIRES OWD-vs-sharing-rule cross-reference. Detection: SE-3 CONTEXT-CLOSES label anchors this check.

---

## FAILURE MODE MAP

*Pre-phase structural threat model. Satisfies C-15 (pre-phase catalog) and C-17 (skill-level threat model).*

| ID | Failure Mode | Phase/Gate Defending | Structural Mechanism |
|----|-------------|---------------------|---------------------|
| FM-1 | Post-incident FLS discovery | PHASE 2 SE-2 + TABLE_2 | Gap? per-row boolean trigger |
| FM-2 | Cumulative privilege accumulation | PHASE 2 SE-1 + TABLE_1 | All roles with BU scope; TABLE_3 effective scope |
| FM-3 | OWD-sharing-rule override | PHASE 2 SE-3 + TABLE_3 | Every sharing rule cross-referenced against OWD |
| FM-4 | Gap loss at phase transition | Phase 0 Chain 1 + routing rule | Per-row immediate TABLE_5 entry |
| FM-5 | Verdict drift across phases | TABLE_4 Security Verdict column | CLEARED/NOT CLEARED inherit from SE-1; SE-4 confirms or overrides |
| FM-6 | Incomplete scope count at aggregation | Phase 0 count M + SE-1 echo N + coverage gate | M == N checked before TABLE_2 begins |
| FM-7 | Layer-override reasoning omitted | TABLE_3 Why Not Overridden column | Required structural column per operation |

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. CS-first sequence. Each phase completes fully before the next.

**PHASE 0 -- CA:** Schema Registry (Step 0.1), Criterion Enforcement Matrix preamble (Step 0.2 -- includes entity count M declaration), ENFORCEMENT LANGUAGE INDEX (Step 0.3), Phase 0 gate statement. Phase 0 EXIT GATE: count M, all schemas, all EL points confirmed.

**PHASE 1 -- CS:** Opens with CS-0 (Phase 0 artifacts by label). Qualitative baseline. Phase 1 EXIT GATE: CS-2, CS-3 with TBD SE columns.

**PHASE 2 -- SE:** Opens with SE-1 scope acknowledgment echoing N (must equal M). Fills TABLE_1-5. CLEARED/NOT CLEARED assigned per role. Phase 2 EXIT GATE: all tables filled; N == M; verdicts assigned.

**PHASE 3 -- CA-1:** Double-anchor + terminal chain audit. Phase 3 EXIT GATE: chain trace + verdict + trace closed.

---

## PHASE 0 -- CA: SCHEMA REGISTRY, ENFORCEMENT PREAMBLE, AND LANGUAGE INDEX

### Step 0.1 -- Schema Registry (CA-authored)

**All schemas SHALL be declared by CA before PHASE 1.**

**Schema ID: TABLE_1 -- Role-Operation Matrix**
`Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` -- Blank-cell rule: Granted / Denied / Conditional (inline) / N/A.

**Schema ID: TABLE_2 -- FLS Coverage**
`Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Gap? = YES/NO. Gap? = YES rows SHALL forward to TABLE_5 immediately per-row.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" -- confirmed at Step 0.1 TABLE_2.

**Schema ID: TABLE_3 -- Record Scope by Role (defense-in-depth)**
`Role | OWD Baseline | Scope Modifier | Effective Scope | Effective Layer | Why Not Overridden | Verified?`

Why Not Overridden column (REQUIRED): for every role/operation where Effective Layer is not the outermost layer (environment/admin role), a non-generic justification SHALL name the specific override mechanism. A blank, "N/A", or generic entry constitutes a FAIL for this column.

> PLACEMENT-CRITERION CONFIRMED (C-20): Why Not Overridden is a required structural table field -- not a prose instruction to explain but a column REQUIRED for every row where Effective Layer is not outermost. Confirmed at Step 0.1 TABLE_3 declaration site, before PHASE 1.

**Schema ID: TABLE_4 -- Escalation Vector Inventory**
`Vector | Checked? | Finding | Severity` -- All four vectors; Checked? = YES.

Per-role escalation roll-up:
`Role | Security Verdict (carry-forward) | Pre-Declaration Commitment | Composite Verdict | Mechanisms Cited | Cross-Audit`

Security Verdict (carry-forward) column: states the CLEARED or NOT CLEARED verdict inherited from the most recent prior phase that assigned it, with explicit continuity language. Example: "CLEARED -- SE-1 scope assessment; no TABLE_4 finding overrides." Override syntax: "NOT CLEARED -- TABLE_4 ESCALATION-PATH overrides SE-1 CLEARED."

> PLACEMENT-CRITERION CONFIRMED (C-13): Security Verdict carry-forward column declared here before PHASE 1. Verdict assigned in SE-1 SHALL carry forward into SE-4 as persistent default. A phase that re-issues a verdict without referencing prior-phase state FAILS C-13.

Mechanisms Cited field: PROHIBITED is any instruction, phrase, or structure that achieves the effect of routing the reader to another section to obtain mechanism content -- regardless of the structural form that produces that effect. Only inline enumeration satisfies this field.

> PLACEMENT-CRITERION CONFIRMED (C-26 / C-27): effect-anchored restriction clause using PROHIBITED. Confirmed at Step 0.1 TABLE_4.

Cross-Audit: verbatim-quote format REQUIRED.
`Pre-decl: "[verbatim]" | Filed: "[verbatim]" | Match: CONFIRMED`

Equivalence clause: any form achieving the delegation effect is PROHIBITED regardless of structural appearance.

**Schema ID: TABLE_5 -- Security Gap Inventory**
`# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation` -- three-field Remediation REQUIRED.

> PLACEMENT-CRITERION CONFIRMED (C-16): TABLE_5 declared at Step 0.1, before PHASE 1.

**Schema ID: CS-2**: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference`
**Schema ID: CS-3**: `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation`

### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored)

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

**SHALL obligations:**
- SHALL-A: TABLE_1 SHALL include every role; every cell SHALL be filled; Security Verdict SHALL be assigned per role in SE-1 and carried forward.
- SHALL-B: TABLE_2 SHALL list every sensitive field; Gap? SHALL be YES/NO per row; Gap? = YES SHALL forward immediately.
- SHALL-C: Every TABLE_1 role SHALL appear in TABLE_3; Why Not Overridden SHALL contain non-generic justification for every non-outermost Effective Layer.
- SHALL-D: TABLE_4 SHALL contain all four vectors; Security Verdict carry-forward column SHALL reference prior verdict with continuity language; Mechanisms Cited SHALL use inline enumeration only.
- SHALL-E: TABLE_5 SHALL contain at least one named gap with discovery context and three-field Remediation.

**Entity count declaration (Phase 0 EXIT GATE):**
M = [CA states count of in-scope roles]. SE-1 EXIT GATE SHALL echo N with the constraint "N must equal M from Phase 0 Step 0.2." Coverage gate at SE-1 EXIT GATE SHALL confirm N == M before TABLE_2 begins.

> PLACEMENT-CRITERION CONFIRMED (C-25): entity count M declared here. SE-1 EXIT GATE SHALL echo N with cross-phase constraint naming this source.

### Step 0.3 -- ENFORCEMENT LANGUAGE INDEX (CA-authored)

| EL-ID | Criterion | Enforcement Point | Verbatim Pass-Condition Phrase | Site Type | Status |
|-------|-----------|-------------------|-------------------------------|-----------|--------|
| EL-01 | C-11 | Phase 0 gate Chain 1 | "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" | DECLARATION-SITE | INLINE-VERBATIM |
| EL-02 | C-12 | SE-2/SE-4 negative-check | "Checked [list] for [role]; [gap type] does not apply because [reason]" | APPLICATION-SITE | RULE-BLOCK |
| EL-03 | C-13 | TABLE_5 Remediation | "expected system state after the fix is applied and how to verify the fix took effect" | DECLARATION-SITE | INLINE-VERBATIM |
| EL-04 | C-14 | SE-5 discovery note | "enables auditing that C-11 inline registration actually occurred" | APPLICATION-SITE | RULE-BLOCK |
| EL-05 | C-15 | SE-4 per-role rule-out | "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" | APPLICATION-SITE | RULE-BLOCK |
| EL-06 | C-16 | TABLE_5 Remediation schema | "declared explicitly at the top of the trace output, before the first analysis phase begins" | DECLARATION-SITE | INLINE-VERBATIM |
| EL-07 | C-17 | CA-1.5 remediation echo | "remediation block that states the fix without linking back to the discovery section does not pass" | APPLICATION-SITE | RULE-BLOCK |
| EL-08 | C-18/C-22 | TABLE_2 Gap? + preamble | "boolean flag...mechanical confirmation" / "co-authorship...provable from output alone" | DECLARATION-SITE (both) | INLINE-VERBATIM |
| EL-09 | C-23 | Phase 0 gate | "execution record, not declarative checklist" | DECLARATION-SITE | INLINE-VERBATIM |
| EL-10 | C-24 | CA-1 precondition | "precondition for closing the trace, not a recommended step" | DECLARATION-SITE | INLINE-VERBATIM |
| EL-11 | C-25 | All enforcement points | each criterion's exact pass-condition phrase | BOTH | CONFIRMED per-row |
| EL-12 | C-24 | TABLE_4 Cross-Audit verbatim | "Pre-decl: '[exact text]' | Filed: '[exact text]' | Match: CONFIRMED" | APPLICATION-SITE | RULE-BLOCK |
| EL-13 | equivalence clause | TABLE_4 equivalence | "any form that achieves the effect of delegating mechanism content...regardless of structural form" | DECLARATION-SITE | INLINE-VERBATIM |
| EL-14 | C-26 | TABLE_4 Mechanisms Cited -- effect-anchored | "PROHIBITED is any instruction, phrase, or structure that achieves the effect of routing the reader to another section" | DECLARATION-SITE | INLINE-VERBATIM |
| EL-15 | C-27 | SHALL obligations + SE-X globally | "80%+ of structurally required operation instructions use SHALL/MUST/REQUIRED/PROHIBITED/FORBIDDEN" | DECLARATION-SITE | INLINE-VERBATIM |
| EL-16 | C-28 | CS-0 opening acknowledgment | "Phase 1 contains a named acknowledgment section referencing Phase 0 artifacts by exact labels before first schema filled" | DECLARATION-SITE | INLINE-VERBATIM |
| EL-17 | C-13 | TABLE_4 Security Verdict carry-forward column | "CLEARED/NOT CLEARED verdict carry-forward with explicit continuity language across consecutive phases" | DECLARATION-SITE | INLINE-VERBATIM |
| EL-18 | C-20 | TABLE_3 Why Not Overridden column | "required structural table field; non-generic justification naming specific override mechanism" | DECLARATION-SITE | INLINE-VERBATIM |
| EL-19 | C-23 | CA-1 terminal chain audit | "linear chain trace statement at terminal phase naming all phase boundaries" | APPLICATION-SITE | RULE-BLOCK |
| EL-20 | C-25 | SE-1 EXIT GATE count echo | "N must equal M from Phase 0 Step 0.2 -- intermediate phase echoes count with cross-phase constraint" | APPLICATION-SITE | RULE-BLOCK |

**Phase 0 coverage note:** 20/20 enforcement points. C-26 (EL-14), C-27 (EL-15), C-28 (EL-16), C-13 (EL-17), C-20 (EL-18), C-23 (EL-19), C-25 (EL-20).

### Phase 0 Gate Statement

Chain 1 -- every gap SHALL be entered into TABLE_5 at the section where it is found -- entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact.
Chain 2 -- every TABLE_5 Remediation entry SHALL be verified via double-anchor.

**Phase 0 gate state log:**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Chain 1 | ACTIVE | EL-01 |
| TABLE_5 three-field format | ACTIVE | EL-06 |
| Gap? per-row trigger | ACTIVE | EL-08 |
| Chain 2 | ACTIVE | EL-07 |
| Entity count M declared | ACTIVE | Step 0.2; EL-20 echo at SE-1 |
| ENFORCEMENT LANGUAGE INDEX 20/20 | CONFIRMED | EL-14/C-26, EL-15/C-27, EL-16/C-28, EL-17/C-13, EL-18/C-20, EL-19/C-23, EL-20/C-25 |
| CA-1 precondition | ACTIVE | EL-10 |

*All 20/20 confirmed. Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Lower-Trust Access Baseline

### CS-0: Phase 0 Input Declaration

*REQUIRED for C-28.*

Inputs consumed:
- **Schema Registry (Step 0.1):** TABLE_1, TABLE_2, TABLE_3 (Why Not Overridden column), TABLE_4 (Security Verdict column + effect-anchored Mechanisms Cited prohibition), TABLE_5, CS-2, CS-3.
- **Criterion Enforcement Matrix preamble (Step 0.2):** SHALL-A through SHALL-E; entity count M = [M value].
- **ENFORCEMENT LANGUAGE INDEX (Step 0.3):** EL-01 through EL-20. EL-16 (C-28) is the criterion this CS-0 satisfies.
- **Phase 0 gate state log:** CS-first; all mechanisms ACTIVE; 20/20 confirmed.

> PLACEMENT-CRITERION CONFIRMED (C-28): CS-0 references Schema Registry (Step 0.1), preamble (Step 0.2), INDEX (Step 0.3), and Phase 0 gate state log by their exact Phase 0 labels before CS-2 or CS-3 are filled.

**CS-1:** For each entity: CRUD, scope, sensitive fields, sharing rules, overreach concerns.

**CS-2** (CS-2 schema): `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference` -- TBD.

**CS-3** (CS-3 schema): `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation` -- TBD.

**Phase 1 EXIT GATE:**
- CS-2 rows present with SE Cross-Reference = TBD: [YES/NO]
- CS-3 rows present with SE Confirmation = TBD: [YES/NO]

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: Failure mode 2 (cumulative privilege accumulation)**

**TABLE_1**: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`

TABLE_1 SHALL include every role with any privilege. Every cell SHALL be Granted / Denied / Conditional (inline) / N/A. SE SHALL update CS-3 SE Confirmation after filling TABLE_1.

**Security Verdict initial assignment (C-13 mechanism):** For each TABLE_1 role, SE SHALL assign CLEARED or NOT CLEARED based on SE-1 scope assessment. Format: "Role X: CLEARED -- SE-1 scope assessment; carry-forward to SE-4."

**SE-1 EXIT GATE (C-22 / C-25):**
- N = [count of roles in TABLE_1] (must equal M from Phase 0 Step 0.2)
- N == M? [YES / NO -- if NO: STOP, resolve discrepancy]
- All TABLE_1 cells filled: [YES/NO]
- Security Verdict assigned per role: [YES/NO]

> RULE (C-25): "N must equal M from Phase 0 Step 0.2" -- this EXIT GATE echoes the count variable with an explicit cross-phase constraint naming Phase 0 Step 0.2. No intermediate phase may silently redefine the scope between count declaration and coverage gate.

*TABLE_2 population begins only after N == M confirmed.*

### SE-2 / SHALL-B -- Field-Level Security Coverage

**CONTEXT-CLOSES: Failure mode 1 (post-incident FLS discovery)**

> RULE (C-22): SE SHALL mark Gap? YES/NO per row. If Gap? = YES, SE SHALL make TABLE_5 entry before next row.

**TABLE_2**: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`

TABLE_2 SHALL list every sensitive field across PII / Financial / Audit-Compliance / Operational.

> RULE (C-12): SE SHALL state: "Checked [list] for [role]; [gap type] does not apply because [reason]" for each category yielding no Gap? = YES.

### SE-3 / SHALL-C -- Record Access Scope (defense-in-depth)

**CONTEXT-CLOSES: Failure mode 3 (OWD-sharing-rule override)**

**TABLE_3**: `Role | OWD Baseline | Scope Modifier | Effective Scope | Effective Layer | Why Not Overridden | Verified?`

TABLE_3 SHALL contain every TABLE_1 role. Effective Scope SHALL be filled. Effective Layer SHALL name the governing layer from: 1=environment/admin, 2=security role+BU, 3=team membership, 4=FLS/column profiles.

> RULE (C-20): Why Not Overridden column SHALL contain a non-generic justification for every role/operation where Effective Layer is not layer 1. A blank or generic entry FAILS. For at least one row, justification SHALL name the specific override mechanism, e.g.: "Environment Admin role not assigned to this role; BU scope is the outermost active constraint."

### SE-4 / SHALL-D -- Privilege Escalation Analysis

**TABLE_4** (all four vectors): `Vector | Checked? | Finding | Severity`

TABLE_4 SHALL contain all four vectors. Checked? SHALL be YES for all.

> RULE (C-15): SE SHALL provide one explicit rule-out per traced role naming specific actions checked and why none permit elevation.

SE SHALL update CS-2 SE Cross-Reference after TABLE_4.

**Per-role escalation roll-up**: `Role | Security Verdict (carry-forward) | Pre-Declaration Commitment | Composite Verdict | Mechanisms Cited | Cross-Audit`

Security Verdict (carry-forward): SE SHALL state the verdict inherited from SE-1 with explicit continuity language. If TABLE_4 produces a new finding: "NOT CLEARED -- TABLE_4 finding overrides SE-1 CLEARED verdict." If no new finding: "CLEARED -- SE-1 verdict persists; no TABLE_4 finding overrides."

> RULE (C-13): Security Verdict column SHALL reference SE-1 verdict with explicit continuity language. Re-issuing a verdict without referencing prior-phase state FAILS.

> RULE (C-26 / C-27): "PROHIBITED is any instruction, phrase, or structure that achieves the effect of routing the reader to another section to obtain mechanism content" -- SE SHALL enumerate each mechanism inline only.

> RULE (C-24): SE SHALL quote verbatim: `Pre-decl: "[verbatim]" | Filed: "[verbatim]" | Match: CONFIRMED`.

### SE-5 / SHALL-E -- Security Gap Inventory

**TABLE_5**: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`

> RULE (C-14): each row SHALL include discovery context.
> RULE (C-17): each Remediation SHALL chain to discovery section.

**Phase 2 EXIT GATE:**
- All tables filled: [YES/NO per table]
- TABLE_3 Why Not Overridden: at least one non-generic entry: [YES/NO] (C-20 enforcement)
- TABLE_4 Security Verdict: all roles reference SE-1 with continuity language: [YES/NO] (C-13 enforcement)
- N == M at SE-1 EXIT GATE: [YES/NO] (C-25 enforcement)

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*Structural close condition -- precondition for closing the trace, not a recommended step.*

**CA-1.1:** TABLE_1 / C-01 / SE-1 / SHALL-A. Verification -> PASS/FAIL
**CA-1.2:** TABLE_2 / C-02 / SE-2 / SHALL-B. Verification -> PASS/FAIL
**CA-1.3:** TABLE_3 with Why Not Overridden column / C-03 / SE-1+SE-3 / SHALL-C. Verify Why Not Overridden has non-generic entry (C-20 enforcement). Verification -> PASS/FAIL
**CA-1.4:** TABLE_4 with Security Verdict carry-forward column / C-04 / SE-4 / SHALL-D. Verify Security Verdict references SE-1 with continuity language (C-13 enforcement). Verify Mechanisms Cited inline only (C-26 enforcement). Verification -> PASS/FAIL
**CA-1.5:** TABLE_5 / C-05 / SE-5 / SHALL-E. Verify three-field Remediation (C-16). Verify discovery chain-back (C-17). Verification -> PASS/FAIL

**CA Format Compliance Verdict -- citing Phase 0:**
Citing: Schema Registry (Step 0.1 -- TABLE_3 Why Not Overridden column, TABLE_4 Security Verdict column and effect-anchored Mechanisms Cited prohibition), preamble (Step 0.2 -- entity count M, SHALL-A through SHALL-E), ENFORCEMENT LANGUAGE INDEX (Step 0.3 -- EL-01 through EL-20), Phase 0 gate state log.

> RULE (C-23): execution record, not declarative checklist.

**Terminal Chain Audit (C-23 enforcement):**

Phase 0 EXIT GATE (Schema Registry Step 0.1 + preamble Step 0.2 with count M + INDEX Step 0.3 + gate state log)
-> Phase 1 INPUT (CS-0 acknowledges Phase 0 Schema Registry, preamble, INDEX, gate log by label)
-> Phase 1 EXIT GATE (CS-2 + CS-3 with TBD SE Cross-Reference/Confirmation declared)
-> Phase 2 INPUT (SE-1 opens; consumes Phase 1 CS-2 + CS-3 by Schema ID; SE-1 EXIT GATE echoes N == M from Phase 0)
-> Phase 2 EXIT GATE (TABLE_1 through TABLE_5 filled; N == M confirmed; CLEARED/NOT CLEARED assigned; Why Not Overridden populated)
-> Phase 3 INPUT (CA-1.1 through CA-1.5 consume TABLE_1-5 by Schema ID; cite Phase 0 Schema Registry and preamble by label)
-> Phase 3 EXIT GATE (terminal chain audit written; CA-1 verdict written; trace closed)

No orphan phase boundaries. Every phase boundary closed.

> RULE (C-23 enforcement): "linear chain trace statement at terminal phase naming all phase boundaries from Phase 0 EXIT GATE through Phase N EXIT GATE" -- this terminal chain audit is that statement. Every phase in the prompt appears above.

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION:**
[EL-01 through EL-20]. Coverage: N/20. If N < 20: FAIL. EL-14 (C-26)? [YES/NO]. EL-15 (C-27)? [YES/NO]. EL-16 (C-28): CS-0 present? [YES/NO]. EL-17 (C-13): Security Verdict carry-forward column? [YES/NO]. EL-18 (C-20): Why Not Overridden column? [YES/NO]. EL-19 (C-23): terminal chain audit above names all phase boundaries? [YES/NO]. EL-20 (C-25): SE-1 EXIT GATE echoes N with "must equal M from Phase 0 Step 0.2"? [YES/NO].

> RULE (C-24): precondition for closing. Trace now closed.

[C-01 through C-05 PASS/FAIL. Overall: COMPLIANT / NON-COMPLIANT.]

[TRACE CLOSED -- CA-1 verdict written.]
