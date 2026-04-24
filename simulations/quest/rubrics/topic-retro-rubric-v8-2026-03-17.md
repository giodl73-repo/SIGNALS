Here is the complete v8 rubric, written to `simulations/quest/rubrics/topic-retro-rubric-v8-2026-03-17.md`.

---

## Two new criteria from Round 9

**C-26 -- Gap Inertia Column Structurally Isolated** (`gap-inertia-column-isolation`)
- Source: V-05 C-13/C-20 double PASS
- The mechanism: C-13 and C-20 fail together when the assumption column is merged with the outcome column. They pass together only when the two are structurally separate columns. Builds on C-20 (assumption must exist) — C-26 requires it be *isolated* from the outcome field.
- Merged = PARTIAL. No assumption field = FAIL (C-20's domain, not scored here).

**C-27 -- Phase Self-Containment Extended to All 8 Phases** (`phase-8-self-containment-extended`)
- Source: V-05 C-19 PASS (persistent PARTIAL in V-01 through V-04)
- The mechanism: C-19 was PARTIAL because SEAL coverage stopped at Phase 6. Phases 7 (gap analysis) and 8 (recommendation) were unprotected. Full PASS requires all 8 phases explicitly covered.
- Phases 1-6 sealed, 7-8 absent = PARTIAL. All 8 named = PASS.

---

## Updated scoring summary

| Tier | Criteria | Pts each | Total |
|------|----------|----------|-------|
| Essential | C-01--C-05 | 12 | 60 |
| Recommended | C-06--C-08 | 10 | 30 |
| Aspirational | C-09--C-27 | 2 | **38** |
| **Total** | | | **128** |

Denominator: non-AMEND = 124, AMEND/no-exclusions = 126, AMEND/exclusions = 128.
ng)
- **Weight**: essential  **Category**: depth
- **Pass condition**: Exactly one Echo, framed as unpredicted (not a restatement of a wrong
  prediction). Multiple echoes or restatements fail.

### C-05 -- Topic and Commitment Context Established
- **Weight**: essential  **Category**: correctness
- **Pass condition**: Topic name and commitment nature stated in first two sections.

---

## Recommended Criteria (30 points total)

### C-06 -- Signal Coverage Summary
- **Weight**: recommended  **Category**: coverage
- **Pass condition**: Summary distinguishes "signals gathered" from "signals absent" across all
  9 namespaces.

### C-07 -- Improvement Recommendation Tied to Gaps or Echo
- **Weight**: recommended  **Category**: depth
- **Pass condition**: Recommendation names the specific gap or Echo it addresses and specifies
  a practice change.

### C-08 -- Accuracy Rate or Ratio Stated
- **Weight**: recommended  **Category**: format
- **Pass condition**: Numerical accuracy summary (ratio or percentage) present in or
  immediately following the Signal Accuracy section.

---

## Aspirational Criteria (38 points total)

### C-09 -- Echo Linked to Systemic Pattern
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: Echo section connects the unexpected finding to a broader pattern of
  failure, not just the isolated instance. (2 pts full / 1 pt partial)

### C-10 -- AMEND Scope Declared and Enforced Per Table
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: When AMEND flag is set, scope is declared at the top and every table
  includes an explicit out-of-scope notation for excluded signals. Scope declared but not
  per-table = PARTIAL. (2 pts full / 1 pt partial)

### C-11 -- Systemic Pattern Echo Field (Named Structural Column)
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Echo section has a labeled structural field (column or named row) for
  the recurring failure mode -- not embedded in prose. Field present but unlabeled = PARTIAL.
  (2 pts full / 1 pt partial)

### C-12 -- Three-Way Wrong/Gap/Echo Isolation
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: Wrong verdicts, gaps, and the Echo occupy distinct structural sections
  with no cross-contamination. A wrong prediction restated as the Echo fails. (2 pts full /
  1 pt partial)

### C-13 -- Inertia Framing for Gaps
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: Each gap entry names the *assumption held without evidence* that made the
  gap invisible -- not just the outcome that would have surfaced. "Would have surfaced"
  phrasing without an assumption statement = FAIL. (2 pts full / 1 pt partial)

### C-14 -- Verdict Label Explicit Not Prose
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Signal accuracy verdicts use an enumerated label set (e.g., C / P / W /
  ND) enforced by table column, not prose phrasing. Prose verdicts that happen to be clear =
  PARTIAL. (2 pts full / 1 pt partial)

### C-15 -- Accuracy Ratio Not Just Count
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Accuracy summary states an explicit ratio or percentage (N/M = X%) in
  addition to or instead of raw counts. Weighted formula score without the N/M=X% form =
  PARTIAL. (2 pts full / 1 pt partial)

### C-16 -- Namespace Coverage Table Not Implied
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Namespace coverage is presented as a structured table with one explicit
  row per namespace (all 9), not as a prose list or implied enumeration. Text list form =
  PARTIAL. (2 pts full / 1 pt partial)

### C-17 -- Recommendation Template (Bracket-Slot)
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Recommendation uses a bracket-slot template that enforces the gap/Echo
  linkage and practice-change fields structurally -- not as free prose. (2 pts full / 1 pt
  partial)

### C-18 -- Echo Systemic Pattern Named (Not Blank, Not Restatement)
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: The pattern field in the Echo section carries a named recurring failure
  mode with a descriptive label (e.g., "[name] -- [recurring failure mode description]") and
  is constrained against being blank or restating a wrong prediction. Field present but
  unconstrained = PARTIAL. (2 pts full / 1 pt partial)

### C-19 -- Phase Completion Self-Contained
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: Every phase is structured so that required fields cannot be silently
  deferred. Tabular phases with self-contained rows satisfy this; non-tabular phases (prose
  sections) must include a structural mechanism preventing silent truncation. Table rows
  self-contained but non-tabular phases unprotected = PARTIAL. (2 pts full / 1 pt partial)

### C-20 -- Gap Inertia Assumption Named
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: The gap table includes a dedicated column (or equivalent labeled field)
  for the *assumption held without evidence* -- the inertia belief that made the gap invisible
  before commitment. This is distinct from what the gap would have surfaced: the assumption
  explains *why* the gap existed, not *what* it missed. A gap table that names only outcomes
  ("Would have surfaced X") without naming the prior belief fails this criterion. Assumption
  field present but merged with outcome = PARTIAL. (2 pts full / 1 pt partial)

### C-21 -- Phase Seal Explicit
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: Each phase ends with an explicit seal statement that names the required
  output fields for that phase and confirms they are populated. The seal is a structural
  artifact (not a general "phase complete" marker) -- it enumerates what must be present.
  Seals present on tabular phases only, with non-tabular phases unsealed = PARTIAL. Addresses
  the truncation failure mode that C-19 (self-contained rows) leaves open: a row-level
  guarantee does not protect phase-level required outputs in prose sections. (2 pts full /
  1 pt partial)

### C-22 -- OOS Secondary Table for Excluded Signals
- **Weight**: aspirational  **Category**: format
- **Pass condition**: When AMEND scope excludes signals from a phase, those signals appear in
  a dedicated secondary "Out of scope" table for that phase -- not silently dropped and not
  noted only in a prose aside or a primary-table footer. The primary table is authoritative
  for in-scope signals; the secondary table is authoritative for excluded signals. Clean
  separation: exclusion commentary absent from primary table. Secondary table absent when
  exclusions exist = PARTIAL. Non-applicable when no signals are excluded in any phase. (2
  pts full / 1 pt partial)

### C-23 -- Phase Seal Format Strings Per Field
- **Weight**: aspirational  **Category**: format
- **Pass condition**: Each field listed in a phase seal carries an explicit format string
  defining the expected value form (e.g., `{signal-name}: {C/P/W/ND} -- {one-line reason}`),
  not just a field label. This makes the seal a format contract rather than a field
  checklist -- the consumer knows both what must be present and what it must look like. Seal
  fields present but with labels only (no format strings) = PARTIAL. Builds on C-21: C-21
  requires the seal enumerate fields; C-23 requires those enumerations carry format
  specifications. (2 pts full / 1 pt partial)

### C-24 -- Echo Why-Unexpected Explained
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: The Echo section carries an explicit field or statement naming *why* the
  finding was unexpected -- that is, which prior belief, model, or assumption it contradicted.
  "Unexpected" as a label alone is not sufficient; the explanation must identify what the
  author expected and why reality diverged. This converts the Echo from a labeled anomaly into
  a belief-correction event. "Why unexpected: [prior model or assumption contradicted]" form
  or equivalent labeled field = PASS. Unexpected label present but no explanation of the prior
  belief = PARTIAL. (2 pts full / 1 pt partial)

### C-25 -- Recommendation Outcome Measurable
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: The improvement recommendation includes an explicit measurable outcome --
  a statement of what would be observably different if the practice change succeeded. This is
  a third required slot beyond gap/echo linkage (C-07) and practice change specification
  (C-07/C-17): "address [gap/echo] by [practice change] so that [measurable outcome]." A
  recommendation that names the gap and change without specifying a measurable outcome =
  PARTIAL. No recommendation present = FAIL (C-07's domain). (2 pts full / 1 pt partial)

### C-26 -- Gap Inertia Column Structurally Isolated
- **Weight**: aspirational  **Category**: format
- **Pass condition**: The gap table carries two structurally separate columns (or clearly
  delineated labeled fields): one for the *assumption held without evidence* (the inertia
  belief) and one for the *surfacing outcome* (what the signal would have revealed). These two
  fields must be isolated -- not merged into a single cell or combined column. When merged,
  the inertia assumption collapses into outcome language and both C-13 and C-20 fail
  simultaneously. Builds on C-20 (which requires the assumption field exist at all): C-26
  requires it be structurally isolated from the outcome field. Assumption present but merged
  with outcome = PARTIAL. No assumption field = FAIL (C-20's domain, not scored here). (2
  pts full / 1 pt partial)

### C-27 -- Phase Self-Containment Extended to All 8 Phases
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: SEAL coverage and self-containment guarantees extend explicitly to all 8
  phases of the retrospective -- including the gap analysis phase (Phase 7) and the
  recommendation phase (Phase 8). A rubric or output that applies SEAL gates and structural
  self-containment only to Phases 1-6 leaves the two phases most likely to be abbreviated
  (gap and recommendation) unprotected against silent truncation. Builds on C-19 (all phases
  must be self-contained) and C-21 (seals must enumerate required fields): C-27 requires the
  8-phase scope itself be complete and explicit in the skill specification. Phases 1-6 with
  SEAL coverage and Phases 7-8 without explicit SEAL specification = PARTIAL. All 8 phases
  with named seals = PASS. (2 pts full / 1 pt partial)

---

## Scoring Summary

| Tier | Criteria | Points Each | Total |
|------|----------|-------------|-------|
| Essential | C-01--C-05 | 12 | 60 |
| Recommended | C-06--C-08 | 10 | 30 |
| Aspirational | C-09--C-27 | 2 | 38 |
| **Total** | | | **128** |

**Denominator adjustment**: C-10 is non-applicable when no AMEND topic is present.
C-22 is non-applicable when no signals are excluded in any phase.
Effective denominator in non-AMEND runs = 124. In AMEND runs with no per-phase
exclusions = 126. In AMEND runs with per-phase exclusions = 128.

**Partial scoring**: PARTIAL on essential = FAIL for "All essential: YES".
PARTIAL on recommended or aspirational = 1 pt.

---

## Change Log

| Version | Criterion | Source | Signal |
|---------|-----------|--------|--------|
| v8 | C-26 gap-inertia-column-isolation | V-05 C-13/C-20 double PASS (Round 9) | C-13 and C-20 resolve simultaneously only when the assumption column is structurally isolated from the outcome column -- merging both into one cell causes both to fail; the structural fix is two separate labeled columns |
| v8 | C-27 phase-8-self-containment-extended | V-05 C-19 PASS (Round 9) | C-19 reached PASS only when SEAL coverage explicitly extended to all 8 phases; rubrics scoped to Phases 1-6 left the gap and recommendation phases unprotected, producing the persistent PARTIAL |
| v7 | C-24 echo-why-unexpected-named | V-02 excellence (Round 8) | Echo sections label findings as unexpected but never require the author to name the prior belief that was contradicted -- the belief-correction is the learning, not the label |
| v7 | C-25 recommendation-outcome-measurable | V-02 C-07 PASS (Round 8) | V-02 Phase 5 requires three components: gap/echo addressed + namespace/process step + measurable outcome; existing C-07 and C-17 capture the first two but leave measurability as optional prose |
| v6 | C-22 oos-secondary-table-explicit | V-02 C-10 PASS (Round 7) | OOS secondary table in Phase 2 shows clean scoping: excluded signals get a dedicated secondary table per phase, not a prose note or primary-table footer |
| v6 | C-23 phase-seal-format-strings-per-field | V-04 C-21 PARTIAL (Round 7) | Seal fields present but "format strings per field not confirmed explicit" -- the excellence is each seal field carries a format specification, making it a format contract rather than a checklist |
| v5 | C-20 gap-inertia-assumption-named | C-13 FAIL in V-01 (Round 6) | Gap tables name outcomes; the assumption that made the gap invisible is a distinct field |
| v5 | C-21 phase-seal-explicit | V-02 Phase-Seal design (Round 6) | Per-phase seals name required fields and confirm presence -- stronger than C-19's row-level self-containment, which leaves non-tabular phases unprotected |

Total available: 124 -> 128.
