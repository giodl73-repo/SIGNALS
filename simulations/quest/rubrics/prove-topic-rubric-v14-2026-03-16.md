---
skill: quest-rubric
skill_target: prove-topic
date: 2026-03-16
version: 14
---

# prove-topic Rubric — v14

## Overview

Scores the `prove-topic` orchestration skill. The skill runs five sub-skills in order
(prove-hypothesis → prove-websearch → prove-intelligence → prove-analysis →
prove-synthesize), grounding the hypothesis in a prior scout artifact and writing one
artifact per stage. Final output is an evidence brief ready for `topic-story`.

Ten criteria total: 5 essential, 3 recommended, 2 aspirational.

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
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

**Pass condition**: The synthesis stage (Stage 5) includes an explicit statement
confirming the evidence brief is ready for the downstream consumer — e.g., "Evidence
brief ready for topic-story." A synthesis that ends without naming the next step or
downstream artifact is a FAIL. A generic "done" or "complete" without naming
`topic-story` is a PARTIAL (30 pts, counts as fail for golden threshold).

---

### C-05 — Artifact paths follow {topic}-{signal}-{date}.md on every write instruction

- **Weight**: essential
- **Category**: format

**Pass condition**: Every write instruction in the response names the full artifact
path — `{topic}-hypothesis-{date}.md`, `{topic}-websearch-{date}.md`, etc. — not just
a prefix defined once at session open. A prefix defined at campaign open but omitted
from individual write instructions is a PARTIAL (30 pts, counts as fail for golden
threshold). Per-instruction path naming in each of the five stages is full PASS.

---

## Recommended Criteria

Output is meaningfully better when these pass.

---

### C-06 — Stage order is forward-only with a gate before Stage 1

- **Weight**: recommended
- **Category**: behavior

**Pass condition**: The response enforces a forward-only sequence with an explicit
gate block (or equivalent checkpoint) that must clear before hypothesis formation
begins. Arbitrary stage reordering, absence of any gate structure, or a gate that
allows bypassing if the scout artifact is absent are all FAIL. The gate must reference
scout-artifact presence as a required condition.

---

### C-07 — Scout signal handoff carries a named anchor into the hypothesis artifact

- **Weight**: recommended
- **Category**: coverage

**Pass condition**: The hypothesis artifact or its frontmatter includes a named field
linking back to the scout artifact used (e.g., `scout_source: {topic}-scout-record-{date}.md`).
The hypothesis artifact alone knowing its own source — not just the campaign preamble —
is the standard. Named anchor present in preamble only is a PARTIAL (10 pts).

---

### C-08 — Evidence gaps and thin findings flagged at point of discovery

- **Weight**: recommended
- **Category**: depth

**Pass condition**: When any evidence stage (web-search, intelligence, analysis) yields
thin, conflicting, or absent evidence, the response flags it at that stage — not only
in the synthesis. A flag at a specific stage that is also carried into the synthesis
is full PASS. A synthesis that mentions thin evidence without any per-stage flag is a
PARTIAL (10 pts). Silence about evidence quality throughout is a FAIL.

---

## Aspirational Criteria

Raise the bar once essential and recommended are stable.

---

### C-09 — Thin-evidence findings propagate to synthesis with confidence qualification

- **Weight**: aspirational
- **Category**: depth

**Pass condition**: If any stage flags thin or conflicting evidence (satisfying C-08),
the synthesis explicitly names that finding, identifies which claim it weakens, and
adjusts the confidence signal accordingly. A synthesis that mentions thin evidence
generally without tracing it to a specific claim is a PARTIAL (5 pts). Full PASS
requires the confidence qualification to name the source stage and the weakened claim.

---

### C-10 — Hypothesis entry is structurally blocked until scout confirmation is recorded

- **Weight**: aspirational
- **Category**: behavior

**Pass condition**: The response includes a structural block — not just a named anchor —
that prevents hypothesis work from proceeding until the scout artifact is explicitly
confirmed present. Examples: a GATE block with a required checkbox before Stage 1
opens, an "abort here if scout-record is absent" instruction with no fallback, or a
required `gate_cleared: true` field in the hypothesis frontmatter that cannot be
pre-populated. A named scout anchor (satisfying C-02) without a blocking gate is
insufficient for C-10. Full PASS requires the gate to make non-compliance visible
before the hypothesis section opens.

---

## Score Sheet

| ID   | Description                                   | Weight        | Result | Points |
|------|-----------------------------------------------|---------------|--------|--------|
| C-01 | All five sub-skills orchestrated in sequence  | essential     |        |        |
| C-02 | Scout artifact loaded and named before hyp.   | essential     |        |        |
| C-03 | Progressive artifact writes — one per stage   | essential     |        |        |
| C-04 | Synthesis signals readiness for topic-story   | essential     |        |        |
| C-05 | Artifact paths named on every write instr.    | essential     |        |        |
| C-06 | Forward-only stage order with gate block      | recommended   |        |        |
| C-07 | Scout anchor in hypothesis artifact           | recommended   |        |        |
| C-08 | Evidence gaps flagged at point of discovery   | recommended   |        |        |
| C-09 | Thin-evidence propagates to synthesis         | aspirational  |        |        |
| C-10 | Hypothesis structurally blocked until scout   | aspirational  |        |        |

**Essential pass count**: __ / 5
**Recommended pass count**: __ / 3
**Aspirational pass count**: __ / 2

**Composite**: `(__ / 5 * 60) + (__ / 3 * 30) + (__ / 2 * 10)` = __

**Golden**: all essential PASS and composite >= 80? [ ] YES  [ ] NO
