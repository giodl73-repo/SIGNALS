Written to `simulations/quest/rubrics/flow-resilience-rubric-v14-2026-03-15.md`.

---

## v14 summary

Three new criteria extracted from R13 excellence signals:

| Criterion | E-tag | Signal | Cracked by |
|-----------|-------|--------|------------|
| **C-42** -- Gate-Close Clause Structural Independence | E-28 | V-01/V-04/V-05 split Gate 2b CLOSE into TWO independent checkboxes; V-02/V-03 use combined form (satisfies C-40 but conflates two audit points) | V-01, V-04, V-05 |
| **C-43** -- Impossibility Argument Basis Clause Independence | E-29 | V-02/V-04/V-05 split Gate 1 CLOSE into TWO independent checkboxes (required-basis:present + prohibited-basis:absent); V-01 uses combined statement (satisfies C-41 but not C-43) | V-02, V-04, V-05 |
| **C-44** -- Bidirectional Gap Registry Artifact Structure | E-30 | V-03/V-05 formal PART A + PART B GAP REGISTRY with three-field entries (Source / Missing link / Consequence); V-01/V-02/V-04 use inline gap notation (satisfies C-38 but not C-44) | V-03, V-05 |

**Scoring delta**: uncapped max 66 -> 72 (36 criteria x 2). Cap unchanged at 10.

**R13 discrimination under v14:**

| Rank | Variation | C-42 | C-43 | C-44 | Uncapped |
|------|-----------|------|------|------|---------|
| 1 | V-05 | PASS | PASS | PASS | **72/72** |
| 2 | V-04 | PASS | PASS | FAIL | **70/72** |
| 3 | V-01 | PASS | FAIL | FAIL | **68/72** |
| 4 | V-02 | FAIL | PASS | FAIL | **67/72** |
| 5 | V-03 | FAIL | FAIL | PASS | **65/72** |

**V-05 achieves 72/72** -- first perfect uncapped score across all rounds. Open for R14: C-43 for V-01; C-42 for V-02/V-03; C-44 for V-01/V-02/V-04; C-15 for V-02/V-03.
ined statement vs two independent checkboxes -- one
structural split away from 70/72); C-42 PASS for V-02/V-03 (combined CLOSE form); C-44 PASS for
V-01/V-02/V-04 (inline gap findings, not formal registry); C-15 PASS for V-02/V-03 (DS Primitive
cited field with VALID/INVALID examples still absent in prose-only form). V-05 achieves 72/72 --
no open criteria remain uncracked; all structural independence patterns are now represented.

**Design rationale highlights:**
- **C-42** is orthogonal to C-40 -- C-40 requires both a positive clause and a prohibition clause
  in the CLOSE block; C-42 requires those clauses to be STRUCTURALLY INDEPENDENT items. A combined
  form satisfies C-40 but fails C-42: when the combined item is disputed, a reviewer cannot
  determine from the CLOSE block alone whether the positive assertion failed, the prohibition
  failed, or both. Separate checkboxes (V-01/V-04/V-05) make each clause independently falsifiable.
  V-02/V-03's combined form "(identity assertion satisfied -- no paraphrase, no independent
  calibration)" passes C-40 but fails C-42.
- **C-43** is orthogonal to C-41 -- C-41 requires the Gate 1 CLOSE postcondition to name required
  basis AND prohibited basis; C-43 requires those checks to be STRUCTURALLY INDEPENDENT items.
  V-01's combined statement "(architecture basis, not description absence)" satisfies C-41 but
  fails C-43: the required-basis check and the prohibited-basis check are evaluated together.
  V-02/V-04/V-05's two-checkbox form evaluates each independently. This matters when an argument
  cites an architecture basis but also includes a supplementary description-absence component --
  the combined check may pass while the prohibition is partially violated.
- **C-44** is orthogonal to C-38 -- C-38 requires the bidirectional matrix to emit a named gap
  finding for uncovered entries; C-44 requires each gap finding to be a structured three-field
  artifact in a named registry section. V-01/V-02/V-04's inline notation ("Dark chaos finding:
  CHAOS-OBS-GAP-NN: ...") names the problem but not the consequence -- a reviewer scanning for gap
  severity must read the prose. V-03/V-05's formal PART A/B GAP REGISTRY with Source / Missing
  link / Consequence fields makes each gap's impact independently auditable and queryable. C-38 is
  satisfied by inline notation; C-44 requires the registry structure.
- **V-05 achieves 72/72** -- the first perfect uncapped score across all rounds. It integrates all
  three structural independence patterns: two-checkbox Gate 2b CLOSE (C-42), two-checkbox Gate 1
  CLOSE (C-43), and formal gap registries (C-44). V-04 at 70/72 lacks only C-44 (formal registry).
  V-01 at 68/72 lacks C-43 (combined Gate 1 statement) and C-44. The independence patterns
  (C-42/C-43) and the registry pattern (C-44) are the remaining R14 discrimination axes.

**C-42 -- Gate-Close Clause Structural Independence (E-28)**
- Signal: V-01's Gate 2b CLOSE: TWO checkboxes -- `[ ] Identity assertion confirmed: every TCR
  contains the verbatim Gate 2 threshold expression -- identical string, not a paraphrase` AND
  `[ ] Prohibition clause confirmed: no TCR contains a paraphrased or independently calibrated
  expression -- no paraphrase, no independent calibration`. V-04/V-05 carry the same two-checkbox
  structure. V-02's Gate 2b CLOSE: ONE combined checkbox -- `[ ] Every Trigger Condition Reference
  contains verbatim Gate 2 threshold expression (identity assertion satisfied -- no paraphrase, no
  independent calibration)`. V-03 uses the same combined form.
- The gap it closes: C-40 requires both a positive confirmation clause and a prohibition clause in
  the CLOSE block. A combined form satisfies C-40 -- both components are present. However, a
  single combined audit point creates an ambiguity under dispute: if the combined item fails, a
  reviewer cannot determine from the CLOSE block alone whether the positive assertion failed, the
  prohibition check failed, or both. Structurally independent checkboxes close this gap: the
  positive assertion can be confirmed while the prohibition check is still pending, or vice versa.
  The independence also enables targeted remediation -- a gate whose positive assertion is confirmed
  but whose prohibition check is not can be re-opened at the prohibition level without invalidating
  the positive confirmation. The combined form is not incorrect; it is structurally less auditable.
- Pass requires: The gate CLOSE block contains the positive confirmation clause AND the prohibition
  clause as SEPARATE, independently-checkable items -- separate checkboxes, separately labeled
  blocks, or equivalent independently-auditable structural form. Each item must be capable of being
  individually confirmed or denied. A single combined item carrying both clauses in one statement
  satisfies C-40 but does not satisfy C-42. The two items must appear in the gate CLOSE block; a
  prohibition clause in a column Fill Requirement or a positive confirmation in the preamble without
  a corresponding independent CLOSE item does not satisfy this criterion.
- Partial: CLOSE block carries both positive confirmation and prohibition clause but in a partially
  separated form -- e.g., main clause plus parenthetical sub-clause within a single checkbox; or
  two prose lines in the CLOSE block that are conceptually distinct but share a single checkbox
  form; or independent structure present for one gate but combined form used in other gates where
  both clause types apply.
- Fail: No gate CLOSE block carries both positive confirmation and prohibition clauses as separate
  items; all CLOSE blocks with both clause types use combined form (C-40-passing but C-42-failing);
  or C-40 FAIL subsumes C-42.

**C-43 -- Impossibility Argument Basis Clause Independence (E-29)**
- Signal: V-02's Gate 1 CLOSE: TWO independent items -- `[ ] Impossibility argument basis
  confirmed: every Argued-Impossible cites an architecture basis (CAP theorem guarantee, synchrony
  constraint, topology bound) -- required basis: present` AND `[ ] Impossibility argument
  prohibition confirmed: no Argued-Impossible argument is based on description absence (the topic
  does not mention X) -- prohibited basis: absent`. V-04/V-05 carry the same two-item structure.
  V-01's Gate 1 CLOSE: ONE combined postcondition -- `[ ] Every Argued-Impossible has DS Primitive
  cited: field completed (architecture basis, not description absence)`. The combined form passes
  C-41; the two-item form satisfies C-43.
- The gap it closes: C-41 requires the Gate 1 CLOSE postcondition to name the required basis type
  (architecture) and the prohibited basis type (description absence) in the same postcondition
  statement. A combined statement satisfies C-41 -- both types are named. However, the combined
  form conflates two independently-verifiable conditions: (a) that a valid architecture basis IS
  present and (b) that a description-absence argument IS NOT present. These conditions are not
  logically equivalent: an argument can cite an architecture basis and also include a supplementary
  description-absence component; an argument can fail to cite an architecture basis without
  explicitly invoking description absence. Independent items allow each condition to be confirmed or
  denied separately, making the Gate 1 closure audit more granular. A combined item may pass when
  a partial violation exists if the violation is in the less-salient component of the conjunction.
- Pass requires: Gate 1 CLOSE postcondition contains required-basis verification ("architecture
  basis present" or equivalent) AND prohibited-basis verification ("description absence absent" or
  equivalent) as SEPARATE, independently-checkable items -- separate checkboxes, separate labeled
  verification blocks, or equivalent independent structural form. Each item must name its condition
  explicitly and be individually confirmable. A single combined postcondition naming both satisfies
  C-41 but does not satisfy C-43. Both items must appear in the Gate 1 CLOSE block; a prohibited-
  basis note in the column Fill Requirement without a corresponding independent CLOSE item does not
  satisfy this criterion.
- Partial: Gate 1 CLOSE contains both required-basis and prohibited-basis checks in a partially
  separated form -- e.g., a single item with labeled sub-clauses ("required basis: present;
  prohibited basis: absent") within one checkbox; or two independent items present but only for a
  subset of impossibility argument types covered by the postcondition.
- Fail: Gate 1 CLOSE postcondition combines required-basis and prohibited-basis in a single unitary
  statement (C-41-passing combined form); or Gate 1 CLOSE carries only one of the two checks
  independently; or C-41 FAIL subsumes C-43 (no Gate 1 quality postcondition exists).

**C-44 -- Bidirectional Gap Registry Artifact Structure (E-30)**
- Signal: V-03's bidirectional matrix requires formal PART A GAP REGISTRY and PART B GAP REGISTRY
  sections before COMPLETE can be declared. Each entry in the registry is a structured three-field
  artifact: Source (the uncovered chaos scenario ID or Observable Signal ID) / Missing link (the
  Observable Signal or chaos scenario that should cover it but does not) / Consequence (what is
  made unverifiable by this coverage gap). V-05 carries the same formal registry structure. V-01
  uses the R12 V-05 standard form with inline gap findings: "Dark chaos finding: CS-NN has no
  linked Observable Signal -> dark chaos scenario. Emit: CHAOS-OBS-GAP-NN". V-02/V-04 use the
  same abbreviated inline form.
- The gap it closes: C-38 requires the bidirectional matrix to emit a named gap finding for any
  uncovered entry in either direction. The inline form (V-01/V-02/V-04) satisfies C-38 -- each
  uncovered entry produces a named finding tag. However, the inline form names the problem without
  structuring the consequence: "CHAOS-OBS-GAP-01: CS-03 has no linked Observable Signal" identifies
  the gap but does not record why the gap matters, making gap severity invisible to a reviewer
  scanning for risk priority without reading surrounding scenario prose. The formal registry adds a
  Consequence field that is independently readable per gap entry. The three-field structure also
  enables registry-level queries (e.g., all consequences of dark chaos scenarios) that inline
  notation cannot support. When the matrix has no uncovered entries, an explicit nil confirmation
  in the registry ("GAP REGISTRY: no uncovered entries") closes the gap that inline notation leaves
  open: inline absence of gap findings is ambiguous between "no gaps" and "gaps not checked."
- Pass requires: The bidirectional coverage matrix produces gap findings as structured three-field
  registry entries in a named section (PART A GAP REGISTRY / PART B GAP REGISTRY, or equivalent
  named registry section). Each entry must carry three explicitly named fields covering: (1) the
  uncovered element identifier (Source), (2) what coverage link is absent (Missing link), and (3)
  what the gap makes unverifiable (Consequence). Both directions must have a named registry section;
  a registry for Part A only satisfies PARTIAL. When the matrix has no uncovered entries, an
  explicit nil confirmation must appear in each registry section. Inline gap notation satisfying
  C-38 does not satisfy C-44; the formal named registry structure is required.
- Partial: Formal registry section present but entries carry fewer than three named fields -- e.g.,
  Source and Missing link without Consequence; or formal registry present for one direction (Part A
  or Part B) but not both; or three-field entries present but embedded in inline notation rather
  than a named registry section; or registry present but nil confirmation absent when no gaps exist.
- Fail: No formal gap registry section in either direction; gap findings appear only as inline
  notations within matrix rows or as prose annotations; or C-38 FAIL subsumes C-44.

**Scoring delta**: aspirational cap unchanged at 10; uncapped max rises from 66 -> 72
(36 criteria x PASS=2).

**R13 discrimination under v14 (uncapped aspirational tiebreak; all composite = 100/100):**

| Rank | Variation | C-42 | C-43 | C-44 | Uncapped Asp. |
|------|-----------|------|------|------|--------------|
| 1 | **V-05** | PASS | PASS | PASS | 72/72 |
| 2 | **V-04** | PASS | PASS | FAIL | 70/72 |
| 3 | **V-01** | PASS | FAIL | FAIL | 68/72 |
| 4 | **V-02** | FAIL | PASS | FAIL | 67/72 |
| 5 | **V-03** | FAIL | FAIL | PASS | 65/72 |

Open for R14: C-43 PASS for V-01 (combined Gate 1 statement needs split into two independent
checkboxes); C-42 PASS for V-02/V-03 (combined Gate 2b CLOSE form); C-44 PASS for V-01/V-02/V-04
(inline gap findings need formal registry structure); C-15 PASS for V-02/V-03 (DS Primitive cited
field with VALID/INVALID examples absent in prose-only form). No fully uncracked criteria remain --
V-05 achieves 72/72 in R13.

---

## v13 summary

Three new criteria extracted from R12 excellence signals:

| Criterion | E-tag | Signal | Cracked by |
|-----------|-------|--------|------------|
| **C-39** -- Gate-Open Precondition Acknowledgment Checkpoint | E-25 | V-02/V-04 Gate 2b OPEN precondition carries explicit named acknowledgment ("verbatim -- not a derivative") before any row filling begins -- a confirmable checkpoint, not a copy instruction | V-02, V-04, V-05 |
| **C-40** -- Gate-Close Prohibition Clause | E-26 | V-02/V-04 Gate 2b CLOSE adds "no paraphrase, no independent calibration" alongside the positive confirmation -- absence verification orthogonal to presence checking | V-02, V-04 |
| **C-41** -- Impossibility Argument Quality Gate Postcondition | E-27 | V-01/V-05 Gate 1 CLOSE postcondition names both required basis ("architecture basis") AND prohibited basis ("not description absence") in one statement -- quality enforcement at gate-close time, beyond C-15's field+examples presence requirement | V-01, V-05 |

**Scoring delta**: uncapped max 60 -> 66 (33 criteria x 2). Cap unchanged at 10.

**R12 discrimination under v13:**

| Rank | Variation | C-15 | C-36 | C-38 | C-39 | C-40 | C-41 | Uncapped |
|------|-----------|------|------|------|------|------|------|---------|
| 1 | V-05 | PASS | PASS | PASS | PASS | PARTIAL | PASS | **65/66** |
| 2 (tie) | V-02 | PARTIAL | PASS | PARTIAL | PASS | PASS | FAIL | **62/66** |
| 2 (tie) | V-04 | PARTIAL | PASS | PARTIAL | PASS | PASS | FAIL | **62/66** |
| 4 | V-01 | PASS | PARTIAL | PARTIAL | FAIL | FAIL | PASS | **60/66** |
| 5 | V-03 | PARTIAL | PARTIAL | PARTIAL | FAIL | FAIL | FAIL | **57/66** |

Open for R13: C-40 PASS for V-05 (one prohibition clause away from 66/66); C-38 PASS for V-01
through V-04 (bidirectional ID-level matrix with named gap findings absent); C-15/C-41 PASS for
V-02/V-03/V-04 (Gate 1 quality postcondition absent). No fully uncracked criteria remain -- the
persistent uncracked block (C-15) was resolved in R12.

**Key design rationale:**
- **C-39** is orthogonal to both C-18 (entry conditions) and C-31 (pre-analysis declaration) -- a
  constraint can be declared upfront, stated as an entry condition, AND confirmed at gate-entry
  time; only C-39 requires the last step
- **C-40** closes the semantically-equivalent loophole that positive CLOSE conditions cannot cover
  -- "verbatim Gate 2 threshold expression" satisfies C-36's identity assertion, but a paraphrase
  passes the positive check while introducing interpretive drift. V-05's CLOSE confirms "(identity
  assertion satisfied)" without a prohibition clause, scoring PARTIAL -- demonstrating that the
  positive confirmation and the prohibition clause are independently load-bearing.
- **C-41** closes the quality-vs-presence gap at Gate 1 closure -- C-15 requires the DS Primitive
  cited field and VALID/INVALID examples. A Gate 1 CLOSE that checks only "DS Primitive cited:
  field non-empty" verifies presence; a description-absence argument satisfies presence while
  failing the architecture-basis standard. V-01/V-05 name the prohibited form in the CLOSE
  postcondition, making quality a gate-closure requirement rather than relying solely on field
  design. Also resolves C-15's persistent PARTIAL block in R12 for V-01 and V-05.

---

## v12 summary

Three new aspirational criteria extracted from Round 11 excellence signals:

| Criterion | E-tag | Source | Cracked by |
|-----------|-------|--------|------------|
| **C-36** -- Chaos-Trigger Threshold Identity Assertion | E-22 | V-05: Column Contract explicitly asserts Gate 2b activation boundary = same threshold expression as Trigger Condition -- identity claim, not a reference link | V-05 only |
| **C-37** -- Observable Signal Detection Horizon | E-23 | V-04/V-05: Detection Horizon as third required component of Observable Signal, defining maximum latency window before signal absence is itself a finding | V-04, V-05 |
| **C-38** -- Chaos-Observability Bidirectional Coverage Matrix | E-24 | V-05: Named cross-reference artifact linking every chaos scenario to >= 1 Observable Signal and vice versa -- V-04 has both C-09 and C-10 outputs but no bridging matrix | V-05 only |

**Scoring delta**: aspirational cap unchanged at 10; uncapped max 54 -> 60 (30 criteria x 2).

**R11 discrimination under v12** (all composites 100/100; tiebreak by uncapped aspirational):

| Rank | Variation | C-36 | C-37 | C-38 | Uncapped Asp. |
|------|-----------|------|------|------|--------------|
| 1 | **V-05** | PASS | PASS | PASS | 59/60 |
| 2 | **V-04** | PARTIAL | PASS | FAIL | 56/60 |
| 3 | **V-03** | PARTIAL | FAIL | FAIL | 54/60 |
| 4 | **V-01** | PARTIAL | FAIL | FAIL | 52/60 |
| 5 | **V-02** | FAIL | FAIL | FAIL | 51/60 |

Open for R12: C-38 and C-36 PASS form (both V-05 only). Persistent uncracked: C-15 PASS (inline
VALID/INVALID examples absent in all rounds).

**Key design rationale:**
- **C-36** distinguishes *identity* from *reference* -- V-01/V-03/V-04 all link to the Trigger
  Condition threshold; only V-05 asserts the chaos activation boundary IS that threshold,
  foreclosing calibration drift
- **C-37** fills the gap between "signal exists" (C-10 base) and "signal absence is actionable"
  -- detection horizon operationalizes absence as a finding with a time boundary, orthogonal to
  both the SLA target (C-35) and the activation threshold (C-34)
- **C-38** closes the V-04 loophole -- having separate C-09 and C-10 outputs is not sufficient;
  "dark chaos" scenarios (fire but unobservable) and "untested observability" hooks (specified but
  never exercised) require an explicit bridging artifact

---

## v11 changes from v10

Three new aspirational criteria added from Round 10 excellence signals:

**C-33 -- Intra-Row Column-Group Phase Gate**
- Signal: V-01/V-04/V-05's "C-phase complete before D-phase begins" advance-inhibitor embedded in
  each row descriptor.
- The gap it closes: row-level gate fires after the row is complete; column-group gate fires before
  D-phase begins within the row -- closes mid-row omission risk.
- Pass requires all elements: named column ownership phases / advance-inhibitor at row descriptor
  level / non-placeholder check for all C-phase cells before D-phase begins.

**C-34 -- Trigger Condition Column: Threshold Expression + Detection Signal**
- Signal: V-02/V-05's Trigger Condition column requiring both a quantified activation threshold
  and a named detection signal (the observable mechanism confirming threshold crossing).
- The gap it closes: the scenario's activation boundary must be operationalizable for alerting from
  column scan alone. A qualitative trigger description cannot be wired to an alert system; a
  threshold expression without a detection signal cannot confirm when the threshold is crossed in
  production. Both components are independently load-bearing.
- Pass requires: dedicated Trigger Condition column with Fill Requirement naming both components;
  at least one row fills both with non-generic content.

**C-35 -- Three-Component Recovery Stage Specification**
- Signal: V-03/V-04/V-05's Recovery Path column extension to three required components per stage:
  mechanism + SLA target + Verification Signal (VS).
- The gap it closes: C-07 requires actor-labeled recovery steps; C-35 requires each stage to be
  independently falsifiable -- the stage is complete when the named observable appears, not when
  the SLA timer expires.
- Pass requires: all three components (mechanism, SLA target, named VS) explicitly required for
  each of the four stages; VS must be named, observable, and distinct from the mechanism.

**Scoring delta**: aspirational cap unchanged at 10; uncapped max rises from 48 -> 54
(27 criteria x PASS=2).

**R10 discrimination under v11 (uncapped aspirational tiebreak; all composite = 100/100):**

| Rank | Variation | C-33 | C-34 | C-35 | Uncapped Asp. |
|------|-----------|------|------|------|--------------|
| 1 | **V-05** | PASS | PASS | PASS | 50/54 |
| 2 | **V-04** | PASS | FAIL | PASS | 47/54 |
| 3 | **V-01** | PASS | FAIL | FAIL | 46/54 |
| 4 (tie) | V-02 | FAIL | PASS | FAIL | 45/54 |
| 4 (tie) | V-03 | FAIL | FAIL | PASS | 45/54 |

---

## v10 changes from v9

Two new aspirational criteria extracted from Round 9 excellence signals:

**C-31 -- Pre-Analysis Bypass Chain Declaration**
- Signal: V-01's named "Bypass Gate-Reopening Protocol" section declared *before Gate 1*, not
  reactively when a bypass is first detected.
- The gap it closes: C-29 requires the bypass chain to execute correctly; C-31 requires the
  chain's structure to be declared upfront -- analogous to C-21.
- Pass requires all four elements: numbered remediation steps / amendment sub-gate convention /
  authorized actors / COMPLETE-blocking statement.

**C-32 -- Bypass-Trigger Column Scanability**
- Signal: V-02/V-05's BYPASS-TRIGGER column in the registry audit table -- each cell must be a
  trigger citation or explicit N/A/SCENARIO-ABSENT, never blank.
- The gap it closes: C-28 requires invocation completeness in prose; C-32 requires bypass
  detection to be column-scannable independent of prose traversal.

**Scoring delta**: aspirational cap unchanged at 10; uncapped max rises from 44 -> 48
(24 criteria x 2).

---

## Essential Criteria (must pass all -- 60% of score)

### C-01 -- Scenario Coverage
- **Weight**: essential
- **Category**: coverage
- **Text**: The output covers all three resilience scenario classes: (1) full connectivity loss
  (client offline), (2) partial failure (dependent service unavailable), and (3) concurrent writes
  across a partition (split-brain / eventual-consistency conflict).
- **Pass condition**: All three classes are represented by distinct named scenarios. A single
  scenario that attempts to cover all three classes fails. Scenarios that collapse class 2 and
  class 3 into a single "network issue" fail.

### C-02 -- Four-Field Structure Per Scenario
- **Weight**: essential
- **Category**: structure
- **Text**: Every failure scenario includes all four required fields: (1) state -- what the system
  state is when failure occurs; (2) capability -- what the user can still do; (3) data at risk --
  what data may be lost, stale, or inconsistent; (4) recovery path -- how the system returns to a
  healthy state.
- **Pass condition**: Every scenario present in the output includes all four fields with non-trivial
  content (not placeholder, "N/A", or a single word). A scenario missing any field fails this
  criterion entirely.

### C-03 -- Gap Identification (Three Types)
- **Weight**: essential
- **Category**: correctness
- **Text**: The output identifies at least one offline experience gap, at least one data consistency
  violation, and at least one missing recovery flow as distinct named findings. These are the three
  explicit output targets the skill defines.
- **Pass condition**: All three finding types appear, each labeled and actionable -- not merely
  implied or bundled. Generic statements like "offline support may be limited" without specificity
  fail.

### C-04 -- Distributed Systems Accuracy
- **Weight**: essential
- **Category**: correctness
- **Text**: Technical claims about failure modes are consistent with distributed systems
  fundamentals. CAP theorem trade-offs, retry semantics, idempotency requirements, and
  conflict-resolution strategies are used correctly wherever referenced.
- **Pass condition**: No materially incorrect distributed-systems claim is present. Fabricated
  error codes, invented protocols, or impossible consistency guarantees (e.g., strong consistency
  with no latency cost across a partition) fail this criterion.

### C-05 -- Commerce Domain Grounding
- **Weight**: essential
- **Category**: depth
- **Text**: The analysis is grounded in the commerce / distributed systems domain. Failure scenarios
  reference realistic commerce flows -- checkout, inventory reservation, payment processing, order
  fulfillment, cart state -- rather than generic CRUD operations.
- **Pass condition**: At least two scenarios are anchored to a recognizable commerce operation by
  name. Purely abstract or domain-agnostic scenarios fail.

---

## Recommended Criteria (improve output quality -- 30% of score)

### C-06 -- Severity and Blast Radius Classification
- **Weight**: recommended
- **Category**: depth
- **Text**: Each failure scenario is annotated with a severity level (e.g., degraded / impaired /
  down) and a blast radius describing what fraction or segment of users is affected. These labels
  enable triage prioritization.
- **Pass condition**: At least half of the scenarios carry both a severity label and a blast-radius
  estimate or qualifier (e.g., "affects all users in offline mode", "affects <1% under
  split-brain"). Scenarios with severity but no blast radius, or vice versa, do not satisfy this
  criterion.

### C-07 -- Recovery Path Specificity with Actor Labels
- **Weight**: recommended
- **Category**: depth
- **Text**: Recovery paths describe concrete steps or system behaviors -- not just outcomes. Each
  step names who or what initiates the action: client, server, operator, or user. Example: "Client
  retries with exponential back-off up to 5 attempts; on exhaustion, server surfaces a manual
  reconcile UI to the user."
- **Pass condition**: At least two recovery paths include actor-labeled steps. Paths that describe
  only the end state ("system recovers", "data is synchronized") without mechanism fail.

### C-08 -- Conflict Resolution Strategy for Eventual Consistency
- **Weight**: recommended
- **Category**: coverage
- **Text**: For eventual-consistency scenarios, the output specifies what conflict resolution
  strategy is assumed (last-write-wins, merge, manual reconcile, reject-stale) and flags whether
  that strategy is adequate for the data type involved (e.g., LWW is inadequate for inventory
  counts).
- **Pass condition**: At least one eventual-consistency scenario names a conflict-resolution
  strategy and includes a brief adequacy judgment. Scenarios that describe lag or divergence
  without naming a resolution strategy fail.

---

## Aspirational Criteria (raise the bar -- 10% of score)

**Scoring**: PASS=2, PARTIAL=1, FAIL=0 per criterion. Aspirational band capped at 10.
Uncapped maximum across 36 criteria is 72; the cap rewards breadth while holding the composite
ceiling at 100.

### C-09 -- Chaos Engineering Test Cases
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The output includes one or more concrete chaos-engineering test scenarios that could be
  scheduled in a test harness. Each scenario specifies: (1) what to inject (network partition,
  latency spike, service kill, packet loss), (2) expected observable behavior, and (3) a binary
  pass/fail signal.
- **Pass condition**: At least one runnable chaos scenario is present with all three elements.
  Vague suggestions to "test resilience" or "add chaos testing" without specifics fail.
- **Partial**: Chaos scenario present but missing one of the three required elements.
- **Fail**: No chaos engineering content, or suggestions without runnable specifics.

### C-10 -- Observability Hooks Tied to Named Gaps
- **Weight**: aspirational
- **Category**: depth
- **Text**: The output recommends specific observability signals -- metrics, logs, traces, or
  alerts -- that would surface each identified gap in production. Each recommendation is tied to a
  specific named gap or scenario from the analysis with a rationale.
- **Pass condition**: At least two observability recommendations are present, each linked to a
  named gap or scenario with a rationale for why that signal would detect the failure early.
  Generic "add monitoring" suggestions without specifics fail.
- **Partial**: Observability recommendations present but fewer than two are tied to named gaps
  with rationale.
- **Fail**: No observability content, or generic recommendations without gap linkage.

### C-11 -- Confidence-Annotated Discovery Catalog
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The distributed-systems analysis phase carries explicit confidence ratings (high /
  medium / low / impossible) for each failure mode before scenarios are committed to the output.
  Each rating cites its basis -- an architecture constraint or DS theory reference -- not just a
  label. Entries rated "impossible" are excluded from the scenario table but retained in the
  discovery phase with their rationale. Entries rated "low confidence" are barred from the scenario
  table until the confidence basis is resolved; flagging alone does not satisfy this gate. This
  triage gate prevents technically invalid scenarios from polluting the output and makes the
  discovery phase independently auditable. (Signal: V-01, V-04.)
- **Pass condition**: Every failure mode in the discovery phase carries a confidence rating with a
  cited basis; "impossible" entries are excluded from the table with retained rationale;
  "low confidence" entries are barred from the table until resolved -- not merely flagged.
- **Partial**: Confidence ratings present on some entries but not all; or impossible entries
  excluded without cited basis; or low-confidence entries flagged but not gated.
- **Fail**: No confidence annotation on discovery-phase entries; impossible scenarios enter the
  output without challenge.

### C-12 -- Nil-Finding Norm for Gap Sections
- **Weight**: aspirational
- **Category**: coverage
- **Text**: Each of the three typed gap sections (offline experience gaps / data consistency
  violations / missing recovery flows) includes an explicit nil finding when no gaps of that type
  are identified for the given topology or load pattern. A nil finding reads as: "No
  offline-experience gaps identified for this deployment pattern -- all critical paths include
  local-fallback state." The nil finding includes a scope rationale explaining why the gap type
  does not apply; a bare "none found" statement does not satisfy this criterion. Silence is not a
  valid nil finding. (Signal: V-01, V-02, V-03.)
- **Pass condition**: All three gap sections are explicitly present; sections with no findings
  carry a labeled nil finding that includes a brief scope rationale explaining why the gap type
  does not apply for this deployment pattern.
- **Partial**: Some nil findings present but not all three sections covered, or nil findings appear
  without scope rationale (bare "none found" statement).
- **Fail**: Missing gap sections are silently absent; reader cannot distinguish "no gaps found"
  from "gaps not analyzed."

### C-13 -- Coverage Accountability Roster
- **Weight**: aspirational
- **Category**: coverage
- **Text**: The output opens with a pre-analysis roster that commits to minimum per-class coverage
  -- at least two scenarios per degradation class -- before scenario analysis begins. The roster is
  checkable: the reader can verify class coverage against the final scenario list without reading
  the full analysis. When a class slot cannot be filled, the output provides an explicit
  impossibility argument or reclassification -- it does not silently reduce coverage below the
  committed minimum. The challenge mechanism ("why can't you fill this slot?") is answered inline,
  not omitted. (Signal: V-03, V-05.)
- **Pass condition**: Pre-analysis roster is present and commits to >=2 scenarios per class; all
  committed slots are filled or explicitly argued impossible / reclassified; roster is independently
  checkable against the final scenario list.
- **Partial**: Roster present but commits to fewer than 2 per class without argument; or roster
  absent but coverage gaps are argued inline rather than silently dropped.
- **Fail**: No coverage accountability mechanism; degradation-class gaps are silently absent.

### C-14 -- Conflict-Resolution Adequacy as DCV Source
- **Weight**: aspirational
- **Category**: correctness
- **Text**: When conflict-resolution analysis judges a strategy to be inadequate or undefined for a
  given data type, that judgment is explicitly fed back into the data-consistency-violation (DCV)
  gap section as a named DCV finding. The conflict-resolution section and the gap identification
  section are bidirectionally linked -- an inadequate or undefined strategy is always a DCV, not a
  standalone note. This prevents conflict-resolution weaknesses from being isolated in one section
  and invisible to the gap tally. When all strategies are adequate, an explicit CLOSED confirmation
  is written. (Signal: V-02, V-04 -- "inadequate/undefined -> DCV" pattern.)
- **Pass condition**: At least one conflict-resolution adequacy judgment of "inadequate" or
  "undefined" generates an explicit, named DCV entry in the gap identification section. The linkage
  is visible: the DCV entry references the conflict-resolution finding that produced it. When no
  inadequate strategies exist, an explicit CLOSED confirmation is present.
- **Partial**: Inadequate strategies noted in conflict-resolution analysis but not linked to a named
  DCV finding in the gap section; or a DCV entry is present without tracing back to its
  conflict-resolution source.
- **Fail**: Conflict-resolution analysis and gap sections are independent silos with no
  cross-referencing; inadequate strategies do not produce DCV entries.

### C-15 -- DS-Primitive-Grounded Impossibility Arguments
- **Weight**: aspirational
- **Category**: correctness
- **Text**: When a coverage slot in the accountability roster cannot be filled, the impossibility
  argument cites a specific distributed systems primitive -- a named CAP theorem guarantee, a
  deployment topology constraint, or a synchronous consistency guarantee that forecloses the
  failure class. Topic-scope arguments ("the topic doesn't mention caching", "the system
  description is too simple for this class") are not valid impossibility arguments. The argument
  must address the architecture, not the description. The template includes a named "DS Primitive
  cited:" field with inline VALID / INVALID annotated examples so that the distinction between an
  architecture argument and description absence is unambiguous. (Signal: V-03 Round 2; V-02
  Round 3.)
- **Pass condition**: Every impossibility argument cites a specific DS primitive via a named "DS
  Primitive cited:" field with an architecture basis. Inline VALID/INVALID annotated examples are
  present in the template. No topic-scope arguments appear; any argument invoking description
  absence rather than architecture constraint fails.
- **Partial**: Some impossibility arguments cite DS primitives but others rely on topic scope or
  description absence; or DS primitive field is present but lacks inline VALID/INVALID examples.
- **Fail**: Impossibility arguments rely solely on topic scope or description absence; no DS
  primitive is cited; or the challenge mechanism is absent entirely.

### C-16 -- Named Gate-State Vocabulary
- **Weight**: aspirational
- **Category**: format
- **Text**: The confidence triage and gap sections use a fixed, named disposition vocabulary --
  entries are assigned exactly one of: Include / BARRED / Argued-Impossible (or equivalent named
  states). Free-text confidence descriptions that do not resolve to one of these named dispositions
  are not valid. Each gate section carries an explicit binary OPEN / CLOSED declaration visible
  without reading the prose. "Flagged" and similar qualitative labels that do not resolve to a
  named disposition are rejected -- a gate section without a named OPEN/CLOSED state is treated as
  OPEN by definition. A gate cannot close while any entry in that section carries an unresolved
  disposition. (Signal: V-02 C-11; V-03 C-11.)
- **Pass condition**: Every entry in the discovery/triage phase carries one of the named
  dispositions; each gate section displays an explicit OPEN/CLOSED state; no free-text confidence
  label is used as a substitute for a named disposition.
- **Partial**: Named dispositions used for most but not all entries; or OPEN/CLOSED gate states
  present for some sections but not all.
- **Fail**: Discovery entries use free-text confidence descriptions without named dispositions; no
  gate sections carry an explicit OPEN/CLOSED state.

### C-17 -- Permanently Barred Entries as Named Coverage Gaps
- **Weight**: aspirational
- **Category**: coverage
- **Text**: Discovery entries that remain BARRED after the confidence triage gate closes -- where
  the low-confidence basis was never resolved -- are not silently dropped from the output. They are
  recorded as named coverage gaps in the coverage accountability register, distinguishing "analyzed,
  barred, recorded" from "not analyzed." An unresolved BARRED entry that produces no downstream
  artifact is invisible to the reader; "analyzed and excluded for architectural reasons"
  (Argued-Impossible) and "analyzed but confidence never confirmed" (permanently BARRED) are not
  equivalent and must not be conflated. (Signal: V-02 C-11.)
- **Pass condition**: Any entry that is BARRED at the close of the triage gate and whose confidence
  basis was never resolved appears as a named coverage gap in the accountability register. No BARRED
  entry silently disappears from the analysis trace.
- **Partial**: Permanently barred entries noted in prose as unresolved but not formally recorded as
  named coverage gaps in the accountability register.
- **Fail**: BARRED entries with unresolved bases are silently dropped; the reader cannot determine
  whether low-confidence failure modes were excluded intentionally or omitted.

### C-18 -- Explicit Phase Entry and Exit Conditions
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Each analysis phase or gate section specifies (1) its entry condition -- which prior
  gates must be CLOSED before this phase begins, referenced by gate identifier -- and (2) its exit
  condition -- what must be true for this gate to be declared CLOSED, stated explicitly. Phases
  that begin or end without stated conditions are implicitly sequential-by-position, which is
  unverifiable. Silence does not mean CLOSED; an explicit CLOSED confirmation is required. This
  prevents phases from running out of order and makes the analysis closure independently auditable.
  (Signal: V-03 C-14.)
- **Pass condition**: At least two phases carry named entry conditions (citing prior gate
  identifiers) and named exit conditions; each of those phases closes with an explicit CLOSED
  confirmation statement.
- **Partial**: Entry or exit conditions present on some phases but not all; or conditions stated
  but without gate-identifier references; or no explicit CLOSED confirmations.
- **Fail**: No phase carries stated entry/exit conditions; phases are ordered by prose position
  only; closure is inferred, not declared.

### C-19 -- Gate Blockage Transparency (Reason-if-OPEN)
- **Weight**: aspirational
- **Category**: format
- **Text**: When a gate is in OPEN state -- not yet closed -- the blocking reason is declared
  inline as a named "Reason if OPEN:" field or equivalent. An OPEN gate with no stated reason is
  indistinguishable from a gate that was never evaluated or was abandoned mid-analysis. The reason
  field must name the specific blocking condition: the unresolved entry ID, the unmet coverage
  minimum, the pending adequacy verdict, or the outstanding amendment. This allows the analysis to
  be resumed deterministically once the blocking condition is resolved, without re-reading all
  prior gate prose. A gate displaying only "OPEN" without a blocking reason is treated as an error,
  not as a valid in-progress state. (Signal: V-03 Round 4 C-18.)
- **Pass condition**: Every gate that appears in OPEN state carries an explicit "Reason if OPEN:"
  field identifying the specific blocking condition. CLOSED gates do not require a reason field.
  Any OPEN gate lacking a stated reason fails this criterion.
- **Partial**: Some OPEN gates carry stated blocking reasons but not all; or blocking reason
  present but identifies only a category ("unresolved entry") without naming the specific blocking
  item.
- **Fail**: OPEN gates carry no stated reason; or all OPEN gates are declared without
  distinguishing the blocking condition from a routine in-progress state.

### C-20 -- Downstream Gate Amendment with Re-Close Record
- **Weight**: aspirational
- **Category**: correctness
- **Text**: When a downstream finding invalidates the output of an already-CLOSED gate (e.g., a
  conflict-resolution adequacy failure requires an additional DCV entry that the prior DCV gate was
  closed without), the prior gate is explicitly re-opened, the amendment is applied, and the gate
  is re-closed under a labeled amendment sub-gate (e.g., "GATE 3b: AMENDED"). The amendment record
  names the downstream finding that triggered the reopening. Late amendments silently appended to a
  closed section are unverifiable and break the gate audit trail. A re-opened gate whose amendment
  is applied without a labeled re-close record is treated as still OPEN. (Signal: V-03 Round 4
  C-14.)
- **Pass condition**: At least one downstream finding that requires an amendment to a prior CLOSED
  gate triggers an explicit re-open, applies the amendment, and re-closes the gate under a labeled
  sub-gate identifier. The amendment record references the downstream finding by ID. When no
  downstream findings require amendments, an explicit confirmation is present.
- **Partial**: Late amendment applied to a prior closed gate section but without a labeled re-open
  / re-close record; or sub-gate label present but the downstream finding that triggered it is not
  referenced.
- **Fail**: Downstream findings that invalidate prior gate outputs are silently appended without
  re-opening the gate; or no mechanism exists for downstream findings to amend prior gate sections;
  or the gate audit trail has no sub-gate amendment records.

### C-21 -- Pre-Analysis Commerce Operation Scope Declaration
- **Weight**: aspirational
- **Category**: coverage
- **Text**: Before scenario analysis begins, the output commits to a named, exhaustive list of
  commerce operations that will be analyzed. The declaration names every operation in scope (e.g.,
  checkout, inventory reservation, payment processing, cart state, order fulfillment, loyalty
  redemption). This commitment is checkable against the final scenario table: any declared operation
  that receives no scenario coverage is a named gap, not a silent omission. Operations excluded
  from the declaration are either explicitly out-of-scope with a stated reason or their absence is
  a coverage gap. C-05 requires scenarios to be anchored to named operations; C-21 requires the
  scope commitment to precede the analysis, not emerge from it. (Signal: V-05 Round 4 C-05.)
- **Pass condition**: A named commerce operation scope list is present before the first scenario
  entry. The list covers at least four distinct operations. The final scenario table provides
  coverage for each declared operation or explicitly records it as a gap. Operations mentioned only
  within scenario bodies (not declared upfront) do not satisfy this criterion.
- **Partial**: Upfront scope declaration present but covers fewer than four operations; or
  declaration present but final coverage is not cross-checked against the declared list; or
  operations appear only in a post-hoc summary, not a pre-analysis commitment.
- **Fail**: No upfront commerce operation scope declaration; the set of covered operations is
  inferred from the scenario table only; coverage gaps are not distinguishable from scope
  exclusions.

### C-22 -- Typed Nil-Finding Identifiers
- **Weight**: aspirational
- **Category**: format
- **Text**: Nil findings carry gap-type prefix identifiers -- OEG-NIL (offline experience gap),
  DCV-NIL (data consistency violation), MRF-NIL (missing recovery flow) -- that bind each nil
  statement to its gap category by name. C-12 requires nil findings with scope rationale; C-22
  requires those nil findings to be addressable by type. A nil statement without a typed identifier
  satisfies C-12 but cannot be audited, queried, or cross-referenced by gap type. Each typed nil
  identifier is unique within an analysis run; if the same gap type produces a nil in multiple
  phases, each carries its own identifier (OEG-NIL-1, OEG-NIL-2). (Signal: V-01 Round 5 C-12
  PASS evidence.)
- **Pass condition**: Every nil finding carries a typed prefix identifier (OEG-NIL, DCV-NIL,
  MRF-NIL, or equivalent named type prefix). Each identifier is unique within the run. Nil
  statements without a typed identifier fail this criterion regardless of rationale quality.
- **Partial**: Typed identifiers present on some nil findings but not all; or typed prefix used
  but not consistently bound to the gap type.
- **Fail**: No typed nil-finding identifiers; nil statements use only prose headings or bare "none
  found" / "N/A" markers; nil findings are not queryable by gap type.

### C-23 -- Scope Declaration Closure Bracket
- **Weight**: aspirational
- **Category**: format
- **Text**: The pre-analysis commerce operation scope declaration (C-21) is bracketed by two named
  boundary blocks: an opening `SCOPE DECLARATION COMPLETE` confirmation that closes the declaration
  phase before analysis begins, and a terminal `Scope Verification` block that cross-checks the
  declared operation list against the final scenario table after analysis concludes. The terminal
  Scope Verification block must name each declared operation and its coverage outcome (covered / gap
  / out-of-scope). A scope declaration that opens but never formally closes is treated as
  unverified. (Signal: V-01 Round 5 C-21 PASS evidence.)
- **Pass condition**: An opening `SCOPE DECLARATION COMPLETE` block (or named equivalent) is
  present immediately after the operation list, before the first analysis phase. A terminal `Scope
  Verification` block (or named equivalent) is present after the final analysis phase, naming each
  declared operation with its coverage outcome. Both blocks are required; a declaration with only
  one does not satisfy this criterion.
- **Partial**: Opening declaration confirmation present but no terminal verification block; or
  terminal block present but coverage outcomes are not named per declared operation.
- **Fail**: No named boundary blocks; scope declaration embedded in prose with no opening
  confirmation; terminal cross-check absent or inferred from scenario table without a named block.

### C-24 -- Template-Embedded Conditional Linkage Rules
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Cross-section linkages that are required by the skill's logic are encoded in the
  template as explicit named conditional rules -- `if [condition]: [action]` -- rather than
  described in prose instructions or left to analyst discretion. The canonical example is the DCV
  linkage from conflict-resolution adequacy: rather than instructing the analyst to "link inadequate
  strategies to DCV findings," the template contains a named rule: `if verdict is [no | undefined]:
  append DCV-CR-NN`. This makes correct cross-section behavior mandatory and machine-checkable.
  C-14 requires the DCV linkage to exist; C-24 requires it to be encoded as a named conditional
  rule. At least two distinct conditional linkage rules must be present to demonstrate that the
  pattern is systemic, not incidental. (Signal: V-01 Round 5 C-14 PASS evidence.)
- **Pass condition**: At least two named conditional linkage rules are present in the template in
  explicit `if [condition]: [action]` form (or a structurally equivalent named rule block). Each
  rule names both its trigger condition and its cross-section action. Prose instructions that
  describe the same logic without an explicit conditional rule form do not satisfy this criterion.
- **Partial**: One conditional linkage rule present but not two; or rules present in conditional
  form but trigger conditions are underspecified; or rules embedded in prose annotations rather
  than named rule blocks.
- **Fail**: No conditional linkage rules in the template; cross-section linkages are described in
  prose instructions only; correct behavior depends on analyst discretion.

### C-25 -- Nil-Finding Supersession Protocol
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Typed nil-finding identifiers (C-22) have a two-state lifecycle: ACTIVE (nil declared,
  gap type not present) and SUPERSEDED (downstream analysis subsequently identifies a gap in the
  same category). When a downstream phase produces a gap finding that supersedes a previously
  declared nil, the nil identifier is explicitly annotated SUPERSEDED with a cross-reference to the
  finding ID that replaced it (e.g., "OEG-NIL-1: SUPERSEDED by OEG-F-3"). When no nil findings
  are superseded, an explicit "no supersessions" confirmation is present. (Signal: V-01 Round 6
  C-22 PASS evidence.)
- **Pass condition**: At least one nil finding that is superseded by a downstream actual finding
  carries an explicit SUPERSEDED annotation citing the superseding finding ID. When no nil findings
  are superseded during the analysis run, an explicit "no supersessions" confirmation is present.
  A nil ID and a gap finding of the same type coexisting without a SUPERSEDED annotation on the
  nil fails this criterion.
- **Partial**: Supersession notation present on superseded nils but does not cite the superseding
  finding ID; or SUPERSEDED present on some superseded nils but not all; or "no supersessions"
  confirmation absent when no supersessions occur.
- **Fail**: Superseded nil findings carry no SUPERSEDED marker; nil identifiers are treated as
  write-once with no lifecycle tracking.

### C-26 -- Confidence Triage Resolution Sub-Gate
- **Weight**: aspirational
- **Category**: correctness
- **Text**: When a BARRED discovery entry has its unresolved confidence basis subsequently
  satisfied during analysis and is upgraded to Include, the upgrade path is recorded under a
  labeled triage resolution sub-gate (e.g., "GATE 1b: RESOLVED"). The resolution sub-gate must
  name: the entry ID being resolved, the confidence basis that was satisfied and how, the new
  Include disposition, and the re-closed triage gate status. When no BARRED entries are resolved
  during analysis, an explicit "no BARRED-to-Include upgrades" confirmation is present. (Signal:
  V-03 Round 6 structural excellence.)
- **Pass condition**: At least one BARRED entry that is resolved to Include during analysis appears
  under a labeled triage resolution sub-gate naming the entry ID, the satisfied basis, and the new
  disposition, with the triage gate re-closed. When no BARRED entries are resolved during analysis,
  an explicit confirmation is present.
- **Partial**: BARRED-to-Include upgrade recorded in prose but without a labeled sub-gate; or
  sub-gate present but does not name the satisfied basis or the entry ID being resolved; or
  confirmation absent when no upgrades occur.
- **Fail**: BARRED entries silently appear in the scenario table as Include with no resolution
  record; no mechanism exists for BARRED entries to be explicitly resolved.

### C-27 -- Named Rule Block Registry
- **Weight**: aspirational
- **Category**: format
- **Text**: The named conditional linkage rules required by C-24 appear in a discrete, named rule
  registry section within the template -- not embedded inline in gate-section prose. Each rule in
  the registry carries a unique identifier (e.g., RULE-CR-DCV, RULE-SCOPE-GAP,
  RULE-NIL-SUPERSEDE) that makes it independently addressable: other gate sections can cite a rule
  by its ID rather than by prose location. A template where rules are correct in form (satisfying
  C-24) but scattered inline through gate prose satisfies C-24 but fails C-27: inline rules are
  not enumerable, not independently auditable, and cannot be cited by ID. (Signal: V-03 Round 6
  structural excellence.)
- **Pass condition**: A named rule registry section is present listing all conditional linkage
  rules. Each rule carries a unique ID, explicit trigger condition, and named cross-section action
  target. Gate sections that invoke linkage behavior cite rules by their registry ID, not by
  restating the conditional logic inline. At least two rules with distinct IDs are present.
- **Partial**: Named rules present and correct in conditional form (satisfying C-24) but embedded
  inline in individual gate sections rather than in a discrete registry; or registry present but
  fewer than two rules carry unique IDs; or rules listed in the registry but gate sections restate
  the conditional logic inline.
- **Fail**: No named rule registry; all conditional linkage rules appear only as inline annotations
  within gate-section prose; the complete rule set cannot be enumerated without reading the full
  template.

### C-28 -- Post-Analysis Rule Registry Audit
- **Weight**: aspirational
- **Category**: correctness
- **Text**: A named rule registry (C-27) is a declaration; a post-analysis registry audit closes
  the loop by confirming which rules were actually invoked during the analysis run. After all
  analysis gates complete, the output includes a named post-analysis audit block that reviews the
  rule registry and reports: (1) which rules fired during the run, citing the specific gate and
  entry that triggered each invocation; (2) how many times each rule fired; and (3) whether any
  registered rules went uninvoked -- and if so, whether the condition was absent from the analysis
  (scenario-absent) or the condition arose but the rule was not applied (rule-bypassed, which is an
  audit failure). (Signal: V-03 Round 7 structural excellence.)
- **Pass condition**: A named post-analysis audit block is present after all analysis gates
  complete. The block lists each registered rule by ID and reports its invocation status: fired
  (with gate and entry citation) or uninvoked (with scenario-absent or rule-bypassed
  classification). At least two registered rules are accounted for. A rule that is invoked but
  whose invocation is not cited by gate and entry fails this criterion.
- **Partial**: Post-analysis review of rule usage present but not as a named, discrete audit block;
  or block present but covers only some registered rules; or invocations listed without citing the
  triggering gate and entry.
- **Fail**: No post-analysis rule audit; the rule registry is treated as a declaration-only
  artifact with no execution verification.

### C-29 -- Rule-Bypass-Triggered Gate Reopening
- **Weight**: aspirational
- **Category**: correctness
- **Text**: C-28 classifies a registered rule as RULE-BYPASSED when its trigger condition arose
  during a gate but the rule was not applied -- an audit failure. C-29 enforces the consequence: a
  RULE-BYPASSED finding is a gate-reopening trigger, not merely a reported deficiency. Before the
  analysis can declare COMPLETE, the affected gate must be explicitly reopened, the bypassed rule
  applied, the gate re-closed under a labeled amendment sub-gate following the C-20 mechanism
  (e.g., "GATE N-bypass: AMENDED"), and the audit entry updated from RULE-BYPASSED to INVOKED.
  C-28 says what the audit reports; C-29 says what a RULE-BYPASSED finding forces. (Signal: V-01
  Round 8 C-28 PASS evidence.)
- **Pass condition**: When the post-analysis audit produces at least one RULE-BYPASSED finding, an
  explicit gate-reopening chain follows: the affected gate is re-opened, the bypassed rule is
  applied, the gate is re-closed under a labeled amendment sub-gate citing the bypass finding ID,
  and the audit entry is updated to INVOKED before COMPLETE is declared. When no RULE-BYPASSED
  conditions exist in the run, an explicit confirmation is present. An analysis that acknowledges
  RULE-BYPASSED and declares COMPLETE without gate remediation fails this criterion.
- **Partial**: RULE-BYPASSED finding acknowledged and gate reopened but no amendment sub-gate
  label present; or gate re-closed without updating the audit entry to INVOKED; or no explicit
  confirmation when the run contains no bypasses.
- **Fail**: RULE-BYPASSED audit findings present with no gate reopening; analysis declares
  COMPLETE with acknowledged bypass failures unresolved.

### C-30 -- Multi-Act Completion Sign-Off
- **Weight**: aspirational
- **Category**: format
- **Text**: When the analysis is structured in two or more distinct named acts (e.g., Act 1 -- DS
  failure mode analysis, Act 2 -- Commerce validation), the completion declaration requires a
  per-act sign-off for each act, not a single monolithic COMPLETE at the end. Each per-act
  sign-off declares: (1) all gates within that act are CLOSED; (2) the act's scope is exhausted;
  and (3) no RULE-BYPASSED conditions remain unresolved within that act. When the analysis is
  single-act, this criterion is scored N/A and treated as PARTIAL for scoring purposes. (Signal:
  V-01 Round 8 C-28 PASS evidence.)
- **Pass condition**: When the analysis has two or more named acts, each act closes with an
  explicit per-act sign-off block declaring all gates within that act CLOSED, scope exhausted, and
  no unresolved RULE-BYPASSED conditions in that act. The terminal COMPLETE then references the
  per-act sign-offs rather than implying gate closure directly. When the analysis is single-act,
  N/A must be explicitly declared.
- **Partial**: Per-act sign-offs present but missing one of the three required elements; or per-act
  sign-off present for some acts but not all; or analysis is single-act and N/A is explicitly
  declared.
- **Fail**: No per-act sign-offs in a multi-act analysis; terminal COMPLETE subsumes all acts
  without per-act gate closure records.

### C-31 -- Pre-Analysis Bypass Chain Declaration
- **Weight**: aspirational
- **Category**: format
- **Text**: The bypass remediation chain required by C-29 is declared as a named pre-analysis
  section before execution begins -- not reactively when a RULE-BYPASSED condition is first
  detected. The pre-analysis section enumerates: (1) the numbered steps of the bypass remediation
  chain (reopen gate, apply bypassed rule, re-close under amendment sub-gate, update audit entry
  to INVOKED); (2) the amendment sub-gate naming convention to be used (e.g., GATE N-bypass:
  AMENDED); (3) the actors authorized to execute each remediation step; and (4) the explicit
  blocking statement that COMPLETE may not be declared while any RULE-BYPASSED entry remains
  unresolved. C-29 requires the bypass chain to execute correctly when triggered; C-31 requires
  the chain's structure to be visible and independently auditable from the outset, before any
  bypass condition arises. (Signal: V-01 Round 9 C-29 PASS evidence.)
- **Pass condition**: A named pre-analysis bypass chain section (or equivalent named block) is
  present before the first analysis gate. The section enumerates the numbered remediation steps,
  names the amendment sub-gate convention, identifies authorized actors, and states the
  COMPLETE-blocking condition explicitly. The section must be pre-analysis (appearing before Gate
  1), not embedded in a terminal block or post-analysis audit.
- **Partial**: Pre-analysis bypass section present but missing one of the four required elements
  (numbered steps / amendment convention / authorized actors / COMPLETE-blocking statement); or
  bypass chain described in preamble prose without a named section block; or section appears
  mid-analysis rather than before Gate 1.
- **Fail**: No pre-analysis bypass chain section; bypass remediation protocol appears only
  reactively at the point of first RULE-BYPASSED detection; the reader cannot verify the
  protocol's structure before encountering its first invocation.

### C-32 -- Bypass-Trigger Column Scanability
- **Weight**: aspirational
- **Category**: format
- **Text**: When the post-analysis registry audit is structured as a table, each registered rule
  carries a dedicated BYPASS-TRIGGER column. The BYPASS-TRIGGER cell for a given rule is either
  (1) non-empty, naming the gate and entry where the rule's trigger condition arose and the rule
  was not applied; or (2) explicitly marked N/A or SCENARIO-ABSENT, confirming that the rule's
  trigger condition never arose during the run. A blank cell is not a valid entry: blank does not
  distinguish "trigger condition never arose" from "trigger condition arose but was not recorded."
  The column enables horizontal scanability: a reader recovers all RULE-BYPASSED entries by
  scanning a single column, without reading gate prose. This is orthogonal to C-28's prose
  completeness requirement. (Signal: V-02/V-05 Round 9 C-29 PASS evidence.)
- **Pass condition**: A BYPASS-TRIGGER column is present in the rule registry audit table. Every
  registered rule's cell in this column is either non-empty (citing gate and entry that triggered
  bypass detection) or explicitly marked N/A / SCENARIO-ABSENT. Blank cells fail this criterion
  regardless of correctness in other columns.
- **Partial**: BYPASS-TRIGGER column present but some cells are blank rather than explicitly
  confirmed N/A or SCENARIO-ABSENT; or column present but entries do not name the specific gate
  and entry that triggered bypass detection; or bypass detection information is presented in a
  separate prose block rather than a dedicated table column.
- **Fail**: No BYPASS-TRIGGER column in the registry audit table; bypass detection requires
  sequential gate-by-gate prose reading; or registry audit is not table-structured and no
  equivalent scannable column mechanism exists.

### C-33 -- Intra-Row Column-Group Phase Gate *(E-19)*
The scenario table columns are partitioned into ownership phases (e.g., C-phase: Commerce Expert
columns such as State and Capability; D-phase: Distributed Systems Expert columns such as Data at
Risk, Recovery Path, Severity, Blast Radius). Within each scenario row, an advance-inhibitor
embedded directly in the row descriptor prevents D-phase column population from beginning until all
C-phase columns in that row carry non-placeholder content. This gate operates at a level below the
slot (row) and above the individual column -- closing the mid-row omission risk that row-level
advance-inhibitors do not address: the row-level gate fires after the row is complete; the
column-group gate fires before D-phase begins within the row. The gate must be embedded in the row
descriptor at slot level or below (not in preamble or a section-level note) to operate during cell
construction. The column-phase labels must be named explicitly; generic "complete all columns
before proceeding" instructions do not satisfy this criterion because they do not name the
within-row ownership boundary as a distinct gate. (Signal: V-01/V-04/V-05 Round 10 -- "C-phase
complete? Do not begin D-phase columns until State and Capability contain non-placeholder content"
embedded in each row descriptor.)

**Pass condition**: The row descriptor for at least one scenario row contains an explicit
column-group phase gate naming the column ownership phases and requiring all C-phase (or equivalent
first-phase) column cells to carry non-placeholder content before any D-phase column cell is begun.
The gate is embedded inside the row descriptor (slot level or below), not positioned above the
table or in a section header. The phase label boundary must be named. Per-row application is
preferred; partial credit applies if the gate appears once as a template instruction for all rows.

**Partial**: Column-group gate semantics present but embedded in preamble or section-level note
rather than a row descriptor; or gate embedded in a row descriptor but uses generic "complete all
columns" language without naming the column-phase boundary; or gate uses named phases but is
applied to only one row in a table where multiple rows require phase-segregated columns.

**Fail**: No intra-row column-group phase gate anywhere in the prompt; within-row ownership
transitions have no advance-inhibitor at column-group granularity; the progression from C-phase to
D-phase columns within a row is ungated.

### C-34 -- Trigger Condition Column: Threshold Expression + Detection Signal *(E-20)*
The scenario table includes a Trigger Condition column (or equivalently named entry-bounding
column) whose Fill Requirement explicitly mandates two distinct components per cell: (1) a threshold
expression -- a quantified activation condition specifying when the scenario becomes active (e.g.,
"inventory count falls below safety-stock threshold", "payment API p99 latency exceeds 500ms"); and
(2) a detection signal -- the named observable mechanism by which the threshold crossing is
confirmed in production (e.g., "inventory-service health probe returns degraded",
"payment-provider timeout counter exceeds N/window"). Together these transform each scenario from a
reactive failure description into a bounded detection specification: the threshold expression
defines the activation boundary; the detection signal defines the monitoring obligation. A reader
can scan the Trigger Condition column and wire an alert for each scenario without reading scenario
prose. A qualitative trigger description ("when the service is unavailable") cannot be
operationalized for alerting; a threshold expression without a detection signal cannot confirm when
the threshold is crossed in production. Both components are independently load-bearing; absence of
either downgrades to PARTIAL. (Signal: V-02/V-05 Round 10 -- Trigger Condition column with
threshold expression + detection signal, making scenarios operationalizable for alerting directly
from column scan.)

**Pass condition**: A Trigger Condition column (or equivalently named entry-bounding column) is
present in the scenario table and its Fill Requirement explicitly names both the threshold
expression component (quantified activation condition) and the detection signal component (named
observable mechanism) as distinct required fields. At least one scenario row descriptor or example
row fills both components with non-generic content. A qualitative trigger description or a
threshold expression without a corresponding detection signal fails.

**Partial**: Trigger Condition column present but Fill Requirement specifies only one of the two
required components; or both components listed as conceptual requirements but row fills or examples
illustrate only one component populated; or Trigger Condition column present as a header without a
Fill Requirement specification of its two-component structure.

**Fail**: No Trigger Condition column (or equivalent entry-bounding column) in the scenario table;
scenarios are bounded only by failure class labels or qualitative descriptions; scenario activation
conditions are not operationalized in column form.

### C-35 -- Three-Component Recovery Stage Specification *(E-21)*
Each of the four Recovery Path lifecycle stages (Detect, Contain, Recover, Validate) carries three
required components in the column specification or row descriptor: (1) mechanism -- the action
taken to advance the stage, with named actor (extending C-07); (2) SLA target -- a named
time-to-[X] commitment paired to the stage (e.g., TTD/Detect, TTC/Contain, TTR/Recover,
TTV/Validate); and (3) Verification Signal (VS) -- a named observable artifact that confirms the
stage is complete independent of SLA elapse (e.g., "inventory-service heartbeat returns 200",
"payment provider ACK logged to audit trail", "dual-write conflict counter resets to 0 for 60s").
The VS makes each stage independently falsifiable: the stage is closed when the named observable
appears, not when the timer expires. SLA elapse records duration; the VS confirms outcome. A
recovery specification that provides mechanism and SLA without a VS cannot be operationally
verified at stage granularity. Each VS must satisfy three properties: (a) named, not generic ("VS:
confirmation" fails; "VS: inventory-service health probe returns 200" passes); (b) observable -- a
system state, log entry, metric value, or API response code; (c) distinct from the mechanism --
evidence of completion, not a restatement of the action taken. (Signal: V-03/V-04/V-05 Round 10
-- Verification Signal per recovery stage, each stage independently falsifiable by a named
observable artifact distinct from mechanism and SLA elapse alone.)

**Pass condition**: The Recovery Path column specification or at least one scenario row descriptor
explicitly requires all three components -- mechanism (with actor), SLA target, and named
Verification Signal -- for each of the four lifecycle stages. The VS requirements must cover all
four stages; a specification that names VS for two stages but leaves the other two as
mechanism+SLA only fails. At least one row descriptor illustrates concrete VS examples for at
least two of the four stages with named observables. A VS described only generically ("stage
confirmed", "recovery verified") without naming the observable artifact fails.

**Partial**: Three-component structure present in the column specification but row descriptors or
examples show only mechanism + SLA (no VS); or VS present for some stages but not all four in the
column specification; or VS present and named for at least two stages but described generically
(non-named observable) for the remaining stages.

**Fail**: Recovery Path specification contains mechanism and SLA only, with no Verification Signal
component anywhere in the column specification or row descriptors; or VS mentioned in prose but
not encoded as a required column component; or Recovery Path stages are not individually specified
(single-block recovery description with no per-stage structure).

### C-36 -- Chaos-Trigger Threshold Identity Assertion *(E-22)*
The chaos engineering phase (C-09) activation boundary is explicitly asserted in the template to
use the same threshold expression as the Trigger Condition column value (C-34) -- not merely a
cross-reference link to it, but an identity claim. The distinction is load-bearing: a
cross-reference (Trigger Condition Reference) allows the chaos activation parameter to be a
derivative or approximation of the production trigger threshold. An identity assertion forecloses
divergence by design: the chaos scenario activates at exactly the production detection boundary,
making the test result directly interpretable without a parameter-translation step. Without this
assertion, chaos tests may use a threshold that is close to but not identical to the production
trigger -- making results non-predictive and introducing an invisible calibration gap between the
chaos harness and the production alerting system. (Signal: V-05 Round 11 -- Column Contract
explicitly states Gate 2b activation boundary is the same threshold expression as Trigger
Condition; V-01/V-03/V-04 provide a Trigger Condition Reference link without an identity
assertion.)

**Pass condition**: The chaos gate contract (column contract, gate precondition, or named rule)
contains an explicit identity assertion stating that the chaos activation boundary expression is
the same threshold expression as the Trigger Condition column value -- by name ("same threshold
expression as Trigger Condition" or equivalent). A cross-reference link or "see Trigger Condition"
pointer without an identity claim does not satisfy this criterion. The assertion must appear in the
template structure, not only in a row-level example.

**Partial**: Trigger Condition Reference column or field present in the chaos gate structure,
linking the chaos scenario to the threshold from the main scenario table, but without an explicit
identity assertion that the two expressions are identical; or identity assertion present but only
in a row-level example, not in the gate contract or column specification.

**Fail**: No cross-reference between chaos activation boundary and Trigger Condition column in the
chaos gate structure; chaos scenarios specify injection parameters independently of the Trigger
Condition threshold; or no chaos gate structure exists (C-09 FAIL subsumes C-36).

### C-37 -- Observable Signal Detection Horizon *(E-23)*
Each Observable Signal specification (C-10) carries a third required component alongside (1) named
signal and (2) rationale: a Detection Horizon -- the maximum latency window within which the signal
is expected to appear after fault onset or threshold crossing. The Detection Horizon transforms
signal absence from an ambiguous state into a named finding: if the named signal has not appeared
within the declared horizon, absence is itself an actionable event requiring escalation. Without a
Detection Horizon, operators cannot distinguish a signal not yet arrived from a signal permanently
absent -- the absence condition cannot be operationalized. The Detection Horizon is distinct from
the SLA target in C-35 (which measures recovery stage duration) and from the threshold expression
in C-34 (which defines the activation boundary): the Detection Horizon defines how quickly the
monitoring system must confirm the fault, independent of how quickly the system recovers. A generic
horizon ("shortly", "promptly", "as soon as possible") does not satisfy this criterion because it
cannot be operationalized as an alert threshold. (Signal: V-04 Round 11 -- Detection Horizon as
required field in Gate 7 Observability Manifest; V-05 Round 11 -- Detection Horizon as explicit
third component in Gate 3 Observable Signal specification.)

**Pass condition**: Detection Horizon is named as a required component in the Observable Signal
specification (column Fill Requirement, manifest row template, or equivalent named structure). The
horizon specifies a concrete time window (e.g., "within 30s of fault injection", "by next
heartbeat cycle <= 60s", "within one scrape interval"). Generic horizon language fails. At least
one row fill or example illustrates a concrete Detection Horizon value. The Detection Horizon must
be structurally distinct from the SLA target and the threshold expression -- a single field serving
multiple purposes does not satisfy this criterion.

**Partial**: Detection Horizon field present in the observability specification but populated
generically ("promptly", "soon") without a concrete time window; or Detection Horizon concept
present in prose description of the observability section without a named required field in the
column specification; or Detection Horizon named but conflated with SLA target or threshold
expression in a shared field.

**Fail**: No Detection Horizon component in the Observable Signal specification; observability
recommendations carry only named signal + rationale (two-component form); or no observability
structure exists (C-10 FAIL subsumes C-37).

### C-38 -- Chaos-Observability Bidirectional Coverage Matrix *(E-24)*
A named cross-reference artifact -- table, matrix, or manifest -- is produced that links each
chaos scenario (C-09) to >= 1 Observable Signal (C-10) by ID, and each Observable Signal to >= 1
chaos scenario by ID. The matrix enforces bidirectional completeness: a chaos scenario with no
linked Observable Signal is a "dark chaos" scenario -- it fires but cannot be confirmed as
detected, making its pass/fail signal unverifiable in production. An Observable Signal with no
linked chaos scenario cannot be exercised by the chaos harness -- it may exist in the observability
manifest but its production behavior under fault conditions is untested. Both failure modes are
invisible without the bidirectional matrix. The matrix also serves as a cross-artifact audit: when
C-09 and C-10 are each satisfied independently (as in V-04, which has Gate 6 and Gate 7 as
separate Act 3 outputs), the matrix is the only artifact that confirms their content is consistent.
Having both a C-09 output and a C-10 output without a bridging matrix does not satisfy this
criterion. (Signal: V-05 Round 11 -- named Chaos-Observability Coverage Matrix cross-referencing
observability coverage against chaos scenario IDs; V-04 has both C-09 and C-10 outputs but no
bridging matrix.)

**Pass condition**: A named cross-reference artifact is present in the output that lists each chaos
scenario by ID alongside its linked Observable Signal(s) by ID, and lists each Observable Signal
by ID alongside its linked chaos scenario(s) by ID. The artifact emits a named gap finding (e.g.,
CHAOS-OBS-GAP-NN) for any chaos scenario with no Observable Signal linkage and for any Observable
Signal with no chaos scenario linkage. Both directions of coverage must be verified by the
artifact; a one-directional listing satisfies PARTIAL only. The artifact must be a distinct named
section or table, not inferred from co-location of C-09 and C-10 outputs.

**Partial**: Cross-reference artifact present but covers only one direction (chaos ->
observability, or observability -> chaos); or both directions covered but gap findings are not
emitted for uncovered entries; or coverage linkage described in prose without a named artifact; or
C-09 and C-10 outputs co-located in the same section but without a named bridging matrix.

**Fail**: No cross-reference artifact between C-09 and C-10 outputs; chaos scenarios and
observability hooks are independently produced with no traceability between them; or C-09 or C-10
absent (parent criterion FAIL subsumes C-38).

### C-39 -- Gate-Open Precondition Acknowledgment Checkpoint *(E-25)*
The Gate OPEN precondition for a gate that enforces a structural constraint (identity assertion,
coverage minimum, quality standard, or equivalent) includes an explicit named acknowledgment
statement that the analyst confirms before the gate opens. The acknowledgment checkpoint is
distinct from a gate status check ("prior gate is CLOSED") -- it requires active confirmation of a
named constraint that governs the gate's operation, not merely verification that preceding phases
have completed. V-02 uses a checkbox form (`[ ] Identity assertion acknowledged: chaos activation
boundary = Gate 2 threshold expression for each scenario, verbatim -- not a derivative`); V-04 and
V-05 use named prose acknowledgment in the Gate OPEN position. The checkpoint closes the gap
between a constraint being declared (in a Column Contract or pre-analysis section) and a constraint
being confirmed at execution time: an analyst familiar with the template can enter a gate without
re-confirming the governing constraint. The acknowledgment checkpoint forces re-confirmation at
gate-entry time, making constraint compliance independently verifiable for each gate invocation.
C-18 requires named entry conditions (which prior gates must be CLOSED); C-39 requires a named
constraint acknowledgment (which operational rule must be confirmed at entry). C-31 requires the
bypass protocol to be declared upfront; C-39 requires specific constraints to be confirmed at the
moment of gate execution. These three criteria are orthogonal: a gate can carry entry conditions,
pre-analysis declarations, and acknowledgment checkpoints simultaneously. (Signal: V-02/V-04 Round
12 -- Gate 2b OPEN precondition carries explicit identity assertion acknowledgment with "verbatim
-- not a derivative" confirmation; V-01/V-03 carry copy instructions without a confirmable
checkpoint.)

**Pass condition**: At least one gate OPEN precondition block contains an explicit named
acknowledgment statement confirming a specific structural constraint. The acknowledgment must name
the constraint it confirms -- not a generic status or "proceed" declaration. It must be positioned
in the Gate OPEN precondition block (not in a column Fill Requirement, preamble, or row
descriptor). Checkbox form (`[ ]`) is the preferred representation; a named prose acknowledgment
positioned in the Gate OPEN block satisfies this criterion. A copy instruction or fill guidance
("copy threshold expression from Gate 2") is not an acknowledgment checkpoint.

**Partial**: Gate OPEN precondition present but carries only gate status checks (prior gate CLOSED,
required artifact present) without a named constraint acknowledgment; or acknowledgment present in
a column Fill Requirement or preamble declaration rather than a Gate OPEN precondition block; or
acknowledgment names the constraint but is phrased as an instruction rather than a confirmable
checkpoint (e.g., "copy the threshold expression" vs "Identity assertion acknowledged: boundary =
threshold expression -- not a derivative").

**Fail**: No gate OPEN preconditions in any gate; or all gate OPEN preconditions carry only status
checks with no constraint acknowledgment; or acknowledgment pattern present only in pre-analysis
declarations without any gate-entry checkpoint.

### C-40 -- Gate-Close Prohibition Clause *(E-26)*
At least one gate CLOSE condition (postcondition block) contains an explicit prohibition clause --
a named statement of the form "no [failure mode]" or "not a [invalid variant]" -- alongside a
positive confirmation clause. The prohibition clause confirms that a named failure mode is absent
from the gate's output, not merely that the success condition is present. The prohibition pattern
closes a gap that positive-only CLOSE conditions cannot cover: a positive CLOSE condition ("every
X has Y filled") can be satisfied while a prohibited variant coexists -- for example, a threshold
expression semantically equivalent to Gate 2 but differently phrased satisfies the positive
assertion while remaining an unauthorized paraphrase. "No paraphrase, no independent calibration"
in the CLOSE explicitly forecloses the semantically-similar-but-not-identical form. Prohibition
clauses are not redundant with criterion Pass conditions: a Pass condition defines the minimum for
a criterion to succeed; a CLOSE prohibition clause verifies that a specific failure mode is absent
from the produced output even where the nominal success condition is satisfied. V-05's Gate 2b
CLOSE confirms "(identity assertion satisfied)" without a prohibition clause, satisfying C-36 but
scoring PARTIAL for C-40 -- demonstrating that the positive confirmation and the prohibition clause
are independently load-bearing components. (Signal: V-02/V-04 Round 12 -- Gate 2b CLOSE: "Every
Trigger Condition Reference contains verbatim Gate 2 threshold expression (identity assertion
satisfied -- no paraphrase, no independent calibration)"; V-05 CLOSE: "(identity assertion
satisfied)" without prohibition clause.)

**Pass condition**: At least one gate CLOSE condition block contains an explicit prohibition clause
naming a specific failure mode (e.g., "no paraphrase", "no independent calibration", "not a
description-absence argument"). The CLOSE block must carry both a positive confirmation clause
("every X has Y") and at least one prohibition clause ("no Z"). The prohibition must name a
specific failure mode -- generic language ("no errors", "no omissions") does not satisfy this
criterion. The prohibition must appear in the gate CLOSE block, not only in a Pass condition or
column Fill Requirement.

**Partial**: CLOSE conditions contain prohibition-like language but describe consequences rather
than naming the absent failure mode ("if paraphrase detected, gate remains OPEN" vs "no paraphrase"
as a CLOSE-time assertion); or prohibition clause present in a column Fill Requirement or row
descriptor rather than a gate CLOSE block; or the CLOSE block contains a named prohibition but no
positive confirmation clause alongside it.

**Fail**: No gate CLOSE conditions carry prohibition clauses; all CLOSE conditions are
positive-only confirmations; failure mode absence is not verified at gate-close time; or only Pass
conditions (criterion-level) name prohibited forms without a CLOSE-block prohibition clause.

### C-41 -- Impossibility Argument Quality Gate Postcondition *(E-27)*
The Gate 1 CLOSE postcondition (or equivalent confidence triage gate closure block) explicitly
verifies the quality of impossibility arguments -- confirming both field completion and argument
basis -- rather than checking field presence only. C-15 requires the template to carry the DS
Primitive cited field with inline VALID/INVALID examples; C-41 requires the Gate 1 CLOSE
postcondition to enforce argument quality at gate-closure time by naming the required basis type
("architecture basis") and the prohibited basis type ("description absence") in the same
postcondition statement. The distinction between a postcondition that checks presence and one that
checks quality is load-bearing: "DS Primitive cited: field non-empty" is satisfied by a field
containing "the topic does not describe a distributed cache" -- a description-absence argument that
fills the field without meeting the architecture-basis standard. The quality postcondition closes
this gap by making architecture grounding a gate-closure requirement verified at run time, not only
a field design intention enforced by inline examples. When the quality postcondition is absent, an
analyst can satisfy the DS Primitive cited field with any text, with quality relying entirely on
correct interpretation of the inline VALID/INVALID examples rather than on a gate-enforced check.
(Signal: V-01/V-05 Round 12 -- Gate 1 CLOSE postcondition: "Every Argued-Impossible has DS
Primitive cited: field completed (architecture basis, not description absence)"; V-02/V-03/V-04
carry advisory prose about DS Primitive naming with no Gate 1 CLOSE postcondition auditing
argument basis.)

**Pass condition**: The Gate 1 (or equivalent confidence triage gate) CLOSE postcondition
explicitly verifies both (a) the DS Primitive cited field is completed and (b) the basis is
architecture-grounded, naming the prohibited basis type ("description absence" or equivalent) by
name in the same postcondition statement. The postcondition must appear in the CLOSE block (not
only in the column Fill Requirement or preamble). A presence-only CLOSE condition ("DS Primitive
cited: field non-empty") does not satisfy this criterion; both the completion check and the quality
check must be explicit.

**Partial**: Gate 1 CLOSE postcondition present and verifies DS Primitive cited field completion
but does not name the prohibited basis type (presence check without quality check); or the
architecture basis requirement is stated but the prohibited form ("description absence") is not
named in the postcondition; or the quality check appears in a preamble or column specification
rather than in the Gate 1 CLOSE block.

**Fail**: No Gate 1 CLOSE postcondition; or Gate 1 CLOSE postcondition checks only gate status or
coverage counts without auditing impossibility argument quality; or C-15 FAIL subsumes C-41 (no
DS Primitive cited field exists in the template).

### C-42 -- Gate-Close Clause Structural Independence *(E-28)*
A gate CLOSE block that contains both a positive confirmation clause and a prohibition clause
(satisfying C-40) carries those two clauses as STRUCTURALLY INDEPENDENT items -- separate
checkboxes, separately labeled verification blocks, or equivalent independently-auditable form.
C-40 requires both clause types to be present; C-42 requires them to be independently verifiable.
The distinction is load-bearing under dispute: a single combined item ("identity assertion
satisfied -- no paraphrase, no independent calibration") passes C-40 but conflates two distinct
audit points into one. When the combined item is disputed or when one component passes while the
other fails, a reviewer cannot determine from the CLOSE block alone which clause is in violation.
Structurally independent items close this gap: the positive assertion can be confirmed while the
prohibition check is still pending, enabling targeted remediation without invalidating the
confirmed component. The independence also surfaces partial states that combined items mask: a
gate whose positive assertion is satisfied but whose prohibition clause has not been evaluated is
distinguishable from a gate where both clauses have been evaluated and confirmed. (Signal:
V-01/V-04/V-05 Round 13 -- Gate 2b CLOSE splits into `[ ] Identity assertion confirmed: every TCR
contains the verbatim Gate 2 threshold expression` AND `[ ] Prohibition clause confirmed: no TCR
contains a paraphrased or independently calibrated expression`; V-02/V-03 combine both into one
checkbox.)

**Pass condition**: At least one gate CLOSE block contains both positive confirmation clause AND
prohibition clause as SEPARATE, independently-checkable items. Each item must be capable of being
individually confirmed or denied -- separate checkboxes, separate labeled verification entries, or
equivalent form where each clause is auditable without the other. A single combined item carrying
both clauses in one statement satisfies C-40 but does not satisfy C-42. Both items must appear in
the gate CLOSE block; a prohibition clause in a column Fill Requirement alongside a positive
confirmation in the CLOSE block does not satisfy the structural independence requirement for the
CLOSE block itself.

**Partial**: CLOSE block carries both positive confirmation and prohibition clause but in a
partially-separated form -- e.g., a single checkbox with labeled sub-components ("identity
assertion: confirmed; prohibition: confirmed") within one audit point; or independently-structured
items present for one gate CLOSE but combined form used in other gates where both clause types
apply.

**Fail**: No gate CLOSE block carries both clause types as structurally independent items; all
CLOSE blocks with both clause types use combined form (C-40-passing but C-42-failing); or C-40
FAIL subsumes C-42.

### C-43 -- Impossibility Argument Basis Clause Independence *(E-29)*
The Gate 1 CLOSE postcondition (satisfying C-41) splits required-basis verification ("architecture
basis present") and prohibited-basis verification ("description absence absent") into STRUCTURALLY
INDEPENDENT items -- separate checkboxes, separate labeled verification blocks, or equivalent
independently-auditable form. C-41 requires both basis types to be named in the same postcondition
statement; C-43 requires them to be independently verifiable. A combined statement such as
"(architecture basis, not description absence)" satisfies C-41 -- both are named -- but conflates
two independently-assessable conditions into a single audit point: (a) that a valid architecture
basis IS present and (b) that a description-absence argument IS NOT present. These conditions are
not logically equivalent and can fail independently: an argument can cite an architecture basis
while also invoking a supplementary description-absence component, passing the positive check while
partially violating the prohibition. Independent items close this gap: the presence verification
can be confirmed while the absence verification is still pending. Independent form also enables
precise remediation -- a Gate 1 CLOSE where the required-basis check confirms but the
prohibited-basis check fails can be re-opened at the prohibition level alone. (Signal: V-02/V-04/
V-05 Round 13 -- Gate 1 CLOSE splits into `[ ] Impossibility argument basis confirmed: every
Argued-Impossible cites an architecture basis ... -- required basis: present` AND `[ ]
Impossibility argument prohibition confirmed: no Argued-Impossible argument is based on description
absence ... -- prohibited basis: absent`; V-01 uses one combined postcondition statement.)

**Pass condition**: Gate 1 CLOSE postcondition contains required-basis verification AND
prohibited-basis verification as SEPARATE, independently-checkable items. Each item must name its
specific condition and be individually confirmable. A single combined postcondition naming both
satisfies C-41 but does not satisfy C-43. Both items must appear in the Gate 1 CLOSE block;
prohibited-basis language only in a column Fill Requirement or preamble without a corresponding
independent CLOSE item does not satisfy this criterion.

**Partial**: Gate 1 CLOSE contains both basis checks in a partially-separated form -- e.g., a
single item with labeled sub-clauses ("required basis: present; prohibited basis: absent") within
one checkpoint; or two independently-structured items present but covering only a subset of the
basis types verified by the postcondition.

**Fail**: Gate 1 CLOSE postcondition combines required-basis and prohibited-basis in a single
unitary statement (C-41-passing combined form); or Gate 1 CLOSE carries only one of the two basis
checks as an independent item; or C-41 FAIL subsumes C-43.

### C-44 -- Bidirectional Gap Registry Artifact Structure *(E-30)*
The bidirectional coverage matrix (C-38) gap findings are produced as structured three-field
registry entries in a named registry section, rather than as inline notations within matrix rows.
C-38 requires a named gap finding for any uncovered entry; C-44 requires each gap finding to be
a structured artifact with three independently-specified fields: (1) Source -- the uncovered
element identifier (the chaos scenario ID or Observable Signal ID that has no covering link);
(2) Missing link -- the Observable Signal or chaos scenario that should cover it but does not
exist or is not linked; (3) Consequence -- what the coverage gap makes unverifiable in production
(e.g., "dark chaos: CS-03 fires but no Observable Signal can confirm detection; pass/fail
unverifiable"). The three-field structure closes the gap that inline notation leaves open: an
inline finding names the problem but not the consequence, making gap severity invisible to a
reviewer scanning for risk priority without reading surrounding scenario prose. The formal registry
also enables registry-level queries (all consequences of dark chaos scenarios; all missing
Observable Signals) that inline notation cannot support. When the matrix has no uncovered entries,
an explicit nil confirmation must appear in each registry section ("GAP REGISTRY: no uncovered
entries") -- inline absence of gap findings is ambiguous between "no gaps" and "gaps not checked."
(Signal: V-03/V-05 Round 13 -- formal PART A GAP REGISTRY and PART B GAP REGISTRY sections
required before COMPLETE; each entry is a three-field structured artifact; V-01/V-02/V-04 use
inline named-finding notation satisfying C-38 but not C-44.)

**Pass condition**: The bidirectional coverage matrix produces gap findings as structured
three-field registry entries (Source / Missing link / Consequence, or equivalent three named
fields) in a named registry section (PART A GAP REGISTRY / PART B GAP REGISTRY, or equivalent
named sections for each matrix direction). Both matrix directions must have a named registry
section. Each uncovered entry produces a registry artifact with all three fields populated. When
a direction has no uncovered entries, an explicit nil confirmation is present in that registry
section. Inline gap notation with named finding tags satisfies C-38 but does not satisfy C-44; the
formal named registry structure is required.

**Partial**: Formal registry section present but entries carry fewer than three named fields (e.g.,
Source and Consequence without Missing link); or formal registry present with three-field entries
for one matrix direction but not both; or three-field entries present but embedded as inline
annotations within matrix rows rather than in a named registry section; or registry sections
present but nil confirmation absent when a direction has no uncovered entries.

**Fail**: No formal gap registry section in either matrix direction; gap findings appear only as
inline notations or prose annotations; or C-38 FAIL subsumes C-44.

---

## Scoring Formula

| Tier | Weight | Criteria | Per-criterion |
|------|--------|----------|--------------|
| Essential | 60% | C-01, C-02, C-03, C-04, C-05 | PASS=12, PARTIAL=6, FAIL=0 |
| Recommended | 30% | C-06, C-07, C-08 | PASS=10, PARTIAL=5, FAIL=0 |
| Aspirational | 10% | C-09 through C-44 | PASS=2, PARTIAL=1, FAIL=0; capped at 10 |

```
composite = sum(essential_scores)               # max 60
          + sum(recommended_scores)             # max 30
          + min(sum(aspirational_scores), 10)   # max 10 (capped)
```

Maximum possible score: **100**

**Golden threshold**: all 5 essential criteria pass **and** composite >= 80.

**Ceiling references under v14:**
- R13 V-03 (C-41 FAIL; C-15 PARTIAL; C-42/C-43 FAIL; C-44 PASS): 65/72 uncapped
  -> composite = 60 + 30 + 10 = **100** (capped)
- R13 V-02 (C-15 PARTIAL; C-42 FAIL; C-44 FAIL; C-43 PASS): 67/72 uncapped
  -> composite = **100** (capped)
- R13 V-01 (C-43 FAIL; C-44 FAIL; C-42 PASS): 68/72 uncapped
  -> composite = **100** (capped)
- R13 V-04 (C-44 FAIL; C-42/C-43 PASS): 70/72 uncapped
  -> composite = **100** (capped)
- R13 V-05 (all 36 criteria PASS): 72/72 uncapped
  -> composite = **100** (new uncapped ceiling: 72/72 -- first perfect score)
- Open for R14: C-43 PASS for V-01 (combined Gate 1 statement); C-42 PASS for V-02/V-03
  (combined Gate 2b CLOSE form); C-44 PASS for V-01/V-02/V-04 (inline gap findings);
  C-15 PASS for V-02/V-03 (DS Primitive cited field with VALID/INVALID examples absent).

---

## Failure Fast-Paths

The following conditions automatically fail scoring regardless of composite score:

- Output contains no explicit failure scenarios (pure prose advice with no scenario structure)
- Output is domain-agnostic (no commerce or distributed systems grounding anywhere)
- Recovery paths are all identical or all trivially "restart the service" / "wait for recovery"
- Fewer than three degradation classes are represented (offline, partial failure, eventual
  consistency)

---

## Version Notes

**v14 changes from v13:**

- **C-42 (new)** -- Gate-close clause structural independence: extracted from V-01/V-04/V-05
  Round 13 structural excellence (Gate 2b CLOSE splits positive identity assertion and prohibition
  clause into two independently-auditable checkboxes). C-40 requires both clause types to be
  present in the CLOSE block; C-42 requires them to be structurally independent -- separately
  falsifiable, separately confirmable. V-02/V-03 use a combined form that satisfies C-40 but
  conflates two audit points. The independence matters when one clause passes and the other fails:
  combined forms cannot surface this partial state. Cracked by V-01, V-04, V-05.
- **C-43 (new)** -- Impossibility argument basis clause independence: extracted from V-02/V-04/
  V-05 Round 13 structural excellence (Gate 1 CLOSE splits required-basis and prohibited-basis
  verification into two independent checkboxes). C-41 requires both basis types named in the same
  postcondition; C-43 requires them as structurally independent items. V-01's combined statement
  "(architecture basis, not description absence)" satisfies C-41 but not C-43. The independence
  matters because required-basis and prohibited-basis are logically independent conditions that can
  fail separately. Cracked by V-02, V-04, V-05.
- **C-44 (new)** -- Bidirectional gap registry artifact structure: extracted from V-03/V-05 Round
  13 structural excellence (formal PART A GAP REGISTRY and PART B GAP REGISTRY sections with
  structured three-field entries: Source / Missing link / Consequence). C-38 requires named gap
  findings; C-44 requires each finding to be a three-field registry artifact in a named section.
  Inline notation (V-01/V-02/V-04) names the problem but not the consequence; the formal registry
  makes gap severity independently auditable and supports registry-level queries. Cracked by
  V-03, V-05.
- **V-05 achieves 72/72** -- first perfect uncapped aspirational score across all rounds. All
  three structural independence/registry patterns converge in V-05: two-checkbox Gate 2b CLOSE
  (C-42), two-checkbox Gate 1 CLOSE (C-43), and formal three-field gap registries (C-44). No
  fully uncracked criteria remain.
- **Aspirational cap unchanged** at 10; uncapped maximum rises from 66 to 72 (36 criteria x
  PASS=2).

**v13 changes from v12:**

- **C-39 (new)** -- Gate-open precondition acknowledgment checkpoint: extracted from V-02/V-04
  Round 12 structural excellence (Gate 2b OPEN precondition carries explicit identity assertion
  acknowledgment with "verbatim -- not a derivative" confirmation before any chaos row filling
  begins). C-18 requires named entry conditions (prior gate closure); C-31 requires the bypass
  protocol declared upfront; C-39 requires a named constraint to be actively confirmed at gate-
  entry time -- these three criteria are orthogonal. V-02 uses the `[ ]` checkbox form; V-04/V-05
  use named prose acknowledgment in the Gate OPEN position -- both satisfy the checkpoint pattern.
  V-01/V-03 carry copy instructions rather than confirmable checkpoints, scoring FAIL. Cracked by
  V-02, V-04, V-05.
- **C-40 (new)** -- Gate-close prohibition clause: extracted from V-02/V-04 Round 12 structural
  excellence (Gate 2b CLOSE: "identity assertion satisfied -- no paraphrase, no independent
  calibration"). Standard CLOSE conditions verify presence; a prohibition clause explicitly
  verifies absence of a named failure mode. V-05's CLOSE confirms "(identity assertion satisfied)"
  without a prohibition clause -- satisfying C-36 (PASS) but scoring PARTIAL for C-40,
  demonstrating the two components are independently load-bearing. V-01/V-03 carry presence-only
  CLOSE conditions, scoring FAIL. Cracked by V-02, V-04.
- **C-41 (new)** -- Impossibility argument quality gate postcondition: extracted from V-01/V-05
  Round 12 structural excellence (Gate 1 CLOSE postcondition: "Every Argued-Impossible has DS
  Primitive cited: field completed (architecture basis, not description absence)"). C-15 requires
  the DS Primitive cited field and VALID/INVALID examples; C-41 requires the Gate 1 CLOSE to name
  the prohibited basis type -- closing the gap where a description-absence argument passes a
  presence-only CLOSE check. V-02/V-03/V-04 carry advisory prose without a Gate 1 quality
  postcondition, scoring FAIL. Cracked by V-01, V-05. Also resolves the persistent C-15 PARTIAL
  block: with the Gate 1 quality postcondition in place, V-01 and V-05 achieve C-15 PASS in R12,
  closing the last criterion that had been uncracked across all prior rounds.
- **Aspirational cap unchanged** at 10; uncapped maximum rises from 60 to 66 (33 criteria x
  PASS=2). V-05 is the new uncapped ceiling at 65/66 (C-40 PARTIAL). Open for R13: C-40 PASS for
  V-05; C-38 PASS for V-01/V-02/V-03/V-04; C-15/C-41 PASS for V-02/V-03/V-04. No fully
  uncracked criteria remain.

**v12 changes from v11:**

- **C-36 (new)** -- Chaos-trigger threshold identity assertion: extracted from V-05 Round 11.
  Cracked by V-05 only; V-01/V-03/V-04 score PARTIAL.
- **C-37 (new)** -- Observable signal detection horizon: extracted from V-04/V-05 Round 11.
  Cracked by V-04 and V-05.
- **C-38 (new)** -- Chaos-observability bidirectional coverage matrix: extracted from V-05 Round
  11. Cracked by V-05 only; V-04 scores FAIL despite having both parent outputs.
- **Aspirational cap unchanged** at 10; uncapped maximum rises from 54 to 60 (30 criteria x
  PASS=2).

**v11 changes from v10:**

- **C-33 (new)** -- Intra-row column-group phase gate: extracted from V-01/V-04/V-05 Round 10.
- **C-34 (new)** -- Trigger condition column: threshold expression + detection signal: extracted
  from V-02/V-05 Round 10.
- **C-35 (new)** -- Three-component recovery stage specification: extracted from V-03/V-04/V-05
  Round 10.
- **Aspirational cap unchanged** at 10; uncapped maximum rises from 48 to 54 (27 criteria x
  PASS=2).

**v10 changes from v9:**

- **C-31 (new)** -- Pre-analysis bypass chain declaration: extracted from V-01 Round 9.
- **C-32 (new)** -- Bypass-trigger column scanability: extracted from V-02/V-05 Round 9.
- **Aspirational cap unchanged** at 10; uncapped maximum rises from 44 to 48 (24 criteria x
  PASS=2).

**v9 changes from v8:**

- **C-29 (new)** -- Rule-bypass-triggered gate reopening.
- **C-30 (new)** -- Multi-act completion sign-off.
- **Aspirational cap unchanged** at 10; uncapped maximum rises from 40 to 44 (22 criteria x
  PASS=2).

**v8 changes from v7:**

- **C-28 (new)** -- Post-analysis rule registry audit.
- **Aspirational cap unchanged** at 10; uncapped maximum rises from 38 to 40 (20 criteria x
  PASS=2).

**v7 changes from v6:**

- **C-25 (new)** -- Nil-finding supersession protocol.
- **C-26 (new)** -- Confidence triage resolution sub-gate.
- **C-27 (new)** -- Named rule block registry.
- **Aspirational cap unchanged** at 10; uncapped maximum rose from 32 to 38.

**v6 changes from v5:**

- **C-22 (new)** -- Typed nil-finding identifiers.
- **C-23 (new)** -- Scope declaration closure bracket.
- **C-24 (new)** -- Template-embedded conditional linkage rules.
- **Aspirational cap unchanged** at 10; uncapped maximum rose from 26 to 32.

**v5 changes from v4:**

- **C-19 (new)** -- Gate blockage transparency (Reason-if-OPEN).
- **C-20 (new)** -- Downstream gate amendment with re-close record.
- **C-21 (new)** -- Pre-analysis commerce operation scope declaration.
- **Aspirational cap unchanged** at 10; uncapped maximum rose from 20 to 26.

**v4 changes from v3:**

- **C-16 (new)** -- Named gate-state vocabulary.
- **C-17 (new)** -- Permanently barred entries as named coverage gaps.
- **C-18 (new)** -- Explicit phase entry and exit conditions.
- **C-15 strengthened** -- Pass condition now requires named "DS Primitive cited:" field with
  inline VALID/INVALID annotated examples.
- **Aspirational cap unchanged** at 10; uncapped maximum rose from 14 to 20.

**v3 changes from v2:**

- **C-14 (new)** -- Conflict-resolution adequacy as DCV source.
- **C-15 (new)** -- DS-primitive-grounded impossibility arguments.
- **C-11 strengthened** -- Low-confidence entries barred (not merely flagged).
- **C-12 strengthened** -- Nil findings require scope rationale.
- **Aspirational scoring**: PASS=2, PARTIAL=1, FAIL=0 per criterion. Band capped at 10.
  Uncapped max 14 across 7 criteria.

**v2 changes from v1:**

- **C-11 (new)** -- Confidence-annotated discovery catalog.
- **C-12 (new)** -- Nil-finding norm for gap sections.
- **C-13 (new)** -- Coverage accountability roster.
- **Aspirational scoring rebalanced**: C-09 and C-10 reduced from PASS=5 to PASS=2 to accommodate
  the growing aspirational tier without changing the band cap.
