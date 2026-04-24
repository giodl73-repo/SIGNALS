Written to `simulations/quest/rubrics/flow-conversation-rubric-v4-2026-03-15.md`.

---

**Two new criteria, two key decisions:**

**C-13 — Pre-Instruction Scoring Register** (from V-02)
The criteria table with "Full credit" / "Zero points" named examples placed *before* the first task instruction. The R3 primary discovery: this single mechanism satisfies both C-10 and C-11 simultaneously — the only variation across R2 and R3 to achieve two aspirational criteria via one structural choice. Pass requires: table precedes instructions, each row has a named zero-point example, no post-instruction positioning.

**C-14 — Per-Section Status-Quo Foil** (from V-01)
Every major section opens with "A first-pass X would say: '[specific text]'" before requirements. Deliberately distinguished from C-10: C-10 passes if one named prohibition exists anywhere in the prompt; C-14 requires the foil to *lead* each section, framing the requirement as the replacement for the bad form rather than just prohibiting it. Pass requires: >=4 sections, foil leads the section (not tails it), specific output instance not generic prohibition.

**Scoring model:** 115 → 125 max. Aspirational tier 5 → 7 criteria (25 → 35 pts). Essential and recommended unchanged.

**V-03 compression finding** produced no criterion — it's a validation result (mechanisms are load-bearing, scaffolding is not), not a new structural technique.
t). C-14 requires the named bad form to *lead* each major section, not to
appear in a central prohibition list or at section endings. The foil positions the
requirement as what the section exists to replace, not merely what it forbids.

**Scoring model update:** Max expands from 115 to 125. Aspirational tier grows from 5
criteria (25 pts) to 7 criteria (35 pts). Essential and recommended tiers are unchanged.

**V-03 compression finding (no new criterion):** R2 V-05's three mechanisms (MAY NOT exit
conditions, CS column headers, named bad forms) retained 115/115 at ~40% word count. This
confirms the mechanisms are the load-bearing elements; explanatory scaffolding is not
required for scoring. V-03 validates existing criteria are mechanism-dependent, not
verbosity-dependent. No new criterion is warranted.

### v3 -> v4: Round 3 validation

| Variation | Mechanisms | Score | New criteria reached |
|-----------|------------|-------|---------------------|
| V-01 Inertia Framing | Per-section status-quo foil | 105/115 | C-10 PASS, C-11 FAIL, C-12 FAIL |
| V-02 Scoring Register | Pre-instruction criteria table | 110/115 | C-10 PASS, C-11 PASS, C-12 FAIL |
| V-03 Minimalist Compression | R2 V-05 at ~40% word count | 115/115 | All 12 retained at ceiling |
| V-04 Inertia + Scoring Register | V-01 frame + V-02 table | (partial) | C-10 PASS, C-11 PASS expected |

C-13 derived from V-02. C-14 derived from V-01. Both are independent: V-01 achieves C-14
without C-13; V-02 achieves C-13 without C-14. A variation combining all five mechanisms
(phases + CS headers + named prohibitions + pre-instruction register + per-section foils)
is expected to reach 125/125.

---

## Scoring Model

| Tier | Pts per criterion | Criteria | Max pts |
|------|------------------|----------|---------|
| Essential | 15 | C-01 C-02 C-03 C-04 | 60 |
| Recommended | 10 | C-05 C-06 C-07 | 30 |
| Aspirational | 5 | C-08 C-09 C-10 C-11 C-12 C-13 C-14 | 35 |
| **Total** | | **14** | **125** |

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
  in context. Generic chatbot vocabulary ("intents", "slots", "utterances") used
  interchangeably with Copilot Studio terms without disambiguation does not satisfy
  this criterion on its own.

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
  not generic advice ("add better error handling").

---

### C-10 -- Named Failure-Mode Prohibition
- **Category:** behavior
- **Weight:** aspirational (5 pts)
- **Derived from:** R1 score delta -- V-04 achieving C-09 PASS; V-01/02/03 all PARTIAL
  because no example-level enforcement was present. R2 validated: V-01 (named prohibitions
  only) scored C-10 PASS at 105/115. R3 validated: V-01 (inertia framing), V-02 (scoring
  register), and V-03 (compressed) all PASS.
- **Text:** The prompt explicitly names a specific degenerate output pattern by instance
  and bans it. The banned example must identify the failure mode concretely (e.g.,
  "do not write 'add better error handling'") so the model can recognize and avoid the
  pattern. General specificity instructions ("be specific", "avoid vague advice") do not
  satisfy this criterion.
- **Pass condition:** At least one prohibited output pattern is named by example in the
  prompt or rubric. The named example must be a plausible output the model would
  otherwise produce. A criterion that only instructs the model to be specific without
  showing what non-specific looks like does not pass.

---

### C-11 -- Structural Domain-Vocabulary Enforcement
- **Category:** behavior
- **Weight:** aspirational (5 pts)
- **Derived from:** R1 score delta -- V-05 achieving C-08 PASS via column schema; V-02
  PARTIAL because generic headers ("User Input", "Bot Response") did not force CS labels
  per row. R2 validated: V-02 (CS column headers only) scored C-11 PASS at 105/115. R3
  validated: V-02 (scoring register) and V-03 (compressed) both PASS.
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
  explicit phase gates; V-01/V-02 getting PARTIAL on C-05/C-06/C-07 due to soft or absent
  exit conditions. R2 validated: V-03 (phase exit conditions only) scored C-12 PASS at
  105/115. R3 validated: V-03 (compressed) retains C-12 PASS at 115/115.
- **Text:** Each phase gate in the prompt includes an explicit exit condition that
  prevents degenerate completion. Exit conditions name the specific failure to block
  (e.g., "exit condition: defect scan MUST report at least one finding per defect type;
  MAY NOT exit with 'no issues found'"). Generic exit conditions ("when you are done",
  "when complete") do not satisfy this criterion.
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
  key property: no R2 variation achieved two aspirational criteria simultaneously.
- **Text:** The prompt contains a structured evaluation register -- a table or equivalent
  display listing scoreable criteria -- positioned before the first task section or phase.
  Each criterion row must pair at least one named full-credit example with at least one
  named zero-point example. The register's position before instructions sets the
  evaluation frame before the model encounters any task requirement.
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
  a section-opening foil structure. Each major section opened with "A first-pass X would
  say: '[specific inadequate text]'" before stating requirements. This is structurally
  distinct from C-10: C-10 requires only that at least one named prohibition exist
  anywhere in the prompt; C-14 requires a named bad-form lead to open each major section,
  framing the requirement as the alternative to a named inadequate pattern.
- **Text:** Each major output section in the prompt opens with an explicit named
  "status-quo" or "first-pass" bad-form example positioned before the section's
  requirements. The foil names a specific inadequate output (e.g., "A first-pass defect
  scan says: 'No significant issues found. Consider adding error handling.'") and frames
  the section's required output as what replaces it.
- **Pass condition:** At least four major output sections each open with a named bad-form
  foil lead positioned before the section's requirements. Each foil must be a specific
  output instance, not a generic prohibition ("do not be vague"). A foil appearing after
  requirements, or a single global prohibition preamble without per-section leads, does
  not pass.

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
