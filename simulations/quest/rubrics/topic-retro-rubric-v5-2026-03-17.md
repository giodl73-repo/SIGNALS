Reading the Round 6 scorecard carefully before writing the rubric.

Two excellence signals are visible in the V-01 scoring:

1. **C-13 FAIL** — The reason is precise: "Would have surfaced" names *outcomes*, not the *assumption held without evidence*. The gap table has no column for the inertia belief. That's a structural absence, not just a missing field.

2. **C-19 PARTIAL + V-02 "Phase-Seal" design** — V-01's table rows are self-contained but non-tabular phases (6, 8) can silently truncate. V-02 responds with per-phase seals that *name required fields and confirm them explicitly* — stronger than structural row self-containment.

These become **C-20** (gap-inertia-assumption-named) and **C-21** (phase-seal-explicit).

---

```markdown
---
skill: quest-rubric
skill_target: topic-retro
date: 2026-03-17
version: 5
prior_version: topic-retro-rubric-v4-2026-03-17.md
changes: |
  Round 6 excellence signals promoted to aspirational criteria.
  C-20: gap-inertia-assumption-named
  C-21: phase-seal-explicit
  Total available updated from 112 to 116 (2 new criteria × 2 pts each).
---

# Scoring Rubric: topic-retro (v5)

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

## Aspirational Criteria (26 points total)

### C-09 — Echo Linked to Systemic Pattern
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: Echo section connects the unexpected finding to a broader pattern of
  failure, not just the isolated instance. (2 pts full / 1 pt partial)

### C-10 — AMEND Scope Declared and Enforced Per Table
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: When AMEND flag is set, scope is declared at the top and every table
  includes an explicit out-of-scope notation for excluded signals. Scope declared but not
  per-table = PARTIAL. (2 pts full / 1 pt partial)

### C-11 — Systemic Pattern Echo Field (Named Structural Column)
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Echo section has a labeled structural field (column or named row) for
  the recurring failure mode — not embedded in prose. Field present but unlabeled = PARTIAL.
  (2 pts full / 1 pt partial)

### C-12 — Three-Way Wrong/Gap/Echo Isolation
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: Wrong verdicts, gaps, and the Echo occupy distinct structural sections
  with no cross-contamination. A wrong prediction restated as the Echo fails. (2 pts full /
  1 pt partial)

### C-13 — Inertia Framing for Gaps
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: Each gap entry names the *assumption held without evidence* that made the
  gap invisible — not just the outcome that would have surfaced. "Would have surfaced" phrasing
  without an assumption statement = FAIL. (2 pts full / 1 pt partial)

### C-14 — Verdict Label Explicit Not Prose
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Signal accuracy verdicts use an enumerated label set (e.g., C / P / W /
  ND) enforced by table column, not prose phrasing. Prose verdicts that happen to be clear =
  PARTIAL. (2 pts full / 1 pt partial)

### C-15 — Accuracy Ratio Not Just Count
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Accuracy summary states an explicit ratio or percentage (N/M = X%) in
  addition to or instead of raw counts. Weighted formula score without the N/M=X% form =
  PARTIAL. (2 pts full / 1 pt partial)

### C-16 — Namespace Coverage Table Not Implied
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Namespace coverage is presented as a structured table with one explicit
  row per namespace (all 9), not as a prose list or implied enumeration. Text list form =
  PARTIAL. (2 pts full / 1 pt partial)

### C-17 — Recommendation Addresses Template
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Recommendation uses a bracket-slot template that enforces the gap/Echo
  linkage and practice-change fields structurally — not as free prose. (2 pts full / 1 pt
  partial)

### C-18 — Echo Systemic Pattern Named (Not Blank, Not Restatement)
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: The pattern field in the Echo section carries a named recurring failure
  mode with a descriptive label (e.g., "[name] — [recurring failure mode description]") and
  is constrained against being blank or restating a wrong prediction. Field present but
  unconstrained = PARTIAL. (2 pts full / 1 pt partial)

### C-19 — Phase Completion Self-Contained
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: Every phase is structured so that required fields cannot be silently
  deferred. Tabular phases with self-contained rows satisfy this; non-tabular phases (prose
  sections) must include a structural mechanism preventing silent truncation. Table rows
  self-contained but non-tabular phases unprotected = PARTIAL. (2 pts full / 1 pt partial)

### C-20 — Gap Inertia Assumption Named
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: The gap table includes a dedicated column (or equivalent labeled field)
  for the *assumption held without evidence* — the inertia belief that made the gap invisible
  before commitment. This is distinct from what the gap would have surfaced: the assumption
  explains *why* the gap existed, not *what* it missed. A gap table that names only outcomes
  ("Would have surfaced X") without naming the prior belief fails this criterion. Assumption
  field present but merged with outcome = PARTIAL. (2 pts full / 1 pt partial)

### C-21 — Phase Seal Explicit
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: Each phase ends with an explicit seal statement that names the required
  output fields for that phase and confirms they are populated. The seal is a structural
  artifact (not a general "phase complete" marker) — it enumerates what must be present.
  Seals present on tabular phases only, with non-tabular phases unsealed = PARTIAL. Addresses
  the truncation failure mode that C-19 (self-contained rows) leaves open: a row-level
  guarantee does not protect phase-level required outputs in prose sections. (2 pts full /
  1 pt partial)

---

## Scoring Summary

| Tier | Criteria | Points Each | Total |
|------|----------|-------------|-------|
| Essential | C-01–C-05 | 12 | 60 |
| Recommended | C-06–C-08 | 10 | 30 |
| Aspirational | C-09–C-21 | 2 | 26 |
| **Total** | | | **116** |

**Denominator adjustment**: C-10 is non-applicable when no AMEND topic is present.
Effective denominator in non-AMEND runs = 114.

**Partial scoring**: PARTIAL on essential = FAIL for "All essential: YES".
PARTIAL on recommended or aspirational = 1 pt.
```

---

**What changed in v5:**

| Criterion | Source | Signal |
|-----------|--------|--------|
| C-20 gap-inertia-assumption-named | C-13 FAIL in V-01 (Round 6) | Gap tables name outcomes; the *assumption* that made the gap invisible is a distinct field |
| C-21 phase-seal-explicit | V-02 "Phase-Seal" design (Round 6) | Per-phase seals name required fields and confirm presence — stronger than C-19's row-level self-containment, which leaves non-tabular phases unprotected |

Total available: 112 → 116.
