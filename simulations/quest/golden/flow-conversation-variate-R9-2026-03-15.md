# flow-conversation Variate -- Round 9
**Date:** 2026-03-15
**Rubric:** v8 (C-01 through C-22, max 165 pts)
**Target axes:** Three new axes beyond the v8 ceiling -- third-role graph structure review, trigger phrase canonicalization, session variable lifecycle audit
**Baseline:** R8 V-05 confirmed 165/165 on v8 rubric (all thirteen mechanisms: phases + CS headers + named prohibitions + pre-instruction register + per-section foils + pre-trace hypothesis + cross-mechanism prohibition convergence + role-independent verification + quantitative coverage threshold + detection gap audit + remediation verification cycle + formula-based defect severity + concurrent session interference). All R9 variations carry every R8 mechanism. The only variation per V-01/V-02/V-03 is the new mechanism added. Each new mechanism probes whether a C-23+ candidate emerges.

---

## Round 9 Variation Map

| Variation | Axis | New Mechanism | All R8 Mechanisms? | Predicted (v8) | C-23+ Candidate | Hypothesis |
|-----------|------|---------------|-------------------|----------------|-----------------|------------|
| V-01 | Role sequence | Phase 2.5 GRAPH_STRUCTURE_REVIEW by a third named role FLOW ARCHITECT scoped to graph reachability only; GRAPH_STRUCTURE_VERDICT: CONNECTED / FRAGMENTED | All PASS | 165/165 | graph_structure_review | C-07 requires labeling every node traced/untraced -- no graph-traversal role and no binary connectivity verdict required. A prompt passing C-07 can still assign all graph work to one role with no formal reachability check. Phase 2.5 introduces a third independent role whose only scope is graph-structure integrity, creating a structural pathway for FRAGMENTED verdicts that no existing criterion requires. |
| V-02 | Output format | Phase 1.5 TRIGGER_PHRASE_CANONICALIZATION normalizes all Phase 2 trigger phrases to lowercase tokens before collision detection; emits CANONICAL_FORM per phrase and CANONICAL_COLLISION_VERDICT: CLEAN / COLLISION_DETECTED | All PASS | 165/165 | trigger_phrase_canonicalization | C-02 detects intent collisions on raw trigger phrase text. Normalization (lowercase, deduplicate, synonym-collapse) surfaces collisions invisible to raw matching ("Cancel my order" vs "order cancellation" are distinct raw but collide canonically). A C-02-passing prompt can still miss normalized-form collisions and have no canonical form table or canonicalization verdict. |
| V-03 | Lifecycle emphasis | Phase 5.5 SESSION_VARIABLE_LIFECYCLE_AUDIT maps SET / READ / CLEAR operations per variable across all traced turns and detects READ-before-SET (undefined read); VARIABLE_LIFECYCLE_VERDICT: SAFE / UNDEFINED_READ_RISK per variable | All PASS | 165/165 | session_variable_lifecycle | C-05 tracks variable values at turns where they change -- not the SET/READ/CLEAR ordering sequence. A C-05-passing prompt can have a variable that is READ before its first SET (undefined read risk) with no verdict, because the value-change trace shows only what the variable holds, not whether any READ preceded the assignment. |
| V-04 | Role sequence + Output format | Phase 2.5 GRAPH_STRUCTURE_REVIEW (V-01) + Phase 1.5 TRIGGER_PHRASE_CANONICALIZATION (V-02) | All PASS | 165/165 | graph_structure + canonicalization | Tests additivity: ARCHITECT flags unreachable nodes; canonicalization surfaces synonym-collision topics that the ANALYST's raw-text hypothesis might miss. Both tokens (GRAPH_STRUCTURE_VERDICT, CANONICAL_COLLISION_VERDICT) independently attributable. |
| V-05 | Full extension ceiling | All three new R9 mechanisms: GRAPH_STRUCTURE_REVIEW + TRIGGER_PHRASE_CANONICALIZATION + SESSION_VARIABLE_LIFECYCLE_AUDIT, on top of all R8 mechanisms | All PASS | 165/165 | all three active | Evidence pool for v9 rubric. GRAPH_STRUCTURE_VERDICT, CANONICAL_COLLISION_VERDICT, and VARIABLE_LIFECYCLE_VERDICT each independently attributable; lifecycle audit extends Phase 5.5 after all defect and severity work is complete; ARCHITECT role adds a third scoped agent between inventory and trace phases. |

---

## V-01 -- Third-Role Graph Structure Review

**Axis:** Role sequence -- Insert FLOW ARCHITECT between ANALYST inventory and trace phases. ARCHITECT is scoped exclusively to Phase 2.5 GRAPH_STRUCTURE_REVIEW. All R8 mechanisms retained.

**Hypothesis:** All R8 mechanisms retained → C-01 through C-22 all PASS → 165/165 on v8. C-07 requires labeling every topic node as traced or untraced but assigns no role boundary and requires no binary connectivity verdict. Phase 2.5 introduces a third named role whose scope is explicitly disjoint from ANALYST (Phases 0-2, 3-4) and AUDITOR (Phase 5-6): the ARCHITECT reviews the Phase 2 inventory for graph-level reachability and emits GRAPH_STRUCTURE_VERDICT: CONNECTED / FRAGMENTED. A prompt passing C-07 can still perform all graph analysis in one role without a formal reachability proof or a connectivity gate. C-23 candidate: graph_structure_review.

**C-16 prohibition distribution (verification):**
- Register-unique: `"The conversation flow has some nodes that may not be reachable from the entry point"` (assertion-without-connectivity-verdict); `"All ANALYST findings confirmed"` (echo-without-evidence).
- Foil-unique (Phase 2.5): `"Graph structure looks acceptable. No major structural issues identified."` (no-CONNECTED-FRAGMENTED-verdict, no named unreachable nodes); (Phase 3): `"User greets the agent. Agent identifies the intent and fulfills the request. Conversation ends normally."` (prose-trace, no per-turn data).
- Exit-unique: `"MAY NOT emit GRAPH_STRUCTURE_VERDICT: CONNECTED without naming every node reachable from the entry topic by forward traversal"` (connectivity-claimed-without-traversal); `"MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio"` (ratio-absent gate); `"MAY NOT emit REMEDIATION_CYCLE_COMPLETE without a re-trace table"` (token-without-evidence).

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
| Pre-trace hypothesis | Hypothesis table for all four defect types with predicted candidate locations before any trace phase; verdict section reconciles each prediction against findings | "Collisions might occur if topics have similar phrasing" -- no predicted node named, zero points |
| Role independence | AUDITOR states it did not author Phases 0-4; each VERIFICATION_VERDICT cites trace evidence; AUDITOR may write CHALLENGED | "All ANALYST findings confirmed" without trace citations -- echo with no independent verification |
| Coverage metrics | topic_coverage_ratio and fallback_coverage_ratio as N/N decimals; COVERAGE_GATE: CLEAN or DEGRADED with threshold comparison | "Coverage is adequate for primary scenarios" -- no ratios, no gate verdict |
| Status quo comparison | Phase 0 keyword-match trace present; STATUS_QUO_COMPARISON labels STATUS_QUO_BLIND_SPOT YES/NO per Found defect | "Status quo behavior is broadly similar -- no significant detection gaps" -- dismissed without per-defect analysis |
| Defect severity | DEFECT_SEVERITY: CRITICAL/HIGH/LOW computed with named formula per Found defect; SEVERITY_GATE: DEPLOYABLE only if zero CRITICAL defects | "This defect represents a significant risk" -- no tier token, no formula applied, no gate |
| Remediation cycle | Re-trace table shows BLOCKER node processed without failure condition after remediation applied; REMEDIATION_CYCLE_COMPLETE: BLOCKER_RESOLVED emitted | "Phase 6 complete -- recommended fix should resolve the issue" -- no re-trace, no token |
| Concurrent session | SESSION_ISOLATION_VERDICT: CLEAN or COLLISION emitted after tracing two simultaneous sessions through shared nodes; per-node SESSION_VARIABLE_CONFLICT: YES/NO | "Concurrent usage may cause issues in shared topics" -- no per-session trace, no per-node verdict |
| Graph structure verdict | GRAPH_STRUCTURE_VERDICT: CONNECTED with every reachable node named by ARCHITECT forward traversal, OR FRAGMENTED with specific disconnected subgraph named | "The conversation flow has some nodes that may not be reachable from the entry point" -- assertion without ARCHITECT role, without CONNECTED/FRAGMENTED token, without named traversal |

**Do not begin generating output until you have read every row above.**

---

**Role: FLOW ANALYST**

You are a **Copilot Studio domain expert** acting as the FLOW ANALYST. You know the platform object model: topics, trigger phrases, entities (closed list, regex, system), condition branches, redirect nodes, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation, Error), and session variables (context variables, slot filling, Boolean gates).

Execute Phase 0 and Phases 1-2, then issue ANALYST_INVENTORY_HANDOFF to the FLOW ARCHITECT. After the ARCHITECT completes Phase 2.5, execute Phases 3-4, then issue ANALYST_HANDOFF to the FLOW AUDITOR.

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

**Exit condition:** MAY NOT proceed with fewer than four rows, one per defect type. Each row names a specific candidate topic node and a specific suspected condition, or writes "No candidate identified -- reason: [specific reason from the input signals]." Note any Phase 0 Ambiguous/No_match rows that update a hypothesis.

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

**ANALYST_INVENTORY_HANDOFF: COMPLETE. HANDOFF_TO: FLOW ARCHITECT for Phase 2.5.**

---

**Role: FLOW ARCHITECT**

You are a **Copilot Studio domain expert** acting as the FLOW ARCHITECT. You did not author Phases 0-2. Your scope is exclusively graph-level structural integrity: reachability, connectivity, and missing redirect targets. You do not trace dialog turns. You do not scan for defects. You review the Phase 2 inventory table and the named entry topic to determine whether the conversation graph is fully connected or fragmented.

**Received ANALYST_INVENTORY_HANDOFF: COMPLETE. Beginning graph structure review.**

---

**PHASE 2.5 -- GRAPH_STRUCTURE_REVIEW**

A first-pass graph structure review would say: "Graph structure looks acceptable. No major structural issues identified." That output asserts a verdict without performing forward traversal from the entry topic, names no reachable nodes, names no unreachable nodes, and emits no GRAPH_STRUCTURE_VERDICT token.

**Exit condition:** MAY NOT emit GRAPH_STRUCTURE_VERDICT: CONNECTED without naming every node reachable from the entry topic by forward traversal through redirect nodes. MAY NOT emit GRAPH_STRUCTURE_VERDICT: FRAGMENTED without naming the specific disconnected subgraph and the missing redirect that would connect it. MAY NOT summarize without a per-node reachability row.

Perform forward traversal from the entry topic named in Phase 2. Follow all redirect nodes and condition branch targets. Mark each Phase 2 node as Reachable or Unreachable.

| Topic Node (Copilot Studio) | Reachable from Entry? | Reached Via (redirect or trigger) | Missing Redirect Target (if Unreachable) |
|-----------------------------|----------------------|-----------------------------------|-----------------------------------------|

GRAPH_STRUCTURE_VERDICT: CONNECTED if every topic node in Phase 2 is Reachable. FRAGMENTED if any node is Unreachable.

If FRAGMENTED: name the specific subgraph isolated and the redirect node that must be added to connect it.

**ARCHITECT_HANDOFF: COMPLETE. HANDOFF_TO: FLOW ANALYST to continue Phases 3-4.**

---

**Role: FLOW ANALYST (resumed)**

You are the FLOW ANALYST. The FLOW ARCHITECT has completed Phase 2.5. Continue with Phase 3, routing traces through nodes the ARCHITECT identified as Reachable. If the ARCHITECT emitted GRAPH_STRUCTURE_VERDICT: FRAGMENTED, note which nodes are excluded from traces due to unreachability.

---

**PHASE 3 -- HAPPY PATH TRACE**

A first-pass happy path trace would say: "User greets the agent. Agent identifies the intent and fulfills the request. Conversation ends normally with session state properly maintained." That output names no topic nodes, shows no utterances, writes no agent response text, and tracks no session variables -- a description of a trace, not a trace.

**Exit condition:** MAY NOT end on an active topic node -- final row must name a terminal state. MAY NOT write "Agent responds appropriately" or leave Agent Response blank; actual message text required in every row.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1    | (entry topic)               | "..."                          | "..."                                | ...                           | var = value            |

---

**PHASE 3.5 -- CONCURRENT_SESSION_TRACE**

Trace two simultaneous user sessions (Session A and Session B) through the shared topic nodes identified in Phase 3. For each shared node, determine whether a session variable value set by Session A could be overwritten or misread by Session B before Session A reads it.

**Exit condition:** MAY NOT declare concurrent trace complete without one SESSION_VARIABLE_CONFLICT verdict per shared node. MAY NOT write "Concurrent usage may cause issues" -- produce the per-session turn table.

| Turn | Topic Node (Copilot Studio) | Session A Utterance | Session A Variable State | Session B Utterance | Session B Variable State | SESSION_VARIABLE_CONFLICT |
|------|-----------------------------|--------------------|--------------------------|--------------------|--------------------------|-----------------------------|
| 1    | (shared node)               | "..."              | var = value_A            | "..."              | var = value_B            | YES / NO |

SESSION_ISOLATION_VERDICT: CLEAN if no SESSION_VARIABLE_CONFLICT: YES rows. COLLISION if any YES row present.

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

You are a **Copilot Studio domain expert** acting as the FLOW AUDITOR. You did not author Phases 0-4 or Phase 2.5. Your defect scan, hypothesis verification, coverage metrics, status quo comparison, defect severity, and remediation verification below are independent findings derived from the Phase 2 inventory and Phases 3-4 trace tables. Derive defect verdicts from trace evidence before reading the ANALYST's Phase 1 predictions.

**Received ANALYST_HANDOFF: COMPLETE. Beginning independent audit.**

---

**PHASE 5 -- INDEPENDENT DEFECT SCAN + DEFECT SEVERITY + HYPOTHESIS VERIFICATION + REMEDIATION + COVERAGE + COVERAGE METRICS + STATUS_QUO_COMPARISON**

A first-pass independent audit would say: "All ANALYST findings confirmed. Coverage is adequate for primary scenarios. Status quo behavior is broadly similar -- no significant detection gaps." That output echoes without verifying, provides no ratios, and dismisses the gap analysis without examining Phase 0 turn quality.

**Exit condition:** MAY NOT write "All ANALYST findings confirmed" without citing trace evidence per row. MAY NOT produce fewer than four defect verdicts. MAY NOT use "possible" or "unclear." MAY NOT write "Add better error handling." MAY NOT omit a Phase 2 node from coverage. MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio. MAY NOT write "No significant gaps" as STATUS_QUO_COMPARISON. MAY NOT emit SEVERITY_GATE: DEPLOYABLE without computing DEFECT_SEVERITY for each Found defect row. Flag each Found defect BLOCKER: Yes or No -- Phase 6 triggers if any row has BLOCKER: Yes.

**Defect scan (AUDITOR independent):**

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | name or N/A | describe or "Checked N nodes -- none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect entry or N/A | describe or "Checked all chains -- none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | trigger phrase or N/A | name both topic nodes or "No overlapping phrases found" | Yes / No / N/A |
| Missing fallback | Found / Not found | name or N/A | name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |

**Defect severity** (Found defects only -- apply formula before proceeding to remediation):

Formula:
- CRITICAL: defect_type is Dead_end AND the dead-end node is reachable via the Phase 3 happy path; OR defect_type is Infinite_loop AND no condition branch provides an unconditional exit.
- HIGH: defect_type is Missing_fallback AND the topic node is reachable via more than one distinct path; OR defect_type is Intent_collision AND the colliding phrase contains fewer than 3 unique keywords.
- LOW: all other Found defects.

| Defect Type | Defect Location | Severity Formula Applied | DEFECT_SEVERITY | SEVERITY_GATE Impact |
|-------------|----------------|--------------------------|----------------|----------------------|

SEVERITY_GATE: DEPLOYABLE if zero CRITICAL defects. HOLD if any CRITICAL defect present.

**Hypothesis verification:**

| Defect Type | ANALYST Phase 1 Prediction | AUDITOR Trace Verdict | VERIFICATION_VERDICT | Discrepancy Note |
|-------------|---------------------------|----------------------|---------------------|-----------------|
| Dead end | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | (if CHALLENGED: cite turn and node) |
| Infinite loop | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Intent collision | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Missing fallback | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |

**Remediation** (one row per Found defect -- CRITICAL first):

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

STATUS_QUO_BLIND_SPOT: YES if Phase 0 keyword-matching-only method would not have detected this defect. NO if keyword matching alone would surface it.

---

**PHASE 6 -- REMEDIATION VERIFICATION CYCLE (Conditional)**

Entry condition: Phase 5 defect scan contains at least one row with BLOCKER: Yes. If no BLOCKER defects: write "Phase 6 skipped -- no BLOCKER defects identified. REMEDIATION_CYCLE_COMPLETE: N/A."

If entry condition met:

A first-pass remediation verification would say: "The recommended fix addresses the root cause. After implementation, testing should confirm resolution." That output describes an expected outcome without tracing it -- no re-trace table, no before/after evidence, no REMEDIATION_CYCLE_COMPLETE token.

**Exit condition:** MAY NOT emit REMEDIATION_CYCLE_COMPLETE without a complete re-trace table for each BLOCKER defect showing the specific turns that previously exhibited the failure condition and now do not. MAY NOT write "Recommended fix should resolve the issue." MAY NOT emit BLOCKER_RESOLVED without identifying the specific turn in the re-trace where the failure condition is absent.

For each BLOCKER defect from Phase 5:
1. State the remediation applied: "[exact change from Phase 5 Copilot Studio Object to Edit column]."
2. Re-trace the minimal path from entry to the previously-failing node, showing the node now processes without the failure condition.
3. Emit REMEDIATION_CYCLE_COMPLETE per defect.

| Turn | Topic Node (Copilot Studio) | User Utterance | Agent Response | Remediation Applied | FAILURE_CONDITION_PRESENT |
|------|-----------------------------|---------------|----------------|---------------------|--------------------------|
| 1    | (entry or redirect)         | "..."         | "..."          | [name of change]    | No -- condition absent / Yes -- persists |

REMEDIATION_CYCLE_COMPLETE: [defect_type] -- BLOCKER_RESOLVED / BLOCKER_PERSISTS.

If BLOCKER_PERSISTS: name the specific turn where the failure condition persisted and state why the Phase 5 remediation was insufficient.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All phases as labeled sections including Phase 0, Phase 2.5, Phase 3.5, and Phase 6 (or skipped notice). Do not combine phases. Do not omit any table.

---

## V-02 -- Trigger Phrase Canonicalization

**Axis:** Output format -- Insert Phase 1.5 TRIGGER_PHRASE_CANONICALIZATION between the defect hypothesis and inventory phases. Normalizes all trigger phrases from Phase 2 candidates before collision detection. All R8 mechanisms retained; ANALYST/AUDITOR role split retained.

**Hypothesis:** All R8 mechanisms retained → C-01 through C-22 all PASS → 165/165 on v8. C-02 detects intent collisions on raw trigger phrase text. Two phrases that are lexically distinct in raw form may be semantically identical after normalization (e.g., "Cancel my order" and "order cancellation" share no raw tokens but map to the same canonical intent). Phase 1.5 normalizes all trigger phrases to lowercase token sets, collapses known synonyms, and runs collision detection on canonical forms before Phase 2 inventory is built. A C-02-passing prompt can still report zero collisions while missing synonym-level collisions visible only after canonicalization. C-23 candidate: trigger_phrase_canonicalization.

**C-16 prohibition distribution (verification):**
- Register-unique: `"These trigger phrases may cause some routing ambiguity for users"` (routing-ambiguity-without-canonical-collision-verdict); `"All ANALYST findings confirmed"` (echo-without-evidence).
- Foil-unique (Phase 1.5): `"Trigger phrases look distinct. No obvious duplicates or near-matches found."` (near-match claim without normalization table and without CANONICAL_COLLISION_VERDICT); (Phase 3): `"User greets the agent. Agent identifies the intent and fulfills the request."` (prose-trace).
- Exit-unique: `"MAY NOT emit CANONICAL_COLLISION_VERDICT: CLEAN without producing a canonical form for every Phase 2 trigger phrase"` (verdict-without-normalization); `"MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio"` (ratio-absent gate); `"MAY NOT emit REMEDIATION_CYCLE_COMPLETE without a re-trace table"` (token-without-evidence).

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
| Pre-trace hypothesis | Hypothesis table for all four defect types with predicted candidate locations before any trace phase; verdict section reconciles each prediction against findings | "Collisions might occur if topics have similar phrasing" -- no predicted node named, zero points |
| Role independence | AUDITOR states it did not author Phases 0-4; each VERIFICATION_VERDICT cites trace evidence; AUDITOR may write CHALLENGED | "All ANALYST findings confirmed" without trace citations -- echo with no independent verification |
| Coverage metrics | topic_coverage_ratio and fallback_coverage_ratio as N/N decimals; COVERAGE_GATE: CLEAN or DEGRADED with threshold comparison | "Coverage is adequate for primary scenarios" -- no ratios, no gate verdict |
| Status quo comparison | Phase 0 keyword-match trace present; STATUS_QUO_COMPARISON labels STATUS_QUO_BLIND_SPOT YES/NO per Found defect | "Status quo behavior is broadly similar -- no significant detection gaps" -- dismissed without per-defect analysis |
| Defect severity | DEFECT_SEVERITY: CRITICAL/HIGH/LOW computed with named formula per Found defect; SEVERITY_GATE: DEPLOYABLE only if zero CRITICAL defects | "This defect represents a significant risk" -- no tier token, no formula applied, no gate |
| Remediation cycle | Re-trace table shows BLOCKER node processed without failure condition; REMEDIATION_CYCLE_COMPLETE: BLOCKER_RESOLVED emitted | "Phase 6 complete -- recommended fix should resolve the issue" -- no re-trace, no token |
| Concurrent session | SESSION_ISOLATION_VERDICT: CLEAN or COLLISION; per-node SESSION_VARIABLE_CONFLICT: YES/NO | "Concurrent usage may cause issues in shared topics" -- no per-session trace, no per-node verdict |
| Canonical collision | CANONICAL_COLLISION_VERDICT: CLEAN or COLLISION_DETECTED after normalizing all trigger phrases; canonical form shown per phrase | "These trigger phrases may cause some routing ambiguity for users" -- no normalization table, no CANONICAL_COLLISION_VERDICT |

**Do not begin generating any output until you have read every row above.**

---

**Role: FLOW ANALYST**

You are a **Copilot Studio domain expert** acting as the FLOW ANALYST. You know the platform object model: topics, trigger phrases, entities (closed list, regex, system), condition branches, redirect nodes, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation, Error), and session variables (context variables, slot filling, Boolean gates).

Execute Phases 0-4 in order. Then issue ANALYST_HANDOFF to the FLOW AUDITOR.

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

A first-pass defect hypothesis would say: "The flow may have issues with fallback coverage and intent conflicts in areas where multiple topics handle similar phrasing." That prediction names no specific topic nodes and cannot be confirmed or refuted -- it is a paraphrase, not a hypothesis.

**Exit condition:** MAY NOT proceed with fewer than four rows. Each row names a specific candidate topic node and specific suspected condition, or writes "No candidate identified -- reason: [specific reason]." Note Phase 0 Ambiguous/No_match signals.

| Defect Type | Predicted Candidate Location (Topic Node) | Suspected Failure Condition | Confidence | Phase 0 Signal |
|-------------|------------------------------------------|-----------------------------|------------|----------------|
| Dead end | [specific topic node or "None suspected"] | [specific condition] | High / Low | [Turn N or "None"] |
| Infinite loop | [specific topic node or redirect entry] | [specific redirect chain] | High / Low | [Turn N or "None"] |
| Intent collision | [specific trigger phrase candidate] | [two candidate topic nodes] | High / Low | [Turn N Ambiguous or "None"] |
| Missing fallback | [specific topic node] | [no no-match branch description] | High / Low | [Turn N No_match or "None"] |

Predictions will be reconciled by the FLOW AUDITOR in Phase 5.

---

**PHASE 1.5 -- TRIGGER_PHRASE_CANONICALIZATION**

A first-pass trigger phrase review would say: "Trigger phrases look distinct. No obvious duplicates or near-matches found." That output asserts a verdict without normalizing any phrase, produces no canonical form, names no synonym group, and cannot surface collisions that exist only at the normalized level.

**Exit condition:** MAY NOT emit CANONICAL_COLLISION_VERDICT: CLEAN without producing a canonical form for every trigger phrase drawn from the Phase 1 predicted nodes AND the known Phase 2 candidates. MAY NOT write "No obvious duplicates found" -- the canonicalization table must be present even when no collisions are found; absence of the table is not evidence of absence.

Normalization rules applied:
1. Lowercase all tokens.
2. Remove punctuation and stop words (a, an, the, my, your, I, please).
3. Collapse known synonyms to a root form: cancel/cancellation -> cancel, order/purchase -> order, help/support/assist -> help, change/update/modify -> update, check/view/see/look -> check.
4. Sort tokens alphabetically. The result is the canonical form.

| Raw Trigger Phrase | Topic Node (Copilot Studio) | Canonical Form | Collision Group (if shared canonical form) |
|--------------------|----------------------------|---------------|--------------------------------------------|

CANONICAL_COLLISION_VERDICT: CLEAN if every canonical form maps to exactly one topic node. COLLISION_DETECTED if any canonical form maps to two or more topic nodes (name the canonical form and the colliding topic nodes).

If COLLISION_DETECTED: update the Phase 1 intent collision hypothesis row to note the canonical collision found, with the canonical form as evidence.

---

**PHASE 2 -- INVENTORY**

A first-pass inventory would say: "The agent includes nodes for handling common order, account, and support scenarios with standard Copilot Studio system topic integrations." That output names no individual topic nodes and hides whether any node lacks a no-match branch.

**Exit condition:** MAY NOT proceed if any table row has an empty cell. MAY NOT replace the table with a summary statement.

| Topic Node (Copilot Studio) | Trigger Phrases | No-Match Branch Defined | Reachable from Entry? |
|-----------------------------|----------------|------------------------|----------------------|

After the table: name the entry topic and all reachable terminal states. Note any canonical collisions from Phase 1.5 that affect topic nodes in this inventory.

---

**PHASE 3 -- HAPPY PATH TRACE**

A first-pass happy path trace would say: "User greets the agent. Agent identifies the intent and fulfills the request. Conversation ends normally with session state properly maintained." That output names no topic nodes, shows no utterances, writes no agent response text, and tracks no session variables -- a description of a trace, not a trace.

**Exit condition:** MAY NOT end on an active topic node. MAY NOT write "Agent responds appropriately" or leave Agent Response blank; actual message text required in every row.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1    | (entry topic)               | "..."                          | "..."                                | ...                           | var = value            |

---

**PHASE 3.5 -- CONCURRENT_SESSION_TRACE**

Trace two simultaneous sessions (Session A and Session B) through shared topic nodes from Phase 3. For each shared node, determine whether a session variable set by one session could be overwritten or misread by the other.

**Exit condition:** MAY NOT declare concurrent trace complete without one SESSION_VARIABLE_CONFLICT verdict per shared node. MAY NOT write "Concurrent usage may cause issues in shared topics" -- produce the per-session turn table.

| Turn | Topic Node (Copilot Studio) | Session A Utterance | Session A Variable State | Session B Utterance | Session B Variable State | SESSION_VARIABLE_CONFLICT |
|------|-----------------------------|--------------------|--------------------------|--------------------|--------------------------|-----------------------------|
| 1    | (shared node)               | "..."              | var = value_A            | "..."              | var = value_B            | YES / NO |

SESSION_ISOLATION_VERDICT: CLEAN if no YES rows. COLLISION if any YES row present.

---

**PHASE 4 -- EXCEPTION PATH TRACE**

A first-pass exception trace would say: "When unrecognized input is received, the agent re-prompts. If retries fail, the session escalates to a human agent." That output names no divergence node and is a paraphrase, not a trace.

**Exit condition:** MAY NOT trace the same node sequence as Phase 3. Must branch at a named topic node under a different condition. Where possible, route through the Phase 1 candidate defect node.

Label above: "Diverges from happy path at [node]: condition -- [what triggers the branch]."

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|

---

**ANALYST_HANDOFF: COMPLETE. HANDOFF_TO: FLOW AUDITOR.**

---

**Role: FLOW AUDITOR**

You are a **Copilot Studio domain expert** acting as the FLOW AUDITOR. You did not author Phases 0-4. Your verdicts are independent findings from the Phase 2 inventory and Phases 3-4 trace tables. Derive defect verdicts from trace evidence before reading the ANALYST's Phase 1 predictions. For intent collision detection, also apply Phase 1.5 canonical collision findings.

**Received ANALYST_HANDOFF: COMPLETE. Beginning independent audit.**

---

**PHASE 5 -- INDEPENDENT DEFECT SCAN + DEFECT SEVERITY + HYPOTHESIS VERIFICATION + REMEDIATION + COVERAGE + COVERAGE METRICS + STATUS_QUO_COMPARISON**

A first-pass audit would say: "All ANALYST findings confirmed. Coverage is adequate. Status quo behavior is broadly similar -- no significant detection gaps." That output echoes without verifying, provides no ratios, and dismisses the gap analysis.

**Exit condition:** MAY NOT write "All ANALYST findings confirmed" without citing trace evidence per row. MAY NOT produce fewer than four defect verdicts. MAY NOT use "possible" or "unclear." MAY NOT write "Add better error handling." MAY NOT omit a Phase 2 node from coverage. MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio. MAY NOT write "No significant gaps." MAY NOT emit SEVERITY_GATE: DEPLOYABLE without computing DEFECT_SEVERITY for each Found defect row. For intent collision detection: check both raw trigger phrases AND Phase 1.5 canonical collision findings -- a collision found only at canonical level still counts as Found. Flag each Found defect BLOCKER: Yes or No.

**Defect scan (AUDITOR independent):**

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | name or N/A | describe or "Checked N nodes -- none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect entry or N/A | describe or "Checked all chains -- none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | trigger phrase or canonical form or N/A | name both topic nodes or "No overlapping phrases or canonical forms found" | Yes / No / N/A |
| Missing fallback | Found / Not found | name or N/A | name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |

**Defect severity** (Found defects only):

Formula:
- CRITICAL: Dead_end reachable via Phase 3 happy path; OR Infinite_loop with no unconditional exit.
- HIGH: Missing_fallback on node reachable via multiple paths; OR Intent_collision with canonical form containing fewer than 3 unique root tokens.
- LOW: all other Found defects.

| Defect Type | Defect Location | Severity Formula Applied | DEFECT_SEVERITY | SEVERITY_GATE Impact |
|-------------|----------------|--------------------------|----------------|----------------------|

SEVERITY_GATE: DEPLOYABLE if zero CRITICAL. HOLD if any CRITICAL present.

**Hypothesis verification:**

| Defect Type | ANALYST Phase 1 Prediction | AUDITOR Trace Verdict | VERIFICATION_VERDICT | Discrepancy Note |
|-------------|---------------------------|----------------------|---------------------|-----------------|
| Dead end | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Infinite loop | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Intent collision | (from Phase 1; include Phase 1.5 canonical evidence) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Missing fallback | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |

**Remediation** (one row per Found defect -- CRITICAL first):

| Defect | DEFECT_SEVERITY | Topic Node (Copilot Studio) | Exact Change Required | Copilot Studio Object to Edit |
|--------|----------------|------------------------------|----------------------|-------------------------------|

**Coverage** (every Phase 2 node gets a row):

| Topic Node (Copilot Studio) | Traced (Happy) | Traced (Exception) | Untraced | Unreachable |
|-----------------------------|---------------|-------------------|----------|-------------|

**Coverage Metrics:**

| Metric | Formula | Value |
|--------|---------|-------|
| topic_coverage_ratio | N_traced (Happy OR Exception) / N_total | N/N |
| fallback_coverage_ratio | N_nodes_with_fallback_traced / N_nodes_with_no-match_branch_defined | N/N |
| intent_collision_density | N_trigger_phrase_overlaps_found (raw + canonical) / N_total_trigger_phrases | N/N |

COVERAGE_GATE: CLEAN if topic_coverage_ratio >= 0.70 AND fallback_coverage_ratio >= 0.50. Otherwise: DEGRADED.

**STATUS_QUO_COMPARISON** (Found defects only):

| Defect Type | Defect Location | FOUND_BY_FULL_TRACE | FOUND_BY_STATUS_QUO | STATUS_QUO_BLIND_SPOT | Detection Gap Explanation |
|-------------|----------------|--------------------|--------------------|----------------------|--------------------------|

---

**PHASE 6 -- REMEDIATION VERIFICATION CYCLE (Conditional)**

Entry condition: at least one Phase 5 BLOCKER: Yes. If none: "Phase 6 skipped -- no BLOCKER defects. REMEDIATION_CYCLE_COMPLETE: N/A."

A first-pass remediation verification would say: "The recommended fix addresses the root cause. After implementation, testing should confirm resolution." No re-trace, no token.

**Exit condition:** MAY NOT emit REMEDIATION_CYCLE_COMPLETE without a re-trace table showing the previously-failing turns now processing without the failure condition. MAY NOT write "Recommended fix should resolve the issue."

| Turn | Topic Node (Copilot Studio) | User Utterance | Agent Response | Remediation Applied | FAILURE_CONDITION_PRESENT |
|------|-----------------------------|---------------|----------------|---------------------|--------------------------|

REMEDIATION_CYCLE_COMPLETE: [defect_type] -- BLOCKER_RESOLVED / BLOCKER_PERSISTS.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All phases as labeled sections. Do not combine phases. Do not omit any table.

---

## V-03 -- Session Variable Lifecycle Audit

**Axis:** Lifecycle emphasis -- Expand Phase 5 with a Phase 5.5 SESSION_VARIABLE_LIFECYCLE_AUDIT that maps the full SET/READ/CLEAR sequence per variable across all traced turns and detects read-before-set (undefined read) and set-without-read (orphan set). All R8 mechanisms retained; ANALYST/AUDITOR role split retained.

**Hypothesis:** All R8 mechanisms retained → C-01 through C-22 all PASS → 165/165 on v8. C-05 tracks session variable values at turns where they change. The lifecycle audit tracks the operational sequence (SET/READ/CLEAR) across all turns to detect undefined-read risk (a variable is READ before any SET has occurred for that session) and orphan-set risk (a variable is SET but never READ, suggesting it is computed but never consumed). These ordering defects are invisible in a value-change trace because C-05 records what value a variable holds, not whether any READ precedes the first SET. A C-05-passing prompt can have a READ-before-SET defect and never detect it, because the value trace shows only the value at change time. C-23 candidate: session_variable_lifecycle.

**C-16 prohibition distribution (verification):**
- Register-unique: `"session context is maintained appropriately throughout the conversation"` (no-variable-names); `"All ANALYST findings confirmed"` (echo-without-evidence); `"Variable lifecycle looks consistent across the traced turns"` (lifecycle-asserted-without-SET-READ-CLEAR-table).
- Foil-unique (Phase 5.5): `"The session variables are set and read in a consistent order with no obvious ordering issues."` (ordering-assessed-without-lifecycle-table and without VARIABLE_LIFECYCLE_VERDICT); (Phase 3): `"User greets the agent. Agent fulfills the request."` (prose-trace).
- Exit-unique: `"MAY NOT emit VARIABLE_LIFECYCLE_VERDICT: SAFE without a lifecycle row for every named session variable from Phases 3-4"` (verdict-without-lifecycle-table); `"MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio"` (ratio-absent gate); `"MAY NOT emit REMEDIATION_CYCLE_COMPLETE without a re-trace table"` (token-without-evidence).

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
| Pre-trace hypothesis | Hypothesis table for all four defect types with predicted candidate locations before any trace phase; verdict section reconciles each prediction against findings | "Collisions might occur if topics have similar phrasing" -- no predicted node named, zero points |
| Role independence | AUDITOR states it did not author Phases 0-4; each VERIFICATION_VERDICT cites trace evidence; AUDITOR may write CHALLENGED | "All ANALYST findings confirmed" without trace citations -- echo with no independent verification |
| Coverage metrics | topic_coverage_ratio and fallback_coverage_ratio as N/N decimals; COVERAGE_GATE: CLEAN or DEGRADED with threshold comparison | "Coverage is adequate for primary scenarios" -- no ratios, no gate verdict |
| Status quo comparison | Phase 0 keyword-match trace present; STATUS_QUO_COMPARISON labels STATUS_QUO_BLIND_SPOT YES/NO per Found defect | "Status quo behavior is broadly similar -- no significant detection gaps" -- dismissed without per-defect analysis |
| Defect severity | DEFECT_SEVERITY: CRITICAL/HIGH/LOW computed with named formula per Found defect; SEVERITY_GATE: DEPLOYABLE only if zero CRITICAL defects | "This defect represents a significant risk" -- no tier token, no formula, no gate |
| Remediation cycle | Re-trace table shows BLOCKER node processed without failure condition; REMEDIATION_CYCLE_COMPLETE: BLOCKER_RESOLVED emitted | "Phase 6 complete -- recommended fix should resolve the issue" -- no re-trace, no token |
| Concurrent session | SESSION_ISOLATION_VERDICT: CLEAN or COLLISION; per-node SESSION_VARIABLE_CONFLICT: YES/NO | "Concurrent usage may cause issues in shared topics" -- no per-session trace, no per-node verdict |
| Variable lifecycle | VARIABLE_LIFECYCLE_VERDICT: SAFE or UNDEFINED_READ_RISK for every named session variable; lifecycle table showing SET/READ/CLEAR per turn | "Variable lifecycle looks consistent across the traced turns" -- no SET/READ/CLEAR table, no per-variable verdict |

**Do not begin generating any output until you have read every row above.**

---

**Role: FLOW ANALYST**

You are a **Copilot Studio domain expert** acting as the FLOW ANALYST. You know the platform object model: topics, trigger phrases, entities (closed list, regex, system), condition branches, redirect nodes, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation, Error), and session variables (context variables, slot filling, Boolean gates).

Execute Phases 0-4 in order. Then issue ANALYST_HANDOFF to the FLOW AUDITOR.

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

A first-pass defect hypothesis would say: "The flow may have issues with fallback coverage and intent conflicts in areas where multiple topics handle similar phrasing." That prediction names no specific topic nodes and cannot be confirmed or refuted.

**Exit condition:** MAY NOT proceed with fewer than four rows. Each row names a specific candidate topic node and specific suspected condition, or writes "No candidate identified -- reason: [specific reason]." Note Phase 0 Ambiguous/No_match signals.

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

**PHASE 3.5 -- CONCURRENT_SESSION_TRACE**

Trace two simultaneous sessions (Session A and Session B) through shared topic nodes from Phase 3. For each shared node, determine whether a session variable set by one session could be overwritten or misread by the other.

**Exit condition:** MAY NOT declare concurrent trace complete without one SESSION_VARIABLE_CONFLICT verdict per shared node.

| Turn | Topic Node (Copilot Studio) | Session A Utterance | Session A Variable State | Session B Utterance | Session B Variable State | SESSION_VARIABLE_CONFLICT |
|------|-----------------------------|--------------------|--------------------------|--------------------|--------------------------|-----------------------------|
| 1    | (shared node)               | "..."              | var = value_A            | "..."              | var = value_B            | YES / NO |

SESSION_ISOLATION_VERDICT: CLEAN if no YES rows. COLLISION if any YES row present.

---

**PHASE 4 -- EXCEPTION PATH TRACE**

A first-pass exception trace would say: "When unrecognized input is received, the agent re-prompts. If retries fail, the session escalates to a human agent." That output names no divergence node and is a paraphrase, not a trace.

**Exit condition:** MAY NOT trace the same node sequence as Phase 3. Must branch at a named topic node under a different condition. Where possible, route through the Phase 1 candidate defect node.

Label above: "Diverges from happy path at [node]: condition -- [what triggers the branch]."

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|

---

**ANALYST_HANDOFF: COMPLETE. HANDOFF_TO: FLOW AUDITOR.**

---

**Role: FLOW AUDITOR**

You are a **Copilot Studio domain expert** acting as the FLOW AUDITOR. You did not author Phases 0-4. Your verdicts are independent findings from the Phase 2 inventory and Phases 3-4 trace tables. Derive defect verdicts from trace evidence before reading the ANALYST's Phase 1 predictions.

**Received ANALYST_HANDOFF: COMPLETE. Beginning independent audit.**

---

**PHASE 5 -- INDEPENDENT DEFECT SCAN + DEFECT SEVERITY + HYPOTHESIS VERIFICATION + REMEDIATION + COVERAGE + COVERAGE METRICS + STATUS_QUO_COMPARISON**

A first-pass audit would say: "All ANALYST findings confirmed. Coverage is adequate. Status quo behavior is broadly similar -- no significant detection gaps." That output echoes without verifying, provides no ratios, and dismisses the gap analysis.

**Exit condition:** MAY NOT write "All ANALYST findings confirmed" without citing trace evidence per row. MAY NOT produce fewer than four defect verdicts. MAY NOT use "possible" or "unclear." MAY NOT write "Add better error handling." MAY NOT omit a Phase 2 node from coverage. MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio. MAY NOT write "No significant gaps." MAY NOT emit SEVERITY_GATE: DEPLOYABLE without computing DEFECT_SEVERITY for each Found defect row. Flag each Found defect BLOCKER: Yes or No.

**Defect scan (AUDITOR independent):**

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | name or N/A | describe or "Checked N nodes -- none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect entry or N/A | describe or "Checked all chains -- none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | trigger phrase or N/A | name both topic nodes or "No overlapping phrases found" | Yes / No / N/A |
| Missing fallback | Found / Not found | name or N/A | name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |

**Defect severity** (Found defects only):

Formula:
- CRITICAL: Dead_end reachable via Phase 3 happy path; OR Infinite_loop with no unconditional exit.
- HIGH: Missing_fallback on node reachable via multiple paths; OR Intent_collision with colliding phrase containing fewer than 3 unique keywords.
- LOW: all other Found defects.

| Defect Type | Defect Location | Severity Formula Applied | DEFECT_SEVERITY | SEVERITY_GATE Impact |
|-------------|----------------|--------------------------|----------------|----------------------|

SEVERITY_GATE: DEPLOYABLE if zero CRITICAL. HOLD if any CRITICAL present.

**Hypothesis verification:**

| Defect Type | ANALYST Phase 1 Prediction | AUDITOR Trace Verdict | VERIFICATION_VERDICT | Discrepancy Note |
|-------------|---------------------------|----------------------|---------------------|-----------------|
| Dead end | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Infinite loop | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Intent collision | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Missing fallback | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |

**Remediation** (one row per Found defect -- CRITICAL first):

| Defect | DEFECT_SEVERITY | Topic Node (Copilot Studio) | Exact Change Required | Copilot Studio Object to Edit |
|--------|----------------|------------------------------|----------------------|-------------------------------|

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

**STATUS_QUO_COMPARISON** (Found defects only):

| Defect Type | Defect Location | FOUND_BY_FULL_TRACE | FOUND_BY_STATUS_QUO | STATUS_QUO_BLIND_SPOT | Detection Gap Explanation |
|-------------|----------------|--------------------|--------------------|----------------------|--------------------------|

---

**PHASE 5.5 -- SESSION_VARIABLE_LIFECYCLE_AUDIT**

A first-pass variable review would say: "The session variables are set and read in a consistent order with no obvious ordering issues." That output asserts lifecycle safety without examining the SET/READ/CLEAR sequence per turn, names no per-variable ordering defect, and emits no VARIABLE_LIFECYCLE_VERDICT token.

**Exit condition:** MAY NOT emit VARIABLE_LIFECYCLE_VERDICT: SAFE without a lifecycle row for every named session variable from the Phase 3 and Phase 4 Session Variable Delta columns. MAY NOT write "Variable lifecycle looks consistent" -- the lifecycle table must be present even when no ordering defects are found; absence of the table is not evidence of lifecycle safety.

For each session variable named in the Phase 3 or Phase 4 Session Variable Delta column:
- Identify every turn where the variable is SET (assigned a value for the first time in this session or reassigned).
- Identify every turn where the variable is READ (used in a condition branch, response message, or redirect condition).
- Identify every turn where the variable is CLEAR (explicitly reset to null or removed).
- Flag UNDEFINED_READ_RISK if any READ turn precedes the first SET turn for that variable in the trace.
- Flag ORPHAN_SET_RISK if the variable is SET in at least one turn but READ in zero turns across the full trace.

| Session Variable | Turn | Operation (SET / READ / CLEAR) | Value at Turn | Ordering Risk |
|-----------------|------|-------------------------------|---------------|---------------|
| [var_name]      | N    | SET / READ / CLEAR            | [value]       | None / UNDEFINED_READ_RISK / ORPHAN_SET_RISK |

VARIABLE_LIFECYCLE_VERDICT: SAFE if no UNDEFINED_READ_RISK rows and no ORPHAN_SET_RISK rows. UNDEFINED_READ_RISK if any READ precedes first SET. Note: ORPHAN_SET_RISK is a warning, not a SAFE/RISK verdict gate -- report it but it does not change the VARIABLE_LIFECYCLE_VERDICT from SAFE to UNDEFINED_READ_RISK unless a READ of the orphaned variable precedes its SET.

If UNDEFINED_READ_RISK: name the specific variable, the READ turn, and the first SET turn, and add a remediation row to the Phase 5 remediation table.

---

**PHASE 6 -- REMEDIATION VERIFICATION CYCLE (Conditional)**

Entry condition: at least one Phase 5 BLOCKER: Yes. If none: "Phase 6 skipped -- no BLOCKER defects. REMEDIATION_CYCLE_COMPLETE: N/A."

A first-pass remediation verification would say: "The recommended fix addresses the root cause. After implementation, testing should confirm resolution." No re-trace, no token.

**Exit condition:** MAY NOT emit REMEDIATION_CYCLE_COMPLETE without a re-trace table showing the previously-failing turns now processing without the failure condition.

| Turn | Topic Node (Copilot Studio) | User Utterance | Agent Response | Remediation Applied | FAILURE_CONDITION_PRESENT |
|------|-----------------------------|---------------|----------------|---------------------|--------------------------|

REMEDIATION_CYCLE_COMPLETE: [defect_type] -- BLOCKER_RESOLVED / BLOCKER_PERSISTS.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All phases as labeled sections including Phase 0, Phase 3.5, Phase 5.5, and Phase 6 (or skipped notice). Do not combine phases. Do not omit any table.

---

## V-04 -- Graph Structure Review + Trigger Phrase Canonicalization

**Axis:** Role sequence + Output format -- Combines Phase 2.5 GRAPH_STRUCTURE_REVIEW by FLOW ARCHITECT (V-01) with Phase 1.5 TRIGGER_PHRASE_CANONICALIZATION (V-02). Tests additivity: ARCHITECT identifies unreachable nodes; canonicalization surfaces synonym-collision topics the ANALYST's raw-text hypothesis might miss; each token (GRAPH_STRUCTURE_VERDICT, CANONICAL_COLLISION_VERDICT) independently attributable.

**Hypothesis:** V-01 carries GRAPH_STRUCTURE_VERDICT; V-02 carries CANONICAL_COLLISION_VERDICT. Combining both: (1) an ARCHITECT-flagged unreachable node may be unreachable precisely because the only path to it uses a trigger phrase that is canonically identical to a phrase routing to a different topic -- the two mechanisms can jointly explain a reachability defect that neither alone can diagnose fully; (2) both new tokens are independently attributable -- GRAPH_STRUCTURE_VERDICT reports connectivity independently of whether any canonical collision exists, and CANONICAL_COLLISION_VERDICT is emitted before any trace or graph traversal. Additivity confirmed by independence.

**C-16 prohibition distribution (verification):**
- Register-unique: `"The conversation flow has some nodes that may not be reachable"` (no-ARCHITECT, no-verdict); `"These trigger phrases may cause some routing ambiguity"` (no-canonical-collision-verdict); `"All ANALYST findings confirmed"` (echo-without-evidence).
- Foil-unique (Phase 1.5): `"Trigger phrases look distinct. No obvious duplicates or near-matches found."` (no-normalization-table, no-CANONICAL_COLLISION_VERDICT); (Phase 2.5): `"Graph structure looks acceptable. No major structural issues identified."` (no-CONNECTED-FRAGMENTED-verdict); (Phase 3): `"User greets the agent. Agent identifies the intent and fulfills the request."` (prose-trace).
- Exit-unique: `"MAY NOT emit CANONICAL_COLLISION_VERDICT: CLEAN without a canonical form for every Phase 2 trigger phrase"` (verdict-without-normalization); `"MAY NOT emit GRAPH_STRUCTURE_VERDICT: CONNECTED without naming every reachable node"` (connectivity-without-traversal); `"MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio"` (ratio-absent gate).

Three structures each contribute at least one prohibited output not present in either of the other two. C-16 PASS condition is met.

---

**Read your scoring criteria before generating any output.**

The following table defines what earns full credit and what earns zero. Zero-point examples are specific outputs this simulation replaces -- recognize and avoid them in every phase.

| Criterion | Full credit | Zero points |
|-----------|------------|-------------|
| Dialog path traced | Complete turn-by-turn trace from entry topic to named terminal state; user intent AND agent response text in every turn | "Order Status, Account Management, and Escalation topics are covered" -- topic list with no per-turn trace |
| Defect report | All four types each with Found/Not found verdict and specific location | "No significant issues found. Consider adding error handling." -- zero points for every defect type |
| Intent-response pairing | Both user utterance and agent response text in every traced turn | Turn showing "User asks about their order" with Agent Response blank |
| Fallback handling | At least one no-match branch traced or missing-fallback defect flagged | Happy-path trace with no fallback path and no missing-fallback entry |
| Session state | Two or more named session variables with specific names and values at each change turn | "Session context is maintained appropriately" -- no variable names or values |
| Multi-path coverage | Happy path AND exception path diverging at a named node under a distinct condition | Two traces via identical node sequence labeled "Happy Path" and "Exception Path" |
| Topic graph completeness | Every topic node inventoried, each labeled traced or untraced | "The agent addresses the main user scenarios comprehensively" -- no per-node inventory |
| Copilot Studio vocabulary | Topics, trigger phrases, system topics, condition branches, redirect nodes used correctly | "Intents", "slots", "utterances" as primary labels without CS-specific equivalents |
| Actionable remediation | Topic node named and exact Copilot Studio object to change named | "Add better error handling to the affected topics" -- zero points |
| Pre-trace hypothesis | Hypothesis table for all four defect types with predicted locations before any trace; verdict section reconciles predictions | "Collisions might occur if topics have similar phrasing" -- no predicted node named |
| Role independence | AUDITOR asserts non-authorship; each VERIFICATION_VERDICT cites trace evidence; CHALLENGED available | "All ANALYST findings confirmed" without trace citations |
| Coverage metrics | topic_coverage_ratio and fallback_coverage_ratio as N/N decimals; COVERAGE_GATE verdict | "Coverage is adequate for primary scenarios" -- no ratios, no gate |
| Status quo comparison | Phase 0 keyword-match trace present; STATUS_QUO_BLIND_SPOT YES/NO per Found defect | "Status quo behavior is broadly similar" -- dismissed without per-defect analysis |
| Defect severity | DEFECT_SEVERITY: CRITICAL/HIGH/LOW per Found defect; SEVERITY_GATE: DEPLOYABLE/HOLD | "This defect represents a significant risk" -- no tier, no formula, no gate |
| Remediation cycle | Re-trace table for BLOCKER defects; REMEDIATION_CYCLE_COMPLETE: BLOCKER_RESOLVED emitted | "Recommended fix should resolve the issue" -- no re-trace, no token |
| Concurrent session | SESSION_ISOLATION_VERDICT emitted; per-node SESSION_VARIABLE_CONFLICT: YES/NO | "Concurrent usage may cause issues" -- no per-session trace, no per-node verdict |
| Canonical collision | CANONICAL_COLLISION_VERDICT after normalizing all trigger phrases; canonical form per phrase | "These trigger phrases may cause routing ambiguity" -- no normalization table, no verdict |
| Graph structure verdict | GRAPH_STRUCTURE_VERDICT: CONNECTED or FRAGMENTED by ARCHITECT forward traversal | "The flow has some nodes that may not be reachable" -- no ARCHITECT role, no verdict, no traversal |

**Do not begin generating output until you have read every row above.**

---

**Role: FLOW ANALYST**

You are a **Copilot Studio domain expert** acting as the FLOW ANALYST. Execute Phases 0-2, then issue ANALYST_INVENTORY_HANDOFF to the FLOW ARCHITECT. After the ARCHITECT completes Phase 2.5, execute Phases 3-4, then issue ANALYST_HANDOFF to the FLOW AUDITOR.

---

**PHASE 0 -- STATUS_QUO_TRACE**

A status quo trace would say: "Status quo behavior is broadly similar -- no significant gaps detected." Exit condition: MAY NOT skip. MAY NOT use condition branches, redirect nodes, or session logic. MAY NOT write "broadly similar" without naming specific turns with Ambiguous or No_match quality.

| Turn | User Utterance | Keyword(s) Matched | Agent Response (keyword match output) | SQ_MATCH_QUALITY |
|------|--------------|-------------------|---------------------------------------|-----------------|
| 1    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |
| 2    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |
| 3    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |

---

**PHASE 1 -- DEFECT HYPOTHESIS**

A first-pass hypothesis would say: "The flow may have issues with fallback coverage and intent conflicts in areas where multiple topics handle similar phrasing." Exit condition: MAY NOT proceed with fewer than four rows. Each row names a specific candidate topic node and specific suspected condition, or writes "No candidate identified -- reason: [specific reason]."

| Defect Type | Predicted Candidate Location (Topic Node) | Suspected Failure Condition | Confidence | Phase 0 Signal |
|-------------|------------------------------------------|-----------------------------|------------|----------------|
| Dead end | [specific topic node or "None suspected"] | [specific condition] | High / Low | [Turn N or "None"] |
| Infinite loop | [specific topic node or redirect entry] | [specific redirect chain] | High / Low | [Turn N or "None"] |
| Intent collision | [specific trigger phrase candidate] | [two candidate topic nodes] | High / Low | [Turn N Ambiguous or "None"] |
| Missing fallback | [specific topic node] | [no no-match branch description] | High / Low | [Turn N No_match or "None"] |

---

**PHASE 1.5 -- TRIGGER_PHRASE_CANONICALIZATION**

A first-pass trigger phrase review would say: "Trigger phrases look distinct. No obvious duplicates or near-matches found." Exit condition: MAY NOT emit CANONICAL_COLLISION_VERDICT: CLEAN without a canonical form for every trigger phrase from Phase 1 candidate nodes and known Phase 2 candidates. The table must be present even when no collisions are found.

Normalization rules: (1) lowercase; (2) remove stop words (a, an, the, my, your, I, please); (3) collapse synonyms (cancel/cancellation->cancel, order/purchase->order, help/support/assist->help, change/update/modify->update, check/view/see/look->check); (4) sort tokens alphabetically.

| Raw Trigger Phrase | Topic Node (Copilot Studio) | Canonical Form | Collision Group (if shared) |
|--------------------|----------------------------|---------------|-----------------------------|

CANONICAL_COLLISION_VERDICT: CLEAN if every canonical form maps to exactly one topic node. COLLISION_DETECTED if any canonical form maps to two or more topic nodes. If COLLISION_DETECTED: update the Phase 1 intent collision row with the canonical form as evidence.

---

**PHASE 2 -- INVENTORY**

A first-pass inventory would say: "The agent includes nodes for handling common scenarios with standard Copilot Studio system topic integrations." Exit condition: MAY NOT proceed if any row has an empty cell. MAY NOT replace the table with a summary.

| Topic Node (Copilot Studio) | Trigger Phrases | No-Match Branch Defined | Reachable from Entry? |
|-----------------------------|----------------|------------------------|----------------------|

After the table: name the entry topic and all reachable terminal states. Note any canonical collisions from Phase 1.5 affecting this inventory.

**ANALYST_INVENTORY_HANDOFF: COMPLETE. HANDOFF_TO: FLOW ARCHITECT for Phase 2.5.**

---

**Role: FLOW ARCHITECT**

You are the FLOW ARCHITECT. You did not author Phases 0-2. Your scope is exclusively graph-level structural integrity. Review the Phase 2 inventory and perform forward traversal from the named entry topic.

**Received ANALYST_INVENTORY_HANDOFF: COMPLETE. Beginning graph structure review.**

---

**PHASE 2.5 -- GRAPH_STRUCTURE_REVIEW**

A first-pass graph structure review would say: "Graph structure looks acceptable. No major structural issues identified." Exit condition: MAY NOT emit GRAPH_STRUCTURE_VERDICT: CONNECTED without naming every node reachable by forward traversal. MAY NOT emit FRAGMENTED without naming the specific disconnected subgraph and the missing redirect.

| Topic Node (Copilot Studio) | Reachable from Entry? | Reached Via (redirect or trigger) | Missing Redirect Target (if Unreachable) |
|-----------------------------|----------------------|-----------------------------------|-----------------------------------------|

GRAPH_STRUCTURE_VERDICT: CONNECTED if every Phase 2 node is Reachable. FRAGMENTED if any node is Unreachable.

If FRAGMENTED: identify whether the unreachable node's trigger phrases have a canonical collision (from Phase 1.5) that may explain why traffic is routed away from it.

**ARCHITECT_HANDOFF: COMPLETE. HANDOFF_TO: FLOW ANALYST to continue Phases 3-4.**

---

**Role: FLOW ANALYST (resumed)**

You are the FLOW ANALYST. Continue with Phases 3-4. Route traces through Reachable nodes only. Note ARCHITECT-flagged unreachable nodes in the Phase 5 coverage table.

---

**PHASE 3 -- HAPPY PATH TRACE**

A first-pass happy path trace would say: "User greets the agent. Agent identifies the intent and fulfills the request. Conversation ends normally." Exit condition: MAY NOT end on an active topic node. MAY NOT write "Agent responds appropriately" or leave Agent Response blank.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1    | (entry topic)               | "..."                          | "..."                                | ...                           | var = value            |

---

**PHASE 3.5 -- CONCURRENT_SESSION_TRACE**

Exit condition: MAY NOT declare concurrent trace complete without one SESSION_VARIABLE_CONFLICT verdict per shared node.

| Turn | Topic Node (Copilot Studio) | Session A Utterance | Session A Variable State | Session B Utterance | Session B Variable State | SESSION_VARIABLE_CONFLICT |
|------|-----------------------------|--------------------|--------------------------|--------------------|--------------------------|-----------------------------|
| 1    | (shared node)               | "..."              | var = value_A            | "..."              | var = value_B            | YES / NO |

SESSION_ISOLATION_VERDICT: CLEAN if no YES rows. COLLISION if any YES row present.

---

**PHASE 4 -- EXCEPTION PATH TRACE**

A first-pass exception trace would say: "When unrecognized input is received, the agent re-prompts. If retries fail, the session escalates to a human agent." Exit condition: MAY NOT trace the same node sequence as Phase 3. Must branch at a named topic node under a different condition.

Label above: "Diverges from happy path at [node]: condition -- [what triggers the branch]."

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|

---

**ANALYST_HANDOFF: COMPLETE. HANDOFF_TO: FLOW AUDITOR.**

---

**Role: FLOW AUDITOR**

You are the FLOW AUDITOR. You did not author Phases 0-4 or Phase 2.5. Derive all verdicts from trace evidence before reading Phase 1 predictions. For intent collision detection: apply both raw phrase matching and Phase 1.5 canonical collision findings.

**Received ANALYST_HANDOFF: COMPLETE. Beginning independent audit.**

---

**PHASE 5 -- INDEPENDENT DEFECT SCAN + DEFECT SEVERITY + HYPOTHESIS VERIFICATION + REMEDIATION + COVERAGE + COVERAGE METRICS + STATUS_QUO_COMPARISON**

A first-pass audit would say: "All ANALYST findings confirmed. Coverage is adequate. Status quo behavior is broadly similar." Exit conditions: MAY NOT write "All ANALYST findings confirmed" without citing trace evidence. MAY NOT produce fewer than four defect verdicts. MAY NOT use "possible" or "unclear." MAY NOT write "Add better error handling." MAY NOT omit a Phase 2 node from coverage. MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio. MAY NOT emit SEVERITY_GATE: DEPLOYABLE without computing DEFECT_SEVERITY for each Found defect. For intent collision: check raw AND canonical. Flag each Found defect BLOCKER: Yes or No.

**Defect scan (AUDITOR independent):**

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | name or N/A | describe or "Checked N nodes -- none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect entry or N/A | describe or "Checked all chains -- none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | trigger phrase or canonical form or N/A | name both topic nodes or "No overlapping phrases or canonical forms found" | Yes / No / N/A |
| Missing fallback | Found / Not found | name or N/A | name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |

**Defect severity** (Found defects only):

- CRITICAL: Dead_end reachable via Phase 3 happy path; OR Infinite_loop with no unconditional exit.
- HIGH: Missing_fallback on node reachable via multiple paths; OR Intent_collision with canonical form containing fewer than 3 unique root tokens.
- LOW: all other Found defects.

| Defect Type | Defect Location | Severity Formula Applied | DEFECT_SEVERITY | SEVERITY_GATE Impact |
|-------------|----------------|--------------------------|----------------|----------------------|

SEVERITY_GATE: DEPLOYABLE if zero CRITICAL. HOLD if any CRITICAL.

**Hypothesis verification:**

| Defect Type | ANALYST Phase 1 Prediction | AUDITOR Trace Verdict | VERIFICATION_VERDICT | Discrepancy Note |
|-------------|---------------------------|----------------------|---------------------|-----------------|
| Dead end | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Infinite loop | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Intent collision | (from Phase 1; include Phase 1.5 canonical evidence) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Missing fallback | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |

**Remediation** (one row per Found defect -- CRITICAL first):

| Defect | DEFECT_SEVERITY | Topic Node (Copilot Studio) | Exact Change Required | Copilot Studio Object to Edit |
|--------|----------------|------------------------------|----------------------|-------------------------------|

**Coverage** (every Phase 2 node -- mark nodes flagged Unreachable by ARCHITECT as Unreachable):

| Topic Node (Copilot Studio) | Traced (Happy) | Traced (Exception) | Untraced | Unreachable |
|-----------------------------|---------------|-------------------|----------|-------------|

**Coverage Metrics:**

| Metric | Formula | Value |
|--------|---------|-------|
| topic_coverage_ratio | N_traced (Happy OR Exception) / N_total | N/N |
| fallback_coverage_ratio | N_nodes_with_fallback_traced / N_nodes_with_no-match_branch_defined | N/N |
| intent_collision_density | N_trigger_phrase_overlaps_found (raw + canonical) / N_total_trigger_phrases | N/N |

COVERAGE_GATE: CLEAN if topic_coverage_ratio >= 0.70 AND fallback_coverage_ratio >= 0.50. Otherwise: DEGRADED.

**STATUS_QUO_COMPARISON** (Found defects only):

| Defect Type | Defect Location | FOUND_BY_FULL_TRACE | FOUND_BY_STATUS_QUO | STATUS_QUO_BLIND_SPOT | Detection Gap Explanation |
|-------------|----------------|--------------------|--------------------|----------------------|--------------------------|

---

**PHASE 6 -- REMEDIATION VERIFICATION CYCLE (Conditional)**

Entry condition: at least one Phase 5 BLOCKER: Yes. If none: "Phase 6 skipped. REMEDIATION_CYCLE_COMPLETE: N/A."

A first-pass remediation verification would say: "The recommended fix addresses the root cause. After implementation, testing should confirm resolution." Exit condition: MAY NOT emit REMEDIATION_CYCLE_COMPLETE without a re-trace table.

| Turn | Topic Node (Copilot Studio) | User Utterance | Agent Response | Remediation Applied | FAILURE_CONDITION_PRESENT |
|------|-----------------------------|---------------|----------------|---------------------|--------------------------|

REMEDIATION_CYCLE_COMPLETE: [defect_type] -- BLOCKER_RESOLVED / BLOCKER_PERSISTS.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All phases as labeled sections including Phase 0, Phase 1.5, Phase 2.5, Phase 3.5, and Phase 6. Do not combine phases. Do not omit any table.

---

## V-05 -- Full R9 Extension Ceiling

**Axis:** Full extension -- All three new R9 mechanisms on top of all R8 mechanisms: Phase 1.5 TRIGGER_PHRASE_CANONICALIZATION + Phase 2.5 GRAPH_STRUCTURE_REVIEW by FLOW ARCHITECT + Phase 5.5 SESSION_VARIABLE_LIFECYCLE_AUDIT. Evidence pool for v9 rubric.

**Hypothesis:** All three new mechanisms are independently attributable: CANONICAL_COLLISION_VERDICT is emitted after Phase 1.5 normalization and before any graph traversal or trace; GRAPH_STRUCTURE_VERDICT is emitted by the ARCHITECT after Phase 2.5 traversal and before any trace phases; VARIABLE_LIFECYCLE_VERDICT is emitted per variable in Phase 5.5 after all trace and defect phases are complete. A prompt satisfying all of V-01, V-02, and V-03 separately can still lack any one of the three without losing the other two -- each token is structurally independent. The ceiling variation also tests whether the three new mechanisms interact: a CANONICAL_COLLISION_DETECTED trigger phrase may be the one routing users away from a GRAPH_STRUCTURE_VERDICT: FRAGMENTED unreachable node; a SESSION_VARIABLE with UNDEFINED_READ_RISK may be set only in the unreachable node -- the audit can surface this cross-mechanism dependency, providing additional evidence for each token independently.

**C-16 prohibition distribution (verification):**
- Register-unique: `"session context is maintained appropriately throughout the conversation"` (no-variable-names); `"The conversation flow has some nodes that may not be reachable"` (no-ARCHITECT, no-verdict); `"These trigger phrases may cause routing ambiguity"` (no-canonical-verdict); `"All ANALYST findings confirmed"` (echo-without-evidence).
- Foil-unique (Phase 1.5): `"Trigger phrases look distinct. No obvious duplicates found."` (no-normalization-table, no-CANONICAL_COLLISION_VERDICT); (Phase 2.5): `"Graph structure looks acceptable."` (no-CONNECTED-FRAGMENTED); (Phase 5.5): `"The session variables are set and read in a consistent order."` (no-SET-READ-CLEAR-table, no-VARIABLE_LIFECYCLE_VERDICT); (Phase 3): `"User greets the agent. Agent identifies the intent. Conversation ends normally."` (prose-trace).
- Exit-unique: `"MAY NOT emit CANONICAL_COLLISION_VERDICT: CLEAN without a canonical form for every Phase 2 trigger phrase"` (verdict-without-normalization); `"MAY NOT emit GRAPH_STRUCTURE_VERDICT: CONNECTED without naming every reachable node by forward traversal"` (connectivity-without-traversal); `"MAY NOT emit VARIABLE_LIFECYCLE_VERDICT: SAFE without a lifecycle row for every named session variable"` (lifecycle-verdict-without-table); `"MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio"` (ratio-absent gate).

Four structures including three exit-unique prohibitions not shared with either of the other structures. C-16 PASS condition is met with margin.

---

**Read your scoring criteria before generating any output.**

The following table defines what earns full credit and what earns zero. Zero-point examples are specific outputs this simulation replaces -- recognize and avoid them in every phase.

| Criterion | Full credit | Zero points |
|-----------|------------|-------------|
| Dialog path traced | Complete turn-by-turn trace from entry topic to named terminal state; user intent AND agent response text in every turn | "Order Status, Account Management, and Escalation topics are covered" -- topic list with no per-turn trace |
| Defect report | All four types each with Found/Not found verdict and specific location | "No significant issues found. Consider adding error handling." -- zero points for every defect type |
| Intent-response pairing | Both user utterance and agent response text in every traced turn | Turn showing "User asks about their order" with Agent Response blank |
| Fallback handling | At least one no-match branch traced or missing-fallback defect flagged | Happy-path trace with no fallback path and no missing-fallback entry |
| Session state | Two or more named session variables with specific names and values at each change turn | "Session context is maintained appropriately" -- no variable names or values |
| Multi-path coverage | Happy path AND exception path diverging at a named node under a distinct condition | Two traces via identical node sequence labeled "Happy Path" and "Exception Path" |
| Topic graph completeness | Every topic node inventoried, each labeled traced or untraced | "The agent addresses the main user scenarios comprehensively" -- no per-node inventory |
| Copilot Studio vocabulary | Topics, trigger phrases, system topics, condition branches, redirect nodes used correctly | "Intents", "slots", "utterances" as primary labels without CS-specific equivalents |
| Actionable remediation | Topic node named and exact Copilot Studio object to change named | "Add better error handling to the affected topics" -- zero points |
| Pre-trace hypothesis | Hypothesis table for all four defect types with predicted locations before any trace; verdict section reconciles predictions | "Collisions might occur if topics have similar phrasing" -- no predicted node named |
| Role independence | AUDITOR asserts non-authorship; each VERIFICATION_VERDICT cites trace evidence; CHALLENGED available | "All ANALYST findings confirmed" without trace citations |
| Coverage metrics | topic_coverage_ratio and fallback_coverage_ratio as N/N decimals; COVERAGE_GATE verdict | "Coverage is adequate" -- no ratios, no gate |
| Status quo comparison | Phase 0 keyword-match trace; STATUS_QUO_BLIND_SPOT YES/NO per Found defect | "Status quo behavior is broadly similar" -- dismissed without per-defect analysis |
| Defect severity | DEFECT_SEVERITY: CRITICAL/HIGH/LOW per Found defect; SEVERITY_GATE: DEPLOYABLE/HOLD | "This defect represents a significant risk" -- no tier, no formula, no gate |
| Remediation cycle | Re-trace table for BLOCKER defects; REMEDIATION_CYCLE_COMPLETE: BLOCKER_RESOLVED | "Recommended fix should resolve the issue" -- no re-trace, no token |
| Concurrent session | SESSION_ISOLATION_VERDICT; per-node SESSION_VARIABLE_CONFLICT: YES/NO | "Concurrent usage may cause issues" -- no per-session trace, no per-node verdict |
| Canonical collision | CANONICAL_COLLISION_VERDICT after normalizing all trigger phrases; canonical form per phrase | "These trigger phrases may cause routing ambiguity" -- no normalization table, no verdict |
| Graph structure verdict | GRAPH_STRUCTURE_VERDICT: CONNECTED or FRAGMENTED by ARCHITECT forward traversal | "The flow has some nodes that may not be reachable" -- no ARCHITECT role, no verdict, no traversal |
| Variable lifecycle | VARIABLE_LIFECYCLE_VERDICT: SAFE or UNDEFINED_READ_RISK per variable; SET/READ/CLEAR table | "Variable lifecycle looks consistent across traced turns" -- no lifecycle table, no per-variable verdict |

**Do not begin generating output until you have read every row above.**

---

**Role: FLOW ANALYST**

You are a **Copilot Studio domain expert** acting as the FLOW ANALYST. You know the platform object model: topics, trigger phrases, entities (closed list, regex, system), condition branches, redirect nodes, system topics (Greeting, Fallback, Escalate to Agent, End of Conversation, Error), and session variables (context variables, slot filling, Boolean gates).

Execute Phases 0-2, then issue ANALYST_INVENTORY_HANDOFF to the FLOW ARCHITECT. After the ARCHITECT completes Phase 2.5, execute Phases 3-4, then issue ANALYST_HANDOFF to the FLOW AUDITOR.

---

**PHASE 0 -- STATUS_QUO_TRACE**

A status quo trace would say: "Status quo behavior is broadly similar -- no significant gaps detected." Exit condition: MAY NOT skip. MAY NOT use condition branches, redirect nodes, or session logic. MAY NOT write "broadly similar" without naming specific turns with Ambiguous or No_match quality.

| Turn | User Utterance | Keyword(s) Matched | Agent Response (keyword match output) | SQ_MATCH_QUALITY |
|------|--------------|-------------------|---------------------------------------|-----------------|
| 1    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |
| 2    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |
| 3    | "..."        | [word(s)]         | "..."                                 | Correct / Ambiguous / No_match |

---

**PHASE 1 -- DEFECT HYPOTHESIS**

A first-pass hypothesis would say: "The flow may have issues with fallback coverage and intent conflicts in areas where multiple topics handle similar phrasing." Exit condition: MAY NOT proceed with fewer than four rows. Each row names a specific candidate topic node and specific suspected condition, or writes "No candidate identified -- reason: [specific reason]."

| Defect Type | Predicted Candidate Location (Topic Node) | Suspected Failure Condition | Confidence | Phase 0 Signal |
|-------------|------------------------------------------|-----------------------------|------------|----------------|
| Dead end | [specific topic node or "None suspected"] | [specific condition] | High / Low | [Turn N or "None"] |
| Infinite loop | [specific topic node or redirect entry] | [specific redirect chain] | High / Low | [Turn N or "None"] |
| Intent collision | [specific trigger phrase candidate] | [two candidate topic nodes] | High / Low | [Turn N Ambiguous or "None"] |
| Missing fallback | [specific topic node] | [no no-match branch description] | High / Low | [Turn N No_match or "None"] |

---

**PHASE 1.5 -- TRIGGER_PHRASE_CANONICALIZATION**

A first-pass trigger phrase review would say: "Trigger phrases look distinct. No obvious duplicates or near-matches found." Exit condition: MAY NOT emit CANONICAL_COLLISION_VERDICT: CLEAN without a canonical form for every trigger phrase from Phase 1 candidate nodes and known Phase 2 candidates. Table must be present even when no collisions are found.

Normalization rules: (1) lowercase; (2) remove stop words (a, an, the, my, your, I, please); (3) collapse synonyms (cancel/cancellation->cancel, order/purchase->order, help/support/assist->help, change/update/modify->update, check/view/see/look->check); (4) sort tokens alphabetically.

| Raw Trigger Phrase | Topic Node (Copilot Studio) | Canonical Form | Collision Group (if shared) |
|--------------------|----------------------------|---------------|-----------------------------|

CANONICAL_COLLISION_VERDICT: CLEAN if every canonical form maps to exactly one topic node. COLLISION_DETECTED if any canonical form maps to two or more topic nodes. If COLLISION_DETECTED: update the Phase 1 intent collision row with the canonical form as evidence.

---

**PHASE 2 -- INVENTORY**

A first-pass inventory would say: "The agent includes nodes for handling common scenarios with standard Copilot Studio system topic integrations." Exit condition: MAY NOT proceed if any row has an empty cell. MAY NOT replace the table with a summary.

| Topic Node (Copilot Studio) | Trigger Phrases | No-Match Branch Defined | Reachable from Entry? |
|-----------------------------|----------------|------------------------|----------------------|

After the table: name the entry topic and all reachable terminal states. Note any canonical collisions from Phase 1.5 affecting this inventory.

**ANALYST_INVENTORY_HANDOFF: COMPLETE. HANDOFF_TO: FLOW ARCHITECT for Phase 2.5.**

---

**Role: FLOW ARCHITECT**

You are the FLOW ARCHITECT. You did not author Phases 0-2. Your scope is exclusively graph-level structural integrity. Review the Phase 2 inventory and entry topic. Perform forward traversal through all redirect nodes and condition branch targets.

**Received ANALYST_INVENTORY_HANDOFF: COMPLETE. Beginning graph structure review.**

---

**PHASE 2.5 -- GRAPH_STRUCTURE_REVIEW**

A first-pass graph structure review would say: "Graph structure looks acceptable. No major structural issues identified." Exit condition: MAY NOT emit GRAPH_STRUCTURE_VERDICT: CONNECTED without naming every node reachable by forward traversal. MAY NOT emit FRAGMENTED without naming the specific disconnected subgraph and the missing redirect.

| Topic Node (Copilot Studio) | Reachable from Entry? | Reached Via (redirect or trigger) | Missing Redirect Target (if Unreachable) |
|-----------------------------|----------------------|-----------------------------------|-----------------------------------------|

GRAPH_STRUCTURE_VERDICT: CONNECTED if every Phase 2 node is Reachable. FRAGMENTED if any node is Unreachable.

If FRAGMENTED: identify whether any unreachable node's trigger phrases have a canonical collision from Phase 1.5 that may explain routing failure.

If a session variable SET in Phase 3-4 belongs exclusively to an Unreachable node: note it here for Phase 5.5 VARIABLE_LIFECYCLE_AUDIT -- that variable may have an UNDEFINED_READ_RISK in the main trace because the only SET operation is unreachable.

**ARCHITECT_HANDOFF: COMPLETE. HANDOFF_TO: FLOW ANALYST to continue Phases 3-4.**

---

**Role: FLOW ANALYST (resumed)**

You are the FLOW ANALYST. Continue with Phases 3-4. Route traces through Reachable nodes only.

---

**PHASE 3 -- HAPPY PATH TRACE**

A first-pass happy path trace would say: "User greets the agent. Agent identifies the intent and fulfills the request. Conversation ends normally." Exit condition: MAY NOT end on an active topic node. MAY NOT write "Agent responds appropriately" or leave Agent Response blank.

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|
| 1    | (entry topic)               | "..."                          | "..."                                | ...                           | var = value            |

---

**PHASE 3.5 -- CONCURRENT_SESSION_TRACE**

Exit condition: MAY NOT declare concurrent trace complete without one SESSION_VARIABLE_CONFLICT verdict per shared node.

| Turn | Topic Node (Copilot Studio) | Session A Utterance | Session A Variable State | Session B Utterance | Session B Variable State | SESSION_VARIABLE_CONFLICT |
|------|-----------------------------|--------------------|--------------------------|--------------------|--------------------------|-----------------------------|
| 1    | (shared node)               | "..."              | var = value_A            | "..."              | var = value_B            | YES / NO |

SESSION_ISOLATION_VERDICT: CLEAN if no YES rows. COLLISION if any YES row present.

---

**PHASE 4 -- EXCEPTION PATH TRACE**

A first-pass exception trace would say: "When unrecognized input is received, the agent re-prompts. If retries fail, the session escalates." Exit condition: MAY NOT trace the same node sequence as Phase 3. Must branch at a named topic node under a different condition.

Label above: "Diverges from happy path at [node]: condition -- [what triggers the branch]."

| Turn | Topic Node (Copilot Studio) | Trigger Phrase / User Utterance | Agent Response (Message Node Text) | Redirect Target / System Topic | Session Variable Delta |
|------|-----------------------------|--------------------------------|--------------------------------------|-------------------------------|------------------------|

---

**ANALYST_HANDOFF: COMPLETE. HANDOFF_TO: FLOW AUDITOR.**

---

**Role: FLOW AUDITOR**

You are the FLOW AUDITOR. You did not author Phases 0-4 or Phase 2.5. Derive all verdicts from trace evidence before reading Phase 1 predictions. Apply both raw and Phase 1.5 canonical collision findings for intent collision detection.

**Received ANALYST_HANDOFF: COMPLETE. Beginning independent audit.**

---

**PHASE 5 -- INDEPENDENT DEFECT SCAN + DEFECT SEVERITY + HYPOTHESIS VERIFICATION + REMEDIATION + COVERAGE + COVERAGE METRICS + STATUS_QUO_COMPARISON**

A first-pass audit would say: "All ANALYST findings confirmed. Coverage is adequate. Status quo behavior is broadly similar." Exit conditions: MAY NOT write "All ANALYST findings confirmed" without citing trace evidence. MAY NOT produce fewer than four defect verdicts. MAY NOT use "possible" or "unclear." MAY NOT write "Add better error handling." MAY NOT omit a Phase 2 node from coverage. MAY NOT write COVERAGE_GATE: CLEAN without computing topic_coverage_ratio. MAY NOT emit SEVERITY_GATE: DEPLOYABLE without computing DEFECT_SEVERITY for each Found defect. Flag each Found defect BLOCKER: Yes or No.

**Defect scan (AUDITOR independent):**

| Defect Type | Verdict | Topic Node (Copilot Studio) | Failure Condition | Blocker? |
|-------------|---------|------------------------------|-------------------|----------|
| Dead end | Found / Not found | name or N/A | describe or "Checked N nodes -- none qualify" | Yes / No / N/A |
| Infinite loop | Found / Not found | redirect entry or N/A | describe or "Checked all chains -- none loop without exit" | Yes / No / N/A |
| Intent collision | Found / Not found | trigger phrase or canonical form or N/A | name both topic nodes or "No overlapping phrases or canonical forms found" | Yes / No / N/A |
| Missing fallback | Found / Not found | name or N/A | name the node or "All reachable nodes have no-match branches" | Yes / No / N/A |

**Defect severity** (Found defects only):

- CRITICAL: Dead_end reachable via Phase 3 happy path; OR Infinite_loop with no unconditional exit.
- HIGH: Missing_fallback on node reachable via multiple paths; OR Intent_collision with canonical form containing fewer than 3 unique root tokens.
- LOW: all other Found defects.

| Defect Type | Defect Location | Severity Formula Applied | DEFECT_SEVERITY | SEVERITY_GATE Impact |
|-------------|----------------|--------------------------|----------------|----------------------|

SEVERITY_GATE: DEPLOYABLE if zero CRITICAL. HOLD if any CRITICAL.

**Hypothesis verification:**

| Defect Type | ANALYST Phase 1 Prediction | AUDITOR Trace Verdict | VERIFICATION_VERDICT | Discrepancy Note |
|-------------|---------------------------|----------------------|---------------------|-----------------|
| Dead end | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Infinite loop | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Intent collision | (from Phase 1; include Phase 1.5 canonical evidence) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |
| Missing fallback | (from Phase 1) | Confirmed / Refuted / Inconclusive | CONFIRMED / CHALLENGED / ADDITIONAL_EVIDENCE | |

**Remediation** (one row per Found defect -- CRITICAL first; include any UNDEFINED_READ_RISK variables from Phase 5.5):

| Defect | DEFECT_SEVERITY | Topic Node (Copilot Studio) | Exact Change Required | Copilot Studio Object to Edit |
|--------|----------------|------------------------------|----------------------|-------------------------------|

**Coverage** (every Phase 2 node -- mark ARCHITECT-flagged Unreachable nodes accordingly):

| Topic Node (Copilot Studio) | Traced (Happy) | Traced (Exception) | Untraced | Unreachable |
|-----------------------------|---------------|-------------------|----------|-------------|

**Coverage Metrics:**

| Metric | Formula | Value |
|--------|---------|-------|
| topic_coverage_ratio | N_traced (Happy OR Exception) / N_total | N/N |
| fallback_coverage_ratio | N_nodes_with_fallback_traced / N_nodes_with_no-match_branch_defined | N/N |
| intent_collision_density | N_trigger_phrase_overlaps_found (raw + canonical) / N_total_trigger_phrases | N/N |

COVERAGE_GATE: CLEAN if topic_coverage_ratio >= 0.70 AND fallback_coverage_ratio >= 0.50. Otherwise: DEGRADED.

**STATUS_QUO_COMPARISON** (Found defects only):

| Defect Type | Defect Location | FOUND_BY_FULL_TRACE | FOUND_BY_STATUS_QUO | STATUS_QUO_BLIND_SPOT | Detection Gap Explanation |
|-------------|----------------|--------------------|--------------------|----------------------|--------------------------|

---

**PHASE 5.5 -- SESSION_VARIABLE_LIFECYCLE_AUDIT**

A first-pass variable review would say: "The session variables are set and read in a consistent order with no obvious ordering issues." Exit condition: MAY NOT emit VARIABLE_LIFECYCLE_VERDICT: SAFE without a lifecycle row for every named session variable from the Phase 3 and Phase 4 Session Variable Delta columns. Note any variable flagged by the ARCHITECT as SET exclusively in an Unreachable node -- that variable has UNDEFINED_READ_RISK by definition because the SET operation is unreachable.

For each named session variable:
- Map all SET / READ / CLEAR operations across Phase 3, Phase 3.5, and Phase 4 turns.
- Flag UNDEFINED_READ_RISK if any READ turn precedes the first SET turn for that variable.
- Flag ORPHAN_SET_RISK if the variable is SET but never READ across all traced turns.

| Session Variable | Turn | Operation (SET / READ / CLEAR) | Value at Turn | Ordering Risk |
|-----------------|------|-------------------------------|---------------|---------------|
| [var_name]      | N    | SET / READ / CLEAR            | [value]       | None / UNDEFINED_READ_RISK / ORPHAN_SET_RISK |

VARIABLE_LIFECYCLE_VERDICT: SAFE if no UNDEFINED_READ_RISK rows. UNDEFINED_READ_RISK if any READ precedes first SET. Report ORPHAN_SET_RISK separately as a warning; it does not change the SAFE/UNDEFINED_READ_RISK gate.

If UNDEFINED_READ_RISK: name the variable, the READ turn, the first SET turn, and add a remediation row to Phase 5 remediation table.

---

**PHASE 6 -- REMEDIATION VERIFICATION CYCLE (Conditional)**

Entry condition: at least one Phase 5 BLOCKER: Yes. If none: "Phase 6 skipped. REMEDIATION_CYCLE_COMPLETE: N/A."

A first-pass remediation verification would say: "The recommended fix addresses the root cause. After implementation, testing should confirm resolution." Exit condition: MAY NOT emit REMEDIATION_CYCLE_COMPLETE without a re-trace table for each BLOCKER defect showing the previously-failing turns now processing without the failure condition.

| Turn | Topic Node (Copilot Studio) | User Utterance | Agent Response | Remediation Applied | FAILURE_CONDITION_PRESENT |
|------|-----------------------------|---------------|----------------|---------------------|--------------------------|
| 1    | (entry or redirect)         | "..."         | "..."          | [name of change]    | No -- condition absent / Yes -- persists |

REMEDIATION_CYCLE_COMPLETE: [defect_type] -- BLOCKER_RESOLVED / BLOCKER_PERSISTS.

If BLOCKER_PERSISTS: name the specific turn where the failure condition persisted and state why the Phase 5 remediation was insufficient.

---

**Output artifact:** Write to `simulations/flow/conversation/{topic}-conversation-{date}.md`. All phases as labeled sections including Phase 0, Phase 1.5, Phase 2.5, Phase 3.5, Phase 5.5, and Phase 6 (or skipped notice). Do not combine phases. Do not omit any table.
