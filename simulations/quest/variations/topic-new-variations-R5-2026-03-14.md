## topic-new Variations — Round 5

Based on the R4 excellence signals (C-19: Stakeholder traceability column, C-20: Temporally layered consequences), all five variations are built on a foundation that satisfies both. The single-axis variables are: **Role Sequence** (V-01), **Output Format** (V-02), **Phrasing Register** (V-03). Combinations follow in V-04 and V-05.

---

## V-01 — Stakeholder-Column as Primary Structural Axis

**Variation axis**: Role sequence
**Hypothesis**: Making the Stakeholder fill-in table the authoritative source for the FIELD SCHEMA's Stakeholder column — and requiring that column before any signal row is valid — enforces C-19 as a structural inevitability rather than a checklist item. Role differentiation (C-08) becomes auditable by column inspection rather than aggregate counting.

---

### Skill: topic:new

Register a new topic, define its investigation strategy, and plan the signals needed for design commit.

**Two outputs**: (1) a row in `simulations/TOPICS.md`, (2) `simulations/{topic}/strategy.md`

---

#### Phase 1 — Stakeholders Table (First Output Required)

Before planning signals, enumerate every role whose outcome depends on this topic.

Write this table as your **first output**:

| # | Stakeholder Role | Immediate Risk if Topic Fails | Downstream Risk if Topic is Skipped |
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
| item name | `{topic}-{signal}-{date}.md` | — | Artifact unlocatable by topic registry | Narrative references a file that does not exist |
| owner role | named role present in Stakeholders table | Required — cite S-N | No accountable party; provenance review fails | Signal is never assigned, never produced; gap persists to design commit |
| priority | `essential` / `recommended` / `optional` only | — | Strategy unparseable as a commit gate | Team proceeds to commit with no defined stopping condition |

The **Stakeholder Ref column** is what makes C-08 verifiable by structural inspection. Counting distinct values in the Owner Role column is insufficient — it does not confirm that each role covers a different risk exposure. Citing distinct S-N rows does.

##### 3.3 COVERAGE SCHEMA

| Constraint | Threshold | Immediate Failure | Downstream Effect |
|-----------|-----------|-------------------|-------------------|
| Essential signals | ≥ 1 | No commit gate exists | Investigation ends arbitrarily; commit is undefined |
| Namespaces represented | ≥ 2 | Single-axis coverage; schema violation | Entire signal categories invisible to topic narrative |
| Distinct Stakeholder Refs | ≥ 2 distinct S-N values | Single-stakeholder coverage | One risk perspective dominates; blindspots persist through design |

##### 3.4 Signal Plan

Pre-write gate — verify before writing any rows:

- [ ] Stakeholders table (Phase 1) has ≥ 3 rows with all columns filled
- [ ] At least 1 planned signal will be marked `essential`
- [ ] At least 2 distinct namespaces will appear
- [ ] At least 2 distinct S-N refs will appear in the Stakeholder Ref column
- [ ] All priorities will be: `essential` / `recommended` / `optional` only
- [ ] All item names will follow `{topic}-{signal}-{date}.md`

| Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
|-----------|-------|-----------|------------|-----------------|----------|

##### 3.5 Commit Gate

List the item names of all essential signals. Design commit is blocked until every listed signal exists. Do not write "all essentials" — name each one. A gate that cannot be pasted into a ticket is not a gate.

---

## V-02 — Schema-First, Prose Minimized

**Variation axis**: Output format
**Hypothesis**: Reducing prose to only what is required (rationale section) and making the two-tier schema the sole structural mechanism tests whether pure schema enforcement — without scaffolding narrative — can satisfy C-14, C-16, C-18, C-19, and C-20 simultaneously. If it can, prose elaboration is compressible.

---

### Skill: topic:new

**Inputs**: topic name, optional seed context
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
| skill | valid skill in namespace | — | Not invokable | Artifact category missing from topic |
| item name | `{topic}-{signal}-{date}.md` | — | Unlocatable by registry | Narrative references nonexistent file |
| owner role | role from Stakeholders table | Required: cite S-N | No accountable party | Signal orphaned; never produced |
| priority | `essential` / `recommended` / `optional` | — | Strategy unparseable | No commit gate; investigation never closes |

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
- [ ] All item names: `{topic}-{signal}-{date}.md`
- [ ] Commit gate names specific items

---

**SIGNAL PLAN**

| Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
|-----------|-------|-----------|------------|-----------------|----------|

---

**COMMIT GATE**

Name the essential signals by item name. These must exist before design commit. Do not reference the table — list each name explicitly.

---

## V-03 — Conversational Imperative Register

**Variation axis**: Phrasing register
**Hypothesis**: Replacing schema vocabulary with direct second-person instruction ("Your first output must be…") while preserving all structural mechanisms tests whether conversational framing reduces cognitive load without reducing structural compliance. The structural elements (tables, consequence columns, checkboxes) remain identical; only the register changes.

---

### topic:new — Register a topic and plan its investigation

You're going to produce two things: a row in TOPICS.md and a strategy file. Do them in order. Each step has a check before you move on.

---

#### Step 1 — Start with who's at risk

Your first output must be a stakeholder table. Every owner role you put in the signal plan must trace back to a row here.

| # | Who | What breaks immediately if this topic fails? | What persists downstream if we skip it entirely? |
|---|-----|---------------------------------------------|--------------------------------------------------|
| S-1 | | | |
| S-2 | | | |
| S-3 | | | |

Fill in at least 3 rows. Use specific role names — "PM", "backend engineer", "design lead", not "user" or "team". Once this table is written, the S-N numbers become your reference keys. You'll cite them in every signal row.

---

#### Step 2 — Register the topic

Add this row to `simulations/TOPICS.md`:

| Topic | Status | Strategy | Registered |
|-------|--------|----------|------------|
| {topic} | planning | simulations/{topic}/strategy.md | {date} |

---

#### Step 3 — Write a rationale

Start `simulations/{topic}/strategy.md` with a Rationale section. At least 2 sentences. Why does this topic need investigation? What decision does it unlock?

---

#### Step 4 — Understand the rules before you plan

Each signal row has 6 fields. Here's what's allowed in each — and what breaks if you get it wrong:

| Field | What's valid | If you get it wrong immediately | What that causes downstream |
|-------|-------------|--------------------------------|----------------------------|
| namespace | scout / draft / review / flow / trace / prove / listen / program / topic | Row can't be executed | That namespace's signals never appear in the topic |
| skill | any valid skill in the namespace | Skill can't be invoked | That artifact category never gets produced |
| item name | `{topic}-{signal}-{date}.md` | Registry can't find it | Narrative references a file that doesn't exist |
| owner role | a role from Step 1 | No one owns it; it fails provenance | Signal never gets made; gap reaches commit |
| stakeholder ref | the S-N from Step 1 | Traceability is broken | Role coverage can't be audited |
| priority | `essential` or `recommended` or `optional` — nothing else | Strategy can't be parsed as a gate | Team doesn't know which signals are required |

**On priority**: This is the failure mode most worth stating explicitly. "High", "medium", "low", "required" — none of these work. The tool that reads the strategy expects exactly `essential`, `recommended`, or `optional`. Anything else makes the strategy inert as a commit gate.

**On stakeholder ref**: Counting "2 distinct owner roles" doesn't tell you whether those roles cover different risks. Citing 2 distinct S-N rows does. Use the ref column.

---

#### Step 5 — Check these before writing

- [ ] Stakeholders table (Step 1) has ≥ 3 rows, all four columns filled
- [ ] At least 1 signal will be `essential`
- [ ] At least 2 different namespaces are in the plan
- [ ] At least 2 different S-N refs are in the Stakeholder Ref column
- [ ] Every priority is exactly: `essential` / `recommended` / `optional`
- [ ] Every item name follows: `{topic}-{signal}-{date}.md`
- [ ] Commit gate (Step 6) will name specific item names

All six boxes checked? Now write the signal plan.

| Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
|-----------|-------|-----------|------------|-----------------|----------|

---

#### Step 6 — Name the commit gate

Add a Commit Gate section to strategy.md. List the item names of every `essential` signal. The team needs these before design commit. Don't say "see the essentials above" — name them. A gate you can't paste into a ticket isn't a gate.

---

## V-04 — Role Sequence + Lifecycle Emphasis (Phased Gates)

**Variation axes**: Role sequence + Lifecycle emphasis
**Hypothesis**: Combining stakeholder-first role sequence with explicit numbered phases and a gate checklist at each phase boundary tests whether per-phase enforcement eliminates criterion omissions more reliably than a single pre-write gate. Each phase is a bounded unit with entry and exit conditions — the model cannot advance without satisfying the current phase's structural requirements.

---

### Skill: topic:new

Register a new topic. Plan the signals that gate design commit. Produce two artifacts: a TOPICS.md row and `simulations/{topic}/strategy.md`.

This skill runs in four phases. Each phase has an entry condition and an exit gate. Do not enter a phase until the previous gate is cleared.

---

#### Phase 1 — Stakeholder Enumeration

**Entry condition**: Topic name is known.
**Exit gate**: Stakeholders table has ≥ 3 rows, all columns filled, roles are specific.

Your first output is the Stakeholders table. Enumerate every role whose outcome depends on this topic.

| # | Stakeholder Role | Immediate Risk (topic fails) | Downstream Risk (topic skipped) |
|---|-----------------|------------------------------|----------------------------------|
| S-1 | | | |
| S-2 | | | |
| S-3 | | | |

This table is the authority for the Stakeholder Ref column in Phase 3's FIELD SCHEMA. Roles not present in this table are not valid signal owners. Rows added to the signal plan after Phase 1 that cite `S-N` values not in this table are broken references.

Two risk columns are required because the nature of harm differs by timing. Immediate risk is what breaks when a decision is made without the signal. Downstream risk is what persists when the signal was never collected. Both must be visible to justify investigation.

**Phase 1 exit gate**:
- [ ] ≥ 3 stakeholder rows, all four columns filled
- [ ] Roles are specific (not "user", not "team")
- [ ] At least 2 distinct risk categories are visible across Immediate Risk and Downstream Risk

---

#### Phase 2 — TOPICS.md Registration

**Entry condition**: Phase 1 exit gate cleared.
**Exit gate**: TOPICS.md row written and parseable.

Append one row to `simulations/TOPICS.md`:

| Topic | Status | Strategy Path | Registered |
|-------|--------|---------------|------------|
| {topic} | planning | simulations/{topic}/strategy.md | {date} |

**Phase 2 exit gate**:
- [ ] Row appended (not replaced) to TOPICS.md
- [ ] Status is exactly `planning`
- [ ] Strategy path is exactly `simulations/{topic}/strategy.md`

---

#### Phase 3 — Strategy File: Schemas and Signal Plan

**Entry condition**: Phase 2 exit gate cleared.
**Exit gate**: All FIELD SCHEMA and COVERAGE SCHEMA constraints satisfied; signal plan written.

Create `simulations/{topic}/strategy.md`.

##### 3.1 Rationale
Two or more sentences explaining why this topic requires investigation and what design decision it informs.

##### 3.2 FIELD SCHEMA

| Field | Valid Values | Stakeholder Ref | Immediate Failure | Downstream Effect |
|-------|-------------|-----------------|-------------------|-------------------|
| namespace | scout / draft / review / flow / trace / prove / listen / program / topic | — | Row unroutable; no execution path exists | Namespace gap — category absent from topic's evidence base |
| skill | valid skill in the namespace | — | Skill not invokable; artifact never produced | Signal category silently missing from commit evaluation |
| item name | `{topic}-{signal}-{date}.md` | — | Unlocatable by registry at validation time | Narrative references a file that does not and cannot exist |
| owner role | role present in Phase 1 Stakeholders table | Required — cite S-N | No accountable party; provenance review fails | Signal never assigned; never produced; gap reaches commit |
| priority | `essential` / `recommended` / `optional` only | — | Strategy unparseable as commit gate | Team proceeds to commit with no defined stopping condition |

##### 3.3 COVERAGE SCHEMA

| Constraint | Threshold | Immediate Failure | Downstream Effect |
|-----------|-----------|-------------------|-------------------|
| Essential signals | ≥ 1 | No commit gate exists | Investigation ends arbitrarily or never |
| Namespaces represented | ≥ 2 | Single-axis coverage; schema violation | Entire categories invisible to topic narrative |
| Distinct Stakeholder Refs | ≥ 2 distinct S-N values | Single-stakeholder coverage | One risk perspective dominates; blindspots persist to production |

##### 3.4 Signal Plan

**Phase 3 entry gate** — verify before writing rows:
- [ ] Phase 1 Stakeholders table has ≥ 3 rows with all columns filled
- [ ] At least 1 planned signal will be `essential`
- [ ] At least 2 distinct namespaces will appear
- [ ] At least 2 distinct S-N refs will appear in the Stakeholder Ref column
- [ ] All priority values will be: `essential` / `recommended` / `optional`
- [ ] All item names will follow: `{topic}-{signal}-{date}.md`

| Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
|-----------|-------|-----------|------------|-----------------|----------|

**Phase 3 exit gate**:
- [ ] Every row satisfies all FIELD SCHEMA fields
- [ ] Every Owner Role cites an S-N present in the Phase 1 table
- [ ] COVERAGE SCHEMA thresholds are met
- [ ] All priority values: `essential` / `recommended` / `optional`

---

#### Phase 4 — Commit Gate Declaration

**Entry condition**: Phase 3 exit gate cleared.
**Exit gate**: Commit gate names specific item names, not a category.

In strategy.md, add a Commit Gate section. List the item names of all essential signals. Design commit is blocked until every listed signal exists.

Do not write "all essential signals" or "see signal plan above." Name each item explicitly. A gate that cannot be copied verbatim into a work item is not a gate.

**Phase 4 exit gate**:
- [ ] Commit gate section exists in strategy.md
- [ ] Each item is named explicitly (not referenced by count or category)
- [ ] Named item count matches the number of `essential` rows in Phase 3

---

#### Consequence Reference

Applies across all phases. Every constraint has two failure tiers.

| Violation | Immediate | Downstream |
|-----------|-----------|------------|
| Invalid priority word | Strategy unparseable | No commit gate; investigation ends arbitrarily |
| No essential signal | Gate undefined | Commit is undefined; quality cannot be evaluated |
| Stakeholder Ref missing | Row unauditable | Role coverage unverifiable; blindspots persist |
| S-N cites unlisted row | Broken reference | Accountability never resolved; signal orphaned |
| < 2 namespaces | Coverage schema fails | Signal categories missing from evidence base |
| Item name off-pattern | Artifact unlocatable | Narrative references nonexistent file |
| Owner role not in Stakeholders table | Provenance failure | Signal never assigned; gap reaches commit |

---

## V-05 — C-19 + C-20 Maximized (Traceability Column + Temporal Consequence Layering)

**Variation axes**: Role sequence + Consequence framing
**Hypothesis**: Making C-19 (Stakeholder column with row-level traceability) and C-20 (Immediate failure / Downstream effect split on every constraint) the co-primary structural mechanisms — and making their interaction explicit — tests whether the two R4 excellence signals reinforce each other when both are maximally featured. C-19 makes role coverage structurally auditable; C-20 makes every constraint carry operational weight at two points in time. Together, they should eliminate the need for any prose-only enforcement.

---

### Skill: topic:new

Register a new topic. Define its investigation strategy. Plan the signals that gate design commit.

**Two outputs**: (1) `simulations/TOPICS.md` row, (2) `simulations/{topic}/strategy.md`

---

#### Step 1 — Stakeholders (First Output, Required)

Write this table before anything else. Signal rows in Step 6 cite these by `S-N`. The citation is what makes role coverage auditable.

| # | Stakeholder Role | Immediate Risk (topic fails) | Downstream Risk (topic skipped) |
|---|-----------------|------------------------------|----------------------------------|
| S-1 | | | |
| S-2 | | | |
| S-3 | | | |

**Why two risk columns on the Stakeholders table**: The same role faces different kinds of harm depending on timing. Immediate risk is what breaks when a decision is made without the signal — a product choice is locked in without the information. Downstream risk is what persists when the topic was never investigated — a shipped product operates without the understanding that would have changed its design. Both must be visible to justify why each role belongs in the investigation.

Minimum 3 rows. Roles must be specific. Every Owner Role in the signal plan must cite an S-N from this table. An S-N citation that does not appear in this table is a broken reference and invalidates the row.

---

#### Step 2 — TOPICS.md

Append one row to `simulations/TOPICS.md`:

| Topic | Status | Strategy | Registered |
|-------|--------|----------|------------|
| {topic} | planning | simulations/{topic}/strategy.md | {date} |

---

#### Step 3 — Rationale

In `simulations/{topic}/strategy.md`, write a Rationale section: 2+ sentences explaining why this topic requires investigation and what design decision it informs.

---

#### Step 4 — FIELD SCHEMA

Every signal row must satisfy this schema. The Stakeholder Ref column is not optional — it is what makes the schema structurally enforceable rather than prose-dependent. Each constraint carries two consequence tiers: what breaks at schema-validation time (Immediate Failure) and what breaks when the strategy is used in execution (Downstream Effect).

| Field | Valid Values | Stakeholder Ref | Immediate Failure | Downstream Effect |
|-------|-------------|-----------------|-------------------|-------------------|
| namespace | scout / draft / review / flow / trace / prove / listen / program / topic | — | Row unroutable; no skill execution path exists | Namespace gap — this category is permanently absent from the topic's evidence base |
| skill | valid skill within the namespace | — | Skill cannot be invoked; artifact is never produced | That signal category is silently excluded from commit evaluation |
| item name | `{topic}-{signal}-{date}.md` | — | Artifact unlocatable by topic registry at validation time | Topic narrative references a file that does not and cannot exist |
| owner role | named role present in Step 1 Stakeholders table | Required — cite S-N | No accountable party; row fails provenance review immediately | Signal is never assigned, never produced; the gap reaches design commit undetected |
| priority | `essential` / `recommended` / `optional` only — no other values | — | Strategy is unparseable as a commit gate at parse time | Team proceeds to commit without a defined stopping condition; investigation ends arbitrarily |

**On the Stakeholder Ref column**: Counting distinct values in the Owner Role column tells you how many role names appear. It does not tell you whether each role covers a distinct risk exposure. Citing distinct S-N values in the Stakeholder Ref column tells you whether the signal plan's accountability structure maps to the actual stakeholder risk surface. C-08 (role differentiation) is satisfied by structural inspection of this column — not by counting.

---

#### Step 5 — COVERAGE SCHEMA

| Constraint | Threshold | Immediate Failure | Downstream Effect |
|-----------|-----------|-------------------|-------------------|
| Essential signals | ≥ 1 | No commit gate exists — the strategy cannot gate any decision | Investigation has no defined stopping condition; it ends arbitrarily or runs indefinitely |
| Namespaces represented | ≥ 2 | Single-axis coverage; schema violation at structural review | Entire signal categories (e.g., trace, flow, prove) are never part of the topic's evidence base |
| Distinct Stakeholder Refs | ≥ 2 distinct S-N values | Single-stakeholder coverage — traceability check fails | One risk perspective dominates the signal plan; unrepresented stakeholder risks persist through design and ship into production |

---

#### Step 6 — Signal Plan

Pre-write gate — verify before writing any rows:

- [ ] Step 1 Stakeholders table: ≥ 3 rows, all four columns filled
- [ ] At least 1 planned signal will carry `essential`
- [ ] At least 2 distinct namespaces will appear
- [ ] At least 2 distinct S-N refs will appear in the Stakeholder Ref column
- [ ] All priority values will be exactly: `essential` / `recommended` / `optional`
- [ ] All item names will follow: `{topic}-{signal}-{date}.md`
- [ ] Commit gate (Step 7) will name specific item names — not "see essentials"

All boxes checked? Write the signal plan:

| Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
|-----------|-------|-----------|------------|-----------------|----------|

---

#### Step 7 — Commit Gate

Name the essential signals by item name. Design commit is blocked until every named signal exists. Do not write "all essential signals" — list each one. A gate that cannot be copied into a ticket is not a gate.

---

#### Consequence Appendix

Every constraint in this skill carries temporal consequence layering. "Immediate failure" fires at schema-validation time. "Downstream effect" fires when the strategy is used in execution or when the built product ships.

| Violation | Immediate | Downstream |
|-----------|-----------|------------|
| Invalid priority word | Strategy unparseable as gate | No stopping condition; commit is undefined |
| No essential signal | Gate undefined; strategy is decorative | Investigation ends arbitrarily; quality cannot be evaluated |
| Stakeholder Ref missing | Row unauditable at review | Role coverage cannot be verified; blindspots persist |
| Stakeholder Ref cites unlisted S-N | Broken reference; row invalid | Accountability never resolved; signal is orphaned |
| < 2 namespaces | Coverage schema fails immediately | Signal categories missing from evidence base |
| Item name off-pattern | Unlocatable by registry | Narrative references a file that will never exist |
| Owner role not in Stakeholders table | Provenance failure at review | Signal never assigned; gap reaches design commit |

---

## Variation Summary

| # | Axis | Structural bet | Key differentiator |
|---|------|---------------|-------------------|
| V-01 | Role sequence | Stakeholder table is authoritative source for FIELD SCHEMA's Stakeholder column | C-19 enforced before signal plan begins |
| V-02 | Output format | Schema replaces prose as the only structural mechanism | Minimal surface area; maximum structural density |
| V-03 | Phrasing register | Conversational second-person with identical structural machinery | Tests whether register affects compliance independently of structure |
| V-04 | Role sequence + Lifecycle | Per-phase gate checklists with entry/exit conditions | Phase-bounded enforcement prevents silent omissions across phases |
| V-05 | Role sequence + Consequence framing | C-19 + C-20 as co-primary mechanisms; consequence appendix makes temporal layering explicit | Tests whether two R4 excellence signals reinforce or duplicate each other |
