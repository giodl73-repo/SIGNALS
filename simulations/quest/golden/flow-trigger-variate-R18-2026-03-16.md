---
skill: flow-trigger
round: 18
rubric_version: 15
new_criteria: [C-42, C-43]
date: 2026-03-16
---

# flow-trigger — Round 18 (Rubric v15) Variations

**New criteria this round:**
- **C-42** — Consequence-embedded assertion brackets: every assertion inside the NOTE block uses
  the extended form `[must be VALUE — inline rationale clause]`, where the rationale is
  syntax-bound inside the bracket itself. Rationale removal requires editing the bracket value,
  not deleting a separate element. Extends C-41 (same register requirement) one level deeper:
  C-40 = fence inseparability; C-41 = register co-domain; C-42 = syntactic co-location of
  constraint and justification.
- **C-43** — Systemic-property assertions in embedded NOTE blocks: at least one assertion in the
  NOTE block asserts a higher-order property of the element combination — not just element
  presence. The named systemic property (e.g., REMEDIATION SELF-SUFFICIENCY) is independently
  falsifiable: it fails if either element is removed, and that consequence is stated inside
  the assertion bracket. Extends C-41 (same register domain); analogous to C-35 DERIVATION TEST
  for failure mode labels.

**Round 17 gap analysis (scored against rubric v14, evaluated retroactively against v15):**
- V-01 R17: C-41 PASS (assertion register NOTE inside fence). C-42 FAIL: NOTE brackets use
  `[must be present]` without inline rationale clause — bracket ends at the constraint value,
  not at a rationale string. C-43 FAIL: NOTE block has two element-presence assertions only;
  no REMEDIATION SELF-SUFFICIENCY or other combined-system-property assertion present.
- V-02 R17: C-41 FAIL vacuous (prose CLOSURE CHECK, no fence — C-40 not a full pass). C-42
  N/A vacuous (C-40 not satisfied, C-41 vacuous, C-42 vacuous). C-43 FAIL: no systemic-property
  assertion anywhere.
- V-03 R17: C-41 FAIL (NOTE inside fence but pure prose/narrative register, not assertion
  register). C-42 FAIL (no `PROPERTY: VALUE [must be VALUE]` brackets in NOTE at all). C-43
  FAIL.
- V-04 R17: C-41 PARTIAL (NOTE inside fence, mixed register — two assertion lines followed by
  a prose consequence sentence). C-42 PARTIAL: two assertion lines present but both use plain
  `[must be present]` without inline rationale inside the bracket. C-43 FAIL: no
  REMEDIATION SELF-SUFFICIENCY assertion; consequence stated in prose sentence not as assertion
  line.
- V-05 R17: C-41 PASS (NOTE inside fence, pure assertion register). C-42 PASS: both attribution
  assertions use extended bracket form `[must be present — inline rationale clause]`. C-43 PASS:
  REMEDIATION SELF-SUFFICIENCY assertion present as third NOTE line using
  `[must be maintained — inline rationale]` form, asserting combined-system property.

**Round 18 ladder (C-42, C-43):**
R17 V-05 established C-42 PASS and C-43 PASS retroactively. R18 probes the two new axes
deliberately across the failure spectrum:
- C-42 axis: plain bracket (FAIL) → inconsistent extension (PARTIAL) → full extension (PASS)
- C-43 axis: no systemic assertion (FAIL) → systemic inference only (FAIL) → explicit systemic
  assertion (PASS)

V-01 (C-42 FAIL: plain brackets; C-43 FAIL: no systemic assertion) →
V-02 (C-42 vacuous FAIL: no fence, C-40 fails; C-43 FAIL) →
V-03 (C-42 PARTIAL: first assertion extended, second plain; C-43 FAIL: systemic consequence in
INERTIA CONTRAST but not as NOTE assertion) →
V-04 (C-42 PASS: all NOTE brackets extended with inline rationale; C-43 FAIL: no
REMEDIATION SELF-SUFFICIENCY assertion — combined-system property inferable but not stated) →
V-05 (C-42 PASS; C-43 PASS: REMEDIATION SELF-SUFFICIENCY assertion present as third NOTE line).

**Variation axes selected:**
- Single-axis: Role sequence (V-01), Output format (V-02), Lifecycle emphasis (V-03)
- Combined: Inertia framing + phrasing register (V-04),
  Phrasing register + extended bracket + systemic assertion (V-05)

---

## V-01

**Variation axis:** Role sequence — Domain Expert obligations appear before Auditor obligations
in the PHASE 0 OBLIGATION REGISTRY row ordering. The CLOSURE CHECK NOTE block uses pure
assertion register (C-41 PASS) but plain brackets without inline rationale clauses (C-42 FAIL).
No REMEDIATION SELF-SUFFICIENCY assertion in the NOTE block (C-43 FAIL).

**Hypothesis:** Reordering the PHASE 0 OBLIGATION REGISTRY so Domain Expert rows (EOR TABLE,
CASCADE DEPTH BUDGET) precede Auditor rows (SCOPE GATE, EXCLUSION LOG, PROHIBITION CONTRACTS,
ARTIFACT MANIFEST, BREACH TOKEN PROTOCOL) signals technical ownership before audit overhead —
the enumeration infrastructure is declared before its guards. The CLOSURE CHECK NOTE block
uses `PROPERTY: VALUE [must be VALUE]` assertion register throughout (C-41 PASS). However,
the bracket form ends at the constraint value — `[must be present]` — with no inline rationale
clause appended after the em-dash. A reader can read the NOTE assertion lines as peer counter
entries (C-41 satisfied) but cannot derive the justification for the constraint from the bracket
itself (C-42 FAIL). No REMEDIATION SELF-SUFFICIENCY or other combined-system-property assertion
appears in the NOTE block (C-43 FAIL).

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

**Job:** Phase 0 SHALL produce and lock all pre-enumeration obligations in the PHASE 0
OBLIGATION REGISTRY before Phase 1 begins. The registry is a unified table; each row carries
all six metadata types as named columns.

**BREACH TOKEN PROTOCOL:** `[PROHIBITION BREACH: Role | {prohibition name} | FM-NN]`

#### PHASE 0 OBLIGATION REGISTRY

*(Row order: Domain Expert obligations first, Auditor obligations follow.)*

| Obligation | Status | Refutation Condition | Weaker Alternative | Failure Mode | Activation Event | Producing Role |
|------------|--------|---------------------|--------------------|--------------|-----------------|----------------|
| The Domain Expert SHALL produce the EOR TABLE (ART-03) during Phase 0 before Phase 1 begins | SATISFIED | Violated if any firing entry is positioned without an inline EOR rule ID citation | Ordering rationale stated as prose ("sync before async") | **anonymous ordering rule** — rule IDs absent; per-entry position unauditable by rule citation | N/A (one-time static declaration; no lifecycle transition activates it) | Domain Expert \| Phase 0 |
| The Domain Expert SHALL produce the CASCADE DEPTH BUDGET (ART-04) during Phase 0 before Phase 4 begins | SATISFIED | Violated if any cascade chain entry lacks a [Depth: N/MAX] counter showing position against declared maximum | Trace chains without a named depth ceiling | **invisible overflow** — depth budget absent; chains exceeding undeclared limit produce no counter signal | Activates at Phase 4 cascade tracing | Domain Expert \| Phase 0 |
| The Auditor SHALL produce the SCOPE GATE (ART-01) during Phase 0 before any candidate is named | SATISFIED | Violated if any candidate is named before the event tuple (entity, operation, field, prev value, new value) appears as a named structural artifact with all five fields declared | Prose scope sentence naming the change context — no named structural artifact | **anonymous scope boundary** — event tuple absent; no candidate structurally excludable; scope requires prose interpretation | N/A (static pre-execution declaration; no lifecycle transition activates it) | Auditor \| Phase 0 |
| The Auditor SHALL produce the EXCLUSION LOG (ART-02) during Phase 0 before any candidate is named | SATISFIED | Violated if any automation layer is evaluated without a named disposition row before candidates are listed | Enumerate only what fired; leave unscanned layers undocumented | **anonymous layer gap** — named disposition absent; unscanned layers produce candidates that cannot be confirmed absent vs. present-but-not-firing | N/A (pre-candidate by construction) | Auditor \| Phase 0 |
| The Auditor SHALL produce PROHIBITION CONTRACTS (ART-05) during Phase 0 before roles operate | SATISFIED | Violated if any prohibition lacks a named Applies After event referencing a Phase 0 or Phase 1 lifecycle transition | Timeless global prohibition without lifecycle scope | **anonymous prohibition** — temporal activation anchor absent; effective period undefined; enforcement depends on phase-ordering inference | N/A (each prohibition within the contract body carries its own Applies After field) | Auditor \| Phase 0 |
| The Auditor SHALL produce the ARTIFACT MANIFEST (ART-06) during Phase 0 before enumeration begins | SATISFIED | Violated if any manifest entry lacks BOTH producing role AND producing phase as named fields | Artifact checklist with IDs but no role or phase attribution | **anonymous artifact gap** — producing role and phase absent; missing artifact cannot be attributed to responsible role and phase | N/A (static pre-enumeration declaration; no lifecycle event triggers its creation) | Auditor \| Phase 0 |
| The Auditor SHALL declare the BREACH TOKEN PROTOCOL during Phase 0 before PROHIBITION CONTRACTS activate | SATISFIED | Violated if no named breach token format string is declared before prohibitions are active | Detect prohibition violations only through post-hoc rubric re-evaluation | **invisible breach** — named token format absent; violations produce no inline signal; undetectable without external rubric | Activates alongside PROHIBITION CONTRACTS (Phase 0) | Auditor \| Phase 0 |

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
- Weaker alternative: Narrative sentence naming the change context
- Failure mode: **anonymous scope boundary** — the mechanism SHALL provide a named event tuple;
  prose sentences are not named structural artifacts; scope membership requires prose interpretation

**PROHIBITION CONTRACTS (temporal anchor vs. timeless prohibition):**
- Weaker alternative: Global prohibition without lifecycle reference
- Failure mode: **anonymous prohibition** — the mechanism SHALL carry a named Applies After
  lifecycle event; timeless prohibitions provide no named activation point; enforcement depends
  on phase-ordering inference

**ARTIFACT MANIFEST (role-attributed vs. ID-only):**
- Weaker alternative: Artifact list with IDs but no producing role or phase columns
- Failure mode: **anonymous artifact gap** — the mechanism SHALL carry both producing role AND
  producing phase as named fields; a gap with no role attribution cannot be remediated from the
  manifest alone

**DERIVATION TEST**

| Failure Mode Label | Absent Structural Property | Derived Minimum Implementation |
|-------------------|---------------------------|-------------------------------|
| **anonymous scope boundary** | Named event tuple as structural artifact with named fields | Scope boundary SHALL be a named artifact. Minimum: structural artifact with entity, operation, field, prev-value, new-value as named fields. A prose sentence is insufficient. |
| **anonymous layer gap** | Named disposition row per automation layer swept | Each layer swept SHALL carry a named disposition row. Minimum: table where every row names layer, disposition, and reason. A missing row is an anonymous layer gap. |
| **anonymous ordering rule** | Named rule ID per ordering principle | Each ordering principle SHALL carry an assigned rule ID. Minimum: table with rule ID column. Each firing entry SHALL cite its rule ID inline. Prose ordering statements are anonymous. |
| **anonymous prohibition** | Named temporal activation anchor ("Applies After" field) | Each prohibition SHALL carry a named Applies After event. Minimum: prohibition table with Applies After column. Timeless prohibitions are anonymous. |
| **anonymous artifact gap** | Named producing role AND named producing phase | Each manifest entry SHALL carry both fields. Either alone is insufficient. Minimum: manifest table with Producing Role and Producing Phase columns, both populated. |
| **invisible breach** | Named breach token format declared before prohibitions activate | A named token string SHALL be declared and used inline at point of violation. Without it, breaches are invisible to document-level scan. |

**Constraint propagation verification:** A reader who reads only the Failure Mode column SHALL
be able to derive the minimum implementation for every Phase 0 obligation without rubric access.

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

**Job:** Identify all candidate triggers without condition filtering. Declare denominator N.
Open all three anomaly question slots. Issue Phrasing Clearance PCC-1 if zero register
violations found.

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

**Exit condition:** Phase 1 SHALL be complete when N is declared, all three anomaly slots are
OPEN, and PCC-1 is issued.

---

### Phase 2 — Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when Phase 1 complete, N declared, PCC-1 issued.

**Job:** Enumerate all synchronous triggers using FIRING ENTRY or NON-FIRING ENTRY schema.
Include at least one negative vocabulary example. Order by execution priority per EOR table.

**Negative vocabulary example (required):** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | EOR Citation | Registration | Depth | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|-------------|-------|-------------|

**Exit condition:** Phase 2 SHALL be complete when every sync-tier candidate has a resolved
entry with all schema slots populated.

---

### Phase 3 — Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when Phase 2 complete and Sync Trigger Table produced.

**Job:** Enumerate all async-tier candidates. Annotate latency tier per entry.

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | EOR Citation | Registration | Depth | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|-------------|-------|-------------|

**Exit condition:** Phase 3 SHALL be complete when every async-tier candidate has a resolved
entry with all slots populated.

---

### Phase 4 — Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when Phases 2 and 3 complete and both tables produced.

**Job:** Trace cascade chains from side-effect field writes. Assign Chain IDs (CH-01, CH-02,
...). Apply `[Depth: N/5]` counter per cascade entry. Apply back-edge detection. Mark final
chain row `[TERMINAL]`. Issue `[DEPTH EXCEEDED: CH-NN]` if any chain exceeds MAX_DEPTH.

**Cascade Chain Table:**

| Chain ID | Depth | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|-------|--------------------|--------------------|--------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be complete when all side-effect writes evaluated, all
chains carry Chain-Status, back-edge detection applied.

---

### Phase 5 — Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when Phase 4 complete and all chains carry Chain-Status.

**Job:** Evidence-anchored verdicts for all three anomaly classes. Cite specific trigger rows.
Propose remediation per confirmed anomaly. Produce adjacency list (trigger graph).

**Trigger Storm:** Evidence: *[rows]* | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Missing Trigger:** Evidence: *[rows]* | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Circular Trigger:** Evidence: *[rows]* | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Exit condition:** Phase 5 SHALL be complete when all three verdicts are issued with cited
evidence and every confirmed anomaly has at least one remediation.

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
---- NOTE: ATTRIBUTION CHAIN ------------------------------------------------
DECLARATION TIME ATTRIBUTION (ART-06):        present [must be present]
DETECTION TIME ATTRIBUTION (ART-NN counters): present [must be present]
---- END NOTE ---------------------------------------------------------------
```

**Exit condition:** Phase 6 SHALL be complete when trigger map covers all triggers with
required columns and closure check is stated.

---

## V-02

**Variation axis:** Output format — CLOSURE CHECK rendered as a pipe-delimited prose block
rather than a code fence; no fence boundary exists to contain a NOTE block inside it; the
attribution chain content appears as a labeled prose paragraph ("**Attribution Note:**")
immediately after the last counter line; the PHASE 0 OBLIGATION REGISTRY obligation text
omits the temporal constraint ("before Phase N begins"), naming role, modal verb, and artifact
but not when.

**Hypothesis:** The PHASE 0 OBLIGATION REGISTRY obligation text reads "The [Role] SHALL produce
the [ARTIFACT]" — naming role, modal verb, and artifact but omitting the temporal constraint.
C-38 WEAK PASS: three of four required components present; a reader consulting only the
Obligation column cannot determine when the obligation must be fulfilled. The CLOSURE CHECK is
reformatted as a prose block with pipe delimiters — no code fence — so no fence boundary exists
to contain any NOTE block. The attribution chain content appears as a prose paragraph labelled
"**Attribution Note:**" immediately after the last counter line; C-40 PARTIAL: co-located
adjacent to the CLOSURE CHECK section but not inside a code fence. C-41 FAIL (vacuous path):
C-40 is not a full pass — the NOTE block register question requires a NOTE block embedded inside
a fence before C-41 can be evaluated. C-42 FAIL (vacuous): C-40 not satisfied; C-41 vacuous;
C-42 vacuous. C-43 FAIL: no systemic-property assertion anywhere.

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

**Job:** Phase 0 SHALL produce and lock all pre-enumeration obligations. Each obligation appears
as a row in the PHASE 0 OBLIGATION REGISTRY unified table with all six metadata types as named
columns.

**BREACH TOKEN PROTOCOL:** `[PROHIBITION BREACH: Role | {prohibition name} | FM-NN]`

#### PHASE 0 OBLIGATION REGISTRY

| Obligation | Status | Refutation Condition | Weaker Alternative | Failure Mode | Activation Event | Producing Role |
|------------|--------|---------------------|--------------------|--------------|-----------------|----------------|
| The Auditor SHALL produce the SCOPE GATE | SATISFIED | Violated if any candidate named before event tuple declared as named artifact with five named fields | Prose scope sentence naming the change context | **anonymous scope boundary** — event tuple absent; scope requires prose interpretation | N/A (static pre-execution; no lifecycle transition activates it) | Auditor \| Phase 0 |
| The Auditor SHALL produce the EXCLUSION LOG | SATISFIED | Violated if any automation layer evaluated without named disposition row before candidates listed | Enumerate only what fired | **anonymous layer gap** — disposition absent; unscanned layers unverifiable | N/A (pre-candidate by construction) | Auditor \| Phase 0 |
| The Domain Expert SHALL produce the EOR TABLE | SATISFIED | Violated if any firing entry lacks inline EOR rule ID citation | Ordering stated as prose | **anonymous ordering rule** — rule IDs absent; position unauditable by citation | N/A (one-time static declaration) | Domain Expert \| Phase 0 |
| The Domain Expert SHALL produce the CASCADE DEPTH BUDGET | SATISFIED | Violated if any cascade entry lacks [Depth: N/MAX] counter | Trace without declared depth ceiling | **invisible overflow** — depth budget absent; no counter signal at overflow | Activates at Phase 4 | Domain Expert \| Phase 0 |
| The Auditor SHALL produce PROHIBITION CONTRACTS | SATISFIED | Violated if any prohibition lacks named Applies After event | Timeless global prohibition | **anonymous prohibition** — temporal anchor absent; effective period undefined | N/A (each row within the contract body carries its own Applies After field) | Auditor \| Phase 0 |
| The Auditor SHALL produce the ARTIFACT MANIFEST | SATISFIED | Violated if any entry lacks BOTH producing role AND producing phase | ID-only artifact list | **anonymous artifact gap** — producing role and phase absent; gap unattributable | N/A (static pre-enumeration declaration) | Auditor \| Phase 0 |
| The Auditor SHALL declare the BREACH TOKEN PROTOCOL | SATISFIED | Violated if no named token format declared before prohibitions activate | Post-hoc rubric re-evaluation for violations | **invisible breach** — token format absent; violations undetectable inline | Activates alongside PROHIBITION CONTRACTS | Auditor \| Phase 0 |

*(SCOPE GATE VALUES, EXCLUSION LOG, EOR TABLE, CASCADE DEPTH BUDGET, PROHIBITION CONTRACTS,
ARTIFACT MANIFEST identical to V-01.)*

---

#### INERTIA CONTRAST

*(Failure modes, DERIVATION TEST, and constraint propagation verification identical to V-01.)*

---

**Phase 0 Exit Signal:** 7/7 SATISFIED — enumeration authorized.

**Exit condition:** Phase 0 SHALL be complete when all 7 obligation rows carry Status: SATISFIED
and exit signal is issued.

---

### STRUCTURAL INVARIANT LAYER, LIFECYCLE OVERVIEW, Phases 1–5

*(Identical to V-01.)*

---

### Phase 6 — Trigger Map and Closure

*(Trigger Map and Denominator Closure identical to V-01.)*

**CLOSURE CHECK:**

EOR citations missing from firing entries: {count} [must be 0]
Gap entries missing counterfactual: {count} [must be 0]
Entries missing registration witness: {count} [must be 0]
Cascade entries missing Depth counter: {count} [must be 0]
Depth-exceeded chains unresolved: {count} [must be 0]
ART-01 (SCOPE GATE) — Auditor, Phase 0: PRODUCED [must be PRODUCED]
ART-02 (EXCLUSION LOG) — Auditor, Phase 0: PRODUCED [must be PRODUCED]
ART-03 (EOR TABLE) — Domain Expert, Phase 0: PRODUCED [must be PRODUCED]
ART-04 (CASCADE DEPTH BUDGET) — Domain Expert, Phase 0: PRODUCED [must be PRODUCED]
ART-05 (PROHIBITION CONTRACTS) — Auditor, Phase 0: PRODUCED [must be PRODUCED]
ART-06 (BREACH TOKEN PROTOCOL) — Auditor, Phase 0: PRODUCED [must be PRODUCED]
PROHIBITION BREACHES: 0 [must be 0]

**Attribution Note:** Role attribution for artifact production operates at two structural time
points. Declaration time: the ARTIFACT MANIFEST names the producing role and phase for each
artifact before enumeration begins — accountability is auditable before any gap forms.
Detection time: each ART-NN counter above names the producing role and phase inline within the
counter value — a reader finding an ABSENT counter identifies the remediation target without
navigating to the ARTIFACT MANIFEST. Both layers are required; removing either breaks
remediation self-sufficiency, not merely reduces coverage.

**Exit condition:** Phase 6 SHALL be complete when trigger map covers all triggers with
required columns and closure check is stated.

---

## V-03

**Variation axis:** Lifecycle emphasis — each phase body opens with an extended "Why this phase
must complete before the next begins" paragraph; the PHASE 0 OBLIGATION REGISTRY carries
complete four-component obligation text; the CLOSURE CHECK has a named NOTE block embedded
inside the code fence using assertion register (C-41 PASS); the NOTE block applies the extended
bracket form `[must be VALUE — inline rationale]` to DECLARATION TIME attribution but uses the
plain bracket form `[must be VALUE]` for DETECTION TIME attribution — inconsistent bracket
extension (C-42 PARTIAL); no REMEDIATION SELF-SUFFICIENCY assertion in the NOTE block (C-43
FAIL).

**Hypothesis:** Lifecycle emphasis variation adds a phase-rationale paragraph to every phase
body, explaining what structural gap the phase closes. The PHASE 0 OBLIGATION REGISTRY carries
complete four-component obligation text (C-38 PASS). The CLOSURE CHECK has a named NOTE block
embedded inside the code fence (C-40 PASS). The NOTE block uses pure assertion register (C-41
PASS): both lines follow `PROPERTY: VALUE [must be CONSTRAINT]` format. However, the bracket
extension is inconsistent: the first line (DECLARATION TIME) appends an inline rationale clause
inside the bracket — `[must be present — ARTIFACT MANIFEST names producing role and phase
pre-enumeration; accountability auditable before any gap forms]` — while the second line
(DETECTION TIME) uses plain `[must be present]` without the rationale clause. C-42 PARTIAL: the
extended bracket form is present on one assertion but absent on the other; a reader scanning the
NOTE block cannot determine whether the inline rationale is a structural property of all NOTE
assertions or an incidental addition to one. No REMEDIATION SELF-SUFFICIENCY or combined-system-
property assertion appears; the systemic guarantee is inferable from reading both assertions but
never stated as a named detection target (C-43 FAIL).

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

**Why Phase 0 exists before Phase 1:** Without Phase 0, trigger enumeration begins without a
structurally declared scope boundary (SCOPE GATE), without a record of which automation layers
were considered (EXCLUSION LOG), without named ordering rules to cite per entry (EOR TABLE),
without a declared depth ceiling to make cascade overflow detectable (CASCADE DEPTH BUDGET),
without role-scoped prohibition contracts to prevent silent scope expansion (PROHIBITION
CONTRACTS), without a role-attributed artifact manifest to enable accountable gap detection
(ARTIFACT MANIFEST), and without a named breach token protocol to make prohibition violations
findable inline (BREACH TOKEN PROTOCOL). Each Phase 0 obligation removes one category of
anonymous failure from the enumeration phases that follow.

**Entry condition:** Phase 0 SHALL begin when scenario specification is received and PROTOCOL
PREAMBLE declared complete.

**Job:** Phase 0 SHALL produce and lock all pre-enumeration obligations in the PHASE 0
OBLIGATION REGISTRY. Each row SHALL carry all six metadata types as named columns and SHALL
carry Status: SATISFIED before the Phase 0 exit signal is issued.

**BREACH TOKEN PROTOCOL:** `[PROHIBITION BREACH: Role | {prohibition name} | FM-NN]`

#### PHASE 0 OBLIGATION REGISTRY

| Obligation | Status | Refutation Condition | Weaker Alternative | Failure Mode | Activation Event | Producing Role |
|------------|--------|---------------------|--------------------|--------------|-----------------|----------------|
| The Auditor SHALL produce the SCOPE GATE (ART-01) during Phase 0 before any candidate is named | SATISFIED | Violated if any candidate is named before the event tuple (entity, operation, field, prev value, new value) appears as a named structural artifact with all five fields declared | Prose scope sentence naming the change context — no named structural artifact | **anonymous scope boundary** — event tuple absent; no candidate structurally excludable; scope requires prose interpretation | N/A (static pre-execution declaration; no lifecycle transition activates it — it SHALL exist before any phase begins by construction) | Auditor \| Phase 0 |
| The Auditor SHALL produce the EXCLUSION LOG (ART-02) during Phase 0 before any candidate is named | SATISFIED | Violated if any automation layer is evaluated without a named disposition row (layer name + disposition + reason) appearing before candidates are listed | Enumerate only what fired; leave unscanned layers undocumented | **anonymous layer gap** — named layer disposition absent; unscanned layers produce candidates that cannot be confirmed absent vs. present-but-not-firing | N/A (exclusion log SHALL be complete before any candidate is named; timing is pre-candidate by construction) | Auditor \| Phase 0 |
| The Domain Expert SHALL produce the EOR TABLE (ART-03) during Phase 0 before Phase 1 begins | SATISFIED | Violated if any firing entry is positioned without an inline EOR rule ID citation | Ordering rationale stated as prose before enumeration ("sync before async") | **anonymous ordering rule** — rule IDs absent; per-entry position unauditable by rule citation | N/A (one-time static declaration; no lifecycle transition activates it — declared once and referenced throughout) | Domain Expert \| Phase 0 |
| The Domain Expert SHALL produce the CASCADE DEPTH BUDGET (ART-04) during Phase 0 before Phase 4 begins | SATISFIED | Violated if any cascade chain entry lacks a [Depth: N/MAX] counter showing position against declared maximum | Trace chains without a named depth ceiling | **invisible overflow** — depth budget absent; chains exceeding undeclared limit produce no counter signal | Activates at Phase 4 cascade tracing (enforcement begins at the first cascade entry) | Domain Expert \| Phase 0 |
| The Auditor SHALL produce PROHIBITION CONTRACTS (ART-05) during Phase 0 before roles operate | SATISFIED | Violated if any prohibition lacks a named Applies After event referencing a Phase 0 or Phase 1 lifecycle transition | Timeless global prohibition without lifecycle scope | **anonymous prohibition** — temporal activation anchor absent; effective period undefined; enforcement depends on phase-ordering inference | N/A (each prohibition within the contract body carries its own Applies After field) | Auditor \| Phase 0 |
| The Auditor SHALL produce the ARTIFACT MANIFEST (ART-06) during Phase 0 before enumeration begins | SATISFIED | Violated if any manifest entry lacks BOTH producing role AND producing phase as named fields (either field alone is insufficient) | Artifact checklist with IDs but no role or phase attribution | **anonymous artifact gap** — producing role and phase absent; missing artifact cannot be attributed to responsible role and phase from manifest alone | N/A (static pre-enumeration declaration; no lifecycle event triggers creation) | Auditor \| Phase 0 |
| The Auditor SHALL declare the BREACH TOKEN PROTOCOL during Phase 0 before PROHIBITION CONTRACTS activate | SATISFIED | Violated if no named breach token format string is declared before prohibitions are active | Detect prohibition violations only through post-hoc rubric re-evaluation | **invisible breach** — named token format absent; violations produce no inline signal; undetectable without external rubric | Activates alongside PROHIBITION CONTRACTS (Phase 0) | Auditor \| Phase 0 |

*(SCOPE GATE VALUES, EXCLUSION LOG, EOR TABLE, CASCADE DEPTH BUDGET, PROHIBITION CONTRACTS,
ARTIFACT MANIFEST identical to V-01.)*

---

#### INERTIA CONTRAST

*(Failure modes, DERIVATION TEST, and constraint propagation verification identical to V-01.)*

---

**Phase 0 Exit Signal:** 7/7 SATISFIED — enumeration authorized.

**Exit condition:** Phase 0 SHALL be complete when all 7 registry rows carry Status: SATISFIED
and exit signal is issued. Phase 1 SHALL NOT begin before this exit signal.

---

### STRUCTURAL INVARIANT LAYER

*(Identical to V-01.)*

---

### LIFECYCLE OVERVIEW

*(Identical to V-01.)*

---

### Phase 1 — Pre-scan

**Why Phase 1 exists before Phase 2:** Without denominator declaration, enumeration cannot be
verified complete. Phase 1 produces the denominator count N before any candidate is filtered
by execution tier. Phase 2 and Phase 3 resolve candidates against N; without N, omissions are
not detectable as structural gaps — they are only discoverable through external review.

*(Entry condition, Job, Anomaly Questions, Denominator Pre-Scan, PCC-1, Exit condition
identical to V-01.)*

---

### Phase 2 — Sync Trigger Enumeration

**Why Phase 2 precedes Phase 3:** Synchronous triggers execute within the originating
transaction — they can abort the change, mutate fields that async triggers later read, or
produce side effects before the record is committed. Enumerating sync triggers first preserves
execution-order fidelity: every async trigger enumerated in Phase 3 sees the post-sync field
state, not the pre-change field state.

*(Entry condition, Job, Negative vocabulary example, Sync Trigger Table, Exit condition
identical to V-01.)*

---

### Phase 3 — Async Trigger Enumeration

**Why Phase 3 follows Phase 2 and precedes Phase 4:** Async triggers execute outside the
transaction on the committed record. Their inputs are the post-sync field values, not the
triggering field values. Phase 3 cannot begin until Phase 2 establishes the post-sync state
baseline; Phase 4 cannot begin until Phase 3 establishes all async side effects for cascade
tracing.

*(Entry condition, Job, Async Trigger Table, Exit condition identical to V-01.)*

---

### Phase 4 — Cascade Tracing

**Why Phase 4 exists before Phase 5:** Without cascade tracing, anomaly assessment operates
on first-order triggers only. Trigger storms frequently manifest in second- and third-order
cascade writes. Circular triggers are back-edges in the cascade graph — they are invisible
without graph construction. Phase 4 must complete before Phase 5 can cite cascade chain rows
as evidence in anomaly verdicts.

*(Entry condition, Job, Cascade Chain Table, Exit condition identical to V-01.)*

---

### Phase 5 — Anomaly Assessment

**Why Phase 5 precedes Phase 6:** Anomaly verdicts must be issued and cited before the trigger
map can classify each trigger's Anomaly Flag column. A trigger map produced before anomaly
assessment is an unevaluated inventory; after assessment, each row's Anomaly Flag carries an
evidence-backed verdict. Phase 6 closure depends on Phase 5 completing all three verdicts.

*(Entry condition, Job, Trigger Storm, Missing Trigger, Circular Trigger, Exit condition
identical to V-01.)*

---

### Phase 6 — Trigger Map and Closure

**Why Phase 6 closes the analysis:** Phases 1–5 produce trigger entries and anomaly verdicts
but no single artifact verifies that every candidate from the denominator declaration is
accounted for and that every Phase 0 artifact was produced by its named responsible role.
The CLOSURE CHECK performs this verification: it counts structural gaps per obligation class
and confirms each Phase 0 artifact was produced by the role named in the ARTIFACT MANIFEST.

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
---- NOTE: ATTRIBUTION CHAIN ------------------------------------------------
DECLARATION TIME ATTRIBUTION (ART-06):        present [must be present — ARTIFACT MANIFEST names producing role and phase pre-enumeration; accountability auditable before any gap forms]
DETECTION TIME ATTRIBUTION (ART-NN counters): present [must be present]
---- END NOTE ---------------------------------------------------------------
```

**Exit condition:** Phase 6 SHALL be complete when trigger map covers all triggers with
required columns and closure check is stated.

---

## V-04

**Variation axis:** Combined — inertia framing (INERTIA CONTRAST extended with DUAL-TIME
ATTRIBUTION CHAIN entry) + phrasing register (full SHALL/MUST throughout) + NOTE block inside
CLOSURE CHECK code fence using pure assertion register with fully extended brackets (C-42
PASS) but no REMEDIATION SELF-SUFFICIENCY assertion (C-43 FAIL).

**Hypothesis:** The PHASE 0 OBLIGATION REGISTRY carries complete four-component obligation text
(C-38 PASS). The INERTIA CONTRAST section adds a seventh entry for the dual-time attribution
chain — naming the weaker alternative (declaration-time attribution only, no counter-level
attribution), the failure mode (**anonymous detection-time attribution**), and the structural
consequence. C-39 PASS via INERTIA CONTRAST mechanism path. The CLOSURE CHECK carries per-
counter inline role attribution (C-37 PASS) and a named NOTE block embedded inside the code
fence (C-40 PASS). The NOTE block uses pure assertion register throughout (C-41 PASS): no prose
sentence appears inside the NOTE block. Both NOTE assertions use the extended bracket form:
`[must be present — inline rationale clause]` — rationale is syntax-bound inside each bracket,
not expressed as a separate line (C-42 PASS). However, the NOTE block carries only the two
element-presence assertions (DECLARATION TIME and DETECTION TIME). The combined-system property
— that removing either layer breaks remediation self-sufficiency — is inferable from reading
both assertions and their rationale clauses together, but is never stated as a named
REMEDIATION SELF-SUFFICIENCY assertion with its own `PROPERTY: VALUE [must be VALUE]` line.
C-43 FAIL: a reader scanning the NOTE block sees element presence asserted; the systemic
guarantee is derivable but not declared as a first-class detection target.

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

**Entry condition:** Phase 0 SHALL begin when scenario specification is received and PROTOCOL
PREAMBLE declared complete.

**Job:** Phase 0 SHALL produce and lock all pre-enumeration obligations in the PHASE 0
OBLIGATION REGISTRY. Each row SHALL carry all six metadata types as named columns. No
obligation's compliance SHALL require navigation outside its row.

**BREACH TOKEN PROTOCOL:** `[PROHIBITION BREACH: Role | {prohibition name} | FM-NN]`

#### PHASE 0 OBLIGATION REGISTRY

| Obligation | Status | Refutation Condition | Weaker Alternative | Failure Mode | Activation Event | Producing Role |
|------------|--------|---------------------|--------------------|--------------|-----------------|----------------|
| The Auditor SHALL produce the SCOPE GATE (ART-01) during Phase 0 before any candidate is named | SATISFIED | Violated if any candidate named before event tuple (entity, operation, field, prev value, new value) declared as named artifact with all five fields | Prose scope sentence — no named structural artifact | **anonymous scope boundary** — event tuple absent; no candidate structurally excludable; scope requires prose interpretation | N/A (static pre-execution; no lifecycle transition activates it) | Auditor \| Phase 0 |
| The Auditor SHALL produce the EXCLUSION LOG (ART-02) during Phase 0 before any candidate is named | SATISFIED | Violated if any layer evaluated without named disposition row before candidates listed | Enumerate only what fired | **anonymous layer gap** — disposition absent; unscanned layers unverifiable | N/A (pre-candidate by construction) | Auditor \| Phase 0 |
| The Domain Expert SHALL produce the EOR TABLE (ART-03) during Phase 0 before Phase 1 begins | SATISFIED | Violated if any firing entry lacks inline EOR rule ID citation | Ordering stated as prose | **anonymous ordering rule** — rule IDs absent; position unauditable by citation | N/A (one-time static declaration) | Domain Expert \| Phase 0 |
| The Domain Expert SHALL produce the CASCADE DEPTH BUDGET (ART-04) during Phase 0 before Phase 4 begins | SATISFIED | Violated if any cascade entry lacks [Depth: N/MAX] counter | Trace without declared depth ceiling | **invisible overflow** — depth budget absent; no counter signal at overflow | Activates at Phase 4 | Domain Expert \| Phase 0 |
| The Auditor SHALL produce PROHIBITION CONTRACTS (ART-05) during Phase 0 before roles operate | SATISFIED | Violated if any prohibition lacks named Applies After event referencing Phase 0 or Phase 1 transition | Timeless global prohibition | **anonymous prohibition** — temporal anchor absent; effective period undefined | N/A (each row within the contract body carries its own Applies After field) | Auditor \| Phase 0 |
| The Auditor SHALL produce the ARTIFACT MANIFEST (ART-06) during Phase 0 before enumeration begins | SATISFIED | Violated if any entry lacks BOTH producing role AND producing phase | ID-only artifact list | **anonymous artifact gap** — producing role and phase absent; gap unattributable | N/A (static pre-enumeration declaration) | Auditor \| Phase 0 |
| The Auditor SHALL declare the BREACH TOKEN PROTOCOL during Phase 0 before PROHIBITION CONTRACTS activate | SATISFIED | Violated if no named token format string declared before prohibitions active | Post-hoc rubric re-evaluation for violations | **invisible breach** — token format absent; violations undetectable inline | Activates alongside PROHIBITION CONTRACTS | Auditor \| Phase 0 |

*(SCOPE GATE VALUES, EXCLUSION LOG, EOR TABLE, CASCADE DEPTH BUDGET, PROHIBITION CONTRACTS,
ARTIFACT MANIFEST identical to V-01.)*

---

#### INERTIA CONTRAST

**SCOPE GATE (event tuple vs. prose preamble):**
- Weaker alternative: Narrative sentence naming the change context
- Failure mode: **anonymous scope boundary** — event tuple absent; scope requires prose
  interpretation

**PROHIBITION CONTRACTS (temporal anchor vs. timeless prohibition):**
- Weaker alternative: Global prohibition without lifecycle reference
- Failure mode: **anonymous prohibition** — temporal anchor absent; effective period undefined;
  enforcement depends on phase-ordering inference

**ARTIFACT MANIFEST (role-attributed vs. ID-only):**
- Weaker alternative: Artifact list with IDs but no producing role or phase columns
- Failure mode: **anonymous artifact gap** — producing role and phase absent; gap unattributable
  from manifest alone

**DUAL-TIME ATTRIBUTION CHAIN (ARTIFACT MANIFEST + CLOSURE CHECK counter):**
- Weaker alternative: Role attribution at declaration time only — ARTIFACT MANIFEST names the
  producing role; CLOSURE CHECK counter carries artifact ID and status but no role attribution
- Failure mode: **anonymous detection-time attribution** — counter level carries no role
  attribution; a reader finding an ABSENT counter must navigate to the ARTIFACT MANIFEST as a
  secondary lookup to identify the remediation target; if that navigation fails (reader stops at
  the CLOSURE CHECK), the remediation target is unidentified. Both layers are required: the
  ARTIFACT MANIFEST establishes accountability before any gap can form; the CLOSURE CHECK counter
  makes the remediation target determinable at the point of detection without secondary
  navigation. Removing either layer breaks remediation self-sufficiency.

**DERIVATION TEST**

| Failure Mode Label | Absent Structural Property | Derived Minimum Implementation |
|-------------------|---------------------------|-------------------------------|
| **anonymous scope boundary** | Named event tuple as structural artifact with named fields | Scope boundary SHALL be a named artifact. Minimum: structural artifact with entity, operation, field, prev-value, new-value as named fields. |
| **anonymous layer gap** | Named disposition row per automation layer swept | Each layer swept SHALL carry a named disposition row. Minimum: table with layer, disposition, reason columns. |
| **anonymous ordering rule** | Named rule ID per ordering principle | Each ordering principle SHALL carry an assigned rule ID. Each firing entry SHALL cite its rule ID inline. |
| **anonymous prohibition** | Named temporal activation anchor ("Applies After" field) | Each prohibition SHALL carry a named Applies After event. Minimum: prohibition table with Applies After column. |
| **anonymous artifact gap** | Named producing role AND named producing phase | Each manifest entry SHALL carry both fields. Either alone is insufficient. |
| **invisible breach** | Named breach token format declared before prohibitions activate | A named token string SHALL be declared and used inline at point of violation. |
| **anonymous detection-time attribution** | Role attribution at counter level in CLOSURE CHECK | Each CLOSURE CHECK artifact production counter SHALL name the producing role and phase inline. Both ARTIFACT MANIFEST attribution and CLOSURE CHECK counter attribution SHALL be declared and maintained together. |

**Constraint propagation verification:** A reader who reads only the Failure Mode column SHALL
be able to derive the minimum implementation for every Phase 0 obligation and for the
dual-time attribution chain without rubric access.

---

**Phase 0 Exit Signal:** 7/7 SATISFIED — enumeration authorized.

**Exit condition:** Phase 0 SHALL be complete when all 7 registry rows carry Status: SATISFIED
and exit signal is issued.

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
---- NOTE: ATTRIBUTION CHAIN ------------------------------------------------
DECLARATION TIME ATTRIBUTION (ART-06):        present [must be present — ARTIFACT MANIFEST names producing role and phase pre-enumeration; accountability auditable before any gap forms]
DETECTION TIME ATTRIBUTION (ART-NN counters): present [must be present — each counter names producing role and phase inline; remediation target determinable at point of detection without secondary navigation to ARTIFACT MANIFEST]
---- END NOTE ---------------------------------------------------------------
```

**Exit condition:** Phase 6 SHALL be complete when trigger map covers all triggers with
required columns and closure check is stated.

---

## V-05

**Variation axis:** Combined — phrasing register (full SHALL/MUST formal imperative throughout)
+ extended bracket form (all NOTE assertions use `[must be VALUE — inline rationale clause]`,
C-42 PASS) + systemic-property assertion (REMEDIATION SELF-SUFFICIENCY added as third NOTE
assertion, C-43 PASS).

**Hypothesis:** The PHASE 0 OBLIGATION REGISTRY carries complete four-component obligation text
(C-38 PASS). The INERTIA CONTRAST section covers all seven mechanism entries: six Phase 0
mechanisms plus DUAL-TIME ATTRIBUTION CHAIN (identical to V-04). C-39 PASS via INERTIA
CONTRAST mechanism path. The CLOSURE CHECK carries per-counter inline role attribution (C-37
PASS) and a named NOTE block embedded inside the code fence (C-40 PASS).

The NOTE block has three properties that jointly satisfy C-41, C-42, and C-43:

**C-41 (register uniformity):** Every line inside the NOTE block uses the same
`PROPERTY: VALUE [must be CONSTRAINT]` assertion register as the surrounding counters. No prose
sentence appears inside the NOTE block. A reader scanning the CLOSURE CHECK cannot distinguish
the NOTE's assertion lines from the counter entries by register alone.

**C-42 (extended bracket form):** Every NOTE assertion uses the extended form
`[must be VALUE — inline rationale clause]`. The rationale is syntax-bound inside the bracket:
removing the rationale requires editing the bracket value, not deleting a separate element. Both
DECLARATION TIME and DETECTION TIME assertions carry inline rationale inside their brackets —
the extension is applied uniformly, not selectively.

**C-43 (systemic-property assertion):** A third assertion —
`REMEDIATION SELF-SUFFICIENCY: maintained [must be maintained — ...]` — asserts a higher-order
property of the two-element combination, not either element alone. The subject is a derived
guarantee: maintaining REMEDIATION SELF-SUFFICIENCY requires BOTH attribution layers to be
present; removing either layer breaks the guarantee. This assertion is independently falsifiable:
it fails if either element is absent, and the consequence is stated inside the bracket. A reader
scanning the CLOSURE CHECK can identify REMEDIATION SELF-SUFFICIENCY as a first-class detection
target — it is a named assertion, not an inference from element presence.

The combined-axis signal (phrasing register + extended bracket + systemic assertion) is
non-trivial: C-40 provides structural containment (NOTE inside fence); C-41 provides semantic
co-domain (NOTE assertions peer to counter assertions); C-42 provides syntactic co-location of
constraint and justification (rationale inside bracket); C-43 provides functional completeness
(the combined-system guarantee is explicitly asserted, not only inferable). All four are required
for the NOTE block to serve as a self-contained detection record for the dual-time attribution
design.

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

*(Phase 0 Job, BREACH TOKEN PROTOCOL, and PHASE 0 OBLIGATION REGISTRY with complete
four-component formal imperative obligation text identical to V-03. SCOPE GATE VALUES,
EXCLUSION LOG, EOR TABLE, CASCADE DEPTH BUDGET, PROHIBITION CONTRACTS, and ARTIFACT MANIFEST
identical to V-01, with all gate statements using SHALL/MUST throughout.)*

---

#### INERTIA CONTRAST

*(All six original Phase 0 mechanism entries plus the DUAL-TIME ATTRIBUTION CHAIN entry
identical to V-04. DERIVATION TEST covers all seven mechanisms. Constraint propagation
verification statement identical to V-04.)*

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
---- NOTE: ATTRIBUTION CHAIN REGISTER ----------------------------------------
DECLARATION TIME ATTRIBUTION (ART-06):        present [must be present — ARTIFACT MANIFEST names producing role and phase pre-enumeration; accountability auditable before any gap forms]
DETECTION TIME ATTRIBUTION (ART-NN counters): present [must be present — each counter names producing role and phase inline; remediation target determinable at point of detection without secondary navigation to ARTIFACT MANIFEST]
REMEDIATION SELF-SUFFICIENCY:                 maintained [must be maintained — removing either attribution layer breaks self-sufficiency; removal is not a coverage reduction]
---- END NOTE ----------------------------------------------------------------
```

**Exit condition:** Phase 6 SHALL be complete when trigger map covers all triggers with
required columns and closure check is stated.
