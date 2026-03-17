Written to `simulations/quest/rubrics/flow-resilience-rubric-v8-2026-03-14.md`.

---

**Changes from v7 to v8:**

| | v7 | v8 |
|---|---|---|
| Denominator | 19 | 21 |
| New criteria | — | C-28, C-29 |
| R7 ceiling (V-05) re-scored | 95.79 (11/19) | 95.24 (11/21) |
| R8 ceiling (V-05) | — | 96.19 (13/21) |
| Open for R9 | none | none (all cracked by R8 V-05) |

---

**C-28** (E-12) — Sub-Field Completeness Gate in Slot-Level Imperative

Source: V-02's Phase Gate and Row Descriptor cells, which read "Do not advance until row N contains non-placeholder content in every column **including all four Recovery Path stages**." This gate operates below column granularity — the advance condition is not "fill the cell" but "fill all named sub-components within the cell." A model that writes only two of four lifecycle stages satisfies a generic "non-placeholder" gate but visibly fails a named-stage gate.

Dependency: C-19 must pass (no slot-level imperative = no sub-field gate to name into).

---

**C-29** (E-13) — Chronic Consequence Enumeration

Source: V-03/V-05's Status Quo Risk column, which enumerates what *continues* if the resilience gap is never fixed — "oversell rate accumulates per-deploy", "duplicate charges compound indefinitely." This is distinct from C-27's acute per-resolution-branch consequences ("if node A wins: oversold; if node B wins: reverted"). Together they constitute a two-horizon outcome specification: incident impact (C-27, acute) + carrying cost of inaction (C-29, chronic).

Dependency: C-27 must pass — the chronic framing extends the acute model rather than replacing it.

---

**R8 discrimination under v8:** V-05 (all three axes) uniquely earns both C-28 and C-29, separating it from V-01/V-02/V-03/V-04 at the rubric level for the first time. V-02/V-04 earn C-28 only (95.71); V-03 earns C-29 only (95.71); V-05 earns both (96.19). The saturation signal from E-1 is preserved: the rubric now discriminates among variations that were previously indistinguishable.
Status Quo Risk column chronic
  enumeration), yielding composite = 60 + 30 + 6.19 = **96.19**. This is the new ceiling.
- R8 breakdown by variation under v8:
  - V-01 (role reorder only): C-28 FAIL, C-29 FAIL -> 11/21 = 5.24 -> **95.24**
  - V-02 (4-stage Recovery Path): C-28 PASS, C-29 FAIL -> 12/21 = 5.71 -> **95.71**
  - V-03 (Status Quo Risk column): C-28 FAIL, C-29 PASS -> 12/21 = 5.71 -> **95.71**
  - V-04 (D-first + 4-stage): C-28 PASS, C-29 FAIL -> 12/21 = 5.71 -> **95.71**
  - V-05 (all three axes): C-28 PASS, C-29 PASS -> 13/21 = 6.19 -> **96.19**

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

### C-28 — Sub-Field Completeness Gate in Slot-Level Imperative *(E-12)*
A slot-level advance-inhibitor condition (C-19) names specific sub-fields or sub-stages
within a column's fill requirement as non-bypass components — for example, "Do not advance
to row N until this row contains non-placeholder content in every column **including all
four Recovery Path stages**." This moves the gate below column granularity: the condition
is not satisfied by filling the cell with any non-placeholder content, but only by filling
all named sub-components within the cell. A partial fill of a structured column (e.g.,
writing only two of four required lifecycle stages) becomes visibly inadequate against a
named-stage gate in a way it would not against a generic "non-placeholder" gate.

**Pass condition**: At least one slot-level advance-inhibitor condition (C-19) names a
specific sub-field, sub-stage, or sub-component from the column's fill specification —
e.g., a named lifecycle stage, a named field within a structured cell, or an enumerated
requirement list — as part of the non-bypass condition. The named sub-field must exist
as a defined sub-structure in the Column Contract or an equivalent column specification.
A gate that reads only "non-placeholder content" without naming any sub-structure does not
satisfy this criterion. C-19 must also pass — C-28 cannot pass if C-19 fails.

### C-29 — Chronic Consequence Enumeration *(E-13)*
At least one scenario row names the accumulating business consequence of *not* addressing
the resilience gap — the carrying cost of inaction — distinct from the per-resolution-
branch acute consequences required by C-27. The chronic enumeration takes the form "if
this gap is never addressed, [ongoing consequence]" — for example, "oversell rate
accumulates per-deploy", "payment reconciliation backlog grows unbounded", "duplicate
fulfillment charges compound indefinitely." This creates a two-horizon outcome
specification within the row: C-27 names what goes wrong during the incident (acute,
per-resolution-branch), and C-29 names what continues to accumulate if the scenario is
never resolved (chronic, carrying-cost). A row that specifies only incident-moment
consequences — even with multiple branches — does not satisfy this criterion.

**Pass condition**: At least one scenario row contains a chronic-consequence statement
that: (1) is business-level (not purely technical), (2) is framed as a persistent or
accumulating effect of inaction rather than an incident-moment outcome, and (3) is
distinct from the per-resolution-branch acute consequences in C-27. A statement that
names a consequence only at incident time (even if phrased as "will result in") without
framing the accumulating or indefinite character of the harm does not satisfy this
criterion. C-27 must also pass — C-29 cannot pass if C-27 fails.

---

**Scoring formula**: `aspirational_pass/21 * 10`

**Ceiling references under v8**:
- V-05 (Round 7 best, re-scored): C-17 PASS, C-18 PASS, C-19 PASS, C-20 PASS, C-21 PASS,
  C-22 PASS, C-23 PASS, C-24 PASS, C-25 PASS, C-26 PASS, C-27 PASS, C-28 FAIL, C-29 FAIL
  -> 11/21 x 10 = 5.24 -> composite = 60 + 30 + 5.24 = **95.24**
- V-02 (Round 8, 4-stage Recovery Path): C-28 PASS, C-29 FAIL -> 12/21 x 10 = 5.71
  -> composite = 60 + 30 + 5.71 = **95.71**
- V-03 (Round 8, Status Quo Risk column): C-28 FAIL, C-29 PASS -> 12/21 x 10 = 5.71
  -> composite = 60 + 30 + 5.71 = **95.71**
- V-04 (Round 8, D-first + 4-stage): C-28 PASS, C-29 FAIL -> 12/21 x 10 = 5.71
  -> composite = 60 + 30 + 5.71 = **95.71**
- V-05 (Round 8, all three axes): C-28 PASS, C-29 PASS -> 13/21 x 10 = 6.19
  -> composite = 60 + 30 + 6.19 = **96.19** (new ceiling)
- Open for R9: none — both C-28 and C-29 cracked by R8 V-05.
