# Flow-Trigger Skill — Round 2 Variations (Rubric v2, Revised Aspirationals)

**Skill**: flow-trigger — Simulate which automations fire when a record changes.
**Rubric**: v2 (C-01 through C-13; N_aspirational = 5: C-09 through C-13)
**Date**: 2026-03-15

---

## Variation Design Notes

Rubric v2 (revised) promotes execution tier/latency to aspirational (C-09), retains cascade
completeness (C-10), and introduces three new aspirational criteria:

| Criterion | Root Failure Mode |
|-----------|------------------|
| C-11 — Candidate denominator declared | **Denominator Post-Declaration**: candidate list appears after or alongside enumeration; non-firers excluded from declared set |
| C-12 — Gap tokens for non-firing candidates | **Silent Candidate Omission**: a candidate evaluated and rejected simply disappears from the numbered sequence with no disposal token |
| C-13 — Anomaly verdict evidence citation | **Citation-Free Verdict**: anomaly verdict makes a claim without referencing specific numbered rows; reviewers cannot audit without re-running the analysis |

These three are the primary targets. Each variation names a structural innovation to drive one
or more criteria mechanically rather than through instruction compliance.

**Variation map**:

| Variation | Axis | Primary Criteria | Hypothesis |
|-----------|------|-----------------|------------|
| V-01 | Role sequence | C-11, C-13 | Separating Scanner and Verdict Analyst roles creates two structural dependencies — denominator locked before enumeration, verdicts cite rows from enumeration — that drive C-11 and C-13 without relying on inline instructions |
| V-02 | Output format | C-12, C-10 | Pre-allocating a numbered slot for every candidate makes disposal tokens fill mandatory structural positions rather than optional annotations; the cascade-spawn field drives C-10 as a per-entry decision |
| V-03 | Phrasing register | C-13 | A mandatory three-part verdict sub-structure (ROW RANGE → FINDING → VERDICT) makes evidence citation a named slot with a visible gap when absent, not an instruction that can be quietly skipped |
| V-04 | Role sequence + output format | C-11, C-12 | Ordering the sequence by Phase 1 C-ID creates a one-to-one mapping between denominator and sequence entries; every C-ID slot must be filled with either a firing entry or a disposal entry |
| V-05 | Phrasing register + inertia framing | C-11, C-12, C-13 | Naming all three new failure modes with their inline detection tags gives the model vocabulary to self-annotate structural violations; a model that understands why each requirement exists is more likely to comply than one given only the requirement |

---

## V-01 — Role Sequence: Scanner → Enumerator → Verdict Analyst

**Variation axis**: Role sequence
**Hypothesis**: Prior variations declare the candidate list and enumeration in the same
section — so the denominator and firing set interleave in the model's attention. The model
can retrospectively fit the pre-scan to the firing set it already generated. V-01 hard-
separates these into three sequential roles: the Scanner role must complete and lock its
denominator before the Enumerator role opens; the Verdict Analyst role has a contractual
constraint to cite entry numbers from the Enumerator output. Two structural dependencies —
Scanner output required for Enumerator input, Enumerator rows required for Verdict citations
— drive C-11 and C-13 without relying on instruction compliance. Neither role can begin
until its upstream role is complete.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert operating in three sequential roles.
Complete each role in full before beginning the next. Do not merge roles or anticipate later-
role output while executing an earlier role.

---

#### ROLE A — SCANNER

**Task**: Declare the candidate denominator. Do not evaluate conditions. Do not determine
which triggers fire. This role produces the only authoritative candidate list for the
entire analysis.

**A-1 — Change Scope Pin**

Restate the change event in one line:
> Scope: `{Entity}.{Field}` changed from `{old value}` to `{new value}` — context: `{action}`

This scope boundary governs Roles B and C. Triggers that do not respond to this entity +
field change are out of scope for the entire analysis.

**A-2 — Candidate Denominator**

List every trigger that *could* fire based on entity, field, and trigger type alone. Include
triggers whose conditions might prevent firing. Do not exclude any trigger based on condition
evaluation.

| C-ID | Trigger Name | PA Flow Type | Matching Basis |
|---|---|---|---|
| C-01 | | `Automated – Dataverse` / `Automated – SharePoint` / `Automated – HTTP` / `Instant` / `Scheduled` | |

**Denominator N = [count]. Locked.** All C-IDs in this table must be accounted for in Role B.

**A-3 — Scanner Handoff**

Deliver to Role B: N candidates — [list by C-ID and name].

Role B may not introduce a trigger absent from this table without marking it
`[NOT IN SCANNER: reason]`. Role B may not remove a C-ID without producing either a
firing entry or a disposal entry for it.

---

#### ROLE B — ENUMERATOR

**Task**: For each candidate from Role A, determine whether it fires and produce a numbered
sequence entry. Every C-ID from Role A must appear in the sequence — either as a firing entry
or as a disposal entry. No C-ID may be silently omitted.

**Firing Entry format** (use when the candidate fires):

**Entry #[N] — [Trigger Name]** (C-ID: [from Role A])
- **PA flow type**: exact term from Role A vocabulary (`Automated – Dataverse` /
  `Automated – SharePoint` / `Automated – HTTP` / `Instant` / `Scheduled`)
- **Execution tier**: `Sync (blocks transaction)` or `Async (~N min [standard|premium] tier)`
- **Condition**: `No condition` or: `Evaluates [text]. Taken: [branch] — [reason]. Skipped: [branch] — [reason].`
- **Reads**: `{Entity}.{Field}` per consumed field
- **Produces**: [lead word: `Sets` / `Creates` / `Deletes` / `Sends email via` / `Calls HTTP` /
  `Starts child flow:` / `Posts adaptive card to`] + connector + target + resulting state
- **Side-effect writes**: `{Entity}.{Field} = {value}` per write, or `None`
- **Cascade**: if a side-effect write matches any C-ID's trigger condition, the downstream
  trigger must be the immediately next numbered entry before the sequence returns to C-ID order

**Disposal Entry format** (use when the candidate does not fire):

**Entry #[N] — [Trigger Name]** (C-ID: [from Role A])
`[NOT FIRED — {reason: condition not taken: [branch result] / field filter mismatch: [detail] / context mismatch: [detail] / FLAGGED GAP: [expected automation absent]}]`

Process candidates Sync-tier first, Async-tier second. Within each tier, use Role A C-ID order.

**B-Summary** (required before Role C begins):
- Total candidates processed: N (must equal Role A denominator N)
- Firing entries: N (list entry #s and trigger names)
- Disposal entries: N (list entry #s and C-IDs)
- Cascade insertions: N (list entry #s and parent C-IDs; not counted in primary slot total)

---

#### ROLE C — VERDICT ANALYST

**Task**: For each of the three anomaly classes, produce an evidence block followed by a
verdict. Every evidence block must cite specific entry numbers from Role B's numbered
sequence. A verdict that appears without entry-number citations is a `[BARE ASSERTION]`.

Role C reads only from the Role B output and B-Summary. Do not re-evaluate triggers.
All findings must reference specific Role B entry numbers.

---

**C-1 — Trigger Storm**

Evidence:
- Firing entry count: [from B-Summary — cite total and list entry #s by name]
- Re-entry check: [for each side-effect write in Role B, state whether the written field
  appears in any C-ID's trigger condition — name the Role B entry # and field for each check]
- Entry numbers inspected: #[list]

Verdict: `CLEARED (count = N, no re-entry; inspected entries: #[list])` or
`STORM DETECTED (count = N; storm entries: #[list]; re-entry: [field → trigger name])`

Mitigation if STORM DETECTED: [debounce strategy / guard condition / concurrency control]

---

**C-2 — Missing Triggers**

Evidence:
- Disposal entries from Role B: [list each entry # with C-ID and its [NOT FIRED] reason]
- FLAGGED GAP disposals: [list entry #s, or "none"]

Verdict: `CLEARED (N candidates: N fired at #[list]; N disposed at #[list]; 0 flagged gaps)`
or `MISSING TRIGGER: [name — entry # — gap cause — risk level]`

Mitigation if MISSING TRIGGER: [trigger registration fix / condition correction / scope clarification]

---

**C-3 — Circular Triggers**

Evidence:
- Entries with side-effect writes: [list entry # → `{Entity.Field} = {value}` per write]
- Directed edges constructed: `Entry #[N] [Trigger A] writes {Entity.Field} → fires [Trigger B]`
  (one edge per write that matches a C-ID trigger condition)
- Entry numbers contributing edges: #[list, or "none — no writes with downstream potential"]
- Graph property: DAG / CYCLIC

Verdict: `CLEARED (DAG confirmed; edges from entries #[list]: {listed edges})` or
`CIRCULAR TRIGGER: [full cycle path with entry numbers]`

Mitigation if CIRCULAR TRIGGER: [cycle-break condition / run-once flag / depth limit]

---

Now receive the scenario and trigger registry. Execute Role A completely, then Role B
completely, then Role C.

---

## V-02 — Output Format: Full-Roster Sequence (Pre-Allocated Slots)

**Variation axis**: Output format
**Hypothesis**: All prior variations write the firing sequence and handle non-firers in a
separate reconciliation table. The reconciliation table may be well-structured, but it
operates on a different axis — a reader who reads only the firing sequence sees no evidence
of candidates that did not fire. V-02 collapses both streams into a single numbered sequence
by pre-allocating a slot for every candidate. Each slot fills with a firing entry if the
candidate fires, or with a `[NOT FIRED — reason]` disposal token if it does not. The cascade
rule inserts cascade children between the parent slot and the next C-ID slot. This makes the
sequence self-contained: every C-ID is present. C-12 is satisfied by construction — there is
no mechanism for silent omission once all slots are pre-allocated.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Produce a trigger fire report using
the Full-Roster Sequence format described below.

---

#### SECTION 1 — SCOPE AND CANDIDATE ROSTER

State the change event:
> **Scope**: `{Entity}.{Field}` changed from `{old}` to `{new}` — context: `{action}`

List all candidates before any evaluation:

| C-ID | Trigger Name | PA Flow Type | Matching Basis |
|---|---|---|---|
| C-01 | | `Automated – Dataverse` / `Automated – SharePoint` / `Automated – HTTP` / `Instant` / `Scheduled` | |

**Roster count N = [count]**. Section 2's Full-Roster Sequence will contain exactly N primary
slots — one per candidate in C-ID order — plus any cascade insertions. Every C-ID listed here
must appear in the sequence. A C-ID absent from the sequence is a structural gap.

---

#### SECTION 2 — FULL-ROSTER SEQUENCE

List all candidates in roster order: Sync-tier C-IDs first, Async-tier C-IDs second.
For each C-ID, produce one of two slot types:

---

**Firing Slot** — use when the candidate fires:

**Slot [C-ID] / Entry #[seq]: [Trigger Name]**

| Field | Value |
|---|---|
| PA flow type | exact term from Section 1 vocabulary |
| Execution tier | `Sync (blocks transaction)` or `Async (~N min [standard\|premium] tier)` |
| Condition | `No condition` or: `Evaluates [text]. Taken: [branch] — [reason]. Skipped: [branch] — [reason].` |
| Reads | `{Entity}.{Field}` per consumed field, comma-separated |
| Produces | [lead: `Sets` / `Creates` / `Deletes` / `Sends email via` / `Calls HTTP` / `Starts child flow:` / `Posts adaptive card to`] + connector + target + resulting state |
| Side-effect writes | `{Entity}.{Field} = {value}` per write, or `None` |
| Cascade spawns? | `NO — [reason: no writes / write does not match any Section 1 C-ID's trigger condition]` or `YES → insert Entry #[seq+1]: [downstream trigger name] before next C-ID slot` |

---

**Disposal Slot** — use when the candidate does not fire:

**Slot [C-ID] / Entry #[seq]: [Trigger Name]**
`[NOT FIRED — {reason}]`

Reason must be specific — one of:
- `condition not taken: [branch evaluation result for this change]`
- `field filter mismatch: [field or value that blocked the trigger matching]`
- `context mismatch: [initiating context or action that prevented firing]`
- `permission gate: [ownership or permission condition not satisfied]`
- `FLAGGED GAP: [reason this trigger was expected to fire but is absent]`

Generic reasons ("not applicable", "not relevant") do not satisfy the disposal requirement.

---

**Cascade insertion rule**: When a Firing Slot's "Cascade spawns?" is YES, insert the cascade
child as the immediately next entry (seq+1) before continuing to the next C-ID in roster order.
Cascade children use the Firing Slot format with C-ID set to `[CASCADE — parent: C-ID]`.
A cascade child's "Cascade spawns?" field follows the same rules as primary entries.

---

**Sequence completeness verification** (write after the last entry):

- Primary slots filled (one per Section 1 C-ID): N / N
- Firing slots: N
- Disposal slots: N
- Cascade insertions: N (not counted in primary slot total)
- Any missing C-IDs from Section 1: [list, or "none"]

---

#### SECTION 3 — PATHOLOGY VERDICTS

Address all three anomaly classes. Each verdict must cite specific Section 2 entry numbers
as evidence.

**Trigger Storm**
- Firing entries from Section 2: [list entry #s and trigger names]
- Total distinct executions: N; cascade children: N; grand total: N
- Re-entry check: [for each YES cascade-spawn entry, does the child's side-effect write feed
  back to any Section 1 C-ID's trigger condition? List entry # → field → C-ID]
- Storm threshold: > 3 distinct trigger executions per change event
- Verdict: `CLEARED (total = N, no re-entry; Section 2 entries inspected: #[list])` or
  `STORM DETECTED (entries: #[list]; count = N; re-entry path: [field → entry #])`

**Missing Triggers**
- Disposal slots with `FLAGGED GAP` from Section 2: [list entry #s and C-IDs, or "none"]
- Verdict: `CLEARED (N candidates: N fired, N disposed with confirmed reasons, 0 flagged gaps)` or
  `MISSING TRIGGER: [name — entry # — gap cause — risk level]`

**Circular Triggers**
- Directed edges from Section 2 side-effect writes: `Entry #[N] writes {Entity.Field} → fires {trigger}` per edge
- Entry numbers contributing edges: #[list, or "none"]
- Graph property: DAG / CYCLIC
- Verdict: `CLEARED (DAG; edges from entries #[list]: {edges listed})` or
  `CIRCULAR TRIGGER: [cycle path with entry numbers]`

---

Now receive the scenario and trigger registry. Begin with Section 1.

---

## V-03 — Phrasing Register: Evidence-Row-Verdict (ERV) Sub-Structure

**Variation axis**: Phrasing register (mandatory named sub-sections within verdict blocks)
**Hypothesis**: Evidence citation instructions ("cite specific entry numbers") can be satisfied
narrowly by inserting a single row reference anywhere in the verdict block. A model that
writes "CLEARED — entries 1-4 inspected" has technically cited rows but without stating
what was found at those rows. V-03 makes evidence citation a three-part named sub-structure:
ROW RANGE (which entries were inspected), FINDING (what was observed at those entries), and
VERDICT (the verdict sentence). A VERDICT that appears without a preceding ROW RANGE and
FINDING is structurally incomplete — a named slot is visibly empty. A ROW RANGE that says
"all entries" without numbering them is a weak pass. This makes C-13 a fill-in-the-blank
requirement with observable failure modes, not a qualitative judgment call.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. This protocol specifies the
Evidence-Row-Verdict (ERV) structure for trigger fire reports. Apply it exactly.

---

#### STEP 1 — CANDIDATE PRE-SCAN

Before determining which triggers fire, list all candidates. This step must appear before
Step 2. A candidate list that first appears within or after Step 2 is a structural error.

| C-ID | Trigger Name | PA Flow Type | Matching Basis |
|---|---|---|---|
| C-01 | | `Automated – Dataverse` / `Automated – SharePoint` / `Automated – HTTP` / `Instant` / `Scheduled` | |

Denominator N = [count]. Every C-ID must be accounted for in Step 2.

---

#### STEP 2 — TRIGGER ENUMERATION

List all candidates in execution-tier order (Sync first, Async second). For each C-ID,
produce a numbered entry — either a firing entry or a disposal entry.

**Firing entry** (candidate fires):

**Entry #[N] — [Trigger Name]** (C-ID: [from Step 1], or `[NOT IN PRE-SCAN: reason]`)
- **PA flow type**: `Automated – Dataverse` / `Automated – SharePoint` / `Automated – HTTP` / `Instant` / `Scheduled`
- **Execution tier**: `Sync (blocks transaction)` or `Async (~N min [standard|premium] tier)`
- **Condition**: `No condition` or: `Evaluates [text]. Taken: [branch] — [reason]. Skipped: [branch] — [reason].`
- **Reads**: `{Entity}.{Field}` per consumed field
- **Produces**: [lead: `Sets` / `Creates` / `Deletes` / `Sends email via` / `Calls HTTP` / `Starts child flow:` / `Posts adaptive card to`] + connector + target + resulting state
- **Side-effect writes**: `{Entity}.{Field} = {value}` per write, or `None`
- **Cascade**: if a side-effect write matches any C-ID's trigger condition, the downstream trigger must be the immediately next numbered entry

**Disposal entry** (candidate does not fire):

**Entry #[N] — [Trigger Name]** (C-ID: [from Step 1])
`[NOT FIRED — {reason: condition not taken: [result] / field filter mismatch: [detail] / context mismatch: [detail] / FLAGGED GAP: [cause]}]`

---

#### STEP 3 — CANDIDATE RECONCILIATION

| C-ID | Trigger Name | Resolution | Entry # | Reason |
|---|---|---|---|---|

Resolution: `FIRED` / `CONFIRMED ABSENT — [specific reason]` / `FLAGGED GAP — [reason]`

---

#### STEP 4 — EVIDENCE-ROW-VERDICT PATHOLOGY ASSESSMENT

For each of the three anomaly classes, produce three named sub-sections in this order:

1. **ROW RANGE** — the specific entry numbers inspected for this class
2. **FINDING** — what was observed at those entry numbers (counts, field values, edge paths)
3. **VERDICT** — a single sentence beginning with `CLEARED` or the detected anomaly name

A VERDICT that appears without a preceding ROW RANGE and FINDING sub-section is structurally
incomplete: mark it `[ERV VIOLATION: verdict present; row-range sub-section absent]`.

A ROW RANGE that says only "all entries" without listing specific numbers is a weak pass;
citing specific entry numbers and what was checked per entry is a full pass.

---

**CLASS 1: TRIGGER STORM**

**ROW RANGE**:
> Entries inspected for storm analysis: #[list each firing entry number and trigger name]
> Total distinct executions counted: N

**FINDING**:
> For each entry in the ROW RANGE — does this entry's side-effect write feed back into any
> other entry in the firing set? (State the entry #, the field written, and whether it matches
> any C-ID's trigger condition.)
> Re-entry paths identified: [describe path with entry numbers, or "none"]

**VERDICT**: `CLEARED (count = N, no re-entry; entries inspected: #[list])` or
`STORM DETECTED (count = N; storm entries: #[list]; re-entry: [field → entry #])`

Mitigation if STORM DETECTED: [debounce / guard condition / concurrency control]

---

**CLASS 2: MISSING TRIGGERS**

**ROW RANGE**:
> Firing entries: #[list] — these candidates are present in the sequence
> Disposal entries: #[list] — these candidates are absent from the firing set

**FINDING**:
> For each disposal entry — restate its [NOT FIRED] reason. Identify any disposal entry
> whose reason indicates an expected automation that should have fired.
> FLAGGED GAP entries: [list entry #s with C-IDs, or "none"]

**VERDICT**: `CLEARED (N candidates: N fired at #[list]; N disposed at #[list]; 0 flagged gaps)` or
`MISSING TRIGGER: [name — entry # — gap cause — risk level]`

Mitigation if MISSING TRIGGER: [trigger registration fix / condition correction]

---

**CLASS 3: CIRCULAR TRIGGERS**

**ROW RANGE**:
> Entries with side-effect writes (candidates for circular dependency): #[list, or "none — no side-effect writes in Step 2"]

**FINDING**:
> For each entry in the ROW RANGE — construct the directed edge:
> `Entry #[N] [Trigger A] writes {Entity.Field} → fires [Trigger B at entry #[M]]`
> or `Entry #[N] write does not fire any other entry in the sequence`
> Full directed edge set: [list edges, or "no edges — no writes with downstream automation potential"]
> Graph property: DAG / CYCLIC

**VERDICT**: `CLEARED (DAG confirmed; edges from entries #[list]: {edges listed})` or
`CIRCULAR TRIGGER: [full cycle path with entry numbers]`

Mitigation if CIRCULAR TRIGGER: [cycle-break condition / run-once guard / depth limit]

---

Now receive the scenario and trigger registry. Begin with Step 1. Apply the ERV structure
exactly for each class in Step 4.

---

## V-04 — Combined: Role Sequence + Output Format (Denominator-Ordered Roster)

**Variation axis**: Role sequence + output format
**Hypothesis**: V-01 separates the Scanner role (denominator) from the Enumerator role
(sequence) to drive C-11. V-02 pre-allocates C-ID slots in the sequence to drive C-12.
V-04 combines these by making the sequence C-ID ordered rather than execution-tier ordered.
The Scanner phase declares candidates in two groups — Sync group first, Async group second —
and each C-ID receives exactly one primary slot in the Phase 2 sequence. The slot fills with
either a firing entry or a disposal entry. Cascade children are inserted between the parent
slot and the next C-ID slot. This creates a one-to-one mapping between denominator and
sequence: N candidates in Phase 1 produces exactly N primary sequence slots in Phase 2.
Silent omission is structurally impossible — the slot exists and must be filled.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert. Produce a trigger fire report in
two phases. Complete Phase 1 before beginning Phase 2.

---

#### PHASE 1 — DENOMINATOR DECLARATION

Declare the full candidate set before any evaluation begins. Group candidates by execution
tier: Sync candidates first, then Async candidates.

**Sync Group** (triggers that execute inline and block the transaction):

| C-ID | Trigger Name | PA Flow Type | Matching Basis |
|---|---|---|---|
| C-S01 | | `Automated – Dataverse` / `Instant` | |

Sync group count: N

**Async Group** (fire-and-forget triggers):

| C-ID | Trigger Name | PA Flow Type | Matching Basis |
|---|---|---|---|
| C-A01 | | `Automated – Dataverse` / `Automated – SharePoint` / `Automated – HTTP` / `Instant` / `Scheduled` | |

Async group count: N

**Total denominator: N = [Sync N] + [Async N]**

This phase is the authoritative candidate set. Phase 2 must produce exactly N primary slots
covering every C-ID. A C-ID absent from Phase 2 is a structural gap.

---

#### PHASE 2 — DENOMINATOR-ORDERED SEQUENCE

Produce entries in C-ID order: all Sync group C-IDs first (C-S**), then all Async group
C-IDs (C-A**). For each C-ID, produce exactly one primary slot entry:

---

**Firing Entry** (candidate fires):

**Entry #[seq] / Slot [C-ID]: [Trigger Name]**

| Field | Value |
|---|---|
| Execution tier | `Sync (blocks transaction)` or `Async (~N min [standard\|premium] tier)` |
| Condition | `No condition` or: `Evaluates [text]. Taken: [branch] — [reason]. Skipped: [branch] — [reason].` |
| Reads | `{Entity}.{Field}` per consumed field |
| Produces | [lead: `Sets` / `Creates` / `Deletes` / `Sends email via` / `Calls HTTP` / `Starts child flow:` / `Posts adaptive card to`] + connector + target + resulting state |
| Side-effect writes | `{Entity}.{Field} = {value}` per write, or `None` |
| Cascade? | `NO` or `YES → insert Entry #[seq+1]: [downstream trigger name]` (cascade child inserted before next C-ID slot) |

---

**Disposal Entry** (candidate does not fire):

**Entry #[seq] / Slot [C-ID]: [Trigger Name]**
`[NOT FIRED — {reason: condition not taken: [result] / field filter mismatch: [detail] / context mismatch: [detail] / FLAGGED GAP: [expected behavior absent]}]`

---

**Cascade children** appear as numbered entries immediately after the parent's slot and before
the next C-ID slot in C-ID order. Format: Firing Entry with C-ID field set to
`[CASCADE from C-ID]`. Cascade children also have a Cascade? field following the same rules.

---

**Phase 2 completeness verification** (required after the last entry):

| Metric | Value |
|---|---|
| Phase 1 denominator | N |
| Primary slots filled | N (one per C-ID — must equal denominator) |
| Firing entries | N |
| Disposal entries | N |
| Cascade insertions | N |
| Missing C-IDs | [list, or "none"] |

---

#### PHASE 3 — PATHOLOGY VERDICTS

Address all three anomaly classes. Each verdict must reference specific Phase 2 entry numbers.

**Trigger Storm**
- Firing entries: [list C-IDs and entry #s from Phase 2]
- Total distinct executions: N (primary) + N (cascade insertions) = N grand total
- Re-entry check: [for each YES Cascade entry, does the child's side-effect write match any
  Phase 1 C-ID's trigger condition? List: entry # → field → C-ID → verdict]
- Storm threshold: > 3 distinct trigger executions per change event
- Verdict: `CLEARED (total = N; no re-entry; Phase 2 entries inspected: #[list])` or
  `STORM DETECTED (entries: #[list]; count = N; re-entry: [path with entry #s])`
- Mitigation if STORM DETECTED: [debounce / condition guard / re-entry block]

**Missing Triggers**
- Disposal entries from Phase 2: [list entry #s, C-IDs, and [NOT FIRED] reasons]
- FLAGGED GAP disposals: [list entry #s, or "none"]
- Verdict: `CLEARED (N: N fired, N disposed confirmed, 0 flagged gaps; Phase 2 entries: #[list])` or
  `MISSING TRIGGER: [C-ID — entry # — gap cause — risk level]`
- Mitigation if MISSING TRIGGER: [registration fix / condition correction]

**Circular Triggers**
- Directed edges from Phase 2 side-effect writes: `Entry #[N] ([C-ID]) writes {Entity.Field} → fires [C-ID/trigger]`
- Entry numbers contributing edges: #[list, or "none"]
- Graph property: DAG / CYCLIC
- Verdict: `CLEARED (DAG confirmed; edges from entries #[list]: {edges listed})` or
  `CIRCULAR TRIGGER: [full cycle path with entry numbers and C-IDs]`
- Mitigation if CIRCULAR TRIGGER: [cycle-break condition / run-once flag / depth limit]

---

Now receive the scenario and trigger registry. Begin with Phase 1.

---

## V-05 — Combined: Phrasing Register + Inertia Framing (Three New Failure Modes Named)

**Variation axis**: Phrasing register (formal normative) + inertia framing
**Hypothesis**: R2/v1 variations named five failure modes that drove strong structural
compliance for criteria through C-10. Rubric v2 adds three aspirational criteria — C-11,
C-12, C-13 — whose failure modes were not yet named. V-05 names them: "Denominator Post-
Declaration" (C-11 miss), "Silent Candidate Omission" (C-12 miss), and "Citation-Free
Verdict" (C-13 miss). Each failure mode receives a formal SHALL requirement and an inline
detection tag. The hypothesis is that naming failure modes and their detection tags in the
same section creates the strongest motivation for self-annotation: a model that understands
WHY each requirement exists applies it more structurally than one given only the requirement.
This drives all three new aspirational criteria simultaneously and produces outputs that are
self-auditing without needing expert review.

---

### Prompt Body

You are a Power Automate / Copilot Studio domain expert conducting a trigger fire analysis.

---

#### NINE FAILURE MODES OF INFORMAL TRIGGER ANALYSIS

Review nine failure modes before the protocol. Each maps to a criterion and has a formal
SHALL requirement with an inline detection tag.

---

**Failure Mode 1 — Undeclared Denominator**
Analysis begins by listing what fires. Triggers never considered leave silence, not a gap.
A reviewer cannot distinguish "considered and excluded" from "never considered."
Maps to: C-01 (trigger enumeration completeness).
*Protocol response*: candidate pre-scan runs before any outcome determination. Denominator
count declared and locked. All candidates must be resolved.

**Failure Mode 2 — Closed-Set Pathology Scan**
Pathology identification happens after the firing set locks in. Anomaly classes with no
instances are silently omitted. Maps to: C-04 (all three anomaly classes assessed).
*Protocol response*: all three anomaly classes SHALL be addressed with named verdicts.
A class may be CLEARED but not silently omitted.

**Failure Mode 3 — Vocabulary Drift**
Non-platform terms like "sends a notification" or "cloud flow" pass informal review.
Maps to: C-05 (platform grounding).
*Protocol response*: governed term sets defined at Section 0. Non-conforming values:
apply `[VOCAB FAIL: actual text]` inline.

**Failure Mode 4 — Branch Amnesia**
Conditional triggers document only the branch that fires. The skipped branch is omitted.
Maps to: C-07 (conditional branch paths).
*Protocol response*: every conditional trigger SHALL declare both branches with reasons.
Single-branch declaration: apply `[BRANCH MISSING: only taken branch declared]` inline.

**Failure Mode 5 — Latency Blindness**
Sync and async triggers are mixed without tier labeling. Async latency is omitted.
Maps to: C-09 (execution tier and latency flags).
*Protocol response*: every trigger SHALL declare its tier; Async triggers SHALL include a
numeric latency estimate. Missing tier: apply `[TIER UNDECLARED]` inline.

**Failure Mode 6 — Cascade Annotation Without Continuation**
A side-effect write with downstream automation potential is noted but does not spawn a new
trigger entry. Maps to: C-10 (cascade completeness).
*Protocol response*: any side-effect write matching a candidate's trigger condition SHALL
produce the downstream trigger as the immediately following numbered entry. Write noted but
not continued: apply `[CASCADE GAP: {trigger name} write not continued]` inline.

**Failure Mode 7 — Denominator Post-Declaration**
The candidate list appears in the same section as or after the firing enumeration. The model
fills in the denominator retroactively to match the firing set already generated. The pre-scan
is not actually predictive of the firing set — it reflects it. Maps to: C-11 (candidate
denominator declared before enumeration).
*Protocol response*: the candidate pre-scan SHALL be a separate named section that completes
before the firing enumeration section begins. A candidate list that first appears within or
after the enumeration: apply `[DENOMINATOR POST-DECLARED: {section where it appeared}]`.

**Failure Mode 8 — Silent Candidate Omission**
A candidate from the pre-scan does not appear in the firing sequence. No disposal token
marks its absence. A reviewer counting sequence entries versus pre-scan entries finds the
discrepancy only if they remember the pre-scan count. Maps to: C-12 (gap tokens for non-
firing candidates).
*Protocol response*: every candidate that does not fire SHALL appear in the numbered sequence
as a disposal entry with an explicit gap token and stated reason. A pre-scan candidate that
is absent from the sequence without a disposal token: apply `[SILENT OMISSION: {candidate name}]`
after the last sequence entry.

**Failure Mode 9 — Citation-Free Verdict**
An anomaly verdict asserts a finding without referencing the specific numbered entries from
the sequence that support it. A reviewer cannot audit the verdict without re-running the
full analysis. Clean verdicts are equally at risk — "CLEARED — no circular triggers" without
citing the rows inspected cannot be verified. Maps to: C-13 (anomaly verdict evidence citation).
*Protocol response*: every anomaly verdict — clean or positive — SHALL cite the specific
entry numbers from the firing sequence that were inspected to reach the verdict. A verdict
without specific entry number citations: apply `[CITATION FREE: {verdict class}]`.

The protocol below addresses each failure mode at its structural root.

---

#### SECTION 0 — GOVERNED TERM SETS (addresses Failure Mode 3)

**Term Set A — PA Flow Type** (non-conforming: apply `[VOCAB FAIL: actual text]`)
`Automated – Dataverse` / `Automated – SharePoint` / `Automated – HTTP` / `Instant` / `Scheduled`

**Term Set B — Execution Tier** (non-conforming: apply `[TIER UNDECLARED]`)
`Sync (blocks transaction)` or `Async (~N min [standard|premium] tier)` — N must be numeric

**Term Set C — Input Field Reference** (non-conforming: apply `[VOCAB FAIL: actual text]`)
Pattern: `{TableName}.{ColumnName}` — any reference that omits table or column name
is non-conforming

**Term Set D — Output Action Lead** (non-conforming: apply `[VOCAB FAIL: actual text]`)
First word must be: `Sets` / `Creates` / `Deletes` / `Sends email via` / `Calls HTTP` /
`Starts child flow:` / `Posts adaptive card to`

**Term Set E — Branch Coverage** (non-conforming: apply `[BRANCH MISSING: only taken branch declared]`)
For conditional triggers: `Taken: [branch] — [reason]` AND `Skipped: [branch] — [reason]`
For unconditional triggers: `No condition`

---

#### SECTION 1 — CANDIDATE PRE-SCAN (addresses Failure Modes 1, 7)

This section SHALL appear as a distinct section before Section 2. A candidate list that
appears for the first time within or after Section 2: apply
`[DENOMINATOR POST-DECLARED: {section where first appeared}]`.

| C-ID | Trigger Name | Type (Term Set A) | Matching Basis |
|---|---|---|---|
| C-01 | | | |

**Denominator N = [count]**. All C-IDs SHALL be accounted for in Section 2 — either as a
firing entry or as a disposal entry. A C-ID absent from Section 2 without a disposal entry:
apply `[SILENT OMISSION: {trigger name}]` after the last Section 2 entry.

---

#### SECTION 2 — TRIGGER ENUMERATION (addresses Failure Modes 3, 4, 5, 6, 8)

List all candidates in execution-tier order (Sync first, Async second). For each C-ID,
produce one entry — firing or disposal.

**Firing entry** (candidate fires):

**Entry #[N] — [Trigger Name]** (C-ID: [from Section 1], or `[NOT IN PRE-SCAN: reason]`)

| Field | Constraint |
|---|---|
| PA flow type | Term Set A — `[VOCAB FAIL: actual]` if non-conforming |
| Execution tier | Term Set B — `[TIER UNDECLARED]` if absent or non-numeric |
| Condition | Term Set E — `[BRANCH MISSING: only taken branch declared]` if single-branch |
| Reads | Term Set C — `[VOCAB FAIL: actual]` if non-conforming |
| Produces | Term Set D lead + connector + target + state — `[VOCAB FAIL: actual]` or `[INSUFFICIENT]` as needed |
| Side-effect writes | `{Entity}.{Field} = {value}` per write, or `None` |
| Cascade continuation | If write matches any Section 1 C-ID's trigger condition: downstream trigger MUST be Entry #[N+1]. If not continued: `[CASCADE GAP: {trigger name} write not continued]` |

**Disposal entry** (candidate does not fire):

**Entry #[N] — [Trigger Name]** (C-ID: [from Section 1])
`[NOT FIRED — {reason: condition not taken: [result] / field filter mismatch: [detail] / context mismatch: [detail] / FLAGGED GAP: [expected behavior absent]}]`

Omitting this entry for a non-firing candidate: `[SILENT OMISSION: {trigger name}]` after
the last entry.

---

#### SECTION 3 — CANDIDATE RECONCILIATION (addresses Failure Mode 2)

| C-ID | Trigger Name | Entry # | Resolution | Reason |
|---|---|---|---|---|

Resolution: `FIRED` / `CONFIRMED ABSENT — [specific reason]` / `FLAGGED GAP — [reason]`
Totals: N FIRED, N CONFIRMED ABSENT, N FLAGGED GAP

---

#### SECTION 4 — PATHOLOGY VERDICTS (addresses Failure Modes 2, 9)

Each verdict SHALL cite specific Section 2 entry numbers as evidence. A verdict without
entry number citations: apply `[CITATION FREE: {class name}]`.

---

**Trigger Storm**

Evidence from Section 2:
- Firing entries: #[list by number and trigger name]
- Total distinct executions: N
- Re-entry check: [for each side-effect write in Section 2, state whether the written field
  appears in any Section 1 C-ID's trigger condition — list: entry # → field → C-ID → result]
- Entries inspected for re-entry analysis: #[list]

Verdict: `CLEARED (count = N, no re-entry; entries inspected: #[list])` or
`STORM DETECTED (count = N; storm entries: #[list]; re-entry: [field → entry #])`

Mitigation if STORM DETECTED: [debounce strategy / guard condition / re-entry flag]

---

**Missing Triggers**

Evidence from Section 2:
- Disposal entries: [list each: entry # → C-ID → [NOT FIRED] reason]
- FLAGGED GAP entries: [list entry #s, or "none"]

Verdict: `CLEARED (N: N fired at #[list]; N disposed at #[list]; 0 flagged gaps)` or
`MISSING TRIGGER: [name — entry # — gap cause — risk level]`

Mitigation if MISSING TRIGGER: [trigger registration fix / condition correction]

---

**Circular Triggers**

Evidence from Section 2:
- Entries with side-effect writes: #[list, or "none"]
- Directed edges: `Entry #[N] [Trigger A] writes {Entity.Field} → fires [Trigger B]` per edge
- Entries contributing edges: #[list, or "none — no writes with downstream automation potential"]
- Graph property: DAG / CYCLIC

Verdict: `CLEARED (DAG confirmed; edges from entries #[list]: {edges listed})` or
`CIRCULAR TRIGGER: [full cycle path with entry numbers]`

Mitigation if CIRCULAR TRIGGER: [cycle-break condition / run-once guard / depth limit]

---

Now receive the scenario and trigger registry. Begin with Section 0. Apply all tags inline.
