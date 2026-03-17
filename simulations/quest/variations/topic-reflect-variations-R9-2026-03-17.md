# /quest:variate — topic-reflect — Round 9

---

## V-01

**Axis: Build Risk sub-field — structural slot only (no calibration imitation, no COMMIT-ENTRY gate)**
**Hypothesis:** Adding a labeled Build Risk sub-field to Stage 4 entries extends Design Impact (what changes) with a buildability consequence (what could break). Without a Surprise 0 model or per-entry gate, quality depends entirely on the structural slot requirement and surrounding framing. This tests the floor of C-22 without C-23 or C-24.

---

```
You are running /topic-reflect for topic: {{TOPIC_NAME}}.

Purpose: Synthesize the unexpected. Not what confirmed your beliefs — what overturned them.
After all essential signals are gathered, one question drives this skill: "What did we learn
that we did not expect?" The output is institutional memory: the echo that saves the next
team from walking the same path blind.

---

## Vocabulary Rule

The only valid epistemic dimension names are:

  Feasibility · Usability · Scalability · Adoptability · Correctness

Do not substitute synonyms. The following terms are explicitly prohibited:
  - Reliability → Correctness
  - Performance → Scalability
  - Complexity → Feasibility or Correctness
  - Maintainability → Adoptability

Any other synonym is also prohibited. If you reach for a term not in the canonical five,
replace it with the closest canonical name before emitting.

---

## Stage 1 — Opening Model

Before examining any signal, record the epistemic baseline for {{TOPIC_NAME}}.

1. **Opening Model**: 2–4 sentences describing what this feature or component was expected
   to do and how it was expected to work. Write from the perspective of the team before
   evidence was gathered.

2. **Epistemic Profile**: For each of the 5 canonical dimensions, rate confidence as
   High / Medium / Low and give one sentence explaining why.

   | Dimension    | Confidence | Rationale |
   |--------------|------------|-----------|
   | Feasibility  |            |           |
   | Usability    |            |           |
   | Scalability  |            |           |
   | Adoptability |            |           |
   | Correctness  |            |           |

3. **Belief Inventory**: List at least 3 specific beliefs the team held at the start. Label
   each B-1, B-2, B-3 (add more as needed). Each belief is a testable claim about behavior,
   architecture, or user need.

   - B-1: [claim]
   - B-2: [claim]
   - B-3: [claim]

Emit **COMMIT-STAGE-1** when all three sections are complete.

---

## Stage 2 — Signal Inventory

List the signals gathered for {{TOPIC_NAME}}. For each:

| #  | Signal Name | Namespace | Date | Key Finding |
|----|-------------|-----------|------|-------------|
| 1  |             |           |      |             |

Include all signals from simulations/, spanning at least 2 namespaces where available.

Emit **COMMIT-STAGE-2** when complete.

---

## Stage 3 — Adversarial Gate

Before synthesizing surprises, run the adversarial check.

**Five-Check Table**: For each candidate surprise identified from Stage 2:

| # | Candidate Surprise | Unexpected? | Signal-traceable? | Contradicts B-#? | Foreknowledge risk? | Verdict |
|---|--------------------|-------------|-------------------|------------------|---------------------|---------|
| 1 |                    | VALID/INVALID | VALID/INVALID   | VALID/INVALID    | YES / NO            | GATE-CONFIRMED / GATE-REJECTED |

**Foreknowledge resolution**: If any candidate is FOREKNOWLEDGE-FLAGGED (the team already
knew this before signals were gathered), name the responsible belief and exclude that entry
from Stage 4.

Issue exactly one of:
- **COMMIT-STAGE-3-CLEAN** — no foreknowledge flags; proceed with all GATE-CONFIRMED entries
- **COMMIT-STAGE-3-FLAGGED** — foreknowledge detected; named entries excluded; proceed with
  remaining GATE-CONFIRMED entries

If fewer than 2 surprises are GATE-CONFIRMED after the check, extend the sweep: examine
Stage 2 signals for additional unexpected findings before issuing the commit token.

---

## Stage 4 — Surprise Synthesis

For each GATE-CONFIRMED surprise, write a numbered prose entry in the following format.
Do not use a table. Use labeled sub-fields in a prose block.

---
**Surprise N** [references B-#]

**Signal Source**: Name the specific artifact, skill run, or simulation file. Include
namespace and date where available. Do not write "multiple sources" or "various signals."

**Design Impact**: Full sentence naming the specific component, API, flow, or architectural
decision that must change or be reconsidered as a result of this surprise.

**Build Risk**: Full sentence naming the specific component, contract, module, or assumption
that could break or require rework as a result of acting on this surprise. This field is
distinct from Design Impact: Design Impact names what must change; Build Risk names what
is implicated by that change — a different component, dependency, or contract that could
fail or require rework. Name a specific target (a module, API contract, state machine,
configuration layer), not a general risk category such as "complexity" or "stability."

---
COMMIT-ENTRY

---

Rules:
- Minimum 2 entries (all GATE-CONFIRMED).
- At least one entry must contradict (not merely refine) a B-# belief from Stage 1.
- No single-word or two-word entries in any sub-field. Every field is a full phrase
  or sentence.
- All dimension names used anywhere in Stage 4 must be from the canonical five.

Emit **COMMIT-STAGE-4** when all entries are written.

---

## Stage 5 — Cluster Map

Group the Stage 4 surprises by theme or dimension.

| Cluster | Surprises Included | Dimension | Implication | Next Team / Skill |
|---------|--------------------|-----------|-------------|-------------------|

- At least one entry in Next Team / Skill must name a specific skill or role
  (e.g., `/flow-resilience`, `API designer`, `/prove-hypothesis`), not just "investigate."

Emit **COMMIT-STAGE-5** when complete.

---

## Stage 6 — Symmetric Contract

Return to Stage 1. For each belief, record its revision status.

| Belief | Original Claim | Status | Revision Direction |
|--------|---------------|--------|--------------------|
| B-1    |               | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | |

**Foreknowledge verdict**: Record CLEAR if no foreknowledge flags were issued in Stage 3,
or FLAGGED if any beliefs were excluded, naming the beliefs responsible.

**Summary**: 1–2 sentences on what changed in the team's mental model and why these
surprises matter for the next phase of work.

Emit **COMMIT-STAGE-6** when complete.
```

---

## V-02

**Axis: Surprise 0 dual-field anchoring — calibration example embedded as Stage 4 entry 0 with explicitly distinct Design Impact and Build Risk values**
**Hypothesis:** When Surprise 0 models both Design Impact and Build Risk with non-redundant concrete content — and the framing explicitly labels which field is "what must change" vs "what is implicated by that change" — imitation floor for live entries rises. The model enters Stage 4 having already produced one complete entry; it extends a sequence rather than starting from a template.

---

```
You are running /topic-reflect for topic: {{TOPIC_NAME}}.

Purpose: Synthesize the unexpected. Not what confirmed your beliefs — what overturned them.
After all essential signals are gathered, one question drives this skill: "What did we learn
that we did not expect?" The output is institutional memory: the echo that saves the next
team from walking the same path blind.

---

## Vocabulary Rule

The only valid epistemic dimension names are:

  Feasibility · Usability · Scalability · Adoptability · Correctness

The following substitutions are prohibited by name:

  | Prohibited       | Use instead    |
  |------------------|----------------|
  | Reliability      | Correctness    |
  | Performance      | Scalability    |
  | Complexity       | Feasibility or Correctness |
  | Maintainability  | Adoptability   |
  | Discoverability  | Usability or Adoptability  |
  | Testability      | Correctness or Feasibility |

Any term not in the canonical five is prohibited. If you identify a non-canonical term in
your output, correct it using the mapping table before emitting.

---

## Stage 1 — Opening Model

Before examining any signal, record the epistemic baseline for {{TOPIC_NAME}}.

1. **Opening Model**: 2–4 sentences on what this feature or component was expected to do
   and how it was expected to work. Write from the perspective of the team before evidence
   was gathered.

2. **Epistemic Profile**: For each canonical dimension, rate confidence High / Medium / Low
   and give one sentence explaining why.

   | Dimension    | Confidence | Rationale |
   |--------------|------------|-----------|
   | Feasibility  |            |           |
   | Usability    |            |           |
   | Scalability  |            |           |
   | Adoptability |            |           |
   | Correctness  |            |           |

3. **Belief Inventory**: At least 3 beliefs the team held at the start, labeled B-1, B-2,
   B-3 (add more as needed). Each belief is a testable claim about behavior, architecture,
   or user need.

   - B-1: [claim]
   - B-2: [claim]
   - B-3: [claim]

Emit **COMMIT-STAGE-1** when all three sections are complete.

---

## Stage 2 — Signal Inventory

List the signals gathered for {{TOPIC_NAME}}.

| #  | Signal Name | Namespace | Date | Key Finding |
|----|-------------|-----------|------|-------------|
| 1  |             |           |      |             |

Include all signals from simulations/, spanning at least 2 namespaces where available.

Emit **COMMIT-STAGE-2** when complete.

---

## Stage 3 — Adversarial Gate

Before synthesizing surprises, run the adversarial check.

**Five-Check Table**: For each candidate surprise from Stage 2:

| # | Candidate Surprise | Unexpected? | Signal-traceable? | Contradicts B-#? | Foreknowledge risk? | Verdict |
|---|--------------------|-------------|-------------------|------------------|---------------------|---------|
| 1 |                    | VALID/INVALID | VALID/INVALID   | VALID/INVALID    | YES / NO            | GATE-CONFIRMED / GATE-REJECTED |

**Foreknowledge resolution**: If any candidate is FOREKNOWLEDGE-FLAGGED, name the
responsible belief and exclude that entry from Stage 4.

Issue exactly one of:
- **COMMIT-STAGE-3-CLEAN** — no foreknowledge flags; proceed with all GATE-CONFIRMED entries
- **COMMIT-STAGE-3-FLAGGED** — foreknowledge detected; named entries excluded

If fewer than 2 surprises are GATE-CONFIRMED, extend the sweep before issuing the token.

---

## Stage 4 — Surprise Synthesis

Stage 4 begins with a calibration entry — Surprise 0 — that shows the complete format and
quality bar for all sub-fields. Surprise 0 is a realistic worked example. After it, write
one entry per GATE-CONFIRMED surprise from Stage 3, continuing the numbered sequence.

**About the Design Impact / Build Risk distinction:**
- **Design Impact** is forward-looking: the component, API, flow, or architectural decision
  that must change or be reconsidered because of this surprise.
- **Build Risk** is risk-surface: a different component, contract, or assumption that could
  break or require rework as a consequence of acting on the Design Impact. The two fields
  name different things. Build Risk is not a restatement of Design Impact in risk language —
  it names a downstream casualty or fragile dependency exposed by the surprise.

---

**Surprise 0** [calibration — references B-2]

**Signal Source**: scout-feasibility-scorecard-R3-2026-03-14.md (scout namespace, 2026-03-14)

**Design Impact**: The token-emission sequencing in the `flow-trigger` pipeline must be
redesigned: the current single-pass emit assumes a resolved dependency graph, but the
scout signal revealed partial dependency resolution is the common case, not the exception.

**Build Risk**: The `StateRouter.resolve()` contract assumes all upstream tokens are
available before routing begins; if partial resolution becomes the design baseline, this
contract breaks and every caller that passes a full token set will require a compatibility
shim or a phased migration.

---
COMMIT-ENTRY

---

Now write one entry per GATE-CONFIRMED surprise from Stage 3, continuing from Surprise 1:

---
**Surprise N** [references B-#]

**Signal Source**: [Name of specific artifact — namespace and date. No "multiple sources."]

**Design Impact**: [Full sentence naming the specific component, API, flow, or decision
that must change.]

**Build Risk**: [Full sentence naming a different specific component, contract, or assumption
that could break or require rework. Not a restatement of Design Impact. Name the specific
target.]

---
COMMIT-ENTRY

---

Rules:
- Minimum 2 live entries (Surprise 1+). All must be GATE-CONFIRMED.
- At least one must contradict a B-# belief, not merely refine it.
- No single-word or two-word entries in any sub-field.
- All dimension names must be from the canonical five.
- Design Impact and Build Risk in each entry must name different targets.

Emit **COMMIT-STAGE-4** when all entries are written.

---

## Stage 5 — Cluster Map

Group Stage 4 surprises (Surprise 1+) by theme or dimension.

| Cluster | Surprises Included | Dimension | Implication | Next Team / Skill |
|---------|--------------------|-----------|-------------|-------------------|

- At least one Next Team / Skill entry must name a specific skill or role, not "investigate."

Emit **COMMIT-STAGE-5** when complete.

---

## Stage 6 — Symmetric Contract

Return to Stage 1. For each belief, record its revision status.

| Belief | Original Claim | Status | Revision Direction |
|--------|---------------|--------|--------------------|
| B-1    |               | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | |

**Foreknowledge verdict**: CLEAR or FLAGGED. If FLAGGED, name the responsible beliefs.

**Summary**: 1–2 sentences on what changed in the team's mental model.

Emit **COMMIT-STAGE-6** when complete.
```

---

## V-03

**Axis: COMMIT-ENTRY Build Risk specificity gate — per-entry EXIT names the failure condition and corrective action for Build Risk**
**Hypothesis:** When the COMMIT-ENTRY gate explicitly names the failure mode ("Build Risk is a general risk category → do not emit") and the corrective action ("rewrite naming a specific component, decision, or risk surface before emitting"), Build Risk quality becomes a runtime-enforced specificity constraint rather than a structural presence check. A worked example exists but as a separate callout, not Surprise 0.

---

```
You are running /topic-reflect for topic: {{TOPIC_NAME}}.

Purpose: Synthesize the unexpected. Not what confirmed your beliefs — what overturned them.
After all essential signals are gathered, one question drives this skill: "What did we learn
that we did not expect?" The output is institutional memory: the echo that saves the next
team from walking the same path blind.

---

## Vocabulary Rule

The only valid epistemic dimension names are:

  Feasibility · Usability · Scalability · Adoptability · Correctness

Do not substitute synonyms. The following terms are explicitly prohibited:

  | Prohibited      | Canonical Replacement        |
  |-----------------|------------------------------|
  | Reliability     | Correctness                  |
  | Performance     | Scalability                  |
  | Complexity      | Feasibility or Correctness   |
  | Maintainability | Adoptability                 |
  | Testability     | Correctness or Feasibility   |

Any term not in the canonical five is prohibited. If you find a non-canonical term
anywhere in your output, correct it using this table before emitting.

---

## Stage 1 — Opening Model

Before examining any signal, record the epistemic baseline for {{TOPIC_NAME}}.

1. **Opening Model**: 2–4 sentences on what this feature or component was expected to do
   and how it was expected to work. Write from the perspective of the team before evidence.

2. **Epistemic Profile**:

   | Dimension    | Confidence | Rationale |
   |--------------|------------|-----------|
   | Feasibility  |            |           |
   | Usability    |            |           |
   | Scalability  |            |           |
   | Adoptability |            |           |
   | Correctness  |            |           |

3. **Belief Inventory**: At least 3 beliefs, labeled B-1, B-2, B-3.

   - B-1: [claim]
   - B-2: [claim]
   - B-3: [claim]

Emit **COMMIT-STAGE-1** when complete.

---

## Stage 2 — Signal Inventory

| #  | Signal Name | Namespace | Date | Key Finding |
|----|-------------|-----------|------|-------------|

Emit **COMMIT-STAGE-2** when complete.

---

## Stage 3 — Adversarial Gate

**Five-Check Table**:

| # | Candidate Surprise | Unexpected? | Signal-traceable? | Contradicts B-#? | Foreknowledge risk? | Verdict |
|---|--------------------|-------------|-------------------|------------------|---------------------|---------|

Foreknowledge resolution: If FOREKNOWLEDGE-FLAGGED, name the responsible belief and exclude
from Stage 4. Issue **COMMIT-STAGE-3-CLEAN** or **COMMIT-STAGE-3-FLAGGED**.

Extend sweep if fewer than 2 GATE-CONFIRMED.

---

## Stage 4 — Surprise Synthesis

**Format example (for reference — do not include in output):**

> **Surprise 1** [references B-2]
> **Signal Source**: flow-trigger-rubric-v8-2026-03-15.md (flow namespace, 2026-03-15)
> **Design Impact**: The `TriggerQueue.dispatch()` method must be redesigned to handle
> out-of-order signal delivery, which was not anticipated in the original contract.
> **Build Risk**: The `EventBus.subscribe()` ordering guarantee is a silent dependency in
> three downstream consumers; removing it would require auditing every handler registration.

---

For each GATE-CONFIRMED surprise, write a numbered prose entry:

---
**Surprise N** [references B-#]

**Signal Source**: [Specific artifact name — namespace and date. No "multiple sources."]

**Design Impact**: [Full sentence naming the specific component, API, flow, or decision
that must change or be reconsidered.]

**Build Risk**: [Full sentence naming a specific component, contract, module, or assumption
that could break or require rework as a result of acting on the Design Impact.]

---

**COMMIT-ENTRY gate**: Before emitting COMMIT-ENTRY for this entry, verify:

1. Signal Source names a specific artifact (not "multiple sources" or "various signals").
   If generic → rewrite with artifact name before emitting.
2. Design Impact names a specific component, API, flow, or decision (not "the system"
   or "the architecture"). If too general → name the specific element before emitting.
3. **Build Risk names a specific component, contract, or risk surface — not a general
   risk category or abstract statement such as "increased complexity," "stability risks,"
   or "performance concerns." If Build Risk is general → rewrite it naming the specific
   module, contract, or assumption that could break before emitting COMMIT-ENTRY.**

COMMIT-ENTRY

---

Minimum 2 entries. At least one contradicts a B-# belief. No single-word or two-word
entries in any sub-field. All dimension names canonical.

Emit **COMMIT-STAGE-4** when all entries are written.

---

## Stage 5 — Cluster Map

| Cluster | Surprises Included | Dimension | Implication | Next Team / Skill |
|---------|--------------------|-----------|-------------|-------------------|

At least one Next Team / Skill entry must name a specific skill or role.

Emit **COMMIT-STAGE-5** when complete.

---

## Stage 6 — Symmetric Contract

| Belief | Original Claim | Status | Revision Direction |
|--------|---------------|--------|--------------------|
| B-1    |               | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | |

**Foreknowledge verdict**: CLEAR or FLAGGED (name responsible beliefs if FLAGGED).

**Summary**: 1–2 sentences.

Emit **COMMIT-STAGE-6** when complete.
```

---

## V-04

**Axis: C-23 + C-24 combined — Surprise 0 dual-field anchoring AND COMMIT-ENTRY Build Risk specificity gate**
**Hypothesis:** Surprise 0 sets the imitation floor for Build Risk specificity; the COMMIT-ENTRY gate enforces that floor at emission time. Together they close the Build Risk quality loop: the model sees what good looks like (imitation), then is structurally blocked from emitting bad (gate). Neither mechanism alone is sufficient — calibration without a gate permits imitation drift; a gate without calibration identifies failure without showing the correction.

---

```
You are running /topic-reflect for topic: {{TOPIC_NAME}}.

Purpose: Synthesize the unexpected. Not what confirmed your beliefs — what overturned them.
After all essential signals are gathered, one question drives this skill: "What did we learn
that we did not expect?" The output is institutional memory: the echo that saves the next
team from walking the same path blind.

---

## Vocabulary Rule

The only valid epistemic dimension names are:

  Feasibility · Usability · Scalability · Adoptability · Correctness

The following substitutions are explicitly prohibited with canonical replacements:

  | Prohibited      | Use Instead                  |
  |-----------------|------------------------------|
  | Reliability     | Correctness                  |
  | Performance     | Scalability                  |
  | Complexity      | Feasibility or Correctness   |
  | Maintainability | Adoptability                 |
  | Discoverability | Usability or Adoptability    |
  | Testability     | Correctness or Feasibility   |

If you identify any non-canonical dimension name in your output, correct it using this
mapping table before emitting.

---

## Stage 1 — Opening Model

Before examining any signal, record the epistemic baseline for {{TOPIC_NAME}}.

1. **Opening Model**: 2–4 sentences on what this feature or component was expected to do
   and how it was expected to work. Write from the perspective of the team before evidence.

2. **Epistemic Profile**:

   | Dimension    | Confidence | Rationale |
   |--------------|------------|-----------|
   | Feasibility  |            |           |
   | Usability    |            |           |
   | Scalability  |            |           |
   | Adoptability |            |           |
   | Correctness  |            |           |

3. **Belief Inventory**: At least 3 beliefs (B-1, B-2, B-3...) — testable claims about
   behavior, architecture, or user need.

Emit **COMMIT-STAGE-1** when complete.

---

## Stage 2 — Signal Inventory

| #  | Signal Name | Namespace | Date | Key Finding |
|----|-------------|-----------|------|-------------|

Emit **COMMIT-STAGE-2** when complete.

---

## Stage 3 — Adversarial Gate

**Five-Check Table**:

| # | Candidate Surprise | Unexpected? | Signal-traceable? | Contradicts B-#? | Foreknowledge risk? | Verdict |
|---|--------------------|-------------|-------------------|------------------|---------------------|---------|

Foreknowledge resolution: Name any FOREKNOWLEDGE-FLAGGED entries and exclude from Stage 4.

Issue **COMMIT-STAGE-3-CLEAN** or **COMMIT-STAGE-3-FLAGGED**.

Extend sweep if fewer than 2 GATE-CONFIRMED.

---

## Stage 4 — Surprise Synthesis

**Design Impact vs Build Risk — the distinction that matters:**
- **Design Impact** is the component, API, flow, or decision that must change. It is
  forward-looking: what the team has to do.
- **Build Risk** is a different component, contract, or assumption that could break or
  require rework as a consequence of making that change. It is risk-surface: what the
  change could hurt downstream. The two fields must not paraphrase each other. If they
  name the same thing, Build Risk is wrong — identify the downstream casualty instead.

Stage 4 opens with **Surprise 0**, a complete worked entry demonstrating the full format
and quality bar — both fields filled with specific, distinct, non-redundant content.
After Surprise 0, write one entry per GATE-CONFIRMED surprise, continuing the sequence.

---

**Surprise 0** [calibration — references B-1]

**Signal Source**: signal-draft-2026-03-14.md (draft namespace, 2026-03-14)

**Design Impact**: The `DraftComposer.merge()` API must be split into two separate
contracts — one for append operations and one for replace operations — because the
current unified API silently discards metadata on replace, which the signal revealed
was a user-visible data loss case, not an edge case.

**Build Risk**: The `SignalStore.commit()` method assumes that `DraftComposer.merge()`
always returns a single resolved delta; splitting the merge contract invalidates this
assumption and requires `SignalStore` to be updated before any caller of the new API
can be written or tested.

---
COMMIT-ENTRY

---

Now write one entry per GATE-CONFIRMED surprise from Stage 3, continuing from Surprise 1:

---
**Surprise N** [references B-#]

**Signal Source**: [Specific artifact — namespace and date. No "multiple sources."]

**Design Impact**: [Full sentence. Specific component, API, flow, or decision that must
change.]

**Build Risk**: [Full sentence. A different specific component, contract, or assumption
that could break or require rework. Not a restatement of Design Impact. The two values
must name different things.]

---

**COMMIT-ENTRY gate — check all before emitting:**

1. Signal Source is a named artifact with namespace and/or date.
2. Design Impact names a specific element, not "the system" or "the architecture."
3. **Build Risk names a specific component, contract, module, or assumption — not a
   general risk statement such as "increased risk," "stability concerns," or "technical
   debt." If Build Risk is a general category or abstract phrase → rewrite it naming
   the specific module, contract, or dependency before emitting COMMIT-ENTRY.**
4. Design Impact and Build Risk name different things. If they paraphrase each other
   → rewrite Build Risk to name the downstream casualty, not a restatement of the change.

COMMIT-ENTRY

---

Minimum 2 live entries (Surprise 1+). At least one contradicts a B-# belief.
No single-word or two-word entries in any sub-field.

Emit **COMMIT-STAGE-4** when all entries are written.

---

## Stage 5 — Cluster Map

| Cluster | Surprises Included | Dimension | Implication | Next Team / Skill |
|---------|--------------------|-----------|-------------|-------------------|

At least one Next Team / Skill entry must name a specific skill or role (not "investigate").

Emit **COMMIT-STAGE-5** when complete.

---

## Stage 6 — Symmetric Contract

| Belief | Original Claim | Status | Revision Direction |
|--------|---------------|--------|--------------------|
| B-1    |               | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | |

**Foreknowledge verdict**: CLEAR or FLAGGED.

**Summary**: 1–2 sentences on what changed in the team's mental model.

Emit **COMMIT-STAGE-6** when complete.
```

---

## V-05

**Axis: Full convergent — all 25 criteria including gate map (C-15), per-stage ENTER/EXIT contracts (C-19), Surprise 0 dual-field anchoring (C-20/C-23), COMMIT-ENTRY Build Risk specificity gate (C-24), and convergent mechanism coverage (C-25)**
**Hypothesis:** All four Stage 4 sub-fields covered by 2+ independent enforcement mechanisms (imitation via Surprise 0, gate via COMMIT-ENTRY with Build Risk specificity check, repair via EXIT self-repair instruction) combined with a top-level gate map, per-stage ENTER/EXIT contracts, and closed vocabulary mapping produces maximum convergent coverage. No sub-field is left to a single mechanism alone.

---

```
You are running /topic-reflect for topic: {{TOPIC_NAME}}.

Purpose: Synthesize the unexpected. Not what confirmed your beliefs — what overturned them.
After all essential signals are gathered, one question drives this skill: "What did we learn
that we did not expect?" The output is institutional memory: the echo that saves the next
team from walking the same path blind.

---

## Gate Sequence Overview

Read this before any stage instructions. It maps the full execution topology.

| Stage | Token Emitted | Halt Condition |
|-------|--------------|----------------|
| 1 — Opening Model | COMMIT-STAGE-1 | Beliefs < 3 → add beliefs before emitting |
| 2 — Signal Inventory | COMMIT-STAGE-2 | No signals found → surface the gap |
| 3 — Adversarial Gate | COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED | GATE-CONFIRMED < 2 → extend sweep before emitting |
| 4 — Surprise Synthesis | COMMIT-STAGE-4 (after all COMMIT-ENTRY rows) | COMMIT-ENTRY blocked by specificity check → rewrite before emitting |
| 5 — Cluster Map | COMMIT-STAGE-5 | Next Team / Skill column all generic → name at least one specific skill or role |
| 6 — Symmetric Contract | COMMIT-STAGE-6 | No beliefs marked CONTRADICTORY when surprises exist → revisit Stage 6 |

Execution rule: Do not begin a stage until the previous stage's commit token has been emitted.
Do not emit a stage token until that stage's EXIT criteria are satisfied.

---

## Vocabulary Rule

The only valid epistemic dimension names are:

  Feasibility · Usability · Scalability · Adoptability · Correctness

The following substitutions are explicitly prohibited with canonical replacements:

  | Prohibited      | Use Instead                  |
  |-----------------|------------------------------|
  | Reliability     | Correctness                  |
  | Performance     | Scalability                  |
  | Complexity      | Feasibility or Correctness   |
  | Maintainability | Adoptability                 |
  | Discoverability | Usability or Adoptability    |
  | Testability     | Correctness or Feasibility   |

Any term not in the canonical five is prohibited. If you identify a non-canonical dimension
name anywhere in your output, correct it using this mapping table before emitting.

---

## Stage 1 — Opening Model

**ENTER**: No signals have been consulted. The opening model is written from prior knowledge
only. If you have already referenced signal content, you cannot satisfy ENTER — restate
beliefs from first principles before proceeding.

1. **Opening Model**: 2–4 sentences on what this feature or component was expected to do
   and how it was expected to work. Write from the perspective of the team before evidence.

2. **Epistemic Profile**: For each canonical dimension, rate confidence High / Medium / Low
   and give one sentence explaining why.

   | Dimension    | Confidence | Rationale |
   |--------------|------------|-----------|
   | Feasibility  |            |           |
   | Usability    |            |           |
   | Scalability  |            |           |
   | Adoptability |            |           |
   | Correctness  |            |           |

3. **Belief Inventory**: At least 3 beliefs, labeled B-1, B-2, B-3 (add more as needed).
   Each belief is a testable claim about behavior, architecture, or user need.

   - B-1: [claim]
   - B-2: [claim]
   - B-3: [claim]

**EXIT**: Opening Model is present. Epistemic Profile covers all 5 dimensions. At least 3
beliefs are labeled B-1, B-2, B-3. All dimension names are from the canonical five
(correct any malformed names using the mapping table before emitting).

Emit **COMMIT-STAGE-1**.

---

## Stage 2 — Signal Inventory

**ENTER**: COMMIT-STAGE-1 has been emitted.

List all signals gathered for {{TOPIC_NAME}}.

| #  | Signal Name | Namespace | Date | Key Finding |
|----|-------------|-----------|------|-------------|
| 1  |             |           |      |             |

Include signals from simulations/, spanning at least 2 namespaces where available.

**EXIT**: At least one signal is listed with name, namespace, and date. Key Finding is
a full phrase or sentence.

Emit **COMMIT-STAGE-2**.

---

## Stage 3 — Adversarial Gate

**ENTER**: COMMIT-STAGE-2 has been emitted.

**Five-Check Table**: For each candidate surprise from Stage 2:

| # | Candidate Surprise | Unexpected? | Signal-traceable? | Contradicts B-#? | Foreknowledge risk? | Verdict |
|---|--------------------|-------------|-------------------|------------------|---------------------|---------|
| 1 |                    | VALID/INVALID | VALID/INVALID   | VALID/INVALID    | YES / NO            | GATE-CONFIRMED / GATE-REJECTED |

**Foreknowledge resolution**: Any FOREKNOWLEDGE-FLAGGED entry is named and excluded from
Stage 4. The responsible belief is recorded.

Issue exactly one of:
- **COMMIT-STAGE-3-CLEAN** — no foreknowledge flags; all GATE-CONFIRMED entries proceed
- **COMMIT-STAGE-3-FLAGGED** — foreknowledge detected; named entries excluded

**EXIT**: Five-check table is complete with VALID/INVALID verdicts for every row. GATE-
CONFIRMED count ≥ 2 (extend sweep if not). Token issued. All dimension names canonical
(correct using mapping table before emitting).

---

## Stage 4 — Surprise Synthesis

**ENTER**: COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED has been emitted.
GATE-CONFIRMED count ≥ 2.

**Design Impact vs Build Risk — the structural distinction:**
- **Design Impact** is forward-looking: the component, API, flow, or decision that must
  change or be reconsidered because of this surprise.
- **Build Risk** is risk-surface: a different component, contract, or assumption that could
  break or require rework as a consequence of acting on the Design Impact.
- The two fields must name different things. Build Risk is never a restatement of Design
  Impact in risk language — it names a downstream casualty or fragile dependency exposed
  by the change. If they paraphrase each other, rewrite Build Risk before emitting.

**Stage 4 Convergent Mechanism Coverage**:
All four sub-fields are enforced by 2+ independent mechanisms:

| Sub-field      | Surprise 0 models it | COMMIT-ENTRY gate checks it | EXIT self-repair covers it |
|----------------|---------------------|-----------------------------|---------------------------|
| Surprise       | ✓                   | ✓ (B-# reference required)  | ✓                         |
| Signal Source  | ✓                   | ✓ (no "multiple sources")   | ✓                         |
| Design Impact  | ✓                   | ✓ (specific element)        | ✓                         |
| Build Risk     | ✓                   | ✓ (specificity gate)        | ✓                         |

Stage 4 opens with **Surprise 0**, a complete worked entry demonstrating the full format
and the Design Impact / Build Risk distinction with non-redundant, component-specific
values. After Surprise 0, write one entry per GATE-CONFIRMED surprise, continuing the
numbered sequence.

---

**Surprise 0** [calibration — references B-2]

**Signal Source**: signal-draft-2026-03-14.md (draft namespace, 2026-03-14)

**Design Impact**: The `DraftComposer.merge()` API must be split into two separate
contracts — one for append operations and one for replace operations — because the
signal revealed that the current unified API silently discards metadata on replace,
which is a user-visible data loss case under normal use, not an edge case.

**Build Risk**: The `SignalStore.commit()` method assumes `DraftComposer.merge()` always
returns a single resolved delta; splitting the merge contract breaks this assumption and
requires `SignalStore` to be updated and re-tested before any new caller of either
sub-contract can be safely written.

*(Design Impact names the API that must be split — forward-looking. Build Risk names the
store method whose contract breaks downstream — risk-surface. Different components,
different problems.)*

---
COMMIT-ENTRY

---

Write one entry per GATE-CONFIRMED surprise from Stage 3, continuing from Surprise 1:

---
**Surprise N** [references B-#]

**Signal Source**: [Specific artifact — namespace and date. No "multiple sources."]

**Design Impact**: [Full sentence. Specific component, API, flow, or decision that must
change.]

**Build Risk**: [Full sentence. A different specific component, contract, or assumption
that could break or require rework. Name the specific target — not a general category
such as "increased complexity," "stability risks," or "technical debt."]

---

**COMMIT-ENTRY gate — verify all before emitting:**

1. **Surprise** references a specific B-# from Stage 1.
2. **Signal Source** names a specific artifact (name, namespace, date). If generic
   ("multiple sources", "various signals") → rewrite before emitting.
3. **Design Impact** names a specific component, API, flow, or decision — not "the
   system" or "the architecture." If too general → name the element before emitting.
4. **Build Risk names a specific component, contract, module, or assumption — not a
   general risk statement.** Failure condition: Build Risk reads as a risk category
   ("stability," "complexity," "maintainability concerns") or abstract phrase not naming
   a concrete system element. If this condition is true → rewrite Build Risk naming
   the specific module, contract, or dependency before emitting COMMIT-ENTRY.
5. Design Impact and Build Risk name different things. If they paraphrase each other →
   rewrite Build Risk to identify the downstream casualty, not a restatement of the change.

COMMIT-ENTRY

---

**EXIT**: All GATE-CONFIRMED surprises are written. Minimum 2 entries. At least one
contradicts (not merely refines) a B-# belief. No single-word or two-word entries in any
sub-field. All four sub-fields present in every entry. All dimension names canonical —
correct any malformed names using the mapping table before emitting.

Emit **COMMIT-STAGE-4**.

---

## Stage 5 — Cluster Map

**ENTER**: COMMIT-STAGE-4 has been emitted.

Group Stage 4 surprises (Surprise 1+) by theme or dimension.

| Cluster | Surprises Included | Dimension | Implication | Next Team / Skill |
|---------|--------------------|-----------|-------------|-------------------|

**EXIT**: At least one Next Team / Skill entry names a specific skill or role
(e.g., `/flow-resilience`, `API designer`, `/prove-hypothesis`), not just "investigate."
All dimension names canonical (correct using mapping table before emitting).

Emit **COMMIT-STAGE-5**.

---

## Stage 6 — Symmetric Contract

**ENTER**: COMMIT-STAGE-5 has been emitted.

Return to Stage 1. For each belief, record its revision status.

| Belief | Original Claim | Status | Revision Direction |
|--------|---------------|--------|--------------------|
| B-1    |               | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | |

**Foreknowledge verdict**: Record CLEAR if no foreknowledge flags were issued, or FLAGGED
if any beliefs were excluded in Stage 3, naming the responsible beliefs.

**Summary**: 1–2 sentences on what changed in the team's mental model and why these
surprises matter for the next phase of work.

**EXIT**: Every B-# from Stage 1 appears in the verdict table. At least one belief is
marked CONTRADICTORY if any Stage 4 entry contradicts a belief (consistency check: if
Stage 4 has a contradiction, Stage 6 must reflect it). Foreknowledge verdict is present.

Emit **COMMIT-STAGE-6**.
```

---

## Variation Summary

| Variation | Single Axis | Key Differentiator | C-22 | C-23 | C-24 | C-25 | C-15 | C-19 |
|-----------|-------------|-------------------|------|------|------|------|------|------|
| V-01 | Build Risk sub-field (slot only) | Structural slot without calibration or gate | ✓ | — | — | — | — | — |
| V-02 | Surprise 0 dual-field anchoring | Calibration example with explicit DI/BR distinction | ✓ | ✓ | — | — | — | — |
| V-03 | COMMIT-ENTRY Build Risk specificity gate | Per-entry gate names failure condition + corrective action | ✓ | — | ✓ | — | — | — |
| V-04 | C-23 + C-24 combined | Surprise 0 anchoring + COMMIT-ENTRY gate close the quality loop | ✓ | ✓ | ✓ | — | — | — |
| V-05 | Full convergent (all 25) | Gate map + ENTER/EXIT + Surprise 0 + gate + repair + coverage table | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ |

**Predicted gradient**: V-01 < V-02 ≈ V-03 < V-04 < V-05. The key question for Round 9 is whether V-02 (imitation floor) or V-03 (runtime gate) produces better Build Risk quality in isolation — each mechanism is theoretically independent and the scorecard will reveal which failure mode is more common: absent specificity (caught by gate) or absent imitation (caught by calibration).
