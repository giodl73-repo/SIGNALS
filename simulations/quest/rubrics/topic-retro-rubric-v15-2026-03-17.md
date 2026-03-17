Done. Here's the rubric at `simulations/quest/rubrics/topic-retro-rubric-v15-2026-03-17.md`.

---

**What changed in v15:**

| | v14 | v15 |
|---|---|---|
| New criteria | — | C-40, C-41 |
| Aspirational pts | 62 (C-09–C-39) | 66 (C-09–C-41) |
| Total | 152 | 156 |
| non-AMEND denom | 148 | 152 |
| AMEND/no-excl denom | 150 | 154 |
| AMEND/excl denom | 152 | 156 |

**C-40 — Manifest-First Derivation** lifts the ceiling above C-38. C-38 says "backward recovery must be a named structural table." C-40 says all downstream tables (backward recovery, namespace coverage, echo input) must be *derived views* of one primary AUDIT MANIFEST — not independently authored. Any section re-authored from scratch fails C-40 even if it satisfies C-38.

**C-41 — Named-Criteria Phase Gate** lifts the ceiling above C-36. C-36 says "phase exit contracts must exist." C-41 says the gate must assert aspiration criteria by their *structural artifact name* ("Backward Recovery Table A: PRESENT"), not by prose description or rubric ID alone. A gate that describes intent without naming the artifact fails C-41 even if it satisfies C-36.

Both criteria are set up so they cannot be passed by prose substitution — which is the core property that made V-05 distinctive across both patterns.
**Category**: correctness
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

## Aspirational Criteria (66 points total)

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

### C-40 -- Manifest-First Derivation (All Downstream Sections as Views)
- **Weight**: aspirational  **Category**: correctness
- **Source**: Round 16, V-05 Pattern 1 excellence signal
- **Pass condition**: C-37/C-38 require named reconciliation tables. C-40 requires that all
  downstream sections — backward recovery tables, namespace coverage table, and Echo input —
  are derived as filtered or grouped views of a single primary AUDIT MANIFEST table rather
  than being independently authored. The manifest must be named and its derivation
  relationships must be stated or structurally evident (e.g., "filtering WRONG rows gives
  Table A; grouping by Namespace gives coverage table"). Any section that is separately
  written rather than derived from the manifest = PARTIAL. A skill that states tables exist
  without naming the manifest as their source = PARTIAL.
  (2 pts full / 1 pt partial)

### C-41 -- Named-Criteria Phase Gate (Aspiration Criteria Asserted by Structural Requirement)
- **Weight**: aspirational  **Category**: correctness
- **Source**: Round 16, V-05 Pattern 2 excellence signal
- **Pass condition**: C-36 requires a phase-level entry/exit contract. C-41 requires the phase
  exit gate to assert aspiration criteria by their structural requirement — naming the exact
  artifact that must be present (e.g., "Backward Recovery Table A: PRESENT") rather than
  describing intent in prose. The gate must reference at least one aspiration criterion by
  its structural artifact name, not by rubric ID alone. A gate that describes what should
  exist without naming the exact artifact = PARTIAL. A gate that references only essential
  or recommended criteria = PARTIAL. (2 pts full / 1 pt partial)
```

---

**What changed in v15:**

| | v14 | v15 |
|---|---|---|
| New criteria | — | C-40, C-41 |
| Aspirational pts | 62 (C-09–C-39) | 66 (C-09–C-41) |
| Total | 152 | 156 |
| non-AMEND denom | 148 | 152 |
| AMEND/no-excl denom | 150 | 154 |
| AMEND/excl denom | 152 | 156 |

**C-40** codifies the V-05 manifest-first derivation pattern: a single AUDIT MANIFEST table is
the primary artifact and every downstream section — backward recovery, coverage, echo input —
is a derived view of it. This eliminates the mechanism that produces contradictions between
tables. It goes beyond C-38 (which asks that a named table exist) by requiring that named
table to be the derivation source for all other tables.

**C-41** codifies the V-05 named-criteria phase gate pattern: the phase exit checklist asserts
aspiration criteria by their structural requirement ("Backward Recovery Table A: PRESENT")
rather than by prose description. This prevents aspiration criteria from being satisfied by
a paragraph when a named structural artifact is what the criterion actually requires. It goes
beyond C-36 (which asks that phase-level entry/exit contracts exist) by requiring the gate to
name specific aspiration artifacts, not just phase completion conditions.
