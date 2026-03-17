Written to `simulations/quest/rubrics/flow-resilience-rubric-v11-2026-03-15.md`.

---

## v11 summary

Three new aspirational criteria added from Round 10 excellence signals:

| Criterion | E-tag | Source | Cracked by |
|-----------|-------|--------|------------|
| **C-33** -- Intra-Row Column-Group Phase Gate | E-19 | V-01/V-04/V-05: "C-phase complete before D-phase begins" advance-inhibitor embedded in each row descriptor | V-01, V-04, V-05 |
| **C-34** -- Trigger Condition Column: Threshold Expression + Detection Signal | E-20 | V-02/V-05: Trigger Condition column with both a quantified activation threshold and a named detection signal, operationalizable for alerting by column scan | V-02, V-05 |
| **C-35** -- Three-Component Recovery Stage Specification | E-21 | V-03/V-04/V-05: Recovery Path extended to mechanism + SLA target + Verification Signal (named observable artifact) per stage, making each stage independently falsifiable | V-03, V-04, V-05 |

**Scoring delta**: aspirational cap unchanged at 10; uncapped max 48 → 54 (27 criteria × 2).

**R10 discrimination under v11** (all weighted composites still 100/100; tiebreak by uncapped aspirational):
- V-05: 50/54 (new ceiling)
- V-04: 47/54
- V-01: 46/54
- V-02, V-03: 45/54 (tied)

Open for R11: none — all three new criteria cracked by R10 V-05.
e mechanism confirming threshold crossing).
- The gap it closes: the scenario's activation boundary must be operationalizable for
  alerting from column scan alone -- an analyst can wire a monitoring alert directly from
  Trigger Condition cells without reading scenario prose. A qualitative trigger description
  cannot be wired to an alert system; a threshold expression without a detection signal
  cannot confirm when the threshold is crossed in production. Both components are
  independently load-bearing.
- Pass requires: dedicated Trigger Condition column with Fill Requirement naming both
  components; at least one row fills both with non-generic content.

**C-35 -- Three-Component Recovery Stage Specification (E-21)**
- Signal: V-03/V-04/V-05's Recovery Path column extension to three required components per
  stage: mechanism + SLA target + Verification Signal (VS). The VS is a named observable
  artifact confirming stage completion independent of SLA elapse (e.g., "inventory-service
  heartbeat returns 200", "payment provider ACK logged to audit trail").
- The gap it closes: C-07 (recommended) requires actor-labeled recovery steps; C-35 requires
  each stage to be independently falsifiable -- the stage is complete when the named
  observable appears, not when the SLA timer expires. SLA elapse records duration; the VS
  confirms outcome. A recovery path providing mechanism and SLA without a VS cannot be
  operationally verified at stage granularity.
- Pass requires: all three components (mechanism, SLA target, named VS) explicitly required
  for each of the four stages in the column specification or row descriptor; VS must be
  named (not generic), observable (system state / log / metric / response code), and
  distinct from the mechanism.

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

Open for R11: none -- all three new criteria cracked by R10 V-05. Persistent uncracked
block: C-09 and C-10 (chaos engineering, observability hooks -- unaddressed across all
rounds).

---

## v10 changes from v9

Two new aspirational criteria extracted from Round 9 excellence signals:

**C-31 -- Pre-Analysis Bypass Chain Declaration**
- Signal: V-01's named "Bypass Gate-Reopening Protocol (DS Expert Authority)" section
  declared *before Gate 1*, not reactively when a bypass is first detected.
- The gap it closes: C-29 requires the bypass chain to execute correctly; C-31 requires the
  chain's structure to be declared upfront -- analogous to C-21 (scope declaration precedes
  analysis). Without it, the bypass protocol is unverifiable until first invocation.
- Pass requires all four elements: numbered remediation steps / amendment sub-gate
  convention / authorized actors / COMPLETE-blocking statement.

**C-32 -- Bypass-Trigger Column Scanability**
- Signal: V-02/V-05's BYPASS-TRIGGER column in the registry audit table -- each cell must
  be a trigger citation or explicit N/A/SCENARIO-ABSENT, never blank.
- The gap it closes: C-28 requires invocation completeness in prose; C-32 requires bypass
  detection to be *column-scannable* independent of prose traversal -- orthogonal audit path
  on the same data. Blank cells are invalid because they conflate "trigger never arose" with
  "trigger unrecorded."
- Incentivizes table-structured registry audits; analyses with prose-only audits score FAIL.

**Scoring delta**: aspirational cap unchanged at 10; uncapped max rises from 44 -> 48
(24 criteria x 2).

---

## Essential Criteria (must pass all -- 60% of score)

### C-01 -- Scenario Coverage
- **Weight**: essential
- **Category**: coverage
- **Text**: The output covers all three resilience scenario classes: (1) full connectivity
  loss (client offline), (2) partial failure (dependent service unavailable), and (3)
  concurrent writes across a partition (split-brain / eventual-consistency conflict).
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
  non-trivial content (not placeholder, "N/A", or a single word). A scenario missing any
  field fails this criterion entirely.

### C-03 -- Gap Identification (Three Types)
- **Weight**: essential
- **Category**: correctness
- **Text**: The output identifies at least one offline experience gap, at least one data
  consistency violation, and at least one missing recovery flow as distinct named findings.
  These are the three explicit output targets the skill defines.
- **Pass condition**: All three finding types appear, each labeled and actionable -- not
  merely implied or bundled. Generic statements like "offline support may be limited"
  without specificity fail.

### C-04 -- Distributed Systems Accuracy
- **Weight**: essential
- **Category**: correctness
- **Text**: Technical claims about failure modes are consistent with distributed systems
  fundamentals. CAP theorem trade-offs, retry semantics, idempotency requirements, and
  conflict-resolution strategies are used correctly wherever referenced.
- **Pass condition**: No materially incorrect distributed-systems claim is present.
  Fabricated error codes, invented protocols, or impossible consistency guarantees (e.g.,
  strong consistency with no latency cost across a partition) fail this criterion.

### C-05 -- Commerce Domain Grounding
- **Weight**: essential
- **Category**: depth
- **Text**: The analysis is grounded in the commerce / distributed systems domain. Failure
  scenarios reference realistic commerce flows -- checkout, inventory reservation, payment
  processing, order fulfillment, cart state -- rather than generic CRUD operations.
- **Pass condition**: At least two scenarios are anchored to a recognizable commerce
  operation by name. Purely abstract or domain-agnostic scenarios fail.

---

## Recommended Criteria (improve output quality -- 30% of score)

### C-06 -- Severity and Blast Radius Classification
- **Weight**: recommended
- **Category**: depth
- **Text**: Each failure scenario is annotated with a severity level (e.g., degraded /
  impaired / down) and a blast radius describing what fraction or segment of users is
  affected. These labels enable triage prioritization.
- **Pass condition**: At least half of the scenarios carry both a severity label and a
  blast-radius estimate or qualifier (e.g., "affects all users in offline mode", "affects
  <1% under split-brain"). Scenarios with severity but no blast radius, or vice versa, do
  not satisfy this criterion.

### C-07 -- Recovery Path Specificity with Actor Labels
- **Weight**: recommended
- **Category**: depth
- **Text**: Recovery paths describe concrete steps or system behaviors -- not just outcomes.
  Each step names who or what initiates the action: client, server, operator, or user.
  Example: "Client retries with exponential back-off up to 5 attempts; on exhaustion,
  server surfaces a manual reconcile UI to the user."
- **Pass condition**: At least two recovery paths include actor-labeled steps. Paths that
  describe only the end state ("system recovers", "data is synchronized") without mechanism
  fail.

### C-08 -- Conflict Resolution Strategy for Eventual Consistency
- **Weight**: recommended
- **Category**: coverage
- **Text**: For eventual-consistency scenarios, the output specifies what conflict resolution
  strategy is assumed (last-write-wins, merge, manual reconcile, reject-stale) and flags
  whether that strategy is adequate for the data type involved (e.g., LWW is inadequate for
  inventory counts).
- **Pass condition**: At least one eventual-consistency scenario names a conflict-resolution
  strategy and includes a brief adequacy judgment. Scenarios that describe lag or divergence
  without naming a resolution strategy fail.

---

## Aspirational Criteria (raise the bar -- 10% of score)

**Scoring**: PASS=2, PARTIAL=1, FAIL=0 per criterion. Aspirational band capped at 10.
Uncapped maximum across 27 criteria is 54; the cap rewards breadth while holding the
composite ceiling at 100.

### C-09 -- Chaos Engineering Test Cases
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The output includes one or more concrete chaos-engineering test scenarios that
  could be scheduled in a test harness. Each scenario specifies: (1) what to inject (network
  partition, latency spike, service kill, packet loss), (2) expected observable behavior,
  and (3) a binary pass/fail signal.
- **Pass condition**: At least one runnable chaos scenario is present with all three
  elements. Vague suggestions to "test resilience" or "add chaos testing" without specifics
  fail.
- **Partial**: Chaos scenario present but missing one of the three required elements.
- **Fail**: No chaos engineering content, or suggestions without runnable specifics.

### C-10 -- Observability Hooks Tied to Named Gaps
- **Weight**: aspirational
- **Category**: depth
- **Text**: The output recommends specific observability signals -- metrics, logs, traces,
  or alerts -- that would surface each identified gap in production. Each recommendation is
  tied to a specific named gap or scenario from the analysis with a rationale.
- **Pass condition**: At least two observability recommendations are present, each linked to
  a named gap or scenario with a rationale for why that signal would detect the failure
  early. Generic "add monitoring" suggestions without specifics fail.
- **Partial**: Observability recommendations present but fewer than two are tied to named
  gaps with rationale.
- **Fail**: No observability content, or generic recommendations without gap linkage.

### C-11 -- Confidence-Annotated Discovery Catalog
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The distributed-systems analysis phase carries explicit confidence ratings
  (high / medium / low / impossible) for each failure mode before scenarios are committed to
  the output. Each rating cites its basis -- an architecture constraint or DS theory
  reference -- not just a label. Entries rated "impossible" are excluded from the scenario
  table but retained in the discovery phase with their rationale. Entries rated "low
  confidence" are barred from the scenario table until the confidence basis is resolved;
  flagging alone does not satisfy this gate. This triage gate prevents technically invalid
  scenarios from polluting the output and makes the discovery phase independently auditable.
  (Signal: V-01, V-04.)
- **Pass condition**: Every failure mode in the discovery phase carries a confidence rating
  with a cited basis; "impossible" entries are excluded from the table with retained
  rationale; "low confidence" entries are barred from the table until resolved -- not merely
  flagged.
- **Partial**: Confidence ratings present on some entries but not all; or impossible entries
  excluded without cited basis; or low-confidence entries flagged but not gated.
- **Fail**: No confidence annotation on discovery-phase entries; impossible scenarios enter
  the output without challenge.

### C-12 -- Nil-Finding Norm for Gap Sections
- **Weight**: aspirational
- **Category**: coverage
- **Text**: Each of the three typed gap sections (offline experience gaps / data consistency
  violations / missing recovery flows) includes an explicit nil finding when no gaps of that
  type are identified for the given topology or load pattern. A nil finding reads as: "No
  offline-experience gaps identified for this deployment pattern -- all critical paths
  include local-fallback state." The nil finding includes a scope rationale explaining why
  the gap type does not apply; a bare "none found" statement does not satisfy this criterion.
  Silence is not a valid nil finding. (Signal: V-01, V-02, V-03.)
- **Pass condition**: All three gap sections are explicitly present; sections with no
  findings carry a labeled nil finding that includes a brief scope rationale explaining why
  the gap type does not apply for this deployment pattern.
- **Partial**: Some nil findings present but not all three sections covered, or nil findings
  appear without scope rationale (bare "none found" statement).
- **Fail**: Missing gap sections are silently absent; reader cannot distinguish "no gaps
  found" from "gaps not analyzed."

### C-13 -- Coverage Accountability Roster
- **Weight**: aspirational
- **Category**: coverage
- **Text**: The output opens with a pre-analysis roster that commits to minimum per-class
  coverage -- at least two scenarios per degradation class -- before scenario analysis
  begins. The roster is checkable: the reader can verify class coverage against the final
  scenario list without reading the full analysis. When a class slot cannot be filled, the
  output provides an explicit impossibility argument or reclassification -- it does not
  silently reduce coverage below the committed minimum. The challenge mechanism ("why can't
  you fill this slot?") is answered inline, not omitted. (Signal: V-03, V-05.)
- **Pass condition**: Pre-analysis roster is present and commits to >=2 scenarios per class;
  all committed slots are filled or explicitly argued impossible / reclassified; roster is
  independently checkable against the final scenario list.
- **Partial**: Roster present but commits to fewer than 2 per class without argument; or
  roster absent but coverage gaps are argued inline rather than silently dropped.
- **Fail**: No coverage accountability mechanism; degradation-class gaps are silently absent.

### C-14 -- Conflict-Resolution Adequacy as DCV Source
- **Weight**: aspirational
- **Category**: correctness
- **Text**: When conflict-resolution analysis judges a strategy to be inadequate or undefined
  for a given data type, that judgment is explicitly fed back into the data-consistency-
  violation (DCV) gap section as a named DCV finding. The conflict-resolution section and
  the gap identification section are bidirectionally linked -- an inadequate or undefined
  strategy is always a DCV, not a standalone note. This prevents conflict-resolution
  weaknesses from being isolated in one section and invisible to the gap tally. When all
  strategies are adequate, an explicit CLOSED confirmation is written. (Signal: V-02, V-04
  -- "inadequate/undefined -> DCV" pattern.)
- **Pass condition**: At least one conflict-resolution adequacy judgment of "inadequate" or
  "undefined" generates an explicit, named DCV entry in the gap identification section. The
  linkage is visible: the DCV entry references the conflict-resolution finding that produced
  it. When no inadequate strategies exist, an explicit CLOSED confirmation is present.
- **Partial**: Inadequate strategies noted in conflict-resolution analysis but not linked to
  a named DCV finding in the gap section; or a DCV entry is present without tracing back to
  its conflict-resolution source.
- **Fail**: Conflict-resolution analysis and gap sections are independent silos with no
  cross-referencing; inadequate strategies do not produce DCV entries.

### C-15 -- DS-Primitive-Grounded Impossibility Arguments
- **Weight**: aspirational
- **Category**: correctness
- **Text**: When a coverage slot in the accountability roster cannot be filled, the
  impossibility argument cites a specific distributed systems primitive -- a named CAP
  theorem guarantee, a deployment topology constraint, or a synchronous consistency
  guarantee that forecloses the failure class. Topic-scope arguments ("the topic doesn't
  mention caching", "the system description is too simple for this class") are not valid
  impossibility arguments. The argument must address the architecture, not the description.
  The template includes a named "DS Primitive cited:" field with inline VALID / INVALID
  annotated examples so that the distinction between an architecture argument and description
  absence is unambiguous. (Signal: V-03 Round 2; V-02 Round 3.)
- **Pass condition**: Every impossibility argument cites a specific DS primitive via a named
  "DS Primitive cited:" field with an architecture basis. Inline VALID/INVALID annotated
  examples are present in the template. No topic-scope arguments appear; any argument
  invoking description absence rather than architecture constraint fails.
- **Partial**: Some impossibility arguments cite DS primitives but others rely on topic
  scope or description absence; or DS primitive field is present but lacks inline
  VALID/INVALID examples.
- **Fail**: Impossibility arguments rely solely on topic scope or description absence; no
  DS primitive is cited; or the challenge mechanism is absent entirely.

### C-16 -- Named Gate-State Vocabulary
- **Weight**: aspirational
- **Category**: format
- **Text**: The confidence triage and gap sections use a fixed, named disposition vocabulary
  -- entries are assigned exactly one of: Include / BARRED / Argued-Impossible (or
  equivalent named states). Free-text confidence descriptions that do not resolve to one of
  these named dispositions are not valid. Each gate section carries an explicit binary
  OPEN / CLOSED declaration visible without reading the prose. "Flagged" and similar
  qualitative labels that do not resolve to a named disposition are rejected -- a gate
  section without a named OPEN/CLOSED state is treated as OPEN by definition. A gate cannot
  close while any entry in that section carries an unresolved disposition. (Signal: V-02
  C-11; V-03 C-11.)
- **Pass condition**: Every entry in the discovery/triage phase carries one of the named
  dispositions; each gate section displays an explicit OPEN/CLOSED state; no free-text
  confidence label is used as a substitute for a named disposition.
- **Partial**: Named dispositions used for most but not all entries; or OPEN/CLOSED gate
  states present for some sections but not all.
- **Fail**: Discovery entries use free-text confidence descriptions without named
  dispositions; no gate sections carry an explicit OPEN/CLOSED state.

### C-17 -- Permanently Barred Entries as Named Coverage Gaps
- **Weight**: aspirational
- **Category**: coverage
- **Text**: Discovery entries that remain BARRED after the confidence triage gate closes --
  where the low-confidence basis was never resolved -- are not silently dropped from the
  output. They are recorded as named coverage gaps in the coverage accountability register,
  distinguishing "analyzed, barred, recorded" from "not analyzed." An unresolved BARRED
  entry that produces no downstream artifact is invisible to the reader; "analyzed and
  excluded for architectural reasons" (Argued-Impossible) and "analyzed but confidence
  never confirmed" (permanently BARRED) are not equivalent and must not be conflated.
  (Signal: V-02 C-11.)
- **Pass condition**: Any entry that is BARRED at the close of the triage gate and whose
  confidence basis was never resolved appears as a named coverage gap in the accountability
  register. No BARRED entry silently disappears from the analysis trace.
- **Partial**: Permanently barred entries noted in prose as unresolved but not formally
  recorded as named coverage gaps in the accountability register.
- **Fail**: BARRED entries with unresolved bases are silently dropped; the reader cannot
  determine whether low-confidence failure modes were excluded intentionally or omitted.

### C-18 -- Explicit Phase Entry and Exit Conditions
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Each analysis phase or gate section specifies (1) its entry condition -- which
  prior gates must be CLOSED before this phase begins, referenced by gate identifier -- and
  (2) its exit condition -- what must be true for this gate to be declared CLOSED, stated
  explicitly. Phases that begin or end without stated conditions are implicitly sequential-
  by-position, which is unverifiable. Silence does not mean CLOSED; an explicit CLOSED
  confirmation is required. This prevents phases from running out of order and makes the
  analysis closure independently auditable. (Signal: V-03 C-14.)
- **Pass condition**: At least two phases carry named entry conditions (citing prior gate
  identifiers) and named exit conditions; each of those phases closes with an explicit
  CLOSED confirmation statement.
- **Partial**: Entry or exit conditions present on some phases but not all; or conditions
  stated but without gate-identifier references; or no explicit CLOSED confirmations.
- **Fail**: No phase carries stated entry/exit conditions; phases are ordered by prose
  position only; closure is inferred, not declared.

### C-19 -- Gate Blockage Transparency (Reason-if-OPEN)
- **Weight**: aspirational
- **Category**: format
- **Text**: When a gate is in OPEN state -- not yet closed -- the blocking reason is declared
  inline as a named "Reason if OPEN:" field or equivalent. An OPEN gate with no stated
  reason is indistinguishable from a gate that was never evaluated or was abandoned
  mid-analysis. The reason field must name the specific blocking condition: the unresolved
  entry ID, the unmet coverage minimum, the pending adequacy verdict, or the outstanding
  amendment. This allows the analysis to be resumed deterministically once the blocking
  condition is resolved, without re-reading all prior gate prose. A gate displaying only
  "OPEN" without a blocking reason is treated as an error, not as a valid in-progress state.
  (Signal: V-03 Round 4 C-18.)
- **Pass condition**: Every gate that appears in OPEN state carries an explicit "Reason if
  OPEN:" field identifying the specific blocking condition. CLOSED gates do not require a
  reason field. Any OPEN gate lacking a stated reason fails this criterion.
- **Partial**: Some OPEN gates carry stated blocking reasons but not all; or blocking reason
  present but identifies only a category ("unresolved entry") without naming the specific
  blocking item.
- **Fail**: OPEN gates carry no stated reason; or all OPEN gates are declared without
  distinguishing the blocking condition from a routine in-progress state.

### C-20 -- Downstream Gate Amendment with Re-Close Record
- **Weight**: aspirational
- **Category**: correctness
- **Text**: When a downstream finding invalidates the output of an already-CLOSED gate
  (e.g., a conflict-resolution adequacy failure requires an additional DCV entry that the
  prior DCV gate was closed without), the prior gate is explicitly re-opened, the amendment
  is applied, and the gate is re-closed under a labeled amendment sub-gate (e.g., "GATE 3b:
  AMENDED"). The amendment record names the downstream finding that triggered the reopening.
  Late amendments silently appended to a closed section are unverifiable and break the gate
  audit trail. A re-opened gate whose amendment is applied without a labeled re-close record
  is treated as still OPEN. (Signal: V-03 Round 4 C-14.)
- **Pass condition**: At least one downstream finding that requires an amendment to a prior
  CLOSED gate triggers an explicit re-open, applies the amendment, and re-closes the gate
  under a labeled sub-gate identifier. The amendment record references the downstream
  finding by ID. When no downstream findings require amendments, an explicit confirmation
  is present.
- **Partial**: Late amendment applied to a prior closed gate section but without a labeled
  re-open / re-close record; or sub-gate label present but the downstream finding that
  triggered it is not referenced.
- **Fail**: Downstream findings that invalidate prior gate outputs are silently appended
  without re-opening the gate; or no mechanism exists for downstream findings to amend
  prior gate sections; or the gate audit trail has no sub-gate amendment records.

### C-21 -- Pre-Analysis Commerce Operation Scope Declaration
- **Weight**: aspirational
- **Category**: coverage
- **Text**: Before scenario analysis begins, the output commits to a named, exhaustive list
  of commerce operations that will be analyzed. The declaration names every operation in
  scope (e.g., checkout, inventory reservation, payment processing, cart state, order
  fulfillment, loyalty redemption). This commitment is checkable against the final scenario
  table: any declared operation that receives no scenario coverage is a named gap, not a
  silent omission. Operations excluded from the declaration are either explicitly
  out-of-scope with a stated reason or their absence is a coverage gap. C-05 requires
  scenarios to be anchored to named operations; C-21 requires the scope commitment to
  precede the analysis, not emerge from it. (Signal: V-05 Round 4 C-05.)
- **Pass condition**: A named commerce operation scope list is present before the first
  scenario entry. The list covers at least four distinct operations. The final scenario
  table provides coverage for each declared operation or explicitly records it as a gap.
  Operations mentioned only within scenario bodies (not declared upfront) do not satisfy
  this criterion.
- **Partial**: Upfront scope declaration present but covers fewer than four operations; or
  declaration present but final coverage is not cross-checked against the declared list; or
  operations appear only in a post-hoc summary, not a pre-analysis commitment.
- **Fail**: No upfront commerce operation scope declaration; the set of covered operations
  is inferred from the scenario table only; coverage gaps are not distinguishable from
  scope exclusions.

### C-22 -- Typed Nil-Finding Identifiers
- **Weight**: aspirational
- **Category**: format
- **Text**: Nil findings carry gap-type prefix identifiers -- OEG-NIL (offline experience
  gap), DCV-NIL (data consistency violation), MRF-NIL (missing recovery flow) -- that bind
  each nil statement to its gap category by name. C-12 requires nil findings with scope
  rationale; C-22 requires those nil findings to be addressable by type. A nil statement
  without a typed identifier satisfies C-12 but cannot be audited, queried, or cross-
  referenced by gap type. Each typed nil identifier is unique within an analysis run; if
  the same gap type produces a nil in multiple phases, each carries its own identifier
  (OEG-NIL-1, OEG-NIL-2). (Signal: V-01 Round 5 C-12 PASS evidence.)
- **Pass condition**: Every nil finding carries a typed prefix identifier (OEG-NIL, DCV-NIL,
  MRF-NIL, or equivalent named type prefix). Each identifier is unique within the run.
  Nil statements without a typed identifier fail this criterion regardless of rationale
  quality.
- **Partial**: Typed identifiers present on some nil findings but not all; or typed prefix
  used but not consistently bound to the gap type.
- **Fail**: No typed nil-finding identifiers; nil statements use only prose headings or bare
  "none found" / "N/A" markers; nil findings are not queryable by gap type.

### C-23 -- Scope Declaration Closure Bracket
- **Weight**: aspirational
- **Category**: format
- **Text**: The pre-analysis commerce operation scope declaration (C-21) is bracketed by two
  named boundary blocks: an opening `SCOPE DECLARATION COMPLETE` confirmation that closes
  the declaration phase before analysis begins, and a terminal `Scope Verification` block
  that cross-checks the declared operation list against the final scenario table after
  analysis concludes. The terminal Scope Verification block must name each declared
  operation and its coverage outcome (covered / gap / out-of-scope). A scope declaration
  that opens but never formally closes is treated as unverified. (Signal: V-01 Round 5
  C-21 PASS evidence.)
- **Pass condition**: An opening `SCOPE DECLARATION COMPLETE` block (or named equivalent)
  is present immediately after the operation list, before the first analysis phase. A
  terminal `Scope Verification` block (or named equivalent) is present after the final
  analysis phase, naming each declared operation with its coverage outcome. Both blocks are
  required; a declaration with only one does not satisfy this criterion.
- **Partial**: Opening declaration confirmation present but no terminal verification block;
  or terminal block present but coverage outcomes are not named per declared operation.
- **Fail**: No named boundary blocks; scope declaration embedded in prose with no opening
  confirmation; terminal cross-check absent or inferred from scenario table without a named
  block.

### C-24 -- Template-Embedded Conditional Linkage Rules
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Cross-section linkages that are required by the skill's logic are encoded in the
  template as explicit named conditional rules -- `if [condition]: [action]` -- rather than
  described in prose instructions or left to analyst discretion. The canonical example is
  the DCV linkage from conflict-resolution adequacy: rather than instructing the analyst to
  "link inadequate strategies to DCV findings," the template contains a named rule: `if
  verdict is [no | undefined]: append DCV-CR-NN`. This makes correct cross-section behavior
  mandatory and machine-checkable. C-14 requires the DCV linkage to exist; C-24 requires it
  to be encoded as a named conditional rule. At least two distinct conditional linkage rules
  must be present to demonstrate that the pattern is systemic, not incidental. (Signal:
  V-01 Round 5 C-14 PASS evidence.)
- **Pass condition**: At least two named conditional linkage rules are present in the
  template in explicit `if [condition]: [action]` form (or a structurally equivalent named
  rule block). Each rule names both its trigger condition and its cross-section action.
  Prose instructions that describe the same logic without an explicit conditional rule form
  do not satisfy this criterion.
- **Partial**: One conditional linkage rule present but not two; or rules present in
  conditional form but trigger conditions are underspecified; or rules embedded in prose
  annotations rather than named rule blocks.
- **Fail**: No conditional linkage rules in the template; cross-section linkages are
  described in prose instructions only; correct behavior depends on analyst discretion.

### C-25 -- Nil-Finding Supersession Protocol
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Typed nil-finding identifiers (C-22) have a two-state lifecycle: ACTIVE (nil
  declared, gap type not present) and SUPERSEDED (downstream analysis subsequently
  identifies a gap in the same category). When a downstream phase produces a gap finding
  that supersedes a previously declared nil, the nil identifier is explicitly annotated
  SUPERSEDED with a cross-reference to the finding ID that replaced it (e.g., "OEG-NIL-1:
  SUPERSEDED by OEG-F-3"). When no nil findings are superseded, an explicit "no
  supersessions" confirmation is present. (Signal: V-01 Round 6 C-22 PASS evidence.)
- **Pass condition**: At least one nil finding that is superseded by a downstream actual
  finding carries an explicit SUPERSEDED annotation citing the superseding finding ID. When
  no nil findings are superseded during the analysis run, an explicit "no supersessions"
  confirmation is present. A nil ID and a gap finding of the same type coexisting without a
  SUPERSEDED annotation on the nil fails this criterion.
- **Partial**: Supersession notation present on superseded nils but does not cite the
  superseding finding ID; or SUPERSEDED present on some superseded nils but not all; or
  "no supersessions" confirmation absent when no supersessions occur.
- **Fail**: Superseded nil findings carry no SUPERSEDED marker; nil identifiers are treated
  as write-once with no lifecycle tracking.

### C-26 -- Confidence Triage Resolution Sub-Gate
- **Weight**: aspirational
- **Category**: correctness
- **Text**: When a BARRED discovery entry has its unresolved confidence basis subsequently
  satisfied during analysis and is upgraded to Include, the upgrade path is recorded under a
  labeled triage resolution sub-gate (e.g., "GATE 1b: RESOLVED"). The resolution sub-gate
  must name: the entry ID being resolved, the confidence basis that was satisfied and how,
  the new Include disposition, and the re-closed triage gate status. When no BARRED entries
  are resolved during analysis, an explicit "no BARRED-to-Include upgrades" confirmation is
  present. (Signal: V-03 Round 6 structural excellence.)
- **Pass condition**: At least one BARRED entry that is resolved to Include during analysis
  appears under a labeled triage resolution sub-gate naming the entry ID, the satisfied
  basis, and the new disposition, with the triage gate re-closed. When no BARRED entries
  are resolved during analysis, an explicit confirmation is present.
- **Partial**: BARRED-to-Include upgrade recorded in prose but without a labeled sub-gate;
  or sub-gate present but does not name the satisfied basis or the entry ID being resolved;
  or confirmation absent when no upgrades occur.
- **Fail**: BARRED entries silently appear in the scenario table as Include with no
  resolution record; no mechanism exists for BARRED entries to be explicitly resolved.

### C-27 -- Named Rule Block Registry
- **Weight**: aspirational
- **Category**: format
- **Text**: The named conditional linkage rules required by C-24 appear in a discrete, named
  rule registry section within the template -- not embedded inline in gate-section prose.
  Each rule in the registry carries a unique identifier (e.g., RULE-CR-DCV, RULE-SCOPE-GAP,
  RULE-NIL-SUPERSEDE) that makes it independently addressable: other gate sections can cite
  a rule by its ID rather than by prose location. A template where rules are correct in form
  (satisfying C-24) but scattered inline through gate prose satisfies C-24 but fails C-27:
  inline rules are not enumerable, not independently auditable, and cannot be cited by ID.
  (Signal: V-03 Round 6 structural excellence.)
- **Pass condition**: A named rule registry section is present listing all conditional
  linkage rules. Each rule carries a unique ID, explicit trigger condition, and named
  cross-section action target. Gate sections that invoke linkage behavior cite rules by
  their registry ID, not by restating the conditional logic inline. At least two rules with
  distinct IDs are present.
- **Partial**: Named rules present and correct in conditional form (satisfying C-24) but
  embedded inline in individual gate sections rather than in a discrete registry; or
  registry present but fewer than two rules carry unique IDs; or rules listed in the
  registry but gate sections restate the conditional logic inline.
- **Fail**: No named rule registry; all conditional linkage rules appear only as inline
  annotations within gate-section prose; the complete rule set cannot be enumerated without
  reading the full template.

### C-28 -- Post-Analysis Rule Registry Audit
- **Weight**: aspirational
- **Category**: correctness
- **Text**: A named rule registry (C-27) is a declaration; a post-analysis registry audit
  closes the loop by confirming which rules were actually invoked during the analysis run.
  After all analysis gates complete, the output includes a named post-analysis audit block
  that reviews the rule registry and reports: (1) which rules fired during the run, citing
  the specific gate and entry that triggered each invocation; (2) how many times each rule
  fired; and (3) whether any registered rules went uninvoked -- and if so, whether the
  condition was absent from the analysis (scenario-absent) or the condition arose but the
  rule was not applied (rule-bypassed, which is an audit failure). (Signal: V-03 Round 7
  structural excellence.)
- **Pass condition**: A named post-analysis audit block is present after all analysis gates
  complete. The block lists each registered rule by ID and reports its invocation status:
  fired (with gate and entry citation) or uninvoked (with scenario-absent or rule-bypassed
  classification). At least two registered rules are accounted for. A rule that is invoked
  but whose invocation is not cited by gate and entry fails this criterion.
- **Partial**: Post-analysis review of rule usage present but not as a named, discrete audit
  block; or block present but covers only some registered rules; or invocations listed
  without citing the triggering gate and entry.
- **Fail**: No post-analysis rule audit; the rule registry is treated as a declaration-only
  artifact with no execution verification.

### C-29 -- Rule-Bypass-Triggered Gate Reopening
- **Weight**: aspirational
- **Category**: correctness
- **Text**: C-28 classifies a registered rule as RULE-BYPASSED when its trigger condition
  arose during a gate but the rule was not applied -- an audit failure. C-29 enforces the
  consequence: a RULE-BYPASSED finding is a gate-reopening trigger, not merely a reported
  deficiency. Before the analysis can declare COMPLETE, the affected gate must be explicitly
  reopened, the bypassed rule applied, the gate re-closed under a labeled amendment sub-gate
  following the C-20 mechanism (e.g., "GATE N-bypass: AMENDED"), and the audit entry
  updated from RULE-BYPASSED to INVOKED. C-28 says what the audit reports; C-29 says what
  a RULE-BYPASSED finding forces. (Signal: V-01 Round 8 C-28 PASS evidence.)
- **Pass condition**: When the post-analysis audit produces at least one RULE-BYPASSED
  finding, an explicit gate-reopening chain follows: the affected gate is re-opened, the
  bypassed rule is applied, the gate is re-closed under a labeled amendment sub-gate citing
  the bypass finding ID, and the audit entry is updated to INVOKED before COMPLETE is
  declared. When no RULE-BYPASSED conditions exist in the run, an explicit confirmation is
  present. An analysis that acknowledges RULE-BYPASSED and declares COMPLETE without gate
  remediation fails this criterion.
- **Partial**: RULE-BYPASSED finding acknowledged and gate reopened but no amendment
  sub-gate label present; or gate re-closed without updating the audit entry to INVOKED; or
  no explicit confirmation when the run contains no bypasses.
- **Fail**: RULE-BYPASSED audit findings present with no gate reopening; analysis declares
  COMPLETE with acknowledged bypass failures unresolved.

### C-30 -- Multi-Act Completion Sign-Off
- **Weight**: aspirational
- **Category**: format
- **Text**: When the analysis is structured in two or more distinct named acts (e.g., Act 1
  -- DS failure mode analysis, Act 2 -- Commerce validation), the completion declaration
  requires a per-act sign-off for each act, not a single monolithic COMPLETE at the end.
  Each per-act sign-off declares: (1) all gates within that act are CLOSED; (2) the act's
  scope is exhausted; and (3) no RULE-BYPASSED conditions remain unresolved within that
  act. When the analysis is single-act, this criterion is scored N/A and treated as PARTIAL
  for scoring purposes. (Signal: V-01 Round 8 C-28 PASS evidence.)
- **Pass condition**: When the analysis has two or more named acts, each act closes with an
  explicit per-act sign-off block declaring all gates within that act CLOSED, scope
  exhausted, and no unresolved RULE-BYPASSED conditions in that act. The terminal COMPLETE
  then references the per-act sign-offs rather than implying gate closure directly. When
  the analysis is single-act, N/A must be explicitly declared.
- **Partial**: Per-act sign-offs present but missing one of the three required elements; or
  per-act sign-off present for some acts but not all; or analysis is single-act and N/A is
  explicitly declared.
- **Fail**: No per-act sign-offs in a multi-act analysis; terminal COMPLETE subsumes all
  acts without per-act gate closure records.

### C-31 -- Pre-Analysis Bypass Chain Declaration
- **Weight**: aspirational
- **Category**: format
- **Text**: The bypass remediation chain required by C-29 is declared as a named
  pre-analysis section before execution begins -- not reactively when a RULE-BYPASSED
  condition is first detected. The pre-analysis section enumerates: (1) the numbered steps
  of the bypass remediation chain (reopen gate, apply bypassed rule, re-close under
  amendment sub-gate, update audit entry to INVOKED); (2) the amendment sub-gate naming
  convention to be used (e.g., GATE N-bypass: AMENDED); (3) the actors authorized to
  execute each remediation step; and (4) the explicit blocking statement that COMPLETE may
  not be declared while any RULE-BYPASSED entry remains unresolved. C-29 requires the
  bypass chain to execute correctly when triggered; C-31 requires the chain's structure to
  be visible and independently auditable from the outset, before any bypass condition
  arises. (Signal: V-01 Round 9 C-29 PASS evidence.)
- **Pass condition**: A named pre-analysis bypass chain section (or equivalent named block)
  is present before the first analysis gate. The section enumerates the numbered
  remediation steps, names the amendment sub-gate convention, identifies authorized actors,
  and states the COMPLETE-blocking condition explicitly. The section must be pre-analysis
  (appearing before Gate 1), not embedded in a terminal block or post-analysis audit.
- **Partial**: Pre-analysis bypass section present but missing one of the four required
  elements (numbered steps / amendment convention / authorized actors / COMPLETE-blocking
  statement); or bypass chain described in preamble prose without a named section block;
  or section appears mid-analysis rather than before Gate 1.
- **Fail**: No pre-analysis bypass chain section; bypass remediation protocol appears only
  reactively at the point of first RULE-BYPASSED detection; the reader cannot verify the
  protocol's structure before encountering its first invocation.

### C-32 -- Bypass-Trigger Column Scanability
- **Weight**: aspirational
- **Category**: format
- **Text**: When the post-analysis registry audit is structured as a table, each registered
  rule carries a dedicated BYPASS-TRIGGER column. The BYPASS-TRIGGER cell for a given rule
  is either (1) non-empty, naming the gate and entry where the rule's trigger condition
  arose and the rule was not applied; or (2) explicitly marked N/A or SCENARIO-ABSENT,
  confirming that the rule's trigger condition never arose during the run. A blank cell is
  not a valid entry: blank does not distinguish "trigger condition never arose" from "trigger
  condition arose but was not recorded." The column enables horizontal scanability: a reader
  recovers all RULE-BYPASSED entries by scanning a single column, without reading gate
  prose. This is orthogonal to C-28's prose completeness requirement. (Signal: V-02/V-05
  Round 9 C-29 PASS evidence.)
- **Pass condition**: A BYPASS-TRIGGER column is present in the rule registry audit table.
  Every registered rule's cell in this column is either non-empty (citing gate and entry
  that triggered bypass detection) or explicitly marked N/A / SCENARIO-ABSENT. Blank cells
  fail this criterion regardless of correctness in other columns.
- **Partial**: BYPASS-TRIGGER column present but some cells are blank rather than explicitly
  confirmed N/A or SCENARIO-ABSENT; or column present but entries do not name the specific
  gate and entry that triggered bypass detection; or bypass detection information is
  presented in a separate prose block rather than a dedicated table column.
- **Fail**: No BYPASS-TRIGGER column in the registry audit table; bypass detection requires
  sequential gate-by-gate prose reading; or registry audit is not table-structured and no
  equivalent scannable column mechanism exists.

### C-33 -- Intra-Row Column-Group Phase Gate *(E-19)*
The scenario table columns are partitioned into ownership phases (e.g., C-phase: Commerce
Expert columns such as State and Capability; D-phase: Distributed Systems Expert columns
such as Data at Risk, Recovery Path, Severity, Blast Radius). Within each scenario row, an
advance-inhibitor embedded directly in the row descriptor prevents D-phase column
population from beginning until all C-phase columns in that row carry non-placeholder
content. This gate operates at a level below the slot (row) and above the individual
column -- closing the mid-row omission risk that row-level advance-inhibitors do not
address: the row-level gate fires after the row is complete; the column-group gate fires
before D-phase begins within the row. The gate must be embedded in the row descriptor at
slot level or below (not in preamble or a section-level note) to operate during cell
construction. The column-phase labels must be named explicitly; generic "complete all
columns before proceeding" instructions do not satisfy this criterion because they do not
name the within-row ownership boundary as a distinct gate. (Signal: V-01/V-04/V-05 Round
10 -- "C-phase complete? Do not begin D-phase columns until State and Capability contain
non-placeholder content" embedded in each row descriptor.)

**Pass condition**: The row descriptor for at least one scenario row contains an explicit
column-group phase gate naming the column ownership phases and requiring all C-phase (or
equivalent first-phase) column cells to carry non-placeholder content before any D-phase
column cell is begun. The gate is embedded inside the row descriptor (slot level or below),
not positioned above the table or in a section header. The phase label boundary must be
named. Per-row application is preferred; partial credit applies if the gate appears once as
a template instruction for all rows.

**Partial**: Column-group gate semantics present but embedded in preamble or section-level
note rather than a row descriptor; or gate embedded in a row descriptor but uses generic
"complete all columns" language without naming the column-phase boundary; or gate uses
named phases but is applied to only one row in a table where multiple rows require
phase-segregated columns.

**Fail**: No intra-row column-group phase gate anywhere in the prompt; within-row
ownership transitions have no advance-inhibitor at column-group granularity; the
progression from C-phase to D-phase columns within a row is ungated.

### C-34 -- Trigger Condition Column: Threshold Expression + Detection Signal *(E-20)*
The scenario table includes a Trigger Condition column (or equivalently named
entry-bounding column) whose Fill Requirement explicitly mandates two distinct components
per cell: (1) a threshold expression -- a quantified activation condition specifying when
the scenario becomes active (e.g., "inventory count falls below safety-stock threshold",
"payment API p99 latency exceeds 500ms"); and (2) a detection signal -- the named
observable mechanism by which the threshold crossing is confirmed in production (e.g.,
"inventory-service health probe returns degraded", "payment-provider timeout counter
exceeds N/window"). Together these transform each scenario from a reactive failure
description into a bounded detection specification: the threshold expression defines the
activation boundary; the detection signal defines the monitoring obligation. A reader can
scan the Trigger Condition column and wire an alert for each scenario without reading
scenario prose. A qualitative trigger description ("when the service is unavailable")
cannot be operationalized for alerting; a threshold expression without a detection signal
cannot confirm when the threshold is crossed in production. Both components are
independently load-bearing; absence of either downgrades to PARTIAL. (Signal: V-02/V-05
Round 10 -- Trigger Condition column with threshold expression + detection signal, making
scenarios operationalizable for alerting directly from column scan.)

**Pass condition**: A Trigger Condition column (or equivalently named entry-bounding
column) is present in the scenario table and its Fill Requirement explicitly names both
the threshold expression component (quantified activation condition) and the detection
signal component (named observable mechanism) as distinct required fields. At least one
scenario row descriptor or example row fills both components with non-generic content. A
qualitative trigger description or a threshold expression without a corresponding detection
signal fails.

**Partial**: Trigger Condition column present but Fill Requirement specifies only one of
the two required components; or both components listed as conceptual requirements but row
fills or examples illustrate only one component populated; or Trigger Condition column
present as a header without a Fill Requirement specification of its two-component
structure.

**Fail**: No Trigger Condition column (or equivalent entry-bounding column) in the
scenario table; scenarios are bounded only by failure class labels or qualitative
descriptions; scenario activation conditions are not operationalized in column form.

### C-35 -- Three-Component Recovery Stage Specification *(E-21)*
Each of the four Recovery Path lifecycle stages (Detect, Contain, Recover, Validate)
carries three required components in the column specification or row descriptor: (1)
mechanism -- the action taken to advance the stage, with named actor (extending C-07);
(2) SLA target -- a named time-to-[X] commitment paired to the stage (e.g., TTD/Detect,
TTC/Contain, TTR/Recover, TTV/Validate); and (3) Verification Signal (VS) -- a named
observable artifact that confirms the stage is complete independent of SLA elapse (e.g.,
"inventory-service heartbeat returns 200", "payment provider ACK logged to audit trail",
"dual-write conflict counter resets to 0 for 60s"). The VS makes each stage independently
falsifiable: the stage is closed when the named observable appears, not when the timer
expires. SLA elapse records duration; the VS confirms outcome. A recovery specification
that provides mechanism and SLA without a VS cannot be operationally verified at stage
granularity. Each VS must satisfy three properties: (a) named, not generic ("VS:
confirmation" fails; "VS: inventory-service health probe returns 200" passes); (b)
observable -- a system state, log entry, metric value, or API response code; (c) distinct
from the mechanism -- evidence of completion, not a restatement of the action taken.
(Signal: V-03/V-04/V-05 Round 10 -- Verification Signal per recovery stage, each stage
independently falsifiable by a named observable artifact distinct from mechanism and SLA
elapse alone.)

**Pass condition**: The Recovery Path column specification or at least one scenario row
descriptor explicitly requires all three components -- mechanism (with actor), SLA target,
and named Verification Signal -- for each of the four lifecycle stages. The VS requirements
must cover all four stages; a specification that names VS for two stages but leaves the
other two as mechanism+SLA only fails. At least one row descriptor illustrates concrete VS
examples for at least two of the four stages with named observables. A VS described only
generically ("stage confirmed", "recovery verified") without naming the observable artifact
fails.

**Partial**: Three-component structure present in the column specification but row
descriptors or examples show only mechanism + SLA (no VS); or VS present for some stages
but not all four in the column specification; or VS present and named for at least two
stages but described generically (non-named observable) for the remaining stages.

**Fail**: Recovery Path specification contains mechanism and SLA only, with no Verification
Signal component anywhere in the column specification or row descriptors; or VS mentioned
in prose but not encoded as a required column component; or Recovery Path stages are not
individually specified (single-block recovery description with no per-stage structure).

---

## Scoring Formula

| Tier | Weight | Criteria | Per-criterion |
|------|--------|----------|--------------|
| Essential | 60% | C-01, C-02, C-03, C-04, C-05 | PASS=12, PARTIAL=6, FAIL=0 |
| Recommended | 30% | C-06, C-07, C-08 | PASS=10, PARTIAL=5, FAIL=0 |
| Aspirational | 10% | C-09 through C-35 | PASS=2, PARTIAL=1, FAIL=0; capped at 10 |

```
composite = sum(essential_scores)               # max 60
          + sum(recommended_scores)             # max 30
          + min(sum(aspirational_scores), 10)   # max 10 (capped)
```

Maximum possible score: **100**

**Golden threshold**: all 5 essential criteria pass **and** composite >= 80.

**Ceiling references under v11:**
- R10 V-01 (intra-row column-group gate): C-33 PASS, C-34 FAIL, C-35 FAIL
  -> 46/54 uncapped -> composite = 60 + 30 + 10 = **100** (capped)
- R10 V-02 (trigger condition): C-33 FAIL, C-34 PASS, C-35 FAIL
  -> 45/54 uncapped -> composite = **100** (capped)
- R10 V-03 (verification signal): C-33 FAIL, C-34 FAIL, C-35 PASS
  -> 45/54 uncapped -> composite = **100** (capped)
- R10 V-04 (column-group + verification signal): C-33 PASS, C-34 FAIL, C-35 PASS
  -> 47/54 uncapped -> composite = **100** (capped)
- R10 V-05 (all three axes): C-33 PASS, C-34 PASS, C-35 PASS
  -> 50/54 uncapped -> composite = **100** (new uncapped ceiling: 50/54)
- Open for R11: none -- all criteria cracked by R10 V-05.

---

## Failure Fast-Paths

The following conditions automatically fail scoring regardless of composite score:

- Output contains no explicit failure scenarios (pure prose advice with no scenario
  structure)
- Output is domain-agnostic (no commerce or distributed systems grounding anywhere)
- Recovery paths are all identical or all trivially "restart the service" / "wait for
  recovery"
- Fewer than three degradation classes are represented (offline, partial failure, eventual
  consistency)

---

## Version Notes

**v11 changes from v10:**

- **C-33 (new)** -- Intra-row column-group phase gate: extracted from V-01/V-04/V-05 Round
  10 structural excellence (embedding a "C-phase complete before D-phase begins" advance-
  inhibitor directly in each scenario row descriptor). The existing gate stack in this
  rubric track gates at row level (slot-level in-row imperatives analogous to C-19) and at
  sub-field granularity within a row cell. C-33 adds the missing level: within-row
  ownership-phase transition. When the scenario table is divided into Commerce Expert
  columns (C-phase) and Distributed Systems Expert columns (D-phase), a model may complete
  all C-phase cells then begin D-phase columns, with the row-level gate only firing after
  the row is fully complete. The column-group gate fires before D-phase begins, enforcing
  C-phase completion as a prerequisite. Naming the column-phase boundary is load-bearing: a
  generic "fill all columns" instruction does not make the ownership transition itself a
  gate boundary. Cracked by V-01, V-04, V-05.
- **C-34 (new)** -- Trigger condition column: threshold expression + detection signal:
  extracted from V-02/V-05 Round 10 structural excellence (Trigger Condition column
  requiring both a quantified threshold expression and a named detection signal per
  scenario). This extends the orthogonal-auditability design principle from C-32 (bypass
  detection via column scan) to scenario activation detection: a reader scanning the Trigger
  Condition column can independently determine when each scenario fires and what signal
  confirms the threshold crossing, without traversing scenario prose. Both components are
  independently required -- a threshold expression defines the activation boundary; a
  detection signal defines the monitoring obligation. Cracked by V-02, V-05.
- **C-35 (new)** -- Three-component recovery stage specification: extracted from V-03/V-04/
  V-05 Round 10 structural excellence (Recovery Path extension to mechanism + SLA target +
  Verification Signal per stage). C-07 (recommended) requires actor-labeled recovery steps;
  C-35 requires each stage to be independently falsifiable by a named observable artifact.
  The VS creates a per-stage completion certificate: stage closure is confirmed by the
  observable's appearance, not by SLA elapse alone. Each VS must be named (not generic),
  observable, and distinct from the mechanism. Cracked by V-03, V-04, V-05.
- **Aspirational cap unchanged** at 10; uncapped maximum rises from 48 to 54 (27 criteria x
  PASS=2). V-05 is the new uncapped ceiling at 50/54. Open for R11: none -- all criteria
  cracked by R10 V-05. Persistent uncracked block: C-09 and C-10 (chaos engineering and
  observability hooks -- unaddressed across all rounds).

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
- **C-15 strengthened** -- Pass condition now requires named "DS Primitive cited:" field
  with inline VALID/INVALID annotated examples.
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
- **Aspirational scoring rebalanced**: C-09 and C-10 reduced from PASS=5 to PASS=2 to
  accommodate the growing aspirational tier without changing the band cap.
