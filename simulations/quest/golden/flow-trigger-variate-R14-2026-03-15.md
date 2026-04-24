---
skill: flow-trigger
round: 14
rubric_version: 13
new_criteria: [C-46]
date: 2026-03-15
---

# flow-trigger -- Round 14 (Rubric v13) Variations

**New criterion this round:**
- **C-46** -- Non-exemption clause includes operational restatement defining the exempted rationale -- the non-exemption clause (C-42) asserts that no artifact surface is exempt from the register invariant by virtue of its summary function. This criterion requires the clause to additionally include an immediate operational restatement that defines what "summary-function rationale" means in concrete terms -- specifically, a second clause (typically introduced with an em-dash or equivalent) stating that "the summary or overview nature of an artifact does not confer exemption from the formal-register obligation" or equivalent. Without this restatement, a reader can invoke a narrow interpretation of "summary-function rationale" and argue that only artifacts explicitly labeled "summary" fall within the clause's scope, leaving artifacts labeled "overview", "digest", or "index" as arguably uncovered. The operational restatement closes this interpretive gap by defining the blocked rationale within the clause itself: the phrase "summary or overview nature" is stated explicitly, blocking the argument that unlabeled-summary artifacts escape the scope. C-42 requires artifact-agnostic scope; this criterion requires the clause to also name the blocked rationale in operational terms, so both the scope (any artifact surface) and the specific rationale being nullified (the summary-or-overview-nature argument) are made explicit within a single clause, making the non-exemption assertion self-sealing against interpretive wedge arguments. An output whose non-exemption clause uses artifact-agnostic scope (passing C-42) but provides no operational definition of the exempted rationale fails this criterion.

**Round 13 gap analysis:**
- V-01: C-46 ABSENT -- no em-dash restatement at all (only artifact-agnostic scope phrase present in Invariant 3)
- V-02: C-46 ABSENT -- em-dash present but uses generic structural-role language ("an artifact's structural role does not confer exemption") instead of naming "summary or overview nature"
- V-03: C-46 ABSENT -- "summary or overview nature" language correct but appears as a separate sentence ("For clarity: the summary or overview nature...") not an em-dash clause immediately following the scope assertion
- V-04: C-46 ABSENT -- em-dash present but only "summary nature" (not "summary or overview") -- leaves "overview" as a potentially unblocked label
- V-05: C-46 PASS -- em-dash + "summary or overview nature" + artifact-agnostic scope = self-sealing; this is the C-46 pass baseline carried into R14

**Variation axes:**

| Variation | Axis | C-46 status | Hypothesis |
|-----------|------|-------------|------------|
| V-01 | Phrasing register axis -- weak em-dash: organizational-structure framing | C-46 FAIL | Invariant 3 has artifact-agnostic scope (C-42 passes) but the em-dash restatement uses "organizational structure" framing rather than naming the summary-or-overview rationale; "a document's organizational structure does not establish register exemptions for its constituent artifacts" is more generic than "structural role" -- it doesn't block the summary-function argument at all; a reader invoking summary-function exemption against the formal-register obligation can still argue the clause addresses only structural-role arguments, not summary-function arguments |
| V-02 | Output format axis -- wrong obligation in restatement | C-46 FAIL | Invariant 3 has the em-dash with correct "summary or overview nature" first part but names the wrong obligation: "does not confer exemption from the platform-vocabulary obligation" instead of "from the formal-register obligation"; C-42 passes; C-46 fails because the operational restatement names the wrong obligation -- a reader invoking the summary-function rationale against the FORMAL-REGISTER obligation can argue the clause blocks only platform-vocabulary exemptions, not formal-register exemptions |
| V-03 | Lifecycle emphasis axis -- correct language, wrong structural placement | C-46 FAIL | Invariant 3 has C-46-correct language but the non-exemption clause appears as a parenthetical AFTER the verifier instruction rather than immediately after the scope assertion; the em-dash still exists but is detached by intervening verifier text; C-42 passes; C-46 fails because the "immediate" co-location requirement is a structural constraint -- the operational definition must directly follow the scope assertion without intervening text |
| V-04 | Phrasing register + output format combination -- correct nature phrase, missing obligation target | C-46 FAIL | Invariant 3 has em-dash + "summary or overview nature" + artifact-agnostic scope, but the restatement uses passive voice without an obligation verb: "does not confer register-exemption status" -- the obligation target "from the formal-register obligation" is omitted; C-42 passes; C-46 fails because the restatement must name the obligation being denied; "register-exemption status" without naming what obligation is not exempted leaves the blocked rationale incomplete |
| V-05 | Full combination -- all axes: C-46 PASS + BONUS SIGNAL (C-47 candidate) | C-46 PASS | Invariant 3 has the full C-46 pass text; additionally, FORMAL-GATE ZONE DECLARATION Rule 1 is extended with a co-authority non-exemption sub-clause making Rule 1 independently informative about what the co-authority prohibits -- a reader checking Rule 1 does not need to consult Invariant 3 to understand that the co-authority also prohibits summary-or-overview exemptions; this is the bonus signal candidate for C-47 |

**Scenario used in all variations:** A Dataverse `incident` record's `statuscode` field has changed from `In Progress` (2) to `Resolved` (5). Your task: determine exactly which automations fire, in what order, with what inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular triggers).

---

## V-01

**Variation axis:** Phrasing register -- weak em-dash restatement using organizational-structure framing instead of summary-or-overview-nature framing
**Hypothesis:** Invariant 3 carries artifact-agnostic scope ("for any artifact surface") so C-42 passes. The em-dash restatement says "a document's organizational structure does not establish register exemptions for its constituent artifacts" -- this is organizational-structure framing, which is even more generic than "structural role" framing. It does not name the summary-function rationale being blocked. A reader invoking a summary-function argument against the formal-register obligation can argue that the em-dash clause addresses only organizational-structure arguments and that summary-function rationale is a separate, unblocked argument path. C-46 fails because the operational restatement does not name the blocked rationale in concrete terms.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dataverse `incident` record's `statuscode` field has changed from `In Progress` (2) to `Resolved` (5). Your task: determine exactly which automations fire, in what order, with what inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular triggers).

Execute the following phases in strict sequence. Each phase SHALL complete before the next begins. No phase SHALL execute until all prior phases have issued their required outputs.

---

### PROTOCOL PREAMBLE

*This block is the governing contract layer. It SHALL appear before Phase 1 and SHALL contain all three contract declarations: Platform Term Contract, FM Catalog, and Entry Schema Contract.*

#### Platform Term Contract

Approved vocabulary:

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
| FM-03 | Missing input/output specification | Named input payload and output action; no placeholders | `[IO FAIL: trigger-name \| FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three pathology classes addressed | `[PATH MISS: class \| FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name \| FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced until no further triggers fire | `[CASCADE SHALLOW \| FM-06]` | 4 |
| FM-07 | Missing conditional branch | Firing and skipped branch both stated | `[BRANCH MISS: trigger-name \| FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used throughout | `[VOCAB FAIL: "actual" -> correction \| FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with one-line mitigation | `[RISK MISS \| FM-09]` | 5 |
| FM-10 | Missing timing annotation | Sync/async distinguished; latency noted | `[TIMING MISS: trigger-name \| FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct vocabulary pair | `[NEG MISS \| FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence; bare assertions are insufficient | `[INSUFFICIENT: evidence needed \| FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition declared per chain | `[CHAIN OPEN: CH-NN \| FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger constructed | `[GRAPH MISS \| FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before condition filtering | `[DENOM MISS \| FM-15]` | 1 |
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |
| FM-18 | No sync/async structural split | Sync and async triggers in separate enumeration phases | `[SPLIT MISS \| FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied to adjacency structure | `[BACKTRACK MISS \| FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each cascade chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN \| FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every violation marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies firing + non-firing + unresolved = N | `[RECON MISS \| FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing trigger entry | `[SE MISS: trigger-name \| FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade-link columns | `[MAP MISS \| FM-25]` | 6 |

*FM-21 is the self-referential entry: any violation marker appearing without an FM code is itself an FM-21 violation.*

---

**--- PHASE-BOUNDARY DEFECT CLASSES ---**

*Structural independence note: FM-16 (Entry Condition Absent) and FM-17 (Gate Register Drift) are structurally non-overlapping failure modes requiring separate FM IDs. The independence covers all three intersection cases in the defect space:*

*FM-16 alone: A phase has no entry condition at all. The defect is presence, not quality. Register evaluation is not applicable because no condition text exists -- there is nothing to evaluate for register quality. Inline tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. FM-17 does NOT apply.*

*FM-17 alone: A phase has an entry condition, but stated descriptively rather than with formal obligation language. Presence is satisfied; only register quality fails. Inline tag: `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. FM-16 does NOT apply.*

*Both simultaneously: A phase has no entry condition AND the document's register pattern throughout indicates that a condition, if present, would also be stated descriptively rather than with formal obligation language. Both defects co-occur and are independently taggable with both tags: `[ENTRY CONDITION ABSENT: Phase N | FM-16]` AND `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. A single FM ID would conflate all three cases -- a reviewer scanning a single inline tag cannot determine the defect class without inspecting the phase body and surrounding context. Separate IDs make each tag independently informative: the tag alone conveys the complete structural fact for that defect class without further inspection required.*

| FM Code | Defect | Description | Tag | Scope |
|---------|--------|-------------|-----|-------|
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |

---

#### Entry Schema Contract

All trigger entries SHALL conform to one of the following schemas. A slot left blank is a schema violation.

**FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:          [automated cloud flow | instant cloud flow | Dataverse plug-in | ...]
Execution Tier:     [sync | async | scheduled]
Trigger Event:
Input Fields:       [specific named fields -- no generic placeholders]
Output Action:      [specific action -- no generic placeholders]
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
Condition (Taken):  [what would cause this trigger to fire -- not met in this scenario]
Condition (Skipped):[what IS true in this scenario that blocks this trigger]
```

---

### STRUCTURAL INVARIANT LAYER

*This section is distinct from the PROTOCOL PREAMBLE. The PREAMBLE declares vocabulary, FM catalog, and schema contracts. This INVARIANT LAYER declares cross-phase structural obligations that hold simultaneously across all phases and all gate-language artifact surfaces. Each invariant cites the FM catalog ID whose inline tag signals a violation -- making violation tagging self-evident from the invariant text without requiring FM catalog lookup.*

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control artifacts: entry condition, job description, and exit condition. A phase body missing any of the three artifacts is a structural defect. **Violation taggable as: missing entry condition -> `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements (entry conditions and exit conditions) in phase bodies throughout this protocol SHALL use formal obligation language (SHALL/MUST) in the obligation position. A gate statement using descriptive state language is a register drift defect. **Violation taggable as: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- The LIFECYCLE OVERVIEW table gate-cell register:** The LIFECYCLE OVERVIEW table entry-condition and exit-condition cells are governed by this INVARIANT LAYER and SHALL satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). A summary-function rationale does NOT establish a register exemption for any artifact surface -- a document's organizational structure does not establish register exemptions for its constituent artifacts. A reader verifying Invariant 2 SHALL verify both phase-body gate statements AND The LIFECYCLE OVERVIEW table gate cells; partial compliance (phase bodies formal, overview cells descriptive) fails Invariant 2 even when the phase bodies themselves are conforming. **Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker appearing in the output SHALL include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** The candidate trigger count N declared in Phase 1 SHALL be reconciled after Phase 3 completes: firing + non-firing + unresolved SHALL equal N. **Violation taggable as: `[RECON MISS | FM-22]`.**

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- THE LIFECYCLE OVERVIEW TABLE

Rule 1 (Governing authority): This DECLARATION governs all entry-condition and
exit-condition cells in The LIFECYCLE OVERVIEW table below. The STRUCTURAL
INVARIANT LAYER (Invariant 3) also governs these cells; this DECLARATION and
Invariant 3 are co-authoritative over The LIFECYCLE OVERVIEW table gate cells.
Phase-body gate statements are governed by their respective phase-body
specifications and by Invariant 2.

Rule 2 (Register requirement): All entry-condition and exit-condition cells in
this table SHALL use formal obligation language (SHALL/MUST) in the obligation
position. A cell stating a condition without an obligation verb is non-conforming
under this Rule and under Invariant 3.

Rule 3 (Self-tagging requirement): Any entry-condition or exit-condition cell
using descriptive state language SHALL be tagged [FM-17: Gate Register Drift]
inline within that cell. A non-conforming untagged cell is a double violation:
FM-17 for register drift and FM-21 for the missing FM code.

Rule 4 (Independent row verification): A reader verifying this table SHALL check
each gate cell independently against Rules 2 and 3. Row N conformance does not
imply Row N+1 conformance.
```

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 1 | Pre-scan | Phase 1 SHALL begin when: input record change specification received and PROTOCOL PREAMBLE declared complete | Identify all candidate triggers without filtering; declare denominator N; open all three anomaly question slots OPEN; issue PCC-1 | Phase 1 SHALL be declared complete when: N is declared, all three anomaly slots are explicitly OPEN, and PCC-1 is issued |
| 2 | Sync Trigger Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued | Enumerate all sync-tier candidates using FIRING ENTRY or NON-FIRING ENTRY schema; include negative vocabulary example; order by priority | Phase 2 SHALL be declared complete when: all sync-tier candidates have resolved entries with all schema slots populated |
| 3 | Async Trigger Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate all async-tier candidates using schema; annotate latency tier per entry | Phase 3 SHALL be declared complete when: all async-tier candidates have resolved entries with all schema slots populated |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both trigger tables produced | Trace all cascade chains from side-effect field writes to terminal; assign chain IDs; apply back-edge detection | Phase 4 SHALL be declared complete when: all side-effect writes evaluated, all chains carry Chain-Status, back-edge detection applied |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete and all cascade chains carry Chain-Status | Deliver evidence-anchored verdicts for storm, missing trigger, circular trigger; propose remediation for each confirmed anomaly | Phase 5 SHALL be declared complete when: all three anomaly class verdicts issued with cited evidence and every confirmed anomaly has at least one remediation step |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and all anomaly verdicts issued | Produce trigger map with execution-tier and Spawns columns; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map covers all triggers with required columns and denominator closure is stated with CLOSED or GAP DETECTED |

---

### Phase 1 -- Pre-scan

**Entry condition:** Phase 1 SHALL begin when the input record change specification has been received and the PROTOCOL PREAMBLE has been declared complete.

**Job:** Phase 1 SHALL perform three operations before any trigger enumeration begins: (1) identify all candidate triggers without condition filtering and declare denominator N; (2) open all three anomaly question slots with explicit OPEN status; (3) scan this protocol for phrasing register violations and issue Phrasing Clearance PCC-1 if zero violations found.

**Anomaly Questions -- Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does the statuscode change from In Progress to Resolved cause more triggers to fire than the environment's operational capacity can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for this status transition that does not appear in the trigger surface? | OPEN |
| Circular Trigger | Does any trigger's output create a field write that re-activates the same or an upstream trigger? | OPEN |

**Denominator Pre-Scan:**

| Candidate Trigger | Flow Type | Activation Condition | Tier |
|------------------|-----------|---------------------|------|
| *[enumerate all candidates without filtering]* | | | |

Total candidate count N = *[integer -- declare before Phase 2 begins]*

**Exit condition:** Phase 1 SHALL be declared complete when: N is declared, all three anomaly question slots are explicitly marked OPEN, and PCC-1 is issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when: Phase 1 is complete, N is declared, and PCC-1 is issued. If PCC-1 is absent, Phase 2 SHALL NOT execute `[ENTRY CONDITION ABSENT: Phase 2 | FM-16]`.

**Job:** Phase 2 SHALL enumerate all synchronous triggers. Every sync-tier candidate from Phase 1 SHALL resolve to a FIRING ENTRY or NON-FIRING ENTRY. No candidate SHALL be omitted without a NON-FIRING ENTRY. At least one negative vocabulary example SHALL be included. [FM-11] Order by execution priority, highest first. [FM-02]

Sync trigger: executes within the same transaction (Dataverse sync plug-in step pre/post-operation; synchronous automated cloud flow on Dataverse change event).

**Negative vocabulary example (required):** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be declared complete when every sync-tier candidate has a resolved entry with all schema slots populated and no blank slots remain.

---

### Phase 3 -- Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when: Phase 2 is complete and the Sync Trigger Table is produced.

**Job:** Phase 3 SHALL enumerate all asynchronous triggers. Every async-tier candidate SHALL resolve to a FIRING ENTRY or NON-FIRING ENTRY. Order by connector tier, then by priority. [FM-02] Annotate latency tier (near-real-time / standard / batch) per entry. [FM-10]

Async trigger: executes outside the originating transaction (Dataverse async plug-in step; automated cloud flow with async trigger mode; Power Automate connector on Dataverse change events).

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be declared complete when every async-tier candidate has a resolved entry with all schema slots populated.

---

### Phase 4 -- Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when: Phase 2 and Phase 3 are complete and both trigger tables are produced.

**Job:** Phase 4 SHALL trace every cascade chain originating from side-effect field writes to its terminal. Each chain SHALL receive a Chain ID. The final row of each chain SHALL be marked [TERMINAL]. [FM-20] Back-edge detection SHALL be applied to the adjacency structure to identify any cycles. [FM-19]

**Cascade Chain Table:**

| Chain ID | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|------|--------------------|--------------------|---------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be declared complete when: all side-effect writes are evaluated, all chains carry Chain-Status, and back-edge detection has been applied.

---

### Phase 5 -- Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when: Phase 4 is complete and all cascade chains carry Chain-Status.

**Job:** Phase 5 SHALL deliver evidence-anchored verdicts for all three anomaly classes. Each verdict SHALL cite evidence from prior phases. Bare assertions SHALL be marked `[INSUFFICIENT: state evidence needed | FM-12]`. Every confirmed anomaly SHALL receive at least one remediation step. [FM-09]

**Trigger Storm:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Missing Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Circular Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Exit condition:** Phase 5 SHALL be declared complete when: all three verdicts are issued with cited evidence and every confirmed anomaly has at least one remediation step.

---

### Phase 6 -- Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when: Phase 5 is complete and all anomaly verdicts are issued.

**Job:** Phase 6 SHALL produce a trigger map with execution-tier and Spawns columns covering all triggers. Denominator closure SHALL be performed: firing + non-firing + unresolved = N.

**Trigger Map:**

| # | Trigger Name | Execution Tier | Anomaly Flag | Spawns |
|---|-------------|---------------|-------------|--------|

**Denominator Closure:** firing + non-firing + unresolved = N -> CLOSED / GAP DETECTED `[RECON MISS | FM-22]`

**Exit condition:** Phase 6 SHALL be declared complete when: trigger map covers all triggers with all required columns and denominator closure is stated with CLOSED or GAP DETECTED.

---

## V-02

**Variation axis:** Output format -- em-dash restatement uses correct "summary or overview nature" phrase but names wrong obligation target (platform-vocabulary instead of formal-register)
**Hypothesis:** Invariant 3 has artifact-agnostic scope so C-42 passes. The em-dash restatement correctly names "summary or overview nature" -- the nature-based rationale -- but the obligation it denies is "the platform-vocabulary obligation" rather than "the formal-register obligation." A reader invoking the summary-function rationale against the FORMAL-REGISTER obligation can still argue that the clause only blocks summary-or-overview exemptions from the platform-vocabulary obligation; the formal-register obligation is a separate, unaddressed obligation. C-46 fails because the operational restatement names the wrong obligation: the blocked rationale is named correctly but the obligation being protected is wrong, so the clause does not seal the formal-register exemption path.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dataverse `incident` record's `statuscode` field has changed from `In Progress` (2) to `Resolved` (5). Your task: determine exactly which automations fire, in what order, with what inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular triggers).

Execute the following phases in strict sequence. Each phase SHALL complete before the next begins. No phase SHALL execute until all prior phases have issued their required outputs.

---

### PROTOCOL PREAMBLE

*This block is the governing contract layer. It SHALL appear before Phase 1 and SHALL contain all three contract declarations: Platform Term Contract, FM Catalog, and Entry Schema Contract.*

#### Platform Term Contract

Approved vocabulary:

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
| FM-03 | Missing input/output specification | Named input payload and output action; no placeholders | `[IO FAIL: trigger-name \| FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three pathology classes addressed | `[PATH MISS: class \| FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name \| FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced until no further triggers fire | `[CASCADE SHALLOW \| FM-06]` | 4 |
| FM-07 | Missing conditional branch | Firing and skipped branch both stated | `[BRANCH MISS: trigger-name \| FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used throughout | `[VOCAB FAIL: "actual" -> correction \| FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with one-line mitigation | `[RISK MISS \| FM-09]` | 5 |
| FM-10 | Missing timing annotation | Sync/async distinguished; latency noted | `[TIMING MISS: trigger-name \| FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct vocabulary pair | `[NEG MISS \| FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence; bare assertions are insufficient | `[INSUFFICIENT: evidence needed \| FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition declared per chain | `[CHAIN OPEN: CH-NN \| FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger constructed | `[GRAPH MISS \| FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before condition filtering | `[DENOM MISS \| FM-15]` | 1 |
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |
| FM-18 | No sync/async structural split | Sync and async triggers in separate enumeration phases | `[SPLIT MISS \| FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied to adjacency structure | `[BACKTRACK MISS \| FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each cascade chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN \| FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every violation marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies firing + non-firing + unresolved = N | `[RECON MISS \| FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing trigger entry | `[SE MISS: trigger-name \| FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade-link columns | `[MAP MISS \| FM-25]` | 6 |

*FM-21 is the self-referential entry: any violation marker appearing without an FM code is itself an FM-21 violation.*

---

**--- PHASE-BOUNDARY DEFECT CLASSES ---**

*Structural independence note: FM-16 (Entry Condition Absent) and FM-17 (Gate Register Drift) are structurally non-overlapping failure modes requiring separate FM IDs. The independence covers all three intersection cases in the defect space:*

*FM-16 alone: A phase has no entry condition at all. The defect is presence, not quality. Register evaluation is not applicable because no condition text exists -- there is nothing to evaluate for register quality. Inline tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. FM-17 does NOT apply.*

*FM-17 alone: A phase has an entry condition, but stated descriptively rather than with formal obligation language. Presence is satisfied; only register quality fails. Inline tag: `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. FM-16 does NOT apply.*

*Both simultaneously: A phase has no entry condition AND the document's register pattern throughout indicates that a condition, if present, would also be stated descriptively rather than with formal obligation language. Both defects co-occur and are independently taggable with both tags: `[ENTRY CONDITION ABSENT: Phase N | FM-16]` AND `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. A single FM ID would conflate all three cases -- a reviewer scanning a single inline tag cannot determine the defect class without inspecting the phase body and surrounding context. Separate IDs make each tag independently informative: the tag alone conveys the complete structural fact for that defect class without further inspection required.*

| FM Code | Defect | Description | Tag | Scope |
|---------|--------|-------------|-----|-------|
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |

---

#### Entry Schema Contract

All trigger entries SHALL conform to one of the following schemas. A slot left blank is a schema violation.

**FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:          [automated cloud flow | instant cloud flow | Dataverse plug-in | ...]
Execution Tier:     [sync | async | scheduled]
Trigger Event:
Input Fields:       [specific named fields -- no generic placeholders]
Output Action:      [specific action -- no generic placeholders]
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
Condition (Taken):  [what would cause this trigger to fire -- not met in this scenario]
Condition (Skipped):[what IS true in this scenario that blocks this trigger]
```

---

### STRUCTURAL INVARIANT LAYER

*This section is distinct from the PROTOCOL PREAMBLE. The PREAMBLE declares vocabulary, FM catalog, and schema contracts. This INVARIANT LAYER declares cross-phase structural obligations that hold simultaneously across all phases and all gate-language artifact surfaces. Each invariant cites the FM catalog ID whose inline tag signals a violation -- making violation tagging self-evident from the invariant text without requiring FM catalog lookup.*

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control artifacts: entry condition, job description, and exit condition. A phase body missing any of the three artifacts is a structural defect. **Violation taggable as: missing entry condition -> `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements (entry conditions and exit conditions) in phase bodies throughout this protocol SHALL use formal obligation language (SHALL/MUST) in the obligation position. A gate statement using descriptive state language is a register drift defect. **Violation taggable as: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- The LIFECYCLE OVERVIEW table gate-cell register:** The LIFECYCLE OVERVIEW table entry-condition and exit-condition cells are governed by this INVARIANT LAYER and SHALL satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). A summary-function rationale does NOT establish a register exemption for any artifact surface -- the summary or overview nature of an artifact does not confer exemption from the platform-vocabulary obligation. A reader verifying Invariant 2 SHALL verify both phase-body gate statements AND The LIFECYCLE OVERVIEW table gate cells; partial compliance (phase bodies formal, overview cells descriptive) fails Invariant 2 even when the phase bodies themselves are conforming. **Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker appearing in the output SHALL include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** The candidate trigger count N declared in Phase 1 SHALL be reconciled after Phase 3 completes: firing + non-firing + unresolved SHALL equal N. **Violation taggable as: `[RECON MISS | FM-22]`.**

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- THE LIFECYCLE OVERVIEW TABLE

Rule 1 (Governing authority): This DECLARATION governs all entry-condition and
exit-condition cells in The LIFECYCLE OVERVIEW table below. The STRUCTURAL
INVARIANT LAYER (Invariant 3) also governs these cells; this DECLARATION and
Invariant 3 are co-authoritative over The LIFECYCLE OVERVIEW table gate cells.
Phase-body gate statements are governed by their respective phase-body
specifications and by Invariant 2.

Rule 2 (Register requirement): All entry-condition and exit-condition cells in
this table SHALL use formal obligation language (SHALL/MUST) in the obligation
position. A cell stating a condition without an obligation verb is non-conforming
under this Rule and under Invariant 3.

Rule 3 (Self-tagging requirement): Any entry-condition or exit-condition cell
using descriptive state language SHALL be tagged [FM-17: Gate Register Drift]
inline within that cell. A non-conforming untagged cell is a double violation:
FM-17 for register drift and FM-21 for the missing FM code.

Rule 4 (Independent row verification): A reader verifying this table SHALL check
each gate cell independently against Rules 2 and 3. Row N conformance does not
imply Row N+1 conformance.
```

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 1 | Pre-scan | Phase 1 SHALL begin when: input record change specification received and PROTOCOL PREAMBLE declared complete | Identify all candidate triggers without filtering; declare denominator N; open all three anomaly question slots OPEN; issue PCC-1 | Phase 1 SHALL be declared complete when: N is declared, all three anomaly slots are explicitly OPEN, and PCC-1 is issued |
| 2 | Sync Trigger Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued | Enumerate all sync-tier candidates using FIRING ENTRY or NON-FIRING ENTRY schema; include negative vocabulary example; order by priority | Phase 2 SHALL be declared complete when: all sync-tier candidates have resolved entries with all schema slots populated |
| 3 | Async Trigger Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate all async-tier candidates using schema; annotate latency tier per entry | Phase 3 SHALL be declared complete when: all async-tier candidates have resolved entries with all schema slots populated |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both trigger tables produced | Trace all cascade chains from side-effect field writes to terminal; assign chain IDs; apply back-edge detection | Phase 4 SHALL be declared complete when: all side-effect writes evaluated, all chains carry Chain-Status, back-edge detection applied |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete and all cascade chains carry Chain-Status | Deliver evidence-anchored verdicts for storm, missing trigger, circular trigger; propose remediation for each confirmed anomaly | Phase 5 SHALL be declared complete when: all three anomaly class verdicts issued with cited evidence and every confirmed anomaly has at least one remediation step |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and all anomaly verdicts issued | Produce trigger map with execution-tier and Spawns columns; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map covers all triggers with required columns and denominator closure is stated with CLOSED or GAP DETECTED |

---

### Phase 1 -- Pre-scan

**Entry condition:** Phase 1 SHALL begin when the input record change specification has been received and the PROTOCOL PREAMBLE has been declared complete.

**Job:** Phase 1 SHALL perform three operations before any trigger enumeration begins: (1) identify all candidate triggers without condition filtering and declare denominator N; (2) open all three anomaly question slots with explicit OPEN status; (3) scan this protocol for phrasing register violations and issue Phrasing Clearance PCC-1 if zero violations found.

**Anomaly Questions -- Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does the statuscode change from In Progress to Resolved cause more triggers to fire than the environment's operational capacity can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for this status transition that does not appear in the trigger surface? | OPEN |
| Circular Trigger | Does any trigger's output create a field write that re-activates the same or an upstream trigger? | OPEN |

**Denominator Pre-Scan:**

| Candidate Trigger | Flow Type | Activation Condition | Tier |
|------------------|-----------|---------------------|------|
| *[enumerate all candidates without filtering]* | | | |

Total candidate count N = *[integer -- declare before Phase 2 begins]*

**Exit condition:** Phase 1 SHALL be declared complete when: N is declared, all three anomaly question slots are explicitly marked OPEN, and PCC-1 is issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when: Phase 1 is complete, N is declared, and PCC-1 is issued. If PCC-1 is absent, Phase 2 SHALL NOT execute `[ENTRY CONDITION ABSENT: Phase 2 | FM-16]`.

**Job:** Phase 2 SHALL enumerate all synchronous triggers. Every sync-tier candidate from Phase 1 SHALL resolve to a FIRING ENTRY or NON-FIRING ENTRY. No candidate SHALL be omitted without a NON-FIRING ENTRY. At least one negative vocabulary example SHALL be included. [FM-11] Order by execution priority, highest first. [FM-02]

Sync trigger: executes within the same transaction (Dataverse sync plug-in step pre/post-operation; synchronous automated cloud flow on Dataverse change event).

**Negative vocabulary example (required):** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be declared complete when every sync-tier candidate has a resolved entry with all schema slots populated and no blank slots remain.

---

### Phase 3 -- Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when: Phase 2 is complete and the Sync Trigger Table is produced.

**Job:** Phase 3 SHALL enumerate all asynchronous triggers. Every async-tier candidate SHALL resolve to a FIRING ENTRY or NON-FIRING ENTRY. Order by connector tier, then by priority. [FM-02] Annotate latency tier (near-real-time / standard / batch) per entry. [FM-10]

Async trigger: executes outside the originating transaction (Dataverse async plug-in step; automated cloud flow with async trigger mode; Power Automate connector on Dataverse change events).

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be declared complete when every async-tier candidate has a resolved entry with all schema slots populated.

---

### Phase 4 -- Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when: Phase 2 and Phase 3 are complete and both trigger tables are produced.

**Job:** Phase 4 SHALL trace every cascade chain originating from side-effect field writes to its terminal. Each chain SHALL receive a Chain ID. The final row of each chain SHALL be marked [TERMINAL]. [FM-20] Back-edge detection SHALL be applied to the adjacency structure to identify any cycles. [FM-19]

**Cascade Chain Table:**

| Chain ID | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|------|--------------------|--------------------|---------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be declared complete when: all side-effect writes are evaluated, all chains carry Chain-Status, and back-edge detection has been applied.

---

### Phase 5 -- Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when: Phase 4 is complete and all cascade chains carry Chain-Status.

**Job:** Phase 5 SHALL deliver evidence-anchored verdicts for all three anomaly classes. Each verdict SHALL cite evidence from prior phases. Bare assertions SHALL be marked `[INSUFFICIENT: state evidence needed | FM-12]`. Every confirmed anomaly SHALL receive at least one remediation step. [FM-09]

**Trigger Storm:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Missing Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Circular Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Exit condition:** Phase 5 SHALL be declared complete when: all three verdicts are issued with cited evidence and every confirmed anomaly has at least one remediation step.

---

### Phase 6 -- Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when: Phase 5 is complete and all anomaly verdicts are issued.

**Job:** Phase 6 SHALL produce a trigger map with execution-tier and Spawns columns covering all triggers. Denominator closure SHALL be performed: firing + non-firing + unresolved = N.

**Trigger Map:**

| # | Trigger Name | Execution Tier | Anomaly Flag | Spawns |
|---|-------------|---------------|-------------|--------|

**Denominator Closure:** firing + non-firing + unresolved = N -> CLOSED / GAP DETECTED `[RECON MISS | FM-22]`

**Exit condition:** Phase 6 SHALL be declared complete when: trigger map covers all triggers with all required columns and denominator closure is stated with CLOSED or GAP DETECTED.

---

## V-03

**Variation axis:** Lifecycle emphasis -- correct C-46 language present but non-exemption clause structurally displaced as a parenthetical after the verifier instruction
**Hypothesis:** Invariant 3 contains the C-46-correct language ("the summary or overview nature of an artifact does not confer exemption from the formal-register obligation") but it appears as a parenthetical note placed AFTER the verifier instruction rather than immediately following the scope assertion with an em-dash. The em-dash form and the "immediately following" co-location are both required by C-46: the restatement must directly follow the scope assertion without intervening text. When verifier-instruction text appears between the scope assertion and the restatement, the operational definition is no longer immediate -- a reader can treat the parenthetical as a supplementary note rather than as an integral part of the non-exemption clause. C-42 passes. C-46 fails because the structural placement breaks the "immediate" requirement.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dataverse `incident` record's `statuscode` field has changed from `In Progress` (2) to `Resolved` (5). Your task: determine exactly which automations fire, in what order, with what inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular triggers).

Execute the following phases in strict sequence. Each phase SHALL complete before the next begins. No phase SHALL execute until all prior phases have issued their required outputs.

---

### PROTOCOL PREAMBLE

*This block is the governing contract layer. It SHALL appear before Phase 1 and SHALL contain all three contract declarations: Platform Term Contract, FM Catalog, and Entry Schema Contract.*

#### Platform Term Contract

Approved vocabulary:

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
| FM-03 | Missing input/output specification | Named input payload and output action; no placeholders | `[IO FAIL: trigger-name \| FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three pathology classes addressed | `[PATH MISS: class \| FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name \| FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced until no further triggers fire | `[CASCADE SHALLOW \| FM-06]` | 4 |
| FM-07 | Missing conditional branch | Firing and skipped branch both stated | `[BRANCH MISS: trigger-name \| FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used throughout | `[VOCAB FAIL: "actual" -> correction \| FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with one-line mitigation | `[RISK MISS \| FM-09]` | 5 |
| FM-10 | Missing timing annotation | Sync/async distinguished; latency noted | `[TIMING MISS: trigger-name \| FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct vocabulary pair | `[NEG MISS \| FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence; bare assertions are insufficient | `[INSUFFICIENT: evidence needed \| FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition declared per chain | `[CHAIN OPEN: CH-NN \| FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger constructed | `[GRAPH MISS \| FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before condition filtering | `[DENOM MISS \| FM-15]` | 1 |
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |
| FM-18 | No sync/async structural split | Sync and async triggers in separate enumeration phases | `[SPLIT MISS \| FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied to adjacency structure | `[BACKTRACK MISS \| FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each cascade chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN \| FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every violation marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies firing + non-firing + unresolved = N | `[RECON MISS \| FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing trigger entry | `[SE MISS: trigger-name \| FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade-link columns | `[MAP MISS \| FM-25]` | 6 |

*FM-21 is the self-referential entry: any violation marker appearing without an FM code is itself an FM-21 violation.*

---

**--- PHASE-BOUNDARY DEFECT CLASSES ---**

*Structural independence note: FM-16 (Entry Condition Absent) and FM-17 (Gate Register Drift) are structurally non-overlapping failure modes requiring separate FM IDs. The independence covers all three intersection cases in the defect space:*

*FM-16 alone: A phase has no entry condition at all. The defect is presence, not quality. Register evaluation is not applicable because no condition text exists -- there is nothing to evaluate for register quality. Inline tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. FM-17 does NOT apply.*

*FM-17 alone: A phase has an entry condition, but stated descriptively rather than with formal obligation language. Presence is satisfied; only register quality fails. Inline tag: `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. FM-16 does NOT apply.*

*Both simultaneously: A phase has no entry condition AND the document's register pattern throughout indicates that a condition, if present, would also be stated descriptively rather than with formal obligation language. Both defects co-occur and are independently taggable with both tags: `[ENTRY CONDITION ABSENT: Phase N | FM-16]` AND `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. A single FM ID would conflate all three cases -- a reviewer scanning a single inline tag cannot determine the defect class without inspecting the phase body and surrounding context. Separate IDs make each tag independently informative: the tag alone conveys the complete structural fact for that defect class without further inspection required.*

| FM Code | Defect | Description | Tag | Scope |
|---------|--------|-------------|-----|-------|
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |

---

#### Entry Schema Contract

All trigger entries SHALL conform to one of the following schemas. A slot left blank is a schema violation.

**FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:          [automated cloud flow | instant cloud flow | Dataverse plug-in | ...]
Execution Tier:     [sync | async | scheduled]
Trigger Event:
Input Fields:       [specific named fields -- no generic placeholders]
Output Action:      [specific action -- no generic placeholders]
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
Condition (Taken):  [what would cause this trigger to fire -- not met in this scenario]
Condition (Skipped):[what IS true in this scenario that blocks this trigger]
```

---

### STRUCTURAL INVARIANT LAYER

*This section is distinct from the PROTOCOL PREAMBLE. The PREAMBLE declares vocabulary, FM catalog, and schema contracts. This INVARIANT LAYER declares cross-phase structural obligations that hold simultaneously across all phases and all gate-language artifact surfaces. Each invariant cites the FM catalog ID whose inline tag signals a violation -- making violation tagging self-evident from the invariant text without requiring FM catalog lookup.*

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control artifacts: entry condition, job description, and exit condition. A phase body missing any of the three artifacts is a structural defect. **Violation taggable as: missing entry condition -> `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements (entry conditions and exit conditions) in phase bodies throughout this protocol SHALL use formal obligation language (SHALL/MUST) in the obligation position. A gate statement using descriptive state language is a register drift defect. **Violation taggable as: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- The LIFECYCLE OVERVIEW table gate-cell register:** The LIFECYCLE OVERVIEW table entry-condition and exit-condition cells are governed by this INVARIANT LAYER and SHALL satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). A summary-function rationale does NOT establish a register exemption for any artifact surface. A reader verifying Invariant 2 SHALL verify both phase-body gate statements AND The LIFECYCLE OVERVIEW table gate cells; partial compliance (phase bodies formal, overview cells descriptive) fails Invariant 2 even when the phase bodies themselves are conforming. (Note: the summary or overview nature of an artifact does not confer exemption from the formal-register obligation.) **Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker appearing in the output SHALL include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** The candidate trigger count N declared in Phase 1 SHALL be reconciled after Phase 3 completes: firing + non-firing + unresolved SHALL equal N. **Violation taggable as: `[RECON MISS | FM-22]`.**

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- THE LIFECYCLE OVERVIEW TABLE

Rule 1 (Governing authority): This DECLARATION governs all entry-condition and
exit-condition cells in The LIFECYCLE OVERVIEW table below. The STRUCTURAL
INVARIANT LAYER (Invariant 3) also governs these cells; this DECLARATION and
Invariant 3 are co-authoritative over The LIFECYCLE OVERVIEW table gate cells.
Phase-body gate statements are governed by their respective phase-body
specifications and by Invariant 2.

Rule 2 (Register requirement): All entry-condition and exit-condition cells in
this table SHALL use formal obligation language (SHALL/MUST) in the obligation
position. A cell stating a condition without an obligation verb is non-conforming
under this Rule and under Invariant 3.

Rule 3 (Self-tagging requirement): Any entry-condition or exit-condition cell
using descriptive state language SHALL be tagged [FM-17: Gate Register Drift]
inline within that cell. A non-conforming untagged cell is a double violation:
FM-17 for register drift and FM-21 for the missing FM code.

Rule 4 (Independent row verification): A reader verifying this table SHALL check
each gate cell independently against Rules 2 and 3. Row N conformance does not
imply Row N+1 conformance.
```

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 1 | Pre-scan | Phase 1 SHALL begin when: input record change specification received and PROTOCOL PREAMBLE declared complete | Identify all candidate triggers without filtering; declare denominator N; open all three anomaly question slots OPEN; issue PCC-1 | Phase 1 SHALL be declared complete when: N is declared, all three anomaly slots are explicitly OPEN, and PCC-1 is issued |
| 2 | Sync Trigger Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued | Enumerate all sync-tier candidates using FIRING ENTRY or NON-FIRING ENTRY schema; include negative vocabulary example; order by priority | Phase 2 SHALL be declared complete when: all sync-tier candidates have resolved entries with all schema slots populated |
| 3 | Async Trigger Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate all async-tier candidates using schema; annotate latency tier per entry | Phase 3 SHALL be declared complete when: all async-tier candidates have resolved entries with all schema slots populated |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both trigger tables produced | Trace all cascade chains from side-effect field writes to terminal; assign chain IDs; apply back-edge detection | Phase 4 SHALL be declared complete when: all side-effect writes evaluated, all chains carry Chain-Status, back-edge detection applied |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete and all cascade chains carry Chain-Status | Deliver evidence-anchored verdicts for storm, missing trigger, circular trigger; propose remediation for each confirmed anomaly | Phase 5 SHALL be declared complete when: all three anomaly class verdicts issued with cited evidence and every confirmed anomaly has at least one remediation step |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and all anomaly verdicts issued | Produce trigger map with execution-tier and Spawns columns; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map covers all triggers with required columns and denominator closure is stated with CLOSED or GAP DETECTED |

---

### Phase 1 -- Pre-scan

**Entry condition:** Phase 1 SHALL begin when the input record change specification has been received and the PROTOCOL PREAMBLE has been declared complete.

**Job:** Phase 1 SHALL perform three operations before any trigger enumeration begins: (1) identify all candidate triggers without condition filtering and declare denominator N; (2) open all three anomaly question slots with explicit OPEN status; (3) scan this protocol for phrasing register violations and issue Phrasing Clearance PCC-1 if zero violations found.

**Anomaly Questions -- Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does the statuscode change from In Progress to Resolved cause more triggers to fire than the environment's operational capacity can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for this status transition that does not appear in the trigger surface? | OPEN |
| Circular Trigger | Does any trigger's output create a field write that re-activates the same or an upstream trigger? | OPEN |

**Denominator Pre-Scan:**

| Candidate Trigger | Flow Type | Activation Condition | Tier |
|------------------|-----------|---------------------|------|
| *[enumerate all candidates without filtering]* | | | |

Total candidate count N = *[integer -- declare before Phase 2 begins]*

**Exit condition:** Phase 1 SHALL be declared complete when: N is declared, all three anomaly question slots are explicitly marked OPEN, and PCC-1 is issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when: Phase 1 is complete, N is declared, and PCC-1 is issued. If PCC-1 is absent, Phase 2 SHALL NOT execute `[ENTRY CONDITION ABSENT: Phase 2 | FM-16]`.

**Job:** Phase 2 SHALL enumerate all synchronous triggers. Every sync-tier candidate from Phase 1 SHALL resolve to a FIRING ENTRY or NON-FIRING ENTRY. No candidate SHALL be omitted without a NON-FIRING ENTRY. At least one negative vocabulary example SHALL be included. [FM-11] Order by execution priority, highest first. [FM-02]

Sync trigger: executes within the same transaction (Dataverse sync plug-in step pre/post-operation; synchronous automated cloud flow on Dataverse change event).

**Negative vocabulary example (required):** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be declared complete when every sync-tier candidate has a resolved entry with all schema slots populated and no blank slots remain.

---

### Phase 3 -- Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when: Phase 2 is complete and the Sync Trigger Table is produced.

**Job:** Phase 3 SHALL enumerate all asynchronous triggers. Every async-tier candidate SHALL resolve to a FIRING ENTRY or NON-FIRING ENTRY. Order by connector tier, then by priority. [FM-02] Annotate latency tier (near-real-time / standard / batch) per entry. [FM-10]

Async trigger: executes outside the originating transaction (Dataverse async plug-in step; automated cloud flow with async trigger mode; Power Automate connector on Dataverse change events).

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be declared complete when every async-tier candidate has a resolved entry with all schema slots populated.

---

### Phase 4 -- Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when: Phase 2 and Phase 3 are complete and both trigger tables are produced.

**Job:** Phase 4 SHALL trace every cascade chain originating from side-effect field writes to its terminal. Each chain SHALL receive a Chain ID. The final row of each chain SHALL be marked [TERMINAL]. [FM-20] Back-edge detection SHALL be applied to the adjacency structure to identify any cycles. [FM-19]

**Cascade Chain Table:**

| Chain ID | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|------|--------------------|--------------------|---------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be declared complete when: all side-effect writes are evaluated, all chains carry Chain-Status, and back-edge detection has been applied.

---

### Phase 5 -- Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when: Phase 4 is complete and all cascade chains carry Chain-Status.

**Job:** Phase 5 SHALL deliver evidence-anchored verdicts for all three anomaly classes. Each verdict SHALL cite evidence from prior phases. Bare assertions SHALL be marked `[INSUFFICIENT: state evidence needed | FM-12]`. Every confirmed anomaly SHALL receive at least one remediation step. [FM-09]

**Trigger Storm:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Missing Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Circular Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Exit condition:** Phase 5 SHALL be declared complete when: all three verdicts are issued with cited evidence and every confirmed anomaly has at least one remediation step.

---

### Phase 6 -- Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when: Phase 5 is complete and all anomaly verdicts are issued.

**Job:** Phase 6 SHALL produce a trigger map with execution-tier and Spawns columns covering all triggers. Denominator closure SHALL be performed: firing + non-firing + unresolved = N.

**Trigger Map:**

| # | Trigger Name | Execution Tier | Anomaly Flag | Spawns |
|---|-------------|---------------|-------------|--------|

**Denominator Closure:** firing + non-firing + unresolved = N -> CLOSED / GAP DETECTED `[RECON MISS | FM-22]`

**Exit condition:** Phase 6 SHALL be declared complete when: trigger map covers all triggers with all required columns and denominator closure is stated with CLOSED or GAP DETECTED.

---

## V-04

**Variation axis:** Phrasing register + output format combination -- em-dash + "summary or overview nature" present but obligation target omitted from restatement
**Hypothesis:** Invariant 3 has em-dash + "summary or overview nature" + artifact-agnostic scope -- C-42 passes. The restatement is: "the summary or overview nature of an artifact does not confer register-exemption status." This uses passive voice without naming the obligation: "register-exemption status" is a state, not an obligation being protected. The phrase "from the formal-register obligation" is absent. C-46 fails because the operational restatement must name the obligation being denied -- a reader who wants to claim exemption from the formal-register obligation can argue that "register-exemption status" refers to some other register or to platform-vocabulary exemption status, not the formal-register obligation specifically. The blocked rationale is named ("summary or overview nature") but the obligation being protected is left unspecified, leaving the interpretive path open.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dataverse `incident` record's `statuscode` field has changed from `In Progress` (2) to `Resolved` (5). Your task: determine exactly which automations fire, in what order, with what inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular triggers).

Execute the following phases in strict sequence. Each phase SHALL complete before the next begins. No phase SHALL execute until all prior phases have issued their required outputs.

---

### PROTOCOL PREAMBLE

*This block is the governing contract layer. It SHALL appear before Phase 1 and SHALL contain all three contract declarations: Platform Term Contract, FM Catalog, and Entry Schema Contract.*

#### Platform Term Contract

Approved vocabulary:

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
| FM-03 | Missing input/output specification | Named input payload and output action; no placeholders | `[IO FAIL: trigger-name \| FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three pathology classes addressed | `[PATH MISS: class \| FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name \| FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced until no further triggers fire | `[CASCADE SHALLOW \| FM-06]` | 4 |
| FM-07 | Missing conditional branch | Firing and skipped branch both stated | `[BRANCH MISS: trigger-name \| FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used throughout | `[VOCAB FAIL: "actual" -> correction \| FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with one-line mitigation | `[RISK MISS \| FM-09]` | 5 |
| FM-10 | Missing timing annotation | Sync/async distinguished; latency noted | `[TIMING MISS: trigger-name \| FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct vocabulary pair | `[NEG MISS \| FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence; bare assertions are insufficient | `[INSUFFICIENT: evidence needed \| FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition declared per chain | `[CHAIN OPEN: CH-NN \| FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger constructed | `[GRAPH MISS \| FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before condition filtering | `[DENOM MISS \| FM-15]` | 1 |
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |
| FM-18 | No sync/async structural split | Sync and async triggers in separate enumeration phases | `[SPLIT MISS \| FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied to adjacency structure | `[BACKTRACK MISS \| FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each cascade chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN \| FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every violation marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies firing + non-firing + unresolved = N | `[RECON MISS \| FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing trigger entry | `[SE MISS: trigger-name \| FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade-link columns | `[MAP MISS \| FM-25]` | 6 |

*FM-21 is the self-referential entry: any violation marker appearing without an FM code is itself an FM-21 violation.*

---

**--- PHASE-BOUNDARY DEFECT CLASSES ---**

*Structural independence note: FM-16 (Entry Condition Absent) and FM-17 (Gate Register Drift) are structurally non-overlapping failure modes requiring separate FM IDs. The independence covers all three intersection cases in the defect space:*

*FM-16 alone: A phase has no entry condition at all. The defect is presence, not quality. Register evaluation is not applicable because no condition text exists -- there is nothing to evaluate for register quality. Inline tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. FM-17 does NOT apply.*

*FM-17 alone: A phase has an entry condition, but stated descriptively rather than with formal obligation language. Presence is satisfied; only register quality fails. Inline tag: `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. FM-16 does NOT apply.*

*Both simultaneously: A phase has no entry condition AND the document's register pattern throughout indicates that a condition, if present, would also be stated descriptively rather than with formal obligation language. Both defects co-occur and are independently taggable with both tags: `[ENTRY CONDITION ABSENT: Phase N | FM-16]` AND `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. A single FM ID would conflate all three cases -- a reviewer scanning a single inline tag cannot determine the defect class without inspecting the phase body and surrounding context. Separate IDs make each tag independently informative: the tag alone conveys the complete structural fact for that defect class without further inspection required.*

| FM Code | Defect | Description | Tag | Scope |
|---------|--------|-------------|-----|-------|
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |

---

#### Entry Schema Contract

All trigger entries SHALL conform to one of the following schemas. A slot left blank is a schema violation.

**FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:          [automated cloud flow | instant cloud flow | Dataverse plug-in | ...]
Execution Tier:     [sync | async | scheduled]
Trigger Event:
Input Fields:       [specific named fields -- no generic placeholders]
Output Action:      [specific action -- no generic placeholders]
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
Condition (Taken):  [what would cause this trigger to fire -- not met in this scenario]
Condition (Skipped):[what IS true in this scenario that blocks this trigger]
```

---

### STRUCTURAL INVARIANT LAYER

*This section is distinct from the PROTOCOL PREAMBLE. The PREAMBLE declares vocabulary, FM catalog, and schema contracts. This INVARIANT LAYER declares cross-phase structural obligations that hold simultaneously across all phases and all gate-language artifact surfaces. Each invariant cites the FM catalog ID whose inline tag signals a violation -- making violation tagging self-evident from the invariant text without requiring FM catalog lookup.*

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control artifacts: entry condition, job description, and exit condition. A phase body missing any of the three artifacts is a structural defect. **Violation taggable as: missing entry condition -> `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements (entry conditions and exit conditions) in phase bodies throughout this protocol SHALL use formal obligation language (SHALL/MUST) in the obligation position. A gate statement using descriptive state language is a register drift defect. **Violation taggable as: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- The LIFECYCLE OVERVIEW table gate-cell register:** The LIFECYCLE OVERVIEW table entry-condition and exit-condition cells are governed by this INVARIANT LAYER and SHALL satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). A summary-function rationale does NOT establish a register exemption for any artifact surface -- the summary or overview nature of an artifact does not confer register-exemption status. A reader verifying Invariant 2 SHALL verify both phase-body gate statements AND The LIFECYCLE OVERVIEW table gate cells; partial compliance (phase bodies formal, overview cells descriptive) fails Invariant 2 even when the phase bodies themselves are conforming. **Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker appearing in the output SHALL include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** The candidate trigger count N declared in Phase 1 SHALL be reconciled after Phase 3 completes: firing + non-firing + unresolved SHALL equal N. **Violation taggable as: `[RECON MISS | FM-22]`.**

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- THE LIFECYCLE OVERVIEW TABLE

Rule 1 (Governing authority): This DECLARATION governs all entry-condition and
exit-condition cells in The LIFECYCLE OVERVIEW table below. The STRUCTURAL
INVARIANT LAYER (Invariant 3) also governs these cells; this DECLARATION and
Invariant 3 are co-authoritative over The LIFECYCLE OVERVIEW table gate cells.
Phase-body gate statements are governed by their respective phase-body
specifications and by Invariant 2.

Rule 2 (Register requirement): All entry-condition and exit-condition cells in
this table SHALL use formal obligation language (SHALL/MUST) in the obligation
position. A cell stating a condition without an obligation verb is non-conforming
under this Rule and under Invariant 3.

Rule 3 (Self-tagging requirement): Any entry-condition or exit-condition cell
using descriptive state language SHALL be tagged [FM-17: Gate Register Drift]
inline within that cell. A non-conforming untagged cell is a double violation:
FM-17 for register drift and FM-21 for the missing FM code.

Rule 4 (Independent row verification): A reader verifying this table SHALL check
each gate cell independently against Rules 2 and 3. Row N conformance does not
imply Row N+1 conformance.
```

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 1 | Pre-scan | Phase 1 SHALL begin when: input record change specification received and PROTOCOL PREAMBLE declared complete | Identify all candidate triggers without filtering; declare denominator N; open all three anomaly question slots OPEN; issue PCC-1 | Phase 1 SHALL be declared complete when: N is declared, all three anomaly slots are explicitly OPEN, and PCC-1 is issued |
| 2 | Sync Trigger Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued | Enumerate all sync-tier candidates using FIRING ENTRY or NON-FIRING ENTRY schema; include negative vocabulary example; order by priority | Phase 2 SHALL be declared complete when: all sync-tier candidates have resolved entries with all schema slots populated |
| 3 | Async Trigger Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate all async-tier candidates using schema; annotate latency tier per entry | Phase 3 SHALL be declared complete when: all async-tier candidates have resolved entries with all schema slots populated |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both trigger tables produced | Trace all cascade chains from side-effect field writes to terminal; assign chain IDs; apply back-edge detection | Phase 4 SHALL be declared complete when: all side-effect writes evaluated, all chains carry Chain-Status, back-edge detection applied |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete and all cascade chains carry Chain-Status | Deliver evidence-anchored verdicts for storm, missing trigger, circular trigger; propose remediation for each confirmed anomaly | Phase 5 SHALL be declared complete when: all three anomaly class verdicts issued with cited evidence and every confirmed anomaly has at least one remediation step |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and all anomaly verdicts issued | Produce trigger map with execution-tier and Spawns columns; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map covers all triggers with required columns and denominator closure is stated with CLOSED or GAP DETECTED |

---

### Phase 1 -- Pre-scan

**Entry condition:** Phase 1 SHALL begin when the input record change specification has been received and the PROTOCOL PREAMBLE has been declared complete.

**Job:** Phase 1 SHALL perform three operations before any trigger enumeration begins: (1) identify all candidate triggers without condition filtering and declare denominator N; (2) open all three anomaly question slots with explicit OPEN status; (3) scan this protocol for phrasing register violations and issue Phrasing Clearance PCC-1 if zero violations found.

**Anomaly Questions -- Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does the statuscode change from In Progress to Resolved cause more triggers to fire than the environment's operational capacity can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for this status transition that does not appear in the trigger surface? | OPEN |
| Circular Trigger | Does any trigger's output create a field write that re-activates the same or an upstream trigger? | OPEN |

**Denominator Pre-Scan:**

| Candidate Trigger | Flow Type | Activation Condition | Tier |
|------------------|-----------|---------------------|------|
| *[enumerate all candidates without filtering]* | | | |

Total candidate count N = *[integer -- declare before Phase 2 begins]*

**Exit condition:** Phase 1 SHALL be declared complete when: N is declared, all three anomaly question slots are explicitly marked OPEN, and PCC-1 is issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when: Phase 1 is complete, N is declared, and PCC-1 is issued. If PCC-1 is absent, Phase 2 SHALL NOT execute `[ENTRY CONDITION ABSENT: Phase 2 | FM-16]`.

**Job:** Phase 2 SHALL enumerate all synchronous triggers. Every sync-tier candidate from Phase 1 SHALL resolve to a FIRING ENTRY or NON-FIRING ENTRY. No candidate SHALL be omitted without a NON-FIRING ENTRY. At least one negative vocabulary example SHALL be included. [FM-11] Order by execution priority, highest first. [FM-02]

Sync trigger: executes within the same transaction (Dataverse sync plug-in step pre/post-operation; synchronous automated cloud flow on Dataverse change event).

**Negative vocabulary example (required):** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be declared complete when every sync-tier candidate has a resolved entry with all schema slots populated and no blank slots remain.

---

### Phase 3 -- Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when: Phase 2 is complete and the Sync Trigger Table is produced.

**Job:** Phase 3 SHALL enumerate all asynchronous triggers. Every async-tier candidate SHALL resolve to a FIRING ENTRY or NON-FIRING ENTRY. Order by connector tier, then by priority. [FM-02] Annotate latency tier (near-real-time / standard / batch) per entry. [FM-10]

Async trigger: executes outside the originating transaction (Dataverse async plug-in step; automated cloud flow with async trigger mode; Power Automate connector on Dataverse change events).

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be declared complete when every async-tier candidate has a resolved entry with all schema slots populated.

---

### Phase 4 -- Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when: Phase 2 and Phase 3 are complete and both trigger tables are produced.

**Job:** Phase 4 SHALL trace every cascade chain originating from side-effect field writes to its terminal. Each chain SHALL receive a Chain ID. The final row of each chain SHALL be marked [TERMINAL]. [FM-20] Back-edge detection SHALL be applied to the adjacency structure to identify any cycles. [FM-19]

**Cascade Chain Table:**

| Chain ID | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|------|--------------------|--------------------|---------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be declared complete when: all side-effect writes are evaluated, all chains carry Chain-Status, and back-edge detection has been applied.

---

### Phase 5 -- Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when: Phase 4 is complete and all cascade chains carry Chain-Status.

**Job:** Phase 5 SHALL deliver evidence-anchored verdicts for all three anomaly classes. Each verdict SHALL cite evidence from prior phases. Bare assertions SHALL be marked `[INSUFFICIENT: state evidence needed | FM-12]`. Every confirmed anomaly SHALL receive at least one remediation step. [FM-09]

**Trigger Storm:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Missing Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Circular Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Exit condition:** Phase 5 SHALL be declared complete when: all three verdicts are issued with cited evidence and every confirmed anomaly has at least one remediation step.

---

### Phase 6 -- Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when: Phase 5 is complete and all anomaly verdicts are issued.

**Job:** Phase 6 SHALL produce a trigger map with execution-tier and Spawns columns covering all triggers. Denominator closure SHALL be performed: firing + non-firing + unresolved = N.

**Trigger Map:**

| # | Trigger Name | Execution Tier | Anomaly Flag | Spawns |
|---|-------------|---------------|-------------|--------|

**Denominator Closure:** firing + non-firing + unresolved = N -> CLOSED / GAP DETECTED `[RECON MISS | FM-22]`

**Exit condition:** Phase 6 SHALL be declared complete when: trigger map covers all triggers with all required columns and denominator closure is stated with CLOSED or GAP DETECTED.

---

## V-05

**Variation axis:** Full combination -- C-46 PASS with BONUS SIGNAL (C-47 candidate): Rule 1 extended with co-authority non-exemption sub-clause making Rule 1 independently self-contained regarding the summary-or-overview prohibition
**Hypothesis:** Invariant 3 carries the full C-46 pass text (artifact-agnostic scope + em-dash + "summary or overview nature" + "formal-register obligation"). Additionally, Rule 1 in the FORMAL-GATE ZONE DECLARATION is extended with an inline non-exemption sub-clause appended to the co-authority declaration: "-- no artifact surface is exempt from this co-authority's formal-register obligation, including any artifact whose nature is summary or overview." This makes Rule 1 independently self-contained: a reader checking only Rule 1 can determine that the co-authority prohibits summary-or-overview exemptions without consulting Invariant 3. The structural feature separating V-05 from V-01 through V-04 is that the exemption prohibition is now declared in two structurally independent locations (Invariant 3 and Rule 1), with Rule 1's declaration being self-contained -- it names both the authority scope and the blocked rationale within a single rule statement. This is the C-47 candidate bonus signal.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dataverse `incident` record's `statuscode` field has changed from `In Progress` (2) to `Resolved` (5). Your task: determine exactly which automations fire, in what order, with what inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular triggers).

Execute the following phases in strict sequence. Each phase SHALL complete before the next begins. No phase SHALL execute until all prior phases have issued their required outputs.

---

### PROTOCOL PREAMBLE

*This block is the governing contract layer. It SHALL appear before Phase 1 and SHALL contain all three contract declarations: Platform Term Contract, FM Catalog, and Entry Schema Contract.*

#### Platform Term Contract

Approved vocabulary:

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
| FM-03 | Missing input/output specification | Named input payload and output action; no placeholders | `[IO FAIL: trigger-name \| FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three pathology classes addressed | `[PATH MISS: class \| FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name \| FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced until no further triggers fire | `[CASCADE SHALLOW \| FM-06]` | 4 |
| FM-07 | Missing conditional branch | Firing and skipped branch both stated | `[BRANCH MISS: trigger-name \| FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used throughout | `[VOCAB FAIL: "actual" -> correction \| FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with one-line mitigation | `[RISK MISS \| FM-09]` | 5 |
| FM-10 | Missing timing annotation | Sync/async distinguished; latency noted | `[TIMING MISS: trigger-name \| FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct vocabulary pair | `[NEG MISS \| FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence; bare assertions are insufficient | `[INSUFFICIENT: evidence needed \| FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition declared per chain | `[CHAIN OPEN: CH-NN \| FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger constructed | `[GRAPH MISS \| FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before condition filtering | `[DENOM MISS \| FM-15]` | 1 |
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |
| FM-18 | No sync/async structural split | Sync and async triggers in separate enumeration phases | `[SPLIT MISS \| FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied to adjacency structure | `[BACKTRACK MISS \| FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each cascade chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN \| FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every violation marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies firing + non-firing + unresolved = N | `[RECON MISS \| FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing trigger entry | `[SE MISS: trigger-name \| FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade-link columns | `[MAP MISS \| FM-25]` | 6 |

*FM-21 is the self-referential entry: any violation marker appearing without an FM code is itself an FM-21 violation.*

---

**--- PHASE-BOUNDARY DEFECT CLASSES ---**

*Structural independence note: FM-16 (Entry Condition Absent) and FM-17 (Gate Register Drift) are structurally non-overlapping failure modes requiring separate FM IDs. The independence covers all three intersection cases in the defect space:*

*FM-16 alone: A phase has no entry condition at all. The defect is presence, not quality. Register evaluation is not applicable because no condition text exists -- there is nothing to evaluate for register quality. Inline tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. FM-17 does NOT apply.*

*FM-17 alone: A phase has an entry condition, but stated descriptively rather than with formal obligation language. Presence is satisfied; only register quality fails. Inline tag: `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. FM-16 does NOT apply.*

*Both simultaneously: A phase has no entry condition AND the document's register pattern throughout indicates that a condition, if present, would also be stated descriptively rather than with formal obligation language. Both defects co-occur and are independently taggable with both tags: `[ENTRY CONDITION ABSENT: Phase N | FM-16]` AND `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. A single FM ID would conflate all three cases -- a reviewer scanning a single inline tag cannot determine the defect class without inspecting the phase body and surrounding context. Separate IDs make each tag independently informative: the tag alone conveys the complete structural fact for that defect class without further inspection required.*

| FM Code | Defect | Description | Tag | Scope |
|---------|--------|-------------|-----|-------|
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |

---

#### Entry Schema Contract

All trigger entries SHALL conform to one of the following schemas. A slot left blank is a schema violation.

**FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:          [automated cloud flow | instant cloud flow | Dataverse plug-in | ...]
Execution Tier:     [sync | async | scheduled]
Trigger Event:
Input Fields:       [specific named fields -- no generic placeholders]
Output Action:      [specific action -- no generic placeholders]
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
Condition (Taken):  [what would cause this trigger to fire -- not met in this scenario]
Condition (Skipped):[what IS true in this scenario that blocks this trigger]
```

---

### STRUCTURAL INVARIANT LAYER

*This section is distinct from the PROTOCOL PREAMBLE. The PREAMBLE declares vocabulary, FM catalog, and schema contracts. This INVARIANT LAYER declares cross-phase structural obligations that hold simultaneously across all phases and all gate-language artifact surfaces. Each invariant cites the FM catalog ID whose inline tag signals a violation -- making violation tagging self-evident from the invariant text without requiring FM catalog lookup.*

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control artifacts: entry condition, job description, and exit condition. A phase body missing any of the three artifacts is a structural defect. **Violation taggable as: missing entry condition -> `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements (entry conditions and exit conditions) in phase bodies throughout this protocol SHALL use formal obligation language (SHALL/MUST) in the obligation position. A gate statement using descriptive state language is a register drift defect. **Violation taggable as: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- The LIFECYCLE OVERVIEW table gate-cell register:** The LIFECYCLE OVERVIEW table entry-condition and exit-condition cells are governed by this INVARIANT LAYER and SHALL satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). A summary-function rationale does NOT establish a register exemption for any artifact surface -- the summary or overview nature of an artifact does not confer exemption from the formal-register obligation. A reader verifying Invariant 2 SHALL verify both phase-body gate statements AND The LIFECYCLE OVERVIEW table gate cells; partial compliance (phase bodies formal, overview cells descriptive) fails Invariant 2 even when the phase bodies themselves are conforming. **Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker appearing in the output SHALL include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** The candidate trigger count N declared in Phase 1 SHALL be reconciled after Phase 3 completes: firing + non-firing + unresolved SHALL equal N. **Violation taggable as: `[RECON MISS | FM-22]`.**

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- THE LIFECYCLE OVERVIEW TABLE

Rule 1 (Governing authority): This DECLARATION governs all entry-condition and
exit-condition cells in The LIFECYCLE OVERVIEW table below. The STRUCTURAL
INVARIANT LAYER (Invariant 3) also governs these cells; this DECLARATION and
Invariant 3 are co-authoritative over The LIFECYCLE OVERVIEW table gate cells --
no artifact surface is exempt from this co-authority's formal-register obligation,
including any artifact whose nature is summary or overview. Phase-body gate
statements are governed by their respective phase-body specifications and by
Invariant 2.

Rule 2 (Register requirement): All entry-condition and exit-condition cells in
this table SHALL use formal obligation language (SHALL/MUST) in the obligation
position. A cell stating a condition without an obligation verb is non-conforming
under this Rule and under Invariant 3.

Rule 3 (Self-tagging requirement): Any entry-condition or exit-condition cell
using descriptive state language SHALL be tagged [FM-17: Gate Register Drift]
inline within that cell. A non-conforming untagged cell is a double violation:
FM-17 for register drift and FM-21 for the missing FM code.

Rule 4 (Independent row verification): A reader verifying this table SHALL check
each gate cell independently against Rules 2 and 3. Row N conformance does not
imply Row N+1 conformance.
```

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 1 | Pre-scan | Phase 1 SHALL begin when: input record change specification received and PROTOCOL PREAMBLE declared complete | Identify all candidate triggers without filtering; declare denominator N; open all three anomaly question slots OPEN; issue PCC-1 | Phase 1 SHALL be declared complete when: N is declared, all three anomaly slots are explicitly OPEN, and PCC-1 is issued |
| 2 | Sync Trigger Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued | Enumerate all sync-tier candidates using FIRING ENTRY or NON-FIRING ENTRY schema; include negative vocabulary example; order by priority | Phase 2 SHALL be declared complete when: all sync-tier candidates have resolved entries with all schema slots populated |
| 3 | Async Trigger Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate all async-tier candidates using schema; annotate latency tier per entry | Phase 3 SHALL be declared complete when: all async-tier candidates have resolved entries with all schema slots populated |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both trigger tables produced | Trace all cascade chains from side-effect field writes to terminal; assign chain IDs; apply back-edge detection | Phase 4 SHALL be declared complete when: all side-effect writes evaluated, all chains carry Chain-Status, back-edge detection applied |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete and all cascade chains carry Chain-Status | Deliver evidence-anchored verdicts for storm, missing trigger, circular trigger; propose remediation for each confirmed anomaly | Phase 5 SHALL be declared complete when: all three anomaly class verdicts issued with cited evidence and every confirmed anomaly has at least one remediation step |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and all anomaly verdicts issued | Produce trigger map with execution-tier and Spawns columns; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map covers all triggers with required columns and denominator closure is stated with CLOSED or GAP DETECTED |

---

### Phase 1 -- Pre-scan

**Entry condition:** Phase 1 SHALL begin when the input record change specification has been received and the PROTOCOL PREAMBLE has been declared complete.

**Job:** Phase 1 SHALL perform three operations before any trigger enumeration begins: (1) identify all candidate triggers without condition filtering and declare denominator N; (2) open all three anomaly question slots with explicit OPEN status; (3) scan this protocol for phrasing register violations and issue Phrasing Clearance PCC-1 if zero violations found.

**Anomaly Questions -- Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does the statuscode change from In Progress to Resolved cause more triggers to fire than the environment's operational capacity can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for this status transition that does not appear in the trigger surface? | OPEN |
| Circular Trigger | Does any trigger's output create a field write that re-activates the same or an upstream trigger? | OPEN |

**Denominator Pre-Scan:**

| Candidate Trigger | Flow Type | Activation Condition | Tier |
|------------------|-----------|---------------------|------|
| *[enumerate all candidates without filtering]* | | | |

Total candidate count N = *[integer -- declare before Phase 2 begins]*

**Exit condition:** Phase 1 SHALL be declared complete when: N is declared, all three anomaly question slots are explicitly marked OPEN, and PCC-1 is issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when: Phase 1 is complete, N is declared, and PCC-1 is issued. If PCC-1 is absent, Phase 2 SHALL NOT execute `[ENTRY CONDITION ABSENT: Phase 2 | FM-16]`.

**Job:** Phase 2 SHALL enumerate all synchronous triggers. Every sync-tier candidate from Phase 1 SHALL resolve to a FIRING ENTRY or NON-FIRING ENTRY. No candidate SHALL be omitted without a NON-FIRING ENTRY. At least one negative vocabulary example SHALL be included. [FM-11] Order by execution priority, highest first. [FM-02]

Sync trigger: executes within the same transaction (Dataverse sync plug-in step pre/post-operation; synchronous automated cloud flow on Dataverse change event).

**Negative vocabulary example (required):** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be declared complete when every sync-tier candidate has a resolved entry with all schema slots populated and no blank slots remain.

---

### Phase 3 -- Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when: Phase 2 is complete and the Sync Trigger Table is produced.

**Job:** Phase 3 SHALL enumerate all asynchronous triggers. Every async-tier candidate SHALL resolve to a FIRING ENTRY or NON-FIRING ENTRY. Order by connector tier, then by priority. [FM-02] Annotate latency tier (near-real-time / standard / batch) per entry. [FM-10]

Async trigger: executes outside the originating transaction (Dataverse async plug-in step; automated cloud flow with async trigger mode; Power Automate connector on Dataverse change events).

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be declared complete when every async-tier candidate has a resolved entry with all schema slots populated.

---

### Phase 4 -- Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when: Phase 2 and Phase 3 are complete and both trigger tables are produced.

**Job:** Phase 4 SHALL trace every cascade chain originating from side-effect field writes to its terminal. Each chain SHALL receive a Chain ID. The final row of each chain SHALL be marked [TERMINAL]. [FM-20] Back-edge detection SHALL be applied to the adjacency structure to identify any cycles. [FM-19]

**Cascade Chain Table:**

| Chain ID | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|------|--------------------|--------------------|---------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be declared complete when: all side-effect writes are evaluated, all chains carry Chain-Status, and back-edge detection has been applied.

---

### Phase 5 -- Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when: Phase 4 is complete and all cascade chains carry Chain-Status.

**Job:** Phase 5 SHALL deliver evidence-anchored verdicts for all three anomaly classes. Each verdict SHALL cite evidence from prior phases. Bare assertions SHALL be marked `[INSUFFICIENT: state evidence needed | FM-12]`. Every confirmed anomaly SHALL receive at least one remediation step. [FM-09]

**Trigger Storm:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Missing Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Circular Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Exit condition:** Phase 5 SHALL be declared complete when: all three verdicts are issued with cited evidence and every confirmed anomaly has at least one remediation step.

---

### Phase 6 -- Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when: Phase 5 is complete and all anomaly verdicts are issued.

**Job:** Phase 6 SHALL produce a trigger map with execution-tier and Spawns columns covering all triggers. Denominator closure SHALL be performed: firing + non-firing + unresolved = N.

**Trigger Map:**

| # | Trigger Name | Execution Tier | Anomaly Flag | Spawns |
|---|-------------|---------------|-------------|--------|

**Denominator Closure:** firing + non-firing + unresolved = N -> CLOSED / GAP DETECTED `[RECON MISS | FM-22]`

**Exit condition:** Phase 6 SHALL be declared complete when: trigger map covers all triggers with all required columns and denominator closure is stated with CLOSED or GAP DETECTED.
