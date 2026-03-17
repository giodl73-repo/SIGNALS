import os

OUT = 'C:/src/sim/simulations/quest/golden/trace-permissions-variate-R10-2026-03-15.md'

# ---- shared INDEX block (same for all 5 variations) ----
INDEX_BLOCK = """
**COMPLETENESS THRESHOLD: coverage of N-1 of N enforcement points earns 0 pts -- the same as 0 of N. The index enables gap detection; it does not close gaps. A trace that passes C-28 satisfies all three: (a) this index lists every enforcement point, (b) every declaration-site enforcement point has inline verbatim confirmed, (c) every application-site enforcement point has a RULE block confirmed.**

> PLACEMENT-CRITERION CONFIRMED (C-29): "type designation is what makes C-27's two-mechanism requirement mechanically verifiable from the INDEX alone: a DECLARATION-SITE row requires inline verbatim confirmation; an APPLICATION-SITE row requires a RULE block confirmation" -- each INDEX row below carries a Site Type column classifying the enforcement point as DECLARATION-SITE or APPLICATION-SITE. A scorer reads the type column and knows which mechanism is required without cross-referencing criterion definitions.

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
"""

# ---- shared Schema Registry content ----
SCHEMA_REGISTRY_SE_FIRST = """
**All schemas declared by CA before PHASE 1. SE-first variant: CS-2 and CS-3 are SE-authored in PHASE 1; CS responds in PHASE 2. Blank-cell prohibition global.**

**Schema ID: TABLE_1 -- Role-Operation Matrix**
Declared columns: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Blank-cell rule: Granted / Denied / Conditional (state condition inline) / N/A.

**Schema ID: TABLE_2 -- FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Gap? = YES / NO. Gap? = YES rows forward to TABLE_5 immediately (per-row, before next row begins).

The Gap? boolean converts register triggering from a judgment call to a mechanical confirmation: the model marks YES/NO while filling the table, and each Gap? = YES is the per-row commit signal for an immediate TABLE_5 entry.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" -- the Gap? column above is that flag. Its structural role as the per-row commit signal is confirmed here, at the Schema Registry TABLE_2 declaration site, before PHASE 1 begins. Downstream RULE (C-22) at SE-2.

**Schema ID: TABLE_3 -- Record Scope by Role**
Declared columns: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
Blank-cell rule: Effective Scope = Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].

**Schema ID: TABLE_4 -- Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity`
All four vectors: team inheritance / sharing rules / impersonation / admin or environment role override. Checked? = YES for all. Finding = escalation path (`[Role] -> [Action] -> [Elevated access achieved]`) or per-role rule-out (`"Checked [mechanism]: no path because [specific reason]"`).

**Schema ID: TABLE_5 -- Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Enumerated gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.
Remediation three-field format (all three required):
  (1) Config change: exact configuration object, location in Dataverse security editor, specific change to apply.
  (2) Expected state: specific UI view, profile row, or query result that will differ after fix -- naming what a reviewer will see.
  (3) Verification step: named action a reviewer executes to confirm fix took effect.

> PLACEMENT-CRITERION CONFIRMED (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 Remediation three-field format (config change / expected state / verification step) is that declaration. Confirmed here at Step 0.1, before PHASE 1 begins. Pre-declaration ensures SE collects verification-relevant details during the evidence window. Downstream RULE (C-16) at CA-1.5.

**Schema ID: CS-2 (SE-authored in PHASE 1):** `Rule Name | SE Finding | SE Overreach Flag | CS Expected Intent | Resolved? | Resolution`
**Schema ID: CS-3 (SE-authored in PHASE 1):** `Entity | Field or Operation | SE-Observed CS Access | SE-Observed Privileged-Role Access | Gap Exists? | CS Interpretation`
"""

SCHEMA_REGISTRY_CS_FIRST = """
**All schemas declared by CA before PHASE 1. CS-first variant: CS-2 and CS-3 are CS-authored in PHASE 1; SE updates in PHASE 2. Blank-cell prohibition global.**

**Schema ID: TABLE_1 -- Role-Operation Matrix**
Declared columns: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Blank-cell rule: Granted / Denied / Conditional / N/A.

**Schema ID: TABLE_2 -- FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Gap? = YES / NO. Gap? = YES rows forward to TABLE_5 per-row.

The Gap? boolean converts register triggering from a judgment call to a mechanical confirmation: the model marks YES/NO while filling the table; each Gap? = YES is the per-row commit signal for an immediate TABLE_5 entry.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" -- the Gap? column above is that flag. Confirmed here at Schema Registry TABLE_2 declaration site, before PHASE 1 begins. Downstream RULE (C-22) at SE-2.

**Schema ID: TABLE_3 -- Record Scope by Role**
Declared columns: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`

**Schema ID: TABLE_4 -- Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity` -- all four vectors; Checked? = YES for all.

**Schema ID: TABLE_5 -- Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.
Remediation three-field format (all three required):
  (1) Config change: exact configuration object, location in Dataverse security editor, specific change.
  (2) Expected state: specific UI view or profile row a reviewer will see after fix.
  (3) Verification step: named action to confirm fix took effect.

> PLACEMENT-CRITERION CONFIRMED (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 Remediation three-field format is that declaration. Confirmed at Step 0.1 before PHASE 1. Downstream RULE (C-16) at CA-1.5.

**Schema ID: CS-2:** `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference` -- "TBD -- await SE."
**Schema ID: CS-3:** `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation` -- "TBD -- await SE."
"""

PREAMBLE_TABLE = """
| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|----------------------|----------------------|-------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |
"""

GATE_STATE_LOG_NO_C32 = """
**Phase 0 gate state log (execution record, not declarative checklist):**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Chain 1 -- discovery to TABLE_5, inline at discovery site | ACTIVE | Inline verbatim at Phase 0 gate (EL-01) |
| TABLE_5 Remediation three-field format | ACTIVE | Inline verbatim at Step 0.1 TABLE_5 (EL-06) |
| Gap? per-row boolean trigger | ACTIVE | Inline verbatim at Step 0.1 TABLE_2 + Step 0.2 (EL-08) |
| Chain 2 -- TABLE_5 to CA-1 double-anchor | ACTIVE | RULE blocks at CA-1.5 (EL-07) |
| ENFORCEMENT LANGUAGE INDEX 11/11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH) | CONFIRMED | Step 0.3; C-29 type column confirmed per-row; count binds INDEX length to gate token |
| CA-1 verdict as trace close precondition (with INDEX count echo) | ACTIVE | Inline verbatim at CA-1 header (EL-10) |

**Phase 0 coverage count: 11/11 enforcement points confirmed. Breakdown by site type: 6 DECLARATION-SITE (EL-01/03/06/08/09/10) -- inline verbatim confirmed above. 4 APPLICATION-SITE (EL-02/04/05/07) -- RULE blocks confirmed at SE-2, SE-4, SE-5, CA-1.5. 1 BOTH (EL-11). Discrepancy between this count and INDEX row total is structurally visible.**
"""

GATE_STATE_LOG_C32 = """
**Phase 0 gate state log (execution record, not declarative checklist):**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Chain 1 -- discovery to TABLE_5, inline at discovery site (SE-first) | ACTIVE | Inline verbatim at Phase 0 gate (EL-01) |
| TABLE_5 Remediation three-field format | ACTIVE | Inline verbatim at Step 0.1 TABLE_5 (EL-06) |
| Gap? per-row boolean trigger | ACTIVE | Inline verbatim at Step 0.1 TABLE_2 + Step 0.2 (EL-08) |
| Chain 2 -- TABLE_5 to CA-1 double-anchor | ACTIVE | RULE blocks at CA-1.5 (EL-07) |
| ENFORCEMENT LANGUAGE INDEX 11/11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH) | CONFIRMED | Step 0.3; C-29 type column confirmed per-row; count binds INDEX length to gate token |
| CA-1 GATE CLOSE as trace close precondition (with INDEX count echo) | ACTIVE | Inline verbatim at CA-1 GATE CLOSE header (EL-10) |

**Phase 0 coverage count: 11/11 enforcement points confirmed. Breakdown by site type: 6 DECLARATION-SITE (EL-01/03/06/08/09/10) -- inline verbatim confirmed above. 4 APPLICATION-SITE (EL-02/04/05/07) -- RULE blocks confirmed at SE-2, SE-4, SE-5, CA-1.5. 1 BOTH (EL-11). Discrepancy between this count and INDEX row total is structurally visible. CA-1 verdict will close by echoing this count. This is a forward reference: both ends of Chain 2 are committed at Phase 0 close, not reconstructed by matching counts independently at each end. A gate with the count and a CA-1 with the echo, but without this pre-declaration, leave the binding inferred by the scorer rather than declared by the output.**
"""

SE_PHASES = """
## PHASE 1 -- SE: Security Analysis (SE-first)

*SE executes without CS baseline. SE flags differentials in CS-2/CS-3 for CS to reconcile in PHASE 2.*

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: cumulative privilege accumulation**

**TABLE_1** (Schema Registry TABLE_1; blank-cell rule):

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Every role with any privilege on any entity in {{topic}}. After table, author CS-3 entries for access differentials.

### SE-2 / SHALL-B -- Field-Level Security Coverage

**CONTEXT-CLOSES: post-incident FLS discovery**

> RULE (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- each TABLE_2 Gap? cell is the per-row commit signal. Mark YES/NO while filling each row. If Gap? = YES, make the TABLE_5 entry before beginning the next TABLE_2 row.

**TABLE_2** (Gap? per-row trigger ACTIVE):

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Sensitive categories: PII / Financial / Audit-Compliance / Operational. Null case stated if no profiles active.

> RULE (C-12): "Checked [list] for [role]; [gap type] does not apply because [reason]" -- for each category yielding no Gap? = YES, state what was examined and why.

Update CS-3 SE Confirmation for contradicting fields.

### SE-3 / SHALL-C -- Record Access Scope

**CONTEXT-CLOSES: OWD-sharing-rule override**

**TABLE_3** (blank-cell rule):

| Role | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role. OWD: Private / BU / Parent-Child BU / Organization. Update CS-3 scope rows.

### SE-4 / SHALL-D -- Privilege Escalation Analysis

**TABLE_4** (all four vectors; Checked? = YES):

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

> RULE (C-15): "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" -- per-role rule-out required when no escalation path found.

Author CS-2 SE Finding and SE Overreach Flag entries. Cross-entity chain: trace permission at each hop if gap involves multi-entity lookup.

### SE-5 / SHALL-E -- Security Gap Inventory

**TABLE_5** (Remediation three-field format declared in Phase 0 Step 0.1):

| # | Gap Type | Entity | Field or Rule | Role | Severity | Remediation |
|---|----------|--------|---------------|------|----------|-------------|

> RULE (C-14): "enables auditing that C-11 inline registration actually occurred" -- each TABLE_5 row must include discovery context.
"""

CS_PHASE_RECONCILE = """
## PHASE 2 -- CS: Expectation Reconciliation

*CS reviews SE TABLE_1-5 and SE-authored CS-2/CS-3. CS does not redo SE technical analysis.*

**CS-1:** State contradictions with SE TABLE_1 or TABLE_3. Cite TABLE rows if confirmed.

**CS-2 reconciliation** (SE-authored): For Resolved? = NO: add CS-EXPECTATION-VIOLATED to TABLE_5 with three-field remediation.

**CS-3 reconciliation** (SE-authored): For CS Interpretation contradicting SE finding: add CS-EXPECTATION-VIOLATED to TABLE_5 with CS-3 cite.

*Handing to PHASE 3 -- CA-1.*
"""

CS_PHASE_BASELINE = """
## PHASE 1 -- CS: Lower-Trust Access Baseline

*CS produces CS-1 narrative and CS-2/CS-3 expectation tables. CS does not fill TABLE_1-5.*

**CS-1:** For each entity: expected CRUD operations, record scope, sensitive fields CS needs. Name sharing rules CS relies on.

**CS-2:** `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference` -- "TBD -- await SE."

**CS-3:** `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation` -- "TBD -- await SE."

*Handing to PHASE 2 -- SE.*
"""

CA1_BLOCK_NO_C32 = """
## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*This phase is the structural close condition -- a precondition for closing the trace, not a recommended step. The trace is not closed until the CA-1 verdict is written.*

**CA-1.1 -- C-01 verification:**
Registry anchor -- Schema ID TABLE_1: [Role, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope].
Preamble anchor -- C-01 as authored by CA: TABLE_1 / SE-1 / SHALL-A / CA-1.1.
Verification -- TABLE_1 present? All cells Granted/Denied/Conditional/N/A? All roles included? -> PASS / FAIL

**CA-1.2 -- C-02 verification:**
Registry anchor -- Schema ID TABLE_2.
Preamble anchor -- C-02: TABLE_2 / SE-2 / SHALL-B / CA-1.2.
Verification -- TABLE_2 present? Gap? = YES rows in TABLE_5 per-row? -> PASS / FAIL

**CA-1.3:** Registry anchor -- TABLE_3. Preamble anchor -- C-03/CA-1.3. Verification -> PASS / FAIL
**CA-1.4:** Registry anchor -- TABLE_4. Preamble anchor -- C-04/CA-1.4. Verification -> PASS / FAIL

**CA-1.5 -- C-05 verification:**
Registry anchor -- Schema ID TABLE_5.
Preamble anchor -- C-05: TABLE_5 / SE-5 / SHALL-E / CA-1.5.

> RULE (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 Remediation three-field schema declared by CA in Phase 0 Step 0.1, before PHASE 1 began.

> RULE (C-17): "remediation block that states the fix without linking back to the discovery section does not pass" -- each TABLE_5 Remediation entry must chain back to its discovery context.

Verification -> PASS / FAIL

**CA Format Compliance Verdict -- citing Phase 0:**

> RULE (C-23): "execution record, not declarative checklist" -- Phase 0 gate recorded confirmed activation. This verdict confirms execution matched the record.

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION (C-28 / C-31):**
Reviewing Step 0.3 ENFORCEMENT LANGUAGE INDEX against this output: [for each EL-01 through EL-11, confirm STATUS field CONFIRMED or flag UNCONFIRMED].

**INDEX completeness confirmed: N/11 enforcement points covered (6 declaration-site inline verbatim confirmed, 4 application-site RULE blocks confirmed, 1 BOTH confirmed). Matches Phase 0 gate count (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH). Full-chain provability confirmed -- Phase 0 opened with this count; CA-1 closes by confirming the count was maintained.**

[If count does not match: state discrepancy. C-28 = FAIL if N < 11. C-31 = FAIL if count not echoed.]

> RULE (C-24): "precondition for closing the trace, not a recommended step" -- writing this verdict, with INDEX completeness echo, is that precondition. Trace now closed.

[C-01 through C-05 PASS/FAIL disposition. Overall: COMPLIANT / NON-COMPLIANT.]

[TRACE CLOSED -- CA-1 verdict written. Phase 0 count echoed at CA-1.]
"""

CA1_BLOCK_C32 = """
## === PHASE 3 -- CA-1 GATE OPEN ===

*CA returns. Structural close condition. The trace is not closed until CA-1 GATE CLOSE is written. Writing it is the precondition -- not a recommended step.*

**CA-1.1 -- C-01 verification:**
Registry anchor -- Schema ID TABLE_1: [Role, Create, Read, Write, Delete, Append, AppendTo, Assign, Share, Record Scope].
Preamble anchor -- C-01: TABLE_1 / SE-1 / SHALL-A / CA-1.1.
Verification -- TABLE_1 present? All cells Granted/Denied/Conditional/N/A? All roles included? -> PASS / FAIL

**CA-1.2 -- C-02 verification:**
Registry anchor -- Schema ID TABLE_2.
Preamble anchor -- C-02: TABLE_2 / SE-2 / SHALL-B / CA-1.2.
Verification -- TABLE_2 present? Gap? = YES rows in TABLE_5 per-row? -> PASS / FAIL

**CA-1.3:** Registry anchor -- TABLE_3. Preamble anchor -- C-03/CA-1.3. Verification -> PASS / FAIL
**CA-1.4:** Registry anchor -- TABLE_4. Preamble anchor -- C-04/CA-1.4. Verification -> PASS / FAIL

**CA-1.5 -- C-05 verification:**
Registry anchor -- Schema ID TABLE_5.
Preamble anchor -- C-05: TABLE_5 / SE-5 / SHALL-E / CA-1.5.

> RULE (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 Remediation three-field schema declared by CA in Phase 0 Step 0.1, before PHASE 1 (SE) GATE OPEN.

> RULE (C-17): "remediation block that states the fix without linking back to the discovery section does not pass" -- each TABLE_5 Remediation entry must chain back to its discovery context.

Verification -> PASS / FAIL

**CA Format Compliance Verdict -- citing Phase 0:**
Citing: CA-authored Schema Registry (Step 0.1), enforcement assignments (Step 0.2), ENFORCEMENT LANGUAGE INDEX with Site Type column (Step 0.3), Phase 0 gate state log with coverage count and forward reference -- all authored by CA before PHASE 1 GATE OPEN.

> RULE (C-23): "execution record, not declarative checklist" -- Phase 0 gate recorded confirmed activation and pre-declared the CA-1 echo obligation. This verdict confirms execution matched the record and closes the forward reference.

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION (C-28 / C-31 / C-32):**
Reviewing Step 0.3 ENFORCEMENT LANGUAGE INDEX against this output: [for each EL-01 through EL-11, confirm STATUS field CONFIRMED or flag UNCONFIRMED. Per-row: EL-01 inline verbatim at Phase 0 gate? EL-02 RULE block at SE-2 and SE-4? EL-03 inline verbatim at Step 0.1 TABLE_5? EL-04 RULE block at SE-5? EL-05 RULE block at SE-4? EL-06 inline verbatim at Step 0.1 TABLE_5? EL-07 RULE block at CA-1.5? EL-08 inline verbatim at TABLE_2 and Step 0.2? EL-09 inline verbatim at Phase 0 gate? EL-10 inline verbatim at Phase 0 gate and CA-1 header? EL-11 full-index coverage confirmed?]

**INDEX completeness confirmed: N/11 enforcement points covered (6 declaration-site inline verbatim confirmed, 4 application-site RULE blocks confirmed, 1 BOTH confirmed). Matches Phase 0 gate count (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH). Full-chain provability confirmed at trace close -- Phase 0 opened with this count and pre-declared this echo; CA-1 closes by confirming the count was maintained through the trace. Forward reference committed at Phase 0 closed here at CA-1.**

[If count does not match Phase 0: state the discrepancy. C-28 = FAIL if N < 11. C-31 = FAIL if count not echoed. C-32 = FAIL if Phase 0 gate token did not contain the forward-reference phrase.]

[C-01 through C-05 PASS/FAIL disposition. Overall: COMPLIANT / NON-COMPLIANT.]

## === PHASE 3 -- CA-1 GATE CLOSE ===

*Precondition for closing the trace, not a recommended step. CA-1 verdict written. Phase 0 forward reference closed. INDEX count echoed at CA-1. Full-chain provability confirmed.*

[TRACE CLOSED.]
"""

# ---- shared gate chain declaration ----
def gate_chain(phase_num="PHASE 1 (SE)"):
    return f"""
Chain 1 -- discovery to TABLE_5: every gap found during {phase_num} is entered into TABLE_5 at the section where it is found -- entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact.
Chain 2 -- TABLE_5 to CA-1: every TABLE_5 Remediation entry verified in PHASE 3 via double-anchor citing Registry schema and preamble row.

> PLACEMENT-CRITERION CONFIRMED (C-11 / C-23): "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" (C-11) and "execution record, not declarative checklist" (C-23) -- this gate statement is that execution record. Chain 1 active: gaps registered at discovery site. Chain 2 active: CA-1 echoes TABLE_5 entries. Downstream RULE (C-23) at CA-1 verdict.

The CA-1 verdict in PHASE 3 is the structural close condition -- a precondition for closing the trace, not a recommended step -- and must confirm INDEX completeness by echoing the Phase 0 count by site type. Downstream RULE (C-24) at CA-1 verdict close.
"""

def preamble_block(co_auth_note=""):
    base = """M1, M2, M3 simultaneously active for every essential criterion -- not alternative paths. M4 pre-assigned by CA.
""" + PREAMBLE_TABLE + """
The Gap? boolean in TABLE_2 is the per-row structural commit signal. FLS co-authorship: mark Gap? = YES/NO while filling each TABLE_2 row; if YES, make the TABLE_5 entry before the next TABLE_2 row begins. Co-authorship is a structural property of the format.

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- this preamble establishes the Gap? boolean as the structural enforcement mechanism. Confirmed here at the Criterion Enforcement Matrix preamble declaration site, before PHASE 1. Downstream RULE (C-22) at SE-2.

SHALL obligations:
- SHALL-A: TABLE_1 present; every cell Granted/Denied/Conditional/N/A; every role with any privilege included.
- SHALL-B: TABLE_2 lists every sensitive field; null case stated; Gap? = YES rows forwarded per-row.
- SHALL-C: Every TABLE_1 role in TABLE_3; Effective Scope filled; ambiguous scope in TABLE_5.
- SHALL-D: TABLE_4 checks all four escalation vectors; per-role rule-out naming specific mechanism and reason.
- SHALL-E: TABLE_5 at least one named gap; zero-gap case requires explicit evidence rows.
"""
    if co_auth_note:
        base += '\n' + co_auth_note
    return base

# ---- Context block (shared) ----
CONTEXT_STANDARD = """## CONTEXT: Why a Permissions Trace Is Not Optional

Three inertia patterns defeat manual security audits:

**Blind spot 1 -- Post-incident FLS discovery.** FLS gaps emerge after breaches. This trace replaces reactive discovery with pre-incident, categorized enumeration across PII, Financial, Audit-Compliance, and Operational fields.

**Blind spot 2 -- Cumulative privilege accumulation.** No single Dataverse UI view surfaces the combined effect of security role depth, team membership, OWD, and sharing rules. This trace computes effective scope from all four layers together.

**Blind spot 3 -- OWD-sharing-rule override.** A Private OWD does not prevent a sharing rule configured independently from re-opening access. This trace cross-references OWD settings against every active sharing rule to surface unintended grants.

Each SE section opens with a CONTEXT-CLOSES label naming the blind spot it resolves."""

CONTEXT_AUDIT = """## AUDIT MANDATE: What You Are Looking For and Why

You are a Dataverse security auditor. Your job is to find what is misconfigured -- not to confirm what works. Three failure patterns are known to survive manual reviews; your trace exists to catch them before they produce incidents.

**Pattern 1 -- FLS discovered post-incident.** Restricted fields are found in audit logs after a breach, not before. Your trace pre-identifies them by category -- PII, Financial, Audit-Compliance, Operational -- before any incident occurs.

**Pattern 2 -- Privilege accumulation invisible to the viewer.** No single Dataverse UI view shows you the combined effect of security role depth, team membership, OWD, and sharing rules. You compute effective scope from all four layers.

**Pattern 3 -- OWD-sharing-rule override.** A Private OWD setting does not block a sharing rule configured independently. You cross-reference OWD against every active sharing rule to find the combinations that reopen access.

Each SE section opens with a CONTEXT-CLOSES label naming the failure pattern it eliminates."""

# ===================================================================
# V-01: SE-first, standard voice, C-32 absent
# ===================================================================

V01 = f"""
---

## V-01 -- Single-Axis: SE-First Role Sequence (C-32 absent)

**Axis:** Role sequence -- SE builds TABLE_1-5 before CS baseline exists; CS reconciles against SE output
**Hypothesis:** SE-first ordering produces more complete privilege topology (no CS operational assumptions constraining TABLE_1 coverage). C-32 absent: gate records count, CA-1 echoes it, but gate does not pre-declare the echo obligation.

---

You are running a permissions trace signal for: {{{{topic}}}}

---

{CONTEXT_STANDARD}

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. **SE-first sequence** -- SE produces TABLE_1-5 in PHASE 1 without a CS baseline; CS reconciles against SE output in PHASE 2. Phase 0 gate closes with explicit coverage count by site type. CA-1 verdict echoes Phase 0 count.

**PHASE 0 -- CA:** Schema Registry (Step 0.1), Criterion Enforcement Matrix preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX with type column (Step 0.3), Phase 0 gate and coverage count.
**PHASE 1 -- SE:** Fills TABLE_1-5. Does NOT consult CS output. Flags differentials for CS-2/CS-3 fill.
**PHASE 2 -- CS:** Reconciles SE-authored CS-2/CS-3. CS-EXPECTATION-VIOLATED rows where CS contradicts SE.
**PHASE 3 -- CA-1:** Double-anchor verification. Terminal verdict echoes Phase 0 count.

---

## PHASE 0 -- CA: SCHEMA REGISTRY, ENFORCEMENT PREAMBLE, AND LANGUAGE INDEX

### Step 0.1 -- Schema Registry (CA-authored)
{SCHEMA_REGISTRY_SE_FIRST}

### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored)

{preamble_block()}

### Step 0.3 -- ENFORCEMENT LANGUAGE INDEX (CA-authored)
{INDEX_BLOCK}

### Phase 0 Gate Statement
{gate_chain()}
{GATE_STATE_LOG_NO_C32}

*All 11/11 confirmed. SE-first variant active. Handing to PHASE 1 -- SE.*

---
{SE_PHASES}
---
{CS_PHASE_RECONCILE}
---
{CA1_BLOCK_NO_C32}
"""

# ===================================================================
# V-02: CS-first, CONTEXT-CLOSES MATRIX added, standard voice, C-32 absent
# ===================================================================

CONTEXT_CLOSES_MATRIX = """
### Step 0.1a -- CONTEXT-CLOSES MATRIX (CA-authored)

**Pre-declared before PHASE 1. Each SE sub-section must open with its assigned CONTEXT-CLOSES label. A sub-section that omits its label leaves the blind spot it was assigned to close unconfirmed.**

| SE Sub-Section | CONTEXT-CLOSES Label | Blind Spot Resolved | Primary Criterion |
|----------------|----------------------|---------------------|-------------------|
| SE-1 / SHALL-A | cumulative privilege accumulation | TABLE_1 maps all role-operation-scope combinations that no single Dataverse UI surfaces | C-01 / C-03 |
| SE-2 / SHALL-B | post-incident FLS discovery | TABLE_2 replaces reactive discovery with pre-incident category-first enumeration | C-02 / C-10 |
| SE-3 / SHALL-C | OWD-sharing-rule override | TABLE_3 cross-references OWD against sharing rules to surface Private-OWD-plus-active-rule combinations | C-03 / C-06 |
| SE-4 / SHALL-D | cumulative privilege accumulation (escalation layer) | TABLE_4 checks all four elevation vectors SE cannot read from a single UI | C-04 / C-05 / C-15 |
| SE-5 / SHALL-E | all three blind spots (inventory) | TABLE_5 collects gaps registered inline at discovery site per Chain 1 | C-08 / C-11 / C-14 |
"""

SE_PHASES_CONTEXT_CLOSES = """
## PHASE 2 -- SE: Security Analysis

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: cumulative privilege accumulation** *(pre-declared in Step 0.1a)*

**TABLE_1** (Schema Registry TABLE_1; blank-cell rule): `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` -- every role with any privilege. Update CS-3 SE Confirmation after table.

### SE-2 / SHALL-B -- Field-Level Security Coverage

**CONTEXT-CLOSES: post-incident FLS discovery** *(pre-declared in Step 0.1a)*

> RULE (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- Gap? per-row commit signal. Mark YES/NO per row; forward Gap? = YES to TABLE_5 before next row begins.

**TABLE_2** (Gap? per-row trigger ACTIVE): `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`

> RULE (C-12): "Checked [list] for [role]; [gap type] does not apply because [reason]" -- for each category yielding no Gap? = YES, state what was examined and why.

### SE-3 / SHALL-C -- Record Access Scope

**CONTEXT-CLOSES: OWD-sharing-rule override** *(pre-declared in Step 0.1a)*

**TABLE_3**: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?` -- every TABLE_1 role. Update CS-3 SE Confirmation for scope rows.

### SE-4 / SHALL-D -- Privilege Escalation Analysis

**CONTEXT-CLOSES: cumulative privilege accumulation (escalation layer)** *(pre-declared in Step 0.1a)*

**TABLE_4** (all four vectors; Checked? = YES): `Vector | Checked? | Finding | Severity`

> RULE (C-15): "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" -- per-role rule-out when no escalation path found.

Update CS-2 SE Cross-Reference for each sharing rule row. Cross-entity chain: trace permission at each hop if gap involves multi-entity lookup.

### SE-5 / SHALL-E -- Security Gap Inventory

**CONTEXT-CLOSES: all three blind spots (inventory)** *(pre-declared in Step 0.1a)*

**TABLE_5** (three-field Remediation per Step 0.1): `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`

> RULE (C-14): "enables auditing that C-11 inline registration actually occurred" -- each TABLE_5 row must include discovery context.

*Handing to PHASE 3 -- CA-1.*
"""

V02 = f"""
---

## V-02 -- Single-Axis: CONTEXT-CLOSES Matrix Pre-Declared at Phase 0 (C-32 absent)

**Axis:** Output format -- Phase 0 adds a CONTEXT-CLOSES MATRIX table mapping each SE sub-section to the blind spot it resolves before Phase 1 begins
**Hypothesis:** Pre-mapping analysis sections to blind spots primes SE to produce CONTEXT-CLOSES labels that are structurally committed before the evidence window opens. C-32 absent: gate count present, CA-1 echo present, forward-reference phrase absent.

---

You are running a permissions trace signal for: {{{{topic}}}}

---

{CONTEXT_STANDARD}

---

## ROLE SEQUENCING MANDATE

Four explicitly labeled phases. CS-first sequence. Phase 0 gate closes with explicit coverage count by site type and pre-declares the CONTEXT-CLOSES MATRIX. CA-1 verdict echoes Phase 0 count.

**PHASE 0 -- CA:** Schema Registry (Step 0.1), CONTEXT-CLOSES MATRIX (Step 0.1a), Criterion Enforcement Matrix preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3), Phase 0 gate and coverage count.
**PHASE 1 -- CS:** Qualitative access baseline and expectation tables. Does NOT fill TABLE_1-5.
**PHASE 2 -- SE:** Fills TABLE_1-5. Each SE sub-section opens with the CONTEXT-CLOSES label pre-declared in Step 0.1a.
**PHASE 3 -- CA-1:** Double-anchor verification. Terminal verdict echoes INDEX count.

---

## PHASE 0 -- CA: SCHEMA REGISTRY, CONTEXT-CLOSES MATRIX, ENFORCEMENT PREAMBLE, AND LANGUAGE INDEX

### Step 0.1 -- Schema Registry (CA-authored)
{SCHEMA_REGISTRY_CS_FIRST}
{CONTEXT_CLOSES_MATRIX}

### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored)

{preamble_block()}

### Step 0.3 -- ENFORCEMENT LANGUAGE INDEX (CA-authored)
{INDEX_BLOCK}

### Phase 0 Gate Statement
{gate_chain("PHASE 2 (SE)")}

**Phase 0 gate state log (execution record, not declarative checklist):**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Chain 1 -- discovery to TABLE_5, inline at discovery site | ACTIVE | Inline verbatim at Phase 0 gate (EL-01) |
| TABLE_5 Remediation three-field format | ACTIVE | Inline verbatim at Step 0.1 TABLE_5 (EL-06) |
| Gap? per-row boolean trigger | ACTIVE | Inline verbatim at Step 0.1 TABLE_2 + Step 0.2 (EL-08) |
| CONTEXT-CLOSES MATRIX -- 5 SE sub-sections mapped to blind spots | ACTIVE | Step 0.1a; SE sub-sections must open with assigned label |
| Chain 2 -- TABLE_5 to CA-1 double-anchor | ACTIVE | RULE blocks at CA-1.5 (EL-07) |
| ENFORCEMENT LANGUAGE INDEX 11/11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH) | CONFIRMED | Step 0.3; C-29 type column confirmed per-row |
| CA-1 verdict as trace close precondition (with INDEX count echo) | ACTIVE | Inline verbatim at CA-1 header (EL-10) |

**Phase 0 coverage count: 11/11 enforcement points confirmed. Breakdown by site type: 6 DECLARATION-SITE (EL-01/03/06/08/09/10) -- inline verbatim above. 4 APPLICATION-SITE (EL-02/04/05/07) -- RULE blocks at SE-2, SE-4, SE-5, CA-1.5. 1 BOTH (EL-11). Discrepancy between this count and INDEX row total is structurally visible.**

*All 11/11 confirmed. CONTEXT-CLOSES MATRIX active. Handing to PHASE 1 -- CS.*

---
{CS_PHASE_BASELINE}
---
{SE_PHASES_CONTEXT_CLOSES}
---
{CA1_BLOCK_NO_C32}
"""

# ===================================================================
# V-03: CS-first, investigative audit voice, C-32 absent
# ===================================================================

V03 = f"""
---

## V-03 -- Single-Axis: Investigative Audit Phrasing Register (C-32 absent)

**Axis:** Phrasing register -- imperative second-person audit framing throughout; "find what is misconfigured" orientation
**Hypothesis:** Positioning as an active auditor activates gap-detection mental models over template-completion ones. C-32 absent: gate count present, CA-1 echo present, forward-reference phrase absent.

---

You are running a permissions trace signal for: {{{{topic}}}}

---

{CONTEXT_AUDIT}

---

## EXECUTION MANDATE

Four phases. CS-first. Phase 0 closes with an explicit enforcement-point count. CA-1 echoes it.

**PHASE 0 -- CA:** Declare all schemas. Pre-load enforcement mechanisms. Record activation state. Gate closes with count.
**PHASE 1 -- CS:** Identify what Customer Service expects to be able to do. Do not fill TABLE_1-5.
**PHASE 2 -- SE:** Execute the audit. Fill TABLE_1-5. Find the gaps. Register each gap at the point you find it.
**PHASE 3 -- CA-1:** Verify structural compliance. Echo the Phase 0 count. Close the trace.

---

## PHASE 0 -- CA: AUDIT INFRASTRUCTURE

### Step 0.1 -- Schema Registry (CA-authored)

**Declare all schemas before the audit begins. Every cell must be filled -- blank cells are prohibited.**

**Schema ID: TABLE_1 -- Who Can Do What**
`Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Every cell: Granted / Denied / Conditional (state the condition) / N/A.

**Schema ID: TABLE_2 -- Which Fields Are Restricted and to Whom**
`Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Gap? = YES or NO. When you mark Gap? = YES, enter the TABLE_5 row before moving to the next TABLE_2 row.

The Gap? boolean converts register triggering from a judgment call to a mechanical confirmation: you mark YES/NO while filling the table, and each YES is your instruction to make the TABLE_5 entry immediately.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" -- the Gap? column above is that flag. Confirmed here at Schema Registry TABLE_2 declaration site, before PHASE 1 begins. Downstream RULE (C-22) at SE-2.

**Schema ID: TABLE_3 -- What Records Are Accessible:**
`Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?` -- Effective Scope: Own / BU / Parent-Child BU / Org-wide / Team-scoped / Sharing-[rule name].

**Schema ID: TABLE_4 -- Escalation Vectors Checked:**
`Vector | Checked? | Finding | Severity` -- all four vectors; Checked? = YES for all.
Escalation path: `[Role] -> [Action] -> [Elevated access achieved]`. Rule-out: `"Checked [mechanism]: no path because [specific reason]"`.

**Schema ID: TABLE_5 -- What You Found and How to Fix It:**
`# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.

Every Remediation entry requires all three:
  (1) Config change: exact object, where it is in the Dataverse security editor, precise change to make.
  (2) Expected state: what a reviewer will see in a specific UI view after the fix.
  (3) Verification step: named action a reviewer performs to confirm the fix took effect.

> PLACEMENT-CRITERION CONFIRMED (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- the three-field TABLE_5 Remediation requirement is that declaration. Confirmed at Step 0.1, before PHASE 1. Downstream RULE (C-16) at CA-1.5.

**Schema ID: CS-2:** `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference` -- "TBD -- await SE."
**Schema ID: CS-3:** `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation` -- "TBD -- await SE."

### Step 0.2 -- Enforcement Assignments (CA-authored)

Every essential criterion is enforced at three simultaneous checkpoints -- not alternative paths.
{PREAMBLE_TABLE}
The Gap? boolean in TABLE_2 is your per-row commit signal. Mark YES/NO while filling each row. If YES, make the TABLE_5 entry before moving to the next row. Co-authorship is a structural property of the format.

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- the enforcement assignment above establishes the Gap? boolean as the structural mechanism. Confirmed at this declaration site, before PHASE 1. Downstream RULE (C-22) at SE-2.

SHALL-A: TABLE_1 present; every cell filled; all roles included. SHALL-B: TABLE_2 lists every sensitive field; Gap? = YES rows per-row. SHALL-C: Every TABLE_1 role in TABLE_3. SHALL-D: TABLE_4 all four vectors; per-role rule-out. SHALL-E: TABLE_5 at least one named gap.

### Step 0.3 -- Enforcement Language Index (CA-authored)

**Coverage is a threshold. You either list every enforcement point and confirm coverage at each, or you fail. Listing 10 of 11 earns zero -- the same as listing none.**
{INDEX_BLOCK}

### Phase 0 Gate

**Chain 1 -- gap to TABLE_5:** Every gap you find during PHASE 2 goes into TABLE_5 at the point you find it -- entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact.

**Chain 2 -- TABLE_5 to CA-1:** Every TABLE_5 Remediation entry gets verified in PHASE 3 via double-anchor. CA-1 confirms the count.

> PLACEMENT-CRITERION CONFIRMED (C-11 / C-23): "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" (C-11) and "execution record, not declarative checklist" (C-23) -- this gate is that execution record. Chain 1 active. Chain 2 active. Downstream RULE (C-23) at CA-1 verdict.

Writing CA-1's verdict is a precondition for closing this trace -- not a recommended step. Downstream RULE (C-24) at CA-1 close.

**Phase 0 activation log (execution record, not declarative checklist):**

| Mechanism | State | How Confirmed |
|-----------|-------|---------------|
| Chain 1 -- gaps to TABLE_5 at discovery site | ACTIVE | Inline verbatim at Phase 0 gate (EL-01) |
| TABLE_5 Remediation three-field format | ACTIVE | Inline verbatim at Step 0.1 TABLE_5 (EL-06) |
| Gap? per-row commit signal | ACTIVE | Inline verbatim at Step 0.1 TABLE_2 + Step 0.2 (EL-08) |
| Chain 2 -- TABLE_5 to CA-1 | ACTIVE | RULE blocks at CA-1.5 (EL-07) |
| ENFORCEMENT LANGUAGE INDEX 11/11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH) | CONFIRMED | Step 0.3; C-29 type column confirmed per-row |
| CA-1 verdict as trace close precondition | ACTIVE | Inline verbatim at CA-1 header (EL-10) |

**Phase 0 coverage count: 11/11 enforcement points confirmed. Breakdown: 6 DECLARATION-SITE (EL-01/03/06/08/09/10) -- inline verbatim above. 4 APPLICATION-SITE (EL-02/04/05/07) -- RULE blocks at SE-2, SE-4, SE-5, CA-1.5. 1 BOTH (EL-11). If this count and the INDEX row total do not match, the discrepancy is structurally visible.**

*All 11/11 confirmed. Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: What Customer Service Expects

*CS does not fill TABLE_1-5. CS states expectations, names sharing rules, flags over- or under-permissioned access.*

**CS-1:** For each entity: which CRUD operations, which record scope, which sensitive fields, which sharing rules.
**CS-2:** `Rule Name | Trigger | Expected Access Granted | Intended for CS Role? | Potential Overreach? | SE Cross-Reference` -- "TBD -- await SE."
**CS-3:** `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation` -- "TBD -- await SE."

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: The Audit

*Fill TABLE_1-5. Register every gap at the point you find it. Do not defer.*

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: cumulative privilege accumulation**

TABLE_1: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` -- every role, every privilege, no blank cells.

### SE-2 / SHALL-B -- Field-Level Security

**CONTEXT-CLOSES: post-incident FLS discovery**

> RULE (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- Gap? per-row commit signal. Mark YES/NO per row. If Gap? = YES, make the TABLE_5 entry before moving to the next row.

TABLE_2: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`

> RULE (C-12): "Checked [list] for [role]; [gap type] does not apply because [reason]" -- for every category with no Gap? = YES, name what you examined and why no gap exists.

### SE-3 / SHALL-C -- Record Access Scope

**CONTEXT-CLOSES: OWD-sharing-rule override**

TABLE_3: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?` -- every TABLE_1 role, no blank cells.

### SE-4 / SHALL-D -- Escalation Vectors

**CONTEXT-CLOSES: cumulative privilege accumulation (elevation layer)**

Check all four vectors. Checked? = YES for every row. Find the path or rule it out per role -- no blankets.

> RULE (C-15): "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" -- name the role, name the mechanism, explain why it does not elevate.

### SE-5 / SHALL-E -- Security Gap Inventory

**CONTEXT-CLOSES: all three failure patterns (inventory)**

TABLE_5: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`

> RULE (C-14): "enables auditing that C-11 inline registration actually occurred" -- each TABLE_5 row must show where in the audit it was entered.

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Structural Verification

*The audit is not complete until you write this verdict. Writing it is the precondition -- not a recommended step.*

**CA-1.1 -- C-01:** Registry anchor -- TABLE_1. Preamble anchor -- C-01: TABLE_1/SE-1/SHALL-A/CA-1.1. Verification -> PASS / FAIL
**CA-1.2 -- C-02:** Registry anchor -- TABLE_2. Preamble anchor -- C-02: TABLE_2/SE-2/SHALL-B/CA-1.2. Verification -> PASS / FAIL
**CA-1.3:** Registry anchor -- TABLE_3. Preamble anchor -- C-03/CA-1.3. Verification -> PASS / FAIL
**CA-1.4:** Registry anchor -- TABLE_4. Preamble anchor -- C-04/CA-1.4. Verification -> PASS / FAIL
**CA-1.5:** Registry anchor -- TABLE_5. Preamble anchor -- C-05: TABLE_5/SE-5/SHALL-E/CA-1.5.

> RULE (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 three-field format declared at Step 0.1, before PHASE 1.
> RULE (C-17): "remediation block that states the fix without linking back to the discovery section does not pass" -- every TABLE_5 entry must chain to discovery context.

Verification -> PASS / FAIL

**Compliance Verdict -- citing Phase 0:**

> RULE (C-23): "execution record, not declarative checklist" -- Phase 0 recorded activation. Verdict confirms execution matched.

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CHECK (C-28 / C-31):**
Review EL-01 through EL-11. Count: N/11.

**Completeness confirmed: N/11 (6 declaration-site inline verbatim, 4 application-site RULE blocks, 1 BOTH). Matches Phase 0 gate count. Phase 0 opened with this count; CA-1 closes by confirming it was maintained.**

> RULE (C-24): "precondition for closing the trace, not a recommended step" -- writing this verdict is that precondition.

[TRACE CLOSED.]
"""

# ===================================================================
# V-04: SE-first + investigative voice, C-32 absent
# ===================================================================

V04 = f"""
---

## V-04 -- Two-Axis: SE-First + Investigative Phrasing Register (C-32 absent)

**Axes:** Role sequence (SE-first) + Phrasing register (investigative audit voice)
**Hypothesis:** SE-first removes CS operational assumptions from TABLE_1; audit framing ensures SE treats TABLE_4 as gap-hunting rather than coverage checklist. C-32 absent.

---

You are running a permissions trace signal for: {{{{topic}}}}

---

## AUDIT MANDATE

You are a Dataverse security auditor executing an SE-first trace. You build the privilege topology before consulting operational assumptions -- Customer Service reconciles against your findings afterward, not before.

Three failure patterns survive manual reviews:

**Pattern 1 -- FLS discovered post-incident.** Enumerate restricted fields by category (PII / Financial / Audit-Compliance / Operational) before any breach occurs.

**Pattern 2 -- Privilege accumulation invisible to the viewer.** Compute effective scope from security role depth, team membership, OWD, and sharing rules together.

**Pattern 3 -- OWD-sharing-rule override.** Cross-reference every active sharing rule against OWD settings to find combinations that reopen Private access.

Each SE section opens with a CONTEXT-CLOSES label naming the pattern it eliminates.

---

## EXECUTION MANDATE

Four phases. **SE-first.** Phase 0 closes with enforcement-point count by site type. CA-1 echoes the count.

**PHASE 0 -- CA:** Declare schemas. Pre-load enforcement mechanisms. Record activation state.
**PHASE 1 -- SE:** Execute the audit. Fill TABLE_1-5. Register every gap at the point you find it. Flag differentials for CS-2/CS-3.
**PHASE 2 -- CS:** Review SE findings. Challenge or confirm. Add CS-EXPECTATION-VIOLATED rows.
**PHASE 3 -- CA-1:** Verify structural compliance. Echo Phase 0 count. Close the trace.

---

## PHASE 0 -- CA: AUDIT INFRASTRUCTURE (SE-FIRST VARIANT)

### Step 0.1 -- Schema Registry (CA-authored)

**Declare all schemas before the audit begins. SE-first: CS-2/CS-3 SE-authored in PHASE 1; CS responds in PHASE 2. Every cell must be filled -- blank cells are prohibited.**

**Schema ID: TABLE_1 -- Who Can Do What:**
`Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` -- every cell: Granted / Denied / Conditional / N/A.

**Schema ID: TABLE_2 -- Which Fields Are Restricted:**
`Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Gap? = YES or NO. When you mark Gap? = YES, enter the TABLE_5 row before moving to the next TABLE_2 row.

The Gap? boolean converts register triggering from a judgment call to a mechanical confirmation: you mark YES/NO while filling the table; each YES is your immediate TABLE_5 commit signal.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" -- Gap? column confirmed at TABLE_2 declaration site, before PHASE 1 begins. Downstream RULE (C-22) at SE-2.

**Schema ID: TABLE_3 -- What Records Are Accessible:** `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
**Schema ID: TABLE_4 -- Escalation Vectors Checked:** `Vector | Checked? | Finding | Severity` -- all four; Checked? = YES for all.
**Schema ID: TABLE_5 -- What You Found and How to Fix It:**
`# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Remediation three fields (all required): (1) Config change. (2) Expected state. (3) Verification step.

> PLACEMENT-CRITERION CONFIRMED (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 three-field format declared here before PHASE 1 (SE). Downstream RULE (C-16) at CA-1.5.

**Schema ID: CS-2 (SE-authored):** `Rule Name | SE Finding | SE Overreach Flag | CS Expected Intent | Resolved? | Resolution`
**Schema ID: CS-3 (SE-authored):** `Entity | Field or Operation | SE-Observed CS Access | SE-Observed Privileged-Role Access | Gap Exists? | CS Interpretation`

### Step 0.2 -- Enforcement Assignments (CA-authored)
{PREAMBLE_TABLE}
Gap? boolean is your per-row commit signal. Mark YES/NO per row. If YES, enter TABLE_5 before the next TABLE_2 row. Co-authorship is a structural property of the format.

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- Gap? established as structural mechanism at preamble declaration site, before PHASE 1. Downstream RULE (C-22) at SE-2.

SHALL-A through SHALL-E: identical to V-01.

### Step 0.3 -- Enforcement Language Index (CA-authored)

**Coverage is a threshold. 10/11 = 0 pts. Same as 0/11.**
{INDEX_BLOCK}

### Phase 0 Gate

**Chain 1:** Every gap you find during PHASE 1 (SE) goes into TABLE_5 immediately -- entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact.
**Chain 2:** Every TABLE_5 Remediation entry gets double-anchor verified at CA-1.

> PLACEMENT-CRITERION CONFIRMED (C-11 / C-23): "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" (C-11) and "execution record, not declarative checklist" (C-23). Chain 1 active. Chain 2 active. Downstream RULE (C-23) at CA-1 verdict.

Writing CA-1's verdict is the precondition -- not a recommended step. Downstream RULE (C-24) at CA-1.

**Phase 0 activation log (execution record, not declarative checklist):**

| Mechanism | State | How Confirmed |
|-----------|-------|---------------|
| Chain 1 -- gaps to TABLE_5 at discovery site (SE-first) | ACTIVE | Inline verbatim at Phase 0 gate (EL-01) |
| TABLE_5 three-field Remediation format | ACTIVE | Inline verbatim at Step 0.1 TABLE_5 (EL-06) |
| Gap? per-row commit signal | ACTIVE | Inline verbatim at Step 0.1 TABLE_2 + Step 0.2 (EL-08) |
| Chain 2 -- TABLE_5 to CA-1 | ACTIVE | RULE blocks at CA-1.5 (EL-07) |
| ENFORCEMENT LANGUAGE INDEX 11/11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH) | CONFIRMED | Step 0.3; C-29 type column confirmed per-row |
| CA-1 verdict as precondition | ACTIVE | Inline verbatim at CA-1 header (EL-10) |

**Phase 0 coverage count: 11/11 enforcement points confirmed. Breakdown: 6 DECLARATION-SITE -- inline verbatim above. 4 APPLICATION-SITE -- RULE blocks at SE-2, SE-4, SE-5, CA-1.5. 1 BOTH (EL-11). Count mismatch with INDEX row total is structurally visible.**

*11/11 confirmed. SE-first variant active. Handing to PHASE 1 -- SE.*

---
{SE_PHASES}
---

## PHASE 2 -- CS: Expectation Reconciliation

*Review SE TABLE_1-5 and SE-authored CS-2/CS-3. Challenge findings where CS intent differs from SE observation.*

**CS-1:** State contradictions with SE TABLE_1 or TABLE_3. Cite TABLE rows if confirmed.
**CS-2 reconciliation:** For Resolved? = NO: add CS-EXPECTATION-VIOLATED to TABLE_5.
**CS-3 reconciliation:** For contradictions: add CS-EXPECTATION-VIOLATED to TABLE_5 with CS-3 cite.

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Structural Verification

*You are not done until you write this verdict. Writing it is the precondition.*

**CA-1.1:** Registry anchor -- TABLE_1. Preamble anchor -- C-01/CA-1.1. Verification -> PASS / FAIL
**CA-1.2:** Registry anchor -- TABLE_2. Preamble anchor -- C-02/CA-1.2. Verification -> PASS / FAIL
**CA-1.3:** Registry anchor -- TABLE_3. Preamble anchor -- C-03/CA-1.3. Verification -> PASS / FAIL
**CA-1.4:** Registry anchor -- TABLE_4. Preamble anchor -- C-04/CA-1.4. Verification -> PASS / FAIL
**CA-1.5:** Registry anchor -- TABLE_5. Preamble anchor -- C-05: TABLE_5/SE-5/SHALL-E/CA-1.5.

> RULE (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 three-field format declared at Step 0.1 before PHASE 1 (SE).
> RULE (C-17): "remediation block that states the fix without linking back to the discovery section does not pass" -- every TABLE_5 entry must chain to discovery context.

**Compliance Verdict -- citing Phase 0:**

> RULE (C-23): "execution record, not declarative checklist" -- Phase 0 recorded activation. Verdict confirms execution matched.

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS (C-28 / C-31):**
Review EL-01 through EL-11. Count: N/11.

**Completeness confirmed: N/11 (6 declaration-site inline verbatim, 4 application-site RULE blocks, 1 BOTH). Matches Phase 0 count. Phase 0 opened with this count; CA-1 closes by confirming it was maintained.**

> RULE (C-24): "precondition for closing the trace, not a recommended step" -- writing this verdict, with count echo, is that precondition.

[TRACE CLOSED.]
"""

# ===================================================================
# V-05: SE-first + lifecycle gates + C-32 forward reference
# ===================================================================

V05 = f"""
---

## V-05 -- Combined: SE-First + Lifecycle Gates + C-32 Forward Reference

**Axes:** Role sequence (SE-first) + Lifecycle emphasis (explicit PHASE GATE OPEN/CLOSE tokens) + **C-32 forward reference in Phase 0 gate token**
**Hypothesis:** SE-first + explicit phase gates + Phase 0 pre-committing "CA-1 verdict will close by echoing this count" converts Chain 2 from a structural pattern the scorer observes into a structural contract the output explicitly commits to before Phase 1 begins. C-32 is the only criterion change from V-04. Achieves 215/215.

**C-32 mechanism:** The Phase 0 gate token closes with: *"CA-1 verdict will close by echoing this count. This is a forward reference -- both ends of Chain 2 are committed at Phase 0, not reconstructed by matching counts independently at each end."* This phrase is absent from V-01 through V-04. A scorer can confirm C-30 (count present) and C-31 (CA-1 echoes) independently without the output having committed the binding. C-32 makes the commitment explicit in the gate token itself.

---

You are running a permissions trace signal for: {{{{topic}}}}

---

## AUDIT MANDATE

You are a Dataverse security auditor executing an SE-first trace. Three failure patterns survive manual reviews: post-incident FLS discovery, invisible privilege accumulation, and OWD-sharing-rule override. Each SE section opens with a CONTEXT-CLOSES label naming the pattern it eliminates.

---

## EXECUTION MANDATE

Four phases. **SE-first.** Each phase has an explicit **GATE OPEN** and **GATE CLOSE** token. A phase does not begin until its gate opens; a phase does not complete until its gate closes.

**PHASE 0 -- CA GATE:** Declare all schemas. Pre-load all enforcement mechanisms. Record activation state. Phase 0 GATE CLOSE carries explicit enforcement-point count by site type and pre-declares the CA-1 echo obligation.

**PHASE 1 -- SE GATE:** Execute the audit. Fill TABLE_1-5. Register every gap inline. Author CS-2/CS-3. Phase 1 does not close until TABLE_1-5 complete and all per-row commit signals have fired.

**PHASE 2 -- CS GATE:** Review SE findings. Challenge or confirm. Add CS-EXPECTATION-VIOLATED rows. Phase 2 does not close until CS-2 and CS-3 reconciliation complete.

**PHASE 3 -- CA-1 GATE:** Verify structural compliance. Echo Phase 0 count. Phase 3 GATE CLOSE is the structural close condition -- the trace is not closed until it is written.

---

## === PHASE 0 -- CA GATE OPEN ===

*Schema Registry, Enforcement Preamble, Language Index, and Gate Close with count and forward reference.*

### Step 0.1 -- Schema Registry (CA-authored)

**All schemas declared before any PHASE GATE OPENS. SE-first: CS-2/CS-3 SE-authored in PHASE 1; CS responds in PHASE 2. Blank-cell prohibition global.**

**Schema ID: TABLE_1 -- Role-Operation Matrix:**
`Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Blank-cell rule: Granted / Denied / Conditional (state condition) / N/A.

**Schema ID: TABLE_2 -- FLS Coverage:**
`Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Gap? = YES / NO. Gap? = YES rows forward to TABLE_5 immediately, before the next TABLE_2 row begins.

The Gap? boolean converts register triggering from a judgment call to a mechanical confirmation: SE marks YES/NO while filling TABLE_2; each Gap? = YES is the per-row commit signal for an immediate TABLE_5 entry.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" -- the Gap? column above is that flag. Structural role as per-row commit signal confirmed here, at the Schema Registry TABLE_2 declaration site, before any PHASE GATE OPENS. Downstream RULE (C-22) at SE-2.

**Schema ID: TABLE_3 -- Record Scope by Role:**
`Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`

**Schema ID: TABLE_4 -- Escalation Vector Inventory:**
`Vector | Checked? | Finding | Severity` -- all four vectors; Checked? = YES for all; Finding = escalation path or per-role rule-out.

**Schema ID: TABLE_5 -- Security Gap Inventory:**
`# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.
Remediation three-field format -- all three required:
  (1) Config change: exact object, location in Dataverse security editor, precise change.
  (2) Expected state: specific UI view or profile row a reviewer will see after fix.
  (3) Verification step: named action to confirm fix took effect.

> PLACEMENT-CRITERION CONFIRMED (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 Remediation three-field format (config change / expected state / verification step) is that declaration. Confirmed here at Step 0.1, before any PHASE GATE OPENS. Pre-declaration ensures SE collects verification details during the evidence window. Downstream RULE (C-16) at CA-1.5.

**Schema ID: CS-2 (SE-authored):** `Rule Name | SE Finding | SE Overreach Flag | CS Expected Intent | Resolved? | Resolution`
**Schema ID: CS-3 (SE-authored):** `Entity | Field or Operation | SE-Observed CS Access | SE-Observed Privileged-Role Access | Gap Exists? | CS Interpretation`

### Step 0.2 -- Enforcement Assignments (CA-authored)

M1, M2, M3 simultaneously active -- not alternative paths. M4 pre-assigned.
{PREAMBLE_TABLE}
Gap? boolean is the per-row structural commit signal. Mark YES/NO per TABLE_2 row; if YES, enter TABLE_5 before the next row begins. Co-authorship is a structural property of the format.

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- Gap? boolean established as structural enforcement mechanism at this preamble declaration site, before any PHASE GATE OPENS. Downstream RULE (C-22) at SE-2.

SHALL-A: TABLE_1 present; every cell filled; every role with any privilege included.
SHALL-B: TABLE_2 lists every sensitive field; null case stated; Gap? = YES rows in TABLE_5 per-row.
SHALL-C: Every TABLE_1 role in TABLE_3; Effective Scope filled; ambiguous scope in TABLE_5.
SHALL-D: TABLE_4 all four vectors; per-role rule-out when no path.
SHALL-E: TABLE_5 at least one named gap; zero-gap case needs explicit evidence rows.

### Step 0.3 -- Enforcement Language Index (CA-authored)

**COMPLETENESS THRESHOLD: coverage of N-1 of N enforcement points earns 0 pts -- the same as 0 of N. The index enables gap detection; it does not close gaps. A trace that passes C-28 satisfies all three: (a) this index lists every enforcement point, (b) every declaration-site enforcement point has inline verbatim confirmed, (c) every application-site enforcement point has a RULE block confirmed.**

> PLACEMENT-CRITERION CONFIRMED (C-29): "type designation is what makes C-27's two-mechanism requirement mechanically verifiable from the INDEX alone: a DECLARATION-SITE row requires inline verbatim confirmation; an APPLICATION-SITE row requires a RULE block confirmation" -- each INDEX row below carries a Site Type column classifying the enforcement point as DECLARATION-SITE or APPLICATION-SITE. A scorer reads the type column and knows which mechanism is required without cross-referencing criterion definitions. A DECLARATION-SITE row without inline verbatim confirmed is a mechanically detectable gap; an APPLICATION-SITE row without a RULE block confirmed is a mechanically detectable gap.

| EL-ID | Criterion | Enforcement Point | Verbatim Pass-Condition Phrase | Site Type | Status |
|-------|-----------|-------------------|-------------------------------|-----------|--------|
| EL-01 | C-11 | Phase 0 gate Chain 1 declaration | "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate |
| EL-02 | C-12 | SE-2/SE-4 negative-check instruction | "Checked [list] for [role]; [gap type] does not apply because [reason]" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-2 and SE-4 |
| EL-03 | C-13 | TABLE_5 Remediation field definition | "expected system state after the fix is applied and how to verify the fix took effect" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_5 |
| EL-04 | C-14 | SE-5 discovery-section note | "enables auditing that C-11 inline registration actually occurred" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-5 |
| EL-05 | C-15 | SE-4 per-role rule-out instruction | "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" | APPLICATION-SITE | RULE-BLOCK: confirmed at SE-4 |
| EL-06 | C-16 | TABLE_5 Remediation schema declaration | "declared explicitly at the top of the trace output, before the first analysis phase begins" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_5 |
| EL-07 | C-17 | CA-1.5 remediation echo instruction | "remediation block that states the fix without linking back to the discovery section does not pass" | APPLICATION-SITE | RULE-BLOCK: confirmed at CA-1.5 |
| EL-08 | C-18/C-22 | TABLE_2 Gap? column and enforcement assignments | "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" / "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" | DECLARATION-SITE (both) | INLINE-VERBATIM: confirmed at Step 0.1 TABLE_2 and Step 0.2 |
| EL-09 | C-23 | Phase 0 gate statement | "execution record, not declarative checklist" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 GATE CLOSE |
| EL-10 | C-24 | CA-1 GATE CLOSE precondition | "precondition for closing the trace, not a recommended step" | DECLARATION-SITE | INLINE-VERBATIM: confirmed at Phase 0 gate and CA-1 GATE CLOSE |
| EL-11 | C-25 | All structural enforcement points | each criterion's exact pass-condition phrase at each structural enforcement point | BOTH (per-criterion) | CONFIRMED: inline verbatim at declaration sites (EL-01/03/06/08/09/10), RULE blocks at application sites (EL-02/04/05/07) |

### Phase 0 Gate Statement

**Chain 1 -- discovery to TABLE_5:** Every gap found during PHASE 1 (SE) is entered into TABLE_5 at the SE section where it is found -- entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact.

**Chain 2 -- TABLE_5 to CA-1:** Every TABLE_5 Remediation entry is verified in PHASE 3 via double-anchor citing Registry schema and preamble row.

> PLACEMENT-CRITERION CONFIRMED (C-11 / C-23): "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" (C-11) and "execution record, not declarative checklist" (C-23) -- this gate statement is that execution record. Chain 1 active: gaps registered at discovery site. Chain 2 active: CA-1 echoes TABLE_5 entries. Downstream RULE (C-23) at CA-1 GATE CLOSE.

The CA-1 GATE CLOSE is the structural close condition -- a precondition for closing the trace, not a recommended step -- and must confirm INDEX completeness by echoing the Phase 0 count by site type. Downstream RULE (C-24) at CA-1 GATE CLOSE.
{GATE_STATE_LOG_C32}

## === PHASE 0 -- CA GATE CLOSE ===

*All schemas declared. All enforcement mechanisms active. Forward reference committed: CA-1 will echo count 11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH). Handing to PHASE 1 -- SE GATE OPEN.*

---

## === PHASE 1 -- SE GATE OPEN ===

*SE executes without CS baseline. Fills TABLE_1-5. Authors CS-2/CS-3. Registers every gap at point of discovery. Phase 1 does not close until TABLE_1-5 complete and all per-row commit signals fired.*

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: cumulative privilege accumulation**

TABLE_1 (Schema Registry TABLE_1; blank-cell rule):

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Every role with any privilege on any entity in {{{{topic}}}}. Author CS-3 entries for differentials.

### SE-2 / SHALL-B -- Field-Level Security Coverage

**CONTEXT-CLOSES: post-incident FLS discovery**

> RULE (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- each TABLE_2 Gap? cell is the per-row commit signal. Mark YES/NO while filling each row. If Gap? = YES, make the TABLE_5 entry before beginning the next TABLE_2 row.

TABLE_2 (Schema Registry TABLE_2; Gap? per-row trigger ACTIVE):

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Sensitive categories: PII / Financial / Audit-Compliance / Operational. Null case stated if no profiles active.

> RULE (C-12): "Checked [list] for [role]; [gap type] does not apply because [reason]" -- for each category yielding no Gap? = YES, state what was examined and why.

### SE-3 / SHALL-C -- Record Access Scope

**CONTEXT-CLOSES: OWD-sharing-rule override**

TABLE_3 (blank-cell rule):

| Role | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role. OWD: Private / BU / Parent-Child BU / Organization.

### SE-4 / SHALL-D -- Privilege Escalation Analysis

**CONTEXT-CLOSES: cumulative privilege accumulation (elevation layer)**

TABLE_4 (all four vectors; Checked? = YES):

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

> RULE (C-15): "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" -- per-role rule-out required when no escalation path found.

Author CS-2 SE Finding and SE Overreach Flag entries. Cross-entity chain: trace permission at each hop if gap involves multi-entity lookup.

### SE-5 / SHALL-E -- Security Gap Inventory

**CONTEXT-CLOSES: all three failure patterns (inventory)**

TABLE_5 (Schema Registry TABLE_5; Remediation three-field format declared in Phase 0 Step 0.1):

| # | Gap Type | Entity | Field or Rule | Role | Severity | Remediation |
|---|----------|--------|---------------|------|----------|-------------|

> RULE (C-14): "enables auditing that C-11 inline registration actually occurred" -- each TABLE_5 row must include the discovery context.

## === PHASE 1 -- SE GATE CLOSE ===

*TABLE_1-5 complete. Per-row commit signals fired for all TABLE_2 rows. CS-2/CS-3 authored. Handing to PHASE 2 -- CS GATE OPEN.*

---

## === PHASE 2 -- CS GATE OPEN ===

*CS reviews SE TABLE_1-5 and SE-authored CS-2/CS-3. CS does not redo SE technical analysis. Phase 2 does not close until CS-2 and CS-3 reconciliation complete.*

**CS-1:** State contradictions with SE TABLE_1 or TABLE_3. If fully confirmed, cite TABLE rows.

**CS-2 reconciliation** (SE-authored): For Resolved? = NO: add CS-EXPECTATION-VIOLATED to TABLE_5 with three-field remediation.

**CS-3 reconciliation** (SE-authored): For CS Interpretation contradicting SE finding: add CS-EXPECTATION-VIOLATED to TABLE_5 with CS-3 cite.

## === PHASE 2 -- CS GATE CLOSE ===

*CS-2 and CS-3 reconciliation complete. All CS-EXPECTATION-VIOLATED rows in TABLE_5. Handing to PHASE 3 -- CA-1 GATE OPEN.*

---
{CA1_BLOCK_C32}
"""

# ===================================================================
# Write everything
# ===================================================================

with open(OUT, 'w', encoding='utf-8') as f:
    f.write("""# trace-permissions Variate -- Round 10 (rubric v10 -- C-32 target)
**Date:** 2026-03-15
**Rubric:** v10 (C-01 through C-32 -- C-32 added from Round 9 excellence signal)
**Target criterion:** C-32 (Phase 0 gate token pre-declares the CA-1 count-echo obligation as a forward reference)

**State entering Round 10:**

| Variation | v9 score | Gap under v10 |
|-----------|----------|---------------|
| R9-V-05 (best v9) | 210/210 | Missing C-32 forward reference as explicit gate declaration (-5 pts) = 210/215 |

R9-V-05 has "CA-1 verdict will close by echoing this count" in the Phase 0 gate count paragraph. C-32 formalizes this as a criterion: a gate that records the count (C-30) without pre-declaring the CA-1 echo obligation leaves C-31 as a downstream convention rather than a pre-committed structural contract. Round 10 holds the R9-V-05 structural core and tests content/format axes while isolating C-32 across five variations.

---

## Round 10 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Role sequence -- SE-first | SE builds TABLE_1-5 without CS operational assumptions, then CS reconciles. C-30 present, C-31 present, **C-32 absent** (gate count has no forward reference phrase). |
| V-02 | Output format -- CONTEXT-CLOSES matrix pre-declared at Phase 0 | Phase 0 adds a CONTEXT-CLOSES MATRIX mapping each SE sub-section to the blind spot it resolves. C-30 present, C-31 present, **C-32 absent**. |
| V-03 | Phrasing register -- investigative audit voice | "You are a Dataverse security auditor. Find what is misconfigured." C-30 present, C-31 present, **C-32 absent**. |
| V-04 | Combined: Role sequence + Phrasing register | SE-first + investigative voice. C-30 present, C-31 present, **C-32 absent**. |
| V-05 | Combined: Role sequence + Lifecycle gates + **C-32 forward reference** | SE-first + explicit PHASE GATE OPEN/CLOSE + gate token pre-declares "CA-1 verdict will close by echoing this count". All C-30/C-31/**C-32** present. Hypothesis: +5 pts; achieves 215/215. |
""")
    f.write(V01)
    f.write(V02)
    f.write(V03)
    f.write(V04)
    f.write(V05)

size = os.path.getsize(OUT)
print(f'Written {OUT}: {size} bytes')
