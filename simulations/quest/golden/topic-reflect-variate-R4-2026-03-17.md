# quest-variate Variations — Round 4 (topic-reflect v4 rubric)
**Skill**: topic-echo (topic-reflect)
**Rubric**: v4-2026-03-17 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-17 aspirational)
**N_essential=5, N_recommended=3, N_aspirational=9**
**Date**: 2026-03-17
**Round**: 4

---

## Context: what informed this round

The v3 rubric produced four perfect 120/120 scores in Round 3 — discrimination exhausted at all 14
prior criteria. Three new aspirational criteria (C-15, C-16, C-17) were extracted from Round 3
excellence signals:

| Criterion | Source variation | What it detected |
|-----------|----------------|-----------------|
| C-15 (pre-stage gate map) | V-03 only | A top-level gate topology table before Stage 1 that lets the model orient to the full execution model before entering stage-by-stage instructions |
| C-16 (worked calibration example) | V-04 only | A filled-in Stage 4 example (not a template) anchoring Signal Source and Design Impact quality against a concrete realistic instance |
| C-17 (named synonym exclusions) | V-01 and V-04 | Prohibited synonym names (Reliability, Performance, Complexity, Maintainability) listed explicitly alongside the general substitution prohibition |

The current T3 baseline (`topic-echo.t3/SKILL.md`) uses different canonical dimension names
(`falsifiability · observability · causal specificity · predictive precision · scope constraints`)
and a table format for Stage 4 entries — both misaligned with the v4 rubric. Round 4 variations
correct both divergences and test whether the three new aspirational mechanisms can be combined
without regression on the 14 established criteria.

**v4 rubric score formula:**
```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 9 * 45)
```

**Golden threshold**: all C-01–C-05 pass AND composite >= 100
**Score landmarks:**
- All essential + all recommended + all 9 aspirational: 135
- All essential + all recommended + 2/9 aspirational: 100 (golden threshold)
- All essential + all recommended + 0 aspirational: 90
- All essential + 0 recommended + 0 aspirational: 60

---

## Variation axis selection

| Axis | Label | Single/Combined | Targets |
|------|-------|----------------|---------|
| A | Phrasing register — formal/technical, imperative | Single | C-17 (named synonym exclusions emerge naturally from rigorous vocabulary enforcement) |
| B | Lifecycle emphasis — explicit ENTER/EXIT conditions per stage | Single | C-01, C-04, C-12 (completeness gates prevent thin fields and premature stage transitions) |
| C | Output format — pre-stage gate sequence map | Single | C-15 (structural navigation before Stage 1) |
| D | A + worked calibration example | Combined | C-17 + C-16 (synonym exclusions + concrete quality anchor at Stage 4 entry) |
| E | C + inertia framing + conversational register | Combined | C-15 + C-01 sharpness (inertia naming makes the CONTRADICTORY verdict more legible in a relaxed register; gate map prevents token confusion the relaxed register might otherwise introduce) |

Base mechanisms in all variations: correct canonical dimension names
(Feasibility · Usability · Scalability · Adoptability · Correctness), Stage 4 as numbered prose
blocks (not tables), COMMIT-STAGE-3-CLEAN / COMMIT-STAGE-3-FLAGGED foreknowledge gate,
GATE-CONFIRMED token naming Stage 4 by name, COMMIT-ENTRY per Stage 4 row.

---

## V-01 — Phrasing Register (Formal/Technical)

**Axis**: A — formal/technical register throughout; imperative directives; named synonym exclusions
in the vocabulary rule.

**Hypothesis**: Formal imperative register eliminates interpretive slack in stage instructions and
prevents vocabulary drift. Naming specific prohibited synonyms (C-17) converts the highest-
probability substitution errors from implicit policy violations to explicit named violations — a
model encountering "do not substitute" may still reach for "Reliability"; a model that has read
"Reliability is prohibited, use Correctness" has no equivalent escape path. Secondary hypothesis:
formal register correlates with longer, more complete field entries (C-12) because the register
signals that terse entries are structurally inappropriate.

---

You are executing `/topic-echo` for topic `{topic}`.

**Function**: Produce the institutional memory artifact for `{topic}`. Answer one question:
**What did this team learn that it did not expect?**

This is not a summary. It is not a confirmation list. It is a synthesis of surprises — findings that
contradicted, revised, or substantially extended the prior model. A finding that confirms a prior
belief is not a surprise. It is excluded.

---

### Vocabulary Declaration

**The only valid epistemic dimension names are:**

> Feasibility · Usability · Scalability · Adoptability · Correctness

The following substitutions are prohibited. Each is named explicitly to close the highest-
probability substitution errors:

| Prohibited term | Canonical substitute |
|----------------|---------------------|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Correctness or Feasibility |
| Maintainability | Adoptability |
| Discoverability | Usability or Adoptability |
| Testability | Correctness or Feasibility |

Any dimension cell containing a term not in the canonical list is malformed. Correct it before
emitting the stage commit token for that stage.

---

### Stage 1 — Opening Model

Do not consult signal artifacts at this stage. Record the epistemic state at investigation onset.

1. **Opening model**: 2–4 sentences. State what the team believed about `{topic}` before signals
   were gathered. Name the specific assumptions that signals could contradict.

2. **Epistemic profile**: One row per canonical dimension, populated from the closed list only:

| Dimension | Prior Belief | Confidence |
|-----------|-------------|------------|
| Feasibility | | HIGH / MEDIUM / LOW |
| Usability | | HIGH / MEDIUM / LOW |
| Scalability | | HIGH / MEDIUM / LOW |
| Adoptability | | HIGH / MEDIUM / LOW |
| Correctness | | HIGH / MEDIUM / LOW |

3. **Belief inventory**: Minimum 3 falsifiable beliefs, numbered B-1 through B-N. Each belief is a
   flat statement about `{topic}` that a signal artifact could contradict.

`COMMIT-STAGE-1`

---

### Stage 2 — Signal Inventory

Consult all signal artifacts for `{topic}`. For each artifact:

| Artifact | Namespace | Date | Primary Finding (1 sentence) |
|----------|-----------|------|------------------------------|
| | | | |

`COMMIT-STAGE-2`

---

### Stage 3 — Adversarial Gate

For each candidate surprise, execute the five-check table. A candidate is a Stage 2 deviation that
appears to contradict or substantially extend a Stage 1 belief.

| Check | Test | Verdict |
|-------|------|---------|
| FC-1 | Absent from all B-# beliefs? | VALID / INVALID |
| FC-2 | Contradicts (not confirms) the opening model? | VALID / INVALID |
| FC-3 | Not predictable from domain knowledge alone? | VALID / INVALID |
| FC-4 | Source artifact specifically named (name, namespace, date)? | VALID / INVALID |
| FC-5 | Design impact non-trivial? | VALID / INVALID |

For each candidate passing all checks, emit the confirmation token naming the destination stage:

`GATE-CONFIRMED-[N]: VALID — Stage 4.`

For each failing candidate:

`GATE-REJECTED-[N]: INVALID — Check [#]: [reason].`

Foreknowledge resolution — after evaluating all candidates:
- No findings anticipated by Stage 1 beliefs: `COMMIT-STAGE-3-CLEAN`
- Any finding anticipated by Stage 1 beliefs: `COMMIT-STAGE-3-FLAGGED — [B-#] anticipated [finding].`

Halt condition: if GATE-CONFIRMED count < 2 after full sweep, extend Stage 2 before proceeding.

---

### Stage 4 — Surprise Synthesis

For each GATE-CONFIRMED candidate, write a numbered prose block. A table row is not acceptable for
this stage; the prose block format is mandatory.

**Surprise N: [Title — 3–6 words, title case]**

**Surprise**: State what was learned. Name the specific B-# it contradicts or substantially
extends. Complete sentence.

**Signal Source**: Name the artifact: full artifact name, namespace, date. One primary source per
entry. "Multiple sources" or "various artifacts" is not acceptable.

**Design Impact**: Name the specific component, API, contract, flow, or decision affected. Complete
sentence. "The system" or "the overall design" is not acceptable.

`COMMIT-ENTRY-[N]: entry committed.`

Minimum 2 entries. If fewer than 2 GATE-CONFIRMED entries exist after the initial Stage 3 sweep,
extend Stage 2 and re-execute Stage 3 before proceeding.

`COMMIT-STAGE-4`

---

### Stage 5 — Cluster Map

Group Stage 4 surprises by shared theme or implication.

| Cluster | Surprises | Implication | Next Team / Skill |
|---------|-----------|-------------|-------------------|
| [Name] | S-N, S-M | [1 sentence] | [Named skill, e.g. `/flow-trigger`, or specific role — not "investigate"] |

Minimum 1 cluster. At least one row must name a specific skill or role in the Next Team / Skill
column.

`COMMIT-STAGE-5`

---

### Stage 6 — Symmetric Contract Closure

Close the contract opened in Stage 1. For each Stage 1 belief:

| Belief | Resolution | Revision Direction | Foreknowledge |
|--------|------------|-------------------|---------------|
| B-N | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | [How the belief changed] | CLEAR / FLAGGED |

**Closing verdict** (2–4 sentences): What does the team now know that it did not know before
investigation? How does this change the design direction for `{topic}`?

Halt condition: if any belief row is FOREKNOWLEDGE-FLAGGED, do not write the artifact. Report the
flag and name the responsible beliefs.

`COMMIT-STAGE-6`

---

### Output

Write to: `simulations/{topic}/{topic}-echo-{date}.md`

Include all 6 stages in sequence. All tokens (`COMMIT-STAGE-1` through `COMMIT-STAGE-6`,
`GATE-CONFIRMED-[N]`, `GATE-REJECTED-[N]`, `COMMIT-ENTRY-[N]`) must appear in the artifact.

---

## V-02 — Lifecycle Emphasis (Explicit ENTER/EXIT per Stage)

**Axis**: B — each stage is bounded by explicit ENTER conditions (prerequisites before the stage
begins) and EXIT conditions (completeness criteria before the commit token). Stages are state
transitions, not prose sections.

**Hypothesis**: Explicit ENTER/EXIT conditions per stage prevent the two primary lifecycle failure
modes: (1) premature stage transition, where the model proceeds to Stage N+1 before Stage N is
complete; (2) stage collapse, where the model merges multiple stages into a single pass and skips
token emissions. ENTER conditions also function as implicit coverage checks — restating minimum
inputs required forces the model to verify its current state before proceeding. Secondary
hypothesis: EXIT conditions listing field-level completeness criteria directly improve C-12 (no
single-word or two-word field entries) because the exit gate names the completeness standard that
fields must meet.

---

You are executing `/topic-echo` for topic `{topic}`.

One question: **What did we learn that we did not expect?**

Not summaries. Not confirmations. Surprises — findings that contradicted or substantially extended
the prior model. The artifact produced here is institutional memory for the next team.

---

### Vocabulary

The 5 canonical epistemic dimension names:

**Feasibility · Usability · Scalability · Adoptability · Correctness**

These names are fixed. Do not substitute. Any other term in a dimension cell is malformed.

---

### Stage 1 — Opening Model

**ENTER**: No signal artifacts have been read. This stage captures prior-state only.

1. **Opening model** (2–4 sentences): What did the team believe about `{topic}` before
   investigation began? Name the specific assumptions that could be overturned.

2. **Epistemic profile**: One row per canonical dimension — prior belief (1–2 sentences) +
   confidence (HIGH / MEDIUM / LOW):

| Dimension | Prior Belief | Confidence |
|-----------|-------------|------------|
| Feasibility | | HIGH / MEDIUM / LOW |
| Usability | | HIGH / MEDIUM / LOW |
| Scalability | | HIGH / MEDIUM / LOW |
| Adoptability | | HIGH / MEDIUM / LOW |
| Correctness | | HIGH / MEDIUM / LOW |

3. **Belief inventory**: ≥3 falsifiable beliefs, numbered B-1 through B-N.

**EXIT**: All 5 dimension rows populated with non-empty prior beliefs. At least 3 beliefs numbered.
No signal artifact has been consulted.

`COMMIT-STAGE-1`

---

### Stage 2 — Signal Inventory

**ENTER**: Stage 1 committed. Now consult signal artifacts.

List every signal artifact for `{topic}`:

| Artifact | Namespace | Date | Primary Finding (1 sentence) |
|----------|-----------|------|------------------------------|
| | | | |

**EXIT**: All available artifacts listed. No artifact omitted. Finding column populated for every
row with a complete sentence.

`COMMIT-STAGE-2`

---

### Stage 3 — Adversarial Gate

**ENTER**: Stage 2 committed. Candidate surprises identified from Stage 2 deviations.

For each candidate, run the five-check table:

| Check | Test | Verdict |
|-------|------|---------|
| FC-1 | Absent from B-1 through B-N? | VALID / INVALID |
| FC-2 | Contradicts (not confirms) the opening model? | VALID / INVALID |
| FC-3 | Not predictable from prior domain knowledge? | VALID / INVALID |
| FC-4 | Source artifact specifically named (name + date)? | VALID / INVALID |
| FC-5 | Design impact non-trivial? | VALID / INVALID |

All VALID → emit `GATE-CONFIRMED-[N]: VALID — Stage 4.`
Any INVALID → emit `GATE-REJECTED-[N]: INVALID — Check [#]: [reason].`

Foreknowledge verdict (after all candidates evaluated):
- All candidates clean: `COMMIT-STAGE-3-CLEAN`
- Any finding anticipated by Stage 1 beliefs: `COMMIT-STAGE-3-FLAGGED — [B-#] anticipated [finding].`

**EXIT**: Every candidate has a verdict. COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED emitted.
GATE-CONFIRMED count confirmed. If count < 2: halt, return to Stage 2, extend inventory, re-execute
Stage 3.

---

### Stage 4 — Surprise Synthesis

**ENTER**: COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED emitted. At least 2 GATE-CONFIRMED
entries confirmed.

Write a numbered prose block for each GATE-CONFIRMED entry:

**Surprise N: [Title]**

**Surprise**: What was learned. Name the specific B-# it contradicts or substantially extends.
Full sentence — not a fragment.

**Signal Source**: Primary artifact: name, namespace, date. One source per entry. "Multiple
sources" is not acceptable.

**Design Impact**: Specific component, API, contract, flow, or decision affected. Full sentence.
"The system" or "the design generally" is not acceptable.

`COMMIT-ENTRY-[N]: entry committed.`

**EXIT per entry**: All three fields populated. Surprise names a B-#. Signal Source names a
specific artifact with date. Design Impact names a specific component or contract. No field is a
fragment or a single noun phrase.

`COMMIT-STAGE-4`

---

### Stage 5 — Cluster Map

**ENTER**: All Stage 4 entries committed.

Group surprises by shared theme:

| Cluster | Surprises | Implication | Next Team / Skill |
|---------|-----------|-------------|-------------------|
| [Name] | S-N, S-M | [1 sentence] | [Named skill or specific role] |

At least one row must name a specific skill (e.g., `/trace-contract`) or role — not "investigate."

**EXIT**: All Stage 4 surprises assigned to a cluster. At least one named next step.

`COMMIT-STAGE-5`

---

### Stage 6 — Symmetric Contract Closure

**ENTER**: All prior stages committed.

Close the loop on Stage 1 beliefs:

| Belief | Resolution | Revision Direction | Foreknowledge |
|--------|------------|-------------------|---------------|
| B-N | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | [Direction of change] | CLEAR / FLAGGED |

**Closing verdict** (2–4 sentences): What does the team now know that it did not know before? How
does this change the design direction for `{topic}`?

Halt condition: if any row is FOREKNOWLEDGE-FLAGGED, do not write the artifact. Name the flagged
beliefs and report the flag.

**EXIT**: Every Stage 1 belief has a resolution row. Revision Direction column populated for every
row. Closing verdict written.

`COMMIT-STAGE-6`

---

### Output

Write to: `simulations/{topic}/{topic}-echo-{date}.md`

All 6 stages in sequence. All tokens present.

---

## V-03 — Output Format: Pre-Stage Gate Sequence Map

**Axis**: C — a complete gate topology table appears before Stage 1, enumerating every stage,
token emitted, and halt condition as a single navigable reference. The model reads the full
execution contract before entering stage-by-stage instructions.

**Hypothesis**: A gate map surfaces the execution model as a single table that the model can
re-consult at any stage without re-reading prior stage prose. The primary benefit is orientation
to the gate topology — which tokens gate which stages, where halts apply, what CLEAN vs FLAGGED
means — before Stage 1 introduces the substantive content. A model that has read the gate map
once can answer "what stage am I in and what halts me?" without back-tracking. Secondary benefit:
the gate map makes COMMIT-STAGE-3-CLEAN and COMMIT-STAGE-3-FLAGGED semantically distinct before
Stage 3 instructions introduce them inline, reducing the risk of conflating them. The risk: the
gate map adds front-loading without adding substantive completeness criteria — if the model treats
it as preamble to skip, C-15 passes but execution quality is unchanged.

---

You are executing `/topic-echo` for topic `{topic}`.

The single question this skill answers: **What did we learn that we did not expect?**

---

### Gate Sequence Overview

Read this before Stage 1. It is the complete execution model for this skill.

| Stage | Name | Emits | Halt Condition |
|-------|------|-------|----------------|
| 1 | Opening Model | `COMMIT-STAGE-1` | None — always executes before any signal artifact is read |
| 2 | Signal Inventory | `COMMIT-STAGE-2` | None — always executes |
| 3 | Adversarial Gate | `GATE-CONFIRMED-[N]` or `GATE-REJECTED-[N]` per candidate; then `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED` | If GATE-CONFIRMED count < 2 after full sweep: halt, extend Stage 2, re-execute Stage 3 |
| 4 | Surprise Synthesis | `COMMIT-ENTRY-[N]` per entry; `COMMIT-STAGE-4` | Requires ≥2 GATE-CONFIRMED entries from Stage 3 |
| 5 | Cluster Map | `COMMIT-STAGE-5` | None |
| 6 | Symmetric Contract Closure | `COMMIT-STAGE-6` | If any belief is FOREKNOWLEDGE-FLAGGED: halt, do not write artifact |

**Token glossary:**
- `GATE-CONFIRMED-[N]: VALID — Stage 4.` — entry passed all five checks; routes to Stage 4
- `GATE-REJECTED-[N]: INVALID — Check [#]: [reason].` — entry failed; excluded from Stage 4
- `COMMIT-STAGE-3-CLEAN` — no Stage 2 finding was anticipated by Stage 1 beliefs
- `COMMIT-STAGE-3-FLAGGED — [B-#] anticipated [finding].` — one or more findings were known going in; named findings excluded from Stage 4
- `COMMIT-ENTRY-[N]: entry committed.` — required after each Stage 4 prose block before the next begins
- `COMMIT-STAGE-1` through `COMMIT-STAGE-6` — all six must appear in the final artifact

---

### Vocabulary

The 5 canonical epistemic dimension names:

**Feasibility · Usability · Scalability · Adoptability · Correctness**

These are the only valid names. Do not substitute.

---

### Stage 1 — Opening Model

Before consulting any signal artifact, record the prior state:

1. **Opening model** (2–4 sentences): what the team believed about `{topic}` before investigation
   began; name the assumptions explicitly.
2. **Epistemic profile**: one row per canonical dimension — prior belief + confidence
   (HIGH / MEDIUM / LOW).
3. **Belief inventory**: ≥3 falsifiable beliefs, numbered B-1 through B-N.

`COMMIT-STAGE-1`

---

### Stage 2 — Signal Inventory

List all signal artifacts for `{topic}`:

| Artifact | Namespace | Date | Primary Finding (1 sentence) |
|----------|-----------|------|------------------------------|
| | | | |

`COMMIT-STAGE-2`

---

### Stage 3 — Adversarial Gate

For each candidate surprise, complete the five-check table:

| Check | Test | Verdict |
|-------|------|---------|
| FC-1 | Absent from Stage 1 beliefs? | VALID / INVALID |
| FC-2 | Contradicts (not confirms) the opening model? | VALID / INVALID |
| FC-3 | Not predictable from domain knowledge alone? | VALID / INVALID |
| FC-4 | Source artifact specifically named? | VALID / INVALID |
| FC-5 | Design impact non-trivial? | VALID / INVALID |

Passing: `GATE-CONFIRMED-[N]: VALID — Stage 4.`
Failing: `GATE-REJECTED-[N]: INVALID — Check [#]: [reason].`

Foreknowledge resolution:
- All clean: `COMMIT-STAGE-3-CLEAN`
- Any anticipated by Stage 1: `COMMIT-STAGE-3-FLAGGED — [B-#] anticipated [finding].`

Refer to the Gate Sequence Overview for the halt condition if GATE-CONFIRMED count < 2.

---

### Stage 4 — Surprise Synthesis

For each GATE-CONFIRMED entry, write a numbered prose block:

**Surprise N: [Title]**

**Surprise**: [What was learned. Name the specific B-# contradicted or extended. Full sentence.]

**Signal Source**: [Artifact name, namespace, date. One specific source per entry.]

**Design Impact**: [Specific component, API, contract, flow, or decision. Full sentence. Not "the
system."]

`COMMIT-ENTRY-[N]: entry committed.`

Minimum 2 entries.

`COMMIT-STAGE-4`

---

### Stage 5 — Cluster Map

| Cluster | Surprises | Implication | Next Team / Skill |
|---------|-----------|-------------|-------------------|
| [Name] | S-N, S-M | [1 sentence] | [Named skill or role] |

At least one row must name a specific skill (e.g., `/trace-permissions`) or role.

`COMMIT-STAGE-5`

---

### Stage 6 — Symmetric Contract Closure

For each Stage 1 belief:

| Belief | Resolution | Revision Direction | Foreknowledge |
|--------|------------|-------------------|---------------|
| B-N | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | [How it changed] | CLEAR / FLAGGED |

Closing verdict (2–4 sentences): what the team now knows, and how it changes the design direction.

Refer to the Gate Sequence Overview for the FOREKNOWLEDGE-FLAGGED halt condition.

`COMMIT-STAGE-6`

---

### Output

Write to: `simulations/{topic}/{topic}-echo-{date}.md`

All 6 stages in order, all tokens present.

---

## V-04 — Combined: Phrasing Register (Formal) + Worked Calibration Example

**Axes**: A (formal/technical register, named synonym exclusions) + D (worked calibration example
at Stage 4 entry).

**Hypothesis**: These two axes address adjacent failure modes at different levels of abstraction.
Named synonym exclusions (C-17) operate at the vocabulary level — they prevent the model from
substituting "Reliability" for "Correctness" because the substitution is explicitly named as a
violation, not merely implied by the closed-list rule. The worked calibration example (C-16)
operates at the quality level — it prevents the model from producing structurally-valid but
semantically-thin Stage 4 entries by providing a realistic filled-in instance that defines the
quality floor. A template such as "[Full sentence]" instructs format; a worked example anchors the
bar against a concrete instance the model can compare itself to. The combination is non-redundant:
a model can follow the vocabulary rule correctly while still producing thin Signal Source or Design
Impact entries; and a model can produce high-quality entries while still drifting on dimension
vocabulary. Both axes are necessary for full C-06 + C-12 + C-16 + C-17 coverage.

---

You are executing `/topic-echo` for topic `{topic}`.

**Role**: Signal Echo Analyst. Your output is institutional memory — a structured record of what
this team learned that contradicted or substantially extended its prior model. The next team reads
this artifact before repeating the investigation. Make every entry specific enough to be
actionable.

**Scope**: Surprises only. A finding that confirms a prior belief is not a surprise and must not
appear in Stage 4.

---

### Vocabulary Declaration

**The only valid epistemic dimension names are:**

> Feasibility · Usability · Scalability · Adoptability · Correctness

The following substitutions are explicitly prohibited. Each is named to prevent the most common
substitution errors by converting them from implicit to named violations:

- **"Reliability"** — prohibited. Use **Correctness**.
- **"Performance"** — prohibited. Use **Scalability**.
- **"Complexity"** — prohibited. Use **Correctness** (structural) or **Feasibility**
  (implementation difficulty).
- **"Maintainability"** — prohibited. Use **Adoptability**.
- **"Discoverability"** — prohibited. Use **Usability** or **Adoptability**.
- **"Testability"** — prohibited. Use **Correctness** or **Feasibility**.

Any dimension cell containing a name not in the canonical list is malformed. Rewrite it before
emitting the stage commit token.

---

### Stage 1 — Opening Model

Before consulting any signal artifact, record the prior state:

1. **Opening model** (2–4 sentences): what the team believed about `{topic}` before signals were
   gathered; name the assumptions explicitly.

2. **Epistemic profile** — one row per canonical dimension:

| Dimension | Prior Belief | Confidence |
|-----------|-------------|------------|
| Feasibility | | HIGH / MEDIUM / LOW |
| Usability | | HIGH / MEDIUM / LOW |
| Scalability | | HIGH / MEDIUM / LOW |
| Adoptability | | HIGH / MEDIUM / LOW |
| Correctness | | HIGH / MEDIUM / LOW |

3. **Belief inventory**: ≥3 falsifiable beliefs, numbered B-1 through B-N.

`COMMIT-STAGE-1`

---

### Stage 2 — Signal Inventory

List all signal artifacts for `{topic}`:

| Artifact | Namespace | Date | Primary Finding (1 sentence) |
|----------|-----------|------|------------------------------|
| | | | |

`COMMIT-STAGE-2`

---

### Stage 3 — Adversarial Gate

For each candidate surprise, execute the five-check table:

| Check | Test | Verdict |
|-------|------|---------|
| FC-1 | Absent from all B-# beliefs? | VALID / INVALID |
| FC-2 | Contradicts (not confirms) the opening model? | VALID / INVALID |
| FC-3 | Not predictable from prior domain knowledge? | VALID / INVALID |
| FC-4 | Source artifact specifically named (name, namespace, date)? | VALID / INVALID |
| FC-5 | Design impact non-trivial? | VALID / INVALID |

All VALID → `GATE-CONFIRMED-[N]: VALID — Stage 4.`
Any INVALID → `GATE-REJECTED-[N]: INVALID — Check [#]: [reason].`

Foreknowledge resolution:
- No anticipated findings → `COMMIT-STAGE-3-CLEAN`
- Any finding anticipated by Stage 1 beliefs → `COMMIT-STAGE-3-FLAGGED — [B-#] anticipated [finding].`

Halt: if GATE-CONFIRMED count < 2, extend Stage 2 before proceeding.

---

### Stage 4 — Surprise Synthesis

**Calibration example** — this is a worked instance, not a template. It defines the quality floor.
Every Stage 4 entry you write must be at or above this bar for Signal Source specificity and
Design Impact concreteness:

> **Surprise 0: Namespace Isolation Blocks Cross-Signal Composition**
>
> **Surprise**: We assumed signal artifacts from different namespaces could be retrieved in a
> single composite query, enabling `/topic-story` to assemble `scout` and `trace` evidence in one
> pass (contradicts B-3). The `topic-registry-trace-contract-2026-02-14.md` artifact revealed that
> the registry enforces namespace partitioning as a hard contract boundary — cross-namespace reads
> are not supported in the current contract model.
>
> **Signal Source**: `topic-registry-trace-contract-2026-02-14.md`, trace namespace, 2026-02-14.
>
> **Design Impact**: The `/topic-story` skill must issue sequential per-namespace reads and merge
> results client-side; the single-query assumption must be removed from the skill contract before
> implementation begins.

For each GATE-CONFIRMED candidate, write a numbered prose block at or above the calibration bar:

**Surprise N: [Title — 3–6 words, title case]**

**Surprise**: [What was learned. Name the specific B-# contradicted or substantially extended.
Full sentence.]

**Signal Source**: [Artifact name, namespace, date. One primary source per entry. "Multiple
sources" or "various artifacts" is not acceptable.]

**Design Impact**: [Specific component, API, contract, flow, or decision affected. Full sentence.
"The system" or "the design generally" is not acceptable.]

`COMMIT-ENTRY-[N]: entry committed.`

Minimum 2 entries.

`COMMIT-STAGE-4`

---

### Stage 5 — Cluster Map

| Cluster | Surprises | Implication | Next Team / Skill |
|---------|-----------|-------------|-------------------|
| [Name] | S-N, S-M | [1 sentence] | [Named skill or specific role] |

At least one row must name a specific skill or role.

`COMMIT-STAGE-5`

---

### Stage 6 — Symmetric Contract Closure

For each Stage 1 belief:

| Belief | Resolution | Revision Direction | Foreknowledge |
|--------|------------|-------------------|---------------|
| B-N | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | [Direction of revision] | CLEAR / FLAGGED |

**Closing verdict** (2–4 sentences): What does the team now know that it did not know before
investigation? How does this change the design direction for `{topic}`?

Halt condition: if any row is FOREKNOWLEDGE-FLAGGED, do not write the artifact. Name the flagged
beliefs.

`COMMIT-STAGE-6`

---

### Output

Write to: `simulations/{topic}/{topic}-echo-{date}.md`

All 6 stages in sequence. All tokens present.

---

## V-05 — Combined: Pre-Stage Gate Map + Inertia Framing + Conversational Register

**Axes**: C (pre-stage gate map) + E (inertia framing — explicit naming of what the team "would
have shipped" without signals) + conversational register.

**Hypothesis**: Conversational framing makes the surprise-orientation more natural and reduces
over-formal template-filling behavior, which can produce structurally-valid entries that are
semantically hollow (the model follows the template without anchoring claims to real artifacts).
Inertia framing sharpens the COHERENT/CONTRADICTORY verdict: making the "what we would have done
without signals" model explicit gives the model a concrete foil against which to test each
finding, reducing COHERENT misclassifications. The gate map compensates for a risk introduced by
the relaxed register — in conversational framing, token emission instructions can read as optional
("you'll be glad you did") — by establishing the execution contract as a non-negotiable topology
before Stage 1 begins. The combination tests whether register-agnostic gate enforcement (via the
map) can maintain token discipline under conversational framing.

---

You are running `/topic-echo` for topic `{topic}`.

One question only: **What did we learn that we didn't expect?**

Not a recap of what went well. Not a list of confirmed assumptions. Just the surprises — the places
where the signals came back different from what the team thought it knew. That's the institutional
memory the next team needs.

---

### Before You Start: Gate Map

Here's the full execution flow. Read it once before Stage 1.

| Stage | What Happens | What Gets Emitted | What Can Stop You |
|-------|-------------|-------------------|-------------------|
| 1 | Write down what you believed before gathering signals — the inertia baseline | `COMMIT-STAGE-1` | Nothing — do this before touching any signal artifact |
| 2 | Inventory every signal artifact for `{topic}` | `COMMIT-STAGE-2` | Nothing |
| 3 | Challenge each candidate: was it actually unexpected? | `GATE-CONFIRMED-[N]` or `GATE-REJECTED-[N]` per candidate; then `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED` | Fewer than 2 survive the gate: go back, extend Stage 2, re-run Stage 3 |
| 4 | Write up the genuine surprises as prose blocks | `COMMIT-ENTRY-[N]` per entry; `COMMIT-STAGE-4` | Needs ≥2 GATE-CONFIRMED from Stage 3 |
| 5 | Cluster the surprises and name next steps | `COMMIT-STAGE-5` | Nothing |
| 6 | Close the loop on Stage 1 beliefs | `COMMIT-STAGE-6` | Any FOREKNOWLEDGE-FLAGGED belief: don't write the artifact |

`GATE-CONFIRMED-[N]: VALID — Stage 4.` means this entry is a real surprise — it proceeds to Stage 4.
`GATE-REJECTED-[N]: INVALID — Check [#]: [reason].` means it didn't qualify — it's excluded.
`COMMIT-STAGE-3-CLEAN` means none of your Stage 1 beliefs anticipated any finding.
`COMMIT-STAGE-3-FLAGGED — [B-#] anticipated [finding].` means at least one finding was already
known going in.

All six `COMMIT-STAGE-[N]` tokens must appear in the artifact. A missing token means an incomplete
run.

---

### Dimension Names (closed list — no substitutions)

When you write about epistemic dimensions, use only these five names:

**Feasibility · Usability · Scalability · Adoptability · Correctness**

Not "Reliability" — that's Correctness. Not "Performance" — that's Scalability. Not
"Maintainability" — that's Adoptability. If you find yourself writing any other name, replace it.

---

### Stage 1 — What Did You Believe?

Before looking at any signal artifact, write down the **inertia baseline** for `{topic}` — what
the team would have shipped if no signals had been gathered. Be specific. Name the assumptions.
These are the bets the signals will test.

**Opening model** (2–4 sentences): the prior state of knowledge. Name the assumptions explicitly.

**Epistemic profile**: one row per dimension:

| Dimension | Prior Belief | Confidence |
|-----------|-------------|------------|
| Feasibility | | HIGH / MEDIUM / LOW |
| Usability | | HIGH / MEDIUM / LOW |
| Scalability | | HIGH / MEDIUM / LOW |
| Adoptability | | HIGH / MEDIUM / LOW |
| Correctness | | HIGH / MEDIUM / LOW |

**Beliefs**: write at least 3, numbered B-1 through B-N. Each is a falsifiable statement about
`{topic}` that a signal could contradict.

`COMMIT-STAGE-1`

---

### Stage 2 — What Signals Do You Have?

List every signal artifact for `{topic}`:

| Artifact | Namespace | Date | One-Sentence Finding |
|----------|-----------|------|---------------------|
| | | | |

`COMMIT-STAGE-2`

---

### Stage 3 — Are These Actually Surprises?

For each candidate finding — something a signal seems to be telling you — run the five-question
check:

| Check | Question | Verdict |
|-------|----------|---------|
| FC-1 | Is it absent from your Stage 1 beliefs? | VALID / INVALID |
| FC-2 | Does it contradict (not just confirm) the inertia baseline? | VALID / INVALID |
| FC-3 | Could you have predicted it without running the signals? | VALID / INVALID |
| FC-4 | Can you name a specific artifact as the source? | VALID / INVALID |
| FC-5 | Does it have a non-trivial impact on the design? | VALID / INVALID |

All VALID → `GATE-CONFIRMED-[N]: VALID — Stage 4.`
Any INVALID → `GATE-REJECTED-[N]: INVALID — Check [#]: [reason].`

If a finding was anticipated by a Stage 1 belief: `COMMIT-STAGE-3-FLAGGED — [B-#] anticipated [finding].`
If all candidates are clean: `COMMIT-STAGE-3-CLEAN`.

Check the Gate Map if fewer than 2 pass — you need to extend Stage 2 before proceeding.

---

### Stage 4 — Write the Surprises

For each GATE-CONFIRMED entry, write a numbered prose block. These are the entries the next team
will actually read — make them specific enough to be useful.

**Surprise N: [Name it — a short phrase capturing what was unexpected]**

**Surprise**: What did you learn? Name the specific B-# it contradicts or substantially changes.
Complete sentence.

**Signal Source**: Name the artifact — full name, namespace, date. One source per entry.
"Multiple sources" or "several signals" is not acceptable.

**Design Impact**: What changes in the design? Name the specific component, contract, flow, API,
or decision. Complete sentence. "The system" or "the overall design" is not acceptable.

`COMMIT-ENTRY-[N]: entry committed.`

Would the next engineer know exactly what to look at from this entry? If not, it's not ready.

Minimum 2 entries.

`COMMIT-STAGE-4`

---

### Stage 5 — What Patterns Emerge?

Group the surprises by what they're pointing at together:

| Cluster Name | Which Surprises | What It Means | Who Handles It Next |
|--------------|-----------------|---------------|---------------------|
| | S-N, S-M | 1 sentence | Named skill (e.g., `/flow-trigger`) or specific role — not "investigate" |

At least one row needs a named next step that someone can actually act on.

`COMMIT-STAGE-5`

---

### Stage 6 — Close the Loop

Go back to your Stage 1 beliefs. For each one:

| Belief | What Happened | How It Changed | Foreknowledge |
|--------|--------------|----------------|---------------|
| B-N | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | Direction of revision | CLEAR / FLAGGED |

**Closing verdict** (2–4 sentences): The team now knows X that it didn't before. Here's how that
changes the direction for `{topic}`.

Check the Gate Map for the FOREKNOWLEDGE-FLAGGED halt condition.

`COMMIT-STAGE-6`

---

### Output

Write to: `simulations/{topic}/{topic}-echo-{date}.md`

All 6 stages, all tokens, in sequence.
