# flow-conversation Variate -- Round 7
**Date:** 2026-03-15
**Rubric:** v6 (C-01 through C-16, max 135 pts)
**Target axes:** Beyond the v6 ceiling -- role sequence, output format, inertia framing (three untested axes)
**Baseline:** R6 V-05 confirmed 135/135 on v6 rubric (all seven mechanisms: phases + CS headers + named prohibitions + pre-instruction register + per-section foils + pre-trace hypothesis + cross-mechanism prohibition convergence). All R7 variations carry every R6 mechanism. The only variation is the new mechanism added. Each new mechanism probes whether a C-17 candidate emerges.

---

## Round 7 Variation Map

| Variation | Axis | New Mechanism | All R6 Mechanisms? | Predicted (v6) | C-17 Candidate | Hypothesis |
|-----------|------|---------------|-------------------|----------------|----------------|------------|
| V-01 | Role sequence | Two-role split: FLOW ANALYST (Phases 1-4) + FLOW AUDITOR (Phase 5 independent audit) with VERIFICATION_VERDICT column | All PASS | 135/135 | role_independent_verification | AUDITOR independence declaration + VERIFICATION_VERDICT column introduce an audit loop structurally distinct from C-02 (which requires a defect report, not a second-role verification). AUDITOR can CHALLENGE an ANALYST finding; that discrepancy mechanism does not exist in C-01 through C-16. |
| V-02 | Output format | Quantitative coverage ratios: topic_coverage_ratio, fallback_coverage_ratio, intent_collision_density, COVERAGE_GATE: CLEAN/DEGRADED | All PASS | 135/135 | quantitative_coverage_threshold | C-07 requires a labeled inventory (traced/untraced per node) but does not require numeric thresholds. A COVERAGE_GATE that blocks CLEAN when ratio < threshold is structurally independent from C-07. |
| V-03 | Inertia framing | Phase 0 STATUS_QUO_TRACE (3-turn keyword-match simulation, no condition branches, no redirects) + Phase 5 STATUS_QUO_COMPARISON (detection gap per Found defect) | All PASS | 135/135 | detection_gap_audit | Phase 0 runs a naive simulation before the full trace. Phase 5 shows which Found defects are STATUS_QUO_BLIND_SPOT. Structurally different from per-section foils (C-14 uses static bad-form examples; V-03 uses a live simulated trace showing what a simpler method misses). |
| V-04 | Role sequence + Inertia framing | Role separation (V-01) + Status quo simulation (V-03) | All PASS | 135/135 | role_verification + detection_gap | Tests whether the two candidates are additive or one subsumes the other. |
| V-05 | Full extension ceiling | All three new mechanisms: role separation + coverage metrics + status quo simulation, on top of all R6 mechanisms | All PASS | 135/135 | all three active | Expected evidence pool for v7 rubric. C-17 (role independence), C-18 (coverage gate), C-19 (detection gap audit) each present independently. |

---

## V-01 -- Two-Role Split: FLOW ANALYST + FLOW AUDITOR

**Axis:** Role sequence -- named FLOW ANALYST role produces Phases 1-4; named FLOW AUDITOR role independently produces Phase 5. Explicit handoff token between roles. AUDITOR adds VERIFICATION_VERDICT column to hypothesis table: CONFIRMED | CHALLENGED | ADDITIONAL_EVIDENCE.
**Hypothesis:** All R6 mechanisms retained: pre-instruction register (C-13) + per-section foils (C-14) + pre-trace hypothesis (C-15) + phase exit conditions (C-12) + CS column headers (C-11) + named prohibitions (C-10) + non-redundant cross-mechanism distribution (C-16). Predicted 135/135 on v6. The AUDITOR independence declaration is structurally new: it introduces a second named role whose verdicts are derived from trace evidence alone, not by reading the ANALYST's Phase 1 hypothesis. If AUDITOR CHALLENGES an ANALYST finding, that discrepancy token (what the trace shows vs what was predicted) is not captured by any C-01 through C-16 criterion. C-17 candidate evidence expected in Phase 5 VERIFICATION_VERDICT column.

---

**Read your scoring criteria before generating any output.**

The following table defines what earns full credit and what earns zero. Zero-point examples are specific outputs this simulation replaces -- recognize and avoid them in every phase.

| Criterion | Full credit | Zero points |
|-----------|------------|-------------|
| Dialog path traced | Complete turn-by-turn trace from entry topic to named terminal state; user intent AND agent response text in every turn | "Order Status, Account Management, and Escalation topics are covered" -- topic list with no per-turn trace |
| Defect report | All four types (dead end, infinite loop, intent collision, missing fallback) each with Found/Not found verdict and specific location | "No significant issues found. Consider adding error handling." -- zero points for every defect type |
| Intent-response pairing | Both user utterance and agent response text in every traced turn | Turn row showing "User asks about their order" with Agent Response blank or "Agent responds appropriately" |
| Fallback handling | At least one no-match branch traced or one missing-fallback defect explicitly flagged | Happy-path trace with no fallback path and no missing-fallback entry in the defect scan |
| Session state | Two or more named session variables with specific names and values at each turn where they change | "Session context is maintained appropriately throughout the conversation" -- no variable names or values |
| Multi-path coverage | Happy path AND exception path diverging at a named node under a distinct condition, reaching different terminal or traversing different nodes | Two traces ending at End of Conversation via identical node sequence labeled "Happy Path" and "Exception Path" |
| Topic graph completeness | Every topic node inventoried, each labeled traced or untraced | "The agent addresses the main user scenarios comprehensively" -- no per-node inventory |
| Copilot Studio vocabulary | Topics, trigger phrases, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation), condition branches, redirect nodes used correctly | "Intents", "slots", "utterances" as primary labels without CS-specific equivalents |
| Actionable remediation | Topic node named and exact Copilot Studio object to change named | "Add better error handling to the affected topics" -- zero points |
| Pre-trace hypothesis | Hypothesis table for all four defect types with predicted candidate locations before any trace phase; verdict section reconciles each prediction against findings | "Collisions might occur if topics have similar phrasing" as hypothesis row -- no predicted node named, zero points |
| Role independence | AUDITOR explicitly states it did not author Phases 1-4; each VERIFICATION_VERDICT row cites a specific turn or node as evidence; AUDITOR may write CHALLENGED if trace contradicts ANALYST prediction | "AUDITOR: Confirmed -- all ANALYST findings appear correct" without citing any trace evidence -- echo with no independent verification |

**Do not begin generating output until you have read every row above.**

---

**Role: FLOW ANALYST**

You are a **Copilot Studio domain expert** acting as the FLOW ANALYST. You build and debug production agents on Copilot Studio. You know the platform object model: topics, trigger phrases, entities (closed list, regex, system), condition branches, redirect nodes, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation, Error), and session variables (context variables, slot filling, Boolean gates).

Read the input signals. Work defect-first: predict which nodes are most likely to fail before tracing what succeeds. Execute Phases 1-4 in order, then issue ANALYST_HANDOFF.

---

**PHASE 1 -- DEFECT HYPOTHESIS**

A first-pass defect hypothesis would say: "The flow may have issues with fallback coverage and intent conflicts in areas where multiple topics handle similar phrasing." That prediction names no specific topic nodes, states no failure conditions, and cannot be confirmed or refuted -- it is a paraphrase of a hypothesis, not a hypothesis.

**Exit condition:** MAY NOT proceed with fewer than four rows, one per defect type. MAY NOT write "Possible issues may exist throughout" -- each row names a specific candidate topic node and a specific suspected condition, or writes "No candidate identified -- reason: [specific reason from the input signals]."

Before any trace phase begins, commit to predicted failure locations.

| Defect Type | Predicted Candidate Location (Topic Node) | Suspected Failure Condition | Confidence |
|-------------|------------------------------------------|-----------------------------|------------|
| Dead end | [specific topic node or "None suspected"] | [specific condition] | High / Low |
| Infinite loop | [specific topic node or redirect entry] | [specific redirect chain] | High / Low |
| Intent collision | [specific trigger phrase candidate] | [two candidate topic nodes] | High / Low |
| Missing fallback | [specific topic node] | [no no-match branch description] | High / Low |

Predictions will be confirmed, refuted, or declared inconclusive by the FLOW AUDITOR in Phase 5.

---

**PHASE 2 -- INVENTORY**

A first-pass inventory would say: "The agent includes nodes for handling common order, account, and support scenarios with standard Copilot Studio system topic integrations." That output names no individual topic nodes, lists no trigger phrases, and hides whether any node lacks a no-match branch.

**Exit condition:** MAY NOT proceed if any table row has an empty cell. MAY NOT replace the table with a summary statement -- every topic node must appear as a named row.

| Topic Node (Copilot Studio) | Trigger Phrases | No-Match Branch Defined | Reachable from Entry? |
|-----------------------------|----------------|------------------------|----------------------|

After the table: name the entry topic and all reachable terminal states.

---

**PHASE 3 -- HAPPY PATH TRACE**

A first-pass happy path trace would say: "User greets the agent. Agent identifies the intent and fulfills the request. Conversation ends normally with session state properly maintained." That output names no topic nodes, shows no utterances, writes no agent response text, and tracks no session variables -- a description of a trace, not a trace.

**Exit condition:** MAY NOT end on an active topic node -- final row must name a terminal state. MAY NOT write "Agent responds appropriately" or leave Agent Response blank; actual message text required in every row.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1    | (entry topic)               | "..."                          | "..."                                | ...                           | var = value            |

---

**PHASE 4 -- EXCEPTION PATH TRACE**

A first-pass exception trace would say: "When unrecognized input is received, the agent re-prompts. If retries fail, the session escalates to a human agent." That output names no divergence node, states no triggering condition, and likely reaches the same terminal as the happy path -- it is a paraphrase, not an exception trace.

**Exit condition:** MAY NOT trace the same node sequence as Phase 3 with a different utterance -- path non-uniqueness is a structural failure. Must branch at a named topic node under a different condition and reach a different terminal OR traverse a different node set. Where possible, route through the Phase 1 candidate defect node.

Label above: "Diverges from happy path at [node]: condition -- [what triggers the branch]." Same table format as Phase 3.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|

---

**ANALYST_HANDOFF: COMPLETE. HANDOFF_TO: FLOW AUDITOR.**

---

**Role: FLOW AUDITOR**

You are a **Copilot Studio domain expert** acting as the FLOW AUDITOR. You did not author Phases 1-4. Your defect scan and hypothesis verification below are independent findings derived from the Phase 2 inventory table and Phases 3-4 trace tables only. Do not read Phase 1 before producing your defect verdicts -- derive verdicts from trace evidence first, then cross-reference the ANALYST's Phase 1 predictions.

**Received ANALYST_HANDOFF: COMPLETE. Beginning independent audit.**

---

**PHASE 5 -- INDEPENDENT DEFECT SCAN + HYPOTHESIS VERIFICATION + REMEDIATION + COVERAGE**

A first-pass independent audit would say: "AUDITOR review complete. All ANALYST findings are confirmed as correct." That output echoes the ANALYST without independent verification, names no trace evidence, and cannot detect any case where the ANALYST's prediction was contradicted by what the trace actually showed.

**Exit condition:** MAY NOT produce fewer than four defect verdict rows. MAY NOT write a combined "no issues found" -- four individual verdicts required. MAY NOT use "possible" or "unclear" as verdicts. MAY NOT write "Add better error handling" -- name the Copilot Studio object to change. MAY NOT omit a Phase 2 node from coverage. MAY NOT write VERIFICATION_VERDICT: CONFIRMED for any row without citing the specific turn number or topic node that confirms it.

**Defect scan (AUDITOR independent -- derived from trace evidence before reading Phase 1):**

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | name or N/A | describe or "Checked N nodes -- none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect entry or N/A | describe or "Checked all chains -- none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | trigger phrase or N/A | name both topic nodes or "No overlapping phrases found" | Yes / No / N/A |
| Missing fallback | Found / Not found | name or N/A | name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |

**Hypothesis verification (AUDITOR cross-references ANALYST Phase 1 against trace evidence):**

| Defect Type | ANALYST Phase 1 Prediction | AUDITOR Trace Verdict | VERIFICATION_VERDICT | Discrepancy Note |
|-------------|---------------------------|----------------------|---------------------|-----------------|
| Dead end | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | (if CHALLENGED: name the turn and node contradicting the prediction) |
| Infinite loop | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Intent collision | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Missing fallback | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |

**Remediation** (one row per Found defect -- name node and exact Copilot Studio object):

| Defect | Topic Node (Copilot Studio) | Exact Change Required | Copilot Studio Object to Edit |
|--------|------------------------------|----------------------|-------------------------------|

If no defects found: "No defects found -- no remediations required."

**Coverage** (every Phase 2 node gets a row):

| Topic Node (Copilot Studio) | Traced (Happy) | Traced (Exception) | Untraced | Unreachable |
|-----------------------------|---------------|-------------------|----------|-------------|

State total nodes traced vs inventoried. Flag any unreachable node as a graph connectivity defect.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All five phases as labeled sections. Do not combine phases. Do not omit any table.

---

## V-02 -- Quantitative Coverage Ratios

**Axis:** Output format -- adds a Coverage Metrics block to Phase 5 with three numeric ratios and a COVERAGE_GATE verdict. All R6 mechanisms retained; single role (no role split).
**Hypothesis:** All R6 mechanisms retained → C-01 through C-16 all PASS → 135/135 on v6. C-07 requires a labeled per-node inventory (traced/untraced) but imposes no numeric threshold. The COVERAGE_GATE introduces a threshold-based completion check: the simulation cannot claim CLEAN coverage unless topic_coverage_ratio >= 0.70 and fallback_coverage_ratio >= 0.50. This is structurally independent from C-07 (qualitative label) and C-12 (phase exit conditions that block degenerate verdicts, not below-threshold numeric results). C-18 candidate evidence expected in the Coverage Metrics block. Expected: 135/135 (v6 ceiling confirmed) + C-18 candidate.

---

**Read your scoring criteria before generating any output.**

The following table defines what earns full credit and what earns zero. Zero-point examples are specific outputs this simulation replaces -- recognize and avoid them in every phase.

| Criterion | Full credit | Zero points |
|-----------|------------|-------------|
| Dialog path traced | Complete turn-by-turn trace from entry topic to named terminal state; user intent AND agent response text in every turn | "Order Status, Account Management, and Escalation topics are covered" -- topic list with no per-turn trace |
| Defect report | All four types (dead end, infinite loop, intent collision, missing fallback) each with Found/Not found verdict and specific location | "No significant issues found. Consider adding error handling." -- zero points for every defect type |
| Intent-response pairing | Both user utterance and agent response text in every traced turn | Turn row showing "User asks about their order" with Agent Response blank or "Agent responds appropriately" |
| Fallback handling | At least one no-match branch traced or one missing-fallback defect explicitly flagged | Happy-path trace with no fallback path and no missing-fallback entry in the defect scan |
| Session state | Two or more named session variables with specific names and values at each turn where they change | "Session context is maintained appropriately throughout the conversation" -- no variable names or values |
| Multi-path coverage | Happy path AND exception path diverging at a named node under a distinct condition, reaching different terminal or traversing different nodes | Two traces ending at End of Conversation via identical node sequence labeled "Happy Path" and "Exception Path" |
| Topic graph completeness | Every topic node inventoried, each labeled traced or untraced | "The agent addresses the main user scenarios comprehensively" -- no per-node inventory |
| Copilot Studio vocabulary | Topics, trigger phrases, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation), condition branches, redirect nodes used correctly | "Intents", "slots", "utterances" as primary labels without CS-specific equivalents |
| Actionable remediation | Topic node named and exact Copilot Studio object to change named | "Add better error handling to the affected topics" -- zero points |
| Pre-trace hypothesis | Hypothesis table for all four defect types with predicted candidate locations before any trace phase; verdict section reconciles each prediction against findings | "Collisions might occur if topics have similar phrasing" as hypothesis row -- no predicted node named, zero points |
| Coverage metrics | topic_coverage_ratio as N_traced/N_total decimal; fallback_coverage_ratio as N_fallback_traced/N_fallback_defined decimal; COVERAGE_GATE: CLEAN or DEGRADED with threshold comparison | "7 of 10 nodes were traced. Coverage is adequate for the primary scenarios." -- no ratios, no gate verdict |

**Do not begin generating output until you have read every row above.**

---

You are a **Copilot Studio domain expert**. You build and debug production agents on Copilot Studio. You know the platform object model: topics, trigger phrases, entities (closed list, regex, system), condition branches, redirect nodes, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation, Error), and session variables (context variables, slot filling, Boolean gates).

Read the input signals. Work defect-first: predict which nodes are most likely to fail before tracing what succeeds. Execute all phases in order.

---

**PHASE 1 -- DEFECT HYPOTHESIS**

A first-pass defect hypothesis would say: "The flow may have issues with fallback coverage and intent conflicts in areas where multiple topics handle similar phrasing." That prediction names no specific topic nodes, states no failure conditions, and cannot be confirmed or refuted -- it is a paraphrase of a hypothesis, not a hypothesis.

**Exit condition:** MAY NOT proceed with fewer than four rows, one per defect type. MAY NOT write "Possible issues may exist throughout" -- each row names a specific candidate topic node and a specific suspected condition, or writes "No candidate identified -- reason: [specific reason from the input signals]."

Before any trace phase begins, commit to predicted failure locations.

| Defect Type | Predicted Candidate Location (Topic Node) | Suspected Failure Condition | Confidence |
|-------------|------------------------------------------|-----------------------------|------------|
| Dead end | [specific topic node or "None suspected"] | [specific condition] | High / Low |
| Infinite loop | [specific topic node or redirect entry] | [specific redirect chain] | High / Low |
| Intent collision | [specific trigger phrase candidate] | [two candidate topic nodes] | High / Low |
| Missing fallback | [specific topic node] | [no no-match branch description] | High / Low |

Predictions will be confirmed, refuted, or declared inconclusive in Phase 5.

---

**PHASE 2 -- INVENTORY**

A first-pass inventory would say: "The agent includes nodes for handling common order, account, and support scenarios with standard Copilot Studio system topic integrations." That output names no individual topic nodes, lists no trigger phrases, and hides whether any node lacks a no-match branch.

**Exit condition:** MAY NOT proceed if any table row has an empty cell. MAY NOT replace the table with a summary statement -- every topic node must appear as a named row.

| Topic Node (Copilot Studio) | Trigger Phrases | No-Match Branch Defined | Reachable from Entry? |
|-----------------------------|----------------|------------------------|----------------------|

After the table: name the entry topic and all reachable terminal states.

---

**PHASE 3 -- HAPPY PATH TRACE**

A first-pass happy path trace would say: "User greets the agent. Agent identifies the intent and fulfills the request. Conversation ends normally with session state properly maintained." That output names no topic nodes, shows no utterances, writes no agent response text, and tracks no session variables -- a description of a trace, not a trace.

**Exit condition:** MAY NOT end on an active topic node -- final row must name a terminal state. MAY NOT write "Agent responds appropriately" or leave Agent Response blank; actual message text required in every row.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1    | (entry topic)               | "..."                          | "..."                                | ...                           | var = value            |

---

**PHASE 4 -- EXCEPTION PATH TRACE**

A first-pass exception trace would say: "When unrecognized input is received, the agent re-prompts. If retries fail, the session escalates to a human agent." That output names no divergence node, states no triggering condition, and likely reaches the same terminal as the happy path -- it is a paraphrase, not an exception trace.

**Exit condition:** MAY NOT trace the same node sequence as Phase 3 with a different utterance -- path non-uniqueness is a structural failure. Must branch at a named topic node under a different condition and reach a different terminal OR traverse a different node set. Where possible, route through the Phase 1 candidate defect node.

Label above: "Diverges from happy path at [node]: condition -- [what triggers the branch]." Same table format as Phase 3.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|

---

**PHASE 5 -- DEFECT SCAN + HYPOTHESIS VERDICT + REMEDIATION + COVERAGE + COVERAGE METRICS**

A first-pass defect scan would say: "No significant issues found. Consider reviewing fallback configuration and adding error handling throughout." A first-pass coverage section would say: "7 of 10 nodes were traced. Coverage is adequate for the primary user scenarios." Neither output can be acted on by an engineer implementing changes in Copilot Studio -- the first names no nodes, the second provides no ratios and no COVERAGE_GATE verdict.

**Exit condition:** MAY NOT produce fewer than four defect verdict rows. MAY NOT write a combined "no issues found" -- four individual verdicts required. MAY NOT use "possible" or "unclear" as verdicts. MAY NOT write "Add better error handling" -- name the Copilot Studio object to change. MAY NOT omit a Phase 2 node from the coverage table. MAY NOT write "Coverage is adequate" as a substitute for the three numeric ratios. MAY NOT report COVERAGE_GATE: CLEAN without computing topic_coverage_ratio and fallback_coverage_ratio.

**Defect scan:**

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | name or N/A | describe or "Checked N nodes -- none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect entry or N/A | describe or "Checked all chains -- none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | trigger phrase or N/A | name both topic nodes or "No overlapping phrases found" | Yes / No / N/A |
| Missing fallback | Found / Not found | name or N/A | name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |

**Hypothesis verdict:** Reconcile each Phase 1 prediction against findings from Phases 3-4.

| Defect Type | Phase 1 Prediction | Outcome | Evidence from Traces |
|-------------|-------------------|---------|--------------------|
| Dead end | (from Phase 1) | Confirmed / Refuted / Inconclusive | (cite node or turn) |
| Infinite loop | (from Phase 1) | Confirmed / Refuted / Inconclusive | (cite node or turn) |
| Intent collision | (from Phase 1) | Confirmed / Refuted / Inconclusive | (cite phrase or node) |
| Missing fallback | (from Phase 1) | Confirmed / Refuted / Inconclusive | (cite node or turn) |

**Remediation** (one row per Found defect -- name node and exact Copilot Studio object):

| Defect | Topic Node (Copilot Studio) | Exact Change Required | Copilot Studio Object to Edit |
|--------|------------------------------|----------------------|-------------------------------|

If no defects found: "No defects found -- no remediations required."

**Coverage** (every Phase 2 node gets a row):

| Topic Node (Copilot Studio) | Traced (Happy) | Traced (Exception) | Untraced | Unreachable |
|-----------------------------|---------------|-------------------|----------|-------------|

**Coverage Metrics:**

Compute from the coverage table above. Do not estimate -- count rows in each column.

| Metric | Formula | Value |
|--------|---------|-------|
| topic_coverage_ratio | N_traced (Happy OR Exception) / N_total | N/N |
| fallback_coverage_ratio | N_nodes_with_fallback_traced / N_nodes_with_no-match_branch_defined | N/N |
| intent_collision_density | N_trigger_phrase_overlaps_found / N_total_trigger_phrases | N/N |

COVERAGE_GATE: CLEAN if topic_coverage_ratio >= 0.70 AND fallback_coverage_ratio >= 0.50. Otherwise: DEGRADED.

If DEGRADED: list the specific topic nodes that must be traced to bring topic_coverage_ratio to >= 0.70.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All five phases as labeled sections. Do not combine phases. Do not omit any table.

---

## V-03 -- Status Quo Simulation (Inertia Framing)

**Axis:** Inertia framing -- adds Phase 0 STATUS_QUO_TRACE (3-turn keyword-match-only simulation) before Phase 1, and a STATUS_QUO_COMPARISON block inside Phase 5. All R6 mechanisms retained; single role.
**Hypothesis:** All R6 mechanisms retained → C-01 through C-16 all PASS → 135/135 on v6. Phase 0 runs a deliberately limited simulation (keyword matching only, no condition branches, no redirect following, no session variable tracking) before the full trace runs. Phase 5 shows which Found defects the status quo method would have missed (STATUS_QUO_BLIND_SPOT: YES/NO per defect). This is structurally distinct from per-section foils (C-14): foils show a bad static example; Phase 0 produces an actual live trace of inferior quality, and Phase 5 computes the detection gap between methods. C-19 candidate evidence expected in STATUS_QUO_COMPARISON. Expected: 135/135 (v6 ceiling confirmed) + C-19 candidate.

---

**Read your scoring criteria before generating any output.**

The following table defines what earns full credit and what earns zero. Zero-point examples are specific outputs this simulation replaces -- recognize and avoid them in every phase.

| Criterion | Full credit | Zero points |
|-----------|------------|-------------|
| Dialog path traced | Complete turn-by-turn trace from entry topic to named terminal state; user intent AND agent response text in every turn | "Order Status, Account Management, and Escalation topics are covered" -- topic list with no per-turn trace |
| Defect report | All four types (dead end, infinite loop, intent collision, missing fallback) each with Found/Not found verdict and specific location | "No significant issues found. Consider adding error handling." -- zero points for every defect type |
| Intent-response pairing | Both user utterance and agent response text in every traced turn | Turn row showing "User asks about their order" with Agent Response blank or "Agent responds appropriately" |
| Fallback handling | At least one no-match branch traced or one missing-fallback defect explicitly flagged | Happy-path trace with no fallback path and no missing-fallback entry in the defect scan |
| Session state | Two or more named session variables with specific names and values at each turn where they change | "Session context is maintained appropriately throughout the conversation" -- no variable names or values |
| Multi-path coverage | Happy path AND exception path diverging at a named node under a distinct condition, reaching different terminal or traversing different nodes | Two traces ending at End of Conversation via identical node sequence labeled "Happy Path" and "Exception Path" |
| Topic graph completeness | Every topic node inventoried, each labeled traced or untraced | "The agent addresses the main user scenarios comprehensively" -- no per-node inventory |
| Copilot Studio vocabulary | Topics, trigger phrases, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation), condition branches, redirect nodes used correctly | "Intents", "slots", "utterances" as primary labels without CS-specific equivalents |
| Actionable remediation | Topic node named and exact Copilot Studio object to change named | "Add better error handling to the affected topics" -- zero points |
| Pre-trace hypothesis | Hypothesis table for all four defect types with predicted candidate locations before any trace phase; verdict section reconciles each prediction against findings | "Collisions might occur if topics have similar phrasing" as hypothesis row -- no predicted node named, zero points |
| Status quo comparison | Phase 0 STATUS_QUO_TRACE uses keyword matching only (no condition branches, no redirect following, no session variables); Phase 5 STATUS_QUO_COMPARISON labels each Found defect YES/NO for STATUS_QUO_BLIND_SPOT | "Status quo behavior is similar to full simulation -- no significant gaps detected" -- no per-defect detection gap analysis |

**Do not begin generating any output until you have read every row above.**

---

You are a **Copilot Studio domain expert**. You build and debug production agents on Copilot Studio. You know the platform object model: topics, trigger phrases, entities (closed list, regex, system), condition branches, redirect nodes, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation, Error), and session variables (context variables, slot filling, Boolean gates).

Read the input signals. Execute all phases in order. Phase 0 runs before the hypothesis phase -- it establishes the status quo baseline first.

---

**PHASE 0 -- STATUS_QUO_TRACE**

A status quo trace would say: "The agent processes user input using keyword matching and returns predefined responses. The behavior is broadly similar to the full simulation, covering the same topics at a lower fidelity." That output names no specific keyword matches, identifies no gaps, and cannot show which defects a keyword-only implementation would miss.

**Exit condition:** MAY NOT skip Phase 0. MAY NOT use condition branches, redirect nodes, or session variable logic in this phase -- keyword matching only. MAY NOT produce a STATUS_QUO_TRACE identical in column depth to Phase 3 -- the status quo method has no Redirect Target column and no Session Variable Delta column. MAY NOT write "Status quo behavior is similar to full simulation" without naming specific turns where keyword matching fails or returns the wrong response.

Run a 3-turn abbreviated trace using keyword matching only. For each turn: which keyword in the user utterance triggers which response, and whether that match is correct, ambiguous, or missing.

| Turn | User Utterance | Keyword(s) Matched | Agent Response (keyword match output) | SQ_MATCH_QUALITY |
|------|--------------|-------------------|---------------------------------------|-----------------|
| 1    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |
| 2    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |
| 3    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |

SQ_MATCH_QUALITY legend: Correct = keyword uniquely identifies the right topic; Ambiguous = keyword matches multiple topics (intent collision candidate); No_match = no keyword match found (missing fallback candidate).

---

**PHASE 1 -- DEFECT HYPOTHESIS**

A first-pass defect hypothesis would say: "The flow may have issues with fallback coverage and intent conflicts in areas where multiple topics handle similar phrasing." That prediction names no specific topic nodes, states no failure conditions, and cannot be confirmed or refuted -- it is a paraphrase of a hypothesis, not a hypothesis.

**Exit condition:** MAY NOT proceed with fewer than four rows, one per defect type. MAY NOT write "Possible issues may exist throughout" -- each row names a specific candidate topic node and a specific suspected condition, or writes "No candidate identified -- reason: [specific reason from the input signals]." Note any Phase 0 Ambiguous or No_match rows that update a hypothesis prediction.

| Defect Type | Predicted Candidate Location (Topic Node) | Suspected Failure Condition | Confidence | Phase 0 Signal |
|-------------|------------------------------------------|-----------------------------|------------|----------------|
| Dead end | [specific topic node or "None suspected"] | [specific condition] | High / Low | [Turn N Ambiguous/No_match or "None"] |
| Infinite loop | [specific topic node or redirect entry] | [specific redirect chain] | High / Low | [Turn N or "None"] |
| Intent collision | [specific trigger phrase candidate] | [two candidate topic nodes] | High / Low | [Turn N Ambiguous or "None"] |
| Missing fallback | [specific topic node] | [no no-match branch description] | High / Low | [Turn N No_match or "None"] |

Predictions will be confirmed, refuted, or declared inconclusive in Phase 5.

---

**PHASE 2 -- INVENTORY**

A first-pass inventory would say: "The agent includes nodes for handling common order, account, and support scenarios with standard Copilot Studio system topic integrations." That output names no individual topic nodes, lists no trigger phrases, and hides whether any node lacks a no-match branch.

**Exit condition:** MAY NOT proceed if any table row has an empty cell. MAY NOT replace the table with a summary statement -- every topic node must appear as a named row.

| Topic Node (Copilot Studio) | Trigger Phrases | No-Match Branch Defined | Reachable from Entry? |
|-----------------------------|----------------|------------------------|----------------------|

After the table: name the entry topic and all reachable terminal states.

---

**PHASE 3 -- HAPPY PATH TRACE**

A first-pass happy path trace would say: "User greets the agent. Agent identifies the intent and fulfills the request. Conversation ends normally with session state properly maintained." That output names no topic nodes, shows no utterances, writes no agent response text, and tracks no session variables -- a description of a trace, not a trace.

**Exit condition:** MAY NOT end on an active topic node -- final row must name a terminal state. MAY NOT write "Agent responds appropriately" or leave Agent Response blank; actual message text required in every row.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1    | (entry topic)               | "..."                          | "..."                                | ...                           | var = value            |

---

**PHASE 4 -- EXCEPTION PATH TRACE**

A first-pass exception trace would say: "When unrecognized input is received, the agent re-prompts. If retries fail, the session escalates to a human agent." That output names no divergence node, states no triggering condition, and likely reaches the same terminal as the happy path -- it is a paraphrase, not an exception trace.

**Exit condition:** MAY NOT trace the same node sequence as Phase 3 with a different utterance -- path non-uniqueness is a structural failure. Must branch at a named topic node under a different condition and reach a different terminal OR traverse a different node set. Where possible, route through the Phase 1 candidate defect node.

Label above: "Diverges from happy path at [node]: condition -- [what triggers the branch]." Same table format as Phase 3.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|

---

**PHASE 5 -- DEFECT SCAN + HYPOTHESIS VERDICT + REMEDIATION + COVERAGE + STATUS_QUO_COMPARISON**

A first-pass defect scan would say: "No significant issues found. Consider reviewing fallback configuration and adding error handling throughout." A first-pass status quo comparison would say: "Status quo behavior is broadly similar to the full simulation -- no significant detection gaps." Neither output can be acted on by an engineer implementing changes in Copilot Studio.

**Exit condition:** MAY NOT produce fewer than four defect verdict rows. MAY NOT write a combined "no issues found" -- four individual verdicts required. MAY NOT use "possible" or "unclear" as verdicts. MAY NOT write "Add better error handling" -- name the Copilot Studio object to change. MAY NOT omit a Phase 2 node from coverage. MAY NOT write "No significant gaps" as STATUS_QUO_COMPARISON -- emit one row per Found defect with an explicit YES/NO for STATUS_QUO_BLIND_SPOT.

**Defect scan:**

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | name or N/A | describe or "Checked N nodes -- none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect entry or N/A | describe or "Checked all chains -- none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | trigger phrase or N/A | name both topic nodes or "No overlapping phrases found" | Yes / No / N/A |
| Missing fallback | Found / Not found | name or N/A | name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |

**Hypothesis verdict:** Reconcile each Phase 1 prediction against findings from Phases 3-4.

| Defect Type | Phase 1 Prediction | Outcome | Evidence from Traces |
|-------------|-------------------|---------|--------------------|
| Dead end | (from Phase 1) | Confirmed / Refuted / Inconclusive | (cite node or turn) |
| Infinite loop | (from Phase 1) | Confirmed / Refuted / Inconclusive | (cite node or turn) |
| Intent collision | (from Phase 1) | Confirmed / Refuted / Inconclusive | (cite phrase or node) |
| Missing fallback | (from Phase 1) | Confirmed / Refuted / Inconclusive | (cite node or turn) |

**Remediation** (one row per Found defect -- name node and exact Copilot Studio object):

| Defect | Topic Node (Copilot Studio) | Exact Change Required | Copilot Studio Object to Edit |
|--------|------------------------------|----------------------|-------------------------------|

If no defects found: "No defects found -- no remediations required."

**Coverage** (every Phase 2 node gets a row):

| Topic Node (Copilot Studio) | Traced (Happy) | Traced (Exception) | Untraced | Unreachable |
|-----------------------------|---------------|-------------------|----------|-------------|

State total nodes traced vs inventoried. Flag any unreachable node as a graph connectivity defect.

**STATUS_QUO_COMPARISON** (one row per Found defect only; omit Not-found rows):

| Defect Type | Defect Location | FOUND_BY_FULL_TRACE | FOUND_BY_STATUS_QUO | STATUS_QUO_BLIND_SPOT | Detection Gap Explanation |
|-------------|----------------|--------------------|--------------------|----------------------|--------------------------|
| (each Found defect from scan above) | (node name) | YES | YES / NO | YES / NO | (if YES: what about keyword matching prevents detection -- e.g., no condition branch to expose the dead end, or ambiguous keyword masks the collision) |

STATUS_QUO_BLIND_SPOT: YES if the Phase 0 STATUS_QUO_TRACE method (keyword matching only, no redirect following, no session tracking) would not have detected this defect. NO if keyword matching alone would surface it.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All phases as labeled sections including Phase 0. Do not combine phases. Do not omit any table.

---

## V-04 -- Role Separation + Status Quo Simulation (Two New Mechanisms)

**Axis:** Role sequence + Inertia framing -- combines V-01's two-role split (ANALYST + AUDITOR) with V-03's Phase 0 STATUS_QUO_TRACE. Tests whether role_independent_verification and detection_gap_audit are additive mechanisms or one subsumes the other.
**Hypothesis:** All R6 mechanisms retained → C-01 through C-16 all PASS → 135/135 on v6. V-01's role split is preserved: ANALYST runs Phases 1-4; AUDITOR independently runs Phase 5. V-03's Phase 0 STATUS_QUO_TRACE is preserved: keyword-matching simulation before the hypothesis phase. AUDITOR Phase 5 now includes both VERIFICATION_VERDICT column and STATUS_QUO_COMPARISON table. If both mechanisms are independently detectable (one does not subsume the other), evidence for both C-17 (role independence) and C-19 (detection gap) is present in the same artifact. Expected: 135/135 (v6 ceiling) + two C-17/C-19 candidate signals.

---

**Read your scoring criteria before generating any output.**

The following table defines what earns full credit and what earns zero. Zero-point examples are specific outputs this simulation replaces -- recognize and avoid them in every phase.

| Criterion | Full credit | Zero points |
|-----------|------------|-------------|
| Dialog path traced | Complete turn-by-turn trace from entry topic to named terminal state; user intent AND agent response text in every turn | "Order Status, Account Management, and Escalation topics are covered" -- topic list with no per-turn trace |
| Defect report | All four types (dead end, infinite loop, intent collision, missing fallback) each with Found/Not found verdict and specific location | "No significant issues found. Consider adding error handling." -- zero points for every defect type |
| Intent-response pairing | Both user utterance and agent response text in every traced turn | Turn row showing "User asks about their order" with Agent Response blank or "Agent responds appropriately" |
| Fallback handling | At least one no-match branch traced or one missing-fallback defect explicitly flagged | Happy-path trace with no fallback path and no missing-fallback entry in the defect scan |
| Session state | Two or more named session variables with specific names and values at each turn where they change | "Session context is maintained appropriately throughout the conversation" -- no variable names or values |
| Multi-path coverage | Happy path AND exception path diverging at a named node under a distinct condition, reaching different terminal or traversing different nodes | Two traces ending at End of Conversation via identical node sequence labeled "Happy Path" and "Exception Path" |
| Topic graph completeness | Every topic node inventoried, each labeled traced or untraced | "The agent addresses the main user scenarios comprehensively" -- no per-node inventory |
| Copilot Studio vocabulary | Topics, trigger phrases, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation), condition branches, redirect nodes used correctly | "Intents", "slots", "utterances" as primary labels without CS-specific equivalents |
| Actionable remediation | Topic node named and exact Copilot Studio object to change named | "Add better error handling to the affected topics" -- zero points |
| Pre-trace hypothesis | Hypothesis table for all four defect types with predicted candidate locations before any trace phase; verdict section reconciles each prediction against findings | "Collisions might occur if topics have similar phrasing" as hypothesis row -- no predicted node named, zero points |
| Role independence | AUDITOR explicitly states it did not author Phases 1-4; each VERIFICATION_VERDICT cites trace evidence; AUDITOR may write CHALLENGED | "AUDITOR: All findings confirmed" without trace citations |
| Status quo comparison | Phase 0 keyword-match trace present; STATUS_QUO_COMPARISON labels STATUS_QUO_BLIND_SPOT per Found defect | "Status quo behavior is broadly similar" -- no per-defect gap analysis |

**Do not begin generating any output until you have read every row above.**

---

**Role: FLOW ANALYST**

You are a **Copilot Studio domain expert** acting as the FLOW ANALYST. You know the platform object model: topics, trigger phrases, entities (closed list, regex, system), condition branches, redirect nodes, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation, Error), and session variables (context variables, slot filling, Boolean gates).

Execute Phase 0 and Phases 1-4 in order. Then issue ANALYST_HANDOFF.

---

**PHASE 0 -- STATUS_QUO_TRACE**

A status quo trace would say: "Keyword matching covers most scenarios. Results are broadly similar to the full simulation." That output names no specific matches, identifies no gaps, and cannot show which defects a keyword-only method misses.

**Exit condition:** MAY NOT skip Phase 0. MAY NOT use condition branches, redirect nodes, or session variable logic. MAY NOT write "Status quo behavior is similar to full simulation" without naming specific turns where keyword matching fails or returns the wrong response.

| Turn | User Utterance | Keyword(s) Matched | Agent Response (keyword match output) | SQ_MATCH_QUALITY |
|------|--------------|-------------------|---------------------------------------|-----------------|
| 1    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |
| 2    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |
| 3    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |

---

**PHASE 1 -- DEFECT HYPOTHESIS**

A first-pass defect hypothesis would say: "The flow may have issues with fallback coverage and intent conflicts in areas where multiple topics handle similar phrasing." That prediction names no specific topic nodes and cannot be confirmed or refuted.

**Exit condition:** MAY NOT proceed with fewer than four rows. Each row names a specific candidate topic node and suspected condition, or writes "No candidate identified -- reason: [specific reason]." Note Phase 0 Ambiguous/No_match signals.

| Defect Type | Predicted Candidate Location (Topic Node) | Suspected Failure Condition | Confidence | Phase 0 Signal |
|-------------|------------------------------------------|-----------------------------|------------|----------------|
| Dead end | [specific topic node or "None suspected"] | [specific condition] | High / Low | [Turn N or "None"] |
| Infinite loop | [specific topic node or redirect entry] | [specific redirect chain] | High / Low | [Turn N or "None"] |
| Intent collision | [specific trigger phrase candidate] | [two candidate topic nodes] | High / Low | [Turn N Ambiguous or "None"] |
| Missing fallback | [specific topic node] | [no no-match branch description] | High / Low | [Turn N No_match or "None"] |

---

**PHASE 2 -- INVENTORY**

A first-pass inventory would say: "The agent includes nodes for handling common order, account, and support scenarios with standard Copilot Studio system topic integrations." That output names no individual topic nodes and hides whether any node lacks a no-match branch.

**Exit condition:** MAY NOT proceed if any table row has an empty cell. MAY NOT replace the table with a summary statement.

| Topic Node (Copilot Studio) | Trigger Phrases | No-Match Branch Defined | Reachable from Entry? |
|-----------------------------|----------------|------------------------|----------------------|

After the table: name the entry topic and all reachable terminal states.

---

**PHASE 3 -- HAPPY PATH TRACE**

A first-pass happy path trace would say: "User greets the agent. Agent identifies intent and fulfills the request. Conversation ends normally." That output names no topic nodes and tracks no session variables -- a description of a trace, not a trace.

**Exit condition:** MAY NOT end on an active topic node. MAY NOT write "Agent responds appropriately" or leave Agent Response blank.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1    | (entry topic)               | "..."                          | "..."                                | ...                           | var = value            |

---

**PHASE 4 -- EXCEPTION PATH TRACE**

A first-pass exception trace would say: "When unrecognized input is received, the agent re-prompts. If retries fail, escalation occurs." That output names no divergence node and cannot be validated against the happy path.

**Exit condition:** MAY NOT trace the same node sequence as Phase 3. Must branch at a named topic node under a different condition. Where possible, route through the Phase 1 candidate defect node.

Label above: "Diverges from happy path at [node]: condition -- [trigger]."

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|

---

**ANALYST_HANDOFF: COMPLETE. HANDOFF_TO: FLOW AUDITOR.**

---

**Role: FLOW AUDITOR**

You are a **Copilot Studio domain expert** acting as the FLOW AUDITOR. You did not author Phases 0-4. Your verdicts are independent findings from Phase 2 inventory and Phases 3-4 trace tables. Derive defect verdicts from trace evidence before reading the ANALYST's Phase 1 predictions.

**Received ANALYST_HANDOFF: COMPLETE. Beginning independent audit.**

---

**PHASE 5 -- INDEPENDENT DEFECT SCAN + HYPOTHESIS VERIFICATION + REMEDIATION + COVERAGE + STATUS_QUO_COMPARISON**

A first-pass independent audit would say: "AUDITOR review complete. All ANALYST findings confirmed. No detection gaps between full simulation and status quo method." That output echoes ANALYST findings without independent verification and writes off the gap analysis without examining Phase 0 turn quality.

**Exit condition:** MAY NOT write "All ANALYST findings confirmed" without citing trace evidence per row. MAY NOT produce fewer than four defect verdicts. MAY NOT use "possible" or "unclear." MAY NOT write "Add better error handling." MAY NOT omit a Phase 2 node from coverage. MAY NOT write "No significant gaps" as STATUS_QUO_COMPARISON.

**Defect scan (AUDITOR independent):**

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | name or N/A | describe or "Checked N nodes -- none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect entry or N/A | describe or "Checked all chains -- none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | trigger phrase or N/A | name both topic nodes or "No overlapping phrases found" | Yes / No / N/A |
| Missing fallback | Found / Not found | name or N/A | name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |

**Hypothesis verification:**

| Defect Type | ANALYST Phase 1 Prediction | AUDITOR Trace Verdict | VERIFICATION_VERDICT | Discrepancy Note |
|-------------|---------------------------|----------------------|---------------------|-----------------|
| Dead end | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | (if CHALLENGED: cite turn and node) |
| Infinite loop | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Intent collision | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Missing fallback | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |

**Remediation** (one row per Found defect):

| Defect | Topic Node (Copilot Studio) | Exact Change Required | Copilot Studio Object to Edit |
|--------|------------------------------|----------------------|-------------------------------|

**Coverage:**

| Topic Node (Copilot Studio) | Traced (Happy) | Traced (Exception) | Untraced | Unreachable |
|-----------------------------|---------------|-------------------|----------|-------------|

**STATUS_QUO_COMPARISON** (Found defects only):

| Defect Type | Defect Location | FOUND_BY_FULL_TRACE | FOUND_BY_STATUS_QUO | STATUS_QUO_BLIND_SPOT | Detection Gap Explanation |
|-------------|----------------|--------------------|--------------------|----------------------|--------------------------|

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All phases as labeled sections. Do not combine phases. Do not omit any table.

---

## V-05 -- Full Extension Ceiling (All Three New Mechanisms + All R6 Mechanisms)

**Axis:** Full extension ceiling -- all three R7 new mechanisms (role separation + quantitative coverage metrics + status quo simulation) combined with all seven R6 mechanisms.
**Hypothesis:** All R6 mechanisms retained → C-01 through C-16 all PASS → 135/135 on v6. All three R7 new mechanisms present simultaneously: ANALYST/AUDITOR role split (C-17 candidate), Coverage Metrics block with COVERAGE_GATE (C-18 candidate), Phase 0 STATUS_QUO_TRACE + STATUS_QUO_COMPARISON (C-19 candidate). Each new mechanism contributes non-redundant evidence beyond the v6 ceiling. Expected: 135/135 confirmed + three C-17/C-18/C-19 candidate signals each present and independently attributable.

**C-16 prohibition distribution (verification for v6 compliance):**
- Register-unique: `"session context is maintained appropriately"` (no-variable-name omission pattern); `"Collisions might occur if topics have similar phrasing"` (no-predicted-node hypothesis pattern); `"The agent addresses the main scenarios comprehensively"` (no-per-node-inventory coverage pattern); `"All ANALYST findings confirmed"` (echo-without-evidence role-independence failure).
- Foil-unique: `"User greets the agent. Agent identifies intent and fulfills request. Conversation ends normally."` (prose-trace-instead-of-table pattern); `"When unrecognized input received, agent re-prompts; if retries fail, escalates."` (exception-path-as-summary pattern); `"Status quo behavior is broadly similar to full simulation -- no significant gaps detected."` (gap-analysis-dismissed-without-per-defect-examination pattern).
- Exit-unique: `"MAY NOT trace the same node sequence as Phase 3 with a different utterance"` (path non-uniqueness failure); `"MAY NOT use 'possible' or 'unclear' as verdicts"` (specific forbidden verdict words); `"MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio"` (ratio-absent gate assertion).

Three structures each contribute at least one prohibited output not present in either of the other two. C-16 PASS condition is met.

---

**Read your scoring criteria before generating any output.**

The following table defines what earns full credit and what earns zero. Zero-point examples are specific outputs this simulation replaces -- recognize and avoid them in every phase.

| Criterion | Full credit | Zero points |
|-----------|------------|-------------|
| Dialog path traced | Complete turn-by-turn trace from entry topic to named terminal state; user intent AND agent response text in every turn | "Order Status, Account Management, and Escalation topics are covered" -- topic list with no per-turn trace |
| Defect report | All four types (dead end, infinite loop, intent collision, missing fallback) each with Found/Not found verdict and specific location | "No significant issues found. Consider adding error handling." -- zero points for every defect type |
| Intent-response pairing | Both user utterance and agent response text in every traced turn | Turn row showing "User asks about their order" with Agent Response blank or "Agent responds appropriately" |
| Fallback handling | At least one no-match branch traced or one missing-fallback defect explicitly flagged | Happy-path trace with no fallback path and no missing-fallback entry in the defect scan |
| Session state | Two or more named session variables with specific names and values at each turn where they change | "Session context is maintained appropriately throughout the conversation" -- no variable names or values |
| Multi-path coverage | Happy path AND exception path diverging at a named node under a distinct condition, reaching different terminal or traversing different nodes | Two traces ending at End of Conversation via identical node sequence labeled "Happy Path" and "Exception Path" |
| Topic graph completeness | Every topic node inventoried, each labeled traced or untraced | "The agent addresses the main user scenarios comprehensively" -- no per-node inventory |
| Copilot Studio vocabulary | Topics, trigger phrases, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation), condition branches, redirect nodes used correctly | "Intents", "slots", "utterances" as primary labels without CS-specific equivalents |
| Actionable remediation | Topic node named and exact Copilot Studio object to change named | "Add better error handling to the affected topics" -- zero points |
| Pre-trace hypothesis | Hypothesis table for all four defect types with predicted candidate locations before any trace phase; verdict section reconciles each prediction against findings | "Collisions might occur if topics have similar phrasing" as hypothesis row -- no predicted node named, zero points |
| Role independence | AUDITOR states it did not author Phases 0-4; each VERIFICATION_VERDICT cites trace evidence; AUDITOR may write CHALLENGED | "All ANALYST findings confirmed" without trace citations -- echo with no independent verification |
| Coverage metrics | topic_coverage_ratio and fallback_coverage_ratio as N/N decimals; COVERAGE_GATE: CLEAN or DEGRADED with threshold comparison | "Coverage is adequate for primary scenarios" -- no ratios, no gate verdict |
| Status quo comparison | Phase 0 keyword-match trace present (no condition branches, no redirects, no session tracking); STATUS_QUO_COMPARISON labels STATUS_QUO_BLIND_SPOT YES/NO per Found defect | "Status quo behavior is broadly similar -- no significant detection gaps" -- dismissed without per-defect analysis |

**Do not begin generating any output until you have read every row above.**

---

**Role: FLOW ANALYST**

You are a **Copilot Studio domain expert** acting as the FLOW ANALYST. You know the platform object model: topics, trigger phrases, entities (closed list, regex, system), condition branches, redirect nodes, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation, Error), and session variables (context variables, slot filling, Boolean gates).

Execute Phase 0 and Phases 1-4 in order. Then issue ANALYST_HANDOFF.

---

**PHASE 0 -- STATUS_QUO_TRACE**

A status quo trace would say: "Status quo behavior is broadly similar to full simulation -- no significant gaps detected." That output dismisses the comparison without examining any specific turn, names no keyword matches, and cannot show which defects a keyword-only method misses.

**Exit condition:** MAY NOT skip Phase 0. MAY NOT use condition branches, redirect nodes, or session variable logic. MAY NOT write "Status quo behavior is broadly similar" without naming specific turns where keyword matching produces Ambiguous or No_match quality.

| Turn | User Utterance | Keyword(s) Matched | Agent Response (keyword match output) | SQ_MATCH_QUALITY |
|------|--------------|-------------------|---------------------------------------|-----------------|
| 1    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |
| 2    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |
| 3    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |

---

**PHASE 1 -- DEFECT HYPOTHESIS**

A first-pass defect hypothesis would say: "The flow may have issues with fallback coverage and intent conflicts in areas where multiple topics handle similar phrasing." That prediction names no specific topic nodes, states no failure conditions, and cannot be confirmed or refuted -- it is a paraphrase of a hypothesis, not a hypothesis.

**Exit condition:** MAY NOT proceed with fewer than four rows, one per defect type. MAY NOT write "Possible issues may exist throughout" -- each row names a specific candidate topic node and a specific suspected condition, or writes "No candidate identified -- reason: [specific reason from the input signals]."

Before any trace phase begins, commit to predicted failure locations. Note any Phase 0 Ambiguous/No_match rows that update a hypothesis.

| Defect Type | Predicted Candidate Location (Topic Node) | Suspected Failure Condition | Confidence | Phase 0 Signal |
|-------------|------------------------------------------|-----------------------------|------------|----------------|
| Dead end | [specific topic node or "None suspected"] | [specific condition] | High / Low | [Turn N or "None"] |
| Infinite loop | [specific topic node or redirect entry] | [specific redirect chain] | High / Low | [Turn N or "None"] |
| Intent collision | [specific trigger phrase candidate] | [two candidate topic nodes] | High / Low | [Turn N Ambiguous or "None"] |
| Missing fallback | [specific topic node] | [no no-match branch description] | High / Low | [Turn N No_match or "None"] |

Predictions will be reconciled by the FLOW AUDITOR in Phase 5.

---

**PHASE 2 -- INVENTORY**

A first-pass inventory would say: "The agent includes nodes for handling common order, account, and support scenarios with standard Copilot Studio system topic integrations." That output names no individual topic nodes, lists no trigger phrases, and hides whether any node lacks a no-match branch.

**Exit condition:** MAY NOT proceed if any table row has an empty cell. MAY NOT replace the table with a summary statement -- every topic node must appear as a named row.

| Topic Node (Copilot Studio) | Trigger Phrases | No-Match Branch Defined | Reachable from Entry? |
|-----------------------------|----------------|------------------------|----------------------|

After the table: name the entry topic and all reachable terminal states.

---

**PHASE 3 -- HAPPY PATH TRACE**

A first-pass happy path trace would say: "User greets the agent. Agent identifies the intent and fulfills the request. Conversation ends normally with session state properly maintained." That output names no topic nodes, shows no utterances, writes no agent response text, and tracks no session variables -- a description of a trace, not a trace.

**Exit condition:** MAY NOT end on an active topic node -- final row must name a terminal state. MAY NOT write "Agent responds appropriately" or leave Agent Response blank; actual message text required in every row.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1    | (entry topic)               | "..."                          | "..."                                | ...                           | var = value            |

---

**PHASE 4 -- EXCEPTION PATH TRACE**

A first-pass exception trace would say: "When unrecognized input is received, the agent re-prompts. If retries fail, the session escalates to a human agent." That output names no divergence node, states no triggering condition, and likely reaches the same terminal as the happy path -- it is a paraphrase, not an exception trace.

**Exit condition:** MAY NOT trace the same node sequence as Phase 3 with a different utterance -- path non-uniqueness is a structural failure. Must branch at a named topic node under a different condition and reach a different terminal OR traverse a different node set. Where possible, route through the Phase 1 candidate defect node.

Label above: "Diverges from happy path at [node]: condition -- [what triggers the branch]." Same table format as Phase 3.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|

---

**ANALYST_HANDOFF: COMPLETE. HANDOFF_TO: FLOW AUDITOR.**

---

**Role: FLOW AUDITOR**

You are a **Copilot Studio domain expert** acting as the FLOW AUDITOR. You did not author Phases 0-4. Your defect scan, hypothesis verification, coverage metrics, and status quo comparison below are independent findings derived from the Phase 2 inventory and Phases 3-4 trace tables. Derive defect verdicts from trace evidence before reading the ANALYST's Phase 1 predictions.

**Received ANALYST_HANDOFF: COMPLETE. Beginning independent audit.**

---

**PHASE 5 -- INDEPENDENT DEFECT SCAN + HYPOTHESIS VERIFICATION + REMEDIATION + COVERAGE + COVERAGE METRICS + STATUS_QUO_COMPARISON**

A first-pass independent audit would say: "All ANALYST findings confirmed. Coverage is adequate for primary scenarios. Status quo behavior is broadly similar -- no significant detection gaps." That output echoes without verifying, provides no ratios, and dismisses the gap analysis without examining Phase 0 turn quality.

**Exit condition:** MAY NOT write "All ANALYST findings confirmed" without citing trace evidence per row. MAY NOT produce fewer than four defect verdicts. MAY NOT use "possible" or "unclear." MAY NOT write "Add better error handling." MAY NOT omit a Phase 2 node from coverage. MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio. MAY NOT write "No significant gaps" as STATUS_QUO_COMPARISON.

**Defect scan (AUDITOR independent):**

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | name or N/A | describe or "Checked N nodes -- none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect entry or N/A | describe or "Checked all chains -- none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | trigger phrase or N/A | name both topic nodes or "No overlapping phrases found" | Yes / No / N/A |
| Missing fallback | Found / Not found | name or N/A | name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |

**Hypothesis verification:**

| Defect Type | ANALYST Phase 1 Prediction | AUDITOR Trace Verdict | VERIFICATION_VERDICT | Discrepancy Note |
|-------------|---------------------------|----------------------|---------------------|-----------------|
| Dead end | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | (if CHALLENGED: cite turn and node) |
| Infinite loop | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Intent collision | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Missing fallback | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |

**Remediation** (one row per Found defect):

| Defect | Topic Node (Copilot Studio) | Exact Change Required | Copilot Studio Object to Edit |
|--------|------------------------------|----------------------|-------------------------------|

If no defects found: "No defects found -- no remediations required."

**Coverage** (every Phase 2 node gets a row):

| Topic Node (Copilot Studio) | Traced (Happy) | Traced (Exception) | Untraced | Unreachable |
|-----------------------------|---------------|-------------------|----------|-------------|

**Coverage Metrics:**

| Metric | Formula | Value |
|--------|---------|-------|
| topic_coverage_ratio | N_traced (Happy OR Exception) / N_total | N/N |
| fallback_coverage_ratio | N_nodes_with_fallback_traced / N_nodes_with_no-match_branch_defined | N/N |
| intent_collision_density | N_trigger_phrase_overlaps_found / N_total_trigger_phrases | N/N |

COVERAGE_GATE: CLEAN if topic_coverage_ratio >= 0.70 AND fallback_coverage_ratio >= 0.50. Otherwise: DEGRADED.

If DEGRADED: list the specific topic nodes that must be traced to bring topic_coverage_ratio to >= 0.70.

**STATUS_QUO_COMPARISON** (Found defects only):

| Defect Type | Defect Location | FOUND_BY_FULL_TRACE | FOUND_BY_STATUS_QUO | STATUS_QUO_BLIND_SPOT | Detection Gap Explanation |
|-------------|----------------|--------------------|--------------------|----------------------|--------------------------|

STATUS_QUO_BLIND_SPOT: YES if Phase 0 keyword-matching-only method would not have detected this defect (no condition branch to expose the dead end, ambiguous keyword masks the collision, etc.). NO if keyword matching alone would surface it.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All phases as labeled sections including Phase 0. Do not combine phases. Do not omit any table.
