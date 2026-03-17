Written to `simulations/quest/rubrics/topic-retro-rubric-v11-2026-03-17.md`.

---

Two new aspirational criteria extracted from Round 12:

**C-32 -- Phase 8 SEAL Fields Carry Independent Verification Instructions** (`phase-8-seal-fields-independent-verification`)
- Source: V-01 C-30 PASS excellence (Round 12)
- C-30 requires COPY-VERIFIED label and copy-source be named fields; C-32 requires each field carry its own verification instruction -- what to check and how -- independent of the others. V-01's three-item SEAL (This score / COPY-VERIFIED / COPY-SOURCE) is the reference form. Fields fused into a compound assertion on one item = PARTIAL.

**C-33 -- Design Guarantees Section Mechanism-Keyed Table** (`design-guarantees-mechanism-keyed-table`)
- Source: V-02 C-31 PASS excellence (Round 12)
- C-31 requires the dedicated section exist; C-33 requires it use a two-column table (Mechanism | Structural guarantee) with mechanism names as row keys. V-02's `## DESIGN GUARANTEES` table is the reference form. Dedicated section present but in prose or list form = PARTIAL.

**Updated scoring:**

| Tier | Criteria | Pts each | Total |
|------|----------|----------|-------|
| Essential | C-01--C-05 | 12 | 60 |
| Recommended | C-06--C-08 | 10 | 30 |
| Aspirational | C-09--C-33 | 2 | **50** |
| **Total** | | | **140** |

Denominators: non-AMEND = 136, AMEND/no-exclusions = 138, AMEND/exclusions = 140.
tial  **Category**: depth
- **Pass condition**: Exactly one Echo is named. It must be framed as unexpected (not a
  restatement of a wrong prediction) and must carry enough context for a reader to act on it
  in a future topic. Multiple echoes or an echo that is simply a restatement of a failed
  prediction fails.

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

## Aspirational Criteria (50 points total)

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
- **Pass condition**: Each gap entry names the assumption held without evidence that made the
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
  for the assumption held without evidence -- the inertia belief that made the gap invisible
  before commitment. This is distinct from what the gap would have surfaced: the assumption
  explains why the gap existed, not what it missed. A gap table that names only outcomes
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
  defining the expected value form, not just a field label. This makes the seal a format
  contract rather than a field checklist -- the consumer knows both what must be present and
  what it must look like. Seal fields present but with labels only (no format strings) =
  PARTIAL. Builds on C-21: C-21 requires the seal enumerate fields; C-23 requires those
  enumerations carry format specifications. (2 pts full / 1 pt partial)

### C-24 -- Echo Why-Unexpected Explained
- **Weight**: aspirational  **Category**: depth
- **Pass condition**: The Echo section carries an explicit field or statement naming why the
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
  PARTIAL. No recommendation present = FAIL (C-07 domain). (2 pts full / 1 pt partial)

### C-26 -- Gap Inertia Column Structurally Isolated
- **Weight**: aspirational  **Category**: format
- **Pass condition**: The gap table carries two structurally separate columns (or clearly
  delineated labeled fields): one for the assumption held without evidence (the inertia
  belief) and one for the surfacing outcome (what the signal would have revealed). These two
  fields must be isolated -- not merged into a single cell or combined column. When merged,
  the inertia assumption collapses into outcome language and both C-13 and C-20 fail
  simultaneously. Builds on C-20 (which requires the assumption field exist at all): C-26
  requires it be structurally isolated from the outcome field. Assumption present but merged
  with outcome = PARTIAL. No assumption field = FAIL (C-20 domain, not scored here). (2
  pts full / 1 pt partial)

### C-27 -- Phase Self-Containment Extended to All Phases
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: SEAL coverage and self-containment guarantees extend explicitly to all
  phases of the retrospective -- including the gap analysis phase and the recommendation
  phase. A rubric or output that applies SEAL gates and structural self-containment only to
  early phases leaves the two phases most likely to be abbreviated (gap and recommendation)
  unprotected against silent truncation. Builds on C-19 (all phases must be self-contained)
  and C-21 (seals must enumerate required fields): C-27 requires the full phase scope itself
  be complete and explicit in the skill specification. Early phases with SEAL coverage and
  later phases without explicit SEAL specification = PARTIAL. All phases with named seals =
  PASS. (2 pts full / 1 pt partial)

### C-28 -- Recommendation Slot Completeness Guard
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: A structural slot guard -- implemented as an explicit SEAL check in the
  recommendation phase -- confirms that all required recommendation slots are filled with
  specific content and that no [placeholder] strings survive to the final output. The guard
  converts the bracket-slot template (C-17) from a structural hint into an enforced completion
  contract: the recommendation phase cannot close without the guard confirming all slots
  populated. C-17 requires the template exist; C-28 requires its slots be verifiably filled.
  Template present but no slot guard = PARTIAL. Slot guard present in SEAL with explicit
  placeholder-check = PASS. (2 pts full / 1 pt partial)

### C-29 -- Phase 8 Score Copy Guard
- **Weight**: aspirational  **Category**: correctness
- **Pass condition**: Phase 8 (or the final output phase) carries an explicit "do not
  recompute" instruction requiring the score to be copied verbatim from the Phase 6 accuracy
  computation rather than derived again. Silent recomputation in a closing phase can introduce
  divergence between the scored table and the final summary verdict -- producing a
  self-consistent output that misreports the actual verdict. The copy guard makes the
  score-transfer auditable: a scorer can verify the final score matches Phase 6 by inspection.
  Phase 8 present but score recomputed or no copy instruction = PARTIAL. Explicit copy
  instruction with "do not recompute" = PASS. (2 pts full / 1 pt partial)

### C-30 -- Phase 8 SEAL Copy-Verified Label and Source Named
- **Weight**: aspirational  **Category**: correctness
- **Source**: V-05 C-23/C-29 excellence signal (Round 11)
- **Pass condition**: The SEAL in Phase 8 carries both a named verification label (e.g.,
  COPY-VERIFIED) and an explicit copy-source specification naming the specific source phase
  (e.g., "Phase 6 verdict"). The label makes the copy operation machine-distinguishable from
  a prose assertion; the source specification makes it auditable by inspection without
  requiring a reviewer to trace phases manually to confirm the origin. C-29 requires the copy
  instruction exist; C-30 requires the SEAL encode both the verified state and the copy
  source as named fields -- elevating the copy guard from an instruction to an auditable
  contract. Copy instruction present in Phase 8 but SEAL lacks label or source = PARTIAL.
  SEAL carries both COPY-VERIFIED label and named source = PASS. (2 pts full / 1 pt partial)

### C-31 -- Design Guarantees Summary Explicit
- **Weight**: aspirational  **Category**: format
- **Source**: V-05 C-28 excellence signal (Round 11)
- **Pass condition**: The skill specification includes an explicit design-guarantees summary --
  a dedicated section or block that documents the key structural decisions (slot templates,
  SEAL guards, copy mechanisms, format contracts) in a readable form for maintainers and
  reviewers. Without this summary, structural guarantees are implied only by reading all phase
  specifications in sequence; with it, a reviewer can audit the key guarantees without
  reconstructing them from phase text. The summary must name specific guarantees (e.g.,
  "Three-slot [slot:X] recommendation; SEAL confirms no [slot: strings survive") and not
  merely assert that guarantees exist. Structural guarantees present in phase specs but no
  dedicated summary = PARTIAL. Explicit summary section naming specific guarantees by
  mechanism = PASS. (2 pts full / 1 pt partial)

### C-32 -- Phase 8 SEAL Fields Carry Independent Verification Instructions
- **Weight**: aspirational  **Category**: correctness
- **Source**: V-01 C-30 PASS excellence (Round 12)
- **Pass condition**: Each field in the Phase 8 SEAL carries its own independent verification
  instruction -- a statement of what to check and how -- not shared across fields or collapsed
  into a compound assertion on a single checklist item. V-01 demonstrates this by splitting
  the SEAL into three independently checkable items: `This score` (value present and
  non-blank), `COPY-VERIFIED` (traced to Phase 6 verdict sentence, not recomputed from Phase
  4), and `COPY-SOURCE` (confirmed by reading Phase 6 directly). The per-field instruction
  makes each SEAL item auditable in isolation -- a reviewer can verify one field without
  reading the others. C-30 requires both COPY-VERIFIED label and copy-source be present as
  named fields; C-32 requires each named field carry its own verification instruction. SEAL
  fields present with label and source (C-30 PASS) but verification instructions shared,
  absent, or fused into a compound assertion on one item = PARTIAL. Each SEAL field carries
  its own independent verification instruction = PASS. (2 pts full / 1 pt partial)

### C-33 -- Design Guarantees Section Mechanism-Keyed Table
- **Weight**: aspirational  **Category**: format
- **Source**: V-02 C-31 PASS excellence (Round 12)
- **Pass condition**: The design-guarantees summary uses a two-column table with mechanism
  names as row keys (columns: Mechanism | Structural guarantee -- what is enforced and how).
  A mechanism-keyed table makes each guarantee independently locatable by name without
  sequential reading; a prose list or trailing bullet enumeration requires reading top-to-
  bottom to locate a specific guarantee. V-02 demonstrates this with a `## DESIGN GUARANTEES`
  section containing a two-column table where each row names a mechanism (Echo lock, Copy
  guard -- body, Copy guard -- SEAL, etc.) and states the structural decision that enforces
  it. C-31 requires a dedicated summary section exist; C-33 requires that section use tabular
  form with mechanism names as independently addressable row identifiers. Dedicated section
  present (C-31 PASS) but content in prose or list form = PARTIAL. Two-column
  mechanism-keyed table with named row identifiers = PASS. (2 pts full / 1 pt partial)

---

## Full Scoring Summary

| Tier | Criteria | Points Each | Total |
|------|----------|-------------|-------|
| Essential | C-01--C-05 | 12 | 60 |
| Recommended | C-06--C-08 | 10 | 30 |
| Aspirational | C-09--C-33 | 2 | 50 |
| **Total** | | | **140** |

**Denominator adjustment**: C-10 is non-applicable when no AMEND topic is present.
C-22 is non-applicable when no signals are excluded in any phase.
Effective denominator in non-AMEND runs = 136. In AMEND runs with no per-phase
exclusions = 138. In AMEND runs with per-phase exclusions = 140.

**Partial scoring**: PARTIAL on essential = FAIL for "All essential: YES".
PARTIAL on recommended or aspirational = 1 pt.

---

## Change Log

| Version | Criterion | Source | Signal |
|---------|-----------|--------|--------|
| v11 | C-32 phase-8-seal-fields-independent-verification | V-01 C-30 PASS (Round 12) | V-01 splits the Phase 8 SEAL into three independently checkable items (This score / COPY-VERIFIED / COPY-SOURCE), each carrying its own verification instruction -- C-30 requires label and source be named fields, but V-01 shows the excellence is per-field independence: each item is auditable in isolation without reading the others |
| v11 | C-33 design-guarantees-mechanism-keyed-table | V-02 C-31 PASS (Round 12) | V-02 replaces the trailing bullet list with a two-column ## DESIGN GUARANTEES table (Mechanism | Structural guarantee) -- C-31 requires the dedicated section exist, but V-02 shows the excellence is mechanism names as row keys, making each guarantee independently locatable without sequential reading |
| v10 | C-30 phase-8-seal-copy-verified-label-and-source | V-05 C-23/C-29 excellence (Round 11) | V-05 Phase 8 SEAL adds a COPY-VERIFIED label and explicitly names "Phase 6 verdict" as the copy source; C-29 requires the copy instruction exist, but V-05 encodes both the verified state and the origin as named SEAL fields, making the copy auditable by inspection without tracing phases |
| v10 | C-31 design-guarantees-summary-explicit | V-05 C-28 excellence (Round 11) | V-05 carries a design-guarantees summary stating structural guarantees explicitly (slot template, SEAL slot check) -- guarantees buried across phase specs are invisible to reviewers; an explicit summary section makes them auditable without reconstructing them from phase text |
| v9 | C-28 recommendation-slot-completeness-guard | V-05 C-07 PASS (Round 10) | C-07 was PARTIAL in V-01 through V-04 because the bracket-slot template (C-17) enforces structure but not slot completeness -- placeholder strings can survive to the final output undetected; V-05 closes this with an explicit SEAL guard in the recommendation phase that checks all three slots contain specific content |
| v9 | C-29 phase-8-score-copy-guard | V-05 Phase 8 excellence (Round 10) | Silent recomputation in the closing phase can diverge from the Phase 6 scored table; V-05 adds a "do not recompute" copy instruction that makes the score-transfer auditable by inspection and prevents the self-consistent-but-wrong final verdict failure mode |
| v8 | C-26 gap-inertia-column-isolation | V-05 C-13/C-20 double PASS (Round 9) | C-13 and C-20 resolve simultaneously only when the assumption column is structurally isolated from the outcome column -- merging both into one cell causes both to fail; the structural fix is two separate labeled columns |
| v8 | C-27 phase-self-containment-extended | V-05 C-19 PASS (Round 9) | C-19 reached PASS only when SEAL coverage explicitly extended to all phases; rubrics scoped to early phases left the gap and recommendation phases unprotected, producing the persistent PARTIAL |
| v7 | C-24 echo-why-unexpected-named | V-02 excellence (Round 8) | Echo sections label findings as unexpected but never require the author to name the prior belief that was contradicted -- the belief-correction is the learning, not the label |
| v7 | C-25 recommendation-outcome-measurable | V-02 C-07 PASS (Round 8) | V-02 Phase 5 requires three components: gap/echo addressed + namespace/process step + measurable outcome; existing C-07 and C-17 capture the first two but leave measurability as optional prose |
| v6 | C-22 oos-secondary-table-explicit | V-02 C-10 PASS (Round 7) | OOS secondary table in Phase 2 shows clean scoping: excluded signals get a dedicated secondary table per phase, not a prose note or primary-table footer |
| v6 | C-23 phase-seal-format-strings-per-field | V-04 C-21 PARTIAL (Round 7) | Seal fields present but "format strings per field not confirmed explicit" -- the excellence is each seal field carries a format specification, making it a format contract rather than a checklist |
| v5 | C-20 gap-inertia-assumption-named | C-13 FAIL in V-01 (Round 6) | Gap tables name outcomes; the assumption that made the gap invisible is a distinct field |
| v5 | C-21 phase-seal-explicit | V-02 Phase-Seal design (Round 6) | Per-phase seals name required fields and confirm presence -- stronger than C-19 row-level self-containment, which leaves non-tabular phases unprotected |

Total available: 136 -> 140.
