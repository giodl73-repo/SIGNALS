Written to `simulations/quest/rubrics/flow-conversation-rubric-v8-2026-03-15.md`.

---

**What changed v7 -> v8:**

Three new aspirational criteria from R8 excellence signals:

| New criterion | Source | Token | Independent from |
|---|---|---|---|
| **C-20 Remediation Verification Cycle** | R8 V-01 | `REMEDIATION_CYCLE_COMPLETE: BLOCKER_RESOLVED / BLOCKER_PERSISTS` | C-09 (spec vs. execution), C-17 (role-scoping vs. temporal), C-15 (predict-before vs. verify-after) |
| **C-21 Formula-Based Defect Severity** | R8 V-02 | `SEVERITY_GATE: DEPLOYABLE / HOLD` | C-18 (coverage ratios, not risk), C-02 (existence, not magnitude) |
| **C-22 Concurrent Session Interference** | R8 V-03 | `SESSION_ISOLATION_VERDICT: CLEAN / COLLISION` | C-02 (no concurrency class), C-05 (single-user), C-06 (sequential paths) |

**Scoring model:** 150 -> 165 max. Aspirational tier: 12 -> 15 criteria (60 -> 75 pts). Essential and Recommended unchanged.

**Predicted R8 scores on v8:**
- V-01, V-02, V-03 (single-mechanism): 155/165
- V-04 (C-20+C-21 combined): 160/165
- V-05 (all thirteen mechanisms): 165/165
cted path.

**C-21 -- Formula-Based Defect Severity** (from R8 V-02)
DEFECT_SEVERITY block applies a named formula (CRITICAL / HIGH / LOW tiers) per found
defect; SEVERITY_GATE: DEPLOYABLE / HOLD gates deployment on the absence of CRITICAL
findings. Not captured by C-18 (coverage completeness ratios, not defect risk
classification) or C-02 (found / not-found verdict per defect type, not severity
grading). Token: SEVERITY_GATE: DEPLOYABLE / HOLD. A prompt satisfying both can still
list every defect without assigning severity or blocking deployment on any finding.

**C-22 -- Concurrent Session Interference** (from R8 V-03)
Phase 3.5 CONCURRENT_SESSION_TRACE traces two simultaneous sessions through shared
nodes; SESSION_VARIABLE_CONFLICT: YES / NO per shared node; SESSION_ISOLATION_VERDICT:
CLEAN / COLLISION. Not captured by C-02 (four-type defect taxonomy has no concurrency
class), C-05 (single-user session variable tracking across turns, not multi-user
contention), or C-06 (structurally distinct sequential paths, not concurrent execution).
Token: SESSION_ISOLATION_VERDICT. A prompt satisfying all three can still produce no
concurrent trace and no conflict verdict.

**Scoring model:** 150 -> 165 max. Aspirational tier: 12 -> 15 criteria (60 -> 75 pts).
Essential and Recommended unchanged.

**Predicted R8 scores on v8:** Each single-mechanism R8 variation scores 155/165. The
ceiling variation combining all thirteen mechanisms: 165/165.

---

## Scoring Model

| Tier | Pts per criterion | Criteria | Max pts |
|------|------------------|----------|---------|
| Essential | 15 | C-01 C-02 C-03 C-04 | 60 |
| Recommended | 10 | C-05 C-06 C-07 | 30 |
| Aspirational | 5 | C-08 through C-22 | 75 |
| **Total** | | **22** | **165** |

**Composite score** = sum of per-criterion points for each PASS verdict.

**Golden threshold:** All 4 essential criteria PASS AND composite >= 80.

---

## Essential Criteria

### C-01 -- Dialog Path Traced
- **Category:** correctness
- **Weight:** essential (15 pts)
- **Text:** The artifact walks at least one complete dialog path from an entry intent to a
  terminal state, showing each turn as a discrete step with a named user intent and a
  named agent response.
- **Pass condition:** At minimum one path is traceable from start to end without gaps.
  Each step must show: (1) user utterance or intent label, (2) agent response or action,
  (3) resulting topic or state. A list of intents without turn-by-turn trace does not pass.

---

### C-02 -- Defect Report Present
- **Category:** correctness
- **Weight:** essential (15 pts)
- **Text:** The artifact contains an explicit defect report that either names at least one
  defect found (with location) or declares that a specific defect type was checked and
  none were found, for each of the four defect types: dead ends, infinite loops, intent
  collisions, missing fallbacks.
- **Pass condition:** All four defect types appear in the artifact, each with a verdict
  (found / not found). A generic "no issues" statement without per-type coverage does
  not pass. Vague "potential issues" without a type label does not pass.

---

### C-03 -- Intent-Response Pairing
- **Category:** correctness
- **Weight:** essential (15 pts)
- **Text:** Every turn in the traced dialog shows a paired user intent and agent response.
  Neither side is omitted.
- **Pass condition:** For every traced turn: user side (utterance, trigger phrase, or
  intent label) AND agent side (response text, action, or redirect) are both present.
  A turn showing only user utterance with no agent response, or only an agent response
  with no triggering intent, does not pass.

---

### C-04 -- Fallback Handling Shown
- **Category:** coverage
- **Weight:** essential (15 pts)
- **Text:** The artifact demonstrates what the agent does when no intent matches at least
  one topic node -- either by tracing a fallback path or by explicitly identifying the
  missing fallback as a defect.
- **Pass condition:** At least one topic node in the trace includes fallback behavior
  (the no-match branch). This may be a traced fallback path, a system topic redirect,
  or a missing-fallback defect entry. An artifact that only traces happy-path turns and
  omits all fallback handling does not pass.

---

## Recommended Criteria

### C-05 -- Session State Tracked
- **Category:** depth
- **Weight:** recommended (10 pts)
- **Text:** Session variables (slots, context variables, entity values) are named and
  their values shown at each turn where they change.
- **Pass condition:** At least two session variables are explicitly named and their
  values traced across the dialog. The artifact shows which turn sets each variable and
  which turns read it. An artifact that describes session state in the abstract without
  showing specific variable names and values does not pass.

---

### C-06 -- Multi-Path Coverage
- **Category:** coverage
- **Weight:** recommended (10 pts)
- **Text:** At least two structurally distinct dialog paths are traced: a happy path and
  at least one exception, fallback, or loop-exit path.
- **Pass condition:** Two paths are present and labeled distinctly. Each path must reach
  a different terminal outcome or branch at a different decision point. Two variations of
  the same happy path do not satisfy this criterion.

---

### C-07 -- Topic Graph Completeness
- **Category:** coverage
- **Weight:** recommended (10 pts)
- **Text:** The artifact names all topic nodes in the conversation graph and identifies
  which nodes were covered by the trace and which were not.
- **Pass condition:** A topic node inventory appears in the artifact (as a table, list,
  or inline coverage map). Each node is labeled traced or untraced. Nodes that are
  unreachable from the entry point are called out explicitly.

---

## Aspirational Criteria

### C-08 -- Copilot Studio Domain Vocabulary
- **Category:** behavior
- **Weight:** aspirational (5 pts)
- **Text:** The simulation uses Copilot Studio-specific terminology correctly throughout:
  topics, trigger phrases, system topics (Greeting, Fallback, Escalate), entities,
  condition branches, and redirect nodes.
- **Pass condition:** At least five Copilot Studio-specific terms are used correctly and
  in context. Generic chatbot vocabulary used interchangeably with Copilot Studio terms
  without disambiguation does not satisfy this criterion on its own.

---

### C-09 -- Actionable Remediation Per Defect
- **Category:** depth
- **Weight:** aspirational (5 pts)
- **Text:** Each identified defect includes a specific, implementable fix: where to add
  the missing fallback, which trigger phrase causes the collision and how to disambiguate,
  which redirect to add to break the loop, or which terminal state to add to close the
  dead end.
- **Pass condition:** Every defect entry in the defect report has a corresponding
  remediation. Remediations must be specific (name the node, topic, or phrase to change),
  not generic advice.

---

### C-10 -- Named Failure-Mode Prohibition
- **Category:** behavior
- **Weight:** aspirational (5 pts)
- **Derived from:** R1 score delta -- V-04 achieving C-09 PASS; V-01/02/03 all PARTIAL
  because no example-level enforcement was present. R2 validated: V-01 (named prohibitions
  only) scored C-10 PASS at 105/115. R3, R4, R5, R6, R7 validated. R8 validated: all
  five variations PASS.
- **Text:** The prompt explicitly names a specific degenerate output pattern by instance
  and bans it. The banned example must identify the failure mode concretely so the model
  can recognize and avoid the pattern. General specificity instructions ("be specific",
  "avoid vague advice") do not satisfy this criterion.
- **Pass condition:** At least one prohibited output pattern is named by example in the
  prompt or rubric. The named example must be a plausible output the model would
  otherwise produce. A criterion that only instructs the model to be specific without
  showing what non-specific looks like does not pass.

---

### C-11 -- Structural Domain-Vocabulary Enforcement
- **Category:** behavior
- **Weight:** aspirational (5 pts)
- **Derived from:** R1 score delta -- V-05 achieving C-08 PASS via column schema; V-02
  PARTIAL because generic headers did not force CS labels per row. R2 validated: V-02
  (CS column headers only) scored C-11 PASS at 105/115. R3, R4, R5, R6, R7, R8
  validated: all ceiling variations retain PASS.
- **Text:** Output tables use Copilot Studio-specific column headers (e.g.,
  "Copilot Studio Object to Edit", "Trigger Phrase", "Redirect Node") rather than generic
  labels ("Fix", "User Input", "Recommendation"). Vocabulary is enforced by the table
  schema itself, not only by role priming.
- **Pass condition:** At least one output table has a column whose header is a
  Copilot Studio-specific term. Role priming alone, without CS-labeled columns, does not
  pass. A column labeled "Fix" that merely permits CS vocabulary does not pass; the
  header must require it by being a CS term.

---

### C-12 -- Phase Exit Conditions Block Degenerate Completion
- **Category:** coverage
- **Weight:** aspirational (5 pts)
- **Derived from:** R1 score delta -- V-03/V-05 achieving full recommended-tier passes via
  explicit phase gates; V-01/V-02 getting PARTIAL due to soft or absent exit conditions.
  R2 validated: V-03 (phase exit conditions only) scored C-12 PASS at 105/115. R3
  validated at 115/115. R4 V-04 confirmed independence: removing C-12 while keeping
  C-13+C-14 drops score by 5. R5 V-04 re-confirmed. R6, R7, R8 validated: all
  variations PASS.
- **Text:** Each phase gate in the prompt includes an explicit exit condition that
  prevents degenerate completion. Exit conditions name the specific failure to block
  (e.g., "exit condition: defect scan MUST report at least one finding per defect type;
  MAY NOT exit with 'no issues found'"). Generic exit conditions do not satisfy this
  criterion.
- **Pass condition:** At least two phase gates have named exit conditions that identify
  a specific blocked degenerate output. The exit condition must be phrased as a hard
  constraint, not a suggestion. An exit condition that says "ensure completeness" without
  naming the failure mode does not pass.

---

### C-13 -- Pre-Instruction Scoring Register
- **Category:** behavior
- **Weight:** aspirational (5 pts)
- **Derived from:** R3 V-02 (Scoring Register) scoring 110/115 -- the first variation to
  achieve two aspirational criteria (C-10 and C-11) via a single mechanism. A criteria
  table placed before task instructions acts simultaneously as a prohibition list (C-10)
  and a vocabulary enforcement schema (C-11). R4 confirmed independence. R5, R6, R7, R8
  validated: all variations PASS.
- **Text:** The prompt contains a structured evaluation register -- a table or equivalent
  display listing scoreable criteria -- positioned before the first task section or phase.
  Each criterion row must pair at least one named full-credit example with at least one
  named zero-point example. The register sets the evaluation frame before the model
  encounters any task requirement.
- **Pass condition:** A structured criteria table appears before any task instruction.
  Each row names a criterion and provides a specific zero-point example (a plausible
  output the model would produce that earns no credit). A criteria list embedded inside
  task sections does not pass. A table without named zero-point examples does not pass.
  A table appearing after the first task instruction does not pass.

---

### C-14 -- Per-Section Status-Quo Foil
- **Category:** behavior
- **Weight:** aspirational (5 pts)
- **Derived from:** R3 V-01 (Inertia Framing) scoring 105/115 -- achieving C-10 PASS via
  a section-opening foil structure. Structurally distinct from C-10: C-10 requires only
  one named prohibition anywhere in the prompt; C-14 requires a named bad-form lead to
  open each major section. R4 confirmed independence. R5, R6, R7, R8 validated: all
  variations PASS.
- **Text:** Each major output section in the prompt opens with an explicit named
  status-quo or first-pass bad-form example positioned before the section requirements.
  The foil names a specific inadequate output and frames the section required output as
  what replaces it.
- **Pass condition:** At least four major output sections each open with a named bad-form
  foil lead positioned before the section requirements. Each foil must be a specific
  output instance, not a generic prohibition. A foil appearing after requirements, or a
  single global prohibition preamble without per-section leads, does not pass.

---

### C-15 -- Pre-Trace Defect Hypothesis
- **Category:** depth
- **Weight:** aspirational (5 pts)
- **Derived from:** R4 V-03 (Role Sequence Reversal, Defect-First) scoring 115/125 --
  the first variation to place a structured defect hypothesis phase before any trace
  phases. Not captured by C-01 through C-14. V-03 scores 115 (not 120+) because it
  lacks C-13 and C-14, not because its own mechanism adds no independent value. R5, R6,
  R7, R8 validated: all variations PASS.
- **Text:** The prompt requires the analyst to record, for each defect type, a predicted
  candidate location and a stated confidence or severity estimate before any trace phase
  begins. A final verdict phase must reconcile each hypothesis entry against the trace
  findings, noting whether the prediction was confirmed, refuted, or inconclusive.
- **Pass condition:** A hypothesis table (or equivalent structured section) appears before
  any trace phase. The table covers all four defect types. Each row names a predicted
  candidate location (a specific topic node or redirect name, not a generic area) and a
  confidence or severity level. A verdict or reconciliation section later in the artifact
  cross-references each hypothesis entry with a finding. A defect scan that only appears
  after tracing, without any pre-trace commitment to predicted locations, does not pass.
  A hypothesis table that lists defect types without predicted locations does not pass.

---

### C-16 -- Cross-Mechanism Prohibition Convergence
- **Category:** behavior
- **Weight:** aspirational (5 pts)
- **Derived from:** R5 V-05 C-10 evidence: "Register zero-points name specific banned
  outputs; per-section foils name additional bad-form patterns; phase exit conditions name
  specific blocked phrases -- three independent reinforcing sources." C-16 is PASS only
  when C-12, C-13, and C-14 all pass AND each structure names prohibition content not
  present in either of the other two. R6, R7, R8 validated: all variations PASS.
- **Text:** Named prohibition coverage is distributed across all three enforcement
  structures simultaneously -- pre-instruction register zero-point examples, per-section
  foil leads, and phase exit MAY NOT gates -- with each structure naming at least one
  specific degenerate output pattern not named by the other two. Prohibition content is
  non-redundant across structures.
- **Pass condition:** All three enforcement structures are present (C-12 PASS, C-13 PASS,
  C-14 PASS) and each independently names at least one prohibited output that does not
  appear in either of the other two structures. Verification: identify at least one
  structure-unique prohibition per mechanism. Repeating the same named prohibition across
  all three structures without adding structure-specific patterns does not pass. C-12,
  C-13, or C-14 failing automatically causes C-16 to fail.

---

### C-17 -- Role-Independent Verification
- **Category:** depth
- **Weight:** aspirational (5 pts)
- **Derived from:** R6 V-01 (Two-Role Split: FLOW ANALYST + FLOW AUDITOR). V-01 assigns
  Phases 1-4 to a named ANALYST role and Phase 5 to a named AUDITOR role. The AUDITOR
  explicitly asserts it did not author any prior phase. VERIFICATION_VERDICT: CHALLENGED
  is a structurally new completion token: a named discrepancy signal that only exists when
  two independent roles can disagree. Not captured by C-02, C-09, or C-15. R7, R8
  validated: all five variations PASS.
- **Text:** The prompt assigns analysis and verification to two explicitly named roles
  scoped to disjoint phase sets. The verification role explicitly asserts it did not author
  the analysis phases. A named discrepancy verdict token (e.g., VERIFICATION_VERDICT:
  CHALLENGED) is defined and enforced: the verification role MUST emit this token when
  it disputes an analysis finding, and a phase exit condition prohibits confirming all
  findings without independent evidence per finding.
- **Pass condition:** (1) Two named roles are defined and scoped to disjoint phases
  (analysis phases vs. verification phase). (2) The verification role's instructions
  include an explicit non-authorship assertion for analysis phases. (3) A named
  discrepancy verdict token is defined and available to the verification role. (4) At
  least one phase exit condition prohibits the verification role from emitting a blanket
  confirmation without citing a specific turn number or topic node per finding. A
  simulation using one role throughout, or a second role that only summarizes the first
  role's output without a discrepancy pathway, does not pass.

---

### C-18 -- Quantitative Coverage Threshold
- **Category:** coverage
- **Weight:** aspirational (5 pts)
- **Derived from:** R6 V-02 (Quantitative Coverage Ratios). V-02 emits a Coverage Metrics
  block computing topic_coverage_ratio, fallback_coverage_ratio, and
  intent_collision_density, gated by COVERAGE_GATE: CLEAN / DEGRADED. The gate requires
  topic_coverage_ratio >= 0.70 AND fallback_coverage_ratio >= 0.50. Independent from
  C-07 (qualitative traced/untraced labels; no threshold computation required) and C-12
  (phase exit conditions that block named failure-mode phrases, not below-threshold
  numeric results). R7, R8 validated: all five variations PASS.
- **Text:** The prompt requires at least two named numeric coverage ratios to be computed
  and reported (e.g., topic_coverage_ratio, fallback_coverage_ratio). Each ratio must
  have an explicit minimum threshold. A named gate token (e.g., COVERAGE_GATE:
  CLEAN / DEGRADED) must be emitted whose PASS verdict is logically conditioned on all
  named thresholds being met. At least one phase exit condition must prohibit emitting the
  gate as CLEAN without computing and stating both ratios numerically.
- **Pass condition:** (1) At least two named coverage ratios are defined with explicit
  numeric minimum thresholds. (2) A named binary gate token is defined whose CLEAN / PASS
  state requires all thresholds to be satisfied. (3) A phase exit condition explicitly
  prohibits emitting the gate as CLEAN without computing and reporting the numeric ratios.
  A qualitative coverage label ("adequate", "sufficient") without a numeric ratio does not
  pass. A phase exit condition that only blocks a named bad phrase without requiring ratio
  computation does not pass.

---

### C-19 -- Detection Gap Audit
- **Category:** depth
- **Weight:** aspirational (5 pts)
- **Derived from:** R6 V-03 (Status Quo Simulation). V-03 inserts a Phase 0
  STATUS_QUO_TRACE that generates an actual inferior simulation under explicitly
  constrained conditions (keyword-match only, 3 turns, no condition branches, no redirect
  nodes, no session variable tracking) before the full-fidelity trace phases. Phase 5
  computes a STATUS_QUO_COMPARISON block with per-defect STATUS_QUO_BLIND_SPOT: YES / NO.
  Independent from C-14 (static bad-form foil; Phase 0 generates a live trace output) and
  C-15 (predict-then-verify for defect locations within one method; Phase 0 is a
  method-comparison). R7, R8 validated: all five variations PASS.
- **Text:** The prompt requires a Phase 0 section that generates an actual simulation
  trace under explicitly constrained inferior conditions. The constraints must name at
  least one structural CS mechanism excluded from Phase 0 that is present in the main
  trace phases. A comparison block in the final phase must read the Phase 0 output
  per-defect type and emit an explicit blind-spot verdict (STATUS_QUO_BLIND_SPOT: YES / NO
  or equivalent) per defect type found in the full trace. A phase exit condition must
  prohibit declaring the comparison complete without one verdict row per found defect type.
- **Pass condition:** (1) A Phase 0 section is defined that generates a live simulation
  trace under named inferior constraints (at least one named exclusion of a CS mechanism
  present in the main trace). (2) A comparison block in the final phase cross-references
  Phase 0 output against Phase 5 defect findings per defect type, emitting an explicit
  blind-spot verdict per defect type found. (3) A phase exit condition prohibits declaring
  the comparison complete without one verdict row per found defect type. A static bad-form
  foil (prompt text only, no live trace generated) does not pass. A comparison that only
  notes "Phase 0 was less detailed" without per-defect blind-spot verdicts does not pass.

---

### C-20 -- Remediation Verification Cycle
- **Category:** depth
- **Weight:** aspirational (5 pts)
- **Derived from:** R8 V-01 (Remediation Verification Cycle). V-01 adds a Phase 6
  REMEDIATION_VERIFICATION_CYCLE triggered conditionally when Phase 5 emits BLOCKER: Yes
  for any defect. Phase 6 re-simulates the affected dialog path after the specified fix
  is applied and emits REMEDIATION_CYCLE_COMPLETE: BLOCKER_RESOLVED / BLOCKER_PERSISTS.
  This is structurally independent from C-09 (names the exact fix required -- specifying
  what to change; Phase 6 executes a re-trace after the change is applied -- specification
  vs. execution), C-17 (assigns independent roles to disjoint phases within a single
  analysis pass; Phase 6 is a temporal extension -- verify-after-remediation -- not a
  role-scoping mechanism; a single analyst can perform Phase 6), and C-15 (commits to a
  defect location prediction before any trace begins; Phase 6 begins only after a defect
  has been confirmed and a fix specified). A prompt satisfying all three can still specify
  a fix, emit a remediation recommendation, and close the defect report without re-tracing
  the affected path.
- **Text:** The prompt defines a Phase 6 (or equivalent) REMEDIATION_VERIFICATION_CYCLE
  that is conditionally triggered when at least one Phase 5 defect finding is classified
  as BLOCKER: Yes. Phase 6 must re-simulate the affected dialog path under the condition
  that the specified fix has been applied, and must emit a named binary verdict token
  (REMEDIATION_CYCLE_COMPLETE: BLOCKER_RESOLVED / BLOCKER_PERSISTS or equivalent). At
  least one phase exit condition must prohibit emitting BLOCKER_RESOLVED without
  re-tracing at least one turn of the affected path.
- **Pass condition:** (1) A post-remediation re-simulation phase is defined and
  conditionally triggered by a BLOCKER: Yes verdict in the defect report phase. (2) The
  phase re-traces the affected path (at least one turn) under the assumption the fix is
  applied. (3) A named binary completion token is defined distinguishing BLOCKER_RESOLVED
  from BLOCKER_PERSISTS. (4) A phase exit condition prohibits emitting BLOCKER_RESOLVED
  without a re-traced turn confirming resolution. A prompt that only specifies the fix
  without re-simulating the path does not pass. A generic "verify the fix was applied"
  instruction without a re-trace and named verdict token does not pass.

---

### C-21 -- Formula-Based Defect Severity
- **Category:** depth
- **Weight:** aspirational (5 pts)
- **Derived from:** R8 V-02 (Formula-Based Defect Severity). V-02 adds a DEFECT_SEVERITY
  block that applies a named formula -- CRITICAL (blocking, conversation-ending defect),
  HIGH (material degradation, incorrect response), LOW (style or minor gap) -- per found
  defect. A named deployment gate SEVERITY_GATE: DEPLOYABLE / HOLD is emitted, where
  HOLD is required if any CRITICAL finding exists. This is structurally independent from
  C-18 (computes coverage completeness ratios to gate adequacy of node coverage; severity
  of a found defect is a different dimension from how many nodes were reached -- a fully
  covered conversation can still have a CRITICAL defect at every node) and C-02 (emits a
  found / not-found verdict per defect type; found / not-found is existence, not risk
  magnitude; a prompt passing C-02 can list every defect without assigning severity or
  blocking deployment). A prompt satisfying both C-02 and C-18 can still lack any
  severity classification and any deployment gate.
- **Text:** The prompt requires a DEFECT_SEVERITY block (or equivalent structured section)
  that assigns a named severity tier (at minimum: a CRITICAL-equivalent and at least one
  lower tier) to every defect found in the Phase 5 report. The severity assignment must
  follow an explicit named formula tied to impact type (e.g., conversation termination,
  incorrect routing, degraded response). A named binary deployment gate token
  (SEVERITY_GATE: DEPLOYABLE / HOLD or equivalent) must be defined, whose HOLD verdict is
  logically required when at least one CRITICAL-tier finding exists. At least one phase
  exit condition must prohibit emitting the gate as DEPLOYABLE without computing severity
  for every found defect.
- **Pass condition:** (1) A named severity formula is defined with at least two tiers,
  one of which is a CRITICAL-equivalent that blocks deployment. (2) Every defect finding
  in the defect report receives an explicit severity tier assignment under the formula.
  (3) A named binary gate token is defined whose HOLD state is triggered by any CRITICAL
  finding. (4) A phase exit condition prohibits emitting the gate as DEPLOYABLE without
  assigning severity to every found defect. A defect report that lists findings without
  severity tiers does not pass. A qualitative severity note ("this is a serious issue")
  without a named tier formula does not pass.

---

### C-22 -- Concurrent Session Interference
- **Category:** depth
- **Weight:** aspirational (5 pts)
- **Derived from:** R8 V-03 (Concurrent Session Trace). V-03 adds a Phase 3.5
  CONCURRENT_SESSION_TRACE that traces two simultaneous sessions (Session A and Session B)
  through shared conversation nodes in parallel. For each shared node, the trace emits
  SESSION_VARIABLE_CONFLICT: YES / NO. A SESSION_ISOLATION_VERDICT: CLEAN / COLLISION is
  emitted for the full concurrent trace. This is structurally independent from C-02
  (defect taxonomy covers dead ends, infinite loops, intent collisions, and missing
  fallbacks -- none of these are concurrency defects; a session variable collision between
  concurrent users is not captured by any of the four types), C-05 (tracks session
  variable values as they change across turns for a single user; multi-user contention
  for a shared variable cannot occur in a single-user trace), and C-06 (traces
  structurally distinct sequential paths that branch at decision points; two concurrent
  sessions executing in parallel through the same node is not a sequential path variation).
  A prompt satisfying all three can still produce no concurrent trace and no per-node
  conflict verdict.
- **Text:** The prompt requires a Phase 3.5 (or equivalent interstitial phase) that
  traces two simultaneous user sessions concurrently through at least one shared
  conversation node. For each shared node, the trace must emit an explicit conflict
  verdict (SESSION_VARIABLE_CONFLICT: YES / NO or equivalent) identifying whether a
  session variable value set by one session could be overwritten or misread by the other.
  A named session isolation verdict token (SESSION_ISOLATION_VERDICT: CLEAN / COLLISION
  or equivalent) must summarize the concurrent trace. At least one phase exit condition
  must prohibit declaring the concurrent trace complete without one conflict verdict per
  shared node.
- **Pass condition:** (1) A concurrent session trace phase is defined that simulates two
  sessions simultaneously through at least one shared node. (2) Each shared node receives
  an explicit per-node conflict verdict (YES / NO for session variable conflict). (3) A
  named binary summary verdict token is defined distinguishing CLEAN from COLLISION.
  (4) A phase exit condition prohibits declaring the concurrent trace complete without one
  conflict verdict per shared node. A single-user trace that notes "concurrent use is
  possible" without actually tracing two sessions does not pass. A conflict discussion
  in the defect report without a per-node conflict verdict table does not pass.

---

## Criterion Summary

| ID | Text (short) | Tier | Pts | Category | Pass condition (short) |
|----|-------------|------|-----|----------|------------------------|
| C-01 | Dialog path traced | essential | 15 | correctness | Complete turn-by-turn path, entry to terminal |
| C-02 | Defect report present | essential | 15 | correctness | All 4 defect types checked with verdict |
| C-03 | Intent-response pairing | essential | 15 | correctness | Both sides present in every turn |
| C-04 | Fallback handling shown | essential | 15 | coverage | At least one no-match branch traced or flagged |
| C-05 | Session state tracked | recommended | 10 | depth | >=2 named variables traced across turns |
| C-06 | Multi-path coverage | recommended | 10 | coverage | Happy path + >=1 exception/fallback path |
| C-07 | Topic graph completeness | recommended | 10 | coverage | Inventory of nodes with traced/untraced labels |
| C-08 | Copilot Studio vocabulary | aspirational | 5 | behavior | >=5 CS-specific terms used correctly in context |
| C-09 | Actionable remediation | aspirational | 5 | depth | Specific fix per defect, not generic advice |
| C-10 | Named failure-mode prohibition | aspirational | 5 | behavior | >=1 degenerate output named by example and banned |
| C-11 | Structural domain-vocab enforcement | aspirational | 5 | behavior | >=1 output table column header is a CS-specific term |
| C-12 | Phase exit conditions block collapse | aspirational | 5 | coverage | >=2 phase gates with hard exit conditions naming the blocked failure |
| C-13 | Pre-instruction scoring register | aspirational | 5 | behavior | Criteria table with named zero-point examples precedes first task instruction |
| C-14 | Per-section status-quo foil | aspirational | 5 | behavior | >=4 sections open with a named bad-form foil before requirements |
| C-15 | Pre-trace defect hypothesis | aspirational | 5 | depth | Hypothesis table for all 4 defect types with predicted locations precedes trace phases; verdict section reconciles predictions against findings |
| C-16 | Cross-mechanism prohibition convergence | aspirational | 5 | behavior | C-12+C-13+C-14 all PASS; each structure names >=1 structure-unique prohibited output not present in either other structure |
| C-17 | Role-independent verification | aspirational | 5 | depth | Two named roles scoped to disjoint phases; verification role asserts non-authorship; named discrepancy token defined; exit condition prohibits blanket confirmation without per-finding evidence |
| C-18 | Quantitative coverage threshold | aspirational | 5 | coverage | >=2 named coverage ratios with numeric thresholds; named binary gate token; exit condition prohibits CLEAN without computing ratios |
| C-19 | Detection gap audit | aspirational | 5 | depth | Phase 0 live inferior trace under named constraints; final-phase per-defect blind-spot verdict; exit condition prohibits incomplete comparison |
| C-20 | Remediation verification cycle | aspirational | 5 | depth | Post-remediation re-simulation phase triggered by BLOCKER: Yes; re-traces affected path; named BLOCKER_RESOLVED/BLOCKER_PERSISTS token; exit condition prohibits BLOCKER_RESOLVED without re-traced turn |
| C-21 | Formula-based defect severity | aspirational | 5 | depth | Named severity formula with >=2 tiers including CRITICAL-equivalent; every found defect assigned a tier; named DEPLOYABLE/HOLD gate; exit condition prohibits DEPLOYABLE without severity assignment |
| C-22 | Concurrent session interference | aspirational | 5 | depth | Phase 3.5 concurrent 2-session trace through shared nodes; per-node SESSION_VARIABLE_CONFLICT verdict; named CLEAN/COLLISION summary token; exit condition prohibits completion without per-node verdict |

---

## Validation History

### v1 -> v2: Round 1 score delta

C-10 derived from V-04 achieving C-09 PASS; V-01/V-02/V-03 all PARTIAL because no
example-level enforcement was present. Named prohibitions yield measurable delta at R1.

### v2 -> v3: Round 2 validation

| Variation | Mechanisms | Score | Notes |
|-----------|------------|-------|-------|
| V-01 Named prohibitions only | Prohibitions, no phase gates | 105/115 | C-10 PASS, C-11 FAIL, C-12 FAIL |
| V-02 CS column headers only | Column headers, no prohibitions | 105/115 | C-10 FAIL, C-11 PASS, C-12 FAIL |
| V-03 Phase exit conditions only | Phase gates, no prohibitions | 105/115 | C-10 FAIL, C-11 FAIL, C-12 PASS |
| V-04 All three mechanisms | Prohibitions + headers + phases | 115/115 | C-10 PASS, C-11 PASS, C-12 PASS |

C-11 derived from V-02. C-12 derived from V-03. Each mechanism independently
contributes 5 pts -- no criterion is redundant with another.

### v3 -> v4: Round 3 validation

| Variation | Mechanisms | Score | Notes |
|-----------|------------|-------|-------|
| V-01 Inertia Framing | Per-section foils, no register | 105/120 | C-13 FAIL, C-14 PASS |
| V-02 Scoring Register | Pre-instruction register, no foils | 110/120 | C-13 PASS, C-14 FAIL |
| V-03 Compressed | All R2 mechanisms, shorter prose | 115/120 | C-13 FAIL, C-14 FAIL -- no new criterion |
| V-04 Register + Foils | Register + foils, no R2 changes | 115/120 | C-13 PASS, C-14 PASS, C-12 FAIL |
| V-05 Full Ceiling | All five mechanisms | 120/120 | All 13 at ceiling |

C-13 derived from V-02. C-14 derived from V-01. V-03 (compression) confirmed criteria
are mechanism-dependent, not verbosity-dependent -- no new criterion warranted.

### v4 -> v5: Round 4 validation

| Variation | Mechanisms | Score | Notes |
|-----------|------------|-------|-------|
| V-01 Pre-Instruction Register Only | C-13 table, no per-section foils | 120/125 | C-13 PASS, C-14 FAIL -- confirms C-13 independence |
| V-02 Per-Section Foil Only | C-14 foils, no pre-instruction register | 120/125 | C-14 PASS, C-13 FAIL -- confirms C-14 independence |
| V-03 Role Sequence Reversal (Defect-First) | Defect hypothesis before traces | 115/125 | C-13 FAIL, C-14 FAIL -- new mechanism discovered |
| V-04 C-13 + C-14 Without Phase Gates | Register + foils, C-12 removed | 120/125 | C-12 FAIL -- confirms C-12 independence from C-13/C-14 |
| V-05 Full Ceiling (All Five Mechanisms) | Phases + CS headers + named prohibitions + register + foils | 125/125 | All 14 retained at ceiling |

C-15 derived from V-03. The defect-first role sequence reversal introduces a
predict-then-verify structure not captured by any C-01 through C-14 criterion.

### v5 -> v6: Round 5 validation

| Variation | Mechanisms | Score | Notes |
|-----------|------------|-------|-------|
| V-01 C-15 Only: Pre-Trace Hypothesis | C-15, C-12, C-11, C-10. No C-13, no C-14 | 120/130 | C-13 FAIL, C-14 FAIL -- confirms C-15 independence |
| V-02 C-15 + C-13: Hypothesis + Register | C-13, C-15, C-12, C-11, C-10. No C-14 | 125/130 | C-14 FAIL -- confirms C-13+C-15 additive |
| V-03 C-15 + C-14: Hypothesis + Foils | C-14, C-15, C-12, C-11, C-10. No C-13 | 125/130 | C-13 FAIL -- confirms C-14+C-15 additive |
| V-04 C-15 + C-13 + C-14 Without Phase Gates | C-13, C-14, C-15, C-11, C-10. C-12 removed | 125/130 | C-12 FAIL -- confirms C-12 independence from C-13/C-14 |
| V-05 Full Ceiling: All Six Mechanisms | C-13, C-14, C-15, C-12, C-11, C-10 | 130/130 | All 15 retained at ceiling |

C-16 derived from V-05 C-10 evidence: when all three prohibition-delivery structures
coexist, each independently contributes non-redundant named degenerate patterns.

### v6 -> v7: Round 6 validation

| Variation | Mechanisms | Score | Notes |
|-----------|------------|-------|-------|
| V-01 Two-Role Split | All R6 + ANALYST/AUDITOR split | 135/135 | C-17 candidate: role_independent_verification |
| V-02 Quantitative Coverage | All R6 + coverage ratios + COVERAGE_GATE | 135/135 | C-18 candidate: quantitative_coverage_threshold |
| V-03 Status Quo Simulation | All R6 + Phase 0 STATUS_QUO_TRACE + BLIND_SPOT | 135/135 | C-19 candidate: detection_gap_audit |

All three variations score 135/135 on v6 (full carryover confirmed). C-17, C-18, and
C-19 derived from V-01, V-02, and V-03 respectively.

### v7 -> v8: Round 7 baseline + Round 8 validation

**Round 7 -- v7 baseline confirmation:**

All five R7 variations confirmed 150/150 on v7. Full mechanism carryover from R6
confirmed. V-05 (all ten mechanisms) established as the R7 ceiling.

**Round 8 -- new mechanism isolation:**

| Variation | New mechanism | C-20 | C-21 | C-22 | v7 score | v8 score |
|-----------|--------------|------|------|------|----------|----------|
| V-01 Remediation Verification Cycle | Phase 6 re-simulation on BLOCKER: Yes | PASS | FAIL | FAIL | 150/150 | 155/165 |
| V-02 Formula-Based Defect Severity | DEFECT_SEVERITY formula + SEVERITY_GATE | FAIL | PASS | FAIL | 150/150 | 155/165 |
| V-03 Concurrent Session Trace | Phase 3.5 + SESSION_ISOLATION_VERDICT | FAIL | FAIL | PASS | 150/150 | 155/165 |
| V-04 C-20+C-21 Combined | Phase 6 + DEFECT_SEVERITY coexist | PASS | PASS | FAIL | 150/150 | 160/165 |
| V-05 Full Ceiling | All thirteen mechanisms | PASS | PASS | PASS | 150/150 | 165/165 |

C-20 derived from R8 V-01. C-21 derived from R8 V-02. C-22 derived from R8 V-03.
V-04 additivity confirmed: BLOCKER-classified CRITICAL defect triggers both severity
gate and remediation re-trace independently -- BLOCKER_RESOLVED and SEVERITY_GATE:
HOLD are independently attributable. V-05 full ceiling confirmed: all three new tokens
(REMEDIATION_CYCLE_COMPLETE, SEVERITY_GATE, SESSION_ISOLATION_VERDICT) independently
attributable; coverage table extended with Session A/B columns from Phase 3.5;
DEFECT_SEVERITY formula extended to classify SESSION_ISOLATION COLLISION at HIGH tier
for nodes with >1 incoming redirect.
