Now I have the full picture. The current golden (R20 QU5) scores well on C-01 through C-10 and C-15, but has gaps on C-11 (standalone vocab block before instructions), C-12 (post-generation self-check), C-13 (AMEND step naming priority drift), and partially C-14 (consequence framing). The 5 variations below target these gaps along distinct axes.

---

# topic-open — Quest Variate Round 2 (V-01 through V-05)

---

## V-01 — Axis: Vocabulary constraint placement
**Hypothesis**: A standalone VOCABULARY LOCK block placed as the very first content — before any schema, register, or phase instruction — reduces C-04 priority drift more than burying F-01 inside a mid-document schema table. Leading with the vocabulary rule plus "most common mistake" consequence framing (C-14) gives the model a reason to care before it touches any instructions.

---

```
# topic-open — Register Topic and Plan Signals

You are executing the `topic-open` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## VOCABULARY LOCK

> Read this block before reading anything else in this skill.
> This is not a schema definition — it is a constraint you apply to every row you write.

**Priority field vocabulary (applies to every signal row you produce):**

| Allowed | Meaning |
|---------|---------|
| `essential` | Consumer cannot commit to design without this signal |
| `recommended` | Consumer commits with increased risk exposure without this signal |
| `optional` | Consumer commits unaffected; nice to have |

**Forbidden values**: `high`, `medium`, `low`, `critical`, `nice-to-have`, or any other vocabulary.

> **Wrong vocabulary = silent breakage. This is the most common mistake in this skill.**
> A strategy file with `high / medium / low` passes visual inspection but is unparseable
> by any downstream tool that gates on priority. The Design Lead cannot determine
> readiness. The commit gate silently stops working.
>
> If you find yourself writing `high`, `medium`, or `low` in the priority column —
> stop, delete it, and replace it with one of the three allowed values above.

---

## INERTIA REGISTER

> Stable IR-NN IDs. Phase directives cite these by ID.

| ID    | Default Behavior                                                           | Override Active In | Stakeholder Most Harmed |
|-------|----------------------------------------------------------------------------|--------------------|--------------------------|
| IR-01 | Skip stakeholder mapping; author signals from feature intuition            | Phase 1            | Product Manager — loses commit-scope ground truth |
| IR-02 | Use "high/medium/low" priority vocabulary from project-management context  | Phase 2            | Design Lead — cannot gate design commit on unparseable priority |
| IR-03 | Collapse commit gate into signal plan section with no structural isolation | Phase 3            | Engineering Lead — no enforced readiness condition at commit time |
| IR-04 | Omit artifact naming convention; use freeform item names                   | Phase 4            | All consumers — strategy unreachable by path-based tools |
| IR-05 | Assign all signals to a single generic owner role                          | Phase 2            | Cross-functional team — coverage gaps invisible when ownership collapses |

---

## FIELD SCHEMA

> F-NN row order = column order in signal table. Fill left to right.

| ID   | Field             | Constraint                                              | Downstream Effect If Violated                                        |
|------|-------------------|---------------------------------------------------------|----------------------------------------------------------------------|
| F-01 | Priority          | Exactly: `essential` / `recommended` / `optional`       | Strategy unusable as commit gate — see VOCABULARY LOCK above         |
| F-02 | Namespace         | One of: scout draft review flow trace prove listen program topic | Invalid routing at runtime                               |
| F-03 | Skill             | Named skill under stated namespace                      | Signal uncollectable; evidence gap invisible                         |
| F-04 | Item Name         | `{topic}-{signal}-{date}.md`                            | Strategy unreachable by path-based tools                             |
| F-05 | Owner Role        | Named role; ≥ 2 distinct roles across all rows (IR-05 override) | Cross-functional gaps invisible                          |

---

## COVERAGE SCHEMA

| ID     | Constraint                  | Minimum | Downstream Effect If Violated |
|--------|-----------------------------|---------|-------------------------------|
| COV-01 | Signals marked `essential`  | ≥ 1     | No commit gate definable; feature ships without evidence gate |
| COV-02 | Distinct namespaces         | ≥ 2     | Single-namespace plan; structural blind spot |
| COV-03 | Distinct owner roles (F-05) | ≥ 2     | Cross-functional gaps invisible |
| COV-04 | Narrative rationale         | ≥ 2 sentences | Decision context absent; signal relevance unverifiable |

---

## PIPELINE OVERVIEW

| Phase | Purpose          | Handoff Artifact       | Exit Gate Summary                           |
|-------|------------------|------------------------|---------------------------------------------|
| 1     | Stakeholder Map  | S-table (≥ 3 rows)     | ≥ 3 rows; all columns populated             |
| 2     | Signal Plan      | Rationale + signal table | F-01–F-05 + COV-01–COV-04; rationale written FIRST |
| 3     | Commit Gate      | Gate block             | ≥ 1 essential named; structurally isolated  |
| 4     | Artifact Write   | TOPICS.md + strategy.md | Both files at correct paths                |

**Read this entire table before executing Phase 1.**

---

## PHASE 1 — STAKEHOLDER MAP

> Overriding IR-01 (skip stakeholder mapping) and IR-05 (single generic owner).

Fill the table. Each row: one decision-maker role, what breaks for them if topic is skipped, what decision this evidence informs.

| Row ID | Decision-Maker Role | Risk Exposure (what breaks for them) | Decision Informed |
|--------|---------------------|--------------------------------------|-------------------|
| S-01   |                     |                                      |                   |
| S-02   |                     |                                      |                   |
| S-03   |                     |                                      |                   |
| S-NN   | (add as needed)     |                                      |                   |

**Exit gate**: ≥ 3 rows. All four columns populated in every row. Do not advance until both checks pass independently.

---

## PHASE 2 — SIGNAL PLAN

> Overriding IR-02 (high/medium/low vocabulary) and IR-05 (single owner).
> **Write NARRATIVE RATIONALE first. The signal table comes after.**

**Entry gate**: Phase 1 exit gate cleared. [ ]

### NARRATIVE RATIONALE

> Write ≥ 2 sentences here before building the signal table.
> Explain: (1) why this topic needs investigation, and (2) what design decision it will inform.
> The roles and contexts you describe here become the owner roles in your signal table.

[Write rationale here — minimum 2 sentences, written before the signal table]

### SIGNAL TABLE

> Column order matches F-01 through F-05. Priority (F-01) is leftmost.
> Re-read VOCABULARY LOCK before filling the Priority column.

| Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04) | Owner Role (F-05) |
|-----------------|------------------|--------------|------------------|-------------------|
|                 |                  |              |                  |                   |

**Exit gate**:
- [ ] Every priority value is one of: `essential` / `recommended` / `optional` (see VOCABULARY LOCK)
- [ ] ≥ 1 row marked `essential` (COV-01)
- [ ] ≥ 2 distinct namespaces (COV-02)
- [ ] ≥ 2 distinct owner roles (COV-03)
- [ ] All item names follow `{topic}-{signal}-{date}.md` (F-04)

---

## PHASE 3 — COMMIT GATE

> Overriding IR-03 (collapse commit gate into signal plan).
> The commit gate is a structurally isolated block — not a section of Phase 2.

**Entry gate**: Phase 2 exit gate cleared. [ ]

```
COMMIT GATE for {TOPIC}
========================
Design commit is authorized when ALL of the following signals are present
in simulations/{TOPIC}/:

REQUIRED (essential — COV-01):
  1. [item name from essential row]
  2. [additional essential rows if any]

PERMITTED AFTER COMMIT (recommended / optional):
  - [list remaining signals]

Enforcement: no design commit proceeds until the REQUIRED signals above
exist as files at their declared paths.
```

**Exit gate**: Gate block written. ≥ 1 essential signal named. Gate is a condition, not a wish list.

---

## PHASE 4 — ARTIFACT WRITE

> Overriding IR-04 (freeform item names).

**Entry gate**: Phase 3 exit gate cleared. [ ]

### Write 1: simulations/TOPICS.md

Append a row:

```
| {TOPIC} | active | simulations/{TOPIC}/strategy.md | [one-line description] |
```

### Write 2: simulations/{TOPIC}/strategy.md

```markdown
# {TOPIC} — Signal Strategy

## Rationale
[paste Phase 2 narrative rationale]

## Stakeholder Map
[paste Phase 1 fill-in table]

## Signal Plan
[paste Phase 2 signal table]

## Commit Gate
[paste Phase 3 commit gate block]
```

**Exit gate**: Both files written at correct paths. All item names follow `{topic}-{signal}-{date}.md`.
```

---

## V-02 — Axis: Post-generation self-check phase
**Hypothesis**: Adding an explicit Phase 5 SELF-CHECK with per-essential-criterion checkboxes after artifact generation — plus a named AMEND step asking specifically "Did any priority row drift to high/medium/low?" — catches errors that inline pre-write gates miss. Pre-write gates are aspirational (you haven't written yet); post-write gates are auditing (you check what you actually produced).

---

```
# topic-open — Register Topic and Plan Signals

You are executing the `topic-open` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## INERTIA REGISTER

| ID    | Default Behavior                                                           | Override Active In | Stakeholder Most Harmed |
|-------|----------------------------------------------------------------------------|--------------------|--------------------------|
| IR-01 | Skip stakeholder mapping; author signals from feature intuition            | Phase 1            | Product Manager — loses commit-scope ground truth |
| IR-02 | Use "high/medium/low" priority vocabulary from project-management context  | Phase 2            | Design Lead — cannot gate design commit on unparseable priority |
| IR-03 | Collapse commit gate into signal plan section with no structural isolation | Phase 3            | Engineering Lead — no enforced readiness condition at commit time |
| IR-04 | Omit artifact naming convention; use freeform item names                   | Phase 4            | All consumers — strategy unreachable by path-based tools |
| IR-05 | Assign all signals to a single generic owner role                          | Phase 2            | Cross-functional team — coverage gaps invisible when ownership collapses |

---

## FIELD SCHEMA

| ID   | Field             | Constraint                                              |
|------|-------------------|---------------------------------------------------------|
| F-01 | Priority          | Exactly: `essential` / `recommended` / `optional` — **not** high/medium/low. Wrong vocabulary = strategy malformed; Design Lead cannot parse readiness. This is the most common mistake. |
| F-02 | Namespace         | One of: scout draft review flow trace prove listen program topic |
| F-03 | Skill             | Named skill under stated namespace |
| F-04 | Item Name         | `{topic}-{signal}-{date}.md` |
| F-05 | Owner Role        | Named role; ≥ 2 distinct roles across all rows |

---

## COVERAGE SCHEMA

| ID     | Constraint                  | Minimum |
|--------|-----------------------------|---------|
| COV-01 | Signals marked `essential`  | ≥ 1     |
| COV-02 | Distinct namespaces         | ≥ 2     |
| COV-03 | Distinct owner roles        | ≥ 2     |
| COV-04 | Narrative rationale         | ≥ 2 sentences |

---

## PHASE 1 — STAKEHOLDER MAP

> Overriding IR-01 and IR-05.

Fill the table. Each row: one decision-maker role, specific harm if topic skipped, concrete decision this evidence informs.

| Row ID | Decision-Maker Role | Risk Exposure | Decision Informed |
|--------|---------------------|---------------|-------------------|
| S-01   |                     |               |                   |
| S-02   |                     |               |                   |
| S-03   |                     |               |                   |

**Exit gate**: ≥ 3 rows; all four columns populated.

---

## PHASE 2 — SIGNAL PLAN

> Overriding IR-02 and IR-05.

**Entry gate**: Phase 1 cleared. [ ]

### Narrative Rationale

Write ≥ 2 sentences here before building the signal table. Explain why this topic needs investigation and what design decision it will inform. The roles you name here become owner roles in your signal table.

[Write rationale here first]

### Signal Table

> Priority (F-01) is leftmost. Allowed values: `essential` / `recommended` / `optional` only.

| Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04) | Owner Role (F-05) |
|-----------------|------------------|--------------|------------------|-------------------|
|                 |                  |              |                  |                   |

---

## PHASE 3 — COMMIT GATE

> Overriding IR-03.

**Entry gate**: Phase 2 cleared. [ ]

```
COMMIT GATE for {TOPIC}
========================
Design commit authorized when ALL of the following are present in simulations/{TOPIC}/:

REQUIRED (essential):
  1. [item name]

PERMITTED AFTER COMMIT:
  - [recommended / optional signals]
```

---

## PHASE 4 — ARTIFACT WRITE

**Entry gate**: Phase 3 cleared. [ ]

**Write 1**: Append to `simulations/TOPICS.md`:

```
| {TOPIC} | active | simulations/{TOPIC}/strategy.md | [description] |
```

**Write 2**: Write `simulations/{TOPIC}/strategy.md`:

```markdown
# {TOPIC} — Signal Strategy

## Rationale
[Phase 2 rationale]

## Stakeholder Map
[Phase 1 table]

## Signal Plan
[Phase 2 signal table]

## Commit Gate
[Phase 3 gate block]
```

---

## PHASE 5 — SELF-CHECK

> **Run this phase after both files are written. Do not skip.**
> Check your actual output, not your intentions.

### Essential Criteria Audit

- [ ] **C-01**: Does `simulations/TOPICS.md` contain a row for this topic with slug, description, and date?
- [ ] **C-02**: Is the strategy file at `simulations/{topic}/strategy.md` — not at a flat path?
- [ ] **C-03**: Does every signal row contain all five fields: namespace, skill, item name, owner role, priority?
- [ ] **C-04**: Does every priority value in the strategy file read exactly `essential`, `recommended`, or `optional`?
  - **PRIORITY DRIFT CHECK**: Scan every priority cell now. Did any row use `high`, `medium`, `low`, or any other value? If yes: AMEND before proceeding.
- [ ] **C-05**: Does the signal table contain at least one row marked `essential`?

### AMEND Step

If C-04 failed the priority drift check:
1. Identify every row where priority is not `essential` / `recommended` / `optional`
2. Replace each incorrect value with the correct vocabulary
3. Re-check: are all priority cells now exactly one of the three allowed values?
4. If the commit gate references item names from corrected rows, verify names still match

If all five checks pass: output is complete.
```

---

## V-03 — Axis: Phrasing register (conversational imperative)
**Hypothesis**: A directive, conversational register ("Don't write X — here is exactly what breaks") produces better compliance than a formal schema-table reference style. The model treats imperative directives differently from table constraints. A conversational voice that explains consequences in plain language reduces C-04 drift without requiring elaborate pre-pipeline machinery.

---

```
# topic-open — Register Topic and Plan Signals

You are running `topic-open`. You will produce two outputs:
- An entry in `simulations/TOPICS.md`
- A strategy file at `simulations/{TOPIC}/strategy.md`

---

## BEFORE YOU START: VOCABULARY

**Do not use `high`, `medium`, or `low` for signal priority. Ever.**

Use exactly these three words and no others:

- `essential` — the team cannot commit to design without this signal
- `recommended` — the team commits with higher risk without this signal
- `optional` — the team commits unaffected; nice to have

Why does this matter? Because every tool downstream that reads your strategy file will
look for exactly these strings to determine whether the topic is ready to commit.
If you write `high` instead of `essential`, the gate silently fails — it does not
error, it just never trips. The Design Lead never knows the topic is missing signals.
**This is the most common mistake in this skill.** Write the vocabulary here before you
begin: `essential`, `recommended`, `optional`. If you find yourself writing anything
else in the priority column, stop and fix it.

---

## BEFORE YOU START: THE THREE DEFAULTS TO OVERRIDE

When registering a topic, you will feel the pull to:

1. Skip stakeholder mapping and just list signals — **don't**. Without mapping who
   needs what decision, you cannot tell if your signal plan has coverage gaps.
2. Use project-management priority vocabulary (high/medium/low) — **don't**. See above.
3. Write a vague "commit when ready" statement instead of a named commit gate — **don't**.
   The Engineering Lead needs to know exactly which files to look for.

The phases below override each of these pulls in sequence.

---

## STEP 1 — MAP YOUR STAKEHOLDERS

Who needs decisions from this topic? For each person, answer: what breaks for them
if the topic is skipped, and what concrete decision does this topic inform?

Fill in at least three rows:

| # | Role | What breaks if topic is skipped | Decision this topic informs |
|---|------|---------------------------------|-----------------------------|
| S-01 | | | |
| S-02 | | | |
| S-03 | | | |

Do not advance until every row has all four cells filled. An empty "what breaks" cell
means you are registering a stakeholder you do not actually understand — stop and think.

---

## STEP 2 — WRITE YOUR RATIONALE (BEFORE THE SIGNAL TABLE)

Before you build any signal table, write 2+ sentences explaining:
- Why does this topic need investigation?
- What design decision will the investigation inform?

Write it here:

[Rationale — write this before the signal table below]

The roles you describe in your rationale are the owner roles in your signal table.
If your rationale does not mention at least two distinct roles, revise it before
building the table — do not just add roles to the table post-hoc.

---

## STEP 3 — PLAN YOUR SIGNALS

Build the signal table. Rules:

- Priority column: use only `essential` / `recommended` / `optional` (see top of skill)
- Namespace: one of scout, draft, review, flow, trace, prove, listen, program, topic
- Item name: `{topic}-{signal}-{date}.md` — no exceptions
- Owner role: a named role; at least 2 distinct roles across all rows
- Include at least 1 signal marked `essential` — without it, you have no commit gate

| Priority | Namespace | Skill | Item Name | Owner Role |
|----------|-----------|-------|-----------|------------|
| | | | | |

---

## STEP 4 — NAME YOUR COMMIT GATE

Write a named commit gate. This is not a summary of Step 3 — it is a conditional:
"design commit proceeds when these specific files exist."

```
COMMIT GATE for {TOPIC}
========================
Design commit authorized when all REQUIRED signals exist at their declared paths:

REQUIRED:
  1. [item name from an essential row]

PERMITTED AFTER COMMIT:
  - [remaining signals]
```

---

## STEP 5 — WRITE THE FILES

**File 1** — Append to `simulations/TOPICS.md`:
```
| {TOPIC} | active | simulations/{TOPIC}/strategy.md | [one-line description] |
```

**File 2** — Write `simulations/{TOPIC}/strategy.md`:
```markdown
# {TOPIC} — Signal Strategy

## Rationale
[your Step 2 rationale]

## Stakeholder Map
[your Step 1 table]

## Signal Plan
[your Step 3 signal table]

## Commit Gate
[your Step 4 gate block]
```

---

## STEP 6 — CHECK YOUR WORK

Read what you actually wrote, not what you intended to write. Answer each question:

1. Is there a row in `TOPICS.md` for this topic? (yes / no)
2. Is the strategy file at `simulations/{topic}/strategy.md`? (yes / no)
3. Does every signal row have all five columns filled? (yes / no)
4. **Does every priority cell read exactly `essential`, `recommended`, or `optional`?**
   Scan each priority cell now. Did any drift to `high`, `medium`, `low`, or anything else?
   (yes = all correct / no = STOP AND FIX BEFORE CONTINUING)
5. Is at least one signal marked `essential`? (yes / no)

If any answer is "no": fix it now, then re-check that item.
If all answers are "yes": done.
```

---

## V-04 — Combination: Vocabulary-first + Post-generation self-check
**Hypothesis**: The vocabulary lock at the top of the skill (from V-01) prevents C-04 drift during generation. The post-generation self-check with named AMEND step (from V-02) catches any drift that the vocabulary lock failed to prevent. Together they form a two-layer defense: prevention + detection. Neither alone is sufficient because the model can acknowledge a vocabulary constraint but drift under generation pressure; and a self-check without prior framing catches errors too late to prevent them.

---

```
# topic-open — Register Topic and Plan Signals

You are executing the `topic-open` skill. Your outputs are:
1. An entry in `simulations/TOPICS.md`
2. A strategy file at `simulations/{TOPIC}/strategy.md`

---

## VOCABULARY LOCK

> This block is read before any schema, register, or phase.
> It declares the single constraint responsible for the most common output failures.

**Priority vocabulary — three values, no substitutes:**

| Value | Meaning | When to use |
|-------|---------|-------------|
| `essential` | Cannot commit to design without this | Signal is a hard gate |
| `recommended` | Commits with elevated risk without this | Signal improves decision quality |
| `optional` | Commits unaffected | Signal is informational only |

**Forbidden**: `high`, `medium`, `low`, `critical`, `p1`, `p2`, or any other vocabulary.

> **Wrong vocabulary = silent breakage. This is the most common mistake in this skill.**
> Tools that gate on priority look for exact string matches. `high` does not match `essential`.
> The gate silently fails. The Design Lead never detects the gap.
>
> Before writing the priority column in any signal row: re-read this block.
> After writing all rows: scan the priority column for forbidden values before advancing.

---

## INERTIA REGISTER

> Stable IR-NN IDs. Phase directives cite by ID.

| ID    | Default Behavior | Override Active In | Stakeholder Most Harmed |
|-------|------------------|--------------------|--------------------------|
| IR-01 | Skip stakeholder mapping | Phase 1 | Product Manager — loses commit-scope ground truth |
| IR-02 | Use high/medium/low priority vocabulary | Phase 2 | Design Lead — cannot gate design commit on unparseable priority |
| IR-03 | Collapse commit gate into signal plan | Phase 3 | Engineering Lead — no enforced readiness condition |
| IR-04 | Use freeform item names | Phase 4 | All consumers — strategy unreachable by path-based tools |
| IR-05 | Assign all signals to single owner role | Phase 2 | Cross-functional team — coverage gaps invisible |

---

## FIELD SCHEMA

> F-01 through F-05. Fill left to right in signal table.

| ID   | Field      | Constraint |
|------|------------|------------|
| F-01 | Priority   | `essential` / `recommended` / `optional` only — see VOCABULARY LOCK |
| F-02 | Namespace  | scout / draft / review / flow / trace / prove / listen / program / topic |
| F-03 | Skill      | Named skill under stated namespace |
| F-04 | Item Name  | `{topic}-{signal}-{date}.md` |
| F-05 | Owner Role | Named role; ≥ 2 distinct roles across all rows (IR-05 override) |

---

## COVERAGE SCHEMA

| ID     | Constraint | Minimum |
|--------|------------|---------|
| COV-01 | Signals marked `essential` | ≥ 1 |
| COV-02 | Distinct namespaces | ≥ 2 |
| COV-03 | Distinct owner roles | ≥ 2 |
| COV-04 | Narrative rationale | ≥ 2 sentences |

---

## PHASE 1 — STAKEHOLDER MAP

> Overriding IR-01 and IR-05.

Fill the table. Each row: named decision-maker role, specific risk if topic skipped, concrete decision informed.

| Row ID | Decision-Maker Role | Risk Exposure | Decision Informed |
|--------|---------------------|---------------|-------------------|
| S-01   |                     |               |                   |
| S-02   |                     |               |                   |
| S-03   |                     |               |                   |
| S-NN   | (add as needed)     |               |                   |

**Exit gate**: ≥ 3 rows; all four columns populated in every row. Check row count and column completeness as separate acts.

---

## PHASE 2 — SIGNAL PLAN

> Overriding IR-02 and IR-05.
> **Write NARRATIVE RATIONALE before the signal table.**

**Entry gate**: Phase 1 cleared. [ ]

### Narrative Rationale

Write ≥ 2 sentences here before building the signal table. Explain why this topic needs investigation and what design decision it informs. The roles you name become owner roles in the table.

[Write rationale here — before the signal table]

### Signal Table

> Re-read VOCABULARY LOCK before writing any priority value.

| Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04) | Owner Role (F-05) |
|-----------------|------------------|--------------|------------------|-------------------|
|                 |                  |              |                  |                   |

**Exit gate**:
- [ ] Priority column: every value is `essential` / `recommended` / `optional`
- [ ] COV-01: ≥ 1 `essential` signal
- [ ] COV-02: ≥ 2 distinct namespaces
- [ ] COV-03: ≥ 2 distinct owner roles
- [ ] COV-04: Narrative rationale written above, ≥ 2 sentences
- [ ] F-04: All item names follow `{topic}-{signal}-{date}.md`

---

## PHASE 3 — COMMIT GATE

> Overriding IR-03.

**Entry gate**: Phase 2 cleared. [ ]

```
COMMIT GATE for {TOPIC}
========================
Design commit authorized when ALL of the following signals exist in simulations/{TOPIC}/:

REQUIRED (essential):
  1. [item name]

PERMITTED AFTER COMMIT (recommended / optional):
  - [remaining signals]
```

**Exit gate**: Gate written. ≥ 1 essential item named. Gate is a condition.

---

## PHASE 4 — ARTIFACT WRITE

> Overriding IR-04.

**Entry gate**: Phase 3 cleared. [ ]

**Write 1**: Append to `simulations/TOPICS.md`:
```
| {TOPIC} | active | simulations/{TOPIC}/strategy.md | [description] |
```

**Write 2**: Write `simulations/{TOPIC}/strategy.md`:
```markdown
# {TOPIC} — Signal Strategy

## Rationale
[Phase 2 rationale]

## Stakeholder Map
[Phase 1 table]

## Signal Plan
[Phase 2 signal table]

## Commit Gate
[Phase 3 gate block]
```

---

## PHASE 5 — POST-GENERATION SELF-CHECK

> **Run after both files are written. Audit what you actually produced.**

### Essential Criteria Checklist

- [ ] **C-01 — TOPICS.md entry**: Does `simulations/TOPICS.md` contain a row for this topic with slug, description, and start date?
- [ ] **C-02 — Strategy path**: Is the strategy file at `simulations/{topic}/strategy.md` specifically — not a flat path, not inline in TOPICS.md?
- [ ] **C-03 — Five fields present**: Does every signal row contain all five fields: priority, namespace, skill, item name, owner role?
- [ ] **C-04 — Priority vocabulary**: Scan every priority cell now. Does each read exactly `essential`, `recommended`, or `optional`?
  - **PRIORITY DRIFT — AMEND TRIGGER**: Did any row use `high`, `medium`, `low`, or any other value? If yes, do not mark C-04 as passing. Go to AMEND.
- [ ] **C-05 — Essential signal present**: Does the signal table contain at least one row marked `essential`?

### AMEND Step

Run this step only if C-04 check found priority drift:

1. List every row where the priority value is not `essential`, `recommended`, or `optional`.
2. For each row: determine which allowed value best matches the intent (`essential` / `recommended` / `optional`).
3. Replace each incorrect value in the strategy file.
4. Re-scan the priority column: are all cells now exactly one of the three allowed values?
5. If the commit gate named any items from corrected rows, verify the item names still match.
6. Return to the checklist and re-check C-04.

Output is complete when all five essential criteria pass.
```

---

## V-05 — Combination: Compact design targeting all C-11 through C-15
**Hypothesis**: A minimal, clean prompt that directly addresses all five new rubric design criteria — standalone vocab block (C-11), consequence framing (C-14), rationale-before-table sequencing (C-15), post-generation self-check (C-12), and named priority drift AMEND step (C-13) — achieves equal or better compliance than the heavily scaffolded golden at lower cognitive load. The golden's pre-pipeline machinery (FAILURE EXAMPLE REGISTRY, PHASE CONSEQUENCE REGISTRY, six-column FIELD SCHEMA) is overhead that a well-positioned vocab lock and self-check can replace.

---

```
# topic-open — Register Topic and Plan Signals

You are executing `topic-open`. Your outputs:
1. Entry in `simulations/TOPICS.md`
2. Strategy file at `simulations/{TOPIC}/strategy.md`

---

## VOCABULARY CONSTRAINT

> Standalone block. Read before any instruction.

The priority field uses exactly three values. No others are valid.

```
essential    — team cannot commit to design without this signal
recommended  — team commits with elevated risk without this signal  
optional     — team commits unaffected; informational only
```

**Wrong vocabulary = silent downstream breakage. This is the most common mistake.**
Tools gate on exact string matches. Writing `high` instead of `essential` causes the
commit gate to silently fail — it does not error, it just stops working. The Design
Lead sees a passing strategy file that is actually broken.

Forbidden: `high`, `medium`, `low`, `critical`, `nice-to-have`, or any other value.

---

## DEFAULTS THIS SKILL OVERRIDES

| Default to override | What this skill does instead |
|---------------------|------------------------------|
| Skip stakeholder mapping | Phase 1 mandatory fill-in (≥ 3 rows) |
| Use high/medium/low priority | Vocabulary Constraint above — 3 values only |
| Collapse commit gate into signal plan | Phase 3 — structurally isolated commit gate |
| Use freeform item names | F-04: `{topic}-{signal}-{date}.md` |
| Single generic owner role | ≥ 2 distinct owner roles across signal rows |

---

## PHASE 1 — STAKEHOLDERS

Fill in at least three rows. Each row: named decision-maker role, what breaks for them if this topic is skipped, what concrete decision this topic informs.

| # | Decision-Maker Role | Risk If Skipped | Decision Informed |
|---|---------------------|-----------------|-------------------|
| S-01 | | | |
| S-02 | | | |
| S-03 | | | |

**Gate**: ≥ 3 rows; all columns populated. Do not advance until both checks pass.

---

## PHASE 2 — SIGNAL PLAN

> **Write narrative rationale FIRST. Then build the signal table.**
> Rationale written before the table ensures owner roles emerge from decision context.

**Entry gate**: Phase 1 cleared. [ ]

### Rationale (write this before the signal table)

Write ≥ 2 sentences: why does this topic need investigation, and what design decision will it inform?
Name the roles involved — these become owner roles in your signal table.

[Rationale here — minimum 2 sentences — before the table]

### Signal Table

Five columns. Left to right: Priority, Namespace, Skill, Item Name, Owner Role.
Re-read VOCABULARY CONSTRAINT before filling the Priority column.

| Priority | Namespace | Skill | Item Name (`{topic}-{signal}-{date}.md`) | Owner Role |
|----------|-----------|-------|------------------------------------------|------------|
| | | | | |

**Gate**:
- Priority: every cell is `essential` / `recommended` / `optional` only
- ≥ 1 row marked `essential`
- ≥ 2 distinct namespaces (scout, draft, review, flow, trace, prove, listen, program, topic)
- ≥ 2 distinct owner roles
- All item names match `{topic}-{signal}-{date}.md`

---

## PHASE 3 — COMMIT GATE

> Structurally isolated. Not a section of Phase 2.

**Entry gate**: Phase 2 cleared. [ ]

```
COMMIT GATE for {TOPIC}
========================
Design commit authorized when all REQUIRED signals exist in simulations/{TOPIC}/:

REQUIRED (essential):
  1. [item name from essential row]

PERMITTED AFTER COMMIT:
  - [recommended and optional signals]
```

**Gate**: ≥ 1 essential item named; gate expressed as a condition.

---

## PHASE 4 — WRITE ARTIFACTS

**Entry gate**: Phase 3 cleared. [ ]

**simulations/TOPICS.md** — append one row:
```
| {TOPIC} | active | simulations/{TOPIC}/strategy.md | [one-line description] |
```

**simulations/{TOPIC}/strategy.md** — write file:
```markdown
# {TOPIC} — Signal Strategy

## Rationale
[Phase 2 rationale]

## Stakeholder Map
[Phase 1 table]

## Signal Plan
[Phase 2 signal table]

## Commit Gate
[Phase 3 gate block]
```

---

## PHASE 5 — SELF-CHECK AND AMEND

> Run after both files are written. Read what you produced, not what you intended.

**Per-essential-criterion audit:**

- [ ] `simulations/TOPICS.md` has a row for this topic with slug, description, and start date?
- [ ] Strategy file is at `simulations/{topic}/strategy.md` — not a flat path?
- [ ] Every signal row has all five fields: priority, namespace, skill, item name, owner role?
- [ ] Every priority cell reads exactly `essential`, `recommended`, or `optional`?
- [ ] At least one signal row is marked `essential`?

**AMEND — Priority Drift Check (run for C-04 above):**
Scan the priority column in your written strategy file now.
- Did any row use `high`, `medium`, `low`, or any other value?
- If yes: list every row where drift occurred. Replace each value with the correct vocabulary. Re-scan before marking C-04 as passing.
- Confirm: are all priority cells now exactly one of `essential` / `recommended` / `optional`?

Output is complete when all five items above are checked.
```

---

## Summary: Variation Axis Map

| Variation | Single Axis / Combination | Primary Rubric Targets | Hypothesis |
|-----------|--------------------------|------------------------|------------|
| V-01 | Single — vocab placement | C-11, C-14 | Standalone vocab block before instructions prevents drift more than buried schema |
| V-02 | Single — post-generation check | C-12, C-13 | Post-write audit catches what pre-write gates miss; AMEND targets priority drift by name |
| V-03 | Single — phrasing register | C-11, C-12, C-13, C-14 | Conversational imperative + consequence framing improves compliance over formal schema tables |
| V-04 | Combination V-01+V-02 | C-11, C-12, C-13, C-14, C-15 | Prevention (vocab lock) + detection (self-check) form a two-layer defense |
| V-05 | Combination compact | C-11, C-12, C-13, C-14, C-15 | Minimal prompt with all 5 new criteria explicitly targeted achieves equal compliance at lower cognitive load |
