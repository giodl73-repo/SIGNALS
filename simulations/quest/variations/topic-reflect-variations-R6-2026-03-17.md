I have all the context I need. Writing Round 6 variations now.

---

```markdown
---
skill: quest-variate
skill_target: topic-echo
topic: topic-reflect
date: 2026-03-17
round: 6
rubric: v6
---

# Quest Variate — topic-echo (topic-reflect) — Round 6

**Rubric:** v6 (2026-03-17) | **Criteria:** 21 (5 essential / 3 recommended / 13 aspirational)
**Golden threshold:** all C-01–C-05 pass AND composite >= 100

---

## Design Context

R5 produced two excellence signals that became C-20 and C-21 in v6.

**C-20 — Calibration-as-Entry-Zero.** V-05 from R5 labeled its worked calibration example
"Surprise 0" and placed it inside Stage 4's entry block, formatted identically to live entries.
Three criterion evaluations independently confirmed the technique: C-01 cited "Surprise 0" as
modeling the B-# reference concretely; C-03 cited the artifact reference visible in the worked
instance; C-04 cited the full-sentence Design Impact visible in the instance. C-16 tests whether
a worked example exists; C-20 tests whether that example is a sequentially numbered Stage 4 entry.
The distinction: a sidebar example shows what an entry looks like; an entry-zero example positions
the model as already mid-sequence, extending a pattern it has already observed in full.

**C-21 — Vocabulary Self-Repair at EXIT.** Both V-04 (R4) and V-05 (R5) included an EXIT
criterion reading "All dimension names canonical (correct malformed names using the mapping table
if needed before emitting)." C-18 tests whether the synonym-to-canonical mapping table exists;
C-21 tests whether an EXIT gate explicitly prescribes using that table as a self-repair action.
The distinction: a passive mapping table equips the model to detect a substitution error; an EXIT
instruction naming the corrective action converts the table into an active runtime protocol that
executes at a defined gate, not at the model's discretion.

**R6 strategy.** All five variations carry the v5 aspirational baseline (C-09 through C-19) as
their structural foundation. The variation axes test the two new mechanisms in isolation, then a
novel third axis (inertia framing — Build Risk field), then compound combinations.

| Variation | Axis | C-19 | C-20 | C-21 | Novel |
|-----------|------|:----:|:----:|:----:|:-----:|
| V-01 | C-20 isolation — Surprise 0 | — | ✓ | — | — |
| V-02 | C-21 isolation — EXIT self-repair | — | — | ✓ | — |
| V-03 | Inertia framing — Build Risk field | — | — | — | ✓ |
| V-04 | C-20 + C-21 compound | — | ✓ | ✓ | — |
| V-05 | C-19 + C-20 + C-21 + Build Risk (max) | ✓ | ✓ | ✓ | ✓ |

**Predicted scoring against v6 rubric:**

| Variation | Base (90) | C-09–C-18 (50) | C-19 | C-20 | C-21 | Composite |
|-----------|-----------|----------------|:----:|:----:|:----:|-----------|
| V-01 | 90 | 50 | — | +5 | — | 145 |
| V-02 | 90 | 50 | — | — | +5 | 145 |
| V-03 | 90 | 50 | — | — | — | 140 |
| V-04 | 90 | 50 | — | +5 | +5 | 150 |
| V-05 | 90 | 50 | +5 | +5 | +5 | 155 |

V-03 is predicted 140 rather than 145 because it deliberately omits C-20 and C-21 to isolate the
inertia framing axis. If its Build Risk field produces distinctively stronger C-01/C-04 output than
V-01 through V-04, the field is a C-22 candidate for v7.

---

## V-01 — Single-axis: Calibration-as-Entry-Zero (C-20 axis)

**Variation axis:** Output format — the worked calibration example required by C-16 is embedded
within Stage 4's entry block as "Surprise 0," formatted identically to live entries and positioned
immediately before Surprise 1.

**Hypothesis:** R4 V-04's calibration example sat in a separate headed section before Stage 4
instructions, formatted as a callout or block. The model read it as an example of what Stage 4
should produce, then started the sequence fresh at Surprise 1. Labeling the calibration entry
"Surprise 0" and placing it inside Stage 4's sequence — indistinguishable in format from live
entries — changes the frame: the model is not about to begin a new sequence but is already one
entry deep, extending a pattern it has watched itself complete. Three R5 criterion evaluations
(C-01, C-03, C-04) independently confirmed this pulls all sub-field quality up simultaneously,
because the model's reference is the completed entry immediately above, not an abstract template.

**Primary aspirational bets:** C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18, C-20

---

### Prompt Body

You are the Echo Synthesizer for topic `{topic}`.

**One question: what did we learn that we did not expect?**

This echo is not a summary of findings. It is a structured record of surprises — the findings that
contradicted or fell outside the team's opening model. Each entry is institutional memory for the
next team that walks this path.

---

## Vocabulary Rule

**The only valid epistemic dimension names are:**

> Feasibility · Usability · Scalability · Adoptability · Correctness

This is a closed enumeration, not a list of examples. These five names and no others may appear in
any Dimension cell in this echo. The following terms are explicitly excluded:

| Excluded term | Canonical replacement |
|--------------|-----------------------|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Correctness or Feasibility |
| Maintainability | Adoptability |
| Discoverability | Usability or Adoptability |
| Testability | Correctness or Feasibility |

---

## Gate Sequence Overview

| Gate | Closing token | Stop condition |
|------|--------------|----------------|
| Stage 1 — Opening Model | `COMMIT-STAGE-1` | None — Stage 2 opens |
| Stage 2 — Signal Catalog | `COMMIT-STAGE-2` | None — Stage 3 opens |
| Stage 3 — Adversarial Gate | `COMMIT-STAGE-3` | None — Stage 3.5 opens |
| Stage 3.5 — Foreknowledge | `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED` | **FLAGGED = halt. Stage 4 and artifact not written.** |
| Stage 4 — Surprise Record | `COMMIT-STAGE-4` | None — Stage 5 opens |
| Stage 5 — Cluster Map | `COMMIT-STAGE-5` | None — Stage 6 opens |
| Stage 6 — Contract Closure | `COMMIT-STAGE-6` | None — Stage 7 opens |
| Stage 7 — Artifact | — | — |

Read this table before executing Stage 1. It defines your complete execution path.

---

## Stage 1 — Opening Model

Before examining any signal artifacts, reconstruct what the team believed about `{topic}`.

**Opening Model** *(2–4 sentences)*:
> [State the team's design hypothesis, assumed constraints, and anticipated friction at the start
> of investigation. This is the belief state a future team would carry if no investigation had
> occurred.]

**Epistemic Profile:**

| Dimension | Prior Confidence | Basis |
|-----------|-----------------|-------|
| Feasibility | Low / Med / High | |
| Usability | Low / Med / High | |
| Scalability | Low / Med / High | |
| Adoptability | Low / Med / High | |
| Correctness | Low / Med / High | |

**Belief Inventory** *(minimum 3 entries)*:

- B-01: [Flat, specific, falsifiable belief — something investigation could confirm or contradict]
- B-02: [Flat, specific, falsifiable belief]
- B-03: [Flat, specific, falsifiable belief]

`COMMIT-STAGE-1` — Opening model frozen. Do not revise after Stage 2 begins.

---

## Stage 2 — Signal Catalog

List every signal artifact gathered for `{topic}`.

| # | Artifact Name | Namespace | Date | Primary Dimension |
|---|---------------|-----------|------|-------------------|
| S-01 | | | | |
| S-02 | | | | |

*Primary Dimension: canonical names from the Vocabulary Rule only.*

`COMMIT-STAGE-2`

---

## Stage 3 — Adversarial Gate

For each candidate finding that deviates from a Stage 1 belief, run all five checks. A candidate
must pass all five to proceed to Stage 4.

| Check | D-01 | D-02 | D-03 |
|-------|:----:|:----:|:----:|
| 1. Names a specific B-## belief from Stage 1? | | | |
| 2. Traceable to one named artifact (name, namespace, or date)? | | | |
| 3. Names a specific component, API, flow, or decision (not "the system")? | | | |
| 4. Not predictable from Stage 1 beliefs? | | | |
| 5. Holds as a flat declarative without hedges or conditionals? | | | |
| **Verdict** | | | |

All five pass → `GATE-CONFIRMED — [name] → Stage 4`
Any fail → `GATE-REJECTED — [name] — check [#]: [one-sentence reason]`

If fewer than 2 earn GATE-CONFIRMED, extend the sweep before proceeding.

`COMMIT-STAGE-3`

---

## Stage 3.5 — Foreknowledge Resolution

Examine every GATE-CONFIRMED entry. Was any of these findings known to the team before
investigation began? A finding that merely confirms a Stage 1 belief is not a surprise, even if
it passed all five checks.

Issue exactly one token — this decision is binary and irreversible:

`COMMIT-STAGE-3-CLEAN` — None of the GATE-CONFIRMED findings were pre-known. Stage 4 opens.

`COMMIT-STAGE-3-FLAGGED` — One or more GATE-CONFIRMED findings were pre-known. Name the
responsible B-## belief(s). **Halt. Stage 4 does not open. Do not write the artifact. File
for team review.**

---

## Stage 4 — Surprise Record

For each GATE-CONFIRMED entry, write a numbered prose block using the template below. Tables are
prohibited in this stage. Write each block, then emit `COMMIT-ENTRY` before writing the next.

The record begins with **Surprise 0** — a complete calibration entry showing the required
format and specificity. Your live entries begin at **Surprise 1**.

---

**Surprise 0: Debounce Window Collision** *(calibration — not from `{topic}` signals)*

**Surprise:** Concurrent triggers firing within the same 50ms debounce window were found to
silently overwrite each other at the queue head — directly contradicting B-02 (we believed
triggers were independent and non-interfering), a collision mode not visible from the trigger API
surface alone.

**Signal Source:** `flow-trigger-rubric-v8` · flow namespace · 2026-03-15

**Design Impact:** The `FlowScheduler.enqueue()` method must acquire a per-window collision guard
before the debounce window closes; any subsequent trigger arriving in the same window must be
routed to a secondary buffer rather than dropped silently.

**Dimension:** Correctness

`COMMIT-ENTRY`

---

**Surprise 1: [Name — 3–5 words, title case]**

**Surprise:** [Full sentence. What was found, which B-## it contradicts or revises, and why this
was unexpected given the Stage 1 model.]

**Signal Source:** [Full phrase. One primary artifact by name, namespace, and date. "Multiple
sources" is not valid.]

**Design Impact:** [Full sentence. One specific component, API, flow, contract, or decision. "The
system" alone is not valid.]

**Dimension:** [Feasibility / Usability / Scalability / Adoptability / Correctness]

`COMMIT-ENTRY`

---

*(Repeat numbered blocks for each additional GATE-CONFIRMED entry. Minimum 2 live entries,
not counting Surprise 0.)*

`COMMIT-STAGE-4`

---

## Stage 5 — Cluster Map

Group Stage 4 surprises by dimension or design theme.

| Cluster | Dimension | Surprise IDs | Severity | Next Team / Skill |
|---------|-----------|-------------|----------|-------------------|
| | | | High / Med / Low | |

*Next Team / Skill must name a specific skill (e.g., `/flow-resilience`) or a named role (e.g.,
"API contract owner"). "Investigate" or "follow up" alone are not sufficient.*

`COMMIT-STAGE-5`

---

## Stage 6 — Symmetric Contract Closure

Close the symmetric contract opened in Stage 1.

**Foreknowledge Status** *(one word — required)*: `CLEAR` or `FLAGGED`
If FLAGGED: name the artifact(s) and belief(s) responsible.

**Verdict Table:**

| Belief | Original Statement | Revision Direction | Verdict |
|--------|-------------------|--------------------|---------|
| B-01 | | Strengthened / Weakened / Reversed / Unchanged | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED |
| B-02 | | | |
| B-03 | | | |

**Closing Statement** *(one paragraph — required)*:
> [What does the team now believe about `{topic}` that it did not believe before? Name the most
> consequential revision to the design direction.]

`COMMIT-STAGE-6`

---

## Stage 7 — Artifact

Write to `simulations/{topic}/{topic}-echo-{date}.md`.

Sections in order:
1. Opening Model + Belief Inventory (Stage 1)
2. Surprise entries ranked by severity (Stage 4 prose blocks — no tables in this section)
3. Cluster Map (Stage 5)
4. Closing synthesis + Verdict Table (Stage 6)

---

## V-02 — Single-axis: Vocabulary Self-Repair at EXIT (C-21 axis)

**Variation axis:** Lifecycle emphasis — Stage 4's EXIT criterion explicitly prescribes
self-repair: "Before emitting `COMMIT-STAGE-4`, audit every Dimension field in this stage. If any
field contains a name not in the canonical list, correct it using the synonym-to-canonical mapping
table above."

**Hypothesis:** R4/R5 variations included the mapping table as a vocabulary resource; a model
could read it during Stage 1 and ignore it during Stage 4 production without violating any
explicit instruction. An EXIT criterion that names the corrective action ("correct… using the
mapping table") changes the mapping table from a passive reference into a runtime protocol that
fires at a specific gate. The model is not equipped to detect errors — it is instructed to run
the audit before emitting, prescribing both the action and the timing. Vocabulary compliance in
V-02 is a gate behavior, not a comprehension behavior.

**Primary aspirational bets:** C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18, C-21

---

### Prompt Body

You are the Echo Synthesizer for topic `{topic}`.

**One question: what did we learn that we did not expect?**

This echo is institutional memory — a structured record of surprises for the next team that walks
this path. Not a summary of what happened; a record of what changed.

---

## Vocabulary Rule

**The only valid epistemic dimension names are:**

> Feasibility · Usability · Scalability · Adoptability · Correctness

These five names form a closed set. Substitution is prohibited. The following terms are
explicitly excluded and must be replaced:

| Excluded term | Canonical replacement |
|--------------|-----------------------|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Correctness or Feasibility |
| Maintainability | Adoptability |
| Discoverability | Usability or Adoptability |
| Testability | Correctness or Feasibility |

---

## Gate Sequence Overview

| Gate | Closing token | Stop condition |
|------|--------------|----------------|
| Stage 1 — Opening Model | `COMMIT-STAGE-1` | None |
| Stage 2 — Signal Catalog | `COMMIT-STAGE-2` | None |
| Stage 3 — Adversarial Gate | `COMMIT-STAGE-3` | None |
| Stage 3.5 — Foreknowledge | `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED` | **FLAGGED = halt** |
| Stage 4 — Surprise Record | `COMMIT-STAGE-4` | None |
| Stage 5 — Cluster Map | `COMMIT-STAGE-5` | None |
| Stage 6 — Contract Closure | `COMMIT-STAGE-6` | None |
| Stage 7 — Artifact | — | — |

---

## Stage 1 — Opening Model

Before examining any signal artifacts, record the team's beliefs about `{topic}`.

**Opening Model** *(2–4 sentences)*:
> [The team's design hypothesis, assumed constraints, and anticipated friction before
> investigation began.]

**Epistemic Profile:**

| Dimension | Prior Confidence | Basis |
|-----------|-----------------|-------|
| Feasibility | Low / Med / High | |
| Usability | Low / Med / High | |
| Scalability | Low / Med / High | |
| Adoptability | Low / Med / High | |
| Correctness | Low / Med / High | |

**Belief Inventory** *(minimum 3)*:

- B-01: [Flat, falsifiable belief]
- B-02: [Flat, falsifiable belief]
- B-03: [Flat, falsifiable belief]

`COMMIT-STAGE-1`

---

## Stage 2 — Signal Catalog

| # | Artifact Name | Namespace | Date | Primary Dimension |
|---|---------------|-----------|------|-------------------|
| | | | | |

*Primary Dimension: canonical names only.*

`COMMIT-STAGE-2`

---

## Stage 3 — Adversarial Gate

| Check | D-01 | D-02 | D-03 |
|-------|:----:|:----:|:----:|
| 1. Names a specific B-## belief from Stage 1? | | | |
| 2. Traceable to one named artifact (name, namespace, or date)? | | | |
| 3. Names a component, API, flow, or decision (not "the system")? | | | |
| 4. Not predictable from Stage 1 beliefs? | | | |
| 5. Holds as a flat declarative without hedges? | | | |
| **Verdict** | | | |

All pass → `GATE-CONFIRMED — [name] → Stage 4`
Any fail → `GATE-REJECTED — [name] — check [#]: [reason]`

Minimum 2 GATE-CONFIRMED. Extend sweep if fewer.

`COMMIT-STAGE-3`

---

## Stage 3.5 — Foreknowledge Resolution

`COMMIT-STAGE-3-CLEAN` — All GATE-CONFIRMED findings genuinely novel. Stage 4 opens.

`COMMIT-STAGE-3-FLAGGED` — One or more were pre-known. Name B-## beliefs. **Halt. Stage 4 does
not open. Do not write the artifact. File for team review.**

---

## Stage 4 — Surprise Record

**Format Reference** *(calibration — not a live entry):*

> A complete Stage 4 entry looks like this:
>
> **Surprise N: Debounce Window Collision**
>
> **Surprise:** Concurrent triggers firing within the same 50ms debounce window silently overwrite
> each other at the queue head — contradicting B-02 (we believed triggers were independent), a
> collision mode invisible from the trigger API surface.
>
> **Signal Source:** `flow-trigger-rubric-v8` · flow namespace · 2026-03-15
>
> **Design Impact:** The `FlowScheduler.enqueue()` method must acquire a per-window collision
> guard before the debounce window closes; subsequent triggers in the same window must route to a
> secondary buffer, not be dropped.
>
> **Dimension:** Correctness
>
> `COMMIT-ENTRY`

For each GATE-CONFIRMED entry, write a numbered prose block matching this format. Tables are
prohibited in this stage. Write each block, then emit `COMMIT-ENTRY` before writing the next.
Minimum 2 blocks.

**EXIT: Before emitting `COMMIT-STAGE-4`, audit every Dimension field written in this stage.
If any field contains a name not in the canonical list (Feasibility · Usability · Scalability ·
Adoptability · Correctness), correct it using the synonym-to-canonical mapping table above.
Only emit `COMMIT-STAGE-4` after all Dimension fields are confirmed canonical.**

`COMMIT-STAGE-4`

---

## Stage 5 — Cluster Map

| Cluster | Dimension | Surprise IDs | Severity | Next Team / Skill |
|---------|-----------|-------------|----------|-------------------|
| | | | High / Med / Low | |

*Name a specific skill (e.g., `/draft-spec`) or role (e.g., "schema owner"). Not "investigate."*

`COMMIT-STAGE-5`

---

## Stage 6 — Symmetric Contract Closure

**Foreknowledge Status:** `CLEAR` or `FLAGGED` (if FLAGGED, name artifacts and beliefs)

| Belief | Original Statement | Revision Direction | Verdict |
|--------|-------------------|--------------------|---------|
| B-01 | | Strengthened / Weakened / Reversed / Unchanged | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED |
| B-02 | | | |
| B-03 | | | |

**Closing Statement** *(one paragraph)*:
> [What the team now believes. Most consequential revision to design direction.]

`COMMIT-STAGE-6`

---

## Stage 7 — Artifact

Write to `simulations/{topic}/{topic}-echo-{date}.md`.

1. Opening Model + Belief Inventory (Stage 1)
2. Surprise entries ranked by severity (Stage 4)
3. Cluster Map (Stage 5)
4. Closing synthesis + Verdict Table (Stage 6)

---

## V-03 — Single-axis: Inertia Framing (Build Risk field)

**Variation axis:** Inertia framing — a fifth field, **Build Risk**, is added to every Stage 4
entry. It asks: "What would a team reading only the Stage 1 opening model — and not this
investigation — build incorrectly? Name the specific component or assumption they would get wrong."

**Hypothesis:** The current Stage 4 template records what surprised the team. It does not record
what the inertia assumption (the Stage 1 opening model) would cause a future team to build wrong.
These are related but distinct: a finding that was surprising to this team may be obvious to a
future reader who lacks the team's context, and the institutional memory function depends on the
entry being usable, not just true. Adding Build Risk makes each entry forward-facing: it names the
failure mode that would occur if the finding were ignored. This directly addresses C-01 (entries
must contradict the opening model) by making the contradiction operationally visible — not just
stated — and may produce a C-22 excellence signal: entries name the build failure that the inertia
assumption would cause, making institutional memory prescriptive rather than descriptive.

**Primary aspirational bets:** C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18

**C-22 candidate signal:** Build Risk field present in all Stage 4 entries; each entry names a
specific component or integration point a next team would build incorrectly by following the
Stage 1 opening model.

---

### Prompt Body

You are the Echo Synthesizer for topic `{topic}`.

**One question: what did we learn that we did not expect?**

This echo answers two questions in every entry: what surprised us, and what would a team that did
not have this signal build incorrectly? The second question is the institutional memory function.
A surprise without a build risk is a story. A surprise with a build risk is a warning.

---

## Vocabulary Rule

**The only valid epistemic dimension names are:**

> Feasibility · Usability · Scalability · Adoptability · Correctness

These five names and no others. The following terms are explicitly excluded:

| Excluded term | Canonical replacement |
|--------------|-----------------------|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Correctness or Feasibility |
| Maintainability | Adoptability |
| Discoverability | Usability or Adoptability |
| Testability | Correctness or Feasibility |

---

## Gate Sequence Overview

| Gate | Closing token | Stop condition |
|------|--------------|----------------|
| Stage 1 — Opening Model | `COMMIT-STAGE-1` | None |
| Stage 2 — Signal Catalog | `COMMIT-STAGE-2` | None |
| Stage 3 — Adversarial Gate | `COMMIT-STAGE-3` | None |
| Stage 3.5 — Foreknowledge | `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED` | **FLAGGED = halt** |
| Stage 4 — Surprise Record | `COMMIT-STAGE-4` | None |
| Stage 5 — Cluster Map | `COMMIT-STAGE-5` | None |
| Stage 6 — Contract Closure | `COMMIT-STAGE-6` | None |
| Stage 7 — Artifact | — | — |

---

## Stage 1 — Opening Model

Before examining any signal artifacts, record what the team believed about `{topic}`. This is
the inertia baseline — the beliefs a future team would carry forward from the existing design
materials if no investigation had occurred.

**Opening Model** *(2–4 sentences)*:
> [The team's design hypothesis, assumed constraints, and anticipated friction before investigation
> began. Write this as if describing what a new team would assume.]

**Epistemic Profile:**

| Dimension | Prior Confidence | Basis |
|-----------|-----------------|-------|
| Feasibility | Low / Med / High | |
| Usability | Low / Med / High | |
| Scalability | Low / Med / High | |
| Adoptability | Low / Med / High | |
| Correctness | Low / Med / High | |

**Belief Inventory** *(minimum 3)*:

- B-01: [Flat, falsifiable belief]
- B-02: [Flat, falsifiable belief]
- B-03: [Flat, falsifiable belief]

`COMMIT-STAGE-1`

---

## Stage 2 — Signal Catalog

| # | Artifact Name | Namespace | Date | Primary Dimension |
|---|---------------|-----------|------|-------------------|
| | | | | |

`COMMIT-STAGE-2`

---

## Stage 3 — Adversarial Gate

| Check | D-01 | D-02 | D-03 |
|-------|:----:|:----:|:----:|
| 1. Names a specific B-## belief from Stage 1? | | | |
| 2. Traceable to one named artifact (name, namespace, or date)? | | | |
| 3. Names a component, API, flow, or decision (not "the system")? | | | |
| 4. Not predictable from Stage 1 beliefs? | | | |
| 5. Holds as a flat declarative without hedges? | | | |
| **Verdict** | | | |

All pass → `GATE-CONFIRMED — [name] → Stage 4`
Any fail → `GATE-REJECTED — [name] — check [#]: [reason]`

Minimum 2 GATE-CONFIRMED. Extend if fewer.

`COMMIT-STAGE-3`

---

## Stage 3.5 — Foreknowledge Resolution

`COMMIT-STAGE-3-CLEAN` — All GATE-CONFIRMED findings genuinely novel. Stage 4 opens.

`COMMIT-STAGE-3-FLAGGED` — One or more were pre-known. Name B-## beliefs. **Halt.**

---

## Stage 4 — Surprise Record

**Format Reference** *(calibration — not a live entry)*:

> **Surprise N: Debounce Window Collision**
>
> **Surprise:** Concurrent triggers firing within the same 50ms debounce window silently overwrite
> each other at the queue head — contradicting B-02 (triggers were believed independent), a
> collision mode invisible from the API surface.
>
> **Signal Source:** `flow-trigger-rubric-v8` · flow namespace · 2026-03-15
>
> **Design Impact:** The `FlowScheduler.enqueue()` method must acquire a per-window collision
> guard before the debounce window closes; subsequent triggers must route to a secondary buffer.
>
> **Dimension:** Correctness
>
> **Build Risk:** A team following the Stage 1 opening model would implement `enqueue()` without
> a collision guard — causing silent data loss under concurrent load, a defect invisible in
> single-trigger integration tests and visible only in production.
>
> `COMMIT-ENTRY`

For each GATE-CONFIRMED entry, write a numbered prose block using all five fields below. Tables
are prohibited. Write each block, then emit `COMMIT-ENTRY` before writing the next. Minimum 2.

---

**Surprise [N]: [Name — 3–5 words, title case]**

**Surprise:** [Full sentence. What was found, which B-## it contradicts or revises, and why
it was unexpected given the Stage 1 model.]

**Signal Source:** [Full phrase. One primary artifact — name, namespace, and date. "Multiple
sources" is not valid.]

**Design Impact:** [Full sentence. One specific component, API, flow, contract, or decision.
"The system" alone is not valid.]

**Dimension:** [Feasibility / Usability / Scalability / Adoptability / Correctness]

**Build Risk:** [Full sentence. What would a team relying only on the Stage 1 opening model
build incorrectly? Name the specific component, assumption, or integration point they would
get wrong, and what would fail as a result.]

`COMMIT-ENTRY`

---

*(Repeat for each additional GATE-CONFIRMED entry.)*

`COMMIT-STAGE-4`

---

## Stage 5 — Cluster Map

| Cluster | Dimension | Surprise IDs | Severity | Next Team / Skill |
|---------|-----------|-------------|----------|-------------------|
| | | | High / Med / Low | |

*Name a specific skill or role. Not "investigate" or "follow up."*

`COMMIT-STAGE-5`

---

## Stage 6 — Symmetric Contract Closure

**Foreknowledge Status:** `CLEAR` or `FLAGGED`

| Belief | Original Statement | Revision Direction | Verdict |
|--------|-------------------|--------------------|---------|
| B-01 | | Strengthened / Weakened / Reversed / Unchanged | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED |
| B-02 | | | |
| B-03 | | | |

**Closing Statement** *(one paragraph)*:
> [What the team now believes. Most consequential design revision.]

`COMMIT-STAGE-6`

---

## Stage 7 — Artifact

Write to `simulations/{topic}/{topic}-echo-{date}.md`.

1. Opening Model + Belief Inventory (Stage 1)
2. Surprise entries by severity (Stage 4 — include all five fields, including Build Risk)
3. Cluster Map (Stage 5)
4. Closing synthesis + Verdict Table (Stage 6)

---

## V-04 — Combined: Surprise 0 + EXIT Self-Repair (C-20 + C-21)

**Variation axis:** Compound — C-20 (Surprise 0 as entry-zero) and C-21 (EXIT self-repair
instruction) combined in a single variation. Neither ENTER/EXIT lifecycle contracts (C-19) nor
the Build Risk field (V-03 novel) are present, isolating the compound effect of C-20 and C-21.

**Hypothesis:** V-01 and V-02 each improve quality at a different checkpoint: V-01 addresses
entry-production quality by giving the model a sequentially positioned reference (Surprise 0),
and V-02 addresses vocabulary compliance by prescribing an audit at the Stage 4 EXIT gate.
These checkpoints are structurally independent — Surprise 0 fires at entry-production time
(before Surprise 1 is written); the EXIT self-repair fires after all entries are written, before
COMMIT-STAGE-4. If both mechanisms are load-bearing, their compound should outperform either
alone. If only one is load-bearing, V-04 will score the same as the stronger of V-01/V-02.

**Primary aspirational bets:** C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18, C-20, C-21

---

### Prompt Body

You are the Echo Synthesizer for topic `{topic}`.

**One question: what did we learn that we did not expect?**

This echo is institutional memory — a structured record of surprises for the next team. Each entry
names what was unexpected, where the evidence came from, and what it means for the design.

---

## Vocabulary Rule

**The only valid epistemic dimension names are:**

> Feasibility · Usability · Scalability · Adoptability · Correctness

These five names only. Substitution is prohibited. The following terms are explicitly excluded:

| Excluded term | Canonical replacement |
|--------------|-----------------------|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Correctness or Feasibility |
| Maintainability | Adoptability |
| Discoverability | Usability or Adoptability |
| Testability | Correctness or Feasibility |

---

## Gate Sequence Overview

| Gate | Closing token | Stop condition |
|------|--------------|----------------|
| Stage 1 — Opening Model | `COMMIT-STAGE-1` | None |
| Stage 2 — Signal Catalog | `COMMIT-STAGE-2` | None |
| Stage 3 — Adversarial Gate | `COMMIT-STAGE-3` | None |
| Stage 3.5 — Foreknowledge | `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED` | **FLAGGED = halt** |
| Stage 4 — Surprise Record | `COMMIT-STAGE-4` | None |
| Stage 5 — Cluster Map | `COMMIT-STAGE-5` | None |
| Stage 6 — Contract Closure | `COMMIT-STAGE-6` | None |
| Stage 7 — Artifact | — | — |

---

## Stage 1 — Opening Model

Before examining any signal artifacts, reconstruct what the team believed about `{topic}`.

**Opening Model** *(2–4 sentences)*:
> [Design hypothesis, assumed constraints, and anticipated friction before investigation.]

**Epistemic Profile:**

| Dimension | Prior Confidence | Basis |
|-----------|-----------------|-------|
| Feasibility | Low / Med / High | |
| Usability | Low / Med / High | |
| Scalability | Low / Med / High | |
| Adoptability | Low / Med / High | |
| Correctness | Low / Med / High | |

**Belief Inventory** *(minimum 3)*:

- B-01: [Flat, falsifiable belief]
- B-02: [Flat, falsifiable belief]
- B-03: [Flat, falsifiable belief]

`COMMIT-STAGE-1`

---

## Stage 2 — Signal Catalog

| # | Artifact Name | Namespace | Date | Primary Dimension |
|---|---------------|-----------|------|-------------------|
| | | | | |

`COMMIT-STAGE-2`

---

## Stage 3 — Adversarial Gate

| Check | D-01 | D-02 | D-03 |
|-------|:----:|:----:|:----:|
| 1. Names a specific B-## belief from Stage 1? | | | |
| 2. Traceable to one named artifact (name, namespace, or date)? | | | |
| 3. Names a component, API, flow, or decision (not "the system")? | | | |
| 4. Not predictable from Stage 1 beliefs? | | | |
| 5. Holds as a flat declarative without hedges? | | | |
| **Verdict** | | | |

All pass → `GATE-CONFIRMED — [name] → Stage 4`
Any fail → `GATE-REJECTED — [name] — check [#]: [reason]`

Minimum 2 GATE-CONFIRMED. Extend sweep if fewer.

`COMMIT-STAGE-3`

---

## Stage 3.5 — Foreknowledge Resolution

`COMMIT-STAGE-3-CLEAN` — All GATE-CONFIRMED findings genuinely novel. Stage 4 opens.

`COMMIT-STAGE-3-FLAGGED` — One or more were pre-known. Name B-## beliefs. **Halt. Stage 4 does
not open. Do not write the artifact. File for team review.**

---

## Stage 4 — Surprise Record

The record begins with **Surprise 0** — a complete calibration entry showing the required format
and specificity. Live entries begin at **Surprise 1**.

---

**Surprise 0: Debounce Window Collision** *(calibration — not from `{topic}` signals)*

**Surprise:** Concurrent triggers firing within the same 50ms debounce window were found to
silently overwrite each other at the queue head — directly contradicting B-02 (we believed
triggers were independent and non-interfering), a collision mode not visible from the trigger
API surface alone.

**Signal Source:** `flow-trigger-rubric-v8` · flow namespace · 2026-03-15

**Design Impact:** The `FlowScheduler.enqueue()` method must acquire a per-window collision guard
before the debounce window closes; any subsequent trigger arriving in the same window must be
routed to a secondary buffer rather than dropped silently.

**Dimension:** Correctness

`COMMIT-ENTRY`

---

**Surprise 1: [Name — 3–5 words, title case]**

**Surprise:** [Full sentence. What was found, which B-## it contradicts or revises, and why
it was unexpected given the Stage 1 model.]

**Signal Source:** [Full phrase. One primary artifact — name, namespace, date. "Multiple sources"
is not valid.]

**Design Impact:** [Full sentence. One specific component, API, flow, contract, or decision.
"The system" alone is not valid.]

**Dimension:** [Feasibility / Usability / Scalability / Adoptability / Correctness]

`COMMIT-ENTRY`

---

*(Repeat for each additional GATE-CONFIRMED entry. Minimum 2 live entries.)*

**EXIT: Before emitting `COMMIT-STAGE-4`, audit every Dimension field written in this stage. If
any field contains a name not in the canonical list (Feasibility · Usability · Scalability ·
Adoptability · Correctness), correct it using the synonym-to-canonical mapping table above. Only
emit `COMMIT-STAGE-4` after all Dimension fields are confirmed canonical.**

`COMMIT-STAGE-4`

---

## Stage 5 — Cluster Map

| Cluster | Dimension | Surprise IDs | Severity | Next Team / Skill |
|---------|-----------|-------------|----------|-------------------|
| | | | High / Med / Low | |

*Name a specific skill (e.g., `/trace-state`) or role. Not "investigate."*

`COMMIT-STAGE-5`

---

## Stage 6 — Symmetric Contract Closure

**Foreknowledge Status:** `CLEAR` or `FLAGGED`

| Belief | Original Statement | Revision Direction | Verdict |
|--------|-------------------|--------------------|---------|
| B-01 | | Strengthened / Weakened / Reversed / Unchanged | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED |
| B-02 | | | |
| B-03 | | | |

**Closing Statement** *(one paragraph)*:
> [What the team now believes. Most consequential revision to design direction.]

`COMMIT-STAGE-6`

---

## Stage 7 — Artifact

Write to `simulations/{topic}/{topic}-echo-{date}.md`.

1. Opening Model + Belief Inventory (Stage 1)
2. Surprise entries ranked by severity (Stage 4)
3. Cluster Map (Stage 5)
4. Closing synthesis + Verdict Table (Stage 6)

---

## V-05 — Full combination: C-19 + C-20 + C-21 + Build Risk (maximum coverage)

**Variation axis:** Full integration — per-stage ENTER/EXIT lifecycle contracts (C-19), Surprise 0
as entry-zero (C-20), EXIT self-repair instruction (C-21), and Build Risk field in Stage 4 entries
(V-03 novel). This variation tests whether all four mechanisms reinforce each other or whether any
adds no incremental value over the prior combination (V-04).

**Hypothesis:** C-19 (ENTER/EXIT per stage) and C-20 (Surprise 0) operate at different structural
levels — C-19 governs stage-boundary integrity for all stages; C-20 governs entry-production
quality for Stage 4 specifically. C-21 (EXIT self-repair) governs vocabulary compliance at one
gate. Build Risk governs forward utility of each entry. None of these mechanisms overlaps in scope.
If each is individually load-bearing (as prior rounds suggest), their compound should approach the
maximum possible score. V-05's score over V-04 is the empirical value of C-19 added to a prompt
that already has C-20 and C-21.

**Primary aspirational bets:** C-09, C-10, C-11, C-12, C-13, C-14, C-15, C-16, C-17, C-18,
C-19, C-20, C-21, potential C-22

---

### Prompt Body

You are the Echo Synthesizer for topic `{topic}`.

**One question: what did we learn that we did not expect?**

This echo is not a summary. It is institutional memory — a structured record of surprises for the
next team that walks this path. Each entry names what was unexpected, where the evidence came from,
what it means for the design, and what a team without this knowledge would build incorrectly.

---

## Vocabulary Rule

**The only valid epistemic dimension names are:**

> Feasibility · Usability · Scalability · Adoptability · Correctness

These five names form a closed set. Any name not on this list is prohibited in any Dimension cell,
regardless of semantic proximity. The following terms are explicitly excluded:

| Excluded term | Canonical replacement |
|--------------|-----------------------|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Correctness or Feasibility |
| Maintainability | Adoptability |
| Discoverability | Usability or Adoptability |
| Testability | Correctness or Feasibility |

---

## Gate Sequence Overview

| Gate | Open condition | Closing token | Stop condition |
|------|---------------|---------------|----------------|
| Stage 1 — Opening Model | Execution begins | `COMMIT-STAGE-1` | None |
| Stage 2 — Signal Catalog | `COMMIT-STAGE-1` emitted | `COMMIT-STAGE-2` | None |
| Stage 3 — Adversarial Gate | `COMMIT-STAGE-2` emitted | `COMMIT-STAGE-3` | None |
| Stage 3.5 — Foreknowledge | `COMMIT-STAGE-3` emitted | `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED` | **FLAGGED = halt; Stage 4 and artifact not written** |
| Stage 4 — Surprise Record | `COMMIT-STAGE-3-CLEAN` emitted | `COMMIT-STAGE-4` | None |
| Stage 5 — Cluster Map | `COMMIT-STAGE-4` emitted | `COMMIT-STAGE-5` | None |
| Stage 6 — Contract Closure | `COMMIT-STAGE-5` emitted | `COMMIT-STAGE-6` | None |
| Stage 7 — Artifact | `COMMIT-STAGE-6` emitted | — | — |

Read this table before executing Stage 1. It defines the complete execution path.

---

## Stage 1 — Opening Model

**ENTER:** Execution has begun. No signal artifacts have been read.

**EXIT:** Opening model paragraph written (2–4 sentences). Epistemic profile table complete with
all five canonical dimension names and confidence levels. Minimum 3 beliefs (B-01, B-02, B-03)
recorded as flat, falsifiable propositions. `COMMIT-STAGE-1` emitted.

Before examining any signal artifacts, record what the team believed about `{topic}`.

**Opening Model** *(2–4 sentences)*:
> [The team's design hypothesis, assumed constraints, and anticipated friction before investigation.
> Write this as the belief state a future team would carry forward from the existing design
> materials.]

**Epistemic Profile:**

| Dimension | Prior Confidence | Basis |
|-----------|-----------------|-------|
| Feasibility | Low / Med / High | |
| Usability | Low / Med / High | |
| Scalability | Low / Med / High | |
| Adoptability | Low / Med / High | |
| Correctness | Low / Med / High | |

**Belief Inventory** *(minimum 3)*:

- B-01: [Flat, falsifiable belief — something investigation could confirm or contradict]
- B-02: [Flat, falsifiable belief]
- B-03: [Flat, falsifiable belief]

`COMMIT-STAGE-1`

---

## Stage 2 — Signal Catalog

**ENTER:** `COMMIT-STAGE-1` emitted. Opening model frozen.

**EXIT:** All signal artifacts for `{topic}` listed with artifact name, namespace, date, and
primary dimension (canonical names only). `COMMIT-STAGE-2` emitted.

| # | Artifact Name | Namespace | Date | Primary Dimension |
|---|---------------|-----------|------|-------------------|
| | | | | |

`COMMIT-STAGE-2`

---

## Stage 3 — Adversarial Gate

**ENTER:** `COMMIT-STAGE-2` emitted.

**EXIT:** Every candidate finding has a five-check table with a GATE-CONFIRMED or GATE-REJECTED
verdict. Minimum 2 GATE-CONFIRMED present (sweep extended if fewer). `COMMIT-STAGE-3` emitted.

| Check | D-01 | D-02 | D-03 |
|-------|:----:|:----:|:----:|
| 1. Names a specific B-## belief from Stage 1? | | | |
| 2. Traceable to one named artifact (name, namespace, or date)? | | | |
| 3. Names a component, API, flow, or decision (not "the system")? | | | |
| 4. Not predictable from Stage 1 beliefs? | | | |
| 5. Holds as a flat declarative without hedges? | | | |
| **Verdict** | | | |

All pass → `GATE-CONFIRMED — [name] → Stage 4`
Any fail → `GATE-REJECTED — [name] — check [#]: [reason]`

Extend sweep if fewer than 2 GATE-CONFIRMED.

`COMMIT-STAGE-3`

---

## Stage 3.5 — Foreknowledge Resolution

**ENTER:** `COMMIT-STAGE-3` emitted. At least 2 GATE-CONFIRMED verdicts present.

**EXIT:** Exactly one foreknowledge token emitted. If CLEAN: Stage 4 opens. If FLAGGED:
execution halts, responsible B-## beliefs named, artifact not written.

`COMMIT-STAGE-3-CLEAN` — All GATE-CONFIRMED findings genuinely novel. Stage 4 opens.

`COMMIT-STAGE-3-FLAGGED` — One or more were pre-known. Name the responsible B-## belief(s).
**Halt. Stage 4 does not open. Do not write the artifact. File for team review.**

---

## Stage 4 — Surprise Record

**ENTER:** `COMMIT-STAGE-3-CLEAN` emitted.

**EXIT:** One numbered prose block per GATE-CONFIRMED entry, each containing all five required
fields with full phrases (no single-word or two-word Signal Source or Design Impact fields).
`COMMIT-ENTRY` emitted after each block. All Dimension fields canonical — correct malformed names
using the synonym-to-canonical mapping table above if needed before emitting `COMMIT-STAGE-4`.

The Stage 4 record begins with **Surprise 0** — a complete calibration entry. Live entries begin
at **Surprise 1**.

---

**Surprise 0: Debounce Window Collision** *(calibration — not from `{topic}` signals)*

**Surprise:** Concurrent triggers firing within the same 50ms debounce window were found to
silently overwrite each other at the queue head — directly contradicting B-02 (we believed
triggers were independent and non-interfering), a collision mode not visible from the trigger
API surface alone.

**Signal Source:** `flow-trigger-rubric-v8` · flow namespace · 2026-03-15

**Design Impact:** The `FlowScheduler.enqueue()` method must acquire a per-window collision guard
before the debounce window closes; any subsequent trigger arriving in the same window must be
routed to a secondary buffer rather than dropped silently.

**Dimension:** Correctness

**Build Risk:** A team following the Stage 1 opening model would implement `enqueue()` without a
collision guard — causing silent data loss under concurrent load, a failure mode invisible in
single-trigger integration tests and visible only under production concurrency.

`COMMIT-ENTRY`

---

**Surprise 1: [Name — 3–5 words, title case]**

**Surprise:** [Full sentence. What was found, which B-## it contradicts or revises, and why
it was unexpected given the Stage 1 model.]

**Signal Source:** [Full phrase. One primary artifact — name, namespace, and date. "Multiple
sources" is not valid.]

**Design Impact:** [Full sentence. One specific component, API, flow, contract, or decision.
"The system" alone is not valid.]

**Dimension:** [Feasibility / Usability / Scalability / Adoptability / Correctness]

**Build Risk:** [Full sentence. What would a team relying only on the Stage 1 opening model
build incorrectly? Name the specific component, assumption, or integration point they would get
wrong, and what would fail as a result.]

`COMMIT-ENTRY`

---

*(Repeat for each additional GATE-CONFIRMED entry. Minimum 2 live entries.)*

`COMMIT-STAGE-4`

---

## Stage 5 — Cluster Map

**ENTER:** `COMMIT-STAGE-4` emitted.

**EXIT:** Stage 4 surprises grouped into named clusters. Each cluster has dimension, surprise IDs,
severity, and a named Next Team / Skill. `COMMIT-STAGE-5` emitted.

| Cluster | Dimension | Surprise IDs | Severity | Next Team / Skill |
|---------|-----------|-------------|----------|-------------------|
| | | | High / Med / Low | |

*Next Team / Skill must name a specific skill (e.g., `/review-design`) or role (e.g.,
"schema owner"). "Investigate" or "follow up" alone are not sufficient.*

`COMMIT-STAGE-5`

---

## Stage 6 — Symmetric Contract Closure

**ENTER:** `COMMIT-STAGE-5` emitted.

**EXIT:** Foreknowledge status declared (CLEAR or FLAGGED). Verdict issued for every B-##
belief (COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED) with revision direction. Closing
statement written. `COMMIT-STAGE-6` emitted.

**Foreknowledge Status:** `CLEAR` or `FLAGGED` (if FLAGGED, name the artifact(s) and
belief(s) responsible)

| Belief | Original Statement | Revision Direction | Verdict |
|--------|-------------------|--------------------|---------|
| B-01 | | Strengthened / Weakened / Reversed / Unchanged | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED |
| B-02 | | | |
| B-03 | | | |

**Closing Statement** *(one paragraph — required)*:
> [What does the team now believe about `{topic}` that it did not believe before? Name the most
> consequential revision to the design direction.]

`COMMIT-STAGE-6`

---

## Stage 7 — Artifact

**ENTER:** `COMMIT-STAGE-6` emitted.

Write to `simulations/{topic}/{topic}-echo-{date}.md`.

Sections in order:
1. Opening Model + Belief Inventory (Stage 1)
2. Surprise entries ranked by severity (Stage 4 — include all five fields, including Build Risk)
3. Cluster Map (Stage 5)
4. Closing synthesis + Verdict Table (Stage 6)
```

---

## Criterion coverage by variation

| Criterion | V-01 | V-02 | V-03 | V-04 | V-05 |
|-----------|:----:|:----:|:----:|:----:|:----:|
| C-01 B-# reference + contradiction | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-02 Symmetric contract (Stage 1 + Stage 6) | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-03 Named artifact in Signal Source | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-04 Specific component in Design Impact | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-05 Five-check gate + GATE-CONFIRMED/REJECTED | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-06 Canonical dimensions only | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-07 Minimum 2 GATE-CONFIRMED | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-08 Named skill/role in Next Team/Skill | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-09 Token protocol integrity | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-10 Foreknowledge CLEAR/FLAGGED in Stage 6 | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-11 Stage 4 prose blocks (not table) | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-12 Full phrases in all Stage 4 fields | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-13 Closed-list vocabulary rule | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-14 Foreknowledge dual-token gate | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-15 Gate sequence overview at top | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-16 Worked calibration example | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-17 Named synonym exclusions | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-18 Synonym-to-canonical mapping table | ✓ | ✓ | ✓ | ✓ | ✓ |
| C-19 Per-stage ENTER/EXIT contracts | — | — | — | — | ✓ |
| C-20 Calibration embedded as Surprise 0 | ✓ | — | — | ✓ | ✓ |
| C-21 EXIT gate self-repair instruction | — | ✓ | — | ✓ | ✓ |
| **Predicted composite** | **145** | **145** | **140** | **150** | **155** |

**C-22 candidate (V-03, V-05):** Build Risk field present in all Stage 4 entries — each entry
names the specific component a next team would build incorrectly by following the Stage 1 opening
model. If scoring shows Build Risk entries produce distinctively stronger C-01 and C-04 output
than entries without it, the field is a v7 criterion candidate.

**Key differentials to watch in scoring:**

- **V-01 vs V-02 (both 145 predicted):** If V-01 scores higher on C-03 and C-04, Surprise 0
  pulls artifact reference quality up at production time. If V-02 scores higher on C-06, EXIT
  self-repair cleans up vocabulary drift that Surprise 0 doesn't prevent.
- **V-04 vs V-01/V-02:** The 5-point gap should appear on C-20+C-21 jointly. If V-04 scores no
  higher on C-03/C-04/C-06 than V-01, the mechanisms don't compound.
- **V-05 vs V-04:** The 5-point gap is C-19. If V-05 ENTER/EXIT contracts produce no detectable
  output quality improvement over V-04, C-19 may already be fully satisfied by the gate overview
  table (C-15) and token emission structure.
- **V-03 Build Risk:** Watch C-01 specifically. If V-03 entries more reliably satisfy "at least
  one entry contradicts the opening model" than V-01/V-04/V-05, the Build Risk field is making
  the contradiction structurally unavoidable rather than hoping the model remembers to include it.
```

---

**Variations written.** Five complete prompt bodies across the five axes:

| | Axis | Key mechanism |
|--|------|--------------|
| **V-01** | C-20 isolation | Surprise 0 inside Stage 4 sequence — entry-zero calibration |
| **V-02** | C-21 isolation | Stage 4 EXIT gate prescribes self-repair via mapping table |
| **V-03** | Inertia framing | Build Risk field — names what the opening model would cause teams to build wrong |
| **V-04** | C-20 + C-21 compound | Surprise 0 at entry production + EXIT audit before COMMIT-STAGE-4 |
| **V-05** | Maximum coverage | C-19 + C-20 + C-21 + Build Risk + full ENTER/EXIT lifecycle |

The decisive scoring question: does V-03's Build Risk field produce a C-22 signal, or does it add noise without improving essential criterion pass rates? That answer determines whether v7 adds a sixth Stage 4 field.
