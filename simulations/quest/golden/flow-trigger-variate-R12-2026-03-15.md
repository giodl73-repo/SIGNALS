---
skill: flow-trigger
round: 12
rubric_version: 12
new_criteria: [C-42, C-43, C-44, C-45]
date: 2026-03-15
---

# flow-trigger -- Round 12 (Rubric v12) Variations

**New criteria this round:**
- **C-42** -- Non-exemption clause generalized to any artifact surface: the clause in Invariant 3 states that a summary-function rationale does not establish a register exemption for *any* artifact surface, not just the LIFECYCLE OVERVIEW by name.
- **C-43** -- Verifier instruction includes even-when-conforming partial-compliance prevention clause: the verifier instruction explicitly names the "phase bodies formal, overview cells descriptive" scenario as a failing state, blocking the most common partial-compliance rationalization.
- **C-44** -- Three-case independence note includes tag-informativeness rationale: the three-case note explains that separate FM IDs make each tag independently informative -- a reviewer scanning a single tag can determine the complete structural fact for that defect class without further inspection.
- **C-45** -- Bidirectional cross-reference uses exact canonical artifact names in both directions: Invariant 3 names "The LIFECYCLE OVERVIEW table" (exact canonical, not positional paraphrase) and Rule 1 names "Invariant 3" (exact numbered identifier). Both directions use exact canonical forms.

**Variation axes:**

| Variation | Axis | R12 Criteria Present | Hypothesis |
|-----------|------|---------------------|------------|
| V-01 | C-38+C-39+C-40+C-41 from R11 V-04 baseline; no R12 criteria | None | Non-exemption names LIFECYCLE OVERVIEW specifically; verifier lacks partial-compliance clause; independence note is two-case only; Invariant 3 uses positional paraphrase |
| V-02 | C-42 only | C-42 | Non-exemption clause says "any artifact surface"; verifier still missing partial-compliance scenario; two-case note; Invariant 3 uses "the overview table" generic |
| V-03 | C-42 + C-44 | C-42, C-44 | Non-exemption generalized; three-case note with tag-informativeness rationale present; verifier still missing "even when conforming" clause; Rule 1 uses generic "the INVARIANT LAYER" |
| V-04 | C-42 + C-43 + C-44 without canonical names | C-42, C-43, C-44 | All three clause/rationale criteria present; Invariant 3 forward ref uses "the overview table in the LIFECYCLE OVERVIEW section" (positional paraphrase) so C-45 loop not closed |
| V-05 | All four: C-42 + C-43 + C-44 + C-45 | C-42, C-43, C-44, C-45 | Closed bidirectional loop with exact canonical names: Invariant 3 names "The LIFECYCLE OVERVIEW table"; Rule 1 names "Invariant 3"; all three clause/rationale criteria present |

**Scenario used in all variations:** A Dataverse `incident` record's `statuscode` field changes from `In Progress` (value: 2) to `Resolved` (value: 5) in a Dynamics 365 Customer Service environment.

---

## V-01

**Variation axis:** C-38+C-39+C-40+C-41 present (from R11 V-04 baseline); C-42 through C-45 absent
**Hypothesis:** Non-exemption clause names the LIFECYCLE OVERVIEW specifically ("NOT exempt...by virtue of its summary function") without the "any artifact surface" generalization that C-42 requires. Verifier instruction says "SHALL verify both surfaces" without the "even when phase bodies themselves are conforming" partial-compliance clause that C-43 requires. Independence note covers only the two standalone cases (FM-16 alone, FM-17 alone) without the simultaneous-failure case and without the tag-informativeness rationale, so C-40 and C-44 fail. Invariant 3 uses "the overview table" (generic) in the forward reference rather than the exact canonical artifact name "The LIFECYCLE OVERVIEW table," so C-45 fails in the forward direction.

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

*Structural independence note: FM-16 (Entry Condition Absent) and FM-17 (Gate Register Drift) are structurally non-overlapping failure modes requiring separate FM IDs. A single FM ID would conflate two independently driftable defect surfaces:*

*FM-16 alone: A phase has no entry condition at all. The defect is presence, not quality. Inline tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.*

*FM-17 alone: A phase has an entry condition stated descriptively. The condition exists -- its register is wrong. Inline tag: `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. FM-16 does NOT apply.*

*Separate IDs make inline tags independently informative.*

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

*This section is distinct from the PROTOCOL PREAMBLE. Each invariant cites the FM catalog ID whose inline tag signals a violation.*

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control artifacts: entry condition, job description, and exit condition. **Violation taggable as: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements in phase bodies SHALL use formal obligation language (SHALL/MUST) in the obligation position. **Violation taggable as: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- LIFECYCLE OVERVIEW gate-cell register:** The overview table entry-condition and exit-condition cells are governed by this INVARIANT LAYER and SHALL satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). The LIFECYCLE OVERVIEW is NOT exempt from Invariant 2 by virtue of its summary function. A reader verifying Invariant 2 SHALL verify both phase-body gate statements AND the overview table gate cells. **Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker SHALL include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** Candidate count N SHALL be reconciled after Phase 3: firing + non-firing + unresolved SHALL equal N. **Violation taggable as: `[RECON MISS | FM-22]`.**

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- LIFECYCLE OVERVIEW TABLE

Rule 1 (Governing authority): This DECLARATION governs all entry-condition and
exit-condition cells in the LIFECYCLE OVERVIEW table below. The STRUCTURAL
INVARIANT LAYER (Invariant 3) also governs these cells; this DECLARATION and
Invariant 3 are co-authoritative over the LIFECYCLE OVERVIEW gate cells.
Phase-body gate statements are governed by their respective phase-body
specifications and by Invariant 2.

Rule 2 (Register requirement): All entry-condition and exit-condition cells in
this table SHALL use formal obligation language (SHALL/MUST) in the obligation
position.

Rule 3 (Self-tagging requirement): Any cell using descriptive state language
SHALL be tagged [FM-17: Gate Register Drift] inline. A non-conforming untagged
cell is a double violation: FM-17 and FM-21.

Rule 4 (Independent row verification): A reader verifying this table SHALL check
each gate cell independently. Row N conformance does not imply Row N+1 conformance.
```

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 1 | Pre-scan | Phase 1 SHALL begin when: input received and PREAMBLE complete | Identify candidates; declare N; open anomaly slots OPEN; issue PCC-1 | Phase 1 SHALL be declared complete when: N declared, anomaly slots OPEN, PCC-1 issued |
| 2 | Sync Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued | Enumerate sync-tier candidates with full schema; include negative example; order by priority | Phase 2 SHALL be declared complete when: all sync-tier candidates have resolved entries |
| 3 | Async Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate async-tier candidates with schema; annotate latency tier | Phase 3 SHALL be declared complete when: all async-tier candidates have resolved entries |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both tables produced | Trace cascade chains; assign chain IDs; apply back-edge detection | Phase 4 SHALL be declared complete when: all side-effect writes evaluated, chains carry Chain-Status |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete and chains carry Chain-Status | Deliver evidence-anchored verdicts; remediate confirmed anomalies | Phase 5 SHALL be declared complete when: all three verdicts issued with evidence and remediations |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and verdicts issued | Produce trigger map with tier and Spawns columns; perform denominator closure | Phase 6 SHALL be declared complete when: map complete and denominator closure stated |

---

### Phase 1 -- Pre-scan

**Entry condition:** Phase 1 SHALL begin when the input record change specification has been received and the PROTOCOL PREAMBLE has been declared complete.

**Job:** Identify all candidate triggers without filtering; declare denominator N; open all three anomaly question slots OPEN; issue PCC-1.

**Anomaly Questions -- Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does the statuscode change from In Progress to Resolved cause more triggers than operational capacity allows? | OPEN |
| Missing Trigger | Is there an expected automation absent from the trigger surface? | OPEN |
| Circular Trigger | Does any trigger output re-activate the same or upstream trigger? | OPEN |

Total candidate count N = *[integer]*

**Exit condition:** Phase 1 SHALL be declared complete when: N declared, anomaly slots OPEN, PCC-1 issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued. If PCC-1 absent, Phase 2 SHALL NOT execute `[ENTRY CONDITION ABSENT: Phase 2 | FM-16]`.

**Job:** Enumerate all sync-tier candidates. Every candidate SHALL resolve to FIRING ENTRY or NON-FIRING ENTRY. At least one negative vocabulary example SHALL be included. [FM-11] Order by priority. [FM-02]

**Negative vocabulary example (required):** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be declared complete when every sync-tier candidate has a resolved entry with all schema slots populated.

---

### Phase 3 -- Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced.

**Job:** Enumerate all async-tier candidates. Every candidate SHALL resolve to FIRING ENTRY or NON-FIRING ENTRY. Annotate latency tier. [FM-10]

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be declared complete when every async-tier candidate has a resolved entry with all schema slots populated.

---

### Phase 4 -- Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both trigger tables produced.

**Job:** Trace every cascade chain to terminal. Assign chain IDs. Mark last row [TERMINAL]. [FM-20] Apply back-edge detection. [FM-19]

| Chain ID | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|------|--------------------|--------------------|---------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be declared complete when: all side-effect writes evaluated, chains carry Chain-Status, back-edge detection applied.

---

### Phase 5 -- Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when: Phase 4 complete and all chains carry Chain-Status.

**Job:** Deliver evidence-anchored verdicts for all three anomaly classes. Each verdict SHALL cite evidence. Confirmed anomalies SHALL receive remediation steps. [FM-09]

**Trigger Storm:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):
**Missing Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):
**Circular Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Exit condition:** Phase 5 SHALL be declared complete when: all three verdicts issued with cited evidence and confirmed anomalies have remediation steps.

---

### Phase 6 -- Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when: Phase 5 complete and anomaly verdicts issued.

**Job:** Produce trigger map with execution-tier and Spawns columns. Perform denominator closure: firing + non-firing + unresolved = N.

| # | Trigger Name | Execution Tier | Anomaly Flag | Spawns |
|---|-------------|---------------|-------------|--------|

**Denominator Closure:** firing + non-firing + unresolved = N -> CLOSED / GAP DETECTED `[RECON MISS | FM-22]`

**Exit condition:** Phase 6 SHALL be declared complete when: trigger map covers all triggers with required columns and denominator closure is stated with CLOSED or GAP DETECTED.

---
---

## V-02

**Variation axis:** C-42 only added
**Hypothesis:** Invariant 3 non-exemption clause now uses "any artifact surface" ("a summary-function rationale does NOT establish a register exemption for any artifact surface"), closing the prospective rationalization path for any future summary artifact -- not just the LIFECYCLE OVERVIEW. C-43 remains absent: verifier instruction says "SHALL verify both surfaces" without the explicit "even when phase bodies themselves are conforming" partial-compliance clause. Independence note still covers only the two standalone cases (FM-16 alone, FM-17 alone) -- no simultaneous-failure case, no tag-informativeness rationale -- so C-40 and C-44 fail. Invariant 3's forward reference to the governed artifact uses "the overview table" (generic) rather than the exact canonical name "The LIFECYCLE OVERVIEW table," so C-45 fails in the forward direction.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dataverse `incident` record's `statuscode` field has changed from `In Progress` (2) to `Resolved` (5). Your task: determine exactly which automations fire, in what order, with what inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular triggers).

Execute the following phases in strict sequence. Each phase SHALL complete before the next begins. No phase SHALL execute until all prior phases have issued their required outputs.

---

### PROTOCOL PREAMBLE

*Governing contract layer. All three declarations appear here before Phase 1.*

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

Deviations SHALL be tagged `[VOCAB FAIL: "actual text" -> correction | FM-08]`.

#### FM Catalog

| FM Code | Failure Mode | Expected Behavior | Output Marker | Phase(s) |
|---------|-------------|-------------------|---------------|----------|
| FM-01 | Trigger omission | Every bound trigger listed by name | `[OMIT: trigger-name \| FM-01]` | 2, 3 |
| FM-02 | Firing order violation | Sync before async; by priority within tier | `[ORDER FAIL: actual \| FM-02]` | 2, 3 |
| FM-03 | Missing input/output specification | Named input payload and output action | `[IO FAIL: trigger-name \| FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three pathology classes addressed | `[PATH MISS: class \| FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name \| FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced until no further triggers fire | `[CASCADE SHALLOW \| FM-06]` | 4 |
| FM-07 | Missing conditional branch | Firing and skipped branch both stated | `[BRANCH MISS: trigger-name \| FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used throughout | `[VOCAB FAIL: "actual" -> correction \| FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with one-line mitigation | `[RISK MISS \| FM-09]` | 5 |
| FM-10 | Missing timing annotation | Sync/async distinguished; latency noted | `[TIMING MISS: trigger-name \| FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct vocabulary pair | `[NEG MISS \| FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence | `[INSUFFICIENT: evidence needed \| FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition declared per chain | `[CHAIN OPEN: CH-NN \| FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger constructed | `[GRAPH MISS \| FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before condition filtering | `[DENOM MISS \| FM-15]` | 1 |
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |
| FM-18 | No sync/async structural split | Sync and async in separate enumeration phases | `[SPLIT MISS \| FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied to adjacency structure | `[BACKTRACK MISS \| FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each cascade chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN \| FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every violation marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies firing + non-firing + unresolved = N | `[RECON MISS \| FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing trigger entry | `[SE MISS: trigger-name \| FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade-link columns | `[MAP MISS \| FM-25]` | 6 |

*FM-21 is self-referential: any marker without an FM code is itself FM-21.*

---

**--- PHASE-BOUNDARY DEFECT CLASSES ---**

*Structural independence note: FM-16 (Entry Condition Absent) and FM-17 (Gate Register Drift) are structurally non-overlapping failure modes requiring separate FM IDs. A single FM ID would conflate two independently driftable defect surfaces:*

*FM-16 alone: A phase has no entry condition. The defect is presence, not quality. Register evaluation is not applicable because no condition text exists. Inline tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.*

*FM-17 alone: A phase has an entry condition but stated descriptively. Presence is satisfied; register quality fails. Inline tag: `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. FM-16 does NOT apply.*

*Separate IDs make inline tags independently informative.*

| FM Code | Defect | Description | Tag | Scope |
|---------|--------|-------------|-----|-------|
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |

---

#### Entry Schema Contract

**FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:          [automated cloud flow | instant cloud flow | Dataverse plug-in | ...]
Execution Tier:     [sync | async | scheduled]
Trigger Event:
Input Fields:       [specific named fields -- no generic placeholders]
Output Action:      [specific action -- no generic placeholders]
Side Effects:       [field writes beyond primary output, or "none"]
Condition (Taken):  [what must be true for this trigger to fire]
Condition (Skipped):[what would cause this trigger NOT to fire]
Anomaly Flag:       [none | storm | missing | circular]
```

**NON-FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:
Reason Not Firing:  [specific condition excluding this trigger]
Condition (Taken):  [what would cause this trigger to fire]
Condition (Skipped):[what blocks this trigger in this scenario]
```

---

### STRUCTURAL INVARIANT LAYER

*Distinct from PROTOCOL PREAMBLE. Cross-phase structural obligations. Each invariant cites its FM ID.*

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control artifacts: entry condition, job description, exit condition. **Violation: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements in phase bodies SHALL use formal obligation language (SHALL/MUST). **Violation: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- LIFECYCLE OVERVIEW gate-cell register:** The overview table entry-condition and exit-condition cells SHALL satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). A summary-function rationale does NOT establish a register exemption for any artifact surface. A reader verifying Invariant 2 SHALL verify both phase-body gate statements AND the overview table gate cells. **Violation: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every marker:** Every inline violation marker SHALL include its FM code. **Violation: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** N SHALL be reconciled after Phase 3: firing + non-firing + unresolved = N. **Violation: `[RECON MISS | FM-22]`.**

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- LIFECYCLE OVERVIEW TABLE

Rule 1 (Governing authority): This DECLARATION governs all entry-condition and
exit-condition cells in the LIFECYCLE OVERVIEW table below. The STRUCTURAL
INVARIANT LAYER (Invariant 3) also governs these cells; this DECLARATION and
Invariant 3 are co-authoritative over the LIFECYCLE OVERVIEW gate cells.

Rule 2 (Register requirement): All entry-condition and exit-condition cells
SHALL use formal obligation language (SHALL/MUST) in the obligation position.

Rule 3 (Self-tagging requirement): Any cell using descriptive state language
SHALL be tagged [FM-17: Gate Register Drift] inline.

Rule 4 (Independent row verification): A reader SHALL check each gate cell
independently. Row N conformance does not imply Row N+1 conformance.
```

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 1 | Pre-scan | Phase 1 SHALL begin when: input received and PREAMBLE complete | Identify candidates; declare N; open anomaly slots OPEN; issue PCC-1 | Phase 1 SHALL be declared complete when: N declared, slots OPEN, PCC-1 issued |
| 2 | Sync Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued | Enumerate sync-tier candidates; include negative example; order by priority | Phase 2 SHALL be declared complete when: all sync-tier candidates resolved |
| 3 | Async Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate async-tier candidates; annotate latency tier | Phase 3 SHALL be declared complete when: all async-tier candidates resolved |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete | Trace cascade chains; assign chain IDs; apply back-edge detection | Phase 4 SHALL be declared complete when: all side-effect writes evaluated, chains carry Chain-Status |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete and chains carry Chain-Status | Deliver evidence-anchored verdicts; remediate confirmed anomalies | Phase 5 SHALL be declared complete when: all three verdicts issued with evidence |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and verdicts issued | Produce trigger map with tier and Spawns columns; perform denominator closure | Phase 6 SHALL be declared complete when: map complete and closure stated |

---

### Phase 1 -- Pre-scan

**Entry condition:** Phase 1 SHALL begin when the input record change specification has been received and the PROTOCOL PREAMBLE has been declared complete.

**Job:** Identify all candidate triggers without filtering; declare denominator N; open anomaly slots OPEN; issue PCC-1.

**Anomaly Questions -- Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does this change cause more triggers than operational capacity allows? | OPEN |
| Missing Trigger | Is there an expected automation absent from the trigger surface? | OPEN |
| Circular Trigger | Does any trigger output re-activate the same or upstream trigger? | OPEN |

Total candidate count N = *[integer]*

**Exit condition:** Phase 1 SHALL be declared complete when: N declared, anomaly slots OPEN, PCC-1 issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued.

**Job:** Enumerate all sync-tier candidates. Every candidate SHALL resolve to FIRING ENTRY or NON-FIRING ENTRY. Include negative example. [FM-11] Order by priority. [FM-02]

**Negative vocabulary example:** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be declared complete when every sync-tier candidate has a resolved entry with all schema slots populated.

---

### Phase 3 -- Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced.

**Job:** Enumerate all async-tier candidates. Every candidate SHALL resolve to FIRING ENTRY or NON-FIRING ENTRY. Annotate latency tier. [FM-10]

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be declared complete when every async-tier candidate has a resolved entry.

---

### Phase 4 -- Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both tables produced.

**Job:** Trace every cascade chain to terminal. Assign chain IDs. Mark last row [TERMINAL]. Apply back-edge detection.

| Chain ID | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|------|--------------------|--------------------|---------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be declared complete when: all side-effect writes evaluated, chains carry Chain-Status, back-edge detection applied.

---

### Phase 5 -- Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when: Phase 4 complete and chains carry Chain-Status.

**Job:** Deliver evidence-anchored verdicts for all three anomaly classes. Cite evidence. Remediate confirmed anomalies.

**Trigger Storm:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):
**Missing Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):
**Circular Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Exit condition:** Phase 5 SHALL be declared complete when: all three verdicts issued with evidence and confirmed anomalies have remediation steps.

---

### Phase 6 -- Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when: Phase 5 complete and verdicts issued.

**Job:** Produce trigger map with execution-tier and Spawns columns. Perform denominator closure.

| # | Trigger Name | Execution Tier | Anomaly Flag | Spawns |
|---|-------------|---------------|-------------|--------|

**Denominator Closure:** firing + non-firing + unresolved = N -> CLOSED / GAP DETECTED

**Exit condition:** Phase 6 SHALL be declared complete when: trigger map complete and denominator closure stated.

---
---

## V-03

**Variation axis:** C-42 + C-44 (non-exemption generalized; three-case independence note with tag-informativeness rationale)
**Hypothesis:** C-42 present: Invariant 3 non-exemption clause says "any artifact surface." C-44 present: three-case independence note covers FM-16-alone, FM-17-alone, and both-simultaneously, including the tag-informativeness rationale ("Separate IDs make each tag independently informative: the tag alone conveys the complete structural fact for that defect class without further inspection required"). C-43 absent: verifier instruction says "SHALL verify both surfaces" without the explicit "even when phase bodies themselves are conforming" clause. C-45 absent in the forward direction: Invariant 3 uses "the overview table" rather than the exact canonical name "The LIFECYCLE OVERVIEW table." Rule 1 return direction names "Invariant 3" correctly, but the forward mismatch means C-45's canonical-name requirement is not met on both sides.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dataverse `incident` record's `statuscode` field has changed from `In Progress` (2) to `Resolved` (5). Your task: determine exactly which automations fire, in what order, with what inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular triggers).

Execute the following phases in strict sequence. Each phase SHALL complete before the next begins.

---

### PROTOCOL PREAMBLE

*Governing contract layer. All three declarations appear before Phase 1.*

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

Deviations SHALL be tagged `[VOCAB FAIL: "actual text" -> correction | FM-08]`.

#### FM Catalog

| FM Code | Failure Mode | Expected Behavior | Output Marker | Phase(s) |
|---------|-------------|-------------------|---------------|----------|
| FM-01 | Trigger omission | Every bound trigger listed by name | `[OMIT: trigger-name \| FM-01]` | 2, 3 |
| FM-02 | Firing order violation | Sync before async; by priority within tier | `[ORDER FAIL: actual \| FM-02]` | 2, 3 |
| FM-03 | Missing input/output specification | Named input payload and output action | `[IO FAIL: trigger-name \| FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three pathology classes addressed | `[PATH MISS: class \| FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name \| FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced until no further triggers fire | `[CASCADE SHALLOW \| FM-06]` | 4 |
| FM-07 | Missing conditional branch | Firing and skipped branch both stated | `[BRANCH MISS: trigger-name \| FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used throughout | `[VOCAB FAIL: "actual" -> correction \| FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with one-line mitigation | `[RISK MISS \| FM-09]` | 5 |
| FM-10 | Missing timing annotation | Sync/async distinguished; latency noted | `[TIMING MISS: trigger-name \| FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct vocabulary pair | `[NEG MISS \| FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence | `[INSUFFICIENT: evidence needed \| FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition declared per chain | `[CHAIN OPEN: CH-NN \| FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger constructed | `[GRAPH MISS \| FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before condition filtering | `[DENOM MISS \| FM-15]` | 1 |
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |
| FM-18 | No sync/async structural split | Sync and async in separate enumeration phases | `[SPLIT MISS \| FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied to adjacency structure | `[BACKTRACK MISS \| FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each cascade chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN \| FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every violation marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies firing + non-firing + unresolved = N | `[RECON MISS \| FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing trigger entry | `[SE MISS: trigger-name \| FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade-link columns | `[MAP MISS \| FM-25]` | 6 |

*FM-21 is self-referential: any marker without an FM code is itself FM-21.*

---

**--- PHASE-BOUNDARY DEFECT CLASSES ---**

*Structural independence note: FM-16 (Entry Condition Absent) and FM-17 (Gate Register Drift) are structurally non-overlapping failure modes requiring separate FM IDs. The independence covers all three intersection cases:*

*FM-16 alone: A phase has no entry condition at all. The defect is presence, not quality. Register evaluation is not applicable because no condition text exists. Inline tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. FM-17 does NOT apply.*

*FM-17 alone: A phase has an entry condition but stated descriptively rather than with formal obligation language. Presence is satisfied; only register quality fails. Inline tag: `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. FM-16 does NOT apply.*

*Both simultaneously: A phase has no entry condition AND the document's register pattern throughout indicates that a condition, if present, would also be stated descriptively. Both defects co-occur and are independently taggable with both tags: `[ENTRY CONDITION ABSENT: Phase N | FM-16]` AND `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. A single FM ID would conflate all three cases -- a reviewer scanning a single inline tag cannot determine the defect class without inspecting the phase body and surrounding context. Separate IDs make each tag independently informative: the tag alone conveys the complete structural fact for that defect class without further inspection required.*

| FM Code | Defect | Description | Tag | Scope |
|---------|--------|-------------|-----|-------|
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |

---

#### Entry Schema Contract

**FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:          [automated cloud flow | Dataverse plug-in | ...]
Execution Tier:     [sync | async | scheduled]
Trigger Event:
Input Fields:       [specific named fields]
Output Action:      [specific action]
Side Effects:       [field writes beyond primary output, or "none"]
Condition (Taken):  [what must be true for this trigger to fire]
Condition (Skipped):[what would cause this trigger NOT to fire]
Anomaly Flag:       [none | storm | missing | circular]
```

**NON-FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:
Reason Not Firing:  [specific condition excluding this trigger]
Condition (Taken):  [what would cause this trigger to fire]
Condition (Skipped):[what blocks this trigger in this scenario]
```

---

### STRUCTURAL INVARIANT LAYER

*Distinct from PROTOCOL PREAMBLE. Each invariant cites its FM ID.*

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control artifacts: entry condition, job description, exit condition. **Violation: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements in phase bodies SHALL use formal obligation language (SHALL/MUST). **Violation: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- LIFECYCLE OVERVIEW gate-cell register:** The overview table entry-condition and exit-condition cells SHALL satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). A summary-function rationale does NOT establish a register exemption for any artifact surface. A reader verifying Invariant 2 SHALL verify both phase-body gate statements AND the overview table gate cells. **Violation: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every marker:** Every inline violation marker SHALL include its FM code. **Violation: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** N SHALL be reconciled after Phase 3: firing + non-firing + unresolved = N. **Violation: `[RECON MISS | FM-22]`.**

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- LIFECYCLE OVERVIEW TABLE

Rule 1 (Governing authority): This DECLARATION governs all entry-condition and
exit-condition cells in the LIFECYCLE OVERVIEW table below. The STRUCTURAL
INVARIANT LAYER (Invariant 3) also governs these cells; this DECLARATION and
Invariant 3 are co-authoritative over these cells.

Rule 2 (Register requirement): All entry-condition and exit-condition cells
SHALL use formal obligation language (SHALL/MUST) in the obligation position.

Rule 3 (Self-tagging requirement): Any cell using descriptive state language
SHALL be tagged [FM-17: Gate Register Drift] inline.

Rule 4 (Independent row verification): A reader SHALL check each gate cell
independently. Row N conformance does not imply Row N+1 conformance.
```

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 1 | Pre-scan | Phase 1 SHALL begin when: input received and PREAMBLE complete | Identify candidates; declare N; open anomaly slots OPEN; issue PCC-1 | Phase 1 SHALL be declared complete when: N declared, slots OPEN, PCC-1 issued |
| 2 | Sync Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued | Enumerate sync-tier candidates; include negative example; order by priority | Phase 2 SHALL be declared complete when: all sync-tier candidates resolved |
| 3 | Async Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate async-tier candidates; annotate latency tier | Phase 3 SHALL be declared complete when: all async-tier candidates resolved |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete | Trace cascade chains; assign chain IDs; apply back-edge detection | Phase 4 SHALL be declared complete when: all side-effect writes evaluated, chains carry Chain-Status |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete and chains carry Chain-Status | Deliver evidence-anchored verdicts; remediate confirmed anomalies | Phase 5 SHALL be declared complete when: all three verdicts issued with evidence |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and verdicts issued | Produce trigger map; perform denominator closure | Phase 6 SHALL be declared complete when: map complete and closure stated |

---

### Phase 1 -- Pre-scan

**Entry condition:** Phase 1 SHALL begin when the input record change specification has been received and the PROTOCOL PREAMBLE has been declared complete.

**Job:** Identify all candidate triggers without filtering; declare N; open anomaly slots OPEN; issue PCC-1.

**Anomaly Questions -- Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does this change cause more triggers than operational capacity allows? | OPEN |
| Missing Trigger | Is there an expected automation absent from the trigger surface? | OPEN |
| Circular Trigger | Does any trigger output re-activate the same or upstream trigger? | OPEN |

Total candidate count N = *[integer]*

**Exit condition:** Phase 1 SHALL be declared complete when: N declared, anomaly slots OPEN, PCC-1 issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued.

**Job:** Enumerate all sync-tier candidates with full schema. Include negative example. Order by priority.

**Negative vocabulary example:** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be declared complete when all sync-tier candidates have resolved entries with all slots populated.

---

### Phase 3 -- Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced.

**Job:** Enumerate all async-tier candidates with full schema. Annotate latency tier.

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be declared complete when all async-tier candidates have resolved entries.

---

### Phase 4 -- Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both tables produced.

**Job:** Trace every cascade chain to terminal. Assign chain IDs. Mark last row [TERMINAL]. Apply back-edge detection.

| Chain ID | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|------|--------------------|--------------------|---------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be declared complete when: all side-effect writes evaluated, chains carry Chain-Status, back-edge detection applied.

---

### Phase 5 -- Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when: Phase 4 complete and chains carry Chain-Status.

**Job:** Deliver evidence-anchored verdicts for all three anomaly classes. Cite evidence. Remediate confirmed anomalies.

**Trigger Storm:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):
**Missing Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):
**Circular Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Exit condition:** Phase 5 SHALL be declared complete when: all three verdicts issued with evidence and confirmed anomalies have remediation steps.

---

### Phase 6 -- Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when: Phase 5 complete and verdicts issued.

**Job:** Produce trigger map with execution-tier and Spawns columns. Perform denominator closure.

| # | Trigger Name | Execution Tier | Anomaly Flag | Spawns |
|---|-------------|---------------|-------------|--------|

**Denominator Closure:** firing + non-firing + unresolved = N -> CLOSED / GAP DETECTED

**Exit condition:** Phase 6 SHALL be declared complete when: map complete and denominator arithmetic stated.

---
---

## V-04

**Variation axis:** C-42 + C-43 + C-44 combined; C-45 not closed (positional paraphrase in forward direction)
**Hypothesis:** All three rationale/clause criteria are present: C-42 (any artifact surface), C-43 (explicit "even when the phase bodies themselves are conforming" clause in verifier instruction), C-44 (tag-informativeness rationale in three-case note). C-45 fails because Invariant 3's forward reference uses "the overview table in the LIFECYCLE OVERVIEW section" -- a positional paraphrase rather than the exact canonical artifact name "The LIFECYCLE OVERVIEW table." Rule 1 return direction correctly names "Invariant 3" by its exact numbered identifier, but the forward direction's paraphrase prevents the C-45 canonical-name requirement from being met simultaneously on both sides.

---

You are a Power Automate / Copilot Studio trigger analysis engine.

A Dataverse `incident` record's `statuscode` field has changed from `In Progress` (2) to `Resolved` (5). Your task: determine exactly which automations fire, in what order, with what inputs and outputs, and identify all trigger pathologies (storms, missing triggers, circular triggers).

Execute the following phases in strict sequence. Each phase SHALL complete before the next begins. No phase SHALL execute until all prior phases have issued their required outputs.

---

### PROTOCOL PREAMBLE

*Governing contract layer: Platform Term Contract, FM Catalog, and Entry Schema Contract. All three appear here before Phase 1.*

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

Deviations SHALL be tagged `[VOCAB FAIL: "actual text" -> correction | FM-08]`.

#### FM Catalog

| FM Code | Failure Mode | Expected Behavior | Output Marker | Phase(s) |
|---------|-------------|-------------------|---------------|----------|
| FM-01 | Trigger omission | Every bound trigger listed by name | `[OMIT: trigger-name \| FM-01]` | 2, 3 |
| FM-02 | Firing order violation | Sync before async; by priority within tier | `[ORDER FAIL: actual \| FM-02]` | 2, 3 |
| FM-03 | Missing input/output specification | Named input payload and output action | `[IO FAIL: trigger-name \| FM-03]` | 2, 3 |
| FM-04 | Missing pathology coverage | All three pathology classes addressed | `[PATH MISS: class \| FM-04]` | 5 |
| FM-05 | False positive trigger | Only triggers scoped to this change | `[FALSE POS: trigger-name \| FM-05]` | 2, 3 |
| FM-06 | Shallow side effect trace | Cascade traced until no further triggers fire | `[CASCADE SHALLOW \| FM-06]` | 4 |
| FM-07 | Missing conditional branch | Firing and skipped branch both stated | `[BRANCH MISS: trigger-name \| FM-07]` | 2, 3 |
| FM-08 | Wrong platform vocabulary | Approved vocabulary used throughout | `[VOCAB FAIL: "actual" -> correction \| FM-08]` | All |
| FM-09 | Missing risk ranking | Pathologies ranked with one-line mitigation | `[RISK MISS \| FM-09]` | 5 |
| FM-10 | Missing timing annotation | Sync/async distinguished; latency noted | `[TIMING MISS: trigger-name \| FM-10]` | 2, 3 |
| FM-11 | Missing negative example | At least one wrong-vs-correct vocabulary pair | `[NEG MISS \| FM-11]` | 2 |
| FM-12 | Ungrounded pathology verdict | Verdict cites evidence | `[INSUFFICIENT: evidence needed \| FM-12]` | 5 |
| FM-13 | Open cascade chain | Termination condition declared per chain | `[CHAIN OPEN: CH-NN \| FM-13]` | 4 |
| FM-14 | No trigger graph | Adjacency list trigger->field->trigger constructed | `[GRAPH MISS \| FM-14]` | 5 |
| FM-15 | No denominator declaration | Count N declared before condition filtering | `[DENOM MISS \| FM-15]` | 1 |
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |
| FM-18 | No sync/async structural split | Sync and async in separate enumeration phases | `[SPLIT MISS \| FM-18]` | 2, 3 |
| FM-19 | No back-edge detection | Back-edge detection applied to adjacency structure | `[BACKTRACK MISS \| FM-19]` | 5 |
| FM-20 | Missing terminal row marker | Each cascade chain closes with [TERMINAL] | `[CHAIN OPEN: CH-NN \| FM-20]` | 4 |
| FM-21 | FM code missing from violation cell | Every violation marker includes FM code | `[FM-21]` | All |
| FM-22 | No denominator reconciliation | Closure verifies firing + non-firing + unresolved = N | `[RECON MISS \| FM-22]` | 6 |
| FM-24 | No side-effect slot | Side-effect slot in every firing trigger entry | `[SE MISS: trigger-name \| FM-24]` | 2, 3 |
| FM-25 | Missing trigger map | Trigger map with tier and cascade-link columns | `[MAP MISS \| FM-25]` | 6 |

*FM-21 is self-referential: any marker without an FM code is itself FM-21.*

---

**--- PHASE-BOUNDARY DEFECT CLASSES ---**

*Structural independence note: FM-16 (Entry Condition Absent) and FM-17 (Gate Register Drift) are structurally non-overlapping failure modes requiring separate FM IDs. The independence covers all three intersection cases in the defect space:*

*FM-16 alone: A phase has no entry condition at all. The defect is presence, not quality. Register evaluation is not applicable because no condition text exists -- there is nothing to evaluate for register quality. Inline tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. FM-17 does NOT apply.*

*FM-17 alone: A phase has an entry condition but it is stated descriptively rather than with formal obligation language. Presence is satisfied; only register quality fails. Inline tag: `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. FM-16 does NOT apply.*

*Both simultaneously: A phase has no entry condition AND the document's register pattern throughout indicates that a condition, if present, would also be stated descriptively rather than with formal obligation language. Both defects co-occur and are independently taggable with both tags: `[ENTRY CONDITION ABSENT: Phase N | FM-16]` AND `[GATE REGISTER DRIFT: Phase N entry | FM-17]`. A single FM ID would conflate all three cases -- a reviewer scanning a single inline tag cannot determine the defect class without inspecting the phase body and surrounding context. Separate IDs make each tag independently informative: the tag alone conveys the complete structural fact for that defect class without further inspection required.*

| FM Code | Defect | Description | Tag | Scope |
|---------|--------|-------------|-----|-------|
| FM-16 | Entry Condition Absent | A named phase carries no entry precondition | `[ENTRY CONDITION ABSENT: Phase N \| FM-16]` | All phases |
| FM-17 | Gate Register Drift | A gate statement uses descriptive language where SHALL/MUST is required | `[GATE REGISTER DRIFT: Phase N gate \| FM-17]` | All phases |

---

#### Entry Schema Contract

**FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:          [automated cloud flow | instant cloud flow | Dataverse plug-in | ...]
Execution Tier:     [sync | async | scheduled]
Trigger Event:
Input Fields:       [specific named fields -- no placeholders]
Output Action:      [specific action -- no placeholders]
Side Effects:       [field writes beyond primary output, or "none"]
Condition (Taken):  [what must be true for this trigger to fire]
Condition (Skipped):[what would cause this trigger NOT to fire]
Anomaly Flag:       [none | storm | missing | circular]
```

**NON-FIRING ENTRY** (all slots required):

```
Trigger Name:
Flow Type:
Reason Not Firing:  [specific condition excluding this trigger]
Condition (Taken):  [what would cause this trigger to fire -- not met]
Condition (Skipped):[what IS true in this scenario that blocks this trigger]
```

---

### STRUCTURAL INVARIANT LAYER

*Distinct from PROTOCOL PREAMBLE. Cross-phase structural obligations. Each invariant cites its FM ID -- making violation tagging self-evident without FM catalog lookup.*

**Invariant 1 -- Phase body completeness:** Every phase body SHALL contain all three control artifacts: entry condition, job description, and exit condition. **Violation taggable as: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.**

**Invariant 2 -- Gate statement formal register (phase bodies):** All gate statements in phase bodies SHALL use formal obligation language (SHALL/MUST) in the obligation position. **Violation taggable as: `[GATE REGISTER DRIFT: Phase N gate | FM-17]`.**

**Invariant 3 -- LIFECYCLE OVERVIEW gate-cell register:** The overview table in the LIFECYCLE OVERVIEW section entry-condition and exit-condition cells are governed by this INVARIANT LAYER and SHALL satisfy the same formal-register obligation as phase-body gate statements (Invariant 2). A summary-function rationale does NOT establish a register exemption for any artifact surface. A reader verifying Invariant 2 SHALL verify both phase-body gate statements AND the overview table gate cells; partial compliance (phase bodies formal, overview cells descriptive) fails Invariant 2 even when the phase bodies themselves are conforming. **Violation taggable as: `[GATE REGISTER DRIFT: LIFECYCLE OVERVIEW Phase N entry/exit | FM-17]`.**

**Invariant 4 -- FM code in every violation marker:** Every inline violation marker SHALL include its FM catalog code. **Violation taggable as: `[FM-21]`.**

**Invariant 5 -- Denominator closure:** N declared in Phase 1 SHALL be reconciled after Phase 3: firing + non-firing + unresolved SHALL equal N. **Violation taggable as: `[RECON MISS | FM-22]`.**

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION -- LIFECYCLE OVERVIEW TABLE

Rule 1 (Governing authority): This DECLARATION governs all entry-condition and
exit-condition cells in the LIFECYCLE OVERVIEW table below. The STRUCTURAL
INVARIANT LAYER (Invariant 3) also governs these cells; this DECLARATION and
Invariant 3 are co-authoritative over the LIFECYCLE OVERVIEW gate cells.
Phase-body gate statements are governed by their respective phase-body
specifications and by Invariant 2.

Rule 2 (Register requirement): All entry-condition and exit-condition cells in
this table SHALL use formal obligation language (SHALL/MUST) in the obligation
position.

Rule 3 (Self-tagging requirement): Any cell using descriptive state language
SHALL be tagged [FM-17: Gate Register Drift] inline. A non-conforming untagged
cell is a double violation: FM-17 and FM-21.

Rule 4 (Independent row verification): A reader verifying this table SHALL check
each gate cell independently. Row N conformance does not imply Row N+1 conformance.
```

| Phase | Name | Entry Condition | Job Description | Exit Condition |
|-------|------|-----------------|-----------------|----------------|
| 1 | Pre-scan | Phase 1 SHALL begin when: input received and PROTOCOL PREAMBLE complete | Identify all candidates; declare N; open anomaly slots OPEN; issue PCC-1 | Phase 1 SHALL be declared complete when: N declared, anomaly slots OPEN, PCC-1 issued |
| 2 | Sync Trigger Enumeration | Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued | Enumerate sync-tier candidates with full schema; include negative vocabulary example | Phase 2 SHALL be declared complete when: all sync-tier candidates have resolved entries |
| 3 | Async Trigger Enumeration | Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced | Enumerate async-tier candidates; annotate latency tier | Phase 3 SHALL be declared complete when: all async-tier candidates have resolved entries |
| 4 | Cascade Tracing | Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both tables produced | Trace cascade chains; assign chain IDs; apply back-edge detection | Phase 4 SHALL be declared complete when: all side-effect writes evaluated, chains carry Chain-Status |
| 5 | Anomaly Assessment | Phase 5 SHALL begin when: Phase 4 complete and chains carry Chain-Status | Deliver evidence-anchored verdicts for all three anomaly classes; remediate confirmed anomalies | Phase 5 SHALL be declared complete when: all three verdicts issued with evidence and remediations |
| 6 | Trigger Map and Closure | Phase 6 SHALL begin when: Phase 5 complete and verdicts issued | Produce trigger map with tier and Spawns columns; perform denominator closure | Phase 6 SHALL be declared complete when: trigger map complete and denominator closure stated |

---

### Phase 1 -- Pre-scan

**Entry condition:** Phase 1 SHALL begin when the input record change specification has been received and the PROTOCOL PREAMBLE has been declared complete.

**Job:** Phase 1 SHALL perform three operations before any enumeration: (1) identify all candidate triggers without filtering and declare N; (2) open all three anomaly question slots OPEN; (3) issue PCC-1.

**Anomaly Questions -- Status: OPEN**

| Anomaly Class | Question | Status |
|---------------|----------|--------|
| Trigger Storm | Does this change cause more triggers than operational capacity allows? | OPEN |
| Missing Trigger | Is there an expected automation absent from the trigger surface? | OPEN |
| Circular Trigger | Does any trigger output re-activate the same or upstream trigger? | OPEN |

Total candidate count N = *[integer]*

**Exit condition:** Phase 1 SHALL be declared complete when: N is declared, all three anomaly slots are explicitly OPEN, and PCC-1 is issued.

---

### Phase 2 -- Sync Trigger Enumeration

**Entry condition:** Phase 2 SHALL begin when: Phase 1 complete, N declared, PCC-1 issued. If PCC-1 absent, Phase 2 SHALL NOT execute `[ENTRY CONDITION ABSENT: Phase 2 | FM-16]`.

**Job:** Enumerate all sync-tier candidates. Every candidate SHALL resolve to FIRING ENTRY or NON-FIRING ENTRY. Include negative vocabulary example. Order by priority.

**Negative vocabulary example:** `[VOCAB FAIL: "workflow" -> automated cloud flow | FM-08]`

| # | Trigger Name | Flow Type | Execution Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 2 SHALL be declared complete when every sync-tier candidate has a resolved entry with all schema slots populated.

---

### Phase 3 -- Async Trigger Enumeration

**Entry condition:** Phase 3 SHALL begin when: Phase 2 complete and Sync Trigger Table produced.

**Job:** Enumerate all async-tier candidates. Every candidate SHALL resolve to FIRING ENTRY or NON-FIRING ENTRY. Annotate latency tier.

| # | Trigger Name | Flow Type | Execution Tier | Latency Tier | Trigger Event | Input Fields | Output Action | Side Effects | Condition (Taken) | Condition (Skipped) | Anomaly Flag |
|---|-------------|-----------|---------------|-------------|--------------|-------------|--------------|-------------|-------------------|---------------------|-------------|

**Exit condition:** Phase 3 SHALL be declared complete when every async-tier candidate has a resolved entry with all schema slots populated.

---

### Phase 4 -- Cascade Tracing

**Entry condition:** Phase 4 SHALL begin when: Phase 2 and Phase 3 complete and both trigger tables produced.

**Job:** Trace every cascade chain to terminal. Assign chain IDs. Mark last row [TERMINAL]. Apply back-edge detection.

| Chain ID | Step | Originating Trigger | Side-Effect Action | Field Mutated | Downstream Trigger | Chain-Status |
|----------|------|--------------------|--------------------|---------------|-------------------|-------------|

**Exit condition:** Phase 4 SHALL be declared complete when: all side-effect writes evaluated, chains carry Chain-Status, back-edge detection applied.

---

### Phase 5 -- Anomaly Assessment

**Entry condition:** Phase 5 SHALL begin when: Phase 4 complete and all chains carry Chain-Status.

**Job:** Deliver evidence-anchored verdicts for all three anomaly classes. Cite evidence. Confirmed anomalies SHALL receive remediation steps.

**Trigger Storm:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):
**Missing Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):
**Circular Trigger:** Evidence: | Verdict: CONFIRMED / NOT DETECTED | Remediation (if confirmed):

**Exit condition:** Phase 5 SHALL be declared complete when: all three verdicts issued with cited evidence and confirmed anomalies have remediation steps.

---

### Phase 6 -- Trigger Map and Closure

**Entry condition:** Phase 6 SHALL begin when: Phase 5 complete and anomaly verdicts issued.

**Job:** Produce trigger map with execution-tier and Spawns columns. Perform denominator closure.

| # | Trigger Name | Execution Tier | Anomaly Flag | Spawns |
|---|-------------|---------------|-------------|--------|

**Denominator Closure:** firing + non-firing + unresolved = N -> CLOSED / GAP DETECTED

**Exit condition:** Phase 6 SHALL be declared complete when: trigger map covers all triggers with required columns and denominator closure is stated with CLOSED or GAP DETECTED.

---
---

## V-05

**Variation axis:** All four: C-42 + C-43 + C-44 + C-45 simultaneously
**Hypothesis:** Full combination produces all four R12 criteria. C-42: Invariant 3 non-exemption clause is artifact-agnostic ("a summary-function rationale does NOT establish a register exemption for any artifact surface -- the summary or overview nature of an artifact does not confer exemption"). C-43: verifier instruction explicitly names the partial-compliance scenario: "fails Invariant 2 even when the phase bodies themselves are conforming." C-44: three-case independence note includes the tag-informativeness rationale: "Separate IDs make each tag independently informative: the tag alone conveys the complete structural fact for that defect class without further inspection required." C-45: closed bidirectional loop with exact canonical names in both directions -- Invariant 3 names "The LIFECYCLE OVERVIEW table" (exact canonical artifact name, not a positional paraphrase) and Rule 1 names "Invariant 3" (exact numbered invariant identifier).

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
