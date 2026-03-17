# /quest:variate — topic-new Round 12 (v11 rubric baseline)

Round 12 variations. Baseline: all 38 criteria (C-01–C-38) are structural invariants across all
five variations. C-35, C-36, C-37, C-38 (the four R11 elevations) are embedded in every variation.

Exploration targets for R12 (candidates for C-39/C-40/C-41):
- **ES-1 from R12**: Full priority-level vocabulary anchoring — all three levels carry decision-state
  anchors, not only "essential" (extends C-35)
- **ES-2 from R12**: Consumer-to-decision-table traceability enforcement — Consumer value in F-05
  must cite a row from Phase 1 decision table; Phase 2 gate explicitly verifies this (extends C-36)
- **ES-3 from R12**: Recovery cost column — pipeline overview carries a third consequence column
  naming the rework chain required when a skip is caught late (extends C-38)

Variation axes selected (3 single-axis, then combine):
1. Full vocabulary anchoring — all three priority levels carry decision-state anchors in FIELD SCHEMA
2. Consumer traceability — F-05 Consumer must trace to Phase 1 decision table; gate enforces it
3. Recovery cost framing — third consequence column names rework chain on late detection

---

## V-01 — Full Priority-Level Vocabulary Anchoring

**Variation axis**: Full vocabulary anchoring — FIELD SCHEMA F-01 row carries decision-state
anchors for all three priority levels, not just "essential." A dedicated Decision-State Anchor
column in FIELD SCHEMA names the operational consumer state each vocabulary term maps to:
- essential: consumer cannot decide without this — decision is blocked
- recommended: consumer decides with increased exposure — quality risk accepted
- optional: consumer decides unaffected — supplementary enrichment only

**Hypothesis**: C-35 closes the gap between column-order enforcement (C-34) and vocabulary meaning
for "essential." But "recommended vs. optional" collapse is the secondary vocabulary failure mode:
models tend to mark borderline signals as "recommended" because recommended sounds appropriately
cautious, without checking whether the consumer's decision would actually proceed without the signal.
Anchoring all three levels at schema-definition time makes the entire vocabulary set operationally
closed — "high/medium/low" has no mapping to any of the three decision states, whereas
"essential/recommended/optional" maps one-to-one. The substitution fails not just at one level
but at all three simultaneously.

---

You are registering a new topic for the Signal plugin and producing a complete investigation
strategy. Every constraint applies to you as the executing model. Read the FIELD SCHEMA before
the pipeline overview.

---

### FIELD SCHEMA — Read first. Schema row order defines signal table column order.

**Schema row order = table column order. F-01=Priority is column 1 of every signal table. A column
order change requires a schema row sequence change first.**

| ID | Field | Canonical Values | Decision-State Anchor | If I Violate This, I Will... |
|----|-------|-----------------|-----------------------|------------------------------|
| F-01 | Priority | essential / recommended / optional | essential = cannot decide — blocked; recommended = decides with risk — exposure accepted; optional = decides unaffected — supplementary | ...write "high/medium/low" — no anchor maps to any decision state — strategy fails C-04 and cannot serve as a commit gate |
| F-02 | Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | — | ...route signals to a nonexistent namespace, breaking downstream invocation |
| F-03 | Skill | skill name within namespace | — | ...name an uninvokable skill no team member can execute |
| F-04 | Item Name | {topic}-{signal}-{date}.md | — | ...create an artifact the registry cannot locate |
| F-05 | Producer → Consumer | "{role} → {role}" — who executes and who uses the signal to decide | — | ...produce signals with no consumer named — priority assignment floats free of any decision dependency |

Signal table column order: **Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04)
| Producer → Consumer (F-05)**

**Priority anchor reminder**: before assigning any priority value, identify the consumer role
(F-05) first. Then map: does the consumer's decision block on this signal (essential), proceed
with risk (recommended), or proceed unaffected (optional)?

---

### PIPELINE OVERVIEW — Read this entire table before executing Phase 0. All exit gates and consequences are declared here.

| Phase | Purpose | Handoff Artifact | Exit Gate | If I Skip This Phase, I Will... | Team Default When I Skip This |
|-------|---------|-----------------|----------|---------------------------------|-------------------------------|
| 0 | Confirm inputs | Confirmed-inputs record (topic name + description, both non-empty) | Both inputs confirmed | ...produce a strategy for an unnamed feature — Phase 1 has nothing to anchor stakeholders or decisions to | Teams name features in the moment and write strategies without anchoring scope |
| 1 | Identify decisions + stakeholders | Decision table (≥ 3 rows, all cells complete) + stakeholder table (≥ 3 rows, all cells complete) | Both tables complete with ≥ 3 rows each, all cells filled | ...plan signals without consumer roles grounded in real decisions — priority anchors collapse to intuition | Teams plan signals from habit; no one checks whether each signal unblocks a decision-maker |
| 2 | Plan signals | Signal table (schema-ordered, F-01 first, ≥ 1 essential, all cells complete) | ≥ 1 essential, all F-05 cells in Producer → Consumer format, all cells complete | ...produce signals with no decision-state mapping — essential/optional become synonyms for "feels important" / "feels minor" | Teams write priority as importance ranking; all borderline signals become recommended by default |
| 3 | Commit gate | Gate decision record (both conditions passed, or return directive) | Both conditions independently verified | ...write TOPICS.md before the strategy passes its own gates — I will have attested to readiness I have not verified | Teams advance to implementation after visual scan of the signal list |
| 4 | Write outputs | TOPICS.md entry + strategy.md at correct paths | Both files written | ...leave the topic unregistered — no other skill can find or build on these signals | Teams keep strategies in personal notes that drift from actual implementation |

I will not execute Phase 0 until I have processed every row including both consequence columns.

**Handoff-artifact rule:** Before beginning any phase, I confirm the previous phase's handoff
artifact is present and complete. Execution of a phase does not substitute for presence of its
handoff artifact.

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

**If I check these sequentially:** confirming the topic name may lead me to treat the description
as implicitly present. Phase 1 will have no scope to anchor decisions or stakeholders to — every
decision identified will float free of any feature boundary. Teams name features on the spot and
skip scope definition; I will have done the same and my handoff artifact will be incomplete.

---

### PHASE 1 — DECISION AND STAKEHOLDER IDENTIFICATION

**Entry requirement:** Phase 0 handoff artifact (confirmed-inputs record) is present and complete.
Confirm before beginning.

**Handoff artifacts to produce:**
1. Decision table — what decisions this topic's signals must enable, who makes each decision
2. Stakeholder table — who is affected, what they care about, which signals are at risk

Phase 2 assigns Priority using the decision-state anchor from F-01. The decision table provides
the consumer roles and decision states needed to apply that anchor. If the decision table is absent,
Phase 2 has no basis for distinguishing essential from recommended — priority anchors collapse.

**Decision table — run first:**
| Decision | Decision-Maker Role | What Signal Makes This Decidable |
|----------|---------------------|----------------------------------|

**Stakeholder table — run second:**
| Stakeholder | Concern | Signals-at-Risk |
|-------------|---------|----------------|

**Check these four items independently. I will not advance to Phase 2 until all four are satisfied
separately:**
- [ ] Decision table has at least 3 rows
- [ ] Every cell in the decision table is complete — no empty cells
- [ ] Stakeholder table has at least 3 rows
- [ ] Every cell in the stakeholder table is complete — no empty cells

**Do not advance until all four boxes are checked independently.**

**If I check these sequentially:** completing the row-count checks may cause me to treat cell
completeness as already verified. I will advance with decision-maker roles named but no "What
Signal Makes This Decidable" mapping — Phase 2 has consumer names but no basis for applying the
F-01 decision-state anchor. Teams plan signals from habit when decision mapping is absent; I will
have produced the structural equivalent.

---

### PHASE 2 — SIGNAL PLANNING

**Entry requirement:** Phase 1 handoff artifacts (decision table + stakeholder table) are both
present and complete. Confirm before beginning.

**Handoff artifact to produce:** Signal table, schema-ordered with F-01 first, all cells complete,
≥ 1 essential, all F-05 cells in Producer → Consumer format.

Column order follows FIELD SCHEMA — **schema row order = table column order, F-01=Priority first**.

**Before assigning Priority for each row, identify the Consumer role (F-05) and apply the F-01
decision-state anchor:**
- **essential** — the named consumer cannot decide without this signal (decision blocked)
- **recommended** — the named consumer decides with increased exposure (quality risk accepted)
- **optional** — the named consumer decides unaffected (supplementary enrichment only)

Priority vocabulary: **essential / recommended / optional only**. "High/medium/low" has no
decision-state anchor and fails C-04.

| Priority | Namespace | Skill | Item Name | Producer → Consumer |
|----------|-----------|-------|-----------|---------------------|

**Check these two items independently. I will not advance to Phase 3 until both are satisfied
separately:**
- [ ] [F-01] At least one row has Priority = essential
- [ ] [F-05] Every cell contains "{role} → {role}" format with both producer and consumer named

**Do not advance until both boxes are checked independently.**

**If I check these sequentially:** confirming essential-signal presence may lead me to treat F-05
completeness as already verified. I will advance with F-05 cells that name only a producer — the
consumer is unnamed and the decision-state anchor cannot be applied retroactively. Teams write
priority as an intuitive ranking when consumer roles are absent; I will have produced the
structural equivalent and my handoff artifact will be incomplete.

---

### PHASE 3 — COMMIT GATE

**Entry requirement:** Phase 2 handoff artifact (complete signal table) is present and complete.
Confirm before beginning.

**Handoff artifact to produce:** Gate decision record — both conditions passed (advance to Phase 4)
or return directive (return to Phase 2 and revise).

I will not write any output until both conditions are independently satisfied.

**Check these two items independently. I will not advance to Phase 4 until both are verified
separately:**
- [ ] [F-01] At least one row has Priority = essential — confirmed against the decision-state
  anchor: at least one consumer's decision is blocked without a planned signal
- [ ] [F-05] At least two distinct Consumer roles appear — signals reach at least two different
  decision-makers

**Do not advance until both boxes are checked independently.**

**If I check these sequentially:** confirming the essential-signal condition may lead me to
rationalize consumer diversity as already present. I will advance past a strategy where every
signal feeds the same decision-maker — no peer can independently validate coverage. Teams scan
visually and declare readiness; I will have attested to a gate decision record that overstates
verified conditions.

If either condition fails, return to Phase 2 and revise.

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
- [ ] All essential signals produced and delivered to named consumer roles
- [ ] Each consumer confirmed their decision was unblocked
- [ ] Strategy covers full topic description scope
```

---

## V-02 — Consumer-to-Decision-Table Traceability Enforcement

**Variation axis**: Consumer traceability — the Consumer role in F-05 must be a Decision-Maker
Role that appears in the Phase 1 decision table. Phase 2 exit gate explicitly checks that every
F-05 Consumer maps to a decision-table row. Phase 3 commit gate cites F-05 with this traceability
condition. The decision table in Phase 1 becomes the authoritative consumer registry from which
all signal consumers are drawn.

**Hypothesis**: C-36 requires F-05 = Producer→Consumer at schema-definition time, making role
differentiation auditable by schema inspection. But if Consumer can be any role string, the schema
field is structurally present without operational constraint — "PM" in F-05 and "PM" in the
decision table may refer to different decision contexts, or the consumer may not correspond to any
decision at all. Requiring the Consumer value to match a Decision-Maker Role in the Phase 1
decision table creates mechanical traceability from signal to decision at fill time. Priority
assignment can then be verified against the consumer's specific decision: if the consumer's
decision does not require this signal (optional), the essential label is falsified by inspection
of the decision table, not only by rubric scoring.

---

You are registering a new topic for the Signal plugin. Your investigation strategy must trace every
signal to a specific decision — who makes it, what makes it decidable, and whether each signal is
blocking, quality-enhancing, or supplementary for that consumer. Read the FIELD SCHEMA first.

---

### FIELD SCHEMA — Read first. Schema row order defines signal table column order.

**Schema row order = table column order. F-01=Priority is column 1 of every signal table. A column
order change requires a schema row sequence change first.**

| ID | Field | Canonical Values | If I Violate This, I Will... |
|----|-------|-----------------|-----------------------------|
| F-01 | Priority | essential / recommended / optional — essential = consumer cannot decide without this | ...write "high/medium/low" and produce a strategy that fails C-04 and cannot be used as a commit gate |
| F-02 | Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | ...route signals to a nonexistent namespace, breaking downstream invocation |
| F-03 | Skill | skill name within namespace | ...name an uninvokable skill no team member can execute |
| F-04 | Item Name | {topic}-{signal}-{date}.md | ...create an artifact the registry cannot locate |
| F-05 | Producer → Consumer | "{role} → {decision-maker role}" — Consumer must match a Decision-Maker Role in Phase 1 decision table | ...name a consumer with no decision-table entry — priority assignment floats free of any verifiable decision context |

Signal table column order: **Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04)
| Producer → Consumer (F-05)**

**F-05 traceability rule:** Consumer value must appear verbatim as a Decision-Maker Role in the
Phase 1 decision table. A consumer role invented at fill time that does not correspond to any
Phase 1 decision severs the chain from signal to decision — priority cannot be verified.

---

### PIPELINE OVERVIEW — Read this entire table before executing Phase 0. All exit gates and consequences are declared here.

| Phase | Purpose | Handoff Artifact | Exit Gate | If I Skip This Phase, I Will... | Team Default When I Skip This |
|-------|---------|-----------------|----------|---------------------------------|-------------------------------|
| 0 | Confirm inputs | Confirmed-inputs record (topic + description, both non-empty) | Both inputs confirmed | ...produce a strategy for an unnamed feature — the consumer registry I build in Phase 1 will have no scope to anchor to | Teams name features in the moment and write strategies without anchoring description |
| 1 | Identify decisions + stakeholders | Decision table (≥ 3 rows, all cells complete) + stakeholder table (≥ 3 rows, all cells complete) | Both tables complete | ...fill F-05 Consumer cells with improvised role strings that trace to nothing — every consumer I name will be structurally untraceable | Teams plan signals without mapping them to decisions; ownership is assigned by availability, not by decision responsibility |
| 2 | Plan signals | Signal table (schema-ordered, ≥ 1 essential, all F-05 Consumers in decision table) | ≥ 1 essential, all F-05 Consumers traceable to Phase 1 decision table | ...produce signals whose consumers are orphaned from any decision — essential/optional assignments cannot be verified by any structural inspection | Teams write consumer roles as job titles and never verify which decision each signal reaches |
| 3 | Commit gate | Gate decision record (both conditions passed, or return) | Both conditions independently verified | ...write TOPICS.md before verifying that signal consumers trace to verified decisions — I will have attested to a strategy that looks complete but severs traceability | Teams advance when the signal list looks long enough |
| 4 | Write outputs | TOPICS.md entry + strategy.md at correct paths | Both files written | ...leave the topic unregistered — the investigation cannot begin | Teams keep strategies in personal notes that drift from the actual work |

I will not execute Phase 0 until I have processed every row including both consequence columns.

**Handoff-artifact rule:** Before beginning any phase, I confirm the previous phase's handoff
artifact is present and complete.

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
implicitly present. Phase 1 will have no scope for the decision table — every decision identified
will float free of any feature boundary, and every consumer role derived from that table will be
ungrounded.

---

### PHASE 1 — DECISION AND STAKEHOLDER IDENTIFICATION

**Entry requirement:** Phase 0 handoff artifact (confirmed-inputs record) is present and complete.
Confirm before beginning.

**Handoff artifacts to produce:**
1. Decision table — the authoritative consumer registry for Phase 2 F-05 values
2. Stakeholder table — who is affected, what they care about, which signals are at risk

Phase 2 F-05 Consumer values must match Decision-Maker Role entries in the decision table. Build
this table first — it constrains every consumer value in the signal plan.

**Decision table — run first:**
| Decision | Decision-Maker Role | What Signal Makes This Decidable |
|----------|---------------------|----------------------------------|

**Stakeholder table — run second:**
| Stakeholder | Concern | Signals-at-Risk |
|-------------|---------|----------------|

**Check these four items independently. Do not advance to Phase 2 until all four are satisfied
separately:**
- [ ] Decision table has at least 3 rows
- [ ] Every cell in the decision table is complete — no empty cells
- [ ] Stakeholder table has at least 3 rows
- [ ] Every cell in the stakeholder table is complete — no empty cells

**Do not advance until all four boxes are checked independently.**

**If checked sequentially:** completing row-count checks may cause you to treat cell completeness
as already verified. You will advance with decision-maker roles named but no "What Signal Makes
This Decidable" column filled — Phase 2 will have consumer names in F-05 but no basis for
verifying whether each signal is essential or optional for that consumer's specific decision. Teams
assign roles by availability when decisions are unspecified; I will have produced the structural
equivalent.

---

### PHASE 2 — SIGNAL PLANNING

**Entry requirement:** Phase 1 handoff artifacts (decision table + stakeholder table) are both
present and complete. Confirm before beginning.

**Handoff artifact to produce:** Signal table, schema-ordered with F-01 first, all cells complete,
≥ 1 essential, every F-05 Consumer traceable to a Decision-Maker Role in the Phase 1 decision table.

Column order follows FIELD SCHEMA — **schema row order = table column order, F-01=Priority first**.

For each signal, identify the consumer role from the Phase 1 decision table before assigning
Priority. Priority maps to decision dependency for that specific consumer:
- **essential** — the consumer cannot make their decision without this signal (blocking)
- **recommended** — the consumer makes the decision with increased exposure (quality risk)
- **optional** — the consumer decides unaffected (supplementary enrichment)

Priority vocabulary: **essential / recommended / optional only**. "High/medium/low" fails C-04.

| Priority | Namespace | Skill | Item Name | Producer → Consumer |
|----------|-----------|-------|-----------|---------------------|

**Check these three items independently. Do not advance to Phase 3 until all three are satisfied
separately:**
- [ ] [F-01] At least one row has Priority = essential
- [ ] [F-05] Every cell contains "{role} → {role}" format with both producer and consumer named
- [ ] [F-05] Every Consumer value appears as a Decision-Maker Role in the Phase 1 decision table

**Do not advance until all three boxes are checked independently.**

**If checked sequentially:** confirming essential-signal presence may lead you to treat F-05
format and F-05 traceability as already verified. You will advance with F-05 cells that name a
consumer role not present in the decision table — the traceability chain is severed. Teams write
consumer roles as job titles without checking whether those roles were in the decision table; I
will have produced the structural equivalent.

---

### PHASE 3 — COMMIT GATE

**Entry requirement:** Phase 2 handoff artifact (complete signal table with traceable F-05 cells)
is present and complete. Confirm before beginning.

**Handoff artifact to produce:** Gate decision record (both conditions passed, or return directive).

Do not write any output until both conditions are independently satisfied.

**Check these two items independently. Do not advance to Phase 4 until both are verified
separately:**
- [ ] [F-01] At least one row has Priority = essential — consumer's decision is blocked without
  a planned signal
- [ ] [F-05] At least two distinct Consumer roles appear in the signal table — and both appear
  in the Phase 1 decision table

**Do not advance until both boxes are checked independently.**

**If checked sequentially:** confirming the essential-signal condition may lead you to rationalize
consumer diversity as already present. You will advance past a strategy where all signals feed a
single consumer — even if that consumer is traceable, the strategy has no multi-decision coverage.
Teams advance after a quick visual check of the signal list; I will have done the same, producing
a gate decision record that attests to a traceability I have not fully verified.

If either condition fails, return to Phase 2 and revise.

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
{rows from Phase 2 — all Consumer values traceable to Decisions table}

## Commit Gate
Before advancing to implementation:
- [ ] All essential signals produced and delivered to traced consumer roles
- [ ] Each consumer confirmed their decision was unblocked
- [ ] Strategy covers full topic description scope
```

---

## V-03 — Recovery Cost Column

**Variation axis**: Recovery cost framing — the pipeline overview carries a third consequence
column: "Recovery Cost When Caught Late" naming the rework chain required if the phase skip is
discovered downstream. The pipeline overview now carries three orthogonal consequence columns:
individual failure (first-person), team inertia default, and recovery cost.

**Hypothesis**: C-32 (first-person consequence) names what the model will produce incorrectly.
C-38 (team default) names the organizational behavior that will execute automatically. Neither
names the concrete rework cost when the skip is caught after Phase 4 artifacts are written. "I
will produce a strategy that fails C-04" is an abstract future failure. "Re-run Phase 2, re-run
Phase 3, re-write TOPICS.md and strategy.md" is a concrete rework chain. Models evaluate costs
in concrete terms more readily than in abstract failure-state terms. Recovery Cost makes the cost
of skipping actionable — not "you will have caused a failure" but "you will have created N phases
of rework that must be redone." These are orthogonal axes: a model can author a correct first-
person failure prediction and acknowledge the team default while still treating the skip as low-
cost if recovery is not named. The third column closes that gap.

---

You are registering a new topic for the Signal plugin and producing a complete investigation
strategy. Read the FIELD SCHEMA first. A phase is complete when its handoff artifact is present
and complete — not when you believe you have executed it.

---

### FIELD SCHEMA — Read first. Schema row order defines signal table column order.

**Schema row order = table column order. F-01=Priority is column 1 of every signal table. A column
order change requires a schema row sequence change first.**

| ID | Field | Canonical Values | If I Violate This, I Will... |
|----|-------|-----------------|-----------------------------|
| F-01 | Priority | essential / recommended / optional — essential = consumer cannot decide without this | ...write "high/medium/low" — no decision-state anchor — strategy fails C-04 and cannot serve as a commit gate |
| F-02 | Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | ...route signals to a nonexistent namespace, breaking downstream invocation |
| F-03 | Skill | skill name within namespace | ...name an uninvokable skill no team member can execute |
| F-04 | Item Name | {topic}-{signal}-{date}.md | ...create an artifact the registry cannot locate |
| F-05 | Producer → Consumer | "{role} → {role}" — who executes and who uses the signal to decide | ...produce signals with no consumer named — essential/optional labels float free of decision dependency |

Signal table column order: **Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04)
| Producer → Consumer (F-05)**

---

### PIPELINE OVERVIEW — Read this entire table before executing Phase 0. All exit gates and consequences are declared here.

| Phase | Purpose | Handoff Artifact | Exit Gate | If I Skip This Phase, I Will... | Team Default When I Skip This | Recovery Cost When Caught Late |
|-------|---------|-----------------|----------|---------------------------------|-------------------------------|-------------------------------|
| 0 | Confirm inputs | Confirmed-inputs record | Both inputs confirmed | ...produce a strategy for an unnamed feature — Phase 1 has nothing to anchor to | Teams name features in the moment and skip scope definition | Re-establish both inputs and re-run all five phases from scratch |
| 1 | Identify decisions + stakeholders | Decision table (≥ 3) + stakeholder table (≥ 3) | Both tables complete | ...assign owner roles with no traceability to real concerns — I will have fabricated every execution path | Teams assign all signals to whoever called the meeting | Re-run Phase 1, re-anchor all F-05 consumer roles in Phase 2, re-run Phase 2, re-run Phase 3, re-write both Phase 4 output files |
| 2 | Plan signals | Signal table (schema-ordered, ≥ 1 essential, all cells complete) | ≥ 1 essential, all cells complete | ...leave the feature with no implied commit gate — the strategy is unactionable | Teams treat the first signals mentioned as the complete list and never return | Re-run Phase 2 with schema-ordered columns, re-run Phase 3, re-write TOPICS.md and strategy.md |
| 3 | Commit gate | Gate decision record (pass or return) | Both conditions independently verified | ...write a false readiness record — I will have attested to a strategy that has not passed its own gates | Teams scan the signal list visually and advance when it looks like enough | Re-run Phase 3 with independently checked conditions, re-write both Phase 4 output files |
| 4 | Write outputs | TOPICS.md entry + strategy.md at correct paths | Both files written | ...leave the topic unregistered — no other skill can find these signals | Teams keep strategies in personal notes that drift from actual implementation | Re-write both output files at their correct paths |

I will not execute Phase 0 until I have processed every row including all three consequence columns.

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

**If I check these sequentially:** confirming the topic name may lead me to treat the description
as implicitly present. Recovery cost if caught late: all five phases must be re-run. Teams name
features in the moment and skip scope definition; I will have done the same.

---

### PHASE 1 — DECISION AND STAKEHOLDER IDENTIFICATION

**Entry requirement:** Phase 0 handoff artifact (confirmed-inputs record) is present. Confirm
before beginning.

**Handoff artifacts to produce:**
1. Decision table — what decisions this topic's signals must enable, who makes each decision
2. Stakeholder table — who is affected, what they care about, which signals are at risk

Phase 2 anchors F-05 Consumer roles and Priority assignments to the decision table.

**Decision table — run first:**
| Decision | Decision-Maker Role | What Signal Makes This Decidable |
|----------|---------------------|----------------------------------|

**Stakeholder table — run second:**
| Stakeholder | Concern | Signals-at-Risk |
|-------------|---------|----------------|

**Check these four items independently. I will not advance to Phase 2 until all four are satisfied
separately:**
- [ ] Decision table has at least 3 rows
- [ ] Every cell in the decision table is complete — no empty cells
- [ ] Stakeholder table has at least 3 rows
- [ ] Every cell in the stakeholder table is complete — no empty cells

**Do not advance until all four boxes are checked independently.**

**If I check these sequentially:** completing row-count checks may cause me to treat cell
completeness as already verified. Recovery cost if caught late: re-run Phase 1, re-anchor all F-05
consumer roles in Phase 2, re-run Phase 2, re-run Phase 3, re-write both output files. Teams
assign all signals to whoever called the meeting when concerns are absent; I will have produced the
structural equivalent.

---

### PHASE 2 — SIGNAL PLANNING

**Entry requirement:** Phase 1 handoff artifacts (decision table + stakeholder table) are both
present and complete. Confirm before beginning.

**Handoff artifact to produce:** Signal table, schema-ordered with F-01 first, all cells complete,
≥ 1 essential.

Column order follows FIELD SCHEMA — **schema row order = table column order, F-01=Priority first**.

Priority vocabulary: **essential / recommended / optional only** — essential = consumer cannot
decide without this. "High/medium/low" fails C-04.

| Priority | Namespace | Skill | Item Name | Producer → Consumer |
|----------|-----------|-------|-----------|---------------------|

**Check these two items independently. I will not advance to Phase 3 until both are satisfied
separately:**
- [ ] [F-01] At least one row has Priority = essential
- [ ] [F-05] Every cell contains "{role} → {role}" format with both producer and consumer named

**Do not advance until both boxes are checked independently.**

**If I check these sequentially:** confirming essential-signal presence may lead me to treat F-05
completeness as already verified. Recovery cost if caught late: re-run Phase 2, re-run Phase 3,
re-write both output files. Teams treat the first signals mentioned as the complete list; I will
have produced the structural equivalent.

---

### PHASE 3 — COMMIT GATE

**Entry requirement:** Phase 2 handoff artifact (complete signal table) is present. Confirm before
beginning.

**Handoff artifact to produce:** Gate decision record (both conditions passed, or return directive).

I will not write any output until both conditions are independently satisfied.

**Check these two items independently. I will not advance to Phase 4 until both are verified
separately:**
- [ ] [F-01] At least one row has Priority = essential
- [ ] [F-05] At least two distinct Consumer roles appear in the table

**Do not advance until both boxes are checked independently.**

**If I check these sequentially:** confirming the essential-signal condition may lead me to
rationalize consumer diversity as already present. Recovery cost if caught late: re-run Phase 3,
re-write both output files. Teams scan visually and advance; I will have attested to readiness not
fully verified.

If either condition fails, return to Phase 2 and revise.

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
- [ ] Each consumer confirmed their decision was unblocked
- [ ] Strategy covers full topic description scope
```

---

## V-04 — Combination: Full Vocabulary Anchoring × Consumer Traceability (V-01 + V-02)

**Variation axis**: Full vocabulary anchoring × consumer-to-decision-table traceability — all
three priority levels carry decision-state anchors in FIELD SCHEMA (V-01) combined with the
requirement that F-05 Consumer values must appear as Decision-Maker Roles in the Phase 1 decision
table (V-02). The FIELD SCHEMA Decision-State Anchor column is present. Phase 2 exit gate includes
the traceability check.

**Hypothesis**: V-01 closes vocabulary substitution for all three levels at schema-definition time.
V-02 closes consumer role improvisation at fill time. These operate at different structural layers
and address different failure modes:
- V-01 acts at **schema-reading time**: all three priority terms are defined against decision
  states before any phase begins. Substitution fails because no decision-state maps to "high."
- V-02 acts at **fill time**: the Consumer in each F-05 cell must be a verifiable decision-maker
  from Phase 1, making priority assignment a closed-loop check — essential is justified when
  the named consumer's decision is blocked, not just when the signal seems important.

A model can write correct vocabulary while naming an invented consumer role (fails V-02 but passes
V-01). A model can name a verified consumer while still substituting "high" (passes V-02 but fails
V-01). Only a model that names a decision-table consumer AND applies the correct vocabulary anchor
for that consumer's decision state satisfies both criteria simultaneously.

---

You are registering a new topic for the Signal plugin. Every signal must trace to a verifiable
decision — who makes it and whether this signal is blocking, quality-enhancing, or supplementary
for that specific decision. Read the FIELD SCHEMA first.

---

### FIELD SCHEMA — Read first. Schema row order defines signal table column order.

**Schema row order = table column order. F-01=Priority is column 1 of every signal table. A column
order change requires a schema row sequence change first.**

| ID | Field | Canonical Values | Decision-State Anchor | If I Violate This, I Will... |
|----|-------|-----------------|-----------------------|------------------------------|
| F-01 | Priority | essential / recommended / optional | essential = cannot decide — blocked; recommended = decides with risk — exposure accepted; optional = decides unaffected — supplementary | ...write "high/medium/low" — no anchor maps to any decision state — fails C-04 — strategy cannot serve as a commit gate |
| F-02 | Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | — | ...route signals to a nonexistent namespace, breaking downstream invocation |
| F-03 | Skill | skill name within namespace | — | ...name an uninvokable skill no team member can execute |
| F-04 | Item Name | {topic}-{signal}-{date}.md | — | ...create an artifact the registry cannot locate |
| F-05 | Producer → Consumer | "{role} → {decision-maker role}" — Consumer must appear as Decision-Maker Role in Phase 1 decision table | — | ...name a consumer with no decision-table entry — priority assignment is unverifiable by any structural inspection |

Signal table column order: **Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04)
| Producer → Consumer (F-05)**

**F-05 traceability rule:** Consumer value must match a Decision-Maker Role in the Phase 1
decision table. Invented consumer roles are not allowed even if they sound plausible.

**Priority anchor workflow:** For each signal row, (1) identify Consumer from decision table,
(2) identify what the consumer's decision requires, (3) apply the F-01 anchor: blocked = essential,
risk-exposed = recommended, unaffected = optional.

---

### PIPELINE OVERVIEW — Read this entire table before executing Phase 0. All exit gates and consequences are declared here.

| Phase | Purpose | Handoff Artifact | Exit Gate | If I Skip This Phase, I Will... | Team Default When I Skip This |
|-------|---------|-----------------|----------|---------------------------------|-------------------------------|
| 0 | Confirm inputs | Confirmed-inputs record (topic + description, both non-empty) | Both inputs confirmed | ...produce a strategy for an unnamed feature — the decision table I build in Phase 1 will have no scope to anchor consumer roles to | Teams name features in the moment and write strategies without anchoring description |
| 1 | Identify decisions + stakeholders | Decision table (≥ 3 rows, all cells complete) + stakeholder table (≥ 3 rows, all cells complete) | Both tables complete | ...fill F-05 with improvised consumer roles that trace to nothing — priority assignments will be aesthetically plausible but structurally unverifiable | Teams plan signals without mapping them to decisions; consumer roles are assigned by availability |
| 2 | Plan signals | Signal table (schema-ordered, F-01 first, ≥ 1 essential, all F-05 Consumers in decision table) | ≥ 1 essential, all F-05 Consumers traceable, all cells complete | ...produce a signal plan where priority assignments are unanchored and consumers are unverified — essential/optional mean nothing auditable | Teams write priority as intuitive importance ranking and consumer roles as job titles |
| 3 | Commit gate | Gate decision record (pass or return) | Both conditions independently verified | ...write TOPICS.md before the strategy traces consumers to verified decisions — I will have written a false readiness record | Teams advance after visual inspection and assume coverage is sufficient |
| 4 | Write outputs | TOPICS.md entry + strategy.md at correct paths | Both files written | ...leave the topic unregistered — the investigation cannot begin | Teams keep strategies in ephemeral notes that drift from the actual work |

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

**If I check these sequentially:** confirming the topic name may lead me to treat the description
as implicitly present. The decision table in Phase 1 will have no scope to anchor consumer roles
or decisions to. Teams name features in the moment; I will have done the same.

---

### PHASE 1 — DECISION AND STAKEHOLDER IDENTIFICATION

**Entry requirement:** Phase 0 handoff artifact (confirmed-inputs record) is present. Confirm
before beginning.

**Handoff artifacts to produce:**
1. Decision table — the authoritative Consumer registry for Phase 2 F-05 values
2. Stakeholder table — who is affected, what they care about, which signals are at risk

The decision table is not optional background context — it is the source of truth for all
Consumer values in the signal plan. Build it completely before Phase 2 begins.

**Decision table — run first:**
| Decision | Decision-Maker Role | What Signal Makes This Decidable |
|----------|---------------------|----------------------------------|

**Stakeholder table — run second:**
| Stakeholder | Concern | Signals-at-Risk |
|-------------|---------|----------------|

**Check these four items independently. I will not advance to Phase 2 until all four are satisfied
separately:**
- [ ] Decision table has at least 3 rows
- [ ] Every cell in the decision table is complete — no empty cells
- [ ] Stakeholder table has at least 3 rows
- [ ] Every cell in the stakeholder table is complete — no empty cells

**Do not advance until all four boxes are checked independently.**

**If I check these sequentially:** completing the row-count checks may cause me to treat cell
completeness as already verified. I will advance with decision-maker roles named but no "What
Signal Makes This Decidable" mapping — Phase 2 consumer roles will have names but the F-01
decision-state anchor cannot be applied because the decision context is unknown. Teams plan
signals from habit when decision mapping is absent; I will have done the same.

---

### PHASE 2 — SIGNAL PLANNING

**Entry requirement:** Phase 1 handoff artifacts (decision table + stakeholder table) are both
present and complete. Confirm before beginning.

**Handoff artifact to produce:** Signal table, schema-ordered with F-01 first, all cells complete,
≥ 1 essential, every F-05 Consumer traceable to Phase 1 decision table.

Column order follows FIELD SCHEMA — **schema row order = table column order, F-01=Priority first**.

**Priority assignment workflow (apply for every row):**
1. Select Consumer from the Phase 1 decision table (F-05 Consumer must match a Decision-Maker Role)
2. Identify the consumer's decision from the decision table
3. Apply the F-01 Decision-State Anchor:
   - **essential** — consumer cannot decide without this (blocked)
   - **recommended** — consumer decides with increased exposure (quality risk accepted)
   - **optional** — consumer decides unaffected (supplementary)

Priority vocabulary: **essential / recommended / optional only**. "High/medium/low" fails C-04.

| Priority | Namespace | Skill | Item Name | Producer → Consumer |
|----------|-----------|-------|-----------|---------------------|

**Check these three items independently. I will not advance to Phase 3 until all three are
satisfied separately:**
- [ ] [F-01] At least one row has Priority = essential
- [ ] [F-05] Every cell contains "{role} → {role}" format with both producer and consumer named
- [ ] [F-05] Every Consumer value appears verbatim as a Decision-Maker Role in Phase 1 decision table

**Do not advance until all three boxes are checked independently.**

**If I check these sequentially:** confirming essential-signal presence may lead me to treat F-05
format and traceability as already verified. I will advance with F-05 Consumers that are not in
the decision table — the decision-state anchor cannot be retrospectively applied to an anonymous
consumer role, and my handoff artifact is incomplete even if the table is filled.

---

### PHASE 3 — COMMIT GATE

**Entry requirement:** Phase 2 handoff artifact (complete signal table with traceable consumers)
is present and complete. Confirm before beginning.

**Handoff artifact to produce:** Gate decision record (both conditions passed, or return directive).

I will not write any output until both conditions are independently satisfied.

**Check these two items independently. I will not advance to Phase 4 until both are verified
separately:**
- [ ] [F-01] At least one row has Priority = essential — confirmed using the F-01 decision-state
  anchor: at least one consumer's decision is blocked without a planned signal
- [ ] [F-05] At least two distinct Consumer roles appear — and both appear in the Phase 1
  decision table

**Do not advance until both boxes are checked independently.**

**If I check these sequentially:** confirming the essential-signal condition may cause me to
rationalize consumer diversity and traceability as implicitly verified. I will advance past a
strategy where all signals feed the same decision-maker, or where a second consumer role was
not in the decision table. Teams advance after visual inspection; I will have attested to a gate
decision record that overstates verified traceability.

If either condition fails, return to Phase 2 and revise.

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
{rows from Phase 2 — all Consumer values traceable to Decisions table}

## Commit Gate
Before advancing to implementation:
- [ ] All essential signals produced and delivered to named consumer roles
- [ ] Each consumer confirmed their decision was unblocked
- [ ] All consumers in signal plan verified against decision table
- [ ] Strategy covers full topic description scope
```

---

## V-05 — Full Combination: Full Vocabulary Anchoring × Consumer Traceability × Recovery Cost

**Variation axis**: All three R12 axes combined — full three-level vocabulary anchoring (V-01),
Consumer-to-decision-table traceability enforcement (V-02), and recovery cost column in pipeline
overview (V-03). The FIELD SCHEMA Decision-State Anchor column covers all three priority levels.
Phase 2 exit gate includes the F-05 traceability check. The pipeline overview carries three
consequence columns: first-person failure, team inertia default, and recovery cost when caught late.

**Hypothesis**: The three mechanisms operate at three independent structural layers and close three
independent failure modes:
- **Full vocabulary anchoring** acts at **schema-reading time**: all three priority terms carry
  decision-state anchors before any phase begins. Substitution fails at all three levels
  simultaneously — "high/medium/low" maps to no decision state at any tier.
- **Consumer traceability** acts at **fill time**: each Consumer in F-05 must be drawn from the
  Phase 1 decision table. Priority assignment is verified at the moment of assignment — the
  decision-state anchor is applied to a specific, traceable decision, not to an abstract consumer.
- **Recovery cost framing** acts at **skip-evaluation time**: the pipeline overview names the
  concrete rework chain for each phase-skip, making skip cost actionable rather than abstract.
  A model that encounters "Re-run Phase 2, re-run Phase 3, re-write both output files" evaluates
  cost differently than one that encounters only "I will produce an unactionable strategy."

No two mechanisms substitute for the other. Together they close three independent failure axes:
vocabulary-tier collapse, consumer improvisation, and skip-cost underestimation.

---

You are registering a new topic for the Signal plugin. Every signal traces to a verified decision
with a named consumer and a decision-grounded priority. Read the FIELD SCHEMA first — it
determines column order and priority vocabulary for every table you produce. A phase is complete
when its handoff artifact is present and complete.

---

### FIELD SCHEMA — Read first. Schema row order defines signal table column order.

**Schema row order = table column order. F-01=Priority is column 1 of every signal table. A column
order change requires a schema row sequence change first.**

| ID | Field | Canonical Values | Decision-State Anchor | If I Violate This, I Will... |
|----|-------|-----------------|-----------------------|------------------------------|
| F-01 | Priority | essential / recommended / optional | essential = cannot decide — blocked; recommended = decides with risk — exposure accepted; optional = decides unaffected — supplementary | ...write "high/medium/low" — no anchor maps to any decision state — fails C-04 — strategy is unusable as a commit gate |
| F-02 | Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | — | ...route signals to a nonexistent namespace, breaking downstream invocation |
| F-03 | Skill | skill name within namespace | — | ...name an uninvokable skill no team member can execute |
| F-04 | Item Name | {topic}-{signal}-{date}.md | — | ...create an artifact the registry cannot locate |
| F-05 | Producer → Consumer | "{role} → {decision-maker role}" — Consumer must appear as Decision-Maker Role in Phase 1 decision table | — | ...name a consumer with no decision-table entry — priority assignment floats free of any verifiable decision, and the entire signal-to-decision chain is severed |

Signal table column order: **Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04)
| Producer → Consumer (F-05)**

**F-05 traceability rule:** Consumer value must appear verbatim as a Decision-Maker Role in the
Phase 1 decision table. A consumer invented at fill time is not traceable even if it appears
plausible — it severs the chain from signal to decision.

**Priority assignment workflow (every row):**
1. Identify Consumer from Phase 1 decision table
2. Identify that consumer's decision from the decision table
3. Apply F-01 anchor: blocked = essential, risk-exposed = recommended, unaffected = optional

---

### PIPELINE OVERVIEW — Read this entire table before executing Phase 0. All exit gates and consequences are declared here.

| Phase | Purpose | Handoff Artifact | Exit Gate | If I Skip This Phase, I Will... | Team Default When I Skip This | Recovery Cost When Caught Late |
|-------|---------|-----------------|----------|---------------------------------|-------------------------------|-------------------------------|
| 0 | Confirm inputs | Confirmed-inputs record (topic + description, both non-empty) | Both inputs confirmed | ...produce a strategy for an unnamed feature — the decision table in Phase 1 will have no scope to anchor consumer roles to | Teams name features on the spot and write strategies without anchoring description | Re-establish both inputs and re-run all five phases from scratch |
| 1 | Identify decisions + stakeholders | Decision table (≥ 3 rows, all cells complete) + stakeholder table (≥ 3 rows, all cells complete) | Both tables complete | ...fill F-05 with improvised consumer roles — priority anchors will be aesthetically plausible but structurally unverifiable | Teams plan signals without mapping them to decisions; consumer roles assigned by availability | Re-run Phase 1, re-anchor all F-05 consumer roles in Phase 2, re-run Phase 2, re-run Phase 3, re-write both Phase 4 output files |
| 2 | Plan signals | Signal table (schema-ordered, F-01 first, ≥ 1 essential, all F-05 Consumers in decision table) | ≥ 1 essential, all F-05 Consumers traceable, all cells complete | ...produce signals with unanchored priority and unverified consumers — essential/optional are meaningless labels without the F-01 anchor applied against a real decision | Teams write priority as intuitive ranking and consumer roles as job titles; recommended is the safe default | Re-run Phase 2 with schema-ordered columns and traceable consumers, re-run Phase 3, re-write both output files |
| 3 | Commit gate | Gate decision record (pass or return) | Both conditions independently verified | ...write TOPICS.md before the strategy traces consumers to decisions — I will have attested to readiness that has not been verified by structural inspection | Teams scan the signal list and advance when it looks like enough; traceability is never checked | Re-run Phase 3 with independently checked conditions, re-write both output files |
| 4 | Write outputs | TOPICS.md entry + strategy.md at correct paths | Both files written | ...leave the topic unregistered — no other skill can find or build on these signals | Teams keep strategies in personal notes that drift from actual work | Re-write both output files at their correct paths |

I will not execute Phase 0 until I have processed every row including all three consequence columns.

**Handoff-artifact rule:** Before beginning any phase, I confirm the previous phase's handoff
artifact is present and complete. Execution of a phase does not substitute for presence of its
handoff artifact.

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

**If I check these sequentially:** confirming the topic name may lead me to treat the description
as implicitly present. Recovery cost if caught late: all five phases must be re-run from scratch.
Teams name features on the spot and skip scope definition; I will have done the same, and my
handoff artifact will be incomplete.

---

### PHASE 1 — DECISION AND STAKEHOLDER IDENTIFICATION

**Entry requirement:** Phase 0 handoff artifact (confirmed-inputs record) is present and complete.
Confirm before beginning.

**Handoff artifacts to produce:**
1. Decision table — the authoritative Consumer registry for Phase 2 F-05 values; Phase 2 cannot
   assign traceable priority without this table
2. Stakeholder table — who is affected, what they care about, which signals are at risk

**Decision table — run first:**
| Decision | Decision-Maker Role | What Signal Makes This Decidable |
|----------|---------------------|----------------------------------|

**Stakeholder table — run second:**
| Stakeholder | Concern | Signals-at-Risk |
|-------------|---------|----------------|

**Check these four items independently. I will not advance to Phase 2 until all four are satisfied
separately:**
- [ ] Decision table has at least 3 rows
- [ ] Every cell in the decision table is complete — no empty cells
- [ ] Stakeholder table has at least 3 rows
- [ ] Every cell in the stakeholder table is complete — no empty cells

**Do not advance until all four boxes are checked independently.**

**If I check these sequentially:** completing row-count checks may cause me to treat cell
completeness as already verified. Recovery cost if caught late: re-run Phase 1, re-anchor all F-05
consumer roles in Phase 2, re-run Phase 2, re-run Phase 3, re-write both output files. Teams assign
all signals to whoever called the meeting when decision context is absent; I will have done the
same, and my handoff artifact will be structurally present but informationally empty.

---

### PHASE 2 — SIGNAL PLANNING

**Entry requirement:** Phase 1 handoff artifacts (decision table + stakeholder table) are both
present and complete. Confirm before beginning.

**Handoff artifact to produce:** Signal table, schema-ordered with F-01 first, all cells complete,
≥ 1 essential, every F-05 Consumer appearing as a Decision-Maker Role in Phase 1 decision table.

Column order follows FIELD SCHEMA — **schema row order = table column order, F-01=Priority first**.

**Priority assignment workflow (apply for every row before writing):**
1. Select Consumer from the Phase 1 decision table — the Consumer in F-05 must appear there
2. Identify that consumer's decision from the decision table
3. Apply the F-01 Decision-State Anchor:
   - **essential** — consumer cannot decide without this (blocked)
   - **recommended** — consumer decides with increased exposure (quality risk accepted)
   - **optional** — consumer decides unaffected (supplementary)

Priority vocabulary: **essential / recommended / optional only**. "High/medium/low" has no
decision-state anchor at any tier and fails C-04.

| Priority | Namespace | Skill | Item Name | Producer → Consumer |
|----------|-----------|-------|-----------|---------------------|

**Check these three items independently. I will not advance to Phase 3 until all three are
satisfied separately:**
- [ ] [F-01] At least one row has Priority = essential
- [ ] [F-05] Every cell contains "{role} → {role}" format with both producer and consumer named
- [ ] [F-05] Every Consumer value appears verbatim as a Decision-Maker Role in Phase 1 decision table

**Do not advance until all three boxes are checked independently.**

**If I check these sequentially:** confirming essential-signal presence may lead me to treat F-05
format and traceability as already verified. Recovery cost if caught late: re-run Phase 2 with
traceable consumers, re-run Phase 3, re-write both output files. Teams write consumer roles as
job titles and never verify traceability; I will have done the same, passing an incomplete handoff
artifact.

---

### PHASE 3 — COMMIT GATE

**Entry requirement:** Phase 2 handoff artifact (complete signal table with traceable consumers)
is present and complete. Confirm before beginning.

**Handoff artifact to produce:** Gate decision record (both conditions passed, or return directive).

I will not write any output until both conditions are independently satisfied.

**Check these two items independently. I will not advance to Phase 4 until both are verified
separately:**
- [ ] [F-01] At least one row has Priority = essential — verified using the F-01 decision-state
  anchor: at least one consumer's decision is blocked without a planned signal
- [ ] [F-05] At least two distinct Consumer roles appear in the signal table — and both appear
  in the Phase 1 decision table

**Do not advance until both boxes are checked independently.**

**If I check these sequentially:** confirming the essential-signal condition may cause me to
rationalize consumer diversity and traceability as implicitly satisfied. Recovery cost if caught
late: re-run Phase 3, re-write both output files. Teams scan visually and advance; I will have
produced a gate decision record that attests to readiness I have not verified by structural
inspection.

If either condition fails, return to Phase 2 and revise.

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
{rows from Phase 2 — all Consumer values traceable to Decisions table}

## Commit Gate
Before advancing to implementation:
- [ ] All essential signals produced and delivered to named consumer roles
- [ ] Each consumer confirmed their decision was unblocked
- [ ] All consumers in signal plan verified against decision table
- [ ] Strategy covers full topic description scope
```

---

## Excellence Signal Candidates for R13

Three patterns that extend beyond any existing criterion and are candidates for criterion
extraction after R12 scoring:

**R12-ES-1 — Full three-level vocabulary anchoring in FIELD SCHEMA** (V-01/V-04/V-05, C-35 extension)

C-35 anchors "essential = consumer cannot decide without this" — one level. V-01/V-04/V-05
anchor all three levels with distinct decision states: essential = blocked, recommended = risk
accepted, optional = unaffected. This is structurally distinct from C-35: C-35 closes the gap
between column-order enforcement and vocabulary meaning for the essential tier; R12-ES-1 closes
the same gap for all three tiers simultaneously. "High/medium/low" has no mapping to any
decision state across all three tiers — substitution fails completely rather than partially. The
mechanism is a Decision-State Anchor column in FIELD SCHEMA where F-01 carries three
anchor entries rather than one. Models tend to collapse recommended/optional when only
essential is anchored; full three-level anchoring removes that collapse vector entirely.

**R12-ES-2 — Consumer-to-decision-table traceability enforcement at Phase 2 exit gate**
(V-02/V-04/V-05, C-36 extension)

C-36 requires FIELD SCHEMA to carry a Producer→Consumer field making role differentiation
auditable by schema inspection. That field is structurally present, but Consumer can be any role
string — the schema constraint is definitional, not traceable. R12-ES-2 requires the Consumer
value in each F-05 cell to appear verbatim as a Decision-Maker Role in the Phase 1 decision
table, enforced by a third item in the Phase 2 exit gate: "Every Consumer value appears in Phase
1 decision table." This is structurally distinct from C-36: C-36 establishes the schema-level
relationship; R12-ES-2 requires that relationship to be mechanically verified at fill time, making
priority assignment auditable against a specific decision context rather than against an abstract
consumer label. The Phase 2 exit gate becomes the enforcement point for cross-phase data integrity.

**R12-ES-3 — Recovery cost column as third consequence axis in pipeline overview**
(V-03/V-05, C-38 extension)

C-38 requires a second consequence column naming the team's default inertia behavior — orthogonal
to the first-person individual-failure column. R12-ES-3 adds a third, orthogonal consequence
column naming the rework chain required when the skip is caught after Phase 4 outputs are written.
The three columns cover three independent temporal axes: (1) immediate individual failure (what I
will produce wrongly, first-person), (2) immediate team inertia (what the team defaults to
without active intervention), and (3) deferred repair cost (what must be re-run when the skip is
caught late). A model can author a correct first-person prediction and name the team default while
still treating the skip as low-cost if repair cost is not named. The recovery cost column makes
skip cost actionable: "Re-run Phase 2, re-run Phase 3, re-write both output files" is a concrete
rework prediction, not an abstract failure state.
