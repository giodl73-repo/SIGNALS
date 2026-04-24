# trace-permissions Variate — Round 7
**Date:** 2026-03-15
**Rubric:** v6 (C-01 through C-23 — C-21/C-22/C-23 added from R6 excellence signals)
**Target criteria:** C-21 (anti-speculation preamble as standalone protocol statement before gate table), C-22 (category drift named as discrete inertia threat I-6 with CATEGORY-DRIFT-VIOLATION marker), C-23 (chain-verifier gate row 5 with token-swap check: Step 1 category count vs downstream annotation count)

**Baseline:** R6-V-05 achieved all three structural locks from Round 5: FLS ENTRY CLOSED terminator, ACTIVATION STATE LOG, Phase 5b self-check close with TRACE CLOSE TOKEN. The three new criteria open the next layer. C-21 requires a submission gate fronted by a protocol-level anti-speculation mandate that makes VERDICT-FAIL visible before the table header — R6-V-05 has no submission gate. C-22 requires the analysis to pre-declare category drift as a named, numbered inertia threat with its own identifier and a fire-on-trigger marker — R6-V-05 has no inertia threat inventory. C-23 requires one gate row to jointly cross-check the Step 1 category inventory completeness, PR-1 propagation into FLS ENTRY blocks, and evidence citation coverage atomically via a token-swap comparison — no prior round closes all three in a single row.

---

## Round 7 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Phrasing register — C-21 isolation: submission gate opened with a standalone ANTI-SPECULATION MANDATE declaration naming VERDICT-FAIL as a protocol-level statement before the table header | R6-V-05 ends at Phase 5b with the TRACE CLOSE TOKEN. No subsequent mechanism catches speculative passes in a downstream verification step. A submission gate with VERDICT-FAIL declared *before* the table header makes the anti-speculation rule visible at the section level — not discoverable only by reading inside a table cell. Row 5 checks Phase 5b TRACE CLOSE TOKEN presence; no chain-verifier or token-swap. Phase 1c unchanged. C-22 and C-23 unsatisfied. Hypothesis: 24/170 gain on C-21. |
| V-02 | Inertia framing — C-22 isolation: inertia threat table I-1 through I-6 declared in Phase 1c before the category inventory; PR-1 propagation contract established before Step 1 runs | R6-V-05's Phase 1c Step 1 is an anonymous category table with no declared threat frame. Declaring I-1 through I-5 (existing structural risks) plus I-6 (category drift — inline re-derivation of PII/Financial/Audit/Compliance labels downstream of Step 1) before Step 1 runs places category drift on equal footing with the original five threats. PR-1 declares the Step 1 table as the single category source of truth; CATEGORY-DRIFT-VIOLATION fires on re-derivation. No submission gate. C-21 and C-23 unsatisfied. Hypothesis: gain on C-22 only. |
| V-03 | Output format — C-23 isolation: submission gate added; row 5 is a chain-verifier integrating Step 1 category token + PR-1 propagation status + evidence citation coverage with explicit token-swap notation | R6-V-05 has no submission gate. Row 5 cross-checks the Phase 1c Step 1 FLS-scope row count against the downstream FLS ENTRY Category annotation count — the token-swap check — making the categorization chain end-to-end verifiable in a single gate row. Phase 1c Step 1 gains a section-close line recording its token for the gate. No pre-gate preamble (C-21 not targeted). No I-6 threat table (C-22 not targeted). Hypothesis: gain on C-23 only. |
| V-04 | Combined — Inertia framing + Phrasing register (C-22 + C-21): I-6 threat + PR-1 in Phase 1c, plus submission gate with pre-gate anti-speculation preamble | I-6 and the pre-gate preamble operate at different phases on different output elements: I-6 fires during Phase 1c Step 2 (production-time); VERDICT-FAIL applies at the submission gate (review-time). They do not interact. V-04 tests whether the two named violation types (CATEGORY-DRIFT-VIOLATION and VERDICT-FAIL) coexist clearly without conceptual bleed. Row 5 checks Phase 5b TRACE CLOSE TOKEN only — C-23 token-swap not targeted. Hypothesis: gain on C-21 + C-22. |
| V-05 | Combined — all three axes + rubric-verbatim language: ANTI-SPECULATION MANDATE preamble (C-21) + I-1 through I-6 with PR-1 (C-22) + chain-verifier gate row 5 with token-swap (C-23) + rubric-exact pass-condition phrases at each enforcement point | Maximum specification fidelity. C-21's phrase ("protocol-level statement before the table header") in the preamble header. C-22's phrase ("carries its own identifier and a marker that fires on re-derivation") in the I-6 threat row. C-23's phrase ("end-to-end chain verification ... includes a token-swap check") in gate row 5's label. All R6-V-05 mechanisms preserved exactly. Hypothesis: gain on all three new criteria. |

---

## V-01 — Single-Axis: Submission Gate with Pre-Gate Anti-Speculation Preamble (C-21 Isolation)

**Axis:** Phrasing register — the submission gate section opens with a standalone ANTI-SPECULATION MANDATE declaration naming VERDICT-FAIL before the table header, not inside it
**Hypothesis:** R6-V-05 closes at Phase 5b with the TRACE CLOSE TOKEN. After the trace closes, no protocol prevents a reviewer from accepting speculative passes in a downstream verification step. The submission gate added here creates a final verification layer whose distinguishing feature is structural placement: VERDICT-FAIL appears as a section-level statement before any table row is visible. A gate that buries the named violation inside a header cell satisfies C-20 but not C-21. V-01 tests whether the pre-gate preamble placement alone — with no inertia threat list and no chain-verifier row — drives a ceiling outcome on C-21.

---

You are running a permissions trace signal for: {{topic}}

---

## PHASE 0 — FULL AUDIT CHAIN GATE

**Complete this phase and write the ACTIVATION STATE LOG before Phase 1 content.**

This trace operates under a bidirectional audit chain. Both directions are pre-established here and remain active for the full output.

**Chain 1 — Discovery to register (active during Phases 1–4):**
Every gap found during Phases 1–4 is entered into the LIVE GAPS REGISTER at the moment of discovery. The Discovered In field records the exact section and context — e.g., "Phase 1c FLS check — Contact.AnnualRevenue". Set at discovery time, not reconstructed.

**Chain 2 — Register to remediation echo (active during Phase 5a):**
Every register entry is echoed in Phase 5a via verbatim slot-fill. The Discovered In value is copied exactly from the register cell. Chain 2 is verified in Phase 5b — that verification is a **precondition for closing the trace, not a recommended step**.

**Per-row FLS trigger — ACTIVE now:**
During Phase 1c, the three-part FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED block format is active. The CLOSED terminator is required before any subsequent FLS ENTRY begins. This makes **co-authorship a structural property of the format**: a Gap? = YES cell without a completed REGISTER SLOT and a CLOSED marker is a broken block detectable by inspection. N/A markers on NO-gap REGISTER SLOTs make **trigger completeness provable from the output alone**.

**Remediation template (pre-declared; applied in Phase 5a to every register entry):**

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

**PHASE 0 GATE — ACTIVATION STATE LOG:**

This log is an **execution record, not a declarative checklist**. Each entry records that the named mechanism is already active as of Phase 0 close — not that it will be activated when the relevant phase is reached.

| Mechanism | Status | Notes |
|-----------|--------|-------|
| Chain 1 — discovery → register, Discovered In set at point of discovery | ACTIVE | Governs all register entries in Phases 1–4 |
| Chain 2 — register → Phase 5a verbatim echo, copy-not-write | ACTIVE | Verified in Phase 5b (structural precondition) |
| Per-row FLS trigger — FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED | ACTIVE | Structural format enforces co-authorship; CLOSED terminator required |
| Remediation template — Config change / Expected state / Verification step | ACTIVE | All three fields required; vague advice fails Config change |
| Mismatch example — Phase 5b self-check instrument | LOADED | Present in working context; Phase 5b self-check is a precondition for trace close |

*All mechanisms confirmed ACTIVE or LOADED at Phase 0 close. Entering PHASE 1.*

---

## LIVE GAPS REGISTER

Opened at Phase 0. Populated inline during Phases 1–4. Chain 1 enforcement point.

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

- **Discovered In**: exact section name and context, set at discovery time — Chain 2 copies this verbatim; Phase 5b verifies the copy
- Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY
- Severity: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 — ENTITY AND ROLE MAP

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Scope | Default access for unauthenticated user |
|--------|-----------------|-------|----------------------------------------|

OWD scope values: Organization / Business Unit / Owner. Missing scope = incomplete row.

Chain 1 check after 1a: OWD anomaly → register (Discovered In: "Phase 1a OWD — [entity]"). None → "Phase 1a: no OWD anomalies — [basis for determination]."

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Team / User / Sharing-[rule name]. All roles with any privilege must appear. Dataverse system names required — display names alone fail C-01.

Chain 1 check after 1b: Scope broader than function → register (Discovered In: "Phase 1b operation-role matrix — [role]"). None → "Phase 1b: no scope anomalies — [basis]."

**1c — Sensitive field categorization:**

Step 1: categorize all fields before checking FLS:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII (name, contact info, ID, government data) | |
| | Financial (billing, pricing, payment, credit) | |
| | Audit/Compliance (modified-by, consent, audit trail) | |
| | Operational (status, queue, SLA, internal notes) | |

Write "none" for empty categories.

Step 2: FLS check for all PII, Financial, and Audit/Compliance fields. Per-row trigger ACTIVE per Phase 0 log — use THREE-PART FLS ENTRY BLOCKS.

**Block format — mandatory for every sensitive field:**

```
FLS ENTRY [n] — [Entity].[Field]
| Entity | Field | Category | FLS Profile? | CS: Read | CS: Write | Expert: Read | Expert: Write | Gap? |
|--------|-------|----------|-------------|----------|-----------|--------------|---------------|------|
| ...    | ...   | ...      | ...         | ...      | ...       | ...          | YES/NO |

REGISTER SLOT [n] (Chain 1 — complete before CLOSED marker):
```

If Gap? = YES:
```
| [G-NN] | Phase 1c FLS check — [Entity].[Field] | MISSING-FLS | [Entity] | [Field] | [Role] | [Severity] |
→ Added to LIVE GAPS REGISTER.
```

If Gap? = NO:
```
→ No gap. Register slot: N/A — [brief confirmation].
```

```
FLS ENTRY [n] CLOSED
```

**Block boundary rule:** A new FLS ENTRY block may not begin until FLS ENTRY [n] CLOSED appears. Co-authorship is a property of the block structure — not a behavioral obligation.

Section close: "Phase 1c FLS complete. [N] FLS ENTRY blocks. [N] CLOSED markers written (must equal [N]). [N] YES entries. [N] N/A register slots. All blocks terminated."

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

Chain 1 check after 1d: Conflicts = YES → register (Discovered In: "Phase 1d sharing rule — [rule name]"). None → "Phase 1d: no SHARING-CONFLICT — [rules checked, specific reason]."

---

## PHASE 2 — TEAM AND CROSS-ENTITY

**2a — Team membership gap:**

For each team-scoped role: who controls team membership, and can that control reach elevated access?

Finding: `[Role] → [adds user to Team X] → [elevated access via team] — mechanism: [how]`
Rule-out: "Checked [teams]: no injection path — [reason]."

Chain 1 check: TEAM-GAP if found (Discovered In: "Phase 2a team membership — [team name]"). None → "Phase 2a: no TEAM-GAP — [teams checked, basis]."

**2b — Cross-entity permission chain:**

Select highest-sensitivity entity (justify from Phase 1c categories). Trace at least two hops:

`[Role] → [Entity A, op: X, scope: Y] → [Relationship: lookup/child/N:N] → [Entity B, op: X, scope: Y]`

INTENTIONAL or EMERGENT at each hop. EMERGENT = gap.

Chain 1 check: CROSS-ENTITY if found (Discovered In: "Phase 2b cross-entity — [role] via [Entity A] → [Entity B]").

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

One subsection per role from Phase 1b. No collective statements.

**Role: [name]**

Escalation-capable privileges examined:
- Team membership Write: [YES / NO — evidence]
- Security role assignment Write: [YES / NO — evidence]
- Record ownership Assign scope: [scope — whether reassignment permits elevation]
- Business unit configuration Write: [YES / NO — evidence]

Conclusion: ESCALATION-PATH FOUND / RULED OUT

If FOUND: `[Role] → [action] → [elevated access] — mechanism: [how]`
If RULED OUT: "No path — [specific reason per privilege]."

Chain 1 check per role: FOUND → register (Discovered In: "Phase 3 escalation — [role name]").

**Negative-check evidence per gap type:** For any gap type with no finding: "Checked [specific items] for [role list]; [type] does not apply because [specific reason]."

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative:**
CRUD + Assign + Record Scope per entity. Cross-reference Phase 1c sensitive fields: PII, Financial, Audit/Compliance accessible to CS — appropriate or overreach?

**Dataverse Security Expert:**
CRUD + Assign + Record Scope per entity. Every privilege the expert holds that Customer Service does not. Least-privilege or admin-level overreach?

**Contrast statement (required):**
One paragraph, both "Customer Service" and "Dataverse security expert" appear by name.

Chain 1 check: Undocumented gaps → register (Discovered In: "Phase 4 role differentiation — [role] — [issue]").

---

## PHASE 5a — REMEDIATION ENTRIES

Chain 2 active. For every register entry, apply the Remediation Contract from Phase 0.

**Slot-fill instruction — Chain 2:** Copy the Discovered In cell from the register row for this gap ID exactly — copy operation, not writing operation.

For each register entry:

```
Gap [ID] (Discovered In: [verbatim copy from register — Chain 2 slot-fill]):
  Config change:     [exact element — role / field / profile / rule and location]
  Expected state:    [UI view or query after fix]
  Verification step: [executable action — UI location and expected result]
```

All three fields required.

---

## PHASE 5b — CHAIN 2 SELF-CHECK CLOSE

**This section is a precondition for closing the trace, not a recommended step. The trace is not closed until the TRACE CLOSE TOKEN is written.**

The mismatch example was loaded at Phase 0. Apply it now.

**Mismatch example:**

> Register: `| G-02 | Phase 1c FLS check — Contact.AnnualRevenue | MISSING-FLS | ... |`
>
> **PASSING echo:** `Gap G-02 (Discovered In: Phase 1c FLS check — Contact.AnnualRevenue):`
>
> **FAILING echoes:**
> `Gap G-02 (Discovered In: FLS gap — AnnualRevenue):` ← entity and section label changed
> `Gap G-02 (Discovered In: Phase 1c FLS):` ← field name truncated
> `Gap G-02 (Discovered In: Phase 1 — AnnualRevenue):` ← "FLS check — Contact" compressed
> `Gap G-02 (Discovered In: Contact field security issue):` ← rephrased
>
> Before completing the table: compare each echo word-for-word. Rewrite any FAILING forms.

**Self-check verification table:**

| Gap ID | Register: Discovered In (exact text) | Phase 5a Echo: Discovered In (exact text) | Match? |
|--------|--------------------------------------|-------------------------------------------|--------|

Fill one row per register entry. Match? = YES or FAIL + corrected.

**TRACE CLOSE TOKEN:** `Chain 2 self-check applied: all Discovered In echoes verified verbatim against register. Rows verified: [N]. FAIL corrections: [N]. Trace closed.`

---

## SUBMISSION GATE

**ANTI-SPECULATION MANDATE — protocol-level declaration, before table:**

No gate row in the table below may record PASS without citing specific evidence from this trace output: a named section, row count, or finding. A row that asserts correctness without evidence citation is a VERDICT-FAIL violation. VERDICT-FAIL is a named violation type, not a severity label — it applies regardless of whether the underlying analysis was thorough. This declaration governs all five rows. Read it before reading any row in the table.

| Row | Check | Evidence Cited | Status |
|-----|-------|----------------|--------|
| 1 | All entities in Phase 1a with OWD and scope stated | Cite Phase 1a row count and scope values | PASS / VERDICT-FAIL |
| 2 | All roles named by Dataverse system name; record scope per entity in Phase 1b | Cite Phase 1b role names and Record Scope column | PASS / VERDICT-FAIL |
| 3 | FLS analyzed for all PII, Financial, Audit/Compliance fields; all FLS ENTRY blocks CLOSED | Cite Phase 1c section close: N blocks, N CLOSED markers | PASS / VERDICT-FAIL |
| 4 | All gap types checked with evidence; negative-check evidence for zero-finding types | Cite Phase 3 negative-check statements and Phase 2 rule-outs | PASS / VERDICT-FAIL |
| 5 | All register entries remediated in Phase 5a; Chain 2 self-check complete with TRACE CLOSE TOKEN written | Cite Phase 5b TRACE CLOSE TOKEN text and row count | PASS / VERDICT-FAIL |

Gate passes only when all five rows read PASS with evidence cited. Any VERDICT-FAIL row halts the gate.

---

## V-02 — Single-Axis: Inertia Threat Table with I-6 Category Drift (C-22 Isolation)

**Axis:** Inertia framing — an inertia threat table (I-1 through I-6) is declared in Phase 1c before the category inventory; I-6 names category drift as a discrete, numbered threat carrying its own identifier and a CATEGORY-DRIFT-VIOLATION marker that fires on re-derivation; PR-1 propagation contract declares Step 1 as the single category source of truth
**Hypothesis:** R6-V-05's Phase 1c Step 1 is an anonymous category table. A model that treats PII/Financial/Audit/Compliance labels as convenient annotations may re-derive them inline in FLS ENTRY Category columns without recognizing the re-derivation as a structural gap. Declaring I-6 before Step 1 places category drift on equal footing with I-1 through I-5. The CATEGORY-DRIFT-VIOLATION marker fires on any FLS ENTRY block where the Category value was not inherited from Step 1. PR-1 makes inheritance a declared contract, not an implied convention. No submission gate added (C-21 and C-23 not targeted).

---

You are running a permissions trace signal for: {{topic}}

---

## PHASE 0 — FULL AUDIT CHAIN GATE

**Complete this phase and write the ACTIVATION STATE LOG before Phase 1 content.**

This trace operates under a bidirectional audit chain. Both directions pre-established here and active for the full output.

**Chain 1 — Discovery to register (active during Phases 1–4):**
Every gap entered into the LIVE GAPS REGISTER at moment of discovery. Discovered In set at discovery time, not reconstructed.

**Chain 2 — Register to remediation echo (active during Phase 5a):**
Every register entry echoed in Phase 5a via verbatim slot-fill. Verified in Phase 5b — **precondition for closing the trace, not a recommended step**.

**Per-row FLS trigger — ACTIVE now:**
Three-part FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED block format active during Phase 1c. **Co-authorship is a structural property of the format**: CLOSED terminator required. N/A markers make **trigger completeness provable from the output alone**.

**Remediation template (pre-declared; applied in Phase 5a):**

```
Gap [ID] (Discovered In: [verbatim from register]):
  Config change:     [exact element and location]
  Expected state:    [UI view or query after fix]
  Verification step: [executable action]
```

**PHASE 0 GATE — ACTIVATION STATE LOG:**

This log is an **execution record, not a declarative checklist**.

| Mechanism | Status | Notes |
|-----------|--------|-------|
| Chain 1 — discovery → register, Discovered In at discovery | ACTIVE | Governs Phases 1–4 |
| Chain 2 — register → Phase 5a verbatim echo, copy-not-write | ACTIVE | Verified in Phase 5b |
| Per-row FLS trigger — FLS ENTRY [n] / REGISTER SLOT [n] / CLOSED | ACTIVE | CLOSED terminator required |
| Remediation template — Config change / Expected state / Verification step | ACTIVE | All three required |
| Mismatch example — Phase 5b self-check instrument | LOADED | Required before trace close |
| I-6 category drift / PR-1 propagation contract | ACTIVE | Fires in Phase 1c Step 2 on re-derivation |

*All mechanisms confirmed at Phase 0 close. Entering PHASE 1.*

---

## LIVE GAPS REGISTER

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

- Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY / CATEGORY-DRIFT
- Severity: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 — ENTITY AND ROLE MAP

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Scope | Default access for unauthenticated user |
|--------|-----------------|-------|----------------------------------------|

Chain 1 check after 1a: OWD anomaly → register (Discovered In: "Phase 1a OWD — [entity]"). None → "Phase 1a: no OWD anomalies — [basis]."

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Dataverse system names required. Chain 1 check after 1b: scope anomaly → register.

**1c — Sensitive field categorization:**

**Inertia threat inventory (declared before Step 1 — each threat is a named structural risk this analysis is designed to detect):**

| ID | Threat | Fires During | Marker |
|----|--------|-------------|--------|
| I-1 | OWD defaults creating unexpected default access (None → Read or higher without intended coverage) | Phase 1a | ESCALATION-PATH (OWD scope) in register |
| I-2 | Missing FLS profiles on PII, Financial, or Audit/Compliance fields | Phase 1c FLS check | MISSING-FLS in register |
| I-3 | Sharing rule overrides granting access to roles not intended to hold it | Phase 1d | SHARING-CONFLICT in register |
| I-4 | Team membership control enabling privilege injection by lower-privilege roles | Phase 2a | TEAM-GAP in register |
| I-5 | EMERGENT cross-entity hops enabling access not directly granted by role privileges | Phase 2b | CROSS-ENTITY in register |
| I-6 | **Category drift** — inline re-derivation of PII / Financial / Audit/Compliance / Operational labels at any point downstream of Phase 1c Step 1; the Step 1 category table is the sole source of truth for all downstream Category values | Phase 1c Step 2 onward | CATEGORY-DRIFT-VIOLATION |

**PR-1: Category propagation contract (established here; active from Step 2 forward):**
The Category column in every FLS ENTRY block inherits its value from the Step 1 category table below — not re-derived inline. At the start of Step 2, write: `[Category chain: active — all FLS ENTRY Category values inherit from Step 1 table]`. Any FLS ENTRY block where the Category value differs from the Step 1 table fires I-6 with marker CATEGORY-DRIFT-VIOLATION and a register entry (Discovered In: "Phase 1c Step 2 — [Entity].[Field] — category re-derived as [value], Step 1 records [correct value]").

Step 1: category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII (name, contact info, ID, government data) | |
| | Financial (billing, pricing, payment, credit) | |
| | Audit/Compliance (modified-by, consent, audit trail) | |
| | Operational (status, queue, SLA, internal notes) | |

Write "none" for empty categories.

Step 2: FLS check for all PII, Financial, and Audit/Compliance fields. Per-row trigger ACTIVE. `[Category chain: active — all FLS ENTRY Category values inherit from Step 1 table]`

**Block format:**

```
FLS ENTRY [n] — [Entity].[Field]
| Entity | Field | Category | FLS Profile? | CS: Read | CS: Write | Expert: Read | Expert: Write | Gap? |
|--------|-------|----------|-------------|----------|-----------|--------------|---------------|------|
| ...    | ...   | ...      | ...         | ...      | ...       | YES/NO |

REGISTER SLOT [n] (Chain 1 — complete before CLOSED marker):
```

If Gap? = YES: `| [G-NN] | Phase 1c FLS check — [Entity].[Field] | MISSING-FLS | ... → Added.`
If Gap? = NO: `→ No gap. N/A — [confirmation].`

```
FLS ENTRY [n] CLOSED
```

**Block boundary rule:** CLOSED terminator required. Category value must match Step 1 table — PR-1 active; re-derivation fires CATEGORY-DRIFT-VIOLATION.

Section close: "Phase 1c FLS complete. [N] blocks. [N] CLOSED. [N] YES. [N] N/A. Category chain: all inherited from Step 1 / [k] CATEGORY-DRIFT-VIOLATION entries."

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

Chain 1 check: Conflicts → register. None → "Phase 1d: no SHARING-CONFLICT — [reason]."

---

## PHASE 2 — TEAM AND CROSS-ENTITY

**2a:** Finding: `[Role] → [Team X] → [elevated access] — mechanism: [how]`. Rule-out: "Checked [teams]: no path — [reason]." Chain 1 check: TEAM-GAP or explicit rule-out.

**2b:** Highest-sensitivity entity (justify from Phase 1c Step 1). Trace two hops. INTENTIONAL / EMERGENT. EMERGENT = gap. Chain 1 check: CROSS-ENTITY or explicit rule-out.

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

One subsection per role from Phase 1b. No collective statements.

**Role: [name]**
- Team membership Write: [YES/NO — evidence]
- Security role assignment Write: [YES/NO — evidence]
- Record ownership Assign scope: [scope — elevation possible?]
- Business unit Write: [YES/NO — evidence]

FOUND → `[Role] → [action] → [elevated access]` + register entry. RULED OUT → reason per privilege.

**Negative-check evidence** for any zero-finding gap type.

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative:** CRUD + scope. Sensitive field access (from Phase 1c Step 1) appropriate or overreach?

**Dataverse Security Expert:** CRUD + scope. Every privilege CS lacks. Least-privilege or overreach?

**Contrast statement (required):** One paragraph, both role names explicit.

Chain 1 check: undocumented gaps → register.

---

## PHASE 5a — REMEDIATION ENTRIES

Chain 2 active. Copy Discovered In verbatim. All three template fields required.

```
Gap [ID] (Discovered In: [verbatim]):
  Config change:     [exact element]
  Expected state:    [UI view after fix]
  Verification step: [executable action]
```

---

## PHASE 5b — CHAIN 2 SELF-CHECK CLOSE

**Precondition for closing the trace.**

**Mismatch example:** PASSING = verbatim copy. FAILING = truncated / dropped / rephrased.

**Self-check verification table:**

| Gap ID | Register: Discovered In (exact) | Phase 5a Echo: Discovered In (exact) | Match? |
|--------|--------------------------------|--------------------------------------|--------|

**TRACE CLOSE TOKEN:** `Chain 2 self-check applied. Rows: [N]. FAIL corrections: [N]. Trace closed.`

---

## V-03 — Single-Axis: Submission Gate with Chain-Verifier Row 5 (C-23 Isolation)

**Axis:** Output format — a submission gate is added after Phase 5b; row 5 jointly verifies Phase 1c Step 1 category inventory completeness, PR-1 propagation into FLS ENTRY blocks, and evidence citation coverage for rows 1–4 via a token-swap check comparing Step 1 FLS-scope row count against downstream FLS ENTRY Category annotation count
**Hypothesis:** R6-V-05 has no submission gate. A gate row 5 that cross-checks the Step 1 category table FLS-scope row count against the count of Category annotations in FLS ENTRY blocks — the token-swap check — makes the categorization chain end-to-end verifiable in a single atomic gate row. Phase 1c Step 1 gains a section-close line recording its token count for the gate to consume. No pre-gate preamble (C-21 not targeted). No I-6 threat table (C-22 not targeted). The Phase 1c Step 2 chain-reminder annotation `[Category chain: active]` is added minimally to provide the downstream annotation count, but no full PR-1 contract or I-6 threat is declared.

---

You are running a permissions trace signal for: {{topic}}

---

## PHASE 0 — FULL AUDIT CHAIN GATE

**Complete this phase and write the ACTIVATION STATE LOG before Phase 1 content.**

This trace operates under a bidirectional audit chain. Both directions pre-established here and active for the full output.

**Chain 1 — Discovery to register (active during Phases 1–4):**
Every gap entered into the LIVE GAPS REGISTER at moment of discovery. Discovered In set at discovery time.

**Chain 2 — Register to remediation echo (active during Phase 5a):**
Every register entry echoed in Phase 5a via verbatim slot-fill. Verified in Phase 5b — **precondition for closing the trace, not a recommended step**.

**Per-row FLS trigger — ACTIVE now:**
Three-part FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED active during Phase 1c. **Co-authorship is a structural property of the format**. N/A markers make **trigger completeness provable from the output alone**.

**Remediation template (pre-declared):**

```
Gap [ID] (Discovered In: [verbatim]):
  Config change:     [exact element and location]
  Expected state:    [UI view after fix]
  Verification step: [executable action]
```

**PHASE 0 GATE — ACTIVATION STATE LOG:**

This log is an **execution record, not a declarative checklist**.

| Mechanism | Status | Notes |
|-----------|--------|-------|
| Chain 1 — discovery → register, Discovered In at discovery | ACTIVE | Governs Phases 1–4 |
| Chain 2 — register → Phase 5a verbatim echo | ACTIVE | Verified in Phase 5b |
| Per-row FLS trigger — FLS ENTRY [n] / REGISTER SLOT [n] / CLOSED | ACTIVE | CLOSED terminator required |
| Remediation template — Config change / Expected state / Verification step | ACTIVE | All three required |
| Mismatch example — Phase 5b self-check instrument | LOADED | Required before trace close |
| Step 1 category token — supplied to submission gate row 5 | PENDING | Set at Phase 1c Step 1 close |

*All mechanisms confirmed at Phase 0 close. Step 1 token will be set during Phase 1c. Entering PHASE 1.*

---

## LIVE GAPS REGISTER

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

- Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY
- Severity: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 — ENTITY AND ROLE MAP

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Scope | Default access for unauthenticated user |
|--------|-----------------|-------|----------------------------------------|

Chain 1 check after 1a: OWD anomaly → register. None → "Phase 1a: no OWD anomalies — [basis]."

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Dataverse system names required. Chain 1 check: scope anomaly → register.

**1c — Sensitive field categorization:**

Step 1: category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII (name, contact info, ID, government data) | |
| | Financial (billing, pricing, payment, credit) | |
| | Audit/Compliance (modified-by, consent, audit trail) | |
| | Operational (status, queue, SLA, internal notes) | |

Write "none" for empty categories.

**Step 1 close (required for submission gate row 5):**
"Phase 1c Step 1 complete. Category table rows: [N total]. FLS-scope rows (PII + Financial + Audit/Compliance): [M]. Step 1 token = [M]. The submission gate chain-verifier row will check this value against the downstream FLS ENTRY Category annotation count."

Step 2: FLS check for all PII, Financial, and Audit/Compliance fields. Per-row trigger ACTIVE — THREE-PART FLS ENTRY BLOCKS.

Write at Step 2 start: `[Category chain: active — FLS ENTRY Category values carry the category from Step 1]`

**Block format:**

```
FLS ENTRY [n] — [Entity].[Field]
| Entity | Field | Category | FLS Profile? | CS: Read | CS: Write | Expert: Read | Expert: Write | Gap? |
|--------|-------|----------|-------------|----------|-----------|--------------|---------------|------|
| ...    | ...   | ...      | ...         | ...      | ...       | YES/NO |

REGISTER SLOT [n] (Chain 1 — complete before CLOSED marker):
```

If Gap? = YES: `| [G-NN] | Phase 1c FLS check — [Entity].[Field] | MISSING-FLS | ... → Added.`
If Gap? = NO: `→ No gap. N/A — [confirmation].`

```
FLS ENTRY [n] CLOSED
```

**Block boundary rule:** CLOSED terminator required. Co-authorship is a property of the format.

Section close: "Phase 1c FLS complete. [N] FLS ENTRY blocks. [N] CLOSED markers (must equal [N]). [N] YES. [N] N/A. FLS ENTRY Category annotation count: [M] (must equal Step 1 token [M] — chain-verifier check prepared)."

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

Chain 1 check: Conflicts → register. None → "Phase 1d: no SHARING-CONFLICT — [reason]."

---

## PHASE 2 — TEAM AND CROSS-ENTITY

**2a:** Finding: `[Role] → [Team X] → [elevated access]`. Rule-out. Chain 1 check.

**2b:** Highest-sensitivity entity (justify). Trace two hops. INTENTIONAL / EMERGENT. Chain 1 check.

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

One subsection per role.

**Role: [name]**
- Team membership Write: [YES/NO — evidence]
- Security role assignment Write: [YES/NO — evidence]
- Record ownership Assign scope: [scope — elevation?]
- Business unit Write: [YES/NO — evidence]

FOUND → chain + register. RULED OUT → reason per privilege.

**Negative-check evidence** for any zero-finding gap type.

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative:** CRUD + scope. Sensitive field access appropriate or overreach?

**Dataverse Security Expert:** CRUD + scope. Every privilege CS lacks. Least-privilege or overreach?

**Contrast statement (required):** One paragraph, both role names explicit.

Chain 1 check: undocumented gaps → register.

---

## PHASE 5a — REMEDIATION ENTRIES

Chain 2 active. Verbatim slot-fill. All three template fields required.

```
Gap [ID] (Discovered In: [verbatim]):
  Config change:     [exact element]
  Expected state:    [UI view after fix]
  Verification step: [executable action]
```

---

## PHASE 5b — CHAIN 2 SELF-CHECK CLOSE

**Precondition for closing the trace.**

**Mismatch example:** PASSING = verbatim. FAILING = truncated / dropped / rephrased.

**Self-check verification table:**

| Gap ID | Register: Discovered In | Phase 5a Echo | Match? |
|--------|------------------------|---------------|--------|

**TRACE CLOSE TOKEN:** `Chain 2 self-check applied. Rows: [N]. FAIL corrections: [N]. Trace closed.`

---

## SUBMISSION GATE

| Row | Check | Evidence Cited | Status |
|-----|-------|----------------|--------|
| 1 | All entities in Phase 1a with OWD and scope | Cite Phase 1a row count | PASS / FAIL |
| 2 | All roles by Dataverse system name; record scope per entity | Cite Phase 1b role names | PASS / FAIL |
| 3 | FLS analyzed for all sensitive fields; all CLOSED markers written | Cite Phase 1c close: N blocks, N CLOSED | PASS / FAIL |
| 4 | All gap types checked with evidence; negative-check evidence present | Cite Phase 3 statements | PASS / FAIL |
| 5 | **Category chain end-to-end verification with token-swap check**: Step 1 FLS-scope token = [M] (from Phase 1c Step 1 close); FLS ENTRY Category annotation count downstream = [M] (from Phase 1c section close); token-swap: [M] == [M]? YES/NO. Category chain: all [M] FLS ENTRY blocks carry inherited category values. Evidence citations rows 1–4: all PASS. | Cite Step 1 token and Phase 1c section-close annotation count | PASS / FAIL |

Row 5 is a jointly enforced row: it passes only when token-swap match, category chain status, and evidence coverage all pass simultaneously. A gate where each sub-check is in an independent row with no row verifying the full chain fails C-23.

---

## V-04 — Combined: I-6 Threat + PR-1 with Submission Gate Anti-Speculation Preamble (C-22 + C-21)

**Axis:** Inertia framing + Phrasing register — Phase 1c gains the inertia threat table I-1 through I-6 with PR-1 propagation contract; the submission gate opens with a standalone ANTI-SPECULATION MANDATE naming VERDICT-FAIL before the table header
**Hypothesis:** I-6 and the VERDICT-FAIL preamble enforce against distinct failure modes at different output positions. I-6 fires during Phase 1c Step 2 when a Category value in an FLS ENTRY block is re-derived rather than inherited from Step 1 — it is a production-time constraint. VERDICT-FAIL fires at the submission gate when a row passes without evidence — it is a review-time constraint. The two named violation types (CATEGORY-DRIFT-VIOLATION and VERDICT-FAIL) are semantically separate; V-04 tests whether they coexist clearly. Row 5 checks Phase 5b TRACE CLOSE TOKEN only — the C-23 token-swap check is not targeted.

---

You are running a permissions trace signal for: {{topic}}

---

## PHASE 0 — FULL AUDIT CHAIN GATE

**Complete this phase and write the ACTIVATION STATE LOG before Phase 1 content.**

This trace operates under a bidirectional audit chain. Both directions pre-established here.

**Chain 1 — Discovery to register (active during Phases 1–4):**
Every gap entered into the LIVE GAPS REGISTER at moment of discovery. Discovered In set at discovery time.

**Chain 2 — Register to remediation echo (active during Phase 5a):**
Every register entry echoed verbatim in Phase 5a. Verified in Phase 5b — **precondition for closing the trace, not a recommended step**.

**Per-row FLS trigger — ACTIVE now:**
Three-part FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED active during Phase 1c. **Co-authorship is a structural property of the format**. N/A markers make **trigger completeness provable from the output alone**.

**Remediation template (pre-declared; applied in Phase 5a):**

```
Gap [ID] (Discovered In: [verbatim]):
  Config change:     [exact element and location]
  Expected state:    [UI view after fix]
  Verification step: [executable action]
```

**PHASE 0 GATE — ACTIVATION STATE LOG:**

This log is an **execution record, not a declarative checklist**.

| Mechanism | Status | Notes |
|-----------|--------|-------|
| Chain 1 — discovery → register, Discovered In at discovery | ACTIVE | Governs Phases 1–4 |
| Chain 2 — register → Phase 5a verbatim echo | ACTIVE | Verified in Phase 5b |
| Per-row FLS trigger — FLS ENTRY [n] / REGISTER SLOT [n] / CLOSED | ACTIVE | CLOSED terminator required |
| Remediation template — Config change / Expected state / Verification step | ACTIVE | All three required |
| Mismatch example — Phase 5b self-check instrument | LOADED | Required before trace close |
| I-6 category drift / PR-1 propagation contract | ACTIVE | Fires in Phase 1c Step 2 on re-derivation |

*All mechanisms confirmed at Phase 0 close. Entering PHASE 1.*

---

## LIVE GAPS REGISTER

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

- Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY / CATEGORY-DRIFT
- Severity: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 — ENTITY AND ROLE MAP

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Scope | Default access for unauthenticated user |
|--------|-----------------|-------|----------------------------------------|

Chain 1 check: OWD anomaly → register. None → "Phase 1a: no OWD anomalies — [basis]."

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Dataverse system names required. Chain 1 check: scope anomaly → register.

**1c — Sensitive field categorization:**

**Inertia threat inventory:**

| ID | Threat | Fires During | Marker |
|----|--------|-------------|--------|
| I-1 | OWD defaults creating unexpected default access | Phase 1a | ESCALATION-PATH (OWD scope) |
| I-2 | Missing FLS profiles on sensitive fields | Phase 1c FLS check | MISSING-FLS |
| I-3 | Sharing rule overrides granting unintended access | Phase 1d | SHARING-CONFLICT |
| I-4 | Team membership enabling privilege injection | Phase 2a | TEAM-GAP |
| I-5 | EMERGENT cross-entity hops | Phase 2b | CROSS-ENTITY |
| I-6 | **Category drift** — inline re-derivation of PII/Financial/Audit/Compliance/Operational labels downstream of Phase 1c Step 1 | Phase 1c Step 2 onward | CATEGORY-DRIFT-VIOLATION |

**PR-1: Category propagation contract:**
The Category column in every FLS ENTRY block inherits its value from the Step 1 table below — not re-derived inline. At Step 2 start, write: `[Category chain: active — inherit from Step 1]`. Re-derivation fires I-6 → CATEGORY-DRIFT-VIOLATION → register entry (Discovered In: "Phase 1c Step 2 — [Entity].[Field] — re-derived [value], Step 1 records [correct value]").

Step 1: category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII | |
| | Financial | |
| | Audit/Compliance | |
| | Operational | |

"none" for empty categories.

Step 2: FLS check. `[Category chain: active — inherit from Step 1]`

**Block format:**

```
FLS ENTRY [n] — [Entity].[Field]
| Entity | Field | Category | FLS Profile? | CS: Read | CS: Write | Expert: Read | Expert: Write | Gap? |
|--------|-------|----------|-------------|----------|-----------|--------------|---------------|------|
| ...    | ...   | ...      | ...         | ...      | YES/NO |

REGISTER SLOT [n]:
```

Gap? = YES → register. Gap? = NO → "N/A — [confirmation]."

```
FLS ENTRY [n] CLOSED
```

**Block boundary rule:** CLOSED required. Category must inherit from Step 1 — re-derivation fires CATEGORY-DRIFT-VIOLATION.

Section close: "Phase 1c complete. [N] blocks. [N] CLOSED. [N] YES. [N] N/A. Category chain: all inherited / [k] violations."

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

Chain 1 check: Conflicts → register. None → "Phase 1d: no SHARING-CONFLICT — [reason]."

---

## PHASE 2 — TEAM AND CROSS-ENTITY

**2a:** Finding / rule-out. Chain 1 check: TEAM-GAP or explicit statement.

**2b:** Highest-sensitivity entity (justify from Phase 1c Step 1). Trace two hops. INTENTIONAL / EMERGENT. Chain 1 check.

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

One subsection per role.

**Role: [name]**
- Team membership Write: [YES/NO — evidence]
- Security role assignment Write: [YES/NO — evidence]
- Record ownership Assign scope: [elevation?]
- Business unit Write: [YES/NO — evidence]

FOUND → chain + register. RULED OUT → reason per privilege.

**Negative-check evidence** for zero-finding gap types.

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative:** CRUD + scope. Sensitive field access appropriate or overreach?

**Dataverse Security Expert:** CRUD + scope. Every privilege CS lacks. Least-privilege or overreach?

**Contrast statement (required):** One paragraph, both role names explicit.

Chain 1 check: undocumented gaps → register.

---

## PHASE 5a — REMEDIATION ENTRIES

Chain 2 active. Verbatim slot-fill. All three template fields required.

```
Gap [ID] (Discovered In: [verbatim]):
  Config change:     [exact element]
  Expected state:    [UI view after fix]
  Verification step: [executable action]
```

---

## PHASE 5b — CHAIN 2 SELF-CHECK CLOSE

**Precondition for closing the trace.**

**Mismatch example:** PASSING = verbatim. FAILING = truncated / dropped / rephrased.

**Self-check verification table:**

| Gap ID | Register: Discovered In | Phase 5a Echo | Match? |
|--------|------------------------|---------------|--------|

**TRACE CLOSE TOKEN:** `Chain 2 self-check applied. Rows: [N]. FAIL corrections: [N]. Trace closed.`

---

## SUBMISSION GATE

**ANTI-SPECULATION MANDATE — protocol-level declaration, before table:**

No gate row may record PASS without citing specific evidence from this trace output. A row that asserts correctness without evidence citation is a VERDICT-FAIL violation. VERDICT-FAIL is a named violation type distinct from CATEGORY-DRIFT-VIOLATION (which fires during Phase 1c production) — VERDICT-FAIL applies at gate review time to any speculative pass. This declaration governs all five rows and is a protocol-level statement: it appears before the table, not inside it.

| Row | Check | Evidence Cited | Status |
|-----|-------|----------------|--------|
| 1 | All entities in Phase 1a with OWD and scope | Cite Phase 1a row count and scope values | PASS / VERDICT-FAIL |
| 2 | All roles by Dataverse system name; record scope per entity | Cite Phase 1b role names | PASS / VERDICT-FAIL |
| 3 | FLS analyzed for all sensitive fields; all blocks CLOSED; no CATEGORY-DRIFT-VIOLATION in section close | Cite Phase 1c close: N blocks, N CLOSED, category chain status | PASS / VERDICT-FAIL |
| 4 | All gap types checked with evidence; negative-check evidence present | Cite Phase 3 statements and Phase 2 rule-outs | PASS / VERDICT-FAIL |
| 5 | All register entries remediated in Phase 5a; TRACE CLOSE TOKEN written | Cite Phase 5b token text and row count | PASS / VERDICT-FAIL |

---

## V-05 — Combined: All Three Axes + Rubric-Verbatim Language (C-21 + C-22 + C-23)

**Axis:** Inertia framing + Phrasing register + Output format — I-1 through I-6 with PR-1 in Phase 1c (C-22) + ANTI-SPECULATION MANDATE preamble before gate table (C-21) + chain-verifier gate row 5 with token-swap check (C-23) + rubric-exact pass-condition phrases at each enforcement point
**Hypothesis:** Each of the three new criteria has a distinguishing phrase that separates its pass condition from the prior criterion's pass condition. C-21: "the named violation type must appear as a protocol-level statement before the table header, not only as a cell or row annotation inside it." C-22: "carries its own identifier and a marker that fires on re-derivation." C-23: "end-to-end chain verification ... includes a token-swap check." Embedding these exact phrases at the structural enforcement points — I-6 row, preamble header, gate row 5 label — gives the model the rubric's own test language before the output is generated. All R6-V-05 mechanisms (ACTIVATION STATE LOG, FLS ENTRY CLOSED terminator, Phase 5b self-check close with TRACE CLOSE TOKEN) are preserved exactly.

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
During Phase 1c, the three-part FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED block format is active. The CLOSED terminator is required before any subsequent FLS ENTRY begins. This makes **co-authorship a structural property of the format**: a Gap? = YES cell without a completed REGISTER SLOT and a CLOSED marker is a broken block detectable by inspection. N/A markers on NO-gap REGISTER SLOTs make **trigger completeness provable from the output alone**.

**Remediation template (pre-declared; applied in Phase 5a to every register entry):**

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

**PHASE 0 GATE — ACTIVATION STATE LOG:**

This log is an **execution record, not a declarative checklist**. Each entry records that the named mechanism is already active as of Phase 0 close — not that it will be activated when the relevant phase is reached. The mismatch example must appear as LOADED to confirm it is in working context at Phase 0.

| Mechanism | Status | Notes |
|-----------|--------|-------|
| Chain 1 — discovery → register, Discovered In set at point of discovery | ACTIVE | Governs all register entries in Phases 1–4 |
| Chain 2 — register → Phase 5a verbatim echo, copy-not-write | ACTIVE | Verified in Phase 5b (structural precondition) |
| Per-row FLS trigger — FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED | ACTIVE | Structural format enforces co-authorship; CLOSED terminator required |
| Remediation template — Config change / Expected state / Verification step | ACTIVE | All three fields required; vague advice fails Config change |
| Mismatch example — Phase 5b self-check instrument | LOADED | Present in working context; Phase 5b self-check is a precondition for trace close |
| I-6 category drift / PR-1 — CATEGORY-DRIFT-VIOLATION marker (carries its own identifier and fires on re-derivation) | ACTIVE | Fires during Phase 1c Step 2 on any re-derivation of Step 1 category labels |

*All mechanisms confirmed ACTIVE or LOADED at Phase 0 close. Entering PHASE 1.*

---

## LIVE GAPS REGISTER

Opened at Phase 0. Populated inline during Phases 1–4. Chain 1 enforcement point.

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

- **Discovered In**: exact section name and context, set at discovery time — Chain 2 copies this verbatim; Phase 5b verifies the copy
- Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY / CATEGORY-DRIFT
- Severity: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 — ENTITY AND ROLE MAP

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Scope | Default access for unauthenticated user |
|--------|-----------------|-------|----------------------------------------|

OWD scope: Organization / Business Unit / Owner. Missing scope = incomplete row.

Chain 1 check after 1a: OWD anomaly → register (Discovered In: "Phase 1a OWD — [entity]"). None → "Phase 1a: no OWD anomalies — [basis for determination]."

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Team / User / Sharing-[rule name]. All roles with any privilege. Dataverse system names required — display names alone fail C-01.

Chain 1 check after 1b: Scope broader than function → register (Discovered In: "Phase 1b operation-role matrix — [role]"). None → "Phase 1b: no scope anomalies — [basis]."

**1c — Sensitive field categorization:**

**Inertia threat inventory (declared before Step 1 — each threat carries its own identifier and a marker that fires on re-derivation or violation):**

| ID | Threat | Fires During | Marker |
|----|--------|-------------|--------|
| I-1 | OWD defaults creating unexpected default access (None → Read or higher without intended coverage) | Phase 1a | ESCALATION-PATH (OWD scope) in register |
| I-2 | Missing FLS profiles on PII, Financial, or Audit/Compliance fields | Phase 1c FLS check | MISSING-FLS in register |
| I-3 | Sharing rule overrides granting access to roles not intended to hold it | Phase 1d | SHARING-CONFLICT in register |
| I-4 | Team membership control enabling privilege injection by lower-privilege roles | Phase 2a | TEAM-GAP in register |
| I-5 | EMERGENT cross-entity hops enabling access not directly granted by role privileges | Phase 2b | CROSS-ENTITY in register |
| I-6 | **Category drift** — inline re-derivation of PII / Financial / Audit/Compliance / Operational labels at any point downstream of Phase 1c Step 1; the Step 1 category table is the single source of truth; this threat **carries its own identifier (I-6) and a marker that fires on re-derivation** | Phase 1c Step 2 onward | CATEGORY-DRIFT-VIOLATION in register |

**PR-1: Category propagation contract (established here; active from Step 2 forward):**
The Category column in every FLS ENTRY block must inherit its value from the Step 1 category table below — not re-derived inline. At the start of Step 2, write: `[Category chain: active — inherit from Step 1 table. PR-1 in effect.]`. Any FLS ENTRY block where the Category value differs from or is absent in the Step 1 table fires I-6 with marker CATEGORY-DRIFT-VIOLATION and a register entry (Discovered In: "Phase 1c Step 2 — [Entity].[Field] — category re-derived as [value], Step 1 records [correct value]", Gap type: CATEGORY-DRIFT).

Step 1: category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII (name, contact info, ID, government data) | |
| | Financial (billing, pricing, payment, credit) | |
| | Audit/Compliance (modified-by, consent, audit trail) | |
| | Operational (status, queue, SLA, internal notes) | |

Write "none" for empty categories.

**Step 1 close:** "Phase 1c Step 1 complete. Category table rows: [N total]. FLS-scope rows (PII + Financial + Audit/Compliance): [M]. Step 1 token = [M]. Submission gate row 5 chain-verifier will compare this token against the downstream FLS ENTRY Category annotation count."

Step 2: FLS check for all PII, Financial, and Audit/Compliance fields. Per-row trigger ACTIVE per Phase 0 log. `[Category chain: active — inherit from Step 1 table. PR-1 in effect.]`

**Block format — mandatory for every sensitive field:**

```
FLS ENTRY [n] — [Entity].[Field]
| Entity | Field | Category | FLS Profile? | CS: Read | CS: Write | Expert: Read | Expert: Write | Gap? |
|--------|-------|----------|-------------|----------|-----------|--------------|---------------|------|
| ...    | ...   | ...      | ...         | ...      | ...       | YES/NO |

REGISTER SLOT [n] (Chain 1 — complete before CLOSED marker):
```

If Gap? = YES:
```
| [G-NN] | Phase 1c FLS check — [Entity].[Field] | MISSING-FLS | [Entity] | [Field] | [Role] | [Severity] |
→ Added to LIVE GAPS REGISTER.
```

If Gap? = NO:
```
→ No gap. Register slot: N/A — [brief confirmation].
```

```
FLS ENTRY [n] CLOSED
```

**Block boundary rule:** A new FLS ENTRY block may not begin until FLS ENTRY [n] CLOSED appears. The CLOSED terminator is the structural boundary marker. Its absence is a visibly broken block. **Co-authorship is a structural property of the format, not a behavioral obligation** — the block structure makes omission impossible to overlook. N/A markers on NO-gap REGISTER SLOTs prove the per-row trigger ran for every field, making **trigger completeness provable from the output alone**. Category value in each block must match Step 1 table — PR-1 active; re-derivation fires CATEGORY-DRIFT-VIOLATION (I-6).

Section close: "Phase 1c FLS complete. [N] FLS ENTRY blocks. [N] CLOSED markers written (must equal [N]). [N] YES entries. [N] N/A register slots (must equal NO-gap rows). FLS ENTRY Category annotation count: [M] (must equal Step 1 token [M] — token-swap verified here and in submission gate row 5). Category chain: all [M] FLS ENTRY Category values inherited from Step 1 / [k] CATEGORY-DRIFT-VIOLATION entries. Trigger completeness: verified by CLOSED marker count and N/A slot count."

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

Chain 1 check after 1d: Conflicts = YES → register (Discovered In: "Phase 1d sharing rule — [rule name]"). None → "Phase 1d: no SHARING-CONFLICT — [rules checked, specific reason]."

---

## PHASE 2 — TEAM AND CROSS-ENTITY

**2a — Team membership gap:**

For each team-scoped role: who controls team membership, and can that control reach elevated access?

Finding: `[Role] → [adds user to Team X] → [elevated access via team] — mechanism: [how]`
Rule-out: "Checked [teams]: no injection path — [reason]."

Chain 1 check: TEAM-GAP if found (Discovered In: "Phase 2a team membership — [team name]"). None → "Phase 2a: no TEAM-GAP — [teams checked, basis]."

**2b — Cross-entity permission chain:**

Select highest-sensitivity entity (justify from Phase 1c Step 1 categories). Trace at least two hops:

`[Role] → [Entity A, op: X, scope: Y] → [Relationship: lookup/child/N:N] → [Entity B, op: X, scope: Y]`

INTENTIONAL or EMERGENT at each hop. EMERGENT = gap.

Chain 1 check: CROSS-ENTITY if found (Discovered In: "Phase 2b cross-entity — [role] via [Entity A] → [Entity B]").

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

One subsection per role from Phase 1b. No collective statements.

**Role: [name]**

Escalation-capable privileges examined:
- Team membership Write: [YES / NO — evidence]
- Security role assignment Write: [YES / NO — evidence]
- Record ownership Assign scope: [scope — whether reassignment permits elevation]
- Business unit configuration Write: [YES / NO — evidence]

Conclusion: ESCALATION-PATH FOUND / RULED OUT

If FOUND: `[Role] → [action] → [elevated access] — mechanism: [how]`
If RULED OUT: "No path — [specific reason per privilege: why it does not permit elevation for this role]."

Chain 1 check per role: FOUND → register (Discovered In: "Phase 3 escalation — [role name]").

**Negative-check evidence per gap type:** For any gap type with no finding: "Checked [specific items] for [role list]; [type] does not apply because [specific reason]."

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative:**
CRUD + Assign + Record Scope per entity from Phase 1b. Cross-reference Phase 1c Step 1 sensitive fields: PII, Financial, and Audit/Compliance fields accessible to CS — appropriate or overreach?

**Dataverse Security Expert:**
CRUD + Assign + Record Scope per entity. Every privilege the expert holds that Customer Service does not. Least-privilege or admin-level overreach?

**Contrast statement (required):**
One paragraph, both "Customer Service" and "Dataverse security expert" appear by name. What CS can do that the expert cannot; what the expert can do that CS cannot.

Chain 1 check: Undocumented gaps → register (Discovered In: "Phase 4 role differentiation — [role] — [issue]").

---

## PHASE 5a — REMEDIATION ENTRIES

Chain 2 active. For every register entry, apply the Remediation Contract from Phase 0.

**Slot-fill instruction — Chain 2:** Copy the Discovered In cell from the register row for this gap ID exactly as it appears — copy operation, not writing operation. No shortening, no paraphrasing.

For each register entry:

```
Gap [ID] (Discovered In: [verbatim copy from register — Chain 2 slot-fill]):
  Config change:     [exact configuration element — role / field / profile / rule and location]
  Expected state:    [UI view or query after fix]
  Verification step: [executable action — UI location and expected result]
```

All three fields required.

---

## PHASE 5b — CHAIN 2 SELF-CHECK CLOSE

**This section is a precondition for closing the trace, not a recommended step. The trace is not closed until the TRACE CLOSE TOKEN is written. A Phase 5a section not followed by a completed Phase 5b is an open trace.**

The mismatch example was loaded at Phase 0. Apply it now.

**Mismatch example:**

> Register: `| G-02 | Phase 1c FLS check — Contact.AnnualRevenue | MISSING-FLS | ... |`
>
> **PASSING echo:** `Gap G-02 (Discovered In: Phase 1c FLS check — Contact.AnnualRevenue):` — exact copy
>
> **FAILING echoes:**
> `Gap G-02 (Discovered In: FLS gap — AnnualRevenue):` ← entity and section label changed
> `Gap G-02 (Discovered In: Phase 1c FLS):` ← field name truncated
> `Gap G-02 (Discovered In: Phase 1 — AnnualRevenue):` ← "FLS check — Contact" compressed
> `Gap G-02 (Discovered In: Contact field security issue):` ← entirely rephrased
>
> Before completing the table: compare each echo word-for-word. Rewrite any FAILING forms.

**Self-check verification table:**

| Gap ID | Register: Discovered In (exact text) | Phase 5a Echo: Discovered In (exact text) | Match? |
|--------|--------------------------------------|-------------------------------------------|--------|

Fill one row per register entry. Match? = YES (verbatim) or FAIL + corrected.

**TRACE CLOSE TOKEN (required before trace closes):**

`Chain 2 self-check applied: all Discovered In echoes verified verbatim against register. Rows verified: [N]. FAIL corrections: [N]. Trace closed.`

This token must be written to close the trace. Its absence means Phase 5b is incomplete and the trace is open.

---

## SUBMISSION GATE

**ANTI-SPECULATION MANDATE — the named violation type (VERDICT-FAIL) is a protocol-level statement before the table header, not only a cell or row annotation inside it:**

No gate row may record PASS without citing specific evidence from this trace output — a named section, row count, token value, or finding. A pass recorded without evidence citation is a VERDICT-FAIL violation regardless of whether the underlying analysis was thorough. VERDICT-FAIL is a distinct named violation type, separate from CATEGORY-DRIFT-VIOLATION (which fires during Phase 1c evidence collection) — VERDICT-FAIL applies at gate review time to any row that asserts correctness without evidence. This statement is a protocol-level declaration governing all five rows below. It must be read before any row in the table.

| Row | Check | Evidence Cited | Status |
|-----|-------|----------------|--------|
| 1 | All entities in Phase 1a with OWD and scope stated | Cite Phase 1a row count and scope values | PASS / VERDICT-FAIL |
| 2 | All roles named by Dataverse system name; record scope per entity in Phase 1b | Cite Phase 1b role names and Record Scope column | PASS / VERDICT-FAIL |
| 3 | FLS analyzed for all PII, Financial, Audit/Compliance fields; all FLS ENTRY blocks CLOSED; no CATEGORY-DRIFT-VIOLATION in section close | Cite Phase 1c close: N blocks, N CLOSED, category chain status | PASS / VERDICT-FAIL |
| 4 | All gap types checked with evidence; negative-check evidence for zero-finding types | Cite Phase 3 statements and Phase 2 rule-outs | PASS / VERDICT-FAIL |
| 5 | **End-to-end chain verification that includes a token-swap check**: (a) Step 1 FLS-scope token = [M] (from Phase 1c Step 1 close); (b) FLS ENTRY Category annotation count downstream = [M] (from Phase 1c section close); (c) token-swap: [M] == [M]? YES/NO; (d) PR-1 propagation: all [M] FLS ENTRY blocks carry inherited Category values — no CATEGORY-DRIFT-VIOLATION; (e) evidence citations for rows 1–4: all PASS cited. This row passes only when all five sub-checks pass simultaneously — it is a jointly enforced chain-verifier row, not five independent checks. | Cite Phase 1c Step 1 token value, Phase 1c section-close annotation count, and row 1–4 evidence citations | PASS / VERDICT-FAIL |

Gate passes only when all five rows read PASS with evidence cited. Any VERDICT-FAIL row halts the gate. Row 5 is an atomically enforced chain-verifier — a gate that checks each sub-criterion in an independent row with no row verifying the full chain end-to-end fails C-23.
