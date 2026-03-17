Looking at the scorecard, the excellence signals that consistently differentiate the top performers (V-03, V-04, V-05) are:

1. **Vocabulary gate with prohibited terms** (V-03) — goes beyond using CS vocabulary to actively listing prohibited generic terms and pre-mapping the CS topology index
2. **Turn-level DEVIATES annotation** (V-04) — inline CONFORMS/DEVIATES verdict per turn, separate from defect classification at the amendments stage

These become C-10 and C-11. The aspirational denominator updates from 2 to 4.

---

```markdown
# Rubric — flow-conversation — v2 (2026-03-14)

> **What changed in v2**: Added C-10 (prohibited vocabulary gate) and C-11
> (turn-level conformance verdict) as aspirational criteria, extracted from Round 1
> excellence signals in V-03 and V-04. Aspirational denominator updated from 2 to 4.

---

## Purpose

Evaluate a simulated Copilot Studio conversation-flow trace for dialog coverage,
defect classification completeness, session state fidelity, and domain vocabulary
discipline.

---

## Essential Criteria (60 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Dialog path traced as turns** | coverage | essential | Output walks the conversation turn-by-turn. Each turn shows: user utterance, topic matched, nodes executed, agent response, and transition target. No turns may be skipped or collapsed into a summary. |
| C-02 | **All four defect classes addressed** | correctness | essential | Output explicitly addresses all four defect classes: dead ends, infinite loops, intent collisions, missing fallbacks. Each class is either found (with example) or confirmed absent. CONFIRMED ABSENT requires an explicit statement of scope. |
| C-03 | **Session state tracked** | correctness | essential | Output maintains and displays session state across turns (e.g., active topic, slot values, prior intent history). State must visibly change or be held across at least two transitions. |
| C-04 | **Copilot Studio framing** | behavior | essential | Analysis uses Copilot Studio vocabulary: topics, trigger phrases, conditions, fallback topics, escalation, session variables. Generic chatbot terms without grounding are not sufficient. |

---

## Recommended Criteria (30 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Defect reproduction steps** | depth | recommended | For each defect found, output provides a minimal reproduction: the exact utterance sequence that triggers the defect and the observable failure mode. |
| C-06 | **Fallback chain coverage** | coverage | recommended | Output traces at least one fallback path to completion — what happens when no topic matches, including escalation or graceful exit. Shows the full chain, not just the first fallback node. |
| C-07 | **Intent collision disambiguation** | depth | recommended | If intent collisions are found, output proposes a disambiguation strategy (e.g., entity enrichment, condition ordering, trigger phrase refactor) with rationale. |

---

## Aspirational Criteria (10 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Graph coverage metric** | depth | aspirational | Output reports a coverage ratio: topics visited / total topics in graph, or intents exercised / total trigger phrases. Gives a quantified signal, not just narrative. |
| C-09 | **Adversarial turn injection** | behavior | aspirational | Output includes at least one adversarial scenario — unexpected user utterance mid-flow, topic switch during slot filling, or session timeout — and shows how the agent responds. |
| C-10 | **Prohibited vocabulary gate** | behavior | aspirational | Output pre-maps the CS topology term set used in the trace AND explicitly lists prohibited generic terms (e.g., "intent," "dialog," "slot," "NLU," "chatbot," "handoff") with a verification that none appear in the output. Demonstrates active vocabulary enforcement, not passive CS term usage. |
| C-11 | **Turn-level conformance verdict** | correctness | aspirational | Each turn in the dialog trace carries an explicit CONFORMS / DEVIATES verdict against the expected topology spec, separate from the defect classification section. Provides inline spec conformance at every step rather than only surfacing findings at the amendments stage. |

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 4 * 10)
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
| C-10 fails | CS vocabulary appears but prohibited terms are also present; no gate verifies discipline |
| C-11 fails | Spec conformance only surfaced in amendment section; per-turn verdict absent |
```
