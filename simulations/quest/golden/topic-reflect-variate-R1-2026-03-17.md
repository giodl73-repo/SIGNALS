---
skill: quest-variate
skill_target: topic-reflect
date: 2026-03-17
round: 1
rubric: v1
rubric_file: simulations/quest/rubrics/topic-echo-rubric-v1-2026-03-17.md
---

# Variations: `topic:reflect` — Round 1 (2026-03-17)

**Rubric:** v1 (2026-03-17) | **Criteria:** 32 (5 essential / 3 recommended / 24 aspirational)

---

## Design Context

This is the inaugural variation set for `topic-reflect`, the renamed and expanded form of
`topic-echo`. The governing question is unchanged: *What did we learn that we did not expect?*
The key structural additions in this rubric generation are:

1. **Build Risk** — a fourth Stage 4 sub-field distinct from Design Impact, naming what is
   implicated (risk-surface) rather than what must change (forward-looking).
2. **Calibration Entry (Surprise 0)** — a pre-populated worked example positioned immediately
   before the live entry loop, labeled to prevent treatment as a live entry.
3. **Stage 7** — structurally separates artifact delivery from the Stage 6 verdict table.
4. **Field Reference block** — consolidates all four sub-field definitions before the entry loop.
5. **C-32 antipattern exclusion** in Signal Source field definition.

Five variation axes are exercised:
- V-01: Single axis — Formal/Specification Register
- V-02: Single axis — Prose-First Output Format (Stage 4)
- V-03: Single axis — Three Named Roles (Signal Archaeologist → Surprise Curator → Impact Synthesizer)
- V-04: Combined — Lifecycle Emphasis + Conversational Register
- V-05: Combined — Inertia Framing + Formal Register + Role Sequence (adds "What We Expected" field)

---

## V-01 — Formal/Specification Register

### Axis Label
Single axis: Formal/Specification Register. Phrasing is precise, imperative, and structured.
All instructions are stated as requirements ("shall," "must," "is required"). Output format
uses tables for Stage 4. No conversational scaffolding.

### Hypothesis
A specification-register prompt will produce higher C-09, C-14, and C-15 scores because
formal token language is self-reinforcing: a model trained on specifications naturally
produces COMMIT tokens and GATE tokens when the surrounding phrasing is specification-style.
The trade-off risk is that formal phrasing may produce table-column entries that are too
terse to satisfy C-12 (no single-word fields) and C-22 (Build Risk as prose sub-field).

---

### Prompt Body

You are executing the `topic-reflect` skill for topic `{topic}`.

The governing question: **What did we learn that we did not expect?**

This is not a summary. It is a synthesis of surprises — institutional memory for the next
team. Each surprise must be named, traced to a specific source signal, and assessed for its
impact on design direction (what must change) and build risk (what is implicated by that
change).

---

#### Gate Overview (read before Stage 1)

The following table governs execution. All stage tokens are required. Halt conditions
are enforced before proceeding to the next stage.

| Stage | Token Required | Halt Condition | Routes To |
|-------|---------------|----------------|-----------|
| 1 | COMMIT-STAGE-1 | Fewer than 3 belief rows | Extend belief elicitation |
| 2 | COMMIT-STAGE-2 | No deviations found | Extend signal sweep |
| 3 | COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED | No VALID deviations | Extend sweep before Stage 4 |
| 4 | COMMIT-ENTRY-[N] per row; COMMIT-STAGE-4 | Fewer than 2 GATE-CONFIRMED rows | Extend sweep |
| 5 | COMMIT-STAGE-5 | Next Team / Skill column empty | Name a skill or role before continuing |
| 6 | COMMIT-STAGE-6 | FOREKNOWLEDGE-FLAGGED unresolved | Do not proceed to Stage 7 |
| 7 | COMMIT-STAGE-7 | FOREKNOWLEDGE-FLAGGED present in Stage 6 | Halt; do not write artifact |

Execution flow: Stage 1 → Stage 2 → Stage 3 (gate) → Stage 4 (one entry per GATE-CONFIRMED
deviation) → Stage 5 → Stage 6 → Stage 7 (artifact write). No stage may be collapsed into
another. The Standalone Collapse Prohibition applies throughout.

---

#### Vocabulary Declaration (Closed Set — Binding)

The following are the only valid dimension names for use in any Epistemic Dimension cell
in this skill execution. This is a closed set. Substitution is prohibited.

**The only valid dimension names are:**
`Feasibility` · `Usability` · `Scalability` · `Adoptability` · `Correctness`

**Prohibited synonyms — do not use in any dimension cell:**

| Prohibited | Canonical Replacement |
|------------|----------------------|
| Reliability | Correctness |
| Performance | Scalability |
| Learnability | Usability |
| Viability | Feasibility |
| Reach | Adoptability |

Any dimension cell containing a prohibited synonym shall be corrected by consulting this
mapping table before the cell is emitted. No variation of the prohibited terms (e.g.,
"Reliability/Correctness," "Perf/Scalability") is permitted. The canonical names are the
only permitted names. Do not substitute, combine, or abbreviate.

This vocabulary rule takes effect at COMMIT-STAGE-1 and remains active through COMMIT-STAGE-7.
Before emitting any dimension cell, verify against this table. If a prohibited synonym is
detected in any prior stage output during review, correct it before proceeding.

---

#### Stage 1 — Opening Collective Baseline

**ENTER condition:** Vocabulary Declaration has been read and acknowledged. Gate Overview has been read.

Answer: *What did the team, as a whole, believe about `{topic}` before investigation began?*

| Field | Content |
|-------|---------|
| Opening model | [2–4 sentences describing the team's collective prior belief state about `{topic}`] |
| Epistemic profile | [1–2 canonical dimension names most central to this model] |

| Belief # | Belief (flat statement) | Domain | Epistemic Dimension |
|----------|------------------------|--------|---------------------|
| B-1 | | | |
| B-2 | | | |
| B-3 | | | |

Rules:
- Epistemic Dimension column: canonical names only (Vocabulary Declaration).
- Audit every cell before committing. If any cell contains a prohibited synonym, consult
  the canonical mapping table and correct before emitting.
- Minimum 3 belief rows. Add B-4, B-5 as needed.

**EXIT criterion:** Opening model present (2+ sentences). Epistemic profile entry present.
Minimum 3 belief rows. All dimension cells contain canonical names only.

COMMIT-STAGE-1. This table is the baseline against which Stage 6 closes.

---

#### Stage 2 — Signal Sweep

**ENTER condition:** COMMIT-STAGE-1 is present.

Read all signal artifacts for `{topic}` by globbing `simulations/**/{topic}-*`. Record
every deviation — a case where a signal showed something different from what a Stage 1
belief predicted.

| Deviation # | Belief # | What the Signal Showed | Artifact (name, namespace, date) |
|-------------|----------|------------------------|----------------------------------|
| D-1 | | | |
| D-2 | | | |
| D-N | | | |

**EXIT criterion:** At least 2 deviations recorded. Every row has a Belief # reference
and a named artifact with date.

COMMIT-STAGE-2.

---

#### Stage 3 — Adversarial Gate

**ENTER condition:** COMMIT-STAGE-2 is present.

Apply all five checks to every deviation. A VALID verdict requires all five checks to pass.

| Check | D-1 | D-2 | D-3 | D-4 | D-5 |
|-------|:---:|:---:|:---:|:---:|:---:|
| Names a specific prior belief (B-#)? | | | | | |
| Traceable to a named artifact (name + date)? | | | | | |
| Design-relevant (names component or decision — not "the system")? | | | | | |
| Genuinely unexpected (not inferable from prior knowledge alone)? | | | | | |
| Survives flat-statement test (no hedging qualifiers required)? | | | | | |
| **Verdict** (VALID / INVALID: check # — reason) | | | | | |

For each VALID deviation, emit the confirmation token. The token names Stage 4, not merely
routes toward it:

`GATE-CONFIRMED-[N]: VALID -- Stage 4.`

For each INVALID deviation, emit the rejection token with the failed check:

`GATE-REJECTED-[N]: INVALID -- Check [#]: [one sentence reason].`

**EXIT criterion:** Every deviation has a VALID or INVALID verdict. At least 2 GATE-CONFIRMED
tokens are present. If fewer than 2 deviations are VALID, extend Stage 2 before proceeding.
Before emitting Stage 3 output, scan all Epistemic Dimension cells from Stage 1 for prohibited
synonyms. If any are found, consult the Vocabulary Declaration mapping table and correct in place.

If at least 2 VALID deviations exist: emit `COMMIT-STAGE-3-CLEAN`.
If fewer than 2 VALID deviations exist after extended sweep: emit `COMMIT-STAGE-3-FLAGGED`
and return to Stage 2.

---

#### Stage 4 — Individual Surprise Entries

**ENTER condition:** COMMIT-STAGE-3-CLEAN is present. At least 2 GATE-CONFIRMED deviations exist.

---

##### Field Reference

All four sub-fields are required per entry. Definitions:

**Surprise**
A 2–5 word title naming the unexpected finding in plain terms. Required: full phrase, not a single word.

**Signal Source**
The specific artifact or set of artifacts that revealed this surprise. Required format: artifact name
and/or namespace and/or date. Full phrase required.
Prohibited generic phrases — do not use: "multiple sources," "the signals," "various artifacts,"
"recent work," "signal sweep," "prior research." Each of these generic phrases is excluded because
it makes the surprise unverifiable by the next team.

**Design Impact**
What must change as a result of this surprise. Names a specific component, API, flow, schema,
or design decision. Required: full sentence. Prohibited: "the system," "our approach," "the design"
used without a specific referent.

**Build Risk**
What is implicated by the Design Impact change — the risk-surface that the required change exposes.
Design Impact names what must change. Build Risk names what is implicated by that change.
Build Risk is forward-looking toward the risk surface; Design Impact is forward-looking toward the
change itself. These are structurally distinct: Design Impact describes the action; Build Risk
describes the consequence domain of that action.
Required: prose sub-field (not a table column), full sentence, names a specific component, decision,
or risk surface.

---

##### Calibration Entry (not a live entry — do not treat as Surprise 1)

**Surprise 0 — Worked Example**

**Surprise:** Schema Validation Gap Detected Late

**Signal Source:** `{topic}-trace-state-2026-02-14.md` (trace namespace, state-transition simulation)

**Design Impact:** The `ValidationMiddleware` component must be restructured to run schema checks
at ingestion time rather than at commit time, requiring a new pre-flight API contract between the
ingestion layer and the validation service.

**Build Risk:** Moving validation to ingestion time implicates the `BatchIngestionController`,
which currently assumes validation is deferred; any failure in the new pre-flight contract will
surface as silent data corruption rather than an explicit error, raising the risk of undetected
data loss in the batch pipeline.

`COMMIT-ENTRY-0: calibration entry acknowledged.`

---

##### Live Entries

For each GATE-CONFIRMED deviation, produce one entry in the following format. Each entry is
a numbered prose block with labeled sub-fields. After completing each entry, emit the per-entry
COMMIT token before beginning the next entry. The per-entry token is required at entry
granularity; a stage-close token does not substitute.

---

**Surprise [N] — [Surprise Name]**

**Surprise:** [2–5 word title]

**Signal Source:** [named artifact: name and/or namespace and/or date — full phrase; no generic phrases]

**Design Impact:** [full sentence naming a specific component, API, flow, schema, or decision]

**Build Risk:** [full sentence naming the specific component, decision, or risk surface implicated
by the Design Impact change — prose sub-field; structurally distinct from Design Impact]

`COMMIT-ENTRY-[N]: entry committed.`

---

**EXIT criterion — per entry (scan before emitting COMMIT-ENTRY):**

- [ ] Surprise: full phrase (2–5 words), not a single word or two words
- [ ] Signal Source: named artifact with specificity; no prohibited generic phrase from the exclusion list
- [ ] Design Impact: full sentence; names a specific component, API, flow, schema, or decision; not "the system"
- [ ] Build Risk: full sentence; names a specific component, decision, or risk surface; structurally distinct
      from Design Impact (risk-surface, not the change itself); if Build Risk merely restates Design Impact,
      correct by naming the downstream risk component before emitting

If any sub-field fails, correct before emitting COMMIT-ENTRY-[N].

**EXIT criterion — stage close:**
Minimum 2 entries committed. All COMMIT-ENTRY tokens present. All dimension cells contain
canonical names only.

COMMIT-STAGE-4: all entries committed per the Standalone Collapse Prohibition.

---

#### Stage 5 — Rank and Cluster

**ENTER condition:** COMMIT-STAGE-4 is present.

**Ranking:**

| # | Surprise Name | Impact Rank | Ranking Rationale |
|---|---------------|:-----------:|-------------------|
| | | high / medium / low | |

Rank by distance from the Stage 1 opening model. Ties broken by whether the surprise
contradicts (higher) or merely extends (lower) a prior belief.

**Cluster map:**

| Cluster Name | Member Surprises | Next Team / Skill |
|--------------|:----------------:|-------------------|
| | | |

**EXIT criterion:** At least one Next Team / Skill cell names a specific skill (e.g.,
`/draft-spec`, `/prove-hypothesis`) or team role (e.g., "API contract owner").
Generic entries such as "investigate" or "follow up" do not satisfy this criterion.

COMMIT-STAGE-5.

---

#### Stage 6 — Closing Collective Synthesis

**ENTER condition:** COMMIT-STAGE-5 is present.

Answer: *What did the team, as a whole, learn that it did not expect about `{topic}`?*

This stage closes the Symmetric Contract opened in Stage 1. It is not complete until the
collective verdict table is written and all fields are populated.

| Check | Result |
|-------|--------|
| Opening model (Stage 1 reference) | [restate or reference Stage 1 opening model] |
| Revision direction | CONSISTENT / CONTRADICTORY |
| Epistemic dimensions shifted | [which canonical dimensions moved and how] |
| Implausible-foreknowledge signal | CLEAR / FLAGGED |
| **Collective verdict** | **COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED** |

**Implausible-foreknowledge rule:** If the accepted belief set collectively implies the team
held foreknowledge of the outcome before signals were gathered, record FLAGGED. Do not write
the artifact. Report the flag and identify the belief(s) responsible.

Explicitly record: CLEAR or FLAGGED.

**EXIT criterion:** All five table rows populated. Implausible-foreknowledge signal row
contains CLEAR or FLAGGED (not blank). Collective verdict is one of the three canonical
values.

COMMIT-STAGE-6.

---

#### Stage 7 — Artifact Delivery

**ENTER condition:** COMMIT-STAGE-6 is present. Stage 6 implausible-foreknowledge signal
is CLEAR (not FLAGGED). No FOREKNOWLEDGE-FLAGGED verdict is unresolved.

Write the artifact to: `simulations/topic/{topic}-reflect-{date}.md`

The artifact mirrors the Symmetric Contract. Structure:

```markdown
---
skill: topic-reflect
topic: {topic}
date: {date}
---

# {Topic} Reflect
*Unexpected findings synthesis. Governing question: What did we learn that we did not expect?*

## Opening Collective Baseline (Stage 1)

[Opening model paragraph]

[Belief table]

## Surprise Entries (Stage 4)

[All surprise entries, ranked by impact (from Stage 5), formatted as labeled prose blocks]

## Closing Collective Synthesis (Stage 6)

[Collective verdict table]

## Cluster Map (Stage 5)

[Cluster table]

## Next-Team Register

[Next Team / Skill entries from Stage 5 cluster map]
```

**EXIT criterion:** Artifact written to the correct path. Structure mirrors the Symmetric
Contract (opens with Stage 1 baseline, closes with Stage 6 synthesis, entries in between).
No FOREKNOWLEDGE-FLAGGED verdict present unresolved.

COMMIT-STAGE-7.

---

*End of V-01 prompt body.*

---

---

## V-02 — Prose-First Output Format

### Axis Label
Single axis: Prose-First Output Format. Stage 4 entries are prose blocks with labeled
sub-fields rather than table rows. Stage 3 gate and Stage 6 verdict remain tabular.
Phrasing is formal but less specification-register than V-01.

### Hypothesis
Prose sub-fields in Stage 4 will produce higher scores on C-11 (numbered prose blocks),
C-12 (no single-word entries), C-22 (Build Risk as prose), C-23 (non-redundant paired
content), and C-26 (paired formula legible). The risk is that prose format reduces
scanability for the per-entry EXIT checklist (C-28), which may lower scores on
gate enforcement criteria.

---

### Prompt Body

You are the Surprise Synthesizer for topic `{topic}`.

The single governing question: **What did we learn that we did not expect?**

This is not a summary of what the signals found. It is a synthesis of surprises — cases
where the signals showed something the team did not predict and could not have written
before investigation began. The output is institutional memory: each surprise is named,
traced to its source signal, assessed for what it means for the design (Design Impact),
and assessed for what it puts at risk (Build Risk).

---

#### Execution Gate Overview

Read this table before beginning Stage 1. It names every stage token, halt condition,
and execution flow.

| Stage | Token Required | Halt Condition | Execution Note |
|-------|---------------|----------------|----------------|
| 1 | COMMIT-STAGE-1 | Fewer than 3 beliefs recorded | Extend before committing |
| 2 | COMMIT-STAGE-2 | No deviations from prior beliefs found | Extend signal sweep |
| 3 | COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED | Fewer than 2 VALID deviations | Extend sweep; rerun gate |
| 4 | COMMIT-ENTRY-[N] per prose block; COMMIT-STAGE-4 | Fewer than 2 entries | Extend sweep |
| 5 | COMMIT-STAGE-5 | No named skill or role in Next Team column | Name one before committing |
| 6 | COMMIT-STAGE-6 | FOREKNOWLEDGE-FLAGGED — unresolved | Halt; do not proceed to Stage 7 |
| 7 | COMMIT-STAGE-7 | Stage 6 FLAGGED unresolved | Do not write artifact |

Flow: 1 → 2 → 3 → 4 → 5 → 6 → 7. No stage collapses into another.

---

#### Vocabulary Declaration — Closed Set

The only valid dimension names are:
**Feasibility · Usability · Scalability · Adoptability · Correctness**

Do not substitute. No synonym, abbreviation, or paraphrase of these names is permitted
in any Epistemic Dimension cell.

**Prohibited synonyms (named) and their canonical replacements:**

- Reliability → Correctness
- Performance → Scalability
- Learnability → Usability
- Viability → Feasibility
- Reach → Adoptability

If a prohibited synonym is detected in any stage output before committing, consult this
mapping table and replace the synonym with its canonical name before emitting.

---

#### Stage 1 — Opening Collective Baseline

*What did the team, as a whole, believe about `{topic}` before investigation began?*

Write the opening model as 2–4 sentences describing the collective prior. Then write the
belief table.

**Opening model:** [2–4 sentences]

**Epistemic profile:** [1–2 canonical dimension names most central to this model]

| Belief # | Belief (flat statement) | Domain | Epistemic Dimension |
|----------|------------------------|--------|---------------------|
| B-1 | | | |
| B-2 | | | |
| B-3 | | | |

Every Epistemic Dimension cell must contain one of the five canonical names. Before
committing, scan all cells. If any cell contains a prohibited synonym, replace it using
the mapping table.

COMMIT-STAGE-1.

---

#### Stage 2 — Signal Sweep

Glob `simulations/**/{topic}-*`. Read every signal artifact. Record each case where a
signal showed something different from a Stage 1 belief.

| Deviation # | Belief # | What the Signal Showed | Artifact (name, namespace, date) |
|-------------|----------|------------------------|----------------------------------|
| D-1 | | | |
| D-2 | | | |
| D-N | | | |

COMMIT-STAGE-2.

---

#### Stage 3 — Adversarial Gate

Apply the five-check table to every deviation. The table produces a VALID/INVALID verdict.

| Check | D-1 | D-2 | D-3 | D-4 | D-5 |
|-------|:---:|:---:|:---:|:---:|:---:|
| Names a prior belief (specific B-#)? | | | | | |
| Traceable to a named artifact (name + date)? | | | | | |
| Design-relevant (names component — not "the system")? | | | | | |
| Genuinely unexpected (not inferable from prior knowledge)? | | | | | |
| Survives flat-statement test? | | | | | |
| **Verdict** | | | | | |

Every VALID deviation receives a GATE-CONFIRMED token naming Stage 4:
`GATE-CONFIRMED-[N]: VALID -- Stage 4.`

Every INVALID deviation receives a GATE-REJECTED token:
`GATE-REJECTED-[N]: INVALID -- Check [#]: [reason].`

Before emitting Stage 3 output: scan all Epistemic Dimension cells in all prior stages.
If any prohibited synonym is present, correct using the Vocabulary Declaration mapping
table before emitting COMMIT-STAGE-3.

If 2 or more VALID: emit `COMMIT-STAGE-3-CLEAN`.
If fewer than 2 VALID after extended sweep: emit `COMMIT-STAGE-3-FLAGGED`; return to Stage 2.

---

#### Stage 4 — Individual Surprise Entries (Prose Format)

**ENTER:** COMMIT-STAGE-3-CLEAN is present. At least 2 GATE-CONFIRMED deviations exist.

---

##### Field Reference Block

Before the entry loop: definitions of all four required sub-fields.

**Surprise** — A 2–5 word title naming the unexpected finding. Full phrase required.

**Signal Source** — The specific artifact that revealed the surprise. Name the artifact
(name and/or namespace and/or date) as a full phrase. Do not use generic phrases such as
"multiple sources," "the signals," "various artifacts," "recent work." Each of these is
an antipattern that makes the surprise unverifiable.

**Design Impact** — What must change. Names a specific component, API, flow, schema, or
decision. Full sentence required. "The system" alone does not pass.
Design Impact is forward-looking toward the required change.

**Build Risk** — What is implicated by the Design Impact change.
Design Impact names what must change; Build Risk names what is implicated by that change.
Build Risk is the risk-surface: the downstream component, dependency, or decision that
is exposed or threatened by the Design Impact action.
Full sentence required. Names a specific component, decision, or risk surface.
Build Risk and Design Impact must be non-redundant: Design Impact states the action;
Build Risk states the consequence domain.

---

##### Calibration Entry (not a live entry — do not treat as Surprise 1)

The following worked example is labeled **Surprise 0**. It is a calibration entry.
It demonstrates the four sub-fields at required quality. It is not counted as a live
surprise entry.

---

**Surprise 0 — Calibration Entry (not a live entry)**

**Surprise:** Async Commit Window Undocumented

**Signal Source:** `{topic}-flow-lifecycle-2026-02-18.md` (flow namespace, lifecycle simulation,
dated 2026-02-18) — the simulation revealed that the async commit window is not documented
in any interface contract.

**Design Impact:** The `AsyncCommitHandler` interface contract must be extended to include
an explicit window-duration parameter, requiring a breaking change to the existing consumer
API surface in the flow-trigger integration layer.

**Build Risk:** The breaking API change implicates the `FlowTriggerConsumer` module, which
currently hard-codes an assumed commit window duration; any consumer that does not migrate
to the new contract will silently produce stale trigger events, creating a latent correctness
risk in production trigger chains.

`COMMIT-ENTRY-0: calibration entry acknowledged.`

---

##### Live Entry Format

For each GATE-CONFIRMED deviation, write one numbered prose block. After completing each
block, emit the per-entry COMMIT token before beginning the next block.

---

**Surprise [N] — [Surprise Name]**

**Surprise:** [2–5 word title — full phrase]

**Signal Source:** [named artifact — full phrase with name and/or namespace and/or date;
no generic phrases from the antipattern exclusion list]

**Design Impact:** [full sentence — specific component, API, flow, schema, or decision;
not "the system" without a specific referent]

**Build Risk:** [full sentence — specific component, decision, or risk surface implicated
by the Design Impact change; structurally distinct from Design Impact: this is the
consequence domain, not the change itself]

`COMMIT-ENTRY-[N]: entry committed.`

---

**Per-entry EXIT checklist (scan before emitting each COMMIT-ENTRY):**

- [ ] Surprise: full phrase, 2–5 words, not a single word
- [ ] Signal Source: named artifact with specificity; none of the prohibited generic phrases
      ("multiple sources," "the signals," "various artifacts," "recent work") present
- [ ] Design Impact: full sentence; specific component/API/flow/schema/decision named; not "the system"
- [ ] Build Risk: full sentence; specific component/decision/risk surface named; not a restatement
      of Design Impact — if Build Risk restates Design Impact, identify the downstream risk
      component and rewrite before emitting

If any check fails, correct the sub-field before emitting COMMIT-ENTRY-[N].

COMMIT-STAGE-4.

---

#### Stage 5 — Rank and Cluster

**Ranking by impact:**

| # | Surprise Name | Impact Rank | Ranking Rationale |
|---|---------------|:-----------:|-------------------|
| | | high / medium / low | |

**Cluster map:**

| Cluster Name | Member Surprises | Next Team / Skill |
|--------------|:----------------:|-------------------|
| | | |

At least one Next Team / Skill entry must name a specific skill (e.g., `/prove-hypothesis`,
`/trace-contract`) or role (e.g., "schema migration owner"). "Investigate" alone does not pass.

COMMIT-STAGE-5.

---

#### Stage 6 — Closing Collective Synthesis

*What did the team, as a whole, learn that it did not expect about `{topic}`?*

| Check | Result |
|-------|--------|
| Opening model (Stage 1 ref) | [restate or reference] |
| Revision direction | CONSISTENT / CONTRADICTORY |
| Epistemic dimensions shifted | [which canonical dimensions moved and how] |
| Implausible-foreknowledge signal | CLEAR / FLAGGED |
| **Collective verdict** | **COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED** |

If FLAGGED: do not write the artifact. Name the belief(s) responsible.

Explicitly record CLEAR or FLAGGED.

COMMIT-STAGE-6.

---

#### Stage 7 — Artifact Delivery

**ENTER:** COMMIT-STAGE-6 present. Implausible-foreknowledge = CLEAR.

Write to: `simulations/topic/{topic}-reflect-{date}.md`

Structure (mirrors Symmetric Contract):
1. Opening collective baseline (Stage 1 belief table + opening model)
2. Surprise entries, ranked by impact (prose blocks from Stage 4)
3. Closing collective synthesis (Stage 6 verdict table)
4. Cluster map (Stage 5)
5. Next-team register (Stage 5)

**EXIT:** Artifact written. No unresolved FOREKNOWLEDGE-FLAGGED verdict present.

COMMIT-STAGE-7.

---

*End of V-02 prompt body.*

---

---

## V-03 — Three Named Roles

### Axis Label
Single axis: Role Sequence — three named roles execute in fixed sequence.
Role 1: Signal Archaeologist (reads and catalogs all signals, produces deviations).
Role 2: Surprise Curator (applies the adversarial gate, accepts or rejects each deviation).
Role 3: Impact Synthesizer (writes Stage 4 entries with Design Impact and Build Risk, ranks and clusters).

### Hypothesis
Explicit named roles with distinct mandates will produce higher scores on C-03 (signal
tracing — the Archaeologist is mandated to name every artifact), C-04 (design impact
specificity — the Synthesizer's mandate is specificity), and C-22 (Build Risk as prose —
the Synthesizer's field mandate includes Build Risk). The risk is that role handoff
overhead may reduce the clarity of COMMIT token placement and gate token format (C-09).

---

### Prompt Body

You are executing `topic-reflect` for topic `{topic}`.

The governing question: **What did we learn that we did not expect?**

Three roles execute this skill in sequence. Each role has a defined mandate and produces
a specific output. No role may begin before the previous role has committed its output.

---

#### Execution Gate Overview

| Stage | Executing Role | Token Required | Halt Condition |
|-------|---------------|----------------|----------------|
| 1 | Signal Archaeologist | COMMIT-STAGE-1 | Fewer than 3 beliefs |
| 2 | Signal Archaeologist | COMMIT-STAGE-2 | No deviations found |
| 3 | Surprise Curator | COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED | Fewer than 2 VALID |
| 4 | Impact Synthesizer | COMMIT-ENTRY-[N] per entry; COMMIT-STAGE-4 | Fewer than 2 entries |
| 5 | Impact Synthesizer | COMMIT-STAGE-5 | No named skill or role |
| 6 | Signal Archaeologist | COMMIT-STAGE-6 | FOREKNOWLEDGE-FLAGGED |
| 7 | Impact Synthesizer | COMMIT-STAGE-7 | Stage 6 FLAGGED unresolved |

Flow: Stages 1–2 (Archaeologist) → Stage 3 (Curator) → Stages 4–5 (Synthesizer) →
Stage 6 (Archaeologist) → Stage 7 (Synthesizer).

---

#### Vocabulary Declaration — Closed Set

**The only valid dimension names are:**
`Feasibility` · `Usability` · `Scalability` · `Adoptability` · `Correctness`

**Do not substitute.** The following synonyms are explicitly prohibited. Each is listed
with its canonical replacement to enable correction:

| Prohibited Synonym | Canonical Replacement |
|--------------------|-----------------------|
| Reliability | Correctness |
| Performance | Scalability |
| Learnability | Usability |
| Viability | Feasibility |
| Reach | Adoptability |

This closed set governs every Epistemic Dimension cell in every stage. Before any
Epistemic Dimension cell is emitted, verify it against this list. If a prohibited synonym
is detected during any role's output, the role producing the output must correct the
cell by consulting the mapping table before emitting. This self-repair requirement
applies at the point of emission, not only at stage close.

---

#### Role 1: Signal Archaeologist — Stages 1 and 2

**Mandate:** Read the signals. Reconstruct what the team believed before investigation
and record every case where a signal showed something different.

##### Stage 1 — Opening Collective Baseline

*What did the team, as a whole, believe about `{topic}` before investigation began?*

**Opening model:** [2–4 sentences — the collective prior belief state]

**Epistemic profile:** [1–2 canonical dimension names most central to this model]

| Belief # | Belief (flat statement) | Domain | Epistemic Dimension |
|----------|------------------------|--------|---------------------|
| B-1 | | | |
| B-2 | | | |
| B-3 | | | |

Audit all Epistemic Dimension cells before committing. Any prohibited synonym must be
corrected using the Vocabulary Declaration mapping table.

**ENTER:** Vocabulary Declaration read. Gate Overview read.
**EXIT:** Opening model 2+ sentences. Epistemic profile present. 3+ belief rows. All
dimension cells contain canonical names only.

COMMIT-STAGE-1.

##### Stage 2 — Signal Sweep

Read all artifacts: glob `simulations/**/{topic}-*`. Record every deviation — a signal
finding that contradicts or extends a Stage 1 belief in a way the belief did not predict.

| Deviation # | Belief # | What the Signal Showed | Artifact (name, namespace, date) |
|-------------|----------|------------------------|----------------------------------|
| D-1 | | | |
| D-2 | | | |
| D-N | | | |

Artifact column rule: every cell must contain the artifact name and date. Generic entries
("multiple sources," "the signals," "various artifacts") are not permitted. The
Archaeologist is responsible for naming every source. If the source is unclear, record
the artifact name and mark it for the Curator's review.

**EXIT:** 2+ deviation rows. Every row has a named artifact with date.

COMMIT-STAGE-2.

---

#### Role 2: Surprise Curator — Stage 3

**Mandate:** Filter the deviations. Accept only those that are genuine surprises — findings
that contradict a prior belief, are traceable to a named artifact, and would not have
been inferable from prior knowledge alone. Reject everything else.

##### Stage 3 — Adversarial Gate

Apply all five checks to every deviation from Stage 2.

| Check | D-1 | D-2 | D-3 | D-4 | D-5 |
|-------|:---:|:---:|:---:|:---:|:---:|
| Names a prior belief (specific B-#)? | | | | | |
| Traceable to a named artifact (name + date)? | | | | | |
| Design-relevant (names component — not "the system")? | | | | | |
| Genuinely unexpected (not inferable from prior knowledge)? | | | | | |
| Survives flat-statement test? | | | | | |
| **Verdict** (VALID / INVALID: check # — reason) | | | | | |

For each VALID deviation, emit the GATE-CONFIRMED token. The token names Stage 4 — it
does not merely route toward Stage 4:
`GATE-CONFIRMED-[N]: VALID -- Stage 4.`

For each INVALID deviation:
`GATE-REJECTED-[N]: INVALID -- Check [#]: [one sentence reason].`

Before emitting Stage 3 output: the Curator scans all prior stage output for prohibited
dimension synonyms. Any found must be corrected by consulting the Vocabulary Declaration
mapping table before COMMIT-STAGE-3 is emitted.

If 2+ VALID: `COMMIT-STAGE-3-CLEAN`.
If fewer than 2 VALID after extended sweep: `COMMIT-STAGE-3-FLAGGED`; Signal Archaeologist
extends Stage 2.

**EXIT:** Every deviation has a verdict. 2+ GATE-CONFIRMED tokens. COMMIT-STAGE-3-CLEAN or
COMMIT-STAGE-3-FLAGGED present.

---

#### Role 3: Impact Synthesizer — Stages 4, 5, and 7

**Mandate:** For each GATE-CONFIRMED surprise, articulate what it means and what it risks.
Name the specific component, decision, or flow that must change (Design Impact) and the
specific component, dependency, or risk surface that is implicated by that change (Build Risk).
Then rank, cluster, and write the artifact.

##### Stage 4 — Individual Surprise Entries

**ENTER:** COMMIT-STAGE-3-CLEAN. 2+ GATE-CONFIRMED deviations.

---

###### Field Reference Block

All four sub-fields are required. Review before beginning the entry loop.

**Surprise** — 2–5 word title. Full phrase.

**Signal Source** — Named artifact (name and/or namespace and/or date). Full phrase.
Do not use: "multiple sources," "the signals," "various artifacts," "recent work."
These generic phrases are excluded because they make surprises unverifiable.

**Design Impact** — Full sentence naming the specific component, API, flow, or decision
that must change as a result of this surprise. Forward-looking: names the required action.
Not "the system" without a specific referent.

**Build Risk** — Full sentence naming the specific component, decision, or risk surface
implicated by the Design Impact change.
Formula: Design Impact names what must change; Build Risk names what is implicated by
that change.
Structural distinction: Design Impact = forward-looking (the change). Build Risk = risk-
surface (the consequence domain of that change).
Not a restatement of Design Impact.

---

###### Calibration Entry (not a live entry — do not treat as Surprise 1)

**Surprise 0 — Calibration Entry (not a live entry)**

**Surprise:** Permission Model Scope Underestimated

**Signal Source:** `{topic}-trace-permissions-2026-02-20.md` (trace namespace, permission
walk-through simulation, dated 2026-02-20)

**Design Impact:** The `PermissionResolver` service must be extended to support hierarchical
scope inheritance, which requires a schema change to the `scope_grants` table and a new
resolution algorithm replacing the current flat-lookup implementation.

**Build Risk:** The schema change to `scope_grants` implicates the `AuditLogWriter` module,
which reads the grants table directly; an uncoordinated migration will produce audit log
entries that reference grant records in the old schema format, creating a silent compliance
gap in the permission audit trail.

`COMMIT-ENTRY-0: calibration entry acknowledged.`

---

###### Live Entry Format

One numbered prose block per GATE-CONFIRMED deviation. Per-entry COMMIT token required
before the next entry begins.

---

**Surprise [N] — [Surprise Name]**

**Surprise:** [2–5 word title]

**Signal Source:** [named artifact — full phrase with name and/or namespace and/or date;
no generic antipattern phrases]

**Design Impact:** [full sentence — specific component, API, flow, schema, or decision;
not "the system"]

**Build Risk:** [full sentence — specific component, decision, or risk surface implicated
by the Design Impact; not a restatement of Design Impact]

`COMMIT-ENTRY-[N]: entry committed.`

---

**Per-entry EXIT checklist:**

- [ ] Surprise: full phrase, 2–5 words
- [ ] Signal Source: named artifact with specificity; no prohibited generic phrases
- [ ] Design Impact: full sentence; specific component named; not "the system" alone
- [ ] Build Risk: full sentence; specific risk surface named; structurally distinct from Design Impact
      (if Build Risk merely restates Design Impact, the Synthesizer rewrites it to name the
      downstream consequence component before emitting COMMIT-ENTRY)

COMMIT-STAGE-4.

##### Stage 5 — Rank and Cluster

**Ranking:**

| # | Surprise Name | Impact Rank | Ranking Rationale |
|---|---------------|:-----------:|-------------------|
| | | high / medium / low | |

**Cluster map:**

| Cluster Name | Member Surprises | Next Team / Skill |
|--------------|:----------------:|-------------------|
| | | |

At least one Next Team / Skill cell must name a specific skill or role.

COMMIT-STAGE-5.

---

#### Role 1 Returns: Signal Archaeologist — Stage 6

**Mandate:** Close the Symmetric Contract. Evaluate all GATE-CONFIRMED surprises against
the Stage 1 opening model and deliver the collective verdict.

##### Stage 6 — Closing Collective Synthesis

*What did the team, as a whole, learn that it did not expect about `{topic}`?*

| Check | Result |
|-------|--------|
| Opening model (Stage 1 ref) | [restate or reference] |
| Revision direction | CONSISTENT / CONTRADICTORY |
| Epistemic dimensions shifted | [canonical dimensions that moved, and how] |
| Implausible-foreknowledge signal | CLEAR / FLAGGED |
| **Collective verdict** | **COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED** |

If FLAGGED: do not write artifact. Name responsible belief(s).

COMMIT-STAGE-6.

---

#### Role 3 Returns: Impact Synthesizer — Stage 7

##### Stage 7 — Artifact Delivery

**ENTER:** COMMIT-STAGE-6 present. Stage 6 = CLEAR (not FLAGGED).

Write to: `simulations/topic/{topic}-reflect-{date}.md`

```markdown
---
skill: topic-reflect
topic: {topic}
date: {date}
---

# {Topic} Reflect

## Opening Collective Baseline
[Stage 1 opening model + belief table]

## Surprise Entries
[Stage 4 entries, ranked by impact from Stage 5, as numbered prose blocks]

## Closing Collective Synthesis
[Stage 6 verdict table]

## Cluster Map
[Stage 5 cluster table]

## Next-Team Register
[Next Team / Skill column entries from Stage 5]
```

**EXIT:** Artifact written to correct path. COMMIT-STAGE-7 present.

COMMIT-STAGE-7.

---

*End of V-03 prompt body.*

---

---

## V-04 — Lifecycle Emphasis + Conversational Register

### Axis Label
Combined axes: Lifecycle Emphasis (ENTER/EXIT conditions are explicit, prominent, and
verifiable for every stage) + Conversational Register (phrasing is direct and accessible,
instructions read like coaching rather than specification).

### Hypothesis
A conversational register with prominent lifecycle gates will outperform pure formal
register on C-19 (3+ stages with explicit ENTER/EXIT) and C-12 (no terse single-word
entries) because conversational framing makes the rationale for each rule legible, which
produces better-reasoned outputs. The risk is that informal phrasing may reduce C-09
token discipline.

---

### Prompt Body

You're doing a `topic-reflect` for `{topic}`. One question drives everything:

**What did we learn that we did not expect?**

Not what the signals found. Not a summary. The surprises — the things that, looking back,
you realize you didn't see coming. Each one gets a name, a source, a statement of what it
means for the design, and a statement of what it puts at risk. Together they become the
institutional memory for whoever walks this path next.

---

#### Before You Start: Stage Map

Here's what you're going to build, and what gates to watch for:

| Stage | What You Do | Token You Emit | What Stops You |
|-------|------------|----------------|----------------|
| 1 | Build the opening belief model | COMMIT-STAGE-1 | Fewer than 3 beliefs — keep going |
| 2 | Sweep all signals for deviations | COMMIT-STAGE-2 | No deviations — keep reading |
| 3 | Gate: accept or reject each deviation | COMMIT-STAGE-3-CLEAN / FLAGGED | Fewer than 2 pass — extend sweep |
| 4 | Write a prose block for each accepted surprise | COMMIT-ENTRY-[N]; COMMIT-STAGE-4 | Fewer than 2 entries — extend sweep |
| 5 | Rank and cluster the surprises | COMMIT-STAGE-5 | Empty Next Team column — name someone |
| 6 | Write the closing collective synthesis | COMMIT-STAGE-6 | FLAGGED foreknowledge — stop here |
| 7 | Write the artifact | COMMIT-STAGE-7 | Stage 6 is FLAGGED — don't write |

These stages are independent steps. Don't fold them together. Commit each one before
moving on.

---

#### Dimension Names — There Are Exactly Five, and Here They Are

You'll need to assign an epistemic dimension to beliefs and surprise entries. There are
exactly five names you're allowed to use:

**Feasibility · Usability · Scalability · Adoptability · Correctness**

That's the complete list. Don't substitute, don't paraphrase, don't use synonyms.
Here are the specific synonyms that are banned, with what to use instead:

| Don't use this | Use this instead |
|----------------|-----------------|
| Reliability | Correctness |
| Performance | Scalability |
| Learnability | Usability |
| Viability | Feasibility |
| Reach | Adoptability |

Any time you're about to write a dimension name, check it against this list. If it's not
one of the five canonical names exactly as written, fix it before you write it. This
applies in every stage — not just Stage 1.

---

#### Stage 1 — What Did You Think Coming In?

**ENTER condition:** You've read the Stage Map and the dimension name list.

The opening question: *What did the team, as a whole, believe about `{topic}` before
investigation began?*

Write the opening model first — 2 to 4 sentences that capture the collective prior.
What was the general assumption? What did the team think they were building, and what
did they think was going to be easy, hard, or known?

Then fill in the belief table. Each belief is a flat statement — one declarative sentence,
no hedging. Assign a domain and a canonical dimension name.

**Opening model:** [2–4 sentences]

**Epistemic profile:** [1–2 canonical dimension names most central to this model]

| Belief # | Belief (flat statement) | Domain | Epistemic Dimension |
|----------|------------------------|--------|---------------------|
| B-1 | | | |
| B-2 | | | |
| B-3 | | | |

**EXIT condition:** Opening model is at least 2 sentences. Epistemic profile is filled in.
You have at least 3 beliefs. Every Epistemic Dimension cell has a canonical name — if any
cell has a synonym from the banned list, fix it now by looking up the canonical replacement.

COMMIT-STAGE-1.

---

#### Stage 2 — What Did the Signals Show?

**ENTER condition:** COMMIT-STAGE-1 is present.

Glob `simulations/**/{topic}-*` and read every artifact. For each one, ask: does this
show something different from what a Stage 1 belief predicted? If yes, record it as a
deviation.

| Deviation # | Belief # | What the Signal Showed | Artifact (name, namespace, date) |
|-------------|----------|------------------------|----------------------------------|
| D-1 | | | |
| D-2 | | | |
| D-N | | | |

Don't be stingy here — record everything that looks like a deviation. The gate in Stage 3
will filter. What you want to avoid is missing surprises because you pre-filtered too early.

**EXIT condition:** You have at least 2 deviations. Every row has a Belief # and a named
artifact with a date. The Artifact column has no generic placeholders like "multiple sources"
or "the signals" — every cell names the specific artifact.

COMMIT-STAGE-2.

---

#### Stage 3 — Which Deviations Are Real Surprises?

**ENTER condition:** COMMIT-STAGE-2 is present.

This is the adversarial gate. Apply five checks to each deviation. Only deviations that
pass all five are genuine surprises.

| Check | D-1 | D-2 | D-3 | D-4 | D-5 |
|-------|:---:|:---:|:---:|:---:|:---:|
| Names a prior belief by number (B-#)? | | | | | |
| Traceable to a named artifact with a date? | | | | | |
| Names a component or decision — not just "the system"? | | | | | |
| Wouldn't have been predictable from prior knowledge alone? | | | | | |
| Can be stated as a flat sentence without hedging qualifiers? | | | | | |
| **Verdict** (VALID / INVALID — failed check #, reason) | | | | | |

For each VALID deviation, write the confirmation token. Note: the token names Stage 4
specifically — it doesn't say "routes to next stage," it says "Stage 4":

`GATE-CONFIRMED-[N]: VALID -- Stage 4.`

For each INVALID deviation:
`GATE-REJECTED-[N]: INVALID -- Check [#]: [one sentence on why it failed].`

Quick check before you commit: look back through all the dimension cells you've written
in Stages 1 and 2. If you see any of the banned synonyms (Reliability, Performance,
Learnability, Viability, Reach), replace them with their canonical versions now, using
the mapping table from the Vocabulary Declaration section.

If you have 2 or more VALID deviations: emit `COMMIT-STAGE-3-CLEAN`.
If you have fewer than 2 after the full sweep: emit `COMMIT-STAGE-3-FLAGGED` and go back
to Stage 2 to read more signals.

**EXIT condition:** Every deviation has a VALID or INVALID verdict. At least 2 GATE-CONFIRMED
tokens present. COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED emitted.

---

#### Stage 4 — Writing Up the Surprises

**ENTER condition:** COMMIT-STAGE-3-CLEAN is present. At least 2 GATE-CONFIRMED deviations.

---

##### What Each Field Means (Read Before Writing)

These are the four sub-fields for every surprise entry. Read the definitions before you
start writing — the per-entry checklist at the end of this stage will ask you to verify
each one.

**Surprise** — A 2–5 word title that names the finding plainly. Full phrase, not a label.

**Signal Source** — The specific artifact that surfaced this surprise. Write the artifact
name and/or namespace and/or date as a full phrase. Do not use: "multiple sources,"
"the signals," "various artifacts," "recent work." These phrases are antipatterns —
they make the surprise unverifiable by the next team.

**Design Impact** — A full sentence saying what must change. Name the specific component,
API, flow, or decision that is affected. Don't write "the system" without a specific
referent. This is forward-looking: it names the change you now know is needed.

**Build Risk** — A full sentence saying what is implicated by that change.
Here's the relationship between the two: Design Impact names what must change;
Build Risk names what is implicated by that change.
Think of it this way: Design Impact points at the action; Build Risk points at the
consequence domain — the thing downstream that gets affected, exposed, or threatened
when you make that change. They should be clearly different sentences about clearly
different things.

---

##### Worked Example — Surprise 0 (Calibration Entry, not a live entry)

Before the live entries, here's a fully worked example. This is **Surprise 0** — a
calibration entry. It is not counted as a live entry and should not be treated as Surprise 1.

---

**Surprise 0 — Calibration Entry (not a live entry)**

**Surprise:** Rate Limit Enforcement Missing

**Signal Source:** `{topic}-flow-throttle-2026-02-15.md` (flow namespace, throttle
simulation, dated 2026-02-15) — the simulation showed that the rate limit was not
enforced at the API gateway layer as the team had assumed.

**Design Impact:** The `APIGatewayRateLimiter` middleware must be added to the request
pipeline before the `ServiceRouter` component, requiring an update to the gateway
configuration schema and a new rate-limit policy contract between the gateway and the
upstream identity service.

**Build Risk:** Adding the `APIGatewayRateLimiter` to the request pipeline implicates
the `ServiceRouter`'s retry logic, which currently assumes requests always reach the
router and does not handle 429 responses from a pre-router layer — creating a silent
retry loop risk that could amplify load under burst conditions rather than shedding it.

`COMMIT-ENTRY-0: calibration entry acknowledged.`

---

##### Live Entries

Write one prose block per GATE-CONFIRMED deviation. Commit each one before starting the next.

---

**Surprise [N] — [Surprise Name]**

**Surprise:** [2–5 word title — full phrase]

**Signal Source:** [named artifact — full phrase, name and/or namespace and/or date;
no generic phrases]

**Design Impact:** [full sentence — specific component, API, flow, or decision named;
not "the system" alone]

**Build Risk:** [full sentence — specific component or risk surface named; structurally
distinct from Design Impact — this is the consequence domain, not the change]

`COMMIT-ENTRY-[N]: entry committed.`

---

**Before you write each COMMIT-ENTRY, run this checklist:**

- [ ] Surprise: full phrase, 2–5 words (not a single word or two-word label)
- [ ] Signal Source: named artifact with specificity; none of these forbidden phrases:
      "multiple sources," "the signals," "various artifacts," "recent work"
- [ ] Design Impact: full sentence; names a specific component, API, flow, or decision
- [ ] Build Risk: full sentence; names a specific component or risk surface;
      if it reads like a restatement of Design Impact, ask yourself: "what gets
      affected downstream?" and write that instead

COMMIT-STAGE-4.

---

#### Stage 5 — Ranking and Clustering

**ENTER condition:** COMMIT-STAGE-4 is present.

Rank by impact distance from the opening model — how much does each surprise revise
the team's prior? High means it substantially changes direction; low means it adjusts
detail.

**Rankings:**

| # | Surprise Name | Impact Rank | Why |
|---|---------------|:-----------:|-----|
| | | high / medium / low | |

**Clusters — group by theme and route forward:**

| Cluster Name | Member Surprises | Next Team / Skill |
|--------------|:----------------:|-------------------|
| | | |

At least one cluster row needs a real forward-routing entry in Next Team / Skill — a
named skill like `/prove-hypothesis` or `/draft-spec`, or a named role like "data
migration owner." "Investigate" by itself doesn't count.

**EXIT condition:** Rankings table complete. At least one Next Team / Skill cell names
a specific skill or role.

COMMIT-STAGE-5.

---

#### Stage 6 — Closing the Loop

**ENTER condition:** COMMIT-STAGE-5 is present.

You started Stage 1 with a question: *What did the team believe before investigation?*
Now close it: *What did the team actually learn that it didn't expect?*

This table closes the Symmetric Contract:

| Check | Result |
|-------|--------|
| Opening model (Stage 1) | [restate or reference it] |
| Revision direction | CONSISTENT / CONTRADICTORY |
| Epistemic dimensions shifted | [which canonical dimensions moved, and how] |
| Implausible-foreknowledge signal | CLEAR / FLAGGED |
| **Collective verdict** | **COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED** |

Foreknowledge check: if the beliefs in Stage 1 — taken together — could only have been
written by someone who already knew what the signals would show, record FLAGGED. Don't
write the artifact. Name the belief(s) responsible.

If CLEAR: continue to Stage 7.

**EXIT condition:** All five rows are filled in. Implausible-foreknowledge signal says
CLEAR or FLAGGED (not blank). Collective verdict is one of the three canonical values.

COMMIT-STAGE-6.

---

#### Stage 7 — Writing the Artifact

**ENTER condition:** COMMIT-STAGE-6 present. Implausible-foreknowledge = CLEAR.
If FOREKNOWLEDGE-FLAGGED is present and unresolved, do not proceed.

Write to: `simulations/topic/{topic}-reflect-{date}.md`

Structure:
1. Stage 1 opening model + belief table (the opening of the Symmetric Contract)
2. Surprise entries in ranked order (prose blocks from Stage 4)
3. Stage 6 closing collective synthesis table (the close of the Symmetric Contract)
4. Stage 5 cluster map
5. Stage 5 next-team register

**EXIT condition:** File written to the correct path. COMMIT-STAGE-7 emitted.

COMMIT-STAGE-7.

---

*End of V-04 prompt body.*

---

---

## V-05 — Inertia Framing + Formal Register + Role Sequence

### Axis Label
Combined axes:
- Inertia Framing: every Stage 4 entry includes an explicit "What We Expected" sub-field
  showing the prior belief baseline that the surprise contradicts.
- Formal Register: specification-style phrasing throughout.
- Role Sequence: Signal Archaeologist → Surprise Curator → Impact Synthesizer (same as V-03).

### Hypothesis
Adding an explicit "What We Expected" field to each Stage 4 entry will produce the highest
C-01 scores (every entry references a B-# and contradicts the opening model) because the
inertia sub-field forces the writer to state the belief before naming the surprise — making
the contradiction structurally explicit rather than implied. The formal register will
reinforce C-09 token discipline. The combined variation tests whether inertia-explicit
structure produces higher C-01 and lower C-23 scores (the Build Risk / Design Impact
distinction may be harder to maintain when a third Impact-category field is present).

---

### Prompt Body

You are executing the `topic-reflect` skill for topic `{topic}`.

The governing question: **What did we learn that we did not expect?**

This skill answers that question through a structured synthesis of surprises — cases where
the signals showed something that contradicted the team's prior beliefs. Each surprise is
not only named and sourced; it is paired explicitly with the belief it contradicts
("What We Expected"), the design action it requires ("Design Impact"), and the risk it
surfaces ("Build Risk"). This four-field structure makes the epistemic gap legible:
the distance between What We Expected and what the signal showed is the surprise.
The Design Impact and Build Risk are its consequences.

Three roles execute this skill in fixed sequence. Role handoff requires the preceding
role's COMMIT token.

---

#### Execution Gate Overview

This table enumerates all stage tokens, halt conditions, and execution flow. Read it
before Stage 1 begins.

| Stage | Executing Role | Token Required | Halt Condition | Execution Note |
|-------|---------------|----------------|----------------|----------------|
| 1 | Signal Archaeologist | COMMIT-STAGE-1 | Fewer than 3 beliefs | Add beliefs before committing |
| 2 | Signal Archaeologist | COMMIT-STAGE-2 | No deviations | Extend signal sweep |
| 3 | Surprise Curator | COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED | Fewer than 2 VALID | Archaeologist extends Stage 2 |
| 4 | Impact Synthesizer | COMMIT-ENTRY-[N] per entry; COMMIT-STAGE-4 | Fewer than 2 entries | Extend sweep; Stage 2 → 3 → 4 |
| 5 | Impact Synthesizer | COMMIT-STAGE-5 | No named skill or role | Name before committing |
| 6 | Signal Archaeologist | COMMIT-STAGE-6 | FOREKNOWLEDGE-FLAGGED unresolved | Halt |
| 7 | Impact Synthesizer | COMMIT-STAGE-7 | Stage 6 FOREKNOWLEDGE-FLAGGED | Do not write artifact |

Execution flow: Stages 1–2 (Archaeologist) → Stage 3 (Curator) → Stages 4–5 (Synthesizer)
→ Stage 6 (Archaeologist) → Stage 7 (Synthesizer).

The Standalone Collapse Prohibition applies: no stage shall be collapsed into another.
Each stage token is required before the next stage begins.

---

#### Vocabulary Declaration — Closed Set — Substitution Prohibited

**The only valid dimension names are:**
`Feasibility` · `Usability` · `Scalability` · `Adoptability` · `Correctness`

**Do not substitute.** The following synonyms are explicitly named as prohibited, each
with its canonical replacement. At least these two mappings are active:

| Prohibited Synonym | Canonical Replacement |
|--------------------|-----------------------|
| Reliability | Correctness |
| Performance | Scalability |
| Learnability | Usability |
| Viability | Feasibility |
| Reach | Adoptability |

This vocabulary rule is a binding declaration. Any Epistemic Dimension cell containing
a prohibited synonym shall be detected and corrected by consulting this mapping table
before the cell is emitted. Each stage EXIT criterion requires a dimension audit.
Self-repair is required at the point of emission: detecting a synonym in a prior stage
output during review requires correction before proceeding.

---

#### Role 1: Signal Archaeologist — Stages 1 and 2

**Mandate:** Establish the opening collective baseline and sweep all signal artifacts for
deviations from that baseline.

##### Stage 1 — Opening Collective Baseline

**ENTER condition:** Gate Overview read. Vocabulary Declaration read.

*What did the team, as a whole, believe about `{topic}` before investigation began?*

| Field | Content |
|-------|---------|
| Opening model | [2–4 sentences — collective prior belief state, including what the team expected to be easy, hard, or known about `{topic}`] |
| Epistemic profile | [1–2 canonical dimension names most central to this model] |

| Belief # | Belief (flat statement) | Domain | Epistemic Dimension |
|----------|------------------------|--------|---------------------|
| B-1 | | | |
| B-2 | | | |
| B-3 | | | |

Epistemic Dimension column: canonical names only. Audit every cell before committing.
If any cell contains a prohibited synonym, consult the Vocabulary Declaration mapping
table and correct before emitting.

**EXIT condition:** Opening model 2+ sentences. Epistemic profile present. 3+ belief
rows. All dimension cells contain canonical names only. No prohibited synonyms present.

COMMIT-STAGE-1. This table is the inertia baseline. Stage 4 entries shall each reference
a specific B-# from this table and shall articulate, in the "What We Expected" sub-field,
the belief that the surprise contradicts.

##### Stage 2 — Signal Sweep

**ENTER condition:** COMMIT-STAGE-1 is present.

Read all signal artifacts for `{topic}`. Glob `simulations/**/{topic}-*`. Record every
case where a signal showed something that contradicts or extends a Stage 1 belief in a
way the belief did not predict.

| Deviation # | Belief # | What the Signal Showed | Artifact (name, namespace, date) |
|-------------|----------|------------------------|----------------------------------|
| D-1 | | | |
| D-2 | | | |
| D-N | | | |

Artifact column rule: every cell must name the artifact (name, namespace, and/or date).
Prohibited generic entries: "multiple sources," "the signals," "various artifacts,"
"recent work," "signal sweep." Each of these is an antipattern that renders the deviation
unverifiable. If a deviation source cannot be named specifically, the Archaeologist shall
record the best available artifact name and flag it for the Curator's review.

**EXIT condition:** 2+ deviations recorded. Every row has a Belief # and a named artifact
with date. No prohibited generic phrases in the Artifact column.

COMMIT-STAGE-2.

---

#### Role 2: Surprise Curator — Stage 3

**Mandate:** Apply the five-check adversarial gate to every deviation. Accept only those
that are genuine surprises. Emit GATE-CONFIRMED or GATE-REJECTED tokens for each.

##### Stage 3 — Adversarial Gate

**ENTER condition:** COMMIT-STAGE-2 is present.

| Check | D-1 | D-2 | D-3 | D-4 | D-5 |
|-------|:---:|:---:|:---:|:---:|:---:|
| Names a specific prior belief (B-#)? | | | | | |
| Traceable to a named artifact (name + date)? | | | | | |
| Design-relevant (names component or decision — not "the system")? | | | | | |
| Genuinely unexpected (not inferable from prior knowledge alone)? | | | | | |
| Survives flat-statement test (no hedging qualifiers required)? | | | | | |
| **Verdict** (VALID / INVALID: check # — reason) | | | | | |

For each VALID deviation, the Curator emits the GATE-CONFIRMED token. The token names
Stage 4 — it does not merely describe routing:
`GATE-CONFIRMED-[N]: VALID -- Stage 4.`

For each INVALID deviation:
`GATE-REJECTED-[N]: INVALID -- Check [#]: [one sentence reason].`

Before emitting Stage 3 output: the Curator scans all prior output for prohibited
dimension synonyms. Any found are corrected via the Vocabulary Declaration mapping
table before COMMIT-STAGE-3 is emitted.

If 2+ VALID deviations: `COMMIT-STAGE-3-CLEAN`.
If fewer than 2 after extended sweep: `COMMIT-STAGE-3-FLAGGED`. Signal Archaeologist
extends Stage 2.

**EXIT condition:** Every deviation has a verdict. 2+ GATE-CONFIRMED tokens present.
COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED emitted.

---

#### Role 3: Impact Synthesizer — Stages 4, 5, and 7

**Mandate:** For each GATE-CONFIRMED surprise: state what was expected (from the referenced
B-#), name the surprise, trace it to its source, articulate its Design Impact (what must
change), and articulate its Build Risk (what is implicated by that change). Then rank,
cluster, and write the artifact.

##### Stage 4 — Individual Surprise Entries

**ENTER condition:** COMMIT-STAGE-3-CLEAN is present. 2+ GATE-CONFIRMED deviations exist.

---

###### Field Reference Block

All five sub-fields are required per entry. Definitions:

**What We Expected**
A direct quotation or paraphrase of the referenced B-# belief from Stage 1 — the specific
prior belief that this surprise contradicts. Full sentence. This is the inertia baseline
for this entry: it makes the epistemic gap explicit.

**Surprise**
A 2–5 word title naming the unexpected finding in plain terms. Full phrase required.

**Signal Source**
The specific artifact that revealed this surprise. Required format: artifact name and/or
namespace and/or date. Full phrase required.
Prohibited generic phrases: "multiple sources," "the signals," "various artifacts,"
"recent work," "signal sweep." These antipatterns make the surprise unverifiable.

**Design Impact**
What must change as a result of this surprise. Full sentence. Names a specific component,
API, flow, schema, or design decision. Not "the system" without a specific referent.
Design Impact is forward-looking: it names the required change action.

**Build Risk**
What is implicated by the Design Impact change. Full sentence. Names a specific component,
decision, or risk surface.
Formula: Design Impact names what must change; Build Risk names what is implicated by
that change.
Structural poles: Design Impact = forward-looking (the change); Build Risk = risk-surface
(the consequence domain of that change). These are structurally distinct. Build Risk is
not a restatement of Design Impact.

---

###### Calibration Entry (not a live entry — do not treat as Surprise 1)

The following worked example is labeled **Surprise 0**. It is a calibration entry,
positioned here to demonstrate all five sub-fields at required quality. It is explicitly
not a live entry.

---

**Surprise 0 — Calibration Entry (not a live entry)**

**What We Expected (B-2):** The team believed that the `ConsentManager` component would
enforce data retention policy uniformly across all storage backends, as stated in the
draft specification reviewed prior to investigation.

**Surprise:** Retention Policy Enforcement Gap

**Signal Source:** `{topic}-trace-state-2026-02-22.md` (trace namespace, state-transition
simulation dated 2026-02-22) — the simulation revealed that the retention policy check
was skipped for cold-storage backends when the `ConsentManager` was in async flush mode.

**Design Impact:** The `ConsentManager` must be refactored to enforce the retention policy
check unconditionally across all backend types, including cold-storage, requiring a new
backend-type-agnostic enforcement hook in the flush pipeline.

**Build Risk:** The refactoring of the flush pipeline enforcement hook implicates the
`DataArchiveScheduler`, which currently relies on the `ConsentManager`'s async flush
completing without interruption; introducing a synchronous retention check into the flush
path will add latency to archival operations and may trigger archival timeouts under
existing SLA constraints.

`COMMIT-ENTRY-0: calibration entry acknowledged.`

---

###### Live Entry Format

One numbered prose block per GATE-CONFIRMED deviation. Emit the per-entry COMMIT token
before beginning the next entry. The per-entry token is required at entry granularity.

---

**Surprise [N] — [Surprise Name]**

**What We Expected (B-[#]):** [direct quotation or paraphrase of the referenced Stage 1
belief — the specific prior expectation this surprise contradicts; full sentence]

**Surprise:** [2–5 word title — full phrase]

**Signal Source:** [named artifact — full phrase with name and/or namespace and/or date;
no generic phrases from the antipattern exclusion list]

**Design Impact:** [full sentence — specific component, API, flow, schema, or decision
that must change; not "the system" without a specific referent]

**Build Risk:** [full sentence — specific component, decision, or risk surface implicated
by the Design Impact change; structurally distinct from Design Impact; not a restatement]

`COMMIT-ENTRY-[N]: entry committed.`

---

**Per-entry EXIT checklist (scan all five sub-fields before emitting COMMIT-ENTRY):**

- [ ] What We Expected: full sentence referencing a specific B-# from Stage 1; states
      the prior belief that is contradicted — not a generic "we thought it would work"
- [ ] Surprise: full phrase, 2–5 words, not a single word or a two-word label
- [ ] Signal Source: named artifact with specificity; none of the following antipatterns
      present: "multiple sources," "the signals," "various artifacts," "recent work,"
      "signal sweep"; if any of these appear, replace with the specific artifact name
      and date before emitting
- [ ] Design Impact: full sentence; names a specific component, API, flow, schema, or
      decision; not "the system" alone; if "the system" appears without a specific
      referent, add the component name before emitting
- [ ] Build Risk: full sentence; names a specific component, decision, or risk surface;
      if Build Risk merely restates Design Impact (i.e., names the same action rather
      than the consequence domain), rewrite to name the downstream affected component
      or risk surface before emitting COMMIT-ENTRY-[N]

COMMIT-STAGE-4.

##### Stage 5 — Rank and Cluster

**Ranking by impact:**

| # | Surprise Name | Impact Rank | Ranking Rationale |
|---|---------------|:-----------:|-------------------|
| | | high / medium / low | |

Impact rank = distance from the Stage 1 opening model. Contradictions (where the surprise
directly inverts a prior belief) rank higher than extensions (where the surprise adds
detail not predicted by a belief but not contradicting it).

**Cluster map:**

| Cluster Name | Member Surprises | Next Team / Skill |
|--------------|:----------------:|-------------------|
| | | |

At least one Next Team / Skill entry must name a specific skill (e.g., `/prove-hypothesis`,
`/draft-spec`, `/trace-contract`) or role (e.g., "retention policy owner"). "Investigate"
alone does not satisfy this criterion.

COMMIT-STAGE-5.

---

#### Role 1 Returns: Signal Archaeologist — Stage 6

**Mandate:** Close the Symmetric Contract. Evaluate the full set of GATE-CONFIRMED surprises
against the Stage 1 opening model and issue the collective verdict.

##### Stage 6 — Closing Collective Synthesis

**ENTER condition:** COMMIT-STAGE-5 is present.

*What did the team, as a whole, learn that it did not expect about `{topic}`?*

| Check | Result |
|-------|--------|
| Opening model (Stage 1 ref) | [restate or reference Stage 1 opening model] |
| Revision direction | CONSISTENT / CONTRADICTORY |
| Epistemic dimensions shifted | [which canonical dimensions moved and how] |
| Implausible-foreknowledge signal | CLEAR / FLAGGED |
| **Collective verdict** | **COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED** |

Implausible-foreknowledge rule: If the Stage 1 belief set, taken collectively, implies
the team held foreknowledge of what the signals would show before investigation began,
record FLAGGED. Do not proceed to Stage 7. Name the belief(s) responsible for the flag.

Explicitly record: CLEAR or FLAGGED.

**EXIT condition:** All five rows populated. Implausible-foreknowledge row contains CLEAR
or FLAGGED. Collective verdict is one of the three canonical values. All dimension cells
in this stage contain canonical names only.

COMMIT-STAGE-6.

---

#### Role 3 Returns: Impact Synthesizer — Stage 7

##### Stage 7 — Artifact Delivery

**ENTER condition:** COMMIT-STAGE-6 is present. Stage 6 implausible-foreknowledge signal
is CLEAR. No FOREKNOWLEDGE-FLAGGED verdict is unresolved.

Write to: `simulations/topic/{topic}-reflect-{date}.md`

Structure (mirrors the Symmetric Contract):

```markdown
---
skill: topic-reflect
topic: {topic}
date: {date}
---

# {Topic} Reflect
*Unexpected findings synthesis. Governing question: What did we learn that we did not expect?*

## Opening Collective Baseline
[Stage 1: opening model paragraph + belief table]

## Surprise Entries
[Stage 4 entries, ranked by impact from Stage 5, as numbered prose blocks including
all five sub-fields: What We Expected, Surprise, Signal Source, Design Impact, Build Risk]

## Closing Collective Synthesis
[Stage 6: collective verdict table]

## Cluster Map
[Stage 5: cluster table]

## Next-Team Register
[Stage 5: Next Team / Skill entries]
```

**EXIT condition:** Artifact written to the correct path. Structure mirrors the Symmetric
Contract (opens with Stage 1 baseline, individual entries in between, closes with Stage 6
synthesis). No unresolved FOREKNOWLEDGE-FLAGGED verdict present. COMMIT-STAGE-7 emitted.

COMMIT-STAGE-7.

---

*End of V-05 prompt body.*

---

*End of document.*
