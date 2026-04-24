# topic-plan Skill Variations -- Round 4 (2026-03-15)

Rubric: v4 (C-17 Two-tier sentinel vocabulary `??`/`--`; C-18 Pre-signal defense
register committed before reading any artifact; C-19 Integer-enforcement gate language
naming banned non-integer forms as a gate failure; C-20 Sequential phase-linked stop
gates referencing the next phase number explicitly.)

Three single-axis variations (V-01, V-02, V-03) then two combinations (V-04, V-05).

R3 status at entry to R4:
- C-17 partially cracked (R3 V-01 inline sentinel rules in schema section, not standalone)
- C-18 partially cracked (R3 V-04 defense register in Step 2, not pre-artifact Phase 0)
- C-19 not cracked (R3 said "must be integers" -- never named non-integers as gate failures)
- C-20 partially cracked (R3 V-03 "Do not advance to Phase N" inconsistent, some gates nameless)

R4 hypothesis: each pattern needs a dedicated named mechanism -- vocabulary contract,
Phase 0, gate-failure rule, explicit next-phase numbering -- to move from partial to full.

---

## V-01: Formal Vocabulary Contract (C-17)

**Variation axis**: Output format -- the `??`/`--` sentinel distinction is formalized as
a standalone VOCABULARY CONTRACT block placed before any schema. The block defines both
tokens with formal rules and examples, and names three specific violations by name. Single
axis.

**Hypothesis**: R3 V-01 embedded the `??`/`--` rule inside a "Pre-committed schema"
section -- close to schema content, far from a formal definition. A model reading the
schema rules and the schema in a single pass may apply them inconsistently because the
rule was never separated from its context. A standalone vocabulary contract placed before
any schema forces the model to process the token definitions as a first-class specification
before encountering any cell to fill. Naming violations explicitly (TOKEN LEFT OPEN,
PREMATURE CLOSURE, SILENT OMISSION) makes each error a detectable breach of a named rule,
not a judgment call. C-17 requires machine-distinguishable gap type, not just gap presence
-- the standalone vocabulary contract is the mechanism that achieves this.

```
You are running /topic:plan for the topic named in the user's message.

---

## VOCABULARY CONTRACT (read before any schema or step)

Two sentinel tokens are used throughout this skill. Their meanings are distinct and
non-interchangeable. Misusing one for the other is a named violation.

| Token | Name | Meaning | When to write |
|-------|------|---------|---------------|
| `??` | OPEN OBLIGATION | Unknown or not yet filled. An obligation exists to supply this value. | Every data cell starts as `??`. Replace with a real value as you fill each table. A `??` remaining in any cell of the final output is a machine-detectable unfilled obligation. |
| `--` | CLOSED DECISION | Deliberately absent. A decision was made that no value belongs here. | Use when the value is genuinely not applicable: a namespace with zero artifacts, a change type with no proposals, or an override threshold that is unspecifiable after reviewing the source. |

**Named violations**:
- TOKEN LEFT OPEN: a `??` remaining in final output where a real value could be supplied
- PREMATURE CLOSURE: writing `--` before verifying that no value exists
- SILENT OMISSION: leaving a cell blank instead of writing either `??` or `--`

Before proceeding: write "VOCABULARY CONTRACT: acknowledged."

---

## Pre-committed output schemas

Every data cell below is pre-filled with `??`. Apply the VOCABULARY CONTRACT to every
cell as you fill each table. No schema may be replaced by prose. No schema may be omitted.

**Schema A -- Strategy anchor**
| Item | Value |
|------|-------|
| Strategy file path | `??` |
| STRATEGY DATE | `??` |
| Dimensions in strategy.md | `??` |

**Schema B -- Signal inventory**
(Add one row per artifact. Each new row starts with `??` in every cell.)
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|
| `??` | `??` | `??` | `??` |

**Schema C -- Namespace audit (all 9 rows required)**
| Namespace | Artifact count | NEW artifact count | Assessment |
|-----------|---------------|-------------------|------------|
| scout | `??` | `??` | `??` |
| draft | `??` | `??` | `??` |
| review | `??` | `??` | `??` |
| flow | `??` | `??` | `??` |
| trace | `??` | `??` | `??` |
| prove | `??` | `??` | `??` |
| listen | `??` | `??` | `??` |
| program | `??` | `??` | `??` |
| topic | `??` | `??` | `??` |

**Schema D -- Delta summary**
  DELTA SUMMARY
  Strategy was written on `??`. `??` artifacts are NEW. `??` are PRIOR.
  NEW artifacts: `??`
  PRIOR artifacts: `??`

**Schema E -- Change proposals**
| # | Action | Dimension | Evidence artifact | Before | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------|-------|---------------|
| `??` | `??` | `??` | `??` | `??` | `??` | `??` |

**Schema F -- Before/after diff**
| Dimension | Before | After | Proposal ref |
|-----------|--------|-------|--------------|
| `??` | `??` | `??` | `??` |

---

## Step 1 -- Read strategy.md

Read `simulations/TOPICS.md` to find the strategy file path for this topic.
Read strategy.md. Fill Schema A (replace all `??`; use `--` per VOCABULARY CONTRACT
only for genuinely absent values). Quote at least one complete sentence from strategy.md.

Stop-gate: STRATEGY DATE recorded as YYYY-MM-DD AND a direct quote present. Scan Schema A
for TOKEN LEFT OPEN violations. Resolve all before continuing.

---

## Step 2 -- Signal inventory and namespace audit

Find every artifact in `simulations/` whose filename contains the topic slug.
Fill Schema B. Apply VOCABULARY CONTRACT to every cell:
- If an artifact date cannot be determined: write `??` (OPEN OBLIGATION) and note why
- Do not write `--` for an artifact you have not checked

Fill Schema C (all 9 rows required). A namespace with zero artifacts writes:
- Artifact count: 0 / NEW artifact count: 0 / Assessment: ABSENT
  (Assessment is never `--` -- it always takes a textual value)

Classify: NEW = artifact date > STRATEGY DATE. PRIOR = artifact date <= STRATEGY DATE.

Scan Schema B and C for TOKEN LEFT OPEN and SILENT OMISSION violations. Resolve all.

---

## Step 3 -- Delta detection

Fill Schema D. Replace every `??` with exact values:
- STRATEGY DATE: from Schema A
- [N] artifacts are NEW: integer count of NEW rows in Schema B
- [M] are PRIOR: integer count of PRIOR rows in Schema B
- NEW artifacts: comma-separated filenames, or `--` (CLOSED DECISION) if none
- PRIOR artifacts: comma-separated filenames, or `--` if none

Schema D must contain zero `??` tokens before proceeding.

If NEW count = 0:
  Write: "STRATEGY IS CURRENT -- 0 artifacts are NEW since [STRATEGY DATE].
  No update warranted."
  Stop here.

---

## Step 4 -- Read NEW artifacts

Read each artifact listed in the Schema D NEW line. PRIOR artifacts are `--` (CLOSED
DECISION: already reflected in strategy.md -- not new information).

Write a short paragraph (no headings, no bullets) describing what the NEW artifacts
collectively reveal. Name at least two artifact filenames.

---

## Step 5 -- Proposals

Only NEW artifacts (Schema D NEW list) may evidence proposals. Fill Schema E.
Apply VOCABULARY CONTRACT to every cell.

- Action: ADD, REMOVE, or REPRIORITIZE (exact text)
- Evidence artifact: a filename from Schema D NEW list
  (writing `--` here is a PREMATURE CLOSURE violation -- a proposal without evidence
  is removed before applying)
- vs. NO CHANGE: state what goes wrong if the strategy is left as-is; name a specific
  risk, gap, or incorrect prediction

Null declarations (required per change type, each on its own labeled line):
- ADDITIONS: `--` | [specific reason no new dimensions were warranted]
- REMOVALS: `--` | [specific reason existing dimensions still hold]
- REPRIORITIZATIONS: `--` | [specific reason order/weight is unchanged]

If proposals exist, fill Schema F.

Final scan: look for any TOKEN LEFT OPEN, PREMATURE CLOSURE, or SILENT OMISSION in
Schemas E and F. Resolve all before the confirmation gate.

---

## Step 6 -- Confirmation gate

Display Schema B, Schema C, Schema D, Schema E, Schema F.

Write exactly:

  PENDING CONFIRMATION -- strategy.md has NOT been modified.

  Proposed: [N] additions / [N] removals / [N] reprioritizations

  Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to
  apply custom version

Stop. Write nothing further until the user replies.

---

## Step 7 -- Apply (triggered by YES or REVISED)

Write exactly the confirmed changes to strategy.md. Do not reformat unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-02: Pre-Signal Defense Register as Phase 0 (C-18)

**Variation axis**: Role sequence -- the defense register is elevated to Phase 0, a
mandatory phase that closes strategy.md before any artifact search begins. All proposals
in later phases must name the specific Phase 0 defense they defeated. Single axis.

**Hypothesis**: R3 V-04 placed the defense register at Step 2, after reading strategy.md.
This means the model has the full strategy context in working memory when writing defenses
-- it can write defenses shaped by anticipated challenges rather than genuinely pre-committing
to them. C-18 requires the register be committed before reading ANY artifact. The only
structural enforcement is a Phase 0 exit gate that says "Do not open any signal artifact
until this register is fully committed" -- paired with a rule that each proposal must name
the specific Phase 0 defense it defeated, not just assert "new evidence found." Making the
linkage explicit and verifiable at the proposal gate closes the post-hoc justification path.

```
You are running /topic:plan for the topic named in the user's message.

The default outcome is NO CHANGE to strategy.md. Every proposal must name the
strategy defense it defeated. Inertia is a co-equal option, not a fallback.

---

## Phase 0 -- Read strategy.md for dimensions, then commit defense register

Read `simulations/TOPICS.md` to find the strategy file path. Read strategy.md.

Record:
  STRATEGY FILE: [path]
  STRATEGY DATE: [YYYY-MM-DD]

List every strategy dimension. Number them.

Quote at least one complete sentence from strategy.md.

Now close strategy.md. Do not open any signal artifact until Phase 0 is complete.

Fill the defense register. One row per strategy dimension. For each row:
- Defense: the strongest argument for keeping this dimension unchanged (not a restated
  dimension name; a genuine argument about why the current framing is sufficient)
- Override threshold: what observable evidence, if present in a signal artifact,
  would justify a change to this dimension

| # | Dimension | Defense: strongest keep-unchanged argument | Override threshold: evidence that would defeat this |
|---|-----------|--------------------------------------------|----------------------------------------------------|
| 1 | [dim] | [argument] | [evidence type] |
| 2 | [dim] | [argument] | [evidence type] |
(continue for all dimensions)

**Phase 0 exit gate**: Every strategy dimension has a row. Every "Defense" cell makes
a genuine argument (not a restatement). Every "Override threshold" cell names a specific
evidence type (not "if there is evidence" or "if warranted").
Do not open any signal artifact -- do not advance to Phase 1 -- until this gate passes.

---

## Phase 1 -- Signal inventory and namespace audit

Find every artifact in `simulations/` whose filename contains the topic slug.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|

Classify: NEW = artifact date > STRATEGY DATE. PRIOR = artifact date <= STRATEGY DATE.

Assess all 9 namespaces:

| Namespace | Artifact count | NEW artifact count | Assessment |
|-----------|---------------|-------------------|------------|
| scout | [N] | [N] | COVERED / ABSENT |
| draft | [N] | [N] | COVERED / ABSENT |
| review | [N] | [N] | COVERED / ABSENT |
| flow | [N] | [N] | COVERED / ABSENT |
| trace | [N] | [N] | COVERED / ABSENT |
| prove | [N] | [N] | COVERED / ABSENT |
| listen | [N] | [N] | COVERED / ABSENT |
| program | [N] | [N] | COVERED / ABSENT |
| topic | [N] | [N] | COVERED / ABSENT |

**Phase 1 exit gate**: All 9 namespace rows present with integer artifact counts.
Do not advance to Phase 2 until every namespace row is filled.

---

## Phase 2 -- Delta detection

Classify artifacts into NEW and PRIOR lists. Write:

  Strategy was written on [STRATEGY DATE]. [N] artifacts are NEW. [M] are PRIOR.
  NEW artifacts: [comma-separated filenames, or "none"]
  PRIOR artifacts: [comma-separated filenames, or "none"]

[N] and [M] must be integers.

**Phase 2 exit gate**: Delta summary sentence present with exact integer counts.
If N = 0: "No new signals since [STRATEGY DATE]. Strategy is current." Stop here.
Do not advance to Phase 3 without passing this gate.

---

## Phase 3 -- Read NEW artifacts and challenge Phase 0 register

Read only the NEW artifacts from Phase 2.

For each NEW artifact, assess which Phase 0 defense arguments it challenges:

| NEW Artifact | Dimension | Phase 0 Defense challenged (quote exactly) | Assessment |
|--------------|-----------|---------------------------------------------|------------|
| [filename] | [dim] | [exact defense text from Phase 0] | VALIDATES / WEAKENS / INVALIDATES |

If a NEW artifact raises a dimension absent from Phase 0:
| [filename] | [NEW DIMENSION] | -- (not in Phase 0 register) | CANDIDATE ADDITION |

**Phase 3 exit gate**: Every NEW artifact has at least one row. Phase 0 defense text
is quoted exactly, not paraphrased. Do not advance to Phase 4 without passing this gate.

---

## Phase 4 -- Proposals

For Phase 3 rows where Assessment is WEAKENS or INVALIDATES, and for CANDIDATE
ADDITION rows, propose changes:

| # | Action | Dimension | Evidence artifact | Before | After | Defense defeated (Phase 0 row #) |
|---|--------|-----------|-------------------|--------|-------|----------------------------------|
| [N] | ADD / REMOVE / REPRIORITIZE | [dim] | [NEW filename] | [before] | [after] | [Phase 0 row # and defense text] |

"Defense defeated" column rules:
- Must reference the Phase 0 defense register by row number AND quote or paraphrase
  the specific defense argument the evidence overcame
- "New evidence found" is not acceptable -- it does not name a specific defense
- "Evidence is compelling" is not acceptable -- it does not reference Phase 0
- A row whose "Defense defeated" cell does not cite Phase 0 will be removed before applying

Null declarations (required per change type, with Phase 0 reference):
- ADDITIONS: none -- Phase 0 defenses for rows [#] held against all NEW artifacts
- REMOVALS: none -- Phase 0 defenses for rows [#] held against all NEW artifacts
- REPRIORITIZATIONS: none -- Phase 0 defenses for rows [#] held against all NEW artifacts

If proposals exist, produce a before/after diff:
| Dimension | Before | After | Proposal ref |
|-----------|--------|-------|--------------|

**Phase 4 exit gate**: Every "Defense defeated" cell references a Phase 0 row by number.
No generic rationale in any "Defense defeated" cell.
Do not advance to Phase 5 without passing this gate.

---

## Phase 5 -- Confirmation gate

Display Phase 0 defense register, Phase 1 inventory + namespace audit, Phase 2 delta
summary, Phase 3 challenge assessment, Phase 4 proposals + diff.

Write exactly:

  PENDING CONFIRMATION -- strategy.md has NOT been modified.

  Proposed: [N] additions / [N] removals / [N] reprioritizations

  Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to
  apply custom version

Stop. Write nothing further until the user replies.

---

## Phase 6 -- Apply (triggered by YES or REVISED)

Write exactly the confirmed changes to strategy.md. Do not reformat unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-03: Sequential Phase-Linked Gates + Integer-Enforcement Gate Language (C-19 + C-20)

**Variation axis**: Lifecycle emphasis -- every stop gate names the next phase number
explicitly; AND the delta phase includes a dedicated INTEGER ENFORCEMENT RULE that names
banned non-integer forms as "a gate failure." Two closely related lifecycle/correctness
criteria treated as a single lifecycle axis. Single axis.

**Hypothesis**: R3 V-03 had "Do not advance to Phase N" in most gates but was
inconsistent -- some gates said "proceed" or "continue" without naming the target phase,
which breaks the sequential chain. C-20 requires the chain to be complete with no gaps.
C-19 adds a specific detection mechanism: beyond "must be integers," the rule explicitly
names the banned forms ("a few", "several", "some", "multiple", "many") and labels their
presence a "gate failure" rather than a quality concern. Both criteria share the same axis:
they make failure detectable by name rather than by judgment.

```
You are running /topic:plan for the topic named in the user's message.

This skill runs in numbered phases. Every phase gate names the next phase number
explicitly. No phase may be skipped. A gate that does not name its successor phase
number is incomplete and does not count as passing.

---

## Phase 1 -- Read strategy.md

Read `simulations/TOPICS.md` to find the strategy file path for this topic.
Read strategy.md.

Record:
  STRATEGY FILE: [path]
  STRATEGY DATE: [YYYY-MM-DD]
  DIMENSIONS: [numbered list of all dimensions]

Quote at least one complete sentence from strategy.md.

**Phase 1 stop gate**: STRATEGY DATE recorded as YYYY-MM-DD AND a direct quote present.
Do not advance to Phase 2 without passing this gate.

---

## Phase 2 -- Signal inventory

Find every artifact in `simulations/` whose filename contains the topic slug.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|
| [fill] | YYYY-MM-DD | [fill] | [fill] |

Classify: NEW = artifact date > STRATEGY DATE. PRIOR = artifact date <= STRATEGY DATE.

Assess all 9 namespaces:

| Namespace | Artifact count | NEW artifact count | Assessment |
|-----------|---------------|-------------------|------------|
| scout | [N] | [N] | COVERED / ABSENT |
| draft | [N] | [N] | COVERED / ABSENT |
| review | [N] | [N] | COVERED / ABSENT |
| flow | [N] | [N] | COVERED / ABSENT |
| trace | [N] | [N] | COVERED / ABSENT |
| prove | [N] | [N] | COVERED / ABSENT |
| listen | [N] | [N] | COVERED / ABSENT |
| program | [N] | [N] | COVERED / ABSENT |
| topic | [N] | [N] | COVERED / ABSENT |

**Phase 2 stop gate**: All 9 namespace rows are present with integer artifact counts.
A missing namespace row or a blank count cell is a gate failure.
Do not advance to Phase 3 without passing this gate.

---

## Phase 3 -- Delta detection (DELTA SUMMARY BLOCK)

This phase has one primary deliverable: the DELTA SUMMARY BLOCK below.
Partition artifacts from Phase 2 into NEW and PRIOR lists, then produce:

  DELTA SUMMARY
  Strategy was written on [STRATEGY DATE]. [N] artifacts are NEW. [M] are PRIOR.
  NEW artifacts: [comma-separated filenames, or "none"]
  PRIOR artifacts: [comma-separated filenames, or "none"]

**INTEGER ENFORCEMENT RULE**: [N] and [M] must be plain integers.
Writing "a few", "several", "some", "multiple", "many", or any other non-integer
value in place of [N] or [M] is a gate failure. If you find a non-integer in the
DELTA SUMMARY BLOCK, recount the rows from Phase 2 and correct the value before
proceeding. Fuzziness in a count is a named failure condition, not a quality concern.

**Phase 3 stop gate**: The DELTA SUMMARY BLOCK is present, [N] is a plain integer,
[M] is a plain integer, and both artifact lists are filled (write "none" if empty).
If N = 0: write "STRATEGY IS CURRENT -- 0 artifacts are NEW since [STRATEGY DATE].
No update warranted." Stop here.
Do not advance to Phase 4 without passing this gate.

---

## Phase 4 -- Read NEW artifacts

Read each artifact listed in the Phase 3 DELTA SUMMARY NEW line.
PRIOR artifacts are already reflected in strategy.md and are not new evidence.

Write a short paragraph (no headings, no bullets) describing what the NEW artifacts
collectively reveal. Name at least two artifact filenames.

**Phase 4 stop gate**: The paragraph is present and names at least two NEW artifact
filenames.
Do not advance to Phase 5 without passing this gate.

---

## Phase 5 -- Proposals

Compare NEW artifact findings to each strategy dimension from Phase 1.

| # | Action | Dimension | Evidence artifact | Before | After | vs. NO CHANGE |
|---|--------|-----------|-------------------|--------|-------|---------------|
| [N] | ADD / REMOVE / REPRIORITIZE | [dim] | [NEW filename only] | [before] | [after] | [specific consequence] |

- Only filenames from Phase 3 NEW artifacts line may appear in the Evidence column.
  A PRIOR filename in the Evidence column is a gate failure -- remove that row.
- The "vs. NO CHANGE" column must state what goes wrong if the strategy is left as-is.
  The following phrases are banned (any row containing them is removed before applying):
  "no change needed" / "compelling reason" / "clearly warranted" / "obviously beneficial" /
  "update is warranted" / "the strategy benefits from this"

Null declarations (required per change type, labeled separately):
- ADDITIONS: none -- [specific reason no new dimensions were warranted]
- REMOVALS: none -- [specific reason existing dimensions still hold]
- REPRIORITIZATIONS: none -- [specific reason order/weight is unchanged]

If proposals exist, also produce a before/after diff:
| Dimension | Before | After | Proposal ref |
|-----------|--------|-------|--------------|

**Phase 5 stop gate**: Every Evidence artifact appears in Phase 3 NEW list. No banned
phrases in any "vs. NO CHANGE" cell. All three null declarations present.
Do not advance to Phase 6 without passing this gate.

---

## Phase 6 -- Confirmation gate

Display: Phase 2 inventory table, Phase 2 namespace audit, Phase 3 DELTA SUMMARY BLOCK,
Phase 5 proposal table, Phase 5 before/after diff (if present).

Write exactly:

  PENDING CONFIRMATION -- strategy.md has NOT been modified.

  Proposed: [N] additions / [N] removals / [N] reprioritizations

  Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to
  apply custom version

Stop. Write nothing further until the user replies.
Do not advance to Phase 7 without user reply.

---

## Phase 7 -- Apply (triggered by YES or REVISED)

Write exactly the confirmed changes to strategy.md. Do not reformat unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-04: Vocabulary Contract + Defense Register as Phase 0 (C-17 + C-18)

**Variation axis**: Output format + Role sequence -- the two-tier sentinel vocabulary
contract (C-17) and the pre-signal defense register as Phase 0 (C-18) are combined. The
vocabulary contract governs all table cells; the defense register governs all proposals.
Combined axis.

**Hypothesis**: C-17 and C-18 target different omission risks at different structural
levels. C-17 targets the cell level: gaps must be machine-distinguishable from deliberate
absences. C-18 targets the proposal level: inertia justification must be evidence-based,
not post-hoc. Combining them tests whether both mechanisms reinforce each other: a defense
register filled with `??`-initialized cells that must be replaced with real defenses before
artifact reading forces both pre-commitment (C-18) and gap visibility (C-17) simultaneously.
The `--` (CLOSED DECISION) token also has a natural role in the defense register: "Override
threshold: --" is a legitimate closed decision when genuinely unspecifiable, while an
unfilled defense cell must stay `??` (TOKEN LEFT OPEN) until written. This creates a
consistent vocabulary across Phase 0 and all subsequent phases.

```
You are running /topic:plan for the topic named in the user's message.

The default outcome is NO CHANGE. Every proposal must name the strategy defense it
defeated. Every table cell is filled, open (`??`), or deliberately absent (`--`).

---

## VOCABULARY CONTRACT (read before Phase 0)

Two sentinel tokens govern all table cells:

| Token | Name | Meaning | When to write |
|-------|------|---------|---------------|
| `??` | OPEN OBLIGATION | Not yet filled -- a real value is expected | Every data cell in every schema starts as `??`. Replace as you work. `??` in a final output cell is a named violation: TOKEN LEFT OPEN. |
| `--` | CLOSED DECISION | Deliberately absent -- no value belongs here | Use when: a namespace has zero artifacts; a change type has no proposals; a Phase 0 override threshold cannot be specified after reviewing strategy.md. Never write `--` to skip filling a cell. |

**Named violations**:
- TOKEN LEFT OPEN: `??` remaining in final output where a value could be supplied
- PREMATURE CLOSURE: `--` written without verifying that no value exists

Acknowledge: "VOCABULARY CONTRACT: `??` = open obligation, `--` = closed decision."

---

## Phase 0 -- Read strategy.md for dimensions, then commit defense register

Read `simulations/TOPICS.md` to find the strategy file path. Read strategy.md.

Fill this record (replace `??` with real values per VOCABULARY CONTRACT):

  STRATEGY FILE: `??`
  STRATEGY DATE: `??`

List all strategy dimensions. Number them.

Quote at least one complete sentence from strategy.md.

Now close strategy.md. Do not open any signal artifact until Phase 0 is complete.

Fill the defense register below. One row per strategy dimension. Replace every `??`
before the Phase 0 gate. `--` is permitted in "Override threshold" only if genuinely
unspecifiable after reviewing strategy.md.

| # | Dimension | Defense: strongest keep-unchanged argument | Override threshold: evidence that would defeat this |
|---|-----------|--------------------------------------------|----------------------------------------------------|
| 1 | `??` | `??` | `??` |
| 2 | `??` | `??` | `??` |
(continue for all dimensions)

**Phase 0 stop gate**: Every row in the defense register has non-`??` content in both
the Defense and Override threshold columns. TOKEN LEFT OPEN check: scan every cell for
`??` and replace or justify before exiting.
Do not open any signal artifact -- do not advance to Phase 1 -- until this gate passes.

---

## Phase 1 -- Signal inventory

Find every artifact in `simulations/` whose filename contains the topic slug.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|
| `??` | `??` | `??` | `??` |

Apply VOCABULARY CONTRACT. A namespace with zero artifacts: count = 0, Assessment = ABSENT
(CLOSED DECISION `--` is not the right token here -- Assessment is always a text value).

| Namespace | Artifact count | NEW artifact count | Assessment |
|-----------|---------------|-------------------|------------|
| scout | `??` | `??` | `??` |
| draft | `??` | `??` | `??` |
| review | `??` | `??` | `??` |
| flow | `??` | `??` | `??` |
| trace | `??` | `??` | `??` |
| prove | `??` | `??` | `??` |
| listen | `??` | `??` | `??` |
| program | `??` | `??` | `??` |
| topic | `??` | `??` | `??` |

Classify: NEW = artifact date > STRATEGY DATE. PRIOR = artifact date <= STRATEGY DATE.

**Phase 1 stop gate**: All 9 namespace rows present with integer counts. TOKEN LEFT OPEN
check: resolve all `??` remaining in inventory and namespace tables.
Do not advance to Phase 2 without passing this gate.

---

## Phase 2 -- Delta detection

Write:

  DELTA SUMMARY
  Strategy was written on [STRATEGY DATE]. [N] artifacts are NEW. [M] are PRIOR.
  NEW artifacts: [filenames, or `--`]
  PRIOR artifacts: [filenames, or `--`]

[N] and [M] must be integers.

**Phase 2 stop gate**: [N] and [M] are integers. `--` used correctly for empty lists
per VOCABULARY CONTRACT (CLOSED DECISION: no artifacts in this list).
If N = 0: "STRATEGY IS CURRENT -- 0 NEW artifacts since [STRATEGY DATE]." Stop here.
Do not advance to Phase 3 without passing this gate.

---

## Phase 3 -- Read NEW artifacts and challenge Phase 0 register

Read only the NEW artifacts from Phase 2.

| NEW Artifact | Dimension | Phase 0 Defense challenged (quote exactly) | Assessment |
|--------------|-----------|---------------------------------------------|------------|
| `??` | `??` | [exact defense text] | VALIDATES / WEAKENS / INVALIDATES |

Artifacts raising a dimension absent from Phase 0:
| `??` | [NEW DIMENSION] | `--` (not in register) | CANDIDATE ADDITION |

**Phase 3 stop gate**: Every NEW artifact has a row. Phase 0 defense text quoted exactly.
TOKEN LEFT OPEN check: resolve all `??` remaining in the challenge table.
Do not advance to Phase 4 without passing this gate.

---

## Phase 4 -- Proposals

For WEAKENS / INVALIDATES rows and CANDIDATE ADDITION rows from Phase 3:

| # | Action | Dimension | Evidence artifact | Before | After | Defense defeated (Phase 0 row #) |
|---|--------|-----------|-------------------|--------|-------|----------------------------------|
| `??` | `??` | `??` | `??` | `??` | `??` | `??` |

Apply VOCABULARY CONTRACT. "Defense defeated" must reference a specific Phase 0 row
by number and quote or paraphrase the defense argument -- TOKEN LEFT OPEN if generic.

Null declarations (use `--` as CLOSED DECISION for absent change types):
- ADDITIONS: `--` | [Phase 0 rows that held, by row #]
- REMOVALS: `--` | [Phase 0 rows that held, by row #]
- REPRIORITIZATIONS: `--` | [Phase 0 rows that held, by row #]

If proposals exist, fill a before/after diff:
| Dimension | Before | After | Proposal ref |
|-----------|--------|-------|--------------|
| `??` | `??` | `??` | `??` |

**Phase 4 stop gate**: No TOKEN LEFT OPEN in proposal table. Every "Defense defeated"
cell cites a Phase 0 row number. All three null declarations present.
Do not advance to Phase 5 without passing this gate.

---

## Phase 5 -- Confirmation gate

Display Phase 0 defense register, Phase 1 inventory + namespace audit, Phase 2 delta
summary, Phase 3 challenge table, Phase 4 proposals + diff.

Final TOKEN LEFT OPEN scan: search all schemas for `??`. Resolve before displaying.

Write exactly:

  PENDING CONFIRMATION -- strategy.md has NOT been modified.

  Proposed: [N] additions / [N] removals / [N] reprioritizations

  Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to
  apply custom version

Stop. Write nothing further until the user replies.
Do not advance to Phase 6 without user reply.

---

## Phase 6 -- Apply (triggered by YES or REVISED)

Write exactly the confirmed changes to strategy.md. Do not reformat unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-05: Full Combination (C-17 + C-18 + C-19 + C-20)

**Variation axis**: Combined -- Vocabulary contract (C-17) + Defense register as Phase 0
(C-18) + Integer-enforcement gate language (C-19) + Sequential phase-linked stop gates
with explicit next-phase numbers (C-20) + pre-committed schemas + conflict audit. Full
combination.

**Hypothesis**: C-17 through C-20 are each partially cracked by prior rounds. Each has a
specific failure mode that earlier variations left open:

- C-17's gap (R3 V-01): sentinel rules embedded inside schema section -- model reads rules
  and schemas in one pass, may not apply rules as first-class constraints. Fix: standalone
  VOCABULARY CONTRACT before all content, with named violations.

- C-18's gap (R3 V-04): defense register in Step 2 after strategy.md is read -- full
  strategy context in working memory enables post-hoc rationalization. Fix: Phase 0
  closes strategy.md before any artifact search begins.

- C-19's gap (all rounds): "must be integers" is a quality instruction; "writing 'a few'
  is a gate failure" is a detectability rule. Only the latter closes the gap. Fix: INTEGER
  ENFORCEMENT RULE at Phase 3 names the banned forms and labels their presence a gate
  failure, not a quality concern.

- C-20's gap (R3 V-03): most gates named the next phase but some did not, breaking the
  chain. Fix: every gate in the template uses the exact phrase "Do not advance to Phase N"
  with the next phase number, with no exceptions.

```
You are running /topic:plan for the topic named in the user's message.

The default outcome is NO CHANGE to strategy.md. Every proposal must defeat a named
strategy defense. Every table cell is filled, open (`??`), or closed (`--`). Every
phase gate names its successor. Integer counts are enforced by rule, not judgment.

---

## VOCABULARY CONTRACT (read before any phase)

Two tokens govern every table cell:

| Token | Name | Meaning | When to write |
|-------|------|---------|---------------|
| `??` | OPEN OBLIGATION | Unknown or not yet filled. A real value is expected. | Every data cell starts as `??`. Replace as you fill each table. A `??` remaining in any final output cell is a named violation: TOKEN LEFT OPEN. |
| `--` | CLOSED DECISION | Deliberately absent. A decision was made that no value belongs here. | Use when: a namespace has zero artifacts; a change type has no proposals; an override threshold is genuinely unspecifiable after reviewing source. Never write `--` to avoid checking a source. |

**Named violations**:
- TOKEN LEFT OPEN: `??` remaining in final output where a value could be supplied
- PREMATURE CLOSURE: `--` written before verifying the source
- CHAIN SKIP: advancing to Phase N+1 without passing Phase N's stop gate

Acknowledge: "VOCABULARY CONTRACT: `??` = open obligation, `--` = closed decision."

---

## Pre-committed output schemas

Every data cell starts as `??`. Schemas are filled in the phase they belong to.
No schema may be replaced by prose. No schema may be omitted.

**Schema A -- Strategy anchor** (Phase 0)
| Item | Value |
|------|-------|
| Strategy file path | `??` |
| STRATEGY DATE | `??` |
| Dimensions | `??` |

**Schema B -- Defense register** (Phase 0; one row per dimension; filled before artifact search)
| # | Dimension | Defense: strongest keep-unchanged argument | Override threshold: evidence that would defeat this |
|---|-----------|--------------------------------------------|----------------------------------------------------|
| 1 | `??` | `??` | `??` |
(add rows as needed)

**Schema C -- Signal inventory** (Phase 1)
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|
| `??` | `??` | `??` | `??` |

**Schema D -- Namespace audit** (Phase 1; all 9 rows required)
| Namespace | Artifact count | NEW artifact count | Assessment |
|-----------|---------------|-------------------|------------|
| scout | `??` | `??` | `??` |
| draft | `??` | `??` | `??` |
| review | `??` | `??` | `??` |
| flow | `??` | `??` | `??` |
| trace | `??` | `??` | `??` |
| prove | `??` | `??` | `??` |
| listen | `??` | `??` | `??` |
| program | `??` | `??` | `??` |
| topic | `??` | `??` | `??` |

**Schema E -- DELTA SUMMARY BLOCK** (Phase 2; sole deliverable of Phase 2)
  DELTA SUMMARY
  Strategy was written on `??`. `??` artifacts are NEW. `??` are PRIOR.
  NEW artifacts: `??`
  PRIOR artifacts: `??`

**Schema F -- Challenge assessment** (Phase 3)
| NEW Artifact | Dimension | Schema B defense challenged (quote exactly) | Assessment |
|--------------|-----------|---------------------------------------------|------------|
| `??` | `??` | `??` | `??` |

**Schema G -- Change proposals** (Phase 4)
| # | Action | Dimension | Evidence artifact | Before | After | Defense defeated (Schema B row #) |
|---|--------|-----------|-------------------|--------|-------|-----------------------------------|
| `??` | `??` | `??` | `??` | `??` | `??` | `??` |

**Schema H -- Before/after diff** (Phase 4)
| Dimension | Before | After | Proposal ref |
|-----------|--------|-------|--------------|
| `??` | `??` | `??` | `??` |

**Schema I -- Conflict audit** (Phase 4)
| Conflict ID | Signal A | Signal B | Dimension | Nature | Resolution |
|-------------|----------|----------|-----------|--------|------------|
| `??` | `??` | `??` | `??` | `??` | `??` |

---

## Phase 0 -- Read strategy.md and commit defense register

Read `simulations/TOPICS.md` to find the strategy file path. Read strategy.md.
Fill Schema A (replace all `??`). Quote at least one complete sentence from strategy.md.

Fill Schema B. One row per Schema A dimension. Rules:
- Replace every `??` with a real defense argument
- `--` permitted in "Override threshold" only if genuinely unspecifiable after reviewing
  strategy.md (this is a CLOSED DECISION -- write `--` and note why unspecifiable)
- Do not open any signal artifact before Schema B is complete

TOKEN LEFT OPEN check: scan Schema A and Schema B for any remaining `??`. Resolve all.

**Phase 0 stop gate**: Schema A STRATEGY DATE is YYYY-MM-DD. A direct quote from
strategy.md is present. Every Schema B row has non-`??` content in Defense column.
Do not advance to Phase 1 without passing this gate.

---

## Phase 1 -- Signal inventory and namespace audit

Find every artifact in `simulations/` whose filename contains the topic slug.
Fill Schema C. Apply VOCABULARY CONTRACT (each new row starts `??`/`??`/`??`/`??`).
Classify: NEW = artifact date > Schema A STRATEGY DATE. PRIOR = date <= STRATEGY DATE.

Fill Schema D (all 9 rows required). Zero-artifact namespace: count = 0, Assessment = ABSENT.
(Assessment never uses `--` -- it is always a textual value.)

TOKEN LEFT OPEN check: scan Schema C and D for `??`. Resolve all.

**Phase 1 stop gate**: All 9 Schema D rows are present with integer counts. No `??`
tokens remain in Schema C or Schema D.
Do not advance to Phase 2 without passing this gate.

---

## Phase 2 -- Delta detection: DELTA SUMMARY BLOCK

Fill Schema E. Replace every `??` with exact values from Schema A and Schema C.

**INTEGER ENFORCEMENT RULE**: The "artifacts are NEW" and "are PRIOR" counts must be
plain integers. Writing "a few", "several", "some", "multiple", "many", or any other
non-integer value in place of these counts is a gate failure. If a non-integer appears
in Schema E, recount the rows in Schema C and correct before proceeding. Non-integer
counts are not a quality concern -- they are a named, detectable failure condition.

TOKEN LEFT OPEN check: scan Schema E for `??`. "NEW artifacts: `??`" must become a
comma-separated list or `--` (CLOSED DECISION: no NEW artifacts).

**Phase 2 stop gate**: Schema E is fully filled. Both counts are plain integers.
If NEW count = 0: write "STRATEGY IS CURRENT -- 0 artifacts are NEW since [STRATEGY DATE].
No update warranted." Stop here.
Do not advance to Phase 3 without passing this gate.

---

## Phase 3 -- Read NEW artifacts and challenge Schema B

Read each artifact in Schema E NEW artifacts line.
Fill Schema F. For each NEW artifact, find which Schema B defenses it challenges.
Quote Schema B defense text exactly -- do not paraphrase.

Artifacts raising a dimension absent from Schema B:
| [filename] | [NEW DIMENSION] | `--` (not in Schema B) | CANDIDATE ADDITION |

TOKEN LEFT OPEN check: resolve any `??` remaining in Schema F.

**Phase 3 stop gate**: Every NEW artifact has at least one Schema F row. All challenged
defense cells contain quoted Schema B text or `--` for CANDIDATE ADDITION rows.
Do not advance to Phase 4 without passing this gate.

---

## Phase 4 -- Proposals

For Schema F rows where Assessment is WEAKENS or INVALIDATES, and for CANDIDATE ADDITION
rows, fill Schema G.

BANNED phrases in "Defense defeated" column -- any row containing these phrases is removed
before applying:
- "new evidence found"
- "evidence is compelling"
- "no change needed"
- "clearly warranted"
- "update is warranted"
- "the strategy benefits from this"
- "obviously beneficial"

"Defense defeated" must name a specific Schema B row number AND quote or reference the
defense argument. A cell that does not do this is a TOKEN LEFT OPEN violation.

Null declarations (required per change type, using `--` as CLOSED DECISION):
- ADD: `--` | [Schema B rows that held, by row # and dimension]
- REMOVE: `--` | [Schema B rows that held, by row # and dimension]
- REPRIORITIZE: `--` | [Schema B rows that held, by row # and dimension]

Fill Schema H for each Schema G row.

Fill Schema I (conflict audit). Identify any two NEW artifacts contradicting each other
on the same strategy dimension. If none: "CONFLICT AUDIT: `--` -- no contradictions
detected between NEW artifacts on any strategy dimension."

**Phase 4 stop gate**: All Schema G Evidence artifacts are in Schema E NEW list. No
BANNED phrases in any "Defense defeated" cell. All three null declarations present. No
TOKEN LEFT OPEN violations in Schemas G, H, or I.
Do not advance to Phase 5 without passing this gate.

---

## Phase 5 -- Confirmation gate

Display: Schema B (defense register), Schema C + D (inventory + namespace audit),
Schema E (DELTA SUMMARY BLOCK), Schema F (challenge assessment), Schema G (proposals),
Schema H (diff), Schema I (conflict audit).

Final scan: search all schemas for `??` (TOKEN LEFT OPEN) and `--` used in place of
a value that could be supplied (PREMATURE CLOSURE). Resolve any violations before
displaying.

Write exactly:

  PENDING CONFIRMATION -- strategy.md has NOT been modified.

  Proposed: [N] additions / [N] removals / [N] reprioritizations

  Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to
  apply custom version

Stop. Write nothing further until the user replies.
Do not advance to Phase 6 without user reply.

---

## Phase 6 -- Apply (triggered by YES or REVISED)

Write exactly the confirmed changes to strategy.md. Do not reformat unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## Round 4 Variation Summary

| Variation | Primary axis | New criteria targeted | Key mechanism | Delta from R3 |
|-----------|--------------|-----------------------|---------------|---------------|
| V-01 | Output format | C-17 (two-tier sentinel vocabulary) | Standalone VOCABULARY CONTRACT block before all schemas; three named violations | R3 embedded rules in schema section; R4 separates vocabulary into a first-class pre-schema block |
| V-02 | Role sequence | C-18 (pre-signal defense register) | Phase 0 closes strategy.md before artifact search; all proposals cite Schema B row # | R3 V-04 register in Step 2 with strategy context present; R4 Phase 0 closes file before any artifact opens |
| V-03 | Lifecycle emphasis | C-19 + C-20 (integer gate-failure language + sequential phase-linked gates) | INTEGER ENFORCEMENT RULE names banned forms as "gate failure"; every gate says "Do not advance to Phase N+1" | R3 V-03 inconsistent gate numbering; no round had "gate failure" language for non-integers |
| V-04 | Output format + Role sequence | C-17 + C-18 | Vocabulary contract + Phase 0 defense register; `--` legitimate for unspecifiable overrides; proposals cite row # | Combines V-01 and V-02; two-tier sentinel and defense register reinforce each other |
| V-05 | Full combination | C-17 + C-18 + C-19 + C-20 | All four mechanisms as dedicated named structural components; TOKEN LEFT OPEN scan at every gate | All four new v4 criteria have dedicated named mechanisms with their own gate language |

**Structural risk ranking** (lowest risk first): V-05 > V-04 > V-02 > V-03 > V-01

V-05 encodes all four criteria as dedicated first-class mechanisms inside named phases with
numbered exit gates and a final TOKEN LEFT OPEN scan. V-01 relies on the vocabulary
contract being actively applied during table construction -- under long context, the
contract may drift to preamble status. V-03's INTEGER ENFORCEMENT RULE is a single-point
enforcement at one phase; the surrounding prompt gives it no structural backup.

**Key R4 distinctions from R3**:
- C-17: standalone VOCABULARY CONTRACT block (not embedded in schema notes)
- C-18: Phase 0 with strategy.md closed before artifact search (not Step 2 post-read)
- C-19: "writing X is a gate failure" (not "must be integers" quality instruction)
- C-20: every gate explicitly says "Do not advance to Phase N+1" (no exceptions)
