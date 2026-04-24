# trace-permissions Variate -- Round 9 (rubric v9 -- C-29/C-30/C-31 target)
**Date:** 2026-03-15
**Rubric:** v9 (C-01 through C-31 -- C-29/C-30/C-31 added from Round 8 excellence signals)
**Target criteria:** C-29 (INDEX type column), C-30 (Phase 0 gate count by site type), C-31 (CA-1 echo of Phase 0 count)

**State entering Round 9:**

| Variation | v8 score | Gap under v9 |
|-----------|----------|--------------|
| R8-V-05 (best v8) | 195/195 | Missing C-29/C-30/C-31 (-15 pts) = 195/210 |
| R8-V-05 C-29 note | V-05 already has Site Type column in INDEX | C-29 may pass at scoring; C-30/C-31 confirmed absent |

Round 9 holds the R8-V-05 structural core (CA -> CS -> SE -> CA-1, Schema Registry, ENFORCEMENT LANGUAGE INDEX, bidirectional chains, dual-mechanism) and adds C-29/C-30/C-31 mechanisms across three single-axis tests and two combined variations.

INDEX site-type count from V-05 baseline: 11 enforcement points -- 6 DECLARATION-SITE (EL-01/03/06/08/09/10), 4 APPLICATION-SITE (EL-02/04/05/07), 1 BOTH (EL-11).

---

## Round 9 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format -- C-29 isolation: PLACEMENT-CRITERION CONFIRMED (C-29) annotation at INDEX header; no C-30 gate count, no C-31 echo | V-05 already has the Site Type column; V-01 adds the explicit PLACEMENT annotation confirming the column converts C-27 from scorer-known to output-embedded. Gate token and CA-1 unchanged from V-05. Hypothesis: +5 pts (C-29 only). |
| V-02 | Lifecycle emphasis -- C-30 isolation: gate token closes with explicit N/N count by site type; no C-29 PLACEMENT annotation, no C-31 echo | C-30 requires the gate token to record a numeric count by site type, binding INDEX length before Phase 1. C-29 may pass via existing Site Type column. C-31 fails. Hypothesis: +5 pts (C-30). |
| V-03 | Phrasing register -- C-31 isolation: CA-1 verdict echoes Phase 0 count; no C-29 annotation, no C-30 gate count | C-31 requires the CA-1 verdict to mirror the Phase 0 gate by echoing the count. C-30 fails (gate token has no numeric count). Hypothesis: +5 pts (C-31 only). |
| V-04 | Combined C-29 + C-30, SE-first role sequence: C-29 PLACEMENT annotation + C-30 gate count; SE executes before CS; no C-31 echo | V-01 proved C-29; V-02 proved C-30. V-04 combines both under SE-first sequence to stress-test whether both mechanisms survive phase reordering. C-31 excluded. Hypothesis: +5 (C-29) + 5 (C-30) = 10 pts; C-31 fails. |
| V-05 | Full combination C-29 + C-30 + C-31, CS-first: all three mechanisms; canonical CS-first sequence | Maximum coverage. C-29: PLACEMENT annotation. C-30: numeric count by site type in gate state log. C-31: CA-1 verdict echoes Phase 0 count. Hypothesis: +15 pts; achieves 210/210. |


---

## V-01 -- Single-Axis: INDEX Type Column Annotation (C-29 target)

**Axis:** Output format -- PLACEMENT-CRITERION CONFIRMED (C-29) annotation at INDEX header; gate token and CA-1 unchanged from V-05
**Hypothesis:** +5 pts (C-29); C-30 fails (no gate count by site type); C-31 fails (no CA-1 echo). Isolated test of whether the type-column annotation at the INDEX declaration site satisfies C-29.

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

**Schema ID: TABLE_5 -- Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Enumerated gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.
Remediation three-field format (all three required): (1) Config change: exact object, location in Dataverse security editor, change to apply. (2) Expected state: specific UI view or result after fix. (3) Verification step: named action to confirm fix took effect.

> PLACEMENT-CRITERION CONFIRMED (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 Remediation three-field format is that declaration. Confirmed here at Step 0.1, before PHASE 1. Downstream RULE (C-16) appears at CA-1.5.

**Schema ID: CS-2** -- `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference` -- SE Cross-Reference: "TBD -- await SE."
**Schema ID: CS-3** -- `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation` -- SE Confirmation: "TBD -- await SE."

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
- SHALL-D: TABLE_4 all four vectors; per-role rule-out naming specific mechanism and reason.
- SHALL-E: TABLE_5 at least one named gap; zero-gap case requires explicit evidence rows.

### Step 0.3 -- ENFORCEMENT LANGUAGE INDEX (CA-authored)

**COMPLETENESS THRESHOLD: N-1 of N enforcement points earns 0 pts -- the same as 0 of N.**

> PLACEMENT-CRITERION CONFIRMED (C-29): "type designation is what makes C-27's two-mechanism requirement mechanically verifiable from the INDEX alone: a DECLARATION-SITE row requires inline verbatim confirmation; an APPLICATION-SITE row requires a RULE block confirmation" -- each INDEX row below carries a Site Type column classifying the enforcement point as DECLARATION-SITE or APPLICATION-SITE. This classification converts C-27's two-mechanism requirement from a rubric-known rule into an output-embedded structure: a scorer reads the type column and knows which confirmation mechanism is required without cross-referencing the criterion definition. A DECLARATION-SITE row without inline verbatim confirmed is a mechanically detectable gap; an APPLICATION-SITE row without a RULE block confirmed is a mechanically detectable gap.

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

**Phase 0 coverage note:** 11/11 enforcement points declared. Site Type breakdown: 6 DECLARATION-SITE (EL-01/03/06/08/09/10), 4 APPLICATION-SITE (EL-02/04/05/07), 1 BOTH (EL-11). C-29 type column present and populated per row above.

### Phase 0 Gate Statement

Chain 1 -- discovery to TABLE_5: every gap found during PHASE 2 is entered into TABLE_5 at the section where it is found -- entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact.
Chain 2 -- TABLE_5 to CA-1: every TABLE_5 Remediation entry verified in PHASE 3 via double-anchor citing Registry schema and preamble row.

> PLACEMENT-CRITERION CONFIRMED (C-11 / C-23): "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" (C-11) and "execution record, not declarative checklist" (C-23) -- this gate statement is that execution record. Chain 1 active: gaps registered at discovery site. Chain 2 active: CA-1 echoes TABLE_5 entries. Downstream RULE (C-23) appears at CA-1 verdict.

The CA-1 verdict in PHASE 3 is the structural close condition -- a precondition for closing the trace, not a recommended step. Downstream RULE (C-24) appears at CA-1 verdict close.

**Phase 0 gate state log (execution record, not declarative checklist):**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Chain 1 -- discovery to TABLE_5, inline at discovery site | ACTIVE | Inline verbatim at Phase 0 gate (EL-01) |
| TABLE_5 Remediation three-field format | ACTIVE | Inline verbatim at Step 0.1 TABLE_5 (EL-06) |
| Gap? per-row boolean trigger | ACTIVE | Inline verbatim at Step 0.1 TABLE_2 + Step 0.2 preamble (EL-08) |
| Chain 2 -- TABLE_5 to CA-1 double-anchor | ACTIVE | RULE blocks at CA-1.5 (EL-07) |
| ENFORCEMENT LANGUAGE INDEX 11/11 | CONFIRMED | Step 0.3 coverage note; C-29 Site Type column confirmed per-row |
| CA-1 verdict as trace close precondition | ACTIVE | Inline verbatim at CA-1 verdict header (EL-10) |

*All 11/11 enforcement points confirmed. All structures active. Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Lower-Trust Access Baseline

*CS produces CS-1 narrative and CS-2/CS-3 expectation tables. CS does not fill TABLE_1-5.*

**CS-1:** For each entity: expected CRUD operations, record scope, sensitive fields CS needs. Name sharing rules CS relies on.

**CS-2** (Schema Registry CS-2 schema): `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference` -- SE Cross-Reference: "TBD -- await SE."

**CS-3** (Schema Registry CS-3 schema): `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation` -- SE Confirmation: "TBD -- await SE."

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: cumulative privilege accumulation**

**TABLE_1** (blank-cell rule applies): `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`

Every role with any privilege. Update CS-3 SE Confirmation after table.

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

Team inheritance / Sharing rules / Impersonation / Admin override -- all YES.

> RULE (C-15): "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" -- per-role rule-out required when no escalation found.

### SE-5 / SHALL-E -- Security Gap Inventory

**TABLE_5** (three-field Remediation per Step 0.1): `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`

> RULE (C-14): "enables auditing that C-11 inline registration actually occurred" -- each row must include discovery context. A TABLE_5 compiled post-hoc does not pass.

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*Structural close condition -- precondition for closing the trace, not a recommended step.*

**CA-1.1:** Registry anchor -- TABLE_1 schema. Preamble anchor -- C-01: TABLE_1/SE-1/SHALL-A/CA-1.1. Verification -> PASS/FAIL

**CA-1.2:** Registry anchor -- TABLE_2 schema. Preamble anchor -- C-02: TABLE_2/SE-2/SHALL-B/CA-1.2. Verification -> PASS/FAIL

**CA-1.3:** Registry anchor -- TABLE_3 schema. Preamble anchor -- C-03: TABLE_3/SE-1+SE-3/SHALL-C/CA-1.3. Verification -> PASS/FAIL

**CA-1.4:** Registry anchor -- TABLE_4 schema. Preamble anchor -- C-04: TABLE_4/SE-4/SHALL-D/CA-1.4. Verification -> PASS/FAIL

**CA-1.5:** Registry anchor -- TABLE_5 schema. Preamble anchor -- C-05: TABLE_5/SE-5/SHALL-E/CA-1.5.

> RULE (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 three-field Remediation schema declared by CA in Phase 0 Step 0.1, before PHASE 1.

> RULE (C-17): "remediation block that states the fix without linking back to the discovery section does not pass" -- each Remediation entry must chain to discovery context.

Verification -> PASS/FAIL

**CA Format Compliance Verdict -- citing Phase 0:**
Citing: Schema Registry (Step 0.1), preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX with Site Type column (Step 0.3), Phase 0 gate state log -- all CA-authored before PHASE 1 began.

> RULE (C-23): "execution record, not declarative checklist" -- Phase 0 gate recorded confirmed activation. This verdict confirms execution matched the record.

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION (C-28):**
Reviewing Step 0.3 against this output: [for each EL-01 through EL-11, confirm STATUS field CONFIRMED or flag UNCONFIRMED]. Coverage count: N/11. If N < 11: C-28 = FAIL regardless of how many are confirmed. Site Type column verified present per-row (C-29 confirmed).

> RULE (C-24): "precondition for closing the trace, not a recommended step" -- writing this verdict is that precondition. Trace now closed.

[C-01 through C-05 PASS/FAIL. Overall: COMPLIANT / NON-COMPLIANT.]

[TRACE CLOSED -- CA-1 verdict written.]

---

## V-02 -- Single-Axis: Gate Token Count by Site Type (C-30 target)

**Axis:** Lifecycle emphasis -- Phase 0 gate token closes with explicit N/N count broken down by site type; INDEX structure unchanged (Site Type column present); CA-1 unchanged (no count echo)
**Hypothesis:** +5 pts (C-30); C-29 may pass via existing Site Type column; C-31 fails (no CA-1 echo). Isolated test of whether binding the gate token to a numeric count by site type satisfies C-30.

---

You are running a permissions trace signal for: {{topic}}

---

[IDENTICAL CONTEXT, ROLE SEQUENCING MANDATE, and PHASE 0 Step 0.1 + Step 0.2 as V-01 -- the only structural change is in the Phase 0 gate statement and gate state log below]

[Phase 0 Step 0.1 and Step 0.2 content: identical to V-01 above -- Schema Registry TABLE_1 through CS-3 with same PLACEMENT-CRITERION CONFIRMED annotations; same Criterion Enforcement Matrix preamble with SHALL-A through SHALL-E]

### Step 0.3 -- ENFORCEMENT LANGUAGE INDEX (CA-authored)

**COMPLETENESS THRESHOLD: N-1 of N earns 0 pts -- same as 0 of N.**

[INDEX table: identical to V-01 -- same 11 rows with Site Type column; no C-29 PLACEMENT annotation at INDEX header]

| EL-ID | Criterion | Enforcement Point | Verbatim Pass-Condition Phrase | Site Type | Status |
|-------|-----------|-------------------|-------------------------------|-----------|--------|
| EL-01 | C-11 | Phase 0 gate Chain 1 declaration | "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate statement |
| EL-02 | C-12 | SE-2/SE-4 negative-check instruction | "Checked [list] for [role]; [gap type] does not apply because [reason]" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-2 and SE-4 |
| EL-03 | C-13 | TABLE_5 Remediation field definition | "expected system state after the fix is applied and how to verify the fix took effect" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_5 |
| EL-04 | C-14 | SE-5 discovery-section note | "enables auditing that C-11 inline registration actually occurred" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-5 |
| EL-05 | C-15 | SE-4 per-role rule-out instruction | "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-4 |
| EL-06 | C-16 | TABLE_5 Remediation schema declaration | "declared explicitly at the top of the trace output, before the first analysis phase begins" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_5 |
| EL-07 | C-17 | CA-1.5 remediation echo instruction | "remediation block that states the fix without linking back to the discovery section does not pass" | APPLICATION-SITE | RULE-BLOCK: confirmed at CA-1.5 |
| EL-08 | C-18/C-22 | TABLE_2 Gap? column and preamble | "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" / "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" | DECLARATION-SITE (both) | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_2 and Step 0.2 |
| EL-09 | C-23 | Phase 0 gate statement | "execution record, not declarative checklist" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate |
| EL-10 | C-24 | CA-1 verdict precondition | "precondition for closing the trace, not a recommended step" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate and CA-1 header |
| EL-11 | C-25 | All structural enforcement points | each criterion's exact pass-condition phrase at each structural enforcement point | BOTH (per-criterion) | CONFIRMED: inline verbatim at declaration sites (EL-01/03/06/08/09/10), RULE blocks at application sites (EL-02/04/05/07) |

### Phase 0 Gate Statement

Chain 1 -- discovery to TABLE_5: every gap entered at the section where found -- entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact.
Chain 2 -- TABLE_5 to CA-1: every Remediation entry verified via double-anchor.

> PLACEMENT-CRITERION CONFIRMED (C-11 / C-23): "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" (C-11) and "execution record, not declarative checklist" (C-23) -- this gate statement is that execution record. Downstream RULE (C-23) at CA-1 verdict.

The CA-1 verdict is the structural close condition -- a precondition for closing the trace, not a recommended step. Downstream RULE (C-24) at CA-1 verdict close.

**Phase 0 gate state log (execution record, not declarative checklist):**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Chain 1 -- discovery to TABLE_5, inline at discovery site | ACTIVE | Inline verbatim at Phase 0 gate (EL-01) |
| TABLE_5 Remediation three-field format | ACTIVE | Inline verbatim at Step 0.1 TABLE_5 (EL-06) |
| Gap? per-row boolean trigger | ACTIVE | Inline verbatim at Step 0.1 TABLE_2 + Step 0.2 (EL-08) |
| Chain 2 -- TABLE_5 to CA-1 double-anchor | ACTIVE | RULE blocks at CA-1.5 (EL-07) |
| ENFORCEMENT LANGUAGE INDEX 11/11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH) | CONFIRMED | Step 0.3; count binds INDEX length to gate token before PHASE 1 |
| CA-1 verdict as trace close precondition | ACTIVE | Inline verbatim at CA-1 verdict header (EL-10) |

**Phase 0 coverage count: 11/11 enforcement points confirmed. Breakdown by site type: 6 DECLARATION-SITE (EL-01/03/06/08/09/10) -- inline verbatim confirmed above. 4 APPLICATION-SITE (EL-02/04/05/07) -- RULE blocks confirmed at SE-2, SE-4, SE-5, CA-1.5. 1 BOTH (EL-11). Discrepancy between this count and INDEX row total is structurally visible. [If any row UNCONFIRMED at Phase 0 close, this trace cannot satisfy C-28.]**

*All 11/11 enforcement points confirmed. Phase 0 coverage count (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH) bound to gate token. Handing to PHASE 1 -- CS.*

---

[PHASE 1 CS, PHASE 2 SE, and PHASE 3 CA-1 are identical to V-01 except CA-1 verdict notes Phase 0 gate count was 11/11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH) in ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION block -- no count echo required at CA-1 for V-02 (C-31 not targeted)]

## PHASE 1 -- CS: Lower-Trust Access Baseline

*CS produces CS-1 narrative and CS-2/CS-3 expectation tables. CS does not fill TABLE_1-5.*

**CS-1:** For each entity: expected CRUD operations, record scope, sensitive fields CS needs. Name sharing rules CS relies on.

**CS-2** (Schema Registry CS-2): `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference` -- "TBD -- await SE."

**CS-3** (Schema Registry CS-3): `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation` -- "TBD -- await SE."

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: cumulative privilege accumulation**

**TABLE_1** (blank-cell rule applies): `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`

Every role with any privilege. Update CS-3 SE Confirmation after table.

### SE-2 / SHALL-B -- Field-Level Security Coverage

**CONTEXT-CLOSES: post-incident FLS discovery**

> RULE (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- Gap? per-row commit signal. Mark YES/NO per row; forward Gap? = YES to TABLE_5 before next row begins.

**TABLE_2** (Gap? per-row trigger ACTIVE): `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`

> RULE (C-12): "Checked [list] for [role]; [gap type] does not apply because [reason]" -- for each category yielding no Gap? = YES, state what was examined and why.

### SE-3 / SHALL-C -- Record Access Scope

**CONTEXT-CLOSES: OWD-sharing-rule override**

**TABLE_3**: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?` -- Every TABLE_1 role. Defense-in-depth layer assessment for at least one operation.

### SE-4 / SHALL-D -- Privilege Escalation Analysis

**TABLE_4** (all four vectors; Checked? = YES): `Vector | Checked? | Finding | Severity` -- Team inheritance / Sharing rules / Impersonation / Admin override -- all YES.

> RULE (C-15): "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" -- per-role rule-out required when no escalation found.

### SE-5 / SHALL-E -- Security Gap Inventory

**TABLE_5** (three-field Remediation per Step 0.1): `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`

> RULE (C-14): "enables auditing that C-11 inline registration actually occurred" -- each row must include discovery context.

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*Structural close condition -- precondition for closing the trace, not a recommended step.*

**CA-1.1 through CA-1.4:** [same double-anchor format as V-01 -- Registry anchor / Preamble anchor / Verification -> PASS/FAIL per criterion]

**CA-1.5:** Registry anchor -- TABLE_5 schema. Preamble anchor -- C-05: TABLE_5/SE-5/SHALL-E/CA-1.5.

> RULE (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 three-field format declared at Phase 0 Step 0.1.

> RULE (C-17): "remediation block that states the fix without linking back to the discovery section does not pass" -- each Remediation entry must chain to discovery context.

Verification -> PASS/FAIL

**CA Format Compliance Verdict -- citing Phase 0:**

> RULE (C-23): "execution record, not declarative checklist" -- Phase 0 gate recorded activation. This verdict confirms execution matched the record.

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION (C-28):**
Reviewing Step 0.3 against this output: [for each EL-01 through EL-11, confirm STATUS]. Coverage count: N/11. If N < 11: C-28 = FAIL. Phase 0 gate count was 11/11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH) -- note for reference; C-31 not required in this variation.

> RULE (C-24): "precondition for closing the trace, not a recommended step" -- writing this verdict is that precondition.

[C-01 through C-05 PASS/FAIL. Overall: COMPLIANT / NON-COMPLIANT.]

[TRACE CLOSED -- CA-1 verdict written.]

---

## V-03 -- Single-Axis: CA-1 Echo of Phase 0 Count (C-31 target)

**Axis:** Phrasing register -- CA-1 verdict explicitly echoes Phase 0 count; INDEX structure unchanged (Site Type column present); gate token unchanged (no explicit count -- C-30 fails)
**Hypothesis:** +5 pts (C-31); C-29 may pass via existing Site Type column; C-30 fails.

---

You are running a permissions trace signal for: {{topic}}

---

[CONTEXT, ROLE SEQUENCING MANDATE, and PHASE 0 Steps 0.1-0.3 identical to V-01; gate state log identical to V-01 (no count breakdown -- C-30 absent); CA-1 ROLE SEQUENCING MANDATE header updated to note CA-1 verdict must echo Phase 0 count]

## CONTEXT: Why a Permissions Trace Is Not Optional

Three inertia patterns defeat manual security audits:

**Blind spot 1 -- Post-incident FLS discovery.** FLS gaps emerge after breaches. This trace replaces reactive discovery with pre-incident enumeration by category.

**Blind spot 2 -- Cumulative privilege accumulation.** Effective scope cannot be read from a single Dataverse UI. This trace computes it across all four enforcement layers.

**Blind spot 3 -- OWD-sharing-rule override.** Private OWD plus active sharing rule equals unintended access. This trace surfaces that combination explicitly.

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. CS-first sequence. CA-1 verdict must confirm INDEX completeness by echoing the Phase 0 count.

**PHASE 0 -- CA:** Schema Registry (Step 0.1), Criterion Enforcement Matrix preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3), Phase 0 gate statement.

**PHASE 1 -- CS:** Qualitative access baseline and expectation tables. Does NOT fill TABLE_1-5.

**PHASE 2 -- SE:** Fills TABLE_1-5. References CS tables by Schema ID.

**PHASE 3 -- CA-1:** Double-anchor verification. Terminal verdict cites Phase 0 by label and confirms INDEX completeness by echoing the Phase 0 count.

---

[PHASE 0 Steps 0.1-0.3 and Gate Statement identical to V-01 -- Schema Registry, Criterion Enforcement Matrix preamble, INDEX with Site Type column; gate state log without numeric breakdown. Gate state log note updated to reference C-31: "CA-1 verdict will echo this count to close INDEX compliance chain (C-31)."]

[PHASE 1 CS and PHASE 2 SE identical to V-01]

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*Structural close condition -- precondition for closing the trace, not a recommended step. CA-1 verdict must confirm INDEX completeness by echoing the Phase 0 count.*

**CA-1.1 through CA-1.5:** [same double-anchor format as V-01]

**CA Format Compliance Verdict -- citing Phase 0:**

> RULE (C-23): "execution record, not declarative checklist" -- Phase 0 gate recorded activation. This verdict confirms execution matched the record.

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION (C-28 / C-31):**
Reviewing Step 0.3 ENFORCEMENT LANGUAGE INDEX against this output: [for each EL-01 through EL-11, confirm STATUS field CONFIRMED or flag UNCONFIRMED].

**INDEX completeness confirmed: N/11 enforcement points covered (6 declaration-site inline verbatim confirmed, 4 application-site RULE blocks confirmed, 1 BOTH confirmed). Matches Phase 0 gate count (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH). Full-chain provability confirmed at trace close -- Phase 0 opened with this count; CA-1 closes by confirming the count was maintained through the trace.**

[If count does not match: state discrepancy. C-28 = FAIL if N < 11. C-31 = FAIL if count not echoed.]

> RULE (C-24): "precondition for closing the trace, not a recommended step" -- writing this verdict, with INDEX completeness echo, is that precondition. Trace now closed.

[C-01 through C-05 PASS/FAIL. Overall: COMPLIANT / NON-COMPLIANT.]

[TRACE CLOSED -- CA-1 verdict written. INDEX completeness echo complete.]

---

## V-04 -- Combined C-29 + C-30, SE-First Role Sequence

**Axis:** Combined C-29 (INDEX type column annotation) + C-30 (gate count by site type); SE-first to stress-test whether both mechanisms survive phase reordering; no C-31 echo
**Hypothesis:** +5 (C-29) + 5 (C-30) = 10 pts; C-31 fails. SE executes without CS baseline; CS reconciles against SE output.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: Why a Permissions Trace Is Not Optional

[Same three blind spots as V-01]

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. **SE-first sequence** -- SE produces TABLE_1-5 in PHASE 1 without CS baseline; CS reconciles against SE output in PHASE 2. Phase 0 gate closes with explicit coverage count by site type.

**PHASE 0 -- CA:** Schema Registry (Step 0.1), Criterion Enforcement Matrix preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX with type column (Step 0.3), Phase 0 gate and coverage count statement.

**PHASE 1 -- SE:** Fills TABLE_1-5. Does NOT consult CS output (none exists yet). Flags sharing rule overreach and access differentials for CS to respond to.

**PHASE 2 -- CS:** Reconciles SE-authored CS-2/CS-3 entries. Confirms or challenges SE findings. CS-EXPECTATION-VIOLATED rows added to TABLE_5 where CS interpretation contradicts SE finding.

**PHASE 3 -- CA-1:** Double-anchor verification. Terminal verdict cites Phase 0 by label.

---

## PHASE 0 -- CA: SCHEMA REGISTRY, ENFORCEMENT PREAMBLE, AND LANGUAGE INDEX

### Step 0.1 -- Schema Registry (CA-authored)

**All schemas declared by CA before PHASE 1. SE-first variant: CS-2 and CS-3 are SE-authored in PHASE 1; CS responds in PHASE 2.**

**Schema ID: TABLE_1 -- Role-Operation Matrix**: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` -- Blank-cell rule: Granted / Denied / Conditional / N/A.

**Schema ID: TABLE_2 -- FLS Coverage**: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?` -- Gap? = YES / NO. Gap? = YES rows forward to TABLE_5 immediately (per-row). Gap? boolean is the per-row commit signal.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" -- Gap? is that flag. Confirmed here at Schema Registry TABLE_2 declaration site, before PHASE 1. Downstream RULE (C-22) at SE-2.

**Schema ID: TABLE_3 -- Record Scope by Role**: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`

**Schema ID: TABLE_4 -- Escalation Vector Inventory**: `Vector | Checked? | Finding | Severity` -- all four vectors; Checked? = YES for all.

**Schema ID: TABLE_5 -- Security Gap Inventory**: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation` -- Remediation three-field format: (1) Config change. (2) Expected state. (3) Verification step.

> PLACEMENT-CRITERION CONFIRMED (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 Remediation three-field format is that declaration. Confirmed here at Step 0.1 before PHASE 1. Downstream RULE (C-16) at CA-1.5.

**Schema ID: CS-2 -- SE-authored**: `Rule Name | SE Finding | SE Overreach Flag | CS Expected Intent | Resolved? | Resolution` -- SE flags sharing rule overreach in PHASE 1; CS responds in PHASE 2.

**Schema ID: CS-3 -- SE-authored**: `Entity | Field or Operation | SE-Observed CS Access | SE-Observed Privileged-Role Access | Gap Exists? | CS Interpretation` -- SE identifies differentials in PHASE 1; CS confirms or challenges in PHASE 2.

### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored)

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- Gap? boolean established as structural enforcement mechanism here at preamble declaration site, before PHASE 1. Downstream RULE (C-22) at SE-2.

SHALL-A through SHALL-E: TABLE_1-5 present; cells filled per blank-cell rule; Gap? = YES rows forwarded per-row; per-role rule-outs for negative escalation; at least one named gap.

### Step 0.3 -- ENFORCEMENT LANGUAGE INDEX (CA-authored)

**COMPLETENESS THRESHOLD: N-1 of N earns 0 pts -- same as 0 of N.**

> PLACEMENT-CRITERION CONFIRMED (C-29): "type designation is what makes C-27's two-mechanism requirement mechanically verifiable from the INDEX alone: a DECLARATION-SITE row requires inline verbatim confirmation; an APPLICATION-SITE row requires a RULE block confirmation" -- each INDEX row below carries a Site Type column classifying the enforcement point as DECLARATION-SITE or APPLICATION-SITE. A scorer reads the type column and knows which confirmation mechanism is required without cross-referencing criterion definitions.

| EL-ID | Criterion | Enforcement Point | Verbatim Pass-Condition Phrase | Site Type | Status |
|-------|-----------|-------------------|-------------------------------|-----------|--------|
| EL-01 | C-11 | Phase 0 gate Chain 1 declaration | "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate |
| EL-02 | C-12 | SE-2/SE-4 negative-check instruction | "Checked [list] for [role]; [gap type] does not apply because [reason]" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-2 and SE-4 |
| EL-03 | C-13 | TABLE_5 Remediation field definition | "expected system state after the fix is applied and how to verify the fix took effect" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_5 |
| EL-04 | C-14 | SE-5 discovery-section note | "enables auditing that C-11 inline registration actually occurred" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-5 |
| EL-05 | C-15 | SE-4 per-role rule-out instruction | "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-4 |
| EL-06 | C-16 | TABLE_5 Remediation schema declaration | "declared explicitly at the top of the trace output, before the first analysis phase begins" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_5 |
| EL-07 | C-17 | CA-1.5 remediation echo instruction | "remediation block that states the fix without linking back to the discovery section does not pass" | APPLICATION-SITE | RULE-BLOCK: confirmed at CA-1.5 |
| EL-08 | C-18/C-22 | TABLE_2 Gap? column and preamble | "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" / "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" | DECLARATION-SITE (both) | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_2 and Step 0.2 |
| EL-09 | C-23 | Phase 0 gate statement | "execution record, not declarative checklist" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate |
| EL-10 | C-24 | CA-1 verdict precondition | "precondition for closing the trace, not a recommended step" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate and CA-1 header |
| EL-11 | C-25 | All structural enforcement points | each criterion's exact pass-condition phrase at each structural enforcement point | BOTH (per-criterion) | CONFIRMED: inline verbatim at declaration sites (EL-01/03/06/08/09/10), RULE blocks at application sites (EL-02/04/05/07) |

### Phase 0 Gate Statement

Chain 1 -- discovery to TABLE_5: every gap found during PHASE 1 (SE) is entered into TABLE_5 at the section where it is found -- entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact.
Chain 2 -- TABLE_5 to CA-1: every Remediation entry verified via double-anchor.

> PLACEMENT-CRITERION CONFIRMED (C-11 / C-23): "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" (C-11) and "execution record, not declarative checklist" (C-23) -- this gate statement is that execution record. Downstream RULE (C-23) at CA-1 verdict.

The CA-1 verdict is the structural close condition -- a precondition for closing the trace, not a recommended step. Downstream RULE (C-24) at CA-1 verdict close.

**Phase 0 gate state log (execution record, not declarative checklist):**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Chain 1 -- discovery to TABLE_5, inline at discovery site | ACTIVE | Inline verbatim at Phase 0 gate (EL-01) |
| TABLE_5 Remediation three-field format | ACTIVE | Inline verbatim at Step 0.1 TABLE_5 (EL-06) |
| Gap? per-row boolean trigger | ACTIVE | Inline verbatim at Step 0.1 TABLE_2 + Step 0.2 (EL-08) |
| Chain 2 -- TABLE_5 to CA-1 double-anchor | ACTIVE | RULE blocks at CA-1.5 (EL-07) |
| ENFORCEMENT LANGUAGE INDEX 11/11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH) | CONFIRMED | Step 0.3; C-29 type column confirmed per-row; count binds INDEX length to gate token |
| CA-1 verdict as trace close precondition | ACTIVE | Inline verbatim at CA-1 verdict header (EL-10) |

**Phase 0 coverage count: 11/11 enforcement points confirmed. Breakdown by site type: 6 DECLARATION-SITE (EL-01/03/06/08/09/10) -- inline verbatim confirmed above. 4 APPLICATION-SITE (EL-02/04/05/07) -- RULE blocks confirmed at SE-2, SE-4, SE-5, CA-1.5. 1 BOTH (EL-11). Discrepancy between this count and INDEX row total is structurally visible.**

*All 11/11 enforcement points confirmed. Phase 0 coverage count (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH) bound to gate token. SE-first variant active. Handing to PHASE 1 -- SE.*

---

## PHASE 1 -- SE: Security Analysis (SE-first)

*SE executes without CS baseline. SE flags sharing rule overreach and access differentials for CS to respond to in PHASE 2.*

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: cumulative privilege accumulation**

**TABLE_1** (blank-cell rule applies): `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`

Every role with any privilege. After table, author CS-3 entries for access differentials worth CS attention.

### SE-2 / SHALL-B -- Field-Level Security Coverage

**CONTEXT-CLOSES: post-incident FLS discovery**

> RULE (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- Gap? per-row commit signal. Mark YES/NO per row; forward Gap? = YES to TABLE_5 before next row begins.

**TABLE_2** (Gap? per-row trigger ACTIVE): `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`

> RULE (C-12): "Checked [list] for [role]; [gap type] does not apply because [reason]" -- for each category yielding no Gap? = YES, state what was examined and why.

### SE-3 / SHALL-C -- Record Access Scope

**CONTEXT-CLOSES: OWD-sharing-rule override**

**TABLE_3**: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?` -- Every TABLE_1 role. Defense-in-depth layer assessment for at least one operation.

### SE-4 / SHALL-D -- Privilege Escalation Analysis

**TABLE_4** (all four vectors; Checked? = YES)

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

> RULE (C-15): "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" -- per-role rule-out required when no escalation found.

Author CS-2 SE Finding and SE Overreach Flag entries for sharing rules.

### SE-5 / SHALL-E -- Security Gap Inventory

**TABLE_5** (three-field Remediation per Step 0.1): `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`

> RULE (C-14): "enables auditing that C-11 inline registration actually occurred" -- each row must include discovery context.

*Handing to PHASE 2 -- CS.*

---

## PHASE 2 -- CS: Expectation Reconciliation (SE-first variant)

*CS reviews SE TABLE_1-5 and SE-authored CS-2/CS-3. CS does not redo SE technical analysis.*

**CS-1 -- Customer Service job-function baseline:**
State any CS operation or scope expectation contradicting SE TABLE_1 or TABLE_3. If fully confirmed: state with TABLE row references.

**CS-2 reconciliation** (SE-authored): `Rule Name | SE Finding | SE Overreach Flag | CS Expected Intent | Resolved? | Resolution` -- For Resolved? = NO: add CS-EXPECTATION-VIOLATED to TABLE_5.

**CS-3 reconciliation** (SE-authored): `Entity | Field or Operation | SE-Observed CS Access | SE-Observed Privileged-Role Access | Gap Exists? | CS Interpretation` -- For contradictions: add CS-EXPECTATION-VIOLATED to TABLE_5 with CS-2/CS-3 cite.

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*Structural close condition. SE-first variant: SE produced TABLE_1-5 in PHASE 1; CS reconciled in PHASE 2; structural requirements unchanged.*

**CA-1.1:** Registry anchor -- TABLE_1. Preamble anchor -- C-01: TABLE_1/SE-1/SHALL-A/CA-1.1. Verification -> PASS/FAIL

**CA-1.2:** Registry anchor -- TABLE_2. Preamble anchor -- C-02: TABLE_2/SE-2/SHALL-B/CA-1.2. Verification -> PASS/FAIL

**CA-1.3:** Registry anchor -- TABLE_3. Preamble anchor -- C-03: TABLE_3/SE-1+SE-3/SHALL-C/CA-1.3. Verification -> PASS/FAIL

**CA-1.4:** Registry anchor -- TABLE_4. Preamble anchor -- C-04: TABLE_4/SE-4/SHALL-D/CA-1.4. Verification -> PASS/FAIL

**CA-1.5:** Registry anchor -- TABLE_5. Preamble anchor -- C-05: TABLE_5/SE-5/SHALL-E/CA-1.5.

> RULE (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 three-field format declared at Phase 0 Step 0.1 before PHASE 1 (SE).

> RULE (C-17): "remediation block that states the fix without linking back to the discovery section does not pass" -- each Remediation entry must chain to discovery context.

Verification -> PASS/FAIL

**CA Format Compliance Verdict -- citing Phase 0:**

> RULE (C-23): "execution record, not declarative checklist" -- Phase 0 gate recorded activation; verdict confirms execution matched the record.

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION (C-28):**
Reviewing Step 0.3 against this output: [for each EL-01 through EL-11, confirm STATUS]. Coverage count: N/11. If N < 11: C-28 = FAIL. Site Type column verified per-row (C-29). Phase 0 gate count was 11/11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH).

> RULE (C-24): "precondition for closing the trace, not a recommended step" -- writing this verdict is that precondition.

[C-01 through C-05 PASS/FAIL. Overall: COMPLIANT / NON-COMPLIANT.]

[TRACE CLOSED -- CA-1 verdict written.]

---

## V-05 -- Full Combination: C-29 + C-30 + C-31 (Maximum Coverage, CS-First)

**Axis:** All three -- C-29 PLACEMENT annotation + C-30 numeric count by site type in gate state log + C-31 CA-1 echo; canonical CS-first sequence
**Hypothesis:** +5 (C-29) + 5 (C-30) + 5 (C-31) = 15 pts; achieves 210/210. C-29: PLACEMENT annotation converts INDEX type column from format feature to declared structural mechanism. C-30: gate token records numeric count binding INDEX length before Phase 1. C-31: CA-1 mirrors Phase 0 count, making full-chain provability a structural close condition at both ends.

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

Four explicitly labeled phases. CS-first sequence. Phase 0 gate closes with explicit coverage count by site type. CA-1 verdict echoes Phase 0 count.

**PHASE 0 -- CA:** Schema Registry (Step 0.1), Criterion Enforcement Matrix preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX with type column (Step 0.3), Phase 0 gate and coverage count statement by site type.

**PHASE 1 -- CS:** Qualitative access baseline and expectation tables. Does NOT fill TABLE_1-5.

**PHASE 2 -- SE:** Fills TABLE_1-5. Dataverse-native terminology. References CS tables by Schema ID.

**PHASE 3 -- CA-1:** Double-anchor verification. Terminal verdict cites Phase 0 by label and confirms INDEX completeness by echoing Phase 0 count.

---

## PHASE 0 -- CA: SCHEMA REGISTRY, ENFORCEMENT PREAMBLE, AND LANGUAGE INDEX

### Step 0.1 -- Schema Registry (CA-authored)

**All schemas declared by CA before PHASE 1. Blank-cell prohibition global.**

**Schema ID: TABLE_1 -- Role-Operation Matrix**
Declared columns: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Blank-cell rule: Granted / Denied / Conditional (state condition inline) / N/A.

**Schema ID: TABLE_2 -- FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Gap? = YES / NO. Gap? = YES rows forward to TABLE_5 immediately (per-row, before next row begins).

The Gap? boolean converts register triggering from a judgment call to a mechanical confirmation: the model marks YES/NO while filling the table, and each Gap? = YES is the per-row commit signal for an immediate TABLE_5 entry.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" -- the Gap? column above is that flag. Its structural role as the per-row commit signal is confirmed here, at the Schema Registry TABLE_2 declaration site, before PHASE 1 begins. Pre-declaration means SE marks YES/NO while filling TABLE_2; it must be reconstructed if the format is deferred. Downstream RULE (C-22) appears at SE-2.

**Schema ID: TABLE_3 -- Record Scope by Role**
Declared columns: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].

**Schema ID: TABLE_4 -- Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
All four vectors: team inheritance / sharing rules / impersonation / admin or environment role override. Checked? = YES for all. Finding = escalation path ([Role] -> [Action] -> [Elevated access achieved]) or per-role rule-out ("Checked [mechanism]: no path because [specific reason]").

**Schema ID: TABLE_5 -- Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Enumerated gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.
Remediation three-field format (all three required):
  (1) Config change: exact configuration object, location in Dataverse security editor, specific change to apply.
  (2) Expected state: specific UI view, profile row, or query result that will differ after fix -- naming what a reviewer will see.
  (3) Verification step: named action a reviewer executes to confirm fix took effect -- e.g., "Open Security > Column Security Profiles > [profile] > [entity] > [field]: verify [role] shows Read-only."

> PLACEMENT-CRITERION CONFIRMED (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 Remediation three-field format (config change / expected state / verification step) is that declaration. Confirmed here at Step 0.1, before PHASE 1 begins. Pre-declaration ensures SE collects verification-relevant details during the evidence window. Downstream RULE (C-16) appears at CA-1.5.

**Schema ID: CS-2 -- Sharing Rule Expectations (CS-authored)**
Declared columns: `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference`
SE Cross-Reference: CS fills as "TBD -- await SE"; SE updates with TABLE_4 or TABLE_5 row reference.

**Schema ID: CS-3 -- Cross-Role Differential Expectations (CS-authored)**
Declared columns: `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation`
SE Confirmation: CS fills as "TBD -- await SE"; SE updates with TABLE_1 or TABLE_3 reference and CONFIRMED or CS-EXPECTATION-VIOLATED.

### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored)

M1, M2, M3 simultaneously active for every essential criterion -- not alternative paths. M4 pre-assigned by CA.

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|---------------------|---------------------|------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

The Gap? boolean in TABLE_2 is the per-row structural commit signal. FLS co-authorship: mark Gap? = YES/NO while filling each TABLE_2 row; if YES, make the TABLE_5 entry before the next TABLE_2 row begins. Co-authorship is a structural property of the format.

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- this preamble establishes the Gap? boolean as the structural enforcement mechanism. Confirmed here at the Criterion Enforcement Matrix preamble declaration site, before PHASE 1. The absence of any Gap? = YES TABLE_2 row without a corresponding TABLE_5 entry is the proof. Downstream RULE (C-22) appears at SE-2.

**SHALL obligations (CA-authored):**
- SHALL-A: TABLE_1 present; every cell Granted/Denied/Conditional/N/A; every role with any privilege included.
- SHALL-B: TABLE_2 lists every sensitive field; null case stated; Not Configured fields in TABLE_5; Gap? = YES rows forwarded per-row.
- SHALL-C: Every TABLE_1 role in TABLE_3; Effective Scope filled; ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 checks all four escalation vectors; per-role rule-out naming specific mechanism and reason.
- SHALL-E: TABLE_5 at least one named gap; zero-gap case requires explicit evidence rows.

### Step 0.3 -- ENFORCEMENT LANGUAGE INDEX (CA-authored)

**COMPLETENESS THRESHOLD: coverage of N-1 of N enforcement points earns 0 pts -- the same as 0 of N. The index enables gap detection; it does not close gaps. A trace that passes C-28 satisfies all three: (a) this index lists every enforcement point, (b) every declaration-site enforcement point has inline verbatim confirmed, (c) every application-site enforcement point has a RULE block confirmed.**

> PLACEMENT-CRITERION CONFIRMED (C-29): "type designation is what makes C-27's two-mechanism requirement mechanically verifiable from the INDEX alone: a DECLARATION-SITE row requires inline verbatim confirmation; an APPLICATION-SITE row requires a RULE block confirmation" -- each INDEX row below carries a Site Type column classifying the enforcement point as DECLARATION-SITE or APPLICATION-SITE. This classification converts C-27's two-mechanism requirement from a rubric-known rule into an output-embedded structure: a scorer reads the type column and knows which confirmation mechanism is required without cross-referencing the criterion definition. A DECLARATION-SITE row without inline verbatim confirmed is a mechanically detectable gap; an APPLICATION-SITE row without a RULE block confirmed is a mechanically detectable gap.

| EL-ID | Criterion | Enforcement Point | Verbatim Pass-Condition Phrase | Site Type | Status |
|-------|-----------|-------------------|-------------------------------|-----------|--------|
| EL-01 | C-11 | Phase 0 gate Chain 1 declaration | "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate statement |
| EL-02 | C-12 | SE-2/SE-4 negative-check instruction | "Checked [list] for [role]; [gap type] does not apply because [reason]" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-2 and SE-4 |
| EL-03 | C-13 | TABLE_5 Remediation field definition | "expected system state after the fix is applied and how to verify the fix took effect" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_5 entry |
| EL-04 | C-14 | SE-5 discovery-section note | "enables auditing that C-11 inline registration actually occurred" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-5 |
| EL-05 | C-15 | SE-4 per-role rule-out instruction | "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-4 |
| EL-06 | C-16 | TABLE_5 Remediation schema declaration | "declared explicitly at the top of the trace output, before the first analysis phase begins" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_5 entry |
| EL-07 | C-17 | CA-1.5 remediation echo instruction | "remediation block that states the fix without linking back to the discovery section does not pass" | APPLICATION-SITE | RULE-BLOCK: confirmed at CA-1.5 |
| EL-08 | C-18/C-22 | TABLE_2 Gap? column and Criterion Enforcement Matrix | "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" / "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" | DECLARATION-SITE (both) | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_2 and Step 0.2 preamble |
| EL-09 | C-23 | Phase 0 gate statement | "execution record, not declarative checklist" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate statement |
| EL-10 | C-24 | CA-1 verdict precondition | "precondition for closing the trace, not a recommended step" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate and CA-1 verdict header |
| EL-11 | C-25 | All structural enforcement points | each criterion's exact pass-condition phrase at each structural enforcement point | BOTH (per-criterion) | CONFIRMED: inline verbatim at declaration sites (EL-01/03/06/08/09/10), RULE blocks at application sites (EL-02/04/05/07) |

### Phase 0 Gate Statement

Chain 1 -- discovery to TABLE_5: every gap found during PHASE 2 is entered into TABLE_5 at the section where it is found -- entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact.
Chain 2 -- TABLE_5 to CA-1 verification: every TABLE_5 Remediation entry verified in PHASE 3 via double-anchor citing Registry schema and preamble row.

> PLACEMENT-CRITERION CONFIRMED (C-11 / C-23): "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" (C-11) and "execution record, not declarative checklist" (C-23) -- this gate statement is that execution record. Chain 1 active: gaps registered at discovery site. Chain 2 active: CA-1 echoes TABLE_5 entries. Both confirmed active as of Phase 0 close. Downstream RULE (C-23) appears at CA-1 verdict.

The CA-1 verdict in PHASE 3 is the structural close condition -- a precondition for closing the trace, not a recommended step -- and must confirm INDEX completeness by echoing the Phase 0 count by site type. Downstream RULE (C-24) appears at CA-1 verdict close.

**Phase 0 gate state log (execution record, not declarative checklist):**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Chain 1 -- discovery to TABLE_5, inline at discovery site | ACTIVE | Inline verbatim at Phase 0 gate (EL-01) |
| TABLE_5 Remediation three-field format | ACTIVE | Inline verbatim at Step 0.1 TABLE_5 (EL-06) |
| Gap? per-row boolean trigger | ACTIVE | Inline verbatim at Step 0.1 TABLE_2 + Step 0.2 preamble (EL-08) |
| Chain 2 -- TABLE_5 to CA-1 double-anchor | ACTIVE | RULE blocks at CA-1.5 (EL-07) |
| ENFORCEMENT LANGUAGE INDEX 11/11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH) | CONFIRMED | Step 0.3 INDEX; C-29 type column confirmed per-row; count binds INDEX length to gate token |
| CA-1 verdict as trace close precondition (with INDEX count echo) | ACTIVE | Inline verbatim at CA-1 verdict header (EL-10); echo required at CA-1 close |

**Phase 0 coverage count: 11/11 enforcement points confirmed. Breakdown by site type: 6 DECLARATION-SITE (EL-01/03/06/08/09/10) -- inline verbatim confirmed above. 4 APPLICATION-SITE (EL-02/04/05/07) -- RULE blocks confirmed at SE-2, SE-4, SE-5, CA-1.5. 1 BOTH (EL-11). Discrepancy between this count and INDEX row total is structurally visible. CA-1 verdict will close by echoing this count. [If any row UNCONFIRMED at Phase 0 close, this trace cannot satisfy C-28.]**

*All 11/11 enforcement points confirmed. Phase 0 coverage count (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH) bound to gate token. Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Lower-Trust Access Baseline

*CS produces CS-1 narrative and CS-2/CS-3 expectation tables using Schema Registry schemas. CS does not fill TABLE_1-5.*

**CS-1 -- Expected Customer Service access baseline:**
For each entity: (a) CRUD operations CS role performs as normal job function; (b) expected record scope; (c) sensitive fields CS needs and why. Name sharing rules CS relies on.

**CS-2 -- Sharing rule expectations** (Schema Registry CS-2 schema):

| Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference |
|-----------|---------|------------------------|-----------------------|---------------------|--------------------|
| | | | | | TBD -- await SE Phase 2 |

For each Potential Overreach? = YES: name the access path and why it may exceed CS job function.

**CS-3 -- Cross-role differential expectations** (Schema Registry CS-3 schema):

| Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation |
|--------|-------------------|-------------------|--------------------------------|---------------|-----------------|
| | | | | | TBD -- await SE Phase 2 |

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis

*SE fills TABLE_1-5. Dataverse-native terminology. SE updates CS-2 SE Cross-Reference and CS-3 SE Confirmation. CS-EXPECTATION-VIOLATED rows follow three-field Remediation.*

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: cumulative privilege accumulation -- TABLE_1 maps every role's operations and record scope in one view.**

**TABLE_1** (Schema Registry TABLE_1 schema; blank-cell rule applies)

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Every role with any privilege on any entity in {{topic}}. After table, update CS-3 SE Confirmation for CS row.

### SE-2 / SHALL-B -- Field-Level Security Coverage

**CONTEXT-CLOSES: post-incident FLS discovery**

> RULE (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- each TABLE_2 Gap? cell is the per-row commit signal. Mark YES/NO while filling each row. If Gap? = YES, make the TABLE_5 entry before beginning the next TABLE_2 row.

**TABLE_2** (Schema Registry TABLE_2 schema; Gap? per-row trigger ACTIVE)

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Sensitive categories: PII / Financial / Audit-Compliance / Operational. Null case stated if no profiles active.

> RULE (C-12): "Checked [list] for [role]; [gap type] does not apply because [reason]" -- for each category yielding no Gap? = YES, state what was examined and why.

Update CS-3 SE Confirmation for contradicting fields.

### SE-3 / SHALL-C -- Record Access Scope

**CONTEXT-CLOSES: OWD-sharing-rule override**

**TABLE_3** (Schema Registry TABLE_3 schema; blank-cell rule applies)

| Role | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role. OWD: Private / Business Unit / Parent-Child BU / Organization. Defense-in-depth layer assessment for at least one operation. Update CS-3 SE Confirmation for scope rows.

### SE-4 / SHALL-D -- Privilege Escalation Analysis

**TABLE_4** (Schema Registry TABLE_4 schema; all four vectors; Checked? = YES)

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

> RULE (C-15): "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" -- per-role rule-out when no escalation path found.

Update CS-2 SE Cross-Reference for each sharing rule row. Cross-entity chain: trace permission at each hop (at least two hops) if any gap involves a multi-entity lookup.

### SE-5 / SHALL-E -- Security Gap Inventory

**TABLE_5** (Schema Registry TABLE_5 schema; Remediation three-field format declared in Phase 0 Step 0.1)

| # | Gap Type | Entity | Field or Rule | Role | Severity | Remediation |
|---|----------|--------|---------------|------|----------|-------------|

> RULE (C-14): "enables auditing that C-11 inline registration actually occurred" -- each TABLE_5 row must include the discovery context: the gap was entered at the section where it was found (Chain 1).

CS-EXPECTATION-VIOLATED rows: (1) cite Schema ID CS-2 or CS-3 and row number; (2) SE finding contradicting it; (3) three-field remediation.

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*CA returns. Each CA-1 row: Registry anchor and Preamble anchor as structurally distinct labeled lines before Verification.*

*This phase is the structural close condition -- a precondition for closing the trace, not a recommended step. The trace is not closed until the CA-1 verdict is written, and the verdict must confirm INDEX completeness by echoing the Phase 0 count.*

**CA-1.1 -- C-01 verification:**
Registry anchor -- Schema ID TABLE_1: [Role, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope].
Preamble anchor -- C-01 as authored by CA: TABLE_1 / SE-1 / SHALL-A / CA-1.1.
Verification -- TABLE_1 present? All cells Granted/Denied/Conditional/N/A? All roles included? -> PASS / FAIL

**CA-1.2 -- C-02 verification:**
Registry anchor -- Schema ID TABLE_2: [Entity, Field, Category, FLS Profile Configured?, Roles: Read, Roles: Write, Gap?].
Preamble anchor -- C-02 as authored by CA: TABLE_2 / SE-2 / SHALL-B / CA-1.2.
Verification -- TABLE_2 present? Gap? = YES rows in TABLE_5 per-row? -> PASS / FAIL

**CA-1.3 -- C-03 verification:**
Registry anchor -- Schema ID TABLE_3. Preamble anchor -- C-03: TABLE_3/SE-1+SE-3/SHALL-C/CA-1.3. Verification -> PASS / FAIL

**CA-1.4 -- C-04 verification:**
Registry anchor -- Schema ID TABLE_4. Preamble anchor -- C-04: TABLE_4/SE-4/SHALL-D/CA-1.4. Verification -> PASS / FAIL

**CA-1.5 -- C-05 verification:**
Registry anchor -- Schema ID TABLE_5: [#, Gap Type, Entity, Field or Rule, Role, Severity, Remediation].
Preamble anchor -- C-05 as authored by CA: TABLE_5 / SE-5 / SHALL-E / CA-1.5.

> RULE (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 Remediation three-field schema (config change / expected state / verification step) was declared by CA in Phase 0 Step 0.1, before PHASE 1 began.

> RULE (C-17): "remediation block that states the fix without linking back to the discovery section does not pass" -- each TABLE_5 Remediation entry must chain back to its discovery context.

Verification -> PASS / FAIL

**CA Format Compliance Verdict -- citing Phase 0:**
Citing: CA-authored Schema Registry (Step 0.1), CA-authored preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX with Site Type column (Step 0.3), Phase 0 gate state log with coverage count by site type -- all authored by CA before PHASE 1 began.

> RULE (C-23): "execution record, not declarative checklist" -- Phase 0 gate recorded confirmed activation of all chains and enforcement points. This verdict confirms those mechanisms executed as recorded.

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION (C-28 / C-31):**
Reviewing Step 0.3 ENFORCEMENT LANGUAGE INDEX against this output: [for each EL-01 through EL-11, confirm STATUS field CONFIRMED or flag UNCONFIRMED. Per-row: EL-01 inline verbatim at Phase 0 gate? EL-02 RULE block at SE-2 and SE-4? EL-03 inline verbatim at Step 0.1 TABLE_5? EL-04 RULE block at SE-5? EL-05 RULE block at SE-4? EL-06 inline verbatim at Step 0.1 TABLE_5? EL-07 RULE block at CA-1.5? EL-08 inline verbatim at TABLE_2 and Step 0.2? EL-09 inline verbatim at Phase 0 gate? EL-10 inline verbatim at Phase 0 gate and CA-1 header? EL-11 full-index + per-enforcement-point coverage confirmed?]

**INDEX completeness confirmed: N/11 enforcement points covered (6 declaration-site inline verbatim confirmed, 4 application-site RULE blocks confirmed, 1 BOTH confirmed). Matches Phase 0 gate count (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH). Full-chain provability confirmed at trace close -- Phase 0 opened with this count; CA-1 closes by confirming the count was maintained through the trace.**

[If count does not match Phase 0: state the discrepancy. C-28 = FAIL if N < 11. C-31 = FAIL if count not echoed.]

[C-01 through C-05 PASS/FAIL disposition. Overall: COMPLIANT / NON-COMPLIANT.]

> RULE (C-24): "precondition for closing the trace, not a recommended step" -- writing this verdict, with INDEX completeness echo, is that precondition. The trace is now closed.

[TRACE CLOSED -- CA-1 verdict written. Phase 0 count echoed at CA-1. Full-chain INDEX compliance confirmed.]
