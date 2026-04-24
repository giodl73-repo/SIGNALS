Looking at the Round 2 scorecard, the two new excellence signals are:

1. **V-03** — Two-role separation where the Auditor reads the *finished* Developer output as a distinct post-production pass ("stronger scan mode"), not inline annotation.
2. **V-04** — Typed assertion fields with constrained verdict enums (`FOUND | CONFIRMED_ABSENT`, not free text) that structurally prevent hedging across all key assertion positions.

These become **C-12** and **C-13**. Aspirational denominator updates from 4 to 6.

---

```markdown
# Rubric — flow-conversation — v3 (2026-03-14)

> **What changed in v3**: Added C-12 (role-separated post-production audit) and C-13
> (typed assertion fields with constrained verdict enums), extracted from Round 2
> excellence signals in V-03 and V-04. Aspirational denominator updated from 4 to 6.
>
> **What changed in v2**: Added C-10 (prohibited vocabulary gate) and C-11
> (turn-level conformance verdict), extracted from Round 1 excellence signals in
> V-03 and V-04. Aspirational denominator updated from 2 to 4.

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
| C-12 | **Role-separated post-production audit** | behavior | aspirational | Output assigns a distinct Auditor role that operates on the *completed* Developer trace as a finished artifact — not inline during production. The Auditor reads the full output in scan mode and produces a separate audit layer (e.g., per-turn spec conformance annotations, prohibited term table). Role separation provides full-output context and prevents the producer from self-certifying. |
| C-13 | **Typed assertion fields with constrained verdict enums** | correctness | aspirational | All key assertion positions use typed structured fields with constrained vocabulary — e.g., `SPEC_CONFORMANCE: CONFORMS \| DEVIATES`, `PROHIBITED_TERM_SCAN: CLEAN \| FOUND`, `DEFECT_VERDICT: FOUND \| CONFIRMED_ABSENT`. No free-text hedging permitted in verdict positions. Constrained enums remove ambiguity and prevent partial or qualified verdicts from masking non-compliance. |

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 6 * 10)
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
| C-12 fails | Audit performed inline by the same role producing the trace; no post-production separation |
| C-13 fails | Verdicts expressed as free text ("looks correct," "probably absent") rather than constrained enum values; hedging possible |
```

---

Two scoring notes follow from applying v3 to the Round 2 results:

- **V-03**: C-12 PASS (Auditor role separation), C-13 status depends on whether typed fields are present — V-03 uses structured blocks but not strict enum constraints, likely FAIL. Score unchanged at **95**.
- **V-04**: C-12 FAIL (no explicit role separation — dual enforcement is inline, not a separate role pass), C-13 PASS (typed fields with `FOUND | CONFIRMED_ABSENT` constraints throughout). Score also stays at **95** under v3 for the same aspirational count.

The two new criteria differentiate V-03 and V-04 from each other rather than from the pack — a variation that combines role separation (C-12) with typed enums (C-13) alongside C-10/C-11 would be the first to score **95 + 10/6 × 2 ≈ 98.3**.
