---
skill: flow-trigger
round: 13
rubric_version: 10
new_criteria: [C-32, C-33]
date: 2026-03-16
---

# flow-trigger — Round 13 (Rubric v10) Variations

**New criteria this round:**
- **C-32** — Unified Phase 0 obligation registry: all six per-row compliance metadata types (typed
  status, refutation condition, weaker alternative, failure mode, activation event, producing role)
  co-located as named columns in a single named table. Separate tables satisfying individual prior
  criteria are a weak pass. A single registry row that is the obligation's complete self-audit
  record is the full pass. Any column empty across all rows without explicit N/A-with-reason fails.
- **C-33** — Constraint-propagating INERTIA CONTRAST: failure mode labels specific enough that
  reading the label alone derives the mechanism's minimum pass condition without consulting the
  rubric. Labels naming the absent structural property ("anonymous prohibition," "anonymous artifact
  gap") satisfy; consequence-only labels ("creates ambiguity," "less traceable") fail.

**Round 12 gap analysis:**
- V-01 through V-04: Phase 0 obligations spread across 5+ separate tables (SCOPE GATE table, EOR
  table, PROHIBITION CONTRACTS table, ARTIFACT MANIFEST, EXCLUSION LOG). Each table satisfies its
  individual prior criterion. Cross-table navigation required to audit one obligation. C-32 FAIL.
- V-01 through V-03: INERTIA CONTRAST failure modes describe consequences without naming absent
  structural properties. C-33 FAIL.
- V-04: INERTIA CONTRAST failure modes partially name structural absences ("activation window
  ambiguous", "scope boundary unverifiable") but labels do not reach constraint-propagation
  strength — reader still needs one reasoning hop from label to pass condition. C-33 WEAK PASS.
- V-05: Not generated in R12. C-32 and C-33 both unresolved.

**Variation axes:**

| Variation | Axis | C-32 Prediction | C-33 Prediction |
|-----------|------|-----------------|-----------------|
| V-01 | Inertia framing — consequence-language failure modes; separate obligation tables | FAIL | FAIL |
| V-02 | Output format — vertical obligation record blocks instead of table rows | WEAK PASS | FAIL |
| V-03 | Role sequence — separate role-owned tables; INERTIA CONTRAST names structural absences | FAIL | WEAK PASS |
| V-04 | Inertia framing + Output format — single unified table + structural-property-naming labels | PASS | WEAK PASS |
| V-05 | Inertia framing + Output format + Lifecycle emphasis — anonymous-X labels + unified table + embedded derivation test | PASS | PASS |

**Scenario used in all variations:** A Dynamics 365 Sales `account` record's `statecode` field
changes from `Active` (0) to `Inactive` (1).

---

## V-01

**Variation axis:** Inertia framing — consequence-language failure modes; separate obligation tables

**Hypothesis:** Phase 0 obligations appear in five separate tables (SCOPE GATE, EOR, EXCLUSION LOG,
PROHIBITION CONTRACTS, ARTIFACT MANIFEST), each satisfying its individual criterion (C-25 through
C-31). The INERTIA CONTRAST section names two mechanisms with failure modes describing
consequences: "scope gap produces false positive candidates" rather than "anonymous scope boundary";
"global prohibition creates temporal ambiguity" rather than "anonymous prohibition." A reader who
knows only the failure mode cannot derive the pass condition without the rubric. C-32 fails because
metadata is spread across separate tables. C-33 fails because labels are consequence-only.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to
`Inactive` (1). Your task: determine exactly which automations fire, in what order, with what
inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular
triggers).

Execute phases in strict sequence. Each phase SHALL complete before the next begins.

---

### PROTOCOL PREAMBLE

*Governing contract layer. Appears before Phase 0. Contains all three contract declarations.*

#### Platform Term Contract

| Approved Term | Prohibited Substitutions |
|--------------|-------------------------|
| automated cloud flow | workflow, automation, rule |
| instant cloud flow | manual flow, button flow |
| scheduled cloud flow | recurring flow, timer flow |
| Dataverse plug-in | plugin, CRM plugin, platform plugin |
| sync plug-in step | synchronous plugin, pre-stage plugin |
| async plug-in step | asynchronous plugin, background plugin |
| trigger event: When a row is added, modified or deleted | record trigger, update trigger |
| Power Automate connector | connector trigger, flow connector |

Any term deviating from this list SHALL be tagged `[VOCAB FAIL: "actual text" -> correction | FM-08]`.

#### FM Catalog

| FM Code | Failure Mode | Expected Behavior | Output Marker | Phase(s) |
|---------|-------------|-------------------|---------------|----------|
| FM-01 | Trigger omission | Every bound trigger listed by name | `[OMIT: trigger-name \| FM-01]` | 2, 3 |
| FM-02 | Firing order violation | Sync before async; by priority within tier | `[ORDER FAIL: actual \| FM-02]` | 2, 3 |
| FM-03 | Missing input/output specification | Named payload and output; no placeholders | `[IO FAIL: trigger-name \| FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three pathology classes addressed | `[PATH MISS: class \| FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name \| FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced until no further triggers fire | `[CASCADE SHALLOW \| FM-06]` | 4 |
| FM-07 | Missing conditional branch | Firing and skipped branch both stated | `[BRANCH MISS: trigger-name \| FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used throughout | `[VOCAB FAIL: "actual" -> correction \| FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with one-line mitigation | `[RISK MISS \| FM-09]` | 5 |
| FM-10 | Missing timing annotation | Sync/async distinguished; latency noted | `[TIMING MISS: trigger-name \| FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct vocabulary pair | `[NEG MISS \| FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence; bare assertions insufficient | `[INSUFFICIENT: evidence needed \| FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition declared per chain | `[CHAIN OPEN: CH-NN \| FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger constructed | `[GRAPH MISS \| FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before condition filtering | `[DENOM MISS \| FM-15]` | 1 |
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All |
| FM-17 | Gate Register Drift | Gate statement uses descriptive language where SHALL/MUST required | `[GATE REGISTER DRIFT: Phase N \| FM-17]` | All |
| FM-18 | No sync/async structural split | Sync and async triggers in separate phases | `[SPLIT MISS \| FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied to adjacency structure | `[BACKTRACK MISS \| FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each cascade chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN \| FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every violation marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure: firing + non-firing + unresolved = N | `[RECON MISS \| FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing trigger entry | `[SE MISS: trigger-name \| FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade-link columns | `[MAP MISS \| FM-25]` | 6 |

*FM-21 is self-referential: any violation marker without an FM code is itself an FM-21 violation.*

**Phase-Boundary Defect Classes note:** FM-16 and FM-17 are structurally non-overlapping.
FM-16: entry condition absent (presence defect). FM-17: entry condition exists but in wrong
register (quality defect). Separate IDs make each tag independently informative — a reviewer
scanning a single tag determines the complete structural fact for that defect class without
further inspection.

#### Entry Schema Contract

All trigger entries SHALL conform to one schema. A blank named slot is a structural gap.

**FIRING ENTRY** (all slots required):
```
Trigger Name:
Flow Type:          [automated cloud flow | instant cloud flow | Dataverse plug-in | ...]
Execution Tier:     [sync | async | scheduled]
Trigger Event:
Input Fields:       [specific named fields — no generic placeholders]
Output Action:      [specific action — no generic placeholders]
Side Effects:       [field writes produced beyond primary output, or "none"]
Condition (Taken):  [what must be true for this trigger to fire]
Condition (Skipped):[what would cause this trigger NOT to fire in this scenario]
Anomaly Flag:       [none | storm | missing | circular]
```

**NON-FIRING ENTRY** (all slots required):
```
Trigger Name:
Flow Type:
Reason Not Firing:  [specific condition excluding this trigger]
Condition (Taken):  [what would cause this trigger to fire — not met in this scenario]
Condition (Skipped):[what IS true in this scenario that blocks this trigger]
```

---

### PHASE 0 — PREPARATION

**Entry condition:** Phase 0 SHALL begin when the scenario specification is received and the
PROTOCOL PREAMBLE has been declared complete.

**Job:** Phase 0 SHALL produce and lock all pre-enumeration structural artifacts before Phase 1
begins. Each artifact type appears in its own dedicated table. Phase 0 SHALL issue an exit signal
only when all obligations carry Status: SATISFIED.

**BREACH TOKEN PROTOCOL:** `[PROHIBITION BREACH: Role | {prohibition name} | FM-NN]`

#### SCOPE GATE

| Field | Value | Status | Refutation Condition |
|-------|-------|--------|---------------------|
| Entity type | account | SATISFIED | Violated if no entity type named before Phase 1 |
| Operation | Update | SATISFIED | Violated if no operation named |
| Triggering field | statecode | SATISFIED | Violated if no field or event named |
| Previous value | Active (0) | SATISFIED | Violated if no pre-change value stated |
| New value | Inactive (1) | SATISFIED | Violated if no post-change value stated |

#### EXCLUSION LOG

| Layer | Disposition | Reason | Status |
|-------|-------------|--------|--------|
| Classic Dynamics 365 workflows | EXCLUDED | Deprecated; not in scope for new implementations | SATISFIED |
| Scheduled cloud flows | EXCLUDED | No field-change trigger; no cron fires on record update | SATISFIED |
| Instant cloud flows | EXCLUDED | Require manual trigger; no manual action in this scenario | SATISFIED |
| Dataverse sync plug-in steps | INCLUDED | Execute within transaction; in scope | SATISFIED |
| Dataverse async plug-in steps | INCLUDED | Execute outside transaction; in scope | SATISFIED |
| Automated cloud flows (Dataverse) | INCLUDED | Trigger on When a row is added, modified or deleted | SATISFIED |

#### EOR TABLE (Execution Order Rules)

| Rule ID | Principle | Applies To | Refutation | Status |
|---------|-----------|-----------|------------|--------|
| EOR-01 | Sync plug-in steps execute before async steps within same change event | All sync entries | Violated if any async entry positioned before a sync entry | SATISFIED |
| EOR-02 | Within sync tier: lower plug-in step rank fires first | Sync plug-in entries | Violated if ordering contradicts documented rank values | SATISFIED |
| EOR-03 | Async steps and automated cloud flows: relative order not guaranteed | All async entries | Violated if relative ordering of async entries stated as deterministic | SATISFIED |

#### CASCADE DEPTH BUDGET

| Parameter | Value | Status | Refutation Condition |
|-----------|-------|--------|---------------------|
| MAX_DEPTH | 5 | SATISFIED | Violated if no named maximum depth declared before Phase 4 |
| Overflow marker | [DEPTH EXCEEDED: CH-NN] | SATISFIED | Violated if chains exceeding budget carry no marker |

#### PROHIBITION CONTRACTS

| Prohibition | Role Bound | Applies After | Status | Refutation Condition |
|-------------|-----------|--------------|--------|---------------------|
| MAY NOT add new candidates after denominator declared | Domain Expert | Denominator declaration (Phase 1) | SATISFIED | Violated if Domain Expert adds candidates after Phase 1 N declaration |
| MAY NOT modify SCOPE GATE fields after exit signal | Classifier | Phase 0 exit signal | SATISFIED | Violated if scope gate is mutated after exit signal |

#### ARTIFACT MANIFEST

| ART-ID | Artifact Name | Producing Role | Producing Phase | Status | Refutation Condition |
|--------|--------------|---------------|-----------------|--------|---------------------|
| ART-01 | SCOPE GATE | Auditor | Phase 0 | SATISFIED | Violated if no event tuple before Phase 1 |
| ART-02 | EXCLUSION LOG | Auditor | Phase 0 | SATISFIED | Violated if no layer sweep before candidates named |
| ART-03 | EOR TABLE | Domain Expert | Phase 0 | SATISFIED | Violated if no rule IDs before entry ordering |
| ART-04 | CASCADE DEPTH BUDGET | Domain Expert | Phase 0 | SATISFIED | Violated if no named depth limit before Phase 4 |
| ART-05 | PROHIBITION CONTRACTS | Auditor | Phase 0 | SATISFIED | Violated if no prohibition declarations before roles active |
| ART-06 | BREACH TOKEN PROTOCOL | Auditor | Phase 0 | SATISFIED | Violated if no named breach token format declared |

#### INERTIA CONTRAST

*Why each Phase 0 mechanism was chosen over the simpler alternative:*

**SCOPE GATE (event tuple vs. prose preamble):**
- Weaker alternative: State scope in an opening narrative sentence ("This analysis covers account
  statecode changes on the Dataverse platform")
- Failure mode: Scope gap produces false positive candidates — without a named boundary definition,
  a reviewer must interpret prose to determine whether any given trigger qualifies, and
  interpretations may diverge

**PROHIBITION CONTRACTS (with "Applies After" field vs. timeless global prohibition):**
- Weaker alternative: State role prohibitions without temporal scope ("Domain Expert may not add
  candidates")
- Failure mode: Global prohibition creates temporal ambiguity — without a named activation event,
  whether a prohibition is currently active cannot be determined from the contract alone, and
  enforcement depends on implied phase sequencing

#### Phase 0 Exit Signal

| Obligation | Status |
|------------|--------|
| ART-01 SCOPE GATE | SATISFIED |
| ART-02 EXCLUSION LOG | SATISFIED |
| ART-03 EOR TABLE | SATISFIED |
| ART-04 CASCADE DEPTH BUDGET | SATISFIED |
| ART-05 PROHIBITION CONTRACTS | SATISFIED |
| ART-06 BREACH TOKEN PROTOCOL | SATISFIED |

Phase 0 EXIT SIGNAL: 6/6 SATISFIED — Phase 1 may begin.

**Exit condition:** Phase 0 SHALL be declared complete when all 6 obligations are SATISFIED and
the exit signal is issued. No Phase 1 entry SHALL occur without this signal.

---

### STRUCTURAL INVARIANT LAYER

**Invariant 1 — Phase body completeness:** Every phase body SHALL contain entry condition, job
description, and exit condition. Violation: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`

**Invariant 2 — Gate statement formal register:** All gate statements SHALL use SHALL/MUST in the
obligation position. Violation: `[GATE REGISTER DRIFT: Phase N | FM-17]`

**Invariant 3 — Denominator closure:** Candidate count N declared in Phase 1 SHALL reconcile after
Phase 3: firing + non-firing + unresolved = N. Violation: `[RECON MISS | FM-22]`

**Invariant 4 — FM code in every marker:** Every violation marker SHALL include its FM catalog
code. Violation: `[FM-21]`

**Invariant 5 — Uniform slot mandate:** Every named slot in every entry schema template is
required. An empty named slot is a structural gap equivalent to a missing entry.

---

### LIFECYCLE OVERVIEW

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 0 | Preparation | Phase 0 SHALL begin when scenario received and PROTOCOL PREAMBLE complete | Produce and lock all Phase 0 artifacts; issue exit signal | Phase 0 SHALL be complete when all 6 obligations SATISFIED and exit signal issued |
| 1 | Pre-scan | Phase 1 SHALL begin when Phase 0 exit signal is issued | Identify all candidate triggers; declare N; open anomaly slots; issue PCC-1 | Phase 1 SHALL be complete when N declared, all three anomaly slots OPEN, PCC-1 issued |
| 2 | Sync Enumeration | Phase 2 SHALL begin when Phase 1 complete, N declared, and PCC-1 issued | Enumerate all sync-tier candidates; include negative vocabulary example; order by priority | Phase 2 SHALL be complete when all sync-tier candidates have resolved entries with all slots populated |
| 3 | Async Enumeration | Phase 3 SHALL begin when Phase 2 complete and Sync Trigger Table produced | Enumerate all async-tier candidates; annotate latency tier per entry | Phase 3 SHALL be complete when all async-tier candidates have resolved entries with all slots populated |
| 4 | Cascade Tracing | Phase 4 SHALL begin when Phases 2 and 3 complete and both tables produced | Trace cascade chains from side-effect writes; assign Chain IDs; apply back-edge detection; mark TERMINAL | Phase 4 SHALL be complete when all side-effect writes evaluated, all chains carry Chain-Status, back-edge detection applied |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when Phase 4 complete and all chains carry Chain-Status | Deliver evidence-anchored verdicts for all three anomaly classes; propose remediation per confirmed anomaly | Phase 5 SHALL be complete when all three verdicts issued with cited evidence and every confirmed anomaly has at least one remediation |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when Phase 5 complete and all anomaly verdicts issued | Produce trigger map; perform denominator closure | Phase 6 SHALL be complete when trigger map covers all triggers with required columns and closure stated |

---

### Phase 1 — Pre-scan

**Entry condition:** Phase 1 SHALL begin when Phase 0 exit signal is issued.

**Job:** Identify all candidate triggers without condition filtering. Declare denominator N. Open
all three anomaly question slots. Issue Phrasing Clearance PCC-1 if zero register violations found.

**Anomaly Questions — Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does this change cause more triggers to fire than the environment can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for account suspension that does not appear? | OPEN |
| Circular Trigger | Does any trigger's output create a field write that re-activates an upstream trigger? | OPEN |

**Denominator Pre-Scan:**

| Candidate Trigger | Flow Type | Activation Condition | Tier |
|------------------|-----------|---------------------|------|
| *[enumerate all candidates without filtering]* | | | |

N = *[integer — declare before Phase 2 begins]*

**Exit condition:** Phase 1 SHALL be complete when N is declared, all three anomaly slots are
explicitly OPEN, and PCC-1 is issued.

---

### Phase 2 — Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when Phase 1 is complete, N is declared, and PCC-1 is
issued. If PCC-1 absent: `[ENTRY CONDITION ABSENT: Phase 2 | FM-16]`

**Job:** Enumerate all synchronous triggers. Every sync-tier candidate SHALL resolve to a FIRING
ENTRY or NON-FIRING ENTRY. No candidate SHALL be omitted without a NON-FIRING ENTRY. At least one
negative vocabulary example SHALL be included. Order by execution priority, highest first.

**Negative vocabulary example (required):** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be complete when every sync-tier candidate has a resolved entry
with all schema slots populated and no blank slots remain.

---

### Phase 3 — Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when Phase 2 is complete and the Sync Trigger Table is
produced.

**Job:** Enumerate all asynchronous triggers. Every async-tier candidate SHALL resolve to a FIRING
ENTRY or NON-FIRING ENTRY. Order by connector tier, then priority. Annotate latency tier
(near-real-time / standard / batch) per entry.

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be complete when every async-tier candidate has a resolved entry
with all schema slots populated.

---

### Phase 4 — Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when Phases 2 and 3 are complete and both trigger tables
are produced.

**Job:** Trace every cascade chain from side-effect field writes to its terminal. Assign Chain IDs.
Mark final row of each chain `[TERMINAL]`. Apply back-edge detection to adjacency structure. Each
cascade entry SHALL carry a `[Depth: N/5]` counter.

**Cascade Chain Table:**

| Chain ID | Depth | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|-------|------|--------------------|-------------------|--------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be complete when all side-effect writes are evaluated, all chains
carry Chain-Status, and back-edge detection has been applied.

---

### Phase 5 — Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when Phase 4 is complete and all cascade chains carry
Chain-Status.

**Job:** Deliver evidence-anchored verdicts for all three anomaly classes. Cite evidence from prior
phases. Bare assertions SHALL be marked `[INSUFFICIENT: state evidence needed | FM-12]`. Every
confirmed anomaly SHALL receive at least one remediation step.

**Trigger Storm:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Missing Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Circular Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Exit condition:** Phase 5 SHALL be complete when all three verdicts are issued with cited evidence
and every confirmed anomaly has at least one remediation step.

---

### Phase 6 — Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when Phase 5 is complete and all anomaly verdicts issued.

**Job:** Produce trigger map covering all triggers with execution-tier and Spawns columns. Perform
denominator closure.

**Trigger Map:**

| # | Trigger Name | Execution Tier | Anomaly Flag | Spawns |
|---|-------------|---------------|-------------|--------|

**Denominator Closure:** firing + non-firing + unresolved = N →
CLOSED / GAP DETECTED `[RECON MISS | FM-22]`

**CLOSURE CHECK:**

| Obligation | Counter | Must-Be |
|------------|---------|---------|
| ART-03 EOR citations missing from sync entries | 0 | 0 |
| Gap entries missing counterfactual | 0 | 0 |
| Entries missing side-effect slot | 0 | 0 |
| Cascade entries missing Depth counter | 0 | 0 |
| PROHIBITION BREACHES | 0 | 0 |
| Denominator closure status | CLOSED | CLOSED |

**Exit condition:** Phase 6 SHALL be complete when trigger map covers all triggers and denominator
closure is stated with CLOSED or GAP DETECTED.

---

## V-02

**Variation axis:** Output format — vertical obligation record blocks instead of table rows

**Hypothesis:** Phase 0 obligations appear as OBLIGATION RECORD blocks: each obligation is a
titled block with all six metadata fields as labeled slots. All six metadata types (status,
refutation, weaker alternative, failure mode, activation event, producing role) are co-located
per obligation, satisfying C-32's intent. However, the rubric requires a "single named
pre-enumeration registry" with "at least 6 typed columns" — the word "columns" implies a table
structure. Vertical blocks are a weak pass at best. Failure modes in this variation still use
consequence language ("scope boundaries become unverifiable," "enforcement becomes unpredictable"),
naming consequences rather than absent structural properties. C-33 fails.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to
`Inactive` (1). Determine which automations fire, in what order, with what inputs and outputs,
and identify all trigger pathologies.

Execute phases in strict sequence.

---

### PROTOCOL PREAMBLE

*(Platform Term Contract, FM Catalog, and Entry Schema Contract identical to V-01.)*

---

### PHASE 0 — PREPARATION

**Entry condition:** Phase 0 SHALL begin when scenario specification is received.

**Job:** Produce and lock all pre-enumeration obligations. Each obligation is presented as a
NAMED OBLIGATION RECORD with all six metadata slots populated. Phase 0 SHALL issue exit signal
when all records carry Status: SATISFIED.

**BREACH TOKEN PROTOCOL:** `[PROHIBITION BREACH: Role | {prohibition name} | FM-NN]`

---

**OBLIGATION RECORD: SCOPE GATE**
- Status: SATISFIED
- Refutation Condition: Violated if any candidate is named before event tuple (entity, operation,
  field, values) appears
- Weaker Alternative: State scope in an opening prose sentence
- Failure Mode: Scope boundaries become unverifiable when recorded informally — a reviewer must
  re-read narrative prose to determine whether a given trigger qualifies, producing divergent
  interpretations
- Activation Event: N/A — scope gate is a static pre-execution declaration
- Producing Role: Auditor | Phase 0

Scope gate values: entity=account | operation=Update | field=statecode | prev=Active(0) | new=Inactive(1)

---

**OBLIGATION RECORD: EXCLUSION LOG**
- Status: SATISFIED
- Refutation Condition: Violated if any automation layer has no named disposition before candidates
  are named
- Weaker Alternative: List only what fired; omit unscanned layers
- Failure Mode: Layer audit gaps create conditions where undetected false positives pass
  unnoticed — a reviewer cannot distinguish a missing trigger from a layer that was never scanned
- Activation Event: N/A — exclusion log is complete before candidate naming
- Producing Role: Auditor | Phase 0

Layer sweep: Classic workflows EXCLUDED (deprecated) | Scheduled flows EXCLUDED (no field trigger)
| Instant flows EXCLUDED (manual trigger) | Sync plug-in steps INCLUDED | Async plug-in steps
INCLUDED | Automated cloud flows INCLUDED

---

**OBLIGATION RECORD: EOR TABLE**
- Status: SATISFIED
- Refutation Condition: Violated if any firing entry is ordered without citing a named rule ID
- Weaker Alternative: State ordering principles in prose before enumeration
- Failure Mode: Entry positions become unverifiable — a reader cannot confirm whether position
  follows the stated rule or is arbitrary when no rule ID is cited
- Activation Event: N/A — EOR table is a static one-time declaration
- Producing Role: Domain Expert | Phase 0

EOR-01: Sync plug-in steps before async (same change event) | EOR-02: Within sync tier, lower rank
fires first | EOR-03: Async and flow entries — relative order not guaranteed

---

**OBLIGATION RECORD: CASCADE DEPTH BUDGET**
- Status: SATISFIED
- Refutation Condition: Violated if any cascade chain entry lacks a [Depth: N/MAX] counter
- Weaker Alternative: Trace cascade chains without an explicit depth constraint
- Failure Mode: Runaway chains become invisible — without a named budget, infinite recursion
  cannot be detected by counter inspection alone
- Activation Event: Activates at Phase 4 cascade tracing
- Producing Role: Domain Expert | Phase 0

MAX_DEPTH = 5. Overflow marker: `[DEPTH EXCEEDED: CH-NN]`

---

**OBLIGATION RECORD: PROHIBITION CONTRACTS**
- Status: SATISFIED
- Refutation Condition: Violated if any prohibition lacks a named "Applies After" event
  referencing a Phase 0 lifecycle transition
- Weaker Alternative: State role prohibitions without temporal scope ("Domain Expert may not
  add candidates")
- Failure Mode: Enforcement becomes unpredictable — without a named activation event, whether
  a prohibition is currently active requires implicit knowledge of phase sequencing rather than
  reading the contract
- Activation Event: N/A — prohibition contracts are declared before roles become active
- Producing Role: Auditor | Phase 0

Prohibitions:
- Domain Expert MAY NOT add candidates *after denominator declaration (Phase 1)*
- Classifier MAY NOT modify SCOPE GATE fields *after Phase 0 exit signal*

---

**OBLIGATION RECORD: ARTIFACT MANIFEST**
- Status: SATISFIED
- Refutation Condition: Violated if any manifest entry lacks producing role AND producing phase
  as named fields
- Weaker Alternative: List required artifacts as bullet points without role attribution
- Failure Mode: Production accountability becomes irresolvable — when an artifact is absent,
  no named role can be held responsible without explicit attribution
- Activation Event: N/A — manifest is a static pre-enumeration declaration
- Producing Role: Auditor | Phase 0

| ART-ID | Artifact | Producing Role | Phase |
|--------|----------|---------------|-------|
| ART-01 | SCOPE GATE | Auditor | 0 |
| ART-02 | EXCLUSION LOG | Auditor | 0 |
| ART-03 | EOR TABLE | Domain Expert | 0 |
| ART-04 | CASCADE DEPTH BUDGET | Domain Expert | 0 |
| ART-05 | PROHIBITION CONTRACTS | Auditor | 0 |
| ART-06 | BREACH TOKEN PROTOCOL | Auditor | 0 |

---

**Phase 0 Exit Signal:** 6/6 SATISFIED — Phase 1 may begin.

**Exit condition:** Phase 0 SHALL be complete when all 6 obligation records carry Status:
SATISFIED and exit signal is issued.

---

### STRUCTURAL INVARIANT LAYER

*(Identical to V-01 — Invariants 1 through 5.)*

---

### LIFECYCLE OVERVIEW

*(Identical to V-01 — Phases 0 through 6.)*

---

### Phase 1 — Pre-scan

*(Identical to V-01.)*

---

### Phase 2 — Sync Trigger Enumeration

*(Identical to V-01.)*

---

### Phase 3 — Async Trigger Enumeration

*(Identical to V-01.)*

---

### Phase 4 — Cascade Tracing

*(Identical to V-01.)*

---

### Phase 5 — Anomaly Assessment

*(Identical to V-01.)*

---

### Phase 6 — Trigger Map and Closure

*(Identical to V-01.)*

---

## V-03

**Variation axis:** Role sequence — Auditor sub-phase (0a) produces governance artifacts; Domain
Expert sub-phase (0b) produces execution artifacts. Obligation metadata spans role boundaries.
INERTIA CONTRAST names structural absences.

**Hypothesis:** Phase 0 is split into two sub-phases with separate role-owned tables. The metadata
(status, refutation, producing role/phase) is present in each table, but Activation Event and
Weaker Alternative / Failure Mode are in a separate INERTIA CONTRAST section at the end of Phase 0.
To audit one obligation's compliance a reader must cross sub-phase 0a table + INERTIA CONTRAST
section. C-32 fails. INERTIA CONTRAST failure modes name structural absences ("scope boundary is
not a named structural artifact," "activation window is absent") — closer to constraint-propagating
but still one reasoning hop from the pass condition. C-33 weak pass.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to
`Inactive` (1). Determine which automations fire, in what order, with what inputs and outputs,
and identify all trigger pathologies.

Execute phases in strict sequence.

---

### PROTOCOL PREAMBLE

*(Platform Term Contract, FM Catalog, and Entry Schema Contract identical to V-01.)*

---

### PHASE 0 — PREPARATION

**Entry condition:** Phase 0 SHALL begin when scenario received and PROTOCOL PREAMBLE complete.

**Job:** Phase 0 is divided into two sub-phases by role. Sub-phase 0a (Auditor role) produces
structural governance artifacts. Sub-phase 0b (Domain Expert role) produces execution
configuration artifacts. Phase 0 EXIT SIGNAL is issued when all sub-phase obligations are SATISFIED.

**BREACH TOKEN PROTOCOL:** `[PROHIBITION BREACH: Role | {prohibition name} | FM-NN]`

#### Sub-phase 0a — Auditor Role

| Artifact | Status | Refutation Condition | Producing Role | Producing Phase |
|----------|--------|---------------------|---------------|-----------------|
| SCOPE GATE (event tuple) | SATISFIED | Violated if no event tuple (entity, operation, field, values) before any candidate is named | Auditor | 0a |
| EXCLUSION LOG (layer sweep) | SATISFIED | Violated if any automation layer lacks a named disposition | Auditor | 0a |
| PROHIBITION CONTRACTS (with temporal anchors) | SATISFIED | Violated if any prohibition lacks a named "Applies After" lifecycle event | Auditor | 0a |
| BREACH TOKEN PROTOCOL | SATISFIED | Violated if no named breach token format declared before prohibitions active | Auditor | 0a |
| ARTIFACT MANIFEST | SATISFIED | Violated if any manifest entry lacks producing role AND producing phase | Auditor | 0a |

**SCOPE GATE:**
Entity: account | Operation: Update | Field: statecode | Previous: Active (0) | New: Inactive (1)

**EXCLUSION LOG:**
Classic workflows: EXCLUDED (deprecated) | Scheduled flows: EXCLUDED (no field-change trigger) |
Instant flows: EXCLUDED (manual trigger) | Sync plug-in steps: INCLUDED | Async plug-in steps:
INCLUDED | Automated cloud flows: INCLUDED

**PROHIBITION CONTRACTS:**
- Domain Expert MAY NOT add new candidates *after denominator declaration (Phase 1 completion)*
- Classifier MAY NOT modify SCOPE GATE fields *after Phase 0 exit signal*

**ARTIFACT MANIFEST:**

| ART-ID | Artifact Name | Producing Role | Producing Phase |
|--------|--------------|---------------|-----------------|
| ART-01 | SCOPE GATE | Auditor | 0a |
| ART-02 | EXCLUSION LOG | Auditor | 0a |
| ART-03 | EOR TABLE | Domain Expert | 0b |
| ART-04 | CASCADE DEPTH BUDGET | Domain Expert | 0b |
| ART-05 | PROHIBITION CONTRACTS | Auditor | 0a |
| ART-06 | BREACH TOKEN PROTOCOL | Auditor | 0a |

#### Sub-phase 0b — Domain Expert Role

| Artifact | Status | Refutation Condition | Producing Role | Producing Phase |
|----------|--------|---------------------|---------------|-----------------|
| EOR TABLE (with named rule IDs) | SATISFIED | Violated if any firing entry positioned without citing a named rule ID | Domain Expert | 0b |
| CASCADE DEPTH BUDGET (named MAX) | SATISFIED | Violated if any cascade chain entry lacks [Depth: N/MAX] counter | Domain Expert | 0b |

**EOR TABLE:**

| Rule ID | Principle |
|---------|-----------|
| EOR-01 | Sync plug-in steps execute before async steps for same change event |
| EOR-02 | Within sync tier: lower plug-in step rank fires first |
| EOR-03 | Async plug-in steps and automated cloud flows: relative order not guaranteed |

**CASCADE DEPTH BUDGET:** MAX_DEPTH = 5. Overflow: `[DEPTH EXCEEDED: CH-NN]`

---

#### INERTIA CONTRAST

*Why structural attributes are required per obligation — named structural absences:*

**SCOPE GATE (named event tuple vs. prose scope):**
- Weaker alternative: "This analysis covers account statecode changes"
- Failure mode: Scope boundary is not a named structural artifact — without a named event tuple,
  no candidate trigger is structurally excludable; in/out-scope determination requires prose
  interpretation per candidate rather than structural lookup
- Stronger mechanism: Named event tuple (entity, operation, field, values) makes excludability
  a structural property

**PROHIBITION CONTRACTS (with temporal anchor vs. global timeless prohibition):**
- Weaker alternative: "Domain Expert may not add candidates" (no activation event named)
- Failure mode: Activation window is absent — without a named lifecycle event in the "Applies
  After" slot, the constraint's temporal scope is undefined; a role agent cannot determine from
  the contract alone when the prohibition becomes active
- Stronger mechanism: Named "Applies After" field makes the prohibition lifecycle-bound

---

**Phase 0 Exit Signal:** 7/7 SATISFIED across sub-phases 0a and 0b. Phase 1 may begin.

**Exit condition:** Phase 0 SHALL be complete when all sub-phase 0a and 0b obligations are
SATISFIED and exit signal issued.

---

### STRUCTURAL INVARIANT LAYER, LIFECYCLE OVERVIEW, Phases 1–6

*(Identical to V-01.)*

---

## V-04

**Variation axis:** Inertia framing + Output format — single unified table with all six metadata
columns; failure modes name absent structural properties

**Hypothesis:** All Phase 0 obligations appear as rows in one PHASE 0 OBLIGATION REGISTRY table
with six typed columns: Status, Refutation Condition, Weaker Alternative, Failure Mode, Activation
Event, Producing Role. Each row is a complete self-audit record for its obligation — no
cross-table navigation required. C-32 passes. Failure modes name absent structural properties
("anonymous scope boundary," "absent temporal anchor," "unattributed production gap") but stop
short of the "anonymous [X]" convention that makes derivation direct. A reader seeing "absent
temporal anchor" knows a temporal anchor is needed but must still reason to "the Applies After
field must be named" as the mechanism. C-33 weak pass.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to
`Inactive` (1). Determine which automations fire, in what order, with what inputs and outputs,
and identify all trigger pathologies.

Execute phases in strict sequence.

---

### PROTOCOL PREAMBLE

*(Platform Term Contract, FM Catalog, and Entry Schema Contract identical to V-01.)*

---

### PHASE 0 — PREPARATION

**Entry condition:** Phase 0 SHALL begin when scenario specification is received and PROTOCOL
PREAMBLE declared complete.

**Job:** Produce and lock all pre-enumeration obligations. ALL obligation metadata SHALL be
co-located in the PHASE 0 OBLIGATION REGISTRY — a single table with six typed columns. Each row
is the obligation's complete self-audit record. No cross-table navigation is required to assess
any single obligation's compliance.

**BREACH TOKEN PROTOCOL:** `[PROHIBITION BREACH: Role | {prohibition name} | FM-NN]`

#### PHASE 0 OBLIGATION REGISTRY

| Obligation | Status | Refutation Condition | Weaker Alternative | Failure Mode | Activation Event | Producing Role |
|------------|--------|---------------------|--------------------|--------------|-----------------|----------------|
| SCOPE GATE | SATISFIED | Violated if any candidate named before event tuple (entity, operation, field, values) declared | Prose scope sentence in opening paragraph | anonymous scope boundary — event tuple absent; no candidate is structurally excludable | N/A [static pre-execution declaration; no lifecycle event governs timing] | Auditor \| Phase 0 |
| EXCLUSION LOG | SATISFIED | Violated if any automation layer evaluated without named disposition (included/excluded + reason) | List only what fired; omit unscanned layers | anonymous layer gap — unscanned layers produce candidates that cannot be verified as absent | N/A [complete before candidate naming] | Auditor \| Phase 0 |
| EOR TABLE | SATISFIED | Violated if any firing entry positioned without citing a named rule ID | Ordering narrative prose preamble ("sync before async") | absent rule IDs — per-entry position unauditable; no rule citation confirms correct ordering | N/A [one-time static declaration before enumeration] | Domain Expert \| Phase 0 |
| CASCADE DEPTH BUDGET | SATISFIED | Violated if any cascade entry lacks [Depth: N/MAX] counter | Trace chains without depth constraint | invisible overflow — chains exceeding undeclared limits cannot be detected by counter inspection | Activates at Phase 4 cascade tracing | Domain Expert \| Phase 0 |
| PROHIBITION CONTRACTS | SATISFIED | Violated if any prohibition lacks named "Applies After" event referencing a Phase 0 transition | Timeless global prohibition without temporal scope | absent temporal anchor — prohibition's effective period undefined; compliance before activation trivially true | Declared in Phase 0; per-prohibition activation event: see contract body | Auditor \| Phase 0 |
| ARTIFACT MANIFEST | SATISFIED | Violated if any manifest entry lacks producing role AND producing phase as named fields | Bulleted artifact list without role/phase attribution | unattributed production gap — missing artifact cannot be assigned to a responsible role or phase | N/A [static pre-enumeration declaration] | Auditor \| Phase 0 |
| BREACH TOKEN PROTOCOL | SATISFIED | Violated if no named breach token format declared before prohibitions active | Detect violations only through post-hoc rubric evaluation | invisible breach — prohibition violations undetectable from artifact surface without external rubric | Alongside PROHIBITION CONTRACTS in Phase 0 | Auditor \| Phase 0 |

**SCOPE GATE VALUES:**
entity=account | operation=Update | field=statecode | prev=Active(0) | new=Inactive(1)

**EXCLUSION LOG:**
Classic workflows: EXCLUDED (deprecated) | Scheduled flows: EXCLUDED (no field-change trigger) |
Instant flows: EXCLUDED (manual trigger required) | Sync plug-in steps: INCLUDED | Async plug-in
steps: INCLUDED | Automated cloud flows: INCLUDED

**EOR TABLE:**
EOR-01: Sync plug-in steps before async (same change event) | EOR-02: Within sync tier, lower rank
first | EOR-03: Async entries — relative order not guaranteed

**CASCADE DEPTH BUDGET:** MAX_DEPTH = 5. Overflow: `[DEPTH EXCEEDED: CH-NN]`

**PROHIBITION CONTRACTS:**
- Domain Expert MAY NOT add new candidates *after denominator declaration (Phase 1)*
- Classifier MAY NOT modify SCOPE GATE fields *after Phase 0 exit signal*

---

#### INERTIA CONTRAST

*Two mechanisms analyzed — failure modes name absent structural properties:*

**SCOPE GATE (event tuple vs. prose preamble):**
- Weaker alternative: "This analysis covers account statecode changes on the Dataverse platform"
- Failure mode: anonymous scope boundary — the absence of a named event tuple means no candidate
  trigger is structurally excludable; scope membership requires prose interpretation
- What this forces: the mechanism must provide a named boundary definition — at minimum, a
  structural artifact with entity, operation, and field as named fields

**PROHIBITION CONTRACTS (temporal anchor vs. timeless prohibition):**
- Weaker alternative: "Domain Expert may not add candidates" — no lifecycle event named
- Failure mode: absent temporal anchor — the prohibition's effective period is undefined across
  phases; enforcement depends on implied sequencing
- What this forces: the mechanism must carry an explicit lifecycle activation event as a named
  field alongside the prohibition declaration

---

**Phase 0 Exit Signal:** 7/7 SATISFIED — enumeration authorized.

**Exit condition:** Phase 0 SHALL be complete when all 7 registry rows carry Status: SATISFIED
and exit signal is issued.

---

### STRUCTURAL INVARIANT LAYER, LIFECYCLE OVERVIEW, Phases 1–6

*(Identical to V-01.)*

---

## V-05

**Variation axis:** Inertia framing + Output format + Lifecycle emphasis — anonymous-X convention;
unified table; embedded derivation test demonstrating label → pass-condition inference

**Hypothesis:** The PHASE 0 OBLIGATION REGISTRY from V-04 is retained. Failure modes are upgraded
to the "anonymous [X]" naming convention: each label names the structural property whose absence
produces the failure, using the pattern "anonymous [property]" or "absent [named field]." An
embedded DERIVATION TEST subsection in the INERTIA CONTRAST section demonstrates for each
mechanism: label → absent structural property → minimum implementation. A reader who knows only
the failure mode label can derive the mechanism's pass condition without consulting the rubric.
C-32 passes (single table, all 6 columns, explicit N/A-with-reason). C-33 passes (labels
specify absent structural property at constraint-propagation strength; derivation test confirms).

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to
`Inactive` (1). Determine which automations fire, in what order, with what inputs and outputs,
and identify all trigger pathologies.

Execute phases in strict sequence.

---

### PROTOCOL PREAMBLE

*(Platform Term Contract, FM Catalog, and Entry Schema Contract identical to V-01.)*

---

### PHASE 0 — PREPARATION

**Entry condition:** Phase 0 SHALL begin when scenario specification is received and PROTOCOL
PREAMBLE declared complete.

**Job:** Produce and lock all pre-enumeration obligations in the PHASE 0 OBLIGATION REGISTRY.
All six metadata types SHALL appear as typed columns in this single named table. Each row is the
obligation's complete self-audit record — cross-table navigation to assess any single obligation's
compliance is eliminated. Any registry column empty across all rows without an explicit
N/A-with-reason constitutes a structural gap.

**BREACH TOKEN PROTOCOL:** `[PROHIBITION BREACH: Role | {prohibition name} | FM-NN]`

#### PHASE 0 OBLIGATION REGISTRY

| Obligation | Status | Refutation Condition | Weaker Alternative | Failure Mode | Activation Event | Producing Role |
|------------|--------|---------------------|--------------------|--------------|-----------------|----------------|
| SCOPE GATE | SATISFIED | Violated if any candidate is named before event tuple (entity, operation, field, values) appears in a named structural artifact | Prose scope sentence ("analysis covers account statecode changes") | **anonymous scope boundary** — named event tuple absent; no candidate is structurally excludable without it | N/A [scope gate is a static pre-execution declaration; no lifecycle event governs its timing — row is N/A because the obligation exists outside phase sequencing] | Auditor \| Phase 0 |
| EXCLUSION LOG | SATISFIED | Violated if any automation layer has no named disposition (included/excluded + reason) before candidates are named | Enumerate only what fired; leave unscanned layers undocumented | **anonymous layer gap** — named layer disposition absent; unscanned layers produce candidates that cannot be verified as absent vs. present-but-not-firing | N/A [exclusion log is complete before any candidate is named — row is N/A because timing is pre-candidate, not phase-gated] | Auditor \| Phase 0 |
| EOR TABLE | SATISFIED | Violated if any firing entry is positioned without citing a named EOR rule ID inline | Prose ordering paragraph before enumeration ("sync before async") | **anonymous ordering rule** — named rule IDs absent; per-entry position cannot be audited by rule citation; a reader cannot confirm ordering is rule-governed vs. arbitrary | N/A [EOR table is a one-time static declaration — row is N/A because it is declared once, not at a phase transition] | Domain Expert \| Phase 0 |
| CASCADE DEPTH BUDGET | SATISFIED | Violated if any cascade chain entry lacks a [Depth: N/MAX] counter | Trace chains without explicit depth ceiling | **invisible overflow** — named depth budget absent; chains exceeding an undeclared limit produce no detectable counter signal; storm verdict cannot reference depth-exceeded entries | Activates at Phase 4 cascade tracing [row is non-N/A because depth budget is only relevant from Phase 4 onward; declaring it earlier has no enforcement effect] | Domain Expert \| Phase 0 |
| PROHIBITION CONTRACTS | SATISFIED | Violated if any prohibition lacks a named "Applies After" event referencing a Phase 0 lifecycle transition or Phase 1 completion | Timeless global role prohibition ("Domain Expert may not add candidates") | **anonymous prohibition** — temporal activation anchor absent; prohibition's effective period undefined across phases; pre-activation "compliance" is trivially satisfiable and provides no enforcement | N/A [prohibition contracts declared in Phase 0 before roles operate; individual activation events named within contract body — row N/A because the contract artifact has no single activation; each prohibition row in the contract body carries its own] | Auditor \| Phase 0 |
| ARTIFACT MANIFEST | SATISFIED | Violated if any manifest entry lacks both producing role AND producing phase as named fields (either alone is insufficient) | Bulleted artifact checklist without role or phase attribution | **anonymous artifact gap** — producing role and phase absent; a missing artifact cannot be attributed to a specific responsible role and phase; CLOSURE CHECK cannot report "Role X, Phase Y: ABSENT" | N/A [manifest is a static pre-enumeration declaration — row is N/A because the manifest exists outside phase sequencing] | Auditor \| Phase 0 |
| BREACH TOKEN PROTOCOL | SATISFIED | Violated if no named breach token format is declared before PROHIBITION CONTRACTS are active | Detect prohibition violations only through post-hoc rubric re-evaluation of output | **invisible breach** — named breach token format absent; prohibition violations produce no inline signal; a reader scanning the artifact cannot find violations without re-scoring against the rubric | Activates alongside PROHIBITION CONTRACTS [row is non-N/A because the breach token protocol takes effect at the same time prohibitions become active] | Auditor \| Phase 0 |

**SCOPE GATE VALUES:**
entity=account | operation=Update | field=statecode | prev=Active(0) | new=Inactive(1)

**EXCLUSION LOG:**

| Layer | Disposition | Reason |
|-------|-------------|--------|
| Classic Dynamics 365 workflows | EXCLUDED | Deprecated; out of scope for new implementations |
| Scheduled cloud flows | EXCLUDED | No field-change trigger; cron schedules do not fire on record updates |
| Instant cloud flows | EXCLUDED | Require manual trigger initiation; no manual action in this scenario |
| Dataverse sync plug-in steps | INCLUDED | Execute within the originating transaction; eligible candidates |
| Dataverse async plug-in steps | INCLUDED | Execute outside the transaction; eligible candidates |
| Automated cloud flows (Dataverse) | INCLUDED | Trigger on "When a row is added, modified or deleted"; eligible candidates |

**EOR TABLE:**

| Rule ID | Principle |
|---------|-----------|
| EOR-01 | Sync plug-in steps execute before async plug-in steps and automated cloud flows for the same change event |
| EOR-02 | Within sync tier: lower plug-in step rank (as registered in the platform) fires first |
| EOR-03 | Async plug-in steps and automated cloud flows execute outside the transaction; relative order among them is not guaranteed |

**CASCADE DEPTH BUDGET:** MAX_DEPTH = 5. Overflow marker: `[DEPTH EXCEEDED: CH-NN | depth N]`

**PROHIBITION CONTRACTS:**

| Prohibition | Role | Applies After |
|-------------|------|--------------|
| MAY NOT add new candidates to enumeration | Domain Expert | Denominator declaration (Phase 1 completion) |
| MAY NOT modify SCOPE GATE field values | Classifier | Phase 0 exit signal |

**ARTIFACT MANIFEST:**

| ART-ID | Artifact | Producing Role | Producing Phase |
|--------|----------|---------------|-----------------|
| ART-01 | SCOPE GATE | Auditor | Phase 0 |
| ART-02 | EXCLUSION LOG | Auditor | Phase 0 |
| ART-03 | EOR TABLE | Domain Expert | Phase 0 |
| ART-04 | CASCADE DEPTH BUDGET | Domain Expert | Phase 0 |
| ART-05 | PROHIBITION CONTRACTS | Auditor | Phase 0 |
| ART-06 | BREACH TOKEN PROTOCOL | Auditor | Phase 0 |

---

#### INERTIA CONTRAST

*How failure mode labels constrain mechanism implementation — the derivation test:*

**DERIVATION TEST**

Each failure mode label in the PHASE 0 OBLIGATION REGISTRY is specific enough that reading it
alone derives the mechanism's minimum pass condition. The test: given only the failure mode label,
identify the absent structural property, then derive the minimum implementation that prevents it.

| Mechanism | Failure Mode Label | Absent Structural Property | Derived Minimum Implementation |
|-----------|-------------------|---------------------------|-------------------------------|
| SCOPE GATE | **anonymous scope boundary** | Named event tuple | Scope boundary must be a named structural artifact. Minimum: event tuple with entity, operation, and field as named fields. Any mechanism that fails to provide a named tuple leaves the scope boundary anonymous. |
| EXCLUSION LOG | **anonymous layer gap** | Named layer disposition per layer | Each automation layer swept must carry a named disposition. Minimum: table or list where every row names the layer and states included/excluded with reason. Missing rows are anonymous layer gaps. |
| EOR TABLE | **anonymous ordering rule** | Named rule IDs per ordering principle | Each ordering principle must carry a named rule ID. Minimum: table where each row has a rule ID (EOR-NN format). Each firing entry must cite its rule ID inline. Absence of named IDs leaves ordering rules anonymous. |
| PROHIBITION CONTRACTS | **anonymous prohibition** | Temporal activation anchor | Each prohibition must carry a named "Applies After" lifecycle event. Minimum: prohibition contract table with an "Applies After" column. Timeless prohibitions are anonymous — their effective period is unnamed. |
| ARTIFACT MANIFEST | **anonymous artifact gap** | Named producing role AND producing phase | Each manifest entry must carry both producing role and producing phase as named fields. Either field alone is insufficient — a gap with only a role or only a phase is still partially anonymous. Minimum: manifest table with Producing Role and Producing Phase columns. |
| BREACH TOKEN PROTOCOL | **invisible breach** | Named breach token format | A named inline marker format must be declared before prohibitions activate. Minimum: a defined token string (e.g., `[PROHIBITION BREACH: Role | prohibition name | FM-NN]`) that appears inline at point of violation. Absence leaves breaches invisible. |

**Constraint propagation verification:** The complete set of failure mode labels in the registry
collectively specifies all Phase 0 mechanism pass conditions. A reader who reads only the Failure
Mode column of the PHASE 0 OBLIGATION REGISTRY — without consulting the rubric or the Refutation
Condition column — can derive the minimum implementation for every Phase 0 obligation.

---

**Phase 0 Exit Signal:** 7/7 SATISFIED — enumeration authorized.

**Exit condition:** Phase 0 SHALL be complete when all 7 registry rows carry Status: SATISFIED
and exit signal is issued.

---

### STRUCTURAL INVARIANT LAYER

*(Identical to V-01 — Invariants 1 through 5.)*

---

### LIFECYCLE OVERVIEW

*(Identical to V-01 — Phases 0 through 6.)*

---

### Phase 1 — Pre-scan

**Entry condition:** Phase 1 SHALL begin when Phase 0 exit signal is issued.

**Job:** Identify all candidate triggers without condition filtering. Declare denominator N. Open
anomaly question slots. Issue Phrasing Clearance PCC-1.

**Anomaly Questions — Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does this change cause more triggers than the environment can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for account suspension that does not appear? | OPEN |
| Circular Trigger | Does any trigger's output re-activate an upstream trigger? | OPEN |

**Denominator Pre-Scan:**

| Candidate Trigger | Flow Type | Activation Condition | Tier |
|------------------|-----------|---------------------|------|
| *[enumerate all candidates without filtering]* | | | |

N = *[integer — declare before Phase 2]*

**Exit condition:** Phase 1 SHALL be complete when N is declared, all three anomaly slots are
OPEN, and PCC-1 is issued.

---

### Phase 2 — Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when Phase 1 complete, N declared, PCC-1 issued. If
PCC-1 absent: `[ENTRY CONDITION ABSENT: Phase 2 | FM-16]`

**Job:** Enumerate all synchronous triggers using FIRING ENTRY or NON-FIRING ENTRY schema.
Include at least one negative vocabulary example. Order by execution priority per EOR table.

**Negative vocabulary example (required):** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be complete when every sync-tier candidate has a resolved entry
with all schema slots populated.

---

### Phase 3 — Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when Phase 2 complete and Sync Trigger Table produced.

**Job:** Enumerate all async-tier candidates. Annotate latency tier per entry.

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be complete when every async-tier candidate has a resolved entry
with all slots populated.

---

### Phase 4 — Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when Phases 2 and 3 complete.

**Job:** Trace cascade chains from side-effect writes. Assign Chain IDs. Mark final row
`[TERMINAL]`. Carry `[Depth: N/5]` counter per entry. Apply back-edge detection.

**Cascade Chain Table:**

| Chain ID | Depth | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|-------|------|--------------------|-------------------|--------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be complete when all side-effect writes evaluated, all chains
carry Chain-Status, back-edge detection applied.

---

### Phase 5 — Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when Phase 4 complete and all chains carry Chain-Status.

**Job:** Evidence-anchored verdicts for all three anomaly classes. Cite evidence. Every confirmed
anomaly receives at least one remediation step.

**Trigger Storm:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Missing Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Circular Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Exit condition:** Phase 5 SHALL be complete when all three verdicts issued with cited evidence.

---

### Phase 6 — Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when Phase 5 complete and all anomaly verdicts issued.

**Job:** Produce trigger map. Perform denominator closure.

**Trigger Map:**

| # | Trigger Name | Execution Tier | Anomaly Flag | Spawns |
|---|-------------|---------------|-------------|--------|

**Denominator Closure:** firing + non-firing + unresolved = N →
CLOSED / GAP DETECTED `[RECON MISS | FM-22]`

**CLOSURE CHECK:**

| Obligation | Counter | Must-Be |
|------------|---------|---------|
| ART-01 through ART-06: all produced (Auditor/Domain Expert Phase 0) | 6/6 | 6/6 |
| EOR citations missing from sync entries | 0 | 0 |
| Gap entries missing counterfactual | 0 | 0 |
| Entries missing side-effect slot | 0 | 0 |
| Cascade entries missing Depth counter | 0 | 0 |
| PROHIBITION BREACHES | 0 | 0 |
| Denominator closure status | CLOSED | CLOSED |

**Exit condition:** Phase 6 SHALL be complete when trigger map covers all triggers and denominator
closure is stated with CLOSED or GAP DETECTED.
