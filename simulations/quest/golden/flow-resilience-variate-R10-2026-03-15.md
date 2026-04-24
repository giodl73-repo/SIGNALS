# Flow-Resilience Skill — Round 10 Variations (Rubric v10)

**Skill**: flow-resilience — Simulate degraded conditions: offline, partial failure, eventual
consistency.
**Rubric**: v10 (C-01 through C-34, essential/recommended/aspirational tiers)
**Date**: 2026-03-15

---

## Round 10 Context

**New criteria entering R10**: C-32 — Intra-Row Column-Group Gate (5-Level Architecture);
C-33 — Trigger Condition Column Specification; C-34 — Verification Signal per Recovery Stage.

**R9 diagnosis**:
- R9 V-05 achieved the ceiling entering R10: all of C-17 through C-31 PASS (15/26 = 5.77,
  composite 95.77). The full-integration axis combined role-sequence bypass ownership (C-31),
  BYPASS-TRIGGER column scanability (v9 ceiling signal), SLA-annotated recovery stages (C-30),
  three-component chronic accumulation framing (C-31), and multi-act sign-off (v9 C-30).
- C-32 gap: the architecture table names four structural levels. An ownership transition
  mid-row (Commerce Expert → DS Expert) is not gated — the model can complete C-phase columns
  then omit D-phase columns without any structural block. A column-group gate inside the row
  descriptor closes this at a level below slot, above individual column.
- C-33 gap: scenario entry conditions are described qualitatively in the scenario name or
  State field. Without a quantified threshold expression and observable detection signal,
  scenarios cannot be operationalized for alerting. A Trigger Condition column in the Column
  Contract makes both components mandatory and independently scannable.
- C-34 gap: recovery stages carry mechanism and SLA target (C-30). Neither alone confirms
  that a stage completed — the SLA records duration, not outcome. A named Verification Signal
  per stage makes each stage independently falsifiable: the stage is not done until the named
  observable artifact appears.

**Variation axes selected**:
- V-01: Single axis — Role sequence (Commerce Expert C-phase → DS Expert D-phase handoff
  within each row enforces the column-group gate; 5-level architecture named explicitly)
- V-02: Single axis — Output format (Trigger Condition column in Column Contract makes
  threshold expression + detection signal scannable; table-dominant throughout)
- V-03: Single axis — Lifecycle emphasis (per-stage VS blocks make each recovery stage
  falsifiable independent of SLA; VS co-located with mechanism + SLA in column spec)
- V-04: Combination — Role sequence + lifecycle emphasis = C-32 + C-34
- V-05: Full integration — all three axes = C-32 + C-33 + C-34

---

## V-01

**Variation axis**: Role sequence — Commerce Expert owns C-phase columns (State, Capability)
within each scenario row; DS Expert owns D-phase columns (Data at Risk, Recovery Path,
Severity, Blast Radius). An explicit intra-row column-group gate prevents D-phase from
beginning until C-phase is complete within that row. The five-level anti-omission architecture
names column-group as the fourth structural level between slot and column.

**Hypothesis**: The column-group gate is most naturally enforced via role sequence: when
Commerce Expert is accountable for C-phase and DS Expert is accountable for D-phase, the
gate instruction has a named owner at each side of the boundary. Without a named handoff,
the column-group transition is an invisible structural seam. Making the handoff explicit
inside the row descriptor — "C-phase complete; DS Expert begins D-phase" — creates an
auditable boundary that cannot be skipped without visibly omitting the handoff confirmation.

---

You are running the **flow-resilience** skill for `{topic}`.

This analysis runs in two sequential acts. Act 1 is the Distributed Systems Expert.
Act 2 is the Commerce Domain Validator. Each act closes with a formal sign-off.
Do not blend the acts.

---

### RULE REGISTRY

| Rule ID | Trigger Condition | Action Required | Bypass Owner |
|---|---|---|---|
| RULE-CR-DCV | Concurrent state modification by multiple actors without a coordination mechanism | Emit DCV-NN in Gate 3; cite rule inline at trigger point | DS Expert (Act 1) |
| RULE-BARRED-CG | Discovery entry confidence basis cannot be resolved from available context | Mark BARRED; emit CG-NN in coverage log | DS Expert (Act 1) |
| RULE-NIL-SUPERSEDE | Downstream finding introduced in a category that held a typed nil | Annotate nil SUPERSEDED citing new finding ID | DS Expert (Act 1) |
| RULE-COMMERCE-ANCHOR | Include scenario references a generic operation with no named commerce flow | Amend to name specific operation; record amendment | Commerce Validator (Act 2) |

**Bypass Owner column**: If a rule shows RULE-BYPASSED in the registry audit, the named
owner is responsible for invoking the bypass gate-reopening protocol. Commerce Validator
cannot reopen Act 1 gates; DS Expert cannot reopen Act 2 gates.

---

### BYPASS GATE-REOPENING PROTOCOL

**Authority**: DS Expert owns this protocol for Act 1 rules; Commerce Validator for Act 2
rules. Cross-act invocation is not permitted.

When any rule shows RULE-BYPASSED in the Post-Analysis Rule Registry Audit:

1. Bypass Owner emits: `GATE N-bypass: REOPENED — [rule ID] — bypass at [gate, entry ID]`
2. Bypass Owner applies the rule: produces DCV-NN, CG-NN, SUPERSEDED annotation, or commerce
   anchor amendment as the rule requires.
3. Bypass Owner emits: `GATE N-bypass: AMENDED — CLOSED — [rule now applied]`
4. Bypass Owner updates the audit row: Status → INVOKED; BYPASS-TRIGGER cell → cleared or
   annotated "RESOLVED — [sub-gate reference]"; Citations += sub-gate reference.

**COMPLETE may not be declared** while any RULE-BYPASSED entry remains unresolved in any act.

---

### ANTI-OMISSION ARCHITECTURE

The following five-level stack assigns one anti-omission mechanism per structural level.
Each mechanism targets a distinct omission risk. No two mechanisms duplicate each other.

| Level | Anti-Omission Mechanism | Omission Risk Targeted | Mechanism Location |
|---|---|---|---|
| Table | Unified row index (`#`) + anti-split instruction | Row fragmentation across ownership transitions | `#` column; anti-split instruction in Gate 2 |
| Section | Phase gate — all rows complete before Gap Identification section | Premature section advance before row set is exhausted | Section gate in Gate 2 |
| Slot | In-row bold imperative: **"Write this row now."** / **"Do not advance to Row N+1 until..."** | Row omission under token pressure | Row Descriptors (below) |
| Column-Group | Intra-row ownership phase gate: C-phase columns complete before D-phase columns begin within the same row | Mid-row D-phase omission when ownership shifts from Commerce Expert to DS Expert | Row Descriptors: Column-Group Gate (below) |
| Column | Column ownership per header (defined in Column Contract, below) | Individual column omission under ownership confusion | Column Contract (below) |

**Anti-split instruction**: Do not create separate sub-tables for Commerce Expert columns
and DS Expert columns. Do not insert a horizontal rule, heading, or section break between
rows when column ownership shifts from C-phase to D-phase within a row.

---

### COLUMN CONTRACT

Place this table before any scenario output. Every column in the Gate 2 scenario table must
have an entry here. A column missing from this contract is a contract violation.

| Column Name | Owner | Phase | Fill Requirement |
|---|---|---|---|
| `#` | Shared | — | Sequential integer; no gaps; no reuse across scenario classes |
| `ID` | Shared | — | FS-NN format; unique per scenario |
| `State` | Commerce Expert | C-phase | Specific system configuration when failure occurs; name components and their states; not "degraded" |
| `Capability` | Commerce Expert | C-phase | Named commerce operations the user can still complete; not "partial functionality" |
| `Data at Risk` | DS Expert | D-phase | Named data type + consistency failure mode (lost / stale / inconsistent with mechanism) |
| `Recovery Path` | DS Expert | D-phase | Four stages in sequence: Detect (mechanism \| TTD target); Contain (mechanism \| TTC target); Recover (mechanism \| TTR target); Validate (mechanism \| TTV target). Each stage names its actor. |
| `Severity` | DS Expert | D-phase | `degraded` / `impaired` / `down` |
| `Blast Radius` | DS Expert | D-phase | Fraction or named segment of users affected |
| `Rule Applied` | DS Expert | D-phase | Rule ID invoked at this row or `—` |

---

### Pre-Analysis: Commerce Operation Scope Declaration

Declare before Gate 1. Minimum four operations from: checkout, inventory reservation,
payment processing, order fulfillment, cart state, loyalty redemption, return/refund.

```
SCOPE DECLARATION
Operations in scope: [list each]
Operations explicitly excluded (with reason): [list or "none"]
SCOPE DECLARATION COMPLETE
```

### Pre-Analysis: Coverage Accountability Roster

| Degradation Class | Committed Minimum | DS Primitive for Impossibility |
|---|---|---|
| Network partition / offline | 2 | [required if slot unfillable] |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

---

```
ACT 1 OPEN — Distributed Systems Expert
Scope: Gates 1–4 + Act 1 Registry Audit + Nil Supersession Log + Scope Verification + ACT 1 CLOSE
```

### GATE 1: Discovery and Triage

```
GATE 1 OPEN
Preconditions:
  [ ] SCOPE DECLARATION COMPLETE present
  [ ] Coverage Accountability Roster committed
Entry confirmed: [yes / no]
```

| # | ID | Failure Class | Confidence Basis | Disposition | Rule Applied | Notes |
|---|---|---|---|---|---|---|
| 1 | FS-01 | | | Include / BARRED / Argued-Impossible | RULE-BARRED-CG or — | |

BARRED: cite RULE-BARRED-CG inline; emit CG-NN.
Argued-Impossible: name DS Primitive by name (CAP theorem constraint, synchrony guarantee,
topology bound). "Topic does not mention X" is not a DS Primitive.

**Gate 1b — BARRED Resolution**

| BARRED ID | Confidence Basis | Resolved? | Resolution Mechanism | New Disposition |
|---|---|---|---|---|

No BARRED entries: `Gate 1b: none.`

```
GATE 1 CLOSE
Exit postconditions:
  [ ] Every candidate has one named disposition
  [ ] Every BARRED entry has CG-NN emitted
  [ ] Every Argued-Impossible cites DS Primitive by name
  [ ] Coverage Accountability Roster counts updated
Gate 1 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 2: Four-Field Scenario Analysis

```
GATE 2 OPEN
Preconditions:
  [ ] Gate 1 STATUS: CLOSED
Entry confirmed: [yes / no]
```

**Anti-split**: Produce the single scenario table below. Do not create separate sub-tables
for Commerce Expert columns and DS Expert columns. Do not insert a horizontal rule, heading,
or section break between rows when column ownership shifts from C-phase to D-phase within a
row.

**Section gate**: Produce all scenario rows before writing the Gap Identification section.

**Column-group gate**: Within each row, complete all C-phase columns (State, Capability)
before writing any D-phase column (Data at Risk, Recovery Path, Severity, Blast Radius).
The C-phase to D-phase transition must be confirmed inline in each row descriptor before
D-phase columns are written.

Use the Row Descriptors below to construct each row. Each descriptor specifies consequence
context, the in-row column-group gate checkpoint, and the advance inhibitor.

---

#### Row Descriptors

**Row 1 — FS-01: [Scenario Name]**

Consequence context (fill before writing): For a concurrent-write scenario — oversell
accumulates if last-write-wins resolves in favor of the later write; double-charge if
payment dedup window is exceeded; duplicate order if merge is naive. For an offline scenario
— stale cart silently overwrites server state on reconnect; user loses changes made during
session without notification.

Chronic if never addressed: oversell count accumulates per-transaction / unbounded / inventory
accuracy metric degrades indefinitely.

**Write this row now.**
C-phase (Commerce Expert): fill State with the exact system configuration when this failure
occurs — name the components involved and their specific states (not "system is degraded").
Fill Capability with the named commerce operations the user can still complete in this state.
**C-phase complete check: do not begin D-phase columns until State and Capability contain
non-placeholder content.**
D-phase (DS Expert): fill Data at Risk with the named data type and the specific consistency
failure mode. Fill Recovery Path with all four stages: Detect (mechanism | TTD target),
Contain (mechanism | TTC target), Recover (mechanism | TTR target), Validate (mechanism |
TTV target) — each step names its actor (client / server / operator / user). Fill Severity
and Blast Radius. Record any rule invocation in Rule Applied.
**Do not advance to Row 2 until this row contains non-placeholder content in every column
including all four Recovery Path stages each with a named mechanism and SLA target.**

---

**Row 2 — FS-02: [Scenario Name]**

Consequence context: [payment idempotency miss → double-charge if payment provider receives
duplicate request; loyalty double-redemption if split-brain resolves both redemption writes
as valid; order state divergence if partial fulfillment failure is not surfaced to user].

Chronic if never addressed: reconciliation backlog grows per-incident / without ceiling /
payment dispute count accumulates.

**Write this row now.**
C-phase (Commerce Expert): fill State and Capability as specified in the Column Contract.
**C-phase complete check: do not begin D-phase columns until C-phase is non-placeholder.**
D-phase (DS Expert): fill Data at Risk, Recovery Path (all four stages with named actors and
SLA targets), Severity, Blast Radius.
**Do not advance to Row 3 until this row contains non-placeholder content in all columns
including all four Recovery Path stages with mechanism and SLA target.**

---

Continue this pattern for all remaining Include scenarios from Gate 1. Every row must have
its own consequence context, column-group gate checkpoint, and advance inhibitor.

Scenario table (single table, all rows):

| # | ID | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius | Rule Applied |
|---|---|---|---|---|---|---|---|---|
| 1 | FS-01 | | | | Detect: [mech\|TTD]; Contain: [mech\|TTC]; Recover: [mech\|TTR]; Validate: [mech\|TTV] | | | |

```
GATE 2 CLOSE
Exit postconditions:
  [ ] Every Include scenario has all four fields with non-trivial content
  [ ] Every row has severity and blast radius labeled
  [ ] Every recovery path has all four stages with named-actor steps and SLA targets
  [ ] All RULE-CR-DCV triggers recorded in Rule Applied
  [ ] Column-group gate checkpoint confirmed for every row
Gate 2 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 3: Gap Identification

```
GATE 3 OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED
Entry confirmed: [yes / no]
```

**OEG — Offline Experience Gaps**

| ID | Scenario Ref | Gap Description | Status-Quo Carrying Cost | Actionable Recommendation |
|---|---|---|---|---|
| OEG-01 | FS-NN | | [rate per session/deploy/transaction \| horizon: unbounded/session-scoped \| user-visible failure] | |

No OEG: `OEG-NIL-1: [scope rationale — specific deployment constraint that forecloses offline experience gaps]`

**DCV — Data Consistency Violations**

| ID | Source | Data Type | Failure Mode | Conflict Resolution Strategy | Adequacy | Status-Quo Carrying Cost | Rule Applied |
|---|---|---|---|---|---|---|---|
| DCV-01 | FS-NN | | | last-write-wins / merge / manual-reconcile / reject-stale / undefined | adequate / inadequate / undefined | [rate \| horizon \| metric] | |

Assign DCV-NN to all RULE-CR-DCV pending entries from Gate 2. Confirm source linkage.
Inadequate or undefined resolution: invoke RULE-CR-DCV; emit DCV-CR-NN with source linkage.
No DCV: `DCV-NIL-1: [scope rationale]`

**MRF — Missing Recovery Flows**

| ID | Scenario Ref | Absent Mechanism | Status-Quo Carrying Cost | Why No Current Path Exists |
|---|---|---|---|---|
| MRF-01 | FS-NN | | [rate \| horizon \| user-visible failure mode] | |

No MRF: `MRF-NIL-1: [scope rationale]`

```
GATE 3 CLOSE
Exit postconditions:
  [ ] All three gap categories present (OEG, DCV, MRF)
  [ ] Every category has at least one named finding or a typed nil with scope rationale
  [ ] Every typed nil has a unique identifier
  [ ] All pending RULE-CR-DCV entries have DCV-NN assignments
  [ ] Conflict resolution verdict present for every eventual-consistency scenario
  [ ] Status-Quo Carrying Cost populated for every named finding (rate + horizon + metric)
Gate 3 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 4: Amendment Pass

```
GATE 4 OPEN
Preconditions:
  [ ] Gate 3 STATUS: CLOSED
Entry confirmed: [yes / no]
```

| AMD ID | Entry ID | Original (summary) | Amended (summary) | Rule Invoked | Gate Re-Opened? |
|---|---|---|---|---|---|
| AMD-01 | | | | RULE-NIL-SUPERSEDE / — | Gate N: AMENDED / no |

No amendments: `Gate 4: no amendments required. No gate re-opens triggered.`

```
GATE 4 CLOSE
Exit postconditions:
  [ ] All recovery paths have minimum two actor-labeled steps
  [ ] Every superseded nil has SUPERSEDED annotation with finding ID
  [ ] Every late DCV finding is in Gate 3: AMENDED with re-close confirmation
Gate 4 STATUS: CLOSED / OPEN — [reason if open]
```

---

### Act 1 Terminal: Post-Analysis Rule Registry Audit

**BYPASS-TRIGGER column**: A RULE-BYPASSED status cell requires a non-empty BYPASS-TRIGGER
entry. An empty BYPASS-TRIGGER cell beside a RULE-BYPASSED status is itself an audit failure.

| Rule ID | Invocations | Citations (gate, entry) | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-CR-DCV | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or `GATE N-bypass: REOPEN — apply RULE-CR-DCV at [gate, entry]`] |
| RULE-BARRED-CG | | | | |
| RULE-NIL-SUPERSEDE | | | | |

If any BYPASS-TRIGGER cell is non-empty — invoke bypass gate-reopening protocol now:

```
GATE N-bypass: REOPENED — [rule ID] — bypass at [gate, entry ID]
```
[Apply rule: emit required output]
```
GATE N-bypass: AMENDED — CLOSED — rule applied at [gate, entry]; Citations += [sub-gate]
```

POST-ANALYSIS REGISTRY AUDIT (ACT 1) COMPLETE: [confirm no RULE-BYPASSED entries remain]

---

### Act 1 Terminal: Nil Supersession Log

| Nil ID | Gap Type | State | Superseded By | Gate |
|---|---|---|---|---|

No supersessions: `No supersessions in this run.`

---

### Act 1 Terminal: Scope Verification

| Declared Operation | Covered | Gap Finding |
|---|---|---|
| [operation] | Yes / No | SV-GAP-NN / — |

SCOPE VERIFICATION COMPLETE

---

```
ACT 1 CLOSE (sign-off)
(1) All gates within Act 1 CLOSED:
    Gate 1:    [CLOSED / OPEN — reason]
    Gate 1b:   [CLOSED / N/A — no BARRED entries]
    Gate 2:    [CLOSED / OPEN — reason]
    Gate 3:    [CLOSED / OPEN — reason]
    Gate 4:    [CLOSED / OPEN — reason]
    GATE N-bypass blocks (if triggered): [CLOSED / none triggered]
    Act 1 Registry Audit: [CLOSED / OPEN — reason]
(2) Act 1 scope exhausted: [yes / list any unresolved items]
(3) No RULE-BYPASSED conditions remain unresolved within Act 1: [yes / exception detail]
ACT 1 STATUS: CLOSED / OPEN
```

---

```
ACT 2 OPEN — Commerce Domain Validator
Entry condition: ACT 1 STATUS: CLOSED
Scope: Gate 5 + Act 2 Registry Audit + Inertia Synthesis + ACT 2 CLOSE
```

### GATE 5: Commerce Domain Validation

```
GATE 5 OPEN
Preconditions:
  [ ] ACT 1 STATUS: CLOSED
Entry confirmed: [yes / no]
```

| Scenario ID | Commerce Operation Named? | Amended Operation (RULE-COMMERCE-ANCHOR) | CV Finding Issued |
|---|---|---|---|
| FS-01 | Yes / No | | — / CV-DCV-01 / CV-OEG-01 / CV-MRF-01 |

Commerce-domain finding targets (check each):
- Inventory oversell under partition: [present / absent — rationale]
- Payment idempotency window expiry: [present / absent — rationale]
- Loyalty point double-redemption under split-brain: [present / absent — rationale]
- Order state divergence under partial fulfillment failure: [present / absent — rationale]

```
GATE 5 CLOSE
Exit postconditions:
  [ ] Every Include scenario anchored to a named commerce operation
  [ ] All RULE-COMMERCE-ANCHOR invocations recorded
  [ ] All four commerce-domain targets checked (present or rationale)
Gate 5 STATUS: CLOSED / OPEN — [reason if open]
```

---

### Act 2 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-COMMERCE-ANCHOR | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or `GATE 5-bypass: REOPEN now`] |

If BYPASS-TRIGGER non-empty — Commerce Validator resolves:

```
GATE 5-bypass: REOPENED — RULE-COMMERCE-ANCHOR — bypass at Gate 5, [scenario ID]
```
[Apply rule: name the commerce operation; record amendment]
```
GATE 5-bypass: AMENDED — CLOSED; Audit update: Status → INVOKED
```

POST-ANALYSIS REGISTRY AUDIT (ACT 2) COMPLETE

---

### Inertia Synthesis — What Does Doing Nothing Cost?

**Per-finding carrying cost** (from Gate 3 Status-Quo Carrying Cost column):
For each named gap (OEG-NN, DCV-NN, MRF-NN): state the failure mode, the rate (per
session / deploy / transaction), the horizon (unbounded / session-scoped / compound growth),
and the named metric that accumulates. One entry per finding.

**Overall synthesis**:
Urgency: HIGH / MEDIUM / LOW
Highest-risk finding: [gap ID] — [carrying cost from Gate 3]
Status-quo option: [what "do nothing" looks like for `{topic}` specifically — not generic]
Intervention recommendation: [owner + threshold + consequence of missing threshold]

```
ACT 2 CLOSE (sign-off)
(1) All gates within Act 2 CLOSED:
    Gate 5: [CLOSED / OPEN — reason]
    GATE 5-bypass blocks (if triggered): [CLOSED / none triggered]
    Act 2 Registry Audit: [CLOSED / OPEN — reason]
(2) Act 2 scope exhausted: [yes — all scenarios commerce-anchored; all CV targets checked;
    inertia synthesis complete]
(3) No RULE-BYPASSED conditions remain unresolved within Act 2: [yes / exception detail]
ACT 2 STATUS: CLOSED / OPEN
```

ANALYSIS COMPLETE (declared only when ACT 1 STATUS: CLOSED AND ACT 2 STATUS: CLOSED)

---

---

## V-02

**Variation axis**: Output format — table-dominant throughout; every gate produces a
Markdown table as its primary artifact. The Column Contract adds a Trigger Condition column
whose Fill Requirement specifies both a threshold expression (quantified condition that
activates the scenario) and a detection signal (observable mechanism confirming the threshold
is crossed). Both components are independently verifiable by column scan.

**Hypothesis**: When threshold expression and detection signal are discrete column cells
rather than qualifiers embedded in scenario prose, they become auditable without reading the
full narrative. A prose-described trigger can absorb vague language ("when the service is
unavailable"); a columnar threshold expression must be quantified. The Column Contract's
Fill Requirement enforces the two-component structure before any row is constructed. Table
format also makes the BYPASS-TRIGGER column in the registry audit independently scannable,
preserving the C-32 bypass-scan property on a separate audit dimension.

---

You are running the **flow-resilience** skill for `{topic}`.

Output format rule: every gate produces a Markdown table as its primary artifact. Prose is
permitted only for impossibility arguments in the Coverage Accountability Roster, nil scope
rationale, and inline rule invocation annotations. Gate status blocks use the structured
format defined below.

---

### RULE REGISTRY

| Rule ID | Trigger Condition | Action Required | Bypass Owner |
|---|---|---|---|
| RULE-CR-DCV | Concurrent state modification by multiple actors without coordination | Emit DCV-NN in Gate 3; cite inline | DS Expert (Act 1) |
| RULE-BARRED-CG | Discovery entry confidence basis unresolvable | Mark BARRED; emit CG-NN | DS Expert (Act 1) |
| RULE-NIL-SUPERSEDE | Downstream finding in category that held a typed nil | Annotate nil SUPERSEDED | DS Expert (Act 1) |
| RULE-COMMERCE-ANCHOR | Include scenario with no named commerce operation | Amend to name operation | Commerce Validator (Act 2) |

---

### BYPASS GATE-REOPENING PROTOCOL

**Authority**: DS Expert for Act 1 rules; Commerce Validator for Act 2 rules. Cross-act
invocation not permitted.

When any rule shows RULE-BYPASSED:

1. Bypass Owner emits: `GATE N-bypass: REOPENED — [rule ID] — bypass at [gate, entry ID]`
2. Bypass Owner applies the rule and produces required output.
3. Bypass Owner emits: `GATE N-bypass: AMENDED — CLOSED`
4. Bypass Owner updates audit row: Status → INVOKED; BYPASS-TRIGGER → RESOLVED — [sub-gate];
   Citations += sub-gate reference.

**COMPLETE may not be declared** while any RULE-BYPASSED entry remains unresolved.

---

### ANTI-OMISSION ARCHITECTURE

| Level | Anti-Omission Mechanism | Omission Risk Targeted | Mechanism Location |
|---|---|---|---|
| Table | Unified row index + anti-split instruction | Row fragmentation across table boundaries | `#` column; anti-split instruction in Gate 2 |
| Section | Phase gate — all rows before Gap Identification | Premature section advance | Section gate in Gate 2 |
| Slot | In-row bold imperative: **"Write this row now."** / **"Do not advance to Row N+1 until..."** | Row omission under token pressure | Row Descriptors (below) |
| Column | Column ownership per header (defined in Column Contract, below) | Column omission under ownership confusion | Column Contract (below) |

**Anti-split instruction**: Do not create separate sub-tables for Commerce Expert columns and
DS Expert columns. Do not insert a horizontal rule, heading, or section break between rows
when column ownership shifts within a row.

---

### COLUMN CONTRACT

| Column Name | Owner | Fill Requirement |
|---|---|---|
| `#` | Shared | Sequential integer; no gaps; no reuse |
| `ID` | Shared | FS-NN format; unique per scenario |
| `Trigger Condition` | DS Expert | **Two required components**: (1) threshold expression — a quantified condition that activates this scenario (e.g., "inventory count < safety-stock threshold", "payment API latency exceeds 500ms p99"); (2) detection signal — the observable mechanism by which the system identifies the threshold being crossed (e.g., "inventory-service health probe returns degraded", "payment-provider timeout counter increments"). A qualitative description ("when the service is unavailable") without a threshold expression fails this requirement. |
| `State` | Commerce Expert | Specific system configuration when failure occurs; name components and states; not "degraded" |
| `Capability` | Commerce Expert | Named commerce operations the user can still complete |
| `Data at Risk` | DS Expert | Named data type + consistency failure mode |
| `Recovery Path` | DS Expert | Four stages: Detect (mechanism \| TTD target); Contain (mechanism \| TTC target); Recover (mechanism \| TTR target); Validate (mechanism \| TTV target). Each step names actor. |
| `Severity` | DS Expert | `degraded` / `impaired` / `down` |
| `Blast Radius` | DS Expert | Fraction or named segment |
| `Rule Applied` | DS Expert | Rule ID or `—` |

---

### Pre-Analysis: Commerce Operation Scope Declaration

| Field | Entry |
|---|---|
| Operations in scope | [minimum four: checkout / inventory reservation / payment processing / order fulfillment / cart state / loyalty redemption / return-refund] |
| Operations excluded | [list with reason or "none"] |
| SCOPE DECLARATION | COMPLETE |

### Pre-Analysis: Coverage Accountability Roster

| Degradation Class | Committed Minimum | DS Primitive for Impossibility |
|---|---|---|
| Network partition / offline | 2 | [required if slot unfillable] |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

---

```
ACT 1 OPEN — Distributed Systems Expert
Scope: Gates 1–4 + Act 1 Registry Audit + Nil Supersession Log + Scope Verification + ACT 1 CLOSE
```

### GATE 1: Discovery and Triage

| # | ID | Failure Class | Confidence Basis | Disposition | Rule Applied | Notes |
|---|---|---|---|---|---|---|
| 1 | FS-01 | Network partition / offline \| Partial service failure \| Eventual consistency | | Include / BARRED / Argued-Impossible | RULE-BARRED-CG or — | |

BARRED entries: cite RULE-BARRED-CG; emit CG-NN.
Argued-Impossible: name DS Primitive.

**Gate 1b — BARRED Resolution**

| BARRED ID | Confidence Basis | Resolved? | Resolution Mechanism | New Disposition |
|---|---|---|---|---|

No BARRED entries: `Gate 1b: none.`

| Gate 1 Status | Exit Postcondition | Met? |
|---|---|---|
| CLOSED / OPEN | Every candidate has one named disposition | |
| | Every BARRED entry has CG-NN emitted | |
| | Every Argued-Impossible cites DS Primitive by name | |

---

### GATE 2: Four-Field Scenario Analysis

**Anti-split**: Single scenario table. Do not split by scenario class. Do not insert
horizontal rules or section breaks between rows when Trigger Condition and State columns
transition between owners within a row.

**Section gate**: Produce all scenario rows before writing the Gap Identification section.

#### Row Descriptors

**Row 1 — FS-01: [Scenario Name]**

Consequence context: [acute consequences per resolution branch — oversell / double-charge /
duplicate fulfillment depending on how concurrent writes resolve]. Chronic if never addressed:
[rate per transaction] / [horizon: unbounded] / [metric: e.g., inventory-accuracy error count
accumulates].

**Write this row now.**
Fill Trigger Condition: provide (1) a threshold expression naming a quantified condition that
activates this scenario and (2) a detection signal naming the observable mechanism confirming
the threshold is crossed. Example: "payment API latency > 500ms p99 / payment-provider timeout
counter increments past alert threshold." Both components are required; a qualitative
description alone fails.
Fill State, Capability, Data at Risk, Recovery Path (all four stages with SLA targets),
Severity, Blast Radius, Rule Applied per Column Contract.
**Do not advance to Row 2 until this row contains non-placeholder content in every column
including both components of Trigger Condition and all four Recovery Path stages each with
a named mechanism and SLA target.**

---

**Row 2 — FS-02: [Scenario Name]**

Consequence context: [payment idempotency miss → double-charge; loyalty double-redemption;
order state divergence under partial fulfillment]. Chronic: reconciliation backlog per-incident
/ without ceiling / dispute-count metric accumulates.

**Write this row now.**
Fill Trigger Condition with threshold expression + detection signal per Column Contract.
Fill remaining columns per Column Contract.
**Do not advance to Row 3 until this row is complete including both Trigger Condition
components and all four Recovery Path stages.**

---

Continue this pattern for all remaining Include scenarios. Scenario table:

| # | ID | Trigger Condition | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius | Rule Applied |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FS-01 | [threshold expression] / [detection signal] | | | | Detect: [mech\|TTD]; Contain: [mech\|TTC]; Recover: [mech\|TTR]; Validate: [mech\|TTV] | | | |

| Gate 2 Status | Exit Postcondition | Met? |
|---|---|---|
| CLOSED / OPEN | Every Include scenario has all four fields with non-trivial content | |
| | Every row has Trigger Condition with threshold expression + detection signal | |
| | Every row has severity, blast radius, all four recovery stages with SLA targets | |
| | All RULE-CR-DCV triggers recorded | |

---

### GATE 3: Gap Identification

**OEG — Offline Experience Gaps**

| ID | Scenario Ref | Gap Description | Status-Quo Carrying Cost | Actionable Recommendation |
|---|---|---|---|---|
| OEG-01 | FS-NN | | [rate \| horizon \| user-visible failure] | |

No OEG: `OEG-NIL-1: [scope rationale]`

**DCV — Data Consistency Violations**

| ID | Source | Data Type | Failure Mode | Conflict Resolution | Adequacy | Status-Quo Carrying Cost | Rule Applied |
|---|---|---|---|---|---|---|---|
| DCV-01 | FS-NN | | | last-write-wins / merge / manual-reconcile / reject-stale / undefined | adequate / inadequate / undefined | [rate per transaction \| horizon \| metric] | |

No DCV: `DCV-NIL-1: [scope rationale]`

**MRF — Missing Recovery Flows**

| ID | Scenario Ref | Absent Mechanism | Status-Quo Carrying Cost | Why No Current Path Exists |
|---|---|---|---|---|
| MRF-01 | FS-NN | | [rate \| horizon \| failure mode] | |

No MRF: `MRF-NIL-1: [scope rationale]`

| Gate 3 Status | Exit Postcondition | Met? |
|---|---|---|
| CLOSED / OPEN | All three gap categories present | |
| | Every finding has Status-Quo Carrying Cost (rate + horizon + metric) | |
| | All RULE-CR-DCV entries assigned DCV-NN | |

---

### GATE 4: Amendment Pass

| AMD ID | Entry ID | Original (summary) | Amended (summary) | Rule Invoked | Gate Re-Opened? |
|---|---|---|---|---|---|

No amendments: `Gate 4: no amendments. No gate re-opens triggered.`

| Gate 4 Status | Exit Postcondition | Met? |
|---|---|---|
| CLOSED / OPEN | All recovery paths have minimum two actor-labeled steps | |
| | Every superseded nil has SUPERSEDED annotation | |

---

### Act 1 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations (gate, entry) | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-CR-DCV | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or `GATE N-bypass: REOPEN — apply RULE-CR-DCV at [gate, entry]`] |
| RULE-BARRED-CG | | | | |
| RULE-NIL-SUPERSEDE | | | | |

BYPASS-TRIGGER non-empty → invoke bypass gate-reopening protocol before ACT 1 CLOSE.

POST-ANALYSIS REGISTRY AUDIT (ACT 1) COMPLETE: [confirm no RULE-BYPASSED entries remain]

---

### Act 1 Terminal: Nil Supersession Log

| Nil ID | Gap Type | State | Superseded By | Gate |
|---|---|---|---|---|

No supersessions: `No supersessions in this run.`

### Act 1 Terminal: Scope Verification

| Declared Operation | Covered | Gap Finding |
|---|---|---|
| [operation] | Yes / No | SV-GAP-NN / — |

```
ACT 1 CLOSE (sign-off)
(1) All gates within Act 1 CLOSED:
    Gate 1: [CLOSED / OPEN — reason]; Gate 1b: [CLOSED / N/A]
    Gate 2: [CLOSED / OPEN — reason]; Gate 3: [CLOSED / OPEN — reason]
    Gate 4: [CLOSED / OPEN — reason]
    GATE N-bypass blocks: [CLOSED / none triggered]
    Act 1 Registry Audit: [CLOSED / OPEN — reason]
(2) Act 1 scope exhausted: [yes / list unresolved items]
(3) No RULE-BYPASSED conditions remain unresolved within Act 1: [yes / exception detail]
ACT 1 STATUS: CLOSED / OPEN
```

---

```
ACT 2 OPEN — Commerce Domain Validator
Entry condition: ACT 1 STATUS: CLOSED
```

### GATE 5: Commerce Domain Validation

| Scenario ID | Commerce Operation Named? | Amended Operation | CV Finding Issued |
|---|---|---|---|
| FS-01 | Yes / No | | — / CV-DCV-01 / CV-OEG-01 / CV-MRF-01 |

Commerce-domain targets: inventory oversell / payment idempotency / loyalty double-redemption
/ order state divergence — each: [present / absent — rationale].

| Gate 5 Status | Exit Postcondition | Met? |
|---|---|---|
| CLOSED / OPEN | Every scenario anchored to named commerce operation | |
| | All four commerce-domain targets checked | |

### Act 2 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-COMMERCE-ANCHOR | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |

POST-ANALYSIS REGISTRY AUDIT (ACT 2) COMPLETE

### Inertia Synthesis

**Per-finding carrying cost**: For each named gap — failure mode, rate, horizon, metric.

**Overall synthesis**:
Urgency: HIGH / MEDIUM / LOW
Highest-risk finding: [gap ID] — [carrying cost from Gate 3]
Status-quo option: [specific to `{topic}`]
Intervention recommendation: [owner + threshold + consequence of missing threshold]

```
ACT 2 CLOSE (sign-off)
(1) All gates within Act 2 CLOSED: Gate 5 / bypass blocks / Registry Audit
(2) Act 2 scope exhausted: [yes]
(3) No RULE-BYPASSED conditions remain unresolved: [yes / exception]
ACT 2 STATUS: CLOSED / OPEN
```

ANALYSIS COMPLETE (declared only when ACT 1 STATUS: CLOSED AND ACT 2 STATUS: CLOSED)

---

---

## V-03

**Variation axis**: Lifecycle emphasis — each of the four Recovery Path stages (Detect,
Contain, Recover, Validate) requires three components in the Column Contract specification:
mechanism (action taken), SLA target (TTD/TTC/TTR/TTV), and Verification Signal (VS — a
named observable artifact confirming stage completion). The VS makes each stage independently
falsifiable: the stage is not done when the SLA elapses — it is done when the named observable
artifact appears.

**Hypothesis**: SLA targets record duration commitment but cannot confirm stage outcome. A
stage that "should take < 5 minutes to detect" can be logged as complete after 5 minutes
whether or not detection actually occurred. A named VS (e.g., "inventory-service heartbeat
returns 200", "payment provider ACK logged to audit trail") creates a falsifiable completion
condition that is independent of elapsed time. Lifecycle emphasis — specifying all four stages
as structured lifecycle blocks in the column spec — makes VS omission visible as a structural
gap rather than an implicit expectation.

---

You are running the **flow-resilience** skill for `{topic}`.

This analysis runs in two sequential acts with distinct roles and independent closure.
Do not blend the acts.

---

### RULE REGISTRY

| Rule ID | Trigger Condition | Action Required | Bypass Owner |
|---|---|---|---|
| RULE-CR-DCV | Concurrent state modification without coordination mechanism | Emit DCV-NN in Gate 3 | DS Expert (Act 1) |
| RULE-BARRED-CG | Discovery entry confidence basis unresolvable | Mark BARRED; emit CG-NN | DS Expert (Act 1) |
| RULE-NIL-SUPERSEDE | Downstream finding supersedes a typed nil | Annotate nil SUPERSEDED | DS Expert (Act 1) |
| RULE-COMMERCE-ANCHOR | Include scenario has no named commerce operation | Amend to name operation | Commerce Validator (Act 2) |

---

### BYPASS GATE-REOPENING PROTOCOL

**Authority**: DS Expert for Act 1 rules; Commerce Validator for Act 2 rules.

When any rule shows RULE-BYPASSED:

1. Bypass Owner emits: `GATE N-bypass: REOPENED — [rule ID] — bypass at [gate, entry ID]`
2. Bypass Owner applies the rule and produces required output.
3. Bypass Owner emits: `GATE N-bypass: AMENDED — CLOSED`
4. Bypass Owner updates audit row: Status → INVOKED; BYPASS-TRIGGER → RESOLVED; Citations +=
   sub-gate reference.

**COMPLETE may not be declared** while any RULE-BYPASSED entry remains unresolved.

---

### ANTI-OMISSION ARCHITECTURE

| Level | Anti-Omission Mechanism | Omission Risk Targeted | Mechanism Location |
|---|---|---|---|
| Table | Unified row index + anti-split instruction | Row fragmentation | `#` column; anti-split instruction in Gate 2 |
| Section | Phase gate — all rows before Gap Identification | Premature section advance | Section gate in Gate 2 |
| Slot | In-row bold imperative: **"Write this row now."** / **"Do not advance to Row N+1 until..."** | Row omission under token pressure | Row Descriptors (below) |
| Column | Column ownership per header (defined in Column Contract, below) | Column omission under ownership confusion | Column Contract (below) |

**Anti-split instruction**: Do not create separate sub-tables for Commerce Expert columns and
DS Expert columns. Do not insert a horizontal rule, heading, or section break between rows
when column ownership shifts within a row.

---

### COLUMN CONTRACT

| Column Name | Owner | Fill Requirement |
|---|---|---|
| `#` | Shared | Sequential integer; no gaps |
| `ID` | Shared | FS-NN format |
| `State` | Commerce Expert | Specific system configuration; name components and states |
| `Capability` | Commerce Expert | Named commerce operations user can still complete |
| `Data at Risk` | DS Expert | Named data type + consistency failure mode |
| `Recovery Path` | DS Expert | **Four stages, each with three components**: (1) mechanism — the action taken to advance the stage, naming the actor (client / server / operator / user); (2) SLA target — Detect→TTD, Contain→TTC, Recover→TTR, Validate→TTV; (3) Verification Signal (VS) — a **named observable artifact** confirming stage completion (e.g., "inventory-service heartbeat returns HTTP 200", "payment provider ACK logged to audit trail", "dual-write conflict counter resets to 0 for 60s"). The VS must be a system state, log entry, metric value, or API response code — not a re-statement of the mechanism. Format: `Detect: [mechanism] \| TTD: [target] \| VS: [named artifact]; Contain: ...` |
| `Severity` | DS Expert | `degraded` / `impaired` / `down` |
| `Blast Radius` | DS Expert | Fraction or named segment |
| `Rule Applied` | DS Expert | Rule ID or `—` |

**VS validity rule**: A VS that reads "confirmed" or "verified" or restates the mechanism
("detection occurred") does not satisfy this requirement. The VS must be observable and
named independently of the mechanism.

---

### Pre-Analysis: Commerce Operation Scope Declaration

Declare before Gate 1. Minimum four operations from: checkout, inventory reservation,
payment processing, order fulfillment, cart state, loyalty redemption, return/refund.

```
SCOPE DECLARATION
Operations in scope: [list]
Exclusions (with reason): [list or "none"]
SCOPE DECLARATION COMPLETE
```

### Pre-Analysis: Coverage Accountability Roster

| Degradation Class | Committed Minimum | DS Primitive for Impossibility |
|---|---|---|
| Network partition / offline | 2 | |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

---

```
ACT 1 OPEN — Distributed Systems Expert
Scope: Gates 1–4 + Act 1 Registry Audit + Nil Supersession Log + Scope Verification + ACT 1 CLOSE
```

### GATE 1: Discovery and Triage

```
GATE 1 OPEN
Preconditions:
  [ ] SCOPE DECLARATION COMPLETE present
  [ ] Coverage Accountability Roster committed
Entry confirmed: [yes / no]
```

| # | ID | Failure Class | Confidence Basis | Disposition | Rule Applied | Notes |
|---|---|---|---|---|---|---|
| 1 | FS-01 | | | Include / BARRED / Argued-Impossible | | |

BARRED: cite RULE-BARRED-CG; emit CG-NN. Argued-Impossible: name DS Primitive.

**Gate 1b — BARRED Resolution**

| BARRED ID | Resolved? | Resolution Mechanism | New Disposition |
|---|---|---|---|

No BARRED: `Gate 1b: none.`

```
GATE 1 CLOSE
Exit postconditions: every candidate disposed / every BARRED has CG-NN / every Argued-Impossible
cites DS Primitive.
Gate 1 STATUS: CLOSED / OPEN — [reason]
```

---

### GATE 2: Four-Field Scenario Analysis

```
GATE 2 OPEN
Preconditions:
  [ ] Gate 1 STATUS: CLOSED
Entry confirmed: [yes / no]
```

**Anti-split**: Single table. Do not create separate sub-tables by ownership. Do not insert
horizontal rules or section breaks between rows.

**Section gate**: Produce all scenario rows before writing the Gap Identification section.

#### Row Descriptors

**Row 1 — FS-01: [Scenario Name]**

Consequence context: [per-resolution-branch consequences — oversell if last-write-wins;
double-charge if payment dedup fails; duplicate fulfillment if merge is naive].
Chronic if never addressed: [accumulation rate per transaction] / [horizon: unbounded] /
[named metric: e.g., inventory-accuracy violations accumulate indefinitely].

**Write this row now.**
Fill State with the exact system configuration when this failure occurs — name components
and their specific states. Fill Capability with named commerce operations still accessible.
Fill Data at Risk with named data type and consistency failure mode.
Fill Recovery Path with all four stages, each containing mechanism + SLA target + VS:
  - Detect: [what triggers detection, who detects, how] | TTD: [target] | VS: [named artifact
    confirming detection is complete — e.g., "alert fires on payment-service error rate metric"]
  - Contain: [action to limit blast radius] | TTC: [target] | VS: [named artifact]
  - Recover: [restoration action] | TTR: [target] | VS: [named artifact]
  - Validate: [confirmation action] | TTV: [target] | VS: [named artifact]
Fill Severity and Blast Radius.
**Do not advance to Row 2 until this row contains non-placeholder content in every column
including all four Recovery Path stages each with mechanism, SLA target, and a named
Verification Signal.**

---

**Row 2 — FS-02: [Scenario Name]**

Consequence context: [payment idempotency window expiry → double-charge; order state
divergence → duplicate fulfillment or lost order]. Chronic: reconciliation backlog per-incident
/ without ceiling / dispute-event count accumulates.

**Write this row now.**
Fill State, Capability, Data at Risk per Column Contract.
Fill Recovery Path: Detect (mechanism | TTD | VS); Contain (mechanism | TTC | VS);
Recover (mechanism | TTR | VS); Validate (mechanism | TTV | VS). Each VS must be a named
observable artifact, not a re-statement of the mechanism.
**Do not advance to Row 3 until all four Recovery Path stages contain mechanism, SLA target,
and a named VS that is observable and distinct from the mechanism.**

---

Continue for all remaining Include scenarios. Scenario table:

| # | ID | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius | Rule Applied |
|---|---|---|---|---|---|---|---|---|
| 1 | FS-01 | | | | Detect: [mech\|TTD\|VS]; Contain: [mech\|TTC\|VS]; Recover: [mech\|TTR\|VS]; Validate: [mech\|TTV\|VS] | | | |

```
GATE 2 CLOSE
Exit postconditions:
  [ ] Every Include scenario has all four fields with non-trivial content
  [ ] Every severity and blast radius labeled
  [ ] Every Recovery Path has all four stages with mechanism, SLA target, and named VS
  [ ] Every VS is observable and distinct from its mechanism
  [ ] All RULE-CR-DCV triggers recorded
Gate 2 STATUS: CLOSED / OPEN — [reason]
```

---

### GATE 3: Gap Identification

```
GATE 3 OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED
Entry confirmed: [yes / no]
```

**OEG — Offline Experience Gaps**

| ID | Scenario Ref | Gap Description | Status-Quo Carrying Cost | Actionable Recommendation |
|---|---|---|---|---|
| OEG-01 | FS-NN | | [rate \| horizon \| user-visible failure] | |

No OEG: `OEG-NIL-1: [scope rationale]`

**DCV — Data Consistency Violations**

| ID | Source | Data Type | Failure Mode | Conflict Resolution | Adequacy | Status-Quo Carrying Cost | Rule Applied |
|---|---|---|---|---|---|---|---|
| DCV-01 | FS-NN | | | last-write-wins / merge / manual-reconcile / reject-stale / undefined | adequate / inadequate / undefined | [rate per transaction \| horizon \| metric accumulates] | |

No DCV: `DCV-NIL-1: [scope rationale]`

**MRF — Missing Recovery Flows**

| ID | Scenario Ref | Absent Mechanism | Status-Quo Carrying Cost | Why No Current Path Exists |
|---|---|---|---|---|
| MRF-01 | FS-NN | | [rate \| horizon \| failure mode] | |

No MRF: `MRF-NIL-1: [scope rationale]`

```
GATE 3 CLOSE
Exit postconditions:
  [ ] All three gap categories present
  [ ] Every finding has Status-Quo Carrying Cost (rate + horizon + metric)
  [ ] All RULE-CR-DCV entries have DCV-NN assignments
  [ ] Conflict resolution verdict present for every eventual-consistency scenario
Gate 3 STATUS: CLOSED / OPEN — [reason]
```

---

### GATE 4: Amendment Pass

```
GATE 4 OPEN — Gate 3 STATUS: CLOSED
```

| AMD ID | Entry ID | Original (summary) | Amended (summary) | Rule Invoked | Gate Re-Opened? |
|---|---|---|---|---|---|

No amendments: `Gate 4: no amendments. No gate re-opens triggered.`

```
GATE 4 CLOSE
Gate 4 STATUS: CLOSED / OPEN
```

---

### Act 1 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations (gate, entry) | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-CR-DCV | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | |
| RULE-BARRED-CG | | | | |
| RULE-NIL-SUPERSEDE | | | | |

BYPASS-TRIGGER non-empty → invoke bypass gate-reopening protocol before ACT 1 CLOSE.

POST-ANALYSIS REGISTRY AUDIT (ACT 1) COMPLETE

### Act 1 Terminal: Nil Supersession Log

| Nil ID | Gap Type | State | Superseded By | Gate |
|---|---|---|---|---|

### Act 1 Terminal: Scope Verification

| Declared Operation | Covered | Gap Finding |
|---|---|---|

```
ACT 1 CLOSE (sign-off)
(1) All gates within Act 1 CLOSED: Gate 1 / Gate 1b / Gate 2 / Gate 3 / Gate 4 /
    GATE N-bypass blocks / Act 1 Registry Audit
(2) Act 1 scope exhausted: [yes / unresolved items]
(3) No RULE-BYPASSED conditions remain unresolved within Act 1: [yes / exception]
ACT 1 STATUS: CLOSED / OPEN
```

---

```
ACT 2 OPEN — Commerce Domain Validator
Entry condition: ACT 1 STATUS: CLOSED
```

### GATE 5: Commerce Domain Validation

| Scenario ID | Commerce Operation Named? | Amended Operation | CV Finding Issued |
|---|---|---|---|
| FS-01 | Yes / No | | — / CV-DCV-01 / CV-OEG-01 / CV-MRF-01 |

Commerce-domain targets: inventory oversell / payment idempotency / loyalty double-redemption
/ order state divergence — each: [present / absent — rationale].

```
GATE 5 CLOSE — Gate 5 STATUS: CLOSED / OPEN
```

### Act 2 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-COMMERCE-ANCHOR | | | | |

POST-ANALYSIS REGISTRY AUDIT (ACT 2) COMPLETE

### Inertia Synthesis

**Per-finding carrying cost**: For each named gap — failure mode / rate / horizon / named metric.

**Overall synthesis**:
Urgency: HIGH / MEDIUM / LOW
Highest-risk finding: [gap ID] — [carrying cost]
Status-quo option: [specific to `{topic}`, not generic]
Intervention recommendation: [owner + threshold + consequence of missing threshold]

```
ACT 2 CLOSE (sign-off)
(1) All gates: Gate 5 / bypass blocks / Registry Audit — [CLOSED / reason]
(2) Act 2 scope exhausted: [yes]
(3) No RULE-BYPASSED conditions remain unresolved: [yes / exception]
ACT 2 STATUS: CLOSED / OPEN
```

ANALYSIS COMPLETE (declared only when ACT 1 STATUS: CLOSED AND ACT 2 STATUS: CLOSED)

---

---

## V-04

**Variation axis**: Combination — Role sequence (C-phase / D-phase intra-row column-group
gate, C-32) + lifecycle emphasis (Verification Signal per recovery stage, C-34).

**Hypothesis**: The column-group gate enforces that Commerce Expert's C-phase columns (State,
Capability) are complete within each row before DS Expert's D-phase columns (Data at Risk,
Recovery Path, Severity, Blast Radius) begin. The VS requirement makes each of the four
recovery stages independently falsifiable at completion time. The combination ensures the
row is structurally sequenced (C-phase before D-phase, C-32) and that the highest-complexity
D-phase column — Recovery Path — carries an observable completion artifact per stage (C-34).
Neither mechanism duplicates the other: column-group ordering governs sequence within the
row; VS governs completeness of stage content within the Recovery Path column.

---

You are running the **flow-resilience** skill for `{topic}`.

This analysis runs in two sequential acts. Act 1: Distributed Systems Expert. Act 2:
Commerce Domain Validator. Each act closes with a formal sign-off. Do not blend the acts.

---

### RULE REGISTRY

| Rule ID | Trigger Condition | Action Required | Bypass Owner |
|---|---|---|---|
| RULE-CR-DCV | Concurrent state modification without coordination | Emit DCV-NN in Gate 3 | DS Expert (Act 1) |
| RULE-BARRED-CG | Discovery entry confidence basis unresolvable | Mark BARRED; emit CG-NN | DS Expert (Act 1) |
| RULE-NIL-SUPERSEDE | Downstream finding supersedes a typed nil | Annotate nil SUPERSEDED | DS Expert (Act 1) |
| RULE-COMMERCE-ANCHOR | Include scenario has no named commerce operation | Amend to name operation | Commerce Validator (Act 2) |

---

### BYPASS GATE-REOPENING PROTOCOL

**Authority**: DS Expert for Act 1 rules; Commerce Validator for Act 2 rules. Cross-act
invocation not permitted.

When any rule shows RULE-BYPASSED:

1. Bypass Owner emits: `GATE N-bypass: REOPENED — [rule ID] — bypass at [gate, entry ID]`
2. Bypass Owner applies the rule: produces required output (DCV-NN, CG-NN, SUPERSEDED
   annotation, or commerce anchor amendment).
3. Bypass Owner emits: `GATE N-bypass: AMENDED — CLOSED`
4. Bypass Owner updates audit row: Status → INVOKED; BYPASS-TRIGGER → RESOLVED — [sub-gate];
   Citations += sub-gate reference.

**COMPLETE may not be declared** while any RULE-BYPASSED entry remains unresolved.

---

### ANTI-OMISSION ARCHITECTURE

Five-level stack. Each level targets a distinct omission risk. No two mechanisms conflict
or duplicate each other.

| Level | Anti-Omission Mechanism | Omission Risk Targeted | Mechanism Location |
|---|---|---|---|
| Table | Unified row index (`#`) + anti-split instruction | Row fragmentation across ownership transitions | `#` column; anti-split instruction in Gate 2 |
| Section | Phase gate — all rows before Gap Identification | Premature section advance | Section gate in Gate 2 |
| Slot | In-row bold imperative: **"Write this row now."** / **"Do not advance to Row N+1 until..."** | Row omission under token pressure | Row Descriptors (below) |
| Column-Group | Intra-row ownership phase gate: C-phase columns (State, Capability) complete before D-phase columns (Data at Risk, Recovery Path, Severity, Blast Radius) begin within the same row | Mid-row D-phase omission when ownership shifts | Row Descriptors: Column-Group Gate (below) |
| Column | Column ownership per header (defined in Column Contract, below) | Individual column omission | Column Contract (below) |

**Anti-split instruction**: Do not create separate sub-tables for Commerce Expert columns
and DS Expert columns. Do not insert a horizontal rule, heading, or section break between
rows when column ownership shifts from C-phase to D-phase within a row.

---

### COLUMN CONTRACT

| Column Name | Owner | Phase | Fill Requirement |
|---|---|---|---|
| `#` | Shared | — | Sequential integer; no gaps |
| `ID` | Shared | — | FS-NN format |
| `State` | Commerce Expert | C-phase | Specific system configuration; name components and states; not "degraded" |
| `Capability` | Commerce Expert | C-phase | Named commerce operations user can still complete |
| `Data at Risk` | DS Expert | D-phase | Named data type + consistency failure mode |
| `Recovery Path` | DS Expert | D-phase | **Four stages, each with three components**: mechanism (actor-labeled action advancing the stage) \| SLA target (Detect→TTD, Contain→TTC, Recover→TTR, Validate→TTV) \| Verification Signal (VS — named observable artifact confirming stage completion: system state, log entry, metric value, or API response code). Format: `Detect: [mech] \| TTD: [target] \| VS: [artifact]; Contain: [mech] \| TTC: [target] \| VS: [artifact]; Recover: [mech] \| TTR: [target] \| VS: [artifact]; Validate: [mech] \| TTV: [target] \| VS: [artifact]`. A VS that restates the mechanism or uses generic language ("confirmed", "verified") fails. |
| `Severity` | DS Expert | D-phase | `degraded` / `impaired` / `down` |
| `Blast Radius` | DS Expert | D-phase | Fraction or named segment |
| `Rule Applied` | DS Expert | D-phase | Rule ID or `—` |

---

### Pre-Analysis: Commerce Operation Scope Declaration

Declare before Gate 1. Minimum four operations from: checkout, inventory reservation,
payment processing, order fulfillment, cart state, loyalty redemption, return/refund.

```
SCOPE DECLARATION
Operations in scope: [list]
Exclusions (with reason): [list or "none"]
SCOPE DECLARATION COMPLETE
```

### Pre-Analysis: Coverage Accountability Roster

| Degradation Class | Committed Minimum | DS Primitive for Impossibility |
|---|---|---|
| Network partition / offline | 2 | |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

---

```
ACT 1 OPEN — Distributed Systems Expert
Scope: Gates 1–4 + Act 1 Registry Audit + Nil Supersession Log + Scope Verification + ACT 1 CLOSE
```

### GATE 1: Discovery and Triage

```
GATE 1 OPEN
Preconditions:
  [ ] SCOPE DECLARATION COMPLETE present
  [ ] Coverage Accountability Roster committed
Entry confirmed: [yes / no]
```

| # | ID | Failure Class | Confidence Basis | Disposition | Rule Applied | Notes |
|---|---|---|---|---|---|---|
| 1 | FS-01 | | | Include / BARRED / Argued-Impossible | | |

BARRED: cite RULE-BARRED-CG; emit CG-NN. Argued-Impossible: name DS Primitive by name.

**Gate 1b — BARRED Resolution**

| BARRED ID | Resolved? | Resolution Mechanism | New Disposition |
|---|---|---|---|

No BARRED: `Gate 1b: none.`

```
GATE 1 CLOSE
Exit postconditions: every candidate disposed / every BARRED has CG-NN /
every Argued-Impossible cites DS Primitive / Coverage Roster updated.
Gate 1 STATUS: CLOSED / OPEN — [reason]
```

---

### GATE 2: Four-Field Scenario Analysis

```
GATE 2 OPEN
Preconditions:
  [ ] Gate 1 STATUS: CLOSED
Entry confirmed: [yes / no]
```

**Anti-split**: Single scenario table. Do not create separate sub-tables for C-phase and
D-phase columns. Do not insert a horizontal rule, heading, or section break between rows
when column ownership shifts from Commerce Expert to DS Expert within a row.

**Section gate**: Produce all scenario rows before writing the Gap Identification section.

**Column-group gate policy**: Within each row, the C-phase columns (State, Capability) must
be complete before any D-phase column (Data at Risk, Recovery Path, Severity, Blast Radius)
is written. Each Row Descriptor below contains an explicit column-group checkpoint.

#### Row Descriptors

**Row 1 — FS-01: [Scenario Name]**

Consequence context: For concurrent-write resolution — oversell if last-write-wins favors
the later write; double-charge if payment idempotency window expires before dedup; duplicate
fulfillment if merge policy is naive. For offline reconnect — stale cart silently overwrites
server state without user notification.
Chronic if never addressed: oversell count accumulates per-transaction / unbounded / inventory
accuracy metric degrades indefinitely.

**Write this row now.**
C-phase (Commerce Expert): fill `State` with the exact system configuration — name components
and their states, not "system is degraded." Fill `Capability` with the named commerce
operations the user can still complete in this failure state.
**Column-group checkpoint: C-phase complete? State and Capability contain non-placeholder
content? If yes, proceed to D-phase. If no, complete C-phase before writing Data at Risk.**
D-phase (DS Expert): fill `Data at Risk` with the named data type and consistency failure
mode. Fill `Recovery Path` with all four stages — each stage requires mechanism (with actor
label) + SLA target + VS (named observable artifact confirming stage completion, distinct
from the mechanism). Fill `Severity` (`degraded` / `impaired` / `down`) and `Blast Radius`.
**Do not advance to Row 2 until this row contains non-placeholder content in every column
including all four Recovery Path stages each with mechanism, SLA target, and a named
Verification Signal that is observable and distinct from the mechanism.**

---

**Row 2 — FS-02: [Scenario Name]**

Consequence context: payment idempotency window expiry → double-charge if provider receives
duplicate authorization; order state divergence under partial fulfillment failure → duplicate
shipment or silent lost order.
Chronic if never addressed: reconciliation backlog grows per-incident / without ceiling /
payment dispute event count accumulates.

**Write this row now.**
C-phase: fill `State` and `Capability` per Column Contract.
**Column-group checkpoint: C-phase complete? If yes, proceed to D-phase.**
D-phase: fill `Data at Risk`, `Recovery Path` (Detect: mechanism|TTD|VS; Contain:
mechanism|TTC|VS; Recover: mechanism|TTR|VS; Validate: mechanism|TTV|VS), `Severity`,
`Blast Radius`.
**Do not advance to Row 3 until all four Recovery Path stages contain mechanism, SLA target,
and a named VS.**

---

Continue for all remaining Include scenarios. Scenario table:

| # | ID | State | Capability | Data at Risk | Recovery Path | Severity | Blast Radius | Rule Applied |
|---|---|---|---|---|---|---|---|---|
| 1 | FS-01 | | | | Detect: [mech\|TTD\|VS]; Contain: [mech\|TTC\|VS]; Recover: [mech\|TTR\|VS]; Validate: [mech\|TTV\|VS] | | | |

```
GATE 2 CLOSE
Exit postconditions:
  [ ] Every Include scenario has all four fields with non-trivial content
  [ ] Every row has column-group checkpoint confirmed (C-phase before D-phase)
  [ ] Every Recovery Path has all four stages with mechanism, SLA target, and named VS
  [ ] Every VS is observable and distinct from its mechanism
  [ ] All RULE-CR-DCV triggers recorded
Gate 2 STATUS: CLOSED / OPEN — [reason]
```

---

### GATE 3: Gap Identification

```
GATE 3 OPEN — Gate 2 STATUS: CLOSED
```

**OEG — Offline Experience Gaps**

| ID | Scenario Ref | Gap Description | Status-Quo Carrying Cost | Actionable Recommendation |
|---|---|---|---|---|
| OEG-01 | FS-NN | | [rate \| horizon \| user-visible failure] | |

No OEG: `OEG-NIL-1: [scope rationale]`

**DCV — Data Consistency Violations**

| ID | Source | Data Type | Failure Mode | Conflict Resolution | Adequacy | Status-Quo Carrying Cost | Rule Applied |
|---|---|---|---|---|---|---|---|
| DCV-01 | FS-NN | | | last-write-wins / merge / manual-reconcile / reject-stale / undefined | adequate / inadequate / undefined | [rate \| horizon \| metric] | |

No DCV: `DCV-NIL-1: [scope rationale]`

**MRF — Missing Recovery Flows**

| ID | Scenario Ref | Absent Mechanism | Status-Quo Carrying Cost | Why No Current Path Exists |
|---|---|---|---|---|
| MRF-01 | FS-NN | | [rate \| horizon \| failure mode] | |

No MRF: `MRF-NIL-1: [scope rationale]`

```
GATE 3 CLOSE
Exit postconditions:
  [ ] All three gap categories present with named findings or typed nils + rationale
  [ ] Every finding has Status-Quo Carrying Cost: rate + horizon + named metric
  [ ] All RULE-CR-DCV entries assigned DCV-NN
  [ ] Conflict resolution verdict for every eventual-consistency scenario
Gate 3 STATUS: CLOSED / OPEN — [reason]
```

---

### GATE 4: Amendment Pass

```
GATE 4 OPEN — Gate 3 STATUS: CLOSED
```

| AMD ID | Entry ID | Original | Amended | Rule Invoked | Gate Re-Opened? |
|---|---|---|---|---|---|

No amendments: `Gate 4: no amendments. No gate re-opens triggered.`

```
GATE 4 CLOSE — Gate 4 STATUS: CLOSED / OPEN
```

---

### Act 1 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations (gate, entry) | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-CR-DCV | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or `GATE N-bypass: REOPEN`] |
| RULE-BARRED-CG | | | | |
| RULE-NIL-SUPERSEDE | | | | |

BYPASS-TRIGGER non-empty → invoke bypass gate-reopening protocol before ACT 1 CLOSE.

POST-ANALYSIS REGISTRY AUDIT (ACT 1) COMPLETE: [confirm no RULE-BYPASSED entries remain]

### Act 1 Terminal: Nil Supersession Log

| Nil ID | Gap Type | State | Superseded By | Gate |
|---|---|---|---|---|

### Act 1 Terminal: Scope Verification

| Declared Operation | Covered | Gap Finding |
|---|---|---|

```
ACT 1 CLOSE (sign-off)
(1) All gates within Act 1 CLOSED:
    Gate 1: [CLOSED / OPEN — reason]; Gate 1b: [CLOSED / N/A]
    Gate 2: [CLOSED / OPEN — reason]; Gate 3: [CLOSED / OPEN — reason]
    Gate 4: [CLOSED / OPEN — reason]
    GATE N-bypass blocks: [CLOSED / none triggered]
    Act 1 Registry Audit: [CLOSED / OPEN — reason]
(2) Act 1 scope exhausted: [yes / unresolved items]
(3) No RULE-BYPASSED conditions remain unresolved within Act 1: [yes / exception]
ACT 1 STATUS: CLOSED / OPEN
```

---

```
ACT 2 OPEN — Commerce Domain Validator
Entry condition: ACT 1 STATUS: CLOSED
Scope: Gate 5 + Act 2 Registry Audit + Inertia Synthesis + ACT 2 CLOSE
```

### GATE 5: Commerce Domain Validation

```
GATE 5 OPEN — ACT 1 STATUS: CLOSED
```

| Scenario ID | Commerce Operation Named? | Amended Operation | CV Finding Issued |
|---|---|---|---|
| FS-01 | Yes / No | | — / CV-DCV-01 / CV-OEG-01 / CV-MRF-01 |

Commerce-domain targets: inventory oversell / payment idempotency / loyalty double-redemption
/ order state divergence — each: [present / absent — rationale].

```
GATE 5 CLOSE — Gate 5 STATUS: CLOSED / OPEN
```

### Act 2 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-COMMERCE-ANCHOR | | | | |

POST-ANALYSIS REGISTRY AUDIT (ACT 2) COMPLETE

### Inertia Synthesis

**Per-finding carrying cost**: For each named gap — failure mode / rate / horizon / named metric.

**Overall synthesis**:
Urgency: HIGH / MEDIUM / LOW
Highest-risk finding: [gap ID] — [carrying cost]
Status-quo option: [specific to `{topic}`]
Intervention recommendation: [owner + threshold + consequence of missing threshold]

```
ACT 2 CLOSE (sign-off)
(1) All gates within Act 2: Gate 5 / bypass blocks / Registry Audit — [CLOSED / reason]
(2) Act 2 scope exhausted: [yes]
(3) No RULE-BYPASSED conditions remain unresolved: [yes / exception]
ACT 2 STATUS: CLOSED / OPEN
```

ANALYSIS COMPLETE (declared only when ACT 1 STATUS: CLOSED AND ACT 2 STATUS: CLOSED)

---

---

## V-05

**Variation axis**: Full integration — Role sequence (C-phase/D-phase column-group gate,
C-32) + Output format (Trigger Condition column with threshold expression + detection signal,
C-33) + Lifecycle emphasis (Verification Signal per recovery stage, C-34). All three new
criteria integrated with all accumulated prior criteria.

**Hypothesis**: The maximum criteria surface requires all three axes simultaneously. C-32
enforces intra-row sequencing — Commerce Expert's C-phase columns (State, Capability,
Trigger Condition threshold) are complete before DS Expert's D-phase columns begin. C-33
adds operationalizable entry conditions to every scenario — each has a quantified threshold
that activates it and an observable signal confirming activation, making the scenario
alertable. C-34 makes each recovery stage independently falsifiable — stage completion is
confirmed by a named observable artifact, not just by SLA elapse. The three criteria are
orthogonal: C-32 governs intra-row sequence; C-33 governs scenario entry conditions; C-34
governs recovery stage completeness. No single-axis variation achieves all three.

---

You are running the **flow-resilience** skill for `{topic}`.

This analysis runs in two sequential acts. Act 1: Distributed Systems Expert (Gates 1–4).
Act 2: Commerce Domain Validator (Gate 5). Each act closes with an independent sign-off.
Do not blend the acts.

---

### RULE REGISTRY

| Rule ID | Trigger Condition | Action Required | Bypass Owner |
|---|---|---|---|
| RULE-CR-DCV | Concurrent state modification by multiple actors without a coordination mechanism | Emit DCV-NN in Gate 3; cite rule inline at trigger point | DS Expert (Act 1) |
| RULE-BARRED-CG | Discovery entry confidence basis cannot be resolved from available context | Mark BARRED; emit CG-NN in coverage log | DS Expert (Act 1) |
| RULE-NIL-SUPERSEDE | Downstream finding introduced in a category that held a typed nil | Annotate nil SUPERSEDED citing new finding ID | DS Expert (Act 1) |
| RULE-COMMERCE-ANCHOR | Include scenario references only a generic operation with no named commerce flow | Amend to name specific commerce operation; record amendment | Commerce Validator (Act 2) |

**Bypass Owner column**: If a rule shows RULE-BYPASSED in the registry audit, the named
owner is responsible for invoking the bypass gate-reopening protocol. Commerce Validator
cannot reopen Act 1 gates; DS Expert cannot reopen Act 2 gates.

---

### BYPASS GATE-REOPENING PROTOCOL

**Authority**: DS Expert for Act 1 rules; Commerce Validator for Act 2 rules. Cross-act
invocation not permitted.

When any rule shows RULE-BYPASSED in the Post-Analysis Rule Registry Audit:

1. Bypass Owner emits:
   `GATE N-bypass: REOPENED — [rule ID] — bypass at [gate, entry ID]`
2. Bypass Owner applies the rule: produces DCV-NN, CG-NN, SUPERSEDED annotation, or
   commerce anchor amendment as required.
3. Bypass Owner emits:
   `GATE N-bypass: AMENDED — CLOSED — [rule now applied at gate, entry]`
4. Bypass Owner updates the audit row: Status → INVOKED; BYPASS-TRIGGER cell → RESOLVED —
   [sub-gate reference]; Citations += sub-gate reference.

**COMPLETE may not be declared** while any RULE-BYPASSED entry remains unresolved in any act.

---

### ANTI-OMISSION ARCHITECTURE

Five structural levels. Each level has a distinct anti-omission mechanism targeting a
distinct omission risk. No two mechanisms conflict or duplicate each other.

| Level | Anti-Omission Mechanism | Omission Risk Targeted | Mechanism Location |
|---|---|---|---|
| Table | Unified row index (`#`) + anti-split instruction | Row fragmentation across ownership transitions at table boundary | `#` column; anti-split instruction in Gate 2 |
| Section | Phase gate — all rows complete before Gap Identification section | Premature section advance before scenario set is exhausted | Section gate instruction in Gate 2 |
| Slot | In-row bold imperative: **"Write this row now."** / **"Do not advance to Row N+1 until [sub-fields] complete."** | Row omission under token pressure | Row Descriptors (below) |
| Column-Group | Intra-row ownership phase gate: C-phase columns complete before D-phase columns begin within the same row | Mid-row D-phase omission when ownership transitions from Commerce Expert to DS Expert | Row Descriptors: Column-Group Gate (below) |
| Column | Column ownership per header (defined in Column Contract, below) | Individual column omission under ownership confusion | Column Contract (below) |

**Anti-split instruction**: Do not create separate sub-tables for Commerce Expert columns and
DS Expert columns. Do not insert a horizontal rule, heading, or section break between rows
when column ownership shifts from C-phase to D-phase within a row.

---

### COLUMN CONTRACT

Place this table before any scenario output. Every column in the Gate 2 scenario table must
have an entry here.

| Column Name | Owner | Phase | Fill Requirement |
|---|---|---|---|
| `#` | Shared | — | Sequential integer; no gaps; no reuse |
| `ID` | Shared | — | FS-NN format; unique |
| `State` | Commerce Expert | C-phase | Specific system configuration when failure occurs; name components and their states; not "system is degraded" |
| `Capability` | Commerce Expert | C-phase | Named commerce operations the user can still complete in this state; not "partial functionality" |
| `Trigger Condition` | DS Expert | C-phase | **Two required components**: (1) threshold expression — a quantified condition that activates this scenario (e.g., "inventory count drops below safety-stock threshold", "payment API latency exceeds 500ms p99", "write queue depth exceeds 10k pending ops"); (2) detection signal — the observable mechanism by which the system identifies the threshold is crossed (e.g., "inventory-service health probe returns degraded", "payment-provider timeout counter increments past alert threshold", "queue-depth metric fires CloudWatch alarm"). A qualitative description without a threshold expression fails. Both components required. |
| `Data at Risk` | DS Expert | D-phase | Named data type + consistency failure mode (lost / stale / inconsistent — with mechanism) |
| `Recovery Path` | DS Expert | D-phase | **Four stages, each with three components**: mechanism (actor-labeled action: client / server / operator / user) \| SLA target (Detect→TTD; Contain→TTC; Recover→TTR; Validate→TTV) \| Verification Signal (VS — **named observable artifact** confirming stage completion: system state, log entry, metric value, API response code). The VS must be named and observable — not a re-statement of the mechanism, not generic ("confirmed", "verified"). Format: `Detect: [mechanism] \| TTD: [target] \| VS: [named artifact]; Contain: [mechanism] \| TTC: [target] \| VS: [artifact]; Recover: [mechanism] \| TTR: [target] \| VS: [artifact]; Validate: [mechanism] \| TTV: [target] \| VS: [artifact]` |
| `Severity` | DS Expert | D-phase | `degraded` / `impaired` / `down` |
| `Blast Radius` | DS Expert | D-phase | Fraction or named segment of users affected |
| `Rule Applied` | DS Expert | D-phase | Rule ID invoked at this row or `—` |

**Column-group boundary**: Trigger Condition is C-phase because its threshold expression
bounds when the scenario is active — Commerce Expert contributes the commerce-domain
threshold (e.g., "below safety-stock level") and DS Expert contributes the detection signal.
Both components must be present before D-phase columns begin.

---

### Pre-Analysis: Commerce Operation Scope Declaration

Declare before Gate 1. Minimum four operations from: checkout, inventory reservation,
payment processing, order fulfillment, cart state, loyalty redemption, return/refund.

```
SCOPE DECLARATION
Operations in scope: [list each]
Operations explicitly excluded (with reason): [list or "none"]
SCOPE DECLARATION COMPLETE
```

### Pre-Analysis: Coverage Accountability Roster

| Degradation Class | Committed Minimum | DS Primitive for Impossibility |
|---|---|---|
| Network partition / offline | 2 | [required if slot unfillable — cite CAP theorem constraint, topology bound, or synchrony guarantee] |
| Partial service failure | 2 | |
| Eventual consistency | 2 | |

---

```
ACT 1 OPEN — Distributed Systems Expert
Scope: Gates 1–4 + Act 1 Registry Audit + Nil Supersession Log + Scope Verification + ACT 1 CLOSE
```

### GATE 1: Discovery and Triage

```
GATE 1 OPEN
Preconditions:
  [ ] SCOPE DECLARATION COMPLETE present
  [ ] Coverage Accountability Roster committed
Entry confirmed: [yes / no]
```

| # | ID | Failure Class | Confidence Basis | Disposition | Rule Applied | Notes |
|---|---|---|---|---|---|---|
| 1 | FS-01 | Network partition / offline \| Partial service failure \| Eventual consistency | | Include / BARRED / Argued-Impossible | RULE-BARRED-CG or — | |

BARRED: cite RULE-BARRED-CG inline; emit CG-NN.
Argued-Impossible: name DS Primitive (CAP theorem guarantee, topology constraint, synchrony
requirement). "Topic does not mention X" is not a DS Primitive.

**Gate 1b — BARRED Resolution**

| BARRED ID | Confidence Basis | Resolved? | Resolution Mechanism | New Disposition |
|---|---|---|---|---|

No BARRED entries: `Gate 1b: none.`

```
GATE 1 CLOSE
Exit postconditions:
  [ ] Every candidate has one named disposition
  [ ] Every BARRED entry has CG-NN emitted
  [ ] Every Argued-Impossible cites DS Primitive by name
  [ ] Coverage Accountability Roster counts updated
Gate 1 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 2: Four-Field Scenario Analysis

```
GATE 2 OPEN
Preconditions:
  [ ] Gate 1 STATUS: CLOSED
Entry confirmed: [yes / no]
```

**Anti-split**: Produce one scenario table. Do not create separate sub-tables for Commerce
Expert columns and DS Expert columns. Do not insert a horizontal rule, heading, or section
break between rows when column ownership shifts from C-phase to D-phase within a row.

**Section gate**: Produce all scenario rows before writing the Gap Identification section.

**Column-group gate policy**: Within each row, all C-phase columns (State, Capability,
Trigger Condition) must contain non-placeholder content before any D-phase column (Data at
Risk, Recovery Path, Severity, Blast Radius) is written. Each Row Descriptor below
contains an explicit column-group checkpoint.

---

#### Row Descriptors

**Row 1 — FS-01: [Scenario Name]**

Consequence context: For concurrent-write scenarios — oversell accumulates per-transaction
if last-write-wins resolves in favor of the later inventory decrement; double-charge per-
transaction if payment provider receives duplicate authorization request outside idempotency
window; duplicate fulfillment per-incident if split-brain order state merges naively.
Chronic if never addressed: oversell count accumulates per-transaction / unbounded /
inventory-accuracy violation metric degrades indefinitely.

**Write this row now.**
C-phase (Commerce Expert + DS Expert threshold):
  - `State`: exact system configuration when this failure occurs — name components and their
    specific states (not "system is degraded"; not "service is down").
  - `Capability`: named commerce operations the user can still complete in this failure state
    (not "some features work").
  - `Trigger Condition`: (1) threshold expression — quantified condition activating this
    scenario (e.g., "cart-service write queue depth exceeds 10k pending ops"); (2) detection
    signal — observable mechanism confirming threshold is crossed (e.g., "cart-service health
    probe returns HTTP 503 for > 3 consecutive checks"). Both required.
**Column-group checkpoint: C-phase complete? State, Capability, and Trigger Condition each
contain non-placeholder content with both Trigger Condition components? If yes, proceed to
D-phase. If no, complete C-phase before writing Data at Risk.**
D-phase (DS Expert):
  - `Data at Risk`: named data type + consistency failure mode.
  - `Recovery Path`: Detect (mechanism with actor | TTD target | VS — named observable artifact
    confirming detection complete, e.g., "alert fires on queue-depth metric dashboard");
    Contain (mechanism with actor | TTC target | VS — e.g., "circuit-breaker OPEN state
    logged in service registry"); Recover (mechanism with actor | TTR target | VS — e.g.,
    "cart-service returns HTTP 200 for 3 consecutive health checks"); Validate (mechanism
    with actor | TTV target | VS — e.g., "pending-ops counter resets to 0 in monitoring
    dashboard"). Each VS must be observable and distinct from its mechanism.
  - `Severity`: degraded / impaired / down.
  - `Blast Radius`: fraction or named segment.
**Do not advance to Row 2 until this row contains non-placeholder content in every column
including both Trigger Condition components and all four Recovery Path stages each with
mechanism, SLA target, and a named Verification Signal that is observable and distinct from
the mechanism.**

---

**Row 2 — FS-02: [Scenario Name]**

Consequence context: payment idempotency window expiry → double-charge if provider receives
duplicate authorization; order state divergence under partial fulfillment failure → duplicate
shipment charged to customer or silent lost order with no notification.
Chronic if never addressed: reconciliation backlog grows per-incident / without ceiling /
payment dispute event count accumulates in finance ledger indefinitely.

**Write this row now.**
C-phase: fill `State`, `Capability`, and `Trigger Condition` (threshold expression + detection
signal — both required) per Column Contract.
**Column-group checkpoint: C-phase complete? Proceed to D-phase only if State, Capability,
and both Trigger Condition components are non-placeholder.**
D-phase: fill `Data at Risk`, `Recovery Path` (Detect: mechanism|TTD|VS; Contain:
mechanism|TTC|VS; Recover: mechanism|TTR|VS; Validate: mechanism|TTV|VS), `Severity`,
`Blast Radius`.
**Do not advance to Row 3 until all C-phase columns are complete and all four Recovery Path
stages each contain mechanism, SLA target, and a named VS.**

---

Continue this pattern for all remaining Include scenarios from Gate 1. Every row must have
its own consequence context, column-group checkpoint, and advance inhibitor.

Scenario table (single table, all rows):

| # | ID | State | Capability | Trigger Condition | Data at Risk | Recovery Path | Severity | Blast Radius | Rule Applied |
|---|---|---|---|---|---|---|---|---|---|
| 1 | FS-01 | | | [threshold expr] / [detection signal] | | Detect: [mech\|TTD\|VS]; Contain: [mech\|TTC\|VS]; Recover: [mech\|TTR\|VS]; Validate: [mech\|TTV\|VS] | | | |

```
GATE 2 CLOSE
Exit postconditions:
  [ ] Every Include scenario has all four fields with non-trivial content
  [ ] Every row has column-group checkpoint confirmed — C-phase complete before D-phase
  [ ] Every Trigger Condition has threshold expression AND detection signal (both non-generic)
  [ ] Every Recovery Path has all four stages: mechanism (actor-labeled) + SLA target + named VS
  [ ] Every VS is observable and distinct from its mechanism
  [ ] Every row has severity and blast radius
  [ ] All RULE-CR-DCV triggers recorded in Rule Applied
Gate 2 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 3: Gap Identification

```
GATE 3 OPEN
Preconditions:
  [ ] Gate 2 STATUS: CLOSED
Entry confirmed: [yes / no]
```

**OEG — Offline Experience Gaps**

| ID | Scenario Ref | Gap Description | Status-Quo Carrying Cost | Actionable Recommendation |
|---|---|---|---|---|
| OEG-01 | FS-NN | | [rate per session/deploy/transaction \| horizon: unbounded/session-scoped \| user-visible metric that accumulates] | |

No OEG: `OEG-NIL-1: [scope rationale — specific deployment constraint that forecloses offline experience gaps]`

**DCV — Data Consistency Violations**

| ID | Source | Data Type | Failure Mode | Conflict Resolution Strategy | Adequacy | Status-Quo Carrying Cost | Rule Applied |
|---|---|---|---|---|---|---|---|
| DCV-01 | FS-NN | | | last-write-wins / merge / manual-reconcile / reject-stale / undefined | adequate / inadequate / undefined | [rate \| horizon \| named metric] | |

Assign DCV-NN to all RULE-CR-DCV pending entries from Gate 2. Inadequate or undefined
conflict resolution: invoke RULE-CR-DCV; emit DCV-CR-NN.
No DCV: `DCV-NIL-1: [scope rationale]`

**MRF — Missing Recovery Flows**

| ID | Scenario Ref | Absent Mechanism | Status-Quo Carrying Cost | Why No Current Path Exists |
|---|---|---|---|---|
| MRF-01 | FS-NN | | [rate \| horizon \| user-visible failure mode] | |

No MRF: `MRF-NIL-1: [scope rationale]`

```
GATE 3 CLOSE
Exit postconditions:
  [ ] All three gap categories present
  [ ] Every finding has Status-Quo Carrying Cost: rate + horizon + named metric
  [ ] All RULE-CR-DCV entries assigned DCV-NN
  [ ] Conflict resolution verdict for every eventual-consistency scenario
  [ ] Every nil has a unique identifier and scope rationale
Gate 3 STATUS: CLOSED / OPEN — [reason if open]
```

---

### GATE 4: Amendment Pass

```
GATE 4 OPEN
Preconditions:
  [ ] Gate 3 STATUS: CLOSED
Entry confirmed: [yes / no]
```

| AMD ID | Entry ID | Original (summary) | Amended (summary) | Rule Invoked | Gate Re-Opened? |
|---|---|---|---|---|---|
| AMD-01 | | | | RULE-NIL-SUPERSEDE / — | Gate N: AMENDED / no |

No amendments: `Gate 4: no amendments required. No gate re-opens triggered.`

```
GATE 4 CLOSE
Exit postconditions:
  [ ] All recovery paths have minimum two actor-labeled steps
  [ ] Every superseded nil has SUPERSEDED annotation with finding ID
  [ ] Every late DCV finding is in Gate 3: AMENDED with re-close confirmation
Gate 4 STATUS: CLOSED / OPEN — [reason if open]
```

---

### Act 1 Terminal: Post-Analysis Rule Registry Audit

**BYPASS-TRIGGER column**: A RULE-BYPASSED status cell requires a non-empty BYPASS-TRIGGER
entry. An empty cell beside RULE-BYPASSED is itself an audit failure.

| Rule ID | Invocations | Citations (gate, entry) | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-CR-DCV | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or `GATE N-bypass: REOPEN — apply RULE-CR-DCV at [gate, entry]`] |
| RULE-BARRED-CG | | | | |
| RULE-NIL-SUPERSEDE | | | | |

If any BYPASS-TRIGGER cell is non-empty — DS Expert invokes bypass gate-reopening protocol:

```
GATE N-bypass: REOPENED — [rule ID] — bypass at [gate, entry ID]
```
[Apply rule: emit required output]
```
GATE N-bypass: AMENDED — CLOSED — rule applied; Citations += [sub-gate]
```

POST-ANALYSIS REGISTRY AUDIT (ACT 1) COMPLETE: [confirm no RULE-BYPASSED entries remain]

---

### Act 1 Terminal: Nil Supersession Log

| Nil ID | Gap Type | State | Superseded By | Gate |
|---|---|---|---|---|

No supersessions: `No supersessions in this run.`

---

### Act 1 Terminal: Scope Verification

| Declared Operation | Covered | Gap Finding |
|---|---|---|
| [operation] | Yes / No | SV-GAP-NN / — |

SCOPE VERIFICATION COMPLETE

---

```
ACT 1 CLOSE (sign-off)
(1) All gates within Act 1 CLOSED:
    Gate 1:    [CLOSED / OPEN — reason]
    Gate 1b:   [CLOSED / N/A — no BARRED entries]
    Gate 2:    [CLOSED / OPEN — reason]
    Gate 3:    [CLOSED / OPEN — reason]
    Gate 4:    [CLOSED / OPEN — reason]
    GATE N-bypass blocks (if triggered): [CLOSED / none triggered]
    Act 1 Registry Audit: [CLOSED / OPEN — reason]
(2) Act 1 scope exhausted: [yes / list any unresolved items]
(3) No RULE-BYPASSED conditions remain unresolved within Act 1: [yes / exception detail]
ACT 1 STATUS: CLOSED / OPEN
```

---

```
ACT 2 OPEN — Commerce Domain Validator
Entry condition: ACT 1 STATUS: CLOSED
Scope: Gate 5 + Act 2 Registry Audit + Inertia Synthesis + ACT 2 CLOSE
```

### GATE 5: Commerce Domain Validation

```
GATE 5 OPEN
Preconditions:
  [ ] ACT 1 STATUS: CLOSED
Entry confirmed: [yes / no]
```

| Scenario ID | Commerce Operation Named? | Amended Operation (RULE-COMMERCE-ANCHOR) | CV Finding Issued |
|---|---|---|---|
| FS-01 | Yes / No | | — / CV-DCV-01 / CV-OEG-01 / CV-MRF-01 |

Commerce-domain finding targets (check each; absent requires explicit rationale):
- Inventory oversell under partition: [present / absent — rationale]
- Payment idempotency window expiry: [present / absent — rationale]
- Loyalty point double-redemption under split-brain: [present / absent — rationale]
- Order state divergence under partial fulfillment failure: [present / absent — rationale]

```
GATE 5 CLOSE
Exit postconditions:
  [ ] Every Include scenario anchored to a named commerce operation
  [ ] All RULE-COMMERCE-ANCHOR invocations recorded
  [ ] All four commerce-domain targets checked with present/absent verdict and rationale
Gate 5 STATUS: CLOSED / OPEN — [reason if open]
```

---

### Act 2 Terminal: Post-Analysis Rule Registry Audit

| Rule ID | Invocations | Citations | Status | BYPASS-TRIGGER |
|---|---|---|---|---|
| RULE-COMMERCE-ANCHOR | | | INVOKED / SCENARIO-ABSENT / RULE-BYPASSED | [empty or `GATE 5-bypass: REOPEN now`] |

If BYPASS-TRIGGER non-empty — Commerce Validator resolves:

```
GATE 5-bypass: REOPENED — RULE-COMMERCE-ANCHOR — bypass at Gate 5, [scenario ID]
```
[Apply rule: name the commerce operation; record amendment]
```
GATE 5-bypass: AMENDED — CLOSED; Audit update: Status → INVOKED
```

POST-ANALYSIS REGISTRY AUDIT (ACT 2) COMPLETE

---

### Inertia Synthesis — What Does Doing Nothing Cost?

**Per-finding carrying cost** (from Gate 3 Status-Quo Carrying Cost column):
For each named gap (OEG-NN, DCV-NN, MRF-NN): state the failure mode, the rate (per
session / deploy / transaction), the horizon (unbounded / session-scoped / compound growth),
and the named metric that accumulates. One entry per finding. The status-quo is a real
option — quantify its cost honestly.

**Overall synthesis**:
Urgency: HIGH / MEDIUM / LOW
Highest-risk finding: [gap ID] — [carrying cost from Gate 3]
Status-quo option: [what "do nothing" looks like for `{topic}` specifically — not generic]
Intervention recommendation: [owner + threshold + consequence of missing threshold]

---

```
ACT 2 CLOSE (sign-off)
(1) All gates within Act 2 CLOSED:
    Gate 5: [CLOSED / OPEN — reason]
    GATE 5-bypass blocks (if triggered): [CLOSED / none triggered]
    Act 2 Registry Audit: [CLOSED / OPEN — reason]
(2) Act 2 scope exhausted: [yes — all scenarios commerce-anchored; all CV targets checked;
    inertia synthesis complete]
(3) No RULE-BYPASSED conditions remain unresolved within Act 2: [yes / exception detail]
ACT 2 STATUS: CLOSED / OPEN
```

ANALYSIS COMPLETE (declared only when ACT 1 STATUS: CLOSED AND ACT 2 STATUS: CLOSED)
