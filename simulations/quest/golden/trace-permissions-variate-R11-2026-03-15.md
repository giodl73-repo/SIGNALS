# trace-permissions Variate -- Round 11 (rubric v10 -- v11 discovery round)
**Date:** 2026-03-15
**Rubric:** v10 (C-01 through C-32 -- all criteria at ceiling 215/215)
**Purpose:** Discovery round -- all 5 variations maintain full v10 compliance (215/215); each introduces a new structural feature as a v11 excellence signal candidate.

**State entering Round 11:**

| Variation | v10 score | New structural feature |
|-----------|-----------|------------------------|
| R10-V-05 (best v10) | 215/215 | Baseline |

All variations hold the R10-V-05 structural core (Phase 0 schema registry + enforcement index + C-32 forward reference). New features are additive.

---

## Round 11 Variation Map

| Variation | Axis | New Feature | Hypothesis |
|-----------|------|-------------|------------|
| V-01 | Inertia framing | ANTI-PATTERN REGISTRY (AP-1..AP-3) with CA-1 firing audit | AP firing audit converts inertia threat list from declaration to two-endpoint execution record |
| V-02 | Output format | TABLE_5 SOURCE-LINK column (Source Table / Source Row / Discovery Phase) | Source-link makes C-11 inline-registration mechanically verifiable by inter-table reference |
| V-03 | Lifecycle emphasis | CRITERION-PHASE-MAP pre-committed at Phase 0; CA-1 echoes per-criterion phase compliance | Phase coverage timeline contract makes late satisfaction mechanically detectable |
| V-04 | Inertia framing + Output format | AP-REGISTRY + TABLE_5 source-link, SE-first | Combined provenance and pattern-resolution; both chains mechanically auditable |
| V-05 | Full combination | SE-first + GATE tokens + AP-REGISTRY + TABLE_5 source-link + CRITERION-PHASE-MAP + C-32 | 215/215 + three v11 excellence signal candidates |

---

## V-01 -- Single-Axis: ANTI-PATTERN REGISTRY with CA-1 Firing Audit

**Axis:** Inertia framing -- Phase 0 pre-declares an ANTI-PATTERN REGISTRY mapping each blind spot to an SE section and reactive marker; CA-1 adds a FIRING AUDIT confirming each marker was resolved
**Hypothesis:** CONTEXT-CLOSES labels satisfy inertia framing structurally. But no current criterion requires CA-1 to confirm each label resolved its assigned anti-pattern. The AP firing audit creates a second endpoint: Phase 0 commits AP identifiers; CA-1 closes each. A trace where SE-2 omits its CONTEXT-CLOSES label is detectable by AP-1 FIRING AUDIT: NOT-FIRED -- without reading the full SE-2 section.
**C-32 forward reference:** PRESENT (CS-first, no GATE tokens)

---

You are running a permissions trace signal for: {{topic}}

---

## ANTI-PATTERN CONTEXT

Three anti-patterns defeat manual Dataverse security audits. Pre-registered with identifier, reactive marker, and assigned SE section.

**ANTI-PATTERN REGISTRY (Phase 0 pre-declaration):**

| AP-ID | Anti-Pattern | Reactive Marker | Assigned SE Section | CA-1 Audit |
|-------|--------------|-----------------|---------------------|------------|
| AP-1 | Post-incident FLS discovery | FLS-BLIND-SPOT-RESOLVED | SE-2 / SHALL-B | FIRED: SE-2 opened with AP-1 reactive marker? |
| AP-2 | Invisible privilege accumulation | PRIV-ACCUMULATION-RESOLVED | SE-1 + SE-4 / SHALL-A + SHALL-D | FIRED: SE-1 and SE-4 opened with AP-2 reactive marker? |
| AP-3 | OWD-sharing-rule override | OWD-OVERRIDE-RESOLVED | SE-3 / SHALL-C | FIRED: SE-3 opened with AP-3 reactive marker? |

> PLACEMENT-CRITERION CONFIRMED (C-21): ANTI-PATTERN REGISTRY is the named inertia threat section; AP-1 through AP-3 are the per-threat identifiers; reactive markers pre-committed. CA-1 ANTI-PATTERN FIRING AUDIT closes the execution record.

Each SE section opens with a CONTEXT-CLOSES label naming its AP-ID and firing its reactive marker.

---

## ROLE SEQUENCING MANDATE

Four phases. **CS-first.** Phase 0 gate closes with coverage count by site type and C-32 forward reference. CA-1 echoes Phase 0 count and includes ANTI-PATTERN FIRING AUDIT.

**PHASE 0 -- CA:** ANTI-PATTERN REGISTRY (above), Schema Registry (Step 0.1), Criterion Enforcement Matrix preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3), Phase 0 gate.
**PHASE 1 -- CS:** Qualitative access baseline and expectation tables. Does NOT fill TABLE_1-5.
**PHASE 2 -- SE:** Fills TABLE_1-5. Each sub-section opens with CONTEXT-CLOSES label naming AP-ID and firing reactive marker.
**PHASE 3 -- CA-1:** Double-anchor verification. Terminal verdict echoes Phase 0 count. ANTI-PATTERN FIRING AUDIT.

---

## PHASE 0 -- CA: SCHEMA REGISTRY, ENFORCEMENT PREAMBLE, AND LANGUAGE INDEX

### Step 0.1 -- Schema Registry (CA-authored)

**All schemas declared before PHASE 1. Blank-cell prohibition global.**

**Schema ID: TABLE_1 -- Role-Operation Matrix**
Declared columns: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope`
Blank-cell rule: Granted / Denied / Conditional (state condition) / N/A.

**Schema ID: TABLE_2 -- FLS Coverage**
Declared columns: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Gap? = YES / NO. Gap? = YES rows forward to TABLE_5 per-row, before next row begins.

The Gap? boolean converts register triggering from a judgment call to a mechanical confirmation: SE marks YES/NO while filling the table; each Gap? = YES is the per-row commit signal for an immediate TABLE_5 entry.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" -- Gap? column confirmed at TABLE_2 declaration site, before PHASE 1. Downstream RULE (C-22) at SE-2.

**Schema ID: TABLE_3 -- Record Scope by Role**
Declared columns: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`

**Schema ID: TABLE_4 -- Escalation Vector Inventory**
Declared columns: `Vector | Checked? | Finding | Severity` -- all four vectors; Checked? = YES for all.

**Schema ID: TABLE_5 -- Security Gap Inventory**
Declared columns: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.
Remediation three-field format (all three required):
  (1) Config change: exact object, location in Dataverse security editor, precise change.
  (2) Expected state: specific UI view or profile row a reviewer will see after fix.
  (3) Verification step: named action to confirm fix took effect.

> PLACEMENT-CRITERION CONFIRMED (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 three-field format declared at Step 0.1. Downstream RULE (C-16) at CA-1.5.

**Schema ID: CS-2:** `Rule Name | Trigger | Expected Access Granted | Intended for CS? | Potential Overreach? | SE Cross-Reference` -- "TBD."
**Schema ID: CS-3:** `Entity | Field or Operation | CS Expected Access | Privileged-Role Expected Access | Gap Expected? | SE Confirmation` -- "TBD."


### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored)

M1, M2, M3 simultaneously active -- not alternative paths. M4 pre-assigned.

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|----------------------|----------------------|-------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

Gap? boolean is the per-row structural commit signal. Co-authorship is a structural property of the format.

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- confirmed at preamble declaration site. Downstream RULE (C-22) at SE-2.

SHALL-A: TABLE_1 all roles, all cells. SHALL-B: TABLE_2 all sensitive fields, Gap? = YES rows per-row. SHALL-C: Every TABLE_1 role in TABLE_3. SHALL-D: TABLE_4 all four vectors, per-role rule-out. SHALL-E: TABLE_5 at least one named gap.


### Step 0.3 -- ENFORCEMENT LANGUAGE INDEX (CA-authored)

**COMPLETENESS THRESHOLD: coverage of N-1 of N enforcement points earns 0 pts -- the same as 0 of N.**

> PLACEMENT-CRITERION CONFIRMED (C-29): each INDEX row carries Site Type column. DECLARATION-SITE = inline verbatim required; APPLICATION-SITE = RULE block required.

| EL-ID | Criterion | Enforcement Point | Verbatim Pass-Condition Phrase | Site Type | Status |
|-------|-----------|-------------------|-------------------------------|-----------|--------|
| EL-01 | C-11 | Phase 0 gate Chain 1 | "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" | DECLARATION-SITE | INLINE-VERBATIM: Phase 0 gate |
| EL-02 | C-12 | SE-2/SE-4 negative-check | "Checked [list] for [role]; [gap type] does not apply because [reason]" | APPLICATION-SITE | RULE-BLOCK: SE-2 and SE-4 |
| EL-03 | C-13 | TABLE_5 Remediation field | "expected system state after the fix is applied and how to verify the fix took effect" | DECLARATION-SITE | INLINE-VERBATIM: Step 0.1 TABLE_5 |
| EL-04 | C-14 | SE-5 discovery note | "enables auditing that C-11 inline registration actually occurred" | APPLICATION-SITE | RULE-BLOCK: SE-5 |
| EL-05 | C-15 | SE-4 per-role rule-out | "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" | APPLICATION-SITE | RULE-BLOCK: SE-4 |
| EL-06 | C-16 | TABLE_5 schema declaration | "declared explicitly at the top of the trace output, before the first analysis phase begins" | DECLARATION-SITE | INLINE-VERBATIM: Step 0.1 TABLE_5 |
| EL-07 | C-17 | CA-1.5 remediation echo | "remediation block that states the fix without linking back to the discovery section does not pass" | APPLICATION-SITE | RULE-BLOCK: CA-1.5 |
| EL-08 | C-18/C-22 | TABLE_2 Gap? and preamble | "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" / "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" | DECLARATION-SITE (both) | INLINE-VERBATIM: Step 0.1 TABLE_2 and Step 0.2 |
| EL-09 | C-23 | Phase 0 gate | "execution record, not declarative checklist" | DECLARATION-SITE | INLINE-VERBATIM: Phase 0 gate |
| EL-10 | C-24 | CA-1 precondition | "precondition for closing the trace, not a recommended step" | DECLARATION-SITE | INLINE-VERBATIM: Phase 0 gate and CA-1 header |
| EL-11 | C-25 | All enforcement points | each criterion's exact pass-condition phrase at each structural enforcement point | BOTH | CONFIRMED |


### Phase 0 Gate Statement

Chain 1 -- discovery to TABLE_5: every gap found during PHASE 2 (SE) is entered into TABLE_5 at the section where it is found -- entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact.
Chain 2 -- TABLE_5 to CA-1: every TABLE_5 Remediation entry verified in PHASE 3 via double-anchor.

> PLACEMENT-CRITERION CONFIRMED (C-11 / C-23): C-11 verbatim and "execution record, not declarative checklist" (C-23). Downstream RULE (C-23) at CA-1 verdict.

CA-1 verdict is precondition -- not a recommended step. Downstream RULE (C-24).

**Phase 0 gate state log (execution record, not declarative checklist):**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Chain 1 -- discovery to TABLE_5, inline at discovery site | ACTIVE | Inline verbatim at Phase 0 gate (EL-01) |
| TABLE_5 Remediation three-field format | ACTIVE | Inline verbatim at Step 0.1 TABLE_5 (EL-06) |
| Gap? per-row boolean trigger | ACTIVE | Inline verbatim at Step 0.1 TABLE_2 + Step 0.2 (EL-08) |
| Chain 2 -- TABLE_5 to CA-1 double-anchor | ACTIVE | RULE blocks at CA-1.5 (EL-07) |
| ANTI-PATTERN REGISTRY 3/3 (AP-1 through AP-3, reactive markers pre-committed) | CONFIRMED | Pre-declared above; CA-1 FIRING AUDIT will close |
| ENFORCEMENT LANGUAGE INDEX 11/11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH) | CONFIRMED | Step 0.3; C-29 type column per-row |
| CA-1 verdict as precondition (with INDEX count echo and AP FIRING AUDIT) | ACTIVE | Inline verbatim at CA-1 header (EL-10) |

**Phase 0 coverage count: 11/11. 6 DECLARATION-SITE. 4 APPLICATION-SITE. 1 BOTH. CA-1 verdict will close by echoing this count. This is a forward reference: both ends of Chain 2 are committed at Phase 0, not reconstructed independently.**

*11/11 confirmed. AP-1/AP-2/AP-3 pre-declared. Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Lower-Trust Access Baseline

*CS does not fill TABLE_1-5.*

**CS-1:** For each entity: expected CRUD, record scope, sensitive fields, sharing rules relied on.
**CS-2:** TBD -- await SE. **CS-3:** TBD -- await SE.

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: AP-2 -- invisible privilege accumulation. Reactive marker: PRIV-ACCUMULATION-RESOLVED.**

TABLE_1 (blank-cell rule): `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` -- every role with any privilege on any entity in {{topic}}.

### SE-2 / SHALL-B -- Field-Level Security Coverage

**CONTEXT-CLOSES: AP-1 -- post-incident FLS discovery. Reactive marker: FLS-BLIND-SPOT-RESOLVED.**

> RULE (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- Gap? per-row commit signal. Mark YES/NO per row. If Gap? = YES, make the TABLE_5 entry before the next TABLE_2 row.

TABLE_2 (Gap? per-row trigger ACTIVE): `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`

> RULE (C-12): "Checked [list] for [role]; [gap type] does not apply because [reason]"

### SE-3 / SHALL-C -- Record Access Scope

**CONTEXT-CLOSES: AP-3 -- OWD-sharing-rule override. Reactive marker: OWD-OVERRIDE-RESOLVED.**

TABLE_3 (blank-cell rule): `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?` -- every TABLE_1 role.

### SE-4 / SHALL-D -- Privilege Escalation Analysis

**CONTEXT-CLOSES: AP-2 -- invisible privilege accumulation (elevation). Reactive marker: PRIV-ACCUMULATION-RESOLVED (escalation check).**

TABLE_4 (all four vectors; Checked? = YES): `Vector | Checked? | Finding | Severity`

> RULE (C-15): "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation"

### SE-5 / SHALL-E -- Security Gap Inventory

**CONTEXT-CLOSES: all three anti-patterns (inventory). AP-1 + AP-2 + AP-3 findings consolidated.**

TABLE_5 (three-field format per Step 0.1): `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`

> RULE (C-14): "enables auditing that C-11 inline registration actually occurred"

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*Precondition -- not a recommended step.*

**CA-1.1:** Registry TABLE_1. Preamble C-01/CA-1.1. -> PASS / FAIL
**CA-1.2:** Registry TABLE_2. Preamble C-02/CA-1.2. -> PASS / FAIL
**CA-1.3:** Registry TABLE_3. Preamble C-03/CA-1.3. -> PASS / FAIL
**CA-1.4:** Registry TABLE_4. Preamble C-04/CA-1.4. -> PASS / FAIL

**CA-1.5:** Registry TABLE_5. Preamble C-05/CA-1.5.

> RULE (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins"

> RULE (C-17): "remediation block that states the fix without linking back to the discovery section does not pass"

-> PASS / FAIL

**ANTI-PATTERN FIRING AUDIT (closes Phase 0 AP-REGISTRY forward reference):**

| AP-ID | Reactive Marker | Assigned SE Section | Status | Evidence |
|-------|-----------------|---------------------|--------|----------|
| AP-1 | FLS-BLIND-SPOT-RESOLVED | SE-2 | FIRED / NOT-FIRED | SE-2 CONTEXT-CLOSES label with AP-1 reactive marker present? |
| AP-2 | PRIV-ACCUMULATION-RESOLVED | SE-1 + SE-4 | FIRED / NOT-FIRED | SE-1 and SE-4 CONTEXT-CLOSES labels with AP-2 reactive marker present? |
| AP-3 | OWD-OVERRIDE-RESOLVED | SE-3 | FIRED / NOT-FIRED | SE-3 CONTEXT-CLOSES label with AP-3 reactive marker present? |

[AP NOT-FIRED: state which SE section failed to open with its assigned reactive marker. A trace with an unresolved AP has a named blind spot.]

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION (C-28 / C-31 / C-32):**

**INDEX: N/11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH). Matches Phase 0 gate count. CA-1 verdict will close by echoing this count. Forward reference committed at Phase 0 closed here.**

> RULE (C-24): "precondition for closing the trace, not a recommended step."

[TRACE CLOSED -- Phase 0 count echoed. AP FIRING AUDIT complete.]

---

## V-02 -- Single-Axis: TABLE_5 SOURCE-LINK Column

**Axis:** Output format -- TABLE_5 schema declaration gains three source-provenance columns (Source Table / Source Row / Discovery Phase) pre-declared at Phase 0; every TABLE_5 row states its inter-table provenance at fill time
**Hypothesis:** C-11 requires gaps to be registered inline at the discovery site, but the rubric confirms this by reading prose timing context. A TABLE_5 SOURCE-LINK column converts inline-registration from a timing requirement into a mechanically verifiable inter-table reference: a scorer confirms C-11 by checking Discovery Phase values -- no prose reading required. A row with Discovery Phase outside PHASE 2 SE-N is a mechanically detectable deferred registration.
**C-32 forward reference:** PRESENT (CS-first, no GATE tokens)

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: Why a Permissions Trace Is Not Optional

Three inertia patterns defeat manual security audits:

**Blind spot 1 -- Post-incident FLS discovery.** FLS gaps emerge after breaches. This trace replaces reactive discovery with pre-incident enumeration across PII, Financial, Audit-Compliance, and Operational fields.

**Blind spot 2 -- Cumulative privilege accumulation.** No single Dataverse UI view surfaces the combined effect of all security layers.

**Blind spot 3 -- OWD-sharing-rule override.** A Private OWD does not prevent a sharing rule from re-opening access.

Each SE section opens with a CONTEXT-CLOSES label.

---

## ROLE SEQUENCING MANDATE

Four phases. **CS-first.** Phase 0 gate closes with coverage count by site type and C-32 forward reference. CA-1 echoes Phase 0 count and includes SOURCE-LINK AUDIT.

**PHASE 0 -- CA:** Schema Registry with TABLE_5 SOURCE-LINK declared (Step 0.1), Criterion Enforcement Matrix preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3), Phase 0 gate.
**PHASE 1 -- CS:** Qualitative access baseline. Does NOT fill TABLE_1-5.
**PHASE 2 -- SE:** Fills TABLE_1-5. Every TABLE_5 entry carries SOURCE-LINK at fill time.
**PHASE 3 -- CA-1:** Double-anchor verification. SOURCE-LINK AUDIT confirms C-11 compliance by inter-table reference. Terminal verdict echoes Phase 0 count.

---

## PHASE 0 -- CA: SCHEMA REGISTRY, ENFORCEMENT PREAMBLE, AND LANGUAGE INDEX

### Step 0.1 -- Schema Registry (CA-authored)

**All schemas declared before PHASE 1. Blank-cell prohibition global.**

**Schema ID: TABLE_1:** `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` -- Granted / Denied / Conditional / N/A.

**Schema ID: TABLE_2:** `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Gap? = YES / NO. Gap? = YES rows forward to TABLE_5 per-row with SOURCE-LINK, before next row begins.

The Gap? boolean converts register triggering from a judgment call to a mechanical confirmation; each Gap? = YES is the per-row commit signal for an immediate TABLE_5 entry.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" -- Gap? column confirmed at TABLE_2 declaration site. Downstream RULE (C-22) at SE-2.

**Schema ID: TABLE_3:** `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
**Schema ID: TABLE_4:** `Vector | Checked? | Finding | Severity` -- all four vectors.

**Schema ID: TABLE_5:** `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation | Source Table | Source Row | Discovery Phase`
Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.
Remediation three-field format (all three required):
  (1) Config change: exact object, location, precise change.
  (2) Expected state: specific UI view or profile row after fix.
  (3) Verification step: named action to confirm fix.
Source provenance three-field format (all three required):
  Source Table: Schema ID of the table that triggered registration (TABLE_2, TABLE_4, CS-2, CS-3).
  Source Row: row identifier from source table.
  Discovery Phase: phase and section where this row was registered (e.g., "PHASE 2 SE-2"). A value outside PHASE 2 SE-N (for SE-authored rows) = deferred registration, C-11 FAIL.

> PLACEMENT-CRITERION CONFIRMED (C-16): TABLE_5 Remediation and SOURCE-LINK three-field formats declared at Step 0.1. Downstream RULE (C-16) at CA-1.5.

> PLACEMENT-CRITERION CONFIRMED (C-11): TABLE_5 SOURCE-LINK Discovery Phase is the per-row execution record. "PHASE 2 SE-N" confirms inline registration at discovery site -- mechanically verifiable without prose-reading.

**Schema ID: CS-2:** TBD. **Schema ID: CS-3:** TBD.


### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored)

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|----------------------|----------------------|-------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

Gap? boolean is the per-row structural commit signal. Co-authorship is a structural property of the format.

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- confirmed. Downstream RULE (C-22) at SE-2.

SHALL-A through SHALL-E: same as V-01. SHALL-B additionally requires SOURCE-LINK per Gap? = YES row.


### Step 0.3 -- ENFORCEMENT LANGUAGE INDEX (CA-authored)

**COMPLETENESS THRESHOLD: N-1 of N = 0 pts.**

> PLACEMENT-CRITERION CONFIRMED (C-29): each INDEX row carries Site Type column.

| EL-ID | Criterion | Enforcement Point | Verbatim Pass-Condition Phrase | Site Type | Status |
|-------|-----------|-------------------|-------------------------------|-----------|--------|
| EL-01 | C-11 | Phase 0 gate Chain 1 + TABLE_5 SOURCE-LINK | "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" | DECLARATION-SITE | INLINE-VERBATIM: Phase 0 gate and Step 0.1 TABLE_5 SOURCE-LINK |
| EL-02 | C-12 | SE-2/SE-4 negative-check | "Checked [list] for [role]; [gap type] does not apply because [reason]" | APPLICATION-SITE | RULE-BLOCK: SE-2 and SE-4 |
| EL-03 | C-13 | TABLE_5 Remediation field | "expected system state after the fix is applied and how to verify the fix took effect" | DECLARATION-SITE | INLINE-VERBATIM: Step 0.1 TABLE_5 |
| EL-04 | C-14 | SE-5 discovery note | "enables auditing that C-11 inline registration actually occurred" | APPLICATION-SITE | RULE-BLOCK: SE-5 |
| EL-05 | C-15 | SE-4 per-role rule-out | "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" | APPLICATION-SITE | RULE-BLOCK: SE-4 |
| EL-06 | C-16 | TABLE_5 schema declaration | "declared explicitly at the top of the trace output, before the first analysis phase begins" | DECLARATION-SITE | INLINE-VERBATIM: Step 0.1 TABLE_5 |
| EL-07 | C-17 | CA-1.5 remediation echo | "remediation block that states the fix without linking back to the discovery section does not pass" | APPLICATION-SITE | RULE-BLOCK: CA-1.5 |
| EL-08 | C-18/C-22 | TABLE_2 Gap? and preamble | "boolean flag..." / "co-authorship..." | DECLARATION-SITE (both) | INLINE-VERBATIM: Step 0.1 TABLE_2 and Step 0.2 |
| EL-09 | C-23 | Phase 0 gate | "execution record, not declarative checklist" | DECLARATION-SITE | INLINE-VERBATIM: Phase 0 gate |
| EL-10 | C-24 | CA-1 precondition | "precondition for closing the trace, not a recommended step" | DECLARATION-SITE | INLINE-VERBATIM: Phase 0 gate and CA-1 header |
| EL-11 | C-25 | All enforcement points | each criterion's exact pass-condition phrase at each structural enforcement point | BOTH | CONFIRMED |


### Phase 0 Gate Statement

Chain 1 -- discovery to TABLE_5: every gap found during PHASE 2 (SE) is entered into TABLE_5 at the section where it is found -- entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact. SOURCE-LINK Discovery Phase confirms phase of registration mechanically.
Chain 2 -- TABLE_5 to CA-1: every TABLE_5 Remediation entry verified in PHASE 3 via double-anchor.

> PLACEMENT-CRITERION CONFIRMED (C-11 / C-23): C-11 verbatim and "execution record, not declarative checklist" (C-23). SOURCE-LINK Discovery Phase is the per-row execution record. Downstream RULE (C-23) at CA-1 verdict.

CA-1 verdict is precondition -- not a recommended step. CA-1 SOURCE-LINK AUDIT will confirm no TABLE_5 row carries Discovery Phase outside PHASE 2 SE-N. Downstream RULE (C-24).

**Phase 0 gate state log (execution record, not declarative checklist):**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Chain 1 -- discovery to TABLE_5 with SOURCE-LINK at fill time | ACTIVE | Inline verbatim at Phase 0 gate (EL-01) and TABLE_5 SOURCE-LINK |
| TABLE_5 Remediation three-field format | ACTIVE | Inline verbatim at Step 0.1 TABLE_5 (EL-06) |
| TABLE_5 SOURCE-LINK three-field format | ACTIVE | Inline verbatim at Step 0.1 TABLE_5 SOURCE-LINK |
| Gap? per-row boolean trigger | ACTIVE | Inline verbatim at Step 0.1 TABLE_2 + Step 0.2 (EL-08) |
| Chain 2 -- TABLE_5 to CA-1 double-anchor | ACTIVE | RULE blocks at CA-1.5 (EL-07) |
| ENFORCEMENT LANGUAGE INDEX 11/11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH) | CONFIRMED | Step 0.3; C-29 type column per-row |
| CA-1 verdict as precondition (with INDEX count echo and SOURCE-LINK AUDIT) | ACTIVE | Inline verbatim at CA-1 header (EL-10) |

**Phase 0 coverage count: 11/11. 6 DECLARATION-SITE. 4 APPLICATION-SITE. 1 BOTH. CA-1 verdict will close by echoing this count. This is a forward reference: both ends of Chain 2 are committed at Phase 0, not reconstructed independently.**

*11/11 confirmed. SOURCE-LINK columns active. Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Lower-Trust Access Baseline

**CS-1:** For each entity: expected CRUD, record scope, sensitive fields, sharing rules relied on.
**CS-2:** TBD. **CS-3:** TBD.

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis

*Every TABLE_5 entry must include SOURCE-LINK (Source Table, Source Row, Discovery Phase = "PHASE 2 SE-N") at fill time.*

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: cumulative privilege accumulation**

TABLE_1: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` -- all roles, no blank cells.

### SE-2 / SHALL-B -- Field-Level Security Coverage

**CONTEXT-CLOSES: post-incident FLS discovery**

> RULE (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- Gap? per-row commit signal. If Gap? = YES, make TABLE_5 entry with SOURCE-LINK (Source Table = TABLE_2, Source Row = [row], Discovery Phase = "PHASE 2 SE-2") before next TABLE_2 row.

TABLE_2: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`

> RULE (C-12): "Checked [list] for [role]; [gap type] does not apply because [reason]"

### SE-3 / SHALL-C -- Record Access Scope

**CONTEXT-CLOSES: OWD-sharing-rule override**

TABLE_3: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?` -- every TABLE_1 role.

### SE-4 / SHALL-D -- Privilege Escalation Analysis

**CONTEXT-CLOSES: cumulative privilege accumulation (elevation)**

TABLE_4 (all four vectors; Checked? = YES): `Vector | Checked? | Finding | Severity`

> RULE (C-15): "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation"

TABLE_4 gaps: TABLE_5 entry with SOURCE-LINK (Source Table = TABLE_4, Discovery Phase = "PHASE 2 SE-4").

### SE-5 / SHALL-E -- Security Gap Inventory

**CONTEXT-CLOSES: all three blind spots (inventory)**

TABLE_5: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation | Source Table | Source Row | Discovery Phase`

> RULE (C-14): "enables auditing that C-11 inline registration actually occurred" -- Discovery Phase outside PHASE 2 SE-N = deferred registration.

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*Precondition -- not a recommended step.*

**CA-1.1:** Registry TABLE_1. Preamble C-01/CA-1.1. -> PASS / FAIL
**CA-1.2:** Registry TABLE_2. Preamble C-02/CA-1.2. -> PASS / FAIL
**CA-1.3:** Registry TABLE_3. Preamble C-03/CA-1.3. -> PASS / FAIL
**CA-1.4:** Registry TABLE_4. Preamble C-04/CA-1.4. -> PASS / FAIL

**CA-1.5:** Registry TABLE_5. Preamble C-05/CA-1.5.

> RULE (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins"

> RULE (C-17): "remediation block that states the fix without linking back to the discovery section does not pass"

-> PASS / FAIL

**SOURCE-LINK AUDIT (closes Phase 0 SOURCE-LINK forward reference):**

For each TABLE_5 row: verify Discovery Phase = "PHASE 2 SE-N" (SE-authored) or "PHASE 2 CS" (CS-EXPECTATION-VIOLATED). Any other value = deferred registration, C-11 FAIL for that row.

Summary: [N total TABLE_5 rows. N PHASE 2 SE rows. N PHASE 2 CS rows. N deferred (C-11 FAIL if any).]

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION (C-28 / C-31 / C-32):**

**INDEX: N/11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH). Matches Phase 0 count. Forward reference closed here.**

> RULE (C-24): "precondition for closing the trace, not a recommended step."

[TRACE CLOSED -- Phase 0 count echoed. SOURCE-LINK AUDIT complete.]

---

## V-03 -- Single-Axis: CRITERION-PHASE-MAP Pre-Commitment

**Axis:** Lifecycle emphasis -- Phase 0 pre-declares a CRITERION-PHASE-MAP table mapping each criterion to the phase where it is first satisfied; CA-1 audits per-criterion phase compliance
**Hypothesis:** The rubric confirms criteria are satisfied (PASS/FAIL) but not that they are satisfied at the right phase. A criterion satisfied one phase late is structurally different from a criterion passing correctly -- the CRITERION-PHASE-MAP makes late satisfaction mechanically detectable. Phase 0 commits "C-02 will first be satisfied at PHASE 2 SE-2." CA-1 audits: "C-02 at SE-2 -- honored." A PHASE-LATE result is detectable without reading the full trace.
**C-32 forward reference:** PRESENT (CS-first, no GATE tokens)

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: Why a Permissions Trace Is Not Optional

Three inertia patterns defeat manual security audits:

**Blind spot 1 -- Post-incident FLS discovery.** Replaces reactive discovery with pre-incident, categorized enumeration.

**Blind spot 2 -- Cumulative privilege accumulation.** Computes effective scope from all four security layers.

**Blind spot 3 -- OWD-sharing-rule override.** Cross-references OWD against every active sharing rule.

Each SE section opens with a CONTEXT-CLOSES label.

---

## ROLE SEQUENCING MANDATE

Four phases. **CS-first.** Phase 0 gate closes with coverage count, C-32 forward reference, and CRITERION-PHASE-MAP pre-commitment. CA-1 echoes Phase 0 count and audits CRITERION-PHASE-MAP.

**PHASE 0 -- CA:** Schema Registry (Step 0.1), Criterion Enforcement Matrix preamble (Step 0.2), ENFORCEMENT LANGUAGE INDEX (Step 0.3), CRITERION-PHASE-MAP (Step 0.4), Phase 0 gate.
**PHASE 1 -- CS:** Qualitative access baseline.
**PHASE 2 -- SE:** Fills TABLE_1-5. Each section satisfies criteria promised in the CRITERION-PHASE-MAP.
**PHASE 3 -- CA-1:** Double-anchor verification. CRITERION-PHASE-MAP AUDIT. Terminal verdict echoes Phase 0 count.

---

## PHASE 0 -- CA: SCHEMA REGISTRY, ENFORCEMENT PREAMBLE, LANGUAGE INDEX, AND CRITERION-PHASE-MAP

### Step 0.1 -- Schema Registry (CA-authored)

**All schemas declared before PHASE 1. Blank-cell prohibition global.**

**Schema ID: TABLE_1:** `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` -- Granted / Denied / Conditional / N/A.

**Schema ID: TABLE_2:** `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Gap? = YES / NO; Gap? = YES rows forward to TABLE_5 per-row.

The Gap? boolean converts register triggering from a judgment call to a mechanical confirmation; each Gap? = YES is the per-row commit signal for an immediate TABLE_5 entry.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" -- Gap? confirmed. Downstream RULE (C-22) at SE-2.

**Schema ID: TABLE_3:** `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
**Schema ID: TABLE_4:** `Vector | Checked? | Finding | Severity` -- all four vectors.
**Schema ID: TABLE_5:** `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`
Remediation three-field: (1) Config change. (2) Expected state. (3) Verification step.

> PLACEMENT-CRITERION CONFIRMED (C-16): TABLE_5 format declared at Step 0.1. Downstream RULE (C-16) at CA-1.5.

**Schema ID: CS-2:** TBD. **Schema ID: CS-3:** TBD.


### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored)

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|----------------------|----------------------|-------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

Gap? boolean is the per-row structural commit signal. Co-authorship is a structural property of the format.

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- confirmed. Downstream RULE (C-22) at SE-2.

SHALL-A: all roles, all cells. SHALL-B: all sensitive fields, Gap? = YES rows per-row. SHALL-C: every TABLE_1 role in TABLE_3. SHALL-D: all four vectors, per-role rule-out. SHALL-E: at least one named gap.


### Step 0.3 -- ENFORCEMENT LANGUAGE INDEX (CA-authored)

**COMPLETENESS THRESHOLD: N-1 of N = 0 pts.**

> PLACEMENT-CRITERION CONFIRMED (C-29): each INDEX row carries Site Type column.

| EL-ID | Criterion | Enforcement Point | Verbatim Pass-Condition Phrase | Site Type | Status |
|-------|-----------|-------------------|-------------------------------|-----------|--------|
| EL-01 | C-11 | Phase 0 gate Chain 1 | "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" | DECLARATION-SITE | INLINE-VERBATIM: Phase 0 gate |
| EL-02 | C-12 | SE-2/SE-4 negative-check | "Checked [list] for [role]; [gap type] does not apply because [reason]" | APPLICATION-SITE | RULE-BLOCK: SE-2 and SE-4 |
| EL-03 | C-13 | TABLE_5 Remediation field | "expected system state after the fix is applied and how to verify the fix took effect" | DECLARATION-SITE | INLINE-VERBATIM: Step 0.1 TABLE_5 |
| EL-04 | C-14 | SE-5 discovery note | "enables auditing that C-11 inline registration actually occurred" | APPLICATION-SITE | RULE-BLOCK: SE-5 |
| EL-05 | C-15 | SE-4 per-role rule-out | "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" | APPLICATION-SITE | RULE-BLOCK: SE-4 |
| EL-06 | C-16 | TABLE_5 schema declaration | "declared explicitly at the top of the trace output, before the first analysis phase begins" | DECLARATION-SITE | INLINE-VERBATIM: Step 0.1 TABLE_5 |
| EL-07 | C-17 | CA-1.5 remediation echo | "remediation block that states the fix without linking back to the discovery section does not pass" | APPLICATION-SITE | RULE-BLOCK: CA-1.5 |
| EL-08 | C-18/C-22 | TABLE_2 Gap? and preamble | "boolean flag..." / "co-authorship..." | DECLARATION-SITE (both) | INLINE-VERBATIM: Step 0.1 TABLE_2 and Step 0.2 |
| EL-09 | C-23 | Phase 0 gate | "execution record, not declarative checklist" | DECLARATION-SITE | INLINE-VERBATIM: Phase 0 gate |
| EL-10 | C-24 | CA-1 precondition | "precondition for closing the trace, not a recommended step" | DECLARATION-SITE | INLINE-VERBATIM: Phase 0 gate and CA-1 header |
| EL-11 | C-25 | All enforcement points | each criterion's exact pass-condition phrase at each structural enforcement point | BOTH | CONFIRMED |


### Step 0.4 -- CRITERION-PHASE-MAP (CA-authored)

**Pre-commitment: each criterion maps to the phase where it is first satisfied. CA-1 audits whether each promised phase was honored. A criterion satisfied at a later phase = PHASE-LATE deviation -- structurally detectable.**

| Criterion | Tier | Promised Phase | Mechanism | CA-1 Audit Row |
|-----------|------|----------------|-----------|----------------|
| C-01 | Essential | PHASE 2 SE-1 | TABLE_1 | CA-1.1 |
| C-02 | Essential | PHASE 2 SE-2 | TABLE_2 + Gap? trigger | CA-1.2 |
| C-03 | Essential | PHASE 2 SE-3 | TABLE_3 | CA-1.3 |
| C-04 | Essential | PHASE 2 SE-4 | TABLE_4 | CA-1.4 |
| C-05 | Recommended | PHASE 2 SE-5 | TABLE_5 | CA-1.5 |
| C-06 | Recommended | PHASE 2 SE-4 | TABLE_4 team gap row | CA-1.4 |
| C-07 | Recommended | PHASE 2 SE-4 | TABLE_4 escalation chain | CA-1.4 |
| C-08..C-25 | Aspirational | PHASE 0 or PHASE 2 | Schema Registry, preamble, RULE blocks | INDEX |
| C-26..C-32 | Aspirational | PHASE 0 | Enforcement Language Index + gate | INDEX |

**Phase 0 forward reference: CA-1 CRITERION-PHASE-MAP AUDIT will verify each promised phase was honored.**


### Phase 0 Gate Statement

Chain 1 -- discovery to TABLE_5: every gap found during PHASE 2 (SE) is entered into TABLE_5 at the section where it is found -- entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact.
Chain 2 -- TABLE_5 to CA-1: every TABLE_5 Remediation entry verified in PHASE 3 via double-anchor.

> PLACEMENT-CRITERION CONFIRMED (C-11 / C-23): C-11 verbatim and "execution record, not declarative checklist" (C-23). Downstream RULE (C-23) at CA-1 verdict.

CA-1 verdict is precondition -- not a recommended step. Downstream RULE (C-24).

**Phase 0 gate state log (execution record, not declarative checklist):**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Chain 1 -- discovery to TABLE_5, inline at discovery site | ACTIVE | Inline verbatim at Phase 0 gate (EL-01) |
| TABLE_5 Remediation three-field format | ACTIVE | Inline verbatim at Step 0.1 TABLE_5 (EL-06) |
| Gap? per-row boolean trigger | ACTIVE | Inline verbatim at Step 0.1 TABLE_2 + Step 0.2 (EL-08) |
| Chain 2 -- TABLE_5 to CA-1 double-anchor | ACTIVE | RULE blocks at CA-1.5 (EL-07) |
| CRITERION-PHASE-MAP 7+ criteria with promised phases | CONFIRMED | Step 0.4; CA-1 PHASE-MAP AUDIT will close |
| ENFORCEMENT LANGUAGE INDEX 11/11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH) | CONFIRMED | Step 0.3 |
| CA-1 verdict as precondition (with INDEX count echo and PHASE-MAP AUDIT) | ACTIVE | Inline verbatim at CA-1 header (EL-10) |

**Phase 0 coverage count: 11/11. 6 DECLARATION-SITE. 4 APPLICATION-SITE. 1 BOTH. CA-1 verdict will close by echoing this count. This is a forward reference: both ends of Chain 2 are committed at Phase 0, not reconstructed independently.**

*11/11 confirmed. CRITERION-PHASE-MAP active. Handing to PHASE 1 -- CS.*

---

## PHASE 1 -- CS: Lower-Trust Access Baseline

**CS-1:** For each entity: expected CRUD, record scope, sensitive fields, sharing rules.
**CS-2:** TBD. **CS-3:** TBD.

*Handing to PHASE 2 -- SE.*

---

## PHASE 2 -- SE: Security Analysis

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: cumulative privilege accumulation** | **CRITERION-PHASE-MAP: C-01 promised PHASE 2 SE-1**

TABLE_1: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` -- all roles, no blank cells.

### SE-2 / SHALL-B -- Field-Level Security Coverage

**CONTEXT-CLOSES: post-incident FLS discovery** | **CRITERION-PHASE-MAP: C-02 promised PHASE 2 SE-2**

> RULE (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- Gap? per-row commit signal.

TABLE_2: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`

> RULE (C-12): "Checked [list] for [role]; [gap type] does not apply because [reason]"

### SE-3 / SHALL-C -- Record Access Scope

**CONTEXT-CLOSES: OWD-sharing-rule override** | **CRITERION-PHASE-MAP: C-03 promised PHASE 2 SE-3**

TABLE_3: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`

### SE-4 / SHALL-D -- Privilege Escalation Analysis

**CONTEXT-CLOSES: cumulative privilege accumulation (elevation)** | **CRITERION-PHASE-MAP: C-04/C-06/C-07 promised PHASE 2 SE-4**

TABLE_4 (all four vectors; Checked? = YES): `Vector | Checked? | Finding | Severity`

> RULE (C-15): "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation"

### SE-5 / SHALL-E -- Security Gap Inventory

**CONTEXT-CLOSES: all three blind spots** | **CRITERION-PHASE-MAP: C-05 promised PHASE 2 SE-5**

TABLE_5: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation`

> RULE (C-14): "enables auditing that C-11 inline registration actually occurred"

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*Precondition -- not a recommended step.*

**CA-1.1:** Registry TABLE_1. Preamble C-01/CA-1.1. PHASE-MAP: C-01 promised PHASE 2 SE-1 -- honored? -> PASS / FAIL / PHASE-LATE
**CA-1.2:** Registry TABLE_2. Preamble C-02/CA-1.2. PHASE-MAP: C-02 promised PHASE 2 SE-2 -- honored? -> PASS / FAIL / PHASE-LATE
**CA-1.3:** Registry TABLE_3. Preamble C-03/CA-1.3. PHASE-MAP: C-03 promised PHASE 2 SE-3. -> PASS / FAIL / PHASE-LATE
**CA-1.4:** Registry TABLE_4. Preamble C-04/CA-1.4. PHASE-MAP: C-04/C-06/C-07 promised PHASE 2 SE-4. -> PASS / FAIL / PHASE-LATE

**CA-1.5:** Registry TABLE_5. Preamble C-05/CA-1.5. PHASE-MAP: C-05 promised PHASE 2 SE-5.

> RULE (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins"

> RULE (C-17): "remediation block that states the fix without linking back to the discovery section does not pass"

-> PASS / FAIL / PHASE-LATE

**CRITERION-PHASE-MAP AUDIT (closes Phase 0 CRITERION-PHASE-MAP forward reference):**

| Criterion | Promised Phase | Actual Phase | Phase Honored? |
|-----------|----------------|--------------|----------------|
| C-01 | PHASE 2 SE-1 | [actual] | YES / PHASE-LATE |
| C-02 | PHASE 2 SE-2 | [actual] | YES / PHASE-LATE |
| C-03 | PHASE 2 SE-3 | [actual] | YES / PHASE-LATE |
| C-04 | PHASE 2 SE-4 | [actual] | YES / PHASE-LATE |
| C-05 | PHASE 2 SE-5 | [actual] | YES / PHASE-LATE |
| C-06 | PHASE 2 SE-4 | [actual] | YES / PHASE-LATE |
| C-07 | PHASE 2 SE-4 | [actual] | YES / PHASE-LATE |

[PHASE-LATE = criterion eventually satisfied but not at promised phase.]

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION (C-28 / C-31 / C-32):**

**INDEX: N/11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH). Matches Phase 0 count. Forward reference closed here.**

> RULE (C-24): "precondition for closing the trace, not a recommended step."

[TRACE CLOSED -- Phase 0 count echoed. CRITERION-PHASE-MAP AUDIT complete.]

---

## V-04 -- Two-Axis: ANTI-PATTERN REGISTRY + TABLE_5 Source-Link, SE-First

**Axes:** Inertia framing (ANTI-PATTERN REGISTRY with CA-1 firing audit) + Output format (TABLE_5 SOURCE-LINK column) + Role sequence (SE-first)
**Hypothesis:** AP REGISTRY proves each blind spot was addressed by a named SE section. TABLE_5 SOURCE-LINK proves each gap was registered inline. SE-first ensures TABLE_1 is built without CS operational assumptions constraining role coverage. Combined, these make anti-pattern resolution and discovery provenance both mechanically auditable -- two independent claims about output quality that cannot be spoofed by reordering prose.
**C-32 forward reference:** PRESENT (SE-first, no GATE tokens)

---

You are running a permissions trace signal for: {{topic}}

---

## ANTI-PATTERN CONTEXT

Three anti-patterns defeat manual Dataverse security audits.

**ANTI-PATTERN REGISTRY (Phase 0 pre-declaration):**

| AP-ID | Anti-Pattern | Reactive Marker | Assigned SE Section | CA-1 Audit |
|-------|--------------|-----------------|---------------------|------------|
| AP-1 | Post-incident FLS discovery | FLS-BLIND-SPOT-RESOLVED | SE-2 | FIRED / NOT-FIRED |
| AP-2 | Invisible privilege accumulation | PRIV-ACCUMULATION-RESOLVED | SE-1 + SE-4 | FIRED / NOT-FIRED |
| AP-3 | OWD-sharing-rule override | OWD-OVERRIDE-RESOLVED | SE-3 | FIRED / NOT-FIRED |

> PLACEMENT-CRITERION CONFIRMED (C-21): ANTI-PATTERN REGISTRY is the named inertia threat section; AP identifiers and reactive markers pre-committed. CA-1 FIRING AUDIT closes the execution record.

---

## ROLE SEQUENCING MANDATE

Four phases. **SE-first.** Phase 0 gate closes with coverage count and C-32 forward reference. CA-1 includes AP FIRING AUDIT and SOURCE-LINK AUDIT.

**PHASE 0 -- CA:** ANTI-PATTERN REGISTRY (above), Schema Registry with TABLE_5 SOURCE-LINK (Step 0.1), Enforcement preamble (Step 0.2), INDEX (Step 0.3), Phase 0 gate.
**PHASE 1 -- SE:** Fills TABLE_1-5. Opens each section with CONTEXT-CLOSES + AP reactive marker. Every TABLE_5 row carries SOURCE-LINK at fill time. Authors CS-2/CS-3.
**PHASE 2 -- CS:** Reviews SE findings. Challenges or confirms. Adds CS-EXPECTATION-VIOLATED rows with SOURCE-LINK.
**PHASE 3 -- CA-1:** Double-anchor verification. AP FIRING AUDIT. SOURCE-LINK AUDIT. Echoes Phase 0 count.

---

## PHASE 0 -- CA: SCHEMA REGISTRY, ENFORCEMENT PREAMBLE, AND LANGUAGE INDEX

### Step 0.1 -- Schema Registry (CA-authored)

**SE-first: CS-2 and CS-3 SE-authored in PHASE 1. Blank-cell prohibition global.**

**Schema ID: TABLE_1:** `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` -- Granted / Denied / Conditional / N/A.

**Schema ID: TABLE_2:** `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Gap? boolean converts register triggering from a judgment call to a mechanical confirmation; each Gap? = YES is the per-row commit signal for an immediate TABLE_5 entry with SOURCE-LINK.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" -- Gap? confirmed. Downstream RULE (C-22) at SE-2.

**Schema ID: TABLE_3:** `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
**Schema ID: TABLE_4:** `Vector | Checked? | Finding | Severity` -- all four; Checked? = YES.

**Schema ID: TABLE_5:** `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation | Source Table | Source Row | Discovery Phase`
Remediation three-field: (1) Config change. (2) Expected state. (3) Verification step.
Source provenance three-field: Source Table = Schema ID of triggering table. Source Row = row that triggered registration. Discovery Phase = "PHASE 1 SE-N". Discovery Phase = "PHASE 2" or later = deferred registration, C-11 FAIL.

> PLACEMENT-CRITERION CONFIRMED (C-16): TABLE_5 formats declared here before PHASE 1 (SE). Downstream RULE (C-16) at CA-1.5.

**Schema ID: CS-2 (SE-authored):** `Rule Name | SE Finding | SE Overreach Flag | CS Expected Intent | Resolved? | Resolution`
**Schema ID: CS-3 (SE-authored):** `Entity | Field or Operation | SE-Observed CS Access | SE-Observed Privileged-Role Access | Gap Exists? | CS Interpretation`


### Step 0.2 -- Criterion Enforcement Matrix Preamble (CA-authored)

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|----------------------|----------------------|-------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

Gap? boolean is the per-row commit signal. Co-authorship is a structural property of the format.

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- confirmed. Downstream RULE (C-22) at SE-2.

SHALL-A: all roles, all cells. SHALL-B: all sensitive fields, Gap? = YES rows per-row with SOURCE-LINK. SHALL-C: every TABLE_1 role in TABLE_3. SHALL-D: all four vectors, per-role rule-out. SHALL-E: at least one named gap with SOURCE-LINK.


### Step 0.3 -- ENFORCEMENT LANGUAGE INDEX (CA-authored)

**COMPLETENESS THRESHOLD: N-1 of N = 0 pts.**

> PLACEMENT-CRITERION CONFIRMED (C-29): Site Type column per INDEX row.

| EL-ID | Criterion | Enforcement Point | Verbatim Pass-Condition Phrase | Site Type | Status |
|-------|-----------|-------------------|-------------------------------|-----------|--------|
| EL-01 | C-11 | Phase 0 gate Chain 1 + TABLE_5 SOURCE-LINK | "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" | DECLARATION-SITE | INLINE-VERBATIM: Phase 0 gate and Step 0.1 TABLE_5 SOURCE-LINK |
| EL-02 | C-12 | SE-2/SE-4 negative-check | "Checked [list] for [role]; [gap type] does not apply because [reason]" | APPLICATION-SITE | RULE-BLOCK: SE-2 and SE-4 |
| EL-03 | C-13 | TABLE_5 Remediation field | "expected system state after the fix is applied and how to verify the fix took effect" | DECLARATION-SITE | INLINE-VERBATIM: Step 0.1 TABLE_5 |
| EL-04 | C-14 | SE-5 discovery note | "enables auditing that C-11 inline registration actually occurred" | APPLICATION-SITE | RULE-BLOCK: SE-5 |
| EL-05 | C-15 | SE-4 per-role rule-out | "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" | APPLICATION-SITE | RULE-BLOCK: SE-4 |
| EL-06 | C-16 | TABLE_5 schema declaration | "declared explicitly at the top of the trace output, before the first analysis phase begins" | DECLARATION-SITE | INLINE-VERBATIM: Step 0.1 TABLE_5 |
| EL-07 | C-17 | CA-1.5 remediation echo | "remediation block that states the fix without linking back to the discovery section does not pass" | APPLICATION-SITE | RULE-BLOCK: CA-1.5 |
| EL-08 | C-18/C-22 | TABLE_2 Gap? and preamble | "boolean flag..." / "co-authorship..." | DECLARATION-SITE (both) | INLINE-VERBATIM: Step 0.1 TABLE_2 and Step 0.2 |
| EL-09 | C-23 | Phase 0 gate | "execution record, not declarative checklist" | DECLARATION-SITE | INLINE-VERBATIM: Phase 0 gate |
| EL-10 | C-24 | CA-1 precondition | "precondition for closing the trace, not a recommended step" | DECLARATION-SITE | INLINE-VERBATIM: Phase 0 gate and CA-1 header |
| EL-11 | C-25 | All enforcement points | each criterion's exact pass-condition phrase at each structural enforcement point | BOTH | CONFIRMED |


### Phase 0 Gate Statement

Chain 1 -- discovery to TABLE_5: every gap found during PHASE 1 (SE) is entered into TABLE_5 at the SE section where it is found -- entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact. SOURCE-LINK Discovery Phase = "PHASE 1 SE-N" at every SE-authored TABLE_5 row.
Chain 2 -- TABLE_5 to CA-1: every TABLE_5 Remediation entry verified in PHASE 3 via double-anchor.

> PLACEMENT-CRITERION CONFIRMED (C-11 / C-23): C-11 verbatim and "execution record, not declarative checklist" (C-23). SOURCE-LINK is the per-row execution record. Downstream RULE (C-23) at CA-1 verdict.

CA-1 verdict is precondition -- not a recommended step. Downstream RULE (C-24).

**Phase 0 gate state log (execution record, not declarative checklist):**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Chain 1 -- discovery to TABLE_5 with SOURCE-LINK (SE-first) | ACTIVE | Inline verbatim at Phase 0 gate (EL-01) and TABLE_5 SOURCE-LINK |
| TABLE_5 Remediation three-field format | ACTIVE | Inline verbatim at Step 0.1 (EL-06) |
| TABLE_5 SOURCE-LINK three-field format | ACTIVE | Inline verbatim at Step 0.1 TABLE_5 |
| Gap? per-row boolean trigger | ACTIVE | Inline verbatim at Step 0.1 TABLE_2 + Step 0.2 (EL-08) |
| Chain 2 -- TABLE_5 to CA-1 | ACTIVE | RULE blocks at CA-1.5 (EL-07) |
| ANTI-PATTERN REGISTRY 3/3 (AP-1 through AP-3) | CONFIRMED | Pre-declared above; CA-1 FIRING AUDIT closes |
| ENFORCEMENT LANGUAGE INDEX 11/11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH) | CONFIRMED | Step 0.3 |
| CA-1 verdict as precondition (with INDEX count echo, AP FIRING AUDIT, SOURCE-LINK AUDIT) | ACTIVE | Inline verbatim at CA-1 header (EL-10) |

**Phase 0 coverage count: 11/11. 6 DECLARATION-SITE. 4 APPLICATION-SITE. 1 BOTH. CA-1 verdict will close by echoing this count. This is a forward reference: both ends of Chain 2 are committed at Phase 0, not reconstructed independently.**

*11/11 confirmed. SE-first. AP-1/AP-2/AP-3 pre-declared. SOURCE-LINK active. Handing to PHASE 1 -- SE.*

---

## PHASE 1 -- SE: Security Analysis (SE-first)

*SE executes without CS baseline. Fills TABLE_1-5 including SOURCE-LINK per row. Authors CS-2/CS-3.*

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: AP-2 -- invisible privilege accumulation. Reactive marker: PRIV-ACCUMULATION-RESOLVED.**

TABLE_1: `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` -- every role in {{topic}}.

### SE-2 / SHALL-B -- Field-Level Security Coverage

**CONTEXT-CLOSES: AP-1 -- post-incident FLS discovery. Reactive marker: FLS-BLIND-SPOT-RESOLVED.**

> RULE (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- Gap? per-row commit signal. If Gap? = YES, make TABLE_5 entry with SOURCE-LINK (Source Table = TABLE_2, Source Row = [row], Discovery Phase = "PHASE 1 SE-2") before next TABLE_2 row.

TABLE_2: `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`

> RULE (C-12): "Checked [list] for [role]; [gap type] does not apply because [reason]"

### SE-3 / SHALL-C -- Record Access Scope

**CONTEXT-CLOSES: AP-3 -- OWD-sharing-rule override. Reactive marker: OWD-OVERRIDE-RESOLVED.**

TABLE_3: `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`

### SE-4 / SHALL-D -- Privilege Escalation Analysis

**CONTEXT-CLOSES: AP-2 -- invisible privilege accumulation (elevation). Reactive marker: PRIV-ACCUMULATION-RESOLVED (escalation check).**

TABLE_4 (all four vectors; Checked? = YES): `Vector | Checked? | Finding | Severity`

> RULE (C-15): "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation"

TABLE_4 gaps: TABLE_5 entry with SOURCE-LINK (Source Table = TABLE_4, Discovery Phase = "PHASE 1 SE-4").

### SE-5 / SHALL-E -- Security Gap Inventory

**CONTEXT-CLOSES: all three anti-patterns (inventory).**

TABLE_5: `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation | Source Table | Source Row | Discovery Phase`

> RULE (C-14): "enables auditing that C-11 inline registration actually occurred" -- Discovery Phase outside PHASE 1 SE-N = deferred registration.

---

## PHASE 2 -- CS: Expectation Reconciliation

*Reviews SE TABLE_1-5 and SE-authored CS-2/CS-3.*

**CS-1:** State contradictions.
**CS-2 reconciliation:** Resolved? = NO -> CS-EXPECTATION-VIOLATED in TABLE_5 with SOURCE-LINK (Source Table = CS-2, Discovery Phase = "PHASE 2 CS").
**CS-3 reconciliation:** Contradictions -> CS-EXPECTATION-VIOLATED with SOURCE-LINK.

*Handing to PHASE 3 -- CA-1.*

---

## PHASE 3 -- CA-1: Double-Anchor Format Compliance Verification

*Precondition -- not a recommended step.*

**CA-1.1:** Registry TABLE_1. Preamble C-01/CA-1.1. -> PASS / FAIL
**CA-1.2:** Registry TABLE_2. Preamble C-02/CA-1.2. -> PASS / FAIL
**CA-1.3:** Registry TABLE_3. Preamble C-03/CA-1.3. -> PASS / FAIL
**CA-1.4:** Registry TABLE_4. Preamble C-04/CA-1.4. -> PASS / FAIL

**CA-1.5:** Registry TABLE_5. Preamble C-05/CA-1.5.

> RULE (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins"

> RULE (C-17): "remediation block that states the fix without linking back to the discovery section does not pass"

-> PASS / FAIL

**ANTI-PATTERN FIRING AUDIT:**

| AP-ID | Reactive Marker | Assigned SE Section | Status | Evidence |
|-------|-----------------|---------------------|--------|----------|
| AP-1 | FLS-BLIND-SPOT-RESOLVED | SE-2 | FIRED / NOT-FIRED | SE-2 CONTEXT-CLOSES label with AP-1 reactive marker? |
| AP-2 | PRIV-ACCUMULATION-RESOLVED | SE-1 + SE-4 | FIRED / NOT-FIRED | SE-1 and SE-4 CONTEXT-CLOSES with AP-2 reactive marker? |
| AP-3 | OWD-OVERRIDE-RESOLVED | SE-3 | FIRED / NOT-FIRED | SE-3 CONTEXT-CLOSES with AP-3 reactive marker? |

**SOURCE-LINK AUDIT:**

For each TABLE_5 row: Discovery Phase = "PHASE 1 SE-N" (SE rows) or "PHASE 2 CS" (CS-EXPECTATION-VIOLATED). Any other = C-11 FAIL.

Summary: [N total. N PHASE 1. N PHASE 2 CS. N deferred (C-11 FAIL if any).]

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION (C-28 / C-31 / C-32):**

**INDEX: N/11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH). Matches Phase 0 count. Forward reference closed here.**

> RULE (C-24): "precondition for closing the trace, not a recommended step."

[TRACE CLOSED -- AP FIRING AUDIT complete. SOURCE-LINK AUDIT complete. Phase 0 count echoed.]

---

## V-05 -- Full Combination: SE-First + GATE Tokens + ANTI-PATTERN REGISTRY + TABLE_5 Source-Link + CRITERION-PHASE-MAP + C-32

**Axes:** Role sequence (SE-first) + Lifecycle emphasis (PHASE GATE OPEN/CLOSE tokens + CRITERION-PHASE-MAP) + Inertia framing (ANTI-PATTERN REGISTRY with CA-1 firing audit) + Output format (TABLE_5 SOURCE-LINK column)
**Hypothesis:** Full combination. All three new structural features alongside the R10-V-05 core. ANTI-PATTERN REGISTRY firing audit converts inertia threats from declarations into a two-endpoint execution record. TABLE_5 SOURCE-LINK converts inline-registration from a timing claim into a mechanically verifiable inter-table reference. CRITERION-PHASE-MAP converts criterion coverage from pass/fail into a phase-timeline contract. Three structurally independent claims about output quality, all auditable without prose-reading. Achieves 215/215 + surfaces three v11 excellence signal candidates.
**C-32 forward reference:** PRESENT

---

You are running a permissions trace signal for: {{topic}}

---

## ANTI-PATTERN CONTEXT

Three anti-patterns defeat manual Dataverse security audits.

**ANTI-PATTERN REGISTRY (Phase 0 pre-declaration):**

| AP-ID | Anti-Pattern | Reactive Marker | Assigned SE Section | CA-1 Audit |
|-------|--------------|-----------------|---------------------|------------|
| AP-1 | Post-incident FLS discovery | FLS-BLIND-SPOT-RESOLVED | SE-2 | FIRED / NOT-FIRED |
| AP-2 | Invisible privilege accumulation | PRIV-ACCUMULATION-RESOLVED | SE-1 + SE-4 | FIRED / NOT-FIRED |
| AP-3 | OWD-sharing-rule override | OWD-OVERRIDE-RESOLVED | SE-3 | FIRED / NOT-FIRED |

> PLACEMENT-CRITERION CONFIRMED (C-21): ANTI-PATTERN REGISTRY is the named inertia threat section; AP identifiers and reactive markers pre-committed; CA-1 FIRING AUDIT closes the execution record.

---

## EXECUTION MANDATE

Four phases. **SE-first.** Each phase has an explicit **GATE OPEN** and **GATE CLOSE** token.

**PHASE 0 -- CA GATE:** Declare all schemas (TABLE_5 with SOURCE-LINK), pre-load enforcement mechanisms, pre-declare CRITERION-PHASE-MAP. GATE CLOSE carries enforcement-point count by site type, C-32 forward reference, and AP/SOURCE-LINK/PHASE-MAP audit commitments.

**PHASE 1 -- SE GATE:** Execute audit. Fill TABLE_1-5. Each SE section opens with CONTEXT-CLOSES + AP reactive marker. Every TABLE_5 row carries SOURCE-LINK at fill time. Phase 1 does not close until TABLE_1-5 complete.

**PHASE 2 -- CS GATE:** Review SE findings. Challenge or confirm. Add CS-EXPECTATION-VIOLATED rows. Phase 2 does not close until CS-2 and CS-3 reconciliation complete.

**PHASE 3 -- CA-1 GATE:** Verify structural compliance. AP FIRING AUDIT. SOURCE-LINK AUDIT. CRITERION-PHASE-MAP AUDIT. Echo Phase 0 count. GATE CLOSE is the structural close condition.

---

## === PHASE 0 -- CA GATE OPEN ===

### Step 0.1 -- Schema Registry (CA-authored)

**All schemas declared before any PHASE GATE OPENS. SE-first. Blank-cell prohibition global.**

**Schema ID: TABLE_1:** `Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope` -- Granted / Denied / Conditional (state condition) / N/A.

**Schema ID: TABLE_2:** `Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap?`
Gap? = YES / NO. Gap? = YES rows forward to TABLE_5 immediately with SOURCE-LINK, before next row begins.

The Gap? boolean converts register triggering from a judgment call to a mechanical confirmation: SE marks YES/NO while filling TABLE_2; each Gap? = YES is the per-row commit signal for an immediate TABLE_5 entry.

> PLACEMENT-CRITERION CONFIRMED (C-18 / C-22): "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" -- Gap? confirmed at TABLE_2 declaration site, before any PHASE GATE OPENS. Downstream RULE (C-22) at SE-2.

**Schema ID: TABLE_3:** `Role | OWD Baseline | Scope Modifier | Effective Scope | Verified?`
**Schema ID: TABLE_4:** `Vector | Checked? | Finding | Severity` -- all four vectors; Checked? = YES.

**Schema ID: TABLE_5:** `# | Gap Type | Entity | Field or Rule | Role | Severity | Remediation | Source Table | Source Row | Discovery Phase`
Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / OVER-PERMISSIONED / CS-EXPECTATION-VIOLATED.
Remediation three-field (all three required): (1) Config change. (2) Expected state. (3) Verification step.
Source provenance three-field (all three required):
  Source Table: Schema ID of triggering table.
  Source Row: row identifier from source table.
  Discovery Phase: "PHASE 1 SE-N" for SE-authored rows; "PHASE 2 CS" for CS-EXPECTATION-VIOLATED. Any other = C-11 FAIL.

> PLACEMENT-CRITERION CONFIRMED (C-16): TABLE_5 formats declared at Step 0.1, before any PHASE GATE OPENS. Downstream RULE (C-16) at CA-1.5.

> PLACEMENT-CRITERION CONFIRMED (C-11): TABLE_5 SOURCE-LINK Discovery Phase is the per-row execution record. "PHASE 1 SE-N" confirms inline registration -- mechanically verifiable without prose-reading.

**Schema ID: CS-2 (SE-authored):** `Rule Name | SE Finding | SE Overreach Flag | CS Expected Intent | Resolved? | Resolution`
**Schema ID: CS-3 (SE-authored):** `Entity | Field or Operation | SE-Observed CS Access | SE-Observed Privileged-Role Access | Gap Exists? | CS Interpretation`


### Step 0.2 -- Enforcement Assignments (CA-authored)

| Criterion | M1: Format Schema | M2: Role Sub-Section | M3: SHALL Obligation | M4: CA Verification Row |
|-----------|-------------------|----------------------|----------------------|-------------------------|
| C-01 | TABLE_1 | SE-1 | SHALL-A | CA-1.1 |
| C-02 | TABLE_2 | SE-2 | SHALL-B | CA-1.2 |
| C-03 | TABLE_3 | SE-1 + SE-3 | SHALL-C | CA-1.3 |
| C-04 | TABLE_4 | SE-4 | SHALL-D | CA-1.4 |
| C-05 | TABLE_5 | SE-5 | SHALL-E | CA-1.5 |

Gap? boolean is the per-row structural commit signal. Co-authorship is a structural property of the format.

> PLACEMENT-CRITERION CONFIRMED (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- confirmed before any PHASE GATE OPENS. Downstream RULE (C-22) at SE-2.

SHALL-A: all roles, all cells. SHALL-B: all sensitive fields, Gap? = YES rows per-row with SOURCE-LINK. SHALL-C: every TABLE_1 role in TABLE_3. SHALL-D: all four vectors, per-role rule-out. SHALL-E: at least one named gap with SOURCE-LINK.


### Step 0.3 -- Enforcement Language Index (CA-authored)

**COMPLETENESS THRESHOLD: N-1 of N = 0 pts. A trace that passes C-28 satisfies all three: (a) this index lists every enforcement point, (b) every declaration-site enforcement point has inline verbatim confirmed, (c) every application-site enforcement point has a RULE block confirmed.**

> PLACEMENT-CRITERION CONFIRMED (C-29): each INDEX row carries Site Type column.

| EL-ID | Criterion | Enforcement Point | Verbatim Pass-Condition Phrase | Site Type | Status |
|-------|-----------|-------------------|-------------------------------|-----------|--------|
| EL-01 | C-11 | Phase 0 gate Chain 1 + TABLE_5 SOURCE-LINK | "entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact" | DECLARATION-SITE | INLINE-VERBATIM: Phase 0 gate and Step 0.1 TABLE_5 SOURCE-LINK |
| EL-02 | C-12 | SE-2/SE-4 negative-check | "Checked [list] for [role]; [gap type] does not apply because [reason]" | APPLICATION-SITE | RULE-BLOCK: SE-2 and SE-4 |
| EL-03 | C-13 | TABLE_5 Remediation field | "expected system state after the fix is applied and how to verify the fix took effect" | DECLARATION-SITE | INLINE-VERBATIM: Step 0.1 TABLE_5 |
| EL-04 | C-14 | SE-5 discovery note | "enables auditing that C-11 inline registration actually occurred" | APPLICATION-SITE | RULE-BLOCK: SE-5 |
| EL-05 | C-15 | SE-4 per-role rule-out | "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation" | APPLICATION-SITE | RULE-BLOCK: SE-4 |
| EL-06 | C-16 | TABLE_5 schema declaration | "declared explicitly at the top of the trace output, before the first analysis phase begins" | DECLARATION-SITE | INLINE-VERBATIM: Step 0.1 TABLE_5 |
| EL-07 | C-17 | CA-1.5 remediation echo | "remediation block that states the fix without linking back to the discovery section does not pass" | APPLICATION-SITE | RULE-BLOCK: CA-1.5 |
| EL-08 | C-18/C-22 | TABLE_2 Gap? and enforcement assignments | "boolean flag in a structured table converts register triggering from a judgment call to a mechanical confirmation" / "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" | DECLARATION-SITE (both) | INLINE-VERBATIM: Step 0.1 TABLE_2 and Step 0.2 |
| EL-09 | C-23 | Phase 0 gate | "execution record, not declarative checklist" | DECLARATION-SITE | INLINE-VERBATIM: Phase 0 GATE CLOSE |
| EL-10 | C-24 | CA-1 GATE CLOSE precondition | "precondition for closing the trace, not a recommended step" | DECLARATION-SITE | INLINE-VERBATIM: Phase 0 gate and CA-1 GATE CLOSE header |
| EL-11 | C-25 | All structural enforcement points | each criterion's exact pass-condition phrase at each structural enforcement point | BOTH (per-criterion) | CONFIRMED: inline verbatim at declaration sites (EL-01/03/06/08/09/10), RULE blocks at application sites (EL-02/04/05/07) |


### Step 0.4 -- CRITERION-PHASE-MAP (CA-authored)

**Pre-commitment: each criterion maps to the phase where it is first satisfied. CA-1 audits whether each promised phase was honored.**

| Criterion | Tier | Promised Phase | Mechanism | CA-1 Check |
|-----------|------|----------------|-----------|------------|
| C-01 | Essential | PHASE 1 SE-1 | TABLE_1 | CA-1.1 |
| C-02 | Essential | PHASE 1 SE-2 | TABLE_2 + Gap? trigger + SOURCE-LINK | CA-1.2 |
| C-03 | Essential | PHASE 1 SE-3 | TABLE_3 | CA-1.3 |
| C-04 | Essential | PHASE 1 SE-4 | TABLE_4 | CA-1.4 |
| C-05 | Recommended | PHASE 1 SE-5 | TABLE_5 | CA-1.5 |
| C-06 | Recommended | PHASE 1 SE-4 | TABLE_4 team gap row | CA-1.4 |
| C-07 | Recommended | PHASE 1 SE-4 | TABLE_4 escalation chain | CA-1.4 |
| C-08..C-25 | Aspirational | PHASE 0 or PHASE 1 | Schema Registry, preamble, RULE blocks | INDEX |
| C-26..C-32 | Aspirational | PHASE 0 | Enforcement Language Index + gate | INDEX |

**Phase 0 forward reference: CA-1 CRITERION-PHASE-MAP AUDIT will verify each promised phase was honored.**


### Phase 0 Gate Statement

**Chain 1:** Every gap found during PHASE 1 (SE) is entered into TABLE_5 at the SE section where it is found -- entered into the findings log at that point in the output -- not deferred to a summary section compiled after the fact. SOURCE-LINK Discovery Phase = "PHASE 1 SE-N" at every SE-authored TABLE_5 row.

**Chain 2:** Every TABLE_5 Remediation entry is verified in PHASE 3 via double-anchor.

> PLACEMENT-CRITERION CONFIRMED (C-11 / C-23): C-11 verbatim and "execution record, not declarative checklist" (C-23). SOURCE-LINK Discovery Phase is the per-row execution record. Chain 1 active. Chain 2 active. Downstream RULE (C-23) at CA-1 GATE CLOSE.

CA-1 GATE CLOSE is the structural close condition -- a precondition for closing the trace, not a recommended step. Downstream RULE (C-24).

**Phase 0 gate state log (execution record, not declarative checklist):**

| Mechanism | State | Confirmation |
|-----------|-------|--------------|
| Chain 1 -- discovery to TABLE_5 with SOURCE-LINK (SE-first) | ACTIVE | Inline verbatim at Phase 0 gate (EL-01) and TABLE_5 SOURCE-LINK |
| TABLE_5 Remediation three-field format | ACTIVE | Inline verbatim at Step 0.1 TABLE_5 (EL-06) |
| TABLE_5 SOURCE-LINK three-field format | ACTIVE | Inline verbatim at Step 0.1 TABLE_5 SOURCE-LINK |
| Gap? per-row boolean trigger | ACTIVE | Inline verbatim at Step 0.1 TABLE_2 + Step 0.2 (EL-08) |
| Chain 2 -- TABLE_5 to CA-1 double-anchor | ACTIVE | RULE blocks at CA-1.5 (EL-07) |
| ANTI-PATTERN REGISTRY 3/3 (AP-1 through AP-3) | CONFIRMED | Pre-declared above; CA-1 FIRING AUDIT closes |
| CRITERION-PHASE-MAP 7+ criteria with promised phases | CONFIRMED | Step 0.4; CA-1 PHASE-MAP AUDIT closes |
| ENFORCEMENT LANGUAGE INDEX 11/11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH) | CONFIRMED | Step 0.3; C-29 type column per-row; count binds INDEX to gate token |
| CA-1 GATE CLOSE as precondition (with INDEX count echo, AP FIRING AUDIT, SOURCE-LINK AUDIT, PHASE-MAP AUDIT) | ACTIVE | Inline verbatim at CA-1 GATE CLOSE header (EL-10) |

**Phase 0 coverage count: 11/11. 6 DECLARATION-SITE (EL-01/03/06/08/09/10). 4 APPLICATION-SITE (EL-02/04/05/07). 1 BOTH (EL-11). Discrepancy between this count and INDEX row total is structurally visible. CA-1 verdict will close by echoing this count. This is a forward reference: both ends of Chain 2 are committed at Phase 0 close, not reconstructed independently at each end. A gate with the count and a CA-1 with the echo, but without this pre-declaration, leave the binding inferred by the scorer rather than declared by the output.**


## === PHASE 0 -- CA GATE CLOSE ===

*All schemas declared including TABLE_5 SOURCE-LINK. All enforcement mechanisms active. ANTI-PATTERN REGISTRY committed. CRITERION-PHASE-MAP committed. Forward references committed: CA-1 will echo count 11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH), close AP FIRING AUDIT, close SOURCE-LINK AUDIT, close PHASE-MAP AUDIT. Handing to PHASE 1 -- SE GATE OPEN.*

---

## === PHASE 1 -- SE GATE OPEN ===

*SE executes without CS baseline. Fills TABLE_1-5 including SOURCE-LINK per row. Authors CS-2/CS-3. Registers every gap at point of discovery. Phase 1 does not close until TABLE_1-5 complete and all per-row commit signals fired.*

### SE-1 / SHALL-A -- Role-Operation Matrix

**CONTEXT-CLOSES: AP-2 -- invisible privilege accumulation. Reactive marker: PRIV-ACCUMULATION-RESOLVED.** | **CRITERION-PHASE-MAP: C-01 promised PHASE 1 SE-1.**

TABLE_1 (blank-cell rule):

| Role | Create | Read | Write | Delete | Append | AppendTo | Assign | Share | Record Scope |
|------|--------|------|-------|--------|--------|----------|--------|-------|--------------|

Every role with any privilege on any entity in {{topic}}. Author CS-3 entries for differentials.

### SE-2 / SHALL-B -- Field-Level Security Coverage

**CONTEXT-CLOSES: AP-1 -- post-incident FLS discovery. Reactive marker: FLS-BLIND-SPOT-RESOLVED.** | **CRITERION-PHASE-MAP: C-02 promised PHASE 1 SE-2.**

> RULE (C-22): "co-authorship is a structural property of the format and trigger completeness is provable from the output alone" -- Gap? per-row commit signal. Mark YES/NO per row. If Gap? = YES, make TABLE_5 entry (SOURCE-LINK: Source Table = TABLE_2, Source Row = [row], Discovery Phase = "PHASE 1 SE-2") before beginning the next TABLE_2 row.

TABLE_2 (Gap? per-row trigger ACTIVE):

| Entity | Field | Category | FLS Profile Configured? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|------------------------|-------------|--------------|------|

Sensitive categories: PII / Financial / Audit-Compliance / Operational. Null case stated if no profiles active.

> RULE (C-12): "Checked [list] for [role]; [gap type] does not apply because [reason]"

### SE-3 / SHALL-C -- Record Access Scope

**CONTEXT-CLOSES: AP-3 -- OWD-sharing-rule override. Reactive marker: OWD-OVERRIDE-RESOLVED.** | **CRITERION-PHASE-MAP: C-03 promised PHASE 1 SE-3.**

TABLE_3 (blank-cell rule):

| Role | OWD Baseline | Scope Modifier | Effective Scope | Verified? |
|------|--------------|----------------|-----------------|-----------|

Every TABLE_1 role. OWD: Private / BU / Parent-Child BU / Organization.

### SE-4 / SHALL-D -- Privilege Escalation Analysis

**CONTEXT-CLOSES: AP-2 -- invisible privilege accumulation (elevation). Reactive marker: PRIV-ACCUMULATION-RESOLVED (escalation check).** | **CRITERION-PHASE-MAP: C-04/C-06/C-07 promised PHASE 1 SE-4.**

TABLE_4 (all four vectors; Checked? = YES):

| Vector | Checked? | Finding | Severity |
|--------|----------|---------|----------|
| Team inheritance | YES | | |
| Sharing rules | YES | | |
| Impersonation (Act on Behalf Of) | YES | | |
| Admin / environment role override | YES | | |

> RULE (C-15): "one explicit rule-out per traced role -- naming the specific actions checked for that role and why none permit elevation"

TABLE_4 gap rows: TABLE_5 entry with SOURCE-LINK (Source Table = TABLE_4, Discovery Phase = "PHASE 1 SE-4"). Author CS-2 SE Finding and SE Overreach Flag entries.

### SE-5 / SHALL-E -- Security Gap Inventory

**CONTEXT-CLOSES: all three anti-patterns (inventory). AP-1 + AP-2 + AP-3 consolidated.** | **CRITERION-PHASE-MAP: C-05 promised PHASE 1 SE-5.**

TABLE_5 (Remediation three-field + SOURCE-LINK three-field per Step 0.1):

| # | Gap Type | Entity | Field or Rule | Role | Severity | Remediation | Source Table | Source Row | Discovery Phase |
|---|----------|--------|---------------|------|----------|-------------|--------------|------------|-----------------|

> RULE (C-14): "enables auditing that C-11 inline registration actually occurred" -- Discovery Phase outside PHASE 1 SE-N (or PHASE 2 CS for CS-EXPECTATION-VIOLATED) = deferred registration.

## === PHASE 1 -- SE GATE CLOSE ===

*TABLE_1-5 complete. Per-row commit signals fired. SOURCE-LINK on every TABLE_5 row. CS-2/CS-3 authored. Handing to PHASE 2 -- CS GATE OPEN.*

---

## === PHASE 2 -- CS GATE OPEN ===

*CS reviews SE TABLE_1-5 and SE-authored CS-2/CS-3. Phase 2 does not close until CS-2 and CS-3 reconciliation complete.*

**CS-1:** State contradictions with SE TABLE_1 or TABLE_3.

**CS-2 reconciliation:** Resolved? = NO -> CS-EXPECTATION-VIOLATED in TABLE_5 with SOURCE-LINK (Source Table = CS-2, Discovery Phase = "PHASE 2 CS").

**CS-3 reconciliation:** CS Interpretation contradicting SE -> CS-EXPECTATION-VIOLATED in TABLE_5 with SOURCE-LINK (Source Table = CS-3, Discovery Phase = "PHASE 2 CS").

## === PHASE 2 -- CS GATE CLOSE ===

*CS-2 and CS-3 reconciliation complete. Handing to PHASE 3 -- CA-1 GATE OPEN.*

---

## === PHASE 3 -- CA-1 GATE OPEN ===

*The trace is not closed until CA-1 GATE CLOSE is written. Writing it is the precondition -- not a recommended step.*

**CA-1.1 -- C-01:** Registry TABLE_1. Preamble C-01/CA-1.1. PHASE-MAP: C-01 promised PHASE 1 SE-1 -- honored? -> PASS / FAIL / PHASE-LATE

**CA-1.2 -- C-02:** Registry TABLE_2. Preamble C-02/CA-1.2. PHASE-MAP: C-02 promised PHASE 1 SE-2 -- honored? -> PASS / FAIL / PHASE-LATE

**CA-1.3:** Registry TABLE_3. Preamble C-03/CA-1.3. PHASE-MAP: C-03 PHASE 1 SE-3. -> PASS / FAIL / PHASE-LATE
**CA-1.4:** Registry TABLE_4. Preamble C-04/CA-1.4. PHASE-MAP: C-04/C-06/C-07 PHASE 1 SE-4. -> PASS / FAIL / PHASE-LATE

**CA-1.5 -- C-05:** Registry TABLE_5. Preamble C-05/CA-1.5. PHASE-MAP: C-05 PHASE 1 SE-5 -- honored?

> RULE (C-16): "declared explicitly at the top of the trace output, before the first analysis phase begins" -- TABLE_5 formats at Step 0.1 before PHASE 1 GATE OPEN.

> RULE (C-17): "remediation block that states the fix without linking back to the discovery section does not pass"

-> PASS / FAIL / PHASE-LATE

**ANTI-PATTERN FIRING AUDIT (closes Phase 0 AP-REGISTRY forward reference):**

| AP-ID | Reactive Marker | Assigned SE Section | Status | Evidence |
|-------|-----------------|---------------------|--------|----------|
| AP-1 | FLS-BLIND-SPOT-RESOLVED | SE-2 | FIRED / NOT-FIRED | SE-2 opened with AP-1 CONTEXT-CLOSES + reactive marker? |
| AP-2 | PRIV-ACCUMULATION-RESOLVED | SE-1 + SE-4 | FIRED / NOT-FIRED | SE-1 and SE-4 opened with AP-2 CONTEXT-CLOSES + reactive marker? |
| AP-3 | OWD-OVERRIDE-RESOLVED | SE-3 | FIRED / NOT-FIRED | SE-3 opened with AP-3 CONTEXT-CLOSES + reactive marker? |

[AP NOT-FIRED = unresolved anti-pattern. State which SE section failed.]

**SOURCE-LINK AUDIT (closes Phase 0 SOURCE-LINK forward reference):**

For each TABLE_5 row: Discovery Phase = "PHASE 1 SE-N" or "PHASE 2 CS". Any other = C-11 FAIL.

Summary: [N total. N PHASE 1 SE rows. N PHASE 2 CS rows. N deferred rows (C-11 FAIL if any).]

**CRITERION-PHASE-MAP AUDIT (closes Phase 0 CRITERION-PHASE-MAP forward reference):**

| Criterion | Promised Phase | Actual Phase | Phase Honored? |
|-----------|----------------|--------------|----------------|
| C-01 | PHASE 1 SE-1 | [actual] | YES / PHASE-LATE |
| C-02 | PHASE 1 SE-2 | [actual] | YES / PHASE-LATE |
| C-03 | PHASE 1 SE-3 | [actual] | YES / PHASE-LATE |
| C-04 | PHASE 1 SE-4 | [actual] | YES / PHASE-LATE |
| C-05 | PHASE 1 SE-5 | [actual] | YES / PHASE-LATE |
| C-06 | PHASE 1 SE-4 | [actual] | YES / PHASE-LATE |
| C-07 | PHASE 1 SE-4 | [actual] | YES / PHASE-LATE |

**CA Format Compliance Verdict -- citing Phase 0:**

> RULE (C-23): "execution record, not declarative checklist" -- Phase 0 gate recorded confirmed activation and pre-declared all forward references. This verdict confirms execution matched and closes all three forward references.

**ENFORCEMENT LANGUAGE INDEX COMPLETENESS CONFIRMATION (C-28 / C-31 / C-32):**
[For each EL-01 through EL-11: confirm STATUS CONFIRMED or flag UNCONFIRMED.]

**INDEX completeness confirmed: N/11 (6 DECLARATION-SITE, 4 APPLICATION-SITE, 1 BOTH). Matches Phase 0 gate count. Full-chain provability confirmed -- Phase 0 opened with this count and pre-declared this echo; CA-1 closes by confirming the count was maintained through the trace. Forward reference committed at Phase 0 closed here at CA-1.**

[C-28 = FAIL if N < 11. C-31 = FAIL if count not echoed. C-32 = FAIL if Phase 0 gate token did not contain the forward-reference phrase.]

[C-01 through C-05 PASS/FAIL/PHASE-LATE disposition. Overall: COMPLIANT / NON-COMPLIANT.]

## === PHASE 3 -- CA-1 GATE CLOSE ===

*Precondition for closing the trace, not a recommended step. CA-1 verdict written. Phase 0 count echoed. AP FIRING AUDIT closed. SOURCE-LINK AUDIT closed. CRITERION-PHASE-MAP AUDIT closed. All three Phase 0 forward references resolved. Full-chain provability confirmed.*

[TRACE CLOSED.]
