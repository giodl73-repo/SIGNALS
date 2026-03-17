# trace-permissions Variate -- Round 10 (rubric v9 -- C-28/C-29 stress-test)
**Date:** 2026-03-15
**Rubric:** v9 (C-01 through C-29 -- C-28/C-29 added from Round 9 excellence signals)
**Target criteria:** C-28 (protocol-class state-semantic differentiation with activation-class-appropriate broken-obligation semantics), C-29 (phase-anchored broken-obligation detection point in PENDING protocol declarations)

**State entering Round 10:**

| Variation | R9 v9 score | Notes |
|-----------|-------------|-------|
| R9-V-04 (best v9) | 195/200 | C-28 + C-29 pass; 5-pt gap candidate: activation-point enumeration specificity in Per-Stage body block |
| R9-V-01 | 190/200 | C-28 passes (ACTIVE state correct); C-29 fails (no phase-anchored detection point in STEP-1-CLOSE-TOKEN broken-obligation note) |

Round 10 holds the V-04-R9 structural core -- Phase 0 body blocks: STEP-1-CLOSE-TOKEN PENDING with Phase 5b detection anchor; Per-Stage Chain-Reminder ACTIVE with LIVE GAPS REGISTER first activation -- and stress-tests C-28/C-29 survival across three surface axes (role sequence, inertia framing, output format). None of the axes removes the body block content required for C-28/C-29.

---

## Round 10 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Single-axis: Role sequence -- SE executes Phase 1c FLS steps before CS validates in a sub-pass; Phase 0 body blocks and ACTIVATION STATE LOG unchanged | C-28/C-29 live entirely in Phase 0 body blocks. Phase 1c execution order does not affect STEP-1-CLOSE-TOKEN PENDING state at Phase 0 close, Per-Stage Chain-Reminder ACTIVE state, or the LIVE GAPS REGISTER first-activation anchor. PENDING->RESOLVED fires at Phase 1c Step 1 close regardless of authorship sequence. Hypothesis: C-28/C-29 unchanged; 195/200 maintained. |
| V-02 | Single-axis: Inertia framing -- CONTEXT preamble added before Phase 0, naming three manual-RBAC-audit blind spots by ID and naming the status-quo tool displaced | Motivational framing adds no structural elements to Phase 0. STEP-1-CLOSE-TOKEN PENDING and Per-Stage Chain-Reminder ACTIVE are Phase 0 declarations -- pre-Phase 0 framing does not affect them. Tests whether blind-spot naming improves C-04 (escalation depth) and C-08 (remediation specificity). Hypothesis: C-28/C-29 unchanged; potential C-04/C-08 gain. |
| V-03 | Single-axis: Output format -- PROTOCOL REGISTRY table replaces prose body blocks; all C-26/C-28/C-29 required fields (Activation Class, State, Activation Points, Broken-Obligation Note, Detection Phase) appear as explicit table columns; LOG rows reference REGISTRY-IDs | Tests whether C-26/C-28/C-29 criteria are content-dependent or require prose block form. Table encoding carries identical semantic content: PENDING state, phase-anchored broken-obligation note with Phase 5b detection, ACTIVE state with FLS ENTRY activation points, state-class assignment. Hypothesis: table encoding satisfies C-26/C-28/C-29; 195/200 maintained. |
| V-04 | Combined A+B: SE-first + inertia framing | V-01 + V-02. Non-overlapping axes: V-01 modifies Phase 1c execution order; V-02 adds pre-Phase 0 framing. Phase 0 body blocks unchanged. Tests whether composition introduces interaction effects on C-28/C-29. Hypothesis: C-28/C-29 unchanged from V-01; potential C-04/C-08 gain from V-02. |
| V-05 | Combined B+C + rubric-verbatim C-28/C-29 language: inertia framing + PROTOCOL REGISTRY table + C-28 activation-class labels as column header identifiers + C-29 exact detection phrase in Broken-Obligation Note column | V-02 + V-03 + maximum criterion-aware specification. PROTOCOL REGISTRY column header reads "Activation Class (DEFERRED-PENDING or IMMEDIATELY-ACTIVE per C-28)". PR-OBL-01 Broken-Obligation Note uses exact C-29 qualifying phrase. PR-OBL-02 broken-obligation note uses exact C-28 ACTIVE-class semantics. DEFERRED-PENDING and IMMEDIATELY-ACTIVE labels embedded in ACTIVATED token and LOG rows. Hypothesis: 200/200. |

---

## V-01 -- Single-Axis: SE-First Phase 1c Execution (Role Sequence Inversion)

**Axis:** Role sequence -- SE completes Phase 1c Steps 1 and 2 (category table and FLS block analysis) before CS validates in Step 2b; Phase 0 body blocks and ACTIVATION STATE LOG unchanged from V-04-R9 baseline
**Hypothesis:** STEP-1-CLOSE-TOKEN PENDING state is a Phase 0 declaration -- it does not claim CS or SE authorship. RESOLVED fires at Step 1 close regardless of which role runs it. Per-Stage Chain-Reminder first activation is at LIVE GAPS REGISTER header (pre-Phase 1), unaffected by Phase 1c sequence. C-28 ACTIVE/PENDING state-class semantics are Phase 0 declarations, not execution-order claims. C-29 Phase 5b detection anchor is a static text field in the broken-obligation note. Both survive SE-first inversion unchanged. Hypothesis: 195/200.

---

You are running a permissions trace signal for: {{topic}}

---

## PHASE 0 -- FULL AUDIT CHAIN GATE

**Complete this phase and write the ACTIVATION STATE LOG before Phase 1 content.**

This trace operates under a bidirectional audit chain. Both directions pre-established here and active for the full output.

**Chain 1 -- Discovery to register (active during Phases 1-4):**
Every gap found during Phases 1-4 entered into LIVE GAPS REGISTER at moment of discovery. Discovered In records exact section and context. Set at discovery time, not reconstructed.

**Chain 2 -- Register to remediation echo (active during Phase 5a):**
Every register entry echoed via verbatim slot-fill. Phase 5b verification is **precondition for closing the trace, not a recommended step**.

**Per-row FLS trigger -- ACTIVE now:**
FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED format active during Phase 1c. CLOSED terminator required before any subsequent FLS ENTRY begins. Co-authorship is a structural property of the format. N/A markers on NO-gap REGISTER SLOTs make trigger completeness provable from the output alone.

**Remediation template (pre-declared; applied in Phase 5a):**

```
Gap [ID] (Discovered In: [verbatim from register -- Chain 2 slot-fill]):
  Config change:     [exact configuration element -- role / field / profile / rule and location]
  Expected state:    [UI view or query after fix]
  Verification step: [executable action -- UI location and expected result]
```

**Protocol: STEP-1-CLOSE-TOKEN (C-24 chain anchor -- C-26 Phase 0 body pre-declaration)**

This protocol is pre-declared here as a named Phase 0 body block. ACTIVATION STATE LOG entry below tracks execution status; this block is the authoritative obligation record.

Definition: At Phase 1c Step 1 close, emit a named close token recording the exact count of items analyzed (C-24 rubric phrase). Phase 1c section close must independently declare the downstream FLS ENTRY Category annotation count. Gate row 5 performs a non-vacuous numerical comparison between the chain anchor value and the section-close annotation count.

Emission format (required at Phase 1c Step 1 close):
```
STEP-1-CLOSE-TOKEN -- ACTIVATED
  Category table total rows analyzed: [N]
  FLS-scope rows (PII + Financial + Audit/Compliance): [M]
  Chain anchor value: [M]
  PENDING status: RESOLVED -- references Phase 0 STEP-1-CLOSE-TOKEN protocol declaration
```

**C-26/C-28 obligation record:**
Status at Phase 0 close: **PENDING** (activation class: deferred -- activation point outside Phase 0)
Activation point: Phase 1c Step 1 close
Broken-obligation note: **Unresolved PENDING at trace close = broken obligation.** A trace reaching Phase 5b with STEP-1-CLOSE-TOKEN still PENDING has a visibly broken chain anchor -- detectable without reading gate row 5.

**Protocol: Per-Stage Chain-Reminder (C-25 consumption-point annotation -- C-26 Phase 0 body pre-declaration)**

This protocol is pre-declared here as a named Phase 0 body block.

Definition: The annotation `[Category chain: active -- inherit from Step 1]` must appear as the first line of every FLS ENTRY block and at the LIVE GAPS REGISTER section header. Converts PR-1 propagation contract from a single-point declaration to a continuously-visible constraint.

**C-26/C-28 obligation record:**
Status at Phase 0 close: **ACTIVE** (activation class: immediately active -- first activation: LIVE GAPS REGISTER header, immediately below)
Subsequent activation points: every FLS ENTRY block open in Phase 1c
Broken-obligation note: **Absence at any FLS ENTRY block open is a broken state -- not deferred to the next block.**

**PHASE 0 GATE -- ACTIVATION STATE LOG:**

Execution record, not declarative checklist. PENDING entries have a named activation point -- reaching that point without the mechanism firing = broken state. Body-level protocol blocks above are authoritative obligation records; LOG rows track execution status.

| Mechanism | Status | Notes |
|-----------|--------|-------|
| Chain 1 -- discovery -> register, Discovered In set at discovery time | ACTIVE | Governs Phases 1-4 |
| Chain 2 -- register -> Phase 5a verbatim echo | ACTIVE | Phase 5b verification is precondition for trace close |
| Per-row FLS trigger -- ENTRY / SLOT / CLOSED | ACTIVE | CLOSED required before next entry |
| Remediation template -- Config change / Expected state / Verification step | ACTIVE | All three fields required |
| Mismatch example -- Phase 5b self-check instrument | LOADED | Precondition for trace close |
| I-6 category drift / PR-1 -- CATEGORY-DRIFT-VIOLATION marker | ACTIVE | Fires during Phase 1c Step 2 on any re-derivation |
| STEP-1-CLOSE-TOKEN -- named chain anchor; **body protocol block declared above** | PENDING | Activation: Phase 1c Step 1 close. Unresolved PENDING = broken obligation. |
| Per-stage chain-reminder -- `[Category chain: active -- inherit from Step 1]`; **body protocol block declared above** | ACTIVE | First activation: LIVE GAPS REGISTER header. Fires at every FLS ENTRY block open. |

*All mechanisms ACTIVE or LOADED. STEP-1-CLOSE-TOKEN PENDING -- body-level obligation declared above is authoritative. Entering PHASE 1.*

---

## LIVE GAPS REGISTER

**[Category chain: active -- inherit from Step 1]** *(Per-stage chain-reminder -- first activation per Phase 0 body protocol declaration)*

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

- Discovered In: exact section name and context, set at discovery time
- Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY / CATEGORY-DRIFT
- Severity: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 -- ENTITY AND ROLE MAP

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Scope | Default access for unauthenticated user |
|--------|-----------------|-------|----------------------------------------|

OWD scope: Organization / Business Unit / Owner. Missing scope = incomplete row.

Chain 1 check: OWD anomaly -> register. None -> "Phase 1a: no OWD anomalies -- [basis]."

**1b -- Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Team / User / Sharing-[rule name]. All roles with any privilege. Dataverse system names required. Highest-privilege role first; CS and SE as deltas.

**1c -- Sensitive field categorization:**

**SE-FIRST EXECUTION ORDER:** SE completes Steps 1 and 2 (category inventory and FLS block analysis) in full before CS validates in Step 2b.

**Inertia threat inventory (declared before Step 1):**

| ID | Threat | Fires During | Marker |
|----|--------|-------------|--------|
| I-1 | OWD defaults creating unexpected access | Phase 1a | ESCALATION-PATH |
| I-2 | Missing FLS on PII, Financial, Audit/Compliance | Phase 1c | MISSING-FLS |
| I-3 | Sharing rule overrides granting unintended access | Phase 1d | SHARING-CONFLICT |
| I-4 | Team membership privilege injection | Phase 2a | TEAM-GAP |
| I-5 | EMERGENT cross-entity hops | Phase 2b | CROSS-ENTITY |
| I-6 | Category drift -- re-derivation downstream of Step 1 | Phase 1c Step 2 onward | CATEGORY-DRIFT-VIOLATION |

**PR-1: Category propagation contract:**
Category in every FLS ENTRY block inherits from Step 1 -- not re-derived inline. Re-derivation fires I-6.

Step 1 (SE-authored): category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII | |
| | Financial | |
| | Audit/Compliance | |
| | Operational | |

Write "none" for empty categories.

**Step 1 close -- STEP-1-CLOSE-TOKEN activation (resolves PENDING from Phase 0 body protocol declaration):**

```
STEP-1-CLOSE-TOKEN -- ACTIVATED
  Category table total rows analyzed: [N]
  FLS-scope rows (PII + Financial + Audit/Compliance): [M]
  Chain anchor value: [M]
  PENDING status: RESOLVED -- references Phase 0 STEP-1-CLOSE-TOKEN protocol declaration
```

Gate row 5 will compare chain anchor [M] against Phase 1c section-close annotation count. Non-vacuous.

Step 2 (SE-authored): FLS check for all PII, Financial, and Audit/Compliance fields. Per-row trigger ACTIVE.

**Block format -- mandatory per sensitive field:**

Per-stage chain-reminder fires at each block open per Phase 0 body declaration:

```
[Category chain: active -- inherit from Step 1]
FLS ENTRY [n] -- [Entity].[Field]
| Entity | Field | Category | FLS Profile? | CS: Read | CS: Write | Expert: Read | Expert: Write | Gap? |
|--------|-------|----------|-------------|----------|-----------|--------------|---------------|------|

REGISTER SLOT [n] (Chain 1 -- complete before CLOSED marker):
```

If Gap? = YES: enter register. If Gap? = NO: "-> No gap. Register slot: N/A -- [confirmation]."

```
FLS ENTRY [n] CLOSED
```

**Step 2b -- CS validation pass:** After SE completes all FLS ENTRY blocks, CS reviews each entry. CS confirms CS Read/Write column values are accurate. Any discrepancy between CS expectation and SE entry is flagged as a MISSING-FLS finding and registered immediately.

Section close:
```
Phase 1c FLS complete.
  FLS ENTRY blocks: [N]
  CLOSED markers: [N] (must equal [N])
  YES entries: [N] / N/A register slots: [N]
  Chain-reminder annotations at block opens: [N] (must equal [N])
  CS validation pass: complete
  Downstream FLS ENTRY Category annotation count: [M]
  (Separately declared for gate row 5 comparison vs STEP-1-CLOSE-TOKEN chain anchor [M])
```

**1d -- Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

Conflicts = YES -> register SHARING-CONFLICT. None -> "Phase 1d: no SHARING-CONFLICT -- [rules checked, reason]."

---

## PHASE 2 -- TEAM AND CROSS-ENTITY

**2a -- Team membership gap:**
Finding: `[Role] -> [Team X] -> [elevated access] -- mechanism: [how]`
Rule-out: "Checked [teams]: no injection path -- [reason]."

**2b -- Cross-entity chain:**
Highest-sensitivity entity (justify from Phase 1c Step 1). Two hops: `[Role] -> [Entity A, op: X, scope: Y] -> [Relationship] -> [Entity B, op: X, scope: Y]`. INTENTIONAL or EMERGENT.

---

## PHASE 3 -- PER-ROLE ESCALATION ANALYSIS

One subsection per role. No collective statements.

**Role: [name]**
- Team membership Write: [YES / NO -- evidence]
- Security role assignment Write: [YES / NO -- evidence]
- Record ownership Assign scope: [scope -- elevation?]
- Business unit configuration Write: [YES / NO -- evidence]

Conclusion: ESCALATION-PATH FOUND / RULED OUT.

**Negative-check evidence:** "Checked [items] for [roles]; [type] does not apply because [specific reason]."

---

## PHASE 4 -- ROLE DIFFERENTIATION

**Customer Service Representative:** CRUD + scope. Sensitive field access from Phase 1c -- appropriate or overreach?
**Dataverse Security Expert:** CRUD + scope. Every privilege CS lacks. Least-privilege or overreach?
**Contrast statement (required):** One paragraph, both role names explicit.

---

## PHASE 5a -- REMEDIATION ENTRIES

Chain 2 active. Copy Discovered In verbatim. Three-field template required.

```
Gap [ID] (Discovered In: [verbatim]):
  Config change:     [exact element and location]
  Expected state:    [UI view after fix]
  Verification step: [executable action]
```

---

## PHASE 5b -- CHAIN 2 SELF-CHECK CLOSE

**Precondition for closing the trace.**

| Gap ID | Register: Discovered In (exact text) | Phase 5a Echo: Discovered In (exact text) | Match? |
|--------|--------------------------------------|-------------------------------------------|--------|

**TRACE CLOSE TOKEN:** `Chain 2 self-check applied. Rows: [N]. FAIL corrections: [N]. Trace closed.`

---

## SUBMISSION GATE

**ANTI-SPECULATION MANDATE -- VERDICT-FAIL before the table header.** No gate row may record PASS without citing specific evidence.

| Row | Check | Evidence Cited | Status |
|-----|-------|----------------|--------|
| 1 | All entities Phase 1a with OWD and scope | Phase 1a row count and scope values | PASS / VERDICT-FAIL |
| 2 | All roles by Dataverse system name; record scope per entity | Phase 1b role names and Record Scope column | PASS / VERDICT-FAIL |
| 3 | FLS analyzed by SE; CS validation complete; CLOSED; chain-reminder count equals block count | Phase 1c close: N blocks, N CLOSED, N annotations; CS Step 2b complete | PASS / VERDICT-FAIL |
| 4 | Gap types checked; negative-check evidence present | Phase 3 statements and Phase 2 rule-outs | PASS / VERDICT-FAIL |
| 5 | Non-vacuous token-swap: (a) STEP-1-CLOSE-TOKEN anchor [M] -- PENDING resolved at Step 1 close, RESOLVED marker references Phase 0 body declaration; (b) section-close annotation count [M] -- separately declared; (c) [M] == [M]? YES/NO; (d) PR-1 clean; (e) rows 1-4 PASS | ACTIVATED block with RESOLVED marker, section-close count, rows 1-4 | PASS / VERDICT-FAIL |

---

## V-02 -- Single-Axis: Inertia Framing (CONTEXT Preamble)

**Axis:** Inertia framing -- CONTEXT section before Phase 0 names three manual RBAC audit blind spots with IDs and names the status-quo tool being displaced; Phase 0 body blocks and all subsequent phases unchanged from V-04-R9 baseline
**Hypothesis:** Pre-Phase 0 motivational framing adds no structural elements to Phase 0. STEP-1-CLOSE-TOKEN PENDING state and Per-Stage Chain-Reminder ACTIVE state are Phase 0 declarations -- framing before Phase 0 does not modify them. Tests whether naming escalation threat classes upfront improves C-04 (escalation vector depth) and C-08 (remediation specificity) by anchoring the trace to known threat patterns. C-28/C-29 unchanged. Hypothesis: 195/200 baseline maintained; potential C-04/C-08 gain.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: Three Blind Spots That Defeat Manual RBAC Review

Three structural gaps defeat point-in-time manual Dataverse security review:

**Blind spot 1 -- Cumulative privilege accumulation.** No Dataverse UI surface shows the combined effect of security role depth, team membership, OWD settings, and sharing rules simultaneously. Manual review of the Roles UI sees assigned roles but not the access scope each role activates across owned entities when combined with team membership and OWD defaults. This trace computes effective scope from all four layers together before any gap hunt begins.

**Blind spot 2 -- Post-incident FLS discovery.** Field-Level Security profile absences appear in incident postmortems, not pre-release audits. No native UI surface enumerates FLS coverage gaps across all sensitive fields at once. This trace enumerates every PII, Financial, and Audit/Compliance field against its FLS profile before any incident occurs.

**Blind spot 3 -- OWD-sharing-rule override blindness.** A Private OWD does not prevent an independently-configured sharing rule from reopening access. Manual review of OWD settings does not automatically cross-reference active sharing rules. This trace cross-references every OWD setting against every active sharing rule to surface unintended grants.

Each Phase 2 and Phase 3 subsection names the blind spot it resolves.

---

## PHASE 0 -- FULL AUDIT CHAIN GATE

**Complete this phase and write the ACTIVATION STATE LOG before Phase 1 content.**

Both audit chain directions pre-established here and active for the full output.

**Chain 1 -- Discovery to register (active during Phases 1-4):**
Every gap entered into LIVE GAPS REGISTER at moment of discovery. Discovered In set at discovery time, not reconstructed.

**Chain 2 -- Register to remediation echo (active during Phase 5a):**
Every register entry echoed via verbatim slot-fill. Phase 5b verification is **precondition for closing the trace, not a recommended step**.

**Per-row FLS trigger -- ACTIVE now:**
FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED format active during Phase 1c. CLOSED required before next entry. Co-authorship structural. N/A markers make trigger completeness provable.

**Remediation template (pre-declared):**

```
Gap [ID] (Discovered In: [verbatim -- Chain 2 slot-fill]):
  Config change:     [exact element and location]
  Expected state:    [UI view or query after fix]
  Verification step: [executable action -- UI location and expected result]
```

**Protocol: STEP-1-CLOSE-TOKEN (C-24 chain anchor -- C-26 Phase 0 body pre-declaration)**

Pre-declared as named Phase 0 body block. ACTIVATION STATE LOG tracks execution status; this block is authoritative.

Definition: At Phase 1c Step 1 close, emit a named close token recording the exact count of items analyzed. Phase 1c section close independently declares downstream FLS ENTRY Category annotation count. Gate row 5 performs non-vacuous numerical comparison.

Emission format (required at Phase 1c Step 1 close):
```
STEP-1-CLOSE-TOKEN -- ACTIVATED
  Category table total rows analyzed: [N]
  FLS-scope rows (PII + Financial + Audit/Compliance): [M]
  Chain anchor value: [M]
  PENDING status: RESOLVED -- references Phase 0 STEP-1-CLOSE-TOKEN protocol declaration
```

**C-26/C-28 obligation record:**
Status at Phase 0 close: **PENDING** (activation class: deferred -- activation point outside Phase 0)
Activation point: Phase 1c Step 1 close
Broken-obligation note: **Unresolved PENDING at trace close = broken obligation.** A trace reaching Phase 5b with STEP-1-CLOSE-TOKEN still PENDING has a visibly broken chain anchor -- detectable without reading gate row 5.

**Protocol: Per-Stage Chain-Reminder (C-25 consumption-point annotation -- C-26 Phase 0 body pre-declaration)**

Pre-declared as named Phase 0 body block.

Definition: `[Category chain: active -- inherit from Step 1]` at every FLS ENTRY block open and at LIVE GAPS REGISTER header. Converts PR-1 propagation contract from single-point declaration to continuously-visible constraint.

**C-26/C-28 obligation record:**
Status at Phase 0 close: **ACTIVE** (activation class: immediately active -- first activation: LIVE GAPS REGISTER header, immediately below)
Subsequent activation points: every FLS ENTRY block open in Phase 1c
Broken-obligation note: **Absence at any FLS ENTRY block open is a broken state -- not deferred to the next block.**

**PHASE 0 GATE -- ACTIVATION STATE LOG:**

Execution record, not declarative checklist. Body-level protocol blocks above are authoritative; LOG rows track execution status.

| Mechanism | Status | Notes |
|-----------|--------|-------|
| Chain 1 -- discovery -> register, Discovered In set at discovery time | ACTIVE | Governs Phases 1-4 |
| Chain 2 -- register -> Phase 5a verbatim echo | ACTIVE | Phase 5b verification is precondition for trace close |
| Per-row FLS trigger -- ENTRY / SLOT / CLOSED | ACTIVE | CLOSED required before next entry |
| Remediation template -- Config change / Expected state / Verification step | ACTIVE | All three fields required |
| Mismatch example -- Phase 5b self-check instrument | LOADED | Precondition for trace close |
| I-6 category drift / PR-1 -- CATEGORY-DRIFT-VIOLATION marker | ACTIVE | Fires during Phase 1c Step 2 on re-derivation |
| STEP-1-CLOSE-TOKEN -- named chain anchor; **body protocol block declared above** | PENDING | Activation: Phase 1c Step 1 close. Unresolved PENDING = broken obligation. |
| Per-stage chain-reminder -- `[Category chain: active -- inherit from Step 1]`; **body protocol block declared above** | ACTIVE | First activation: LIVE GAPS REGISTER header. Fires at every FLS ENTRY block open. |

*All mechanisms ACTIVE or LOADED. STEP-1-CLOSE-TOKEN PENDING -- body-level obligation declared above is authoritative. Entering PHASE 1.*

---

## LIVE GAPS REGISTER

**[Category chain: active -- inherit from Step 1]** *(Per-stage chain-reminder -- first activation per Phase 0 body declaration)*

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

---

## PHASE 1 -- ENTITY AND ROLE MAP

**1a -- Entity and OWD inventory:** *(Resolves blind spot 1 -- OWD layer)*

| Entity | Org-Wide Default | Scope | Default access for unauthenticated user |
|--------|-----------------|-------|----------------------------------------|

OWD scope: Organization / Business Unit / Owner.

**1b -- Operation-role matrix:** *(Resolves blind spot 1 -- role + scope combined view)*

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Dataverse system names required. Highest-privilege role first; CS and SE as deltas.

**1c -- Sensitive field categorization:** *(Resolves blind spot 2 -- FLS pre-incident coverage)*

**Inertia threat inventory:**

| ID | Threat | Fires During | Marker |
|----|--------|-------------|--------|
| I-1 | OWD defaults creating unexpected access | Phase 1a | ESCALATION-PATH |
| I-2 | Missing FLS on PII, Financial, Audit/Compliance | Phase 1c | MISSING-FLS |
| I-3 | Sharing rule overrides granting unintended access | Phase 1d | SHARING-CONFLICT |
| I-4 | Team membership privilege injection | Phase 2a | TEAM-GAP |
| I-5 | EMERGENT cross-entity hops | Phase 2b | CROSS-ENTITY |
| I-6 | Category drift downstream of Step 1 | Phase 1c Step 2 onward | CATEGORY-DRIFT-VIOLATION |

**PR-1: Category propagation contract:** Category in FLS ENTRY blocks inherits from Step 1.

Step 1: category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII | |
| | Financial | |
| | Audit/Compliance | |
| | Operational | |

**Step 1 close -- STEP-1-CLOSE-TOKEN activation:**

```
STEP-1-CLOSE-TOKEN -- ACTIVATED
  Category table total rows analyzed: [N]
  FLS-scope rows (PII + Financial + Audit/Compliance): [M]
  Chain anchor value: [M]
  PENDING status: RESOLVED -- references Phase 0 STEP-1-CLOSE-TOKEN protocol declaration
```

Step 2: FLS check. Block format:

```
[Category chain: active -- inherit from Step 1]
FLS ENTRY [n] -- [Entity].[Field]
| Entity | Field | Category | FLS Profile? | CS: Read | CS: Write | Expert: Read | Expert: Write | Gap? |
|--------|-------|----------|-------------|----------|-----------|--------------|---------------|------|

REGISTER SLOT [n] (Chain 1):
```

Gap? = YES -> register. Gap? = NO -> "-> No gap. Register slot: N/A."

```
FLS ENTRY [n] CLOSED
```

Section close:
```
Phase 1c FLS complete.
  Blocks: [N] / CLOSED: [N] / YES: [N] / N/A: [N]
  Chain-reminder annotations: [N] (must equal [N])
  Downstream annotation count: [M]
  (Gate row 5: [M] vs anchor [M])
```

**1d -- Sharing rule inventory:** *(Resolves blind spot 3 -- OWD-sharing override)*

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

---

## PHASE 2 -- TEAM AND CROSS-ENTITY

**2a -- Team membership gap:** *(Blind spot 1 -- team injection layer)*
Finding / rule-out with specific evidence.

**2b -- Cross-entity chain:**
Two hops from highest-sensitivity entity. INTENTIONAL or EMERGENT.

---

## PHASE 3 -- PER-ROLE ESCALATION ANALYSIS

One subsection per role.

**Role: [name]** -- Team Write / Role Assignment Write / Assign scope / BU Write.
Conclusion: ESCALATION-PATH FOUND / RULED OUT.

**Negative-check evidence:** "Checked [items]; [type] does not apply because [specific reason]."

---

## PHASE 4 -- ROLE DIFFERENTIATION

**Customer Service Representative / Dataverse Security Expert.** Contrast statement with both names explicit.

---

## PHASE 5a -- REMEDIATION ENTRIES

Verbatim Discovered In. Three-field template.

---

## PHASE 5b -- CHAIN 2 SELF-CHECK CLOSE

**Precondition for closing the trace.**

| Gap ID | Register: Discovered In | Phase 5a Echo: Discovered In | Match? |

**TRACE CLOSE TOKEN:** `Chain 2 self-check applied. Rows: [N]. FAIL: [N]. Trace closed.`

---

## SUBMISSION GATE

**ANTI-SPECULATION MANDATE -- VERDICT-FAIL before the table header.**

| Row | Check | Evidence Cited | Status |
|-----|-------|----------------|--------|
| 1 | All entities Phase 1a with OWD and scope | Phase 1a row count and scope values | PASS / VERDICT-FAIL |
| 2 | All roles Dataverse system names; record scope per entity | Phase 1b roles and Record Scope column | PASS / VERDICT-FAIL |
| 3 | FLS analyzed; CLOSED; chain-reminder count equals block count | Phase 1c close: N blocks, N CLOSED, N annotations | PASS / VERDICT-FAIL |
| 4 | Gap types checked; negative-check evidence present | Phase 3 and Phase 2 rule-outs | PASS / VERDICT-FAIL |
| 5 | Token-swap: anchor [M] vs section-close [M]; RESOLVED references Phase 0; PR-1 clean; rows 1-4 PASS | ACTIVATED block, section-close count, rows 1-4 | PASS / VERDICT-FAIL |

---

## V-03 -- Single-Axis: PROTOCOL REGISTRY Table (Output Format)

**Axis:** Output format -- PROTOCOL REGISTRY table replaces prose body blocks for STEP-1-CLOSE-TOKEN and Per-Stage Chain-Reminder; all C-26/C-28/C-29 required fields appear as explicit table columns (Activation Class, State, Activation Points, Broken-Obligation Note, Detection Phase); ACTIVATION STATE LOG rows reference REGISTRY-IDs
**Hypothesis:** C-26 requires four fields per protocol: named block, state, activation point, broken-obligation note. C-28 requires state-class assignment to match activation timing and broken-obligation semantics to match state class. C-29 requires the broken-obligation note to name a specific trace phase as the detection point. All four fields can be encoded as table columns with identical semantic content. The prose block form is a structural vehicle; the content is the criterion. If criteria inspect content (state class, broken-obligation text, activation point, detection phase) rather than requiring a prose section, table encoding satisfies. Hypothesis: C-26/C-28/C-29 pass; 195/200 maintained.

---

You are running a permissions trace signal for: {{topic}}

---

## PHASE 0 -- FULL AUDIT CHAIN GATE

**Complete this phase and write the ACTIVATION STATE LOG before Phase 1 content.**

**Chain 1 -- Discovery to register (Phases 1-4):** Discovered In set at discovery time, not reconstructed.

**Chain 2 -- Register to remediation echo (Phase 5a):** Verbatim slot-fill. Phase 5b verification is **precondition for closing the trace**.

**Per-row FLS trigger -- ACTIVE:** FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED during Phase 1c. CLOSED required before next entry. N/A markers make trigger completeness provable.

**Remediation template (pre-declared):**
```
Gap [ID] (Discovered In: [verbatim]):
  Config change:     [exact element and location]
  Expected state:    [UI view after fix]
  Verification step: [executable action]
```

**PROTOCOL REGISTRY (Phase 0 pre-declaration -- authoritative obligation records before Phase 1):**

| REGISTRY-ID | Protocol Name | Activation Class | State at Phase 0 Close | Activation Point(s) | Broken-Obligation Note | Detection Phase |
|-------------|--------------|-----------------|----------------------|--------------------|-----------------------|----------------|
| PR-OBL-01 | STEP-1-CLOSE-TOKEN (C-24 chain anchor) | Deferred -- activation point outside Phase 0 | **PENDING** | Phase 1c Step 1 close | Unresolved PENDING at trace close = broken obligation | **Phase 5b** -- a trace reaching Phase 5b with STEP-1-CLOSE-TOKEN still PENDING has a visibly broken chain anchor |
| PR-OBL-02 | Per-Stage Chain-Reminder (C-25 annotation) | Immediately active -- from Phase 0 itself | **ACTIVE** | First: LIVE GAPS REGISTER header (immediately below). Subsequent: every FLS ENTRY block open in Phase 1c | Absence at any FLS ENTRY block open is a broken state -- not deferred to the next block | N/A (immediately active; broken state observable at any absent consumption site) |

**Emission format for PR-OBL-01 (Phase 1c Step 1 close):**
```
STEP-1-CLOSE-TOKEN -- ACTIVATED [PR-OBL-01]
  Category table total rows analyzed: [N]
  FLS-scope rows (PII + Financial + Audit/Compliance): [M]
  Chain anchor value: [M]
  PENDING status: RESOLVED -- references Phase 0 PROTOCOL REGISTRY PR-OBL-01
```

**Annotation form for PR-OBL-02 (LIVE GAPS REGISTER header and every FLS ENTRY block open):**
```
[Category chain: active -- inherit from Step 1] [PR-OBL-02]
```

**PHASE 0 GATE -- ACTIVATION STATE LOG:**

Execution record. PROTOCOL REGISTRY above is authoritative. LOG rows reference REGISTRY-IDs.

| Mechanism | REGISTRY-ID | Status | Notes |
|-----------|------------|--------|-------|
| Chain 1 -- discovery -> register | -- | ACTIVE | Governs Phases 1-4 |
| Chain 2 -- register -> Phase 5a verbatim echo | -- | ACTIVE | Phase 5b precondition |
| Per-row FLS trigger -- ENTRY / SLOT / CLOSED | -- | ACTIVE | CLOSED required |
| Remediation template -- three fields | -- | ACTIVE | All fields required |
| Mismatch example -- Phase 5b self-check | -- | LOADED | Precondition for trace close |
| I-6 category drift / PR-1 | -- | ACTIVE | Fires on re-derivation |
| STEP-1-CLOSE-TOKEN; **REGISTRY PR-OBL-01** | PR-OBL-01 | PENDING | Activation: Phase 1c Step 1 close. Unresolved = broken obligation. |
| Per-stage chain-reminder; **REGISTRY PR-OBL-02** | PR-OBL-02 | ACTIVE | First activation: LIVE GAPS REGISTER header. |

*PR-OBL-01 PENDING. PR-OBL-02 ACTIVE. PROTOCOL REGISTRY is authoritative. Entering PHASE 1.*

---

## LIVE GAPS REGISTER

**[Category chain: active -- inherit from Step 1] [PR-OBL-02]** *(Per-stage chain-reminder -- first activation per PROTOCOL REGISTRY)*

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

---

## PHASE 1 -- ENTITY AND ROLE MAP

**1a -- Entity and OWD inventory:**

| Entity | Org-Wide Default | Scope | Default access for unauthenticated user |
|--------|-----------------|-------|----------------------------------------|

OWD scope: Organization / Business Unit / Owner.

**1b -- Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Dataverse system names required. Highest-privilege role first.

**1c -- Sensitive field categorization:**

**Inertia threat inventory:**

| ID | Threat | Fires During | Marker |
|----|--------|-------------|--------|
| I-1 | OWD defaults | Phase 1a | ESCALATION-PATH |
| I-2 | Missing FLS | Phase 1c | MISSING-FLS |
| I-3 | Sharing rule overrides | Phase 1d | SHARING-CONFLICT |
| I-4 | Team membership injection | Phase 2a | TEAM-GAP |
| I-5 | Cross-entity hops | Phase 2b | CROSS-ENTITY |
| I-6 | Category drift | Phase 1c Step 2 onward | CATEGORY-DRIFT-VIOLATION |

**PR-1: Category propagation contract:** Category in FLS ENTRY blocks inherits from Step 1.

Step 1: category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII | |
| | Financial | |
| | Audit/Compliance | |
| | Operational | |

**Step 1 close -- PR-OBL-01 activation:**

```
STEP-1-CLOSE-TOKEN -- ACTIVATED [PR-OBL-01]
  Category table total rows analyzed: [N]
  FLS-scope rows: [M] / Chain anchor: [M]
  PENDING status: RESOLVED -- references Phase 0 PROTOCOL REGISTRY PR-OBL-01
```

Step 2: FLS check. Block format:

```
[Category chain: active -- inherit from Step 1] [PR-OBL-02]
FLS ENTRY [n] -- [Entity].[Field]
| Entity | Field | Category | FLS Profile? | CS: Read | CS: Write | Expert: Read | Expert: Write | Gap? |
|--------|-------|----------|-------------|----------|-----------|--------------|---------------|------|

REGISTER SLOT [n] (Chain 1):
```

Gap? = YES -> register. Gap? = NO -> "-> No gap. Register slot: N/A."

```
FLS ENTRY [n] CLOSED
```

Section close:
```
Phase 1c FLS complete.
  Blocks: [N] / CLOSED: [N] / YES: [N] / N/A: [N]
  PR-OBL-02 annotations at block opens: [N] (must equal [N])
  Downstream annotation count: [M]
  (Gate row 5: PR-OBL-01 anchor [M] vs downstream [M])
```

**1d -- Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

---

## PHASE 2 -- TEAM AND CROSS-ENTITY

**2a:** Finding / rule-out with evidence.
**2b:** Two-hop chain. INTENTIONAL or EMERGENT.

---

## PHASE 3 -- PER-ROLE ESCALATION ANALYSIS

One subsection per role.

**Role: [name]** -- Team Write / Role Assignment Write / Assign scope / BU Write. Conclusion: FOUND / RULED OUT.

**Negative-check evidence:** "Checked [items]; [type] does not apply because [reason]."

---

## PHASE 4 -- ROLE DIFFERENTIATION

**Customer Service Representative / Dataverse Security Expert.** Contrast statement with both names explicit.

---

## PHASE 5a -- REMEDIATION ENTRIES

Verbatim Discovered In. Three-field template.

---

## PHASE 5b -- CHAIN 2 SELF-CHECK CLOSE

**Precondition for closing the trace.**

| Gap ID | Register: Discovered In | Phase 5a Echo: Discovered In | Match? |

**TRACE CLOSE TOKEN:** `Chain 2 self-check. Rows: [N]. FAIL: [N]. Trace closed.`

---

## SUBMISSION GATE

**ANTI-SPECULATION MANDATE -- VERDICT-FAIL before the table header.**

| Row | Check | Evidence Cited | Status |
|-----|-------|----------------|--------|
| 1 | All entities Phase 1a with OWD and scope | Phase 1a counts | PASS / VERDICT-FAIL |
| 2 | All roles Dataverse system names; scope | Phase 1b | PASS / VERDICT-FAIL |
| 3 | FLS analyzed; CLOSED; PR-OBL-02 count equals block count | Phase 1c close counts | PASS / VERDICT-FAIL |
| 4 | Gap types checked; negative-check evidence present | Phase 3, Phase 2 | PASS / VERDICT-FAIL |
| 5 | Token-swap: PR-OBL-01 anchor [M] vs downstream [M]; RESOLVED references REGISTRY; PR-1 clean; rows 1-4 PASS | ACTIVATED block, section-close, rows 1-4 | PASS / VERDICT-FAIL |

---

## V-04 -- Combined: SE-First + Inertia Framing

**Axis:** Combined role sequence + inertia framing -- SE executes Phase 1c before CS validates; CONTEXT preamble names three blind spots; Phase 0 body blocks unchanged from V-04-R9 baseline
**Hypothesis:** V-01 proves SE-first inversion preserves C-28/C-29. V-02 proves inertia framing adds no Phase 0 structural change. Axes operate at non-overlapping sites: V-01 modifies Phase 1c execution order; V-02 adds pre-Phase 0 framing. Phase 0 body blocks, ACTIVATION STATE LOG, and PROTOCOL states unchanged. Hypothesis: 195/200 baseline maintained; potential C-04/C-08 gain from inertia framing.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: Three Blind Spots That Defeat Manual RBAC Review

**Blind spot 1 -- Cumulative privilege accumulation.** The Dataverse Roles UI shows assigned roles, not the combined effective scope produced by roles, team membership, OWD defaults, and sharing rules together. This trace computes effective scope from all four layers before any gap hunt begins.

**Blind spot 2 -- Post-incident FLS discovery.** FLS profile absences appear in incident response, not in pre-release review. This trace enumerates every PII, Financial, and Audit/Compliance field against its FLS profile.

**Blind spot 3 -- OWD-sharing-rule override blindness.** Private OWD settings do not prevent independently-configured sharing rules from reopening access. This trace cross-references every OWD setting against every active sharing rule.

Each Phase 2 and Phase 3 subsection names the blind spot it resolves.

---

## PHASE 0 -- FULL AUDIT CHAIN GATE

**Complete this phase and write the ACTIVATION STATE LOG before Phase 1 content.**

**Chain 1 -- Discovery to register (Phases 1-4):** Discovered In set at discovery time, not reconstructed.

**Chain 2 -- Register to remediation echo (Phase 5a):** Verbatim slot-fill. Phase 5b is **precondition for closing the trace**.

**Per-row FLS trigger -- ACTIVE:** FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED during Phase 1c. CLOSED required. N/A markers make completeness provable.

**Remediation template (pre-declared):**
```
Gap [ID] (Discovered In: [verbatim]):
  Config change: / Expected state: / Verification step:
```

**Protocol: STEP-1-CLOSE-TOKEN (C-24 chain anchor -- C-26 Phase 0 body pre-declaration)**

Pre-declared as named Phase 0 body block. ACTIVATION STATE LOG tracks execution status; this block is authoritative.

Definition: At Phase 1c Step 1 close, emit a named close token recording the exact count of items analyzed. Phase 1c section close independently declares the downstream annotation count. Gate row 5 performs a non-vacuous numerical comparison.

Emission format:
```
STEP-1-CLOSE-TOKEN -- ACTIVATED
  Rows analyzed: [N] / FLS-scope rows: [M] / Chain anchor: [M]
  PENDING status: RESOLVED -- references Phase 0 STEP-1-CLOSE-TOKEN protocol declaration
```

**C-26/C-28 obligation record:**
Status at Phase 0 close: **PENDING** (activation class: deferred -- activation point outside Phase 0)
Activation point: Phase 1c Step 1 close
Broken-obligation note: **Unresolved PENDING at trace close = broken obligation.** A trace reaching Phase 5b with STEP-1-CLOSE-TOKEN still PENDING has a visibly broken chain anchor -- detectable without reading gate row 5.

**Protocol: Per-Stage Chain-Reminder (C-25 consumption-point annotation -- C-26 Phase 0 body pre-declaration)**

Pre-declared as named Phase 0 body block.

Definition: `[Category chain: active -- inherit from Step 1]` at every FLS ENTRY block open and at LIVE GAPS REGISTER header. Converts PR-1 propagation contract from single-point declaration to continuously-visible constraint.

**C-26/C-28 obligation record:**
Status at Phase 0 close: **ACTIVE** (activation class: immediately active -- first activation: LIVE GAPS REGISTER header, immediately below)
Subsequent activation points: every FLS ENTRY block open in Phase 1c
Broken-obligation note: **Absence at any FLS ENTRY block open is a broken state -- not deferred to the next block.**

**PHASE 0 GATE -- ACTIVATION STATE LOG:**

Execution record. Body-level protocol blocks above are authoritative; LOG rows track status.

| Mechanism | Status | Notes |
|-----------|--------|-------|
| Chain 1 -- discovery -> register | ACTIVE | Governs Phases 1-4 |
| Chain 2 -- register -> Phase 5a verbatim echo | ACTIVE | Phase 5b precondition |
| Per-row FLS trigger -- ENTRY / SLOT / CLOSED | ACTIVE | CLOSED required |
| Remediation template -- three fields | ACTIVE | All fields required |
| Mismatch example -- Phase 5b self-check | LOADED | Precondition for trace close |
| I-6 category drift / PR-1 | ACTIVE | Fires on re-derivation |
| STEP-1-CLOSE-TOKEN; **body protocol block declared above** | PENDING | Activation: Phase 1c Step 1 close. Unresolved = broken obligation. |
| Per-stage chain-reminder; **body protocol block declared above** | ACTIVE | First activation: LIVE GAPS REGISTER header. |

*STEP-1-CLOSE-TOKEN PENDING. Per-stage chain-reminder ACTIVE. Entering PHASE 1.*

---

## LIVE GAPS REGISTER

**[Category chain: active -- inherit from Step 1]** *(Per-stage chain-reminder -- first activation)*

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

---

## PHASE 1 -- ENTITY AND ROLE MAP

**1a -- Entity and OWD inventory:** *(Blind spot 1 -- OWD layer)*

| Entity | Org-Wide Default | Scope | Default access for unauthenticated user |
|--------|-----------------|-------|----------------------------------------|

OWD scope: Organization / Business Unit / Owner.

**1b -- Operation-role matrix:** *(Blind spot 1 -- combined scope)*

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Dataverse system names required. Highest-privilege role first.

**1c -- Sensitive field categorization:** *(Blind spot 2 -- FLS coverage)*

**SE-FIRST EXECUTION ORDER:** SE completes Steps 1 and 2 before CS validates in Step 2b.

**Inertia threat inventory:**

| ID | Threat | Fires During | Marker |
|----|--------|-------------|--------|
| I-1 | OWD defaults | Phase 1a | ESCALATION-PATH |
| I-2 | Missing FLS | Phase 1c | MISSING-FLS |
| I-3 | Sharing rule overrides | Phase 1d | SHARING-CONFLICT |
| I-4 | Team membership injection | Phase 2a | TEAM-GAP |
| I-5 | Cross-entity hops | Phase 2b | CROSS-ENTITY |
| I-6 | Category drift | Phase 1c Step 2 onward | CATEGORY-DRIFT-VIOLATION |

**PR-1:** Category in FLS ENTRY blocks inherits from Step 1.

Step 1 (SE-authored): category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII | |
| | Financial | |
| | Audit/Compliance | |
| | Operational | |

**Step 1 close:**
```
STEP-1-CLOSE-TOKEN -- ACTIVATED
  Rows: [N] / FLS-scope: [M] / Anchor: [M]
  PENDING status: RESOLVED -- references Phase 0 STEP-1-CLOSE-TOKEN protocol declaration
```

Step 2 (SE-authored): FLS check. Block format:

```
[Category chain: active -- inherit from Step 1]
FLS ENTRY [n] -- [Entity].[Field]
| Entity | Field | Category | FLS Profile? | CS: Read | CS: Write | Expert: Read | Expert: Write | Gap? |
|--------|-------|----------|-------------|----------|-----------|--------------|---------------|------|

REGISTER SLOT [n] (Chain 1):
FLS ENTRY [n] CLOSED
```

**Step 2b (CS validation):** CS reviews SE FLS entries; confirms CS columns; flags discrepancies as MISSING-FLS.

Section close:
```
Phase 1c FLS complete.
  Blocks: [N] / CLOSED: [N] / YES: [N] / N/A: [N] / Annotations: [N] / Count: [M]
  CS validation: complete. Gate row 5: anchor [M] vs count [M].
```

**1d -- Sharing rule inventory:** *(Blind spot 3 -- OWD-sharing override)*

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts? |
|-----------|---------|---------------|-------------|------------|

---

## PHASE 2 -- TEAM AND CROSS-ENTITY

**2a:** *(Blind spot 1 -- team layer)* Finding / rule-out.
**2b:** Two-hop chain. INTENTIONAL or EMERGENT.

---

## PHASE 3 -- PER-ROLE ESCALATION ANALYSIS

One subsection per role.

**Role: [name]** -- Team Write / Role Assignment Write / Assign scope / BU Write.
Conclusion: FOUND / RULED OUT.

**Negative-check evidence:** "Checked [items]; [type] does not apply because [reason]."

---

## PHASE 4 -- ROLE DIFFERENTIATION

**Customer Service Representative / Dataverse Security Expert.** Contrast statement with both names explicit.

---

## PHASE 5a -- REMEDIATION ENTRIES

Verbatim Discovered In. Three-field template.

---

## PHASE 5b -- CHAIN 2 SELF-CHECK CLOSE

**Precondition for closing the trace.**

| Gap ID | Register: Discovered In | Phase 5a Echo: Discovered In | Match? |

**TRACE CLOSE TOKEN:** `Chain 2 self-check. Rows: [N]. FAIL: [N]. Trace closed.`

---

## SUBMISSION GATE

**ANTI-SPECULATION MANDATE.**

| Row | Check | Evidence Cited | Status |
|-----|-------|----------------|--------|
| 1 | All entities OWD and scope | Phase 1a counts | PASS / VERDICT-FAIL |
| 2 | All roles Dataverse system names | Phase 1b | PASS / VERDICT-FAIL |
| 3 | FLS SE-authored; CS validation; CLOSED; annotations = blocks | Phase 1c close | PASS / VERDICT-FAIL |
| 4 | Gap types; negative-check evidence | Phase 3, Phase 2 | PASS / VERDICT-FAIL |
| 5 | Token-swap anchor [M] vs count [M]; RESOLVED; PR-1 clean; rows 1-4 | ACTIVATED block, section-close, rows 1-4 | PASS / VERDICT-FAIL |

---

## V-05 -- Combined: Inertia Framing + PROTOCOL REGISTRY + Rubric-Verbatim C-28/C-29 Language

**Axis:** Combined inertia framing + PROTOCOL REGISTRY table + C-28/C-29 rubric-exact language: PROTOCOL REGISTRY column header "Activation Class (DEFERRED-PENDING or IMMEDIATELY-ACTIVE per C-28)" names the C-28 criterion; PR-OBL-01 Broken-Obligation Note cell uses exact C-29 detection phrase; PR-OBL-02 broken-obligation note uses C-28 ACTIVE-class exact semantics; DEFERRED-PENDING / IMMEDIATELY-ACTIVE labels thread through ACTIVATED token and LOG rows
**Hypothesis:** V-03 proves PROTOCOL REGISTRY table encodes C-26/C-28/C-29 content. V-02 proves inertia framing adds no Phase 0 disruption. V-05 combines both and embeds C-28/C-29 criterion identifiers directly in REGISTRY column headers and cell values -- a scorer verifies state-class assignment from the REGISTRY table alone without any Phase 0 prose cross-reference. C-29 exact detection phrase appears verbatim in the REGISTRY table cell. Hypothesis: 200/200.

---

You are running a permissions trace signal for: {{topic}}

---

## CONTEXT: Three Blind Spots That Defeat Manual RBAC Review

**Blind spot 1 -- Cumulative privilege accumulation.** Manual review of the Dataverse Roles UI sees assigned roles, not the combined effective scope from roles, team membership, OWD defaults, and sharing rules together. This trace computes effective scope from all four layers before any gap hunt begins.

**Blind spot 2 -- Post-incident FLS discovery.** Field-Level Security gaps surface in incident response, not pre-release audit. No Dataverse UI enumerates FLS coverage across all sensitive fields simultaneously. This trace enumerates every PII, Financial, and Audit/Compliance field against its FLS profile.

**Blind spot 3 -- OWD-sharing-rule override blindness.** Private OWD does not prevent independently-configured sharing rules from reopening access. Manual OWD review does not cross-reference sharing rules. This trace cross-references both.

Each Phase 2 and Phase 3 subsection names the blind spot it resolves.

---

## PHASE 0 -- FULL AUDIT CHAIN GATE

**Complete this phase and write the ACTIVATION STATE LOG before Phase 1 content.**

**Chain 1 -- Discovery to register (Phases 1-4):** Discovered In set at discovery time, not reconstructed.

**Chain 2 -- Register to remediation echo (Phase 5a):** Verbatim slot-fill. Phase 5b is **precondition for closing the trace, not a recommended step**.

**Per-row FLS trigger -- ACTIVE:** FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED. CLOSED required before next entry. N/A markers make trigger completeness provable from output alone.

**Remediation template (pre-declared):**
```
Gap [ID] (Discovered In: [verbatim]):
  Config change:     [exact element and location]
  Expected state:    [UI view after fix]
  Verification step: [executable action]
```

**PROTOCOL REGISTRY (C-26 pre-declaration; C-28 activation-class designation; C-29 phase-anchored detection):**

Pre-declared before Phase 1. Column headers embed criterion identifiers. Each row is an authoritative obligation record.

| REGISTRY-ID | Protocol Name | Activation Class (DEFERRED-PENDING or IMMEDIATELY-ACTIVE per C-28) | State at Phase 0 Close | Activation Point(s) | Broken-Obligation Note (C-28: semantics must match state class) | Detection Phase (C-29: named phase where broken obligation becomes visible) |
|-------------|--------------|-------------------------------------------------------------------|----------------------|--------------------|-----------------------------------------------------------------|---------------------------------------------------------------------------|
| PR-OBL-01 | STEP-1-CLOSE-TOKEN (C-24 chain anchor) | **DEFERRED-PENDING** -- activation point is Phase 1c Step 1 close, which is outside Phase 0 | **PENDING** | Phase 1c Step 1 close (sole activation point) | Unresolved PENDING at trace close = broken obligation | **Phase 5b** -- a trace reaching Phase 5b with STEP-1-CLOSE-TOKEN still PENDING has a visibly broken chain anchor |
| PR-OBL-02 | Per-Stage Chain-Reminder (C-25 annotation) | **IMMEDIATELY-ACTIVE** -- active from Phase 0 itself; first activation at LIVE GAPS REGISTER header immediately below | **ACTIVE** | First: LIVE GAPS REGISTER header (below). Subsequent: every FLS ENTRY block open in Phase 1c | Absence at any named consumption point (FLS ENTRY block open) is a broken state -- not deferred to the next block | N/A -- IMMEDIATELY-ACTIVE class; broken state is observable at each absent FLS ENTRY block open without waiting for a deferred detection phase |

**Emission format for PR-OBL-01 (Phase 1c Step 1 close):**
```
STEP-1-CLOSE-TOKEN -- ACTIVATED [PR-OBL-01: DEFERRED-PENDING -> RESOLVED]
  Category table total rows analyzed: [N]
  FLS-scope rows (PII + Financial + Audit/Compliance): [M]
  Chain anchor value: [M]
  PENDING status: RESOLVED -- references Phase 0 PROTOCOL REGISTRY PR-OBL-01
```

**Annotation form for PR-OBL-02 (LIVE GAPS REGISTER header and every FLS ENTRY block open):**
```
[Category chain: active -- inherit from Step 1] [PR-OBL-02: IMMEDIATELY-ACTIVE -- absence is a broken state]
```

**PHASE 0 GATE -- ACTIVATION STATE LOG:**

Execution record. PROTOCOL REGISTRY above is authoritative. Each LOG row references its REGISTRY-ID and activation class label.

| Mechanism | REGISTRY-ID | Activation Class (C-28) | Status | Notes |
|-----------|------------|------------------------|--------|-------|
| Chain 1 -- discovery -> register | -- | -- | ACTIVE | Governs Phases 1-4 |
| Chain 2 -- register -> Phase 5a verbatim echo | -- | -- | ACTIVE | Phase 5b precondition |
| Per-row FLS trigger -- ENTRY / SLOT / CLOSED | -- | -- | ACTIVE | CLOSED required |
| Remediation template -- three fields | -- | -- | ACTIVE | All fields required |
| Mismatch example -- Phase 5b self-check | -- | -- | LOADED | Precondition for trace close |
| I-6 category drift / PR-1 | -- | -- | ACTIVE | Fires on re-derivation |
| STEP-1-CLOSE-TOKEN; **REGISTRY PR-OBL-01** | PR-OBL-01 | DEFERRED-PENDING | PENDING | Activation: Phase 1c Step 1 close. Phase 5b detection. |
| Per-stage chain-reminder; **REGISTRY PR-OBL-02** | PR-OBL-02 | IMMEDIATELY-ACTIVE | ACTIVE | First activation: LIVE GAPS REGISTER header. |

*PR-OBL-01 DEFERRED-PENDING. PR-OBL-02 IMMEDIATELY-ACTIVE. PROTOCOL REGISTRY is authoritative. Entering PHASE 1.*

---

## LIVE GAPS REGISTER

**[Category chain: active -- inherit from Step 1] [PR-OBL-02: IMMEDIATELY-ACTIVE -- absence is a broken state]** *(Per-stage chain-reminder -- first activation per PROTOCOL REGISTRY)*

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

---

## PHASE 1 -- ENTITY AND ROLE MAP

**1a -- Entity and OWD inventory:** *(Resolves blind spot 1 -- OWD layer)*

| Entity | Org-Wide Default | Scope | Default access for unauthenticated user |
|--------|-----------------|-------|----------------------------------------|

OWD scope: Organization / Business Unit / Owner. Missing scope = incomplete row.

**1b -- Operation-role matrix:** *(Resolves blind spot 1 -- combined effective scope)*

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Dataverse system names required. Highest-privilege role first; CS and SE as structural deltas.

**1c -- Sensitive field categorization:** *(Resolves blind spot 2 -- FLS pre-incident)*

**Inertia threat inventory:**

| ID | Threat | Fires During | Marker |
|----|--------|-------------|--------|
| I-1 | OWD defaults | Phase 1a | ESCALATION-PATH |
| I-2 | Missing FLS | Phase 1c | MISSING-FLS |
| I-3 | Sharing rule overrides | Phase 1d | SHARING-CONFLICT |
| I-4 | Team membership injection | Phase 2a | TEAM-GAP |
| I-5 | Cross-entity hops | Phase 2b | CROSS-ENTITY |
| I-6 | Category drift | Phase 1c Step 2 onward | CATEGORY-DRIFT-VIOLATION |

**PR-1: Category propagation contract:** Category in FLS ENTRY blocks inherits from Step 1 -- not re-derived inline.

Step 1: category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII | |
| | Financial | |
| | Audit/Compliance | |
| | Operational | |

**Step 1 close -- PR-OBL-01 activation (DEFERRED-PENDING -> RESOLVED):**

```
STEP-1-CLOSE-TOKEN -- ACTIVATED [PR-OBL-01: DEFERRED-PENDING -> RESOLVED]
  Category table total rows analyzed: [N]
  FLS-scope rows (PII + Financial + Audit/Compliance): [M]
  Chain anchor value: [M]
  PENDING status: RESOLVED -- references Phase 0 PROTOCOL REGISTRY PR-OBL-01
```

Gate row 5 will carry PR-OBL-01 anchor [M] vs section-close annotation count [M]. Non-vacuous comparison.

Step 2: FLS check for all PII, Financial, and Audit/Compliance fields.

**Block format -- mandatory per sensitive field:**

```
[Category chain: active -- inherit from Step 1] [PR-OBL-02: IMMEDIATELY-ACTIVE -- absence is a broken state]
FLS ENTRY [n] -- [Entity].[Field]
| Entity | Field | Category | FLS Profile? | CS: Read | CS: Write | Expert: Read | Expert: Write | Gap? |
|--------|-------|----------|-------------|----------|-----------|--------------|---------------|------|

REGISTER SLOT [n] (Chain 1 -- complete before CLOSED):
```

Gap? = YES -> register. Gap? = NO -> "-> No gap. Register slot: N/A."

```
FLS ENTRY [n] CLOSED
```

Section close:
```
Phase 1c FLS complete.
  FLS ENTRY blocks: [N] / CLOSED markers: [N] (must equal [N])
  YES entries: [N] / N/A: [N]
  PR-OBL-02 annotations at block opens: [N] (must equal [N])
  Downstream category annotation count: [M]
  (Gate row 5 non-vacuous: PR-OBL-01 anchor [M] vs downstream count [M])
```

**1d -- Sharing rule inventory:** *(Resolves blind spot 3 -- OWD-sharing override)*

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

Conflicts = YES -> register SHARING-CONFLICT. None -> "Phase 1d: no SHARING-CONFLICT -- [rules checked, reason]."

---

## PHASE 2 -- TEAM AND CROSS-ENTITY

**2a:** *(Blind spot 1 -- team injection layer)* Finding / rule-out with specific evidence.

**2b:** Two-hop chain from highest-sensitivity entity. INTENTIONAL or EMERGENT.

---

## PHASE 3 -- PER-ROLE ESCALATION ANALYSIS

One subsection per role.

**Role: [name]** -- Team Write / Role Assignment Write / Assign scope / BU Write.
Conclusion: ESCALATION-PATH FOUND / RULED OUT.

**Negative-check evidence:** "Checked [items]; [type] does not apply because [reason]."

---

## PHASE 4 -- ROLE DIFFERENTIATION

**Customer Service Representative:** CRUD + scope. Sensitive field access -- appropriate or overreach?
**Dataverse Security Expert:** CRUD + scope. Every privilege CS lacks. Least-privilege or overreach?
**Contrast statement (required):** One paragraph, both role names explicit.

---

## PHASE 5a -- REMEDIATION ENTRIES

Verbatim Discovered In. Three-field template per Phase 0.

```
Gap [ID] (Discovered In: [verbatim]):
  Config change:     [exact element and location]
  Expected state:    [UI view after fix]
  Verification step: [executable action]
```

---

## PHASE 5b -- CHAIN 2 SELF-CHECK CLOSE

**Precondition for closing the trace, not a recommended step.**

| Gap ID | Register: Discovered In (exact text) | Phase 5a Echo: Discovered In (exact text) | Match? |
|--------|--------------------------------------|-------------------------------------------|--------|

**TRACE CLOSE TOKEN:** `Chain 2 self-check applied. Rows: [N]. FAIL corrections: [N]. Trace closed.`

---

## SUBMISSION GATE

**ANTI-SPECULATION MANDATE -- VERDICT-FAIL before the table header.** No gate row may record PASS without citing specific evidence.

| Row | Check | Evidence Cited | Status |
|-----|-------|----------------|--------|
| 1 | All entities Phase 1a with OWD and scope | Phase 1a row count and scope values | PASS / VERDICT-FAIL |
| 2 | All roles by Dataverse system name; record scope per entity | Phase 1b role names and Record Scope column | PASS / VERDICT-FAIL |
| 3 | FLS analyzed; CLOSED; PR-OBL-02 annotation count equals block count | Phase 1c close: N blocks, N CLOSED, N PR-OBL-02 annotations | PASS / VERDICT-FAIL |
| 4 | Gap types checked; negative-check evidence present | Phase 3 statements and Phase 2 rule-outs | PASS / VERDICT-FAIL |
| 5 | Non-vacuous token-swap: (a) PR-OBL-01 DEFERRED-PENDING anchor [M] -- resolved at Phase 1c Step 1 close, ACTIVATED token references PROTOCOL REGISTRY; (b) section-close annotation count [M] -- separately declared; (c) [M] == [M]? YES/NO; (d) PR-1: no CATEGORY-DRIFT-VIOLATION; (e) rows 1-4 PASS | ACTIVATED token with PR-OBL-01 RESOLVED label, section-close count, rows 1-4 | PASS / VERDICT-FAIL |
