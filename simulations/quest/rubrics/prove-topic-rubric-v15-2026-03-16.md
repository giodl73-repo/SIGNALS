Reading the scorecard carefully to identify the new excellence patterns before writing v15.

The Round 15 scorecard surfaces two new patterns not captured in any existing C-09/C-10 aspirational slot:

1. **EXIT SIGNAL chaining** (V-03, V-05 excel) — each stage declares a named EXIT SIGNAL and the *next* stage's ENTRY CONDITION requires that signal by name, transforming sequential ordering from narrative instruction into structural gate.

2. **Counter-hypothesis resolved in Stage 5 with controlled verdict vocabulary** (V-03, V-05 pass; V-01, V-02 fail; V-04 partial) — dedicated COUNTER-HYPOTHESIS RESOLUTION block in synthesis with REFUTED / PARTIALLY REFUTED / OPEN RISK vocabulary and artifact citation.

These become C-11 and C-12. Scoring formula updates to `aspirational_pass / 4 * 10`.

---

```markdown
---
skill: quest-rubric
skill_target: prove-topic
date: 2026-03-16
version: 15
---

# prove-topic Rubric — v15

## Overview

Scores the `prove-topic` orchestration skill. The skill runs five sub-skills in order
(prove-hypothesis → prove-websearch → prove-intelligence → prove-analysis →
prove-synthesize), grounding the hypothesis in a prior scout artifact and writing one
artifact per stage. Final output is an evidence brief ready for `topic-story`.

Twelve criteria total: 5 essential, 3 recommended, 4 aspirational.

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 4 * 10)
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

**Pass condition**: At least one write instruction is issued per stage, producing a
distinct artifact at each step: hypothesis artifact, web-search summary, intelligence
summary, analysis artifact, and synthesis brief. A response that collects all evidence
then writes a single artifact at Stage 5 is a FAIL. Five write instructions with
matching artifact names is the exemplar.

---

### C-04 — Synthesis explicitly signals readiness for topic-story

- **Weight**: essential
- **Category**: correctness

**Pass condition**: Stage 5 synthesis ends with an explicit readiness handoff. The
phrase "Evidence brief complete. Ready for /topic-story." (or a semantically
equivalent forward-handoff line) must appear as the stage's named exit signal.
A synthesis that concludes without naming the next destination skill is a FAIL.
A synthesis that lists the next step as a user instruction ("you should now run
/topic-story") rather than an embedded exit line is a FAIL.

---

### C-05 — Counter-hypothesis formed in Stage 1

- **Weight**: essential
- **Category**: correctness

**Pass condition**: Stage 1 (prove-hypothesis) produces a named counter-hypothesis
alongside the primary hypothesis — a testable opposing claim, not a generic risk
list. The counter-hypothesis must be recorded in the Stage 1 artifact as a distinct
field or labeled section. A Stage 1 that lists only the primary hypothesis with no
counter position is a FAIL. A "risks" or "limitations" list that does not identify a
falsifiable opposing claim is a FAIL.

---

## Recommended Criteria

Three recommended criteria. Each missed recommended criterion reduces the composite
score but does not alone block golden status.

---

### C-06 — Campaign halts if scout artifact not found

- **Weight**: recommended
- **Category**: behavior

**Pass condition**: If the scout artifact cannot be located, the skill halts the
entire campaign and records which file path was searched. Proceeding to Stage 1
without a confirmed scout artifact is a FAIL. A warning that does not block execution
is a FAIL.

---

### C-07 — Cross-stage evidence alignment tracked

- **Weight**: recommended
- **Category**: correctness

**Pass condition**: At least one stage (typically Stage 3 or Stage 4) produces an
explicit alignment field or section — e.g., `s3_alignment: ALIGNED / CONTRADICTS /
MIXED` — comparing internal intelligence against the web-search findings. A skill
that gathers both external and internal evidence but never surfaces their relationship
is a FAIL for this criterion.

---

### C-08 — Artifact paths follow naming convention throughout

- **Weight**: recommended
- **Category**: correctness

**Pass condition**: Every write instruction uses the canonical artifact naming pattern
`{topic}-{signal}-{date}.md` stored under `simulations/{namespace}/{skill}/`. An
artifact written to an ad-hoc path or named without the topic prefix is a FAIL for
this criterion.

---

## Aspirational Criteria

Four aspirational criteria. Distinguish exemplary responses from merely correct
ones. All four passing indicates a reference-quality implementation.

---

### C-09 — Per-stage displacement/inertia framing

- **Weight**: aspirational
- **Category**: depth

**Pass condition**: Each stage explicitly frames its finding in terms of how it
shifts or sustains the hypothesis — e.g., a displacement score, an inertia
qualifier, or an explicit "this stage moves the needle by X because Y" statement.
Stages that report findings without connecting them to hypothesis trajectory do not
meet this criterion.

---

### C-10 — Numerical confidence scoring with explicit calculation

- **Weight**: aspirational
- **Category**: depth

**Pass condition**: The synthesis (Stage 5) or analysis (Stage 4) includes a
numerical confidence score (e.g., 0–10 or percentage) with an explicit derivation
showing how the per-stage evidence combined to produce it. A bare number without
calculation logic does not meet this criterion.

---

### C-11 — EXIT SIGNAL chaining enforces stage order structurally

- **Weight**: aspirational
- **Category**: behavior
- **First observed**: Round 15 (V-03, V-05)

**Pass condition**: Each stage declares a named EXIT SIGNAL (e.g.,
`hypothesis_locked`, `websearch_complete`, `intelligence_complete`,
`analysis_complete`, `synthesis_complete`), and the following stage's ENTRY
CONDITION explicitly requires that signal by name before it may proceed. The
sequence constraint is structural — not merely narrative. A skill that lists the
correct order in prose but does not gate each stage on the prior stage's EXIT SIGNAL
does not meet this criterion. Five EXIT SIGNALs with five matching ENTRY CONDITIONS
is the exemplar.

---

### C-12 — Counter-hypothesis resolved in Stage 5 with controlled verdict vocabulary

- **Weight**: aspirational
- **Category**: correctness
- **First observed**: Round 15 (V-03, V-05)

**Pass condition**: Stage 5 synthesis includes a dedicated COUNTER-HYPOTHESIS
RESOLUTION block that closes the loop opened in Stage 1. The resolution verdict must
use controlled vocabulary — exactly one of: **REFUTED**, **PARTIALLY REFUTED**, or
**OPEN RISK** — accompanied by a `resolution_evidence` field citing the specific
stage artifact(s) that justify the verdict. A Stage 5 that returns a
`hypothesis_verdict` without separately resolving the counter-hypothesis does not
meet this criterion. A verdict not drawn from the three-value vocabulary does not
meet this criterion. Counter-hypothesis resolved in Stage 4 rather than Stage 5 is a
FAIL (wrong stage).
```
