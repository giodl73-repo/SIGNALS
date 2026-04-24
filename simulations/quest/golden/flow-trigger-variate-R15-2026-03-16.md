---
skill: flow-trigger
round: 15
rubric_version: 12
new_criteria: [C-38, C-39]
date: 2026-03-16
---

# flow-trigger — Round 15 (Rubric v12) Variations

**New criteria this round:**
- **C-38** — Obligation statement self-containment: reading the obligation text column alone (without
  opening producing role, activation event, or refutation columns) yields a complete specification
  of who must do what with what content by when. Labels and category names in the obligation text
  are a weak pass even when other columns are fully populated. A full pass requires the obligation
  text itself to carry: named role + modal verb (SHALL/MUST) + named artifact + temporal constraint.
- **C-39** — Attribution chain design rationale: the output explicitly documents that both
  attribution layers exist, names the artifact where each operates, and explains why both are
  required — so that removing either layer is understood to break remediation self-sufficiency, not
  merely reduce coverage. Extends C-31 (ARTIFACT MANIFEST layer) and C-37 (CLOSURE CHECK layer).

**Round 14 gap analysis:**
- V-01 through V-03 (R14): Obligation column contains artifact name labels only ("EOR TABLE",
  "SCOPE GATE"). C-38 FAIL. CLOSURE CHECK note acknowledges "attribution exists at both points" but
  offers no consequence statement for removal. C-39 FAIL.
- V-04 (R14): Unified registry; N/A-with-reason per cell; "anonymous [X]" labels; DERIVATION TEST
  inside INERTIA CONTRAST; ROLE ACCOUNTABILITY DECLARATION in prose paragraph before counters.
  Obligation column still contains artifact names only. C-38 FAIL. CLOSURE CHECK mentions declaration
  time and detection time but no explanation of why both required or what breaks if either removed.
  C-39 FAIL (two layers named but no design rationale).
- V-05 (R14): All C-34–C-37 PASS. Inline role per counter. Post-counter note reads "Role attribution
  exists at both declaration time (ARTIFACT MANIFEST) and detection time (CLOSURE CHECK counter),
  eliminating the manifest cross-reference..." Obligation column still artifact name labels only.
  C-38 FAIL. C-39 WEAK PASS: names both layers with artifacts; explains that cross-reference is
  eliminated but does not explain what breaks if either layer is absent from future outputs.

**Variation axes:**

| Variation | Axis | C-38 | C-39 |
|-----------|------|------|------|
| V-01 | Role sequence — Domain Expert obligations listed before Auditor; Obligation column carries artifact name labels only; CLOSURE CHECK note names both attribution points but no consequence statement | FAIL | FAIL |
| V-02 | Output format — vertical record blocks; Obligation text carries role + SHALL + artifact but no temporal constraint; CLOSURE CHECK note names both attribution layers and their artifacts but no removal consequence | WEAK PASS | WEAK PASS |
| V-03 | Lifecycle emphasis — unified table with extended lifecycle narrative; Obligation column carries complete self-contained clauses (role + SHALL + artifact + temporal constraint); CLOSURE CHECK note names both layers and artifacts but still no removal consequence | PASS | WEAK PASS |
| V-04 | Phrasing register — formal imperative throughout; Obligation clauses uniformly imperative; ATTRIBUTION CHAIN DESIGN RATIONALE section after CLOSURE CHECK names both artifacts, explains why both required, states what breaks if either removed | PASS | PASS |
| V-05 | Full combination — complete obligation clauses; attribution rationale co-located inline within CLOSURE CHECK block; "removing either layer is understood to break remediation self-sufficiency, not merely reduce coverage" language explicit | PASS | PASS |

**Scenario used in all variations:** A Dynamics 365 Sales `account` record's `statecode` field
changes from `Active` (0) to `Inactive` (1).

---

## V-01

**Variation axis:** Role sequence — Domain Expert obligations listed before Auditor obligations
in the PHASE 0 OBLIGATION REGISTRY; Obligation column carries artifact name labels only (no
self-contained spec clause); CLOSURE CHECK carries inline role per counter (C-37 PASS) but
post-counter note names both attribution points without explaining why both are required.

**Hypothesis:** The PHASE 0 OBLIGATION REGISTRY reorders rows so Domain Expert obligations (EOR
TABLE, CASCADE DEPTH BUDGET) appear before Auditor obligations (SCOPE GATE, EXCLUSION LOG,
PROHIBITION CONTRACTS, ARTIFACT MANIFEST, BREACH TOKEN PROTOCOL). This role sequence variation
has no scoring effect but makes the ordering asymmetry visible. The Obligation column carries the
artifact category name ("EOR TABLE", "SCOPE GATE") — sufficient to identify what is being declared
but not who declares it, with what modal verb, or by when. Reading the Obligation column alone
yields the artifact category; consulting Producing Role and Activation Event columns is required
to determine the complete specification. C-38 FAIL: category labels are present; complete spec
clauses are absent. The CLOSURE CHECK carries per-counter inline role attribution (C-37 PASS from
R14). A post-counter italicized note reads: "Role attribution exists at both declaration time
(ARTIFACT MANIFEST) and detection time (CLOSURE CHECK counter)." Both layers are named; their
artifacts are named. But no consequence statement appears — removing either layer is not explained
as a loss of remediation self-sufficiency. C-39 FAIL: design rationale absent; the note is a
structural observation, not a requirement statement.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to
`Inactive` (1). Determine which automations fire, in what order, with what inputs and outputs,
and identify all trigger pathologies (storms, missing triggers, circular triggers).

ALL phases SHALL execute in strict sequence. Each phase SHALL be declared complete before the
next SHALL begin.

---

### PROTOCOL PREAMBLE

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
| FM-17 | Gate Register Drift | Gate statement uses descriptive language where SHALL/MUST required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All |
| FM-18 | No sync/async structural split | Sync and async triggers in separate phases | `[SPLIT MISS \| FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied to adjacency structure | `[BACKTRACK MISS \| FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each cascade chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN \| FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every violation marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure: firing + non-firing + unresolved = N | `[RECON MISS \| FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing trigger entry | `[SE MISS: trigger-name \| FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade-link columns | `[MAP MISS \| FM-25]` | 6 |

*FM-21 is self-referential: any violation marker appearing without an FM code is itself an
FM-21 violation.*

#### Entry Schema Contract

All trigger entries SHALL conform to one schema. A blank named slot is a structural gap.

**FIRING ENTRY** (all slots required):
```
Trigger Name:
Flow Type:          [automated cloud flow | instant cloud flow | Dataverse plug-in | ...]
Execution Tier:     [sync | async | scheduled]
Trigger Event:
Input Fields:       [specific named fields]
Output Action:      [specific action]
Side Effects:       [field writes beyond primary output, or "none"]
Condition (Taken):  [what must be true for this trigger to fire]
Condition (Skipped):[what would cause this trigger NOT to fire in this scenario]
EOR Citation:       [EOR-NN]
Registration:       [artifact name or UNWITNESSED]
Depth:              [N/MAX or N/A]
Anomaly Flag:       [none | storm | missing | circular]
```

**NON-FIRING ENTRY** (all slots required):
```
Trigger Name:
Flow Type:
Reason Not Firing:  [specific condition excluding this trigger]
Condition (Taken):  [what would cause this trigger to fire]
Condition (Skipped):[what IS true in this scenario that blocks this trigger]
Counterfactual:     [flip condition: what would cause this to fire]
Registration:       [artifact name or UNWITNESSED]
```

---

### PHASE 0 — PREPARATION

**Entry condition:** Phase 0 SHALL begin when scenario specification is received and PROTOCOL
PREAMBLE declared complete.

**Job:** Phase 0 SHALL produce and lock all pre-enumeration obligations in the PHASE 0 OBLIGATION
REGISTRY before Phase 1 begins. The registry is a unified table. Each row carries all six metadata
types as named columns.

**BREACH TOKEN PROTOCOL:** `[PROHIBITION BREACH: Role | {prohibition name} | FM-NN]`

#### PHASE 0 OBLIGATION REGISTRY

| Obligation | Status | Refutation Condition | Weaker Alternative | Failure Mode | Activation Event | Producing Role |
|------------|--------|---------------------|--------------------|--------------|-----------------|----------------|
| EOR TABLE | SATISFIED | Violated if any firing entry is positioned without an inline EOR rule ID citation | Ordering rationale stated as prose ("sync before async") | **anonymous ordering rule** — rule IDs absent; per-entry position unauditable by rule citation | N/A (static pre-enumeration declaration; no lifecycle transition activates it) | Domain Expert \| Phase 0 |
| CASCADE DEPTH BUDGET | SATISFIED | Violated if any cascade entry lacks a [Depth: N/MAX] counter | Trace chains without a named depth ceiling | **invisible overflow** — depth budget absent; chains exceeding undeclared limit produce no counter signal | Activates at Phase 4 cascade tracing | Domain Expert \| Phase 0 |
| SCOPE GATE | SATISFIED | Violated if any candidate is named before the event tuple (entity, operation, field, prev value, new value) appears as a named structural artifact | Prose scope sentence naming the change context | **anonymous scope boundary** — event tuple absent; no candidate structurally excludable; scope requires prose interpretation | N/A (static pre-execution declaration; exists before any phase begins by construction) | Auditor \| Phase 0 |
| EXCLUSION LOG | SATISFIED | Violated if any automation layer is evaluated without a named disposition row before candidates are listed | Enumerate only what fired; leave unscanned layers undocumented | **anonymous layer gap** — named disposition absent; unscanned layers produce candidates that cannot be confirmed absent vs. present-but-not-firing | N/A (complete before any candidate is named; timing is pre-candidate by construction) | Auditor \| Phase 0 |
| PROHIBITION CONTRACTS | SATISFIED | Violated if any prohibition lacks a named Applies After event referencing a Phase 0 or Phase 1 lifecycle transition | Timeless global prohibition without lifecycle scope | **anonymous prohibition** — temporal activation anchor absent; effective period undefined; enforcement depends on phase-ordering inference | N/A (artifact-level row; each prohibition within carries its own Applies After field) | Auditor \| Phase 0 |
| ARTIFACT MANIFEST | SATISFIED | Violated if any manifest entry lacks BOTH producing role AND producing phase as named fields | Artifact checklist with IDs but no role or phase attribution | **anonymous artifact gap** — producing role and phase absent; missing artifact cannot be attributed to responsible role and phase | N/A (static pre-enumeration declaration; no lifecycle event triggers creation) | Auditor \| Phase 0 |
| BREACH TOKEN PROTOCOL | SATISFIED | Violated if no named breach token format is declared before PROHIBITION CONTRACTS are active | Detect prohibition violations only through post-hoc rubric re-evaluation | **invisible breach** — named token format absent; violations produce no inline signal; undetectable without external rubric | Activates alongside PROHIBITION CONTRACTS (Phase 0) | Auditor \| Phase 0 |

**SCOPE GATE VALUES:**
entity=account | operation=Update | field=statecode | prev=Active(0) | new=Inactive(1)

**EXCLUSION LOG:**

| Layer | Disposition | Reason |
|-------|-------------|--------|
| Classic Dynamics 365 workflows | EXCLUDED | Deprecated; not in scope for new implementations |
| Scheduled cloud flows | EXCLUDED | No field-change trigger; cron does not fire on record update |
| Instant cloud flows | EXCLUDED | Manual trigger required; no manual action in scenario |
| Dataverse sync plug-in steps | INCLUDED | Execute within transaction; eligible candidates |
| Dataverse async plug-in steps | INCLUDED | Execute outside transaction; eligible candidates |
| Automated cloud flows (Dataverse) | INCLUDED | Trigger on: When a row is added, modified or deleted |

**EOR TABLE:**

| Rule ID | Principle |
|---------|-----------|
| EOR-01 | Sync plug-in steps SHALL execute before async plug-in steps and automated cloud flows for the same change event |
| EOR-02 | Within sync tier: lower plug-in step rank (as registered) SHALL fire first |
| EOR-03 | Async plug-in steps and automated cloud flows execute outside transaction; relative order SHALL NOT be stated as deterministic |

**CASCADE DEPTH BUDGET:** MAX_DEPTH = 5. Overflow: `[DEPTH EXCEEDED: CH-NN | depth N]`

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

**SCOPE GATE (event tuple vs. prose preamble):**
- Weaker alternative: Narrative sentence naming the change context — no named structural artifact
- Failure mode: **anonymous scope boundary** — the mechanism SHALL provide a named event tuple;
  prose sentences are not named structural artifacts; scope membership requires prose interpretation

**PROHIBITION CONTRACTS (temporal anchor vs. timeless prohibition):**
- Weaker alternative: Global prohibition without lifecycle reference
- Failure mode: **anonymous prohibition** — the mechanism SHALL carry a named Applies After
  lifecycle event; timeless prohibitions provide no named activation point; enforcement depends on
  phase-ordering inference

**ARTIFACT MANIFEST (role-attributed vs. ID-only):**
- Weaker alternative: Artifact list with IDs but no producing role or phase columns
- Failure mode: **anonymous artifact gap** — the mechanism SHALL carry both producing role AND
  producing phase as named fields; a gap with no role attribution cannot be remediated from the
  manifest alone

**DERIVATION TEST**

*Demonstrates constraint propagation from failure mode label to minimum implementation:*

| Failure Mode Label | Absent Structural Property | Derived Minimum Implementation |
|-------------------|---------------------------|-------------------------------|
| **anonymous scope boundary** | Named event tuple as structural artifact with named fields | Scope boundary SHALL be a named artifact. Minimum: structural artifact with entity, operation, field, prev-value, new-value as named fields. A prose sentence is insufficient. |
| **anonymous layer gap** | Named disposition row per automation layer swept | Each layer swept SHALL carry a named disposition row. Minimum: table where every row names layer, disposition, and reason. A missing row is an anonymous layer gap. |
| **anonymous ordering rule** | Named rule ID per ordering principle | Each ordering principle SHALL carry an assigned rule ID. Minimum: table with rule ID column. Each firing entry SHALL cite its rule ID inline. Prose ordering statements are anonymous. |
| **anonymous prohibition** | Named temporal activation anchor ("Applies After" field) | Each prohibition SHALL carry a named Applies After event. Minimum: prohibition table with Applies After column. Timeless prohibitions are anonymous. |
| **anonymous artifact gap** | Named producing role AND named producing phase | Each manifest entry SHALL carry both fields. Either alone is insufficient. Minimum: manifest table with Producing Role and Producing Phase columns, both populated. |
| **invisible breach** | Named breach token format declared before prohibitions activate | A named token string SHALL be declared and used inline at point of violation. Without it, breaches are invisible to document-level scan. |

**Constraint propagation verification:** A reader who reads only the Failure Mode column SHALL be
able to derive the minimum implementation for every Phase 0 obligation without rubric access.

---

**Phase 0 Exit Signal:** 7/7 SATISFIED — enumeration authorized.

**Exit condition:** Phase 0 SHALL be complete when all 7 registry rows carry Status: SATISFIED
and exit signal is issued.

---

### STRUCTURAL INVARIANT LAYER

**Invariant 1 — Phase body completeness:** Every phase body SHALL contain entry condition, job
description, and exit condition. Violation: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`

**Invariant 2 — Gate statement register:** All gate statements SHALL use SHALL/MUST in the
obligation position. Violation: `[GATE REGISTER DRIFT: Phase N | FM-17]`

**Invariant 3 — Denominator closure:** Candidate count N declared in Phase 1 SHALL reconcile
after Phase 3: firing + non-firing + unresolved = N. Violation: `[RECON MISS | FM-22]`

**Invariant 4 — FM code in every marker:** Every violation marker SHALL include its FM catalog
code. Violation: `[FM-21]`

**Invariant 5 — Uniform slot mandate:** Every named slot in every entry schema template is
required. An empty named slot is a structural gap equivalent to a missing entry.

---

### LIFECYCLE OVERVIEW

| Phase | Name | Entry Condition | Job | Exit Condition |
|-------|------|-----------------|-----|----------------|
| 0 | Preparation | Scenario received; PROTOCOL PREAMBLE complete | Produce and lock Phase 0 artifacts; issue exit signal | 7/7 obligations SATISFIED; exit signal issued |
| 1 | Pre-scan | Phase 0 exit signal issued | Identify candidates; declare N; open anomaly slots; issue PCC-1 | N declared; three anomaly slots OPEN; PCC-1 issued |
| 2 | Sync Enumeration | Phase 1 complete; N declared; PCC-1 issued | Enumerate sync-tier candidates; include negative vocabulary example | All sync-tier candidates resolved with all slots populated |
| 3 | Async Enumeration | Phase 2 complete; Sync Trigger Table produced | Enumerate async-tier candidates; annotate latency tier | All async-tier candidates resolved with all slots populated |
| 4 | Cascade Tracing | Phases 2 and 3 complete | Trace cascade chains; Chain IDs; depth counters; back-edge detection; TERMINAL markers | All side-effect writes evaluated; all chains carry Chain-Status |
| 5 | Anomaly Assessment | Phase 4 complete; all chains carry Chain-Status | Evidence-anchored verdicts for all three anomaly classes; remediation per confirmed anomaly | All three verdicts issued with cited rows; confirmed anomalies remediated |
| 6 | Trigger Map and Closure | Phase 5 complete; all anomaly verdicts issued | Produce trigger map; denominator closure; CLOSURE CHECK | Trigger map complete; closure stated; CLOSURE CHECK issued |

---

### Phase 1 — Pre-scan

**Entry condition:** Phase 1 SHALL begin when Phase 0 exit signal is issued.

**Job:** Identify all candidate triggers without condition filtering. Declare denominator N. Open
all three anomaly question slots. Issue Phrasing Clearance PCC-1 if zero register violations found.

**Anomaly Questions — Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does this change cause more triggers than the environment can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for account inactivation that does not fire? | OPEN |
| Circular Trigger | Does any trigger's output re-activate an upstream trigger? | OPEN |

**Denominator Pre-Scan:**

| Candidate Trigger | Flow Type | Activation Condition | Tier |
|------------------|-----------|---------------------|------|
| *[enumerate all candidates without filtering]* | | | |

N = *[integer — declare before Phase 2]*

**PCC-1:** Issued when zero FM-08/FM-16/FM-17 markers found in Phase 0 and preamble.

**Exit condition:** Phase 1 SHALL be complete when N is declared, all three anomaly slots are OPEN,
and PCC-1 is issued.

---

### Phase 2 — Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when Phase 1 complete, N declared, PCC-1 issued.

**Job:** Enumerate all synchronous triggers using FIRING ENTRY or NON-FIRING ENTRY schema. Include
at least one negative vocabulary example. Order by execution priority per EOR table.

**Negative vocabulary example (required):** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | EOR Citation | Registration | Depth | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|-------------|-------|-------------|

**Exit condition:** Phase 2 SHALL be complete when every sync-tier candidate has a resolved entry
with all schema slots populated.

---

### Phase 3 — Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when Phase 2 complete and Sync Trigger Table produced.

**Job:** Enumerate all async-tier candidates. Annotate latency tier per entry.

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | EOR Citation | Registration | Depth | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|-------------|-------|-------------|

**Exit condition:** Phase 3 SHALL be complete when every async-tier candidate has a resolved entry
with all slots populated.

---

### Phase 4 — Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when Phases 2 and 3 complete and both tables produced.

**Job:** Trace cascade chains from side-effect field writes. Assign Chain IDs (CH-01, CH-02, ...).
Apply `[Depth: N/5]` counter per cascade entry. Apply back-edge detection. Mark final chain row
`[TERMINAL]`. Issue `[DEPTH EXCEEDED: CH-NN]` if any chain exceeds MAX_DEPTH.

**Cascade Chain Table:**

| Chain ID | Depth | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|-------|--------------------|--------------------|--------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be complete when all side-effect writes evaluated, all chains
carry Chain-Status, back-edge detection applied.

---

### Phase 5 — Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when Phase 4 complete and all chains carry Chain-Status.

**Job:** Evidence-anchored verdicts for all three anomaly classes. Cite specific trigger rows.
Propose remediation per confirmed anomaly. Produce adjacency list (trigger graph).

**Trigger Storm:** Evidence: *[rows]* | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Missing Trigger:** Evidence: *[rows]* | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Circular Trigger:** Evidence: *[rows]* | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Exclusion log reference:** *[cite ART-02 entries supporting verdict scope]*

**Exit condition:** Phase 5 SHALL be complete when all three verdicts are issued with cited evidence
and every confirmed anomaly has at least one remediation.

---

### Phase 6 — Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when Phase 5 complete and all anomaly verdicts issued.

**Job:** Produce trigger map. Perform denominator closure. Issue CLOSURE CHECK.

**Trigger Map:**

| # | Trigger Name | Execution Tier | Anomaly Flag | Cascade Link |
|---|-------------|---------------|-------------|-------------|

**Denominator Closure:** *[firing] + [non-firing] + [unresolved]* = N -> CLOSED / GAP DETECTED
`[RECON MISS | FM-22]`

**CLOSURE CHECK:**

```
EOR citations missing from firing entries:                            {count} [must be 0]
Gap entries missing counterfactual:                                   {count} [must be 0]
Entries missing registration witness:                                 {count} [must be 0]
Cascade entries missing Depth counter:                                {count} [must be 0]
Depth-exceeded chains unresolved:                                     {count} [must be 0]
ART-01 (SCOPE GATE)            — Auditor, Phase 0:        PRODUCED [must be PRODUCED]
ART-02 (EXCLUSION LOG)         — Auditor, Phase 0:        PRODUCED [must be PRODUCED]
ART-03 (EOR TABLE)             — Domain Expert, Phase 0:  PRODUCED [must be PRODUCED]
ART-04 (CASCADE DEPTH BUDGET)  — Domain Expert, Phase 0:  PRODUCED [must be PRODUCED]
ART-05 (PROHIBITION CONTRACTS) — Auditor, Phase 0:        PRODUCED [must be PRODUCED]
ART-06 (BREACH TOKEN PROTOCOL) — Auditor, Phase 0:        PRODUCED [must be PRODUCED]
PROHIBITION BREACHES:                                                 0 [must be 0]
```

*Role attribution exists at both declaration time (ARTIFACT MANIFEST) and detection time
(CLOSURE CHECK counter).*

**Exit condition:** Phase 6 SHALL be complete when trigger map covers all triggers with required
columns and closure check is stated.

---

## V-02

**Variation axis:** Output format — Phase 0 obligations presented as vertical record blocks
(not a unified table); Obligation text in each block carries role + SHALL + artifact but no
temporal constraint; CLOSURE CHECK note names both attribution layers and their artifacts but
stops short of explaining why both are required.

**Hypothesis:** The Phase 0 obligation format changes from a unified table to vertical record
blocks — each block is a self-contained structured record with labeled fields. This satisfies
C-32 as a WEAK PASS: all six metadata types are present per obligation but in vertical format,
not tabular columns. The Obligation text field in each block reads "The [Role] SHALL produce
the [ARTIFACT]" — naming the role, the modal verb, and the artifact. The temporal constraint
("during Phase 0," "before Phase 1 begins") is absent. C-38 WEAK PASS: the text carries three
of the four required elements (who + SHALL + artifact) but not the temporal element ("by when").
A reader consulting only the obligation text field cannot determine when the obligation must be
satisfied. The CLOSURE CHECK carries per-counter inline role attribution (C-37 PASS). A post-
counter note reads: "Role attribution operates at two structural time points. Declaration time:
the ARTIFACT MANIFEST names the producing role and phase as a pre-enumeration commitment.
Detection time: each CLOSURE CHECK counter above names the producing role and phase inline.
Both attribution points are present in this output and both artifacts are named." C-39 WEAK PASS:
names both layers, names the artifacts where each operates, but does not explain what happens if
either layer is removed — the note is a structural inventory, not a design rationale.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to
`Inactive` (1). Determine which automations fire, in what order, with what inputs and outputs,
and identify all trigger pathologies.

ALL phases SHALL execute in strict sequence. Each phase SHALL be declared complete before the
next SHALL begin.

---

### PROTOCOL PREAMBLE

*(Platform Term Contract, FM Catalog, and Entry Schema Contract identical to V-01.)*

---

### PHASE 0 — PREPARATION

**Entry condition:** Phase 0 SHALL begin when scenario specification is received and PROTOCOL
PREAMBLE declared complete.

**Job:** Phase 0 SHALL produce and lock all pre-enumeration obligations. Each obligation is
recorded as a vertical record block. Each block contains all six metadata types as labeled
fields. The complete set of blocks constitutes the PHASE 0 OBLIGATION REGISTRY.

**BREACH TOKEN PROTOCOL:** `[PROHIBITION BREACH: Role | {prohibition name} | FM-NN]`

---

**OBLIGATION: SCOPE GATE**

```
Obligation Text:      The Auditor SHALL produce the SCOPE GATE
Status:               SATISFIED
Refutation:           Violated if any candidate named before event tuple declared as named artifact
Weaker Alternative:   Prose scope sentence naming the change context
Failure Mode:         anonymous scope boundary — event tuple absent; no candidate structurally
                      excludable; scope requires prose interpretation
Activation Event:     N/A (static pre-execution declaration; no lifecycle transition activates it)
Producing Role:       Auditor | Phase 0
```

**OBLIGATION: EXCLUSION LOG**

```
Obligation Text:      The Auditor SHALL produce the EXCLUSION LOG
Status:               SATISFIED
Refutation:           Violated if any automation layer evaluated without named disposition row
Weaker Alternative:   Enumerate only what fired; leave unscanned layers undocumented
Failure Mode:         anonymous layer gap — disposition absent; unscanned layers produce candidates
                      that cannot be confirmed absent vs. present-but-not-firing
Activation Event:     N/A (complete before any candidate named; pre-candidate by construction)
Producing Role:       Auditor | Phase 0
```

**OBLIGATION: EOR TABLE**

```
Obligation Text:      The Domain Expert SHALL produce the EOR TABLE
Status:               SATISFIED
Refutation:           Violated if any firing entry positioned without inline EOR rule ID citation
Weaker Alternative:   Ordering rationale stated as prose before enumeration
Failure Mode:         anonymous ordering rule — rule IDs absent; per-entry position unauditable
                      by rule citation
Activation Event:     N/A (one-time static declaration; no lifecycle transition activates it)
Producing Role:       Domain Expert | Phase 0
```

**OBLIGATION: CASCADE DEPTH BUDGET**

```
Obligation Text:      The Domain Expert SHALL produce the CASCADE DEPTH BUDGET
Status:               SATISFIED
Refutation:           Violated if any cascade entry lacks a [Depth: N/MAX] counter
Weaker Alternative:   Trace chains without named depth ceiling
Failure Mode:         invisible overflow — depth budget absent; chains exceeding undeclared limit
                      produce no counter signal
Activation Event:     Activates at Phase 4 cascade tracing
Producing Role:       Domain Expert | Phase 0
```

**OBLIGATION: PROHIBITION CONTRACTS**

```
Obligation Text:      The Auditor SHALL produce PROHIBITION CONTRACTS
Status:               SATISFIED
Refutation:           Violated if any prohibition lacks a named Applies After event
Weaker Alternative:   Timeless global prohibition without lifecycle scope
Failure Mode:         anonymous prohibition — temporal activation anchor absent; enforcement
                      depends on phase-ordering inference
Activation Event:     N/A (artifact-level row; each prohibition within carries its own Applies
                      After field)
Producing Role:       Auditor | Phase 0
```

**OBLIGATION: ARTIFACT MANIFEST**

```
Obligation Text:      The Auditor SHALL produce the ARTIFACT MANIFEST
Status:               SATISFIED
Refutation:           Violated if any manifest entry lacks both producing role AND producing phase
Weaker Alternative:   Artifact checklist with IDs but no role or phase attribution
Failure Mode:         anonymous artifact gap — producing role and phase absent; missing artifact
                      cannot be attributed to responsible role and phase
Activation Event:     N/A (static pre-enumeration declaration; no lifecycle event triggers creation)
Producing Role:       Auditor | Phase 0
```

**OBLIGATION: BREACH TOKEN PROTOCOL**

```
Obligation Text:      The Auditor SHALL produce the BREACH TOKEN PROTOCOL
Status:               SATISFIED
Refutation:           Violated if no named breach token format declared before prohibitions active
Weaker Alternative:   Detect violations only through post-hoc rubric re-evaluation
Failure Mode:         invisible breach — named token format absent; violations produce no inline
                      signal; undetectable without external rubric
Activation Event:     Activates alongside PROHIBITION CONTRACTS (Phase 0)
Producing Role:       Auditor | Phase 0
```

*(SCOPE GATE VALUES, EXCLUSION LOG, EOR TABLE, CASCADE DEPTH BUDGET, PROHIBITION CONTRACTS,
ARTIFACT MANIFEST identical to V-01.)*

---

#### INERTIA CONTRAST

*(Failure modes, DERIVATION TEST, and constraint propagation verification identical to V-01.)*

---

**Phase 0 Exit Signal:** 7/7 SATISFIED — enumeration authorized.

**Exit condition:** Phase 0 SHALL be complete when all 7 obligation blocks carry Status: SATISFIED
and exit signal is issued.

---

### STRUCTURAL INVARIANT LAYER, LIFECYCLE OVERVIEW, Phases 1–5

*(Identical to V-01.)*

---

### Phase 6 — Trigger Map and Closure

*(Trigger Map and Denominator Closure identical to V-01.)*

**CLOSURE CHECK:**

```
EOR citations missing from firing entries:                            {count} [must be 0]
Gap entries missing counterfactual:                                   {count} [must be 0]
Entries missing registration witness:                                 {count} [must be 0]
Cascade entries missing Depth counter:                                {count} [must be 0]
Depth-exceeded chains unresolved:                                     {count} [must be 0]
ART-01 (SCOPE GATE)            — Auditor, Phase 0:        PRODUCED [must be PRODUCED]
ART-02 (EXCLUSION LOG)         — Auditor, Phase 0:        PRODUCED [must be PRODUCED]
ART-03 (EOR TABLE)             — Domain Expert, Phase 0:  PRODUCED [must be PRODUCED]
ART-04 (CASCADE DEPTH BUDGET)  — Domain Expert, Phase 0:  PRODUCED [must be PRODUCED]
ART-05 (PROHIBITION CONTRACTS) — Auditor, Phase 0:        PRODUCED [must be PRODUCED]
ART-06 (BREACH TOKEN PROTOCOL) — Auditor, Phase 0:        PRODUCED [must be PRODUCED]
PROHIBITION BREACHES:                                                 0 [must be 0]
```

*Role attribution operates at two structural time points. Declaration time: the ARTIFACT MANIFEST
(ART-01 through ART-06 above) names the producing role and phase as a pre-enumeration commitment.
Detection time: each CLOSURE CHECK counter names the producing role and phase inline. Both
attribution points are present in this output and both artifacts are named.*

**Exit condition:** Phase 6 SHALL be complete when trigger map covers all triggers with required
columns and closure check is stated.

---

## V-03

**Variation axis:** Lifecycle emphasis — unified table with extended lifecycle narrative; Obligation
column carries complete self-contained clauses (role + SHALL + artifact + temporal constraint);
CLOSURE CHECK note names both attribution layers and their artifacts but does not explain removal
consequences.

**Hypothesis:** The Phase 0 preamble receives extended lifecycle narrative treatment: each artifact's
purpose and timing requirement are explained in a short prose paragraph before the registry, and the
registry itself is introduced with explicit lifecycle context ("The obligations below bind each role
to a specific artifact production within Phase 0. Each row is the obligation's complete
specification; Phase 1 SHALL NOT begin until all rows carry Status: SATISFIED."). The PHASE 0
OBLIGATION REGISTRY is a unified table (C-32 PASS). The Obligation column now carries a complete
self-contained specification clause for each row — naming the role, the modal verb, the artifact,
and the temporal constraint. For example: "The Auditor SHALL produce the EXCLUSION LOG (ART-02)
during Phase 0 before any candidate is named." Reading the Obligation column alone yields all four
required elements without consulting any other column. C-38 PASS. The CLOSURE CHECK carries per-
counter inline role attribution (C-37 PASS). A post-counter note reads: "Role attribution operates
at two structural time points: (1) declaration time — the ARTIFACT MANIFEST names the producing
role and phase before enumeration begins; (2) detection time — each CLOSURE CHECK counter names
the producing role and phase inline. Both attribution points are present; both artifacts are named."
C-39 WEAK PASS: names both layers, names both artifacts. The note stops at structural inventory
and does not explain what breaks if either layer is removed from a future output. A reader cannot
determine from this note whether removing declaration-time attribution would degrade functionality
or merely reduce documentation completeness.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to
`Inactive` (1). Determine which automations fire, in what order, with what inputs and outputs,
and identify all trigger pathologies.

ALL phases SHALL execute in strict sequence. Each phase SHALL be declared complete before the
next SHALL begin.

---

### PROTOCOL PREAMBLE

*(Platform Term Contract, FM Catalog, and Entry Schema Contract identical to V-01.)*

---

### PHASE 0 — PREPARATION

**Entry condition:** Phase 0 SHALL begin when scenario specification is received and PROTOCOL
PREAMBLE declared complete.

**Job:** Phase 0 SHALL produce and lock all pre-enumeration obligations in the PHASE 0 OBLIGATION
REGISTRY. The obligations below bind each role to a specific artifact production within Phase 0.
Each row is the obligation's complete specification; Phase 1 SHALL NOT begin until all rows carry
Status: SATISFIED. Each row SHALL carry all six metadata types as named columns.

**Why these obligations exist before enumeration:**
The SCOPE GATE ensures no candidate is named before the evaluation boundary is a declared
artifact. The EXCLUSION LOG converts the automation layer sweep from an implied operation to
an auditable record. The EOR TABLE transforms platform ordering rules into named, citable rule
IDs. The CASCADE DEPTH BUDGET makes the point at which runaway chains are declared structurally
detectable. PROHIBITION CONTRACTS bind role actions to explicit lifecycle events, eliminating
silent scope expansion. The ARTIFACT MANIFEST assigns production accountability to named roles
and phases before any gap can occur. The BREACH TOKEN PROTOCOL makes violations findable at
document-scan time.

**BREACH TOKEN PROTOCOL:** `[PROHIBITION BREACH: Role | {prohibition name} | FM-NN]`

#### PHASE 0 OBLIGATION REGISTRY

| Obligation | Status | Refutation Condition | Weaker Alternative | Failure Mode | Activation Event | Producing Role |
|------------|--------|---------------------|--------------------|--------------|-----------------|----------------|
| The Auditor SHALL produce the SCOPE GATE (ART-01) during Phase 0 before any candidate is named | SATISFIED | Violated if any candidate is named before the event tuple (entity, operation, field, prev value, new value) appears as a named structural artifact with all five fields declared | Prose scope sentence naming the change context — no named structural artifact | **anonymous scope boundary** — event tuple absent; no candidate structurally excludable; scope requires prose interpretation | N/A (static pre-execution declaration; it has no lifecycle event that activates it — it SHALL exist before any phase begins; the activation concept is inapplicable because the gate is construction-time, not transition-time) | Auditor \| Phase 0 |
| The Auditor SHALL produce the EXCLUSION LOG (ART-02) during Phase 0 before any candidate is named | SATISFIED | Violated if any automation layer is evaluated without a named disposition row (layer name + included/excluded + reason) appearing before candidates are listed | Enumerate only what fired; leave unscanned layers undocumented | **anonymous layer gap** — named disposition absent; unscanned layers produce candidates that cannot be confirmed absent vs. present-but-not-firing | N/A (exclusion log SHALL be complete before any candidate is named; timing is pre-candidate by construction, not triggered by a lifecycle transition) | Auditor \| Phase 0 |
| The Domain Expert SHALL produce the EOR TABLE (ART-03) during Phase 0 before Phase 1 begins | SATISFIED | Violated if any firing entry is positioned without an inline EOR rule ID citation ("Positioned because: EOR-NN") | Ordering principle stated as prose before enumeration | **anonymous ordering rule** — rule IDs absent; per-entry position unauditable by rule citation | N/A (one-time static declaration; no lifecycle transition activates it — it is declared once and referenced throughout) | Domain Expert \| Phase 0 |
| The Domain Expert SHALL produce the CASCADE DEPTH BUDGET (ART-04) during Phase 0 before Phase 4 begins | SATISFIED | Violated if any cascade chain entry lacks a [Depth: N/MAX] counter showing position against declared maximum | Trace chains without an explicit depth ceiling | **invisible overflow** — depth budget absent; chains exceeding undeclared limit produce no counter signal | Activates at Phase 4 cascade tracing (depth budget SHALL be enforced from the first cascade entry; declaring it in Phase 0 establishes the contract; enforcement begins at Phase 4) | Domain Expert \| Phase 0 |
| The Auditor SHALL produce PROHIBITION CONTRACTS (ART-05) during Phase 0 before roles operate | SATISFIED | Violated if any prohibition lacks a named Applies After event referencing a Phase 0 transition or Phase 1 completion | Timeless global prohibition without lifecycle scope | **anonymous prohibition** — temporal activation anchor absent; effective period undefined; enforcement depends on phase-ordering inference | N/A (artifact-level row; each individual prohibition within the contract body carries its own Applies After field; the artifact itself has no single activation event) | Auditor \| Phase 0 |
| The Auditor SHALL produce the ARTIFACT MANIFEST (ART-06) during Phase 0 before enumeration begins | SATISFIED | Violated if any manifest entry lacks BOTH producing role AND producing phase as named fields | Artifact checklist with IDs but no role or phase attribution | **anonymous artifact gap** — producing role and phase absent; missing artifact cannot be attributed to responsible role and phase from manifest alone | N/A (static pre-enumeration declaration; no lifecycle event triggers its creation — it is construction-time) | Auditor \| Phase 0 |
| The Auditor SHALL declare the BREACH TOKEN PROTOCOL (ART-07) during Phase 0 before PROHIBITION CONTRACTS activate | SATISFIED | Violated if no named breach token format string is declared before prohibitions are active AND the token format is not machine-inspectable | Detect prohibition violations only through post-hoc rubric re-evaluation | **invisible breach** — named token format absent; violations produce no inline signal; undetectable without external rubric | Activates alongside PROHIBITION CONTRACTS (Phase 0 — the breach token SHALL take effect at the same time prohibitions become active) | Auditor \| Phase 0 |

*(SCOPE GATE VALUES, EXCLUSION LOG, EOR TABLE, CASCADE DEPTH BUDGET, PROHIBITION CONTRACTS,
ARTIFACT MANIFEST identical to V-01.)*

---

#### INERTIA CONTRAST

*(Failure modes, DERIVATION TEST, and constraint propagation verification identical to V-01.)*

---

**Phase 0 Exit Signal:** 7/7 SATISFIED — enumeration authorized.

**Exit condition:** Phase 0 SHALL be complete when all 7 registry rows carry Status: SATISFIED
and exit signal is issued. Phase 1 SHALL NOT begin before this signal.

---

### STRUCTURAL INVARIANT LAYER, LIFECYCLE OVERVIEW, Phases 1–5

*(Identical to V-01.)*

---

### Phase 6 — Trigger Map and Closure

*(Trigger Map and Denominator Closure identical to V-01.)*

**CLOSURE CHECK:**

```
EOR citations missing from firing entries:                            {count} [must be 0]
Gap entries missing counterfactual:                                   {count} [must be 0]
Entries missing registration witness:                                 {count} [must be 0]
Cascade entries missing Depth counter:                                {count} [must be 0]
Depth-exceeded chains unresolved:                                     {count} [must be 0]
ART-01 (SCOPE GATE)            — Auditor, Phase 0:        PRODUCED [must be PRODUCED]
ART-02 (EXCLUSION LOG)         — Auditor, Phase 0:        PRODUCED [must be PRODUCED]
ART-03 (EOR TABLE)             — Domain Expert, Phase 0:  PRODUCED [must be PRODUCED]
ART-04 (CASCADE DEPTH BUDGET)  — Domain Expert, Phase 0:  PRODUCED [must be PRODUCED]
ART-05 (PROHIBITION CONTRACTS) — Auditor, Phase 0:        PRODUCED [must be PRODUCED]
ART-06 (BREACH TOKEN PROTOCOL) — Auditor, Phase 0:        PRODUCED [must be PRODUCED]
PROHIBITION BREACHES:                                                 0 [must be 0]
```

*Role attribution operates at two structural time points: (1) declaration time — the ARTIFACT
MANIFEST (Phase 0) names the producing role and phase for each artifact before enumeration begins;
(2) detection time — each CLOSURE CHECK counter names the producing role and phase inline with the
production status. Both attribution points are present in this output. Both artifacts are named:
the ARTIFACT MANIFEST carries declaration-time attribution; the CLOSURE CHECK counter carries
detection-time attribution.*

**Exit condition:** Phase 6 SHALL be complete when trigger map covers all triggers with required
columns and closure check is stated.

---

## V-04

**Variation axis:** Phrasing register — formal imperative throughout; Obligation column carries
complete formal imperative clauses (role + SHALL + artifact + temporal constraint); separate
ATTRIBUTION CHAIN DESIGN RATIONALE section after CLOSURE CHECK names both artifacts, explains
why both layers are required, and states what breaks if either is removed.

**Hypothesis:** The phrasing register is uniformly formal imperative: SHALL appears in every
obligation statement, every gate condition, every invariant, and every phase exit condition. The
PHASE 0 OBLIGATION REGISTRY is a unified table (C-32 PASS). The Obligation column carries the
same complete self-contained clauses as V-03 (C-38 PASS). The CLOSURE CHECK carries per-counter
inline role attribution (C-37 PASS). The C-39 gap from V-03 is closed: a named ATTRIBUTION CHAIN
DESIGN RATIONALE section appears after the CLOSURE CHECK block. This section names both attribution
layers, names the artifact where each operates, and explains why both are required with an explicit
consequence statement for removing either layer. "Removing declaration-time attribution (from the
ARTIFACT MANIFEST) means role accountability is only discoverable when a gap is detected at closure
time; no pre-enumeration commitment can be audited independently of a detected gap. Removing
detection-time attribution (from the CLOSURE CHECK counter) means enforcement is anonymous; a
reader finding an ABSENT counter must navigate to the ARTIFACT MANIFEST as a secondary lookup to
identify the remediation target. Neither layer alone provides remediation self-sufficiency."
C-38 PASS, C-39 PASS. The rationale is present as a named section adjacent to but not co-located
within the CLOSURE CHECK block.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to
`Inactive` (1). Determine which automations fire, in what order, with what inputs and outputs,
and identify all trigger pathologies.

ALL phases SHALL execute in strict sequence. Each phase SHALL be declared complete before the
next SHALL begin. No phase SHALL begin until all prior phases have issued their required outputs.

---

### PROTOCOL PREAMBLE

*(Platform Term Contract, FM Catalog, and Entry Schema Contract identical to V-01.)*

---

### PHASE 0 — PREPARATION

**Entry condition:** Phase 0 SHALL begin only when the scenario specification has been received
AND the PROTOCOL PREAMBLE has been declared complete. No pre-enumeration obligation SHALL be
omitted.

**Job:** Phase 0 SHALL produce and lock all pre-enumeration obligations in the PHASE 0 OBLIGATION
REGISTRY. The registry SHALL contain one row per obligation. Each row SHALL carry all six metadata
types as named columns. No obligation's compliance SHALL require navigation outside its row.

**BREACH TOKEN PROTOCOL:** `[PROHIBITION BREACH: Role | {prohibition name} | FM-NN]`

#### PHASE 0 OBLIGATION REGISTRY

| Obligation | Status | Refutation Condition | Weaker Alternative | Failure Mode | Activation Event | Producing Role |
|------------|--------|---------------------|--------------------|--------------|-----------------|----------------|
| The Auditor SHALL produce the SCOPE GATE (ART-01) during Phase 0 before any candidate is named | SATISFIED | Violated if any candidate is named before the event tuple (entity, operation, field, previous value, new value) appears as a named structural artifact with those five fields explicitly declared | Prose scope sentence ("analysis covers account statecode changes") | **anonymous scope boundary** — event tuple absent; no candidate is structurally excludable without named boundary fields; excludability requires prose interpretation | N/A (scope gate is a static pre-execution declaration; it SHALL exist before any phase begins; the activation concept is inapplicable because the gate is construction-time, not transition-time) | Auditor \| Phase 0 |
| The Auditor SHALL produce the EXCLUSION LOG (ART-02) during Phase 0 before any candidate is named | SATISFIED | Violated if any automation layer is evaluated without a named disposition row (layer name + included/excluded + reason) appearing before candidates are named | Enumerate only what fired; leave unscanned layers undocumented | **anonymous layer gap** — named layer disposition absent; unscanned layers produce candidates that cannot be confirmed absent vs. present-but-not-firing; completeness is unverifiable | N/A (exclusion log SHALL be complete before any candidate is named; timing is pre-candidate by construction, not triggered by a lifecycle transition) | Auditor \| Phase 0 |
| The Domain Expert SHALL produce the EOR TABLE (ART-03) during Phase 0 before Phase 1 begins | SATISFIED | Violated if any firing entry is positioned in the enumeration without an inline EOR rule ID citation | Ordering principle stated as prose before enumeration ("sync before async") | **anonymous ordering rule** — named rule IDs absent; per-entry position cannot be audited by rule citation; a reader cannot confirm whether ordering is rule-governed or arbitrary | N/A (EOR table is a one-time static declaration before enumeration; it is declared once and referenced throughout; no lifecycle transition activates it) | Domain Expert \| Phase 0 |
| The Domain Expert SHALL produce the CASCADE DEPTH BUDGET (ART-04) during Phase 0 before Phase 4 begins | SATISFIED | Violated if any cascade chain entry lacks a [Depth: N/MAX] counter showing position against declared maximum | Trace chains without explicit depth ceiling | **invisible overflow** — named depth budget absent; chains exceeding an undeclared limit produce no detectable counter signal; storm verdict cannot reference depth-exceeded entries as a named class | Activates at Phase 4 cascade tracing (depth budget SHALL be enforced from the first cascade entry in Phase 4; declaring it earlier has no enforcement effect) | Domain Expert \| Phase 0 |
| The Auditor SHALL produce PROHIBITION CONTRACTS (ART-05) during Phase 0 before roles operate | SATISFIED | Violated if any prohibition lacks a named "Applies After" event referencing a Phase 0 lifecycle transition or Phase 1 completion | Timeless global prohibition ("Domain Expert may not add candidates" with no lifecycle scope) | **anonymous prohibition** — temporal activation anchor absent; prohibition effective period undefined; pre-activation compliance is trivially satisfiable and enforcement depends on phase-ordering inference | N/A (prohibition contracts are declared in Phase 0 before roles operate; the PROHIBITION CONTRACTS artifact itself has no single activation event — each prohibition row within the contract body carries its own Applies After field) | Auditor \| Phase 0 |
| The Auditor SHALL produce the ARTIFACT MANIFEST (ART-06) during Phase 0 before enumeration begins | SATISFIED | Violated if any manifest entry lacks BOTH producing role AND producing phase as named fields (either field alone is insufficient) | Bulleted artifact checklist with IDs but no role or phase attribution | **anonymous artifact gap** — producing role and phase absent; a missing artifact cannot be attributed to a specific responsible role and phase; CLOSURE CHECK cannot report "Role X, Phase Y: ABSENT" | N/A (manifest is a static pre-enumeration declaration; it SHALL exist before enumeration begins; no lifecycle event triggers its creation — it is construction-time) | Auditor \| Phase 0 |
| The Auditor SHALL declare the BREACH TOKEN PROTOCOL (ART-07) during Phase 0 before PROHIBITION CONTRACTS activate | SATISFIED | Violated if no named breach token format string is declared before PROHIBITION CONTRACTS are active AND the token format string is not machine-inspectable | Detect prohibition violations only through post-hoc rubric re-evaluation of the completed output | **invisible breach** — named breach token format absent; prohibition violations produce no inline signal; a reader scanning the artifact cannot find violations without re-scoring against the rubric | Activates alongside PROHIBITION CONTRACTS (the breach token SHALL take effect at the same time prohibitions become active; declaring it earlier is permissible but it has no enforcement effect until prohibitions are active) | Auditor \| Phase 0 |

*(SCOPE GATE VALUES, EXCLUSION LOG, EOR TABLE, CASCADE DEPTH BUDGET, PROHIBITION CONTRACTS,
ARTIFACT MANIFEST identical to V-01, with all gate statements using SHALL/MUST throughout.)*

---

#### INERTIA CONTRAST

*(Failure modes, DERIVATION TEST, and constraint propagation verification identical to V-01,
with all rationale lines using SHALL imperative register.)*

---

**Phase 0 Exit Signal:** 7/7 SATISFIED — enumeration authorized.

**Exit condition:** Phase 0 SHALL be complete when all 7 registry rows carry Status: SATISFIED
and exit signal is issued. No enumeration entry SHALL appear before this signal.

---

### STRUCTURAL INVARIANT LAYER, LIFECYCLE OVERVIEW, Phases 1–5

*(Identical to V-01, with all gate statements using SHALL/MUST throughout.)*

---

### Phase 6 — Trigger Map and Closure

*(Trigger Map and Denominator Closure identical to V-01.)*

**CLOSURE CHECK:**

```
EOR citations missing from firing entries:                            {count} [must be 0]
Gap entries missing counterfactual:                                   {count} [must be 0]
Entries missing registration witness:                                 {count} [must be 0]
Cascade entries missing Depth counter:                                {count} [must be 0]
Depth-exceeded chains unresolved:                                     {count} [must be 0]
ART-01 (SCOPE GATE)            — Auditor, Phase 0:        PRODUCED [must be PRODUCED]
ART-02 (EXCLUSION LOG)         — Auditor, Phase 0:        PRODUCED [must be PRODUCED]
ART-03 (EOR TABLE)             — Domain Expert, Phase 0:  PRODUCED [must be PRODUCED]
ART-04 (CASCADE DEPTH BUDGET)  — Domain Expert, Phase 0:  PRODUCED [must be PRODUCED]
ART-05 (PROHIBITION CONTRACTS) — Auditor, Phase 0:        PRODUCED [must be PRODUCED]
ART-06 (BREACH TOKEN PROTOCOL) — Auditor, Phase 0:        PRODUCED [must be PRODUCED]
PROHIBITION BREACHES:                                                 0 [must be 0]
```

**Exit condition:** Phase 6 SHALL be complete when trigger map covers all triggers with required
columns and closure check is stated.

---

#### ATTRIBUTION CHAIN DESIGN RATIONALE

Role attribution for artifact production operates at two structural time points in this output:

**Declaration time — ARTIFACT MANIFEST (Phase 0):** The ARTIFACT MANIFEST names the producing
role and phase for each artifact before enumeration begins. This commitment is a pre-enumeration
structural declaration, auditable independently of whether any gap is later detected. A reviewer
can inspect the ARTIFACT MANIFEST to verify that every artifact has a named responsible role
without waiting for a CLOSURE CHECK to be run.

**Detection time — CLOSURE CHECK counter (Phase 6):** Each CLOSURE CHECK artifact production
counter names the producing role and phase inline within the counter value. A reader finding an
ABSENT counter can identify the remediation target (role and phase) from the counter line alone.

**Why both layers are required:**
Removing declaration-time attribution (from the ARTIFACT MANIFEST) means role accountability is
only discoverable when a gap is detected at closure time. The ARTIFACT MANIFEST provides no
pre-enumeration commitment that could be audited before any gap occurs. A reviewer inspecting
only the CLOSURE CHECK receives correct remediation guidance when a gap is present, but cannot
verify accountability coverage before gaps occur.

Removing detection-time attribution (from the CLOSURE CHECK counter) means the ARTIFACT MANIFEST
carries the requirement as a pre-enumeration commitment but CLOSURE CHECK enforcement is anonymous.
A reader finding an ABSENT counter must navigate to the ARTIFACT MANIFEST as a secondary lookup to
identify the remediation target — cross-reference is required, and cross-reference failure (the
reader stops at the CLOSURE CHECK) leaves the remediation target unidentified.

Neither layer alone provides remediation self-sufficiency. Both SHALL be declared and maintained
together: the ARTIFACT MANIFEST establishes accountability before gaps can occur; the CLOSURE CHECK
counter makes the remediation target determinable at the point of detection without secondary
navigation.

---

## V-05

**Variation axis:** Full combination — complete self-contained obligation clauses (C-38 PASS);
attribution chain design rationale co-located inline within the CLOSURE CHECK block (C-39 PASS);
"removing either layer is understood to break remediation self-sufficiency, not merely reduce
coverage" language explicit and inseparable from the detection mechanism.

**Hypothesis:** V-04 is retained in full: PHASE 0 OBLIGATION REGISTRY with complete self-contained
obligation clauses (C-38 PASS), N/A-with-reason per cell (C-36 PASS), "anonymous [X]" labels
(C-34 PASS), DERIVATION TEST nested inside INERTIA CONTRAST (C-35 PASS), per-counter inline role
(C-37 PASS). The structural gap from V-04 is closed: the ATTRIBUTION CHAIN DESIGN RATIONALE is no
longer a separate post-CLOSURE CHECK section but is embedded as a named note block INSIDE the
CLOSURE CHECK structure, immediately following the counter block. This co-location makes the design
rationale physically inseparable from the mechanism it describes — a reader who encounters the
CLOSURE CHECK encounters the rationale without needing to navigate to a sibling section. The note
uses explicit self-sufficiency language: "removing either layer is understood to break remediation
self-sufficiency, not merely reduce coverage." C-38 PASS, C-39 PASS. Both criteria satisfied with
the rationale inseparably bound to the mechanism.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dynamics 365 Sales `account` record's `statecode` field has changed from `Active` (0) to
`Inactive` (1). Determine which automations fire, in what order, with what inputs and outputs,
and identify all trigger pathologies.

ALL phases SHALL execute in strict sequence. Each phase SHALL be declared complete before the
next SHALL begin. No phase SHALL begin until all prior phases have issued their required outputs.

---

### PROTOCOL PREAMBLE

*(Platform Term Contract, FM Catalog, and Entry Schema Contract identical to V-01.)*

---

### PHASE 0 — PREPARATION

*(Phase 0 Job, BREACH TOKEN PROTOCOL, and PHASE 0 OBLIGATION REGISTRY with complete self-contained
obligation clauses identical to V-04. SCOPE GATE VALUES, EXCLUSION LOG, EOR TABLE, CASCADE DEPTH
BUDGET, PROHIBITION CONTRACTS, and ARTIFACT MANIFEST identical to V-01, with all gate statements
using SHALL/MUST throughout.)*

---

#### INERTIA CONTRAST

*(Failure modes, DERIVATION TEST, and constraint propagation verification identical to V-01,
with all rationale lines using SHALL imperative register.)*

---

**Phase 0 Exit Signal:** 7/7 SATISFIED — enumeration authorized.

**Exit condition:** Phase 0 SHALL be complete when all 7 registry rows carry Status: SATISFIED
and exit signal is issued. No enumeration entry SHALL appear before this signal.

---

### STRUCTURAL INVARIANT LAYER, LIFECYCLE OVERVIEW, Phases 1–5

*(Identical to V-01, with all gate statements using SHALL/MUST throughout.)*

---

### Phase 6 — Trigger Map and Closure

*(Trigger Map and Denominator Closure identical to V-01.)*

**CLOSURE CHECK:**

```
EOR citations missing from firing entries:                            {count} [must be 0]
Gap entries missing counterfactual:                                   {count} [must be 0]
Entries missing registration witness:                                 {count} [must be 0]
Cascade entries missing Depth counter:                                {count} [must be 0]
Depth-exceeded chains unresolved:                                     {count} [must be 0]
ART-01 (SCOPE GATE)            — Auditor, Phase 0:        PRODUCED [must be PRODUCED]
ART-02 (EXCLUSION LOG)         — Auditor, Phase 0:        PRODUCED [must be PRODUCED]
ART-03 (EOR TABLE)             — Domain Expert, Phase 0:  PRODUCED [must be PRODUCED]
ART-04 (CASCADE DEPTH BUDGET)  — Domain Expert, Phase 0:  PRODUCED [must be PRODUCED]
ART-05 (PROHIBITION CONTRACTS) — Auditor, Phase 0:        PRODUCED [must be PRODUCED]
ART-06 (BREACH TOKEN PROTOCOL) — Auditor, Phase 0:        PRODUCED [must be PRODUCED]
PROHIBITION BREACHES:                                                 0 [must be 0]
```

*ATTRIBUTION CHAIN DESIGN RATIONALE (co-located with detection mechanism):*

*Role attribution for artifact production exists at two structural time points in this output.
Declaration time: the ARTIFACT MANIFEST (Phase 0, above) names the producing role and phase for
each artifact as a pre-enumeration commitment, auditable before any gap is detected. Detection
time: each CLOSURE CHECK counter above names the producing role and phase inline, so the
remediation target is determinable from the counter value alone.*

*Both layers are required by design. Removing declaration-time attribution means the ARTIFACT
MANIFEST provides no accountability commitment auditable before a gap occurs — role identity is
only discoverable at detection time, after a gap has already formed. Removing detection-time
attribution means a reader finding an ABSENT counter must navigate to the ARTIFACT MANIFEST as
a secondary lookup to identify the remediation target; if that navigation fails, the remediation
target is unidentified. Removing either layer is understood to break remediation self-sufficiency,
not merely reduce coverage. The ARTIFACT MANIFEST and the CLOSURE CHECK counter role attribution
SHALL be declared and maintained together.*

**Exit condition:** Phase 6 SHALL be complete when trigger map covers all triggers with required
columns and closure check is stated.
