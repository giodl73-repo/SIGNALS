---

## Round 8 — topic-new Variations (v7 rubric)

**New criteria in scope**: C-23 (schema row IDs for gate citation), C-24 (pipeline overview table before phase content), C-25 (commit gate as dedicated Phase 8, separate from signal plan Phase 7).

**Single-axis selected**: Lifecycle emphasis (V-01), Output format (V-02), Phrasing register (V-03).  
**Combinations**: Lifecycle + Inertia framing (V-04), Output format + Role sequence + Inertia framing (V-05).

---

## V-01 — Lifecycle Emphasis

**Axis**: Lifecycle emphasis — the pipeline overview table carries three informational columns (Purpose, Produces, Exit Gate), making each phase's contribution derivable from the overview alone before the model reads any phase body.

**Hypothesis**: A three-column overview table (Purpose + Produces + Exit Gate) satisfies C-24 with maximum architectural clarity — a reviewer can verify every exit gate condition from the overview alone without entering phase bodies. Adding explicit "Produces" outputs also pre-declares the artifact shape of each phase, which may improve C-02 and C-10 compliance across diverse inputs.

---

### REGISTER A NEW TOPIC

#### PIPELINE OVERVIEW

Read this entire table before executing Phase 1. All exit gate conditions are declared here. Each phase also carries its own inline gate — both layers must be satisfied.

| Phase | Purpose | Produces | Exit Gate |
|-------|---------|----------|-----------|
| 1 | Enumerate stakeholders and their risk exposure | Stakeholders table with S-01..S-N rows | >= 3 rows; all 4 columns filled; roles specific (e.g., "PM", "tech lead") — not "user" |
| 2 | Register the topic in the shared registry | One appended row in `simulations/TOPICS.md` | Row present with topic name, status=active, and strategy path |
| 3 | Write narrative rationale | Rationale section in `simulations/{topic}/strategy.md` | >= 2 sentences; names the design decision this strategy informs |
| 4 | Define constraint schemas | FIELD SCHEMA (F-01..F-05) and COVERAGE SCHEMA (COV-01..COV-03) | All 8 rows present; each carries Immediate Failure and Downstream Effect |
| 5 | Define artifact naming convention | Naming Convention section in strategy.md | Pattern documented with at least one parameterized example |
| 6 | Verify signal plan preconditions | Pre-write checklist | All F-01..F-05 and COV-01..COV-03 checkable before writing rows |
| 7 | Produce signal plan rows | Signal Plan table in strategy.md | All rows pass F-01..F-05; full set passes COV-01..COV-03 |
| 8 | Name the commit gate | Commit Gate section in strategy.md | >= 1 essential signal named by exact item name; gate condition stated explicitly |

Do not advance past any phase until its exit gate is satisfied.

---

### PHASE 1 — STAKEHOLDERS

WHO BEARS THE RISK if this topic's strategy is wrong? Fill in this table as your first output. Roles in the signal plan must trace back to rows in this table.

| # | Stakeholder Role | Decision They Own | Risk If Strategy Fails |
|---|-----------------|-------------------|------------------------|
| S-01 | | | |
| S-02 | | | |
| S-03 | | | |
| ... | | | |

**Phase 1 exit gate:**
- [ ] >= 3 rows filled; all four columns populated
- [ ] Roles are specific (not "user", "person", "stakeholder")
- [ ] Each risk statement names a concrete failure outcome

---

### PHASE 2 — TOPICS.md ENTRY

Append one row to `simulations/TOPICS.md`:

| Topic | Status | Strategy Path |
|-------|--------|---------------|
| {topic} | active | simulations/{topic}/strategy.md |

**Phase 2 exit gate:**
- [ ] Row appended to `simulations/TOPICS.md`
- [ ] Status is exactly `active`
- [ ] Strategy path is exactly `simulations/{topic}/strategy.md`

---

### PHASE 3 — RATIONALE

Open `simulations/{topic}/strategy.md`. Write:

```
## Rationale

{>= 2 sentences explaining why this topic needs investigation
and what design decision this strategy informs}
```

**Phase 3 exit gate:**
- [ ] Rationale section exists in `simulations/{topic}/strategy.md`
- [ ] >= 2 sentences present
- [ ] Names the specific design decision this topic strategy informs

---

### PHASE 4 — CONSTRAINT SCHEMAS

These two schemas are the authoritative constraint registry. Gate checkpoints in Phases 6 and 7 cite rows by ID — do not restate rules inline.

#### FIELD SCHEMA

| ID | Field | Rule | Immediate Failure | Downstream Effect |
|----|-------|------|-------------------|-------------------|
| F-01 | Namespace | Must be one of: scout, draft, review, flow, trace, prove, listen, program, topic | Row rejected — namespace does not correspond to a real skill set | Signal is orphaned; team cannot find or produce it |
| F-02 | Skill | Must name a specific skill within the declared namespace | Row rejected — skill is ambiguous or unresolvable | Signal is never generated; gap remains invisible |
| F-03 | Item Name | Must follow `{topic}-{signal}-{date}.md` (parameterized template acceptable) | Row rejected — artifact is unlocatable | Signal cannot be scheduled, reviewed, or committed |
| F-04 | Owner Role | Must reference a specific S-N row from the Phase 1 Stakeholders table | Row rejected — owner is unresolvable to a real accountable role | Signal has no owner; it is never produced |
| F-05 | Priority | Must be exactly: `essential` / `recommended` / `optional` — no substitutions | Strategy unparseable as commit gate | Team commits without a defined stopping condition |

#### COVERAGE SCHEMA

| ID | Rule | Threshold | Immediate Failure | Downstream Effect |
|----|------|-----------|-------------------|-------------------|
| COV-01 | At least one essential signal | >= 1 row where priority = essential | Strategy has no commit gate | Team has no mandatory stopping condition before design commit |
| COV-02 | Multi-namespace coverage | >= 2 distinct namespaces across all rows | Strategy is single-perspective | Critical risk categories invisible to the plan |
| COV-03 | Differentiated owner roles | >= 2 distinct S-N refs across all rows | All signals owned by one person | Single point of failure; cross-functional review cannot occur |

**Phase 4 exit gate:**
- [ ] FIELD SCHEMA rows F-01 through F-05 are present and complete
- [ ] COVERAGE SCHEMA rows COV-01 through COV-03 are present and complete
- [ ] Every row carries both Immediate Failure and Downstream Effect columns populated

---

### PHASE 5 — ARTIFACT NAMING CONVENTION

Write a dedicated section in `simulations/{topic}/strategy.md`:

```
## Artifact Naming Convention

Pattern: {topic}-{signal}-{date}.md
Example: {topic}-scout-feasibility-{date}.md

All signal item names in the Signal Plan must follow this pattern.
Parameterized templates are acceptable in the strategy file.
```

**Phase 5 exit gate:**
- [ ] Naming Convention section has its own heading in strategy.md
- [ ] Pattern documented
- [ ] At least one parameterized example present

---

### PHASE 6 — PRE-WRITE VERIFICATION

Before writing any signal rows, verify that all constraints are satisfiable for your planned signal set. Do not advance to Phase 7 until all items pass.

**Phase 6 exit gate (entry gate for Phase 7):**
- [ ] F-01: All planned namespaces are in the allowed set
- [ ] F-02: All planned skills are named specifically
- [ ] F-03: All planned item names can be expressed as `{topic}-{signal}-{date}.md`
- [ ] F-04: Every planned owner role corresponds to an S-N row from Phase 1
- [ ] F-05: All planned priority values are exactly `essential` / `recommended` / `optional`
- [ ] COV-01: At least 1 signal is planned as `essential`
- [ ] COV-02: At least 2 distinct namespaces are represented
- [ ] COV-03: At least 2 distinct S-N rows are referenced as owners

---

### PHASE 7 — SIGNAL PLAN

Write the signal plan table to `simulations/{topic}/strategy.md`:

```
## Signal Plan

| Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
|-----------|-------|-----------|------------|-----------------|----------|
```

Every row must satisfy F-01 through F-05. The complete set must satisfy COV-01 through COV-03.

**Phase 7 exit gate:**
- [ ] All rows satisfy F-01 (valid namespace)
- [ ] All rows satisfy F-02 (named skill)
- [ ] All rows satisfy F-03 (item name follows convention)
- [ ] All rows satisfy F-04 (owner references S-N from Phase 1)
- [ ] All rows satisfy F-05 (priority is essential / recommended / optional)
- [ ] Table satisfies COV-01 (>= 1 essential row present)
- [ ] Table satisfies COV-02 (>= 2 distinct namespaces)
- [ ] Table satisfies COV-03 (>= 2 distinct S-N refs)

Do not advance to Phase 8 until all exit gate items are checked.

---

### PHASE 8 — COMMIT GATE

This is a dedicated phase separate from signal plan production. It names the mandatory minimum set required before design commit.

Write to `simulations/{topic}/strategy.md`:

```
## Commit Gate

Design commit requires the following signals to exist:
- {item-name-1} (essential)
- {item-name-2} (essential)
...

Gate condition: all items above must be present before design commit proceeds.
```

**Phase 8 exit gate:**
- [ ] >= 1 essential signal named by its exact item name from Phase 7
- [ ] Gate condition stated explicitly (not "most signals" — specific named signals)
- [ ] Commit Gate section has its own dedicated heading in strategy.md

---

---

## V-02 — Output Format

**Axis**: Output format — ultra-compact ID-citation-only gates. Gate checkboxes cite schema row IDs exclusively (e.g., `- [ ] F-01..F-05 pass`) without restating rule prose. The pipeline overview is minimal (Phase + Exit Gate, no Purpose/Produces columns).

**Hypothesis**: Reducing gate checkboxes to schema ID references (not prose restatements) tests whether mechanical compactness improves or degrades compliance. If the FIELD SCHEMA and COVERAGE SCHEMA are established in Phase 4, a Phase 7 gate that reads `- [ ] F-01..F-05: all rows pass` is structurally equivalent to an expanded checklist but takes one line. The hypothesis is that ID-only gates satisfy C-21 and C-23 equally well while reducing total prompt length.

---

### REGISTER A NEW TOPIC

#### PIPELINE OVERVIEW

All exit gates are declared in this table. Read before executing any phase.

| Phase | Exit Gate |
|-------|-----------|
| 1 — Stakeholders | >= 3 rows; all 4 cols filled; roles specific |
| 2 — TOPICS.md | Row appended; status=active; path correct |
| 3 — Rationale | >= 2 sentences; design decision named |
| 4 — Schemas | F-01..F-05 rows present; COV-01..COV-03 rows present; each row has both consequence tiers |
| 5 — Naming | Pattern documented; parameterized example present |
| 6 — Pre-write | F-01..F-05 checkable; COV-01..COV-03 checkable |
| 7 — Signal Plan | F-01..F-05 pass per row; COV-01..COV-03 pass across rows; post-write gate clear |
| 8 — Commit Gate | >= 1 essential named by item name; gate condition explicit |

---

### PHASE 1 — STAKEHOLDERS

First output: fill in this table.

| # | Role | Decision Owned | Risk If Strategy Fails |
|---|------|----------------|------------------------|
| S-01 | | | |
| S-02 | | | |
| S-03 | | | |

- [ ] >= 3 rows; all 4 columns filled; roles specific

---

### PHASE 2 — TOPICS.md

Append to `simulations/TOPICS.md`:

`{topic} | active | simulations/{topic}/strategy.md`

- [ ] Row appended; status=active; path=`simulations/{topic}/strategy.md`

---

### PHASE 3 — RATIONALE

Write to `simulations/{topic}/strategy.md`:

```
## Rationale
{>= 2 sentences; names the design decision this strategy informs}
```

- [ ] >= 2 sentences; design decision named

---

### PHASE 4 — SCHEMAS

#### FIELD SCHEMA

| ID | Field | Rule | Immediate Failure | Downstream Effect |
|----|-------|------|-------------------|-------------------|
| F-01 | Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | Row rejected | Signal orphaned |
| F-02 | Skill | Specific skill within namespace | Row rejected | Signal never produced |
| F-03 | Item Name | `{topic}-{signal}-{date}.md` template | Row rejected | Artifact untrackable |
| F-04 | Owner Role | S-N reference from Phase 1 table | Row rejected | No accountable owner |
| F-05 | Priority | `essential` / `recommended` / `optional` only | Strategy unparseable as commit gate | Team commits without stopping condition |

#### COVERAGE SCHEMA

| ID | Rule | Threshold | Immediate Failure | Downstream Effect |
|----|------|-----------|-------------------|-------------------|
| COV-01 | >= 1 essential signal | priority=essential count >= 1 | No commit gate defined | No mandatory stopping condition |
| COV-02 | >= 2 distinct namespaces | namespace distinct count >= 2 | Single-perspective strategy | Critical risks unseen |
| COV-03 | >= 2 distinct S-N refs | stakeholder ref distinct count >= 2 | Single owner across all signals | No cross-functional coverage |

- [ ] F-01..F-05 rows all present; consequence columns populated
- [ ] COV-01..COV-03 rows all present; consequence columns populated

---

### PHASE 5 — NAMING CONVENTION

Write to strategy.md:

```
## Artifact Naming Convention
Pattern: {topic}-{signal}-{date}.md
Example: {topic}-scout-feasibility-{date}.md
```

- [ ] Pattern documented; parameterized example present

---

### PHASE 6 — PRE-WRITE GATE

Verify before writing any signal rows:

- [ ] F-01: namespaces planned are in allowed set
- [ ] F-02: skills planned are named specifically
- [ ] F-03: item names expressible as `{topic}-{signal}-{date}.md`
- [ ] F-04: every owner maps to an S-N from Phase 1
- [ ] F-05: all priorities are essential / recommended / optional
- [ ] COV-01: >= 1 essential planned
- [ ] COV-02: >= 2 namespaces planned
- [ ] COV-03: >= 2 distinct S-N refs planned

---

### PHASE 7 — SIGNAL PLAN

Write to `simulations/{topic}/strategy.md`:

```
## Signal Plan

| Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
|-----------|-------|-----------|------------|-----------------|----------|
```

**Entry gate** (from Phase 6 — must be clear before writing rows).

**Exit gate** (verify after writing rows before advancing to Phase 8):
- [ ] F-01..F-05 pass for every row
- [ ] COV-01..COV-03 pass across the full set

---

### PHASE 8 — COMMIT GATE

Write to `simulations/{topic}/strategy.md`:

```
## Commit Gate

Design commit requires:
- {item-name} (essential)
...
Gate condition: all listed signals must exist before design commit proceeds.
```

**Phase 8 entry gate:** Phase 7 exit gate must be cleared.

**Phase 8 exit gate:**
- [ ] >= 1 essential signal named by exact item name from Phase 7
- [ ] Gate condition explicit (named signals, not "most signals" or "sufficient signals")
- [ ] Commit Gate has its own heading in strategy.md

---

---

## V-03 — Phrasing Register

**Axis**: Phrasing register — conversational imperative ("Here's what you do", "Before you write a single row") throughout all phases, while preserving the full structural backbone (F-N/COV-N IDs, pipeline overview, Phase 8 isolation).

**Hypothesis**: Conversational register reduces cognitive friction during prompt execution without reducing structural compliance. The hypothesis is that a model executing a conversational-register prompt achieves the same schema-ID-citation and gate-per-boundary compliance as a formal register prompt, and that any compliance gap would indicate the formal register was doing enforcement work that the structure alone should provide.

---

### REGISTER A NEW TOPIC

Here's the complete pipeline. Read this overview before you do anything — it lists every phase, what you'll produce, and what has to be true before you move on.

| Phase | What you do | What you produce | You can move on when... |
|-------|-------------|-----------------|-------------------------|
| 1 — Who's at risk | Map everyone affected by a bad strategy | Stakeholders table (S-01..S-N) | >= 3 rows filled, roles specific, risks concrete |
| 2 — Register it | Add the topic to the shared registry | One row in `simulations/TOPICS.md` | Row present, status=active, path correct |
| 3 — Explain why | Write the rationale | Rationale section in strategy.md | >= 2 sentences, design decision named |
| 4 — Define the rules | Establish the constraint schemas | FIELD SCHEMA (F-01..F-05) + COVERAGE SCHEMA (COV-01..COV-03) | All rows present, both consequence tiers filled |
| 5 — Name the artifacts | Define the naming convention | Naming Convention section | Pattern documented, example present |
| 6 — Check before writing | Verify your plan against the schemas | Pre-write checklist cleared | F-01..F-05 and COV-01..COV-03 all checkable |
| 7 — Write the signals | Produce the signal plan table | Signal Plan table in strategy.md | Every row passes F-01..F-05; full set passes COV-01..COV-03 |
| 8 — Name the gate | State the commit gate explicitly | Commit Gate section in strategy.md | >= 1 essential named by item name, gate condition stated |

Don't move past any phase until the "You can move on when..." condition is met.

---

### PHASE 1 — WHO'S AT RISK?

Before you plan any signals, map out who gets hurt if this strategy is wrong. This is your first output — not the signal plan, not the TOPICS.md entry. This table.

| # | Role | Decision They Own | What Goes Wrong If the Strategy Fails |
|---|------|-------------------|---------------------------------------|
| S-01 | | | |
| S-02 | | | |
| S-03 | | | |
| ... | | | |

The roles you write here (S-01, S-02, ...) are what you'll use in the signal plan's Owner Role column. If a role doesn't appear here, it can't own a signal.

**Before you move on:**
- [ ] >= 3 rows filled, all 4 columns populated
- [ ] Roles are specific — "PM", "tech lead", "backend engineer", not "user" or "team"
- [ ] Each risk is a concrete failure outcome, not a vague concern

---

### PHASE 2 — REGISTER THE TOPIC

Add one row to `simulations/TOPICS.md`:

| Topic | Status | Strategy Path |
|-------|--------|---------------|
| {topic} | active | simulations/{topic}/strategy.md |

**Before you move on:**
- [ ] Row is in `simulations/TOPICS.md`
- [ ] Status is exactly `active`
- [ ] Path is exactly `simulations/{topic}/strategy.md`

---

### PHASE 3 — EXPLAIN WHY THIS TOPIC MATTERS

Open `simulations/{topic}/strategy.md` and write a rationale section. Tell the reader why this topic needs investigation and what design decision this strategy will inform.

```
## Rationale

{Your explanation here — at least 2 sentences.
Name the specific design decision that this strategy's signals will resolve.}
```

**Before you move on:**
- [ ] Rationale section is in strategy.md
- [ ] >= 2 sentences present
- [ ] The design decision is named (not "we need to learn about this" — state what will be decided)

---

### PHASE 4 — DEFINE THE CONSTRAINT RULES

Here are the two schemas that govern every signal row and the overall signal set. Later phases cite these by row ID — you won't need to restate the rules, just reference them.

#### FIELD SCHEMA — rules that apply to every individual signal row

| ID | Field | What's required | If you get it wrong immediately | What that causes downstream |
|----|-------|-----------------|--------------------------------|------------------------------|
| F-01 | Namespace | Must be one of: scout, draft, review, flow, trace, prove, listen, program, topic | The row doesn't map to a real skill set | The signal can't be found or produced |
| F-02 | Skill | Must name a specific skill within that namespace — not just the namespace itself | The row is ambiguous and unresolvable | The signal is never generated; the gap is invisible |
| F-03 | Item Name | Must follow `{topic}-{signal}-{date}.md` — parameterized template is fine | The artifact can't be located | The signal can't be reviewed, scheduled, or committed |
| F-04 | Owner Role | Must be an S-N reference from your Phase 1 table | The owner is unresolvable | The signal has no accountable owner and will never get done |
| F-05 | Priority | Must be exactly `essential`, `recommended`, or `optional` — nothing else | The strategy can't be parsed as a commit gate | The team won't know what signals are mandatory before design commit |

#### COVERAGE SCHEMA — rules that apply to the signal plan as a whole

| ID | Rule | Minimum | If the minimum isn't met immediately | What that causes downstream |
|----|------|---------|--------------------------------------|------------------------------|
| COV-01 | At least one essential signal | >= 1 row where priority = essential | The strategy has no commit gate | Nothing gates design commit; the topic can commit without evidence |
| COV-02 | Multiple namespaces covered | >= 2 distinct namespaces | The strategy is single-perspective | Entire risk categories go unexamined before commit |
| COV-03 | Multiple owners | >= 2 distinct S-N refs | All signals belong to one person | Single point of failure; no cross-functional coverage |

**Before you move on:**
- [ ] F-01 through F-05 are all present with both consequence columns filled
- [ ] COV-01 through COV-03 are all present with both consequence columns filled

---

### PHASE 5 — NAME THE ARTIFACTS

Every signal you plan needs to produce a real file. Write the naming convention in strategy.md so anyone reading the plan knows exactly what file to look for.

```
## Artifact Naming Convention

Pattern: {topic}-{signal}-{date}.md
Example: {topic}-scout-feasibility-{date}.md

Every item name in the Signal Plan follows this pattern.
Parameterized templates are fine in the strategy file.
```

**Before you move on:**
- [ ] The Naming Convention section has its own heading in strategy.md
- [ ] The pattern is documented
- [ ] At least one parameterized example is shown

---

### PHASE 6 — CHECK YOUR PLAN BEFORE WRITING ROWS

Before you write a single signal row, verify that your planned signals can actually satisfy the schemas. This is your pre-write gate — clear it completely before moving to Phase 7.

- [ ] F-01: Every namespace you're planning is in the allowed set
- [ ] F-02: Every skill you're naming is specific, not just a namespace label
- [ ] F-03: Every item name you're planning fits `{topic}-{signal}-{date}.md`
- [ ] F-04: Every owner you're assigning corresponds to an S-N from your Phase 1 table
- [ ] F-05: Every priority you're assigning is exactly `essential`, `recommended`, or `optional`
- [ ] COV-01: At least one signal is going to be `essential`
- [ ] COV-02: At least two different namespaces are represented
- [ ] COV-03: At least two different S-N rows are going to be referenced as owners

---

### PHASE 7 — WRITE THE SIGNAL PLAN

Now write the signal plan table. Every row must pass F-01 through F-05. The full table must pass COV-01 through COV-03.

```
## Signal Plan

| Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
|-----------|-------|-----------|------------|-----------------|----------|
```

**After you've written the rows, check before moving to Phase 8:**
- [ ] Every row passes F-01 (valid namespace)
- [ ] Every row passes F-02 (named skill)
- [ ] Every row passes F-03 (item name follows convention)
- [ ] Every row passes F-04 (owner is an S-N from Phase 1)
- [ ] Every row passes F-05 (priority is essential / recommended / optional)
- [ ] The table passes COV-01 (>= 1 essential row)
- [ ] The table passes COV-02 (>= 2 distinct namespaces)
- [ ] The table passes COV-03 (>= 2 distinct S-N refs)

Don't move to Phase 8 until all of the above are checked.

---

### PHASE 8 — NAME THE COMMIT GATE

This is a separate phase from writing the signal rows. You've now produced the rows — here you name the mandatory minimum that must exist before design commit is permitted.

Write to `simulations/{topic}/strategy.md`:

```
## Commit Gate

Design commit requires the following signals to exist:
- {item-name-1} (essential)
- {item-name-2} (essential)
...

Gate condition: every signal listed above must be present before design commit proceeds.
```

**Before you're done:**
- [ ] At least 1 essential signal is named by its exact item name from Phase 7
- [ ] The gate condition is explicit — it names specific signals, not a general description
- [ ] The Commit Gate section has its own heading in strategy.md

---

---

## V-04 — Lifecycle Emphasis + Inertia Framing

**Axes**: Lifecycle emphasis + Inertia framing — the pipeline overview adds a "Without this phase" column that states the inertia failure mode for each phase; each phase opener carries a one-line inertia statement before its structural body.

**Hypothesis**: Embedding inertia consequences in the pipeline overview's "Without this phase" column creates a triple-layer gate: overview declaration (C-24), per-phase inline gate (C-21), and per-phase inertia consequence (C-14). The inertia column in the overview makes downstream harm visible architecturally, not just at the constraint level. The hypothesis is that this produces the strongest C-14 + C-24 co-satisfaction without prose bloat, because consequence framing lives in table cells rather than paragraphs.

---

### REGISTER A NEW TOPIC

#### PIPELINE OVERVIEW

All exit gates are declared here. All inertia failure modes are declared here. Read this entire table before executing any phase.

| Phase | Exit Gate | Without This Phase |
|-------|-----------|-------------------|
| 1 — Stakeholders | >= 3 rows; all 4 cols filled; roles specific | Owner roles in the signal plan default to generic labels; no cross-functional accountability |
| 2 — TOPICS.md | Row appended; status=active; path correct | Topic is invisible to the registry; strategy is unreachable from the index |
| 3 — Rationale | >= 2 sentences; design decision named | Strategy exists with no stated purpose; reviewers cannot evaluate whether the signal set is sufficient |
| 4 — Schemas | F-01..F-05 and COV-01..COV-03 present; both consequence tiers filled | Constraints drift to prose warnings; gate checkpoints have no authoritative source to cite |
| 5 — Naming | Pattern documented; parameterized example present | Artifact names are ad-hoc; signals cannot be located, scheduled, or committed |
| 6 — Pre-write | F-01..F-05 and COV-01..COV-03 checkable | Invalid rows enter the signal plan; violations are discovered after the strategy is in use |
| 7 — Signal Plan | F-01..F-05 per row; COV-01..COV-03 across rows; post-write gate clear | Signal plan exists with no structural verification; commit gate references may be inconsistent with actual rows |
| 8 — Commit Gate | >= 1 essential named by item name; gate condition explicit | Strategy has signal rows but no named stopping condition; design commit proceeds by default |

Do not advance past any phase until its exit gate is satisfied.

---

### PHASE 1 — STAKEHOLDERS

*Without this phase: signals default to a single owner role, cross-functional accountability disappears, and the signal plan reflects whoever spoke last.*

WHO BEARS THE RISK if this topic's strategy is wrong? Fill in this table as your first output.

| # | Stakeholder Role | Decision They Own | Risk If Strategy Fails |
|---|-----------------|-------------------|------------------------|
| S-01 | | | |
| S-02 | | | |
| S-03 | | | |
| ... | | | |

**Phase 1 exit gate:**
- [ ] >= 3 rows filled; all 4 columns populated
- [ ] Roles are specific (e.g., "PM", "tech lead") — not "user" or "stakeholder"
- [ ] Risk statements name concrete failure outcomes

---

### PHASE 2 — TOPICS.md ENTRY

*Without this phase: the topic exists only in this strategy file; it cannot be discovered from the registry or linked from downstream tools.*

Append one row to `simulations/TOPICS.md`:

| Topic | Status | Strategy Path |
|-------|--------|---------------|
| {topic} | active | simulations/{topic}/strategy.md |

**Phase 2 exit gate:**
- [ ] Row appended to `simulations/TOPICS.md`
- [ ] Status is exactly `active`
- [ ] Path is exactly `simulations/{topic}/strategy.md`

---

### PHASE 3 — RATIONALE

*Without this phase: the strategy is a bare signal list with no stated purpose; reviewers cannot determine whether the signal set is adequate for the decision it's meant to inform.*

Write to `simulations/{topic}/strategy.md`:

```
## Rationale

{>= 2 sentences explaining why this topic needs investigation
and which design decision this strategy informs}
```

**Phase 3 exit gate:**
- [ ] Rationale section exists in `simulations/{topic}/strategy.md`
- [ ] >= 2 sentences present
- [ ] The specific design decision is named

---

### PHASE 4 — CONSTRAINT SCHEMAS

*Without this phase: constraints live as prose instructions; gate checkpoints must restate rules rather than cite them, and drift between definition and enforcement is guaranteed.*

#### FIELD SCHEMA

| ID | Field | Rule | Immediate Failure | Downstream Effect |
|----|-------|------|-------------------|-------------------|
| F-01 | Namespace | One of: scout, draft, review, flow, trace, prove, listen, program, topic | Row rejected — no valid skill set mapping | Signal orphaned; team cannot find or produce it |
| F-02 | Skill | Specific skill within namespace — not the namespace itself | Row rejected — ambiguous or unresolvable | Signal never generated; gap invisible to planning |
| F-03 | Item Name | `{topic}-{signal}-{date}.md` (parameterized template acceptable) | Row rejected — artifact unlocatable | Signal untrackable; review and commit impossible |
| F-04 | Owner Role | S-N reference from Phase 1 Stakeholders table | Row rejected — owner unresolvable | Signal has no accountable owner; never produced |
| F-05 | Priority | Exactly: `essential` / `recommended` / `optional` — no substitutions | Strategy unparseable as commit gate | Team commits without a defined stopping condition |

#### COVERAGE SCHEMA

| ID | Rule | Threshold | Immediate Failure | Downstream Effect |
|----|------|-----------|-------------------|-------------------|
| COV-01 | At least one essential signal | >= 1 essential row | Strategy has no commit gate | No mandatory stopping condition before design commit |
| COV-02 | Multi-namespace coverage | >= 2 distinct namespaces | Single-perspective strategy | Entire risk categories absent from the investigation |
| COV-03 | Differentiated owner roles | >= 2 distinct S-N refs | All signals owned by one person | Single point of failure; cross-functional review blocked |

**Phase 4 exit gate:**
- [ ] F-01 through F-05 present; Immediate Failure + Downstream Effect populated for each
- [ ] COV-01 through COV-03 present; Immediate Failure + Downstream Effect populated for each

---

### PHASE 5 — ARTIFACT NAMING CONVENTION

*Without this phase: signal item names are ad-hoc; artifacts cannot be systematically located, and reviewers cannot verify whether a signal exists.*

Write to `simulations/{topic}/strategy.md`:

```
## Artifact Naming Convention

Pattern: {topic}-{signal}-{date}.md
Example: {topic}-scout-feasibility-{date}.md

All signal item names in the Signal Plan follow this pattern.
```

**Phase 5 exit gate:**
- [ ] Naming Convention section has its own heading in strategy.md
- [ ] Pattern documented
- [ ] At least one parameterized example present

---

### PHASE 6 — PRE-WRITE VERIFICATION

*Without this phase: invalid rows enter the signal plan silently; violations surface during strategy use, not during production.*

Verify before writing any signal rows:

- [ ] F-01: planned namespaces are all in the allowed set
- [ ] F-02: planned skills are all named specifically
- [ ] F-03: planned item names are all expressible as `{topic}-{signal}-{date}.md`
- [ ] F-04: every planned owner role corresponds to an S-N row from Phase 1
- [ ] F-05: all planned priority values are exactly `essential` / `recommended` / `optional`
- [ ] COV-01: >= 1 essential signal planned
- [ ] COV-02: >= 2 distinct namespaces planned
- [ ] COV-03: >= 2 distinct S-N refs planned

---

### PHASE 7 — SIGNAL PLAN

*Without post-write verification: signal rows can be written that violate F-01..F-05 or fail COV-01..COV-03, and the commit gate in Phase 8 would reference a non-compliant plan.*

**Entry gate:** Phase 6 exit gate must be clear before writing rows.

Write to `simulations/{topic}/strategy.md`:

```
## Signal Plan

| Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
|-----------|-------|-----------|------------|-----------------|----------|
```

**Phase 7 exit gate** (verify after writing rows, before advancing to Phase 8):
- [ ] F-01 through F-05 pass for every row
- [ ] COV-01 through COV-03 pass across the full set

---

### PHASE 8 — COMMIT GATE

*Without this phase: the strategy has a signal list but no stopping condition; teams commit based on feel rather than defined evidence.*

This is a dedicated phase separate from signal row production. Name the minimum evidence required before design commit.

Write to `simulations/{topic}/strategy.md`:

```
## Commit Gate

Design commit requires the following signals to exist:
- {item-name-1} (essential)
- {item-name-2} (essential)
...

Gate condition: all listed signals must be present before design commit proceeds.
```

**Phase 8 exit gate:**
- [ ] >= 1 essential signal named by exact item name from Phase 7
- [ ] Gate condition explicit (specific named signals, not a general threshold)
- [ ] Commit Gate has its own dedicated heading in strategy.md

---

---

## V-05 — Output Format + Role Sequence + Inertia Framing

**Axes**: Output format (ID-citation-only gates) + Role sequence (stakeholder table is explicitly named as the source of all schema F-04 values, wired through the overview table's role-sequence declaration) + Inertia framing (pipeline overview "Without this phase" column; inertia opener per phase).

**Hypothesis**: Combining schema-ID-only gate notation with a role-sequence-explicit pipeline (the overview table cites S-N sourcing for F-04) and per-phase inertia openers creates the most mechanically complete prompt in the set. The F-04 row explicitly states that owner roles derive from the Phase 1 table, and the pre-write gate's F-04 checkbox enforces it — making role differentiation C-08 structurally satisfiable by schema inspection rather than by counting distinct values across the output. The hypothesis is that this triple combination produces higher signal plan quality on adversarial inputs (inputs with ambiguous owner roles) because the mechanical coupling leaves no room for role-defaulting.

---

### REGISTER A NEW TOPIC

#### PIPELINE OVERVIEW

Read this table completely before Phase 1. All gate conditions declared here. All inertia failure modes declared here.

| Phase | Gate | Without This Phase |
|-------|------|--------------------|
| 1 — Stakeholders → S-N keys | >= 3 rows; 4 cols filled; roles specific | F-04 has no valid source; all owner roles are unresolvable; C-08 cannot be satisfied |
| 2 — TOPICS.md row | Row appended; status=active; path correct | Topic is not registered; strategy is disconnected from the index |
| 3 — Rationale | >= 2 sentences; design decision named | Strategy purpose is implicit; reviewers cannot evaluate signal adequacy |
| 4 — F-01..F-05 + COV-01..COV-03 | All 8 rows present; both consequence tiers filled | Gate checkpoints in Phases 6–7 have no canonical source to cite; rules drift |
| 5 — Naming Convention | Pattern documented; example present | Item names are ad-hoc; artifacts untrackable |
| 6 — Pre-write: F-01..F-05, COV-01..COV-03 | All schema IDs checkable | Invalid rows enter Phase 7 silently |
| 7 — Signal Plan rows | F-01..F-05 per row; COV-01..COV-03 across rows; post-write clear | Rows unverified; Phase 8 commit gate cites a non-validated plan |
| 8 — Commit Gate | >= 1 essential named by item name; condition explicit | Signal plan has no stopping condition; design commit proceeds by default |

---

### PHASE 1 — STAKEHOLDERS

*Without this phase: F-04 (Owner Role) has no valid source. Every signal row's owner field is unresolvable. C-08 cannot be satisfied by schema inspection.*

This table is the source of truth for all owner roles in the signal plan. S-N keys assigned here are the only valid values for F-04.

| # | Role | Decision Owned | Risk If Strategy Fails |
|---|------|----------------|------------------------|
| S-01 | | | |
| S-02 | | | |
| S-03 | | | |
| ... | | | |

- [ ] >= 3 rows; all 4 cols filled; roles specific (not "user")
- [ ] Each risk names a concrete failure outcome

---

### PHASE 2 — TOPICS.md

*Without this phase: the topic is invisible to every tool that reads the registry.*

Append: `{topic} | active | simulations/{topic}/strategy.md`

- [ ] Row in `simulations/TOPICS.md`; status=active; path=`simulations/{topic}/strategy.md`

---

### PHASE 3 — RATIONALE

*Without this phase: no stated purpose; reviewers cannot determine if the signal set is adequate.*

```
## Rationale
{>= 2 sentences; name the design decision this strategy informs}
```

- [ ] >= 2 sentences; design decision named

---

### PHASE 4 — SCHEMAS

*Without this phase: gate checkpoints in Phases 6–7 must restate rules in prose; drift between definition and enforcement is inevitable.*

#### FIELD SCHEMA

| ID | Field | Rule | Immediate Failure | Downstream Effect |
|----|-------|------|-------------------|-------------------|
| F-01 | Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | Row rejected — no skill set mapping | Signal orphaned |
| F-02 | Skill | Named specific skill within namespace | Row rejected — ambiguous | Signal never produced |
| F-03 | Item Name | `{topic}-{signal}-{date}.md` template | Row rejected — unlocatable | Signal untrackable |
| F-04 | Owner Role | S-N reference from Phase 1 table (the ONLY valid source) | Row rejected — unresolvable owner | Signal has no accountable owner; never produced |
| F-05 | Priority | `essential` / `recommended` / `optional` only | Strategy unparseable as commit gate | Team commits without stopping condition |

#### COVERAGE SCHEMA

| ID | Rule | Threshold | Immediate Failure | Downstream Effect |
|----|------|-----------|-------------------|-------------------|
| COV-01 | Essential signal exists | >= 1 essential row | No commit gate | No mandatory stopping condition |
| COV-02 | Multi-namespace | >= 2 distinct namespaces | Single-perspective | Risk categories unseen |
| COV-03 | Multi-owner | >= 2 distinct S-N refs | Single point of ownership | Cross-functional coverage absent |

- [ ] F-01..F-05 all present; Immediate Failure + Downstream Effect filled
- [ ] COV-01..COV-03 all present; Immediate Failure + Downstream Effect filled

---

### PHASE 5 — NAMING CONVENTION

*Without this phase: item names in Phase 7 are ad-hoc; F-03 cannot be verified.*

```
## Artifact Naming Convention
Pattern: {topic}-{signal}-{date}.md
Example: {topic}-scout-feasibility-{date}.md
```

- [ ] Pattern documented; parameterized example present; own heading in strategy.md

---

### PHASE 6 — PRE-WRITE

*Without this phase: invalid rows enter Phase 7 silently; violations surface after strategy is in use.*

- [ ] F-01: namespaces in allowed set
- [ ] F-02: skills named specifically
- [ ] F-03: item names fit `{topic}-{signal}-{date}.md`
- [ ] F-04: all owners are S-N from Phase 1 table
- [ ] F-05: all priorities are essential / recommended / optional
- [ ] COV-01: >= 1 essential planned
- [ ] COV-02: >= 2 namespaces planned
- [ ] COV-03: >= 2 distinct S-N refs planned

---

### PHASE 7 — SIGNAL PLAN

*Without post-write gate: rows can violate F-01..F-05 or fail COV-01..COV-03 before Phase 8 cites them.*

**Entry gate:** Phase 6 exit gate clear.

```
## Signal Plan

| Namespace | Skill | Item Name | Owner Role | Stakeholder Ref | Priority |
|-----------|-------|-----------|------------|-----------------|----------|
```

**Exit gate** (after writing rows, before Phase 8):
- [ ] F-01..F-05 pass for every row
- [ ] COV-01..COV-03 pass across the full set

---

### PHASE 8 — COMMIT GATE

*Without this phase: signal rows exist but no stopping condition is named; design commit proceeds by default.*

This phase is separate from signal row production. Phase 7 owns rows. Phase 8 owns the named stopping condition.

**Entry gate:** Phase 7 exit gate clear.

```
## Commit Gate

Design commit requires:
- {item-name} (essential)
...
Gate condition: all listed signals must exist before design commit proceeds.
```

**Exit gate:**
- [ ] >= 1 essential named by exact item name from Phase 7
- [ ] Condition explicit (named signals, not a general description)
- [ ] Commit Gate has its own dedicated heading in strategy.md

---

---

## Variation Summary

| Variation | Axis | Hypothesis | C-23 | C-24 | C-25 |
|-----------|------|------------|------|------|------|
| V-01 | Lifecycle emphasis | 3-column overview (Purpose + Produces + Exit Gate) maximizes architectural clarity | F-N/COV-N IDs + gate citations | Pipeline overview table with Purpose/Produces/Exit Gate before Phase 1 | Phase 7 signal rows + Phase 8 commit gate as separate phases |
| V-02 | Output format | ID-only gate checkboxes (no prose restatement) minimize length without reducing structural compliance | F-N/COV-N IDs; gates cite IDs only (e.g., "F-01..F-05 pass") | Minimal 2-column overview (Phase + Exit Gate) before Phase 1 | Phase 7 entry gate + exit gate; Phase 8 as own phase with entry/exit |
| V-03 | Phrasing register | Conversational register ("Here's what you do") does not degrade structural compliance | F-N/COV-N IDs; gates cite IDs in conversational framing | 4-column overview (Phase + What + Produces + You can move on when) before Phase 1 | Phase 7 "after you've written the rows" gate; Phase 8 as dedicated "separate phase" |
| V-04 | Lifecycle + Inertia | "Without this phase" column in overview co-satisfies C-14 + C-24 architecturally | F-N/COV-N IDs + gate citations | 3-column overview with inertia "Without this phase" column before Phase 1 | Phase 7 entry + exit gates; Phase 8 as dedicated phase with inertia opener |
| V-05 | Output format + Role sequence + Inertia | Role-sequence-explicit pipeline (F-04 sourcing declared in overview) + ID-only gates + inertia framing produces strongest adversarial-input compliance | F-N/COV-N IDs; ID-only gates | 3-column overview (Phase + Gate + Without this phase) before Phase 1 | Phase 7 entry + exit gates; Phase 8 as own phase with "separate from Phase 7" declaration |

**Key structural properties all 5 share:**
- Pipeline overview table before Phase 1 (C-24)
- FIELD SCHEMA rows F-01..F-05 with stable IDs; COVERAGE SCHEMA rows COV-01..COV-03 with stable IDs (C-23)
- Gate checkboxes cite F-N/COV-N IDs rather than restating prose (C-23)
- Phase 7 has both entry gate (before writing rows) and exit gate (after writing rows) (C-21, C-25)
- Phase 8 is a dedicated phase separate from Phase 7 signal plan production (C-25)
- Stakeholders fill-in table as Phase 1 first output with >= 3 row gate (C-17, C-22)
- Temporally layered consequence columns in both schemas (C-20)

**V-02 most likely to surface a C-21 failure** if the ID-only gate notation is not recognized as satisfying the "named condition" requirement — the scorer should check whether `- [ ] F-01..F-05 pass` qualifies as a named exit gate per the C-21 pass condition.
