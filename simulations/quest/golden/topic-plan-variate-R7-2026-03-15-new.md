# topic-plan Skill Variations — Round 7 (2026-03-15)

Rubric: v7 (C-01–C-27)
New criterion this round: C-27 (Write-surface enforcement completeness)

---

## Round 7 Design Notes

Round 6 surfaced three new criteria from excellence signals in R5 V-05:

- **C-24** — cell-level banned-forms check instruction at the point of production (not
  only a preamble-level list): before writing each free-text justification cell, an
  explicit instruction directs the model to check it against the BANNED FORMS list.
- **C-25** — banned-forms scope propagation to null declaration reason cells: the
  constraint must be explicitly stated as applying to null declarations, not only
  inferred from a global gate or preamble.
- **C-26** — Gate-0 pre-signal stop gate: the defense register (Phase 0) has its own
  numbered stop gate that explicitly blocks artifact reads until it passes.

R6 V-05 achieved all three individually. C-27 is the new criterion that tests whether
all three are *architecturally present together*: three distinct write surfaces, each
with a point-of-production enforcement block that fires before output.

The three write surfaces:

- **WS-1 (Gate 0)** — a read-barrier declaration before Phase 0 actions, naming Gate 0
  as the block; artifact reads cannot begin until Gate 0 passes.
- **WS-2 (Schema E/F boundary)** — a labeled block at the boundary between objective
  proposal columns and the free-text inertia column; fires before the model writes any
  cell in the "vs. NO CHANGE" column or null declaration reason.
- **WS-3 (null declaration templates)** — the null declaration template itself contains
  the banned-forms check instruction and verbatim-quoted banned strings inline; the
  check is part of the template, not a separate gate condition.

A variation can satisfy C-24, C-25, and C-26 individually while scattering the checks
across phases — one in a preamble, one in a gate condition, one in phase fill notes.
C-27 tests the *placement discipline*: each check fires at its write surface, making
violation impossible to produce through normal execution rather than detectable after
the fact.

| Variation | Primary axis | WS-1 mechanism | WS-2 mechanism | WS-3 mechanism |
|-----------|-------------|----------------|----------------|----------------|
| V-01 | Role sequence | PRE-COMMIT BLOCK before Phase 0; Gate 0 named in read-barrier | SCHEMA BOUNDARY BLOCK labeled header between Schema D and Schema E | Null templates contain inline `BANNED: [list]` + check instruction |
| V-02 | Output format | Three named WS-blocks as first-class headers; WS-1 GATE BLOCK precedes all phases | WS-2 BOUNDARY BLOCK is its own section header | WS-3 NULL BLOCK is embedded in each null declaration row |
| V-03 | Lifecycle emphasis | WRITE SURFACE REGISTER declared upfront naming all three sites; WS-1 fires first | Lifecycle annotates "WS-2 ACTIVE" at schema boundary | "WS-3 ACTIVE" header inside null declaration fill instruction |
| V-04 | Phrasing register + inertia framing | Short imperatives; each enforcement site has a "Why:" motivation; Gate 0 motivated as evidence independence | WHY-LABELED check block at schema boundary | Null template contains "Why:" + verbatim banned strings |
| V-05 | Combined (all axes + C-27 as skeleton) | WRITE-SURFACE ARCHITECTURE declared upfront; WS-1 is first structural primitive | LABELED BOUNDARY BLOCK anchored to architecture declaration | NULL DECLARATION TEMPLATE anchored to architecture; check is structural, not optional |

**Predicted discriminator:** C-27 will discriminate on whether the three checks form an
architecture or a checklist. A variation where WS-2 is a parenthetical in phase fill
instructions (not a labeled block at the schema boundary) and WS-3 is embedded in a
gate condition (not inside the template itself) satisfies C-24+C-25+C-26 individually
but misses C-27's architectural completeness requirement.

---

## V-01: Role Sequence — PRE-COMMIT BLOCK + SCHEMA BOUNDARY BLOCK + Inline Null Templates

**Variation axis**: Role sequence — the three write-surface enforcement sites are
ordered by the lifecycle: WS-1 fires first (PRE-COMMIT BLOCK declares the read-barrier
before any phase action), WS-2 fires at the Schema D/E boundary (a labeled SCHEMA
BOUNDARY BLOCK with its own header, not a parenthetical), WS-3 fires inside each null
declaration template. The sequencing makes each enforcement site the first action at
its write surface; no site relies on a downstream gate.

**Hypothesis**: Role sequencing enforces write-surface discipline by making each
enforcement event the *entry condition* for its write surface rather than a quality
check that could be skipped. The PRE-COMMIT BLOCK appears before Phase 0 actions begin,
establishing the read-barrier as an architectural commitment before strategy.md is even
touched. The SCHEMA BOUNDARY BLOCK (labeled header between Schema D and Schema E) makes
the cell-level check unavoidable — the schema header is the boundary, and crossing it
requires acknowledging the check. Inline null declaration templates make WS-3 inseparable
from the null form itself. C-27's architectural completeness is satisfied because each
write surface has a labeled enforcement block that fires at the surface, not elsewhere.

```
You are running /topic:plan for the topic named in the user's message.

---

## PRE-COMMIT BLOCK — Read barrier (WS-1)

READ-BARRIER ACTIVE: no signal artifacts may be read until Gate 0 passes.

Gate 0 governs Phase 0 (defense register). Phase 0 must complete and Gate 0 must show
STATUS: PASS before any file read other than strategy.md date extraction.

This block is the WS-1 enforcement site. It fires before Phase 0 actions begin.

---

## VOCABULARY CONTRACT (standing reference — applies throughout all phases)

Sentinel tokens:
  `??`  — open obligation: value unknown or not yet determined
  `--`  — closed decision: value deliberately absent or not applicable

Named violations:
  VIOLATION-1: leaving a cell blank when `??` would be correct
  VIOLATION-2: writing `??` for a confirmed zero (zero is the required form)
  VIOLATION-3: writing `--` in a required cell (only optional cells accept `--`)

---

## BANNED OUTPUT FORMS (standing reference — applies to all free-text cells)

All strings below are banned in every free-text justification cell.
Any match disqualifies the row or declaration containing it.

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

Delta count sentence banned forms:
  "a few"
  "several"
  "some"
  "multiple"
  "many"

---

## Pre-committed schemas (fill in order — no schema may be skipped or replaced with prose)

**Schema DR — Defense register** (Phase 0 only; LOCKED before any artifact read;
every row is a dimension currently defended by strategy.md)

| D-R-N | Dimension name | Current defense argument (from strategy.md) |
|-------|---------------|----------------------------------------------|
| D-R-1 |               |                                              |
| D-R-2 |               |                                              |
| ...   |               |                                              |

Every "Defense defeated (Row D-R-N)" citation in Schemas E and F must name a
specific D-R-N row from this table. A named defense without a row number does not
satisfy that column.

**Schema A — Strategy commitment** (Phase 1; SEALED at Gate 1)

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
  [paste exact text from strategy.md — no paraphrase, no summary, no restatement]
  ===VERBATIM END===
  Source dimension: D-[N] — [dimension name]
  (D-N label must match a row in the Schema A dimensions table above.)

  ================================================================
  STRATEGY.MD SEALED
  Sealed after: Phase 1 (Schema A and VERBATIM BLOCK complete)
  Prohibition: strategy.md may not be re-read until after user reply
  Violation condition: any "Before" value not in Schema A D-N rows is a
               SEAL violation and must be dropped
  Prohibition lifts: after user reply to confirmation gate
  Schema A contains: [N] dimensions labeled D-1 through D-[N]
  Boundary: Schema A complete. No signal artifacts examined yet.
  ================================================================

**Schema B — Signal inventory**
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|

**Schema C — Namespace audit (all 9 rows required)**
Rules: all 9 rows must appear; zero-counts for absent namespaces; NEVER write ABSENT
Change pressure: HIGH if New > 0 | LOW if Total > 0 and New = 0 | NONE if Total = 0

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
  Excluded from proposals: [all remaining namespaces]
  Rule: Phase 5 proposals may only cite evidence from HIGH-pressure namespaces.
        A proposal row citing any excluded namespace is a SCOPE violation and
        must be dropped.
  ================================================================

**Schema D — Coverage map**
| Schema A label | Dimension | NEW signal finding | Assessment |
|----------------|-----------|--------------------|-----------  |

---

### SCHEMA BOUNDARY BLOCK — WS-2 enforcement site

This block is the WS-2 enforcement site. It fires at the boundary between Schema D
(objective coverage analysis) and Schema E (free-text inertia cells).

CELL-LEVEL BANNED-FORMS CHECK — MANDATORY before writing Schema E or F:

Before writing any cell in the "vs. NO CHANGE — MANDATORY" column of Schema E or F:
1. Draft the cell text.
2. Check it against every string in the BANNED OUTPUT FORMS list above.
3. If any banned string appears: discard the draft. Rewrite naming a specific
   consequence. Repeat until no banned string matches.
4. Only then present the cell.

Writing the cell before completing steps 1–4 is a gate failure at Gate 5.

---

**Schema E — Additions**
| # | Dimension [NEW] | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before (Schema A text) | After | vs. NO CHANGE — MANDATORY |
|---|-----------------|-------------------|--------------------|------------------------------|------------------------|-------|--------------------------|

**Schema F — Removals and Reprioritizations**
| # | Action | Dimension | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before (Schema A text) | After | vs. NO CHANGE — MANDATORY |
|---|--------|-----------|-------------------|--------------------|------------------------------|------------------------|-------|--------------------------|

**Schema G — Before/after diff**
| Dimension | Schema A ref | Before | After | Proposal ref |
|-----------|-------------|--------|-------|--------------|

**Schema H — Conflict audit** (if empty, write typed null: CONFLICT DETECTION — NULL: [specific reason])
| Conflict ID | Signal A | Signal B | Dimension | Nature |
|-------------|----------|----------|-----------|--------|

---

## Phase 0 — Defense register

READ-BARRIER (WS-1) IS ACTIVE. No artifact reads until Gate 0 passes.

Read `simulations/TOPICS.md` to find the strategy file path. Read strategy.md once.

Fill Schema DR: one row per dimension currently defended in strategy.md. Each defense
argument must be non-generic and trace to specific strategy.md text. The following
defense arguments are banned from Schema DR:
  "no reason to change"
  "no compelling reason"
  "nothing to update"

[Gate 0 — reproduce with all three fields filled before advancing:
  GATE 0 | Phase: Defense register
  Condition evaluated: Schema DR filled; each argument non-generic and tracing to
                       strategy.md text; no banned defense arguments present
  Result found: [D-R-N count; example defense argument quoted from DR table]
  STATUS: PASS / STOP]

Do not advance to Phase 1 without passing Gate 0. READ-BARRIER remains active
until Gate 0 STATUS: PASS is written.

---

## Phase 1 — Strategy commitment and seal

Read strategy.md (last authorized read before SEAL). Fill Schema A, VERBATIM EVIDENCE
BLOCK (Source dimension D-[N] — [name]), and STRATEGY.MD SEALED block (all six fields,
Boundary field both halves).

[Gate 1 — reproduce with all three fields filled before advancing:
  GATE 1 | Phase: Strategy commitment
  Condition evaluated: Schema A filled; VERBATIM BLOCK delimiters present + Source
                       dimension in D-N format; SEALED block 6 fields with Boundary:
                       "Schema A complete. No signal artifacts examined yet."
  Result found: [strategy date; D-N count; Source dimension label; SEAL confirmed]
  STATUS: PASS / STOP]

Do not advance to Phase 2 without passing Gate 1.

---

## Phase 2 — Signal inventory

List every artifact in `simulations/` whose filename contains the topic slug.
Fill Schema B. Fill Schema C (all 9 rows; zero-counts; NEVER write ABSENT).
Write PROPOSAL SCOPE block after Schema C.

NEW = artifact date strictly after Schema A strategy date.
PRIOR = artifact date on or before Schema A strategy date.

Write the mandatory delta count sentence:
"Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
N and M must be integers. Writing "a few", "several", "some", "multiple", or
any non-integer value is a gate failure.

If no artifacts: "No signal artifacts found. Cannot run /topic:plan." Stop.
If no HIGH-pressure namespaces: "STRATEGY CURRENT — no new signals." Stop.

[Gate 2 — reproduce with all three fields filled before advancing:
  GATE 2 | Phase: Signal inventory and scope declaration
  Condition evaluated: 9 namespace rows present; ABSENT not used; PROPOSAL SCOPE
                       written; delta sentence with integer counts; integer check:
                       "a few/several/some/multiple/many" — none present
  Result found: [namespace pressures; HIGH namespaces; delta sentence]
  STATUS: PASS / STOP]

Do not advance to Phase 3 without passing Gate 2.

---

## Phase 3 — Delta partition

Partition Schema B artifacts into NEW and PRIOR sets. PRIOR artifacts reflect signals
already incorporated in strategy.md and may not drive proposals.

[Gate 3 — reproduce with all three fields filled before advancing:
  GATE 3 | Phase: Delta partition
  Condition evaluated: NEW vs PRIOR count confirmed; no PRIOR artifact classified NEW
  Result found: [NEW filenames listed; or "none new"]
  STATUS: PASS / STOP]

If STATUS: STOP: "STRATEGY CURRENT." End here.
Do not advance to Phase 4 without passing Gate 3.

---

## Phase 4 — Read NEW artifacts and synthesize

Read each NEW artifact from Phase 3. strategy.md remains sealed.

Write a short paragraph (4–6 sentences) describing what the NEW artifacts collectively
reveal. Name at least two artifact filenames by name in the text.

[Gate 4 — reproduce with all three fields filled before advancing:
  GATE 4 | Phase: New artifact synthesis
  Condition evaluated: synthesis paragraph written; at least two filenames named
  Result found: [filenames cited]
  STATUS: PASS / STOP]

Do not advance to Phase 5 without passing Gate 4.

---

## Phase 5 — Coverage map and proposals

PROPOSAL SCOPE active: [reproduce HIGH-pressure namespaces from PROPOSAL SCOPE].

Fill Schema D. Default verdict for every dimension: NO CHANGE. Burden of proof
is on any proposed change, not on the status quo.

Fill Schemas E and F. For every proposal row:
- Evidence: in Phase 3 NEW list AND in PROPOSAL SCOPE namespaces
- Schema A ref (D-N): matches locked dimension; cross-check against VERBATIM BLOCK
  Source dimension
- Defense defeated (Row D-R-N): cite specific D-R-N from Schema DR; a named defense
  without a row number does not satisfy this column
- Before: from locked Schema A only; drop proposal if Before cannot be filled from
  Schema A
- vs. NO CHANGE — MANDATORY: SCHEMA BOUNDARY BLOCK (WS-2) check applies; draft cell,
  check against BANNED OUTPUT FORMS, rewrite if any match, then present

Null declarations (WS-3 enforcement — each type labeled separately):

  ADDITIONS NULL DECLARATION:
  Template: ADD — NULL: [reason why no additions are warranted]
  WS-3 CHECK (fires inside this template before writing reason):
    Draft the reason. Check it against: "no new signals" / "nothing to add" /
    "no changes needed" / "not applicable". If any match: discard draft. Rewrite
    naming the specific condition that rules out additions. Repeat until clean.
  Write the null declaration only after the WS-3 check passes.

  REMOVALS NULL DECLARATION:
  Template: REMOVE — NULL: [reason why no removals are warranted]
  WS-3 CHECK (fires inside this template before writing reason):
    Draft the reason. Check it against: "no new signals" / "nothing to add" /
    "no changes needed" / "not applicable". If any match: discard draft. Rewrite
    naming the specific condition that rules out removals. Repeat until clean.
  Write the null declaration only after the WS-3 check passes.

  REPRIORITIZATIONS NULL DECLARATION:
  Template: REPRIORITIZE — NULL: [reason why no reprioritizations are warranted]
  WS-3 CHECK (fires inside this template before writing reason):
    Draft the reason. Check it against: "no new signals" / "nothing to add" /
    "no changes needed" / "not applicable". If any match: discard draft. Rewrite
    naming the specific condition that rules out reprioritizations. Repeat until clean.
  Write the null declaration only after the WS-3 check passes.

Fill Schema G. Fill Schema H (or write typed null: CONFLICT DETECTION — NULL: [reason]).

[Gate 5 — reproduce with all three fields filled before advancing:
  GATE 5 | Phase: Proposals complete
  Condition evaluated: null declarations all present with WS-3 checks documented;
                       evidence in SCOPE; D-N refs match Schema A; D-R-N refs match
                       Schema DR; vs. NO CHANGE cells checked against BANNED OUTPUT
                       FORMS (SCHEMA BOUNDARY BLOCK); Schema G count; Schema H or
                       typed null
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Do not advance to Phase 6 without passing Gate 5.

---

## Phase 6 — Confirmation gate

Display all schemas (Schema DR, VERBATIM BLOCK, SEALED block, PROPOSAL SCOPE,
Schemas D through H).

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
to apply your version
---

[Gate 6 — reproduce with all three fields filled before advancing:
  GATE 6 | Phase: Confirmation gate
  Condition evaluated: PENDING CONFIRMATION banner written with integer counts
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Stop. Write nothing further until the user replies.

---

## Apply (triggered by YES or REVISED)

The SEAL lifts. Write exactly the confirmed changes to strategy.md. No reformatting
of unchanged sections. Confirm:
"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-02: Output Format — Three WS-Blocks as First-Class Section Headers

**Variation axis**: Output format — the three write-surface enforcement sites are
formatted as first-class section headers (`###`) that appear in the skill structure
at the exact moment each write surface is reached. `WS-1 GATE BLOCK` appears before
Phase 0. `WS-2 BOUNDARY BLOCK` appears between Schema D and Schema E. `WS-3 NULL BLOCK`
appears inside each null declaration template row. The format makes each enforcement
site a named section visible in any outline view, not a paragraph embedded in phase
instructions.

**Hypothesis**: First-class section headers enforce C-27 through structural visibility:
any reader of the skill — human or model — can verify the three enforcement sites by
scanning headers. A parenthetical or inline note can be missed in execution; a section
header cannot be executed-past without generating output at that location. The `WS-3
NULL BLOCK` embedded inside each null declaration template makes C-25 scope propagation
architectural: the null template itself contains the enforcement block, so writing the
null without the check is structurally impossible. C-24 (cell-level check) and C-26
(Gate 0) are enforced by the same header-visibility property.

```
You are running /topic:plan for the topic named in the user's message.

Fill each section in order. Do not skip a section. Do not read ahead.

---

## VOCABULARY CONTRACT (standing reference)

Sentinel tokens:
  `??`  — open obligation: unknown or not yet determined
  `--`  — closed decision: deliberately absent or not applicable

Named violations:
  VIOLATION-1: leaving a cell blank when `??` would be correct
  VIOLATION-2: writing `??` for a confirmed zero
  VIOLATION-3: writing `--` in a required cell

---

## BANNED OUTPUT FORMS (standing reference)

Apply to all free-text cells before presenting. Match = disqualified.

vs. NO CHANGE / inertia cells:
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
  "a few"  "several"  "some"  "multiple"  "many"

---

## Pre-committed schemas

**Schema DR — Defense register** (Phase 0; LOCKED before artifact reads)
| D-R-N | Dimension name | Current defense argument (from strategy.md) |
|-------|---------------|----------------------------------------------|

Every "Defense defeated (Row D-R-N)" citation in Schema E/F must name a specific D-R-N.

**Schema A — Strategy commitment** (Phase 1; SEALED at Gate 1)
| Field | Value |
|-------|-------|
| Strategy file | |
| Strategy date | |
| Completion criteria | |
| Scope | |

Dimensions:
| Label | Dimension name | What strategy.md says |
|-------|---------------|----------------------|
| D-1   |               |                      |
| ...   |               |                      |

VERBATIM EVIDENCE BLOCK:
  ===VERBATIM START===
  [exact text from strategy.md — no paraphrase]
  ===VERBATIM END===
  Source dimension: D-[N] — [dimension name]

  ================================================================
  STRATEGY.MD SEALED
  Sealed after: Phase 1
  Prohibition: strategy.md may not be re-read until after user reply
  Violation condition: any "Before" value not in Schema A D-N rows is a SEAL violation
  Prohibition lifts: after user reply
  Schema A contains: [N] dimensions labeled D-1 through D-[N]
  Boundary: Schema A complete. No signal artifacts examined yet.
  ================================================================

**Schema B — Signal inventory**
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|

**Schema C — Namespace audit (all 9 rows required)**
Change pressure: HIGH if New > 0 | LOW if Total > 0 and New = 0 | NONE if Total = 0
| Namespace | Total | New | Change pressure |
|-----------|-------|-----|-----------------|
| scout | | | |
| draft | | | |
| review | | | |
| flow | | | |
| trace | | | |
| prove | | | |
| listen | | | |
| program | | | |
| topic | | | |

PROPOSAL SCOPE block (write after Schema C):
  ================================================================
  PROPOSAL SCOPE
  HIGH-pressure namespaces: [list or "none"]
  Excluded: [all others]
  Rule: proposals cite only HIGH-pressure evidence.
  ================================================================

**Schema D — Coverage map**
| Schema A label | Dimension | NEW signal finding | Assessment |
|----------------|-----------|--------------------|-----------  |

---

### WS-2 BOUNDARY BLOCK

This section is the WS-2 write-surface enforcement site.

CELL-LEVEL CHECK — required before writing any cell in the "vs. NO CHANGE — MANDATORY"
column of Schema E or Schema F:

  Step 1: Draft the cell text.
  Step 2: Compare against every string in BANNED OUTPUT FORMS (vs. NO CHANGE section).
  Step 3: Match found → discard draft, rewrite naming a specific consequence, repeat.
  Step 4: No match → present the cell.

This check fires at this boundary. It does not apply retrospectively at a gate condition.

---

**Schema E — Additions**
| # | Dimension [NEW] | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before | After | vs. NO CHANGE — MANDATORY |
|---|-----------------|-------------------|--------------------|------------------------------|--------|-------|--------------------------|

**Schema F — Removals and Reprioritizations**
| # | Action | Dimension | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before | After | vs. NO CHANGE — MANDATORY |
|---|--------|-----------|-------------------|--------------------|------------------------------|--------|-------|--------------------------|

**Schema G — Before/after diff**
| Dimension | Schema A ref | Before | After | Proposal ref |
|-----------|-------------|--------|-------|--------------|

**Schema H — Conflict audit** (empty → CONFLICT DETECTION — NULL: [specific reason])
| Conflict ID | Signal A | Signal B | Dimension | Nature |
|-------------|----------|----------|-----------|--------|

---

### WS-1 GATE BLOCK

This section is the WS-1 write-surface enforcement site.

READ-BARRIER: no signal artifacts may be read until Gate 0 passes.

Gate 0 governs Phase 0 (defense register). No file read — except for strategy.md date
extraction in this step — may occur until Gate 0 STATUS: PASS is written.

Proceed to Phase 0 now.

---

## Phase 0 — Defense register

Read `simulations/TOPICS.md`. Find strategy file path. Read strategy.md.

Fill Schema DR: one row per defended dimension. Each defense argument must:
(a) be non-generic — banned: "no compelling reason", "no reason to change", "nothing
    to update"
(b) trace to specific strategy.md text (quote or paraphrase the exact passage)

[Gate 0 — reproduce before advancing:
  GATE 0 | Phase: Defense register
  Condition evaluated: Schema DR rows filled; arguments non-generic; no banned
                       defense arguments; each argument traces to strategy.md
  Result found: [D-R-N count; one example argument quoted]
  STATUS: PASS / STOP]

Do not advance to Phase 1 without passing Gate 0.

---

## Phase 1 — Strategy commitment and seal

Read strategy.md (last authorized read). Fill Schema A, VERBATIM EVIDENCE BLOCK,
and STRATEGY.MD SEALED block (all six fields).

[Gate 1 — reproduce before advancing:
  GATE 1 | Phase: Strategy commitment
  Condition evaluated: Schema A filled; VERBATIM BLOCK with delimiters; Source
                       dimension in D-N format; SEALED block complete; Boundary field:
                       "Schema A complete. No signal artifacts examined yet."
  Result found: [strategy date; D-N count; SEAL confirmed]
  STATUS: PASS / STOP]

Do not advance to Phase 2 without passing Gate 1.

---

## Phase 2 — Signal inventory

List every artifact in `simulations/` matching the topic slug. Fill Schema B.
Fill Schema C (all 9 rows; zero-counts; NEVER write ABSENT). Write PROPOSAL SCOPE.

NEW = date strictly after Schema A strategy date.
PRIOR = date on or before Schema A strategy date.

Mandatory delta count sentence (integer counts required):
"Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
Writing "a few", "several", "some", "multiple", or "many" is a gate failure.

If no artifacts: "No signal artifacts found." Stop.
If no HIGH-pressure namespaces: "STRATEGY CURRENT." Stop.

[Gate 2 — reproduce before advancing:
  GATE 2 | Phase: Signal inventory
  Condition evaluated: 9 namespace rows; ABSENT not used; PROPOSAL SCOPE written;
                       delta sentence with integer N and M; no banned count forms
  Result found: [HIGH namespaces; delta sentence]
  STATUS: PASS / STOP]

Do not advance to Phase 3 without passing Gate 2.

---

## Phase 3 — Delta partition

Classify Schema B artifacts into NEW and PRIOR. PRIOR cannot drive proposals.

[Gate 3 — reproduce before advancing:
  GATE 3 | Phase: Delta partition
  Condition evaluated: classification complete; no PRIOR artifact labeled NEW
  Result found: [NEW filenames, or "none new"]
  STATUS: PASS / STOP]

If STATUS: STOP: "STRATEGY CURRENT." End.
Do not advance to Phase 4 without passing Gate 3.

---

## Phase 4 — New artifact synthesis

Read each NEW artifact. strategy.md sealed.

Write synthesis paragraph (4–6 sentences). Name at least two artifact filenames.

[Gate 4 — reproduce before advancing:
  GATE 4 | Phase: New artifact synthesis
  Condition evaluated: paragraph written; at least two filenames cited
  Result found: [filenames cited]
  STATUS: PASS / STOP]

Do not advance to Phase 5 without passing Gate 4.

---

## Phase 5 — Coverage map and proposals

PROPOSAL SCOPE active: [HIGH namespaces from PROPOSAL SCOPE].

Fill Schema D. Default: NO CHANGE. Burden of proof is on change.

Fill Schemas E and F (WS-2 BOUNDARY BLOCK check applies to every "vs. NO CHANGE" cell).

Null declarations:

--- WS-3 NULL BLOCK: ADD ---
Write: ADD — NULL: [reason]
Before writing [reason]: check it against BANNED OUTPUT FORMS null declaration section.
Banned: "no new signals" / "nothing to add" / "no changes needed" / "not applicable"
If any match: rewrite naming the specific condition that rules out additions.
---

--- WS-3 NULL BLOCK: REMOVE ---
Write: REMOVE — NULL: [reason]
Before writing [reason]: check it against BANNED OUTPUT FORMS null declaration section.
Banned: "no new signals" / "nothing to add" / "no changes needed" / "not applicable"
If any match: rewrite naming the specific condition that rules out removals.
---

--- WS-3 NULL BLOCK: REPRIORITIZE ---
Write: REPRIORITIZE — NULL: [reason]
Before writing [reason]: check it against BANNED OUTPUT FORMS null declaration section.
Banned: "no new signals" / "nothing to add" / "no changes needed" / "not applicable"
If any match: rewrite naming the specific condition that rules out reprioritizations.
---

Fill Schema G. Fill Schema H (or CONFLICT DETECTION — NULL: [reason]).

[Gate 5 — reproduce before advancing:
  GATE 5 | Phase: Proposals complete
  Condition evaluated: null declarations present (all three types, each with WS-3 check
                       documented); evidence in SCOPE; D-N and D-R-N refs match schemas;
                       vs. NO CHANGE cells checked at WS-2 BOUNDARY BLOCK; Schema G
                       count; Schema H or typed null
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Do not advance to Phase 6 without passing Gate 5.

---

## Phase 6 — Confirmation gate

Display all schemas.

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to discard | REVISED + edited table to apply your version
---

Stop. Do not write further until the user replies.

---

## Apply (triggered by YES or REVISED)

SEAL lifts. Write exactly the confirmed changes. No reformatting.
"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-03: Lifecycle Emphasis — WRITE SURFACE REGISTER + Milestone Annotations

**Variation axis**: Lifecycle emphasis — a WRITE SURFACE REGISTER is declared upfront
before all schemas, naming all three write surfaces as lifecycle milestones. Each
enforcement site is then annotated in the lifecycle with its milestone tag: `[WS-1 MILESTONE]`,
`[WS-2 MILESTONE]`, `[WS-3 MILESTONE]`. The register creates a contract that the
lifecycle then fulfills; any execution path that skips a milestone is verifiably
incomplete against the register.

**Hypothesis**: A declared register gives C-27's architectural completeness a verifiable
structure: the three write surfaces exist as named commitments before any phase runs,
and each milestone annotation in the lifecycle confirms the commitment is honored. The
register also makes the skill self-auditing — a reviewer can check the register against
the lifecycle milestones without reading all phase instructions. The milestone annotations
at each write surface prevent the checks from being absorbed into gate conditions or
preamble text: a WS-2 milestone that appears only inside a Gate 5 condition is not at
the write surface and does not fulfill the register commitment.

```
You are running /topic:plan for the topic named in the user's message.

---

## WRITE SURFACE REGISTER

This skill has three write-surface enforcement milestones. Each fires at its write
surface during execution. All three must be present for architectural completeness.

| ID   | Write surface | Location in lifecycle | Enforcement mechanism |
|------|---------------|-----------------------|-----------------------|
| WS-1 | Pre-signal barrier | Before Phase 0 actions | READ-BARRIER DECLARATION names Gate 0; no artifact read until Gate 0 passes |
| WS-2 | Proposal column fill | At Schema D/E boundary | CELL-LEVEL CHECK BLOCK fires before any "vs. NO CHANGE" cell is written |
| WS-3 | Null declaration reason | Inside each null template | WS-3 check instruction embedded in template; fires before [reason] is written |

Register commitment: all three milestones will appear in the lifecycle below,
tagged `[WS-N MILESTONE]`, at their respective write surfaces.

---

## VOCABULARY CONTRACT (standing reference)

Sentinel tokens:
  `??`  — open obligation: unknown or not yet determined
  `--`  — closed decision: deliberately absent or not applicable

Named violations:
  VIOLATION-1: blank cell where `??` is correct
  VIOLATION-2: `??` for a confirmed zero
  VIOLATION-3: `--` in a required cell

---

## BANNED OUTPUT FORMS (standing reference)

vs. NO CHANGE and inertia cells — banned strings:
  "no change needed"  /  "clearly warranted"  /  "no compelling reason"
  "not necessary at this time"  /  "nothing to add"

Null declaration reason cells — banned strings:
  "no new signals"  /  "nothing to add"  /  "no changes needed"  /  "not applicable"

Delta count sentence — banned forms:
  "a few"  /  "several"  /  "some"  /  "multiple"  /  "many"

---

## Pre-committed schemas

**Schema DR — Defense register** (Phase 0; LOCKED before artifact reads)
| D-R-N | Dimension name | Current defense argument (from strategy.md) |
|-------|---------------|----------------------------------------------|

Every "Defense defeated (Row D-R-N)" citation in Schema E/F must name a specific D-R-N.
A named defense without a row number does not satisfy the column.

**Schema A — Strategy commitment** (Phase 1; SEALED at Gate 1)
| Field | Value |
|-------|-------|
| Strategy file | |
| Strategy date | |
| Completion criteria | |
| Scope | |

Dimensions:
| Label | Dimension name | What strategy.md says |
|-------|---------------|----------------------|
| D-1   | | |
| ...   | | |

VERBATIM EVIDENCE BLOCK:
  ===VERBATIM START===
  [exact text from strategy.md]
  ===VERBATIM END===
  Source dimension: D-[N] — [dimension name]

  ================================================================
  STRATEGY.MD SEALED
  Sealed after: Phase 1
  Prohibition: no re-read of strategy.md until after user reply
  Violation condition: any "Before" value not in Schema A D-N rows is a SEAL violation
  Prohibition lifts: after user reply
  Schema A contains: [N] dimensions labeled D-1 through D-[N]
  Boundary: Schema A complete. No signal artifacts examined yet.
  ================================================================

**Schema B — Signal inventory**
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|

**Schema C — Namespace audit (all 9 rows required)**
Change pressure: HIGH if New > 0 | LOW if Total > 0 and New = 0 | NONE if Total = 0
| Namespace | Total | New | Change pressure |
|-----------|-------|-----|-----------------|
| scout | | | |
| draft | | | |
| review | | | |
| flow | | | |
| trace | | | |
| prove | | | |
| listen | | | |
| program | | | |
| topic | | | |

PROPOSAL SCOPE (write after Schema C):
  ================================================================
  PROPOSAL SCOPE
  HIGH-pressure namespaces: [list or "none"]
  Excluded: [all others]
  Rule: proposals cite only HIGH-pressure evidence.
  ================================================================

**Schema D — Coverage map**
| Schema A label | Dimension | NEW signal finding | Assessment |
|----------------|-----------|--------------------|-----------  |

---

[WS-2 MILESTONE] — CELL-LEVEL CHECK BLOCK

This milestone fulfills WRITE SURFACE REGISTER WS-2.

Before writing any cell in the "vs. NO CHANGE — MANDATORY" column in Schema E or F:
  (a) Draft the cell text.
  (b) Check each word against the BANNED OUTPUT FORMS vs. NO CHANGE section.
  (c) Any match → discard, rewrite naming a specific consequence, repeat.
  (d) No match → write the cell.

This check fires here, at the Schema D/E boundary. It does not apply retrospectively.

---

**Schema E — Additions**
| # | Dimension [NEW] | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before | After | vs. NO CHANGE — MANDATORY |
|---|-----------------|-------------------|--------------------|------------------------------|--------|-------|--------------------------|

**Schema F — Removals and Reprioritizations**
| # | Action | Dimension | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before | After | vs. NO CHANGE — MANDATORY |
|---|--------|-----------|-------------------|--------------------|------------------------------|--------|-------|--------------------------|

**Schema G — Before/after diff**
| Dimension | Schema A ref | Before | After | Proposal ref |
|-----------|-------------|--------|-------|--------------|

**Schema H — Conflict audit** (empty → CONFLICT DETECTION — NULL: [reason])
| Conflict ID | Signal A | Signal B | Dimension | Nature |
|-------------|----------|----------|-----------|--------|

---

## Phase 0 — Defense register

[WS-1 MILESTONE] — READ-BARRIER DECLARATION

This milestone fulfills WRITE SURFACE REGISTER WS-1.

READ-BARRIER ACTIVE: no signal artifact reads until Gate 0 STATUS: PASS.
Gate 0 governs this phase. No file except strategy.md (date only) may be read
until Gate 0 clears.

Read `simulations/TOPICS.md`. Locate strategy file. Read strategy.md.

Fill Schema DR: one row per defended dimension. Each defense argument must trace to
specific strategy.md text and must not use banned forms:
  "no compelling reason"  /  "no reason to change"  /  "nothing to update"

[Gate 0 — reproduce before advancing: do not advance to Phase 1 without Gate 0 PASS
  GATE 0 | Phase: Defense register
  Condition evaluated: Schema DR complete; each row non-generic; no banned arguments;
                       each traces to strategy.md text
  Result found: [D-R-N count; example argument]
  STATUS: PASS / STOP]

READ-BARRIER ACTIVE until Gate 0 STATUS: PASS is written above.

---

## Phase 1 — Strategy commitment and seal

Read strategy.md. Fill Schema A, VERBATIM EVIDENCE BLOCK, and STRATEGY.MD SEALED.

[Gate 1 — reproduce before advancing:
  GATE 1 | Phase: Strategy commitment
  Condition evaluated: Schema A; VERBATIM with delimiters; Source D-N; SEALED 6 fields;
                       Boundary: "Schema A complete. No signal artifacts examined yet."
  Result found: [strategy date; D-N count; SEAL confirmed]
  STATUS: PASS / STOP]

Do not advance to Phase 2 without Gate 1 PASS.

---

## Phase 2 — Signal inventory

List all artifacts in `simulations/` matching topic slug. Fill Schema B and Schema C
(all 9 rows; zero-counts; NEVER write ABSENT). Write PROPOSAL SCOPE.

NEW = date strictly after Schema A strategy date.
PRIOR = date on or before.

Mandatory delta count sentence:
"Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
N and M must be integers. "a few" / "several" / "some" / "multiple" / "many" = gate failure.

If no artifacts: "No signal artifacts found." Stop.
If no HIGH namespaces: "STRATEGY CURRENT." Stop.

[Gate 2 — reproduce before advancing:
  GATE 2 | Phase: Signal inventory
  Condition evaluated: 9 rows; zero-counts; PROPOSAL SCOPE; integer counts; no banned
                       count forms
  Result found: [HIGH namespaces; delta sentence]
  STATUS: PASS / STOP]

Do not advance to Phase 3 without Gate 2 PASS.

---

## Phase 3 — Delta partition

Classify Schema B into NEW and PRIOR. PRIOR cannot drive proposals.

[Gate 3 — reproduce before advancing:
  GATE 3 | Phase: Delta partition
  Condition evaluated: all artifacts classified; no PRIOR labeled NEW
  Result found: [NEW filenames, or "none new"]
  STATUS: PASS / STOP]

If STATUS: STOP: "STRATEGY CURRENT." End.
Do not advance to Phase 4 without Gate 3 PASS.

---

## Phase 4 — New artifact synthesis

Read NEW artifacts. strategy.md sealed.

Write synthesis paragraph (4–6 sentences) naming at least two artifact filenames.

[Gate 4 — reproduce before advancing:
  GATE 4 | Phase: Synthesis
  Condition evaluated: paragraph written; two filenames named
  Result found: [filenames]
  STATUS: PASS / STOP]

Do not advance to Phase 5 without Gate 4 PASS.

---

## Phase 5 — Coverage map and proposals

PROPOSAL SCOPE active: [HIGH namespaces].

Fill Schema D. Default verdict: NO CHANGE.

Fill Schemas E and F using WS-2 MILESTONE check for every "vs. NO CHANGE" cell.

Null declarations — write all three types using the WS-3 templates below:

[WS-3 MILESTONE] — NULL DECLARATION TEMPLATES

This milestone fulfills WRITE SURFACE REGISTER WS-3.

For each null declaration type, the check fires inside the template before [reason]
is written:

  ADD — NULL: [reason]
    WS-3 check before writing [reason]:
    Banned: "no new signals" / "nothing to add" / "no changes needed" / "not applicable"
    Match found → discard, rewrite naming the specific ruling-out condition.

  REMOVE — NULL: [reason]
    WS-3 check before writing [reason]:
    Banned: "no new signals" / "nothing to add" / "no changes needed" / "not applicable"
    Match found → discard, rewrite naming the specific ruling-out condition.

  REPRIORITIZE — NULL: [reason]
    WS-3 check before writing [reason]:
    Banned: "no new signals" / "nothing to add" / "no changes needed" / "not applicable"
    Match found → discard, rewrite naming the specific ruling-out condition.

Use these templates exactly. Write the null declaration only after the WS-3 check passes.

Fill Schema G. Fill Schema H (or CONFLICT DETECTION — NULL: [reason]).

[Gate 5 — reproduce before advancing:
  GATE 5 | Phase: Proposals
  Condition evaluated: all three null types present with WS-3 milestones documented;
                       evidence in SCOPE; D-N and D-R-N refs match schemas; vs. NO
                       CHANGE cells cleared WS-2 check; Schema G filled; Schema H
                       or typed null
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Do not advance to Phase 6 without Gate 5 PASS.

---

## Phase 6 — Confirmation gate

Display all schemas.

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to discard | REVISED + edited table to apply your version
---

Stop. Write nothing until user replies.

---

## Apply (triggered by YES or REVISED)

SEAL lifts. Write confirmed changes only.
"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-04: Phrasing Register + Inertia Framing — WHY-Motivated Enforcement with NO CHANGE First

**Variation axis**: Phrasing register + inertia framing — short imperative sentences
throughout; each enforcement site carries a WHY: motivation explaining why the check
exists at this surface rather than elsewhere; the skill opens with NO CHANGE as the
explicit default and frames each enforcement site as protecting the inertia judgment.
The WHY motivations make the checks self-explanatory: a model that understands why
each check exists applies the rule's spirit in edge cases.

**Hypothesis**: Motivation-grounded enforcement satisfies C-27 through a different
architectural channel than labeled blocks or register declarations. When a model
understands that WS-1 protects evidence independence (reading strategy first anchors
the frame), WS-2 protects inertia integrity (the vs. NO CHANGE cell is where the
burden-of-proof claim is made), and WS-3 protects null declaration quality (null
reasons must be as rigorous as proposal reasons), the checks become self-reinforcing
rather than rules to obey. The WHY: motivation also makes each write surface distinct
in intent — a check for WS-2 cannot substitute for WS-3 and vice versa — which is
what C-27's "fires at its respective write surface" requirement needs.

```
The default outcome is NO CHANGE to strategy.md.
New signals must beat the null hypothesis — leaving strategy.md unchanged — before
any change is proposed. Every enforcement mechanism in this skill protects that default.

You are running /topic:plan for the topic named in the user's message.

---

## VOCABULARY CONTRACT

`??` — open obligation (unknown, not yet filled)
`--` — closed decision (deliberately absent, not applicable)

Violations:
  VIOLATION-1: blank cell when `??` is correct
  VIOLATION-2: `??` for a confirmed zero
  VIOLATION-3: `--` in a required cell

---

## BANNED OUTPUT FORMS

These strings are banned in all free-text cells. Match = disqualified.

vs. NO CHANGE / inertia:
  "no change needed"  "clearly warranted"  "no compelling reason"
  "not necessary at this time"  "nothing to add"

Null declaration reasons:
  "no new signals"  "nothing to add"  "no changes needed"  "not applicable"

Delta count:
  "a few"  "several"  "some"  "multiple"  "many"

---

## Pre-committed schemas

**Schema DR — Defense register**
WHY: The defense register commits to defending the status quo before any signals are
read. Signals can then only change a row they specifically defeat — not reframe
dimensions that were never challenged.

| D-R-N | Dimension name | Current defense argument (from strategy.md) |
|-------|---------------|----------------------------------------------|
| D-R-1 | | |
| ...   | | |

Banned defense arguments: "no compelling reason" / "no reason to change" / "nothing to update"
Each defense must trace to specific strategy.md text.

**Schema A — Strategy commitment** (SEALED at Gate 1)
| Field | Value |
|-------|-------|
| Strategy file | |
| Strategy date | |
| Completion criteria | |
| Scope | |

Dimensions:
| Label | Dimension name | What strategy.md says |
|-------|---------------|----------------------|
| D-1 | | |
| ... | | |

VERBATIM EVIDENCE BLOCK:
  ===VERBATIM START===
  [exact strategy.md text]
  ===VERBATIM END===
  Source dimension: D-[N] — [name]

  ================================================================
  STRATEGY.MD SEALED
  Sealed after: Phase 1
  Prohibition: no re-read until after user reply
  Violation: any "Before" value not in Schema A D-N rows is a SEAL violation
  Lifts: after user reply
  Schema A contains: [N] dimensions D-1 through D-[N]
  Boundary: Schema A complete. No signal artifacts examined yet.
  ================================================================

**Schema B — Signal inventory**
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|

**Schema C — Namespace audit (all 9 rows)**
Rule: zero-counts for absent namespaces. Never write ABSENT.
Change pressure: HIGH if New > 0 | LOW if Total > 0 and New = 0 | NONE if Total = 0
| Namespace | Total | New | Change pressure |
|-----------|-------|-----|-----------------|
| scout | | | |
| draft | | | |
| review | | | |
| flow | | | |
| trace | | | |
| prove | | | |
| listen | | | |
| program | | | |
| topic | | | |

PROPOSAL SCOPE (after Schema C):
  ================================================================
  PROPOSAL SCOPE
  HIGH namespaces: [list or "none"]
  Excluded: [rest]
  Rule: proposals cite only HIGH-pressure evidence.
  ================================================================

**Schema D — Coverage map**
| Schema A label | Dimension | NEW signal finding | Assessment |
|----------------|-----------|--------------------|-----------  |

**Schema D/E BOUNDARY — CELL-LEVEL CHECK (WS-2)**
WHY: The "vs. NO CHANGE" column is where the claim "this beats doing nothing" is made.
That claim must be specific and testable. Hedge phrases make the claim unverifiable and
smuggle in conclusions without evidence. This check fires here — at the boundary where
the claim cell is about to be written — so no hedge phrase can reach the output.

Before writing any "vs. NO CHANGE — MANDATORY" cell in Schema E or F:
  1. Draft the cell text.
  2. Check against BANNED OUTPUT FORMS vs. NO CHANGE section.
  3. Match → discard, rewrite with a specific consequence, repeat.
  4. No match → write the cell.

**Schema E — Additions**
| # | Dimension [NEW] | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before | After | vs. NO CHANGE — MANDATORY |
|---|-----------------|-------------------|--------------------|------------------------------|--------|-------|--------------------------|

**Schema F — Removals and Reprioritizations**
| # | Action | Dimension | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before | After | vs. NO CHANGE — MANDATORY |
|---|--------|-----------|-------------------|--------------------|------------------------------|--------|-------|--------------------------|

**Schema G — Before/after diff**
| Dimension | Schema A ref | Before | After | Proposal ref |
|-----------|-------------|--------|-------|--------------|

**Schema H — Conflict audit** (empty → CONFLICT DETECTION — NULL: [reason])
| Conflict ID | Signal A | Signal B | Dimension | Nature |
|-------------|----------|----------|-----------|--------|

---

## Phase 0 — Defense register

WS-1 ENFORCEMENT — PRE-SIGNAL READ-BARRIER:
WHY: Reading signal artifacts before committing to a defense register allows the
signals to frame which dimensions are "worth defending." The read-barrier forces the
model to name what it is defending before it can be influenced by what the signals say.
NO signal artifact may be read until Gate 0 passes.

Read `simulations/TOPICS.md`. Read strategy.md. Fill Schema DR.

[Gate 0 — reproduce before advancing:
  GATE 0 | Phase: Defense register
  Condition evaluated: Schema DR rows filled; arguments non-generic; none use banned
                       forms; each traces to strategy.md text
  Result found: [D-R-N count; example]
  STATUS: PASS / STOP]

Gate 0 must show STATUS: PASS before Phase 1 begins. No artifact reads until then.

---

## Phase 1 — Strategy commitment and seal

Read strategy.md (last read before SEAL). Fill Schema A, VERBATIM BLOCK, SEALED block.

[Gate 1 — reproduce before advancing:
  GATE 1 | Phase: Strategy commitment
  Condition evaluated: Schema A; VERBATIM with delimiters; D-N Source dimension;
                       SEALED 6 fields; Boundary field both halves
  Result found: [date; D-N count; SEAL]
  STATUS: PASS / STOP]

Do not advance to Phase 2 without Gate 1 PASS.

---

## Phase 2 — Signal inventory

List all artifacts in `simulations/` matching topic slug. Fill Schema B and C.
Write PROPOSAL SCOPE.

NEW = date strictly after Schema A strategy date. PRIOR = on or before.

Mandatory delta count sentence:
"Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
N and M must be integers. "a few" / "several" / "some" / "multiple" / "many" = failure.

No artifacts: "No signal artifacts found." Stop.
No HIGH namespaces: "STRATEGY CURRENT." Stop.

[Gate 2 — reproduce before advancing:
  GATE 2 | Phase: Signal inventory
  Condition evaluated: 9 rows; no ABSENT; PROPOSAL SCOPE; integer delta counts; no
                       banned count forms
  Result found: [HIGH namespaces; delta sentence]
  STATUS: PASS / STOP]

Do not advance to Phase 3 without Gate 2 PASS.

---

## Phase 3 — Delta partition

Classify Schema B into NEW and PRIOR. PRIOR cannot drive proposals.

[Gate 3 — reproduce before advancing:
  GATE 3 | Phase: Delta partition
  Condition evaluated: all classified; no PRIOR labeled NEW
  Result found: [NEW filenames or "none new"]
  STATUS: PASS / STOP]

STATUS: STOP → "STRATEGY CURRENT." End.
Do not advance to Phase 4 without Gate 3 PASS.

---

## Phase 4 — New artifact synthesis

Read each NEW artifact. strategy.md sealed.
Write 4–6 sentence synthesis paragraph. Name at least two artifact filenames.

[Gate 4 — reproduce before advancing:
  GATE 4 | Phase: Synthesis
  Condition evaluated: paragraph written; two filenames named
  Result found: [filenames]
  STATUS: PASS / STOP]

Do not advance to Phase 5 without Gate 4 PASS.

---

## Phase 5 — Coverage map and proposals

PROPOSAL SCOPE active: [HIGH namespaces].

Fill Schema D. Default: NO CHANGE. Proposals beat the null or don't exist.

Fill Schemas E and F. Schema D/E BOUNDARY CHECK (WS-2) applies to every
"vs. NO CHANGE" cell.

Null declarations — write all three using templates below:

ADD — NULL: [reason]
WS-3 ENFORCEMENT:
WHY: A null declaration reason must justify why NO CHANGE wins for this type. Hedge
phrases defer that judgment rather than making it. The check fires inside this template
so the same rigor applied to proposal rows applies to null rows.
Before writing [reason]: check against null-section BANNED OUTPUT FORMS.
Banned: "no new signals" / "nothing to add" / "no changes needed" / "not applicable"
Match → discard, rewrite naming the ruling-out condition, repeat.

REMOVE — NULL: [reason]
WS-3 ENFORCEMENT:
WHY: [same motivation as ADD]
Before writing [reason]: check against null-section BANNED OUTPUT FORMS.
Banned: "no new signals" / "nothing to add" / "no changes needed" / "not applicable"
Match → discard, rewrite naming the ruling-out condition, repeat.

REPRIORITIZE — NULL: [reason]
WS-3 ENFORCEMENT:
WHY: [same motivation as ADD]
Before writing [reason]: check against null-section BANNED OUTPUT FORMS.
Banned: "no new signals" / "nothing to add" / "no changes needed" / "not applicable"
Match → discard, rewrite naming the ruling-out condition, repeat.

Fill Schema G. Fill Schema H (or CONFLICT DETECTION — NULL: [reason]).

[Gate 5 — reproduce before advancing:
  GATE 5 | Phase: Proposals
  Condition evaluated: three null declarations with WS-3 enforcement documented;
                       evidence in SCOPE; D-N and D-R-N refs valid; vs. NO CHANGE
                       cells cleared WS-2 check; Schema G; Schema H or typed null
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Do not advance to Phase 6 without Gate 5 PASS.

---

## Phase 6 — Confirmation gate

Display all schemas.

Write exactly:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

NO CHANGE is the default. A reply of NO keeps strategy.md unchanged.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to discard | REVISED + edited table
---

Stop. Nothing further until user replies.

---

## Apply (triggered by YES or REVISED)

SEAL lifts. Write only confirmed changes.
"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-05: Combined — WRITE-SURFACE ARCHITECTURE as Structural Skeleton

**Variation axis**: Combined — the WRITE-SURFACE ARCHITECTURE is declared as a named
structural block before any schema or phase, establishing all three enforcement sites
as first-class primitives. Each subsequent enforcement site in the lifecycle anchors
itself to the architecture declaration with an explicit reference: "WS-1 enforcement
per ARCHITECTURE" / "WS-2 enforcement per ARCHITECTURE" / "WS-3 enforcement per
ARCHITECTURE." This makes the architecture self-verifying: any execution path where
an enforcement site does not reference the architecture is incomplete by definition.

**Hypothesis**: Declaring the architecture before any phase runs makes C-27 the
*governing contract* rather than a checklist item. The three write surfaces are named
in the architecture before strategy.md is read, before any schema is filled, before
any phase runs — establishing them as mandatory structural commitments. When each
enforcement site anchors to the architecture, a model executing the skill cannot skip
a write surface without breaking a named, declared contract visible from the first block.
The evacuated synthesis zone property (C-24 analog) applies to the architecture block
itself: the block declares primitives but does not instantiate them — instantiation
happens at each lifecycle site. All prior skeleton elements (vocabulary contract,
PROPOSAL SCOPE, sequential gate chain, two-tier sentinel, verbatim-quoted banned forms,
defense register with row-number anchoring) are present as the inherited skeleton.
The three new WS primitives extend the skeleton without replacing any prior element.

```
You are running /topic:plan for the topic named in the user's message.

---

## WRITE-SURFACE ARCHITECTURE

This block is the governing contract for this skill. It declares three write-surface
enforcement primitives. All three must fire at their respective write surfaces. Having
any two of three does not satisfy the architecture.

WSA-1 — PRE-SIGNAL READ BARRIER (governs: entry to Phase 0 actions)
  Mechanism: a read-barrier declaration fires before Phase 0 begins. Gate 0 is named
    as the barrier. No signal artifact may be read until Gate 0 STATUS: PASS.
  Implementation site: immediately before Phase 0 instructions begin.
  Condition: Gate 0 written and passing before any artifact read.

WSA-2 — SCHEMA BOUNDARY CHECK (governs: Schema E/F free-text column fill)
  Mechanism: a labeled CELL-LEVEL CHECK BLOCK fires at the Schema D/E boundary.
    Before writing any "vs. NO CHANGE — MANDATORY" cell, the model drafts, checks
    against BANNED OUTPUT FORMS, and rewrites if any match. No cell is presented
    before the check completes.
  Implementation site: labeled block at the boundary between Schema D and Schema E.
  Condition: block present and labeled; check instruction explicit and pre-fill.

WSA-3 — NULL DECLARATION TEMPLATE CHECK (governs: null declaration reason cells)
  Mechanism: each null declaration template contains an inline banned-forms check
    instruction and verbatim-quoted banned strings. The check fires inside the
    template before [reason] is written. Null declarations are not exempt from
    banned-forms enforcement.
  Implementation site: inside each ADD / REMOVE / REPRIORITIZE null template.
  Condition: check instruction and banned strings appear inside all three templates.

Architectural completeness requires WSA-1, WSA-2, and WSA-3 to all be present and
fire at their implementation sites. This architecture is declared here, before any
phase runs, so every subsequent enforcement site is verifiable against this block.

---

## VOCABULARY CONTRACT (standing reference)

Two-tier sentinel vocabulary:
  `??`  — open obligation: value is unknown or not yet determined (to be filled)
  `--`  — closed decision: value is deliberately absent or not applicable

Named violations:
  VIOLATION-1: leaving a cell blank when `??` would be correct
  VIOLATION-2: writing `??` for a confirmed zero (write 0, not `??`)
  VIOLATION-3: writing `--` in a required cell (only optional cells accept `--`)
  VIOLATION-4: leaving a D-R-N citation cell blank (write `??` if unknown; `--` is
               not acceptable for a required citation)

---

## BANNED OUTPUT FORMS (standing reference)

The following strings are banned in all free-text justification cells.
Any match disqualifies the row or declaration containing it.
Check cells before presenting — not after.

vs. NO CHANGE / inertia cells — banned verbatim:
  "no change needed"
  "clearly warranted"
  "no compelling reason"
  "not necessary at this time"
  "nothing to add"

Null declaration reason cells — banned verbatim:
  "no new signals"
  "nothing to add"
  "no changes needed"
  "not applicable"

Delta count sentence — banned verbatim:
  "a few"
  "several"
  "some"
  "multiple"
  "many"

Writing any banned form in its cell — even if the surrounding text is substantive —
disqualifies the cell. Paraphrase does not satisfy this constraint; the banned strings
are exact-match patterns.

---

## Pre-committed schemas (fill in order — no schema may be skipped or replaced with prose)

**Schema DR — Defense register**
(Phase 0 only; LOCKED before any artifact read; WSA-1 governs the barrier before this
schema is built; every row is a dimension currently defended by strategy.md)

| D-R-N | Dimension name | Current defense argument (from strategy.md) |
|-------|---------------|----------------------------------------------|
| D-R-1 |               |                                              |
| D-R-2 |               |                                              |
| ...   |               |                                              |

Defense argument requirements:
- Each argument must be non-generic and trace to specific strategy.md text.
- Banned defense arguments: "no compelling reason" / "no reason to change" /
  "nothing to update" — these are hedge phrases and disqualify the row.
- Every "Defense defeated (Row D-R-N)" citation in Schemas E and F must name a
  specific D-R-N row. A named defense without a row number does not satisfy the column.

**Schema A — Strategy commitment** (Phase 1; SEALED at Gate 1)

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
  [exact text from strategy.md — copy-paste; no paraphrase, no summary]
  ===VERBATIM END===
  Source dimension: D-[N] — [dimension name]
  (D-N label must match a row in Schema A dimensions. Non-matching label = block failure.)

  ================================================================
  STRATEGY.MD SEALED
  Sealed after: Phase 1 (Schema A and VERBATIM BLOCK complete)
  Prohibition: strategy.md may not be re-opened or re-read until after user reply
  Violation condition: any "Before" value written after this line that is not present
               in Schema A D-N rows above is a SEAL violation and must be dropped
  Prohibition lifts: after user reply to confirmation gate
  Schema A contains: [N] dimensions labeled D-1 through D-[N]
  Boundary: Schema A complete. No signal artifacts examined yet.
  ================================================================

**Schema B — Signal inventory**
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|

**Schema C — Namespace audit (all 9 rows required)**
Rules: all 9 rows must appear; zero-counts for absent namespaces; NEVER write ABSENT
Change pressure: HIGH if New > 0 | LOW if Total > 0 and New = 0 | NONE if Total = 0

| Namespace | Total | New | Change pressure |
|-----------|-------|-----|-----------------|
| scout     |       |     |                 |
| draft     |       |     |                 |
| review    |       |     |                 |
| flow      |       |     |                 |
| trace     |       |     |                 |
| prove     |       |     |                 |
| listen    |       |     |                 |
| program   |       |     |                 |
| topic     |       |     |                 |

PROPOSAL SCOPE (write after Schema C):
  ================================================================
  PROPOSAL SCOPE
  HIGH-pressure namespaces (New > 0): [list or "none"]
  Excluded from proposals: [all remaining namespaces]
  Rule: Phase 5 proposals may only cite evidence from HIGH-pressure namespaces.
        A proposal row citing an excluded namespace is a SCOPE violation; drop the row.
  ================================================================

**Schema D — Coverage map**
| Schema A label | Dimension | NEW signal finding | Assessment |
|----------------|-----------|--------------------|-----------  |

---

[WSA-2 ENFORCEMENT — WRITE-SURFACE ARCHITECTURE, per ARCHITECTURE block above]

CELL-LEVEL CHECK BLOCK — fires at Schema D/E boundary (before Schema E is filled)

This block is the WSA-2 write surface. It fires here. A check that appears only at
Gate 5 or in preamble text does not satisfy WSA-2 — this block at this location is
the required implementation site.

Before writing any cell in the "vs. NO CHANGE — MANDATORY" column of Schema E or F:
  Step 1 — Draft the cell text.
  Step 2 — Check draft against BANNED OUTPUT FORMS vs. NO CHANGE / inertia section.
            Banned: "no change needed" / "clearly warranted" / "no compelling reason" /
            "not necessary at this time" / "nothing to add"
  Step 3 — Any match found: discard draft. Rewrite naming a specific consequence if
            left unchanged. Repeat Steps 1–3.
  Step 4 — No match: present the cell.

Do not write Schema E or F rows before completing this block.

---

**Schema E — Additions**
| # | Dimension [NEW] | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before (Schema A text) | After | vs. NO CHANGE — MANDATORY |
|---|-----------------|-------------------|--------------------|------------------------------|------------------------|-------|--------------------------|

**Schema F — Removals and Reprioritizations**
| # | Action | Dimension | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before (Schema A text) | After | vs. NO CHANGE — MANDATORY |
|---|--------|-----------|-------------------|--------------------|------------------------------|------------------------|-------|--------------------------|

**Schema G — Before/after diff**
| Dimension | Schema A ref | Before | After | Proposal ref |
|-----------|-------------|--------|-------|--------------|

**Schema H — Conflict audit** (empty → CONFLICT DETECTION — NULL: [specific reason])
| Conflict ID | Signal A | Signal B | Dimension | Nature |
|-------------|----------|----------|-----------|--------|

---

## Phase 0 — Defense register

[WSA-1 ENFORCEMENT — WRITE-SURFACE ARCHITECTURE, per ARCHITECTURE block above]

PRE-SIGNAL READ BARRIER: no signal artifact reads until Gate 0 STATUS: PASS.

This is the WSA-1 write surface. Gate 0 is the named barrier. No file except
strategy.md (read in this phase for the defense register) may be opened until
Gate 0 passes. Any artifact read before Gate 0 STATUS: PASS violates WSA-1.

Read `simulations/TOPICS.md` to locate the strategy file. Read strategy.md once.

Fill Schema DR: one row per dimension currently defended in strategy.md.
Every argument must trace to specific strategy.md text. Banned forms above apply.

[Gate 0 — reproduce with all three fields filled before advancing — do not advance
to Phase 1 without Gate 0 STATUS: PASS:
  GATE 0 | Phase: Defense register | WSA-1 barrier
  Condition evaluated: Schema DR complete; all arguments non-generic; no banned
                       defense arguments; each argument traces to strategy.md text
  Result found: [D-R-N count; example defense argument quoted verbatim from DR]
  STATUS: PASS / STOP]

WSA-1 READ BARRIER ACTIVE until Gate 0 STATUS: PASS is written above.

---

## Phase 1 — Strategy commitment and seal

Read strategy.md (last authorized read before SEAL). Fill Schema A, VERBATIM EVIDENCE
BLOCK (Source dimension D-[N] — [name]), and STRATEGY.MD SEALED block (all six fields,
Boundary field both halves: "Schema A complete." and "No signal artifacts examined yet.").

[Gate 1 — reproduce with all three fields filled before advancing:
  GATE 1 | Phase: Strategy commitment
  Condition evaluated: Schema A complete; VERBATIM BLOCK delimiters present; Source
                       dimension in D-N format matching Schema A row; SEALED block
                       six fields filled; Boundary: "Schema A complete. No signal
                       artifacts examined yet."
  Result found: [strategy date; D-N count; Source dimension; "SEAL confirmed"]
  STATUS: PASS / STOP]

Do not advance to Phase 2 without Gate 1 STATUS: PASS.

---

## Phase 2 — Signal inventory

List all artifacts in `simulations/` whose filename contains the topic slug.
Fill Schema B. Fill Schema C (all 9 rows; zero-counts for absent; NEVER write ABSENT).
Write PROPOSAL SCOPE after Schema C.

Classification:
  NEW  = artifact date strictly after Schema A strategy date
  PRIOR = artifact date on or before Schema A strategy date

Mandatory delta count sentence (write this verbatim, with integer values):
"Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."

Integer enforcement: N and M must be integers. The following are gate failures:
  writing "a few" / "several" / "some" / "multiple" / "many" in place of N or M

No artifacts found: "No signal artifacts found. Cannot run /topic:plan." Stop.
No HIGH-pressure namespaces: "STRATEGY CURRENT — no new signals since strategy date." Stop.

[Gate 2 — reproduce with all three fields filled before advancing:
  GATE 2 | Phase: Signal inventory and scope declaration
  Condition evaluated: 9 namespace rows present; ABSENT not used; zero-counts for
                       absent; PROPOSAL SCOPE block written with HIGH namespaces
                       named; delta sentence written with integer N and M; integer
                       check: no banned count form present
  Result found: [namespace pressures; HIGH namespaces; delta sentence verbatim]
  STATUS: PASS / STOP]

Do not advance to Phase 3 without Gate 2 STATUS: PASS.

---

## Phase 3 — Delta partition

Classify Schema B artifacts into NEW and PRIOR sets.
PRIOR artifacts are already reflected in strategy.md and may not drive proposals.

[Gate 3 — reproduce with all three fields filled before advancing:
  GATE 3 | Phase: Delta partition
  Condition evaluated: all Schema B artifacts classified as NEW or PRIOR; no PRIOR
                       artifact labeled NEW; NEW count confirmed
  Result found: [NEW filenames listed by name, or "none new"]
  STATUS: PASS / STOP]

If STATUS: STOP: "STRATEGY CURRENT — all signals predate strategy. No proposals." End.
Do not advance to Phase 4 without Gate 3 STATUS: PASS.

---

## Phase 4 — New artifact synthesis

Read each NEW artifact from Phase 3. strategy.md remains SEALED.

Write a synthesis paragraph (4–6 sentences) describing what the NEW signals collectively
reveal. Name at least two artifact filenames by name in the text.

[Gate 4 — reproduce with all three fields filled before advancing:
  GATE 4 | Phase: New artifact synthesis
  Condition evaluated: synthesis paragraph written (4–6 sentences); at least two
                       artifact filenames named; strategy.md not referenced
  Result found: [filenames named in paragraph]
  STATUS: PASS / STOP]

Do not advance to Phase 5 without Gate 4 STATUS: PASS.

---

## Phase 5 — Coverage map and proposals

PROPOSAL SCOPE active: [reproduce HIGH-pressure namespaces from PROPOSAL SCOPE block].

Fill Schema D (coverage map). Default verdict for every dimension: NO CHANGE.
Burden of proof is on the proposed change — not on the status quo.

Fill Schemas E and F. Per-row requirements:
  - Evidence: in Phase 3 NEW list AND in PROPOSAL SCOPE HIGH namespaces
  - Schema A ref (D-N): matches a locked dimension; cross-check against VERBATIM BLOCK
    Source dimension
  - Defense defeated (Row D-R-N): cite specific D-R-N from Schema DR; a named defense
    without a row number does not satisfy this column; `??` if genuinely unknown
  - Before: from locked Schema A only; if Before cannot be filled from Schema A, drop
    the proposal
  - vs. NO CHANGE — MANDATORY: WSA-2 CELL-LEVEL CHECK BLOCK applies (see above);
    draft, check, rewrite if banned form matches, present

Null declarations — fill all three using WSA-3 templates:

[WSA-3 ENFORCEMENT — WRITE-SURFACE ARCHITECTURE, per ARCHITECTURE block above]
NULL DECLARATION TEMPLATES — checks fire inside each template before [reason] is written.

  ADD — NULL: [reason]
    WSA-3 check (fires here, inside this template, before [reason] is written):
    Check [reason] draft against null-declaration BANNED OUTPUT FORMS:
    Banned verbatim: "no new signals" / "nothing to add" / "no changes needed" / "not applicable"
    Match found: discard draft. Rewrite naming the specific condition ruling out additions.
    No match: write [reason].

  REMOVE — NULL: [reason]
    WSA-3 check (fires here, inside this template, before [reason] is written):
    Check [reason] draft against null-declaration BANNED OUTPUT FORMS:
    Banned verbatim: "no new signals" / "nothing to add" / "no changes needed" / "not applicable"
    Match found: discard draft. Rewrite naming the specific condition ruling out removals.
    No match: write [reason].

  REPRIORITIZE — NULL: [reason]
    WSA-3 check (fires here, inside this template, before [reason] is written):
    Check [reason] draft against null-declaration BANNED OUTPUT FORMS:
    Banned verbatim: "no new signals" / "nothing to add" / "no changes needed" / "not applicable"
    Match found: discard draft. Rewrite naming the specific condition ruling out reprioritizations.
    No match: write [reason].

All three null declaration types must appear, even if all are NULL.
WSA-3 enforcement must be documented (check completed, result noted) for each.

Fill Schema G (before/after diff for all proposals). Fill Schema H (or CONFLICT
DETECTION — NULL: [specific reason explaining why no conflicts were found]).

[Gate 5 — reproduce with all three fields filled before advancing:
  GATE 5 | Phase: Proposals complete | WSA-2 and WSA-3 enforcement documented
  Condition evaluated: Schemas E/F complete with WSA-2 check documented per row;
                       three null declaration types present with WSA-3 checks
                       documented; evidence in PROPOSAL SCOPE; D-N refs match Schema
                       A; D-R-N refs match Schema DR (row numbers cited, not names
                       only); vs. NO CHANGE cells cleared WSA-2 check; Schema G
                       count; Schema H or CONFLICT DETECTION typed null
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Do not advance to Phase 6 without Gate 5 STATUS: PASS.

---

## Phase 6 — Confirmation gate

Display all schemas (Schema DR, VERBATIM BLOCK, SEALED block, PROPOSAL SCOPE,
Schemas D through H).

Write exactly the following block:

---
PENDING CONFIRMATION — strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
to apply your version
---

[Gate 6 — reproduce with all three fields filled before advancing:
  GATE 6 | Phase: Confirmation gate
  Condition evaluated: PENDING CONFIRMATION banner written; integer counts for all
                       three types; write-surface architecture complete (WSA-1 at
                       Phase 0, WSA-2 at Schema D/E boundary, WSA-3 in null templates)
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Stop. Write nothing further until the user replies.

---

## Apply (triggered by YES or REVISED)

SEAL lifts. Write exactly the confirmed changes to strategy.md.
Do not reformat unchanged sections. Confirm:
"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## Round 7 Variation Summary

| Variation | Primary axis | WSA-1 mechanism | WSA-2 mechanism | WSA-3 mechanism |
|-----------|-------------|-----------------|-----------------|-----------------|
| V-01 | Role sequence | PRE-COMMIT BLOCK before Phase 0; Gate 0 named as read-barrier | SCHEMA BOUNDARY BLOCK labeled header between Schema D and E | Inline `WS-3 CHECK` with verbatim banned strings inside each null template |
| V-02 | Output format | WS-1 GATE BLOCK as first-class section header before Phase 0 | WS-2 BOUNDARY BLOCK as first-class section header | WS-3 NULL BLOCK sections embedded in each null declaration row |
| V-03 | Lifecycle emphasis | WRITE SURFACE REGISTER declared upfront; WS-1 MILESTONE fires at Phase 0 | WS-2 MILESTONE header at Schema D/E boundary | WS-3 MILESTONE header inside null declaration fill section |
| V-04 | Phrasing register + inertia framing | PRE-SIGNAL READ-BARRIER with WHY: motivation at Phase 0 | Schema D/E BOUNDARY WHY-labeled check block | NULL template with WHY: motivation + inline banned strings |
| V-05 | Combined (all axes as skeleton) | WRITE-SURFACE ARCHITECTURE declared upfront; WSA-1 fires with explicit barrier label and reference to architecture | CELL-LEVEL CHECK BLOCK at Schema D/E boundary; references architecture by name | WSA-3 NULL DECLARATION TEMPLATES section; checks reference architecture; three templates each contain inline banned-forms check |

**C-27 structural risk ranking** (lowest failure risk first):

V-05 > V-03 > V-01 > V-02 > V-04

V-05 declares the architecture as the governing contract before any phase, making each
enforcement site verifiable against a named commitment. A reviewer checking C-27 can
confirm all three sites by: (1) finding WSA-1 at Phase 0, (2) finding WSA-2 at Schema
D/E boundary, (3) finding WSA-3 inside each null template — all three referenced
against the WRITE-SURFACE ARCHITECTURE block.

V-03's WRITE SURFACE REGISTER plus milestone annotations provides similar verifiability
through the register/milestone pattern rather than the architecture/reference pattern.

V-01 and V-02 satisfy all three sites but may fail C-27 if an auditor reads the PRE-COMMIT
BLOCK (V-01) or WS-1 GATE BLOCK (V-02) as appearing at the wrong position relative to
Phase 0 actions — the positioning of WS-1 before Phase 0 vs. at Phase 0 entry is where
these variations are most vulnerable.

V-04's WHY-motivated enforcement is strongest for edge-case generalization but weakest
for mechanical auditing: a reviewer checking C-27 must interpret the WHY motivations to
confirm the architecture rather than scanning for named structural blocks.

**Predicted discriminating axis:** Whether V-01/V-02/V-03 achieve C-27 will depend on
whether the labeled blocks at WSA-2 are positioned literally at the Schema D/E boundary
in the schema section (before any Schema E row), not in Phase 5 prose. V-05 is explicit
about this: the labeled block appears between Schema D and Schema E in the pre-committed
schemas section, making it impossible to fill Schema E without crossing the block.

```json
{
  "variation_count": 5,
  "rubric_version": "v7",
  "new_criterion": "C-27",
  "ceiling": 100,
  "primary_discriminator": "C-27 architectural completeness — three write surfaces at their implementation sites vs. scattered across phases",
  "secondary_discriminator": "WSA-2 placement — labeled block at Schema D/E boundary in schema section vs. embedded in Phase 5 instructions",
  "predicted_winner": "V-05"
}
```
