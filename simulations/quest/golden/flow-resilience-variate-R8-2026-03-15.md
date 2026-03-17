# Flow-Resilience Skill — Round 8 Variations (Rubric v8)

**Skill**: flow-resilience — Simulate degraded conditions: offline, partial failure, eventual consistency.
**Rubric**: v8 (C-01 through C-28, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Round 8 Context

**New criterion entering R8**: C-28 -- Post-Analysis Rule Registry Audit.

**R7 diagnosis**:
- V-03 (R7) introduced a named terminal section "Post-Analysis Registry Audit" that reviews
  the rule registry after all gates complete and reports per-rule invocation status. C-28
  extracts this as a required criterion: every rule must be accounted for as INVOKED (with
  gate + entry citations), SCENARIO-ABSENT (triggering condition never arose), or
  RULE-BYPASSED (condition arose but rule not applied — an audit failure). A registry that is
  declared but never post-audited cannot prove invocations actually occurred.
- V-05 (R7) achieved the highest integration ceiling entering R8: all three of C-25, C-26,
  and C-27 plus full R6 formalization. R8 variations must extend that ceiling by targeting
  C-28 while keeping accumulated criteria intact.

**Variation axes selected**:
- V-01: Single axis — Role sequence (DS Expert owns gates, Commerce Validator owns domain pass)
- V-02: Single axis — Output format (table-dominant at every gate)
- V-03: Single axis — Lifecycle emphasis (explicit GATE-OPEN / GATE-CLOSE boundary blocks)
- V-04: Combination — Phrasing register (conversational/imperative) + Inertia framing
- V-05: Full integration — Role sequence + lifecycle emphasis + table registry audit + all C-01–C-28

---

## V-01

**Variation axis**: Role sequence — DS Expert owns the gate protocol (Acts 1–4); Commerce
Domain Validator runs a separate post-gate domain pass (Act 2) then co-signs the registry audit.

**Hypothesis**: Blending the DS and commerce roles in a single pass causes commerce anchoring
to be satisfied superficially — scenarios get a commerce label grafted on after DS logic
determines their shape. Separating the roles forces the DS expert to produce technically
rigorous scenarios without worrying about commerce vocabulary, then the commerce validator
grounds them in real flows. The registry audit gains a second signer, making RULE-BYPASSED
findings more visible.

---

You are running the **flow-resilience** skill for a software feature in active development.
This analysis runs in two sequential acts with distinct roles. Do not blend them.

---

### RULE REGISTRY

All conditional linkage rules are declared here before any analysis begins.
Gate sections cite rules by ID — they do not restate the logic inline.

**RULE-CR-DCV**: If a scenario involves concurrent state modification by multiple actors
without a coordination mechanism, classify the conflict as a named Data Consistency Violation
and assign it a DCV-NN identifier in the Gap Identification gate.

**RULE-BARRED-CG**: If a discovery entry's confidence basis cannot be resolved from available
context, mark the entry BARRED and emit a named Coverage Gap (CG-NN) entry recording the
unresolvable basis. The CG entry persists in the coverage log regardless of whether the
BARRED entry is later resolved.

**RULE-NIL-SUPERSEDE**: If a downstream gate or amendment introduces a gap finding in a
category that previously held a typed nil identifier, annotate the nil SUPERSEDED citing
the new finding ID. Format: `OEG-NIL-1: SUPERSEDED by OEG-F-02`.

**RULE-COMMERCE-ANCHOR**: If a scenario in the Include column references only a generic
operation (e.g., "data write", "state update") with no named commerce flow, Act 2 Commerce
Validator must amend it to name a specific commerce operation and record the amendment under
COMMERCE VALIDATION AMENDMENTS.

---

## ACT 1 — DISTRIBUTED SYSTEMS EXPERT

You are a distributed systems expert. Your responsibility: triage failure scenarios with
technical rigor, run the four-gate protocol, manage the nil lifecycle, invoke registry rules
at every trigger point, and close all gates before handing off to Act 2.

### Pre-Analysis: Commerce Operation Scope Declaration

Before Gate 1, declare the commerce operations in scope for this analysis run.
Minimum four operations from: checkout, inventory reservation, payment processing,
order fulfillment, cart state, loyalty redemption, return/refund.

```
SCOPE DECLARATION
Operations in scope: [list each]
Operations explicitly excluded (with reason): [list or "none"]
```

SCOPE DECLARATION COMPLETE

### Pre-Analysis: Coverage Accountability Roster

Commit to minimum scenario slots per degradation class before Gate 1.
Minimum two per class.

| Degradation Class | Committed Minimum | Actual (fill after Gate 2) |
|---|---|---|
| Network partition / offline | 2 | |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

If a class slot cannot be filled, provide a DS-primitive-grounded impossibility argument
citing a specific CAP theorem guarantee, deployment topology constraint, or synchronous
consistency guarantee that forecloses the class.

DS Primitive cited: [required field for every impossibility claim]
VALID: "Under CP topology, network partitions prevent divergent writes — eventual
consistency lag cannot arise in this configuration."
INVALID: "The topic doesn't mention caching, so this class doesn't apply."

---

### GATE 1: Discovery and Triage

Entry condition: SCOPE DECLARATION COMPLETE block present.

For each failure scenario candidate:
- Assign ID (FS-NN)
- Classify failure class: `Network partition / offline` | `Partial service failure` |
  `Eventual consistency`
- State confidence basis (what context or architecture constraint justifies this scenario)
- Assign disposition: `Include` | `BARRED` | `Argued-Impossible`

For BARRED: cite RULE-BARRED-CG; state the unresolvable basis; emit CG-NN entry.
For Argued-Impossible: cite DS Primitive by name; record impossibility argument.

Disposition table: ID | Failure Class | Confidence Basis | Disposition | Notes

**GATE 1b — BARRED Resolution Check**

After initial triage, evaluate each BARRED entry. If the confidence basis can be resolved:
- Record under `GATE 1b: RESOLVED` — entry ID, satisfied basis, resolution mechanism,
  new disposition (Include), triage gate re-closed.

If no BARRED entries resolve: "No BARRED-to-Include upgrades in this run."

GATE 1 STATUS: [OPEN | CLOSED]
Reason if OPEN: [name the specific blocking entry or unmet condition]

---

### GATE 2: Four-Field Scenario Analysis

Entry condition: GATE 1 STATUS: CLOSED

For each scenario in Include, produce all four required fields with non-trivial content:

1. **State** — Specific system state when failure occurs. Not "system is degraded."
2. **Capability** — Named actions the user can still take. Not "partial functionality."
3. **Data at risk** — Name the data type and the consistency failure mode.
4. **Recovery path** — Concrete steps back to healthy state. Each step names the actor:
   `client` | `server` | `operator` | `user`. Minimum two actor-labeled steps per path.

Annotate each scenario:
- **Severity**: `degraded` | `impaired` | `down`
- **Blast radius**: fraction or segment affected

For any scenario with concurrent modification: invoke RULE-CR-DCV.
Record invocation inline: "RULE-CR-DCV invoked — Gate 2, FS-NN → DCV-NN pending Gate 3."

GATE 2 STATUS: [OPEN | CLOSED]
Reason if OPEN: [blocking condition]

---

### GATE 3: Gap Identification

Entry condition: GATE 2 STATUS: CLOSED

Identify findings in all three mandatory categories.

**OEG — Offline Experience Gaps**
For each gap: assign OEG-NN. State what the user cannot do offline that the system
does not handle or surface clearly, and why it matters to the user.
If no gaps: `OEG-NIL-1: [scope rationale — explain why offline experience gaps do not
arise for this deployment pattern; bare "none found" does not satisfy this criterion]`

**DCV — Data Consistency Violations**
For each violation: assign DCV-NN. Name the data and consistency failure mode.
For RULE-CR-DCV entries pending from Gate 2: assign the DCV-NN now and confirm linkage.
If no violations: `DCV-NIL-1: [scope rationale]`

**MRF — Missing Recovery Flows**
For each missing flow: assign MRF-NN. Name the scenario and the absent mechanism.
If no missing flows: `MRF-NIL-1: [scope rationale]`

**Conflict Resolution Analysis**

For each eventual-consistency scenario from Gate 2:
- Name the conflict resolution strategy: `last-write-wins` | `merge` | `manual-reconcile` |
  `reject-stale` | `undefined`
- Adequacy verdict: `adequate` | `inadequate` | `undefined`
- If inadequate or undefined: invoke RULE-CR-DCV → emit DCV-CR-NN linked to this source.
  Format: "DCV-CR-NN: [description] — source: conflict-resolution adequacy failure at FS-NN"
- If all strategies adequate: CONFLICT RESOLUTION CLOSED — no DCV-CR findings generated.

GATE 3 STATUS: [OPEN | CLOSED]
Reason if OPEN: [blocking condition]

---

### GATE 4: Amendment Pass

Entry condition: GATE 3 STATUS: CLOSED

Review all Gate 2 scenarios and Gate 3 findings for required amendments:
- Recovery paths too vague (missing actor-labeled steps) → amend → record entry ID,
  original, amended, triggering reason.
- Gate 3 findings that override a prior typed nil → invoke RULE-NIL-SUPERSEDE →
  annotate the nil SUPERSEDED with the superseding finding ID.
- RULE-CR-DCV invocations from Gate 2 whose DCV-NN entries were assigned in Gate 3 →
  confirm the Gate 2 → Gate 3 linkage is traceable.
- Downstream conflict-resolution finding requiring a DCV amendment to a closed Gate 3
  section → reopen Gate 3 under `GATE 3: AMENDED` → apply amendment → re-close.

If no gate re-opens triggered: "No gate re-opens in this run."

GATE 4 STATUS: [OPEN | CLOSED]
Reason if OPEN: [blocking condition]

---

## ACT 2 — COMMERCE DOMAIN VALIDATOR

Entry condition: GATE 4 STATUS: CLOSED

Review all scenarios produced in Act 1 (Gates 1–4). For each scenario:
1. Is it anchored to a named commerce operation from the scope declaration?
2. If not: invoke RULE-COMMERCE-ANCHOR — amend to name the commerce operation.
   Record under COMMERCE VALIDATION AMENDMENTS: scenario ID, original operation
   description, amended operation name.

Review OEG, DCV, and MRF findings for commerce-domain-specific issues that Act 1 may not
have surfaced (inventory oversell under partition, payment idempotency window expiry,
loyalty point double-redemption, order state divergence under partial fulfillment failure).
Issue any additional findings as CV-DCV-NN, CV-OEG-NN, or CV-MRF-NN.

```
COMMERCE VALIDATION COMPLETE
Scenarios reviewed: [N]
RULE-COMMERCE-ANCHOR invocations: [N — or "none"]
Additional commerce-domain findings: [list with IDs — or "none"]
```

---

## TERMINAL: Nil Supersession Log

List every typed nil identifier issued across both acts. For each:
- Identifier
- State: `ACTIVE` | `SUPERSEDED`
- If SUPERSEDED: cite the superseding finding ID and gate/act where supersession occurred.

If no nil was superseded: "No supersessions in this run."

---

## TERMINAL: Scope Verification

Cross-check the pre-analysis scope declaration against the final scenario table.

| Operation Declared | Covered by Scenario | Gap Finding (if any) |
|---|---|---|
| [each operation] | Yes / No | [gap ID or —] |

Any declared operation without scenario coverage and without an impossibility argument
is an unclosed scope gap. Record as SV-GAP-NN.

SCOPE VERIFICATION COMPLETE

---

## TERMINAL: Post-Analysis Rule Registry Audit

After all gates, acts, and terminal blocks complete, audit every registered rule.
For each rule in the registry, report:
1. **Invocation count** — how many times it fired
2. **Citations** — specific gate and entry ID for each invocation
3. **Status**: `INVOKED` | `SCENARIO-ABSENT` | `RULE-BYPASSED`

Status definitions:
- `INVOKED`: rule fired; all invocations cited by gate and entry.
- `SCENARIO-ABSENT`: triggering condition never arose in this run. Acceptable.
- `RULE-BYPASSED`: triggering condition arose but rule was not applied. Audit failure —
  reopen the affected gate, apply the rule, re-close before completing this block.

| Rule ID | Invocation Count | Citations | Status |
|---|---|---|---|
| RULE-CR-DCV | | | |
| RULE-BARRED-CG | | | |
| RULE-NIL-SUPERSEDE | | | |
| RULE-COMMERCE-ANCHOR | | | |

POST-ANALYSIS REGISTRY AUDIT COMPLETE
Act 1 (DS Expert) sign-off: [confirm all rules accounted for]
Act 2 (Commerce Validator) sign-off: [confirm RULE-COMMERCE-ANCHOR status accurate]

---

---

## V-02

**Variation axis**: Output format — table-dominant at every gate. Every gate produces a
structured table; prose is reserved for impossibility arguments and scope rationale only.
The registry audit is a verification table, not a narrative block.

**Hypothesis**: When each gate outputs a table with explicit column headers, a scorer can
verify C-01 through C-28 by scanning column completeness rather than parsing prose. The
four required fields of C-02 become column headers — a missing column is immediately
visible. The registry audit becomes a checkable grid rather than a prose description of
what fired.

---

You are running the **flow-resilience** skill for a software feature in active development.

Output format rule: every gate produces a Markdown table as its primary artifact. Prose
annotations are permitted only for impossibility arguments, scope rationale in nil findings,
and actor-labeled steps in recovery paths (which must remain inline in table cells, not
as separate prose blocks).

---

### RULE REGISTRY

| Rule ID | Trigger Condition | Action | Target Section |
|---|---|---|---|
| RULE-CR-DCV | Scenario has concurrent state modification by multiple actors without coordination mechanism | Classify as DCV finding; assign DCV-NN | Gate 3: DCV section |
| RULE-BARRED-CG | Discovery entry confidence basis cannot be resolved | Mark BARRED; emit CG-NN entry | Gate 1 coverage log |
| RULE-NIL-SUPERSEDE | Downstream finding introduced in category that held a typed nil | Annotate nil SUPERSEDED citing new finding ID | Gate 4 nil audit |
| RULE-COMMERCE-ANCHOR | Include scenario references generic operation only (no named commerce flow) | Amend to name specific commerce operation | Gate 5 commerce pass |

---

### Pre-Analysis: Commerce Operation Scope Declaration

Declare before Gate 1.

| Operation | In Scope | Exclusion Reason (if any) |
|---|---|---|
| [operation name] | Yes / No | |
| ... | | |

Minimum four operations in scope.

SCOPE DECLARATION COMPLETE

### Pre-Analysis: Coverage Accountability Roster

| Degradation Class | Committed Minimum | DS Primitive for Impossibility (if unable to fill) |
|---|---|---|
| Network partition / offline | 2 | |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

If a class slot cannot be filled, populate the DS Primitive column with a specific
architecture constraint. "The topic doesn't mention X" is not a valid entry.

---

### GATE 1: Discovery and Triage

| ID | Failure Class | Confidence Basis | Disposition | Rule Applied | Notes |
|---|---|---|---|---|---|
| FS-01 | | | Include / BARRED / Argued-Impossible | | |
| ... | | | | | |

For every BARRED entry: cite RULE-BARRED-CG in the Rule Applied column.
For every Argued-Impossible entry: name the DS Primitive in the Notes column.

**GATE 1b — BARRED Resolution Check**

| BARRED Entry ID | Confidence Basis | Resolved? | Resolution Mechanism | New Disposition |
|---|---|---|---|---|
| FS-NN | | Yes / No | | Include / Remains BARRED |

If no BARRED entries: "Gate 1b: no BARRED entries to resolve."

Coverage Gap Log (for permanently BARRED entries):

| CG ID | Entry ID | Unresolvable Basis | Gap Classification |
|---|---|---|---|
| CG-01 | FS-NN | | Permanently BARRED |

GATE 1 STATUS: OPEN / CLOSED
Reason if OPEN: [specific blocking entry or condition]

---

### GATE 2: Four-Field Scenario Analysis

| ID | State | Capability | Data at Risk | Recovery Path (actor-labeled steps) | Severity | Blast Radius | Rule Applied |
|---|---|---|---|---|---|---|---|
| FS-01 | | | | 1. [actor]: [action]; 2. [actor]: [action] | degraded / impaired / down | | |
| ... | | | | | | | |

Column requirements:
- **State**: specific system state, not "degraded."
- **Capability**: named actions, not "partial functionality."
- **Data at risk**: name the data type and failure mode.
- **Recovery path**: minimum two actor-labeled steps in the cell.
- **Severity**: exactly one of `degraded` | `impaired` | `down`.
- **Blast radius**: fraction or segment (e.g., "all users with active carts").
- **Rule Applied**: cite RULE-CR-DCV if concurrent modification present.

GATE 2 STATUS: OPEN / CLOSED
Reason if OPEN: [scenario ID with missing field or unmet condition]

---

### GATE 3: Gap Identification

**OEG — Offline Experience Gaps**

| ID | Scenario Ref | Gap Description | Actionable Recommendation |
|---|---|---|---|
| OEG-01 | FS-NN | | |

If no OEG findings: `OEG-NIL-1` — [scope rationale explaining why offline experience
gaps do not arise for this deployment pattern].

**DCV — Data Consistency Violations**

| ID | Source | Data Type | Consistency Failure | Conflict Resolution Strategy | Adequacy Verdict | Rule Applied |
|---|---|---|---|---|---|---|
| DCV-01 | FS-NN | | | last-write-wins / merge / manual / reject-stale / undefined | adequate / inadequate / undefined | |

For inadequate or undefined verdicts: invoke RULE-CR-DCV in the Rule Applied column;
the DCV entry becomes DCV-CR-NN with source linkage.

If no DCV findings: `DCV-NIL-1` — [scope rationale].
If all conflict-resolution strategies adequate: CONFLICT RESOLUTION CLOSED.

**MRF — Missing Recovery Flows**

| ID | Scenario Ref | Recovery Gap | Why No Current Path Exists |
|---|---|---|---|
| MRF-01 | FS-NN | | |

If no MRF findings: `MRF-NIL-1` — [scope rationale].

GATE 3 STATUS: OPEN / CLOSED
Reason if OPEN: [gap category missing or nil rationale absent]

---

### GATE 4: Amendment Pass

| Amendment ID | Entry ID | Original Content (summary) | Amended Content (summary) | Rule Invoked | Gate Re-Opened? |
|---|---|---|---|---|---|
| AMD-01 | FS-NN or finding ID | | | RULE-NIL-SUPERSEDE / none | Gate 3: AMENDED / no |

If a RULE-NIL-SUPERSEDE invocation is required, also update the nil entry in Gate 3:
`[NIL-ID]: SUPERSEDED by [finding ID] — Gate 4, AMD-NN`

If no amendments: "Gate 4: no amendments required."
If no gate re-opens: "No gate re-opens triggered in this run."

GATE 4 STATUS: OPEN / CLOSED
Reason if OPEN: [outstanding amendment or unresolved supersession]

---

### GATE 5: Commerce Domain Validation

Entry condition: GATE 4 STATUS: CLOSED

| Scenario ID | Commerce Operation Named? | Amended Operation (if RULE-COMMERCE-ANCHOR applied) |
|---|---|---|
| FS-01 | Yes / No | |

Additional commerce-domain findings:

| ID | Type | Finding | Source Scenario |
|---|---|---|---|
| CV-DCV-01 | DCV | | FS-NN |

COMMERCE VALIDATION COMPLETE

---

## TERMINAL: Nil Supersession Log

| Nil ID | Gap Type | State | Superseded By | Gate / Act |
|---|---|---|---|---|
| OEG-NIL-1 | OEG | ACTIVE / SUPERSEDED | OEG-F-02 / — | Gate 4 / — |

If no supersessions: "No supersessions in this run."

---

## TERMINAL: Scope Verification

| Declared Operation | Scenario Coverage | Gap Finding |
|---|---|---|
| [operation] | Yes / No | SV-GAP-NN / — |

SCOPE VERIFICATION COMPLETE

---

## TERMINAL: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Gate Citations (gate, entry) | Status |
|---|---|---|---|
| RULE-CR-DCV | [N] | Gate 2 FS-NN→DCV-NN; Gate 3 conflict verdict | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED |
| RULE-BARRED-CG | [N] | Gate 1 FS-NN→CG-NN | |
| RULE-NIL-SUPERSEDE | [N] | Gate 4 AMD-NN, NIL-ID | |
| RULE-COMMERCE-ANCHOR | [N] | Gate 5 FS-NN | |

Status definitions in table context:
- **INVOKED**: row has citation(s) in the Gate Citations column.
- **SCENARIO-ABSENT**: triggering condition absent from run; acceptable.
- **RULE-BYPASSED**: condition arose but rule not applied; reopens affected gate before
  this block can be marked COMPLETE.

POST-ANALYSIS REGISTRY AUDIT COMPLETE

---

---

## V-03

**Variation axis**: Lifecycle emphasis — every gate opens with a named GATE-OPEN block
stating preconditions and closes with a named GATE-CLOSE block stating exit postconditions
and an explicit CLOSED confirmation. No gate may proceed without satisfying its GATE-OPEN
conditions; no gate may be declared closed without satisfying its GATE-CLOSE conditions.

**Hypothesis**: The existing gate protocol declares entry conditions in prose and appends
a STATUS line at the end. Formalizing the boundary into two named blocks — GATE-OPEN and
GATE-CLOSE — makes closure independently auditable: a reader can locate all GATE-CLOSE
blocks without reading gate prose. It also makes GATE-OPEN conditions checkable before
the analyst starts the gate content, preventing skip-ahead errors that leave entry
conditions unsatisfied.

---

You are running the **flow-resilience** skill for a software feature in active development.

Lifecycle rule: every analysis gate is bounded by two named blocks — a GATE-OPEN block
and a GATE-CLOSE block. A gate that begins without a GATE-OPEN block has no confirmed
entry state. A gate that ends without a GATE-CLOSE block is implicitly OPEN. Neither
condition is acceptable.

---

### RULE REGISTRY

**RULE-CR-DCV**: If a scenario involves concurrent state modification by multiple actors
without a coordination mechanism → emit named DCV-NN finding in Gate 3.

**RULE-BARRED-CG**: If a discovery entry's confidence basis is unresolvable → mark BARRED
→ emit CG-NN in coverage log. Record invocation: "RULE-BARRED-CG at Gate 1, FS-NN → CG-NN."

**RULE-NIL-SUPERSEDE**: If a downstream finding introduces a gap in a category that held
a typed nil → annotate nil SUPERSEDED citing new finding ID.
Record invocation: "RULE-NIL-SUPERSEDE at Gate 4, AMD-NN → NIL-ID: SUPERSEDED by F-NN."

**RULE-COMMERCE-ANCHOR**: If an Include scenario has no named commerce operation → amend
with specific commerce operation.
Record invocation: "RULE-COMMERCE-ANCHOR at Gate 5, FS-NN → [amended operation]."

---

### Pre-Analysis: Commerce Operation Scope Declaration

Declare all commerce operations in scope before Gate 1. Minimum four.

Operations in scope: [list]
Operations explicitly excluded (with reason): [list or "none"]

SCOPE DECLARATION COMPLETE

### Pre-Analysis: Coverage Accountability Roster

Commit to minimum per-class coverage before Gate 1. Minimum two per class.

| Degradation Class | Committed Minimum |
|---|---|
| Network partition / offline | 2 |
| Partial service failure | 2 |
| Eventual consistency | 2 |

For any class that cannot reach two scenarios: provide a DS-primitive-grounded
impossibility argument. DS Primitive cited: [required field].
VALID: architecture constraint that forecloses the class.
INVALID: description-scope argument ("the topic doesn't mention X").

---

### GATE 1: Discovery and Triage

```
GATE 1 OPEN
Preconditions:
  [x] SCOPE DECLARATION COMPLETE block present
  [x] Coverage Accountability Roster committed
Entry confirmed: [yes / no — resolve before proceeding]
```

For each failure scenario candidate:
- ID (FS-NN), failure class, confidence basis, disposition: `Include` | `BARRED` |
  `Argued-Impossible`
- BARRED: cite RULE-BARRED-CG; emit CG-NN naming unresolvable basis.
- Argued-Impossible: cite DS Primitive.

Disposition table: ID | Failure Class | Confidence Basis | Disposition | Notes

**Gate 1b — BARRED Resolution Sub-Gate**

```
GATE 1b OPEN
Precondition: Gate 1 discovery complete; BARRED entries identified.
```

For each BARRED entry: can the confidence basis be resolved?
- If yes: record `GATE 1b: RESOLVED` — entry ID, satisfied basis, mechanism, new
  disposition (Include), Gate 1b re-closed.
- If no: entry remains BARRED; CG entry stands.
If no BARRED entries: "Gate 1b: no BARRED entries present."

```
GATE 1b CLOSE
Exit postconditions:
  [ ] Every BARRED entry either has a GATE 1b: RESOLVED record or a standing CG entry
  [ ] No BARRED entry silently promoted to Include without a resolution record
Gate 1b STATUS: CLOSED / OPEN
Reason if OPEN: [specific entry ID and unmet condition]
```

```
GATE 1 CLOSE
Exit postconditions:
  [ ] Every candidate has exactly one named disposition
  [ ] Every BARRED entry has a CG-NN entry in the coverage log
  [ ] Every Argued-Impossible entry cites a DS Primitive by name
  [ ] Coverage Accountability Roster updated with actual counts
  [ ] No free-text confidence description used in place of a named disposition
Gate 1 STATUS: CLOSED / OPEN
Reason if OPEN: [specific blocking entry or condition]
```

---

### GATE 2: Four-Field Scenario Analysis

```
GATE 2 OPEN
Preconditions:
  [x] Gate 1 STATUS: CLOSED
Entry confirmed: [yes / no]
```

For each scenario in Include, produce all four required fields:
1. **State** — Specific system state at failure onset.
2. **Capability** — Named actions the user can still take.
3. **Data at risk** — Named data type and consistency failure mode.
4. **Recovery path** — Concrete steps; each step names the actor:
   `client` | `server` | `operator` | `user`. Minimum two steps.

Annotate: Severity (`degraded` | `impaired` | `down`) and Blast radius.

For concurrent-modification scenarios: invoke RULE-CR-DCV inline.

```
GATE 2 CLOSE
Exit postconditions:
  [ ] Every Include scenario has all four fields with non-trivial content
  [ ] Every scenario has both severity and blast radius annotation
  [ ] Every recovery path has at least two actor-labeled steps
  [ ] All RULE-CR-DCV invocations recorded inline with DCV-NN pending
  [ ] Coverage Accountability Roster per-class counts verified against committed minimums
Gate 2 STATUS: CLOSED / OPEN
Reason if OPEN: [scenario ID with missing field, or coverage minimum unmet]
```

---

### GATE 3: Gap Identification

```
GATE 3 OPEN
Preconditions:
  [x] Gate 2 STATUS: CLOSED
Entry confirmed: [yes / no]
```

**OEG — Offline Experience Gaps**
Identify each gap: OEG-NN, description, actionable recommendation.
No gaps: `OEG-NIL-1: [scope rationale — why this gap type does not arise here]`

**DCV — Data Consistency Violations**
Identify each violation: DCV-NN, data type, failure mode.
Assign DCV-NN to all RULE-CR-DCV entries pending from Gate 2.
No violations: `DCV-NIL-1: [scope rationale]`

**MRF — Missing Recovery Flows**
Identify each missing flow: MRF-NN, scenario ref, absent mechanism.
No missing flows: `MRF-NIL-1: [scope rationale]`

**Conflict Resolution Analysis**
For each eventual-consistency scenario: name strategy, verdict (adequate / inadequate /
undefined). Inadequate or undefined → invoke RULE-CR-DCV → emit DCV-CR-NN with source
linkage. All adequate → CONFLICT RESOLUTION CLOSED.

```
GATE 3 CLOSE
Exit postconditions:
  [ ] All three gap sections present (OEG, DCV, MRF)
  [ ] Every section has at least one named finding or a typed nil with scope rationale
  [ ] Every typed nil uses a unique identifier (OEG-NIL-N, DCV-NIL-N, MRF-NIL-N)
  [ ] All RULE-CR-DCV invocations from Gate 2 have assigned DCV-NN entries
  [ ] Conflict resolution analysis present for every eventual-consistency scenario
  [ ] Conflict Resolution CLOSED or DCV-CR-NN entries generated for inadequate verdicts
Gate 3 STATUS: CLOSED / OPEN
Reason if OPEN: [gap category missing, nil rationale absent, or CR verdict unresolved]
```

---

### GATE 4: Amendment Pass

```
GATE 4 OPEN
Preconditions:
  [x] Gate 3 STATUS: CLOSED
Entry confirmed: [yes / no]
```

Review all prior gate outputs. Issue amendments for:
- Vague recovery paths → add actor-labeled steps.
- Typed nil now superseded by a Gate 3 finding → invoke RULE-NIL-SUPERSEDE.
- Downstream CR finding requiring DCV addition → reopen Gate 3 under `GATE 3: AMENDED`.

For each amendment: entry ID, original (brief), amended, rule invoked (if any).
For each gate re-open: sub-gate label (e.g., `GATE 3: AMENDED`), triggering finding ID,
re-close confirmation.

No amendments needed: "Gate 4: no amendments in this run."
No gate re-opens: "No gate re-opens triggered."

```
GATE 4 CLOSE
Exit postconditions:
  [ ] All recovery paths have actor-labeled steps
  [ ] Every superseded nil carries SUPERSEDED annotation with finding ID
  [ ] Every late DCV finding is in Gate 3: AMENDED with re-close confirmation
  [ ] No RULE-NIL-SUPERSEDE invocation is unrecorded
Gate 4 STATUS: CLOSED / OPEN
Reason if OPEN: [outstanding amendment or unresolved gate re-open]
```

---

### GATE 5: Commerce Domain Validation

```
GATE 5 OPEN
Preconditions:
  [x] Gate 4 STATUS: CLOSED
Entry confirmed: [yes / no]
```

Review all Include scenarios from Gates 1–4. For each: confirm commerce operation named.
If not: invoke RULE-COMMERCE-ANCHOR; record amendment.
Identify any commerce-domain-specific findings not surfaced by Gates 1–4.

COMMERCE VALIDATION COMPLETE
Scenarios reviewed: [N] | RULE-COMMERCE-ANCHOR invocations: [N or "none"]
Additional findings: [IDs or "none"]

```
GATE 5 CLOSE
Exit postconditions:
  [ ] Every Include scenario anchored to a named commerce operation
  [ ] RULE-COMMERCE-ANCHOR invocations recorded with scenario ID and amended operation
  [ ] Any additional CV-DCV-NN / CV-OEG-NN findings assigned and recorded
Gate 5 STATUS: CLOSED / OPEN
Reason if OPEN: [scenario without commerce anchor, or rule not applied]
```

---

## TERMINAL: Nil Supersession Log

List every typed nil issued. State: `ACTIVE` | `SUPERSEDED`.
If SUPERSEDED: cite finding ID and gate where supersession occurred.
No supersessions: "No supersessions in this run."

---

## TERMINAL: Scope Verification

For each declared operation: covered (yes/no) → gap finding if uncovered.

| Declared Operation | Covered | Gap Finding |
|---|---|---|
| [operation] | Yes / No | SV-GAP-NN / — |

SCOPE VERIFICATION COMPLETE

---

## TERMINAL: Post-Analysis Rule Registry Audit

```
POST-ANALYSIS REGISTRY AUDIT OPEN
Preconditions:
  [x] All gate CLOSE blocks confirmed
  [x] Commerce Validation COMPLETE
  [x] Nil Supersession Log written
  [x] Scope Verification COMPLETE
```

For each registered rule, report invocation count, all citations (gate + entry), and status.

**RULE-CR-DCV**
Invocations: [N]
Citations: [Gate 2, FS-NN → DCV-NN; Gate 3, CR adequacy FS-NN → DCV-CR-NN; ...]
Status: INVOKED / SCENARIO-ABSENT / RULE-BYPASSED

**RULE-BARRED-CG**
Invocations: [N]
Citations: [Gate 1, FS-NN → CG-NN; ...]
Status: INVOKED / SCENARIO-ABSENT / RULE-BYPASSED

**RULE-NIL-SUPERSEDE**
Invocations: [N]
Citations: [Gate 4, AMD-NN, NIL-ID: SUPERSEDED by F-NN; ...]
Status: INVOKED / SCENARIO-ABSENT / RULE-BYPASSED

**RULE-COMMERCE-ANCHOR**
Invocations: [N]
Citations: [Gate 5, FS-NN → [amended operation]; ...]
Status: INVOKED / SCENARIO-ABSENT / RULE-BYPASSED

RULE-BYPASSED handling: if any rule has RULE-BYPASSED status, reopen the affected gate,
apply the rule, re-close, and update this audit block before marking it COMPLETE.

```
POST-ANALYSIS REGISTRY AUDIT CLOSE
Exit postconditions:
  [ ] Every registered rule has an invocation status assigned
  [ ] Every INVOKED rule has at least one cited invocation (gate + entry)
  [ ] No RULE-BYPASSED findings remain unresolved
  [ ] SCENARIO-ABSENT rules confirm condition never arose (not just "rule not needed")
POST-ANALYSIS REGISTRY AUDIT STATUS: COMPLETE
```

---

---

## V-04

**Variation axes**: Phrasing register (conversational / imperative) + Inertia framing
(each gate names what a team without this analysis would typically miss).

**Hypothesis**: Formal gate vocabulary creates a perception of bureaucratic overhead that
causes analysts to rush through the protocol. Conversational register with short imperative
sentences reduces friction and makes each step feel like a decision rather than a form.
Inertia framing ("without this gate, a team typically...") makes the value of each step
visible, increasing motivation to execute rigorously and helping practitioners explain the
tool's value to skeptical stakeholders.

---

You are running the **flow-resilience** skill for a software feature.

Forget the formal tone for a moment. Here is what you are actually doing:

You are stress-testing a feature against three ways systems break — going offline, partial
failure, and data falling out of sync — before someone ships it and discovers these gaps in
production. For each way it can break, you need to answer four questions: what state is the
system in, what can the user still do, what data is at risk, and how does the system recover.
Then you identify the gaps — offline experience gaps, data consistency violations, missing
recovery flows — and you make sure nothing was missed.

Do this in five steps. In each step, before you start: check the entry condition. After you
finish: confirm the exit condition. Don't skip steps.

---

### Rule Registry

Declare your rules before you start. You will cite these by ID throughout — don't restate
the logic inline.

**RULE-CR-DCV**: When you see a scenario where two actors can write to the same data
concurrently without a coordination mechanism, that's a data consistency violation.
Emit DCV-NN in Step 3.

**RULE-BARRED-CG**: When you can't confirm a scenario's confidence basis from available
context, mark it BARRED and write a Coverage Gap (CG-NN) entry so it's not silently dropped.

**RULE-NIL-SUPERSEDE**: When you write a "no gaps found" nil identifier and later find
a real gap in the same category, go back and mark the nil SUPERSEDED, citing the new
finding. Don't let a nil and a real gap coexist.

**RULE-COMMERCE-ANCHOR**: When a scenario doesn't name a real commerce operation
(checkout, inventory reservation, payment, order fulfillment, cart, loyalty), Step 5 must
amend it to name one. Don't leave generic operations in the output.

---

### Before You Start: Scope and Coverage Commitment

Name the commerce operations you are going to analyze. At least four.

Without this step, a team typically ships with checkout analyzed but inventory reservation
untested, discovering the gap when a flash sale causes oversell under partition.

Operations in scope: [list — minimum four]
Operations excluded (with reason): [list or "none"]

SCOPE DECLARATION COMPLETE

Then commit to minimum scenario counts per failure class. At least two per class.

| Class | Min |
|---|---|
| Network partition / offline | 2 |
| Partial service failure | 2 |
| Eventual consistency | 2 |

If you can't fill a class, explain why using a specific architecture reason — not "the
topic doesn't mention it." State the DS primitive that forecloses the class.

---

### Step 1: Triage Your Scenarios

Without this step, teams typically include one vague "network failure" scenario and miss
three distinct failure classes — collapsing offline, partial failure, and eventual
consistency lag into a single "network issue" that generates one recommendation instead of
three distinct recovery designs.

Entry check: Is SCOPE DECLARATION COMPLETE? Yes → proceed. No → write it first.

For each scenario candidate:
- Give it an ID (FS-NN)
- Pick its class: Network partition/offline | Partial service failure | Eventual consistency
- State your confidence basis
- Assign a disposition: Include | BARRED | Argued-Impossible

BARRED entry: invoke RULE-BARRED-CG; write CG-NN.
Argued-Impossible entry: name the DS primitive.

Check BARRED entries: can any confidence basis be resolved? If yes: record resolution
under **GATE 1b: RESOLVED** (entry ID, satisfied basis, new disposition). If no: leave
BARRED; CG entry stands. No BARRED entries: state that.

Exit check: Every candidate has one named disposition. Every BARRED has a CG entry.
No entry uses free-text confidence labels (not "probably fine," "unclear" — those aren't
dispositions).

**Step 1: DONE / BLOCKED**
If BLOCKED: [what's still unresolved]

---

### Step 2: Work Through the Four Fields

Without this step, teams describe failure scenarios as "the checkout breaks" with no
state, no user capability, no data risk named, and no recovery path — which produces
a ticket saying "fix checkout" with no actionable detail.

Entry check: Step 1 DONE? Yes → proceed.

For each scenario in Include, fill in all four fields. None of them can be a placeholder:

**State**: What exactly is the system doing when this failure occurs? Name the state.
**Capability**: What can the user still do? Name specific actions.
**Data at risk**: What data might be lost, stale, or split? Name it.
**Recovery path**: Walk through how the system gets back to healthy. For each step,
name who does it: `client` | `server` | `operator` | `user`. At least two labeled steps.

Add severity (degraded / impaired / down) and blast radius (who is affected, how many).

When you see concurrent writes: invoke RULE-CR-DCV and note it inline.

Exit check: Every Include scenario has all four fields, severity, blast radius, and at
least two actor-labeled recovery steps. No "N/A," no single-word fields.

**Step 2: DONE / BLOCKED**
If BLOCKED: [scenario ID and missing field]

---

### Step 3: Identify the Gaps

Without this step, teams generate scenario tables and then never extract the findings.
The gaps stay buried in individual scenario rows and never become actionable issues.

Entry check: Step 2 DONE? Yes → proceed.

Find your gaps in three categories:

**Offline Experience Gaps (OEG-NN)**: What can't the user do offline that the system
doesn't handle or surface? If none: write `OEG-NIL-1:` followed by a rationale
explaining why offline experience gaps don't arise here. "None found" alone is not enough.

**Data Consistency Violations (DCV-NN)**: What data can go stale, inconsistent, or lost?
Include anything flagged RULE-CR-DCV from Step 2. If none: write `DCV-NIL-1:` with rationale.

**Missing Recovery Flows (MRF-NN)**: What recovery scenarios have no defined path?
If none: write `MRF-NIL-1:` with rationale.

For each eventual-consistency scenario from Step 2: name the conflict resolution strategy
and judge its adequacy. Inadequate or undefined strategy: invoke RULE-CR-DCV → emit
DCV-CR-NN linking back to the strategy assessment.

Exit check: All three categories present. Every category has at least one finding or
a typed nil (OEG-NIL-N, DCV-NIL-N, MRF-NIL-N) with scope rationale.

**Step 3: DONE / BLOCKED**
If BLOCKED: [missing category or nil without rationale]

---

### Step 4: Clean Up

Without this step, recovery paths stay vague, nil identifiers coexist with real findings
of the same type with no resolution, and late findings from Step 3 never propagate back
to Step 2 scenarios.

Entry check: Step 3 DONE? Yes → proceed.

Do three things:
1. Any recovery path still vague? Add actor-labeled steps.
2. Any Step 3 finding in a category that had a nil? Invoke RULE-NIL-SUPERSEDE —
   annotate the nil as SUPERSEDED citing the new finding ID.
3. Any Step 3 finding that requires amending an already-closed section? Reopen it
   under a labeled sub-gate (`GATE 3: AMENDED`) and re-close.

Record every amendment: entry ID, what changed, why.
No amendments needed: state that. No gate re-opens triggered: state that.

Exit check: No nil coexists with a real finding of the same type without a SUPERSEDED
annotation. Every re-opened section has a labeled re-close record.

**Step 4: DONE / BLOCKED**
If BLOCKED: [outstanding amendment or unresolved supersession]

---

### Step 5: Commerce Domain Check

Without this step, scenarios get labeled with generic operations like "data write" that
make it impossible to prioritize — a DCV in "data write" gets no stakeholder attention;
a DCV in "inventory reservation during checkout" triggers a P0 review.

Entry check: Step 4 DONE? Yes → proceed.

Go through every Include scenario. Does it name a real commerce operation? If not: invoke
RULE-COMMERCE-ANCHOR and amend it. Record what you changed.

Check for commerce-domain gaps the previous steps may have missed:
- Inventory oversell under partition
- Payment idempotency window expiry
- Loyalty point double-redemption
- Order state divergence under partial fulfillment failure

Issue any new findings as CV-DCV-NN, CV-OEG-NN, or CV-MRF-NN.

COMMERCE VALIDATION COMPLETE
Scenarios checked: [N] | RULE-COMMERCE-ANCHOR invocations: [N or "none"]
New findings: [list or "none"]

---

## Terminal: Nil Supersession Log

List every typed nil. State: ACTIVE or SUPERSEDED. If SUPERSEDED: cite the finding and step.
No supersessions: "No supersessions in this run."

## Terminal: Scope Verification

For each declared operation: was it covered? If not: name the gap.

| Operation | Covered | Gap |
|---|---|---|
| [operation] | Yes / No | SV-GAP-NN / — |

SCOPE VERIFICATION COMPLETE

---

## Terminal: Post-Analysis Rule Registry Audit

Now check that every rule you declared actually ran when it should have.

Without this step, a rule registry is a list of intentions. Teams can declare five rules,
satisfy none of them, and claim compliance because the registry exists. The audit makes
the difference between "rules declared" and "rules executed."

For each rule:

**RULE-CR-DCV**
How many times it fired: [N]
Where it fired: [Step/Gate N, entry ID → DCV-NN; ...]
Status: INVOKED | SCENARIO-ABSENT | RULE-BYPASSED

**RULE-BARRED-CG**
How many times it fired: [N]
Where it fired: [Step 1, FS-NN → CG-NN; ...]
Status: INVOKED | SCENARIO-ABSENT | RULE-BYPASSED

**RULE-NIL-SUPERSEDE**
How many times it fired: [N]
Where it fired: [Step 4, AMD-NN, NIL-ID: SUPERSEDED by F-NN; ...]
Status: INVOKED | SCENARIO-ABSENT | RULE-BYPASSED

**RULE-COMMERCE-ANCHOR**
How many times it fired: [N]
Where it fired: [Step 5, FS-NN → [operation]; ...]
Status: INVOKED | SCENARIO-ABSENT | RULE-BYPASSED

SCENARIO-ABSENT means: the condition that triggers this rule never came up. That's OK.
RULE-BYPASSED means: the condition came up but you didn't apply the rule. Not OK.
If you have a RULE-BYPASSED finding: go back, apply the rule, come back, update this block.

POST-ANALYSIS REGISTRY AUDIT COMPLETE

---

---

## V-05

**Variation axes**: Full integration — role sequence (DS Expert / Commerce Validator) +
lifecycle emphasis (GATE-OPEN / GATE-CLOSE blocks) + table-dominant output for Gate 2
and registry audit + conversational inertia framing at Gap Identification + all C-01–C-28.

**Hypothesis**: The full integration achieves maximum criterion coverage while the role
separation enforces DS accuracy independent of commerce grounding. GATE-OPEN / GATE-CLOSE
blocks make closure independently auditable. Table output at Gate 2 surfaces C-02 field
completeness visually. Inertia framing at Gate 3 makes gap findings actionable rather than
taxonomic. The Post-Analysis Registry Audit (C-28) closes the execution loop on all four
rules, making the registry verifiable without re-reading the full analysis.

---

You are running the **flow-resilience** skill for a software feature in active development.

This analysis runs in two sequential acts: **Act 1 — Distributed Systems Expert** (Gates
1–4) and **Act 2 — Commerce Domain Validator** (Gate 5). Do not blend roles. Act 2 does
not begin until Act 1 closes all gates.

Output format: Gates 1b, 2, and the registry audit use tables. Gates 1, 3, and 4 use
structured prose with typed identifiers. All gates use GATE-OPEN and GATE-CLOSE blocks.

---

### RULE REGISTRY

Declared before any analysis. All rules cited by ID in gate sections — logic not restated
inline.

**RULE-CR-DCV**
Trigger: scenario has concurrent state modification by multiple actors without a
coordination mechanism.
Action: emit named DCV-NN finding in Gate 3; link back to triggering scenario ID.

**RULE-BARRED-CG**
Trigger: discovery entry confidence basis cannot be resolved from available context.
Action: mark entry BARRED; emit CG-NN in coverage log naming the unresolvable basis.

**RULE-NIL-SUPERSEDE**
Trigger: downstream finding introduces a gap in a category that currently holds a typed
nil identifier.
Action: annotate the nil `[NIL-ID]: SUPERSEDED by [finding ID]`; record in nil supersession
log with gate and entry citation.

**RULE-COMMERCE-ANCHOR**
Trigger: Include scenario names only a generic operation (no named commerce flow).
Action: amend scenario to name a specific commerce operation; record under Act 2
COMMERCE VALIDATION AMENDMENTS.

---

### Pre-Analysis: Commerce Operation Scope Declaration

Act 1 (DS Expert) declares before Gate 1. Minimum four operations.

Operations in scope: [list]
Operations explicitly excluded (with reason): [list or "none"]

SCOPE DECLARATION COMPLETE

### Pre-Analysis: Coverage Accountability Roster

| Degradation Class | Committed Minimum | DS Primitive for Impossibility (if class unfillable) |
|---|---|---|
| Network partition / offline | 2 | |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

Impossibility arguments must cite a specific architecture constraint.
DS Primitive cited: [required field]
VALID example: architecture constraint that forecloses the class.
INVALID example: topic-scope argument ("the topic doesn't mention X").

---

### GATE 1: Discovery and Triage

```
GATE 1 OPEN
Preconditions:
  [ ] SCOPE DECLARATION COMPLETE block present
  [ ] Coverage Accountability Roster committed
  [ ] All preconditions met before proceeding
```

For each failure scenario candidate:
- ID (FS-NN), failure class, confidence basis, disposition:
  `Include` | `BARRED` | `Argued-Impossible`
- BARRED: invoke RULE-BARRED-CG; emit CG-NN.
- Argued-Impossible: cite DS Primitive.

Disposition table: ID | Failure Class | Confidence Basis | Disposition | Notes

**Gate 1b — BARRED Resolution Sub-Gate**

| BARRED Entry | Confidence Basis | Resolved? | Resolution Mechanism | New Disposition |
|---|---|---|---|---|
| FS-NN | | Yes / No | | Include / Remains BARRED |

GATE 1b: RESOLVED entries (if any): [entry ID, satisfied basis, Include, Gate 1b closed]
No BARRED-to-Include upgrades: state if true.

```
GATE 1 CLOSE
Exit postconditions:
  [ ] Every candidate has exactly one named disposition
  [ ] Every BARRED entry has a CG-NN entry
  [ ] Every Argued-Impossible entry cites a DS Primitive by name
  [ ] No free-text confidence label used as a disposition substitute
  [ ] Coverage Accountability Roster updated with actual counts (or impossibility
      argument filling the DS Primitive column for any unfilled class)
Gate 1 STATUS: CLOSED / OPEN
Reason if OPEN: [specific blocking condition]
```

---

### GATE 2: Four-Field Scenario Analysis

```
GATE 2 OPEN
Precondition: Gate 1 STATUS: CLOSED
```

| ID | Commerce Operation | State | Capability | Data at Risk | Recovery Path (actor-labeled) | Severity | Blast Radius | RULE-CR-DCV? |
|---|---|---|---|---|---|---|---|---|
| FS-01 | | | | | 1. [actor]: [step]; 2. [actor]: [step] | degraded/impaired/down | | Yes (→DCV-NN) / No |

Column constraints:
- Commerce Operation: named commerce flow (may be "TBD — awaiting Act 2 review" only if
  the scenario clearly maps to one but the specific name is uncertain).
- State: specific, not "degraded."
- Capability: named actions.
- Data at risk: named data type and failure mode.
- Recovery path: minimum two actor-labeled steps.
- Severity: exactly one of three values.
- Blast radius: fraction or segment.
- RULE-CR-DCV: if Yes, record pending DCV-NN to be assigned in Gate 3.

```
GATE 2 CLOSE
Exit postconditions:
  [ ] All four required fields present and non-trivial in every row
  [ ] All scenarios have both severity and blast radius
  [ ] All recovery paths have at least two actor-labeled steps
  [ ] All RULE-CR-DCV applications noted with pending DCV-NN
  [ ] Coverage Accountability Roster final counts confirmed
Gate 2 STATUS: CLOSED / OPEN
Reason if OPEN: [row ID and missing field or annotation]
```

---

### GATE 3: Gap Identification

```
GATE 3 OPEN
Precondition: Gate 2 STATUS: CLOSED
```

Without this gate, scenario tables sit in documents and never produce actionable findings.
Teams read the scenarios, say "yeah that's bad," and file no tickets. This gate extracts
the findings from the scenarios and makes them independently actionable.

**OEG — Offline Experience Gaps**
For each gap: OEG-NN | description | why it matters | actionable recommendation.
No gaps: `OEG-NIL-1: [scope rationale — why offline experience gaps don't arise here]`

**DCV — Data Consistency Violations**
For each violation: DCV-NN | data type | failure mode | commerce operation affected.
Assign DCV-NN to RULE-CR-DCV entries pending from Gate 2.
No violations: `DCV-NIL-1: [scope rationale]`

**MRF — Missing Recovery Flows**
For each missing flow: MRF-NN | scenario ref | absent mechanism | impact if never built.
No missing flows: `MRF-NIL-1: [scope rationale]`

**Conflict Resolution Analysis**
For each eventual-consistency scenario from Gate 2:
- Strategy named: `last-write-wins` | `merge` | `manual-reconcile` | `reject-stale` |
  `undefined`
- Adequacy verdict: `adequate` | `inadequate` | `undefined`
- Inadequate or undefined: invoke RULE-CR-DCV → emit `DCV-CR-NN` with source linkage.
- All adequate: CONFLICT RESOLUTION CLOSED.

```
GATE 3 CLOSE
Exit postconditions:
  [ ] All three gap sections present (OEG, DCV, MRF)
  [ ] Every section has a named finding or a typed nil (OEG-NIL-N, DCV-NIL-N, MRF-NIL-N)
  [ ] Every typed nil has a scope rationale (not bare "none found")
  [ ] All RULE-CR-DCV entries from Gate 2 assigned DCV-NN
  [ ] Conflict resolution analyzed for every eventual-consistency scenario
  [ ] CONFLICT RESOLUTION CLOSED or DCV-CR-NN entries present
Gate 3 STATUS: CLOSED / OPEN
Reason if OPEN: [missing section, nil without rationale, or CR verdict pending]
```

---

### GATE 4: Amendment Pass

```
GATE 4 OPEN
Precondition: Gate 3 STATUS: CLOSED
```

Review all prior gates. Issue amendments:
- Vague recovery paths: add actor-labeled steps; record entry ID, original, amended, reason.
- Gate 3 finding in category with typed nil: invoke RULE-NIL-SUPERSEDE; annotate nil
  SUPERSEDED citing new finding ID.
- Downstream finding requiring DCV addition to closed Gate 3: reopen under
  `GATE 3: AMENDED`; apply DCV-CR-NN; re-close with sub-gate label.

No amendments: "Gate 4: no amendments in this run."
No gate re-opens: "No gate re-opens triggered."

```
GATE 4 CLOSE
Exit postconditions:
  [ ] All recovery paths have actor-labeled steps (minimum two per scenario)
  [ ] Every superseded nil has SUPERSEDED annotation with superseding finding ID
  [ ] Every gate re-open has a labeled sub-gate and re-close confirmation
  [ ] No nil and gap finding of the same type coexist without SUPERSEDED annotation
Gate 4 STATUS: CLOSED / OPEN
Reason if OPEN: [outstanding amendment or unresolved supersession]
```

---

### GATE 5: Commerce Domain Validation (Act 2 — Commerce Domain Validator)

```
GATE 5 OPEN
Precondition: Gate 4 STATUS: CLOSED
Role: Commerce Domain Validator (distinct from Act 1)
```

Review all Include scenarios from Gates 1–4. For each:
1. Is it anchored to a named commerce operation?
2. If not (or "TBD"): invoke RULE-COMMERCE-ANCHOR; amend; record under COMMERCE
   VALIDATION AMENDMENTS.

Review OEG, DCV, MRF findings for commerce-domain-specific gaps not surfaced in Act 1:
- Inventory oversell under partition
- Payment idempotency window expiry under partial service failure
- Loyalty point double-redemption in eventual consistency lag window
- Order state divergence under partial fulfillment failure

Issue additional findings as CV-DCV-NN, CV-OEG-NN, CV-MRF-NN.

COMMERCE VALIDATION COMPLETE
Scenarios reviewed: [N]
RULE-COMMERCE-ANCHOR invocations: [N or "none"]
Additional commerce-domain findings: [IDs or "none"]

```
GATE 5 CLOSE
Exit postconditions:
  [ ] Every Include scenario has a named commerce operation
  [ ] All RULE-COMMERCE-ANCHOR invocations recorded with scenario ID and amended operation
  [ ] Any CV-DCV-NN / CV-OEG-NN / CV-MRF-NN findings assigned and described
Gate 5 STATUS: CLOSED / OPEN
Reason if OPEN: [scenario without commerce anchor or rule not applied]
```

---

## TERMINAL: Nil Supersession Log

| Nil ID | Gap Type | State | Superseded By | Gate |
|---|---|---|---|---|
| OEG-NIL-1 | OEG | ACTIVE / SUPERSEDED | OEG-F-NN / — | Gate 4 / — |

No supersessions: "No supersessions in this run."

---

## TERMINAL: Scope Verification

| Declared Operation | Scenario Coverage | Gap Finding |
|---|---|---|
| [operation] | Yes / No | SV-GAP-NN / — |

Any declared operation without coverage and without an impossibility argument is an
unclosed scope gap.

SCOPE VERIFICATION COMPLETE

---

## TERMINAL: Post-Analysis Rule Registry Audit

```
POST-ANALYSIS REGISTRY AUDIT OPEN
Preconditions:
  [ ] All Gate CLOSE blocks confirmed (Gates 1–5)
  [ ] Nil Supersession Log written
  [ ] Scope Verification COMPLETE
```

| Rule ID | Invocation Count | Citations (gate, entry → target) | Status |
|---|---|---|---|
| RULE-CR-DCV | [N] | Gate 2 FS-NN→DCV-NN pending; Gate 3 CR FS-NN→DCV-CR-NN; ... | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED |
| RULE-BARRED-CG | [N] | Gate 1 FS-NN→CG-NN; ... | |
| RULE-NIL-SUPERSEDE | [N] | Gate 4 AMD-NN, NIL-ID: SUPERSEDED by F-NN; ... | |
| RULE-COMMERCE-ANCHOR | [N] | Gate 5 FS-NN→[operation]; ... | |

Status definitions:
- **INVOKED**: rule fired; each invocation cited by gate and entry. No uncited invocation.
- **SCENARIO-ABSENT**: triggering condition never arose. State which condition was absent.
- **RULE-BYPASSED**: condition arose but rule was not applied. Audit failure.

RULE-BYPASSED handling: identify the entry, reopen the affected gate, apply the rule,
re-close the gate, update this table. Block cannot be COMPLETE while any RULE-BYPASSED
row is unresolved.

Act 1 sign-off (DS Expert): all RULE-CR-DCV, RULE-BARRED-CG, RULE-NIL-SUPERSEDE
accounted for.
Act 2 sign-off (Commerce Validator): RULE-COMMERCE-ANCHOR status confirmed.

```
POST-ANALYSIS REGISTRY AUDIT CLOSE
Exit postconditions:
  [ ] Every registered rule has a row with invocation count, citations, and status
  [ ] Every INVOKED rule has at least one cited invocation (gate + entry)
  [ ] No RULE-BYPASSED row left unresolved
  [ ] SCENARIO-ABSENT rules confirm condition absent (not just "rule not needed")
POST-ANALYSIS REGISTRY AUDIT STATUS: COMPLETE
```
