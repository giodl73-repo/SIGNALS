```markdown
# Rubric — flow-conversation — v10 (2026-03-15)

> **What changed in v10**: Added C-30 (mutation-first authoring), C-31
> (AUTHORIZED_REWRITERS extension), C-32 (Contract Auditor pre-execution
> completeness gate), C-33 (Phase 6-A CONTRACT_AUDIT_GATE_HONORED), C-34
> (coverage quality gate CLEAN|DEGRADED), C-35 (SIMULATION_DELTA and
> STATUS_QUO_GAP), C-36 (CONSTRAINT_VERDICTS per turn), and C-37 (CONV_NN
> arithmetic evidence), extracted from Round 10 excellence signals across V-01
> through V-05.
>
> C-30 requires Phase 1-S to be authored BEFORE Phase 1 SESSION_STATE. Session
> state is not independently authored; it is derived by replaying Phase 1-S
> mutations in turn order. This structural ordering makes TIMELINE_STATE_MISMATCH
> — the finding targeted by Phase 6-E (C-29) — structurally impossible: a
> SESSION_STATE value cannot exist that lacks a Phase 1-S mutation event, because
> the snapshot is reconstructed from the log rather than authored in parallel.
> Phase 6-E under mutation-first authoring therefore verifies structural
> completeness (every turn has at least one mutation event; the replay accounts
> for every variable-turn combination) rather than hunting discrepancies between
> two independently-constructed tables. V-01 and V-04 used this pattern in Round
> 10; V-02, V-03, and V-05 authored Phase 1-S additively after Phase 1, which
> satisfies C-26 but not C-30. Prior rounds did not distinguish mutation-first
> from additive-after; the Round 10 scoring gap between PASS+ and PASS on C-26
> and C-29 made the distinction visible.
>
> C-31 extends the SESSION_VARIABLE_TIMELINE_CONTRACT (C-25) to require an
> AUTHORIZED_REWRITERS list per variable, declaring every topic permitted to
> write the variable beyond its FIRST_WRITTEN_TOPIC. Without this field, any
> write originating from a topic not declared as FIRST_WRITTEN_TOPIC generates
> an OFF_CONTRACT_WRITE anomaly — including legitimate re-writes in multi-topic
> flows where a downstream topic must refresh a variable. C-31 closes the
> false-positive gap by converting legitimate re-writers from anomalies into
> declared entries. The Contract Auditor (C-32) cross-checks AUTHORIZED_REWRITERS
> against the topology: every declared rewriter must appear in Phase 0-D-1; an
> AUTHORIZED_REWRITER referencing an undeclared topic is itself a CONTRACT_GAP
> finding. V-04 introduced AUTHORIZED_REWRITERS in Round 10; no prior round
> variation carried this field.
>
> C-32 requires a CONTRACT AUDITOR agent to verify, before trace execution begins
> (Phase 0-CA-1), that every session variable appearing in the topic topology
> (VARS_IN_TOPOLOGY) has a corresponding entry in the SESSION_VARIABLE_TIMELINE_CONTRACT
> (VARS_IN_CONTRACT). The Auditor produces a VARS_IN_TOPOLOGY vs VARS_IN_CONTRACT
> completeness delta; a non-empty delta is a CONTRACT_COMPLETENESS_FAILURE that
> blocks trace execution. This converts C-25 from a documentation requirement
> into a hard pre-execution gate: the contract cannot be accidentally incomplete
> when Phase 1 begins, because the Contract Auditor must sign off before the
> Developer proceeds. The CONTRACT AUDITOR role is structurally separate from
> both the Developer and the post-execution Auditor; its scope is exclusively
> contract completeness before execution. V-04 introduced this role in Round 10.
>
> C-33 requires Phase 6-A to include a CONTRACT_AUDIT_GATE_HONORED field
> confirming that the Contract Auditor gate (C-32) produced a PASS result before
> Phase 1 execution began. This closes the verification loop: Phase 0-CA-1
> opens the gate; Phase 6-A confirms the gate was honored and not bypassed.
> Without C-33, a trace could carry a populated Phase 0-CA-1 block but proceed
> to Phase 1 before the Auditor completed its review, satisfying the structural
> appearance of C-32 without the procedural guarantee. CONTRACT_AUDIT_GATE_HONORED:
> PASS requires the Phase 0-CA-1 delta to be empty (VARS_IN_TOPOLOGY =
> VARS_IN_CONTRACT) and must be the final entry in Phase 6-A before the
> Auditor certification. V-04 introduced this pattern in Round 10.
>
> C-34 requires Phase 5-A to declare a COVERAGE_QUALITY_GATE status — CLEAN or
> DEGRADED — as the headline before reporting the four coverage ratios. Status is
> DEGRADED whenever TIMELINE_ANOMALY_RATE > 0; under DEGRADED status all four
> coverage ratios carry PROVISIONAL designation. A Developer reporting PROVISIONAL
> topic and transition coverage must explicitly acknowledge that temporal ordering
> defects exist before any coverage claim is accepted by the Auditor. This
> prevents coverage-washing: a trace with TIMELINE_ANOMALY_RATE > 0 cannot report
> a clean coverage headline while embedding the anomaly rate as a fourth parallel
> entry in an undifferentiated list. CLEAN status requires TIMELINE_ANOMALY_RATE
> = 0. V-03 introduced COVERAGE_QUALITY_GATE in Round 10; prior variations
> reported all four ratios in parallel without a quality headline, making it
> possible to present strong topic and transition coverage alongside a non-zero
> anomaly rate without highlighting the contradiction.
>
> C-35 requires a SIMULATION_DELTA section comparing trace findings against what
> a team relying on manual review (STATUS_QUO) would have detected without
> simulation. The section identifies defects FOUND_BY_SIMULATION_ONLY (visible
> only through structured turn-by-turn tracing), defects FOUND_BY_BOTH, and any
> STATUS_QUO_GAP — the delta that justifies the simulation investment. The
> Auditor verifies SIMULATION_DELTA_COMPLETE: the section must enumerate every
> FOUND defect from Phase 3 and assign it to a detection-method category;
> uncategorized defects are an audit finding. This layer serves adoption: the
> artifact self-justifies against "we already reviewed this flow" resistance by
> quantifying what structured simulation found that prior manual review would have
> missed. V-02 introduced SIMULATION_DELTA in Round 10; the innovation is in the
> meta-narrative layer rather than in structural contract enforcement.
>
> C-36 requires each turn row in the Phase 1 turn table to carry a
> CONSTRAINT_VERDICTS column listing named constraint IDs (CONV-NN) evaluated
> against that turn, beyond the binary CONFORMANCE column required by C-11.
> CONSTRAINT_VERDICTS makes the specific invariant under test at each turn
> explicit: a DEVIATES verdict can be traced to the exact CONV-NN that failed
> rather than attributed to a generic conformance failure. Each CONV-NN must
> appear in the Phase 0-D-4 invariant register (C-14); a CONV-NN in
> CONSTRAINT_VERDICTS that has no Phase 0-D-4 entry is a CONTRACT_GAP finding.
> C-36 is additive to C-11: a turn must carry both a CONFORMANCE verdict (PASS
> condition for C-11) and a CONSTRAINT_VERDICTS list (PASS condition for C-36).
> V-05 introduced per-turn CONV-NN constraint IDs in Round 10.
>
> C-37 requires CONV-NN invariants involving session variable mutations to include
> arithmetic evidence: PRE (value before mutation), MUTATION (declared delta or
> operation), POST (value after mutation), and a CONV_NN_EVIDENCE CHECK confirming
> PRE + MUTATION = POST for additive operations or the equivalent for non-numeric
> mutations. This makes mutation correctness verifiable by inspection at the
> evidence layer rather than asserted at the conformance layer. A CONFORMANCE:
> CONFORMS verdict on a mutation invariant without CONV_NN_EVIDENCE is an
> unverified assertion; C-37 converts it into a verified proof. C-37 applies
> only to invariants with computable mutation semantics (numeric, boolean, or
> string-append); invariants with conditional or branching mutation semantics
> must declare a CONV_NN_EVIDENCE_CLASS: CONDITIONAL and provide the branch
> condition instead. V-05 introduced CONV_01_EVIDENCE arithmetic checks in Round
> 10.
>
> Aspirational denominator updated from 46 to 66.
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

## Aspirational Criteria (66 points total)

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
| C-30 | **Mutation-first authoring** | structure | 4 | Phase 1-S is authored before Phase 1 SESSION_STATE. SESSION_STATE is not independently authored; it is derived by replaying Phase 1-S mutations in turn order. Each SESSION_STATE cell cites the Phase 1-S entry from which it was reconstructed. Phase 6-E under mutation-first authoring verifies structural completeness — every turn has a mutation event; the replay accounts for every variable-turn combination — rather than hunting for discrepancies between two independently-authored tables. A trace satisfies C-26 with additive Phase 1-S authoring; C-30 requires mutation-first ordering. |
| C-31 | **AUTHORIZED_REWRITERS extension to timeline contract** | structure | 2 | The SESSION_VARIABLE_TIMELINE_CONTRACT (C-25) includes an AUTHORIZED_REWRITERS list per variable, declaring every topic permitted to write the variable beyond FIRST_WRITTEN_TOPIC. A write from a topic absent from both FIRST_WRITTEN_TOPIC and AUTHORIZED_REWRITERS is an OFF_CONTRACT_WRITE anomaly. A write from a declared AUTHORIZED_REWRITER is not an anomaly. The Contract Auditor (C-32) verifies that every AUTHORIZED_REWRITER appears in Phase 0-D-1; a rewriter referencing an undeclared topic is a CONTRACT_GAP finding. |
| C-32 | **Contract Auditor pre-execution completeness gate** | structure | 3 | Phase 0-CA-1 is authored by a CONTRACT AUDITOR agent whose sole scope is SESSION_VARIABLE_TIMELINE_CONTRACT completeness before trace execution begins. The Auditor produces a VARS_IN_TOPOLOGY vs VARS_IN_CONTRACT delta: every session variable appearing in the Phase 0-D-1 topic topology must have a contract entry. A non-empty delta is a CONTRACT_COMPLETENESS_FAILURE that blocks Phase 1 execution. The CONTRACT AUDITOR is structurally separate from both the Developer and the post-execution Auditor. Phase 0-CA-1 must be the final Phase 0 artifact before Phase 1 begins. |
| C-33 | **Phase 6-A CONTRACT_AUDIT_GATE_HONORED** | correctness | 2 | Phase 6-A includes a CONTRACT_AUDIT_GATE_HONORED field confirming that Phase 0-CA-1 produced an empty delta (VARS_IN_TOPOLOGY = VARS_IN_CONTRACT) before Phase 1 execution began. CONTRACT_AUDIT_GATE_HONORED: PASS must be the final entry in Phase 6-A before the post-execution Auditor certification. A trace carrying a populated Phase 0-CA-1 block but lacking CONTRACT_AUDIT_GATE_HONORED in Phase 6-A does not satisfy C-33; the gate requirement is fulfilled on paper only without the Phase 6-A verification close. |
| C-34 | **Coverage quality gate CLEAN\|DEGRADED** | correctness | 3 | Phase 5-A declares COVERAGE_QUALITY_GATE: CLEAN or DEGRADED as the headline before reporting the four coverage ratios. DEGRADED when TIMELINE_ANOMALY_RATE > 0; all four ratios carry PROVISIONAL designation under DEGRADED. A PROVISIONAL ratio must carry an explicit acknowledgment that temporal ordering defects exist; the Auditor may not accept a PROVISIONAL ratio as a clean coverage claim. CLEAN requires TIMELINE_ANOMALY_RATE = 0. A trace omitting the COVERAGE_QUALITY_GATE headline does not satisfy C-34 even if individual ratios are present. |
| C-35 | **SIMULATION_DELTA and STATUS_QUO_GAP** | behavior | 2 | A SIMULATION_DELTA section compares trace findings against STATUS_QUO (manual review without structured simulation). Each FOUND defect from Phase 3 is assigned to FOUND_BY_SIMULATION_ONLY or FOUND_BY_BOTH. The STATUS_QUO_GAP is the count and list of FOUND_BY_SIMULATION_ONLY defects. The Auditor verifies SIMULATION_DELTA_COMPLETE: every Phase 3 FOUND defect must appear in exactly one detection-method category; an uncategorized defect is an audit finding. The section need not appear in a numbered Phase but must be present before Auditor certification. |
| C-36 | **CONSTRAINT_VERDICTS per turn** | correctness | 2 | Every row in the Phase 1 turn table carries a CONSTRAINT_VERDICTS column listing the CONV-NN constraint IDs evaluated against that turn. CONSTRAINT_VERDICTS is additive to the CONFORMANCE column (C-11): both columns must be present. Each CONV-NN in CONSTRAINT_VERDICTS must appear in the Phase 0-D-4 invariant register; a CONV-NN referencing an unregistered invariant is a CONTRACT_GAP finding. A DEVIATES[CONV-NN] verdict in CONSTRAINT_VERDICTS takes precedence over a CONFORMS verdict in CONFORMANCE if evidence supports it; the Auditor flags any CONFORMANCE/CONSTRAINT_VERDICTS contradiction as a VERDICT_MISMATCH finding. |
| C-37 | **CONV_NN arithmetic evidence** | correctness | 2 | CONV-NN invariants involving session variable mutations include arithmetic evidence: PRE (value before mutation), MUTATION (declared delta or operation), POST (value after mutation), and a CONV_NN_EVIDENCE CHECK confirming PRE + MUTATION = POST for additive operations or the equivalent check for the declared operation type. Invariants with conditional or branching mutation semantics declare CONV_NN_EVIDENCE_CLASS: CONDITIONAL and provide the branch condition instead of an arithmetic check. A CONFORMANCE: CONFORMS verdict on a mutation invariant without CONV_NN_EVIDENCE is an unverified assertion; C-37 is not satisfied by verdict alone. |

---

## Scoring

| Tier | Points |
|------|--------|
| Essential (C-01 – C-04) | 60 |
| Recommended (C-05 – C-07) | 30 |
| Aspirational (C-08 – C-37) | 66 |
| **Max** | **156** |

PARTIAL credit on aspirational criteria: 0.5 × weight when the criterion is
structurally present but incompletely executed as specified.
```
