Done. Here's `topic-retro-rubric-v16-2026-03-17.md`.

---

**What changed in v16:**

| | v15 | v16 |
|---|---|---|
| New criteria | -- | C-42, C-43 |
| Aspirational pts | 66 (C-09--C-41) | 70 (C-09--C-43) |
| Total | 156 | 160 |
| non-AMEND denom | 152 | 156 |
| AMEND/no-excl denom | 154 | 158 |
| AMEND/excl denom | 156 | 160 |

**C-42 -- Bidirectional Manifest Citation** lifts the ceiling above C-40. C-40 requires downstream sections to declare derivation from the AUDIT MANIFEST (backward direction). C-42 requires the manifest itself to carry a `Derived Views` column naming what it feeds (forward direction). With both directions present the manifest becomes a consistency verification surface navigable from any starting point. Backward only (C-40 PASS) = PARTIAL.

**C-43 -- PRE-EXECUTION CONTRACT as Manifest Navigation Index** lifts the ceiling above C-39. C-39 requires Signal window and Mode fields in the contract. C-43 requires each structural commitment to also carry a `Manifest column` field naming the exact AUDIT MANIFEST column that evidences it — transforming the contract from a prospective declaration into a pre-execution auditor navigation index. C-39 PASS without Manifest column mapping = PARTIAL; Manifest column present but maps to section names rather than column names = PARTIAL.

Both criteria require structural columns — neither can be passed by prose substitution.
# Essential Criteria (60 points total)

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

## Aspirational Criteria (70 points total)

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
  recurring failure mode -- not embedded in prose. Field present but unlabeled = PARTIAL.
  (2 pts full / 1 pt partial)

### C-12 through C-35
*(Defined in prior rubric versions; not reproduced here. Scoring and pass conditions
unchanged from v13.)*

---

### C-36 -- Three-Pass Architectural Isolation as Structural Property
- **Weight**: aspirational  **Category**: format
- **Source**: Round 14 pattern 1
- **Pass condition**: C-12 requires wrong verdicts, gaps, and Echo to occupy distinct sections.
  C-36 requires that isolation to be a structural property of the template architecture --
  e.g., each pass is a named architectural phase with its own entry/exit criteria or a
  phase-numbered gate -- not merely a written prohibition. "Do not mix wrong and Echo" in prose
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
  the backward recovery path to be implemented as a named structural table -- not prose or
  inline math -- with explicit columns for: (a) starting count of wrong verdicts, (b)
  step-by-step recovery to total prediction count, and (c) a reconciliation result row.
  Reconciliation present as prose or single computed value = PARTIAL.
  (2 pts full / 1 pt partial)

### C-39 -- Signal Window and Mode Declared in Pre-Execution Contract
- **Weight**: aspirational  **Category**: format
- **Source**: Round 15, V-02 C-05 excellence signal
- **Pass condition**: C-05 requires Topic and Commitment nature in the opening section. C-39
  requires two additional named structural fields in the Pre-Execution Contract: (a) Signal
  window -- the bounding date range, sprint, or iteration scope for predictions evaluated --
  and (b) Mode -- an explicit AMEND/FRESH flag or equivalent. Fields inferred from prose or
  absent entirely = PARTIAL. (2 pts full / 1 pt partial)

### C-40 -- Manifest-First Derivation (All Downstream Sections as Views)
- **Weight**: aspirational  **Category**: correctness
- **Source**: Round 16, V-05 Pattern 1 excellence signal
- **Pass condition**: C-37/C-38 require named reconciliation tables. C-40 requires that all
  downstream sections -- backward recovery tables, namespace coverage table, and Echo input --
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
  exit gate to assert aspiration criteria by their structural requirement -- naming the exact
  artifact that must be present (e.g., "Backward Recovery Table A: PRESENT") rather than
  describing intent in prose. The gate must reference at least one aspiration criterion by
  its structural artifact name, not by rubric ID alone. A gate that describes what should
  exist without naming the exact artifact = PARTIAL. A gate that references only essential
  or recommended criteria = PARTIAL. (2 pts full / 1 pt partial)

### C-42 -- Bidirectional Manifest Citation (Forward + Backward Audit Trail)
- **Weight**: aspirational  **Category**: format
- **Source**: Round 17, V-05 pattern 1 excellence signal
- **Pass condition**: C-40 requires downstream sections to declare derivation from the AUDIT
  MANIFEST (backward citation: downstream -> manifest). C-42 requires the citation to be
  bidirectional: (a) the AUDIT MANIFEST table must include a named `Derived Views` column
  listing which downstream table(s) each row feeds (forward citation: manifest -> downstream),
  AND (b) each downstream section header must carry a `[DERIVED FROM: AUDIT MANIFEST |
  OPERATION: ...]` declaration (backward citation: downstream -> manifest). With both
  directions present, any point in the document is a navigable entry into the full derivation
  chain. Backward citations only (C-40 PASS) without a Derived Views column in the manifest
  = PARTIAL. Forward Derived Views column present but downstream headers lack DERIVED FROM
  declarations = PARTIAL. (2 pts full / 1 pt partial)

### C-43 -- PRE-EXECUTION CONTRACT as Manifest Navigation Index
- **Weight**: aspirational  **Category**: format
- **Source**: Round 17, V-05 pattern 2 excellence signal
- **Pass condition**: C-39 requires Signal window and Mode fields in the Pre-Execution
  Contract. C-43 requires the Pre-Execution Contract to include a `Manifest column` field
  for each structural commitment, mapping that commitment to the exact AUDIT MANIFEST column
  name that sources it (e.g., "Verdict -> Verdict column"). This transforms the contract from
  a prospective what-will-happen declaration into a pre-execution auditor navigation index:
  an assessor can locate the evidential basis of any commitment before execution begins.
  Contract satisfies C-39 but has no Manifest column field = PARTIAL. Manifest column field
  present but maps to section names or prose descriptions rather than exact column names
  = PARTIAL. (2 pts full / 1 pt partial)
```

---

**What changed in v16:**

| | v15 | v16 |
|---|---|---|
| New criteria | -- | C-42, C-43 |
| Aspirational pts | 66 (C-09--C-41) | 70 (C-09--C-43) |
| Total | 156 | 160 |
| non-AMEND denom | 152 | 156 |
| AMEND/no-excl denom | 154 | 158 |
| AMEND/excl denom | 156 | 160 |

**C-42** lifts the ceiling above C-40. C-40 requires derivation to be stated in the downstream
section (backward direction only). C-42 requires the manifest itself to carry a `Derived Views`
column that names what it feeds (forward direction), creating a complete bidirectional audit
trail. The manifest becomes a consistency verification surface: an assessor can start at any
row in the manifest and follow the forward citation to find the downstream table that should
reflect it, or start at any downstream table and follow the backward citation to the manifest
rows that sourced it. Prior to V-05, only the backward direction existed.

**C-43** lifts the ceiling above C-39. C-39 requires Signal window and Mode as named fields in
the Pre-Execution Contract. C-43 requires every structural commitment in the contract to carry
a `Manifest column` field naming the exact AUDIT MANIFEST column that will evidence it. This
makes the contract an auditor navigation index before execution: instead of reading the prose
commitment and then searching the manifest for the relevant column, the assessor has a direct
pointer. The contract was previously forward-looking (what will happen); C-43 makes it also
backward-pointing (where in the manifest to verify it happened).

Both criteria are set up so they cannot be passed by prose substitution: C-42 requires a
structural column in the manifest table, and C-43 requires a structural field in the contract
table -- neither can be satisfied by a paragraph.
