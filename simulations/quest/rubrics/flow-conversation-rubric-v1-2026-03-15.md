---
skill: quest-rubric
skill_target: flow-conversation
date: 2026-03-15
version: 1
---

# Rubric — flow-conversation — v1 (2026-03-15)

**Skill:** Simulate a multi-turn agent conversation through a topic graph. Walk the dialog
path: user intents, agent responses, topic transitions, fallback handling, session state.
Identify dead ends, infinite loops, intent collisions, and missing fallbacks.
**Stock role:** Copilot Studio domain expert.

---

## Scoring Model

| Tier | Weight | Criteria | Points if all pass |
|------|--------|----------|--------------------|
| Essential | 60% | 4 criteria | 60 |
| Recommended | 30% | 3 criteria | 30 |
| Aspirational | 10% | 2 criteria | 10 |

**Composite score** = (essential_pass/4 × 60) + (recommended_pass/3 × 30) + (aspirational_pass/2 × 10)

**Golden threshold:** All 4 essential criteria pass AND composite ≥ 80.

---

## Essential Criteria

### C-01 — Dialog Path Traced
- **Category:** correctness
- **Weight:** essential
- **Text:** The artifact walks at least one complete dialog path from an entry intent to a
  terminal state, showing each turn as a discrete step with a named user intent and a
  named agent response.
- **Pass condition:** At minimum one path is traceable from start to end without gaps.
  Each step must show: (1) user utterance or intent label, (2) agent response or action,
  (3) resulting topic or state. A list of intents without turn-by-turn trace does not pass.

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

## Criterion Summary

| ID | Text (short) | Tier | Category | Pass Condition (short) |
|----|-------------|------|----------|------------------------|
| C-01 | Dialog path traced | essential | correctness | Complete turn-by-turn path, entry → terminal |
| C-02 | Defect report present | essential | correctness | All 4 defect types checked with verdict |
| C-03 | Intent–response pairing | essential | correctness | Both sides present in every turn |
| C-04 | Fallback handling shown | essential | coverage | At least one no-match branch traced or flagged |
| C-05 | Session state tracked | recommended | depth | ≥2 named variables traced across turns |
| C-06 | Multi-path coverage | recommended | coverage | Happy path + ≥1 exception/fallback path |
| C-07 | Topic graph completeness | recommended | coverage | Inventory of nodes with traced/untraced labels |
| C-08 | Copilot Studio vocabulary | aspirational | behavior | ≥5 CS-specific terms used correctly in context |
| C-09 | Actionable remediation | aspirational | depth | Specific fix per defect, not generic advice |
