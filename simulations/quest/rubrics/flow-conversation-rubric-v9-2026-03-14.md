```markdown
# Rubric — flow-conversation — v9 (2026-03-15)

> **What changed in v9**: Added C-25 (session variable timeline contract),
> C-26 (session timeline mutation log), C-27 (timeline anomaly defect class),
> C-28 (Phase 6-D topic aggregate consistency audit), and C-29 (Phase 6-E
> session timeline consistency audit), extracted from Round 9 excellence
> signals in V-04.
>
> C-25 requires a Phase 0-A-6 SESSION_VARIABLE_TIMELINE_CONTRACT declaring the
> full lifecycle of every session variable before execution begins:
> FIRST_WRITTEN_TOPIC (the topic that creates the variable), CLEARED_BY (the
> topic or condition that destroys it), and READ_AFTER_CLEARED
> (FORBIDDEN|ALLOWED). This contract converts implicit session state behavior
> — which prior rounds rationalized post-hoc from Phase 0-D-3 evidence — into
> a pre-execution commitment. The Auditor verifies that Phase 1 mutations
> conform to the declared contract rather than inferring conformance from
> observed behavior. V-04 is the first variation to declare this contract;
> V-01 through V-03 set session variable behavior implicitly inside Phase 0-D-3
> without a temporal lifecycle commitment, leaving the contract unauditable.
>
> C-26 requires a Phase 1-S SESSION_TIMELINE that is strictly additive to the
> Phase 1 turn table. Each row records one variable-turn event: variable name,
> turn ID, mutation type (WRITE|READ|CLEAR|NO_CHANGE), and value after
> mutation. Phase 1 SESSION_STATE snapshots show what state exists at each
> turn; the SESSION_TIMELINE shows how each variable's state arrived there.
> Temporal ordering defects — reads before first write, reads after clear —
> are invisible in state snapshots and immediately legible in sequential
> mutation order. Phase 6-E (C-29) closes the verification loop by
> reconstructing SESSION_STATE from Phase 1-S and comparing against Phase 1
> snapshots.
>
> C-27 formalizes TIMELINE_ANOMALY as the seventh structural defect class at
> state-ordering level, orthogonal to all prior defect levels. The six prior
> classes operate at graph topology, edge, slot-fill path, severity, and
> session variable (SLOT_GAP) levels; TIMELINE_ANOMALY operates at temporal
> state sequencing. Instances include: READ_AFTER_CLEAR (reading a variable
> after CLEARED_BY fires without an intervening WRITE), OFF_CONTRACT_WRITE
> (writing in a topic not declared as FIRST_WRITTEN_TOPIC or an authorized
> re-writer), and STALE_READ (reading a variable whose most recent state is a
> CLEAR-permitted but unrefreshed value). TIMELINE_ANOMALY_RATE =
> timeline_anomalies_found / total_variable_turn_events is the fourth coverage
> dimension in Phase 5, joining topic, transition, and slot-path ratios. A
> trace achieving 100% on the first three coverage ratios can still carry
> TIMELINE_ANOMALY_RATE > 0.
>
> C-28 makes Phase 6-D the mandatory Auditor gate for C-24. C-24 requires a
> Phase 1-T topic aggregate; C-28 requires that an independent Phase 6-D audit
> explicitly cross-checks the conformance_rollup column in Phase 1-T against
> the DEVIATES count per topic derived from Phase 1 turn-level verdicts. A
> mismatch is a TOPIC_ROLLUP_MISMATCH finding. All Round 9 variations except
> V-04 carried C-24 PARTIAL (2/4) because Phase 6-D was absent; the scoring
> gap was visible but the criterion did not isolate the Auditor gate as a
> separate failure mode. C-28 separates the gate so its absence is scored
> independently of the data requirement in C-24.
>
> C-29 requires a Phase 6-E Session Timeline Consistency Audit. The Auditor
> independently reconstructs SESSION_STATE for each turn by replaying Phase
> 1-S mutations in sequence and compares the reconstructed state against the
> Phase 1 SESSION_STATE column. Any discrepancy is a TIMELINE_STATE_MISMATCH
> finding. This closes the verification loop between the additive mutation log
> (Phase 1-S, C-26) and the snapshot evidence (Phase 1 SESSION_STATE): both
> representations must be equivalent at every turn. Phase 6-E is the session
> variable counterpart to Phase 6-D, which audits the topic aggregate layer;
> together they complete the Auditor verification stack across the three
> additive data structures introduced in Round 8–9 (Phase 1-T, Phase 1-S).
>
> C-24 pass condition updated to reference C-28 as the mandatory Auditor gate:
> full credit for C-24 requires C-28 PASS.
>
> Aspirational denominator updated from 26 to 46.
>
> *(prior change history preserved unchanged)*

---

## Purpose

Evaluate a simulated Copilot Studio conversation-flow trace for dialog
coverage, defect classification completeness, session state fidelity, and
domain vocabulary discipline.

---

## Essential Criteria (60 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-01 | **Dialog path traced as turns** | coverage | 15 | Output walks the conversation turn-by-turn. Each turn shows: user utterance, topic matched, nodes executed, agent response, and transition target. No turns may be skipped or collapsed into a summary. |
| C-02 | **All four defect classes addressed** | correctness | 15 | Output explicitly addresses all four defect classes: dead ends, infinite loops, intent collisions, missing fallbacks. Each class is either found (with example) or confirmed absent. CONFIRMED ABSENT requires an explicit statement of scope. |
| C-03 | **Session state tracked** | correctness | 15 | Output maintains and displays session state across turns (e.g., active topic, slot values, prior intent history). State must visibly change or be held across at least two transitions. |
| C-04 | **Copilot Studio framing** | behavior | 15 | Analysis uses Copilot Studio vocabulary: topics, trigger phrases, conditions, fallback topics, escalation, session variables. Generic chatbot terms without grounding are not sufficient. |

---

## Recommended Criteria (30 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-05 | **Defect reproduction steps** | depth | 10 | For each defect found, output provides a minimal reproduction: the exact utterance sequence that triggers the defect and the observable failure mode. |
| C-06 | **Fallback chain coverage** | coverage | 10 | Output traces at least one fallback path to completion — what happens when no topic matches, including escalation or graceful exit. Shows the full chain, not just the first fallback node. |
| C-07 | **Intent collision disambiguation** | depth | 10 | If intent collisions are found, output proposes a disambiguation strategy (e.g., entity enrichment, condition ordering, trigger phrase refactor) with rationale. |

---

## Aspirational Criteria (46 points total)

| ID | Criterion | Category | Weight | Pass Condition |
|----|-----------|----------|--------|----------------|
| C-08 | **Graph coverage metric** | coverage | 1 | Phase 5 reports topic_coverage_ratio = topics_visited / total_declared. Denominator derived from Phase 0-D-1 topic registry. Ratio reported as a fraction with both numerator and denominator visible. |
| C-09 | **Adversarial turn injection** | depth | 1 | Phase 6 injects at least one adversarial utterance mid-conversation (off-topic, ambiguous, or contradictory). Output records the injection point with turn ID, the system response, and any defect triggered. Recovery path must be traced to completion. |
| C-10 | **Prohibited vocabulary gate** | behavior | 1 | Developer self-declares permitted and prohibited vocabulary in Phase 0-D-2 before tracing. Prohibited terms (generic chatbot vocabulary without Copilot Studio grounding) are absent from all Phase 1 trace entries. Developer signs the gate at Phase 0-D-2 close. |
| C-11 | **Turn-level conformance verdict** | correctness | 1 | Every row in the Phase 1 turn table carries an explicit CONFORMANCE verdict: CONFORMS \| DEVIATES[INVARIANT-ID]. No turn may be left without a verdict. DEVIATES entries cite the violated invariant by its registered ID from Phase 0-D-4. |
| C-12 | **Topic graph pre-declaration** | structure | 1 | Phase 0-D-1 declares all topics, trigger phrases, entry conditions, and exit targets before Phase 1 tracing begins. The trace may only reference topics present in this registry; first encounter of an undeclared topic is a CONTRACT_GAP finding. |
| C-13 | **Session variable registry** | structure | 1 | Phase 0-D-3 lists all session variables with PERSISTENCE_CLASS (SESSION \| TOPIC_SCOPED \| GLOBAL) and initial value before the trace begins. Variables appearing in Phase 1 SESSION_STATE must be registered here; first appearance of an unregistered variable is a CONTRACT_GAP finding. |
| C-14 | **Invariant register** | correctness | 1 | Phase 0-D-4 declares all conversation-level invariants, each with a unique INVARIANT-ID and a falsification condition. Every DEVIATES verdict in Phase 1 and every defect in Phase 3 must cite at least one registered INVARIANT-ID. |
| C-15 | **Escalation path traced** | coverage | 1 | At least one escalation path to a human agent (or equivalent terminal handoff) is traced in full: trigger condition, handoff node name, session state at handoff, and agent receipt confirmation. Escalation is CONFIRMED ABSENT only if no escalation topic is declared in Phase 0-D-1. |
| C-16 | **Phase 0 pre-execution contract** | structure | 1 | Output opens with a complete Phase 0 block declaring all graph artifacts — topics (0-D-1), vocabulary (0-D-2), session variables (0-D-3), invariants (0-D-4) — before any Phase 1 turn is traced. Phase 0 closure is the boundary at which the Developer commits to the contract; Auditor phases verify against it. |
| C-17 | **Developer / Auditor role separation** | behavior | 1 | Output explicitly separates Developer phases (Phases 0–5: trace construction, defect classification, coverage calculation) from Auditor phases (Phase 6-*: independent verification). Auditor findings are structurally isolated and may not retroactively alter Developer rows; discrepancies are recorded as audit findings. |
| C-18 | **Slot-fill path tracking** | coverage | 1 | Slot-filling topics record: slots targeted, fill attempt order, fill result (FILLED \| SKIPPED \| INTERRUPTED), and any short-circuit path taken when required slots are bypassed. An interrupted slot-fill sequence is flagged as a candidate defect for Phase 3 review. |
| C-19 | **Orphaned topic detection** | coverage | 1 | Phase 5 identifies topics declared in Phase 0-D-1 but unreachable or never visited in the trace as ORPHAN defects. These must be included in the denominator of the topic_coverage_ratio (C-08). An orphaned topic may not be silently excluded from coverage accounting. |
| C-20 | **Recovery verdict classification** | correctness | 1 | Each FOUND defect in Phase 3 carries a recovery verdict: RECOVERABLE[min_turns, target_state] \| UNRECOVERABLE[reason]. UNRECOVERABLE requires explicit justification; RECOVERABLE requires a concrete target state and minimum turn count to reach it. MASKED_BY defects (C-23) carry conditional form: RECOVERABLE[min_turns, target_state, requires_fix=DEFECT_CLASS]. |
| C-21 | **Severity co-residency audit** | correctness | 3 | An independent Phase 6-B Severity Co-Residency Audit verifies that every FOUND defect row contains both SEVERITY_CLASS and INVARIANT_CITE. Neither column may substitute for the other. EXEMPT status locks CONFIRMED_ABSENT rows out of the audit. The audit produces a structured table; a prose note does not satisfy the criterion. |
| C-22 | **Transition completeness map** | coverage | 3 | Phase 0-D-5 TRANSITION_MAP declares all conversation graph edges before tracing: TRANS-NN (source_topic, target_topic, condition, REQUIRED\|OPTIONAL). Phase 5 reports transitions_exercised / total_declared as a second coverage ratio orthogonal to topic coverage. Unexercised REQUIRED transitions are orphaned-edge defects with UNRECOVERABLE[missing edge] recovery verdicts. |
| C-23 | **Defect entanglement analysis** | correctness | 3 | Phase 3-E ENTANGLEMENT_MAP assigns every FOUND defect an ENTANGLEMENT_VERDICT: ISOLATED \| ENABLES[DEFECT_CLASS] \| MASKED_BY[DEFECT_CLASS]. MASKED_BY defects carry conditional recovery verdicts (C-20). Phase 6-C independently audits map consistency against Phase 1 turn-level evidence. |
| C-24 | **Topic-indexed trace aggregation** | coverage | 4 | Phase 1-T topic aggregate is strictly additive to the Phase 1 turn table — not replacing it. Each row shows: turns_visited, session_variables_set/read (lifecycle summary), defect_citations with TOPIC_ID provenance, adversarial_injection_count, and conformance_rollup. Full credit requires C-28 PASS: the Phase 6-D Auditor cross-check of Phase 1-T conformance_rollup against Phase 1 turn-level DEVIATES counts is the mandatory Auditor gate for this criterion. |
| C-25 | **Session variable timeline contract** | structure | 4 | Phase 0-A-6 SESSION_VARIABLE_TIMELINE_CONTRACT declares the full lifecycle of every session variable before execution: FIRST_WRITTEN_TOPIC, CLEARED_BY, READ_AFTER_CLEARED (FORBIDDEN\|ALLOWED). All variables registered in Phase 0-D-3 must appear in this contract. The contract is a pre-execution commitment; Auditor phases may not grant retroactive dispensation for undeclared lifecycle events. |
| C-26 | **Session timeline mutation log** | structure | 4 | Phase 1-S SESSION_TIMELINE is a turn-indexed mutation log, strictly additive to Phase 1. Each row records: variable name, turn ID, mutation type (WRITE\|READ\|CLEAR\|NO_CHANGE), value after mutation. Every session variable appearing in Phase 1 SESSION_STATE must have a Phase 1-S entry for each turn in which it is non-null. The log serves as the evidence base for TIMELINE_ANOMALY classification (C-27) and Phase 6-E verification (C-29). |
| C-27 | **Timeline anomaly defect class** | correctness | 4 | TIMELINE_ANOMALY is recognized as the seventh structural defect class at state-ordering level, orthogonal to graph topology, edge, slot-fill path, and severity defect levels. Instances include: READ_AFTER_CLEAR, OFF_CONTRACT_WRITE, and STALE_READ. Phase 5 reports TIMELINE_ANOMALY_RATE = timeline_anomalies_found / total_variable_turn_events as the fourth coverage ratio alongside topic, transition, and slot-path ratios. A trace may achieve 100% on the first three ratios while TIMELINE_ANOMALY_RATE > 0. |
| C-28 | **Phase 6-D topic aggregate consistency audit** | correctness | 4 | An independent Phase 6-D Auditor cross-checks the conformance_rollup column in Phase 1-T against the DEVIATES count for each topic derived from Phase 1 turn-level verdicts. A mismatch is a TOPIC_ROLLUP_MISMATCH finding. This audit is the mandatory Auditor gate for C-24: C-24 cannot achieve full credit without C-28 PASS. The audit is structurally separate from Phase 1-T data presentation; both must be present. |
| C-29 | **Phase 6-E session timeline consistency audit** | correctness | 4 | An independent Phase 6-E Auditor reconstructs SESSION_STATE for each turn by replaying Phase 1-S mutations in sequence and compares the reconstructed state against the Phase 1 SESSION_STATE column. Any discrepancy is a TIMELINE_STATE_MISMATCH finding. This audit closes the verification loop between the additive mutation log (Phase 1-S, C-26) and the snapshot evidence (Phase 1 SESSION_STATE): both representations must be equivalent at every turn. |
```
