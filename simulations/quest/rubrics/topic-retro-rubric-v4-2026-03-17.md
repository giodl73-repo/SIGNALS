Looking at the Round 5 scorecard, two new excellence patterns emerge:

1. **C-09 PARTIAL (both variations)** — "Why unpredicted" field is present but neither variation explicitly requires naming a *repeating systemic failure mode*. V-01 would have passed if it demanded a named pattern, not just an explanation.

2. **V-02 truncation creates scoring uncertainty on Phase 4** — when a phase is cut off, required fields become unverifiable. V-01's table-dominant structure avoids this because each row is self-contained. The excellence signal is phases that cannot silently defer required fields.

These become **C-18** and **C-19**.

---

```markdown
---
skill: quest-rubric
skill_target: topic-retro
date: 2026-03-17
version: 4
prior_version: topic-retro-rubric-v3-2026-03-17.md
changes: |
  Round 5 excellence signals promoted to aspirational criteria.
  C-18: echo-systemic-pattern-named
  C-19: phase-completion-self-contained
  Total available updated from 108 to 112 (2 new criteria × 2 pts each).
---

# Scoring Rubric: topic-retro (v4)

Post-commitment retrospective on a topic's signals. Evaluates whether the output delivers
structured retrospective value: what signals were gathered, which predictions held, which
failed, what gaps mattered, and the one unexpected finding (the Echo).

---

## Essential Criteria (60 points total)

### C-01 — Signal Accuracy Section Present
- **Weight**: essential  **Category**: correctness
- **Pass condition**: Named section lists at least one signal by name with both prediction and
  actual outcome. List without the comparison fails.

### C-02 — Correct/Wrong Verdict Per Signal
- **Weight**: essential  **Category**: correctness
- **Pass condition**: Every signal carries a verdict label. Vague language without a clear
  verdict fails.

### C-03 — Gaps Section Present and Actionable
- **Weight**: essential  **Category**: coverage
- **Pass condition**: At least one gap named with decision-impact statement. Gap without impact
  fails.

### C-04 — Echo Present (One Unexpected Finding)
- **Weight**: essential  **Category**: depth
- **Pass condition**: Exactly one Echo, framed as unpredicted (not a restatement of a wrong
  prediction). Multiple echoes or restatements fail.

### C-05 — Topic and Commitment Context Established
- **Weight**: essential  **Category**: correctness
- **Pass condition**: Topic name and commitment nature stated in first two sections.

---

## Recommended Criteria (30 points total)

### C-06 — Signal Coverage Summary
- **Weight**: recommended  **Category**: coverage
- **Pass condition**: Summary distinguishes "signals gathered" from "signals absent" across all
  9 namespaces.

### C-07 — Improvement Recommendation Tied to Gaps or Echo
- **Weight**: recommended  **Category**: depth
- **Pass condition**: Recommendation names the specific gap or Echo it addresses and specifies
  a practice change.

### C-08 — Accuracy Rate or Ratio Stated
- **Weight**: recommended  **Category**: format
- **Pass condition**: Numerical accuracy summary (ratio or percentage) present in or
  immediately following the Signal Accuracy section.

---

## Aspirational Criteria (22 points total)

### C-09 — Echo Linked to Systemic Pattern *(baseline)*
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: Echo includes a "Why unpredicted" explanation that references a
  recurring failure mode, not just the specific instance. Generic surprise does not pass.

### C-10 — Prediction Specificity (Measurable Expected Value)
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: Predictions in the accuracy section state a measurable or falsifiable
  expectation. Vague claims ("this will help") fail; specific expected behaviors or thresholds
  pass.

### C-11 — Gap Decision-Impact Ranked
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: Gaps are ranked or marked by decision-impact severity. A flat list
  without severity ordering fails.

### C-12 — Signal Count Matches Commitment Scope
- **Weight**: aspirational  **Category**: coverage
- **Pass condition**: The count of assessed signals plausibly matches the commitment scope.
  A 3-namespace feature with signals only from 1 namespace fails the plausibility check.

### C-13 — Commitment Outcome Explicitly Stated
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: What actually happened to the commitment (shipped, cancelled, pivoted,
  deferred) is stated in the opening context section.

### C-14 — verdict-label-explicit-not-prose *(Round 2)*
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Verdict is a named column or field constrained to an enumerated set
  (CORRECT / WRONG / PARTIAL). Prose-embedded verdict where the label can be omitted fails.

### C-15 — accuracy-ratio-not-count *(Round 2)*
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Accuracy summary states N correct / M total = X%. A bare count without
  the ratio and percentage fails.

### C-16 — namespace-coverage-table-not-implied *(Round 2)*
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Namespace coverage is a table with explicit rows for all 9 namespaces.
  Prose headers or structural implication without a table fail.

### C-17 — recommendation-addresses-template *(Round 2)*
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Recommendation uses the exact template:
  > **Recommendation**: Addresses [Gap: name / Echo] by [specific practice change].
  Free-form prose without the template structure fails.

### C-18 — echo-systemic-pattern-named *(Round 5)*
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: The Echo names a repeating systemic failure mode, not just explains why
  this instance was unpredicted. Must use a named-pattern structure:
  > **Pattern**: [name] — [description of recurring failure mode].
  A "Why unpredicted" explanation without a named pattern fails.

### C-19 — phase-completion-self-contained *(Round 5)*
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Every required phase or section delivers all its required fields within
  a single continuous pass. No phase may defer required content to a continuation turn.
  Any phase whose required fields are unverifiable due to truncation or deferral fails.

---

## Scoring Summary

| Tier | Criteria | Points Each | Total |
|------|----------|-------------|-------|
| Essential | C-01–C-05 | 12 | 60 |
| Recommended | C-06–C-08 | 10 | 30 |
| Aspirational (baseline) | C-09–C-13 | 2 | 10 |
| Aspirational (Round 2) | C-14–C-17 | 2 | 8 |
| Aspirational (Round 5) | C-18–C-19 | 2 | 4 |
| **Total** | | | **112** |
```
