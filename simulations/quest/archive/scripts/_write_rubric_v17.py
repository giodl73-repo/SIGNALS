import pathlib

dest = pathlib.Path('C:/src/sim/simulations/quest/rubrics/topic-retro-rubric-v17-2026-03-17.md')

# Read v16 as base; strip the leading "Done. Here's..." preamble and the trailing duplicate
# changelog block, then splice in v17 header + C-44/C-45.

sections = []

# --- CHANGELOG HEADER ---
sections.append("""\
# topic-retro Rubric v17 -- 2026-03-17

**What changed in v17:**

| | v16 | v17 |
|---|---|---|
| New criteria | -- | C-44, C-45 |
| Aspirational pts | 70 (C-09--C-43) | 74 (C-09--C-45) |
| Total | 160 | 164 |
| non-AMEND denom | 156 | 160 |
| AMEND/no-excl denom | 158 | 162 |
| AMEND/excl denom | 160 | 164 |

**C-44 -- SEAL-Enforced Bidirectional Navigation Completeness** lifts the ceiling above C-42.
C-42 requires the structural columns for both citation directions to be present. C-44 requires
the Phase 0 SEAL to verify three additional properties that prevent PARTIAL degradation over
time: exact Derived Views table names, a forward navigation check statement, and a backward
navigation check statement. C-42 PASS without these SEAL items = PARTIAL.

**C-45 -- Assessor Navigation Preamble (Three-Entry-Point Declaration)** lifts the ceiling above
C-43. C-43 requires a `Manifest column` field mapping contract rows to manifest columns. C-45
requires the contract to be prefaced by a structured navigation preamble naming all three valid
audit entry points: (1) contract row -> manifest column, (2) manifest row -> derived views,
(3) phase section header -> derived from declaration. Preamble absent or fewer than three entry
points = PARTIAL; three entry points named in prose rather than a structured block = PARTIAL.

Both criteria require structural enforcement -- neither can be passed by prose description of intent.

---
""")

# --- ESSENTIAL CRITERIA ---
sections.append("""\
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
""")

# --- RECOMMENDED CRITERIA ---
sections.append("""\
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
""")

# --- ASPIRATIONAL CRITERIA ---
sections.append("""\
## Aspirational Criteria (74 points total)

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

### C-44 -- SEAL-Enforced Bidirectional Navigation Completeness
- **Weight**: aspirational  **Category**: correctness
- **Source**: Round 18, V-05 C-42 excellence signal
- **Pass condition**: C-42 requires the structural columns for both citation directions to be
  present. C-44 requires the Phase 0 SEAL to verify three additional properties that prevent
  PARTIAL degradation over time: (a) each Derived Views entry names the exact downstream table
  identifier rather than a generic label (e.g., "Phase 2 Signal Coverage Table" not "Phase 2
  table"), (b) a forward navigation check statement is present in Phase 0 explicitly declaring
  the manifest -> downstream direction as verified, and (c) a backward navigation check
  statement is present in Phase 0 explicitly declaring the downstream -> manifest direction as
  verified. A SEAL that checks structural column presence (satisfying C-42) but does not
  enforce exact naming or the directional check statements = PARTIAL. A SEAL that covers both
  directional check statements but accepts generic Derived Views entries = PARTIAL.
  (2 pts full / 1 pt partial)

### C-45 -- Assessor Navigation Preamble (Three-Entry-Point Declaration)
- **Weight**: aspirational  **Category**: format
- **Source**: Round 18, V-05 C-43 excellence signal
- **Pass condition**: C-43 requires a `Manifest column` field mapping each contract row to the
  exact AUDIT MANIFEST column that evidences it. C-45 requires the contract to be prefaced by
  an explicit assessor navigation preamble -- a structured block (not prose) that names all
  valid audit entry points, enabling any assessor to enter the audit system from any starting
  point without prior knowledge of its architecture. The preamble must name at least three
  entry points: (1) contract row -> manifest column via the `Manifest column` field, (2)
  manifest row -> downstream table via the `Derived Views` column, (3) phase section header ->
  manifest source via the `[DERIVED FROM]` declaration. Preamble present but names fewer than
  three distinct entry points = PARTIAL. All three entry points present but embedded in prose
  rather than a structured navigation block = PARTIAL.
  (2 pts full / 1 pt partial)

---
""")

# --- EXTENDED CHANGELOG ---
sections.append("""\
**What changed in v17 (extended):**

**C-44** lifts the ceiling above C-42. C-42 ensures both citation directions exist as structural
columns. C-44 ensures the Phase 0 SEAL guards the quality and completeness of those columns:
Derived Views entries must be precise enough to be navigable (exact artifact names, not generic
labels), and explicit check statements must declare both directions as verified. Without C-44, a
template satisfies C-42 by having the columns present while silently degrading to generic entries
("Phase 2 table") that name the right section family but not the right artifact. V-05's three
SEAL items -- exact-name check, forward check statement, backward check statement -- are the
structural mechanism that prevents this. C-44 makes those SEAL items a scoreable requirement.

**C-45** lifts the ceiling above C-43. C-43 ensures the contract carries a `Manifest column`
field so an assessor can navigate from any contract row to the manifest column that will evidence
it. C-45 ensures the navigation system is fully declared before the assessor begins reading: a
preamble block that enumerates all three entry points makes the bidirectional audit system
self-describing. Without C-45, an assessor who starts from a manifest row rather than a contract
row has no declared entry path; the preamble closes that gap. V-05's three-entry-point
declaration and explicit "bidirectional audit system navigable from three entry points" framing
are the structural elements C-45 captures.

Both criteria are SEAL-level structural requirements -- they cannot be satisfied by prose
description of intent or by verifying that the underlying citations happen to be correct.
""")

dest.write_text('\n'.join(sections), encoding='utf-8')
print('written', dest.stat().st_size, 'bytes')
