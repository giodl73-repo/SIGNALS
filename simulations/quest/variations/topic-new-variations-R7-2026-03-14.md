Written to `simulations/quest/variations/topic-new-variations-R7-2026-03-14.md`.

---

## Round 7 Variations — topic-new (v6 rubric)

**R6 diagnosis**: Under v6's two new criteria, only V-03 from R6 satisfies all 14 aspirational criteria. The other four variations fail:
- **C-21** (per-phase exit gates): V-01, V-02, V-04 had only one pre-write gate; V-05 had a gate in Phase 7 only
- **C-22** (stakeholder minimum row count gate): V-01, V-04, V-05 had "Minimum 3 rows" as a prose note, not a structural exit gate

**R7 design**: All five variations satisfy C-21 and C-22 via structurally distinct mechanisms.

| # | Axis | C-21/C-22 mechanism |
|---|------|---------------------|
| V-01 | Compact gate injection | One-item checklist after every phase; Phase 1 gate: `>= 3 rows, all four columns filled` |
| V-02 | Conversational register fix | "Before moving on" checklist at every step + named COVERAGE SCHEMA table (also fixes C-18 from R6) |
| V-03 | Pipeline overview table | Opening pipeline spec table with Exit Gate column for every phase row — C-21 satisfied architecturally before any phase content is read |
| V-04 | Schema-row-cited gates | Gates cite schema rows by ID (F-01–F-05, COV-01–COV-03); Phase 1 gate: `S-TABLE: >= 3 rows` |
| V-05 | Inertia framing + per-phase gates | Every phase opens with inertia statement + closes with exit gate checklist; Phase 1 gate: `>= 3 rows, roles specific` |

**Expected outcomes under v6**: V-01, V-03, V-04, V-05 should score 100 (14/14). V-02 should also reach 100 — the C-18 failure from R6 is fixed by the named COVERAGE SCHEMA table in Step 4. New discriminating question: does V-04's schema-ID gate notation satisfy C-21's "named condition or checklist" requirement, or does it need a more explicit checklist form?
Gates cite schema rows by identifier (F-01–F-05, COV-01–COV-03) rather than restating constraints inline. C-21 via a gate at every boundary. C-22 via "S-TABLE: >= 3 rows" as an explicit Phase 1 gate item. Tests whether schema-coupled gates are harder to satisfy trivially. |
| V-05 | Inertia framing + per-phase gates | R6 V-05 redesigned: every phase still opens with an inertia statement (ambient failure before this phase runs) and now closes with an explicit exit gate checklist. Phase 1 gate includes >= 3 rows. Tests whether motivational openers + structural gates produce the highest comprehension-enforcement product. |

---

## V-01 — Compact Gate Injection

**Variation axis**: Lifecycle emphasis (minimal gate form) — V-04 (R6) base with an explicit one-item or two-item exit gate appended after every section
**Hypothesis**: The minimum viable exit gate is a one-line bold assertion or a two-checkbox block. V-04's compressed bold-heading format already satisfies C-01–C-20; adding compact gates after every phase satisfies C-21 without bloating the template. C-22 is satisfied by converting the stakeholder prose note into a checklist gate: "Phase 1 exit gate: >= 3 rows, all columns filled."

---

### Skill: topic:new

**Inputs**: topic name
**Outputs**: TOPICS.md row + `simulations/{topic}/strategy.md`

---

#### Phase 1 — Stakeholders (first output)

Fill in this table before any other output:

| # | Role | Immediate Risk (topic fails) | Downstream Risk (topic skipped) |
|---|------|------------------------------|--------------------------------|
| S-1 | | | |
| S-2 | | | |
| S-3 | | | |

Roles must be specific (not "user", not "team"). The Stakeholder Ref column in FIELD SCHEMA cites these rows by `S-N`. Citations to unlisted rows are broken references. Signal rows without citations are unauditable.

**Phase 1 exit gate:**
- [ ] >= 3 rows, all four columns filled
- [ ] Roles are specific and non-generic

---

#### Phase 2 — TOPICS.md

Append exactly one row to `simulations/TOPICS.md`:

| Topic | Status | Strategy | Registered |
|-------|--------|----------|------------|
| {topic} | planning | simulations/{topic}/strategy.md | {date} |

**Phase 2 exit gate:**
- [ ] Row appended; status = `planning`; path = `simulations/{topic}/strategy.md`

---

#### Phase 3 — Rationale

Create `simulations/{topic}/strategy.md`. Write a Rationale section. Minimum 2 sentences: why this topic needs investigation, and what design decision it informs.

**Phase 3 exit gate:**
- [ ] >= 2 sentences; design decision named

---

#### Phase 4 — FIELD SCHEMA

**FIELD SCHEMA**

| Field | Valid Values | Stakeholder Ref | Immediate Failure | Downstream Effect |
|-------|-------------|-----------------|-------------------|-------------------|
| namespace | scout / draft / review / flow / trace / prove / listen / program / topic | — | Row unroutable; no execution path | Namespace gap permanent in evidence base |
| skill | valid skill in namespace | — | Not invokable; artifact never produced | Signal category absent from all commit evaluations |
| item name | `{topic}-{signal}-{date}.md` — see Phase 5 | — | Unlocatable by topic registry | Narrative references a nonexistent file |
| owner role | role from Stakeholders table | Required: cite S-N | No accountable party; provenance fails | Signal orphaned; never produced; gap reaches commit |
| priority | `essential` / `recommended` / `optional` only | — | Strategy unparseable as commit gate | Team commits without a defined stopping condition |

**Phase 4 exit gate:**
- [ ] All five field rows present; each has Immediate Failure + Downstream Effect populated

---

#### Phase 5 — Artifact Naming Convention

**Artifact Naming Convention**

Pattern: `{topic}-{signal}-{date}.md`
- `{topic}` — slug (lowercase, hyphenated)
- `{signal}` — skill name (e.g., `scout-feasibility`, `draft-spec`, `prove-hypothesis`)
- `{date}` — `YYYY-MM-DD`

Example: `payments-scout-feasibility-2026-03-14.md`

Non-conforming item names are treated as missing by `topic:score`, `topic:status`, and `topic:report`.

**Phase 5 exit gate:**
- [ ] Pattern written; at least one example provided

---

#### Phase 6 — COVERAGE SCHEMA

**COVERAGE SCHEMA**

| Constraint | Threshold | Immediate Failure | Downstream Effect |
|-----------|-----------|-------------------|-------------------|
| Essential signals | >= 1 | No commit gate | Investigation ends arbitrarily; commit is undefined |
| Namespaces represented | >= 2 | Single-axis coverage; schema violation | Signal categories invisible to topic narrative |
| Distinct S-N refs | >= 2 distinct S-N values | Single-stakeholder coverage | One risk perspective dominates; blindspots persist to commit |

**Phase 6 exit gate:**
- [ ] All three constraint rows present; each has Immediate Failure + Downstream Effect populated

---

#### Phase 7 — Signal Plan + Commit Gate

**Gate checklist — verify before writing any signal rows:**
- [ ] Phase 1 Stakeholders table: >= 3 rows, all columns filled
- [ ] At least 1 planned signal will be `essential`
- [ ] At least 2 distinct namespaces will appear
- [ ] At least 2 distinct S-N refs will appear in Stakeholder Ref column
- [ ] All priorities: `essential` / `recommended` / `optional` only
- [ ] All item names: `{topic}-{signal}-{date}.md` (see Artifact Naming Convention, Phase 5)
- [ ] Commit Gate will name each essential signal by item name

**Signal Plan:**

| Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
|-----------|-------|-----------|------------|-----------------|----------|

**Commit Gate**

Name every essential signal by item name. Design commit is blocked until all listed signals exist. Do not write "all essentials above" — name each one explicitly. A gate that cannot be pasted into a ticket is not a gate.

**Phase 7 exit gate:**
- [ ] Every signal row satisfies all FIELD SCHEMA fields
- [ ] All S-N refs resolve to Phase 1 rows
- [ ] COVERAGE SCHEMA thresholds met
- [ ] Commit Gate names each essential by item name

---

## V-02 — Conversational Register Fix

**Variation axis**: Phrasing register — conversational second-person throughout; fixes R6 V-02's C-18 failure (adds named COVERAGE SCHEMA table with consequence columns); adds per-step "before moving on" exit gates (C-21); Step 1 exit gate checklist with >= 3 rows (C-22)
**Hypothesis**: R6 V-02 scored 99.17 because it had no separate named COVERAGE SCHEMA table — coverage constraints lived only in the pre-write checklist. Adding a named COVERAGE SCHEMA table (Step 4b) fixes C-18. Making Step 1's condition an explicit checklist fixes C-22. Adding gate lines after each step fixes C-21. Register change has no effect on structural compliance — the structural elements carry all criteria regardless of surrounding prose.

---

### topic:new — Register a topic and plan its investigation

You're producing two things: a row in TOPICS.md and a strategy file. Work through these steps in order. Each step ends with a gate — check it before moving on.

---

#### Step 1 — Start with who's at risk

Your **first output** is a stakeholders table. Before you plan a single signal, fill this in:

| # | Who | What breaks immediately if this topic fails? | What persists downstream if we skip it entirely? |
|---|-----|---------------------------------------------|--------------------------------------------------|
| S-1 | | | |
| S-2 | | | |
| S-3 | | | |

Use specific role names — "PM", "backend engineer", "design lead" — not "user" or "team". The S-N numbers become your reference keys. You'll cite them in every signal row you write. An S-N you cite later that isn't in this table is a broken reference.

**Before moving to Step 2:**
- [ ] Table has >= 3 rows with all four columns filled
- [ ] Every role is specific, not generic

---

#### Step 2 — Register the topic

Add this row to `simulations/TOPICS.md`:

| Topic | Status | Strategy | Registered |
|-------|--------|----------|------------|
| {topic} | planning | simulations/{topic}/strategy.md | {date} |

**Before moving to Step 3:**
- [ ] Row written with status `planning` and path `simulations/{topic}/strategy.md`

---

#### Step 3 — Write a rationale

Create `simulations/{topic}/strategy.md`. Start with a Rationale section. At least 2 sentences: why does this topic need investigation, and what design decision does it inform?

**Before moving to Step 4:**
- [ ] Rationale section exists; >= 2 sentences; design decision named

---

#### Step 4 — Learn the field rules and coverage rules

**Field rules**

Each signal row has 6 fields. Here's what's valid and what breaks — immediately and downstream — if you use the wrong value.

**FIELD SCHEMA**

| Field | What's valid | Stakeholder Ref | If wrong immediately | What that causes downstream |
|-------|-------------|-----------------|---------------------|---------------------------|
| namespace | scout / draft / review / flow / trace / prove / listen / program / topic | — | Row can't be executed | That namespace never appears in the evidence base |
| skill | any valid skill in the namespace | — | Skill can't be invoked | That artifact category never gets produced |
| item name | `{topic}-{signal}-{date}.md` | — | Registry can't find it | Narrative references a file that doesn't exist |
| owner role | a role from your Step 1 table | Required — cite S-N | No one owns it; provenance fails | Signal never gets made; gap reaches commit |
| priority | `essential` or `recommended` or `optional` — nothing else | — | Strategy can't be parsed as a gate | Team doesn't know which signals must exist before commit |

On priority: "high", "medium", "low", "required" — none of these work. Anything other than the three canonical values makes the strategy inert as a commit gate.

On Stakeholder Ref: Counting distinct role names doesn't confirm different risks are covered. Citing 2 distinct S-N rows does. Use the column.

**Coverage rules**

These apply to the signal plan as a whole — not to individual rows.

**COVERAGE SCHEMA**

| Constraint | Threshold | If violated immediately | What that causes downstream |
|-----------|-----------|------------------------|---------------------------|
| Essential signals | >= 1 | No commit gate; strategy unparseable as gate | Investigation ends when momentum runs out, not when evidence floor is met |
| Namespaces represented | >= 2 | Single-axis coverage; schema violation | Entire signal categories absent from topic narrative |
| Distinct S-N refs cited | >= 2 distinct S-N values | Single-stakeholder coverage | One risk perspective dominates; blindspots persist to commit |

**Before moving to Step 5:**
- [ ] FIELD SCHEMA written; all 5 rows have both consequence columns populated
- [ ] COVERAGE SCHEMA written; all 3 rows have both consequence columns populated

---

#### Step 5 — Know the naming pattern

Every item name must follow this pattern:

```
{topic}-{signal}-{date}.md
```

- `{topic}` — topic slug, lowercase, hyphenated
- `{signal}` — skill name (e.g., `scout-feasibility`, `draft-spec`, `prove-hypothesis`)
- `{date}` — `YYYY-MM-DD`

Example: `payments-scout-feasibility-2026-03-14.md`

An item name that doesn't follow this convention can't be found by `topic:score` or `topic:status`. Downstream skills treat non-conforming names as missing artifacts.

**Before moving to Step 6:**
- [ ] Artifact Naming Convention section written; pattern documented; at least one example provided

---

#### Step 6 — Check these before writing any rows

- [ ] Step 1 table has >= 3 rows with all four columns filled
- [ ] At least 1 signal will be `essential`
- [ ] At least 2 different namespaces are in your plan
- [ ] At least 2 different S-N refs will appear in the Stakeholder Ref column
- [ ] Every priority is exactly: `essential` / `recommended` / `optional`
- [ ] Every item name follows: `{topic}-{signal}-{date}.md`
- [ ] Your commit gate (Step 7) will name specific item names

All boxes checked? Write the signal plan:

| Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
|-----------|-------|-----------|------------|-----------------|----------|

---

#### Step 7 — Name the commit gate

Add a Commit Gate section to your strategy file. List the item names of every `essential` signal. Don't say "see the essentials above" — name them. A gate you can't paste into a ticket isn't a gate.

**Step 7 done when:**
- [ ] Commit Gate section exists
- [ ] Every essential signal named by item name explicitly

---

## V-03 — Pipeline Overview Table

**Variation axis**: Output format — the prompt opens with a pipeline spec table (Phase / Produces / Exit Gate) before any phase content is shown; each phase is then expanded in full
**Hypothesis**: A pipeline overview table where every row has an Exit Gate column satisfies C-21 before the model reads a single phase. The structural overview makes per-phase gates architecturally visible at a glance — the model cannot claim to have missed them because the table enumerates all exit conditions in one place before execution begins. C-22 is satisfied by the Phase 1 row's ">= 3 rows, all cols filled" entry. Testing whether structural overview + phase expansion is reinforcing rather than redundant.

---

### Skill: topic:new

Register a new topic. Define its investigation strategy. Plan the signals that gate design commit.

**Outputs**: (1) row in `simulations/TOPICS.md` — (2) `simulations/{topic}/strategy.md`

---

#### Pipeline Overview

Each phase has a named exit gate. Do not advance to phase N+1 until phase N's exit gate is cleared.

| Phase | Produces | Exit Gate |
|-------|----------|-----------|
| 1. Stakeholders | Fill-in table (first output) | >= 3 rows; all 4 cols filled; roles specific; S-N refs assigned |
| 2. TOPICS.md | One appended row | Status = `planning`; path = `simulations/{topic}/strategy.md` |
| 3. Rationale | Prose section in strategy.md | >= 2 sentences; design decision named |
| 4. Schemas | FIELD SCHEMA + COVERAGE SCHEMA in strategy.md | All 5 field rows + all 3 coverage rows; each has Immediate Failure + Downstream Effect |
| 5. Artifact Naming | Named section in strategy.md | Pattern written; >= 1 concrete example |
| 6. Signal Plan + Commit Gate | Signal table + Commit Gate section | All FIELD + COVERAGE constraints met; Commit Gate names each essential by item name |

Each phase below expands the corresponding pipeline row.

---

#### Phase 1 — Stakeholders

**Produces**: Stakeholders fill-in table (first output of the skill)

Enumerate every role whose outcome depends on this topic. This table is the authority for the Stakeholder Ref column in Phase 4. Roles not present here are not valid signal owners.

| # | Stakeholder Role | Immediate Risk (topic fails) | Downstream Risk (topic skipped) |
|---|-----------------|------------------------------|----------------------------------|
| S-1 | | | |
| S-2 | | | |
| S-3 | | | |

A Stakeholder Ref citing an S-N absent from this table is a broken reference. A signal row with no Stakeholder Ref is unauditable. Both are FIELD SCHEMA violations.

**Phase 1 exit gate:**
- [ ] >= 3 rows, all four columns filled
- [ ] Roles are specific (not "user", not "team")

---

#### Phase 2 — TOPICS.md

**Produces**: One appended row

Append exactly one row to `simulations/TOPICS.md`:

| Topic | Status | Strategy Path | Registered |
|-------|--------|---------------|------------|
| {topic} | planning | simulations/{topic}/strategy.md | {date} |

**Phase 2 exit gate:**
- [ ] Row appended; status = `planning`; path = `simulations/{topic}/strategy.md`

---

#### Phase 3 — Rationale

**Produces**: Rationale section in `simulations/{topic}/strategy.md`

Create the strategy file. Write a Rationale section. Minimum 2 sentences: why this topic needs investigation, and what design decision it informs.

**Phase 3 exit gate:**
- [ ] >= 2 sentences written; design decision named

---

#### Phase 4 — Schemas

**Produces**: FIELD SCHEMA and COVERAGE SCHEMA sections in strategy.md

Write both schemas. Each constraint in both schemas carries two consequence tiers.

**FIELD SCHEMA**

| Field | Valid Values | Stakeholder Ref | Immediate Failure | Downstream Effect |
|-------|-------------|-----------------|-------------------|-------------------|
| namespace | scout / draft / review / flow / trace / prove / listen / program / topic | — | Row unroutable; no execution path | Namespace permanently absent from evidence base |
| skill | valid skill within the namespace | — | Not invokable; artifact not produced | Signal category missing from commit evaluation |
| item name | `{topic}-{signal}-{date}.md` — see Phase 5 | — | Unlocatable by topic registry | Narrative references a file the system cannot find |
| owner role | role present in Phase 1 Stakeholders table | Required — cite S-N | No accountable party; provenance fails | Signal never assigned; gap reaches design commit |
| priority | `essential` / `recommended` / `optional` only | — | Strategy unparseable as commit gate | Team proceeds without a defined stopping condition |

**COVERAGE SCHEMA**

| Constraint | Threshold | Immediate Failure | Downstream Effect |
|-----------|-----------|-------------------|-------------------|
| Essential signals | >= 1 | No commit gate | Investigation ends arbitrarily; commit is undefined |
| Namespaces represented | >= 2 | Single-axis coverage; schema violation | Entire signal categories invisible to topic narrative |
| Distinct Stakeholder Refs | >= 2 distinct S-N values | Single-stakeholder coverage | One risk perspective dominates; blindspots persist to production |

**Phase 4 exit gate:**
- [ ] FIELD SCHEMA: all five field rows present; Immediate Failure + Downstream Effect in every row
- [ ] COVERAGE SCHEMA: all three constraint rows present; Immediate Failure + Downstream Effect in every row

---

#### Phase 5 — Artifact Naming Convention

**Produces**: Artifact Naming Convention section in strategy.md

Write an Artifact Naming Convention section. All signal item names must conform to this pattern:

```
{topic}-{signal}-{date}.md
```

- `{topic}` — topic slug (lowercase, hyphenated)
- `{signal}` — skill name within the namespace (e.g., `scout-feasibility`, `draft-spec`, `prove-hypothesis`)
- `{date}` — `YYYY-MM-DD`

Example: `payments-scout-feasibility-2026-03-14.md`

A non-conforming item name is unlocatable by `topic:score`, `topic:status`, and `topic:report`. These skills treat a mis-named artifact the same as a missing one — both appear as gaps.

**Phase 5 exit gate:**
- [ ] Section written with pattern explicitly stated
- [ ] At least one concrete example provided

---

#### Phase 6 — Signal Plan + Commit Gate

**Produces**: Signal Plan table and Commit Gate section in strategy.md

Pre-write gate — verify all before writing any signal rows:

- [ ] Phase 1 Stakeholders table: >= 3 rows, all columns filled
- [ ] At least 1 planned signal will be `essential`
- [ ] At least 2 distinct namespaces will appear
- [ ] At least 2 distinct S-N refs will appear in Stakeholder Ref column
- [ ] All priorities: `essential` / `recommended` / `optional` only
- [ ] All item names: conform to Artifact Naming Convention (Phase 5)
- [ ] Commit Gate will name each essential signal by item name

**Signal Plan:**

| Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
|-----------|-------|-----------|------------|-----------------|----------|

**Commit Gate section**: Name every essential signal by item name. Design commit is blocked until all listed signals exist. Do not write "all essential signals" — name each one. A gate that cannot be pasted into a ticket is not a gate.

**Phase 6 exit gate:**
- [ ] Every signal row satisfies all FIELD SCHEMA fields
- [ ] All S-N refs resolve to Phase 1 rows
- [ ] COVERAGE SCHEMA thresholds are met
- [ ] Commit Gate names each essential by item name

---

## V-04 — Schema-Row-Cited Gates

**Variation axis**: Role sequence + lifecycle — each phase exit gate cites schema rows by identifier (F-01 through F-05 for FIELD SCHEMA; COV-01 through COV-03 for COVERAGE SCHEMA) rather than restating constraints inline
**Hypothesis**: Gate items that reference schema rows by ID create a tighter mechanical coupling between constraint definition and enforcement checkpoint. A gate item reading "F-05: all priority values are exactly `essential / recommended / optional`" traces back to a specific schema row rather than restating a free-form rule. This makes gates harder to satisfy trivially (the model must reference the schema) and shorter per item. C-21 via a gate at every phase boundary. C-22 via "S-TABLE: >= 3 rows" as a named Phase 1 gate item — enforced as a structural condition before Phase 2 can begin.

---

### Skill: topic:new

**Inputs**: topic name
**Outputs**: TOPICS.md row + `simulations/{topic}/strategy.md`

---

#### Phase 1 — Stakeholders

Produce the Stakeholders fill-in table as your first output. Every signal row in Phase 6 will cite a row in this table by its S-N identifier.

| # | Stakeholder Role | Immediate Risk (topic fails) | Downstream Risk (topic skipped) |
|---|-----------------|------------------------------|----------------------------------|
| S-1 | | | |
| S-2 | | | |
| S-3 | | | |

Roles must be specific. A Stakeholder Ref in the signal plan that cites an S-N not present here is a broken reference. A signal row without a Stakeholder Ref is unauditable.

**Phase 1 exit gate:**
- [ ] S-TABLE: >= 3 rows, all four columns filled, roles specific

---

#### Phase 2 — TOPICS.md Registration

Append one row to `simulations/TOPICS.md`:

| Topic | Status | Strategy Path | Registered |
|-------|--------|---------------|------------|
| {topic} | planning | simulations/{topic}/strategy.md | {date} |

**Phase 2 exit gate:**
- [ ] TOPICS-ROW: status = `planning`; path = `simulations/{topic}/strategy.md`

---

#### Phase 3 — Rationale

Create `simulations/{topic}/strategy.md`. Write a Rationale section.

**Phase 3 exit gate:**
- [ ] RATIONALE: >= 2 sentences; design decision named

---

#### Phase 4 — Schemas

Write FIELD SCHEMA and COVERAGE SCHEMA in strategy.md. Assign row IDs as shown.

**FIELD SCHEMA**

| Row | Field | Valid Values | Stakeholder Ref | Immediate Failure | Downstream Effect |
|-----|-------|-------------|-----------------|-------------------|-------------------|
| F-01 | namespace | scout / draft / review / flow / trace / prove / listen / program / topic | — | Row unroutable; no execution path | Namespace permanently absent from evidence base |
| F-02 | skill | valid skill within the namespace | — | Not invokable; artifact not produced | Signal category absent from commit evaluation |
| F-03 | item name | `{topic}-{signal}-{date}.md` — see Phase 5 | — | Unlocatable by topic registry | Narrative references a file that does not exist |
| F-04 | owner role | role present in Phase 1 Stakeholders table | Required — cite S-N | No accountable party; provenance fails | Signal never assigned; gap reaches design commit |
| F-05 | priority | `essential` / `recommended` / `optional` only | — | Strategy unparseable as commit gate | Team commits without a defined stopping condition |

**COVERAGE SCHEMA**

| Row | Constraint | Threshold | Immediate Failure | Downstream Effect |
|-----|-----------|-----------|-------------------|-------------------|
| COV-01 | Essential signals | >= 1 | No commit gate; investigation cannot formally close | Commit happens when momentum ends, not when evidence floor is met |
| COV-02 | Namespaces represented | >= 2 | Single-axis coverage; schema violation | Entire signal categories invisible to topic narrative |
| COV-03 | Distinct Stakeholder Refs | >= 2 distinct S-N values | Single-stakeholder coverage | One risk perspective dominates; blindspots persist to production |

**Phase 4 exit gate:**
- [ ] F-01 through F-05: all five rows present, each with Immediate Failure + Downstream Effect
- [ ] COV-01 through COV-03: all three rows present, each with Immediate Failure + Downstream Effect
- [ ] F-04 Stakeholder Ref column labeled "Required — cite S-N"

---

#### Phase 5 — Artifact Naming Convention

Write an Artifact Naming Convention section in strategy.md.

```
{topic}-{signal}-{date}.md
```

- `{topic}` — slug (lowercase, hyphenated)
- `{signal}` — skill name (e.g., `scout-feasibility`, `draft-spec`)
- `{date}` — `YYYY-MM-DD`

Example: `payments-scout-feasibility-2026-03-14.md`

Non-conforming names are treated as missing by all downstream topic skills.

**Phase 5 exit gate:**
- [ ] ART-NAMING: section exists; pattern written; >= 1 example

---

#### Phase 6 — Signal Plan + Commit Gate

**Pre-write gate — cite schema rows:**
- [ ] S-TABLE: >= 3 rows filled (Phase 1)
- [ ] F-01: all namespace values from valid list
- [ ] F-03: all item names match `{topic}-{signal}-{date}.md` (Phase 5)
- [ ] F-04: every owner role cites a valid S-N from Phase 1
- [ ] F-05: all priorities are exactly `essential` / `recommended` / `optional`
- [ ] COV-01: >= 1 signal will be `essential`
- [ ] COV-02: >= 2 distinct namespaces will appear
- [ ] COV-03: >= 2 distinct S-N refs will appear

**Signal Plan:**

| Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
|-----------|-------|-----------|------------|-----------------|----------|

**Commit Gate**

Name every essential signal (F-05 = `essential`) by item name. Design commit is blocked until all listed signals exist. Name each explicitly — do not reference the table.

**Phase 6 exit gate:**
- [ ] Every row satisfies F-01 through F-05
- [ ] All S-N refs resolve to Phase 1 rows
- [ ] COV-01 through COV-03 thresholds met
- [ ] Commit Gate names each essential by item name

---

## V-05 — Inertia Framing + Per-Phase Gates

**Variation axis**: Inertia framing + lifecycle emphasis — every phase opens with an inertia statement (the ambient failure state before this phase runs) and closes with an explicit exit gate checklist; Phase 1 gate includes >= 3 rows
**Hypothesis**: R6 V-05 failed C-21 (gate only in Phase 7) and likely C-22 (Phase 1 "Minimum 3 rows" as prose). Adding exit gates at every phase boundary while preserving the inertia openers produces the highest comprehension-enforcement product: the inertia opener explains *why* the phase matters (motivational layer); the structure enforces *what* to produce; the exit gate prevents advancing without it. The two layers are not redundant — inertia builds semantic weight; the gate enforces production.

---

### Skill: topic:new

Without this skill, teams commit to feature designs based on whatever signals happen to exist: prior experience, hallway discussions, one PM's instinct. Work advances because momentum is present, not because evidence is sufficient. This skill makes the gap between "what we know" and "what we need to know" visible before commit.

**Two outputs**: (1) a row in `simulations/TOPICS.md`, (2) `simulations/{topic}/strategy.md`

---

#### Phase 1 — Stakeholders

Without a stakeholders table, signal planning defaults to whoever is loudest in the planning session. Roles that would have flagged a design risk never surface. Their concerns don't disappear — they reappear as post-ship bugs, support escalations, and adoption failures.

Write this table as your **first output**:

| # | Stakeholder Role | Immediate Risk (commit without evidence) | Downstream Risk (shipped without insight) |
|---|-----------------|------------------------------------------|-------------------------------------------|
| S-1 | | | |
| S-2 | | | |
| S-3 | | | |

Specific roles only — "PM", "backend engineer", "security reviewer", not "user" or "team". The S-N keys are your accountability identifiers. Every signal row in Phase 6 cites one. An uncited row is unauditable. A citation that doesn't resolve to a row here is a broken reference.

**Phase 1 exit gate:**
- [ ] >= 3 rows, all four columns filled
- [ ] Roles are specific and named, not generic categories

---

#### Phase 2 — TOPICS.md Registration

Without registration, the topic has no canonical path. Skills that look for signals by topic — `topic:score`, `topic:status`, `topic:report` — cannot locate the strategy file. The topic becomes invisible to the investigation pipeline before investigation begins.

Append one row to `simulations/TOPICS.md`:

| Topic | Status | Strategy Path | Registered |
|-------|--------|---------------|------------|
| {topic} | planning | simulations/{topic}/strategy.md | {date} |

**Phase 2 exit gate:**
- [ ] Row appended; status = `planning`; path = `simulations/{topic}/strategy.md`

---

#### Phase 3 — Rationale

Without a rationale, the strategy is a list of tasks with no stated purpose. When coverage gaps emerge mid-investigation, there is no anchor for deciding whether a gap matters. The design decision the investigation informs stays implicit — and implicit decisions are never challenged.

Write a Rationale section in `simulations/{topic}/strategy.md`. Minimum 2 sentences: why investigation is needed, and what design decision it informs.

**Phase 3 exit gate:**
- [ ] Rationale section exists; >= 2 sentences; design decision named

---

#### Phase 4 — FIELD SCHEMA

Without a field schema, signal rows accumulate however the model sees fit. Priority vocabulary drifts to "high/medium/low". Owner roles cluster to the team lead. Namespaces repeat. The resulting plan looks like a strategy but cannot function as one — there is no mechanical way to parse it as a commit gate.

Every signal row must satisfy this schema. Each constraint carries two consequence tiers.

**FIELD SCHEMA**

| Field | Valid Values | Stakeholder Ref | Immediate Failure | Downstream Effect |
|-------|-------------|-----------------|-------------------|-------------------|
| namespace | scout / draft / review / flow / trace / prove / listen / program / topic | — | Row unroutable; no execution path | Namespace permanently absent from evidence base |
| skill | valid skill within the namespace | — | Not invokable; artifact not produced | Signal category missing from all commit evaluations |
| item name | `{topic}-{signal}-{date}.md` — see Phase 5 | — | Unlocatable by topic registry | Narrative references a file the system cannot find |
| owner role | role present in Phase 1 Stakeholders table | Required — cite S-N | No accountable party; provenance fails | Signal never assigned; gap reaches design commit |
| priority | `essential` / `recommended` / `optional` only | — | Strategy unparseable as commit gate | Team commits without a stopping condition |

**Phase 4 exit gate:**
- [ ] FIELD SCHEMA written; all five rows present; Immediate Failure + Downstream Effect in every row

---

#### Phase 5 — Artifact Naming Convention

Without a documented naming convention, item names in the signal plan will vary in format. Some will be parseable. Some won't. Downstream skills cannot distinguish a missing artifact from a mis-named one — both appear as gaps. The investigation looks incomplete even when the work was done.

**Artifact Naming Convention**

All item names must follow:

```
{topic}-{signal}-{date}.md
```

- `{topic}` — topic slug (lowercase, hyphenated)
- `{signal}` — skill name (e.g., `scout-feasibility`, `draft-spec`, `prove-hypothesis`)
- `{date}` — `YYYY-MM-DD`

Example: `payments-scout-feasibility-2026-03-14.md`

Deviate from this pattern and the artifact is invisible to every downstream topic skill.

**Phase 5 exit gate:**
- [ ] Section exists; pattern explicitly written; >= 1 concrete example

---

#### Phase 6 — COVERAGE SCHEMA

Without coverage thresholds, a strategy can satisfy every field requirement with a single `essential` signal in one namespace owned by one person. It is technically valid and strategically blind — exactly one signal category investigated, exactly one stakeholder's risk addressed, exactly one discipline's concerns visible.

**COVERAGE SCHEMA**

| Constraint | Threshold | Immediate Failure | Downstream Effect |
|-----------|-----------|-------------------|-------------------|
| Essential signals | >= 1 | No commit gate; investigation cannot formally close | Team commits when momentum runs out, not when evidence floor is met |
| Namespaces represented | >= 2 | Single-axis coverage; schema violation | Entire signal categories — trace, flow, prove, listen — never investigated |
| Distinct Stakeholder Refs | >= 2 distinct S-N values | Single-stakeholder coverage | One risk perspective dominates; other roles' concerns persist undetected to production |

**Phase 6 exit gate:**
- [ ] COVERAGE SCHEMA written; all three rows present; Immediate Failure + Downstream Effect in every row

---

#### Phase 7 — Signal Plan

Without a pre-write gate, the model writes signal rows and discovers coverage problems after the fact — if at all. The gate forces verification before commitment. Errors found here cost one revision. Errors found at commit cost a retrospective.

**Pre-write gate:**
- [ ] Phase 1 Stakeholders table: >= 3 rows, all columns filled
- [ ] At least 1 planned signal will be `essential`
- [ ] At least 2 distinct namespaces will appear
- [ ] At least 2 distinct S-N refs will appear in the Stakeholder Ref column
- [ ] All priorities: `essential` / `recommended` / `optional` only
- [ ] All item names: conform to Artifact Naming Convention (Phase 5)
- [ ] Commit Gate (Phase 8) will name specific item names

| Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
|-----------|-------|-----------|------------|-----------------|----------|

**Phase 7 exit gate:**
- [ ] Every signal row satisfies all FIELD SCHEMA fields
- [ ] All S-N refs resolve to Phase 1 rows
- [ ] COVERAGE SCHEMA thresholds are met

---

#### Phase 8 — Commit Gate

Without a named commit gate, "done" means "ran out of time" or "the PM said ship it." The team cannot point to a specific signal set and say: this is the evidence floor we agreed to. The investigation is retroactively complete as soon as anyone declares it so.

Name the essential signals by item name. Design commit is blocked until every listed signal exists. Do not write "all essential signals above" — name each one. A gate that cannot be copied into a ticket is not a gate.

**Phase 8 exit gate:**
- [ ] Commit Gate section exists in strategy.md
- [ ] Every essential signal named by item name explicitly

---

## Variation Summary

| # | Axis | C-21 mechanism | C-22 mechanism | Structural bet |
|---|------|---------------|----------------|----------------|
| V-01 | Compact gate injection | Two-item checklist after every phase | Phase 1 checklist: ">= 3 rows, all four columns filled" | Minimum viable gate form; tests whether a checklist after each section satisfies C-21 without adding prose overhead |
| V-02 | Conversational register fix | "Before moving on" checklist at every step | Step 1 checklist: ">= 3 rows with all four columns filled" | Register change is safe; C-18 fix (named COVERAGE SCHEMA) + per-step gates brings V-02 to 100 |
| V-03 | Pipeline overview table | Pipeline table carries Exit Gate column for every phase row | Phase 1 pipeline row: ">= 3 rows; all 4 cols filled; specific roles" | Structural overview makes all exit gates visible before any phase runs; C-21 satisfied architecturally |
| V-04 | Schema-row-cited gates | Gate items cite F-N / COV-N row IDs at every phase | Phase 1 gate: "S-TABLE: >= 3 rows" | Schema-ID coupling makes gates compact and mechanically traceable; harder to satisfy by rote checklist-ticking |
| V-05 | Inertia framing + per-phase gates | Exit gate checklist after every phase | Phase 1 exit gate: ">= 3 rows, all four columns filled, roles specific" | Inertia opener (why this phase) + exit gate (what must be produced) = maximum comprehension-enforcement product |
