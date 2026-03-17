# topic-plan Skill Variations -- Round 5 (revised rubric v5, 2026-03-15)

Rubric: v5 revised (C-01 through C-23; C-21 Vocabulary contract violation
enumeration, C-22 Row-number anchor citation in defense linkage, C-23 Verbatim-
quoted banned forms are the three new aspirational criteria extracted from Round 4
scorecard excellence signals)

Round 4 recap: The prior R5 V-05 was the strongest variation (VERBATIM BLOCK +
change-pressure table + STRATEGY.MD SEALED block). Three patterns appeared in PASS
cells with no matching criterion in C-01--C-20:
- V-01 C-17 PASS: the vocabulary contract enumerated "three named violations" beyond
  token definitions; the existing C-17 only requires two tokens be defined.
- V-02 C-08/C-18 PASS: proposals cited a "Phase 0 row number" they defeated, making
  inertia linkage independently verifiable; C-08/C-18 only require that a defense
  argument be named, not that a row number be cross-referenced.
- V-02/V-03 C-16 PASS: banned phrases appeared in quoted form exactly as they would
  appear in model output; C-16 only requires that hedge phrases be "named and banned,"
  not that they be verbatim-quoted.

Round 5 targets: C-21 (vocabulary contract must enumerate named violations, not only
define tokens), C-22 (defense linkage must cite row number, not only name a defense),
C-23 (banned forms must be verbatim-quoted, not described by paraphrase).

Three single-axis variations (V-01, V-02, V-03), then two combinations (V-04, V-05).

---

## V-01: Output format -- Named-violation enumeration in vocabulary contract

**Variation axis**: Output format -- a VOCABULARY CONTRACT block appears at the top
of the pre-committed schemas section. The block defines the two sentinel tokens
(`??` and `--`) and enumerates three named violation conditions, making misuse modes
as explicitly defined as the tokens themselves.

**Hypothesis**: C-17 (two-tier sentinel vocabulary) requires two distinct tokens to
be defined, but is silent on what constitutes a misuse of each token. Without named
violations, a model may write `??` for a namespace it has confirmed has zero
artifacts (known-empty vs. unknown are indistinguishable) or omit a sentinel
entirely (a blank cell looks different from `--` but the rule against blank cells is
buried in prose rather than in the contract block itself). C-21 closes this by
requiring the contract to pre-enumerate specific violation conditions in the same
block as the token definitions, making the contract self-enforcing. This tests
whether co-locating violation enumeration with token definitions reduces misuse
rates compared to spreading the rules across prose instructions.

```
The result of this skill may be zero changes, some changes, or a full strategy
replacement. Inertia -- keeping strategy.md unchanged -- is a co-equal outcome,
not a fallback. The burden of proof rests on change.

You are running /topic:plan for the topic named in the user's message.

---

## VOCABULARY CONTRACT (applies to every schema and every gate output)

Two sentinel tokens are defined and required:

  ??  Open obligation -- the value is unknown or has not yet been determined.
      A ?? cell signals work that must be completed before this gate passes.

  --  Closed decision -- the value is deliberately absent or not applicable.
      A -- cell signals that this slot was evaluated and found to have no value.

Named violations (each is a contract failure; a schema containing any violation
must not be presented as complete):

  VIOLATION-1: A cell is left blank instead of writing ?? or -- .
               An empty cell is not a declaration of any kind.

  VIOLATION-2: ?? is written in a cell where the model already knows the value
               is zero or absent. A confirmed zero must be written as 0 or -- ,
               never as ??.

  VIOLATION-3: -- is written in a required cell (one that must have a value for
               the gate to pass). -- is reserved for optional or not-applicable
               slots; required slots must be filled with their actual value or ??.

---

## Pre-committed schemas (fill in order -- no schema may be skipped or
## replaced with prose)

**Schema A -- Strategy commitment** (Phase 1 only; SEALED at Gate 1)

| Field               | Value |
|---------------------|-------|
| Strategy file       |       |
| Strategy date       |       |
| Completion criteria |       |
| Scope               |       |

Dimensions (label D-1 through D-N in order of appearance in strategy.md):

| Label | Dimension name | What strategy.md says |
|-------|----------------|----------------------|
| D-1   |                |                      |
| D-2   |                |                      |
| ...   |                |                      |

VERBATIM EVIDENCE BLOCK (required output artifact -- reproduce with both
delimiters and Source dimension field filled):

  ===VERBATIM START===
  [paste exact text from strategy.md here -- no paraphrase, no summary,
   no restatement; copy-paste the exact words as they appear in the file]
  ===VERBATIM END===
  Source dimension: D-[N] -- [dimension name]
  (The D-N label must match a row in the Schema A dimensions table above.)

After Schema A and the VERBATIM EVIDENCE BLOCK, reproduce the STRATEGY.MD SEALED
block with all six fields completed:

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
and F must trace to a D-N row in the locked Schema A.

**Schema B -- Signal inventory**
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|

**Schema C -- Namespace audit (all 9 rows required)**
Rules:
- All 9 rows must appear. Absent namespaces: Total = 0, New = 0, pressure = NONE.
- VOCABULARY CONTRACT in force: write 0 (not ??, not --, not "none") for confirmed
  zero counts. Do not write ABSENT or skip any row.
- Change pressure: HIGH if New > 0 | LOW if Total > 0 and New = 0 | NONE if Total = 0

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

After Schema C: HIGH-pressure namespaces: [list names with New counts, or "none"]

**Schema D -- Coverage map**
| Schema A label | Dimension | NEW signal finding | Assessment |
|----------------|-----------|--------------------|---------   |

**Schema E -- Additions**
| # | Dimension [NEW] | Evidence artifact | Schema A ref (D-N) | Before (Schema A text) | After | vs. NO CHANGE |
|---|-----------------|-------------------|--------------------|------------------------|-------|---------------|

**Schema F -- Removals and Reprioritizations**
| # | Action | Dimension | Evidence artifact | Schema A ref (D-N) | Before (Schema A text) | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------------------|------------------------|-------|---------------|

**Schema G -- Before/after diff**
| Dimension | Schema A ref | Before | After | Proposal ref |
|-----------|--------------|--------|-------|--------------|

**Schema H -- Conflict audit**
| Conflict ID | Signal A | Signal B | Dimension | Nature |
|-------------|----------|----------|-----------|--------|

---

## Phase 1 -- Read strategy.md

Read `simulations/TOPICS.md` to find the strategy file. Read strategy.md.

Fill Schema A: all field rows, all D-N dimension rows, VERBATIM EVIDENCE BLOCK
(both delimiters intact, Source dimension in D-N format matching a Schema A row),
and STRATEGY.MD SEALED block (all six fields filled including Boundary field).

Check VOCABULARY CONTRACT: every empty cell must show ?? or --.
VIOLATION-1, VIOLATION-2, VIOLATION-3 disqualify any schema presented as complete.

[Gate 1 -- reproduce with all three fields filled:
  GATE 1 | Phase: Strategy commitment, verbatim block, and seal
  Condition evaluated: [Schema A filled; VERBATIM BLOCK has delimiters + Source
                        dimension in D-N format; SEALED block has all 6 fields;
                        no VOCABULARY CONTRACT violations in any schema cell]
  Result found: [Strategy date, D-N count, VERBATIM Source dimension label,
                 "SEAL present", "BOUNDARY field states both halves"]
  STATUS: PASS / STOP]

Do not advance to Phase 2 without Gate 1 STATUS: PASS.

---

## Phase 2 -- Signal inventory and namespace audit

List every artifact in `simulations/` whose filename contains the topic slug.
Fill Schema B (all artifacts). Fill Schema C (all 9 rows).

NEW = artifact date strictly after Schema A Strategy date.
PRIOR = artifact date on or before Schema A Strategy date.

Write the HIGH-pressure namespace summary immediately after Schema C.

VOCABULARY CONTRACT check: Schema C must have 0 (not ??) in every confirmed-zero
Total and New cell. All 9 namespace rows must be present.

If no artifacts: "No signal artifacts found. Cannot run /topic:plan." Stop.
If no HIGH-pressure namespaces: "STRATEGY CURRENT -- no new signals since
[Strategy date]. No update warranted." Stop.

[Gate 2 -- reproduce with all three fields filled:
  GATE 2 | Phase: Signal inventory
  Condition evaluated: [all 9 namespace rows with numeric counts and pressure
                        ratings; no ?? in confirmed-zero cells; ABSENT not used]
  Result found: [each namespace with Total/New/pressure; HIGH-pressure list]
  STATUS: PASS / STOP]

Do not advance to Phase 3 without Gate 2 STATUS: PASS.

---

## Phase 3 -- Delta partition and mandatory count sentence

Partition Schema B:
  NEW (date > Strategy date): [filenames and dates]
  PRIOR (date <= Strategy date): [filenames and dates]

Write exactly: "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
[N] and [M] must be integers. Writing "a few", "several", "some", or any non-integer
value is a gate failure, not a quality concern.

PRIOR artifacts may not drive proposals. The SEAL is in force.

[Gate 3 -- reproduce with all three fields filled:
  GATE 3 | Phase: Delta partition
  Condition evaluated: [mandatory count sentence present with integer N and M;
                        NEW vs. PRIOR partition complete]
  Result found: [N NEW, M PRIOR -- integers confirmed]
  STATUS: PASS / STOP]

Do not advance to Phase 4 without Gate 3 STATUS: PASS.

---

## Phase 4 -- Read NEW artifacts

Read each NEW artifact. The SEAL is in force.

Write a short paragraph (4-6 sentences) on collective findings.
Name at least two artifact filenames.

[Gate 4 -- reproduce with all three fields filled:
  GATE 4 | Phase: New artifact synthesis
  Condition evaluated: [synthesis paragraph written; at least two filenames cited]
  Result found: [specific filenames cited]
  STATUS: PASS / STOP]

Do not advance to Phase 5 without Gate 4 STATUS: PASS.

---

## Phase 5 -- Coverage map and proposals

Fill Schema D.

Default verdict: NO CHANGE. Burden of proof is on change.

Fill Schemas E and F. For every proposal row:
- Evidence must be from a NEW artifact (HIGH-pressure namespace only)
- Schema A ref (D-N) must name a specific locked dimension
- Before must reproduce Schema A D-N text (SEAL violation if it requires re-reading
  strategy.md; if Before cannot be written from Schema A, drop the proposal)
- vs. NO CHANGE: mandatory column; name a specific consequence of leaving the
  strategy unchanged. "No change needed" is not an acceptable entry in this column.

Null declarations (each type labeled separately):
  ADDITIONS: none -- [reason] | or [N] proposed
  REMOVALS: none -- [reason] | or [N] proposed
  REPRIORITIZATIONS: none -- [reason] | or [N] proposed

VOCABULARY CONTRACT check before presenting schemas: no blank cells, no ?? in
confirmed-zero cells, no -- in required cells.

Fill Schemas G and H.

[Gate 5 -- reproduce with all three fields filled:
  GATE 5 | Phase: Proposals complete
  Condition evaluated: [all three null declarations present; Schema G row count;
                        no Before value requires strategy.md re-read; vs. NO CHANGE
                        column has specific consequence in every non-null row;
                        no VOCABULARY CONTRACT violations]
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Do not advance to Phase 6 without Gate 5 STATUS: PASS.

---

## Phase 6 -- Confirmation gate

Display all schemas (including VERBATIM EVIDENCE BLOCK and STRATEGY.MD SEALED
block from Phase 1).

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
  Condition evaluated: [PENDING CONFIRMATION block written with proposal counts]
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Stop. Write nothing further until the user replies.

---

## Apply (triggered by YES or REVISED)

The SEAL lifts when the user replies. Write exactly the confirmed changes to
strategy.md. No additional edits. Confirm:
"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-02: Lifecycle emphasis -- Defense register with row-number anchors

**Variation axis**: Lifecycle emphasis -- a Phase 0 (Defense register) is inserted
before Phase 1. The defense register table assigns an explicit D-R row number to
each potential change dimension. Each subsequent proposal row in Schemas E and F
must cite "Defense defeated: Row D-R-[N]", making inertia linkage independently
verifiable as a cross-reference without re-reading prose.

**Hypothesis**: C-18 (pre-signal defense register) requires each potential change
dimension to have a committed defense argument before reading artifacts, and C-08
requires each proposal to name the defense it defeated. The gap: a "named defense"
without a row number requires the reviewer to match names across two tables,
introducing ambiguity when dimension names are similar or abbreviated. C-22 closes
this by requiring the citation to include a row number (e.g., "Defense defeated:
Row D-R-3"), so that inertia linkage is verifiable by cross-reference, not by
prose matching. This tests whether assigning explicit row IDs to defense register
entries and requiring those IDs in proposal citations improves cross-reference
verifiability compared to named-only defenses.

```
The result of this skill may be zero changes, some changes, or a full strategy
replacement. Inertia -- keeping strategy.md unchanged -- is a co-equal outcome,
not a fallback. The burden of proof rests on change.

You are running /topic:plan for the topic named in the user's message.

---

## Pre-committed schemas (fill in order -- no schema may be skipped or
## replaced with prose)

**Schema A -- Strategy commitment** (Phase 1 only; SEALED at Gate 1)

| Field               | Value |
|---------------------|-------|
| Strategy file       |       |
| Strategy date       |       |
| Completion criteria |       |
| Scope               |       |

Dimensions (label D-1 through D-N in order of appearance in strategy.md):

| Label | Dimension name | What strategy.md says |
|-------|----------------|----------------------|
| D-1   |                |                      |
| D-2   |                |                      |
| ...   |                |                      |

VERBATIM EVIDENCE BLOCK (required output artifact -- reproduce with both
delimiters and Source dimension field filled):

  ===VERBATIM START===
  [paste exact text from strategy.md here -- no paraphrase, no summary,
   no restatement; copy-paste the exact words as they appear in the file]
  ===VERBATIM END===
  Source dimension: D-[N] -- [dimension name]
  (The D-N label must match a row in the Schema A dimensions table above.)

After Schema A and the VERBATIM EVIDENCE BLOCK, reproduce the STRATEGY.MD SEALED
block with all six fields completed:

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

**Schema DR -- Defense register** (committed in Phase 0; rows locked before Phase 2)

One row per Schema A dimension. Each row is assigned a permanent D-R row number.
The active defense argument states why the current strategy entry is sufficient.
A defense argument of "no reason to change" is not acceptable -- name the specific
rationale from strategy.md.

| Row  | Schema A ref | Dimension name | Active defense argument |
|------|--------------|----------------|-------------------------|
| D-R-1 |             |                |                         |
| D-R-2 |             |                |                         |
| ...   |             |                |                         |

Each proposal row in Schemas E and F must cite the specific D-R row it defeated:
"Defense defeated: Row D-R-[N]" -- where [N] is the exact row number from Schema DR.
A named defense without a row number does not satisfy this requirement.

**Schema B -- Signal inventory**
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|

**Schema C -- Namespace audit (all 9 rows required)**
Rules:
- All 9 rows must appear. Absent namespaces: Total = 0, New = 0, pressure = NONE.
- Do not write ABSENT or skip any row. Zero-counts are the required form.
- Change pressure: HIGH if New > 0 | LOW if Total > 0 and New = 0 | NONE if Total = 0

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

After Schema C: HIGH-pressure namespaces: [list names with New counts, or "none"]

**Schema D -- Coverage map**
| Schema A label | Dimension | NEW signal finding | Assessment |
|----------------|-----------|--------------------|---------   |

**Schema E -- Additions**
| # | Dimension [NEW] | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before (Schema A text) | After | vs. NO CHANGE |
|---|-----------------|-------------------|--------------------|------------------------------|------------------------|-------|---------------|

**Schema F -- Removals and Reprioritizations**
| # | Action | Dimension | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before (Schema A text) | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------------------|------------------------------|------------------------|-------|---------------|

**Schema G -- Before/after diff**
| Dimension | Schema A ref | Before | After | Proposal ref |
|-----------|--------------|--------|-------|--------------|

**Schema H -- Conflict audit**
| Conflict ID | Signal A | Signal B | Dimension | Nature |
|-------------|----------|----------|-----------|--------|

---

## Phase 0 -- Defense register

Read `simulations/TOPICS.md` to find the strategy file. Read strategy.md.

Fill Schema A: all field rows, all D-N dimension rows.

Then fill Schema DR: one row per Schema A dimension, with the D-R row number
assigned sequentially (D-R-1, D-R-2, ...). Write the active defense argument for
each dimension -- the specific rationale from strategy.md for why this dimension's
current entry is sufficient. Do not write "no reason to change" -- that is not
a defense argument; it is an absence of one.

Schema DR is locked after Gate 0. Row numbers assigned here are the only valid
row references in "Defense defeated: Row D-R-N" citations.

[Gate 0 -- reproduce with all three fields filled:
  GATE 0 | Phase: Defense register
  Condition evaluated: [Schema DR has one row per Schema A dimension; each row
                        has a D-R row number, a Schema A ref, and an active
                        defense argument; no row reads "no reason to change"]
  Result found: [D-R row count matching D-N dimension count; all defense
                 arguments name specific strategy.md rationale]
  STATUS: PASS / STOP]

Do not advance to Phase 1 without Gate 0 STATUS: PASS.

---

## Phase 1 -- Seal strategy.md

Fill the VERBATIM EVIDENCE BLOCK (both delimiters intact, Source dimension in
D-N format matching a Schema A row). Reproduce the STRATEGY.MD SEALED block
(all six fields filled including Boundary field).

[Gate 1 -- reproduce with all three fields filled:
  GATE 1 | Phase: Verbatim block and seal
  Condition evaluated: [VERBATIM BLOCK has delimiters + Source dimension in D-N
                        format; SEALED block has all 6 fields filled including
                        Boundary stating "Schema A complete. No signal artifacts
                        examined yet."]
  Result found: [Strategy date, D-N count, VERBATIM Source dimension label,
                 "SEAL present with Boundary field"]
  STATUS: PASS / STOP]

Do not advance to Phase 2 without Gate 1 STATUS: PASS.

---

## Phase 2 -- Signal inventory and namespace audit

List every artifact in `simulations/` whose filename contains the topic slug.
Fill Schema B (all artifacts). Fill Schema C (all 9 rows -- zero-counts for
absent namespaces, NEVER write ABSENT).

Write the HIGH-pressure namespace summary immediately after Schema C.

NEW = artifact date strictly after Schema A Strategy date.
PRIOR = artifact date on or before Schema A Strategy date.

If no artifacts: "No signal artifacts found. Cannot run /topic:plan." Stop.
If no HIGH-pressure namespaces: "STRATEGY CURRENT -- no new signals since
[Strategy date]. No update warranted." Stop.

[Gate 2 -- reproduce with all three fields filled:
  GATE 2 | Phase: Signal inventory
  Condition evaluated: [all 9 namespace rows with numeric counts and pressure
                        ratings; ABSENT not used anywhere in Schema C]
  Result found: [each namespace with Total/New/pressure; HIGH-pressure list]
  STATUS: PASS / STOP]

Do not advance to Phase 3 without Gate 2 STATUS: PASS.

---

## Phase 3 -- Delta partition and mandatory count sentence

Partition Schema B:
  NEW (date > Strategy date): [filenames and dates]
  PRIOR (date <= Strategy date): [filenames and dates]

Write exactly: "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
[N] and [M] must be integers. Writing "a few", "several", "some", or any non-integer
value is a gate failure.

PRIOR artifacts may not drive proposals. The SEAL is in force.

[Gate 3 -- reproduce with all three fields filled:
  GATE 3 | Phase: Delta partition
  Condition evaluated: [mandatory count sentence present with integer N and M]
  Result found: [N NEW, M PRIOR -- integers confirmed]
  STATUS: PASS / STOP]

Do not advance to Phase 4 without Gate 3 STATUS: PASS.

---

## Phase 4 -- Read NEW artifacts

Read each NEW artifact. The SEAL is in force.

Write a short paragraph (4-6 sentences) on collective findings.
Name at least two artifact filenames.

[Gate 4 -- reproduce with all three fields filled:
  GATE 4 | Phase: New artifact synthesis
  Condition evaluated: [synthesis paragraph written; at least two filenames cited]
  Result found: [specific filenames cited]
  STATUS: PASS / STOP]

Do not advance to Phase 5 without Gate 4 STATUS: PASS.

---

## Phase 5 -- Coverage map and proposals

Fill Schema D.

Default verdict: NO CHANGE. Burden of proof is on change.

Fill Schemas E and F. For every proposal row:
- Evidence must be from a NEW artifact (HIGH-pressure namespace only)
- Schema A ref (D-N): name the specific locked dimension
- Defense defeated (Row D-R-N): MANDATORY -- cite the exact Schema DR row number
  the evidence defeated (e.g., "Defense defeated: Row D-R-3"). A named defense
  without a row number does not satisfy this column.
- Before must reproduce Schema A D-N text (SEAL violation if it requires
  re-reading strategy.md; if Before cannot be written from Schema A, drop)
- vs. NO CHANGE: name a specific consequence of leaving the strategy unchanged

Null declarations (each type labeled separately):
  ADDITIONS: none -- [reason] | or [N] proposed
  REMOVALS: none -- [reason] | or [N] proposed
  REPRIORITIZATIONS: none -- [reason] | or [N] proposed

Fill Schemas G and H.

[Gate 5 -- reproduce with all three fields filled:
  GATE 5 | Phase: Proposals complete
  Condition evaluated: [all three null declarations present; every non-null
                        proposal row has a "Defense defeated: Row D-R-N" citation
                        matching a Schema DR row number; Schema G row count]
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Do not advance to Phase 6 without Gate 5 STATUS: PASS.

---

## Phase 6 -- Confirmation gate

Display all schemas (including VERBATIM EVIDENCE BLOCK and STRATEGY.MD SEALED
block from Phase 1).

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
  Condition evaluated: [PENDING CONFIRMATION block written with proposal counts]
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Stop. Write nothing further until the user replies.

---

## Apply (triggered by YES or REVISED)

The SEAL lifts when the user replies. Write exactly the confirmed changes to
strategy.md. No additional edits. Confirm:
"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-03: Phrasing register -- Verbatim-quoted banned forms in all disqualification rules

**Variation axis**: Phrasing register -- every hedge-phrase disqualification rule
in the skill prompt states banned phrases in verbatim-quoted form exactly as they
would appear in model output (e.g., `"no change needed"`, `"clearly warranted"`,
`"several artifacts"`). Described paraphrases ("common hedge phrases") are replaced
by the exact strings that would trigger a violation.

**Hypothesis**: C-16 (hedge-phrase disqualification) requires that required
justification columns explicitly name and ban common hedge phrases. The gap: a
rule that says "do not use hedge phrases like 'no change needed'" leaves the
definition of "hedge phrase" open to interpretation -- a model may not recognize
"no significant change needed" as equivalent to "no change needed" unless the
exact quoted form is the stated violation. C-23 closes this by requiring that
banned forms appear verbatim-quoted in the exact form they would appear in output,
making violations pattern-matchable without interpretive judgment. This tests whether
replacing described prohibitions with verbatim-quoted strings reduces the rate of
near-miss hedge phrases that evade the spirit of the rule while satisfying its
literal terms.

```
The result of this skill may be zero changes, some changes, or a full strategy
replacement. Inertia -- keeping strategy.md unchanged -- is a co-equal outcome,
not a fallback. The burden of proof rests on change.

You are running /topic:plan for the topic named in the user's message.

---

## Pre-committed schemas (fill in order -- no schema may be skipped or
## replaced with prose)

**Schema A -- Strategy commitment** (Phase 1 only; SEALED at Gate 1)

| Field               | Value |
|---------------------|-------|
| Strategy file       |       |
| Strategy date       |       |
| Completion criteria |       |
| Scope               |       |

Dimensions (label D-1 through D-N in order of appearance in strategy.md):

| Label | Dimension name | What strategy.md says |
|-------|----------------|----------------------|
| D-1   |                |                      |
| D-2   |                |                      |
| ...   |                |                      |

VERBATIM EVIDENCE BLOCK (required output artifact -- reproduce with both
delimiters and Source dimension field filled):

  ===VERBATIM START===
  [paste exact text from strategy.md here -- no paraphrase, no summary,
   no restatement; copy-paste the exact words as they appear in the file]
  ===VERBATIM END===
  Source dimension: D-[N] -- [dimension name]
  (The D-N label must match a row in the Schema A dimensions table above.)

After Schema A and the VERBATIM EVIDENCE BLOCK, reproduce the STRATEGY.MD SEALED
block with all six fields completed:

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

Schema A is LOCKED and SEALED after Gate 1.

**Schema B -- Signal inventory**
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|

**Schema C -- Namespace audit (all 9 rows required)**
Rules:
- All 9 rows must appear. Absent namespaces: Total = 0, New = 0, pressure = NONE.
- Do not write ABSENT or skip any row. Zero-counts are the required form.
- Change pressure: HIGH if New > 0 | LOW if Total > 0 and New = 0 | NONE if Total = 0

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

After Schema C: HIGH-pressure namespaces: [list names with New counts, or "none"]

**Schema D -- Coverage map**
| Schema A label | Dimension | NEW signal finding | Assessment |
|----------------|-----------|--------------------|---------   |

**Schema E -- Additions**
| # | Dimension [NEW] | Evidence artifact | Schema A ref (D-N) | Before (Schema A text) | After | vs. NO CHANGE |
|---|-----------------|-------------------|--------------------|------------------------|-------|---------------|

BANNED FORMS in Schema E "vs. NO CHANGE" column (any of these strings is a
disqualification; the cell must be rewritten before Gate 5 passes):
  "no change needed"
  "change is clearly warranted"
  "no update required"
  "the evidence is sufficient"
  "this speaks for itself"

**Schema F -- Removals and Reprioritizations**
| # | Action | Dimension | Evidence artifact | Schema A ref (D-N) | Before (Schema A text) | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------------------|------------------------|-------|---------------|

BANNED FORMS in Schema F "vs. NO CHANGE" column (same list; any occurrence
disqualifies the row):
  "no change needed"
  "change is clearly warranted"
  "no update required"
  "the evidence is sufficient"
  "this speaks for itself"

**Schema G -- Before/after diff**
| Dimension | Schema A ref | Before | After | Proposal ref |
|-----------|--------------|--------|-------|--------------|

**Schema H -- Conflict audit**
| Conflict ID | Signal A | Signal B | Dimension | Nature |
|-------------|----------|----------|-----------|--------|

---

## Phase 1 -- Read strategy.md

Read `simulations/TOPICS.md` to find the strategy file. Read strategy.md.

Fill Schema A and VERBATIM EVIDENCE BLOCK and STRATEGY.MD SEALED block.

[Gate 1 -- reproduce with all three fields filled:
  GATE 1 | Phase: Strategy commitment, verbatim block, and seal
  Condition evaluated: [Schema A filled; VERBATIM BLOCK has delimiters + Source
                        dimension in D-N format; SEALED block has all 6 fields]
  Result found: [Strategy date, D-N count, VERBATIM Source dimension, SEAL present,
                 Boundary field states both halves]
  STATUS: PASS / STOP]

Do not advance to Phase 2 without Gate 1 STATUS: PASS.

---

## Phase 2 -- Signal inventory and namespace audit

List every artifact in `simulations/` whose filename contains the topic slug.
Fill Schema B (all artifacts). Fill Schema C (all 9 rows -- zero-counts for
absent namespaces, NEVER write ABSENT).

Write the HIGH-pressure namespace summary immediately after Schema C.

NEW = artifact date strictly after Schema A Strategy date.
PRIOR = artifact date on or before Schema A Strategy date.

If no artifacts: "No signal artifacts found. Cannot run /topic:plan." Stop.
If no HIGH-pressure namespaces: "STRATEGY CURRENT -- no new signals since
[Strategy date]. No update warranted." Stop.

[Gate 2 -- reproduce with all three fields filled:
  GATE 2 | Phase: Signal inventory
  Condition evaluated: [all 9 namespace rows with numeric counts; ABSENT not used]
  Result found: [each namespace with Total/New/pressure; HIGH-pressure list]
  STATUS: PASS / STOP]

Do not advance to Phase 3 without Gate 2 STATUS: PASS.

---

## Phase 3 -- Delta partition and mandatory count sentence

Partition Schema B into NEW and PRIOR.

Write exactly: "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."

BANNED COUNT FORMS: writing "a few", "several", "some", "multiple", "many", or any
non-integer value in place of [N] or [M] is a gate failure. Integer counts only.

PRIOR artifacts may not drive proposals.

[Gate 3 -- reproduce with all three fields filled:
  GATE 3 | Phase: Delta partition
  Condition evaluated: [mandatory sentence with integer N and M; no banned count forms]
  Result found: [N NEW integer, M PRIOR integer]
  STATUS: PASS / STOP]

Do not advance to Phase 4 without Gate 3 STATUS: PASS.

---

## Phase 4 -- Read NEW artifacts

Read each NEW artifact. Write a synthesis paragraph (4-6 sentences). Name at least
two artifact filenames by their exact filenames.

[Gate 4 -- reproduce with all three fields filled:
  GATE 4 | Phase: New artifact synthesis
  Condition evaluated: [synthesis paragraph; at least two exact filenames cited]
  Result found: [specific filenames cited]
  STATUS: PASS / STOP]

Do not advance to Phase 5 without Gate 4 STATUS: PASS.

---

## Phase 5 -- Coverage map and proposals

Fill Schema D.

Default verdict: NO CHANGE. Burden of proof is on change.

Fill Schemas E and F. For every proposal row:
- Evidence: NEW artifact (HIGH-pressure namespace only)
- Schema A ref (D-N): specific locked dimension
- Before: reproduce Schema A D-N text (SEAL violation if requires re-reading;
  if Before cannot be written from Schema A, drop the proposal)
- vs. NO CHANGE: MANDATORY -- name a specific consequence of leaving the strategy
  unchanged. Check cell against BANNED FORMS list above before presenting.
  Any banned form disqualifies the row -- rewrite before Gate 5.

Null declarations (each type labeled separately):
  ADDITIONS: none -- [reason] | or [N] proposed
  REMOVALS: none -- [reason] | or [N] proposed
  REPRIORITIZATIONS: none -- [reason] | or [N] proposed

BANNED FORMS also apply to null declaration reasoning. These strings disqualify
a null declaration reason:
  "nothing to change"
  "no new signals"
  "signals are insufficient"
  "strategy remains valid"
Replace with: the specific dimension assessed and the specific reason the evidence
did not reach the threshold.

Fill Schemas G and H.

[Gate 5 -- reproduce with all three fields filled:
  GATE 5 | Phase: Proposals complete
  Condition evaluated: [all three null declarations present; no BANNED FORMS in
                        vs. NO CHANGE column; no BANNED FORMS in null declaration
                        reasons; no Before requires strategy.md re-read]
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Do not advance to Phase 6 without Gate 5 STATUS: PASS.

---

## Phase 6 -- Confirmation gate

Display all schemas.

Write exactly:

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
to apply your version
---

[Gate 6 -- reproduce with all three fields filled:
  GATE 6 | Phase: Confirmation gate
  Condition evaluated: [PENDING CONFIRMATION block written with proposal counts]
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Stop. Write nothing further until the user replies.

---

## Apply (triggered by YES or REVISED)

The SEAL lifts when the user replies. Write exactly the confirmed changes to
strategy.md. Confirm:
"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-04: Combination -- Vocabulary contract violation enumeration + Row-number anchor citation

**Variation axis**: Combination of V-01 (C-21, output format) and V-02 (C-22,
lifecycle emphasis). The VOCABULARY CONTRACT block with named violations is added
at the top, AND Phase 0 with a row-numbered defense register is inserted before
Phase 1. Each proposal row must satisfy both: no VOCABULARY CONTRACT violations
AND a "Defense defeated: Row D-R-N" citation with a row number matching Schema DR.

**Hypothesis**: V-01 and V-02 address orthogonal failure modes. V-01 addresses
token misuse (blank cells, wrong sentinels) through an upfront contract with named
violations. V-02 addresses inertia-linkage verifiability (named defenses that
cannot be cross-referenced) through row numbers in a pre-committed register.
These two mechanisms do not interact: a proposal row can satisfy the defense-
linkage row number requirement while still containing a blank cell (VOCABULARY
CONTRACT violation), and vice versa. Combining them forces both failure modes to
be addressed simultaneously. The hypothesis is that the combination produces lower
overall error rates than either axis alone, because each mechanism closes a gap
the other does not address.

```
The result of this skill may be zero changes, some changes, or a full strategy
replacement. Inertia -- keeping strategy.md unchanged -- is a co-equal outcome,
not a fallback. The burden of proof rests on change.

You are running /topic:plan for the topic named in the user's message.

---

## VOCABULARY CONTRACT (applies to every schema and every gate output)

Two sentinel tokens are defined and required:

  ??  Open obligation -- the value is unknown or has not yet been determined.
      A ?? cell signals work that must be completed before this gate passes.

  --  Closed decision -- the value is deliberately absent or not applicable.
      A -- cell signals that this slot was evaluated and found to have no value.

Named violations:

  VIOLATION-1: A cell is left blank instead of writing ?? or -- .
               An empty cell is not a declaration of any kind.

  VIOLATION-2: ?? is written in a cell where the model already knows the value
               is zero or absent. A confirmed zero must be written as 0 or -- .

  VIOLATION-3: -- is written in a required cell (one that must have a value
               for the gate to pass). Required cells must be filled with their
               actual value or ??.

---

## Pre-committed schemas (fill in order -- no schema may be skipped or
## replaced with prose)

**Schema A -- Strategy commitment** (Phase 1 only; SEALED at Gate 1)

| Field               | Value |
|---------------------|-------|
| Strategy file       |       |
| Strategy date       |       |
| Completion criteria |       |
| Scope               |       |

Dimensions (label D-1 through D-N in order of appearance in strategy.md):

| Label | Dimension name | What strategy.md says |
|-------|----------------|----------------------|
| D-1   |                |                      |
| D-2   |                |                      |
| ...   |                |                      |

VERBATIM EVIDENCE BLOCK:

  ===VERBATIM START===
  [paste exact text from strategy.md here]
  ===VERBATIM END===
  Source dimension: D-[N] -- [dimension name]

STRATEGY.MD SEALED block (all six fields required):

  ================================================================
  STRATEGY.MD SEALED
  Sealed after: Phase 1 (Schema A and VERBATIM BLOCK complete)
  Prohibition: strategy.md may not be re-opened or re-read until
               after the user replies YES, NO, or REVISED.
  Violation condition: Any "Before" value not traceable to Schema A
               D-N rows is a SEAL violation and must be dropped.
  Prohibition lifts: After user reply to the confirmation gate.
  Schema A contains: [N] dimensions labeled D-1 through D-[N]
  Boundary: Schema A complete. No signal artifacts examined yet.
  ================================================================

**Schema DR -- Defense register** (Phase 0; rows locked before Phase 2)

| Row   | Schema A ref | Dimension name | Active defense argument |
|-------|--------------|----------------|-------------------------|
| D-R-1 |              |                |                         |
| D-R-2 |              |                |                         |
| ...   |              |                |                         |

VOCABULARY CONTRACT check: every cell must be filled; ?? for unknown, 0 or -- for
confirmed-absent. VIOLATION-1 applies -- no blank cells in Schema DR.

**Schema B -- Signal inventory**
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|

**Schema C -- Namespace audit (all 9 rows required)**
VOCABULARY CONTRACT check: confirmed-zero counts must be written as 0 (not ??, not --).

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

**Schema D -- Coverage map**
| Schema A label | Dimension | NEW signal finding | Assessment |
|----------------|-----------|--------------------|---------   |

**Schema E -- Additions**
| # | Dimension [NEW] | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before (Schema A text) | After | vs. NO CHANGE |
|---|-----------------|-------------------|--------------------|------------------------------|------------------------|-------|---------------|

Defense defeated column: MANDATORY. Must cite the exact Schema DR row number
(e.g., "Row D-R-3"). A named defense without a row number does not satisfy
this column. VIOLATION-1 applies: a blank cell here is not a null declaration.

**Schema F -- Removals and Reprioritizations**
| # | Action | Dimension | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before (Schema A text) | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------------------|------------------------------|------------------------|-------|---------------|

**Schema G -- Before/after diff**
| Dimension | Schema A ref | Before | After | Proposal ref |
|-----------|--------------|--------|-------|--------------|

**Schema H -- Conflict audit**
| Conflict ID | Signal A | Signal B | Dimension | Nature |
|-------------|----------|----------|-----------|--------|

---

## Phase 0 -- Defense register

Read `simulations/TOPICS.md` to find the strategy file. Read strategy.md.

Fill Schema A (all field rows, all D-N dimension rows).

Fill Schema DR: one row per Schema A dimension, assigned D-R row numbers
sequentially. Write the active defense argument for each dimension from
strategy.md. "No reason to change" is not an acceptable defense argument.

VOCABULARY CONTRACT: no blank cells in Schema DR or Schema A.

[Gate 0 -- reproduce with all three fields filled:
  GATE 0 | Phase: Defense register
  Condition evaluated: [Schema DR has one row per Schema A dimension; each row
                        has D-R row number, Schema A ref, defense argument;
                        no VOCABULARY CONTRACT violations in either schema]
  Result found: [D-R row count; all defense arguments non-generic]
  STATUS: PASS / STOP]

Do not advance to Phase 1 without Gate 0 STATUS: PASS.

---

## Phase 1 -- Seal strategy.md

Fill the VERBATIM EVIDENCE BLOCK (Source dimension in D-N format).
Reproduce the STRATEGY.MD SEALED block (all six fields including Boundary).

[Gate 1 -- reproduce with all three fields filled:
  GATE 1 | Phase: Verbatim block and seal
  Condition evaluated: [VERBATIM BLOCK has delimiters + D-N Source; SEALED block
                        has 6 fields; no VOCABULARY CONTRACT violations]
  Result found: [Strategy date, D-N count, Source dimension label, SEAL + Boundary]
  STATUS: PASS / STOP]

Do not advance to Phase 2 without Gate 1 STATUS: PASS.

---

## Phase 2 -- Signal inventory and namespace audit

List every artifact in `simulations/` whose filename contains the topic slug.
Fill Schema B and Schema C (all 9 rows; zero-counts as 0, never ABSENT).

VOCABULARY CONTRACT: confirmed-zero Total/New cells must be 0, not ??.

NEW = date strictly after Schema A Strategy date.
PRIOR = date on or before Schema A Strategy date.

If no artifacts: "No signal artifacts found." Stop.
If no HIGH-pressure namespaces: "STRATEGY CURRENT." Stop.

[Gate 2 -- reproduce with all three fields filled:
  GATE 2 | Phase: Signal inventory
  Condition evaluated: [9 rows; numeric counts; no VOCABULARY CONTRACT violations]
  Result found: [each namespace with Total/New/pressure; HIGH-pressure list]
  STATUS: PASS / STOP]

Do not advance to Phase 3 without Gate 2 STATUS: PASS.

---

## Phase 3 -- Delta partition and mandatory count sentence

Partition Schema B into NEW and PRIOR.

Write exactly: "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."
[N] and [M] must be integers. "A few", "several", "some", or any non-integer is a
gate failure.

[Gate 3 -- reproduce with all three fields filled:
  GATE 3 | Phase: Delta partition
  Condition evaluated: [mandatory sentence with integer N and M]
  Result found: [N NEW, M PRIOR]
  STATUS: PASS / STOP]

Do not advance to Phase 4 without Gate 3 STATUS: PASS.

---

## Phase 4 -- Read NEW artifacts

Read each NEW artifact. Write a synthesis paragraph (4-6 sentences, two filenames).

[Gate 4 -- reproduce with all three fields filled:
  GATE 4 | Phase: New artifact synthesis
  Condition evaluated: [paragraph; two filenames cited]
  Result found: [filenames]
  STATUS: PASS / STOP]

Do not advance to Phase 5 without Gate 4 STATUS: PASS.

---

## Phase 5 -- Coverage map and proposals

Fill Schema D. Default verdict: NO CHANGE. Burden of proof is on change.

Fill Schemas E and F. Every proposal row must satisfy:
- Evidence: NEW artifact (HIGH-pressure namespace only)
- Schema A ref (D-N): specific locked dimension
- Defense defeated (Row D-R-N): MANDATORY row number from Schema DR
- Before: Schema A D-N text (SEAL violation if requires re-reading)
- vs. NO CHANGE: specific consequence of leaving strategy unchanged

"No change needed" is not an acceptable entry in vs. NO CHANGE.

VOCABULARY CONTRACT: no blank cells in any column of Schemas E or F.

Null declarations:
  ADDITIONS: none -- [reason] | or [N] proposed
  REMOVALS: none -- [reason] | or [N] proposed
  REPRIORITIZATIONS: none -- [reason] | or [N] proposed

Fill Schemas G and H.

[Gate 5 -- reproduce with all three fields filled:
  GATE 5 | Phase: Proposals complete
  Condition evaluated: [null declarations present; Defense defeated column has
                        D-R row numbers in every non-null row; no VOCABULARY
                        CONTRACT violations; vs. NO CHANGE column non-generic]
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Do not advance to Phase 6 without Gate 5 STATUS: PASS.

---

## Phase 6 -- Confirmation gate

Display all schemas. Write exactly:

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table
to apply your version
---

[Gate 6 -- reproduce with all three fields filled:
  GATE 6 | Phase: Confirmation gate
  Condition evaluated: [PENDING CONFIRMATION block with proposal counts]
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Stop. Write nothing further until the user replies.

---

## Apply (triggered by YES or REVISED)

The SEAL lifts. Write confirmed changes to strategy.md. Confirm:
"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-05: Full combination -- Vocabulary contract + Row-number anchors + Verbatim-quoted banned forms

**Variation axis**: Full combination of V-01 (C-21), V-02 (C-22), and V-03 (C-23).
The VOCABULARY CONTRACT block with named violations, Phase 0 defense register with
row-numbered entries and mandatory D-R-N citations, and verbatim-quoted banned
forms in all disqualification rules are combined in a single prompt body.

**Hypothesis**: Each of the three single-axis variations addresses a distinct failure
mode: sentinel misuse (C-21), unverifiable inertia linkage (C-22), and interpretive
hedge-phrase evasion (C-23). These failure modes are statistically independent --
a model may pass any two while failing the third. The full combination closes all
three simultaneously. The hypothesis is that adding all three mechanisms produces
a higher floor score across all rubric dimensions than any single-axis variation,
because no single failure mode can pull the total below golden threshold. The
combination also tests for interaction effects: do the three mechanisms reinforce
each other (e.g., does the upfront vocabulary contract prime the model to apply
verbatim-quoted forms correctly) or do they interfere (e.g., does Phase 0's defense
register consume enough context that C-21's vocabulary contract is less salient by
Phase 5)?

```
The result of this skill may be zero changes, some changes, or a full strategy
replacement. Inertia -- keeping strategy.md unchanged -- is a co-equal outcome,
not a fallback. The burden of proof rests on change, not on stability.

You are running /topic:plan for the topic named in the user's message.

---

## VOCABULARY CONTRACT (applies to every schema and every gate output)

Two sentinel tokens are defined and required:

  ??  Open obligation -- the value is unknown or has not yet been determined.

  --  Closed decision -- the value is deliberately absent or not applicable.

Named violations (any occurrence disqualifies a schema presented as complete):

  VIOLATION-1: A cell is left blank instead of writing ?? or --.
               An empty cell is not a declaration of any kind.

  VIOLATION-2: ?? appears in a cell where the value is already known to be
               zero or absent. A confirmed zero must be written as 0 or --.

  VIOLATION-3: -- appears in a required cell (one that must have a value for
               the gate to pass). Required cells must contain their actual
               value or ??.

---

## Banned output forms (verbatim; any of these strings in a required column
## is a disqualification requiring a rewrite before the gate passes)

In "vs. NO CHANGE" column and inertia-justification cells:
  "no change needed"
  "no update required"
  "change is clearly warranted"
  "the evidence speaks for itself"
  "signals are insufficient"
  "nothing to change"
  "strategy remains valid"

In null declaration reasoning:
  "no new signals"
  "no change needed"
  "nothing to add"
  "nothing to remove"
  "nothing to reprioritize"

In delta count sentence (replace with integer N and M):
  "a few"
  "several"
  "some"
  "multiple"
  "many"

---

## Pre-committed schemas (fill in order -- no schema may be skipped or
## replaced with prose)

**Schema A -- Strategy commitment** (Phase 1 only; SEALED at Gate 1)

| Field               | Value |
|---------------------|-------|
| Strategy file       |       |
| Strategy date       |       |
| Completion criteria |       |
| Scope               |       |

Dimensions (label D-1 through D-N in order of appearance in strategy.md):

| Label | Dimension name | What strategy.md says |
|-------|----------------|----------------------|
| D-1   |                |                      |
| D-2   |                |                      |
| ...   |                |                      |

VERBATIM EVIDENCE BLOCK:

  ===VERBATIM START===
  [paste exact text from strategy.md -- no paraphrase, no summary]
  ===VERBATIM END===
  Source dimension: D-[N] -- [dimension name]

STRATEGY.MD SEALED block (all six fields required):

  ================================================================
  STRATEGY.MD SEALED
  Sealed after: Phase 1 (Schema A and VERBATIM BLOCK complete)
  Prohibition: strategy.md may not be re-opened or re-read until
               after the user replies YES, NO, or REVISED.
  Violation condition: Any "Before" value not traceable to Schema A
               D-N rows is a SEAL violation and must be dropped.
  Prohibition lifts: After user reply to the confirmation gate.
  Schema A contains: [N] dimensions labeled D-1 through D-[N]
  Boundary: Schema A complete. No signal artifacts examined yet.
  ================================================================

**Schema DR -- Defense register** (Phase 0; rows locked before Phase 2)

One row per Schema A dimension. D-R row numbers are assigned here and are the
only valid row references in "Defense defeated: Row D-R-N" citations.

| Row   | Schema A ref | Dimension name | Active defense argument |
|-------|--------------|----------------|-------------------------|
| D-R-1 |              |                |                         |
| D-R-2 |              |                |                         |
| ...   |              |                |                         |

VOCABULARY CONTRACT: no blank cells. Defense argument column must not contain
"no reason to change" -- that is not a defense argument; name the specific
strategy.md rationale.

**Schema B -- Signal inventory**
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|

**Schema C -- Namespace audit (all 9 rows required)**
VOCABULARY CONTRACT: confirmed-zero counts written as 0 (not ??, not --, not ABSENT).

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

**Schema D -- Coverage map**
| Schema A label | Dimension | NEW signal finding | Assessment |
|----------------|-----------|--------------------|---------   |

**Schema E -- Additions**
| # | Dimension [NEW] | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before (Schema A text) | After | vs. NO CHANGE |
|---|-----------------|-------------------|--------------------|------------------------------|------------------------|-------|---------------|

MANDATORY: "Defense defeated" must cite exact Schema DR row number (e.g., "Row D-R-3").
A named defense without a row number does not satisfy this column.
"vs. NO CHANGE" must not contain any Banned output form listed above.
VOCABULARY CONTRACT: no blank cells in any column.

**Schema F -- Removals and Reprioritizations**
| # | Action | Dimension | Evidence artifact | Schema A ref (D-N) | Defense defeated (Row D-R-N) | Before (Schema A text) | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------------------|------------------------------|------------------------|-------|---------------|

Same requirements as Schema E: row-number citation required; no banned forms in
"vs. NO CHANGE"; no blank cells.

**Schema G -- Before/after diff**
| Dimension | Schema A ref | Before | After | Proposal ref |
|-----------|--------------|--------|-------|--------------|

**Schema H -- Conflict audit**
| Conflict ID | Signal A | Signal B | Dimension | Nature |
|-------------|----------|----------|-----------|--------|

---

## Phase 0 -- Defense register

Read `simulations/TOPICS.md` to find the strategy file. Read strategy.md.

Fill Schema A (all field rows, all D-N dimensions).

Fill Schema DR: assign D-R row numbers sequentially; write the specific defense
argument for each dimension from strategy.md. The defense argument must name the
specific strategy.md rationale, not a generic statement.

VOCABULARY CONTRACT check: run VIOLATION-1, VIOLATION-2, VIOLATION-3 on all cells
before declaring Schema DR complete.

[Gate 0 -- reproduce with all three fields filled:
  GATE 0 | Phase: Defense register
  Condition evaluated: [Schema DR has one row per Schema A dimension; D-R row
                        numbers present; defense arguments are non-generic;
                        no VOCABULARY CONTRACT violations]
  Result found: [D-R row count; all defenses name specific strategy.md rationale]
  STATUS: PASS / STOP]

Do not advance to Phase 1 without Gate 0 STATUS: PASS.

---

## Phase 1 -- Seal strategy.md

Fill the VERBATIM EVIDENCE BLOCK (Source dimension in D-N format matching Schema A).
Reproduce the STRATEGY.MD SEALED block with all six fields including Boundary.

VOCABULARY CONTRACT check on SEALED block: no field may be blank (?? is acceptable
for a field whose value has not yet been determined; -- is not acceptable for
required fields like "Strategy file" or "Schema A contains").

[Gate 1 -- reproduce with all three fields filled:
  GATE 1 | Phase: Verbatim block and seal
  Condition evaluated: [VERBATIM BLOCK has delimiters + D-N Source dimension;
                        SEALED block has 6 fields; Boundary states both halves;
                        no VOCABULARY CONTRACT violations]
  Result found: [Strategy date, D-N count, Source dimension label (D-N format),
                 SEAL present, Boundary: "Schema A complete. No signal artifacts
                 examined yet."]
  STATUS: PASS / STOP]

Do not advance to Phase 2 without Gate 1 STATUS: PASS.

---

## Phase 2 -- Signal inventory and namespace audit

List every artifact in `simulations/` whose filename contains the topic slug.
Fill Schema B and Schema C (all 9 rows -- zero-counts as 0, NEVER ABSENT, NEVER ??
for confirmed zero).

Write the HIGH-pressure namespace summary after Schema C.

NEW = artifact date strictly after Schema A Strategy date.
PRIOR = artifact date on or before Schema A Strategy date.

If no artifacts: "No signal artifacts found. Cannot run /topic:plan." Stop.
If all New = 0: "STRATEGY CURRENT -- no new signals since [Strategy date]." Stop.

[Gate 2 -- reproduce with all three fields filled:
  GATE 2 | Phase: Signal inventory
  Condition evaluated: [9 namespace rows; integer counts; no VOCABULARY CONTRACT
                        violations; no ABSENT; no ?? for confirmed zeros]
  Result found: [each namespace Total/New/pressure; HIGH-pressure namespaces listed]
  STATUS: PASS / STOP]

Do not advance to Phase 3 without Gate 2 STATUS: PASS.

---

## Phase 3 -- Delta partition and mandatory count sentence

Partition Schema B into NEW and PRIOR.

Write exactly:
  "Strategy was written on [DATE]. [N] artifacts are NEW. [M] are PRIOR."

BANNED COUNT FORMS (any of these strings in place of [N] or [M] is a gate failure):
  "a few"
  "several"
  "some"
  "multiple"
  "many"

[N] and [M] must be integers.

[Gate 3 -- reproduce with all three fields filled:
  GATE 3 | Phase: Delta partition
  Condition evaluated: [mandatory sentence present; [N] and [M] are integers;
                        no BANNED COUNT FORMS]
  Result found: [N NEW artifacts (integer), M PRIOR artifacts (integer)]
  STATUS: PASS / STOP]

Do not advance to Phase 4 without Gate 3 STATUS: PASS.

---

## Phase 4 -- Read NEW artifacts

Read each NEW artifact. Write a synthesis paragraph (4-6 sentences). Name at least
two artifact filenames by their exact filenames.

[Gate 4 -- reproduce with all three fields filled:
  GATE 4 | Phase: New artifact synthesis
  Condition evaluated: [paragraph; at least two exact filenames cited]
  Result found: [specific filenames]
  STATUS: PASS / STOP]

Do not advance to Phase 5 without Gate 4 STATUS: PASS.

---

## Phase 5 -- Coverage map and proposals

Fill Schema D. Default verdict: NO CHANGE. Burden of proof is on change.

Fill Schemas E and F. For every proposal row:
- Evidence artifact: from a NEW artifact, HIGH-pressure namespace only
- Schema A ref (D-N): specific locked dimension row label
- Defense defeated: cite "Row D-R-[N]" from Schema DR -- the exact row number.
  A named defense without a row number does not satisfy this column.
- Before: reproduce Schema A D-N text. If Before cannot be written from Schema A
  without re-opening strategy.md, the proposal is a SEAL violation; drop it.
- vs. NO CHANGE: name a specific consequence of leaving the strategy unchanged.
  Check cell against BANNED OUTPUT FORMS above before presenting. Any banned form
  disqualifies the row -- rewrite before Gate 5.

VOCABULARY CONTRACT: run VIOLATION-1, VIOLATION-2, VIOLATION-3 on all Schema E
and F cells before presenting.

Null declarations (each type labeled separately; check against BANNED OUTPUT FORMS):
  ADDITIONS: none -- [specific reason, not "no new signals" or "nothing to add"] | or [N] proposed
  REMOVALS: none -- [specific reason, not "nothing to remove"] | or [N] proposed
  REPRIORITIZATIONS: none -- [specific reason, not "nothing to reprioritize"] | or [N] proposed

Fill Schemas G and H. VOCABULARY CONTRACT: no blank cells.

[Gate 5 -- reproduce with all three fields filled:
  GATE 5 | Phase: Proposals complete
  Condition evaluated: [all three null declarations present; "Defense defeated"
                        column has D-R row numbers in every non-null row; no
                        BANNED OUTPUT FORMS in vs. NO CHANGE or null reasons;
                        no VOCABULARY CONTRACT violations; no Before requires
                        strategy.md re-read]
  Result found: [N additions / N removals / N reprioritizations (integers)]
  STATUS: PASS / STOP]

Do not advance to Phase 6 without Gate 5 STATUS: PASS.

---

## Phase 6 -- Confirmation gate

Display all schemas (including VERBATIM EVIDENCE BLOCK and STRATEGY.MD SEALED
block from Phase 1).

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
  Condition evaluated: [PENDING CONFIRMATION block with integer proposal counts]
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

Stop. Write nothing further until the user replies.

---

## Apply (triggered by YES or REVISED)

The SEAL lifts when the user replies. Write exactly the confirmed changes to
strategy.md. No additional edits. Confirm:
"strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```
