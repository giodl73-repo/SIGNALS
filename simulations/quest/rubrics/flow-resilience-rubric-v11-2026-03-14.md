Written to `simulations/quest/rubrics/flow-resilience-rubric-v11-2026-03-14.md`.

---

**Changes from v10 to v11:**

| | v10 | v11 |
|---|---|---|
| Denominator | 26 | 29 |
| New criteria | — | C-35, C-36, C-37 |
| R10 ceiling re-scored | 96.92 (18/26) | 96.21 (18/29) |
| R11 ceiling | — | 97.24 (21/29) |
| Open for R12 | none | none (V-03/V-05 crack all three) |

**Three new aspirational criteria added:**

**C-35 (E-19) — Pre-Table Inertia Assessment with Per-Class Carrying Cost Pre-Commitment**
The Status Quo Risk column becomes a constrained fill: a named pre-table section establishes per-class carrying costs, and the Column Contract + row descriptors require fills to reference those pre-committed costs rather than author consequences independently. A model cannot abbreviate without visibly contradicting the prior strategic framing. Depends on C-31.

**C-36 (E-20) — Per-Class Inertia Tipping Point Signal**
The Inertia Assessment sub-section requires one observable threshold expression per failure class (quantified condition + named metric) at which deferral becomes indefensible — applying the C-33 threshold+detection-signal standard to the inertia competitor. Depends on C-35.

**C-37 (E-21) — Inertia Verdict Post-Gap Register**
A second section-level phase gate: after the Gap Register, a named Inertia Verdict synthesizes gap findings + pre-committed carrying costs into HIGH/MEDIUM/LOW threat level with the single strongest argument against deferral. Closes the three-position inertia loop: pre-table assessment → per-row Status Quo Risk → post-gap verdict. Depends on C-35.

**R11 discrimination:** V-01/V-02/V-04 remain at 18/29 = 96.21. V-03 (inertia-first) and V-05 (all axes) tie at 21/29 = 97.24 — the new ceiling. Axes A and B introduce no new rubric surface; Axis C alone raises it.
ssential
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

### C-30 — SLA-Annotated Recovery Path Stages *(E-14)*
Each of the four Recovery Path lifecycle stages (Detect, Contain, Recover, Validate) is
paired with a named SLA target type in the column specification or row descriptor —
specifically Detect/TTD (Time to Detect), Contain/TTC (Time to Contain), Recover/TTR
(Time to Recover), Validate/TTV (Time to Validate), or equivalent named measurable
commitments. This transforms the Recovery Path from a qualitative sequence into a testable
commitment specification: a fill that names stage actions without corresponding SLA targets
is incomplete against this standard in a way it would not be against a stage-name-only
gate. A row descriptor or column specification that lists stage names only ("Detect,
Contain, Recover, Validate") without pairing each stage to a measurement type does not
satisfy this criterion.

**Pass condition**: At least one Recovery Path column specification or row descriptor
pairs each of the four named lifecycle stages with a corresponding named SLA target type.
The pairing must appear in a column specification, column contract entry, or row
descriptor — not only in an example output row. The four pairings must be complete: a
specification that pairs two stages with SLA targets but leaves the other two unnamed
fails. C-28 must also pass — C-30 cannot pass if C-28 fails.

### C-31 — Three-Component Chronic Accumulation Framing *(E-15)*
At least one chronic-consequence specification (C-29) structures the accumulating harm as
three named components: (1) a *rate component* — a qualifier naming the accumulation
interval or trigger (e.g., "per-deploy", "per-transaction", "per-incident"); (2) a
*horizon component* — a qualifier naming the trajectory without intervention (e.g.,
"indefinitely", "without ceiling", "unbounded", "compound growth"); and (3) a *metric
component* — a named business metric that accumulates (e.g., oversell count,
reconciliation backlog items, duplicate charge events). This tightens C-29's chronic
framing from a binary "inaction has consequences" assertion to a quantified accumulation
model: a reader can estimate magnitude (rate), duration (horizon), and what is being
measured (metric). A chronic statement that names a consequence without both a rate
qualifier and a horizon qualifier does not satisfy this criterion, even if it names a
business metric.

**Pass condition**: At least one chronic-consequence statement contains all three
components — rate qualifier, horizon qualifier, and named business metric — present in
the same statement or in immediately adjacent cells in the same row. The rate and horizon
qualifiers must be distinct: a statement of the form "X accumulates" without naming an
accumulation interval (rate) or a trajectory bound (horizon) fails even if X is a named
metric. C-29 must also pass — C-31 cannot pass if C-29 fails.

### C-32 — Intra-Row Column-Group Gate (5-Level Architecture) *(E-16)*
The prompt extends the four-level anti-omission architecture (C-21) to five levels by
adding an intra-slot column-group sequencing gate: within a single scenario row, columns
assigned to one owner phase (e.g., C-phase: Commerce Expert columns) must be complete
before columns assigned to the next owner phase (e.g., D-phase: Distributed Systems Expert
columns) are begun. This gate operates at a level below the slot (row) and above the
individual column — targeting the risk that an ownership transition mid-row is misread as
a section boundary. The five-level naming is load-bearing: a prompt that uses the gate
without naming all five levels cannot demonstrate that the mechanism targets a distinct
structural level rather than restating column-level ownership (C-20).

**Pass condition**: The prompt explicitly names all five structural levels (table, section,
slot, column-group, column) and assigns a distinct advance-inhibitor to the column-group
level — specifying that one ownership phase's columns must be complete before the next
phase begins within the same row. The gate must be positioned inside the row descriptor
(at slot level or below), not in preamble or a section-level note. C-21 must also pass —
C-32 cannot pass if C-21 fails.

### C-33 — Trigger Condition Column Specification *(E-17)*
The prompt specifies a Trigger Condition column (or equivalently named entry-bounding
column) that pairs each scenario with both a threshold expression and a detection signal.
The threshold expression is a quantified condition that activates the scenario (e.g.,
"inventory count drops below safety-stock threshold", "payment API latency exceeds 500ms
p99"). The detection signal is the observable mechanism by which the system identifies
the threshold being crossed (e.g., "inventory-service health probe returns degraded",
"payment-provider timeout counter increments"). This transforms each scenario from a
reactive failure description into a bounded detection specification: the scenario is
active only when the named observable condition is met, and the detection signal defines
the monitoring obligation. A scenario bounded only by failure class without a threshold
expression and detection signal cannot be operationalized for alerting.

**Pass condition**: A Trigger Condition column (or equivalent) appears in the Column
Contract meta-table (C-24) with a Fill Requirement specifying both a threshold expression
and a detection signal as distinct components. At least one row descriptor fills both
components with non-generic content. A trigger description that is qualitative only
("when the service is unavailable") without a threshold expression fails. C-24 must also
pass — C-33 cannot pass if C-24 fails.

### C-34 — Verification Signal per Recovery Stage *(E-18)*
Each of the four Recovery Path lifecycle stages (Detect, Contain, Recover, Validate)
carries three components in the column specification or row descriptor: (1) *mechanism* —
the action taken to advance the stage; (2) *SLA target* — the named time commitment
(TTD/TTC/TTR/TTV from C-30); and (3) *Verification Signal (VS)* — a named observable
artifact that confirms the stage is complete (e.g., "inventory-service heartbeat returns
200", "payment provider ACK logged to audit trail", "dual-write conflict counter resets
to 0 for 60s"). The VS makes the recovery specification falsifiable per stage: a stage is
not complete until the named observable artifact appears, independent of elapsed time
alone. A recovery path that names mechanism and SLA without a VS cannot be operationally
verified — the SLA records duration but does not confirm the stage outcome.

**Pass condition**: The Recovery Path column specification or at least one row descriptor
requires all three components — mechanism, SLA target, and named Verification Signal —
for each of the four lifecycle stages. The VS must be named (not described generically as
"confirmation" or "verified") in the column specification or a row descriptor. The VS
must be observable (a system state, log entry, metric value, or API response code) and
must be distinct from a re-statement of the mechanism. C-30 must also pass — C-34 cannot
pass if C-30 fails.

### C-35 — Pre-Table Inertia Assessment with Per-Class Carrying Cost Pre-Commitment *(E-19)*
The prompt includes a named section (e.g., "Step 1: Inertia Assessment") positioned before
the scenario table that establishes per-class carrying costs for each of the three failure
classes. The Column Contract specifies that the Status Quo Risk column must be filled
consistently with the carrying costs pre-committed in this section (not authored
independently per row). At least one row descriptor reinforces the constraint by naming
the pre-table section as the reference source for that row's Status Quo Risk fill — e.g.,
"Status Quo Risk must use the metric established for Class N in the Inertia Assessment."
This transforms the Status Quo Risk column from a per-row independent assertion into a
constrained fill: a model cannot abbreviate chronic consequences without visibly
contradicting a prior strategic-level pre-commitment made before the table was constructed.
A prompt where Status Quo Risk is independently authored per row without a pre-committed
reference — even if the column passes C-29 and C-31 — does not satisfy this criterion.

**Pass condition**: A named pre-table section explicitly establishes per-class carrying
costs for all three scenario classes. The Column Contract entry for Status Quo Risk names
the pre-table section as the reference source for the fill (not a fill requirement standing
alone). At least one row descriptor names the pre-table section as the constraint source
for that row's Status Quo Risk fill. C-31 must also pass — C-35 cannot pass if C-31 fails.

### C-36 — Per-Class Inertia Tipping Point Signal *(E-20)*
The pre-table Inertia Assessment (C-35) includes a sub-section requiring, for each of the
three failure classes, a named observable threshold expression at which the carrying cost
has crossed a point where deferral becomes indefensible — paired with a named metric being
monitored (e.g., "oversell-event count exceeds 50 per month", "cart-abandonment rate rises
more than 2% above baseline"). This applies the C-33 threshold+detection-signal standard
to the inertia assessment: just as C-33 makes each failure scenario falsifiable by entry
condition, C-36 makes each inertia claim falsifiable by exit condition. A qualitative
inertia assessment ("this will get worse over time") without a named threshold expression
and monitored metric does not satisfy this criterion — the tipping point must be
operationalizable for alerting.

**Pass condition**: The pre-table Inertia Assessment contains a sub-section requiring one
observable signal per failure class, each signal specifying both a threshold expression
(quantified condition) and a named metric being monitored. The threshold expression must
be quantified — "oversell-event count exceeds 50/month" satisfies; "worsens over time"
does not. All three failure classes must be covered; a tipping point for only one or two
classes fails. C-35 must also pass — C-36 cannot pass if C-35 fails.

### C-37 — Inertia Verdict Post-Gap Register *(E-21)*
A section positioned after the Gap Register (and structurally dependent on its completion)
synthesizes the gap findings and the pre-committed carrying costs from the Inertia
Assessment (C-35) into a single verdict: a HIGH/MEDIUM/LOW inertia threat level with the
single strongest argument against deferral (2-3 sentences). This creates a second
section-level phase gate — the Gap Register must be complete before the verdict can be
written — and closes the inertia specification loop across three structural positions:
(1) pre-table Inertia Assessment establishes the carrying cost framing, (2) per-row
Status Quo Risk fills from the pre-committed costs, (3) the post-gap Inertia Verdict
synthesizes gaps and costs into an actionable threat assessment. A prompt that includes
an inertia section before the table without requiring a corresponding post-gap synthesis
closes only two of the three positions and does not satisfy this criterion.

**Pass condition**: A section appearing after the Gap Register requires a named Inertia
Verdict specifying a threat level (HIGH/MEDIUM/LOW or equivalent ordinal scale) and a
single strongest argument against deferral. The verdict section must name both the gap
findings and the pre-committed carrying costs (from the pre-table Inertia Assessment) as
inputs to the judgment. The verdict must be structurally dependent on Gap Register
completion — positioned after the three gap findings or gated by an explicit instruction
naming the Gap Register as a prerequisite. C-35 must also pass — C-37 cannot pass if
C-35 fails.

---

**Scoring formula**: `aspirational_pass/29 * 10`

**Ceiling references under v11**:
- V-05 (Round 7 best, re-scored): C-17 through C-27 PASS, C-28 through C-37 FAIL
  -> 11/29 x 10 = 3.79 -> composite = 60 + 30 + 3.79 = **93.79**
- V-05 (Round 8, all three axes, re-scored): C-17 through C-29 PASS, C-30 through C-37 FAIL
  -> 13/29 x 10 = 4.48 -> composite = 60 + 30 + 4.48 = **94.48**
- V-05 (Round 9, all three axes, re-scored): C-17 through C-31 PASS, C-32 through C-37 FAIL
  -> 15/29 x 10 = 5.17 -> composite = 60 + 30 + 5.17 = **95.17**
- V-05 (Round 10, all three axes, re-scored): C-17 through C-34 PASS, C-35 through C-37 FAIL
  -> 18/29 x 10 = 6.21 -> composite = 60 + 30 + 6.21 = **96.21**
- V-01 (Round 11, D-phase-first): C-35 FAIL, C-36 FAIL, C-37 FAIL
  -> 18/29 x 10 = 6.21 -> composite = **96.21**
- V-02 (Round 11, stage sub-specs): C-35 FAIL, C-36 FAIL, C-37 FAIL
  -> 18/29 x 10 = 6.21 -> composite = **96.21**
- V-04 (Round 11, D-first + sub-specs): C-35 FAIL, C-36 FAIL, C-37 FAIL
  -> 18/29 x 10 = 6.21 -> composite = **96.21**
- V-03 (Round 11, inertia-first): C-35 PASS, C-36 PASS, C-37 PASS
  -> 21/29 x 10 = 7.24 -> composite = 60 + 30 + 7.24 = **97.24** (new ceiling)
- V-05 (Round 11, all three axes): C-35 PASS, C-36 PASS, C-37 PASS
  -> 21/29 x 10 = 7.24 -> composite = **97.24** (ties V-03)
- Open for R12: none — all three new criteria cracked by R11 V-03 and V-05.
  Persistent uncracked block: C-09 through C-16 (8 criteria, unaddressed across all rounds).
