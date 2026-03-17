# quest-variate Variations — Round 5 (topic-reflect v5 rubric)
**Skill**: topic-echo (topic-reflect)
**Rubric**: v5-2026-03-17 (C-01–C-05 essential, C-06–C-08 recommended, C-09–C-19 aspirational)
**N_essential=5, N_recommended=3, N_aspirational=11**
**Date**: 2026-03-17
**Round**: 5

---

## Context: what informed this round

The v4 rubric produced four golden scores in Round 4 — V-01 and V-03 at 125, V-02 at 120, V-04
at 130. Two new aspirational criteria (C-18, C-19) were extracted from Round 4 excellence signals:

| Criterion | Source variation | What it detected |
|-----------|----------------|-----------------|
| C-18 (synonym-to-canonical mapping) | V-01 only | A vocabulary table that not only names prohibited synonyms but maps each to its canonical replacement — closing the substitution loop that C-17 opens |
| C-19 (per-stage ENTER/EXIT lifecycle contract) | V-02 only | Explicit ENTER conditions and EXIT criteria at each stage boundary — stages as verifiable state transitions rather than prose sections |

The v5 rubric score formula:

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 11 * 55)
```

**Golden threshold**: all C-01–C-05 pass AND composite >= 100
**Score landmarks:**
- All essential + all recommended + all 11 aspirational: 145
- All essential + all recommended + 2/11 aspirational: 100 (golden threshold)
- All essential + all recommended + 0 aspirational: 90
- All essential + 0 recommended + 0 aspirational: 60

---

## Variation axis selection

| Axis | Label | Single/Combined | Targets |
|------|-------|----------------|---------|
| A | Synonym-to-canonical mapping | Single | C-18 (closes the substitution loop opened by C-17) |
| B | Per-stage ENTER/EXIT contracts | Single | C-19 (stages as verifiable state transitions, not prose sections) |
| C | Pre-stage gate sequence map | Single | C-15 (navigation context before Stage 1; orientation to gate topology) |
| D | A + B | Combined | C-18 + C-19 (both new criteria without other structural additions) |
| E | A + B + C + worked calibration | Combined | C-18 + C-19 + C-15 + C-16 (maximum aspirational coverage) |

Base mechanisms in all variations: correct canonical dimension names
(Feasibility · Usability · Scalability · Adoptability · Correctness), Stage 4 as numbered prose
blocks (not tables), COMMIT-STAGE-3-CLEAN / COMMIT-STAGE-3-FLAGGED foreknowledge gate,
GATE-CONFIRMED token naming Stage 4 by name, COMMIT-ENTRY per Stage 4 row, at least two named
prohibited synonyms (C-17: Reliability and Performance named in all variations).

---

## V-01 — Synonym-to-Canonical Mapping (C-18)

**Axis**: A — formal/technical register; named synonym exclusions (C-17) extended to include a
canonical replacement for each prohibited term (C-18). No ENTER/EXIT contracts. No gate map.

**Hypothesis**: C-17 names prohibited synonyms and converts them from implicit to explicit
violations — a model that has read "Reliability is prohibited" can no longer claim ignorance.
C-18 closes the second half of the problem: a model that knows "Reliability is prohibited" still
has to infer the correct replacement, and may reach for another non-canonical term. A model given
"Reliability → Correctness" has no residual substitution ambiguity. The mapping table format
(not inline prose) is the structural choice: a scannable table can be consulted before writing
dimension cells without re-reading Stage 1 prose. Secondary hypothesis: formal imperative register
correlates with longer, more complete field entries (C-12) because the register signals that
terse fragments are structurally inappropriate.

---

You are executing `/topic-echo` for topic `{topic}`.

**Function**: Produce the institutional memory artifact for `{topic}`. Answer one question:
**What did this team learn that it did not expect?**

This is not a summary. It is not a confirmation list. It is a synthesis of surprises — findings
that contradicted, revised, or substantially extended the prior model. A finding that confirms a
prior belief is not a surprise. It is excluded.

---

### Vocabulary Declaration

**The only valid epistemic dimension names are:**

> Feasibility · Usability · Scalability · Adoptability · Correctness

The following table maps each prohibited synonym to its canonical replacement. Use this table to
correct any malformed dimension cell before emitting the commit token for that stage:

| Prohibited term | Canonical replacement |
|----------------|----------------------|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Correctness (structural) or Feasibility (implementation) |
| Maintainability | Adoptability |
| Discoverability | Usability or Adoptability |
| Testability | Correctness or Feasibility |

Any dimension cell containing a prohibited term is malformed. Replace it using the mapping table
above before emitting the stage commit token.

---

### Stage 1 — Opening Model

Do not consult signal artifacts at this stage. Record the epistemic state at investigation onset.

1. **Opening model**: 2–4 sentences. State what the team believed about `{topic}` before signals
   were gathered. Name the specific assumptions that signals could contradict.

2. **Epistemic profile**: One row per canonical dimension, from the closed list only:

| Dimension | Prior Belief | Confidence |
|-----------|-------------|------------|
| Feasibility | | HIGH / MEDIUM / LOW |
| Usability | | HIGH / MEDIUM / LOW |
| Scalability | | HIGH / MEDIUM / LOW |
| Adoptability | | HIGH / MEDIUM / LOW |
| Correctness | | HIGH / MEDIUM / LOW |

3. **Belief inventory**: Minimum 3 falsifiable beliefs, numbered B-1 through B-N. Each belief is
   a flat statement about `{topic}` that a signal artifact could contradict.

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

For each candidate surprise, execute the five-check table. A candidate is a Stage 2 deviation
that appears to contradict or substantially extend a Stage 1 belief.

| Check | Test | Verdict |
|-------|------|---------|
| FC-1 | Absent from all B-# beliefs? | VALID / INVALID |
| FC-2 | Contradicts (not confirms) the opening model? | VALID / INVALID |
| FC-3 | Not predictable from domain knowledge alone? | VALID / INVALID |
| FC-4 | Source artifact specifically named (name, namespace, date)? | VALID / INVALID |
| FC-5 | Design impact non-trivial? | VALID / INVALID |

For each candidate passing all checks:

`GATE-CONFIRMED-[N]: VALID — Stage 4.`

For each failing candidate:

`GATE-REJECTED-[N]: INVALID — Check [#]: [reason].`

Foreknowledge resolution — after evaluating all candidates:
- No findings anticipated by Stage 1 beliefs: `COMMIT-STAGE-3-CLEAN`
- Any finding anticipated by Stage 1 beliefs: `COMMIT-STAGE-3-FLAGGED — [B-#] anticipated [finding].`

Halt condition: if GATE-CONFIRMED count < 2 after full sweep, extend Stage 2 before proceeding.

---

### Stage 4 — Surprise Synthesis

For each GATE-CONFIRMED candidate, write a numbered prose block. A table row is not acceptable
for this stage; the prose block format is mandatory.

**Surprise N: [Title — 3–6 words, title case]**

**Surprise**: State what was learned. Name the specific B-# it contradicts or substantially
extends. Complete sentence.

**Signal Source**: Name the artifact: full artifact name, namespace, date. One primary source per
entry. "Multiple sources" or "various artifacts" is not acceptable.

**Design Impact**: Name the specific component, API, contract, flow, or decision affected.
Complete sentence. "The system" or "the overall design" is not acceptable.

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

Halt condition: if any belief row is FOREKNOWLEDGE-FLAGGED, do not write the artifact. Report
the flag and name the responsible beliefs.

`COMMIT-STAGE-6`

---

### Output

Write to: `simulations/{topic}/{topic}-echo-{date}.md`

Include all 6 stages in sequence. All tokens (`COMMIT-STAGE-1` through `COMMIT-STAGE-6`,
`GATE-CONFIRMED-[N]`, `GATE-REJECTED-[N]`, `COMMIT-ENTRY-[N]`) must appear in the artifact.

---

## V-02 — Per-Stage ENTER/EXIT Lifecycle Contracts (C-19)

**Axis**: B — each stage is bounded by explicit ENTER conditions (what must be true before the
stage begins) and EXIT criteria (what constitutes successful completion before the commit token).
Stages are verifiable state transitions, not prose sections. No synonym mapping table. No gate map.

**Hypothesis**: Explicit ENTER/EXIT contracts address two primary lifecycle failure modes:
(1) premature stage transition — the model proceeds to Stage N+1 before Stage N is complete;
(2) stage collapse — the model merges multiple stages into a single pass and omits intermediate
tokens. ENTER conditions function as implicit coverage checks: restating minimum inputs required
before a stage forces the model to verify its current state before proceeding. EXIT criteria
function as completeness gates: listing field-level requirements before the commit token prevents
the model from emitting a token without satisfying those requirements. Secondary hypothesis: EXIT
criteria naming specific field completeness requirements directly improve C-12 compliance (no
single-word or two-word field entries) because the exit gate names the standard fields must meet
before the stage can close.

---

You are executing `/topic-echo` for topic `{topic}`.

One question: **What did we learn that we did not expect?**

Not summaries. Not confirmations. Surprises only — findings that contradicted or substantially
extended the prior model. The artifact produced here is institutional memory for the next team.

---

### Vocabulary

The 5 canonical epistemic dimension names:

**Feasibility · Usability · Scalability · Adoptability · Correctness**

These names are fixed. Do not substitute. Prohibited synonyms: "Reliability" (use Correctness),
"Performance" (use Scalability), "Maintainability" (use Adoptability). Any other term in a
dimension cell is malformed — replace it before emitting the stage commit token.

---

### Stage 1 — Opening Model

**ENTER**: No signal artifacts have been read. This stage captures prior-state only. Prior
beliefs must be recorded before any artifact is consulted.

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

**EXIT**: All 5 dimension rows populated with non-empty prior beliefs. At least 3 beliefs
numbered. No signal artifact has been consulted.

`COMMIT-STAGE-1`

---

### Stage 2 — Signal Inventory

**ENTER**: Stage 1 committed. Now consult signal artifacts.

List every signal artifact for `{topic}`:

| Artifact | Namespace | Date | Primary Finding (1 sentence) |
|----------|-----------|------|------------------------------|
| | | | |

**EXIT**: All available artifacts listed. Finding column populated for every row with a complete
sentence. No artifact omitted.

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
| FC-4 | Source artifact specifically named (name + namespace + date)? | VALID / INVALID |
| FC-5 | Design impact non-trivial? | VALID / INVALID |

All VALID → emit `GATE-CONFIRMED-[N]: VALID — Stage 4.`
Any INVALID → emit `GATE-REJECTED-[N]: INVALID — Check [#]: [reason].`

Foreknowledge verdict (after all candidates evaluated):
- All candidates clean: `COMMIT-STAGE-3-CLEAN`
- Any finding anticipated by Stage 1 beliefs: `COMMIT-STAGE-3-FLAGGED — [B-#] anticipated [finding].`

**EXIT**: Every candidate has a verdict token. COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED
emitted. GATE-CONFIRMED count verified. If count < 2: halt, return to Stage 2, extend inventory,
re-execute Stage 3.

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
specific artifact with date. Design Impact names a specific component or contract. No field is
a fragment or a single noun phrase.

`COMMIT-STAGE-4`

---

### Stage 5 — Cluster Map

**ENTER**: All Stage 4 entries committed.

Group surprises by shared theme:

| Cluster | Surprises | Implication | Next Team / Skill |
|---------|-----------|-------------|-------------------|
| [Name] | S-N, S-M | [1 sentence] | [Named skill or specific role] |

At least one row must name a specific skill (e.g., `/trace-contract`) or role — not "investigate."

**EXIT**: All Stage 4 surprises assigned to a cluster. At least one named next step present.

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

**EXIT**: Every Stage 1 belief has a resolution row. Revision Direction column populated for
every row. Closing verdict written.

`COMMIT-STAGE-6`

---

### Output

Write to: `simulations/{topic}/{topic}-echo-{date}.md`

All 6 stages in sequence. All tokens present.

---

## V-03 — Pre-Stage Gate Sequence Map (C-15)

**Axis**: C — a complete gate topology table appears before Stage 1, enumerating every stage,
token emitted, and halt condition as a single navigable reference. No synonym mapping table. No
ENTER/EXIT contracts.

**Hypothesis**: The gate map surfaces the execution model as a single table the model can
re-consult at any stage without re-reading prior stage prose. The primary benefit is orientation
to the gate topology — which tokens gate which stages, where halts apply, what CLEAN vs FLAGGED
means — before Stage 1 introduces the substantive content. The gate map also makes
COMMIT-STAGE-3-CLEAN and COMMIT-STAGE-3-FLAGGED semantically distinct before Stage 3
instructions introduce them inline, reducing the risk of conflating them mid-execution. Over R4
V-03, this variation adds named synonym exclusions (C-17: Reliability and Performance named
explicitly) as a base mechanism, testing whether the gate map and C-17 are structurally
independent (gate map targets C-15; C-17 targets the vocabulary layer). Risk: if the model
treats the gate map as skippable preamble, C-15 passes but the orientation benefit evaporates.

---

You are executing `/topic-echo` for topic `{topic}`.

The single question this skill answers: **What did we learn that we did not expect?**

---

### Gate Sequence Overview

Read this before Stage 1. It is the complete execution model for this skill.

| Stage | Name | Emits | Halt Condition |
|-------|------|-------|----------------|
| 1 | Opening Model | `COMMIT-STAGE-1` | None — executes before any signal artifact is read |
| 2 | Signal Inventory | `COMMIT-STAGE-2` | None — always executes |
| 3 | Adversarial Gate | `GATE-CONFIRMED-[N]` or `GATE-REJECTED-[N]` per candidate; then `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED` | If GATE-CONFIRMED count < 2 after full sweep: halt, extend Stage 2, re-execute Stage 3 |
| 4 | Surprise Synthesis | `COMMIT-ENTRY-[N]` per entry; `COMMIT-STAGE-4` | Requires >=2 GATE-CONFIRMED entries from Stage 3 |
| 5 | Cluster Map | `COMMIT-STAGE-5` | None |
| 6 | Symmetric Contract Closure | `COMMIT-STAGE-6` | If any belief is FOREKNOWLEDGE-FLAGGED: halt, do not write artifact |

**Token glossary:**
- `GATE-CONFIRMED-[N]: VALID -- Stage 4.` -- entry passed all five checks; routes to Stage 4
- `GATE-REJECTED-[N]: INVALID -- Check [#]: [reason].` -- entry failed; excluded from Stage 4
- `COMMIT-STAGE-3-CLEAN` -- no Stage 2 finding was anticipated by Stage 1 beliefs
- `COMMIT-STAGE-3-FLAGGED -- [B-#] anticipated [finding].` -- one or more findings were known
- `COMMIT-ENTRY-[N]: entry committed.` -- required after each Stage 4 prose block
- `COMMIT-STAGE-1` through `COMMIT-STAGE-6` -- all six must appear in the final artifact

---

### Vocabulary

The 5 canonical epistemic dimension names:

**Feasibility · Usability · Scalability · Adoptability · Correctness**

These are the only valid names. Do not substitute. Prohibited synonyms: "Reliability" (use
Correctness), "Performance" (use Scalability), "Maintainability" (use Adoptability). Any other
term in a dimension cell is malformed — replace it before emitting the commit token for that
stage.

---

### Stage 1 — Opening Model

Before consulting any signal artifact, record the prior state:

1. **Opening model** (2–4 sentences): what the team believed about `{topic}` before investigation
   began; name the assumptions explicitly.
2. **Epistemic profile**: one row per canonical dimension — prior belief + confidence
   (HIGH / MEDIUM / LOW).
3. **Belief inventory**: >=3 falsifiable beliefs, numbered B-1 through B-N.

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
| FC-4 | Source artifact specifically named (name, namespace, date)? | VALID / INVALID |
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

**Design Impact**: [Specific component, API, contract, flow, or decision. Full sentence. Not
"the system."]

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

## V-04 — Combined: Synonym Mapping + ENTER/EXIT (C-18 + C-19)

**Axes**: A (synonym-to-canonical mapping) + B (per-stage ENTER/EXIT contracts). Formal register.
No gate map. No worked calibration example.

**Hypothesis**: These two mechanisms address adjacent structural gaps at different levels of the
execution model. The synonym mapping table (C-18) operates at the vocabulary level — it closes
the substitution loop by specifying canonical replacements, not only naming what is prohibited.
The per-stage ENTER/EXIT contracts (C-19) operate at the transition level — they convert each
stage from an instruction sequence into a verifiable state machine step. The combination is
non-redundant: a model can follow the mapping table correctly while still experiencing premature
stage transitions; a model can follow ENTER/EXIT contracts while still substituting "Reliability"
for "Correctness" in dimension cells. Both mechanisms are necessary to close their respective
gaps simultaneously. Secondary hypothesis: the EXIT criteria naming field-level completeness
requirements reinforce the canonical vocabulary rule — a Stage 1 EXIT criterion requiring all
dimension rows to be non-empty implicitly pressures the model to use correct names, since
malformed cells must be corrected (via the mapping table) before the EXIT criterion is satisfied.

---

You are executing `/topic-echo` for topic `{topic}`.

**Function**: Produce the institutional memory artifact for `{topic}`. Answer one question:
**What did this team learn that it did not expect?**

Not a summary. Not a confirmation list. A synthesis of surprises — findings that contradicted,
revised, or substantially extended the prior model. A finding that confirms a prior belief is
not a surprise and is excluded.

---

### Vocabulary Declaration

**The only valid epistemic dimension names are:**

> Feasibility · Usability · Scalability · Adoptability · Correctness

The following table maps each prohibited synonym to its canonical replacement. Use this table to
correct any malformed dimension cell before emitting the commit token for that stage:

| Prohibited term | Canonical replacement |
|----------------|----------------------|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Correctness (structural) or Feasibility (implementation) |
| Maintainability | Adoptability |
| Discoverability | Usability or Adoptability |
| Testability | Correctness or Feasibility |

A dimension cell containing any term not in the canonical list is malformed. Correct it using the
mapping table above before proceeding.

---

### Stage 1 — Opening Model

**ENTER**: No signal artifacts have been read. Record the epistemic state at investigation onset.
Prior beliefs must be captured before any artifact is consulted.

1. **Opening model** (2–4 sentences): what the team believed about `{topic}` before signals were
   gathered; name the specific assumptions that signals could contradict.

2. **Epistemic profile**: one row per canonical dimension, from the closed list only:

| Dimension | Prior Belief | Confidence |
|-----------|-------------|------------|
| Feasibility | | HIGH / MEDIUM / LOW |
| Usability | | HIGH / MEDIUM / LOW |
| Scalability | | HIGH / MEDIUM / LOW |
| Adoptability | | HIGH / MEDIUM / LOW |
| Correctness | | HIGH / MEDIUM / LOW |

3. **Belief inventory**: >=3 falsifiable beliefs, numbered B-1 through B-N. Each belief is a
   flat statement about `{topic}` that a signal artifact could contradict.

**EXIT**: All 5 dimension rows populated with non-empty prior beliefs. At least 3 beliefs
numbered. No signal artifact has been consulted. All dimension names from the canonical list
(correct malformed names using the mapping table before emitting).

`COMMIT-STAGE-1`

---

### Stage 2 — Signal Inventory

**ENTER**: Stage 1 committed. Now consult signal artifacts.

List every signal artifact for `{topic}`:

| Artifact | Namespace | Date | Primary Finding (1 sentence) |
|----------|-----------|------|------------------------------|
| | | | |

**EXIT**: All available artifacts listed. Finding column populated for every row with a complete
sentence. No artifact omitted.

`COMMIT-STAGE-2`

---

### Stage 3 — Adversarial Gate

**ENTER**: Stage 2 committed. Candidates identified from Stage 2 deviations.

For each candidate, execute the five-check table:

| Check | Test | Verdict |
|-------|------|---------|
| FC-1 | Absent from all B-# beliefs? | VALID / INVALID |
| FC-2 | Contradicts (not confirms) the opening model? | VALID / INVALID |
| FC-3 | Not predictable from domain knowledge alone? | VALID / INVALID |
| FC-4 | Source artifact specifically named (name, namespace, date)? | VALID / INVALID |
| FC-5 | Design impact non-trivial? | VALID / INVALID |

All VALID → `GATE-CONFIRMED-[N]: VALID — Stage 4.`
Any INVALID → `GATE-REJECTED-[N]: INVALID — Check [#]: [reason].`

Foreknowledge verdict (after all candidates evaluated):
- No anticipated findings: `COMMIT-STAGE-3-CLEAN`
- Any finding anticipated by Stage 1 beliefs: `COMMIT-STAGE-3-FLAGGED — [B-#] anticipated [finding].`

**EXIT**: Every candidate has a verdict token. COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED
emitted. GATE-CONFIRMED count verified. If count < 2: halt, return to Stage 2, extend inventory,
re-execute Stage 3.

---

### Stage 4 — Surprise Synthesis

**ENTER**: COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED emitted. At least 2 GATE-CONFIRMED
entries confirmed.

For each GATE-CONFIRMED entry, write a numbered prose block:

**Surprise N: [Title — 3–6 words, title case]**

**Surprise**: What was learned. Name the specific B-# contradicted or substantially extended.
Complete sentence.

**Signal Source**: Artifact name, namespace, date. One primary source per entry. "Multiple
sources" or "various artifacts" is not acceptable.

**Design Impact**: Specific component, API, contract, flow, or decision affected. Complete
sentence. "The system" or "the overall design" is not acceptable.

`COMMIT-ENTRY-[N]: entry committed.`

**EXIT per entry**: All three fields populated. Surprise field names a B-#. Signal Source names
a specific artifact with date. Design Impact names a specific component or contract. No field
is a fragment or a single noun phrase.

`COMMIT-STAGE-4`

---

### Stage 5 — Cluster Map

**ENTER**: All Stage 4 entries committed.

Group Stage 4 surprises by shared theme:

| Cluster | Surprises | Implication | Next Team / Skill |
|---------|-----------|-------------|-------------------|
| [Name] | S-N, S-M | [1 sentence] | [Named skill or specific role] |

At least one row must name a specific skill (e.g., `/flow-trigger`) or role — not "investigate."

**EXIT**: All Stage 4 surprises assigned to a cluster. At least one named next step present.

`COMMIT-STAGE-5`

---

### Stage 6 — Symmetric Contract Closure

**ENTER**: All prior stages committed.

Close the contract opened in Stage 1. For each Stage 1 belief:

| Belief | Resolution | Revision Direction | Foreknowledge |
|--------|------------|-------------------|---------------|
| B-N | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | [How the belief changed] | CLEAR / FLAGGED |

**Closing verdict** (2–4 sentences): What does the team now know that it did not know before
investigation? How does this change the design direction for `{topic}`?

Halt condition: if any row is FOREKNOWLEDGE-FLAGGED, do not write the artifact. Report the flag
and name the responsible beliefs.

**EXIT**: Every Stage 1 belief has a resolution row. Revision Direction column populated for
every row. Closing verdict written. No FOREKNOWLEDGE-FLAGGED row present (or artifact halted
and not written).

`COMMIT-STAGE-6`

---

### Output

Write to: `simulations/{topic}/{topic}-echo-{date}.md`

All 6 stages in sequence. All tokens present.

---

## V-05 — Combined: Gate Map + Synonym Mapping + ENTER/EXIT + Worked Example (C-15 + C-18 + C-19 + C-16)

**Axes**: C (gate map) + A (synonym mapping) + B (ENTER/EXIT) + worked calibration example (C-16).
Formal register.

**Hypothesis**: Each axis targets a distinct failure mode at a different layer of the execution
model:
- Gate map (C-15): prevents orientation failure — the model enters stage-by-stage instructions
  without knowing the full gate topology, causing token confusion and stage sequence errors
- Synonym mapping (C-18): prevents substitution failure — the model knows what's prohibited but
  not what to use instead, and may reach for a second non-canonical term
- ENTER/EXIT (C-19): prevents transition failure — the model advances stages prematurely or
  collapses multiple stages into one pass
- Worked example (C-16): prevents quality failure — the model produces structurally valid but
  semantically thin Stage 4 entries that satisfy format rules but not specificity standards

These failure modes are independent: any subset can occur while the others are prevented. The
gate map provides the orientation layer that makes ENTER/EXIT contracts and the synonym mapping
table self-locating — the model can re-consult the gate map at any point to confirm its position
in the execution sequence. The worked example anchors Stage 4 output quality against an
observable floor that the ENTER/EXIT EXIT criterion formalizes as a completeness gate. The
combination represents maximum coverage of the four aspirational mechanisms that individually
appeared in R3/R4 excellence signals.

---

You are executing `/topic-echo` for topic `{topic}`.

**Function**: Produce the institutional memory artifact for `{topic}`. Answer one question:
**What did this team learn that it did not expect?**

Not a summary. Not a confirmation list. A synthesis of surprises — findings that contradicted,
revised, or substantially extended the prior model. A finding that confirms a prior belief is
not a surprise and is excluded.

---

### Gate Sequence Overview

Read this before Stage 1. It is the complete execution model for this skill.

| Stage | Name | Emits | Halt Condition |
|-------|------|-------|----------------|
| 1 | Opening Model | `COMMIT-STAGE-1` | None — executes before any signal artifact is read |
| 2 | Signal Inventory | `COMMIT-STAGE-2` | None — always executes |
| 3 | Adversarial Gate | `GATE-CONFIRMED-[N]` or `GATE-REJECTED-[N]` per candidate; then `COMMIT-STAGE-3-CLEAN` or `COMMIT-STAGE-3-FLAGGED` | If GATE-CONFIRMED count < 2 after full sweep: halt, extend Stage 2, re-execute Stage 3 |
| 4 | Surprise Synthesis | `COMMIT-ENTRY-[N]` per entry; `COMMIT-STAGE-4` | Requires >=2 GATE-CONFIRMED entries from Stage 3 |
| 5 | Cluster Map | `COMMIT-STAGE-5` | None |
| 6 | Symmetric Contract Closure | `COMMIT-STAGE-6` | If any belief is FOREKNOWLEDGE-FLAGGED: halt, do not write artifact |

**Token glossary:**
- `GATE-CONFIRMED-[N]: VALID -- Stage 4.` -- entry passed all five checks; routes to Stage 4
- `GATE-REJECTED-[N]: INVALID -- Check [#]: [reason].` -- entry failed; excluded from Stage 4
- `COMMIT-STAGE-3-CLEAN` -- no Stage 2 finding was anticipated by Stage 1 beliefs
- `COMMIT-STAGE-3-FLAGGED -- [B-#] anticipated [finding].` -- one or more findings were known
- `COMMIT-ENTRY-[N]: entry committed.` -- required after each Stage 4 prose block
- `COMMIT-STAGE-1` through `COMMIT-STAGE-6` -- all six must appear in the final artifact

---

### Vocabulary Declaration

**The only valid epistemic dimension names are:**

> Feasibility · Usability · Scalability · Adoptability · Correctness

The following table maps each prohibited synonym to its canonical replacement. Use this table to
correct any malformed dimension cell before emitting the commit token for that stage:

| Prohibited term | Canonical replacement |
|----------------|----------------------|
| Reliability | Correctness |
| Performance | Scalability |
| Complexity | Correctness (structural) or Feasibility (implementation) |
| Maintainability | Adoptability |
| Discoverability | Usability or Adoptability |
| Testability | Correctness or Feasibility |

Any dimension cell containing a prohibited term is malformed. Replace it using the mapping table
above before emitting the stage commit token.

---

### Stage 1 — Opening Model

**ENTER**: No signal artifacts have been read. Record prior-state only. Prior beliefs must be
captured before any artifact is consulted.

1. **Opening model** (2–4 sentences): what the team believed about `{topic}` before investigation
   began; name the specific assumptions explicitly.

2. **Epistemic profile**: one row per canonical dimension — prior belief + confidence
   (HIGH / MEDIUM / LOW):

| Dimension | Prior Belief | Confidence |
|-----------|-------------|------------|
| Feasibility | | HIGH / MEDIUM / LOW |
| Usability | | HIGH / MEDIUM / LOW |
| Scalability | | HIGH / MEDIUM / LOW |
| Adoptability | | HIGH / MEDIUM / LOW |
| Correctness | | HIGH / MEDIUM / LOW |

3. **Belief inventory**: >=3 falsifiable beliefs, numbered B-1 through B-N.

**EXIT**: All 5 dimension rows populated with non-empty prior beliefs. At least 3 beliefs
numbered. No signal artifact consulted. All dimension names canonical (correct using mapping
table if needed before emitting).

`COMMIT-STAGE-1`

---

### Stage 2 — Signal Inventory

**ENTER**: Stage 1 committed. Now consult signal artifacts.

List all signal artifacts for `{topic}`:

| Artifact | Namespace | Date | Primary Finding (1 sentence) |
|----------|-----------|------|------------------------------|
| | | | |

**EXIT**: All available artifacts listed. Finding column populated for every row with a complete
sentence. No artifact omitted.

`COMMIT-STAGE-2`

---

### Stage 3 — Adversarial Gate

**ENTER**: Stage 2 committed. Candidates identified from Stage 2 deviations.

For each candidate, complete the five-check table:

| Check | Test | Verdict |
|-------|------|---------|
| FC-1 | Absent from Stage 1 beliefs? | VALID / INVALID |
| FC-2 | Contradicts (not confirms) the opening model? | VALID / INVALID |
| FC-3 | Not predictable from domain knowledge alone? | VALID / INVALID |
| FC-4 | Source artifact specifically named (name, namespace, date)? | VALID / INVALID |
| FC-5 | Design impact non-trivial? | VALID / INVALID |

Passing: `GATE-CONFIRMED-[N]: VALID — Stage 4.`
Failing: `GATE-REJECTED-[N]: INVALID — Check [#]: [reason].`

Foreknowledge resolution:
- All clean: `COMMIT-STAGE-3-CLEAN`
- Any anticipated by Stage 1: `COMMIT-STAGE-3-FLAGGED — [B-#] anticipated [finding].`

**EXIT**: Every candidate has a verdict token. COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED
emitted. Refer to the Gate Sequence Overview for the halt condition if GATE-CONFIRMED count < 2.

---

### Stage 4 — Surprise Synthesis

**ENTER**: COMMIT-STAGE-3-CLEAN or COMMIT-STAGE-3-FLAGGED emitted. At least 2 GATE-CONFIRMED
entries confirmed.

**Calibration example** — this is a worked instance, not a template. It defines the quality
floor. Every Stage 4 entry you write must be at or above this bar for Signal Source specificity
and Design Impact concreteness:

> **Surprise 0: Namespace Isolation Blocks Cross-Signal Composition**
>
> **Surprise**: We assumed signal artifacts from different namespaces could be retrieved in a
> single composite query, enabling `/topic-story` to assemble `scout` and `trace` evidence in
> one pass (contradicts B-3). The `topic-registry-trace-contract-2026-02-14.md` artifact
> revealed that the registry enforces namespace partitioning as a hard contract boundary —
> cross-namespace reads are not supported in the current contract model.
>
> **Signal Source**: `topic-registry-trace-contract-2026-02-14.md`, trace namespace, 2026-02-14.
>
> **Design Impact**: The `/topic-story` skill must issue sequential per-namespace reads and
> merge results client-side; the single-query assumption must be removed from the skill contract
> before implementation begins.

For each GATE-CONFIRMED candidate, write a numbered prose block at or above the calibration bar:

**Surprise N: [Title — 3–6 words, title case]**

**Surprise**: What was learned. Name the specific B-# contradicted or substantially extended.
Complete sentence.

**Signal Source**: Artifact name, namespace, date. One primary source per entry. "Multiple
sources" or "various artifacts" is not acceptable.

**Design Impact**: Specific component, API, contract, flow, or decision affected. Complete
sentence. "The system" or "the overall design" is not acceptable.

`COMMIT-ENTRY-[N]: entry committed.`

**EXIT per entry**: All three fields populated. Surprise names a B-#. Signal Source names a
specific artifact with date. Design Impact names a specific component or contract. No field
is a fragment or a single noun phrase.

`COMMIT-STAGE-4`

---

### Stage 5 — Cluster Map

**ENTER**: All Stage 4 entries committed.

Group Stage 4 surprises by shared theme or implication:

| Cluster | Surprises | Implication | Next Team / Skill |
|---------|-----------|-------------|-------------------|
| [Name] | S-N, S-M | [1 sentence] | [Named skill or specific role] |

At least one row must name a specific skill (e.g., `/flow-trigger`) or role — not "investigate."

**EXIT**: All Stage 4 surprises assigned to a cluster. At least one named next step present.

`COMMIT-STAGE-5`

---

### Stage 6 — Symmetric Contract Closure

**ENTER**: All prior stages committed.

Close the contract opened in Stage 1. For each Stage 1 belief:

| Belief | Resolution | Revision Direction | Foreknowledge |
|--------|------------|-------------------|---------------|
| B-N | COHERENT / CONTRADICTORY / FOREKNOWLEDGE-FLAGGED | [How the belief changed] | CLEAR / FLAGGED |

**Closing verdict** (2–4 sentences): What does the team now know that it did not know before
investigation? How does this change the design direction for `{topic}`?

Halt condition: if any row is FOREKNOWLEDGE-FLAGGED, do not write the artifact. Report the flag
and name the responsible beliefs.

Refer to the Gate Sequence Overview for the FOREKNOWLEDGE-FLAGGED halt condition.

**EXIT**: Every Stage 1 belief has a resolution row. Revision Direction column populated for
every row. Closing verdict written.

`COMMIT-STAGE-6`

---

### Output

Write to: `simulations/{topic}/{topic}-echo-{date}.md`

All 6 stages in sequence. All tokens present.
