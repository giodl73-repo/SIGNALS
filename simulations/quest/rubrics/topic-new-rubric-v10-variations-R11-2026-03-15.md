# /quest:variate — topic-new Round 11 (v10 rubric baseline)

Round 11 variations. Baseline: all 34 criteria (C-01–C-34) are structural invariants across all
five variations. C-32, C-33, C-34 (the three R10 elevations) are embedded in every variation.

Exploration targets for R11 (candidates for C-35/C-36/C-37):
- **ES-3 from R10**: Behavioral inertia framing — "Status-Quo Default (if phase skipped)"
- **New axis — Role sequence**: Consumer-anchored signal planning (who uses each signal decides priority)
- **New axis — Lifecycle emphasis**: Phase handoff artifact tracking (phases verified by artifact presence)

Variation axes selected (3 single-axis, then combine):
1. Inertia framing — how prominently the status-quo behavioral default is named
2. Role sequence — producer+consumer anchoring before priority assignment
3. Lifecycle emphasis — phase handoff artifacts as entry requirements

---

## V-01 — Inertia Framing: Behavioral-Default Consequence Column

**Variation axis**: Inertia framing — the pipeline overview carries two consequence columns: the
existing first-person "If I Skip This Phase, I Will..." column (C-32) plus a new "Team Default When
I Skip This" column that names the specific organizational behavior that fills the vacuum when each
phase is skipped. Skip-cost is stated twice: as a self-attributed personal failure and as a named
team behavioral default the executing model must actively override.

**Hypothesis**: First-person consequence framing (C-32) makes skip-cost self-attributed but
describes a hypothetical future state. "Team Default When I Skip This" names an *already-existing*
behavior that the phase is competing against — making the skip choice not "will I cause a failure?"
but "will I enact the default that is already waiting?" The named default raises the cost of
skipping by making inertia explicit rather than implicit.

---

You are registering a new topic for the Signal plugin and producing a complete investigation
strategy. Every constraint applies to you as the executing model. Read the FIELD SCHEMA before the
pipeline overview.

---

### FIELD SCHEMA — Read first. Schema row order defines signal table column order.

**Schema row order = table column order. F-01=Priority is column 1 of every signal table. A column
order change requires a schema row sequence change first.**

| ID | Field | Canonical Values | If I Violate This, I Will... |
|----|-------|-----------------|------------------------------|
| F-01 | Priority | essential / recommended / optional | ...write "high/medium/low" and produce a strategy that fails C-04 and cannot be rubric-scored |
| F-02 | Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | ...route signals to a nonexistent namespace, breaking downstream invocation |
| F-03 | Skill | skill name within namespace | ...name an uninvokable skill no team member can execute |
| F-04 | Item Name | {topic}-{signal}-{date}.md | ...create an artifact the registry cannot locate |
| F-05 | Owner Role | role responsible for executing this skill | ...produce signals with no execution owner — they will never be produced |

Signal table column order: **Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04)
| Owner Role (F-05)**

---

### PIPELINE OVERVIEW — I will read every row completely before executing Phase 0.

| Phase | Purpose | Produces | Exit Gate | If I Skip This Phase, I Will... | Team Default When I Skip This |
|-------|---------|---------|----------|--------------------------------|-------------------------------|
| 0 | Confirm inputs | Validated topic name + description | I have confirmed both inputs | ...produce a strategy for an unnamed feature — I will have registered nothing | Teams name features in the moment and write strategies without an anchoring description |
| 1 | Identify stakeholders | Stakeholder table ≥ 3 complete rows | I have ≥ 3 rows with all cells filled | ...assign owner roles with no traceability to real concerns — I will have fabricated an execution path | Teams assign all signals to whoever called the meeting |
| 2 | Plan signals | Signal table, schema-ordered, ≥ 1 essential | I have ≥ 1 essential, all cells complete | ...leave the feature with no implied commit gate — I will have produced an unactionable strategy | Teams treat the first four signals mentioned in conversation as the complete list |
| 3 | Commit gate | Pass/return decision | I have independently verified both conditions | ...write a false readiness record into TOPICS.md — I will have attested to a strategy that has not passed its own gates | Teams advance to implementation after a quick visual scan of the signal list |
| 4 | Write outputs | TOPICS.md entry + strategy.md | I have written both files at the correct paths | ...leave the topic unregistered — I will have completed the skill with no durable artifact | Teams keep strategies in personal notes that no other skill can reference |

I will not execute Phase 0 until I have processed every row including both consequence columns.

---

### PHASE 0 — INPUT VALIDATION

I will confirm both inputs before proceeding:
- Topic name: {topic}
- Topic description: {description}

**Check these two items independently. I will not advance to Phase 1 until both are confirmed
separately:**
- [ ] Topic name is present and non-empty
- [ ] Topic description is present and non-empty

**Do not advance until both boxes are checked independently.**

**If I check these sequentially:** confirming the topic name may lead me to treat the description as
implicitly present. I will advance to Phase 1 with a missing description — every stakeholder concern
I identify will float free of any feature scope. Teams name features in the moment and skip scope
definition; I will have done the same.

---

### PHASE 1 — STAKEHOLDER IDENTIFICATION

I will identify stakeholders most affected by this feature decision.

| Stakeholder | Concern | Signals-at-Risk |
|-------------|---------|----------------|

**Check these two items independently. I will not advance to Phase 2 until both are satisfied
separately:**
- [ ] I have at least 3 rows in the stakeholder table
- [ ] Every cell in every row is complete — no empty cells

**Do not advance until both boxes are checked independently.**

**If I check these sequentially:** a table with 3 rows where Concern and Signals-at-Risk cells are
empty satisfies the row-count check. I will advance with 3 stakeholder names and nothing else. The
owner roles I assign in Phase 2 will have no traceability to any concern. Teams assign all signals
to whoever called the meeting when stakeholder concerns are absent; I will have produced the
structural equivalent.

---

### PHASE 2 — SIGNAL PLANNING

I will plan the signals needed for design commit. Column order follows FIELD SCHEMA — **schema row
order = table column order, F-01=Priority first**.

Priority vocabulary: **essential / recommended / optional only**. "High/medium/low" fails C-04.

| Priority | Namespace | Skill | Item Name | Owner Role |
|----------|-----------|-------|-----------|------------|

I will include at least one essential signal. I will assign different Owner Role values where
signals require different expertise.

**Check these two items independently. I will not advance to Phase 3 until both are satisfied
separately:**
- [ ] At least one row has Priority = essential
- [ ] All cells in every row are complete — no empty cells

**Do not advance until both boxes are checked independently.**

**If I check these sequentially:** confirming essential-signal presence may lead me to treat cell
completeness as already verified by the act of filling. I will advance with rows that have Priority
filled but Item Name or Owner Role cells empty. Teams treat the first four signals mentioned as the
complete list; incomplete cells are the structural equivalent.

---

### PHASE 3 — COMMIT GATE

I will not write any output until both conditions are independently satisfied.

**Check these two items independently. I will not advance to Phase 4 until both are verified
separately:**
- [ ] [F-01] At least one row has Priority = essential
- [ ] [F-05] At least two distinct Owner Role values appear in the table

**Do not advance until both boxes are checked independently.**

**If I check these sequentially:** confirming the essential-signal condition may lead me to
rationalize that any populated table satisfies the role condition. I will advance past a strategy
where every signal shares the same owner role. Teams advance after a quick visual scan and declare
themselves ready; I will have done the same, attesting to readiness I have not verified.

If either condition fails, I return to Phase 2 and revise.

---

### PHASE 4 — OUTPUT PRODUCTION

I will write both artifacts.

**TOPICS.md entry** — append to `simulations/TOPICS.md`:
```
## {topic}
{description}
Strategy: simulations/{topic}/strategy.md
Signals: {n} planned ({e} essential, {r} recommended, {o} optional)
```

**strategy.md** — write to `simulations/{topic}/strategy.md`:
```markdown
# {topic} — Signal Strategy
{description}

## Rationale
{Why these signals? What decision do they inform? What team default does this investigation override?}

## Stakeholders
| Stakeholder | Concern | Signals-at-Risk |
{rows from Phase 1}

## Signals
| Priority | Namespace | Skill | Item Name | Owner Role |
{rows from Phase 2}

## Commit Gate
Before advancing to implementation:
- [ ] All essential signals produced
- [ ] All owner roles confirmed
- [ ] Strategy covers full topic description scope
```

---

## V-02 — Role Sequence: Consumer-Anchored Signal Planning

**Variation axis**: Role sequence — Phase 2 requires the executing model to identify both a
Producer role and a Consumer role for each signal. Consumer is named before Priority is assigned.
F-05 becomes "Producer → Consumer" format. Priority vocabulary is anchored to the consumer's
decision dependency at fill time: essential = consumer cannot decide without it; recommended =
strengthens the decision; optional = decision proceeds without it.

**Hypothesis**: Assigning priority after naming the consumer role converts priority from an
intuitive ranking ("this feels important") to a decision-dependency classification ("this decision
cannot be made without this signal"). When the consuming decision-maker is named first, C-04
vocabulary substitution becomes structurally harder — "high/medium/low" has no mapping to "cannot
decide / strengthens / optional," whereas "essential/recommended/optional" does. Priority vocabulary
is grounded in an observable relationship at the moment of assignment rather than enforced only by
downstream rubric check.

---

You are registering a new topic for the Signal plugin. Your investigation strategy must be
actionable: every signal needs someone who produces it and someone who uses it to make a decision.
Read the FIELD SCHEMA first.

---

### FIELD SCHEMA — Read first. Schema row order defines signal table column order.

**Schema row order = table column order. F-01=Priority is column 1 of every signal table. A column
order change requires a schema row sequence change first.**

| ID | Field | Canonical Values | Violation Consequence |
|----|-------|-----------------|----------------------|
| F-01 | Priority | essential / recommended / optional | Vocabulary substitution (high/medium/low) fails C-04 and breaks rubric scoring |
| F-02 | Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | Invalid namespace breaks artifact routing |
| F-03 | Skill | skill name within namespace | Invented skill breaks invocation contract |
| F-04 | Item Name | {topic}-{signal}-{date}.md | Malformed name breaks registry lookup |
| F-05 | Producer → Consumer | "{role} → {role}" — who executes the skill and who uses the signal to decide | No consumer = no decision dependency — priority assignment floats free of actual value |

Signal table column order: **Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04)
| Producer → Consumer (F-05)**

---

### PIPELINE OVERVIEW — Read completely before executing Phase 0.

| Phase | Purpose | Produces | Exit Gate | If I Skip This Phase, I Will... |
|-------|---------|---------|----------|--------------------------------|
| 0 | Confirm inputs | Validated topic + description | Both inputs confirmed | ...produce a strategy for an unnamed feature — the artifact will be unroutable |
| 1 | Identify decisions and stakeholders | Decision table (≥ 3) + stakeholder table (≥ 3 rows) | Both tables complete | ...plan signals without anchoring to any real decision — priority assignments will be intuitive, not decision-grounded |
| 2 | Plan signals | Signal table, schema-ordered, each with Producer → Consumer | ≥ 1 essential, all F-05 cells in "X → Y" format | ...produce signals with no consumer named — "essential" and "optional" become meaningless labels |
| 3 | Commit gate | Pass/return decision | Both conditions independently satisfied | ...write a false readiness record — I will have attested to a strategy that has not passed its own gates |
| 4 | Write outputs | TOPICS.md entry + strategy.md | Both files at correct paths | ...leave the topic unregistered — no other skill can build on these signals |

I will not execute Phase 0 until I have processed every row in this table.

---

### PHASE 0 — INPUT VALIDATION

Confirm both inputs. Do not advance to Phase 1 until both are present.
- Topic name: {topic}
- Topic description: {description}

**Check these two items independently. Do not advance to Phase 1 until both are confirmed
separately:**
- [ ] Topic name is present and non-empty
- [ ] Topic description is present and non-empty

**Do not advance until both boxes are checked independently.**

**If checked sequentially:** confirming the topic name may lead you to treat description as
implicitly present. Phase 1 will have no scope to anchor decisions to — every decision identified
will float free of any feature boundary.

---

### PHASE 1 — DECISION AND STAKEHOLDER IDENTIFICATION

Identify decisions first. Signal planning in Phase 2 anchors consumer roles to this table.

**Decision table — run first:**
| Decision | Decision-Maker Role | What Signal Makes This Decidable |
|----------|---------------------|----------------------------------|

**Stakeholder table — run second:**
| Stakeholder | Concern | Signals-at-Risk |
|-------------|---------|----------------|

**Check these four items independently. Do not advance to Phase 2 until all four are satisfied
separately:**
- [ ] Decision table has at least 3 rows
- [ ] Every cell in the decision table is complete
- [ ] Stakeholder table has at least 3 rows
- [ ] Every cell in the stakeholder table is complete

**Do not advance until all four boxes are checked independently.**

**If checked sequentially:** completing the row-count checks may cause you to treat cell completeness
as already verified. You will advance with decision-maker roles named but no "What Signal Makes This
Decidable" mapping — Phase 2 has consumer names but no basis for assigning essential vs. recommended,
because no signal has been traced to any decision.

---

### PHASE 2 — SIGNAL PLANNING

Column order follows FIELD SCHEMA — **schema row order = table column order, F-01=Priority first**.

For each signal, name the Consumer before assigning Priority. Priority maps to decision dependency:
- **essential** — the consumer's decision cannot be made without this signal
- **recommended** — this signal strengthens the decision but is not blocking
- **optional** — the decision proceeds without this signal; this is supplementary

Priority vocabulary: **essential / recommended / optional only**. "High/medium/low" fails C-04.

| Priority | Namespace | Skill | Item Name | Producer → Consumer |
|----------|-----------|-------|-----------|---------------------|

Consumer role in F-05 must appear in the Phase 1 decision table.

**Check these two items independently. Do not advance to Phase 3 until both are satisfied
separately:**
- [ ] At least one row has Priority = essential
- [ ] Every F-05 cell contains "X → Y" format with both producer and consumer named

**Do not advance until both boxes are checked independently.**

**If checked sequentially:** confirming essential-signal presence may lead you to treat F-05
completeness as already verified. You will advance with F-05 cells that name only a producer — the
decision-dependency chain is severed, and essential/recommended/optional become intuitive labels
without operational referents.

---

### PHASE 3 — COMMIT GATE

Do not write any output until both conditions are independently satisfied.

**Check these two items independently. Do not advance to Phase 4 until both are verified separately:**
- [ ] [F-01] At least one row has Priority = essential
- [ ] [F-05] At least two distinct Consumer roles appear — signals reach at least two different
  decision-makers

**Do not advance until both boxes are checked independently.**

**If checked sequentially:** confirming the essential-signal condition may lead you to rationalize
consumer diversity as already present. You will advance past a strategy where every signal feeds
the same decision-maker — the strategy has a commit gate but no distributed decision value. One
role controls all signal consumption, and no peer can independently validate coverage.

If either condition fails, return to Phase 2 and revise.

---

### PHASE 4 — OUTPUT PRODUCTION

Write both artifacts.

**TOPICS.md entry** — append to `simulations/TOPICS.md`:
```
## {topic}
{description}
Strategy: simulations/{topic}/strategy.md
Signals: {n} planned ({e} essential, {r} recommended, {o} optional)
```

**strategy.md** — write to `simulations/{topic}/strategy.md`:
```markdown
# {topic} — Signal Strategy
{description}

## Rationale
{Why these signals? What decisions do they enable? What competing interpretation does this
investigation distinguish against?}

## Decisions
| Decision | Decision-Maker Role | What Signal Makes This Decidable |
{rows from Phase 1 decision table}

## Stakeholders
| Stakeholder | Concern | Signals-at-Risk |
{rows from Phase 1 stakeholder table}

## Signals
| Priority | Namespace | Skill | Item Name | Producer → Consumer |
{rows from Phase 2}

## Commit Gate
Before advancing to implementation:
- [ ] All essential signals produced and delivered to consumer roles
- [ ] All consumer roles confirmed their signals
- [ ] Strategy covers full topic description scope
```

---

## V-03 — Lifecycle Emphasis: Phase Handoff Artifacts

**Variation axis**: Lifecycle emphasis — each phase is defined by its handoff artifact: the specific
table or record it passes to the next phase as its entry input. PIPELINE OVERVIEW includes a
"Handoff Artifact" column. Entry to each phase requires confirming the previous phase's handoff
artifact is present and complete. A phase is not done because it was executed — it is done because
its handoff artifact exists.

**Hypothesis**: Phase-completion defined by artifact presence rather than execution self-report
eliminates the failure mode where a phase is partially executed but reported as complete. Each
gate becomes: "I have the previous phase's artifact." This makes phase-skipping detectable by
artifact absence rather than by gate override — a model cannot claim to be at Phase 3 if the
Phase 2 signal table does not exist. The handoff-artifact column also makes the pipeline's
information flow visible architecturally before execution begins.

---

You are registering a new topic for the Signal plugin. Read the FIELD SCHEMA before the pipeline
overview. A phase is complete when its handoff artifact is present and complete.

---

### FIELD SCHEMA — Read first. Schema row order defines signal table column order.

**Schema row order = table column order. F-01=Priority is column 1 of every signal table. A column
order change requires a schema row sequence change first.**

| ID | Field | Canonical Values | Violation Consequence |
|----|-------|-----------------|----------------------|
| F-01 | Priority | essential / recommended / optional | Vocabulary substitution fails C-04 |
| F-02 | Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | Invalid namespace breaks routing |
| F-03 | Skill | skill name within namespace | Invented skill breaks invocation |
| F-04 | Item Name | {topic}-{signal}-{date}.md | Malformed name breaks registry |
| F-05 | Owner Role | role responsible for executing this skill | No owner = no execution path |

Signal table column order: **Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04)
| Owner Role (F-05)**

---

### PIPELINE OVERVIEW — Read completely before executing Phase 0.

| Phase | Purpose | Handoff Artifact | Exit Gate | If I Skip This Phase, I Will... |
|-------|---------|-----------------|----------|--------------------------------|
| 0 | Confirm inputs | Confirmed-inputs record (topic name + description, both non-empty) | Handoff artifact present | ...pass Phase 1 a strategy that has no name and no scope — Phase 1 has nothing to anchor stakeholders to |
| 1 | Identify stakeholders | Stakeholder table (≥ 3 rows, all cells complete) | Handoff artifact present | ...pass Phase 2 a signal plan with no owner-role anchors — every owner assigned will be fabricated |
| 2 | Plan signals | Signal table (schema-ordered, ≥ 1 essential, all cells complete) | Handoff artifact present | ...pass Phase 3 an empty or partial signal list — the commit gate has no table to verify |
| 3 | Commit gate | Gate decision record (both conditions passed, or return directive) | Handoff artifact present | ...begin output production before the strategy has cleared its own gates — false readiness |
| 4 | Write outputs | TOPICS.md entry + strategy.md at correct paths | Both files written | ...leave the topic unregistered — the investigation has no durable entry point |

I will not execute Phase 0 until I have processed every row including the Handoff Artifact column.

**Handoff-artifact rule:** Before beginning any phase, I confirm the previous phase's handoff
artifact is present and complete. Execution of a phase does not substitute for presence of its
handoff artifact.

---

### PHASE 0 — INPUT VALIDATION

**Handoff artifact to produce:** Confirmed-inputs record — topic name and description, both non-empty.

- Topic name: {topic}
- Topic description: {description}

**Check these two items independently. Do not advance to Phase 1 until both are confirmed
separately:**
- [ ] Topic name is present and non-empty
- [ ] Topic description is present and non-empty

**Do not advance until both boxes are checked independently.**

**If checked sequentially:** confirming the topic name may lead you to treat the description as
present by implication. Phase 1 will receive a confirmed-inputs record with a missing description.
Every stakeholder concern identified will float free of any feature scope — Phase 2 inherits an
unanchored stakeholder table.

---

### PHASE 1 — STAKEHOLDER IDENTIFICATION

**Entry requirement:** Phase 0 handoff artifact (confirmed-inputs record) is present and complete.
Confirm before beginning.

**Handoff artifact to produce:** Stakeholder table with ≥ 3 rows and all cells complete. This is
Phase 2's owner-role source — if absent or incomplete, Phase 2 has no anchor for owner assignment.

| Stakeholder | Concern | Signals-at-Risk |
|-------------|---------|----------------|

**Check these two items independently. Do not advance to Phase 2 until both are satisfied
separately:**
- [ ] I have at least 3 rows in the stakeholder table
- [ ] Every cell in every row is complete — no empty cells

**Do not advance until both boxes are checked independently.**

**If checked sequentially:** a table with 3 rows where Concern and Signals-at-Risk cells are empty
satisfies the row-count condition. Phase 2 receives a stakeholder table that is structurally present
but informationally empty — owner roles assigned will have no traceability to any concern, and the
handoff artifact is incomplete even though the table exists.

---

### PHASE 2 — SIGNAL PLANNING

**Entry requirement:** Phase 1 handoff artifact (complete stakeholder table) is present and
complete. Confirm before beginning.

**Handoff artifact to produce:** Signal table, schema-ordered, all cells complete, ≥ 1 essential.
This is Phase 3's verification input — Phase 3 cannot gate on a table that does not exist.

Column order follows FIELD SCHEMA — **schema row order = table column order, F-01=Priority first**.

Priority vocabulary: **essential / recommended / optional only**. "High/medium/low" fails C-04.

| Priority | Namespace | Skill | Item Name | Owner Role |
|----------|-----------|-------|-----------|------------|

**Check these two items independently. Do not advance to Phase 3 until both are satisfied
separately:**
- [ ] At least one row has Priority = essential
- [ ] All cells in every row are complete — no empty cells

**Do not advance until both boxes are checked independently.**

**If checked sequentially:** confirming essential-signal presence may lead you to treat cell
completeness as already verified. Phase 3 will receive a signal table with empty cells — the commit
gate will find column gaps but there is no clean return point, because Phase 2 has been marked
complete.

---

### PHASE 3 — COMMIT GATE

**Entry requirement:** Phase 2 handoff artifact (complete signal table) is present and complete.
Confirm before beginning.

**Handoff artifact to produce:** Gate decision record — both conditions passed (advance to Phase 4)
or return directive (return to Phase 2 and revise).

Do not write any output until both conditions are independently satisfied.

**Check these two items independently. Do not advance to Phase 4 until both are verified separately:**
- [ ] [F-01] At least one row has Priority = essential
- [ ] [F-05] At least two distinct Owner Role values appear in the table

**Do not advance until both boxes are checked independently.**

**If checked sequentially:** confirming the essential-signal condition may lead you to accept the
role condition as implicitly satisfied. You will advance to Phase 4 with a strategy where every
signal shares the same owner — the handoff artifact will be a gate decision record that attests to
readiness that was not fully verified.

If either condition fails, return to Phase 2 and revise the signal table.

---

### PHASE 4 — OUTPUT PRODUCTION

**Entry requirement:** Phase 3 handoff artifact (gate decision record, both conditions passed) is
present. Confirm before beginning.

Write both artifacts.

**TOPICS.md entry** — append to `simulations/TOPICS.md`:
```
## {topic}
{description}
Strategy: simulations/{topic}/strategy.md
Signals: {n} planned ({e} essential, {r} recommended, {o} optional)
```

**strategy.md** — write to `simulations/{topic}/strategy.md`:
```markdown
# {topic} — Signal Strategy
{description}

## Rationale
{Why these signals? What design decision do they inform? What alternative approach does this
investigation distinguish against?}

## Stakeholders
| Stakeholder | Concern | Signals-at-Risk |
{rows from Phase 1}

## Signals
| Priority | Namespace | Skill | Item Name | Owner Role |
{rows from Phase 2}

## Commit Gate
Before advancing to implementation:
- [ ] All essential signals produced
- [ ] All owner roles confirmed
- [ ] Strategy covers full topic description scope
```

---

## V-04 — Combination: Inertia Framing × Lifecycle Emphasis (V-01 + V-03)

**Variation axis**: Inertia framing × lifecycle emphasis — behavioral-default consequence column
(V-01: "Team Default When I Skip This") combined with phase handoff artifact tracking (V-03: phase
entry requires previous phase's artifact). The pipeline overview carries both consequence columns.
Every phase gate confirms artifact presence before checking conditions.

**Hypothesis**: Behavioral-default framing (V-01) and handoff-artifact tracking (V-03) close two
independent skip-rationalization pathways. V-01 raises the motivational cost of skipping by naming
the behavioral default that will fill the vacuum — making inertia explicit. V-03 raises the
mechanical cost of skipping by making phase-completion detectable by artifact presence — so a phase
cannot be silently reported as complete if its artifact is absent. A model that encounters both
knows not only *what it is doing* when it skips (enacting the named default) but also *that the
skip is detectable* (the artifact will be missing). These are independent deterrents that compound.

---

You are registering a new topic for the Signal plugin. Read the FIELD SCHEMA first. A phase is
complete when its handoff artifact is present and complete — not when you believe you have executed
it.

---

### FIELD SCHEMA — Read first. Schema row order defines signal table column order.

**Schema row order = table column order. F-01=Priority is column 1 of every signal table. A column
order change requires a schema row sequence change first.**

| ID | Field | Canonical Values | If I Violate This, I Will... |
|----|-------|-----------------|------------------------------|
| F-01 | Priority | essential / recommended / optional | ...write "high/medium/low" and produce a strategy that fails C-04 and cannot be rubric-scored |
| F-02 | Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | ...route signals to a nonexistent namespace, breaking downstream invocation |
| F-03 | Skill | skill name within namespace | ...name an uninvokable skill no team member can execute |
| F-04 | Item Name | {topic}-{signal}-{date}.md | ...create an artifact the registry cannot locate |
| F-05 | Owner Role | role responsible for executing this skill | ...produce signals with no execution owner — they will never be produced |

Signal table column order: **Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04)
| Owner Role (F-05)**

---

### PIPELINE OVERVIEW — I will read every row completely before executing Phase 0.

| Phase | Purpose | Handoff Artifact | Exit Gate | If I Skip This Phase, I Will... | Team Default When I Skip This |
|-------|---------|-----------------|----------|--------------------------------|-------------------------------|
| 0 | Confirm inputs | Confirmed-inputs record | Both inputs confirmed | ...produce a strategy for an unnamed feature — Phase 1 has nothing to anchor to | Teams name features in the moment and write strategies without scope |
| 1 | Identify stakeholders | Stakeholder table ≥ 3 rows, all cells filled | ≥ 3 rows, all cells complete | ...assign owner roles with no traceability to real concerns — Phase 2 inherits fabricated execution paths | Teams assign all signals to whoever called the meeting |
| 2 | Plan signals | Signal table, schema-ordered, all cells filled | ≥ 1 essential, all cells complete | ...pass Phase 3 an empty or partial signal list — the commit gate has nothing to verify | Teams treat the first signals mentioned as the complete list and never return to add more |
| 3 | Commit gate | Gate decision record (pass or return) | Both conditions independently satisfied | ...write TOPICS.md before the strategy passes its own gates — a false record of readiness | Teams scan the signal list visually and advance when it looks like enough |
| 4 | Write outputs | TOPICS.md entry + strategy.md | Both files written | ...leave the topic unregistered — no other skill can find or build on these signals | Teams keep strategies in ephemeral notes that drift from the actual implementation |

I will not execute Phase 0 until I have processed every row including both consequence columns.

**Handoff-artifact rule:** Before beginning any phase, I confirm the previous phase's handoff
artifact is present and complete.

---

### PHASE 0 — INPUT VALIDATION

**Handoff artifact to produce:** Confirmed-inputs record — topic name and description, both non-empty.

- Topic name: {topic}
- Topic description: {description}

**Check these two items independently. I will not advance to Phase 1 until both are confirmed
separately:**
- [ ] Topic name is present and non-empty
- [ ] Topic description is present and non-empty

**Do not advance until both boxes are checked independently.**

**If I check these sequentially:** confirming the topic name may lead me to treat the description as
present. Phase 1 will have no scope to anchor stakeholders to — every concern identified will float
free of any feature boundary. Teams name features in the moment and skip scope definition; I will
have done the same and my handoff artifact will be incomplete.

---

### PHASE 1 — STAKEHOLDER IDENTIFICATION

**Entry requirement:** Phase 0 handoff artifact (confirmed-inputs record) is present. Confirm
before beginning.

**Handoff artifact to produce:** Stakeholder table, ≥ 3 rows, all cells complete.

| Stakeholder | Concern | Signals-at-Risk |
|-------------|---------|----------------|

**Check these two items independently. I will not advance to Phase 2 until both are satisfied
separately:**
- [ ] I have at least 3 rows in the stakeholder table
- [ ] Every cell in every row is complete — no empty cells

**Do not advance until both boxes are checked independently.**

**If I check these sequentially:** a table with 3 rows where Concern and Signals-at-Risk cells are
empty satisfies the row-count check. My Phase 1 handoff artifact will be structurally present but
informationally empty — Phase 2 inherits stakeholder names with no concerns, and owner roles
assigned will be untraceable. Teams assign all signals to whoever called the meeting when concerns
are absent; I will have produced the structural equivalent.

---

### PHASE 2 — SIGNAL PLANNING

**Entry requirement:** Phase 1 handoff artifact (complete stakeholder table) is present. Confirm
before beginning.

**Handoff artifact to produce:** Signal table, schema-ordered, all cells complete, ≥ 1 essential.

Column order follows FIELD SCHEMA — **schema row order = table column order, F-01=Priority first**.

Priority vocabulary: **essential / recommended / optional only**. "High/medium/low" fails C-04.

| Priority | Namespace | Skill | Item Name | Owner Role |
|----------|-----------|-------|-----------|------------|

I will include at least one essential signal. I will assign different Owner Role values where
signals require different expertise.

**Check these two items independently. I will not advance to Phase 3 until both are satisfied
separately:**
- [ ] At least one row has Priority = essential
- [ ] All cells in every row are complete

**Do not advance until both boxes are checked independently.**

**If I check these sequentially:** confirming essential-signal presence may lead me to treat cell
completeness as already verified. Phase 3 will receive a signal table with empty cells — I will
find gaps at the commit gate with no clean return path. Teams treat the first signals mentioned as
the complete list and never return; I will have done the same, passing an incomplete handoff artifact.

---

### PHASE 3 — COMMIT GATE

**Entry requirement:** Phase 2 handoff artifact (complete signal table) is present. Confirm before
beginning.

**Handoff artifact to produce:** Gate decision record (both conditions passed, or return directive).

I will not write any output until both conditions are independently satisfied.

**Check these two items independently. I will not advance to Phase 4 until both are verified
separately:**
- [ ] [F-01] At least one row has Priority = essential
- [ ] [F-05] At least two distinct Owner Role values appear in the table

**Do not advance until both boxes are checked independently.**

**If I check these sequentially:** confirming the essential-signal condition may lead me to
rationalize that any populated table satisfies the role condition. I will advance past a strategy
where every signal shares the same owner. Teams scan the signal list visually and advance when it
looks like enough; I will have done the same, producing a gate decision record that attests to
readiness I have not verified.

If either condition fails, return to Phase 2 and revise.

---

### PHASE 4 — OUTPUT PRODUCTION

**Entry requirement:** Phase 3 handoff artifact (gate decision record, both conditions passed) is
present. Confirm before beginning.

**TOPICS.md entry** — append to `simulations/TOPICS.md`:
```
## {topic}
{description}
Strategy: simulations/{topic}/strategy.md
Signals: {n} planned ({e} essential, {r} recommended, {o} optional)
```

**strategy.md** — write to `simulations/{topic}/strategy.md`:
```markdown
# {topic} — Signal Strategy
{description}

## Rationale
{Why these signals? What decision do they inform? What team default does this investigation override?}

## Stakeholders
| Stakeholder | Concern | Signals-at-Risk |
{rows from Phase 1}

## Signals
| Priority | Namespace | Skill | Item Name | Owner Role |
{rows from Phase 2}

## Commit Gate
Before advancing to implementation:
- [ ] All essential signals produced
- [ ] All owner roles confirmed
- [ ] Strategy covers full topic description scope
```

---

## V-05 — Full Combination: Inertia Framing × Role Sequence × Lifecycle Emphasis

**Variation axis**: Inertia framing × role sequence × lifecycle emphasis — all three axes combined.
Behavioral-default consequence column (V-01), consumer-anchored signal planning with "Producer →
Consumer" F-05 (V-02), and phase handoff artifact tracking (V-03). The pipeline overview carries
handoff artifacts and both consequence columns. Phase 2 requires naming consumers before assigning
priority, with priority vocabulary anchored to decision dependency. Every phase gate confirms
artifact presence first.

**Hypothesis**: The three mechanisms operate at three independent structural layers:
- Inertia framing acts at **overview-reading time**: names the behavioral default the model must
  override before execution begins.
- Consumer anchoring acts at **fill time**: grounds priority vocabulary in decision dependency at
  the moment each row is written, before any rubric validation.
- Handoff-artifact tracking acts at **gate time**: makes phase-completion objectively detectable,
  so skip attempts produce detectable artifact absence rather than silent advancement.

No two mechanisms substitute for the other. Together they close three independent failure modes:
behavioral rationalization, vocabulary substitution, and silent phase-skipping.

---

You are registering a new topic for the Signal plugin. Read the FIELD SCHEMA first — it determines
column order for every table you produce. A phase is complete when its handoff artifact is present
and complete.

---

### FIELD SCHEMA — Read first. Schema row order defines signal table column order.

**Schema row order = table column order. F-01=Priority is column 1 of every signal table. A column
order change requires a schema row sequence change first.**

| ID | Field | Canonical Values | If I Violate This, I Will... |
|----|-------|-----------------|------------------------------|
| F-01 | Priority | essential / recommended / optional | ...write "high/medium/low" and produce a strategy that fails C-04 — the rubric cannot score this topic |
| F-02 | Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | ...route signals to a nonexistent namespace, breaking downstream invocation |
| F-03 | Skill | skill name within namespace | ...name an uninvokable skill no team member can execute |
| F-04 | Item Name | {topic}-{signal}-{date}.md | ...create an artifact the registry cannot locate |
| F-05 | Producer → Consumer | "{role} → {role}" — who executes the skill and who uses the signal to decide | ...produce signals with no consumer — priority assignment floats free of decision dependency |

Signal table column order: **Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04)
| Producer → Consumer (F-05)**

---

### PIPELINE OVERVIEW — I will read every row completely before executing Phase 0.

| Phase | Purpose | Handoff Artifact | Exit Gate | If I Skip This Phase, I Will... | Team Default When I Skip This |
|-------|---------|-----------------|----------|--------------------------------|-------------------------------|
| 0 | Confirm inputs | Confirmed-inputs record | Both inputs confirmed | ...produce a strategy for an unnamed feature — Phase 1 has no scope to anchor decisions to | Teams name features on the spot and write strategies without anchoring description |
| 1 | Identify decisions + stakeholders | Decision table (≥ 3) + stakeholder table (≥ 3) | Both tables complete | ...plan signals without anchoring to any real decision — priority assignments will be intuitive, not decision-grounded | Teams plan signals from habit; no one checks whether each signal unblocks a decision |
| 2 | Plan signals | Signal table, schema-ordered, all cells complete, each F-05 in Producer → Consumer format | ≥ 1 essential, all F-05 cells complete | ...produce signals with no consumer chain — essential/optional become meaningless labels | Teams write owner roles as job titles and never trace which decision each signal enables |
| 3 | Commit gate | Gate decision record (pass or return) | Both conditions independently satisfied | ...write TOPICS.md before the strategy passes its own gates — I will have attested to readiness I have not verified | Teams advance to implementation after visual inspection and assume the rest will work out |
| 4 | Write outputs | TOPICS.md entry + strategy.md | Both files written | ...leave the topic unregistered — the investigation cannot begin | Teams keep strategies in personal notes that drift from the actual work |

I will not execute Phase 0 until I have processed every row including both consequence columns.

**Handoff-artifact rule:** Before beginning any phase, I confirm the previous phase's handoff
artifact is present and complete.

---

### PHASE 0 — INPUT VALIDATION

**Handoff artifact to produce:** Confirmed-inputs record — topic name and description, both non-empty.

- Topic name: {topic}
- Topic description: {description}

**Check these two items independently. I will not advance to Phase 1 until both are confirmed
separately:**
- [ ] Topic name is present and non-empty
- [ ] Topic description is present and non-empty

**Do not advance until both boxes are checked independently.**

**If I check these sequentially:** confirming the topic name may lead me to treat the description as
present. Phase 1 will have no scope to anchor decisions to — every decision I identify will float
free of any feature boundary. Teams name features on the spot and skip scope definition; I will
have done the same, and my handoff artifact will be incomplete.

---

### PHASE 1 — DECISION AND STAKEHOLDER IDENTIFICATION

**Entry requirement:** Phase 0 handoff artifact (confirmed-inputs record) is present and complete.
Confirm before beginning.

**Handoff artifacts to produce:**
1. Decision table — what decisions this topic's signals must enable, who makes each decision
2. Stakeholder table — who is affected, what they care about, which signals are at risk

Phase 2 anchors Consumer roles and priority assignments to the decision table. If the decision table
is absent or incomplete, Phase 2 has no basis for decision-grounded priority assignment.

**Decision table — run first:**
| Decision | Decision-Maker Role | What Signal Makes This Decidable |
|----------|---------------------|----------------------------------|

**Stakeholder table — run second:**
| Stakeholder | Concern | Signals-at-Risk |
|-------------|---------|----------------|

**Check these four items independently. Do not advance to Phase 2 until all four are satisfied
separately:**
- [ ] Decision table has at least 3 rows
- [ ] Every cell in the decision table is complete
- [ ] Stakeholder table has at least 3 rows
- [ ] Every cell in the stakeholder table is complete

**Do not advance until all four boxes are checked independently.**

**If checked sequentially:** completing the row-count checks for both tables may lead you to treat
cell completeness as already verified. You will advance with decision-maker roles named but no "What
Signal Makes This Decidable" mapping. Phase 2 has consumer names but no basis for assigning
essential vs. recommended — no signal has been traced to any decision. Teams plan signals from habit
when decision mapping is absent; I will have produced the structural equivalent.

---

### PHASE 2 — SIGNAL PLANNING

**Entry requirement:** Phase 1 handoff artifacts (decision table + stakeholder table) are both
present and complete. Confirm before beginning.

**Handoff artifact to produce:** Signal table, schema-ordered, all cells complete, ≥ 1 essential,
every F-05 cell in "Producer → Consumer" format.

Column order follows FIELD SCHEMA — **schema row order = table column order, F-01=Priority first**.

For each signal, name the Consumer role before assigning Priority. Consumer must appear in the
Phase 1 decision table. Priority maps to decision dependency:
- **essential** — the consumer's decision cannot be made without this signal
- **recommended** — this signal strengthens the decision but is not blocking
- **optional** — the decision proceeds without this signal

Priority vocabulary: **essential / recommended / optional only**. "High/medium/low" fails C-04.

| Priority | Namespace | Skill | Item Name | Producer → Consumer |
|----------|-----------|-------|-----------|---------------------|

**Check these two items independently. Do not advance to Phase 3 until both are satisfied
separately:**
- [ ] At least one row has Priority = essential
- [ ] Every F-05 cell contains "X → Y" format with both producer and consumer named

**Do not advance until both boxes are checked independently.**

**If checked sequentially:** confirming essential-signal presence may lead you to treat F-05
completeness as already verified. You will advance with F-05 cells that name only a producer — the
decision-dependency chain is severed. Teams write owner roles as job titles and never trace which
decision each signal enables; I will have produced the structural equivalent and my handoff artifact
will be incomplete.

---

### PHASE 3 — COMMIT GATE

**Entry requirement:** Phase 2 handoff artifact (complete signal table) is present and complete.
Confirm before beginning.

**Handoff artifact to produce:** Gate decision record (both conditions passed, or return directive).

Do not write any output until both conditions are independently satisfied.

**Check these two items independently. Do not advance to Phase 4 until both are verified separately:**
- [ ] [F-01] At least one row has Priority = essential
- [ ] [F-05] At least two distinct Consumer roles appear — signals reach at least two different
  decision-makers

**Do not advance until both boxes are checked independently.**

**If checked sequentially:** confirming the essential-signal condition may lead me to rationalize
consumer diversity as already present. I will advance past a strategy where every signal feeds the
same decision-maker. Teams advance after visual inspection and assume the rest will work out; I will
have done the same, producing a gate decision record that attests to readiness I have not verified.

If either condition fails, return to Phase 2 and revise.

---

### PHASE 4 — OUTPUT PRODUCTION

**Entry requirement:** Phase 3 handoff artifact (gate decision record, both conditions passed) is
present. Confirm before beginning.

**TOPICS.md entry** — append to `simulations/TOPICS.md`:
```
## {topic}
{description}
Strategy: simulations/{topic}/strategy.md
Signals: {n} planned ({e} essential, {r} recommended, {o} optional)
```

**strategy.md** — write to `simulations/{topic}/strategy.md`:
```markdown
# {topic} — Signal Strategy
{description}

## Rationale
{Why these signals? What decisions do they enable? What team default does this investigation
override?}

## Decisions
| Decision | Decision-Maker Role | What Signal Makes This Decidable |
{rows from Phase 1 decision table}

## Stakeholders
| Stakeholder | Concern | Signals-at-Risk |
{rows from Phase 1 stakeholder table}

## Signals
| Priority | Namespace | Skill | Item Name | Producer → Consumer |
{rows from Phase 2}

## Commit Gate
Before advancing to implementation:
- [ ] All essential signals produced and delivered to consumer roles
- [ ] All consumer roles confirmed their signals unblocked their decisions
- [ ] Strategy covers full topic description scope
```

---

## Excellence Signal Candidates for R12

Three patterns that extend beyond any existing criterion and are candidates for criterion extraction
after R11 scoring:

**R11-ES-1 — Behavioral-default naming in consequence column** (V-01/V-04/V-05, C-29/C-32 extension)

The "Team Default When I Skip This" column names the specific organizational behavior that fills
the vacuum when a phase is skipped, rather than naming a system failure or a personal consequence.
This is structurally distinct from first-person consequence framing (C-32): C-32 makes the
executing model the subject of the failure; R11-ES-1 names the social/organizational default that
already exists and will execute automatically if the model does not override it. The named default
converts the skip choice from "will I cause a failure?" to "will I enact the default that is
already waiting for me?" The behavioral default is more motivationally salient because it is not
hypothetical — it is currently active.

**R11-ES-2 — Consumer-anchored priority assignment** (V-02/V-05, C-04/C-31 extension)

Requiring the Consumer role to be named before Priority is assigned grounds priority vocabulary in
an observable decision-dependency relationship at fill time, rather than in retrospective rubric
enforcement. "Essential" means "the consumer cannot decide without this"; "recommended" means "it
strengthens the decision"; "optional" means "the decision proceeds without it." This is structurally
distinct from priority-first column placement (C-31): C-31 prevents context-induced substitution
by placing Priority before namespace/skill framing can anchor vocabulary; R11-ES-2 prevents
substitution by giving each priority term a decision-dependency referent that "high/medium/low"
cannot satisfy.

**R11-ES-3 — Phase handoff artifact as entry requirement** (V-03/V-04/V-05, C-21/C-24 extension)

Defining phase completion by artifact presence rather than execution self-report makes every
phase-skip detectable: a model at Phase 3 that does not have a Phase 2 signal table cannot satisfy
Phase 3's entry requirement. This is structurally distinct from per-phase exit gates (C-21) and
pipeline overview gates (C-24): those criteria require gates to be declared; R11-ES-3 requires
phase entry to be conditioned on artifact presence from the previous phase. The distinction is
between exit-gate declaration (C-21) and entry-gate enforcement by artifact dependency (R11-ES-3).
The handoff-artifact rule cannot be rationalized past because artifact presence is binary and
externally verifiable, not self-reported.
