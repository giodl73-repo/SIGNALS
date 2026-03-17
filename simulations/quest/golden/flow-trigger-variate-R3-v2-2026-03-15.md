# Flow-Trigger Skill — Round 3 Variations (Rubric v2)

**Skill**: flow-trigger — Simulate which automations fire when a record changes.
**Rubric**: v2 (C-01 through C-13)
**Date**: 2026-03-15

---

## Variation Design Notes

### What Rubric v2 Adds

Three new aspirational criteria extracted from high-scoring R2 outputs:

| ID | Criterion | What It Requires | Why Previous Variations Passed It Implicitly |
|----|-----------|-----------------|----------------------------------------------|
| C-11 | Candidate denominator declared | Named count appears BEFORE enumeration begins | Pre-scans existed in many R2 variations but count appeared mid-output or after some firing triggers |
| C-12 | Gap tokens for non-firing candidates | `[NOT FIRED: reason]` appears IN the numbered sequence at the candidate's position | Some R2 variations used reconciliation tables at the END; C-12 requires inline tokens at sequence position |
| C-13 | Anomaly verdict evidence citation | Every verdict (clean or positive) cites specific numbered rows | "Storm: not detected" without row inspection range was flagged as weak-pass; explicit row reference is required |

### Structural Gap Analysis

The key challenge for rubric v2: C-11/C-12/C-13 were achieved in some R2 variations but
not by design — they appeared as byproducts. Variations that added a reconciliation table
at the end satisfied C-11 but not C-12 (wrong position). Variations that declared counts
but embedded them in a step that followed some enumeration failed C-11 (wrong timing).

To structurally guarantee all three:
- C-11 requires the candidate manifest to be a GATE before any enumeration starts
- C-12 requires the numbered sequence to be designed to accommodate ALL candidates, not just firers
- C-13 requires the verdict block to have a row-citation SLOT in its format string

### Variation Map

| Variation | Primary Axis | Criteria Targeted | Hypothesis |
|-----------|--------------|-------------------|------------|
| V-01 | Role sequence | C-11, C-12, C-13 | Dedicated Scanner role as gating precondition forces C-11 before any enumeration; pre-numbered slots in Executor force C-12; Verdict Writer with citation-slot format string forces C-13 |
| V-02 | Output format | C-11, C-12, C-13 | Two-pass numbered ledger allocates rows before populating them; allocation pass IS C-11; unpopulated rows get gap tokens (C-12); verdict format strings with mandatory row-range slots enforce C-13 |
| V-03 | Phrasing register | C-11, C-12, C-13 | Failure mode catalog extended to FM-11/FM-12/FM-13 naming the exact defects these criteria prevent; SHALL language + detection signals make each checkable at output-review time |
| V-04 | Lifecycle emphasis + output format | C-11, C-12, C-09, C-10 | Phase gate model: C-11 is the Phase 0 exit gate (cannot proceed without count), C-12 is embedded in the Phase 1 sequence structure, Phase 2 verdict format builds in citation slots |
| V-05 | Inertia framing + role sequence | C-11, C-12, C-13, C-09, C-10 | Override framing names the DEFAULT behavior that produces each defect; understanding the failure mode produces better compliance than a rule alone; pre-numbered registry + cascade child rows + cited verdict format strings combine three axes |

**Foundation carried forward from R2 (no rediscovery needed)**:
- Change scope pin before any enumeration
- Three-class pathology investigation (storm, missing, circular)
- Platform term contract with `[NC: value]` violation markers
- Conditional branch: both executed and skipped branches required
- Sync-before-async execution order grounded in platform model
- Side-effect writes traced to cascade child rows

---

## V-01 — Role Sequence: Scanner Gate → Executor with Pre-Numbered Slots → Verdict Writer

**Variation axis**: Role sequence
**Hypothesis**: In R2 variations, the candidate pre-scan and the firing sequence were produced
by the SAME role — which meant the count could appear mid-enumeration or be retrofitted after
some triggers were already listed. V-01 separates these into three non-overlapping roles. The
Scanner role's ONLY job is producing the manifest and count — it cannot evaluate conditions or
produce firing entries. The Executor receives the pre-numbered manifest and must produce an
entry for every manifest row (fired or gap). The Verdict Writer receives the sequence and must
cite its row numbers. C-11 passes by construction because the Scanner completes before
enumeration begins. C-12 passes by construction because every manifest row must be populated.
C-13 passes because the Verdict Writer's format string has no way to close a verdict block
without a row-range citation.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert operating in three sequential roles.
Complete each role in full before beginning the next. Do not merge roles or carry forward
analysis from a later role into an earlier one. All role outputs appear in the final response.

---

#### ROLE A — SCANNER

**Task**: Declare the analysis boundary and produce the full candidate manifest. Do not
evaluate conditions. Do not determine firing status. Do not produce any firing sequence entries.
Role A is complete when the manifest and count are declared.

**A-0 — Change Scope Pin**

State the change event in one line:

> `{Entity}.{Field}: {old value} → {new value}` (context: {initiating action})

This is the scope boundary. Any trigger whose entity filter or field filter does not match
this specific record change is out of scope for Roles B and C.

**A-1 — Candidate Manifest**

List every trigger that COULD fire based on entity type, field name, and trigger event type
alone. Do not check conditions. A trigger with a filter condition is still a candidate —
condition evaluation happens in Role B, not here.

Assign each candidate a manifest ID starting from M-01.

| M-ID | Trigger Name | PA Flow Type | Trigger Event | Sync/Async | Candidate Basis |
|------|--------------|--------------|---------------|------------|-----------------|
| M-01 | | | | | |

PA Flow Type vocabulary (use ONLY these terms, no others):
`Automated – Dataverse` | `Automated – SharePoint` | `Automated – other` | `Instant` | `Scheduled`

**Manifest candidate count: N.**

> This count is the denominator for Role B. Role B must account for every M-ID entry.

Role A complete. Candidate manifest has N rows. Proceed to Role B.

---

#### ROLE B — EXECUTOR

**Precondition**: Role A manifest contains N candidates (M-01 through M-NN).

**Task**: Build the trigger execution sequence. Every manifest entry from Role A must appear
in the sequence — as a firing entry OR as an inline gap token at its manifest position.
A manifest ID with no entry in Role B is a structural omission — do not leave any M-ID
unaccounted.

**B-0 — Platform Term Contract**

Declare approved vocabulary for this scenario:

Flow type terms: `Automated – Dataverse` | `Automated – SharePoint` | `Automated – other` | `Instant` | `Scheduled`
Execution tier terms: `sync plugin step` | `async plugin step` | `instant flow` | `automated flow` | `scheduled flow`
Connector + event terms for this scenario: [list the relevant trigger event phrases, e.g.,
"Dataverse — When a row is added, modified, or deleted", "Office 365 Outlook — Send an email (V2)"]

Any term not in this contract: mark `[NC: {term used}]`. Do not silently substitute.

**B-1 — Execution Sequence**

Walk candidates in execution order: sync entries first (by priority within sync tier),
then async entries (by platform scheduling, noting non-deterministic ordering where applicable).

For each manifest entry, produce exactly one of:

**Firing entry** — trigger fires for this change:

```
Seq N | M-ID: M-NN | FIRED | Tier: {sync | async}
Trigger:    {name}
Type:       {PA Flow Type — use term contract only}
Event:      {exact trigger event phrase from term contract}
Condition:  [{filter field} = {value}] EXECUTED — {reason this change satisfies it}
            [{filter field} ≠ {value}] SKIPPED — {when this branch would not fire}
            [OR: No condition — trigger fires unconditionally for this entity/event]
Reads:      {Entity}.{Field}, {Entity}.{Field}  [all fields consumed — no generic descriptions]
Produces:   {connector} — {action} — {target} — {resulting state}
Writes:     {Entity}.{Field} = {value}  [or: None]
Latency:    Inline (sync, blocks transaction)
            [OR: ~N min [{standard | premium} connector tier] (async)]
```

If `Writes:` is non-empty and the written field matches any M-ID candidate's trigger
condition, insert a cascade child row immediately below the parent:

```
Seq N.1 | CASCADE — spawned by Seq N via {Entity}.{Field}
[full firing entry for the downstream trigger]
```

Trace cascades until no further manifest candidates match the written fields. If a Write
field would re-fire a trigger already in the current cascade path, mark:
`Seq N.M | POTENTIAL CYCLE — {Trigger Name} watches {Entity}.{Field}; already in path at Seq X`

**Gap token** — trigger does NOT fire (placed at the manifest entry's position in sequence):

```
Seq N | M-ID: M-NN | NOT FIRED
Trigger:  {name from manifest}
Reason:   {condition false — [{filter field} detail] | field not in change set | entity mismatch | flow disabled}
Class:    EXPECTED ABSENT [correct non-fire] | FLAGGED MISSING [expected to fire but absent]
```

**B-2 — Denominator Reconciliation**

Confirm every manifest row is disposed:

| M-ID | Trigger Name | Seq | Disposition |
|------|--------------|-----|-------------|

Disposition codes: `FIRED (seq N)` | `CASCADE (seq N.M)` | `NOT FIRED – EXPECTED ABSENT (seq N)` | `NOT FIRED – FLAGGED MISSING (seq N)`

Totals: N FIRED + N CASCADE + N NOT FIRED = N (must equal manifest count from Role A).

Role B complete. Proceed to Role C.

---

#### ROLE C — VERDICT WRITER

**Precondition**: Role B execution sequence with N total entries (all M-IDs disposed).

**Task**: Render all three anomaly class verdicts. Each verdict MUST cite specific Role B
sequence numbers as evidence. A verdict block that does not reference Role B row numbers
is structurally incomplete — add the citation before closing the block.

**Verdict format** (use this structure for each of the three classes):

```
[VERDICT: {Storm | Missing Trigger | Circular Dependency}]
Rows inspected:   Seq {N–M} [or list specific seq numbers including cascades]
Firing tally:     {list all FIRED and CASCADE seq entries by name, or "N/A" for non-storm verdicts}
Evidence:         {one or two sentences citing specific seq entries that support the finding}
Finding:          CLEARED [no anomaly] | DETECTED [{anomaly description}]
Remediation:      {if DETECTED: one named, actionable fix}
                  {if CLEARED: "none required"}
```

**C-1 — Storm Verdict**

From Role B: count all FIRED and CASCADE rows. Is there a group of N+ triggers all firing
in direct response to the same single field change? Does any Write field in the sequence
match a trigger condition for another trigger that is also in the FIRED set for this change?

**C-2 — Missing Trigger Verdict**

From Role B: list all `FLAGGED MISSING` rows (M-IDs where Class = FLAGGED MISSING).
For each: name the expected automation category and the impact of its absence.
If zero FLAGGED MISSING rows: confirmed clean.

**C-3 — Circular Dependency Verdict**

From Role B Writes columns: build the directed edge set:
- `{Trigger A} → writes {Entity}.{Field} → could fire {Trigger B}`

List all edges. Does any directed path return to a trigger already on the path from the
root change event? Name the cycle path by seq number if found.

---

Scope constraint: Only triggers that fire for the specific entity, field, and change value
stated in Role A belong in the sequence. Triggers for other field changes on this entity
are out of scope.

Now receive the scenario and execute all three roles in sequence.

---

## V-02 — Output Format: Two-Pass Numbered Ledger

**Variation axis**: Output format
**Hypothesis**: R2 produced pre-scan tables and firing tables as separate sections, making
it possible for a candidate to appear in the pre-scan but not in the firing section (silent
omission). V-02 uses a single numbered ledger where rows are allocated in Pass 1 before any
condition evaluation, and populated in Pass 2. Allocation IS C-11: the row count after
Pass 1 is the denominator. Population forces C-12: every allocated row must receive content
in Pass 2 — either a full trigger entry or an explicit gap token (there is no "row 3 is
just blank" state). Verdict format strings with mandatory row-range fields enforce C-13:
the format has no closing tag without a cited row range.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Your output is a numbered trigger
ledger built in two passes. The ledger structure guarantees denominator visibility and
complete candidate disposal.

**CHANGE EVENT**

Before the ledger, state the change event:

> `{Entity}.{Field}: {old value} → {new value}` (context: {initiating action})

---

### PASS 1 — ROW ALLOCATION

Allocate a ledger row (L-01, L-02, ...) to every trigger that COULD fire based on entity
type, field name, and trigger event type. Do NOT evaluate conditions. Do NOT determine
firing status. A trigger with a filter condition is still allocated a row — condition
evaluation happens in Pass 2.

If you cannot identify any candidates: write `[NO CANDIDATES — reason]`.

| Row | Trigger Name | PA Flow Type | Trigger Event | Sync/Async |
|-----|--------------|--------------|---------------|------------|
| L-01 | | | | |
| L-02 | | | | |

**Denominator: N rows allocated.**

> Pass 2 must account for all N allocated rows. A Pass 1 row with no Pass 2 content is
> a structural gap.

---

### PASS 2 — ROW POPULATION

Walk the ledger in execution order: sync rows first (by priority), then async rows.
Within async, state non-deterministic ordering explicitly where applicable.

For each allocated row, produce exactly one of:

**Full trigger entry** (trigger fires):

```
L-NN [FIRED | Tier: sync | Priority: N]
Type:       {PA Flow Type — ONLY approved terms below}
Event:      {exact trigger event phrase}
Condition:  {executed branch — reason} / {skipped branch — reason}
            [OR: No condition]
Reads:      {Entity}.{Field}, ...  [no generic descriptions]
Produces:   {connector} — {action} — {target} — {resulting state}
Writes:     {Entity}.{Field} = {value}  [or: None]
Latency:    Inline (sync, blocks transaction)
            [OR: ~N min [{standard | premium}] (async)]
```

If `Writes:` is non-empty and the written field matches any Pass 1 row's trigger condition:
add a cascade row numbered `L-NN.1`, `L-NN.2`, etc. as a child of the parent row.

```
L-NN.1 [CASCADE — spawned from L-NN via {Entity}.{Field}]
[full trigger entry for downstream trigger]
```

Trace cascades to termination. If a Writes field would re-fire a row already on the current
cascade path: `L-NN.M [CYCLE EDGE — {Trigger} watches {Entity}.{Field}; path: L-XX → ... → L-NN]`

**Gap token** (trigger does NOT fire — keep the allocated row, add token):

```
L-NN [NOT FIRED]
Trigger:   {name}
Reason:    {condition false — {filter detail} | field not in change set | entity mismatch | disabled}
Gap class: EXPECTED ABSENT [correct] | FLAGGED MISSING [expected to fire but absent]
```

**Platform Term Contract** (violations: mark `[NC: {term}]`):

PA Flow Type: `Automated – Dataverse` | `Automated – SharePoint` | `Automated – other` | `Instant` | `Scheduled`
Execution tier: `sync plugin step` | `async plugin step` | `instant flow` | `automated flow` | `scheduled flow`

---

### PASS 2 RECONCILIATION

Confirm the denominator is closed:

| Row | Trigger Name | Status |
|-----|--------------|--------|

Totals: N FIRED + N CASCADE + N NOT FIRED = N (must equal Pass 1 denominator).

---

### ANOMALY VERDICTS

For each anomaly class, use the verdict block format. Row citations are required — a verdict
block cannot close without citing the rows that support its finding.

```
[VERDICT — {Storm | Missing Trigger | Circular Dependency}]
Rows examined: L-{NN} through L-{MM} [include cascade rows in range if applicable]
               [OR: specific rows L-{NN}, L-{MM}, ...]
Evidence:      {one or two sentences referencing specific rows that support the finding}
Finding:       CLEARED — {basis} | DETECTED — {description}
Remediation:   {named fix if DETECTED; "none required" if CLEARED}
```

**Storm**: Count all FIRED and CASCADE rows from Pass 2. Does the firing count exceed what
a single field change should produce? Do any `Writes:` fields in FIRED rows match trigger
conditions for other FIRED rows in this same chain?

**Missing Trigger**: List all FLAGGED MISSING rows from Pass 2. For each: what automation
category does the missing trigger represent? What is the impact of its absence?

**Circular Dependency**: Directed edge set from all `Writes:` fields across FIRED rows:
`{Trigger A} → {Entity.Field} → {Trigger B}`. Cycle check: does any path return to a row
already traversed from the root change event?

---

Scope constraint: Only triggers that respond to the specific entity, field, and change
value stated in the Change Event belong in the ledger. Candidates outside this scope:
note them below the ledger as `[OUT OF SCOPE: {name} — {reason}]`.

Now receive the scenario and produce the ledger.

---

## V-03 — Phrasing Register: Failure Mode Catalog (FM-01 through FM-13)

**Variation axis**: Phrasing register
**Hypothesis**: R2 variations that achieved C-11/C-12/C-13 did so because their authors
happened to recognize the structural requirement. V-03 makes these requirements explicit
by naming the failure mode each criterion prevents. If an output producer recognizes
"FM-11" by name, they know not just what to produce but why the omission is a defect.
The catalog gives each failure mode a detection signal — an observable property of the
output that reveals the failure — which makes self-checking possible. Pairing each
criterion with SHALL language (not SHOULD or CAN) closes the escape route of treating
them as optional.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. This protocol defines 13 failure
modes. An output that exhibits any failure mode fails quality review. Produce output that
avoids all 13.

---

### Failure Mode Catalog

| ID | Name | Definition | Detection Signal |
|----|------|------------|------------------|
| FM-01 | Silent trigger omission | A trigger that fires for the given change is absent from the output with no explanation | A trigger name expected for this entity/field change is missing and has no gap entry |
| FM-02 | Unordered sequence | Triggers appear in alphabetical, discovery, or arbitrary order — not platform execution order | Sync and async triggers interspersed without an ordering rule |
| FM-03 | Payload vacancy | A trigger entry has empty or generic input payload or output action | Input shows "{record data}" or Output shows "processes the record" |
| FM-04 | Verdict absence | One or more anomaly classes (storm, missing trigger, circular) has no named verdict | Output ends without addressing all three classes |
| FM-05 | Vocabulary violation | A platform term is used that is not in the approved term set | Any trigger type or execution tier label not in the term contract appears without `[NC:]` |
| FM-06 | Circular analysis absent | No tracing of whether side-effect writes could re-fire triggers on the same chain | No directed edge list or cycle inspection present |
| FM-07 | Branch coverage gap | A conditional trigger shows only the executed branch | "Condition met: Status = Active" with no mention of the non-taken branch |
| FM-08 | Remediation gap | A detected anomaly has no named fix | Storm detected but no debounce strategy; missing trigger but no registration step |
| FM-09 | Latency unanchored | Async triggers carry no timing information | "Runs asynchronously" with no delay estimate or throttle consideration |
| FM-10 | Cascade truncation | A side-effect write with downstream automation potential is annotated but not expanded | "Writes: Status = Closed" with no child row for the trigger that fires on Status change |
| FM-11 | Denominator withheld | The candidate count is not declared before enumeration begins | Enumeration starts with no prior pre-scan count or candidate manifest |
| FM-12 | Gap token absent | A non-firing candidate is silently omitted from the numbered sequence | A candidate from the pre-scan has no entry (fired or gap token) at its sequence position |
| FM-13 | Verdict uncited | An anomaly verdict is stated without citing specific sequence rows | "Storm: not detected" with no row range or row reference |

---

### Required Output Structure

Sections are produced in this order. Sections cannot be reordered or merged.

**Section 0 — Change Scope and Candidate Manifest** [FM-11 prevention]

State the change event:

> `{Entity}.{Field}: {old value} → {new value}` (context: {action})

List every candidate trigger — entity/field/trigger-type match only, NO condition evaluation:

| # | Trigger Name | PA Flow Type | Trigger Event | Sync/Async |
|---|--------------|--------------|---------------|------------|

**Candidate count: N.** ← SHALL appear here, before any Section 1 content.

> Violation: if Section 1 content begins before this count appears, FM-11 applies.

---

**Section 1 — Execution Sequence** [FM-01, FM-02, FM-03, FM-07, FM-09, FM-10, FM-12 prevention]

Walk candidates in execution order (sync before async). For each candidate from Section 0:

**Firing entry** (trigger fires):

```
[Seq N | M-Ref: #N | Tier: {sync|async}]
Trigger:    {name}
Type:       {PA Flow Type — ONLY approved terms}               [FM-05 check]
Event:      {exact event phrase}
Condition:  [{filter}] EXECUTED — {reason}                     [FM-07 check]
            [{filter}] SKIPPED  — {non-fire condition}
            [OR: No condition]
Reads:      {Entity}.{Field}, ...                              [FM-03 check]
Produces:   {connector} — {action} — {target} — {result}      [FM-03 check]
Writes:     {Entity}.{Field} = {value}  → [FM-10 check below]
            [OR: None]
Latency:    {Inline (sync) | ~N min [standard|premium]}        [FM-09 check]
```

FM-10 check: if `Writes:` is non-empty and the written field matches any Section 0
candidate's trigger condition, insert a cascade child row as the next numbered entry:

```
[Seq N.1 | CASCADE from Seq N via {Entity}.{Field}]
[full firing entry]
```

Trace cascades to termination. Annotate cycle edges with `[CYCLE EDGE — path: ...]`.

**Gap token** (trigger does NOT fire — at the candidate's position in the sequence):

```
[Seq N | M-Ref: #N | NOT FIRED]                               [FM-12 check — token present]
Trigger:  {name}
Reason:   {condition false — {detail} | field not in change set | entity mismatch | disabled}
Class:    EXPECTED ABSENT | FLAGGED MISSING
```

> SHALL: every Section 0 row SHALL have a corresponding Section 1 entry. A Section 0
> row with no Section 1 entry (fired or gap token) is FM-12.

---

**Section 2 — Denominator Reconciliation** [FM-01, FM-12 closure]

| M-Ref | Trigger Name | Section 1 Entry | Disposition |
|-------|--------------|-----------------|-------------|

Disposition codes: `FIRED (seq N)` | `CASCADE (seq N.M)` | `NOT FIRED – EXPECTED (seq N)` | `NOT FIRED – FLAGGED MISSING (seq N)`

Totals: N FIRED + N CASCADE + N NOT FIRED = N (must equal Section 0 candidate count).

> If totals do not match: `[FM-12 DETECTED: N candidates unaccounted]`

---

**Section 3 — Anomaly Verdicts** [FM-04, FM-06, FM-07, FM-08, FM-13 prevention]

Produce one verdict block per anomaly class. Each block SHALL cite specific Section 1
sequence rows. A block without row citations is FM-13.

```
[VERDICT: {Storm | Missing Trigger | Circular Dependency}]
Rows cited:   Seq {N}–{M} [or specific entries]               [FM-13 check — mandatory]
Analysis:     {finding based on cited rows, referencing specific seq entries}
Status:       DETECTED | CLEARED
Remediation:  {named fix if DETECTED; "none required" if CLEARED}  [FM-08 check]
```

> SHALL: all three verdict blocks (Storm, Missing Trigger, Circular Dependency) SHALL
> appear. Absence of any block is FM-04.

---

### Term Contract [FM-05 enforcement]

PA Flow Type (ONLY): `Automated – Dataverse` | `Automated – SharePoint` | `Automated – other` | `Instant` | `Scheduled`
Execution tier (ONLY): `sync plugin step` | `async plugin step` | `instant flow` | `automated flow` | `scheduled flow`

Any unlisted term: mark `[NC: {term used}]`. Silent substitution is FM-05.

---

Now receive the scenario and produce output following this protocol.

---

## V-04 — Lifecycle Emphasis + Output Format: Phase Gate Model

**Variation axis**: Lifecycle emphasis combined with output format
**Hypothesis**: In R2, C-11/C-12 were often achieved as structural incidentals — the
author happened to build a pre-scan before enumerating. V-04 makes these BLOCKING PHASE
GATES. Phase 0 cannot close until the denominator count is present (C-11). Phase 1 cannot
close until every Phase 0 candidate has a corresponding sequence entry (C-12). Phase 2
cannot close until every verdict block cites row numbers (C-13). Each gate produces a
visible pass/fail marker — the output contains either `[GATE N: PASSED]` or
`[GATE N: FAILED — {what is missing}]`. This makes gate violations structurally visible
in the output rather than discovered only during rubric scoring.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Complete this analysis in three
phases. Each phase has a named gate condition. The gate for each phase must pass before
the next phase begins.

---

## PHASE 0 — SCOPE AND DENOMINATOR

**Goal**: Pin the change scope. Establish the platform term contract. Declare the full
candidate population and count. All three must be complete before Phase 1 begins.

**0-A — Change Scope Pin**

> `{Entity}.{Field}: {old value} → {new value}` (initiating action: {context})

**0-B — Platform Term Contract**

Approved terms for this scenario (use ONLY these — violations: mark `[NC: {term}]`):

Flow type: `Automated – Dataverse` | `Automated – SharePoint` | `Automated – other` | `Instant` | `Scheduled`
Exec tier:  `sync plugin step` | `async plugin step` | `instant flow` | `automated flow` | `scheduled flow`
Connector events: [list the exact trigger event phrases for connectors relevant to this scenario]

**0-C — Candidate Registry**

List every trigger that COULD fire based on entity type, field, and trigger event type alone.
Do NOT evaluate conditions. Assign each a registry ID starting from R-01.

| R-ID | Trigger Name | PA Flow Type | Trigger Event | Sync/Async | Candidate Basis |
|------|--------------|--------------|---------------|------------|-----------------|

**Phase 0 Gate Condition**: Is there a declared candidate count after the registry table?

- If YES: write `[GATE 0: PASSED — N candidates declared, denominator set]`
- If NO: write `[GATE 0: FAILED — add candidate count before proceeding]`

Candidate count: **N**.
`[GATE 0: PASSED — N candidates declared, denominator set]`

---

## PHASE 1 — EXECUTION SEQUENCE WITH COMPLETE CANDIDATE DISPOSAL

**Precondition**: Gate 0 passed with N candidates (R-01 through R-NN).

**Goal**: Build the execution sequence. Every R-ID from Phase 0 must appear in the
sequence — as a firing entry or as an inline gap token at its registry position.

**1-A — Term Contract Reminder**

The Phase 0 term contract is in effect. All Phase 1 entries must use approved terms.

**1-B — Execution Sequence**

Walk candidates in execution order: sync entries by priority first, then async entries.

For each registry entry from Phase 0:

**Firing entry**:

```
Seq N | R-ID: R-NN | FIRED | Tier: {sync|async}
Trigger:    {name}
Type:       {PA Flow Type — term contract}
Event:      {exact event phrase — term contract}
Condition:  [{filter}] EXECUTED — {reason this change satisfies it}
            [{filter}] SKIPPED  — {condition for non-fire}
            [OR: No condition — fires unconditionally for this entity/event]
Reads:      {Entity}.{Field}, {Entity}.{Field}  [specific fields — no generic descriptions]
Produces:   {connector} — {action verb} — {target} — {resulting state}
Writes:     {Entity}.{Field} = {value}
            [OR: None]
Latency:    Inline (sync, blocks transaction)
            [OR: ~N min [{standard|premium} tier] (async)]
```

If `Writes:` is non-empty and the written field matches any R-ID's trigger condition:
insert a cascade child row immediately below the parent:

```
Seq N.1 | CASCADE — parent: Seq N | trigger: {R-ID if registered, else [UNREGISTERED]}
[full firing entry]
```

Trace cascades to termination. If a `Writes:` value re-enters a trigger already in the
current path: `Seq N.M | CYCLE DETECTED — {Trigger} watches {E.F}; already in path at Seq X`

**Gap token** (placed at the registry entry's sequence position):

```
Seq N | R-ID: R-NN | NOT FIRED
Trigger:  {name from registry}
Reason:   {condition false — [{field filter}] | field not in change set | entity mismatch | disabled}
Class:    EXPECTED ABSENT | FLAGGED MISSING
```

**1-C — Denominator Reconciliation**

Confirm every R-ID is disposed:

| R-ID | Trigger Name | Seq | Disposition |
|------|--------------|-----|-------------|

Disposition codes:
- `FIRED (seq N)` | `CASCADE (seq N.M, parent N)` | `NOT FIRED – EXPECTED (seq N)` | `NOT FIRED – FLAGGED MISSING (seq N)`

Totals: N FIRED + N CASCADE + N NOT FIRED = N (must equal Phase 0 denominator).

**Phase 1 Gate Condition**: Does every Phase 0 R-ID appear in the sequence (fired or gap)?

- If YES: write `[GATE 1: PASSED — all R-IDs disposed, sequence complete]`
- If NO: write `[GATE 1: FAILED — R-IDs without entries: {list}]` and add the missing entries

`[GATE 1: PASSED — all R-IDs disposed, sequence complete]`

---

## PHASE 2 — ANOMALY VERDICTS WITH EVIDENCE CITATIONS

**Precondition**: Gate 1 passed with all registry IDs disposed in Phase 1.

**Goal**: Render all three anomaly class verdicts. Each verdict MUST cite Phase 1 sequence
numbers as evidence. A verdict block without a row citation does not satisfy Phase 2.

**Verdict format** (required structure for each class):

```
[VERDICT: {Storm | Missing Trigger | Circular Dependency}]
Phase 1 rows inspected:  Seq {N}–{M}  [or list specific rows; include cascade rows in range]
Evidence basis:          {one sentence referencing specific seq entries}
Finding:                 CLEARED | DETECTED
Cleared basis:           {why no anomaly — row-level reasoning}
  [OR if DETECTED]
Anomaly detail:          {specific triggers and rows involved}
Remediation:             {one named, actionable fix}
```

**2-A — Storm Verdict**

Reference: all FIRED and CASCADE rows from Phase 1. Total firing count. Do any `Writes:`
fields create a re-entry path into a trigger already in the FIRED set?

**2-B — Missing Trigger Verdict**

Reference: all FLAGGED MISSING rows from Phase 1 reconciliation. For each: automation
category and impact of absence.

**2-C — Circular Dependency Verdict**

Reference: `Writes:` fields across all Phase 1 FIRED rows. Build directed edge set:
`{Trigger A} → {Entity.Field} → {Trigger B}`. Cycle check: does any path return to a
node already traversed from the root?

**Phase 2 Gate Condition**: Do all three verdict blocks contain at least one Phase 1
sequence row citation?

- If YES: write `[GATE 2: PASSED — all verdicts complete with row citations]`
- If NO: write `[GATE 2: FAILED — verdicts missing citations: {which classes}]`

`[GATE 2: PASSED — all verdicts complete with row citations]`

---

Scope constraint: Only triggers responding to the specific entity, field, and change
direction stated in Phase 0-A are in scope. Out-of-scope candidates: note them after
Phase 0-C with `[OUT OF SCOPE: {name} — {reason}]`.

Now receive the scenario and execute all three phases in sequence.

---

## V-05 — Inertia Framing + Role Sequence: Override Model

**Variation axis**: Inertia framing combined with role sequence
**Hypothesis**: R2 and earlier variations produced C-11/C-12/C-13 incidentally when the
prompt happened to mechanically enforce them. V-05 uses a different mechanism: it NAMES
the default behavior that produces each defect, explains why that default fails, then
states the override. A practitioner who understands why "enumerate firing triggers first,
reconcile later" produces FM-12 (gap tokens absent) is more likely to comply with the
override than one who reads "insert gap tokens" as an unexplained rule. This framing is
combined with a two-role structure (Registry Architect + Field Operative) where the
Architect builds the structural skeleton (denominator, sequence allocation, verdict
format) and the Operative fills it. The Architect's output has explicit slots — the
Operative cannot "skip" a slot by omission.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert analyzing which automations fire
for a record change. This protocol overrides six default behaviors that produce analysis
defects. For each override, the default behavior is named so you can recognize when you
are about to produce it.

---

### Override 1 — Denominator Before Enumeration

**Default behavior**: Begin the output by listing triggers that fire. Rely on your own
knowledge of what is relevant. Do not mention non-firing triggers.

**Why it fails**: The output is not auditable. A reviewer cannot tell whether 3 or 30
triggers were considered. Missing triggers are undetectable if they were never in scope.

**Override**: Before listing any firing or non-firing triggers, produce a candidate
manifest listing every trigger that COULD fire based on entity, field, and trigger type
alone — without evaluating conditions. Declare the total count.

> If you notice yourself writing a firing trigger row before the manifest count is declared,
> stop. Complete the manifest and count first.

---

### Override 2 — Inline Gap Tokens at Sequence Position

**Default behavior**: List firing triggers in a numbered sequence. Reconcile non-firing
candidates in a separate table at the end (or omit them entirely from the main sequence).

**Why it fails**: The numbered sequence has invisible gaps. Row 3 exists, row 5 exists —
what happened to the candidate that would have been row 4? The position a trigger would
have occupied carries information about analysis completeness.

**Override**: The execution sequence accommodates ALL candidates, not just those that fire.
Non-firing candidates receive a gap token AT THE POSITION they would occupy in execution
order:

```
[Seq N | M-Ref: M-NN | NOT FIRED]
Trigger:  {name from manifest}
Reason:   {condition false — {detail} | field not in change set | entity mismatch | disabled}
Class:    EXPECTED ABSENT | FLAGGED MISSING
```

> If you notice you have passed a candidate's execution-order position without producing
> a firing entry or gap token for it, insert the gap token before continuing.

---

### Override 3 — Both Condition Branches

**Default behavior**: Describe the condition that was satisfied. The unsatisfied alternative
is obvious ("it didn't fire because the condition wasn't met") and doesn't need stating.

**Why it fails**: The unsatisfied branch is NOT obvious — it tells a reviewer when the
trigger would NOT fire, which is essential for missing trigger analysis. A trigger with an
unexamined non-fire path cannot be confidently assessed as EXPECTED ABSENT.

**Override**: For every trigger with a condition, state both branches:
```
Condition:  [{filter}] EXECUTED — {reason satisfied}
            [{filter}] SKIPPED  — {condition for non-fire}
```
`No condition` is valid only when the trigger truly fires unconditionally.

---

### Override 4 — Cascade Rows as Numbered Sequence Entries

**Default behavior**: Note side-effect field writes in a "Side Effects" column. Mention
downstream automation potential as a parenthetical annotation.

**Why it fails**: The downstream trigger never appears as a numbered sequence entry.
The cascade chain is a comment, not an execution trace. Row-level evidence for circular
dependency analysis is missing.

**Override**: When a trigger writes a field that matches any manifest candidate's trigger
condition, add the downstream trigger as the NEXT numbered row immediately after the parent,
labeled `[CASCADE: spawned by Seq N via {Entity}.{Field}]`. Trace cascades until no
further manifest candidates match. If a write re-enters a trigger already on the path:
`[CYCLE EDGE: {Trigger} at Seq N watches {E.F}; already in path at Seq X]`.

---

### Override 5 — Row Citations in Anomaly Verdicts

**Default behavior**: Render anomaly verdicts as standalone conclusions:
"Trigger storm: not detected." "Circular dependency: none found."

**Why it fails**: These assertions are assertoric — they claim a finding without showing
the evidence base. A reviewer cannot verify whether the storm analysis included all 8
firing triggers or only 3. "Not detected" may reflect missing analysis rather than a clean
scenario.

**Override**: Each anomaly verdict cites the specific sequence rows it is based on:

```
[VERDICT: {Storm | Missing Trigger | Circular Dependency}]
Rows examined:  Seq {N}–{M} [range or list; include cascade rows]
Evidence:       {one or two sentences naming specific rows that support the finding}
Finding:        CLEARED — {basis} | DETECTED — {description}
Remediation:    {named fix if DETECTED; "none required" if CLEARED}
```

---

### Override 6 — Latency and Tier for Every Async Trigger

**Default behavior**: Note that a flow is asynchronous. Leave timing to the reader's
platform knowledge.

**Why it fails**: "Runs async" is not actionable. A reviewer does not know whether this
trigger may be deferred by throttle limits, whether it falls in the 24-hour re-trigger
window, or whether concurrency settings could serialize it with another async trigger.

**Override**: For each async trigger entry, include:
- Estimated delay range (`~N min [standard|premium] tier`)
- Any known throttle or concurrency implication for this scenario's scale

---

### Output Structure

Produce output in this exact order:

1. **Change Scope Pin**: `{Entity}.{Field}: {old} → {new}` (context: {action})

2. **Platform Term Contract**: Approved terms for PA Flow Type and execution tier for this
   scenario. Any unlisted term: mark `[NC: {term}]`.

3. **Candidate Manifest** [Override 1]: Table with M-Ref IDs, count declared.
   ```
   Candidate count: N.  ← must appear here before Section 4 begins
   ```

4. **Execution Sequence** [Override 2, 3, 4, 6]: All manifest entries as firing rows or
   inline gap tokens, in execution order (sync before async). Cascades as child rows with
   cascade labels.

5. **Denominator Reconciliation**: Table confirming all M-Refs disposed. Totals = denominator.

6. **Anomaly Verdicts** [Override 5]: Three verdict blocks (Storm, Missing Trigger, Circular
   Dependency). Each block cites specific sequence rows from Section 4.

---

Scope constraint: Only triggers that respond to the specific entity, field, and change value
in the Change Scope Pin are in scope.

Now receive the scenario and produce the output.
