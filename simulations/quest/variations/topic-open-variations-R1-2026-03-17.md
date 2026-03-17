Good. I have the rubric, the current (minimal) skill body, and the full ecosystem context. Generating 5 variations now.

---

# topic-open Variations — Round 1

**Skill**: Register a new topic, define its strategy, plan the signals needed for design commit.
**Rubric**: `simulations/quest/rubrics/topic-open-rubric-v1-2026-03-17.md`
**Key failure to suppress**: C-04 — models substitute `high/medium/low` for `essential/recommended/optional`.

---

## V-01 — Axis: Phrasing Register (imperative + hard constraints stated upfront)

**Hypothesis**: Stating the priority vocabulary as a hard constraint before any instructions prevents C-04 substitution. Imperative commands reduce ambiguity about what is required vs optional.

```
You are opening a new Signal topic. A topic is a named investigation. Opening it means
two things: registering it in TOPICS.md and writing a strategy that plans every signal
the team intends to gather before design commit.

---

HARD CONSTRAINTS — read before doing anything else:

1. Priority values are EXACTLY: essential | recommended | optional
   Never substitute: high/medium/low, must/should/could, critical/normal/low.
   Using any other vocabulary silently breaks downstream commit gate logic.

2. Every signal row must contain all five fields:
   namespace | skill | item name | owner role | priority
   No field may be omitted. No two fields may be collapsed into one.

3. At least one signal must have priority = essential.
   A strategy with no essential signals has no commit gate and is useless.

4. The strategy file goes to: simulations/{topic}/strategy.md
   Not inline in TOPICS.md. Not at a flat path.

---

STEP 1 — TOPICS.md

Read simulations/TOPICS.md.
Append one row with: topic slug | short description | date (YYYY-MM-DD).
Write the file.

STEP 2 — Strategy rationale

Before listing signals, write 2-4 sentences:
- What decision does this topic inform?
- What would happen if we committed to design without investigating it?
The rationale is what separates a useful strategy from a mechanical table.

STEP 3 — Signal plan

List every signal the topic needs. For each:
  namespace  — one of: scout draft review flow trace prove listen program topic
  skill      — the specific skill that produces this signal (e.g., scout-competitors)
  item name  — {topic}-{signal}-{date}.md (use today's date or a placeholder date)
  owner role — the role responsible for running the skill
  priority   — essential | recommended | optional (see constraint 1 above)

Use at least 2 distinct namespaces.
Assign at least 2 distinct owner roles across the signal set.

STEP 4 — Commit gate

Write a COMMIT GATE section naming the exact signals (by item name) that must exist
before design commit. The gate is not implicit. A reader must be able to evaluate
whether the gate is met without re-reading the full strategy.

STEP 5 — Write artifact

Write the complete strategy to: simulations/{topic}/strategy.md

Format: markdown. Sections: Rationale, Signals (table), Commit Gate.
```

---

## V-02 — Axis: Output Format (prose rationale first, table driven by rationale)

**Hypothesis**: Requiring prose rationale before the signal table forces the model to ground signal selection in a real decision, improving C-07 and making C-08 (differentiated roles) more natural because different roles address different aspects of the decision.

```
Register a new topic, define its strategy, plan the signals needed for design commit.

Output:
  1. An entry in simulations/TOPICS.md
  2. A strategy file at simulations/{topic}/strategy.md

---

THE STRATEGY FILE HAS TWO PARTS IN THIS ORDER:

Part A — Rationale (write this first)

Answer in prose, at least 2 sentences:
  - Why does this topic need investigation?
  - What design decision will the signals inform?
  - What is the cost of skipping investigation and committing without signals?

The rationale determines which signals matter. Write it before choosing signals.

Part B — Signal table (derive from rationale)

For each signal your rationale implies, create one table row:

| namespace | skill | item name | owner role | priority |

Column definitions:
  namespace  — the namespace this signal comes from (scout/draft/review/flow/trace/prove/listen/program/topic)
  skill      — the specific skill that produces this artifact
  item name  — artifact filename following: {topic}-{signal}-{date}.md
  owner role — who runs this skill; vary roles across signals to reflect real ownership
  priority   — MUST be exactly one of: essential | recommended | optional
               Do NOT use: high/medium/low or any other scale.
               essential = required for commit gate
               recommended = strong value but not a blocker
               optional = low cost, run if time permits

Signal set requirements:
  - At least one priority = essential (otherwise there is no commit gate)
  - At least 2 distinct namespaces represented
  - At least 2 distinct owner roles

---

COMMIT GATE (end of strategy file)

After the table, write a COMMIT GATE section:
List the item names of every essential signal. These are the artifacts that must exist
before the team may commit to this design. Make the list explicit — do not say "all essential signals."

---

TOPICS.md entry

Append to simulations/TOPICS.md:
  | {slug} | {one-sentence description} | {YYYY-MM-DD} |

Write simulations/TOPICS.md, then write simulations/{topic}/strategy.md.
```

---

## V-03 — Axis: Lifecycle Emphasis (explicit SETUP / EXECUTE / WRITE / AMEND phases)

**Hypothesis**: Structuring the skill as named lifecycle phases (matching Signal's 4-phase pattern) prevents the model from collapsing or skipping steps, especially the AMEND phase that prompts the commit gate.

```
You are running /topic-new. This skill follows the 4-phase Signal lifecycle.

---

PHASE 1 — SETUP

Determine:
  a. Topic slug (from user input or context)
  b. Today's date (for artifact naming)
  c. Existing topics: read simulations/TOPICS.md

Check: is this topic already registered? If yes, stop and report.
If no, continue.

---

PHASE 2 — EXECUTE: Draft the strategy

2a. Write the rationale (2-4 sentences):
    What is this topic investigating? What decision does it gate?
    What risk does uninvestigated commitment carry?

2b. Enumerate signals:
    For each signal, determine all five fields:

    FIELD 1 — namespace: scout | draft | review | flow | trace | prove | listen | program | topic
    FIELD 2 — skill: the sub-skill that produces this artifact
    FIELD 3 — item name: {topic}-{signal}-{date}.md
    FIELD 4 — owner role: who is responsible for running this skill
    FIELD 5 — priority: essential | recommended | optional
              STOP — do not use high/medium/low. The only valid values are the three above.
              essential = gates commit. recommended = valuable. optional = run if time allows.

    Constraints:
    - Minimum 1 signal with priority = essential
    - Minimum 2 distinct namespaces
    - Minimum 2 distinct owner roles

2c. Identify the commit gate:
    List the item names of all essential signals. This is the minimal set for design commit.

---

PHASE 3 — WRITE

Write 1: Append to simulations/TOPICS.md
  New row: | {slug} | {description} | {date} |

Write 2: Create simulations/{topic}/strategy.md
  Structure:
  ## Rationale
  {your prose from 2a}

  ## Signals
  | namespace | skill | item name | owner role | priority |
  {rows from 2b}

  ## Commit Gate
  Design commit requires all of the following signals to exist:
  {item names from 2c}

---

PHASE 4 — AMEND

Review the strategy before finalizing:
  - Did every row get all 5 fields?
  - Did any row use high/medium/low instead of essential/recommended/optional?
  - Is there at least one essential signal?
  - Does the commit gate name specific item names (not just "all essential")?

Fix any violations. Write final files.
```

---

## V-04 — Axis: Inertia Framing (name the status-quo competitor prominently)

**Hypothesis**: Framing the skill against the status quo (ad-hoc notes, no strategy, implicit gates) motivates the model to produce a more complete output because it understands what it is replacing and why completeness matters.

```
Without /topic-new, teams open features by starting work. There is no registration.
There is no signal plan. Commit gates are implicit or absent. Investigation happens
reactively after design decisions have calcified.

/topic-new replaces ad-hoc investigation with a deliberate editorial plan: here is
what we need to know, who will gather it, and what must exist before we commit.

---

Run /topic-new for the current topic. Produce two outputs:

OUTPUT 1 — TOPICS.md entry

The status quo: topics are tracked in people's heads or in Notion. The Signal
equivalent is a single row in simulations/TOPICS.md.

Read simulations/TOPICS.md.
Append: | {slug} | {one-sentence description} | {YYYY-MM-DD} |
Write the file.

OUTPUT 2 — strategy.md

Path: simulations/{topic}/strategy.md
(Not inline in TOPICS.md. Not in a flat directory. At the exact path above.)

The strategy is what a committed-but-uninvestigated decision lacked. Write it in
two sections:

SECTION A — Rationale
Why does this topic need signals before commit? What decision does it gate?
What would a team who skipped this step not know? (2-4 sentences.)

SECTION B — Signal plan
For each signal you plan to gather, one table row:

| namespace | skill | item name | owner role | priority |

Priority vocabulary — THIS IS LOAD-BEARING:
  Use ONLY: essential | recommended | optional
  Do NOT use: high/medium/low, P0/P1/P2, critical/normal/low, or any other scale.
  The commit gate logic downstream reads these exact strings. Wrong vocabulary = silent
  breakage. This is the most common mistake in topic strategy files.

  essential   = this signal must exist before design commit
  recommended = strongly valuable; investigate if not time-constrained
  optional    = low cost; gather if investigation is already open

At minimum:
  - One signal marked essential (otherwise the strategy has no commit gate)
  - Two or more distinct namespaces (scout, draft, review, flow, trace, prove, listen, program, topic)
  - Two or more distinct owner roles

SECTION C — Commit Gate
End the strategy with an explicit list of item names (not "all essential signals" —
the actual names) that must exist before design commit. Without this section, the
commit gate is implicit — the same failure mode the skill is designed to prevent.
```

---

## V-05 — Axis: Combination (imperative constraints + prose-first + phase structure + inertia framing)

**Hypothesis**: Combining hard vocabulary constraints (V-01), prose-before-table sequencing (V-02), named lifecycle phases (V-03), and inertia framing (V-04) produces the most rubric-complete output by eliminating each failure mode at the point where it arises.

```
/topic-new replaces the default: starting work without a signal plan. The output is
two artifacts — a TOPICS.md entry and a strategy file — that together define what the
team intends to learn before committing to this design.

---

VOCABULARY CONSTRAINT (enforce throughout):

Priority values in this skill are EXACTLY:
  essential | recommended | optional

These are the only valid values. Do not use: high/medium/low, critical/minor, P0/P1,
must/should/could, or any other scale. The commit gate evaluator reads these exact
strings. Any substitution silently disables the gate.

---

PHASE 1 — SETUP

1. Read simulations/TOPICS.md.
2. Determine the topic slug from user input or context.
3. Verify the topic is not already registered. If it is, stop.

---

PHASE 2 — RATIONALE (write before signals)

Before listing any signals, write 2-4 sentences answering:
  - What does this topic investigate?
  - What design decision will the signals inform?
  - What is the cost of committing without signals — what would not be known?

The rationale is the editorial contract for the signal plan. Without it, the
strategy is a table without a reason.

---

PHASE 3 — SIGNAL PLAN

For each signal implied by the rationale, define all five fields:

  namespace  — one of: scout draft review flow trace prove listen program topic
  skill      — specific sub-skill (e.g. scout-competitors, prove-hypothesis)
  item name  — {topic}-{signal}-{date}.md  (use YYYY-MM-DD format for date)
  owner role — role responsible; vary across signals to reflect real ownership
  priority   — essential | recommended | optional  (see vocabulary constraint above)

Signal set must satisfy:
  [ ] At least 1 signal with priority = essential
  [ ] At least 2 distinct namespaces
  [ ] At least 2 distinct owner roles

---

PHASE 4 — COMMIT GATE

Write a COMMIT GATE section listing the item names (not a description — the actual
filenames) of every essential signal. These are the artifacts whose existence allows
the team to commit to design. The gate must be evaluable without re-reading the table.

Example form:
  ## Commit Gate
  The following signals must exist before design commit:
  - {topic}-competitors-2026-03-17.md
  - {topic}-feasibility-2026-03-17.md

---

PHASE 5 — WRITE

Write 1: Append to simulations/TOPICS.md
  | {slug} | {one-sentence description} | {YYYY-MM-DD} |

Write 2: simulations/{topic}/strategy.md
  ## Rationale
  {from phase 2}

  ## Signals
  | namespace | skill | item name | owner role | priority |
  {rows from phase 3}

  ## Commit Gate
  {from phase 4}

---

PHASE 6 — SELF-CHECK (before finalizing)

Read back the strategy. Verify:
  [ ] Every row has all 5 fields (namespace, skill, item name, owner role, priority)
  [ ] Every priority value is exactly: essential | recommended | optional
  [ ] At least one row has priority = essential
  [ ] Commit Gate names specific item filenames
  [ ] Strategy path is simulations/{topic}/strategy.md

Fix any violations. Write final files.
```

---

## Variation Summary

| Var | Axis | Primary Hypothesis | C-04 defense | C-09 defense |
|-----|------|--------------------|-------------|-------------|
| V-01 | Phrasing register — imperative + constraints upfront | Hard rules first prevents vocabulary drift | Explicit constraint block before instructions | Explicit STEP for commit gate |
| V-02 | Output format — prose-first, table-second | Rationale grounds signal selection; roles emerge naturally | Column definition names exact strings | Named COMMIT GATE section required |
| V-03 | Lifecycle emphasis — 4 named phases | Phase structure prevents step collapse or omission | STOP callout inside field definitions | Phase 4 derives gate from Phase 2 |
| V-04 | Inertia framing — status quo named prominently | Understanding what is replaced motivates completeness | Load-bearing vocabulary callout with breakage explanation | Section C = explicit gate requirement |
| V-05 | Combination — all four axes | Each failure mode suppressed at the point it arises | Vocabulary constraint block + self-check | Phase 4 dedicated to gate + self-check item |
