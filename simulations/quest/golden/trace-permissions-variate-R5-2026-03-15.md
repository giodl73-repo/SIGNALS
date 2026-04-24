# trace-permissions Variate — Round 5
**Date:** 2026-03-15
**Rubric:** v5 (C-01 through C-21 — C-19/C-20/C-21 added from R4-V-05 excellence signals)
**Target criteria:** C-19 (FLS table rows and gap register co-authored per row), C-20 (Phase 0 gate pre-establishes full bidirectional chain with per-row trigger active), C-21 (C-17 verification via concrete mismatch example)

**Baseline:** R4-V-05 achieved structural enforcement of C-16 (Phase 0 gate), C-17 (slot-fill echo), and C-18 (per-row boolean trigger). The three new criteria close the remaining sequencing gaps: C-19 converts the per-row trigger from a two-step sequence (fill Gap?, then register) into a single co-production act; C-20 upgrades Phase 0 from "remediation template declared" to "full bidirectional chain pre-established with trigger already active"; C-21 converts the Phase 5 copy instruction from behavioral to self-verifiable by supplying a concrete failure example.

---

## Round 5 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Lifecycle emphasis — C-20 isolation: Phase 0 names both chain directions and marks per-row trigger ACTIVE before Phase 1 | R4-V-05's Phase 0 declared the remediation template and the per-row trigger, but did not explicitly name the two-direction chain as a single pre-established structure. The model could treat C-17 as a Phase 5 task rather than a live constraint during evidence collection. Naming both directions — register Discovered In field → Phase 5 echo — and marking the trigger as ACTIVE in the gate token puts the full audit frame in working context before row 1 of Phase 1 is filled. |
| V-02 | Output format — C-19 isolation: FLS section reformatted as interleaved Entry blocks, each row physically adjacent to its register slot | R4-V-05's per-row trigger was still two sequential steps: mark Gap? YES, then write the register entry. The model could fill multiple rows then "apply" the trigger retrospectively without violating the format. Interleaved blocks — table row immediately followed by a mandatory register slot (N/A if Gap? = NO) — make co-authorship a structural property of the format rather than a behavioral contract. The model cannot output the next row without having completed the register slot for the current one. |
| V-03 | Phrasing register — C-21 isolation: Phase 5 provides a concrete mismatch example that converts the copy instruction into a self-verifiable test | R4-V-05's slot-fill instruction in Phase 5 said "copy verbatim." A model paraphrasing "Phase 1c FLS check — Contact.AnnualRevenue" to "FLS gap — AnnualRevenue" might not self-detect the violation. A concrete failure example — showing both the correct verbatim copy and the plausible paraphrase that fails — gives the model an executable test it can apply to its own output before the trace is closed. |
| V-04 | Lifecycle emphasis + Output format — C-20 + C-19 combo: expanded Phase 0 gate + interleaved FLS blocks | These two mechanisms close the chain at different structural levels: Phase 0 establishes the frame before evidence collection begins; the interleaved block format enforces co-authorship during evidence collection. Together they make it structurally impossible to complete Phase 1 with a deferred register pass. |
| V-05 | Full triple lock — C-20 + C-19 + C-21: all three new criteria addressed structurally, combined with the full R4 mechanism stack | The complete inline-registration stack (C-11/C-18/C-19) and the full bidirectional audit chain (C-14/C-17 → C-20/C-21) both enforced in a single prompt. Every prior aspirational criterion remains addressed. This is the production candidate for R5. |

---

## V-01 — Lifecycle Emphasis: Phase 0 Full Bidirectional Gate (C-20 Isolation)

**Axis:** Lifecycle emphasis — Phase 0 explicitly names both chain directions and marks the per-row trigger as ACTIVE before Phase 1 begins
**Hypothesis:** R4-V-05 declared the remediation template and the per-row trigger in Phase 0, but named them as independent structures. The bidirectional chain — register Discovered In field → Phase 5 echo — was implicit: the Discovered In column existed and the slot-fill instruction existed, but they were never described as two ends of the same chain. Naming both directions explicitly in Phase 0 and marking the trigger as ACTIVE from that point ensures the model enters the evidence window with the full audit frame already in working context, not assembled piecemeal as each phase is reached.

---

You are running a permissions trace signal for: {{topic}}

---

## PHASE 0 — BIDIRECTIONAL AUDIT CHAIN GATE

**Complete this phase and write the gate token before advancing to Phase 1.**

This trace uses a bidirectional audit chain. Both directions are pre-established here, before any entity has been inventoried or any gap has been found.

**Chain direction 1 — Discovery to register:**
Every gap found during Phases 1–4 is entered into the LIVE GAPS REGISTER at the point of discovery with a Discovered In field recording the exact section. The Discovered In value is set at discovery time, not reconstructed later.

**Chain direction 2 — Register to remediation:**
Every LIVE GAPS REGISTER entry is echoed in Phase 5 via a slot-fill operation: the Discovered In value is copied verbatim from the register row into the corresponding remediation entry. The remediation entry does not summarize, shorten, or paraphrase the Discovered In value.

**Per-row trigger — ACTIVE from this point:**
During Phase 1c FLS table fill, the per-row trigger is ACTIVE. This means: after filling the Gap? cell for each FLS table row, if Gap? = YES, a register entry is written immediately before the next row begins. The trigger fires row by row during table fill — not as a post-table review pass.

**Remediation template (pre-declared, applied in Phase 5 to every register entry):**

```
Gap [ID] (Discovered In: [copy verbatim from register]):
  Config change:     [the exact configuration element to modify — name the role, field, profile,
                      or rule and its location in the security editor]
  Expected state:    [what the system shows after the fix — name the UI view, profile row, or
                      query result that will differ]
  Verification step: [the named action a reviewer executes — e.g., "Open Security > Field Security
                      Profiles > [profile] > [entity] > [field]: verify [role] shows Read-only"]
```

Rules: Config change names a specific element, not a category. Expected state names a UI location. Verification step is executable by a reviewer unfamiliar with the gap history.

> **PHASE 0 GATE** — Write this line before Phase 1 content:
> *"Phase 0 complete. Bidirectional chain pre-established: Chain 1 active (discovery → register with Discovered In). Chain 2 active (register → Phase 5 echo verbatim). Per-row FLS trigger ACTIVE. Remediation template declared: Config change / Expected state / Verification step. Advancing to Phase 1."*

---

## LIVE GAPS REGISTER

Updated at point of discovery. A row is invalid without a Discovered In entry.

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

- **Discovered In**: exact section name and context — e.g., "Phase 1c FLS check — Contact.AnnualRevenue" or "Phase 3 escalation — Customer Service role"
- Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY
- Severity: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 — ENTITY AND ROLE MAP

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Default access for unauthenticated user |
|--------|-----------------|----------------------------------------|

Register check after 1a: Does any OWD create unexpected default access? If yes: add to register (Discovered In: "Phase 1a OWD — [entity]"). If no: "Phase 1a check: no OWD anomalies — [basis]."

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Team / User / Sharing-[rule name]. Every role with any privilege must appear.

Register check after 1b: Any role with Record Scope broader than its function? If yes: add to register (Discovered In: "Phase 1b operation-role matrix — [role]"). If no: "Phase 1b check: no scope anomalies — [basis]."

**1c — Sensitive field categorization:**

Step 1: enumerate fields by category:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII (name, contact info, ID, government data) | |
| | Financial (billing, pricing, payment, credit) | |
| | Audit/Compliance (modified-by, consent, audit trail) | |
| | Operational (status, queue, SLA, internal notes) | |

Write "none" for empty categories.

Step 2: FLS check — per-row trigger ACTIVE:

| Entity | Field | Category | FLS Profile? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|-------------|-------------|--------------|------|

Per-row trigger rule (Chain 1 in effect):
> After filling each row's Gap? cell — if Gap? = YES: write the register entry NOW before the next row. Discovered In = "Phase 1c FLS check — [entity].[field]". Then resume.
> If Gap? = NO: continue to next row.

Section close: "Phase 1c FLS complete. [N] YES entries. [N] register entries written."

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

Register check after 1d: For each Conflicts = YES: add to register (Discovered In: "Phase 1d sharing rule — [rule name]"). If none: "Phase 1d check: no SHARING-CONFLICT entries — [rules checked, reason]."

---

## PHASE 2 — TEAM AND CROSS-ENTITY

**2a — Team membership gap:**

For each team-scoped role, identify who controls membership and whether that control permits elevation.

Finding: `[Role] → [adds user to Team X] → [elevated access via team] — mechanism: [how]`
Rule-out: "Checked team membership control for [team list]: no injection path — [reason]."

Register check after 2a: Add any TEAM-GAP (Discovered In: "Phase 2a team membership — [team]").

**2b — Cross-entity permission chain:**

Select the entity with highest data sensitivity (use Phase 1c categories to justify the selection).

Trace at least two entity hops:

`[Role] → [Entity A, op: X, scope: Y] → [Relationship: lookup/child/N:N] → [Entity B, op: X, scope: Y]`

At each hop: mark access as INTENTIONAL (expected by design) or EMERGENT (side effect of relationship). EMERGENT = gap.

Register check after 2b: Add any CROSS-ENTITY findings (Discovered In: "Phase 2b cross-entity — [role] via [Entity A] → [Entity B]").

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

One subsection per role from Phase 1b. Do not merge roles into a collective statement.

For each role:

**Role: [name]**

Escalation-capable privileges examined:
- Team membership Write: [YES / NO — evidence]
- Security role assignment Write: [YES / NO — evidence]
- Record ownership Assign scope: [scope — whether reassignment permits elevation]
- Business unit configuration Write: [YES / NO — evidence]

Conclusion: ESCALATION-PATH FOUND / RULED OUT

If FOUND: `[Role] → [action] → [elevated access achieved]`
If RULED OUT: "No path — [specific reason each checked privilege does not permit elevation]."

Register check after each role: If ESCALATION-PATH FOUND: add to register (Discovered In: "Phase 3 escalation — [role name]"). Ruled out = absence in register confirms negative.

Negative-check evidence per gap type: For any gap type that yields no finding across all roles, write:
"Checked [specific items] for [role list]; [gap type] does not apply because [specific reason]."

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative:**
CRUD + Assign + Record Scope per entity. Which Phase 1c sensitive fields can Customer Service read or write? Is each access appropriate to the CS job function or overreach?

**Dataverse Security Expert:**
CRUD + Assign + Record Scope per entity. Every privilege the expert holds that Customer Service does not. Does the expert role follow least-privilege or hold admin-level access beyond configuration scope?

**Contrast statement (required):**
One paragraph explicitly contrasting the two roles. Both role names must appear. State: what Customer Service can do that the expert cannot, and what the expert can do that Customer Service cannot.

---

## PHASE 5 — REMEDIATION

Chain 2 active: for every entry in the LIVE GAPS REGISTER, copy the Discovered In value verbatim into the remediation entry using the template declared in Phase 0.

**Copy instruction:** The Discovered In value in each remediation entry must be an exact copy of the corresponding Discovered In cell in the register. Copying is a slot-fill operation, not a paraphrase.

For each register entry:

```
Gap [ID] (Discovered In: [verbatim copy from register — exact text, no compression]):
  Config change:     [exact element — role / field / profile / rule name and location]
  Expected state:    [what the system shows after the fix — name the UI view or test query]
  Verification step: [executable action — name UI location and expected result]
```

---

## V-02 — Output Format: Interleaved FLS Entry Blocks (C-19 Isolation)

**Axis:** Output format — the FLS section is reformatted from a table with a post-row trigger to an interleaved block structure: each FLS entry is a two-part block (Table Row / Register Slot), where the Register Slot is mandatory regardless of Gap? value
**Hypothesis:** R4-V-02/V-05 used a per-row trigger: fill the Gap? cell, then apply the trigger. This was still two sequential steps — the model could technically complete the table first and apply triggers retrospectively, satisfying the format without true co-authorship. Interleaved blocks make the register slot structurally adjacent to and required by each table row. The model cannot output FLS Entry N+1 without a completed register slot for Entry N. Gap? = NO produces an explicit "no gap" marker, not silence — confirming that the co-authorship step ran for every row, not just the ones with gaps.

---

You are running a permissions trace signal for: {{topic}}

---

## REMEDIATION CONTRACT

Declared before analysis begins. Applied in Phase 5 to every gap in the register.

```
Gap [ID] (Discovered In: [section — copy verbatim from register]):
  Config change:     [exact element to modify and where in the solution]
  Expected state:    [what the system shows after the change — name the UI view or query]
  Verification step: [the action to confirm the fix — name the UI location and expected result]
```

Rules: Config change names a specific element, not a category. Expected state names a UI location. Verification step is executable by a reviewer unfamiliar with the gap history.

---

## LIVE GAPS REGISTER

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

- **Discovered In**: exact section name — copied verbatim into Phase 5 remediation entries
- Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY
- Severity: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 — ENTITY AND ROLE MAP

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Default access for unauthenticated user |
|--------|-----------------|----------------------------------------|

Register check after 1a: OWD anomaly? If yes: add (Discovered In: "Phase 1a OWD — [entity]"). If no: "Phase 1a: no OWD anomalies — [basis]."

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Team / User / Sharing-[rule name]. All roles with any privilege.

Register check after 1b: Scope broader than function? If yes: add (Discovered In: "Phase 1b operation-role matrix — [role]"). If no: "Phase 1b: no scope anomalies — [basis]."

**1c — Sensitive field categorization:**

Step 1: category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII (name, contact info, ID, government data) | |
| | Financial (billing, pricing, payment, credit) | |
| | Audit/Compliance (modified-by, consent, audit trail) | |
| | Operational (status, queue, SLA, internal notes) | |

"none" for empty categories.

Step 2: FLS check using INTERLEAVED ENTRY BLOCKS.

**Format for each FLS entry — mandatory structure:**

```
FLS ENTRY — [Entity].[Field]
| Entity | Field | Category | FLS Profile? | CS: Read | CS: Write | Expert: Read | Expert: Write | Gap? |
|--------|-------|----------|-------------|----------|-----------|--------------|---------------|------|
| ...    | ...   | ...      | ...         | ...      | ...       | ...          | ...           | YES/NO |

REGISTER SLOT (required — complete before next FLS ENTRY):
```

If Gap? = YES:
```
| [G-NN] | Phase 1c FLS check — [Entity].[Field] | MISSING-FLS | [Entity] | [Field] | [Role missing access] | [Severity] |
→ Added to LIVE GAPS REGISTER.
```

If Gap? = NO:
```
→ No gap. Register slot: N/A.
```

**Co-authorship rule:** A new FLS ENTRY block may not begin until the REGISTER SLOT for the preceding entry is complete. Gap? = YES without a completed REGISTER SLOT above it is a format violation.

Section close: "Phase 1c FLS complete. [N] FLS ENTRY blocks. [N] YES entries. [N] register entries written. All REGISTER SLOTS complete."

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

Register check after 1d: For each Conflicts = YES: add (Discovered In: "Phase 1d sharing rule — [rule name]"). If none: "Phase 1d: no SHARING-CONFLICT entries — [rules checked, reason]."

---

## PHASE 2 — TEAM AND CROSS-ENTITY

**2a — Team membership gap:**

For each team-scoped role: who controls membership, and can that control reach elevated access?

Finding: `[Role] → [adds user to Team X] → [elevated access] — mechanism: [how]`
Rule-out: "Checked team membership control for [team list]: no injection path — [reason]."

Register check after 2a: Add any TEAM-GAP (Discovered In: "Phase 2a team membership — [team]").

**2b — Cross-entity permission chain:**

Select the highest-sensitivity entity (justify using Phase 1c categories). Trace at least two hops:

`[Role] → [Entity A, op: X, scope: Y] → [Relationship] → [Entity B, op: X, scope: Y]`

Mark each hop: INTENTIONAL or EMERGENT. EMERGENT = gap.

Register check after 2b: Add any CROSS-ENTITY findings (Discovered In: "Phase 2b cross-entity — [role] via [A] → [B]").

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

One subsection per role from Phase 1b. No collective statements.

For each role:

**Role: [name]**

Escalation-capable privileges:
- Team membership Write: [YES / NO — evidence]
- Security role assignment Write: [YES / NO — evidence]
- Record ownership Assign scope: [scope — elevation possible?]
- Business unit configuration Write: [YES / NO — evidence]

Conclusion: ESCALATION-PATH FOUND / RULED OUT

If FOUND: `[Role] → [action] → [elevated access]`
If RULED OUT: "No path — [specific reason per checked privilege]."

Register check per role: FOUND → add (Discovered In: "Phase 3 escalation — [role]").

Negative-check evidence: For any gap type with no finding: "Checked [items] for [role list]; [gap type] does not apply because [reason]."

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative:** CRUD + Assign + Record Scope per entity. Sensitive field access from Phase 1c: appropriate or overreach?

**Dataverse Security Expert:** CRUD + Assign + Record Scope per entity. Every privilege CS lacks. Least-privilege or admin-level overreach?

**Contrast statement (required):** One paragraph, both role names. What CS can do that the expert cannot; what the expert can do that CS cannot.

---

## PHASE 5 — REMEDIATION

For every register entry, apply the Remediation Contract. Copy the Discovered In value verbatim.

```
Gap [ID] (Discovered In: [verbatim copy]):
  Config change:     [exact element — name and location]
  Expected state:    [UI view or query after fix]
  Verification step: [executable action — UI location and expected result]
```

---

## V-03 — Phrasing Register: Mismatch Example in Phase 5 (C-21 Isolation)

**Axis:** Phrasing register — Phase 5 provides a concrete failure example that converts the copy instruction from behavioral to self-verifiable
**Hypothesis:** R4-V-03/V-05 told the model to "copy the Discovered In value verbatim." A model producing "FLS gap — AnnualRevenue" when the register said "Phase 1c FLS check — Contact.AnnualRevenue" might not flag itself as failing — the summary looks reasonable. A concrete mismatch example shows exactly what a passing copy looks like versus what a plausible-but-failing paraphrase looks like. The model can now check its own output against the example before closing the trace. Self-verification converts C-17 from a format check the evaluator applies externally into an operation the model runs internally.

---

You are running a permissions trace signal for: {{topic}}

---

## REMEDIATION CONTRACT

Declared before analysis begins. Applied in Phase 5.

```
Gap [ID] (Discovered In: [section — copy verbatim from register]):
  Config change:     [exact element to modify and where in the solution]
  Expected state:    [what the system shows after the change — name the UI view or query]
  Verification step: [the action to confirm the fix — name the UI location and expected result]
```

Rules: Config change names a specific element. Expected state names a UI location. Verification step is executable.

---

## LIVE GAPS REGISTER

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

- **Discovered In**: exact section name — e.g., "Phase 1c FLS check — Contact.AnnualRevenue"
- Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY
- Severity: CRITICAL / HIGH / MEDIUM

Register rule: Write the register entry immediately when a gap appears. A section may not end with an unregistered gap. If no gaps in a section, write the negative confirmation before the next heading.

---

## PHASE 1 — ENTITY AND ROLE MAP

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Default access for unauthenticated user |
|--------|-----------------|----------------------------------------|

Register check after 1a: OWD anomaly? If yes: add (Discovered In: "Phase 1a OWD — [entity]"). If no: "Phase 1a: no OWD anomalies — [basis]."

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Team / User / Sharing-[rule name]. All roles with any privilege.

Register check after 1b: Scope broader than function? If yes: add (Discovered In: "Phase 1b operation-role matrix — [role]"). If no: "Phase 1b: no scope anomalies — [basis]."

**1c — Sensitive field categorization:**

Step 1: category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII (name, contact info, ID, government data) | |
| | Financial (billing, pricing, payment, credit) | |
| | Audit/Compliance (modified-by, consent, audit trail) | |
| | Operational (status, queue, SLA, internal notes) | |

"none" for empty categories.

Step 2: FLS check — per-row trigger:

| Entity | Field | Category | FLS Profile? | Roles: Read | Roles: Write | Gap? |
|--------|-------|----------|-------------|-------------|--------------|------|

Per-row trigger: after filling each row's Gap? cell — if YES: write the register entry NOW before the next row. Discovered In = "Phase 1c FLS check — [entity].[field]". Then resume.

Section close: "Phase 1c FLS complete. [N] YES entries. [N] register entries written."

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

Register check after 1d: For each Conflicts = YES: add (Discovered In: "Phase 1d sharing rule — [rule name]"). If none: "Phase 1d: no SHARING-CONFLICT entries — [rules checked, reason]."

---

## PHASE 2 — TEAM AND CROSS-ENTITY

**2a — Team membership gap:**

For each team-scoped role: who controls membership, and can that control reach elevated access?

Finding: `[Role] → [adds user to Team X] → [elevated access] — mechanism: [how]`
Rule-out: "Checked team membership control for [team list]: no injection path — [reason]."

Register check after 2a: Add any TEAM-GAP (Discovered In: "Phase 2a team membership — [team]").

**2b — Cross-entity permission chain:**

Select the highest-sensitivity entity (justify using Phase 1c categories). Trace at least two hops:

`[Role] → [Entity A, op: X, scope: Y] → [Relationship] → [Entity B, op: X, scope: Y]`

Mark each hop: INTENTIONAL or EMERGENT. EMERGENT = gap.

Register check after 2b: Add any CROSS-ENTITY findings (Discovered In: "Phase 2b cross-entity — [role] via [A] → [B]").

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

One subsection per role from Phase 1b. No collective statements.

For each role:

**Role: [name]**

Escalation-capable privileges:
- Team membership Write: [YES / NO — evidence]
- Security role assignment Write: [YES / NO — evidence]
- Record ownership Assign scope: [scope — elevation possible?]
- Business unit configuration Write: [YES / NO — evidence]

Conclusion: ESCALATION-PATH FOUND / RULED OUT

If FOUND: `[Role] → [action] → [elevated access]`
If RULED OUT: "No path — [specific reason per checked privilege]."

Register check per role: FOUND → add (Discovered In: "Phase 3 escalation — [role]").

Negative-check evidence: For any gap type with no finding: "Checked [items] for [role list]; [gap type] does not apply because [reason]."

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative:** CRUD + Assign + Record Scope per entity. Sensitive field access from Phase 1c: appropriate or overreach?

**Dataverse Security Expert:** CRUD + Assign + Record Scope per entity. Every privilege CS lacks. Least-privilege or admin-level overreach?

**Contrast statement (required):** One paragraph, both role names. What CS can do that the expert cannot; what the expert can do that CS cannot.

---

## PHASE 5 — REMEDIATION

For every entry in the LIVE GAPS REGISTER, apply the Remediation Contract.

**Copy instruction for Discovered In:**
The Discovered In value in this section must be an exact verbatim copy of the Discovered In cell in the register — not a summary, not a compression, not a paraphrase.

**Mismatch example (use this to self-check your output before closing):**

> Suppose the LIVE GAPS REGISTER contains:
> `| G-02 | Phase 1c FLS check — Contact.AnnualRevenue | MISSING-FLS | ... |`
>
> PASSING — Discovered In echoed verbatim:
> `Gap G-02 (Discovered In: Phase 1c FLS check — Contact.AnnualRevenue):`
>
> FAILING — plausible-but-wrong paraphrase:
> `Gap G-02 (Discovered In: FLS gap — AnnualRevenue):` ← missing entity name, missing phase context
> `Gap G-02 (Discovered In: Phase 1c FLS):` ← truncated, field name dropped
> `Gap G-02 (Discovered In: Contact field security gap):` ← entirely rephrased
>
> Before closing Phase 5: read each Discovered In echo and compare it to the register cell. If it looks like any of the FAILING forms, rewrite it.

For each register entry:

```
Gap [ID] (Discovered In: [verbatim — cross-checked against register]):
  Config change:     [exact element — name and location]
  Expected state:    [UI view or query after fix]
  Verification step: [executable action — UI location and expected result]
```

---

## V-04 — Lifecycle + Format: C-20 + C-19 Combo

**Axis:** Lifecycle emphasis + Output format — expanded Phase 0 gate (C-20) + interleaved FLS entry blocks (C-19)
**Hypothesis:** C-20 establishes the full audit chain before evidence collection begins; C-19 enforces co-authorship during evidence collection. These are temporally complementary: Phase 0 primes the frame; the interleaved blocks prevent any row from escaping the frame during fill. Neither mechanism alone closes both failure modes. Phase 0 without interleaved blocks allows the model to enter Phase 1 with the right context but still defer register entries to a post-table pass. Interleaved blocks without Phase 0 enforce the structure during Phase 1 but the bidirectional chain may not be in working context when Phase 5 is reached. Together: the chain is established before row 1 and enforced at every row.

---

You are running a permissions trace signal for: {{topic}}

---

## PHASE 0 — BIDIRECTIONAL AUDIT CHAIN GATE

**Complete this phase and write the gate token before Phase 1 content.**

**Bidirectional chain (both directions pre-established now):**

Chain 1 — Discovery → Register: Every gap found in Phases 1–4 is entered into the LIVE GAPS REGISTER at the point of discovery. The Discovered In field records the exact section — e.g., "Phase 1c FLS check — [entity].[field]". This value is set at discovery time.

Chain 2 — Register → Remediation echo: Every LIVE GAPS REGISTER entry is echoed verbatim in Phase 5. The Discovered In value is slot-filled from the register cell — not paraphrased, not compressed, not reconstructed.

**Per-row FLS trigger — ACTIVE:** During Phase 1c FLS table fill, the interleaved block format is active. Each FLS entry consists of a table row followed immediately by a register slot. The register slot must be completed before the next FLS entry begins.

**Remediation template (applied in Phase 5 to every register entry):**

```
Gap [ID] (Discovered In: [verbatim from register]):
  Config change:     [exact element — role/field/profile/rule and its location]
  Expected state:    [what the system shows after the fix — specific UI view or query]
  Verification step: [named executable action — UI location and expected result]
```

> **PHASE 0 GATE** — Write this line before Phase 1:
> *"Phase 0 complete. Chain 1 active: discovery → register with Discovered In. Chain 2 active: register → Phase 5 verbatim echo. Per-row FLS trigger ACTIVE: interleaved block format engaged for Phase 1c. Remediation template declared. Advancing to Phase 1."*

---

## LIVE GAPS REGISTER

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

- **Discovered In**: exact section name — e.g., "Phase 1c FLS check — Account.CreditLimit"
- Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY
- Severity: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 — ENTITY AND ROLE MAP

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Default access for unauthenticated user |
|--------|-----------------|----------------------------------------|

Register check after 1a: OWD anomaly? If yes: add (Discovered In: "Phase 1a OWD — [entity]"). If no: "Phase 1a: no OWD anomalies — [basis]."

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Team / User / Sharing-[rule name]. All roles with any privilege.

Register check after 1b: Scope broader than function? If yes: add (Discovered In: "Phase 1b operation-role matrix — [role]"). If no: "Phase 1b: no scope anomalies — [basis]."

**1c — Sensitive field categorization:**

Step 1: category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII (name, contact info, ID, government data) | |
| | Financial (billing, pricing, payment, credit) | |
| | Audit/Compliance (modified-by, consent, audit trail) | |
| | Operational (status, queue, SLA, internal notes) | |

"none" for empty categories.

Step 2: FLS check using INTERLEAVED ENTRY BLOCKS (per-row trigger ACTIVE from Phase 0).

**Entry block structure — apply for every field:**

```
FLS ENTRY — [Entity].[Field]
| Entity | Field | Category | FLS Profile? | CS Read | CS Write | Expert Read | Expert Write | Gap? |
| [val]  | [val] | [val]    | [val]        | [val]   | [val]    | [val]       | [val]        | YES/NO |

REGISTER SLOT:
```

Gap? = YES → write register entry immediately, before next FLS ENTRY:
```
| [G-NN] | Phase 1c FLS check — [Entity].[Field] | MISSING-FLS | [Entity] | [Field] | [Role] | [Severity] |
→ Added to LIVE GAPS REGISTER.
```

Gap? = NO → write:
```
→ No gap. Register slot: N/A — [brief confirmation: e.g., "FLS profile restricts CS to Read-only; appropriate for Financial field"].
```

**Format rule:** A new FLS ENTRY block may not begin until the REGISTER SLOT for the current entry is complete. This is the Chain 1 enforcement point.

Section close: "Phase 1c FLS complete. [N] FLS ENTRY blocks. [N] YES entries. [N] register entries written. All REGISTER SLOTS complete."

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

Register check after 1d: For each Conflicts = YES: add (Discovered In: "Phase 1d sharing rule — [rule name]"). If none: "Phase 1d: no SHARING-CONFLICT entries — [rules checked, reason]."

---

## PHASE 2 — TEAM AND CROSS-ENTITY

**2a — Team membership gap:**

For each team-scoped role: who controls membership, and can that control reach elevated access?

Finding: `[Role] → [adds user to Team X] → [elevated access] — mechanism: [how]`
Rule-out: "Checked team membership control for [team list]: no injection path — [reason]."

Register check after 2a: Add any TEAM-GAP (Discovered In: "Phase 2a team membership — [team]").

**2b — Cross-entity permission chain:**

Select the highest-sensitivity entity (justify using Phase 1c categories). Trace at least two hops:

`[Role] → [Entity A, op: X, scope: Y] → [Relationship] → [Entity B, op: X, scope: Y]`

Mark each hop: INTENTIONAL or EMERGENT. EMERGENT = gap.

Register check after 2b: Add any CROSS-ENTITY findings (Discovered In: "Phase 2b cross-entity — [role] via [A] → [B]").

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

One subsection per role from Phase 1b. No collective statements.

For each role:

**Role: [name]**

Escalation-capable privileges:
- Team membership Write: [YES / NO — evidence]
- Security role assignment Write: [YES / NO — evidence]
- Record ownership Assign scope: [scope — elevation possible?]
- Business unit configuration Write: [YES / NO — evidence]

Conclusion: ESCALATION-PATH FOUND / RULED OUT

If FOUND: `[Role] → [action] → [elevated access]`
If RULED OUT: "No path — [specific reason per checked privilege]."

Register check per role: FOUND → add (Discovered In: "Phase 3 escalation — [role]").

Negative-check evidence: For any gap type with no finding: "Checked [items] for [role list]; [gap type] does not apply because [reason]."

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative:** CRUD + Assign + Record Scope per entity. Sensitive field access from Phase 1c: appropriate or overreach?

**Dataverse Security Expert:** CRUD + Assign + Record Scope per entity. Every privilege CS lacks. Least-privilege or admin-level overreach?

**Contrast statement (required):** One paragraph, both role names explicitly. What CS can do that the expert cannot; what the expert can do that CS cannot.

---

## PHASE 5 — REMEDIATION

Chain 2 active: for every register entry, copy Discovered In verbatim into the remediation entry.

For each register entry:

```
Gap [ID] (Discovered In: [verbatim from register cell]):
  Config change:     [exact element — name and location]
  Expected state:    [UI view or query after fix]
  Verification step: [executable action — UI location and expected result]
```

---

## V-05 — Full Triple Lock: C-20 + C-19 + C-21 (Production Candidate)

**Axis:** Lifecycle emphasis + Output format + Phrasing register — all three new criteria addressed structurally, combined with the full R4 mechanism stack
**Hypothesis:** The three new criteria close three distinct failure modes at three distinct structural points: C-20 ensures the full audit frame is in working context before evidence collection begins (Phase 0); C-19 ensures co-authorship fires at every FLS row during evidence collection (Phase 1c); C-21 ensures the model can self-verify its own Phase 5 echo before the trace closes (Phase 5). Each layer closes a gap the prior layer leaves open: Phase 0 alone cannot prevent deferred register entries during Phase 1; interleaved blocks alone cannot guarantee Phase 5 echoes are verbatim if the chain was never explicitly framed; the mismatch example alone cannot prevent mid-trace registration gaps. The three together form a complete structural guarantee from pre-trace to post-trace.

---

You are running a permissions trace signal for: {{topic}}

---

## PHASE 0 — FULL AUDIT CHAIN GATE

**Complete this phase and write the gate token. Phase 1 content may not appear above this gate token.**

This trace operates under a bidirectional audit chain. Both directions are pre-established here. Both are active for the remainder of the output.

**Chain 1 — Discovery to register (active during Phases 1–4):**
Every gap found during Phases 1–4 is entered into the LIVE GAPS REGISTER at the moment of discovery. The Discovered In field records the exact section and context — e.g., "Phase 1c FLS check — Contact.AnnualRevenue" or "Phase 3 escalation — Customer Service role". This value is set at discovery time, not reconstructed from memory.

**Chain 2 — Register to remediation echo (active during Phase 5):**
Every LIVE GAPS REGISTER entry is echoed in Phase 5 using a verbatim slot-fill. The Discovered In value in Phase 5 is copied exactly from the register cell — same section name, same entity, same field. No summarizing, no shortening, no paraphrasing. Chain 2 is a copy operation, not a writing operation.

**Per-row FLS trigger — ACTIVE now:**
During Phase 1c FLS table fill, the interleaved block format is active. Each FLS entry is a two-part block: a table row and a register slot. The register slot must be completed before the next table row begins. This enforces Chain 1 at the per-row level during the FLS section — the highest-volume gap-generation phase of the trace.

**Remediation template (pre-declared; applied in Phase 5 to every register entry):**

```
Gap [ID] (Discovered In: [verbatim from register — Chain 2 slot-fill]):
  Config change:     [the exact configuration element to modify — name the role, field, profile,
                      or rule and its location in the security editor]
  Expected state:    [what the system shows after the fix — name the specific UI view, profile
                      row, or query result that will differ from the current state]
  Verification step: [the named action a reviewer executes — e.g., "Open Security > Field
                      Security Profiles > [profile name] > [entity] > [field]: verify [role]
                      shows Read-only"]
```

Template rules:
- Config change must name a specific element, not a category of action.
- Expected state must name the UI location where the change will be visible.
- Verification step must be executable by a reviewer unfamiliar with the gap history. "Consult your admin" and "review the configuration" fail this requirement.
- A remediation entry missing Expected state or Verification step fails C-13 regardless of how specific Config change is.

> **PHASE 0 GATE** — Write this exact line before Phase 1 content:
> *"Phase 0 complete. Chain 1 active: discovery → register with Discovered In field set at point of discovery. Chain 2 active: register → Phase 5 verbatim slot-fill, copy-not-write. Per-row FLS trigger ACTIVE: interleaved block format engaged for Phase 1c. Remediation template declared: Config change / Expected state / Verification step. Mismatch example loaded for Phase 5 self-check. Advancing to Phase 1."*

---

## LIVE GAPS REGISTER

Opened at Phase 0. Populated inline during Phases 1–4. Chain 1 enforcement point.

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

- **Discovered In**: exact section name and context, set at discovery time — this is the value Chain 2 will copy verbatim into Phase 5
- Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY
- Severity: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 — ENTITY AND ROLE MAP

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Default access for unauthenticated user |
|--------|-----------------|----------------------------------------|

Chain 1 check after 1a: Does any OWD create unexpected default access? If yes: add to register (Discovered In: "Phase 1a OWD — [entity]"). If no: "Phase 1a: no OWD anomalies — [basis for no-gap determination]."

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Team / User / Sharing-[rule name]. All roles with any privilege on any entity must appear. No roles omitted.

Chain 1 check after 1b: Any role with Record Scope broader than its operational function? If yes: add to register (Discovered In: "Phase 1b operation-role matrix — [role]"). If no: "Phase 1b: no scope anomalies — [basis]."

**1c — Sensitive field categorization:**

Step 1: categorize all fields for each entity before checking FLS:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII (name, contact info, ID, government data) | |
| | Financial (billing, pricing, payment, credit) | |
| | Audit/Compliance (modified-by, consent, audit trail) | |
| | Operational (status, queue, SLA, internal notes) | |

Write "none" for empty categories. Do not leave rows blank.

Step 2: FLS check for all PII, Financial, and Audit/Compliance fields. Per-row trigger ACTIVE — use INTERLEAVED ENTRY BLOCKS.

**Entry block format (mandatory for every field):**

```
FLS ENTRY — [Entity].[Field]
| Entity | Field | Category | FLS Profile? | CS: Read | CS: Write | Expert: Read | Expert: Write | Gap? |
|--------|-------|----------|-------------|----------|-----------|--------------|---------------|------|
| ...    | ...   | ...      | ...         | ...      | ...       | ...          | ...           | YES/NO |

REGISTER SLOT (Chain 1 — complete before next FLS ENTRY):
```

If Gap? = YES:
```
| [G-NN] | Phase 1c FLS check — [Entity].[Field] | MISSING-FLS | [Entity] | [Field] | [Role lacking access] | CRITICAL/HIGH/MEDIUM |
→ Added to LIVE GAPS REGISTER.
```

If Gap? = NO:
```
→ No gap. Register slot: N/A — [brief confirmation: e.g., "FLS profile restricts CS to Read-only on Financial field; no gap"].
```

**Block rule:** A new FLS ENTRY block may not begin until the REGISTER SLOT for the current entry is complete. This rule is enforced by the format, not by judgment. A YES in the Gap? column without a completed REGISTER SLOT above it is a format violation that fails C-19 regardless of what appears in the section close or Phase 5.

Section close: "Phase 1c FLS complete. [N] FLS ENTRY blocks produced. [N] YES entries in Gap? column. [N] register entries written. [N] N/A register slots written. All REGISTER SLOTS complete. Chain 1 per-row trigger: fully applied."

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

Chain 1 check after 1d: For each Conflicts = YES: add to register (Discovered In: "Phase 1d sharing rule — [rule name]"). If none: "Phase 1d: no SHARING-CONFLICT entries — [rules checked, specific reason no conflict]."

---

## PHASE 2 — TEAM AND CROSS-ENTITY

**2a — Team membership gap:**

For each team-scoped role: who controls team membership, and can that control reach elevated access?

Finding: `[Role] → [adds user to Team X] → [elevated access via team] — mechanism: [how]`
Rule-out: "Checked team membership control for [team list]: no injection path — [reason]."

Chain 1 check after 2a: Add any TEAM-GAP (Discovered In: "Phase 2a team membership — [team name]"). If none: "Phase 2a: no TEAM-GAP entries — [teams checked, basis]."

**2b — Cross-entity permission chain:**

Select the entity with the highest data sensitivity using Phase 1c categories to justify the selection explicitly.

Trace at least two entity hops:

`[Role] → [Entity A, op: X, scope: Y] → [Relationship: lookup/child/N:N] → [Entity B, op: X, scope: Y]`

At each hop: mark as INTENTIONAL (expected by design) or EMERGENT (side effect of relationship structure). EMERGENT hops are gaps.

Chain 1 check after 2b: Add any CROSS-ENTITY findings (Discovered In: "Phase 2b cross-entity — [role] via [Entity A] → [Entity B]").

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

One subsection per role from Phase 1b matrix. Do not merge. Do not write a collective statement covering all roles.

For each role:

**Role: [name]**

Escalation-capable privileges examined:
- Team membership Write: [YES / NO — evidence: which table or configuration checked]
- Security role assignment Write: [YES / NO — evidence]
- Record ownership Assign scope: [scope — state whether reassignment can place records under a higher-privilege owner]
- Business unit configuration Write: [YES / NO — evidence]

Conclusion: ESCALATION-PATH FOUND / RULED OUT

If FOUND: `[Role] → [action] → [elevated access achieved] — mechanism: [how the action produces elevation]`
If RULED OUT: "No path — [specific reason for each checked privilege: why it does not permit elevation for this role]."

Chain 1 check per role: ESCALATION-PATH FOUND → add to register (Discovered In: "Phase 3 escalation — [role name]"). Ruled out = no entry.

**Negative-check evidence per gap type:** For any gap type that yields no finding across all roles, document explicitly:
"Checked [specific items examined] for [role list]; [gap type] does not apply because [specific reason]."
A blanket "no issues found" without enumeration of what was examined fails C-12.

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative:**
CRUD + Assign + Record Scope per entity from Phase 1b. Cross-reference with Phase 1c sensitive fields: which PII, Financial, and Audit/Compliance fields can Customer Service read or write? For each sensitive field accessible to CS: is access appropriate to the CS job function, or does it constitute overreach?

**Dataverse Security Expert:**
CRUD + Assign + Record Scope per entity. Every privilege the expert holds that Customer Service does not. Does the expert role follow least-privilege, or does it hold admin-level access that extends beyond configuration scope?

**Contrast statement (required):**
One paragraph explicitly contrasting the two roles. Both "Customer Service" and "Dataverse security expert" must appear by name. State: what Customer Service can do that the expert cannot, and what the expert can do that Customer Service cannot. A contrast section that names one role without the other fails C-07.

Chain 1 check after Phase 4: Any gaps surfaced during role differentiation that are not yet in the register? Add now (Discovered In: "Phase 4 role differentiation — [role] — [issue]").

---

## PHASE 5 — REMEDIATION

Chain 2 active. For every entry in the LIVE GAPS REGISTER, apply the Remediation Contract from Phase 0.

**Slot-fill instruction — Chain 2:**
The Discovered In value in each remediation entry below is a copy operation, not a writing operation. Locate the Discovered In cell in the register row for this gap ID. Copy it exactly as it appears. Do not shorten, summarize, or restate.

**Mismatch example (self-check before closing this phase):**

> Suppose the LIVE GAPS REGISTER contains:
> `| G-02 | Phase 1c FLS check — Contact.AnnualRevenue | MISSING-FLS | Contact | AnnualRevenue | Customer Service | HIGH |`
>
> **PASSING** — verbatim copy:
> `Gap G-02 (Discovered In: Phase 1c FLS check — Contact.AnnualRevenue):`
>
> **FAILING** — looks reasonable, is not verbatim:
> `Gap G-02 (Discovered In: FLS gap — AnnualRevenue):` ← entity name dropped, section label changed
> `Gap G-02 (Discovered In: Phase 1c FLS):` ← field name truncated
> `Gap G-02 (Discovered In: Phase 1 — AnnualRevenue):` ← "FLS check — Contact" compressed out
> `Gap G-02 (Discovered In: Contact field security issue):` ← entirely rephrased
>
> **Self-check:** Before writing "Phase 5 complete", read each Discovered In echo and compare it word-for-word against the register cell. If it matches any FAILING form above — partial, abbreviated, or rephrased — rewrite it to match the PASSING form.

For each register entry:

```
Gap [ID] (Discovered In: [verbatim copy from register — self-checked]):
  Config change:     [exact configuration element — role name / field name / profile name /
                      rule name, and where to find it in the solution]
  Expected state:    [what you will see after applying the change — name the UI view or
                      test query that will differ]
  Verification step: [the action to confirm the fix — name the UI location and expected
                      result, e.g., "Open Security > Field Security Profiles > [profile] >
                      [entity] > [field]: verify [role] shows Read-only"]
```

Every gap gets all three fields. A gap with Expected state missing fails C-13. A gap without a specific, executable Verification step fails C-13. "Consult your admin" and "review this configuration" fail C-08 and C-13 together.

Phase 5 close: "Phase 5 complete. [N] gaps remediated. Chain 2 self-check applied: all Discovered In echoes verified verbatim against register."
