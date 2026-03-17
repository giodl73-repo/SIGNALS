Two excellence signals from R15 extract cleanly:

1. **V-02 C-37 PASS** — backward recovery implemented as two separate named tables with step-by-step recovery columns, not a single gate or inline math. This goes beyond C-37's reconciliation requirement.

2. **V-02 C-05 PASS** — PRE-EXECUTION CONTRACT as a filled table with four named structural fields including Signal window and Mode, beyond what C-05 requires (Topic + Commitment only).

---

```markdown
skill: quest-rubric | skill_target: topic-retro | version: 14

## Scoring Table

| Tier | Criteria | Pts each | Total |
|------|----------|----------|-------|
| Essential | C-01–C-05 | 12 | 60 |
| Recommended | C-06–C-08 | 10 | 30 |
| Aspirational | C-09–C-39 | 2 | **62** |
| **Total** | | | **152** |

Denominators: non-AMEND = **148**, AMEND/no-exclusions = **150**, AMEND/exclusions = **152**.

---

## Essential Criteria (60 points total)

### C-01 -- One Echo Named, Unexpected, Actionable
- **Weight**: essential  **Category**: correctness
- **Pass condition**: Exactly one Echo is named, described as unexpected at time of prediction,
  and links to an actionable follow-up. Echo: NONE is a valid pass when no qualifying signal
  exists.

### C-02 -- Wrong Verdicts Identified
- **Weight**: essential  **Category**: correctness
- **Pass condition**: Every signal with a WRONG verdict is listed with a brief explanation of
  why the prediction failed.

### C-03 -- Gap Analysis Present
- **Weight**: essential  **Category**: coverage
- **Pass condition**: A dedicated gap section identifies namespaces or signal types that were
  absent during the topic run.

### C-04 -- Echo Disqualification Rule Enforced
- **Weight**: essential  **Category**: correctness
- **Pass condition**: An explicit disqualification rule prevents a wrong prediction from being
  restated as the Echo. The rule must be present as a named gate, not implied. A wrong
  prediction promoted to Echo without disqualification check = FAIL.

### C-05 -- Topic and Commitment Context Established
- **Weight**: essential  **Category**: correctness
- **Pass condition**: Topic name and commitment nature are stated in the first two sections
  (e.g., PRE-EXECUTION CONTRACT block or equivalent opening).

---

## Recommended Criteria (30 points total)

### C-06 -- Signal Coverage Summary
- **Weight**: recommended  **Category**: coverage
- **Pass condition**: Summary distinguishes "signals gathered" from "signals absent" across all
  9 namespaces, with at least one explicit entry per namespace.

### C-07 -- Improvement Recommendation Tied to Gaps or Echo
- **Weight**: recommended  **Category**: depth
- **Pass condition**: Recommendation names the specific gap or Echo it addresses (e.g.,
  "Addresses: [Gap: scout-feasibility]") and specifies a practice change.

### C-08 -- Accuracy Rate or Ratio Stated
- **Weight**: recommended  **Category**: format
- **Pass condition**: Numerical accuracy summary in ratio or percentage form (e.g., "7/9 =
  77.8%") present in or immediately following the Signal Accuracy section.

---

## Aspirational Criteria (62 points total)

### C-09 -- Echo Linked to Systemic Pattern
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: Echo section connects the unexpected finding to a broader pattern of
  failure, not just the isolated instance. (2 pts full / 1 pt partial)

### C-10 -- AMEND Scope Declared and Enforced Per Table
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: When AMEND flag is set, scope is declared at the top and every table
  includes an explicit out-of-scope notation for excluded signals. Scope declared but not
  enforced per-table = PARTIAL. Non-AMEND run = N/A. (2 pts full / 1 pt partial)

### C-11 -- Systemic Pattern Echo Field (Named Structural Column)
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Echo section has a labeled structural field (column or named row) for the
  recurring failure mode — not embedded in prose. Field present but unlabeled = PARTIAL.
  (2 pts full / 1 pt partial)

### C-12 through C-35
*(Defined in prior rubric versions; not reproduced here. Scoring and pass conditions
unchanged from v13.)*

---

### C-36 -- Three-Pass Architectural Isolation as Structural Property
- **Weight**: aspirational  **Category**: format
- **Source**: Round 14 pattern 1
- **Pass condition**: C-12 requires wrong verdicts, gaps, and Echo to occupy distinct sections.
  C-36 requires that isolation to be a structural property of the template architecture —
  e.g., each pass is a named architectural phase with its own entry/exit criteria or a
  phase-numbered gate — not merely a written prohibition. "Do not mix wrong and Echo" in prose
  satisfies C-12 but fails C-36. Structural enforcement present but no phase-level entry/exit
  contract = PARTIAL. (2 pts full / 1 pt partial)

### C-37 -- Accuracy Reconciliation Cross-Check
- **Weight**: aspirational  **Category**: correctness
- **Source**: Round 14 pattern 2
- **Pass condition**: C-08/C-15 require an accuracy ratio to be stated. C-37 requires the ratio
  to be verified by a forward/backward reconciliation: a forward count (predictions evaluated
  sequentially) and a backward count (starting from wrong verdicts, recovering total) are
  compared and must agree. Ratio stated (C-08/C-15 PASS) but no reconciliation cross-check =
  PARTIAL. (2 pts full / 1 pt partial)

### C-38 -- Backward Recovery Table as Named Structural Artifact
- **Weight**: aspirational  **Category**: format
- **Source**: Round 15, V-02 C-37 excellence signal
- **Pass condition**: C-37 requires a forward/backward reconciliation cross-check. C-38 requires
  the backward recovery path to be implemented as a named structural table — not prose or
  inline math — with explicit columns for: (a) starting count of wrong verdicts, (b)
  step-by-step recovery to total prediction count, and (c) a reconciliation result row.
  Reconciliation present as prose or single computed value = PARTIAL.
  (2 pts full / 1 pt partial)

### C-39 -- Signal Window and Mode Declared in Pre-Execution Contract
- **Weight**: aspirational  **Category**: format
- **Source**: Round 15, V-02 C-05 excellence signal
- **Pass condition**: C-05 requires Topic and Commitment nature in the opening section. C-39
  requires two additional named structural fields in the Pre-Execution Contract: (a) Signal
  window — the bounding date range, sprint, or iteration scope for predictions evaluated —
  and (b) Mode — an explicit AMEND/FRESH flag or equivalent. Fields inferred from prose or
  absent entirely = PARTIAL. (2 pts full / 1 pt partial)
```

---

**What changed in v14:**

| | v13 | v14 |
|---|---|---|
| New criteria | — | C-38, C-39 |
| Aspirational pts | 58 (C-09–C-37) | 62 (C-09–C-39) |
| Total | 148 | 152 |
| non-AMEND denom | 144 | 148 |
| AMEND/no-excl denom | 146 | 150 |
| AMEND/excl denom | 148 | 152 |

**C-38** codifies the V-02 pattern where the backward recovery is itself a two-table structural artifact (forward count table + backward recovery table with step-by-step columns), not a gate or prose check. This lifts the ceiling above C-37 PASS.

**C-39** codifies the V-02 PRE-EXECUTION CONTRACT pattern where Signal window and Mode are explicit structural fields alongside Topic and Commitment — giving the contract four named rows rather than two. These fields make run scope auditable without reading prose.
