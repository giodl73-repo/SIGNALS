Written to `simulations/quest/rubrics/topic-retro-rubric-v6-2026-03-17.md`.

---

**Two excellence signals extracted from Round 7:**

**C-22 — OOS Secondary Table for Excluded Signals** (oos-secondary-table-explicit)
- Source: V-02 C-10 PASS — "OOS secondary table in Phase 2 — clean scoping"
- The pattern: under AMEND, excluded signals don't disappear from the primary table with a footer note — they get a dedicated secondary table. Primary table = in-scope only. Secondary table = excluded only. No commentary bleeds across.
- PARTIAL: secondary table absent when exclusions exist. N/A: when no signals are excluded.

**C-23 — Phase Seal Format Strings Per Field** (phase-seal-format-strings-per-field)
- Source: V-04 C-21 PARTIAL — "format strings per field not confirmed explicit"
- The pattern: C-21 required seals enumerate fields; C-23 requires each field in a seal carry a format string (e.g., `{signal}: {C/P/W/ND} -- {reason}`). Labels alone = checklist. Labels + format strings = contract.
- PARTIAL: fields present but no format strings. FAIL: no seal at all (that's C-21's domain).

**Scoring summary updated:**

| Tier | Criteria | Pts each | Total |
|------|----------|----------|-------|
| Essential | C-01--C-05 | 12 | 60 |
| Recommended | C-06--C-08 | 10 | 30 |
| Aspirational | C-09--C-23 | 2 | 30 |
| **Total** | | | **120** |

116 → 120. Two new denominator adjustment notes added (C-22 N/A when no exclusions; effective denominator rules for non-AMEND = 116, AMEND with no exclusions = 118).
 a wrong
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

## Aspirational Criteria (30 points total)

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
  mode with a descriptive label (e.g., "[name] -- [recurring failure mode description]") and
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

### C-22 — OOS Secondary Table for Excluded Signals
- **Weight**: aspirational  **Category**: format
- **Pass condition**: When AMEND scope excludes signals from a phase, those signals appear in
  a dedicated secondary "Out of scope" table for that phase -- not silently dropped and not
  noted only in a prose aside or a primary-table footer. The primary table is authoritative
  for in-scope signals; the secondary table is authoritative for excluded signals. Clean
  separation: exclusion commentary absent from primary table. Secondary table absent when
  exclusions exist = PARTIAL. Non-applicable when no signals are excluded in any phase. (2
  pts full / 1 pt partial)

### C-23 — Phase Seal Format Strings Per Field
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Each field listed in a phase seal carries an explicit format string
  defining the expected value form (e.g., `{signal-name}: {C/P/W/ND} -- {one-line reason}`),
  not just a field label. This makes the seal a format contract rather than a field
  checklist -- the consumer knows both what must be present and what it must look like. Seal
  fields present but with labels only (no format strings) = PARTIAL. Builds on C-21: C-21
  requires the seal enumerate fields; C-23 requires those enumerations carry format
  specifications. (2 pts full / 1 pt partial)

---

## Scoring Summary

| Tier | Criteria | Points Each | Total |
|------|----------|-------------|-------|
| Essential | C-01--C-05 | 12 | 60 |
| Recommended | C-06--C-08 | 10 | 30 |
| Aspirational | C-09--C-23 | 2 | 30 |
| **Total** | | | **120** |

**Denominator adjustment**: C-10 is non-applicable when no AMEND topic is present.
C-22 is non-applicable when no signals are excluded in any phase.
Effective denominator in non-AMEND runs = 116. In AMEND runs with no per-phase
exclusions = 118.

**Partial scoring**: PARTIAL on essential = FAIL for "All essential: YES".
PARTIAL on recommended or aspirational = 1 pt.

---

## Change Log

| Criterion | Source | Signal |
|-----------|--------|--------|
| C-22 oos-secondary-table-explicit | V-02 C-10 PASS (Round 7) | OOS secondary table in Phase 2 shows clean scoping: excluded signals get a dedicated secondary table per phase, not a prose note or primary-table footer |
| C-23 phase-seal-format-strings-per-field | V-04 C-21 PARTIAL (Round 7) | Seal fields present but "format strings per field not confirmed explicit" -- the excellence is each seal field carries a format specification, making it a format contract rather than a checklist |

Total available: 116 -> 120.
