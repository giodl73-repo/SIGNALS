```markdown
# Rubric — flow-conversation — v4 (2026-03-14)

> **What changed in v4**: Added C-14 (contract-first schema authorship) and C-15
> (table columns as structural enforcement), extracted from Round 4 excellence
> signals in V-03/V-04/V-05 and V-01/V-04/V-05 respectively. Aspirational
> denominator updated from 6 to 8.
>
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
| C-12 | **Role-separated post-production audit** | behavior | aspirational | Output assigns a distinct Auditor role that operates on the *completed* Developer trace as a finished artifact — not inline during production. A hard phase-gate boundary marker (e.g., `=== DEVELOPER ARTIFACT COMPLETE ===`) separates production from audit. The Auditor reads the full output in scan mode and produces a separate audit layer. Role separation provides full-output context and prevents the producer from self-certifying. The phase gate is load-bearing: imperative role-switch phrasing without the hard boundary is insufficient. |
| C-13 | **Typed assertion fields with constrained verdict enums** | correctness | aspirational | All key assertion positions use typed structured fields with constrained vocabulary — e.g., `SPEC_CONFORMANCE: CONFORMS \| DEVIATES`, `PROHIBITED_TERM_SCAN: CLEAN \| FOUND`, `DEFECT_VERDICT: FOUND \| CONFIRMED_ABSENT`. No free-text hedging permitted in verdict positions. Constrained enums remove ambiguity and prevent partial or qualified verdicts from masking non-compliance. |
| C-14 | **Contract-first schema authorship** | behavior | aspirational | The Auditor declares the complete assertion contract (all typed fields, all enum values, all prohibited-term list) in a Phase 0 schema block *before* the Developer writes any output. The Developer is bound to the Phase 0 schema in all subsequent phases. This prevents the Auditor from reverse-engineering criteria post-hoc and provides a stronger independence guarantee than retroactive-only auditing. |
| C-15 | **Table columns as structural enforcement** | correctness | aspirational | Per-turn output is formatted as a typed table with mandatory columns for each assertion field (e.g., SPEC_CONFORMANCE, PROHIBITED_TERM_SCAN, SESSION_VARIABLES). A blank cell in a mandatory column is a visible structural failure. Block or narrative per-turn format cannot achieve this property: omitted fields are invisible, whereas a missing table cell is not. |

---

## Scoring Formula

```
composite = (essential_pass / 4 * 60)
          + (recommended_pass / 3 * 30)
          + (aspirational_pass / 8 * 10)
```

**Golden threshold**: all 4 essential criteria pass AND composite >= 80.

---

## Failure Modes

| Failure | Likely Cause |
|---------|-------------|
| C-12 FAIL despite Auditor section present | Phase gate absent or imperative-only role switch; model treats Auditor as inline continuation and self-certifies |
| C-13 FAIL despite structured output | Free-text or hedged language in verdict positions (e.g., "likely CONFORMS", "mostly CLEAN") |
| C-14 FAIL despite typed fields | Assertion schema declared after Developer work begins (retroactive); Auditor can adjust criteria to match output |
| C-15 FAIL despite per-turn verdicts | Block/narrative format used instead of table; missing assertions not visible as structural gaps |
| C-10 FAIL despite CS vocabulary used | No explicit prohibited-term list; no terminal scan verifying absence; passive usage without active enforcement |
```
