Written to `simulations/quest/rubrics/flow-resilience-rubric-v14-2026-03-14.md`.

---

**v14 summary — what changed:**

| | v13 | v14 |
|---|---|---|
| Denominator | 32 | **35** |
| New criteria | C-39, C-40 | **C-41, C-42, C-43** |
| R13 ceiling | 100.00 (32/32) | **99.14 (32/35)** |
| R14 ceiling | 100.00 (32/32) | **open — three-axis coverage determines score** |

**Three new criteria extracted from R14 structural axes:**

- **C-41 — Named Sub-Part Labeling Within Pre-Table Inertia Assessment** *(E-33)* — From the Three-Act Memo axis. The Inertia Assessment (C-35) must have three *named* sub-parts (framing / carrying cost / tipping point) labeled as 1a/1b/1c or Act I/II/III. Row descriptors must cross-reference by sub-part label ("Step 1b carrying cost", "Act II carrying cost"), not just by section name. Unlabeled prose that satisfies C-35/C-36 content-wise but lacks structural division fails. Depends on C-35 + C-36.

- **C-42 — Pre-Table SLA Budget Pre-Commitment** *(E-34)* — From the SLA Budget axis. Mirrors C-35 for SLA targets: a named pre-table section pre-commits TTD/TTC/TTR/TTV values per failure class; the Column Contract names that section as the reference source; at least one row descriptor names the SLA Budget as the constraint source. Satisfying C-30 (SLA-annotated stages) without the pre-committed reference source fails. Depends on C-30 + C-35.

- **C-43 — Failure Signature Column Specification** *(E-35)* — From the Failure Signature axis. The Column Contract includes a Failure Signature column describing the *behavioral fingerprint during the failure* — distinct from Trigger Condition (entry threshold) and State (pre-failure config). Requires at least two actor viewpoints per row (client/server, node-A/node-B, etc.). Generic "system unavailable" fills without actor differentiation fail. Depends on C-24 + C-33.

The R14 ceiling under v14 is open: all five variations pass 32/35; the maximum 100.00 is achievable by any variation implementing all three axes.
lumn Contract includes
a Failure Signature column specifying the observable behavioral fingerprint of the
failure in progress -- distinct from Trigger Condition (C-33, which bounds entry
thresholds) and from State (which describes pre-failure configuration). The Failure
Signature describes what the failure looks like to each system actor while it is
occurring, with at least two distinct actor viewpoints named per row (e.g., client view /
server view, or node-A view / node-B view). Extracted from the Failure Signature axis
in R14.

The R13 ceiling re-scores from 100.00 (32/32) to **99.14 (32/35)** -- those variations
did not implement the three new axes. The R14 ceiling under v14 is open pending
per-variation axis-coverage scoring; maximum achievable is 100.00 (35/35) for a
variation implementing all three axes.

---

## Essential Criteria (guarantee basic output quality -- 60% of score)

### C-01 -- Three Distinct Failure Classes
- **Weight**: essential
- **Category**: coverage
- **Text**: The output covers three structurally distinct failure classes: (1) client-side
  connectivity loss -- the client cannot reach the server due to offline state, partial
  connectivity, or intermittent network failure; (2) data consistency violation -- the
  system processes transactions that produce inconsistent state across nodes, including
  split-write, oversell, double-charge, or phantom inventory outcomes; (3) split-brain /
  eventual-consistency conflict -- two or more nodes independently process conflicting
  state updates that must later be reconciled (e.g., concurrent checkout on separate
  nodes, dual-write with diverging inventory counts, split-brain / eventual-consistency
  conflict).
- **Pass condition**: All three classes are represented by distinct named scenarios. A
  single scenario that attempts to cover all three classes fails. Scenarios that collapse
  class 2 and class 3 into a single "network issue" fail.

### C-02 -- Four-Field Structure Per Scenario
- **Weight**: essential
- **Category**: structure
- **Text**: Every failure scenario includes all four required fields: (1) state -- what the
  system state is when failure occurs; (2) capability -- what the user can still do; (3)
  data at risk -- what data may be lost, stale, or inconsistent; (4) recovery path -- how
  the system returns to a healthy state.
- **Pass condition**: Every scenario present in the output includes all four fields with
  non-trivial content (not placeholder or "N/A"). A scenario missing any field fails this
  criterion.

### C-03 -- Gap Identification
- **Weight**: essential
- **Category**: correctness
- **Text**: The output identifies at least one offline experience gap, at least one data
  consistency violation, and at least one missing recovery flow as distinct findings.
- **Pass condition**: All three finding types appear, each labeled and actionable (not just
  implied). Generic statements like "offline support may be limited" without specificity
  fail.

### C-04 -- Distributed Systems Accuracy
- **Weight**: essential
- **Category**: correctness
- **Text**: Technical claims about failure modes are consistent with distributed systems
  fundamentals: CAP theorem trade-offs, retry semantics, idempotency requirements, and
  conflict-resolution strategies are used correctly where referenced.
- **Pass condition**: No materially incorrect distributed-systems claim is present.
  Fabricated error codes, invented protocols, or impossible consistency guarantees fail
  this criterion.

### C-05 -- Commerce Domain Grounding
- **Weight**: essential
- **Category**: depth
- **Text**: The analysis is grounded in the commerce / distributed systems domain. Failure
  scenarios reference realistic commerce flows (e.g., checkout, inventory reservation,
  payment processing, order fulfillment) rather than generic CRUD operations.
- **Pass condition**: At least two scenarios are anchored to a recognizable commerce
  operation. Purely abstract or domain-agnostic scenarios fail.

---

## Recommended Criteria (improve output quality -- 30% of score)

### C-06 -- Severity and Blast Radius Classification
- **Weight**: recommended
- **Category**: depth
- **Text**: Each failure scenario is annotated with a severity level (e.g., degraded /
  impaired / down) and a blast radius (what percentage or which segment of users is
  affected). This helps triage prioritization.
- **Pass condition**: At least half of the scenarios carry both a severity label and a
  blast-radius estimate or qualifier (e.g., "affects all users in offline mode", "affects
  <1% under split-brain").

---

## Aspirational Criteria (ceiling-raising -- 10% of score)

### C-09 -- Per-Scenario Chaos Test Block *(E-22)*
The prompt specifies a Chaos Test Block for each scenario row, requiring four named
components: (1) *Inject* -- a named, reproducible failure condition that activates the
scenario; (2) *Expected Behavior* -- the system response that should occur when the
failure is injected; (3) *Pass Signal* -- the observable artifact confirming the expected
behavior occurred; (4) *Fail Signal* -- the observable artifact confirming the expected
behavior did not occur. The specification appears in a Chaos Test Block Specification
meta-table or equivalent structural definition, making omission of any component a
visible contract violation rather than a content gap. Each scenario row descriptor
includes a chaos block fill template co-located with the row.

**Pass condition**: A Chaos Test Block Specification defines all four components
(Inject / Expected Behavior / Pass Signal / Fail Signal) with non-generic fill
requirements specifying named, reproducible conditions. Each row descriptor references
or includes a chaos block fill template. The specification must be a structural
meta-table or equivalent -- a prose description of chaos testing intent does not satisfy
this criterion.

### C-10 -- Per-Finding Observability Hooks *(E-23)*
Each Gap Register finding includes three inline observability fields co-located at
finding granularity: (1) *Metric* -- the named system or business metric to monitor for
this finding; (2) *Alert* -- the named alert condition that fires when the metric
threshold is crossed; (3) *Owner* -- the responsible role or team. The Gap Register
format specification requires all three fields per finding with non-generic fill
requirements (a named metric, a specific alert condition, a responsible role rather than
"TBD"). A Gap Register format that lists finding content without per-finding
observability fields does not satisfy this criterion.

**Pass condition**: The Gap Register format specification requires all three observability
fields (Metric / Alert / Owner) inline with each finding. Fill requirements for each
field must specify non-generic content. A finding without all three inline fields fails
the format requirement. C-03 must also pass -- C-10 cannot pass if C-03 fails.

### C-11 -- Actor-Chain Notation on Recovery Mechanisms *(E-24)*
The Recovery Path column specification requires each stage mechanism to begin with a
labeled actor-chain prefix -- `client ->`, `server ->`, `operator ->`, or `user ->` --
identifying which system actor owns the transition. At least three of the four lifecycle
stages (Detect, Contain, Recover, Validate) in every scenario row must carry a labeled
actor prefix. This applies the column-level ownership principle (C-20) below the column
to the mechanism sub-field: ownership is assigned at actor granularity rather than at
column or role granularity alone. A mechanism described in prose without a labeled actor
prefix ("the system retries", "circuit breaker opens") does not satisfy the actor-chain
requirement.

**Pass condition**: The Recovery Path column specification or equivalent structural
definition explicitly requires actor-chain prefix notation on stage mechanisms, names
the accepted prefix forms (at minimum: `client ->`, `server ->`, `operator ->`,
`user ->`), and specifies a minimum threshold (at least three of four stages per row
must carry a labeled prefix). At least one row descriptor demonstrates the pattern with
example prefixes. C-20 must also pass -- C-11 cannot pass if C-20 fails.

### C-12 -- Constrained Conflict Resolution Vocabulary *(E-25)*
The Column Contract or equivalent specification constrains all references to conflict
resolution strategies to a canonical vocabulary set: `last-write-wins`, `merge`,
`manual-reconcile`, and `reject-stale`. Free-text paraphrases -- "the most recent write
wins", "reconcile manually", "discard the stale entry" -- are explicitly negated as
insufficient; the canonical term must appear as a discrete label. This transforms the
conflict strategy field from a prose-fill slot into a template-fill slot: a model cannot
satisfy the requirement by describing the concept without using the canonical term. The
constraint applies to both row descriptor fills and to adequacy judgments within the
scenario.

**Pass condition**: A vocabulary constraint block (in the Column Contract, a blockquote,
or an equivalent dedicated structure) names the canonical conflict vocabulary terms,
states that free-text descriptions do not satisfy the constraint, and requires the
canonical term as a discrete label. At least one row descriptor applies the constraint
with an example canonical label and an adequacy judgment that references the constraint.
C-24 must also pass -- C-12 cannot pass if C-24 fails.

### C-13 -- Gap-Merge Prevention via Self-Verifying Count *(E-26)*
The Gap Register format includes a structural mechanism that prevents merger or counting
collapse of the three required finding types. The mechanism must include a count field --
"Finding types present: ___ of 3" or equivalent -- that would register as incomplete if
any two finding types were merged into one. The count field must appear as required
output content that the model fills in, not as a reader audit note: a correct count
("3 of 3") requires all three finding types to genuinely be present, and an omission
or merge produces "2 of 3", making the artifact visibly incomplete without reader audit.
A Gap Register format that requires three findings without a self-verifying count
mechanism does not satisfy this criterion.

**Pass condition**: The Gap Register output format specifies a count field ("Finding
types present: ___ of 3" or equivalent) as model-generated output content, covering all
three required finding types. The format requirement states that a finding missing
required fields fails the format requirement, creating dual verification (count integrity
+ per-finding field completeness). A completeness checklist present only in prompt
instructions rather than as required output content with a model-filled count field does
not satisfy this criterion.

### C-14 -- Chaos Blocks Co-Located at Row Granularity *(E-27)*
Each scenario row's Chaos Test Block is co-located immediately after its row descriptor
in the output -- not consolidated into a standalone chaos section elsewhere. The prompt
includes an anti-boundary instruction that negates at least two chaos consolidation
escape forms: "not a separate chaos section" and "not a standalone chaos-engineering
table" (or equivalent). The Section Order Requirement specifies that each scenario row
must be followed by its Chaos Test Block before the next row begins -- making the
co-location requirement a sequencing gate, not merely a stylistic preference. A prompt
that specifies chaos blocks without explicit co-location instructions leaves the model
free to consolidate them under token pressure.

**Pass condition**: An anti-boundary instruction negates at least two chaos consolidation
forms (separate section AND standalone table, or equivalent distinct artifacts). A
Section Order Requirement positions the chaos block immediately after each row, before
the next row begins. C-09 must also pass -- C-14 cannot pass if C-09 fails.

### C-15 -- Per-Finding Observability Hook as Inline Co-Location *(E-28)*
Observability hooks (Metric / Alert / Owner from C-10) appear inline with each Gap
Register finding -- not consolidated into a separate observability section. The prompt
includes an explicit anti-boundary instruction negating "a separate observability
section" or "a standalone observability table" at finding granularity. This applies
the same co-location principle as C-14 (chaos blocks co-located per row) to Gap
Register findings: attaching required metadata adjacent to its target finding prevents
deferral to a consolidation section where token pressure causes omission or format
collapse.

**Pass condition**: An anti-boundary instruction negates at least one observability
consolidation form ("not a separate observability section" or equivalent). The Gap
Register format specification positions observability fields inline with each finding --
not after all findings in a trailing section. C-10 must also pass -- C-15 cannot pass if
C-10 fails.

### C-16 -- Self-Verification Completeness Checklist as Output Content *(E-29)*
The output includes a Finding Completeness Checklist as an explicit required output
section -- not a reader audit tool but a model-generated verification artifact. The
checklist uses a count-gate format: one `[ ]` checkbox per finding type plus a
"Finding types present: ___ of 3" count field that the model must fill in with an
accurate count. Making the model write the count forces explicit self-verification:
a correct count ("3 of 3") is only accurate if all three finding types are genuinely
present; an omission or merge produces "2 of 3" or fewer, making the artifact visibly
incomplete without requiring reader audit. A completeness checklist present only in
the prompt instructions for reader use -- rather than as a required output section with
a model-filled count -- does not satisfy this criterion.

**Pass condition**: The prompt's output specification requires a Finding Completeness
Checklist section with one checkbox per finding type and a count field ("Finding types
present: ___ of 3" or equivalent) as model-generated output content. The count field
must be positioned after the Gap Register findings to function as post-hoc
self-verification. C-13 must also pass -- C-16 cannot pass if C-13 fails.

### C-17 -- Unified Table Index
The prompt includes a `#` column (or equivalent row identifier) in the scenario table
and contains an explicit instruction prohibiting the model from splitting the table
across scenario classes, role sections, or any other structural boundary.

**Pass condition**: A row-index column is present AND the prompt contains an explicit
anti-split instruction referencing the unified table. A `#` column without an anti-split
instruction scores PARTIAL, not PASS.

### C-18 -- Section-Level Phase Gate
The prompt contains an explicit instruction requiring the model to complete all scenario
table rows before advancing to subsequent output sections (e.g., Gap Register, Findings,
Recommendations). The gate instruction names the boundary condition by section name.

**Pass condition**: An explicit gate instruction of the form "Produce all N rows before
writing [section name]" (or equivalent) appears in the prompt. An implicit sequencing
expectation (e.g., table appearing before gap register in an example output) does not
satisfy this criterion.

### C-19 -- Slot-Level In-Row Imperatives
Bold imperative text is embedded inside the Content field descriptor of at least two
scenario table rows, co-located at cell granularity rather than in preamble, blockquotes,
or section headers. The pattern is: **"Write this row now."** followed by the fill
requirement, followed by **"Do not advance to row N until [condition]."**

**Pass condition**: At least two Content field descriptors contain embedded bold
imperative text matching the "Write this row now / Do not advance" pattern inside the
cell content itself. Instructions appearing above the table, in a blockquote before the
first row, or in a checklist after the table do not satisfy this criterion. A prose
section adjacent to the output table (not inside a per-row field table schema) also does
not satisfy this criterion.

### C-20 -- Column-Level Ownership Assignment
The prompt assigns an explicit owner (e.g., role name, expert label) to each column in
the scenario table, either via inline column-header labels or via a structural ownership
specification.

**Pass condition**: Every column in the scenario table has a named owner. Ownership
implied by section headers (e.g., a "Commerce Expert" heading above a sub-table) does
not satisfy this criterion -- ownership must be assigned per column.

### C-21 -- Layered Granularity Architecture *(E-5)*
The prompt explicitly architects its four anti-omission mechanisms as a coordinated
four-level stack: one mechanism per structural level (table-level unified index -> C-17,
section-level phase gates -> C-18, slot-level in-row imperatives -> C-19, column-level
ownership -> C-20). Each mechanism targets a distinct omission risk at a distinct
structural level, so no two mechanisms conflict with or duplicate each other.

**Pass condition**: The prompt explicitly names all four structural levels (table,
section, slot, column) and assigns a distinct anti-omission mechanism to each. Implicit
satisfaction -- a prompt that happens to use all four mechanisms without naming the
four-level architecture -- fails. An output that names only two or three levels without
the fourth also fails.

### C-22 -- Anti-Boundary Instruction by Structural Symptom *(E-6)*
The anti-boundary instruction names the failure mode by its structural symptom in output
-- what the artifact would look like if the model misread the ownership transition as a
section cue -- rather than by the intent violation alone. It says "not a sub-table
boundary, not a role-sequence trigger" rather than only "keep all rows in a single
table." Symptom-naming prevents the model from satisfying the letter of the instruction
while still producing a structural boundary under a different label.

**Pass condition**: The anti-boundary instruction includes at least two symptom-level
negations that name specific structural artifacts to avoid (e.g., "not a sub-table
boundary", "not a role-sequence trigger", "not a horizontal rule between ownership
blocks"). An instruction that states only a positive ("keep rows together", "use one
table") without negating at least two symptom forms fails -- even if the unified row
index (C-17) passes.

### C-23 -- In-Row Bold Imperative as Genuine Slot-Level Co-location *(E-7)*
Bold imperative text embedded inside the Content field descriptor of a scenario table
row -- phrased as **"Write this row now."** followed by the fill requirement, followed
by **"Do not advance to row N until [condition]."** -- is genuine slot-level co-location.
The model reads this text exactly when constructing that cell, operating below section
gates (which the model passes before entering table construction) and below table-level
blockquotes or preamble (which appear before the first row). This makes it structurally
impossible to satisfy section-level or preamble-level instructions and then omit the row.

**Pass condition**: At least two Content field descriptors in the scenario table contain
bold imperative text matching the pattern "Write this row now" / "Do not advance to row N
until [condition]" embedded inside the cell content itself. A blockquote appearing above
the table, a section header before the row, or a checklist after the table does not
satisfy this criterion -- the imperative must be co-located inside the Content descriptor
at cell granularity.

### C-24 -- Column-Ownership Meta-Table as Pre-Output Specification *(E-8)*
The prompt includes a separate meta-table (columns: Name / Owner / Fill Requirement)
placed before the output table itself. This creates structural pre-commitment: the model
processes per-column responsibility before constructing any row, making column omission
detectable as a contract violation rather than an oversight. A parenthetical label in a
column header, a role-section heading above the table, or inline ownership notes inside
a row descriptor do not satisfy this criterion -- the meta-table must be a standalone
structure positioned before the first output row.

**Pass condition**: A discrete meta-table with at least Name, Owner, and Fill Requirement
columns (or equivalent fields) appears in the prompt before the scenario output table.
The meta-table must cover every column in the output table. If any output column lacks a
corresponding meta-table entry, the criterion fails.

### C-25 -- Two-Symptom Anti-Boundary Negation Pattern *(E-9)*
The anti-boundary instruction names two distinct structural artifacts that must not
appear. The pairing is load-bearing: the first negation addresses table splitting (e.g.,
"Do not create separate tables for Commerce Expert columns and Distributed Systems Expert
columns"), and the second addresses invisible boundary insertion (e.g., "Do not insert
a horizontal rule, heading, or section break between rows when column ownership shifts").
A model that satisfies negation-1 by consolidating tables could still insert a `---`
separator; negation-2 closes that escape route. Single-symptom instructions leave at
least one structural escape route open.

**Pass condition**: The anti-boundary instruction names at least two distinct structural
artifacts to avoid -- one artifact addressing table-level splitting and one addressing
intra-table boundary insertion (horizontal rule, heading, section break, or equivalent).
Both negations must be present. A prompt that satisfies C-22 (two symptom-level
negations) but targets the same class of artifact (e.g., two sub-table variants) does
not satisfy C-25 -- the two negations must address different boundary mechanisms.

### C-26 -- Architecture-to-Contract Forward Reference *(E-10)*
The four-level anti-omission architecture table (C-21) contains a Mechanism column entry
that names a downstream artifact by its exact section title -- for example, "defined in
the Column Contract (below)" or "see Row Descriptors section below." This creates a
closed-loop verifiable chain: the architecture announces its own artifacts by name before
those artifacts appear, so a reader can confirm each promised artifact exists and a model
cannot omit the named artifact without visibly breaking the chain. An architecture table
that describes what a mechanism *does* without naming the downstream artifact by section
title does not satisfy this criterion -- the forward reference must be by name, not by
function.

**Pass condition**: At least one row in the architecture table (C-21) has a Mechanism
column entry that names a downstream section, table, or structural artifact by its exact
title as it appears elsewhere in the prompt. The named artifact must actually exist in
the prompt. A description of mechanism function without a title-level pointer fails.
C-21 must also pass -- C-26 cannot pass if C-21 fails.

### C-27 -- Consequence-Enumeration in Slot-Level Descriptors *(E-11)*
A slot-level row descriptor (C-23) names the specific business consequences of each
possible resolution outcome *before* the fill requirement -- for example, "oversell if
resolution A wins, double-charge if resolution B wins, duplicate fulfillment if merge is
naive." This elevates the fill requirement from a content specification to an outcome
specification: a vague fill becomes visibly inadequate against named stakes. A descriptor
that specifies what content to write without enumerating per-outcome consequences does
not satisfy this criterion.

**Pass condition**: At least one row descriptor contains consequence-enumeration of the
form "X consequence if outcome A, Y consequence if outcome B" (or equivalent) positioned
before the fill instruction for that row. The consequences must be business-level (not
purely technical) and must be distinct per outcome. A descriptor that names a single
consequence without branching across outcomes does not satisfy this criterion. C-23 must
also pass -- C-27 cannot pass if C-23 fails.

### C-28 -- Sub-Field Completeness Gate in Slot-Level Imperative *(E-12)*
A slot-level advance-inhibitor condition (C-19) names specific sub-fields or sub-stages
within a column's fill requirement as non-bypass components -- for example, "Do not
advance to row N until this row contains non-placeholder content in every column
**including all four Recovery Path stages**." This moves the gate below column
granularity: the condition is not satisfied by filling the cell with any non-placeholder
content, but only by filling all named sub-components within the cell. A partial fill of
a structured column (e.g., writing only two of four required lifecycle stages) becomes
visibly inadequate against a named-stage gate in a way it would not against a generic
"non-placeholder" gate.

**Pass condition**: At least one slot-level advance-inhibitor condition (C-19) names a
specific sub-field, sub-stage, or sub-component from the column's fill specification --
e.g., a named lifecycle stage, a named field within a structured cell, or an enumerated
requirement list -- as part of the non-bypass condition. The named sub-field must exist
as a defined sub-structure in the Column Contract or an equivalent column specification.
A gate that reads only "non-placeholder content" without naming any sub-structure does
not satisfy this criterion. C-19 must also pass -- C-28 cannot pass if C-19 fails.

### C-29 -- Chronic Consequence Enumeration *(E-13)*
At least one scenario row names the accumulating business consequence of *not* addressing
the resilience gap -- the carrying cost of inaction -- distinct from the per-resolution-
branch acute consequences required by C-27. The chronic enumeration takes the form "if
this gap is never addressed, [ongoing consequence]" -- for example, "oversell rate
accumulates per-deploy", "payment reconciliation backlog grows unbounded", "duplicate
fulfillment charges compound indefinitely." This creates a two-horizon outcome
specification within the row: C-27 names what goes wrong during the incident (acute,
per-resolution-branch), and C-29 names what continues to accumulate if the scenario is
never resolved (chronic, carrying-cost).

**Pass condition**: At least one scenario row contains a chronic-consequence statement
that: (1) is business-level (not purely technical), (2) is framed as a persistent or
accumulating effect of inaction rather than an incident-moment outcome, and (3) is
distinct from the per-resolution-branch acute consequences in C-27. A statement that
names a consequence only at incident time (even if phrased as "will result in") without
framing the accumulating or indefinite character of the harm does not satisfy this
criterion. C-27 must also pass -- C-29 cannot pass if C-27 fails.

### C-30 -- SLA-Annotated Recovery Path Stages *(E-14)*
Each of the four Recovery Path lifecycle stages (Detect, Contain, Recover, Validate) is
paired with a named SLA target type in the column specification or row descriptor --
specifically Detect/TTD (Time to Detect), Contain/TTC (Time to Contain), Recover/TTR
(Time to Recover), Validate/TTV (Time to Validate), or equivalent named measurable
commitments. This transforms the Recovery Path from a qualitative sequence into a
testable commitment specification: a fill that names stage actions without corresponding
SLA targets is incomplete against this standard in a way it would not be against a
stage-name-only gate.

**Pass condition**: At least one Recovery Path column specification or row descriptor
pairs each of the four named lifecycle stages with a corresponding named SLA target
type. The pairing must appear in a column specification, column contract entry, or row
descriptor -- not only in an example output row. The four pairings must be complete: a
specification that pairs two stages with SLA targets but leaves the other two unnamed
fails. C-28 must also pass -- C-30 cannot pass if C-28 fails.

### C-31 -- Three-Component Chronic Accumulation Framing *(E-15)*
At least one chronic-consequence specification (C-29) structures the accumulating harm
as three named components: (1) a *rate component* -- a qualifier naming the accumulation
interval or trigger (e.g., "per-deploy", "per-transaction", "per-incident"); (2) a
*horizon component* -- a qualifier naming the trajectory without intervention (e.g.,
"indefinitely", "without ceiling", "unbounded", "compound growth"); and (3) a *metric
component* -- a named business metric that accumulates (e.g., oversell count,
reconciliation backlog items, duplicate charge events). This tightens C-29's chronic
framing from a binary "inaction has consequences" assertion to a quantified accumulation
model.

**Pass condition**: At least one chronic-consequence statement contains all three
components -- rate qualifier, horizon qualifier, and named business metric -- present in
the same statement or in immediately adjacent cells in the same row. The rate and
horizon qualifiers must be distinct: a statement of the form "X accumulates" without
naming an accumulation interval (rate) or a trajectory bound (horizon) fails even if
X is a named metric. C-29 must also pass -- C-31 cannot pass if C-29 fails.

### C-32 -- Intra-Row Column-Group Gate (5-Level Architecture) *(E-16)*
The prompt extends the four-level anti-omission architecture (C-21) to five levels by
adding an intra-slot column-group sequencing gate: within a single scenario row, columns
assigned to one owner phase (e.g., C-phase: Commerce Expert columns) must be complete
before columns assigned to the next owner phase (e.g., D-phase: Distributed Systems
Expert columns) are begun. This gate operates at a level below the slot (row) and above
the individual column -- targeting the risk that an ownership transition mid-row is
misread as a section boundary. The five-level naming is load-bearing: a prompt that uses
the gate without naming all five levels cannot demonstrate that the mechanism targets a
distinct structural level rather than restating column-level ownership (C-20).

**Pass condition**: The prompt explicitly names all five structural levels (table,
section, slot, column-group, column) and assigns a distinct advance-inhibitor to the
column-group level -- specifying that one ownership phase's columns must be complete
before the next phase begins within the same row. The gate must be positioned inside the
row descriptor (at slot level or below), not in preamble or a section-level note. C-21
must also pass -- C-32 cannot pass if C-21 fails.

### C-33 -- Trigger Condition Column Specification *(E-17)*
The prompt specifies a Trigger Condition column (or equivalently named entry-bounding
column) that pairs each scenario with both a threshold expression and a detection signal.
The threshold expression is a quantified condition that activates the scenario (e.g.,
"inventory count drops below safety-stock threshold", "payment API latency exceeds
500ms p99"). The detection signal is the observable mechanism by which the system
identifies the threshold being crossed (e.g., "inventory-service health probe returns
degraded", "payment-provider timeout counter increments"). This transforms each scenario
from a reactive failure description into a bounded detection specification.

**Pass condition**: A Trigger Condition column (or equivalent) appears in the Column
Contract meta-table (C-24) with a Fill Requirement specifying both a threshold expression
and a detection signal as distinct components. At least one row descriptor fills both
components with non-generic content. A trigger description that is qualitative only
("when the service is unavailable") without a threshold expression fails. C-24 must also
pass -- C-33 cannot pass if C-24 fails.

### C-34 -- Verification Signal per Recovery Stage *(E-18)*
Each of the four Recovery Path lifecycle stages (Detect, Contain, Recover, Validate)
carries three components in the column specification or row descriptor: (1) *mechanism*
-- the action taken to advance the stage; (2) *SLA target* -- the named time commitment
(TTD/TTC/TTR/TTV from C-30); and (3) *Verification Signal (VS)* -- a named observable
artifact that confirms the stage is complete (e.g., "inventory-service heartbeat returns
200", "payment provider ACK logged to audit trail", "dual-write conflict counter resets
to 0 for 60s"). The VS makes the recovery specification falsifiable per stage: a stage
is not complete until the named observable artifact appears, independent of elapsed time
alone.

**Pass condition**: The Recovery Path column specification or at least one row descriptor
requires all three components -- mechanism, SLA target, and named Verification Signal --
for each of the four lifecycle stages. The VS must be named (not described generically
as "confirmation" or "verified") in the column specification or a row descriptor. The VS
must be observable (a system state, log entry, metric value, or API response code) and
must be distinct from a re-statement of the mechanism. C-30 must also pass -- C-34 cannot
pass if C-30 fails.

### C-35 -- Pre-Table Inertia Assessment with Per-Class Carrying Cost Pre-Commitment *(E-19)*
The prompt includes a named section (e.g., "Step 1: Inertia Assessment") positioned
before the scenario table that establishes per-class carrying costs for each of the
three failure classes. The Column Contract specifies that the Status Quo Risk column
must be filled consistently with the carrying costs pre-committed in this section (not
authored independently per row). At least one row descriptor reinforces the constraint
by naming the pre-table section as the reference source for that row's Status Quo Risk
fill -- e.g., "Status Quo Risk must use the metric established for Class N in the
Inertia Assessment." A prompt where Status Quo Risk is independently authored per row
without a pre-committed reference -- even if the column passes C-29 and C-31 -- does not
satisfy this criterion.

**Pass condition**: A named pre-table section explicitly establishes per-class carrying
costs for all three scenario classes. The Column Contract entry for Status Quo Risk
names the pre-table section as the reference source for the fill (not a fill requirement
standing alone). At least one row descriptor names the pre-table section as the
constraint source for that row's Status Quo Risk fill. C-31 must also pass -- C-35
cannot pass if C-31 fails.

### C-36 -- Per-Class Inertia Tipping Point Signal *(E-20)*
The pre-table Inertia Assessment (C-35) includes a sub-section requiring, for each of
the three failure classes, a named observable threshold expression at which the carrying
cost has crossed a point where deferral becomes indefensible -- paired with a named
metric being monitored (e.g., "oversell-event count exceeds 50 per month",
"cart-abandonment rate rises more than 2% above baseline"). This applies the C-33
threshold+detection-signal standard to the inertia assessment: just as C-33 makes each
failure scenario falsifiable by entry condition, C-36 makes each inertia claim
falsifiable by exit condition.

**Pass condition**: The pre-table Inertia Assessment contains a sub-section requiring
one observable signal per failure class, each signal specifying both a threshold
expression (quantified condition) and a named metric being monitored. The threshold
expression must be quantified -- "oversell-event count exceeds 50/month" satisfies;
"worsens over time" does not. All three failure classes must be covered. C-35 must also
pass -- C-36 cannot pass if C-35 fails.

### C-37 -- Inertia Verdict Post-Gap Register *(E-21)*
A section positioned after the Gap Register synthesizes the gap findings and the
pre-committed carrying costs from the Inertia Assessment (C-35) into a single verdict:
a HIGH/MEDIUM/LOW inertia threat level with the single strongest argument against
deferral (2-3 sentences). This creates a second section-level phase gate and closes the
inertia specification loop across three structural positions: (1) pre-table Inertia
Assessment establishes the carrying cost framing, (2) per-row Status Quo Risk fills from
the pre-committed costs, (3) the post-gap Inertia Verdict synthesizes gaps and costs
into an actionable threat assessment. A prompt that includes an inertia section before
the table without requiring a corresponding post-gap synthesis closes only two of the
three positions and does not satisfy this criterion.

**Pass condition**: A section appearing after the Gap Register requires a named Inertia
Verdict specifying a threat level (HIGH/MEDIUM/LOW or equivalent ordinal scale) and a
single strongest argument against deferral. The verdict section must name both the gap
findings and the pre-committed carrying costs as inputs to the judgment. The verdict must
be structurally dependent on Gap Register completion -- positioned after the three gap
findings or gated by an explicit instruction naming the Gap Register as a prerequisite.
C-35 must also pass -- C-37 cannot pass if C-35 fails.

### C-38 -- Anti-Boundary Umbrella Instruction (Four-Escape Negation) *(E-30)*
A single anti-boundary instruction or contiguous block names four distinct structural
escape forms simultaneously: (1) *table-split escape* -- separate tables per column
owner group (the escape negated by C-25 negation-1); (2) *intra-table boundary escape*
-- horizontal rule, heading, or section break between rows (the escape negated by C-25
negation-2); (3) *chaos consolidation escape* -- standalone chaos section or standalone
chaos-engineering table (the co-location escape route for Axis D content); (4)
*observability consolidation escape* -- standalone observability section or standalone
observability table (the co-location escape route for Axis E content). The four
negations must appear in a single instruction or contiguous block -- not distributed
across separate axis-specific notes -- so a model reading any one instruction sees all
four closed escape routes simultaneously. This extends C-25 (two-symptom negation) from
two escape forms to four, closing all structural consolidation escape routes identified
across Axes D and E without requiring separate per-axis anti-boundary clauses.

**Pass condition**: A single instruction or contiguous block negates all four escape
forms: (1) table split by column owner, (2) intra-table boundary insertion, (3)
standalone section for row-appended content (chaos blocks), and (4) standalone section
for finding-appended content (observability hooks). All four must appear in the same
instruction or immediately adjacent sentences -- an anti-boundary instruction that covers
escapes 1-2 in one section and escapes 3-4 in a separate per-axis note does not satisfy
this criterion. C-25 must also pass -- C-38 cannot pass if C-25 fails. C-14 and C-15
must also pass -- the umbrella cannot close chaos and observability escape routes if
those co-location requirements are not themselves established.

### C-39 -- Present-Tense Write Imperative in Slot-Level Directive *(E-31)*
The slot-level write directive (the first half of the C-19 two-part pattern) uses a
present-tense action verb -- "**Write this row now.**" -- rather than a locational or
task-initiation marker -- "Begin Row N here.", "Fill in Row N.", "Start Row N content."
The linguistic distinction is structural, not stylistic: "Write" is a performative
directing the model to produce output immediately; "Begin" or "Fill in" are task-boundary
markers that orient the model to a position or mode without specifying the output action.
A location marker can be satisfied by acknowledging the row's position without producing
its content; a performative action verb cannot. Under the full two-part pattern required
by C-19 ("Write this row now" + "Do not advance to row N until [condition]"), substituting
a location marker in the first half degrades the imperative from a production command to
a position label, reducing the constraint's force from content-gating to navigational.

**Pass condition**: At least two Content field descriptors contain a slot-level write
directive using a present-tense action verb ("Write", "Output", "Produce", or equivalent
performative) in bold, co-located at cell granularity. A bold locational marker ("Begin
Row N here"), a task-initiation form ("Fill in Row N"), or a preparatory frame ("Row N
content follows") does not satisfy this criterion even if bold and even if the second
half of the C-19 pattern (advance-inhibitor) is correctly formed. C-19 must also pass --
C-39 cannot pass if C-19 fails.

### C-40 -- Section Order Requirement Covers Row-Appended Content *(E-32)*
The Section Order Requirement (C-18) extends beyond section-level gating (all scenario
rows before Gap Register) to explicitly include each row's co-located chaos block as a
sequencing dependency at row granularity. The extended requirement specifies that row
N's scenario columns AND row N's chaos block must both be complete before row N+1
begins -- creating a two-stage completion gate per row: (1) complete the row's column
content; (2) complete the row's chaos block; then advance to the next row. This closes
the consolidation escape where a model produces all three scenario rows contiguously and
then writes chaos blocks as a trailing batch despite the C-14 co-location requirement:
by naming chaos blocks in the Section Order Requirement, chaos block deferral becomes a
sequencing violation rather than merely a co-location preference. A Section Order
Requirement that gates only the section-level transition (all rows before Gap Register)
without naming row-level chaos block completion as an advance condition does not satisfy
this criterion.

**Pass condition**: The Section Order Requirement explicitly names row-appended structural
content (chaos test block, chaos block, or equivalent co-appended content) as part of
the row-level advance condition, specifying that each row's chaos block must be complete
before the next row begins. Naming the chaos block by its structural label is required --
a generic "complete each row fully before advancing" without naming co-appended content
does not satisfy this criterion. C-18 must also pass -- C-40 cannot pass if C-18 fails.
C-09 and C-14 must also pass -- C-40 cannot close a chaos-deferral escape that is not
established by the chaos co-location requirement.

### C-41 -- Named Sub-Part Labeling Within Pre-Table Inertia Assessment *(E-33)*
The pre-table Inertia Assessment (C-35) is internally divided into three named sub-parts
with distinct labels corresponding to distinct functional roles: (a) a framing sub-part
that establishes why the domain is inherently fragile (context for all three failure
classes); (b) a carrying-cost sub-part that enumerates per-class carrying costs (the
source values referenced by C-35 row fills); (c) a tipping-point sub-part that specifies
the per-class exit signal (the source values referenced by C-36 fills). Sub-parts are
named by alphanumeric code (1a / 1b / 1c), act-label (Act I / Act II / Act III), or
equivalent discrete labels. Row descriptors that reference the inertia assessment by
sub-part label -- e.g., "Status Quo Risk = Class 1 Step 1b carrying cost" or "Class 1
Act II carrying cost" -- rather than by section name alone create falsifiable
cross-references: a fill that draws from the wrong sub-part produces a visible
inconsistency against the sub-part label. A pre-table section that satisfies C-35 and
C-36 but uses unlabeled prose or undifferentiated sub-sections without named functional
roles does not satisfy this criterion even if carrying costs and tipping points are both
present.

**Pass condition**: The pre-table Inertia Assessment contains three named sub-parts with
distinct labels (alphanumeric, act-label, or equivalent) covering framing, carrying cost,
and tipping point as separately labeled divisions. At least one row descriptor references
the inertia assessment section by sub-part label rather than by section name alone -- the
cross-reference must be to the sub-part (e.g., "Step 1b" or "Act II"), not merely to
"the Inertia Assessment." C-35 must also pass -- C-41 cannot pass if C-35 fails. C-36
must also pass -- C-41 cannot pass if C-36 fails.

### C-42 -- Pre-Table SLA Budget Pre-Commitment *(E-34)*
Analogous to C-35's per-class carrying-cost pre-commitment, the prompt includes a named
pre-table SLA Budget section that pre-commits Recovery Path SLA targets -- TTD (Time to
Detect), TTC (Time to Contain), TTR (Time to Recover), TTV (Time to Validate), or
equivalent named time commitments -- for each failure class before the scenario table
begins. The Column Contract Recovery Path entry names the SLA Budget section as the
reference source for SLA target fills, rather than specifying SLA values as independently
authored per-row content. At least one row descriptor explicitly names the SLA Budget
section as the constraint source for that row's SLA annotations -- e.g., "SLA targets
from pre-committed SLA Budget (above)." This creates the same pre-commitment contract
for SLA targets that C-35 creates for carrying costs: independently authored per-row SLA
values become a visible contract violation rather than a silent divergence from the
pre-committed budget. A prompt that satisfies C-30 (SLA-annotated recovery stages)
without a pre-committed SLA Budget reference source does not satisfy this criterion.

**Pass condition**: A named pre-table SLA Budget section pre-commits SLA targets for all
four recovery stages (TTD / TTC / TTR / TTV or equivalent) covering all three failure
classes. The Column Contract Recovery Path entry names the SLA Budget section as the
reference source for SLA target fills -- not a free-fill requirement. At least one row
descriptor names the SLA Budget section as the constraint source for that row's SLA
annotations. C-30 must also pass -- C-42 cannot pass if C-30 fails. C-35 must also pass
-- C-42 cannot pass if C-35 fails (SLA Budget pre-commitment parallels the Inertia
Assessment's pre-commitment pattern; the structural requirement is the same).

### C-43 -- Failure Signature Column Specification *(E-35)*
The Column Contract includes a Failure Signature column (or equivalently named column)
that specifies, per scenario row, the observable behavioral fingerprint of the failure
in progress -- distinct from Trigger Condition (C-33, which bounds the entry threshold)
and from State (which describes system configuration at failure onset). The Failure
Signature describes what the failure looks like to each system actor *while the failure
is occurring*: e.g., "client view: repeated connection timeouts with no TCP reset;
server view: silent queue growth without consumer acknowledgment" for connectivity loss,
or "node-A view: holds last-write state; node-B view: holds diverging last-write state;
observability view: no conflict event logged" for split-brain. The actor differentiation
is structural: at least two distinct actor viewpoints (e.g., client / server, node-A /
node-B, or user / operator) must be named per row. This transforms scenario descriptions
from entry-bounded state snapshots into behaviorally characterized patterns
independently identifiable by their runtime signature rather than only by preconditions.

**Pass condition**: A Failure Signature column (or equivalent) appears in the Column
Contract meta-table (C-24) with a Fill Requirement specifying the observable behavioral
pattern per actor during the failure, explicitly distinguished from trigger entry
conditions (C-33) and from pre-failure state. At least one row descriptor fills the
Failure Signature with actor-differentiated behavioral descriptions naming at least two
distinct actors and their respective observable patterns -- generic descriptions ("system
is unavailable") without actor differentiation fail. C-24 must also pass -- C-43 cannot
pass if C-24 fails. C-33 must also pass -- C-43 cannot pass if C-33 fails (Failure
Signature requires a clear structural distinction from Trigger Condition; that
distinction requires Trigger Condition to be defined in the Column Contract).

---

**Scoring formula**: `aspirational_pass/35 * 10`

**Ceiling references under v14**:
- V-05 (Round 7 best, re-scored): C-17 through C-27 PASS, C-28 through C-43 FAIL
  -> 11/35 x 10 = 3.14 -> composite = 60 + 30 + 3.14 = **93.14**
- V-05 (Round 8, all three axes, re-scored): C-17 through C-29 PASS, C-30 through C-43 FAIL
  -> 13/35 x 10 = 3.71 -> composite = 60 + 30 + 3.71 = **93.71**
- V-05 (Round 9, all three axes, re-scored): C-17 through C-31 PASS, C-32 through C-43 FAIL
  -> 15/35 x 10 = 4.29 -> composite = 60 + 30 + 4.29 = **94.29**
- V-05 (Round 10, all three axes, re-scored): C-17 through C-34 PASS, C-35 through C-43 FAIL
  -> 18/35 x 10 = 5.14 -> composite = 60 + 30 + 5.14 = **95.14**
- V-03 / V-05 (Round 11, inertia axis, re-scored): C-17 through C-37 PASS; C-09 to C-16, C-38 to C-43 FAIL
  -> 21/35 x 10 = 6.00 -> composite = 60 + 30 + 6.00 = **96.00** (R11 ceiling)
- V-01 (Round 12, Axis D only, re-scored): C-09, C-14, C-17 through C-37, C-39, C-40 PASS; C-10 to C-13, C-15, C-16, C-38, C-41 to C-43 FAIL
  -> 25/35 x 10 = 7.14 -> composite = **97.14**
- V-03 (Round 12, Axis F only, re-scored): C-11, C-12, C-17 through C-37, C-39, C-40 PASS; C-09, C-10, C-13 to C-16, C-38, C-41 to C-43 FAIL
  -> 25/35 x 10 = 7.14 -> composite = **97.14**
- V-02 (Round 12, Axis E only, re-scored): C-10, C-13, C-15, C-16, C-17 through C-37, C-39, C-40 PASS; C-09, C-11, C-12, C-14, C-38, C-41 to C-43 FAIL
  -> 27/35 x 10 = 7.71 -> composite = **97.71**
- V-04 (Round 12, Axes D + E, re-scored): C-09, C-10, C-13, C-14, C-15, C-16, C-17 through C-37, C-39, C-40 PASS; C-11, C-12, C-38, C-41 to C-43 FAIL
  -> 29/35 x 10 = 8.29 -> composite = **98.29**
- V-05 (Round 12, Axes D + E + F, re-scored): C-09 through C-40 all PASS; C-41 to C-43 FAIL
  -> 32/35 x 10 = 9.14 -> composite = **99.14** (R12 ceiling under v14)
- V-03 (Round 13, re-scored): essential + recommended PASS; aspirational: C-09 to C-18 PASS (10), C-20 to C-22 PASS (3), C-24 to C-26 PASS (3), C-32 + C-33 + C-38 + C-40 PASS (4); C-19 PARTIAL (0.5), C-23 PARTIAL (0.5); C-27 to C-31 FAIL (cascade from C-23/C-19); C-34 to C-37 FAIL (cascade from C-30/C-31); C-39 FAIL (cascade from C-19 PARTIAL); C-41 to C-43 FAIL
  -> 21/35 x 10 = 6.00 -> composite = **96.00**
- V-01 / V-02 / V-04 / V-05 (Round 13, re-scored): C-09 through C-40 all PASS; C-41 to C-43 FAIL
  -> 32/35 x 10 = 9.14 -> composite = **99.14** (R13 ceiling under v14)
- R14 ceiling (open -- pending per-variation axis-coverage scoring):
  All five pass C-09 through C-40 (32 criteria). C-41 to C-43 determined by axis coverage.
  - Single-axis variation (one new criterion): 33/35 x 10 = 9.43 -> composite = **99.43**
  - Two-axis variation (two new criteria): 34/35 x 10 = 9.71 -> composite = **99.71**
  - Full three-axis variation (C-41 + C-42 + C-43 PASS): 35/35 x 10 = 10.00 -> composite = **100.00**
