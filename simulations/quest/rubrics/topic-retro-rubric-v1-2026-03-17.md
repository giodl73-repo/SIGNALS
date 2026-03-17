---
skill: quest-rubric
skill_target: topic-retro
date: 2026-03-17
version: 1
---

# Scoring Rubric: topic-retro

Post-commitment retrospective on a topic's signals. Evaluates whether the output delivers
structured retrospective value: what signals were gathered, which predictions held, which
failed, what gaps mattered, and the one unexpected finding (the Echo).

---

## Essential Criteria (60 points total)

### C-01 — Signal Accuracy Section Present
- **Weight**: essential
- **Category**: correctness
- **Text**: The output contains a Signal Accuracy section that explicitly compares predicted
  outcomes against actual outcomes for at least the primary signals gathered during the topic.
- **Pass condition**: A named section (or clearly labelled block) lists at least one signal
  by name, states what was predicted, and states what actually occurred. Both prediction and
  actual must be present — a list of signals without the comparison fails.

### C-02 — Correct/Wrong Verdict Per Signal
- **Weight**: essential
- **Category**: correctness
- **Text**: Each signal in the accuracy section receives an explicit verdict (correct,
  partially correct, or wrong), not just a description. Verdicts must be directionally
  unambiguous.
- **Pass condition**: Every signal entry in the accuracy section carries a verdict label or
  equivalent marker. Vague language ("somewhat aligned", "generally matched") without a
  clear verdict fails.

### C-03 — Gaps Section Present and Actionable
- **Weight**: essential
- **Category**: coverage
- **Text**: The output contains a Gaps section that identifies signals that were not gathered
  but, if they had been, would have changed or strengthened the go/no-go decision.
- **Pass condition**: At least one gap is named and accompanied by a statement of how it
  would have affected the decision. A gap listed without decision impact fails. An empty
  Gaps section ("no gaps identified") fails unless the reasoning for completeness is explicit.

### C-04 — Echo Present (One Unexpected Finding)
- **Weight**: essential
- **Category**: depth
- **Text**: The output contains an Echo section identifying the single most unexpected thing
  learned — something that was not predicted by any gathered signal. This is the core
  retrospective signal for improving future signal quality.
- **Pass condition**: Exactly one Echo is named. It must be framed as unexpected (not a
  restatement of a wrong prediction) and must carry enough context for a reader to act on it
  in a future topic. Multiple echoes or an echo that is simply a restatement of a failed
  prediction fails.

### C-05 — Topic and Commitment Context Established
- **Weight**: essential
- **Category**: correctness
- **Text**: The output names the topic under review and identifies the commitment that was
  made (shipped feature, decision taken, spec approved, etc.) so the retrospective is anchored
  to a specific event.
- **Pass condition**: Topic name and the nature of the commitment are stated within the first
  two sections (or in a header/preamble). A retrospective with no anchor event fails.

---

## Recommended Criteria (30 points total)

### C-06 — Signal Coverage Summary
- **Weight**: recommended
- **Category**: coverage
- **Text**: The output includes a summary of which signal namespaces were exercised versus
  which were absent, giving the reader a quick completeness picture across the nine signal
  types (scout, draft, review, flow, trace, prove, listen, program, topic).
- **Pass condition**: A summary (table, list, or prose) indicates namespace coverage. At
  minimum it distinguishes "signals gathered" from "signals absent". Mentioning only the
  signals that were gathered without acknowledging absence fails.

### C-07 — Improvement Recommendation Tied to Gaps or Echo
- **Weight**: recommended
- **Category**: depth
- **Text**: The output concludes with at least one concrete recommendation for improving
  signal quality on future topics, derived directly from the identified gaps or the Echo —
  not generic advice.
- **Pass condition**: A recommendation names the specific gap or Echo it addresses and
  specifies a change to signal gathering practice (e.g., "run scout-feasibility before
  committing to timeline" not "gather more signals next time").

### C-08 — Accuracy Rate or Ratio Stated
- **Weight**: recommended
- **Category**: format
- **Text**: The output quantifies signal accuracy as a ratio or rate (e.g., "4 of 6 signals
  correct", "67% accuracy") to give a scannable quality indicator without requiring the
  reader to count manually.
- **Pass condition**: A numerical accuracy summary appears in the Signal Accuracy section or
  immediately following it. Purely qualitative summaries without any count or percentage fail
  this criterion.

---

## Aspirational Criteria (10 points total)

### C-09 — Echo Linked to Systemic Pattern
- **Weight**: aspirational
- **Category**: depth
- **Text**: The Echo is not treated as an isolated anomaly but is connected to a broader
  pattern — either a known limitation of a signal type, a recurring blind spot across past
  topics, or a structural gap in the plugin's current namespace coverage.
- **Pass condition**: The Echo section (or a commentary following it) explicitly names the
  pattern or prior instance, not just the current observation. An Echo treated as a one-off
  without pattern linkage fails this criterion.

### C-10 — AMEND Variants Handled Correctly
- **Weight**: aspirational
- **Category**: behavior
- **Text**: When the skill is invoked with an AMEND modifier (focus on specific signal type,
  or adjusted time window), the output correctly scopes its analysis to the amendment without
  losing the structural skeleton (all three sections still present, even if narrowed).
- **Pass condition**: If an AMEND argument is provided, the amended scope is named in the
  preamble and the analysis stays within that scope. If no AMEND is provided, this criterion
  is evaluated as not applicable (does not penalize). An AMEND invocation that ignores the
  scope or drops required sections fails.

---

## Scoring Formula

```
composite = (essential_pass / 5 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 5 essential criteria pass AND composite >= 80.

| Band | Composite | Meaning |
|------|-----------|---------|
| Gold | >= 80, all essential pass | Retrospective is trustworthy and actionable |
| Silver | >= 65, all essential pass | Useful but missing depth or coverage |
| Bronze | >= 50, all essential pass | Structurally valid, thin on insight |
| Fail | any essential fails | Output is not a valid retrospective |

---

## Notes for Evaluators

- C-01 through C-04 form the structural skeleton. A response missing any of the three named
  sections (Signal Accuracy, Gaps, Echo) automatically fails the corresponding essential.
- C-04 (Echo) is intentionally strict: the unexpected finding must be genuinely unpredicted.
  If a signal predicted X and X did not happen, that is a wrong prediction (C-02), not an
  Echo. The Echo is something no signal was even pointing at.
- C-10 is only scored when an AMEND modifier is present in the invocation. Absence of AMEND
  should be recorded as N/A and the aspirational points redistributed to C-09 for scoring
  purposes (i.e., treat aspirational as 10 points from C-09 alone).
