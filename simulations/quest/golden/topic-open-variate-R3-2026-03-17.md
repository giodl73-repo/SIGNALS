# topic-open — Round 3 Variations

**Skill**: Register a new topic, define its strategy, plan the signals needed for design commit.
**Rubric version**: v3 (C-01 through C-17, aspirational denominator = 9)
**Round context**: All R2 variations scored 88 (V-04, V-05) but failed C-01 — every variation dropped `{YYYY-MM-DD}` from the TOPICS.md row template when focusing on C-11–C-15. C-16 and C-17 are the two new aspirational criteria.

**R3 target**: Fix C-01 (via C-16: field-complete literal template) in all variations. Add C-17 (causal sequencing instruction) throughout. Build on R2's V-04/V-05 best patterns.

**Variation axes selected**:
- Template lock (C-16) — single axis
- Causal sequencing (C-17) — single axis
- Phrasing register (conversational) — single axis, rescuing R2 V-03's vivid consequence style
- C-16 + C-17 + full scaffolding — combination
- C-16 + C-17 + compact design — combination

---

## V-01 — Template Lock (C-16 focus)

**Axis**: The TOPICS.md row template is extracted into a named canonical block (`TOPICS.md ROW TEMPLATE`), physically separated from phase instructions, and explicitly referenced at write time with the instruction "copy it — do not reconstruct from memory."

**Hypothesis**: Isolating the row template as a named copy-paste block (rather than burying it inside phase instructions) prevents date regression because the model fills in placeholders rather than reconstructing the format. The template becomes a first-class artifact of the skill, not an inline detail.

---

## VOCABULARY LOCK

> Read this block before reading anything else in this skill.

Signal priority takes exactly three values:
- `essential`
- `recommended`
- `optional`

**Wrong vocabulary = silent breakage. This is the most common mistake.**

Tools downstream gate on exact string matches. Writing `high` instead of `essential` causes the commit gate to silently fail — no error, no warning, the gate simply never fires. The Design Lead never learns the topic is missing signals. Do not substitute `high`, `medium`, `low`, or any other term.

---

## TOPICS.md ROW TEMPLATE

The canonical row format for `simulations/TOPICS.md`:

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

Three required fields:
- **{topic-slug}** — lowercase-hyphenated identifier, unique within TOPICS.md
- **{one-line description}** — one sentence: what does this topic investigate, what decision does it inform?
- **{YYYY-MM-DD}** — ISO date the topic was opened (today's date)

This template is the source of truth. When you reach Phase 4 Write 1, return here and copy it. Do not reconstruct from memory.

---

## Skill Purpose

Register a new topic in the Signal system. Produce two outputs:
1. One row appended to `simulations/TOPICS.md` — using the ROW TEMPLATE above
2. Strategy file at `simulations/{topic}/strategy.md` — the editorial plan for this topic's investigation

---

## Field Schema

Every row in the signal table requires five fields:
- **F-01 Priority**: `essential` / `recommended` / `optional` — see VOCABULARY LOCK
- **F-02 Namespace**: scout / draft / review / flow / trace / prove / listen / program / topic
- **F-03 Skill**: specific skill within the namespace
- **F-04 Item Name**: `{topic}-{signal}-{date}.md`
- **F-05 Owner Role**: role responsible for this signal

Coverage minimums:
- COV-01: ≥ 1 row marked `essential`
- COV-02: ≥ 2 distinct namespaces
- COV-03: ≥ 2 distinct owner roles

---

## Phase 1 — Setup

Read `simulations/TOPICS.md`. Confirm this topic does not already exist. If it exists, stop — report the collision, do not create a duplicate entry.

---

## Phase 2 — Narrative Rationale + Signal Table

**Write NARRATIVE RATIONALE first. The signal table follows.**

The rationale surfaces the decision context. Owner roles in the table should emerge from the decisions described in the rationale. Writing the rationale first means roles derive from purpose; writing it after means roles are column-fillers.

Rationale format:
- ≥ 2 sentences
- State: (1) why this topic needs investigation, (2) what design decision the signals inform

Build the signal table after the rationale is written. Apply F-01 through F-05 to every row.

**Phase 2 Exit Gate** — check before advancing:
- [ ] Rationale is ≥ 2 sentences
- [ ] Every priority value matches VOCABULARY LOCK exactly
- [ ] COV-01: ≥ 1 `essential` row
- [ ] COV-02: ≥ 2 distinct namespaces
- [ ] COV-03: ≥ 2 distinct owner roles
- [ ] All item names follow `{topic}-{signal}-{date}.md`

---

## Phase 3 — Commit Gate

Structurally isolated from Phase 2. Write a `## COMMIT GATE` section in strategy.md listing all essential signals by exact item name:

```
## COMMIT GATE
Design commit requires all essential signals complete:
- {item-name-1}
- {item-name-2}
[list all essential signals]
```

---

## Phase 4 — Write Output

**Write 1 — TOPICS.md entry**

Return to the **TOPICS.md ROW TEMPLATE** at the top of this skill. Copy it. Fill in the three placeholders. Append to `simulations/TOPICS.md`.

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

The template is above — do not reconstruct it. Three fields: slug, description, date.

**Write 2 — Strategy file**

Write `simulations/{topic}/strategy.md` containing: narrative rationale, signal table, COMMIT GATE section.

---

## Phase 5 — Post-Generation Self-Check

Audit what you actually wrote. Read the output — not what you intended.

**C-01**: TOPICS.md row has slug + description + start date in YYYY-MM-DD format?
→ If date is missing: return to the TOPICS.md ROW TEMPLATE above. Use the three-field template. Replace the row before proceeding.

**C-02**: Strategy at `simulations/{topic}/strategy.md` — not a flat path?

**C-03**: Every signal row has all five fields (F-01 through F-05)?

**C-04**: Every priority value is exactly `essential`, `recommended`, or `optional`?
→ PRIORITY DRIFT AMEND: If any row has `high`, `medium`, `low`, or other: list each row, replace the invalid value, re-scan all priority cells before marking C-04 passing.

**C-05**: Signal table contains at least one `essential` row?

---

---

## V-02 — Causal Sequencing (C-17 focus)

**Axis**: Every ordering instruction in the skill is accompanied by a stated causal reason — not "do X before Y" but "do X before Y because Z." Applied consistently: vocabulary block first, rationale before table, self-check after writing, template referenced not reconstructed.

**Hypothesis**: Causal instructions resist erosion under generation pressure better than positional ones because the model can verify it is following the intent of the instruction, not just the surface order. V-05 from R2 showed a single causal phrase ("ensures owner roles emerge from decision context") strengthens C-15 adherence; this variation amplifies that pattern throughout.

---

## VOCABULARY LOCK

> This block is first in the skill — before schema, before phases, before everything — because priority vocabulary errors corrupt all downstream automation silently. Read it before you encounter any schema or instruction below.

Signal priority takes exactly three values:
- `essential`
- `recommended`
- `optional`

**Wrong vocabulary = silent breakage. This is the most common mistake.**

`high` does not match `essential` in string comparison. The commit gate silently fails — no error, just no gate. The Design Lead never detects missing signals. This is why the constraint is here, first, before you read the schema: once the vocabulary is locked in, every row you write is already constrained.

---

## Skill Purpose

Register a new topic in the Signal system:
- One row appended to `simulations/TOPICS.md`
- Strategy file at `simulations/{topic}/strategy.md`

The strategy is the editorial plan: which signals to gather, who owns them, which ones gate design commit.

---

## Field Schema

Five fields per signal row — because every downstream tool (topic-status, topic-scanner) parses all five:
- **Priority**: `essential` / `recommended` / `optional` (VOCABULARY LOCK applies — see above)
- **Namespace**: scout / draft / review / flow / trace / prove / listen / program / topic
- **Skill**: specific skill within the namespace
- **Item Name**: `{topic}-{signal}-{date}.md`
- **Owner Role**: role responsible for this signal

---

## Phase 1 — Setup

Read `simulations/TOPICS.md` to confirm the topic is not already registered — because registering a duplicate silently creates two competing strategy files with no merge path. Stop on collision.

---

## Phase 2 — Execute

### Step A: Write Narrative Rationale First

Write the narrative rationale **before** building the signal table — because owner roles in the table should emerge from the decisions described in the rationale, not from retrospective column-filling. If the table comes first, roles become decorative labels assigned to fill a column. If the rationale comes first, roles surface as the stakeholders who own the decisions being described.

Rationale:
- ≥ 2 sentences
- State: (1) why this topic needs investigation, (2) what design decisions the signals inform

### Step B: Then Build the Signal Table

Build the table after the rationale — because the rationale answers "who should care about this signal?", which determines the owner role column. The table is a formalization of what the rationale already implies.

Coverage minimums (declared here, during construction, so violations are caught before writing rather than after):
- ≥ 1 row marked `essential` — without this there is no commit gate; the topic has no defined finish line
- ≥ 2 distinct namespaces — prevents monoculture investigations
- ≥ 2 distinct owner roles — ensures accountability is distributed

---

## Phase 3 — Commit Gate

Write this section after the signal table — because the commit gate is defined by which signals are marked `essential`, and those signals must exist before the gate can be enumerated.

Structurally isolated. Not a subsection of Phase 2.

```
## COMMIT GATE
Design commit requires all essential signals complete:
- {item-name-1} [list all essential signals by exact item name]
```

---

## Phase 4 — Write Output

**TOPICS.md row** — use this exact template, because a reconstructed template drifts from the canonical three-field format:

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

Fill in: lowercase-hyphenated slug, one-sentence description, today's date in YYYY-MM-DD. All three fields are required. The date marks when the topic was opened.

**Strategy file** — write to `simulations/{topic}/strategy.md` (not a flat path, not inline in TOPICS.md) — because topic-status and topic-scanner glob for this specific path; a flat path silently breaks coverage computation.

---

## Phase 5 — Post-Generation Self-Check

Run this check after both files are written — because this check tests what you produced, not what you planned to produce. Running it before writing would verify intentions; running it after verifies output.

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date?
**C-02**: Strategy at `simulations/{topic}/strategy.md`?
**C-03**: Every signal row has all 5 fields?
**C-04**: Every priority exactly `essential` / `recommended` / `optional`?
**C-05**: At least one `essential` signal?

**AMEND — PRIORITY DRIFT**: Triggered by any C-04 failure. List each failing row. Replace invalid priority values. Re-scan all cells before marking C-04 passing.

**AMEND — DATE FIELD**: Triggered by C-01 date failure. Return to Phase 4 TOPICS.md template. Use the three-field template. Replace the row. Verify three fields present.

---

---

## V-03 — Conversational Register + Full Coverage

**Axis**: Conversational imperative phrasing (built on R2 V-03's vivid consequence framing) with all R2 V-03 gaps repaired: explicit `{YYYY-MM-DD}` in the row template (C-01 fix / C-16), explicit ≥ 2 namespace minimum (C-06 fix), and causal explanation for sequencing (C-17).

**Hypothesis**: R2 V-03 had the strongest C-14 evidence — its consequence framing was notably more vivid than any other variation. The C-01 and C-06 failures were mechanical gaps, not register failures. A fully-correct conversational variation matches V-04/V-05 on aspirational and outperforms them on C-14 vividness.

---

## BEFORE YOU START: VOCABULARY

You are about to plan a topic's investigation. Before you do anything else, read this.

Signal priority has exactly three valid values:

- `essential`
- `recommended`
- `optional`

**Do not use `high`, `medium`, or `low`. Not even once.**

Here is why this matters more than it seems: every tool downstream from this strategy file looks for these exact strings. If you write `high` instead of `essential`, the tool does not error — it silently ignores that signal. The commit gate never fires. The Design Lead never knows the topic is missing key evidence. The file looks perfectly valid. The investigation silently stalls. That is the scenario you are preventing by reading this before touching any schema below.

**This is the most common mistake in this skill.**

---

## What You're Making

Two outputs:
1. A row in `simulations/TOPICS.md` — so the topic exists in the registry
2. A strategy file at `simulations/{topic}/strategy.md` — your plan for how to investigate this topic

---

## The TOPICS.md Row

The row has exactly three fields. Copy this template and fill in the placeholders:

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

- **{topic-slug}**: lowercase-hyphenated identifier (e.g., `signal-latency`)
- **{one-line description}**: one sentence — what does this topic investigate and what decision does it inform?
- **{YYYY-MM-DD}**: today's date in ISO format — this is when you opened the topic

All three fields are required. The date is not optional.

---

## Step 1: Check for Collisions

Read `simulations/TOPICS.md`. Make sure the topic you're registering does not already exist. If it does, stop — report the collision and ask for clarification.

---

## Step 2: Write Your Rationale First

Before you build the signal table, write 2 or more sentences explaining:
- Why does this topic need investigation?
- What design decision will these signals inform?

Write this **before** the table — not after. Here's why: the decisions you describe in the rationale determine which roles are responsible for which signals. If you write the table first and add rationale afterward, the owner roles become post-hoc labels you assign to fill a column. If you write the rationale first, the roles emerge from the question you're trying to answer — they have a reason to exist.

---

## Step 3: Build the Signal Table

Now build the table. Five columns:

| Priority | Namespace | Skill | Item Name | Owner Role |
|----------|-----------|-------|-----------|------------|

Rules:
- **Priority**: `essential`, `recommended`, or `optional` — exactly those words. See the vocabulary block above.
- **Namespace**: pick from scout / draft / review / flow / trace / prove / listen / program / topic. Use **at least 2 distinct namespaces** across your rows.
- **Skill**: the specific skill within the namespace
- **Item Name**: `{topic}-{signal}-{date}.md`
- **Owner Role**: pull these from the decisions you described in Step 2

Minimums:
- At least 1 row marked `essential` — without this, you have no commit gate and no defined finish line
- At least 2 distinct namespaces
- At least 2 distinct owner roles

---

## Step 4: Name Your Commit Gate

Write a `## COMMIT GATE` section in strategy.md. List every `essential` signal by its exact item name. This gate must be met before design commit.

---

## Step 5: Write the Files

**File 1 — TOPICS.md row**: Copy the template from above and fill in the three fields. Do not reconstruct it — copy it.

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**File 2 — strategy.md**: Write to `simulations/{topic}/strategy.md`. Include the rationale, signal table, and COMMIT GATE section.

---

## Step 6: Check Your Work

Read what you actually wrote. Not what you intended to write — what you wrote.

**Q1**: Does the TOPICS.md row have three fields: slug, description, and a date in YYYY-MM-DD format?
→ If the date is missing: go back to the template in Step 5 and use all three fields.

**Q2**: Is the strategy file at `simulations/{topic}/strategy.md` — not a flat path, not inside TOPICS.md itself?

**Q3**: Does every signal row have all five fields: Priority, Namespace, Skill, Item Name, Owner Role?

**Q4**: Did any priority drift to `high`, `medium`, `low`, or anything else?
→ If yes — stop. List every row where it happened. Replace each invalid value. Re-read the vocabulary block if you need a reminder. Do not mark this step as done until every priority cell reads exactly `essential`, `recommended`, or `optional`.

**Q5**: Does the table have at least one row marked `essential`?

---

---

## V-04 — Combination: C-16 + C-17 + Full Scaffolding

**Axis**: Combines the field-complete canonical template (C-16) with causal sequencing throughout (C-17), using R2 V-04's full phase structure as the base. Every phase transition has a stated reason; the TOPICS.md template is a named first-class block.

**Hypothesis**: R2 V-04 achieved 88 (7/7 aspirational) blocked only by C-01. Adding C-16 (named canonical template) and C-17 (causal sequencing at three points: vocabulary placement, rationale sequencing, post-gen check timing) closes the remaining gap without adding structural overhead. The full scaffolding absorbs both new criteria naturally.

---

## VOCABULARY LOCK

> This block precedes all schema, register, and phase directives — because priority vocabulary errors corrupt downstream gating silently, and the lock must be set before any instruction can override it. Read before anything else.

Signal priority uses exactly three values:
- `essential`
- `recommended`
- `optional`

**Wrong vocabulary = silent breakage. This is the most common mistake in this skill.**

Tools that gate on priority look for exact string matches. `high` does not match `essential`. The gate silently fails — it does not error, it simply never trips. The Design Lead never detects the gap. Do not use `high`, `medium`, `low`, or any other substitution.

---

## TOPICS.md ROW TEMPLATE

The canonical row format for `simulations/TOPICS.md`:

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

Three required fields:
- **{topic-slug}**: lowercase-hyphenated identifier
- **{one-line description}**: one sentence describing what this topic investigates and what decision it informs
- **{YYYY-MM-DD}**: ISO date the topic was opened (today's date)

Reference this template at write time. Do not reconstruct it from memory — reconstructed templates drop fields.

---

## FIELD SCHEMA

Every signal row requires five fields (because topic-status parses all five for coverage computation):
- **F-01 Priority**: `essential` / `recommended` / `optional` — VOCABULARY LOCK applies
- **F-02 Namespace**: scout / draft / review / flow / trace / prove / listen / program / topic
- **F-03 Skill**: specific skill within the namespace
- **F-04 Item Name**: `{topic}-{signal}-{date}.md`
- **F-05 Owner Role**: role responsible for this signal

---

## COVERAGE SCHEMA

- COV-01: ≥ 1 signal marked `essential` (no essential = no commit gate = no defined finish line)
- COV-02: ≥ 2 distinct namespaces
- COV-03: ≥ 2 distinct owner roles (roles should derive from Phase 2 rationale)

---

## Phase 1 — Setup

Read `simulations/TOPICS.md`. Verify the topic does not already exist. Stop on collision.

---

## Phase 2 — Content Generation

### Write NARRATIVE RATIONALE First

Write the narrative rationale before constructing the signal table — so owner roles emerge from the decision context rather than from post-hoc column-filling. The rationale surfaces the question: who needs to answer this, and what decision depends on knowing? Writing it first means the owner roles in the table have a derivable reason to exist. Writing it after means they are assigned to fill a schema requirement.

Requirements:
- ≥ 2 sentences
- State: (1) why this topic requires investigation, (2) what design decisions these signals inform

### Then Build the Signal Table

Construct the signal table after the rationale exists — because the rationale determines owner roles, and the signal table formalizes them. Columns: Priority | Namespace | Skill | Item Name | Owner Role. Apply F-01 through F-05 to every row.

**Phase 2 Exit Gate**:
- [ ] Rationale is written and ≥ 2 sentences
- [ ] Every priority value matches VOCABULARY LOCK exactly
- [ ] COV-01: ≥ 1 `essential` row
- [ ] COV-02: ≥ 2 distinct namespaces
- [ ] COV-03: ≥ 2 distinct owner roles
- [ ] All item names match `{topic}-{signal}-{date}.md`

---

## Phase 3 — Commit Gate

This section is structurally isolated. Not a subsection of Phase 2. Written after the signal table because the commit gate is enumerated from essential signals — the table must exist before the gate can be named.

```
## COMMIT GATE
Design commit requires all essential signals complete:
- {item-name-1}
- {item-name-2}
[all essential signals by exact item name]
```

---

## Phase 4 — Write Output

**Write 1 — TOPICS.md entry**

Return to the **TOPICS.md ROW TEMPLATE** at the top of this skill. Copy it. Fill in the three placeholders. Append to `simulations/TOPICS.md`.

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

The template is the source of truth — do not reconstruct it. Three fields: slug, description, date.

**Write 2 — Strategy file**

Write `simulations/{topic}/strategy.md` containing: narrative rationale, signal table, COMMIT GATE section.

---

## Phase 5 — Post-Generation Self-Check

Audit what you actually produced — this phase runs after writing because it checks output, not intent. Running it before writing would verify what you planned to produce, not what you produced.

**C-01**: TOPICS.md row contains slug + description + start date in YYYY-MM-DD format?
**C-02**: Strategy at `simulations/{topic}/strategy.md` (not flat path)?
**C-03**: Every signal row has all five fields (F-01 through F-05)?
**C-04**: Every priority value is exactly `essential`, `recommended`, or `optional`?
**C-05**: Signal table contains at least one `essential` row?

---

## Phase 5 — AMEND

**PRIORITY DRIFT — AMEND TRIGGER**: Did any row use `high`, `medium`, `low`, or any other value?

Do not mark C-04 as passing. Execute:
1. List every row where drift occurred
2. Replace each invalid value with the correct vocabulary term
3. Re-scan all priority cells
4. Re-run C-04 check before marking passing

**TOPICS.md DATE — AMEND TRIGGER**: Did C-01 fail on the date field?

Return to the TOPICS.md ROW TEMPLATE at the top of this skill. The template has three fields: slug, description, and `{YYYY-MM-DD}`. Replace the row using the canonical template. Fill in today's date. Verify three fields are present.

---

---

## V-05 — Combination Compact: All Criteria, Minimal Scaffolding

**Axis**: Compact design carrying all 9 aspirational criteria — including C-16 (canonical row template as a named block) and C-17 (causal sequencing explanation inline) — building directly on R2 V-05's proven minimal structure. The DEFAULTS TABLE absorbs inertia, coverage, and sequencing rationale in a single block.

**Hypothesis**: R2 V-05 achieved 7/7 aspirational at lower cognitive load than V-04 using a DEFAULTS TABLE. Adding C-16 and C-17 to the compact structure requires one additional named block (TOPICS.md template) and one additional "because" clause (in the sequencing instruction) — no new sections, no new phases. The result achieves 9/9 aspirational while staying compact.

---

## VOCABULARY CONSTRAINT

Standalone block. Read before any instruction.

Signal priority: exactly `essential` / `recommended` / `optional`. Wrong vocabulary = silent downstream breakage. This is the most common mistake. Tools gate on exact string matches — writing `high` instead of `essential` causes the commit gate to silently fail. It does not error. It stops working. The Design Lead sees a passing strategy file that is actually broken.

---

## TOPICS.md ROW TEMPLATE

Copy this template when writing the TOPICS.md entry. Do not reconstruct from memory — reconstructed templates drop fields:

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

Three fields required: slug (lowercase-hyphenated), description (one sentence), date (YYYY-MM-DD, today).

---

## DEFAULTS THIS SKILL OVERRIDES

| Default | This Skill's Rule | Why |
|---------|-------------------|-----|
| Any priority vocabulary | `essential` / `recommended` / `optional` only | Downstream tools gate on exact string matches |
| Free-form TOPICS.md row | Use the ROW TEMPLATE above (3 fields: slug, description, YYYY-MM-DD) | Date field required; reconstructed templates regress |
| Table before context | Rationale first, then signal table | Owner roles emerge from decision context, not post-hoc column-filling |
| Inline commit gate | Structurally isolated `## COMMIT GATE` section | Parseable by topic-status; not a subsection of the signal table |

---

## Phase 1 — Setup

Read `simulations/TOPICS.md`. Confirm topic not already registered. Stop on collision.

---

## Phase 2 — Generate

**Rationale first. Signal table second.**

Write the narrative rationale before building the signal table — so owner roles emerge from decision context rather than post-hoc count enforcement. If the table comes first, owner roles become column-fillers; if the rationale comes first, they become meaningful stakeholders whose accountability derives from the decisions being described.

Rationale: ≥ 2 sentences. State why the topic requires investigation and what decisions the signals inform.

Signal table (after rationale is written):

| Priority | Namespace | Skill | Item Name | Owner Role |
|----------|-----------|-------|-----------|------------|

Requirements:
- Priority: `essential` / `recommended` / `optional` — see VOCABULARY CONSTRAINT
- Item Name: `{topic}-{signal}-{date}.md`
- ≥ 1 row `essential`; ≥ 2 distinct namespaces (scout/draft/review/flow/trace/prove/listen/program/topic); ≥ 2 distinct owner roles

---

## Phase 3 — Commit Gate

Structurally isolated. Not a section of Phase 2.

Write `## COMMIT GATE` in strategy.md listing all `essential` signals by exact item name:

```
## COMMIT GATE
Design commit requires all essential signals complete:
- {item-name-1} [all essential signals]
```

---

## Phase 4 — Write

**TOPICS.md entry**: Return to the ROW TEMPLATE above. Copy it. Fill in slug, description, and today's date. Three fields — do not omit the date.

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**Strategy file**: Write to `simulations/{topic}/strategy.md` — not flat path.

---

## Phase 5 — Self-Check and Amend

After both files written — because this checks actual output, not intentions. Running before writing would test what you planned to write; running after tests what you wrote.

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date?
**C-02**: Strategy at `simulations/{topic}/strategy.md`?
**C-03**: Every signal row has all five fields: priority, namespace, skill, item name, owner role?
**C-04**: Every priority exactly `essential` / `recommended` / `optional`?
**C-05**: At least one `essential` row?

**AMEND — Priority Drift**: If C-04 fails: identify each row with drift. Replace invalid values. Re-scan before marking C-04 passing.

**AMEND — Date Field**: If C-01 fails on date: return to the ROW TEMPLATE in Phase 4. Use the three-field canonical template. Fill in today's date. Verify three fields present before proceeding.
