# topic-plan Skill Variations — Round 2 (2026-03-15)

Rubric: v2 (C-01 through C-12; C-11 Phase-gated lifecycle, C-12 Pre-scan commitment
are new aspirational criteria added from Round 1 excellence signals)

Round 1 recap: V-03 (named phases with PASS/STOP gates) was the only R1 variation
that passed C-01, C-02, C-03, and C-05 in the same run. V-04 (pre-signal defense
register) was the only R1 variation that made C-01 causal rather than incidental.
These two patterns became C-11 and C-12.

Round 2 target: crack C-11 (phase-gate visible *in the output*, not just in
instructions) and C-12 (strategy dimensions committed *before* artifact scan begins,
preventing backward rationalization).

Three single-axis variations (V-01, V-02, V-03) then two combinations (V-04, V-05).

---

## V-01: Phase-Gate Syntax — Visible GATE BLOCK in Output

**Variation axis**: Lifecycle emphasis — each phase boundary requires the model to
reproduce a literal GATE BLOCK with STATUS filled. The gate is an output artifact,
not an instruction fragment.

**Hypothesis**: R1's V-03 used exit gate language in instructions, but the gate was
described conditionally ("Do not advance without passing"). C-11 requires the gate
to be *visible in the output itself*, not just encoded in the prompt. Making the GATE
BLOCK a template the model must reproduce (with PASS/STOP filled in) at each phase
boundary turns it into a structural output artifact: if it is absent, C-11 fails
visibly. If STATUS is STOP, the model cannot continue to the next phase — the gate
is self-enforcing in the output trace.

```
You are running /topic:plan for the topic named in the user's message.

This skill runs in five named phases. At the end of each phase you MUST reproduce
the GATE BLOCK below with [N] and [STATUS] filled. You may not begin the next phase
until the gate for the current phase shows STATUS: PASS.

GATE BLOCK template (reproduce verbatim, fill every bracket):

  ===================================
  PHASE [N] GATE
  STATUS: PASS / STOP
  Condition met: [one sentence]
  ===================================

If STATUS is STOP, state what is missing and retry the phase before advancing.

---

## Phase 1 -- Read strategy.md

Read `simulations/TOPICS.md` to locate the strategy file path for this topic.
Read strategy.md. Record:

  STRATEGY FILE: [path]
  STRATEGY DATE: [YYYY-MM-DD]

Quote at least one complete sentence from strategy.md to confirm you read it.

Gate condition: STRATEGY DATE is recorded AND at least one direct quote appears.

[Reproduce GATE BLOCK for Phase 1 here before proceeding]

---

## Phase 2 -- Signal inventory and namespace audit

List every artifact in `simulations/` whose filename contains the topic slug.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|
| [fill]            | YYYY-MM-DD    | [fill]      | [fill]    |

NEW = artifact date > STRATEGY DATE. PRIOR = date <= STRATEGY DATE.

Assess all 9 namespaces. Every row is required. ABSENT is a valid count:

| Namespace | Count | NEW count | Status           |
|-----------|-------|-----------|------------------|
| scout     | [N]   | [N]       | COVERED / ABSENT |
| draft     | [N]   | [N]       | COVERED / ABSENT |
| review    | [N]   | [N]       | COVERED / ABSENT |
| flow      | [N]   | [N]       | COVERED / ABSENT |
| trace     | [N]   | [N]       | COVERED / ABSENT |
| prove     | [N]   | [N]       | COVERED / ABSENT |
| listen    | [N]   | [N]       | COVERED / ABSENT |
| program   | [N]   | [N]       | COVERED / ABSENT |
| topic     | [N]   | [N]       | COVERED / ABSENT |

Gate condition: All 9 namespace rows are present with counts filled.

[Reproduce GATE BLOCK for Phase 2 here before proceeding]

---

## Phase 3 -- Delta detection

Partition artifacts from Phase 2:

  NEW (artifact date > STRATEGY DATE):  [list filenames and dates]
  PRIOR (artifact date <= STRATEGY DATE): [list filenames and dates]

PRIOR artifacts may not drive proposals. They were available when strategy.md
was written.

Gate condition: At least one NEW artifact is identified. If none, write:
"STRATEGY IS CURRENT -- no new signals since STRATEGY DATE ([date]).
No update warranted." STATUS: STOP -- end here.

[Reproduce GATE BLOCK for Phase 3 here before proceeding]

---

## Phase 4 -- Read, compare, and propose

Read each NEW artifact. For each strategy dimension, assess new signal coverage:

| Dimension       | In strategy? | NEW signal says | Assessment                              |
|-----------------|--------------|-----------------|-----------------------------------------|
| [fill]          | YES / NO     | [summary]       | VALIDATED / CHALLENGED / NOT COVERED / [NEW] |

Produce change proposals:

| # | Action               | Dimension | Evidence artifact  | Before | After | vs. NO CHANGE   |
|---|----------------------|-----------|--------------------|--------|-------|-----------------|
| [fill] | ADD / REMOVE / REPRIORITIZE | [fill] | [NEW filename] | [fill] | [fill] | [specific] |

Only NEW artifacts (Phase 3) may appear in the Evidence column.

Null declarations per change type (required -- labeled separately, not collectively):
  ADDITIONS: none -- [reason] / or [N] proposed above
  REMOVALS: none -- [reason] / or [N] proposed above
  REPRIORITIZATIONS: none -- [reason] / or [N] proposed above

Conflict audit (required even if null):
| Conflict ID | Signal A | Signal B | Dimension | Nature |
|-------------|----------|----------|-----------|--------|
If no conflicts: "CONFLICT AUDIT: none -- no contradictions between NEW artifacts."

Before/after diff (produce only if proposals exist):
| Dimension | Before | After | Proposal ref                      |
|-----------|--------|-------|-----------------------------------|
| [fill]    | [fill] | [fill]| ADD-N / REMOVE-N / REPRIORITIZE-N |

Gate condition: All Evidence artifacts appear in Phase 3 NEW list AND all three
change-type null declarations are written.

[Reproduce GATE BLOCK for Phase 4 here before proceeding]

---

## Phase 5 -- Confirmation gate

Display Phase 2 inventory, Phase 3 delta partition, Phase 4 proposals, and
Phase 4 before/after diff.

Write exactly:

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to
apply custom version
---

[Reproduce GATE BLOCK for Phase 5 here]

Stop. Write nothing further until the user replies.

---

## Apply (triggered by YES or REVISED)

Write exactly the confirmed changes to strategy.md. No additional edits.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-02: Pre-Scan Commitment Block — Lock Strategy State Before Artifact Access

**Variation axis**: Output format — a standalone COMMITMENT BLOCK is filled
immediately after reading strategy.md and before any directory listing or artifact
access. The block is explicitly marked LOCKED once Phase 2 begins.

**Hypothesis**: R1's V-04 had a "pre-signal defense register" but it was adjacent to
the inventory step header, not a hard ordering constraint. C-12 is satisfied only if
the strategy state commitment *precedes* the artifact listing itself in the output.
A distinct COMMITMENT BLOCK with explicit instruction "Output this BEFORE accessing
simulations/" makes the temporal ordering auditable in the output trace: the
commitment block must appear before any artifact table. The "Before" column in all
proposal rows must reference COMMITMENT BLOCK text, not re-read strategy.md,
preventing rationalization after the fact.

```
You are running /topic:plan for the topic named in the user's message.

---

## Step 1 -- Read strategy.md

Read `simulations/TOPICS.md` to locate the strategy file path for this topic.
Read strategy.md. Record its last-modified date as the STRATEGY DATE.

---

## Step 2 -- Write COMMITMENT BLOCK (output BEFORE accessing any signal files)

IMMEDIATELY after reading strategy.md and BEFORE listing any artifacts in
simulations/, output the following block with all fields filled. Do not proceed
to Step 3 until this block is written and complete.

  [COMMITMENT BLOCK -- written before artifact scan]
  Strategy file: [path]
  Strategy date: [YYYY-MM-DD]
  Dimensions:
    1. [dimension name] -- [one-line description]
    2. [dimension name] -- [one-line description]
    [continue for all dimensions found]
  Completion criteria (as stated in strategy.md):
    [list each criterion]
  Scope (quote or close paraphrase):
    [text from strategy.md]
  [END COMMITMENT -- LOCKED after this point]

This block represents the "before" state. It may not be modified after Step 3 begins.
Any proposal that changes a dimension listed here must explicitly name which line it
modifies.

---

## Step 3 -- Signal inventory

Now list every artifact in `simulations/` whose filename contains the topic slug.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|
| [fill]            | YYYY-MM-DD    | [fill]      | [fill]    |

NEW = artifact date > Strategy date from COMMITMENT BLOCK.
PRIOR = date <= Strategy date.

Assess all 9 namespaces (every namespace required, ABSENT is valid):

| Namespace | Artifact count | NEW count |
|-----------|----------------|-----------|
| scout     | [N]            | [N]       |
| draft     | [N]            | [N]       |
| review    | [N]            | [N]       |
| flow      | [N]            | [N]       |
| trace     | [N]            | [N]       |
| prove     | [N]            | [N]       |
| listen    | [N]            | [N]       |
| program   | [N]            | [N]       |
| topic     | [N]            | [N]       |

If no artifacts are NEW, write:
"STRATEGY IS CURRENT -- no new signals since [STRATEGY DATE]. No update warranted."
Stop here.

---

## Step 4 -- Read NEW artifacts and map to COMMITMENT BLOCK

Read each NEW artifact. PRIOR artifacts were available when strategy.md was written
and may not drive proposals.

For each dimension in the COMMITMENT BLOCK, assess whether NEW artifacts address it:

| Dimension (from COMMITMENT BLOCK) | NEW signal coverage | Assessment                  |
|-----------------------------------|---------------------|-----------------------------|
| [commitment dimension]            | [summary]           | VALIDATED / CHALLENGED / NOT COVERED |

For each dimension in NEW artifacts that is absent from the COMMITMENT BLOCK:

| New dimension found | Source artifact | Candidate ADD? |
|--------------------|-----------------|----------------|
| [name]             | [filename]      | YES / NO       |

---

## Step 5 -- Proposals

For each CHALLENGED or NOT COVERED dimension, and each Candidate ADD, evaluate
whether a change proposal is warranted. NO CHANGE is the default verdict.

| # | Action               | Dimension | Evidence artifact | Before (COMMITMENT BLOCK text) | After | vs. NO CHANGE |
|---|----------------------|-----------|--------------------|-------------------------------|-------|---------------|
| [fill] | ADD / REMOVE / REPRIORITIZE | [fill] | [NEW filename] | [exact text from COMMITMENT BLOCK] | [fill] | [specific reason] |

"Before" must quote or paraphrase COMMITMENT BLOCK text -- do not re-read strategy.md.

Null declarations per change type (each labeled separately):
  ADDITIONS: none -- [reason] / or [N] proposed above
  REMOVALS: none -- [reason] / or [N] proposed above
  REPRIORITIZATIONS: none -- [reason] / or [N] proposed above

Before/after diff (produce only if proposals exist):
| Dimension | Before                  | After  | Proposal ref |
|-----------|-------------------------|--------|--------------|
| [fill]    | [COMMITMENT BLOCK text] | [fill] | ADD-N / REMOVE-N / REPRIORITIZE-N |

---

## Step 6 -- Confirmation gate

Display Step 2 COMMITMENT BLOCK, Step 3 inventory, Step 4 coverage map, Step 5
proposals, and before/after diff.

Write exactly:

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to
apply custom version
---

Stop. Write nothing further until the user replies.

---

## Step 7 -- Apply (triggered by YES or REVISED)

Write exactly the confirmed changes to strategy.md. Do not reformat unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-03: Phrasing Register — Active Imperative, Present-Tense Directives

**Variation axis**: Phrasing register — every instruction is an active, present-tense
imperative addressed to the model as an actor executing right now; no conditional
language, no passive voice, no "should" or "may".

**Hypothesis**: R1 variations used formal documentation-style phrasing ("This table is
required", "Output this"). Formal phrasing describes what the output should look like.
Active imperative phrasing ("Write this now. Stop. Do not continue until you write
it.") treats each directive as live. The hypothesis is that present-tense imperatives
reduce drift under long context because each step reads as an instruction being issued
in the moment, not a background spec the model can satisfy partially and move on. This
is tested specifically against C-11 and C-12: both require strict temporal ordering
that benefits from commands rather than descriptions.

```
You are running /topic:plan for the topic named in the user's message.

Before you do anything else, read this twice: the default outcome is NO CHANGE to
strategy.md. Every proposal must earn its place.

---

## Step 1 -- Read strategy.md now

Open `simulations/TOPICS.md`. Find the strategy file path for this topic. Open it.

Write down these four things before you open any other file:

  STRATEGY FILE: [the path you just read]
  STRATEGY DATE: [the last-modified date, YYYY-MM-DD]
  STRATEGY DIMENSIONS: [list every dimension you found, comma-separated]
  STRATEGY CRITERIA: [list completion criteria as stated]

Copy one sentence from strategy.md here verbatim: "[paste it]"

STOP. Do not open any file in simulations/ until you have written the five lines above.

---

## Step 2 -- Lock your strategy picture

Write this commitment table now. Base it entirely on what you read in Step 1. Do not
look at any signal artifact yet.

| Dimension          | What strategy.md says             | What would force a revision              |
|--------------------|-----------------------------------|------------------------------------------|
| [fill]             | [direct quote or close paraphrase]| [specific signal type or finding]        |

Fill one row for every dimension in STRATEGY DIMENSIONS. Do not proceed to Step 3
until this table is complete.

Write this line: "Commitment table complete. No signal artifacts read yet."

---

## Step 3 -- List every artifact

Now list every file in `simulations/` whose name contains the topic slug.

For each file write one row:
  [filename] | [date] | NEW / PRIOR | [namespace]

NEW = artifact date is after STRATEGY DATE.
PRIOR = artifact date is on or before STRATEGY DATE.

Then assess each namespace. Write one line per namespace, all nine, even if empty:
  scout:   [N total] | [N new]
  draft:   [N total] | [N new]
  review:  [N total] | [N new]
  flow:    [N total] | [N new]
  trace:   [N total] | [N new]
  prove:   [N total] | [N new]
  listen:  [N total] | [N new]
  program: [N total] | [N new]
  topic:   [N total] | [N new]

If no artifacts are NEW, write: "No new signals since [STRATEGY DATE]. Strategy is
current. STOP -- no update warranted." And stop.

---

## Step 4 -- Read the NEW artifacts

Open each NEW artifact now. Read it. Do not re-open strategy.md.

Write a short paragraph about what you learned from the NEW artifacts. Mention at
least two artifact filenames by name. Do not compare to strategy.md yet -- just
describe what you found.

---

## Step 5 -- Challenge each dimension

Go back to your Step 2 commitment table. For each dimension, ask: does any NEW
artifact challenge what strategy.md says about this dimension?

Write one assessment line per dimension from Step 2:
  [Dimension] -- VALIDATED / CHALLENGED / NOT TOUCHED -- [one sentence] -- [artifact or "no NEW artifact"]

Then ask: do any NEW artifacts raise a dimension absent from Step 2?

Write one line for each absent dimension:
  [dimension name] -- ABSENT FROM STRATEGY -- from [artifact filename] -- CANDIDATE ADD

---

## Step 6 -- Write your proposals

Write exactly three sections. Do not skip any section. Do not collapse them into one.

ADDITIONS (new dimensions to add to strategy.md):
| # | Dimension | Evidence | Before | After | Why adding beats NO CHANGE          |
|---|-----------|----------|--------|-------|-------------------------------------|
If none: write "ADDITIONS: none -- inertia holds for all candidate additions."

REMOVALS (dimensions to remove from strategy.md):
| # | Dimension | Evidence | Before | After | Why removing beats NO CHANGE        |
|---|-----------|----------|--------|-------|-------------------------------------|
If none: write "REMOVALS: none -- inertia holds."

REPRIORITIZATIONS (changes to ordering or weighting in strategy.md):
| # | Dimension | Evidence | Before | After | Why reprioritizing beats NO CHANGE  |
|---|-----------|----------|--------|-------|-------------------------------------|
If none: write "REPRIORITIZATIONS: none -- inertia holds."

Before/after diff for each proposed change:
| Dimension | Before | After | Proposal ref |
|-----------|--------|-------|--------------|

Conflict scan -- two NEW artifacts that contradict each other on the same dimension:
  CONFLICT AUDIT: [list contradictions] / none -- no contradictions detected.

---

## Step 7 -- Stop and ask

Show Step 3 inventory, Step 5 assessment, Step 6 proposals, and the before/after diff.

Write this exactly:

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to
apply custom version
---

STOP. Do not write another word until the user replies.

---

## Step 8 -- Apply (after YES or REVISED)

Write the confirmed changes to strategy.md now. Change only what was confirmed. Do
not reformat anything you did not change.

Write: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-04: C-11 + C-12 Targeted Combination — Visible Gates + Locked Commitment

**Combination axes**: Lifecycle (GATE STATUS line visible in output at each phase
boundary, C-11) + Role sequence / Pre-scan commitment (COMMITMENT BLOCK locked before
any artifact access, C-12).

**Hypothesis**: C-11 and C-12 have orthogonal failure modes. C-11 fails when phases
are present in instructions but invisible or absent in output. C-12 fails when strategy
state is registered after or concurrently with the artifact scan, enabling backward
rationalization. These two failure modes are independent: a prompt can have visible
gates and still rationalize (C-12 fail), or pre-commit and still lack output-visible
gates (C-11 fail). Combining a GATE STATUS line (makes phase structure auditable in
output) with a LOCKED COMMITMENT BLOCK (makes pre-scan state auditable) addresses both
simultaneously. The prompt is sized to minimum-necessary length for the two targeted
criteria — avoiding the full overhead of V-05 while covering all 12 criteria via the
two new additions plus the R1 baseline structure.

```
You are running /topic:plan for the topic named in the user's message.

This skill has five phases. Two rules govern the entire run:

Rule 1 -- GATE STATUS: At the end of each phase, write exactly one line:
  [PHASE N GATE: PASS -- condition met] or [PHASE N GATE: STOP -- what is missing]
  If STATUS is STOP, complete the missing condition and rewrite the gate before advancing.

Rule 2 -- COMMITMENT BLOCK: Filled immediately after reading strategy.md (Phase 1),
  before any access to simulations/ artifacts. Format:
    [COMMITMENT BLOCK]
    Strategy file: [path]
    Strategy date: [YYYY-MM-DD]
    Dimensions: [list all]
    Completion criteria: [list as stated]
    Scope: [quote or paraphrase]
    [END COMMITMENT -- LOCKED]
  This block may not be modified once Phase 2 begins.

---

## Phase 1 -- Read strategy.md

Read `simulations/TOPICS.md` to locate the strategy file for this topic. Read
strategy.md. Fill and output the COMMITMENT BLOCK now, before opening any file
in simulations/.

Exit gate condition: COMMITMENT BLOCK is written with Strategy date, at least two
Dimensions, and Completion criteria filled.

[PHASE 1 GATE: PASS / STOP -- ...]

---

## Phase 2 -- Signal inventory

List every artifact in `simulations/` whose filename contains the topic slug.

| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|
| [fill]            | YYYY-MM-DD    | [fill]      | [fill]    |

NEW = artifact date > Strategy date from COMMITMENT BLOCK.
PRIOR = date <= Strategy date.

Assess all 9 namespaces (all rows required, ABSENT is valid):

| Namespace | Total | NEW |
|-----------|-------|-----|
| scout     |       |     |
| draft     |       |     |
| review    |       |     |
| flow      |       |     |
| trace     |       |     |
| prove     |       |     |
| listen    |       |     |
| program   |       |     |
| topic     |       |     |

Exit gate condition: All 9 namespace rows present with Total and NEW counts filled.

[PHASE 2 GATE: PASS / STOP -- ...]

---

## Phase 3 -- Delta detection

Partition inventory:
  NEW (date > COMMITMENT BLOCK strategy date): [list]
  PRIOR (date <= COMMITMENT BLOCK strategy date): [list]

PRIOR artifacts were available when strategy.md was written. They may not drive
proposals.

Exit gate condition: At least one NEW artifact exists.
If none: "STRATEGY CURRENT -- no new signals since [date]. No update needed."

[PHASE 3 GATE: PASS -- N new artifacts found / STOP -- no new artifacts, end here]

---

## Phase 4 -- Compare NEW signals to COMMITMENT BLOCK

Read each NEW artifact. Map findings to COMMITMENT BLOCK dimensions:

| Dimension (COMMITMENT BLOCK) | NEW signal finding       | Assessment                      |
|------------------------------|--------------------------|---------------------------------|
| [fill]                       | [summary from NEW files] | VALIDATED / CHALLENGED / NOT COVERED |

For each dimension in NEW artifacts absent from COMMITMENT BLOCK:
| New dimension | Source artifact | Status        |
|---------------|-----------------|---------------|
| [fill]        | [filename]      | CANDIDATE ADD |

Produce proposals (NO CHANGE is the default verdict):

| # | Action               | Dimension | Evidence artifact | Before (COMMITMENT BLOCK text) | After | vs. NO CHANGE |
|---|----------------------|-----------|--------------------|-------------------------------|-------|---------------|
| [fill] | ADD / REMOVE / REPRIORITIZE | [fill] | [NEW filename] | [COMMITMENT BLOCK text] | [fill] | [specific] |

Null declarations (each type labeled separately -- silence fails):
  ADDITIONS: none -- [reason] / or [N proposed above]
  REMOVALS: none -- [reason] / or [N proposed above]
  REPRIORITIZATIONS: none -- [reason] / or [N proposed above]

Conflict scan:
  CONFLICTS: [contradictions between NEW artifacts] / none detected.

Before/after diff (if proposals exist):
| Dimension | Before                  | After  | Proposal ref |
|-----------|-------------------------|--------|--------------|

Exit gate condition: All Evidence artifacts are from Phase 3 NEW list AND all three
null declarations are written.

[PHASE 4 GATE: PASS / STOP -- ...]

---

## Phase 5 -- Confirmation gate

Display Phase 1 COMMITMENT BLOCK, Phase 2 inventory, Phase 3 delta, Phase 4
proposals, and Phase 4 before/after diff.

Write exactly:

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to
apply custom version
---

[PHASE 5 GATE: PASS -- awaiting user confirmation]

Stop. Write nothing further until the user replies.

---

## Apply (triggered by YES or REVISED)

Write exactly the confirmed changes to strategy.md. No additional edits.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## V-05: Full R2 Combination — All 12 Criteria

**Combination axes**: Pre-committed schemas (V-01 / R1) + Inertia opening premise
(V-02 / R1) + GATE STATUS output line per phase (C-11 from R2 V-01) + COMMITMENT
BLOCK locked before scan (C-12 from R2 V-02) + Type-labeled nulls (C-09) + Conflict
detection (C-10) + Before/after diff (C-07) + Evidence citation (C-06).

**Hypothesis**: R1's V-05 achieved all 10 R1 criteria by combining pre-committed
schemas, inertia framing, phase gates, and type-labeled nulls. R2 adds two structural
upgrades:
- GATE STATUS line is an explicit output artifact the model writes at each phase
  boundary (C-11 upgrade: gate becomes output-visible, not just instruction-level)
- Schema A is a COMMITMENT BLOCK that must be filled before any simulations/ access
  begins (C-12 addition: the pre-scan state is locked in the output trace)
All other R1 V-05 mechanisms are retained. The combination targets all 12 criteria.
Length risk is mitigated by the GATE STATUS lines acting as checkpoints that reset
attention at each phase boundary.

```
You are running /topic:plan for the topic named in the user's message.

---

## Opening premise

The default outcome of this skill is NO CHANGE to strategy.md. Inertia is a
co-equal option, not a fallback. The burden of proof rests on change, not on
stability. This premise governs every proposal gate below.

---

## Pre-committed output schema

Declare now, before reading any file. All schemas below will be filled exactly
as shown. No schema may be replaced by prose. No schema may be omitted.
No two schemas may be merged.

**Schema A -- Strategy commitment** (filled in Phase 1, BEFORE any artifact access;
LOCKED once Phase 2 begins -- may not be modified to reflect what artifacts say)
| Item                | Value                            |
|---------------------|----------------------------------|
| Strategy file       | [path]                           |
| Strategy date       | YYYY-MM-DD                       |
| Dimensions (all)    | [comma-separated list]           |
| Completion criteria | [list as stated in strategy.md]  |
| Scope               | [quote or paraphrase]            |

**Schema B -- Signal inventory**
| Artifact filename | Artifact date | NEW / PRIOR | Namespace |
|-------------------|---------------|-------------|-----------|

**Schema C -- Namespace audit (all 9 rows required)**
| Namespace | Total | NEW | Status           |
|-----------|-------|-----|------------------|
| scout     |       |     | COVERED / ABSENT |
| draft     |       |     | COVERED / ABSENT |
| review    |       |     | COVERED / ABSENT |
| flow      |       |     | COVERED / ABSENT |
| trace     |       |     | COVERED / ABSENT |
| prove     |       |     | COVERED / ABSENT |
| listen    |       |     | COVERED / ABSENT |
| program   |       |     | COVERED / ABSENT |
| topic     |       |     | COVERED / ABSENT |

**Schema D -- Signal-to-dimension coverage map**
| Dimension (Schema A)  | NEW signal finding | Assessment                              |
|-----------------------|--------------------|-----------------------------------------|

**Schema E -- Additions proposals**
| # | Dimension | Evidence artifact | Before (Schema A text) | After | vs. NO CHANGE |
|---|-----------|------------------|------------------------|-------|---------------|

**Schema F -- Removals and Reprioritizations proposals**
| # | Action               | Dimension | Evidence artifact | Before (Schema A text) | After | vs. NO CHANGE |
|---|----------------------|-----------|--------------------|------------------------|-------|---------------|

**Schema G -- Before/after diff**
| Dimension | Before | After | Proposal ref                      |
|-----------|--------|-------|-----------------------------------|

**Schema H -- Conflict audit**
| Conflict ID | Signal A | Signal B | Dimension | Nature | Resolution |
|-------------|----------|----------|-----------|--------|------------|

---

## Phase 1 -- Read strategy.md

Read `simulations/TOPICS.md` to locate the strategy file for this topic. Read
strategy.md.

Fill Schema A now. Schema A is LOCKED once Phase 2 begins. It records only what
strategy.md says -- not what artifacts say. Quote at least one sentence from
strategy.md to confirm you read it.

Write exactly one of:
  [PHASE 1 GATE: PASS -- Schema A filled with Strategy date, Dimensions, and Criteria]
  [PHASE 1 GATE: STOP -- [missing field] -- fill before advancing]

Do not begin Phase 2 until PHASE 1 GATE shows PASS.

---

## Phase 2 -- Signal inventory and namespace audit

List every artifact in `simulations/` whose filename contains the topic slug.
Fill Schema B (all artifacts). Fill Schema C (all 9 namespace rows).

Classify: NEW = artifact date > Schema A Strategy date. PRIOR = date <= Strategy date.

Write exactly one of:
  [PHASE 2 GATE: PASS -- Schema B filled, Schema C has all 9 rows with counts]
  [PHASE 2 GATE: STOP -- [missing rows] -- fill before advancing]

Do not begin Phase 3 until PHASE 2 GATE shows PASS.

---

## Phase 3 -- Delta detection

Partition Schema B:

  NEW (date > Schema A Strategy date):
  - [filename] | [date]

  PRIOR (date <= Schema A Strategy date):
  - [filename] | [date]

PRIOR artifacts may not drive proposals. They were available when strategy.md
was written.

Write exactly one of:
  [PHASE 3 GATE: PASS -- [N] NEW artifacts identified]
  [PHASE 3 GATE: STOP -- no NEW artifacts. Write: "STRATEGY CURRENT -- no new
  signals since [date]. No update warranted." End here.]

Do not begin Phase 4 until PHASE 3 GATE shows PASS.

---

## Phase 4 -- Read NEW artifacts

Read each NEW artifact. Write a short paragraph (no structure, no headings) about
what they reveal collectively. Name at least two artifacts by filename. Do not
compare to Schema A yet.

Write exactly one of:
  [PHASE 4 GATE: PASS -- paragraph written, at least 2 filenames cited]
  [PHASE 4 GATE: STOP -- paragraph missing or no filenames -- write before advancing]

---

## Phase 5 -- Coverage map

Fill Schema D: map each dimension from Schema A against NEW artifact findings.
For each NEW artifact dimension absent from Schema A, add a row with Assessment "[NEW]".

Write exactly one of:
  [PHASE 5 GATE: PASS -- all Schema A dimensions have a row in Schema D]
  [PHASE 5 GATE: STOP -- [missing dimensions] -- complete before advancing]

---

## Phase 6 -- Proposals

Reminder: NO CHANGE is the default verdict.

Fill Schema E (Additions). Fill Schema F (Removals / Reprioritizations).

For each proposal row:
- Evidence artifact must appear in the Phase 3 NEW list
- "vs. NO CHANGE" must name the specific consequence of NOT changing -- not a
  generic phrase
- "Before" must reference Schema A text directly -- do not re-read strategy.md

Null declarations (required -- labeled per type -- a single unlabeled "no changes"
covering multiple types fails this requirement):
  ADDITIONS: none -- [reason] / or [N] proposed in Schema E
  REMOVALS: none -- [reason] / or [N] proposed in Schema F
  REPRIORITIZATIONS: none -- [reason] / or [N] proposed in Schema F

Fill Schema G (before/after diff) for every row in Schema E and Schema F.

Fill Schema H (conflict audit). Identify any two NEW artifacts that contradict
each other on the same dimension. If none:
  "CONFLICT AUDIT: none -- no contradictions detected between NEW artifacts."

Write exactly one of:
  [PHASE 6 GATE: PASS -- all three null declarations written, Schema G and H filled]
  [PHASE 6 GATE: STOP -- [missing declaration or schema] -- complete before advancing]

Do not begin Phase 7 until PHASE 6 GATE shows PASS.

---

## Phase 7 -- Confirmation gate

Display Schema A, Schema B, Schema C, Schema D, Schema E, Schema F, Schema G,
Schema H.

Write exactly:

---
PENDING CONFIRMATION -- strategy.md has NOT been modified.

Proposed: [N] additions / [N] removals / [N] reprioritizations

Reply YES to apply | NO to keep strategy.md unchanged | REVISED + edited table to
apply custom version
---

[PHASE 7 GATE: PASS -- awaiting user confirmation]

Stop. Write nothing further until the user replies.

---

## Apply (triggered by YES or REVISED)

Write exactly the confirmed changes to strategy.md. Do not reformat unchanged sections.
Confirm: "strategy.md updated: [N] additions, [N] removals, [N] reprioritizations."
```

---

## Round 2 Variation Summary

| Variation | Primary axis | C-11 mechanism | C-12 mechanism | Key R2 addition vs R1 |
|-----------|-------------|----------------|----------------|------------------------|
| V-01 | Lifecycle (gate syntax) | GATE BLOCK template reproduced in output at each phase; absence is visible | None (no pre-scan commitment) | Output-visible gate artifact vs instruction-only gate in R1 V-03 |
| V-02 | Output format (commitment block) | None (no output-visible gates) | COMMITMENT BLOCK written and output before Step 3 artifact access; "Before" column references block text | Named commitment block vs embedded defense register in R1 V-04 |
| V-03 | Phrasing register (active imperative) | "STOP. Do not open any file in simulations/ until..." -- ordering enforced by imperative | "Write this down BEFORE you open any other file" -- commitment via imperative stop directive | Active-tense ordering vs conditional description in R1 variations |
| V-04 | Combination (C-11 + C-12 targeted) | GATE STATUS line at each phase boundary | COMMITMENT BLOCK locked before Phase 2 artifact access | Minimum-necessary combination targeting both new criteria without full V-05 overhead |
| V-05 | Full R2 combination | GATE STATUS line per phase (output artifact) + Schema A locked as commitment | Schema A filled as COMMITMENT before any simulations/ access; "Before" columns reference Schema A text | All 12 criteria; Schema A = commitment block; gate status = phase visibility |

**Structural risk ranking** (lowest risk first): V-05 > V-04 > V-01 > V-02 > V-03

V-05 encodes all 12 criteria: Schema A as locked pre-scan commitment (C-12), GATE
STATUS output lines per phase (C-11), pre-committed schema slots (C-01 through C-05),
inertia premise + per-proposal "vs. NO CHANGE" column (C-08), evidence citation (C-06),
before/after diff (C-07), type-labeled nulls (C-09), conflict audit (C-10).

V-03 is highest risk: active imperative phrasing is effective at short context but is
most susceptible to drift under long runs where stop directives are distant from the
action they govern.
