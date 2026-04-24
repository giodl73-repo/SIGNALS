# Flow-Resilience Skill — Round 9 Variations (Rubric v9)

**Skill**: flow-resilience — Simulate degraded conditions: offline, partial failure, eventual consistency.
**Rubric**: v9 (C-01 through C-30, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Round 9 Context

**New criteria entering R9**: C-29 -- Rule-Bypass-Triggered Gate Reopening; C-30 -- Multi-Act Completion Sign-Off.

**R8 diagnosis**:
- R8 V-03 introduced GATE-OPEN / GATE-CLOSE boundary blocks (lifecycle emphasis axis), making
  gate closure independently auditable by structural scan.
- R8 V-05 achieved the highest integration ceiling entering R9: all of C-25 through C-28 plus
  full GATE-OPEN/GATE-CLOSE formalization. R9 variations must extend that ceiling by targeting
  C-29 and C-30 while keeping all accumulated criteria intact.
- C-28 (post-analysis rule registry audit) established RULE-BYPASSED as an audit status. C-29
  makes RULE-BYPASSED a *structural trigger*: it must reopen the affected gate, apply the rule,
  close the gate under an amendment sub-gate, and update the audit entry to INVOKED before
  COMPLETE may be declared. C-28 said what to report; C-29 says what that report forces.
- C-30 makes per-act completion independently verifiable: a single terminal COMPLETE in a
  multi-act analysis cannot confirm Act 1's gates are closed. Each act must emit its own
  sign-off block. Single-act analyses score C-30 as N/A (PARTIAL, 1 point).

**Variation axes selected**:
- V-01: Single axis -- Role sequence (DS Expert owns bypass-gate-reopening; Commerce Validator
  co-signs per-act sign-off for Act 2 scope only)
- V-02: Single axis -- Output format (table-dominant; BYPASS-TRIGGER column in registry
  audit makes C-29 checkable by column scan)
- V-03: Single axis -- Lifecycle emphasis (explicit ACT-CLOSE blocks with three-item per-act
  sign-off checklist enforce C-30 structurally)
- V-04: Combination -- Phrasing register (conversational/imperative) + Inertia framing
  (status-quo competitor prominently featured in gap section and inertia verdict)
- V-05: Full integration -- Role sequence + lifecycle emphasis + table registry with
  bypass-trigger column + conversational enforcement + inertia competitor + all C-01--C-30

---

## V-01

**Variation axis**: Role sequence -- DS Expert owns the gate protocol and bypass-gate-reopening
authority (Acts 1--4); Commerce Domain Validator owns the domain pass and co-signs the Act 2
per-act sign-off. Each act closes with a named sign-off block. DS Expert re-opens any bypassed
gate; Commerce Validator cannot proceed to COMPLETE if a RULE-BYPASSED entry is unresolved in
Act 2.

**Hypothesis**: RULE-BYPASSED is a structural failure in the DS Expert's gate ownership, not a
Commerce domain problem. Assigning bypass-gate-reopening authority explicitly to DS Expert
creates a single accountable owner per bypass event, preventing ambiguity about who is
responsible for re-opening and re-closing the affected gate. Commerce Validator's per-act
sign-off is scoped to Act 2 only, making the dual sign-off verifiable at domain-split
granularity.

---

You are running the **flow-resilience** skill for `{topic}`.

This analysis runs in two sequential acts with distinct roles and independent closure
requirements. Do not blend the acts.

---

### RULE REGISTRY

All conditional linkage rules declared here before any analysis begins. Gates cite rules by
ID -- they do not restate logic inline.

**RULE-CR-DCV**: If a scenario involves concurrent state modification by multiple actors
without a coordination mechanism, classify the conflict as a named Data Consistency Violation
and assign a DCV-NN identifier in the Gap Identification gate.

**RULE-BARRED-CG**: If a discovery entry's confidence basis cannot be resolved from available
context, mark the entry BARRED and emit a named Coverage Gap (CG-NN) entry. The CG entry
persists regardless of whether the BARRED entry is later resolved.

**RULE-NIL-SUPERSEDE**: If a downstream gate or amendment introduces a gap finding in a
category that previously held a typed nil identifier, annotate the nil SUPERSEDED citing
the new finding ID. Format: `OEG-NIL-1: SUPERSEDED by OEG-F-02`.

**RULE-COMMERCE-ANCHOR**: If a scenario in the Include column references only a generic
operation with no named commerce flow, Act 2 Commerce Validator must amend it and record
the amendment under COMMERCE VALIDATION AMENDMENTS.

---

### Bypass Gate-Reopening Protocol (DS Expert Authority)

**Authority**: DS Expert owns this protocol. Commerce Validator cannot invoke bypass
gate-reopening for Act 1 gates.

When the Post-Analysis Rule Registry Audit records a rule as RULE-BYPASSED:

1. DS Expert reopens the affected gate: emit a named sub-gate block
   `GATE N-bypass: REOPENED` stating the bypassed rule ID and the entry where the
   bypass occurred.
2. DS Expert applies the rule: produce the finding, amendment, or action the rule
   requires (DCV-NN, CG-NN, SUPERSEDED annotation, or commerce anchor).
3. DS Expert closes the sub-gate: `GATE N-bypass: AMENDED -- CLOSED` confirming the
   rule is now applied.
4. DS Expert updates the registry audit entry from RULE-BYPASSED to INVOKED, citing
   the sub-gate reference and the generated output.

**COMPLETE may not be declared** while any RULE-BYPASSED entry remains unresolved in
the audit table.

---

## ACT 1 -- DISTRIBUTED SYSTEMS EXPERT

You are a distributed systems expert. Your task: triage failure scenarios with technical
rigor, run Gates 1--4, manage the nil lifecycle, invoke registry rules at every trigger
point, apply the bypass-gate-reopening protocol if any RULE-BYPASSED entries are found
in the registry audit, and close Act 1 with a per-act sign-off before handing off.

### Pre-Analysis: Commerce Operation Scope Declaration

Declare before Gate 1. Minimum four operations from: checkout, inventory reservation,
payment processing, order fulfillment, cart state, loyalty redemption, return/refund.

```
SCOPE DECLARATION
Operations in scope: [list each]
Operations explicitly excluded (with reason): [list or "none"]
```

SCOPE DECLARATION COMPLETE

### Pre-Analysis: Coverage Accountability Roster

Commit to minimum scenario slots per degradation class before Gate 1. Minimum two per class.

| Degradation Class | Committed Minimum | Actual (fill after Gate 2) |
|---|---|---|
| Network partition / offline | 2 | |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

Impossibility argument (if a class slot cannot be filled): cite a specific DS primitive
(CAP theorem guarantee, deployment topology constraint, or synchronous consistency guarantee).
VALID: "Under CP topology, network partitions prevent divergent writes."
INVALID: "The topic doesn't mention caching."

---

### GATE 1: Discovery and Triage

Entry condition: SCOPE DECLARATION COMPLETE block present.

For each failure scenario candidate:
- Assign ID (FS-NN)
- Failure class: `Network partition / offline` | `Partial service failure` |
  `Eventual consistency`
- Confidence basis
- Disposition: `Include` | `BARRED` | `Argued-Impossible`

BARRED: cite RULE-BARRED-CG; emit CG-NN.
Argued-Impossible: cite DS Primitive by name.

Disposition table: ID | Failure Class | Confidence Basis | Disposition | Notes

**Gate 1b -- BARRED Resolution Sub-Gate**

For each BARRED entry: attempt resolution.
- Resolved: record `GATE 1b: RESOLVED` -- entry ID, mechanism, new disposition (Include).
- Not resolved: entry remains BARRED; CG entry stands.
- No BARRED entries: "Gate 1b: no BARRED entries present."

GATE 1 STATUS: [OPEN | CLOSED]
Reason if OPEN: [specific blocking entry]

---

### GATE 2: Four-Field Scenario Analysis

Entry condition: GATE 1 STATUS: CLOSED

For each Include scenario, produce all four required fields:

1. **State** -- Specific system state when failure occurs. Not "degraded."
2. **Capability** -- Named actions the user can still take. Not "partial functionality."
3. **Data at risk** -- Named data type and the consistency failure mode.
4. **Recovery path** -- Concrete steps; each step names the actor (`client` | `server` |
   `operator` | `user`). Minimum two actor-labeled steps.

Annotate: Severity (`degraded` | `impaired` | `down`) and Blast radius.

Concurrent-modification scenarios: invoke RULE-CR-DCV inline.
Record: "RULE-CR-DCV invoked -- Gate 2, FS-NN -> DCV-NN pending Gate 3."

GATE 2 STATUS: [OPEN | CLOSED]
Reason if OPEN: [scenario ID with missing field]

---

### GATE 3: Gap Identification

Entry condition: GATE 2 STATUS: CLOSED

**OEG -- Offline Experience Gaps**
Each gap: OEG-NN, description, actionable recommendation.
No gaps: `OEG-NIL-1: [scope rationale -- explain why this gap type does not arise]`

**DCV -- Data Consistency Violations**
Each violation: DCV-NN, data type, failure mode.
Assign DCV-NN to all RULE-CR-DCV pending entries from Gate 2.
No violations: `DCV-NIL-1: [scope rationale]`

**MRF -- Missing Recovery Flows**
Each missing flow: MRF-NN, scenario ref, absent mechanism.
No missing flows: `MRF-NIL-1: [scope rationale]`

**Conflict Resolution Analysis**
For each eventual-consistency scenario: name strategy (`last-write-wins` | `merge` |
`manual-reconcile` | `reject-stale` | `undefined`), adequacy verdict.
Inadequate or undefined: invoke RULE-CR-DCV; emit DCV-CR-NN with source linkage.
All adequate: CONFLICT RESOLUTION CLOSED.

GATE 3 STATUS: [OPEN | CLOSED]
Reason if OPEN: [gap category missing or nil rationale absent]

---

### GATE 4: Amendment Pass

Entry condition: GATE 3 STATUS: CLOSED

Review all Gate 2 scenarios and Gate 3 findings:
- Recovery paths too vague: amend; record entry ID, original, amended, triggering reason.
- Typed nil now superseded: invoke RULE-NIL-SUPERSEDE; annotate nil SUPERSEDED.
- Gate 3 re-open triggered by downstream CR finding: reopen under `GATE 3: AMENDED`;
  apply amendment; re-close.

No amendments: "Gate 4: no amendments required."
No gate re-opens: "No gate re-opens triggered."

GATE 4 STATUS: [OPEN | CLOSED]
Reason if OPEN: [outstanding amendment or unresolved supersession]

---

### TERMINAL: Post-Analysis Rule Registry Audit (Act 1 scope)

Entry condition: GATE 4 STATUS: CLOSED

For each rule, report invocation count, citations, and status.

| Rule ID | Invocation Count | Citations (gate + entry) | Status |
|---|---|---|---|
| RULE-CR-DCV | | | |
| RULE-BARRED-CG | | | |
| RULE-NIL-SUPERSEDE | | | |

Status: `INVOKED` (cited) | `SCENARIO-ABSENT` (trigger never arose -- acceptable) |
`RULE-BYPASSED` (trigger arose but rule not applied -- **DS Expert must invoke bypass
gate-reopening protocol before this audit can be marked COMPLETE**).

**If any RULE-BYPASSED entry is present**:
1. Emit `GATE N-bypass: REOPENED -- [rule ID] -- [entry where bypass occurred]`
2. Apply rule; produce required output
3. Emit `GATE N-bypass: AMENDED -- CLOSED`
4. Update audit row: Status -> INVOKED; add sub-gate citation

POST-ANALYSIS REGISTRY AUDIT (ACT 1) COMPLETE: [confirm no RULE-BYPASSED entries remain]

---

### ACT 1 SIGN-OFF (C-30)

```
ACT 1 SIGN-OFF
(1) All gates within Act 1 CLOSED:
    Gate 1: [CLOSED / reason if open]
    Gate 1b: [CLOSED / N/A -- no BARRED entries]
    Gate 2: [CLOSED / reason if open]
    Gate 3: [CLOSED / reason if open]
    Gate 4: [CLOSED / reason if open]
    Any GATE N-bypass sub-gates: [CLOSED / none triggered]
(2) Act 1 scope exhausted: [yes -- all Include scenarios analyzed through Gate 4]
(3) No RULE-BYPASSED conditions remain unresolved within Act 1: [yes / exception detail]
ACT 1 STATUS: CLOSED
```

---

## ACT 2 -- COMMERCE DOMAIN VALIDATOR

Entry condition: ACT 1 STATUS: CLOSED

Review all scenarios from Gates 1--4. For each:
1. Is it anchored to a named commerce operation from the scope declaration?
2. If not: invoke RULE-COMMERCE-ANCHOR; amend; record under COMMERCE VALIDATION AMENDMENTS.

Identify additional commerce-domain findings Act 1 may not have surfaced:
inventory oversell under partition, payment idempotency window expiry, loyalty point
double-redemption, order state divergence under partial fulfillment failure.
Issue as CV-DCV-NN, CV-OEG-NN, or CV-MRF-NN.

```
COMMERCE VALIDATION COMPLETE
Scenarios reviewed: [N]
RULE-COMMERCE-ANCHOR invocations: [N or "none"]
Additional findings: [IDs or "none"]
```

### Post-Analysis Rule Registry Audit (Act 2 scope)

| Rule ID | Invocation Count | Citations | Status |
|---|---|---|---|
| RULE-COMMERCE-ANCHOR | | | |

If RULE-BYPASSED: invoke bypass gate-reopening protocol within Act 2 scope;
emit `GATE 5-bypass: REOPENED`, apply rule, emit `GATE 5-bypass: AMENDED -- CLOSED`,
update audit row.

POST-ANALYSIS REGISTRY AUDIT (ACT 2) COMPLETE: [confirm no RULE-BYPASSED entries remain]

---

### ACT 2 SIGN-OFF (C-30)

```
ACT 2 SIGN-OFF
(1) All gates within Act 2 CLOSED:
    Gate 5 (Commerce Validation): [CLOSED / reason if open]
    Any GATE 5-bypass sub-gates: [CLOSED / none triggered]
(2) Act 2 scope exhausted: [yes -- all scenarios reviewed for commerce anchoring;
    all additional CV findings issued]
(3) No RULE-BYPASSED conditions remain unresolved within Act 2: [yes / exception detail]
ACT 2 STATUS: CLOSED
```

---

### TERMINAL: Nil Supersession Log

List every typed nil issued across both acts. State: `ACTIVE` | `SUPERSEDED`.
If SUPERSEDED: cite finding ID and gate where supersession occurred.
No supersessions: "No supersessions in this run."

---

### TERMINAL: Scope Verification

| Declared Operation | Covered | Gap Finding |
|---|---|---|
| [operation] | Yes / No | SV-GAP-NN / -- |

SCOPE VERIFICATION COMPLETE

---

### COMPLETE

COMPLETE may be declared only when:
- ACT 1 SIGN-OFF: CLOSED
- ACT 2 SIGN-OFF: CLOSED
- No RULE-BYPASSED entry in either act's registry audit remains unresolved

ANALYSIS COMPLETE

---

---

## V-02

**Variation axis**: Output format -- table-dominant throughout. Every gate produces a
Markdown table as its primary artifact. The rule registry audit adds a BYPASS-TRIGGER
column: any RULE-BYPASSED status cell automatically forces a non-empty GATE-REOPEN entry
in the adjacent column, making C-29 checkable by column scan without reading prose.

**Hypothesis**: When RULE-BYPASSED appears as a status cell in a table, it can be silently
read past in prose review but not in column review -- a non-empty BYPASS-TRIGGER cell beside
every RULE-BYPASSED row makes the bypass event structurally visible. Removing the prose
narrative from gate outputs reduces the surface area where bypass conditions can be soft-
pedaled with qualifying language. Tables also make C-02's four fields enforceable as four
column headers, not four paragraph topics.

---

You are running the **flow-resilience** skill for `{topic}`.

Output format rule: every gate produces a Markdown table as its primary artifact. Prose is
permitted only for impossibility arguments in the Coverage Accountability Roster, scope
rationale in nil findings, and actor-labeled steps inside Recovery Path cells (inline, not
as separate blocks).

---

### RULE REGISTRY

| Rule ID | Trigger Condition | Action | Target Section |
|---|---|---|---|
| RULE-CR-DCV | Scenario has concurrent state modification by multiple actors without a coordination mechanism | Classify as DCV-NN finding; cite rule inline at trigger point | Gate 3 DCV section |
| RULE-BARRED-CG | Discovery entry's confidence basis cannot be resolved | Mark BARRED; emit CG-NN in coverage log | Gate 1 coverage log |
| RULE-NIL-SUPERSEDE | Downstream finding introduced in category that held a typed nil | Annotate nil SUPERSEDED citing new finding ID | Gate 4 nil audit |
| RULE-COMMERCE-ANCHOR | Include scenario references generic operation only (no named commerce flow) | Amend to name specific commerce operation; record amendment | Gate 5 commerce pass |

---

### Pre-Analysis: Commerce Operation Scope Declaration

| Operation | In Scope | Exclusion Reason |
|---|---|---|
| [operation] | Yes / No | [reason or --] |

Minimum four operations in scope. SCOPE DECLARATION COMPLETE

### Pre-Analysis: Coverage Accountability Roster

| Degradation Class | Committed Minimum | DS Primitive for Impossibility (if slot unfilable) |
|---|---|---|
| Network partition / offline | 2 | |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

DS Primitive must name a specific architecture constraint. "Topic doesn't mention X" is
invalid.

---

### GATE 1: Discovery and Triage

| ID | Failure Class | Confidence Basis | Disposition | Rule Applied | Notes |
|---|---|---|---|---|---|
| FS-01 | | | Include / BARRED / Argued-Impossible | -- | |

BARRED entries: cite RULE-BARRED-CG in Rule Applied column.
Argued-Impossible entries: name DS Primitive in Notes column.

**Gate 1b -- BARRED Resolution**

| BARRED Entry ID | Confidence Basis | Resolved? | Mechanism | New Disposition |
|---|---|---|---|---|
| FS-NN | | Yes / No | | Include / Remains BARRED |

Coverage Gap Log (permanently BARRED entries):

| CG ID | Entry ID | Unresolvable Basis | Status |
|---|---|---|---|
| CG-01 | FS-NN | | Permanently BARRED |

No BARRED entries: "Gate 1b: no BARRED entries."

GATE 1 STATUS: OPEN / CLOSED
Reason if OPEN: [entry ID and unmet condition]

---

### GATE 2: Four-Field Scenario Analysis

| ID | State | Capability | Data at Risk | Recovery Path (actor-labeled steps) | Severity | Blast Radius | Rule Applied |
|---|---|---|---|---|---|---|---|
| FS-01 | | | | 1. [actor]: [action]; 2. [actor]: [action] | degraded / impaired / down | | |

Column requirements:
- **State**: specific configuration, not "degraded."
- **Capability**: named commerce operations, not "partial functionality."
- **Data at risk**: name the data type and failure mode.
- **Recovery path**: minimum two actor-labeled steps inline.
- **Severity**: exactly `degraded` | `impaired` | `down`.
- **Blast radius**: fraction or named segment.
- **Rule Applied**: cite RULE-CR-DCV if concurrent modification present.

GATE 2 STATUS: OPEN / CLOSED
Reason if OPEN: [scenario ID and missing field]

---

### GATE 3: Gap Identification

**OEG -- Offline Experience Gaps**

| ID | Scenario Ref | Gap Description | Actionable Recommendation |
|---|---|---|---|
| OEG-01 | FS-NN | | |

No OEG findings: `OEG-NIL-1` -- [scope rationale].

**DCV -- Data Consistency Violations**

| ID | Source | Data Type | Consistency Failure Mode | Conflict Resolution | Adequacy Verdict | Rule Applied |
|---|---|---|---|---|---|---|
| DCV-01 | FS-NN | | | last-write-wins / merge / manual-reconcile / reject-stale / undefined | adequate / inadequate / undefined | |

Inadequate or undefined: cite RULE-CR-DCV; entry becomes DCV-CR-NN.
No DCV findings: `DCV-NIL-1` -- [scope rationale].
All strategies adequate: CONFLICT RESOLUTION CLOSED.

**MRF -- Missing Recovery Flows**

| ID | Scenario Ref | Recovery Gap | Why No Current Path Exists |
|---|---|---|---|
| MRF-01 | FS-NN | | |

No MRF findings: `MRF-NIL-1` -- [scope rationale].

GATE 3 STATUS: OPEN / CLOSED
Reason if OPEN: [missing category or nil rationale absent]

---

### GATE 4: Amendment Pass

| AMD ID | Entry ID | Original (summary) | Amended (summary) | Rule Invoked | Gate Re-Opened? |
|---|---|---|---|---|---|
| AMD-01 | | | | RULE-NIL-SUPERSEDE / -- | Gate N: AMENDED / no |

Nil supersessions: annotate inline in Gate 3 tables.
No amendments: "Gate 4: no amendments required."
No gate re-opens: "No gate re-opens triggered."

GATE 4 STATUS: OPEN / CLOSED

---

### GATE 5: Commerce Domain Validation

| Scenario ID | Commerce Operation Named? | Amended Operation (if RULE-COMMERCE-ANCHOR applied) |
|---|---|---|
| FS-01 | Yes / No | |

Additional commerce-domain findings:

| ID | Type | Finding | Source Scenario |
|---|---|---|---|
| CV-DCV-01 | DCV / OEG / MRF | | FS-NN |

COMMERCE VALIDATION COMPLETE

---

### TERMINAL: Nil Supersession Log

| Nil ID | Gap Type | State | Superseded By | Gate |
|---|---|---|---|---|
| OEG-NIL-1 | OEG | ACTIVE / SUPERSEDED | -- / OEG-F-02 | -- / Gate 4 |

No supersessions: "No supersessions in this run."

---

### TERMINAL: Scope Verification

| Declared Operation | Covered | Gap Finding |
|---|---|---|
| [operation] | Yes / No | SV-GAP-NN / -- |

SCOPE VERIFICATION COMPLETE

---

### TERMINAL: Post-Analysis Rule Registry Audit

**BYPASS-TRIGGER column protocol**: If Status is RULE-BYPASSED, the BYPASS-TRIGGER column
must contain a non-empty gate-reopening directive. An empty BYPASS-TRIGGER cell beside a
RULE-BYPASSED row is itself an audit failure.

| Rule ID | Invocations | Gate Citations (gate, entry) | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-CR-DCV | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty if INVOKED/ABSENT; `GATE N-bypass: REOPEN -- apply RULE-CR-DCV at [gate, entry]` if BYPASSED] |
| RULE-BARRED-CG | | | | |
| RULE-NIL-SUPERSEDE | | | | |
| RULE-COMMERCE-ANCHOR | | | | |

**If any BYPASS-TRIGGER cell is non-empty**:
1. Emit the named sub-gate: `GATE N-bypass: REOPENED`; state rule ID and bypass entry.
2. Apply rule; produce required output (DCV-NN, CG-NN, SUPERSEDED annotation, or anchor).
3. Emit: `GATE N-bypass: AMENDED -- CLOSED`
4. Return to audit table; update Status -> INVOKED; add sub-gate reference to Citations.

POST-ANALYSIS REGISTRY AUDIT COMPLETE
Confirm: BYPASS-TRIGGER column is entirely empty OR all non-empty cells have resolved
GATE N-bypass: AMENDED -- CLOSED blocks.

C-30 note: This analysis is single-act (Gates 1--5 run by a single analyst sequence).
C-30 scores N/A (PARTIAL) -- no dual act boundary requires independent sign-off.

ANALYSIS COMPLETE

---

---

## V-03

**Variation axis**: Lifecycle emphasis -- every gate and every act is bounded by a named
GATE-OPEN block and a named GATE-CLOSE block. Acts additionally close with an ACT-CLOSE
block containing the three-item C-30 sign-off checklist. No gate or act may be declared
closed without satisfying its exit postconditions.

**Hypothesis**: R8 V-03 showed that GATE-OPEN / GATE-CLOSE blocks make gate boundaries
independently auditable by structural scan. Extending the same pattern to act boundaries
with ACT-CLOSE blocks enforces C-30 structurally: each act's closure is a named artifact
with three verifiable postconditions, not an implicit terminal state. An analyst who omits
the ACT-CLOSE block leaves an open act, visible at scan time.

---

You are running the **flow-resilience** skill for `{topic}`.

Lifecycle rules:
1. Every analysis gate is bounded by a GATE-OPEN block (preconditions) and a GATE-CLOSE
   block (exit postconditions + status).
2. Every analysis act is bounded by an ACT-OPEN declaration and an ACT-CLOSE block with
   the three C-30 sign-off items.
3. A gate with no GATE-CLOSE block is implicitly OPEN. An act with no ACT-CLOSE block is
   implicitly OPEN. Neither state may persist at COMPLETE.

---

### RULE REGISTRY

**RULE-CR-DCV**: Concurrent state modification without coordination mechanism -> emit DCV-NN.
Record invocation: "RULE-CR-DCV at Gate 2, FS-NN -> DCV-NN pending Gate 3."

**RULE-BARRED-CG**: Unresolvable confidence basis -> mark BARRED -> emit CG-NN.
Record invocation: "RULE-BARRED-CG at Gate 1, FS-NN -> CG-NN."

**RULE-NIL-SUPERSEDE**: Downstream finding supersedes typed nil -> annotate nil SUPERSEDED.
Record invocation: "RULE-NIL-SUPERSEDE at Gate 4, AMD-NN -> NIL-ID: SUPERSEDED by F-NN."

**RULE-COMMERCE-ANCHOR**: Include scenario has no named commerce flow -> amend.
Record invocation: "RULE-COMMERCE-ANCHOR at Gate 5, FS-NN -> [amended operation]."

---

### Pre-Analysis: Commerce Operation Scope Declaration

Operations in scope: [list at least four from checkout, inventory reservation,
payment processing, order fulfillment, cart state, loyalty redemption, return/refund]
Operations excluded (with reason): [list or "none"]

SCOPE DECLARATION COMPLETE

### Pre-Analysis: Coverage Accountability Roster

| Degradation Class | Committed Minimum |
|---|---|
| Network partition / offline | 2 |
| Partial service failure | 2 |
| Eventual consistency | 2 |

DS Primitive required for any class that cannot reach committed minimum.

---

```
ACT 1 OPEN -- Distributed Systems Expert
Scope: Gates 1-4 + post-analysis registry audit (Act 1 rules) + ACT-CLOSE
```

### GATE 1: Discovery and Triage

```
GATE 1 OPEN
Preconditions:
  [x] SCOPE DECLARATION COMPLETE present
  [x] Coverage Accountability Roster committed
Entry confirmed: [yes / no]
```

For each failure scenario candidate: ID (FS-NN) | failure class | confidence basis |
disposition (Include / BARRED / Argued-Impossible).
BARRED: invoke RULE-BARRED-CG; emit CG-NN.
Argued-Impossible: cite DS Primitive by name.

Disposition table: ID | Failure Class | Confidence Basis | Disposition | Notes

**Gate 1b -- BARRED Resolution Sub-Gate**

```
GATE 1b OPEN
Precondition: Gate 1 discovery complete; BARRED entries identified or "none."
```

Attempt resolution of each BARRED entry.
Resolved: `GATE 1b: RESOLVED` -- entry ID, mechanism, new disposition.
Unresolved: entry remains BARRED; CG entry stands.
No BARRED entries: "Gate 1b: no BARRED entries present."

```
GATE 1b CLOSE
Exit postconditions:
  [ ] Every BARRED entry has a GATE 1b: RESOLVED record or a standing CG entry
  [ ] No BARRED entry promoted to Include without a resolution record
Gate 1b STATUS: CLOSED / OPEN
Reason if OPEN: [entry ID and unmet condition]
```

```
GATE 1 CLOSE
Exit postconditions:
  [ ] Every candidate has exactly one named disposition
  [ ] Every BARRED entry has a CG-NN in the coverage log
  [ ] Every Argued-Impossible cites a DS Primitive by name
  [ ] Coverage Accountability Roster updated with actual counts
Gate 1 STATUS: CLOSED / OPEN
Reason if OPEN: [blocking entry or condition]
```

---

### GATE 2: Four-Field Scenario Analysis

```
GATE 2 OPEN
Preconditions:
  [x] Gate 1 STATUS: CLOSED
Entry confirmed: [yes / no]
```

For each Include scenario, produce:
1. **State** -- specific system state at failure onset
2. **Capability** -- named actions the user can still take
3. **Data at risk** -- named data type and consistency failure mode
4. **Recovery path** -- concrete steps; each names the actor (`client` | `server` |
   `operator` | `user`). Minimum two actor-labeled steps.

Annotate: Severity (`degraded` | `impaired` | `down`) and Blast radius.
Concurrent-modification scenarios: invoke RULE-CR-DCV inline.

```
GATE 2 CLOSE
Exit postconditions:
  [ ] Every Include scenario has all four fields with non-trivial content
  [ ] Every scenario has severity and blast radius annotations
  [ ] Every recovery path has at least two actor-labeled steps
  [ ] All RULE-CR-DCV invocations recorded inline
  [ ] Coverage Accountability Roster per-class counts verified
Gate 2 STATUS: CLOSED / OPEN
Reason if OPEN: [scenario ID and missing field or unmet count]
```

---

### GATE 3: Gap Identification

```
GATE 3 OPEN
Preconditions:
  [x] Gate 2 STATUS: CLOSED
Entry confirmed: [yes / no]
```

**OEG -- Offline Experience Gaps**
Each gap: OEG-NN, description, actionable recommendation.
No gaps: `OEG-NIL-1: [scope rationale]`

**DCV -- Data Consistency Violations**
Each violation: DCV-NN, data type, failure mode.
Pending RULE-CR-DCV entries: assign DCV-NN now; confirm linkage.
No violations: `DCV-NIL-1: [scope rationale]`

**MRF -- Missing Recovery Flows**
Each missing flow: MRF-NN, scenario ref, absent mechanism.
No missing flows: `MRF-NIL-1: [scope rationale]`

**Conflict Resolution Analysis**
Per eventual-consistency scenario: name strategy (canonical only), adequacy verdict.
Inadequate/undefined: invoke RULE-CR-DCV; emit DCV-CR-NN with source linkage.
All adequate: CONFLICT RESOLUTION CLOSED.

```
GATE 3 CLOSE
Exit postconditions:
  [ ] All three gap sections present: OEG, DCV, MRF
  [ ] Every section has at least one named finding or a typed nil with scope rationale
  [ ] All pending RULE-CR-DCV entries have assigned DCV-NN identifiers
  [ ] Conflict resolution verdict present for every eventual-consistency scenario
Gate 3 STATUS: CLOSED / OPEN
Reason if OPEN: [missing category or nil rationale absent]
```

---

### GATE 4: Amendment Pass

```
GATE 4 OPEN
Preconditions:
  [x] Gate 3 STATUS: CLOSED
Entry confirmed: [yes / no]
```

Review all prior gate outputs for amendments:
- Vague recovery paths -> add actor-labeled steps; record entry ID, original, amended.
- Typed nil superseded by Gate 3 finding -> invoke RULE-NIL-SUPERSEDE.
- Late CR finding requiring DCV addition -> reopen Gate 3 under `GATE 3: AMENDED`.

For each gate re-open: sub-gate label, triggering finding ID, re-close confirmation.

No amendments: "Gate 4: no amendments."
No re-opens: "No gate re-opens triggered."

```
GATE 4 CLOSE
Exit postconditions:
  [ ] All recovery paths have actor-labeled steps
  [ ] Every superseded nil carries SUPERSEDED annotation with finding ID
  [ ] Every late DCV finding is in Gate 3: AMENDED with re-close confirmation
  [ ] No RULE-NIL-SUPERSEDE invocation unrecorded
Gate 4 STATUS: CLOSED / OPEN
Reason if OPEN: [outstanding amendment or unresolved re-open]
```

---

### TERMINAL: Post-Analysis Rule Registry Audit (Act 1)

```
POST-ANALYSIS REGISTRY AUDIT OPEN (ACT 1)
Preconditions:
  [x] Gate 4 STATUS: CLOSED
```

For each rule (Act 1 scope), report invocation count, citations, and status.

**RULE-CR-DCV**
Invocations: [N] | Citations: [Gate 2 FS-NN -> DCV-NN; Gate 3 CR FS-NN -> DCV-CR-NN]
Status: INVOKED / SCENARIO-ABSENT / RULE-BYPASSED

**RULE-BARRED-CG**
Invocations: [N] | Citations: [Gate 1 FS-NN -> CG-NN]
Status: INVOKED / SCENARIO-ABSENT / RULE-BYPASSED

**RULE-NIL-SUPERSEDE**
Invocations: [N] | Citations: [Gate 4 AMD-NN, NIL-ID]
Status: INVOKED / SCENARIO-ABSENT / RULE-BYPASSED

**Bypass Gate-Reopening (C-29)**: For each RULE-BYPASSED entry:

```
GATE N-bypass: REOPENED
Rule ID: [which rule was bypassed]
Bypass entry: [gate + entry where bypass occurred]
```

[Apply rule: emit required DCV-NN, CG-NN, SUPERSEDED annotation, or actor-labeled step]

```
GATE N-bypass: AMENDED -- CLOSED
Rule now applied at: [gate and entry]
Audit row updated: [rule ID] Status -> INVOKED; Citations += [sub-gate reference]
```

Repeat for each RULE-BYPASSED entry.

```
POST-ANALYSIS REGISTRY AUDIT CLOSE (ACT 1)
Exit postconditions:
  [ ] Every rule has a status entry
  [ ] Every RULE-BYPASSED entry has a completed GATE N-bypass: AMENDED -- CLOSED block
  [ ] No RULE-BYPASSED entry remains unresolved
Act 1 Registry Audit STATUS: CLOSED / OPEN
```

---

```
ACT 1 CLOSE (C-30 per-act sign-off)
(1) All gates within Act 1 CLOSED:
    Gate 1: [CLOSED / OPEN -- reason]
    Gate 1b: [CLOSED / N/A]
    Gate 2: [CLOSED / OPEN -- reason]
    Gate 3: [CLOSED / OPEN -- reason]
    Gate 4: [CLOSED / OPEN -- reason]
    GATE N-bypass blocks (if any): [CLOSED / none triggered]
    Act 1 Registry Audit: [CLOSED / OPEN -- reason]
(2) Act 1 scope exhausted: [yes -- all Include scenarios analyzed through Gate 4]
(3) No RULE-BYPASSED conditions remain unresolved within Act 1: [yes / exception detail]
ACT 1 STATUS: CLOSED / OPEN
```

---

```
ACT 2 OPEN -- Commerce Domain Validator
Entry condition: ACT 1 STATUS: CLOSED
Scope: Gate 5 + post-analysis registry audit (Act 2 rules) + ACT-CLOSE
```

### GATE 5: Commerce Domain Validation

```
GATE 5 OPEN
Preconditions:
  [x] ACT 1 STATUS: CLOSED
Entry confirmed: [yes / no]
```

Review all Include scenarios from Gates 1--4. For each: confirm commerce operation named.
If not: invoke RULE-COMMERCE-ANCHOR; amend; record under COMMERCE VALIDATION AMENDMENTS.
Identify additional commerce-domain findings (inventory oversell, payment idempotency
window expiry, loyalty double-redemption, order state divergence).
Issue as CV-DCV-NN, CV-OEG-NN, or CV-MRF-NN.

COMMERCE VALIDATION COMPLETE
Scenarios reviewed: [N] | RULE-COMMERCE-ANCHOR invocations: [N or "none"]
Additional findings: [IDs or "none"]

```
GATE 5 CLOSE
Exit postconditions:
  [ ] Every Include scenario anchored to a named commerce operation
  [ ] All RULE-COMMERCE-ANCHOR invocations recorded with scenario ID and amended name
  [ ] Any additional CV findings assigned and recorded
Gate 5 STATUS: CLOSED / OPEN
Reason if OPEN: [scenario without commerce anchor or rule not applied]
```

---

### TERMINAL: Post-Analysis Rule Registry Audit (Act 2)

```
POST-ANALYSIS REGISTRY AUDIT OPEN (ACT 2)
Preconditions:
  [x] Gate 5 STATUS: CLOSED
```

**RULE-COMMERCE-ANCHOR**
Invocations: [N] | Citations: [Gate 5 FS-NN -> amended operation]
Status: INVOKED / SCENARIO-ABSENT / RULE-BYPASSED

**Bypass Gate-Reopening (C-29) if RULE-BYPASSED**:

```
GATE 5-bypass: REOPENED
Rule ID: RULE-COMMERCE-ANCHOR
Bypass entry: [Gate 5 scenario ID where anchor was missing but rule not applied]
```

[Apply rule: amend scenario to name specific commerce operation; record amendment]

```
GATE 5-bypass: AMENDED -- CLOSED
Rule now applied at Gate 5, [scenario ID]
Audit row updated: RULE-COMMERCE-ANCHOR Status -> INVOKED
```

```
POST-ANALYSIS REGISTRY AUDIT CLOSE (ACT 2)
Exit postconditions:
  [ ] RULE-COMMERCE-ANCHOR has a status entry
  [ ] Any RULE-BYPASSED entry resolved with GATE 5-bypass: AMENDED -- CLOSED
Act 2 Registry Audit STATUS: CLOSED / OPEN
```

---

### TERMINAL: Nil Supersession Log

List every typed nil issued. State: `ACTIVE` | `SUPERSEDED`.
If SUPERSEDED: cite finding ID and gate. No supersessions: "No supersessions in this run."

---

### TERMINAL: Scope Verification

| Declared Operation | Covered | Gap Finding |
|---|---|---|
| [operation] | Yes / No | SV-GAP-NN / -- |

SCOPE VERIFICATION COMPLETE

---

```
ACT 2 CLOSE (C-30 per-act sign-off)
(1) All gates within Act 2 CLOSED:
    Gate 5: [CLOSED / OPEN -- reason]
    GATE 5-bypass blocks (if any): [CLOSED / none triggered]
    Act 2 Registry Audit: [CLOSED / OPEN -- reason]
(2) Act 2 scope exhausted: [yes -- all scenarios reviewed for commerce anchoring;
    all additional CV findings issued]
(3) No RULE-BYPASSED conditions remain unresolved within Act 2: [yes / exception detail]
ACT 2 STATUS: CLOSED / OPEN
```

ANALYSIS COMPLETE (declared only when ACT 1 STATUS: CLOSED AND ACT 2 STATUS: CLOSED)

---

---

## V-04

**Variation axis**: Phrasing register (conversational/imperative) + Inertia framing
(status-quo competitor prominently named in the gap identification and synthesis sections).

**Hypothesis**: Formal block-syntax prompts create compliance by bureaucratic completeness --
the analyst fills the template. Conversational imperative prompts create compliance by
decision pressure -- "Do this now: if you find concurrent modification, invoke RULE-CR-DCV
before moving on." The inertia framing surfaces the real cost of not addressing degradation
gaps by naming the status-quo alternative (accepting the carrying cost) as a visible
competitor to each finding, giving the synthesis section measurable stakes.

---

You are running the **flow-resilience** skill for `{topic}`. Your job: simulate every
realistic way this feature can degrade, find the gaps in how the current system handles
those failures, and tell us whether the cost of fixing those gaps exceeds the cost of
carrying them. Do that honestly -- including the option of doing nothing.

Work through five gates in order. Do not skip ahead. At the end, audit every rule you
were supposed to apply and fix anything you missed.

---

### Rules You Are Accountable For

Write these down before starting. You will be asked to account for every one of them.

**RULE-CR-DCV** -- Any time two actors can write to the same state at the same time without
coordination, that is a Data Consistency Violation. Name it, assign it a DCV-NN identifier,
and put it in your Gap findings. Do not describe it as "potential" or "may cause issues."

**RULE-BARRED-CG** -- Any scenario you cannot ground in the available context gets marked
BARRED. When you mark something BARRED, emit a Coverage Gap entry (CG-NN). The CG entry
stays in the record even if you later resolve the BARRED entry.

**RULE-NIL-SUPERSEDE** -- If you issue a "no findings here" nil identifier and later find
an actual finding in that category, go back and mark the nil SUPERSEDED. Do not let it
stand as if the category were still empty.

**RULE-COMMERCE-ANCHOR** -- Every scenario must be anchored to a real commerce operation --
checkout, inventory reservation, payment processing, order fulfillment, cart state. If you
have a scenario that only says "data write" or "state update," amend it to name the actual
commerce operation.

---

### Before You Start: Commit to Your Scope

Name at least four commerce operations this analysis covers. Name any you are explicitly
leaving out and say why.

Operations in scope: [list]
Exclusions: [list or "none"]

SCOPE DECLARATION COMPLETE

Now commit to minimum coverage: at least two scenarios per degradation class (offline,
partial failure, eventual consistency). If a class is impossible for this deployment, cite
the specific architecture constraint -- not a description-scope argument.

| Degradation Class | Committed Minimum |
|---|---|
| Network partition / offline | 2 |
| Partial service failure | 2 |
| Eventual consistency | 2 |

---

### Gate 1 -- Find Your Scenarios

For each scenario candidate you identify: give it an ID (FS-NN), name its failure class,
state your confidence basis, and commit to a disposition: Include, BARRED, or
Argued-Impossible.

If you mark something BARRED: invoke RULE-BARRED-CG right now. Emit the CG-NN entry.

If you argue something is impossible: name the DS primitive that makes it impossible.
"The topic doesn't mention distributed deployment" is not a DS primitive.

Then check: can any BARRED entry be resolved? If yes, record the resolution. If not,
the CG entry stands.

GATE 1 STATUS: CLOSED when every candidate has a disposition, every BARRED entry has
a CG-NN, and every Argued-Impossible cites a named DS primitive.

---

### Gate 2 -- Build Each Scenario

For each Include scenario, write four things. All four are required. Missing any one
of them makes the scenario incomplete.

1. **State** -- What exactly is the system doing when this failure hits? Name the
   components and their states. Not "the system is degraded."

2. **Capability** -- What can the user actually do? Name the specific operations that
   still work. Not "some features remain available."

3. **Data at risk** -- What specific data could be lost, stale, or inconsistent?
   Name the data type and how the consistency failure manifests.

4. **Recovery path** -- How does the system get back to healthy? Write out each step.
   Every step names who does it: `client`, `server`, `operator`, or `user`. Minimum two
   named-actor steps per path.

Also: label the severity (`degraded` / `impaired` / `down`) and name the blast radius.

If any scenario involves two actors modifying the same state without coordination:
invoke RULE-CR-DCV right now, before moving to the next scenario. Record: "RULE-CR-DCV
invoked -- Gate 2, FS-NN -> DCV-NN pending Gate 3." Do not defer this.

GATE 2 STATUS: CLOSED when every Include scenario has all four fields, every severity
and blast radius are labeled, and every RULE-CR-DCV trigger has been invoked and recorded.

---

### Gate 3 -- Name the Gaps (and Name What Doing Nothing Costs)

Three gap categories. You must address all three. For each category: either find the
gap or issue a typed nil with a scope rationale. "None found" without a rationale is
not acceptable.

**Offline Experience Gaps (OEG-NN)**
What can the user not do offline that the current system does not handle or surface
clearly? For each gap: name it, explain why it matters to the user, and state what the
status-quo carrying cost is if the gap is not addressed. Carrying cost: name the specific
user-visible failure mode (cart drop, stale restore, lost order) and the rate at which
it compounds (per session, per deploy, per transaction).

No gaps: `OEG-NIL-1: [scope rationale -- specific deployment constraint that forecloses
offline experience gaps]`

**Data Consistency Violations (DCV-NN)**
Assign DCV-NN identifiers to all RULE-CR-DCV entries pending from Gate 2.
For each violation: name the data, the failure mode, and the status-quo carrying cost
(rate + horizon). For every eventual-consistency scenario, name the conflict resolution
strategy using canonical vocabulary only: `last-write-wins`, `merge`, `manual-reconcile`,
`reject-stale`. State whether it is adequate. If inadequate or undefined: invoke
RULE-CR-DCV and emit DCV-CR-NN.

No violations: `DCV-NIL-1: [scope rationale]`

**Missing Recovery Flows (MRF-NN)**
What recovery does the system not provide? For each: name the scenario, the absent
mechanism, and the status-quo carrying cost (what happens to the user if there is no
recovery path and they just wait).

No missing flows: `MRF-NIL-1: [scope rationale]`

GATE 3 STATUS: CLOSED when all three categories are addressed and every category has
at least one named finding or a typed nil with a specific scope rationale.

---

### Gate 4 -- Fix What Needs Fixing

Look back at everything you produced in Gates 1--3. Make three checks:

1. Are any recovery paths still vague (no named actors)? Amend them. Record: entry ID,
   what you changed, and why.

2. Did any typed nil get superseded by a finding you introduced later? Invoke
   RULE-NIL-SUPERSEDE. Annotate the nil as SUPERSEDED, citing the finding ID.

3. Did any conflict-resolution inadequacy in Gate 3 require a new DCV entry that belongs
   in Gate 3? If so, reopen Gate 3 under `GATE 3: AMENDED`, add the entry, re-close.

If nothing needs fixing: "Gate 4: no amendments in this run. No gate re-opens triggered."

GATE 4 STATUS: CLOSED when all recovery paths have named actors, all superseded nils are
annotated, and all late DCV entries are in Gate 3: AMENDED with re-close confirmation.

---

### Gate 5 -- Commerce Domain Check

Look at every Include scenario. Is each one anchored to a named commerce operation?
Checkout, inventory reservation, payment processing, order fulfillment, cart state --
one of these or another real commerce operation must appear by name.

If any scenario only says something generic: invoke RULE-COMMERCE-ANCHOR, amend it,
record the amendment.

Now look at the Gap findings from a commerce expert's lens. Did Gates 1--4 miss:
- Inventory oversell under partition?
- Payment idempotency window expiry under partial failure?
- Loyalty point double-redemption under split-brain?
- Order state divergence under partial fulfillment failure?

If yes: issue CV-DCV-NN, CV-OEG-NN, or CV-MRF-NN.

COMMERCE VALIDATION COMPLETE | Scenarios reviewed: [N] | RULE-COMMERCE-ANCHOR: [N or none]

GATE 5 STATUS: CLOSED when every scenario is anchored and all CV findings are issued.

---

### Terminal: Nil Supersession Log

Every typed nil you issued: list it, state whether it is ACTIVE or SUPERSEDED, and if
SUPERSEDED, name what superseded it and where.

---

### Terminal: Scope Verification

Every operation you declared in scope at the start: did at least one scenario cover it?
If not: record SV-GAP-NN. An uncovered declared operation with no impossibility argument
is an open scope gap.

| Declared Operation | Covered | Gap Finding |
|---|---|---|
| [operation] | Yes / No | SV-GAP-NN / -- |

SCOPE VERIFICATION COMPLETE

---

### Terminal: Rule Registry Audit -- Account for Everything

Go through every rule you declared at the start. For each one:

- How many times did it fire?
- What did it produce? (Name the gate and the finding ID for every invocation.)
- Status: `INVOKED` (fired and cited), `SCENARIO-ABSENT` (trigger never came up --
  that is fine), or `RULE-BYPASSED` (the trigger came up but you did not apply the rule
  -- that is an audit failure).

| Rule ID | Invocations | Gate + Finding Citations | Status |
|---|---|---|---|
| RULE-CR-DCV | | | |
| RULE-BARRED-CG | | | |
| RULE-NIL-SUPERSEDE | | | |
| RULE-COMMERCE-ANCHOR | | | |

**If any rule shows RULE-BYPASSED** -- do not proceed to COMPLETE. Go back now:
1. Name the gate where the bypass occurred.
2. Reopen that gate: write `GATE N-bypass: REOPENED -- [rule ID] -- [entry where bypass occurred]`.
3. Apply the rule. Produce the finding, amendment, or annotation it requires.
4. Close the gate: `GATE N-bypass: AMENDED -- CLOSED`.
5. Return to this table. Update the Status to INVOKED. Add the sub-gate to Citations.

Only proceed to COMPLETE when the Status column contains no RULE-BYPASSED entries.

POST-ANALYSIS REGISTRY AUDIT COMPLETE

---

### Inertia Synthesis -- Should We Fix This?

This analysis found [N] gap findings across [M] failure classes. Before recommending action,
name the status-quo competitor: what does the team gain by not addressing these gaps?

State: the current carrying cost (which finding, which rate, which horizon), the status-quo
option (accept the carrying cost and monitor), and the intervention recommendation (fix this
finding first, at this threshold, owned by this team). Be direct about the trade-off -- if
the carrying cost is low and the fix cost is high, say so.

Urgency: HIGH / MEDIUM / LOW
Highest-risk finding: [gap ID] -- [rate + horizon from Gate 3]
Status-quo option: [describe what "do nothing" looks like for this specific feature]
Intervention recommendation: [owner, trigger threshold, consequence of missing threshold]

C-30 note: This is a single-act analysis. C-30 scores N/A (PARTIAL) -- per-act sign-off
blocks are not required for a single analyst sequence with no act boundary.

ANALYSIS COMPLETE

---

---

## V-05

**Variation axis**: Full integration -- Role sequence (DS Expert owns bypass-gate-reopening;
Commerce Validator owns Act 2 sign-off) + lifecycle emphasis (ACT-OPEN / ACT-CLOSE blocks
with C-30 sign-off) + table-dominant rule registry audit with BYPASS-TRIGGER column +
conversational enforcement framing at bypass-trigger points + inertia competitor
prominently featured in Gap Register and synthesis.

**Hypothesis**: The maximum criteria surface requires all axes simultaneously: role
accountability for bypass handling (C-29 ownership clear), structural ACT-CLOSE blocks
(C-30 independently verifiable), table audit with BYPASS-TRIGGER column (C-29 visible at
scan time), conversational bypass instruction at point-of-use (no ambiguity about what to
do when a bypass is found), and inertia framing in the gap and synthesis sections (C-16
depth). No single-axis variation achieves all five simultaneously.

---

You are running the **flow-resilience** skill for `{topic}`.

This analysis runs in two sequential acts. Act 1 is the Distributed Systems Expert.
Act 2 is the Commerce Domain Validator. Each act closes with a formal sign-off.
Do not blend the acts.

---

### RULE REGISTRY

| Rule ID | Trigger Condition | Action Required | Bypass Owner |
|---|---|---|---|
| RULE-CR-DCV | Concurrent state modification without coordination mechanism | Emit DCV-NN in Gate 3 | DS Expert (Act 1) |
| RULE-BARRED-CG | Discovery entry confidence basis unresolvable | Mark BARRED; emit CG-NN | DS Expert (Act 1) |
| RULE-NIL-SUPERSEDE | Downstream finding supersedes a typed nil | Annotate nil SUPERSEDED | DS Expert (Act 1) |
| RULE-COMMERCE-ANCHOR | Include scenario has no named commerce operation | Amend to name operation | Commerce Validator (Act 2) |

**Bypass Owner column**: If a rule shows RULE-BYPASSED in the registry audit, the named
owner for that rule is responsible for invoking the bypass gate-reopening protocol.
Commerce Validator cannot re-open Act 1 gates; DS Expert cannot re-open Act 2 gates.

---

### Bypass Gate-Reopening Protocol

When the Post-Analysis Rule Registry Audit records any rule as RULE-BYPASSED:

1. The Bypass Owner named in the registry emits: `GATE N-bypass: REOPENED -- [rule ID] --
   bypass at [gate, entry ID]`.
2. The Bypass Owner applies the rule: produces DCV-NN, CG-NN, SUPERSEDED annotation,
   or commerce anchor amendment.
3. The Bypass Owner emits: `GATE N-bypass: AMENDED -- CLOSED -- [rule now applied]`.
4. The Bypass Owner returns to the audit table and updates:
   - Status: RULE-BYPASSED -> INVOKED
   - BYPASS-TRIGGER cell: cleared (or crossed to "RESOLVED -- [sub-gate reference]")
   - Citations: add sub-gate reference

COMPLETE may not be declared while any RULE-BYPASSED entry remains unresolved in any act.

---

### Pre-Analysis: Commerce Operation Scope Declaration

Declare before Gate 1. Minimum four operations from: checkout, inventory reservation,
payment processing, order fulfillment, cart state, loyalty redemption, return/refund.

Operations in scope: [list]
Exclusions (with reason): [list or "none"]

SCOPE DECLARATION COMPLETE

### Pre-Analysis: Coverage Accountability Roster

| Degradation Class | Committed Minimum | DS Primitive for Impossibility |
|---|---|---|
| Network partition / offline | 2 | [required if slot unfilable] |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

---

```
ACT 1 OPEN -- Distributed Systems Expert
Scope: Gates 1-4 + Act 1 Registry Audit + Nil Supersession Log + Scope Verification + ACT 1 CLOSE
```

### GATE 1: Discovery and Triage

```
GATE 1 OPEN
Preconditions:
  [x] SCOPE DECLARATION COMPLETE present
  [x] Coverage Accountability Roster committed
Entry confirmed: [yes / no]
```

| ID | Failure Class | Confidence Basis | Disposition | Rule Applied | Notes |
|---|---|---|---|---|---|
| FS-01 | | | Include / BARRED / Argued-Impossible | | |

BARRED: cite RULE-BARRED-CG. Argued-Impossible: name DS Primitive.

**Gate 1b -- BARRED Resolution**

| BARRED ID | Confidence Basis | Resolved? | Mechanism | New Disposition |
|---|---|---|---|---|

No BARRED entries: "Gate 1b: none."

```
GATE 1 CLOSE
Exit postconditions:
  [ ] Every candidate has one named disposition
  [ ] Every BARRED entry has CG-NN in the coverage log
  [ ] Every Argued-Impossible cites DS Primitive by name
  [ ] Coverage Accountability Roster counts updated
Gate 1 STATUS: CLOSED / OPEN
```

---

### GATE 2: Four-Field Scenario Analysis

```
GATE 2 OPEN
Preconditions:
  [x] Gate 1 STATUS: CLOSED
Entry confirmed: [yes / no]
```

| ID | State | Capability | Data at Risk | Recovery Path (actor-labeled) | Severity | Blast Radius | Rule Applied |
|---|---|---|---|---|---|---|---|
| FS-01 | | | | 1. [actor]: [step]; 2. [actor]: [step] | degraded/impaired/down | | RULE-CR-DCV or -- |

State: specific configuration. Capability: named commerce operations. Data at Risk:
data type and failure mode. Recovery Path: minimum two named-actor steps.

```
GATE 2 CLOSE
Exit postconditions:
  [ ] Every Include scenario has all four fields with non-trivial content
  [ ] Every severity and blast radius labeled
  [ ] Every recovery path has minimum two actor-labeled steps
  [ ] All RULE-CR-DCV triggers recorded in Rule Applied column
Gate 2 STATUS: CLOSED / OPEN
```

---

### GATE 3: Gap Identification

```
GATE 3 OPEN
Preconditions:
  [x] Gate 2 STATUS: CLOSED
Entry confirmed: [yes / no]
```

**OEG -- Offline Experience Gaps**

| ID | Scenario Ref | Gap Description | Status-Quo Carrying Cost | Actionable Recommendation |
|---|---|---|---|---|
| OEG-01 | FS-NN | | [rate + horizon + user-visible failure mode] | |

Status-Quo Carrying Cost: name what "doing nothing" looks like -- specific failure mode,
rate (per session / deploy / transaction), horizon (unbounded / session-scoped).
No OEG: `OEG-NIL-1: [scope rationale]`

**DCV -- Data Consistency Violations**

| ID | Source | Data Type | Failure Mode | Conflict Resolution | Adequacy | Status-Quo Carrying Cost | Rule Applied |
|---|---|---|---|---|---|---|---|
| DCV-01 | FS-NN | | | last-write-wins/merge/manual-reconcile/reject-stale/undefined | adequate/inadequate/undefined | [rate + horizon] | |

Pending RULE-CR-DCV entries from Gate 2: assign DCV-NN now. Confirm Gate 2 -> Gate 3
linkage in the Source column.
Inadequate/undefined adequacy: cite RULE-CR-DCV; emit DCV-CR-NN with source linkage.
All strategies adequate: CONFLICT RESOLUTION CLOSED.
No DCV: `DCV-NIL-1: [scope rationale]`

**MRF -- Missing Recovery Flows**

| ID | Scenario Ref | Recovery Gap | Status-Quo Carrying Cost | Why No Current Path Exists |
|---|---|---|---|---|
| MRF-01 | FS-NN | | [rate + horizon + user-visible failure] | |

No MRF: `MRF-NIL-1: [scope rationale]`

```
GATE 3 CLOSE
Exit postconditions:
  [ ] All three gap categories present (OEG, DCV, MRF)
  [ ] Every category has at least one named finding or a typed nil with scope rationale
  [ ] Every typed nil has a unique identifier
  [ ] All pending RULE-CR-DCV entries have DCV-NN assignments
  [ ] Conflict resolution verdict present for every eventual-consistency scenario
  [ ] Status-Quo Carrying Cost column populated for every named finding
Gate 3 STATUS: CLOSED / OPEN
```

---

### GATE 4: Amendment Pass

```
GATE 4 OPEN
Preconditions:
  [x] Gate 3 STATUS: CLOSED
Entry confirmed: [yes / no]
```

| AMD ID | Entry ID | Original (summary) | Amended (summary) | Rule Invoked | Gate Re-Opened? |
|---|---|---|---|---|---|
| AMD-01 | | | | RULE-NIL-SUPERSEDE / -- | Gate N: AMENDED / no |

No amendments: "Gate 4: no amendments. No gate re-opens triggered."

```
GATE 4 CLOSE
Exit postconditions:
  [ ] All recovery paths have actor-labeled steps
  [ ] Every superseded nil has SUPERSEDED annotation with finding ID
  [ ] Every late DCV finding is in Gate 3: AMENDED with re-close confirmation
Gate 4 STATUS: CLOSED / OPEN
```

---

### Act 1 Terminal: Post-Analysis Rule Registry Audit

**BYPASS-TRIGGER column**: RULE-BYPASSED in Status column -> non-empty BYPASS-TRIGGER
cell required. An empty BYPASS-TRIGGER cell beside RULE-BYPASSED is itself an audit
failure. DS Expert invokes the bypass gate-reopening protocol for all Act 1 rule bypasses.

| Rule ID | Invocations | Citations (gate, entry) | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-CR-DCV | | | INVOKED/SCENARIO-ABSENT/RULE-BYPASSED | [empty or `GATE N-bypass: REOPEN now -- apply RULE-CR-DCV at [gate, entry]`] |
| RULE-BARRED-CG | | | | |
| RULE-NIL-SUPERSEDE | | | | |

**If any BYPASS-TRIGGER cell is non-empty** -- DS Expert must resolve before ACT 1 CLOSE:

```
GATE N-bypass: REOPENED
Rule ID: [rule]  Bypass entry: [gate + entry ID]
```
[Apply rule now: emit DCV-NN / CG-NN / SUPERSEDED annotation / actor-labeled step]
```
GATE N-bypass: AMENDED -- CLOSED
Rule applied at: [gate, entry]  Audit update: Status -> INVOKED; Citations += [sub-gate]
```

POST-ANALYSIS REGISTRY AUDIT (ACT 1) COMPLETE

---

### Act 1 Terminal: Nil Supersession Log

| Nil ID | Gap Type | State | Superseded By | Gate |
|---|---|---|---|---|

No supersessions: "No supersessions in this run."

---

### Act 1 Terminal: Scope Verification

| Declared Operation | Covered | Gap Finding |
|---|---|---|
| [operation] | Yes / No | SV-GAP-NN / -- |

SCOPE VERIFICATION COMPLETE

---

```
ACT 1 CLOSE (C-30 sign-off)
(1) All gates within Act 1 CLOSED:
    Gate 1: [CLOSED / OPEN -- reason]
    Gate 1b: [CLOSED / N/A -- no BARRED entries]
    Gate 2: [CLOSED / OPEN -- reason]
    Gate 3: [CLOSED / OPEN -- reason]
    Gate 4: [CLOSED / OPEN -- reason]
    GATE N-bypass blocks (if triggered): [CLOSED / none triggered]
    Act 1 Registry Audit: [CLOSED / OPEN -- reason]
(2) Act 1 scope exhausted: [yes / list any unresolved items]
(3) No RULE-BYPASSED conditions remain unresolved within Act 1: [yes / exception detail]
ACT 1 STATUS: CLOSED / OPEN
```

---

```
ACT 2 OPEN -- Commerce Domain Validator
Entry condition: ACT 1 STATUS: CLOSED
Scope: Gate 5 + Act 2 Registry Audit + ACT 2 CLOSE
```

### GATE 5: Commerce Domain Validation

```
GATE 5 OPEN
Preconditions:
  [x] ACT 1 STATUS: CLOSED
Entry confirmed: [yes / no]
```

| Scenario ID | Commerce Operation Named? | Amended Operation (RULE-COMMERCE-ANCHOR) | CV Finding Issued |
|---|---|---|---|
| FS-01 | Yes / No | | -- / CV-DCV-01 / CV-OEG-01 / CV-MRF-01 |

Commerce-domain finding targets (check each):
- Inventory oversell under partition: [present / absent -- rationale]
- Payment idempotency window expiry: [present / absent -- rationale]
- Loyalty point double-redemption under split-brain: [present / absent -- rationale]
- Order state divergence under partial fulfillment: [present / absent -- rationale]

COMMERCE VALIDATION COMPLETE
Scenarios reviewed: [N] | RULE-COMMERCE-ANCHOR invocations: [N or "none"]

```
GATE 5 CLOSE
Exit postconditions:
  [ ] Every Include scenario anchored to a named commerce operation
  [ ] All RULE-COMMERCE-ANCHOR invocations recorded
  [ ] All four commerce-domain targets checked (present or rationale)
Gate 5 STATUS: CLOSED / OPEN
```

---

### Act 2 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-COMMERCE-ANCHOR | | | INVOKED/SCENARIO-ABSENT/RULE-BYPASSED | [empty or `GATE 5-bypass: REOPEN now`] |

**If BYPASS-TRIGGER non-empty** -- Commerce Validator resolves:

```
GATE 5-bypass: REOPENED
Rule ID: RULE-COMMERCE-ANCHOR  Bypass entry: [Gate 5 scenario ID]
```
[Apply rule: name the commerce operation; record amendment]
```
GATE 5-bypass: AMENDED -- CLOSED
Audit update: Status -> INVOKED
```

POST-ANALYSIS REGISTRY AUDIT (ACT 2) COMPLETE

---

### Inertia Synthesis -- What Does Doing Nothing Cost?

Name the status-quo competitor for each gap finding. This section has two required components:

**Per-finding carrying cost** (from Gate 3 Status-Quo Carrying Cost column):
For each named gap (OEG-NN, DCV-NN, MRF-NN), state: the failure mode, the rate (per
session / deploy / transaction), the horizon (unbounded / session-scoped / compound growth).
One sentence per finding. The status-quo is a real option -- quantify its cost honestly.

**Overall synthesis**:
Urgency: HIGH / MEDIUM / LOW
Highest-risk finding: [gap ID] -- [carrying cost from Gate 3]
Status-quo option: [what "do nothing" looks like for `{topic}` specifically -- not generic]
Intervention recommendation: [owner + threshold + consequence of missing threshold]

```
ACT 2 CLOSE (C-30 sign-off)
(1) All gates within Act 2 CLOSED:
    Gate 5: [CLOSED / OPEN -- reason]
    GATE 5-bypass blocks (if triggered): [CLOSED / none triggered]
    Act 2 Registry Audit: [CLOSED / OPEN -- reason]
(2) Act 2 scope exhausted: [yes -- all scenarios commerce-anchored; all CV targets checked;
    inertia synthesis complete]
(3) No RULE-BYPASSED conditions remain unresolved within Act 2: [yes / exception detail]
ACT 2 STATUS: CLOSED / OPEN
```

ANALYSIS COMPLETE (declared only when ACT 1 STATUS: CLOSED AND ACT 2 STATUS: CLOSED)
