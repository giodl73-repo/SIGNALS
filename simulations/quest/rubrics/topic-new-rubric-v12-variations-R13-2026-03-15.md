# /quest:variate — topic-new Round 13 (v12 rubric baseline)

Round 13 variations. Baseline: all 41 criteria (C-01–C-41) are structural invariants across all
five variations. C-39, C-40, C-41 (the three R12 elevations) are embedded in every variation.

Exploration targets for R13 (candidates for C-42/C-43/C-44):
- **ES-1 from R13**: Stakeholder-first Phase 1 ordering — stakeholder table runs before decision
  table, grounding decision-maker roles in a broader stakeholder roster before narrowing to decisions
- **ES-2 from R13**: Second-person imperative phrasing — external-instruction register replaces
  first-person self-commitment; tests whether voice changes structural compliance in executed strategies
- **ES-3 from R13**: Dedicated INERTIA REGISTER block — all five team defaults named and numbered
  before FIELD SCHEMA; pipeline "Team Default" cells become register back-references

Variation axes selected (3 single-axis, then combine):
1. Role sequence — stakeholder table before decision table in Phase 1
2. Phrasing register — second-person imperative throughout (replaces first-person commitment)
3. Inertia framing — dedicated INERTIA REGISTER block; pipeline table back-references IR entries

---

## V-01 — Stakeholder-First Phase 1 Ordering

**Variation axis**: Role sequence — Phase 1 runs stakeholder identification first, then derives the
decision table from the stakeholder roster. Decision-maker roles are filtered from the stakeholder
table rather than generated independently, ensuring consumer traceability begins from a
people-centric enumeration rather than a feature-centric one.

**Hypothesis**: Current decision-first Phase 1 ordering risks generating decision tables from feature
knowledge ("what decisions does this feature touch?") rather than people knowledge ("who is
affected?"). If the model generates a decision table without first enumerating stakeholders, it may
name decision-maker roles that reflect prior training patterns rather than the specific feature's
actual stakeholder set. Stakeholder-first ordering forces people identification before decision
mapping — every Decision-Maker Role in the decision table must trace to a stakeholder row. This
closes a potential F-05 Consumer coverage gap where relevant decision-makers are missed because
they were never surfaced as stakeholders.

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
| F-05 | Producer → Consumer | "{role} → {decision-maker role}" — Consumer must appear verbatim as a Decision-Maker Role in Phase 1 decision table | — | ...name a consumer with no decision-table entry — priority assignment floats free of any verifiable decision context |

Signal table column order: **Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04)
| Producer → Consumer (F-05)**

**Priority anchor reminder**: before assigning any priority value, identify the consumer role (F-05)
first. Then map: does the consumer's decision block on this signal (essential), proceed with risk
(recommended), or proceed unaffected (optional)?

**F-05 traceability rule**: Consumer value must appear verbatim as a Decision-Maker Role in the
Phase 1 decision table. A consumer role invented at fill time that does not correspond to any
Phase 1 decision-table row severs the chain from signal to decision.

---

### PIPELINE OVERVIEW — Read this entire table before executing Phase 0. All exit gates and consequences are declared here.

| Phase | Purpose | Handoff Artifact | Exit Gate | If I Skip This Phase, I Will... | Team Default When I Skip This | Recovery Rework Chain (Late Detection) |
|-------|---------|-----------------|----------|---------------------------------|-------------------------------|----------------------------------------|
| 0 | Confirm inputs | Confirmed-inputs record (topic name + description, both non-empty) | Both inputs confirmed | ...produce a strategy for an unnamed feature — Phase 1 has nothing to anchor stakeholders or decisions to | Teams name features in the moment and write strategies without anchoring scope | Re-confirm topic name and description independently; discard all Phase 1 outputs; restart Phase 1 from scratch |
| 1 | Identify stakeholders + decisions | Stakeholder table (≥ 3 rows, all cells complete) + decision table (≥ 3 rows, all cells complete) | Both tables complete with ≥ 3 rows each, all cells filled | ...plan signals without consumer roles grounded in real decisions — priority anchors collapse to intuition | Teams plan signals from habit; no one checks whether each signal unblocks a decision-maker | Re-run Phase 1 (rebuild both tables from confirmed inputs); re-run Phase 2 (rebuild signal table with corrected consumer roster); rewrite strategy.md |
| 2 | Plan signals | Signal table (schema-ordered, F-01 first, ≥ 1 essential, all F-05 Consumers traceable to Phase 1 decision table) | ≥ 1 essential, all F-05 Consumers traceable, all cells complete | ...produce signals whose consumers are orphaned from any decision — essential/optional become synonyms for "feels important" / "feels minor" | Teams write priority as importance ranking; all borderline signals become recommended by default | Re-run Phase 2 applying decision-state anchor to every row; rewrite signal table; re-run Phase 3 |
| 3 | Commit gate | Gate decision record (both conditions passed, or return directive) | Both conditions independently verified | ...write TOPICS.md before the strategy passes its own gates — I will have attested to readiness I have not verified | Teams advance to implementation after visual scan of the signal list | Re-run Phase 3 against corrected signal table; if either condition fails return to Phase 2; rewrite gate record; rewrite both output files |
| 4 | Write outputs | TOPICS.md entry + strategy.md at correct paths | Both files written | ...leave the topic unregistered — no other skill can find or build on these signals | Teams keep strategies in personal notes that drift from actual implementation | Re-run Phase 4; write TOPICS.md entry and strategy.md to canonical paths; re-register topic |

I will not execute Phase 0 until I have processed every row including all three consequence columns.

**Handoff-artifact rule**: Before beginning any phase, I confirm the previous phase's handoff
artifact is present and complete. Execution of a phase does not substitute for presence of its
handoff artifact.

---

### PHASE 0 — INPUT VALIDATION

**Handoff artifact to produce**: Confirmed-inputs record — topic name and description, both non-empty.

- Topic name: {topic}
- Topic description: {description}

**Check these two items independently. I will not advance to Phase 1 until both are confirmed
separately:**
- [ ] Topic name is present and non-empty
- [ ] Topic description is present and non-empty

**Do not advance until both boxes are checked independently.**

**If I check these sequentially**: confirming the topic name may lead me to treat the description as
implicitly present. Phase 1 will have no scope to anchor stakeholders or decisions to — every
stakeholder and decision identified will float free of any feature boundary.

---

### PHASE 1 — STAKEHOLDER AND DECISION IDENTIFICATION

**Entry requirement**: Phase 0 handoff artifact (confirmed-inputs record) is present and complete.
Confirm before beginning.

**Handoff artifacts to produce:**
1. Stakeholder table — who is affected, what they care about, which signals are at risk
2. Decision table — what decisions this topic's signals must enable, who makes each decision

**Run stakeholder identification first.** The stakeholder table surfaces the full population of
affected parties. The decision table then identifies which stakeholders are decision-makers and
maps each decision to what signal makes it decidable. Phase 2 F-05 Consumer values must appear
verbatim as Decision-Maker Role entries in the decision table. Building the stakeholder table first
ensures the decision table's Decision-Maker Roles are drawn from a complete people roster rather
than generated independently from feature knowledge.

**Stakeholder table — run first:**
| Stakeholder | Concern | Signals-at-Risk |
|-------------|---------|----------------|

**Decision table — run second (Decision-Maker Roles must trace to stakeholder rows):**
| Decision | Decision-Maker Role | What Signal Makes This Decidable |
|----------|---------------------|----------------------------------|

**Check these four items independently. I will not advance to Phase 2 until all four are satisfied
separately:**
- [ ] Stakeholder table has at least 3 rows
- [ ] Every cell in the stakeholder table is complete — no empty cells
- [ ] Decision table has at least 3 rows
- [ ] Every cell in the decision table is complete — no empty cells

**Do not advance until all four boxes are checked independently.**

**If I check these sequentially**: completing the row-count checks may cause me to treat cell
completeness as already verified. I will advance with decision-maker roles named but no "What
Signal Makes This Decidable" mapping — Phase 2 has consumer names but no basis for applying the
F-01 decision-state anchor. Teams plan signals from habit when decision mapping is absent; I will
have produced the structural equivalent.

---

### PHASE 2 — SIGNAL PLANNING

**Entry requirement**: Phase 1 handoff artifacts (stakeholder table + decision table) are both
present and complete. Confirm before beginning.

**Handoff artifact to produce**: Signal table, schema-ordered with F-01 first, all cells complete,
≥ 1 essential, every F-05 Consumer appearing verbatim as a Decision-Maker Role in the Phase 1
decision table.

Column order follows FIELD SCHEMA — **schema row order = table column order, F-01=Priority first**.

**Before assigning Priority for each row, identify the Consumer role (F-05) from the Phase 1
decision table and apply the F-01 decision-state anchor:**
- **essential** — the named consumer cannot decide without this signal (decision blocked)
- **recommended** — the named consumer decides with increased exposure (quality risk accepted)
- **optional** — the named consumer decides unaffected (supplementary enrichment only)

Priority vocabulary: **essential / recommended / optional only**. "High/medium/low" has no
decision-state anchor and fails C-04.

| Priority | Namespace | Skill | Item Name | Producer → Consumer |
|----------|-----------|-------|-----------|---------------------|

**Check these three items independently. I will not advance to Phase 3 until all three are satisfied
separately:**
- [ ] [F-01] At least one row has Priority = essential
- [ ] [F-05] Every cell contains "{role} → {role}" format with both producer and consumer named
- [ ] [F-05] Every Consumer value appears verbatim as a Decision-Maker Role in the Phase 1 decision table

**Do not advance until all three boxes are checked independently.**

**If I check these sequentially**: confirming essential-signal presence may lead me to treat F-05
format and F-05 traceability as already verified. I will advance with F-05 cells that name a
consumer role not present in the decision table — the traceability chain is severed. Teams write
consumer roles as job titles without checking whether those roles appeared in the decision table;
I will have produced the structural equivalent.

---

### PHASE 3 — COMMIT GATE

**Entry requirement**: Phase 2 handoff artifact (complete signal table) is present and complete.
Confirm before beginning.

**Handoff artifact to produce**: Gate decision record — both conditions passed (advance to Phase 4)
or return directive (return to Phase 2 and revise).

I will not write any output until both conditions are independently satisfied.

**Check these two items independently. I will not advance to Phase 4 until both are verified
separately:**
- [ ] [F-01] At least one row has Priority = essential — confirmed against the decision-state
  anchor: at least one consumer's decision is blocked without a planned signal
- [ ] [F-05] At least two distinct Consumer roles appear — signals reach at least two different
  decision-makers, and both Consumer roles appear verbatim in the Phase 1 decision table

**Do not advance until both boxes are checked independently.**

**If I check these sequentially**: confirming the essential-signal condition may lead me to
rationalize consumer diversity as already present. I will advance past a strategy where every
signal feeds the same decision-maker — no peer can independently validate coverage. Teams scan
visually and declare readiness; I will have attested to a gate decision record that overstates
verified conditions.

If either condition fails, return to Phase 2 and revise.

---

### PHASE 4 — OUTPUT PRODUCTION

**Entry requirement**: Phase 3 handoff artifact (gate decision record, both conditions passed) is
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

## Stakeholders
| Stakeholder | Concern | Signals-at-Risk |
{rows from Phase 1 stakeholder table}

## Decisions
| Decision | Decision-Maker Role | What Signal Makes This Decidable |
{rows from Phase 1 decision table}

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

## V-02 — Second-Person Imperative Phrasing

**Variation axis**: Phrasing register — the prompt uses second-person imperative throughout
("Do not advance...", "Confirm before beginning", "You will not execute...") instead of first-person
commitment ("I will not advance...", "I confirm...", "I will have produced..."). Consequence
warnings address the executing model as "you" rather than as a committed first-person agent.

**Hypothesis**: First-person phrasing frames constraints as self-imposed commitments the model
makes to itself — "I will not advance" positions compliance as an identity-consistent act rather
than an instruction being followed. Second-person imperative positions the same constraints as
external instructions from the prompt author. The hypothesis is that first-person framing produces
stronger structural compliance because the model internalizes the constraint as a self-attribution
("I am the kind of executor that does not skip gates") rather than as a received instruction
that could be overridden. If V-02 scores lower than V-01 on structural compliance criteria,
first-person phrasing is confirmed as load-bearing. If V-02 scores equally, the distinction
is cosmetic and the axis is neutral.

---

You are registering a new topic for the Signal plugin and producing a complete investigation
strategy. Every constraint in this prompt applies to your execution. Read the FIELD SCHEMA before
the pipeline overview.

---

### FIELD SCHEMA — Read first. Schema row order defines signal table column order.

**Schema row order = table column order. F-01=Priority is column 1 of every signal table. A column
order change requires a schema row sequence change first.**

| ID | Field | Canonical Values | Decision-State Anchor | If You Violate This, You Will... |
|----|-------|-----------------|-----------------------|----------------------------------|
| F-01 | Priority | essential / recommended / optional | essential = cannot decide — blocked; recommended = decides with risk — exposure accepted; optional = decides unaffected — supplementary | ...write "high/medium/low" — no anchor maps to any decision state — strategy fails C-04 and cannot serve as a commit gate |
| F-02 | Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | — | ...route signals to a nonexistent namespace, breaking downstream invocation |
| F-03 | Skill | skill name within namespace | — | ...name an uninvokable skill no team member can execute |
| F-04 | Item Name | {topic}-{signal}-{date}.md | — | ...create an artifact the registry cannot locate |
| F-05 | Producer → Consumer | "{role} → {decision-maker role}" — Consumer must appear verbatim as a Decision-Maker Role in Phase 1 decision table | — | ...name a consumer with no decision-table entry — priority assignment floats free of any verifiable decision context |

Signal table column order: **Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04)
| Producer → Consumer (F-05)**

**Priority anchor reminder**: before assigning any priority value, identify the consumer role (F-05)
first. Then map: does the consumer's decision block on this signal (essential), proceed with risk
(recommended), or proceed unaffected (optional)?

**F-05 traceability rule**: Consumer value must appear verbatim as a Decision-Maker Role in the
Phase 1 decision table. A consumer role not present in any Phase 1 decision-table row severs the
chain from signal to decision.

---

### PIPELINE OVERVIEW — Read this entire table before executing Phase 0. All exit gates and consequences are declared here.

| Phase | Purpose | Handoff Artifact | Exit Gate | If You Skip This Phase, You Will... | Team Default When This Is Skipped | Recovery Rework Chain (Late Detection) |
|-------|---------|-----------------|----------|-------------------------------------|-----------------------------------|----------------------------------------|
| 0 | Confirm inputs | Confirmed-inputs record (topic name + description, both non-empty) | Both inputs confirmed | ...produce a strategy for an unnamed feature — Phase 1 has nothing to anchor stakeholders or decisions to | Teams name features in the moment and write strategies without anchoring scope | Re-confirm topic name and description independently; discard all Phase 1 outputs; restart Phase 1 from scratch |
| 1 | Identify decisions + stakeholders | Decision table (≥ 3 rows, all cells complete) + stakeholder table (≥ 3 rows, all cells complete) | Both tables complete with ≥ 3 rows each, all cells filled | ...plan signals without consumer roles grounded in real decisions — priority anchors collapse to intuition | Teams plan signals from habit; no one checks whether each signal unblocks a decision-maker | Re-run Phase 1 (rebuild both tables from confirmed inputs); re-run Phase 2 (rebuild signal table with corrected consumer roster); rewrite strategy.md |
| 2 | Plan signals | Signal table (schema-ordered, F-01 first, ≥ 1 essential, all F-05 Consumers traceable to Phase 1 decision table) | ≥ 1 essential, all F-05 Consumers traceable, all cells complete | ...produce signals whose consumers are orphaned from any decision — essential/optional become synonyms for "feels important" / "feels minor" | Teams write priority as importance ranking; all borderline signals become recommended by default | Re-run Phase 2 applying decision-state anchor to every row; rewrite signal table; re-run Phase 3 |
| 3 | Commit gate | Gate decision record (both conditions passed, or return directive) | Both conditions independently verified | ...write TOPICS.md before the strategy passes its own gates — you will have attested to readiness not yet verified | Teams advance to implementation after visual scan of the signal list | Re-run Phase 3 against corrected signal table; if either condition fails return to Phase 2; rewrite gate record; rewrite both output files |
| 4 | Write outputs | TOPICS.md entry + strategy.md at correct paths | Both files written | ...leave the topic unregistered — no other skill can find or build on these signals | Teams keep strategies in personal notes that drift from actual implementation | Re-run Phase 4; write TOPICS.md entry and strategy.md to canonical paths; re-register topic |

Do not execute Phase 0 until you have processed every row including all three consequence columns.

**Handoff-artifact rule**: Before beginning any phase, confirm the previous phase's handoff artifact
is present and complete. Executing a phase does not substitute for presence of its handoff artifact.

---

### PHASE 0 — INPUT VALIDATION

**Handoff artifact to produce**: Confirmed-inputs record — topic name and description, both non-empty.

- Topic name: {topic}
- Topic description: {description}

**Check these two items independently. Do not advance to Phase 1 until both are confirmed
separately:**
- [ ] Topic name is present and non-empty
- [ ] Topic description is present and non-empty

**Do not advance until both boxes are checked independently.**

**If checked sequentially**: confirming the topic name may lead you to treat the description as
implicitly present. Phase 1 will have no scope to anchor stakeholders or decisions to — every
stakeholder and decision identified will float free of any feature boundary.

---

### PHASE 1 — DECISION AND STAKEHOLDER IDENTIFICATION

**Entry requirement**: Phase 0 handoff artifact (confirmed-inputs record) is present and complete.
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

**Check these four items independently. Do not advance to Phase 2 until all four are satisfied
separately:**
- [ ] Decision table has at least 3 rows
- [ ] Every cell in the decision table is complete — no empty cells
- [ ] Stakeholder table has at least 3 rows
- [ ] Every cell in the stakeholder table is complete — no empty cells

**Do not advance until all four boxes are checked independently.**

**If checked sequentially**: completing the row-count checks may cause you to treat cell completeness
as already verified. You will advance with decision-maker roles named but no "What Signal Makes
This Decidable" mapping — Phase 2 has consumer names but no basis for applying the F-01
decision-state anchor. Teams plan signals from habit when decision mapping is absent; you will have
produced the structural equivalent.

---

### PHASE 2 — SIGNAL PLANNING

**Entry requirement**: Phase 1 handoff artifacts (decision table + stakeholder table) are both
present and complete. Confirm before beginning.

**Handoff artifact to produce**: Signal table, schema-ordered with F-01 first, all cells complete,
≥ 1 essential, every F-05 Consumer appearing verbatim as a Decision-Maker Role in the Phase 1
decision table.

Column order follows FIELD SCHEMA — **schema row order = table column order, F-01=Priority first**.

**Before assigning Priority for each row, identify the Consumer role (F-05) from the Phase 1
decision table and apply the F-01 decision-state anchor:**
- **essential** — the named consumer cannot decide without this signal (decision blocked)
- **recommended** — the named consumer decides with increased exposure (quality risk accepted)
- **optional** — the named consumer decides unaffected (supplementary enrichment only)

Priority vocabulary: **essential / recommended / optional only**. "High/medium/low" has no
decision-state anchor and fails C-04.

| Priority | Namespace | Skill | Item Name | Producer → Consumer |
|----------|-----------|-------|-----------|---------------------|

**Check these three items independently. Do not advance to Phase 3 until all three are satisfied
separately:**
- [ ] [F-01] At least one row has Priority = essential
- [ ] [F-05] Every cell contains "{role} → {role}" format with both producer and consumer named
- [ ] [F-05] Every Consumer value appears verbatim as a Decision-Maker Role in the Phase 1 decision table

**Do not advance until all three boxes are checked independently.**

**If checked sequentially**: confirming essential-signal presence may lead you to treat F-05 format
and F-05 traceability as already verified. You will advance with F-05 cells that name a consumer
role not present in the decision table — the traceability chain is severed. Teams write consumer
roles as job titles without checking whether those roles appeared in the decision table; you will
have produced the structural equivalent.

---

### PHASE 3 — COMMIT GATE

**Entry requirement**: Phase 2 handoff artifact (complete signal table) is present and complete.
Confirm before beginning.

**Handoff artifact to produce**: Gate decision record — both conditions passed (advance to Phase 4)
or return directive (return to Phase 2 and revise).

Do not write any output until both conditions are independently satisfied.

**Check these two items independently. Do not advance to Phase 4 until both are verified
separately:**
- [ ] [F-01] At least one row has Priority = essential — confirmed against the decision-state
  anchor: at least one consumer's decision is blocked without a planned signal
- [ ] [F-05] At least two distinct Consumer roles appear — signals reach at least two different
  decision-makers, and both Consumer roles appear verbatim in the Phase 1 decision table

**Do not advance until both boxes are checked independently.**

**If checked sequentially**: confirming the essential-signal condition may lead you to rationalize
consumer diversity as already present. You will advance past a strategy where every signal feeds
the same decision-maker — no peer can independently validate coverage. Teams scan visually and
declare readiness; you will have attested to a gate decision record that overstates verified
conditions.

If either condition fails, return to Phase 2 and revise.

---

### PHASE 4 — OUTPUT PRODUCTION

**Entry requirement**: Phase 3 handoff artifact (gate decision record, both conditions passed) is
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

## V-03 — Dedicated INERTIA REGISTER Block

**Variation axis**: Inertia framing — a named INERTIA REGISTER block appears before FIELD SCHEMA,
listing all five team defaults as numbered register entries (IR-01 through IR-05). The pipeline
table "Team Default When This Is Skipped" column becomes a back-reference ("→ IR-01") rather than
prose, keeping the table compact. The register block makes the status-quo competitor maximally
prominent and gives each inertia pattern a name that can be cited in phase warnings.

**Hypothesis**: The current form embeds team defaults as prose cells within the pipeline table —
visible once during the mandatory pipeline-overview read, then accessible only by re-scanning the
table. A dedicated register block surfaced before FIELD SCHEMA makes every inertia default a
named, titled, first-class concept. Phase consequence warnings can then cite "→ IR-03: Teams write
priority as importance ranking" rather than restating the default inline. The hypothesis is that
elevating inertia to a named register increases the probability that the model recognizes the
specific team default it is overriding at each phase, rather than treating phase warnings as
boilerplate. If IR back-references appear in model outputs (explicitly naming which inertia default
is being overridden), the axis surfaces an excellence signal worth promoting to a criterion.

---

You are registering a new topic for the Signal plugin and producing a complete investigation
strategy. Every constraint applies to you as the executing model. Read the INERTIA REGISTER, then
the FIELD SCHEMA, then the pipeline overview — in that order.

---

### INERTIA REGISTER — Read this before FIELD SCHEMA. These are the five team defaults this strategy is designed to override.

| IR | Phase | Team Default | What This Strategy Does Instead |
|----|-------|-------------|----------------------------------|
| IR-01 | 0 | Teams name features in the moment and write strategies without anchoring scope description | Phase 0 independently confirms topic name and description before any Phase 1 work begins |
| IR-02 | 1 | Teams plan signals from habit; no one checks whether each signal unblocks a decision-maker | Phase 1 builds a decision table mapping every decision to a decision-maker role and what makes it decidable |
| IR-03 | 2 | Teams write priority as importance ranking; all borderline signals become recommended by default | Phase 2 applies the F-01 decision-state anchor (blocked / risk-accepted / unaffected) before assigning every priority value |
| IR-04 | 3 | Teams advance to implementation after visual scan of the signal list | Phase 3 verifies two gate conditions independently — sequential checks do not substitute for independent verification |
| IR-05 | 4 | Teams keep strategies in personal notes that drift from actual implementation | Phase 4 writes both TOPICS.md entry and strategy.md to canonical file system paths |

If I complete any phase without overriding its registered inertia default, I will have produced
the team default — not a Signal-grade artifact.

---

### FIELD SCHEMA — Read second. Schema row order defines signal table column order.

**Schema row order = table column order. F-01=Priority is column 1 of every signal table. A column
order change requires a schema row sequence change first.**

| ID | Field | Canonical Values | Decision-State Anchor | If I Violate This, I Will... |
|----|-------|-----------------|-----------------------|------------------------------|
| F-01 | Priority | essential / recommended / optional | essential = cannot decide — blocked; recommended = decides with risk — exposure accepted; optional = decides unaffected — supplementary | ...write "high/medium/low" — no anchor maps to any decision state — strategy fails C-04 and cannot serve as a commit gate |
| F-02 | Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | — | ...route signals to a nonexistent namespace, breaking downstream invocation |
| F-03 | Skill | skill name within namespace | — | ...name an uninvokable skill no team member can execute |
| F-04 | Item Name | {topic}-{signal}-{date}.md | — | ...create an artifact the registry cannot locate |
| F-05 | Producer → Consumer | "{role} → {decision-maker role}" — Consumer must appear verbatim as a Decision-Maker Role in Phase 1 decision table | — | ...name a consumer with no decision-table entry — priority assignment floats free of any verifiable decision context |

Signal table column order: **Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04)
| Producer → Consumer (F-05)**

**Priority anchor reminder**: before assigning any priority value, identify the consumer role (F-05)
first. Then map: does the consumer's decision block on this signal (essential), proceed with risk
(recommended), or proceed unaffected (optional)?

**F-05 traceability rule**: Consumer value must appear verbatim as a Decision-Maker Role in the
Phase 1 decision table. A consumer role invented at fill time that does not correspond to any
Phase 1 decision-table row severs the chain from signal to decision.

---

### PIPELINE OVERVIEW — Read this entire table before executing Phase 0. All exit gates and consequences are declared here.

| Phase | Purpose | Handoff Artifact | Exit Gate | If I Skip This Phase, I Will... | Team Default | Recovery Rework Chain (Late Detection) |
|-------|---------|-----------------|----------|---------------------------------|--------------|----------------------------------------|
| 0 | Confirm inputs | Confirmed-inputs record (topic name + description, both non-empty) | Both inputs confirmed | ...produce a strategy for an unnamed feature — Phase 1 has nothing to anchor stakeholders or decisions to | → IR-01 | Re-confirm topic name and description independently; discard all Phase 1 outputs; restart Phase 1 from scratch |
| 1 | Identify decisions + stakeholders | Decision table (≥ 3 rows, all cells complete) + stakeholder table (≥ 3 rows, all cells complete) | Both tables complete with ≥ 3 rows each, all cells filled | ...plan signals without consumer roles grounded in real decisions — priority anchors collapse to intuition | → IR-02 | Re-run Phase 1 (rebuild both tables from confirmed inputs); re-run Phase 2 (rebuild signal table with corrected consumer roster); rewrite strategy.md |
| 2 | Plan signals | Signal table (schema-ordered, F-01 first, ≥ 1 essential, all F-05 Consumers traceable to Phase 1 decision table) | ≥ 1 essential, all F-05 Consumers traceable, all cells complete | ...produce signals whose consumers are orphaned from any decision — essential/optional become synonyms for "feels important" / "feels minor" | → IR-03 | Re-run Phase 2 applying decision-state anchor to every row; rewrite signal table; re-run Phase 3 |
| 3 | Commit gate | Gate decision record (both conditions passed, or return directive) | Both conditions independently verified | ...write TOPICS.md before the strategy passes its own gates — I will have attested to readiness I have not verified | → IR-04 | Re-run Phase 3 against corrected signal table; if either condition fails return to Phase 2; rewrite gate record; rewrite both output files |
| 4 | Write outputs | TOPICS.md entry + strategy.md at correct paths | Both files written | ...leave the topic unregistered — no other skill can find or build on these signals | → IR-05 | Re-run Phase 4; write TOPICS.md entry and strategy.md to canonical paths; re-register topic |

I will not execute Phase 0 until I have processed every row including all three consequence columns.

**Handoff-artifact rule**: Before beginning any phase, I confirm the previous phase's handoff
artifact is present and complete. Execution of a phase does not substitute for presence of its
handoff artifact.

---

### PHASE 0 — INPUT VALIDATION

**Handoff artifact to produce**: Confirmed-inputs record — topic name and description, both non-empty.

This phase overrides **IR-01**: teams name features in the moment without anchoring scope.

- Topic name: {topic}
- Topic description: {description}

**Check these two items independently. I will not advance to Phase 1 until both are confirmed
separately:**
- [ ] Topic name is present and non-empty
- [ ] Topic description is present and non-empty

**Do not advance until both boxes are checked independently.**

**If I check these sequentially**: confirming the topic name may lead me to treat the description as
implicitly present. Phase 1 will have no scope to anchor stakeholders or decisions to — every
stakeholder and decision identified will float free of any feature boundary. I will have reproduced
IR-01.

---

### PHASE 1 — DECISION AND STAKEHOLDER IDENTIFICATION

**Entry requirement**: Phase 0 handoff artifact (confirmed-inputs record) is present and complete.
Confirm before beginning.

This phase overrides **IR-02**: teams plan signals without mapping them to decisions.

**Handoff artifacts to produce:**
1. Decision table — what decisions this topic's signals must enable, who makes each decision
2. Stakeholder table — who is affected, what they care about, which signals are at risk

Phase 2 assigns Priority using the decision-state anchor from F-01. The decision table provides
the consumer roles and decision states needed to apply that anchor. If the decision table is absent,
Phase 2 has no basis for distinguishing essential from recommended — priority anchors collapse,
reproducing IR-03 before Phase 2 even runs.

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

**If I check these sequentially**: completing the row-count checks may cause me to treat cell
completeness as already verified. I will advance with decision-maker roles named but no "What
Signal Makes This Decidable" mapping — Phase 2 has consumer names but no basis for applying the
F-01 decision-state anchor. I will have reproduced IR-02.

---

### PHASE 2 — SIGNAL PLANNING

**Entry requirement**: Phase 1 handoff artifacts (decision table + stakeholder table) are both
present and complete. Confirm before beginning.

This phase overrides **IR-03**: teams write priority as an importance ranking.

**Handoff artifact to produce**: Signal table, schema-ordered with F-01 first, all cells complete,
≥ 1 essential, every F-05 Consumer appearing verbatim as a Decision-Maker Role in the Phase 1
decision table.

Column order follows FIELD SCHEMA — **schema row order = table column order, F-01=Priority first**.

**Before assigning Priority for each row, identify the Consumer role (F-05) from the Phase 1
decision table and apply the F-01 decision-state anchor:**
- **essential** — the named consumer cannot decide without this signal (decision blocked)
- **recommended** — the named consumer decides with increased exposure (quality risk accepted)
- **optional** — the named consumer decides unaffected (supplementary enrichment only)

Priority vocabulary: **essential / recommended / optional only**. "High/medium/low" has no
decision-state anchor and fails C-04.

| Priority | Namespace | Skill | Item Name | Producer → Consumer |
|----------|-----------|-------|-----------|---------------------|

**Check these three items independently. I will not advance to Phase 3 until all three are satisfied
separately:**
- [ ] [F-01] At least one row has Priority = essential
- [ ] [F-05] Every cell contains "{role} → {role}" format with both producer and consumer named
- [ ] [F-05] Every Consumer value appears verbatim as a Decision-Maker Role in the Phase 1 decision table

**Do not advance until all three boxes are checked independently.**

**If I check these sequentially**: confirming essential-signal presence may lead me to treat F-05
format and F-05 traceability as already verified. I will advance with F-05 cells that name a
consumer role not present in the decision table — the traceability chain is severed. I will have
reproduced IR-03 at the consumer-grounding level.

---

### PHASE 3 — COMMIT GATE

**Entry requirement**: Phase 2 handoff artifact (complete signal table) is present and complete.
Confirm before beginning.

This phase overrides **IR-04**: teams advance after visual scan.

**Handoff artifact to produce**: Gate decision record — both conditions passed (advance to Phase 4)
or return directive (return to Phase 2 and revise).

I will not write any output until both conditions are independently satisfied.

**Check these two items independently. I will not advance to Phase 4 until both are verified
separately:**
- [ ] [F-01] At least one row has Priority = essential — confirmed against the decision-state
  anchor: at least one consumer's decision is blocked without a planned signal
- [ ] [F-05] At least two distinct Consumer roles appear — signals reach at least two different
  decision-makers, and both Consumer roles appear verbatim in the Phase 1 decision table

**Do not advance until both boxes are checked independently.**

**If I check these sequentially**: confirming the essential-signal condition may lead me to
rationalize consumer diversity as already present. I will advance past a strategy where every
signal feeds the same decision-maker. I will have reproduced IR-04.

If either condition fails, return to Phase 2 and revise.

---

### PHASE 4 — OUTPUT PRODUCTION

**Entry requirement**: Phase 3 handoff artifact (gate decision record, both conditions passed) is
present. Confirm before beginning.

This phase overrides **IR-05**: teams keep strategies in personal notes.

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

## V-04 — Stakeholder-First + Second-Person Imperative (Axes 1+2)

**Variation axis**: Role sequence + Phrasing register — Phase 1 runs stakeholder table before
decision table (Axis 1), and all constraint language uses second-person imperative throughout
(Axis 2). Combines the people-first grounding hypothesis with the external-instruction phrasing
hypothesis.

**Hypothesis**: V-01 tests whether stakeholder-first Phase 1 ordering closes the Consumer coverage
gap. V-02 tests whether second-person phrasing weakens structural compliance relative to
first-person commitment. V-04 tests the interaction: does stakeholder-first ordering partially
compensate for any compliance weakening from second-person phrasing? If V-04 scores higher than
V-02 but equal to V-01, role sequence dominates phrasing. If V-04 scores lower than V-01 and V-02,
the axes have negative interaction. The combination also tests whether stakeholder-first ordering
is robust across phrasing registers — if it passes in both first- and second-person forms, it is
phrasing-invariant.

---

You are registering a new topic for the Signal plugin and producing a complete investigation
strategy. Every constraint in this prompt applies to your execution. Read the FIELD SCHEMA before
the pipeline overview.

---

### FIELD SCHEMA — Read first. Schema row order defines signal table column order.

**Schema row order = table column order. F-01=Priority is column 1 of every signal table. A column
order change requires a schema row sequence change first.**

| ID | Field | Canonical Values | Decision-State Anchor | If You Violate This, You Will... |
|----|-------|-----------------|-----------------------|----------------------------------|
| F-01 | Priority | essential / recommended / optional | essential = cannot decide — blocked; recommended = decides with risk — exposure accepted; optional = decides unaffected — supplementary | ...write "high/medium/low" — no anchor maps to any decision state — strategy fails C-04 and cannot serve as a commit gate |
| F-02 | Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | — | ...route signals to a nonexistent namespace, breaking downstream invocation |
| F-03 | Skill | skill name within namespace | — | ...name an uninvokable skill no team member can execute |
| F-04 | Item Name | {topic}-{signal}-{date}.md | — | ...create an artifact the registry cannot locate |
| F-05 | Producer → Consumer | "{role} → {decision-maker role}" — Consumer must appear verbatim as a Decision-Maker Role in Phase 1 decision table | — | ...name a consumer with no decision-table entry — priority assignment floats free of any verifiable decision context |

Signal table column order: **Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04)
| Producer → Consumer (F-05)**

**Priority anchor reminder**: before assigning any priority value, identify the consumer role (F-05)
first. Then map: does the consumer's decision block on this signal (essential), proceed with risk
(recommended), or proceed unaffected (optional)?

**F-05 traceability rule**: Consumer value must appear verbatim as a Decision-Maker Role in the
Phase 1 decision table. A consumer role not present in any Phase 1 decision-table row severs the
chain from signal to decision.

---

### PIPELINE OVERVIEW — Read this entire table before executing Phase 0. All exit gates and consequences are declared here.

| Phase | Purpose | Handoff Artifact | Exit Gate | If You Skip This Phase, You Will... | Team Default When This Is Skipped | Recovery Rework Chain (Late Detection) |
|-------|---------|-----------------|----------|-------------------------------------|-----------------------------------|----------------------------------------|
| 0 | Confirm inputs | Confirmed-inputs record (topic name + description, both non-empty) | Both inputs confirmed | ...produce a strategy for an unnamed feature — Phase 1 has nothing to anchor stakeholders or decisions to | Teams name features in the moment and write strategies without anchoring scope | Re-confirm topic name and description independently; discard all Phase 1 outputs; restart Phase 1 from scratch |
| 1 | Identify stakeholders + decisions | Stakeholder table (≥ 3 rows, all cells complete) + decision table (≥ 3 rows, all cells complete) | Both tables complete with ≥ 3 rows each, all cells filled | ...plan signals without consumer roles grounded in real decisions — priority anchors collapse to intuition | Teams plan signals from habit; no one checks whether each signal unblocks a decision-maker | Re-run Phase 1 (rebuild both tables from confirmed inputs); re-run Phase 2 (rebuild signal table with corrected consumer roster); rewrite strategy.md |
| 2 | Plan signals | Signal table (schema-ordered, F-01 first, ≥ 1 essential, all F-05 Consumers traceable to Phase 1 decision table) | ≥ 1 essential, all F-05 Consumers traceable, all cells complete | ...produce signals whose consumers are orphaned from any decision — essential/optional become synonyms for "feels important" / "feels minor" | Teams write priority as importance ranking; all borderline signals become recommended by default | Re-run Phase 2 applying decision-state anchor to every row; rewrite signal table; re-run Phase 3 |
| 3 | Commit gate | Gate decision record (both conditions passed, or return directive) | Both conditions independently verified | ...write TOPICS.md before the strategy passes its own gates — you will have attested to readiness not yet verified | Teams advance to implementation after visual scan of the signal list | Re-run Phase 3 against corrected signal table; if either condition fails return to Phase 2; rewrite gate record; rewrite both output files |
| 4 | Write outputs | TOPICS.md entry + strategy.md at correct paths | Both files written | ...leave the topic unregistered — no other skill can find or build on these signals | Teams keep strategies in personal notes that drift from actual implementation | Re-run Phase 4; write TOPICS.md entry and strategy.md to canonical paths; re-register topic |

Do not execute Phase 0 until you have processed every row including all three consequence columns.

**Handoff-artifact rule**: Before beginning any phase, confirm the previous phase's handoff artifact
is present and complete. Executing a phase does not substitute for presence of its handoff artifact.

---

### PHASE 0 — INPUT VALIDATION

**Handoff artifact to produce**: Confirmed-inputs record — topic name and description, both non-empty.

- Topic name: {topic}
- Topic description: {description}

**Check these two items independently. Do not advance to Phase 1 until both are confirmed
separately:**
- [ ] Topic name is present and non-empty
- [ ] Topic description is present and non-empty

**Do not advance until both boxes are checked independently.**

**If checked sequentially**: confirming the topic name may lead you to treat the description as
implicitly present. Phase 1 will have no scope to anchor stakeholders or decisions to — every
stakeholder and decision identified will float free of any feature boundary.

---

### PHASE 1 — STAKEHOLDER AND DECISION IDENTIFICATION

**Entry requirement**: Phase 0 handoff artifact (confirmed-inputs record) is present and complete.
Confirm before beginning.

**Handoff artifacts to produce:**
1. Stakeholder table — who is affected, what they care about, which signals are at risk
2. Decision table — what decisions this topic's signals must enable, who makes each decision

**Run stakeholder identification first.** The stakeholder table surfaces the full population of
affected parties. The decision table then identifies which stakeholders are decision-makers and
maps each decision to what signal makes it decidable. Phase 2 F-05 Consumer values must appear
verbatim as Decision-Maker Role entries in the decision table. Building the stakeholder table first
ensures the decision table's Decision-Maker Roles are drawn from a complete people roster rather
than generated independently from feature knowledge.

**Stakeholder table — run first:**
| Stakeholder | Concern | Signals-at-Risk |
|-------------|---------|----------------|

**Decision table — run second (Decision-Maker Roles must trace to stakeholder rows):**
| Decision | Decision-Maker Role | What Signal Makes This Decidable |
|----------|---------------------|----------------------------------|

**Check these four items independently. Do not advance to Phase 2 until all four are satisfied
separately:**
- [ ] Stakeholder table has at least 3 rows
- [ ] Every cell in the stakeholder table is complete — no empty cells
- [ ] Decision table has at least 3 rows
- [ ] Every cell in the decision table is complete — no empty cells

**Do not advance until all four boxes are checked independently.**

**If checked sequentially**: completing the row-count checks may cause you to treat cell completeness
as already verified. You will advance with decision-maker roles named but no "What Signal Makes
This Decidable" mapping — Phase 2 has consumer names but no basis for applying the F-01
decision-state anchor. Teams plan signals from habit when decision mapping is absent; you will have
produced the structural equivalent.

---

### PHASE 2 — SIGNAL PLANNING

**Entry requirement**: Phase 1 handoff artifacts (stakeholder table + decision table) are both
present and complete. Confirm before beginning.

**Handoff artifact to produce**: Signal table, schema-ordered with F-01 first, all cells complete,
≥ 1 essential, every F-05 Consumer appearing verbatim as a Decision-Maker Role in the Phase 1
decision table.

Column order follows FIELD SCHEMA — **schema row order = table column order, F-01=Priority first**.

**Before assigning Priority for each row, identify the Consumer role (F-05) from the Phase 1
decision table and apply the F-01 decision-state anchor:**
- **essential** — the named consumer cannot decide without this signal (decision blocked)
- **recommended** — the named consumer decides with increased exposure (quality risk accepted)
- **optional** — the named consumer decides unaffected (supplementary enrichment only)

Priority vocabulary: **essential / recommended / optional only**. "High/medium/low" has no
decision-state anchor and fails C-04.

| Priority | Namespace | Skill | Item Name | Producer → Consumer |
|----------|-----------|-------|-----------|---------------------|

**Check these three items independently. Do not advance to Phase 3 until all three are satisfied
separately:**
- [ ] [F-01] At least one row has Priority = essential
- [ ] [F-05] Every cell contains "{role} → {role}" format with both producer and consumer named
- [ ] [F-05] Every Consumer value appears verbatim as a Decision-Maker Role in the Phase 1 decision table

**Do not advance until all three boxes are checked independently.**

**If checked sequentially**: confirming essential-signal presence may lead you to treat F-05 format
and F-05 traceability as already verified. You will advance with F-05 cells that name a consumer
role not present in the decision table — the traceability chain is severed. Teams write consumer
roles as job titles without checking whether those roles appeared in the decision table; you will
have produced the structural equivalent.

---

### PHASE 3 — COMMIT GATE

**Entry requirement**: Phase 2 handoff artifact (complete signal table) is present and complete.
Confirm before beginning.

**Handoff artifact to produce**: Gate decision record — both conditions passed (advance to Phase 4)
or return directive (return to Phase 2 and revise).

Do not write any output until both conditions are independently satisfied.

**Check these two items independently. Do not advance to Phase 4 until both are verified
separately:**
- [ ] [F-01] At least one row has Priority = essential — confirmed against the decision-state
  anchor: at least one consumer's decision is blocked without a planned signal
- [ ] [F-05] At least two distinct Consumer roles appear — signals reach at least two different
  decision-makers, and both Consumer roles appear verbatim in the Phase 1 decision table

**Do not advance until both boxes are checked independently.**

**If checked sequentially**: confirming the essential-signal condition may lead you to rationalize
consumer diversity as already present. You will advance past a strategy where every signal feeds
the same decision-maker — no peer can independently validate coverage. Teams scan visually and
declare readiness; you will have attested to a gate decision record that overstates verified
conditions.

If either condition fails, return to Phase 2 and revise.

---

### PHASE 4 — OUTPUT PRODUCTION

**Entry requirement**: Phase 3 handoff artifact (gate decision record, both conditions passed) is
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

## Stakeholders
| Stakeholder | Concern | Signals-at-Risk |
{rows from Phase 1 stakeholder table}

## Decisions
| Decision | Decision-Maker Role | What Signal Makes This Decidable |
{rows from Phase 1 decision table}

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

## V-05 — Stakeholder-First + Second-Person + INERTIA REGISTER (All Three Axes)

**Variation axis**: Role sequence + Phrasing register + Inertia framing — combines all three axes.
Phase 1 runs stakeholder table first (Axis 1). All constraint language uses second-person imperative
(Axis 2). A named INERTIA REGISTER block appears before FIELD SCHEMA with pipeline table
back-references (Axis 3).

**Hypothesis**: V-05 is the maximum-surface variation. The three axes are designed to be
independently beneficial: stakeholder-first closes Consumer coverage gaps (Axis 1), second-person
tests phrasing neutrality (Axis 2), and the INERTIA REGISTER elevates status-quo competitors to
named first-class concepts (Axis 3). If all three are independently beneficial, V-05 should score
highest. If any axis is harmful, V-05 will score lower than the single-axis variations that exclude
it. The combination also tests whether the INERTIA REGISTER IR-citation language is compatible
with second-person phrasing — "you will have reproduced IR-02" (second-person IR citation) vs.
"I will have reproduced IR-02" (first-person IR citation in V-03). The interaction between Axis 2
and Axis 3 is the unique signal of V-05.

---

You are registering a new topic for the Signal plugin and producing a complete investigation
strategy. Every constraint in this prompt applies to your execution. Read the INERTIA REGISTER,
then the FIELD SCHEMA, then the pipeline overview — in that order.

---

### INERTIA REGISTER — Read this before FIELD SCHEMA. These are the five team defaults this strategy is designed to override.

| IR | Phase | Team Default | What This Strategy Does Instead |
|----|-------|-------------|----------------------------------|
| IR-01 | 0 | Teams name features in the moment and write strategies without anchoring scope description | Phase 0 independently confirms topic name and description before any Phase 1 work begins |
| IR-02 | 1 | Teams plan signals from habit; no one checks whether each signal unblocks a decision-maker | Phase 1 builds a decision table mapping every decision to a decision-maker role and what makes it decidable |
| IR-03 | 2 | Teams write priority as importance ranking; all borderline signals become recommended by default | Phase 2 applies the F-01 decision-state anchor (blocked / risk-accepted / unaffected) before assigning every priority value |
| IR-04 | 3 | Teams advance to implementation after visual scan of the signal list | Phase 3 verifies two gate conditions independently — sequential checks do not substitute for independent verification |
| IR-05 | 4 | Teams keep strategies in personal notes that drift from actual implementation | Phase 4 writes both TOPICS.md entry and strategy.md to canonical file system paths |

If you complete any phase without overriding its registered inertia default, you will have produced
the team default — not a Signal-grade artifact.

---

### FIELD SCHEMA — Read second. Schema row order defines signal table column order.

**Schema row order = table column order. F-01=Priority is column 1 of every signal table. A column
order change requires a schema row sequence change first.**

| ID | Field | Canonical Values | Decision-State Anchor | If You Violate This, You Will... |
|----|-------|-----------------|-----------------------|----------------------------------|
| F-01 | Priority | essential / recommended / optional | essential = cannot decide — blocked; recommended = decides with risk — exposure accepted; optional = decides unaffected — supplementary | ...write "high/medium/low" — no anchor maps to any decision state — strategy fails C-04 and cannot serve as a commit gate |
| F-02 | Namespace | scout / draft / review / flow / trace / prove / listen / program / topic | — | ...route signals to a nonexistent namespace, breaking downstream invocation |
| F-03 | Skill | skill name within namespace | — | ...name an uninvokable skill no team member can execute |
| F-04 | Item Name | {topic}-{signal}-{date}.md | — | ...create an artifact the registry cannot locate |
| F-05 | Producer → Consumer | "{role} → {decision-maker role}" — Consumer must appear verbatim as a Decision-Maker Role in Phase 1 decision table | — | ...name a consumer with no decision-table entry — priority assignment floats free of any verifiable decision context |

Signal table column order: **Priority (F-01) | Namespace (F-02) | Skill (F-03) | Item Name (F-04)
| Producer → Consumer (F-05)**

**Priority anchor reminder**: before assigning any priority value, identify the consumer role (F-05)
first. Then map: does the consumer's decision block on this signal (essential), proceed with risk
(recommended), or proceed unaffected (optional)?

**F-05 traceability rule**: Consumer value must appear verbatim as a Decision-Maker Role in the
Phase 1 decision table. A consumer role not present in any Phase 1 decision-table row severs the
chain from signal to decision.

---

### PIPELINE OVERVIEW — Read this entire table before executing Phase 0. All exit gates and consequences are declared here.

| Phase | Purpose | Handoff Artifact | Exit Gate | If You Skip This Phase, You Will... | Team Default | Recovery Rework Chain (Late Detection) |
|-------|---------|-----------------|----------|-------------------------------------|--------------|----------------------------------------|
| 0 | Confirm inputs | Confirmed-inputs record (topic name + description, both non-empty) | Both inputs confirmed | ...produce a strategy for an unnamed feature — Phase 1 has nothing to anchor stakeholders or decisions to | → IR-01 | Re-confirm topic name and description independently; discard all Phase 1 outputs; restart Phase 1 from scratch |
| 1 | Identify stakeholders + decisions | Stakeholder table (≥ 3 rows, all cells complete) + decision table (≥ 3 rows, all cells complete) | Both tables complete with ≥ 3 rows each, all cells filled | ...plan signals without consumer roles grounded in real decisions — priority anchors collapse to intuition | → IR-02 | Re-run Phase 1 (rebuild both tables from confirmed inputs); re-run Phase 2 (rebuild signal table with corrected consumer roster); rewrite strategy.md |
| 2 | Plan signals | Signal table (schema-ordered, F-01 first, ≥ 1 essential, all F-05 Consumers traceable to Phase 1 decision table) | ≥ 1 essential, all F-05 Consumers traceable, all cells complete | ...produce signals whose consumers are orphaned from any decision — essential/optional become synonyms for "feels important" / "feels minor" | → IR-03 | Re-run Phase 2 applying decision-state anchor to every row; rewrite signal table; re-run Phase 3 |
| 3 | Commit gate | Gate decision record (both conditions passed, or return directive) | Both conditions independently verified | ...write TOPICS.md before the strategy passes its own gates — you will have attested to readiness not yet verified | → IR-04 | Re-run Phase 3 against corrected signal table; if either condition fails return to Phase 2; rewrite gate record; rewrite both output files |
| 4 | Write outputs | TOPICS.md entry + strategy.md at correct paths | Both files written | ...leave the topic unregistered — no other skill can find or build on these signals | → IR-05 | Re-run Phase 4; write TOPICS.md entry and strategy.md to canonical paths; re-register topic |

Do not execute Phase 0 until you have processed every row including all three consequence columns.

**Handoff-artifact rule**: Before beginning any phase, confirm the previous phase's handoff artifact
is present and complete. Executing a phase does not substitute for presence of its handoff artifact.

---

### PHASE 0 — INPUT VALIDATION

**Handoff artifact to produce**: Confirmed-inputs record — topic name and description, both non-empty.

This phase overrides **IR-01**: teams name features in the moment without anchoring scope.

- Topic name: {topic}
- Topic description: {description}

**Check these two items independently. Do not advance to Phase 1 until both are confirmed
separately:**
- [ ] Topic name is present and non-empty
- [ ] Topic description is present and non-empty

**Do not advance until both boxes are checked independently.**

**If checked sequentially**: confirming the topic name may lead you to treat the description as
implicitly present. Phase 1 will have no scope to anchor stakeholders or decisions to — every
stakeholder and decision identified will float free of any feature boundary. You will have
reproduced IR-01.

---

### PHASE 1 — STAKEHOLDER AND DECISION IDENTIFICATION

**Entry requirement**: Phase 0 handoff artifact (confirmed-inputs record) is present and complete.
Confirm before beginning.

This phase overrides **IR-02**: teams plan signals without mapping them to decisions.

**Handoff artifacts to produce:**
1. Stakeholder table — who is affected, what they care about, which signals are at risk
2. Decision table — what decisions this topic's signals must enable, who makes each decision

**Run stakeholder identification first.** The stakeholder table surfaces the full population of
affected parties. The decision table then identifies which stakeholders are decision-makers and
maps each decision to what signal makes it decidable. Phase 2 F-05 Consumer values must appear
verbatim as Decision-Maker Role entries in the decision table. Building the stakeholder table first
ensures the decision table's Decision-Maker Roles are drawn from a complete people roster rather
than generated independently from feature knowledge.

**Stakeholder table — run first:**
| Stakeholder | Concern | Signals-at-Risk |
|-------------|---------|----------------|

**Decision table — run second (Decision-Maker Roles must trace to stakeholder rows):**
| Decision | Decision-Maker Role | What Signal Makes This Decidable |
|----------|---------------------|----------------------------------|

**Check these four items independently. Do not advance to Phase 2 until all four are satisfied
separately:**
- [ ] Stakeholder table has at least 3 rows
- [ ] Every cell in the stakeholder table is complete — no empty cells
- [ ] Decision table has at least 3 rows
- [ ] Every cell in the decision table is complete — no empty cells

**Do not advance until all four boxes are checked independently.**

**If checked sequentially**: completing the row-count checks may cause you to treat cell completeness
as already verified. You will advance with decision-maker roles named but no "What Signal Makes
This Decidable" mapping — Phase 2 has consumer names but no basis for applying the F-01
decision-state anchor. You will have reproduced IR-02.

---

### PHASE 2 — SIGNAL PLANNING

**Entry requirement**: Phase 1 handoff artifacts (stakeholder table + decision table) are both
present and complete. Confirm before beginning.

This phase overrides **IR-03**: teams write priority as an importance ranking.

**Handoff artifact to produce**: Signal table, schema-ordered with F-01 first, all cells complete,
≥ 1 essential, every F-05 Consumer appearing verbatim as a Decision-Maker Role in the Phase 1
decision table.

Column order follows FIELD SCHEMA — **schema row order = table column order, F-01=Priority first**.

**Before assigning Priority for each row, identify the Consumer role (F-05) from the Phase 1
decision table and apply the F-01 decision-state anchor:**
- **essential** — the named consumer cannot decide without this signal (decision blocked)
- **recommended** — the named consumer decides with increased exposure (quality risk accepted)
- **optional** — the named consumer decides unaffected (supplementary enrichment only)

Priority vocabulary: **essential / recommended / optional only**. "High/medium/low" has no
decision-state anchor and fails C-04.

| Priority | Namespace | Skill | Item Name | Producer → Consumer |
|----------|-----------|-------|-----------|---------------------|

**Check these three items independently. Do not advance to Phase 3 until all three are satisfied
separately:**
- [ ] [F-01] At least one row has Priority = essential
- [ ] [F-05] Every cell contains "{role} → {role}" format with both producer and consumer named
- [ ] [F-05] Every Consumer value appears verbatim as a Decision-Maker Role in the Phase 1 decision table

**Do not advance until all three boxes are checked independently.**

**If checked sequentially**: confirming essential-signal presence may lead you to treat F-05 format
and F-05 traceability as already verified. You will advance with F-05 cells that name a consumer
role not present in the decision table — the traceability chain is severed. You will have reproduced
IR-03 at the consumer-grounding level.

---

### PHASE 3 — COMMIT GATE

**Entry requirement**: Phase 2 handoff artifact (complete signal table) is present and complete.
Confirm before beginning.

This phase overrides **IR-04**: teams advance after visual scan.

**Handoff artifact to produce**: Gate decision record — both conditions passed (advance to Phase 4)
or return directive (return to Phase 2 and revise).

Do not write any output until both conditions are independently satisfied.

**Check these two items independently. Do not advance to Phase 4 until both are verified
separately:**
- [ ] [F-01] At least one row has Priority = essential — confirmed against the decision-state
  anchor: at least one consumer's decision is blocked without a planned signal
- [ ] [F-05] At least two distinct Consumer roles appear — signals reach at least two different
  decision-makers, and both Consumer roles appear verbatim in the Phase 1 decision table

**Do not advance until both boxes are checked independently.**

**If checked sequentially**: confirming the essential-signal condition may lead you to rationalize
consumer diversity as already present. You will advance past a strategy where every signal feeds
the same decision-maker. You will have reproduced IR-04.

If either condition fails, return to Phase 2 and revise.

---

### PHASE 4 — OUTPUT PRODUCTION

**Entry requirement**: Phase 3 handoff artifact (gate decision record, both conditions passed) is
present. Confirm before beginning.

This phase overrides **IR-05**: teams keep strategies in personal notes.

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

## Stakeholders
| Stakeholder | Concern | Signals-at-Risk |
{rows from Phase 1 stakeholder table}

## Decisions
| Decision | Decision-Maker Role | What Signal Makes This Decidable |
{rows from Phase 1 decision table}

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

## Scoring Predictions

| Variation | ES-1 (Stakeholder-first) | ES-2 (Second-person) | ES-3 (Inertia Register) | Expected Invariant Score | Notes |
|-----------|--------------------------|----------------------|------------------------|--------------------------|-------|
| V-01 | PASS | FAIL | FAIL | 41/41 | Single-axis; phrasing neutral on invariants |
| V-02 | FAIL | PASS | FAIL | 41/41 | Phrasing change leaves structural criteria unchanged |
| V-03 | FAIL | FAIL | PASS | 41/41 | IR block + back-references; inertia register is additive |
| V-04 | PASS | PASS | FAIL | 41/41 | Combination of V-01 + V-02; no structural conflict |
| V-05 | PASS | PASS | PASS | 41/41 | All three axes; IR-citation language in second-person is the unique signal |

**C-18 / C-20 status**: Both are expected to remain as aspirational failures across all R13
variations. C-18 (COVERAGE SCHEMA) and C-20 (Temporal tiers) require structural additions not
targeted by any R13 axis. They are candidates for R14 exploration.

**ES signal to watch in V-03 and V-05**: Does the model's output explicitly cite IR back-references
when describing what inertia it is overriding? If model outputs contain "overriding IR-02" or
"→ IR-03" language, that is the excellence signal for a potential C-42 criterion requiring
per-phase inertia citation in the Rationale section of strategy.md.

**ES signal to watch in V-01 and V-04**: Does the decision table's Decision-Maker Role column
show broader coverage (more distinct roles) when derived from a prior stakeholder table? If
stakeholder-first produces demonstrably more complete consumer rosters, that is the excellence
signal for a potential C-43 criterion requiring stakeholder-first Phase 1 ordering with explicit
derivation note.
