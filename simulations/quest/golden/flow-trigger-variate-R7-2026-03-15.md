# flow-trigger Skill Prompt Variations — Round 7

Generated: 2026-03-15
Rubric: v7 (C-01 through C-27, aspirational /20)
New criteria targeted: C-25 (per-phase entry conditions), C-26 (formal prescriptive register throughout), C-27 (LIFECYCLE OVERVIEW table precedes all phases)

---

## Gap Analysis Entering Round 7

### Pre-read of R6 Scorecard Evidence (Against Rubric v6, C-01 Through C-26 as axis)

R6 established formal prescriptive register (C-26) as its primary variation axis across all five variations. R6 V-05 was the full-integration variation: prescriptive register in all role contracts, a phrasing audit phase at both entry and exit with explicit entry/exit conditions, a dedicated Phrasing Audit Table, and FM cross-references in the lifecycle phase table.

**What R6 V-05 structural features map to R7 rubric additions:**

| R6 V-05 Feature | R7 Criterion | Notes |
|-----------------|-------------|-------|
| `Entry condition:` per role alongside `Exit condition:` | C-25 | R6 V-05 had this; it was not in rubric v6; now formally added |
| All role definitions written in SHALL/MUST/PROHIBITED | C-26 | R6 axis; now formalized in rubric as a scoreable criterion |
| LIFECYCLE OVERVIEW table preceding all roles | C-27 | R6 V-05 had this; not in rubric v6; now formally added |

**Consequence**: R6 V-05 would have passed C-25, C-26, and C-27 had the rubric existed then. R7 does not need to discover these features — it needs to isolate, amplify, and lock them as individual structural invariants.

### R7 Variation Map

Foundation carried forward from R6 (no rediscovery needed):
- FM catalog with reflexive entry (C-24)
- Entry schema contract for FIRING and NON-FIRING entries (C-19)
- Platform vocabulary contract with VOCAB FAIL tags (C-21)
- PROTOCOL PREAMBLE unifying all three contracts (C-22)
- Phase protocol with named phases and job descriptions (C-20)
- Per-phase completion gates on all phases (C-23)
- Candidate denominator pre-scan (C-14)
- Anomaly questions pre-opened before enumeration (C-10)
- Both trigger and skip paths per entry (C-16)
- Denominator closure check after enumeration (C-17)
- Trigger map with execution tier and cascade link columns (C-15)
- Cascade completeness: side-effect writes spawn downstream trigger rows (C-11)
- Evidence-anchored anomaly verdicts (C-13)
- Anomaly remediation guidance per detected anomaly (C-08)
- Self-annotating inline markers for non-conformance (C-12)
- Platform grounding via Power Automate / Dataverse vocabulary (C-07)

| Variation | Axis | New Criteria Targeted | Hypothesis |
|-----------|------|----------------------|------------|
| V-01 | Phrasing register | C-26 | Writing all obligation statements using SHALL/MUST/PROHIBITED/MAY NOT exclusively — in phase job descriptions, slot contracts, and entry/exit conditions — makes C-26 pass by construction; the formal register also tightens C-23 (phase gates become binary-auditable) and C-12 (non-conformance inline markers are clearly distinguishable from obligation text) without requiring structural additions |
| V-02 | Lifecycle emphasis | C-25 | Adding an explicit `Entry condition:` statement to every phase alongside its existing `Exit condition:` makes C-25 pass by construction; bidirectional bounding of all phase boundaries makes phase sequencing independently auditable for both entry and exit without adding a consolidated overview or upgrading register |
| V-03 | Output format | C-27 | Placing a LIFECYCLE OVERVIEW table immediately after the PROTOCOL PREAMBLE — listing all phases with phase ID, job, entry condition stub, and exit condition stub — makes C-27 pass by construction; the overview table also visually exposes any phase that lacks entry/exit conditions (supporting C-23 and C-25) and makes phase control flow navigable before any analysis begins |
| V-04 | Phrasing register + lifecycle emphasis | C-25 + C-26 | Combining bidirectional phase gates (entry + exit conditions on every phase) with full formal prescriptive register passes both C-25 and C-26; formal obligation verbs in entry/exit condition statements produce the strongest structural pairing: each phase boundary states precisely what MUST be true before entry and exactly when exit SHALL be declared complete |
| V-05 | Phrasing register + lifecycle emphasis + output format | C-25 + C-26 + C-27 | Full integration: LIFECYCLE OVERVIEW table in the PROTOCOL PREAMBLE (C-27), bidirectional entry/exit conditions on every phase (C-25), and formal SHALL/MUST/PROHIBITED register throughout all obligation statements (C-26); the combination makes the entire analysis protocol auditable at three levels simultaneously: contract layer (PREAMBLE), phase map layer (OVERVIEW table), and phase body layer (entry/exit gates with formal verbs) |

---

## V-01 — Phrasing Register: Formal Obligation Language Throughout

**Variation axis**: Phrasing register
**Hypothesis**: When all obligation statements in the protocol — phase job descriptions, slot contracts, input/output constraints, anomaly gate instructions, and entry/exit conditions — use formal obligation verbs (SHALL, MUST, PROHIBITED, MAY NOT) exclusively, C-26 passes by construction. The formal register also tightens C-23 (phase gates become binary-auditable obligations rather than guidance) and C-12 (obligation text and non-conformance tags are visually distinguishable). No structural additions (entry conditions, overview table) are made beyond what R6 V-05 carried.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. You SHALL simulate which automations fire when the following record change occurs.

**SCENARIO**

Record: Dynamics 365 Opportunity (opportunity entity)
Change: `Status` field changed from `In Progress` to `Closed Won`
Context: Change made by a sales representative via the model-driven app Opportunity form, saved by user click.

You SHALL complete this analysis using the five-phase protocol defined below. You SHALL complete each phase in full before beginning the next. You SHALL NOT merge phases. You SHALL NOT advance to a later phase before the current phase's exit condition is satisfied.

---

### PROTOCOL PREAMBLE

All three contract declarations below SHALL be read before Phase 1 begins. No platform term SHALL appear in the output before the Platform Vocabulary Contract is declared. No FM tag SHALL appear in the output before the FM Catalog is declared. No entry slot SHALL be used before the Entry Schema Contract is declared.

---

#### Platform Vocabulary Contract

Approved terms for this analysis:

- `sync plugin step` — Dataverse plugin registered on the synchronous pipeline (pre-operation or post-operation, same transaction)
- `async plugin step` — Dataverse plugin registered on the asynchronous pipeline (post-operation, separate system job)
- `automated flow` — Power Automate flow triggered by a Dataverse record-change event (When a row is added, modified or deleted)
- `instant flow` — Power Automate flow triggered manually or by another flow/app
- `scheduled flow` — Power Automate flow triggered on a time-based recurrence
- `business rule` — Model-driven app client-side or server-side rule evaluated on field value
- `real-time workflow` — Legacy Dataverse synchronous workflow (deprecated but may be active)
- `classic workflow` — Legacy Dataverse asynchronous background workflow

Vocabulary deviation SHALL be tagged: `[VOCAB FAIL: {actual term} | FM-03]`

---

#### Failure Mode Catalog

Every inline FM tag in this output SHALL resolve to an entry in this catalog. An FM tag with no catalog entry SHALL itself be tagged: `[FM-15: Catalog Opacity — inline tag FM-NN references no catalog entry]`

**FM-01** — Undeclared Denominator: Enumeration begins without a declared candidate count. Response: Phase 1 SHALL declare N candidates before Phase 2 begins.

**FM-02** — Silent Trigger Omission: A trigger candidate identified in Phase 1 does not appear as a trigger row or an explicit exclusion in Phase 2. Response: Every CA-NN from Phase 1 SHALL appear in Phase 2 or Phase 5 with a disposition.

**FM-03** — Vocabulary Drift: A platform term not in the approved vocabulary appears in the output. Response: Tag the term `[VOCAB FAIL: {term} | FM-03]`.

**FM-04** — Branch Blindness: A trigger entry contains a Condition (Taken) slot but no Condition (Skipped) slot, or vice versa. Response: Both slots SHALL be populated. Missing slot: `[BRANCH BLIND: {entry name} | FM-04]`.

**FM-05** — Storm Evidence Gap: A trigger storm verdict is stated without citing specific trigger rows that contribute to the fire count. Response: Every storm verdict SHALL cite at minimum two CA-IDs and their combined fire count.

**FM-06** — Missing-Trigger Evidence Gap: A missing trigger verdict is stated without citing expected-but-absent candidates. Response: Every missing trigger verdict SHALL reference FLAGGED GAP entries from Phase 5.

**FM-07** — Cycle Evidence Gap: A circular trigger verdict is stated without citing the specific back-edge path. Response: Every cycle verdict SHALL state the path: `{Trigger A} -> {Field Write} -> {Trigger B} -> ... -> {Trigger A}`.

**FM-08** — Cascade Orphan: A side-effect field write with downstream automation potential appears only as an annotation; no downstream trigger row is added for it. Response: Every side-effect write with automation potential SHALL spawn a trigger row in the same phase.

**FM-09** — Denominator Closure Skip: Enumeration completes without an arithmetic closure check. Response: Phase 5 SHALL verify `(FIRED + CONFIRMED ABSENT + FLAGGED GAP) = N`.

**FM-10** — Trigger Map Incomplete: Trigger map is absent, or is present but missing execution tier or cascade link columns. Response: Trigger map SHALL include: Seq, Trigger Name, Tier (sync/async), Anomaly Flag, Spawns.

**FM-11** — Remediation Gap: An anomaly is detected with no remediation guidance. Response: Every confirmed anomaly SHALL have at least one actionable remediation step.

**FM-12** — Entry Schema Violation: A trigger entry is missing one or more declared schema slots. Response: Missing slot SHALL be marked `[SLOT MISSING: {slot name} | FM-12]`.

**FM-13** — Anomaly Gate Absent: An anomaly question (storm / missing / circular) is not pre-opened before Phase 2 begins. Response: All three anomaly questions SHALL be declared OPEN before the first trigger entry.

**FM-14** — Phase Register Violation: An obligation statement in a phase uses descriptive or aspirational language instead of formal obligation verbs (SHALL/MUST/PROHIBITED/MAY NOT). Response: Tag the phrase `[REGISTER FAIL: "{actual text}" -> SHALL/MUST/PROHIBITED | FM-14]`.

**FM-15** — Catalog Opacity: An inline FM tag references an ID not present in this catalog. Response: Tag `[FM-15: Catalog Opacity — FM-NN has no catalog entry]`.

---

#### Entry Schema Contract

**FIRING ENTRY** — every firing trigger entry SHALL contain all of the following slots:

```
Seq:              [integer]
Trigger Name:     [approved vocabulary term]
CA-Ref:           [CA-NN identifier from Phase 1]
Tier:             [sync | async]
Layer:            [plugin step | automated flow | business rule | real-time workflow | classic workflow]
Condition (Taken):   [what MUST be true for this trigger to fire in this scenario]
Condition (Skipped): [what would cause this trigger NOT to fire]
Inputs:           [field/event consumed]
Outputs:          [field write / notification / record creation]
Side Effects:     [additional field writes or spawned actions; "None" if absent]
Spawns:           [CA-NN of any cascade trigger; "None" if absent]
Anomaly Flag:     [none | storm | missing | cycle | FM-NN]
```

A missing slot SHALL be marked `[SLOT MISSING: {slot name} | FM-12]`.

**NON-FIRING ENTRY** — every candidate that does NOT fire SHALL contain:

```
CA-Ref:              [CA-NN identifier]
Trigger Name:        [approved vocabulary term or description]
Condition (Taken):   [the condition under which this trigger would fire]
Condition (Skipped): [the specific condition that prevents it firing in this scenario]
Verdict:             [CONFIRMED ABSENT | FLAGGED GAP]
FM Flag:             [FM-02 if FLAGGED GAP; "none" if CONFIRMED ABSENT]
```

---

### Phase 1: Candidate Pre-scan

**Job**: Phase 1 SHALL identify all automation candidates potentially affected by the Opportunity Status field changing to `Closed Won`. Phase 1 SHALL produce a numbered CA-NN list and declare the candidate denominator N before any trigger is enumerated.

**Anomaly questions** — all three SHALL be declared OPEN before the first CA entry:

```
STORM QUESTION — Status: OPEN
  Is there a set of triggers that collectively fire more than 3 times for a single Status change?

MISSING QUESTION — Status: OPEN
  Is there an expected automation (e.g., revenue recognition flow, manager notification) that does not fire?

CIRCULAR QUESTION — Status: OPEN
  Does any trigger chain produce a field write that re-triggers an earlier trigger in the chain?
```

For each candidate, state:
- CA-NN: Name | Probable Type (approved vocabulary term) | Probable Tier | Evidence of Registration

**Candidate Denominator**: At the close of Phase 1, state: `Candidate denominator: N = [count]`. Phase 2 SHALL NOT begin until this statement is present.

**Phase 1 is complete when**: The anomaly questions are declared OPEN, all CA-NN candidates are listed, and the candidate denominator N is stated.

---

### Phase 2: Trigger Enumeration

**Job**: Phase 2 SHALL enumerate every trigger that fires, in the order it fires, using the FIRING ENTRY schema. Side-effect writes with automation potential SHALL spawn a new trigger row immediately following the row that produces the write. Candidates that do not fire SHALL be enumerated using the NON-FIRING ENTRY schema.

All enumeration SHALL use the approved vocabulary. Vocabulary deviation SHALL be tagged `[VOCAB FAIL: {term} | FM-03]`. A trigger entry with a missing slot SHALL be tagged `[SLOT MISSING: {slot name} | FM-12]`. A trigger entry with only one condition direction SHALL be tagged `[BRANCH BLIND: {entry name} | FM-04]`.

**Phase 2 is complete when**: Every CA-NN candidate from Phase 1 has appeared as either a FIRING ENTRY or a NON-FIRING ENTRY, and all side-effect writes with automation potential have spawned downstream trigger rows.

---

### Phase 3: Anomaly Analysis

**Job**: Phase 3 SHALL close all three anomaly questions opened in Phase 1 with evidence-anchored verdicts. Each verdict SHALL cite specific trigger rows, CA-IDs, or field writes from Phase 2. A bare assertion verdict with no cited evidence SHALL be tagged `[EVIDENCE GAP | FM-05, FM-06, or FM-07]`. Every confirmed anomaly SHALL include at least one remediation step; a confirmed anomaly with no remediation SHALL be tagged `[REMEDIATION ABSENT | FM-11]`.

**STORM VERDICT**: Cite trigger rows counted. If total fires > 3 for a single change event: CONFIRMED + remediation (e.g., debounce strategy, condition filter). If not: NOT DETECTED.

**MISSING TRIGGER VERDICT**: Reference FLAGGED GAP entries from Phase 2. If any exist: CONFIRMED + remediation (e.g., register missing trigger, add condition). If none: NOT DETECTED.

**CIRCULAR TRIGGER VERDICT**: State the directed edge set from Phase 2 side-effect writes. Apply DFS back-edge detection:

```
Initialize: visited = {}  |  in-path = {}
For each trigger T not in visited:
  1. Add T to in-path
  2. For each downstream trigger U that T fires:
     a. If U in in-path: [BACK-EDGE: T -> ... -> U | FM-07]
     b. If U not in visited: recurse on U
  3. Remove T from in-path; add T to visited
State result: Graph property: DAG | CYCLIC
```

If CYCLIC: CONFIRMED + remediation (cycle-break condition, idempotency guard). If DAG: NOT DETECTED.

**Phase 3 is complete when**: All three anomaly verdicts are stated with cited evidence, and all confirmed anomalies have remediation guidance.

---

### Phase 4: Trigger Map Assembly

**Job**: Phase 4 SHALL produce a trigger map covering all firing triggers. The map SHALL include: Seq, Trigger Name, Tier (sync/async), Anomaly Flag, and Spawns (CA-NN reference or "none"). A map missing the Tier or Spawns column SHALL be tagged `[FM-10]`.

| Seq | Trigger Name | CA-Ref | Tier | Anomaly Flag | Spawns |
|-----|-------------|--------|------|-------------|--------|

**Phase 4 is complete when**: All firing triggers from Phase 2 appear in the table with all five columns populated.

---

### Phase 5: Denominator Closure

**Job**: Phase 5 SHALL perform the arithmetic closure check: verify that `FIRED + CONFIRMED ABSENT + FLAGGED GAP = N`, where N is the denominator declared in Phase 1. A mismatch SHALL be tagged `[CLOSURE MISMATCH: {actual count} != N | FM-09]`.

State:
```
Candidates identified (Phase 1): N
FIRED: [count]
CONFIRMED ABSENT: [count]
FLAGGED GAP: [count]
Sum: [count]
Closure: VERIFIED | [CLOSURE MISMATCH: {sum} != N | FM-09]
```

**Phase 5 is complete when**: The closure arithmetic is stated, the sum is verified against N, and any mismatch is tagged.

---

Now receive the scenario above and produce the trigger analysis following this protocol. Every obligation statement you write SHALL use SHALL/MUST/PROHIBITED/MAY NOT. Descriptive phrasing in obligation positions (e.g., "should", "tries to", "is expected to") SHALL be tagged `[REGISTER FAIL: "{actual text}" -> SHALL/MUST/PROHIBITED | FM-14]`.

---

## V-02 — Lifecycle Emphasis: Per-phase Entry Conditions on All Phases

**Variation axis**: Lifecycle emphasis
**Hypothesis**: Adding an explicit `Entry condition:` statement to every phase alongside its existing `Exit condition:` makes C-25 pass by construction. Bidirectional bounding of phase boundaries makes phase sequencing independently auditable: a reader can confirm that Phase N's entry precondition was satisfied (verifying the prior phase's output was checked) and that Phase N's exit condition was satisfied (verifying the phase's job was completed). No formal register upgrade or overview table is introduced — the single-axis test is whether entry conditions alone are sufficient for C-25 with no other changes.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Your task is to simulate which automations fire when the following record change occurs.

**SCENARIO**

Record: Dynamics 365 Opportunity (opportunity entity)
Change: `Status` field changed from `In Progress` to `Closed Won`
Context: Change made by a sales representative via the model-driven app Opportunity form, saved by user click.

Complete this analysis using the five-phase protocol below. Complete each phase in full before beginning the next. Do not merge phases.

---

### PROTOCOL PREAMBLE

Read all three contract declarations below before beginning Phase 1.

---

#### Platform Vocabulary Contract

Approved terms:

- `sync plugin step` — Dataverse plugin, synchronous pipeline
- `async plugin step` — Dataverse plugin, asynchronous pipeline
- `automated flow` — Power Automate, Dataverse record-change trigger
- `instant flow` — Power Automate, manual or app trigger
- `scheduled flow` — Power Automate, time-based recurrence
- `business rule` — model-driven app client-side or server-side rule
- `real-time workflow` — legacy Dataverse synchronous workflow
- `classic workflow` — legacy Dataverse asynchronous background workflow

Vocabulary deviation: tag `[VOCAB FAIL: {actual term} | FM-03]`

---

#### Failure Mode Catalog

**FM-01** — Undeclared Denominator: enumeration begins without a declared candidate count.
**FM-02** — Silent Trigger Omission: a Phase 1 candidate has no disposition in Phase 2 or Phase 5.
**FM-03** — Vocabulary Drift: unapproved platform term in output.
**FM-04** — Branch Blindness: trigger entry has only one condition direction.
**FM-05** — Storm Evidence Gap: storm verdict without citing specific trigger rows.
**FM-06** — Missing-Trigger Evidence Gap: missing trigger verdict without citing FLAGGED GAP entries.
**FM-07** — Cycle Evidence Gap: circular trigger verdict without citing a back-edge path.
**FM-08** — Cascade Orphan: side-effect write with automation potential not linked to a downstream trigger row.
**FM-09** — Denominator Closure Skip: enumeration completes without arithmetic closure check.
**FM-10** — Trigger Map Incomplete: map absent or missing Tier or Spawns columns.
**FM-11** — Remediation Gap: confirmed anomaly with no remediation step.
**FM-12** — Entry Schema Violation: trigger entry missing a declared schema slot.
**FM-13** — Anomaly Gate Absent: anomaly question not pre-opened before Phase 2 begins.
**FM-14** — Entry Condition Absent: a phase body begins without a declared entry condition statement. Tag: `[ENTRY CONDITION ABSENT: Phase N | FM-14]`.
**FM-15** — Catalog Opacity: inline FM tag references an ID not in this catalog. Tag: `[FM-15: Catalog Opacity — FM-NN has no catalog entry]`.

---

#### Entry Schema Contract

**FIRING ENTRY** — all slots required:

```
Seq:                 [integer]
Trigger Name:        [approved vocabulary term]
CA-Ref:              [CA-NN]
Tier:                [sync | async]
Layer:               [plugin step | automated flow | business rule | real-time workflow | classic workflow]
Condition (Taken):   [what must be true for this trigger to fire]
Condition (Skipped): [what would cause this trigger NOT to fire]
Inputs:              [field/event consumed]
Outputs:             [field write / notification / record creation]
Side Effects:        [additional writes or actions; "None" if absent]
Spawns:              [CA-NN of cascade trigger; "None" if absent]
Anomaly Flag:        [none | storm | missing | cycle | FM-NN]
```

Missing slot: `[SLOT MISSING: {slot name} | FM-12]`

**NON-FIRING ENTRY** — all slots required:

```
CA-Ref:              [CA-NN]
Trigger Name:        [name or description]
Condition (Taken):   [condition under which this would fire]
Condition (Skipped): [specific condition preventing fire in this scenario]
Verdict:             [CONFIRMED ABSENT | FLAGGED GAP]
FM Flag:             [FM-02 if FLAGGED GAP; "none" if CONFIRMED ABSENT]
```

---

### Phase 1: Candidate Pre-scan

**Entry condition**: Phase 1 begins when the PROTOCOL PREAMBLE is complete — the Platform Vocabulary Contract, FM Catalog, and Entry Schema Contract are all declared.

**Job**: Identify all automation candidates potentially affected by the Status field changing to `Closed Won`. Produce a numbered CA-NN list and declare the candidate denominator N.

Anomaly questions — declare all three OPEN before the first CA entry:

```
STORM QUESTION — Status: OPEN
  Are there triggers that collectively fire more than 3 times for this single change?

MISSING QUESTION — Status: OPEN
  Is there an expected automation that does not fire?

CIRCULAR QUESTION — Status: OPEN
  Does any trigger chain produce a field write that re-triggers an earlier trigger?
```

For each candidate: CA-NN | Name | Probable Type | Tier | Evidence of Registration

Close with: `Candidate denominator: N = [count]`

**Exit condition**: Phase 1 is complete when the anomaly questions are declared OPEN and the candidate denominator N is stated. Phase 2 SHALL NOT begin until N is declared. A missing N: `[FM-01]`.

---

### Phase 2: Trigger Enumeration

**Entry condition**: Phase 2 begins when Phase 1 has declared N candidates and opened all three anomaly questions. If Phase 1 exit condition is not met: `[ENTRY CONDITION ABSENT: Phase 2 | FM-14]`.

**Job**: Enumerate every firing trigger in order using the FIRING ENTRY schema. Enumerate every non-firing candidate using the NON-FIRING ENTRY schema. Side-effect writes with automation potential spawn a downstream FIRING ENTRY immediately following the producing row.

**Exit condition**: Phase 2 is complete when every CA-NN from Phase 1 has a FIRING or NON-FIRING entry, and all side-effect writes with automation potential have spawned downstream rows.

---

### Phase 3: Anomaly Analysis

**Entry condition**: Phase 3 begins when Phase 2 has produced FIRING and NON-FIRING entries for all N candidates and has linked all cascade side effects. If Phase 2 exit condition is not met: `[ENTRY CONDITION ABSENT: Phase 3 | FM-14]`.

**Job**: Close all three anomaly questions with evidence-anchored verdicts citing Phase 2 rows. State the directed edge set and apply DFS back-edge detection for the circular verdict. Every confirmed anomaly includes at least one remediation step.

STORM VERDICT: cite firing rows, state count, confirm or deny.
MISSING VERDICT: cite FLAGGED GAP entries from Phase 2, confirm or deny.
CIRCULAR VERDICT: directed edge set + DFS steps + graph property (DAG / CYCLIC), confirm or deny.

**Exit condition**: Phase 3 is complete when all three anomaly questions have closed verdicts with evidence citations, and all confirmed anomalies have remediation steps.

---

### Phase 4: Trigger Map Assembly

**Entry condition**: Phase 4 begins when Phase 3 has closed all three anomaly verdicts. If Phase 3 exit condition is not met: `[ENTRY CONDITION ABSENT: Phase 4 | FM-14]`.

**Job**: Produce a trigger map covering all firing triggers from Phase 2.

Required columns: Seq | Trigger Name | CA-Ref | Tier | Anomaly Flag | Spawns

Missing Tier or Spawns column: `[FM-10]`

**Exit condition**: Phase 4 is complete when all firing triggers appear in the table with all six columns populated.

---

### Phase 5: Denominator Closure

**Entry condition**: Phase 5 begins when Phase 4's trigger map is complete. If Phase 4 exit condition is not met: `[ENTRY CONDITION ABSENT: Phase 5 | FM-14]`.

**Job**: Perform arithmetic closure: verify `FIRED + CONFIRMED ABSENT + FLAGGED GAP = N`.

```
Candidates identified (Phase 1): N
FIRED: [count]
CONFIRMED ABSENT: [count]
FLAGGED GAP: [count]
Sum: [count]
Closure: VERIFIED | [CLOSURE MISMATCH: {sum} != N | FM-09]
```

**Exit condition**: Phase 5 is complete when the closure arithmetic is stated and verified against N.

---

Now receive the scenario above and produce the trigger analysis following this protocol. At the start of each phase body, state the entry condition check: confirm the prior phase's exit condition was met, or tag `[ENTRY CONDITION ABSENT: Phase N | FM-14]`.

---

## V-03 — Output Format: LIFECYCLE OVERVIEW Table Before Phase 1

**Variation axis**: Output format
**Hypothesis**: Placing a LIFECYCLE OVERVIEW table immediately after the PROTOCOL PREAMBLE — listing all five phases with Phase ID, Job, Entry Condition, and Exit Condition — makes C-27 pass by construction. The overview table makes the complete phase control flow navigable before any analysis begins, and also visually exposes any phase that lacks an entry or exit condition (supporting C-23 and C-25 without requiring separate per-phase enforcement language). No formal register upgrade is made.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Your task is to simulate which automations fire when the following record change occurs.

**SCENARIO**

Record: Dynamics 365 Opportunity (opportunity entity)
Change: `Status` field changed from `In Progress` to `Closed Won`
Context: Change made by a sales representative via the model-driven app Opportunity form, saved by user click.

Complete this analysis using the five-phase protocol below. Complete each phase in full before beginning the next. Do not merge phases.

---

### PROTOCOL PREAMBLE

Read all three contract declarations and the LIFECYCLE OVERVIEW before beginning Phase 1.

---

#### Platform Vocabulary Contract

Approved terms:

- `sync plugin step` — Dataverse plugin, synchronous pipeline
- `async plugin step` — Dataverse plugin, asynchronous pipeline
- `automated flow` — Power Automate, Dataverse record-change trigger
- `instant flow` — Power Automate, manual or app trigger
- `scheduled flow` — Power Automate, time-based recurrence
- `business rule` — model-driven app client-side or server-side rule
- `real-time workflow` — legacy Dataverse synchronous workflow
- `classic workflow` — legacy Dataverse asynchronous background workflow

Vocabulary deviation: `[VOCAB FAIL: {actual term} | FM-03]`

---

#### Failure Mode Catalog

**FM-01** — Undeclared Denominator: enumeration begins without a declared candidate count.
**FM-02** — Silent Trigger Omission: a Phase 1 candidate has no disposition in Phase 2 or Phase 5.
**FM-03** — Vocabulary Drift: unapproved platform term in output.
**FM-04** — Branch Blindness: trigger entry has only one condition direction.
**FM-05** — Storm Evidence Gap: storm verdict without citing specific trigger rows.
**FM-06** — Missing-Trigger Evidence Gap: missing trigger verdict without citing FLAGGED GAP entries.
**FM-07** — Cycle Evidence Gap: circular trigger verdict without citing a back-edge path.
**FM-08** — Cascade Orphan: side-effect write with automation potential not linked to a downstream trigger row.
**FM-09** — Denominator Closure Skip: enumeration completes without arithmetic closure check.
**FM-10** — Trigger Map Incomplete: map absent or missing required columns.
**FM-11** — Remediation Gap: confirmed anomaly with no remediation step.
**FM-12** — Entry Schema Violation: trigger entry missing a declared schema slot.
**FM-13** — Anomaly Gate Absent: anomaly question not pre-opened before Phase 2 begins.
**FM-14** — Overview Table Absent or Incomplete: LIFECYCLE OVERVIEW table not present in PROTOCOL PREAMBLE, or a phase row is missing a required column. Tag: `[OVERVIEW INCOMPLETE: {phase or column name} | FM-14]`.
**FM-15** — Catalog Opacity: inline FM tag references an ID not in this catalog. Tag: `[FM-15: Catalog Opacity — FM-NN has no catalog entry]`.

---

#### Entry Schema Contract

**FIRING ENTRY** — all slots required:

```
Seq:                 [integer]
Trigger Name:        [approved vocabulary term]
CA-Ref:              [CA-NN]
Tier:                [sync | async]
Layer:               [plugin step | automated flow | business rule | real-time workflow | classic workflow]
Condition (Taken):   [what must be true for this trigger to fire]
Condition (Skipped): [what would cause this trigger NOT to fire]
Inputs:              [field/event consumed]
Outputs:             [field write / notification / record creation]
Side Effects:        [additional writes or actions; "None" if absent]
Spawns:              [CA-NN of cascade trigger; "None" if absent]
Anomaly Flag:        [none | storm | missing | cycle | FM-NN]
```

Missing slot: `[SLOT MISSING: {slot name} | FM-12]`

**NON-FIRING ENTRY** — all slots required:

```
CA-Ref:              [CA-NN]
Trigger Name:        [name or description]
Condition (Taken):   [condition under which this would fire]
Condition (Skipped): [specific condition preventing fire in this scenario]
Verdict:             [CONFIRMED ABSENT | FLAGGED GAP]
FM Flag:             [FM-02 if FLAGGED GAP; "none" if CONFIRMED ABSENT]
```

---

#### LIFECYCLE OVERVIEW

The following table summarizes all five phases of this analysis. This table is the navigable control-flow artifact for the entire protocol. A reader can audit the complete phase sequence from this table alone without reading the phase bodies.

| Phase | Name | Job Summary | Entry Condition | Exit Condition |
|-------|------|-------------|-----------------|----------------|
| 1 | Candidate Pre-scan | Identify all automation candidates; declare denominator N; open all three anomaly questions | PROTOCOL PREAMBLE declared (vocabulary, FM catalog, entry schema, this overview table) | N declared; all three anomaly questions declared OPEN |
| 2 | Trigger Enumeration | Enumerate all firing triggers (FIRING ENTRY schema); enumerate all non-firing candidates (NON-FIRING ENTRY schema); spawn cascade rows for side-effect writes with automation potential | Phase 1 exit condition met: N declared and anomaly questions opened | All N candidates have a FIRING or NON-FIRING entry; all cascade side-effect writes have spawned downstream rows |
| 3 | Anomaly Analysis | Close all three anomaly questions with evidence-anchored verdicts; state directed edge set; apply DFS back-edge detection; provide remediation for every confirmed anomaly | Phase 2 exit condition met: all candidates enumerated, cascades linked | All three anomaly verdicts closed with cited evidence; all confirmed anomalies have remediation steps |
| 4 | Trigger Map Assembly | Produce trigger map with all required columns (Seq, Trigger Name, CA-Ref, Tier, Anomaly Flag, Spawns) | Phase 3 exit condition met: all anomaly verdicts closed | All firing triggers in map; all six columns populated |
| 5 | Denominator Closure | Verify FIRED + CONFIRMED ABSENT + FLAGGED GAP = N; state arithmetic result | Phase 4 exit condition met: trigger map complete | Closure arithmetic stated; sum verified against N |

A phase row in this table that is missing a Job Summary, Entry Condition, or Exit Condition: `[OVERVIEW INCOMPLETE: Phase N - {column name} | FM-14]`.

---

### Phase 1: Candidate Pre-scan

**Job**: Identify all automation candidates. Produce CA-NN list and declare candidate denominator N. Open all three anomaly questions before the first CA entry.

Anomaly questions — declare OPEN before first CA entry:

```
STORM QUESTION — Status: OPEN
MISSING QUESTION — Status: OPEN
CIRCULAR QUESTION — Status: OPEN
```

For each candidate: CA-NN | Name | Probable Type | Tier | Evidence of Registration

Close with: `Candidate denominator: N = [count]`

Exit condition: N is declared and anomaly questions are OPEN. Missing N: `[FM-01]`.

---

### Phase 2: Trigger Enumeration

**Job**: Enumerate all firing and non-firing candidates using declared schemas.

Every entry uses the FIRING ENTRY or NON-FIRING ENTRY schema. Cascade side-effect writes with automation potential spawn a downstream FIRING ENTRY.

Exit condition: all N candidates have a disposition; all cascade writes linked.

---

### Phase 3: Anomaly Analysis

**Job**: Close all three anomaly questions with evidence-anchored verdicts. Include directed edge set and DFS result for the circular verdict. Include remediation for every confirmed anomaly.

Exit condition: all three verdicts closed with cited evidence; all confirmed anomalies have remediation.

---

### Phase 4: Trigger Map Assembly

**Job**: Produce trigger map for all firing triggers.

Required columns: Seq | Trigger Name | CA-Ref | Tier | Anomaly Flag | Spawns

Missing required column: `[FM-10]`

Exit condition: all firing triggers in map; all six columns populated.

---

### Phase 5: Denominator Closure

**Job**: Arithmetic closure check.

```
Candidates identified (Phase 1): N
FIRED: [count]
CONFIRMED ABSENT: [count]
FLAGGED GAP: [count]
Sum: [count]
Closure: VERIFIED | [CLOSURE MISMATCH: {sum} != N | FM-09]
```

Exit condition: closure arithmetic stated and verified against N.

---

Now receive the scenario above and produce the trigger analysis following this protocol. Begin by confirming that all five rows in the LIFECYCLE OVERVIEW table are present with all four required columns. A missing table: `[OVERVIEW INCOMPLETE: Table absent | FM-14]`.

---

## V-04 — Combined: Formal Register + Per-phase Entry Conditions (C-25 + C-26)

**Variation axis**: Phrasing register + lifecycle emphasis
**Hypothesis**: Combining bidirectional phase gates (explicit Entry condition: and Exit condition: on every phase) with full formal prescriptive register (SHALL/MUST/PROHIBITED/MAY NOT throughout all obligation statements) passes both C-25 and C-26. The pairing is stronger than either axis alone: formal obligation verbs in entry/exit condition statements produce binary-auditable phase boundaries — each boundary states precisely what MUST be true for entry and exactly when Phase N SHALL be declared complete. No LIFECYCLE OVERVIEW table is introduced, isolating the test to the register-and-gating combination.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. You SHALL simulate which automations fire when the following record change occurs.

**SCENARIO**

Record: Dynamics 365 Opportunity (opportunity entity)
Change: `Status` field changed from `In Progress` to `Closed Won`
Context: Change made by a sales representative via the model-driven app Opportunity form, saved by user click.

You SHALL complete this analysis using the five-phase protocol below. You SHALL complete each phase in full before advancing to the next. You SHALL NOT merge phases. You SHALL NOT advance until the current phase's exit condition is satisfied. You SHALL NOT begin a phase until its entry condition is satisfied.

---

### PROTOCOL PREAMBLE

All three contract declarations below SHALL be read before Phase 1 begins. No platform term SHALL appear before the Platform Vocabulary Contract is declared. No FM tag SHALL appear before the FM Catalog is declared. No entry slot SHALL be used before the Entry Schema Contract is declared.

---

#### Platform Vocabulary Contract

Approved terms:

- `sync plugin step` — Dataverse plugin, synchronous pipeline
- `async plugin step` — Dataverse plugin, asynchronous pipeline
- `automated flow` — Power Automate, Dataverse record-change trigger
- `instant flow` — Power Automate, manual or app trigger
- `scheduled flow` — Power Automate, time-based recurrence
- `business rule` — model-driven app client-side or server-side rule
- `real-time workflow` — legacy Dataverse synchronous workflow
- `classic workflow` — legacy Dataverse asynchronous background workflow

A vocabulary deviation SHALL be tagged: `[VOCAB FAIL: {actual term} | FM-03]`

---

#### Failure Mode Catalog

Every inline FM tag SHALL resolve to an entry in this catalog. An FM tag with no catalog entry SHALL be tagged: `[FM-15: Catalog Opacity — FM-NN has no catalog entry]`

**FM-01** — Undeclared Denominator: Phase 2 begins without a declared candidate count. Phase 1 SHALL declare N before Phase 2 MAY begin.
**FM-02** — Silent Trigger Omission: A Phase 1 candidate has no disposition in Phase 2 or Phase 5. Every CA-NN SHALL appear with a disposition.
**FM-03** — Vocabulary Drift: Unapproved platform term appears in output. Tag: `[VOCAB FAIL: {term} | FM-03]`.
**FM-04** — Branch Blindness: A trigger entry has only one condition direction. Both Condition (Taken) and Condition (Skipped) SHALL be populated. Tag: `[BRANCH BLIND: {entry name} | FM-04]`.
**FM-05** — Storm Evidence Gap: Storm verdict stated without citing specific trigger rows. Storm verdicts SHALL cite at minimum two CA-IDs and their combined fire count.
**FM-06** — Missing-Trigger Evidence Gap: Missing trigger verdict stated without citing FLAGGED GAP entries. Missing trigger verdicts SHALL cite FLAGGED GAP entries from Phase 5.
**FM-07** — Cycle Evidence Gap: Circular trigger verdict stated without citing a back-edge path. Circular verdicts SHALL state the full path.
**FM-08** — Cascade Orphan: A side-effect write with automation potential is annotated but does not spawn a downstream trigger row. Every side-effect write with automation potential SHALL spawn a downstream FIRING ENTRY.
**FM-09** — Denominator Closure Skip: Phase 5 completes without arithmetic closure check. Phase 5 SHALL verify FIRED + CONFIRMED ABSENT + FLAGGED GAP = N.
**FM-10** — Trigger Map Incomplete: Map is absent or missing Tier or Spawns columns. Trigger map SHALL include Seq, Trigger Name, CA-Ref, Tier, Anomaly Flag, Spawns.
**FM-11** — Remediation Gap: A confirmed anomaly has no remediation step. Every confirmed anomaly SHALL include at least one actionable remediation step.
**FM-12** — Entry Schema Violation: A trigger entry is missing a declared schema slot. Missing slot SHALL be tagged: `[SLOT MISSING: {slot name} | FM-12]`.
**FM-13** — Anomaly Gate Absent: An anomaly question is not declared OPEN before Phase 2 begins. All three anomaly questions SHALL be declared OPEN at the close of Phase 1.
**FM-14** — Phase Entry Condition Absent: A phase body begins without a confirmed entry condition check. Entry condition SHALL be stated at the start of each phase body. Tag: `[ENTRY CONDITION ABSENT: Phase N | FM-14]`.
**FM-15** — Catalog Opacity: An inline FM tag references an ID not present in this catalog. Tag: `[FM-15: Catalog Opacity — FM-NN has no catalog entry]`.
**FM-16** — Register Violation: An obligation statement in a phase uses descriptive or aspirational language instead of formal obligation verbs. Tag: `[REGISTER FAIL: "{actual text}" -> SHALL/MUST/PROHIBITED | FM-16]`.

---

#### Entry Schema Contract

**FIRING ENTRY** — every firing trigger entry SHALL contain all of the following slots:

```
Seq:                 [integer]
Trigger Name:        [approved vocabulary term]
CA-Ref:              [CA-NN]
Tier:                [sync | async]
Layer:               [plugin step | automated flow | business rule | real-time workflow | classic workflow]
Condition (Taken):   [what MUST be true for this trigger to fire]
Condition (Skipped): [what would cause this trigger NOT to fire]
Inputs:              [field/event consumed]
Outputs:             [field write / notification / record creation]
Side Effects:        [additional writes or actions; "None" if absent]
Spawns:              [CA-NN of cascade trigger; "None" if absent]
Anomaly Flag:        [none | storm | missing | cycle | FM-NN]
```

A missing slot SHALL be tagged: `[SLOT MISSING: {slot name} | FM-12]`

**NON-FIRING ENTRY** — every non-firing candidate SHALL contain:

```
CA-Ref:              [CA-NN]
Trigger Name:        [name or description]
Condition (Taken):   [condition under which this would fire]
Condition (Skipped): [specific condition preventing fire in this scenario]
Verdict:             [CONFIRMED ABSENT | FLAGGED GAP]
FM Flag:             [FM-02 if FLAGGED GAP; "none" if CONFIRMED ABSENT]
```

---

### Phase 1: Candidate Pre-scan

**Entry condition**: Phase 1 MUST begin after the PROTOCOL PREAMBLE is complete. All three contract declarations (Platform Vocabulary Contract, FM Catalog, Entry Schema Contract) SHALL be present before Phase 1 begins. If any contract declaration is absent: `[ENTRY CONDITION ABSENT: Phase 1 — {missing contract} | FM-14]`.

**Job**: Phase 1 SHALL identify all automation candidates potentially affected by the Status field changing to `Closed Won`. Phase 1 SHALL produce a numbered CA-NN list. Phase 1 SHALL declare the candidate denominator N. Phase 1 SHALL open all three anomaly questions before the first CA entry is written.

Anomaly questions — all three SHALL be declared OPEN before the first CA entry:

```
STORM QUESTION — Status: OPEN
  Is there a set of triggers that collectively fire more than 3 times for this single change?

MISSING QUESTION — Status: OPEN
  Is there an expected automation that does not fire?

CIRCULAR QUESTION — Status: OPEN
  Does any trigger chain produce a field write that re-triggers an earlier trigger?
```

For each candidate: CA-NN | Name | Probable Type (approved term) | Tier | Evidence of Registration

Close Phase 1 with: `Candidate denominator: N = [count]`

**Exit condition**: Phase 1 SHALL be declared complete when: (a) all three anomaly questions are declared OPEN, and (b) the candidate denominator N is stated. Phase 2 SHALL NOT begin until both conditions are met. A missing N SHALL be tagged: `[FM-01]`.

---

### Phase 2: Trigger Enumeration

**Entry condition**: Phase 2 MUST begin only after Phase 1's exit condition is satisfied: N is declared and all three anomaly questions are OPEN. If Phase 1 exit condition is not met: `[ENTRY CONDITION ABSENT: Phase 2 | FM-14]`.

**Job**: Phase 2 SHALL enumerate every trigger that fires using the FIRING ENTRY schema. Phase 2 SHALL enumerate every non-firing candidate using the NON-FIRING ENTRY schema. Side-effect writes with automation potential SHALL spawn a new FIRING ENTRY immediately following the producing row. Vocabulary drift SHALL be tagged `[VOCAB FAIL: {term} | FM-03]`. A missing schema slot SHALL be tagged `[SLOT MISSING: {slot name} | FM-12]`. An entry with only one condition direction SHALL be tagged `[BRANCH BLIND: {entry name} | FM-04]`.

**Exit condition**: Phase 2 SHALL be declared complete when every CA-NN from Phase 1 has a FIRING or NON-FIRING entry, and all side-effect writes with automation potential have spawned downstream FIRING ENTRIES.

---

### Phase 3: Anomaly Analysis

**Entry condition**: Phase 3 MUST begin only after Phase 2's exit condition is satisfied: all N candidates have dispositions and all cascade side-effect writes have spawned downstream rows. If Phase 2 exit condition is not met: `[ENTRY CONDITION ABSENT: Phase 3 | FM-14]`.

**Job**: Phase 3 SHALL close all three anomaly questions with evidence-anchored verdicts. Every verdict SHALL cite specific trigger rows, CA-IDs, or field writes from Phase 2. A bare assertion verdict with no cited evidence SHALL be tagged with the appropriate evidence-gap FM code. Every confirmed anomaly SHALL include at least one actionable remediation step. A confirmed anomaly with no remediation SHALL be tagged `[REMEDIATION ABSENT | FM-11]`.

STORM VERDICT: cite rows counted; if total fires > 3 for a single change: CONFIRMED + debounce or condition strategy; else NOT DETECTED.

MISSING TRIGGER VERDICT: cite FLAGGED GAP entries from Phase 5 table; if any exist: CONFIRMED + registration or condition remedy; else NOT DETECTED.

CIRCULAR TRIGGER VERDICT:
- State directed edge set from Phase 2 side-effect writes.
- Apply DFS:
  ```
  Initialize: visited = {}  |  in-path = {}
  For each trigger T not in visited:
    1. Add T to in-path
    2. For each downstream trigger U fired by T:
       a. If U in in-path: [BACK-EDGE: T -> ... -> U | FM-07]
       b. If U not in visited: recurse on U
    3. Remove T from in-path; add T to visited
  State: Graph property: DAG | CYCLIC
  ```
- If CYCLIC: CONFIRMED + cycle-break or idempotency remedy; else NOT DETECTED.

**Exit condition**: Phase 3 SHALL be declared complete when all three anomaly verdicts are closed with cited evidence and all confirmed anomalies have remediation steps.

---

### Phase 4: Trigger Map Assembly

**Entry condition**: Phase 4 MUST begin only after Phase 3's exit condition is satisfied: all three anomaly verdicts are closed with cited evidence. If Phase 3 exit condition is not met: `[ENTRY CONDITION ABSENT: Phase 4 | FM-14]`.

**Job**: Phase 4 SHALL produce a trigger map covering all firing triggers from Phase 2.

Required columns: Seq | Trigger Name | CA-Ref | Tier | Anomaly Flag | Spawns

A map missing the Tier or Spawns column SHALL be tagged `[FM-10]`.

| Seq | Trigger Name | CA-Ref | Tier | Anomaly Flag | Spawns |
|-----|-------------|--------|------|-------------|--------|

**Exit condition**: Phase 4 SHALL be declared complete when all firing triggers from Phase 2 appear in the table with all six columns populated.

---

### Phase 5: Denominator Closure

**Entry condition**: Phase 5 MUST begin only after Phase 4's exit condition is satisfied: the trigger map is complete. If Phase 4 exit condition is not met: `[ENTRY CONDITION ABSENT: Phase 5 | FM-14]`.

**Job**: Phase 5 SHALL perform arithmetic closure. Phase 5 SHALL verify that FIRED + CONFIRMED ABSENT + FLAGGED GAP = N, where N is the candidate denominator declared in Phase 1. A mismatch SHALL be tagged `[CLOSURE MISMATCH: {actual sum} != N | FM-09]`.

```
Candidates identified (Phase 1): N
FIRED: [count]
CONFIRMED ABSENT: [count]
FLAGGED GAP: [count]
Sum: [count]
Closure: VERIFIED | [CLOSURE MISMATCH: {sum} != N | FM-09]
```

**Exit condition**: Phase 5 SHALL be declared complete when the closure arithmetic is stated and the sum is verified against N.

---

Now receive the scenario above and produce the trigger analysis following this protocol. At the start of each phase body, state the entry condition check before producing any phase content. Every obligation statement you write SHALL use SHALL/MUST/PROHIBITED/MAY NOT. Descriptive phrasing in obligation positions SHALL be tagged `[REGISTER FAIL: "{actual text}" -> SHALL/MUST/PROHIBITED | FM-16]`.

---

## V-05 — Full Integration: LIFECYCLE OVERVIEW + Entry Conditions + Formal Register (C-25 + C-26 + C-27)

**Variation axis**: Phrasing register + lifecycle emphasis + output format
**Hypothesis**: Full integration of all three R7 structural additions produces a protocol that is auditable at three independent levels simultaneously: (1) the PROTOCOL PREAMBLE makes the contract layer navigable as a unit (C-22), (2) the LIFECYCLE OVERVIEW table makes the complete phase control flow navigable before any analysis begins (C-27), and (3) per-phase entry and exit conditions with formal SHALL/MUST obligation language make every individual phase boundary bidirectionally auditable (C-25 + C-26). The three levels are mutually reinforcing: the LIFECYCLE OVERVIEW table cross-references entry/exit conditions that must match phase body declarations, and formal register makes those declarations binary-auditable obligations rather than guidance.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. You SHALL simulate which automations fire when the following record change occurs.

**SCENARIO**

Record: Dynamics 365 Opportunity (opportunity entity)
Change: `Status` field changed from `In Progress` to `Closed Won`
Context: Change made by a sales representative via the model-driven app Opportunity form, saved by user click.

You SHALL complete this analysis using the five-phase protocol defined below. You SHALL complete each phase in full before advancing. You SHALL NOT merge phases. You SHALL NOT begin a phase until its entry condition is satisfied. You SHALL NOT advance from a phase until its exit condition is satisfied.

---

### PROTOCOL PREAMBLE

All contract declarations and the LIFECYCLE OVERVIEW table SHALL be present before Phase 1 begins. No platform term SHALL appear before the Platform Vocabulary Contract is declared. No FM tag SHALL appear before the FM Catalog is declared. No entry slot SHALL be used before the Entry Schema Contract is declared. Phase 1 SHALL NOT begin before the LIFECYCLE OVERVIEW table is present.

---

#### Platform Vocabulary Contract

Approved terms:

- `sync plugin step` — Dataverse plugin, synchronous pipeline (pre-operation or post-operation, same transaction)
- `async plugin step` — Dataverse plugin, asynchronous pipeline (post-operation, separate system job)
- `automated flow` — Power Automate, Dataverse record-change trigger (When a row is added, modified or deleted)
- `instant flow` — Power Automate, manual trigger or child flow call
- `scheduled flow` — Power Automate, time-based recurrence trigger
- `business rule` — model-driven app client-side or server-side rule evaluated on field value
- `real-time workflow` — legacy Dataverse synchronous workflow (deprecated; may be active in tenant)
- `classic workflow` — legacy Dataverse asynchronous background workflow

A vocabulary deviation SHALL be tagged: `[VOCAB FAIL: {actual term} | FM-03]`
Approved terms are PROHIBITED from modification in output text without a VOCAB FAIL tag.

---

#### Failure Mode Catalog

Every inline FM tag SHALL resolve to an entry in this catalog. An FM tag with no catalog entry SHALL be tagged: `[FM-16: Catalog Opacity — FM-NN has no catalog entry]`. FM-16 is the reflexive catalog entry: its subject is the catalog itself.

**FM-01** — Undeclared Denominator: Phase 2 begins without a declared candidate count. Phase 1 SHALL declare N; Phase 2 SHALL NOT begin without it.
**FM-02** — Silent Trigger Omission: A Phase 1 candidate has no disposition in Phase 2 or Phase 5. Every CA-NN SHALL appear with a FIRED, CONFIRMED ABSENT, or FLAGGED GAP disposition.
**FM-03** — Vocabulary Drift: An unapproved platform term appears in output. Tag: `[VOCAB FAIL: {term} | FM-03]`.
**FM-04** — Branch Blindness: A trigger entry is missing Condition (Taken) or Condition (Skipped). Both slots SHALL be populated. Tag: `[BRANCH BLIND: {entry name} | FM-04]`.
**FM-05** — Storm Evidence Gap: Storm verdict stated without citing specific trigger rows. Storm verdict SHALL cite at minimum two CA-IDs and their combined fire count.
**FM-06** — Missing-Trigger Evidence Gap: Missing trigger verdict stated without citing FLAGGED GAP entries. Tag: `[EVIDENCE GAP: missing trigger verdict | FM-06]`.
**FM-07** — Cycle Evidence Gap: Circular trigger verdict stated without citing a back-edge path. Circular verdict SHALL state the full cycle path.
**FM-08** — Cascade Orphan: A side-effect write with automation potential does not spawn a downstream FIRING ENTRY. Every such write SHALL spawn a downstream row.
**FM-09** — Denominator Closure Skip: Phase 5 completes without arithmetic closure check. Phase 5 SHALL verify FIRED + CONFIRMED ABSENT + FLAGGED GAP = N.
**FM-10** — Trigger Map Incomplete: Map is absent or missing required columns. Map SHALL include Seq, Trigger Name, CA-Ref, Tier, Anomaly Flag, Spawns.
**FM-11** — Remediation Gap: A confirmed anomaly has no remediation step. Every confirmed anomaly SHALL include at least one actionable remediation step.
**FM-12** — Entry Schema Violation: A trigger entry is missing a declared schema slot. Tag: `[SLOT MISSING: {slot name} | FM-12]`.
**FM-13** — Anomaly Gate Absent: An anomaly question is not declared OPEN before Phase 2 begins. Tag: `[FM-13: anomaly question not pre-opened]`.
**FM-14** — Entry Condition Absent: A phase body begins without a confirmed entry condition check. Tag: `[ENTRY CONDITION ABSENT: Phase N | FM-14]`.
**FM-15** — Register Violation: An obligation statement uses descriptive or aspirational language. Tag: `[REGISTER FAIL: "{actual text}" -> SHALL/MUST/PROHIBITED | FM-15]`.
**FM-16** — Catalog Opacity (reflexive): An inline FM tag references an ID not present in this catalog. This entry makes the catalog self-validating. Tag: `[FM-16: Catalog Opacity — FM-NN has no catalog entry]`.

---

#### Entry Schema Contract

**FIRING ENTRY** — every firing trigger entry SHALL contain all of the following slots:

```
Seq:                 [integer — global sequence position]
Trigger Name:        [approved vocabulary term]
CA-Ref:              [CA-NN identifier from Phase 1]
Tier:                [sync | async]
Layer:               [plugin step | automated flow | business rule | real-time workflow | classic workflow]
Condition (Taken):   [what MUST be true for this trigger to fire in this scenario]
Condition (Skipped): [what would cause this trigger NOT to fire]
Inputs:              [field/event consumed by this trigger]
Outputs:             [field write / notification / record creation produced]
Side Effects:        [additional field writes or spawned actions; "None" if absent]
Spawns:              [CA-NN of any downstream cascade trigger; "None" if absent]
Anomaly Flag:        [none | storm | missing | cycle | FM-NN]
```

A missing slot SHALL be tagged: `[SLOT MISSING: {slot name} | FM-12]`

**NON-FIRING ENTRY** — every candidate that does NOT fire SHALL contain:

```
CA-Ref:              [CA-NN]
Trigger Name:        [name or description]
Condition (Taken):   [condition under which this would fire]
Condition (Skipped): [specific condition preventing fire in this scenario]
Verdict:             [CONFIRMED ABSENT | FLAGGED GAP]
FM Flag:             [FM-02 if FLAGGED GAP; "none" if CONFIRMED ABSENT]
```

---

#### LIFECYCLE OVERVIEW

This table IS the navigable control-flow artifact for the entire protocol. A reader SHALL be able to audit the complete phase sequence from this table alone without reading phase bodies. This table SHALL be present in the PROTOCOL PREAMBLE before Phase 1 begins. A missing table SHALL be tagged: `[FM-14: LIFECYCLE OVERVIEW absent]`. A row with a missing required column SHALL be tagged: `[FM-14: LIFECYCLE OVERVIEW row Phase N missing {column name}]`.

| Phase | Name | Entry Condition | Job | Exit Condition |
|-------|------|-----------------|-----|----------------|
| 1 | Candidate Pre-scan | PROTOCOL PREAMBLE complete: vocabulary contract, FM catalog, entry schema, and this LIFECYCLE OVERVIEW table all present | Identify all automation candidates; produce CA-NN list; declare denominator N; open all three anomaly questions | N declared; all three anomaly questions declared OPEN |
| 2 | Trigger Enumeration | Phase 1 exit condition met: N declared, anomaly questions opened | Enumerate all firing triggers (FIRING ENTRY schema); enumerate all non-firing candidates (NON-FIRING ENTRY schema); spawn cascade rows for side-effect writes with automation potential | All N candidates have a FIRING or NON-FIRING disposition; all cascade side-effect writes have spawned downstream rows |
| 3 | Anomaly Analysis | Phase 2 exit condition met: all candidates enumerated, cascades linked | Close all three anomaly questions with evidence-anchored verdicts; state directed edge set; apply DFS back-edge detection; provide remediation for every confirmed anomaly | All three anomaly verdicts closed with cited evidence; all confirmed anomalies have remediation steps |
| 4 | Trigger Map Assembly | Phase 3 exit condition met: all anomaly verdicts closed | Produce trigger map with all required columns: Seq, Trigger Name, CA-Ref, Tier, Anomaly Flag, Spawns | All firing triggers in map; all six columns populated for every row |
| 5 | Denominator Closure | Phase 4 exit condition met: trigger map complete | Verify FIRED + CONFIRMED ABSENT + FLAGGED GAP = N; state arithmetic result; tag any mismatch | Closure arithmetic stated; sum verified against N |

---

### Phase 1: Candidate Pre-scan

**Entry condition**: Phase 1 SHALL begin after the PROTOCOL PREAMBLE is complete. The Platform Vocabulary Contract, FM Catalog, Entry Schema Contract, and LIFECYCLE OVERVIEW table SHALL all be present. If any contract or the overview table is absent: `[ENTRY CONDITION ABSENT: Phase 1 — {missing element} | FM-14]`.

**Job**: Phase 1 SHALL identify all automation candidates potentially affected by the Status field changing to `Closed Won`. Phase 1 SHALL produce a numbered CA-NN list. Phase 1 SHALL declare the candidate denominator N. Phase 1 SHALL open all three anomaly questions before the first CA entry is written.

Anomaly questions — all three SHALL be declared OPEN before the first CA entry:

```
STORM QUESTION — Status: OPEN
  Is there a set of triggers that collectively fire more than 3 times for this single change event?

MISSING QUESTION — Status: OPEN
  Is there an expected automation (e.g., revenue recognition, forecast update, close notification)
  that does not fire?

CIRCULAR QUESTION — Status: OPEN
  Does any trigger chain produce a field write that re-triggers an earlier trigger in the chain?
```

For each candidate, state:
- CA-NN: Trigger Name | Probable Type (approved vocabulary term) | Tier (sync/async) | Evidence of Registration

Close Phase 1 with: `Candidate denominator: N = [count]`

**Exit condition**: Phase 1 SHALL be declared complete when: (a) all three anomaly questions are declared OPEN, and (b) the candidate denominator N is stated. Phase 2 SHALL NOT begin until both are confirmed. A missing N SHALL be tagged `[FM-01]`. Unopened anomaly questions SHALL be tagged `[FM-13]`.

---

### Phase 2: Trigger Enumeration

**Entry condition**: Phase 2 SHALL begin only after Phase 1's exit condition is satisfied: N is declared and all three anomaly questions are OPEN. Entry condition check MUST appear at the start of Phase 2 body. If Phase 1 exit condition is not met: `[ENTRY CONDITION ABSENT: Phase 2 | FM-14]`.

**Job**: Phase 2 SHALL enumerate every trigger that fires, in global sequence order, using the FIRING ENTRY schema. Phase 2 SHALL enumerate every non-firing candidate using the NON-FIRING ENTRY schema. Side-effect writes with automation potential SHALL spawn a new FIRING ENTRY at the next sequence position, immediately following the producing row. Vocabulary drift SHALL be tagged `[VOCAB FAIL: {term} | FM-03]`. A missing schema slot SHALL be tagged `[SLOT MISSING: {slot name} | FM-12]`. An entry missing one condition direction SHALL be tagged `[BRANCH BLIND: {entry name} | FM-04]`.

**Exit condition**: Phase 2 SHALL be declared complete when every CA-NN from Phase 1 has a FIRING or NON-FIRING entry, and all side-effect writes with automation potential have spawned downstream FIRING ENTRIES.

---

### Phase 3: Anomaly Analysis

**Entry condition**: Phase 3 SHALL begin only after Phase 2's exit condition is satisfied: all N candidates have dispositions and all cascade side-effect writes have spawned downstream rows. Entry condition check MUST appear at the start of Phase 3 body. If Phase 2 exit condition is not met: `[ENTRY CONDITION ABSENT: Phase 3 | FM-14]`.

**Job**: Phase 3 SHALL close all three anomaly questions opened in Phase 1. Each verdict SHALL cite specific trigger rows, CA-IDs, or field writes from Phase 2. A bare assertion verdict SHALL be tagged with the corresponding evidence-gap FM code. Every confirmed anomaly SHALL include at least one actionable remediation step; a confirmed anomaly with no remediation SHALL be tagged `[REMEDIATION ABSENT | FM-11]`.

**STORM VERDICT**: Cite all contributing trigger rows and state their combined fire count. If total fires > 3 for a single change event: CONFIRMED + debounce strategy or condition-filter remedy. If not: NOT DETECTED.

**MISSING TRIGGER VERDICT**: Cite FLAGGED GAP entries from Phase 5 (or state "none found in Phase 2"). If any FLAGGED GAP entries exist: CONFIRMED + trigger registration or condition-add remedy. If none: NOT DETECTED.

**CIRCULAR TRIGGER VERDICT**: State the directed edge set constructed from all Phase 2 Side Effects and Spawns links. Apply DFS back-edge detection:

```
Initialize: visited = {}  |  in-path = {}
For each trigger T not yet in visited:
  1. Add T to in-path
  2. For each downstream trigger U fired by T (per edge set):
     a. If U in in-path: PROHIBITED to continue without tagging [BACK-EDGE: T -> ... -> U -> T | FM-07]
     b. If U not in visited: recurse on U
  3. Remove T from in-path; add T to visited
Final state: Graph property: DAG | CYCLIC
```

If CYCLIC: CONFIRMED + cycle-break condition or idempotency guard remedy. If DAG: NOT DETECTED.

**Exit condition**: Phase 3 SHALL be declared complete when all three anomaly verdicts are closed with cited evidence and all confirmed anomalies have at least one remediation step.

---

### Phase 4: Trigger Map Assembly

**Entry condition**: Phase 4 SHALL begin only after Phase 3's exit condition is satisfied: all three anomaly verdicts are closed. Entry condition check MUST appear at the start of Phase 4 body. If Phase 3 exit condition is not met: `[ENTRY CONDITION ABSENT: Phase 4 | FM-14]`.

**Job**: Phase 4 SHALL produce a trigger map covering all firing triggers from Phase 2. The map SHALL include all six required columns. A map missing the Tier or Spawns column SHALL be tagged `[FM-10]`.

Required columns: Seq | Trigger Name | CA-Ref | Tier | Anomaly Flag | Spawns

| Seq | Trigger Name | CA-Ref | Tier | Anomaly Flag | Spawns |
|-----|-------------|--------|------|-------------|--------|

**Exit condition**: Phase 4 SHALL be declared complete when all firing triggers from Phase 2 appear in the table with all six columns populated for every row.

---

### Phase 5: Denominator Closure

**Entry condition**: Phase 5 SHALL begin only after Phase 4's exit condition is satisfied: the trigger map is complete with all six columns populated. Entry condition check MUST appear at the start of Phase 5 body. If Phase 4 exit condition is not met: `[ENTRY CONDITION ABSENT: Phase 5 | FM-14]`.

**Job**: Phase 5 SHALL perform the arithmetic closure check. Phase 5 SHALL verify that FIRED + CONFIRMED ABSENT + FLAGGED GAP = N, where N is the candidate denominator declared in Phase 1. A mismatch SHALL be tagged `[CLOSURE MISMATCH: {actual sum} != N | FM-09]`. Phase 5 MUST NOT be omitted if N > 0.

```
Candidates identified (Phase 1): N
FIRED: [count]
CONFIRMED ABSENT: [count]
FLAGGED GAP: [count]
Sum: [count]
Closure: VERIFIED | [CLOSURE MISMATCH: {sum} != N | FM-09]
```

**Exit condition**: Phase 5 SHALL be declared complete when the closure arithmetic is stated and the sum is verified against N. An unverified closure is a structural defect, not a scope judgment.

---

Now receive the scenario above and produce the trigger analysis following this protocol exactly.

Before Phase 1 begins, confirm: "PROTOCOL PREAMBLE complete — Platform Vocabulary Contract, FM Catalog, Entry Schema Contract, and LIFECYCLE OVERVIEW table all present."

At the start of each phase body, state the entry condition check: confirm the prior phase's exit condition was met, or tag `[ENTRY CONDITION ABSENT: Phase N | FM-14]`.

All obligation statements in your output SHALL use SHALL/MUST/PROHIBITED/MAY NOT. Descriptive phrasing in obligation positions (e.g., "should", "tries to", "is expected to") SHALL be tagged `[REGISTER FAIL: "{actual text}" -> SHALL/MUST/PROHIBITED | FM-15]`.
