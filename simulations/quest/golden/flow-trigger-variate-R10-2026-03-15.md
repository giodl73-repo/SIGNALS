---
skill: flow-trigger
round: 10
rubric_version: 10
new_criteria: [C-34, C-35, C-36, C-37]
date: 2026-03-15
---

# flow-trigger — Round 10 (Rubric v10) Variations

**New criteria this round:**
- **C-34** — INVARIANT LAYER numbered invariants are FM-ID-anchored: each numbered invariant governing a gate obligation cites the FM catalog ID whose inline tag signals a violation, making violation tagging self-evident from the invariant text without catalog lookup.
- **C-35** — PHASE-BOUNDARY DEFECT CLASSES sub-header includes structural independence explanation: the FM catalog grouping of FM-16 and FM-17 states explicitly why a single FM ID would conflate detection and why the two classes are structurally non-overlapping.
- **C-36** — FORMAL-GATE ZONE DECLARATION is a numbered code block with four or more rules: the LIFECYCLE OVERVIEW declaration takes the code-block form, making each rule independently addressable and mechanically auditable.
- **C-37** — INVARIANT LAYER includes invariant explicitly governing LIFECYCLE OVERVIEW gate-cell register: at least one numbered invariant directly names the LIFECYCLE OVERVIEW gate cells as within scope of the cross-phase formal-register authority.

**Variation axes:**

| Variation | Axis | Hypothesis |
|-----------|------|------------|
| V-01 | INVARIANT LAYER — FM-ID-anchored invariants (C-34 only) | When each numbered invariant includes an FM-ID citation, violation tagging is self-evident from the invariant text; the INVARIANT LAYER and FM catalog become mutually cross-referencing |
| V-02 | FM catalog — PHASE-BOUNDARY DEFECT CLASSES independence explanation (C-35 only) | When the sub-header includes a structural independence note, the catalog is self-justifying: a reader understands why a single FM ID would conflate entry-condition absence with gate-register drift |
| V-03 | LIFECYCLE OVERVIEW — FORMAL-GATE ZONE DECLARATION as numbered code block (C-36 only) | Converting the declaration from prose annotation to a numbered code block makes each constraint independently addressable without prose interpretation |
| V-04 | INVARIANT LAYER — explicit LIFECYCLE OVERVIEW governing invariant (C-37 only) | When an invariant explicitly names the LIFECYCLE OVERVIEW gate cells, the three gate-register surfaces are cross-linked from a single pre-Phase-1 declaration |
| V-05 | All four axes combined — C-34 + C-35 + C-36 + C-37 simultaneously | FM-ID-anchored invariants + self-justifying catalog + auditable code-block declaration + INVARIANT LAYER/overview cross-link |

---

## V-01

**Variation axis:** INVARIANT LAYER — FM-ID-anchored invariants (C-34 only)
**Hypothesis:** When each numbered invariant in the INVARIANT LAYER includes an FM-ID citation in its obligation text, violation tagging is self-evident from the invariant itself. A reviewer scanning the INVARIANT LAYER can determine the correct inline tag without consulting the FM catalog, making the two artifacts mutually cross-referencing.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A record change has occurred. Your task: determine exactly which automations fire, in what order, with what inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular triggers).

Execute the following phases in strict sequence. Each phase SHALL complete before the next begins.

---

### PROTOCOL PREAMBLE

#### Platform Term Contract

Approved vocabulary:

| Approved Term | Prohibited Substitutions |
|--------------|-------------------------|
| automated cloud flow | workflow, automation, rule |
| instant cloud flow | manual flow, button flow |
| scheduled cloud flow | recurring flow, timer flow |
| Dataverse plug-in | plugin, CRM plugin |
| sync plug-in step | synchronous plugin |
| async plug-in step | asynchronous plugin |
| trigger event: When a row is added, modified or deleted | record trigger, update trigger |
| Power Automate connector | connector trigger |

Deviations SHALL be tagged `[VOCAB FAIL: "actual text" -> correction | FM-08]`.

#### FM Catalog

| FM Code | Failure Mode | Expected Behavior | Output Marker | Phase(s) |
|---------|-------------|-------------------|---------------|----------|
| FM-01 | Trigger omission | Every bound trigger listed | `[OMIT: trigger-name | FM-01]` | 2, 3 |
| FM-02 | Firing order violation | Sync before async; by priority within tier | `[ORDER FAIL: actual | FM-02]` | 2, 3 |
| FM-03 | Missing input/output specification | Named input payload and output action | `[IO FAIL: trigger-name | FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three classes addressed | `[PATH MISS: class | FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name | FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced to terminal | `[CASCADE SHALLOW | FM-06]` | 4 |
| FM-07 | Missing conditional branch | Both branches stated | `[BRANCH MISS: trigger-name | FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used | `[VOCAB FAIL: "actual" -> correction | FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with mitigation | `[RISK MISS | FM-09]` | 5 |
| FM-10 | Missing timing annotation | Latency noted per trigger | `[TIMING MISS: trigger-name | FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct pair | `[NEG MISS | FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence | `[INSUFFICIENT: evidence needed | FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition per chain | `[CHAIN OPEN: CH-NN | FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger | `[GRAPH MISS | FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before filtering | `[DENOM MISS | FM-15]` | 1 |
| FM-16 | Entry Condition Absent | Phase has no entry precondition | `[ENTRY CONDITION ABSENT: Phase N | FM-16]` | All |
| FM-17 | Gate Register Drift | Gate statement uses descriptive language where SHALL/MUST required | `[GATE REGISTER DRIFT: Phase N gate | FM-17]` | All |
| FM-18 | No sync/async structural split | Sync and async in separate phases | `[SPLIT MISS | FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied | `[BACKTRACK MISS | FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN | FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies N = sum | `[RECON MISS | FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing entry | `[SE MISS: trigger-name | FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade columns | `[MAP MISS | FM-25]` | 6 |

*FM-21 is self-referential: any violation marker without an FM code is itself an FM-21 violation.*

**PHASE-BOUNDARY DEFECT CLASSES**

| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N | FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate | FM-17]` | All phases |

#### Entry Schema Contract

**FIRING ENTRY** (all slots required):

    Trigger Name:
    Flow Type:          [automated cloud flow | Dataverse plug-in | ...]
    Execution Tier:     [sync | async | scheduled]
    Trigger Event:
    Input Fields:       [specific named fields -- no placeholders]
    Output Action:      [specific action -- no placeholders]
    Side Effects:       [field writes beyond primary output, or "none"]
    Condition (Taken):  [what must be true for this trigger to fire]
    Condition (Skipped):[what would cause this trigger NOT to fire]
    Anomaly Flag:       [none | storm | missing | circular]

**NON-FIRING ENTRY** (all slots required):

    Trigger Name:
    Flow Type:
    Reason Not Firing:
    Condition (Taken):
    Condition (Skipped):

---

### STRUCTURAL INVARIANT LAYER

*Distinct from the PROTOCOL PREAMBLE. These are cross-phase structural obligations applying to all phases simultaneously. Each invariant cites the FM catalog ID whose inline tag signals a violation -- making violation tagging self-evident from the invariant text without catalog lookup.*

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control artifacts: entry condition, job description, and exit condition. A phase body missing any artifact is a structural defect. **Violation taggable as: missing entry condition -> `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register:** All gate statements (entry conditions and exit conditions) in phase bodies SHALL use formal obligation language (SHALL/MUST) in the obligation position. Descriptive state language in gate positions is a register drift defect. **Violation taggable as: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- LIFECYCLE OVERVIEW gate-cell register:** The LIFECYCLE OVERVIEW table entry-condition and exit-condition cells SHALL use formal obligation language (SHALL/MUST). Cells using descriptive state language SHALL be tagged inline. **Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker appearing in the output SHALL include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** Candidate count N declared in Phase 1 SHALL be reconciled after enumeration: firing + non-firing + unresolved SHALL equal N. **Violation taggable as: `[RECON MISS | FM-22]`.**

---

### LIFECYCLE OVERVIEW

*This table lists all phases with entry condition, job description, and exit condition. LIFECYCLE OVERVIEW gate cells SHALL use formal obligation language (SHALL/MUST) per Invariant 3 above. Cells using descriptive state language SHALL be tagged `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N | FM-17]`.*

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 1 | Pre-scan | Phase 1 SHALL begin when: input received and PREAMBLE declared | Identify all candidates; declare N; open anomaly slots; issue PCC-1 | Phase 1 SHALL be declared complete when: N declared, anomaly slots OPEN, PCC-1 issued |
| 2 | Sync Trigger Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued | Enumerate sync-tier candidates with full schema; include negative vocabulary example | Phase 2 SHALL be declared complete when: all sync-tier candidates have resolved entries with all slots populated |
| 3 | Async Trigger Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate async-tier candidates with schema; annotate latency tier | Phase 3 SHALL be declared complete when: all async-tier candidates have resolved entries with all slots populated |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both tables produced | Trace cascade chains; assign chain IDs; back-edge detection | Phase 4 SHALL be declared complete when: all side-effect writes evaluated, all chains carry Chain-Status, back-edge detection complete |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete and chains resolved | Deliver evidence-anchored verdicts for three anomaly classes; remediate confirmed anomalies | Phase 5 SHALL be declared complete when: all three verdicts issued with evidence and confirmed anomalies have remediations |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and anomaly verdicts issued | Produce trigger map with tier and cascade columns; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map complete and denominator arithmetic stated |

---

### Phase 1 -- Pre-scan

**Entry condition:** Phase 1 SHALL begin when the input record change specification has been received and the PROTOCOL PREAMBLE has been declared complete.

**Job:** Identify all candidate triggers without condition filtering; declare denominator N; open all three anomaly question slots; issue Phrasing Clearance PCC-1.

**Phrasing Audit:** Scan this protocol for informal constructions. Issue PCC-1 if zero violations found.

**Anomaly Questions -- Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does any single change cause more triggers than operational capacity allows? | OPEN |
| Missing Trigger | Is an expected automation absent from the trigger surface? | OPEN |
| Circular Trigger | Does any trigger output re-activate the same or upstream trigger? | OPEN |

**Denominator Pre-Scan:**

| Candidate Trigger | Flow Type | Activation Condition | Tier |
|------------------|-----------|---------------------|------|
| *[enumerate all candidates -- no filtering yet]* | | | |

Total candidate count N = *[integer]*

**Exit condition:** Phase 1 SHALL be declared complete when N is declared, all three anomaly slots are OPEN, and PCC-1 is issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued. If PCC-1 is absent Phase 2 SHALL NOT execute `[ENTRY CONDITION ABSENT: Phase 2 | FM-16]`.

**Job:** Enumerate all sync-tier candidates using FIRING ENTRY or NON-FIRING ENTRY schema. Include at least one negative vocabulary example. Order by priority. [FM-02]

Sync trigger: executes within the same transaction (Dataverse sync plug-in step pre/post-operation; synchronous automated cloud flow on Dataverse change event).

**Negative vocabulary example (required):** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be declared complete when all sync-tier candidates have resolved entries with all schema slots populated.

---

### Phase 3 -- Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced.

**Job:** Enumerate all async-tier candidates using schema. Annotate latency tier (near-real-time/standard/batch) per entry.

Async trigger: executes outside the originating transaction (Dataverse async plug-in step; automated cloud flow with async trigger mode; Power Automate connector on Dataverse change events).

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be declared complete when all async-tier candidates have resolved entries with all schema slots populated.

---

### Phase 4 -- Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both trigger tables produced.

**Job:** Trace cascade chains until no further triggers fire (no depth limit). [FM-13] Assign chain IDs (CH-01, CH-02, ...). Mark last row of each chain [TERMINAL]. [FM-20] Apply back-edge detection after all chains traced. [FM-19]

**Cascade Chain Table:**

| Chain ID | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|------|--------------------|--------------------|---------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be declared complete when all side-effect writes are evaluated, all chains carry Chain-Status, and back-edge detection is complete.

---

### Phase 5 -- Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when: Phase 4 complete and cascade chains resolved.

**Job:** Deliver evidence-anchored verdicts for all three anomaly classes. Cite evidence per verdict. Bare assertions SHALL be marked `[INSUFFICIENT | FM-12]`. Confirmed anomalies SHALL each receive a remediation step. [FM-09]

**Trigger Storm:** Evidence: | Verdict: | Remediation:

**Missing Trigger:** Evidence: | Verdict: | Remediation:

**Circular Trigger:** Evidence: | Verdict: | Remediation:

**Exit condition:** Phase 5 SHALL be declared complete when all three verdicts are issued with evidence and confirmed anomalies have remediation steps.

---

### Phase 6 -- Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when: Phase 5 complete and anomaly verdicts issued.

**Job:** Produce trigger map with execution-tier and Spawns columns. Perform denominator closure: firing + non-firing + unresolved = N.

**Trigger Map:**

| # | Trigger Name | Execution Tier | Anomaly Flag | Spawns |
|---|-------------|---------------|-------------|--------|

**Denominator Closure:** firing + non-firing + unresolved = N -> CLOSED / GAP DETECTED `[RECON MISS | FM-22]`

**Exit condition:** Phase 6 SHALL be declared complete when trigger map covers all triggers and denominator closure arithmetic is stated.

---
---

## V-02

**Variation axis:** FM catalog -- PHASE-BOUNDARY DEFECT CLASSES independence explanation (C-35 only)
**Hypothesis:** When the PHASE-BOUNDARY DEFECT CLASSES sub-header includes an explicit structural independence note explaining why FM-16 and FM-17 cannot share a single FM ID, the catalog becomes self-justifying. A reader understands not just that two IDs exist but why the distinction matters for defect detection.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A record change has occurred. Your task: determine exactly which automations fire, in what order, with what inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular triggers).

Execute the following phases in strict sequence. Each phase SHALL complete before the next begins.

---

### PROTOCOL PREAMBLE

#### Platform Term Contract

Approved vocabulary:

| Approved Term | Prohibited Substitutions |
|--------------|-------------------------|
| automated cloud flow | workflow, automation, rule |
| instant cloud flow | manual flow, button flow |
| scheduled cloud flow | recurring flow, timer flow |
| Dataverse plug-in | plugin, CRM plugin |
| sync plug-in step | synchronous plugin |
| async plug-in step | asynchronous plugin |
| trigger event: When a row is added, modified or deleted | record trigger, update trigger |
| Power Automate connector | connector trigger |

Deviations SHALL be tagged `[VOCAB FAIL: "actual text" -> correction | FM-08]`.

#### FM Catalog

| FM Code | Failure Mode | Expected Behavior | Output Marker | Phase(s) |
|---------|-------------|-------------------|---------------|----------|
| FM-01 | Trigger omission | Every bound trigger listed | `[OMIT: trigger-name | FM-01]` | 2, 3 |
| FM-02 | Firing order violation | Sync before async; by priority within tier | `[ORDER FAIL: actual | FM-02]` | 2, 3 |
| FM-03 | Missing input/output specification | Named input payload and output action | `[IO FAIL: trigger-name | FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three classes addressed | `[PATH MISS: class | FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name | FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced to terminal | `[CASCADE SHALLOW | FM-06]` | 4 |
| FM-07 | Missing conditional branch | Both branches stated | `[BRANCH MISS: trigger-name | FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used | `[VOCAB FAIL: "actual" -> correction | FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with mitigation | `[RISK MISS | FM-09]` | 5 |
| FM-10 | Missing timing annotation | Latency noted per trigger | `[TIMING MISS: trigger-name | FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct pair | `[NEG MISS | FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence | `[INSUFFICIENT: evidence needed | FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition per chain | `[CHAIN OPEN: CH-NN | FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger | `[GRAPH MISS | FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before filtering | `[DENOM MISS | FM-15]` | 1 |
| FM-18 | No sync/async structural split | Sync and async in separate phases | `[SPLIT MISS | FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied | `[BACKTRACK MISS | FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN | FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies N = sum | `[RECON MISS | FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing entry | `[SE MISS: trigger-name | FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade columns | `[MAP MISS | FM-25]` | 6 |

*FM-21 is self-referential: any violation marker without an FM code is itself an FM-21 violation.*

---

**--- PHASE-BOUNDARY DEFECT CLASSES ---**

*Structural independence note: FM-16 (Entry Condition Absent) and FM-17 (Gate Register Drift) are structurally non-overlapping failure modes that require separate FM IDs. The distinction reflects an independently driftable defect surface:*

*FM-16 alone: A phase has no entry condition at all. There is nothing to evaluate for register quality -- the defect is presence, not quality.*

*FM-17 alone: A phase has an entry condition, but it is stated descriptively ("Phase N begins when [condition is true]") rather than with formal obligation language ("Phase N SHALL begin when [condition]"). The condition exists -- its register is wrong.*

*Both simultaneously: No entry condition is present, and if one were present, the document's register pattern indicates it would be descriptively worded.*

*A single FM ID would conflate these cases. A reviewer scanning `[FM-16: Phase 3]` could not determine whether the condition was absent or present-but-informal without reading the phase body. Separate IDs make inline tags independently informative -- the tag alone conveys the structural fact.*

| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N | FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate | FM-17]` | All phases |

---

#### Entry Schema Contract

**FIRING ENTRY** (all slots required):

    Trigger Name:
    Flow Type:
    Execution Tier:     [sync | async | scheduled]
    Trigger Event:
    Input Fields:
    Output Action:
    Side Effects:       [field writes beyond primary output, or "none"]
    Condition (Taken):
    Condition (Skipped):
    Anomaly Flag:       [none | storm | missing | circular]

**NON-FIRING ENTRY** (all slots required):

    Trigger Name:
    Flow Type:
    Reason Not Firing:
    Condition (Taken):
    Condition (Skipped):

---

### STRUCTURAL INVARIANT LAYER

*Distinct from the PROTOCOL PREAMBLE. Cross-phase structural obligations applying to all phases simultaneously.*

**Invariant 1:** Every phase body SHALL contain all three control artifacts: entry condition, job description, and exit condition.

**Invariant 2:** All gate statements (entry conditions and exit conditions) in phase bodies SHALL use formal obligation language (SHALL/MUST) in the obligation position. Descriptive state language in gate positions is a register drift defect.

**Invariant 3:** The LIFECYCLE OVERVIEW table entry-condition and exit-condition cells SHALL use formal obligation language (SHALL/MUST). Cells using descriptive state language SHALL be tagged `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N | FM-17]`.

**Invariant 4:** Every inline violation marker SHALL include its FM catalog code.

**Invariant 5:** Candidate count N declared in Phase 1 SHALL be reconciled after enumeration: firing + non-firing + unresolved SHALL equal N.

---

### LIFECYCLE OVERVIEW

*This table lists all phases with entry condition, job description, and exit condition. LIFECYCLE OVERVIEW gate cells SHALL use formal obligation language (SHALL/MUST). Cells using descriptive state language SHALL be tagged `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N | FM-17]`.*

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 1 | Pre-scan | Phase 1 SHALL begin when: input received and PREAMBLE declared | Identify all candidates; declare N; open anomaly slots; issue PCC-1 | Phase 1 SHALL be declared complete when: N declared, anomaly slots OPEN, PCC-1 issued |
| 2 | Sync Trigger Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued | Enumerate sync-tier candidates with full schema; include negative vocabulary example | Phase 2 SHALL be declared complete when: all sync-tier candidates have resolved entries |
| 3 | Async Trigger Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate async-tier candidates with schema; annotate latency tier | Phase 3 SHALL be declared complete when: all async-tier candidates have resolved entries |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both tables produced | Trace cascade chains; assign chain IDs; back-edge detection | Phase 4 SHALL be declared complete when: all side-effect writes evaluated, all chains carry Chain-Status |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete and chains resolved | Deliver evidence-anchored verdicts for three anomaly classes; remediate confirmed anomalies | Phase 5 SHALL be declared complete when: all three verdicts issued with evidence |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and anomaly verdicts issued | Produce trigger map; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map complete and denominator arithmetic stated |

---

### Phase 1 -- Pre-scan

**Entry condition:** Phase 1 SHALL begin when the input record change specification has been received and the PROTOCOL PREAMBLE has been declared complete.

**Job:** Identify all candidate triggers without filtering; declare denominator N; open all three anomaly question slots; issue PCC-1.

**Anomaly Questions -- Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does any single change cause more triggers than operational capacity allows? | OPEN |
| Missing Trigger | Is an expected automation absent from the trigger surface? | OPEN |
| Circular Trigger | Does any trigger output re-activate the same or upstream trigger? | OPEN |

**Denominator Pre-Scan:** | Candidate Trigger | Flow Type | Activation Condition | Tier |

Total candidate count N = *[integer]*

**Exit condition:** Phase 1 SHALL be declared complete when N is declared, all three anomaly slots are OPEN, and PCC-1 is issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued.

**Job:** Enumerate all sync-tier candidates with schema. Include negative vocabulary example. Order by priority.

**Negative vocabulary example:** `[VOCAB FAIL: "plugin" -> Dataverse plug-in | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be declared complete when all sync-tier candidates have resolved entries with all schema slots populated.

---

### Phase 3 -- Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when Phase 2 is complete and the Sync Trigger Table is produced.

**Job:** Enumerate all async-tier candidates with schema. Annotate latency tier per entry.

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be declared complete when all async-tier candidates have resolved entries.

---

### Phase 4 -- Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when Phase 2 and Phase 3 are complete and both trigger tables are produced.

**Job:** Trace cascade chains until no further triggers fire. Assign chain IDs. Mark [TERMINAL] per chain. Apply back-edge detection.

**Cascade Chain Table:**

| Chain ID | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|------|--------------------|--------------------|---------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be declared complete when all side-effect writes are evaluated, all chains carry Chain-Status, and back-edge detection is complete.

---

### Phase 5 -- Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when Phase 4 is complete and cascade chains are resolved.

**Job:** Deliver evidence-anchored verdicts for all three anomaly classes. Cite evidence. Remediate confirmed anomalies.

**Trigger Storm:** Evidence: | Verdict: | Remediation:

**Missing Trigger:** Evidence: | Verdict: | Remediation:

**Circular Trigger:** Evidence: | Verdict: | Remediation:

**Exit condition:** Phase 5 SHALL be declared complete when all three verdicts are issued with evidence and confirmed anomalies have remediation steps.

---

### Phase 6 -- Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when Phase 5 is complete and anomaly verdicts are issued.

**Job:** Produce trigger map with tier and Spawns columns. Perform denominator closure.

**Trigger Map:**

| # | Trigger Name | Execution Tier | Anomaly Flag | Spawns |
|---|-------------|---------------|-------------|--------|

**Denominator Closure:** firing + non-firing + unresolved = N -> CLOSED / GAP DETECTED

**Exit condition:** Phase 6 SHALL be declared complete when trigger map covers all triggers and denominator closure is stated.

---
---

## V-03

**Variation axis:** LIFECYCLE OVERVIEW -- FORMAL-GATE ZONE DECLARATION as numbered code block (C-36 only)
**Hypothesis:** Converting the LIFECYCLE OVERVIEW gate-zone declaration from a prose instruction to a numbered code block with 4+ rules makes each constraint independently addressable and mechanically auditable. A reader can check each rule individually without interpreting prose intent.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A record change has occurred. Your task: determine exactly which automations fire, in what order, with what inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular triggers).

Execute the following phases in strict sequence. Each phase SHALL complete before the next begins.

---

### PROTOCOL PREAMBLE

#### Platform Term Contract

Approved vocabulary:

| Approved Term | Prohibited Substitutions |
|--------------|-------------------------|
| automated cloud flow | workflow, automation, rule |
| instant cloud flow | manual flow, button flow |
| scheduled cloud flow | recurring flow, timer flow |
| Dataverse plug-in | plugin, CRM plugin |
| sync plug-in step | synchronous plugin |
| async plug-in step | asynchronous plugin |
| trigger event: When a row is added, modified or deleted | record trigger, update trigger |
| Power Automate connector | connector trigger |

Deviations SHALL be tagged `[VOCAB FAIL: "actual text" -> correction | FM-08]`.

#### FM Catalog

| FM Code | Failure Mode | Expected Behavior | Output Marker | Phase(s) |
|---------|-------------|-------------------|---------------|----------|
| FM-01 | Trigger omission | Every bound trigger listed | `[OMIT: trigger-name | FM-01]` | 2, 3 |
| FM-02 | Firing order violation | Sync before async; by priority within tier | `[ORDER FAIL: actual | FM-02]` | 2, 3 |
| FM-03 | Missing input/output specification | Named input payload and output action | `[IO FAIL: trigger-name | FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three classes addressed | `[PATH MISS: class | FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name | FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced to terminal | `[CASCADE SHALLOW | FM-06]` | 4 |
| FM-07 | Missing conditional branch | Both branches stated | `[BRANCH MISS: trigger-name | FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used | `[VOCAB FAIL: "actual" -> correction | FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with mitigation | `[RISK MISS | FM-09]` | 5 |
| FM-10 | Missing timing annotation | Latency noted per trigger | `[TIMING MISS: trigger-name | FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct pair | `[NEG MISS | FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence | `[INSUFFICIENT: evidence needed | FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition per chain | `[CHAIN OPEN: CH-NN | FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger | `[GRAPH MISS | FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before filtering | `[DENOM MISS | FM-15]` | 1 |
| FM-16 | Entry Condition Absent | Phase has no entry precondition | `[ENTRY CONDITION ABSENT: Phase N | FM-16]` | All |
| FM-17 | Gate Register Drift | Gate statement uses descriptive language where SHALL/MUST required | `[GATE REGISTER DRIFT: Phase N gate | FM-17]` | All |
| FM-18 | No sync/async structural split | Sync and async in separate phases | `[SPLIT MISS | FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied | `[BACKTRACK MISS | FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN | FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies N = sum | `[RECON MISS | FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing entry | `[SE MISS: trigger-name | FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade columns | `[MAP MISS | FM-25]` | 6 |

**PHASE-BOUNDARY DEFECT CLASSES**

| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N | FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate | FM-17]` | All phases |

#### Entry Schema Contract

**FIRING ENTRY** (all slots required):

    Trigger Name:
    Flow Type:
    Execution Tier:     [sync | async | scheduled]
    Trigger Event:
    Input Fields:
    Output Action:
    Side Effects:       [field writes beyond primary output, or "none"]
    Condition (Taken):
    Condition (Skipped):
    Anomaly Flag:       [none | storm | missing | circular]

**NON-FIRING ENTRY** (all slots required):

    Trigger Name:
    Flow Type:
    Reason Not Firing:
    Condition (Taken):
    Condition (Skipped):

---

### STRUCTURAL INVARIANT LAYER

*Distinct from the PROTOCOL PREAMBLE. Cross-phase structural obligations applying to all phases simultaneously.*

**Invariant 1:** Every phase body SHALL contain all three control artifacts: entry condition, job description, and exit condition.

**Invariant 2:** All gate statements SHALL use formal obligation language (SHALL/MUST) in the obligation position. Descriptive gate language is a register drift defect.

**Invariant 3:** The LIFECYCLE OVERVIEW table gate cells SHALL satisfy the same formal-register requirement as phase-body gate statements.

**Invariant 4:** Every inline violation marker SHALL include its FM catalog code.

**Invariant 5:** Candidate count N declared in Phase 1 SHALL be reconciled after enumeration.

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- LIFECYCLE OVERVIEW TABLE

Rule 1 (Governing authority): This DECLARATION governs all entry-condition and
exit-condition cells in the LIFECYCLE OVERVIEW table below. It operates
independently of phase-body gate statement specifications.

Rule 2 (Register requirement): All entry-condition and exit-condition cells in
this table SHALL use formal obligation language (SHALL/MUST) in the obligation
position. A cell stating "Phase N begins when [condition]" without an obligation
verb is non-conforming under this Rule.

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
| 1 | Pre-scan | Phase 1 SHALL begin when: input received and PREAMBLE declared | Identify all candidates; declare N; open anomaly slots; issue PCC-1 | Phase 1 SHALL be declared complete when: N declared, anomaly slots OPEN, PCC-1 issued |
| 2 | Sync Trigger Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued | Enumerate sync-tier candidates with full schema; include negative vocabulary example | Phase 2 SHALL be declared complete when: all sync-tier candidates have resolved entries |
| 3 | Async Trigger Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate async-tier candidates with schema; annotate latency tier | Phase 3 SHALL be declared complete when: all async-tier candidates have resolved entries |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both tables produced | Trace cascade chains; assign chain IDs; back-edge detection | Phase 4 SHALL be declared complete when: all side-effect writes evaluated, all chains carry Chain-Status |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete and chains resolved | Deliver evidence-anchored verdicts; remediate confirmed anomalies | Phase 5 SHALL be declared complete when: all three verdicts issued with evidence |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and anomaly verdicts issued | Produce trigger map; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map complete and denominator arithmetic stated |

---

### Phase 1 -- Pre-scan

**Entry condition:** Phase 1 SHALL begin when input received and PROTOCOL PREAMBLE declared complete.

**Job:** Identify all candidates without filtering; declare N; open anomaly slots; issue PCC-1.

**Anomaly Questions -- Status: OPEN**

| Trigger Storm | OPEN | Missing Trigger | OPEN | Circular Trigger | OPEN |

Total candidate count N = *[integer]*

**Exit condition:** Phase 1 SHALL be declared complete when N declared, anomaly slots OPEN, PCC-1 issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when Phase 1 complete, N declared, PCC-1 issued.

**Job:** Enumerate sync-tier candidates with schema. Negative vocabulary example required. Order by priority.

**Negative vocabulary example:** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be declared complete when all sync-tier candidates have resolved entries with all slots populated.

---

### Phase 3 -- Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when Phase 2 complete and Sync Trigger Table produced.

**Job:** Enumerate async-tier candidates. Annotate latency tier per entry.

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be declared complete when all async-tier candidates have resolved entries.

---

### Phase 4 -- Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when Phase 2 and Phase 3 complete and both tables produced.

**Job:** Trace cascade chains until no further triggers fire. Assign chain IDs. Mark [TERMINAL]. Apply back-edge detection.

**Cascade Chain Table:**

| Chain ID | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|------|--------------------|--------------------|---------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be declared complete when all side-effect writes evaluated, all chains carry Chain-Status, back-edge detection complete.

---

### Phase 5 -- Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when Phase 4 complete and chains resolved.

**Job:** Deliver evidence-anchored verdicts for trigger storm, missing trigger, circular trigger. Remediate confirmed anomalies.

**Trigger Storm:** Evidence: | Verdict: | Remediation:
**Missing Trigger:** Evidence: | Verdict: | Remediation:
**Circular Trigger:** Evidence: | Verdict: | Remediation:

**Exit condition:** Phase 5 SHALL be declared complete when all three verdicts issued with evidence and confirmed anomalies have remediations.

---

### Phase 6 -- Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when Phase 5 complete and anomaly verdicts issued.

**Job:** Produce trigger map. Perform denominator closure.

**Trigger Map:**

| # | Trigger Name | Execution Tier | Anomaly Flag | Spawns |
|---|-------------|---------------|-------------|--------|

**Denominator Closure:** firing + non-firing + unresolved = N -> CLOSED / GAP DETECTED

**Exit condition:** Phase 6 SHALL be declared complete when trigger map covers all triggers and denominator closure is stated.

---
---

## V-04

**Variation axis:** INVARIANT LAYER -- explicit LIFECYCLE OVERVIEW governing invariant (C-37 only)
**Hypothesis:** When an invariant in the INVARIANT LAYER explicitly names the LIFECYCLE OVERVIEW gate cells as governed by the cross-phase formal-register obligation, the three gate-register surfaces (phase bodies, overview cells, invariant layer) are cross-linked from a single pre-Phase-1 declaration. A reader checking the INVARIANT LAYER can confirm all three surfaces are governed without consulting the LIFECYCLE OVERVIEW separately.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A record change has occurred. Your task: determine exactly which automations fire, in what order, with what inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular triggers).

Execute the following phases in strict sequence. Each phase SHALL complete before the next begins.

---

### PROTOCOL PREAMBLE

#### Platform Term Contract

Approved vocabulary:

| Approved Term | Prohibited Substitutions |
|--------------|-------------------------|
| automated cloud flow | workflow, automation, rule |
| instant cloud flow | manual flow, button flow |
| scheduled cloud flow | recurring flow, timer flow |
| Dataverse plug-in | plugin, CRM plugin |
| sync plug-in step | synchronous plugin |
| async plug-in step | asynchronous plugin |
| trigger event: When a row is added, modified or deleted | record trigger, update trigger |
| Power Automate connector | connector trigger |

Deviations SHALL be tagged `[VOCAB FAIL: "actual text" -> correction | FM-08]`.

#### FM Catalog

| FM Code | Failure Mode | Expected Behavior | Output Marker | Phase(s) |
|---------|-------------|-------------------|---------------|----------|
| FM-01 | Trigger omission | Every bound trigger listed | `[OMIT: trigger-name | FM-01]` | 2, 3 |
| FM-02 | Firing order violation | Sync before async; by priority within tier | `[ORDER FAIL: actual | FM-02]` | 2, 3 |
| FM-03 | Missing input/output specification | Named input payload and output action | `[IO FAIL: trigger-name | FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three classes addressed | `[PATH MISS: class | FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name | FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced to terminal | `[CASCADE SHALLOW | FM-06]` | 4 |
| FM-07 | Missing conditional branch | Both branches stated | `[BRANCH MISS: trigger-name | FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used | `[VOCAB FAIL: "actual" -> correction | FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with mitigation | `[RISK MISS | FM-09]` | 5 |
| FM-10 | Missing timing annotation | Latency noted per trigger | `[TIMING MISS: trigger-name | FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct pair | `[NEG MISS | FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence | `[INSUFFICIENT: evidence needed | FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition per chain | `[CHAIN OPEN: CH-NN | FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger | `[GRAPH MISS | FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before filtering | `[DENOM MISS | FM-15]` | 1 |
| FM-16 | Entry Condition Absent | Phase has no entry precondition | `[ENTRY CONDITION ABSENT: Phase N | FM-16]` | All |
| FM-17 | Gate Register Drift | Gate statement uses descriptive language where SHALL/MUST required | `[GATE REGISTER DRIFT: Phase N gate | FM-17]` | All |
| FM-18 | No sync/async structural split | Sync and async in separate phases | `[SPLIT MISS | FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied | `[BACKTRACK MISS | FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN | FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies N = sum | `[RECON MISS | FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing entry | `[SE MISS: trigger-name | FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade columns | `[MAP MISS | FM-25]` | 6 |

**PHASE-BOUNDARY DEFECT CLASSES**

| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N | FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate | FM-17]` | All phases |

#### Entry Schema Contract

**FIRING ENTRY** (all slots required):

    Trigger Name:
    Flow Type:
    Execution Tier:     [sync | async | scheduled]
    Trigger Event:
    Input Fields:
    Output Action:
    Side Effects:       [field writes beyond primary output, or "none"]
    Condition (Taken):
    Condition (Skipped):
    Anomaly Flag:       [none | storm | missing | circular]

**NON-FIRING ENTRY** (all slots required):

    Trigger Name:
    Flow Type:
    Reason Not Firing:
    Condition (Taken):
    Condition (Skipped):

---

### STRUCTURAL INVARIANT LAYER

*Distinct from the PROTOCOL PREAMBLE. These are cross-phase structural obligations applying to all phases and all gate-language artifact surfaces simultaneously. Invariant 4 cross-links the INVARIANT LAYER authority to the LIFECYCLE OVERVIEW table.*

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control artifacts: entry condition, job description, and exit condition. A phase body missing any artifact is a structural defect.

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements (entry conditions and exit conditions) in phase bodies SHALL use formal obligation language (SHALL/MUST) in the obligation position. Descriptive state language in gate positions is a register drift defect tagged `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.

**Invariant 3 -- FM code completeness:** Every inline violation marker SHALL include its FM catalog code. A marker without an FM code is tagged `[FM-21]`.

**Invariant 4 -- LIFECYCLE OVERVIEW gate-cell register:** The LIFECYCLE OVERVIEW table entry-condition and exit-condition cells are governed by this INVARIANT LAYER and SHALL satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). The LIFECYCLE OVERVIEW table is NOT exempt from Invariant 2 by virtue of its summary function. A reader verifying Invariant 2 SHALL verify both phase-body gate statements AND LIFECYCLE OVERVIEW gate cells -- partial compliance (phase bodies formal, overview cells descriptive) fails Invariant 2. Any LIFECYCLE OVERVIEW gate cell using descriptive state language SHALL be tagged `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.

**Invariant 5 -- Denominator closure:** Candidate count N declared in Phase 1 SHALL be reconciled after enumeration: firing + non-firing + unresolved SHALL equal N.

---

### LIFECYCLE OVERVIEW

*This table lists all phases with entry condition, job description, and exit condition. Per Invariant 4 of the STRUCTURAL INVARIANT LAYER above, entry-condition and exit-condition cells in this table SHALL use formal obligation language (SHALL/MUST). Cells using descriptive state language SHALL be tagged `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N | FM-17]`.*

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 1 | Pre-scan | Phase 1 SHALL begin when: input received and PREAMBLE declared | Identify all candidates; declare N; open anomaly slots; issue PCC-1 | Phase 1 SHALL be declared complete when: N declared, anomaly slots OPEN, PCC-1 issued |
| 2 | Sync Trigger Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued | Enumerate sync-tier candidates with full schema; include negative vocabulary example | Phase 2 SHALL be declared complete when: all sync-tier candidates have resolved entries |
| 3 | Async Trigger Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate async-tier candidates with schema; annotate latency tier | Phase 3 SHALL be declared complete when: all async-tier candidates have resolved entries |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both tables produced | Trace cascade chains; assign chain IDs; back-edge detection | Phase 4 SHALL be declared complete when: all side-effect writes evaluated, all chains carry Chain-Status |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete and chains resolved | Deliver evidence-anchored verdicts; remediate confirmed anomalies | Phase 5 SHALL be declared complete when: all three verdicts issued with evidence |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and anomaly verdicts issued | Produce trigger map; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map complete and denominator arithmetic stated |

---

### Phase 1 -- Pre-scan

**Entry condition:** Phase 1 SHALL begin when input received and PROTOCOL PREAMBLE declared complete.

**Job:** Identify all candidates without filtering; declare N; open anomaly slots; issue PCC-1.

**Anomaly Questions -- Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does any single change cause more triggers than operational capacity allows? | OPEN |
| Missing Trigger | Is an expected automation absent from the trigger surface? | OPEN |
| Circular Trigger | Does any trigger output re-activate the same or upstream trigger? | OPEN |

Total candidate count N = *[integer]*

**Exit condition:** Phase 1 SHALL be declared complete when N declared, anomaly slots OPEN, PCC-1 issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when Phase 1 complete, N declared, PCC-1 issued.

**Job:** Enumerate sync-tier candidates with schema. Include negative vocabulary example. Order by priority.

**Negative vocabulary example:** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be declared complete when all sync-tier candidates have resolved entries with all slots populated.

---

### Phase 3 -- Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when Phase 2 complete and Sync Trigger Table produced.

**Job:** Enumerate async-tier candidates with schema. Annotate latency tier per entry.

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be declared complete when all async-tier candidates have resolved entries.

---

### Phase 4 -- Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when Phase 2 and Phase 3 complete and both tables produced.

**Job:** Trace cascade chains until no further triggers fire. Assign chain IDs. Mark [TERMINAL]. Apply back-edge detection.

**Cascade Chain Table:**

| Chain ID | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|------|--------------------|--------------------|---------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be declared complete when all side-effect writes evaluated, all chains carry Chain-Status, back-edge detection complete.

---

### Phase 5 -- Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when Phase 4 complete and chains resolved.

**Job:** Deliver evidence-anchored verdicts for all three anomaly classes. Cite evidence. Remediate confirmed anomalies.

**Trigger Storm:** Evidence: | Verdict: | Remediation:
**Missing Trigger:** Evidence: | Verdict: | Remediation:
**Circular Trigger:** Evidence: | Verdict: | Remediation:

**Exit condition:** Phase 5 SHALL be declared complete when all three verdicts issued with evidence and confirmed anomalies have remediations.

---

### Phase 6 -- Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when Phase 5 complete and anomaly verdicts issued.

**Job:** Produce trigger map. Perform denominator closure.

**Trigger Map:**

| # | Trigger Name | Execution Tier | Anomaly Flag | Spawns |
|---|-------------|---------------|-------------|--------|

**Denominator Closure:** firing + non-firing + unresolved = N -> CLOSED / GAP DETECTED

**Exit condition:** Phase 6 SHALL be declared complete when trigger map covers all triggers and denominator closure is stated.

---
---

## V-05

**Variation axis:** All four axes combined -- C-34 + C-35 + C-36 + C-37 simultaneously
**Hypothesis:** The full combination produces a protocol whose INVARIANT LAYER is FM-ID-anchored (C-34), whose FM catalog PHASE-BOUNDARY DEFECT CLASSES grouping is self-justifying (C-35), whose LIFECYCLE OVERVIEW gate-zone is declared in an auditable code-block format (C-36), and whose INVARIANT LAYER cross-links to the overview table gate-cell obligation (C-37). All four new surfaces are mutually cross-referencing from a single pre-Phase-1 structure.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A record change has occurred. Your task: determine exactly which automations fire, in what order, with what inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular triggers).

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
| FM-01 | Trigger omission | Every bound trigger listed by name | `[OMIT: trigger-name | FM-01]` | 2, 3 |
| FM-02 | Firing order violation | Sync before async; by priority within tier | `[ORDER FAIL: actual | FM-02]` | 2, 3 |
| FM-03 | Missing input/output specification | Named input payload and output action; no placeholders | `[IO FAIL: trigger-name | FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three pathology classes addressed | `[PATH MISS: class | FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name | FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced until no further triggers fire | `[CASCADE SHALLOW | FM-06]` | 4 |
| FM-07 | Missing conditional branch | Firing and skipped branch both stated | `[BRANCH MISS: trigger-name | FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used throughout | `[VOCAB FAIL: "actual" -> correction | FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with one-line mitigation | `[RISK MISS | FM-09]` | 5 |
| FM-10 | Missing timing annotation | Sync/async distinguished; latency noted | `[TIMING MISS: trigger-name | FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct vocabulary pair | `[NEG MISS | FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence; bare assertions are insufficient | `[INSUFFICIENT: evidence needed | FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition declared per chain | `[CHAIN OPEN: CH-NN | FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger constructed | `[GRAPH MISS | FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before condition filtering | `[DENOM MISS | FM-15]` | 1 |
| FM-18 | No sync/async structural split | Sync and async triggers in separate enumeration phases | `[SPLIT MISS | FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied to adjacency structure | `[BACKTRACK MISS | FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each cascade chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN | FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every violation marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies firing + non-firing + unresolved = N | `[RECON MISS | FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing trigger entry | `[SE MISS: trigger-name | FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade-link columns | `[MAP MISS | FM-25]` | 6 |

*FM-21 is the self-referential entry: any violation marker appearing without an FM code is itself an FM-21 violation.*

---

**--- PHASE-BOUNDARY DEFECT CLASSES ---**

*Structural independence note: FM-16 (Entry Condition Absent) and FM-17 (Gate Register Drift) are structurally non-overlapping failure modes that require separate FM IDs. The distinction reflects an independently driftable defect surface:*

*FM-16 alone: A phase has no entry condition at all. There is nothing to evaluate for register quality -- the defect is presence, not quality. Inline tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.*

*FM-17 alone: A phase has an entry condition, but it is stated descriptively ("Phase N begins when [condition is true]") rather than with formal obligation language ("Phase N SHALL begin when [condition]"). The condition exists -- its register is wrong. Inline tag: `[GATE REGISTER DRIFT: Phase N entry | FM-17]`.*

*Both simultaneously: No entry condition is present AND, were one present, the document's register pattern indicates it would be descriptively worded. Both tags apply.*

*A single FM ID would conflate these three cases. A reviewer scanning `[FM-16: Phase 3]` could not determine without reading the phase body whether the condition was absent or present-but-informal. Separate IDs make inline tags independently informative -- the tag alone conveys the structural fact.*

| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N | FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement (entry or exit condition) uses descriptive state language where a formal obligation verb (SHALL/MUST) is required | `[GATE REGISTER DRIFT: Phase N gate | FM-17]` | All phases |

---

#### Entry Schema Contract

All trigger entries SHALL conform to one of the following schemas. A slot left blank is a schema violation.

**FIRING ENTRY** (all slots required):

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

**NON-FIRING ENTRY** (all slots required):

    Trigger Name:
    Flow Type:
    Reason Not Firing:  [specific condition excluding this trigger]
    Condition (Taken):  [what would cause this trigger to fire -- not met in this scenario]
    Condition (Skipped):[what IS true in this scenario that blocks this trigger]

---

### STRUCTURAL INVARIANT LAYER

*This section is distinct from the PROTOCOL PREAMBLE. The PREAMBLE declares vocabulary, FM catalog, and schema contracts. This INVARIANT LAYER declares cross-phase structural obligations that hold simultaneously across all phases and all gate-language artifact surfaces. Each invariant cites the FM catalog ID whose inline tag signals a violation -- making violation tagging self-evident from the invariant text without requiring FM catalog lookup.*

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control artifacts: entry condition, job description, and exit condition. A phase body missing any of the three artifacts is a structural defect. **Violation taggable as: missing entry condition -> `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements (entry conditions and exit conditions) in phase bodies throughout this protocol SHALL use formal obligation language (SHALL/MUST) in the obligation position. A gate statement using descriptive state language ("Phase N is complete when [state]" without an obligation verb) is a register drift defect. **Violation taggable as: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- LIFECYCLE OVERVIEW gate-cell register:** The LIFECYCLE OVERVIEW table entry-condition and exit-condition cells are governed by this INVARIANT LAYER and SHALL satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). The LIFECYCLE OVERVIEW is NOT exempt from Invariant 2 by virtue of its summary function. A reader verifying Invariant 2 SHALL check both phase-body gate statements AND LIFECYCLE OVERVIEW gate cells. Partial compliance (phase bodies formal, overview cells descriptive) fails Invariant 2. **Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker appearing in the output SHALL include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** The candidate trigger count N declared in Phase 1 SHALL be reconciled after Phase 3 completes: firing + non-firing + unresolved SHALL equal N. **Violation taggable as: `[RECON MISS | FM-22]`.**

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- LIFECYCLE OVERVIEW TABLE

Rule 1 (Governing authority): This DECLARATION governs all entry-condition and
exit-condition cells in the LIFECYCLE OVERVIEW table below. The STRUCTURAL
INVARIANT LAYER (Invariant 3) also governs these cells; this DECLARATION and
Invariant 3 are co-authoritative. Phase-body gate statements are governed by
their respective phase-body specifications.

Rule 2 (Register requirement): All entry-condition and exit-condition cells in
this table SHALL use formal obligation language (SHALL/MUST) in the obligation
position. A cell stating "Phase N begins when [condition]" without an obligation
verb is non-conforming under this Rule and under Invariant 3.

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
| 1 | Pre-scan | Phase 1 SHALL begin when: input record change specification received and PROTOCOL PREAMBLE declared complete | Identify all candidate triggers without filtering; declare denominator N; open all three anomaly question slots OPEN; issue Phrasing Clearance PCC-1 | Phase 1 SHALL be declared complete when: N is declared, all three anomaly slots are explicitly OPEN, and PCC-1 is issued |
| 2 | Sync Trigger Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued; if PCC-1 is absent Phase 2 SHALL NOT execute `[ENTRY CONDITION ABSENT: Phase 2 | FM-16]` | Enumerate all sync-tier candidates using FIRING ENTRY or NON-FIRING ENTRY schema; include negative vocabulary example; order by priority | Phase 2 SHALL be declared complete when: all sync-tier candidates have resolved entries with all schema slots populated and no blank slots remain |
| 3 | Async Trigger Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate all async-tier candidates using schema; annotate latency tier (near-real-time/standard/batch) per entry | Phase 3 SHALL be declared complete when: all async-tier candidates have resolved entries with all schema slots populated |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both trigger tables produced | Trace all cascade chains from side-effect field writes to terminal; assign chain IDs; apply back-edge detection | Phase 4 SHALL be declared complete when: all side-effect writes from Phases 2-3 evaluated, all chains carry Chain-Status, back-edge detection applied |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete and all cascade chains carry Chain-Status | Deliver evidence-anchored verdicts for trigger storm, missing trigger, circular trigger; propose remediation for each confirmed anomaly | Phase 5 SHALL be declared complete when: all three anomaly class verdicts issued with cited evidence and every confirmed anomaly has at least one remediation step |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and all anomaly verdicts issued | Produce trigger map with execution-tier and Spawns columns; perform denominator closure: firing + non-firing + unresolved = N | Phase 6 SHALL be declared complete when: trigger map covers all triggers with all required columns and denominator closure is stated with CLOSED or GAP DETECTED result |

---

### Phase 1 -- Pre-scan

**Entry condition:** Phase 1 SHALL begin when the input record change specification has been received and the PROTOCOL PREAMBLE has been declared complete.

**Job:** Phase 1 SHALL perform three operations before any trigger enumeration begins: (1) identify all candidate triggers without condition filtering and declare denominator N; (2) open all three anomaly question slots with explicit OPEN status; (3) scan this protocol for phrasing register violations and issue Phrasing Clearance PCC-1 if zero violations found.

**Anomaly Questions -- Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does any single field/event change cause more triggers to fire than the scenario's operational capacity can absorb? | OPEN |
| Missing Trigger | Is there an expected automation for this change that does not appear in the trigger surface? | OPEN |
| Circular Trigger | Does any trigger's output create a field write that re-activates the same or an upstream trigger? | OPEN |

**Denominator Pre-Scan:**

| Candidate Trigger | Flow Type | Activation Condition | Tier |
|------------------|-----------|---------------------|------|
| *[enumerate all candidates -- no filtering yet]* | | | |

Total candidate count N = *[integer -- declare before Phase 2 begins]*

**Exit condition:** Phase 1 SHALL be declared complete when: N is declared, all three anomaly question slots are explicitly marked OPEN, and PCC-1 is issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when: Phase 1 is complete, N is declared, and PCC-1 is issued. If PCC-1 is absent, Phase 2 SHALL NOT execute `[ENTRY CONDITION ABSENT: Phase 2 | FM-16]`.

**Job:** Phase 2 SHALL enumerate all synchronous triggers. Every sync-tier candidate from Phase 1 SHALL resolve to a FIRING ENTRY or NON-FIRING ENTRY. No candidate SHALL be omitted without a NON-FIRING ENTRY. At least one negative vocabulary example SHALL be included using `[VOCAB FAIL]` to demonstrate enforcement. [FM-11] Order by execution priority, highest first. [FM-02]

Sync trigger: executes within the same transaction (Dataverse sync plug-in step pre/post-operation; synchronous automated cloud flow on Dataverse change event).

**Negative vocabulary example (required):** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

**Sync Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be declared complete when every sync-tier candidate has a resolved entry with all schema slots populated and no blank slots remain.

---

### Phase 3 -- Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when: Phase 2 is complete and the Sync Trigger Table is produced.

**Job:** Phase 3 SHALL enumerate all asynchronous triggers. Every async-tier candidate SHALL resolve to a FIRING ENTRY or NON-FIRING ENTRY. Order by connector tier, then by priority. [FM-02] Annotate latency tier (near-real-time/standard/batch) per entry. [FM-10]

Async trigger: executes outside the originating transaction (Dataverse async plug-in step; automated cloud flow with async trigger mode; Power Automate connector on Dataverse change events).

**Async Trigger Table:**

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be declared complete when every async-tier candidate has a resolved entry with all schema slots populated.

---

### Phase 4 -- Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when: Phase 2 and Phase 3 are complete and both trigger tables are produced.

**Job:** Phase 4 SHALL trace every cascade chain spawned by side-effect field writes identified in Phases 2-3. Assign chain IDs (CH-01, CH-02, ...). Termination condition: trace each chain until no further triggers fire (no depth limit). [FM-13] Mark last row of each chain [TERMINAL]. [FM-20] If last row lacks [TERMINAL], apply `[CHAIN OPEN: CH-NN | FM-13]`. Apply back-edge detection after all chains traced. [FM-19]

**Cascade Chain Table:**

| Chain ID | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|------|--------------------|--------------------|---------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be declared complete when: every side-effect field write from Phases 2-3 has been evaluated, all chains carry a Chain-Status value, and back-edge detection has been applied.

---

### Phase 5 -- Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when: Phase 4 is complete and all cascade chains carry a Chain-Status value.

**Job:** Phase 5 SHALL deliver evidence-anchored verdicts for all three anomaly classes opened in Phase 1. Each verdict SHALL cite evidence from the trigger enumeration sections (trigger name, field write, row reference, or sequence observation). Bare assertions WITHOUT evidence SHALL be marked `[INSUFFICIENT: state evidence needed | FM-12]`. Every confirmed anomaly SHALL receive at least one concrete remediation step. [FM-09]

**Trigger Storm:**
- Evidence: *[cite trigger rows or cascade steps]*
- Verdict: CONFIRMED / NOT DETECTED
- Remediation (if confirmed): *[debounce strategy, sequencing change, or scope reduction]*

**Missing Trigger:**
- Evidence: *[cite expected automation and gap in trigger surface]*
- Verdict: CONFIRMED / NOT DETECTED
- Remediation (if confirmed): *[trigger registration, condition correction, or scope extension]*

**Circular Trigger:**
- Evidence: *[cite back-edge from Phase 4 or chain adjacency]*
- Verdict: CONFIRMED / NOT DETECTED
- Remediation (if confirmed): *[cycle-break condition, flag field, or re-sequencing]*

**Exit condition:** Phase 5 SHALL be declared complete when: all three anomaly class verdicts are issued with cited evidence, and every confirmed anomaly has at least one remediation step.

---

### Phase 6 -- Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when: Phase 5 is complete and all anomaly verdicts are issued.

**Job:** Phase 6 SHALL produce the trigger map and perform the denominator closure check. The trigger map SHALL cover all triggers (firing and non-firing) with at minimum: trigger name, execution tier, anomaly flag, and Spawns column (row reference for downstream cascade trigger, or "none"). The denominator closure SHALL verify: firing entries + non-firing entries + unresolved = N (declared in Phase 1).

**Trigger Map:**

| # | Trigger Name | Execution Tier | Anomaly Flag | Spawns |
|---|-------------|---------------|-------------|--------|

**Denominator Closure:**
- N declared in Phase 1: *[value]*
- Firing entries (Phases 2+3): *[count]*
- Non-firing entries (Phases 2+3): *[count]*
- Unresolved: *[count]*
- Verification: *[firing + non-firing + unresolved = N]* -> CLOSED / GAP DETECTED `[RECON MISS | FM-22]`

**Exit condition:** Phase 6 SHALL be declared complete when: trigger map covers all triggers with all required columns, and denominator closure arithmetic is stated explicitly with result CLOSED or GAP DETECTED.
