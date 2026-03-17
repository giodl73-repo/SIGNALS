# topic-plan Skill Variations -- Round 6 (rubric v6, 2026-03-15)

Rubric: v6 (C-01 through C-26; C-24 Cell-level banned-forms check instruction,
C-25 Banned-forms scope propagation, C-26 Gate-0 pre-signal stop gate are the
three new aspirational criteria extracted from Round 5 scorecard excellence
signals)

Round 5 recap: V-05 (full combination: Boundary field + D-N Source dimension +
PROPOSAL SCOPE block) scored highest at 99.33. Two PARTIAL criteria persist
from R5 V-05:
- C-10: Schema H present but not in its own dedicated numbered phase; no
  "CONFLICT DETECTION -- NULL" typed null form.
- C-13: "Defense defeated: MANDATORY" stated as a labeled paragraph below the
  schema, not in the column header itself.

Three patterns appeared in R5 PASS cells with no matching criterion in C-01--C-23:
- V-03 C-16 PASS: "Check cell against BANNED FORMS list before presenting.
  Any banned form disqualifies the row." This is a point-of-production check
  instruction -- distinct from C-16 (defines/bans phrases) and C-23 (quotes
  them verbatim). The banned forms rule becomes an active write-time gate at
  each cell, not a post-hoc quality note.
- V-03 C-09 PASS: "with BANNED FORMS applied to reasons" in null declarations.
  Null declaration justification cells are subject to the same banned forms
  check as proposal rows. C-16 and C-23 don't constrain scope; this pattern
  closes the null-declaration escape hatch.
- V-02 C-12 PASS: "Gate 0 through Gate 5." The pre-signal defense register
  (Phase 0) has its own numbered stop gate. C-20 requires sequential numbered
  gates but doesn't require Phase 0 to be explicitly gated; a Phase 0 without
  Gate 0 satisfies C-20 while leaving the pre-signal commitment ungated.

Round 6 targets: C-24 (cell-level check instruction at point of production,
not just a defined list), C-25 (banned-forms scope extends explicitly to null
declaration reason cells), C-26 (Phase 0 defense register has its own Gate 0
that explicitly blocks all artifact reads until it passes).

Three single-axis variations (V-01, V-02, V-03), then two combinations (V-04,
V-05).

---

## V-01: Output format -- Cell-level banned-forms check instruction (C-24 target)

**Variation axis**: Output format -- each column that produces free-text
justification output carries an explicit point-of-production instruction
immediately before the schema header: "Before writing each [vs. NO CHANGE /
inertia] cell, check it against the BANNED OUTPUT FORMS list above. Any match
disqualifies the row." The instruction appears at the schema boundary -- at the
fill point, not only in the preamble.

**Hypothesis**: R5 V-05 defines banned forms in the preamble BANNED OUTPUT FORMS
block, and Gate 5 checks both vs. NO CHANGE and null reasons against it. But
the preamble block is a standing reference, not a point-of-production directive.
C-24 requires an explicit check instruction "at the column or phase level" that
directs the model to check the cell before writing. A preamble-level list
without a cell-level check instruction does not satisfy C-24 even when the list
is verbatim-quoted. The fix is a labeled CELL-LEVEL CHECK block placed
immediately above each schema that contains free-text justification cells.
V-02 (null declaration scope, C-25) and V-03 (Gate-0, C-26) are omitted to
isolate the C-24 axis. Expected: C-24 PASS, C-25 FAIL (null declaration check
embedded in template but not explicitly instructed), C-26 FAIL (Gate 0 exists
but no PRE-COMMIT block explicitly blocking artifact reads).

```
You are running /topic:plan for the topic named in the user's message.

---

## VOCABULARY CONTRACT (standing reference -- applies throughout all phases)

Sentinel tokens:
  `??`  -- open obligation: value is unknown or not yet determined
  `--`  -- closed decision: value is deliberately absent or not applicable

Named violations:
  VIOLATION-1: leaving a cell blank when `??` would be correct
  VIOLATION-2: writing `??` for a confirmed zero (zero is the required form)
  VIOLATION-3: writing `--` in a required cell (only optional cells accept `--`)

## BANNED OUTPUT FORMS (standing reference -- applies to all free-text cells)

The following strings are banned in all free-text justification cells.
Any match disqualifies the row or null declaration containing it.

vs. NO CHANGE and inertia cells:
  "no change needed"
  "clearly warranted"
  "no compelling reason"
  "not necessary at this time"
  "nothing to add"

Null declaration reason cells:
  "no new signals"
  "nothing to add"
  "no changes needed"
  "not applicable"

Delta count sentence:
  "a few"
  "several"
  "some"
  "multiple"
  "many"

---

## Pre-committed schemas (fill in order -- no schema may be skipped or replaced
## with prose)

**Schema DR -- Defense register** (Phase 0 only; LOCKED before any artifact
read; every row is a dimension currently defended by strategy.md)

| D-R-N | Dimension name | Current defense argument (from strategy.md) |
|-------|---------------|----------------------------------------------|
| D-R-1 |               |                                              |
| D-R-2 |               |                                              |
| ...   |               |                                              |

Every "Defense defeated (Row D-R-N)" citation in Schemas E and F must name a
specific D-R-N row from this table. A named defense without a row number does
not satisfy that column.

**Schema A -- Strategy commitment** (Phase 1 only; SEALED at Gate 1)

| Field               | Value |
|---------------------|-------|
| Strategy file       |       |
| Strategy date       |       |
| Completion criteria |       |
| Scope               |       |

Dimensions (label D-1 through D-N in order of appearance in strategy.md):

| Label | Dimension name | What strategy.md says |
|-------|---------------|----------------------|
| D-1   |               |                      |
| D-2   |               |                      |
| ...   |               |                      |

VERBATIM EVIDENCE BLOCK (required output artifact):

  ===VERBATIM START===
  [paste exact text from strategy.md -- no paraphrase, no summary,
   no restatement; copy-paste the exact words as they appear]
  ===VERBATIM END===
  Source dimension: D-[N] -- [dimension name]
  (D-N label must match a row in the Schema A dimensions table above.
   A Source dimension not matching a D-N label fails this block.)

  ================================================================
  STRATEGY.MD SEALED
  Sealed after: Phase 1 (Schema A and VERBATIM BLOCK complete)
  Prohibition: strategy.md may not be re-opened or re-read until
               after the user replies YES, NO, or REVISED.
  Violation condition: Any "Before" value written after this line
               that contains text not present in the Schema A D-N
               rows above is a SEAL violation and must be dropped.
  Prohibition lifts: After user reply to the confirmation gate.
  Schema A contains: [N] dimensions labeled D-1 through D-[N]
  Boundary: Schema A complete. No signal artifacts examined yet.
  ================================================================

**Schema B -- Signal inventory**
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|

**Schema C -- Namespace audit (all 9 rows required)**
Rules:
- All 9 rows must appear. Absent namespaces: Total = 0, New = 0, pressure = NONE.
- Do not write ABSENT or skip any row. Zero-counts are the required form.
- Change pressure: HIGH if New > 0 | LOW if Total > 0 and New = 0 | NONE if
  Total = 0

| Namespace | Total | New | Change pressure |
|-----------|-------|-----|-----------------|
| scout     |       |     | HIGH/LOW/NONE   |
| draft     |       |     | HIGH/LOW/NONE   |
| review    |       |     | HIGH/LOW/NONE   |
| flow      |       |     | HIGH/LOW/NONE   |
| trace     |       |     | HIGH/LOW/NONE   |
| prove     |       |     | HIGH/LOW/NONE   |
| listen    |       |     | HIGH/LOW/NONE   |
| program   |       |     | HIGH/LOW/NONE   |
| topic     |       |     | HIGH/LOW/NONE   |

After Schema C, write the PROPOSAL SCOPE block:

  ================================================================
  PROPOSAL SCOPE
  HIGH-pressure namespaces (New > 0): [list names, or "none"]
  Excluded from proposals: [all remaining namespaces not listed above]
  Rule: Phase 5 proposals may only cite evidence from HIGH-pressure
        namespaces. A proposal row citing any excluded namespace is a
        SCOPE violation and must be dropped.
  ================================================================

**Schema D -- Coverage map**
| Schema A label | Dimension | NEW signal finding | Assessment |
|----------------|-----------|--------------------|---------  |

(CELL-LEVEL CHECK: before writing each vs. NO CHANGE cell in Schema E or F,
check it against the BANNED OUTPUT FORMS list above. Any match disqualifies
the row. Do not present the cell before completing the check.)

**Schema E -- Additions**
| # | Dimension [NEW] | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before (Schema A text) | After | vs. NO CHANGE -- MANDATORY |
|---|-----------------|-------------------|--------------------|------------------------------|------------------------|-------|---------------------------|

**Schema F -- Removals and Reprioritizations**
| # | Action | Dimension | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before (Schema A text) | After | vs. NO CHANGE -- MANDATORY |
|---|--------|-----------|-------------------|--------------------|------------------------------|------------------------|-------|---------------------------|

**Schema G -- Before/after diff**
| Dimension | Schema A ref | Before | After | Proposal ref |
|-----------|-------------|--------|-------|--------------|

**Schema H -- Conflict audit** (if empty, write typed null below:
CONFLICT DETECTION -- NULL: [specific reason])
| Conflict ID | Signal A | Signal B | Dimension | Nature |
|-------------|----------|----------|-----------|--------|

---

## Phase 0 -- Defense register

Read `simulations/TOPICS.md` to find the strategy file. Read strategy.md once.

Fill Schema DR: one row per dimension currently defended in strategy.md. Each
defense argument must be non-generic and trace to specific strategy.md text.
"No reason to change" and "no compelling reason" are banned defense arguments.

[Gate 0 -- reproduce with all three fields filled:
  GATE 0 | Phase: Defense register
  Condition evaluated: [Schema DR filled; each argument non-generic and tracing
                        to strategy.md text]
  Result found: [D-R-N count; example defense argument]
  STATUS: PASS / STOP]

Do not begin Phase 1 until Gate 0 shows STATUS: PASS.

---

## Phase 1 -- Strategy commitment and seal

Read strategy.md to fill Schema A (last authorized read; SEAL closes at Gate 1).

Fill Schema A, VERBATIM EVIDENCE BLOCK (Source dimension D-[N] -- [name]),
and STRATEGY.MD SEALED block (all six fields, Boundary field both halves).

[Gate 1 -- reproduce with all three fields filled:
  GATE 1 | Phase: Strategy commitment
  Condition evaluated: [Schema A filled; VERBATIM BLOCK delimiters + Source
                        dimension in D-N format; SEALED block 6 fields with
                        Boundary: "Schema A complete. No signal artifacts
                        examined yet."]
  Result found: [Strategy date, D-N count, Source dimension label, "SEAL +
                 Boundary confirmed"]
  STATUS: PASS / STOP]

Do not begin Phase 2 until Gate 1 shows STATUS: PASS.

---

## Phase 2 -- Signal inventory

List every artifact in `simulations/` whose filename contains the topic slug.
Fill Schema B. Fill Schema C (all 9 rows; zero-counts; NEVER write ABSENT).
Write PROPOSAL SCOPE block after Schema C.

NEW = artifact date strictly after Schema A Strategy date.
PRIOR = date on or before Schema A Strategy date.

Write the mandatory delta count sentence:
"Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
N and M must be integers. Writing "a few", "several", "some", or any
non-integer value is a gate failure.

If no artifacts: "No signal artifacts found. Cannot run /topic:plan." Stop.
If no HIGH-pressure namespaces: "STRATEGY CURRENT." Stop.

[Gate 2 -- reproduce with all three fields filled:
  GATE 2 | Phase: Signal inventory and scope declaration
  Condition evaluated: [9 namespace rows; ABSENT not used; PROPOSAL SCOPE
                        written; delta sentence with integer counts]
  Result found: [namespace pressures; SCOPE namespaces; delta sentence]
  STATUS: PASS / STOP]

Do not begin Phase 3 until Gate 2 shows STATUS: PASS.

---

## Phase 3 -- Delta partition

Partition Schema B into NEW and PRIOR. PRIOR artifacts may not drive proposals.

[Gate 3 -- reproduce with all three fields filled:
  GATE 3 | Phase: Delta partition
  Condition evaluated: [NEW vs PRIOR count confirmed]
  Result found: [filenames classified as NEW, or "none new"]
  STATUS: PASS / STOP]

If STATUS: STOP: "STRATEGY CURRENT." End here.
Do not begin Phase 4 until Gate 3 shows STATUS: PASS.

---

## Phase 4 -- Read NEW artifacts

Read each NEW artifact. Strategy.md remains sealed.

Write a short paragraph (4-6 sentences). Name at least two artifact filenames.

[Gate 4 -- reproduce with all three fields filled:
  GATE 4 | Phase: New artifact synthesis
  Condition evaluated: [paragraph written; at least two filenames cited]
  Result found: [filenames cited]
  STATUS: PASS / STOP]

Do not begin Phase 5 until Gate 4 shows STATUS: PASS.

---

## Phase 5 -- Coverage map and proposals

PROPOSAL SCOPE active: [reproduce HIGH-pressure namespaces from PROPOSAL SCOPE].

Fill Schema D. Default verdict: NO CHANGE. Burden of proof is on change.

Fill Schemas E and F. For every proposal row:
- Evidence in Phase 3 NEW list AND in PROPOSAL SCOPE namespaces
- Schema A ref (D-N) matches locked dimension; cross-check against Source
  dimension in VERBATIM BLOCK
- Defense defeated (Row D-R-N): cite specific D-R-N from Schema DR; a named
  defense without a row number does not satisfy this column
- Before from locked Schema A only; drop proposal if Before cannot be filled
  from Schema A
- vs. NO CHANGE (MANDATORY): name a specific consequence; check this cell
  against the BANNED OUTPUT FORMS list before presenting; any match
  disqualifies the row

Null declarations (each type labeled separately):
  ADDITIONS: none -- [reason] | or [N] proposed
  REMOVALS: none -- [reason] | or [N] proposed
  REPRIORITIZATIONS: none -- [reason] | or [N] proposed

Fill Schema G. Fill Schema H (or write typed null if empty).

[Gate 5 -- reproduce with all three fields filled:
  GATE 5 | Phase: Proposals complete
  Condition evaluated: [null declarations present; evidence in SCOPE; D-N refs
                        locked; vs. NO CHANGE cells checked against BANNED
                        OUTPUT FORMS; Schema G count; H or typed null]
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Do not begin Phase 6 until Gate 5 shows STATUS: PASS.

---

## Phase 6 -- Confirmation gate

Display all schemas (Schema DR, VERBATIM BLOCK, SEALED block, PROPOSAL SCOPE).

Write exactly:

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
to apply your version
---

[Gate 6 -- reproduce with all three fields filled:
  GATE 6 | Phase: Confirmation gate
  Condition evaluated: [PENDING CONFIRMATION with integer counts]
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Stop. Write nothing further until the user replies.

---

## Apply (triggered by YES or REVISED)

The SEAL lifts. Write exactly the confirmed changes to strategy.md. Confirm:
"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-02: Lifecycle emphasis -- Banned-forms scope propagation to null declarations (C-25 target)

**Variation axis**: Lifecycle emphasis -- the banned forms constraint is
propagated into the null declaration templates at the point of production.
Each null declaration reason cell carries an in-template banned-forms check
instruction and verbatim-quoted banned strings inline, making the template
itself signal the violation condition rather than relying on a gate-level
check after the cell is already written.

**Hypothesis**: R5 V-05's Gate 5 checks "both vs. NO CHANGE and null declaration
reasons" against the banned forms list, but this is a post-fill gate, not a
pre-fill cell-level instruction inside the template. C-25 requires the banned
forms constraint to apply to every free-text justification cell including null
declaration reason cells, not only proposal rows. A Gate 5 check satisfies C-16
and C-23 but not C-25: C-25 requires scope propagation, meaning the constraint
must be explicitly stated as applying to null cells, not inferred from a global
gate. Embedding verbatim banned strings inline in each null declaration template
-- with an explicit "check this reason against BANNED OUTPUT FORMS before
writing" instruction -- closes both C-24 (cell-level check instruction) and
C-25 (explicit scope propagation). V-01 (column-level check, C-24) and V-03
(Gate-0, C-26) are omitted from this variation to isolate the C-25 axis.

```
You are running /topic:plan for the topic named in the user's message.

---

## VOCABULARY CONTRACT (standing reference)

Sentinel tokens:
  `??`  -- open obligation: unknown or not yet determined
  `--`  -- closed decision: deliberately absent or not applicable

Named violations:
  VIOLATION-1: leaving a cell blank when `??` would be correct
  VIOLATION-2: writing `??` for a confirmed zero
  VIOLATION-3: writing `--` in a required cell

## BANNED OUTPUT FORMS (standing reference)

Apply this list to every free-text cell before presenting.
Any match disqualifies the row or null declaration containing it.

vs. NO CHANGE and inertia cells:
  "no change needed"
  "clearly warranted"
  "no compelling reason"
  "not necessary at this time"
  "nothing to add"

Null declaration reason cells (same constraint; null declarations are NOT
exempt; a banned form in a null declaration reason fails the declaration):
  "no new signals"
  "nothing to add"
  "no changes needed"
  "not applicable"

Delta count sentence:
  "a few"
  "several"
  "some"
  "multiple"
  "many"

---

## Pre-committed schemas (fill in order -- no schema may be skipped or replaced
## with prose)

**Schema DR -- Defense register** (Phase 0; LOCKED before any artifact read)

| D-R-N | Dimension name | Current defense argument (from strategy.md) |
|-------|---------------|----------------------------------------------|
| D-R-1 |               |                                              |
| D-R-2 |               |                                              |
| ...   |               |                                              |

**Schema A -- Strategy commitment** (Phase 1; SEALED at Gate 1)

| Field               | Value |
|---------------------|-------|
| Strategy file       |       |
| Strategy date       |       |
| Completion criteria |       |
| Scope               |       |

Dimensions:

| Label | Dimension name | What strategy.md says |
|-------|---------------|----------------------|
| D-1   |               |                      |
| D-2   |               |                      |
| ...   |               |                      |

VERBATIM EVIDENCE BLOCK:

  ===VERBATIM START===
  [paste exact text from strategy.md]
  ===VERBATIM END===
  Source dimension: D-[N] -- [dimension name]

  ================================================================
  STRATEGY.MD SEALED
  Sealed after: Phase 1
  Prohibition: strategy.md may not be re-opened until after user reply.
  Violation condition: Any "Before" value not in Schema A D-N rows is a
               SEAL violation and must be dropped.
  Prohibition lifts: After user reply.
  Schema A contains: [N] dimensions labeled D-1 through D-[N]
  Boundary: Schema A complete. No signal artifacts examined yet.
  ================================================================

**Schema B -- Signal inventory**
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|

**Schema C -- Namespace audit (all 9 rows required)**
Rules: all 9 rows; zero-counts for absent; NEVER write ABSENT
Change pressure: HIGH if New > 0 | LOW if Total > 0 and New = 0 | NONE if
Total = 0

| Namespace | Total | New | Change pressure |
|-----------|-------|-----|-----------------|
| scout     |       |     | HIGH/LOW/NONE   |
| draft     |       |     | HIGH/LOW/NONE   |
| review    |       |     | HIGH/LOW/NONE   |
| flow      |       |     | HIGH/LOW/NONE   |
| trace     |       |     | HIGH/LOW/NONE   |
| prove     |       |     | HIGH/LOW/NONE   |
| listen    |       |     | HIGH/LOW/NONE   |
| program   |       |     | HIGH/LOW/NONE   |
| topic     |       |     | HIGH/LOW/NONE   |

After Schema C, write the PROPOSAL SCOPE block:

  ================================================================
  PROPOSAL SCOPE
  HIGH-pressure namespaces (New > 0): [list names, or "none"]
  Excluded from proposals: [remaining namespaces]
  Rule: proposals may only cite evidence from HIGH-pressure namespaces.
  ================================================================

**Schema D -- Coverage map**
| Schema A label | Dimension | NEW signal finding | Assessment |
|----------------|-----------|--------------------|---------  |

**Schema E -- Additions**
| # | Dimension [NEW] | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before | After | vs. NO CHANGE -- MANDATORY |
|---|-----------------|-------------------|--------------------|------------------------------|--------|-------|---------------------------|

**Schema F -- Removals and Reprioritizations**
| # | Action | Dimension | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before | After | vs. NO CHANGE -- MANDATORY |
|---|--------|-----------|-------------------|--------------------|------------------------------|--------|-------|---------------------------|

**Schema G -- Before/after diff**
| Dimension | Schema A ref | Before | After | Proposal ref |
|-----------|-------------|--------|-------|--------------|

**Schema H -- Conflict audit**
| Conflict ID | Signal A | Signal B | Dimension | Nature |
|-------------|----------|----------|-----------|--------|

---

## Phase 0 -- Defense register

Read `simulations/TOPICS.md` to find strategy file. Read strategy.md.

Fill Schema DR: one row per dimension. Each defense argument non-generic,
traces to strategy.md text.

[Gate 0 -- reproduce with all three fields filled:
  GATE 0 | Phase: Defense register
  Condition evaluated: [Schema DR filled; arguments non-generic]
  Result found: [D-R-N count; example argument]
  STATUS: PASS / STOP]

Do not begin Phase 1 until Gate 0 shows STATUS: PASS.

---

## Phase 1 -- Strategy commitment and seal

Read strategy.md (last authorized read). Fill Schema A, VERBATIM EVIDENCE BLOCK
(Source dimension D-[N] -- [name]), STRATEGY.MD SEALED block (6 fields, Boundary
both halves).

[Gate 1 -- reproduce with all three fields filled:
  GATE 1 | Phase: Strategy commitment
  Condition evaluated: [Schema A; VERBATIM BLOCK; SEALED block 6 fields]
  Result found: [Strategy date, D-N count, Source label, Boundary confirmed]
  STATUS: PASS / STOP]

Do not begin Phase 2 until Gate 1 shows STATUS: PASS.

---

## Phase 2 -- Signal inventory

Fill Schema B and Schema C (all 9 rows; zero-counts; NEVER ABSENT).
Write PROPOSAL SCOPE block.

NEW = date strictly after Schema A Strategy date. PRIOR = date on or before.

Write the mandatory delta count sentence:
"Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
N and M must be integers. Non-integer values are a gate failure.

If no artifacts: stop. If no HIGH-pressure namespaces: "STRATEGY CURRENT." Stop.

[Gate 2 -- reproduce with all three fields filled:
  GATE 2 | Phase: Signal inventory
  Condition evaluated: [9 rows; ABSENT not used; PROPOSAL SCOPE written; delta
                        sentence with integers]
  Result found: [pressures; SCOPE namespaces; delta sentence]
  STATUS: PASS / STOP]

Do not begin Phase 3 until Gate 2 shows STATUS: PASS.

---

## Phase 3 -- Delta partition

Partition Schema B into NEW and PRIOR. PRIOR artifacts may not drive proposals.

[Gate 3 -- reproduce with all three fields filled:
  GATE 3 | Phase: Delta partition
  Condition evaluated: [NEW vs PRIOR confirmed]
  Result found: [filenames as NEW, or "none new"]
  STATUS: PASS / STOP]

If STATUS: STOP: "STRATEGY CURRENT." End here.
Do not begin Phase 4 until Gate 3 shows STATUS: PASS.

---

## Phase 4 -- Read NEW artifacts

Read each NEW artifact. Write a paragraph (4-6 sentences). Name >= 2 filenames.

[Gate 4 -- reproduce with all three fields filled:
  GATE 4 | Phase: New artifact synthesis
  Condition evaluated: [paragraph written; two filenames cited]
  Result found: [filenames cited]
  STATUS: PASS / STOP]

Do not begin Phase 5 until Gate 4 shows STATUS: PASS.

---

## Phase 5 -- Coverage map and proposals

PROPOSAL SCOPE active: [HIGH-pressure namespaces from PROPOSAL SCOPE].

Fill Schema D. Default verdict: NO CHANGE.

Fill Schemas E and F. For every proposal row:
- Evidence in Phase 3 NEW list AND in PROPOSAL SCOPE namespaces
- Schema A ref (D-N) matches locked dimension
- Defense defeated (Row D-R-N): specific D-R-N row; no row number fails column
- Before from locked Schema A only
- vs. NO CHANGE (MANDATORY): name a specific consequence; check against
  BANNED OUTPUT FORMS before presenting; any match disqualifies the row

Null declarations (each type labeled separately; the reason cell is subject
to the BANNED OUTPUT FORMS constraint; check the reason against the banned
null declaration forms list before writing; any match fails this declaration):

  ADDITIONS: none -- [specific reason explaining why no additions are warranted;
    check this reason against BANNED OUTPUT FORMS before writing;
    "no new signals", "nothing to add", "no changes needed", "not applicable"
    are banned and any match here fails this declaration]
  | or [N] proposed

  REMOVALS: none -- [specific reason explaining why no removals are warranted;
    check this reason against BANNED OUTPUT FORMS before writing;
    "no new signals", "nothing to add", "no changes needed", "not applicable"
    are banned and any match here fails this declaration]
  | or [N] proposed

  REPRIORITIZATIONS: none -- [specific reason explaining why no
    reprioritizations are warranted; check this reason against BANNED OUTPUT
    FORMS before writing; "no new signals", "nothing to add", "no changes
    needed", "not applicable" are banned and any match here fails this
    declaration]
  | or [N] proposed

Fill Schema G. If Schema H is empty:
CONFLICT DETECTION -- NULL: [specific reason]

[Gate 5 -- reproduce with all three fields filled:
  GATE 5 | Phase: Proposals complete
  Condition evaluated: [null declarations with checked reasons; evidence in
                        SCOPE; D-N refs locked; Schema G; H or typed null]
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Do not begin Phase 6 until Gate 5 shows STATUS: PASS.

---

## Phase 6 -- Confirmation gate

Display all schemas (Schema DR, VERBATIM BLOCK, SEALED block, PROPOSAL SCOPE).

Write exactly:

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
to apply your version
---

[Gate 6 -- reproduce with all three fields filled:
  GATE 6 | Phase: Confirmation gate
  Condition evaluated: [PENDING CONFIRMATION with integer counts]
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Stop. Write nothing further until the user replies.

---

## Apply (triggered by YES or REVISED)

Write exactly the confirmed changes to strategy.md. Confirm:
"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-03: Role sequence -- Gate-0 pre-signal stop gate with PRE-COMMIT block (C-26 target)

**Variation axis**: Role sequence -- the pre-signal defense register (Phase 0)
gains a PRE-COMMIT BLOCK that appears before any Phase 0 action, explicitly
stating that no artifact may be read until Gate 0 passes. Gate 0 closes with
an instruction: "Do not advance to Phase 1 and do not read any signal artifact
until this gate shows STATUS: PASS." The two-part structure -- pre-action
declaration plus gate instruction -- makes Gate 0 an explicit read barrier, not
merely a phase boundary.

**Hypothesis**: R5 V-05 had Phase 0 with a defense register and a Gate 0 in
the sequential chain (C-18 PASS, C-20 PASS). But Gate 0's instruction reads
"Do not begin Phase 1 until Gate 0 shows STATUS: PASS," which blocks Phase 1
but does not explicitly block artifact reads. C-26 requires the pre-signal gate
to explicitly block any artifact reads, not only Phase 1 advancement. The gap:
a motivated model could read signal files during Phase 0 before Gate 0 fires,
satisfy Phase 0, then pass Gate 0 -- no instruction says artifact reads are
forbidden before Gate 0. The PRE-COMMIT BLOCK closes this gap by declaring at
the start of Phase 0 that no reads of any kind are permitted until Gate 0 passes.
V-01 (C-24) and V-02 (C-25) are excluded from this variation.

```
You are running /topic:plan for the topic named in the user's message.

---

## VOCABULARY CONTRACT (standing reference)

Sentinel tokens:
  `??`  -- open obligation: unknown or not yet determined
  `--`  -- closed decision: deliberately absent or not applicable

Named violations:
  VIOLATION-1: leaving a cell blank when `??` would be correct
  VIOLATION-2: writing `??` for a confirmed zero
  VIOLATION-3: writing `--` in a required cell

## BANNED OUTPUT FORMS (standing reference)

Apply this list to every free-text cell before presenting.
Any match disqualifies the row or null declaration containing it.

vs. NO CHANGE and inertia cells:
  "no change needed"
  "clearly warranted"
  "no compelling reason"
  "not necessary at this time"
  "nothing to add"

Null declaration reason cells:
  "no new signals"
  "nothing to add"
  "no changes needed"
  "not applicable"

Delta count sentence:
  "a few"
  "several"
  "some"
  "multiple"
  "many"

---

## Pre-committed schemas (fill in order -- no schema may be skipped or replaced
## with prose)

**Schema DR -- Defense register** (Phase 0 only; LOCKED and SEALED before any
artifact read; this table must be committed in writing before strategy.md or
any signal file is opened for any purpose)

| D-R-N | Dimension name | Current defense argument (from strategy.md) |
|-------|---------------|----------------------------------------------|
| D-R-1 |               |                                              |
| D-R-2 |               |                                              |
| ...   |               |                                              |

Every "Defense defeated (Row D-R-N)" citation in Schemas E and F must name a
specific D-R-N row from this table. A named defense without a row number does
not satisfy that column.

**Schema A -- Strategy commitment** (Phase 1 only; SEALED at Gate 1)

| Field               | Value |
|---------------------|-------|
| Strategy file       |       |
| Strategy date       |       |
| Completion criteria |       |
| Scope               |       |

Dimensions:

| Label | Dimension name | What strategy.md says |
|-------|---------------|----------------------|
| D-1   |               |                      |
| D-2   |               |                      |
| ...   |               |                      |

VERBATIM EVIDENCE BLOCK:

  ===VERBATIM START===
  [paste exact text from strategy.md]
  ===VERBATIM END===
  Source dimension: D-[N] -- [dimension name]

  ================================================================
  STRATEGY.MD SEALED
  Sealed after: Phase 1
  Prohibition: strategy.md may not be re-opened until after user reply.
  Violation condition: Any "Before" value not in Schema A D-N rows is a
               SEAL violation and must be dropped.
  Prohibition lifts: After user reply.
  Schema A contains: [N] dimensions labeled D-1 through D-[N]
  Boundary: Schema A complete. No signal artifacts examined yet.
  ================================================================

**Schema B -- Signal inventory**
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|

**Schema C -- Namespace audit (all 9 rows required)**
Rules: all 9 rows; zero-counts for absent; NEVER write ABSENT
Change pressure: HIGH if New > 0 | LOW if Total > 0 and New = 0 | NONE if
Total = 0

| Namespace | Total | New | Change pressure |
|-----------|-------|-----|-----------------|
| scout     |       |     | HIGH/LOW/NONE   |
| draft     |       |     | HIGH/LOW/NONE   |
| review    |       |     | HIGH/LOW/NONE   |
| flow      |       |     | HIGH/LOW/NONE   |
| trace     |       |     | HIGH/LOW/NONE   |
| prove     |       |     | HIGH/LOW/NONE   |
| listen    |       |     | HIGH/LOW/NONE   |
| program   |       |     | HIGH/LOW/NONE   |
| topic     |       |     | HIGH/LOW/NONE   |

After Schema C, write the PROPOSAL SCOPE block:

  ================================================================
  PROPOSAL SCOPE
  HIGH-pressure namespaces (New > 0): [list names, or "none"]
  Excluded from proposals: [remaining namespaces]
  Rule: proposals may only cite evidence from HIGH-pressure namespaces.
  ================================================================

**Schema D -- Coverage map**
| Schema A label | Dimension | NEW signal finding | Assessment |
|----------------|-----------|--------------------|---------  |

**Schema E -- Additions**
| # | Dimension [NEW] | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before | After | vs. NO CHANGE -- MANDATORY |
|---|-----------------|-------------------|--------------------|------------------------------|--------|-------|---------------------------|

**Schema F -- Removals and Reprioritizations**
| # | Action | Dimension | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before | After | vs. NO CHANGE -- MANDATORY |
|---|--------|-----------|-------------------|--------------------|------------------------------|--------|-------|---------------------------|

**Schema G -- Before/after diff**
| Dimension | Schema A ref | Before | After | Proposal ref |
|-----------|-------------|--------|-------|--------------|

**Schema H -- Conflict audit**
| Conflict ID | Signal A | Signal B | Dimension | Nature |
|-------------|----------|----------|-----------|--------|

---

## Phase 0 -- Defense register

PRE-COMMIT BLOCK -- reproduce this before taking any action in Phase 0:

  ================================================================
  PHASE 0 PRE-COMMIT
  No artifact may be read -- not strategy.md, not any signal file
  in simulations/ -- until Schema DR is committed in writing and
  Gate 0 passes with STATUS: PASS.
  Reading strategy.md or any artifact before Gate 0 passes is a
  pre-commit violation that invalidates the defense register.
  The defense register must be committed before evidence is read,
  so that proposals must defeat a pre-committed argument rather
  than a post-hoc rationalization.
  ================================================================

To fill Schema DR, read strategy.md once. Do not read any signal artifacts.

Fill Schema DR: one row per dimension currently defended in strategy.md.
Each defense argument must be non-generic and trace to specific strategy.md
text. "No reason to change" and "no compelling reason" are not acceptable
defense arguments.

[Gate 0 -- reproduce with all three fields filled:
  GATE 0 | Phase: Pre-signal defense register
  Condition evaluated: [PRE-COMMIT BLOCK reproduced before Phase 0 action;
                        Schema DR filled with one row per strategy dimension;
                        each defense argument non-generic and traces to
                        strategy.md text]
  Result found: [D-R-N count; example defense argument with source reference]
  STATUS: PASS / STOP

  Do not advance to Phase 1 and do not read any signal artifact until this
  gate shows STATUS: PASS. A Gate 0 STATUS: STOP blocks all subsequent reads
  and all subsequent phases.]

---

## Phase 1 -- Strategy commitment and seal

Read strategy.md (authorized read; SEAL closes at Gate 1).

Fill Schema A, VERBATIM EVIDENCE BLOCK (Source dimension D-[N] -- [name]),
STRATEGY.MD SEALED block (6 fields, Boundary: "Schema A complete. No signal
artifacts examined yet.").

[Gate 1 -- reproduce with all three fields filled:
  GATE 1 | Phase: Strategy commitment
  Condition evaluated: [Schema A; VERBATIM BLOCK; SEALED block 6 fields]
  Result found: [Strategy date, D-N count, Source label, Boundary]
  STATUS: PASS / STOP]

Do not advance to Phase 2 until Gate 1 shows STATUS: PASS.

---

## Phase 2 -- Signal inventory

Fill Schema B and Schema C (all 9 rows; zero-counts; NEVER ABSENT).
Write PROPOSAL SCOPE block.

Write the mandatory delta count sentence:
"Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
N and M must be integers. Non-integer values are a gate failure.

If no artifacts: stop. If no HIGH-pressure namespaces: "STRATEGY CURRENT." Stop.

[Gate 2 -- reproduce with all three fields filled:
  GATE 2 | Phase: Signal inventory
  Condition evaluated: [9 rows; ABSENT not used; PROPOSAL SCOPE written;
                        delta sentence with integer counts]
  Result found: [pressures; SCOPE namespaces; delta sentence]
  STATUS: PASS / STOP]

Do not advance to Phase 3 until Gate 2 shows STATUS: PASS.

---

## Phase 3 -- Delta partition

Partition Schema B into NEW and PRIOR. PRIOR artifacts may not drive proposals.

[Gate 3 -- reproduce with all three fields filled:
  GATE 3 | Phase: Delta partition
  Condition evaluated: [NEW vs PRIOR confirmed]
  Result found: [filenames as NEW, or "none new"]
  STATUS: PASS / STOP]

If STATUS: STOP: "STRATEGY CURRENT." End here.
Do not advance to Phase 4 until Gate 3 shows STATUS: PASS.

---

## Phase 4 -- Read NEW artifacts

Read each NEW artifact. Write a paragraph (4-6 sentences). Name >= 2 filenames.

[Gate 4 -- reproduce with all three fields filled:
  GATE 4 | Phase: New artifact synthesis
  Condition evaluated: [paragraph written; two filenames cited]
  Result found: [filenames cited]
  STATUS: PASS / STOP]

Do not advance to Phase 5 until Gate 4 shows STATUS: PASS.

---

## Phase 5 -- Coverage map and proposals

PROPOSAL SCOPE active: [HIGH-pressure namespaces from PROPOSAL SCOPE].

Fill Schema D. Default verdict: NO CHANGE.

Fill Schemas E and F. For every proposal row:
- Evidence in Phase 3 NEW list AND in PROPOSAL SCOPE namespaces
- Schema A ref (D-N) matches locked dimension
- Defense defeated (Row D-R-N): specific D-R-N; no row number fails column
- Before from locked Schema A only
- vs. NO CHANGE (MANDATORY): specific consequence; check against BANNED OUTPUT
  FORMS before presenting; any match disqualifies the row

Null declarations (each type labeled separately):
  ADDITIONS: none -- [reason] | or [N] proposed
  REMOVALS: none -- [reason] | or [N] proposed
  REPRIORITIZATIONS: none -- [reason] | or [N] proposed

Fill Schema G. If Schema H is empty:
CONFLICT DETECTION -- NULL: [specific reason]

[Gate 5 -- reproduce with all three fields filled:
  GATE 5 | Phase: Proposals complete
  Condition evaluated: [null declarations; evidence in SCOPE; D-N locked;
                        Schema G; H or typed null]
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Do not advance to Phase 6 until Gate 5 shows STATUS: PASS.

---

## Phase 6 -- Confirmation gate

Display all schemas (Schema DR, VERBATIM BLOCK, SEALED block, PROPOSAL SCOPE).

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
to apply your version
---

[Gate 6 -- reproduce with all three fields filled:
  GATE 6 | Phase: Confirmation gate
  Condition evaluated: [PENDING CONFIRMATION with integer counts]
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Stop. Write nothing further until the user replies.

---

## Apply (triggered by YES or REVISED)

Write exactly the confirmed changes to strategy.md. Confirm:
"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-04: Combination C-24 + C-25 -- Cell-level check + null declaration scope

**Variation axis**: V-01 (cell-level banned-forms check instruction at every
vs. NO CHANGE column, targeting C-24) combined with V-02 (banned-forms scope
propagation into null declaration reason templates with inline check
instruction, targeting C-25). V-03 (Gate-0 PRE-COMMIT block, C-26) is excluded
to isolate the two output-format improvements from the role-sequence gate change.

**Hypothesis**: V-01 closes C-24 by placing a CELL-LEVEL CHECK block at the
schema boundary directing the model to check vs. NO CHANGE cells before writing.
V-02 closes C-25 by embedding the banned-forms check instruction inside the null
declaration templates at point of use. These two axes are structurally
independent -- C-24 targets proposal columns, C-25 targets null declaration
reason cells -- and combining them incurs no redundancy. V-04 should score C-24
PASS, C-25 PASS, C-26 FAIL (Gate 0 exists and is linked but no PRE-COMMIT BLOCK
explicitly blocking artifact reads before it fires).

```
You are running /topic:plan for the topic named in the user's message.

---

## VOCABULARY CONTRACT (standing reference)

Sentinel tokens:
  `??`  -- open obligation: unknown or not yet determined
  `--`  -- closed decision: deliberately absent or not applicable

Named violations:
  VIOLATION-1: leaving a cell blank when `??` would be correct
  VIOLATION-2: writing `??` for a confirmed zero
  VIOLATION-3: writing `--` in a required cell

## BANNED OUTPUT FORMS (standing reference)

Apply this list to every free-text cell before presenting.
Any match disqualifies the row or null declaration containing it.
This constraint applies to proposal columns AND null declaration reason cells.
Null declarations are not exempt.

vs. NO CHANGE and inertia cells:
  "no change needed"
  "clearly warranted"
  "no compelling reason"
  "not necessary at this time"
  "nothing to add"

Null declaration reason cells (explicitly in scope -- null declarations are NOT
exempt; any banned form in a null reason fails the declaration):
  "no new signals"
  "nothing to add"
  "no changes needed"
  "not applicable"

Delta count sentence:
  "a few"
  "several"
  "some"
  "multiple"
  "many"

---

## Pre-committed schemas (fill in order -- no schema may be skipped or replaced
## with prose)

**Schema DR -- Defense register** (Phase 0; LOCKED before any artifact read)

| D-R-N | Dimension name | Current defense argument (from strategy.md) |
|-------|---------------|----------------------------------------------|
| D-R-1 |               |                                              |
| D-R-2 |               |                                              |
| ...   |               |                                              |

Every "Defense defeated (Row D-R-N)" citation must name a specific D-R-N row.
A named defense without a row number does not satisfy that column.

**Schema A -- Strategy commitment** (Phase 1; SEALED at Gate 1)

| Field               | Value |
|---------------------|-------|
| Strategy file       |       |
| Strategy date       |       |
| Completion criteria |       |
| Scope               |       |

Dimensions:

| Label | Dimension name | What strategy.md says |
|-------|---------------|----------------------|
| D-1   |               |                      |
| D-2   |               |                      |
| ...   |               |                      |

VERBATIM EVIDENCE BLOCK:

  ===VERBATIM START===
  [paste exact text from strategy.md]
  ===VERBATIM END===
  Source dimension: D-[N] -- [dimension name]

  ================================================================
  STRATEGY.MD SEALED
  Sealed after: Phase 1
  Prohibition: strategy.md may not be re-opened until after user reply.
  Violation condition: Any "Before" value not in Schema A D-N rows is a SEAL
               violation and must be dropped.
  Prohibition lifts: After user reply.
  Schema A contains: [N] dimensions labeled D-1 through D-[N]
  Boundary: Schema A complete. No signal artifacts examined yet.
  ================================================================

**Schema B -- Signal inventory**
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|

**Schema C -- Namespace audit (all 9 rows required)**
Rules: all 9 rows; zero-counts for absent; NEVER write ABSENT
Change pressure: HIGH if New > 0 | LOW if Total > 0 and New = 0 | NONE if
Total = 0

| Namespace | Total | New | Change pressure |
|-----------|-------|-----|-----------------|
| scout     |       |     | HIGH/LOW/NONE   |
| draft     |       |     | HIGH/LOW/NONE   |
| review    |       |     | HIGH/LOW/NONE   |
| flow      |       |     | HIGH/LOW/NONE   |
| trace     |       |     | HIGH/LOW/NONE   |
| prove     |       |     | HIGH/LOW/NONE   |
| listen    |       |     | HIGH/LOW/NONE   |
| program   |       |     | HIGH/LOW/NONE   |
| topic     |       |     | HIGH/LOW/NONE   |

After Schema C, write the PROPOSAL SCOPE block:

  ================================================================
  PROPOSAL SCOPE
  HIGH-pressure namespaces (New > 0): [list names, or "none"]
  Excluded from proposals: [remaining namespaces]
  Rule: proposals may only cite evidence from HIGH-pressure namespaces.
  ================================================================

**Schema D -- Coverage map**
| Schema A label | Dimension | NEW signal finding | Assessment |
|----------------|-----------|--------------------|---------  |

(CELL-LEVEL CHECK: before writing each vs. NO CHANGE cell in Schema E or F,
check it against the BANNED OUTPUT FORMS list above. Any match disqualifies
the row. Do not present the cell before completing the check.)

**Schema E -- Additions**
| # | Dimension [NEW] | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before | After | vs. NO CHANGE -- MANDATORY |
|---|-----------------|-------------------|--------------------|------------------------------|--------|-------|---------------------------|

**Schema F -- Removals and Reprioritizations**
| # | Action | Dimension | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before | After | vs. NO CHANGE -- MANDATORY |
|---|--------|-----------|-------------------|--------------------|------------------------------|--------|-------|---------------------------|

**Schema G -- Before/after diff**
| Dimension | Schema A ref | Before | After | Proposal ref |
|-----------|-------------|--------|-------|--------------|

**Schema H -- Conflict audit**
| Conflict ID | Signal A | Signal B | Dimension | Nature |
|-------------|----------|----------|-----------|--------|

---

## Phase 0 -- Defense register

Read `simulations/TOPICS.md` to find strategy file. Read strategy.md.

Fill Schema DR: one row per dimension in strategy.md. Each defense argument
non-generic and tracing to strategy.md text. "No reason to change" and "no
compelling reason" are banned.

[Gate 0 -- reproduce with all three fields filled:
  GATE 0 | Phase: Defense register
  Condition evaluated: [Schema DR filled; arguments non-generic]
  Result found: [D-R-N count; example argument]
  STATUS: PASS / STOP]

Do not begin Phase 1 until Gate 0 shows STATUS: PASS.

---

## Phase 1 -- Strategy commitment and seal

Read strategy.md (last authorized read; SEAL closes at Gate 1).

Fill Schema A, VERBATIM EVIDENCE BLOCK (Source dimension D-[N] -- [name]),
STRATEGY.MD SEALED block (6 fields, Boundary both halves).

[Gate 1 -- reproduce with all three fields filled:
  GATE 1 | Phase: Strategy commitment
  Condition evaluated: [Schema A; VERBATIM BLOCK; SEALED block 6 fields]
  Result found: [Strategy date, D-N count, Source label, Boundary]
  STATUS: PASS / STOP]

Do not begin Phase 2 until Gate 1 shows STATUS: PASS.

---

## Phase 2 -- Signal inventory

Fill Schema B and Schema C (all 9 rows; zero-counts; NEVER ABSENT).
Write PROPOSAL SCOPE block.

Write mandatory delta count sentence:
"Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
Non-integer values are a gate failure.

If no artifacts: stop. If no HIGH-pressure namespaces: "STRATEGY CURRENT." Stop.

[Gate 2 -- reproduce with all three fields filled:
  GATE 2 | Phase: Signal inventory
  Condition evaluated: [9 rows; ABSENT not used; PROPOSAL SCOPE written;
                        delta sentence with integers]
  Result found: [pressures; SCOPE namespaces; delta sentence]
  STATUS: PASS / STOP]

Do not begin Phase 3 until Gate 2 shows STATUS: PASS.

---

## Phase 3 -- Delta partition

Partition Schema B into NEW and PRIOR. PRIOR artifacts may not drive proposals.

[Gate 3 -- reproduce with all three fields filled:
  GATE 3 | Phase: Delta partition
  Condition evaluated: [NEW vs PRIOR confirmed]
  Result found: [filenames as NEW, or "none new"]
  STATUS: PASS / STOP]

If STATUS: STOP: "STRATEGY CURRENT." End here.
Do not begin Phase 4 until Gate 3 shows STATUS: PASS.

---

## Phase 4 -- Read NEW artifacts

Read each NEW artifact. Write a paragraph (4-6 sentences). Name >= 2 filenames.

[Gate 4 -- reproduce with all three fields filled:
  GATE 4 | Phase: New artifact synthesis
  Condition evaluated: [paragraph written; two filenames cited]
  Result found: [filenames cited]
  STATUS: PASS / STOP]

Do not begin Phase 5 until Gate 4 shows STATUS: PASS.

---

## Phase 5 -- Coverage map and proposals

PROPOSAL SCOPE active: [HIGH-pressure namespaces from PROPOSAL SCOPE].

Fill Schema D. Default verdict: NO CHANGE.

Fill Schemas E and F. For every proposal row:
- Evidence in Phase 3 NEW list AND in PROPOSAL SCOPE namespaces
- Schema A ref (D-N) matches locked dimension
- Defense defeated (Row D-R-N): specific D-R-N; no row number fails column
- Before from locked Schema A only
- vs. NO CHANGE (MANDATORY): check this cell against the BANNED OUTPUT FORMS
  list before writing; any match disqualifies the row

Null declarations (each type labeled separately; the reason cell is subject to
the BANNED OUTPUT FORMS constraint; check the reason against the banned null
declaration forms list before writing; any match fails this declaration):

  ADDITIONS: none -- [specific reason; check against BANNED OUTPUT FORMS before
    writing; "no new signals", "nothing to add", "no changes needed", "not
    applicable" are banned; any match fails this declaration]
  | or [N] proposed

  REMOVALS: none -- [specific reason; check against BANNED OUTPUT FORMS before
    writing; "no new signals", "nothing to add", "no changes needed", "not
    applicable" are banned; any match fails this declaration]
  | or [N] proposed

  REPRIORITIZATIONS: none -- [specific reason; check against BANNED OUTPUT
    FORMS before writing; "no new signals", "nothing to add", "no changes
    needed", "not applicable" are banned; any match fails this declaration]
  | or [N] proposed

Fill Schema G. If Schema H is empty:
CONFLICT DETECTION -- NULL: [specific reason]

[Gate 5 -- reproduce with all three fields filled:
  GATE 5 | Phase: Proposals complete
  Condition evaluated: [null declarations with checked reasons; evidence in
                        SCOPE; D-N locked; vs. NO CHANGE cells checked;
                        Schema G; H or typed null]
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Do not begin Phase 6 until Gate 5 shows STATUS: PASS.

---

## Phase 6 -- Confirmation gate

Display all schemas (Schema DR, VERBATIM BLOCK, SEALED block, PROPOSAL SCOPE).

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
to apply your version
---

[Gate 6 -- reproduce with all three fields filled:
  GATE 6 | Phase: Confirmation gate
  Condition evaluated: [PENDING CONFIRMATION with integer counts]
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Stop. Write nothing further until the user replies.

---

## Apply (triggered by YES or REVISED)

Write exactly the confirmed changes to strategy.md. Confirm:
"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-05: Full combination C-24 + C-25 + C-26 -- All three R6 axes

**Variation axis**: All three single-axis variations combined -- cell-level
banned-forms check instruction at every vs. NO CHANGE column (V-01, targeting
C-24), banned-forms scope propagation into null declaration reason templates
with inline check instruction (V-02, targeting C-25), and Gate-0 PRE-COMMIT
block explicitly blocking all artifact reads until the defense register is
committed (V-03, targeting C-26).

**Hypothesis**: The three new v6 criteria address three structurally independent
failure modes: C-24 (point-of-production check, not just a defined list), C-25
(null declaration scope, closing the hedge-phrase escape hatch in reason cells),
C-26 (explicit read barrier at Phase 0, not just a phase-linked gate). V-03's
PRE-COMMIT BLOCK makes Gate 0 a read barrier before the defense register is
committed; V-01's column-level CELL-LEVEL CHECK block makes banned-forms
checking happen at fill time for proposal rows; V-02's inline template
instructions make banned-forms checking happen at fill time for null declaration
reasons. Combining all three makes the skill's three standing contracts fully
self-enforcing at their respective points of production rather than at
downstream gates.

```
You are running /topic:plan for the topic named in the user's message.

---

## VOCABULARY CONTRACT (standing reference -- applies throughout all phases)

Sentinel tokens:
  `??`  -- open obligation: value is unknown or not yet determined
  `--`  -- closed decision: value is deliberately absent or not applicable

Named violations:
  VIOLATION-1: leaving a cell blank when `??` would be correct
  VIOLATION-2: writing `??` for a confirmed zero (zero is the required form)
  VIOLATION-3: writing `--` in a required cell (only optional cells accept `--`)

## BANNED OUTPUT FORMS (standing reference -- applies to all free-text cells)

The following strings are banned. Before writing any free-text cell, check it
against this list. Any match disqualifies the row or null declaration. This
constraint applies to proposal columns AND null declaration reason cells; null
declarations are not exempt.

vs. NO CHANGE and inertia cells:
  "no change needed"
  "clearly warranted"
  "no compelling reason"
  "not necessary at this time"
  "nothing to add"

Null declaration reason cells (explicitly in scope; a banned form in a null
declaration reason fails the declaration, not only the row):
  "no new signals"
  "nothing to add"
  "no changes needed"
  "not applicable"

Delta count sentence:
  "a few"
  "several"
  "some"
  "multiple"
  "many"

---

## Pre-committed schemas (fill in order -- no schema may be skipped or replaced
## with prose)

**Schema DR -- Defense register** (Phase 0 only; LOCKED and SEALED before any
artifact read -- this table must be committed in writing before strategy.md or
any signal file is opened)

| D-R-N | Dimension name | Current defense argument (from strategy.md) |
|-------|---------------|----------------------------------------------|
| D-R-1 |               |                                              |
| D-R-2 |               |                                              |
| ...   |               |                                              |

Every "Defense defeated (Row D-R-N)" citation in Schemas E and F must name a
specific D-R-N row from this locked table. A named defense without a row number
does not satisfy that column.

**Schema A -- Strategy commitment** (Phase 1 only; SEALED at Gate 1)

| Field               | Value |
|---------------------|-------|
| Strategy file       |       |
| Strategy date       |       |
| Completion criteria |       |
| Scope               |       |

Dimensions (label D-1 through D-N in order of appearance in strategy.md):

| Label | Dimension name | What strategy.md says |
|-------|---------------|----------------------|
| D-1   |               |                      |
| D-2   |               |                      |
| ...   |               |                      |

VERBATIM EVIDENCE BLOCK:

  ===VERBATIM START===
  [paste exact text from strategy.md -- no paraphrase, no summary,
   no restatement; copy-paste the exact words as they appear in the file]
  ===VERBATIM END===
  Source dimension: D-[N] -- [dimension name]
  (D-N label must match a row in the Schema A dimensions table above.
   A Source dimension not matching a D-N label fails this block.)

  ================================================================
  STRATEGY.MD SEALED
  Sealed after: Phase 1 (Schema A and VERBATIM BLOCK complete)
  Prohibition: strategy.md may not be re-opened or re-read until
               after the user replies YES, NO, or REVISED.
  Violation condition: Any "Before" value written after this line
               that contains text not present in the Schema A D-N
               rows above is a SEAL violation and must be dropped.
  Prohibition lifts: After user reply to the confirmation gate.
  Schema A contains: [N] dimensions labeled D-1 through D-[N]
  Boundary: Schema A complete. No signal artifacts examined yet.
  ================================================================

Schema A is LOCKED and SEALED after Gate 1. All "Before" values in Schemas E
and F must trace to a D-N row in the locked Schema A. The D-N label in every
"Schema A ref (D-N)" column must match a row in the Schema A dimensions table;
a reader can independently cross-check it against the Source dimension in the
VERBATIM EVIDENCE BLOCK.

**Schema B -- Signal inventory**
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|

**Schema C -- Namespace audit (all 9 rows required)**
Rules:
- All 9 rows must appear. Absent namespaces: Total = 0, New = 0, pressure = NONE.
- Do not write ABSENT or skip any row. Zero-counts are the required form.
- Change pressure: HIGH if New > 0 | LOW if Total > 0 and New = 0 | NONE if
  Total = 0

| Namespace | Total | New | Change pressure |
|-----------|-------|-----|-----------------|
| scout     |       |     | HIGH/LOW/NONE   |
| draft     |       |     | HIGH/LOW/NONE   |
| review    |       |     | HIGH/LOW/NONE   |
| flow      |       |     | HIGH/LOW/NONE   |
| trace     |       |     | HIGH/LOW/NONE   |
| prove     |       |     | HIGH/LOW/NONE   |
| listen    |       |     | HIGH/LOW/NONE   |
| program   |       |     | HIGH/LOW/NONE   |
| topic     |       |     | HIGH/LOW/NONE   |

After Schema C, write the PROPOSAL SCOPE block:

  ================================================================
  PROPOSAL SCOPE
  HIGH-pressure namespaces (New > 0): [list names, or "none"]
  Excluded from proposals: [all remaining namespaces not listed above]
  Rule: Phase 5 proposals may only cite evidence from HIGH-pressure
        namespaces. A proposal row citing any excluded namespace is a
        SCOPE violation and must be dropped.
  ================================================================

**Schema D -- Coverage map**
| Schema A label | Dimension | NEW signal finding | Assessment |
|----------------|-----------|--------------------|---------  |

(CELL-LEVEL CHECK: before writing each vs. NO CHANGE cell in Schema E or F,
check it against the BANNED OUTPUT FORMS list above. Any match disqualifies
the row. Do not present the cell before completing the check.)

**Schema E -- Additions**
| # | Dimension [NEW] | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before (Schema A text) | After | vs. NO CHANGE -- MANDATORY |
|---|-----------------|-------------------|--------------------|------------------------------|------------------------|-------|---------------------------|

**Schema F -- Removals and Reprioritizations**
| # | Action | Dimension | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before (Schema A text) | After | vs. NO CHANGE -- MANDATORY |
|---|--------|-----------|-------------------|--------------------|------------------------------|------------------------|-------|---------------------------|

**Schema G -- Before/after diff**
| Dimension | Schema A ref | Before | After | Proposal ref |
|-----------|-------------|--------|-------|--------------|

**Schema H -- Conflict audit** (if empty, write typed null immediately below:
CONFLICT DETECTION -- NULL: [specific reason no conflicts were found])
| Conflict ID | Signal A | Signal B | Dimension | Nature |
|-------------|----------|----------|-----------|--------|

---

## Phase 0 -- Defense register

PRE-COMMIT BLOCK -- reproduce this before taking any action in Phase 0:

  ================================================================
  PHASE 0 PRE-COMMIT
  No artifact may be read -- not strategy.md, not any signal file
  in simulations/ -- until Schema DR is committed in writing and
  Gate 0 passes with STATUS: PASS.
  Reading strategy.md or any artifact before Gate 0 passes is a
  pre-commit violation that invalidates the defense register.
  The defense register must be committed before evidence is read,
  so that proposals must defeat a pre-committed argument rather
  than a post-hoc rationalization.
  ================================================================

To fill Schema DR, read strategy.md once. Do not read any signal artifacts.

Fill Schema DR: one row per dimension currently defended in strategy.md.
Each defense argument must be non-generic and trace to specific strategy.md
text. "No reason to change" and "no compelling reason" are not acceptable;
check each defense argument against the BANNED OUTPUT FORMS list before writing.

[Gate 0 -- reproduce with all three fields filled:
  GATE 0 | Phase: Pre-signal defense register
  Condition evaluated: [PRE-COMMIT BLOCK reproduced before Phase 0 action;
                        Schema DR filled with one row per strategy dimension;
                        each defense argument non-generic, traces to strategy.md
                        text, and passes the BANNED OUTPUT FORMS check]
  Result found: [D-R-N count; example defense argument with source reference]
  STATUS: PASS / STOP

  Do not advance to Phase 1 and do not read any signal artifact until this
  gate shows STATUS: PASS. A Gate 0 STATUS: STOP blocks all subsequent reads
  and all subsequent phases.]

---

## Phase 1 -- Strategy commitment and seal

Read strategy.md to fill Schema A (last authorized read; SEAL closes at Gate 1;
strategy.md may not be re-read until user replies after Phase 6).

Fill Schema A: all field rows, all D-N dimension rows, VERBATIM EVIDENCE BLOCK
(both delimiters intact, Source dimension in D-[N] -- [name] format matching a
Schema A row), and STRATEGY.MD SEALED block (all six fields -- Boundary field
must state both halves: "Schema A complete. No signal artifacts examined yet.").

All three artifacts must appear in the Phase 1 output before Gate 1.

[Gate 1 -- reproduce with all three fields filled:
  GATE 1 | Phase: Strategy commitment, verbatim block, and seal
  Condition evaluated: [Schema A filled; VERBATIM BLOCK delimiters + Source
                        dimension in D-N format matching Schema A row; SEALED
                        block 6 fields including Boundary: "Schema A complete.
                        No signal artifacts examined yet."]
  Result found: [Strategy date, D-N count, Source dimension D-N label, "SEAL +
                 Boundary confirmed"]
  STATUS: PASS / STOP]

Do not advance to Phase 2 until Gate 1 shows STATUS: PASS.

---

## Phase 2 -- Signal inventory and namespace audit

List every artifact in `simulations/` whose filename contains the topic slug.
Fill Schema B (all artifacts). Fill Schema C (all 9 rows -- zero-counts for
absent namespaces, NEVER write ABSENT).

Write the PROPOSAL SCOPE block immediately after Schema C.

NEW = artifact date strictly after Schema A Strategy date.
PRIOR = date on or before Schema A Strategy date.

Write the mandatory delta count sentence:
"Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
N and M must be integers. Writing "a few", "several", "some", or any non-integer
value is a gate failure, not a quality concern.

If no artifacts: "No signal artifacts found. Cannot run /topic:plan." Stop.
If no HIGH-pressure namespaces: "STRATEGY CURRENT." Stop.

[Gate 2 -- reproduce with all three fields filled:
  GATE 2 | Phase: Signal inventory and scope declaration
  Condition evaluated: [all 9 namespace rows with numeric counts and pressure
                        ratings; ABSENT not used; PROPOSAL SCOPE block written
                        with HIGH-pressure and excluded namespace lists; delta
                        count sentence present with integer N and M]
  Result found: [each namespace Total/New/pressure; PROPOSAL SCOPE namespaces;
                 delta sentence with exact counts]
  STATUS: PASS / STOP]

Do not advance to Phase 3 until Gate 2 shows STATUS: PASS.

---

## Phase 3 -- Delta partition

Partition Schema B:
  NEW (date > Strategy date): [filenames and dates]
  PRIOR (date <= Strategy date): [filenames and dates]

PRIOR artifacts may not drive proposals. The SEAL is in force.

[Gate 3 -- reproduce with all three fields filled:
  GATE 3 | Phase: Delta partition
  Condition evaluated: [count of NEW vs PRIOR artifacts confirmed]
  Result found: [specific filenames classified as NEW, or "none new"]
  STATUS: PASS / STOP]

If STATUS: STOP: "STRATEGY CURRENT." End here.
Do not advance to Phase 4 until Gate 3 shows STATUS: PASS.

---

## Phase 4 -- Read NEW artifacts

Read each NEW artifact. The SEAL is in force -- strategy.md may not be
re-opened.

Write a short paragraph (4-6 sentences) on collective findings.
Name at least two artifact filenames. Do not compare to Schema A yet.

[Gate 4 -- reproduce with all three fields filled:
  GATE 4 | Phase: New artifact synthesis
  Condition evaluated: [paragraph written; at least two filenames cited;
                        no Schema A comparison in this phase]
  Result found: [specific filenames cited]
  STATUS: PASS / STOP]

Do not advance to Phase 5 until Gate 4 shows STATUS: PASS.

---

## Phase 5 -- Coverage map and proposals

PROPOSAL SCOPE active: [reproduce HIGH-pressure namespaces from the PROPOSAL
SCOPE block above]. Only evidence from these namespaces may drive proposals.

Fill Schema D. For NEW artifact dimensions absent from Schema A, add a row
labeled "NEW DIMENSION".

Default verdict: NO CHANGE. Burden of proof is on change.

Fill Schemas E and F. For every proposal row:
- Evidence artifact must appear in Phase 3 NEW list AND belong to a namespace
  listed in the PROPOSAL SCOPE block; if not, drop the proposal (SCOPE
  violation)
- Schema A ref (D-N) must name a specific locked dimension; cross-check it
  against the VERBATIM Source dimension label in Phase 1
- Defense defeated (Row D-R-N): cite the specific D-R-N row from Schema DR
  that this proposal defeats; a named defense without a row number does not
  satisfy this column
- Before must reproduce Schema A D-N text from the locked Schema A; drop the
  proposal if Before cannot be filled from locked Schema A
- vs. NO CHANGE (MANDATORY): name a specific consequence of leaving strategy
  unchanged; check this cell against the BANNED OUTPUT FORMS list before
  writing; any match disqualifies the row

Null declarations (each type labeled separately; the reason cell is subject to
the BANNED OUTPUT FORMS constraint; null declarations are not exempt; check the
reason against the banned null declaration forms list before writing; any match
fails this declaration):

  ADDITIONS: none -- [specific reason explaining why no additions are
    warranted; check this reason against BANNED OUTPUT FORMS before writing;
    "no new signals", "nothing to add", "no changes needed", "not applicable"
    are banned; any match here fails this declaration]
  | or [N] proposed

  REMOVALS: none -- [specific reason explaining why no removals are warranted;
    check this reason against BANNED OUTPUT FORMS before writing; "no new
    signals", "nothing to add", "no changes needed", "not applicable" are
    banned; any match here fails this declaration]
  | or [N] proposed

  REPRIORITIZATIONS: none -- [specific reason explaining why no
    reprioritizations are warranted; check this reason against BANNED OUTPUT
    FORMS before writing; "no new signals", "nothing to add", "no changes
    needed", "not applicable" are banned; any match here fails this
    declaration]
  | or [N] proposed

Fill Schema G (before/after diff for every proposal row).

Fill Schema H (conflict audit). If Schema H is empty, write the typed null
immediately below: CONFLICT DETECTION -- NULL: [specific reason no conflicts
were found; check this reason against BANNED OUTPUT FORMS before writing].

[Gate 5 -- reproduce with all three fields filled:
  GATE 5 | Phase: Proposals complete
  Condition evaluated: [all three null declarations present with checked
                        reasons; all proposal evidence verified in PROPOSAL
                        SCOPE namespaces; each Schema A ref matches a locked
                        D-N label; all vs. NO CHANGE cells checked against
                        BANNED OUTPUT FORMS before presenting; Schema G row
                        count; Schema H or typed null present]
  Result found: [N additions / N removals / N reprioritizations; SCOPE
                 namespace count]
  STATUS: PASS / STOP]

Do not advance to Phase 6 until Gate 5 shows STATUS: PASS.

---

## Phase 6 -- Confirmation gate

Display all schemas (including Schema DR, VERBATIM EVIDENCE BLOCK, STRATEGY.MD
SEALED block, and PROPOSAL SCOPE block from prior phases).

Write exactly:

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
to apply your version
---

The SEAL remains in force until user reply.

[Gate 6 -- reproduce with all three fields filled:
  GATE 6 | Phase: Confirmation gate
  Condition evaluated: [PENDING CONFIRMATION block written with integer proposal
                        counts]
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Stop. Write nothing further until the user replies.

---

## Apply (triggered by YES or REVISED)

The SEAL lifts when the user replies. Write exactly the confirmed changes to
strategy.md. No additional edits. Confirm:
"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```
