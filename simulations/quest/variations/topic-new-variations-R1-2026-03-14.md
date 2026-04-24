Written to `simulations/quest/variations/topic-new-variations-R1-2026-03-14.md`.

---

## Round 1 Variations — Summary

| V | Axis | Key mechanism |
|---|------|---------------|
| **V-01** | Output format | Pre-printed table schema with `Priority (essential/recommended/optional)` column header prevents C-04 by making the column title itself the vocabulary |
| **V-02** | Phrasing register | Short declarative imperatives + one-line exclusion note; tests whether terse register reduces drift |
| **V-03** | Lifecycle emphasis | Hard `GATE:` lines between Setup/Execute/Findings phases; forces the model to complete all five fields before advancing |
| **V-04** | Format + priority enforcement | Pre-printed template + two-point vocabulary definition: once at the column header, once as a named exclusion list |
| **V-05** | All axes combined | Pre-printed headers at every failure surface: exclusion list (C-04), coverage gate checklist (C-05), pre-printed Commit Gate section (C-09), Naming Reference section (C-10) |

**Predicted ceiling:** V-05 — every criterion has a structural pre-print, no criterion can be silently omitted. V-04 is the nearest competitor. V-01 is the minimal test: does schema-by-column-header alone hold?

**Hardest criterion across all variations:** C-04. V-01 and V-02 give it one enforcement point each. V-03 gives it a gate. V-04 gives it two points (header + exclusion list). V-05 gives it three (header + exclusion list + coverage gate checklist).
 values inline at the table header.
**Hypothesis:** If the model sees a pre-printed table with a `Priority (essential/recommended/optional)`
column header before writing any rows, it will not substitute "high/medium/low." The template acts
as a schema, not a style guide.

```
You are running /topic:new.

Your job: register a new topic and produce its signal strategy.

Two artifacts are produced by this skill:
1. An entry in TOPICS.md
2. A strategy file at simulations/{topic}/strategy.md

---

INPUT: Read the topic name, one-line description, and (optional) target outcome from the user's
invocation. If any are missing, ask once and wait for the answer before proceeding.

---

STEP 1 — REGISTER IN TOPICS.md

Read simulations/TOPICS.md (create it if absent). Append one row:

| Topic | Description | Started | Status |
|-------|-------------|---------|--------|
| {topic} | {one-line description} | {today} | active |

Write the updated file.

---

STEP 2 — WRITE STRATEGY

Write simulations/{topic}/strategy.md. The strategy has three sections.

### Rationale

Write 2–4 sentences: why does this topic need investigation? What decision does it inform?
What happens if the team commits to a design without it?

### Signal Plan

Fill this table. Every row must fill every column. Do not leave any cell blank.

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|
| (one of: scout/draft/review/flow/trace/prove/listen/program/topic) | (skill within that namespace) | {topic}-{item}-{date}.md | (PM / developer / architect / designer / researcher / other) | (essential / recommended / optional) |

Rules:
- Priority column accepts ONLY these three values: essential, recommended, optional.
  Do not write: high, medium, low, required, nice-to-have, or any other value.
- At least one row must be marked essential. A strategy with no essential signals has no
  defined commit gate and is invalid.
- Aim for signals from at least 2 distinct namespaces.
- Use at least 2 distinct owner roles across the rows.

### Commit Gate

State explicitly what the minimal signal set is before design commit. Example:
"All essential signals gathered + at least 2 recommended."

---

STEP 3 — CONFIRM

Print to terminal:
  Topic registered: {topic}
  Strategy written: simulations/{topic}/strategy.md
  TOPICS.md updated.
  Essential signals: {count}
  Total signals planned: {count}
```

---

## V-02: Phrasing Register

**Axis:** Phrasing register -- conversational/imperative register ("Ask. Confirm. Write.") with
short declarative sentences rather than spec-style prose. Tests whether reduced syntactic
complexity keeps the model from drifting on structural requirements.
**Hypothesis:** Shorter, more direct instructions reduce the chance the model paraphrases the
priority vocabulary. A model that copies "essential / recommended / optional" from a short
direct line is less likely to drift than one processing a long paragraph.

```
You are running /topic:new. Two outputs: a TOPICS.md entry and a strategy file.

1. COLLECT INPUT

Ask for anything missing:
- Topic name (short slug, no spaces -- e.g., frogs, atlas, sync)
- One-line description of the feature
- Target outcome (optional -- e.g., design commit, go/no-go, spec draft)

Do not proceed until you have at least topic name and description.

2. UPDATE TOPICS.md

Open simulations/TOPICS.md. Create it if missing.
Add one row: topic | description | today's date | active.
Save.

3. WRITE RATIONALE

Open simulations/{topic}/strategy.md. Create it fresh.
Write a short rationale section -- 2 to 4 sentences. Answer:
- Why does this feature need investigation before committing?
- What decision does the strategy inform?

4. PLAN SIGNALS

Write a table of planned signals. Every signal gets five fields:

  Namespace | Skill | Item name | Owner role | Priority

Item name format: {topic}-{slug}-{date}.md

Priority must be one of exactly three values:
  essential   <- needed before design commit
  recommended <- deepens confidence, not blocking
  optional    <- only if time permits

No other values. Not "high". Not "required". Not "nice-to-have".

Rules:
- At least one signal must be essential. No essential signals = no commit gate = invalid strategy.
- Cover at least 2 namespaces.
- Use at least 2 distinct owner roles (PM, developer, architect, designer, researcher, etc.).

5. WRITE COMMIT GATE

Add a sentence after the table stating what the minimum signal set is before the team can
commit to a design. E.g.: "Gate: all essential signals complete + at least 1 recommended."

6. PRINT SUMMARY

Print to terminal:
  Topic registered: {topic}
  Strategy written: simulations/{topic}/strategy.md
  TOPICS.md updated.
```

---

## V-03: Lifecycle Emphasis

**Axis:** Lifecycle emphasis -- explicit Setup / Execute / Findings phase boundaries with
hard gates between them. Tests whether treating the skill as a phased workflow prevents
field omission at the Execute phase.
**Hypothesis:** When each phase is named and bounded, the model treats the signal table as
an execution output (not a summary), and is less likely to skip required fields or collapse
phases together.

```
You are running /topic:new in lightweight mode.

This skill runs in three phases: SETUP, EXECUTE, FINDINGS.
Complete each phase before proceeding to the next.

---

## PHASE 1: SETUP

Identify the topic parameters from the user's invocation:
- Topic name: a short slug (no spaces, no dashes) -- e.g., frogs, atlas, sim
- Description: one sentence describing the feature under investigation
- Target outcome: what decision will this investigation inform? (If not provided, infer from
  description and ask the user to confirm.)

GATE: Do not begin PHASE 2 until topic name and description are confirmed.

---

## PHASE 2: EXECUTE

Two sub-tasks run in order:

### 2a. Register the topic

Read simulations/TOPICS.md (create if absent).
Add one row to the registry table:

| Topic | Description | Started | Status |
|-------|-------------|---------|--------|
| {topic} | {description} | {date} | active |

Write the file.

### 2b. Build the signal plan

Determine which signals this topic needs. For each signal, record:

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|

Column rules:
- Namespace: one of scout, draft, review, flow, trace, prove, listen, program, topic
- Skill: the skill within that namespace (e.g., feasibility, users, state, hypothesis)
- Item name: follows the convention {topic}-{slug}-{date}.md
- Owner role: who runs this signal (PM, developer, architect, designer, researcher, ...)
- Priority: exactly one of these three values -- essential / recommended / optional
  WARNING: Do not use high/medium/low or any substitute. Only these three values are valid.

Coverage requirements:
- At least one signal marked essential (if none, the strategy has no commit gate)
- At least 2 distinct namespaces represented
- At least 2 distinct owner roles

GATE: Do not begin PHASE 3 until the signal table is complete with all five columns filled.

---

## PHASE 3: FINDINGS

Write simulations/{topic}/strategy.md with this structure:

```markdown
# Strategy: {topic}
*{description}*
*Target outcome: {target outcome}*
*Date: {date}*

## Rationale

[2-4 sentences: why this topic needs investigation, what decision it informs,
what the cost is of committing without it]

## Signal Plan

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|
[rows from PHASE 2]

## Commit Gate

[State explicitly: the minimum signal set required before design commit]
```

After writing, print:
  Topic registered: {topic}
  Strategy: simulations/{topic}/strategy.md
  TOPICS.md updated.
  Essential signals: {count} / {total}
```

---

## V-04: Output Format + Priority Enforcement

**Axes:** Output format (pre-printed template) + priority enforcement (vocabulary defined twice --
once at schema level, once as a negative example list).
**Hypothesis:** Defining the priority vocabulary at two points in the prompt (column header + an
explicit exclusion list) makes substitution structurally harder. The exclusion list ("not high,
not required, not critical") triggers a negative-example check that pre-printing alone may not.

```
You are running /topic:new. Produce two artifacts: a TOPICS.md entry and a strategy file.

INPUT

Read from the user's invocation:
- topic: short slug, no spaces (e.g., frogs, atlas, vault)
- description: one line describing the feature
- target: what decision this investigation supports (optional; infer if absent)

If topic or description is missing, ask once and wait.

---

ARTIFACT 1: TOPICS.md entry

Path: simulations/TOPICS.md
Action: Read, append row, write.

| Topic | Description | Started | Status |
|-------|-------------|---------|--------|
| {topic} | {description} | {today} | active |

---

ARTIFACT 2: simulations/{topic}/strategy.md

Write the file with the following sections. Do not omit any section.

### Rationale

[2-4 sentences explaining why this feature cannot be committed to without investigation.
Answer: what decision does this strategy inform? What is the cost of skipping it?]

### Signal Plan

The priority column accepts exactly three values:
  essential       <- signal is required before design commit
  recommended     <- signal deepens confidence but is not blocking
  optional        <- signal is useful only if time allows

INVALID values (do not use): high, medium, low, required, critical, nice-to-have, P1, P2, P3.

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|
| scout/draft/review/flow/trace/prove/listen/program/topic | {skill} | {topic}-{slug}-{date}.md | PM/developer/architect/designer/researcher | essential/recommended/optional |

Requirements:
- Every row fills every column. No blank cells.
- At least one row is marked essential. (No essential = invalid. A topic with no essential
  signals has no commit gate and cannot be used to govern design decisions.)
- At least 2 distinct namespaces appear in the Namespace column.
- At least 2 distinct owner roles appear in the Owner role column.
- Item name follows: {topic}-{slug}-{date}.md

### Commit Gate

Complete this sentence: "Design commit is permitted when: [list the minimum signal set]."

Example: "Design commit is permitted when: all essential signals are gathered and at
least 2 recommended signals are gathered."

---

TERMINAL OUTPUT

After writing both artifacts:
  Topic registered: {topic}
  Strategy: simulations/{topic}/strategy.md
  TOPICS.md updated.
  Essential signals: {count}
  Recommended: {count}
  Optional: {count}
  Namespaces covered: {list}
```

---

## V-05: Full Structure (All Axes)

**Axes:** Pre-printed template + explicit phase gates + inline vocabulary (defined + exclusion
list) + commit gate section pre-printed + naming convention pre-printed. Maximum enforcement
surface across all failure modes.
**Hypothesis:** When every structural requirement is encoded as a pre-printed element the model
fills in (rather than generates), no criterion can be omitted by accident. C-04 is prevented by
the exclusion list. C-05 is prevented by the gate check. C-09 and C-10 are prevented by
pre-printed sections. This is the maximum-coverage variation; composite score should be highest.

```
You are running /topic:new.

This skill produces exactly two written artifacts:
  1. An entry appended to simulations/TOPICS.md
  2. A strategy file at simulations/{topic}/strategy.md

Run the three phases below in order. Do not skip phases.

---

## PHASE 1 — SETUP

Collect:
  topic:       {slug, no spaces — e.g., frogs, atlas, vaultdoor}
  description: {one sentence: what feature is under investigation}
  target:      {what decision this investigation must inform — infer if not given, then confirm}

GATE: Confirm topic name and description with the user before writing anything.

---

## PHASE 2 — EXECUTE

### 2a — TOPICS.md

Read simulations/TOPICS.md. Create if absent with this header:

```markdown
# Topics Registry

| Topic | Description | Started | Status |
|-------|-------------|---------|--------|
```

Append one row and write:

| {topic} | {description} | {today's date} | active |

### 2b — Signal plan

Determine which signals this topic needs. For each signal, populate all five fields:

COLUMN DEFINITIONS (copy these headers verbatim into your table):

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|

- Namespace: exactly one of: scout | draft | review | flow | trace | prove | listen | program | topic
- Skill: the skill within that namespace (e.g., feasibility, users, state, synthesis, adoption)
- Item name: MUST follow the naming convention: {topic}-{slug}-{date}.md
  Example for topic "frogs": frogs-feasibility-2026-03-14.md
- Owner role: who is responsible for gathering this signal
  Examples: PM, developer, architect, designer, researcher, SRE, compliance
- Priority: EXACTLY one of these three words — no others are valid:
    essential       (required before design commit)
    recommended     (strengthens the case, not blocking)
    optional        (pursue only if time permits)
  INVALID substitutes: high / medium / low / required / critical / P1 / P2 / P3 / nice-to-have
  Using any invalid value makes the strategy unusable as a commit gate.

Coverage gate (check before proceeding to PHASE 3):
  [ ] At least one row marked essential — if zero, the strategy has no commit gate (invalid)
  [ ] At least 2 distinct namespaces in the Namespace column
  [ ] At least 2 distinct roles in the Owner role column
  [ ] Every cell in every row is filled

GATE: Do not proceed to PHASE 3 until all four coverage checks pass.

---

## PHASE 3 — WRITE AND CONFIRM

Write simulations/{topic}/strategy.md. Copy these section headers exactly:

```markdown
# Strategy: {topic}

*{description}*
*Target outcome: {target}*
*Date: {today}*

## Rationale

{2-4 sentences: why does this topic need investigation? What happens if the team
commits to a design without gathering these signals? What is the cost of skipping?}

## Signal Plan

| Namespace | Skill | Item name | Owner role | Priority |
|-----------|-------|-----------|------------|----------|
{rows from PHASE 2 — all five columns filled, priority = essential/recommended/optional only}

## Commit Gate

Design commit is permitted when: {explicit statement of minimum signal set}.
Example: "All essential signals gathered AND at least 2 recommended signals gathered."
Do not leave this section implicit. State the gate as a condition, not a hope.

## Naming Reference

All item names in this strategy follow the convention:
  {topic}-{slug}-{date}.md
Example: {topic}-feasibility-{today}.md
```

After writing, print to terminal:
  Topic registered: {topic}
  Strategy: simulations/{topic}/strategy.md
  TOPICS.md updated.
  Essential signals: {count}
  Recommended signals: {count}
  Optional signals: {count}
  Namespaces covered: {space-separated list}
  Commit gate: {one-line restatement}
```
