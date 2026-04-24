# flow-trigger Skill Prompt Variations -- Round 8

Generated: 2026-03-15
Rubric: v8 (C-01 through C-30, aspirational /23 pts, max 113)
New criteria targeted: C-28 (phase body self-contained), C-29 (FM catalog names entry-condition-absent), C-30 (gate statement register matches job statement register)

---

## Gap Analysis Entering Round 8

### Pre-read of R7 Scorecard Evidence (Against Rubric v7, C-01 Through C-27)

R7 established three new criteria: C-25 (per-phase entry conditions), C-26 (formal prescriptive register throughout), C-27 (LIFECYCLE OVERVIEW table precedes all phases). R7 V-05 was the full-integration variation: LIFECYCLE OVERVIEW table in the PROTOCOL PREAMBLE, bidirectional entry/exit conditions on every phase, and formal SHALL/MUST/PROHIBITED register throughout all obligation statements.

**What R7 V-05 structural features map to R8 rubric additions:**

| R7 V-05 Feature | R8 Criterion | Gap |
|-----------------|-------------|-----|
| Entry conditions appear in LIFECYCLE OVERVIEW table per phase | C-25 PASS | C-28 fails: phase bodies carry only Job + Exit condition. A reader who opens to Phase 3 body cannot confirm the entry precondition without scrolling back to the LIFECYCLE OVERVIEW. |
| FM catalog with FM-15 (Catalog Opacity) as reflexive entry | C-24 PASS | C-29 fails: no FM entry names entry-condition-absence as a defect class. Missing entry conditions are observed only by reviewer inspection, not self-tagged inline. |
| Formal register in job descriptions and slot contracts | C-26 PASS | C-30 fails: exit gate statements use "Phase N is complete when:" -- descriptive form -- while job descriptions use SHALL/MUST. Gate positions drift to descriptive register even in formally-correct protocols. |

**Consequence**: R7 V-05 would have received PARTIALs on C-28, C-29, and C-30. R8 does not re-discover R7 features -- it adds exactly what R7 V-05 left open at each phase boundary.

### R8 Variation Map

Foundation carried forward from R7 (no rediscovery needed):
- FM catalog with reflexive entry for catalog-level defects (C-24)
- Entry schema contract for FIRING and NON-FIRING entries (C-19)
- Platform vocabulary contract with VOCAB FAIL tags (C-21)
- PROTOCOL PREAMBLE unifying all three contracts (C-22)
- Phase protocol with named phases and job descriptions (C-20)
- Per-phase completion gates on all phases (C-23)
- Per-phase entry conditions declared on all phases (C-25)
- LIFECYCLE OVERVIEW table preceding all phases (C-27)
- Formal prescriptive register (SHALL/MUST/PROHIBITED) throughout (C-26)
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
| V-01 | Gate register | C-30 | Requiring all gate statements (entry conditions and exit conditions) to use SHALL/MUST in the obligation position -- "Phase N SHALL be declared complete when:" and "Phase N SHALL NOT begin until:" -- makes C-30 pass by construction. Gate positions are the drift-prone artifact type even in otherwise-formal protocols; naming the gate register explicitly compels uniformity. |
| V-02 | Phase body self-contained | C-28 | Requiring each phase body to explicitly restate all three control artifacts (entry condition, job description, exit condition) within the body itself -- independent of the LIFECYCLE OVERVIEW table -- makes C-28 pass by construction. A "PHASE BODY CONTRACT" header per phase signals that the body is self-contained and structurally forbids reliance on the LIFECYCLE OVERVIEW for control-flow context. |
| V-03 | FM catalog entry-condition-absent | C-29 | Adding FM-16 (Entry Condition Absent) to the FM catalog and instructing inline tagging of any phase body missing an entry condition as `[ENTRY CONDITION ABSENT: Phase N | FM-16]` makes C-29 pass by construction. Entry-condition absence becomes a structurally detectable defect rather than a silent gap observable only by reviewer inspection. |
| V-04 | Phase body self-contained + FM-16 | C-28 + C-29 | Phase bodies are self-contained (C-28) and FM-16 is in the catalog (C-29). The two criteria compound: C-28 compels entry conditions to appear in phase bodies; FM-16 makes their absence automatically detectable inline. A phase body that omits its entry condition is doubly penalized: it fails the "self-contained" structural check AND generates a tagged defect. |
| V-05 | Gate register + phase body self-contained + FM-16 | C-28 + C-29 + C-30 | Full integration: phase bodies carry all three control artifacts (C-28), FM-16 names entry-condition-absence (C-29), and all gate statements use SHALL/MUST in the obligation position (C-30). The LIFECYCLE OVERVIEW table itself uses formal gate register. The prompt models correct register in its own phase structure, cascading formal language into the output's phase boundaries. |

---

## V-01 -- Gate Register: Formal Obligation Language in All Gate Positions

**Variation axis**: Gate register (C-30)
**Hypothesis**: When all gate statements -- both entry conditions ("Phase N SHALL NOT begin until:") and exit conditions ("Phase N SHALL be declared complete when:") -- use formal obligation verbs in the obligation position, C-30 passes by construction. Gate positions are the artifact type most prone to descriptive drift ("Phase N is complete when:") even in protocols where job descriptions use SHALL/MUST throughout. Explicitly naming the gate form in the prompt compels register uniformity across artifact types without adding structural elements beyond R7 V-05.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. You SHALL simulate which automations fire when the following record change occurs.

**SCENARIO**

Record: Dynamics 365 Opportunity (opportunity entity)
Change: `Status` field changed from `In Progress` to `Closed Won`
Context: Change made by a sales representative via the model-driven app Opportunity form, saved by user click.

You SHALL complete this analysis using the five-phase protocol defined below. You SHALL complete each phase in full before beginning the next. You SHALL NOT merge phases. You SHALL NOT advance to a later phase before the current phase's exit condition is met.

**Gate register rule**: Every entry condition statement in this protocol SHALL use the form "Phase N SHALL NOT begin until: [precondition]". Every exit condition statement SHALL use the form "Phase N SHALL be declared complete when: [condition]". Descriptive gate form ("Phase N is complete when:" without an obligation verb) SHALL be tagged `[GATE REGISTER DRIFT: "{actual text}" -> SHALL be declared complete | FM-17]`.

---

### PROTOCOL PREAMBLE

All three contract declarations below SHALL be present before Phase 1 begins. No platform term SHALL appear before the Platform Vocabulary Contract. No FM tag SHALL appear before the FM Catalog. No entry slot SHALL be used before the Entry Schema Contract.

#### Platform Vocabulary Contract

Approved terms for this analysis (deviations SHALL be tagged `[VOCAB FAIL: {actual term} | FM-03]`):

- `sync plugin step` -- Dataverse plugin registered on the synchronous pipeline (pre-operation or post-operation, same transaction)
- `async plugin step` -- Dataverse plugin registered on the asynchronous pipeline (post-operation, separate system job)
- `automated flow` -- Power Automate flow triggered by a Dataverse record-change event
- `instant flow` -- Power Automate flow triggered manually or by another flow/app
- `scheduled flow` -- Power Automate flow triggered on a time-based recurrence
- `business rule` -- Model-driven app client-side or server-side rule evaluated on field value
- `real-time workflow` -- Legacy Dataverse synchronous workflow (deprecated but may be active)
- `classic workflow` -- Legacy Dataverse asynchronous background workflow

#### Failure Mode Catalog

Every inline FM tag in this output SHALL resolve to an entry in this catalog. An FM tag with no catalog entry SHALL be tagged `[FM-15: Catalog Opacity -- inline tag FM-NN references no catalog entry]`.

**FM-01** -- Undeclared Denominator: Enumeration begins without a declared candidate count. Correction: Phase 1 SHALL declare N before Phase 2 begins.
**FM-02** -- Silent Trigger Omission: A candidate identified in Phase 1 has no disposition in Phase 2. Correction: Every CA-NN SHALL appear as FIRING or NON-FIRING.
**FM-03** -- Vocabulary Drift: A non-approved platform term appears in the output. Tag: `[VOCAB FAIL: {term} | FM-03]`.
**FM-04** -- Branch Blindness: A trigger entry has a Condition (Taken) slot but no Condition (Skipped), or vice versa. Tag: `[BRANCH BLIND: {entry name} | FM-04]`.
**FM-05** -- Storm Evidence Gap: Storm verdict stated without citing specific trigger rows. Correction: Cite at minimum two CA-IDs and their combined fire count.
**FM-06** -- Missing-Trigger Evidence Gap: Missing trigger verdict stated without citing expected-but-absent candidates. Correction: Reference FLAGGED GAP entries.
**FM-07** -- Cycle Evidence Gap: Circular trigger verdict stated without citing the back-edge path. Correction: State `{Trigger A} -> {Field Write} -> {Trigger B} -> ... -> {Trigger A}`.
**FM-08** -- Cascade Orphan: Side-effect field write with automation potential has no downstream trigger row. Correction: Every such write SHALL spawn a trigger row.
**FM-09** -- Denominator Closure Skip: Enumeration completes without arithmetic closure check. Correction: Phase 5 SHALL verify `(FIRED + CONFIRMED ABSENT + FLAGGED GAP) = N`.
**FM-10** -- Trigger Map Incomplete: Trigger map missing execution tier or cascade link columns. Tag: `[FM-10]`.
**FM-11** -- Remediation Gap: Confirmed anomaly has no remediation guidance. Tag: `[REMEDIATION ABSENT | FM-11]`.
**FM-12** -- Entry Schema Violation: Trigger entry missing a declared schema slot. Tag: `[SLOT MISSING: {slot name} | FM-12]`.
**FM-13** -- Anomaly Gate Absent: An anomaly question is not pre-opened before Phase 2. Correction: All three SHALL be declared OPEN before the first trigger entry.
**FM-14** -- Phase Register Violation: Obligation statement in a phase body uses descriptive language instead of SHALL/MUST/PROHIBITED/MAY NOT. Tag: `[REGISTER FAIL: "{actual text}" -> SHALL/MUST | FM-14]`.
**FM-15** -- Catalog Opacity: Inline FM tag references an ID not present in this catalog. Tag: `[FM-15: Catalog Opacity]`.
**FM-16** -- Entry Condition Absent: A named phase carries no entry precondition statement. Tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`.
**FM-17** -- Gate Register Drift: A gate statement (entry or exit condition) uses descriptive form in the obligation position instead of SHALL/MUST. Tag: `[GATE REGISTER DRIFT: "{actual text}" -> SHALL be declared complete | FM-17]`.

*FM-15 and FM-16 are catalog-level and phase-structure defects respectively. FM-17 is the gate-position register defect -- it fires when gate statements pass C-26's SHALL threshold test (job descriptions use SHALL) but drift at gate positions.*

#### Entry Schema Contract

**FIRING ENTRY** -- every firing trigger entry SHALL contain all of the following slots:

```
Seq:                 [integer]
Trigger Name:        [approved vocabulary term]
CA-Ref:              [CA-NN identifier from Phase 1]
Tier:                [sync | async]
Layer:               [plugin step | automated flow | business rule | real-time workflow | classic workflow]
Condition (Taken):   [what MUST be true for this trigger to fire in this scenario]
Condition (Skipped): [what would cause this trigger NOT to fire]
Inputs:              [field/event consumed]
Outputs:             [field write / notification / record creation]
Side Effects:        [additional field writes or spawned actions; "None" if absent]
Spawns:              [CA-NN of any cascade trigger; "None" if absent]
Anomaly Flag:        [none | storm | missing | cycle | FM-NN]
```

A missing slot SHALL be marked `[SLOT MISSING: {slot name} | FM-12]`.

**NON-FIRING ENTRY** -- every non-firing candidate SHALL contain:

```
CA-Ref:              [CA-NN identifier]
Trigger Name:        [approved vocabulary term or description]
Condition (Taken):   [what would cause this trigger to fire]
Condition (Skipped): [the specific condition preventing it firing in this scenario]
Verdict:             [CONFIRMED ABSENT | FLAGGED GAP]
FM Flag:             [FM-02 if FLAGGED GAP; "none" if CONFIRMED ABSENT]
```

---

### LIFECYCLE OVERVIEW

The following table SHALL precede all phases. It states entry conditions, jobs, and exit conditions for all phases. Entry conditions use the obligation form "SHALL NOT begin until:". Exit conditions use the obligation form "SHALL be declared complete when:". Any row using descriptive gate language SHALL be tagged `[FM-17]` in the cell.

| Phase | Name | Entry condition (SHALL NOT begin until) | Job | Exit condition (SHALL be declared complete when) |
|-------|------|-----------------------------------------|-----|--------------------------------------------------|
| 1 | Candidate Pre-scan | Scenario received; PROTOCOL PREAMBLE is complete; no trigger entries written | Identify all automation candidates; declare denominator N; open all three anomaly question slots | N candidates listed; denominator stated; all three anomaly questions carry Status: OPEN |
| 2 | Trigger Enumeration | Phase 1 SHALL be declared complete; denominator N declared; anomaly slots carry Status: OPEN | Enumerate all N candidates as FIRING ENTRY or NON-FIRING ENTRY per schema; cascade side-effect writes spawn new rows | All N CA-NN candidates have a disposition; all automation-potential side-effect writes have spawned downstream rows |
| 3 | Anomaly Analysis | Phase 2 SHALL be declared complete; all candidates enumerated | Close all three anomaly question slots with evidence-cited verdicts and remediation | All three anomaly verdicts carry Status: CLOSED; each cites evidence; each confirmed anomaly has remediation |
| 4 | Trigger Map Assembly | Phase 3 SHALL be declared complete; all anomaly verdicts closed | Produce the trigger map with Seq, Trigger Name, CA-Ref, Tier, Anomaly Flag, Spawns columns | Table covers all firing triggers; all six columns populated per row |
| 5 | Denominator Closure | Phase 4 SHALL be declared complete; trigger map complete | Verify (FIRED + CONFIRMED ABSENT + FLAGGED GAP) = N arithmetic; state VERIFIED or tag CLOSURE MISMATCH | Closure formula stated; result declared VERIFIED or tagged `[FM-09]` |

---

### Phase 1: Candidate Pre-scan

**Entry condition**: Phase 1 SHALL NOT begin until: the PROTOCOL PREAMBLE is fully declared, the scenario is received, and no trigger entry has been written.

**Job**: Phase 1 SHALL identify all automation candidates potentially affected by the Opportunity Status field changing to `Closed Won`. Phase 1 SHALL produce a numbered CA-NN list and declare the candidate denominator N.

**Anomaly questions** -- all three SHALL carry Status: OPEN before the first CA entry:

```
STORM QUESTION     Status: OPEN
  Does any single change event trigger more than 3 automations in the same execution tier?

MISSING QUESTION   Status: OPEN
  Is there an expected automation that does not appear in the candidate list?

CIRCULAR QUESTION  Status: OPEN
  Does any trigger chain produce a field write that re-fires an earlier trigger in the chain?
```

For each candidate, state: `CA-NN: Name | Probable Type | Probable Tier | Evidence of Registration`

State at the close of Phase 1: `Candidate denominator: N = [count]`

**Exit condition**: Phase 1 SHALL be declared complete when: all three anomaly questions carry Status: OPEN, all CA-NN candidates are listed, and the denominator statement is present.

---

### Phase 2: Trigger Enumeration

**Entry condition**: Phase 2 SHALL NOT begin until: Phase 1 SHALL be declared complete, denominator N is stated, and all three anomaly questions carry Status: OPEN.

**Job**: Phase 2 SHALL enumerate every trigger that fires in the order it fires, using the FIRING ENTRY schema. Side-effect writes with automation potential SHALL spawn a new trigger row immediately following the row that produces the write. Candidates that do not fire SHALL use the NON-FIRING ENTRY schema. Vocabulary deviation SHALL be tagged `[VOCAB FAIL: {term} | FM-03]`. A missing slot SHALL be tagged `[SLOT MISSING: {slot name} | FM-12]`. A missing condition direction SHALL be tagged `[BRANCH BLIND: {entry name} | FM-04]`.

**Exit condition**: Phase 2 SHALL be declared complete when: every CA-NN candidate from Phase 1 has a FIRING ENTRY or NON-FIRING ENTRY, and all side-effect writes with automation potential have spawned downstream trigger rows.

---

### Phase 3: Anomaly Analysis

**Entry condition**: Phase 3 SHALL NOT begin until: Phase 2 SHALL be declared complete and all candidates enumerated.

**Job**: Phase 3 SHALL close all three anomaly questions with evidence-anchored verdicts. Each verdict SHALL cite specific trigger rows, CA-IDs, or field writes from Phase 2. A verdict with no cited evidence SHALL be tagged `[EVIDENCE GAP | FM-05, FM-06, or FM-07]`. Every confirmed anomaly SHALL include at least one remediation step; absence of remediation SHALL be tagged `[REMEDIATION ABSENT | FM-11]`.

- **STORM VERDICT**: Cite firing trigger rows. If count > 3 in the same tier: CONFIRMED + remediation. If not: NOT DETECTED.
- **MISSING TRIGGER VERDICT**: Reference FLAGGED GAP entries. If any: CONFIRMED + remediation. If none: NOT DETECTED.
- **CIRCULAR TRIGGER VERDICT**: Apply DFS back-edge detection on the Spawns graph. If back-edge found: CONFIRMED + cycle-break remediation. If DAG: NOT DETECTED.

**Exit condition**: Phase 3 SHALL be declared complete when: all three anomaly questions carry Status: CLOSED, all verdicts cite evidence, and all CONFIRMED verdicts carry a remediation step.

---

### Phase 4: Trigger Map Assembly

**Entry condition**: Phase 4 SHALL NOT begin until: Phase 3 SHALL be declared complete and all anomaly verdicts closed.

**Job**: Phase 4 SHALL produce a trigger map covering all firing triggers. The map SHALL include: Seq, Trigger Name, CA-Ref, Tier (sync/async), Anomaly Flag, Spawns. A map missing the Tier or Spawns column SHALL be tagged `[FM-10]`.

| Seq | Trigger Name | CA-Ref | Tier | Anomaly Flag | Spawns |
|-----|-------------|--------|------|-------------|--------|
| ... | ... | ... | ... | ... | ... |

**Exit condition**: Phase 4 SHALL be declared complete when: all firing triggers from Phase 2 appear in the table and all six columns are populated.

---

### Phase 5: Denominator Closure

**Entry condition**: Phase 5 SHALL NOT begin until: Phase 4 SHALL be declared complete and the trigger map is present.

**Job**: Phase 5 SHALL perform the arithmetic closure check: `FIRED + CONFIRMED ABSENT + FLAGGED GAP = N`. A mismatch SHALL be tagged `[CLOSURE MISMATCH: {actual count} != N | FM-09]`.

```
Candidates identified (Phase 1): N
FIRED:             [count]
CONFIRMED ABSENT:  [count]
FLAGGED GAP:       [count]
Sum:               [count]
Closure:           VERIFIED | [CLOSURE MISMATCH: {sum} != N | FM-09]
```

**Exit condition**: Phase 5 SHALL be declared complete when: the closure arithmetic is stated, the sum is verified against N, and any mismatch is tagged.

---

## V-02 -- Phase Body Self-Contained: All Three Control Artifacts in Every Phase Body

**Variation axis**: Phase body self-contained (C-28)
**Hypothesis**: Requiring each phase body to open with a labeled "PHASE BODY CONTRACT" block that explicitly states entry condition, job, and exit condition -- independent of and duplicating the LIFECYCLE OVERVIEW -- makes C-28 pass by construction. The self-contained block signals to any reader opening to a phase mid-document that control-flow context is fully present in the body. Structural repetition is intentional: the LIFECYCLE OVERVIEW provides navigable overview; the phase body provides independent auditability. No gate register change is made (V-01 covered that axis); this variation tests whether the phase-body redundancy pattern alone is sufficient.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. You SHALL simulate which automations fire when the following record change occurs.

**SCENARIO**

Record: Dynamics 365 Opportunity (opportunity entity)
Change: `Status` field changed from `In Progress` to `Closed Won`
Context: Change made by a sales representative via the model-driven app Opportunity form, saved by user click.

You SHALL complete this analysis using the five-phase protocol below. Every phase body SHALL be self-contained: it SHALL open with a PHASE BODY CONTRACT block stating the entry condition, job, and exit condition for that phase. A reader who opens to any phase body in this document SHALL NOT need to consult the LIFECYCLE OVERVIEW to determine that phase's control-flow context. The LIFECYCLE OVERVIEW is for navigation; each phase body is for independent auditing.

---

### PROTOCOL PREAMBLE

#### Platform Vocabulary Contract

Approved terms (deviations SHALL be tagged `[VOCAB FAIL: {actual term} | FM-03]`):

- `sync plugin step` -- Dataverse plugin registered on the synchronous pipeline
- `async plugin step` -- Dataverse plugin registered on the asynchronous pipeline
- `automated flow` -- Power Automate flow triggered by a Dataverse record-change event
- `instant flow` -- Power Automate flow triggered manually or by another flow/app
- `scheduled flow` -- Power Automate flow triggered on a time-based recurrence
- `business rule` -- Model-driven app client-side or server-side rule
- `real-time workflow` -- Legacy Dataverse synchronous workflow
- `classic workflow` -- Legacy Dataverse asynchronous background workflow

#### Failure Mode Catalog

Every inline FM tag in this output SHALL resolve to an entry below. An FM tag with no catalog entry SHALL be tagged `[FM-15: Catalog Opacity -- FM-NN references no catalog entry]`.

**FM-01** -- Undeclared Denominator: Phase 2 begins without N declared.
**FM-02** -- Silent Trigger Omission: A CA-NN from Phase 1 has no disposition in Phase 2.
**FM-03** -- Vocabulary Drift: Non-approved platform term used. Tag: `[VOCAB FAIL: {term} | FM-03]`.
**FM-04** -- Branch Blindness: Entry has one condition slot, not both. Tag: `[BRANCH BLIND: {entry name} | FM-04]`.
**FM-05** -- Storm Evidence Gap: Storm verdict stated without citing trigger rows.
**FM-06** -- Missing-Trigger Evidence Gap: Missing trigger verdict without citing absent candidates.
**FM-07** -- Cycle Evidence Gap: Circular verdict without citing back-edge path.
**FM-08** -- Cascade Orphan: Automation-potential side-effect write has no downstream trigger row.
**FM-09** -- Denominator Closure Skip: No arithmetic closure check after enumeration. Tag: `[FM-09]`.
**FM-10** -- Trigger Map Incomplete: Tier or Spawns column absent. Tag: `[FM-10]`.
**FM-11** -- Remediation Gap: Confirmed anomaly has no remediation. Tag: `[REMEDIATION ABSENT | FM-11]`.
**FM-12** -- Entry Schema Violation: Trigger entry missing declared slot. Tag: `[SLOT MISSING: {slot name} | FM-12]`.
**FM-13** -- Anomaly Gate Absent: Anomaly question not pre-opened before Phase 2.
**FM-14** -- Phase Register Violation: Obligation statement uses descriptive language. Tag: `[REGISTER FAIL: "{actual text}" | FM-14]`.
**FM-15** -- Catalog Opacity: Inline FM tag references undeclared ID. Tag: `[FM-15: Catalog Opacity]`.
**FM-16** -- Entry Condition Absent: A named phase body carries no entry precondition. Tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. This failure mode is the primary target of V-02: the PHASE BODY CONTRACT pattern prevents FM-16 from firing by structural construction.
**FM-17** -- Gate Register Drift: Gate statement uses descriptive obligation form. Tag: `[GATE REGISTER DRIFT: "{actual text}" | FM-17]`.

*FM-15 is reflexive (catalog-level). FM-16 fires when a phase body omits its entry condition -- the PHASE BODY CONTRACT pattern in this variation prevents FM-16 by requiring all three control artifacts in every phase body.*

#### Entry Schema Contract

**FIRING ENTRY**:
```
Seq:                 [integer]
Trigger Name:        [approved vocabulary term]
CA-Ref:              [CA-NN from Phase 1]
Tier:                [sync | async]
Layer:               [plugin step | automated flow | business rule | real-time workflow | classic workflow]
Condition (Taken):   [what MUST be true for this trigger to fire]
Condition (Skipped): [what would prevent this trigger from firing]
Inputs:              [field/event consumed]
Outputs:             [field write / notification / record creation]
Side Effects:        [downstream writes or spawned actions; "None" if absent]
Spawns:              [CA-NN of cascade trigger; "None" if absent]
Anomaly Flag:        [none | storm | missing | cycle | FM-NN]
```

**NON-FIRING ENTRY**:
```
CA-Ref:              [CA-NN identifier]
Trigger Name:        [approved vocabulary term]
Condition (Taken):   [what would cause this trigger to fire]
Condition (Skipped): [the specific condition preventing it in this scenario]
Verdict:             [CONFIRMED ABSENT | FLAGGED GAP]
FM Flag:             [FM-02 if FLAGGED GAP; "none" if CONFIRMED ABSENT]
```

---

### LIFECYCLE OVERVIEW

Navigation reference only. Each phase body is self-contained and SHALL be consulted for independent auditing.

| Phase | Name | Entry condition | Job | Exit condition |
|-------|------|----------------|-----|----------------|
| 1 | Candidate Pre-scan | Scenario received; preamble complete | Identify candidates; declare N; open anomaly questions | N declared; anomaly slots OPEN |
| 2 | Trigger Enumeration | Phase 1 complete; N declared; slots OPEN | Enumerate all N candidates per schema | All N candidates disposed; cascades spawned |
| 3 | Anomaly Analysis | Phase 2 complete | Close anomaly slots with evidence-cited verdicts | All slots CLOSED; confirmed anomalies have remediation |
| 4 | Trigger Map Assembly | Phase 3 complete | Produce trigger map with all six columns | All firing triggers in table; all columns populated |
| 5 | Denominator Closure | Phase 4 complete | Verify closure arithmetic | Closure formula stated; VERIFIED or MISMATCH tagged |

---

### Phase 1: Candidate Pre-scan

```
PHASE BODY CONTRACT -- Phase 1
Entry condition:  This phase body SHALL NOT be entered until: the PROTOCOL PREAMBLE is fully
                  declared (Platform Vocabulary Contract, FM Catalog, Entry Schema Contract),
                  the scenario is received, and no trigger entry has been written.
Job:              Identify all automation candidates potentially affected by the Opportunity
                  Status field changing to Closed Won. Produce a numbered CA-NN list.
                  Declare the candidate denominator N. Open all three anomaly question slots.
Exit condition:   This phase body SHALL be declared complete when: the denominator statement
                  "Candidate denominator: N = [count]" is present, all CA-NN candidates are
                  listed, and all three anomaly questions carry Status: OPEN.
```

**Anomaly questions** -- declare Status: OPEN before the first CA entry:

```
STORM QUESTION     Status: OPEN
  Does any single change event fire more than 3 automations in the same execution tier?

MISSING QUESTION   Status: OPEN
  Is there an expected automation absent from the candidate list?

CIRCULAR QUESTION  Status: OPEN
  Does any trigger chain produce a field write that re-fires an earlier trigger?
```

For each candidate, state: `CA-NN: Name | Probable Type | Probable Tier | Evidence of Registration`

`Candidate denominator: N = [count]`

---

### Phase 2: Trigger Enumeration

```
PHASE BODY CONTRACT -- Phase 2
Entry condition:  This phase body SHALL NOT be entered until: Phase 1 is declared complete
                  (denominator N stated, all three anomaly questions carry Status: OPEN).
Job:              Enumerate every trigger that fires, in order, using the FIRING ENTRY schema.
                  Side-effect writes with automation potential SHALL spawn a new trigger row
                  immediately after the row that produces the write. Non-firing candidates
                  SHALL use the NON-FIRING ENTRY schema.
Exit condition:   This phase body SHALL be declared complete when: every CA-NN candidate
                  from Phase 1 has either a FIRING ENTRY or NON-FIRING ENTRY, and all
                  side-effect field writes with automation potential have spawned downstream
                  trigger rows.
```

[ENUMERATE TRIGGERS HERE]

---

### Phase 3: Anomaly Analysis

```
PHASE BODY CONTRACT -- Phase 3
Entry condition:  This phase body SHALL NOT be entered until: Phase 2 is declared complete
                  (all candidates enumerated, all cascade rows present).
Job:              Close all three anomaly question slots. Each verdict SHALL cite specific
                  trigger rows, CA-IDs, or field writes from Phase 2. A verdict with no
                  cited evidence SHALL be tagged [EVIDENCE GAP | FM-05/FM-06/FM-07]. Every
                  confirmed anomaly SHALL include at least one concrete remediation step.
Exit condition:   This phase body SHALL be declared complete when: all three anomaly
                  questions carry Status: CLOSED, all verdicts cite evidence, and all
                  CONFIRMED verdicts carry a remediation step.
```

- **STORM VERDICT**: Cite firing trigger rows. If count > 3 in same tier: CONFIRMED + remediation. Else: NOT DETECTED.
- **MISSING TRIGGER VERDICT**: Reference FLAGGED GAP entries. If any: CONFIRMED + remediation. Else: NOT DETECTED.
- **CIRCULAR TRIGGER VERDICT**: Apply DFS back-edge detection on the Spawns graph. If back-edge: CONFIRMED + cycle-break. Else: NOT DETECTED.

---

### Phase 4: Trigger Map Assembly

```
PHASE BODY CONTRACT -- Phase 4
Entry condition:  This phase body SHALL NOT be entered until: Phase 3 is declared complete
                  (all three anomaly verdicts carry Status: CLOSED).
Job:              Produce a trigger map table covering all firing triggers with columns:
                  Seq, Trigger Name, CA-Ref, Tier (sync/async), Anomaly Flag, Spawns.
                  A map missing Tier or Spawns SHALL be tagged [FM-10].
Exit condition:   This phase body SHALL be declared complete when: all firing triggers from
                  Phase 2 appear in the table and all six columns are populated per row.
```

| Seq | Trigger Name | CA-Ref | Tier | Anomaly Flag | Spawns |
|-----|-------------|--------|------|-------------|--------|

---

### Phase 5: Denominator Closure

```
PHASE BODY CONTRACT -- Phase 5
Entry condition:  This phase body SHALL NOT be entered until: Phase 4 is declared complete
                  (trigger map present with all columns populated).
Job:              Perform the arithmetic closure check: verify that
                  FIRED + CONFIRMED ABSENT + FLAGGED GAP = N (denominator from Phase 1).
                  A mismatch SHALL be tagged [CLOSURE MISMATCH: {actual count} != N | FM-09].
Exit condition:   This phase body SHALL be declared complete when: the closure arithmetic
                  is stated in the format below, the sum is verified against N, and any
                  mismatch is tagged.
```

```
Candidates identified (Phase 1): N
FIRED:             [count]
CONFIRMED ABSENT:  [count]
FLAGGED GAP:       [count]
Sum:               [count]
Closure:           VERIFIED | [CLOSURE MISMATCH: {sum} != N | FM-09]
```

---

## V-03 -- FM Catalog Entry-Condition-Absent: FM-16 Named and Inline-Taggable

**Variation axis**: FM catalog entry-condition-absent (C-29)
**Hypothesis**: Adding FM-16 (Entry Condition Absent) to the FM catalog and explicitly instructing inline tagging of `[ENTRY CONDITION ABSENT: Phase N | FM-16]` for any phase body missing an entry precondition makes C-29 pass by construction. Entry-condition absence transitions from a silent gap (detectable only by a reviewer reading the phase body) to a named structural defect (self-taggable by the analysis itself). Phase bodies may still omit entry conditions -- but the omission is now structurally visible rather than reviewable-only. No phase-body-contract pattern (V-02) or gate-register change (V-01) is introduced. Single-axis test.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. You SHALL simulate which automations fire when the following record change occurs.

**SCENARIO**

Record: Dynamics 365 Opportunity (opportunity entity)
Change: `Status` field changed from `In Progress` to `Closed Won`
Context: Change made by a sales representative via the model-driven app Opportunity form, saved by user click.

You SHALL complete this analysis using the five-phase protocol below. Entry condition self-check rule: before writing any phase body content, verify that the phase body contains an explicit entry condition statement. If the entry condition is absent, tag the phase opening: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. Do not suppress this tag -- it is a named failure mode, not an editorial note.

---

### PROTOCOL PREAMBLE

#### Platform Vocabulary Contract

Approved terms (deviations SHALL be tagged `[VOCAB FAIL: {actual term} | FM-03]`):

- `sync plugin step` -- Dataverse plugin registered on the synchronous pipeline
- `async plugin step` -- Dataverse plugin registered on the asynchronous pipeline
- `automated flow` -- Power Automate flow triggered by a Dataverse record-change event
- `instant flow` -- Power Automate flow triggered manually or by another flow/app
- `scheduled flow` -- Power Automate flow triggered on a time-based recurrence
- `business rule` -- Model-driven app client-side or server-side rule
- `real-time workflow` -- Legacy Dataverse synchronous workflow
- `classic workflow` -- Legacy Dataverse asynchronous background workflow

#### Failure Mode Catalog

Every inline FM tag in this output SHALL resolve to an entry below. An FM tag with no catalog entry SHALL be tagged `[FM-15: Catalog Opacity]`.

**FM-01** -- Undeclared Denominator: Phase 2 begins without N declared.
**FM-02** -- Silent Trigger Omission: CA-NN from Phase 1 has no disposition in Phase 2.
**FM-03** -- Vocabulary Drift: Non-approved term used. Tag: `[VOCAB FAIL: {term} | FM-03]`.
**FM-04** -- Branch Blindness: Entry has one condition slot, not both. Tag: `[BRANCH BLIND: {name} | FM-04]`.
**FM-05** -- Storm Evidence Gap: Storm verdict stated without citing trigger rows.
**FM-06** -- Missing-Trigger Evidence Gap: Missing trigger verdict without citing absent candidates.
**FM-07** -- Cycle Evidence Gap: Circular verdict without citing back-edge path.
**FM-08** -- Cascade Orphan: Automation-potential side-effect write has no downstream trigger row.
**FM-09** -- Denominator Closure Skip: No arithmetic closure check after enumeration.
**FM-10** -- Trigger Map Incomplete: Tier or Spawns column absent.
**FM-11** -- Remediation Gap: Confirmed anomaly has no remediation.
**FM-12** -- Entry Schema Violation: Trigger entry missing a declared slot. Tag: `[SLOT MISSING: {slot name} | FM-12]`.
**FM-13** -- Anomaly Gate Absent: Anomaly question not pre-opened before Phase 2.
**FM-14** -- Phase Register Violation: Obligation statement uses descriptive language. Tag: `[REGISTER FAIL: "{actual text}" | FM-14]`.
**FM-15** -- Catalog Opacity: Inline FM tag references undeclared ID. (Catalog-level reflexive defect.)
**FM-16** -- Entry Condition Absent: A named phase body carries no entry precondition statement. Tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. This is the primary defect class targeted by the entry condition self-check rule in this protocol. Every phase body SHALL carry an explicit "Entry condition:" statement; absence of this statement SHALL be self-tagged using this FM ID.
**FM-17** -- Gate Register Drift: Gate statement (entry or exit condition) uses descriptive form in obligation position. Tag: `[GATE REGISTER DRIFT: "{actual text}" | FM-17]`.

*FM-15 is the catalog-level reflexive defect. FM-16 is the phase-structure defect -- naming it in the catalog makes entry-condition absence self-taggable rather than reviewer-dependent. An output that omits a phase entry condition but does not tag FM-16 fails this criterion more severely than one that at least tags the gap.*

#### Entry Schema Contract

**FIRING ENTRY**:
```
Seq:                 [integer]
Trigger Name:        [approved vocabulary term]
CA-Ref:              [CA-NN from Phase 1]
Tier:                [sync | async]
Layer:               [plugin step | automated flow | business rule | real-time workflow | classic workflow]
Condition (Taken):   [what MUST be true for this trigger to fire]
Condition (Skipped): [what would prevent this trigger from firing]
Inputs:              [field/event consumed]
Outputs:             [field write / notification / record creation]
Side Effects:        [downstream writes or spawned actions; "None" if absent]
Spawns:              [CA-NN of cascade trigger; "None" if absent]
Anomaly Flag:        [none | storm | missing | cycle | FM-NN]
```

**NON-FIRING ENTRY**:
```
CA-Ref:              [CA-NN identifier]
Trigger Name:        [approved vocabulary term]
Condition (Taken):   [what would cause this trigger to fire]
Condition (Skipped): [the specific condition preventing it in this scenario]
Verdict:             [CONFIRMED ABSENT | FLAGGED GAP]
FM Flag:             [FM-02 if FLAGGED GAP; "none" if CONFIRMED ABSENT]
```

---

### LIFECYCLE OVERVIEW

| Phase | Name | Entry condition | Job | Exit condition |
|-------|------|----------------|-----|----------------|
| 1 | Candidate Pre-scan | Scenario received; preamble complete; no entries written | Identify candidates; declare N; open anomaly questions | N declared; all three anomaly questions carry Status: OPEN |
| 2 | Trigger Enumeration | Phase 1 complete; N declared; anomaly slots OPEN | Enumerate all N candidates per schema; cascade side-effects spawn rows | All N candidates disposed; all automation-potential side-effects have downstream rows |
| 3 | Anomaly Analysis | Phase 2 complete; all candidates enumerated | Close anomaly slots with evidence-cited verdicts and remediation | All slots CLOSED; confirmed anomalies have remediation |
| 4 | Trigger Map Assembly | Phase 3 complete; all anomaly verdicts closed | Produce trigger map with Seq, Name, CA-Ref, Tier, Anomaly Flag, Spawns | All firing triggers in table; all columns populated |
| 5 | Denominator Closure | Phase 4 complete; trigger map present | Verify (FIRED + CONFIRMED ABSENT + FLAGGED GAP) = N | Closure formula stated; VERIFIED or FM-09 tagged |

---

### Phase 1: Candidate Pre-scan

**Entry condition**: Scenario received; PROTOCOL PREAMBLE fully declared; no trigger entry written yet. Tag this phase `[ENTRY CONDITION ABSENT: Phase 1 | FM-16]` if this statement is absent.

**Job**: Phase 1 SHALL identify all automation candidates potentially affected by the Opportunity Status field changing to `Closed Won`. Phase 1 SHALL produce a numbered CA-NN list and declare the candidate denominator N.

**Anomaly questions** -- all three SHALL carry Status: OPEN before the first CA entry:

```
STORM QUESTION     Status: OPEN
  Does any single change event fire more than 3 automations in the same execution tier?

MISSING QUESTION   Status: OPEN
  Is there an expected automation absent from the candidate list?

CIRCULAR QUESTION  Status: OPEN
  Does any trigger chain produce a field write that re-fires an earlier trigger?
```

For each candidate: `CA-NN: Name | Probable Type | Probable Tier | Evidence of Registration`

`Candidate denominator: N = [count]`

**Exit condition**: Phase 1 is complete when: denominator N is stated, all CA-NN listed, all three anomaly questions carry Status: OPEN.

---

### Phase 2: Trigger Enumeration

**Entry condition**: Phase 1 is complete (denominator N declared; anomaly slots OPEN). Tag this phase `[ENTRY CONDITION ABSENT: Phase 2 | FM-16]` if this statement is absent.

**Job**: Phase 2 SHALL enumerate every trigger in the order it fires using the FIRING ENTRY schema. Side-effect writes with automation potential SHALL spawn a new trigger row immediately following. Non-firing candidates SHALL use the NON-FIRING ENTRY schema. Vocabulary deviation SHALL be tagged `[VOCAB FAIL: {term} | FM-03]`. Missing slot SHALL be tagged `[SLOT MISSING: {slot} | FM-12]`. Missing condition direction SHALL be tagged `[BRANCH BLIND: {name} | FM-04]`.

**Exit condition**: Phase 2 is complete when all N CA-NN candidates are disposed and all automation-potential side-effects have spawned downstream rows.

[ENUMERATE TRIGGERS HERE]

---

### Phase 3: Anomaly Analysis

**Entry condition**: Phase 2 is complete (all candidates enumerated, all cascade rows present). Tag this phase `[ENTRY CONDITION ABSENT: Phase 3 | FM-16]` if this statement is absent.

**Job**: Phase 3 SHALL close all three anomaly questions with evidence-anchored verdicts. Each verdict SHALL cite specific trigger rows, CA-IDs, or field writes from Phase 2. No-evidence verdict: tag `[EVIDENCE GAP | FM-05/FM-06/FM-07]`. Confirmed anomaly with no remediation: tag `[REMEDIATION ABSENT | FM-11]`.

- **STORM VERDICT**: Cite firing rows. If count > 3 in same tier: CONFIRMED + remediation. Else: NOT DETECTED.
- **MISSING TRIGGER VERDICT**: Reference FLAGGED GAP entries. If any: CONFIRMED + remediation. Else: NOT DETECTED.
- **CIRCULAR TRIGGER VERDICT**: Apply DFS back-edge detection. If back-edge: CONFIRMED + cycle-break. Else: NOT DETECTED.

**Exit condition**: Phase 3 is complete when all three anomaly questions carry Status: CLOSED, all verdicts cite evidence, and all CONFIRMED verdicts have remediation.

---

### Phase 4: Trigger Map Assembly

**Entry condition**: Phase 3 is complete (all anomaly verdicts carry Status: CLOSED). Tag this phase `[ENTRY CONDITION ABSENT: Phase 4 | FM-16]` if this statement is absent.

**Job**: Phase 4 SHALL produce a trigger map covering all firing triggers with columns: Seq, Trigger Name, CA-Ref, Tier (sync/async), Anomaly Flag, Spawns. Missing Tier or Spawns column: tag `[FM-10]`.

| Seq | Trigger Name | CA-Ref | Tier | Anomaly Flag | Spawns |
|-----|-------------|--------|------|-------------|--------|

**Exit condition**: Phase 4 is complete when all firing triggers from Phase 2 appear in the table and all six columns are populated.

---

### Phase 5: Denominator Closure

**Entry condition**: Phase 4 is complete (trigger map present with all six columns). Tag this phase `[ENTRY CONDITION ABSENT: Phase 5 | FM-16]` if this statement is absent.

**Job**: Phase 5 SHALL perform the arithmetic closure check. Mismatch: tag `[CLOSURE MISMATCH: {count} != N | FM-09]`.

```
Candidates identified (Phase 1): N
FIRED:             [count]
CONFIRMED ABSENT:  [count]
FLAGGED GAP:       [count]
Sum:               [count]
Closure:           VERIFIED | [CLOSURE MISMATCH: {sum} != N | FM-09]
```

**Exit condition**: Phase 5 is complete when closure arithmetic is stated, sum verified against N, and any mismatch tagged.

---

## V-04 -- Phase Body Self-Contained + FM-16 Named: C-28 and C-29 Combined

**Variation axis**: Phase body self-contained (C-28) + FM catalog entry-condition-absent (C-29)
**Hypothesis**: Phase bodies are structurally self-contained via the PHASE BODY CONTRACT pattern (C-28), AND FM-16 is named in the catalog (C-29). The two criteria compound: C-28 compels entry conditions to appear within each phase body; FM-16 makes their absence inline-taggable. Any output that fails to include entry conditions in a phase body now has two failure modes simultaneously: the PHASE BODY CONTRACT is structurally violated (C-28), and FM-16 SHOULD be tagged but is absent (C-29). The combination produces stronger structural pressure than either criterion alone. No gate register change (V-01 axis) is applied here.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. You SHALL simulate which automations fire when the following record change occurs.

**SCENARIO**

Record: Dynamics 365 Opportunity (opportunity entity)
Change: `Status` field changed from `In Progress` to `Closed Won`
Context: Change made by a sales representative via the model-driven app Opportunity form, saved by user click.

You SHALL complete this analysis using the five-phase protocol below. Two invariants apply to every phase body:

**Invariant 1 -- Phase body self-contained**: Every phase body SHALL open with a PHASE BODY CONTRACT block containing exactly three labeled lines: `Entry condition:`, `Job:`, and `Exit condition:`. A phase body that contains Job and Exit condition but no Entry condition SHALL be tagged `[ENTRY CONDITION ABSENT: Phase N | FM-16]` at the opening of the PHASE BODY CONTRACT block.

**Invariant 2 -- FM-16 self-tagging**: If any phase body is missing an entry condition, the first line of that phase body SHALL be `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. This tag is not editorial -- it is a structural defect declaration and SHALL appear even if the phase's analysis is otherwise complete.

---

### PROTOCOL PREAMBLE

#### Platform Vocabulary Contract

Approved terms (deviations SHALL be tagged `[VOCAB FAIL: {actual term} | FM-03]`):

- `sync plugin step` -- Dataverse plugin registered on the synchronous pipeline
- `async plugin step` -- Dataverse plugin registered on the asynchronous pipeline
- `automated flow` -- Power Automate flow triggered by a Dataverse record-change event
- `instant flow` -- Power Automate flow triggered manually or by another flow/app
- `scheduled flow` -- Power Automate flow triggered on a time-based recurrence
- `business rule` -- Model-driven app client-side or server-side rule
- `real-time workflow` -- Legacy Dataverse synchronous workflow
- `classic workflow` -- Legacy Dataverse asynchronous background workflow

#### Failure Mode Catalog

Every inline FM tag SHALL resolve to an entry below. Unresolvable FM tag: `[FM-15: Catalog Opacity]`.

**FM-01** -- Undeclared Denominator: Phase 2 begins without N declared.
**FM-02** -- Silent Trigger Omission: CA-NN from Phase 1 has no disposition.
**FM-03** -- Vocabulary Drift: Non-approved term. Tag: `[VOCAB FAIL: {term} | FM-03]`.
**FM-04** -- Branch Blindness: Entry missing one condition direction. Tag: `[BRANCH BLIND: {name} | FM-04]`.
**FM-05** -- Storm Evidence Gap: Storm verdict without citing trigger rows.
**FM-06** -- Missing-Trigger Evidence Gap: Missing trigger verdict without citing absent candidates.
**FM-07** -- Cycle Evidence Gap: Circular verdict without citing back-edge path.
**FM-08** -- Cascade Orphan: Automation-potential side-effect write has no downstream trigger row.
**FM-09** -- Denominator Closure Skip: No arithmetic closure check. Tag: `[FM-09]`.
**FM-10** -- Trigger Map Incomplete: Tier or Spawns column absent. Tag: `[FM-10]`.
**FM-11** -- Remediation Gap: Confirmed anomaly without remediation. Tag: `[REMEDIATION ABSENT | FM-11]`.
**FM-12** -- Entry Schema Violation: Trigger entry missing declared slot. Tag: `[SLOT MISSING: {slot} | FM-12]`.
**FM-13** -- Anomaly Gate Absent: Anomaly question not pre-opened before Phase 2.
**FM-14** -- Phase Register Violation: Obligation statement uses descriptive language. Tag: `[REGISTER FAIL: "{text}" | FM-14]`.
**FM-15** -- Catalog Opacity: FM tag references undeclared ID. (Reflexive catalog-level defect.)
**FM-16** -- Entry Condition Absent: A phase body carries no entry precondition. Tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. Every phase body in this protocol MUST open with a PHASE BODY CONTRACT block containing an `Entry condition:` line. A phase body missing this line SHALL be self-tagged with FM-16 at its opening. FM-16 is the target defect of Invariant 2 above.
**FM-17** -- Gate Register Drift: Gate statement uses descriptive obligation form. Tag: `[GATE REGISTER DRIFT: "{text}" | FM-17]`.

*FM-15 is the catalog-level reflexive defect. FM-16 is the phase-body entry-condition defect. Together they ensure that both catalog completeness and phase-boundary completeness are self-verifiable without external reviewer expertise.*

#### Entry Schema Contract

**FIRING ENTRY**:
```
Seq:                 [integer]
Trigger Name:        [approved vocabulary term]
CA-Ref:              [CA-NN from Phase 1]
Tier:                [sync | async]
Layer:               [plugin step | automated flow | business rule | real-time workflow | classic workflow]
Condition (Taken):   [what MUST be true for this trigger to fire]
Condition (Skipped): [what would prevent this trigger from firing]
Inputs:              [field/event consumed]
Outputs:             [field write / notification / record creation]
Side Effects:        [downstream writes or spawned actions; "None" if absent]
Spawns:              [CA-NN of cascade trigger; "None" if absent]
Anomaly Flag:        [none | storm | missing | cycle | FM-NN]
```

**NON-FIRING ENTRY**:
```
CA-Ref:              [CA-NN identifier]
Trigger Name:        [approved vocabulary term]
Condition (Taken):   [what would cause this trigger to fire]
Condition (Skipped): [the specific condition preventing it in this scenario]
Verdict:             [CONFIRMED ABSENT | FLAGGED GAP]
FM Flag:             [FM-02 if FLAGGED GAP; "none" if CONFIRMED ABSENT]
```

---

### LIFECYCLE OVERVIEW

Navigation reference only. Every phase body is independently auditable via its own PHASE BODY CONTRACT block.

| Phase | Name | Entry condition | Job | Exit condition |
|-------|------|----------------|-----|----------------|
| 1 | Candidate Pre-scan | Preamble complete; scenario received; no entries written | Identify candidates; declare N; open anomaly questions | N declared; anomaly slots OPEN |
| 2 | Trigger Enumeration | Phase 1 complete; N declared; slots OPEN | Enumerate all N candidates; cascade side-effects spawn rows | All N disposed; all automation-potential side-effects spawned |
| 3 | Anomaly Analysis | Phase 2 complete | Close anomaly slots with evidence-cited verdicts and remediation | All slots CLOSED; confirmed anomalies have remediation |
| 4 | Trigger Map Assembly | Phase 3 complete | Produce trigger map with six named columns | All firing triggers in table; all columns populated |
| 5 | Denominator Closure | Phase 4 complete | Verify (FIRED + CONFIRMED ABSENT + FLAGGED GAP) = N | Closure formula stated; VERIFIED or FM-09 tagged |

---

### Phase 1: Candidate Pre-scan

```
PHASE BODY CONTRACT -- Phase 1
Entry condition:  Scenario received. PROTOCOL PREAMBLE fully declared (Platform Vocabulary
                  Contract, FM Catalog, Entry Schema Contract all present). No trigger entry
                  written yet.
Job:              Identify all automation candidates potentially affected by the Opportunity
                  Status field changing to Closed Won. Produce a numbered CA-NN list. Declare
                  the candidate denominator N. Open all three anomaly question slots.
Exit condition:   This phase SHALL be complete when the denominator statement is present,
                  all CA-NN candidates are listed, and all three anomaly questions carry
                  Status: OPEN.
```

```
STORM QUESTION     Status: OPEN
  Does any single change event fire more than 3 automations in the same execution tier?

MISSING QUESTION   Status: OPEN
  Is there an expected automation absent from the candidate list?

CIRCULAR QUESTION  Status: OPEN
  Does any trigger chain produce a field write that re-fires an earlier trigger?
```

For each candidate: `CA-NN: Name | Probable Type | Probable Tier | Evidence of Registration`

`Candidate denominator: N = [count]`

---

### Phase 2: Trigger Enumeration

```
PHASE BODY CONTRACT -- Phase 2
Entry condition:  Phase 1 is complete: denominator N stated; all three anomaly questions
                  carry Status: OPEN.
Job:              Enumerate every trigger that fires, in the order it fires, using the
                  FIRING ENTRY schema. Side-effect writes with automation potential SHALL spawn
                  a new trigger row immediately following the producing row. Non-firing
                  candidates SHALL use the NON-FIRING ENTRY schema.
Exit condition:   This phase SHALL be complete when every CA-NN candidate has a FIRING ENTRY
                  or NON-FIRING ENTRY, and all automation-potential side-effect writes have
                  spawned downstream trigger rows.
```

[ENUMERATE TRIGGERS HERE]

---

### Phase 3: Anomaly Analysis

```
PHASE BODY CONTRACT -- Phase 3
Entry condition:  Phase 2 is complete: all N CA-NN candidates enumerated; all cascade rows
                  present.
Job:              Close all three anomaly question slots with evidence-anchored verdicts. Each
                  verdict SHALL cite specific trigger rows, CA-IDs, or field writes from
                  Phase 2. Confirmed anomaly without remediation: tag [REMEDIATION ABSENT |
                  FM-11]. No-evidence verdict: tag [EVIDENCE GAP | FM-05/FM-06/FM-07].
Exit condition:   This phase SHALL be complete when all three anomaly questions carry Status:
                  CLOSED, all verdicts cite evidence, and all CONFIRMED verdicts have
                  remediation.
```

- **STORM VERDICT**: Cite firing rows. If > 3 in same tier: CONFIRMED + remediation. Else: NOT DETECTED.
- **MISSING TRIGGER VERDICT**: Reference FLAGGED GAP entries. If any: CONFIRMED + remediation. Else: NOT DETECTED.
- **CIRCULAR TRIGGER VERDICT**: DFS back-edge detection on Spawns graph. If back-edge: CONFIRMED + cycle-break. Else: NOT DETECTED.

---

### Phase 4: Trigger Map Assembly

```
PHASE BODY CONTRACT -- Phase 4
Entry condition:  Phase 3 is complete: all three anomaly questions carry Status: CLOSED.
Job:              Produce a trigger map table covering all firing triggers. Columns SHALL be:
                  Seq, Trigger Name, CA-Ref, Tier (sync/async), Anomaly Flag, Spawns.
                  Missing Tier or Spawns: tag [FM-10].
Exit condition:   This phase SHALL be complete when all firing triggers from Phase 2 appear in
                  the table and all six columns are populated per row.
```

| Seq | Trigger Name | CA-Ref | Tier | Anomaly Flag | Spawns |
|-----|-------------|--------|------|-------------|--------|

---

### Phase 5: Denominator Closure

```
PHASE BODY CONTRACT -- Phase 5
Entry condition:  Phase 4 is complete: trigger map present with all six columns populated.
Job:              Perform the arithmetic closure check: verify FIRED + CONFIRMED ABSENT +
                  FLAGGED GAP = N. Mismatch: tag [CLOSURE MISMATCH: {count} != N | FM-09].
Exit condition:   This phase SHALL be complete when closure arithmetic is stated, sum is
                  verified against N, and any mismatch is tagged.
```

```
Candidates identified (Phase 1): N
FIRED:             [count]
CONFIRMED ABSENT:  [count]
FLAGGED GAP:       [count]
Sum:               [count]
Closure:           VERIFIED | [CLOSURE MISMATCH: {sum} != N | FM-09]
```

---

## V-05 -- Full Integration: C-28 + C-29 + C-30 + All R7 Criteria

**Variation axis**: Phase body self-contained + FM-16 named + gate register formal + all prior criteria
**Hypothesis**: Full integration of all three R8 criteria: (1) PHASE BODY CONTRACT blocks make every phase body independently auditable (C-28), (2) FM-16 in the catalog names entry-condition-absence as a taggable defect class (C-29), (3) all gate statements -- both entry conditions and exit conditions -- use SHALL/MUST in the obligation position, and the LIFECYCLE OVERVIEW table itself uses formal gate register (C-30). The prompt models correct register in its own instructions, cascading formal gate language into the output. This is the strongest structural configuration for R8.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. You SHALL simulate which automations fire when the following record change occurs.

**SCENARIO**

Record: Dynamics 365 Opportunity (opportunity entity)
Change: `Status` field changed from `In Progress` to `Closed Won`
Context: Change made by a sales representative via the model-driven app Opportunity form, saved by user click.

You SHALL complete this analysis using the five-phase protocol defined below. Three structural invariants govern every phase boundary:

**Invariant 1 -- Phase body self-contained**: Every phase body SHALL open with a PHASE BODY CONTRACT block containing three labeled lines: `Entry condition:`, `Job:`, and `Exit condition:`. No phase body SHALL omit any of these three lines. A phase body containing Job and Exit condition but no Entry condition SHALL be tagged `[ENTRY CONDITION ABSENT: Phase N | FM-16]` as the first line of the PHASE BODY CONTRACT block.

**Invariant 2 -- FM-16 self-tagging**: Every phase body missing its `Entry condition:` line SHALL be self-tagged with `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. This tag is a named structural defect, not a comment. It SHALL appear in the output even if the remainder of the phase analysis is complete.

**Invariant 3 -- Gate register**: All entry condition statements SHALL use the obligation form: `This phase SHALL NOT begin until: [precondition]`. All exit condition statements SHALL use the obligation form: `This phase SHALL be declared complete when: [condition]`. Descriptive gate form ("Phase N is complete when:" without SHALL) SHALL be tagged `[GATE REGISTER DRIFT: "{actual text}" | FM-17]`.

---

### PROTOCOL PREAMBLE

All three contract declarations below SHALL be present before Phase 1 begins. No platform term SHALL appear before the Platform Vocabulary Contract. No FM tag SHALL appear before the FM Catalog. No entry slot SHALL be used before the Entry Schema Contract. All obligation statements in this preamble use formal register; any deviation SHALL be tagged `[REGISTER FAIL: "{text}" | FM-14]`.

#### Platform Vocabulary Contract

Approved terms (deviations SHALL be tagged `[VOCAB FAIL: {actual term} | FM-03]`):

- `sync plugin step` -- Dataverse plugin registered on the synchronous pipeline (pre-operation or post-operation, same transaction)
- `async plugin step` -- Dataverse plugin registered on the asynchronous pipeline (post-operation, separate system job)
- `automated flow` -- Power Automate flow triggered by a Dataverse record-change event (When a row is added, modified or deleted)
- `instant flow` -- Power Automate flow triggered manually or by another flow/app
- `scheduled flow` -- Power Automate flow triggered on a time-based recurrence
- `business rule` -- Model-driven app client-side or server-side rule evaluated on field value
- `real-time workflow` -- Legacy Dataverse synchronous workflow (deprecated but may be active)
- `classic workflow` -- Legacy Dataverse asynchronous background workflow

#### Failure Mode Catalog

Every inline FM tag in this output SHALL resolve to an entry in this catalog. An FM tag with no catalog entry SHALL be tagged `[FM-15: Catalog Opacity -- inline tag FM-NN references no catalog entry]`. This catalog is reflexive: FM-15 covers catalog incompleteness; FM-16 covers phase-body entry-condition absence; both make the protocol self-validating without external reviewer expertise.

**FM-01** -- Undeclared Denominator: Phase 2 begins without N declared. Correction: Phase 1 SHALL declare N before Phase 2 begins.
**FM-02** -- Silent Trigger Omission: A CA-NN from Phase 1 has no disposition in Phase 2. Correction: Every CA-NN SHALL appear as FIRING or NON-FIRING.
**FM-03** -- Vocabulary Drift: A non-approved platform term appears in the output. Tag: `[VOCAB FAIL: {term} | FM-03]`.
**FM-04** -- Branch Blindness: A trigger entry has one condition slot without the other. Tag: `[BRANCH BLIND: {entry name} | FM-04]`.
**FM-05** -- Storm Evidence Gap: Storm verdict stated without citing trigger rows. Correction: Cite at minimum two CA-IDs and their combined fire count.
**FM-06** -- Missing-Trigger Evidence Gap: Missing trigger verdict without citing absent candidates. Correction: Reference FLAGGED GAP entries.
**FM-07** -- Cycle Evidence Gap: Circular verdict without citing the back-edge path. Correction: State `{Trigger A} -> {Field Write} -> {Trigger B} -> ... -> {Trigger A}`.
**FM-08** -- Cascade Orphan: Automation-potential side-effect write has no downstream trigger row. Correction: Every such write SHALL spawn a trigger row.
**FM-09** -- Denominator Closure Skip: No arithmetic closure check after enumeration. Tag: `[CLOSURE MISMATCH: {count} != N | FM-09]`.
**FM-10** -- Trigger Map Incomplete: Trigger map missing Tier or Spawns column. Tag: `[FM-10]`.
**FM-11** -- Remediation Gap: Confirmed anomaly has no remediation. Tag: `[REMEDIATION ABSENT | FM-11]`.
**FM-12** -- Entry Schema Violation: Trigger entry missing a declared slot. Tag: `[SLOT MISSING: {slot name} | FM-12]`.
**FM-13** -- Anomaly Gate Absent: Anomaly question not pre-opened before Phase 2. Correction: All three SHALL carry Status: OPEN before the first trigger entry.
**FM-14** -- Phase Register Violation: Obligation statement in a phase body uses descriptive language instead of SHALL/MUST/PROHIBITED/MAY NOT. Tag: `[REGISTER FAIL: "{actual text}" -> SHALL/MUST | FM-14]`.
**FM-15** -- Catalog Opacity: Inline FM tag references an ID not present in this catalog. (Reflexive catalog-level defect -- this entry makes catalog incompleteness self-detectable.)
**FM-16** -- Entry Condition Absent: A named phase body carries no `Entry condition:` line in its PHASE BODY CONTRACT block. Tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. This FM entry makes entry-condition absence a named, inline-taggable defect class. A phase body that omits its entry condition SHALL be self-tagged; the tag SHALL appear as the first line of the PHASE BODY CONTRACT block.
**FM-17** -- Gate Register Drift: A gate statement (entry condition or exit condition) uses descriptive form ("Phase N is complete when:") where an obligation verb (SHALL) is required ("Phase N SHALL be declared complete when:"). Tag: `[GATE REGISTER DRIFT: "{actual text}" -> SHALL be declared complete | FM-17]`. This FM entry makes gate-position register drift a named defect distinct from general register violation (FM-14): FM-14 fires for job descriptions and slot contracts; FM-17 fires for gate positions specifically.

*FM-15, FM-16, and FM-17 address three distinct self-validation failures. FM-15: catalog references an absent ID. FM-16: a phase body has no entry condition. FM-17: a gate statement drifts to descriptive register. All three can be detected and tagged without external reviewer expertise.*

#### Entry Schema Contract

**FIRING ENTRY** -- every firing trigger entry SHALL contain all of the following slots:

```
Seq:                 [integer]
Trigger Name:        [approved vocabulary term]
CA-Ref:              [CA-NN identifier from Phase 1]
Tier:                [sync | async]
Layer:               [plugin step | automated flow | business rule | real-time workflow | classic workflow]
Condition (Taken):   [what MUST be true for this trigger to fire in this scenario]
Condition (Skipped): [what would cause this trigger NOT to fire]
Inputs:              [field/event consumed]
Outputs:             [field write / notification / record creation]
Side Effects:        [additional writes or spawned actions; "None" if absent]
Spawns:              [CA-NN of any cascade trigger; "None" if absent]
Anomaly Flag:        [none | storm | missing | cycle | FM-NN]
```

A missing slot SHALL be marked `[SLOT MISSING: {slot name} | FM-12]`.

**NON-FIRING ENTRY** -- every candidate that does NOT fire SHALL contain:

```
CA-Ref:              [CA-NN identifier]
Trigger Name:        [approved vocabulary term]
Condition (Taken):   [the condition under which this trigger would fire]
Condition (Skipped): [the specific condition preventing it in this scenario]
Verdict:             [CONFIRMED ABSENT | FLAGGED GAP]
FM Flag:             [FM-02 if FLAGGED GAP; "none" if CONFIRMED ABSENT]
```

---

### LIFECYCLE OVERVIEW

The following table SHALL precede all phases. All gate language in this table SHALL use formal obligation register. Entry condition cells SHALL use "SHALL NOT begin until:" form. Exit condition cells SHALL use "SHALL be declared complete when:" form. A cell using descriptive gate form SHALL be tagged `[FM-17]`.

| Phase | Name | Entry condition (SHALL NOT begin until) | Job | Exit condition (SHALL be declared complete when) |
|-------|------|-----------------------------------------|-----|--------------------------------------------------|
| 1 | Candidate Pre-scan | PROTOCOL PREAMBLE fully declared; scenario received; no trigger entry written | Identify all automation candidates; declare denominator N; open all three anomaly question slots | Denominator N stated; all CA-NN candidates listed; all three anomaly questions carry Status: OPEN |
| 2 | Trigger Enumeration | Phase 1 SHALL be declared complete; denominator N stated; all three anomaly questions carry Status: OPEN | Enumerate all N candidates as FIRING ENTRY or NON-FIRING ENTRY per schema; cascade side-effect writes spawn new rows | All N CA-NN candidates have a disposition; all automation-potential side-effect writes have spawned downstream rows |
| 3 | Anomaly Analysis | Phase 2 SHALL be declared complete; all N candidates enumerated; all cascade rows present | Close all three anomaly question slots with evidence-cited verdicts and remediation guidance | All three anomaly questions carry Status: CLOSED; each verdict cites evidence; each confirmed anomaly has remediation |
| 4 | Trigger Map Assembly | Phase 3 SHALL be declared complete; all three anomaly verdicts carry Status: CLOSED | Produce the trigger map with Seq, Trigger Name, CA-Ref, Tier, Anomaly Flag, Spawns columns | All firing triggers from Phase 2 appear in the table; all six columns populated per row |
| 5 | Denominator Closure | Phase 4 SHALL be declared complete; trigger map complete | Verify (FIRED + CONFIRMED ABSENT + FLAGGED GAP) = N arithmetic; state VERIFIED or tag CLOSURE MISMATCH | Closure formula stated; result declared VERIFIED or tagged `[CLOSURE MISMATCH: {count} != N | FM-09]` |

---

### Phase 1: Candidate Pre-scan

```
PHASE BODY CONTRACT -- Phase 1
Entry condition:  This phase SHALL NOT begin until: the PROTOCOL PREAMBLE is fully declared
                  (Platform Vocabulary Contract, FM Catalog, Entry Schema Contract all
                  present); the scenario is received; no trigger entry has been written.
Job:              Identify all automation candidates potentially affected by the Opportunity
                  Status field changing to Closed Won. Produce a numbered CA-NN list. Declare
                  the candidate denominator N. Open all three anomaly question slots with
                  Status: OPEN before the first CA entry is written.
Exit condition:   This phase SHALL be declared complete when: the denominator statement
                  "Candidate denominator: N = [count]" is present, all CA-NN candidates are
                  listed, and all three anomaly questions carry Status: OPEN.
```

**Anomaly questions** -- all three SHALL carry Status: OPEN before the first CA entry:

```
STORM QUESTION     Status: OPEN
  Does any single change event fire more than 3 automations in the same execution tier?
  Evidence: [to be cited in Phase 3]   Verdict: [PENDING]

MISSING QUESTION   Status: OPEN
  Is there an expected automation absent from the candidate list?
  Evidence: [to be cited in Phase 3]   Verdict: [PENDING]

CIRCULAR QUESTION  Status: OPEN
  Does any trigger chain produce a field write that re-fires an earlier trigger?
  Evidence: [to be cited in Phase 3]   Verdict: [PENDING]
```

For each candidate, state: `CA-NN: Name | Probable Type | Probable Tier | Evidence of Registration`

`Candidate denominator: N = [count]`

---

### Phase 2: Trigger Enumeration

```
PHASE BODY CONTRACT -- Phase 2
Entry condition:  This phase SHALL NOT begin until: Phase 1 SHALL be declared complete;
                  denominator N is stated; all three anomaly questions carry Status: OPEN.
Job:              Enumerate every trigger that fires, in the order it fires, using the FIRING
                  ENTRY schema. Side-effect writes with automation potential SHALL spawn a new
                  trigger row immediately following the producing row. Candidates that do not
                  fire SHALL use the NON-FIRING ENTRY schema. Vocabulary deviation SHALL be
                  tagged [VOCAB FAIL: {term} | FM-03]. A missing slot SHALL be tagged
                  [SLOT MISSING: {slot name} | FM-12]. A missing condition direction SHALL be
                  tagged [BRANCH BLIND: {entry name} | FM-04].
Exit condition:   This phase SHALL be declared complete when: every CA-NN candidate from
                  Phase 1 has a FIRING ENTRY or NON-FIRING ENTRY, and all side-effect field
                  writes with automation potential have spawned downstream trigger rows.
```

[ENUMERATE TRIGGERS HERE using FIRING ENTRY and NON-FIRING ENTRY schemas]

---

### Phase 3: Anomaly Analysis

```
PHASE BODY CONTRACT -- Phase 3
Entry condition:  This phase SHALL NOT begin until: Phase 2 SHALL be declared complete; all
                  N CA-NN candidates are enumerated; all automation-potential side-effect
                  writes have spawned downstream rows.
Job:              Close all three anomaly question slots. Each verdict SHALL cite specific
                  trigger rows, CA-IDs, or field writes from Phase 2. A verdict with no cited
                  evidence SHALL be tagged [EVIDENCE GAP | FM-05/FM-06/FM-07]. Every confirmed
                  anomaly SHALL include at least one concrete remediation step. An anomaly
                  confirmed without remediation SHALL be tagged [REMEDIATION ABSENT | FM-11].
Exit condition:   This phase SHALL be declared complete when: all three anomaly questions
                  carry Status: CLOSED, all verdicts cite evidence, and all CONFIRMED verdicts
                  carry a remediation step.
```

**STORM VERDICT**: Cite firing trigger rows counted. If total fires in the same tier > 3: CONFIRMED + debounce/filter remediation. If not: NOT DETECTED.

**MISSING TRIGGER VERDICT**: Reference FLAGGED GAP entries from Phase 2. If any: CONFIRMED + registration/condition remediation. If none: NOT DETECTED.

**CIRCULAR TRIGGER VERDICT**: Apply DFS back-edge detection on the Spawns graph constructed from Phase 2 rows:

```
Initialize: visited = {}  |  in-path = {}
For each trigger T not in visited:
  1. Add T to in-path
  2. For each downstream trigger U that T spawns:
     a. If U in in-path: [BACK-EDGE: T -> ... -> U | FM-07]
     b. If U not in visited: recurse on U
  3. Remove T from in-path; add T to visited
Graph property: DAG | CYCLIC
```

If CYCLIC: CONFIRMED + cycle-break condition remediation. If DAG: NOT DETECTED.

---

### Phase 4: Trigger Map Assembly

```
PHASE BODY CONTRACT -- Phase 4
Entry condition:  This phase SHALL NOT begin until: Phase 3 SHALL be declared complete; all
                  three anomaly questions carry Status: CLOSED.
Job:              Produce a trigger map table covering all firing triggers. The table SHALL
                  include six columns: Seq, Trigger Name, CA-Ref, Tier (sync/async), Anomaly
                  Flag, Spawns. A map missing the Tier or Spawns column SHALL be tagged
                  [FM-10].
Exit condition:   This phase SHALL be declared complete when: all firing triggers from Phase 2
                  appear in the table and all six columns are populated per row.
```

| Seq | Trigger Name | CA-Ref | Tier | Anomaly Flag | Spawns |
|-----|-------------|--------|------|-------------|--------|
| ... | ... | ... | ... | ... | ... |

---

### Phase 5: Denominator Closure

```
PHASE BODY CONTRACT -- Phase 5
Entry condition:  This phase SHALL NOT begin until: Phase 4 SHALL be declared complete; the
                  trigger map is present with all six columns populated.
Job:              Perform the arithmetic closure check: verify that FIRED + CONFIRMED ABSENT +
                  FLAGGED GAP = N, where N is the denominator declared in Phase 1. A mismatch
                  SHALL be tagged [CLOSURE MISMATCH: {actual count} != N | FM-09]. State the
                  result using the format below.
Exit condition:   This phase SHALL be declared complete when: the closure arithmetic is
                  stated in the format below, the sum is verified against N, and any mismatch
                  is tagged.
```

```
Candidates identified (Phase 1): N
FIRED:             [count]
CONFIRMED ABSENT:  [count]
FLAGGED GAP:       [count]
Sum:               [FIRED + CONFIRMED ABSENT + FLAGGED GAP]
Closure:           VERIFIED | [CLOSURE MISMATCH: {sum} != N | FM-09]
```
