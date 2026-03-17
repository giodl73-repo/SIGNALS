**R6 variations written** to `simulations/quest/variations/topic-new-variations-R6-2026-03-14.md`.

---

## Summary

**R5 diagnosis carried forward**: All four complete variations from R5 scored 99.17. Single persistent gap: **C-13 fails for C-10** — artifact naming existed only as a FIELD SCHEMA row, not as a dedicated named section heading. R5 V-03 was never written.

**R6 design**: All five variations fix C-13 by adding a named `Artifact Naming Convention` section. The axes vary *how* that fix is expressed:

| # | Axis | Key bet |
|---|------|---------|
| V-01 | Minimal C-13 fix | One named section grafted onto R5 V-01; everything else unchanged. Tests whether C-13 is isolated. |
| V-02 | Phrasing register | Complete the R5 V-03 that was never written. Conversational second-person with identical structural machinery. |
| V-03 | Lifecycle emphasis | Six numbered phases with entry/exit gates. Naming convention is its own phase with a gate checklist. |
| V-04 | C-13 + schema compression | Section compressed to two lines (heading + pattern + example). Tests whether heading alone satisfies C-13 regardless of body length. |
| V-05 | C-13 + inertia framing + lifecycle | Every phase opens with "without this step, teams do X and Y breaks." Consequence columns feel earned. |

The expected composite for V-01 is **100** — all 12 aspirational criteria now satisfied: C-13 gains its dedicated ARTIFACT NAMING section, C-20 temporal layering and C-19 Stakeholder Ref column are preserved from R5.
holder Role | Immediate Risk if Topic Fails | Downstream Risk if Topic is Skipped |
|---|-----------------|-------------------------------|-------------------------------------|
| S-1 | | | |
| S-2 | | | |
| S-3 | | | |

Minimum 3 rows. Roles must be specific (not "user", not "team"). The Stakeholder Ref column in FIELD SCHEMA cites these row numbers by `S-N`. A signal row with no Stakeholder Ref is unauditable. A signal row that cites an `S-N` not present in this table is a broken reference. Both are FIELD SCHEMA violations.

---

#### Phase 2 — TOPICS.md

Append one row to `simulations/TOPICS.md`:

| Topic | Status | Strategy Path | Registered |
|-------|--------|---------------|------------|
| {topic} | planning | simulations/{topic}/strategy.md | {date} |

---

#### Phase 3 — strategy.md

Create `simulations/{topic}/strategy.md` with sections in this order.

##### 3.1 Rationale

Two or more sentences: why this topic needs investigation and what design decision it informs.

##### 3.2 FIELD SCHEMA

Every signal row must satisfy all fields. Each constraint carries two consequence tiers.

| Field | Valid Values | Stakeholder Ref | Immediate Failure | Downstream Effect |
|-------|-------------|-----------------|-------------------|-------------------|
| namespace | scout / draft / review / flow / trace / prove / listen / program / topic | — | Row unroutable; no skill can execute it | Namespace gap — signal category absent from evidence base permanently |
| skill | valid skill in the namespace | — | Skill not invokable; artifact never produced | Signal category silently excluded from commit evaluation |
| item name | `{topic}-{signal}-{date}.md` — see Artifact Naming Convention below | — | Artifact unlocatable by topic registry | Narrative references a file that does not exist |
| owner role | named role present in Stakeholders table | Required — cite S-N | No accountable party; provenance review fails | Signal is never assigned, never produced; gap persists to design commit |
| priority | `essential` / `recommended` / `optional` only | — | Strategy unparseable as a commit gate | Team proceeds to commit with no defined stopping condition |

The **Stakeholder Ref column** is what makes C-08 verifiable by structural inspection. Counting distinct values in the Owner Role column does not confirm that each role covers a different risk exposure. Citing distinct S-N rows does.

##### 3.3 Artifact Naming Convention

All signal item names follow exactly this pattern:

```
{topic}-{signal}-{date}.md
```

- `{topic}` — the topic slug (lowercase, hyphenated, no spaces)
- `{signal}` — the skill name within the namespace (e.g., `scout-feasibility`, `draft-spec`, `prove-hypothesis`)
- `{date}` — date of registration in `YYYY-MM-DD` format

Example: `payments-scout-feasibility-2026-03-14.md`

A name that does not follow this convention is unlocatable by `topic:score`, `topic:status`, and `topic:report`. The downstream skill chain depends on this pattern to resolve artifacts to their topics. Non-conforming names are treated as missing.

##### 3.4 COVERAGE SCHEMA

| Constraint | Threshold | Immediate Failure | Downstream Effect |
|-----------|-----------|-------------------|-------------------|
| Essential signals | ≥ 1 | No commit gate exists | Investigation ends arbitrarily; commit is undefined |
| Namespaces represented | ≥ 2 | Single-axis coverage; schema violation | Entire signal categories invisible to topic narrative |
| Distinct Stakeholder Refs | ≥ 2 distinct S-N values | Single-stakeholder coverage | One risk perspective dominates; blindspots persist through design |

##### 3.5 Signal Plan

Pre-write gate — verify before writing any rows:

- [ ] Stakeholders table (Phase 1) has ≥ 3 rows with all columns filled
- [ ] At least 1 planned signal will be marked `essential`
- [ ] At least 2 distinct namespaces will appear
- [ ] At least 2 distinct S-N refs will appear in the Stakeholder Ref column
- [ ] All priorities will be: `essential` / `recommended` / `optional` only
- [ ] All item names will follow `{topic}-{signal}-{date}.md` (Artifact Naming Convention above)

| Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
|-----------|-------|-----------|------------|-----------------|----------|

##### 3.6 Commit Gate

List the item names of all essential signals. Design commit is blocked until every listed signal exists. Do not write "all essentials" — name each one. A gate that cannot be pasted into a ticket is not a gate.

---

## V-02 — Conversational Imperative Register (Complete)

**Variation axis**: Phrasing register — second-person imperative ("your first output", "do not proceed", "name each one") throughout; all structural mechanisms (tables, consequence columns, checkbox gate, named sections) preserved identically; C-13 fix embedded as a named step
**Hypothesis**: R5 V-03 attempted this axis but was never written. A full conversational version with all structural machinery intact will reach 100. Register change does not affect structural compliance — the structural elements carry all criteria regardless of the prose between them.

---

### topic:new — Register a topic and plan its investigation

You're producing two things: a row in TOPICS.md and a strategy file. Work through these steps in order. Each step tells you what to produce and when to stop.

---

#### Step 1 — Start with who's at risk

Your **first output** is a stakeholders table. Before you plan a single signal, write this:

| # | Who | What breaks immediately if this topic fails? | What persists downstream if we skip it entirely? |
|---|-----|---------------------------------------------|--------------------------------------------------|
| S-1 | | | |
| S-2 | | | |
| S-3 | | | |

Fill in at least 3 rows. Use specific role names — "PM", "backend engineer", "design lead", not "user" or "team". Once you write this table, the S-N numbers become your reference keys. You'll cite them in every signal row you write.

Do not move to Step 2 until this table has ≥ 3 rows with all four columns filled.

---

#### Step 2 — Register the topic

Add this row to `simulations/TOPICS.md`:

| Topic | Status | Strategy | Registered |
|-------|--------|----------|------------|
| {topic} | planning | simulations/{topic}/strategy.md | {date} |

---

#### Step 3 — Write a rationale

Create `simulations/{topic}/strategy.md`. Start with a Rationale section. Write at least 2 sentences: why does this topic need investigation, and what design decision does it inform?

---

#### Step 4 — Learn the field rules before you plan

Each signal row has 6 fields. Here's what's valid in each one, and what breaks — immediately and downstream — if you use the wrong value:

| Field | What's valid | Stakeholder Ref | If you get it wrong immediately | What that causes downstream |
|-------|-------------|-----------------|--------------------------------|----------------------------|
| namespace | scout / draft / review / flow / trace / prove / listen / program / topic | — | Row can't be executed | That namespace's signals never appear in the evidence base |
| skill | any valid skill in the namespace | — | Skill can't be invoked | That artifact category never gets produced |
| item name | `{topic}-{signal}-{date}.md` | — | Registry can't find it | Narrative references a file that doesn't exist |
| owner role | a role from your Step 1 table | Required — cite S-N | No one owns it; provenance fails | Signal never gets made; gap reaches commit |
| stakeholder ref | the S-N from Step 1 | — | Traceability is broken | Role coverage can't be audited by inspection |
| priority | `essential` or `recommended` or `optional` — nothing else | — | Strategy can't be parsed as a gate | Team doesn't know which signals are required to commit |

Two things worth stating directly:

**On priority**: This is the failure mode most worth being explicit about. "High", "medium", "low", "required" — none of these work. The tool that reads the strategy expects exactly `essential`, `recommended`, or `optional`. Anything else makes the strategy inert as a commit gate.

**On stakeholder ref**: Counting distinct owner role names doesn't tell you whether those roles cover different risks. Citing 2 distinct S-N rows does. Use the ref column.

---

#### Step 5 — Know the naming pattern before you write item names

Every item name must follow this pattern:

```
{topic}-{signal}-{date}.md
```

- `{topic}` — topic slug, lowercase, hyphenated
- `{signal}` — skill name (e.g., `scout-feasibility`, `draft-spec`, `prove-hypothesis`)
- `{date}` — `YYYY-MM-DD`

Example: `payments-scout-feasibility-2026-03-14.md`

An item name that doesn't follow this convention can't be found by `topic:score` or `topic:status`. Downstream skills treat non-conforming names as missing artifacts.

---

#### Step 6 — Check these before you write any rows

- [ ] Your Step 1 table has ≥ 3 rows with all four columns filled
- [ ] At least 1 signal will be `essential`
- [ ] At least 2 different namespaces are in your plan
- [ ] At least 2 different S-N refs appear in the Stakeholder Ref column
- [ ] Every priority is exactly: `essential` / `recommended` / `optional`
- [ ] Every item name follows: `{topic}-{signal}-{date}.md`
- [ ] Your commit gate (Step 7) will name specific item names

All boxes checked? Now write the signal plan:

| Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
|-----------|-------|-----------|------------|-----------------|----------|

---

#### Step 7 — Name the commit gate

Add a Commit Gate section to your strategy file. List the item names of every `essential` signal. The team needs these before design commit. Don't say "see the essentials above" — name them. A gate you can't paste into a ticket isn't a gate.

---

## V-03 — Lifecycle Emphasis (Explicit Phase Gates with Entry/Exit Conditions)

**Variation axis**: Lifecycle emphasis — numbered phases with explicit entry conditions, what-to-produce labels, and exit gate checklists at every phase boundary; C-13 fix is its own named phase
**Hypothesis**: Per-phase gate checklists with entry and exit conditions eliminate silent criterion omissions at phase transitions. When the model must declare what it produced and verify it before advancing, the C-13 ARTIFACT NAMING phase cannot be skipped because it has an entry condition and a named exit gate.

---

### Skill: topic:new

Register a new topic. Define its investigation strategy. Plan the signals that gate design commit.

**Output 1**: row in `simulations/TOPICS.md`
**Output 2**: `simulations/{topic}/strategy.md`

This skill runs in six phases. Each phase has an entry condition, a declared output, and an exit gate. Do not enter a phase until the previous exit gate is cleared.

---

#### Phase 1 — Stakeholder Enumeration

**Entry condition**: Topic name is known.
**Output**: Stakeholders table.
**Exit gate**: ≥ 3 rows, all columns filled, roles specific.

Produce the Stakeholders table as your first output. Enumerate every role whose outcome depends on this topic.

| # | Stakeholder Role | Immediate Risk (topic fails) | Downstream Risk (topic skipped) |
|---|-----------------|------------------------------|----------------------------------|
| S-1 | | | |
| S-2 | | | |
| S-3 | | | |

This table is the authority for the Stakeholder Ref column in Phase 4. Roles not present here are not valid signal owners. A Stakeholder Ref that cites an S-N absent from this table is a broken reference and invalidates the signal row.

**Phase 1 exit gate**:
- [ ] ≥ 3 stakeholder rows, all four columns filled
- [ ] Roles are specific (not "user", not "team")

---

#### Phase 2 — TOPICS.md Registration

**Entry condition**: Phase 1 exit gate cleared.
**Output**: One appended row in `simulations/TOPICS.md`.
**Exit gate**: Row written with correct status and strategy path.

Append one row to `simulations/TOPICS.md`:

| Topic | Status | Strategy Path | Registered |
|-------|--------|---------------|------------|
| {topic} | planning | simulations/{topic}/strategy.md | {date} |

**Phase 2 exit gate**:
- [ ] Row appended (not replaced) to TOPICS.md
- [ ] Status is exactly `planning`
- [ ] Strategy path is exactly `simulations/{topic}/strategy.md`

---

#### Phase 3 — Rationale

**Entry condition**: Phase 2 exit gate cleared.
**Output**: Rationale section in `simulations/{topic}/strategy.md`.
**Exit gate**: ≥ 2 sentences written; decision context named.

Create `simulations/{topic}/strategy.md`. Write a Rationale section. Minimum 2 sentences: why this topic needs investigation, and what design decision it informs.

**Phase 3 exit gate**:
- [ ] Rationale section exists in strategy.md
- [ ] ≥ 2 sentences
- [ ] At least one sentence names the design decision the investigation informs

---

#### Phase 4 — Schema Definition

**Entry condition**: Phase 3 exit gate cleared.
**Output**: FIELD SCHEMA and COVERAGE SCHEMA sections in strategy.md.
**Exit gate**: Both schemas written with Immediate Failure and Downstream Effect columns.

##### FIELD SCHEMA

| Field | Valid Values | Stakeholder Ref | Immediate Failure | Downstream Effect |
|-------|-------------|-----------------|-------------------|-------------------|
| namespace | scout / draft / review / flow / trace / prove / listen / program / topic | — | Row unroutable; no execution path exists | Namespace gap — category permanently absent from evidence base |
| skill | valid skill within the namespace | — | Skill not invokable; artifact never produced | Signal category silently missing from commit evaluation |
| item name | `{topic}-{signal}-{date}.md` — see Phase 5 | — | Unlocatable by topic registry | Narrative references a file that does not exist |
| owner role | role present in Phase 1 Stakeholders table | Required — cite S-N | No accountable party; provenance review fails | Signal never assigned; gap reaches commit |
| priority | `essential` / `recommended` / `optional` only | — | Strategy unparseable as commit gate | Team proceeds to commit with no stopping condition |

##### COVERAGE SCHEMA

| Constraint | Threshold | Immediate Failure | Downstream Effect |
|-----------|-----------|-------------------|-------------------|
| Essential signals | ≥ 1 | No commit gate exists | Investigation ends arbitrarily |
| Namespaces represented | ≥ 2 | Single-axis coverage; schema violation | Entire categories invisible to topic narrative |
| Distinct Stakeholder Refs | ≥ 2 distinct S-N values | Single-stakeholder coverage | One risk perspective dominates; blindspots persist to production |

**Phase 4 exit gate**:
- [ ] FIELD SCHEMA includes all five field rows
- [ ] Each FIELD SCHEMA row has Immediate Failure and Downstream Effect columns populated
- [ ] COVERAGE SCHEMA has all three constraint rows
- [ ] Each COVERAGE SCHEMA row has Immediate Failure and Downstream Effect columns populated

---

#### Phase 5 — Artifact Naming Convention

**Entry condition**: Phase 4 exit gate cleared.
**Output**: Artifact Naming Convention section in strategy.md.
**Exit gate**: Pattern documented with example.

Write an Artifact Naming Convention section in strategy.md. All signal item names must conform to this pattern:

```
{topic}-{signal}-{date}.md
```

- `{topic}` — topic slug (lowercase, hyphenated)
- `{signal}` — skill name within the namespace (e.g., `scout-feasibility`, `draft-spec`)
- `{date}` — `YYYY-MM-DD`

Example: `payments-scout-feasibility-2026-03-14.md`

A non-conforming item name is unlocatable by `topic:score`, `topic:status`, and `topic:report`. These skills cannot distinguish a missing artifact from a mis-named one — both appear as gaps.

**Phase 5 exit gate**:
- [ ] Artifact Naming Convention section exists in strategy.md
- [ ] Pattern written explicitly
- [ ] At least one concrete example provided

---

#### Phase 6 — Signal Plan and Commit Gate

**Entry condition**: Phase 5 exit gate cleared.
**Output**: Signal Plan table and Commit Gate section in strategy.md.
**Exit gate**: All FIELD SCHEMA and COVERAGE SCHEMA constraints satisfied; commit gate names specific items.

Pre-write gate — verify before writing any signal rows:

- [ ] Phase 1 Stakeholders table: ≥ 3 rows, all columns filled
- [ ] At least 1 planned signal will be `essential`
- [ ] At least 2 distinct namespaces will appear
- [ ] At least 2 distinct S-N refs will appear in the Stakeholder Ref column
- [ ] All priority values will be: `essential` / `recommended` / `optional` only
- [ ] All item names will follow the Artifact Naming Convention from Phase 5

| Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
|-----------|-------|-----------|------------|-----------------|----------|

**Commit Gate section**: List the item names of all essential signals. Design commit is blocked until every listed signal exists. Name each signal explicitly — do not reference the table.

**Phase 6 exit gate**:
- [ ] Every signal row satisfies all FIELD SCHEMA fields
- [ ] All Stakeholder Ref values cite S-N rows from Phase 1
- [ ] COVERAGE SCHEMA thresholds are met
- [ ] Commit Gate section names each essential signal by item name

---

## V-04 — C-13 Fix + Schema Compression (Minimal Surface Area)

**Variation axes**: C-13 compliance + output format (schema compression)
**Hypothesis**: R5 V-02 proved prose compression is safe — pure schema enforcement without scaffolding narrative satisfies all criteria. The C-13 fix can be compressed to a named section with a single pattern line and one example, without becoming a prose section. Tests whether the named section heading alone satisfies C-13 regardless of section body length.

---

### Skill: topic:new

**Inputs**: topic name
**Outputs**: TOPICS.md row + `simulations/{topic}/strategy.md`

---

#### Output 1 — TOPICS.md

Append exactly one row:

| Topic | Status | Strategy | Registered |
|-------|--------|----------|------------|
| {topic} | planning | simulations/{topic}/strategy.md | {date} |

---

#### Output 2 — strategy.md

Path: `simulations/{topic}/strategy.md`

---

**STAKEHOLDERS** (fill as first step)

| # | Role | Immediate Risk | Downstream Risk |
|---|------|----------------|-----------------|
| S-1 | | | |
| S-2 | | | |
| S-3 | | | |

Minimum 3 rows. FIELD SCHEMA's Stakeholder Ref column cites these by `S-N`. Citations to unlisted rows are broken references. Rows with no citation are unauditable.

---

**RATIONALE** (required, 2+ sentences)

Why this topic. What decision it informs.

---

**FIELD SCHEMA**

| Field | Valid Values | Stakeholder Ref | Immediate Failure | Downstream Effect |
|-------|-------------|-----------------|-------------------|-------------------|
| namespace | scout / draft / review / flow / trace / prove / listen / program / topic | — | Unroutable | Namespace gap in evidence base |
| skill | valid skill in namespace | — | Not invokable | Artifact category missing |
| item name | `{topic}-{signal}-{date}.md` | — | Unlocatable by registry | Narrative references nonexistent file |
| owner role | role from Stakeholders table | Required: cite S-N | No accountable party | Signal orphaned; never produced |
| priority | `essential` / `recommended` / `optional` | — | Strategy unparseable | No commit gate; investigation never closes |

---

**ARTIFACT NAMING CONVENTION**

Pattern: `{topic}-{signal}-{date}.md` — Example: `payments-scout-feasibility-2026-03-14.md`

Non-conforming names are treated as missing by all downstream topic skills.

---

**COVERAGE SCHEMA**

| Constraint | Threshold | Immediate Failure | Downstream Effect |
|-----------|-----------|-------------------|-------------------|
| Essential signals | ≥ 1 | No gate | Investigation ends arbitrarily |
| Namespaces | ≥ 2 | Single-axis | Categories missing from evidence |
| Distinct S-N refs | ≥ 2 | Single-stakeholder | Blindspots persist to commit |

---

**GATE CHECKLIST** (verify before writing signal plan)

- [ ] Stakeholders table: ≥ 3 rows, all columns filled
- [ ] ≥ 1 signal will be `essential`
- [ ] ≥ 2 namespaces will be represented
- [ ] ≥ 2 distinct S-N refs will appear
- [ ] All priorities: `essential` / `recommended` / `optional`
- [ ] All item names: `{topic}-{signal}-{date}.md` (see Artifact Naming Convention above)
- [ ] Commit gate will name specific items

---

**SIGNAL PLAN**

| Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
|-----------|-------|-----------|------------|-----------------|----------|

---

**COMMIT GATE**

Name the essential signals by item name. These must exist before design commit. Name each one explicitly.

---

## V-05 — C-13 Fix + Inertia Framing + Lifecycle Phases

**Variation axes**: C-13 compliance + inertia framing (status-quo competitor as motivation) + lifecycle emphasis
**Hypothesis**: When every section opens by naming what teams do *without* this skill — and what breaks as a result — the consequence columns feel earned rather than ceremonial. Combined with explicit lifecycle phases and the C-13 fix as a named phase, this maximizes the operational weight of every constraint. Tests whether inertia framing amplifies consequence framing (C-14, C-20) beyond what temporal columns alone provide.

---

### Skill: topic:new

Without this skill, teams commit to feature designs based on whatever signals exist in memory: hallway conversations, guesses about user needs, one engineer's prior experience. The decision gets made because work must advance — not because evidence says it should. This skill changes that. It makes the gap between "what we know" and "what we need to know" visible before commit.

**Two outputs**: (1) a row in `simulations/TOPICS.md`, (2) `simulations/{topic}/strategy.md`

---

#### Phase 1 — Who Loses When We Decide Without Evidence

Without a stakeholders table, signal planning defaults to the PM's list of concerns or the loudest voice in the room. Roles that would have flagged a design risk stay invisible until post-ship.

Write this table **first**:

| # | Stakeholder Role | Immediate Risk (commit without evidence) | Downstream Risk (shipped without insight) |
|---|-----------------|------------------------------------------|-------------------------------------------|
| S-1 | | | |
| S-2 | | | |
| S-3 | | | |

Minimum 3 rows. Specific roles only. The S-N identifiers are your accountability keys — every signal row in the plan cites one. An uncited row is unauditable. A citation that doesn't resolve to a row in this table is a broken reference.

---

#### Phase 2 — TOPICS.md Registration

Without registration, the topic has no canonical path. Other skills cannot locate the strategy file. The topic becomes invisible to `topic:status`, `topic:score`, and `topic:report`.

Append one row to `simulations/TOPICS.md`:

| Topic | Status | Strategy Path | Registered |
|-------|--------|---------------|------------|
| {topic} | planning | simulations/{topic}/strategy.md | {date} |

---

#### Phase 3 — Rationale

Without a rationale, the strategy is a list of tasks with no stated purpose. When signal coverage gaps emerge mid-investigation, there is no anchor for deciding whether a gap matters. The decision the investigation informs stays implicit, and implicit decisions are never challenged.

Write a Rationale section in `simulations/{topic}/strategy.md`. Minimum 2 sentences: why investigation is needed, and what design decision it informs.

---

#### Phase 4 — FIELD SCHEMA

Without a field schema, signal rows accumulate however the model feels appropriate. Priority vocabulary drifts to "high/medium/low". Owner roles cluster to the team lead. Stakeholder coverage becomes a guess.

Every signal row must satisfy this schema. Each constraint names what breaks if violated — immediately, when the schema is checked, and downstream, when the strategy is used in execution.

| Field | Valid Values | Stakeholder Ref | Immediate Failure | Downstream Effect |
|-------|-------------|-----------------|-------------------|-------------------|
| namespace | scout / draft / review / flow / trace / prove / listen / program / topic | — | Row unroutable; no execution path | Namespace permanently absent from evidence base |
| skill | valid skill within the namespace | — | Skill not invokable; artifact not produced | Signal category missing from all commit evaluations |
| item name | `{topic}-{signal}-{date}.md` — see Artifact Naming Convention | — | Unlocatable by registry | Narrative references a file the system cannot find |
| owner role | role present in Phase 1 Stakeholders table | Required — cite S-N | No accountable party; provenance fails | Signal never assigned; gap reaches design commit |
| priority | `essential` / `recommended` / `optional` only | — | Strategy unparseable as a commit gate | Team commits without a stopping condition |

---

#### Phase 5 — Artifact Naming Convention

Without a documented naming convention, item names in the signal plan will vary in format. Some will be parseable. Some won't. Downstream skills cannot distinguish a missing artifact from a mis-named one — both look like gaps. The investigation appears incomplete even when the work was done.

All item names must follow:

```
{topic}-{signal}-{date}.md
```

- `{topic}` — topic slug (lowercase, hyphenated)
- `{signal}` — skill name (e.g., `scout-feasibility`, `draft-spec`, `prove-hypothesis`)
- `{date}` — `YYYY-MM-DD`

Example: `payments-scout-feasibility-2026-03-14.md`

Deviate from this pattern and the artifact is invisible to every downstream topic skill.

---

#### Phase 6 — COVERAGE SCHEMA

Without coverage thresholds, a strategy can satisfy all five field requirements on a single essential signal in a single namespace owned by one person. The strategy is technically valid and strategically blind.

| Constraint | Threshold | Immediate Failure | Downstream Effect |
|-----------|-----------|-------------------|-------------------|
| Essential signals | ≥ 1 | No commit gate; investigation cannot formally close | Team commits when momentum runs out, not when evidence is sufficient |
| Namespaces represented | ≥ 2 | Single-axis coverage; schema violation | Entire signal categories — trace, flow, prove, listen — are never investigated |
| Distinct Stakeholder Refs | ≥ 2 distinct S-N values | Single-stakeholder coverage | One risk perspective dominates; the other roles' concerns persist undetected through design and into production |

---

#### Phase 7 — Signal Plan

Without a pre-write gate, the model writes signal rows and checks coverage after the fact — if at all. Errors discovered after writing require rewrites. The gate forces verification to happen before commitment.

Pre-write gate:

- [ ] Phase 1 Stakeholders table: ≥ 3 rows, all columns filled
- [ ] At least 1 planned signal will be `essential`
- [ ] At least 2 distinct namespaces will appear
- [ ] At least 2 distinct S-N refs will appear in the Stakeholder Ref column
- [ ] All priorities: `essential` / `recommended` / `optional` only
- [ ] All item names: conform to Artifact Naming Convention (Phase 5)
- [ ] Commit Gate (Phase 8) will name specific item names

| Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
|-----------|-------|-----------|------------|-----------------|----------|

---

#### Phase 8 — Commit Gate

Without a named commit gate, "done" means "ran out of time" or "the PM said ship it." The team cannot point to a specific signal set and say: this is the evidence floor we committed to.

Name the essential signals by item name. Design commit is blocked until every listed signal exists. Do not write "all essential signals" — name each one. A gate that cannot be copied into a ticket is not a gate.

---

## Variation Summary

| # | Axis | Structural bet | Expected C-13 path |
|---|------|---------------|-------------------|
| V-01 | C-13 minimal fix | One named section added to R5 V-01; all else preserved | Section 3.3 "Artifact Naming Convention" with pattern + example |
| V-02 | Phrasing register | Conversational second-person; same structural machinery | Step 5 "Know the naming pattern" as named step heading |
| V-03 | Lifecycle emphasis | Six phases with entry/exit gates; naming is its own phase | Phase 5 "Artifact Naming Convention" with phase-gate format |
| V-04 | C-13 + schema compression | Named section compressed to two lines; tests minimum viable form | `**ARTIFACT NAMING CONVENTION**` heading + pattern + example |
| V-05 | C-13 + inertia + lifecycle | Status-quo failure framing in every phase opener | Phase 5 "Artifact Naming Convention" with inertia opening |
