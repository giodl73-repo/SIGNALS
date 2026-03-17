Written to `simulations/quest/rubrics/flow-conversation-rubric-v2-2026-03-15.md`.

---

## What changed and why

**Three new aspirational criteria, derived directly from score deltas:**

**C-10 — Named failure-mode prohibition (5 pts)**
The delta between V-04 (C-09 PASS) and V-01/02/03 (all PARTIAL) was not about asking for specificity — it was about naming the specific bad output and banning it by instance. "Do not write 'add better error handling'" is qualitatively different from "be specific." This criterion captures that technique.

**C-11 — Structural domain-vocabulary enforcement (5 pts)**
V-02 got C-08 PARTIAL because generic column headers ("User Input", "Bot Response") don't force CS vocabulary — they only allow it. V-05 got PASS because "Copilot Studio Object to Edit" as a column header makes every row in that column a CS artifact by construction. Role priming is soft; column schema is structural. This criterion rewards the structural approach.

**C-12 — Phase exit conditions block degenerate completion (5 pts)**
V-01/V-02 got PARTIAL on C-05/C-06/C-07 because phases with soft or absent exit conditions leave the model free to collapse ("no issues found", shallow divergence). V-03/V-05 passed all three by requiring hard exit conditions that name the blocked failure. This criterion makes that technique explicit and scoreable.

**Scoring model update:**
Max expands from 100 → 115 (aspirational tier: 2 × 5 → 5 × 5). Golden threshold stays at ≥ 80 — it was calibrated to the V-01 baseline of 82.5, which remains a meaningful floor. The composite formula simplifies to per-criterion point multiplication, no fractions.
rn trace does not pass.

---

### C-02 — Defect Report Present
- **Category:** correctness
- **Weight:** essential
- **Text:** The artifact contains an explicit defect report that either names at least one
  defect found (with location) or declares that a specific defect type was checked and
  none were found, for each of the four defect types: dead ends, infinite loops, intent
  collisions, missing fallbacks.
- **Pass condition:** All four defect types appear in the artifact, each with a verdict
  (found / not found). A generic "no issues" statement without per-type coverage does
  not pass. Vague "potential issues" without a type label does not pass.

---

### C-03 — Intent–Response Pairing
- **Category:** correctness
- **Weight:** essential
- **Text:** Every turn in the traced dialog shows a paired user intent and agent response.
  Neither side is omitted.
- **Pass condition:** For every traced turn: user side (utterance, trigger phrase, or
  intent label) AND agent side (response text, action, or redirect) are both present.
  A turn showing only user utterance with no agent response, or only an agent response
  with no triggering intent, does not pass.

---

### C-04 — Fallback Handling Shown
- **Category:** coverage
- **Weight:** essential
- **Text:** The artifact demonstrates what the agent does when no intent matches at least
  one topic node — either by tracing a fallback path or by explicitly identifying the
  missing fallback as a defect.
- **Pass condition:** At least one topic node in the trace includes fallback behavior
  (the no-match branch). This may be a traced fallback path, a system topic redirect,
  or a missing-fallback defect entry. An artifact that only traces happy-path turns and
  omits all fallback handling does not pass.

---

## Recommended Criteria

### C-05 — Session State Tracked
- **Category:** depth
- **Weight:** recommended
- **Text:** Session variables (slots, context variables, entity values) are named and
  their values shown at each turn where they change.
- **Pass condition:** At least two session variables are explicitly named and their
  values traced across the dialog. The artifact shows which turn sets each variable and
  which turns read it. An artifact that describes session state in the abstract without
  showing specific variable names and values does not pass.

---

### C-06 — Multi-Path Coverage
- **Category:** coverage
- **Weight:** recommended
- **Text:** At least two structurally distinct dialog paths are traced: a happy path and
  at least one exception, fallback, or loop-exit path.
- **Pass condition:** Two paths are present and labeled distinctly. Each path must reach
  a different terminal outcome or branch at a different decision point. Two variations of
  the same happy path do not satisfy this criterion.

---

### C-07 — Topic Graph Completeness
- **Category:** coverage
- **Weight:** recommended
- **Text:** The artifact names all topic nodes in the conversation graph and identifies
  which nodes were covered by the trace and which were not.
- **Pass condition:** A topic node inventory appears in the artifact (as a table, list,
  or inline coverage map). Each node is labeled traced or untraced. Nodes that are
  unreachable from the entry point are called out explicitly.

---

## Aspirational Criteria

### C-08 — Copilot Studio Domain Vocabulary
- **Category:** behavior
- **Weight:** aspirational
- **Text:** The simulation uses Copilot Studio–specific terminology correctly throughout:
  topics, trigger phrases, system topics (Greeting, Fallback, Escalate), entities,
  condition branches, and redirect nodes.
- **Pass condition:** At least five Copilot Studio–specific terms are used correctly and
  in context. Generic chatbot vocabulary ("intents", "slots", "utterances") used
  interchangeably with Copilot Studio terms without disambiguation does not satisfy
  this criterion on its own.

---

### C-09 — Actionable Remediation Per Defect
- **Category:** depth
- **Weight:** aspirational
- **Text:** Each identified defect includes a specific, implementable fix: where to add
  the missing fallback, which trigger phrase causes the collision and how to disambiguate,
  which redirect to add to break the loop, or which terminal state to add to close the
  dead end.
- **Pass condition:** Every defect entry in the defect report has a corresponding
  remediation. Remediations must be specific (name the node, topic, or phrase to change),
  not generic advice ("add better error handling").

---

### C-10 — Named Failure-Mode Prohibition
- **Category:** behavior
- **Weight:** aspirational
- **Derived from:** Round 1 V-04 achieving C-09 PASS; V-01/02/03 all PARTIAL because
  no example-level enforcement was present.
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

### C-11 — Structural Domain-Vocabulary Enforcement
- **Category:** behavior
- **Weight:** aspirational
- **Derived from:** Round 1 V-05 achieving C-08 PASS via column schema; V-02 PARTIAL
  because generic headers ("User Input", "Bot Response") did not force CS labels per row.
- **Text:** Output tables use Copilot Studio–specific column headers (e.g.,
  "Copilot Studio Object to Edit", "Trigger Phrase", "Redirect Node") rather than generic
  labels ("Fix", "User Input", "Recommendation"). Vocabulary is enforced by the table
  schema itself, not only by role priming.
- **Pass condition:** At least one output table has a column whose header is a
  Copilot Studio–specific term. Role priming alone, without CS-labeled columns, does not
  pass. A column labeled "Fix" that merely permits CS vocabulary does not pass; the
  header must require it by being a CS term.

---

### C-12 — Phase Exit Conditions Block Degenerate Completion
- **Category:** coverage
- **Weight:** aspirational
- **Derived from:** Round 1 V-03/V-05 achieving full recommended-tier passes via explicit
  phase gates; V-01/V-02 getting PARTIAL on C-05/C-06/C-07 due to soft or absent exit
  conditions.
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

## Criterion Summary

| ID | Text (short) | Tier | Category | Pass Condition (short) |
|----|-------------|------|----------|------------------------|
| C-01 | Dialog path traced | essential | correctness | Complete turn-by-turn path, entry → terminal |
| C-02 | Defect report present | essential | correctness | All 4 defect types checked with verdict |
| C-03 | Intent–response pairing | essential | correctness | Both sides present in every turn |
| C-04 | Fallback handling shown | essential | coverage | At least one no-match branch traced or flagged |
| C-05 | Session state tracked | recommended | depth | >=2 named variables traced across turns |
| C-06 | Multi-path coverage | recommended | coverage | Happy path + >=1 exception/fallback path |
| C-07 | Topic graph completeness | recommended | coverage | Inventory of nodes with traced/untraced labels |
| C-08 | Copilot Studio vocabulary | aspirational | behavior | >=5 CS-specific terms used correctly in context |
| C-09 | Actionable remediation | aspirational | depth | Specific fix per defect, not generic advice |
| C-10 | Named failure-mode prohibition | aspirational | behavior | >=1 degenerate output named by example and banned |
| C-11 | Structural domain-vocab enforcement | aspirational | behavior | >=1 output table column header is a CS-specific term |
| C-12 | Phase exit conditions block collapse | aspirational | coverage | >=2 phase gates with hard exit conditions naming the blocked failure |
