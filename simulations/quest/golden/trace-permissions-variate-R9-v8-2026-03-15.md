# trace-permissions Variate — Round 9 (rubric v8 — C-26/C-27 target)
**Date:** 2026-03-15
**Rubric:** v8 (C-01 through C-27 — C-26/C-27 added from Round 8 excellence signals)
**Target criteria:** C-26 (Phase 0 body-level protocol pre-declaration with PENDING → ACTIVATED lifecycle), C-27 (rubric-verbatim pass-condition language at enforcement instruction sites)

**State entering Round 9:**

| Variation | R8 score | Gap under v8 |
|-----------|----------|--------------|
| R8-V-05 (best v8) | 180/180 | Missing C-26/C-27 (-10 pts) = 180/190 |

R8-V-04 pre-declares STEP-1-CLOSE-TOKEN in the ACTIVATION STATE LOG with a PENDING state and activation note — the structural move that becomes C-26. R8-V-05 adds rubric-verbatim language at enforcement points — the move that becomes C-27. Neither Round 8 variation satisfies both simultaneously as formally specified criteria.

C-26 gap in R8-V-05: STEP-1-CLOSE-TOKEN appears in the ACTIVATION STATE LOG as PENDING with an activation note, but not as a named Phase 0 body block. C-26 requires: (a) a Phase 0 body-level named block independent of the LOG row, (b) explicit PENDING state with stated activation point, (c) broken-obligation note ("unresolved PENDING at trace close = broken obligation"), (d) `PENDING status: RESOLVED` marker at the activation point referencing the Phase 0 body declaration.

C-27 gap in R8-V-05: Enforcement instruction sites use descriptive labels rather than the exact rubric pass-condition phrases. C-27 requires the C-24 phrase ("named close token recording the exact count of items analyzed") and the C-25 consumption-point requirement to appear verbatim at: Step 1 close instruction label, Phase 1c section close field label, gate row 5 description, PR-1 text, block format definition.

---

## Round 9 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Single-axis: Lifecycle emphasis — C-26 isolation: Phase 0 body-level named protocol blocks for STEP-1-CLOSE-TOKEN and per-stage chain-reminder, each carrying PENDING state + activation point + broken-obligation note; Step 1 close emits `PENDING status: RESOLVED` referencing Phase 0 body declaration; enforcement instruction labels remain descriptive (C-27 not targeted) | R8-V-05 has STEP-1-CLOSE-TOKEN in the ACTIVATION STATE LOG as PENDING with an activation note — the obligation exists as a LOG row but not as a Phase 0 body block reviewable independently of the LOG table. C-26 requires the protocol to appear as a named body block so a reviewer reading Phase 0 encounters a complete obligation record before reaching the LOG. V-01 adds two named body blocks (one per protocol) before the ACTIVATION STATE LOG, each with the four C-26 requirements. Step 1 close emits `PENDING status: RESOLVED — references Phase 0 STEP-1-CLOSE-TOKEN protocol declaration`. No rubric-verbatim enforcement labels — C-27 not targeted. Hypothesis: +5 pts (C-26 only); C-27 fails. |
| V-02 | Single-axis: Phrasing register — C-27 isolation: rubric-verbatim C-24 pass-condition phrase at Step 1 close instruction label; rubric-verbatim C-25 consumption-point phrase at Phase 1c section close label, gate row 5 description, PR-1 text, and block format definition; Phase 0 body structure unchanged from R8-V-05 (C-26 not targeted) | R8-V-05 uses descriptive enforcement labels. C-27 requires the exact rubric pass-condition phrase at each enforcement site so the site is self-auditing — a reviewer matches enforcement text against the rubric without re-reading the specification. V-02 replaces descriptive labels with rubric-exact phrases at the five named enforcement sites, leaving Phase 0 body structure unchanged (ACTIVATION STATE LOG PENDING row for STEP-1-CLOSE-TOKEN, no body block). C-26 fails by design. Hypothesis: +5 pts (C-27 only). |
| V-03 | Single-axis: Role sequence — ceiling-first delta framing with DELTA-FROM-CEILING annotations: highest-privilege role established first in Phase 1b; CS and SE rows each carry explicit DELTA-FROM-CEILING field listing absent privileges; no C-26 body blocks; no C-27 verbatim labels (control variation) | R8-V-05 follows CS → SE sequence without an explicit ceiling establishment pass. V-03 inserts a ceiling pass at Phase 1b open; each non-ceiling role row carries a DELTA-FROM-CEILING annotation. Tests whether ceiling-delta framing strengthens C-10 independently of C-26/C-27. Neither C-26 nor C-27 mechanisms are added — confirms that ceiling framing alone does not produce false C-26/C-27 scores. Hypothesis: +0 pts for C-26/C-27 (control); C-10 ceiling-delta framing gain measured independently. |
| V-04 | Combined: C-26 + C-27 — Phase 0 body-level protocol blocks (C-26) + rubric-verbatim enforcement labels (C-27) on R8-V-05 structural base | V-01 establishes C-26 (body blocks + RESOLVED marker); V-02 establishes C-27 (verbatim labels). Mechanisms operate at non-overlapping structural sites: C-26 modifies Phase 0 body and the Step 1 close RESOLVED marker; C-27 modifies enforcement instruction labels at five sites. No structural conflict. V-04 combines both on the R8-V-05 base (STEP-1-CLOSE-TOKEN, per-stage chain-reminder, bidirectional chain, ceiling-first roles, prior criteria all preserved). Hypothesis: 190/190. |
| V-05 | Combined + obligation lifecycle IDs: V-04 structure with named obligation identifiers (OBL-01 for STEP-1-CLOSE-TOKEN, OBL-02 for per-stage chain-reminder) threading through every enforcement site — each site carries both its lifecycle state marker and its rubric-verbatim phrase, making it independently self-auditing without Phase 0 cross-reference | V-04 satisfies C-26 and C-27 but an auditor reading gate row 5 must recall Phase 0 to confirm the RESOLVED marker references the correct declaration. V-05 adds obligation IDs that thread every site: Phase 0 assigns OBL-01 to STEP-1-CLOSE-TOKEN and OBL-02 to per-stage chain-reminder. Step 1 close carries `PENDING status: RESOLVED [OBL-01]` + C-24 rubric phrase. Phase 1c section close carries `[OBL-01 downstream consumption point]` + C-25 phrase. Gate row 5 carries `[OBL-01 chain verification]`. PR-1 carries `[OBL-02 source declaration]`. Block format carries `[OBL-02 per-block activation]`. Each site names its obligation ID and rubric criterion — no Phase 0 lookup required. Hypothesis: 190/190 with maximum reviewer independence. |

---

## V-01 — Single-Axis: Phase 0 Body-Level Protocol Pre-Declaration (C-26 Isolation)

**Axis:** Lifecycle emphasis — named protocol body blocks in Phase 0 with PENDING state + activation point + broken-obligation note; `PENDING status: RESOLVED` at Step 1 close referencing Phase 0 body declaration; enforcement instruction labels remain descriptive (C-27 not targeted)
**Hypothesis:** R8-V-05 pre-declares STEP-1-CLOSE-TOKEN in the ACTIVATION STATE LOG as a PENDING row. The obligation exists in the LOG but not as a Phase 0 body block with a reviewable structure independent of the table. C-26 requires the protocol to appear as a named body block — a reviewer reading Phase 0 encounters the complete obligation (definition, state, activation point, broken-obligation consequence) before reaching the LOG. V-01 adds two named body blocks before the ACTIVATION STATE LOG, each carrying all four C-26 requirements. Step 1 close emits `PENDING status: RESOLVED — references Phase 0 STEP-1-CLOSE-TOKEN protocol declaration`. No rubric-verbatim labels added.

---

You are running a permissions trace signal for: {{topic}}

---

## PHASE 0 — FULL AUDIT CHAIN GATE

**Complete this phase and write the ACTIVATION STATE LOG before Phase 1 content.**

This trace operates under a bidirectional audit chain. Both directions pre-established here and active for the full output.

**Chain 1 — Discovery to register (active during Phases 1–4):**
Every gap found during Phases 1–4 is entered into the LIVE GAPS REGISTER at the moment of discovery. The Discovered In field records the exact section and context — e.g., "Phase 1c FLS check — Contact.AnnualRevenue". Set at discovery time, not reconstructed.

**Chain 2 — Register to remediation echo (active during Phase 5a):**
Every register entry is echoed in Phase 5a via verbatim slot-fill. Chain 2 is verified in Phase 5b — that verification is a **precondition for closing the trace, not a recommended step**.

**Per-row FLS trigger — ACTIVE now:**
During Phase 1c, the three-part FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED block format is active. The CLOSED terminator is required before any subsequent FLS ENTRY begins. **Co-authorship is a structural property of the format**. N/A markers on NO-gap REGISTER SLOTs make **trigger completeness provable from the output alone**.

**Remediation template (pre-declared; applied in Phase 5a to every register entry):**

```
Gap [ID] (Discovered In: [verbatim from register — Chain 2 slot-fill]):
  Config change:     [exact configuration element — role / field / profile / rule and location]
  Expected state:    [UI view or query after fix]
  Verification step: [executable action — UI location and expected result]
```

**Protocol: STEP-1-CLOSE-TOKEN (C-24 chain anchor — C-26 Phase 0 body pre-declaration)**

This protocol is pre-declared here as a named Phase 0 body block. Its ACTIVATION STATE LOG entry below tracks execution status; this block is the authoritative obligation record.

Definition: At Phase 1c Step 1 close, emit this named artifact. The Phase 1c section close must independently declare the downstream FLS ENTRY Category annotation count. Gate row 5 performs a non-vacuous numerical comparison between the chain anchor value and the section-close annotation count.

Emission format (required at Phase 1c Step 1 close):
```
STEP-1-CLOSE-TOKEN — ACTIVATED
  Category table total rows analyzed: [N]
  FLS-scope rows (PII + Financial + Audit/Compliance): [M]
  Chain anchor value: [M]
  PENDING status: RESOLVED — references Phase 0 STEP-1-CLOSE-TOKEN protocol declaration
```

**C-26 obligation record:**
Status at Phase 0 close: **PENDING**
Activation point: Phase 1c Step 1 close
Broken-obligation note: **Unresolved PENDING at trace close = broken obligation.** A trace that reaches Phase 5b with STEP-1-CLOSE-TOKEN still PENDING has a visibly broken chain anchor — detectable without reading gate row 5.

**Protocol: Per-Stage Chain-Reminder (C-25 consumption-point annotation — C-26 Phase 0 body pre-declaration)**

This protocol is pre-declared here as a named Phase 0 body block.

Definition: The annotation `[Category chain: active — inherit from Step 1]` must appear as the first line of every FLS ENTRY block — before the block's table header. The same annotation must appear at the LIVE GAPS REGISTER section header. This converts the PR-1 propagation contract from a single-point declaration into a continuously visible constraint at each consumption site.

**C-26 obligation record:**
Status at Phase 0 close: **ACTIVE** (first activation: LIVE GAPS REGISTER section header, immediately below)
Subsequent activation points: every FLS ENTRY block open in Phase 1c
Broken-obligation note: **Absence at any FLS ENTRY block open is a broken state — not deferred to the next block.**

**PHASE 0 GATE — ACTIVATION STATE LOG:**

This log is an **execution record, not a declarative checklist**. PENDING entries have a named activation point — reaching that point without the mechanism firing = broken state. Body-level protocol blocks above are authoritative obligation records; LOG rows track execution status.

| Mechanism | Status | Notes |
|-----------|--------|-------|
| Chain 1 — discovery → register, Discovered In set at point of discovery | ACTIVE | Governs all register entries in Phases 1–4 |
| Chain 2 — register → Phase 5a verbatim echo, copy-not-write | ACTIVE | Verified in Phase 5b (structural precondition for trace close) |
| Per-row FLS trigger — FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED | ACTIVE | Structural format; CLOSED terminator required |
| Remediation template — Config change / Expected state / Verification step | ACTIVE | All three fields required |
| Mismatch example — Phase 5b self-check instrument | LOADED | Phase 5b self-check is a precondition for trace close |
| I-6 category drift / PR-1 — CATEGORY-DRIFT-VIOLATION marker | ACTIVE | Fires during Phase 1c Step 2 on any re-derivation of Step 1 category labels |
| STEP-1-CLOSE-TOKEN — named chain anchor; **body protocol block declared above** | PENDING | Activation point: Phase 1c Step 1 close. Unresolved PENDING = broken obligation. |
| Per-stage chain-reminder — `[Category chain: active — inherit from Step 1]` at FLS ENTRY block open and Gap Register header; **body protocol block declared above** | ACTIVE | First activation: LIVE GAPS REGISTER header. Fires at every FLS ENTRY block open. |

*All mechanisms ACTIVE or LOADED. STEP-1-CLOSE-TOKEN PENDING — body-level protocol declaration above is authoritative. Entering PHASE 1.*

---

## LIVE GAPS REGISTER

Opened at Phase 0. Populated inline during Phases 1–4. Chain 1 enforcement point.

**[Category chain: active — inherit from Step 1 for all category-related findings in this register]** *(Per-stage chain-reminder (C-25) — first activation per Phase 0 body protocol declaration)*

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

- **Discovered In**: exact section name and context, set at discovery time — not reconstructed
- Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY / CATEGORY-DRIFT
- Severity: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 — ENTITY AND ROLE MAP

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Scope | Default access for unauthenticated user |
|--------|-----------------|-------|----------------------------------------|

OWD scope: Organization / Business Unit / Owner. Missing scope = incomplete row.

Chain 1 check after 1a: OWD anomaly → register (Discovered In: "Phase 1a OWD — [entity]"). None → "Phase 1a: no OWD anomalies — [basis]."

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Team / User / Sharing-[rule name]. All roles with any privilege. Dataverse system names required — display names alone fail C-01. Highest-privilege role first; CS and SE expressed as deltas.

Chain 1 check after 1b: Scope anomaly → register. None → "Phase 1b: no scope anomalies — [basis]."

**1c — Sensitive field categorization:**

**Inertia threat inventory (declared before Step 1):**

| ID | Threat | Fires During | Marker |
|----|--------|-------------|--------|
| I-1 | OWD defaults creating unexpected default access | Phase 1a | ESCALATION-PATH (OWD scope) in register |
| I-2 | Missing FLS profiles on PII, Financial, or Audit/Compliance fields | Phase 1c FLS check | MISSING-FLS in register |
| I-3 | Sharing rule overrides granting unintended access | Phase 1d | SHARING-CONFLICT in register |
| I-4 | Team membership control enabling privilege injection | Phase 2a | TEAM-GAP in register |
| I-5 | EMERGENT cross-entity hops | Phase 2b | CROSS-ENTITY in register |
| I-6 | Category drift — re-derivation of PII / Financial / Audit/Compliance / Operational labels downstream of Phase 1c Step 1 | Phase 1c Step 2 onward | CATEGORY-DRIFT-VIOLATION in register |

**PR-1: Category propagation contract:**
The Category column in every FLS ENTRY block must inherit its value from the Step 1 category table — not re-derived inline. Re-derivation fires I-6 → CATEGORY-DRIFT-VIOLATION → register entry. The per-stage chain-reminder (Phase 0 body protocol) is the enforcement mechanism.

Step 1: category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII (name, contact info, ID, government data) | |
| | Financial (billing, pricing, payment, credit) | |
| | Audit/Compliance (modified-by, consent, audit trail) | |
| | Operational (status, queue, SLA, internal notes) | |

Write "none" for empty categories.

**Step 1 close — STEP-1-CLOSE-TOKEN activation (C-26: resolves PENDING from Phase 0 body protocol declaration):**

```
STEP-1-CLOSE-TOKEN — ACTIVATED
  Category table total rows analyzed: [N]
  FLS-scope rows (PII + Financial + Audit/Compliance): [M]
  Chain anchor value: [M]
  PENDING status: RESOLVED — references Phase 0 STEP-1-CLOSE-TOKEN protocol declaration
```

Gate row 5 will compare chain anchor value [M] against Phase 1c section-close downstream annotation count. Both values are separately named. The comparison is non-vacuous.

Step 2: FLS check for all PII, Financial, and Audit/Compliance fields. Per-row trigger ACTIVE.

**Block format — mandatory for every sensitive field:**

Per-stage chain-reminder fires at each block open (Phase 0 body protocol):

```
[Category chain: active — inherit from Step 1]
FLS ENTRY [n] — [Entity].[Field]
| Entity | Field | Category | FLS Profile? | CS: Read | CS: Write | Expert: Read | Expert: Write | Gap? |
|--------|-------|----------|-------------|----------|-----------|--------------|---------------|------|

REGISTER SLOT [n] (Chain 1 — complete before CLOSED marker):
```

If Gap? = YES: enter register. If Gap? = NO: "→ No gap. Register slot: N/A — [confirmation]."

```
FLS ENTRY [n] CLOSED
```

**Block boundary rule:** CLOSED terminator required. Chain-reminder at every block open per Phase 0 body declaration — absence is a broken state. Category must match Step 1 — PR-1 active.

Section close:
```
Phase 1c FLS complete.
  FLS ENTRY blocks: [N]
  CLOSED markers written: [N] (must equal [N])
  YES entries: [N] / N/A register slots: [N]
  Chain-reminder annotations at block opens: [N] (must equal [N])
  Downstream FLS ENTRY Category annotation count: [M]
  (Separately declared for gate row 5 comparison vs STEP-1-CLOSE-TOKEN chain anchor value [M])
```

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

Chain 1 check after 1d: Conflicts = YES → register. None → "Phase 1d: no SHARING-CONFLICT — [rules checked, reason]."

---

## PHASE 2 — TEAM AND CROSS-ENTITY

**2a — Team membership gap:**
Finding: `[Role] → [Team X] → [elevated access] — mechanism: [how]`
Rule-out: "Checked [teams]: no injection path — [reason]."
Chain 1 check: TEAM-GAP if found.

**2b — Cross-entity permission chain:**
Highest-sensitivity entity (justify from Phase 1c Step 1). Two hops: `[Role] → [Entity A, op: X, scope: Y] → [Relationship] → [Entity B, op: X, scope: Y]`. INTENTIONAL or EMERGENT.

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

One subsection per role. No collective statements.

**Role: [name]**
- Team membership Write: [YES / NO — evidence]
- Security role assignment Write: [YES / NO — evidence]
- Record ownership Assign scope: [scope — elevation?]
- Business unit configuration Write: [YES / NO — evidence]

Conclusion: ESCALATION-PATH FOUND / RULED OUT.

**Negative-check evidence per gap type:** "Checked [items] for [roles]; [type] does not apply because [specific reason]."

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative:** CRUD + scope. Sensitive field access from Phase 1c Step 1 — appropriate or overreach?
**Dataverse Security Expert:** CRUD + scope. Every privilege CS lacks. Least-privilege or overreach?
**Contrast statement (required):** One paragraph, both role names explicit.
Chain 1 check: undocumented gaps → register.

---

## PHASE 5a — REMEDIATION ENTRIES

Chain 2 active. Copy Discovered In verbatim. All three template fields required.

```
Gap [ID] (Discovered In: [verbatim copy — Chain 2 slot-fill]):
  Config change:     [exact element and location]
  Expected state:    [UI view after fix]
  Verification step: [executable action]
```

---

## PHASE 5b — CHAIN 2 SELF-CHECK CLOSE

**Precondition for closing the trace.**

Mismatch example loaded at Phase 0. PASSING = verbatim. FAILING = truncated / dropped / rephrased.

| Gap ID | Register: Discovered In (exact text) | Phase 5a Echo: Discovered In (exact text) | Match? |
|--------|--------------------------------------|-------------------------------------------|--------|

**TRACE CLOSE TOKEN:** `Chain 2 self-check applied: all Discovered In echoes verified verbatim. Rows: [N]. FAIL corrections: [N]. Trace closed.`

---

## SUBMISSION GATE

**ANTI-SPECULATION MANDATE — VERDICT-FAIL before the table header:** No gate row may record PASS without citing specific evidence.

| Row | Check | Evidence Cited | Status |
|-----|-------|----------------|--------|
| 1 | All entities Phase 1a with OWD and scope | Cite Phase 1a row count and scope values | PASS / VERDICT-FAIL |
| 2 | All roles by Dataverse system name; record scope per entity | Cite Phase 1b role names and Record Scope column | PASS / VERDICT-FAIL |
| 3 | FLS analyzed for all sensitive fields; all CLOSED; chain-reminder count equals block count | Cite Phase 1c close: N blocks, N CLOSED, N chain-reminder annotations | PASS / VERDICT-FAIL |
| 4 | All gap types checked; negative-check evidence present | Cite Phase 3 statements and Phase 2 rule-outs | PASS / VERDICT-FAIL |
| 5 | Non-vacuous token-swap: (a) STEP-1-CLOSE-TOKEN chain anchor [M] — PENDING resolved at Phase 1c Step 1 close, RESOLVED marker references Phase 0 body protocol declaration; (b) Phase 1c section-close annotation count [M] — separately declared; (c) [M] == [M]? YES/NO; (d) PR-1 — no CATEGORY-DRIFT-VIOLATION; (e) rows 1–4 PASS | Cite STEP-1-CLOSE-TOKEN ACTIVATED block (with RESOLVED marker referencing Phase 0 body), Phase 1c section-close count, rows 1–4 | PASS / VERDICT-FAIL |

---

## V-02 — Single-Axis: Rubric-Verbatim Enforcement Labels (C-27 Isolation)

**Axis:** Phrasing register — rubric-exact C-24 pass-condition phrase at Step 1 close instruction label; rubric-exact C-25 consumption-point phrase at Phase 1c section close label, gate row 5 description, PR-1 text, and block format definition; Phase 0 body structure unchanged from R8-V-05 (C-26 not targeted)
**Hypothesis:** R8-V-05 uses descriptive enforcement labels. C-27 requires the exact rubric pass-condition phrase at each enforcement site — the site becomes self-auditing without requiring the reviewer to re-read the rubric. V-02 changes five enforcement instruction sites to rubric-exact phrases: (1) Step 1 close: "emit a named close token recording the exact count of items analyzed"; (2) Phase 1c section close: C-25 consumption-point phrase; (3) gate row 5: "non-vacuous numerical comparison" + C-25 per-stage requirement; (4) PR-1: "converts the propagation contract from a single-point declaration to a continuously-visible constraint"; (5) block format definition: exact annotation form `[Category chain: active — inherit from Step N]`. Phase 0 keeps R8-V-05's ACTIVATION STATE LOG PENDING row without body-block expansion. C-26 fails by design.

---

You are running a permissions trace signal for: {{topic}}

---

## PHASE 0 — FULL AUDIT CHAIN GATE

**Complete this phase and write the ACTIVATION STATE LOG before Phase 1 content.**

This trace operates under a bidirectional audit chain. Both directions pre-established here and active for the full output.

**Chain 1 — Discovery to register (active during Phases 1–4):**
Every gap found during Phases 1–4 is entered into the LIVE GAPS REGISTER at the moment of discovery. Discovered In set at discovery time, not reconstructed.

**Chain 2 — Register to remediation echo (active during Phase 5a):**
Every register entry echoed in Phase 5a via verbatim slot-fill. Verified in Phase 5b — **precondition for closing the trace**.

**Per-row FLS trigger — ACTIVE now:**
Three-part FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED format active during Phase 1c. CLOSED terminator required. Co-authorship is structural. N/A markers make trigger completeness provable.

**Remediation template (pre-declared):**
```
Gap [ID] (Discovered In: [verbatim — Chain 2 slot-fill]):
  Config change:     [exact element and location]
  Expected state:    [UI view or query after fix]
  Verification step: [executable action]
```

**C-24 chain anchor — STEP-1-CLOSE-TOKEN protocol:**
At Phase 1c Step 1 close, emit the STEP-1-CLOSE-TOKEN named artifact with chain anchor value [M]. Phase 1c section close independently declares the downstream annotation count. Gate row 5 performs a non-vacuous numerical comparison.

**PHASE 0 GATE — ACTIVATION STATE LOG:**

This log is an **execution record, not a declarative checklist**.

| Mechanism | Status | Notes |
|-----------|--------|-------|
| Chain 1 — discovery → register, Discovered In set at discovery time | ACTIVE | Governs Phases 1–4 |
| Chain 2 — register → Phase 5a verbatim echo | ACTIVE | Phase 5b verification is precondition for trace close |
| Per-row FLS trigger — FLS ENTRY / REGISTER SLOT / CLOSED | ACTIVE | CLOSED required before next entry |
| Remediation template — Config change / Expected state / Verification step | ACTIVE | All three fields required |
| Mismatch example — Phase 5b self-check instrument | LOADED | Precondition for trace close |
| I-6 category drift / PR-1 — CATEGORY-DRIFT-VIOLATION marker | ACTIVE | Fires on re-derivation during Phase 1c Step 2 onward |
| STEP-1-CLOSE-TOKEN (C-24) — named chain anchor at Phase 1c Step 1 close | PENDING | Set at Phase 1c Step 1 close; consumed by Phase 1c section close and gate row 5 |
| Per-stage chain-reminder (C-25) — `[Category chain: active — inherit from Step N]` at FLS ENTRY block open and Gap Register header | ACTIVE | First activation: LIVE GAPS REGISTER header |

*All mechanisms ACTIVE or LOADED. STEP-1-CLOSE-TOKEN PENDING — will be set at Phase 1c Step 1 close. Entering PHASE 1.*

---

## LIVE GAPS REGISTER

**[Category chain: active — inherit from Step 1]** *(Per-stage chain-reminder (C-25) — first activation)*

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

---

## PHASE 1 — ENTITY AND ROLE MAP

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Scope | Default access for unauthenticated user |
|--------|-----------------|-------|----------------------------------------|

OWD scope: Organization / Business Unit / Owner. Missing scope = incomplete row.

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Dataverse system names required. Record Scope: Org / BU / Team / User / Sharing-[rule name].

**1c — Sensitive field categorization:**

**Inertia threat inventory:**

| ID | Threat | Fires During | Marker |
|----|--------|-------------|--------|
| I-1 | OWD defaults creating unexpected default access | Phase 1a | ESCALATION-PATH |
| I-2 | Missing FLS profiles on PII, Financial, or Audit/Compliance | Phase 1c FLS check | MISSING-FLS |
| I-3 | Sharing rule overrides granting unintended access | Phase 1d | SHARING-CONFLICT |
| I-4 | Team membership control enabling privilege injection | Phase 2a | TEAM-GAP |
| I-5 | EMERGENT cross-entity hops | Phase 2b | CROSS-ENTITY |
| I-6 | Category drift — re-derivation of labels downstream of Step 1 | Phase 1c Step 2 onward | CATEGORY-DRIFT-VIOLATION |

**PR-1: Category propagation contract — converts the propagation contract from a single-point declaration to a continuously-visible constraint (C-25 rubric phrase):**
Category in every FLS ENTRY block inherits from Step 1 — not re-derived inline. Re-derivation fires I-6. The per-stage chain-reminder annotation at each FLS ENTRY block open is the mechanism that converts this contract from single-point declaration to continuously visible constraint.

Step 1: category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII | |
| | Financial | |
| | Audit/Compliance | |
| | Operational | |

**Step 1 close — emit a named close token recording the exact count of items analyzed (C-24 rubric phrase — chain anchor):**

```
STEP-1-CLOSE-TOKEN — ACTIVATED
  Category table total rows analyzed: [N]
  FLS-scope rows (PII + Financial + Audit/Compliance): [M]
  Chain anchor value: [M]
  Phase 0 PENDING status: RESOLVED
```

Step 2: FLS check for all PII, Financial, and Audit/Compliance fields.

**Block format — mandatory per sensitive field; consumption-point chain-reminder required at block open (C-25: `[Category chain: active — inherit from Step N]` exact form required at each consumption point):**

```
[Category chain: active — inherit from Step 1]
FLS ENTRY [n] — [Entity].[Field]
| Entity | Field | Category | FLS Profile? | CS: Read | CS: Write | Expert: Read | Expert: Write | Gap? |
|--------|-------|----------|-------------|----------|-----------|--------------|---------------|------|

REGISTER SLOT [n] (Chain 1 — complete before CLOSED marker):
```

If Gap? = YES: enter register. If Gap? = NO: "→ No gap. Register slot: N/A."

```
FLS ENTRY [n] CLOSED
```

Section close — downstream annotation count declared separately; C-25 consumption-point chain-reminder count verified:
```
Phase 1c FLS complete.
  FLS ENTRY blocks: [N] / CLOSED markers: [N]
  YES entries: [N] / N/A register slots: [N]
  Chain-reminder annotations at block opens: [N] (must equal [N] — C-25 per-stage consumption-point verification: converts contract to continuously-visible constraint)
  Downstream FLS ENTRY Category annotation count: [M]
  (Separately declared for non-vacuous numerical comparison vs STEP-1-CLOSE-TOKEN anchor [M] at gate row 5 — C-24 rubric phrase)
```

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

---

## PHASE 2 — TEAM AND CROSS-ENTITY

**2a:** Finding: `[Role] → [Team X] → [elevated access]`. Rule-out: "Checked [teams]: no path — [reason]."
**2b:** Two-hop cross-entity chain from highest-sensitivity entity. INTENTIONAL or EMERGENT.

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

One subsection per role.

**Role: [name]**
- Team membership Write: [YES / NO]
- Security role assignment Write: [YES / NO]
- Record ownership Assign scope: [scope]
- Business unit configuration Write: [YES / NO]

Conclusion: ESCALATION-PATH FOUND / RULED OUT.

**Negative-check evidence:** "Checked [items] for [roles]; [type] does not apply because [specific reason]."

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative:** CRUD + scope. **Dataverse Security Expert:** CRUD + scope.
**Contrast statement:** Both role names explicit.

---

## PHASE 5a — REMEDIATION ENTRIES

Verbatim Discovered In. All three template fields.

```
Gap [ID] (Discovered In: [verbatim]):
  Config change: / Expected state: / Verification step:
```

---

## PHASE 5b — CHAIN 2 SELF-CHECK CLOSE

**Precondition for closing the trace.**

| Gap ID | Register: Discovered In | Phase 5a Echo: Discovered In | Match? |
|--------|------------------------|------------------------------|--------|

**TRACE CLOSE TOKEN:** `Chain 2 self-check applied. Rows: [N]. FAIL corrections: [N]. Trace closed.`

---

## SUBMISSION GATE

**ANTI-SPECULATION MANDATE — VERDICT-FAIL before the table header.**

| Row | Check | Evidence Cited | Status |
|-----|-------|----------------|--------|
| 1 | All entities Phase 1a with OWD and scope | Phase 1a row count and scope values | PASS / VERDICT-FAIL |
| 2 | All roles by Dataverse system name; record scope per entity | Phase 1b role names and Record Scope column | PASS / VERDICT-FAIL |
| 3 | FLS analyzed; all CLOSED; chain-reminder count equals block count (C-25: per-stage consumption-point annotation — converts contract to continuously-visible constraint) | Phase 1c close: N blocks, N CLOSED, N chain-reminder annotations | PASS / VERDICT-FAIL |
| 4 | All gap types checked; negative-check evidence present | Phase 3 statements and Phase 2 rule-outs | PASS / VERDICT-FAIL |
| 5 | **Non-vacuous numerical comparison (C-24 rubric phrase):** (a) STEP-1-CLOSE-TOKEN = named close token recording the exact count of items analyzed [M]; (b) Phase 1c section-close annotation count [M] — separately declared; (c) [M] == [M]? YES/NO; (d) PR-1: converts propagation contract from single-point declaration to continuously-visible constraint (C-25 rubric phrase) — no CATEGORY-DRIFT-VIOLATION; (e) rows 1–4 PASS | STEP-1-CLOSE-TOKEN ACTIVATED block, Phase 1c section-close count, rows 1–4 | PASS / VERDICT-FAIL |

---

## V-03 — Single-Axis: Ceiling-First Delta Framing (Control Variation)

**Axis:** Role sequence — highest-privilege role enumerated first in Phase 1b; CS and SE rows each carry DELTA-FROM-CEILING annotation; no C-26 body blocks; no C-27 verbatim labels
**Hypothesis:** R8-V-05 follows CS → SE sequence without an explicit ceiling pass. V-03 inserts a ceiling establishment step at Phase 1b open, then traces CS and SE as structural deltas. Hypothesis: +0 pts for C-26/C-27 (control — confirms ceiling-delta framing does not produce false positives); C-10 ceiling-floor delta gain measured independently. Neither C-26 nor C-27 are targeted.

---

You are running a permissions trace signal for: {{topic}}

---

## PHASE 0 — FULL AUDIT CHAIN GATE

**Complete this phase and write the ACTIVATION STATE LOG before Phase 1 content.**

**Chain 1 — Discovery to register (active during Phases 1–4):** Discovered In set at discovery time, not reconstructed.

**Chain 2 — Register to remediation echo (active during Phase 5a):** Verbatim slot-fill. Phase 5b verification is **precondition for closing the trace**.

**Per-row FLS trigger — ACTIVE:** FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED. CLOSED terminator required.

**Remediation template:**
```
Gap [ID] (Discovered In: [verbatim]):
  Config change: / Expected state: / Verification step:
```

**PHASE 0 GATE — ACTIVATION STATE LOG:**

| Mechanism | Status | Notes |
|-----------|--------|-------|
| Chain 1 — discovery → register | ACTIVE | Governs Phases 1–4 |
| Chain 2 — register → Phase 5a verbatim echo | ACTIVE | Phase 5b precondition |
| Per-row FLS trigger — ENTRY / SLOT / CLOSED | ACTIVE | CLOSED required |
| Remediation template — three fields | ACTIVE | All fields required |
| Mismatch example — Phase 5b self-check | LOADED | Precondition for trace close |
| I-6 category drift / PR-1 — CATEGORY-DRIFT-VIOLATION | ACTIVE | Fires on re-derivation |
| STEP-1-CLOSE-TOKEN (C-24) | PENDING | Activation: Phase 1c Step 1 close |
| Per-stage chain-reminder (C-25) | ACTIVE | First activation: LIVE GAPS REGISTER header |

---

## LIVE GAPS REGISTER

**[Category chain: active — inherit from Step 1]**

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

---

## PHASE 1 — ENTITY AND ROLE MAP

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Scope | Default access for unauthenticated user |
|--------|-----------------|-------|----------------------------------------|

OWD scope: Organization / Business Unit / Owner.

**1b — Operation-role matrix (ceiling-first sequence):**

**CEILING ESTABLISHMENT:** Before CS or SE rows, enumerate the maximum-privilege role for all entities in {{topic}}. All subsequent roles are analyzed as structural deltas from this ceiling.

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope | DELTA-FROM-CEILING |
|--------|------|--------|------|-------|--------|--------|--------------|-------------------|
| | [Highest-privilege role] | | | | | | | — (ceiling) |
| | Customer Service Representative | | | | | | | [every privilege the ceiling has that CS lacks] |
| | Dataverse Security Expert | | | | | | | [every privilege the ceiling has that SE lacks] |

**DELTA-FROM-CEILING:** List each CRUD privilege and scope where the ceiling role exceeds this role. If no delta, state "No delta — equivalent." CS gaps computed from ceiling are structural; CS gaps discovered by inspection are manual — the ceiling-first sequence makes them visible without hunting.

Ceiling-floor trigger: if CS DELTA-FROM-CEILING is empty for any entity, register ESCALATION-PATH — CS scope matches ceiling.

Dataverse system names required.

**1c — Sensitive field categorization:**

**Inertia threat inventory:**

| ID | Threat | Fires During | Marker |
|----|--------|-------------|--------|
| I-1 | OWD defaults creating unexpected access | Phase 1a | ESCALATION-PATH |
| I-2 | Missing FLS on PII, Financial, Audit/Compliance | Phase 1c | MISSING-FLS |
| I-3 | Sharing rule overrides | Phase 1d | SHARING-CONFLICT |
| I-4 | Team membership privilege injection | Phase 2a | TEAM-GAP |
| I-5 | EMERGENT cross-entity hops | Phase 2b | CROSS-ENTITY |
| I-6 | Category drift — re-derivation downstream of Step 1 | Phase 1c Step 2 onward | CATEGORY-DRIFT-VIOLATION |

**PR-1: Category propagation contract:** Category in FLS ENTRY blocks inherits from Step 1 — not re-derived.

Step 1: category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII | |
| | Financial | |
| | Audit/Compliance | |
| | Operational | |

**Step 1 close — STEP-1-CLOSE-TOKEN activation:**
```
STEP-1-CLOSE-TOKEN — ACTIVATED
  Category table total rows: [N] / FLS-scope rows: [M] / Chain anchor: [M]
  Phase 0 PENDING status: RESOLVED
```

Step 2: FLS check. Block format:
```
[Category chain: active — inherit from Step 1]
FLS ENTRY [n] — [Entity].[Field]
| ...table... |

REGISTER SLOT [n]: [Gap entry or N/A]
FLS ENTRY [n] CLOSED
```

**Ceiling-delta FLS annotation (per block):** Does the ceiling role have a different FLS posture for this field? If yes: "Ceiling [role] has [Read/Write]. Delta: CS/SE gap is structural, not incidental."

Section close:
```
Phase 1c FLS complete. Blocks: [N] / CLOSED: [N] / Annotations: [N] / Count: [M]
(Gate row 5: [M] vs STEP-1-CLOSE-TOKEN anchor [M])
```

**1d — Sharing rule inventory:** | Rule Name | Trigger | Access | OWD | Conflicts? |

---

## PHASE 2 — TEAM AND CROSS-ENTITY

**2a — Team membership gap (ceiling-informed):** Does team membership bring CS or SE scope closer to the ceiling? Finding / rule-out with evidence.

**2b — Cross-entity chain:** Two hops from highest-sensitivity entity. INTENTIONAL or EMERGENT.

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

One subsection per role.

**Role: [name]** — Team Write / Role Assignment Write / Assign scope / BU Write. Conclusion: ESCALATION-PATH FOUND / RULED OUT.

**Negative-check evidence:** "Checked [items]; [type] does not apply because [reason]."

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative vs ceiling:** delta stated. **Dataverse Security Expert vs ceiling:** delta stated. **Contrast statement:** Both names explicit.

---

## PHASE 5a — REMEDIATION ENTRIES

Verbatim Discovered In. Three-field template.

---

## PHASE 5b — CHAIN 2 SELF-CHECK CLOSE

**Precondition.** | Gap ID | Register | Phase 5a Echo | Match? |

**TRACE CLOSE TOKEN:** `Rows: [N]. FAIL: [N]. Trace closed.`

---

## SUBMISSION GATE

**ANTI-SPECULATION MANDATE — VERDICT-FAIL before the table.**

| Row | Check | Evidence | Status |
|-----|-------|----------|--------|
| 1 | OWD and scope for all entities | Phase 1a counts | PASS / VERDICT-FAIL |
| 2 | Dataverse system names; ceiling established; DELTA-FROM-CEILING for CS and SE | Phase 1b ceiling row + delta columns | PASS / VERDICT-FAIL |
| 3 | FLS analyzed; CLOSED; chain-reminder count = block count; ceiling-delta annotations present | Phase 1c close counts | PASS / VERDICT-FAIL |
| 4 | Gap types checked; negative-check evidence | Phase 3 + Phase 2 rule-outs | PASS / VERDICT-FAIL |
| 5 | Token-swap: STEP-1-CLOSE-TOKEN [M] vs section-close [M]; PR-1 clean; rows 1–4 PASS | Token, section-close count, rows 1–4 | PASS / VERDICT-FAIL |

---

## V-04 — Combined: C-26 + C-27 (Body Blocks + Verbatim Labels)

**Axis:** Combined lifecycle emphasis + phrasing register — Phase 0 body-level named protocol blocks with PENDING→RESOLVED lifecycle (C-26) + rubric-exact pass-condition phrases at all five enforcement sites (C-27)
**Hypothesis:** V-01 establishes C-26 (body blocks + RESOLVED marker). V-02 establishes C-27 (verbatim labels). Mechanisms operate at non-overlapping structural sites: C-26 modifies Phase 0 body structure and the Step 1 close RESOLVED marker; C-27 modifies enforcement instruction labels at Step 1 close, Phase 1c section close, gate row 5, PR-1, and block format definition. No structural conflict. V-04 combines both on the R8-V-05 base. Hypothesis: 190/190.

---

You are running a permissions trace signal for: {{topic}}

---

## PHASE 0 — FULL AUDIT CHAIN GATE

**Complete this phase and write the ACTIVATION STATE LOG before Phase 1 content.**

This trace operates under a bidirectional audit chain. Both directions pre-established here and active for the full output.

**Chain 1 — Discovery to register (active during Phases 1–4):**
Every gap found during Phases 1–4 entered into LIVE GAPS REGISTER at moment of discovery. Discovered In set at discovery time, not reconstructed.

**Chain 2 — Register to remediation echo (active during Phase 5a):**
Every register entry echoed via verbatim slot-fill. Verified in Phase 5b — **precondition for closing the trace**.

**Per-row FLS trigger — ACTIVE now:**
FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED format active during Phase 1c. CLOSED terminator required. Co-authorship structural. N/A markers make trigger completeness provable.

**Remediation template (pre-declared):**
```
Gap [ID] (Discovered In: [verbatim — Chain 2 slot-fill]):
  Config change:     [exact configuration element — role / field / profile / rule and location]
  Expected state:    [UI view or query after fix]
  Verification step: [executable action — UI location and expected result]
```

**Protocol: STEP-1-CLOSE-TOKEN (C-24 chain anchor — C-26 Phase 0 body pre-declaration)**

This protocol is pre-declared here as a named Phase 0 body block. ACTIVATION STATE LOG entry below tracks execution status; this block is the authoritative obligation record.

Definition: At Phase 1c Step 1 close, emit a named close token recording the exact count of items analyzed (C-24 rubric phrase). Phase 1c section close independently declares the downstream FLS ENTRY Category annotation count as a separately named value. Gate row 5 performs a non-vacuous numerical comparison between the two named values.

Emission format (required at Phase 1c Step 1 close):
```
STEP-1-CLOSE-TOKEN — ACTIVATED
  Category table total rows analyzed: [N]
  FLS-scope rows (PII + Financial + Audit/Compliance): [M]
  Chain anchor value: [M]
  PENDING status: RESOLVED — references Phase 0 STEP-1-CLOSE-TOKEN protocol declaration
```

**C-26 obligation record:**
Status at Phase 0 close: **PENDING**
Activation point: Phase 1c Step 1 close
Broken-obligation note: **Unresolved PENDING at trace close = broken obligation.** A trace reaching Phase 5b with STEP-1-CLOSE-TOKEN still PENDING has a visibly broken chain anchor — detectable without reading gate row 5.

**Protocol: Per-Stage Chain-Reminder (C-25 consumption-point annotation — C-26 Phase 0 body pre-declaration)**

This protocol is pre-declared here as a named Phase 0 body block.

Definition: The annotation `[Category chain: active — inherit from Step 1]` must appear as the first line of every FLS ENTRY block and at the LIVE GAPS REGISTER section header. This converts the PR-1 propagation contract from a single-point declaration to a continuously-visible constraint (C-25 rubric phrase).

**C-26 obligation record:**
Status at Phase 0 close: **ACTIVE** (first activation: LIVE GAPS REGISTER header immediately below)
Subsequent activation points: every FLS ENTRY block open in Phase 1c
Broken-obligation note: **Absence at any FLS ENTRY block open is a broken state — not deferred to the next block.**

**PHASE 0 GATE — ACTIVATION STATE LOG:**

This log is an **execution record, not a declarative checklist**. PENDING entries have a named activation point — reaching that point without the mechanism firing = broken state. Body-level protocol blocks above are authoritative; LOG rows track execution status.

| Mechanism | Status | Notes |
|-----------|--------|-------|
| Chain 1 — discovery → register, Discovered In set at discovery time | ACTIVE | Governs Phases 1–4 |
| Chain 2 — register → Phase 5a verbatim echo | ACTIVE | Phase 5b verification is precondition for trace close |
| Per-row FLS trigger — ENTRY / SLOT / CLOSED | ACTIVE | CLOSED required before next entry |
| Remediation template — Config change / Expected state / Verification step | ACTIVE | All three fields required |
| Mismatch example — Phase 5b self-check instrument | LOADED | Precondition for trace close |
| I-6 category drift / PR-1 — CATEGORY-DRIFT-VIOLATION marker | ACTIVE | Fires on re-derivation during Phase 1c Step 2 onward |
| STEP-1-CLOSE-TOKEN — named chain anchor; **body protocol block declared above** | PENDING | Activation point: Phase 1c Step 1 close. Unresolved PENDING = broken obligation. |
| Per-stage chain-reminder — `[Category chain: active — inherit from Step 1]`; **body protocol block declared above** | ACTIVE | First activation: LIVE GAPS REGISTER header. Fires at every FLS ENTRY block open. |

*All mechanisms ACTIVE or LOADED. STEP-1-CLOSE-TOKEN PENDING — body-level obligation declared above is authoritative. Entering PHASE 1.*

---

## LIVE GAPS REGISTER

**[Category chain: active — inherit from Step 1]** *(Per-stage chain-reminder (C-25) — first activation per Phase 0 body declaration)*

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

---

## PHASE 1 — ENTITY AND ROLE MAP

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Scope | Default access for unauthenticated user |
|--------|-----------------|-------|----------------------------------------|

OWD scope: Organization / Business Unit / Owner. Missing scope = incomplete row.

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Team / User / Sharing-[rule name]. All roles with any privilege. Dataverse system names required. Highest-privilege role first.

**1c — Sensitive field categorization:**

**Inertia threat inventory:**

| ID | Threat | Fires During | Marker |
|----|--------|-------------|--------|
| I-1 | OWD defaults creating unexpected access | Phase 1a | ESCALATION-PATH |
| I-2 | Missing FLS on PII, Financial, Audit/Compliance | Phase 1c | MISSING-FLS |
| I-3 | Sharing rule overrides | Phase 1d | SHARING-CONFLICT |
| I-4 | Team membership privilege injection | Phase 2a | TEAM-GAP |
| I-5 | EMERGENT cross-entity hops | Phase 2b | CROSS-ENTITY |
| I-6 | Category drift — re-derivation downstream of Step 1 | Phase 1c Step 2 onward | CATEGORY-DRIFT-VIOLATION |

**PR-1: Category propagation contract — converts the propagation contract from a single-point declaration to a continuously-visible constraint (C-25 rubric phrase):**
Category in every FLS ENTRY block inherits from Step 1 — not re-derived inline. Re-derivation fires I-6. The per-stage chain-reminder declared in Phase 0 body protocol is the mechanism that makes this contract continuously visible at each consumption site.

Step 1: category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII | |
| | Financial | |
| | Audit/Compliance | |
| | Operational | |

**Step 1 close — emit a named close token recording the exact count of items analyzed (C-24 rubric phrase — chain anchor); resolves PENDING from Phase 0 body protocol declaration (C-26):**

```
STEP-1-CLOSE-TOKEN — ACTIVATED
  Category table total rows analyzed: [N]
  FLS-scope rows (PII + Financial + Audit/Compliance): [M]
  Chain anchor value: [M]
  PENDING status: RESOLVED — references Phase 0 STEP-1-CLOSE-TOKEN protocol declaration
```

Gate row 5 will compare chain anchor [M] against Phase 1c section-close annotation count [M]. Both named. Non-vacuous.

Step 2: FLS check for all PII, Financial, and Audit/Compliance fields.

**Block format — mandatory per sensitive field; consumption-point chain-reminder required at block open (C-25: `[Category chain: active — inherit from Step N]` exact form required — converts contract from single-point declaration to continuously-visible constraint):**

```
[Category chain: active — inherit from Step 1]
FLS ENTRY [n] — [Entity].[Field]
| Entity | Field | Category | FLS Profile? | CS: Read | CS: Write | Expert: Read | Expert: Write | Gap? |
|--------|-------|----------|-------------|----------|-----------|--------------|---------------|------|

REGISTER SLOT [n] (Chain 1 — complete before CLOSED marker):
```

If Gap? = YES: enter register. If Gap? = NO: "→ No gap. Register slot: N/A."

```
FLS ENTRY [n] CLOSED
```

Section close — downstream annotation count declared separately for non-vacuous gate row 5 comparison; C-25 consumption-point annotation count verified:
```
Phase 1c FLS complete.
  FLS ENTRY blocks: [N] / CLOSED markers: [N] (must equal [N])
  YES entries: [N] / N/A register slots: [N]
  Chain-reminder annotations at block opens: [N] (must equal [N] — C-25 per-stage consumption-point verification: converts contract to continuously-visible constraint)
  Downstream FLS ENTRY Category annotation count: [M]
  (Separately declared for non-vacuous numerical comparison vs STEP-1-CLOSE-TOKEN anchor [M] — C-24 rubric phrase)
```

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

---

## PHASE 2 — TEAM AND CROSS-ENTITY

**2a:** Finding / rule-out with specific evidence.
**2b:** Two-hop chain from highest-sensitivity entity. INTENTIONAL or EMERGENT.

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

One subsection per role. No collective statements.

**Role: [name]** — Team Write / Role Assignment Write / Assign scope / BU Write. Conclusion: FOUND / RULED OUT.

**Negative-check evidence:** "Checked [items]; [type] does not apply because [reason]."

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative / Dataverse Security Expert.** Contrast statement with both names explicit.

---

## PHASE 5a — REMEDIATION ENTRIES

Verbatim Discovered In. Three-field template.

```
Gap [ID] (Discovered In: [verbatim]):
  Config change: / Expected state: / Verification step:
```

---

## PHASE 5b — CHAIN 2 SELF-CHECK CLOSE

**Precondition for closing the trace.**

| Gap ID | Register: Discovered In | Phase 5a Echo: Discovered In | Match? |
|--------|------------------------|------------------------------|--------|

**TRACE CLOSE TOKEN:** `Chain 2 self-check applied. Rows: [N]. FAIL corrections: [N]. Trace closed.`

---

## SUBMISSION GATE

**ANTI-SPECULATION MANDATE — VERDICT-FAIL before the table header.**

| Row | Check | Evidence Cited | Status |
|-----|-------|----------------|--------|
| 1 | All entities Phase 1a with OWD and scope | Phase 1a row count and scope values | PASS / VERDICT-FAIL |
| 2 | All roles by Dataverse system name; record scope per entity | Phase 1b role names and Record Scope column | PASS / VERDICT-FAIL |
| 3 | FLS analyzed; all CLOSED; chain-reminder count equals block count (C-25: per-stage consumption-point annotation — converts contract to continuously-visible constraint) | Phase 1c close: N blocks, N CLOSED, N chain-reminder annotations | PASS / VERDICT-FAIL |
| 4 | All gap types checked; negative-check evidence present | Phase 3 statements and Phase 2 rule-outs | PASS / VERDICT-FAIL |
| 5 | **Non-vacuous numerical comparison (C-24 rubric phrase):** (a) STEP-1-CLOSE-TOKEN = named close token recording the exact count of items analyzed [M]; PENDING resolved at Phase 1c Step 1 close referencing Phase 0 body protocol declaration (C-26); (b) Phase 1c section-close annotation count [M] — separately declared; (c) [M] == [M]? YES/NO; (d) PR-1: converts propagation contract from single-point declaration to continuously-visible constraint (C-25 rubric phrase) — no CATEGORY-DRIFT-VIOLATION; (e) rows 1–4 PASS | STEP-1-CLOSE-TOKEN ACTIVATED block with RESOLVED marker, Phase 1c section-close count, rows 1–4 | PASS / VERDICT-FAIL |

---

## V-05 — Combined + Obligation Lifecycle IDs (Maximum Reviewer Independence)

**Axis:** Combined lifecycle + phrasing register + obligation ID tags — V-04 structure with named obligation identifiers (OBL-01 for STEP-1-CLOSE-TOKEN, OBL-02 for per-stage chain-reminder) threading through every enforcement site; each site carries both lifecycle state marker and rubric-verbatim phrase, making it independently self-auditing without Phase 0 cross-reference
**Hypothesis:** V-04 satisfies C-26 and C-27. An auditor reading gate row 5 must still recall Phase 0 to confirm the RESOLVED marker references the correct body declaration. V-05 adds obligation IDs that thread all enforcement sites: Phase 0 assigns OBL-01 to STEP-1-CLOSE-TOKEN and OBL-02 to per-stage chain-reminder. Step 1 close carries `PENDING status: RESOLVED [OBL-01]` + C-24 rubric phrase. Phase 1c section close carries `[OBL-01 downstream consumption point]` + C-25 phrase. Gate row 5 carries `[OBL-01 chain verification]`. PR-1 carries `[OBL-02 source declaration]`. Block format carries `[OBL-02 per-block activation]`. Each site names its obligation ID and rubric criterion — no Phase 0 lookup required. Hypothesis: 190/190 with maximum reviewer independence.

---

You are running a permissions trace signal for: {{topic}}

---

## PHASE 0 — FULL AUDIT CHAIN GATE

**Complete this phase and write the ACTIVATION STATE LOG before Phase 1 content.**

This trace operates under a bidirectional audit chain. Both directions pre-established here and active for the full output.

**Chain 1 — Discovery to register (active during Phases 1–4):** Discovered In set at discovery time, not reconstructed.

**Chain 2 — Register to remediation echo (active during Phase 5a):** Verbatim slot-fill. Phase 5b verification is **precondition for closing the trace**.

**Per-row FLS trigger — ACTIVE:** FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED. CLOSED required before next entry. Co-authorship structural. N/A markers make completeness provable.

**Remediation template:**
```
Gap [ID] (Discovered In: [verbatim — Chain 2 slot-fill]):
  Config change:     [exact element and location]
  Expected state:    [UI view or query after fix]
  Verification step: [executable action]
```

**Protocol OBL-01: STEP-1-CLOSE-TOKEN (C-24 chain anchor — C-26 Phase 0 body pre-declaration)**

Obligation ID: **OBL-01**. This ID threads through every downstream enforcement and consumption site. A reviewer encountering OBL-01 anywhere can locate this block by ID — no full Phase 0 re-read required.

Definition: At Phase 1c Step 1 close, emit a named close token recording the exact count of items analyzed (C-24 rubric phrase). Phase 1c section close independently declares the downstream FLS ENTRY Category annotation count. Gate row 5 performs a non-vacuous numerical comparison between the two named values.

Emission format (required at Phase 1c Step 1 close):
```
STEP-1-CLOSE-TOKEN — ACTIVATED [OBL-01]
  Category table total rows analyzed: [N]
  FLS-scope rows (PII + Financial + Audit/Compliance): [M]
  Chain anchor value: [M]
  PENDING status: RESOLVED — references Phase 0 OBL-01 protocol declaration
```

**C-26 obligation record for OBL-01:**
Status at Phase 0 close: **PENDING**
Activation point: Phase 1c Step 1 close
Broken-obligation note: **Unresolved OBL-01 at trace close = broken obligation.** A trace reaching Phase 5b with STEP-1-CLOSE-TOKEN still PENDING has a visibly broken chain anchor — detectable without reading gate row 5.

**Protocol OBL-02: Per-Stage Chain-Reminder (C-25 consumption-point annotation — C-26 Phase 0 body pre-declaration)**

Obligation ID: **OBL-02**. Threads through every activation and consumption site.

Definition: `[Category chain: active — inherit from Step 1]` must appear as the first line of every FLS ENTRY block and at the LIVE GAPS REGISTER header. Converts PR-1 from a single-point declaration to a continuously-visible constraint (C-25 rubric phrase). Each OBL-02 site carries both the obligation ID and the C-25 rubric phrase — self-auditing without Phase 0 lookup.

**C-26 obligation record for OBL-02:**
Status at Phase 0 close: **ACTIVE** (first activation: LIVE GAPS REGISTER header immediately below — carries `[OBL-02 first activation]`)
Subsequent activation points: every FLS ENTRY block open in Phase 1c
Broken-obligation note: **Absence of OBL-02 at any FLS ENTRY block open is a broken state — not deferred to the next block.**

**PHASE 0 GATE — ACTIVATION STATE LOG:**

This log is an **execution record, not a declarative checklist**. Body-level protocol blocks above are authoritative obligation records. Each LOG row carries its obligation ID.

| Mechanism | Status | Notes |
|-----------|--------|-------|
| Chain 1 — discovery → register | ACTIVE | Governs Phases 1–4 |
| Chain 2 — register → Phase 5a verbatim echo | ACTIVE | Phase 5b precondition |
| Per-row FLS trigger — ENTRY / SLOT / CLOSED | ACTIVE | CLOSED required |
| Remediation template — three fields | ACTIVE | All fields required |
| Mismatch example — Phase 5b self-check | LOADED | Precondition for trace close |
| I-6 category drift / PR-1 — CATEGORY-DRIFT-VIOLATION | ACTIVE | Fires on re-derivation |
| **OBL-01** STEP-1-CLOSE-TOKEN — named chain anchor; body protocol declared above | PENDING | Activation: Phase 1c Step 1 close. Unresolved = broken obligation. |
| **OBL-02** Per-stage chain-reminder; body protocol declared above | ACTIVE | First activation: LIVE GAPS REGISTER header `[OBL-02 first activation]`. |

*All mechanisms ACTIVE or LOADED. OBL-01 PENDING. OBL-02 ACTIVE. Entering PHASE 1.*

---

## LIVE GAPS REGISTER

**[Category chain: active — inherit from Step 1] [OBL-02 first activation] — converts propagation contract from single-point declaration to continuously-visible constraint (C-25)**

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

---

## PHASE 1 — ENTITY AND ROLE MAP

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Scope | Default access for unauthenticated user |
|--------|-----------------|-------|----------------------------------------|

OWD scope: Organization / Business Unit / Owner.

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Dataverse system names required. Highest-privilege role first.

**1c — Sensitive field categorization:**

**Inertia threat inventory:**

| ID | Threat | Fires During | Marker |
|----|--------|-------------|--------|
| I-1 | OWD defaults creating unexpected access | Phase 1a | ESCALATION-PATH |
| I-2 | Missing FLS on PII, Financial, Audit/Compliance | Phase 1c | MISSING-FLS |
| I-3 | Sharing rule overrides | Phase 1d | SHARING-CONFLICT |
| I-4 | Team membership privilege injection | Phase 2a | TEAM-GAP |
| I-5 | EMERGENT cross-entity hops | Phase 2b | CROSS-ENTITY |
| I-6 | Category drift downstream of Step 1 | Phase 1c Step 2 onward | CATEGORY-DRIFT-VIOLATION |

**PR-1 [OBL-02 source declaration]: Category propagation contract — converts the propagation contract from a single-point declaration to a continuously-visible constraint (C-25 rubric phrase):**
Category in every FLS ENTRY block inherits from Step 1 — not re-derived inline. OBL-02 chain-reminder is the enforcement mechanism: fires at each consumption site with `[OBL-02 per-block activation]` + C-25 phrase — making the constraint visible without PR-1 lookup.

Step 1: category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII | |
| | Financial | |
| | Audit/Compliance | |
| | Operational | |

**Step 1 close — emit a named close token recording the exact count of items analyzed (C-24 rubric phrase — chain anchor); resolves OBL-01 PENDING (C-26):**

```
STEP-1-CLOSE-TOKEN — ACTIVATED [OBL-01 chain verification]
  Category table total rows analyzed: [N]
  FLS-scope rows (PII + Financial + Audit/Compliance): [M]
  Chain anchor value: [M]
  PENDING status: RESOLVED — references Phase 0 OBL-01 protocol declaration
```

Gate row 5 will carry `[OBL-01 chain verification]` and the C-24 rubric phrase. Chain anchor [M] vs section-close annotation count [M]. Non-vacuous.

Step 2: FLS check for all PII, Financial, and Audit/Compliance fields.

**Block format — mandatory per sensitive field; OBL-02 consumption-point chain-reminder required at block open (C-25: `[Category chain: active — inherit from Step N]` exact form required — converts contract from single-point declaration to continuously-visible constraint):**

```
[Category chain: active — inherit from Step 1] [OBL-02 per-block activation]
FLS ENTRY [n] — [Entity].[Field]
| Entity | Field | Category | FLS Profile? | CS: Read | CS: Write | Expert: Read | Expert: Write | Gap? |
|--------|-------|----------|-------------|----------|-----------|--------------|---------------|------|

REGISTER SLOT [n] (Chain 1 — complete before CLOSED marker):
```

If Gap? = YES: enter register. If Gap? = NO: "→ No gap. Register slot: N/A."

```
FLS ENTRY [n] CLOSED
```

Section close — downstream annotation count [OBL-01 downstream consumption point] declared separately; OBL-02 per-stage count verified:
```
Phase 1c FLS complete.
  FLS ENTRY blocks: [N] / CLOSED markers: [N]
  YES entries: [N] / N/A register slots: [N]
  OBL-02 chain-reminder annotations at block opens: [N] (must equal [N] — C-25: converts contract to continuously-visible constraint)
  Downstream FLS ENTRY Category annotation count [OBL-01 downstream]: [M]
  (Separately declared for non-vacuous numerical comparison vs STEP-1-CLOSE-TOKEN OBL-01 anchor [M] at gate row 5 — C-24 rubric phrase)
```

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

---

## PHASE 2 — TEAM AND CROSS-ENTITY

**2a:** Finding / rule-out with evidence. **2b:** Two-hop chain. INTENTIONAL or EMERGENT.

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

One subsection per role. No collective statements.

**Role: [name]** — Team Write / Role Assignment Write / Assign scope / BU Write. Conclusion: FOUND / RULED OUT.

**Negative-check evidence:** "Checked [items]; [type] does not apply because [reason]."

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative / Dataverse Security Expert.** Contrast statement with both names.

---

## PHASE 5a — REMEDIATION ENTRIES

Verbatim Discovered In. Three-field template.

```
Gap [ID] (Discovered In: [verbatim]):
  Config change: / Expected state: / Verification step:
```

---

## PHASE 5b — CHAIN 2 SELF-CHECK CLOSE

**Precondition for closing the trace.**

| Gap ID | Register: Discovered In | Phase 5a Echo: Discovered In | Match? |
|--------|------------------------|------------------------------|--------|

**TRACE CLOSE TOKEN:** `Chain 2 self-check applied. Rows: [N]. FAIL corrections: [N]. Trace closed.`

---

## SUBMISSION GATE

**ANTI-SPECULATION MANDATE — VERDICT-FAIL before the table header.**

| Row | Check | Evidence Cited | Status |
|-----|-------|----------------|--------|
| 1 | All entities Phase 1a with OWD and scope | Phase 1a row count and scope values | PASS / VERDICT-FAIL |
| 2 | All roles by Dataverse system name; record scope per entity | Phase 1b role names and Record Scope column | PASS / VERDICT-FAIL |
| 3 | FLS analyzed; all CLOSED; OBL-02 chain-reminder count equals block count (C-25: per-stage consumption-point annotation — converts contract to continuously-visible constraint; `[OBL-02 per-block activation]` at each block open) | Phase 1c close: N blocks, N CLOSED, N OBL-02 annotations | PASS / VERDICT-FAIL |
| 4 | All gap types checked; negative-check evidence present | Phase 3 statements and Phase 2 rule-outs | PASS / VERDICT-FAIL |
| 5 | **Non-vacuous numerical comparison [OBL-01 chain verification] (C-24 rubric phrase):** (a) STEP-1-CLOSE-TOKEN = named close token recording the exact count of items analyzed [M]; OBL-01 PENDING resolved at Phase 1c Step 1 close referencing Phase 0 body protocol declaration (C-26); (b) Phase 1c section-close OBL-01 downstream annotation count [M] — separately declared; (c) [M] == [M]? YES/NO; (d) PR-1 / OBL-02: converts propagation contract from single-point declaration to continuously-visible constraint (C-25 rubric phrase) — no CATEGORY-DRIFT-VIOLATION; (e) rows 1–4 PASS | STEP-1-CLOSE-TOKEN ACTIVATED block with OBL-01 RESOLVED marker, Phase 1c section-close OBL-01 downstream count, rows 1–4 | PASS / VERDICT-FAIL |
