Here is the complete updated rubric:

---

# Rubric — flow-conversation — v7 (2026-03-14)

> **What changed in v7**: Added C-19 (reachability map pre-computation) and
> C-20 (recovery path verdict per FOUND defect), extracted from Round 7
> excellence signals in V-02 and V-01 respectively.
>
> C-19 requires the Developer to declare a REACHABILITY_MAP in Phase 0-D:
> entry topic, all topics reachable by transitivity, and orphaned topics
> (defined but unreachable). The Auditor classifies orphaned topics as ORPHAN
> defects — a fifth structural defect class, defined at graph level rather than
> execution level, required regardless of whether orphaned topics appear in any
> trace path. C-19 also tightens C-08: the coverage ratio denominator must
> derive from the declared REACHABILITY_MAP (`reachable_visited /
> total_reachable`), not from the set of all defined topics. V-02 was the first
> variation to fully satisfy C-08 by grounding the metric in declared topology.
>
> C-20 requires each FOUND defect row to carry a mandatory RECOVERY field:
> RECOVERABLE[min_turns, target_state] or UNRECOVERABLE[reason]. A FOUND row
> without a RECOVERY field is a structural failure; CONFIRMED_ABSENT rows are
> exempt. C-20 extends C-05 (defect reproduction steps) by requiring not just
> the trigger path but whether and how a user can escape the defect state --
> transforming defect reporting from classification into actionable remediation
> guidance.
>
> V-03's session variable persistence scope was noted in the Round 7 scorecard
> as an extension of C-03, not a structural novelty, and does not generate a
> new criterion. V-04's defect severity triage was not promoted: its
> implementation corrupted typed-verdict discipline (C-13 PARTIAL) and
> displaced invariant citations (C-18 FAIL), producing the lowest Round 7
> score (97). The pattern may be revisited in a future round with proper
> type constraints that prevent business-domain terms from leaking into verdict
> fields and that preserve coexistence with C-17 and C-18.
>
> Aspirational denominator updated from 11 to 13.
>
> *(prior change history preserved unchanged)*

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
| C-06 | **Fallback chain coverage** | coverage | recommended | Output traces at least one fallback path to completion -- what happens when no topic matches, including escalation or graceful exit. Shows the full chain, not just the first fallback node. |
| C-07 | **Intent collision disambiguation** | depth | recommended | If intent collisions are found, output proposes a disambiguation strategy (e.g., entity enrichment, condition ordering, trigger phrase refactor) with rationale. |

---

## Aspirational Criteria (13 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Graph coverage metric** | depth | aspirational | Output reports a coverage ratio: topics visited / total topics in graph, or intents exercised / total trigger phrases. Gives a quantified signal, not just narrative. **When C-19 is also satisfied, the denominator must derive from the declared REACHABILITY_MAP (`reachable_visited / total_reachable`), not the count of all defined topics.** |
| C-09 | **Adversarial turn injection** | behavior | aspirational | Output includes at least one adversarial scenario -- unexpected user utterance mid-flow, topic switch during slot filling, or session timeout -- and shows how the agent responds. |
| C-10 | **Prohibited vocabulary gate** | behavior | aspirational | Output pre-maps the CS topology term set used in the trace AND explicitly lists prohibited generic terms with a verification that none appear in the output. Demonstrates active vocabulary enforcement, not passive CS term usage. |
| C-11 | **Turn-level conformance verdict** | correctness | aspirational | Each turn carries an explicit CONFORMS / DEVIATES verdict against the expected topology spec, separate from the defect classification section. |
| C-12 | **Role-separated post-production audit** | behavior | aspirational | Output assigns a distinct Auditor role operating on the *completed* Developer trace. A hard phase-gate boundary marker separates production from audit. The phase gate is load-bearing: imperative role-switch phrasing without the hard boundary is insufficient. |
| C-13 | **Typed assertion fields with constrained verdict enums** | correctness | aspirational | All key assertion positions use typed structured fields with constrained vocabulary. No free-text hedging permitted in verdict positions. |
| C-14 | **Contract-first schema authorship** | behavior | aspirational | The Auditor declares the complete assertion contract in a Phase 0 schema block *before* the Developer writes any output. The Developer is bound to the Phase 0 schema in all subsequent phases. |
| C-15 | **Table columns as structural enforcement** | correctness | aspirational | Per-turn output is formatted as a typed table with mandatory columns for each assertion field. A blank cell in a mandatory column is a visible structural failure. |
| C-16 | **Developer domain pre-contract** | behavior | aspirational | The Developer declares a Phase 0 domain block -- topic inventory, CS vocabulary binding, and session variable registry -- *before* the Auditor writes the assertion schema. Mutual pre-commitment: C-14 requires Auditor pre-contracting, C-16 requires both parties to declare before any trace output exists. |
| C-17 | **Gap-closure annotation** | correctness | aspirational | Each structural phase carries an annotation linking it to the prior-round gap it resolves and produces a `GAP_CLOSURE_VERDICT: CLOSED \| OPEN` enum confirming closure. A phase that re-opens a previously closed gap is a structural failure. |
| C-18 | **Topology invariant registry with cross-traceability** | correctness | aspirational | Developer Phase 0-D pre-commits named structural invariants (`INVARIANT-TOPO-NN`, `INVARIANT-SV-NN`). The Auditor adds `INVARIANT_CONFORMANCE: HOLDS \| VIOLATED[NN]` as a mandatory trace table column. `CONFIRMED_ABSENT` defect rows must cite the invariant ID that guarantees absence -- a CONFIRMED_ABSENT row without an invariant citation is a contract violation. |
| **C-19** | **Reachability map pre-computation** | coverage | aspirational | Developer Phase 0-D declares a REACHABILITY_MAP listing: (a) the conversation entry topic, (b) all topics reachable from entry by transitivity, and (c) any orphaned topics -- defined in the system but unreachable from the entry point by any transition path. The Auditor classifies orphaned topics as ORPHAN defects, a **fifth structural defect class** operating at graph level rather than execution level. ORPHAN defects are required findings regardless of whether orphaned topics appear in the trace path -- their absence from the trace is evidence of the defect, not evidence of absence. C-08's coverage ratio, when C-19 is satisfied, must use `reachable_visited / total_reachable` with the denominator sourced from the REACHABILITY_MAP; a ratio computed against `total_defined` topics when unreachable topics exist is a measurement error, not a coverage metric. C-19 extends C-18 (topology invariant registry) by adding graph-level reachability as a first-class pre-computation artifact alongside structural invariants. |
| **C-20** | **Recovery path verdict per FOUND defect** | depth | aspirational | Each row in the defect table carrying verdict FOUND must include a mandatory RECOVERY field: RECOVERABLE[min_turns, target_state] or UNRECOVERABLE[reason]. A FOUND row without a RECOVERY field is a structural failure under C-15 (table columns as structural enforcement). CONFIRMED_ABSENT rows are exempt. RECOVERABLE specifies the minimum turn count to exit the defect state and the target session state after recovery. UNRECOVERABLE states the reason no escape path exists (e.g., "topic exit node absent," "fallback chain terminates in same defect"). C-20 extends C-05 (defect reproduction steps): C-05 requires the trigger path, C-20 requires the escape path. Together they transform a defect row from a classification record into a complete remediation brief -- severity of entrapment is now a first-class property of the defect, not an inference. |

---

**Two patterns not promoted and why:**

- **V-03 (persistence scope)**: Scorecard called it an extension of C-03, not a structural novelty. No new criterion.
- **V-04 (severity triage)**: C-13 PARTIAL (BUSINESS_IMPACT free-text breaks typed-verdict discipline) + C-18 FAIL (CONFIRMED_ABSENT rows cited SEVERITY: N/A instead of INVARIANT-ID). The pattern itself has value but the R7 implementation demonstrates it cannot coexist with existing type constraints without explicit guardrails. Candidate for R8 with constrained enums (P0|P1|P2) and explicit coexistence rules for C-17/C-18.
_CLOSURE_VERDICT: CLOSED \| OPEN` enum confirming closure. Confirmed closures make rubric evolution traceable within the output and prevent regression on gaps identified in prior scoring rounds. A phase that re-opens a previously closed gap is a structural failure. |
| C-18 | **Topology invariant registry with cross-traceability** | correctness | aspirational | Developer Phase 0-D pre-commits named structural invariants (e.g., `INVARIANT-TOPO-NN`, `INVARIANT-SV-NN`) representing design-time guarantees about the agent topology (e.g., "every topic has exactly one fallback exit," "session variable X is cleared on topic exit"). The Auditor incorporates these invariant IDs into the assertion contract (C-14) and adds `INVARIANT_CONFORMANCE: HOLDS \| VIOLATED[NN]` as a mandatory column in the trace table (C-15). `CONFIRMED_ABSENT` defect rows must cite the invariant ID that structurally guarantees absence -- a CONFIRMED_ABSENT row without an invariant citation is a contract violation. This creates bidirectional traceability: every design-time claim is testable at runtime, and every runtime absence claim is grounded in a declared invariant. C-18 extends C-16 (domain pre-contract) by requiring the domain block to carry a named ID system that propagates through audit columns and defect classification, not merely a vocabulary and topology description. |
| C-19 | **Reachability map pre-computation** | coverage | aspirational | Developer Phase 0-D declares a REACHABILITY_MAP listing: (a) the conversation entry topic, (b) all topics reachable from entry by transitivity, and (c) any orphaned topics -- defined in the system but unreachable from the entry point by any transition path. The Auditor classifies orphaned topics as ORPHAN defects, a fifth structural defect class operating at graph level rather than execution level. ORPHAN defects are required findings regardless of whether orphaned topics appear in the trace path -- their absence from the trace is evidence of the defect, not evidence of absence. C-08's coverage ratio, when C-19 is satisfied, must use `reachable_visited / total_reachable` with the denominator sourced from the REACHABILITY_MAP; a ratio computed against `total_defined` topics when unreachable topics exist is a measurement error, not a coverage metric. C-19 extends C-18 (topology invariant registry) by adding graph-level reachability as a first-class pre-computation artifact alongside structural invariants. |
| C-20 | **Recovery path verdict per FOUND defect** | depth | aspirational | Each row in the defect table carrying verdict FOUND must include a mandatory RECOVERY field with one of two typed values: RECOVERABLE[min_turns, target_state] or UNRECOVERABLE[reason]. A FOUND row without a RECOVERY field is a structural failure under C-15 (table columns as structural enforcement). CONFIRMED_ABSENT rows are exempt. RECOVERABLE specifies the minimum turn count required to exit the defect state and the target session state after recovery. UNRECOVERABLE states the reason no escape path exists (e.g., "topic exit node absent," "fallback chain terminates in same defect"). C-20 extends C-05 (defect reproduction steps): C-05 requires the trigger path, C-20 requires the escape path. Together they transform a defect row from a classification record into a complete remediation brief -- severity of entrapment is now a first-class property of the defect, not an inference. |
