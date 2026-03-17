# flow-trigger Skill Prompt Variations -- Round 9

Generated: 2026-03-15
Rubric: v9 (C-01 through C-33, aspirational /26 pts, max 116)
New criteria targeted: C-31 (cross-cutting invariant layer), C-32 (FM catalog distinguishes gate-register drift from entry-condition absence), C-33 (LIFECYCLE OVERVIEW as formal-gate zone)

---

## Gap Analysis Entering Round 9

### Pre-read of R8 Scorecard Evidence (Against Rubric v8, C-01 Through C-30)

R8 established three new criteria: C-28 (phase body self-contained), C-29 (FM catalog names entry-condition-absent), C-30 (gate statement register matches job statement register). R8 V-05 was the full-integration variation: PHASE BODY CONTRACT blocks with all three control artifacts in every phase body, FM-16 naming entry-condition-absence, FM-17 naming gate-register drift, and all gate statements using SHALL/MUST in the obligation position including the LIFECYCLE OVERVIEW table.

**What R8 V-05 structural features map to R9 rubric additions:**

| R8 V-05 Feature | R9 Criterion | Gap |
|-----------------|-------------|-----|
| Three numbered invariants embedded as inline prose in the opening paragraph, before the PROTOCOL PREAMBLE | C-31 PARTIAL | Invariants exist but are not a named, standalone INVARIANT LAYER section. They are co-located with the role statement and scenario instructions, not architecturally separated as a distinct named layer. A reviewer auditing cross-phase obligations cannot navigate directly to an INVARIANT LAYER header -- they must read the full opening block. The separation between PREAMBLE contract declarations and cross-phase structural invariants is not explicit. |
| FM-16 and FM-17 as separate entries in a flat FM catalog list | C-32 PARTIAL | Both entries exist. But no catalog sub-header or grouping names them as a distinct paired set of phase-boundary defect classes. A reviewer scanning for phase-boundary failure modes cannot immediately identify FM-16 + FM-17 as the specifically targeted pair without scanning all 17 entries. |
| LIFECYCLE OVERVIEW table with formal gate language and inline `[FM-17]` tagging rule in introductory prose | C-33 PASS (in R8 V-05) | R8 V-05 passes C-33 by construction. However, R8 V-03 and V-04 demonstrate that C-27 + C-30 can both pass while overview cells remain descriptive -- the LIFECYCLE OVERVIEW is a second independently driftable gate surface that C-33 closes. R9 tests whether a named FORMAL-GATE ZONE DECLARATION block makes C-33 more structurally compelled than inline prose. |

**Consequence**: R8 V-05 receives PARTIAL on C-31 (invariants exist but not as a named layer), PARTIAL on C-32 (FM-16 and FM-17 exist but not grouped), and PASS on C-33. R9 does not re-discover R8 features -- it adds exactly what R8 V-05 left structurally implicit.

### R9 Variation Map

Foundation carried forward from R8 (no rediscovery needed):
- Phase body self-contained via PHASE BODY CONTRACT blocks (C-28)
- FM-16 naming entry-condition-absence in the FM catalog (C-29)
- All gate statements using SHALL/MUST in the obligation position (C-30)
- FM-15 reflexive catalog-level defect entry (C-24)
- LIFECYCLE OVERVIEW table preceding all phases (C-27)
- Per-phase entry conditions (C-25), per-phase exit gates (C-23)
- Formal prescriptive register throughout (C-26)
- PROTOCOL PREAMBLE unifying FM catalog, entry schema, platform vocabulary (C-22)
- All prior aspirational criteria C-08 through C-21

| Variation | Axis | New Criteria Targeted | Hypothesis |
|-----------|------|----------------------|------------|
| V-01 | Invariant layer placement -- STRUCTURAL INVARIANT LAYER as a named section after the PROTOCOL PREAMBLE | C-31 | When the cross-phase structural invariants are hoisted from opening prose into a dedicated named section labeled "STRUCTURAL INVARIANT LAYER" positioned after the PROTOCOL PREAMBLE and before Phase 1, C-31 passes by construction. The section header makes the invariant layer independently navigable as a unit, distinct from the PREAMBLE's contract declarations. |
| V-02 | FM catalog grouping -- PHASE-BOUNDARY DEFECT CLASSES sub-header explicitly groups FM-16 and FM-17 | C-32 | When the FM catalog contains a named sub-header "PHASE-BOUNDARY DEFECT CLASSES" that explicitly groups FM-16 (Entry Condition Absent) and FM-17 (Gate Register Drift) as distinct, independently taggable entries, C-32 passes by construction. A reviewer scanning for phase-boundary failure modes finds both entries under a single navigable header. |
| V-03 | LIFECYCLE OVERVIEW zone declaration -- opens with a named FORMAL-GATE ZONE DECLARATION block | C-33 | When the LIFECYCLE OVERVIEW section opens with a labeled "FORMAL-GATE ZONE DECLARATION" block explicitly stating that entry and exit condition cells SHALL use obligation language and SHALL be tagged `[FM-17]` if descriptive, C-33 passes by construction via a named, independently auditable artifact rather than prose instruction. |
| V-04 | Named INVARIANT LAYER + FM catalog phase-boundary grouping | C-31, C-32 | The STRUCTURAL INVARIANT LAYER cross-references the FM IDs for violations (FM-16 for entry-condition absence, FM-17 for gate register drift). The FM catalog's PHASE-BOUNDARY DEFECT CLASSES sub-section resolves those FM IDs. The two artifacts form a closed reference loop: invariant obligation to FM ID to defect definition. |
| V-05 | Full integration: named INVARIANT LAYER + FM phase-boundary grouping + LIFECYCLE OVERVIEW formal-gate zone | C-31, C-32, C-33 | All three new criteria combined with the complete R8 V-05 foundation. The STRUCTURAL INVARIANT LAYER names cross-phase obligations; the PHASE-BOUNDARY DEFECT CLASSES sub-section names the defects when violated; the LIFECYCLE OVERVIEW FORMAL-GATE ZONE DECLARATION closes the second independently driftable gate surface. |

---

## V-01 -- Named INVARIANT LAYER Section: Cross-Phase Obligations as a Standalone Artifact

**Variation axis**: Invariant layer placement (C-31)
**Hypothesis**: R8 V-05 embedded three structural invariants in the opening paragraph as inline prose before the PROTOCOL PREAMBLE. C-31 requires a *named layer distinct from the PREAMBLE*. When the invariants are moved into a dedicated section labeled "STRUCTURAL INVARIANT LAYER" -- positioned after the PROTOCOL PREAMBLE and before Phase 1 -- the architectural separation becomes explicit. The PREAMBLE declares contracts; the INVARIANT LAYER declares cross-phase structural obligations. A reviewer auditing cross-phase consistency navigates directly to the section header. No FM catalog grouping (C-32) or LIFECYCLE OVERVIEW zone declaration (C-33) is added in this variation.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. You SHALL simulate which automations fire when the following record change occurs.

**SCENARIO**

Record: Dynamics 365 Opportunity (opportunity entity)
Change: `Status` field changed from `In Progress` to `Closed Won`
Context: Change made by a sales representative via the model-driven app Opportunity form, saved by user click.

You SHALL complete this analysis using the five-phase protocol defined below. You SHALL complete each phase in full before beginning the next. You SHALL NOT merge phases. You SHALL NOT advance to a later phase before the current phase's exit condition is met.

---

### PROTOCOL PREAMBLE

All three contract declarations below SHALL be present before the STRUCTURAL INVARIANT LAYER and before Phase 1 begins. No platform term SHALL appear before the Platform Vocabulary Contract. No FM tag SHALL appear before the FM Catalog. No entry slot SHALL be used before the Entry Schema Contract.

#### Platform Vocabulary Contract

Approved terms for this analysis (deviations SHALL be tagged `[VOCAB FAIL: {actual term} | FM-03]`):

- `sync plugin step` -- Dataverse plugin registered on the synchronous pipeline (pre-operation or post-operation, same transaction)
- `async plugin step` -- Dataverse plugin registered on the asynchronous pipeline (post-operation, separate system job)
- `automated flow` -- Power Automate flow triggered by a Dataverse record-change event (When a row is added, modified or deleted)
- `instant flow` -- Power Automate flow triggered manually or by another flow/app
- `scheduled flow` -- Power Automate flow triggered on a time-based recurrence
- `business rule` -- Model-driven app client-side or server-side rule evaluated on field value
- `real-time workflow` -- Legacy Dataverse synchronous workflow (deprecated but may be active)
- `classic workflow` -- Legacy Dataverse asynchronous background workflow

#### Failure Mode Catalog

Every inline FM tag in this output SHALL resolve to an entry in this catalog. An FM tag with no catalog entry SHALL be tagged `[FM-15: Catalog Opacity -- inline tag FM-NN references no catalog entry]`.

**FM-01** -- Undeclared Denominator: Phase 2 begins without N declared.
**FM-02** -- Silent Trigger Omission: A CA-NN from Phase 1 has no disposition in Phase 2.
**FM-03** -- Vocabulary Drift: Non-approved term. Tag: `[VOCAB FAIL: {term} | FM-03]`.
**FM-04** -- Branch Blindness: Entry has one condition slot without the other. Tag: `[BRANCH BLIND: {entry name} | FM-04]`.
**FM-05** -- Storm Evidence Gap: Storm verdict stated without citing trigger rows.
**FM-06** -- Missing-Trigger Evidence Gap: Missing trigger verdict without citing absent candidates.
**FM-07** -- Cycle Evidence Gap: Circular verdict without citing back-edge path.
**FM-08** -- Cascade Orphan: Automation-potential side-effect write has no downstream trigger row.
**FM-09** -- Denominator Closure Skip: No arithmetic closure check.
**FM-10** -- Trigger Map Incomplete: Tier or Spawns column absent.
**FM-11** -- Remediation Gap: Confirmed anomaly has no remediation. Tag: `[REMEDIATION ABSENT | FM-11]`.
**FM-12** -- Entry Schema Violation: Trigger entry missing declared slot. Tag: `[SLOT MISSING: {slot name} | FM-12]`.
**FM-13** -- Anomaly Gate Absent: Anomaly question not pre-opened before Phase 2.
**FM-14** -- Phase Register Violation: Obligation statement uses descriptive language. Tag: `[REGISTER FAIL: "{actual text}" -> SHALL/MUST | FM-14]`.
**FM-15** -- Catalog Opacity: FM tag references undeclared ID. (Reflexive catalog-level defect.)
**FM-16** -- Entry Condition Absent: A named phase body carries no `Entry condition:` line in its PHASE BODY CONTRACT block. Tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. Absence defect -- the line is missing entirely. Distinct from FM-17 (register drift).
**FM-17** -- Gate Register Drift: A gate statement uses descriptive form in the obligation position. Tag: `[GATE REGISTER DRIFT: "{actual text}" -> SHALL be declared complete | FM-17]`. Register drift defect -- gate statement present but wrong register. Distinct from FM-16 (absence) and FM-14 (job-description register violations).

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

**NON-FIRING ENTRY** -- every non-firing candidate SHALL contain:

```
CA-Ref:              [CA-NN identifier]
Trigger Name:        [approved vocabulary term or description]
Condition (Taken):   [what would cause this trigger to fire]
Condition (Skipped): [the specific condition preventing it in this scenario]
Verdict:             [CONFIRMED ABSENT | FLAGGED GAP]
FM Flag:             [FM-02 if FLAGGED GAP; "none" if CONFIRMED ABSENT]
```

---

### STRUCTURAL INVARIANT LAYER

The following numbered invariants are cross-phase structural obligations. They apply to every phase body in this analysis regardless of per-phase content. This section is architecturally distinct from the PROTOCOL PREAMBLE (which declares vocabulary, FM catalog, and entry schema contracts) and from Phase bodies (which carry per-phase analysis). A reviewer auditing cross-phase structural consistency SHALL consult this section as the canonical source for cross-phase obligations.

**Invariant 1 -- Phase body self-contained** [violation: FM-16]: Every phase body SHALL open with a PHASE BODY CONTRACT block containing exactly three labeled lines: `Entry condition:`, `Job:`, and `Exit condition:`. No phase body SHALL omit any of these three lines. A phase body containing Job and Exit condition but no Entry condition SHALL be tagged `[ENTRY CONDITION ABSENT: Phase N | FM-16]` as the first line of the PHASE BODY CONTRACT block.

**Invariant 2 -- FM-16 self-tagging compelled** [violation: FM-16]: Every phase body missing its `Entry condition:` line SHALL open with `[ENTRY CONDITION ABSENT: Phase N | FM-16]` as the first line. This tag is a structural defect declaration, not a comment. It SHALL appear in the output even if the remainder of the phase analysis is otherwise complete.

**Invariant 3 -- Gate register uniformity** [violation: FM-17]: All entry condition statements throughout this analysis SHALL use the form: `This phase SHALL NOT begin until: [precondition]`. All exit condition statements SHALL use the form: `This phase SHALL be declared complete when: [condition]`. Descriptive gate form ("Phase N is complete when:" without SHALL) SHALL be tagged `[GATE REGISTER DRIFT: "{actual text}" -> SHALL be declared complete | FM-17]`. This invariant applies to every gate statement in every phase body AND in the LIFECYCLE OVERVIEW table.

---

### LIFECYCLE OVERVIEW

The following table SHALL precede all phases. Gate cells comply with Invariant 3: entry condition cells use "SHALL NOT begin until:" form; exit condition cells use "SHALL be declared complete when:" form. A cell using descriptive gate form SHALL be tagged `[FM-17]`.

| Phase | Name | Entry condition (SHALL NOT begin until) | Job | Exit condition (SHALL be declared complete when) |
|-------|------|-----------------------------------------|-----|--------------------------------------------------|
| 1 | Candidate Pre-scan | PROTOCOL PREAMBLE fully declared; STRUCTURAL INVARIANT LAYER declared; scenario received; no trigger entry written | Identify all automation candidates; declare denominator N; open all three anomaly question slots | Denominator N stated; all CA-NN listed; all three anomaly questions carry Status: OPEN |
| 2 | Trigger Enumeration | Phase 1 SHALL be declared complete; N declared; all three anomaly questions carry Status: OPEN | Enumerate all N candidates per schema; cascade side-effect writes spawn new rows | All N CA-NN candidates have a disposition; all automation-potential side-effect writes have spawned downstream rows |
| 3 | Anomaly Analysis | Phase 2 SHALL be declared complete; all N candidates enumerated; all cascade rows present | Close all three anomaly slots with evidence-cited verdicts and remediation | All three anomaly questions carry Status: CLOSED; each verdict cites evidence; each confirmed anomaly has remediation |
| 4 | Trigger Map Assembly | Phase 3 SHALL be declared complete; all anomaly verdicts carry Status: CLOSED | Produce trigger map with Seq, Trigger Name, CA-Ref, Tier, Anomaly Flag, Spawns | All firing triggers appear in the table; all six columns populated per row |
| 5 | Denominator Closure | Phase 4 SHALL be declared complete; trigger map complete | Verify (FIRED + CONFIRMED ABSENT + FLAGGED GAP) = N | Closure formula stated; result declared VERIFIED or tagged `[CLOSURE MISMATCH: {count} != N | FM-09]` |

---

### Phase 1: Candidate Pre-scan

```
PHASE BODY CONTRACT -- Phase 1
Entry condition:  This phase SHALL NOT begin until: the PROTOCOL PREAMBLE is fully declared
                  (Platform Vocabulary Contract, FM Catalog, Entry Schema Contract all
                  present); the STRUCTURAL INVARIANT LAYER is declared; the scenario is
                  received; no trigger entry has been written.
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
                  trigger row immediately following the producing row. Non-firing candidates
                  SHALL use the NON-FIRING ENTRY schema. Vocabulary deviation SHALL be tagged
                  [VOCAB FAIL: {term} | FM-03]. Missing slot: [SLOT MISSING: {slot} | FM-12].
                  Missing condition direction: [BRANCH BLIND: {entry name} | FM-04].
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
                  anomaly SHALL include at least one concrete remediation step; absence of
                  remediation SHALL be tagged [REMEDIATION ABSENT | FM-11].
Exit condition:   This phase SHALL be declared complete when: all three anomaly questions
                  carry Status: CLOSED, all verdicts cite evidence, and all CONFIRMED verdicts
                  carry a remediation step.
```

**STORM VERDICT**: Cite firing trigger rows counted. If total fires in the same tier > 3: CONFIRMED + debounce/filter remediation. If not: NOT DETECTED.

**MISSING TRIGGER VERDICT**: Reference FLAGGED GAP entries from Phase 2. If any: CONFIRMED + remediation. If none: NOT DETECTED.

**CIRCULAR TRIGGER VERDICT**: Apply DFS back-edge detection on the Spawns graph. If back-edge: CONFIRMED + cycle-break remediation. If DAG: NOT DETECTED.

---

### Phase 4: Trigger Map Assembly

```
PHASE BODY CONTRACT -- Phase 4
Entry condition:  This phase SHALL NOT begin until: Phase 3 SHALL be declared complete; all
                  three anomaly questions carry Status: CLOSED.
Job:              Produce a trigger map covering all firing triggers. Columns SHALL be:
                  Seq, Trigger Name, CA-Ref, Tier (sync/async), Anomaly Flag, Spawns.
                  Missing Tier or Spawns: tag [FM-10].
Exit condition:   This phase SHALL be declared complete when: all firing triggers from Phase 2
                  appear in the table and all six columns are populated per row.
```

| Seq | Trigger Name | CA-Ref | Tier | Anomaly Flag | Spawns |
|-----|-------------|--------|------|-------------|--------|

---

### Phase 5: Denominator Closure

```
PHASE BODY CONTRACT -- Phase 5
Entry condition:  This phase SHALL NOT begin until: Phase 4 SHALL be declared complete;
                  trigger map present with all six columns populated.
Job:              Perform the arithmetic closure check: FIRED + CONFIRMED ABSENT +
                  FLAGGED GAP = N. Mismatch SHALL be tagged [CLOSURE MISMATCH: {count} != N
                  | FM-09].
Exit condition:   This phase SHALL be declared complete when: closure arithmetic is stated,
                  sum is verified against N, and any mismatch is tagged.
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

## V-02 -- FM Catalog Phase-Boundary Defect Class Grouping: PHASE-BOUNDARY DEFECT CLASSES Sub-Header

**Variation axis**: FM catalog structure (C-32)
**Hypothesis**: R8 V-05 had FM-16 and FM-17 as separate entries in a flat FM catalog list. Both entries existed and were distinct, but no catalog navigation made them identifiable as a paired set. C-32 requires the catalog to *structurally distinguish* gate-register drift from entry-condition absence -- which a flat list with no grouping only achieves implicitly. Adding a named sub-header "PHASE-BOUNDARY DEFECT CLASSES" that groups FM-16 and FM-17 together, with an explanatory note marking them as independently taggable and structurally distinct, makes C-32 pass by construction. No named INVARIANT LAYER section (C-31) or LIFECYCLE OVERVIEW zone declaration (C-33) is added.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. You SHALL simulate which automations fire when the following record change occurs.

**SCENARIO**

Record: Dynamics 365 Opportunity (opportunity entity)
Change: `Status` field changed from `In Progress` to `Closed Won`
Context: Change made by a sales representative via the model-driven app Opportunity form, saved by user click.

You SHALL complete this analysis using the five-phase protocol defined below. Three structural invariants govern every phase boundary:

**Invariant 1 -- Phase body self-contained**: Every phase body SHALL open with a PHASE BODY CONTRACT block containing three labeled lines: `Entry condition:`, `Job:`, and `Exit condition:`. A phase body missing its Entry condition line SHALL be tagged `[ENTRY CONDITION ABSENT: Phase N | FM-16]` as the first line.

**Invariant 2 -- FM-16 self-tagging compelled**: Every phase body missing its `Entry condition:` line SHALL open with `[ENTRY CONDITION ABSENT: Phase N | FM-16]` as a structural defect declaration. This tag SHALL appear even if the phase's analysis is otherwise complete.

**Invariant 3 -- Gate register uniformity**: All entry conditions SHALL use the form: `This phase SHALL NOT begin until: [precondition]`. All exit conditions SHALL use the form: `This phase SHALL be declared complete when: [condition]`. Descriptive gate form SHALL be tagged `[GATE REGISTER DRIFT: "{actual text}" -> SHALL be declared complete | FM-17]`.

---

### PROTOCOL PREAMBLE

All three contract declarations below SHALL be present before Phase 1 begins.

#### Platform Vocabulary Contract

Approved terms (deviations SHALL be tagged `[VOCAB FAIL: {actual term} | FM-03]`):

- `sync plugin step` -- Dataverse plugin registered on the synchronous pipeline
- `async plugin step` -- Dataverse plugin registered on the asynchronous pipeline
- `automated flow` -- Power Automate flow triggered by a Dataverse record-change event
- `instant flow` -- Power Automate flow triggered manually or by another flow/app
- `scheduled flow` -- Power Automate flow on a time-based recurrence
- `business rule` -- Model-driven app client-side or server-side rule evaluated on field value
- `real-time workflow` -- Legacy Dataverse synchronous workflow
- `classic workflow` -- Legacy Dataverse asynchronous background workflow

#### Failure Mode Catalog

Every inline FM tag SHALL resolve to an entry below. Unresolvable tag: `[FM-15: Catalog Opacity -- FM-NN references no catalog entry]`.

**FM-01** -- Undeclared Denominator: Phase 2 begins without N declared.
**FM-02** -- Silent Trigger Omission: CA-NN from Phase 1 has no disposition.
**FM-03** -- Vocabulary Drift: Non-approved term. Tag: `[VOCAB FAIL: {term} | FM-03]`.
**FM-04** -- Branch Blindness: Entry missing one condition direction. Tag: `[BRANCH BLIND: {name} | FM-04]`.
**FM-05** -- Storm Evidence Gap: Storm verdict without citing trigger rows.
**FM-06** -- Missing-Trigger Evidence Gap: Missing trigger verdict without citing absent candidates.
**FM-07** -- Cycle Evidence Gap: Circular verdict without citing back-edge path.
**FM-08** -- Cascade Orphan: Automation-potential side-effect write has no downstream trigger row.
**FM-09** -- Denominator Closure Skip: No arithmetic closure check.
**FM-10** -- Trigger Map Incomplete: Tier or Spawns column absent.
**FM-11** -- Remediation Gap: Confirmed anomaly without remediation. Tag: `[REMEDIATION ABSENT | FM-11]`.
**FM-12** -- Entry Schema Violation: Missing declared slot. Tag: `[SLOT MISSING: {slot name} | FM-12]`.
**FM-13** -- Anomaly Gate Absent: Anomaly question not pre-opened before Phase 2.
**FM-14** -- Phase Register Violation: Descriptive language in obligation position. Tag: `[REGISTER FAIL: "{actual text}" | FM-14]`.
**FM-15** -- Catalog Opacity: FM tag references undeclared ID. (Reflexive catalog-level defect.)

**--- PHASE-BOUNDARY DEFECT CLASSES ---**

*The following two FM entries are the phase-boundary defect class pair. They are grouped here as a named unit because: (a) both are independently taggable with distinct inline tag forms, (b) they are structurally independent -- a phase can exhibit FM-17 without FM-16, or FM-16 without FM-17, and (c) a reviewer auditing phase-boundary compliance should check this sub-section as a single navigable artifact. A catalog that lists FM-16 but has no separate FM entry for gate-register drift (FM-17) fails to make the two defect classes independently taggable.*

**FM-16** -- Entry Condition Absent: A named phase body carries no `Entry condition:` line in its PHASE BODY CONTRACT block. Tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. This is an *absence* defect -- the entry condition is entirely missing. Structurally distinct from FM-17: FM-16 fires when no entry condition exists; FM-17 fires when an entry condition exists but is written in descriptive register.

**FM-17** -- Gate Register Drift: A gate statement (entry condition or exit condition) uses descriptive form ("Phase N is complete when:") in the obligation position instead of formal obligation language ("Phase N SHALL be declared complete when:"). Tag: `[GATE REGISTER DRIFT: "{actual text}" -> SHALL be declared complete | FM-17]`. This is a *register drift* defect -- the gate statement is present but incorrect. Structurally distinct from FM-16 (absence) and from FM-14 (which fires for job-description and slot-contract register violations, not gate positions).

**--- END PHASE-BOUNDARY DEFECT CLASSES ---**

#### Entry Schema Contract

**FIRING ENTRY** -- every firing trigger entry SHALL contain all of the following slots:

```
Seq:                 [integer]
Trigger Name:        [approved vocabulary term]
CA-Ref:              [CA-NN from Phase 1]
Tier:                [sync | async]
Layer:               [plugin step | automated flow | business rule | real-time workflow | classic workflow]
Condition (Taken):   [what MUST be true for this trigger to fire]
Condition (Skipped): [what would cause this trigger NOT to fire]
Inputs:              [field/event consumed]
Outputs:             [field write / notification / record creation]
Side Effects:        [downstream writes or spawned actions; "None" if absent]
Spawns:              [CA-NN of cascade trigger; "None" if absent]
Anomaly Flag:        [none | storm | missing | cycle | FM-NN]
```

**NON-FIRING ENTRY** -- every non-firing candidate SHALL contain:

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

The following table SHALL precede all phases. Gate cells comply with Invariant 3: entry condition cells use "SHALL NOT begin until:" form; exit condition cells use "SHALL be declared complete when:" form. A descriptive gate cell SHALL be tagged `[FM-17]`.

| Phase | Name | Entry condition (SHALL NOT begin until) | Job | Exit condition (SHALL be declared complete when) |
|-------|------|-----------------------------------------|-----|--------------------------------------------------|
| 1 | Candidate Pre-scan | PROTOCOL PREAMBLE fully declared (including PHASE-BOUNDARY DEFECT CLASSES sub-section); scenario received; no trigger entry written | Identify candidates; declare N; open anomaly questions | Denominator N stated; all CA-NN listed; all three anomaly questions carry Status: OPEN |
| 2 | Trigger Enumeration | Phase 1 SHALL be declared complete; N declared; anomaly slots OPEN | Enumerate all N candidates per schema; cascade side-effects spawn rows | All N candidates have a disposition; all automation-potential side-effects have spawned rows |
| 3 | Anomaly Analysis | Phase 2 SHALL be declared complete; all N candidates enumerated | Close anomaly slots with evidence-cited verdicts and remediation | All slots CLOSED; confirmed anomalies have remediation |
| 4 | Trigger Map Assembly | Phase 3 SHALL be declared complete; all verdicts closed | Produce trigger map with six named columns | All firing triggers in table; all six columns populated |
| 5 | Denominator Closure | Phase 4 SHALL be declared complete; trigger map present | Verify (FIRED + CONFIRMED ABSENT + FLAGGED GAP) = N | Closure formula stated; VERIFIED or FM-09 tagged |

---

### Phase 1: Candidate Pre-scan

```
PHASE BODY CONTRACT -- Phase 1
Entry condition:  This phase SHALL NOT begin until: PROTOCOL PREAMBLE fully declared
                  (including FM catalog with PHASE-BOUNDARY DEFECT CLASSES sub-section);
                  scenario received; no trigger entry written.
Job:              Identify all automation candidates potentially affected by the Opportunity
                  Status field changing to Closed Won. Produce numbered CA-NN list. Declare
                  denominator N. Open all three anomaly question slots with Status: OPEN.
Exit condition:   This phase SHALL be declared complete when: denominator N stated, all
                  CA-NN listed, all three anomaly questions carry Status: OPEN.
```

```
STORM QUESTION     Status: OPEN   Evidence: [Phase 3]   Verdict: [PENDING]
MISSING QUESTION   Status: OPEN   Evidence: [Phase 3]   Verdict: [PENDING]
CIRCULAR QUESTION  Status: OPEN   Evidence: [Phase 3]   Verdict: [PENDING]
```

For each candidate: `CA-NN: Name | Probable Type | Probable Tier | Evidence of Registration`
`Candidate denominator: N = [count]`

---

### Phase 2: Trigger Enumeration

```
PHASE BODY CONTRACT -- Phase 2
Entry condition:  This phase SHALL NOT begin until: Phase 1 SHALL be declared complete;
                  denominator N stated; all three anomaly questions carry Status: OPEN.
Job:              Enumerate every trigger in firing order using FIRING ENTRY schema. Side-
                  effect writes with automation potential SHALL spawn downstream trigger rows.
                  Non-firing candidates use NON-FIRING ENTRY schema. Deviation: [VOCAB FAIL
                  | FM-03]. Missing slot: [SLOT MISSING | FM-12]. Missing condition direction:
                  [BRANCH BLIND | FM-04].
Exit condition:   This phase SHALL be declared complete when: all CA-NN candidates have a
                  FIRING ENTRY or NON-FIRING ENTRY; all automation-potential side-effects
                  have spawned downstream rows.
```

[ENUMERATE TRIGGERS HERE]

---

### Phase 3: Anomaly Analysis

```
PHASE BODY CONTRACT -- Phase 3
Entry condition:  This phase SHALL NOT begin until: Phase 2 SHALL be declared complete; all
                  N candidates enumerated; all cascade rows present.
Job:              Close all three anomaly question slots with evidence-anchored verdicts.
                  Each verdict SHALL cite specific rows, CA-IDs, or field writes from
                  Phase 2. No-evidence verdict: [EVIDENCE GAP | FM-05/FM-06/FM-07].
                  Confirmed anomaly without remediation: [REMEDIATION ABSENT | FM-11].
Exit condition:   This phase SHALL be declared complete when: all three anomaly questions
                  carry Status: CLOSED; all verdicts cite evidence; all CONFIRMED verdicts
                  have remediation.
```

**STORM VERDICT**: If > 3 fires in same tier: CONFIRMED + debounce remediation. Else: NOT DETECTED.
**MISSING TRIGGER VERDICT**: If FLAGGED GAP entries present: CONFIRMED + remediation. Else: NOT DETECTED.
**CIRCULAR TRIGGER VERDICT**: DFS back-edge detection on Spawns graph. If back-edge: CONFIRMED + cycle-break. Else: NOT DETECTED.

---

### Phase 4: Trigger Map Assembly

```
PHASE BODY CONTRACT -- Phase 4
Entry condition:  This phase SHALL NOT begin until: Phase 3 SHALL be declared complete; all
                  anomaly verdicts carry Status: CLOSED.
Job:              Produce trigger map: Seq, Trigger Name, CA-Ref, Tier, Anomaly Flag, Spawns.
                  Missing Tier or Spawns: [FM-10].
Exit condition:   This phase SHALL be declared complete when: all firing triggers appear in
                  the table and all six columns are populated per row.
```

| Seq | Trigger Name | CA-Ref | Tier | Anomaly Flag | Spawns |
|-----|-------------|--------|------|-------------|--------|

---

### Phase 5: Denominator Closure

```
PHASE BODY CONTRACT -- Phase 5
Entry condition:  This phase SHALL NOT begin until: Phase 4 SHALL be declared complete;
                  trigger map present with all six columns.
Job:              Arithmetic closure: FIRED + CONFIRMED ABSENT + FLAGGED GAP = N. Mismatch:
                  [CLOSURE MISMATCH: {count} != N | FM-09].
Exit condition:   This phase SHALL be declared complete when: closure arithmetic stated; sum
                  verified against N; any mismatch tagged.
```

```
Candidates (Phase 1): N
FIRED:             [count]
CONFIRMED ABSENT:  [count]
FLAGGED GAP:       [count]
Sum:               [count]
Closure:           VERIFIED | [CLOSURE MISMATCH: {sum} != N | FM-09]
```

---

## V-03 -- LIFECYCLE OVERVIEW Formal-Gate Zone: Named Zone Declaration Block

**Variation axis**: LIFECYCLE OVERVIEW zone annotation (C-33)
**Hypothesis**: R8 V-05 passed C-33 via an introductory sentence in the LIFECYCLE OVERVIEW section: "The following table SHALL precede all phases. All gate language in this table SHALL use formal obligation register..." The sentence was sufficient, but it was prose rather than a named structural artifact. V-03 tests whether opening the LIFECYCLE OVERVIEW with a dedicated "FORMAL-GATE ZONE DECLARATION" block -- a named, labeled, independently auditable artifact -- makes C-33 more strongly compelled and independently verifiable. The block states the obligation, the required gate forms, and the `[FM-17]` self-tagging rule as a standalone declaration. No named INVARIANT LAYER (C-31) or FM catalog grouping (C-32) is added.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. You SHALL simulate which automations fire when the following record change occurs.

**SCENARIO**

Record: Dynamics 365 Opportunity (opportunity entity)
Change: `Status` field changed from `In Progress` to `Closed Won`
Context: Change made by a sales representative via the model-driven app Opportunity form, saved by user click.

You SHALL complete this analysis using the five-phase protocol defined below. Three structural invariants govern every phase boundary:

**Invariant 1 -- Phase body self-contained**: Every phase body SHALL open with a PHASE BODY CONTRACT block containing three labeled lines: `Entry condition:`, `Job:`, and `Exit condition:`. A phase body missing its Entry condition line SHALL be tagged `[ENTRY CONDITION ABSENT: Phase N | FM-16]` as the first line.

**Invariant 2 -- FM-16 self-tagging compelled**: Every phase body missing its `Entry condition:` line SHALL open with `[ENTRY CONDITION ABSENT: Phase N | FM-16]` as a structural defect declaration. This tag SHALL appear even if the rest of the phase analysis is complete.

**Invariant 3 -- Gate register uniformity**: All entry conditions SHALL use the form: `This phase SHALL NOT begin until: [precondition]`. All exit conditions SHALL use the form: `This phase SHALL be declared complete when: [condition]`. Descriptive gate form SHALL be tagged `[GATE REGISTER DRIFT: "{actual text}" -> SHALL be declared complete | FM-17]`. This invariant applies in both phase bodies and the LIFECYCLE OVERVIEW table.

---

### PROTOCOL PREAMBLE

All three contract declarations below SHALL be present before Phase 1 begins.

#### Platform Vocabulary Contract

Approved terms (deviations SHALL be tagged `[VOCAB FAIL: {actual term} | FM-03]`):

- `sync plugin step` -- Dataverse plugin on the synchronous pipeline
- `async plugin step` -- Dataverse plugin on the asynchronous pipeline
- `automated flow` -- Power Automate flow triggered by a Dataverse record-change event
- `instant flow` -- Power Automate flow triggered manually or by another flow/app
- `scheduled flow` -- Power Automate flow on a time-based recurrence
- `business rule` -- Model-driven app client-side or server-side rule
- `real-time workflow` -- Legacy Dataverse synchronous workflow
- `classic workflow` -- Legacy Dataverse asynchronous background workflow

#### Failure Mode Catalog

Every inline FM tag SHALL resolve to an entry below. Unresolvable tag: `[FM-15: Catalog Opacity]`.

**FM-01** -- Undeclared Denominator.
**FM-02** -- Silent Trigger Omission.
**FM-03** -- Vocabulary Drift. Tag: `[VOCAB FAIL: {term} | FM-03]`.
**FM-04** -- Branch Blindness. Tag: `[BRANCH BLIND: {name} | FM-04]`.
**FM-05** -- Storm Evidence Gap.
**FM-06** -- Missing-Trigger Evidence Gap.
**FM-07** -- Cycle Evidence Gap.
**FM-08** -- Cascade Orphan.
**FM-09** -- Denominator Closure Skip.
**FM-10** -- Trigger Map Incomplete.
**FM-11** -- Remediation Gap. Tag: `[REMEDIATION ABSENT | FM-11]`.
**FM-12** -- Entry Schema Violation. Tag: `[SLOT MISSING: {slot} | FM-12]`.
**FM-13** -- Anomaly Gate Absent.
**FM-14** -- Phase Register Violation. Tag: `[REGISTER FAIL: "{text}" | FM-14]`.
**FM-15** -- Catalog Opacity. (Reflexive catalog-level defect.)
**FM-16** -- Entry Condition Absent: Phase body carries no `Entry condition:` line. Tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. Absence defect. Distinct from FM-17.
**FM-17** -- Gate Register Drift: Gate statement uses descriptive obligation form. Tag: `[GATE REGISTER DRIFT: "{text}" | FM-17]`. Fires in phase body gate positions AND in LIFECYCLE OVERVIEW gate cells. Distinct from FM-16 (absence) and FM-14 (job-description register violations).

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

```
FORMAL-GATE ZONE DECLARATION
This table is declared as a formal-gate zone. The following rules apply without
exception to every cell in the Entry condition and Exit condition columns:

  Rule 1: Entry condition cells SHALL use obligation form:
          "SHALL NOT begin until: [precondition]"

  Rule 2: Exit condition cells SHALL use obligation form:
          "SHALL be declared complete when: [condition]"

  Rule 3: A cell using descriptive state language ("Phase N is complete when
          [condition]" without an obligation verb) SHALL be tagged [FM-17:
          Gate Register Drift] inline within the cell, in addition to
          providing the descriptive text.

  Rule 4: No gate cell in this table SHALL be left blank. A blank entry-
          condition cell SHALL be tagged [FM-16]; a blank exit-condition cell
          SHALL be tagged [FM-09].

This declaration is independently auditable: a reviewer verifies every gate
cell in this table against these four rules without consulting the rubric.
The LIFECYCLE OVERVIEW table is the second independently driftable gate
surface in this analysis. Gate register compliance in phase bodies does not
imply compliance in this table; both surfaces are audited independently.
```

| Phase | Name | Entry condition (SHALL NOT begin until) | Job | Exit condition (SHALL be declared complete when) |
|-------|------|-----------------------------------------|-----|--------------------------------------------------|
| 1 | Candidate Pre-scan | PROTOCOL PREAMBLE fully declared; scenario received; no trigger entry written | Identify all candidates; declare N; open anomaly questions | Denominator N stated; all CA-NN listed; all three anomaly questions carry Status: OPEN |
| 2 | Trigger Enumeration | Phase 1 SHALL be declared complete; N declared; anomaly slots carry Status: OPEN | Enumerate all N candidates per schema; cascade side-effects spawn rows | All N candidates have a disposition; all automation-potential side-effects have spawned rows |
| 3 | Anomaly Analysis | Phase 2 SHALL be declared complete; all N candidates enumerated | Close anomaly slots with evidence-cited verdicts and remediation | All slots CLOSED; confirmed anomalies have remediation |
| 4 | Trigger Map Assembly | Phase 3 SHALL be declared complete; all verdicts carry Status: CLOSED | Produce trigger map with six named columns | All firing triggers in table; all six columns populated per row |
| 5 | Denominator Closure | Phase 4 SHALL be declared complete; trigger map present | Verify (FIRED + CONFIRMED ABSENT + FLAGGED GAP) = N | Closure formula stated; VERIFIED or `[CLOSURE MISMATCH: {count} != N | FM-09]` tagged |

---

### Phase 1: Candidate Pre-scan

```
PHASE BODY CONTRACT -- Phase 1
Entry condition:  This phase SHALL NOT begin until: PROTOCOL PREAMBLE fully declared;
                  scenario received; no trigger entry written.
Job:              Identify all automation candidates potentially affected by the Opportunity
                  Status field changing to Closed Won. Produce numbered CA-NN list. Declare
                  denominator N. Open all three anomaly question slots with Status: OPEN.
Exit condition:   This phase SHALL be declared complete when: denominator N stated, all
                  CA-NN listed, all three anomaly questions carry Status: OPEN.
```

```
STORM QUESTION     Status: OPEN
MISSING QUESTION   Status: OPEN
CIRCULAR QUESTION  Status: OPEN
```

For each candidate: `CA-NN: Name | Probable Type | Probable Tier | Evidence of Registration`
`Candidate denominator: N = [count]`

---

### Phase 2: Trigger Enumeration

```
PHASE BODY CONTRACT -- Phase 2
Entry condition:  This phase SHALL NOT begin until: Phase 1 SHALL be declared complete;
                  N stated; anomaly questions carry Status: OPEN.
Job:              Enumerate every trigger in firing order using FIRING ENTRY schema. Side-
                  effect writes with automation potential SHALL spawn downstream trigger rows.
                  Non-firing candidates use NON-FIRING ENTRY schema.
Exit condition:   This phase SHALL be declared complete when: all CA-NN candidates disposed;
                  all automation-potential side-effects have spawned downstream rows.
```

[ENUMERATE TRIGGERS HERE]

---

### Phase 3: Anomaly Analysis

```
PHASE BODY CONTRACT -- Phase 3
Entry condition:  This phase SHALL NOT begin until: Phase 2 SHALL be declared complete; all
                  N candidates enumerated; all cascade rows present.
Job:              Close all three anomaly question slots with evidence-anchored verdicts.
                  Each verdict SHALL cite rows, CA-IDs, or field writes from Phase 2.
Exit condition:   This phase SHALL be declared complete when: all three anomaly questions
                  carry Status: CLOSED; all verdicts cite evidence; all CONFIRMED verdicts
                  carry a remediation step.
```

**STORM VERDICT**: If > 3 fires in same tier: CONFIRMED + debounce remediation. Else: NOT DETECTED.
**MISSING TRIGGER VERDICT**: If FLAGGED GAP entries: CONFIRMED + remediation. Else: NOT DETECTED.
**CIRCULAR TRIGGER VERDICT**: DFS back-edge detection on Spawns graph. If back-edge: CONFIRMED + cycle-break. Else: NOT DETECTED.

---

### Phase 4: Trigger Map Assembly

```
PHASE BODY CONTRACT -- Phase 4
Entry condition:  This phase SHALL NOT begin until: Phase 3 SHALL be declared complete; all
                  anomaly verdicts carry Status: CLOSED.
Job:              Produce trigger map: Seq, Trigger Name, CA-Ref, Tier, Anomaly Flag, Spawns.
                  Missing Tier or Spawns: [FM-10].
Exit condition:   This phase SHALL be declared complete when: all firing triggers appear in
                  the table and all six columns are populated.
```

| Seq | Trigger Name | CA-Ref | Tier | Anomaly Flag | Spawns |
|-----|-------------|--------|------|-------------|--------|

---

### Phase 5: Denominator Closure

```
PHASE BODY CONTRACT -- Phase 5
Entry condition:  This phase SHALL NOT begin until: Phase 4 SHALL be declared complete;
                  trigger map present with all six columns.
Job:              Arithmetic closure: FIRED + CONFIRMED ABSENT + FLAGGED GAP = N.
Exit condition:   This phase SHALL be declared complete when: closure arithmetic stated;
                  sum verified against N; any mismatch tagged [FM-09].
```

```
Candidates (Phase 1): N
FIRED:             [count]
CONFIRMED ABSENT:  [count]
FLAGGED GAP:       [count]
Sum:               [count]
Closure:           VERIFIED | [CLOSURE MISMATCH: {sum} != N | FM-09]
```

---

## V-04 -- Named INVARIANT LAYER + FM Phase-Boundary Grouping: C-31 and C-32 Combined

**Variation axis**: Invariant layer placement + FM catalog phase-boundary grouping (C-31 + C-32)
**Hypothesis**: The STRUCTURAL INVARIANT LAYER (C-31) and the PHASE-BOUNDARY DEFECT CLASSES FM catalog sub-section (C-32) are architecturally complementary artifacts. The invariant layer declares structural obligations; the phase-boundary sub-section names the FM IDs that fire when those obligations are violated. When Invariant 1 cross-references FM-16 and Invariant 3 cross-references FM-17, and the FM catalog resolves both FM IDs under a named PHASE-BOUNDARY DEFECT CLASSES header, the two artifacts form a closed reference loop: obligation declaration to FM ID to defect definition. A reviewer can trace any structural obligation in the invariant layer to its specific defect class in the catalog and back. No LIFECYCLE OVERVIEW zone declaration (C-33) is added in this variation.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. You SHALL simulate which automations fire when the following record change occurs.

**SCENARIO**

Record: Dynamics 365 Opportunity (opportunity entity)
Change: `Status` field changed from `In Progress` to `Closed Won`
Context: Change made by a sales representative via the model-driven app Opportunity form, saved by user click.

You SHALL complete this analysis using the five-phase protocol defined below. You SHALL complete each phase in full before beginning the next. You SHALL NOT merge phases.

---

### PROTOCOL PREAMBLE

All three contract declarations below SHALL be present before the STRUCTURAL INVARIANT LAYER and before Phase 1 begins.

#### Platform Vocabulary Contract

Approved terms (deviations SHALL be tagged `[VOCAB FAIL: {actual term} | FM-03]`):

- `sync plugin step` -- Dataverse plugin on the synchronous pipeline (pre-operation or post-operation)
- `async plugin step` -- Dataverse plugin on the asynchronous pipeline (post-operation, separate system job)
- `automated flow` -- Power Automate flow triggered by a Dataverse record-change event
- `instant flow` -- Power Automate flow triggered manually or by another flow/app
- `scheduled flow` -- Power Automate flow on a time-based recurrence
- `business rule` -- Model-driven app client-side or server-side rule evaluated on field value
- `real-time workflow` -- Legacy Dataverse synchronous workflow
- `classic workflow` -- Legacy Dataverse asynchronous background workflow

#### Failure Mode Catalog

Every inline FM tag SHALL resolve to an entry below. Unresolvable tag: `[FM-15: Catalog Opacity -- FM-NN references no catalog entry]`.

**FM-01** -- Undeclared Denominator: Phase 2 begins without N declared.
**FM-02** -- Silent Trigger Omission: CA-NN from Phase 1 has no disposition.
**FM-03** -- Vocabulary Drift: Non-approved term. Tag: `[VOCAB FAIL: {term} | FM-03]`.
**FM-04** -- Branch Blindness: Entry missing one condition direction. Tag: `[BRANCH BLIND: {name} | FM-04]`.
**FM-05** -- Storm Evidence Gap: Storm verdict without citing trigger rows.
**FM-06** -- Missing-Trigger Evidence Gap: Missing trigger verdict without citing absent candidates.
**FM-07** -- Cycle Evidence Gap: Circular verdict without citing back-edge path.
**FM-08** -- Cascade Orphan: Automation-potential side-effect write has no downstream trigger row.
**FM-09** -- Denominator Closure Skip: No arithmetic closure check.
**FM-10** -- Trigger Map Incomplete: Tier or Spawns column absent.
**FM-11** -- Remediation Gap: Confirmed anomaly without remediation. Tag: `[REMEDIATION ABSENT | FM-11]`.
**FM-12** -- Entry Schema Violation: Missing declared slot. Tag: `[SLOT MISSING: {slot} | FM-12]`.
**FM-13** -- Anomaly Gate Absent: Anomaly question not pre-opened before Phase 2.
**FM-14** -- Phase Register Violation: Descriptive language in obligation position. Tag: `[REGISTER FAIL: "{text}" | FM-14]`.
**FM-15** -- Catalog Opacity: FM tag references undeclared ID. (Reflexive catalog-level defect.)

**--- PHASE-BOUNDARY DEFECT CLASSES ---**

*The following two FM entries are the phase-boundary defect class pair. They are grouped here as a named unit because: (a) both are independently taggable with distinct inline tag forms; (b) they are structurally independent defects -- FM-16 fires for absence, FM-17 fires for register drift, and both can occur independently; (c) a reviewer auditing phase-boundary compliance checks this sub-section as a single navigable artifact. The STRUCTURAL INVARIANT LAYER (below) cross-references both FM IDs; this sub-section is the resolution target for those cross-references.*

**FM-16** -- Entry Condition Absent: A named phase body carries no `Entry condition:` line in its PHASE BODY CONTRACT block. Tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. This is an *absence* defect. Cross-referenced by STRUCTURAL INVARIANT LAYER Invariants 1 and 2 as the defect ID for entry-condition omission. Structurally distinct from FM-17: FM-16 fires when no entry condition exists; FM-17 fires when an entry condition exists but uses the wrong register.

**FM-17** -- Gate Register Drift: A gate statement (entry condition or exit condition) uses descriptive form in the obligation position. Tag: `[GATE REGISTER DRIFT: "{actual text}" -> SHALL be declared complete | FM-17]`. This is a *register drift* defect. Cross-referenced by STRUCTURAL INVARIANT LAYER Invariant 3 as the defect ID for gate register violations. Fires in phase body gate positions AND in LIFECYCLE OVERVIEW gate cells. Structurally distinct from FM-16 (absence) and FM-14 (job-description register violations).

**--- END PHASE-BOUNDARY DEFECT CLASSES ---**

#### Entry Schema Contract

**FIRING ENTRY** -- every firing trigger entry SHALL contain all of the following slots:

```
Seq:                 [integer]
Trigger Name:        [approved vocabulary term]
CA-Ref:              [CA-NN from Phase 1]
Tier:                [sync | async]
Layer:               [plugin step | automated flow | business rule | real-time workflow | classic workflow]
Condition (Taken):   [what MUST be true for this trigger to fire]
Condition (Skipped): [what would cause this trigger NOT to fire]
Inputs:              [field/event consumed]
Outputs:             [field write / notification / record creation]
Side Effects:        [downstream writes or spawned actions; "None" if absent]
Spawns:              [CA-NN of cascade trigger; "None" if absent]
Anomaly Flag:        [none | storm | missing | cycle | FM-NN]
```

**NON-FIRING ENTRY** -- every non-firing candidate SHALL contain:

```
CA-Ref:              [CA-NN identifier]
Trigger Name:        [approved vocabulary term]
Condition (Taken):   [what would cause this trigger to fire]
Condition (Skipped): [the specific condition preventing it in this scenario]
Verdict:             [CONFIRMED ABSENT | FLAGGED GAP]
FM Flag:             [FM-02 if FLAGGED GAP; "none" if CONFIRMED ABSENT]
```

---

### STRUCTURAL INVARIANT LAYER

The following numbered invariants are cross-phase structural obligations. They apply simultaneously to every phase body in this analysis, regardless of per-phase content. This section is architecturally distinct from the PROTOCOL PREAMBLE above (which declares vocabulary, FM catalog, and entry schema contracts). The INVARIANT LAYER declares the structural properties that must hold at every phase boundary. Each invariant cross-references the FM ID from the PHASE-BOUNDARY DEFECT CLASSES sub-section that fires when the invariant is violated, creating a closed reference loop between obligation and defect definition.

**Invariant 1 -- Phase body self-contained** [violation: FM-16]: Every phase body SHALL open with a PHASE BODY CONTRACT block containing exactly three labeled lines: `Entry condition:`, `Job:`, and `Exit condition:`. No phase body SHALL omit any of these three lines. A phase body containing Job and Exit condition but no Entry condition SHALL be tagged `[ENTRY CONDITION ABSENT: Phase N | FM-16]` as the first line of the PHASE BODY CONTRACT block.

**Invariant 2 -- FM-16 self-tagging compelled** [violation: FM-16]: Every phase body missing its `Entry condition:` line SHALL open with `[ENTRY CONDITION ABSENT: Phase N | FM-16]` as the first line. This tag is a structural defect declaration, not a comment. It SHALL appear in the output even if the remainder of the phase analysis is complete.

**Invariant 3 -- Gate register uniformity** [violation: FM-17]: All entry condition statements throughout this analysis SHALL use the form: `This phase SHALL NOT begin until: [precondition]`. All exit condition statements SHALL use the form: `This phase SHALL be declared complete when: [condition]`. Descriptive gate form SHALL be tagged `[GATE REGISTER DRIFT: "{actual text}" -> SHALL be declared complete | FM-17]`. This invariant applies to every gate statement in every phase body AND in the LIFECYCLE OVERVIEW table.

---

### LIFECYCLE OVERVIEW

The following table SHALL precede all phases. Gate cells comply with Invariant 3: entry condition cells use "SHALL NOT begin until:" form; exit condition cells use "SHALL be declared complete when:" form. A descriptive gate cell SHALL be tagged `[FM-17]`.

| Phase | Name | Entry condition (SHALL NOT begin until) | Job | Exit condition (SHALL be declared complete when) |
|-------|------|-----------------------------------------|-----|--------------------------------------------------|
| 1 | Candidate Pre-scan | PROTOCOL PREAMBLE fully declared (including PHASE-BOUNDARY DEFECT CLASSES sub-section); STRUCTURAL INVARIANT LAYER declared; scenario received; no trigger entry written | Identify candidates; declare N; open anomaly questions | Denominator N stated; all CA-NN listed; all three anomaly questions carry Status: OPEN |
| 2 | Trigger Enumeration | Phase 1 SHALL be declared complete; N declared; anomaly slots carry Status: OPEN | Enumerate all N candidates per schema; cascade side-effects spawn rows | All N candidates have a disposition; all automation-potential side-effects have spawned rows |
| 3 | Anomaly Analysis | Phase 2 SHALL be declared complete; all N candidates enumerated | Close anomaly slots with evidence-cited verdicts and remediation | All slots CLOSED; confirmed anomalies have remediation |
| 4 | Trigger Map Assembly | Phase 3 SHALL be declared complete; all verdicts carry Status: CLOSED | Produce trigger map with six named columns | All firing triggers in table; all six columns populated |
| 5 | Denominator Closure | Phase 4 SHALL be declared complete; trigger map present | Verify (FIRED + CONFIRMED ABSENT + FLAGGED GAP) = N | Closure formula stated; VERIFIED or FM-09 tagged |

---

### Phase 1: Candidate Pre-scan

```
PHASE BODY CONTRACT -- Phase 1
Entry condition:  This phase SHALL NOT begin until: PROTOCOL PREAMBLE fully declared
                  (including PHASE-BOUNDARY DEFECT CLASSES sub-section in FM Catalog);
                  STRUCTURAL INVARIANT LAYER declared; scenario received; no trigger entry
                  written.
Job:              Identify all automation candidates potentially affected by the Opportunity
                  Status field changing to Closed Won. Produce numbered CA-NN list. Declare
                  denominator N. Open all three anomaly question slots with Status: OPEN.
Exit condition:   This phase SHALL be declared complete when: denominator N stated, all
                  CA-NN listed, all three anomaly questions carry Status: OPEN.
```

```
STORM QUESTION     Status: OPEN   Evidence: [Phase 3]   Verdict: [PENDING]
MISSING QUESTION   Status: OPEN   Evidence: [Phase 3]   Verdict: [PENDING]
CIRCULAR QUESTION  Status: OPEN   Evidence: [Phase 3]   Verdict: [PENDING]
```

For each candidate: `CA-NN: Name | Probable Type | Probable Tier | Evidence of Registration`
`Candidate denominator: N = [count]`

---

### Phase 2: Trigger Enumeration

```
PHASE BODY CONTRACT -- Phase 2
Entry condition:  This phase SHALL NOT begin until: Phase 1 SHALL be declared complete;
                  denominator N stated; all three anomaly questions carry Status: OPEN.
Job:              Enumerate every trigger in firing order using FIRING ENTRY schema. Side-
                  effect writes with automation potential SHALL spawn downstream trigger rows.
                  Non-firing candidates use NON-FIRING ENTRY schema.
Exit condition:   This phase SHALL be declared complete when: all CA-NN candidates have a
                  FIRING ENTRY or NON-FIRING ENTRY; all automation-potential side-effects
                  have spawned downstream rows.
```

[ENUMERATE TRIGGERS HERE]

---

### Phase 3: Anomaly Analysis

```
PHASE BODY CONTRACT -- Phase 3
Entry condition:  This phase SHALL NOT begin until: Phase 2 SHALL be declared complete; all
                  N candidates enumerated; all cascade rows present.
Job:              Close all three anomaly question slots with evidence-anchored verdicts.
                  Each verdict SHALL cite specific rows, CA-IDs, or field writes from
                  Phase 2. Confirmed anomaly without remediation: [REMEDIATION ABSENT | FM-11].
Exit condition:   This phase SHALL be declared complete when: all three anomaly questions
                  carry Status: CLOSED; all verdicts cite evidence; all CONFIRMED verdicts
                  have remediation.
```

**STORM VERDICT**: If > 3 fires in same tier: CONFIRMED + debounce remediation. Else: NOT DETECTED.
**MISSING TRIGGER VERDICT**: If FLAGGED GAP entries present: CONFIRMED + remediation. Else: NOT DETECTED.
**CIRCULAR TRIGGER VERDICT**: DFS back-edge detection on Spawns graph. If back-edge: CONFIRMED + cycle-break. Else: NOT DETECTED.

---

### Phase 4: Trigger Map Assembly

```
PHASE BODY CONTRACT -- Phase 4
Entry condition:  This phase SHALL NOT begin until: Phase 3 SHALL be declared complete; all
                  anomaly verdicts carry Status: CLOSED.
Job:              Produce trigger map: Seq, Trigger Name, CA-Ref, Tier, Anomaly Flag, Spawns.
                  Missing Tier or Spawns: [FM-10].
Exit condition:   This phase SHALL be declared complete when: all firing triggers appear in
                  the table and all six columns are populated per row.
```

| Seq | Trigger Name | CA-Ref | Tier | Anomaly Flag | Spawns |
|-----|-------------|--------|------|-------------|--------|

---

### Phase 5: Denominator Closure

```
PHASE BODY CONTRACT -- Phase 5
Entry condition:  This phase SHALL NOT begin until: Phase 4 SHALL be declared complete;
                  trigger map present with all six columns.
Job:              Arithmetic closure: FIRED + CONFIRMED ABSENT + FLAGGED GAP = N. Mismatch:
                  [CLOSURE MISMATCH: {count} != N | FM-09].
Exit condition:   This phase SHALL be declared complete when: closure arithmetic stated; sum
                  verified against N; any mismatch tagged.
```

```
Candidates (Phase 1): N
FIRED:             [count]
CONFIRMED ABSENT:  [count]
FLAGGED GAP:       [count]
Sum:               [count]
Closure:           VERIFIED | [CLOSURE MISMATCH: {sum} != N | FM-09]
```

---

## V-05 -- Full Integration: Named INVARIANT LAYER + FM Phase-Boundary Grouping + LIFECYCLE OVERVIEW Formal-Gate Zone

**Variation axis**: All three R9 criteria combined (C-31 + C-32 + C-33) with complete R8 V-05 foundation
**Hypothesis**: Full integration creates a closed structural audit chain across three distinct layers: (1) the STRUCTURAL INVARIANT LAYER section (C-31) declares cross-phase obligations before Phase 1 and outside the PREAMBLE; (2) the PHASE-BOUNDARY DEFECT CLASSES FM catalog sub-section (C-32) provides the FM-16 and FM-17 entries that the invariant layer cross-references; (3) the LIFECYCLE OVERVIEW FORMAL-GATE ZONE DECLARATION (C-33) applies Invariant 3's gate register rule explicitly to the overview table surface as a named, independently auditable zone. The three layers are mutually referencing: the INVARIANT LAYER references FM-16 and FM-17 by ID; the FM catalog resolves both under a named grouping header; the LIFECYCLE OVERVIEW zone declaration applies the same gate register rule to its gate cells, closing the second independently driftable surface. This configuration satisfies all criteria through R9.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. You SHALL simulate which automations fire when the following record change occurs.

**SCENARIO**

Record: Dynamics 365 Opportunity (opportunity entity)
Change: `Status` field changed from `In Progress` to `Closed Won`
Context: Change made by a sales representative via the model-driven app Opportunity form, saved by user click.

You SHALL complete this analysis using the five-phase protocol defined below. You SHALL complete each phase in full before beginning the next. You SHALL NOT merge phases. You SHALL NOT advance to a later phase before the current phase's exit condition is met.

---

### PROTOCOL PREAMBLE

All three contract declarations below SHALL be present before the STRUCTURAL INVARIANT LAYER and before Phase 1 begins. No platform term SHALL appear before the Platform Vocabulary Contract. No FM tag SHALL appear before the FM Catalog. No entry slot SHALL be used before the Entry Schema Contract. All obligation statements in this preamble use formal register; any deviation SHALL be tagged `[REGISTER FAIL: "{text}" | FM-14]`.

#### Platform Vocabulary Contract

Approved terms for this analysis (deviations SHALL be tagged `[VOCAB FAIL: {actual term} | FM-03]`):

- `sync plugin step` -- Dataverse plugin registered on the synchronous pipeline (pre-operation or post-operation, same transaction)
- `async plugin step` -- Dataverse plugin registered on the asynchronous pipeline (post-operation, separate system job)
- `automated flow` -- Power Automate flow triggered by a Dataverse record-change event (When a row is added, modified or deleted)
- `instant flow` -- Power Automate flow triggered manually or by another flow/app
- `scheduled flow` -- Power Automate flow triggered on a time-based recurrence
- `business rule` -- Model-driven app client-side or server-side rule evaluated on field value
- `real-time workflow` -- Legacy Dataverse synchronous workflow (deprecated but may be active)
- `classic workflow` -- Legacy Dataverse asynchronous background workflow

#### Failure Mode Catalog

Every inline FM tag in this output SHALL resolve to an entry in this catalog. An FM tag with no catalog entry SHALL be tagged `[FM-15: Catalog Opacity -- inline tag FM-NN references no catalog entry]`. This catalog is reflexive: FM-15 covers catalog incompleteness.

**FM-01** -- Undeclared Denominator: Phase 2 begins without N declared. Correction: Phase 1 SHALL declare N before Phase 2 begins.
**FM-02** -- Silent Trigger Omission: A CA-NN from Phase 1 has no disposition in Phase 2. Correction: Every CA-NN SHALL appear as FIRING or NON-FIRING.
**FM-03** -- Vocabulary Drift: A non-approved platform term appears in the output. Tag: `[VOCAB FAIL: {term} | FM-03]`.
**FM-04** -- Branch Blindness: A trigger entry has one condition slot without the other. Tag: `[BRANCH BLIND: {entry name} | FM-04]`.
**FM-05** -- Storm Evidence Gap: Storm verdict stated without citing trigger rows.
**FM-06** -- Missing-Trigger Evidence Gap: Missing trigger verdict without citing absent candidates.
**FM-07** -- Cycle Evidence Gap: Circular verdict without citing the back-edge path.
**FM-08** -- Cascade Orphan: Automation-potential side-effect write has no downstream trigger row.
**FM-09** -- Denominator Closure Skip: No arithmetic closure check after enumeration.
**FM-10** -- Trigger Map Incomplete: Trigger map missing Tier or Spawns column.
**FM-11** -- Remediation Gap: Confirmed anomaly has no remediation. Tag: `[REMEDIATION ABSENT | FM-11]`.
**FM-12** -- Entry Schema Violation: Trigger entry missing a declared schema slot. Tag: `[SLOT MISSING: {slot name} | FM-12]`.
**FM-13** -- Anomaly Gate Absent: An anomaly question is not pre-opened before Phase 2.
**FM-14** -- Phase Register Violation: Obligation statement uses descriptive language instead of SHALL/MUST/PROHIBITED/MAY NOT. Tag: `[REGISTER FAIL: "{actual text}" -> SHALL/MUST | FM-14]`.
**FM-15** -- Catalog Opacity: Inline FM tag references an ID not present in this catalog. (Reflexive catalog-level defect.)

**--- PHASE-BOUNDARY DEFECT CLASSES ---**

*The following two FM entries are the phase-boundary defect class pair. They are grouped here as a named unit because: (a) both are independently taggable with distinct inline tag forms; (b) they are structurally independent -- FM-16 fires for absence (no entry condition line), FM-17 fires for register drift (entry condition present but descriptively worded), and both can occur independently; (c) a reviewer auditing phase-boundary compliance checks this sub-section as a single navigable artifact. The STRUCTURAL INVARIANT LAYER below cross-references both FM IDs; this sub-section is the resolution target for those cross-references. The LIFECYCLE OVERVIEW FORMAL-GATE ZONE DECLARATION applies FM-17 tagging to the overview table surface.*

**FM-16** -- Entry Condition Absent: A named phase body carries no `Entry condition:` line in its PHASE BODY CONTRACT block. Tag: `[ENTRY CONDITION ABSENT: Phase N | FM-16]`. This is an *absence* defect -- the entry condition statement is entirely missing. Cross-referenced by STRUCTURAL INVARIANT LAYER Invariants 1 and 2 as the defect ID for entry-condition omission. Structurally distinct from FM-17: FM-16 fires when no entry condition exists; FM-17 fires when an entry condition exists but is written in descriptive register.

**FM-17** -- Gate Register Drift: A gate statement (entry condition or exit condition) uses descriptive form ("Phase N is complete when:") in the obligation position where a formal obligation verb is required ("Phase N SHALL be declared complete when:"). Tag: `[GATE REGISTER DRIFT: "{actual text}" -> SHALL be declared complete | FM-17]`. This is a *register drift* defect. Cross-referenced by STRUCTURAL INVARIANT LAYER Invariant 3 and the LIFECYCLE OVERVIEW FORMAL-GATE ZONE DECLARATION. Fires in phase body gate positions AND in LIFECYCLE OVERVIEW gate cells. Structurally distinct from FM-16 (absence) and FM-14 (job-description and slot-contract register violations).

**--- END PHASE-BOUNDARY DEFECT CLASSES ---**

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

### STRUCTURAL INVARIANT LAYER

The following numbered invariants are cross-phase structural obligations. They apply simultaneously to every phase body in this analysis, regardless of per-phase content. This section is architecturally distinct from the PROTOCOL PREAMBLE (which declares contracts: vocabulary, FM catalog, entry schema) and from the LIFECYCLE OVERVIEW (which provides navigable phase sequencing). The INVARIANT LAYER declares the structural properties that must hold at every phase boundary throughout the entire output. A reviewer auditing cross-phase structural consistency SHALL check this section first, then verify compliance in each phase body and in the LIFECYCLE OVERVIEW.

Each invariant cross-references the FM ID from the PHASE-BOUNDARY DEFECT CLASSES sub-section that fires when the invariant is violated.

**Invariant 1 -- Phase body self-contained** [violation: FM-16]: Every phase body in this output SHALL open with a PHASE BODY CONTRACT block containing exactly three labeled lines: `Entry condition:`, `Job:`, and `Exit condition:`. No phase body SHALL omit any of these three lines. A phase body containing Job and Exit condition but no Entry condition SHALL be tagged `[ENTRY CONDITION ABSENT: Phase N | FM-16]` as the first line of the PHASE BODY CONTRACT block.

**Invariant 2 -- FM-16 self-tagging compelled** [violation: FM-16]: Every phase body missing its `Entry condition:` line SHALL open with `[ENTRY CONDITION ABSENT: Phase N | FM-16]` as the first line. This tag is a structural defect declaration, not a comment. It SHALL appear in the output even if the remainder of the phase analysis is complete. An output that omits entry conditions AND omits FM-16 self-tags fails more severely than one that at least tags the gap.

**Invariant 3 -- Gate register uniformity** [violation: FM-17]: All entry condition statements throughout this output SHALL use the form: `This phase SHALL NOT begin until: [precondition]`. All exit condition statements SHALL use the form: `This phase SHALL be declared complete when: [condition]`. Descriptive gate form ("Phase N is complete when:" without a formal obligation verb) SHALL be tagged `[GATE REGISTER DRIFT: "{actual text}" -> SHALL be declared complete | FM-17]`. This invariant applies to every gate statement in every phase body AND in every gate cell of the LIFECYCLE OVERVIEW table. The LIFECYCLE OVERVIEW FORMAL-GATE ZONE DECLARATION (below) enforces this invariant on the overview table surface specifically.

---

### LIFECYCLE OVERVIEW

```
FORMAL-GATE ZONE DECLARATION
This table is declared as a formal-gate zone. The following rules apply without
exception to every cell in the Entry condition and Exit condition columns of
this table:

  Rule 1: Entry condition cells SHALL use obligation form:
          "SHALL NOT begin until: [precondition]"

  Rule 2: Exit condition cells SHALL use obligation form:
          "SHALL be declared complete when: [condition]"

  Rule 3: A cell using descriptive state language ("Phase N is complete when
          [condition]" without an obligation verb) SHALL be tagged [FM-17:
          Gate Register Drift] inline within the cell in addition to providing
          the descriptive text.

  Rule 4: No gate cell in this table SHALL be left blank. A blank entry-
          condition cell SHALL be tagged [FM-16]; a blank exit-condition cell
          SHALL be tagged [FM-09].

This declaration is independently auditable: a reviewer verifies every gate
cell in this table against these four rules without consulting the rubric or
the phase bodies. The LIFECYCLE OVERVIEW is the second independently driftable
gate surface in this analysis (after phase bodies). Gate register compliance
in phase bodies does not imply compliance in this table; both surfaces are
audited independently against Invariant 3 of the STRUCTURAL INVARIANT LAYER.
```

| Phase | Name | Entry condition (SHALL NOT begin until) | Job | Exit condition (SHALL be declared complete when) |
|-------|------|-----------------------------------------|-----|--------------------------------------------------|
| 1 | Candidate Pre-scan | PROTOCOL PREAMBLE fully declared (all three contracts including PHASE-BOUNDARY DEFECT CLASSES); STRUCTURAL INVARIANT LAYER declared; scenario received; no trigger entry written | Identify all automation candidates; declare denominator N; open all three anomaly question slots | Denominator N stated; all CA-NN candidates listed; all three anomaly questions carry Status: OPEN |
| 2 | Trigger Enumeration | Phase 1 SHALL be declared complete; denominator N stated; all three anomaly questions carry Status: OPEN | Enumerate all N candidates as FIRING ENTRY or NON-FIRING ENTRY per schema; cascade side-effect writes spawn downstream rows | All N CA-NN candidates have a disposition; all automation-potential side-effect writes have spawned downstream rows |
| 3 | Anomaly Analysis | Phase 2 SHALL be declared complete; all N candidates enumerated; all cascade rows present | Close all three anomaly question slots with evidence-cited verdicts and remediation guidance | All three anomaly questions carry Status: CLOSED; each verdict cites evidence; each confirmed anomaly has remediation |
| 4 | Trigger Map Assembly | Phase 3 SHALL be declared complete; all three anomaly verdicts carry Status: CLOSED | Produce trigger map with Seq, Trigger Name, CA-Ref, Tier, Anomaly Flag, Spawns columns | All firing triggers from Phase 2 appear in the table; all six columns populated per row |
| 5 | Denominator Closure | Phase 4 SHALL be declared complete; trigger map complete with all six columns | Verify (FIRED + CONFIRMED ABSENT + FLAGGED GAP) = N; state VERIFIED or tag CLOSURE MISMATCH | Closure formula stated; result declared VERIFIED or tagged `[CLOSURE MISMATCH: {count} != N | FM-09]` |

---

### Phase 1: Candidate Pre-scan

```
PHASE BODY CONTRACT -- Phase 1
Entry condition:  This phase SHALL NOT begin until: the PROTOCOL PREAMBLE is fully declared
                  (Platform Vocabulary Contract, FM Catalog with PHASE-BOUNDARY DEFECT
                  CLASSES sub-section, and Entry Schema Contract all present); the STRUCTURAL
                  INVARIANT LAYER is declared; the scenario is received; no trigger entry
                  has been written.
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
  Does any trigger chain produce a field write that re-fires an earlier trigger in the chain?
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
                  anomaly SHALL include at least one concrete remediation step. Confirmed
                  anomaly without remediation SHALL be tagged [REMEDIATION ABSENT | FM-11].
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
Job:              Produce a trigger map table covering all firing triggers. Columns SHALL be:
                  Seq, Trigger Name, CA-Ref, Tier (sync/async), Anomaly Flag, Spawns. A
                  missing Tier or Spawns column SHALL be tagged [FM-10].
Exit condition:   This phase SHALL be declared complete when: all firing triggers from Phase 2
                  appear in the table and all six columns are populated per row.
```

| Seq | Trigger Name | CA-Ref | Tier | Anomaly Flag | Spawns |
|-----|-------------|--------|------|-------------|--------|

---

### Phase 5: Denominator Closure

```
PHASE BODY CONTRACT -- Phase 5
Entry condition:  This phase SHALL NOT begin until: Phase 4 SHALL be declared complete;
                  trigger map present with all six columns populated per row.
Job:              Perform the arithmetic closure check: FIRED + CONFIRMED ABSENT +
                  FLAGGED GAP = N. Mismatch SHALL be tagged [CLOSURE MISMATCH: {count} != N
                  | FM-09].
Exit condition:   This phase SHALL be declared complete when: closure arithmetic is stated,
                  sum is verified against N, and any mismatch is tagged.
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

## Variation Summary

| Variation | Axis | C-31 | C-32 | C-33 | Distinguishing Feature vs R8 V-05 |
|-----------|------|------|------|------|-----------------------------------|
| V-01 | Named INVARIANT LAYER section | PASS | PARTIAL | PARTIAL | Dedicated "STRUCTURAL INVARIANT LAYER" section after PROTOCOL PREAMBLE; invariants are named, numbered, and navigable as a unit distinct from PREAMBLE contracts |
| V-02 | FM catalog PHASE-BOUNDARY DEFECT CLASSES sub-header | PARTIAL | PASS | PARTIAL | "PHASE-BOUNDARY DEFECT CLASSES" sub-header in FM catalog groups FM-16 + FM-17 as a named navigable pair with explanatory note marking structural independence |
| V-03 | LIFECYCLE OVERVIEW FORMAL-GATE ZONE DECLARATION block | PARTIAL | PARTIAL | PASS | "FORMAL-GATE ZONE DECLARATION" block opens LIFECYCLE OVERVIEW as a named, independently auditable structural artifact with four explicit rules and FM-17 inline tagging requirement |
| V-04 | Named INVARIANT LAYER + FM phase-boundary grouping | PASS | PASS | PARTIAL | STRUCTURAL INVARIANT LAYER cross-references FM-16 and FM-17 by ID; PHASE-BOUNDARY DEFECT CLASSES sub-section resolves both; closed reference loop between obligation and defect definition |
| V-05 | Full integration -- C-31 + C-32 + C-33 | PASS | PASS | PASS | All three new layers combined: STRUCTURAL INVARIANT LAYER references FM IDs; PHASE-BOUNDARY DEFECT CLASSES resolves them; LIFECYCLE OVERVIEW FORMAL-GATE ZONE DECLARATION applies Invariant 3 to the second independently driftable gate surface |
