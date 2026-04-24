# topic-plan Skill Variations — Round 8 (2026-03-15)

Rubric: v8 (C-01–C-30, max 100)
New criteria this round: C-28 (WS blocks as first-class section headers), C-29 (write-surface
register before Phase 0), C-30 (register-milestone linkage per WS block)

---

## Round 8 Design Notes

Round 7 surfaced three discriminating signals relevant to the write-surface enforcement stack:

1. **C-27 reachable but not structurally auditable** — Prior variations achieved all three
   write-surface enforcement blocks (Gate 0, Schema boundary, null template) but embedded
   them as bullets inside phase descriptions or inline within schema definitions. A reviewer
   could only confirm completeness by reading full phase content. C-28 closes this: each WS
   block must be a first-class section header, independently navigable by scanning titles alone.

2. **Write-surface coverage was emergent, not declared** — The three enforcement blocks were
   discovered by reading the skill. No upfront contract stated what all three sites were
   before any phase ran. C-29 closes this: a register table commits to all three sites before
   Phase 0, making completeness auditable at the document level (three rows declared, three
   milestones must appear).

3. **Register and delivery sites were parallel but unlinked** — Even with C-29's register and
   C-28's headers, nothing proved the blocks delivered what the register promised. C-30 closes
   this: each WS block must cite its register row number, creating a closed audit chain.

**Round 8 strategy**: All five variations satisfy C-28 (WS-1/WS-2/WS-3 as `##` section
headers), C-29 (register table before Phase 0), and C-30 (each block cites its register row).
The primary discriminating axis is structural organization: how the register, the defense
layer, the phase chain, and the WS blocks are sequenced and framed.

---

## V-01: Output Format — Register as Document Spine

**Variation axis**: Output format — the WRITE SURFACE REGISTER is the document's structural
spine; every subsequent major block is either a WS milestone, a phase, or a gate. Navigating
the document by section headers alone reveals the full write-surface architecture without
reading any content.

**Hypothesis**: When the register is the first section and the three WS blocks are the most
prominent recurring headers (appearing at the three critical execution moments), a reviewer
can audit write-surface completeness by scanning section titles without reading phase content.
This makes C-28, C-29, and C-30 all auditable in under 30 seconds.

---

```
You are executing the topic:plan skill — Signal strategy revision.

---

## WRITE SURFACE REGISTER

> Positioned before all phases. Declares the three write surfaces that will receive
> enforcement blocks below. Audit completeness by counting WS milestone headers —
> three rows declared, three milestone sections must appear.

| Row | Identifier | Surface Type           | Trigger Condition                                      |
|-----|------------|------------------------|--------------------------------------------------------|
| 1   | WS-1       | Pre-read barrier       | Before any artifact is opened (Phase 0 entry)         |
| 2   | WS-2       | Schema boundary check  | Before filling any proposal column (Phase 3 entry)    |
| 3   | WS-3       | Null declaration template | Inside each typed null declaration (Phase 3 body)  |

Audit rule: three rows. Three `## WS-N` headers must appear below. Verify by scanning
section titles — no prose-reading required.

---

## VOCABULARY CONTRACT

Two sentinel tokens are in force throughout all cells, columns, and free-text fields:

| Token | Meaning                            | Violation condition                                   |
|-------|------------------------------------|-------------------------------------------------------|
| `??`  | Open obligation — unknown/unfilled | Leaving a cell blank when `??` is correct is a violation |
| `--`  | Closed decision — deliberately absent | Writing `??` when a deliberate decision has been made is a violation |

**Banned forms** — disqualified in any justification, inertia, reason, or null-declaration cell:

> `"no change needed"` · `"nothing to add"` · `"clearly warranted"` · `"seems sufficient"` ·
> `"a few artifacts"` · `"several artifacts"` · `"some signals"` · any non-integer count

Writing any banned form is a gate failure at point of production. Check every free-text cell
against this list before writing it. This check applies to null declaration reason cells
equally — null declarations do not receive a scope exemption.

Violation enumeration:
- Blank cell where `??` is required: vocabulary violation
- `??` where `--` is the correct token: vocabulary violation
- Any banned form in any cell: vocabulary violation
- Non-integer count in the delta summary sentence: integer-enforcement gate failure

---

## WS-1 — Pre-Read Barrier

> **WS-1 MILESTONE — fulfills Register Row 1**

**GATE 0 — PRE-SIGNAL STOP. Do not read any artifact until this gate passes.**

Before opening strategy.md or any signal artifact:

1. State today's date.
2. Open strategy.md header only. Extract: strategy version, date written, and listed
   namespace priorities as last recorded. Close without reading body content.
3. Fill the Defense Register table below from strategy.md header data.

**Defense Register** — commit before reading any signal:

| Row | Change Dimension             | Current Strategy Position | Defense Argument | Signal Threshold to Defeat |
|-----|------------------------------|--------------------------|-----------------|---------------------------|
| 1   | ADD new namespace coverage   | ??                        | ??               | ??                         |
| 2   | REMOVE existing priority     | ??                        | ??               | ??                         |
| 3   | REPRIORITIZE ordering        | ??                        | ??               | ??                         |
| 4   | Coverage gap within namespace| ??                        | ??               | ??                         |
| 5   | Signal staleness / artifact age | ??                     | ??               | ??                         |

Fill every `??` from strategy.md before reading any signal artifacts. A blank Defense
Register cell is a Gate 0 failure. No banned forms permitted in any cell.

**GATE 0 PASS CONDITION**: All five Defense Register rows filled with non-`??` values,
no banned forms present. Do not advance to Phase 1 without meeting this condition.
Do not advance to Phase 1 without passing Gate 0.

---

## PHASE 1 — Signal Inventory

Read all signal artifacts across all 9 namespaces. For each namespace, fill one row:

| Namespace | Artifact Filename | Date | Status         |
|-----------|------------------|------|----------------|
| scout     | ??               | ??   | ??             |
| draft     | ??               | ??   | ??             |
| review    | ??               | ??   | ??             |
| flow      | ??               | ??   | ??             |
| trace     | ??               | ??   | ??             |
| prove     | ??               | ??   | ??             |
| listen    | ??               | ??   | ??             |
| program   | ??               | ??   | ??             |
| topic     | ??               | ??   | ??             |

If no artifact exists for a namespace: write `--` in the filename column, `--` in the
date column, and `ABSENT` in the status column. A blank cell is a vocabulary violation.

**GATE 1 — Do not advance to Phase 2** until all 9 rows are filled with non-blank values.
No banned forms present in any cell.

---

## PHASE 2 — Delta Classification

Compare each artifact date against the strategy.md written date:

| Namespace | Artifact Date | Strategy Written Date | NEW / PRIOR |
|-----------|--------------|----------------------|-------------|
| scout     | ??           | ??                   | ??          |
| draft     | ??           | ??                   | ??          |
| review    | ??           | ??                   | ??          |
| flow      | ??           | ??                   | ??          |
| trace     | ??           | ??                   | ??          |
| prove     | ??           | ??                   | ??          |
| listen    | ??           | ??                   | ??          |
| program   | ??           | ??                   | ??          |
| topic     | ??           | ??                   | ??          |

**Mandatory delta sentence** (integer values required):
> "Strategy was written on [DATE]. [N] artifacts are NEW. [M] artifacts are PRIOR."

Integer-enforcement rule: writing "a few", "several", "some", or any non-integer value
in the above sentence is a gate failure.

**GATE 2 — Do not advance to Phase 3** until: (1) all rows classified, (2) mandatory
delta sentence present with exact integer values, (3) no banned forms in any cell.

---

## WS-2 — Schema Boundary Check

> **WS-2 MILESTONE — fulfills Register Row 2**

**PRE-FILL BARRIER. Do not write any proposal row until this check completes.**

Before filling any cell in the Proposal Table (Phase 3):

1. Confirm the delta sentence contains integers.
2. Confirm only NEW-classified artifacts will be cited as evidence.
3. Confirm the following mandatory columns are labeled in the table header:
   - `Change Type` (ADD / REMOVE / REPRIORITIZE)
   - `Evidence Artifact` (filename required; `??` if unknown)
   - `Before` (current strategy state)
   - `After` (proposed state)
   - `Inertia Defeated` **[MANDATORY]** (why NO CHANGE is insufficient)
   - `Defense Defeated` (row number from Defense Register)
4. **Check each cell you are about to write against the BANNED FORMS list** before writing.
   Any match disqualifies the row.

**GATE 3 — Do not fill proposal rows** until all mandatory column headers are present and
banned-forms check is complete. Do not advance to Phase 3 without passing Gate 3.

---

## PHASE 3 — Proposals

Fill one row per proposal. Only NEW artifacts may generate proposals.

| # | Change Type | Evidence Artifact | Before | After | Inertia Defeated [MANDATORY] | Defense Defeated |
|---|-------------|------------------|--------|-------|------------------------------|-----------------|
| 1 | ??          | ??               | ??     | ??    | ??                           | ??              |

**Inertia Defeated [MANDATORY]**: State the specific reason NO CHANGE is insufficient.
Check this cell against the BANNED FORMS list before writing. `"no change needed"` and
`"clearly warranted"` are not acceptable entries and disqualify the row.

**Defense Defeated**: Cite the row number from the Defense Register that this proposal
defeated (e.g., "Defense defeated: Row 3"). A named defense without a row number does
not satisfy this column.

If no ADD proposals exist, write:
> ADD — NULL: No new coverage warranted because [specific reason — check against banned
> forms before writing this cell].

If no REMOVE proposals exist, write:
> REMOVE — NULL: No removals warranted because [specific reason — check against banned
> forms before writing this cell].

If no REPRIORITIZE proposals exist, write:
> REPRIORITIZE — NULL: No re-prioritization warranted because [specific reason — check
> against banned forms before writing this cell].

**GATE 4 — Do not advance to Phase 4** until: (1) all proposal rows complete with no blank
cells, (2) inertia column has no banned forms, (3) defense column has row numbers, (4) all
three change types have either a proposal row or a labeled null declaration.

---

## WS-3 — Null Declaration Template

> **WS-3 MILESTONE — fulfills Register Row 3**

**NULL DECLARATION BARRIER. Governs every null declaration produced in Phase 3 and Phase 4.**

All null declarations must:

1. Use the typed form: `[CHANGE TYPE] — NULL` (never a single "nothing to change" statement).
2. Include a specific reason checked against the BANNED FORMS list.
3. Not use: `"no change needed"` · `"nothing to add"` · `"clearly warranted"` · `"seems sufficient"`.

**Banned forms apply to null declarations equally — null declarations are not exempt from
the vocabulary contract.** A null declaration that uses a hedge phrase is a scope violation.

---

## PHASE 4 — Conflict Detection

Audit NEW artifacts for cross-artifact contradictions on the same namespace priority:

| Artifact A | Artifact B | Dimension | Contradiction Type | Resolution |
|------------|------------|-----------|-------------------|-----------|
| ??         | ??         | ??        | ??                | ??        |

If no conflicts exist:
> CONFLICT DETECTION — NULL: No cross-artifact contradictions detected because [specific
> reason — check against banned forms before writing].

**GATE 5 — Do not advance to Phase 5** without completing conflict detection. A blank
table with no null declaration is a gate failure.

---

## PHASE 5 — Confirmation Gate

Present all proposals (including null declarations) to the user.

> **STOP. Do not modify strategy.md until the user responds.**
>
> Below are the proposed changes to strategy.md based on NEW signal artifacts.
> Respond with:
> - **YES** — proceed with all proposals as stated
> - **NO** — discard all proposals
> - **REVISED** — modify specific rows before applying
>
> [Present complete proposals table and all null declarations here]
>
> Awaiting confirmation before any file modification.

**GATE 6 — Do not modify strategy.md** until the user responds YES, NO, or REVISED.
```

---

## V-02: Lifecycle Emphasis — Phase State Machine with Entry/Exit Conditions

**Variation axis**: Lifecycle emphasis — every phase is a self-contained state machine
unit with explicit ENTRY CONDITION, JOB, and EXIT CONDITION. WS blocks appear as
lifecycle transitions between phases, marking the boundary between safe and unsafe
write surfaces. Phases cannot be entered silently.

**Hypothesis**: When each phase declares its own entry precondition (what must be true
before the phase starts), the WS blocks become natural checkpoints at phase transitions
rather than standalone enforcement injections. This makes the sequential gate chain
(C-20) and write-surface enforcement (C-27-C-30) a single unified architecture.

---

```
You are executing the topic:plan skill — Signal strategy revision.

---

## SKILL ARCHITECTURE

This skill executes as a strict phase sequence. Each phase has:
- ENTRY CONDITION: what must be true before this phase starts
- JOB: what this phase produces
- EXIT CONDITION: what must be true before advancing to the next phase

Three write surfaces require enforcement blocks. They are declared here and delivered
as named sections below.

---

## WRITE SURFACE REGISTER

> Declared before any phase executes. Three enforcement blocks will appear as named
> sections below. Audit completeness by scanning section headers.

| Row | Identifier | Surface Type           | Trigger Condition                                      |
|-----|------------|------------------------|--------------------------------------------------------|
| 1   | WS-1       | Pre-read barrier       | Phase 0 entry — before opening strategy.md            |
| 2   | WS-2       | Schema boundary        | Phase 3 entry — before filling any proposal column    |
| 3   | WS-3       | Null declaration gate  | Phase 3 body — inside each null declaration           |

---

## VOCABULARY CONTRACT

Two tokens govern all cells throughout execution:

| Token | Meaning                              | Violation condition                                  |
|-------|--------------------------------------|------------------------------------------------------|
| `??`  | Open obligation — unknown/unfilled   | Blank cell where `??` is required                   |
| `--`  | Closed decision — deliberately absent | `??` where a deliberate absent decision is correct  |

Banned forms (disqualified everywhere, including null declarations):
> `"no change needed"` · `"nothing to add"` · `"clearly warranted"` · `"seems sufficient"` ·
> `"a few artifacts"` · `"several artifacts"` · `"some signals"` · any non-integer count

Violation = gate failure at point of production. Check before writing. Null declarations
are not exempt.

---

## WS-1 — Pre-Read Barrier

> **WS-1 MILESTONE — fulfills Register Row 1**

ENTRY CONDITION: No artifacts have been read. Execution has not yet entered any phase.
JOB: Build the Defense Register and extract the strategy date.
EXIT CONDITION: All Defense Register rows filled, no `??` remaining, no banned forms.

**GATE 0 — PRE-SIGNAL STOP.**
Do not open strategy.md body or any signal artifact until Gate 0 passes.

**Phase 0 — Defense Register Construction**

Open strategy.md header only (date and structure metadata). Do not read body content.

Extract and record:
- STRATEGY DATE: [YYYY-MM-DD]
- Listed namespace priorities as recorded in strategy.md header

Fill the Defense Register from strategy.md header data:

| Row | Change Dimension             | Current Strategy Position | Defense Argument | Signal Threshold to Defeat |
|-----|------------------------------|--------------------------|-----------------|---------------------------|
| 1   | ADD new namespace coverage   | ??                        | ??               | ??                         |
| 2   | REMOVE existing priority     | ??                        | ??               | ??                         |
| 3   | REPRIORITIZE ordering        | ??                        | ??               | ??                         |
| 4   | Coverage gap within namespace| ??                        | ??               | ??                         |
| 5   | Signal staleness             | ??                        | ??               | ??                         |

GATE 0 PASS CONDITION: All cells filled with non-`??` values, no banned forms.
Do not advance to Phase 1 without passing Gate 0.

---

## PHASE 1 — Signal Inventory

ENTRY CONDITION: Gate 0 passed. Defense Register complete. No signal artifacts read yet.
JOB: Inventory all 9 namespaces. Classify each artifact as NEW or PRIOR.
EXIT CONDITION: All 9 namespace rows filled. Mandatory delta sentence written with integers.

Assess all 9 namespaces:

| Namespace | Artifact Filename | Artifact Date | Strategy Date | NEW / PRIOR |
|-----------|------------------|---------------|---------------|-------------|
| scout     | ??               | ??            | ??            | ??          |
| draft     | ??               | ??            | ??            | ??          |
| review    | ??               | ??            | ??            | ??          |
| flow      | ??               | ??            | ??            | ??          |
| trace     | ??               | ??            | ??            | ??          |
| prove     | ??               | ??            | ??            | ??          |
| listen    | ??               | ??            | ??            | ??          |
| program   | ??               | ??            | ??            | ??          |
| topic     | ??               | ??            | ??            | ??          |

No artifact for a namespace: `--` filename, `--` date, classify as `ABSENT`.

**Mandatory delta sentence** (integers only; non-integer is gate failure):
> "Strategy was written on [DATE]. [N] artifacts are NEW. [M] artifacts are PRIOR."

GATE 1 PASS CONDITION: All 9 rows filled, delta sentence present with integer values.
Do not advance to Phase 2 without passing Gate 1.

---

## PHASE 2 — Artifact Reading

ENTRY CONDITION: Gate 1 passed. All 9 namespaces inventoried.
JOB: Read full content of every NEW-classified artifact.
EXIT CONDITION: All NEW artifacts read. Reading confirmed.

Read every artifact classified NEW in Phase 1. Do not skip any.

Write: READING COMPLETE — [N] NEW artifacts read in full.

GATE 2 PASS CONDITION: READING COMPLETE statement present with integer count.
Do not advance to Phase 3 without passing Gate 2.

---

## WS-2 — Schema Boundary Check

> **WS-2 MILESTONE — fulfills Register Row 2**

ENTRY CONDITION: Gates 0, 1, 2 all passed.
JOB: Validate the proposal table schema before any row is filled.
EXIT CONDITION: All mandatory columns confirmed. Banned-forms check complete.

**PRE-FILL BARRIER. Do not write any proposal row until this check completes.**

Required columns (must appear as labeled headers):
- `Change Type` (ADD / REMOVE / REPRIORITIZE)
- `Evidence Artifact` (filename required; `??` if unknown)
- `Before` / `After`
- `Inertia Defeated` **[MANDATORY]** — why NO CHANGE is insufficient; banned forms disqualify
- `Defense Defeated` — row number from Defense Register

Pre-fill check:
1. Delta sentence confirmed with integer values ✓/✗
2. Only NEW artifacts will be cited as evidence ✓/✗
3. All mandatory columns present in table header ✓/✗
4. Banned-forms check primed for every cell ✓/✗

GATE 3 PASS CONDITION: All four checks ✓. Do not fill proposal rows without passing Gate 3.

---

## PHASE 3 — Proposals

ENTRY CONDITION: Gate 3 passed. Schema validated. Banned-forms check active.
JOB: Produce typed proposals. Produce typed null declarations for absent change types.
EXIT CONDITION: All rows complete. All three change types addressed. All cells filled.

| # | Change Type | Evidence Artifact | Before | After | Inertia Defeated [MANDATORY] | Defense Defeated |
|---|-------------|------------------|--------|-------|------------------------------|-----------------|

For `Inertia Defeated [MANDATORY]`: state why NO CHANGE is insufficient. Check against
banned forms before writing. `"no change needed"` disqualifies the row.

For `Defense Defeated`: cite row number (e.g., "Row 3"). A name without a row number
does not satisfy this column.

Absent change types — one null declaration each, typed form required:
> [TYPE] — NULL: [specific reason — banned-forms check applies here too]

GATE 4 PASS CONDITION: All proposal rows complete. All three change types addressed
(proposal or typed null). No blank cells. No banned forms in inertia or null cells.
Do not advance to Phase 4 without passing Gate 4.

---

## WS-3 — Null Declaration Template

> **WS-3 MILESTONE — fulfills Register Row 3**

ENTRY CONDITION: Operating inside Phase 3 body when a change type has no proposals.
JOB: Structure null declarations to prevent hedge phrases from entering typed null cells.
EXIT CONDITION: Each null declaration uses typed form and passes banned-forms check.

Null declaration template:
```
[CHANGE TYPE] — NULL: [reason — check against banned forms list before writing]
```

Requirements:
1. Typed form required: `ADD — NULL`, `REMOVE — NULL`, `REPRIORITIZE — NULL`
2. Reason cell checked against banned forms before writing
3. `"no change needed"` · `"nothing to add"` · `"clearly warranted"` are scope violations
4. A single "no changes to make" statement covering all types is a structural violation —
   each absent type requires its own labeled null declaration

---

## PHASE 4 — Conflict Detection

ENTRY CONDITION: Gate 4 passed. All proposals complete.
JOB: Audit NEW artifacts for cross-artifact contradictions on the same namespace priority.
EXIT CONDITION: Contradiction table filled or conflict null declaration written.

| Artifact A | Artifact B | Dimension | Contradiction Type | Resolution |
|------------|------------|-----------|-------------------|-----------|

If no conflicts:
> CONFLICT DETECTION — NULL: [reason — banned forms apply]

GATE 5 PASS CONDITION: Table filled or null declaration present. Do not advance to Phase 5
without passing Gate 5.

---

## PHASE 5 — Confirmation Gate

ENTRY CONDITION: Gate 5 passed. All proposals and null declarations finalized.
JOB: Present proposals to user. Halt. Await YES / NO / REVISED.
EXIT CONDITION: User responds YES, NO, or REVISED.

> **STOP. Do not modify strategy.md until the user responds.**
>
> Proposed changes below. Respond with YES / NO / REVISED.
>
> [Present proposals table and all null declarations]

GATE 6 PASS CONDITION: User responds YES, NO, or REVISED.
Do not modify strategy.md until Gate 6 passes.
```

---

## V-03: Inertia Framing — Null Hypothesis as Presumptive Winner

**Variation axis**: Inertia framing — the skill opens with a null hypothesis declaration:
"The strategy is correct until evidence defeats it." The defense register is foregrounded
as the presumptive winner. Every proposal is an explicit override of the null hypothesis
for a specific change dimension. The WS blocks enforce this framing structurally.

**Hypothesis**: When the entire skill is framed around "defeat the null hypothesis" rather
than "find changes to make," proposals become evidence-grounded rather than opportunity-seeking.
The defense register is not a formality — it is the standard every proposal must beat.
This framing makes the inertia column (C-08) and defense citation (C-22) feel mandatory
rather than supplementary.

---

```
You are executing the topic:plan skill — Signal strategy revision.

---

## NULL HYPOTHESIS DECLARATION

The strategy is currently correct. This is the default outcome of this skill.

Every proposal in this skill makes one claim: "The null hypothesis is wrong about
[change dimension]." That claim requires evidence from a NEW signal artifact that
post-dates the strategy. Without such evidence, the null hypothesis stands.

At the end of this skill, the expected output is: strategy.md unchanged.

---

## WRITE SURFACE REGISTER

> The null hypothesis is enforced at three write surfaces. Each is declared here
> before any phase executes. Each has a milestone block below.

| Row | Identifier | Surface Type           | Trigger Condition                                     | Null Hypothesis Relevance              |
|-----|------------|------------------------|-------------------------------------------------------|----------------------------------------|
| 1   | WS-1       | Pre-read barrier       | Before any artifact is read (Phase 0 entry)           | Defense register must be built before evidence is gathered |
| 2   | WS-2       | Schema boundary        | Before filling proposal columns (Phase 3 entry)       | Each proposal must cite why NO CHANGE fails |
| 3   | WS-3       | Null declaration gate  | Inside each null declaration (Phase 3 body)           | Null declarations must state why the null hypothesis holds |

---

## VOCABULARY CONTRACT

Two tokens are in force:

| Token | Meaning                             | Violation                                            |
|-------|-------------------------------------|------------------------------------------------------|
| `??`  | Open obligation — not yet filled    | Blank cell where `??` is correct                    |
| `--`  | Closed decision — deliberately null | `??` where a deliberate absent decision is correct  |

Banned forms — disqualify any cell, including null declaration reason cells:
> `"no change needed"` · `"nothing to add"` · `"clearly warranted"` · `"seems sufficient"` ·
> `"a few artifacts"` · `"several artifacts"` · `"some signals"` · any non-integer count

The null hypothesis does not grant null declarations a scope exemption. A null declaration
that uses a hedge phrase is a vocabulary violation.

---

## WS-1 — Pre-Read Barrier (Null Hypothesis Anchoring)

> **WS-1 MILESTONE — fulfills Register Row 1**

The null hypothesis cannot be built post-hoc. Before reading any signal, commit to
what the current strategy says and why it should be believed.

**GATE 0 — NULL HYPOTHESIS MUST BE COMMITTED BEFORE EVIDENCE IS GATHERED.**
Do not open strategy.md body or any signal artifact until Gate 0 passes.

**Phase 0: Build the Null Hypothesis Defense Register**

Open strategy.md header only. Extract: strategy version, strategy date, and listed
namespace priorities. Record:

STRATEGY DATE: [YYYY-MM-DD]

Then fill the Defense Register — the null hypothesis per change dimension:

| Row | Change Dimension             | Null Hypothesis (Current Strategy Says) | Defense Strength (HIGH/MED/LOW) | Signal That Would Defeat It |
|-----|------------------------------|-----------------------------------------|--------------------------------|----------------------------|
| 1   | ADD new namespace coverage   | ??                                      | ??                              | ??                         |
| 2   | REMOVE existing priority     | ??                                      | ??                              | ??                         |
| 3   | REPRIORITIZE ordering        | ??                                      | ??                              | ??                         |
| 4   | Coverage gap in namespace    | ??                                      | ??                              | ??                         |
| 5   | Signal staleness             | ??                                      | ??                              | ??                         |

A `??` remaining in any cell means the null hypothesis has not been fully committed.
No banned forms permitted. Check each cell before writing.

GATE 0 PASS CONDITION: All Defense Register cells filled. No banned forms. No `??` remaining.
Do not advance to Phase 1 without passing Gate 0.

---

## PHASE 1 — Signal Inventory

Locate all signal artifacts. For each of the 9 namespaces, record what exists:

| Namespace | Artifact Filename | Date | vs. Strategy Date | Classification |
|-----------|------------------|------|-------------------|----------------|
| scout     | ??               | ??   | ??                | ??             |
| draft     | ??               | ??   | ??                | ??             |
| review    | ??               | ??   | ??                | ??             |
| flow      | ??               | ??   | ??                | ??             |
| trace     | ??               | ??   | ??                | ??             |
| prove     | ??               | ??   | ??                | ??             |
| listen    | ??               | ??   | ??                | ??             |
| program   | ??               | ??   | ??                | ??             |
| topic     | ??               | ??   | ??                | ??             |

No artifact: `--` filename, `--` date, `ABSENT` classification.

**Mandatory delta sentence** (integers only — non-integer is gate failure):
> "Strategy was written on [DATE]. [N] artifacts are NEW. [M] artifacts are PRIOR."

GATE 1 PASS CONDITION: All 9 rows filled. Delta sentence present with integer values.

---

## PHASE 2 — Evidence Gathering

Read the full content of every NEW-classified artifact. These are the only artifacts
eligible to defeat the null hypothesis.

Write: EVIDENCE GATHERED — [N] NEW artifacts read.

GATE 2 PASS CONDITION: EVIDENCE GATHERED statement present with integer count.

---

## WS-2 — Schema Boundary Check (Null Hypothesis Override Gate)

> **WS-2 MILESTONE — fulfills Register Row 2**

A proposal claims the null hypothesis is wrong. Before writing that claim, verify the
claim apparatus is structurally complete.

**PRE-FILL BARRIER. Do not write any proposal row until this check completes.**

Every proposal requires these columns (verify headers before filling rows):
- `Change Type` — ADD / REMOVE / REPRIORITIZE
- `Evidence Artifact` — filename; `??` if unknown; PRIOR-classified artifacts are excluded
- `Before` / `After` — the specific before/after states
- `Null Hypothesis Override` **[MANDATORY]** — why does the null hypothesis fail for this row?
  Check this cell against banned forms before writing. No hedge phrases.
- `Defense Defeated` — row number from the Defense Register (e.g., "Row 2")

Banned-forms check: check every cell you are about to write against the vocabulary contract
banned forms list. Any match disqualifies the row. `"no change needed"` · `"clearly warranted"`
are the most common violations — they assert without defeating the null.

GATE 3 PASS CONDITION: All columns present as labeled headers. Banned-forms check activated.
Do not fill proposal rows without passing Gate 3.

---

## PHASE 3 — Null Hypothesis Override Proposals

Each row in this table claims the null hypothesis is wrong for a specific dimension.
Make the claim with evidence.

| # | Change Type | Evidence Artifact | Before | After | Null Hypothesis Override [MANDATORY] | Defense Defeated |
|---|-------------|------------------|--------|-------|--------------------------------------|-----------------|

`Null Hypothesis Override [MANDATORY]`: State the specific reason the current strategy
fails for this dimension. Check against banned forms before writing. `"no change needed"`
asserts the opposite of a proposal and is incoherent here — use it only in null declarations.

`Defense Defeated`: cite the Defense Register row number. "Row 3" satisfies. "The staleness
defense" without a row number does not.

Absent change types — each must have its own typed null declaration:

> ADD — NULL: The null hypothesis holds for ADD because [specific reason — check against
> banned forms before writing].

> REMOVE — NULL: The null hypothesis holds for REMOVE because [specific reason — check
> against banned forms before writing].

> REPRIORITIZE — NULL: The null hypothesis holds for REPRIORITIZE because [specific reason —
> check against banned forms before writing].

GATE 4: All change types addressed (proposal or typed null). No blank cells. No banned forms.

---

## WS-3 — Null Declaration Template (Null Hypothesis Confirmation)

> **WS-3 MILESTONE — fulfills Register Row 3**

A null declaration confirms that the null hypothesis holds for this change type. That
confirmation requires a specific reason — not a hedge phrase.

Template:
```
[CHANGE TYPE] — NULL: The null hypothesis holds because [specific reason — check against
banned forms before writing].
```

Enforcement:
1. Typed form required for each absent change type independently
2. `"no change needed"` · `"clearly warranted"` · `"seems sufficient"` are banned — they
   describe the null hypothesis holding without stating why evidence didn't defeat it
3. Null declarations are subject to the full vocabulary contract — no scope exemption
4. A single "nothing to change" statement covering all types is a structural failure

---

## PHASE 4 — Conflict Detection

Audit NEW artifacts for cross-artifact contradictions. Contradictions complicate null
hypothesis decisions — two artifacts pointing in opposite directions may mean neither
defeats the null.

| Artifact A | Artifact B | Dimension | Contradiction Type | Effect on Null Hypothesis |
|------------|------------|-----------|-------------------|-----------------------------|

No conflicts:
> CONFLICT DETECTION — NULL: No cross-artifact contradictions found; null hypothesis
> decisions are not complicated by conflicting evidence because [specific reason —
> banned forms apply].

GATE 5: Table filled or null declaration written. No banned forms.

---

## PHASE 5 — Confirmation Gate

Present all proposals and null declarations. The null hypothesis is the default.

> **STOP. Do not modify strategy.md until the user confirms.**
>
> Below are the proposals that claim the null hypothesis is wrong, and the null
> declarations confirming where it holds.
>
> Respond: **YES** (apply), **NO** (discard), or **REVISED** (modify before applying).
>
> [Present proposals table and null declarations]

GATE 6: Do not modify strategy.md until YES, NO, or REVISED received.
```

---

## V-04: Combined — Format + Lifecycle (Register Spine + Phase State Machine)

**Variation axes combined**: Output format (V-01: WS register as document spine) and
lifecycle emphasis (V-02: phase state machine with ENTRY/EXIT conditions).

**Hypothesis**: Combining a first-class register spine (every WS block is a top-level
heading that auditors scan) with a strict phase state machine (every phase declares
entry and exit conditions) creates a doubly-auditable structure. A reviewer can audit
write-surface completeness by scanning headers and audit phase sequencing by scanning
entry/exit conditions — two independent audit paths.

---

```
You are executing the topic:plan skill — Signal strategy revision.

The default outcome is NO CHANGE to strategy.md.

---

## SKILL MANIFEST

This manifest governs the entire execution. All contracts, phases, and write-surface
milestones are derived from this block.

**Phase sequence:**
0. Defense Register (pre-read, inside WS-1)
1. Signal Inventory
2. Artifact Reading
3. Proposals (entry blocked by WS-2; null declarations governed by WS-3)
4. Conflict Detection
5. Confirmation Gate

**Write-surface milestones:**
Three enforcement sections appear as first-class headers below. Audit completeness
by scanning section titles — three rows declared here, three `## WS-N` headers below.

**Gate chain:**
Gate 0 (WS-1) → Gate 1 → Gate 2 → Gate 3 (WS-2) → Gate 4 → Gate 5 → Gate 6

Each gate cites the next gate number. A phase cannot begin unless all prior gates
have passed in sequence.

---

## WRITE SURFACE REGISTER

| Row | Identifier | Surface Type           | Trigger Condition                                  |
|-----|------------|------------------------|----------------------------------------------------|
| 1   | WS-1       | Pre-read barrier       | Phase 0 entry — before any artifact open          |
| 2   | WS-2       | Schema boundary        | Phase 3 entry — before filling any proposal row   |
| 3   | WS-3       | Null declaration gate  | Phase 3 body — inside each null declaration       |

---

## VOCABULARY CONTRACT

| Token | Meaning                              | Violation                                          |
|-------|--------------------------------------|----------------------------------------------------|
| `??`  | Open obligation — unknown/unfilled   | Blank cell where `??` applies                     |
| `--`  | Closed decision — deliberately absent | `??` where a deliberate decision is correct       |

Banned forms (all cells, including null declarations — no scope exemption):
> `"no change needed"` · `"nothing to add"` · `"clearly warranted"` · `"seems sufficient"` ·
> `"a few artifacts"` · `"several artifacts"` · `"some signals"` · any non-integer count

Check every free-text cell against this list before writing. Any match is a gate failure.

---

## WS-1 — Pre-Read Barrier

> **WS-1 MILESTONE — fulfills Register Row 1**

ENTRY CONDITION: No artifacts read. Execution has not entered any phase.
JOB: Extract strategy date and commit Defense Register before evidence is gathered.
EXIT CONDITION: Strategy date extracted. All Defense Register rows filled. No `??` remaining.

**GATE 0 — PRE-SIGNAL STOP.**
Do not open strategy.md body or any signal artifact until Gate 0 passes.
Do not advance to Phase 1 without passing Gate 0.

**Phase 0 execution inside WS-1:**

Open strategy.md header only. Extract STRATEGY DATE: [YYYY-MM-DD]. Close without reading body.

Defense Register:

| Row | Change Dimension             | Current Strategy Position | Defense Argument      | Threshold to Defeat |
|-----|------------------------------|--------------------------|----------------------|---------------------|
| 1   | ADD new namespace coverage   | ??                        | ??                    | ??                  |
| 2   | REMOVE existing priority     | ??                        | ??                    | ??                  |
| 3   | REPRIORITIZE ordering        | ??                        | ??                    | ??                  |
| 4   | Coverage gap in namespace    | ??                        | ??                    | ??                  |
| 5   | Signal staleness             | ??                        | ??                    | ??                  |

GATE 0 PASS CONDITION: All cells filled with non-`??` values, no banned forms.

---

## PHASE 1 — Signal Inventory

ENTRY CONDITION: Gate 0 passed.
JOB: Assess all 9 namespaces. Produce inventory table. Write mandatory delta sentence.
EXIT CONDITION: All 9 rows filled. Delta sentence present with integer counts.

| Namespace | Artifact Filename | Artifact Date | Strategy Date | NEW / PRIOR |
|-----------|------------------|---------------|---------------|-------------|
| scout     | ??               | ??            | ??            | ??          |
| draft     | ??               | ??            | ??            | ??          |
| review    | ??               | ??            | ??            | ??          |
| flow      | ??               | ??            | ??            | ??          |
| trace     | ??               | ??            | ??            | ??          |
| prove     | ??               | ??            | ??            | ??          |
| listen    | ??               | ??            | ??            | ??          |
| program   | ??               | ??            | ??            | ??          |
| topic     | ??               | ??            | ??            | ??          |

No artifact: `--` filename, `--` date, `ABSENT` in NEW/PRIOR.

Mandatory delta sentence (integer values only; non-integer values are a gate failure):
> "Strategy was written on [DATE]. [N] artifacts are NEW. [M] artifacts are PRIOR."

**GATE 1 PASS CONDITION**: All 9 rows filled. Delta sentence present with integers.
Do not advance to Phase 2 without passing Gate 1.

---

## PHASE 2 — Artifact Reading

ENTRY CONDITION: Gate 1 passed. Inventory complete.
JOB: Read full content of every NEW artifact.
EXIT CONDITION: READING COMPLETE statement written with integer count.

Read every NEW-classified artifact in full.

Write: READING COMPLETE — [N] NEW artifacts read.

**GATE 2 PASS CONDITION**: READING COMPLETE present with integer.
Do not advance to WS-2 without passing Gate 2.

---

## WS-2 — Schema Boundary Check

> **WS-2 MILESTONE — fulfills Register Row 2**

ENTRY CONDITION: Gates 0, 1, 2 all passed.
JOB: Validate proposal table schema and prime banned-forms enforcement.
EXIT CONDITION: All mandatory columns confirmed. Banned-forms check activated for every cell.

**PRE-FILL BARRIER. Do not write any proposal row until this section completes.**

Mandatory column headers (check before filling):
- `Change Type` (ADD / REMOVE / REPRIORITIZE)
- `Evidence Artifact` (filename required; `??` only if truly unknown)
- `Before` / `After`
- `Inertia Defeated` **[MANDATORY]** — specific reason NO CHANGE is insufficient;
  check this cell against banned forms before writing; `"no change needed"` disqualifies
- `Defense Defeated` — Defense Register row number (e.g., "Row 3")

Banned-forms check activation:
Before writing each cell: scan the value against the vocabulary contract banned forms list.
Any match is a gate failure. This applies to every cell including `Inertia Defeated` and
null declaration reason cells.

**GATE 3 PASS CONDITION**: All mandatory columns present. Banned-forms check active.
Do not fill proposal rows without passing Gate 3.
Do not advance to Phase 3 without passing Gate 3.

---

## PHASE 3 — Proposals

ENTRY CONDITION: Gate 3 passed. Schema validated. Banned-forms check active.
JOB: Produce typed proposals and typed null declarations for all absent change types.
EXIT CONDITION: All three change types addressed. No blank cells. No banned forms.

| # | Change Type | Evidence Artifact | Before | After | Inertia Defeated [MANDATORY] | Defense Defeated |
|---|-------------|------------------|--------|-------|------------------------------|-----------------|

`Inertia Defeated [MANDATORY]`: specific reason NO CHANGE is insufficient. `"no change needed"`
disqualifies the row. Check before writing.

`Defense Defeated`: row number from Defense Register. "Row N" format required. A name without
a row number does not satisfy this column.

Absent change types (each typed separately per WS-3):

**GATE 4 PASS CONDITION**: All change types addressed (proposal or typed null). No blank cells.
No banned forms. Do not advance to Phase 4 without passing Gate 4.

---

## WS-3 — Null Declaration Template

> **WS-3 MILESTONE — fulfills Register Row 3**

ENTRY CONDITION: Operating inside Phase 3. A change type has no proposals.
JOB: Produce a typed null declaration with a specific reason that passes banned-forms check.
EXIT CONDITION: Typed form used. Reason cell passes banned-forms check.

Template:
```
[CHANGE TYPE] — NULL: [specific reason — check against banned forms before writing]
```

Rules:
1. Each absent change type requires its own labeled null declaration
2. `"no change needed"` · `"nothing to add"` · `"clearly warranted"` are banned
3. Null declarations are not exempt from the vocabulary contract
4. A single "nothing to change" covering multiple types is a structural violation

---

## PHASE 4 — Conflict Detection

ENTRY CONDITION: Gate 4 passed. Proposals and null declarations complete.
JOB: Audit NEW artifacts for cross-artifact contradictions.
EXIT CONDITION: Contradiction table filled or conflict null declaration written.

| Artifact A | Artifact B | Dimension | Contradiction Type | Resolution |
|------------|------------|-----------|-------------------|-----------|

No conflicts:
> CONFLICT DETECTION — NULL: [reason — banned forms apply]

**GATE 5 PASS CONDITION**: Table filled or null declaration present.
Do not advance to Phase 5 without passing Gate 5.

---

## PHASE 5 — Confirmation Gate

ENTRY CONDITION: Gate 5 passed. All proposals and null declarations finalized.
JOB: Present proposals to user. Halt until YES / NO / REVISED received.
EXIT CONDITION: User responds YES, NO, or REVISED.

> **STOP. Do not modify strategy.md until the user responds.**
>
> [Present proposals table and all null declarations]
>
> Reply YES (apply all), NO (discard all), or REVISED (specify modifications).

**GATE 6 PASS CONDITION**: User response received.
Do not modify strategy.md until Gate 6 passes.
```

---

## V-05: Combined — Role Sequence (Inverted) + Inertia Framing

**Variation axes combined**: Role sequence (inverted — artifact inventory runs before the
defense register is built, so the defense register is constructed with artifact dates already
known) and inertia framing (null hypothesis language throughout).

**Hypothesis**: Building the defense register AFTER knowing what artifacts exist (and how
old they are) produces stronger defense arguments than building it blind. The defense register
is still committed before full artifact content is read, but the defender now knows whether
any signals post-date the strategy. This closes the gap between a rubber-stamp defense
register and a genuinely calibrated one — while preserving the inertia-first discipline.

---

```
You are executing the topic:plan skill — Signal strategy revision.

The null hypothesis is: strategy.md is correct. This skill tries to defeat it.
The burden of proof is on change, not on the status quo.

---

## WRITE SURFACE REGISTER

> The null hypothesis is enforced at three write surfaces. Declared here before any
> phase executes. Three milestone sections follow.

| Row | Identifier | Surface Type           | Trigger Condition                                         |
|-----|------------|------------------------|-----------------------------------------------------------|
| 1   | WS-1       | Pre-read barrier       | After inventory, before reading artifact content (Phase 1 entry) |
| 2   | WS-2       | Schema boundary        | Before filling proposal columns (Phase 3 entry)           |
| 3   | WS-3       | Null declaration gate  | Inside each null declaration (Phase 3 body)               |

Note: In this skill, WS-1 fires after date/filename inventory but before content reading.
This allows the defense register to be built with artifact dates known but content unseen.

---

## VOCABULARY CONTRACT

| Token | Meaning                              | Violation                                          |
|-------|--------------------------------------|----------------------------------------------------|
| `??`  | Open obligation — unknown/unfilled   | Blank cell where `??` applies                     |
| `--`  | Closed decision — deliberately absent | `??` where a deliberate decision is correct       |

Banned forms (all cells, including null declarations — null declarations are not exempt):
> `"no change needed"` · `"nothing to add"` · `"clearly warranted"` · `"seems sufficient"` ·
> `"a few artifacts"` · `"several artifacts"` · `"some signals"` · any non-integer count

Check before writing. Any banned form is a gate failure.

---

## PHASE 0 — Date and Header Extraction

Open strategy.md header only. Do not read body content.
Extract: STRATEGY DATE: [YYYY-MM-DD] and listed namespace priorities.
Close the file.

This phase produces only the strategy date and header data. No content read. No
artifact content read. This is not a WS-1 gate — WS-1 fires after inventory completes.

GATE 0 PASS CONDITION: STRATEGY DATE recorded. Strategy header extracted.

---

## PHASE 1A — Artifact Inventory (Filenames and Dates Only)

Before building the defense register, discover what artifacts exist and how old they are.
Do not read artifact content yet.

| Namespace | Artifact Filename | Artifact Date | vs. Strategy Date | NEW / PRIOR |
|-----------|------------------|---------------|-------------------|-------------|
| scout     | ??               | ??            | ??                | ??          |
| draft     | ??               | ??            | ??                | ??          |
| review    | ??               | ??            | ??                | ??          |
| flow      | ??               | ??            | ??                | ??          |
| trace     | ??               | ??            | ??                | ??          |
| prove     | ??               | ??            | ??                | ??          |
| listen    | ??               | ??            | ??                | ??          |
| program   | ??               | ??            | ??                | ??          |
| topic     | ??               | ??            | ??                | ??          |

No artifact: `--` filename, `--` date, `ABSENT` classification.

Mandatory delta sentence (integers only; non-integer is gate failure):
> "Strategy was written on [DATE]. [N] artifacts are NEW. [M] artifacts are PRIOR."

GATE 1A PASS CONDITION: All 9 rows filled. Delta sentence present with integers.
Do not advance to WS-1 without passing Gate 1A.

---

## WS-1 — Pre-Read Barrier (Informed Defense Register)

> **WS-1 MILESTONE — fulfills Register Row 1**

The artifact dates are now known. The content is not. Build the defense register with
the knowledge of which artifacts post-date the strategy, but without reading their content.
This is the strongest possible defense commitment — informed about the threat's existence,
but not yet exposed to its arguments.

**GATE 0 (renumbered: GATE 1B) — PRE-CONTENT STOP.**
Do not read artifact content until the defense register is complete.
Do not advance to Phase 1B without passing this gate.

Defense Register (build with artifact dates known, content unseen):

| Row | Change Dimension             | Null Hypothesis (Strategy Says) | Defense Strength Given [N] NEW Artifacts | Content Threshold to Defeat |
|-----|------------------------------|---------------------------------|------------------------------------------|-----------------------------|
| 1   | ADD new namespace coverage   | ??                               | ??                                        | ??                          |
| 2   | REMOVE existing priority     | ??                               | ??                                        | ??                          |
| 3   | REPRIORITIZE ordering        | ??                               | ??                                        | ??                          |
| 4   | Coverage gap in namespace    | ??                               | ??                                        | ??                          |
| 5   | Signal staleness             | ??                               | ??                                        | ??                          |

`Defense Strength`: calibrate this knowing how many NEW artifacts exist. If 6 of 9
namespaces have NEW artifacts, the null hypothesis is under more pressure than if 1 does.
State this explicitly. Do not write `"low"` without a reason.

GATE 1B PASS CONDITION: All Defense Register cells filled with non-`??` values.
No banned forms. Defense strength calibrated against the actual NEW count.
Do not advance to Phase 1B without passing Gate 1B.

---

## PHASE 1B — Artifact Content Reading

GATE 1B passed. The null hypothesis is committed. Now read.

Read the full content of every NEW-classified artifact.

Write: CONTENT READING COMPLETE — [N] NEW artifacts read.

GATE 2 PASS CONDITION: CONTENT READING COMPLETE present with integer.

---

## WS-2 — Schema Boundary Check

> **WS-2 MILESTONE — fulfills Register Row 2**

**PRE-FILL BARRIER. Do not write any proposal row until this check completes.**

Every proposal claims the null hypothesis is wrong. The claim apparatus requires these
columns (verify headers before filling rows):

- `Change Type` (ADD / REMOVE / REPRIORITIZE)
- `Evidence Artifact` (filename; `??` only if genuinely unknown; PRIOR excluded)
- `Before` / `After`
- `Null Hypothesis Defeater` **[MANDATORY]** — the specific reason the null is wrong;
  check against banned forms before writing; `"no change needed"` · `"clearly warranted"`
  assert the opposite of a proposal and disqualify the row
- `Defense Defeated` — row number from Defense Register (e.g., "Row 2")

Banned-forms pre-fill check: for each cell about to be written, scan against the
vocabulary contract banned forms list. Any match disqualifies the row. This check applies
to `Null Hypothesis Defeater` cells and null declaration reason cells.

GATE 3 PASS CONDITION: All columns present. Banned-forms check active.
Do not fill proposal rows without passing Gate 3.

---

## PHASE 3 — Proposals

Each row claims the null hypothesis is wrong for a specific dimension.

| # | Change Type | Evidence Artifact | Before | After | Null Hypothesis Defeater [MANDATORY] | Defense Defeated |
|---|-------------|------------------|--------|-------|--------------------------------------|-----------------|

`Null Hypothesis Defeater [MANDATORY]`: why does the current strategy fail here?
Check against banned forms before writing.

`Defense Defeated`: Defense Register row number. "Row N" format. Name alone insufficient.

Absent change types — typed null declarations governed by WS-3 below.

GATE 4 PASS CONDITION: All three change types addressed. No blank cells. No banned forms.

---

## WS-3 — Null Declaration Template (Null Hypothesis Confirmation)

> **WS-3 MILESTONE — fulfills Register Row 3**

A null declaration confirms the null hypothesis holds for this change type. The confirmation
must name the evidence (or its absence) that preserved the null.

Template:
```
[CHANGE TYPE] — NULL: The null hypothesis holds because [specific reason referencing
artifact evidence or absence — check against banned forms before writing].
```

Enforcement:
1. One null declaration per absent change type — not one combined statement
2. `"no change needed"` · `"clearly warranted"` · `"seems sufficient"` are banned — they
   describe the outcome without explaining why evidence failed to defeat the null
3. Null declarations receive no scope exemption from the vocabulary contract
4. The reason cell must specifically address why the NEW artifacts did not defeat the
   null hypothesis for this change type

---

## PHASE 4 — Conflict Detection

Audit NEW artifacts for cross-artifact contradictions. Contradictions may weaken
proposals or preserve the null.

| Artifact A | Artifact B | Dimension | Contradiction | Effect on Proposals |
|------------|------------|-----------|---------------|---------------------|

No conflicts:
> CONFLICT DETECTION — NULL: No contradictions found; all null hypothesis decisions
> remain uncontested because [reason — banned forms apply].

GATE 5 PASS CONDITION: Table filled or null declaration written.

---

## PHASE 5 — Confirmation Gate

> **STOP. The null hypothesis stands until you confirm override.**
>
> Below are proposals claiming the null is wrong, and null declarations confirming
> where it holds.
>
> Reply **YES** (apply overrides), **NO** (null hypothesis stands in full), or
> **REVISED** (specify which overrides to modify before applying).
>
> [Present proposals table and all null declarations]

GATE 6 PASS CONDITION: User responds YES, NO, or REVISED.
Do not modify strategy.md until Gate 6 passes.
```

---

## Round 8 Predicted Scoring

### C-28, C-29, C-30 Coverage by Variation

| Variation | C-28 Mechanism                                        | C-29 Mechanism                               | C-30 Mechanism                                |
|-----------|-------------------------------------------------------|----------------------------------------------|-----------------------------------------------|
| V-01      | `## WS-1`, `## WS-2`, `## WS-3` top-level headers   | Register table as 2nd section after manifest | Each block opens with "fulfills Register Row N" |
| V-02      | Same header pattern; WS blocks are phase transitions  | Register before Phase 0 in SKILL ARCHITECTURE | "WS-N MILESTONE — fulfills Register Row N" in each block |
| V-03      | Same header pattern; blocks carry null-hypothesis framing | Register before Phase 0 in its own section | "fulfills Register Row N" in each block header |
| V-04      | Same header pattern; blocks carry ENTRY/JOB/EXIT     | Register in SKILL MANIFEST section           | "WS-N MILESTONE — fulfills Register Row N" in each |
| V-05      | Same header pattern; WS-1 fires after inventory (inverted) | Register declares inverted WS-1 trigger | "fulfills Register Row 1" with trigger note |

### Essential Criteria Coverage (all five variations)

| Criterion | Coverage |
|-----------|---------|
| C-01 Read strategy.md | Phase 0 opens strategy.md header, cites structure |
| C-02 All 9 namespaces | Phase 1 table has all 9 namespace rows |
| C-03 Delta detection | NEW/PRIOR split, strategy date named, PRIOR excluded |
| C-04 Typed proposals | ADD / REMOVE / REPRIORITIZE; typed null for each absent |
| C-05 Confirmation gate | Phase 5 explicit YES/NO/REVISED halt |

### Recommended Criteria Coverage

| Criterion | Coverage |
|-----------|---------|
| C-06 Evidence citation | Evidence Artifact column in proposals table |
| C-07 Before/After diff | Before/After columns mandatory |
| C-08 Inertia justification | Inertia Defeated [MANDATORY] column; banned forms disqualify |

### Discriminating Axes for Round 9

C-28, C-29, and C-30 are predicted to reach saturation this round — all five designs
address them architecturally. The predicted discriminators for Round 9 will emerge from:

1. **Defense register column precision** — does the defense register schema require a
   "Defense Strength" column calibrated to the actual artifact count, or is a bare
   "Defense Argument" column sufficient? V-05 adds this calibration; others do not.

2. **WS-1 timing flexibility** — V-05 fires WS-1 after inventory but before content read.
   V-01–V-04 fire WS-1 before any artifact opens. A rubric criterion distinguishing
   "pre-inventory" from "post-inventory but pre-content" would differentiate V-05 from
   all others.

3. **Conflict detection output completeness** — Phase 4 conflict detection produces a
   table in all five variations, but the "Effect on Proposals" or "Effect on Null
   Hypothesis" column appears only in V-03 and V-05. A criterion requiring conflict
   detection to feed back into the proposal table would distinguish this.

```json
{
  "round": 8,
  "rubric_version": "v8",
  "max_score": 100,
  "new_criteria": ["C-28", "C-29", "C-30"],
  "predicted_all_pass_c28": true,
  "predicted_all_pass_c29": true,
  "predicted_all_pass_c30": true,
  "predicted_discriminators_round_9": [
    "Defense register calibration column: 'defense strength given N NEW artifacts' vs bare defense argument",
    "WS-1 timing: pre-inventory vs post-inventory-pre-content as distinct enforcement sites",
    "Conflict detection feedback loop: effect-on-proposals column linking Phase 4 back to Phase 3"
  ]
}
```
