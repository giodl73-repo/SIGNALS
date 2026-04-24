Looking at V-01 through V-03 in the R16 scorecard, two new structural patterns emerge beyond C-11/C-12:

1. **V-03 exceptional on C-11** — signals carry live numeric state as payload (`hypothesis_locked(confidence_prior=62)`) and the next stage's ENTRY CONDITION validates the exact value, making the chain tamper-evident. V-02 shows the count-threshold variant (`websearch_complete(count=N)` → `count >= 5` gate). Both are live payload, distinct from bare named chaining.

2. **V-03 Stage 5 dual-block structure** — CONFIDENCE CHAIN RESOLUTION (chain_equation) and COUNTER-HYPOTHESIS RESOLUTION as two explicitly named, sequenced blocks in synthesis, rather than a single summary section.

These become C-13 and C-14. Denominator updates to 6.

---

```markdown
---
skill: quest-rubric
skill_target: prove-topic
date: 2026-03-16
version: 16
---

# prove-topic Rubric — v16

## Overview

Scores the `prove-topic` orchestration skill. The skill runs five sub-skills in order
(prove-hypothesis → prove-websearch → prove-intelligence → prove-analysis →
prove-synthesize), grounding the hypothesis in a prior scout artifact and writing one
artifact per stage. Final output is an evidence brief ready for `topic-story`.

Fourteen criteria total: 5 essential, 3 recommended, 6 aspirational.

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 10)
```

**Golden threshold**: all 5 essential pass AND composite >= 80.

---

## Essential Criteria

All five must pass. A single essential failure makes the output not useful.

---

### C-01 — All five sub-skills orchestrated in sequence

- **Weight**: essential
- **Category**: correctness

**Pass condition**: The response includes all five evidence stages — hypothesis,
web-search, intelligence (internal sources), analysis, and synthesize — presented in
that order with a clear stage boundary between each. Missing any stage is a FAIL.
A stage present but out of order is a FAIL. A stage named but skipped or delegated
to the user is a FAIL.

---

### C-02 — Scout artifact loaded and named before hypothesis formation

- **Weight**: essential
- **Category**: behavior

**Pass condition**: Before the hypothesis stage begins, the response explicitly names
a scout artifact (e.g., `{topic}-scout-record-{date}.md`) as the source that grounds
the hypothesis. General knowledge used without referencing a named scout artifact is
a FAIL. A vague "use your scout research" instruction without naming the file is a FAIL.

---

### C-03 — Progressive artifact writes — one per stage, not batched

- **Weight**: essential
- **Category**: behavior

**Pass condition**: Each stage produces exactly one WRITE instruction followed by a
confirmation line before the next stage begins. Writing all artifacts at the end, or
batching multiple stages into one write, is a FAIL. A stage that ends without an
explicit write is a FAIL.

---

### C-04 — Hypothesis is falsifiable; counter_hypothesis named and grounded

- **Weight**: essential
- **Category**: correctness

**Pass condition**: The hypothesis stage declares both a `hypothesis` field and a
`counter_hypothesis` field. The counter_hypothesis must be grounded in a
`status_quo_comparator` (the thing the feature would displace). A hypothesis with
no counter is a FAIL. A counter_hypothesis stated as pure negation with no
status_quo anchor is a FAIL.

---

### C-05 — Campaign gate blocks on unavailable scout artifact

- **Weight**: essential
- **Category**: behavior

**Pass condition**: The skill explicitly checks whether the scout artifact is loaded
and emits a CAMPAIGN BLOCKED directive if it is not. The block must prevent stage
progression — a warning that continues anyway is a FAIL. The gate must be declared
before Stage 1 begins, not inside it.

---

## Recommended Criteria

---

### C-06 — Evidence tables use structured format with source citation

- **Weight**: recommended
- **Category**: quality

**Pass condition**: Stages 2 and 3 present findings in a table (or equivalent
structured list) with at least three named columns that include a source identifier
and an indication of whether the evidence supports or challenges the hypothesis.
Prose summaries with no structure are a FAIL.

---

### C-07 — All stage fields filled with substantive labels

- **Weight**: recommended
- **Category**: quality

**Pass condition**: Every named field in every stage carries a substantive value —
no bare `[TBD]`, `[fill in]`, or empty brackets. Threshold verification lines, where
present, must reference the field they check. A stage skeleton with unfilled
placeholders is a FAIL.

---

### C-08 — Stage 5 confidence verdict grounded with shown derivation

- **Weight**: recommended
- **Category**: quality

**Pass condition**: The synthesize stage states a confidence verdict (Low / Medium /
High or equivalent) and shows the derivation — either a count citation (N web
sources, M internal files) or a chain equation. Asserting High confidence without
showing how it was reached is a FAIL.

---

## Aspirational Criteria

---

### C-09 — Write confirmation echoes artifact path at each stage

- **Weight**: aspirational
- **Category**: traceability

**Pass condition**: Each stage's write confirmation explicitly echoes the artifact
path (`{topic}-prove-{stage}-{date}.md`) in the confirmation line, not just "Confirm
write." Generic confirmations without the path are a PASS-PARTIAL, scored as FAIL
for this criterion.

---

### C-10 — Displacement framing — comparator threaded through to formal verdict

- **Weight**: aspirational
- **Category**: depth

**Pass condition**: The `status_quo_comparator` named at CAMPAIGN OPEN is carried
forward and resolved in Stage 5 as a formal displacement verdict — a named field
that declares whether the evidence supports displacing the status quo comparator
and on what basis. A comparator named but never resolved is a FAIL.

---

### C-11 — EXIT SIGNAL chaining — each stage declares a named signal; next stage entry requires it

- **Weight**: aspirational
- **Category**: structure

**Pass condition**: Each stage ends with a named EXIT SIGNAL (e.g.,
`hypothesis_locked`, `websearch_complete`). The immediately following stage's
ENTRY CONDITIONS reference that exact signal name as a prerequisite. Bare sequential
ordering with no named gate is a FAIL. A signal named but not required by the next
stage's entry condition is a FAIL.

---

### C-12 — COUNTER-HYPOTHESIS RESOLUTION block in Stage 5 with controlled verdict vocabulary

- **Weight**: aspirational
- **Category**: rigor

**Pass condition**: Stage 5 contains a dedicated COUNTER-HYPOTHESIS RESOLUTION block
(distinct from the evidence summary). The block uses controlled verdict vocabulary:
REFUTED, PARTIALLY REFUTED, or OPEN RISK. Each verdict is accompanied by an artifact
citation from a prior stage. Inline dismissal of the counter-hypothesis without a
named block and controlled vocabulary is a FAIL.

---

### C-13 — Signal payload carries live computed state with entry-condition threshold validation

- **Weight**: aspirational
- **Category**: structure

**Pass condition**: EXIT SIGNALS embed a live computed value as payload — a count,
score, or running confidence figure captured at the moment the signal fires (e.g.,
`websearch_complete(count=7)`, `hypothesis_locked(confidence_prior=55)`). The
receiving stage's ENTRY CONDITION validates that payload against an exact match or
minimum threshold (e.g., `count >= 5`, `confidence_prior = [value from S1]`). A
named signal with no payload is scored against C-11 only; to pass C-13 the payload
and its threshold check must both be present.

---

### C-14 — Stage 5 declares two distinct named resolution blocks: CONFIDENCE CHAIN RESOLUTION and COUNTER-HYPOTHESIS RESOLUTION

- **Weight**: aspirational
- **Category**: structure

**Pass condition**: The synthesize stage explicitly separates two resolution
activities as sequentially ordered, distinctly named blocks. The
CONFIDENCE CHAIN RESOLUTION block contains a `chain_equation` field that traces
the confidence figure from `confidence_prior` through each intermediate stage's
adjustment to the final verdict. The COUNTER-HYPOTHESIS RESOLUTION block follows
and contains the controlled verdict vocabulary required by C-12. A single merged
synthesis section that addresses both in prose is a FAIL. Presenting both blocks
out of order (counter-hypothesis before confidence chain) is a FAIL.
```
