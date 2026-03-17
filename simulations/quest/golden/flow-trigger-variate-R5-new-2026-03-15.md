# flow-trigger Skill Prompt Variations — Round 5 (Rubric v5)

**Skill**: flow-trigger — Simulate which automations fire when a record changes.
**Rubric**: v5 (C-01 through C-21, aspirational 14 pts, max 104)
**Date**: 2026-03-15
**New criteria targeted**: C-18 (FM catalog pre-declared), C-19 (entry schema contract before enumeration), C-20 (phase protocol with job descriptions), C-21 (platform term contract before use)

---

## Gap Analysis Entering Round 5

### Pre-read of R4 Scorecard Evidence (Against Rubric v4, C-01 Through C-17)

R4 best performers (V-01, V-04) achieved C-01–C-17. Three structural patterns appear in R4 output that the v5 rubric now crystallises into named criteria:

| Pattern | Where Observed in R4 | R4 Mechanism | R5 Gap (C-18/C-19/C-20/C-21) |
|---------|---------------------|--------------|-------------------------------|
| FM catalog declared in preamble | R4 V-01 FM-01–FM-17 block before roles | FM codes listed before Role A begins | C-18 requires the catalog to appear as a named PROTOCOL block, not embedded in role narrative. R4 had FM codes interleaved with role descriptions; C-18 requires a standalone FM block before the first analysis section. |
| Entry schemas declared implicitly via column headers | R4 V-01 Role B table column headers define the implicit schema | Column names carry slot requirements | C-19 requires explicit FIRING ENTRY and NON-FIRING ENTRY schemas with every slot named before the first numbered trigger row. An implicit schema via column headers fails C-19. |
| Phase structure via role labels | R4 "Role A / Role B / Role C / Role D / Role E" | Role names imply phases | C-20 requires each phase to have a stated **job description** — what the phase must *deliver* — not just a label. R4 role names ("Scanner", "Tracer") name the role but do not state the phase gate or job. |
| Vocabulary contract inside Role A | R4 V-01 "A-1 -- Vocabulary Contract" block | Contract appears as the first item in Role A | C-21 requires the platform term contract to appear BEFORE any platform-specific terms appear in the output — i.e., before Role A, not as the opening item of Role A. If Role A's task description uses the word "automated flow" before the contract is declared, C-21 fails. |

### What Rubric v5 Adds (C-18 Through C-21)

| ID | Criterion | Pattern Source in R4 | R5 Design Obligation |
|----|-----------|---------------------|----------------------|
| C-18 | FM catalog pre-declared | R4 FM block before roles | Move FM catalog to a standalone PROTOCOL PREAMBLE section that precedes ALL roles and ALL platform-specific language. The block is labeled, not embedded in prose. |
| C-19 | Entry schema contract declared before enumeration | R4 implicit via column headers | Write explicit FIRING ENTRY and NON-FIRING ENTRY schema contracts, each listing every required slot by name, before the first numbered trigger entry. |
| C-20 | Phase protocol with explicit phase job descriptions | R4 role labels (Scanner, Tracer, etc.) | Name each phase, assign a job description ("Phase N's job is to deliver X"), and state at least one gate condition for the closing phase. |
| C-21 | Platform term contract declared before use | R4 vocab contract inside Role A | Place PLATFORM TERM CONTRACT in the PROTOCOL PREAMBLE section, before any platform-specific term appears anywhere in the prompt. |

### R5 Variation Map

All four new criteria (C-18–C-21) target the *preamble layer* — the structural content declared before any trigger enumeration begins. The R5 challenge is making each criterion's pass condition structurally compelled by the prompt design, not dependent on the model choosing to comply.

| Variation | Axes | New Criteria Targeted | Hypothesis |
|-----------|------|-----------------------|------------|
| V-01 | FM catalog block structure | C-18, C-21 | Separating the FM catalog into a standalone pre-role block (not embedded in Role A) and pairing it with a PLATFORM TERM CONTRACT in the same preamble section satisfies C-18 and C-21 structurally. |
| V-02 | Dual-slot entry schema contract | C-19, C-16 | Declaring explicit FIRING ENTRY and NON-FIRING ENTRY schema contracts (with all slots named) before the first numbered row makes slot omissions schema violations rather than narrative gaps — structurally compels C-19. |
| V-03 | Phase protocol with job descriptions | C-20 | Replacing role labels with explicitly numbered phases, each carrying a one-sentence job description and a gate condition for the terminal phase, satisfies C-20 without changing analysis content. |
| V-04 | Contract Layer combining C-18 + C-19 + C-21 | C-18, C-19, C-21 | A single CONTRACT DECLARATION section at the top declares all three contracts (FM catalog, entry schemas, vocab list) before any role structure begins. Role structure begins only after the contract section is complete. |
| V-05 | Three-layer stack: Contract → Analysis → Closure | C-18, C-19, C-20, C-21 | Organising the entire output as three explicitly-labeled structural layers — CONTRACT LAYER, ANALYSIS LAYER, CLOSURE LAYER — with all four new contracts in the CONTRACT LAYER satisfies all four new criteria in a single architectural decision. |

**Foundation carried forward** (no rediscovery needed from R4):
- Complete trigger enumeration including non-firing entries (C-01)
- Firing order with sync-before-async rule (C-02)
- Input/output per trigger (C-03)
- Anomaly assessment for all three classes (C-04)
- Side effects enumerated per trigger (C-05)
- Trigger conditions and filters stated (C-06)
- Platform role grounded with domain terms (C-07)
- Anomaly remediation guidance on detections (C-08)
- Trigger map with exec tier and cascade link (C-09, C-15)
- Anomaly slots pre-opened before enumeration (C-10)
- Cascade completeness — side-effect writes spawn trigger rows (C-11)
- Self-annotating inline markers (C-12)
- Anomaly verdicts evidence-anchored (C-13)
- Candidate denominator pre-declared (C-14)
- Both trigger path and skip path documented per entry (C-16)
- Denominator closure check after enumeration (C-17)

---

## V-01 — FM Catalog as Protocol Preamble Block (Single-Axis: C-18 + C-21)

**Variation axis**: Role sequence — preamble layer restructure
**Hypothesis**: R4 placed the FM catalog inside or immediately before roles, making it ambiguous whether the catalog or the role structure was the governing layer. V-01 promotes the FM catalog to a named PROTOCOL PREAMBLE that precedes all role declarations. The PLATFORM TERM CONTRACT occupies the first block inside that preamble, before any platform-specific vocabulary appears in the prompt. This placement structurally compels C-18 (catalog before first analysis section) and C-21 (vocab contract before any platform terms appear).

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. You will analyse trigger automation for the scenario given to you. Follow the protocol below exactly. Complete each phase before starting the next. Do not merge phases.

---

### PROTOCOL PREAMBLE

*This section must be read and re-stated (abbreviated) at the top of your output before any trigger analysis begins. It governs every term, defect code, and format constraint that appears in phases below.*

---

#### PLATFORM TERM CONTRACT

The following terms are the only approved platform vocabulary for this analysis. Every trigger entry is assessed against this list. A term used in an output cell that does not appear here is a vocabulary deviation.

| Slot | Approved Terms |
|------|----------------|
| Trigger Type | `sync plugin step` \| `async plugin step` \| `instant flow` \| `automated flow` \| `scheduled flow` \| `Dataverse change trigger` \| `Copilot Studio topic trigger` \| `custom API webhook` |
| Execution Tier | `Sync` \| `Async` \| `Scheduled` |
| Latency | Sync: `Inline (blocks transaction)` \| Async: `~N min [standard\|premium] connector tier` (N required) \| Scheduled: `{cron expression or interval}` |
| Condition Branch | `Taken: {condition} -- {reason}` AND `Skipped: {condition} -- {reason}` |
| Input Payload | `{Entity}.{Field}` notation |
| Output Action | Opens with: `Sets` \| `Creates` \| `Deletes` \| `Sends notification via` \| `Calls HTTP` \| `Starts child flow:` \| `Posts adaptive card to` |

Violation tagging rule: When an unapproved term appears in any output cell, tag that cell: `[VOCAB FAIL: {actual term} | FM-03]`.

---

#### FAILURE MODE CATALOG (FM-01 through FM-14)

This catalog is declared before any analysis section. Every inline FM tag in the output resolves to a named entry here. Tags citing an FM code not in this catalog are themselves a violation of FM-14 (Catalog Opacity).

| ID | Name | Defect | Response |
|----|------|--------|----------|
| FM-01 | Undeclared Denominator | Enumeration begins without pre-scan count | Phase 1 declares N before any condition evaluation |
| FM-02 | Denominator Shrinkage | Conditions evaluated during pre-scan reduce candidate count | Pre-scan by entity/field/type only; `[FM-02: condition evaluated during pre-scan]` |
| FM-03 | Vocabulary Drift | Unapproved term in trigger entry | Replace with contract term; `[VOCAB FAIL: {term} | FM-03]` |
| FM-04 | Branch Blindness | Condition (Skipped) slot missing | Add skipped condition; `[BRANCH BLIND: {entry name} | FM-04]` |
| FM-05 | Input/Output Gap | Trigger entry missing input field or output action | Populate both slots; `[SLOT EMPTY: {slot} | FM-05]` |
| FM-06 | Verdict Without Evidence | Anomaly verdict stated without trigger row or field citation | Cite row number or field write; `[UNANCHORED: {verdict} | FM-06]` |
| FM-07 | Cascade Truncation | Chain ends without `[TERMINAL]` marker | Add terminal marker or `[CHAIN OPEN: CH-NN | FM-07]` |
| FM-08 | Denominator Closure Skip | Post-enumeration closure arithmetic missing | Add explicit count reconciliation after last trigger row |
| FM-09 | Tier Blur | Sync and async triggers mixed in same structural table | Separate structural tables; `[FM-09: wrong-tier trigger in table]` |
| FM-10 | Self-Gating | Analysis role produces verdicts on its own output | Gate role writes verdicts only; analysis role cannot approve itself |
| FM-11 | Side-Effect Orphan | Side-effect field write carries automation potential but no downstream trigger row | Add downstream trigger row or explicit exclusion |
| FM-12 | Schema Contract Absent | Trigger entry written before schema contract declared | Declare FIRING ENTRY and NON-FIRING ENTRY schemas before first entry |
| FM-13 | Anomaly Slot Closure Skip | Anomaly slot opened in Phase 1 never receives a verdict | Close all three slots with evidence before gate |
| FM-14 | Catalog Opacity | Inline FM tag references code not declared in this catalog | Any FM-NN tag with no matching catalog entry is itself a catalog defect |

---

### PHASE 1 — PRE-SCAN AND BOUNDARY DECLARATION

**Phase 1's job**: Establish the analysis boundary, enumerate all trigger candidates by entity/field/type without evaluating conditions, declare the candidate count N, and open all three anomaly question slots. Phase 1 is complete when N is stated and all three anomaly slots are OPEN.

**Output this block at the start of Phase 1:**

```
CHANGE SCOPE PIN
  Entity: {entity name}
  Field:  {field name}
  Change: {old value} -> {new value}
  Context: {initiating action}

CANDIDATE PRE-SCAN (FM-02 guard: entity/field/type match only -- no condition evaluation)
  CA-01 | {trigger name} | {type from PLATFORM TERM CONTRACT} | matched by: {entity/field/plugin name}
  CA-NN | ...
  Total candidates: N = {number}

ANOMALY QUESTION SLOTS
  STORM    | Status: OPEN | Question: Does any single field change cause more than one trigger of the same type to fire?
  MISSING  | Status: OPEN | Question: Are there expected automations for this change event that do not appear in the candidate list?
  CIRCULAR | Status: OPEN | Question: Does any trigger chain contain a back-edge (A fires B fires ... fires A)?
```

Do not evaluate any condition in this phase. Candidate scan terminates when entity/field/type matching is exhausted.

---

### PHASE 2 — ENTRY SCHEMA DECLARATION

**Phase 2's job**: Declare the structural schema for all trigger entries before the first numbered entry is written. Phase 2 is complete when both FIRING ENTRY and NON-FIRING ENTRY schemas are explicitly stated with every required slot named.

**Write these two schema blocks before the first trigger row:**

```
ENTRY SCHEMA CONTRACT

FIRING ENTRY (required slots -- all must be populated or tagged [SLOT EMPTY: {slot} | FM-05]):
  Row:                [sequential number]
  Trigger Name:       [name | type from PLATFORM TERM CONTRACT]
  Exec Tier:          [Sync | Async | Scheduled]
  Latency:            [from PLATFORM TERM CONTRACT latency column]
  Condition (Taken):  [Taken: {condition} -- {reason}]
  Condition (Skipped):[Skipped: {condition} -- {reason}]
  Input:              [{Entity}.{Field} notation]
  Output:             [action from PLATFORM TERM CONTRACT output column]
  Side Effects:       [{Entity}.{Field} = {value} | "none"]
  Spawns:             [Row N | "none"]
  Anomaly Flag:       [none | storm | missing | circular]
  CA-Ref:             [CA-NN from Phase 1]

NON-FIRING ENTRY (required slots):
  Row:                [sequential number]
  Trigger Name:       [name | type from PLATFORM TERM CONTRACT]
  Status:             NON-FIRING
  CA-Ref:             [CA-NN from Phase 1]
  Reason:             [explicit reason this trigger does not fire]
  Condition (Skipped):[Skipped: {condition} -- {reason}]
```

Schema violation marker: any entry missing a required slot carries `[SLOT EMPTY: {slot} | FM-05]` in that slot position. Any entry written without a declared schema carries `[FM-12: schema contract absent]` at the entry level.

---

### PHASE 3 — TRIGGER ENUMERATION

**Phase 3's job**: Produce one FIRING ENTRY or NON-FIRING ENTRY row for every CA-NN candidate from Phase 1. Every row conforms to the Phase 2 schema contract. Phase 3 is complete when all N candidates are accounted for with a row.

Produce the SYNC FIRING TABLE (FM-09 guard: async triggers in this table get `[FM-09]`), then the ASYNC FIRING TABLE, then the NON-FIRING TABLE.

At the end of Phase 3 write:

```
PHASE 3 HANDOFF
  Sync firing rows:     {count}
  Async firing rows:    {count}
  Non-firing rows:      {count}
  Total rows:           {sum}
  Cascade chains opened:{CH-NN list or "none"}
```

---

### PHASE 4 — CASCADE TRACE AND ANOMALY CLOSURE

**Phase 4's job**: (a) Trace every cascade chain from Phase 3 to a terminal event. (b) Close all three anomaly slots from Phase 1 with evidence. Phase 4 is complete when every open chain carries `[TERMINAL]` or `[CHAIN OPEN: CH-NN | FM-07]` AND all three anomaly slots carry a verdict with evidence citations.

**Cascade trace** (per chain):

```
Chain CH-{N}: {root trigger name}
  Step 1: {trigger} -> {output field write or action} | Spawns: {next trigger or TERMINAL}
  Step N: {trigger} -> {output} | [TERMINAL] -- reason: {termination condition}
  OR
  Step N: {trigger} -> {output} | [CHAIN OPEN: CH-NN | FM-07] -- reason: {why chain cannot terminate}
```

**Anomaly closure** (close each slot with evidence):

```
ANOMALY CLOSURE
  STORM:
    Evidence: {trigger rows N, N+1 citing same change; or "no simultaneous fires detected"}
    Verdict:  DETECTED | NOT DETECTED
    [If DETECTED] Remediation: {debounce strategy, de-duplication, or trigger condition refinement}

  MISSING:
    Evidence: {expected trigger name, expected entity/event, absence in Phase 3 rows; or "all expected triggers present"}
    Verdict:  DETECTED | NOT DETECTED
    [If DETECTED] Remediation: {register missing trigger, add flow, or document intentional absence}

  CIRCULAR:
    DFS traversal: {show in-path set at each step, or state "no back-edge found after full traversal"}
    Evidence: {back-edge citation: step X spawns trigger already in path; or "full traversal complete, no back-edge"}
    Verdict:  DETECTED | NOT DETECTED
    [If DETECTED] Remediation: {condition guard, cycle-break, or re-sequencing}
```

Verdicts without evidence citations carry `[UNANCHORED: {verdict} | FM-06]`. Anomaly slots not closed before the Phase 5 gate carry `[FM-13: slot not closed]`.

---

### PHASE 5 — DENOMINATOR CLOSURE AND GATE

**Phase 5's job**: Verify that (firing rows + non-firing rows) = N from Phase 1. Produce the trigger map summary. Issue a PASS or FAIL gate. Phase 5's gate is the final output; no analysis content follows it.

**Denominator closure:**

```
DENOMINATOR CLOSURE (FM-08 guard)
  N declared in Phase 1:    {number}
  Firing rows in Phase 3:   {count}
  Non-firing rows in Phase 3: {count}
  Total accounted:          {firing + non-firing}
  Match:                    YES | NO
  [If NO] Unaccounted candidates: {CA-NN list}
```

Discrepancy: `[DENOMINATOR GAP: N={declared} actual={actual} | FM-08]`

**Trigger map** (C-09 + C-15):

| Row | Trigger Name | Type | Exec Tier | Order | Anomaly Flag | Spawns |
|-----|-------------|------|-----------|-------|--------------|--------|
| ... | ... | ... | ... | ... | none/storm/missing/circular | Row N or none |

**Gate:**

```
GATE
  Anomaly slots closed:     YES | NO (list any OPEN)
  Denominator matched:      YES | NO
  FM-14 violations (invalid FM codes): {count or "none"}
  Schema violations (FM-12): {count or "none"}
  Overall: PASS | FAIL
  [If FAIL] Blocking issues: {list}
```

---

## V-02 — Dual-Slot Entry Schema Contract (Single-Axis: C-19)

**Variation axis**: Output format — entry schema contract as first-class structural gate
**Hypothesis**: R4 conveyed entry structure implicitly via column header definitions in table declarations. C-19 requires the FIRING ENTRY and NON-FIRING ENTRY schemas to be *explicitly declared* with every required slot named, before any enumeration begins. V-02 makes the schema contract a standalone protocol gate: enumeration cannot start until both schemas are written. This is a single-axis variation — the schema contract block is the new mechanism; role structure and FM catalog are carried from R4 foundations.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Analyse trigger automation for the scenario provided. Follow the four-phase protocol below. Each phase gate must be satisfied before the next phase begins.

---

#### PLATFORM TERM CONTRACT

Declare this at the top of your output. Approved platform vocabulary:

- Trigger types: `sync plugin step` | `async plugin step` | `instant flow` | `automated flow` | `scheduled flow` | `Dataverse change trigger` | `Copilot Studio topic trigger` | `custom API webhook`
- Execution tiers: `Sync` | `Async` | `Scheduled`
- Output action verbs: `Sets` | `Creates` | `Deletes` | `Sends notification via` | `Calls HTTP` | `Starts child flow:` | `Posts adaptive card to`

Vocabulary deviation: `[VOCAB FAIL: {actual term}]`

---

#### FAILURE MODE CATALOG

| FM | Name | Inline Tag |
|----|------|-----------|
| FM-01 | Undeclared Denominator | `[FM-01: enumeration begins without N]` |
| FM-02 | Branch Blindness | `[BRANCH BLIND: {entry} | FM-02]` |
| FM-03 | Input/Output Gap | `[SLOT EMPTY: {slot} | FM-03]` |
| FM-04 | Verdict Without Evidence | `[UNANCHORED: {verdict} | FM-04]` |
| FM-05 | Cascade Truncation | `[CHAIN OPEN: CH-NN | FM-05]` |
| FM-06 | Denominator Closure Skip | `[DENOMINATOR GAP: N={n} actual={a} | FM-06]` |
| FM-07 | Schema Contract Absent | `[FM-07: entry written before schema declared]` |
| FM-08 | Tier Blur | `[FM-08: wrong tier in table]` |
| FM-09 | Vocabulary Drift | `[VOCAB FAIL: {term}]` |
| FM-10 | Anomaly Slot Open at Gate | `[FM-10: anomaly slot not closed]` |
| FM-11 | Catalog Opacity | `[FM-11: FM tag references undeclared code]` |

---

#### ENTRY SCHEMA CONTRACT

*This section must appear in your output before the first numbered trigger entry. Both schemas are required. Missing schemas: `[FM-07]` on every entry in the affected table.*

**FIRING ENTRY SCHEMA** — Required slots. Absent slots tagged `[SLOT EMPTY: {slot name} | FM-03]`.

```
Row:                  [sequential integer]
Name:                 [trigger name]
Type:                 [approved type from PLATFORM TERM CONTRACT]
Exec Tier:            [Sync | Async | Scheduled]
Latency:              [inline-blocks-transaction | ~N min standard | ~N min premium | {cron}]
Condition (Taken):    [explicit condition that causes this trigger to fire]
Condition (Skipped):  [explicit condition that causes this trigger NOT to fire]
Input:                [{Entity}.{Field}]
Output:               [approved action verb + target]
Side Effects:         [{Entity}.{Field} = {value} | none]
Spawns:               [Row N (cascade continues) | none]
Anomaly Flag:         [none | storm | missing | circular]
CA-Ref:               [CA-NN]
```

**NON-FIRING ENTRY SCHEMA** — Required slots.

```
Row:                  [sequential integer]
Name:                 [trigger name]
Type:                 [approved type from PLATFORM TERM CONTRACT]
Status:               NON-FIRING
CA-Ref:               [CA-NN]
Reason:               [why this trigger does not fire in this scenario]
Condition (Skipped):  [the condition that is not met, stated explicitly]
```

Both schemas remain in your output throughout analysis. Every entry is audited against the schema it belongs to.

---

#### PHASE 1 — CANDIDATE ENUMERATION AND ANOMALY SLOT OPENING

**Gate**: N declared. All three anomaly slots OPEN. No conditions evaluated.

```
CHANGE SCOPE:
  {Entity}.{Field}: {old} -> {new}

CANDIDATE PRE-SCAN:
  CA-01 | {name} | {type} | match basis: {entity/field/plugin reference}
  ...
  N = {total count}

ANOMALY SLOTS (OPEN):
  [ ] Storm:    Does any single field change fire the same trigger type more than once?
  [ ] Missing:  Is there any expected automation for this change that is absent from the candidate list?
  [ ] Circular: Does any chain contain a back-edge (trigger A -> ... -> trigger A)?
```

---

#### PHASE 2 — TRIGGER ENUMERATION

**Gate**: Every CA-NN from Phase 1 has a row. Rows conform to declared FIRING ENTRY or NON-FIRING ENTRY schema. No anomaly verdicts in this phase.

Write each entry using the schema contracts above. Do not skip slots. Produce sync firing rows, then async firing rows, then non-firing rows.

End Phase 2 with:

```
PHASE 2 TALLY:
  Sync firing: {n}  |  Async firing: {n}  |  Non-firing: {n}  |  Total: {sum}
  Cascade chains: {CH-NN list or none}
```

---

#### PHASE 3 — CASCADE TRACE AND ANOMALY CLOSURE

**Gate**: Every open cascade chain resolves to `[TERMINAL]` or `[CHAIN OPEN: CH-NN | FM-05]`. All three anomaly slots closed with evidence.

For each cascade chain from Phase 2:

```
Chain CH-{N} | Root: {trigger name}
  Step 1: {name} | Output: {field write or action} | Spawns: {next trigger name or TERMINAL}
  ...
  Step N: {name} | Output: {action} | [TERMINAL]: {termination reason}
```

Anomaly closure (cite Phase 2 row numbers and chain steps as evidence):

```
[x] Storm:    Verdict: DETECTED | NOT DETECTED
              Evidence: {row citations or "no simultaneous fires across Phase 2 rows"}
              [If DETECTED] Remediation: {concrete fix}

[x] Missing:  Verdict: DETECTED | NOT DETECTED
              Evidence: {expected trigger, absence confirmation}
              [If DETECTED] Remediation: {concrete fix}

[x] Circular: DFS trace: {show in-path set steps or "full traversal, no back-edge"}
              Verdict: DETECTED | NOT DETECTED
              Evidence: {back-edge or traversal completion}
              [If DETECTED] Remediation: {concrete fix}
```

Verdicts without evidence: `[UNANCHORED: {verdict} | FM-04]`

---

#### PHASE 4 — DENOMINATOR CLOSURE AND TRIGGER MAP

**Gate (Phase 4's job)**: Verify (firing + non-firing) = N. Produce trigger map. Issue PASS or FAIL. No new analysis after this gate.

```
DENOMINATOR CHECK:
  N (Phase 1):             {n}
  Firing (Phase 2):        {n}
  Non-firing (Phase 2):    {n}
  Total:                   {sum}
  Result: MATCHED | GAP -- {unaccounted CA-NN list}
```

Trigger map:

| Row | Name | Type | Exec Tier | Latency | Anomaly Flag | Spawns |
|-----|------|------|-----------|---------|--------------|--------|
| ... | ... | ... | ... | ... | ... | ... |

```
GATE:
  Anomaly slots:       CLOSED | {list open}
  Denominator:         MATCHED | GAP
  Schema violations:   {count | none}
  Vocab violations:    {count | none}
  FM-11 violations:    {count | none}
  OVERALL: PASS | FAIL
```

---

## V-03 — Phase Protocol with Explicit Job Descriptions (Single-Axis: C-20)

**Variation axis**: Lifecycle emphasis — phase protocol as the primary structural device
**Hypothesis**: R4 used "Role A / Role B / Role C / Role D / Role E" labels to sequence analysis. Labels name the performer but do not state what each phase must *deliver* or what makes the phase complete. C-20 requires each phase to carry a job description — a one-sentence statement of what the phase must produce — and a gate condition for at minimum the final phase. V-03 replaces role labels with phase labels, each with a stated job. The content of each phase (pre-scan, enumeration, cascade, anomaly closure, gate) is identical to R4 best performers; only the framing changes.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Analyse trigger automation for the scenario provided. The analysis is divided into five phases. Before beginning each phase, re-state its job description. Complete a phase's deliverable before starting the next.

---

#### PLATFORM TERM CONTRACT

State this at the top of your response before any platform-specific vocabulary appears.

Approved terms:

| Category | Approved Values |
|----------|----------------|
| Trigger type | `sync plugin step` \| `async plugin step` \| `instant flow` \| `automated flow` \| `scheduled flow` \| `Dataverse change trigger` \| `Copilot Studio topic trigger` \| `custom API webhook` |
| Execution tier | `Sync` \| `Async` \| `Scheduled` |
| Output verb | `Sets` \| `Creates` \| `Deletes` \| `Sends notification via` \| `Calls HTTP` \| `Starts child flow:` \| `Posts adaptive card to` |

Non-conforming terms: `[VOCAB FAIL: {actual term}]`

---

#### FAILURE MODE CATALOG (FM-01 through FM-12)

Declared before Phase 1 begins. All FM tags in phase output resolve to this catalog.

| ID | Name | Description | Inline Tag |
|----|------|-------------|-----------|
| FM-01 | Undeclared Denominator | N not stated before enumeration | `[FM-01]` |
| FM-02 | Denominator Shrinkage | Condition evaluated in pre-scan | `[FM-02: condition in pre-scan]` |
| FM-03 | Vocabulary Drift | Unapproved term used | `[VOCAB FAIL: {term}]` |
| FM-04 | Branch Blindness | Condition (Skipped) absent | `[BRANCH BLIND: {entry} | FM-04]` |
| FM-05 | Slot Gap | Required entry slot empty | `[SLOT EMPTY: {slot} | FM-05]` |
| FM-06 | Verdict Orphan | Anomaly verdict without evidence | `[UNANCHORED: {verdict} | FM-06]` |
| FM-07 | Open Chain | Cascade chain without terminal | `[CHAIN OPEN: CH-NN | FM-07]` |
| FM-08 | Closure Skip | Denominator arithmetic absent | `[FM-08]` |
| FM-09 | Tier Blur | Sync in async table or vice versa | `[FM-09: tier mismatch]` |
| FM-10 | Side-Effect Orphan | Side-effect write with downstream potential, no spawn row | `[FM-11: side effect not spawned]` |
| FM-11 | Slot Open at Gate | Anomaly slot not closed before Phase 5 | `[FM-11: slot open at gate]` |
| FM-12 | Schema Absent | Entry written before schema contract | `[FM-12]` |

---

#### ENTRY SCHEMA CONTRACT

Both schemas are declared here, before Phase 1. Entries not conforming to their schema carry `[SLOT EMPTY: {slot} | FM-05]`.

**FIRING ENTRY**: Row | Name | Type | Exec Tier | Latency | Condition (Taken) | Condition (Skipped) | Input | Output | Side Effects | Spawns | Anomaly Flag | CA-Ref

**NON-FIRING ENTRY**: Row | Name | Type | Status=NON-FIRING | CA-Ref | Reason | Condition (Skipped)

---

### PHASE 1 — PRE-SCAN

**Job**: Identify every automation trigger candidate in the scenario by name, type, and match basis — without evaluating conditions. Declare the total candidate count N. Open all three anomaly question slots.

**Phase 1 is complete when**: N is stated and three anomaly slots are open.

**Deliverable**:

```
CHANGE SCOPE: {Entity}.{Field} {old} -> {new} | {initiating action}

PRE-SCAN (entity/field/type match only; no condition evaluation):
  CA-01 | {name} | {type} | {match basis}
  ...
  N = {count}

ANOMALY SLOTS:
  [ ] Storm   -- OPEN: Does one change fire the same trigger type more than once?
  [ ] Missing -- OPEN: Are expected automations absent from the candidate list?
  [ ] Circular -- OPEN: Does any cascade chain loop back to a prior trigger?
```

---

### PHASE 2 — ENUMERATION

**Job**: Produce one FIRING ENTRY or NON-FIRING ENTRY row for every candidate from Phase 1. Every row conforms to the schema declared in the ENTRY SCHEMA CONTRACT above.

**Phase 2 is complete when**: All N candidates have a row. Firing + non-firing count = N.

Write sync firing rows first (FM-09: async triggers here get `[FM-09: tier mismatch]`), then async firing rows, then non-firing rows.

At end of Phase 2:

```
PHASE 2 TALLY: Sync={n} | Async={n} | Non-firing={n} | Total={n}
Cascade chains opened: {CH-NN -> root trigger | none}
```

---

### PHASE 3 — CASCADE TRACE

**Job**: Walk every cascade chain from Phase 2 to its terminal event. Mark each chain `[TERMINAL]` or `[CHAIN OPEN: CH-NN | FM-07]`.

**Phase 3 is complete when**: Every chain has a terminal marker.

Per chain:

```
CH-{N}: {root trigger}
  Step 1: {trigger} -> {output} | next: {trigger name or TERMINAL}
  Step N: {trigger} -> {output} | [TERMINAL]: {reason}
```

Unresolvable chain: `[CHAIN OPEN: CH-NN | FM-07]: {why termination cannot be determined}`

---

### PHASE 4 — ANOMALY CLOSURE

**Job**: Close all three anomaly slots from Phase 1 with evidence drawn from Phase 2 rows and Phase 3 chain steps. For each detection, provide a concrete remediation.

**Phase 4 is complete when**: All three anomaly slots are closed with verdict + evidence.

```
[x] Storm:
    Evidence: {Phase 2 row citations or "no multiple-fire pattern detected"}
    Verdict:  DETECTED | NOT DETECTED
    [If DETECTED] Remediation: {debounce / dedup / condition filter}

[x] Missing:
    Evidence: {expected trigger name, expected event, Phase 2 row showing absence}
    Verdict:  DETECTED | NOT DETECTED
    [If DETECTED] Remediation: {register trigger / create flow / document intentional gap}

[x] Circular:
    DFS: {in-path set steps; or "traversal complete, no back-edge found"}
    Evidence: {back-edge trigger row; or "no cycle in full traversal"}
    Verdict:  DETECTED | NOT DETECTED
    [If DETECTED] Remediation: {condition guard / cycle-break / re-sequence}
```

Verdicts without evidence: `[UNANCHORED: {verdict} | FM-06]`

---

### PHASE 5 — DENOMINATOR CLOSURE AND GATE

**Job**: Verify that all N candidates are accounted for. Produce the trigger map. Issue PASS or FAIL. No new analysis content appears after this phase.

**Phase 5's gate condition**: (firing + non-firing) = N AND all anomaly slots closed AND no open FM violations.

```
DENOMINATOR CLOSURE:
  N declared (Phase 1):       {n}
  Firing rows (Phase 2):      {n}
  Non-firing rows (Phase 2):  {n}
  Accounted:                  {sum}
  Result: MATCHED | GAP
  [If GAP] Unaccounted: {CA-NN list}
```

Trigger map:

| Row | Name | Type | Exec Tier | Latency | Anomaly | Spawns |
|-----|------|------|-----------|---------|---------|--------|

```
GATE:
  Anomaly slots closed:    YES | NO -- {list open}
  Denominator matched:     YES | NO
  Vocab violations:        {n | none}
  Schema violations:       {n | none}
  FM code violations:      {n | none}
  OVERALL: PASS | FAIL
  [If FAIL]: {blocking issue list}
```

---

## V-04 — CONTRACT LAYER: FM Catalog + Entry Schema + Vocab (C-18 + C-19 + C-21)

**Variation axis**: Role sequence + output format — CONTRACT LAYER before role structure
**Hypothesis**: R4's best performers (V-01, V-03) declared FM catalogs and vocab contracts *within* role definitions (FM block before Role A, vocab inside Role A). C-18, C-19, and C-21 require these contracts to appear before any role structure or analysis begins. V-04 introduces a CONTRACT DECLARATION section that precedes all roles and contains all three contracts. Role structure begins only after the CONTRACT DECLARATION is complete. This single architectural change satisfies C-18, C-19, and C-21 simultaneously.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Before beginning any trigger analysis, produce the CONTRACT DECLARATION section below in its entirety. Then proceed through the four analysis roles. No role may reference a concept, term, or FM code that is not declared in the CONTRACT DECLARATION.

---

### CONTRACT DECLARATION

*Write this section first, in full, before any trigger analysis begins.*

---

#### CONTRACT 1 — PLATFORM TERM CONTRACT

The following terms govern all trigger entries. Terms not on this list are vocabulary deviations; tag the cell: `[VOCAB FAIL: {actual term}]`.

```
APPROVED TRIGGER TYPES:
  sync plugin step
  async plugin step
  instant flow
  automated flow
  scheduled flow
  Dataverse change trigger
  Copilot Studio topic trigger
  custom API webhook

APPROVED EXECUTION TIERS:
  Sync    -- inline, blocks transaction
  Async   -- queued, ~N min latency (N required)
  Scheduled -- {cron or interval}

APPROVED OUTPUT ACTION VERBS:
  Sets | Creates | Deletes | Sends notification via |
  Calls HTTP | Starts child flow: | Posts adaptive card to
```

---

#### CONTRACT 2 — FAILURE MODE CATALOG (FM-01 through FM-13)

All inline FM tags in this analysis resolve to an entry in this catalog. A tag citing an FM code not listed here is itself a defect: `[FM-13: undeclared FM code cited]`.

```
FM-01  Undeclared Denominator      N not stated before enumeration begins
FM-02  Denominator Shrinkage       Condition evaluated in pre-scan reduces candidate count
FM-03  Vocabulary Drift            Unapproved platform term in output cell
FM-04  Branch Blindness            Condition (Skipped) slot absent from entry
FM-05  Slot Gap                    Required entry slot empty or unpopulated
FM-06  Verdict Orphan              Anomaly verdict stated without evidence citation
FM-07  Cascade Truncation          Chain ends without [TERMINAL] or [CHAIN OPEN]
FM-08  Denominator Closure Skip    Post-enumeration arithmetic check absent
FM-09  Tier Blur                   Sync trigger in async table or vice versa
FM-10  Side-Effect Orphan          Downstream-automation-bearing side effect lacks spawn row
FM-11  Anomaly Slot Open at Gate   Anomaly slot not closed before final gate
FM-12  Schema Contract Absent      Entry written before schema contract declared
FM-13  Catalog Opacity             Inline FM code references undeclared catalog entry
```

Output cross-reference rule: every output cell containing a defect carries its FM code inline. Format: `[defect description | FM-NN]`. Reviewers diagnose violations from the output cell; they do not re-read the CONTRACT DECLARATION.

---

#### CONTRACT 3 — ENTRY SCHEMA CONTRACT

Both schemas below govern every trigger entry in Role B. Entries written before these schemas are declared carry `[FM-12: schema contract absent]` at the entry level. Entries missing required slots carry `[SLOT EMPTY: {slot} | FM-05]`.

**FIRING ENTRY SCHEMA**

```
Row:                 [integer -- sequential]
Name:                [trigger name]
Type:                [APPROVED TRIGGER TYPE from Contract 1]
Exec Tier:           [Sync | Async | Scheduled]
Latency:             [inline-blocks-transaction | ~N min standard | ~N min premium | cron]
Condition (Taken):   [Taken: {condition} -- {reason it holds in this scenario}]
Condition (Skipped): [Skipped: {condition} -- {reason it does not hold}]
Input:               [{Entity}.{Field}]
Output:              [APPROVED VERB + target]
Side Effects:        [{Entity}.{Field} = {value} | none]
Spawns:              [Row N | none]
Anomaly Flag:        [none | storm | missing | circular]
CA-Ref:              [CA-NN]
```

**NON-FIRING ENTRY SCHEMA**

```
Row:                 [integer -- sequential]
Name:                [trigger name]
Type:                [APPROVED TRIGGER TYPE from Contract 1]
Status:              NON-FIRING
CA-Ref:              [CA-NN]
Reason:              [explicit reason trigger does not fire]
Condition (Skipped): [Skipped: {condition} -- {why this condition is not met}]
```

---

*CONTRACT DECLARATION COMPLETE. Role analysis begins below.*

---

### ROLE A — SCANNER

**Task**: Establish the analysis boundary, enumerate all trigger candidates by entity/field/type without condition evaluation, declare N, and open the three anomaly question slots.

```
CHANGE SCOPE PIN:
  Entity.Field: {entity}.{field}
  Change: {old} -> {new}
  Initiating Action: {action}

CANDIDATE PRE-SCAN (FM-02 guard: entity/field/type match only):
  CA-01 | {name} | {type from Contract 1} | {match basis}
  ...
  DENOMINATOR: N = {count}

ANOMALY QUESTIONS (Status: OPEN):
  [ ] STORM    -- Do any two triggers fire simultaneously for this change?
  [ ] MISSING  -- Are there expected automations absent from this candidate list?
  [ ] CIRCULAR -- Does any cascade chain terminate by re-firing a prior trigger?
```

---

### ROLE B — TRACER

**Task**: Produce one entry per CA-NN candidate. Use FIRING ENTRY schema for firing triggers; NON-FIRING ENTRY schema for non-firing triggers. All terms must conform to Contract 1. All defects are tagged with FM codes from Contract 2.

Write SYNC FIRING TABLE, then ASYNC FIRING TABLE (FM-09 guard per table), then NON-FIRING TABLE.

End with:

```
TRACER HANDOFF:
  Sync:       {count}
  Async:      {count}
  Non-firing: {count}
  Total:      {sum} (must equal N)
  Chains:     {CH-NN list or none}
  [Any NOT-IN-DENOMINATOR entries]: {list or none}
```

---

### ROLE C — CASCADE CLOSER AND ANOMALY GATEKEEPER

**Task**: (a) Walk every cascade chain to terminal. (b) Close all three anomaly slots.

**(a) Cascade chains:**

```
Chain CH-{N} | Root: {trigger}
  Step 1: {trigger} -> {output} | Spawns: {next trigger}
  Step N: {trigger} -> {output} | [TERMINAL]: {condition}
  OR [CHAIN OPEN: CH-N | FM-07]: {reason}
```

**(b) Anomaly closure:**

```
[ ] STORM:
    Evidence: {row citations from Role B | "no simultaneous fires"}
    Verdict:  DETECTED | NOT DETECTED
    [If DETECTED] Remediation: {specific fix}

[ ] MISSING:
    Evidence: {expected trigger, Phase B absence confirmation}
    Verdict:  DETECTED | NOT DETECTED
    [If DETECTED] Remediation: {specific fix}

[ ] CIRCULAR:
    DFS: {in-path set steps | "full traversal, no back-edge"}
    Evidence: {back-edge or traversal complete}
    Verdict:  DETECTED | NOT DETECTED
    [If DETECTED] Remediation: {specific fix}
```

Verdicts without evidence: `[UNANCHORED: {verdict} | FM-06]`

---

### ROLE D — RECONCILIATION AUDITOR AND GATE

**Task**: Verify denominator closure. Produce trigger map. Issue gate. No analysis content generated by this role — only verification and summary.

```
DENOMINATOR CLOSURE (FM-08 guard):
  N (Role A):         {n}
  Firing (Role B):    {n}
  Non-firing (Role B):{n}
  Accounted:          {sum}
  Result: MATCHED | GAP
  [If GAP] Missing: {CA-NN list}
```

Trigger map:

| Row | Name | Type | Exec Tier | Latency | Anomaly Flag | Spawns |
|-----|------|------|-----------|---------|--------------|--------|

```
GATE:
  Contract 1 violations (vocab): {n | none}
  Contract 2 violations (FM codes): {n | none}
  Contract 3 violations (schema): {n | none}
  Anomaly slots closed: YES | NO
  Denominator matched:  YES | NO
  OVERALL: PASS | FAIL
  [If FAIL]: {list}
```

---

## V-05 — Three-Layer Stack: Contract Layer → Analysis Layer → Closure Layer (All Four: C-18 + C-19 + C-20 + C-21)

**Variation axis**: Lifecycle emphasis + phrasing register
**Hypothesis**: The four new v5 criteria (C-18, C-19, C-20, C-21) all require *declared contracts that precede analysis*. V-05 makes this architectural by naming three structural layers — CONTRACT LAYER, ANALYSIS LAYER, CLOSURE LAYER — and assigning all contract declarations to the first layer. The CONTRACT LAYER declares the FM catalog (C-18), entry schemas (C-19), phase protocol with job descriptions (C-20), and platform term contract (C-21). The ANALYSIS LAYER contains all trigger enumeration and cascade tracing. The CLOSURE LAYER contains all anomaly verdicts, denominator arithmetic, and the gate. No analysis content appears in the CONTRACT LAYER; no contract content appears in the ANALYSIS LAYER.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Structure your output as three explicitly-labeled layers. Do not blend content across layers. The layers are:

1. **CONTRACT LAYER** — all structural contracts, before any analysis
2. **ANALYSIS LAYER** — all trigger enumeration and cascade tracing
3. **CLOSURE LAYER** — all anomaly verdicts, denominator arithmetic, gate

Begin.

---

## CONTRACT LAYER

*All four contracts must appear in this layer before the ANALYSIS LAYER begins. Analysis content is prohibited in this layer.*

---

### CL-1: PLATFORM TERM CONTRACT

The following terms are the authorised vocabulary for this analysis. Non-conforming terms are tagged `[VOCAB FAIL: {term}]` at the point of use.

```
TRIGGER TYPES (authorised):
  sync plugin step
  async plugin step
  instant flow
  automated flow
  scheduled flow
  Dataverse change trigger
  Copilot Studio topic trigger
  custom API webhook

EXECUTION TIERS:
  Sync      -- executes inline, blocks the calling transaction
  Async     -- queued execution, ~N min latency (N must be stated)
  Scheduled -- time-based, {interval or cron expression}

OUTPUT ACTION VERBS:
  Sets | Creates | Deletes | Sends notification via |
  Calls HTTP | Starts child flow: | Posts adaptive card to
```

---

### CL-2: FAILURE MODE CATALOG (FM-01 through FM-14)

This catalog is the reference for all defect annotations in the ANALYSIS and CLOSURE layers. Any FM tag in those layers resolves to an entry here. A tag referencing a code not in this catalog is itself `[FM-14: catalog opacity]`.

```
FM-01  Undeclared Denominator        N not stated before first enumeration row
FM-02  Denominator Shrinkage         Condition evaluated during pre-scan
FM-03  Vocabulary Drift              Unapproved term in output cell
FM-04  Branch Blindness              Condition (Skipped) slot absent from entry
FM-05  Slot Gap                      Required schema slot empty
FM-06  Verdict Orphan                Anomaly verdict without evidence citation
FM-07  Cascade Truncation            Chain ends without [TERMINAL] or [CHAIN OPEN]
FM-08  Denominator Closure Skip      Post-enumeration arithmetic absent from Closure Layer
FM-09  Tier Blur                     Sync trigger in async section or vice versa
FM-10  Side-Effect Orphan            Side effect with automation potential lacks spawn row
FM-11  Anomaly Slot Open at Gate     Anomaly slot unclosed in Closure Layer gate
FM-12  Schema Contract Absent        Entry written without prior schema declaration
FM-13  Self-Gating                   Analysis content generated by the gate/closure role
FM-14  Catalog Opacity               FM tag references code not in this catalog
```

Self-annotation rule: every output cell containing a defect carries its FM code in the format `[description | FM-NN]`. A cell with a defect and no FM code is itself `[FM-14]`.

---

### CL-3: ENTRY SCHEMA CONTRACT

Both schemas are declared in this layer before any trigger rows appear. Rows in the ANALYSIS LAYER are audited against these schemas. Missing schemas: `[FM-12]` on every affected entry.

**FIRING ENTRY SCHEMA** — required slots:

```
  Row:                  integer (sequential within session)
  Name:                 trigger name (unique within session)
  Type:                 authorised trigger type from CL-1
  Exec Tier:            Sync | Async | Scheduled (from CL-1)
  Latency:              inline-blocks-transaction | ~N min standard | ~N min premium | {cron}
  Condition (Taken):    Taken: {condition} -- {reason it is satisfied in this scenario}
  Condition (Skipped):  Skipped: {condition} -- {reason it is not satisfied}
  Input:                {Entity}.{Field}
  Output:               {authorised verb} {target}
  Side Effects:         {Entity}.{Field} = {value} | none
  Spawns:               Row N (cascade continues to that row) | none
  Anomaly Flag:         none | storm | missing | circular
  CA-Ref:               CA-NN (maps to pre-scan candidate)
```

Absent slot: `[SLOT EMPTY: {slot name} | FM-05]`
Absent skipped condition: `[BRANCH BLIND: {entry name} | FM-04]`
Unapproved type: `[VOCAB FAIL: {type} | FM-03]`

**NON-FIRING ENTRY SCHEMA** — required slots:

```
  Row:                  integer (sequential, shared with firing entries)
  Name:                 trigger name
  Type:                 authorised trigger type from CL-1
  Status:               NON-FIRING
  CA-Ref:               CA-NN
  Reason:               explicit reason this trigger does not fire in the scenario
  Condition (Skipped):  Skipped: {condition} -- {reason it is not met}
```

---

### CL-4: PHASE PROTOCOL

The ANALYSIS LAYER and CLOSURE LAYER execute the following phases in order. Each phase carries a job description. The output must re-state the phase job at the start of that phase.

```
Phase A — PRE-SCAN
  Job: Identify all trigger candidates by entity/field/type. Declare N. Open anomaly slots.
  Complete when: N stated, three anomaly slots are OPEN, no condition evaluated.

Phase B — ENUMERATION
  Job: Produce one schema-conforming entry for every CA-NN candidate.
  Complete when: All N candidates have a row; (firing + non-firing) count stated.

Phase C — CASCADE TRACE
  Job: Walk every cascade chain to terminal. Mark each chain TERMINAL or CHAIN OPEN.
  Complete when: Every chain carries a terminal marker.

Phase D — ANOMALY CLOSURE (Closure Layer)
  Job: Close all three anomaly question slots with evidence from Phases B and C.
  Complete when: All three slots carry verdict + evidence; detections have remediations.

Phase E — DENOMINATOR GATE (Closure Layer)
  Job (Phase E's gate): Verify (firing + non-firing) = N. Produce trigger map. PASS or FAIL.
  Gate condition: All anomaly slots closed AND denominator matched AND no open FM violations.
  Complete when: Gate issued. No analysis content follows.
```

---

*CONTRACT LAYER COMPLETE. ANALYSIS LAYER begins.*

---

## ANALYSIS LAYER

---

### Phase A — PRE-SCAN

*Job (from CL-4): Identify all trigger candidates by entity/field/type. Declare N. Open anomaly slots.*

```
CHANGE SCOPE PIN:
  Entity.Field: {entity}.{field}
  Change:       {old value} -> {new value}
  Context:      {initiating action or user role}

CANDIDATE PRE-SCAN:
  [FM-02 guard: entity/field/type matching only -- no condition evaluation]
  CA-01 | {trigger name} | {type from CL-1} | matched by: {entity/field/plugin reference}
  CA-NN | ...
  N = {total count}

ANOMALY QUESTION SLOTS (Status: OPEN):
  [ ] STORM    -- Does one field change fire the same trigger type more than once?
  [ ] MISSING  -- Are expected automations absent from the candidate list above?
  [ ] CIRCULAR -- Does any cascade chain contain a back-edge?
```

Phase A complete: N stated, three slots open.

---

### Phase B — ENUMERATION

*Job (from CL-4): Produce one schema-conforming entry for every CA-NN candidate.*

*Entries conform to FIRING ENTRY or NON-FIRING ENTRY schema from CL-3. FM violations tagged per CL-2.*

**SYNC FIRING TABLE** (FM-09: async entries here tagged `[FM-09: tier mismatch in sync table]`)

[Trigger rows conforming to FIRING ENTRY schema]

**ASYNC FIRING TABLE** (FM-09: sync entries here tagged `[FM-09: tier mismatch in async table]`)

[Trigger rows conforming to FIRING ENTRY schema]

**NON-FIRING TABLE**

[Rows conforming to NON-FIRING ENTRY schema]

```
PHASE B TALLY:
  Sync firing:   {n}
  Async firing:  {n}
  Non-firing:    {n}
  Total:         {sum}
  Cascade chains opened: {CH-NN -> root trigger | none}
```

---

### Phase C — CASCADE TRACE

*Job (from CL-4): Walk every cascade chain to terminal. Mark each chain TERMINAL or CHAIN OPEN.*

For each chain opened in Phase B:

```
Chain CH-{N} | Root: {trigger name} | Root Row: {row number from Phase B}
  Step 1: {trigger name} (Row {N}) | Output: {field write or action} | Spawns: {next trigger name}
  ...
  Step N: {trigger name} | Output: {action} | [TERMINAL]: {termination condition stated}
  OR
  Step N: {trigger name} | Output: {action} | [CHAIN OPEN: CH-N | FM-07]: {why terminal cannot be reached}
```

If no cascade chains exist: state "No cascade chains. Phase C complete."

Phase C complete: every chain carries `[TERMINAL]` or `[CHAIN OPEN: CH-N | FM-07]`.

---

*ANALYSIS LAYER COMPLETE. CLOSURE LAYER begins.*

---

## CLOSURE LAYER

---

### Phase D — ANOMALY CLOSURE

*Job (from CL-4): Close all three anomaly question slots with evidence from Phases B and C.*

```
[x] STORM:
    Evidence (from Phase B rows):
      {cite specific row numbers and trigger names, or "no trigger fires more than once per change"}
    Verdict: DETECTED | NOT DETECTED
    [If DETECTED]
      Remediation: {debounce strategy | dedup condition | trigger filter refinement}
      FM tag: [storm detected: {trigger pair} | anomaly]

[x] MISSING:
    Evidence (from Phase A pre-scan and Phase B non-firing rows):
      {cite expected trigger name and its absence, or "all expected automations present in Phase B"}
    Verdict: DETECTED | NOT DETECTED
    [If DETECTED]
      Remediation: {register missing trigger | create flow | document intentional gap}
      FM tag: [missing trigger: {expected name} | anomaly]

[x] CIRCULAR:
    DFS traversal (show in-path set at each step, or confirm "full traversal complete"):
      {in-path: {} | step 1: {trigger} -- in-path: {trigger} | step 2: ...}
      {or: DFS complete across all Phase C chains; no back-edge found}
    Evidence: {back-edge cite: step N spawns trigger already in path | "no back-edge in full traversal"}
    Verdict: DETECTED | NOT DETECTED
    [If DETECTED]
      Remediation: {condition guard on re-firing trigger | cycle-break field | re-sequencing}
      FM tag: [circular: {back-edge path} | anomaly]
```

Verdicts without evidence citations: `[UNANCHORED: {verdict} | FM-06]`

Phase D complete: all three slots carry verdict + evidence; detections have remediations.

---

### Phase E — DENOMINATOR GATE

*Job (from CL-4): Verify (firing + non-firing) = N. Produce trigger map. Issue PASS or FAIL. No analysis content follows.*

*Gate condition: All anomaly slots closed AND denominator matched AND no open FM violations.*

```
DENOMINATOR CLOSURE (FM-08 guard):
  N declared in Phase A:       {n}
  Firing rows in Phase B:      {n}
  Non-firing rows in Phase B:  {n}
  Total accounted:             {sum}
  Match: MATCHED | GAP
  [If GAP] Unaccounted CA-NN: {list}
```

Discrepancy marker: `[DENOMINATOR GAP: N={declared} actual={actual} | FM-08]`

**TRIGGER MAP** (all phases, at-a-glance):

| Row | Trigger Name | Type | Exec Tier | Latency | Anomaly Flag | Spawns |
|-----|-------------|------|-----------|---------|--------------|--------|
| ... | ... | ... | ... | ... | none/storm/missing/circular | Row N or none |

```
PHASE E GATE:
  CL-1 (vocab) violations:        {count | none}
  CL-2 (FM catalog) violations:   {count | none}
  CL-3 (schema) violations:       {count | none}
  Anomaly slots closed:            YES | NO -- {list any OPEN}
  Denominator matched:             YES | NO
  Self-gating violations (FM-13):  {count | none}
  OVERALL: PASS | FAIL
  [If FAIL] Blocking issues: {ordered list}
```

*Phase E complete. No further content.*

---

## Variation Summary

| Variation | Primary Axis | C-18 | C-19 | C-20 | C-21 | Mechanism |
|-----------|-------------|------|------|------|------|-----------|
| V-01 | Role sequence | FM catalog as standalone PROTOCOL PREAMBLE block (not embedded in Role A) | Incidental — entry schema inside phase body | No explicit phase labels | Vocab contract in PROTOCOL PREAMBLE before any platform terms | Two-contract preamble: FM catalog + vocab contract co-located before roles |
| V-02 | Output format | FM catalog as compact pre-role table | **ENTRY SCHEMA CONTRACT block before first row** — both schemas with all slots named | No explicit phase labels | Vocab contract in preamble block | Schema contract is the primary new structural gate; slot omissions become schema violations |
| V-03 | Lifecycle emphasis | FM catalog before Phase 1 | Entry schemas declared before Phase 1 (incidental) | **Phase 1–5 each with stated job description and gate for Phase 5** | Vocab contract before Phase 1 (incidental) | Phase job descriptions replace role labels; phase gate is the new structural mechanism |
| V-04 | Role sequence + output format | **CONTRACT DECLARATION section before all roles** containing FM catalog | **CONTRACT 3: ENTRY SCHEMA CONTRACT** in pre-role section | No explicit phase labels | **CONTRACT 1: PLATFORM TERM CONTRACT** in pre-role section | Three-contract declaration block before role structure; roles begin only after contracts complete |
| V-05 | Lifecycle + phrasing | **CL-2 in CONTRACT LAYER** | **CL-3 in CONTRACT LAYER** | **CL-4 PHASE PROTOCOL with job descriptions** | **CL-1 in CONTRACT LAYER** | Three-layer architecture (CONTRACT / ANALYSIS / CLOSURE); all four contracts in CL; no analysis in CL |
