# flow-lifecycle — Round 15 Variations (Rubric v15)

**Rubric**: v15 · 47 criteria (39 aspirational) · Ceiling entering R15: 39/39
(R14 V-05 achieved 39/39 retroactive score under v15; C-46 and C-47 signals implicitly present via
SECTION A per-phase incumbent reference comments and IM-ID citation wording in EX Trigger/Why
Problematic fields.)

**Open criteria entering R15**: C-46, C-47 — both implicitly triggered by R14 V-05 but never
explicitly named as required structural sub-fields. R15 escalates both to named, positionally fixed,
format-verifiable sub-fields in their canonical locations: `IM Reference:` in PHASE ENTRY CONTRACT
(C-46) and `IM Ref:` in each SECTION A EX block (C-47). Goal: reliable C-46/C-47 compliance across
variations rather than inference-dependent implicit anchoring.

**Evidence from R14 excellence (C-46, C-47):**

- **C-46 signal**: R14 V-05 placed a per-phase "Incumbent reference" comment at the top of each
  SECTION A naming the primary IM-ID most likely to manifest. This was detected as C-46 (per-phase
  IM-reference callout) but lives in SECTION A, not PHASE ENTRY CONTRACT. R15 V-04 promotes the
  callout to a named `IM Reference:` sub-field in the PHASE ENTRY CONTRACT block where C-46 requires
  it, making it string-comparable and positionally verifiable without traversal.
- **C-47 signal**: R14 V-05 used Trigger and Why Problematic wording to anchor EX blocks to IM-IDs
  implicitly ("cite the IM-ID it reflects where applicable"). C-47 requires a named `IM Ref:` sub-field
  alongside `Bottleneck Ref:` in every EX block — dual-citation architecture, not prose anchoring.
  R15 V-05 makes `IM Ref:` a structural peer of `Bottleneck Ref:`, completing the convergence-point
  architecture.

**R15 design premise**: R14 established the B-NN↔Exception traceability infrastructure (C-44) and
the three-field phase gate contract architecture (C-45). R15 anchors the INCUMBENT BASELINE into the
phase architecture directly — first at phase-entry level (C-46), then at exception-block level
(C-47). Single-axis tests confirm which structural location is the minimum required for each criterion;
V-05 confirms they compose without conflict.

**New criteria targeted in R15:**

**C-46 target (V-04, V-05)**: Add a named `IM Reference:` sub-field to every PHASE ENTRY CONTRACT.
Field lists IM-IDs from INCUMBENT BASELINE whose failure modes represent active risks entering that
phase. NONE sentinel for phases with no active IM risk. Distinct from the R14 V-05 approach of
placing an incumbent comment at SECTION A level — R15 puts it in the contract block itself.

**C-47 target (V-05)**: Add a named `IM Ref:` sub-field to every SECTION A EX block alongside the
existing `Bottleneck Ref:` (C-42). Dual-citation makes EX blocks the convergence point for three
traceability chains simultaneously: Role (C-40), B-NN (C-42), Baseline (C-47). CHAIN STATUS gains
a `Baseline→Exception` direction. R14 V-05 implicitly traced this; R15 makes it format-verifiable.

**Variation matrix:**

| Variation | Axes | C-44 Exception Refs per-block | C-45 CONTRACT SUMMARY | C-46 IM Reference in entry | C-47 IM Ref in EX block | Primary hypothesis |
|-----------|------|------------------------------|----------------------|---------------------------|------------------------|--------------------|
| V-01 | Role sequence | NO (gate only) | NO | NO | NO | Baseline — no C-44/C-45/C-46/C-47 explicit structure; establishes floor for single-axis comparisons |
| V-02 | Output format | YES (named block, format example) | NO | NO | NO | Isolated per-block `Exception Refs:` instruction produces reliable C-44; C-45/C-46/C-47 remain FAIL |
| V-03 | Lifecycle emphasis | NO (gate only) | YES (dedicated section) | NO | NO | Dedicated PHASE GATE CONTRACT SUMMARY section scores C-45 independently; C-44/C-46/C-47 remain FAIL |
| V-04 | Inertia framing | NO (gate only) | NO | YES (named sub-field) | NO | Explicit `IM Reference:` named sub-field in PHASE ENTRY CONTRACT scores C-46; single-axis test confirms without C-44/C-45/C-47 |
| V-05 | Output format + Lifecycle emphasis + Inertia framing | YES (named block) | YES (dedicated section) | YES (named sub-field) | YES (named sub-field, dual-cite) | Maximum density — all four criteria compose; EX blocks carry triple citation (C-40 + C-42 + C-47); CHAIN STATUS gains Baseline→Exception direction |

**Structural change summary vs R14 V-05:**

| Section | R14 V-05 had | V-01 removes | V-02 adds | V-03 adds | V-04 adds | V-05 combines |
|---------|-------------|-------------|----------|----------|----------|--------------|
| PHASE GATE CONTRACT SUMMARY | Dedicated named section | Removed | — | Restored | — | Restored |
| PHASE ENTRY CONTRACT | Prior phase, Prior phase blocked bottleneck only | Same as R14 V-01 | — | — | `IM Reference:` named sub-field | All three sub-fields |
| SECTION A EX blocks | Bottleneck Ref + Role Ref + implicit IM-ID prose wording | Bottleneck Ref + Role Ref only | — | — | — | + `IM Ref:` named sub-field (dual-cite) |
| B-NN block `Exception Refs:` | Isolated named instruction block | Removed (gate-only) | Restored (isolated block) | Gate-only | Gate-only | Restored (isolated block) |
| CHAIN STATUS | 11 directions | 11 directions | + B-NN→Exception consistency | Same as V-01 | + Baseline→Phase direction | + Baseline→Exception direction (12 total) |

---

## V-01 — Axis: Role Sequence (Default Ordering, Baseline)

**Variation axis**: Role sequence — default domain-natural role ordering (Sales/Procurement/Finance/
Operations sequence determined by process type). INCUMBENT BASELINE uses standard two-row structure
without per-phase incumbent callouts. PHASE ENTRY CONTRACT carries two sequential-linkage sub-fields
only (`Prior phase:` and `Prior phase blocked bottleneck:`); no `IM Reference:` sub-field. SECTION A
EX blocks carry `Bottleneck Ref:` and `Role Ref:` only; no `IM Ref:` sub-field. Bottleneck Analysis
uses preamble gate check only for the B-NN→Exception direction (no per-block `Exception Refs:` field).
No PHASE GATE CONTRACT SUMMARY section.

**Hypothesis**: Without explicit C-44/C-45/C-46/C-47 structural additions, the baseline prompt
produces approximately 34/39 aspirational coverage. All structural elements from C-01 through C-43
should pass (C-43 depends on prior round scaffolding). C-44 requires per-block enumeration beyond
preamble gate check; C-45 requires an explicit named three-field unit declaration; C-46 requires a
named `IM Reference:` sub-field in PHASE ENTRY CONTRACT; C-47 requires a named `IM Ref:` sub-field
in EX blocks. None of these are present in V-01, establishing the floor for the three single-axis
variations.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1 in document order.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools used (spreadsheets, email, phone), handoff
mechanisms, where records are stored, who initiates the process manually.]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure in the manual process] | [daily / per-cycle / per-exception] | [downstream effect on SLA or accuracy] |
| IM-02 | [second distinct failure mode — different process layer from IM-01] | [frequency] | [downstream effect] |

**Cost of no action**: [Named measure with current-state value or rate, declared before PHASE 1.
Both IM-IDs must be reachable from at least one B-NN Cause field below. Example: "Average credit
approval cycle time: 5.8 days vs 3-day SLA" or "Manual matching error rate: 12% per period."]

---

### Role Registry Gate

> GATE BLOCK: Complete before the Role Sequence Schedule and before tracing any state.
> All four anti-generic checks must clear before proceeding.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation (all four must clear before proceeding):
- [ ] No R-ID entry uses "Approver" without a domain qualifier
- [ ] No R-ID entry uses "Owner" without a named responsibility
- [ ] Each R-ID is referenced by at least one Decision Supplement block, the Role Sequence
      Schedule, and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field
- [ ] Each declared R-ID appears in at least one EX block's `Role Ref:` sub-field — R-IDs
      with no observable EX trace are "dark" roles and constitute a gate violation

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to owned phases with
> activation triggers, handoff triggers, and parallel windows. B-NN Cause fields must cite
> the blocking R-ID from this schedule (Dual-Cite Fail Condition B). R-IDs cited in EX block
> `Role Ref:` sub-fields must appear in this schedule as the phase owner for the enclosing phase.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact — not "Start"] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1 — name the artifact] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

Rules: Every phase must have a Primary Owner. Activation Trigger for Phase 1 must name an external
event or prior-process artifact. Every R-ID here must match a Role Registry Gate entry.

---

### Phase Structure

For each phase in the lifecycle, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" by name.
> Two sequential-linkage sub-fields are required and must not be conflated:
> `Prior phase:` carries the literal phase identifier (Phase→Phase backward linkage).
> `Prior phase blocked bottleneck:` carries the B-ID from the prior exit gate (B-NN boundary
> continuity). Both are independently verifiable by string comparison.

- Entry Condition: [specific named artifact from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name — must match Role Sequence Schedule primary owner for this phase]) — [verification method]
- Blocking condition: [if entry condition not met: which state is entered, which role notified, re-entry path]
- Prior phase: [Literal identifier of the preceding phase block, e.g., "PHASE 1 — Initiation".
  Phase 1 carries NONE or INIT as sentinel. Non-first phase with sentinel fails. First phase
  with phase identifier fails. Must string-match preceding phase block label in document order.]
- Prior phase blocked bottleneck: [B-ID from prior phase PHASE EXIT GATE `Blocked bottleneck:`
  or NONE if that field was NONE, or N/A for Phase 1. Must string-match prior exit gate field
  AND B-NN block identifier.]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition — name the state, threshold breach, or missing input]
> - Trace: [path of states traversed from trigger to resolution or terminal; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason this failure mode matters]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. Preamble gate check verifies that every declared B-ID
>   appears in at least one EX block's `Bottleneck Ref:` — populate accurately. NONE if no
>   declared bottleneck was causal.]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID
>   matching the schedule entry for the enclosing phase. Free-text without R-ID fails.]

Minimum 1 exception trace per phase; 3 total minimum.
Every declared R-ID in the Role Registry Gate must appear in at least one EX block Role Ref.
Bottleneck Ref and Role Ref are independent sub-fields; populate both for every EX block.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules:
- Every state must have a named Entry Condition. "Ready" or "Previous step complete" fails.
- Every Exit must reference a destination S-ID or carry the label TERMINAL.
- Type values: NORMAL / DECISION / PARALLEL-FORK / PARALLEL-JOIN / EXCEPTION / TERMINAL

**Decision Supplement Blocks** (one per DECISION-type state in this phase):

> **DS-[S-ID] — [State Name]**
> - Condition: [rule or threshold evaluated]; Owner: R-[ID]; Branch A: → S-[ID];
>   Branch B: → S-[ID] or TERMINAL; Fallback: [action if condition cannot be evaluated]

**PHASE EXIT GATE**

> `Blocked bottleneck:` names the B-ID that can delay this phase's exit, or NONE.
> `Next phase:` names the subsequent phase by literal identifier, or NONE/END for last phase.
> These sub-fields are independent: `Blocked bottleneck:` carries a B-ID;
> `Next phase:` carries a Phase label. Do not conflate.

- Exit Condition: [what the phase must have produced to be considered complete]
- Required outputs: [named artifacts, decisions, or state records that must exist]
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) confirms all required outputs present
- Blocking condition: [if required outputs absent: re-entry path or escalation]
- Blocked bottleneck: [B-NN or NONE. Must string-match Bottleneck Analysis identifier AND
  next phase's `Prior phase blocked bottleneck:`.]
- Next phase: [Literal identifier of the subsequent phase block. Last phase: NONE or END sentinel.
  Must string-match next phase block label in document order.]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [states traversed; cite S-IDs in sequence]
- **Branch 2**: [states traversed; cite S-IDs in sequence]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join / OR-join — specify which applies and explain why

---

### Edge Case Enumeration

At least three edge cases distinct from SECTION A exception flows:

> **EC-[N] — [Edge Case Name]**
> - Triggering Condition: [specific scenario]
> - Why Problematic: [specific reason this falls outside documented handling]
> - Correct Response: R-[ID] ([role name]) — [specific correct action; name target state or resolution path]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF — {Topic} lifecycle → [adjacent process name]**
> - Sending State: S-[ID] / Receiving Process: [name] / Data Payload: [named fields]
> - Expected Acknowledgment: [signal or confirmation] / Failure Mode: [if acknowledgment not received]
> - Owner: R-[ID]

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Rules: AT-RISK = typical duration exceeds SLA target. Every AT-RISK row must carry a Bottleneck Ref
citing a B-NN from Bottleneck Analysis. Minimum 3 annotated rows; at least 1 must be AT-RISK.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both Dual-Cite Fail Conditions independently.
>
> **Dual-Cite Fail Condition A** — Cause field contains no IM-ID literal string (e.g., "IM-01"):
> fails C-39. Verify: search Cause field for "IM-" followed by digits. Absence → fail.
>
> **Dual-Cite Fail Condition B** — Cause field contains no R-ID literal string (e.g., "R-01"):
> fails C-39. Verify: search Cause field for "R-" followed by digits. Absence → fail.
>
> B-IDs assigned here must string-match ALL of: (1) PHASE EXIT GATE `Blocked bottleneck:`
> fields, (2) PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:` in the following phase,
> and (3) EX block `Bottleneck Ref:` fields where non-NONE.
>
> Concrete format example for Evidence field:
> `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
>
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: A field containing only "see SLA ANALYSIS" or state names without
> AT-RISK row-level S-ID specificity does not satisfy.
>
> **DUAL-LOCATION REQUIREMENTS:**
> (1) Concrete named domain example must appear in BOTH this preamble AND each B-NN per-block
> Evidence hint.
> (2) Labeled axes (`Required format:` / `Fail condition:`) must appear in BOTH this preamble
> AND each B-NN per-block Evidence hint.
>
> **B-NN→Exception Gate Check**: Every declared B-ID below must appear in at least one EX
> block's `Bottleneck Ref:` sub-field across all phases. A B-ID absent from all EX blocks is
> a "dark bottleneck" — declared failure mode with no exception-phase trace. Dark bottlenecks
> are gate violations. Report result in CHAIN STATUS `B-NN→Exception` direction.
>
> Anti-embedding: Declare CHAIN STATUS in its own dedicated top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).
  Example: "IM-01 (manual reconciliation gap) combined with R-02 (GL Manager) period-close
  unavailability — approval queue at S-05. 'IM-01' satisfies A; 'R-02' satisfies B."]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream state, SLA node, or adjacent process affected]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01.]

---

**B-02 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string AND R-ID literal string.]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: [same as B-01]
  - [List each AT-RISK SLA row citing B-02.]

---

**Gap Identification**

> MISSING: [step name] — [rationale: why it belongs; failure mode enabled; which phase;
> which IM-ID it would reduce if present]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name gap]
- Backward (B→SLA): [every B-NN Evidence field lists AT-RISK SLA rows; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID matches a declared B-NN; name any mismatch]
- Phase-boundary B-NN continuity: [every exit gate B-ID matches next phase's `Prior phase blocked bottleneck:`; list pairs or name break]
- Phase-sequence: [every PHASE ENTRY CONTRACT `Prior phase:` matches preceding phase block label; PHASE 1 carries NONE/INIT; list pairs or name mismatch]
- Phase-exit-sequence: [every PHASE EXIT GATE `Next phase:` matches subsequent phase block; last phase carries NONE/END; list pairs or name mismatch]
- Exception→B: [every EX block `Bottleneck Ref:` B-ID (non-NONE) matches a declared B-NN; list EX→B-NN pairs or name unresolved block]
- B-NN→Exception: [every declared B-ID appears in at least one EX block's `Bottleneck Ref:`; enumerate B-ID→EX pairs; name any B-ID with no EX trace (dark bottleneck)]
- Exception→Role: [every EX block `Role Ref:` R-ID matches ROLE SEQUENCE SCHEDULE primary owner; list EX→R-ID pairs or name mismatch]
- Role→Exception: [every declared R-ID appears in at least one EX block `Role Ref:`; list R-ID→EX pairs; name dark roles]
- Dual-cite status: [every B-NN Cause has both IM-ID and R-ID; name any block missing either]
- Gap (if OPEN): [unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state that reaches it] |
| [failure terminal name] | FAILURE | [branch or state that reaches it] |
| [cancel terminal name] | CANCEL | [branch or state that reaches it] |

> Completeness check: Every exit branch in every SECTION B state table must reach one of the
> declared terminals. No branch may end at a non-terminal state without `continues-via: S-[ID]`.

---
---

## V-02 — Axis: Output Format (Isolated Per-Block Exception Refs, C-44 Target)

**Variation axis**: Output format — the `Exception Refs:` instruction in each B-NN block is
promoted to an isolated, self-contained named instruction block with its own format example and
failure condition, separated from the preamble gate check. The preamble retains only the gate check
(document-level existence assertion); each B-NN block carries a dedicated `Exception Refs:` section
with its own inline format hint naming the specific B-ID. Makes the per-block `Exception Refs:` field
format-identical to the Evidence field (both carry a named instruction block with Required format +
Fail condition). No PHASE GATE CONTRACT SUMMARY, no `IM Reference:` in entry contracts, no `IM Ref:`
in EX blocks.

**Hypothesis**: The V-01 baseline's preamble-only gate check is insufficient for C-44, which requires
per-block navigable lookup (not just a document-level existence assertion). Promoting `Exception Refs:`
to an isolated named instruction block — symmetric to how the Evidence field has its own format hint —
produces cleaner C-44 compliance because the generating model receives a single, unambiguous format
signal per block. C-44 should pass; C-45/C-46/C-47 remain FAIL. Expected: ~35/39.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1 in document order.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools used, handoff mechanisms, storage, initiator]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure] | [daily / per-cycle / per-exception] | [downstream effect] |
| IM-02 | [second distinct failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [Named measure with current-state value or rate, declared before PHASE 1.
Both IM-IDs must be reachable from at least one B-NN Cause field.]

---

### Role Registry Gate

> GATE BLOCK: Complete before the Role Sequence Schedule and before tracing any state.
> All four anti-generic checks must clear before proceeding.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation (all four must clear before proceeding):
- [ ] No R-ID entry uses "Approver" without a domain qualifier
- [ ] No R-ID entry uses "Owner" without a named responsibility
- [ ] Each R-ID is referenced by at least one Decision Supplement block, the Role Sequence
      Schedule, and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field
- [ ] Each declared R-ID appears in at least one EX block's `Role Ref:` sub-field

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to owned phases with
> activation triggers, handoff triggers, and parallel windows. B-NN Cause fields must cite
> the blocking R-ID from this schedule (Dual-Cite Fail Condition B).

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact — not "Start"] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1 — name the artifact] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

---

### Phase Structure

For each phase in the lifecycle, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" by name.
> `Prior phase:` carries the literal phase identifier (Phase→Phase backward linkage).
> `Prior phase blocked bottleneck:` carries the B-ID from the prior exit gate (B-NN boundary
> continuity). Both are independently verifiable by string comparison.

- Entry Condition: [specific named artifact from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name]) — [verification method]
- Blocking condition: [if entry condition not met: state entered, role notified, re-entry path]
- Prior phase: [Literal identifier of the preceding phase block. Phase 1: NONE or INIT sentinel.]
- Prior phase blocked bottleneck: [B-ID from prior exit gate or NONE or N/A for Phase 1.]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition — name state, threshold breach, or missing input]
> - Trace: [states traversed; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. The B-NN block's `Exception Refs:` field (declared in
>   Bottleneck Analysis below) must list this EX block ID if Bottleneck Ref is non-NONE —
>   populate accurately for bidirectional consistency.]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID.]

Minimum 1 per phase; 3 total minimum. Bottleneck Ref and Role Ref independent; populate both.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules: Named Entry Condition required; Exits → S-ID or TERMINAL; standard Type values.

**Decision Supplement Blocks** (one per DECISION-type state):

> **DS-[S-ID] — [State Name]**: Condition / Owner R-[ID] / Branch A / Branch B / Fallback

**PHASE EXIT GATE**

> `Blocked bottleneck:` carries a B-ID. `Next phase:` carries a Phase label. Orthogonal fields.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name]) confirms all required outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Must string-match Bottleneck Analysis AND next phase's
  `Prior phase blocked bottleneck:`.]
- Next phase: [Literal identifier of subsequent phase block. Last phase: NONE or END sentinel.]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID]; **Branch 1**: [S-IDs]; **Branch 2**: [S-IDs]
- **JOIN at**: S-[ID]; **Join Condition**: AND-join / OR-join — specify and explain

### Edge Case Enumeration

Three or more, distinct from SECTION A:

> **EC-[N] — [Edge Case Name]**: Triggering Condition / Why Problematic / Correct Response: R-[ID] — [action]

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF**: Sending State S-[ID] / Receiving Process / Data Payload /
> Expected Acknowledgment / Failure Mode / Owner R-[ID]

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|

Minimum 3 rows; at least 1 AT-RISK citing a B-NN.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both Dual-Cite Fail Conditions independently.
>
> **Dual-Cite Fail Condition A** — no IM-ID literal string in Cause → fails C-39.
> **Dual-Cite Fail Condition B** — no R-ID literal string in Cause → fails C-39.
>
> B-IDs here must string-match: (1) PHASE EXIT GATE `Blocked bottleneck:` fields,
> (2) PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:` in the following phase,
> (3) EX block `Bottleneck Ref:` fields where non-NONE.
>
> Concrete format example for Evidence field:
> `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
>
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: A field containing only "see SLA ANALYSIS" or state names without
> AT-RISK row-level S-ID specificity does not satisfy.
>
> **DUAL-LOCATION REQUIREMENTS:**
> (1) Concrete named domain example in BOTH preamble AND each B-NN per-block Evidence hint.
> (2) Labeled axes (`Required format:` / `Fail condition:`) in BOTH preamble AND each hint.
>
> **B-NN→Exception Gate Check**: Every declared B-ID below must appear in at least one EX
> block's `Bottleneck Ref:`. Dark bottlenecks are gate violations. Report in CHAIN STATUS.
>
> Anti-embedding: CHAIN STATUS in its own top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field AND an Exception Refs field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream state, SLA node, or adjacent process affected]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] — [Exception Name])`
  - Fail condition: NONE declared here means this is a dark bottleneck — declared process
    failure mode with no exception-phase trace. Dark bottleneck = gate violation for the
    B-NN→Exception direction. A listed EX block ID that has no matching `Bottleneck Ref:
    B-01` in the cited EX block fails the CHAIN STATUS B-NN→Exception consistency check.
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-01, or NONE.]

---

**B-02 — [Bottleneck Name]**

- Cause: [Required: IM-ID AND R-ID literal strings.]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: [same as B-01]
  - [List each AT-RISK SLA row citing B-02.]
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] — [Exception Name])`
  - Fail condition: NONE = dark bottleneck (gate violation). Listed EX block ID without
    matching `Bottleneck Ref: B-02` in the cited EX block fails consistency check.
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-02, or NONE.]

---

**Gap Identification**

> MISSING: [step name] — [why it belongs; failure mode enabled; which phase; which IM-ID reduced]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [enumerate pairs or name gap]
- Backward (B→SLA): [enumerate or name gap]
- Exit gate consistency: [every exit gate B-ID matches a declared B-NN; name mismatch]
- Phase-boundary B-NN continuity: [exit gate B-ID matches next entry contract; list pairs]
- Phase-sequence: [every `Prior phase:` matches preceding block label; PHASE 1 NONE/INIT]
- Phase-exit-sequence: [every `Next phase:` matches subsequent block label; last phase NONE/END]
- Exception→B: [every EX `Bottleneck Ref:` B-ID matches a declared B-NN; list pairs]
- B-NN→Exception: [every declared B-ID has at least one non-NONE entry in its `Exception Refs:`
  field; each listed EX block ID string-matches an EX block with `Bottleneck Ref:` citing this
  B-ID; enumerate B-ID→EX pairs; name any B-ID with NONE in Exception Refs (dark bottleneck)
  or any listed ID whose EX block does not carry matching Bottleneck Ref (consistency failure)]
- Exception→Role: [every EX `Role Ref:` R-ID matches schedule primary owner; list pairs]
- Role→Exception: [every declared R-ID in at least one EX `Role Ref:`; list pairs; name dark roles]
- Dual-cite status: [every B-NN Cause has both IM-ID and R-ID; name missing]
- Gap (if OPEN): [unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state] |
| [failure terminal name] | FAILURE | [branch or state] |
| [cancel terminal name] | CANCEL | [branch or state] |

> Completeness check: Every exit branch must reach a declared terminal. No mid-flow endings
> without `continues-via: S-[ID]`.

---
---

## V-03 — Axis: Lifecycle Emphasis (Dedicated PHASE GATE CONTRACT SUMMARY, C-45 Target)

**Variation axis**: Lifecycle emphasis — an explicit **PHASE GATE CONTRACT SUMMARY** section is
added before PHASE 1 as a dedicated top-level block that names all three phase gate contract fields
as a declared unit, states their value types explicitly, and declares the orthogonality property.
This section is parallel to the Role Registry Gate: it declares the phase gate architecture before
any phase is traced, making the three-field system a named structural commitment honored in every
phase block. Per-block `Exception Refs:` in B-NN blocks is NOT added (C-44 not targeted). No
`IM Reference:` in PHASE ENTRY CONTRACT (C-46 not targeted). No `IM Ref:` in EX blocks (C-47
not targeted).

**Hypothesis**: C-45 requires "an explicit preamble or dedicated contract summary naming the complete
three-field phase gate system as a unit" with explicit orthogonality declaration. A dedicated
top-level section parallel to the Role Registry Gate — naming all three fields in one block with
explicit orthogonality and string-comparison declarations — is a more reliable C-45 trigger than
cross-block phrasing distributed across ENTRY CONTRACT and EXIT GATE instructions. C-44/C-46/C-47
remain FAIL. Expected: ~36/39.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1 in document order.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools used, handoff mechanisms, storage, initiator]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure] | [frequency] | [downstream effect] |
| IM-02 | [second distinct failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [Named quantified measure before PHASE 1. Both IM-IDs reachable from
at least one B-NN Cause field.]

---

### Role Registry Gate

> GATE BLOCK: Complete before Role Sequence Schedule and before tracing any state.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation (all four must clear):
- [ ] No R-ID entry uses "Approver" without a domain qualifier
- [ ] No R-ID entry uses "Owner" without a named responsibility
- [ ] Each R-ID referenced by at least one Decision Supplement block, Role Sequence Schedule,
      and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field
- [ ] Each declared R-ID appears in at least one EX block's `Role Ref:` sub-field

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to active phases,
> activation trigger, handoff trigger, and parallel windows.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event] | [completion condition] | R-[ID] or NONE | [window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1] | [completion condition] | R-[ID] or NONE | [window or NONE] |

---

### Phase Gate Contract Summary

> **DECLARED UNIT: THREE-FIELD PHASE GATE CONTRACT**
>
> This document uses a three-field phase gate contract. All three fields are declared here
> as a named unit before PHASE 1 is traced. Every phase block must carry all three fields
> in their designated structural locations.
>
> | Field Name | Location | Value Type | Traceability Direction |
> |------------|----------|------------|----------------------|
> | `Prior phase:` | PHASE ENTRY CONTRACT | Phase label (e.g., "PHASE 1 — Initiation") | Phase→Phase, backward (entry side) |
> | `Prior phase blocked bottleneck:` | PHASE ENTRY CONTRACT | B-ID (e.g., "B-01") | B-NN boundary continuity, entry side |
> | `Next phase:` | PHASE EXIT GATE | Phase label (e.g., "PHASE 2 — Credit Review") | Phase→Phase, forward (exit side) |
>
> **ORTHOGONALITY DECLARATION:**
> `Prior phase blocked bottleneck:` carries a B-ID (string pattern: "B-" followed by digits,
> e.g., "B-01"). `Next phase:` carries a Phase label (string pattern: "PHASE N — [Name]" or
> NONE/END sentinel). These two fields carry orthogonal value types independently verifiable
> by string comparison: a B-ID in `Next phase:` is a detectable format violation; a Phase
> label in `Prior phase blocked bottleneck:` is a detectable format violation. No inference
> required — the patterns are non-overlapping by construction.
>
> `Prior phase:` and `Next phase:` form a symmetric bidirectional Phase→Phase pair: entry
> contracts declare backward linkage; exit gates declare forward linkage. `Prior phase blocked
> bottleneck:` is orthogonal to both — it carries a B-ID, not a Phase label.
>
> CHAIN STATUS verifies three directions derived from this contract:
> - `Phase-sequence`: every `Prior phase:` string-matches the preceding phase block label
> - `Phase-exit-sequence`: every `Next phase:` string-matches the subsequent phase block label
> - `Phase-boundary B-NN continuity`: every exit gate `Blocked bottleneck:` B-ID string-matches
>   the next phase's `Prior phase blocked bottleneck:` field

---

### Phase Structure

For each phase in the lifecycle, produce the following five blocks in document order. All
three Phase Gate Contract fields must be populated in every phase block per the PHASE GATE
CONTRACT SUMMARY above.

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Phase Gate Contract fields 1 and 2 are required here. Field 3 (`Next phase:`) lives in
> the PHASE EXIT GATE below. `Prior phase:` carries a Phase label (backward); `Prior phase
> blocked bottleneck:` carries a B-ID (entry gate). These fields are orthogonal — see PHASE
> GATE CONTRACT SUMMARY above.

- Entry Condition: [specific named artifact from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name]) — [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase: [Literal identifier of preceding phase block. Phase 1: NONE or INIT sentinel.
  Format: "PHASE N — [Name]".]
- Prior phase blocked bottleneck: [B-ID from prior exit gate or NONE or N/A for Phase 1.
  Format: "B-NN". This field carries a B-ID — NOT a Phase label. Do not conflate with `Prior phase:`.]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition]
> - Trace: [states traversed; cite S-IDs]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason]
> - Bottleneck Ref: [B-NN or NONE. B-ID must string-match a Bottleneck Analysis identifier.
>   Preamble gate check verifies every declared B-ID appears in at least one such field.]
> - Role Ref: [R-ID of ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID.]

Minimum 1 per phase; 3 total minimum. Bottleneck Ref and Role Ref independent; populate both.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules: Named Entry Condition required; Exits → S-ID or TERMINAL; standard Type values.

**Decision Supplement Blocks** (one per DECISION-type state):

> **DS-[S-ID] — [State Name]**: Condition / Owner R-[ID] / Branch A / Branch B / Fallback

**PHASE EXIT GATE**

> Phase Gate Contract field 3 lives here: `Next phase:` (Phase label, forward).
> This field carries a Phase label — NOT a B-ID. `Blocked bottleneck:` carries a B-ID.
> These two sub-fields are orthogonal (see PHASE GATE CONTRACT SUMMARY above).

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Must string-match Bottleneck Analysis identifier AND
  next phase's `Prior phase blocked bottleneck:`. Format: "B-NN" — a B-ID, not a Phase label.]
- Next phase: [Literal identifier of the subsequent phase block. Last phase: NONE or END sentinel.
  Format: "PHASE N — [Name]". This field carries a Phase label — not a B-ID. See PHASE GATE
  CONTRACT SUMMARY orthogonality declaration for format verification rule.]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID]; **Branch 1**: [S-IDs]; **Branch 2**: [S-IDs]
- **JOIN at**: S-[ID]; **Join Condition**: AND-join / OR-join — specify and explain

### Edge Case Enumeration

Three or more, distinct from SECTION A:

> **EC-[N] — [Edge Case Name]**: Triggering Condition / Why Problematic / Correct Response: R-[ID] — [action]

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF**: Sending State S-[ID] / Receiving Process / Data Payload /
> Expected Acknowledgment / Failure Mode / Owner R-[ID]

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|

Minimum 3 rows; at least 1 AT-RISK citing a B-NN.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both Dual-Cite Fail Conditions independently.
>
> **Dual-Cite Fail Condition A** — no IM-ID literal string in Cause → fails C-39.
> **Dual-Cite Fail Condition B** — no R-ID literal string in Cause → fails C-39.
>
> B-IDs string-match: (1) EXIT GATE `Blocked bottleneck:`, (2) next phase ENTRY CONTRACT
> `Prior phase blocked bottleneck:`, (3) EX block `Bottleneck Ref:` where non-NONE.
>
> Concrete format example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: Field containing only "see SLA ANALYSIS" or no AT-RISK row-level S-ID
> specificity does not satisfy.
>
> **DUAL-LOCATION REQUIREMENTS:**
> (1) Concrete example in BOTH preamble AND each per-block Evidence hint.
> (2) Labeled axes in BOTH preamble AND each per-block Evidence hint.
>
> **B-NN→Exception Gate Check**: Every declared B-ID must appear in at least one EX block's
> `Bottleneck Ref:`. Dark bottlenecks are gate violations. Report in CHAIN STATUS.
>
> Anti-embedding: CHAIN STATUS in its own top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream state, SLA node, or adjacent process affected]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: No AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01.]

---

**B-02 — [Bottleneck Name]**

- Cause: [Required: IM-ID AND R-ID literal strings.]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: [same as B-01]
  - [List each AT-RISK SLA row citing B-02.]

---

**Gap Identification**

> MISSING: [step name] — [why it belongs; failure mode enabled; which phase; which IM-ID reduced]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [enumerate pairs or name gap]
- Backward (B→SLA): [enumerate or name gap]
- Exit gate consistency: [every exit gate B-ID matches a declared B-NN; name mismatch]
- Phase-boundary B-NN continuity: [exit gate B-ID matches next entry contract; list pairs]
- Phase-sequence: [every `Prior phase:` matches preceding block label; PHASE 1 NONE/INIT]
- Phase-exit-sequence: [every `Next phase:` matches subsequent block label; last phase NONE/END]
- Exception→B: [every EX `Bottleneck Ref:` B-ID matches a declared B-NN; list pairs]
- B-NN→Exception: [every declared B-ID appears in at least one EX block's `Bottleneck Ref:`; enumerate B-ID→EX pairs; name dark bottlenecks]
- Exception→Role: [every EX `Role Ref:` R-ID matches schedule primary owner; list pairs]
- Role→Exception: [every declared R-ID in at least one EX `Role Ref:`; list pairs; name dark roles]
- Dual-cite status: [every B-NN Cause has both IM-ID and R-ID; name missing]
- Gap (if OPEN): [unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state] |
| [failure terminal name] | FAILURE | [branch or state] |
| [cancel terminal name] | CANCEL | [branch or state] |

> Completeness check: Every exit branch must reach a declared terminal.

---
---

## V-04 — Axis: Inertia Framing (Explicit IM Reference in PHASE ENTRY CONTRACT, C-46 Target)

**Variation axis**: Inertia framing — each PHASE ENTRY CONTRACT carries an explicit named
`IM Reference:` sub-field listing the IM-IDs from INCUMBENT BASELINE whose failure modes represent
active risks entering that phase. This opens the Baseline→Phase traceability direction as a
per-phase navigable lookup: a reader can jump directly from any PHASE ENTRY CONTRACT to the INCUMBENT
BASELINE rows that motivated that phase's entry controls. NONE sentinel for phases with no active IM
risk at entry. IM-IDs must match literal identifiers from the INCUMBENT BASELINE table — string
comparison only, no inference. No PHASE GATE CONTRACT SUMMARY (C-45 not targeted). No per-block
`Exception Refs:` in B-NN blocks (C-44 not targeted). No `IM Ref:` in EX blocks (C-47 not targeted).

**Hypothesis**: C-46 requires a named `IM Reference:` sub-field in the PHASE ENTRY CONTRACT block
— not at SECTION A level as in R14 V-05's "Incumbent reference" comment, but in the entry contract
itself. Adding this single named field to the PHASE ENTRY CONTRACT instruction, with explicit IM-ID
format requirement and NONE sentinel, scores C-46. Baseline→Phase direction appears in CHAIN STATUS.
C-44/C-45/C-47 remain FAIL. Expected: ~37/39.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1 in document order.
> The IM-IDs assigned here are the anchor identifiers for the `IM Reference:` sub-field in
> each PHASE ENTRY CONTRACT below. Every phase entry carries an explicit IM Reference field
> listing which incumbent failure modes are active risks entering that phase.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools used (spreadsheets, email, phone), handoff
mechanisms, where records are stored, who initiates the process manually. Include the primary
point where the incumbent fails under volume or time pressure.]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure — the one most visible to the domain team] | [daily / per-cycle / per-exception] | [downstream effect on SLA or accuracy] |
| IM-02 | [second distinct failure mode — different process layer from IM-01] | [frequency] | [downstream effect] |

**Cost of no action**: [Named measure with current-state value or rate, declared before PHASE 1.
Must be specific enough to anchor B-NN Cause fields. Both IM-IDs must be reachable from at least
one B-NN Cause field. Example: "Average credit approval cycle time: 5.8 days vs 3-day SLA" or
"Manual matching error rate: 12% per period."]

---

### Role Registry Gate

> GATE BLOCK: Complete before the Role Sequence Schedule and before tracing any state.
> All four anti-generic checks must clear before proceeding.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation (all four must clear before proceeding):
- [ ] No R-ID entry uses "Approver" without a domain qualifier
- [ ] No R-ID entry uses "Owner" without a named responsibility
- [ ] Each R-ID is referenced by at least one Decision Supplement block, the Role Sequence
      Schedule, and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field
- [ ] Each declared R-ID appears in at least one EX block's `Role Ref:` sub-field

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to owned phases with
> activation triggers, handoff triggers, and parallel windows. B-NN Cause fields must cite
> the blocking R-ID from this schedule (Dual-Cite Fail Condition B).

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact — not "Start"] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1 — name the artifact] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

---

### Phase Structure

For each phase in the lifecycle, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" by name.
> Three sub-fields are required in the entry contract:
> `Prior phase:` carries the literal phase identifier (Phase→Phase backward linkage).
> `Prior phase blocked bottleneck:` carries the B-ID from the prior exit gate (B-NN boundary
> continuity). `IM Reference:` lists IM-IDs from INCUMBENT BASELINE whose failure modes are
> active risks entering this phase (Baseline→Phase traceability).
> All three are independently verifiable by string comparison.

- Entry Condition: [specific named artifact from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name — must match Role Sequence Schedule primary owner for this phase]) — [verification method]
- Blocking condition: [if entry condition not met: which state is entered, which role notified, re-entry path]
- Prior phase: [Literal identifier of the preceding phase block, e.g., "PHASE 1 — Initiation".
  Phase 1 carries NONE or INIT as sentinel. Must string-match preceding phase block label.]
- Prior phase blocked bottleneck: [B-ID from prior exit gate `Blocked bottleneck:` or NONE
  or N/A for Phase 1. Must string-match prior exit gate AND B-NN block identifier.]
- IM Reference: [List every IM-ID from INCUMBENT BASELINE whose failure mode represents an
  active risk entering this phase. Use exact IM-ID identifiers as declared in the INCUMBENT
  BASELINE table (e.g., "IM-01, IM-02"). If no incumbent failure mode is an active risk at
  this phase's entry point, write NONE. String comparison only — IM-IDs must literal-match
  INCUMBENT BASELINE table identifiers. No inference. Example: "IM-01 (manual reconciliation
  gap — active entry risk because pre-condition check relies on manually produced artifact
  vulnerable to this failure mode)."]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition — name the state, threshold breach, or missing input]
> - Trace: [states traversed; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. Preamble gate check verifies every declared B-ID appears
>   in at least one such field — populate accurately.]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID.]

Minimum 1 exception trace per phase; 3 total minimum.
Every declared R-ID must appear in at least one EX block Role Ref.
Bottleneck Ref and Role Ref are independent sub-fields; populate both.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules: Named Entry Condition required; Exits → S-ID or TERMINAL; standard Type values.

**Decision Supplement Blocks** (one per DECISION-type state):

> **DS-[S-ID] — [State Name]**: Condition / Owner R-[ID] / Branch A / Branch B / Fallback

**PHASE EXIT GATE**

> `Blocked bottleneck:` carries a B-ID. `Next phase:` carries a Phase label. Orthogonal fields.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name]) confirms all required outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Must string-match Bottleneck Analysis AND next phase's
  `Prior phase blocked bottleneck:`.]
- Next phase: [Literal identifier of subsequent phase. Last phase: NONE or END sentinel.]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID]; **Branch 1**: [S-IDs]; **Branch 2**: [S-IDs]
- **JOIN at**: S-[ID]; **Join Condition**: AND-join / OR-join — specify and explain

### Edge Case Enumeration

Three or more, distinct from SECTION A:

> **EC-[N] — [Edge Case Name]**: Triggering Condition / Why Problematic / Correct Response: R-[ID] — [action]

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF**: Sending State S-[ID] / Receiving Process / Data Payload /
> Expected Acknowledgment / Failure Mode / Owner R-[ID]

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|

Minimum 3 rows; at least 1 AT-RISK citing a B-NN.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both Dual-Cite Fail Conditions independently.
>
> **Dual-Cite Fail Condition A** — no IM-ID literal string in Cause → fails C-39.
> **Dual-Cite Fail Condition B** — no R-ID literal string in Cause → fails C-39.
>
> B-IDs here must string-match: (1) PHASE EXIT GATE `Blocked bottleneck:` fields,
> (2) PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:` in the following phase,
> (3) EX block `Bottleneck Ref:` fields where non-NONE.
>
> Concrete format example for Evidence field:
> `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
>
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: A field containing only "see SLA ANALYSIS" or state names without
> AT-RISK row-level S-ID specificity does not satisfy.
>
> **DUAL-LOCATION REQUIREMENTS:**
> (1) Concrete named domain example in BOTH preamble AND each B-NN per-block Evidence hint.
> (2) Labeled axes (`Required format:` / `Fail condition:`) in BOTH preamble AND each hint.
>
> **B-NN→Exception Gate Check**: Every declared B-ID below must appear in at least one EX
> block's `Bottleneck Ref:`. Dark bottlenecks are gate violations. Report in CHAIN STATUS.
>
> Anti-embedding: CHAIN STATUS in its own top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream state, SLA node, or adjacent process affected]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: No AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01.]

---

**B-02 — [Bottleneck Name]**

- Cause: [Required: IM-ID AND R-ID literal strings.]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: [same as B-01]
  - [List each AT-RISK SLA row citing B-02.]

---

**Gap Identification**

> MISSING: [step name] — [why it belongs; failure mode enabled; which phase; which IM-ID reduced]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [enumerate pairs or name gap]
- Backward (B→SLA): [enumerate or name gap]
- Exit gate consistency: [every exit gate B-ID matches a declared B-NN; name mismatch]
- Phase-boundary B-NN continuity: [exit gate B-ID matches next entry contract; list pairs]
- Phase-sequence: [every `Prior phase:` matches preceding block label; PHASE 1 NONE/INIT]
- Phase-exit-sequence: [every `Next phase:` matches subsequent block label; last phase NONE/END]
- Exception→B: [every EX `Bottleneck Ref:` B-ID matches a declared B-NN; list pairs]
- B-NN→Exception: [every declared B-ID appears in at least one EX block's `Bottleneck Ref:`; enumerate B-ID→EX pairs; name dark bottlenecks]
- Exception→Role: [every EX `Role Ref:` R-ID matches schedule primary owner; list pairs]
- Role→Exception: [every declared R-ID in at least one EX `Role Ref:`; list pairs; name dark roles]
- Dual-cite status: [every B-NN Cause has both IM-ID and R-ID; name missing]
- Baseline→Phase: [every PHASE ENTRY CONTRACT `IM Reference:` field contains only IM-IDs
  declared in INCUMBENT BASELINE table; list phase→IM-ID pairs; name any phase whose IM Reference
  field contains a non-declared IM-ID string or is absent; phases with NONE sentinel are CLOSED
  for this direction]
- Gap (if OPEN): [unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state] |
| [failure terminal name] | FAILURE | [branch or state] |
| [cancel terminal name] | CANCEL | [branch or state] |

> Completeness check: Every exit branch must reach a declared terminal.

---
---

## V-05 — Combination: Output Format + Lifecycle Emphasis + Inertia Framing (C-44 + C-45 + C-46 + C-47)

**Variation axis**: Output format + Lifecycle emphasis + Inertia framing — maximum structural
density for all four R15 criteria. (1) Isolated per-block `Exception Refs:` named instruction block
in each B-NN block (V-02 axis, C-44). (2) Dedicated PHASE GATE CONTRACT SUMMARY section before PHASE 1
(V-03 axis, C-45). (3) Named `IM Reference:` sub-field in every PHASE ENTRY CONTRACT (V-04 axis,
C-46). (4) Named `IM Ref:` sub-field in every SECTION A EX block alongside existing `Bottleneck Ref:`
(new for R15, C-47). EX blocks become triple-citation blocks: Role (C-40 via `Role Ref:`), B-NN
(C-42 via `Bottleneck Ref:`), and Baseline (C-47 via `IM Ref:`). CHAIN STATUS gains a
`Baseline→Exception` direction, completing the full traceability graph.

**Hypothesis**: V-05 is the minimum R15 configuration to achieve C-44, C-45, C-46, and C-47
simultaneously. Each structural addition is architecturally independent: C-44 lives in B-NN blocks,
C-45 lives in the PHASE GATE CONTRACT SUMMARY, C-46 lives in PHASE ENTRY CONTRACTs, C-47 lives in
EX blocks. The four additions do not interact structurally — they extend different sections of the
document with new named fields. If all four pass, single-axis results from V-02/V-03/V-04 will
confirm each criterion is independently sufficient. Expected: 39/39 = 10.000.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1 in document order.
> This section is the inertia reference: IM-IDs assigned here are anchor identifiers for
> (1) `IM Reference:` in every PHASE ENTRY CONTRACT and (2) `IM Ref:` in every SECTION A EX
> block. Every exception trace and bottleneck must be traceable back to a named IM-ID.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools used (spreadsheets, email, phone), handoff
mechanisms, where records are stored, who initiates the process manually. Include the primary
failure point under volume or time pressure.]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure — the one most visible to the domain team] | [daily / per-cycle / per-exception] | [downstream effect on SLA or accuracy] |
| IM-02 | [second distinct failure mode — different process layer from IM-01] | [frequency] | [downstream effect] |

**Cost of no action**: [Named measure with current-state value or rate, declared before PHASE 1.
Both IM-IDs must be reachable from at least one B-NN Cause field. Example: "Average credit
approval cycle time: 5.8 days vs 3-day SLA — IM-01 primary driver" or "Manual matching error
rate: 12% per period, IM-02 primary driver."]

---

### Role Registry Gate

> GATE BLOCK: Complete before the Role Sequence Schedule and before tracing any state.
> All four anti-generic checks must clear before proceeding.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation (all four must clear before proceeding):
- [ ] No R-ID entry uses "Approver" without a domain qualifier
- [ ] No R-ID entry uses "Owner" without a named responsibility
- [ ] Each R-ID is referenced by at least one Decision Supplement block, the Role Sequence
      Schedule, and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field
- [ ] Each declared R-ID appears in at least one EX block's `Role Ref:` sub-field — R-IDs
      with no observable EX trace are "dark" roles and constitute a gate violation

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to owned phases with
> activation triggers, handoff triggers, and parallel windows. B-NN Cause fields must cite
> the blocking R-ID from this schedule (Dual-Cite Fail Condition B). R-IDs in EX block
> `Role Ref:` must match the schedule entry for the enclosing phase. Every declared R-ID
> must appear in at least one EX block Role Ref — the Role Registry Gate fourth check enforces this.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact — not "Start"] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1 — name the artifact] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

Rules: Every phase has a Primary Owner. Activation Trigger for Phase 1 must name an external
event or prior-process artifact. Every R-ID here must match a Role Registry Gate entry.

---

### Phase Gate Contract Summary

> **DECLARED UNIT: THREE-FIELD PHASE GATE CONTRACT**
>
> This document uses a three-field phase gate contract. All three fields are named here as a
> declared unit before PHASE 1 is traced. Every phase block must carry all three fields in
> their designated structural locations. A fourth field (`IM Reference:`) augments PHASE ENTRY
> CONTRACTs with Baseline→Phase traceability; it is not part of the three-field gate contract
> but is required in every PHASE ENTRY CONTRACT block.
>
> | Field Name | Location | Value Type | Traceability Direction |
> |------------|----------|------------|----------------------|
> | `Prior phase:` | PHASE ENTRY CONTRACT | Phase label (e.g., "PHASE 1 — Initiation") | Phase→Phase, backward (entry side) |
> | `Prior phase blocked bottleneck:` | PHASE ENTRY CONTRACT | B-ID (e.g., "B-01") | B-NN boundary continuity, entry side |
> | `Next phase:` | PHASE EXIT GATE | Phase label (e.g., "PHASE 2 — Credit Review") | Phase→Phase, forward (exit side) |
>
> **ORTHOGONALITY DECLARATION:**
> `Prior phase blocked bottleneck:` carries a B-ID (string pattern: "B-" followed by digits,
> e.g., "B-01"). `Next phase:` carries a Phase label (string pattern: "PHASE N — [Name]" or
> NONE/END sentinel). These two fields carry orthogonal value types independently verifiable
> by string comparison: a B-ID in `Next phase:` is a detectable format violation; a Phase
> label in `Prior phase blocked bottleneck:` is a detectable format violation. No inference
> required — the patterns are non-overlapping by construction.
>
> `Prior phase:` and `Next phase:` form a symmetric bidirectional Phase→Phase pair.
> `Prior phase blocked bottleneck:` is orthogonal to both — B-ID, not Phase label.
>
> CHAIN STATUS verifies three gate-contract directions:
> - `Phase-sequence`: every `Prior phase:` string-matches the preceding phase block label
> - `Phase-exit-sequence`: every `Next phase:` string-matches the subsequent phase block label
> - `Phase-boundary B-NN continuity`: every exit gate `Blocked bottleneck:` B-ID string-matches
>   the next phase's `Prior phase blocked bottleneck:` field

---

### Phase Structure

For each phase in the lifecycle, produce the following five blocks in document order. All
three Phase Gate Contract fields must be populated in every phase block per the PHASE GATE
CONTRACT SUMMARY above. `IM Reference:` must additionally appear in every PHASE ENTRY CONTRACT.

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Phase Gate Contract fields 1 and 2 live here; field 3 (`Next phase:`) lives in PHASE EXIT GATE.
> `IM Reference:` is a fourth required sub-field providing Baseline→Phase traceability.
> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" by name.
> All four sub-fields are independently verifiable by string comparison.

- Entry Condition: [specific named artifact from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) — [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase: [Literal identifier of preceding phase block, e.g., "PHASE 1 — Initiation".
  Phase 1: NONE or INIT sentinel. Must string-match preceding phase block label. Format: "PHASE N — [Name]".]
- Prior phase blocked bottleneck: [B-ID from prior exit gate `Blocked bottleneck:` or NONE
  or N/A for Phase 1. Format: "B-NN". Must string-match prior exit gate AND B-NN block identifier.
  This field carries a B-ID — NOT a Phase label. Do not conflate with `Prior phase:`.]
- IM Reference: [List every IM-ID from INCUMBENT BASELINE whose failure mode represents an
  active risk entering this phase. Use exact IM-ID identifiers as declared in the INCUMBENT
  BASELINE table (e.g., "IM-01, IM-02"). If no incumbent failure mode is an active risk at
  this phase's entry point, write NONE. IM-IDs must literal-match INCUMBENT BASELINE table
  identifiers — string comparison only, no inference. This sub-field opens the Baseline→Phase
  traceability direction: a reader can navigate directly from this phase's entry contract to
  the INCUMBENT BASELINE rows whose failure modes motivated the entry controls for this phase.
  Example: "IM-01 (manual reconciliation gap — active entry risk: pre-condition artifact
  produced manually and vulnerable to IM-01 failure mode before this phase begins)."]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition — name the state, threshold breach, or missing input]
> - Trace: [path of states from trigger to resolution or terminal; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason this failure mode matters]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. The B-NN block's `Exception Refs:` field must list this
>   EX block ID if Bottleneck Ref is non-NONE — populate accurately for chain consistency.
>   NONE only if no declared bottleneck was causal. This is the Exception→B-NN traceability
>   artifact (C-42 direction).]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID
>   matching the schedule's Primary Owner entry for the enclosing phase. Free-text without
>   R-ID fails. R-ID absent from schedule fails.]
> - IM Ref: [IM-ID from INCUMBENT BASELINE whose failure mode this exception traces, or NONE.
>   Use exact IM-ID identifier as declared in the INCUMBENT BASELINE table (e.g., "IM-01").
>   This sub-field completes the dual-citation architecture: `Bottleneck Ref:` links this EX
>   block to a B-NN (C-42); `IM Ref:` links this EX block directly to the INCUMBENT BASELINE
>   failure mode (C-47). Together they make this EX block the convergence point for the
>   B-NN↔Exception and Baseline↔Exception traceability chains simultaneously.
>   NONE if no incumbent baseline failure mode is directly traceable to this exception.
>   String comparison only — IM-ID must literal-match INCUMBENT BASELINE table identifier.
>   Example: "IM-01 — this exception is the process-visible manifestation of the incumbent
>   manual reconciliation failure mode entering Phase 2."]

Minimum 1 exception trace per phase; 3 total minimum.
Every declared R-ID in the Role Registry Gate must appear in at least one EX block Role Ref.
Bottleneck Ref, Role Ref, and IM Ref are independent sub-fields; populate all three for every EX block.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules: Named Entry Condition required; Exits → S-ID or TERMINAL; standard Type values.

**Decision Supplement Blocks** (one per DECISION-type state in this phase):

> **DS-[S-ID] — [State Name]**: Condition / Owner R-[ID] / Branch A / Branch B / Fallback

**PHASE EXIT GATE**

> Phase Gate Contract field 3 lives here: `Next phase:` (Phase label, forward).
> `Blocked bottleneck:` carries a B-ID. These two sub-fields are orthogonal — see PHASE GATE
> CONTRACT SUMMARY above.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Must string-match Bottleneck Analysis identifier AND
  next phase's `Prior phase blocked bottleneck:`. Format: "B-NN" — a B-ID, not a Phase label.]
- Next phase: [Literal identifier of the subsequent phase block. Last phase: NONE or END.
  Format: "PHASE N — [Name]". This field carries a Phase label — not a B-ID. See PHASE GATE
  CONTRACT SUMMARY orthogonality declaration.]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID]; **Branch 1**: [S-IDs]; **Branch 2**: [S-IDs]
- **JOIN at**: S-[ID]; **Join Condition**: AND-join / OR-join — specify and explain

### Edge Case Enumeration

Three or more, distinct from SECTION A:

> **EC-[N] — [Edge Case Name]**: Triggering Condition / Why Problematic / Correct Response: R-[ID] — [action]

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF**: Sending State S-[ID] / Receiving Process / Data Payload /
> Expected Acknowledgment / Failure Mode / Owner R-[ID]

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|

Minimum 3 rows; at least 1 AT-RISK citing a B-NN.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both Dual-Cite Fail Conditions independently.
>
> **Dual-Cite Fail Condition A** — Cause field contains no IM-ID literal string (e.g., "IM-01"):
> fails C-39. Verify: search Cause field for "IM-" followed by digits. Absence → fail.
>
> **Dual-Cite Fail Condition B** — Cause field contains no R-ID literal string (e.g., "R-01"):
> fails C-39. Verify: search Cause field for "R-" followed by digits. Absence → fail.
>
> B-IDs assigned here must string-match ALL of: (1) PHASE EXIT GATE `Blocked bottleneck:`
> fields, (2) PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:` in the following phase,
> and (3) EX block `Bottleneck Ref:` fields where non-NONE.
>
> Concrete format example for Evidence field:
> `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
>
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: A field containing only "see SLA ANALYSIS" or state names without
> AT-RISK row-level S-ID specificity does not satisfy.
>
> **DUAL-LOCATION REQUIREMENTS:**
> (1) Concrete named domain example must appear in BOTH this preamble AND each B-NN per-block
> Evidence hint.
> (2) Labeled axes (`Required format:` / `Fail condition:`) must appear in BOTH this preamble
> AND each B-NN per-block Evidence hint.
>
> **B-NN→Exception Gate Check**: Every declared B-ID below must appear in at least one EX
> block's `Bottleneck Ref:` sub-field across all phases. A B-ID absent from all EX blocks is
> a "dark bottleneck" — declared failure mode with no exception-phase trace. Dark bottlenecks
> are gate violations. Report result in CHAIN STATUS `B-NN→Exception` direction.
>
> Anti-embedding: Declare CHAIN STATUS in its own dedicated top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field AND an Exception Refs field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).
  Example: "IM-01 (manual reconciliation gap) combined with R-02 (GL Manager) period-close
  unavailability — approval queue at S-05. 'IM-01' satisfies A; 'R-02' satisfies B."]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream state, SLA node, or adjacent process affected]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] — [Exception Name])`
  - Fail condition: NONE declared here means this is a dark bottleneck — declared process
    failure mode with no exception-phase trace. Dark bottleneck = gate violation for the
    B-NN→Exception direction. A listed EX block ID that has no matching `Bottleneck Ref:
    B-01` in the cited EX block fails the CHAIN STATUS B-NN→Exception consistency check.
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-01, or NONE.]

---

**B-02 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string AND R-ID literal string.]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: [same as B-01]
  - [List each AT-RISK SLA row citing B-02.]
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] — [Exception Name])`
  - Fail condition: NONE = dark bottleneck (gate violation). Listed EX block ID without
    matching `Bottleneck Ref: B-02` fails consistency check.
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-02, or NONE.]

---

**Gap Identification**

> MISSING: [step name] — [why it belongs; failure mode enabled; which phase; which IM-ID reduced]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name gap]
- Backward (B→SLA): [every B-NN Evidence field lists AT-RISK SLA rows; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID matches a declared B-NN; name any mismatch]
- Phase-boundary B-NN continuity: [every exit gate B-ID matches next phase's `Prior phase blocked bottleneck:`; list pairs or name break]
- Phase-sequence: [every PHASE ENTRY CONTRACT `Prior phase:` matches preceding phase block label; PHASE 1 carries NONE/INIT; list pairs or name mismatch]
- Phase-exit-sequence: [every PHASE EXIT GATE `Next phase:` matches subsequent phase block label; last phase carries NONE/END; list pairs or name mismatch]
- Exception→B: [every EX block `Bottleneck Ref:` B-ID (non-NONE) matches a declared B-NN; list EX→B-NN pairs or name unresolved block]
- B-NN→Exception: [every declared B-ID has at least one non-NONE entry in its `Exception Refs:`
  field; each listed EX block ID string-matches an EX block with `Bottleneck Ref:` citing this
  B-ID; enumerate B-ID→EX pairs; name any B-ID with NONE in Exception Refs (dark bottleneck)
  or any listed ID whose EX block does not carry matching Bottleneck Ref (consistency failure)]
- Exception→Role: [every EX block `Role Ref:` R-ID matches ROLE SEQUENCE SCHEDULE primary owner; list EX→R-ID pairs or name mismatch]
- Role→Exception: [every declared R-ID appears in at least one EX block `Role Ref:`; list R-ID→EX pairs; name dark roles]
- Dual-cite status: [every B-NN Cause has both IM-ID and R-ID; name any block missing either]
- Baseline→Phase: [every PHASE ENTRY CONTRACT `IM Reference:` field contains only IM-IDs declared
  in INCUMBENT BASELINE; list phase→IM-ID pairs; phases with NONE sentinel are CLOSED for this
  direction; name any phase whose IM Reference contains a non-declared IM-ID or is absent]
- Baseline→Exception: [every SECTION A EX block `IM Ref:` field contains only IM-IDs declared
  in INCUMBENT BASELINE or NONE sentinel; list EX→IM-ID pairs; name any EX block whose IM Ref
  contains a non-declared IM-ID or is absent (dark exception — baseline failure mode not traceable
  to this exception block); EX blocks with NONE sentinel are CLOSED for this direction]
- Gap (if OPEN): [unresolved direction and unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state that reaches it] |
| [failure terminal name] | FAILURE | [branch or state that reaches it] |
| [cancel terminal name] | CANCEL | [branch or state that reaches it] |

> Completeness check: Every exit branch in every SECTION B state table must reach one of the
> declared terminals. No branch may end at a non-terminal state without `continues-via: S-[ID]`.

---
