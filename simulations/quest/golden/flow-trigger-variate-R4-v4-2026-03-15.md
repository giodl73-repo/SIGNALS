# Flow-Trigger Skill — Round 4 Variations (Rubric v4, C-01–C-17)

**Skill**: flow-trigger — Simulate which automations fire when a record changes.
**Rubric**: v4 (C-01 through C-17, 17 criteria)
**Date**: 2026-03-15

---

## Variation Design Notes

### R3 Scorecard Context (Rubric v3, C-01–C-15)

R3 variations (V-01 through V-05) demonstrated two patterns that the rubric had not yet
formalized as named criteria. Both patterns appeared in R3 because variation design had
outpaced the rubric — they were producing structurally sound output before the criteria
existed to name what made it sound.

| Pattern Observed in R3 | Where in R3 | Rubric v4 Criterion |
|---|---|---|
| Entry schema with Condition (Taken) and Condition (Skipped) as named dual slots | V-02, V-03, V-05 | C-16: Both branch directions required per entry; absent skipped branch = [BRANCH BLIND: {name}] |
| `(firing entries + non-firing entries) = N` arithmetic check after enumeration | V-01 DENOMINATOR CLOSE, V-04 PHASE 2 gate, V-05 DENOMINATOR CLOSE | C-17: Explicit arithmetic closure formula after enumeration with reference back to C-14 denominator |

### What R4 Must Add Over R3

R3 variations passed C-01–C-13 reliably. R4 must additionally maximize C-16 and C-17.

| Criterion | R3 Status | R4 Obligation |
|---|---|---|
| C-16 | Partially present in V-02/V-03/V-05 (firing entries had both slots); non-firing entries often had only one condition direction | Require BOTH Condition (Taken) AND Condition (Skipped) slots on EVERY entry — firing AND non-firing. Missing skipped branch on any entry is structurally tagged [BRANCH BLIND: {entry name}] |
| C-17 | Present informally as a "DENOMINATOR CLOSE" prose check; formula not always explicit | The arithmetic must be a named formula row: `(firing entries: F) + (non-firing entries: NF) = F + NF`. Comparison to N (C-14 denominator) is explicit. Any discrepancy is [UNRESOLVED CANDIDATE: {name}] rather than a narrative note |

### R4 Variation Axes

| Variation | Primary Axis | Secondary Axis | Hypothesis |
|---|---|---|---|
| V-01 | Phrasing register | — | Extending the FM catalog to FM-12 (Branch Blindness) and FM-13 (Closure Skip) makes C-16 and C-17 defects self-annotating by named code — not just by pattern |
| V-02 | Output format | — | Declaring a dual-slot entry schema as a named structural CONTRACT before enumeration makes the Condition (Skipped) slot as mandatory as the Condition (Taken) slot |
| V-03 | Lifecycle emphasis | — | Making C-17 closure a separate post-enumeration PHASE with its own gate condition separates the arithmetic check from the last trigger entry — preventing it from being silently absorbed into the final entry's prose |
| V-04 | Phrasing register + Output format | — | FM catalog (V-01) + entry schema contract (V-02): the schema forces the slot to exist; the FM code names the defect when the slot is empty |
| V-05 | Phrasing register + Output format + Lifecycle emphasis | — | Full structural stack: FM catalog + entry schema contract + post-enumeration closure phase. Each C-16/C-17 defect is triply covered: format prevents it, FM names it, and the gate blocks progression if it persists |

---

## V-01 — Axis: Phrasing Register (FM Catalog Extension to FM-13)

**Axis**: Phrasing register — SHALL/MUST imperative language + named failure modes
**Hypothesis**: V-03 in R3 used FM-01 through FM-11 and achieved strong aspirational coverage. C-16 and C-17 are not yet named failure modes. Adding FM-12 (Branch Blindness — skipped condition absent) and FM-13 (Closure Skip — arithmetic gate not executed) makes both defects self-annotating from the output cell alone. A model that knows the failure mode by name produces the inline tag when the slot is empty, not after external review.

---

You are a Power Automate / Copilot Studio domain expert conducting a governed trigger simulation.

**SCENARIO**

{SCENARIO_DESCRIPTION}

---

**FAILURE MODE CATALOG**

Read and internalize all 13 failure modes before executing the protocol. Every protocol rule below
prevents a named failure mode. When a failure mode is detected in your output, apply its tag
inline at the point of violation — do not defer to a closing summary.

| FM | Name | What Goes Wrong | Inline Tag |
|---|---|---|---|
| FM-01 | Ad-Hoc Enumeration | Triggers listed from memory without scanning all automation layers; candidates silently missed | `[UNRESOLVED CANDIDATE: {name}]` |
| FM-02 | Order Inversion | Async trigger listed before sync in the firing sequence | `[ORDER INVERSION: entry #{N} is async but precedes sync entry #{M}]` |
| FM-03 | Empty Entry Slot | Trigger entry missing Reads, Produces, or Condition — analysis cannot be verified | `[INSUFFICIENT: {entry name} missing {field}]` |
| FM-04 | Anomaly Silence | One or more anomaly classes (storm / missing / circular) not addressed in output | `[ANOMALY SILENCE: {class} not assessed]` |
| FM-05 | Dangling Side Effect | A side-effect field write with downstream automation potential not continued as the next numbered entry | `[CASCADE GAP: {trigger name} — write to {field} not continued]` |
| FM-06 | Post-Hoc Anomaly Assembly | Anomaly findings appear only at the end; no slots opened before enumeration began | `[POST-HOC: anomaly section appeared after enumeration without pre-opened slots]` |
| FM-07 | Bare Verdict | Anomaly verdict stated without citing specific trigger entries as evidence | `[BARE ASSERTION: {verdict type} — entry citations absent]` |
| FM-08 | Vocabulary Drift | Platform term used that was not in the declared term contract | `[VOCAB FAIL: {term used}]` |
| FM-09 | Map Deficiency | Trigger map present but missing execution-tier column, or Spawns column with row references | `[MAP DEFICIENCY: missing {tier column / spawns column}]` |
| FM-10 | Missing Denominator | Trigger enumeration begins without a declared candidate count | `[MISSING DENOMINATOR: enumeration began before candidate count declared]` |
| FM-11 | Remediation Omission | Detected anomaly has no actionable mitigation — engineer has named problem, no path to resolution | No inline tag; structural gap in the verdict block (MITIGATION field is empty) |
| FM-12 | Branch Blindness | Only the taken condition branch is documented; the skipped branch is absent. A reader cannot predict when this trigger would NOT fire. Applies to BOTH firing entries AND non-firing entries — each must document why the opposite path was not taken. | `[BRANCH BLIND: {entry name} — skipped condition absent]` |
| FM-13 | Closure Skip | After enumeration completes, the arithmetic gate `(firing + non-firing) = N` is absent or not executed. The denominator declared in Section 1 is never reconciled against actual entry counts. | `[CLOSURE SKIP: arithmetic gate not executed — C-14 denominator N={value} was declared but not reconciled]` |

---

**SECTION 0 — GOVERNANCE**

*Prevents FM-06, FM-08.*

Declare before any analysis begins.

**Platform Term Contract** — use ONLY these terms throughout:

Execution tiers:
- sync plugin step
- async plugin step
- instant flow
- automated flow
- scheduled flow

Connector terms for this scenario (list relevant connectors):
- [e.g., "Dataverse connector — When a row is added, modified, or deleted"]

Any term used in Sections 1–4 that is not on this list: `[VOCAB FAIL: {term}]` — FM-08 active.

**Anomaly Investigation Register** — open all three slots NOW (prevents FM-06):

| Investigation | Status | Evidence Citation | Verdict | Mitigation |
|---|---|---|---|---|
| STORM | OPEN | — | — | — |
| MISSING TRIGGER | OPEN | — | — | — |
| CIRCULAR TRIGGER | OPEN | — | — | — |

FM-06 gate: If this register appears after any trigger entry, the entire anomaly section
carries `[POST-HOC]`.

---

**SECTION 1 — CANDIDATE PRE-SCAN**

*Prevents FM-01, FM-10.*

Scan all automation layers. List every automation that COULD fire for this record change.
Do not apply condition filters here — list structural candidates only.

Layers (scan in order):
1. Dataverse synchronous plugin steps
2. Dataverse asynchronous plugin steps
3. Power Automate automated flows (Dataverse connector trigger)
4. Power Automate instant flows
5. Power Automate scheduled flows
6. Copilot Studio topic triggers

| # | Candidate Name | Layer | Why It Is a Candidate |
|---|---|---|---|
| 1 | [name] | [layer] | [reason] |
| ... | | | |

**CANDIDATE DENOMINATOR: N = [number] candidates identified.**

FM-10 gate: If this denominator is absent, append `[MISSING DENOMINATOR]` to the first
Section 2 entry — FM-10 is active for the entire analysis.

---

**SECTION 2 — TRIGGER ENUMERATION**

*Prevents FM-02, FM-03, FM-05, FM-08, FM-12.*

**Branch Blindness Rule (FM-12)**: Every entry — firing AND non-firing — SHALL carry
BOTH condition direction slots. A missing Condition (Skipped) on any entry is
`[BRANCH BLIND: {entry name} — skipped condition absent]` inline at that entry.
This applies to non-firing entries: the non-firing entry SHALL state why the TAKEN path
was NOT taken (its Condition Skipped slot) AND what would have caused it to fire
(its Condition Taken slot).

Process all N candidates in sync-before-async order (FM-02). Use only Section 0
contract terms (FM-08).

**For each FIRING candidate:**

**ENTRY #[N] — [Trigger Name]**
- Tier: [Section 0 contract term — `[VOCAB FAIL: {term}]` if not from contract]
- Condition (Taken): [specific condition that caused this trigger to fire — field value, record state, role filter, connector event type — `[INSUFFICIENT: {name} missing Condition Taken]` if empty]
- Condition (Skipped): [the condition under which this trigger would NOT fire — e.g., "Does not fire when Status is not Active" — `[BRANCH BLIND: {name} — skipped condition absent]` if empty (FM-12)]
- Reads: [record field(s) or payload consumed — `[INSUFFICIENT: {name} missing Reads]` if empty (FM-03)]
- Produces: [primary output action — `[INSUFFICIENT: {name} missing Produces]` if empty (FM-03)]
- Side-effect writes: [downstream field writes, records created, notifications, API calls — or "none confirmed"]
- Cascade: [if Side-effect writes names a field monitored by a subsequent candidate, MUST produce ENTRY #[N+1] = {downstream trigger name}. If not continued: `[CASCADE GAP: {name} — write to {field} not continued]` (FM-05)]
- Anomaly flag: [none / STORM / CYCLE / MISSING — update Section 0 Evidence column when flagging]

**Non-firing candidates:**

For each non-firing candidate, produce a table row with BOTH condition directions (FM-12):

| Candidate # | Name | Layer | Condition (Taken) — What Would Cause It to Fire | Condition (Skipped) — Why It Did Not Fire in This Scenario |
|---|---|---|---|---|
| [A-#] | [name] | [layer] | [what threshold / filter / event type would activate this] | [specific reason not met — e.g., "Automated flow trigger condition filters on field X = 'Y'; current value is 'Z'"] |

`[BRANCH BLIND: {name} — skipped condition absent]` if the Condition (Skipped) column
is empty for any non-firing row — FM-12 active for that row.

---

**SECTION 3 — DENOMINATOR CLOSURE GATE**

*Prevents FM-13. This section is separate from Section 2 — it is NOT the last row of Section 2.*

After completing Section 2, execute the arithmetic closure. Do not embed this in Section 2's
final entry or in a prose note — it occupies its own heading.

**Closure Arithmetic:**

| | Count |
|---|---|
| N declared in Section 1 | [N] |
| Firing entries (Section 2 numbered entries) | [F] |
| Non-firing entries (Section 2 non-firing table rows) | [NF] |
| Total resolved: F + NF | [F + NF] |
| Matches N? | YES / GAP |

**Formula verification**: `(F) + (NF) = [sum]`. Must equal `N = [N from Section 1]`.

If total ≠ N: `[UNRESOLVED CANDIDATE: {name}]` for each candidate present in Section 1
but absent from both the firing entries and the non-firing table — FM-01 active.

If this section is absent after Section 2: `[CLOSURE SKIP: arithmetic gate not executed — C-14 denominator N={N} was declared but not reconciled]` — FM-13 active.

---

**SECTION 4 — PATHOLOGY ASSESSMENT**

*Prevents FM-04, FM-06, FM-07, FM-11.*

Close all three Section 0 anomaly investigations. For each, cite Section 2 entry numbers
as evidence before stating the verdict (FM-07). Provide mitigation for every detected
anomaly (FM-11).

**STORM INVESTIGATION**
Evidence (cite Section 2 entry numbers — `[BARE ASSERTION: STORM verdict]` if absent):
- [specific observation — e.g., "Entry #2 and Entry #3 are both automated flows that fire on the same Dataverse row-modified event with no condition differentiation"]
Verdict: [STORM DETECTED / NOT DETECTED]
Mitigation (required if STORM DETECTED):
- [debounce strategy / condition filter addition / flow consolidation]
Register update: STATUS → CLOSED

**MISSING TRIGGER INVESTIGATION**
Evidence (cite Section 2 non-firing entries or Section 3 gaps):
- [specific observation]
Verdict: [MISSING TRIGGER DETECTED / NOT DETECTED]
Mitigation (required if MISSING TRIGGER DETECTED):
- [trigger registration fix / condition correction / flow creation]
Register update: STATUS → CLOSED

**CIRCULAR TRIGGER INVESTIGATION**
Evidence (trace any Section 2 Cascade chain that loops back):
- [chain trace, or "No Cascade chain in Section 2 closes back on a prior entry"]
Verdict: [CIRCULAR TRIGGER DETECTED / NOT DETECTED]
Mitigation (required if CIRCULAR TRIGGER DETECTED):
- [update-check flag / cycle-break condition / re-sequencing]
Register update: STATUS → CLOSED

Update Section 0 register with all evidence citations, verdicts, and mitigations.

---

**SECTION 5 — TRIGGER MAP**

*Prevents FM-09.*

Build the trigger map from Section 2 entries.

| # | Trigger Name | Tier | Fires? | Spawns (row ref) | Anomaly Flag |
|---|---|---|---|---|---|
| [Sec 2 entry #] | [name] | [Section 0 contract term] | YES/NO | Row #[ref] or none | none/storm/cycle/missing |

Column rules:
- Tier: Section 0 contract labels only — `[VOCAB FAIL: {term}]` for deviations (FM-08).
- Spawns: for any Section 2 entry where Cascade = YES, reference the spawned entry's row number. Referenced row absent: `[CASCADE GAP: {name}]` (FM-05).
- Include non-firing candidates from Section 2 non-firing table as NO rows.

`[MAP DEFICIENCY: missing {tier column / spawns column}]` if either column is absent — FM-09 active.

---

## V-02 — Axis: Output Format (Dual-Slot Entry Schema as Named Contract)

**Axis**: Output format — declare the entry schema as a named structural contract before enumeration
**Hypothesis**: R3 embedded Condition (Taken) and Condition (Skipped) inside entry prose. When the slots are named inside the entry body, a model may skip one while writing the other. Promoting the dual-slot requirement to a named ENTRY SCHEMA CONTRACT declared before enumeration begins makes the Condition (Skipped) slot as structurally mandatory as the Tier slot. Schema violations (empty Condition Skipped) are `[BRANCH BLIND]` at the schema level, not a prose instruction.

---

You are a Power Automate / Copilot Studio domain expert. Analyze which automations fire for
the given record change.

**SCENARIO**

{SCENARIO_DESCRIPTION}

---

**PART A — GOVERNANCE**

**A.1 — Platform Term Contract**

Declare once. All parts use only these labels.

Execution tiers:
- sync plugin step
- async plugin step
- instant flow
- automated flow
- scheduled flow

Connector terms for this scenario:
- [list relevant connectors — e.g., "Dataverse connector — When a row is added, modified, or deleted"]

Vocabulary violations: `[VOCAB FAIL: {term}]` inline at point of use.

**A.2 — Anomaly Investigation Register**

Open all three slots before Part B begins.

| Investigation | Status | Evidence | Verdict | Mitigation |
|---|---|---|---|---|
| STORM | OPEN | — | — | — |
| MISSING TRIGGER | OPEN | — | — | — |
| CIRCULAR TRIGGER | OPEN | — | — | — |

---

**PART B — CANDIDATE PRE-SCAN**

Scan every automation layer. List structural candidates — do not apply condition filters.

Layers: Dataverse sync plugin steps → async plugin steps → Power Automate automated flows → instant flows → scheduled flows → Copilot Studio topic triggers.

| # | Candidate Name | Layer | Why It Is a Candidate |
|---|---|---|---|
| 1 | [name] | [layer] | [reason] |
| ... | | | |

**CANDIDATE DENOMINATOR: N = [number].**

---

**PART C — ENTRY SCHEMA CONTRACT**

Every trigger entry produced in Part D — firing AND non-firing — SHALL conform to this
schema. This schema is a CONTRACT, not a template. An entry that omits any required field
is structurally deficient at that field.

**FIRING ENTRY SCHEMA:**

```
ENTRY #[N] — [Trigger Name]
├── Tier             : [A.1 contract term]
│                      [VOCAB FAIL: {term}] if not from contract
├── Condition (Taken): [the specific condition that caused this trigger to fire]
│                      [INSUFFICIENT: {name} missing Condition Taken] if empty
├── Condition (Skipped): [the condition under which this trigger would NOT fire]
│                        [BRANCH BLIND: {name} — skipped condition absent] if empty
├── Reads            : [record field(s) or payload consumed]
│                      [INSUFFICIENT: {name} missing Reads] if empty
├── Produces         : [primary output action]
│                      [INSUFFICIENT: {name} missing Produces] if empty
├── Side-effect writes: [downstream writes — field updates, record creation, notifications,
│                        API calls — or "none confirmed"]
├── Cascade          : [if Side-effect writes has automation potential:
│                        MUST be "ENTRY #[N+1] = {downstream trigger name}"
│                        else "none" or [CASCADE GAP: {name} — write to {field} not continued]]
└── Anomaly flag     : [none / STORM / CYCLE / MISSING]
```

**NON-FIRING ENTRY SCHEMA:**

Non-firing entries also require BOTH condition directions. A non-firing entry SHALL
document: (a) the condition that WOULD have caused it to fire (Condition Taken — the path
not taken), and (b) the specific reason it did not fire in this scenario (Condition
Skipped — the operative branch).

```
NON-FIRING — [Candidate Name]
├── Layer              : [from Part B candidate list]
├── Condition (Taken)  : [what would have caused this automation to fire]
│                        [INSUFFICIENT: {name} missing Condition Taken] if empty
├── Condition (Skipped): [the specific condition not met in this scenario]
│                        [BRANCH BLIND: {name} — skipped condition absent] if empty
└── Notes              : [any additional context — e.g., "registered but filtered out by scope condition"]
```

**Schema enforcement**: Before submitting Part D, verify every FIRING ENTRY and every
NON-FIRING entry against this schema. Empty slots carry their inline marker at the point
of omission.

---

**PART D — TRIGGER ENUMERATION**

Apply the Part C schema to all N candidates. Use sync-before-async ordering throughout.

[FIRING ENTRY entries using FIRING ENTRY SCHEMA]

[NON-FIRING entries using NON-FIRING ENTRY SCHEMA]

---

**PART E — DENOMINATOR CLOSURE**

Execute the arithmetic closure after Part D completes. This is a standalone section —
not a prose note appended to the last firing entry.

**Arithmetic Gate:**

```
Denominator declared (Part B):  N = [N]
Firing entries (Part D):         F = [count]
Non-firing entries (Part D):    NF = [count]
                                 ─────────
Total resolved:              F + NF = [sum]
Matches N?                         [YES / GAP]
```

If `F + NF < N`: `[UNRESOLVED CANDIDATE: {name}]` for each Part B candidate not found
in Part D firing entries or non-firing entries.

If `F + NF > N`: `[EXCESS ENTRY: {name}]` for each Part D entry not present in the Part B
candidate list — candidate was introduced in enumeration without a pre-scan basis.

---

**PART F — PATHOLOGY ASSESSMENT**

Close all three Part A.2 anomaly investigations. For each, evidence precedes verdict.

**STORM**
Evidence (cite Part D entry numbers):
- [observation]
Verdict: [STORM DETECTED / NOT DETECTED]
Mitigation (required if DETECTED): [specific fix]
Register update: STATUS → CLOSED

**MISSING TRIGGER**
Evidence (cite Part D non-firing entries or Part E gaps):
- [observation]
Verdict: [MISSING TRIGGER DETECTED / NOT DETECTED]
Mitigation (required if DETECTED): [specific fix]
Register update: STATUS → CLOSED

**CIRCULAR TRIGGER**
Evidence (trace any Part D Cascade chain that loops back):
- [observation]
Verdict: [CIRCULAR TRIGGER DETECTED / NOT DETECTED]
Mitigation (required if DETECTED): [specific fix]
Register update: STATUS → CLOSED

---

**PART G — TRIGGER MAP**

| # | Trigger Name | Tier | Fires? | Spawns (row ref) | Anomaly Flag |
|---|---|---|---|---|---|
| [Part D #] | [name] | [A.1 contract term] | YES/NO | Row #[ref] or none | none/storm/cycle/missing |

- Tier: A.1 contract terms only — `[VOCAB FAIL: {term}]` if not.
- Spawns: row reference for any Cascade = YES entry in Part D. Absent referenced row: `[CASCADE GAP: {name}]`.
- Include all non-firing candidates as NO rows.
- `[MAP DEFICIENCY: missing {tier column / spawns column}]` if either column absent.

---

## V-03 — Axis: Lifecycle Emphasis (C-17 Closure as a Mandatory Separate Phase)

**Axis**: Lifecycle emphasis — denominator closure as its own lifecycle phase, not an appendage
**Hypothesis**: R3 variations embedded the denominator closure check as the last row of the enumeration section or as a prose note under a trigger entry. This proximity to enumeration invites the closure check to be absorbed into the final entry's summary. Making the closure an explicit numbered Phase 4 with its own gate condition, its own input contracts (N from Phase 2, F and NF from Phase 3), and its own output table separates the arithmetic verification from the analysis — making it structurally impossible to silently omit.

---

You are a Power Automate / Copilot Studio domain expert. Execute the trigger simulation
using the phase protocol below. Each phase has required inputs and required outputs.
The next phase begins only when the current phase's outputs are complete.

**SCENARIO**

{SCENARIO_DESCRIPTION}

---

**PHASE 1 — GOVERNANCE AND PRE-SCAN**

**Required outputs:** (a) Platform Term Contract declared, (b) Anomaly Register open (3 slots),
(c) Candidate list with denominator N.

**1.1 — Platform Term Contract**

Execution tiers (use only these labels in all phases):
- sync plugin step
- async plugin step
- instant flow
- automated flow
- scheduled flow

Connector terms for this scenario:
- [list relevant connectors]

Vocabulary violations in any phase: `[VOCAB FAIL: {term}]` at point of use.

**1.2 — Anomaly Register**

Open all three investigations before Phase 2 begins.

| Investigation | Status | Evidence (Phase 3) | Verdict (Phase 3) | Mitigation (Phase 3) |
|---|---|---|---|---|
| STORM | OPEN | — | — | — |
| MISSING TRIGGER | OPEN | — | — | — |
| CIRCULAR TRIGGER | OPEN | — | — | — |

**1.3 — Candidate Pre-Scan**

Layers (scan all six before proceeding):
1. Dataverse synchronous plugin steps
2. Dataverse asynchronous plugin steps
3. Power Automate automated flows (Dataverse connector)
4. Power Automate instant flows
5. Power Automate scheduled flows
6. Copilot Studio topic triggers

| # | Candidate Name | Layer | Why It Is a Candidate |
|---|---|---|---|
| 1 | [name] | [layer] | [reason] |

**CANDIDATE DENOMINATOR: N = [number]. This value is the Phase 4 input.**

**Phase 1 complete.** Proceed to Phase 2.

---

**PHASE 2 — TRIGGER ENUMERATION**

**Required inputs:** Candidate list (N items), Phase 1 term contract, Phase 1 anomaly register.
**Required outputs:** All N candidates resolved as firing entries or non-firing entries. Every
entry has both condition directions populated.

**Enumeration rules:**
- Sync-before-async ordering throughout.
- Phase 1 contract terms only — `[VOCAB FAIL: {term}]` for deviations.
- If a Side-effect writes entry has downstream automation potential, the next numbered entry
  SHALL be the downstream trigger. Non-continuation: `[CASCADE GAP: {name}]`.
- **Both condition directions required per entry (C-16)**:
  - Firing entries: Condition (Taken) = the condition that caused this trigger to fire;
    Condition (Skipped) = the condition under which it would NOT fire.
  - Non-firing entries: Condition (Taken) = what would have caused this to fire;
    Condition (Skipped) = the specific condition not met in this scenario.
  - Missing Condition (Skipped) on ANY entry: `[BRANCH BLIND: {entry name} — skipped condition absent]`.

**FIRING ENTRY format:**

**ENTRY #[N] — [Trigger Name]**
- Tier: [Phase 1 contract term]
- Condition (Taken): [condition that caused this to fire — or `[INSUFFICIENT]`]
- Condition (Skipped): [condition under which this would NOT fire — or `[BRANCH BLIND: {name}]`]
- Reads: [input fields/payload — or `[INSUFFICIENT]`]
- Produces: [primary output — or `[INSUFFICIENT]`]
- Side-effect writes: [explicit list or "none confirmed"]
- Cascade: [ENTRY #[N+1] = {name} / none / `[CASCADE GAP: {name}]`]
- Anomaly flag: [none / STORM / CYCLE / MISSING]

**NON-FIRING ENTRY format:**

| Candidate # | Name | Layer | Condition (Taken) — Would Fire When | Condition (Skipped) — Did Not Fire Because |
|---|---|---|---|---|
| [#] | [name] | [layer] | [activation threshold] | [specific condition absent in this scenario — `[BRANCH BLIND: {name}]` if empty] |

**Phase 2 complete when:** All N candidates appear as either ENTRY rows or non-firing
table rows. Do NOT count or verify totals here — that is Phase 4's job.

Proceed to Phase 3.

---

**PHASE 3 — PATHOLOGY ASSESSMENT**

**Required inputs:** Phase 2 firing entries and non-firing entries.
**Required outputs:** All three Phase 1 anomaly investigations closed with evidence and verdicts.
Detected anomalies have mitigations.

For each investigation:

**[INVESTIGATION TYPE]**
Evidence (cite Phase 2 ENTRY numbers or non-firing row references):
- [specific observation — or `[BARE ASSERTION: {type} verdict — entry citations absent]` if
  no evidence is present before the verdict]
Verdict: [DETECTED / NOT DETECTED]
Mitigation (required if DETECTED):
- [actionable fix: debounce / registration / cycle-break / re-sequencing]
Phase 1 register update: STATUS → CLOSED

**Phase 3 complete when:** All three investigations show STATUS = CLOSED in Phase 1 register.

Proceed to Phase 4.

---

**PHASE 4 — DENOMINATOR CLOSURE**

**Required inputs:** N from Phase 1 (CANDIDATE DENOMINATOR), firing entry count F from
Phase 2, non-firing entry count NF from Phase 2.
**Required outputs:** Arithmetic gate result. Named gaps or excess entries if the formula
does not balance.

This phase is structurally independent from Phase 2 (enumeration) and Phase 3 (pathology).
Its inputs are counts derived from Phase 2, not Phase 2 content itself.

**Closure Table:**

| Input | Value | Source |
|---|---|---|
| Candidate denominator N | [N] | Phase 1 §1.3 |
| Firing entries F | [F] | Phase 2 firing entries count |
| Non-firing entries NF | [NF] | Phase 2 non-firing table row count |
| Total resolved: F + NF | [sum] | Phase 4 arithmetic |
| Expected: N | [N] | Phase 1 |
| Closure result | BALANCED / GAP / EXCESS | — |

**Arithmetic formula:** `F + NF = N` must hold.

If `F + NF < N`: `[UNRESOLVED CANDIDATE: {name}]` for each Phase 1 candidate not resolved
in Phase 2. GAP in Closure result.

If `F + NF > N`: `[EXCESS ENTRY: {name}]` for each Phase 2 entry not in Phase 1 candidate
list. EXCESS in Closure result.

If `F + NF = N`: Closure result = BALANCED.

**Phase 4 complete when:** Closure result is stated.

Proceed to Phase 5.

---

**PHASE 5 — TRIGGER MAP**

**Required inputs:** Phase 2 firing and non-firing entries.
**Required outputs:** Trigger map with execution-tier and Spawns columns populated.

| # | Trigger Name | Tier | Fires? | Spawns (row ref) | Anomaly Flag |
|---|---|---|---|---|---|
| [Phase 2 #] | [name] | [Phase 1 contract term] | YES/NO | Row #[ref] or none | none/storm/cycle/missing |

- Tier column: Phase 1 contract terms only — `[VOCAB FAIL: {term}]` for deviations.
- Spawns column: for any Phase 2 entry where Cascade = YES, reference the spawned entry's
  row number. Absent referenced row: `[CASCADE GAP: {name}]`.
- Include non-firing entries as NO rows.
- `[MAP DEFICIENCY: missing {tier column / spawns column}]` if either column absent.

---

## V-04 — Combined: Phrasing Register + Output Format

**Axes**: Phrasing register (FM-12, FM-13) × Output format (dual-slot entry schema as contract)
**Hypothesis**: FM-12 names the defect; the schema contract forces the slot structure. When both
mechanisms are present, the schema makes the Condition (Skipped) slot structurally required and
the FM-12 tag fires at the precise location of the omission. V-01 alone requires model
self-application of FM-12; V-02 alone creates the schema but lacks the named defect code.
Combined, they cross-validate: schema prevents omission, FM code makes any residual omission
diagnosable from the output cell.

---

You are a Power Automate / Copilot Studio domain expert conducting a governed trigger simulation.

**SCENARIO**

{SCENARIO_DESCRIPTION}

---

**FAILURE MODE CATALOG (FM-01 through FM-13)**

Output Cross-Reference Rule: when a failure mode is active, carry its FM code at the point
of violation in the output cell. Reviewers diagnose violations from the output cell alone.

| FM | Name | Inline Tag |
|---|---|---|
| FM-01 | Ad-Hoc Enumeration | `[UNRESOLVED CANDIDATE: {name}]` |
| FM-02 | Order Inversion | `[ORDER INVERSION: entry #{N} precedes sync entry #{M}]` |
| FM-03 | Empty Entry Slot | `[INSUFFICIENT: {name} missing {field}]` |
| FM-04 | Anomaly Silence | `[ANOMALY SILENCE: {class}]` |
| FM-05 | Dangling Side Effect | `[CASCADE GAP: {name} — write to {field} not continued]` |
| FM-06 | Post-Hoc Anomaly Assembly | `[POST-HOC: anomaly section appeared after enumeration]` |
| FM-07 | Bare Verdict | `[BARE ASSERTION: {verdict type}]` |
| FM-08 | Vocabulary Drift | `[VOCAB FAIL: {term}]` |
| FM-09 | Map Deficiency | `[MAP DEFICIENCY: missing {tier column / spawns column}]` |
| FM-10 | Missing Denominator | `[MISSING DENOMINATOR]` |
| FM-11 | Remediation Omission | (structural gap — MITIGATION field empty) |
| FM-12 | Branch Blindness | `[BRANCH BLIND: {entry name} — skipped condition absent \| FM-12]` |
| FM-13 | Closure Skip | `[CLOSURE SKIP: arithmetic gate not executed \| FM-13]` |

---

**SECTION 0 — GOVERNANCE**

*Prevents FM-06, FM-08, FM-10.*

**Platform Term Contract:**

Execution tiers:
- sync plugin step
- async plugin step
- instant flow
- automated flow
- scheduled flow

Connector terms for this scenario: [list relevant connectors]

**Anomaly Investigation Register** — open before Section 1:

| Investigation | Status | Evidence | Verdict | Mitigation |
|---|---|---|---|---|
| STORM | OPEN | — | — | — |
| MISSING TRIGGER | OPEN | — | — | — |
| CIRCULAR TRIGGER | OPEN | — | — | — |

---

**SECTION 1 — CANDIDATE PRE-SCAN**

*Prevents FM-01, FM-10.*

Layers: Dataverse sync plugin steps → async plugin steps → Power Automate automated flows →
instant flows → scheduled flows → Copilot Studio topic triggers.

| # | Candidate Name | Layer | Why It Is a Candidate |
|---|---|---|---|
| 1 | [name] | [layer] | [reason] |

**CANDIDATE DENOMINATOR: N = [number].**

---

**SECTION 2 — ENTRY SCHEMA CONTRACT**

*Prevents FM-12. This section declares the structural contract before any entry is written.*

Every entry produced in Section 3 — firing AND non-firing — SHALL conform to one of the
two schemas below. Both schemas require BOTH condition directions. FM-12 fires when
Condition (Skipped) is absent on any entry.

**FIRING ENTRY SCHEMA:**
```
ENTRY #[N] — [Trigger Name]
Tier             : [Section 0 contract term | VOCAB FAIL: {term} | FM-08]
Condition (Taken): [condition that caused this to fire | INSUFFICIENT: {name} | FM-03]
Condition (Skipped): [condition under which this would NOT fire
                      | BRANCH BLIND: {name} — skipped condition absent | FM-12]
Reads            : [input fields/payload | INSUFFICIENT: {name} missing Reads | FM-03]
Produces         : [primary output | INSUFFICIENT: {name} missing Produces | FM-03]
Side-effect writes: [explicit list or "none confirmed"]
Cascade          : [ENTRY #[N+1] = {name} / none / CASCADE GAP: {name} | FM-05]
Anomaly flag     : [none / STORM / CYCLE / MISSING]
```

**NON-FIRING ENTRY SCHEMA:**
```
NON-FIRING — [Candidate Name]
Layer              : [from Section 1]
Condition (Taken)  : [what would have caused this to fire
                      | INSUFFICIENT: {name} missing Condition Taken | FM-03]
Condition (Skipped): [the specific condition not met in this scenario
                      | BRANCH BLIND: {name} — skipped condition absent | FM-12]
Notes              : [optional context]
```

Both condition directions are required even on non-firing entries. The Condition (Taken)
on a non-firing entry is the counterfactual — it documents the path NOT taken in this
scenario.

---

**SECTION 3 — TRIGGER ENUMERATION**

*Apply Section 2 schema to all N candidates. Sync-before-async ordering.*

[FIRING ENTRY records per FIRING ENTRY SCHEMA — FM codes inline at any slot violation]

[NON-FIRING records per NON-FIRING ENTRY SCHEMA — FM codes inline at any slot violation]

---

**SECTION 4 — DENOMINATOR CLOSURE**

*Prevents FM-13. This section is structurally independent from Section 3.*
*Its only job is the arithmetic gate.*

| | Count |
|---|---|
| N declared (Section 1) | [N] |
| Firing entries F (Section 3) | [F] |
| Non-firing entries NF (Section 3) | [NF] |
| Total: F + NF | [sum] |
| Matches N? | YES / GAP |

Formula: `F + NF = N`.

- If gap: `[UNRESOLVED CANDIDATE: {name} | FM-01]` for each missing candidate.
- If excess: `[EXCESS ENTRY: {name}]` for each entry not in Section 1.
- If Section 4 is absent: `[CLOSURE SKIP: arithmetic gate not executed | FM-13]`.

---

**SECTION 5 — PATHOLOGY ASSESSMENT**

*Prevents FM-04, FM-06, FM-07, FM-11.*

Close all three Section 0 investigations.

**[STORM / MISSING TRIGGER / CIRCULAR TRIGGER]**
Evidence (cite Section 3 entry numbers — `[BARE ASSERTION: {type} | FM-07]` if absent):
- [observation]
Verdict: [DETECTED / NOT DETECTED]
Mitigation (required if DETECTED — FM-11 if absent): [specific fix]
Register update: STATUS → CLOSED

---

**SECTION 6 — TRIGGER MAP**

*Prevents FM-09.*

| # | Trigger Name | Tier | Fires? | Spawns (row ref) | Anomaly Flag |
|---|---|---|---|---|---|
| [Sec 3 #] | [name] | [Section 0 contract term] | YES/NO | Row #[ref] or none | none/storm/cycle/missing |

- `[VOCAB FAIL: {term} | FM-08]` for non-contract Tier labels.
- `[CASCADE GAP: {name} | FM-05]` for unresolved Spawns references.
- `[MAP DEFICIENCY: missing {col} | FM-09]` if Tier or Spawns column absent.

---

## V-05 — Combined: Phrasing Register + Output Format + Lifecycle Emphasis

**Axes**: Phrasing register (FM-13 catalog) × Output format (entry schema contract) × Lifecycle emphasis (post-enumeration closure phase)
**Hypothesis**: Full structural stack. The FM catalog names defects (V-01). The entry schema contract makes Condition (Skipped) mandatory at the point of authoring (V-02). The phase gate makes the arithmetic closure structurally impossible to absorb into enumeration (V-03). Each mechanism addresses a different failure vector for C-16 and C-17: vocabulary (FM-12/FM-13), structure (schema contract), and lifecycle (phase separation). Together they create overlapping coverage — a slot omission that the schema alone might pass due to a blank cell is caught by FM-12 tagging, which is in turn caught by the phase gate requiring a non-zero NF count.

---

You are a Power Automate / Copilot Studio domain expert running a governed trigger simulation.
You are operating under a three-layer compliance protocol:
(1) Failure Mode Catalog — names every class of defect;
(2) Entry Schema Contract — defines the required structure of every output entry;
(3) Phase Protocol — sequences analysis so that each step's output gates the next.

**SCENARIO**

{SCENARIO_DESCRIPTION}

---

### LAYER 1 — FAILURE MODE CATALOG (FM-01 through FM-13)

Every protocol rule in Layers 2 and 3 addresses a named failure mode. When a failure mode
is active, carry its FM code at the point of violation in the output cell.

| FM | Name | Inline Tag |
|---|---|---|
| FM-01 | Ad-Hoc Enumeration | `[UNRESOLVED CANDIDATE: {name}]` |
| FM-02 | Order Inversion | `[ORDER INVERSION: entry #{N} precedes sync entry #{M}]` |
| FM-03 | Empty Entry Slot | `[INSUFFICIENT: {name} missing {field}]` |
| FM-04 | Anomaly Silence | `[ANOMALY SILENCE: {class}]` |
| FM-05 | Dangling Side Effect | `[CASCADE GAP: {name} — write to {field} not continued]` |
| FM-06 | Post-Hoc Anomaly Assembly | `[POST-HOC]` |
| FM-07 | Bare Verdict | `[BARE ASSERTION: {verdict type}]` |
| FM-08 | Vocabulary Drift | `[VOCAB FAIL: {term}]` |
| FM-09 | Map Deficiency | `[MAP DEFICIENCY: missing {col}]` |
| FM-10 | Missing Denominator | `[MISSING DENOMINATOR]` |
| FM-11 | Remediation Omission | (structural gap — MITIGATION cell empty) |
| FM-12 | Branch Blindness | `[BRANCH BLIND: {name} — skipped condition absent \| FM-12]` |
| FM-13 | Closure Skip | `[CLOSURE SKIP: arithmetic gate not executed \| FM-13]` |

---

### LAYER 2 — ENTRY SCHEMA CONTRACT

Two schemas below define the only valid structure for trigger entries. Both require BOTH
condition directions. The Condition (Skipped) slot is a first-class required field,
not a secondary annotation. Omission activates FM-12 inline at that slot.

**SCHEMA A — FIRING ENTRY:**
```
ENTRY #[N] — [Trigger Name]
├── Tier              : [contract term | VOCAB FAIL: {term} | FM-08]
├── Condition (Taken) : [fires when: {specific condition} | INSUFFICIENT: missing | FM-03]
├── Condition (Skipped): [does not fire when: {condition} | BRANCH BLIND: {name} | FM-12]
├── Reads             : [input fields/payload | INSUFFICIENT: missing | FM-03]
├── Produces          : [primary output | INSUFFICIENT: missing | FM-03]
├── Side-effect writes: [downstream writes or "none confirmed"]
├── Cascade           : [ENTRY #[N+1] = {name} / none / CASCADE GAP: {name} | FM-05]
└── Anomaly flag      : [none / STORM / CYCLE / MISSING]
```

**SCHEMA B — NON-FIRING ENTRY:**
```
NON-FIRING — [Candidate Name]
├── Layer              : [from Phase 1 candidate list]
├── Condition (Taken)  : [would fire when: {threshold/filter} | INSUFFICIENT: missing | FM-03]
├── Condition (Skipped): [did not fire because: {specific unmet condition}
│                          | BRANCH BLIND: {name} — skipped condition absent | FM-12]
└── Notes              : [optional context]
```

The Condition (Taken) on a NON-FIRING entry is the counterfactual — the unfired path.
Both directions must be documented to satisfy C-16. A non-firing entry with only
"Condition (Skipped): field X ≠ Y" and no "Condition (Taken)" activates FM-12.

---

### LAYER 3 — PHASE PROTOCOL

Five phases. Each phase has required outputs. Phase N+1 begins only when Phase N outputs
are complete.

---

**PHASE 1 — GOVERNANCE**

Required outputs: (a) Term contract declared, (b) Anomaly register open with 3 OPEN slots,
(c) Candidate list with denominator N.

**Term Contract:**
Execution tiers: sync plugin step / async plugin step / instant flow / automated flow / scheduled flow.
Connector terms for this scenario: [list relevant connectors].
Violations in any phase: `[VOCAB FAIL: {term} | FM-08]`.

**Anomaly Register:**
| Investigation | Status | Evidence | Verdict | Mitigation |
|---|---|---|---|---|
| STORM | OPEN | — | — | — |
| MISSING TRIGGER | OPEN | — | — | — |
| CIRCULAR TRIGGER | OPEN | — | — | — |

**Candidate Pre-Scan:**

Layers: Dataverse sync plugin steps → async plugin steps → Power Automate automated flows
→ instant flows → scheduled flows → Copilot Studio topic triggers.

| # | Candidate Name | Layer | Why It Is a Candidate |
|---|---|---|---|
| 1 | [name] | [layer] | [reason] |

**CANDIDATE DENOMINATOR: N = [number].** This is the Phase 3 input.

Phase 1 outputs complete → proceed to Phase 2.

---

**PHASE 2 — TRIGGER ENUMERATION**

Required outputs: All N candidates resolved as SCHEMA A or SCHEMA B entries. Every Condition
(Skipped) slot populated. FM-12 inline at any empty Condition (Skipped) slot.

Enumeration rules:
- Sync-before-async ordering — FM-02 if violated.
- Phase 1 term contract throughout — FM-08 if violated.
- Cascade obligation: side-effect writes with automation potential spawn the next numbered entry — FM-05 if not continued.
- Both condition directions on every entry (Layer 2 schemas) — FM-12 if Condition (Skipped) absent on any entry.

[FIRING ENTRY records per SCHEMA A]

[NON-FIRING records per SCHEMA B]

Phase 2 outputs: F firing entries, NF non-firing entries. Do not verify totals here.

Phase 2 outputs complete → proceed to Phase 3.

---

**PHASE 3 — DENOMINATOR CLOSURE**

Required inputs: N (Phase 1), F (Phase 2 firing count), NF (Phase 2 non-firing count).
Required output: Arithmetic closure table with BALANCED / GAP / EXCESS verdict.

This phase is physically separated from Phase 2. Its output is a table of counts, not a
review of trigger content.

**Closure Table:**

| Quantity | Value | Source |
|---|---|---|
| Denominator N | [N] | Phase 1 candidate pre-scan |
| Firing entries F | [F] | Phase 2 firing entry count |
| Non-firing entries NF | [NF] | Phase 2 non-firing entry count |
| Total resolved: F + NF | [sum] | Phase 3 arithmetic |
| Expected: N | [N] | Phase 1 |
| **Closure verdict** | **BALANCED / GAP / EXCESS** | — |

Formula: `F + NF = N`.
- GAP: `[UNRESOLVED CANDIDATE: {name} | FM-01]` per missing candidate.
- EXCESS: `[EXCESS ENTRY: {name}]` per Phase 2 entry not in Phase 1.
- Absent Phase 3 entirely: `[CLOSURE SKIP: arithmetic gate not executed | FM-13]`.

Phase 3 complete → proceed to Phase 4.

---

**PHASE 4 — PATHOLOGY ASSESSMENT**

Required outputs: All three Phase 1 anomaly investigations closed. Evidence precedes every
verdict. Detected anomalies have mitigations.

**STORM**
Evidence (cite Phase 2 ENTRY numbers — `[BARE ASSERTION: STORM | FM-07]` if absent):
- [observation]
Verdict: [DETECTED / NOT DETECTED]
Mitigation (required if DETECTED — FM-11 if absent): [specific fix]
Phase 1 register: STORM → CLOSED

**MISSING TRIGGER**
Evidence (cite Phase 2 non-firing entries or Phase 3 gaps):
- [observation]
Verdict: [DETECTED / NOT DETECTED]
Mitigation (required if DETECTED — FM-11 if absent): [specific fix]
Phase 1 register: MISSING TRIGGER → CLOSED

**CIRCULAR TRIGGER**
Evidence (trace any Phase 2 Cascade chain that loops back):
- [observation]
Verdict: [DETECTED / NOT DETECTED]
Mitigation (required if DETECTED — FM-11 if absent): [specific fix]
Phase 1 register: CIRCULAR TRIGGER → CLOSED

Phase 4 complete → proceed to Phase 5.

---

**PHASE 5 — TRIGGER MAP**

Required output: Trigger map with Tier column (Phase 1 contract terms) and Spawns column
(Phase 2 row references). All N candidates appear.

| # | Trigger Name | Tier | Fires? | Spawns (row ref) | Anomaly Flag |
|---|---|---|---|---|---|
| [Phase 2 #] | [name] | [contract term] | YES/NO | Row #[ref] or none | none/storm/cycle/missing |

- Non-Phase-1-contract Tier label: `[VOCAB FAIL: {term} | FM-08]`.
- Unresolved Spawns reference: `[CASCADE GAP: {name} | FM-05]`.
- Missing Tier column: `[MAP DEFICIENCY: missing tier column | FM-09]`.
- Missing Spawns column: `[MAP DEFICIENCY: missing spawns column | FM-09]`.
- Phase 5 absent: `[MAP DEFICIENCY: trigger map entirely absent | FM-09]`.
