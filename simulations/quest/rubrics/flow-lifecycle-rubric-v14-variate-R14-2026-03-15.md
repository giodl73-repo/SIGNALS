# flow-lifecycle — Round 14 Variations (Rubric v14)

**Rubric**: v14 · 45 criteria (37 aspirational) · Ceiling entering R14: 37/37
(R13 V-05 achieved perfect retroactive score under v14; all C-44 and C-45 signals present.)

**Open criteria entering R14**: None — ceiling is already 37/37. R14 explores whether
alternative axis combinations produce the same ceiling more robustly, and whether inertia
framing and role-sequence axes interact with C-44/C-45 compliance.

**Evidence from R13 excellence (C-44, C-45):**

- **C-44 signal**: R13 V-02 established that per-block `Exception Refs:` in each B-NN block
  (listing every EX block whose `Bottleneck Ref:` cites this B-ID) is the discriminating
  property. Gate-only (R13 V-01) was insufficient. V-05 confirmed G2 + H compose cleanly.
- **C-45 signal**: R13 V-04 established that naming `Blocked bottleneck:` and `Next phase:`
  as orthogonal in the EXIT GATE instruction, combined with `Prior phase:` and `Prior phase
  blocked bottleneck:` in the ENTRY CONTRACT, triggers C-45. R13 V-05 confirmed all three
  fields can be named explicitly as a unit in the PHASE ENTRY CONTRACT preamble.

**R14 design premise**: R13 axes (G1/G2/H) targeted structural additions. R14 explores
whether a dedicated **PHASE GATE CONTRACT SUMMARY** section (naming all three fields as an
explicit declared unit) is a more reliable C-45 trigger than the R13 cross-block phrasing
approach. Simultaneously explores whether **Finance-first role sequencing** and **inertia
framing** interact with evidence quality.

**New criteria targeted in R14:**

**C-44 target (V-02, V-04, V-05)**: Make the per-block `Exception Refs:` instruction
a self-contained named block with format example and failure condition, isolated from the
preamble gate check. Tests whether a cleaner per-block format hint produces more reliable
C-44 compliance than the R13 combined-instruction approach.

**C-45 target (V-03, V-05)**: Introduce an explicit **PHASE GATE CONTRACT SUMMARY** section
before PHASE 1 that names all three phase gate contract fields as a declared unit and states
the orthogonality property explicitly. Tests whether a dedicated named section outperforms
the R13 approach of distributing the declaration across ENTRY CONTRACT and EXIT GATE
instructions.

**Variation matrix:**

| Variation | Axes | C-44 Exception Refs per-block | C-45 CONTRACT SUMMARY | Inertia framing | Finance-first roles | Primary hypothesis |
|-----------|------|------------------------------|----------------------|-----------------|--------------------|--------------------|
| V-01 | Role sequence | NO (gate only) | NO | Standard | YES | Finance-first role ordering changes which B-IDs appear in dual-cite evidence; no C-44/C-45 structural additions |
| V-02 | Output format | YES (named block, format example) | NO | Standard | NO | Isolated per-block `Exception Refs:` instruction with its own format hint produces more reliable C-44 compliance than embedded instruction |
| V-03 | Lifecycle emphasis | NO (gate only) | YES (dedicated section) | Standard | NO | Dedicated PHASE GATE CONTRACT SUMMARY section naming all three fields as a unit is more reliable C-45 trigger than distributed cross-block phrasing |
| V-04 | Role sequence + Output format | YES (named block) | NO | Standard | YES | Finance-first roles + explicit per-block refs compose without conflict; C-44 passes independently of role ordering |
| V-05 | Output format + Lifecycle emphasis | YES (named block) | YES (dedicated section) | Prominent per-phase | NO | Maximum density: per-block Exception Refs + PHASE GATE CONTRACT SUMMARY achieves both C-44 and C-45; prominent inertia framing improves dual-cite Evidence quality |

**Structural change summary vs R13 V-05:**

| Section | R13 V-05 had | V-01 changes | V-02 adds | V-03 adds | V-04 combines | V-05 combines |
|---------|-------------|-------------|----------|----------|--------------|--------------|
| Role Registry Gate / Schedule | Operations-first default order | Finance-first R-ID ordering | — | — | Finance-first | — |
| PHASE GATE CONTRACT SUMMARY | Absent (implicit across ENTRY+EXIT) | — | — | Dedicated named section | — | Dedicated named section |
| B-NN block `Exception Refs:` hint | Combined with preamble gate check | Gate-only (G2 removed) | Isolated named sub-block | Gate-only | Isolated named sub-block | Isolated named sub-block |
| Bottleneck Analysis PREAMBLE | Combined gate + dual-location | Preamble gate only | Preamble gate only | Preamble gate only | Preamble gate only | Preamble gate only |
| INCUMBENT BASELINE | Standard preamble | Finance-domain failure modes prioritized | Standard | Standard | Finance-domain | Prominent per-phase IM-ref callout |

---

## V-01 — Axis: Role Sequence (Finance-First Ordering)

**Variation axis**: Role sequence — the Role Registry Gate and Role Sequence Schedule
declare Finance roles first (e.g., Finance Controller, Finance Analyst, Credit Analyst),
then Operations roles, then Sales or Case roles last. The INCUMBENT BASELINE prioritizes
financial failure modes (IM-01, IM-02) over operational ones, anchoring the dual-cite
chain to Finance-domain bottlenecks. The structural template is otherwise identical to
the R13 V-05 baseline: preamble gate check only (no per-block `Exception Refs:` field),
`Next phase:` in exit gates (C-43), `Prior phase:` in entry contracts (C-41). No dedicated
PHASE GATE CONTRACT SUMMARY section.

**Hypothesis**: Finance-first role sequencing changes which roles appear as B-NN Cause R-IDs
and as `Role Ref:` fields in EX blocks. If the model follows the declared role ordering
when selecting blocking roles for B-NN Cause fields, Finance roles will dominate the
dual-cite evidence chain, producing more specific IM-ID → B-NN traceability for financial
failure modes. This axis does not add C-44 or C-45 structure; it tests whether role
ordering affects evidence quality independently of structural changes. C-44 and C-45 should
remain at their R13 V-01-equivalent status (FAIL/FAIL) since neither per-block
`Exception Refs:` nor a three-field contract declaration is added.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1 in document order.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools used (spreadsheets, email, phone), handoff
mechanisms, where records are stored, who initiates the process manually. Lead with the
financial control point — where does the Finance team touch the process first?]

**Incumbent failure modes** (Finance-domain failures first; assign IM-ID to each):

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [Finance-domain recurring failure: e.g., manual GL reconciliation error, credit limit override without approval, duplicate invoice matching gap] | [daily / per-cycle / per-exception] | [downstream financial control break] |
| IM-02 | [Second Finance-domain or cross-functional failure mode: e.g., period-close entry cutoff missed, approval routing without SLA timestamp] | [frequency] | [downstream effect] |

**Cost of no action**: [Named financial measure with current-state value or rate, declared
before PHASE 1. Must be Finance-domain quantified. Example: "Average credit hold review cycle:
5.8 days against 3-day SLA" or "Manual GL reconciliation error rate: 6.3% per period close,
generating 40+ rework tickets." Both IM-IDs above must be reachable from at least one B-NN
Cause field below.]

---

### Role Registry Gate

> GATE BLOCK: Complete before the Role Sequence Schedule and before tracing any state.
> All four anti-generic checks must clear before proceeding.
> Finance roles must be declared with R-01 and R-02 (highest-numbered Finance responsibilities
> first); Operations and Sales/Case roles follow.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [Finance role — primary financial control responsibility] | [named financial control function] |
| R-02 | [Finance role — secondary financial or approval responsibility] | [named responsibility] |
| R-03 | [Operations or Sales/Case role] | [named operational responsibility] |

Anti-generic validation (all four must clear before proceeding):
- [ ] No R-ID entry uses "Approver" without a domain qualifier (e.g., "Finance Credit Approver" passes; "Approver" fails)
- [ ] No R-ID entry uses "Owner" without a named responsibility
- [ ] Each R-ID is referenced by at least one Decision Supplement block, the Role Sequence
      Schedule, and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field
- [ ] Each declared R-ID appears in at least one EX block's `Role Ref:` sub-field — R-IDs
      with no observable EX trace are "dark" roles and constitute a gate violation; identify
      any dark R-IDs before proceeding to phase content generation

Role set by process type (Finance roles listed first in each set):
- L2O → Finance Credit Analyst / Sales Manager / Sales Rep / Legal Counsel / Fulfillment Coordinator
- P2P → Finance Controller / Accounts Payable Specialist / Procurement Officer / Receiving Dock Supervisor
- Period Close → Controller / GL Manager / Finance Analyst / External Auditor
- Case Lifecycle → Case Manager / Legal Counsel / Support Engineer / Operations Coordinator

---

### Role Sequence Schedule

> Declared after Role Registry Gate and before PHASE 1. Finance roles (R-01, R-02) are
> declared first in the schedule even if their activation is mid-process. Maps each R-ID
> to owned phases with activation triggers, handoff triggers, and parallel windows.
> B-NN Cause fields must cite the blocking R-ID from this schedule (Dual-Cite Fail Condition B).
> R-IDs cited in EX block `Role Ref:` sub-fields must appear in this schedule as the phase
> owner for the enclosing phase.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact — not "Start"] | [specific completion condition] | R-[ID] or NONE | [concurrent activity window or NONE] |
| Phase 2 | R-[ID] | [handoff received from phase 1 — name the artifact] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

Rules:
- Finance roles (R-01, R-02) must appear in at least one phase as Primary Owner.
- Activation Trigger for Phase 1 must name a Finance-domain event or external artifact.
- Handoff Trigger must be specific enough that a Finance reviewer can determine the exact
  moment of transfer (name the document, approval, or state record transferred).
- Parallel windows must declare start/end states (S-IDs) when known.
- Every R-ID in this schedule must match an entry in the Role Registry Gate.

---

### Phase Structure

For each phase in the lifecycle, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" by name.
> Two sequential-linkage sub-fields are required:
> `Prior phase:` = literal phase identifier (Phase→Phase backward linkage).
> `Prior phase blocked bottleneck:` = B-ID from prior exit gate (B-NN boundary continuity).
> Both are independently verifiable by string comparison.

- Entry Condition: [specific named artifact from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name — must match Role Sequence Schedule primary owner for this phase]) — [verification method]
- Blocking condition: [if entry condition not met: which state is entered, which role notified, re-entry path]
- Prior phase: [Literal identifier of the preceding phase block, e.g., "PHASE 1 — Initiation".
  Phase 1 carries NONE or INIT as sentinel. Non-first phase with sentinel fails. First phase
  with phase identifier fails. Must string-match preceding phase block label in document order.]
- Prior phase blocked bottleneck: [B-ID from prior phase PHASE EXIT GATE `Blocked bottleneck:`
  or NONE if that field was NONE, or N/A for Phase 1. Must string-match prior exit gate field
  AND B-NN block identifier. Example: "B-01 (inherited from Phase 1 exit gate — Finance credit
  approval backlog still active at phase boundary; R-01 Finance Credit Analyst blocking per
  Role Sequence Schedule)."]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition — name the state, threshold breach, or missing input]
> - Trace: [path of states traversed from trigger to resolution or terminal; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason this failure mode matters]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. The Bottleneck Analysis preamble gate check will verify
>   that every declared B-ID appears in at least one EX block's `Bottleneck Ref:` — populate
>   accurately. NONE if no declared bottleneck was causal.]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Must be a
>   literal R-ID matching the schedule entry for the enclosing phase. Example: "R-01 —
>   Finance Credit Analyst owns Phase 1 per Role Sequence Schedule." Free-text without R-ID
>   fails. R-ID absent from schedule fails.]

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
> - Condition: [the rule or threshold evaluated at this decision point]
> - Owner: R-[ID] ([role name from Role Registry])
> - Branch A ([condition outcome]): → S-[ID] ([state name])
> - Branch B ([condition outcome]): → S-[ID] ([state name]) or TERMINAL
> - Fallback: [action if condition cannot be evaluated — who is notified, what state is entered]

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
  next phase's `Prior phase blocked bottleneck:`. Example: "B-01 — Finance credit approval
  backlog by R-01 delays phase exit; inherited by Phase 2 entry contract."]
- Next phase: [Literal identifier of the subsequent phase block, e.g., "PHASE 2 — Credit
  Review". Last phase carries NONE or END as sentinel. Must string-match next phase block
  label in document order.]

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
> - Triggering Condition: [specific scenario that produces this edge case]
> - Why Problematic: [specific reason this falls outside documented handling]
> - Correct Response: R-[ID] ([role name]) — [specific correct action; name target state or resolution path]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF — {Topic} lifecycle → [adjacent process name]**
> - Sending State: S-[ID] ([state name])
> - Receiving Process: [adjacent process name]
> - Data Payload: [named fields or record types transferred]
> - Expected Acknowledgment: [signal or confirmation message from receiving process]
> - Failure Mode: [what happens if acknowledgment not received within SLA]
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
> a "dark bottleneck" — a declared failure mode with no exception-phase trace. Dark bottlenecks
> are gate violations. Verify after all phases: for each declared B-ID, scan EX blocks for
> `Bottleneck Ref:` containing that B-ID string. Absence → dark bottleneck gate violation.
> Report result in CHAIN STATUS `B-NN→Exception` direction.
>
> Anti-embedding: Declare CHAIN STATUS in its own dedicated top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Finance-Domain Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).
  Finance-domain bottleneck: cite the Finance role (R-01 or R-02) as the blocking R-ID.
  Example: "IM-01 (manual GL reconciliation) combined with R-01 (Finance Controller)
  period-close unavailability — approval queue at S-05. 'IM-01' satisfies A; 'R-01' satisfies B."]
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
- Backward (B→SLA): [every B-NN Evidence field lists AT-RISK SLA rows citing it; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID string-matches a declared B-NN; name any mismatch]
- Phase-boundary B-NN continuity: [every exit gate B-ID matches next phase's `Prior phase blocked bottleneck:`; list phase pairs or name break]
- Phase-sequence: [every PHASE ENTRY CONTRACT `Prior phase:` identifier string-matches preceding phase block label; PHASE 1 carries NONE/INIT sentinel; list pairs or name mismatch]
- Phase-exit-sequence: [every PHASE EXIT GATE `Next phase:` identifier string-matches subsequent phase block label; last phase carries NONE/END sentinel; list exit gate→next phase pairs or name any mismatch]
- Exception→B: [every EX block `Bottleneck Ref:` B-ID (non-NONE) matches a declared B-NN; list EX→B-NN pairs or name unresolved block]
- B-NN→Exception: [every declared B-ID appears in at least one EX block's `Bottleneck Ref:` sub-field; enumerate B-ID→EX pairs; name any B-ID with no EX trace (dark bottleneck)]
- Exception→Role: [every EX block `Role Ref:` R-ID matches ROLE SEQUENCE SCHEDULE primary owner for enclosing phase; list EX→R-ID pairs or name mismatch]
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

**Variation axis**: Output format — the `Exception Refs:` instruction in each B-NN block
is promoted to an isolated, self-contained named instruction block with its own format
example and failure condition, separated from the preamble gate check. The preamble retains
only the gate check (document-level existence assertion); each B-NN block carries a dedicated
`Exception Refs:` section with its own inline format hint naming the specific B-ID. This
makes the per-block `Exception Refs:` field format-identical to the Evidence field (both
carry a named instruction block with Required format + Fail condition). No PHASE GATE
CONTRACT SUMMARY section is added; C-45 is not targeted.

**Hypothesis**: The R13 V-02 per-block `Exception Refs:` instruction was embedded within
the preamble gate check commentary. Promoting it to an isolated named instruction block —
symmetric to how the Evidence field has its own format hint — may produce cleaner compliance
because the generating model receives a single, unambiguous format signal for `Exception
Refs:` rather than extracting it from gate-check prose. C-44 should pass more reliably when
the per-block instruction is visually and structurally separated. C-45 should remain FAIL
since no three-field contract declaration is added.

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
| IM-01 | [specific recurring failure in the manual process] | [daily / per-cycle / per-exception] | [downstream effect] |
| IM-02 | [second distinct failure mode] | [frequency] | [downstream effect] |

**Cost of no action**: [Named measure with current-state value or rate, declared before
PHASE 1. Both IM-IDs must be reachable from at least one B-NN Cause field. Example:
"Average credit approval cycle time: 5.8 days vs 3-day SLA" or "Manual matching error
rate: 12% per period."]

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

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to owned phases
> with activation triggers, handoff triggers, and parallel windows. B-NN Cause fields must
> cite the blocking R-ID from this schedule (Dual-Cite Fail Condition B). R-IDs in EX block
> `Role Ref:` must match the schedule entry for the enclosing phase.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [external event or prior-process artifact — not "Start"] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1 — name the artifact] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

Rules: Every phase must have a Primary Owner. Triggers must be specific. Every R-ID here
must match a Role Registry Gate entry.

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
  Phase 1 carries NONE or INIT as sentinel. Must string-match preceding phase block label.]
- Prior phase blocked bottleneck: [B-ID from prior exit gate `Blocked bottleneck:` or NONE
  or N/A for Phase 1. Must string-match prior exit gate AND B-NN block identifier.]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition — name state, threshold breach, or missing input]
> - Trace: [path of states from trigger to resolution or terminal; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. This is the Exception→Bottleneck traceability artifact.
>   The reverse direction is carried by the `Exception Refs:` field in the cited B-NN block
>   below — that field must list this EX block's ID if Bottleneck Ref is non-NONE.]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID
>   matching the schedule entry for the enclosing phase.]

Minimum 1 per phase; 3 total minimum. Bottleneck Ref and Role Ref independent; populate both.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules: Named Entry Condition required; Exits → S-ID or TERMINAL; standard Type values.

**Decision Supplement Blocks** (one per DECISION-type state):

> **DS-[S-ID] — [State Name]**
> - Condition: [rule or threshold]; Owner: R-[ID]; Branch A: → S-[ID]; Branch B: → TERMINAL; Fallback: [action]

**PHASE EXIT GATE**

> `Blocked bottleneck:` carries a B-ID (phase→B-NN forward reference).
> `Next phase:` carries a Phase identifier (phase→phase forward linkage). Orthogonal fields.
> `Blocked bottleneck:` must string-match Bottleneck Analysis AND next phase's
> `Prior phase blocked bottleneck:`. `Next phase:` must string-match next phase block label.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Must appear in Bottleneck Analysis AND in next phase's
  `Prior phase blocked bottleneck:`.]
- Next phase: [Literal identifier of subsequent phase block. Last phase: NONE or END sentinel.
  Must string-match next phase block label in document order.]

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
> block's `Bottleneck Ref:` sub-field. A B-ID with no EX citation is a "dark bottleneck"
> and a gate violation. Report in CHAIN STATUS `B-NN→Exception` direction.
>
> Anti-embedding: Declare CHAIN STATUS in its own dedicated top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field AND an Exception Refs field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).
  Example: "IM-01 (manual spreadsheet reconciliation) combined with R-02 (GL Manager)
  period-close unavailability — queue at S-05. 'IM-01' satisfies A; 'R-02' satisfies B."]
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
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-01. Example:
    `"EX-1A (Phase 1 — Credit Limit Exceeded), EX-2B (Phase 2 — Approval Timeout)"`]

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
  - Fail condition: NONE declared = dark bottleneck (gate violation). Listed ID without
    matching `Bottleneck Ref: B-02` in the cited EX block fails consistency check.
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
- Phase-exit-sequence: [every PHASE EXIT GATE `Next phase:` identifier string-matches subsequent phase block; last phase carries NONE/END; list pairs or name mismatch]
- Exception→B: [every EX block `Bottleneck Ref:` B-ID (non-NONE) matches a declared B-NN; list EX→B-NN pairs or name unresolved block]
- B-NN→Exception: [every declared B-ID has at least one non-NONE entry in its `Exception Refs:` field; each listed EX block ID string-matches an EX block with `Bottleneck Ref:` citing this B-ID; enumerate B-ID→EX pairs; name any B-ID with NONE in Exception Refs (dark bottleneck) or any listed ID whose EX block does not carry matching Bottleneck Ref]
- Exception→Role: [every EX block `Role Ref:` R-ID matches ROLE SEQUENCE SCHEDULE primary owner; list EX→R-ID pairs or name mismatch]
- Role→Exception: [every declared R-ID appears in at least one EX block `Role Ref:`; list R-ID→EX pairs; name dark roles]
- Dual-cite status: [every B-NN Cause has both IM-ID and R-ID; name any block missing either]
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

**Variation axis**: Lifecycle emphasis — an explicit **PHASE GATE CONTRACT SUMMARY** section
is added before PHASE 1 as a dedicated top-level block that names all three phase gate
contract fields as a declared unit, states their value types, and explicitly declares the
orthogonality property. This section is analogous to the Role Registry Gate: it declares
the phase gate architecture before any phase is traced, making the three-field system a
named structural commitment that the generating model must honor in every phase block.
Per-block `Exception Refs:` in B-NN blocks is NOT added (C-44 not targeted); the Bottleneck
Analysis retains preamble gate check only.

**Hypothesis**: C-45 requires an "explicit preamble or dedicated contract summary naming the
complete three-field phase gate system as a unit." A dedicated top-level section — parallel
to the Role Registry Gate and Role Sequence Schedule — is more likely to trigger C-45 than
cross-block phrasing distributed across ENTRY CONTRACT and EXIT GATE instructions. By naming
all three fields in one block with explicit orthogonality and string-comparison declarations,
the three-field contract becomes a first-class structural element rather than an implicit
property of two separate gate instructions. C-44 should remain FAIL since no per-block
`Exception Refs:` field is added.

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
> in their designated locations.
>
> | Field Name | Location | Value Type | Traceability Direction |
> |------------|----------|------------|----------------------|
> | `Prior phase:` | PHASE ENTRY CONTRACT | Phase label (e.g., "PHASE 1 — Initiation") | Phase→Phase, backward (entry side) |
> | `Prior phase blocked bottleneck:` | PHASE ENTRY CONTRACT | B-ID (e.g., "B-01") | B-NN boundary continuity, entry side |
> | `Next phase:` | PHASE EXIT GATE | Phase label (e.g., "PHASE 2 — Credit Review") | Phase→Phase, forward (exit side) |
>
> **ORTHOGONALITY DECLARATION:**
> `Prior phase blocked bottleneck:` carries a B-ID (format pattern: "B-" followed by digits,
> e.g., "B-01"). `Next phase:` carries a Phase label (format pattern: "PHASE N — [Name]" or
> NONE/END sentinel). These two fields carry orthogonal value types independently verifiable
> by string comparison: a B-ID in `Next phase:` is a format violation; a Phase label in
> `Prior phase blocked bottleneck:` is a format violation. Detection requires no inference —
> the format patterns are distinct and non-overlapping.
>
> `Prior phase:` and `Next phase:` form a symmetric bidirectional pair: entry contracts
> declare backward linkage; exit gates declare forward linkage. `Prior phase blocked
> bottleneck:` is orthogonal to both — it carries a B-ID, not a Phase label.
>
> CHAIN STATUS verifies three directions from this contract:
> - `Phase-sequence`: every `Prior phase:` string-matches preceding phase block label
> - `Phase-exit-sequence`: every `Next phase:` string-matches subsequent phase block label
> - `Phase-boundary B-NN continuity`: every exit gate `Blocked bottleneck:` B-ID string-matches
>   next phase's `Prior phase blocked bottleneck:`

---

### Phase Structure

For each phase in the lifecycle, produce the following five blocks in document order. All
three Phase Gate Contract fields must be populated in every phase block.

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" by name.
> Phase Gate Contract fields 1 and 2 live here:
> `Prior phase:` (Phase label, backward) and `Prior phase blocked bottleneck:` (B-ID, entry).
> These two fields are orthogonal: one carries a Phase label; one carries a B-ID.

- Entry Condition: [specific named artifact from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) — [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase: [Literal identifier of preceding phase block. Phase 1: NONE or INIT sentinel.
  Must string-match preceding phase block label in document order. Format: "PHASE N — [Name]".]
- Prior phase blocked bottleneck: [B-ID from prior exit gate `Blocked bottleneck:` or NONE
  or N/A for Phase 1. Format: "B-NN". Must string-match prior exit gate AND B-NN block identifier.
  This field carries a B-ID — NOT a Phase label. Do not conflate with `Prior phase:`.]

**SECTION A — EXCEPTION TRACES**

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition]
> - Trace: [states traversed; cite S-IDs]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason]
> - Bottleneck Ref: [B-NN or NONE. B-ID must string-match a Bottleneck Analysis identifier.
>   The preamble gate check verifies that every declared B-ID appears in at least one such
>   field — populate accurately.]
> - Role Ref: [R-ID of ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID
>   matching schedule entry for enclosing phase.]

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
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Must string-match Bottleneck Analysis identifier AND
  next phase's `Prior phase blocked bottleneck:`. Format: "B-NN" — a B-ID, not a Phase label.]
- Next phase: [Literal identifier of the subsequent phase block. Format: "PHASE N — [Name]".
  Last phase: NONE or END sentinel. Must string-match next phase block label in document order.
  This field carries a Phase label — not a B-ID. See PHASE GATE CONTRACT SUMMARY orthogonality
  declaration for format verification rule.]

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
> block's `Bottleneck Ref:` sub-field. Dark bottlenecks are gate violations. Report in
> CHAIN STATUS `B-NN→Exception` direction.
>
> Anti-embedding: Declare CHAIN STATUS in its own dedicated top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream state, SLA node, or adjacent process]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
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

- Forward (SLA→B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name gap]
- Backward (B→SLA): [every B-NN Evidence field lists AT-RISK SLA rows; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID matches a declared B-NN; name any mismatch]
- Phase-boundary B-NN continuity: [every exit gate B-ID matches next phase's `Prior phase blocked bottleneck:`; list pairs or name break]
- Phase-sequence: [every PHASE ENTRY CONTRACT `Prior phase:` matches preceding phase block label; PHASE 1 carries NONE/INIT; list pairs or name mismatch]
- Phase-exit-sequence: [every PHASE EXIT GATE `Next phase:` matches subsequent phase block label; last phase carries NONE/END; list pairs or name mismatch]
- Exception→B: [every EX block `Bottleneck Ref:` B-ID (non-NONE) matches a declared B-NN; list pairs or name unresolved block]
- B-NN→Exception: [every declared B-ID appears in at least one EX block's `Bottleneck Ref:`; enumerate B-ID→EX pairs; name dark bottlenecks]
- Exception→Role: [every EX block `Role Ref:` R-ID matches ROLE SEQUENCE SCHEDULE primary owner; list pairs or name mismatch]
- Role→Exception: [every declared R-ID appears in at least one EX block `Role Ref:`; list pairs; name dark roles]
- Dual-cite status: [every B-NN Cause has both IM-ID and R-ID; name any block missing either]
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

## V-04 — Combination: Role Sequence + Output Format (Finance-First + C-44 Per-Block Refs)

**Variation axis**: Role sequence + Output format — Finance-first role ordering (V-01 axis)
combined with the isolated per-block `Exception Refs:` named instruction block (V-02 axis).
Tests whether Finance-domain role sequencing and explicit C-44 per-block format hints
compose without structural conflict. No PHASE GATE CONTRACT SUMMARY is added; C-45 is
not targeted.

**Hypothesis**: C-44 is a per-block structural property of B-NN blocks independent of which
roles are declared first. If Finance-first ordering changes which R-IDs appear in B-NN Cause
fields but does not change the `Exception Refs:` population (which depends on EX block
`Bottleneck Ref:` fields, not role ordering), then V-04 should achieve C-44 while maintaining
Finance-domain dual-cite quality. The combination tests independence of the two axes: role
ordering operates on the R-ID citation chain; `Exception Refs:` operates on the EX→B-NN
chain. C-45 should remain FAIL (no contract summary added).

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Finance-domain failure modes first.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools, handoffs, storage. Lead with Finance control point.]

**Incumbent failure modes** (Finance-domain failures first):

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [Finance-domain recurring failure] | [frequency] | [downstream financial control break] |
| IM-02 | [Second Finance-domain or cross-functional failure] | [frequency] | [downstream effect] |

**Cost of no action**: [Named financial measure with value or rate, before PHASE 1. Both IM-IDs
reachable from at least one B-NN Cause field.]

---

### Role Registry Gate

> GATE BLOCK. Finance roles declared with R-01 and R-02. All four checks must clear.

| R-ID | Role | Function |
|------|------|----------|
| R-01 | [Finance role — primary financial control] | [named financial function] |
| R-02 | [Finance role — secondary financial or approval] | [named responsibility] |
| R-03 | [Operations or Sales/Case role] | [named operational responsibility] |

Anti-generic validation (all four must clear):
- [ ] No R-ID entry uses "Approver" without a domain qualifier
- [ ] No R-ID entry uses "Owner" without a named responsibility
- [ ] Each R-ID referenced by at least one Decision Supplement block, Role Sequence Schedule,
      and at least one PHASE EXIT GATE Exit verification or Blocked bottleneck field
- [ ] Each declared R-ID appears in at least one EX block's `Role Ref:` sub-field

Role set by process type (Finance roles first):
- L2O → Finance Credit Analyst / Sales Manager / Sales Rep / Legal Counsel / Fulfillment Coordinator
- P2P → Finance Controller / Accounts Payable Specialist / Procurement Officer / Receiving Dock Supervisor
- Period Close → Controller / GL Manager / Finance Analyst / External Auditor
- Case Lifecycle → Case Manager / Legal Counsel / Support Engineer / Operations Coordinator

---

### Role Sequence Schedule

> Finance roles (R-01, R-02) declared first. B-NN Cause fields must cite the blocking
> Finance R-ID where the bottleneck is Finance-domain.

| Phase | Primary Owner (R-ID) | Activation Trigger | Handoff Trigger | Parallel Role (R-ID) | Parallel Window |
|-------|---------------------|-------------------|-----------------|----------------------|----------------|
| Phase 1 | R-[ID] | [Finance-domain event or external artifact] | [specific completion condition] | R-[ID] or NONE | [concurrent window or NONE] |
| Phase 2 | R-[ID] | [handoff from phase 1 — name artifact] | [completion condition] | R-[ID] or NONE | [concurrent activity or NONE] |

---

### Phase Structure

For each phase, produce the following five blocks in document order:

---

**PHASE [N] — [PHASE NAME]**

**PHASE ENTRY CONTRACT**

> Entry Condition references prior phase's PHASE EXIT GATE "Required outputs" by name.
> `Prior phase:` = Phase label (backward). `Prior phase blocked bottleneck:` = B-ID (entry).
> Both independently verifiable by string comparison.

- Entry Condition: [specific named artifact from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) — [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase: [Literal preceding phase identifier or NONE/INIT for Phase 1.]
- Prior phase blocked bottleneck: [B-ID from prior exit gate or NONE or N/A for Phase 1.]

**SECTION A — EXCEPTION TRACES**

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition]; Trace: [S-IDs]; Handling Role: R-[ID]; Terminal: [state or continues-via]
> - Why Problematic: [specific reason]
> - Bottleneck Ref: [B-NN or NONE. B-ID string-matches Bottleneck Analysis identifier.
>   The B-NN block below carries an `Exception Refs:` field that must list this EX block ID
>   if Bottleneck Ref is non-NONE — populate accurately for bidirectional consistency.]
> - Role Ref: [Literal R-ID of ROLE SEQUENCE SCHEDULE primary owner for this phase.]

Minimum 1 per phase; 3 total minimum. Bottleneck Ref and Role Ref independent; populate both.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules: Named Entry Condition required; Exits → S-ID or TERMINAL; standard Type values.

**Decision Supplement Blocks** (one per DECISION-type state):

> **DS-[S-ID]**: Condition / Owner R-[ID] / Branch A / Branch B / Fallback

**PHASE EXIT GATE**

> `Blocked bottleneck:` carries a B-ID. `Next phase:` carries a Phase label. Orthogonal.

- Exit Condition: [what the phase must produce to be complete]
- Required outputs: [named artifacts, decisions, or state records]
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) confirms all outputs present
- Blocking condition: [re-entry path or escalation if outputs absent]
- Blocked bottleneck: [B-NN or NONE. Must appear in Bottleneck Analysis AND next phase's `Prior phase blocked bottleneck:`.]
- Next phase: [Literal identifier of subsequent phase block. Last phase: NONE or END.]

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

> **PREAMBLE**: Each B-NN Cause field must satisfy both Dual-Cite Fail Conditions. Finance
> roles (R-01, R-02) must appear as the blocking R-ID in at least one B-NN Cause field.
>
> **Dual-Cite Fail Condition A** — no IM-ID literal string → fails.
> **Dual-Cite Fail Condition B** — no R-ID literal string → fails.
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

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field AND an Exception Refs field.**

---

**B-01 — [Finance-Domain Bottleneck Name]**

- Cause: [Required: IM-ID literal string AND R-ID literal string. Finance role (R-01 or R-02)
  as blocking R-ID where bottleneck is Finance-domain.]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails
- Impact: [downstream state, SLA node, or adjacent process]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: No AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01.]
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] — [Exception Name])`
  - Fail condition: NONE = dark bottleneck (gate violation). Listed EX block ID without
    matching `Bottleneck Ref: B-01` fails CHAIN STATUS B-NN→Exception consistency check.
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-01, or NONE.]

---

**B-02 — [Bottleneck Name]**

- Cause: [Required: IM-ID AND R-ID literal strings.]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: [same as B-01]
  - [List each AT-RISK SLA row citing B-02.]
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] — [Exception Name])`
  - Fail condition: NONE = dark bottleneck (gate violation).
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
- Phase-boundary B-NN continuity: [every exit gate B-ID matches next entry contract; list pairs]
- Phase-sequence: [every `Prior phase:` matches preceding block label; PHASE 1 NONE/INIT]
- Phase-exit-sequence: [every `Next phase:` matches subsequent block label; last phase NONE/END]
- Exception→B: [every EX `Bottleneck Ref:` B-ID matches a declared B-NN; list pairs]
- B-NN→Exception: [every declared B-ID has non-NONE `Exception Refs:`; each listed EX ID string-matches EX block with matching Bottleneck Ref; enumerate pairs; name dark bottlenecks]
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

## V-05 — Combination: Output Format + Lifecycle Emphasis (C-44 + C-45 + Inertia Framing)

**Variation axis**: Output format + Lifecycle emphasis + Inertia framing — maximum density
for the two new v14 criteria: isolated per-block `Exception Refs:` named instruction block
in each B-NN block (V-02 axis, C-44), dedicated PHASE GATE CONTRACT SUMMARY before PHASE 1
(V-03 axis, C-45), and prominent inertia framing with per-phase IM-reference callouts. The
INCUMBENT BASELINE's failure modes are echoed at the opening of each phase's SECTION A to
anchor exception traces to the specific incumbent failure pattern that phase is most likely
to expose. This tests whether per-phase incumbent anchoring improves dual-cite Evidence
field quality in addition to serving the inertia framing axis.

**Hypothesis**: V-05 is the minimum R14 configuration to achieve both C-44 and C-45
simultaneously. The isolated per-block `Exception Refs:` format (V-02 architecture) is more
robust than the R13 embedded-instruction approach for C-44. The dedicated PHASE GATE CONTRACT
SUMMARY section (V-03 architecture) is more robust than the R13 cross-block phrasing approach
for C-45. The combination of both in a single prompt body — with inertia framing providing
additional dual-cite anchoring — should achieve 37/37 aspirational coverage. If V-05 passes
both C-44 and C-45, V-02 and V-03 single-axis results will determine whether each criterion
requires its specific structural addition or whether the combination is necessary.

---

You are running **flow-lifecycle** for topic: {Topic}.

### INCUMBENT BASELINE

> Complete before the Role Registry Gate. Every B-NN Cause field must satisfy both Dual-Cite
> Fail Conditions. Quantified metric must appear before PHASE 1 in document order.
> This section is the inertia reference: every exception trace (SECTION A) and bottleneck
> (B-NN Cause) must trace back to a named IM-ID from this section.

**Process type**: [L2O / P2P / Period Close / Case Lifecycle — auto-detect from {Topic}]

**Incumbent description**: [1–3 sentences: tools used (spreadsheets, email, phone), handoff
mechanisms, where records are stored, who initiates the process manually. Include the primary
point where the incumbent fails under volume or time pressure.]

**Incumbent failure modes**:

| IM-ID | Failure Mode | Frequency | Downstream Effect |
|-------|-------------|-----------|------------------|
| IM-01 | [specific recurring failure — the one most visible to the Finance or Operations team] | [daily / per-cycle / per-exception] | [downstream effect on SLA or accuracy] |
| IM-02 | [second distinct failure mode — different process layer from IM-01] | [frequency] | [downstream effect] |

**Cost of no action**: [Named measure with current-state value or rate, declared before
PHASE 1. Must be specific enough to anchor B-NN Cause fields. Example: "Average credit
approval cycle time: 5.8 days vs 3-day SLA — IM-01 primary driver" or "Manual matching
error rate: 12% per period, IM-02 primary driver."]

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

> Declared after Role Registry Gate and before PHASE 1. Maps each R-ID to owned phases
> with activation triggers, handoff triggers, and parallel windows. B-NN Cause fields must
> cite the blocking R-ID (Dual-Cite Fail Condition B). R-IDs in EX block `Role Ref:` must
> match the schedule entry for the enclosing phase. Every declared R-ID must appear in at
> least one EX block Role Ref — the Role Registry Gate fourth check enforces this.

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
> their designated structural locations.
>
> | Field Name | Location | Value Type | Traceability Direction |
> |------------|----------|------------|----------------------|
> | `Prior phase:` | PHASE ENTRY CONTRACT | Phase label (e.g., "PHASE 1 — Initiation") | Phase→Phase, backward (entry side) |
> | `Prior phase blocked bottleneck:` | PHASE ENTRY CONTRACT | B-ID (e.g., "B-01") | B-NN boundary continuity, entry side |
> | `Next phase:` | PHASE EXIT GATE | Phase label (e.g., "PHASE 2 — Credit Review") | Phase→Phase, forward (exit side) |
>
> **ORTHOGONALITY DECLARATION:**
> `Prior phase blocked bottleneck:` carries a B-ID (string pattern: "B-" followed by digits).
> `Next phase:` carries a Phase label (string pattern: "PHASE N — [Name]" or NONE/END sentinel).
> These two fields carry orthogonal value types independently verifiable by string comparison:
> a B-ID in `Next phase:` is a detectable format violation; a Phase label in `Prior phase
> blocked bottleneck:` is a detectable format violation. No inference required — the patterns
> are non-overlapping by construction.
>
> `Prior phase:` and `Next phase:` form a symmetric bidirectional Phase→Phase pair:
> entry contracts declare backward linkage ("who preceded me?");
> exit gates declare forward linkage ("who follows me?").
> `Prior phase blocked bottleneck:` is orthogonal to both — it carries a B-ID, not a Phase label.
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
> the PHASE EXIT GATE below.
> `Prior phase:` carries a Phase label (backward). `Prior phase blocked bottleneck:` carries
> a B-ID (entry gate). These fields are orthogonal — see PHASE GATE CONTRACT SUMMARY.
> Entry Condition must reference the prior phase's PHASE EXIT GATE "Required outputs" by name.

- Entry Condition: [specific named artifact from prior phase's Required outputs]
- Pre-condition check: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) — [verification method]
- Blocking condition: [state entered and role notified if entry condition not met]
- Prior phase: [Literal identifier of preceding phase block, e.g., "PHASE 1 — Initiation".
  Phase 1: NONE or INIT sentinel. Non-first phase with sentinel fails. First phase with
  phase identifier fails. String-match to preceding phase block label required.]
- Prior phase blocked bottleneck: [B-ID from prior exit gate `Blocked bottleneck:` or NONE
  or N/A for Phase 1. String-match to prior exit gate AND B-NN block identifier required.
  Example: "B-01 (inherited from Phase 1 exit gate — incumbent IM-01 reconciliation delay
  still active at phase boundary; R-02 blocking per Role Sequence Schedule)."]

**SECTION A — EXCEPTION TRACES**

> Incumbent reference: the primary IM-ID most likely to manifest as an exception in this
> phase is [{IM-01 or IM-02 — identify the most relevant one}]. Exception traces in this
> phase should anchor to that IM-ID via their `Bottleneck Ref:` field where applicable.

For each exception trace originating in this phase:

> **EX-[Phase#][Letter] — [Exception Name]**
> - Trigger: [specific condition — name state, threshold breach, or missing input that the
>   incumbent process fails to prevent; cite the IM-ID it reflects where applicable]
> - Trace: [path of states from trigger to resolution or terminal; cite S-IDs in sequence]
> - Handling Role: R-[ID] ([role name])
> - Terminal: [terminal state name] or [continues-via: S-[ID]]
> - Why Problematic: [specific operational or compliance reason; cite the incumbent failure
>   mode (IM-ID) that this exception represents or enables]
> - Bottleneck Ref: [B-NN that enabled this exception, or NONE. B-ID must string-match a
>   Bottleneck Analysis identifier. The B-NN block's `Exception Refs:` field must list this
>   EX block ID if Bottleneck Ref is non-NONE — populate accurately for chain consistency.
>   NONE only if no declared bottleneck was causal.]
> - Role Ref: [R-ID of the ROLE SEQUENCE SCHEDULE primary owner for this phase. Literal R-ID
>   matching the schedule's Primary Owner entry for the phase containing this exception.
>   Free-text without R-ID fails. R-ID absent from schedule fails.]

Minimum 1 exception trace per phase; 3 total minimum.
Every declared R-ID in the Role Registry Gate must appear in at least one EX block Role Ref.
Bottleneck Ref and Role Ref are independent; populate both for every EX block.

**SECTION B — STATE TRANSITION TABLE**

| S-ID | State Name | Entry Condition | Exits | Owner (R-ID) | Type |
|------|-----------|-----------------|-------|--------------|------|

Rules:
- Every state must have a named Entry Condition. "Ready" or "Previous step complete" fails.
- Every Exit must reference a destination S-ID or carry the label TERMINAL.
- Type values: NORMAL / DECISION / PARALLEL-FORK / PARALLEL-JOIN / EXCEPTION / TERMINAL

**Decision Supplement Blocks** (one per DECISION-type state in this phase):

> **DS-[S-ID] — [State Name]**
> - Condition: [rule or threshold evaluated at this decision point]
> - Owner: R-[ID] ([role name from Role Registry])
> - Branch A ([outcome]): → S-[ID] ([state name])
> - Branch B ([outcome]): → S-[ID] ([state name]) or TERMINAL
> - Fallback: [action if condition cannot be evaluated — who is notified, what state is entered]

**PHASE EXIT GATE**

> Phase Gate Contract field 3 lives here: `Next phase:` (Phase label, forward).
> `Blocked bottleneck:` carries a B-ID. `Next phase:` carries a Phase label.
> These are orthogonal value types — see PHASE GATE CONTRACT SUMMARY.
> The B-ID in `Blocked bottleneck:` is inherited by the next phase's PHASE ENTRY CONTRACT
> `Prior phase blocked bottleneck:`. The Phase label in `Next phase:` is the string target
> for the next phase's block header — verifiable without inference.

- Exit Condition: [what the phase must have produced to be considered complete]
- Required outputs: [named artifacts, decisions, or state records that must exist]
- Exit verification: R-[ID] ([role name — must match Role Sequence Schedule primary owner]) confirms all required outputs present
- Blocking condition: [if required outputs absent: re-entry path or escalation]
- Blocked bottleneck: [B-NN or NONE. Must string-match Bottleneck Analysis identifier AND
  next phase's `Prior phase blocked bottleneck:`. Format: "B-NN" — a B-ID. Not a Phase label.]
- Next phase: [Literal identifier of the subsequent phase block, e.g., "PHASE 2 — Credit
  Review". Last phase: NONE or END sentinel. Must string-match next phase block label in
  document order. Format: "PHASE N — [Name]" — a Phase label. Not a B-ID. See PHASE GATE
  CONTRACT SUMMARY orthogonality declaration.]

---

[Repeat Phase Structure for each phase. Minimum 2 phases required.]

---

### Parallel Path Modeling

- **FORK at**: S-[ID] ([state name])
- **Branch 1**: [states traversed; cite S-IDs in sequence]
- **Branch 2**: [states traversed; cite S-IDs in sequence]
- **JOIN at**: S-[ID] ([join state name])
- **Join Condition**: AND-join / OR-join — specify which and explain why this process requires it

---

### Edge Case Enumeration

At least three edge cases distinct from SECTION A exception flows:

> **EC-[N] — [Edge Case Name]**
> - Triggering Condition: [specific scenario; note whether incumbent process would detect this]
> - Why Problematic: [specific reason outside documented handling; cite IM-ID if applicable]
> - Correct Response: R-[ID] ([role name]) — [specific correct action; name target state]

---

### Cross-Process Interaction Modeling

> **CROSS-PROCESS HANDOFF — {Topic} lifecycle → [adjacent process name]**
> - Sending State: S-[ID] ([state name])
> - Receiving Process: [adjacent process name]
> - Data Payload: [named fields or record types transferred]
> - Expected Acknowledgment: [signal or confirmation from receiving process]
> - Failure Mode: [what happens if acknowledgment not received within SLA]
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
>
> **Dual-Cite Fail Condition A** — Cause field contains no IM-ID literal string (e.g., "IM-01"):
> fails C-39. Verify: search Cause field for "IM-" followed by digits. Absence → fail.
>
> **Dual-Cite Fail Condition B** — Cause field contains no R-ID literal string (e.g., "R-02"):
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
> (1) Concrete named domain example (`"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`)
> must appear in BOTH this preamble AND each B-NN per-block Evidence hint.
> (2) Labeled axes (`Required format:` / `Fail condition:`) must appear in BOTH this preamble
> AND each B-NN per-block Evidence hint.
>
> **B-NN→Exception Gate Check**: Every declared B-ID must appear in at least one EX block's
> `Bottleneck Ref:` sub-field across all phases. A B-ID absent from all EX blocks is a "dark
> bottleneck" — declared failure mode with no exception-phase trace. Dark bottlenecks are gate
> violations. Verify after all phases: scan EX blocks for each B-ID literal string. Absence →
> gate violation. Report in CHAIN STATUS `B-NN→Exception` direction.
>
> Anti-embedding: Declare CHAIN STATUS in its own dedicated top-level section after SLA ANALYSIS.

**SCAFFOLD REQUIREMENT: ALL B-NN blocks declared below must carry an Evidence field AND an Exception Refs field.**

---

**B-01 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string (Condition A) AND R-ID literal string (Condition B).
  Cite the IM-ID from INCUMBENT BASELINE that this bottleneck instantiates. Example: "IM-01
  (manual spreadsheet GL reconciliation) combined with R-02 (GL Manager) period-close peak
  unavailability — queue accumulation at S-05. 'IM-01' satisfies A; 'R-02' satisfies B."]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream state, SLA node, or adjacent process affected by this bottleneck]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-01`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-01. Example: `"S-05: Credit Hold Review -- AT-RISK, causal source: B-01"`]
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] — [Exception Name])`
  - Fail condition: NONE declared here = dark bottleneck (gate violation): B-01 is declared
    as a process failure mode but has no exception-phase trace, leaving the causal chain from
    bottleneck to observable exception unverifiable. A listed EX block ID that does not have
    `Bottleneck Ref: B-01` in the cited EX block fails the CHAIN STATUS B-NN→Exception
    consistency check — the forward and reverse citations must be string-consistent.
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-01. Example:
    `"EX-1A (Phase 1 — Credit Limit Exceeded), EX-2B (Phase 2 — Approval Queue Timeout)"`]

---

**B-02 — [Bottleneck Name]**

- Cause: [Required: IM-ID literal string AND R-ID literal string. Cite the IM-ID from
  INCUMBENT BASELINE that this bottleneck instantiates.]
  - Dual-Cite Fail Condition A: Cause contains no IM-ID string → fails C-39
  - Dual-Cite Fail Condition B: Cause contains no R-ID string → fails C-39
- Impact: [downstream effect]
- Evidence:
  - Required format: `[State name -- S-ID]: AT-RISK, causal source: B-02`
  - Fail condition: A field containing only "see SLA ANALYSIS" or state names without
    AT-RISK row-level S-ID specificity does not satisfy.
  - [List each AT-RISK SLA row citing B-02. Example: `"S-07: Invoice Matching -- AT-RISK, causal source: B-02"`]
- Exception Refs:
  - Required format: `EX-[Phase#][Letter] (Phase [N] — [Exception Name])`
  - Fail condition: NONE = dark bottleneck (gate violation). Listed ID without matching
    `Bottleneck Ref: B-02` in cited EX block fails consistency check.
  - [List each EX block identifier whose `Bottleneck Ref:` cites B-02, or NONE.]

---

**Gap Identification**

> MISSING: [step name] — [rationale: why it belongs; which incumbent failure mode (IM-ID)
> it would reduce; which phase; what exception or bottleneck its absence enables]

---

### CHAIN STATUS

> Anti-embedding: Dedicated top-level section. Not embedded in SLA ANALYSIS.

CHAIN STATUS: [CLOSED / OPEN]

- Forward (SLA→B): [every AT-RISK SLA row cites a B-ID; enumerate pairs or name gap]
- Backward (B→SLA): [every B-NN Evidence field lists AT-RISK SLA rows citing it; enumerate or name gap]
- Exit gate consistency: [every PHASE EXIT GATE `Blocked bottleneck:` B-ID string-matches a declared B-NN; name any mismatch]
- Phase-boundary B-NN continuity: [every exit gate `Blocked bottleneck:` B-ID string-matches next phase's `Prior phase blocked bottleneck:`; list phase pairs or name break]
- Phase-sequence: [every PHASE ENTRY CONTRACT `Prior phase:` identifier string-matches preceding phase block label; PHASE 1 carries NONE/INIT sentinel; list pairs or name mismatch]
- Phase-exit-sequence: [every PHASE EXIT GATE `Next phase:` identifier string-matches subsequent phase block label; last phase carries NONE/END sentinel; list exit gate→next phase pairs or name any mismatch]
- Exception→B: [every EX block `Bottleneck Ref:` B-ID (non-NONE) matches a declared B-NN; list EX→B-NN pairs or name unresolved block]
- B-NN→Exception: [every declared B-ID has at least one non-NONE entry in its `Exception Refs:` field; each listed EX block ID string-matches an EX block with `Bottleneck Ref:` citing this B-ID; enumerate B-ID→EX block pairs from Exception Refs; name any B-ID with NONE in Exception Refs (dark bottleneck) or any listed EX ID whose referenced block does not carry matching Bottleneck Ref]
- Exception→Role: [every EX block `Role Ref:` R-ID matches ROLE SEQUENCE SCHEDULE primary owner for enclosing phase; list EX→R-ID pairs or name mismatch]
- Role→Exception: [every declared R-ID in the Role Registry Gate appears in at least one EX block's `Role Ref:`; list R-ID→EX block pairs; name any R-ID with no EX trace (dark role)]
- Dual-cite status: [every B-NN Cause contains both IM-ID and R-ID string; name any block missing either]
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
