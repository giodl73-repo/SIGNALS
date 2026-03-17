# flow-lifecycle — Round 11 Variations (Rubric v11)

**Rubric**: v11 · 39 criteria (31 aspirational) · Ceiling entering R11: 31/31 (R10 V-04/V-05
cracked C-37; R10 V-01/V-04/V-05 cracked C-38; R10 V-01 compound cracked C-39, V-04/V-05
confirmed)

**Open criteria entering R11**: None — C-37, C-38, C-39 all cracked. All five R11 variations
carry the full architecture needed to pass C-01 through C-39. Variation axes probe C-40+.

**Evidence from R10 excellence (C-37, C-38, C-39):**

- **C-37 signal**: PHASE EXIT GATE carries `Blocked bottleneck: B-NN or NONE` as a named
  sub-field. B-ID in the exit gate is a forward reference: it is declared before Bottleneck
  Analysis and must string-match the B-NN identifier in that section. Traceability direction:
  Phase→B-NN.
- **C-38 signal**: ROLE SEQUENCE SCHEDULE is declared after Role Registry Gate and before PHASE 1.
  It maps each R-ID to a phase with an Activation Trigger, Handoff Trigger, and Parallel Window.
  Traceability direction: Role→Phase verifiable by string comparison (R-02 in schedule matches
  R-02 in exit gate's Exit verification field).
- **C-39 signal**: B-NN Cause field cites both an IM-ID literal string (Baseline→B-NN direction,
  from C-34) and an R-ID literal string (Role→B-NN direction, from C-38). When "IM-01" appears
  in INCUMBENT BASELINE, "R-02" appears in ROLE SEQUENCE SCHEDULE, and both appear in B-01 Cause,
  three artifacts are linked by two string comparisons simultaneously.

**Rubric note (C-40 / C-41 probes):**

C-39 closes the Baseline→B-NN and Role→B-NN directions. Two unexplored traceability directions
remain at the boundary of the current architecture:
- **C-40 probe (Exception→B-NN)**: EX-NNLetter blocks currently trace to terminal states but do
  not cite the bottleneck that enables the exception. Adding `Bottleneck Ref: B-NN or NONE` to
  every EX block creates a fourth orthogonal traceability direction verifiable by string comparison.
- **C-41 probe (Phase-boundary B-NN continuity)**: The PHASE EXIT GATE declares a forward-reference
  B-ID (C-37). If the next phase's PHASE ENTRY CONTRACT mirrors this with a back-reference to the
  same B-ID, the bottleneck is traceable across the phase boundary in both directions without
  navigating the full Bottleneck Analysis section.

**Variation axes chosen:**

- **Axis A — C-39 Dual-Cite Explicitness**: The Bottleneck Analysis preamble and each B-NN block
  Cause hint split the C-39 requirement into two discrete, independently verifiable fail conditions:
  one for absent IM-ID citation and one for absent R-ID citation. Probes whether separating the
  two fail conditions from a combined statement into named conditions increases reliability of
  dual citation.
- **Axis B — Exception-Bottleneck Citation**: Each EX-NNLetter block gains `Bottleneck Ref: B-NN
  or NONE`. CHAIN STATUS gains an Exception→B direction. Probes C-40.
- **Axis C — Phase Entry Blocked-Bottleneck Back-Reference**: PHASE ENTRY CONTRACT gains `Prior
  phase blocked bottleneck:` citing the B-ID from the prior phase's PHASE EXIT GATE `Blocked
  bottleneck` field (or NONE if that field was NONE). Probes C-41.

| Variation | Axis | Hypothesis |
|-----------|------|-----------|
| V-01 | A only: C-39 dual-cite explicit fail conditions | Splitting the preamble's combined C-39 statement into two named fail conditions — one for IM-ID absence, one for R-ID absence — makes each check independently satisfiable and surfaces partial citations as unambiguous failures, increasing the probability that both literal strings appear in every Cause field |
| V-02 | B only: Exception-Bottleneck citation | Adding `Bottleneck Ref: B-NN or NONE` to every EX block creates a fourth traceability direction (Exception→B-NN) orthogonal to SLA↔B-NN, Baseline→B-NN, and Role→B-NN — the chain EX-2A cites B-02; B-02 Evidence cites S-07; S-07 is AT-RISK in SLA Analysis is verifiable by three string comparisons, potentially surfacing C-40 |
| V-03 | C only: Phase Entry Blocked-Bottleneck back-reference | A `Prior phase blocked bottleneck:` field in PHASE ENTRY CONTRACT mirrors the prior phase's PHASE EXIT GATE `Blocked bottleneck` B-ID; when Phase N exit gate says "B-02" and Phase N+1 entry contract says "B-02 (inherited from Phase N exit gate)", the bottleneck is round-trip traceable across the phase boundary without navigating Bottleneck Analysis, potentially surfacing C-41 |
| V-04 | A + B: Dual-cite explicitness + Exception-Bottleneck citation | Explicit dual-cite fail conditions (C-39 reliability) compound with EX-block bottleneck citation (C-40 probe): when every Cause field is verified to contain IM-ID and R-ID, and every EX block cites the same B-IDs, a reviewer can navigate from any exception trace to its root cause via three string comparisons (EX→B-NN→IM-ID+R-ID) with no inference at any step |
| V-05 | A + B + C: All three axes | Maximum traceability density across all directions: dual-cite Cause fields, Exception→B-NN links, and Phase-boundary B-NN continuity — tests whether a six-artifact cross-reference system (INCUMBENT BASELINE / ROLE SEQUENCE SCHEDULE / EX blocks / PHASE ENTRY CONTRACT / PHASE EXIT GATE / B-NN blocks) remains internally consistent and whether the compound architecture surfaces both C-40 and C-41 simultaneously |

---

## V-01 — Axis A: C-39 Dual-Cite Explicit Fail Conditions

**Variation axis**: Lifecycle emphasis — the Bottleneck Analysis preamble replaces the combined
C-39 requirement ("cite IM-ID and R-ID") with two discrete named fail conditions, one for each
missing citation. Each B-NN block Cause hint likewise declares two independent fail lines. This
makes the dual-cite requirement unambiguously verifiable: a reviewer tests two independent
string-presence conditions rather than a combined judgment.

**Hypothesis**: C-39 requires both IM-ID and R-ID to appear as literal strings in the Cause
field. When the preamble says "cite (1) IM-ID and (2) R-ID", a partial citation (IM-ID only)
can be read as an attempt that missed the second half. When the preamble instead declares
`Fail condition A: Cause contains no IM-ID literal string — fails C-39` and
`Fail condition B: Cause contains no R-ID literal string — fails C-39` as separate named lines,
the partial-citation ambiguity collapses. Each condition is testable by a single grep against the
Cause text. This structural change does not add new artifacts — it makes the existing C-39
contract maximally precise.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must cite at least one IM-ID
> from this table by literal string. The quantified metric must appear before the first PHASE
> block in document order. A metric declared after PHASE 1 begins fails C-35.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools used (spreadsheets, email, phone), handoff
mechanisms, where records are stored, who initiates the process manually]

**Incumbent failure modes** (assign IM-ID to each):

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure in the manual process] | [daily / per-cycle / per-exception] | [what breaks downstream when this occurs] |
| IM-02 | [second distinct failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [Named measure with current-state value or rate, declared before PHASE 1.
Example: "Average rejection cycle time: 3.2 days per rejected invoice" or
"Credit approval rework rate: 18% per period." Both IM-IDs above must be reachable from at
least one B-NN Cause field in Bottleneck Analysis below.]

---

### Role Registry Gate

> GATE BLOCK: Complete before the Role Sequence Schedule and before tracing any state.
> Do not begin any phase until all R-ID entries are filled and all three anti-generic checks pass.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation (all three must clear before proceeding):
- [ ] No R-ID entry uses "Approver" without a domain qualifier
- [ ] No R-ID entry uses "Owner" without a named responsibility
- [ ] Each R-ID is referenced by at least one Decision Supplement block, the Role Sequence
      Schedule, and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to its active phases,
> activation trigger, handoff trigger, and any parallel windows. B-NN Cause fields must cite
> the blocking R-ID from this schedule when role unavailability contributes to delay — this
> is the R-ID literal string required by Dual-Cite Fail Condition B (see Bottleneck Analysis).

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact — not "Start"] | [specific completion condition — "approval received" fails; "Credit Limit Approved with attached credit memo" passes] | R-[ID] or NONE | [concurrent activity window or NONE] |
| Phase 2 | R-[ID] | [handoff received from phase 1 — name the artifact] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

Rules:
- Every phase must have a Primary Owner.
- Activation Trigger for Phase 1 must name an external event or prior-process artifact.
- Handoff Trigger must be specific enough that a reviewer can determine the exact moment of transfer.
- Parallel windows must declare start/end states (S-IDs) when known.
- Every R-ID in this schedule must match an entry in the Role Registry Gate.

---

### Phase Structure

For each phase in the lifecycle, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> This gate must be completed before SECTION A or SECTION B for this phase.
> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" field
> by name — "previous phase complete" fails.

- Entry Condition: [specific named artifact or state record from prior phase's Required outputs field]
- Pre-condition check: R-[ID] ([role name — must match Role Sequence Schedule primary owner for this phase]) — [how they verify the entry condition is met]
- Blocking condition: [if entry condition is not met: which state is entered, which role is notified, what re-entry path applies]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition that causes deviation — name the state, threshold breach, or missing input]
> - Trace: [path of states traversed from trigger to resolution or terminal; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason this failure mode matters for this process type]

Minimum 1 exception trace per phase. Minimum 3 exception traces total across all phases.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules:
- Every state must have a named Entry Condition. "Ready" or "Previous step complete" fails.
- Every Exit must reference a destination S-ID or carry the label TERMINAL.
- Type values: NORMAL / DECISION / PARALLEL-FORK / PARALLEL-JOIN / EXCEPTION / TERMINAL

**Decision Supplement Blocks** (one per DECISION-type state in this phase):

> **DS-[S-ID] — [State Name]**
> - Condition: [the rule or threshold evaluated at this decision point]
> - Owner: R-[ID] ([role name from Role Registry])
> - Branch A ([condition outcome]): → S-[ID] ([state name])
> - Branch B ([condition outcome]): → S-[ID] ([state name]) or TERMINAL
> - Fallback: [action if condition cannot be evaluated — who is notified, what state is entered]

**PHASE EXIT GATE**

> `Blocked bottleneck:` names the B-ID that can delay this phase's exit, or NONE. The B-ID
> must string-match the identifier declared in Bottleneck Analysis below — assign the B-ID now
> and use the same string in that section. This is a forward reference.

- Exit Condition: [what the phase must have produced to be considered complete]
- Required outputs: [named artifacts, decisions, or state records that must exist]
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) confirms all required outputs are present
- Blocking condition: [if required outputs are absent: re-entry path or escalation]
- Blocked bottleneck: [B-NN that can delay this phase's exit, or NONE. Example: "B-01 — manual spreadsheet reconciliation by R-02 blocks invoice approval exit until GL entries are verified."]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

Identify at least one fork/join with labeled join condition:

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [path — states traversed in sequence; cite S-IDs]
- **Branch 2**: [path — states traversed in sequence; cite S-IDs]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join (both branches must complete) / OR-join (first branch sufficient) — specify which applies and explain why this process requires that join type

---

### Edge Case Enumeration

Identify at least three edge cases distinct from SECTION A exception flows:

> **EC-[N] — [Edge Case Name]**
> - Triggering Condition: [specific scenario that produces this edge case]
> - Why Problematic: [specific reason this falls outside documented handling]
> - Correct Response: R-[ID] ([role name]) — [specific correct action; name the target state or resolution path]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF — {Topic} lifecycle → [adjacent process name]**
> - Sending State: S-[ID] ([state name])
> - Receiving Process: [adjacent process name]
> - Data Payload: [named fields or record types transferred]
> - Expected Acknowledgment: [signal or confirmation message from receiving process]
> - Failure Mode: [what happens if acknowledgment is not received within SLA]
> - Owner: R-[ID] ([role name])

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Rules:
- AT-RISK = typical duration exceeds SLA target
- Every AT-RISK row must carry a Bottleneck Ref citing a B-NN from Bottleneck Analysis
- Minimum 3 annotated rows; at least 1 must be AT-RISK

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both of the following independent conditions.
> Each condition is verifiable by a single string-presence check against the Cause field text.
>
> **Dual-Cite Fail Condition A** — Cause field contains no IM-ID literal string (e.g., "IM-01"):
> fails C-39. Verify: search the Cause field text for "IM-" followed by digits. Absence → fail.
>
> **Dual-Cite Fail Condition B** — Cause field contains no R-ID literal string (e.g., "R-02"):
> fails C-39. Verify: search the Cause field text for "R-" followed by digits. Absence → fail.
>
> A Cause field that cites IM-01 but not an R-ID satisfies Condition A but fails Condition B.
> Both conditions must pass independently. Combined language ("due to manual process failures")
> that implies a root cause without naming IM-ID and R-ID by literal string fails both.
>
> B-IDs assigned here must string-match the `Blocked bottleneck:` fields in PHASE EXIT GATEs.
>
> Concrete format example for Evidence field:
> `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
>
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: A field containing only "see SLA ANALYSIS" or state names without
> AT-RISK row-level S-ID specificity does not satisfy.
>
> **DUAL-LOCATION REQUIREMENTS:**
> (1) Concrete named domain example (`"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`)
> must appear in BOTH this preamble AND each B-NN per-block Evidence hint.
> (2) Labeled axes (`` `Required format:` `` / `` `Fail condition:` ``) must appear in BOTH
> this preamble AND each B-NN per-block Evidence hint.
>
> Anti-embedding: Do not embed CHAIN STATUS inside the SLA ANALYSIS section.
> Declare CHAIN STATUS in its own dedicated top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [specific cause. Required: cite IM-ID literal string (Fail Condition A) AND R-ID literal
  string (Fail Condition B). Example: "IM-01 (manual spreadsheet GL reconciliation) combined with
  R-02 (GL Manager) unavailable during period-close peak — causes queue accumulation at S-05.
  Dual-cite check: 'IM-01' satisfies Condition A; 'R-02' satisfies Condition B."]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream state, SLA node, or adjacent process affected]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [specific cause — cite IM-ID literal string (Condition A) AND R-ID literal string
  (Condition B). Both must be present as literal strings. Example: "IM-02 (email-based approval
  routing without timestamp) combined with R-03 (Finance Controller) not available for same-day
  review — delays invoice matching at S-07. Dual-cite: 'IM-02' satisfies A; 'R-03' satisfies B."]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]

---

**Gap Identification**

> MISSING: [step name] — [rationale: why it belongs in this process model; what failure mode its
> absence enables; which phase it belongs in; which IM-ID it would reduce if present]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name the unlinked row]
- Backward (B→SLA): [every B-NN names affected SLA nodes; enumerate or name the gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID string-matches a declared B-NN block; name any mismatch]
- Dual-cite status: [every B-NN Cause field contains both an IM-ID string and an R-ID string; name any block where either is absent]
- Gap (if OPEN): [name the unresolved direction and the unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state that reaches it] |
| [failure terminal name] | FAILURE | [branch or state that reaches it] |
| [cancel terminal name] | CANCEL | [branch or state that reaches it] |

> Completeness check: Every exit branch in every SECTION B state table must reach one of the
> declared terminals above. No branch may end at a non-terminal state without an explicit
> `continues-via: S-[ID]` pointer.

---
---

## V-02 — Axis B: Exception-Bottleneck Citation

**Variation axis**: Output format — each EX-NNLetter block gains a `Bottleneck Ref: B-NN or NONE`
sub-field declaring whether the exception was enabled by a declared bottleneck. CHAIN STATUS
gains an Exception→B direction. This is the same pattern as AT-RISK SLA rows citing B-IDs
(C-14/C-16), applied one level up: exception traces cite the bottleneck that made the exception
possible.

**Hypothesis**: Exception traces currently terminate at a state and name a handling role, but do
not declare whether the exception is a symptom of a known bottleneck. When EX-2A cites `B-02`
and B-02's Evidence field cites `S-07: AT-RISK`, the Exception→B-NN→SLA chain is verifiable
by string comparison without navigating the SLA table directly from the exception: EX-2A B-02
string-matches B-02 block, B-02 Evidence string-matches S-07 AT-RISK row. This fourth
traceability direction is orthogonal to SLA↔B-NN (C-14/C-16), Baseline→B-NN (C-34), and
Role→B-NN (C-39). If a reviewer can validate all four directions by string comparison, the
cross-reference system may have sufficient density to surface C-40 as an independent criterion.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must cite at least one IM-ID
> by literal string. Quantified metric must appear before PHASE 1 in document order.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools, handoff mechanisms, storage, initiator]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure] | [frequency] | [downstream effect] |
| IM-02 | [second distinct failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [Named measure with current-state value or rate, declared before PHASE 1.
Example: "Purchase order cycle time: 8.1 days against 5-day target" or
"Manual matching error rate: 12% per period, generating 40+ exception tickets."]

---

### Role Registry Gate

> GATE BLOCK: Complete before Role Sequence Schedule and before tracing any state.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation:
- [ ] No entry uses "Approver" without a domain qualifier
- [ ] No entry uses "Owner" without a named responsibility
- [ ] Each R-ID appears in at least one Decision Supplement block, the Role Sequence Schedule,
      and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to active phases,
> activation trigger, handoff trigger, and parallel windows. B-NN Cause fields must cite
> the blocking R-ID from this schedule when role unavailability contributes to delay.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact — not "Start"] | [specific completion condition] | R-[ID] or NONE | [concurrent activity window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

Rules:
- Every phase must have a Primary Owner. Triggers must be specific.
- Every R-ID in this schedule must match an entry in the Role Registry Gate.

---

### Phase Structure

For each phase, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" by name.

- Entry Condition: [named artifact from prior phase exit gate's Required outputs field]
- Pre-condition check: R-[ID] ([role name from Role Sequence Schedule]) — [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition — name the state, threshold breach, or missing input]
> - Trace: [path of states from trigger to resolution or terminal; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. If a declared bottleneck created
>   the condition that triggered this exception, cite the B-ID here. The B-ID must string-match
>   an identifier in Bottleneck Analysis below. Example: "B-01 — manual reconciliation backlog
>   caused the missing approval that triggered this exception." NONE if no declared bottleneck
>   was causal.]

Minimum 1 exception trace per phase. Minimum 3 total. For each EX block with a non-NONE
Bottleneck Ref: the B-ID must appear in both the EX block and the Bottleneck Analysis section
(string consistency). CHAIN STATUS below will verify this direction.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules: Named Entry Condition required; Exits → S-ID or TERMINAL; standard Type values.

**Decision Supplement Blocks** (one per DECISION-type state):

> **DS-[S-ID] — [State Name]**
> - Condition: [rule or threshold]
> - Owner: R-[ID] ([role name from Role Registry])
> - Branch A ([outcome]): → S-[ID]
> - Branch B ([outcome]): → S-[ID] or TERMINAL
> - Fallback: [action if condition cannot be evaluated]

**PHASE EXIT GATE**

> `Blocked bottleneck:` names the B-ID that can delay this exit, or NONE. B-ID must
> string-match the Bottleneck Analysis identifier below.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Example: "B-02 — manual three-way match backlog blocks receipt confirmation exit until R-03 resolves discrepancy."]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [states traversed; cite S-IDs]
- **Branch 2**: [states traversed; cite S-IDs]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join / OR-join — specify which and explain why

---

### Edge Case Enumeration

At least three, distinct from SECTION A exception flows:

> **EC-[N] — [Edge Case Name]**
> - Triggering Condition: [specific scenario]
> - Why Problematic: [specific reason outside documented handling]
> - Correct Response: R-[ID] ([role name]) — [specific correct action]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF — {Topic} lifecycle → [adjacent process name]**
> - Sending State: S-[ID]; Receiving Process: [name]; Data Payload: [fields]
> - Expected Acknowledgment: [signal]; Failure Mode: [if no acknowledgment]; Owner: R-[ID]

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Minimum 3 rows; at least 1 AT-RISK citing a B-NN.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must cite (1) IM-ID from INCUMBENT BASELINE and (2)
> the blocking R-ID from the Role Sequence Schedule when role unavailability contributes.
> B-IDs here must match both PHASE EXIT GATE `Blocked bottleneck:` fields and any EX block
> `Bottleneck Ref:` fields — all three contexts must use the same B-ID string.
>
> Concrete format example for Evidence field:
> `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
>
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: A field containing only "see SLA ANALYSIS" or state names without
> AT-RISK row-level S-ID specificity does not satisfy.
>
> **DUAL-LOCATION REQUIREMENTS:**
> (1) Concrete named domain example (`"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`)
> must appear in BOTH this preamble AND each B-NN per-block Evidence hint.
> (2) Labeled axes (`` `Required format:` `` / `` `Fail condition:` ``) must appear in BOTH
> this preamble AND each B-NN per-block Evidence hint.
>
> Anti-embedding: Do not embed CHAIN STATUS inside the SLA ANALYSIS section.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [cite IM-ID from INCUMBENT BASELINE and blocking R-ID from Role Sequence Schedule.
  Example: "IM-01 (manual GL reconciliation) combined with R-02 (GL Manager) peak-period
  unavailability — queue accumulation at S-05. R-02 is the Phase 2 primary owner whose
  absence delays the phase exit."]
- Impact: [downstream state, SLA node, or adjacent process]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [cite IM-ID and blocking R-ID. Example: "IM-02 (email routing without timestamp)
  combined with R-03 unavailability — invoice matching queue at S-07."]
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]

---

**Gap Identification**

> MISSING: [step name] — [why it belongs; failure mode enabled; which phase; which IM-ID reduced]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK row cites a B-ID; enumerate pairs or name the unlinked row]
- Backward (B→SLA): [every B-NN names affected SLA nodes; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID matches a declared B-NN; name any mismatch]
- Exception→B: [every EX block `Bottleneck Ref:` B-ID (where non-NONE) matches a declared B-NN; list EX→B-NN pairs or name the unresolved EX block]
- Gap (if OPEN): [name the unresolved direction and the unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state] |
| [failure terminal name] | FAILURE | [branch or state] |
| [cancel terminal name] | CANCEL | [branch or state] |

> Every exit branch must reach a declared terminal. No mid-flow endings without `continues-via:`.

---
---

## V-03 — Axis C: Phase Entry Blocked-Bottleneck Back-Reference

**Variation axis**: Lifecycle emphasis — each PHASE ENTRY CONTRACT gains a `Prior phase blocked
bottleneck:` sub-field that mirrors the prior phase's PHASE EXIT GATE `Blocked bottleneck` value.
If the prior exit gate declared `Blocked bottleneck: B-02`, the entry contract of the next phase
declares `Prior phase blocked bottleneck: B-02 (inherited from Phase N exit gate)`. If the prior
exit gate declared NONE, this field likewise declares NONE.

**Hypothesis**: C-37 creates a forward reference from a phase to a B-NN (Phase N Exit Gate →
B-NN). When the next phase's ENTRY CONTRACT mirrors this with a back-reference, the B-ID becomes
traceable across the phase boundary in both directions: exit gate of Phase N declares B-02
forward; entry contract of Phase N+1 inherits B-02 backward. A reviewer can verify phase-boundary
bottleneck continuity by comparing three strings: Phase N exit gate `Blocked bottleneck: B-02`,
Phase N+1 entry contract `Prior phase blocked bottleneck: B-02`, and B-02 block identifier in
Bottleneck Analysis. No navigation of SLA Analysis or Role Schedule is required. If this
round-trip traceability across phase boundaries is a distinct structural property from the
single-direction forward reference of C-37, it may surface as C-41.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must cite at least one IM-ID
> by literal string and the blocking R-ID from the Role Sequence Schedule when applicable.
> Quantified metric must appear before PHASE 1 in document order.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools, handoff mechanisms, storage, initiator]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure] | [frequency] | [downstream effect] |
| IM-02 | [second distinct failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [Named quantified measure declared before PHASE 1. Example: "Support case
mean-time-to-resolve: 11.4 days vs 7-day SLA target" or "Duplicate payment rate: 4.7% per period."]

---

### Role Registry Gate

> GATE BLOCK: Complete before Role Sequence Schedule and before tracing any state.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation:
- [ ] No entry uses "Approver" without a domain qualifier
- [ ] No entry uses "Owner" without a named responsibility
- [ ] Each R-ID appears in at least one Decision Supplement block, the Role Sequence Schedule,
      and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to active phases,
> activation trigger, handoff trigger, and parallel windows. B-NN Cause fields must cite
> the blocking R-ID from this schedule when role unavailability contributes to delay.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1] | [completion condition] | R-[ID] or NONE | [concurrent window or NONE] |

Rules:
- Every phase must have a Primary Owner. Triggers must be specific.
- Every R-ID here must match an entry in the Role Registry Gate.

---

### Phase Structure

For each phase, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" by name.
> `Prior phase blocked bottleneck:` must mirror the prior phase's PHASE EXIT GATE
> `Blocked bottleneck:` value — same B-ID string or NONE. Phase 1 has no prior phase;
> declare `Prior phase blocked bottleneck: N/A (first phase)`.

- Entry Condition: [named artifact from prior phase exit gate's Required outputs field]
- Pre-condition check: R-[ID] ([role name from Role Sequence Schedule]) — [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase blocked bottleneck: [B-ID from prior phase's PHASE EXIT GATE `Blocked bottleneck:`
  field, or NONE if that field was NONE, or N/A for Phase 1. Must string-match the prior phase
  exit gate's Blocked bottleneck field and the B-NN block identifier in Bottleneck Analysis.
  Example: "B-01 (inherited from Phase 1 exit gate — manual reconciliation delay still active
  at phase boundary)."]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition — name state, threshold, or missing input]
> - Trace: [state path; cite S-IDs]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state] or [continues-via: S-[ID]]
> - Why Problematic: [process-specific reason]

Minimum 1 per phase; 3 total minimum.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules: Named Entry Condition required; Exits → S-ID or TERMINAL; standard Type values.

**Decision Supplement Blocks** (one per DECISION-type state):

> **DS-[S-ID] — [State Name]**
> - Condition: [rule or threshold]
> - Owner: R-[ID] ([role name from Role Registry])
> - Branch A ([outcome]): → S-[ID]
> - Branch B ([outcome]): → S-[ID] or TERMINAL
> - Fallback: [action if undecidable]

**PHASE EXIT GATE**

> `Blocked bottleneck:` names the B-ID that can delay this exit, or NONE. B-ID must
> string-match the Bottleneck Analysis identifier and the next phase's PHASE ENTRY CONTRACT
> `Prior phase blocked bottleneck:` field — three-way string consistency is the property.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. The B-ID declared here must appear in Bottleneck Analysis
  AND must be mirrored in the next phase's PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:`
  field. Example: "B-01 — spreadsheet reconciliation backlog delays approval output; will be
  inherited by Phase 2 entry contract as prior-phase blocker."]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [states traversed; cite S-IDs]
- **Branch 2**: [states traversed; cite S-IDs]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join / OR-join — specify and explain

---

### Edge Case Enumeration

Three or more, distinct from SECTION A:

> **EC-[N] — [Edge Case Name]**
> - Triggering Condition: [specific scenario]
> - Why Problematic: [specific consequence]
> - Correct Response: R-[ID] ([role name]) — [specific action]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF — {Topic} lifecycle → [adjacent process name]**
> - Sending State: S-[ID]; Receiving Process: [name]; Data Payload: [fields]
> - Expected Acknowledgment: [signal]; Failure Mode: [if no acknowledgment]; Owner: R-[ID]

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Minimum 3 rows; at least 1 AT-RISK citing a B-NN.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must cite (1) IM-ID from INCUMBENT BASELINE and (2) the
> blocking R-ID from the Role Sequence Schedule when role unavailability contributes. B-IDs here
> must string-match PHASE EXIT GATE `Blocked bottleneck:` fields and PHASE ENTRY CONTRACT
> `Prior phase blocked bottleneck:` fields in the following phase — three-way string consistency.
>
> Concrete format example for Evidence field:
> `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
>
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: A field containing only "see SLA ANALYSIS" or state names without
> AT-RISK row-level S-ID specificity does not satisfy.
>
> **DUAL-LOCATION REQUIREMENTS:**
> (1) Concrete named domain example must appear in BOTH this preamble AND each B-NN Evidence hint.
> (2) Labeled axes must appear in BOTH this preamble AND each B-NN Evidence hint.
>
> Anti-embedding: Do not embed CHAIN STATUS inside the SLA ANALYSIS section.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [cite IM-ID and blocking R-ID. Example: "IM-01 (manual spreadsheet reconciliation) +
  R-02 (GL Manager) peak unavailability — queue at S-05. R-02 owns Phase 2 (Role Sequence
  Schedule); their absence delays the phase exit gate and carries forward into Phase 3 entry."]
- Impact: [downstream state, SLA node, or adjacent process]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List AT-RISK SLA rows citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [cite IM-ID and blocking R-ID]
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List AT-RISK SLA rows citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]

---

**Gap Identification**

> MISSING: [step name] — [why it belongs; failure mode enabled; which phase; which IM-ID reduced]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK row cites a B-ID; enumerate or name gap]
- Backward (B→SLA): [every B-NN names affected SLA nodes; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID matches a declared B-NN; name any mismatch]
- Phase-boundary continuity: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID string-matches the next phase's PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:` value; list phase-pairs or name the break]
- Gap (if OPEN): [name the unresolved direction and the unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state] |
| [failure terminal name] | FAILURE | [branch or state] |
| [cancel terminal name] | CANCEL | [branch or state] |

> Every exit branch must reach a declared terminal. No mid-flow endings without `continues-via:`.

---
---

## V-04 — Axes A + B: Dual-Cite Explicitness + Exception-Bottleneck Citation

**Variation axes**: A (C-39 Dual-Cite Explicit Fail Conditions) + B (Exception-Bottleneck
Citation — `Bottleneck Ref:` in EX blocks)

**Hypothesis**: The two axes target different structural weaknesses. Axis A addresses ambiguous
partial citations in Cause fields: when IM-ID and R-ID are declared as two independent fail
conditions, a partial citation fails unambiguously rather than escaping as "mostly correct."
Axis B addresses the gap between exception traces and bottleneck analysis: EX blocks that cite
B-IDs create a fourth traceability direction (Exception→B-NN). Under compound pressure, the
architecture achieves: (1) every Cause field is verifiably dual-cited (IM-ID + R-ID), and
(2) every exception that was caused by a bottleneck explicitly declares which one. A reviewer
can navigate from any exception trace to its full causal chain — EX-2A cites B-02; B-02 Cause
cites IM-01 (satisfying Condition A) and R-02 (satisfying Condition B) — via three string
comparisons. This two-axis combination may be the minimum architecture for C-40.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions (IM-ID literal string and R-ID literal string). Quantified metric must appear
> before PHASE 1.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools, handoff mechanisms, storage, initiator]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure] | [frequency] | [downstream effect] |
| IM-02 | [second distinct failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [Named quantified measure declared before PHASE 1. Both IM-IDs must be
reachable from at least one B-NN Cause field below. Example: "Average credit approval cycle
time: 5.8 days vs 3-day SLA" or "Goods receipt discrepancy rate: 8.4% per period."]

---

### Role Registry Gate

> GATE BLOCK: Complete before Role Sequence Schedule and before tracing any state.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation:
- [ ] No entry uses "Approver" without a domain qualifier
- [ ] No entry uses "Owner" without a named responsibility
- [ ] Each R-ID appears in at least one Decision Supplement block, the Role Sequence Schedule,
      and at least one PHASE EXIT GATE Exit verification, Blocked bottleneck field,
      or EX block Bottleneck Ref (as the blocking role)

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to active phases,
> activation trigger, handoff trigger, and parallel windows. B-NN Cause fields and EX block
> `Bottleneck Ref:` annotations must be consistent with this schedule — R-IDs cited in Cause
> fields must appear in this schedule as phase owners or parallel roles.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1] | [completion condition] | R-[ID] or NONE | [concurrent window or NONE] |

Rules:
- Every phase must have a Primary Owner. Triggers must be specific.
- Every R-ID here must match an entry in the Role Registry Gate.
- Parallel windows must state start/end states (S-IDs) when known.

---

### Phase Structure

For each phase, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Entry Condition must reference prior phase's PHASE EXIT GATE "Required outputs" by name.

- Entry Condition: [named artifact from prior phase exit gate]
- Pre-condition check: R-[ID] ([role name from Role Sequence Schedule]) — [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition — name state, threshold, or missing input]
> - Trace: [state path; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state] or [continues-via: S-[ID]]
> - Why Problematic: [process-specific reason]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. Example: "B-01 — the manual reconciliation backlog created
>   the missing-approval condition that triggered this exception." NONE if no declared bottleneck
>   was causal for this specific trigger.]

Minimum 1 per phase; 3 total minimum. CHAIN STATUS Exception→B direction will verify B-ID
string consistency across EX blocks and Bottleneck Analysis.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules: Named Entry Condition required; Exits → S-ID or TERMINAL; standard Type values.

**Decision Supplement Blocks** (one per DECISION-type state):

> **DS-[S-ID] — [State Name]**
> - Condition: [rule or threshold]
> - Owner: R-[ID] ([role name from Role Registry])
> - Branch A ([outcome]): → S-[ID]
> - Branch B ([outcome]): → S-[ID] or TERMINAL
> - Fallback: [action if undecidable]

**PHASE EXIT GATE**

> `Blocked bottleneck:` names the B-ID that can delay this exit, or NONE. B-ID must
> string-match Bottleneck Analysis identifier.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Example: "B-01 — manual spreadsheet reconciliation delays approval exit; R-02 (GL Manager) is the blocking role per Role Sequence Schedule."]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [states traversed; cite S-IDs]
- **Branch 2**: [states traversed; cite S-IDs]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join / OR-join — specify and explain

---

### Edge Case Enumeration

Three or more, distinct from SECTION A:

> **EC-[N] — [Edge Case Name]**
> - Triggering Condition: [specific scenario]
> - Why Problematic: [specific consequence]
> - Correct Response: R-[ID] ([role name]) — [specific action]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF — {Topic} lifecycle → [adjacent process name]**
> - Sending State: S-[ID]; Receiving Process: [name]; Data Payload: [fields]
> - Expected Acknowledgment: [signal]; Failure Mode: [if no acknowledgment]; Owner: R-[ID]

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Minimum 3 rows; at least 1 AT-RISK citing a B-NN.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both of the following conditions independently.
>
> **Dual-Cite Fail Condition A** — Cause field contains no IM-ID literal string (e.g., "IM-01"):
> fails C-39. Test: search Cause text for "IM-" followed by digits. Absence → fail.
>
> **Dual-Cite Fail Condition B** — Cause field contains no R-ID literal string (e.g., "R-02"):
> fails C-39. Test: search Cause text for "R-" followed by digits. Absence → fail.
>
> Partial citation (IM-ID present but R-ID absent, or R-ID present but IM-ID absent) satisfies
> one condition and fails the other. Both must pass. B-IDs assigned here must string-match
> PHASE EXIT GATE `Blocked bottleneck:` fields AND EX block `Bottleneck Ref:` fields.
>
> Concrete format example for Evidence field:
> `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
>
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: A field containing only "see SLA ANALYSIS" or state names without
> AT-RISK row-level S-ID specificity does not satisfy.
>
> **DUAL-LOCATION REQUIREMENTS:**
> (1) Concrete named domain example must appear in BOTH this preamble AND each B-NN Evidence hint.
> (2) Labeled axes must appear in BOTH this preamble AND each B-NN Evidence hint.
>
> Anti-embedding: Do not embed CHAIN STATUS inside the SLA ANALYSIS section.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [Required: cite IM-ID literal string (Condition A) AND R-ID literal string (Condition B).
  Example: "IM-01 (manual spreadsheet GL reconciliation) combined with R-02 (GL Manager) peak
  unavailability — queue accumulation at S-05. R-02 is Phase 2 primary owner per Role Sequence
  Schedule. Dual-cite: 'IM-01' satisfies Condition A; 'R-02' satisfies Condition B."]
  - Dual-Cite Fail Condition A: no IM-ID string in Cause → fails C-39
  - Dual-Cite Fail Condition B: no R-ID string in Cause → fails C-39
- Impact: [downstream state, SLA node, or adjacent process]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List AT-RISK SLA rows citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [Required: cite IM-ID literal string AND R-ID literal string.
  Example: "IM-02 (email approval routing without timestamp) combined with R-03 (Finance
  Controller) same-day unavailability — invoice matching queue at S-07."]
  - Dual-Cite Fail Condition A: no IM-ID string in Cause → fails C-39
  - Dual-Cite Fail Condition B: no R-ID string in Cause → fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List AT-RISK SLA rows citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]

---

**Gap Identification**

> MISSING: [step name] — [why it belongs; failure mode enabled; which phase; which IM-ID reduced]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK row cites a B-ID; enumerate pairs or name gap]
- Backward (B→SLA): [every B-NN names affected SLA nodes; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID matches a declared B-NN; name any mismatch]
- Exception→B: [every EX block `Bottleneck Ref:` B-ID (where non-NONE) matches a declared B-NN; list EX→B-NN pairs or name unresolved EX block]
- Dual-cite status: [every B-NN Cause field contains both IM-ID and R-ID string; name any block where either is absent]
- Gap (if OPEN): [name the unresolved direction and the unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state] |
| [failure terminal name] | FAILURE | [branch or state] |
| [cancel terminal name] | CANCEL | [branch or state] |

> Every exit branch must reach a declared terminal. No mid-flow endings without `continues-via:`.

---
---

## V-05 — Axes A + B + C: Dual-Cite Explicitness + Exception-Bottleneck Citation + Phase Entry Back-Reference

**Variation axes**: A (Dual-Cite Explicit Fail Conditions) + B (Exception `Bottleneck Ref:`) +
C (Phase Entry `Prior phase blocked bottleneck:`)

**Hypothesis**: All three axes activate simultaneously, producing a six-artifact cross-reference
system verifiable entirely by string comparison: INCUMBENT BASELINE (IM-IDs), ROLE SEQUENCE
SCHEDULE (R-IDs), EX blocks (Bottleneck Ref), PHASE ENTRY CONTRACTs (Prior phase blocked
bottleneck), PHASE EXIT GATEs (Blocked bottleneck), and B-NN blocks (Cause, Evidence, B-ID).
Every traceability direction is active: SLA↔B-NN (C-14/C-16), Baseline→B-NN (C-34),
Role→B-NN (C-39 Condition B), Phase→B-NN (C-37), Phase-boundary B-NN (C-41 probe),
Exception→B-NN (C-40 probe). A reviewer starting at any artifact can reach any other artifact
in the system via at most two string comparisons. If C-40 and C-41 are independent criteria,
V-05 is the only variation where both are simultaneously active. If they compose into a single
higher-order criterion requiring all six artifacts to be internally consistent, V-05 is the only
configuration that can surface it.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Every BOTTLENECK IMPACT MATRIX row must cite an IM-ID from this table.
> Quantified metric must appear before PHASE 1.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools, handoff mechanisms, storage, initiator]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure] | [frequency] | [downstream effect] |
| IM-02 | [second distinct failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [Named quantified measure declared before PHASE 1. Example: "Case
escalation rate: 34% of cases reach senior review vs 15% target" or "Period-close reconciliation
cycle: 6.2 days vs 4-day regulatory deadline."]

---

### Role Registry Gate

> GATE BLOCK: Complete before Role Sequence Schedule and before tracing any state.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [domain-specific role] | [named responsibility] |
| R-02 | [domain-specific role] | [named responsibility] |
| R-03 | [domain-specific role] | [named responsibility] |

Anti-generic validation:
- [ ] No entry uses "Approver" without a domain qualifier
- [ ] No entry uses "Owner" without a named responsibility
- [ ] Each R-ID appears in at least one Decision Supplement block, the Role Sequence Schedule,
      and at least one of: PHASE EXIT GATE Blocked bottleneck field, EX block Bottleneck Ref
      (as blocking role), or PHASE ENTRY CONTRACT Prior phase blocked bottleneck annotation

Role set by process type:
- L2O → Sales Rep / Sales Manager / Finance Credit Analyst / Legal Counsel / Fulfillment Coordinator
- P2P → Procurement Officer / Accounts Payable Specialist / Receiving Dock Supervisor / Finance Controller
- Period Close → Finance Analyst / GL Manager / Controller / External Auditor
- Case Lifecycle → Support Engineer / Case Manager / Legal Counsel / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to active phases,
> activation trigger, handoff trigger, and parallel windows. R-IDs cited in B-NN Cause fields
> (Condition B) must appear in this schedule. R-IDs cited in EX block Bottleneck Ref annotations
> as blocking roles must also appear in this schedule.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact — not "Start"] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1] | [completion condition] | R-[ID] or NONE | [concurrent window or NONE] |

Rules:
- Every phase must have a Primary Owner. Triggers must be specific.
- Every R-ID here must match an entry in the Role Registry Gate.
- Parallel windows must state start/end states (S-IDs) when known.

---

### Phase Structure

For each phase, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" by name.
> `Prior phase blocked bottleneck:` must mirror the prior phase's exit gate `Blocked bottleneck:`
> value exactly — same B-ID string, or NONE, or N/A for Phase 1. Three-way string consistency:
> this field, the prior exit gate field, and the B-NN block identifier must all match.

- Entry Condition: [named artifact from prior phase exit gate's Required outputs field]
- Pre-condition check: R-[ID] ([role name from Role Sequence Schedule]) — [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase blocked bottleneck: [B-ID from prior phase PHASE EXIT GATE `Blocked bottleneck:`
  or NONE or N/A (Phase 1). Must string-match prior exit gate AND B-NN block identifier.
  Example: "B-02 (inherited from Phase 1 exit gate — invoice matching backlog carries into
  Phase 2 until receipt confirmation is issued)."]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition — name state, threshold breach, or missing input]
> - Trace: [state path; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state] or [continues-via: S-[ID]]
> - Why Problematic: [process-specific operational or compliance reason]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. Example: "B-01 — manual reconciliation backlog created the
>   missing-entry condition that triggered this exception; R-02 was unavailable to resolve it
>   before the deadline." NONE if no declared bottleneck was causal for this specific trigger.]

Minimum 1 per phase; 3 total minimum.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules: Named Entry Condition required; Exits → S-ID or TERMINAL; standard Type values.

**Decision Supplement Blocks** (one per DECISION-type state):

> **DS-[S-ID] — [State Name]**
> - Condition: [rule or threshold]
> - Owner: R-[ID] ([role name from Role Registry])
> - Branch A ([outcome]): → S-[ID]
> - Branch B ([outcome]): → S-[ID] or TERMINAL
> - Fallback: [action if undecidable]

**PHASE EXIT GATE**

> `Blocked bottleneck:` names the B-ID that can delay this exit, or NONE. B-ID must
> string-match: (1) Bottleneck Analysis identifier, (2) the next phase's PHASE ENTRY CONTRACT
> `Prior phase blocked bottleneck:` field. Three-way consistency is the structural property.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. B-ID must appear in Bottleneck Analysis AND be mirrored
  in the next phase's PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:` field.
  Example: "B-01 — manual spreadsheet reconciliation by R-02 delays GL approval exit;
  this blocker carries forward to Phase 2 entry contract as prior-phase inherited bottleneck."]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [states traversed; cite S-IDs]
- **Branch 2**: [states traversed; cite S-IDs]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join / OR-join — specify and explain

---

### Edge Case Enumeration

Three or more, distinct from SECTION A:

> **EC-[N] — [Edge Case Name]**
> - Triggering Condition: [specific scenario]
> - Why Problematic: [specific consequence]
> - Correct Response: R-[ID] ([role name]) — [specific action]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF — {Topic} lifecycle → [adjacent process name]**
> - Sending State: S-[ID]; Receiving Process: [name]; Data Payload: [fields]
> - Expected Acknowledgment: [signal]; Failure Mode: [if no acknowledgment]; Owner: R-[ID]

---

### SLA and Timing Analysis

| S-ID | State Name | SLA Target | Typical Duration | Status | Bottleneck Ref |
|------|-----------|------------|------------------|--------|----------------|
| | | | | AT-RISK / ON-TRACK | B-NN (if AT-RISK) |

Minimum 3 rows; at least 1 AT-RISK citing a B-NN.

---

### Bottleneck Analysis

> **PREAMBLE**: Each B-NN Cause field must satisfy both of the following conditions independently.
>
> **Dual-Cite Fail Condition A** — Cause field contains no IM-ID literal string (e.g., "IM-01"):
> fails C-39. Test: search Cause text for "IM-" followed by digits. Absence → fail.
>
> **Dual-Cite Fail Condition B** — Cause field contains no R-ID literal string (e.g., "R-02"):
> fails C-39. Test: search Cause text for "R-" followed by digits. Absence → fail.
>
> Partial citation fails the absent condition. Both must pass. B-IDs here must string-match:
> (1) PHASE EXIT GATE `Blocked bottleneck:` fields, (2) PHASE ENTRY CONTRACT `Prior phase
> blocked bottleneck:` fields in the following phase, and (3) EX block `Bottleneck Ref:` fields
> where non-NONE. All four contexts must be consistent by string comparison.
>
> Concrete format example for Evidence field:
> `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`
>
> Required format: `[State name -- S-ID]: AT-RISK, causal source: B-[ID]`
> Fail condition: A field containing only "see SLA ANALYSIS" or state names without
> AT-RISK row-level S-ID specificity does not satisfy.
>
> **DUAL-LOCATION REQUIREMENTS:**
> (1) Concrete named domain example must appear in BOTH this preamble AND each B-NN Evidence hint.
> (2) Labeled axes must appear in BOTH this preamble AND each B-NN Evidence hint.
>
> Anti-embedding: Do not embed CHAIN STATUS inside the SLA ANALYSIS section.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).
  Example: "IM-01 (manual spreadsheet GL reconciliation) combined with R-02 (GL Manager)
  period-close peak unavailability — causes queue accumulation at S-05. R-02 is Phase 2
  primary owner per Role Sequence Schedule. This B-ID will appear in Phase 1 exit gate
  `Blocked bottleneck:` and Phase 2 entry contract `Prior phase blocked bottleneck:`.
  Dual-cite: 'IM-01' satisfies Condition A; 'R-02' satisfies Condition B."]
  - Dual-Cite Fail Condition A: no IM-ID string in Cause → fails C-39
  - Dual-Cite Fail Condition B: no R-ID string in Cause → fails C-39
- Impact: [downstream state, SLA node, or adjacent process]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List AT-RISK SLA rows citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string AND R-ID literal string. Example: "IM-02 (email
  approval routing without SLA timestamp) combined with R-03 (Finance Controller) same-day
  unavailability — invoice matching queue at S-07. Dual-cite: 'IM-02' satisfies Condition A;
  'R-03' satisfies Condition B."]
  - Dual-Cite Fail Condition A: no IM-ID string in Cause → fails C-39
  - Dual-Cite Fail Condition B: no R-ID string in Cause → fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List AT-RISK SLA rows citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]

---

**Gap Identification**

> MISSING: [step name] — [why it belongs; failure mode enabled; which phase; which IM-ID reduced]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK row cites a B-ID; enumerate pairs or name gap]
- Backward (B→SLA): [every B-NN names affected SLA nodes; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID matches a declared B-NN; name any mismatch]
- Phase-boundary continuity: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID string-matches the next phase's PHASE ENTRY CONTRACT `Prior phase blocked bottleneck:`; list phase-pairs or name break]
- Exception→B: [every EX block `Bottleneck Ref:` B-ID (where non-NONE) matches a declared B-NN; list EX→B-NN pairs or name unresolved EX block]
- Dual-cite status: [every B-NN Cause field contains both IM-ID and R-ID string; name any block missing either]
- Gap (if OPEN): [name the unresolved direction and the unlinked entry]

---

### Terminal States

| Terminal | Type | Reached From |
|----------|------|-------------|
| [success terminal name] | SUCCESS | [branch or state] |
| [failure terminal name] | FAILURE | [branch or state] |
| [cancel terminal name] | CANCEL | [branch or state] |

> Every exit branch must reach a declared terminal. No mid-flow endings without `continues-via:`.
