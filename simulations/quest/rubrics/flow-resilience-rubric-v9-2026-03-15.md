Written to `simulations/quest/rubrics/flow-resilience-rubric-v9-2026-03-15.md`.

---

**Two new criteria extracted from Round 8:**

**C-29 -- Rule-Bypass-Triggered Gate Reopening** (V-01 C-28: "RULE-BYPASSED must reopen affected gate before COMPLETE")

C-28 says what the audit *reports* (RULE-BYPASSED = audit failure). C-29 says what it *forces*: the finding is a gate-reopening trigger, not a note. The affected gate must be re-opened, the bypassed rule applied, the gate re-closed under a C-20-style amendment sub-gate (e.g., `GATE N-bypass: AMENDED`), and the audit entry updated to INVOKED before COMPLETE may be declared. An analysis that acknowledges the bypass and proceeds to COMPLETE has an unresolved execution failure in its record.

**C-30 -- Multi-Act Completion Sign-Off** (V-01 C-28: "dual Act 1 / Act 2 sign-off")

A single terminal COMPLETE in a multi-act analysis cannot verify per-act gate closure -- an open gate in Act 1 is invisible from Act 2's terminal block. Each act must close with its own sign-off declaring: (1) all gates within that act CLOSED, (2) scope exhausted, (3) no unresolved RULE-BYPASSED conditions in that act. Single-act analyses score C-30 as N/A (PARTIAL, 1 point).

**Scoring delta**: cap unchanged at 10; uncapped aspirational max rises from 40 to 44 (22 criteria x 2).
distinguish
Act 1 gate closure from Act 2 gate closure. Each act must close with its own per-act
sign-off declaring: (1) all gates within that act are CLOSED; (2) the act's scope is
exhausted; and (3) no RULE-BYPASSED conditions remain unresolved within that act. The
dual sign-off makes each act's closure independently auditable and prevents Act 2's
completion from implicitly masking Act 1 deficiencies.

**Scoring delta**: cap unchanged at 10; uncapped aspirational max rises from 40 to 44
(22 criteria x 2).

---

## Essential Criteria (must pass all -- 60% of score)

### C-01 -- Three Degradation Classes
- **Weight**: essential
- **Category**: coverage
- **Text**: The output covers all three distinct failure-mode degradation classes: (1) full
  disconnection -- client is offline or the network is partitioned from all servers; (2)
  partial failure -- one or more backend services are unavailable but the system remains
  partially accessible; (3) eventual-consistency conflict -- concurrent writes diverge
  across nodes in a distributed deployment, producing data inconsistency without full
  unavailability. All three classes are represented by distinct named scenarios.
- **Pass condition**: At least one scenario per degradation class is present. Scenarios
  that collapse class 2 and class 3 into a single "network issue" fail. Analyses that
  address class 1 only (offline-only) fail.

### C-02 -- Four-Field Structure Per Scenario
- **Weight**: essential
- **Category**: structure
- **Text**: Every failure scenario includes all four required fields: (1) state -- what the
  system state is when failure occurs; (2) capability -- what the user can still do; (3) data
  at risk -- what data may be lost, stale, or inconsistent; (4) recovery path -- how the
  system returns to a healthy state.
- **Pass condition**: Every scenario present in the output includes all four fields with
  non-trivial content (not placeholder, "N/A", or a single word). A scenario missing any
  field fails this criterion entirely.

### C-03 -- Gap Identification (Three Types)
- **Weight**: essential
- **Category**: correctness
- **Text**: The output identifies at least one offline experience gap, at least one data
  consistency violation, and at least one missing recovery flow as distinct named findings.
  These are the three explicit output targets the skill defines.
- **Pass condition**: All three finding types appear, each labeled and actionable -- not merely
  implied or bundled. Generic statements like "offline support may be limited" without
  specificity fail.

### C-04 -- Distributed Systems Accuracy
- **Weight**: essential
- **Category**: correctness
- **Text**: Technical claims about failure modes are consistent with distributed systems
  fundamentals. CAP theorem trade-offs, retry semantics, idempotency requirements, and
  conflict-resolution strategies are used correctly wherever referenced.
- **Pass condition**: No materially incorrect distributed-systems claim is present. Fabricated
  error codes, invented protocols, or impossible consistency guarantees (e.g., strong
  consistency with no latency cost across a partition) fail this criterion.

### C-05 -- Commerce Domain Grounding
- **Weight**: essential
- **Category**: depth
- **Text**: The analysis is grounded in the commerce / distributed systems domain. Failure
  scenarios reference realistic commerce flows -- checkout, inventory reservation, payment
  processing, order fulfillment, cart state -- rather than generic CRUD operations.
- **Pass condition**: At least two scenarios are anchored to a recognizable commerce operation
  by name. Purely abstract or domain-agnostic scenarios fail.

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
  describe only the end state ("system recovers", "data is synchronized") without
  mechanism fail.

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
Uncapped maximum across 22 criteria is 44; the cap rewards breadth while holding the
composite ceiling at 100.

### C-09 -- Chaos Engineering Test Cases
- **Weight**: aspirational
- **Category**: behavior
- **Text**: The output includes one or more concrete chaos-engineering test scenarios that
  could be scheduled in a test harness. Each scenario specifies: (1) what to inject (network
  partition, latency spike, service kill, packet loss), (2) expected observable behavior, and
  (3) a binary pass/fail signal.
- **Pass condition**: At least one runnable chaos scenario is present with all three elements.
  Vague suggestions to "test resilience" or "add chaos testing" without specifics fail.
- **Partial**: Chaos scenario present but missing one of the three required elements.
- **Fail**: No chaos engineering content, or suggestions without runnable specifics.

### C-10 -- Observability Hooks Tied to Named Gaps
- **Weight**: aspirational
- **Category**: depth
- **Text**: The output recommends specific observability signals -- metrics, logs, traces, or
  alerts -- that would surface each identified gap in production. Each recommendation is tied
  to a specific named gap or scenario from the analysis with a rationale.
- **Pass condition**: At least two observability recommendations are present, each linked to a
  named gap or scenario with a rationale for why that signal would detect the failure early.
  Generic "add monitoring" suggestions without specifics fail.
- **Partial**: Observability recommendations present but fewer than two are tied to named
  gaps with rationale.
- **Fail**: No observability content, or generic recommendations without gap linkage.

### C-11 -- Confidence-Annotated Discovery Catalog
- **Weight**: aspirational
- **Category**: correctness
- **Text**: The distributed-systems analysis phase carries explicit confidence ratings
  (high / medium / low / impossible) for each failure mode before scenarios are committed to
  the output. Each rating cites its basis -- an architecture constraint or DS theory reference
  -- not just a label. Entries rated "impossible" are excluded from the scenario table but
  retained in the discovery phase with their rationale. Entries rated "low confidence" are
  barred from the scenario table until the confidence basis is resolved; flagging alone does
  not satisfy this gate. This triage gate prevents technically invalid scenarios from
  polluting the output and makes the discovery phase independently auditable.
  (Signal: V-01, V-04.)
- **Pass condition**: Every failure mode in the discovery phase carries a confidence rating
  with a cited basis; "impossible" entries are excluded from the table with retained rationale;
  "low confidence" entries are barred from the table until resolved -- not merely flagged.
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
  offline-experience gaps identified for this deployment pattern -- all critical paths include
  local-fallback state." The nil finding includes a scope rationale explaining why the gap
  type does not apply; a bare "none found" statement does not satisfy this criterion. Silence
  is not a valid nil finding. (Signal: V-01, V-02, V-03.)
- **Pass condition**: All three gap sections are explicitly present; sections with no findings
  carry a labeled nil finding that includes a brief scope rationale explaining why the gap
  type does not apply for this deployment pattern.
- **Partial**: Some nil findings present but not all three sections covered, or nil findings
  appear without scope rationale (bare "none found" statement).
- **Fail**: Missing gap sections are silently absent; reader cannot distinguish "no gaps
  found" from "gaps not analyzed."

### C-13 -- Coverage Accountability Roster
- **Weight**: aspirational
- **Category**: coverage
- **Text**: The output opens with a pre-analysis roster that commits to minimum per-class
  coverage -- at least two scenarios per degradation class -- before scenario analysis begins.
  The roster is checkable: the reader can verify class coverage against the final scenario
  list without reading the full analysis. When a class slot cannot be filled, the output
  provides an explicit impossibility argument or reclassification -- it does not silently
  reduce coverage below the committed minimum. The challenge mechanism ("why can't you fill
  this slot?") is answered inline, not omitted. (Signal: V-03, V-05.)
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
  violation (DCV) gap section as a named DCV finding. The conflict-resolution section and the
  gap identification section are bidirectionally linked -- an inadequate or undefined strategy
  is always a DCV, not a standalone note. This prevents conflict-resolution weaknesses from
  being isolated in one section and invisible to the gap tally. When all strategies are
  adequate, an explicit CLOSED confirmation is written. (Signal: V-02, V-04 --
  "inadequate/undefined -> DCV" pattern.)
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
  impossibility argument cites a specific distributed systems primitive -- a named CAP theorem
  guarantee, a deployment topology constraint, or a synchronous consistency guarantee that
  forecloses the failure class. Topic-scope arguments ("the topic doesn't mention caching",
  "the system description is too simple for this class") are not valid impossibility
  arguments. The argument must address the architecture, not the description. The template
  includes a named "DS Primitive cited:" field with inline VALID / INVALID annotated examples
  so that the distinction between an architecture argument and description absence is
  unambiguous. (Signal: V-03 Round 2 -- "'The topic doesn't mention X' is not an
  impossibility argument."; V-02 Round 3 -- named field + counter-examples as the mechanism.)
- **Pass condition**: Every impossibility argument cites a specific DS primitive via a named
  "DS Primitive cited:" field with an architecture basis. Inline VALID/INVALID annotated
  examples are present in the template. No topic-scope arguments appear; any argument
  invoking description absence rather than architecture constraint fails.
- **Partial**: Some impossibility arguments cite DS primitives but others rely on topic scope
  or description absence; or DS primitive field is present but lacks inline VALID/INVALID
  examples.
- **Fail**: Impossibility arguments rely solely on topic scope or description absence; no DS
  primitive is cited; or the challenge mechanism is absent entirely.

### C-16 -- Named Gate-State Vocabulary
- **Weight**: aspirational
- **Category**: format
- **Text**: The confidence triage and gap sections use a fixed, named disposition vocabulary
  -- entries are assigned exactly one of: Include / BARRED / Argued-Impossible (or equivalent
  named states). Free-text confidence descriptions that do not resolve to one of these named
  dispositions are not valid. Each gate section carries an explicit binary OPEN / CLOSED
  declaration visible without reading the prose. "Flagged" and similar qualitative labels
  that do not resolve to a named disposition are rejected -- a gate section without a named
  OPEN/CLOSED state is treated as OPEN by definition. A gate cannot close while any entry
  in that section carries an unresolved disposition. (Signal: V-02 C-11 -- "BARRED (low --
  [unresolved basis])"; V-03 C-11 -- "GATE OPEN -- LOW CONFIDENCE named disposition;
  'Flagged is not a disposition' explicitly stated.")
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
  excluded for architectural reasons" (Argued-Impossible) and "analyzed but confidence never
  confirmed" (permanently BARRED) are not equivalent and must not be conflated.
  (Signal: V-02 C-11 -- "barred entries either resolve to Include or remain barred and are
  recorded as a coverage gap.")
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
  analysis closure independently auditable. (Signal: V-03 C-14 -- "entry condition: Gate 3
  CLOSED on 3a and 3c (3b stays open); exit condition: DCV amendment + Gate 3b CLOSED;
  explicit CLOSED confirmation required.")
- **Pass condition**: At least two phases carry named entry conditions (citing prior gate
  identifiers) and named exit conditions; each of those phases closes with an explicit CLOSED
  confirmation statement.
- **Partial**: Entry or exit conditions present on some phases but not all; or conditions
  stated but without gate-identifier references; or no explicit CLOSED confirmations.
- **Fail**: No phase carries stated entry/exit conditions; phases are ordered by prose
  position only; closure is inferred, not declared.

### C-19 -- Gate Blockage Transparency (Reason-if-OPEN)
- **Weight**: aspirational
- **Category**: format
- **Text**: When a gate is in OPEN state -- not yet closed -- the blocking reason is declared
  inline as a named "Reason if OPEN:" field or equivalent. An OPEN gate with no stated reason
  is indistinguishable from a gate that was never evaluated or was abandoned mid-analysis. The
  reason field must name the specific blocking condition: the unresolved entry ID, the unmet
  coverage minimum, the pending adequacy verdict, or the outstanding amendment. This allows
  the analysis to be resumed deterministically once the blocking condition is resolved, without
  re-reading all prior gate prose. A gate displaying only "OPEN" without a blocking reason is
  treated as an error, not as a valid in-progress state. (Signal: V-03 Round 4 C-18 --
  "GATE N STATUS: [OPEN | CLOSED] with 'Reason if OPEN' field" as the mechanism for
  auditable gate tracking.)
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
- **Text**: When a downstream finding invalidates the output of an already-CLOSED gate (e.g.,
  a conflict-resolution adequacy failure requires an additional DCV entry that the prior DCV
  gate was closed without), the prior gate is explicitly re-opened, the amendment is applied,
  and the gate is re-closed under a labeled amendment sub-gate (e.g., "GATE 3b: AMENDED").
  The amendment record names the downstream finding that triggered the reopening. Late
  amendments silently appended to a closed section are unverifiable and break the gate audit
  trail. A re-opened gate whose amendment is applied without a labeled re-close record is
  treated as still OPEN. (Signal: V-03 Round 4 C-14 -- "this reopens Gate 3 for that
  amendment only; write `GATE 3b: AMENDED`" as the mechanism for traceable late-finding
  integration.)
- **Pass condition**: At least one downstream finding that requires an amendment to a prior
  CLOSED gate triggers an explicit re-open, applies the amendment, and re-closes the gate
  under a labeled sub-gate identifier. The amendment record references the downstream finding
  by ID. When no downstream findings require amendments, an explicit confirmation is present.
- **Partial**: Late amendment applied to a prior closed gate section but without a labeled
  re-open / re-close record; or sub-gate label present but the downstream finding that
  triggered it is not referenced.
- **Fail**: Downstream findings that invalidate prior gate outputs are silently appended
  without re-opening the gate; or no mechanism exists for downstream findings to amend prior
  gate sections; or the gate audit trail has no sub-gate amendment records.

### C-21 -- Pre-Analysis Commerce Operation Scope Declaration
- **Weight**: aspirational
- **Category**: coverage
- **Text**: Before scenario analysis begins, the output commits to a named, exhaustive list of
  commerce operations that will be analyzed. The declaration names every operation in scope
  (e.g., checkout, inventory reservation, payment processing, cart state, order fulfillment,
  loyalty redemption). This commitment is checkable against the final scenario table: any
  declared operation that receives no scenario coverage is a named gap, not a silent omission.
  Operations excluded from the declaration are either explicitly out-of-scope with a stated
  reason or their absence is a coverage gap. C-05 requires scenarios to be anchored to named
  operations; C-21 requires the scope commitment to precede the analysis, not emerge from it.
  (Signal: V-05 Round 4 C-05 -- explicit upfront enumeration of all six named commerce
  operations before scenario derivation begins.)
- **Pass condition**: A named commerce operation scope list is present before the first
  scenario entry. The list covers at least four distinct operations. The final scenario table
  provides coverage for each declared operation or explicitly records it as a gap. Operations
  mentioned only within scenario bodies (not declared upfront) do not satisfy this criterion.
- **Partial**: Upfront scope declaration present but covers fewer than four operations; or
  declaration present but final coverage is not cross-checked against the declared list; or
  operations appear only in a post-hoc summary, not a pre-analysis commitment.
- **Fail**: No upfront commerce operation scope declaration; the set of covered operations is
  inferred from the scenario table only; coverage gaps are not distinguishable from scope
  exclusions.

### C-22 -- Typed Nil-Finding Identifiers
- **Weight**: aspirational
- **Category**: format
- **Text**: Nil findings carry gap-type prefix identifiers -- OEG-NIL (offline experience
  gap), DCV-NIL (data consistency violation), MRF-NIL (missing recovery flow) -- that bind
  each nil statement to its gap category by name. C-12 requires nil findings with scope
  rationale; C-22 requires those nil findings to be addressable by type. A nil statement
  without a typed identifier satisfies C-12 but cannot be audited, queried, or cross-
  referenced by gap type. The identifier also makes it unambiguous which of the three output
  targets is being declared nil: a generic "no gaps found" statement that doesn't name the
  target type is insufficient even if a scope rationale is present. Each typed nil identifier
  is unique within an analysis run; if the same gap type produces a nil in multiple phases,
  each carries its own identifier (OEG-NIL-1, OEG-NIL-2). (Signal: V-01 Round 5 C-12 PASS
  evidence -- "`OEG-NIL: ... [scope rationale explaining why this gap type does not apply
  for this deployment pattern]`" as the mechanism for type-addressable nil findings.)
- **Pass condition**: Every nil finding carries a typed prefix identifier (OEG-NIL, DCV-NIL,
  MRF-NIL, or equivalent named type prefix). Each identifier is unique within the run.
  Nil statements without a typed identifier fail this criterion regardless of rationale
  quality.
- **Partial**: Typed identifiers present on some nil findings but not all; or typed prefix
  used but not consistently bound to the gap type (e.g., OEG-NIL used for a recovery-flow
  nil).
- **Fail**: No typed nil-finding identifiers; nil statements use only prose headings or bare
  "none found" / "N/A" markers; nil findings are not queryable by gap type.

### C-23 -- Scope Declaration Closure Bracket
- **Weight**: aspirational
- **Category**: format
- **Text**: The pre-analysis commerce operation scope declaration (C-21) is bracketed by two
  named boundary blocks: an opening `SCOPE DECLARATION COMPLETE` confirmation that closes
  the declaration phase before analysis begins, and a terminal `Scope Verification` block
  that cross-checks the declared operation list against the final scenario table after
  analysis concludes. C-21 requires the upfront commitment and checkability; C-23 requires
  the bracket to be structurally visible as two distinct named blocks so that scope opening
  and scope closure are independently auditable without reading the full analysis. The
  terminal Scope Verification block must name each declared operation and its coverage
  outcome (covered / gap / out-of-scope). A scope declaration that opens but never formally
  closes is treated as unverified. (Signal: V-01 Round 5 C-21 PASS evidence -- "Full
  `SCOPE DECLARATION COMPLETE` block before Phase 1; Scope Verification cross-check at end;
  In-scope/Excluded tripartite with rationale" as the mechanism for auditable scope closure.)
- **Pass condition**: An opening `SCOPE DECLARATION COMPLETE` block (or named equivalent) is
  present immediately after the operation list, before the first analysis phase. A terminal
  `Scope Verification` block (or named equivalent) is present after the final analysis phase,
  naming each declared operation with its coverage outcome. Both blocks are required; a
  declaration with only one does not satisfy this criterion.
- **Partial**: Opening declaration confirmation present but no terminal verification block;
  or terminal verification block present but not tied to the upfront declaration list; or
  terminal block present but coverage outcomes are not named per declared operation.
- **Fail**: No named boundary blocks; scope declaration is embedded in prose with no opening
  confirmation; terminal cross-check is absent or inferred from the scenario table without
  a named block.

### C-24 -- Template-Embedded Conditional Linkage Rules
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Cross-section linkages that are required by the skill's logic are encoded in the
  template as explicit named conditional rules -- `if [condition]: [action]` -- rather than
  described in prose instructions or left to analyst discretion. The canonical example is the
  DCV linkage from conflict-resolution adequacy: rather than instructing the analyst to "link
  inadequate strategies to DCV findings," the template contains a named rule: `if verdict is
  [no | undefined]: append DCV-CR-NN`. This makes correct cross-section behavior mandatory
  and machine-checkable. C-14 requires the DCV linkage to exist; C-24 requires it to be
  encoded as a named conditional rule. A prose instruction that describes the linkage without
  encoding a trigger condition does not satisfy this criterion. At least two distinct
  conditional linkage rules must be present to demonstrate that the pattern is systemic, not
  incidental. (Signal: V-01 Round 5 C-14 PASS evidence -- "Phase 4: 'If verdict is `no` or
  strategy is `undefined`: append `DCV-CR-NN`' -- linkage to Phase 3" as the mechanism for
  mandatory cross-section linkage.)
- **Pass condition**: At least two named conditional linkage rules are present in the template
  in explicit `if [condition]: [action]` form (or a structurally equivalent named rule block).
  Each rule names both its trigger condition and its cross-section action. Prose instructions
  that describe the same logic without an explicit conditional rule form do not satisfy this
  criterion.
- **Partial**: One conditional linkage rule present but not two; or rules present in
  conditional form but trigger conditions are underspecified (e.g., "if inadequate: update
  DCV" without naming what "inadequate" evaluates); or rules embedded in prose annotations
  rather than named rule blocks.
- **Fail**: No conditional linkage rules in the template; cross-section linkages are described
  in prose instructions only; correct behavior depends on analyst discretion rather than
  template enforcement.

### C-25 -- Nil-Finding Supersession Protocol
- **Weight**: aspirational
- **Category**: correctness
- **Text**: Typed nil-finding identifiers (C-22) have a two-state lifecycle: ACTIVE (nil
  declared, gap type not present for this deployment pattern) and SUPERSEDED (downstream
  analysis subsequently identifies a gap in the same category, rendering the nil declaration
  obsolete). When a downstream phase produces a gap finding that supersedes a previously
  declared nil, the nil identifier is explicitly annotated SUPERSEDED with a cross-reference
  to the finding ID that replaced it (e.g., "OEG-NIL-1: SUPERSEDED by OEG-F-3"). A nil
  declaration that has been superseded but carries no SUPERSEDED marker leaves the reader
  uncertain whether the nil still stands -- the nil ID and the new finding coexist without
  resolution. A nil marked SUPERSEDED without citing the superseding finding ID is incomplete:
  the reader cannot trace the discovery to its nil declaration. The supersession protocol
  creates a closed audit trail from nil declaration through gap discovery and prevents a live
  nil and a live gap from coexisting on the same gap type in the same analysis run. When no
  nil findings are superseded, an explicit "no supersessions" confirmation is present.
  (Signal: V-01 Round 6 C-22 PASS evidence -- "supersession notation defined"; C-20 PARTIAL
  evidence -- "DCV-NIL-1: SUPERSEDED noted" as the mechanism for nil lifecycle tracking.)
- **Pass condition**: At least one nil finding that is superseded by a downstream actual
  finding carries an explicit SUPERSEDED annotation citing the superseding finding ID. When
  no nil findings are superseded during the analysis run, an explicit "no supersessions"
  confirmation is present. A nil ID and a gap finding of the same type coexisting without a
  SUPERSEDED annotation on the nil fails this criterion.
- **Partial**: Supersession notation present on superseded nils but does not cite the
  superseding finding ID; or SUPERSEDED present on some superseded nils but not all; or
  "no supersessions" confirmation absent when no supersessions occur.
- **Fail**: Superseded nil findings carry no SUPERSEDED marker; a nil declaration and a gap
  finding of the same type coexist in the output without resolution; nil identifiers are
  treated as write-once with no lifecycle tracking.

### C-26 -- Confidence Triage Resolution Sub-Gate
- **Weight**: aspirational
- **Category**: correctness
- **Text**: When a BARRED discovery entry has its unresolved confidence basis subsequently
  satisfied during analysis and is upgraded to Include, the upgrade path is recorded under a
  labeled triage resolution sub-gate (e.g., "GATE 1b: RESOLVED" or equivalent named sub-
  gate). C-17 addresses the case where a BARRED entry's basis is never resolved -- the entry
  remains permanently BARRED and is recorded as a coverage gap. C-26 addresses the inverse:
  when the basis is resolved and the entry is promoted to Include, that promotion is auditable.
  Without a named sub-gate, a scenario that silently appears in the Include column may have
  been BARRED earlier with no trace of the resolution -- the reader cannot distinguish "was
  always Include" from "was BARRED, basis resolved, promoted." The resolution sub-gate must
  name: the entry ID being resolved, the confidence basis that was satisfied and how, the new
  Include disposition, and the re-closed triage gate status. When no BARRED entries are
  resolved during analysis, an explicit "no BARRED-to-Include upgrades" confirmation is
  present. (Signal: V-03 Round 6 structural excellence -- "Gate 1b" as a labeled sub-gate
  for BARRED-to-Include promotion paths.)
- **Pass condition**: At least one BARRED entry that is resolved to Include during analysis
  appears under a labeled triage resolution sub-gate naming the entry ID, the satisfied basis,
  and the new disposition, with the triage gate re-closed. When no BARRED entries are resolved
  during analysis, an explicit confirmation is present.
- **Partial**: BARRED-to-Include upgrade recorded in prose but without a labeled sub-gate; or
  sub-gate present but does not name the satisfied basis or the entry ID being resolved; or
  confirmation absent when no upgrades occur.
- **Fail**: BARRED entries silently appear in the scenario table as Include with no resolution
  record; the reader cannot determine whether entries were always Include or promoted from
  BARRED; or no mechanism exists for BARRED entries to be explicitly resolved during analysis.

### C-27 -- Named Rule Block Registry
- **Weight**: aspirational
- **Category**: format
- **Text**: The named conditional linkage rules required by C-24 appear in a discrete, named
  rule registry section within the template -- not embedded inline in gate-section prose.
  Each rule in the registry carries a unique identifier (e.g., RULE-CR-DCV, RULE-SCOPE-GAP,
  RULE-NIL-SUPERSEDE) that makes it independently addressable: other gate sections can cite a
  rule by its ID rather than by prose location. C-24 requires that at least two named
  conditional rules exist in explicit `if [condition]: [action]` form; C-27 requires that the
  complete rule set be enumerable from a single registry section without traversing the full
  analysis template. A template where rules are correct in form (satisfying C-24) but
  scattered inline through gate prose satisfies C-24 but fails C-27: inline rules are not
  enumerable, not independently auditable, and cannot be cited by ID from other gate
  conditions. The registry structure also prevents rule duplication across gates, since all
  rules are declared once and cited many times. (Signal: V-03 Round 6 structural excellence
  -- named RULE blocks as a discrete section vs. V-01/V-02 inline prose conditionals that
  satisfy the trigger-condition form but are not enumerable by ID.)
- **Pass condition**: A named rule registry section is present listing all conditional linkage
  rules. Each rule carries a unique ID, explicit trigger condition, and named cross-section
  action target. Gate sections that invoke linkage behavior cite rules by their registry ID,
  not by restating the conditional logic inline. At least two rules with distinct IDs are
  present.
- **Partial**: Named rules present and correct in conditional form (satisfying C-24) but
  embedded inline in individual gate sections rather than in a discrete registry; or registry
  present but fewer than two rules carry unique IDs; or rules listed in the registry but gate
  sections restate the conditional logic inline rather than citing registry IDs.
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
  rule was not applied (rule-bypassed, which is an audit failure). Without a post-analysis
  audit, a correctly declared registry may contain rules that were silently skipped during
  execution: the gate prose will reference rule IDs but the reader cannot confirm that
  invocations actually occurred or were complete. A rule that never fires may indicate an
  overly restricted scope or a rule targeting a condition that the template's confidence-
  triage gate permanently prevents from reaching the linkage gate. The audit block makes
  rule execution independently verifiable without re-reading the full analysis.
  (Signal: V-03 Round 7 structural excellence -- "Post-Analysis Registry Audit" as a named
  terminal block confirming per-rule invocation counts and uninvoked-rule disposition.)
- **Pass condition**: A named post-analysis audit block is present after all analysis gates
  complete. The block lists each registered rule by ID and reports its invocation status:
  fired (with gate and entry citation) or uninvoked (with scenario-absent or rule-bypassed
  classification). At least two registered rules are accounted for. A rule that is invoked
  but whose invocation is not cited by gate and entry fails this criterion.
- **Partial**: Post-analysis review of rule usage present but not as a named, discrete audit
  block; or block present but covers only some registered rules without explanation for
  omitted ones; or invocations listed without citing the triggering gate and entry.
- **Fail**: No post-analysis rule audit; the rule registry is treated as a declaration-only
  artifact with no execution verification; the reader cannot determine which rules were
  applied during the run without re-reading all gate sections.

### C-29 -- Rule-Bypass-Triggered Gate Reopening
- **Weight**: aspirational
- **Category**: correctness
- **Text**: C-28 classifies a registered rule as RULE-BYPASSED when its trigger condition
  arose during a gate but the rule was not applied -- an audit failure. C-29 enforces the
  consequence: a RULE-BYPASSED finding is a gate-reopening trigger, not merely a reported
  deficiency. Before the analysis can declare COMPLETE, the affected gate must be explicitly
  reopened, the bypassed rule applied, the gate re-closed under a labeled amendment sub-gate
  following the C-20 mechanism (e.g., "GATE N-bypass: AMENDED"), and the audit entry updated
  from RULE-BYPASSED to INVOKED. C-28 says what the audit reports; C-29 says what a
  RULE-BYPASSED finding forces. An analysis that acknowledges a RULE-BYPASSED classification
  in the audit and proceeds to COMPLETE without reopening the affected gate has an unresolved
  execution failure in its record. The distinction between C-28 and C-29: C-28 requires the
  audit to exist and classify each uninvoked rule; C-29 requires that the RULE-BYPASSED
  classification actively blocks the COMPLETE declaration until the gate is remediated.
  (Signal: V-01 Round 8 C-28 PASS evidence -- "RULE-BYPASSED must reopen affected gate
  before COMPLETE.")
- **Pass condition**: When the post-analysis audit produces at least one RULE-BYPASSED finding,
  an explicit gate-reopening chain follows: the affected gate is re-opened, the bypassed rule
  is applied, the gate is re-closed under a labeled amendment sub-gate citing the bypass
  finding ID, and the audit entry is updated to INVOKED before COMPLETE is declared. When no
  RULE-BYPASSED conditions exist in the run, an explicit confirmation is present. An analysis
  that acknowledges RULE-BYPASSED and declares COMPLETE without gate remediation fails this
  criterion.
- **Partial**: RULE-BYPASSED finding acknowledged and gate reopened but no amendment sub-gate
  label present; or gate re-closed without updating the audit entry to INVOKED; or no
  explicit confirmation when the run contains no bypasses.
- **Fail**: RULE-BYPASSED audit findings present with no gate reopening; analysis declares
  COMPLETE with acknowledged bypass failures unresolved; or RULE-BYPASSED is treated as a
  non-blocking informational note rather than a remediation trigger.

### C-30 -- Multi-Act Completion Sign-Off
- **Weight**: aspirational
- **Category**: format
- **Text**: When the analysis is structured in two or more distinct named acts (e.g.,
  Act 1 -- DS failure mode analysis, Act 2 -- Commerce validation), the completion
  declaration requires a per-act sign-off for each act, not a single monolithic COMPLETE at
  the end. Each per-act sign-off declares: (1) all gates within that act are CLOSED; (2) the
  act's scope is exhausted; and (3) no RULE-BYPASSED conditions remain unresolved within that
  act. A single terminal COMPLETE in a multi-act analysis does not distinguish Act 1 gate
  closure from Act 2 gate closure -- if one act has an open gate or an unresolved bypass, the
  composite COMPLETE masks it. The dual sign-off makes each act's closure independently
  auditable and prevents Act 2's completion from implicitly absorbing Act 1 deficiencies by
  proximity. Both the per-act sign-offs and the terminal COMPLETE are required; the terminal
  COMPLETE confirms that all per-act sign-offs have been issued, not that gate closure is
  inferred from the terminal block alone. (Signal: V-01 Round 8 C-28 PASS evidence --
  "dual Act 1 / Act 2 sign-off.")
- **Pass condition**: When the analysis has two or more named acts, each act closes with an
  explicit per-act sign-off block declaring all gates within that act CLOSED, scope exhausted,
  and no unresolved RULE-BYPASSED conditions in that act. The terminal COMPLETE then
  references the per-act sign-offs rather than implying gate closure directly. When the
  analysis is single-act, this criterion is scored N/A and treated as PARTIAL for scoring
  purposes (contributing 1 point without requiring multi-act structure that the analysis
  design does not call for).
- **Partial**: Per-act sign-offs present but missing one of the three required elements (gate
  closure declaration / scope exhausted statement / bypass confirmation); or per-act sign-off
  present for some acts but not all; or analysis is single-act and N/A is explicitly declared.
- **Fail**: No per-act sign-offs in a multi-act analysis; terminal COMPLETE subsumes all acts
  without per-act gate closure records; or per-act sign-offs present but do not reference the
  RULE-BYPASSED state for that act.

---

## Scoring Formula

| Tier | Weight | Criteria | Per-criterion |
|------|--------|----------|--------------|
| Essential | 60% | C-01, C-02, C-03, C-04, C-05 | PASS=12, PARTIAL=6, FAIL=0 |
| Recommended | 30% | C-06, C-07, C-08 | PASS=10, PARTIAL=5, FAIL=0 |
| Aspirational | 10% | C-09 through C-30 | PASS=2, PARTIAL=1, FAIL=0; capped at 10 |

```
composite = sum(essential_scores)               # max 60
          + sum(recommended_scores)             # max 30
          + min(sum(aspirational_scores), 10)   # max 10 (capped)
```

Maximum possible score: **100**

**Golden threshold**: all 5 essential criteria pass **and** composite >= 80.

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

**v9 changes from v8:**

- **C-29 (new)** -- Rule-bypass-triggered gate reopening: extracted from V-01 Round 8 C-28
  PASS evidence ("RULE-BYPASSED must reopen affected gate before COMPLETE"). C-28 requires
  the post-analysis audit to classify each uninvoked rule as scenario-absent or rule-bypassed
  and marks the latter as an audit failure. C-29 enforces the consequence: a RULE-BYPASSED
  finding is a blocker, not a note. The affected gate must be explicitly reopened (C-20
  mechanism), the bypassed rule applied, the gate re-closed under an amendment sub-gate, and
  the audit entry updated to INVOKED before COMPLETE may be declared. Without this criterion,
  an analysis can acknowledge a bypass in the audit and still close without remediation --
  the audit report would record an unresolved execution failure that is visible but does not
  block the output. C-29 closes that gap by making RULE-BYPASSED a gating condition on the
  COMPLETE declaration itself.
- **C-30 (new)** -- Multi-act completion sign-off: extracted from V-01 Round 8 C-28 PASS
  evidence ("dual Act 1 / Act 2 sign-off"). When the analysis is structured in two or more
  named acts, a single terminal COMPLETE cannot verify per-act gate closure: an open gate or
  unresolved bypass in Act 1 is not visible in Act 2's terminal declaration. C-30 requires
  each act to close with its own sign-off block declaring all gates within that act CLOSED,
  scope exhausted, and no unresolved RULE-BYPASSED conditions in that act. The terminal
  COMPLETE then references the per-act sign-offs rather than subsuming them. Single-act
  analyses score C-30 as N/A (PARTIAL, 1 point) -- the criterion does not penalize analyses
  that are not designed as multi-act; it rewards analyses that are and handle act-level
  closure explicitly.
- **Aspirational cap unchanged** at 10; uncapped maximum rises from 40 to 44 (22 criteria x
  PASS=2). Breadth is rewarded; the composite ceiling stays at 100.

**v8 changes from v7:**

- **C-28 (new)** -- Post-analysis rule registry audit: extracted from V-03 Round 7 structural
  excellence ("Post-Analysis Registry Audit" terminal block). C-27 requires that conditional
  linkage rules appear in a discrete, enumerable registry section with unique IDs. C-28
  closes the execution loop: after all gates complete, a named audit block confirms which
  registry rules fired during the run (citing the gate and entry that triggered each
  invocation), how many times each fired, and whether any rules went uninvoked -- and
  classifies uninvoked rules as scenario-absent (triggering condition never arose) or
  rule-bypassed (condition arose but rule was not applied, which is an audit failure).
  A correctly declared registry that is never post-audited cannot prove that gate invocations
  actually occurred; the audit block makes rule execution independently verifiable without
  re-reading the full analysis.
- **Aspirational cap unchanged** at 10; uncapped maximum rises from 38 to 40 (20 criteria x
  PASS=2).

**v7 changes from v6:**

- **C-25 (new)** -- Nil-finding supersession protocol.
- **C-26 (new)** -- Confidence triage resolution sub-gate.
- **C-27 (new)** -- Named rule block registry.
- **Aspirational cap unchanged** at 10; uncapped maximum rose from 32 to 38 (19 criteria x
  PASS=2).

**v6 changes from v5:**

- **C-22 (new)** -- Typed nil-finding identifiers.
- **C-23 (new)** -- Scope declaration closure bracket.
- **C-24 (new)** -- Template-embedded conditional linkage rules.
- **Aspirational cap unchanged** at 10; uncapped maximum rose from 26 to 32 (16 criteria x
  PASS=2).

**v5 changes from v4:**

- **C-19 (new)** -- Gate blockage transparency (Reason-if-OPEN).
- **C-20 (new)** -- Downstream gate amendment with re-close record.
- **C-21 (new)** -- Pre-analysis commerce operation scope declaration.
- **Aspirational cap unchanged** at 10; uncapped maximum rose from 20 to 26 (13 criteria x
  PASS=2).

**v4 changes from v3:**

- **C-16 (new)** -- Named gate-state vocabulary.
- **C-17 (new)** -- Permanently barred entries as named coverage gaps.
- **C-18 (new)** -- Explicit phase entry and exit conditions.
- **C-15 strengthened** -- Pass condition now explicitly requires a named "DS Primitive
  cited:" template field with inline VALID/INVALID annotated examples.
- **Aspirational cap unchanged** at 10; uncapped maximum rose from 14 to 20 (10 criteria x
  PASS=2).

**v3 changes from v2:**

- **C-14 (new)** -- Conflict-resolution adequacy as DCV source.
- **C-15 (new)** -- DS-primitive-grounded impossibility arguments.
- **C-11 strengthened** -- Low-confidence entries barred (not merely flagged); each rating
  requires a cited basis.
- **C-12 strengthened** -- Nil findings require scope rationale; bare "none found" no longer
  sufficient.
- **Aspirational scoring**: PASS=2, PARTIAL=1, FAIL=0 per criterion. Band capped at 10.
  Uncapped max 14 across 7 criteria.

**v2 changes from v1:**

- **C-11 (new)** -- Confidence-annotated discovery catalog.
- **C-12 (new)** -- Nil-finding norm for gap sections.
- **C-13 (new)** -- Coverage accountability roster.
- **Aspirational scoring rebalanced**: C-09 and C-10 reduced from PASS=5 to PASS=2 to
  accommodate the growing aspirational tier without changing the band cap.
