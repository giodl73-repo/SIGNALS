---
skill: flow-trigger
round: 16
rubric_version: 15
new_criteria: [C-48, C-49, C-50]
date: 2026-03-15
---

# flow-trigger -- Round 16 (Rubric v15) Variations

**New criteria this round:**
- **C-48** -- Rule 1 sub-clause obligation element is obligation-rationale consistent: the obligation named in Rule 1's sub-clause must be "formal-register" -- the same obligation the FORMAL-GATE ZONE DECLARATION governs. A sub-clause can carry a correct rationale element and scope element while naming the wrong obligation ("platform-vocabulary"), producing a prohibition that is internally inconsistent. A misleading sub-clause is structurally worse than an absent one. C-47 requires the sub-clause to name both scope and rationale; this criterion requires the obligation element to match the governed surface.
- **C-49** -- Rule 1 sub-clause scope uses the canonical two-term pair "summary or overview": the scope element must include both "summary" and "overview", not a shortened form such as "summary nature" alone. A scope of "summary nature" only reintroduces the interpretive gap C-46 was designed to seal -- "overview", "digest", and "index" artifacts remain arguably exempt. The canonical two-term pair is the minimum scope for Rule 1 to be self-sealing to the same degree as Invariant 3.
- **C-50** -- Rule 1 sub-clause reproduces C-46's em-dash restatement structural pattern: Rule 1's sub-clause must follow the same two-part em-dash structure C-46 requires in Invariant 3: initial assertion clause + em-dash separator + operational restatement naming the blocked rationale in concrete terms. C-47 does not explicitly require this structural pattern -- it requires scope and rationale to be present, but not that they appear in the em-dash two-part form. C-50 closes that gap.

**Round 15 gap analysis:**
- V-01: C-47 ABSENT -- Rule 1 ends after co-authority reference; no sub-clause at all
- V-02: C-47 ABSENT -- sub-clause has artifact-agnostic scope ("no artifact surface") and correct obligation but no named rationale (summary-or-overview nature not stated)
- V-03: C-47 ABSENT -- correct rationale and scope but wrong obligation ("platform-vocabulary"); internally inconsistent; C-48 candidate revealed
- V-04: C-47 ABSENT -- correct obligation and em-dash but "summary nature" only, not "summary or overview"; C-49 candidate revealed
- V-05: C-47 PASS + C-50 bonus signal -- full sub-clause: correct obligation ("formal-register"), both terms ("summary or overview"), em-dash restatement explicit; fourth element (em-dash structure) identified as C-50 candidate

All R16 variations carry **C-46 PASS** in Invariant 3 and **C-47 PASS** in Rule 1 (sub-clause present with scope and rationale). The single variation axis is the sub-clause's three new sub-element properties: obligation name (C-48), scope completeness (C-49), and em-dash restatement structure (C-50).

**Variation axes:**

| Variation | Axis | C-48 | C-49 | C-50 | Hypothesis |
|-----------|------|------|------|------|------------|
| V-01 | Obligation element -- Rule 1 sub-clause names wrong obligation ("platform-vocabulary") while scope and em-dash are correct | FAIL | PASS | PASS | C-47 passes (scope+rationale present); C-48 fails: the named obligation (platform-vocabulary) is structurally inconsistent with the named rationale (summary-or-overview nature); a platform-vocabulary obligation is not typically exempted on summary-function grounds; the sub-clause is internally misleading |
| V-02 | Scope element -- Rule 1 sub-clause names correct obligation and has em-dash but uses "summary nature" only, not "summary or overview" | PASS | FAIL | PASS | C-47 passes; C-48 passes (correct obligation); C-49 fails: "overview", "digest", and "index" artifacts remain arguable exemption candidates; the two-term canonical pair is the minimum necessary to match Invariant 3's self-sealing coverage |
| V-03 | Structural form -- Rule 1 sub-clause has correct obligation and correct scope term pair but no em-dash restatement (single assertion clause only) | PASS | PASS | FAIL | C-47 passes; C-48 and C-49 pass; C-50 fails: the sub-clause asserts the prohibition but does not operationally restate the blocked rationale in a second clause; a reader who reads only the assertion without the restatement encounters a weaker prohibition that lacks the self-sealing architecture of Invariant 3 |
| V-04 | Compound failure -- assertion clause uses correct obligation ("formal-register") but em-dash restatement names different obligation ("platform-vocabulary"); scope incomplete ("summary nature" only) | FAIL | FAIL | PASS | C-47 passes; C-48 fails: obligation inconsistency within the sub-clause itself -- assertion and restatement name different obligations, making the sub-clause self-contradictory on obligation; C-49 fails: scope incomplete; the compound defect is distinct from V-01 because here the assertion clause is correct and only the restatement drifts |
| V-05 | Full combination -- correct obligation ("formal-register"), both scope terms ("summary or overview"), em-dash restatement present | PASS | PASS | PASS | All three C-48/C-49/C-50 requirements met from Rule 1 alone; sub-clause is self-sealing: correct governed surface, complete scope, and structural restatement that closes interpretive wedge arguments without consulting Invariant 3 |

**Scenario used in all variations:** A Dataverse `incident` record's `statuscode` field has changed from `In Progress` (2) to `Resolved` (5) in a Dynamics 365 Customer Service environment.

---

## V-01

**Variation axis:** Obligation element -- Rule 1 sub-clause names wrong obligation ("platform-vocabulary") with correct scope ("summary or overview") and correct em-dash restatement structure
**Hypothesis:** C-47 passes: sub-clause is present, scope is artifact-qualified ("summary or overview"), and rationale is named. C-48 fails: the obligation named in both the assertion clause and the restatement is "platform-vocabulary" rather than "formal-register". The named rationale (summary-or-overview nature) does not apply to the named obligation (platform-vocabulary): platform-vocabulary conformance is not the kind of obligation that summary-function exemptions are typically invoked to escape, making the sub-clause internally inconsistent. A reader checking Rule 1 for guidance on the formal-register obligation finds a sub-clause that governs a different obligation entirely. The sub-clause is structurally present (C-47 passes) but governs the wrong surface.

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

*Structural independence note: FM-16 (Entry Condition Absent) and FM-17 (Gate Register Drift) are structurally non-overlapping failure modes requiring separate FM IDs. The independence covers all three intersection cases:*

*FM-16 alone: A phase has no entry condition. Defect is presence, not quality. Register evaluation is not applicable -- no condition text exists to evaluate. Inline tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. FM-17 does NOT apply.*

*FM-17 alone: A phase has an entry condition stated descriptively rather than with formal obligation language. Presence satisfied; only register quality fails. Inline tag: `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. FM-16 does NOT apply.*

*Both simultaneously: A phase has no entry condition AND the document's register pattern indicates that a condition, if present, would also be stated descriptively. Both defects co-occur and are independently taggable: `[ENTRY CONDITION ABSENT: Phase N | FM-16]` AND `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. A single FM ID would conflate all three cases -- separate IDs make each tag independently informative.*

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

*Distinct from the PROTOCOL PREAMBLE. The PREAMBLE declares vocabulary, FM catalog, and schema contracts. This INVARIANT LAYER declares cross-phase structural obligations holding simultaneously across all phases and all gate-language artifact surfaces. Each invariant cites the FM catalog ID whose inline tag signals a violation.*

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control artifacts: entry condition, job description, and exit condition. **Violation taggable as: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements in phase bodies SHALL use formal obligation language (SHALL/MUST) in the obligation position. **Violation taggable as: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- The LIFECYCLE OVERVIEW table gate-cell register:** The LIFECYCLE OVERVIEW table entry-condition and exit-condition cells are governed by this INVARIANT LAYER and SHALL satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). The LIFECYCLE OVERVIEW table is NOT exempt from Invariant 2 by virtue of its summary function -- the summary or overview nature of an artifact does not confer exemption from the formal-register obligation. A reader verifying Invariant 2 SHALL verify both phase-body gate statements AND The LIFECYCLE OVERVIEW table gate cells; partial compliance fails Invariant 2 even when the phase bodies themselves are conforming. **Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker SHALL include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** The candidate trigger count N declared in Phase 1 SHALL be reconciled after Phase 3: firing + non-firing + unresolved SHALL equal N. **Violation taggable as: `[RECON MISS | FM-22]`.**

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- THE LIFECYCLE OVERVIEW TABLE

Rule 1 (Governing authority): This DECLARATION governs all entry-condition and
exit-condition cells in The LIFECYCLE OVERVIEW table below. The STRUCTURAL
INVARIANT LAYER (Invariant 3) also governs these cells; this DECLARATION and
Invariant 3 are co-authoritative over The LIFECYCLE OVERVIEW table gate cells.
No artifact surface is exempt from this co-authority's platform-vocabulary
obligation, including any artifact whose nature is summary or overview -- the
summary or overview nature of an artifact does not confer exemption from the
platform-vocabulary obligation.
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
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and all anomaly verdicts issued | Produce trigger map with execution-tier and Spawns columns; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map covers all triggers with required columns and denominator closure stated with CLOSED or GAP DETECTED |

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

**Variation axis:** Scope element -- Rule 1 sub-clause names correct obligation ("formal-register") and has em-dash restatement but uses "summary nature" only, dropping "overview"
**Hypothesis:** C-47 passes: sub-clause present, rationale named, scope term present. C-48 passes: obligation "formal-register" is correct. C-49 fails: the scope term is "summary nature" alone -- an artifact labeled "overview", "digest", or "index" can argue the sub-clause addresses only items explicitly classified as summaries, and that overview-type artifacts are a separate class not covered. The interpretive gap that C-46 sealed in Invariant 3 is reintroduced at the Rule 1 level: "overview" is not blocked by name in the sub-clause. C-50 passes: em-dash restatement is structurally present (two-part form).

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

*Structural independence note: FM-16 (Entry Condition Absent) and FM-17 (Gate Register Drift) are structurally non-overlapping failure modes requiring separate FM IDs. The independence covers all three intersection cases:*

*FM-16 alone: A phase has no entry condition. Defect is presence, not quality. Register evaluation is not applicable -- no condition text exists to evaluate. Inline tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. FM-17 does NOT apply.*

*FM-17 alone: A phase has an entry condition stated descriptively rather than with formal obligation language. Presence satisfied; only register quality fails. Inline tag: `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. FM-16 does NOT apply.*

*Both simultaneously: A phase has no entry condition AND the document's register pattern indicates that a condition, if present, would also be stated descriptively. Both defects co-occur and are independently taggable: `[ENTRY CONDITION ABSENT: Phase N | FM-16]` AND `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. A single FM ID would conflate all three cases -- separate IDs make each tag independently informative.*

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

*Distinct from the PROTOCOL PREAMBLE. The PREAMBLE declares vocabulary, FM catalog, and schema contracts. This INVARIANT LAYER declares cross-phase structural obligations holding simultaneously across all phases and all gate-language artifact surfaces. Each invariant cites the FM catalog ID whose inline tag signals a violation.*

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control artifacts: entry condition, job description, and exit condition. **Violation taggable as: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements in phase bodies SHALL use formal obligation language (SHALL/MUST) in the obligation position. **Violation taggable as: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- The LIFECYCLE OVERVIEW table gate-cell register:** The LIFECYCLE OVERVIEW table entry-condition and exit-condition cells are governed by this INVARIANT LAYER and SHALL satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). The LIFECYCLE OVERVIEW table is NOT exempt from Invariant 2 by virtue of its summary function -- the summary or overview nature of an artifact does not confer exemption from the formal-register obligation. A reader verifying Invariant 2 SHALL verify both phase-body gate statements AND The LIFECYCLE OVERVIEW table gate cells; partial compliance fails Invariant 2 even when the phase bodies themselves are conforming. **Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker SHALL include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** The candidate trigger count N declared in Phase 1 SHALL be reconciled after Phase 3: firing + non-firing + unresolved SHALL equal N. **Violation taggable as: `[RECON MISS | FM-22]`.**

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- THE LIFECYCLE OVERVIEW TABLE

Rule 1 (Governing authority): This DECLARATION governs all entry-condition and
exit-condition cells in The LIFECYCLE OVERVIEW table below. The STRUCTURAL
INVARIANT LAYER (Invariant 3) also governs these cells; this DECLARATION and
Invariant 3 are co-authoritative over The LIFECYCLE OVERVIEW table gate cells.
No artifact surface is exempt from this co-authority's formal-register
obligation, including any artifact whose nature is a summary -- the summary
nature of an artifact does not confer exemption from the formal-register
obligation.
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
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and all anomaly verdicts issued | Produce trigger map with execution-tier and Spawns columns; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map covers all triggers with required columns and denominator closure stated with CLOSED or GAP DETECTED |

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

**Variation axis:** Structural form -- Rule 1 sub-clause has correct obligation ("formal-register") and correct two-term scope ("summary or overview") but no em-dash restatement: the sub-clause is a single assertion clause without a second operational restatement clause
**Hypothesis:** C-47 passes: sub-clause is present; the scope qualifier "whose nature is summary or overview" supplies both scope and rationale within a single clause; the obligation is named. C-48 passes: obligation is "formal-register". C-49 passes: both "summary" and "overview" are named. C-50 fails: the sub-clause lacks the em-dash + second clause that operationally restates the blocked rationale. A reader finds the assertion ("no artifact surface is exempt... including any artifact whose nature is summary or overview") but no follow-through clause making the prohibition operationally concrete. The assertion-only form is weaker than Invariant 3's two-part structure: without the restatement, a reader can argue the scope qualifier is merely illustrative rather than a complete prohibition.

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

*Structural independence note: FM-16 (Entry Condition Absent) and FM-17 (Gate Register Drift) are structurally non-overlapping failure modes requiring separate FM IDs. The independence covers all three intersection cases:*

*FM-16 alone: A phase has no entry condition. Defect is presence, not quality. Register evaluation is not applicable -- no condition text exists to evaluate. Inline tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. FM-17 does NOT apply.*

*FM-17 alone: A phase has an entry condition stated descriptively rather than with formal obligation language. Presence satisfied; only register quality fails. Inline tag: `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. FM-16 does NOT apply.*

*Both simultaneously: A phase has no entry condition AND the document's register pattern indicates that a condition, if present, would also be stated descriptively. Both defects co-occur and are independently taggable: `[ENTRY CONDITION ABSENT: Phase N | FM-16]` AND `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. A single FM ID would conflate all three cases -- separate IDs make each tag independently informative.*

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

*Distinct from the PROTOCOL PREAMBLE. The PREAMBLE declares vocabulary, FM catalog, and schema contracts. This INVARIANT LAYER declares cross-phase structural obligations holding simultaneously across all phases and all gate-language artifact surfaces. Each invariant cites the FM catalog ID whose inline tag signals a violation.*

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control artifacts: entry condition, job description, and exit condition. **Violation taggable as: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements in phase bodies SHALL use formal obligation language (SHALL/MUST) in the obligation position. **Violation taggable as: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- The LIFECYCLE OVERVIEW table gate-cell register:** The LIFECYCLE OVERVIEW table entry-condition and exit-condition cells are governed by this INVARIANT LAYER and SHALL satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). The LIFECYCLE OVERVIEW table is NOT exempt from Invariant 2 by virtue of its summary function -- the summary or overview nature of an artifact does not confer exemption from the formal-register obligation. A reader verifying Invariant 2 SHALL verify both phase-body gate statements AND The LIFECYCLE OVERVIEW table gate cells; partial compliance fails Invariant 2 even when the phase bodies themselves are conforming. **Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker SHALL include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** The candidate trigger count N declared in Phase 1 SHALL be reconciled after Phase 3: firing + non-firing + unresolved SHALL equal N. **Violation taggable as: `[RECON MISS | FM-22]`.**

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- THE LIFECYCLE OVERVIEW TABLE

Rule 1 (Governing authority): This DECLARATION governs all entry-condition and
exit-condition cells in The LIFECYCLE OVERVIEW table below. The STRUCTURAL
INVARIANT LAYER (Invariant 3) also governs these cells; this DECLARATION and
Invariant 3 are co-authoritative over The LIFECYCLE OVERVIEW table gate cells.
No artifact surface is exempt from this co-authority's formal-register
obligation, including any artifact whose nature is summary or overview.
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
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and all anomaly verdicts issued | Produce trigger map with execution-tier and Spawns columns; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map covers all triggers with required columns and denominator closure stated with CLOSED or GAP DETECTED |

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

**Variation axis:** Compound failure -- assertion clause names correct obligation ("formal-register") but the em-dash restatement names a different obligation ("platform-vocabulary"); scope is also incomplete ("summary nature" only, dropping "overview")
**Hypothesis:** C-47 passes: sub-clause present with scope qualifier and rationale in the em-dash restatement. C-48 fails: obligation inconsistency within the sub-clause itself -- the assertion clause says "formal-register obligation" but the em-dash restatement says "platform-vocabulary obligation"; the two clauses are not obligation-consistent with each other; a reader checking the sub-clause for formal-register prohibition finds the assertion supports it but the restatement undermines it by naming a different obligation. C-49 fails: "summary nature" only, "overview" not named. The compound defect is distinct from V-01 (which has wrong obligation consistently throughout): here the assertion is correct and only the restatement drifts, making the sub-clause self-contradictory on obligation rather than uniformly wrong.

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

*Structural independence note: FM-16 (Entry Condition Absent) and FM-17 (Gate Register Drift) are structurally non-overlapping failure modes requiring separate FM IDs. The independence covers all three intersection cases:*

*FM-16 alone: A phase has no entry condition. Defect is presence, not quality. Register evaluation is not applicable -- no condition text exists to evaluate. Inline tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. FM-17 does NOT apply.*

*FM-17 alone: A phase has an entry condition stated descriptively rather than with formal obligation language. Presence satisfied; only register quality fails. Inline tag: `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. FM-16 does NOT apply.*

*Both simultaneously: A phase has no entry condition AND the document's register pattern indicates that a condition, if present, would also be stated descriptively. Both defects co-occur and are independently taggable: `[ENTRY CONDITION ABSENT: Phase N | FM-16]` AND `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. A single FM ID would conflate all three cases -- separate IDs make each tag independently informative.*

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

*Distinct from the PROTOCOL PREAMBLE. The PREAMBLE declares vocabulary, FM catalog, and schema contracts. This INVARIANT LAYER declares cross-phase structural obligations holding simultaneously across all phases and all gate-language artifact surfaces. Each invariant cites the FM catalog ID whose inline tag signals a violation.*

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control artifacts: entry condition, job description, and exit condition. **Violation taggable as: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements in phase bodies SHALL use formal obligation language (SHALL/MUST) in the obligation position. **Violation taggable as: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- The LIFECYCLE OVERVIEW table gate-cell register:** The LIFECYCLE OVERVIEW table entry-condition and exit-condition cells are governed by this INVARIANT LAYER and SHALL satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). The LIFECYCLE OVERVIEW table is NOT exempt from Invariant 2 by virtue of its summary function -- the summary or overview nature of an artifact does not confer exemption from the formal-register obligation. A reader verifying Invariant 2 SHALL verify both phase-body gate statements AND The LIFECYCLE OVERVIEW table gate cells; partial compliance fails Invariant 2 even when the phase bodies themselves are conforming. **Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker SHALL include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** The candidate trigger count N declared in Phase 1 SHALL be reconciled after Phase 3: firing + non-firing + unresolved SHALL equal N. **Violation taggable as: `[RECON MISS | FM-22]`.**

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- THE LIFECYCLE OVERVIEW TABLE

Rule 1 (Governing authority): This DECLARATION governs all entry-condition and
exit-condition cells in The LIFECYCLE OVERVIEW table below. The STRUCTURAL
INVARIANT LAYER (Invariant 3) also governs these cells; this DECLARATION and
Invariant 3 are co-authoritative over The LIFECYCLE OVERVIEW table gate cells.
No artifact surface is exempt from this co-authority's formal-register
obligation, including any artifact whose nature is a summary -- the summary
nature of an artifact does not confer exemption from the platform-vocabulary
obligation.
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
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and all anomaly verdicts issued | Produce trigger map with execution-tier and Spawns columns; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map covers all triggers with required columns and denominator closure stated with CLOSED or GAP DETECTED |

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

**Variation axis:** Full combination -- Rule 1 sub-clause has correct obligation ("formal-register"), canonical two-term scope ("summary or overview"), and em-dash restatement structural pattern
**Hypothesis:** C-47 passes: sub-clause present, scope named, rationale named. C-48 passes: obligation is "formal-register" -- the same obligation the FORMAL-GATE ZONE DECLARATION governs; obligation and rationale are consistent (summary-or-overview exemption is a claim that would be invoked specifically against formal-register requirements). C-49 passes: both "summary" and "overview" are named in the canonical two-term pair; the scope is complete and self-sealing to the same degree as Invariant 3. C-50 passes: the sub-clause follows the two-part em-dash structure -- initial assertion clause names the obligation and scope, em-dash separator, operational restatement concretely names the blocked rationale. The sub-clause is independently self-sealing: a reader who checks Rule 1 alone, without consulting Invariant 3, encounters the complete prohibition in structurally self-reinforcing form. This is the R16 baseline for the bonus signal scan (C-51 candidates).

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

*Structural independence note: FM-16 (Entry Condition Absent) and FM-17 (Gate Register Drift) are structurally non-overlapping failure modes requiring separate FM IDs. The independence covers all three intersection cases:*

*FM-16 alone: A phase has no entry condition. Defect is presence, not quality. Register evaluation is not applicable -- no condition text exists to evaluate. Inline tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. FM-17 does NOT apply.*

*FM-17 alone: A phase has an entry condition stated descriptively rather than with formal obligation language. Presence satisfied; only register quality fails. Inline tag: `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. FM-16 does NOT apply.*

*Both simultaneously: A phase has no entry condition AND the document's register pattern indicates that a condition, if present, would also be stated descriptively. Both defects co-occur and are independently taggable: `[ENTRY CONDITION ABSENT: Phase N | FM-16]` AND `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. A single FM ID would conflate all three cases -- separate IDs make each tag independently informative.*

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

*Distinct from the PROTOCOL PREAMBLE. The PREAMBLE declares vocabulary, FM catalog, and schema contracts. This INVARIANT LAYER declares cross-phase structural obligations holding simultaneously across all phases and all gate-language artifact surfaces. Each invariant cites the FM catalog ID whose inline tag signals a violation.*

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control artifacts: entry condition, job description, and exit condition. **Violation taggable as: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements in phase bodies SHALL use formal obligation language (SHALL/MUST) in the obligation position. **Violation taggable as: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- The LIFECYCLE OVERVIEW table gate-cell register:** The LIFECYCLE OVERVIEW table entry-condition and exit-condition cells are governed by this INVARIANT LAYER and SHALL satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). The LIFECYCLE OVERVIEW table is NOT exempt from Invariant 2 by virtue of its summary function -- the summary or overview nature of an artifact does not confer exemption from the formal-register obligation. A reader verifying Invariant 2 SHALL verify both phase-body gate statements AND The LIFECYCLE OVERVIEW table gate cells; partial compliance fails Invariant 2 even when the phase bodies themselves are conforming. **Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker SHALL include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** The candidate trigger count N declared in Phase 1 SHALL be reconciled after Phase 3: firing + non-firing + unresolved SHALL equal N. **Violation taggable as: `[RECON MISS | FM-22]`.**

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- THE LIFECYCLE OVERVIEW TABLE

Rule 1 (Governing authority): This DECLARATION governs all entry-condition and
exit-condition cells in The LIFECYCLE OVERVIEW table below. The STRUCTURAL
INVARIANT LAYER (Invariant 3) also governs these cells; this DECLARATION and
Invariant 3 are co-authoritative over The LIFECYCLE OVERVIEW table gate cells.
No artifact surface is exempt from this co-authority's formal-register
obligation, including any artifact whose nature is summary or overview -- the
summary or overview nature of an artifact does not confer exemption from the
formal-register obligation.
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
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and all anomaly verdicts issued | Produce trigger map with execution-tier and Spawns columns; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map covers all triggers with required columns and denominator closure stated with CLOSED or GAP DETECTED |

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
