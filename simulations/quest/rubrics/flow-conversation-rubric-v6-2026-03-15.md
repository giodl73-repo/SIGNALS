Written to `simulations/quest/rubrics/flow-conversation-rubric-v6-2026-03-15.md`.

---

**What changed v5 → v6:**

**C-16 — Cross-Mechanism Prohibition Convergence** (from R5 V-05)

The one new criterion. V-05's full-ceiling evidence for C-10 explicitly names *"three independent reinforcing sources"* — register zero-points, per-section foils, and phase exit conditions each naming **distinct** specific degenerate patterns. This is structurally independent of C-10 (which only requires one prohibition anywhere), C-12, C-13, and C-14 (which each require their mechanism to be present without mandating non-redundant content across mechanisms).

C-16 can only PASS when C-12 + C-13 + C-14 all pass AND each structure contributes prohibition content not repeated in the other two. V-01 through V-04 each have at most two active prohibition-delivery structures — none can satisfy C-16.

**Scoring model:** 130 → 135 max. Aspirational tier: 8 → 9 criteria (40 → 45 pts). Essential and recommended unchanged.

**Expected ceiling variation:** All seven mechanisms combined → 135/135.

**Predicted Round 6 scores using v6:**

| Variation | C-16 | Predicted score |
|-----------|------|-----------------|
| V-01 (C-15 only) | FAIL | 120/135 |
| V-02 (C-15+C-13) | FAIL | 125/135 |
| V-03 (C-15+C-14) | FAIL | 125/135 |
| V-04 (C-15+C-13+C-14, no C-12) | FAIL | 125/135 |
| V-05 (all six) | PASS | 135/135 |
/115 | C-10 PASS, C-11 PASS, C-12 PASS |

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
predict-then-verify structure (hypothesis table before any trace phases) not captured
by any C-01 through C-14 criterion. V-03 scores 115 because it lacks C-13 and C-14,
not because its own mechanism adds no independent value.

### v5 -> v6: Round 5 validation

| Variation | Mechanisms | Score | Notes |
|-----------|------------|-------|-------|
| V-01 C-15 Only: Pre-Trace Hypothesis | C-15, C-12, C-11, C-10. No C-13, no C-14 | 120/130 | C-13 FAIL, C-14 FAIL -- confirms C-15 independence |
| V-02 C-15 + C-13: Hypothesis + Register | C-13, C-15, C-12, C-11, C-10. No C-14 | 125/130 | C-14 FAIL -- confirms C-13+C-15 additive |
| V-03 C-15 + C-14: Hypothesis + Foils | C-14, C-15, C-12, C-11, C-10. No C-13 | 125/130 | C-13 FAIL -- confirms C-14+C-15 additive |
| V-04 C-15 + C-13 + C-14 Without Phase Gates | C-13, C-14, C-15, C-11, C-10. C-12 removed | 125/130 | C-12 FAIL -- confirms C-12 independence from C-13/C-14 |
| V-05 Full Ceiling: All Six Mechanisms | C-13, C-14, C-15, C-12, C-11, C-10 | 130/130 | All 15 retained at ceiling |

C-16 derived from V-05 C-10 evidence: "Register zero-points name specific banned
outputs; per-section foils name additional bad-form patterns; phase exit conditions
name specific blocked phrases -- three independent reinforcing sources." When all three
prohibition-delivery structures coexist, each independently contributes non-redundant
named degenerate patterns. V-01 through V-04 each have at most two prohibition-delivery
structures active simultaneously; none can achieve C-16. A variation combining all seven
mechanisms is expected to reach 135/135.

**Scoring model:** 130 -> 135 max. Aspirational tier: 8 -> 9 criteria (40 -> 45 pts).
Essential and recommended unchanged.

**Expected ceiling variation:** All seven mechanisms combined (phases + CS headers +
named prohibitions + pre-instruction register + per-section foils + pre-trace hypothesis
+ cross-mechanism prohibition convergence) -> 135/135.

---

## Scoring Model

| Tier | Pts per criterion | Criteria | Max pts |
|------|------------------|----------|---------|
| Essential | 15 | C-01 C-02 C-03 C-04 | 60 |
| Recommended | 10 | C-05 C-06 C-07 | 30 |
| Aspirational | 5 | C-08 C-09 C-10 C-11 C-12 C-13 C-14 C-15 C-16 | 45 |
| **Total** | | **16** | **135** |

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
  only) scored C-10 PASS at 105/115. R3 validated: inertia framing, scoring register, and
  compressed variations all PASS. R4 validated across all five variations. R5 validated
  across all five variations; V-05 evidence notes three independent reinforcing sources
  each contributing non-redundant named patterns.
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
  (CS column headers only) scored C-11 PASS at 105/115. R3, R4, and R5 validated: all
  ceiling variations retain PASS.
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
  C-13+C-14 drops score by 5. R5 V-04 re-confirmed: C-13+C-14+C-15 without C-12 scores
  125/130 (C-12 FAIL).
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
  and a vocabulary enforcement schema (C-11). The pre-instruction temporal position is the
  key property: no R2 variation achieved two aspirational criteria simultaneously. R4
  confirmed independence: V-01 (register only) achieves 120/125, C-14 FAIL. R5 confirmed:
  V-02 (C-15+C-13, no C-14) achieves 125/130.
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
  open each major section, framing the requirement as the alternative to a named
  inadequate pattern. R4 confirmed independence: V-02 (foils only) achieves 120/125,
  C-13 FAIL. R5 confirmed: V-03 (C-15+C-14, no C-13) achieves 125/130.
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
  phases. V-03 passes all C-01 through C-12 via this structure alone, demonstrating the
  mechanism is independently sufficient for those criteria. The predict-then-verify
  structure is not captured by any existing criterion: C-02 requires a defect report
  after tracing; C-15 requires a hypothesis committed before evidence is gathered, with
  a reconciliation verdict after. V-03 scores 115 (not 120+) because it lacks C-13 and
  C-14, not because its own mechanism adds no independent value. R5 confirmed across all
  five variations: V-01 achieves 120/130 with C-15 as the sole new mechanism; V-05
  achieves 130/130 with all six mechanisms.
- **Text:** The prompt requires the analyst to record, for each defect type, a predicted
  candidate location and a stated confidence or severity estimate before any trace phase
  begins. A final verdict phase must reconcile each hypothesis entry against the trace
  findings, noting whether the prediction was confirmed, refuted, or inconclusive. This
  enforces a predict-then-verify arc across the artifact rather than a trace-then-label
  arc.
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
  specific blocked phrases -- three independent reinforcing sources." When all three
  prohibition-delivery structures (pre-instruction register, per-section foils, phase exit
  conditions) coexist, each independently contributes non-redundant named degenerate
  patterns. V-01 through V-04 each have at most two prohibition-delivery structures active
  simultaneously; none can achieve C-16. C-16 is PASS only when C-12, C-13, and C-14 all
  pass AND each structure names prohibition content not present in either of the other two.
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
