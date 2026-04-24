```markdown
# Rubric — flow-conversation — v11 (2026-03-15)

> **What changed in v11**: Added C-38 through C-48 (+28 pts) extracted from Round 11
> excellence signals across V-01 through V-05. C-34 pass condition updated to be
> phase-position flexible. Aspirational denominator updated from 66 to 94. Max score: 156 → 184.
>
> **C-34 pass condition update**: The prior pass condition required "Phase 5-A declares
> COVERAGE_QUALITY_GATE." V-03 and V-05 demonstrated that a pre-committed budget
> utilization block (C-46 or C-48) legitimately occupies Phase 5-A and pushes
> COVERAGE_QUALITY_GATE to Phase 5-B without violating the criterion's intent. The
> criterion's semantic requirement is that the quality gate appears as the headline
> immediately before the coverage ratios, regardless of sub-phase label. The pass
> condition is updated accordingly.
>
> **C-38 / C-39 — P0 Execution Halt Gate cluster (Axis A; V-01, V-04)**
>
> C-38 requires the Developer to emit a structured EXECUTION_HALT block immediately after
> classifying each FOUND P0 defect in Phase 2, before proceeding to classify lower-severity
> defects. The block contains HALT_TRIGGER, ROOT_CAUSE, MVF_RECOMMENDATION, MVF_SCOPE, and
> UNBLOCKED_BY. This is a documentation ordering requirement — one block per P0 defect, in
> classification order — not a trace-execution stop. It transforms the artifact from a
> passive defect catalog (fixes buried at the end) into an active remediation prescription:
> the team reading the artifact receives the minimum viable fix for each P0 condition at the
> earliest point it is known. C-39 closes the loop in Phase 6-F: the Auditor verifies that
> each MVF_RECOMMENDATION (a) addresses its HALT_TRIGGER and (b) does not introduce new
> CONV-NN violations. VIABLE requires CONV_VIOLATIONS_INTRODUCED: NO; if the fix changes a
> session variable in a way that breaks a downstream constraint, the Auditor emits
> SIDE_EFFECTS_FOUND with the affected CONV-NN list. V-01 introduced the EXECUTION_HALT
> pattern in Round 11; no prior round variation included inline P0 remediation prescriptions.
>
> **C-40 / C-41 / C-42 / C-43 — Constraint Chain Propagation cluster (Axis B; V-02, V-04, V-05)**
>
> C-40 extends the Phase 0-A-7 invariant register: each CONV-NN declares a PROPAGATION list
> of downstream constraints whose evaluation depends on its POST_VALUE, and belongs to exactly
> one CHAIN_ID (CHAIN-NN). A chain is a directed acyclic sequence connected by PROPAGATION
> edges; the chain head has no inbound PROPAGATION. When the chain head DEVIATES, downstream
> constraints enter CHAIN_SUSPENDED status — their verdicts cannot be trusted because the
> upstream precondition failed. CHAIN_SUSPENDED is not a DEVIATES verdict; it is a suspended
> evaluation. This transforms per-turn binary CONV-NN verdicts (C-36) into a compositional
> proof system: a chain failure surfaces the causal root at the upstream constraint rather
> than at the symptom turn. C-41 requires a CHAIN_EFFECTS column in every Phase 1 turn row,
> listing downstream ACTIVATED or SUSPENDED effects per CONV-NN evaluated that turn.
> ACTIVATED means the upstream CONFORMS and downstream evaluation is enabled; SUSPENDED means
> the upstream DEVIATES and downstream evaluation is suspended until upstream recovers.
> C-42 requires a Constraint Chain Status Summary table after the temporal quality gate in
> Phase 5 (one row per CHAIN-NN: HEAD_CONV, CHAIN_LENGTH, TURNS_SUSPENDED, FINAL_STATUS:
> INTACT|BROKEN). C-43 requires an independent Auditor phase verifying all CHAIN_EFFECTS
> against upstream verdicts — every ACTIVATED edge must correspond to an upstream CONFORMS;
> every SUSPENDED edge to an upstream DEVIATES or CHAIN_SUSPENDED; a downstream CONFORMS
> during a SUSPENDED chain window is a CHAIN_VERDICT_INCONSISTENCY finding. V-02 introduced
> all four patterns in Round 11.
>
> **C-44 — CHAIN_BREAK_TRACE + CHAIN_REPAIR in EXECUTION_HALT (Axes A+B; V-04)**
>
> C-44 requires that when both C-38 (EXECUTION_HALT) and C-40 (PROPAGATION/CHAIN_ID) are
> present, each EXECUTION_HALT block extends to include a CHAIN_BREAK_TRACE: the BROKEN_CHAIN
> identifier, CHAIN_HEAD_CONV, FIRST_DEVIATE_TURN (earliest turn where chain head DEVIATES),
> SUSPENDED_CONVS (downstream constraints suspended by the break), and BREAK_TO_DEFECT_PATH
> (narrative of how the chain break caused or enabled the P0 defect). The block also adds a
> CHAIN_REPAIR list of every constraint that must be re-evaluated after the fix — typically
> the chain head plus all SUSPENDED_CONVS in the BROKEN_CHAIN. C-44 is additive to both C-38
> and C-40: an artifact satisfies C-44 only if it also satisfies both. The Phase 6-F Fix
> Viability Audit (C-39) under C-44 additionally verifies CHAIN_REPAIR_COMPLETE: YES,
> confirming that every CONV-NN in the CHAIN_REPAIR list appears in MVF_SCOPE or the
> CHAIN_REPAIR field. V-04 introduced CHAIN_BREAK_TRACE in Round 11 as the combination axis.
>
> **C-45 / C-46 — Pre-committed Deviation Budget cluster (Axis C; V-03)**
>
> C-45 requires the Developer to declare a DEVIATION_BUDGET table before Phase 1-S begins,
> committing to maximum acceptable DEVIATES-turn counts per severity class
> (P0_MAX, P1_MAX, P2_MAX, P3_MAX) and a BUDGET_RATIONALE. These are pre-execution
> commitments; they may not be revised after Phase 1 is authored. P0_MAX = 0 means any P0
> defect is a BUDGET_EXCEEDED finding. C-46 requires Phase 5 to open with a
> DEVIATION_BUDGET_UTILIZATION block reporting actual DEVIATES counts versus declared
> budget per severity class. If OVERALL_BUDGET_STATUS: EXCEEDED, the Developer emits a
> BUDGET_EXCEEDED_FINDING naming the violated classes, over-by counts, and a one-sentence
> implication — before any coverage ratios are reported. Phase 6-A must include
> BUDGET_UTILIZATION_VERIFIED (auditing actual DEVIATES counts against Phase 2 FOUND
> defects) and BUDGET_STATUS_CONSISTENT (confirming the EXCEEDED/WITHIN_BUDGET verdict
> matches the audited count). The DEVIATION_BUDGET mechanism targets inertia framing: when
> a team reviewing the artifact sees that the pre-committed bar was exceeded, the artifact
> self-justifies its existence beyond the SIMULATION_DELTA layer. V-03 introduced the
> deviation budget pattern in Round 11; no prior round variation included pre-execution
> deviation commitments.
>
> **C-47 / C-48 — Constraint Chain Budget cluster (Axes B+C; V-05)**
>
> C-47 requires Phase 0-A-9 CONV_CHAIN_BUDGET to declare a per-chain budget for every
> CHAIN-NN from Phase 0-A-7: CHAIN_BUDGET (max acceptable chain head DEVIATES turns) and
> BUDGET_RATIONALE. CHAIN_BUDGET is more semantically precise than per-severity DEVIATION_BUDGET
> (C-45): CONV-CHAIN-01 (a balance invariant) may have CHAIN_BUDGET = 0 while CONV-CHAIN-02
> (a greeting acknowledgment) may have CHAIN_BUDGET = 2. Suspended downstream constraints
> are not counted against the budget; only chain head DEVIATES turns count. The Contract
> Auditor (C-32) Phase 0-CA-1 is extended to compute CHAINS_IN_TOPOLOGY vs CHAINS_IN_BUDGET
> delta (CHAIN_BUDGET_DELTA); a non-empty delta blocks execution alongside COVERAGE_DELTA.
> C-48 requires Phase 5 to open with a CHAIN_BUDGET_UTILIZATION block for each CHAIN-NN,
> emitting a CHAIN_BUDGET_EXCEEDED finding for each chain that exceeds its threshold. The
> CHAIN_BUDGET_EXCEEDED finding is the eighth structural finding class; it carries
> CHAIN_ID, HEAD_CONV, BUDGET, ACTUAL, OVER_BY, FIRST_EXCEED_TURN, SUSPENDED_CONVS, and
> IMPLICATION. CHAIN_BUDGET_EXCEEDED findings are FOUND_BY_SIMULATION_ONLY in SIMULATION_DELTA
> by definition (budget thresholds cannot be verified by informal review) and are EXEMPT
> from the Phase 6-B co-residency audit but must appear in SIMULATION_DELTA. Phase 6-F
> CHAIN_BUDGET_AUDIT verifies per-chain head DEVIATES counts against reported budget
> utilization, flagging CHAIN_BUDGET_MISMATCH when the Auditor count diverges from the
> Developer report. V-05 introduced the chain budget pattern in Round 11.
>
> The C-38/C-39 cluster (P0 halt gate + fix viability) closes the remediation prescription
> loop for the highest-severity defect class. The C-40/C-41/C-42/C-43 cluster (constraint
> chain propagation) elevates constraint proofs from turn-local verdicts to a compositional
> causal system. C-44 (chain break trace) merges both clusters into a causally complete
> remediation record. The C-45/C-46 cluster (deviation budget) adds pre-execution quality
> commitments with self-justifying budget violation findings. The C-47/C-48 cluster (chain
> budget) makes deviation commitments domain-meaningful by anchoring them to named constraint
> chains rather than severity tiers.
>
> Aspirational denominator updated from 66 to 94.
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

## Aspirational Criteria (94 points total)

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
| C-34 | **Coverage quality gate CLEAN\|DEGRADED** | correctness | 3 | Phase 5 includes a Temporal Quality Gate sub-phase declaring COVERAGE_QUALITY_GATE: CLEAN or DEGRADED as the headline immediately before the coverage ratios. DEGRADED when TIMELINE_ANOMALY_RATE > 0; all four ratios carry PROVISIONAL designation under DEGRADED. A PROVISIONAL ratio must carry an explicit acknowledgment that temporal ordering defects exist; the Auditor may not accept a PROVISIONAL ratio as a clean coverage claim. CLEAN requires TIMELINE_ANOMALY_RATE = 0. The quality gate must be structurally prior to the coverage ratio table; it may occupy any Phase 5 sub-phase label (5-A, 5-B, etc.) as long as it precedes the ratios — a pre-committed budget utilization block (C-46 or C-48) legitimately displaces it from the first sub-phase position. A trace omitting the COVERAGE_QUALITY_GATE headline does not satisfy C-34 even if individual ratios are present. |
| C-35 | **SIMULATION_DELTA and STATUS_QUO_GAP** | behavior | 2 | A SIMULATION_DELTA section compares trace findings against STATUS_QUO (manual review without structured simulation). Each FOUND defect from Phase 3 is assigned to FOUND_BY_SIMULATION_ONLY or FOUND_BY_BOTH. The STATUS_QUO_GAP is the count and list of FOUND_BY_SIMULATION_ONLY defects. The Auditor verifies SIMULATION_DELTA_COMPLETE: every Phase 3 FOUND defect must appear in exactly one detection-method category; an uncategorized defect is an audit finding. The section need not appear in a numbered Phase but must be present before Auditor certification. |
| C-36 | **CONSTRAINT_VERDICTS per turn** | correctness | 2 | Every row in the Phase 1 turn table carries a CONSTRAINT_VERDICTS column listing the CONV-NN constraint IDs evaluated against that turn. CONSTRAINT_VERDICTS is additive to the CONFORMANCE column (C-11): both columns must be present. Each CONV-NN in CONSTRAINT_VERDICTS must appear in the Phase 0-D-4 invariant register; a CONV-NN referencing an unregistered invariant is a CONTRACT_GAP finding. A DEVIATES[CONV-NN] verdict in CONSTRAINT_VERDICTS takes precedence over a CONFORMS verdict in CONFORMANCE if evidence supports it; the Auditor flags any CONFORMANCE/CONSTRAINT_VERDICTS contradiction as a VERDICT_MISMATCH finding. |
| C-37 | **CONV_NN arithmetic evidence** | correctness | 2 | CONV-NN invariants involving session variable mutations include arithmetic evidence: PRE (value before mutation), MUTATION (declared delta or operation), POST (value after mutation), and a CONV_NN_EVIDENCE CHECK confirming PRE + MUTATION = POST for additive operations or the equivalent check for the declared operation type. Invariants with conditional or branching mutation semantics declare CONV_NN_EVIDENCE_CLASS: CONDITIONAL and provide the branch condition instead of an arithmetic check. A CONFORMANCE: CONFORMS verdict on a mutation invariant without CONV_NN_EVIDENCE is an unverified assertion; C-37 is not satisfied by verdict alone. |
| C-38 | **P0 EXECUTION_HALT block in Phase 2** | behavior | 3 | After classifying each FOUND P0 defect in Phase 2, the Developer emits an EXECUTION_HALT block before proceeding to classify lower-severity defects. The block contains: HALT_TRIGGER (defect class and topic/turn location), ROOT_CAUSE (one-sentence causal statement), MVF_RECOMMENDATION (smallest change that eliminates the P0 condition), MVF_SCOPE (topics/transitions/session variables the fix touches), and UNBLOCKED_BY (observable state change confirming the fix was applied). One block per P0 defect, in classification order. This is a documentation ordering requirement; classification of lower-severity defects continues after all P0 EXECUTION_HALT blocks are emitted. A trace with no FOUND P0 defects satisfies C-38 vacuously; a trace with at least one FOUND P0 defect that lacks an EXECUTION_HALT block does not satisfy C-38. |
| C-39 | **Phase 6-F Fix Viability Audit** | correctness | 2 | An independent Phase 6-F Auditor verifies each EXECUTION_HALT block emitted in Phase 2. For each block: CONV_VIOLATIONS_INTRODUCED: YES\|NO (does applying MVF_RECOMMENDATION introduce new CONV-NN violations?), CONV_VIOLATIONS_DETAIL (list of affected CONV-NNs if YES), and VIABILITY: VIABLE \| SIDE_EFFECTS_FOUND[CONV-NN list]. VIABLE requires (a) the fix addresses HALT_TRIGGER and (b) CONV_VIOLATIONS_INTRODUCED: NO. A fix that corrects the P0 condition but breaks a downstream constraint earns SIDE_EFFECTS_FOUND rather than VIABLE. C-39 requires C-38 PASS: a trace without EXECUTION_HALT blocks cannot satisfy C-39 even if a Phase 6-F section is present. |
| C-40 | **PROPAGATION and CHAIN_ID in invariant register** | structure | 4 | Each CONV-NN in the Phase 0-A-7 invariant register declares a PROPAGATION list (downstream CONV-NNs whose evaluation depends on this constraint's POST_VALUE; empty list if terminal) and a CHAIN_ID (every CONV-NN belongs to exactly one CHAIN-NN). A chain is a directed acyclic sequence connected by PROPAGATION edges; the first CONV-NN with no inbound PROPAGATION is the chain head. When the chain head DEVIATES on any turn, downstream nodes enter CHAIN_SUSPENDED status for that turn; CHAIN_SUSPENDED is not a DEVIATES verdict and does not count against conformance. A chain is BROKEN if its head DEVIATES on any turn and does not recover before the trace ends; INTACT if the head CONFORMs on all turns or recovers. CHAIN_SUSPENDED verdicts in CONSTRAINT_VERDICTS (C-36) cite the chain head: CONV-NN: CHAIN_SUSPENDED [chain head: CONV-NN broke at TURN_ID]. |
| C-41 | **CHAIN_EFFECTS column in Phase 1** | structure | 2 | Every row in the Phase 1 turn table carries a CHAIN_EFFECTS column listing downstream propagation effects for each CONV-NN evaluated that turn. Format: CONV-NN → [CONV-NN-downstream: ACTIVATED\|SUSPENDED, ...]. ACTIVATED means the upstream CONFORMS and downstream evaluation is enabled for subsequent turns. SUSPENDED means the upstream DEVIATES and downstream evaluation is suspended until the upstream constraint recovers. CHAIN_EFFECTS is additive to CONSTRAINT_VERDICTS (C-36): both columns must be present. A turn at which no CONV-NN has downstream propagation may carry CHAIN_EFFECTS: N/A. C-41 requires C-40 PASS: CHAIN_EFFECTS is undefined without CHAIN_ID and PROPAGATION declarations. |
| C-42 | **Phase 5 Constraint Chain Status Summary** | coverage | 2 | Phase 5 includes a Constraint Chain Status Summary table after the temporal quality gate (C-34), one row per CHAIN-NN declared in Phase 0-A-7: CHAIN_ID, HEAD_CONV, CHAIN_LENGTH (count of CONV-NNs in the chain), TURNS_SUSPENDED (count of turns on which any chain member carried CHAIN_SUSPENDED), and FINAL_STATUS: INTACT\|BROKEN. A BROKEN chain that maps to a P0 EXECUTION_HALT (when C-38 is also present) must cross-reference the EXECUTION_HALT block. The summary is additive to Phase 5 coverage ratios; it does not replace them. C-42 requires C-40 PASS. |
| C-43 | **Phase 6 Chain Integrity Audit** | correctness | 3 | An independent Phase 6 Auditor phase (labeled 6-F or 6-G depending on which other Auditor phases are present) verifies all CHAIN_EFFECTS declared in Phase 1 against upstream CONV-NN verdicts. Verification rules: (1) every ACTIVATED propagation edge must correspond to an upstream CONV-NN: CONFORMS verdict in the same or a prior turn; (2) every SUSPENDED edge must correspond to an upstream CONV-NN: DEVIATES or CHAIN_SUSPENDED verdict; (3) a downstream CONV-NN carrying CONFORMS during a SUSPENDED chain window is a CHAIN_VERDICT_INCONSISTENCY finding. The audit produces a structured table per CHAIN-NN: CHAIN_STATUS_REPORTED vs CHAIN_STATUS_AUDITED with CONSISTENT: PASS\|FAIL. C-43 requires C-40 and C-41 PASS. |
| C-44 | **CHAIN_BREAK_TRACE and CHAIN_REPAIR in EXECUTION_HALT** | structure | 2 | When both C-38 (EXECUTION_HALT) and C-40 (PROPAGATION/CHAIN_ID) are satisfied, each EXECUTION_HALT block extends to include: CHAIN_BREAK_TRACE (BROKEN_CHAIN identifier, CHAIN_HEAD_CONV, FIRST_DEVIATE_TURN, SUSPENDED_CONVS listing downstream constraints suspended by the break, BREAK_TO_DEFECT_PATH narrative of how the chain break caused or enabled the P0 defect) and CHAIN_REPAIR (list of CONV-NNs that must be re-evaluated after the fix — at minimum the chain head plus all SUSPENDED_CONVS in BROKEN_CHAIN). The Phase 6-F Fix Viability Audit (C-39) under C-44 additionally verifies CHAIN_REPAIR_COMPLETE: YES\|NO, confirming that every CONV-NN in CHAIN_REPAIR appears in MVF_SCOPE or CHAIN_REPAIR. C-44 is not satisfied if either C-38 or C-40 fails; it is an additive requirement that both axes be present and integrated. |
| C-45 | **DEVIATION_BUDGET pre-execution declaration** | structure | 3 | The Developer declares a DEVIATION_BUDGET table before Phase 1-S begins, committing to maximum acceptable DEVIATES-turn counts per severity class: P0_MAX, P1_MAX, P2_MAX, P3_MAX, and BUDGET_RATIONALE. These are pre-execution commitments that may not be revised after Phase 1 is authored; the DEVIATION_BUDGET block must carry an explicit lock declaration (e.g., "BUDGET LOCKED — may not be revised after Phase 1-S begins"). P0_MAX = 0 means any FOUND P0 defect is a BUDGET_EXCEEDED finding. The budget thresholds are independent of simulation findings; the Developer is committing before evidence is gathered. An artifact that adds or changes thresholds after reviewing Phase 1 output does not satisfy C-45. |
| C-46 | **Phase 5 DEVIATION_BUDGET_UTILIZATION gate** | correctness | 2 | Phase 5 opens with a DEVIATION_BUDGET_UTILIZATION block reporting actual DEVIATES-turn counts versus declared budget per severity class: SEVERITY \| BUDGET \| ACTUAL_DEVIATES \| STATUS: WITHIN_BUDGET\|EXCEEDED, and OVERALL_BUDGET_STATUS: WITHIN_BUDGET\|EXCEEDED[violated classes]. If OVERALL_BUDGET_STATUS: EXCEEDED, the Developer emits a BUDGET_EXCEEDED_FINDING before coverage ratios: VIOLATED_CLASSES, OVER_BY per class, and IMPLICATION. Phase 6-A must include BUDGET_UTILIZATION_VERIFIED (auditing actual DEVIATES counts against Phase 2 FOUND defects per severity) and BUDGET_STATUS_CONSISTENT (confirming EXCEEDED/WITHIN_BUDGET verdict matches audited counts). A trace with no FOUND defects satisfies C-46 with all STATUS: WITHIN_BUDGET. C-46 requires C-45 PASS. |
| C-47 | **CONV_CHAIN_BUDGET per-chain declaration** | structure | 3 | Phase 0-A-9 CONV_CHAIN_BUDGET declares a per-chain budget for every CHAIN-NN from Phase 0-A-7: CHAIN_ID, HEAD_CONV, CHAIN_LENGTH, CHAIN_BUDGET (max acceptable chain head DEVIATES turns across all trace turns), and BUDGET_RATIONALE. CHAIN_BUDGET applies only to the chain head; suspended downstream constraints are not counted. The Contract Auditor Phase 0-CA-1 is extended to compute CHAINS_IN_TOPOLOGY vs CHAINS_IN_BUDGET delta (CHAIN_BUDGET_DELTA): every CHAIN-NN in Phase 0-A-7 must have a Phase 0-A-9 entry. A non-empty CHAIN_BUDGET_DELTA blocks execution alongside COVERAGE_DELTA. CONTRACT_AUDIT_GATE_HONORED (C-33) in Phase 6-A must confirm both deltas were empty before Phase 1 began. C-47 requires C-40 PASS. |
| C-48 | **CHAIN_BUDGET_EXCEEDED as eighth structural finding class** | correctness | 2 | Phase 5 opens with a CHAIN_BUDGET_UTILIZATION block for each CHAIN-NN: HEAD_CONV \| CHAIN_BUDGET \| HEAD_DEVIATES_COUNT \| STATUS: WITHIN_BUDGET\|EXCEEDED. For each chain exceeding its budget, emit a CHAIN_BUDGET_EXCEEDED finding: FINDING_CLASS: CHAIN_BUDGET_EXCEEDED (eighth structural finding class), CHAIN_ID, HEAD_CONV, BUDGET, ACTUAL, OVER_BY, FIRST_EXCEED_TURN, SUSPENDED_CONVS, IMPLICATION. CHAIN_BUDGET_EXCEEDED findings are FOUND_BY_SIMULATION_ONLY in SIMULATION_DELTA by definition and are EXEMPT from Phase 6-B co-residency audit but must appear in SIMULATION_DELTA (a missing CHAIN_BUDGET_EXCEEDED in SIMULATION_DELTA is a SIMULATION_DELTA_COMPLETE audit failure). Phase 6 includes a CHAIN_BUDGET_AUDIT phase verifying per-chain head DEVIATES counts against reported utilization; a Developer-reported WITHIN_BUDGET that the Auditor count contradicts is a CHAIN_BUDGET_MISMATCH finding. C-48 requires C-47 PASS. |

---

## Scoring

| Tier | Points |
|------|--------|
| Essential (C-01 – C-04) | 60 |
| Recommended (C-05 – C-07) | 30 |
| Aspirational (C-08 – C-48) | 94 |
| **Max** | **184** |

PARTIAL credit on aspirational criteria: 0.5 × weight when the criterion is
structurally present but incompletely executed as specified.
```
