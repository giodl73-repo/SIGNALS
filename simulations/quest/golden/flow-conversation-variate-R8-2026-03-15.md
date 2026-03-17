# flow-conversation Variate -- Round 8
**Date:** 2026-03-15
**Rubric:** v7 (C-01 through C-19, max 150 pts)
**Target axes:** Three unexplored axes beyond the v7 ceiling -- iterative remediation verification, severity-tiered defect ranking, concurrent session interference
**Baseline:** R7 V-05 confirmed 150/150 on v7 rubric (all ten mechanisms: phases + CS headers + named prohibitions + pre-instruction register + per-section foils + pre-trace hypothesis + cross-mechanism prohibition convergence + role-independent verification + quantitative coverage threshold + detection gap audit). All R8 variations carry every R7 mechanism. The only variation is the new mechanism added. Each new mechanism probes whether a C-20+ candidate emerges.

---

## Round 8 Variation Map

| Variation | Axis | New Mechanism | All R7 Mechanisms? | Predicted (v7) | C-20+ Candidate | Hypothesis |
|-----------|------|---------------|-------------------|----------------|-----------------|------------|
| V-01 | Role sequence (post-audit) | Phase 6 REMEDIATION_VERIFICATION_CYCLE: AUDITOR re-traces BLOCKER defect path after applying Phase 5 remediation; named token REMEDIATION_CYCLE_COMPLETE: BLOCKER_RESOLVED / BLOCKER_PERSISTS | All PASS | 150/150 | remediation_verification_cycle | C-09 requires naming what to change but no re-trace after the change. C-17 requires role independence in defect scanning. Phase 6 adds verification-through-re-simulation: a structure that only exists when a BLOCKER defect triggers a second simulation pass. A prompt passing C-09 and C-17 can still terminate at "apply this fix" without ever re-tracing. |
| V-02 | Output format (defect scoring) | DEFECT_SEVERITY block in Phase 5: formula-based tier (CRITICAL/HIGH/LOW) per Found defect; SEVERITY_GATE: DEPLOYABLE/HOLD keyed on zero CRITICAL | All PASS | 150/150 | formula_based_defect_severity | C-18 measures graph traversal completeness (coverage ratio). C-02 classifies whether a defect was found. Neither requires a risk-impact formula. A prompt passing both can still write "This defect is high priority" without a tier token, formula, or gate. |
| V-03 | Role sequence (concurrent) | Phase 3.5 CONCURRENT_SESSION_TRACE: two simultaneous user sessions traced through shared topic nodes; SESSION_ISOLATION_VERDICT: CLEAN/COLLISION per shared node | All PASS | 150/150 | concurrent_session_interference | C-02 four-type taxonomy has no concurrency class. C-05 tracks one user's session variables. C-06 requires two structurally distinct paths but they are sequential, not concurrent. A prompt passing C-02, C-05, C-06 can still produce no concurrent session trace and no isolation verdict. |
| V-04 | Role sequence + Output format | Phase 6 remediation cycle (V-01) + DEFECT_SEVERITY block (V-02) | All PASS | 150/150 | remediation_cycle + severity_tiers | Tests additivity: a BLOCKER defect triggers both CRITICAL severity classification and remediation re-trace; Phase 6 confirms BLOCKER_RESOLVED after the CRITICAL-tier fix is applied. |
| V-05 | Full extension ceiling | All three new mechanisms: remediation cycle + severity tiers + concurrent session trace, on top of all R7 mechanisms | All PASS | 150/150 | all three active | Evidence pool for v8 rubric. C-20 (remediation_verification_cycle), C-21 (formula_based_defect_severity), C-22 (concurrent_session_interference) each present independently. |

---

## V-01 -- Iterative Remediation Cycle

**Axis:** Role sequence (post-audit) -- adds Phase 6 REMEDIATION_VERIFICATION_CYCLE conditionally triggered when Phase 5 finds a BLOCKER defect. All R7 mechanisms retained.
**Hypothesis:** All R7 mechanisms retained → C-01 through C-19 all PASS → 150/150 on v7. Phase 6 extends the AUDITOR role: apply the Phase 5 remediation mentally, re-trace the minimal path through the previously-BLOCKER node, verify the failure condition is absent. Named token REMEDIATION_CYCLE_COMPLETE: BLOCKER_RESOLVED / BLOCKER_PERSISTS. C-20 candidate: remediation_verification_cycle. Independent from C-09 (names the fix -- Phase 6 re-simulates after the fix, which C-09 does not require), C-17 (role independence of defect scanning -- Phase 6 is fix-then-re-trace, a different temporal structure), and C-15 (predict-then-verify for defect locations before tracing -- Phase 6 is verify-after-remediation, not predict-before-trace).

**C-16 prohibition distribution (verification):**
- Register-unique: `"session context is maintained appropriately"` (no-variable-name omission); `"Collisions might occur if topics have similar phrasing"` (no-predicted-node hypothesis); `"The agent addresses the main scenarios comprehensively"` (no-per-node-inventory); `"All ANALYST findings confirmed"` (echo-without-evidence); `"Phase 6 complete -- recommended fix should resolve the issue"` (remediation-claimed-without-re-trace).
- Foil-unique: `"User greets the agent. Agent identifies intent and fulfills request. Conversation ends normally."` (prose-trace); `"When unrecognized input received, agent re-prompts; if retries fail, escalates."` (exception-as-summary); `"Status quo behavior is broadly similar -- no significant gaps detected."` (gap-dismissed); `"The recommended fix addresses the root cause. After implementation, testing should confirm resolution."` (expectation-without-trace).
- Exit-unique: `"MAY NOT trace the same node sequence as Phase 3 with a different utterance"` (path non-uniqueness); `"MAY NOT use 'possible' or 'unclear' as verdicts"` (forbidden verdict words); `"MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio"` (ratio-absent gate); `"MAY NOT emit REMEDIATION_CYCLE_COMPLETE without a re-trace table for each BLOCKER defect"` (token-without-evidence).

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
| Status quo comparison | Phase 0 keyword-match trace present; STATUS_QUO_COMPARISON labels STATUS_QUO_BLIND_SPOT YES/NO per Found defect | "Status quo behavior is broadly similar -- no significant detection gaps" -- dismissed without per-defect analysis |
| Remediation cycle | Re-trace table shows BLOCKER node processed without failure condition after remediation applied; REMEDIATION_CYCLE_COMPLETE: BLOCKER_RESOLVED emitted | "Phase 6 complete -- recommended fix should resolve the issue" -- no re-trace, no before/after evidence, no token |

**Do not begin generating output until you have read every row above.**

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

**Exit condition:** MAY NOT proceed with fewer than four rows, one per defect type. MAY NOT write "Possible issues may exist throughout" -- each row names a specific candidate topic node and a specific suspected condition, or writes "No candidate identified -- reason: [specific reason from the input signals]." Note any Phase 0 Ambiguous/No_match rows that update a hypothesis.

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

Label above: "Diverges from happy path at [node]: condition -- [what triggers the branch]."

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|

---

**ANALYST_HANDOFF: COMPLETE. HANDOFF_TO: FLOW AUDITOR.**

---

**Role: FLOW AUDITOR**

You are a **Copilot Studio domain expert** acting as the FLOW AUDITOR. You did not author Phases 0-4. Your defect scan, hypothesis verification, coverage metrics, status quo comparison, and remediation verification below are independent findings derived from the Phase 2 inventory and Phases 3-4 trace tables. Derive defect verdicts from trace evidence before reading the ANALYST's Phase 1 predictions.

**Received ANALYST_HANDOFF: COMPLETE. Beginning independent audit.**

---

**PHASE 5 -- INDEPENDENT DEFECT SCAN + HYPOTHESIS VERIFICATION + REMEDIATION + COVERAGE + COVERAGE METRICS + STATUS_QUO_COMPARISON**

A first-pass independent audit would say: "All ANALYST findings confirmed. Coverage is adequate for primary scenarios. Status quo behavior is broadly similar -- no significant detection gaps." That output echoes without verifying, provides no ratios, and dismisses the gap analysis without examining Phase 0 turn quality.

**Exit condition:** MAY NOT write "All ANALYST findings confirmed" without citing trace evidence per row. MAY NOT produce fewer than four defect verdicts. MAY NOT use "possible" or "unclear." MAY NOT write "Add better error handling." MAY NOT omit a Phase 2 node from coverage. MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio. MAY NOT write "No significant gaps" as STATUS_QUO_COMPARISON. Flag each Found defect with BLOCKER: Yes or No -- Phase 6 triggers if any row has BLOCKER: Yes.

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

STATUS_QUO_BLIND_SPOT: YES if Phase 0 keyword-matching-only method would not have detected this defect. NO if keyword matching alone would surface it.

---

**PHASE 6 -- REMEDIATION VERIFICATION CYCLE (Conditional)**

Entry condition: Phase 5 defect scan contains at least one row with BLOCKER: Yes. If no BLOCKER defects found in Phase 5: write "Phase 6 skipped -- no BLOCKER defects identified. REMEDIATION_CYCLE_COMPLETE: N/A."

If entry condition met:

A first-pass remediation verification would say: "The recommended fix addresses the root cause. After implementation, testing should confirm resolution." That output describes an expected outcome without tracing it -- no re-trace table, no before/after evidence, no REMEDIATION_CYCLE_COMPLETE token with a specific verdict.

**Exit condition:** MAY NOT emit REMEDIATION_CYCLE_COMPLETE without a complete re-trace table for each BLOCKER defect showing the specific turns that previously exhibited the failure condition and now do not. MAY NOT write "Recommended fix should resolve the issue" -- show the re-traced turns. MAY NOT emit BLOCKER_RESOLVED without identifying the specific turn in the re-trace where the failure condition is absent.

For each BLOCKER defect from Phase 5:
1. State the remediation applied: "[exact change from Phase 5 Copilot Studio Object to Edit column]."
2. Re-trace the minimal path from the entry trigger to the previously-failing node and beyond, showing that after the remediation the node now processes without the failure condition.
3. Emit REMEDIATION_CYCLE_COMPLETE per defect.

| Turn | Topic Node (Copilot Studio) | User Utterance | Agent Response | Remediation Applied | FAILURE_CONDITION_PRESENT |
|------|-----------------------------|---------------|----------------|---------------------|--------------------------|
| 1    | (entry or redirect)         | "..."         | "..."          | [name of change]    | No -- condition absent / Yes -- persists |

REMEDIATION_CYCLE_COMPLETE: [defect_type] -- BLOCKER_RESOLVED (failure condition absent in re-trace) / BLOCKER_PERSISTS (failure condition still present -- remediation insufficient, escalate).

If BLOCKER_PERSISTS: name the specific turn in the re-trace where the failure condition persisted and state why the Phase 5 remediation was insufficient.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All phases as labeled sections including Phase 0 and Phase 6 (or Phase 6 skipped notice). Do not combine phases. Do not omit any table.

---

## V-02 -- Severity-Tiered Defect Ranking

**Axis:** Output format (defect scoring) -- adds a DEFECT_SEVERITY block inside Phase 5 with formula-based tier classification per Found defect and a SEVERITY_GATE completion token. All R7 mechanisms retained; single ANALYST/AUDITOR role split retained.
**Hypothesis:** All R7 mechanisms retained → C-01 through C-19 all PASS → 150/150 on v7. C-02 classifies defects as Found/Not found -- no severity formula. C-18 measures graph traversal completeness -- no defect impact formula. The DEFECT_SEVERITY block computes a tier (CRITICAL/HIGH/LOW) per Found defect using a named formula and gates deployment on zero CRITICAL defects. A prompt passing C-02 and C-18 can still say "This defect is high priority" without a tier token, formula, or SEVERITY_GATE. C-21 candidate evidence expected in DEFECT_SEVERITY block.

**C-16 prohibition distribution (verification):**
- Register-unique: `"session context is maintained appropriately"` (no-variable-name); `"Collisions might occur if topics have similar phrasing"` (no-node hypothesis); `"The agent addresses the main scenarios comprehensively"` (no-per-node inventory); `"All ANALYST findings confirmed"` (echo-without-evidence); `"This defect represents a significant risk"` (severity-claim-without-formula).
- Foil-unique: `"User greets the agent. Agent identifies intent and fulfills request."` (prose-trace); `"When unrecognized input received, agent re-prompts."` (exception-as-summary); `"Status quo behavior is broadly similar."` (gap-dismissed); `"This defect has a medium impact on user experience. Priority fix recommended."` (impact-claim-without-tier).
- Exit-unique: `"MAY NOT trace the same node sequence as Phase 3 with a different utterance"` (path non-uniqueness); `"MAY NOT use 'possible' or 'unclear' as verdicts"` (forbidden verdict words); `"MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio"` (ratio-absent gate); `"MAY NOT emit SEVERITY_GATE: DEPLOYABLE without computing DEFECT_SEVERITY for each Found defect row"` (gate-without-formula).

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
| Status quo comparison | Phase 0 keyword-match trace present; STATUS_QUO_COMPARISON labels STATUS_QUO_BLIND_SPOT YES/NO per Found defect | "Status quo behavior is broadly similar -- no significant detection gaps" -- dismissed without per-defect analysis |
| Defect severity | DEFECT_SEVERITY: CRITICAL/HIGH/LOW computed with named formula per Found defect; SEVERITY_GATE: DEPLOYABLE only if zero CRITICAL defects | "This defect represents a significant risk" -- no tier token, no formula applied, no gate |

**Do not begin generating output until you have read every row above.**

---

**Role: FLOW ANALYST**

You are a **Copilot Studio domain expert** acting as the FLOW ANALYST. You know the platform object model: topics, trigger phrases, entities (closed list, regex, system), condition branches, redirect nodes, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation, Error), and session variables (context variables, slot filling, Boolean gates).

Execute Phase 0 and Phases 1-4 in order. Then issue ANALYST_HANDOFF.

---

**PHASE 0 -- STATUS_QUO_TRACE**

A status quo trace would say: "Status quo behavior is broadly similar to full simulation -- no significant gaps detected." That output dismisses the comparison without examining any specific turn and cannot show which defects a keyword-only method misses.

**Exit condition:** MAY NOT skip Phase 0. MAY NOT use condition branches, redirect nodes, or session variable logic. MAY NOT write "Status quo behavior is broadly similar" without naming specific turns where keyword matching fails.

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

Predictions will be reconciled by the FLOW AUDITOR in Phase 5.

---

**PHASE 2 -- INVENTORY**

A first-pass inventory would say: "The agent includes nodes for handling common order, account, and support scenarios with standard Copilot Studio system topic integrations." That output names no individual topic nodes and hides whether any node lacks a no-match branch.

**Exit condition:** MAY NOT proceed if any table row has an empty cell. MAY NOT replace the table with a summary statement.

| Topic Node (Copilot Studio) | Trigger Phrases | No-Match Branch Defined | Reachable from Entry? |
|-----------------------------|----------------|------------------------|----------------------|

After the table: name the entry topic and all reachable terminal states.

---

**PHASE 3 -- HAPPY PATH TRACE**

A first-pass happy path trace would say: "User greets the agent. Agent identifies the intent and fulfills the request. Conversation ends normally with session state properly maintained." That output names no topic nodes, shows no utterances, writes no agent response text, and tracks no session variables -- a description of a trace, not a trace.

**Exit condition:** MAY NOT end on an active topic node. MAY NOT write "Agent responds appropriately" or leave Agent Response blank.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1    | (entry topic)               | "..."                          | "..."                                | ...                           | var = value            |

---

**PHASE 4 -- EXCEPTION PATH TRACE**

A first-pass exception trace would say: "When unrecognized input is received, the agent re-prompts. If retries fail, the session escalates to a human agent." That output names no divergence node and is a paraphrase, not a trace.

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

**PHASE 5 -- INDEPENDENT DEFECT SCAN + DEFECT SEVERITY + HYPOTHESIS VERIFICATION + REMEDIATION + COVERAGE + COVERAGE METRICS + STATUS_QUO_COMPARISON**

A first-pass independent audit would say: "All ANALYST findings confirmed. This defect has a medium impact on user experience. Coverage is adequate. Status quo behavior is broadly similar." That output echoes without verifying, applies no severity formula, provides no tier token, provides no ratios, and dismisses the gap analysis.

**Exit condition:** MAY NOT write "All ANALYST findings confirmed" without citing trace evidence per row. MAY NOT produce fewer than four defect verdicts. MAY NOT use "possible" or "unclear." MAY NOT write "Add better error handling." MAY NOT omit a Phase 2 node from coverage. MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio. MAY NOT write "No significant gaps" as STATUS_QUO_COMPARISON. MAY NOT emit SEVERITY_GATE: DEPLOYABLE without computing DEFECT_SEVERITY for each Found defect row.

**Defect scan (AUDITOR independent):**

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | name or N/A | describe or "Checked N nodes -- none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect entry or N/A | describe or "Checked all chains -- none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | trigger phrase or N/A | name both topic nodes or "No overlapping phrases found" | Yes / No / N/A |
| Missing fallback | Found / Not found | name or N/A | name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |

**Defect severity** (Found defects only -- apply formula before proceeding to remediation):

Formula:
- CRITICAL: defect_type is Dead_end AND the dead-end node is reachable from the entry topic via the Phase 3 happy path (affects primary flow); OR defect_type is Infinite_loop AND no condition branch or redirect in the loop provides an unconditional exit.
- HIGH: defect_type is Missing_fallback AND the topic node is reachable via more than one distinct path in Phase 2 inventory; OR defect_type is Intent_collision AND the colliding trigger phrase contains fewer than 3 unique keywords.
- LOW: all other Found defects.

| Defect Type | Defect Location | Severity Formula Applied | DEFECT_SEVERITY | SEVERITY_GATE Impact |
|-------------|----------------|--------------------------|----------------|----------------------|

SEVERITY_GATE: DEPLOYABLE if zero CRITICAL defects in the Found set. HOLD if any CRITICAL defect present.

**Hypothesis verification:**

| Defect Type | ANALYST Phase 1 Prediction | AUDITOR Trace Verdict | VERIFICATION_VERDICT | Discrepancy Note |
|-------------|---------------------------|----------------------|---------------------|-----------------|
| Dead end | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | (if CHALLENGED: cite turn and node) |
| Infinite loop | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Intent collision | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Missing fallback | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |

**Remediation** (one row per Found defect -- name node and exact Copilot Studio object; priority order: CRITICAL first):

| Defect | DEFECT_SEVERITY | Topic Node (Copilot Studio) | Exact Change Required | Copilot Studio Object to Edit |
|--------|----------------|------------------------------|----------------------|-------------------------------|

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

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All phases as labeled sections. Do not combine phases. Do not omit any table.

---

## V-03 -- Concurrent Session Interference

**Axis:** Role sequence (concurrent) -- adds Phase 3.5 CONCURRENT_SESSION_TRACE between Phase 3 and Phase 4. Two simultaneous user sessions traced through shared topic nodes to detect SESSION_VARIABLE_CONFLICT. All R7 mechanisms retained.
**Hypothesis:** All R7 mechanisms retained → C-01 through C-19 all PASS → 150/150 on v7. C-02's four defect types (dead end, infinite loop, intent collision, missing fallback) include no concurrency class. C-05 tracks session variables for one user path. C-06 requires two structurally distinct paths but they are sequential -- a prompt passing C-02, C-05, C-06 can still produce no concurrent session trace and no isolation verdict. C-22 candidate evidence expected in SESSION_ISOLATION_VERDICT.

**C-16 prohibition distribution (verification):**
- Register-unique: `"session context is maintained appropriately"` (no-variable-name); `"Collisions might occur if topics have similar phrasing"` (no-node hypothesis); `"The agent addresses the main scenarios comprehensively"` (no-per-node inventory); `"All ANALYST findings confirmed"` (echo-without-evidence); `"Multiple simultaneous sessions are generally supported by the platform"` (platform-guarantee-without-trace).
- Foil-unique: `"User greets the agent. Agent identifies intent and fulfills request."` (prose-trace); `"When unrecognized input received, agent re-prompts."` (exception-as-summary); `"Status quo behavior is broadly similar."` (gap-dismissed); `"The agent handles multiple sessions correctly due to platform-level isolation."` (delegation-to-platform-without-verification).
- Exit-unique: `"MAY NOT trace the same node sequence as Phase 3 with a different utterance"` (path non-uniqueness); `"MAY NOT use 'possible' or 'unclear' as verdicts"` (forbidden verdict words); `"MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio"` (ratio-absent gate); `"MAY NOT write SESSION_ISOLATION_VERDICT: CLEAN without tracing both sessions through every shared topic node identified in Phase 2"` (verdict-without-shared-node-examination).

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
| Status quo comparison | Phase 0 keyword-match trace present; STATUS_QUO_COMPARISON labels STATUS_QUO_BLIND_SPOT YES/NO per Found defect | "Status quo behavior is broadly similar -- no significant detection gaps" -- dismissed without per-defect analysis |
| Concurrent session trace | Phase 3.5 traces Session A and Session B through all shared topic nodes; per-node SESSION_VARIABLE_CONFLICT check; SESSION_ISOLATION_VERDICT: CLEAN/COLLISION emitted after all shared nodes examined | "Multiple simultaneous sessions are generally supported by the platform" -- no per-node trace, no variable delta comparison, no isolation verdict |

**Do not begin generating output until you have read every row above.**

---

**Role: FLOW ANALYST**

You are a **Copilot Studio domain expert** acting as the FLOW ANALYST. You know the platform object model: topics, trigger phrases, entities (closed list, regex, system), condition branches, redirect nodes, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation, Error), and session variables (context variables, slot filling, Boolean gates).

Execute Phase 0, Phases 1-3, Phase 3.5, and Phase 4 in order. Then issue ANALYST_HANDOFF.

---

**PHASE 0 -- STATUS_QUO_TRACE**

A status quo trace would say: "Status quo behavior is broadly similar to full simulation -- no significant gaps detected." That output dismisses the comparison without examining any specific turn and cannot show which defects a keyword-only method misses.

**Exit condition:** MAY NOT skip Phase 0. MAY NOT use condition branches, redirect nodes, or session variable logic. MAY NOT write "Status quo behavior is broadly similar" without naming specific turns where keyword matching fails.

| Turn | User Utterance | Keyword(s) Matched | Agent Response (keyword match output) | SQ_MATCH_QUALITY |
|------|--------------|-------------------|---------------------------------------|-----------------|
| 1    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |
| 2    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |
| 3    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |

---

**PHASE 1 -- DEFECT HYPOTHESIS**

A first-pass defect hypothesis would say: "The flow may have issues with fallback coverage and intent conflicts in areas where multiple topics handle similar phrasing." That prediction names no specific topic nodes and cannot be confirmed or refuted.

**Exit condition:** MAY NOT proceed with fewer than four rows. Each row names a specific candidate topic node and suspected condition, or writes "No candidate identified -- reason: [specific reason]." Note Phase 0 signals.

| Defect Type | Predicted Candidate Location (Topic Node) | Suspected Failure Condition | Confidence | Phase 0 Signal |
|-------------|------------------------------------------|-----------------------------|------------|----------------|
| Dead end | [specific topic node or "None suspected"] | [specific condition] | High / Low | [Turn N or "None"] |
| Infinite loop | [specific topic node or redirect entry] | [specific redirect chain] | High / Low | [Turn N or "None"] |
| Intent collision | [specific trigger phrase candidate] | [two candidate topic nodes] | High / Low | [Turn N Ambiguous or "None"] |
| Missing fallback | [specific topic node] | [no no-match branch description] | High / Low | [Turn N No_match or "None"] |

Predictions will be reconciled by the FLOW AUDITOR in Phase 5.

---

**PHASE 2 -- INVENTORY**

A first-pass inventory would say: "The agent includes nodes for handling common order, account, and support scenarios with standard Copilot Studio system topic integrations." That output names no individual topic nodes and hides whether any node lacks a no-match branch.

**Exit condition:** MAY NOT proceed if any table row has an empty cell. MAY NOT replace the table with a summary statement.

| Topic Node (Copilot Studio) | Trigger Phrases | No-Match Branch Defined | Reachable from Entry? |
|-----------------------------|----------------|------------------------|----------------------|

After the table: name the entry topic and all reachable terminal states. Identify the topic node reachable via the greatest number of distinct incoming redirects -- this is the PRIMARY_SHARED_NODE and will be used as Session B's entry point in Phase 3.5.

---

**PHASE 3 -- HAPPY PATH TRACE**

A first-pass happy path trace would say: "User greets the agent. Agent identifies the intent and fulfills the request. Conversation ends normally with session state properly maintained." That output names no topic nodes and tracks no session variables.

**Exit condition:** MAY NOT end on an active topic node. MAY NOT write "Agent responds appropriately" or leave Agent Response blank.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1    | (entry topic)               | "..."                          | "..."                                | ...                           | var = value            |

---

**PHASE 3.5 -- CONCURRENT SESSION TRACE**

A first-pass concurrent session assessment would say: "The agent handles multiple sessions correctly due to platform-level isolation. No additional verification required." That output delegates correctness to a platform guarantee without tracing Session A and Session B through shared nodes -- no per-node variable delta comparison, no SESSION_VARIABLE_CONFLICT check, no SESSION_ISOLATION_VERDICT.

**Exit condition:** MAY NOT write SESSION_ISOLATION_VERDICT: CLEAN without tracing both sessions through every shared topic node identified in Phase 2. MAY NOT write "The platform handles session isolation natively" as the verdict -- trace both sessions and report the variable delta per session per shared node.

Session A: Continues the Phase 3 happy path session (same entry, same variable state at Turn 1).
Session B: Enters at the PRIMARY_SHARED_NODE identified in Phase 2, 1 turn after Session A arrives there. Use a different trigger phrase from the one Session A used to reach that node.

A topic node is SHARED if it appears in the path of both Session A and Session B within the concurrent window.

For each SHARED node, determine:
1. Does Session A write a session variable at this node?
2. Does Session B write the same session variable at this node?
3. If both write to the same variable: SESSION_VARIABLE_CONFLICT: YES (risk of overwrite). If different variables or only one session writes: SESSION_VARIABLE_CONFLICT: NO.

| Shared Topic Node | Session A at Node (Turn N) | Session A Variable Delta | Session B at Node (Turn M) | Session B Variable Delta | SESSION_VARIABLE_CONFLICT |
|-------------------|---------------------------|--------------------------|---------------------------|--------------------------|--------------------------|
| (each shared node) | Turn N | var = value or "no write" | Turn M | var = value or "no write" | YES / NO |

SESSION_ISOLATION_VERDICT: CLEAN if zero SESSION_VARIABLE_CONFLICT: YES rows. COLLISION if any YES row present.

If COLLISION: name the specific shared node, the variable name, and which session's write would be overwritten.

---

**PHASE 4 -- EXCEPTION PATH TRACE**

A first-pass exception trace would say: "When unrecognized input is received, the agent re-prompts. If retries fail, the session escalates to a human agent." That output names no divergence node and is a paraphrase, not a trace.

**Exit condition:** MAY NOT trace the same node sequence as Phase 3. Must branch at a named topic node under a different condition. Where possible, route through the Phase 1 candidate defect node.

Label above: "Diverges from happy path at [node]: condition -- [trigger]."

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|

---

**ANALYST_HANDOFF: COMPLETE. HANDOFF_TO: FLOW AUDITOR.**

---

**Role: FLOW AUDITOR**

You are a **Copilot Studio domain expert** acting as the FLOW AUDITOR. You did not author Phases 0-4 or Phase 3.5. Your verdicts are independent findings from Phase 2 inventory, Phases 3-4 trace tables, and Phase 3.5 concurrent session table. Derive defect verdicts from trace evidence before reading the ANALYST's Phase 1 predictions.

**Received ANALYST_HANDOFF: COMPLETE. Beginning independent audit.**

---

**PHASE 5 -- INDEPENDENT DEFECT SCAN + HYPOTHESIS VERIFICATION + REMEDIATION + COVERAGE + COVERAGE METRICS + STATUS_QUO_COMPARISON**

A first-pass independent audit would say: "All ANALYST findings confirmed. Coverage is adequate. Status quo behavior is broadly similar." That output echoes without verifying, provides no ratios, and dismisses the gap analysis.

**Exit condition:** MAY NOT write "All ANALYST findings confirmed" without citing trace evidence per row. MAY NOT produce fewer than four defect verdicts. MAY NOT use "possible" or "unclear." MAY NOT write "Add better error handling." MAY NOT omit a Phase 2 node from coverage. MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio. MAY NOT write "No significant gaps" as STATUS_QUO_COMPARISON.

Note: If Phase 3.5 SESSION_ISOLATION_VERDICT is COLLISION, report the conflicting shared node as an additional defect finding beyond the four primary types, with Copilot Studio Object to Edit named in the remediation table.

**Defect scan (AUDITOR independent):**

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | name or N/A | describe or "Checked N nodes -- none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect entry or N/A | describe or "Checked all chains -- none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | trigger phrase or N/A | name both topic nodes or "No overlapping phrases found" | Yes / No / N/A |
| Missing fallback | Found / Not found | name or N/A | name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |
| Session isolation | (from Phase 3.5) | node name or N/A | SESSION_VARIABLE_CONFLICT detail or "Phase 3.5 CLEAN" | Yes / No / N/A |

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

| Topic Node (Copilot Studio) | Traced (Happy) | Traced (Exception) | Traced (Session A) | Traced (Session B) | Untraced | Unreachable |
|-----------------------------|---------------|-------------------|-------------------|-------------------|----------|-------------|

**Coverage Metrics:**

| Metric | Formula | Value |
|--------|---------|-------|
| topic_coverage_ratio | N_traced (any path) / N_total | N/N |
| fallback_coverage_ratio | N_nodes_with_fallback_traced / N_nodes_with_no-match_branch_defined | N/N |
| intent_collision_density | N_trigger_phrase_overlaps_found / N_total_trigger_phrases | N/N |

COVERAGE_GATE: CLEAN if topic_coverage_ratio >= 0.70 AND fallback_coverage_ratio >= 0.50. Otherwise: DEGRADED.

**STATUS_QUO_COMPARISON** (Found defects only):

| Defect Type | Defect Location | FOUND_BY_FULL_TRACE | FOUND_BY_STATUS_QUO | STATUS_QUO_BLIND_SPOT | Detection Gap Explanation |
|-------------|----------------|--------------------|--------------------|----------------------|--------------------------|

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All phases as labeled sections including Phase 0 and Phase 3.5. Do not combine phases. Do not omit any table.

---

## V-04 -- Remediation Cycle + Severity Tiers (Two New Mechanisms)

**Axis:** Role sequence (post-audit) + Output format (defect scoring) -- combines V-01's Phase 6 REMEDIATION_VERIFICATION_CYCLE with V-02's DEFECT_SEVERITY block. Tests whether the two candidates are additive: a BLOCKER defect triggers both CRITICAL severity classification and remediation re-trace; Phase 6 confirms BLOCKER_RESOLVED after the CRITICAL-tier fix.
**Hypothesis:** All R7 mechanisms retained → C-01 through C-19 all PASS → 150/150 on v7. V-01's Phase 6 is preserved; V-02's DEFECT_SEVERITY formula and SEVERITY_GATE are preserved. If both mechanisms are independently detectable, evidence for both C-20 (remediation_verification_cycle) and C-21 (formula_based_defect_severity) is present in the same artifact.

**C-16 prohibition distribution (verification):**
- Register-unique: `"session context is maintained appropriately"`, `"Collisions might occur if topics have similar phrasing"`, `"The agent addresses the main scenarios comprehensively"`, `"All ANALYST findings confirmed"`, `"Phase 6 complete -- recommended fix should resolve the issue"`, `"This defect represents a significant risk"`.
- Foil-unique: `"User greets the agent. Agent identifies intent and fulfills request."`, `"When unrecognized input received, agent re-prompts."`, `"Status quo behavior is broadly similar."`, `"The recommended fix addresses the root cause. Testing should confirm."`, `"This defect has a medium impact on user experience."`.
- Exit-unique: `"MAY NOT trace the same node sequence as Phase 3"`, `"MAY NOT use 'possible' or 'unclear' as verdicts"`, `"MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio"`, `"MAY NOT emit REMEDIATION_CYCLE_COMPLETE without a re-trace table for each BLOCKER defect"`, `"MAY NOT emit SEVERITY_GATE: DEPLOYABLE without computing DEFECT_SEVERITY for each Found defect row"`.

All three structures contribute unique prohibited outputs. C-16 PASS condition is met.

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
| Status quo comparison | Phase 0 keyword-match trace present; STATUS_QUO_COMPARISON labels STATUS_QUO_BLIND_SPOT YES/NO per Found defect | "Status quo behavior is broadly similar -- no significant detection gaps" -- dismissed without per-defect analysis |
| Defect severity | DEFECT_SEVERITY: CRITICAL/HIGH/LOW per Found defect with named formula; SEVERITY_GATE: DEPLOYABLE only if zero CRITICAL | "This defect represents a significant risk" -- no tier token, no formula, no gate |
| Remediation cycle | Re-trace shows BLOCKER node processed without failure condition; REMEDIATION_CYCLE_COMPLETE: BLOCKER_RESOLVED emitted | "Phase 6 complete -- recommended fix should resolve the issue" -- no re-trace, no evidence, no token |

**Do not begin generating output until you have read every row above.**

---

**Role: FLOW ANALYST**

You are a **Copilot Studio domain expert** acting as the FLOW ANALYST. Execute Phase 0 and Phases 1-4 in order. Then issue ANALYST_HANDOFF.

---

**PHASE 0 -- STATUS_QUO_TRACE**

A status quo trace would say: "Status quo behavior is broadly similar to full simulation -- no significant gaps detected." That output cannot show which defects a keyword-only method misses.

**Exit condition:** MAY NOT skip Phase 0. MAY NOT use condition branches, redirect nodes, or session variable logic. MAY NOT write "Status quo behavior is broadly similar" without naming specific failing turns.

| Turn | User Utterance | Keyword(s) Matched | Agent Response (keyword match output) | SQ_MATCH_QUALITY |
|------|--------------|-------------------|---------------------------------------|-----------------|
| 1    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |
| 2    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |
| 3    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |

---

**PHASE 1 -- DEFECT HYPOTHESIS**

A first-pass defect hypothesis would say: "The flow may have issues with fallback coverage and intent conflicts in areas where multiple topics handle similar phrasing." That prediction names no specific topic nodes and cannot be confirmed or refuted.

**Exit condition:** MAY NOT proceed with fewer than four rows. Each row names a specific candidate topic node and suspected condition, or writes "No candidate identified -- reason: [specific reason]."

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

A first-pass happy path trace would say: "User greets the agent. Agent identifies the intent and fulfills the request. Conversation ends normally with session state properly maintained." That output tracks no session variables.

**Exit condition:** MAY NOT end on an active topic node. MAY NOT write "Agent responds appropriately" or leave Agent Response blank.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1    | (entry topic)               | "..."                          | "..."                                | ...                           | var = value            |

---

**PHASE 4 -- EXCEPTION PATH TRACE**

A first-pass exception trace would say: "When unrecognized input is received, the agent re-prompts. If retries fail, the session escalates." That output names no divergence node.

**Exit condition:** MAY NOT trace the same node sequence as Phase 3. Must branch at a named topic node under a different condition.

Label above: "Diverges from happy path at [node]: condition -- [trigger]."

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|

---

**ANALYST_HANDOFF: COMPLETE. HANDOFF_TO: FLOW AUDITOR.**

---

**Role: FLOW AUDITOR**

You are a **Copilot Studio domain expert** acting as the FLOW AUDITOR. You did not author Phases 0-4. Your verdicts are independent findings from Phase 2 inventory and Phases 3-4 trace tables. Derive defect verdicts from trace evidence before reading Phase 1.

**Received ANALYST_HANDOFF: COMPLETE. Beginning independent audit.**

---

**PHASE 5 -- INDEPENDENT DEFECT SCAN + DEFECT SEVERITY + HYPOTHESIS VERIFICATION + REMEDIATION + COVERAGE + COVERAGE METRICS + STATUS_QUO_COMPARISON**

A first-pass audit would say: "All ANALYST findings confirmed. This defect has a medium impact on user experience. Coverage is adequate. Status quo behavior is broadly similar." That output echoes without verifying, applies no severity formula, provides no ratios, and dismisses the gap analysis.

**Exit condition:** MAY NOT write "All ANALYST findings confirmed" without citing trace evidence per row. MAY NOT produce fewer than four defect verdicts. MAY NOT use "possible" or "unclear." MAY NOT write "Add better error handling." MAY NOT omit a Phase 2 node. MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio. MAY NOT write "No significant gaps." MAY NOT emit SEVERITY_GATE: DEPLOYABLE without computing DEFECT_SEVERITY for each Found defect row. Flag BLOCKER: Yes/No per defect row -- Phase 6 triggers if any BLOCKER: Yes.

**Defect scan (AUDITOR independent):**

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | name or N/A | describe or "Checked N nodes -- none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect entry or N/A | describe or "Checked all chains -- none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | trigger phrase or N/A | name both topic nodes or "No overlapping phrases found" | Yes / No / N/A |
| Missing fallback | Found / Not found | name or N/A | name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |

**Defect severity** (Found defects only):

Formula: CRITICAL if Dead_end reachable via happy path OR Infinite_loop with no unconditional exit. HIGH if Missing_fallback reachable via > 1 path OR Intent_collision with < 3 unique keywords. LOW otherwise.

| Defect Type | Defect Location | Severity Formula Applied | DEFECT_SEVERITY | SEVERITY_GATE Impact |
|-------------|----------------|--------------------------|----------------|----------------------|

SEVERITY_GATE: DEPLOYABLE if zero CRITICAL defects. HOLD if any CRITICAL present.

**Hypothesis verification:**

| Defect Type | ANALYST Phase 1 Prediction | AUDITOR Trace Verdict | VERIFICATION_VERDICT | Discrepancy Note |
|-------------|---------------------------|----------------------|---------------------|-----------------|
| Dead end | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | (if CHALLENGED: cite turn and node) |
| Infinite loop | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Intent collision | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Missing fallback | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |

**Remediation** (priority order: CRITICAL first):

| Defect | DEFECT_SEVERITY | Topic Node (Copilot Studio) | Exact Change Required | Copilot Studio Object to Edit |
|--------|----------------|------------------------------|----------------------|-------------------------------|

**Coverage:**

| Topic Node (Copilot Studio) | Traced (Happy) | Traced (Exception) | Untraced | Unreachable |
|-----------------------------|---------------|-------------------|----------|-------------|

**Coverage Metrics:**

| Metric | Formula | Value |
|--------|---------|-------|
| topic_coverage_ratio | N_traced (Happy OR Exception) / N_total | N/N |
| fallback_coverage_ratio | N_nodes_with_fallback_traced / N_nodes_with_no-match_branch_defined | N/N |
| intent_collision_density | N_trigger_phrase_overlaps_found / N_total_trigger_phrases | N/N |

COVERAGE_GATE: CLEAN if topic_coverage_ratio >= 0.70 AND fallback_coverage_ratio >= 0.50. Otherwise: DEGRADED.

**STATUS_QUO_COMPARISON** (Found defects only):

| Defect Type | Defect Location | FOUND_BY_FULL_TRACE | FOUND_BY_STATUS_QUO | STATUS_QUO_BLIND_SPOT | Detection Gap Explanation |
|-------------|----------------|--------------------|--------------------|----------------------|--------------------------|

---

**PHASE 6 -- REMEDIATION VERIFICATION CYCLE (Conditional)**

Entry condition: Phase 5 defect scan has at least one BLOCKER: Yes row. If none: "Phase 6 skipped -- no BLOCKER defects. REMEDIATION_CYCLE_COMPLETE: N/A."

A first-pass remediation verification would say: "The recommended fix addresses the root cause. After implementation, testing should confirm resolution." That output describes an expected outcome without tracing it -- no re-trace, no before/after evidence, no REMEDIATION_CYCLE_COMPLETE token.

**Exit condition:** MAY NOT emit REMEDIATION_CYCLE_COMPLETE without a complete re-trace table for each BLOCKER defect. MAY NOT write "Recommended fix should resolve the issue" -- show the re-traced turns. Note: for any BLOCKER defect classified CRITICAL in DEFECT_SEVERITY, the re-trace must explicitly confirm the CRITICAL failure condition is absent (not only that the node processes differently).

For each BLOCKER defect:
1. State the remediation applied (exact change from Phase 5 Copilot Studio Object to Edit column).
2. Re-trace the minimal path from entry trigger to the previously-failing node.
3. Emit REMEDIATION_CYCLE_COMPLETE per defect.

| Turn | Topic Node (Copilot Studio) | User Utterance | Agent Response | Remediation Applied | FAILURE_CONDITION_PRESENT |
|------|-----------------------------|---------------|----------------|---------------------|--------------------------|
| 1    | (entry or redirect)         | "..."         | "..."          | [change name]       | No -- condition absent / Yes -- persists |

REMEDIATION_CYCLE_COMPLETE: [defect_type] -- BLOCKER_RESOLVED / BLOCKER_PERSISTS.

If BLOCKER_PERSISTS: name the specific turn where the failure condition persisted and state why the Phase 5 remediation was insufficient.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All phases as labeled sections including Phase 0 and Phase 6 (or Phase 6 skipped notice). Do not combine phases. Do not omit any table.

---

## V-05 -- Full Extension Ceiling (All Three New Mechanisms)

**Axis:** Full extension ceiling -- all three R8 new mechanisms (remediation cycle + severity tiers + concurrent session trace) combined with all ten R7 mechanisms.
**Hypothesis:** All R7 mechanisms retained → C-01 through C-19 all PASS → 150/150 on v7. All three R8 new mechanisms present simultaneously: Phase 6 REMEDIATION_VERIFICATION_CYCLE (C-20 candidate), DEFECT_SEVERITY formula and SEVERITY_GATE (C-21 candidate), Phase 3.5 CONCURRENT_SESSION_TRACE and SESSION_ISOLATION_VERDICT (C-22 candidate). Each new mechanism contributes non-redundant evidence beyond the v7 ceiling. Expected: 150/150 confirmed + three C-20/C-21/C-22 candidate signals each present and independently attributable.

**C-16 prohibition distribution (verification for v7 compliance):**
- Register-unique: `"session context is maintained appropriately"` (no-variable-name omission); `"Collisions might occur if topics have similar phrasing"` (no-predicted-node hypothesis); `"The agent addresses the main scenarios comprehensively"` (no-per-node inventory); `"All ANALYST findings confirmed"` (echo-without-evidence); `"Phase 6 complete -- recommended fix should resolve the issue"` (remediation-claimed-without-re-trace); `"This defect represents a significant risk"` (severity-claim-without-formula); `"Multiple simultaneous sessions are generally supported by the platform"` (platform-guarantee-without-trace).
- Foil-unique: `"User greets the agent. Agent identifies intent and fulfills request. Conversation ends normally."` (prose-trace-instead-of-table); `"When unrecognized input received, agent re-prompts; if retries fail, escalates."` (exception-path-as-summary); `"Status quo behavior is broadly similar to full simulation -- no significant gaps detected."` (gap-dismissed-without-examination); `"The recommended fix addresses the root cause. After implementation, testing should confirm resolution."` (expectation-without-re-trace); `"This defect has a medium impact on user experience. Priority fix recommended."` (impact-claim-without-tier); `"The agent handles multiple sessions correctly due to platform-level isolation."` (delegation-without-verification).
- Exit-unique: `"MAY NOT trace the same node sequence as Phase 3 with a different utterance"` (path non-uniqueness failure); `"MAY NOT use 'possible' or 'unclear' as verdicts"` (specific forbidden verdict words); `"MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio"` (ratio-absent gate assertion); `"MAY NOT emit REMEDIATION_CYCLE_COMPLETE without a re-trace table for each BLOCKER defect"` (token-without-evidence); `"MAY NOT emit SEVERITY_GATE: DEPLOYABLE without computing DEFECT_SEVERITY for each Found defect row"` (gate-without-formula); `"MAY NOT write SESSION_ISOLATION_VERDICT: CLEAN without tracing both sessions through every shared topic node"` (verdict-without-shared-node-examination).

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
| Status quo comparison | Phase 0 keyword-match trace present; STATUS_QUO_COMPARISON labels STATUS_QUO_BLIND_SPOT YES/NO per Found defect | "Status quo behavior is broadly similar -- no significant detection gaps" -- dismissed without per-defect analysis |
| Defect severity | DEFECT_SEVERITY: CRITICAL/HIGH/LOW per Found defect with named formula; SEVERITY_GATE: DEPLOYABLE only if zero CRITICAL | "This defect represents a significant risk" -- no tier token, no formula, no gate |
| Concurrent session trace | Phase 3.5 traces Session A and Session B through all shared nodes; per-node SESSION_VARIABLE_CONFLICT; SESSION_ISOLATION_VERDICT emitted | "Multiple simultaneous sessions are generally supported by the platform" -- no per-node trace, no variable comparison, no verdict |
| Remediation cycle | Re-trace shows BLOCKER node processed without failure condition; REMEDIATION_CYCLE_COMPLETE: BLOCKER_RESOLVED | "Phase 6 complete -- recommended fix should resolve the issue" -- no re-trace, no evidence, no token |

**Do not begin generating output until you have read every row above.**

---

**Role: FLOW ANALYST**

You are a **Copilot Studio domain expert** acting as the FLOW ANALYST. You know the platform object model: topics, trigger phrases, entities (closed list, regex, system), condition branches, redirect nodes, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation, Error), and session variables (context variables, slot filling, Boolean gates).

Execute Phase 0, Phases 1-3, Phase 3.5, and Phase 4 in order. Then issue ANALYST_HANDOFF.

---

**PHASE 0 -- STATUS_QUO_TRACE**

A status quo trace would say: "Status quo behavior is broadly similar to full simulation -- no significant gaps detected." That output dismisses the comparison without examining any specific turn and cannot show which defects a keyword-only method misses.

**Exit condition:** MAY NOT skip Phase 0. MAY NOT use condition branches, redirect nodes, or session variable logic. MAY NOT write "Status quo behavior is broadly similar" without naming specific turns where keyword matching produces Ambiguous or No_match quality.

| Turn | User Utterance | Keyword(s) Matched | Agent Response (keyword match output) | SQ_MATCH_QUALITY |
|------|--------------|-------------------|---------------------------------------|-----------------|
| 1    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |
| 2    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |
| 3    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |

---

**PHASE 1 -- DEFECT HYPOTHESIS**

A first-pass defect hypothesis would say: "The flow may have issues with fallback coverage and intent conflicts in areas where multiple topics handle similar phrasing." That prediction names no specific topic nodes, states no failure conditions, and cannot be confirmed or refuted -- it is a paraphrase of a hypothesis, not a hypothesis.

**Exit condition:** MAY NOT proceed with fewer than four rows, one per defect type. MAY NOT write "Possible issues may exist throughout" -- each row names a specific candidate topic node and a specific suspected condition, or writes "No candidate identified -- reason: [specific reason from the input signals]." Note any Phase 0 Ambiguous/No_match rows that update a hypothesis.

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

After the table: name the entry topic and all reachable terminal states. Identify the PRIMARY_SHARED_NODE (topic node reachable via the greatest number of distinct incoming redirects) for use in Phase 3.5.

---

**PHASE 3 -- HAPPY PATH TRACE**

A first-pass happy path trace would say: "User greets the agent. Agent identifies the intent and fulfills the request. Conversation ends normally with session state properly maintained." That output names no topic nodes, shows no utterances, writes no agent response text, and tracks no session variables -- a description of a trace, not a trace.

**Exit condition:** MAY NOT end on an active topic node -- final row must name a terminal state. MAY NOT write "Agent responds appropriately" or leave Agent Response blank; actual message text required in every row.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1    | (entry topic)               | "..."                          | "..."                                | ...                           | var = value            |

---

**PHASE 3.5 -- CONCURRENT SESSION TRACE**

A first-pass concurrent session assessment would say: "The agent handles multiple sessions correctly due to platform-level isolation. No additional verification required." That output delegates correctness to a platform guarantee without tracing shared nodes -- no per-node variable delta comparison, no SESSION_VARIABLE_CONFLICT check, no SESSION_ISOLATION_VERDICT.

**Exit condition:** MAY NOT write SESSION_ISOLATION_VERDICT: CLEAN without tracing both sessions through every shared topic node identified in Phase 2. MAY NOT write "The platform handles session isolation natively" -- trace both sessions and report the variable delta per session per shared node.

Session A: Continues the Phase 3 happy path session state at Turn 1.
Session B: Enters at the PRIMARY_SHARED_NODE from Phase 2, 1 turn after Session A arrives there, using a different trigger phrase.

A topic node is SHARED if reachable by both Session A and Session B within the concurrent window.

| Shared Topic Node | Session A at Node (Turn N) | Session A Variable Delta | Session B at Node (Turn M) | Session B Variable Delta | SESSION_VARIABLE_CONFLICT |
|-------------------|---------------------------|--------------------------|---------------------------|--------------------------|--------------------------|
| (each shared node) | Turn N | var = value or "no write" | Turn M | var = value or "no write" | YES / NO |

SESSION_ISOLATION_VERDICT: CLEAN if zero SESSION_VARIABLE_CONFLICT: YES rows. COLLISION if any YES row present.

If COLLISION: name the node, the variable, and which session's write would be overwritten.

---

**PHASE 4 -- EXCEPTION PATH TRACE**

A first-pass exception trace would say: "When unrecognized input is received, the agent re-prompts. If retries fail, the session escalates to a human agent." That output names no divergence node, states no triggering condition, and is a paraphrase, not an exception trace.

**Exit condition:** MAY NOT trace the same node sequence as Phase 3 with a different utterance -- path non-uniqueness is a structural failure. Must branch at a named topic node under a different condition and reach a different terminal OR traverse a different node set. Where possible, route through the Phase 1 candidate defect node.

Label above: "Diverges from happy path at [node]: condition -- [what triggers the branch]."

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|

---

**ANALYST_HANDOFF: COMPLETE. HANDOFF_TO: FLOW AUDITOR.**

---

**Role: FLOW AUDITOR**

You are a **Copilot Studio domain expert** acting as the FLOW AUDITOR. You did not author Phases 0-4 or Phase 3.5. Your defect scan, hypothesis verification, severity assessment, coverage metrics, status quo comparison, and remediation verification below are independent findings derived from the Phase 2 inventory, Phases 3-4 trace tables, and Phase 3.5 concurrent session table. Derive defect verdicts from trace evidence before reading the ANALYST's Phase 1 predictions.

**Received ANALYST_HANDOFF: COMPLETE. Beginning independent audit.**

---

**PHASE 5 -- INDEPENDENT DEFECT SCAN + DEFECT SEVERITY + HYPOTHESIS VERIFICATION + REMEDIATION + COVERAGE + COVERAGE METRICS + STATUS_QUO_COMPARISON**

A first-pass independent audit would say: "All ANALYST findings confirmed. This defect has a medium impact on user experience. Coverage is adequate for primary scenarios. Status quo behavior is broadly similar -- no significant detection gaps." That output echoes without verifying, applies no severity formula, provides no tier tokens, provides no ratios, and dismisses the gap analysis without examining Phase 0 turn quality.

**Exit condition:** MAY NOT write "All ANALYST findings confirmed" without citing trace evidence per row. MAY NOT produce fewer than four defect verdicts. MAY NOT use "possible" or "unclear." MAY NOT write "Add better error handling." MAY NOT omit a Phase 2 node from coverage. MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio. MAY NOT write "No significant gaps" as STATUS_QUO_COMPARISON. MAY NOT emit SEVERITY_GATE: DEPLOYABLE without computing DEFECT_SEVERITY for each Found defect row. Flag BLOCKER: Yes/No per defect -- Phase 6 triggers if any BLOCKER: Yes. If Phase 3.5 SESSION_ISOLATION_VERDICT is COLLISION, add a session_isolation row to the defect scan.

**Defect scan (AUDITOR independent):**

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | name or N/A | describe or "Checked N nodes -- none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect entry or N/A | describe or "Checked all chains -- none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | trigger phrase or N/A | name both topic nodes or "No overlapping phrases found" | Yes / No / N/A |
| Missing fallback | Found / Not found | name or N/A | name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |
| Session isolation | (from Phase 3.5 verdict) | node name or N/A | SESSION_VARIABLE_CONFLICT detail or "Phase 3.5 CLEAN -- no concurrent write conflicts" | Yes / No / N/A |

**Defect severity** (Found defects only):

Formula: CRITICAL if Dead_end reachable via Phase 3 happy path OR Infinite_loop with no unconditional exit. HIGH if Missing_fallback reachable via > 1 path OR Intent_collision with < 3 unique keywords OR Session_isolation COLLISION at a node with > 1 incoming redirect. LOW otherwise.

| Defect Type | Defect Location | Severity Formula Applied | DEFECT_SEVERITY | SEVERITY_GATE Impact |
|-------------|----------------|--------------------------|----------------|----------------------|

SEVERITY_GATE: DEPLOYABLE if zero CRITICAL defects in the Found set. HOLD if any CRITICAL defect present.

**Hypothesis verification:**

| Defect Type | ANALYST Phase 1 Prediction | AUDITOR Trace Verdict | VERIFICATION_VERDICT | Discrepancy Note |
|-------------|---------------------------|----------------------|---------------------|-----------------|
| Dead end | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | (if CHALLENGED: cite turn and node) |
| Infinite loop | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Intent collision | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Missing fallback | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |

**Remediation** (priority order: CRITICAL first):

| Defect | DEFECT_SEVERITY | Topic Node (Copilot Studio) | Exact Change Required | Copilot Studio Object to Edit |
|--------|----------------|------------------------------|----------------------|-------------------------------|

If no defects found: "No defects found -- no remediations required."

**Coverage** (every Phase 2 node gets a row; include Session A and Session B columns from Phase 3.5):

| Topic Node (Copilot Studio) | Traced (Happy) | Traced (Exception) | Traced (Session A) | Traced (Session B) | Untraced | Unreachable |
|-----------------------------|---------------|-------------------|-------------------|-------------------|----------|-------------|

**Coverage Metrics:**

| Metric | Formula | Value |
|--------|---------|-------|
| topic_coverage_ratio | N_traced (any path) / N_total | N/N |
| fallback_coverage_ratio | N_nodes_with_fallback_traced / N_nodes_with_no-match_branch_defined | N/N |
| intent_collision_density | N_trigger_phrase_overlaps_found / N_total_trigger_phrases | N/N |

COVERAGE_GATE: CLEAN if topic_coverage_ratio >= 0.70 AND fallback_coverage_ratio >= 0.50. Otherwise: DEGRADED.

If DEGRADED: list the specific topic nodes that must be traced to bring topic_coverage_ratio to >= 0.70.

**STATUS_QUO_COMPARISON** (Found defects only):

| Defect Type | Defect Location | FOUND_BY_FULL_TRACE | FOUND_BY_STATUS_QUO | STATUS_QUO_BLIND_SPOT | Detection Gap Explanation |
|-------------|----------------|--------------------|--------------------|----------------------|--------------------------|

STATUS_QUO_BLIND_SPOT: YES if Phase 0 keyword-matching-only method would not have detected this defect. NO if keyword matching alone would surface it.

---

**PHASE 6 -- REMEDIATION VERIFICATION CYCLE (Conditional)**

Entry condition: Phase 5 defect scan has at least one row with BLOCKER: Yes. If no BLOCKER defects: write "Phase 6 skipped -- no BLOCKER defects identified. REMEDIATION_CYCLE_COMPLETE: N/A."

A first-pass remediation verification would say: "The recommended fix addresses the root cause. After implementation, testing should confirm resolution." That output describes an expected outcome without tracing it -- no re-trace table, no before/after evidence, no REMEDIATION_CYCLE_COMPLETE token with a specific verdict.

**Exit condition:** MAY NOT emit REMEDIATION_CYCLE_COMPLETE without a complete re-trace table for each BLOCKER defect showing the specific turns that previously exhibited the failure condition and now do not. MAY NOT write "Recommended fix should resolve the issue" -- show the re-traced turns. For any BLOCKER defect classified CRITICAL in DEFECT_SEVERITY, the re-trace must explicitly confirm the CRITICAL failure condition is absent (not only that the node processes differently). MAY NOT emit BLOCKER_RESOLVED without identifying the specific turn in the re-trace where the failure condition is absent.

For each BLOCKER defect from Phase 5:
1. State the remediation applied: "[exact change from Phase 5 Copilot Studio Object to Edit column]."
2. Re-trace the minimal path from the entry trigger to the previously-failing node and beyond.
3. Emit REMEDIATION_CYCLE_COMPLETE per defect.

| Turn | Topic Node (Copilot Studio) | User Utterance | Agent Response | Remediation Applied | FAILURE_CONDITION_PRESENT |
|------|-----------------------------|---------------|----------------|---------------------|--------------------------|
| 1    | (entry or redirect)         | "..."         | "..."          | [name of change]    | No -- condition absent / Yes -- persists |

REMEDIATION_CYCLE_COMPLETE: [defect_type] -- BLOCKER_RESOLVED (failure condition absent in re-trace) / BLOCKER_PERSISTS (failure condition still present -- remediation insufficient, escalate).

If BLOCKER_PERSISTS: name the specific turn in the re-trace where the failure condition persisted and state why the Phase 5 remediation was insufficient.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All phases as labeled sections including Phase 0, Phase 3.5, and Phase 6 (or Phase 6 skipped notice). Do not combine phases. Do not omit any table.

---

### Predicted Round 8 Scores on v7

| Variation | Mechanisms | C-20 (remediation_cycle) | C-21 (severity_tiers) | C-22 (concurrent_sessions) | v7 score |
|-----------|------------|--------------------------|----------------------|---------------------------|----------|
| V-01 Remediation Cycle | All R7 + Phase 6 | PASS | FAIL | FAIL | 150/150 |
| V-02 Severity Tiers | All R7 + DEFECT_SEVERITY | FAIL | PASS | FAIL | 150/150 |
| V-03 Concurrent Sessions | All R7 + Phase 3.5 | FAIL | FAIL | PASS | 150/150 |
| V-04 Remediation + Severity | All R7 + V-01 + V-02 | PASS | PASS | FAIL | 150/150 |
| V-05 Full Extension Ceiling | All R7 + all three | PASS | PASS | PASS | 150/150 |

All five variations score 150/150 on v7. No v7 criterion is broken by any new mechanism. Three new C-20/C-21/C-22 candidate signals are present in V-05. A v8 rubric upgrade is expected if all three mechanisms are confirmed structurally independent from C-01 through C-19.
