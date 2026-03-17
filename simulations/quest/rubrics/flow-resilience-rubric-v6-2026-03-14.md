Reading the scorecard carefully, I can extract two new excellence signals:

- **E-8** → **C-24**: Column-ownership meta-table as pre-output specification
- **E-9** → **C-25**: Two-symptom anti-boundary negation pattern (closes escape routes)

Denominator bumps from 15 → 17.

```markdown
# Rubric: flow-resilience — v6

**Two new aspirational criteria added from Round 5 excellence signals:**

### C-24 — Column-Ownership Meta-Table as Pre-Output Specification *(E-8)*
The prompt includes a separate meta-table (columns: Name / Owner / Fill Requirement)
placed before the output table itself. This creates structural pre-commitment: the model
processes per-column responsibility before constructing any row, making column omission
detectable as a contract violation rather than an oversight. A parenthetical label in a
column header, a role-section heading above the table, or inline ownership notes inside
a row descriptor do not satisfy this criterion — the meta-table must be a standalone
structure positioned before the first output row.

**Pass condition**: A discrete meta-table with at least Name, Owner, and Fill Requirement
columns (or equivalent fields) appears in the prompt before the scenario output table. The
meta-table must cover every column in the output table. If any output column lacks a
corresponding meta-table entry, the criterion fails.

### C-25 — Two-Symptom Anti-Boundary Negation Pattern *(E-9)*
The anti-boundary instruction names two distinct structural artifacts that must not appear.
The pairing is load-bearing: the first negation addresses table splitting (e.g., "Do not
create separate tables for Commerce Expert columns and Distributed Systems Expert columns"),
and the second addresses invisible boundary insertion (e.g., "Do not insert a horizontal
rule, heading, or section break between rows when column ownership shifts"). A model that
satisfies negation-1 by consolidating tables could still insert a `---` separator;
negation-2 closes that escape route. Single-symptom instructions leave at least one
structural escape route open.

**Pass condition**: The anti-boundary instruction names at least two distinct structural
artifacts to avoid — one artifact addressing table-level splitting and one addressing
intra-table boundary insertion (horizontal rule, heading, section break, or equivalent).
Both negations must be present. A prompt that satisfies C-22 (two symptom-level negations)
but targets the same class of artifact (e.g., two sub-table variants) does not satisfy
C-25 — the two negations must address different boundary mechanisms.

---

**Updated scoring formula**: `aspirational_pass/17 * 10` (denominator bumped from 15 to 17).

**Under v6**: V-02 is the Round 5 ceiling at 92.7. Under v6 it scores 4/17 × 10 = 2.35
for aspirational (C-17, C-18, C-20, C-22 pass; C-21, C-23, C-24, C-25 fail — C-22 passes
the two-symptom test but C-25 requires the two negations to address different boundary
mechanisms, which V-02 satisfies; on reflection C-25 PASS for V-02), yielding
5/17 × 10 = 2.94, composite = 60 + 30 + 2.94 = **92.94**. C-21 (explicit four-level
architecture naming) and C-23 (cell-embedded bold imperatives) remain open for Round 6.
C-24 (column-ownership meta-table) is achievable in Round 6 by promoting V-02's implicit
pattern to an explicit pre-output spec.

---

## Essential Criteria (must pass all — 60% of score)

### C-01 — Scenario Coverage
- **Weight**: essential
- **Category**: coverage
- **Text**: The output covers all three resilience scenario classes: (1) full connectivity
  loss (client offline), (2) partial failure (dependent service unavailable), and (3)
  concurrent writes across a partition (split-brain / eventual-consistency conflict).
- **Pass condition**: All three classes are represented by distinct named scenarios. A
  single scenario that attempts to cover all three classes fails. Scenarios that collapse
  class 2 and class 3 into a single "network issue" fail.

### C-02 — Four-Field Structure Per Scenario
- **Weight**: essential
- **Category**: structure
- **Text**: Every failure scenario includes all four required fields: (1) state — what the
  system state is when failure occurs; (2) capability — what the user can still do; (3)
  data at risk — what data may be lost, stale, or inconsistent; (4) recovery path — how
  the system returns to a healthy state.
- **Pass condition**: Every scenario present in the output includes all four fields with
  non-trivial content (not placeholder or "N/A"). A scenario missing any field fails this
  criterion.

### C-03 — Gap Identification
- **Weight**: essential
- **Category**: correctness
- **Text**: The output identifies at least one offline experience gap, at least one data
  consistency violation, and at least one missing recovery flow as distinct findings.
- **Pass condition**: All three finding types appear, each labeled and actionable (not just
  implied). Generic statements like "offline support may be limited" without specificity
  fail.

### C-04 — Distributed Systems Accuracy
- **Weight**: essential
- **Category**: correctness
- **Text**: Technical claims about failure modes are consistent with distributed systems
  fundamentals: CAP theorem trade-offs, retry semantics, idempotency requirements, and
  conflict-resolution strategies are used correctly where referenced.
- **Pass condition**: No materially incorrect distributed-systems claim is present.
  Fabricated error codes, invented protocols, or impossible consistency guarantees fail
  this criterion.

### C-05 — Commerce Domain Grounding
- **Weight**: essential
- **Category**: depth
- **Text**: The analysis is grounded in the commerce / distributed systems domain. Failure
  scenarios reference realistic commerce flows (e.g., checkout, inventory reservation,
  payment processing, order fulfillment) rather than generic CRUD operations.
- **Pass condition**: At least two scenarios are anchored to a recognizable commerce
  operation. Purely abstract or domain-agnostic scenarios fail.

---

## Recommended Criteria (improve output quality — 30% of score)

### C-06 — Severity and Blast Radius Classification
- **Weight**: recommended
- **Category**: depth
- **Text**: Each failure scenario is annotated with a severity level (e.g., degraded /
  impaired / down) and a blast radius (what percentage or which segment of users is
  affected). This helps triage prioritization.
- **Pass condition**: At least half of the scenarios carry both a severity label and a
  blast-radius estimate or qualifier (e.g., "affects all users in offline mode", "affects
  <1% under split-brain").

---

## Aspirational Criteria (ceiling-raising — 10% of score)

### C-17 — Unified Table Index
The prompt includes a `#` column (or equivalent row identifier) in the scenario table and
contains an explicit instruction prohibiting the model from splitting the table across
scenario classes, role sections, or any other structural boundary.

**Pass condition**: A row-index column is present AND the prompt contains an explicit
anti-split instruction referencing the unified table. A `#` column without an anti-split
instruction scores PARTIAL, not PASS.

### C-18 — Section-Level Phase Gate
The prompt contains an explicit instruction requiring the model to complete all scenario
table rows before advancing to subsequent output sections (e.g., Gap Register, Findings,
Recommendations). The gate instruction names the boundary condition by section name.

**Pass condition**: An explicit gate instruction of the form "Produce all N rows before
writing [section name]" (or equivalent) appears in the prompt. An implicit sequencing
expectation (e.g., table appearing before gap register in an example output) does not
satisfy this criterion.

### C-19 — Slot-Level In-Row Imperatives
Bold imperative text is embedded inside the Content field descriptor of at least two
scenario table rows, co-located at cell granularity rather than in preamble, blockquotes,
or section headers. The pattern is: **"Write this row now."** followed by the fill
requirement, followed by **"Do not advance to row N until [condition]."**

**Pass condition**: At least two Content field descriptors contain embedded bold imperative
text matching the "Write this row now / Do not advance" pattern inside the cell content
itself. Instructions appearing above the table, in a blockquote before the first row, or
in a checklist after the table do not satisfy this criterion.

### C-20 — Column-Level Ownership Assignment
The prompt assigns an explicit owner (e.g., role name, expert label) to each column in the
scenario table, either via inline column-header labels or via a structural ownership
specification.

**Pass condition**: Every column in the scenario table has a named owner. Ownership implied
by section headers (e.g., a "Commerce Expert" heading above a sub-table) does not satisfy
this criterion — ownership must be assigned per column.

### C-21 — Layered Granularity Architecture *(E-5)*
The prompt explicitly architects its four anti-omission mechanisms as a coordinated
four-level stack: one mechanism per structural level (table-level unified index → C-17,
section-level phase gates → C-18, slot-level in-row imperatives → C-19, column-level
ownership → C-20). Each mechanism targets a distinct omission risk at a distinct structural
level, so no two mechanisms conflict with or duplicate each other.

**Pass condition**: The prompt explicitly names all four structural levels (table, section,
slot, column) and assigns a distinct anti-omission mechanism to each. Implicit satisfaction
— a prompt that happens to use all four mechanisms without naming the four-level
architecture — fails. An output that names only two or three levels without the fourth
also fails.

### C-22 — Anti-Boundary Instruction by Structural Symptom *(E-6)*
The anti-boundary instruction names the failure mode by its structural symptom in output —
what the artifact would look like if the model misread the ownership transition as a section
cue — rather than by the intent violation alone. It says "not a sub-table boundary, not a
role-sequence trigger" rather than only "keep all rows in a single table." Symptom-naming
prevents the model from satisfying the letter of the instruction while still producing a
structural boundary under a different label.

**Pass condition**: The anti-boundary instruction includes at least two symptom-level
negations that name specific structural artifacts to avoid (e.g., "not a sub-table
boundary", "not a role-sequence trigger", "not a horizontal rule between ownership
blocks"). An instruction that states only a positive ("keep rows together", "use one
table") without negating at least two symptom forms fails — even if the unified row
index (C-17) passes.

### C-23 — In-Row Bold Imperative as Genuine Slot-Level Co-location *(E-7)*
Bold imperative text embedded inside the Content field descriptor of a scenario table row
— phrased as **"Write this row now."** followed by the fill requirement, followed by
**"Do not advance to row N until [condition]."** — is genuine slot-level co-location. The
model reads this text exactly when constructing that cell, operating below section gates
(which the model passes before entering table construction) and below table-level
blockquotes or preamble (which appear before the first row). This makes it structurally
impossible to satisfy section-level or preamble-level instructions and then omit the row.

**Pass condition**: At least two Content field descriptors in the scenario table contain
bold imperative text matching the pattern "Write this row now" / "Do not advance to row N
until [condition]" embedded inside the cell content itself. A blockquote appearing above
the table, a section header before the row, or a checklist after the table does not satisfy
this criterion — the imperative must be co-located inside the Content descriptor at cell
granularity.

### C-24 — Column-Ownership Meta-Table as Pre-Output Specification *(E-8)*
The prompt includes a separate meta-table (columns: Name / Owner / Fill Requirement)
placed before the output table itself. This creates structural pre-commitment: the model
processes per-column responsibility before constructing any row, making column omission
detectable as a contract violation rather than an oversight. A parenthetical label in a
column header, a role-section heading above the table, or inline ownership notes inside a
row descriptor do not satisfy this criterion — the meta-table must be a standalone
structure positioned before the first output row.

**Pass condition**: A discrete meta-table with at least Name, Owner, and Fill Requirement
columns (or equivalent fields) appears in the prompt before the scenario output table. The
meta-table must cover every column in the output table. If any output column lacks a
corresponding meta-table entry, the criterion fails.

### C-25 — Two-Symptom Anti-Boundary Negation Pattern *(E-9)*
The anti-boundary instruction names two distinct structural artifacts that must not appear.
The pairing is load-bearing: the first negation addresses table splitting (e.g., "Do not
create separate tables for Commerce Expert columns and Distributed Systems Expert columns"),
and the second addresses invisible boundary insertion (e.g., "Do not insert a horizontal
rule, heading, or section break between rows when column ownership shifts"). A model that
satisfies negation-1 by consolidating tables could still insert a `---` separator;
negation-2 closes that escape route. Single-symptom instructions leave at least one
structural escape route open.

**Pass condition**: The anti-boundary instruction names at least two distinct structural
artifacts to avoid — one artifact addressing table-level splitting and one addressing
intra-table boundary insertion (horizontal rule, heading, section break, or equivalent).
Both negations must be present. A prompt that satisfies C-22 (two symptom-level negations)
but targets the same class of artifact (e.g., two sub-table variants) does not satisfy
C-25 — the two negations must address different boundary mechanisms.

---

**Scoring formula**: `aspirational_pass/17 * 10`

**Ceiling reference under v6**:
- V-02 (Round 5 best): C-17 PASS, C-18 PASS, C-19 FAIL, C-20 PASS, C-21 FAIL,
  C-22 PASS, C-23 FAIL, C-24 FAIL, C-25 PASS → 5/17 × 10 = 2.94
  → composite = 60 + 30 + 2.94 = **92.94**
- C-21 (explicit four-level stack naming), C-23 (cell-embedded bold imperatives),
  and C-24 (pre-output meta-table) remain open for Round 6.
```
