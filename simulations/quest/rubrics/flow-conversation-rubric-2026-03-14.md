Rubric written to `simulations/quest/rubrics/flow-conversation-rubric-2026-03-14.md`.

**Structure:**
- **4 essential** (C-01 to C-04): dialog path traced, all four defect classes addressed, session state tracked, Copilot Studio vocabulary used
- **3 recommended** (C-05 to C-07): defect reproduction steps, full fallback chain trace, collision disambiguation strategy
- **2 aspirational** (C-08 to C-09): graph coverage ratio, adversarial turn injection

**Design notes:**
- C-02 requires both finding *and* confirming absence — a common gap where outputs only report what they find
- C-04 is the domain gate: generic "chatbot" framing without Copilot Studio topology is an automatic essential fail
- C-08 turns narrative ("I checked most topics") into a signal ("11/14 topics visited, 78%")
- Golden threshold requires all 4 essentials + composite >= 80
lasses: dead ends, infinite loops, intent collisions, missing fallbacks. Each class is either found (with example) or confirmed absent. |
| C-03 | **Session state tracked** | correctness | essential | Output maintains and displays session state across turns (e.g., active topic, slot values, prior intent history). State must visibly change or be held across at least two transitions. |
| C-04 | **Copilot Studio framing** | behavior | essential | Analysis uses Copilot Studio vocabulary: topics, trigger phrases, conditions, fallback topics, escalation, session variables. Generic chatbot terms without grounding are not sufficient. |

---

## Recommended Criteria (30 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Defect reproduction steps** | depth | recommended | For each defect found, output provides a minimal reproduction: the exact utterance sequence that triggers the defect and the observable failure mode. |
| C-06 | **Fallback chain coverage** | coverage | recommended | Output traces at least one fallback path to completion -- what happens when no topic matches, including escalation or graceful exit. Shows the full chain, not just the first fallback node. |
| C-07 | **Intent collision disambiguation** | depth | recommended | If intent collisions are found, output proposes a disambiguation strategy (e.g., entity enrichment, condition ordering, trigger phrase refactor) with rationale. |

---

## Aspirational Criteria (10 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Graph coverage metric** | depth | aspirational | Output reports a coverage ratio: topics visited / total topics in graph, or intents exercised / total trigger phrases. Gives a quantified signal, not just narrative. |
| C-09 | **Adversarial turn injection** | behavior | aspirational | Output includes at least one adversarial scenario -- unexpected user utterance mid-flow, topic switch during slot filling, or session timeout -- and shows how the agent responds. |

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 2 * 10)
```

**Golden threshold**: all 4 essential criteria pass AND composite >= 80.

---

## Failure Modes

| Failure | Likely Cause |
|---------|-------------|
| C-01 fails | Output describes the graph abstractly without walking actual turns |
| C-02 fails | Output only finds defects present, never confirms absence of others |
| C-03 fails | Each turn is evaluated independently with no carried state |
| C-04 fails | Reviewer uses generic chatbot framing, misses Copilot Studio topology |
