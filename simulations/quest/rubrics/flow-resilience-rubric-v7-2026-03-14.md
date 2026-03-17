Written to `simulations/quest/rubrics/flow-resilience-rubric-v7-2026-03-14.md`.

---

**Changes from v6 to v7:**

| | v6 | v7 |
|---|---|---|
| Denominator | 17 | 19 |
| New criteria | — | C-26, C-27 |
| R6 ceiling (V-05) re-scored | 94.71 (8/17) | 94.21 (8/19) |
| Open for R7 | C-19 | C-19, C-26, C-27 |

**C-26** (E-10) — Architecture-to-contract forward reference: the C-21 architecture table's Mechanism column must name downstream artifacts by their exact section title, creating a verifiable closed-loop chain. Depends on C-21 passing.

**C-27** (E-11) — Consequence-enumeration in slot-level descriptors: at least one C-23 row descriptor must enumerate distinct business consequences per resolution outcome *before* the fill instruction, making vague fills visibly inadequate against named stakes. Depends on C-23 passing.

Both dependency guards (C-21 required for C-26, C-23 required for C-27) are encoded in the pass conditions — a variation can't earn the derived criterion without earning the structural criterion it extends.
tifact by its exact
title as it appears elsewhere in the prompt. The named artifact must actually exist in the
prompt. A description of mechanism function without a title-level pointer fails. C-21 must
also pass — C-26 cannot pass if C-21 fails.

### C-27 — Consequence-Enumeration in Slot-Level Descriptors *(E-11)*
A slot-level row descriptor (C-23) names the specific business consequences of each
possible resolution outcome *before* the fill requirement — for example, "oversell if
resolution A wins, double-charge if resolution B wins, duplicate fulfillment if merge is
naive." This elevates the fill requirement from a content specification to an outcome
specification: a vague fill becomes visibly inadequate against named stakes. A descriptor
that specifies what content to write without enumerating per-outcome consequences does not
satisfy this criterion.

**Pass condition**: At least one row descriptor contains consequence-enumeration of the
form "X consequence if outcome A, Y consequence if outcome B" (or equivalent) positioned
before the fill instruction for that row. The consequences must be business-level (not
purely technical) and must be distinct per outcome. A descriptor that names a single
consequence without branching across outcomes does not satisfy this criterion. C-23 must
also pass — C-27 cannot pass if C-23 fails.

---

**Updated scoring formula**: `aspirational_pass/19 * 10` (denominator bumped from 17 to 19).

**Under v7**: V-05 is the Round 6 ceiling at 94.71. Under v7 it scores 8/19 x 10 = 4.21
for aspirational (C-17, C-18, C-20, C-21, C-22, C-23, C-24, C-25 pass; C-19, C-26, C-27
fail), yielding composite = 60 + 30 + 4.21 = **94.21**. C-19 (slot-level imperatives
inside a per-row field table schema), C-26 (architecture-to-contract forward reference),
and C-27 (consequence-enumeration in slot descriptors) remain open for Round 7. C-26 is
achievable by adding a title-level pointer in V-05's architecture table Mechanism column;
C-27 requires promoting at least one Row Descriptor to enumerate per-outcome business
consequences before the fill.

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
in a checklist after the table do not satisfy this criterion. A prose section adjacent to
the output table (not inside a per-row field table schema) also does not satisfy this
criterion.

### C-20 — Column-Level Ownership Assignment
The prompt assigns an explicit owner (e.g., role name, expert label) to each column in the
scenario table, either via inline column-header labels or via a structural ownership
specification.

**Pass condition**: Every column in the scenario table has a named owner. Ownership implied
by section headers (e.g., a "Commerce Expert" heading above a sub-table) does not satisfy
this criterion — ownership must be assigned per column.

### C-21 — Layered Granularity Architecture *(E-5)*
The prompt explicitly architects its four anti-omission mechanisms as a coordinated
four-level stack: one mechanism per structural level (table-level unified index -> C-17,
section-level phase gates -> C-18, slot-level in-row imperatives -> C-19, column-level
ownership -> C-20). Each mechanism targets a distinct omission risk at a distinct structural
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

### C-26 — Architecture-to-Contract Forward Reference *(E-10)*
The four-level anti-omission architecture table (C-21) contains a Mechanism column entry
that names a downstream artifact by its exact section title — for example, "defined in the
Column Contract (below)" or "see Row Descriptors section below." This creates a
closed-loop verifiable chain: the architecture announces its own artifacts by name before
those artifacts appear, so a reader can confirm each promised artifact exists and a model
cannot omit the named artifact without visibly breaking the chain. An architecture table
that describes what a mechanism *does* without naming the downstream artifact by section
title does not satisfy this criterion — the forward reference must be by name, not by
function.

**Pass condition**: At least one row in the architecture table (C-21) has a Mechanism
column entry that names a downstream section, table, or structural artifact by its exact
title as it appears elsewhere in the prompt. The named artifact must actually exist in the
prompt. A description of mechanism function without a title-level pointer fails. C-21 must
also pass — C-26 cannot pass if C-21 fails.

### C-27 — Consequence-Enumeration in Slot-Level Descriptors *(E-11)*
A slot-level row descriptor (C-23) names the specific business consequences of each
possible resolution outcome *before* the fill requirement — for example, "oversell if
resolution A wins, double-charge if resolution B wins, duplicate fulfillment if merge is
naive." This elevates the fill requirement from a content specification to an outcome
specification: a vague fill becomes visibly inadequate against named stakes. A descriptor
that specifies what content to write without enumerating per-outcome consequences does not
satisfy this criterion.

**Pass condition**: At least one row descriptor contains consequence-enumeration of the
form "X consequence if outcome A, Y consequence if outcome B" (or equivalent) positioned
before the fill instruction for that row. The consequences must be business-level (not
purely technical) and must be distinct per outcome. A descriptor that names a single
consequence without branching across outcomes does not satisfy this criterion. C-23 must
also pass — C-27 cannot pass if C-23 fails.

---

**Scoring formula**: `aspirational_pass/19 * 10`

**Ceiling reference under v7**:
- V-05 (Round 6 best): C-17 PASS, C-18 PASS, C-19 FAIL, C-20 PASS, C-21 PASS,
  C-22 PASS, C-23 PASS, C-24 PASS, C-25 PASS, C-26 FAIL, C-27 FAIL -> 8/19 x 10 = 4.21
  -> composite = 60 + 30 + 4.21 = **94.21**
- C-19 (slot-level imperatives inside per-row field table schema), C-26
  (architecture-to-contract forward reference), and C-27 (consequence-enumeration in
  slot descriptors) remain open for Round 7.
