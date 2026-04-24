---
skill: flow-trigger
source: flow-trigger-variate-R20-2026-03-16.md V-05
rubric_version: 17
qu5_pass: true
date: 2026-03-16
---

# flow-trigger -- QU5 Simplified Golden Prompt

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

### PHASE 0 -- PREPARATION

**Forward dependency for Phase 1:** Phase 1 requires all seven Phase 0 artifacts locked before
any candidate is named. If Phase 1 begins before Phase 0 completes, **pre-enumeration state
collapse** occurs: candidates are evaluated without a scope boundary, layer sweep record,
ordering rules, or cascade depth ceiling.

**Entry condition:** Phase 0 SHALL begin when scenario specification is received and PROTOCOL
PREAMBLE declared complete.

**Job:** Phase 0 SHALL produce and lock all pre-enumeration obligations in the PHASE 0
OBLIGATION REGISTRY before Phase 1 begins.

**BREACH TOKEN PROTOCOL:** `[PROHIBITION BREACH: Role | {prohibition name} | FM-NN]`

#### PHASE 0 OBLIGATION REGISTRY

*(Row order: Domain Expert obligations first -- declaration-time artifact producers; Auditor
obligations follow -- verification-time enforcers.)*

| Obligation | Status | Refutation Condition | Weaker Alternative | Failure Mode | Activation Event | Producing Role |
|------------|--------|---------------------|--------------------|--------------|-----------------|----------------|
| The Domain Expert SHALL produce the EOR TABLE (ART-03) during Phase 0 before Phase 1 begins | SATISFIED | Any firing entry lacks inline EOR rule ID citation | Prose ordering rationale | **anonymous ordering rule** | N/A | Domain Expert \| Phase 0 |
| The Domain Expert SHALL produce the CASCADE DEPTH BUDGET (ART-04) during Phase 0 before Phase 4 begins | SATISFIED | Any cascade chain entry lacks a [Depth: N/MAX] counter | Trace chains without a named depth ceiling | **invisible overflow** | Activates at Phase 4 cascade tracing | Domain Expert \| Phase 0 |
| The Auditor SHALL produce the SCOPE GATE (ART-01) during Phase 0 before any candidate is named | SATISFIED | Any candidate named before the event tuple (entity, operation, field, prev, new) appears as a named artifact | Prose scope sentence | **anonymous scope boundary** | N/A | Auditor \| Phase 0 |
| The Auditor SHALL produce the EXCLUSION LOG (ART-02) during Phase 0 before any candidate is named | SATISFIED | Any automation layer evaluated without a named disposition row | Enumerate only included layers | **anonymous layer gap** | N/A | Auditor \| Phase 0 |
| The Auditor SHALL produce PROHIBITION CONTRACTS (ART-05) during Phase 0 before roles operate | SATISFIED | Any prohibition lacks a named Applies After lifecycle event | Timeless global prohibition | **anonymous prohibition** | N/A | Auditor \| Phase 0 |
| The Auditor SHALL produce the ARTIFACT MANIFEST (ART-06) during Phase 0 before enumeration begins | SATISFIED | Any manifest entry lacks BOTH producing role AND producing phase | ID-only artifact list | **anonymous artifact gap** | N/A | Auditor \| Phase 0 |
| The Auditor SHALL declare the BREACH TOKEN PROTOCOL during Phase 0 before PROHIBITION CONTRACTS activate | SATISFIED | No named breach token format string declared before prohibitions active | Post-hoc violation detection only | **invisible breach** | Activates alongside PROHIBITION CONTRACTS | Auditor \| Phase 0 |

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
- Failure mode: **anonymous scope boundary** -- event tuple absent; scope requires prose
  interpretation

**PROHIBITION CONTRACTS (temporal anchor vs. timeless prohibition):**
- Weaker alternative: Global prohibition without lifecycle reference
- Failure mode: **anonymous prohibition** -- temporal anchor absent; effective period undefined;
  enforcement depends on phase-ordering inference

**ARTIFACT MANIFEST (role-attributed vs. ID-only):**
- Weaker alternative: Artifact list with IDs but no producing role or phase columns
- Failure mode: **anonymous artifact gap** -- producing role and phase absent; gap unattributable
  from manifest alone

**DUAL-TIME ATTRIBUTION CHAIN (ARTIFACT MANIFEST + CLOSURE CHECK counter):**
- Weaker alternative: Role attribution at declaration time only -- ARTIFACT MANIFEST names the
  producing role; CLOSURE CHECK counter carries artifact ID and status but no role attribution
- Failure mode: **anonymous detection-time attribution** -- counter level carries no role
  attribution; a reader finding an ABSENT counter must navigate to the ARTIFACT MANIFEST as a
  secondary lookup; if that navigation fails, the remediation target is unidentified. Both
  layers are required: the ARTIFACT MANIFEST establishes accountability before any gap can form;
  the CLOSURE CHECK counter makes the remediation target determinable at the point of detection
  without secondary navigation. Removing either layer breaks remediation self-sufficiency.

**DERIVATION TEST**

| Failure Mode Label | Absent Structural Property | Derived Minimum Implementation |
|-------------------|---------------------------|-------------------------------|
| **anonymous scope boundary** | Named event tuple as structural artifact with named fields | Scope boundary SHALL be a named artifact. Minimum: entity, operation, field, prev-value, new-value as named fields. |
| **anonymous layer gap** | Named disposition row per automation layer swept | Each layer swept SHALL carry a named disposition row. Minimum: table with layer, disposition, reason columns. |
| **anonymous ordering rule** | Named rule ID per ordering principle | Each ordering principle SHALL carry an assigned rule ID. Each firing entry SHALL cite its rule ID inline. |
| **anonymous prohibition** | Named temporal activation anchor ("Applies After" field) | Each prohibition SHALL carry a named Applies After event. Minimum: prohibition table with Applies After column. |
| **anonymous artifact gap** | Named producing role AND named producing phase | Each manifest entry SHALL carry both fields. Either alone is insufficient. |
| **invisible breach** | Named breach token format declared before prohibitions activate | A named token string SHALL be declared and used inline at point of violation. |
| **anonymous detection-time attribution** | Role attribution at counter level in CLOSURE CHECK | Each CLOSURE CHECK artifact counter SHALL name the producing role and phase inline. Both ARTIFACT MANIFEST and CLOSURE CHECK counter attribution SHALL be declared together. |

**Constraint propagation verification:** A reader who reads only the Failure Mode column SHALL
be able to derive the minimum implementation for every obligation without rubric access.

---

**Phase 0 Exit Signal:** 7/7 SATISFIED -- enumeration authorized.

**Exit condition:** Phase 0 SHALL be complete when all 7 registry rows carry Status: SATISFIED
and exit signal is issued. No enumeration entry SHALL appear before this signal.

---

### Phase 1 -- Pre-scan

**Forward dependency for Phase 2:** Phase 2 requires denominator N declared and all three
anomaly slots OPEN before sync-tier enumeration begins. If Phase 2 begins before Phase 1
declares N, **denominator-free enumeration** occurs: trigger entries are added without a
declared population count; omissions are structurally invisible.

**Entry condition:** Phase 1 SHALL begin when Phase 0 exit signal is issued.

**Job:** Identify all candidate triggers without condition filtering. Declare denominator N.
Open all three anomaly question slots. Issue Phrasing Clearance PCC-1 if zero register
violations found.

**Anomaly Questions -- Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does this change cause more triggers than the environment can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for account inactivation that does not fire? | OPEN |
| Circular Trigger | Does any trigger's output re-activate an upstream trigger? | OPEN |

**Denominator Pre-Scan:**

| Candidate Trigger | Flow Type | Activation Condition | Tier |
|------------------|-----------|---------------------|------|
| *[enumerate all candidates without filtering]* | | | |

N = *[integer -- declare before Phase 2]*

**PCC-1:** Issued when zero FM-08/FM-16/FM-17 markers found in Phase 0 and preamble.

**Exit condition:** Phase 1 SHALL be complete when N is declared, all three anomaly slots are
OPEN, and PCC-1 is issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Forward dependency for Phase 3:** Phase 3 requires the Sync Trigger Table produced with all
sync-tier candidates resolved before async-tier enumeration begins. Async triggers execute on
the post-sync committed record state. If Phase 3 begins before Phase 2 produces the Sync
Trigger Table, **post-sync state ambiguity** occurs: async input fields are enumerated against
an unknown post-sync field state.

**Entry condition:** Phase 2 SHALL begin when Phase 1 is complete, N declared, PCC-1 issued.

**Job:** Enumerate all synchronous triggers using FIRING ENTRY or NON-FIRING ENTRY schema.
Include at least one negative vocabulary example. Order by execution priority per EOR table.

**Negative vocabulary example (required):** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | EOR Citation | Registration | Depth | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|-------------|-------|-------------|

**Exit condition:** Phase 2 SHALL be complete when every sync-tier candidate has a resolved
entry with all schema slots populated.

---

### Phase 3 -- Async Trigger Enumeration

**Forward dependency for Phase 4:** Phase 4 requires the Async Trigger Table produced with all
async-tier candidates resolved before cascade tracing begins. If Phase 4 begins before Phase 3
completes, **incomplete cascade basis** occurs: cascade tracing begins before all first-order
triggers are declared; side-effect writes from undeclared async triggers are absent from the
cascade graph.

**Entry condition:** Phase 3 SHALL begin when Phase 2 is complete and Sync Trigger Table
produced.

**Job:** Enumerate all async-tier candidates. Annotate latency tier per entry.

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | EOR Citation | Registration | Depth | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|-------------|-------|-------------|

**Exit condition:** Phase 3 SHALL be complete when every async-tier candidate has a resolved
entry with all slots populated.

---

### Phase 4 -- Cascade Tracing

**Forward dependency for Phase 5:** Phase 5 requires all cascade chains to carry Chain-Status
and back-edge detection applied before anomaly assessment begins. If Phase 5 begins before
Phase 4 completes, **evidence-free anomaly verdict** occurs: every verdict requires
`[INSUFFICIENT: cascade evidence absent | FM-12]`.

**Entry condition:** Phase 4 SHALL begin when Phases 2 and 3 are complete and both tables
produced.

**Job:** Trace cascade chains from side-effect field writes. Assign Chain IDs (CH-01, CH-02,
...). Apply `[Depth: N/5]` counter per cascade entry. Apply back-edge detection. Mark final
chain row `[TERMINAL]`. Issue `[DEPTH EXCEEDED: CH-NN]` if any chain exceeds MAX_DEPTH.

**Cascade Chain Table:**

| Chain ID | Depth | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|-------|--------------------|--------------------|--------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be complete when all side-effect writes evaluated, all
chains carry Chain-Status, back-edge detection applied.

---

### Phase 5 -- Anomaly Assessment

**Forward dependency for Phase 6:** Phase 6 requires all three anomaly verdicts issued with
cited evidence before the trigger map is finalized. If Phase 6 begins before Phase 5 completes,
**unevaluated trigger map** occurs: Anomaly Flag values are assigned without evidence citations.

**Entry condition:** Phase 5 SHALL begin when Phase 4 is complete and all chains carry
Chain-Status.

**Job:** Evidence-anchored verdicts for all three anomaly classes. Cite specific trigger rows.
Propose remediation per confirmed anomaly. Produce adjacency list (trigger graph).

**Trigger Storm:** Evidence: *[rows]* | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Missing Trigger:** Evidence: *[rows]* | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Circular Trigger:** Evidence: *[rows]* | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Exit condition:** Phase 5 SHALL be complete when all three verdicts are issued with cited
evidence and every confirmed anomaly has at least one remediation.

---

### Phase 6 -- Trigger Map and Closure

**Closing dependency statement:** Phases 1-5 produce trigger entries and anomaly verdicts but
no single artifact verifies that every denominator candidate is accounted for and every Phase 0
artifact was produced by its named responsible role. Phase 6 closes this gap: the CLOSURE CHECK
counts structural gaps per obligation class, confirms each Phase 0 artifact was produced by the
role named in the ARTIFACT MANIFEST, and issues the denominator reconciliation.

**Entry condition:** Phase 6 SHALL begin when Phase 5 is complete and all anomaly verdicts
issued.

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
ART-01 (SCOPE GATE)            -- Auditor, Phase 0:        PRODUCED [must be PRODUCED]
ART-02 (EXCLUSION LOG)         -- Auditor, Phase 0:        PRODUCED [must be PRODUCED]
ART-03 (EOR TABLE)             -- Domain Expert, Phase 0:  PRODUCED [must be PRODUCED]
ART-04 (CASCADE DEPTH BUDGET)  -- Domain Expert, Phase 0:  PRODUCED [must be PRODUCED]
ART-05 (PROHIBITION CONTRACTS) -- Auditor, Phase 0:        PRODUCED [must be PRODUCED]
ART-06 (BREACH TOKEN PROTOCOL) -- Auditor, Phase 0:        PRODUCED [must be PRODUCED]
PROHIBITION BREACHES:                                                 0 [must be 0]
---- NOTE: ATTRIBUTION CHAIN REGISTER ----------------------------------------
DECLARATION TIME ATTRIBUTION (ART-06):        present [must be present -- ARTIFACT MANIFEST names producing role and phase pre-enumeration; accountability auditable before any gap forms]
DETECTION TIME ATTRIBUTION (ART-NN counters): present [must be present -- each counter names producing role and phase inline; remediation target determinable at point of detection without secondary navigation to ARTIFACT MANIFEST]
REMEDIATION SELF-SUFFICIENCY:                 maintained [must be maintained -- removing either attribution layer breaks self-sufficiency; this is a structural failure, not a coverage reduction]
---- END NOTE ----------------------------------------------------------------
```

**Exit condition:** Phase 6 SHALL be complete when trigger map covers all triggers with
required columns and closure check is stated.
