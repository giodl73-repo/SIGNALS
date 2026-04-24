Now I have everything. The R3 scorecard shows all 5 R3 variations scored 100/100 on the v3 rubric, with excellence signals pointing toward R4. Before writing the variations, let me trace R3 against the three new v4 criteria to understand the baseline:

**R3 gap analysis against C-18/C-19/C-20**:
- **C-18** (explicit anti-reconstruction directive): V-01, V-03, V-04, V-05 PASS; V-02 borderline ("use this exact template, because reconstructed templates drift" — reason given but prohibition not explicit)
- **C-19** (structural constraints cite downstream tool): V-02 PASS ("because topic-status and topic-scanner glob for this specific path"); V-04 PASS ("because topic-status parses all five for coverage computation"); V-01, V-03, V-05 FAIL — path and field schema rules have no tool name
- **C-20** (comparative failure framing): All 5 PASS for the rationale→table instruction, but only V-03 extends it to a second ordering instruction (template copy)

R4 primary gap: **C-19** fails in 3 of 5 R3 variations. **C-18** is borderline in V-02. **C-20** passes narrowly everywhere but only V-03 showed full depth.

---

# topic-open — Round 4 Variations

**Skill**: Register a new topic, define its strategy, plan the signals needed for design commit.
**Rubric version**: v4 (C-01 through C-20, aspirational denominator = 12)
**Round context**: All R3 variations scored 100/100 on the v3 rubric. Excellence signals carried forward: (1) named AMEND — DATE FIELD trigger parallel to PRIORITY DRIFT AMEND, (2) pervasive causal density across all ordering instructions. R4 adds C-18, C-19, C-20.

**R4 gap analysis against new criteria**:
- C-19 failed in V-01, V-03, V-05 (path and field schema rules had no tool citations)
- C-18 was borderline in V-02 (implicit prohibition, not explicit)
- C-20 was narrow in V-01, V-02, V-04, V-05 (single instruction contrasted; only V-03 extended to multiple)

**Variation axes selected**:
- C-18 as primary framing device (COPY-NOT-RECONSTRUCT applied as labeled rule to all templates) — single axis
- C-19 as pervasive architectural principle (tool citation on every structural constraint) — single axis
- C-20 extended to all ordering instructions (not just rationale→table) — single axis, conversational register
- Lifecycle phases + contrast tables at each phase decision boundary — combination
- Compact DEFAULTS TABLE extended with two new columns (What Breaks + Tool That Detects It) — combination

---

## V-01 — Anti-Reconstruction Architecture (C-18 primary axis)

**Axis**: C-18 as the primary organizing principle. The COPY-NOT-RECONSTRUCT directive is applied as a titled, labeled rule preceding every template and schema block — not embedded as a phrase within instruction prose. Each prohibition names the specific failure mode it prevents.

**Hypothesis**: In R3, anti-reconstruction directives appeared as phrases ("do not reconstruct from memory") embedded inside phase instructions. Elevating the prohibition to a titled rule that precedes each template signals a constraint class to the model, not a style preference. The named failure mode per template ("reconstruction drops the date field at high frequency"; "reconstruction collapses five fields to three or four, causing topic-status to silently skip rows") gives the model a concrete reason to treat each directive as load-bearing rather than advisory.

---

### VOCABULARY LOCK

> Standalone block. Read before anything else in this skill — because priority vocabulary errors corrupt all downstream automation silently, and the lock must be set before any schema or instruction below.

Signal priority uses exactly three values:
- `essential`
- `recommended`
- `optional`

**Wrong vocabulary = silent breakage. This is the most common mistake in this skill.**

`high` does not match `essential` in string comparison. topic-status performs exact string matching on the priority field. The commit gate silently fails — no error, no warning, the gate simply never fires. The Design Lead never learns the investigation is incomplete. Do not substitute `high`, `medium`, `low`, or any other term.

---

### TOPICS.md ROW TEMPLATE

> **COPY — DO NOT RECONSTRUCT.**
> Reconstruction failure mode: when the row template is rebuilt from memory rather than copied, the `{YYYY-MM-DD}` date field is dropped at high frequency. The resulting row registers the topic without a start date. topic-status cannot compute topic age or filter the registry by date range. Use the canonical template below and fill in the three placeholders.

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

Three required fields:
- **{topic-slug}**: lowercase-hyphenated identifier, unique within TOPICS.md
- **{one-line description}**: one sentence — what does this topic investigate, what decision does it inform?
- **{YYYY-MM-DD}**: ISO date the topic was opened (today's date). Not optional.

When you reach Phase 4 Write-1, return here and copy this template.

---

### FIELD SCHEMA

> **COPY — DO NOT RECONSTRUCT.**
> Reconstruction failure mode: reconstructed schemas consistently collapse five fields into three or four. topic-status parses all five fields for coverage computation; topic-scanner reads the Item Name field for signal file discovery. A missing field causes both tools to silently skip that signal row — coverage computation returns wrong counts with no error.

Every signal row requires five fields:

| Field | Values | Notes |
|-------|--------|-------|
| **Priority** | `essential` / `recommended` / `optional` | VOCABULARY LOCK applies — exact string match required |
| **Namespace** | scout / draft / review / flow / trace / prove / listen / program / topic | Pick from this list |
| **Skill** | specific skill within the namespace | e.g., `scout-feasibility` |
| **Item Name** | `{topic}-{signal}-{date}.md` | Full artifact filename pattern |
| **Owner Role** | role responsible for this signal | Derived from narrative rationale |

Coverage minimums:
- COV-01: ≥ 1 row marked `essential` — no essential = no commit gate = no defined finish line
- COV-02: ≥ 2 distinct namespaces — prevents monoculture investigations
- COV-03: ≥ 2 distinct owner roles — accountability must be distributed

---

### Skill Purpose

Register a new topic in the Signal system. Two outputs:
1. One row appended to `simulations/TOPICS.md` — using the ROW TEMPLATE above
2. Strategy file at `simulations/{topic}/strategy.md` — the editorial plan for this topic's investigation

---

### Phase 1 — Setup

Read `simulations/TOPICS.md`. Confirm this topic does not already exist. Stop on collision — do not create a duplicate entry.

---

### Phase 2 — Narrative Rationale + Signal Table

**Write NARRATIVE RATIONALE first. Then build the signal table.**

Write the rationale before the signal table — because the decisions you describe in the rationale determine which roles are responsible for which signals. If you write the rationale first, owner roles emerge from purpose: each role is the stakeholder for a decision that must be answered. If you write the signal table first, owner roles become post-hoc labels assigned to fill a column without a derivable reason to exist.

Rationale requirements:
- ≥ 2 sentences
- State: (1) why this topic needs investigation, (2) what design decisions the signals will inform

Build the signal table after the rationale exists. Apply FIELD SCHEMA to every row.

**Phase 2 Exit Gate** — check before advancing:
- [ ] Rationale written and ≥ 2 sentences
- [ ] Every priority value matches VOCABULARY LOCK exactly
- [ ] COV-01: ≥ 1 `essential` row
- [ ] COV-02: ≥ 2 distinct namespaces
- [ ] COV-03: ≥ 2 distinct owner roles
- [ ] All item names follow `{topic}-{signal}-{date}.md`

---

### Phase 3 — Commit Gate

Structurally isolated from Phase 2. Written after the signal table — because the gate is enumerated from essential signals, and the table must exist before the gate can name them.

```
## COMMIT GATE
Design commit requires all essential signals complete:
- {item-name-1}
- {item-name-2}
[list all essential signals by exact item name]
```

---

### Phase 4 — Write Output

**Write-1 — TOPICS.md entry**

Return to the **TOPICS.md ROW TEMPLATE** above. Copy it — do not reconstruct. Fill in the three placeholders. Append to `simulations/TOPICS.md`.

**Write-2 — Strategy file**

Write to `simulations/{topic}/strategy.md` — not a flat path, not inline in TOPICS.md — because topic-status and topic-scanner glob for this specific path. A wrong or flat path causes silent coverage failure: topic-status reports zero coverage and topic-scanner discovers zero signals, both with no diagnostic.

Contents: narrative rationale, signal table, COMMIT GATE section.

---

### Phase 5 — Post-Generation Self-Check

Read what you actually wrote. Not what you intended — what you produced.

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date?
**C-02**: Strategy at `simulations/{topic}/strategy.md` — not flat?
**C-03**: Every signal row has all five fields (Priority, Namespace, Skill, Item Name, Owner Role)?
**C-04**: Every priority exactly `essential` / `recommended` / `optional`?
**C-05**: At least one `essential` signal?

**AMEND — PRIORITY DRIFT**: If C-04 fails: list each row with drift. Replace invalid priority values. Re-scan all cells. Re-run C-04 before marking passing.

**AMEND — DATE FIELD**: If C-01 fails on date: return to the TOPICS.md ROW TEMPLATE above. Copy the three-field canonical template. Fill in today's date. Verify three fields present before proceeding.

---

---

## V-02 — Tool-Citation Pervasive (C-19 primary axis)

**Axis**: C-19 as the primary organizing principle. Every structural constraint in the skill — vocabulary rule, path rule, field schema, commit gate isolation — is anchored to the exact downstream tool that depends on it. The pattern applied throughout: "Rule X applies because Tool Y depends on it and silently fails if X is violated."

**Hypothesis**: In R3, only V-02 and V-04 cited specific tools for structural constraints, and only for one rule each. R4 V-02 extends tool citation to every structural constraint: vocabulary lock (topic-status commit-gate check), path rule (topic-status and topic-scanner glob), field schema (topic-status coverage parse + topic-scanner item discovery), commit gate isolation (topic-status section parser). When the model understands which specific automation breaks for each rule, it treats each rule as a system invariant rather than a style guideline — and can reason about the intent rather than just restoring surface form under generation pressure.

---

### VOCABULARY LOCK

> **Standalone block. Read before anything else in this skill — because priority vocabulary errors corrupt all downstream automation silently. This lock must be set before any schema or instruction is read.**

Signal priority uses exactly three values:
- `essential`
- `recommended`
- `optional`

**Wrong vocabulary = silent breakage. This is the most common mistake in this skill.**

How topic-status enforces this: it performs exact string comparison against `essential`, `recommended`, `optional`. Writing `high` instead of `essential` does not produce an error — topic-status simply excludes that signal from the commit-gate check. The gate silently fails. The Design Lead sees a valid-looking strategy file and believes the investigation is on track. This is why the constraint is here, first, before you encounter any row: the vocabulary is locked before any schema or instruction can introduce drift.

---

### TOPICS.md ROW TEMPLATE

Copy this template — do not reconstruct it. When rebuilt from memory, the `{YYYY-MM-DD}` date field is the most commonly dropped placeholder:

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

Three fields required:
- **{topic-slug}**: lowercase-hyphenated identifier, unique within TOPICS.md
- **{one-line description}**: one sentence — what this topic investigates and what decision it informs
- **{YYYY-MM-DD}**: ISO date opened (today's date). Not optional.

---

### FIELD SCHEMA

**Five fields required per signal row — because topic-status parses all five fields for coverage computation, and topic-scanner reads the Item Name field for signal artifact discovery.**

A schema with four fields (common when Owner Role is merged with Skill, or Item Name is omitted) causes topic-status to silently skip those rows in coverage counts — zero error, wrong percentage. A missing or malformed Item Name causes topic-scanner to fail to discover that signal's artifact file.

| Field | Values |
|-------|--------|
| **Priority** | `essential` / `recommended` / `optional` — VOCABULARY LOCK |
| **Namespace** | scout / draft / review / flow / trace / prove / listen / program / topic |
| **Skill** | specific skill within the namespace |
| **Item Name** | `{topic}-{signal}-{date}.md` |
| **Owner Role** | role responsible for this signal |

Coverage minimums:
- COV-01: ≥ 1 `essential` — no essential = no commit gate
- COV-02: ≥ 2 distinct namespaces
- COV-03: ≥ 2 distinct owner roles

---

### Skill Purpose

Two outputs:
1. Row appended to `simulations/TOPICS.md`
2. Strategy file at `simulations/{topic}/strategy.md`

---

### Phase 1 — Setup

Read `simulations/TOPICS.md` — because topic-status loads this file on every status check; a duplicate topic entry creates ambiguous coverage aggregation with no merge path. Confirm the topic is not already registered. Stop on collision.

---

### Phase 2 — Narrative Rationale + Signal Table

**Write NARRATIVE RATIONALE before building the signal table.**

Write the rationale before the table — because the rationale surfaces the decisions that determine owner roles. If the rationale comes first, each owner role in the table maps to a decision stakeholder who must answer the question being investigated. If the signal table comes first, owner roles become retroactive column-fillers with no derivable reason to exist. Step A (rationale) determines who should care; Step B (table) formalizes it.

**Step A — Write Narrative Rationale**

≥ 2 sentences. State: (1) why this topic requires investigation, (2) what design decisions the signals inform.

**Step B — Build Signal Table**

After the rationale exists. Columns: Priority | Namespace | Skill | Item Name | Owner Role. Apply FIELD SCHEMA to every row.

**Phase 2 Exit Gate**:
- [ ] Rationale written and ≥ 2 sentences
- [ ] Every priority exactly `essential` / `recommended` / `optional`
- [ ] COV-01: ≥ 1 `essential` row
- [ ] COV-02: ≥ 2 distinct namespaces
- [ ] COV-03: ≥ 2 distinct owner roles
- [ ] All item names: `{topic}-{signal}-{date}.md`

---

### Phase 3 — Commit Gate

**Structurally isolated section. Written after the signal table — because topic-status reads the `## COMMIT GATE` section as a named, parseable block to determine design-commit readiness. A commit gate embedded inside the signal table (as a subsection or row) fails topic-status's section parser — coverage computation returns no gate status.**

```
## COMMIT GATE
Design commit requires all essential signals complete:
- {item-name-1}
- {item-name-2}
[all essential signals by exact item name]
```

---

### Phase 4 — Write Output

**Write-1 — TOPICS.md entry**

Return to the TOPICS.md ROW TEMPLATE above. Copy it — do not reconstruct. Append to `simulations/TOPICS.md`.

**Write-2 — Strategy file**

Write to `simulations/{topic}/strategy.md` — not a flat path, not inline in TOPICS.md — because topic-status and topic-scanner both glob for `simulations/{topic}/strategy.md` specifically. topic-status uses this path to compute coverage; topic-scanner uses it to discover planned signals for a topic. A flat path (`simulations/strategy.md`) or mismatched path causes both tools to silently return zero results with no diagnostic.

Contents: narrative rationale, signal table, COMMIT GATE section.

---

### Phase 5 — Post-Generation Self-Check

Run after both files are written — because this phase checks what you produced, not what you planned. Running before writing would test intentions; running after tests output.

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date?
**C-02**: Strategy at `simulations/{topic}/strategy.md`?
**C-03**: Every signal row has all five fields — topic-status parses all five; missing fields = silently skipped rows?
**C-04**: Every priority exactly `essential` / `recommended` / `optional` — exact string match required by topic-status?
**C-05**: At least one `essential` signal?

**AMEND — PRIORITY DRIFT**: If C-04 fails: list each row with drift. Replace invalid priority values. Re-scan all cells. Re-run C-04 before marking passing.

**AMEND — DATE FIELD**: If C-01 fails on date: return to the ROW TEMPLATE above. Copy the three-field canonical template. Fill in today's date. Verify three fields present before proceeding.

---

---

## V-03 — Comparative Failure Framing Throughout (C-20 primary axis, conversational register)

**Axis**: C-20 extended beyond the rationale→table instruction to cover all four ordering decisions in the skill. Each ordering instruction uses explicit side-by-side path contrast: (1) vocabulary-first vs. schema-first, (2) copy-template vs. reconstruct, (3) rationale-before-table vs. table-before-rationale, (4) self-check-after-writing vs. self-check-before-writing. Phrasing is conversational (R3 V-03 register), which produced the strongest C-14 vividness in R3.

**Hypothesis**: In R3, all variations showed comparative framing for the rationale→table ordering (C-17/C-20 passing). Only V-03 extended contrast framing to the template copy instruction, and no variation extended it to the vocabulary-first or self-check-timing instructions. R4 V-03 applies the contrast pattern systematically to every ordering choice. When every ordering decision has a visible non-compliant path with a concrete consequence, the model has a full cost map — it can reason about intent at each step rather than restoring surface order.

---

### BEFORE YOU START: VOCABULARY

Read this before anything else.

Signal priority has exactly three valid values:
- `essential`
- `recommended`
- `optional`

**Do not use `high`, `medium`, or `low`. Not even once.**

**If you read this block first**: the constraint is locked before you encounter any signal row. Every row you write is already constrained by the vocabulary you just read. topic-status finds the signals, the commit gate fires correctly.

**If you skip this block and read the schema first**: you may already have formed row vocabulary before the constraint arrives. Priority drift happens. topic-status performs exact string matching — `high` does not match `essential`. The commit gate silently excludes that signal. The Design Lead sees a valid-looking strategy file. The investigation stalls. No error is raised.

This is why the vocabulary block is here, first. Read it now.

---

### TOPICS.md ROW TEMPLATE

Copy this template when writing the TOPICS.md entry:

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

Three required fields: slug (lowercase-hyphenated), description (one sentence), date (YYYY-MM-DD today).

**If you copy this template**: you get three fields, including the date. Fill in the placeholders. The row is complete.

**If you reconstruct the template from memory**: the `{YYYY-MM-DD}` date field is dropped at high frequency. The row registers the topic without a start date. Date-dependent queries on the topic registry return wrong results.

Copy. Do not reconstruct.

---

### What You're Making

Two outputs:
1. A row in `simulations/TOPICS.md` — so the topic exists in the registry
2. A strategy file at `simulations/{topic}/strategy.md` — your plan for how to investigate this topic

---

### Step 1: Check for Collisions

Read `simulations/TOPICS.md`. Confirm the topic does not already exist. Stop on collision.

---

### Step 2: Write Your Rationale First

Before you build the signal table, write ≥ 2 sentences explaining:
- Why does this topic need investigation?
- What design decision will these signals inform?

Write this **before** the table — not after.

**If you write the rationale first**: the decisions you describe surface the question "who should own this signal?" Owner roles in the table emerge from the stakeholders you just named. Each role exists because a specific decision requires a specific accountable person.

**If you write the table first**: you fill the Owner Role column after the fact, looking for roles to assign to a schema slot. The roles become post-hoc labels — they reflect column structure, not decision accountability. A coverage review has no way to assess whether the roles are correct.

The rationale determines the roles. Write it first.

---

### Step 3: Build the Signal Table

After writing the rationale, build the table. Five columns:

| Priority | Namespace | Skill | Item Name | Owner Role |
|----------|-----------|-------|-----------|------------|

Rules:
- **Priority**: `essential`, `recommended`, or `optional` — exactly those words (see vocabulary block above). topic-status gates on exact string match.
- **Namespace**: scout / draft / review / flow / trace / prove / listen / program / topic — use **at least 2 distinct namespaces**
- **Skill**: the specific skill within the namespace
- **Item Name**: `{topic}-{signal}-{date}.md`
- **Owner Role**: drawn from the decisions you described in Step 2

Minimums:
- ≥ 1 row marked `essential` — without this, you have no commit gate and no defined finish line
- ≥ 2 distinct namespaces
- ≥ 2 distinct owner roles

---

### Step 4: Name Your Commit Gate

Write a `## COMMIT GATE` section in strategy.md listing every `essential` signal by its exact item name.

---

### Step 5: Write the Files

**File 1 — TOPICS.md row**: Use the template above. Copy it — do not reconstruct.

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

**File 2 — strategy.md**: Write to `simulations/{topic}/strategy.md` — not a flat path, not inline in TOPICS.md — because topic-status and topic-scanner glob for this specific path. A wrong path causes both tools to silently return zero results.

---

### Step 6: Check Your Work

**If you run this check after writing**: you verify what you actually produced. Generation errors that diverge from intentions are caught. The check is meaningful.

**If you run this check before writing**: you verify what you intend to produce. Intentions and outputs diverge under generation pressure — this catches nothing real.

Run it after writing.

**Q1**: Does the TOPICS.md row have three fields — slug, description, date in YYYY-MM-DD format?

**Q2**: Is strategy.md at `simulations/{topic}/strategy.md` — not flat, not inside TOPICS.md itself?

**Q3**: Does every signal row have all five fields: Priority, Namespace, Skill, Item Name, Owner Role?

**Q4**: Did any priority drift to `high`, `medium`, `low`, or anything else?
→ If yes — stop. List every row where it happened. Replace each invalid value. Read the vocabulary block if you need a reminder. Do not mark Q4 done until every priority cell reads exactly `essential`, `recommended`, or `optional`.

**Q5**: Does the signal table have at least one row marked `essential`?

**AMEND — PRIORITY DRIFT**: If Q4 fails: list every row with drift. Replace each value. Re-scan all priority cells before marking Q4 passing.

**AMEND — DATE FIELD**: If Q1 fails on date: return to the ROW TEMPLATE in Step 5. Copy the three-field canonical template. Fill in today's date in YYYY-MM-DD. Verify all three fields are present before proceeding.

---

---

## V-04 — Combination: Lifecycle Phases + Contrast Tables

**Combination**: Full phase structure (R3 V-04 base) combined with explicit two-row path contrast tables at each phase decision point. Phase 2 (rationale ordering), Phase 4 (template copy), and Phase 5 (check timing) each have a Compliant / Non-Compliant contrast block. All three R4 criteria at maximum depth: C-18 (explicit prohibition with named failure mode), C-19 (tool citation on path, field schema, and commit gate), C-20 (contrast tables throughout, not just rationale instruction).

**Hypothesis**: The phase structure provides navigable scaffolding. Contrast tables at phase transitions add a consequence layer — the model doesn't just follow phase instructions, it can see the failure mode of the wrong path at each decision point. Together, scaffolding + contrast tables create a skill that is both easy to navigate and robust to generation pressure: at every key decision, the cost of the non-compliant path is explicitly shown rather than asserted.

---

### VOCABULARY LOCK

> **Standalone block. Read before anything else in this skill — because priority vocabulary errors corrupt all downstream automation silently, and this lock must be set before any schema or instruction below.**

Signal priority uses exactly three values:
- `essential`
- `recommended`
- `optional`

**Wrong vocabulary = silent breakage. This is the most common mistake in this skill.**

topic-status performs exact string comparison on the priority field. `high` does not match `essential`. The commit gate silently fails — it does not error, it simply never trips. The Design Lead never detects the gap. Do not use `high`, `medium`, `low`, or any substitution.

---

### TOPICS.md ROW TEMPLATE

> **COPY — DO NOT RECONSTRUCT.**
> Reconstruction failure mode: the `{YYYY-MM-DD}` date field is the most commonly dropped field when the template is rebuilt from memory. A row without a date is structurally valid markdown but breaks date-range queries on the topic registry. Use the canonical template below.

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

Three required fields:
- **{topic-slug}**: lowercase-hyphenated identifier, unique within TOPICS.md
- **{one-line description}**: one sentence — what this topic investigates and what decision it informs
- **{YYYY-MM-DD}**: ISO date opened (today's date). Not optional.

When you reach Phase 4 Write-1, return here and copy this template.

---

### FIELD SCHEMA

**Five fields per signal row — topic-status parses all five fields for coverage computation; topic-scanner reads the Item Name field for signal artifact discovery:**

| Field | Values |
|-------|--------|
| F-01 Priority | `essential` / `recommended` / `optional` — VOCABULARY LOCK |
| F-02 Namespace | scout / draft / review / flow / trace / prove / listen / program / topic |
| F-03 Skill | specific skill within the namespace |
| F-04 Item Name | `{topic}-{signal}-{date}.md` |
| F-05 Owner Role | role responsible for this signal |

Coverage minimums:
- COV-01: ≥ 1 `essential` row (no essential = no commit gate = no defined finish line)
- COV-02: ≥ 2 distinct namespaces
- COV-03: ≥ 2 distinct owner roles

---

### Skill Purpose

Register a new topic. Two outputs:
1. One row appended to `simulations/TOPICS.md`
2. Strategy file at `simulations/{topic}/strategy.md`

---

### Phase 1 — Setup

Read `simulations/TOPICS.md`. Confirm this topic does not already exist. Stop on collision — do not create a duplicate entry.

---

### Phase 2 — Content Generation

#### Phase 2 Decision: Rationale Before Table

| Path | Consequence |
|------|-------------|
| **Compliant**: Write narrative rationale first, then signal table | Owner roles emerge from the decisions described in the rationale — each role is the accountable stakeholder for a question being answered. Coverage review can verify roles against the rationale. |
| **Non-compliant**: Write signal table first, then add rationale | Owner roles are assigned post-hoc to fill a schema column. They reflect column structure, not decision accountability. A coverage review has no basis to challenge or validate them. |

**Step 2A — Write Narrative Rationale**

≥ 2 sentences. State: (1) why this topic requires investigation, (2) what design decisions the signals inform.

**Step 2B — Build Signal Table**

After the rationale exists. Columns: Priority | Namespace | Skill | Item Name | Owner Role. Apply F-01 through F-05 to every row.

**Phase 2 Exit Gate**:
- [ ] Rationale written and ≥ 2 sentences
- [ ] Every priority exactly `essential` / `recommended` / `optional`
- [ ] COV-01: ≥ 1 `essential` row
- [ ] COV-02: ≥ 2 distinct namespaces
- [ ] COV-03: ≥ 2 distinct owner roles
- [ ] All item names: `{topic}-{signal}-{date}.md`

---

### Phase 3 — Commit Gate

Structurally isolated from Phase 2. Written after the signal table — because topic-status reads `## COMMIT GATE` as a named parseable section to determine design-commit readiness. A gate embedded inside the signal table as a subsection or row fails topic-status's section parser; coverage computation returns no gate status.

```
## COMMIT GATE
Design commit requires all essential signals complete:
- {item-name-1}
- {item-name-2}
[all essential signals by exact item name]
```

---

### Phase 4 — Write Output

#### Phase 4 Decision: Template Copy vs. Reconstruction

| Path | Consequence |
|------|-------------|
| **Compliant**: Return to ROW TEMPLATE above. Copy it. Fill in placeholders. | Three fields present, including the date. No omission possible from inference. |
| **Non-compliant**: Reconstruct the row format from memory. | The `{YYYY-MM-DD}` date field is dropped at high frequency. The topic is registered without a start date. |

**Write-1 — TOPICS.md entry**

Return to the **TOPICS.md ROW TEMPLATE** above. Copy it — do not reconstruct. Fill in the three placeholders. Append to `simulations/TOPICS.md`.

**Write-2 — Strategy file**

Write to `simulations/{topic}/strategy.md` — not a flat path, not inline in TOPICS.md — because topic-status and topic-scanner glob for this specific path. A wrong path causes both tools to silently return zero results with no diagnostic.

Contents: narrative rationale, signal table, COMMIT GATE section.

---

### Phase 5 — Post-Generation Self-Check

#### Phase 5 Decision: Check Timing

| Path | Consequence |
|------|-------------|
| **Compliant**: Run this check after both files are written. | Verifies what you produced — catches generation errors that diverged from intentions. The check is meaningful. |
| **Non-compliant**: Run this check before writing. | Verifies what you intend to produce. Intentions and outputs diverge under generation pressure. Does not catch generation errors. |

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date?
**C-02**: Strategy at `simulations/{topic}/strategy.md` — not flat?
**C-03**: Every signal row has all five fields (F-01 through F-05)?
**C-04**: Every priority exactly `essential` / `recommended` / `optional`?
**C-05**: At least one `essential` signal?

**AMEND — PRIORITY DRIFT**: If C-04 fails: list each row with drift. Replace invalid priority values. Re-scan all cells. Re-run C-04 before marking passing.

**AMEND — DATE FIELD**: If C-01 fails on date: return to the TOPICS.md ROW TEMPLATE above. Copy the three-field canonical template. Fill in today's date. Verify three fields present before proceeding.

---

---

## V-05 — Compact + Extended DEFAULTS TABLE (Combination)

**Combination**: R3 V-05's compact DEFAULTS TABLE structure extended from three columns to five: Default → This Skill's Rule → Why → What Breaks If You Skip → Tool That Detects It. The two new columns simultaneously satisfy C-20 (the "What Breaks" column makes the non-compliant path consequence concrete for each rule, not just the rationale instruction) and C-19 (the "Tool" column names the specific downstream tool for each structural constraint). The DEFAULTS TABLE becomes a complete decision matrix; no new sections are added.

**Hypothesis**: R3 V-05 achieved 100/100 with the fewest sections, using a DEFAULTS TABLE to absorb inertia, coverage, and sequencing rationale compactly. Adding two columns converts the table from a 3-column declaration into a 5-column consequence chain. The model gets C-19 tool citation and C-20 comparative framing for every rule in a single block — without additional phases or prose sections. The compact structure is preserved while adding full consequence coverage.

---

### VOCABULARY CONSTRAINT

Standalone block. Read before any instruction.

Signal priority: exactly `essential` / `recommended` / `optional`. Wrong vocabulary = silent downstream breakage. **This is the most common mistake.**

topic-status performs exact string comparison on the priority field. Writing `high` instead of `essential` causes the commit-gate check to silently exclude that signal — no error, no warning, the gate never fires. The Design Lead sees a passing strategy file that is actually broken.

---

### TOPICS.md ROW TEMPLATE

Copy this template when writing the TOPICS.md entry. Do not reconstruct from memory — reconstructed templates reliably drop the date field:

```
| {topic-slug} | {one-line description of what this topic investigates} | {YYYY-MM-DD} |
```

Three fields required: slug (lowercase-hyphenated), description (one sentence), date (YYYY-MM-DD, today).

---

### DEFAULTS THIS SKILL OVERRIDES

| Default | This Skill's Rule | Why | What Breaks If You Skip | Tool That Detects It |
|---------|-------------------|-----|------------------------|---------------------|
| Any priority vocabulary | `essential` / `recommended` / `optional` only — exact string | Downstream tools gate on exact string matches | Commit gate silently excludes signals; investigation stalls with no warning or diagnostic | topic-status (commit-gate check, exact string match) |
| Free-form TOPICS.md row | Copy ROW TEMPLATE above — 3 fields: slug, description, YYYY-MM-DD | Date field required; reconstructed rows drop it | Topic registry missing date; date-range queries return wrong results; topic cannot be filtered by age | topic-status (date filter) |
| Signal table before rationale | Rationale first, then signal table | Owner roles emerge from decision context. If table first: roles are labels with no derivable purpose. If rationale first: roles are stakeholders accountable to named decisions. | Owner roles are unverifiable; coverage review has no basis to assess accountability distribution | topic-story (role synthesis during narrative) |
| Inline commit gate | Structurally isolated `## COMMIT GATE` section | topic-status reads this as a named section; embedded gates fail the section parser | topic-status cannot determine design-commit readiness; commit gate reports as missing | topic-status (commit-gate section parser) |
| Flat strategy path | Write to `simulations/{topic}/strategy.md` | topic-status and topic-scanner glob for this specific path | Both tools silently return zero results; coverage computation produces 0 with no error | topic-status, topic-scanner (glob pattern match) |

---

### Phase 1 — Setup

Read `simulations/TOPICS.md`. Confirm topic not already registered. Stop on collision.

---

### Phase 2 — Generate

**Rationale first. Signal table second.**

Write the narrative rationale before building the signal table — because the rationale determines which decisions need answering, and those decisions determine which roles are accountable. If the rationale comes first, owner roles in the table emerge as the stakeholders responsible for each open decision. If the table comes first, owner roles become column-fillers assigned to satisfy a schema requirement, with no derivable accountability.

Rationale: ≥ 2 sentences. State why the topic requires investigation and what decisions the signals inform.

Signal table (after rationale is written):

| Priority | Namespace | Skill | Item Name | Owner Role |
|----------|-----------|-------|-----------|------------|

Requirements:
- Priority: `essential` / `recommended` / `optional` — see VOCABULARY CONSTRAINT
- Item Name: `{topic}-{signal}-{date}.md`
- ≥ 1 row `essential`; ≥ 2 distinct namespaces (scout/draft/review/flow/trace/prove/listen/program/topic); ≥ 2 distinct owner roles

---

### Phase 3 — Commit Gate

Structurally isolated. Not a subsection of Phase 2.

Write `## COMMIT GATE` in strategy.md listing all `essential` signals by exact item name:

```
## COMMIT GATE
Design commit requires all essential signals complete:
- {item-name-1} [all essential signals]
```

---

### Phase 4 — Write

**TOPICS.md entry**: Return to the ROW TEMPLATE above. Copy it. Fill in slug, description, and today's date. Three fields — do not omit the date. Append to `simulations/TOPICS.md`.

**Strategy file**: Write to `simulations/{topic}/strategy.md` — see DEFAULTS TABLE for path rule and tool dependency.

---

### Phase 5 — Self-Check and Amend

After both files written — because checking after writing tests what you produced; checking before writing tests what you intended to produce. These are not the same. Run it after.

**C-01**: TOPICS.md row has slug + description + YYYY-MM-DD date?
**C-02**: Strategy at `simulations/{topic}/strategy.md`?
**C-03**: Every signal row has all five fields: priority, namespace, skill, item name, owner role?
**C-04**: Every priority exactly `essential` / `recommended` / `optional`?
**C-05**: At least one `essential` row?

**AMEND — Priority Drift**: If C-04 fails: identify each row with drift. Replace invalid values. Re-scan before marking C-04 passing.

**AMEND — Date Field**: If C-01 fails on date: return to the ROW TEMPLATE above. Copy the three-field canonical template. Fill in today's date. Verify three fields present before proceeding.

---

---

## Variation Summary

| Axis | V-01 | V-02 | V-03 | V-04 | V-05 |
|------|------|------|------|------|------|
| Primary | C-18 as labeled rule (COPY-NOT-RECONSTRUCT on each template/schema block) | C-19 pervasive (tool citation on every structural constraint) | C-20 throughout (contrast framing on all 4 ordering choices) | Lifecycle phases + contrast tables at each phase decision | Compact DEFAULTS TABLE + 2 new columns (What Breaks, Tool) |
| Register | Formal / technical | Formal / technical | Conversational / imperative | Formal / technical | Compact / declarative |
| C-18 depth | Titled rule per block, named failure mode per block | Explicit prohibition with reason | Per-instruction "If you copy / If you reconstruct" | Titled rule + Phase 4 contrast table | Explicit prohibition with named failure mode |
| C-19 depth | Path + field schema | Path + field schema + commit gate + Phase 1 | Path only | Path + field schema + commit gate | All rules via DEFAULTS TABLE "Tool" column |
| C-20 depth | Rationale ordering | Rationale ordering | All 4 ordering choices: vocab-first, template-copy, rationale, self-check timing | All 3 major phase decisions (contrast tables) | All rules via DEFAULTS TABLE "What Breaks" column |
| Structure | 5 phases + 3 named header blocks | 5 phases + 2 named header blocks | 6 conversational steps + 2 named header blocks | 5 phases + 2 named header blocks + 3 contrast tables | 4 phases + 1 extended DEFAULTS TABLE |

**R4 predicted gaps closed**:
- V-01: Fixes C-19 (adds tool citations to both path and field schema) while making C-18 the primary structural motif
- V-02: Fixes C-18 borderline from R3 V-02 (explicit "do not reconstruct" added); C-19 extended to commit gate and Phase 1
- V-03: Fixes C-19 (adds tool citation to path rule); makes C-20 the deepest of any variation across 4 instructions
- V-04: Fixes nothing from R3 V-04 (already strongest in R3); explores contrast-table structure as C-20 delivery format
- V-05: Fixes C-19 (adds "Tool" column to DEFAULTS TABLE); C-20 delivered via "What Breaks" column for all rules, not just rationale instruction
