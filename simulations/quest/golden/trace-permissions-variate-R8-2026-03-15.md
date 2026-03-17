# trace-permissions Variate — Round 8
**Date:** 2026-03-15
**Rubric:** v7 (C-01 through C-25 — C-24/C-25 added from R7 excellence signals)
**Target criteria:** C-24 (Step 1 close token as chain anchor — named token emission at Step 1 close + downstream annotation count declared at Phase 1c section close, enabling non-vacuous numerical comparison in gate row 5), C-25 (per-stage chain-reminder annotation at consumption points — each FLS ENTRY block and Gap Register section opens with `[Category chain: active — inherit from Step 1]`)

**Baseline:** R7-V-05 achieved all three new criteria from Round 6 (C-21 anti-speculation preamble, C-22 I-6 category drift threat with CATEGORY-DRIFT-VIOLATION marker, C-23 chain-verifier gate row 5 with token-swap check). The two new criteria open the next layer. C-24 requires the token compared in gate row 5 to be a *named, structured artifact emitted at Step 1 close* — not a number embedded in prose. Without a recorded source anchor, the gate row's numerical comparison is unverifiable. C-25 requires the propagation contract to be re-stated at every FLS ENTRY block and Gap Register consumption point — not declared once at Step 2 start and implied thereafter.

**State entering Round 8:**

| Variation | R7-V-05 gap for C-24 | R7-V-05 gap for C-25 |
|-----------|---------------------|---------------------|
| R7-V-05 (best) | Step 1 close embeds token as prose sentence; Phase 1c section close does not separately declare downstream annotation count as a named value — the token-swap in gate row 5 compares a prose-embedded number against the section close count but no named source artifact exists | `[Category chain: active]` appears once at Step 2 start only; no per-FLS-ENTRY-block opening annotation; no Gap Register chain-reminder at section open |

Path to 180/180: (a) name the Step 1 close token as a formally emitted artifact (`STEP-1-CLOSE-TOKEN`); (b) have Phase 1c section close separately declare the downstream annotation count as a named value; (c) gate row 5 cites both named values for a non-vacuous comparison; (d) every FLS ENTRY block opens with `[Category chain: active — inherit from Step 1]`; (e) LIVE GAPS REGISTER section header carries the same chain-reminder.

---

## Round 8 Variation Map

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | Single-axis: C-24 isolation — Step 1 close emits `STEP-1-CLOSE-TOKEN` as a named structural artifact; Phase 1c section close separately declares downstream annotation count | R7-V-05's Step 1 close embeds "Step 1 token = [M]" in a prose sentence. The token exists but is not a named protocol artifact; the section close does not separately declare the downstream count as a distinct named value. C-24 requires the source anchor to be recorded as a named token at Step 1 close, and the section close to announce the annotation count — making the gate row 5 comparison between two explicitly named, separately declared values. V-01 adds STEP-1-CLOSE-TOKEN to Phase 0 ACTIVATION STATE LOG as PENDING; Step 1 close emits the token in structured format; Phase 1c section close declares downstream count separately. No per-FLS-ENTRY chain-reminder (C-25 not targeted). |
| V-02 | Single-axis: C-25 isolation — every FLS ENTRY block opens with `[Category chain: active — inherit from Step 1]`; LIVE GAPS REGISTER section carries the chain-reminder at header | R7-V-05 has one `[Category chain: active]` line at Step 2 start. C-25 requires the reminder to appear at each consumption point — each FLS ENTRY block open and each Gap Register section open. The distinction is proactive constraint visibility at consumption sites vs single-point declaration. V-02 moves the annotation from Step 2 preamble into the FLS ENTRY block format as a required first line, and adds a chain-reminder note to the LIVE GAPS REGISTER header. No STEP-1-CLOSE-TOKEN change (C-24 not targeted). |
| V-03 | Combined: C-24 + C-25 — STEP-1-CLOSE-TOKEN at Step 1 close + Phase 1c section-close downstream annotation count + per-FLS-ENTRY-block and Gap Register chain-reminders | V-01 establishes C-24; V-02 establishes C-25. V-03 combines both on the R7-V-05 base (which already holds C-21 + C-22 + C-23). The mechanisms operate at different output positions with no structural conflict: C-24 affects Step 1 close and Phase 1c section close; C-25 affects FLS ENTRY block headers and the Gap Register section header. Hypothesis: 180/180. |
| V-04 | Combined variant: C-24 + C-25 hoisted to Phase 0 ACTIVATION STATE LOG as pre-declared protocol mechanisms, both PENDING until Phase 1c activates them | V-03 introduces both mechanisms at their point of use. V-04 hoists both to Phase 0 — the ACTIVATION STATE LOG pre-declares `STEP-1-CLOSE-TOKEN (C-24 chain anchor)` as PENDING and `Per-stage chain-reminder (C-25 consumption-point annotation)` as PENDING, each with explicit activation notes. This makes the protocol reviewable from Phase 0 before Phase 1 begins, and makes failure to fire the token or reminder a visibly broken state (PENDING → ACTIVE transition never recorded). Tests whether Phase 0 pre-declaration strengthens C-24 and C-25 pass conditions or whether point-of-use declaration (V-03) is sufficient. |
| V-05 | Combined + rubric-verbatim language: V-03 structure + rubric-exact phrases at each C-24 and C-25 enforcement point | Maximum specification fidelity. C-24 phrases: "named close token recording the exact count of items analyzed" at Step 1 close instruction; "announce the downstream annotation count" at Phase 1c section close instruction; "non-vacuous numerical comparison" in gate row 5. C-25 phrases: "`[Category chain: active — inherit from Step N]` exact form required" at each FLS ENTRY block format line; "consumption point — chain-reminder required at block open" in block boundary rule; "converts the propagation contract from a single-point declaration to a continuously-visible constraint" in PR-1. Tests whether rubric-exact pass-condition language in the prompt reliably produces rubric-satisfying structure in the output. |

---

## V-01 — Single-Axis: Named STEP-1-CLOSE-TOKEN as Chain Anchor (C-24 Isolation)

**Axis:** Output format — Phase 1c Step 1 emits `STEP-1-CLOSE-TOKEN` as a named, structured protocol artifact (not a number embedded in prose); Phase 1c section close separately declares the downstream FLS ENTRY Category annotation count as a named value; gate row 5 cites both named values for a non-vacuous numerical comparison
**Hypothesis:** R7-V-05's Step 1 close reads: "Step 1 token = [M]. The submission gate chain-verifier row will check this value against the downstream FLS ENTRY Category annotation count." The token value exists, but it is embedded in a prose sentence — not a named artifact. The Phase 1c section close states the annotation count but does not separately declare it as a named value alongside the token. C-24 requires the source anchor to be a named close token recorded at Step 1 close, and the section close to announce the downstream annotation count independently, so that the gate row 5 comparison is between two explicitly named, separately declared values rather than two numbers found by reading sentences. V-01 isolates this change: the rest of V-05 is preserved exactly.

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
During Phase 1c, the three-part FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED block format is active. The CLOSED terminator is required before any subsequent FLS ENTRY begins. **Co-authorship is a structural property of the format**: a Gap? = YES cell without a completed REGISTER SLOT and a CLOSED marker is a broken block detectable by inspection. N/A markers on NO-gap REGISTER SLOTs make **trigger completeness provable from the output alone**.

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
| I-6 category drift / PR-1 — CATEGORY-DRIFT-VIOLATION marker (carries its own identifier and fires on re-derivation) | ACTIVE | Fires during Phase 1c Step 2 on any re-derivation of Step 1 category labels |
| STEP-1-CLOSE-TOKEN — named chain anchor emitted at Phase 1c Step 1 close | PENDING | Set at Phase 1c Step 1 close with exact FLS-scope field count; consumed by Phase 1c section close and gate row 5; token not set = broken chain anchor |

*All mechanisms confirmed ACTIVE or LOADED at Phase 0 close. STEP-1-CLOSE-TOKEN PENDING — will be set at Phase 1c Step 1 close. Entering PHASE 1.*

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

**Step 1 close — STEP-1-CLOSE-TOKEN (required by Phase 0 ACTIVATION STATE LOG; gate row 5 reads this named value):**

```
STEP-1-CLOSE-TOKEN
  Category table total rows analyzed: [N]
  FLS-scope rows (PII + Financial + Audit/Compliance): [M]
  Chain anchor value: [M]
```

This token is the source anchor for the chain-verifier gate row 5. The Phase 1c section close will independently declare the downstream FLS ENTRY Category annotation count. Gate row 5 performs a numerical comparison of STEP-1-CLOSE-TOKEN chain anchor value [M] against that separately declared count. A gate row that compares against a count never named here = non-vacuous comparison failed.

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

**Block boundary rule:** A new FLS ENTRY block may not begin until FLS ENTRY [n] CLOSED appears. **Co-authorship is a structural property of the format**: the block structure makes omission impossible to overlook. N/A markers prove trigger completeness from the output alone. Category value in each block must match Step 1 table — PR-1 active; re-derivation fires CATEGORY-DRIFT-VIOLATION (I-6).

Section close:

```
Phase 1c FLS complete.
  FLS ENTRY blocks: [N]
  CLOSED markers written: [N] (must equal [N])
  YES entries: [N]
  N/A register slots: [N] (must equal NO-gap rows)
  Downstream FLS ENTRY Category annotation count: [M]
  (This count is declared here for gate row 5 token-swap. Must equal STEP-1-CLOSE-TOKEN chain anchor value [M].)
  Category chain: all [M] FLS ENTRY Category values inherited from Step 1 / [k] CATEGORY-DRIFT-VIOLATION entries
```

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
If RULED OUT: "No path — [specific reason per privilege]."

Chain 1 check per role: FOUND → register (Discovered In: "Phase 3 escalation — [role name]").

**Negative-check evidence per gap type:** For any gap type with no finding: "Checked [specific items] for [role list]; [type] does not apply because [specific reason]."

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative:**
CRUD + Assign + Record Scope per entity from Phase 1b. Cross-reference Phase 1c Step 1 sensitive fields: PII, Financial, and Audit/Compliance fields accessible to CS — appropriate or overreach?

**Dataverse Security Expert:**
CRUD + Assign + Record Scope per entity. Every privilege the expert holds that Customer Service does not. Least-privilege or admin-level overreach?

**Contrast statement (required):**
One paragraph, both "Customer Service" and "Dataverse security expert" appear by name.

Chain 1 check: Undocumented gaps → register (Discovered In: "Phase 4 role differentiation — [role] — [issue]").

---

## PHASE 5a — REMEDIATION ENTRIES

Chain 2 active. For every register entry, apply the Remediation Contract from Phase 0.

**Slot-fill instruction — Chain 2:** Copy the Discovered In cell from the register row for this gap ID exactly as it appears — copy operation, not writing operation.

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
> `Gap G-02 (Discovered In: Contact field security issue):` ← entirely rephrased
>
> Before completing the table: compare each echo word-for-word. Rewrite any FAILING forms.

**Self-check verification table:**

| Gap ID | Register: Discovered In (exact text) | Phase 5a Echo: Discovered In (exact text) | Match? |
|--------|--------------------------------------|-------------------------------------------|--------|

Fill one row per register entry. Match? = YES (verbatim) or FAIL + corrected.

**TRACE CLOSE TOKEN:** `Chain 2 self-check applied: all Discovered In echoes verified verbatim against register. Rows verified: [N]. FAIL corrections: [N]. Trace closed.`

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
| 5 | **End-to-end chain verification including non-vacuous token-swap**: (a) STEP-1-CLOSE-TOKEN chain anchor value = [M] (from Phase 1c Step 1 close — named artifact); (b) downstream FLS ENTRY Category annotation count = [M] (from Phase 1c section close — separately declared value); (c) token-swap: STEP-1-CLOSE-TOKEN [M] == section-close annotation count [M]? YES/NO; (d) PR-1 propagation: all [M] FLS ENTRY blocks carry inherited Category values — no CATEGORY-DRIFT-VIOLATION; (e) evidence citations for rows 1–4: all PASS cited. This row passes only when all five sub-checks pass simultaneously. | Cite STEP-1-CLOSE-TOKEN value, Phase 1c section-close downstream annotation count declaration, and rows 1–4 evidence citations | PASS / VERDICT-FAIL |

Gate passes only when all five rows read PASS with evidence cited. Row 5 is a jointly enforced chain-verifier row: a gate that compares against a count never named in STEP-1-CLOSE-TOKEN format = non-vacuous comparison failed; C-24 not satisfied.

---

## V-02 — Single-Axis: Per-Stage Chain-Reminder at Consumption Points (C-25 Isolation)

**Axis:** Lifecycle emphasis — every FLS ENTRY block opens with `[Category chain: active — inherit from Step 1]` as its first visible line, before the table row; the LIVE GAPS REGISTER section header carries a chain-reminder note; the reminder appears at each consumption point, not once at Step 2 start and never again
**Hypothesis:** R7-V-05 writes `[Category chain: active — inherit from Step 1 table. PR-1 in effect.]` once at the start of Step 2. C-25's pass condition requires the reminder to appear at each Phase or compound block that *consumes* category labels — each FLS ENTRY block open and each Gap Register opening. The distinction is proactive constraint visibility at consumption sites vs single-point declaration. A model that sees the PR-1 contract once at Step 2 start may not carry it forward into each block. A model that sees the reminder at every FLS ENTRY block open has no opportunity to treat it as already discharged. V-02 isolates this: the Step 1 close format and Phase 1c section close are unchanged from R7-V-05 (STEP-1-CLOSE-TOKEN not added, C-24 not targeted).

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
During Phase 1c, the three-part FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED block format is active. The CLOSED terminator is required before any subsequent FLS ENTRY begins. **Co-authorship is a structural property of the format**: a Gap? = YES cell without a completed REGISTER SLOT and a CLOSED marker is a broken block detectable by inspection. N/A markers on NO-gap REGISTER SLOTs make **trigger completeness provable from the output alone**.

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

This log is an **execution record, not a declarative checklist**.

| Mechanism | Status | Notes |
|-----------|--------|-------|
| Chain 1 — discovery → register, Discovered In set at point of discovery | ACTIVE | Governs all register entries in Phases 1–4 |
| Chain 2 — register → Phase 5a verbatim echo, copy-not-write | ACTIVE | Verified in Phase 5b (structural precondition) |
| Per-row FLS trigger — FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED | ACTIVE | Structural format enforces co-authorship; CLOSED terminator required |
| Remediation template — Config change / Expected state / Verification step | ACTIVE | All three fields required; vague advice fails Config change |
| Mismatch example — Phase 5b self-check instrument | LOADED | Present in working context; Phase 5b self-check is a precondition for trace close |
| I-6 category drift / PR-1 — CATEGORY-DRIFT-VIOLATION marker (carries its own identifier and fires on re-derivation) | ACTIVE | Fires during Phase 1c Step 2 on any re-derivation of Step 1 category labels |
| Per-stage chain-reminder — `[Category chain: active — inherit from Step 1]` at each FLS ENTRY block open and Gap Register open | ACTIVE | Fires at each consumption point; absence at any block open is a broken reminder — not a deferred one |

*All mechanisms confirmed ACTIVE or LOADED at Phase 0 close. Entering PHASE 1.*

---

## LIVE GAPS REGISTER

Opened at Phase 0. Populated inline during Phases 1–4. Chain 1 enforcement point.

**[Category chain: active — inherit from Step 1 for all category-related findings in this register]**

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

Chain 1 check after 1a: OWD anomaly → register. None → "Phase 1a: no OWD anomalies — [basis]."

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Team / User / Sharing-[rule name]. All roles with any privilege. Dataverse system names required.

Chain 1 check after 1b: Scope anomaly → register. None → "Phase 1b: no scope anomalies — [basis]."

**1c — Sensitive field categorization:**

**Inertia threat inventory (declared before Step 1 — each threat carries its own identifier and a marker that fires on re-derivation or violation):**

| ID | Threat | Fires During | Marker |
|----|--------|-------------|--------|
| I-1 | OWD defaults creating unexpected default access | Phase 1a | ESCALATION-PATH (OWD scope) in register |
| I-2 | Missing FLS profiles on PII, Financial, or Audit/Compliance fields | Phase 1c FLS check | MISSING-FLS in register |
| I-3 | Sharing rule overrides granting unintended access | Phase 1d | SHARING-CONFLICT in register |
| I-4 | Team membership control enabling privilege injection | Phase 2a | TEAM-GAP in register |
| I-5 | EMERGENT cross-entity hops | Phase 2b | CROSS-ENTITY in register |
| I-6 | **Category drift** — inline re-derivation of PII / Financial / Audit/Compliance / Operational labels downstream of Phase 1c Step 1; this threat **carries its own identifier (I-6) and a marker that fires on re-derivation** | Phase 1c Step 2 onward | CATEGORY-DRIFT-VIOLATION in register |

**PR-1: Category propagation contract (established here; active from Step 2 forward):**
The Category column in every FLS ENTRY block must inherit its value from the Step 1 category table below — not re-derived inline. Any FLS ENTRY block where the Category value differs from the Step 1 table fires I-6 with marker CATEGORY-DRIFT-VIOLATION and a register entry. The chain-reminder annotation `[Category chain: active — inherit from Step 1]` must appear at the open of every FLS ENTRY block — this is the per-stage visibility requirement for the propagation contract. A single announcement at Step 2 start does not satisfy this requirement; the reminder must appear at each consumption point.

Step 1: category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII (name, contact info, ID, government data) | |
| | Financial (billing, pricing, payment, credit) | |
| | Audit/Compliance (modified-by, consent, audit trail) | |
| | Operational (status, queue, SLA, internal notes) | |

Write "none" for empty categories.

**Step 1 close:** "Phase 1c Step 1 complete. Category table rows: [N total]. FLS-scope rows (PII + Financial + Audit/Compliance): [M]. Step 1 token = [M]. Submission gate row 5 chain-verifier will compare this token against the downstream FLS ENTRY Category annotation count."

Step 2: FLS check for all PII, Financial, and Audit/Compliance fields. Per-row trigger ACTIVE per Phase 0 log.

**Block format — mandatory for every sensitive field:**

Every FLS ENTRY block must open with the chain-reminder annotation before the table row. The reminder is a per-block requirement, not a once-per-section prefix:

```
[Category chain: active — inherit from Step 1]
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

**Block boundary rule:** A new FLS ENTRY block may not begin until FLS ENTRY [n] CLOSED appears. Every block must begin with `[Category chain: active — inherit from Step 1]` — this annotation is the consumption-point reminder; its absence at any block open is a C-25 violation regardless of whether the Step 2 preamble announced the contract. Category value in each block must match Step 1 table — PR-1 active; re-derivation fires CATEGORY-DRIFT-VIOLATION (I-6).

Section close: "Phase 1c FLS complete. [N] FLS ENTRY blocks. [N] CLOSED markers written (must equal [N]). [N] YES entries. [N] N/A register slots. [N] chain-reminder annotations at block opens (must equal [N]). FLS ENTRY Category annotation count: [M] (must equal Step 1 token [M]). Category chain: all [M] inherited from Step 1 / [k] CATEGORY-DRIFT-VIOLATION entries."

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

Chain 1 check after 1d: Conflicts = YES → register. None → "Phase 1d: no SHARING-CONFLICT — [rules checked, reason]."

---

## PHASE 2 — TEAM AND CROSS-ENTITY

**2a — Team membership gap:**

For each team-scoped role: who controls team membership, and can that control reach elevated access?

Finding: `[Role] → [adds user to Team X] → [elevated access via team] — mechanism: [how]`
Rule-out: "Checked [teams]: no injection path — [reason]."

Chain 1 check: TEAM-GAP if found. None → "Phase 2a: no TEAM-GAP — [teams checked, basis]."

**2b — Cross-entity permission chain:**

Select highest-sensitivity entity (justify from Phase 1c Step 1 categories). Trace at least two hops:

`[Role] → [Entity A, op: X, scope: Y] → [Relationship: lookup/child/N:N] → [Entity B, op: X, scope: Y]`

INTENTIONAL or EMERGENT at each hop. EMERGENT = gap.

Chain 1 check: CROSS-ENTITY if found.

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

One subsection per role from Phase 1b. No collective statements.

**Role: [name]**

Escalation-capable privileges examined:
- Team membership Write: [YES / NO — evidence]
- Security role assignment Write: [YES / NO — evidence]
- Record ownership Assign scope: [scope — elevation?]
- Business unit configuration Write: [YES / NO — evidence]

Conclusion: ESCALATION-PATH FOUND / RULED OUT

If FOUND: `[Role] → [action] → [elevated access] — mechanism: [how]`
If RULED OUT: "No path — [specific reason per privilege]."

Chain 1 check per role: FOUND → register (Discovered In: "Phase 3 escalation — [role name]").

**Negative-check evidence per gap type:** For any gap type with no finding: "Checked [specific items] for [role list]; [type] does not apply because [specific reason]."

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative:**
CRUD + Assign + Record Scope per entity. Cross-reference Phase 1c Step 1 sensitive fields: PII, Financial, and Audit/Compliance fields accessible to CS — appropriate or overreach?

**Dataverse Security Expert:**
CRUD + Assign + Record Scope per entity. Every privilege the expert holds that Customer Service does not. Least-privilege or admin-level overreach?

**Contrast statement (required):**
One paragraph, both "Customer Service" and "Dataverse security expert" appear by name.

Chain 1 check: Undocumented gaps → register (Discovered In: "Phase 4 role differentiation — [role] — [issue]").

---

## PHASE 5a — REMEDIATION ENTRIES

Chain 2 active. For every register entry, apply the Remediation Contract from Phase 0.

**Slot-fill instruction — Chain 2:** Copy the Discovered In cell from the register row for this gap ID exactly as it appears — copy operation, not writing operation.

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

**This section is a precondition for closing the trace, not a recommended step.**

The mismatch example was loaded at Phase 0. Apply it now.

**Mismatch example:**

> Register: `| G-02 | Phase 1c FLS check — Contact.AnnualRevenue | MISSING-FLS | ... |`
>
> **PASSING echo:** `Gap G-02 (Discovered In: Phase 1c FLS check — Contact.AnnualRevenue):`
>
> **FAILING echoes:**
> `Gap G-02 (Discovered In: FLS gap — AnnualRevenue):` ← entity and section label changed
> `Gap G-02 (Discovered In: Phase 1c FLS):` ← field name truncated
> `Gap G-02 (Discovered In: Contact field security issue):` ← rephrased
>
> Before completing the table: compare each echo word-for-word. Rewrite any FAILING forms.

**Self-check verification table:**

| Gap ID | Register: Discovered In (exact text) | Phase 5a Echo: Discovered In (exact text) | Match? |
|--------|--------------------------------------|-------------------------------------------|--------|

Fill one row per register entry. Match? = YES (verbatim) or FAIL + corrected.

**TRACE CLOSE TOKEN:** `Chain 2 self-check applied: all Discovered In echoes verified verbatim against register. Rows verified: [N]. FAIL corrections: [N]. Trace closed.`

---

## SUBMISSION GATE

**ANTI-SPECULATION MANDATE — the named violation type (VERDICT-FAIL) is a protocol-level statement before the table header, not only a cell or row annotation inside it:**

No gate row may record PASS without citing specific evidence from this trace output — a named section, row count, token value, or finding. VERDICT-FAIL is a distinct named violation type that applies at gate review time. This declaration governs all five rows and must be read before any row in the table.

| Row | Check | Evidence Cited | Status |
|-----|-------|----------------|--------|
| 1 | All entities in Phase 1a with OWD and scope stated | Cite Phase 1a row count and scope values | PASS / VERDICT-FAIL |
| 2 | All roles named by Dataverse system name; record scope per entity | Cite Phase 1b role names and Record Scope column | PASS / VERDICT-FAIL |
| 3 | FLS analyzed for all sensitive fields; all CLOSED markers written; chain-reminder annotation at each FLS ENTRY block open counted in section close | Cite Phase 1c close: N blocks, N CLOSED, N chain-reminder annotations | PASS / VERDICT-FAIL |
| 4 | All gap types checked with evidence; negative-check evidence for zero-finding types | Cite Phase 3 statements and Phase 2 rule-outs | PASS / VERDICT-FAIL |
| 5 | **End-to-end chain verification with token-swap check**: (a) Step 1 FLS-scope token = [M] (from Phase 1c Step 1 close); (b) FLS ENTRY Category annotation count = [M] (from Phase 1c section close); (c) token-swap: [M] == [M]? YES/NO; (d) PR-1 propagation: all [M] FLS ENTRY blocks carry inherited Category values — no CATEGORY-DRIFT-VIOLATION; (e) evidence citations rows 1–4: all PASS cited. Row 5 passes only when all five sub-checks pass simultaneously. | Cite Step 1 token, Phase 1c section-close annotation count, and rows 1–4 evidence | PASS / VERDICT-FAIL |

---

## V-03 — Combined: Named Chain Anchor + Per-Stage Consumption-Point Reminders (C-24 + C-25)

**Axis:** Output format + Lifecycle emphasis — STEP-1-CLOSE-TOKEN as named structured artifact at Phase 1c Step 1 close (C-24) combined with `[Category chain: active — inherit from Step 1]` annotation at the open of every FLS ENTRY block and Gap Register section (C-25)
**Hypothesis:** V-01 proves C-24 (named token emission + separately declared downstream annotation count enables non-vacuous gate row 5 comparison). V-02 proves C-25 (per-FLS-ENTRY-block chain-reminder makes propagation contract continuously visible at each consumption site). V-03 combines both on the R7-V-05 base (which holds C-21 + C-22 + C-23). The mechanisms have no structural interaction: C-24 modifies Step 1 close format and Phase 1c section close; C-25 modifies FLS ENTRY block format and Gap Register header. The full chain from STEP-1-CLOSE-TOKEN source anchor → per-block reminders at consumption points → Phase 1c section-close annotation count → gate row 5 non-vacuous comparison should satisfy all 25 criteria for 180/180.

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
During Phase 1c, the three-part FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED block format is active. The CLOSED terminator is required before any subsequent FLS ENTRY begins. **Co-authorship is a structural property of the format**: a Gap? = YES cell without a completed REGISTER SLOT and a CLOSED marker is a broken block detectable by inspection. N/A markers on NO-gap REGISTER SLOTs make **trigger completeness provable from the output alone**.

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

This log is an **execution record, not a declarative checklist**. Each entry records that the named mechanism is already active as of Phase 0 close.

| Mechanism | Status | Notes |
|-----------|--------|-------|
| Chain 1 — discovery → register, Discovered In set at point of discovery | ACTIVE | Governs all register entries in Phases 1–4 |
| Chain 2 — register → Phase 5a verbatim echo, copy-not-write | ACTIVE | Verified in Phase 5b (structural precondition) |
| Per-row FLS trigger — FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED | ACTIVE | Structural format enforces co-authorship; CLOSED terminator required |
| Remediation template — Config change / Expected state / Verification step | ACTIVE | All three fields required; vague advice fails Config change |
| Mismatch example — Phase 5b self-check instrument | LOADED | Present in working context; Phase 5b self-check is a precondition for trace close |
| I-6 category drift / PR-1 — CATEGORY-DRIFT-VIOLATION marker (carries its own identifier and fires on re-derivation) | ACTIVE | Fires during Phase 1c Step 2 on any re-derivation of Step 1 category labels |
| STEP-1-CLOSE-TOKEN — named chain anchor emitted at Phase 1c Step 1 close | PENDING | Set at Phase 1c Step 1 close with exact FLS-scope field count; consumed by Phase 1c section close and gate row 5 |
| Per-stage chain-reminder — `[Category chain: active — inherit from Step 1]` at open of every FLS ENTRY block and Gap Register section | ACTIVE | Fires at each consumption point; must appear before the table header in every FLS ENTRY block |

*All mechanisms confirmed ACTIVE or LOADED at Phase 0 close. STEP-1-CLOSE-TOKEN PENDING — set at Phase 1c Step 1 close. Entering PHASE 1.*

---

## LIVE GAPS REGISTER

Opened at Phase 0. Populated inline during Phases 1–4. Chain 1 enforcement point.

**[Category chain: active — inherit from Step 1 for all category-related findings in this register]**

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

- **Discovered In**: exact section name and context, set at discovery time
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

Record Scope: Org / BU / Team / User / Sharing-[rule name]. All roles with any privilege. Dataverse system names required — display names alone fail C-01.

Chain 1 check after 1b: Scope anomaly → register. None → "Phase 1b: no scope anomalies — [basis]."

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
The Category column in every FLS ENTRY block must inherit its value from the Step 1 category table below — not re-derived inline. Any FLS ENTRY block where the Category value differs from the Step 1 table fires I-6 with marker CATEGORY-DRIFT-VIOLATION and a register entry (Discovered In: "Phase 1c Step 2 — [Entity].[Field] — category re-derived as [value], Step 1 records [correct value]", Gap type: CATEGORY-DRIFT). The chain-reminder annotation `[Category chain: active — inherit from Step 1]` at each FLS ENTRY block open converts this contract from a single-point declaration into a continuously visible constraint at each consumption site.

Step 1: category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII (name, contact info, ID, government data) | |
| | Financial (billing, pricing, payment, credit) | |
| | Audit/Compliance (modified-by, consent, audit trail) | |
| | Operational (status, queue, SLA, internal notes) | |

Write "none" for empty categories.

**Step 1 close — STEP-1-CLOSE-TOKEN (required by Phase 0 ACTIVATION STATE LOG):**

```
STEP-1-CLOSE-TOKEN
  Category table total rows analyzed: [N]
  FLS-scope rows (PII + Financial + Audit/Compliance): [M]
  Chain anchor value: [M]
```

This named token records the source count at the moment of Step 1 close. The Phase 1c section close will independently declare the downstream FLS ENTRY Category annotation count. Gate row 5 performs a non-vacuous numerical comparison: STEP-1-CLOSE-TOKEN chain anchor value [M] vs Phase 1c section-close downstream count [M].

Step 2: FLS check for all PII, Financial, and Audit/Compliance fields. Per-row trigger ACTIVE per Phase 0 log.

**Block format — mandatory for every sensitive field:**

Every FLS ENTRY block must open with the chain-reminder annotation before the table header. This is a per-block requirement:

```
[Category chain: active — inherit from Step 1]
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

**Block boundary rule:** A new FLS ENTRY block may not begin until FLS ENTRY [n] CLOSED appears. Every block must begin with `[Category chain: active — inherit from Step 1]`. **Co-authorship is a structural property of the format**. N/A markers prove trigger completeness from the output alone. Category value must match Step 1 table — PR-1 active; re-derivation fires CATEGORY-DRIFT-VIOLATION (I-6).

Section close:

```
Phase 1c FLS complete.
  FLS ENTRY blocks: [N]
  CLOSED markers written: [N] (must equal [N])
  YES entries: [N]
  N/A register slots: [N] (must equal NO-gap rows)
  Chain-reminder annotations at block opens: [N] (must equal [N] — one per block)
  Downstream FLS ENTRY Category annotation count: [M]
  (Separately declared here for gate row 5 token-swap. Must equal STEP-1-CLOSE-TOKEN chain anchor value [M].)
  Category chain: all [M] FLS ENTRY Category values inherited from Step 1 / [k] CATEGORY-DRIFT-VIOLATION entries
```

**1d — Sharing rule inventory:**

| Rule Name | Trigger | Access Opened | OWD Baseline | Conflicts Role Intent? |
|-----------|---------|---------------|-------------|------------------------|

Chain 1 check after 1d: Conflicts = YES → register. None → "Phase 1d: no SHARING-CONFLICT — [rules checked, specific reason]."

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
If RULED OUT: "No path — [specific reason per privilege]."

Chain 1 check per role: FOUND → register (Discovered In: "Phase 3 escalation — [role name]").

**Negative-check evidence per gap type:** For any gap type with no finding: "Checked [specific items] for [role list]; [type] does not apply because [specific reason]."

---

## PHASE 4 — ROLE DIFFERENTIATION

**Customer Service Representative:**
CRUD + Assign + Record Scope per entity from Phase 1b. Cross-reference Phase 1c Step 1 sensitive fields: PII, Financial, and Audit/Compliance fields accessible to CS — appropriate or overreach?

**Dataverse Security Expert:**
CRUD + Assign + Record Scope per entity. Every privilege the expert holds that Customer Service does not. Least-privilege or admin-level overreach?

**Contrast statement (required):**
One paragraph, both "Customer Service" and "Dataverse security expert" appear by name.

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

**This section is a precondition for closing the trace, not a recommended step. The trace is not closed until the TRACE CLOSE TOKEN is written.**

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

**TRACE CLOSE TOKEN:** `Chain 2 self-check applied: all Discovered In echoes verified verbatim against register. Rows verified: [N]. FAIL corrections: [N]. Trace closed.`

---

## SUBMISSION GATE

**ANTI-SPECULATION MANDATE — the named violation type (VERDICT-FAIL) is a protocol-level statement before the table header, not only a cell or row annotation inside it:**

No gate row may record PASS without citing specific evidence from this trace output — a named section, row count, token value, or finding. VERDICT-FAIL is a distinct named violation type, separate from CATEGORY-DRIFT-VIOLATION (which fires during Phase 1c evidence collection) — VERDICT-FAIL applies at gate review time to any row that asserts correctness without evidence. This statement is a protocol-level declaration governing all five rows below. It must be read before any row in the table.

| Row | Check | Evidence Cited | Status |
|-----|-------|----------------|--------|
| 1 | All entities in Phase 1a with OWD and scope stated | Cite Phase 1a row count and scope values | PASS / VERDICT-FAIL |
| 2 | All roles named by Dataverse system name; record scope per entity in Phase 1b | Cite Phase 1b role names and Record Scope column | PASS / VERDICT-FAIL |
| 3 | FLS analyzed for all PII, Financial, Audit/Compliance fields; all CLOSED markers written; chain-reminder annotation count equals block count in section close | Cite Phase 1c close: N blocks, N CLOSED, N chain-reminder annotations, category chain status | PASS / VERDICT-FAIL |
| 4 | All gap types checked with evidence; negative-check evidence for zero-finding types | Cite Phase 3 statements and Phase 2 rule-outs | PASS / VERDICT-FAIL |
| 5 | **End-to-end chain verification including non-vacuous token-swap**: (a) STEP-1-CLOSE-TOKEN chain anchor value = [M] (from Phase 1c Step 1 close — named structured artifact); (b) downstream FLS ENTRY Category annotation count = [M] (from Phase 1c section close — separately declared value); (c) token-swap: STEP-1-CLOSE-TOKEN [M] == section-close count [M]? YES/NO; (d) PR-1 propagation: all [M] FLS ENTRY blocks carry inherited Category values — no CATEGORY-DRIFT-VIOLATION; (e) evidence citations for rows 1–4: all PASS cited. This row passes only when all five sub-checks pass simultaneously. | Cite STEP-1-CLOSE-TOKEN value (named artifact), Phase 1c section-close downstream annotation count (separately declared), and rows 1–4 evidence | PASS / VERDICT-FAIL |

Gate passes only when all five rows read PASS with evidence cited. Row 5 is a jointly enforced chain-verifier. A comparison against a count never recorded in STEP-1-CLOSE-TOKEN format = non-vacuous comparison failed (C-24 not satisfied). A gate that does not report chain-reminder annotation count in row 3 = C-25 not verified.

---

## V-04 — Combined Variant: C-24 and C-25 Hoisted to Phase 0 as Pre-Declared Protocol Mechanisms

**Axis:** Role sequence / Lifecycle emphasis — both C-24 (STEP-1-CLOSE-TOKEN) and C-25 (per-stage chain-reminder) are pre-declared as named mechanisms in the Phase 0 ACTIVATION STATE LOG with PENDING → ACTIVE transition semantics, making both reviewable before Phase 1 begins and making failure to fire them visible as a broken PENDING state
**Hypothesis:** V-03 introduces both mechanisms at their point of use (Step 1 close and FLS ENTRY block format). The mechanisms work, but a reviewer reading the output from Phase 0 cannot verify that both are expected until reaching Phase 1c. V-04 hoists both into Phase 0: the ACTIVATION STATE LOG has explicit rows for STEP-1-CLOSE-TOKEN (PENDING — set at Phase 1c Step 1 close) and Per-stage chain-reminder (ACTIVE — fires at each FLS ENTRY block open and Gap Register section open). The PENDING state for STEP-1-CLOSE-TOKEN creates a pre-declared obligation: if Step 1 never emits the token, the Phase 0 log has a PENDING entry that was never resolved — a visibly broken chain anchor. Tests whether Phase 0 pre-declaration strengthens the C-24 pass condition relative to V-03's point-of-use definition.

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

**C-24 chain anchor — STEP-1-CLOSE-TOKEN protocol (pre-declared here; set at Phase 1c Step 1 close):**

At Phase 1c Step 1 close, emit this named artifact:

```
STEP-1-CLOSE-TOKEN
  Category table total rows analyzed: [N]
  FLS-scope rows (PII + Financial + Audit/Compliance): [M]
  Chain anchor value: [M]
```

The Phase 1c section close must independently declare the downstream FLS ENTRY Category annotation count. Gate row 5 performs a non-vacuous numerical comparison: STEP-1-CLOSE-TOKEN chain anchor value vs Phase 1c section-close annotation count. If Step 1 does not emit this named artifact, Phase 0 has an unresolved PENDING mechanism — the chain anchor is broken.

**C-25 per-stage chain-reminder protocol (pre-declared here; active from Phase 1c Step 2 onward):**

The annotation `[Category chain: active — inherit from Step 1]` must appear as the first line of every FLS ENTRY block — before the block's table header. The same annotation must appear at the LIVE GAPS REGISTER section header. This converts the PR-1 propagation contract from a single-point declaration (announced once before Step 2) into a continuously visible constraint present at each site that consumes category labels. Absence at any FLS ENTRY block open is a broken reminder — it is not deferred to the next block.

**PHASE 0 GATE — ACTIVATION STATE LOG:**

This log is an **execution record, not a declarative checklist**. PENDING entries have a named activation point — if that point is reached without the mechanism firing, the trace has a broken state.

| Mechanism | Status | Notes |
|-----------|--------|-------|
| Chain 1 — discovery → register, Discovered In set at point of discovery | ACTIVE | Governs all register entries in Phases 1–4 |
| Chain 2 — register → Phase 5a verbatim echo, copy-not-write | ACTIVE | Verified in Phase 5b (structural precondition) |
| Per-row FLS trigger — FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED | ACTIVE | Structural format enforces co-authorship; CLOSED terminator required |
| Remediation template — Config change / Expected state / Verification step | ACTIVE | All three fields required; vague advice fails Config change |
| Mismatch example — Phase 5b self-check instrument | LOADED | Present in working context; Phase 5b self-check is a precondition for trace close |
| I-6 category drift / PR-1 — CATEGORY-DRIFT-VIOLATION marker (carries its own identifier and fires on re-derivation) | ACTIVE | Fires during Phase 1c Step 2 on any re-derivation of Step 1 category labels |
| STEP-1-CLOSE-TOKEN (C-24) — named chain anchor; protocol declared above | PENDING | Activation point: Phase 1c Step 1 close. Unresolved PENDING at trace close = broken chain anchor. |
| Per-stage chain-reminder (C-25) — `[Category chain: active — inherit from Step 1]` at FLS ENTRY block open and Gap Register section open; protocol declared above | ACTIVE | First activation: LIVE GAPS REGISTER section header (this document). Must fire at every subsequent FLS ENTRY block open. |

*All mechanisms confirmed ACTIVE or LOADED. STEP-1-CLOSE-TOKEN PENDING — activation at Phase 1c Step 1 close. Entering PHASE 1.*

---

## LIVE GAPS REGISTER

Opened at Phase 0. Populated inline during Phases 1–4. Chain 1 enforcement point.

**[Category chain: active — inherit from Step 1 for all category-related findings in this register]** *(Per-stage chain-reminder (C-25) — first activation point)*

| ID | Discovered In | Gap Type | Entity | Field (if FLS) | Role | Severity |
|----|--------------|----------|--------|----------------|------|----------|

- **Discovered In**: exact section name and context, set at discovery time
- Gap types: MISSING-FLS / ESCALATION-PATH / SHARING-CONFLICT / TEAM-GAP / CROSS-ENTITY / CATEGORY-DRIFT
- Severity: CRITICAL / HIGH / MEDIUM

---

## PHASE 1 — ENTITY AND ROLE MAP

**1a — Entity and OWD inventory:**

| Entity | Org-Wide Default | Scope | Default access for unauthenticated user |
|--------|-----------------|-------|----------------------------------------|

OWD scope: Organization / Business Unit / Owner. Missing scope = incomplete row.

Chain 1 check after 1a: OWD anomaly → register. None → "Phase 1a: no OWD anomalies — [basis]."

**1b — Operation-role matrix:**

| Entity | Role | Create | Read | Write | Delete | Assign | Record Scope |
|--------|------|--------|------|-------|--------|--------|--------------|

Record Scope: Org / BU / Team / User / Sharing-[rule name]. All roles with any privilege. Dataverse system names required — display names alone fail C-01.

Chain 1 check after 1b: Scope anomaly → register. None → "Phase 1b: no scope anomalies — [basis]."

**1c — Sensitive field categorization:**

**Inertia threat inventory (declared before Step 1 — each threat carries its own identifier and a marker that fires on re-derivation or violation):**

| ID | Threat | Fires During | Marker |
|----|--------|-------------|--------|
| I-1 | OWD defaults creating unexpected default access | Phase 1a | ESCALATION-PATH (OWD scope) in register |
| I-2 | Missing FLS profiles on PII, Financial, or Audit/Compliance fields | Phase 1c FLS check | MISSING-FLS in register |
| I-3 | Sharing rule overrides granting unintended access | Phase 1d | SHARING-CONFLICT in register |
| I-4 | Team membership control enabling privilege injection | Phase 2a | TEAM-GAP in register |
| I-5 | EMERGENT cross-entity hops | Phase 2b | CROSS-ENTITY in register |
| I-6 | **Category drift** — inline re-derivation of PII / Financial / Audit/Compliance / Operational labels at any point downstream of Phase 1c Step 1; carries its own identifier (I-6) and a marker that fires on re-derivation | Phase 1c Step 2 onward | CATEGORY-DRIFT-VIOLATION in register |

**PR-1: Category propagation contract (established here; active from Step 2 forward):**
The Category column in every FLS ENTRY block must inherit its value from the Step 1 category table below — not re-derived inline. Re-derivation fires I-6 → CATEGORY-DRIFT-VIOLATION → register entry. The per-stage chain-reminder (C-25) declared in Phase 0 fires at each FLS ENTRY block open — this is the mechanism that converts PR-1 from a single-point contract into a continuously visible constraint.

Step 1: category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII (name, contact info, ID, government data) | |
| | Financial (billing, pricing, payment, credit) | |
| | Audit/Compliance (modified-by, consent, audit trail) | |
| | Operational (status, queue, SLA, internal notes) | |

Write "none" for empty categories.

**Step 1 close — STEP-1-CLOSE-TOKEN activation (resolves PENDING from Phase 0 ACTIVATION STATE LOG):**

```
STEP-1-CLOSE-TOKEN — ACTIVATED
  Category table total rows analyzed: [N]
  FLS-scope rows (PII + Financial + Audit/Compliance): [M]
  Chain anchor value: [M]
  Phase 0 PENDING status: RESOLVED
```

Gate row 5 will compare this chain anchor value against the Phase 1c section-close downstream annotation count. Both values are separately named. The comparison is non-vacuous.

Step 2: FLS check for all PII, Financial, and Audit/Compliance fields. Per-row trigger ACTIVE per Phase 0 log.

**Block format — mandatory for every sensitive field:**

Per-stage chain-reminder (C-25, declared in Phase 0) fires at each block open:

```
[Category chain: active — inherit from Step 1]
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

**Block boundary rule:** CLOSED terminator required. Chain-reminder `[Category chain: active — inherit from Step 1]` at every block open — pre-declared in Phase 0; absence is a broken state. Category value must match Step 1 table — PR-1 active.

Section close:

```
Phase 1c FLS complete.
  FLS ENTRY blocks: [N]
  CLOSED markers written: [N] (must equal [N])
  YES entries: [N]
  N/A register slots: [N]
  Chain-reminder annotations at block opens: [N] (must equal [N] — per-stage C-25 verification)
  Downstream FLS ENTRY Category annotation count: [M]
  (Separately declared for gate row 5 token-swap vs STEP-1-CLOSE-TOKEN anchor [M])
  Category chain: all [M] FLS ENTRY Category values inherited from Step 1 / [k] CATEGORY-DRIFT-VIOLATION entries
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
Chain 1 check: TEAM-GAP if found. None → "Phase 2a: no TEAM-GAP — [teams, basis]."

**2b — Cross-entity permission chain:**

Highest-sensitivity entity (justify from Phase 1c Step 1). Trace two hops: `[Role] → [Entity A, op: X, scope: Y] → [Relationship] → [Entity B, op: X, scope: Y]`. INTENTIONAL or EMERGENT. Chain 1 check: CROSS-ENTITY if found.

---

## PHASE 3 — PER-ROLE ESCALATION ANALYSIS

One subsection per role. No collective statements.

**Role: [name]**
- Team membership Write: [YES / NO — evidence]
- Security role assignment Write: [YES / NO — evidence]
- Record ownership Assign scope: [scope — elevation?]
- Business unit configuration Write: [YES / NO — evidence]

Conclusion: ESCALATION-PATH FOUND / RULED OUT. Chain 1 check if found.

**Negative-check evidence per gap type:** For any zero-finding type: "Checked [items] for [roles]; [type] does not apply because [specific reason]."

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

Mismatch example loaded at Phase 0. Apply now: PASSING = verbatim. FAILING = truncated / dropped / rephrased.

| Gap ID | Register: Discovered In (exact text) | Phase 5a Echo: Discovered In (exact text) | Match? |
|--------|--------------------------------------|-------------------------------------------|--------|

**TRACE CLOSE TOKEN:** `Chain 2 self-check applied: all Discovered In echoes verified verbatim. Rows: [N]. FAIL corrections: [N]. Trace closed.`

---

## SUBMISSION GATE

**ANTI-SPECULATION MANDATE — VERDICT-FAIL is a protocol-level statement before the table header:**

No gate row may record PASS without citing specific evidence. VERDICT-FAIL applies at gate review time. This declaration governs all five rows and must be read before any row in the table.

| Row | Check | Evidence Cited | Status |
|-----|-------|----------------|--------|
| 1 | All entities Phase 1a with OWD and scope | Cite Phase 1a row count and scope values | PASS / VERDICT-FAIL |
| 2 | All roles by Dataverse system name; record scope per entity | Cite Phase 1b role names and Record Scope column | PASS / VERDICT-FAIL |
| 3 | FLS analyzed for all sensitive fields; all CLOSED; chain-reminder count equals block count (C-25 per-stage verification) | Cite Phase 1c close: N blocks, N CLOSED, N chain-reminder annotations | PASS / VERDICT-FAIL |
| 4 | All gap types checked; negative-check evidence present | Cite Phase 3 statements and Phase 2 rule-outs | PASS / VERDICT-FAIL |
| 5 | **Non-vacuous token-swap chain verification**: (a) STEP-1-CLOSE-TOKEN chain anchor [M] — PENDING resolved in Phase 1c (named artifact from Phase 0 pre-declaration); (b) Phase 1c section-close downstream annotation count [M] — separately declared value; (c) token-swap [M] == [M]? YES/NO; (d) PR-1 propagation — no CATEGORY-DRIFT-VIOLATION; (e) rows 1–4 all PASS. Jointly enforced — all five sub-checks required. | Cite STEP-1-CLOSE-TOKEN ACTIVATED token, Phase 1c section-close count, and rows 1–4 evidence | PASS / VERDICT-FAIL |

Gate passes when all five rows PASS with evidence. Any VERDICT-FAIL halts the gate.

---

## V-05 — Combined + Rubric-Verbatim Language (C-24 + C-25 at Maximum Specification Fidelity)

**Axis:** Phrasing register — V-03 structure with rubric-exact pass-condition phrases embedded at each C-24 and C-25 enforcement point
**Hypothesis:** Each new criterion has distinguishing language that separates its pass condition from the adjacent criterion's pass condition. C-24: "emit a named close token recording the exact count of items analyzed" and "Phase 1c section close must announce the downstream annotation count" and "non-vacuous numerical comparison". C-25: "`[Category chain: active — inherit from Step N]`" exact form and "consumption point — chain-reminder required at block open" and "converts the propagation contract from a single-point declaration to a continuously-visible constraint at each block that consumes category labels." Embedding these exact phrases at the structural enforcement points — Step 1 close instruction, Phase 1c section close instruction, block format definition, gate row 5 label — gives the model the rubric's own pass-condition language before the output is generated. All R7-V-05 mechanisms (ACTIVATION STATE LOG, FLS ENTRY CLOSED, Phase 5b self-check, TRACE CLOSE TOKEN, VERDICT-FAIL preamble, I-6 with CATEGORY-DRIFT-VIOLATION, PR-1, chain-verifier gate row 5) are preserved exactly.

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
During Phase 1c, the three-part FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED block format is active. The CLOSED terminator is required before any subsequent FLS ENTRY begins. **Co-authorship is a structural property of the format**: a Gap? = YES cell without a completed REGISTER SLOT and a CLOSED marker is a broken block detectable by inspection. N/A markers on NO-gap REGISTER SLOTs make **trigger completeness provable from the output alone**.

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

This log is an **execution record, not a declarative checklist**. Each entry records that the named mechanism is already active as of Phase 0 close.

| Mechanism | Status | Notes |
|-----------|--------|-------|
| Chain 1 — discovery → register, Discovered In set at point of discovery | ACTIVE | Governs all register entries in Phases 1–4 |
| Chain 2 — register → Phase 5a verbatim echo, copy-not-write | ACTIVE | Verified in Phase 5b (structural precondition) |
| Per-row FLS trigger — FLS ENTRY [n] / REGISTER SLOT [n] / FLS ENTRY [n] CLOSED | ACTIVE | Structural format enforces co-authorship; CLOSED terminator required |
| Remediation template — Config change / Expected state / Verification step | ACTIVE | All three fields required; vague advice fails Config change |
| Mismatch example — Phase 5b self-check instrument | LOADED | Present in working context; Phase 5b self-check is a precondition for trace close |
| I-6 category drift / PR-1 — CATEGORY-DRIFT-VIOLATION marker (carries its own identifier and fires on re-derivation) | ACTIVE | Fires during Phase 1c Step 2 on any re-derivation of Step 1 category labels |
| STEP-1-CLOSE-TOKEN (C-24) — named close token recording the exact count of items analyzed; emitted at Phase 1c Step 1 close; Phase 1c section close announces the downstream annotation count; gate row 5 performs a non-vacuous numerical comparison between these two separately declared values | PENDING | Activation: Phase 1c Step 1 close. Unresolved PENDING = chain anchor absent = C-24 fail. |
| Per-stage chain-reminder (C-25) — `[Category chain: active — inherit from Step 1]` exact form at open of every FLS ENTRY block (consumption point) and Gap Register section; converts the propagation contract from a single-point declaration to a continuously-visible constraint at each block that consumes category labels | ACTIVE | First fire: LIVE GAPS REGISTER header below. Must fire at every subsequent consumption point. Absence at any FLS ENTRY block open = C-25 fail. |

*All mechanisms confirmed ACTIVE or LOADED at Phase 0 close. STEP-1-CLOSE-TOKEN PENDING. Entering PHASE 1.*

---

## LIVE GAPS REGISTER

Opened at Phase 0. Populated inline during Phases 1–4. Chain 1 enforcement point.

**[Category chain: active — inherit from Step 1]** *(exact form — C-25 per-stage chain-reminder; first consumption point)*

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
The Category column in every FLS ENTRY block must inherit its value from the Step 1 category table below — not re-derived inline. At each FLS ENTRY block open (consumption point), write the chain-reminder annotation in its exact form: `[Category chain: active — inherit from Step 1]`. This annotation converts the PR-1 propagation contract from a single-point declaration (announced once before Step 2) into a continuously-visible constraint at each block that consumes category labels. Any FLS ENTRY block where the Category value differs from the Step 1 table fires I-6 with marker CATEGORY-DRIFT-VIOLATION and a register entry (Discovered In: "Phase 1c Step 2 — [Entity].[Field] — category re-derived as [value], Step 1 records [correct value]", Gap type: CATEGORY-DRIFT). A prompt that declares PR-1 and I-6 but has no per-stage reminders at consumption points does not satisfy C-25.

Step 1: category inventory:

| Entity | Category | Fields |
|--------|----------|--------|
| | PII (name, contact info, ID, government data) | |
| | Financial (billing, pricing, payment, credit) | |
| | Audit/Compliance (modified-by, consent, audit trail) | |
| | Operational (status, queue, SLA, internal notes) | |

Write "none" for empty categories.

**Step 1 close — emit a named close token recording the exact count of items analyzed (C-24 chain anchor):**

```
STEP-1-CLOSE-TOKEN
  Category table total rows analyzed: [N]
  FLS-scope rows (PII + Financial + Audit/Compliance): [M]
  Chain anchor value: [M]
```

This is a named close token recording the exact count of items analyzed. The Phase 1c section close must announce the downstream annotation count as a separately declared value. Gate row 5 performs a non-vacuous numerical comparison between the STEP-1-CLOSE-TOKEN chain anchor value [M] and the Phase 1c section-close annotation count [M]. A gate that performs a token-swap check against a count never explicitly recorded at source — never emitted in this STEP-1-CLOSE-TOKEN format — fails C-24.

Step 2: FLS check for all PII, Financial, and Audit/Compliance fields. Per-row trigger ACTIVE per Phase 0 log.

**Block format — mandatory for every sensitive field:**

Every FLS ENTRY block is a consumption point. The chain-reminder `[Category chain: active — inherit from Step 1]` must appear in its exact form as the first line before the block table header:

```
[Category chain: active — inherit from Step 1]
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

**Block boundary rule:** A new FLS ENTRY block may not begin until FLS ENTRY [n] CLOSED appears. Every FLS ENTRY block is a consumption point — the chain-reminder `[Category chain: active — inherit from Step 1]` (exact form) is required at block open. Its absence at any block open means the propagation contract is not continuously visible at that consumption site — C-25 fail for that block. **Co-authorship is a structural property of the format**: the block structure makes omission impossible to overlook. N/A markers prove trigger completeness from the output alone. Category value in each block must match Step 1 table — PR-1 active; re-derivation fires CATEGORY-DRIFT-VIOLATION (I-6).

Section close — announce the downstream annotation count (C-24 second anchor):

```
Phase 1c FLS complete.
  FLS ENTRY blocks: [N]
  CLOSED markers written: [N] (must equal [N])
  YES entries: [N]
  N/A register slots: [N] (must equal NO-gap rows)
  Chain-reminder annotations at consumption points: [N] (must equal [N] — C-25 per-stage verification)
  Downstream FLS ENTRY Category annotation count: [M]
  (Announced here as separately declared value for C-24 gate row 5 non-vacuous comparison.
   Must equal STEP-1-CLOSE-TOKEN chain anchor value [M].)
  Category chain: all [M] FLS ENTRY Category values inherited from Step 1 / [k] CATEGORY-DRIFT-VIOLATION entries
  Trigger completeness: verified by CLOSED marker count and N/A slot count
```

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
| 3 | FLS analyzed for all PII, Financial, Audit/Compliance fields; all CLOSED markers written; chain-reminder annotation (C-25 exact form) count equals FLS ENTRY block count in section close — no C-25 violation | Cite Phase 1c close: N blocks, N CLOSED, N consumption-point chain-reminder annotations, category chain status | PASS / VERDICT-FAIL |
| 4 | All gap types checked with evidence; negative-check evidence for zero-finding types | Cite Phase 3 statements and Phase 2 rule-outs | PASS / VERDICT-FAIL |
| 5 | **End-to-end chain verification including non-vacuous numerical comparison**: (a) STEP-1-CLOSE-TOKEN chain anchor value = [M] (named close token recording the exact count of items analyzed, emitted at Phase 1c Step 1 close); (b) Phase 1c section-close downstream annotation count = [M] (announced by section close as separately declared value); (c) non-vacuous numerical comparison: STEP-1-CLOSE-TOKEN [M] == section-close annotation count [M]? YES/NO; (d) PR-1 propagation — no CATEGORY-DRIFT-VIOLATION (C-25 chain-reminder converted single-point declaration into continuously-visible constraint at each consumption point); (e) evidence citations rows 1–4: all PASS cited. Row 5 passes only when all five sub-checks pass simultaneously — it is a jointly enforced chain-verifier row. A gate that compares against a count never explicitly recorded in STEP-1-CLOSE-TOKEN format = non-vacuous comparison failed (C-24 not satisfied). | Cite STEP-1-CLOSE-TOKEN value (named close token, exact count), Phase 1c section-close downstream annotation count (separately declared), and rows 1–4 evidence citations | PASS / VERDICT-FAIL |

Gate passes only when all five rows read PASS with evidence cited. Any VERDICT-FAIL row halts the gate. Row 5 is an atomically enforced chain-verifier — a gate that checks each sub-criterion in an independent row with no row verifying the full chain end-to-end fails C-23. A gate whose row 5 cites a token count not emitted as a named structured artifact at Step 1 close fails C-24. A gate that does not report chain-reminder annotation count in row 3 fails C-25.
