# trace-permissions Variate — Round 6
**Date:** 2026-03-15
**Rubric:** v6 (C-01 through C-24 — C-22/C-23/C-24 added from R5-V-05 excellence signals)
**Target criteria:** C-22 (co-authorship enforced as structural format property with N/A completeness markers), C-23 (gate token carries active-state confirmation for all pre-declared structures), C-24 (Phase 5 trace closure gated on explicit self-check completion)

**Baseline:** R5-V-05 achieved all three new criteria in embryonic form — the FLS ENTRY/REGISTER SLOT block structure, the gate token with active-state language, and the Phase 5 self-check close all originate there. The three new criteria pin down exactly what each element must do structurally rather than behaviorally: C-22 requires the block boundary rule to be a format constraint (not a remembered obligation), with N/A markers proving trigger completeness for all rows; C-23 requires the gate token to record each mechanism as ACTIVE (execution log, not to-do list), including the mismatch example as "loaded"; C-24 requires a structural close condition (a required token, not a recommended step) that makes omission visible.

---

## Round 6 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Output format — C-22 isolation: FLS ENTRY blocks gain a syntactic CLOSED terminator that makes block boundary failure visibly broken in the output | R5-V-05's block rule was stated as "enforced by the format, not by judgment" but the format itself had no visible signal when a block was incomplete — an evaluator had to check whether a REGISTER SLOT preceded the next FLS ENTRY. Adding a named FLS ENTRY [n] CLOSED terminator to each block makes incompleteness syntactically detectable: a new FLS ENTRY that appears before its predecessor's CLOSED marker is a structurally broken output, not merely a skipped step. N/A markers on NO-gap REGISTER SLOTs are unchanged. C-23 and C-24 carried forward from R5-V-05. Hypothesis: 16/16. |
| V-02 | Lifecycle emphasis — C-23 isolation: Phase 0 gate replaced by a named ACTIVATION STATE LOG table in which each mechanism has an explicit row with Status = ACTIVE / ARMED / LOADED | R5-V-05's gate token was a single-sentence run-on: "Chain 1 active: ... Chain 2 active: ... Per-row FLS trigger ACTIVE: ... Mismatch example loaded..." The activation states were present but inline and easy to skim. Replacing the sentence with a structured table — one row per mechanism, Status column requiring ACTIVE/ARMED/LOADED — makes each activation state an independently verifiable entry. An evaluator confirms C-23 by checking the Status column, not by parsing prose. C-22 and C-24 carried forward from R5-V-05. Hypothesis: 16/16. |
| V-03 | Lifecycle emphasis — C-24 isolation: Phase 5 split into Phase 5a (remediation entries) and Phase 5b (Chain 2 self-check close section with row-by-row verification table) | R5-V-05's Phase 5 close was a single line: "Phase 5 complete. [N] gaps remediated. Chain 2 self-check applied: all Discovered In echoes verified verbatim against register." The model was told to apply the self-check before writing that line but the verification itself was not structured. Splitting into Phase 5a and Phase 5b with a mandatory row-by-row table (Register: Discovered In vs Phase 5a echo vs Match?) forces the self-check to produce explicit evidence rather than a bare assertion. The TRACE CLOSE TOKEN at the end of Phase 5b is the structural precondition: absent the token, the trace is visibly open. C-22 and C-23 carried forward from R5-V-05. Hypothesis: 16/16. |
| V-04 | Combined — C-22 + C-23: CLOSED terminator on FLS ENTRY blocks (V-01) + ACTIVATION STATE LOG table in Phase 0 (V-02) | Tests whether the two structural additions compose without interaction effects. The CLOSED terminator addresses format enforcement in Phase 1c; the ACTIVATION STATE LOG addresses execution-state recording in Phase 0. They operate at different phases and on different structural elements. Standard R5-V-05 Phase 5 self-check close carried forward. Hypothesis: 16/16. |
| V-05 | Combined — all three axes + rubric-verbatim C-22/C-23/C-24 language: CLOSED terminator (C-22) + ACTIVATION STATE LOG (C-23) + Phase 5b self-check section (C-24) + rubric-exact language embedded in the structural rules | Maximum specification fidelity: C-22's pass condition language ("co-authorship is a structural property of the format and trigger completeness is provable from the output alone") appears in the FLS ENTRY block rule; C-23's pass condition language ("execution log, not declarative checklist") appears in the ACTIVATION STATE LOG header; C-24's pass condition language ("precondition for closing the trace, not a recommended step") appears in the Phase 5b section header. Three independent structural additions that target the three independent failure modes the new criteria close. Hypothesis: 16/16. |

---

## V-01 — Single-Axis: FLS ENTRY CLOSED Terminator (C-22 Isolation)

**Axis:** Output format — each FLS block gains a named CLOSED terminator, making block boundary failure syntactically visible rather than only declaratively prohibited
**Hypothesis:** R5-V-05 stated the block rule as "enforced by the format, not by judgment" but a model could produce a Gap? = YES cell, skip the REGISTER SLOT, and begin the next FLS ENTRY without any syntactic break — the omission is visible only to an evaluator checking whether a REGISTER SLOT appeared. The CLOSED terminator makes this impossible to overlook: a new FLS ENTRY [n+1] that opens before FLS ENTRY [n] CLOSED is a structurally broken block at a glance. All other R5-V-05 mechanisms (Chain 1/Chain 2, gate token, mismatch example) are preserved exactly.

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
During Phase 1c FLS check, the three-part FLS ENTRY block format is active. Each FLS entry consists of: (1) FLS ENTRY [n] — the field data row; (2) REGISTER SLOT [n] — the gap entry or N/A marker; (3) FLS ENTRY [n] CLOSED — the block terminator. The CLOSED terminator is required before any subsequent FLS ENTRY begins. This is the Chain 1 per-row enforcement point.

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

Template rules: Config change names a specific element. Expected state names a UI location. Verification step is executable by a reviewer unfamiliar with the gap history.

> **PHASE 0 GATE** — Write this exact line before Phase 1 content:
> *"Phase 0 complete. Chain 1 active: discovery → register with Discovered In field set at point of discovery. Chain 2 active: register → Phase 5 verbatim slot-fill, copy-not-write. Per-row FLS trigger ACTIVE: three-part FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED block format engaged for Phase 1c. Remediation template declared: Config change / Expected state / Verification step. Mismatch example loaded for Phase 5 self-check. Advancing to Phase 1."*

---

## LIVE GAPS REGISTER

Opened at Phase 0. Populated inline during Phases 1–4. Chain 1 enforcement point.

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

- **Discovered In**: exact section name and context, set at discovery time — this is the value Chain 2 copies verbatim into Phase 5
- Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY
- Severity: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 — ENTITY AND ROLE MAP

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Default access for unauthenticated user |
|--------|-----------------|----------------------------------------|

Chain 1 check after 1a: Does any OWD create unexpected default access? If yes: add to register (Discovered In: "Phase 1a OWD — [entity]"). If no: "Phase 1a: no OWD anomalies — [basis for determination]."

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

Step 2: FLS check for all PII, Financial, and Audit/Compliance fields. Per-row trigger ACTIVE — use THREE-PART FLS ENTRY BLOCKS.

**Block format — mandatory for every field:**

```
FLS ENTRY [n] — [Entity].[Field]
| Entity | Field | Category | FLS Profile? | CS: Read | CS: Write | Expert: Read | Expert: Write | Gap? |
|--------|-------|----------|-------------|----------|-----------|--------------|---------------|------|
| ...    | ...   | ...      | ...         | ...      | ...       | ...          | ...           | YES/NO |

REGISTER SLOT [n]:
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

```
FLS ENTRY [n] CLOSED
```

**Block boundary rule:** A new FLS ENTRY block may not begin until FLS ENTRY [n] CLOSED appears for the current block. The CLOSED terminator is the structural boundary marker — its absence is a visibly incomplete block, not a procedural skip. A Gap? = YES cell without a REGISTER SLOT and a subsequent CLOSED marker is a broken block detectable by inspection. This constraint is a property of the format: co-authorship between the field data row and the register slot is enforced by the block structure, not by a remembered obligation.

Section close: "Phase 1c FLS complete. [N] FLS ENTRY blocks. [N] CLOSED markers written (must equal [N] blocks). [N] YES entries. [N] N/A register slots. All REGISTER SLOTS complete. All blocks terminated."

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
A blanket "no issues found" without enumeration fails C-12.

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative:**
CRUD + Assign + Record Scope per entity from Phase 1b. Cross-reference with Phase 1c sensitive fields: which PII, Financial, and Audit/Compliance fields can Customer Service read or write? For each sensitive field accessible to CS: is access appropriate to the CS job function, or does it constitute overreach?

**Dataverse Security Expert:**
CRUD + Assign + Record Scope per entity. Every privilege the expert holds that Customer Service does not. Does the expert role follow least-privilege, or does it hold admin-level access that extends beyond configuration scope?

**Contrast statement (required):**
One paragraph explicitly contrasting the two roles. Both "Customer Service" and "Dataverse security expert" must appear by name. State: what Customer Service can do that the expert cannot, and what the expert can do that Customer Service cannot. A contrast section that names one role without the other fails C-07.

Chain 1 check after Phase 4: Any gaps surfaced during role differentiation not yet in the register? Add now (Discovered In: "Phase 4 role differentiation — [role] — [issue]").

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

Every gap gets all three fields. A gap with Expected state missing fails C-13. A gap without a specific, executable Verification step fails C-13.

Phase 5 close: "Phase 5 complete. [N] gaps remediated. Chain 2 self-check applied: all Discovered In echoes verified verbatim against register."

---

## V-02 — Single-Axis: ACTIVATION STATE LOG in Phase 0 (C-23 Isolation)

**Axis:** Lifecycle emphasis — Phase 0 gate replaced by a named ACTIVATION STATE LOG table, giving each pre-declared mechanism an explicit row with Status = ACTIVE / ARMED / LOADED
**Hypothesis:** R5-V-05's gate token packed all activation states into a single sentence. An evaluator checking C-23 had to parse prose to confirm that each mechanism was named as ACTIVE. Replacing the sentence with a structured table makes each mechanism's activation state an independently verifiable table cell. The Status column must carry ACTIVE, ARMED, or LOADED — not vague statements like "declared" or "will be used." The table header explicitly labels the log as an execution record rather than a declaration of intent, directly satisfying C-23's requirement that the gate token "record state (what is active entering Phase 1) not intent (what the model should do)." All other R5-V-05 mechanisms carried forward exactly.

---

You are running a permissions trace signal for: {{topic}}

---

## PHASE 0 — FULL AUDIT CHAIN GATE

**Complete this phase and write the ACTIVATION STATE LOG before Phase 1 content. Phase 1 content may not appear above the logged gate close.**

This trace operates under a bidirectional audit chain. Both directions are pre-established here. Both are active for the remainder of the output.

**Chain 1 — Discovery to register (active during Phases 1–4):**
Every gap found during Phases 1–4 is entered into the LIVE GAPS REGISTER at the moment of discovery. The Discovered In field records the exact section and context — e.g., "Phase 1c FLS check — Contact.AnnualRevenue" or "Phase 3 escalation — Customer Service role". Set at discovery time, not reconstructed from memory.

**Chain 2 — Register to remediation echo (active during Phase 5):**
Every LIVE GAPS REGISTER entry is echoed in Phase 5 using a verbatim slot-fill. The Discovered In value in Phase 5 is copied exactly from the register cell — same section name, same entity, same field. No summarizing, no shortening, no paraphrasing. Chain 2 is a copy operation, not a writing operation.

**Per-row FLS trigger — ACTIVE now:**
During Phase 1c FLS check, the interleaved FLS ENTRY/REGISTER SLOT block format is active. Each FLS entry consists of a table row and a register slot. The register slot must be completed before the next table row begins. This enforces Chain 1 at the per-row level during Phase 1c.

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

Template rules: Config change names a specific element. Expected state names a UI location. Verification step is executable by a reviewer unfamiliar with the gap history.

**PHASE 0 GATE — ACTIVATION STATE LOG:**

This log is an execution record, not a declaration of intent. Each entry confirms that the named mechanism is already active as of Phase 0 close — not that it will be activated when the relevant phase is reached.

| Mechanism | Status | Notes |
|-----------|--------|-------|
| Chain 1 — discovery → register, Discovered In set at point of discovery | ACTIVE | Governs Phases 1–4 register fill |
| Chain 2 — register → Phase 5 verbatim echo, copy-not-write | ACTIVE | Governs Phase 5 slot-fill |
| Per-row FLS trigger — interleaved FLS ENTRY / REGISTER SLOT for Phase 1c | ACTIVE | Block boundary rule enforced per row |
| Remediation template — Config change / Expected state / Verification step | ACTIVE | Pre-declared above; all three fields required per gap |
| Mismatch example — self-check instrument for Chain 2 echo verification | LOADED | Available at Phase 5; required before trace close |

*All mechanisms confirmed ACTIVE or LOADED at Phase 0 close. Entering PHASE 1.*

---

## LIVE GAPS REGISTER

Opened at Phase 0. Populated inline during Phases 1–4. Chain 1 enforcement point.

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

- **Discovered In**: exact section name and context, set at discovery time — this is the value Chain 2 copies verbatim into Phase 5
- Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY
- Severity: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 — ENTITY AND ROLE MAP

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Default access for unauthenticated user |
|--------|-----------------|----------------------------------------|

Chain 1 check after 1a: OWD anomaly? If yes: add to register (Discovered In: "Phase 1a OWD — [entity]"). If no: "Phase 1a: no OWD anomalies — [basis]."

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Team / User / Sharing-[rule name]. All roles with any privilege must appear.

Chain 1 check after 1b: Scope broader than function? If yes: add to register (Discovered In: "Phase 1b operation-role matrix — [role]"). If no: "Phase 1b: no scope anomalies — [basis]."

**1c — Sensitive field categorization:**

Step 1: category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII (name, contact info, ID, government data) | |
| | Financial (billing, pricing, payment, credit) | |
| | Audit/Compliance (modified-by, consent, audit trail) | |
| | Operational (status, queue, SLA, internal notes) | |

Write "none" for empty categories.

Step 2: FLS check using INTERLEAVED ENTRY BLOCKS (per-row trigger ACTIVE from Phase 0 log).

**Entry block structure — apply for every sensitive field:**

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

**Block rule:** A new FLS ENTRY block may not begin until the REGISTER SLOT for the current entry is complete. This rule is enforced by the format, not by judgment.

Section close: "Phase 1c FLS complete. [N] FLS ENTRY blocks. [N] YES entries. [N] register entries written. [N] N/A register slots written. All REGISTER SLOTS complete. Chain 1 per-row trigger: fully applied."

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

Chain 1 check after 1d: For each Conflicts = YES: add to register (Discovered In: "Phase 1d sharing rule — [rule name]"). If none: "Phase 1d: no SHARING-CONFLICT entries — [rules checked, reason]."

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

Mark each hop as INTENTIONAL or EMERGENT. EMERGENT = gap.

Chain 1 check after 2b: Add any CROSS-ENTITY findings (Discovered In: "Phase 2b cross-entity — [role] via [Entity A] → [Entity B]").

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

One subsection per role from Phase 1b. No collective statements.

For each role:

**Role: [name]**

Escalation-capable privileges examined:
- Team membership Write: [YES / NO — evidence]
- Security role assignment Write: [YES / NO — evidence]
- Record ownership Assign scope: [scope — whether reassignment permits elevation]
- Business unit configuration Write: [YES / NO — evidence]

Conclusion: ESCALATION-PATH FOUND / RULED OUT

If FOUND: `[Role] → [action] → [elevated access achieved] — mechanism: [how]`
If RULED OUT: "No path — [specific reason per checked privilege]."

Chain 1 check per role: FOUND → add to register (Discovered In: "Phase 3 escalation — [role name]"). Ruled out = no entry.

Negative-check evidence per gap type: For any gap type with no finding: "Checked [items] for [role list]; [gap type] does not apply because [reason]."

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative:** CRUD + Assign + Record Scope per entity from Phase 1b. Cross-reference with Phase 1c sensitive fields: which PII, Financial, and Audit/Compliance fields accessible? Appropriate or overreach?

**Dataverse Security Expert:** CRUD + Assign + Record Scope per entity. Every privilege the expert holds that Customer Service does not. Least-privilege or admin-level overreach?

**Contrast statement (required):** One paragraph, both role names explicit. What CS can do that the expert cannot; what the expert can do that CS cannot.

Chain 1 check after Phase 4: Any undocumented gaps? Add now (Discovered In: "Phase 4 role differentiation — [role] — [issue]").

---

## PHASE 5 — REMEDIATION

Chain 2 active. For every entry in the LIVE GAPS REGISTER, apply the Remediation Contract from Phase 0.

**Slot-fill instruction — Chain 2:**
Locate the Discovered In cell in the register row for this gap ID. Copy it exactly — same section name, same entity, same field. No shortening or paraphrasing.

**Mismatch example (self-check before closing this phase):**

> Suppose the register contains:
> `| G-02 | Phase 1c FLS check — Contact.AnnualRevenue | MISSING-FLS | Contact | AnnualRevenue | Customer Service | HIGH |`
>
> **PASSING:** `Gap G-02 (Discovered In: Phase 1c FLS check — Contact.AnnualRevenue):`
>
> **FAILING:**
> `Gap G-02 (Discovered In: FLS gap — AnnualRevenue):` ← entity and section label changed
> `Gap G-02 (Discovered In: Phase 1c FLS):` ← field name truncated
> `Gap G-02 (Discovered In: Phase 1 — AnnualRevenue):` ← "FLS check — Contact" compressed out
> `Gap G-02 (Discovered In: Contact field security issue):` ← rephrased
>
> Before writing "Phase 5 complete": compare each Discovered In echo word-for-word against the register cell. Rewrite any that match a FAILING form.

For each register entry:

```
Gap [ID] (Discovered In: [verbatim copy — self-checked against register]):
  Config change:     [exact element — role / field / profile / rule and location]
  Expected state:    [UI view or query after fix]
  Verification step: [executable action — UI location and expected result]
```

Phase 5 close: "Phase 5 complete. [N] gaps remediated. Chain 2 self-check applied: all Discovered In echoes verified verbatim against register."

---

## V-03 — Single-Axis: Phase 5 Split into 5a and 5b (C-24 Isolation)

**Axis:** Lifecycle emphasis — Phase 5 divided into Phase 5a (remediation entries) and Phase 5b (Chain 2 self-check close section with a row-by-row verification table and a required TRACE CLOSE TOKEN)
**Hypothesis:** R5-V-05's Phase 5 instructed the model to self-check and then write "Phase 5 complete. Chain 2 self-check applied: all Discovered In echoes verified verbatim against register." The self-check instruction and the completion marker were collapsed into the same motion: the model was told to check, then declare it checked. The structural close condition existed as a sentence to write but not as a section to produce. Phase 5b separates the self-check into a mandatory evidence-producing section: a row-by-row verification table that shows the register value, the Phase 5a echo, and the Match? result. The TRACE CLOSE TOKEN at the end of Phase 5b is the structural precondition — absent the token, the trace is visibly open. Completing Phase 5b requires producing the table, not just declaring the check was applied. All other R5-V-05 mechanisms carried forward exactly.

---

You are running a permissions trace signal for: {{topic}}

---

## PHASE 0 — FULL AUDIT CHAIN GATE

**Complete this phase and write the gate token. Phase 1 content may not appear above this gate token.**

This trace operates under a bidirectional audit chain. Both directions are pre-established here and remain active for the full output.

**Chain 1 — Discovery to register (active during Phases 1–4):**
Every gap found during Phases 1–4 is entered into the LIVE GAPS REGISTER at the moment of discovery. The Discovered In field records the exact section and context — e.g., "Phase 1c FLS check — Contact.AnnualRevenue". Set at discovery time, not reconstructed.

**Chain 2 — Register to remediation echo (active during Phase 5a):**
Every register entry is echoed in Phase 5a via verbatim slot-fill. The Discovered In value in Phase 5a is copied exactly from the register cell. Chain 2 is verified in Phase 5b before the trace closes.

**Per-row FLS trigger — ACTIVE now:**
During Phase 1c, the interleaved FLS ENTRY/REGISTER SLOT block format is active. Each FLS entry is a table row followed immediately by a register slot. The slot must be completed before the next entry begins.

**Remediation template (pre-declared; applied in Phase 5a to every register entry):**

```
Gap [ID] (Discovered In: [verbatim from register — Chain 2 slot-fill]):
  Config change:     [exact element — role / field / profile / rule and location]
  Expected state:    [what the system shows after fix — name the UI view or query]
  Verification step: [named executable action — UI location and expected result]
```

> **PHASE 0 GATE** — Write this exact line before Phase 1 content:
> *"Phase 0 complete. Chain 1 active: discovery → register with Discovered In field set at point of discovery. Chain 2 active: register → Phase 5a verbatim slot-fill; verified in Phase 5b. Per-row FLS trigger ACTIVE: interleaved block format engaged for Phase 1c. Remediation template declared: Config change / Expected state / Verification step. Mismatch example loaded for Phase 5b self-check. Advancing to Phase 1."*

---

## LIVE GAPS REGISTER

Opened at Phase 0. Populated inline during Phases 1–4.

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

- **Discovered In**: exact section name and context — the value Phase 5b will verify verbatim
- Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY
- Severity: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 — ENTITY AND ROLE MAP

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Default access for unauthenticated user |
|--------|-----------------|----------------------------------------|

Chain 1 check after 1a: OWD anomaly? Register if yes (Discovered In: "Phase 1a OWD — [entity]"). If no: "Phase 1a: no OWD anomalies — [basis]."

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Team / User / Sharing-[rule name]. All roles with any privilege.

Chain 1 check after 1b: Scope broader than function? If yes: register (Discovered In: "Phase 1b operation-role matrix — [role]"). If no: "Phase 1b: no scope anomalies — [basis]."

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

**Entry block format:**

```
FLS ENTRY — [Entity].[Field]
| Entity | Field | Category | FLS Profile? | CS: Read | CS: Write | Expert: Read | Expert: Write | Gap? |
|--------|-------|----------|-------------|----------|-----------|--------------|---------------|------|
| ...    | ...   | ...      | ...         | ...      | ...       | ...          | ...           | YES/NO |

REGISTER SLOT (Chain 1 — complete before next FLS ENTRY):
```

Gap? = YES → register entry immediately. Gap? = NO → "No gap. Register slot: N/A — [brief confirmation]."

**Block rule:** A new FLS ENTRY block may not begin until the REGISTER SLOT for the current entry is complete. This is the Chain 1 per-row enforcement point.

Section close: "Phase 1c FLS complete. [N] FLS ENTRY blocks. [N] YES entries. [N] register entries written. [N] N/A slots. All REGISTER SLOTS complete."

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

Chain 1 check after 1d: Conflicts = YES → register (Discovered In: "Phase 1d sharing rule — [rule name]"). If none: "Phase 1d: no SHARING-CONFLICT entries — [rules checked, reason]."

---

## PHASE 2 — TEAM AND CROSS-ENTITY

**2a — Team membership gap:**

Finding: `[Role] → [adds user to Team X] → [elevated access] — mechanism: [how]`
Rule-out: "Checked [teams]: no injection path — [reason]."

Chain 1 check: TEAM-GAP if found (Discovered In: "Phase 2a team membership — [team]"). If none: "Phase 2a: no TEAM-GAP entries — [basis]."

**2b — Cross-entity permission chain:**

Select highest-sensitivity entity (justify from Phase 1c). Trace at least two hops:

`[Role] → [Entity A, op: X, scope: Y] → [Relationship] → [Entity B, op: X, scope: Y]`

Mark each hop INTENTIONAL or EMERGENT. EMERGENT = gap.

Chain 1 check: CROSS-ENTITY if found (Discovered In: "Phase 2b cross-entity — [role] via [A] → [B]").

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

One subsection per role. No collective statements.

**Role: [name]**

- Team membership Write: [YES / NO — evidence]
- Security role assignment Write: [YES / NO — evidence]
- Record ownership Assign scope: [scope — elevation possible?]
- Business unit configuration Write: [YES / NO — evidence]

Conclusion: ESCALATION-PATH FOUND / RULED OUT

If FOUND: `[Role] → [action] → [elevated access] — mechanism: [how]`
If RULED OUT: "No path — [specific reason per privilege]."

Chain 1 check per role: FOUND → register (Discovered In: "Phase 3 escalation — [role]").

Negative-check evidence: For gap types with no finding: "Checked [items] for [role list]; [type] does not apply because [reason]."

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative:** CRUD + Assign + Record Scope. Sensitive field access: appropriate or overreach?

**Dataverse Security Expert:** CRUD + Assign + Record Scope. Every privilege CS lacks. Least-privilege or overreach?

**Contrast statement (required):** One paragraph, both role names explicit.

Chain 1 check: Undocumented gaps → register (Discovered In: "Phase 4 role differentiation — [role] — [issue]").

---

## PHASE 5a — REMEDIATION ENTRIES

Chain 2 active. For every register entry, apply the Remediation Contract from Phase 0.

**Slot-fill instruction — Chain 2:**
Copy the Discovered In value verbatim from the register cell. Do not shorten or restate.

For each register entry:

```
Gap [ID] (Discovered In: [verbatim copy from register]):
  Config change:     [exact element — role / field / profile / rule and location]
  Expected state:    [UI view or query after fix]
  Verification step: [executable action — UI location and expected result]
```

All three fields required per gap. A gap without Expected state or Verification step fails C-13.

---

## PHASE 5b — CHAIN 2 SELF-CHECK CLOSE

**This section is a structural precondition for closing the trace, not a recommended step. The trace is not closed until the TRACE CLOSE TOKEN at the bottom of this section is written.**

For each remediation entry in Phase 5a, verify that the Discovered In echo matches the register cell verbatim. Complete the self-check table before writing the close token.

**Mismatch example:**
> Register: `Phase 1c FLS check — Contact.AnnualRevenue`
> PASSING echo: `Phase 1c FLS check — Contact.AnnualRevenue` (exact copy)
> FAILING echoes: `FLS gap — AnnualRevenue` / `Phase 1c FLS` / `Phase 1 — AnnualRevenue` / `Contact field security issue`
> If any echo matches a FAILING form: rewrite the Phase 5a entry before completing the table.

**Self-check verification table:**

| Gap ID | Register: Discovered In | Phase 5a Echo: Discovered In | Match? |
|--------|------------------------|------------------------------|--------|

Fill one row per register entry. Match? = YES (exact) or FAIL (rewrote — state new value). A Match? = FAIL row requires the Phase 5a entry to have been corrected before this table is complete.

After completing the table, write the required close token:

**TRACE CLOSE TOKEN:** `Chain 2 self-check applied: all Discovered In echoes verified verbatim against register. Rows in table: [N]. FAIL corrections: [N]. Trace closed.`

The trace is not closed until this token appears. A Phase 5a section followed by no Phase 5b section, or a Phase 5b section without the TRACE CLOSE TOKEN, is an open trace.

---

## V-04 — Combined: FLS ENTRY CLOSED Terminator + ACTIVATION STATE LOG (C-22 + C-23)

**Axis:** Combined — V-01's FLS ENTRY [n] CLOSED terminator (C-22) + V-02's ACTIVATION STATE LOG table in Phase 0 (C-23)
**Hypothesis:** V-01 and V-02 target different phases with no structural overlap: V-01 modifies the Phase 1c FLS block format; V-02 modifies the Phase 0 gate. They are temporally complementary and test the same structural properties at different points — Phase 0 records that each mechanism is ACTIVE before evidence collection; Phase 1c enforces block completeness during evidence collection. Together they close both the gate-declaration gap (C-23) and the format-enforcement gap (C-22) simultaneously. Standard R5-V-05 Phase 5 self-check carried forward for C-24. Hypothesis: 16/16.

---

You are running a permissions trace signal for: {{topic}}

---

## PHASE 0 — FULL AUDIT CHAIN GATE

**Complete this phase and write the ACTIVATION STATE LOG before Phase 1 content.**

This trace operates under a bidirectional audit chain. Both directions are pre-established here.

**Chain 1 — Discovery to register (active during Phases 1–4):**
Every gap found is entered into the LIVE GAPS REGISTER at the moment of discovery. The Discovered In field records the exact section and context. Set at discovery time.

**Chain 2 — Register to remediation echo (active during Phase 5):**
Every register entry is echoed in Phase 5 via verbatim slot-fill. The Discovered In value is copied exactly — not paraphrased, not compressed.

**Per-row FLS trigger — ACTIVE now:**
During Phase 1c, the three-part FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED block format is active. Each block is terminated by a CLOSED marker. A new FLS ENTRY may not begin until the current block's CLOSED marker is written.

**Remediation template (pre-declared; applied in Phase 5 to every register entry):**

```
Gap [ID] (Discovered In: [verbatim from register — Chain 2 slot-fill]):
  Config change:     [exact element and location]
  Expected state:    [UI view or query after fix]
  Verification step: [executable action — UI location and expected result]
```

**PHASE 0 GATE — ACTIVATION STATE LOG:**

This log records execution state at Phase 0 close. Each entry confirms the mechanism is already active, not that it will be activated.

| Mechanism | Status | Activation Point |
|-----------|--------|-----------------|
| Chain 1 — discovery → register, Discovered In set at discovery | ACTIVE | Phase 0 declared above |
| Chain 2 — register → Phase 5 verbatim echo, copy-not-write | ACTIVE | Phase 0 declared above |
| Per-row FLS trigger — FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED blocks | ACTIVE | Engages at Phase 1c first row |
| Remediation template — Config change / Expected state / Verification step | ACTIVE | Pre-declared above; all three fields required |
| Mismatch example — Chain 2 self-check instrument | LOADED | Provided in Phase 5; required before trace close |

*All mechanisms ACTIVE or LOADED at Phase 0 close. Entering PHASE 1.*

---

## LIVE GAPS REGISTER

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

- **Discovered In**: exact section and context, set at discovery time
- Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY
- Severity: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 — ENTITY AND ROLE MAP

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Default access for unauthenticated user |
|--------|-----------------|----------------------------------------|

Chain 1 check after 1a: OWD anomaly → register (Discovered In: "Phase 1a OWD — [entity]"). None → "Phase 1a: no OWD anomalies — [basis]."

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Team / User / Sharing-[rule name]. All roles with any privilege.

Chain 1 check after 1b: Scope anomaly → register (Discovered In: "Phase 1b operation-role matrix — [role]"). None → "Phase 1b: no scope anomalies — [basis]."

**1c — Sensitive field categorization:**

Step 1: category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII | |
| | Financial | |
| | Audit/Compliance | |
| | Operational | |

"none" for empty categories.

Step 2: FLS check using THREE-PART FLS ENTRY BLOCKS (per-row trigger ACTIVE per Phase 0 log).

**Block format — mandatory for every sensitive field:**

```
FLS ENTRY [n] — [Entity].[Field]
| Entity | Field | Category | FLS Profile? | CS: Read | CS: Write | Expert: Read | Expert: Write | Gap? |
|--------|-------|----------|-------------|----------|-----------|--------------|---------------|------|
| ...    | ...   | ...      | ...         | ...      | ...       | ...          | ...           | YES/NO |

REGISTER SLOT [n]:
```

Gap? = YES → register entry immediately before CLOSED marker.
Gap? = NO → "No gap. Register slot: N/A — [brief confirmation]."

```
FLS ENTRY [n] CLOSED
```

**Block boundary rule:** A new FLS ENTRY block may not begin until FLS ENTRY [n] CLOSED appears. The CLOSED terminator is the structural boundary: its absence makes the block visibly broken. Co-authorship is a property of the block structure enforced by the format — not a behavioral obligation.

Section close: "Phase 1c FLS complete. [N] FLS ENTRY blocks. [N] CLOSED markers written. [N] YES entries. [N] N/A register slots. All blocks terminated."

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

Chain 1 check after 1d: Conflicts → register (Discovered In: "Phase 1d sharing rule — [rule name]"). None → "Phase 1d: no SHARING-CONFLICT — [rules checked, reason]."

---

## PHASE 2 — TEAM AND CROSS-ENTITY

**2a — Team membership gap:**

Finding: `[Role] → [adds user to Team X] → [elevated access] — mechanism: [how]`
Rule-out: "Checked [teams]: no injection path — [reason]."

Chain 1 check: TEAM-GAP if found (Discovered In: "Phase 2a team membership — [team]"). None → state explicitly.

**2b — Cross-entity permission chain:**

Select highest-sensitivity entity (justify from Phase 1c). Trace at least two hops:

`[Role] → [Entity A, op: X, scope: Y] → [Relationship] → [Entity B, op: X, scope: Y]`

INTENTIONAL or EMERGENT at each hop. EMERGENT = gap.

Chain 1 check: CROSS-ENTITY if found (Discovered In: "Phase 2b cross-entity — [role] via [A] → [B]").

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

One subsection per role. No collective statements.

**Role: [name]**

- Team membership Write: [YES / NO — evidence]
- Security role assignment Write: [YES / NO — evidence]
- Record ownership Assign scope: [scope — elevation possible?]
- Business unit configuration Write: [YES / NO — evidence]

ESCALATION-PATH FOUND → `[Role] → [action] → [elevated access] — mechanism: [how]`
RULED OUT → "No path — [reason per privilege]."

Chain 1 check: FOUND → register (Discovered In: "Phase 3 escalation — [role]").

Negative-check evidence: "Checked [items] for [role list]; [type] does not apply because [reason]."

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative:** CRUD + Assign + Record Scope. Sensitive field access: appropriate or overreach?

**Dataverse Security Expert:** CRUD + Assign + Record Scope. Every privilege CS lacks. Least-privilege or overreach?

**Contrast statement (required):** One paragraph, both role names explicit.

Chain 1 check: Undocumented gaps → register (Discovered In: "Phase 4 role differentiation — [role] — [issue]").

---

## PHASE 5 — REMEDIATION

Chain 2 active. For every register entry, apply the Remediation Contract.

**Slot-fill instruction — Chain 2:** Copy Discovered In verbatim from the register cell.

**Mismatch example (self-check before closing):**

> Register: `Phase 1c FLS check — Contact.AnnualRevenue`
> PASSING: `Gap G-02 (Discovered In: Phase 1c FLS check — Contact.AnnualRevenue):`
> FAILING: entity dropped / field truncated / section compressed / rephrased
> Before "Phase 5 complete": compare each echo word-for-word. Rewrite any FAILING forms.

```
Gap [ID] (Discovered In: [verbatim copy — self-checked]):
  Config change:     [exact element and location]
  Expected state:    [UI view or query after fix]
  Verification step: [executable action — UI location and expected result]
```

Phase 5 close: "Phase 5 complete. [N] gaps remediated. Chain 2 self-check applied: all Discovered In echoes verified verbatim against register."

---

## V-05 — Combined: All Three + Rubric-Verbatim Language (C-22 + C-23 + C-24)

**Axis:** Combined — V-01's FLS ENTRY [n] CLOSED terminator (C-22) + V-02's ACTIVATION STATE LOG table (C-23) + V-03's Phase 5b self-check section (C-24) + rubric-exact language embedded in each structural element's rule declaration
**Hypothesis:** Each of the three new criteria has a distinguishing phrase that separates the pass condition from the prior criterion's pass condition. C-22: "co-authorship is a structural property of the format and trigger completeness is provable from the output alone." C-23: "execution log, not declarative checklist." C-24: "precondition for closing the trace, not a recommended step." Embedding these exact phrases in the rules that govern each structural element provides the model with the rubric's own test language at the point of production — before the output is generated, not after evaluation. Maximum specification fidelity. Hypothesis: 16/16.

---

You are running a permissions trace signal for: {{topic}}

---

## PHASE 0 — FULL AUDIT CHAIN GATE

**Complete this phase and write the ACTIVATION STATE LOG before Phase 1 content.**

This trace operates under a bidirectional audit chain. Both directions are pre-established here and remain active for the full output.

**Chain 1 — Discovery to register (active during Phases 1–4):**
Every gap found during Phases 1–4 is entered into the LIVE GAPS REGISTER at the moment of discovery. The Discovered In field records the exact section and context — e.g., "Phase 1c FLS check — Contact.AnnualRevenue". Set at discovery time, not reconstructed.

**Chain 2 — Register to remediation echo (active during Phase 5a):**
Every register entry is echoed in Phase 5a via verbatim slot-fill. The Discovered In value in Phase 5a is copied exactly from the register cell. Chain 2 is verified in Phase 5b — that verification is a **precondition for closing the trace, not a recommended step**.

**Per-row FLS trigger — ACTIVE now:**
During Phase 1c, the three-part FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED block format is active. The CLOSED terminator is required before any subsequent FLS ENTRY begins. This makes **co-authorship a structural property of the format**: a Gap? = YES cell without a completed REGISTER SLOT and a CLOSED marker is a broken block detectable by inspection, not merely a procedural skip. N/A markers on NO-gap REGISTER SLOTs prove the trigger ran for every row, making **trigger completeness provable from the output alone**.

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

This log is an **execution record, not a declarative checklist**. Each entry records that the named mechanism is already active as of Phase 0 close — not that it will be activated when the relevant phase is reached. The mismatch example must appear as LOADED to confirm it is in working context at Phase 0, not merely declared in a Phase 5b instruction that may be reached later.

| Mechanism | Status | Notes |
|-----------|--------|-------|
| Chain 1 — discovery → register, Discovered In set at point of discovery | ACTIVE | Governs all register entries in Phases 1–4 |
| Chain 2 — register → Phase 5a verbatim echo, copy-not-write | ACTIVE | Verified in Phase 5b (structural precondition) |
| Per-row FLS trigger — FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED | ACTIVE | Structural format enforces co-authorship; CLOSED terminator required |
| Remediation template — Config change / Expected state / Verification step | ACTIVE | All three fields required; vague advice ("review permissions") fails Config change |
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

| Entity | Org-Wide Default | Default access for unauthenticated user |
|--------|-----------------|----------------------------------------|

Chain 1 check after 1a: OWD anomaly → register (Discovered In: "Phase 1a OWD — [entity]"). None → "Phase 1a: no OWD anomalies — [basis for determination]."

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Team / User / Sharing-[rule name]. All roles with any privilege on any entity must appear.

Chain 1 check after 1b: Scope broader than function → register (Discovered In: "Phase 1b operation-role matrix — [role]"). None → "Phase 1b: no scope anomalies — [basis]."

**1c — Sensitive field categorization:**

Step 1: categorize all fields before checking FLS:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII (name, contact info, ID, government data) | |
| | Financial (billing, pricing, payment, credit) | |
| | Audit/Compliance (modified-by, consent, audit trail) | |
| | Operational (status, queue, SLA, internal notes) | |

"none" for empty categories.

Step 2: FLS check for all PII, Financial, and Audit/Compliance fields. Per-row trigger ACTIVE per Phase 0 log — use THREE-PART FLS ENTRY BLOCKS.

**Block format — mandatory for every sensitive field:**

```
FLS ENTRY [n] — [Entity].[Field]
| Entity | Field | Category | FLS Profile? | CS: Read | CS: Write | Expert: Read | Expert: Write | Gap? |
|--------|-------|----------|-------------|----------|-----------|--------------|---------------|------|
| ...    | ...   | ...      | ...         | ...      | ...       | ...          | ...           | YES/NO |

REGISTER SLOT [n] (Chain 1 — complete before CLOSED marker):
```

If Gap? = YES:
```
| [G-NN] | Phase 1c FLS check — [Entity].[Field] | MISSING-FLS | [Entity] | [Field] | [Role] | [Severity] |
→ Added to LIVE GAPS REGISTER.
```

If Gap? = NO:
```
→ No gap. Register slot: N/A — [brief confirmation: e.g., "FLS profile restricts CS to Read-only on Financial field; no gap"].
```

```
FLS ENTRY [n] CLOSED
```

**Block boundary rule:** A new FLS ENTRY block may not begin until FLS ENTRY [n] CLOSED appears. The CLOSED terminator is the structural boundary marker. Its absence is a visibly broken block. **Co-authorship is a structural property of the format, not a behavioral obligation** — the block structure makes omission impossible to overlook. N/A markers on NO-gap REGISTER SLOTs prove the per-row trigger ran for every field, making **trigger completeness provable from the output alone** without relying on section-close counts.

Section close: "Phase 1c FLS complete. [N] FLS ENTRY blocks. [N] CLOSED markers written (must equal [N]). [N] YES entries. [N] N/A register slots (must equal [N] — NO-gap rows). All blocks terminated. Trigger completeness: verified by CLOSED marker count and N/A slot count."

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

Chain 1 check after 1d: Conflicts = YES → register (Discovered In: "Phase 1d sharing rule — [rule name]"). None → "Phase 1d: no SHARING-CONFLICT — [rules checked, specific reason]."

---

## PHASE 2 — TEAM AND CROSS-ENTITY

**2a — Team membership gap:**

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
If RULED OUT: "No path — [specific reason per privilege: why it does not permit elevation for this role]."

Chain 1 check per role: FOUND → register (Discovered In: "Phase 3 escalation — [role name]").

**Negative-check evidence per gap type:** For any gap type with no finding: "Checked [specific items] for [role list]; [type] does not apply because [specific reason]."

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative:**
CRUD + Assign + Record Scope per entity. Cross-reference Phase 1c sensitive fields: PII, Financial, Audit/Compliance fields accessible to CS — appropriate or overreach?

**Dataverse Security Expert:**
CRUD + Assign + Record Scope per entity. Every privilege the expert holds that Customer Service does not. Least-privilege or admin-level overreach?

**Contrast statement (required):**
One paragraph, both "Customer Service" and "Dataverse security expert" appear by name. What CS can do that the expert cannot; what the expert can do that CS cannot.

Chain 1 check: Undocumented gaps → register (Discovered In: "Phase 4 role differentiation — [role] — [issue]").

---

## PHASE 5a — REMEDIATION ENTRIES

Chain 2 active. For every register entry, apply the Remediation Contract from Phase 0.

**Slot-fill instruction — Chain 2:**
Copy the Discovered In cell from the register row for this gap ID exactly as it appears. This is a copy operation, not a writing operation. No shortening, no paraphrasing.

For each register entry:

```
Gap [ID] (Discovered In: [verbatim copy from register — Chain 2 slot-fill]):
  Config change:     [exact configuration element — role name / field name / profile name /
                      rule name, and where to find it in the solution]
  Expected state:    [what you will see after applying the change — name the UI view or
                      test query that will differ]
  Verification step: [the action to confirm the fix — name the UI location and expected
                      result, e.g., "Open Security > Field Security Profiles > [profile] >
                      [entity] > [field]: verify [role] shows Read-only"]
```

All three fields required. Missing Expected state or Verification step fails C-13.

---

## PHASE 5b — CHAIN 2 SELF-CHECK CLOSE

**This section is a precondition for closing the trace, not a recommended step. The trace is not closed until the TRACE CLOSE TOKEN at the bottom of this section is written. A Phase 5a section not followed by a completed Phase 5b section is an open trace.**

The mismatch example was loaded at Phase 0. Apply it now.

**Mismatch example:**

> Register: `| G-02 | Phase 1c FLS check — Contact.AnnualRevenue | MISSING-FLS | ... |`
>
> **PASSING echo:** `Gap G-02 (Discovered In: Phase 1c FLS check — Contact.AnnualRevenue):` — exact copy
>
> **FAILING echoes — any of these is a Chain 2 failure:**
> `Gap G-02 (Discovered In: FLS gap — AnnualRevenue):` ← entity and section label changed
> `Gap G-02 (Discovered In: Phase 1c FLS):` ← field name truncated
> `Gap G-02 (Discovered In: Phase 1 — AnnualRevenue):` ← "FLS check — Contact" compressed
> `Gap G-02 (Discovered In: Contact field security issue):` ← entirely rephrased
>
> Cross-check: if any Phase 5a echo looks like any FAILING form above — even partially — rewrite it before completing the table below.

**Self-check verification table:**

| Gap ID | Register: Discovered In (exact text) | Phase 5a Echo: Discovered In (exact text) | Match? |
|--------|--------------------------------------|-------------------------------------------|--------|

Fill one row per register entry. Match? = YES (verbatim) or FAIL + corrected. A FAIL row means the Phase 5a entry was rewritten before this table was completed.

**TRACE CLOSE TOKEN (required before trace closes):**

`Chain 2 self-check applied: all Discovered In echoes verified verbatim against register. Rows verified: [N]. FAIL corrections: [N]. Trace closed.`

This token must be written to close the trace. Its absence means Phase 5b is incomplete and the trace is open.
