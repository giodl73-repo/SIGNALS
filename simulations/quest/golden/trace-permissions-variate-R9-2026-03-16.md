# trace-permissions Variate -- Round 9 (rubric v9 -- C-31/C-32 target)
**Date:** 2026-03-16
**Rubric:** v9 (C-01 through C-32 -- C-31/C-32 added from Round 8 excellence signals)
**Target criteria:** C-31 (verbatim-quote format in cross-audit assertion), C-32 (intent-anchored equivalence clause in prohibition instructions)

**State entering Round 9:**

| Variation | Prior score (N=23 aspirational) | Gap under v9 (N=25 aspirational) |
|-----------|----------------------------------|----------------------------------|
| Best prior (all C-01 through C-30) | 23/23 aspirational passing | C-31 absent (-1), C-32 absent (-1) = 23/25 aspirational |

Round 9 holds the prior structural core (CA -> CS -> SE -> CA-1, Schema Registry, ENFORCEMENT LANGUAGE INDEX with Site Type column, bidirectional chains, dual-mechanism, three-field no-finding, cross-audit present but characterization-based, equivalence clauses present but bare) and adds C-31/C-32 mechanisms across three single-axis tests and two combined variations.

Baseline INDEX entry count from prior best: EL-01 through EL-11 (11 enforcement points). Round 9 adds EL-12 (C-29/C-31 verbatim cross-audit) and/or EL-13 (C-30/C-32 intent-anchored equivalence) to reach 12 or 13 enforcement points.

---

## Round 9 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format -- C-31 isolation: VERBATIM-CROSS-AUDIT format annotation at Step 0.1 TABLE_4 declaration site and SE-4 RULE-BLOCK; EL-12 added to INDEX; equivalence clauses remain bare (C-32 fails by design) | C-31 requires the cross-audit assertion to quote both the pre-declaration and the closing mechanism column verbatim. V-01 adds `Pre-decl: "[exact text]" | Filed: "[exact text]" | Match: CONFIRMED` format. Equivalence clauses remain "or any equivalent form" without named effect. Hypothesis: +weight(C-31); C-32 fails. |
| V-02 | Lifecycle emphasis -- C-32 isolation: intent-anchored equivalence clauses at Step 0.1 TABLE_4 prohibition declaration site and SE-4 instruction; cross-audit assertion uses characterization format (C-31 fails by design) | C-32 requires the equivalence clause to name the prohibited mechanism of effect. V-02 rewrites prohibition instructions to include "or any equivalent form that delegates mechanism content to another section" and "or any equivalent form that co-mingles content from another structural site." Cross-audit uses characterization. Hypothesis: +weight(C-32); C-31 fails. |
| V-03 | Role sequence -- SE-first + C-31 isolation: SE executes before CS; C-31 verbatim cross-audit present; C-32 absent | Stress-test: does verbatim cross-audit mechanism (C-31) survive phase reordering? SE fills TABLE_1-5 without CS baseline; CS reconciles against SE output in PHASE 2. Cross-audit still quotes verbatim from SE-4 pre-declaration and closing mechanism column. Hypothesis: +weight(C-31); C-32 fails; SE-first does not degrade C-31. |
| V-04 | Combined C-31 + C-32, phrasing register formal/technical + CS-first: both mechanisms active; all instruction language uses SHALL/MUST/PROHIBITED markers; no conversational framing | V-01 proved C-31; V-02 proved C-32. V-04 combines both under formal/technical register. CS-first canonical sequence. Hypothesis: +weight(C-31) + weight(C-32). |
| V-05 | Full combination C-31 + C-32 + quantified inertia framing, CS-first: verbatim cross-audit + intent-anchored equivalence + CONTEXT opens with measurable claims about manual audit detection failure | Maximum coverage. C-31: verbatim-quote cross-audit at SE-4, indexed at EL-12. C-32: intent-anchored equivalence at Step 0.1 TABLE_4 and SE-4, indexed at EL-13. Inertia: CONTEXT quantifies what manual security audits structurally miss. Hypothesis: +weight(C-31) + weight(C-32); achieves 25/25 aspirational. |

---

## V-01 -- Single-Axis: Verbatim Cross-Audit Format (C-31 target)

**Axis:** Output format -- VERBATIM-CROSS-AUDIT annotation at TABLE_4 declaration site (Step 0.1); EL-12 added to INDEX; equivalence clauses remain bare (C-32 fails)
**Hypothesis:** +weight(C-31); C-32 fails (equivalence clause has no named prohibited effect). Isolated test of whether the verbatim-quote format at the SE-4 instruction site satisfies C-31.

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

Mechanisms Cited field: list each mechanism inline by type. Do not write "see table above", "mechanisms cited in SE-4", "per the analysis above", "as documented above", or any equivalent form -- restate each mechanism inline.

> PLACEMENT-CRITERION CONFIRMED (C-27): "explicit prohibition naming the disallowed form" -- the Mechanisms Cited field definition above names disallowed forms. Confirmed here at Schema Registry TABLE_4 declaration site, before PHASE 1. Downstream RULE (C-27) appears at SE-4.

Cross-Audit field: verbatim-quote format required. Each Cross-Audit cell uses the format:
`Pre-decl: "[exact text copied verbatim from Pre-Declaration Commitment cell]" | Filed: "[exact text copied verbatim from Mechanisms Cited cell]" | Match: CONFIRMED`
This format quotes both sites exactly, making match verification a zero-judgment mechanical operation. A characterization-based cross-audit does not satisfy C-31.

> PLACEMENT-CRITERION CONFIRMED (C-29 / C-31): "Pre-decl: '[exact text]' | Filed: '[exact text]' | Match: CONFIRMED" -- the verbatim-quote format above quotes both the Pre-Declaration Commitment and the Mechanisms Cited cell verbatim, making the cross-audit a zero-judgment mechanical match operation rather than a reader-performed semantic comparison. Confirmed here at Schema Registry TABLE_4 Cross-Audit field declaration site, before PHASE 1. Downstream RULE-BLOCK (C-31) appears at SE-4.

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

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- this preamble establishes the Gap? boolean as the structural enforcement mechanism. Confirmed here at the preamble declaration site, before PHASE 1. Downstream RULE (C-22) appears at SE-2.

**SHALL obligations (CA-authored):**
- SHALL-A: TABLE_1 present; every cell Granted/Denied/Conditional/N/A; every role with any privilege included.
- SHALL-B: TABLE_2 lists every sensitive field; null case stated; Gap? = YES rows forwarded per-row.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Effective Scope filled; ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 all four vectors; per-role rule-out naming specific mechanism and reason; per-role roll-up with Pre-Declaration Commitment, Composite Verdict, Mechanisms Cited (inline), Cross-Audit (verbatim format per Step 0.1).
- SHALL-E: TABLE_5 at least one named gap; zero-gap case requires explicit evidence rows.

### Step 0.3 -- ENFORCEMENT LANGUAGE INDEX (CA-authored)

**COMPLETENESS THRESHOLD: N-1 of N enforcement points earns 0 pts -- the same as 0 of N.**

> PLACEMENT-CRITERION CONFIRMED (C-25 / C-28): "type designation is what makes C-27's two-mechanism requirement mechanically verifiable from the INDEX alone" -- each INDEX row carries a Site Type column classifying the enforcement point as DECLARATION-SITE or APPLICATION-SITE. A scorer reads the type column and knows which confirmation mechanism is required without cross-referencing criterion definitions.

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
| EL-12 | C-29 / C-31 | TABLE_4 Cross-Audit field definition + SE-4 roll-up instruction | "Pre-decl: '[exact text]' | Filed: '[exact text]' | Match: CONFIRMED" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-4; PLACEMENT annotation at Step 0.1 TABLE_4 Cross-Audit field |

**Phase 0 coverage note:** 12/12 enforcement points declared. Site Type breakdown: 6 DECLARATION-SITE (EL-01/03/06/08/09/10), 5 APPLICATION-SITE (EL-02/04/05/07/12), 1 BOTH (EL-11). C-31 verbatim cross-audit annotation present at Step 0.1 TABLE_4. C-32 absent -- equivalence clauses are bare.

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
| ENFORCEMENT LANGUAGE INDEX 12/12 | CONFIRMED | Step 0.3; C-25 Site Type column confirmed per-row; C-31 verbatim cross-audit annotation confirmed at Step 0.1 TABLE_4 (EL-12) |
| CA-1 verdict as trace close precondition | ACTIVE | Inline verbatim at CA-1 verdict header (EL-10) |

*All 12/12 enforcement points confirmed. All structures active. Handing to PHASE 1 -- CS.*

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

Every role with any privilege. Update CS-3 SE Confirmation column after filling TABLE_1.

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

For each role:
- Pre-Declaration Commitment: state the structural assumptions governing NOT POSSIBLE verdicts for this role BEFORE analysis begins.
- Composite Verdict: name each NOT POSSIBLE vector's mechanism type inline -- not by count alone.
- Mechanisms Cited: list each mechanism inline by type. Do not write "see table above", "mechanisms cited in SE-4", "per the analysis above", "as documented above", or any equivalent form -- restate each mechanism inline.

> RULE (C-27): "explicit prohibition naming the disallowed form" -- the Mechanisms Cited instruction above names disallowed back-reference forms. Each mechanism restated inline.

> RULE (C-29 / C-31): "Pre-decl: '[exact text]' | Filed: '[exact text]' | Match: CONFIRMED" -- each Cross-Audit cell quotes the Pre-Declaration Commitment cell and the Mechanisms Cited cell verbatim, side-by-side, with an explicit match verdict. A characterization-based cross-audit ("Pre-decl identifies mechanism type X; Filed confirms mechanism type X; match confirmed") does not satisfy C-31. Verbatim quotation required at both sites. Example: `Pre-decl: "No owner-access team accepts this role under current team membership configuration" | Filed: "No owner-access team accepts this role under current team membership configuration" | Match: CONFIRMED`

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
Citing: Schema Registry (Step 0.1 including TABLE_4 Cross-Audit verbatim format), preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX with Site Type column (Step 0.3), Phase 0 gate state log -- all CA-authored before PHASE 1 began.

> RULE (C-23): "execution record, not declarative checklist" -- Phase 0 gate recorded confirmed activation. This verdict confirms execution matched the record.

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION (C-28):**
Reviewing Step 0.3 against this output: [for each EL-01 through EL-12, confirm STATUS field CONFIRMED or flag UNCONFIRMED]. Coverage count: N/12. If N < 12: C-28 = FAIL regardless of how many are confirmed. EL-12 (C-29/C-31 verbatim cross-audit): RULE-BLOCK confirmed at SE-4 roll-up? [YES/NO].

> RULE (C-24): "precondition for closing the trace, not a recommended step" -- writing this verdict is that precondition. Trace now closed.

[C-01 through C-05 PASS/FAIL. Overall: COMPLIANT / NON-COMPLIANT.]

[TRACE CLOSED -- CA-1 verdict written.]

---

## V-02 -- Single-Axis: Intent-Anchored Equivalence Clause (C-32 target)

**Axis:** Lifecycle emphasis -- intent-anchored equivalence clauses at Step 0.1 TABLE_4 prohibition declaration site and SE-4 instruction (EL-13 added to INDEX); cross-audit uses characterization format (C-31 fails by design)
**Hypothesis:** +weight(C-32); C-31 fails (cross-audit assertion characterizes both sites rather than quoting verbatim). Isolated test of whether naming the prohibited mechanism of effect in the equivalence clause satisfies C-32.

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
Gap? = YES / NO. Gap? = YES rows forward to TABLE_5 immediately (per-row). The Gap? boolean converts register triggering from a judgment call to a mechanical confirmation.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" -- confirmed here at Schema Registry TABLE_2 declaration site, before PHASE 1. Downstream RULE (C-22) at SE-2.

**Schema ID: TABLE_3 -- Record Scope by Role**
Declared columns: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`

**Schema ID: TABLE_4 -- Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
All four vectors; Checked? = YES for all.

Per-role escalation roll-up sub-table (authored in SE-4):
`Role | Pre-Declaration Commitment | Composite Verdict | Mechanisms Cited | Cross-Audit`

Mechanisms Cited field: list each mechanism inline by type. Do not write "see table above", "mechanisms cited in SE-4", "see vectors above", "as documented above", "consistent with the analysis above", "per the findings above", whether that form is a sentence, a label, a parenthetical phrase, or any equivalent form that delegates mechanism content to another section rather than restating it inline.

> PLACEMENT-CRITERION CONFIRMED (C-27 / C-30 / C-32): "explicit prohibition naming the disallowed form" (C-27) and equivalence clause with named prohibited effect (C-30 / C-32) -- the Mechanisms Cited prohibition above names six specific disallowed forms, names their structural categories ("whether that form is a sentence, a label, a parenthetical phrase"), and anchors the equivalence clause to the prohibited mechanism of effect ("that delegates mechanism content to another section rather than restating it inline"). A form that delegates mechanism content is prohibited regardless of its structural appearance. Confirmed here at Schema Registry TABLE_4 declaration site, before PHASE 1. Downstream RULE (C-27 / C-32) at SE-4.

Cross-Audit field: states that the pre-declared assumption and the closing mechanism column name the same structural fact for each vector. A cross-audit identifies the structural fact at both sites and confirms alignment. [Note: this variation uses characterization format -- C-31 verbatim-quote format is NOT applied here.]

**Schema ID: TABLE_5 -- Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Remediation three-field format: (1) Config change. (2) Expected state. (3) Verification step.

> PLACEMENT-CRITERION CONFIRMED (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- confirmed at Step 0.1, before PHASE 1. Downstream RULE (C-16) at CA-1.5.

**Schema ID: CS-2**: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference` -- SE Cross-Reference: "TBD -- await SE."
**Schema ID: CS-3**: `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation` -- SE Confirmation: "TBD -- await SE."

### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored)

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- confirmed here at preamble declaration site, before PHASE 1. Downstream RULE (C-22) at SE-2.

**SHALL obligations:** SHALL-A through SHALL-E as defined above. SHALL-D: TABLE_4 all four vectors; per-role rule-out naming specific mechanism and reason; per-role roll-up with intent-anchored Mechanisms Cited prohibition; Cross-Audit confirming pre-declaration / mechanism column alignment.

### Step 0.3 -- ENFORCEMENT LANGUAGE INDEX (CA-authored)

**COMPLETENESS THRESHOLD: N-1 of N enforcement points earns 0 pts -- the same as 0 of N.**

> PLACEMENT-CRITERION CONFIRMED (C-25 / C-28): Site Type column present per-row. DECLARATION-SITE rows require inline verbatim confirmation; APPLICATION-SITE rows require RULE-BLOCK confirmation.

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
| EL-13 | C-30 / C-32 | TABLE_4 Mechanisms Cited prohibition + SE-4 instruction | "or any equivalent form that delegates mechanism content to another section rather than restating it inline" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_4 Mechanisms Cited prohibition; second clause for column exclusivity confirmed at SE-4 |

**Phase 0 coverage note:** 12/12 enforcement points declared. Site Type breakdown: 6 DECLARATION-SITE (EL-01/03/06/08/09/10/13), 4 APPLICATION-SITE (EL-02/04/05/07), 1 BOTH (EL-11). C-32 intent-anchored equivalence annotation present at Step 0.1 TABLE_4. C-31 absent -- cross-audit uses characterization format.

### Phase 0 Gate Statement

Chain 1 -- discovery to TABLE_5: every gap found during PHASE 2 is entered into TABLE_5 at the section where found -- entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact.
Chain 2 -- TABLE_5 to CA-1: every Remediation entry verified via double-anchor.

> PLACEMENT-CRITERION CONFIRMED (C-11 / C-23): execution record confirmed. Chain 1 active. Chain 2 active. CA-1 verdict is the structural close condition -- a precondition for closing the trace, not a recommended step.

**Phase 0 gate state log:**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Chain 1 -- discovery to TABLE_5, inline at discovery site | ACTIVE | EL-01 |
| TABLE_5 Remediation three-field format | ACTIVE | EL-06 |
| Gap? per-row boolean trigger | ACTIVE | EL-08 |
| Chain 2 -- TABLE_5 to CA-1 double-anchor | ACTIVE | EL-07 |
| ENFORCEMENT LANGUAGE INDEX 12/12 | CONFIRMED | EL-13 intent-anchored equivalence confirmed at Step 0.1 TABLE_4 |
| CA-1 verdict as trace close precondition | ACTIVE | EL-10 |

*All 12/12 enforcement points confirmed. Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Lower-Trust Access Baseline

*CS produces CS-1 narrative and CS-2/CS-3 expectation tables. CS does not fill TABLE_1-5.*

**CS-1:** For each entity: expected CRUD, record scope, sensitive fields CS needs. Name sharing rules relied on.

**CS-2** (CS-2 schema): `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference` -- "TBD -- await SE."

**CS-3** (CS-3 schema): `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation` -- "TBD -- await SE."

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: cumulative privilege accumulation**

**TABLE_1** (blank-cell rule applies): `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`

Update CS-3 SE Confirmation after filling TABLE_1.

### SE-2 / SHALL-B -- Field-Level Security Coverage

**CONTEXT-CLOSES: post-incident FLS discovery**

> RULE (C-22): Gap? per-row commit signal active. Mark YES/NO per row; if Gap? = YES, TABLE_5 entry before next row.

**TABLE_2** (Gap? per-row trigger ACTIVE): `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`

> RULE (C-12): "Checked [list] for [role]; [gap type] does not apply because [reason]" -- per category yielding no Gap? = YES.

### SE-3 / SHALL-C -- Record Access Scope

**CONTEXT-CLOSES: OWD-sharing-rule override**

**TABLE_3**: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?` -- Every TABLE_1 role.

### SE-4 / SHALL-D -- Privilege Escalation Analysis

**TABLE_4** (all four vectors; Checked? = YES): `Vector | Checked? | Finding | Severity`

Team inheritance / Sharing rules / Impersonation / Admin override -- all YES.

> RULE (C-15): "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation."

**Per-role escalation roll-up:**
`Role | Pre-Declaration Commitment | Composite Verdict | Mechanisms Cited | Cross-Audit`

> RULE (C-27 / C-30 / C-32): "explicit prohibition naming the disallowed form" with intent-anchored equivalence -- Mechanisms Cited field: do not write "see table above", "mechanisms cited in SE-4", "see vectors above", "as documented above", "consistent with the analysis above", "per the findings above", whether that form is a sentence, a label, a parenthetical phrase, or any equivalent form that delegates mechanism content to another section rather than restating it inline. A form that produces the effect of delegation -- routing the reader to another location for the mechanism content -- is prohibited regardless of its structural appearance.

Cross-Audit field: confirm that the Pre-Declaration Commitment and the Mechanisms Cited cell name the same structural fact for each vector. State the structural fact at both sites and confirm alignment. [Characterization format -- C-31 verbatim-quote not applied in this variation.]

### SE-5 / SHALL-E -- Security Gap Inventory

**TABLE_5** (three-field Remediation): `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`

> RULE (C-14): each row must include discovery context.
> RULE (C-17): each Remediation must chain to discovery section.

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*Structural close condition -- precondition for closing the trace, not a recommended step.*

**CA-1.1 through CA-1.5:** [double-anchor format: Registry anchor (Step 0.1 schema) + Preamble anchor (C-0X: TABLE_X/SE-X/SHALL-X/CA-1.X) + Verification -> PASS/FAIL per criterion]

> RULE (C-16): TABLE_5 three-field schema declared at Phase 0 Step 0.1.
> RULE (C-17): each Remediation entry chains to discovery context.

**CA Format Compliance Verdict -- citing Phase 0:**
Citing: Schema Registry (Step 0.1 including TABLE_4 intent-anchored Mechanisms Cited prohibition), preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3), Phase 0 gate state log.

> RULE (C-23): execution record confirmed.

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION (C-28):**
[EL-01 through EL-13 -- confirm STATUS CONFIRMED or flag UNCONFIRMED]. Coverage count: N/12. If N < 12: C-28 = FAIL. EL-13 (C-30/C-32 intent-anchored equivalence): INLINE-VERBATIM confirmed at Step 0.1 TABLE_4? [YES/NO].

> RULE (C-24): writing this verdict is the precondition for closing the trace. Trace now closed.

[C-01 through C-05 PASS/FAIL. Overall: COMPLIANT / NON-COMPLIANT.]

[TRACE CLOSED -- CA-1 verdict written.]

---

## V-03 -- Single-Axis: SE-First Sequence + Verbatim Cross-Audit (C-31 target, role-sequence stress test)

**Axis:** Role sequence -- SE executes before CS (SE-first); C-31 verbatim cross-audit present; C-32 absent
**Hypothesis:** +weight(C-31); C-32 fails; SE-first sequence does not degrade C-31 pass. Tests whether the verbatim cross-audit mechanism survives inversion of the CS/SE execution order.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: Why a Permissions Trace Is Not Optional

Three inertia patterns defeat manual security audits:

**Blind spot 1 -- Post-incident FLS discovery.** FLS gaps emerge after breaches. This trace replaces reactive discovery with pre-incident, categorized enumeration by field sensitivity class.

**Blind spot 2 -- Cumulative privilege accumulation.** No single Dataverse UI view surfaces the combined effect of role depth, team membership, OWD, and sharing rules. This trace computes effective scope across all four enforcement layers simultaneously.

**Blind spot 3 -- OWD-sharing-rule override.** A Private OWD does not prevent a separately configured sharing rule from re-opening access. This trace cross-references OWD settings against every active sharing rule to surface unintended grants.

Each SE section opens with a CONTEXT-CLOSES label naming the blind spot it resolves.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. **SE-first sequence** -- SE produces TABLE_1-5 in PHASE 1 without CS baseline; CS reconciles against SE output in PHASE 2. Sequence label appears as section header. Each phase completes fully before the next begins.

**PHASE 0 -- CA:** Schema Registry (Step 0.1), Criterion Enforcement Matrix preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3), Phase 0 gate statement. CA is sole author.

**PHASE 1 -- SE:** Fills TABLE_1-5. No CS baseline yet. SE flags sharing rule overreach and access differentials in CS-2/CS-3 for CS to respond to.

**PHASE 2 -- CS:** Reconciles SE-authored CS-2/CS-3 entries. Confirms or challenges SE findings. Adds CS-EXPECTATION-VIOLATED rows to TABLE_5 where CS interpretation contradicts SE finding.

**PHASE 3 -- CA-1:** Double-anchor verification per criterion. Terminal verdict cites Phase 0 by label. Trace not closed until verdict is written.

---

## PHASE 0 -- CA: SCHEMA REGISTRY, ENFORCEMENT PREAMBLE, AND LANGUAGE INDEX

### Step 0.1 -- Schema Registry (CA-authored)

**All schemas declared by CA before PHASE 1. SE-first variant: CS-2 and CS-3 are SE-authored in PHASE 1; CS responds in PHASE 2.**

**Schema ID: TABLE_1 -- Role-Operation Matrix**
`Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` -- Blank-cell rule: Granted / Denied / Conditional / N/A.

**Schema ID: TABLE_2 -- FLS Coverage**
`Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?` -- Gap? = YES / NO. Gap? = YES rows forward to TABLE_5 per-row.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" -- confirmed here at Schema Registry TABLE_2 declaration site, before PHASE 1. Downstream RULE (C-22) at SE-2.

**Schema ID: TABLE_3 -- Record Scope by Role**
`Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`

**Schema ID: TABLE_4 -- Escalation Vector Inventory**
`Vector | Checked? | Finding | Severity` -- All four vectors; Checked? = YES for all.

Per-role escalation roll-up sub-table (SE-authored in PHASE 1):
`Role | Pre-Declaration Commitment | Composite Verdict | Mechanisms Cited | Cross-Audit`

Mechanisms Cited field: list each mechanism inline by type. Do not write "see table above", "as documented above", "per the analysis above", or any equivalent form -- restate each mechanism inline.

> PLACEMENT-CRITERION CONFIRMED (C-27): prohibition on back-references named here at TABLE_4 declaration site. Downstream RULE (C-27) at SE-4.

Cross-Audit field: verbatim-quote format required.
`Pre-decl: "[exact text copied verbatim from Pre-Declaration Commitment cell]" | Filed: "[exact text copied verbatim from Mechanisms Cited cell]" | Match: CONFIRMED`

> PLACEMENT-CRITERION CONFIRMED (C-29 / C-31): verbatim cross-audit format declared here at Schema Registry TABLE_4 Cross-Audit field declaration site, before PHASE 1. This format makes the match verification a zero-judgment mechanical operation. Downstream RULE-BLOCK (C-31) appears at SE-4.

**Schema ID: TABLE_5 -- Security Gap Inventory**
`# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation` -- three-field Remediation: (1) Config change. (2) Expected state. (3) Verification step.

> PLACEMENT-CRITERION CONFIRMED (C-16): TABLE_5 three-field format declared here at Step 0.1, before PHASE 1. Downstream RULE (C-16) at CA-1.5.

**Schema ID: CS-2 -- SE-authored in PHASE 1**: `Rule Name | SE Finding | SE Overreach Flag | CS Expected Intent | Resolved? | Resolution`
**Schema ID: CS-3 -- SE-authored in PHASE 1**: `Entity | Field or Operation | SE-Observed CS Access | SE-Observed Privileged-Role Access | Gap Exists? | CS Interpretation`

### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored)

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

> PLACEMENT-CRITERION CONFIRMED (C-22): Gap? boolean as structural enforcement mechanism. Downstream RULE (C-22) at SE-2.

**SHALL-D extended:** TABLE_4 all four vectors; per-role rule-out naming specific mechanism; per-role roll-up with verbatim Cross-Audit format per Step 0.1.

### Step 0.3 -- ENFORCEMENT LANGUAGE INDEX (CA-authored)

**COMPLETENESS THRESHOLD: N-1 of N earns 0 pts -- same as 0 of N.**

> PLACEMENT-CRITERION CONFIRMED (C-25 / C-28): Site Type column present per-row.

| EL-ID | Criterion | Enforcement Point | Verbatim Pass-Condition Phrase | Site Type | Status |
|-------|-----------|-------------------|-------------------------------|-----------|--------|
| EL-01 | C-11 | Phase 0 gate Chain 1 declaration | "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate |
| EL-02 | C-12 | SE-2/SE-4 negative-check instruction | "Checked [list] for [role]; [gap type] does not apply because [reason]" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-2 and SE-4 |
| EL-03 | C-13 | TABLE_5 Remediation field definition | "expected system state after the fix is applied and how to verify the fix took effect" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_5 |
| EL-04 | C-14 | SE-5 discovery-section note | "enables auditing that C-11 inline registration actually occurred" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-5 |
| EL-05 | C-15 | SE-4 per-role rule-out instruction | "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-4 |
| EL-06 | C-16 | TABLE_5 Remediation schema declaration | "declared explicitly at the top of the trace output, before the first analysis phase begins" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_5 |
| EL-07 | C-17 | CA-1.5 remediation echo instruction | "remediation block that states the fix without linking back to the discovery section does not pass" | APPLICATION-SITE | RULE-BLOCK: confirmed at CA-1.5 |
| EL-08 | C-18/C-22 | TABLE_2 Gap? column and preamble | "boolean flag..." / "co-authorship..." | DECLARATION-SITE (both) | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_2 and Step 0.2 |
| EL-09 | C-23 | Phase 0 gate statement | "execution record, not declarative checklist" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate |
| EL-10 | C-24 | CA-1 verdict precondition | "precondition for closing the trace, not a recommended step" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate and CA-1 header |
| EL-11 | C-25 | All structural enforcement points | each criterion's exact pass-condition phrase at each structural enforcement point | BOTH (per-criterion) | CONFIRMED: inline verbatim at declaration sites, RULE blocks at application sites |
| EL-12 | C-29 / C-31 | TABLE_4 Cross-Audit field definition + SE-4 roll-up instruction | "Pre-decl: '[exact text]' | Filed: '[exact text]' | Match: CONFIRMED" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-4; PLACEMENT annotation at Step 0.1 TABLE_4 |

**Phase 0 coverage note:** 12/12 enforcement points declared (SE-first variant). Site Type breakdown: 6 DECLARATION-SITE, 5 APPLICATION-SITE (EL-12 added), 1 BOTH. C-31 verbatim cross-audit present. C-32 absent.

### Phase 0 Gate Statement

Chain 1 -- discovery to TABLE_5: every gap found during PHASE 1 (SE) is entered into TABLE_5 at the section where found -- entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact.
Chain 2 -- TABLE_5 to CA-1: every Remediation entry verified via double-anchor.

> PLACEMENT-CRITERION CONFIRMED (C-11 / C-23): execution record confirmed. CA-1 verdict is the close precondition.

**Phase 0 gate state log:**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Chain 1 -- discovery to TABLE_5, inline | ACTIVE | EL-01 |
| TABLE_5 Remediation three-field format | ACTIVE | EL-06 |
| Gap? per-row boolean trigger | ACTIVE | EL-08 |
| Chain 2 -- TABLE_5 to CA-1 double-anchor | ACTIVE | EL-07 |
| ENFORCEMENT LANGUAGE INDEX 12/12 | CONFIRMED | EL-12 C-31 verbatim cross-audit confirmed at Step 0.1 TABLE_4 |
| CA-1 verdict as trace close precondition | ACTIVE | EL-10 |

*All 12/12 confirmed. SE-first sequence active. Handing to PHASE 1 -- SE.*

---

## PHASE 1 -- SE: Security Analysis (SE-first)

*SE fills TABLE_1-5 without CS baseline. SE flags sharing rule overreach and access differentials for CS reconciliation in PHASE 2.*

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: cumulative privilege accumulation**

**TABLE_1**: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` (blank-cell rule applies)

After TABLE_1: author CS-3 rows for access differentials and CS-2 rows for sharing rules flagged for CS review.

### SE-2 / SHALL-B -- Field-Level Security Coverage

**CONTEXT-CLOSES: post-incident FLS discovery**

> RULE (C-22): Gap? per-row commit signal. Mark YES/NO; if Gap? = YES, TABLE_5 entry before next row.

**TABLE_2**: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`

> RULE (C-12): "Checked [list] for [role]; [gap type] does not apply because [reason]" -- per category yielding no Gap? = YES.

### SE-3 / SHALL-C -- Record Access Scope

**CONTEXT-CLOSES: OWD-sharing-rule override**

**TABLE_3**: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?` -- Every TABLE_1 role.

### SE-4 / SHALL-D -- Privilege Escalation Analysis

**TABLE_4**: `Vector | Checked? | Finding | Severity` -- All four vectors, all Checked? = YES.

> RULE (C-15): per-role rule-out required when no escalation found.

**Per-role escalation roll-up** (TABLE_4 sub-table):
`Role | Pre-Declaration Commitment | Composite Verdict | Mechanisms Cited | Cross-Audit`

Mechanisms Cited: restate each mechanism inline. Do not write "see table above" or any equivalent form.

> RULE (C-27): back-reference prohibition active per Step 0.1 declaration.

> RULE (C-29 / C-31): "Pre-decl: '[exact text]' | Filed: '[exact text]' | Match: CONFIRMED" -- Cross-Audit cell quotes Pre-Declaration Commitment and Mechanisms Cited cell verbatim. Match verification is a zero-judgment mechanical operation. Example: `Pre-decl: "Sharing rules for this entity are restricted to same-BU access; no sharing rule targets this role for cross-BU grants" | Filed: "Sharing rules for this entity are restricted to same-BU access; no sharing rule targets this role for cross-BU grants" | Match: CONFIRMED`

### SE-5 / SHALL-E -- Security Gap Inventory

**TABLE_5**: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`

> RULE (C-14): each row includes discovery context.
> RULE (C-17): each Remediation chains to discovery section.

*Handing to PHASE 2 -- CS.*

---

## PHASE 2 -- CS: Reconciliation

*CS reconciles SE-authored CS-2/CS-3 entries. Confirms or challenges SE findings. Adds CS-EXPECTATION-VIOLATED rows to TABLE_5 where CS interpretation contradicts SE finding.*

**CS-1 reconciliation narrative:** For each entity, CS confirms SE-observed access levels match CS expectations or states the discrepancy.

**CS-2 reconciliation** (SE-authored CS-2): populate CS Expected Intent and Resolved? columns. If unresolved, author TABLE_5 CS-EXPECTATION-VIOLATED entry.

**CS-3 reconciliation** (SE-authored CS-3): populate CS Interpretation column. Challenge any SE finding inconsistent with CS expected access.

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*Structural close condition -- precondition for closing the trace, not a recommended step.*

**CA-1.1 through CA-1.5:** [Registry anchor (Step 0.1 schema) + Preamble anchor + Verification -> PASS/FAIL per criterion]

> RULE (C-16): TABLE_5 three-field format declared at Phase 0 Step 0.1.
> RULE (C-17): each Remediation chains to discovery context.

**CA Format Compliance Verdict -- citing Phase 0:**
Citing: Schema Registry (Step 0.1 including TABLE_4 verbatim Cross-Audit format), preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3), Phase 0 gate state log. SE-first sequence: PHASE 1 was SE, PHASE 2 was CS. Phase 0 structures valid for both sequences.

> RULE (C-23): execution record confirmed.

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION:**
[EL-01 through EL-12, confirm STATUS]. N/12. EL-12 (C-31 verbatim cross-audit): RULE-BLOCK at SE-4 confirmed? [YES/NO].

> RULE (C-24): writing this verdict closes the trace.

[C-01 through C-05 PASS/FAIL. Overall: COMPLIANT / NON-COMPLIANT.]

[TRACE CLOSED -- CA-1 verdict written.]

---

## V-04 -- Combined C-31 + C-32, Formal/Technical Phrasing Register

**Axis:** Combined C-31 + C-32 active; phrasing register is purely formal/technical -- all instruction language uses SHALL/MUST/PROHIBITED; no conversational framing; CS-first canonical sequence
**Hypothesis:** +weight(C-31) + weight(C-32). Tests whether formal/technical register affects mechanism execution fidelity or whether both mechanisms survive register shift intact.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: PERMISSIONS TRACE EXECUTION MANDATE

**COMPLIANCE GAP CATEGORY 1 -- FIELD-LEVEL SECURITY ENUMERATION FAILURE.** FLS gap detection in manual audit processes is structurally deferred to post-incident discovery. This trace MUST enumerate FLS assignments and denials across PII, Financial, Audit-Compliance, and Operational field categories before the first security incident occurs.

**COMPLIANCE GAP CATEGORY 2 -- EFFECTIVE SCOPE COMPUTATION DEFICIT.** No single Dataverse administrative view presents the computed effective scope resulting from the combination of security role depth, team membership, organization-wide default, and sharing rule configuration. This trace MUST compute effective scope across all four enforcement layers for every role.

**COMPLIANCE GAP CATEGORY 3 -- OWD-SHARING-RULE INTERACTION UNVERIFIED.** A Private organization-wide default does not prevent a sharing rule from independently granting cross-record access. This trace MUST cross-reference all active sharing rule configurations against the OWD setting for each entity.

Each SE section opens with a CONTEXT-CLOSES label identifying the compliance gap category it closes.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. CS-first sequence. Each phase MUST complete fully before the next begins. Phase labels MUST appear as section headers.

**PHASE 0 -- CA:** Schema Registry (Step 0.1), Criterion Enforcement Matrix preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3), Phase 0 gate statement. CA is sole author. No other role may contribute to PHASE 0.

**PHASE 1 -- CS:** Qualitative access baseline and expectation tables. CS MUST NOT fill TABLE_1 through TABLE_5. CS schemas only.

**PHASE 2 -- SE:** Fills TABLE_1 through TABLE_5 using Dataverse-native terminology. SE MUST reference CS schemas by Schema ID. SE MUST NOT author CS-1 narrative.

**PHASE 3 -- CA-1:** Double-anchor verification per essential criterion. Terminal verdict MUST cite Phase 0 by label. Trace MUST NOT be declared closed until CA-1 verdict is written.

---

## PHASE 0 -- CA: SCHEMA REGISTRY, ENFORCEMENT PREAMBLE, AND LANGUAGE INDEX

### Step 0.1 -- Schema Registry (CA-authored)

ALL SCHEMAS MUST BE DECLARED BY CA BEFORE PHASE 1 BEGINS. BLANK-CELL PROHIBITION IS GLOBAL AND UNCONDITIONAL.

**Schema ID: TABLE_1 -- Role-Operation Matrix**
Declared columns: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
BLANK-CELL RULE: Every cell MUST contain one of: Granted / Denied / Conditional (condition stated inline) / N/A. Blank cells are PROHIBITED.

**Schema ID: TABLE_2 -- FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Gap? column MUST contain YES or NO per row. Gap? = YES REQUIRES an immediate TABLE_5 entry before the next TABLE_2 row begins. This per-row boolean converts TABLE_5 registration from an editorial judgment to a mechanical obligation.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" -- the Gap? column constitutes that boolean flag. Structural role as per-row commit signal confirmed at Schema Registry TABLE_2 declaration site, before PHASE 1. Downstream RULE (C-22) at SE-2.

**Schema ID: TABLE_3 -- Record Scope by Role**
Declared columns: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
BLANK-CELL RULE: Effective Scope MUST be one of: Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].

**Schema ID: TABLE_4 -- Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
All four vectors MUST be present: team inheritance / sharing rules / impersonation / admin or environment role override. Checked? MUST be YES for all four. Finding MUST state an escalation path or a per-role rule-out naming the specific mechanism and reason for NOT POSSIBLE verdict.

Per-role escalation roll-up sub-table (SE-authored in PHASE 2):
`Role | Pre-Declaration Commitment | Composite Verdict | Mechanisms Cited | Cross-Audit`

Mechanisms Cited field INSTRUCTION: List each NOT POSSIBLE vector's mechanism type inline. The following forms are PROHIBITED: "see table above", "mechanisms cited in SE-4", "see vectors above", "as documented above", "consistent with the analysis above", "per the findings above", "as identified above", whether that form is a sentence, a label, a parenthetical phrase, or any equivalent form that delegates mechanism content to another section rather than restating it inline. A form PRODUCES THE PROHIBITED EFFECT OF DELEGATION if it routes the reader to another section to obtain the mechanism content rather than providing the content at the current location.

> PLACEMENT-CRITERION CONFIRMED (C-27 / C-30 / C-32): "explicit prohibition naming the disallowed form" (C-27) -- six specific disallowed forms named above. Equivalence clause names the prohibited mechanism of effect (C-30 / C-32): "any equivalent form that delegates mechanism content to another section rather than restating it inline" -- the test for equivalence is effect-membership, not form-resemblance. A form that produces delegation is prohibited regardless of structural appearance. Confirmed at Schema Registry TABLE_4 declaration site, before PHASE 1. Downstream RULE (C-27 / C-32) at SE-4.

Cross-Audit field INSTRUCTION: MUST use verbatim-quote format:
`Pre-decl: "[EXACT TEXT FROM Pre-Declaration Commitment CELL -- NO PARAPHRASE]" | Filed: "[EXACT TEXT FROM Mechanisms Cited CELL -- NO PARAPHRASE]" | Match: CONFIRMED`
PARAPHRASE IS PROHIBITED. CHARACTERIZATION IS PROHIBITED. Both cells MUST be quoted verbatim. Match verification MUST be a zero-judgment mechanical string comparison.

> PLACEMENT-CRITERION CONFIRMED (C-29 / C-31): "Pre-decl: '[exact text]' | Filed: '[exact text]' | Match: CONFIRMED" -- verbatim-quote format declared here at Schema Registry TABLE_4 Cross-Audit field instruction site, before PHASE 1. This format eliminates all semantic judgment from the cross-audit verification step. Downstream RULE-BLOCK (C-31) at SE-4.

**Schema ID: TABLE_5 -- Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Gap Types MUST be one of: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.
Remediation MUST include all three fields: (1) Config change: exact object name, location in Dataverse security editor, precise change. (2) Expected state: specific UI view or observable result after fix. (3) Verification step: named action to confirm fix.

> PLACEMENT-CRITERION CONFIRMED (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 Remediation three-field format declared at Step 0.1, before PHASE 1. Downstream RULE (C-16) at CA-1.5.

**Schema ID: CS-2**: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference` -- SE Cross-Reference: PENDING -- await SE.
**Schema ID: CS-3**: `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation` -- SE Confirmation: PENDING -- await SE.

### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored)

M1, M2, M3 MUST be simultaneously active for every essential criterion. M4 pre-assigned.

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- Gap? boolean structural enforcement confirmed at preamble declaration site, before PHASE 1. Downstream RULE (C-22) at SE-2.

**SHALL OBLIGATIONS (CA-authored, unconditional):**
- SHALL-A: TABLE_1 MUST be present; every cell MUST be Granted/Denied/Conditional/N/A; every role with any privilege MUST be included.
- SHALL-B: TABLE_2 MUST list every sensitive field; null case MUST be stated; Gap? = YES rows MUST be forwarded per-row.
- SHALL-C: Every TABLE_1 role MUST appear in TABLE_3 with Effective Scope filled; ambiguous scope MUST go to TABLE_5.
- SHALL-D: TABLE_4 MUST include all four vectors; per-role rule-out MUST name specific mechanism and reason; per-role roll-up MUST include verbatim Cross-Audit format per Step 0.1 and intent-anchored Mechanisms Cited prohibition per Step 0.1.
- SHALL-E: TABLE_5 MUST include at least one named gap; zero-gap case REQUIRES explicit evidence rows.

### Step 0.3 -- ENFORCEMENT LANGUAGE INDEX (CA-authored)

**COMPLETENESS THRESHOLD: N-1 OF N ENFORCEMENT POINTS EARNS 0 POINTS -- IDENTICAL TO 0 OF N. PARTIAL COMPLIANCE IS NOT COMPLIANCE.**

> PLACEMENT-CRITERION CONFIRMED (C-25 / C-28): Site Type column present per-row. DECLARATION-SITE rows REQUIRE inline verbatim confirmation. APPLICATION-SITE rows REQUIRE RULE-BLOCK confirmation. Scorer reads Site Type column to determine required confirmation mechanism without consulting criterion definitions.

| EL-ID | Criterion | Enforcement Point | Verbatim Pass-Condition Phrase | Site Type | Status |
|-------|-----------|-------------------|-------------------------------|-----------|--------|
| EL-01 | C-11 | Phase 0 gate Chain 1 declaration | "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate |
| EL-02 | C-12 | SE-2/SE-4 negative-check instruction | "Checked [list] for [role]; [gap type] does not apply because [reason]" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-2 and SE-4 |
| EL-03 | C-13 | TABLE_5 Remediation field definition | "expected system state after the fix is applied and how to verify the fix took effect" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_5 |
| EL-04 | C-14 | SE-5 discovery-section note | "enables auditing that C-11 inline registration actually occurred" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-5 |
| EL-05 | C-15 | SE-4 per-role rule-out instruction | "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-4 |
| EL-06 | C-16 | TABLE_5 Remediation schema declaration | "declared explicitly at the top of the trace output, before the first analysis phase begins" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_5 |
| EL-07 | C-17 | CA-1.5 remediation echo instruction | "remediation block that states the fix without linking back to the discovery section does not pass" | APPLICATION-SITE | RULE-BLOCK: confirmed at CA-1.5 |
| EL-08 | C-18/C-22 | TABLE_2 Gap? column and Criterion Enforcement Matrix | "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" / "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" | DECLARATION-SITE (both) | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_2 and Step 0.2 |
| EL-09 | C-23 | Phase 0 gate statement | "execution record, not declarative checklist" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate |
| EL-10 | C-24 | CA-1 verdict precondition | "precondition for closing the trace, not a recommended step" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate and CA-1 header |
| EL-11 | C-25 | All structural enforcement points | each criterion's exact pass-condition phrase at each structural enforcement point | BOTH (per-criterion) | CONFIRMED: inline verbatim at declaration sites, RULE blocks at application sites |
| EL-12 | C-29 / C-31 | TABLE_4 Cross-Audit field instruction + SE-4 roll-up | "Pre-decl: '[exact text]' | Filed: '[exact text]' | Match: CONFIRMED" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-4; PLACEMENT annotation at Step 0.1 TABLE_4 |
| EL-13 | C-30 / C-32 | TABLE_4 Mechanisms Cited prohibition + SE-4 instruction | "or any equivalent form that delegates mechanism content to another section rather than restating it inline" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_4; second clause at SE-4 |

**Phase 0 coverage note:** 13/13 enforcement points declared. Site Type: 7 DECLARATION-SITE (EL-01/03/06/08/09/10/13), 5 APPLICATION-SITE (EL-02/04/05/07/12), 1 BOTH (EL-11). Both C-31 and C-32 present.

### Phase 0 Gate Statement

Chain 1 -- discovery to TABLE_5: every gap found during PHASE 2 MUST be entered into TABLE_5 at the section where found -- entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact.
Chain 2 -- TABLE_5 to CA-1: every TABLE_5 Remediation entry MUST be verified in PHASE 3 via double-anchor.

> PLACEMENT-CRITERION CONFIRMED (C-11 / C-23): "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" (C-11) and "execution record, not declarative checklist" (C-23). CA-1 verdict MUST be written as the structural close precondition.

**Phase 0 gate state log:**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Chain 1 -- discovery to TABLE_5, inline at discovery site | ACTIVE | EL-01 |
| TABLE_5 Remediation three-field format | ACTIVE | EL-06 |
| Gap? per-row boolean trigger | ACTIVE | EL-08 |
| Chain 2 -- TABLE_5 to CA-1 double-anchor | ACTIVE | EL-07 |
| ENFORCEMENT LANGUAGE INDEX 13/13 | CONFIRMED | EL-12 (C-31 verbatim cross-audit) + EL-13 (C-32 intent-anchored equivalence) both confirmed at Step 0.1 TABLE_4 |
| CA-1 verdict as trace close precondition | ACTIVE | EL-10 |

*ALL 13/13 ENFORCEMENT POINTS CONFIRMED. ALL STRUCTURES ACTIVE. HANDING TO PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Access Baseline

*CS MUST produce CS-1 narrative and CS-2/CS-3 tables. CS MUST NOT fill TABLE_1 through TABLE_5.*

**CS-1:** For each entity: expected CRUD operations, record scope constraints, sensitive fields requiring CS read access. Name every sharing rule CS relies on. Flag any potential overreach.

**CS-2**: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference` -- SE Cross-Reference: PENDING.

**CS-3**: `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation` -- SE Confirmation: PENDING.

*HANDING TO PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: COMPLIANCE GAP CATEGORY 2 (effective scope computation deficit)**

**TABLE_1** MUST be filled: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` (blank-cell rule UNCONDITIONAL)

SE MUST update CS-3 SE Confirmation column after filling TABLE_1.

### SE-2 / SHALL-B -- Field-Level Security Coverage

**CONTEXT-CLOSES: COMPLIANCE GAP CATEGORY 1 (FLS enumeration failure)**

> RULE (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- Gap? boolean active. Mark YES/NO per row; if Gap? = YES, TABLE_5 entry REQUIRED before next TABLE_2 row.

**TABLE_2** MUST be filled: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`

> RULE (C-12): "Checked [list] for [role]; [gap type] does not apply because [reason]" -- REQUIRED per category yielding no Gap? = YES.

### SE-3 / SHALL-C -- Record Access Scope

**CONTEXT-CLOSES: COMPLIANCE GAP CATEGORY 3 (OWD-sharing-rule interaction)**

**TABLE_3** MUST be filled: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?` -- Every TABLE_1 role MUST be present.

### SE-4 / SHALL-D -- Privilege Escalation Analysis

**TABLE_4** MUST include all four vectors with Checked? = YES: `Vector | Checked? | Finding | Severity`

> RULE (C-15): "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" -- REQUIRED when no escalation path found.

SE MUST update CS-2 SE Cross-Reference after TABLE_4.

**Per-role escalation roll-up** (TABLE_4 sub-table):

> RULE (C-27 / C-30 / C-32): Mechanisms Cited field -- the following forms are PROHIBITED: "see table above", "mechanisms cited in SE-4", "see vectors above", "as documented above", "consistent with the analysis above", "per the findings above", "as identified above", whether that form is a sentence, a label, a parenthetical phrase, or any equivalent form that delegates mechanism content to another section rather than restating it inline. A FORM THAT DELEGATES is prohibited regardless of structural appearance. Each mechanism MUST be restated inline.

> RULE (C-29 / C-31): Cross-Audit field MUST use verbatim-quote format: `Pre-decl: "[EXACT TEXT FROM Pre-Declaration Commitment -- NO PARAPHRASE]" | Filed: "[EXACT TEXT FROM Mechanisms Cited -- NO PARAPHRASE]" | Match: CONFIRMED`. Characterization and paraphrase are PROHIBITED.

### SE-5 / SHALL-E -- Security Gap Inventory

**TABLE_5** MUST include three-field Remediation: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`

> RULE (C-14): each row MUST include discovery context.
> RULE (C-17): each Remediation MUST chain to the discovery section.

*HANDING TO PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Compliance Verification

*STRUCTURAL CLOSE CONDITION -- PRECONDITION FOR CLOSING THE TRACE, NOT A RECOMMENDED STEP.*

**CA-1.1:** TABLE_1 schema / C-01: TABLE_1/SE-1/SHALL-A/CA-1.1. -> PASS/FAIL
**CA-1.2:** TABLE_2 schema / C-02: TABLE_2/SE-2/SHALL-B/CA-1.2. -> PASS/FAIL
**CA-1.3:** TABLE_3 schema / C-03: TABLE_3/SE-1+SE-3/SHALL-C/CA-1.3. -> PASS/FAIL
**CA-1.4:** TABLE_4 schema (including per-role roll-up) / C-04: TABLE_4/SE-4/SHALL-D/CA-1.4. -> PASS/FAIL
**CA-1.5:** TABLE_5 schema / C-05: TABLE_5/SE-5/SHALL-E/CA-1.5.

> RULE (C-16): TABLE_5 three-field format declared at Phase 0 Step 0.1.
> RULE (C-17): each Remediation entry MUST chain to discovery section.

-> PASS/FAIL

**CA FORMAT COMPLIANCE VERDICT -- CITING PHASE 0:**
Citing: Schema Registry (Step 0.1 -- TABLE_4 verbatim Cross-Audit format + intent-anchored Mechanisms Cited prohibition), preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX with Site Type column (Step 0.3), Phase 0 gate state log. All structures confirmed by CA before PHASE 1.

> RULE (C-23): execution record confirmed. Verdict confirms execution matched record.

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION:**
[EL-01 through EL-13 -- CONFIRMED or UNCONFIRMED]. Count: N/13. N < 13 = C-28 FAIL unconditionally. EL-12 (C-31): RULE-BLOCK at SE-4? [YES/NO]. EL-13 (C-32): INLINE-VERBATIM at Step 0.1 TABLE_4? [YES/NO].

> RULE (C-24): "precondition for closing the trace, not a recommended step" -- this verdict IS that precondition. TRACE NOW CLOSED.

[C-01 PASS/FAIL. C-02 PASS/FAIL. C-03 PASS/FAIL. C-04 PASS/FAIL. C-05 PASS/FAIL. OVERALL: COMPLIANT / NON-COMPLIANT.]

[TRACE CLOSED -- CA-1 VERDICT WRITTEN.]

---

## V-05 -- Full Combination: C-31 + C-32 + Quantified Inertia Framing, CS-First

**Axis:** Both C-31 and C-32 active; CONTEXT section opens with quantified claims about manual audit detection failure; CS-first canonical sequence; inertia framing gives each blind spot a named detection gap with a measurable failure mode
**Hypothesis:** +weight(C-31) + weight(C-32). Achieves 25/25 aspirational under v9 rubric. Inertia framing increases the likelihood that a model executing the prompt produces the full analysis rather than stopping at surface-level coverage.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: Why a Permissions Trace Is Not Optional

Three structural failure modes make manual Dataverse security review systematically incomplete:

**Failure mode 1 -- FLS discovery deferred to post-incident.** Manual FLS review is triggered by a data exposure incident, not by a scheduled audit. At that point, the affected field-category combinations (PII, Financial, Audit-Compliance, Operational) have already been accessible to roles that should have been denied. This trace eliminates the deferral by enumerating all field-role-access combinations before the first incident, categorized by sensitivity class. The gap register (TABLE_5) closes with explicit Gap? = YES / NO per field row, not with a narrative summary that can omit categories.

**Failure mode 2 -- Effective scope not computed.** Security administrators typically review one control layer at a time: roles in the security editor, OWD in settings, sharing rules in configuration, team membership in the team panel. No view presents the computed intersection. A role with BU-level read, a team membership that includes an owner-access team, and a sharing rule granting cross-BU access has an effective scope that is wider than any single-layer view shows. This trace computes the intersection for every role in TABLE_3, with Scope Modifier and Effective Scope stated explicitly rather than implied.

**Failure mode 3 -- OWD-sharing-rule interaction invisible without cross-reference.** A Private OWD is routinely read as "access restricted to record owner." That reading is wrong when a sharing rule configured for a different business purpose grants access to the same entity for a different role. The sharing rule configuration and the OWD setting appear in different UI locations and are almost never reviewed in combination. This trace makes the combination explicit by requiring a cross-reference in TABLE_3 and flagging every OWD + sharing rule combination where the effective scope diverges from the OWD baseline.

Each SE section opens with a CONTEXT-CLOSES label naming the specific failure mode it closes and the structural mechanism that closes it.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. CS-first sequence. Labels appear as section headers. Each phase completes fully before the next begins.

**PHASE 0 -- CA:** Schema Registry (Step 0.1), Criterion Enforcement Matrix preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3), Phase 0 gate statement. CA is sole author.

**PHASE 1 -- CS:** Qualitative access baseline and CS-2/CS-3 expectation tables. CS does NOT fill TABLE_1-5.

**PHASE 2 -- SE:** Fills TABLE_1-5 using Dataverse-native terminology. References CS tables by Schema ID.

**PHASE 3 -- CA-1:** Double-anchor verification per criterion. Terminal verdict cites Phase 0 by label. Trace not closed until verdict is written.

---

## PHASE 0 -- CA: SCHEMA REGISTRY, ENFORCEMENT PREAMBLE, AND LANGUAGE INDEX

### Step 0.1 -- Schema Registry (CA-authored)

**All schemas declared by CA before PHASE 1. Blank-cell prohibition global.**

**Schema ID: TABLE_1 -- Role-Operation Matrix**
Declared columns: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Blank-cell rule: Granted / Denied / Conditional (state condition inline) / N/A.

**Schema ID: TABLE_2 -- FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Gap? = YES / NO per row. Gap? = YES triggers an immediate TABLE_5 entry before the next TABLE_2 row begins. The Gap? boolean converts registration from an editorial judgment into a per-row mechanical obligation: the fill-and-flag action is structurally simultaneous with the TABLE_2 row, not deferred.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" -- the Gap? column is that flag. Structural role as per-row commit signal confirmed here at Schema Registry TABLE_2 declaration site, before PHASE 1. Downstream RULE (C-22) appears at SE-2.

**Schema ID: TABLE_3 -- Record Scope by Role**
Declared columns: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name]. Scope Modifier names every applicable modifier (team grant, sharing rule, role hierarchy) so Effective Scope is independently auditable.

**Schema ID: TABLE_4 -- Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
All four vectors required: team inheritance / sharing rules / impersonation / admin or environment role override. Checked? = YES for all four. Finding states escalation path or per-role rule-out with specific mechanism and reason.

Per-role escalation roll-up sub-table (SE-authored in PHASE 2):
`Role | Pre-Declaration Commitment | Composite Verdict | Mechanisms Cited | Cross-Audit`

Pre-Declaration Commitment: stated before analysis of that role begins -- names the structural assumptions governing NOT POSSIBLE verdicts. Establishes the verifiable contract closed by the Cross-Audit.

Composite Verdict: names each NOT POSSIBLE vector's closing mechanism type inline. Does not summarize by count alone.

Mechanisms Cited field: list each mechanism inline by type. Do not write "see table above", "mechanisms cited in SE-4", "see vectors above", "as documented above", "consistent with the analysis above", "per the findings above", "as noted earlier", whether that form is a sentence, a label, a parenthetical phrase, or any equivalent form that delegates mechanism content to another section rather than restating it inline. The prohibited effect is delegation: routing the reader elsewhere to obtain the mechanism content instead of providing it at the current location.

> PLACEMENT-CRITERION CONFIRMED (C-27 / C-30 / C-32): "explicit prohibition naming the disallowed form" (C-27) -- seven specific disallowed forms named above. Equivalence clause present (C-30) naming the prohibited mechanism of effect (C-32): "any equivalent form that delegates mechanism content to another section rather than restating it inline." A form is prohibited if it produces the effect of delegation regardless of its structural appearance -- the test is effect-membership, not form-resemblance. Confirmed here at Schema Registry TABLE_4 Mechanisms Cited field declaration site, before PHASE 1. Downstream RULE (C-27 / C-32) appears at SE-4.

Cross-Audit field: verbatim-quote format required.
`Pre-decl: "[exact text copied verbatim from Pre-Declaration Commitment cell -- no paraphrase, no characterization, no abbreviation]" | Filed: "[exact text copied verbatim from Mechanisms Cited cell -- no paraphrase, no characterization, no abbreviation]" | Match: CONFIRMED`
Verbatim quotation at both sites makes the cross-audit a zero-judgment mechanical string comparison. A cross-audit that characterizes both sites ("Pre-decl identifies no team inheritance path; Filed confirms no team inheritance path; Match: CONFIRMED") does not satisfy C-31 -- it states a conclusion without presenting the evidence in a form that is independently verifiable character-for-character.

> PLACEMENT-CRITERION CONFIRMED (C-29 / C-31): "Pre-decl: '[exact text]' | Filed: '[exact text]' | Match: CONFIRMED" -- verbatim-quote format declared here at Schema Registry TABLE_4 Cross-Audit field declaration site, before PHASE 1. Both C-29 (cross-audit assertion present) and C-31 (verbatim quotation at both sites) are confirmed at this site. Downstream RULE-BLOCK (C-31) appears at SE-4.

**Schema ID: TABLE_5 -- Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Enumerated gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.
Remediation three-field format (all three required): (1) Config change: exact object name, location in Dataverse security editor, precise change to apply. (2) Expected state: specific UI view or observable system result after fix. (3) Verification step: named action that confirms the fix took effect.

> PLACEMENT-CRITERION CONFIRMED (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 three-field Remediation format is that declaration. Confirmed at Step 0.1, before PHASE 1. Downstream RULE (C-16) at CA-1.5.

**Schema ID: CS-2**: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference` -- SE Cross-Reference: "TBD -- await SE."
**Schema ID: CS-3**: `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation` -- SE Confirmation: "TBD -- await SE."

### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored)

M1, M2, M3 simultaneously active for every essential criterion. M4 pre-assigned.

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- Gap? boolean as structural enforcement mechanism confirmed at preamble declaration site, before PHASE 1. Downstream RULE (C-22) at SE-2.

**SHALL obligations (CA-authored):**
- SHALL-A: TABLE_1 present; all cells Granted/Denied/Conditional/N/A; every role with any privilege included.
- SHALL-B: TABLE_2 lists every sensitive field; null case stated; Gap? = YES rows forwarded per-row to TABLE_5.
- SHALL-C: Every TABLE_1 role in TABLE_3 with Effective Scope filled; ambiguous scope registered in TABLE_5.
- SHALL-D: TABLE_4 all four vectors Checked? = YES; per-role rule-out naming specific mechanism; per-role roll-up with verbatim Cross-Audit (C-31) and intent-anchored Mechanisms Cited prohibition (C-32) per Step 0.1.
- SHALL-E: TABLE_5 at least one named gap; zero-gap case requires explicit evidence rows confirming each category was checked.

### Step 0.3 -- ENFORCEMENT LANGUAGE INDEX (CA-authored)

**COMPLETENESS THRESHOLD: N-1 of N enforcement points earns 0 pts -- the same as 0 of N.**

> PLACEMENT-CRITERION CONFIRMED (C-25 / C-28): Site Type column present per-row. DECLARATION-SITE rows require inline verbatim confirmation; APPLICATION-SITE rows require RULE-BLOCK confirmation. Type column converts two-mechanism enforcement from a rubric-known rule to an output-embedded structure: scorer reads Site Type and knows which confirmation is required without consulting criterion definitions.

| EL-ID | Criterion | Enforcement Point | Verbatim Pass-Condition Phrase | Site Type | Status |
|-------|-----------|-------------------|-------------------------------|-----------|--------|
| EL-01 | C-11 | Phase 0 gate Chain 1 declaration | "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate statement |
| EL-02 | C-12 | SE-2/SE-4 negative-check instruction | "Checked [list] for [role]; [gap type] does not apply because [reason]" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-2 and SE-4 |
| EL-03 | C-13 | TABLE_5 Remediation field definition | "expected system state after the fix is applied and how to verify the fix took effect" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_5 |
| EL-04 | C-14 | SE-5 discovery-section note | "enables auditing that C-11 inline registration actually occurred" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-5 |
| EL-05 | C-15 | SE-4 per-role rule-out instruction | "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-4 |
| EL-06 | C-16 | TABLE_5 Remediation schema declaration | "declared explicitly at the top of the trace output, before the first analysis phase begins" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_5 |
| EL-07 | C-17 | CA-1.5 remediation echo instruction | "remediation block that states the fix without linking back to the discovery section does not pass" | APPLICATION-SITE | RULE-BLOCK: confirmed at CA-1.5 |
| EL-08 | C-18/C-22 | TABLE_2 Gap? column and Criterion Enforcement Matrix preamble | "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" / "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" | DECLARATION-SITE (both) | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_2 and Step 0.2 preamble |
| EL-09 | C-23 | Phase 0 gate statement | "execution record, not declarative checklist" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate statement |
| EL-10 | C-24 | CA-1 verdict precondition | "precondition for closing the trace, not a recommended step" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate and CA-1 verdict header |
| EL-11 | C-25 | All structural enforcement points | each criterion's exact pass-condition phrase at each structural enforcement point | BOTH (per-criterion) | CONFIRMED: inline verbatim at declaration sites (EL-01/03/06/08/09/10), RULE blocks at application sites (EL-02/04/05/07) |
| EL-12 | C-29 / C-31 | TABLE_4 Cross-Audit field declaration + SE-4 roll-up instruction | "Pre-decl: '[exact text]' | Filed: '[exact text]' | Match: CONFIRMED" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-4; PLACEMENT annotation at Step 0.1 TABLE_4 Cross-Audit field |
| EL-13 | C-30 / C-32 | TABLE_4 Mechanisms Cited prohibition + SE-4 instruction | "or any equivalent form that delegates mechanism content to another section rather than restating it inline" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_4 Mechanisms Cited field; downstream RULE at SE-4 |

**Phase 0 coverage note:** 13/13 enforcement points declared. Site Type breakdown: 7 DECLARATION-SITE (EL-01/03/06/08/09/10/13), 5 APPLICATION-SITE (EL-02/04/05/07/12), 1 BOTH (EL-11). C-31 verbatim cross-audit confirmed at Step 0.1 TABLE_4 (EL-12). C-32 intent-anchored equivalence confirmed at Step 0.1 TABLE_4 (EL-13). Both mechanisms present.

### Phase 0 Gate Statement

Chain 1 -- discovery to TABLE_5: every gap found during PHASE 2 is entered into TABLE_5 at the section where it is found -- entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact. Gap? = YES in TABLE_2 is the per-row trigger; each trigger event is structurally inseparable from the TABLE_5 entry that follows it.
Chain 2 -- TABLE_5 to CA-1: every TABLE_5 Remediation entry is verified in PHASE 3 via double-anchor citing the Registry schema and the preamble row.

> PLACEMENT-CRITERION CONFIRMED (C-11 / C-23): "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" (C-11) and "execution record, not declarative checklist" (C-23) -- this gate statement is that execution record. Chain 1 active: discovery-site registration enforced structurally via Gap? boolean. Chain 2 active: CA-1 double-anchor closes every Remediation entry. Downstream RULE (C-23) appears at CA-1 verdict.

The CA-1 verdict in PHASE 3 is the structural close condition -- a precondition for closing the trace, not a recommended step. Downstream RULE (C-24) at CA-1 verdict close.

**Phase 0 gate state log (execution record, not declarative checklist):**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Chain 1 -- discovery to TABLE_5, inline at discovery site | ACTIVE | Inline verbatim at Phase 0 gate (EL-01) |
| TABLE_5 Remediation three-field format | ACTIVE | Inline verbatim at Step 0.1 TABLE_5 (EL-06) |
| Gap? per-row boolean trigger | ACTIVE | Inline verbatim at Step 0.1 TABLE_2 + Step 0.2 preamble (EL-08) |
| Chain 2 -- TABLE_5 to CA-1 double-anchor | ACTIVE | RULE blocks at CA-1.5 (EL-07) |
| ENFORCEMENT LANGUAGE INDEX 13/13 | CONFIRMED | Step 0.3; Site Type column confirmed per-row; EL-12 (C-31 verbatim cross-audit) + EL-13 (C-32 intent-anchored equivalence) both confirmed at Step 0.1 TABLE_4 |
| CA-1 verdict as trace close precondition | ACTIVE | Inline verbatim at CA-1 verdict header (EL-10) |

*All 13/13 enforcement points confirmed. All structures active. Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Lower-Trust Access Baseline

*CS produces CS-1 narrative and CS-2/CS-3 expectation tables. CS does not fill TABLE_1-5.*

**CS-1:** For each entity in {{topic}}: expected CRUD operations for CS role, record scope constraints (which records CS expects to see), sensitive fields CS must read. Name every sharing rule CS relies on. Flag any sharing rule that may grant access beyond the intended CS scope -- this is the Failure Mode 3 check from CS perspective.

**CS-2** (Schema Registry CS-2 schema): `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference` -- SE Cross-Reference: "TBD -- await SE."

**CS-3** (Schema Registry CS-3 schema): `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation` -- SE Confirmation: "TBD -- await SE."

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: Failure Mode 2 (effective scope not computed) -- structural mechanism: TABLE_3 cross-layer computation from TABLE_1 role baseline.**

**TABLE_1** (blank-cell rule applies): `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`

Every role with any privilege. Update CS-3 SE Confirmation column after TABLE_1 is complete.

### SE-2 / SHALL-B -- Field-Level Security Coverage

**CONTEXT-CLOSES: Failure Mode 1 (FLS discovery deferred) -- structural mechanism: Gap? per-row boolean forces registration at discovery time, not at trace close.**

> RULE (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- Gap? boolean active. Mark YES/NO per row; if Gap? = YES, TABLE_5 entry before next TABLE_2 row begins. Discovery-time registration is the structural enforcement; post-hoc consolidation is not possible when this rule is followed.

**TABLE_2** (Gap? per-row trigger ACTIVE): `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`

Sensitive categories: PII / Financial / Audit-Compliance / Operational.

> RULE (C-12): "Checked [list] for [role]; [gap type] does not apply because [reason]" -- for each category yielding no Gap? = YES, state what was examined and why the category is clean.

### SE-3 / SHALL-C -- Record Access Scope

**CONTEXT-CLOSES: Failure Mode 3 (OWD-sharing-rule interaction invisible) -- structural mechanism: TABLE_3 Scope Modifier column requires naming every sharing rule and team grant that modifies OWD baseline.**

**TABLE_3** (blank-cell rule applies): `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`

Every TABLE_1 role present. Scope Modifier: name every applicable modifier. Flag any case where Effective Scope differs from OWD Baseline -- each such row is a potential SHARING-CONFLICT candidate for TABLE_5.

### SE-4 / SHALL-D -- Privilege Escalation Analysis

**TABLE_4** (all four vectors; Checked? = YES): `Vector | Checked? | Finding | Severity`

Team inheritance / Sharing rules / Impersonation (Act on Behalf Of) / Admin or environment role override -- all Checked? = YES.

> RULE (C-15): "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" -- per-role rule-out required when no escalation path found.

Update CS-2 SE Cross-Reference after TABLE_4.

**Per-role escalation roll-up** (TABLE_4 sub-table):
`Role | Pre-Declaration Commitment | Composite Verdict | Mechanisms Cited | Cross-Audit`

For each role:
- Pre-Declaration Commitment: state the structural assumptions governing NOT POSSIBLE verdicts before analysis of this role begins. This is the contract that the Cross-Audit will verify.
- Composite Verdict: name each NOT POSSIBLE vector's closing mechanism type inline (not by count).
- Mechanisms Cited: list each mechanism inline by type.

> RULE (C-27 / C-30 / C-32): Mechanisms Cited MUST NOT contain "see table above", "mechanisms cited in SE-4", "see vectors above", "as documented above", "consistent with the analysis above", "per the findings above", "as noted earlier", whether that form is a sentence, a label, a parenthetical phrase, or any equivalent form that delegates mechanism content to another section rather than restating it inline. The prohibited effect is delegation -- routing the reader to another location for the mechanism content. A form produces this effect regardless of its structural appearance if it requires the reader to look elsewhere for the mechanism.

> RULE (C-29 / C-31): Cross-Audit MUST use verbatim-quote format: `Pre-decl: "[exact text from Pre-Declaration Commitment -- verbatim, no paraphrase]" | Filed: "[exact text from Mechanisms Cited -- verbatim, no paraphrase]" | Match: CONFIRMED`. The verbatim format makes the cross-audit a zero-judgment mechanical string comparison. A characterization-based cross-audit (e.g., "Pre-decl identifies no team path; Filed confirms no team path; Match: CONFIRMED") asserts a conclusion without presenting the evidence in a form the reader can verify character-for-character -- it does not satisfy C-31 even if the conclusion is correct.

### SE-5 / SHALL-E -- Security Gap Inventory

**TABLE_5** (three-field Remediation per Step 0.1): `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`

> RULE (C-14): "enables auditing that C-11 inline registration actually occurred" -- each row must include discovery context identifying the SE section where the gap was found. A TABLE_5 populated at the end of SE without discovery context does not pass.

> RULE (C-17): "remediation block that states the fix without linking back to the discovery section does not pass" -- each Remediation entry must chain to the SE section and the specific finding that generated the gap row.

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*Structural close condition -- precondition for closing the trace, not a recommended step.*

**CA-1.1:** Registry anchor -- TABLE_1 schema (Step 0.1). Preamble anchor -- C-01: TABLE_1/SE-1/SHALL-A/CA-1.1. Verification -> PASS/FAIL

**CA-1.2:** Registry anchor -- TABLE_2 schema (Step 0.1). Preamble anchor -- C-02: TABLE_2/SE-2/SHALL-B/CA-1.2. Verification -> PASS/FAIL

**CA-1.3:** Registry anchor -- TABLE_3 schema (Step 0.1). Preamble anchor -- C-03: TABLE_3/SE-1+SE-3/SHALL-C/CA-1.3. Verification -> PASS/FAIL

**CA-1.4:** Registry anchor -- TABLE_4 schema including per-role roll-up columns with verbatim Cross-Audit and intent-anchored Mechanisms Cited prohibition (Step 0.1). Preamble anchor -- C-04: TABLE_4/SE-4/SHALL-D/CA-1.4. Verification -> PASS/FAIL

**CA-1.5:** Registry anchor -- TABLE_5 schema (Step 0.1). Preamble anchor -- C-05: TABLE_5/SE-5/SHALL-E/CA-1.5.

> RULE (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 three-field Remediation schema declared by CA at Phase 0 Step 0.1, before PHASE 1. Downstream schema declaration requirement satisfied.

> RULE (C-17): "remediation block that states the fix without linking back to the discovery section does not pass" -- each Remediation entry must chain to discovery context. Verify each TABLE_5 row has discovery section reference.

Verification -> PASS/FAIL

**CA Format Compliance Verdict -- citing Phase 0:**
Citing: Schema Registry (Step 0.1 -- TABLE_4 verbatim Cross-Audit format (C-31) + intent-anchored Mechanisms Cited prohibition naming "any equivalent form that delegates mechanism content to another section" (C-32)), preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX with Site Type column (Step 0.3), Phase 0 gate state log -- all CA-authored before PHASE 1 began.

> RULE (C-23): "execution record, not declarative checklist" -- Phase 0 gate recorded confirmed activation of all 13 enforcement points. This verdict confirms execution matched the record.

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION (C-28 / C-25):**
Reviewing Step 0.3 ENFORCEMENT LANGUAGE INDEX against this output: [for each EL-01 through EL-13, confirm STATUS field CONFIRMED or flag UNCONFIRMED with reason].

Coverage count: N/13. N < 13 = C-28 FAIL unconditionally -- the same as 0 of 13.

- EL-12 (C-29 / C-31 verbatim cross-audit): RULE-BLOCK at SE-4 roll-up present? [YES/NO]. Cross-Audit cells use `Pre-decl: "[exact text]" | Filed: "[exact text]" | Match: CONFIRMED` format? [YES/NO].
- EL-13 (C-30 / C-32 intent-anchored equivalence): INLINE-VERBATIM at Step 0.1 TABLE_4 Mechanisms Cited prohibition present? [YES/NO]. Prohibition includes "or any equivalent form that delegates mechanism content to another section"? [YES/NO].

> RULE (C-24): "precondition for closing the trace, not a recommended step" -- writing this verdict, with full INDEX completeness confirmation, is that precondition. Trace now closed.

[C-01 PASS/FAIL. C-02 PASS/FAIL. C-03 PASS/FAIL. C-04 PASS/FAIL. C-05 PASS/FAIL. Overall: COMPLIANT / NON-COMPLIANT.]

[TRACE CLOSED -- CA-1 verdict written.]
