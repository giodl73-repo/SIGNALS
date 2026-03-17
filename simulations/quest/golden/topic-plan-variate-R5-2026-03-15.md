# topic-plan Skill Variations -- Round 5 (2026-03-15)

Rubric: v5 (C-01 through C-21; C-19 Source-anchored verbatim quotation, C-20
Change-pressure proposal filter, C-21 SEAL violation as named output category are
the three new aspirational criteria added from Round 4 excellence signals)

Round 4 recap: V-05 (full combination: VERBATIM BLOCK + change-pressure table +
STRATEGY.MD SEALED block) scored highest. C-21 (SEAL violation as named output
category) was addressed by V-03/V-05's SEALED block. Five failure modes remained:
- C-15 was the universal miss across all five R4 variations: the SEALED block
  asserts "commitment complete" but omits "no signal artifacts read yet." These
  are two distinct claims; the SEALED block's five fields cover only the first
  (C-18/C-21). The second half (C-15) is unrepresented as a named field.
- C-19: V-01's VERBATIM EVIDENCE BLOCK names a Source element (dimension name,
  scope clause, criteria statement) but does not require it to map to a D-N row
  label. A reader verifying a "Before" value needs to find the D-N row, not just
  the element name.
- C-20: V-02/V-04/V-05's HIGH-pressure list after Schema C names which namespaces
  are HIGH, but Phase 5 instructions say "evidence from HIGH-pressure namespace
  only" without a visible PROPOSAL SCOPE block that a reader can check against the
  HIGH-pressure list without re-running the inventory.

Round 5 targets: C-15 (universal miss -- all five R4 variations failed), C-19
(Source element must resolve to a D-N label), C-20 (HIGH-pressure list must
visibly gate Phase 5 via a named PROPOSAL SCOPE artifact).

Three single-axis variations (V-01, V-02, V-03), then two combinations (V-04,
V-05).

---

## V-01: Boundary Field in SEALED Block -- Temporal Boundary Attestation

**Variation axis**: Lifecycle emphasis -- the STRATEGY.MD SEALED block gains a
sixth mandatory `Boundary:` field that states both halves of the C-15 attestation
in a single named field: "Schema A complete. No signal artifacts examined yet."

**Hypothesis**: C-15 was missed universally in R4 because the five-field SEALED
block (V-03/V-05) exhaustively covers the commitment side of the ordering contract
(what was sealed, what is prohibited, what constitutes a violation, when the
prohibition lifts, how many dimensions were committed) but treats the scan side as
an implicit consequence rather than an explicit claim. The model fills the SEALED
block from a template with five named fields; a sixth field named `Boundary:` must
also be filled, and its value has two required halves. A blank or partial `Boundary:`
field is visibly wrong in a way that omitted prose is not. The Boundary field makes
C-15 structurally parallel to C-18 and C-21: all three are named fields in the same
SEALED block, all three must be non-empty for Gate 1 to pass.

```
You are running /topic:plan for the topic named in the user's message.

---

## Pre-committed schemas (fill in order -- no schema may be skipped or replaced
## with prose)

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

VERBATIM EVIDENCE BLOCK (required output artifact -- reproduce with both
delimiters and Source element filled):

  ===VERBATIM START===
  [paste exact text from strategy.md here -- no paraphrase, no summary,
   no restatement; copy-paste the exact words as they appear in the file]
  ===VERBATIM END===
  Source element: [name the specific dimension, scope clause, or criteria
                   statement this text appears under in strategy.md]

After Schema A and the VERBATIM EVIDENCE BLOCK are written, reproduce the
STRATEGY.MD SEALED block below with all six fields completed:

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
| Schema A label | Dimension | NEW signal finding | Assessment                      |
|----------------|-----------|--------------------|---------------------------------|

**Schema E -- Additions**
| # | Dimension [NEW] | Evidence artifact | Schema A ref (D-N) | Before (Schema A text) | After | vs. NO CHANGE |
|---|-----------------|-------------------|---------------------|------------------------|-------|---------------|

**Schema F -- Removals and Reprioritizations**
| # | Action | Dimension | Evidence artifact | Schema A ref (D-N) | Before (Schema A text) | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|---------------------|------------------------|-------|---------------|

**Schema G -- Before/after diff**
| Dimension | Schema A ref | Before | After | Proposal ref |
|-----------|-------------|--------|-------|--------------|

**Schema H -- Conflict audit**
| Conflict ID | Signal A | Signal B | Dimension | Nature |
|-------------|----------|----------|-----------|--------|

---

## Phase 1 -- Read strategy.md

Read `simulations/TOPICS.md` to find the strategy file. Read strategy.md.

Fill Schema A: all field rows, all D-N dimension rows, VERBATIM EVIDENCE BLOCK
(both delimiters intact, Source element named), and STRATEGY.MD SEALED block
(all six fields filled -- Boundary field must state both halves).

All three artifacts must appear in the Phase 1 output before Gate 1.

[Gate 1 -- reproduce with all three fields filled:
  GATE 1 | Phase: Strategy commitment, verbatim block, and seal
  Condition evaluated: [Schema A filled; VERBATIM BLOCK has delimiters + Source;
                        STRATEGY.MD SEALED block has all 6 fields filled including
                        Boundary field with both halves present]
  Result found: [Strategy date, D-N count, VERBATIM Source element, "SEAL present
                 with Boundary: Schema A complete. No signal artifacts examined yet."]
  STATUS: PASS / STOP]

Do not begin Phase 2 until Gate 1 shows STATUS: PASS.

---

## Phase 2 -- Signal inventory and namespace audit

List every artifact in `simulations/` whose filename contains the topic slug.
Fill Schema B (all artifacts). Fill Schema C (all 9 rows -- zero-counts for
absent namespaces, NEVER write ABSENT).

Write the HIGH-pressure namespace summary immediately after Schema C.

NEW = artifact date strictly after Schema A Strategy date.
PRIOR = date on or before Schema A Strategy date.

If no artifacts: "No signal artifacts found. Cannot run /topic:plan." Stop.
If no HIGH-pressure namespaces (all New = 0): "STRATEGY CURRENT -- no new
signals since [Strategy date]. No update warranted." Stop.

[Gate 2 -- reproduce with all three fields filled:
  GATE 2 | Phase: Signal inventory
  Condition evaluated: [all 9 namespace rows with numeric counts and pressure ratings;
                        ABSENT not used anywhere in Schema C]
  Result found: [each namespace with Total/New/pressure; HIGH-pressure list]
  STATUS: PASS / STOP]

Do not begin Phase 3 until Gate 2 shows STATUS: PASS.

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
Do not begin Phase 4 until Gate 3 shows STATUS: PASS.

---

## Phase 4 -- Read NEW artifacts

Read each NEW artifact. The SEAL is in force -- strategy.md may not be re-opened.

Write a short paragraph (4-6 sentences) on collective findings.
Name at least two artifact filenames. Do not compare to Schema A yet.

[Gate 4 -- reproduce with all three fields filled:
  GATE 4 | Phase: New artifact synthesis
  Condition evaluated: [paragraph written and at least two filenames cited]
  Result found: [specific filenames cited]
  STATUS: PASS / STOP]

---

## Phase 5 -- Coverage map and proposals

Fill Schema D. For NEW artifact dimensions absent from Schema A, add a row
labeled "NEW DIMENSION".

Default verdict: NO CHANGE. Burden of proof is on change.

Fill Schemas E and F. For every proposal row:
- Evidence must be in Phase 3 NEW list (HIGH-pressure namespace only)
- Schema A ref (D-N) must name a specific locked dimension
- Before must reproduce Schema A D-N text -- SEAL violation if text requires
  re-reading strategy.md; if Before cannot be written from Schema A, drop
  the proposal
- vs. NO CHANGE must name a specific consequence of leaving strategy unchanged

Null declarations (each type labeled separately):
  ADDITIONS: none -- [reason] | or [N] proposed
  REMOVALS: none -- [reason] | or [N] proposed
  REPRIORITIZATIONS: none -- [reason] | or [N] proposed

Fill Schemas G and H.

[Gate 5 -- reproduce with all three fields filled:
  GATE 5 | Phase: Proposals complete
  Condition evaluated: [all three null declarations present; Schema G row count;
                        no Before value requires a strategy.md re-read]
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

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

## V-02: D-N Tagged Source in VERBATIM Block -- Source-Anchored Verbatim Quotation

**Variation axis**: Output format -- the VERBATIM EVIDENCE BLOCK's Source element
is replaced by a two-part `Source dimension:` field that combines the D-N row
label with the dimension name, e.g., `Source dimension: D-3 -- sequencing`.

**Hypothesis**: V-01/V-05's `Source element: [name the specific dimension...]`
requires the model to name a semantic entity (a scope clause, a dimension name, a
criteria statement) but does not require it to resolve to a D-N row label. C-19
requires the quote to be tagged to a named dimension via a Source element, where
"named dimension" means the D-N label from Schema A, making "Before" values cross-
checkable. A reader verifying a "Before" value in Schema E (which says `Schema A
ref (D-N): D-3`) needs to find the verbatim quote at the D-3 row; a Source element
that names only "sequencing" requires the reader to match element names rather than
follow a D-N pointer. Replacing `Source element:` with `Source dimension: D-[N] --
[dimension name]` creates a direct pointer: the Source dimension field in the
VERBATIM BLOCK and the Schema A ref column in Schema E cite the same D-N label.
A mismatch between the two is immediately detectable.

```
You are running /topic:plan for the topic named in the user's message.

---

## Pre-committed schemas (fill in order -- no schema may be skipped or replaced
## with prose)

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

VERBATIM EVIDENCE BLOCK (required output artifact -- reproduce with both
delimiters and Source dimension field filled):

  ===VERBATIM START===
  [paste exact text from strategy.md here -- no paraphrase, no summary,
   no restatement; copy-paste the exact words as they appear in the file]
  ===VERBATIM END===
  Source dimension: D-[N] -- [dimension name]
  (The D-N label must match a row in the Schema A dimensions table above.
   A Source dimension field that does not match a D-N label fails this block.)

After Schema A and the VERBATIM EVIDENCE BLOCK are written, reproduce the
STRATEGY.MD SEALED block below with all five fields completed:

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
  ================================================================

Schema A is LOCKED and SEALED after Gate 1. All "Before" values in Schemas E
and F must trace to a D-N row in the locked Schema A.

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
| Schema A label | Dimension | NEW signal finding | Assessment                      |
|----------------|-----------|--------------------|---------------------------------|

**Schema E -- Additions**
| # | Dimension [NEW] | Evidence artifact | Schema A ref (D-N) | Before (Schema A text) | After | vs. NO CHANGE |
|---|-----------------|-------------------|---------------------|------------------------|-------|---------------|

**Schema F -- Removals and Reprioritizations**
| # | Action | Dimension | Evidence artifact | Schema A ref (D-N) | Before (Schema A text) | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|---------------------|------------------------|-------|---------------|

**Schema G -- Before/after diff**
| Dimension | Schema A ref | Before | After | Proposal ref |
|-----------|-------------|--------|-------|--------------|

**Schema H -- Conflict audit**
| Conflict ID | Signal A | Signal B | Dimension | Nature |
|-------------|----------|----------|-----------|--------|

---

## Phase 1 -- Read strategy.md

Read `simulations/TOPICS.md` to find the strategy file. Read strategy.md.

Fill Schema A: all field rows, all D-N dimension rows, VERBATIM EVIDENCE BLOCK
(both delimiters intact, Source dimension field filled as `D-[N] -- [name]`),
and STRATEGY.MD SEALED block (all five fields filled).

All three artifacts must appear in the Phase 1 output before Gate 1.

[Gate 1 -- reproduce with all three fields filled:
  GATE 1 | Phase: Strategy commitment, verbatim block, and seal
  Condition evaluated: [Schema A filled; VERBATIM BLOCK has delimiters + Source
                        dimension in D-N format matching a Schema A row; STRATEGY.MD
                        SEALED block has all 5 fields filled]
  Result found: [Strategy date, D-N count, VERBATIM Source dimension label (e.g.,
                 "D-3 -- sequencing"), "SEAL present"]
  STATUS: PASS / STOP]

Do not begin Phase 2 until Gate 1 shows STATUS: PASS.

---

## Phase 2 -- Signal inventory and namespace audit

List every artifact in `simulations/` whose filename contains the topic slug.
Fill Schema B (all artifacts). Fill Schema C (all 9 rows -- zero-counts for
absent namespaces, NEVER write ABSENT).

Write the HIGH-pressure namespace summary immediately after Schema C.

NEW = artifact date strictly after Schema A Strategy date.
PRIOR = date on or before Schema A Strategy date.

If no artifacts: "No signal artifacts found. Cannot run /topic:plan." Stop.
If no HIGH-pressure namespaces (all New = 0): "STRATEGY CURRENT -- no new
signals since [Strategy date]. No update warranted." Stop.

[Gate 2 -- reproduce with all three fields filled:
  GATE 2 | Phase: Signal inventory
  Condition evaluated: [all 9 namespace rows with numeric counts and pressure ratings;
                        ABSENT not used anywhere in Schema C]
  Result found: [each namespace with Total/New/pressure; HIGH-pressure list]
  STATUS: PASS / STOP]

Do not begin Phase 3 until Gate 2 shows STATUS: PASS.

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
Do not begin Phase 4 until Gate 3 shows STATUS: PASS.

---

## Phase 4 -- Read NEW artifacts

Read each NEW artifact. The SEAL is in force -- strategy.md may not be re-opened.

Write a short paragraph (4-6 sentences) on collective findings.
Name at least two artifact filenames. Do not compare to Schema A yet.

[Gate 4 -- reproduce with all three fields filled:
  GATE 4 | Phase: New artifact synthesis
  Condition evaluated: [paragraph written and at least two filenames cited]
  Result found: [specific filenames cited]
  STATUS: PASS / STOP]

---

## Phase 5 -- Coverage map and proposals

Fill Schema D. For NEW artifact dimensions absent from Schema A, add a row
labeled "NEW DIMENSION".

Default verdict: NO CHANGE. Burden of proof is on change.

Fill Schemas E and F. For every proposal row:
- Evidence must be in Phase 3 NEW list (HIGH-pressure namespace only)
- Schema A ref (D-N) must name a specific locked dimension; the D-N label must
  match either a Source dimension field from the VERBATIM BLOCK or a D-N row in
  Schema A -- these are two independent cross-checks on the same label
- Before must reproduce Schema A D-N text -- SEAL violation if text requires
  re-reading strategy.md; if Before cannot be written from Schema A, drop
  the proposal
- vs. NO CHANGE must name a specific consequence of leaving strategy unchanged

Null declarations (each type labeled separately):
  ADDITIONS: none -- [reason] | or [N] proposed
  REMOVALS: none -- [reason] | or [N] proposed
  REPRIORITIZATIONS: none -- [reason] | or [N] proposed

Fill Schemas G and H.

[Gate 5 -- reproduce with all three fields filled:
  GATE 5 | Phase: Proposals complete
  Condition evaluated: [all three null declarations present; Schema G row count;
                        each Schema A ref matches a D-N label in locked Schema A]
  Result found: [N additions / N removals / N reprioritizations]
  STATUS: PASS / STOP]

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

## V-03: PROPOSAL SCOPE Block -- Change-Pressure Proposal Filter

**Variation axis**: Role sequence -- after Schema C is filled and the HIGH-pressure
list is written, the skill emits a named PROPOSAL SCOPE block before Phase 5 begins.
The block names the HIGH-pressure namespaces from Schema C and declares all others
excluded from the proposal phase. Phase 5 opens by reproducing the PROPOSAL SCOPE
header as a visible constraint on what may generate proposals.

**Hypothesis**: V-02/V-04/V-05 from R4 compute change pressure per namespace (C-17)
and list HIGH-pressure namespaces after Schema C, then instruct Phase 5 to restrict
evidence to HIGH-pressure namespaces "only." C-20 requires more than a prose
restriction: HIGH-pressure namespaces must be explicitly listed and the proposal
phase must visibly restrict its scope to them, so a reader can independently verify
that proposal volume is proportionate to HIGH-pressure namespace count without
re-running the inventory. The gap is that Phase 5's "HIGH-pressure namespace only"
instruction is a filter rule embedded in prose; it can be satisfied without emitting
a visible PROPOSAL SCOPE artifact. A named PROPOSAL SCOPE block, placed between
Gate 4 and the Schema D fill instruction, makes the filter a visible output artifact:
the reader can count proposals and verify they cite only namespaces listed in the
PROPOSAL SCOPE. A proposal citing a LOW or NONE namespace is a SCOPE violation,
auditable from the output alone.

```
You are running /topic:plan for the topic named in the user's message.

---

## Pre-committed schemas (fill in order -- no schema may be skipped or replaced
## with prose)

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

VERBATIM EVIDENCE BLOCK (required output artifact -- reproduce with both
delimiters and Source element filled):

  ===VERBATIM START===
  [paste exact text from strategy.md here -- no paraphrase, no summary,
   no restatement; copy-paste the exact words as they appear in the file]
  ===VERBATIM END===
  Source element: [name the specific dimension, scope clause, or criteria
                   statement this text appears under in strategy.md]

After Schema A and the VERBATIM EVIDENCE BLOCK are written, reproduce the
STRATEGY.MD SEALED block below with all five fields completed:

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
  ================================================================

Schema A is LOCKED and SEALED after Gate 1. All "Before" values in Schemas E
and F must trace to a D-N row in the locked Schema A.

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

After Schema C is complete, write the PROPOSAL SCOPE block:

  ================================================================
  PROPOSAL SCOPE
  HIGH-pressure namespaces (New > 0): [list names, or "none"]
  Excluded from proposals: [all remaining namespaces not listed above]
  Rule: Phase 5 proposals may only cite evidence from HIGH-pressure
        namespaces. A proposal row citing any excluded namespace is a
        SCOPE violation and must be dropped.
  ================================================================

**Schema D -- Coverage map**
| Schema A label | Dimension | NEW signal finding | Assessment                      |
|----------------|-----------|--------------------|---------------------------------|

**Schema E -- Additions**
| # | Dimension [NEW] | Evidence artifact | Schema A ref (D-N) | Before (Schema A text) | After | vs. NO CHANGE |
|---|-----------------|-------------------|---------------------|------------------------|-------|---------------|

**Schema F -- Removals and Reprioritizations**
| # | Action | Dimension | Evidence artifact | Schema A ref (D-N) | Before (Schema A text) | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|---------------------|------------------------|-------|---------------|

**Schema G -- Before/after diff**
| Dimension | Schema A ref | Before | After | Proposal ref |
|-----------|-------------|--------|-------|--------------|

**Schema H -- Conflict audit**
| Conflict ID | Signal A | Signal B | Dimension | Nature |
|-------------|----------|----------|-----------|--------|

---

## Phase 1 -- Read strategy.md

Read `simulations/TOPICS.md` to find the strategy file. Read strategy.md.

Fill Schema A: all field rows, all D-N dimension rows, VERBATIM EVIDENCE BLOCK
(both delimiters intact, Source element named), and STRATEGY.MD SEALED block
(all five fields filled).

All three artifacts must appear in the Phase 1 output before Gate 1.

[Gate 1 -- reproduce with all three fields filled:
  GATE 1 | Phase: Strategy commitment, verbatim block, and seal
  Condition evaluated: [Schema A filled; VERBATIM BLOCK has delimiters + Source;
                        STRATEGY.MD SEALED block has all 5 fields filled]
  Result found: [Strategy date, D-N count, VERBATIM Source element, "SEAL present"]
  STATUS: PASS / STOP]

Do not begin Phase 2 until Gate 1 shows STATUS: PASS.

---

## Phase 2 -- Signal inventory and namespace audit

List every artifact in `simulations/` whose filename contains the topic slug.
Fill Schema B (all artifacts). Fill Schema C (all 9 rows -- zero-counts for
absent namespaces, NEVER write ABSENT).

Write the PROPOSAL SCOPE block immediately after Schema C.

NEW = artifact date strictly after Schema A Strategy date.
PRIOR = date on or before Schema A Strategy date.

If no artifacts: "No signal artifacts found. Cannot run /topic:plan." Stop.
If no HIGH-pressure namespaces (all New = 0): "STRATEGY CURRENT -- no new
signals since [Strategy date]. No update warranted." Stop.

[Gate 2 -- reproduce with all three fields filled:
  GATE 2 | Phase: Signal inventory and scope declaration
  Condition evaluated: [all 9 namespace rows with numeric counts and pressure ratings;
                        PROPOSAL SCOPE block written with HIGH-pressure and excluded lists]
  Result found: [each namespace with Total/New/pressure; PROPOSAL SCOPE namespaces]
  STATUS: PASS / STOP]

Do not begin Phase 3 until Gate 2 shows STATUS: PASS.

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
Do not begin Phase 4 until Gate 3 shows STATUS: PASS.

---

## Phase 4 -- Read NEW artifacts

Read each NEW artifact. The SEAL is in force -- strategy.md may not be re-opened.

Write a short paragraph (4-6 sentences) on collective findings.
Name at least two artifact filenames. Do not compare to Schema A yet.

[Gate 4 -- reproduce with all three fields filled:
  GATE 4 | Phase: New artifact synthesis
  Condition evaluated: [paragraph written and at least two filenames cited]
  Result found: [specific filenames cited]
  STATUS: PASS / STOP]

---

## Phase 5 -- Coverage map and proposals

PROPOSAL SCOPE active: [reproduce HIGH-pressure namespaces from the PROPOSAL
SCOPE block above]. Only evidence from these namespaces may drive proposals.

Fill Schema D. For NEW artifact dimensions absent from Schema A, add a row
labeled "NEW DIMENSION".

Default verdict: NO CHANGE. Burden of proof is on change.

Fill Schemas E and F. For every proposal row:
- Evidence artifact must appear in Phase 3 NEW list AND belong to a namespace
  listed in the PROPOSAL SCOPE block; if not, drop the proposal
- Schema A ref (D-N) must name a specific locked dimension
- Before must reproduce Schema A D-N text -- SEAL violation if text requires
  re-reading strategy.md; if Before cannot be written from Schema A, drop
  the proposal
- vs. NO CHANGE must name a specific consequence of leaving strategy unchanged

Null declarations (each type labeled separately):
  ADDITIONS: none -- [reason] | or [N] proposed
  REMOVALS: none -- [reason] | or [N] proposed
  REPRIORITIZATIONS: none -- [reason] | or [N] proposed

Fill Schemas G and H.

[Gate 5 -- reproduce with all three fields filled:
  GATE 5 | Phase: Proposals complete
  Condition evaluated: [all three null declarations present; all proposal evidence
                        verified to be in PROPOSAL SCOPE namespaces; Schema G row count]
  Result found: [N additions / N removals / N reprioritizations; SCOPE namespace count]
  STATUS: PASS / STOP]

---

## Phase 6 -- Confirmation gate

Display all schemas (including VERBATIM EVIDENCE BLOCK, STRATEGY.MD SEALED block,
and PROPOSAL SCOPE block from Phases 1-2).

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

## V-04: Combination V-01 + V-03 -- Boundary Field + PROPOSAL SCOPE Block

**Variation axis**: Output format (two axes combined) -- the STRATEGY.MD SEALED
block gains a sixth `Boundary:` field (V-01, targeting C-15), and a named
PROPOSAL SCOPE block is written after Schema C to gate Phase 5 (V-03, targeting
C-20).

**Hypothesis**: C-15 (Boundary attestation) and C-20 (change-pressure proposal
filter) both involve named output blocks that encode an ordering contract: C-15
says "strategy.md committed, no artifacts seen yet"; C-20 says "these namespaces
have pressure, others are excluded from proposals." The two blocks appear at
different temporal positions -- the Boundary field at the SEAL (end of Phase 1),
the PROPOSAL SCOPE block after Schema C (end of Phase 2) -- and are structurally
independent: one is a field inside the SEALED block; the other is a freestanding
output artifact. Together they make two previously implicit ordering constraints
auditable from the output: the commitment-before-scan constraint (C-15) and the
pressure-before-proposals constraint (C-20). A reader can verify both without
access to the execution trace.

```
You are running /topic:plan for the topic named in the user's message.

---

## Pre-committed schemas (fill in order -- no schema may be skipped or replaced
## with prose)

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

VERBATIM EVIDENCE BLOCK (required output artifact -- reproduce with both
delimiters and Source element filled):

  ===VERBATIM START===
  [paste exact text from strategy.md here -- no paraphrase, no summary,
   no restatement; copy-paste the exact words as they appear in the file]
  ===VERBATIM END===
  Source element: [name the specific dimension, scope clause, or criteria
                   statement this text appears under in strategy.md]

After Schema A and the VERBATIM EVIDENCE BLOCK are written, reproduce the
STRATEGY.MD SEALED block below with all six fields completed:

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

After Schema C is complete, write the PROPOSAL SCOPE block:

  ================================================================
  PROPOSAL SCOPE
  HIGH-pressure namespaces (New > 0): [list names, or "none"]
  Excluded from proposals: [all remaining namespaces not listed above]
  Rule: Phase 5 proposals may only cite evidence from HIGH-pressure
        namespaces. A proposal row citing any excluded namespace is a
        SCOPE violation and must be dropped.
  ================================================================

**Schema D -- Coverage map**
| Schema A label | Dimension | NEW signal finding | Assessment                      |
|----------------|-----------|--------------------|---------------------------------|

**Schema E -- Additions**
| # | Dimension [NEW] | Evidence artifact | Schema A ref (D-N) | Before (Schema A text) | After | vs. NO CHANGE |
|---|-----------------|-------------------|---------------------|------------------------|-------|---------------|

**Schema F -- Removals and Reprioritizations**
| # | Action | Dimension | Evidence artifact | Schema A ref (D-N) | Before (Schema A text) | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|---------------------|------------------------|-------|---------------|

**Schema G -- Before/after diff**
| Dimension | Schema A ref | Before | After | Proposal ref |
|-----------|-------------|--------|-------|--------------|

**Schema H -- Conflict audit**
| Conflict ID | Signal A | Signal B | Dimension | Nature |
|-------------|----------|----------|-----------|--------|

---

## Phase 1 -- Read strategy.md

Read `simulations/TOPICS.md` to find the strategy file. Read strategy.md.

Fill Schema A: all field rows, all D-N dimension rows, VERBATIM EVIDENCE BLOCK
(both delimiters intact, Source element named), and STRATEGY.MD SEALED block
(all six fields filled -- Boundary field must state both halves).

All three artifacts must appear in the Phase 1 output before Gate 1.

[Gate 1 -- reproduce with all three fields filled:
  GATE 1 | Phase: Strategy commitment, verbatim block, and seal
  Condition evaluated: [Schema A filled; VERBATIM BLOCK has delimiters + Source;
                        STRATEGY.MD SEALED block has all 6 fields including Boundary
                        field: "Schema A complete. No signal artifacts examined yet."]
  Result found: [Strategy date, D-N count, VERBATIM Source element, "SEAL + Boundary
                 confirmed"]
  STATUS: PASS / STOP]

Do not begin Phase 2 until Gate 1 shows STATUS: PASS.

---

## Phase 2 -- Signal inventory and namespace audit

List every artifact in `simulations/` whose filename contains the topic slug.
Fill Schema B (all artifacts). Fill Schema C (all 9 rows -- zero-counts for
absent namespaces, NEVER write ABSENT).

Write the PROPOSAL SCOPE block immediately after Schema C.

NEW = artifact date strictly after Schema A Strategy date.
PRIOR = date on or before Schema A Strategy date.

If no artifacts: "No signal artifacts found. Cannot run /topic:plan." Stop.
If no HIGH-pressure namespaces (all New = 0): "STRATEGY CURRENT -- no new
signals since [Strategy date]. No update warranted." Stop.

[Gate 2 -- reproduce with all three fields filled:
  GATE 2 | Phase: Signal inventory and scope declaration
  Condition evaluated: [all 9 namespace rows with numeric counts and pressure ratings;
                        PROPOSAL SCOPE block written with HIGH-pressure and excluded lists]
  Result found: [each namespace with Total/New/pressure; PROPOSAL SCOPE namespaces]
  STATUS: PASS / STOP]

Do not begin Phase 3 until Gate 2 shows STATUS: PASS.

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
Do not begin Phase 4 until Gate 3 shows STATUS: PASS.

---

## Phase 4 -- Read NEW artifacts

Read each NEW artifact. The SEAL is in force -- strategy.md may not be re-opened.

Write a short paragraph (4-6 sentences) on collective findings.
Name at least two artifact filenames. Do not compare to Schema A yet.

[Gate 4 -- reproduce with all three fields filled:
  GATE 4 | Phase: New artifact synthesis
  Condition evaluated: [paragraph written and at least two filenames cited]
  Result found: [specific filenames cited]
  STATUS: PASS / STOP]

---

## Phase 5 -- Coverage map and proposals

PROPOSAL SCOPE active: [reproduce HIGH-pressure namespaces from the PROPOSAL
SCOPE block above]. Only evidence from these namespaces may drive proposals.

Fill Schema D. For NEW artifact dimensions absent from Schema A, add a row
labeled "NEW DIMENSION".

Default verdict: NO CHANGE. Burden of proof is on change.

Fill Schemas E and F. For every proposal row:
- Evidence artifact must appear in Phase 3 NEW list AND belong to a namespace
  listed in the PROPOSAL SCOPE block; if not, drop the proposal
- Schema A ref (D-N) must name a specific locked dimension
- Before must reproduce Schema A D-N text -- SEAL violation if text requires
  re-reading strategy.md; if Before cannot be written from Schema A, drop
  the proposal
- vs. NO CHANGE must name a specific consequence of leaving strategy unchanged

Null declarations (each type labeled separately):
  ADDITIONS: none -- [reason] | or [N] proposed
  REMOVALS: none -- [reason] | or [N] proposed
  REPRIORITIZATIONS: none -- [reason] | or [N] proposed

Fill Schemas G and H.

[Gate 5 -- reproduce with all three fields filled:
  GATE 5 | Phase: Proposals complete
  Condition evaluated: [all three null declarations present; all proposal evidence
                        verified to be in PROPOSAL SCOPE namespaces; Schema G row count]
  Result found: [N additions / N removals / N reprioritizations; SCOPE namespace count]
  STATUS: PASS / STOP]

---

## Phase 6 -- Confirmation gate

Display all schemas (including VERBATIM EVIDENCE BLOCK, STRATEGY.MD SEALED block,
and PROPOSAL SCOPE block).

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

## V-05: Full Combination V-01 + V-02 + V-03 -- All Three New v5 Axes

**Variation axis**: All three single-axis variations combined -- Boundary field in
SEALED block (V-01, targeting C-15), D-N tagged Source dimension in VERBATIM BLOCK
(V-02, targeting C-19), and PROPOSAL SCOPE block gating Phase 5 (V-03, targeting
C-20).

**Hypothesis**: The three new v5 criteria (C-15, C-19, C-20) each address a
different auditable ordering claim: C-15 asserts the pre-scan state (commitment
complete, no artifacts seen), C-19 asserts the verbatim quote maps to a specific
D-N row (making "Before" cross-checkable), C-20 asserts that change pressure
computed in Phase 2 explicitly scopes Phase 5 (not just restricts it by prose
instruction). All three claims are currently unrepresented as named output
artifacts in R4 V-05. Adding all three to the same prompt makes the commitment
protocol fully self-documenting: a reader can verify the pre-scan state (SEALED
Boundary field), the evidence provenance (Source dimension D-N), and the proposal
scope (PROPOSAL SCOPE block) without re-executing the skill or inspecting traces.
The three additions are structurally independent -- each occupies a different output
artifact (SEALED block field, VERBATIM BLOCK field, freestanding SCOPE block) and
enforces a different ordering property -- so combining them incurs no redundancy.

```
You are running /topic:plan for the topic named in the user's message.

---

## Pre-committed schemas (fill in order -- no schema may be skipped or replaced
## with prose)

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

VERBATIM EVIDENCE BLOCK (required output artifact -- reproduce with both
delimiters and Source dimension field filled):

  ===VERBATIM START===
  [paste exact text from strategy.md here -- no paraphrase, no summary,
   no restatement; copy-paste the exact words as they appear in the file]
  ===VERBATIM END===
  Source dimension: D-[N] -- [dimension name]
  (The D-N label must match a row in the Schema A dimensions table above.
   A Source dimension that does not match a D-N label fails this block.)

After Schema A and the VERBATIM EVIDENCE BLOCK are written, reproduce the
STRATEGY.MD SEALED block below with all six fields completed:

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
a reader can independently verify it against the Source dimension in the VERBATIM
EVIDENCE BLOCK without re-reading strategy.md.

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

After Schema C is complete, write the PROPOSAL SCOPE block:

  ================================================================
  PROPOSAL SCOPE
  HIGH-pressure namespaces (New > 0): [list names, or "none"]
  Excluded from proposals: [all remaining namespaces not listed above]
  Rule: Phase 5 proposals may only cite evidence from HIGH-pressure
        namespaces. A proposal row citing any excluded namespace is a
        SCOPE violation and must be dropped.
  ================================================================

**Schema D -- Coverage map**
| Schema A label | Dimension | NEW signal finding | Assessment                      |
|----------------|-----------|--------------------|---------------------------------|

**Schema E -- Additions**
| # | Dimension [NEW] | Evidence artifact | Schema A ref (D-N) | Before (Schema A text) | After | vs. NO CHANGE |
|---|-----------------|-------------------|---------------------|------------------------|-------|---------------|

**Schema F -- Removals and Reprioritizations**
| # | Action | Dimension | Evidence artifact | Schema A ref (D-N) | Before (Schema A text) | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|---------------------|------------------------|-------|---------------|

**Schema G -- Before/after diff**
| Dimension | Schema A ref | Before | After | Proposal ref |
|-----------|-------------|--------|-------|--------------|

**Schema H -- Conflict audit**
| Conflict ID | Signal A | Signal B | Dimension | Nature |
|-------------|----------|----------|-----------|--------|

---

## Phase 1 -- Read strategy.md

Read `simulations/TOPICS.md` to find the strategy file. Read strategy.md.

Fill Schema A: all field rows, all D-N dimension rows, VERBATIM EVIDENCE BLOCK
(both delimiters intact, Source dimension field in `D-[N] -- [name]` format
matching a Schema A row), and STRATEGY.MD SEALED block (all six fields filled --
Boundary field must state both halves).

All three artifacts must appear in the Phase 1 output before Gate 1.

[Gate 1 -- reproduce with all three fields filled:
  GATE 1 | Phase: Strategy commitment, verbatim block, and seal
  Condition evaluated: [Schema A filled; VERBATIM BLOCK has delimiters + Source
                        dimension in D-N format matching a Schema A row; STRATEGY.MD
                        SEALED block has all 6 fields filled including Boundary field:
                        "Schema A complete. No signal artifacts examined yet."]
  Result found: [Strategy date, D-N count, VERBATIM Source dimension label, "SEAL +
                 Boundary confirmed"]
  STATUS: PASS / STOP]

Do not begin Phase 2 until Gate 1 shows STATUS: PASS.

---

## Phase 2 -- Signal inventory and namespace audit

List every artifact in `simulations/` whose filename contains the topic slug.
Fill Schema B (all artifacts). Fill Schema C (all 9 rows -- zero-counts for
absent namespaces, NEVER write ABSENT).

Write the PROPOSAL SCOPE block immediately after Schema C.

NEW = artifact date strictly after Schema A Strategy date.
PRIOR = date on or before Schema A Strategy date.

If no artifacts: "No signal artifacts found. Cannot run /topic:plan." Stop.
If no HIGH-pressure namespaces (all New = 0): "STRATEGY CURRENT -- no new
signals since [Strategy date]. No update warranted." Stop.

[Gate 2 -- reproduce with all three fields filled:
  GATE 2 | Phase: Signal inventory and scope declaration
  Condition evaluated: [all 9 namespace rows with numeric counts and pressure ratings;
                        ABSENT not used; PROPOSAL SCOPE block written with HIGH-pressure
                        and excluded namespace lists]
  Result found: [each namespace with Total/New/pressure; PROPOSAL SCOPE namespaces named]
  STATUS: PASS / STOP]

Do not begin Phase 3 until Gate 2 shows STATUS: PASS.

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
Do not begin Phase 4 until Gate 3 shows STATUS: PASS.

---

## Phase 4 -- Read NEW artifacts

Read each NEW artifact. The SEAL is in force -- strategy.md may not be re-opened.

Write a short paragraph (4-6 sentences) on collective findings.
Name at least two artifact filenames. Do not compare to Schema A yet.

[Gate 4 -- reproduce with all three fields filled:
  GATE 4 | Phase: New artifact synthesis
  Condition evaluated: [paragraph written and at least two filenames cited]
  Result found: [specific filenames cited]
  STATUS: PASS / STOP]

---

## Phase 5 -- Coverage map and proposals

PROPOSAL SCOPE active: [reproduce HIGH-pressure namespaces from the PROPOSAL
SCOPE block above]. Only evidence from these namespaces may drive proposals.

Fill Schema D. For NEW artifact dimensions absent from Schema A, add a row
labeled "NEW DIMENSION".

Default verdict: NO CHANGE. Burden of proof is on change.

Fill Schemas E and F. For every proposal row:
- Evidence artifact must appear in Phase 3 NEW list AND belong to a namespace
  listed in the PROPOSAL SCOPE block; if not, drop the proposal (SCOPE violation)
- Schema A ref (D-N) must name a specific locked dimension; it must match a D-N row
  in Schema A -- a reader can cross-check it against the VERBATIM Source dimension
  field without re-reading strategy.md
- Before must reproduce Schema A D-N text -- SEAL violation if text requires
  re-reading strategy.md; if Before cannot be written from Schema A, drop
  the proposal
- vs. NO CHANGE must name a specific consequence of leaving strategy unchanged

Null declarations (each type labeled separately):
  ADDITIONS: none -- [reason] | or [N] proposed
  REMOVALS: none -- [reason] | or [N] proposed
  REPRIORITIZATIONS: none -- [reason] | or [N] proposed

Fill Schemas G and H.

[Gate 5 -- reproduce with all three fields filled:
  GATE 5 | Phase: Proposals complete
  Condition evaluated: [all three null declarations present; all proposal evidence
                        in PROPOSAL SCOPE namespaces; each Schema A ref matches a D-N
                        label in locked Schema A; Schema G row count]
  Result found: [N additions / N removals / N reprioritizations; SCOPE namespace count]
  STATUS: PASS / STOP]

---

## Phase 6 -- Confirmation gate

Display all schemas (including VERBATIM EVIDENCE BLOCK, STRATEGY.MD SEALED block,
and PROPOSAL SCOPE block from Phases 1-2).

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
